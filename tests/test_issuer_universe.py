"""Issuer universe from N-PORT holdings.

The retained LQD filing is real. Its expected counts and sums come from a separate regex reading of
the raw XML, not from the module's parser. The small loan filing below is synthetic: it covers
loan, missing-LEI, default, restricted and missing-value cases the LQD filing does not contain.
"""

import json
import re
from decimal import Decimal
from pathlib import Path

from deploy_workflow.issuer_universe import main, universe

ROOT = Path(__file__).resolve().parents[1]
LQD = ROOT / "runs/lqd-portfolio-001/sources/LQD-20250531-NPORT.xml"
JPMORGAN = "8I5DZWZKVSZI1NUHU748"


def test_real_filing_counts_and_sums_match_an_independent_reading():
    raw = LQD.read_bytes()
    blocks = re.findall(rb"<invstOrSec>(.*?)</invstOrSec>", raw, re.DOTALL)
    corporate_debt = [
        b
        for b in blocks
        if b"<assetCat>DBT</assetCat>" in b
        and not re.search(rb"<issuerCat>(UST|USGA|USGSE|MUN|NUSS|PF|RF)</issuerCat>", b)
    ]
    jpm = sum(
        Decimal(re.search(rb"<valUSD>([^<]+)</valUSD>", b)[1].decode())
        for b in corporate_debt
        if f"<lei>{JPMORGAN}</lei>".encode() in b
    )
    result = universe({LQD.name: raw})
    (fund,) = result["funds"]
    assert fund["holdings"] == len(blocks) == 2910
    assert fund["kept"] == {"bond": len(corporate_debt)}
    assert sum(result["excluded_holdings"].values()) == len(blocks) - len(corporate_debt)
    assert sum(i["holdings"] for i in result["issuers"]) == len(corporate_debt)
    (entry,) = (i for i in result["issuers"] if i["key"] == JPMORGAN)
    held = entry["funds"]["iShares iBoxx $ Investment Grade Corporate Bond ETF"]
    assert Decimal(held["value_usd"]) == jpm
    assert held["holdings"] == sum(f"<lei>{JPMORGAN}</lei>".encode() in b for b in corporate_debt)
    assert all(i["sec_registrant"] is None for i in result["issuers"])


def nport(series: str, *holdings: str) -> bytes:
    return (
        '<edgarSubmission xmlns="http://www.sec.gov/edgar/nport"><formData><genInfo>'
        f"<regName>Synthetic Trust</regName><regCik>0000000001</regCik>"
        f"<seriesName>{series}</seriesName><seriesId>S000000001</seriesId>"
        "<repPdDate>2026-06-30</repPdDate></genInfo><invstOrSecs>"
        + "".join(holdings)
        + "</invstOrSecs></formData></edgarSubmission>"
    ).encode()


def holding(name, lei, asset, value, *, cat="CORP", default="N", restricted="N"):
    value_tag = f"<valUSD>{value}</valUSD>" if value is not None else ""
    return (
        f"<invstOrSec><name>{name}</name><lei>{lei}</lei><cusip>123456AB7</cusip>"
        f"{value_tag}<assetCat>{asset}</assetCat><issuerCat>{cat}</issuerCat>"
        f"<invCountry>US</invCountry><isRestrictedSec>{restricted}</isRestrictedSec>"
        f"<debtSec><maturityDt>2030-01-15</maturityDt><isDefault>{default}</isDefault></debtSec>"
        "</invstOrSec>"
    )


def test_bonds_and_loans_join_by_lei_and_flags_are_kept():
    lei = "ABCDEFGHIJKLMNOPQRST"
    bonds = nport(
        "Synthetic High Yield ETF",
        holding("Casino Co", lei, "DBT", "100.50", restricted="Y"),
        holding("No Lei Corp", "N/A", "DBT", "5", default="Y"),
        holding("US Treasury", "N/A", "DBT", "999", cat="UST"),
    )
    loans = nport(
        "Synthetic Loan ETF",
        holding("CASINO CO TL B", lei, "LON", "20"),
        holding("No Lei Corp", "N/A", "LON", None),
    )
    result = universe({"hy.xml": bonds, "loan.xml": loans})
    by_key = {i["key"]: i for i in result["issuers"]}
    casino = by_key[lei]
    assert casino["bonds_and_loans"] and casino["restricted_holdings"] == 1
    assert casino["funds"]["Synthetic High Yield ETF"]["value_usd"] == "100.50"
    assert casino["names"] == ["CASINO CO TL B", "Casino Co"]
    no_lei = by_key["name:NO LEI CORP"]
    assert no_lei["holdings_in_default"] == 1 and no_lei["bonds_and_loans"]
    # A missing value is counted as missing and never shown as zero.
    assert no_lei["funds"]["Synthetic Loan ETF"] == {
        "holdings": 1,
        "value_usd": None,
        "values_missing": 1,
    }
    assert result["excluded_holdings"] == {"DBT / UST": 1}
    assert result["issuers"][0]["key"] in {lei, "name:NO LEI CORP"}  # held by both funds


def test_cli_writes_once_and_refuses_a_non_nport_file(tmp_path, capsys):
    out = tmp_path / "universe.json"
    assert main(["--nport", str(LQD), "--out", str(out)]) == 0
    assert json.loads(out.read_text())["schema"] == "issuer-universe/1"
    assert "issuers: 497" in capsys.readouterr().out
    assert main(["--nport", str(LQD), "--out", str(out)]) == 2
    bad = tmp_path / "not-nport.xml"
    bad.write_text("<root/>")
    assert main(["--nport", str(bad), "--out", str(tmp_path / "other.json")]) == 2
    assert "genInfo" in capsys.readouterr().err
