"""S16 C10: a redirect may leave the scheme-default port only for the origin the manifest named."""

from collections.abc import Mapping

import pytest

from deploy_workflow.research import webfetch

HOST = "example.com"


class _Response:
    def __init__(self, status: int, headers: Mapping[str, str], body: bytes) -> None:
        self.status, self.headers, self.body = status, headers, body

    def getheader(self, name: str, default: str | None = None) -> str | None:
        return self.headers.get(name, default)

    def read(self, amt: int) -> bytes:
        out, self.body = self.body[:amt], self.body[amt:]
        return out


class _Connection:
    """Answers the first request of a fetch with the redirect (if any), later ones with 200."""

    def __init__(self, location: str | None, first: bool) -> None:
        self.location, self.first = location, first

    def request(self, method: str, url: str, *, headers: Mapping[str, str]) -> None:
        return None

    def getresponse(self) -> _Response:
        if self.location is not None and self.first:
            return _Response(302, {"Location": self.location}, b"")
        return _Response(200, {"Content-Type": "text/plain"}, b"landed")

    def close(self) -> None:
        return None


def _fetch(
    url: str, location: str | None
) -> tuple[list[tuple[str, int]], str | None, bytes | None]:
    seen: list[tuple[str, int]] = []

    def connect(target: webfetch.ConnectionTarget) -> _Connection:
        seen.append((target.host, target.port))
        return _Connection(location, first=len(seen) == 1)

    record, body, _media = webfetch.fetch(
        url,
        manifest_hosts=frozenset({HOST}),
        resolver=lambda _host: ["93.184.216.34"],
        connect=connect,
        cap=1000,
        clock=lambda: 0.0,
    )
    return seen, record.reason, body


# Hand-derived: only the first connection (443) happens when the redirect is refused.
@pytest.mark.parametrize(
    "location",
    [
        f"https://{HOST}:8443/admin",
        f"https://{HOST}:80/x",
        f"http://{HOST}:8080/x",
        f"https://{HOST}:444/x",
        f"https://{HOST.upper()}:8443/x",
    ],
)
def test_redirect_to_another_port_is_refused(location: str) -> None:
    seen, reason, body = _fetch(f"https://{HOST}/a", location)
    assert seen == [(HOST, 443)]
    assert body is None and reason is not None and "refused" in reason


@pytest.mark.parametrize("location", [f"https://{HOST}:443/b", f"https://{HOST}/b", "/b"])
def test_redirect_to_the_default_port_is_followed(location: str) -> None:
    seen, reason, body = _fetch(f"https://{HOST}/a", location)
    assert seen == [(HOST, 443), (HOST, 443)]
    assert reason is None and body == b"landed"


def test_redirect_to_the_origin_the_manifest_named_is_followed() -> None:
    # The manifest url itself names :8443, so that exact origin may be redirected to.
    seen, reason, body = _fetch(f"https://{HOST}:8443/a", f"https://{HOST}:8443/b")
    assert seen == [(HOST, 8443), (HOST, 8443)] and reason is None and body == b"landed"


def test_redirect_from_a_named_port_to_another_port_is_refused() -> None:
    seen, reason, body = _fetch(f"https://{HOST}:8443/a", f"https://{HOST}:9443/b")
    assert seen == [(HOST, 8443)] and body is None and reason is not None


def test_redirect_to_an_ipv6_literal_with_a_port_is_refused() -> None:
    seen, reason, body = _fetch(f"https://{HOST}/a", "https://[2001:db8::1]:8443/x")
    assert seen == [(HOST, 443)] and body is None and reason is not None
