"""What an ``ev-*`` span states about a TDR.6 figure's basis: its currency, scale, period length
and period end (S16 A02/C02).

A located figure's ``unit``, ``currency`` and ``period_end`` are model text; the review holds each
to the source. A property is read from the cited span when the span states it, else from the
item's ``Basis:`` lines (CP-1C's ``BASIS_PREFIX``, as a peer desk prints one basis above its
figure lines). The readers are deliberately narrow: what they do not recognise is not stated, so
the figure is refused (fail closed), never given a guessed basis.
"""

import re
import unicodedata
from collections.abc import Callable, Iterable
from datetime import date
from typing import Final

from deploy_vii.quotes import normalise

# Active ISO 4217 codes (2025 list): a three-capital word of a span is a currency only if listed.
_ISO_CODES: Final = """
    AED AFN ALL AMD ANG AOA ARS AUD AWG AZN BAM BBD BDT BGN BHD BIF BMD BND BOB BRL BSD BTN BWP
    BYN BZD CAD CDF CHF CLP CNY COP CRC CUP CVE CZK DJF DKK DOP DZD EGP ERN ETB EUR FJD FKP GBP
    GEL GHS GIP GMD GNF GTQ GYD HKD HNL HTG HUF IDR ILS INR IQD IRR ISK JMD JOD JPY KES KGS KHR
    KMF KPW KRW KWD KYD KZT LAK LBP LKR LRD LSL LYD MAD MDL MGA MKD MMK MNT MOP MRU MUR MVR MWK
    MXN MYR MZN NAD NGN NIO NOK NPR NZD OMR PAB PEN PGK PHP PKR PLN PYG QAR RON RSD RUB RWF SAR
    SBD SCR SDG SEK SGD SHP SLE SOS SRD SSP STN SVC SYP SZL THB TJS TMT TND TOP TRY TTD TWD TZS
    UAH UGX USD UYU UZS VES VND VUV WST XAF XCD XCG XOF XPF YER ZAR ZMW ZWG
"""
ISO_4217: Final = frozenset(_ISO_CODES.split())
_CODE: Final = re.compile(r"(?<![A-Za-z])[A-Z]{3}(?![A-Z])")
# A symbol names its code only where it is unambiguous; any other currency symbol stands for
# itself, which no declared code equals.
_SYMBOL_CODE: Final = {"€": "EUR", "£": "GBP"}

_SCALE: Final = re.compile(
    r"\b(?i:(thousands?|millions?|mn|billions?|bn|units))\b"
    r"|(?:(?<![A-Za-z])[A-Z]{3}|[$€£¥])\s?(k|m|mn|bn)\b"
)
_SCALE_OF: Final = {
    "thousand": "thousands",
    "thousands": "thousands",
    "k": "thousands",
    "million": "millions",
    "millions": "millions",
    "mn": "millions",
    "m": "millions",
    "billion": "billions",
    "billions": "billions",
    "bn": "billions",
    "units": "units",
}

TWELVE_MONTHS: Final = "twelve months"
_OTHER_LENGTH: Final = "another period length"
_MONTHS: Final = re.compile(
    r"\b(?i:(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|[0-9]{1,2})"
    r"[ -]months?)\b"
)
_TWELVE_TAG: Final = re.compile(r"\b(?:LTM|TTM)\b")
_OTHER_PERIOD: Final = re.compile(
    r"\b(?i:quarter(?:ly|s)?|half[ -]year(?:ly)?|(?:first|second) half|interim|"
    r"year[ -]to[ -]date|weeks?)\b|\b(?:YTD|Q[1-4]|[1-4]Q|H[12])\b"
)

_MONTH_NAMES: Final = (
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
)
_MONTH: Final = (
    r"(January|February|March|April|May|June|July|August|September|October|November|December"
    r"|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sept|Sep|Oct|Nov|Dec)\.?"
)
_ISO_DATE: Final = re.compile(r"(?<![0-9])([0-9]{4})-([0-9]{2})-([0-9]{2})(?![0-9])")
_MONTH_DAY_YEAR: Final = re.compile(rf"\b{_MONTH} ([0-9]{{1,2}}),? ([0-9]{{4}})\b")
_DAY_MONTH_YEAR: Final = re.compile(rf"\b([0-9]{{1,2}}) {_MONTH},? ([0-9]{{4}})\b")


def currencies(text: str) -> frozenset[str]:
    """The ISO 4217 codes the text names (``US$`` as USD) and any other currency symbol."""
    text = text.replace("US$", " USD ")
    found = {code for code in _CODE.findall(text) if code in ISO_4217}
    for char in text:
        if unicodedata.category(char) == "Sc":
            found.add(_SYMBOL_CODE.get(char, char))
    return frozenset(found)


def scales(text: str) -> frozenset[str]:
    """The scales the text states: thousands, millions, billions or units (a word, or ``m``,
    ``mn``, ``bn``, ``k`` after a currency code or symbol)."""
    return frozenset(
        _SCALE_OF[(match.group(1) or match.group(2)).lower()] for match in _SCALE.finditer(text)
    )


def period_lengths(text: str) -> frozenset[str]:
    """``TWELVE_MONTHS`` for a twelve-month statement (``twelve months``, ``12-month``, LTM,
    TTM), another tag for any other length the text states (a quarter, a half year, nine
    months, year to date)."""
    found = {
        TWELVE_MONTHS if match.group(1).lower() in ("twelve", "12") else _OTHER_LENGTH
        for match in _MONTHS.finditer(text)
    }
    if _TWELVE_TAG.search(text):
        found.add(TWELVE_MONTHS)
    if _OTHER_PERIOD.search(text):
        found.add(_OTHER_LENGTH)
    return frozenset(found)


def _month(name: str) -> int:
    return next(i for i, full in enumerate(_MONTH_NAMES, 1) if full.startswith(name.lower()))


def _date(year: str, month: int, day: str) -> date | None:
    try:
        return date(int(year), month, int(day))
    except ValueError:
        return None


def period_ends(text: str) -> frozenset[date]:
    """The calendar dates the text states as ``2025-12-31``, ``December 31, 2025`` or
    ``31 December 2025`` (month names in full or abbreviated)."""
    found = [_date(y, int(m), d) for y, m, d in _ISO_DATE.findall(text)]
    found += [_date(y, _month(m), d) for m, d, y in _MONTH_DAY_YEAR.findall(text)]
    found += [_date(y, _month(m), d) for d, m, y in _DAY_MONTH_YEAR.findall(text)]
    return frozenset(day for day in found if day is not None)


def stated[T](read: Callable[[str], frozenset[T]], span: str, basis: Iterable[str]) -> frozenset[T]:
    """What the cited span states by ``read``; when it states nothing, what the item's ``Basis:``
    lines state together."""
    own = read(normalise(span))
    if own:
        return own
    return frozenset(item for line in basis for item in read(normalise(line)))
