"""Free module-scoped stores during a run that keeps only failed tests' temporary directories.

`tmp_path_retention_policy=failed` (set by tools/nightly_tests.py) removes a passing test's
`tmp_path` at once, but pytest removes what `tmp_path_factory.mktemp` made (the module fixtures
holding a workflow store of about 120 MB) only when the whole session passes. This drops a
module's directories when the module ends with no new failure. With the default policy nothing
changes.
"""

from __future__ import annotations

import shutil
from collections.abc import Iterator

import pytest


@pytest.fixture(scope="module", autouse=True)
def _drop_passing_module_dirs(request: pytest.FixtureRequest) -> Iterator[None]:
    factory = request.config._tmp_path_factory  # type: ignore[attr-defined]
    if request.config.getini("tmp_path_retention_policy") != "failed":
        yield
        return
    base = factory.getbasetemp()
    before = {path for path in base.iterdir() if not path.is_symlink()}
    failed = request.session.testsfailed
    yield
    if request.session.testsfailed == failed:
        for path in set(base.iterdir()) - before:
            if not path.is_symlink():
                shutil.rmtree(path, ignore_errors=True)
