#!/usr/bin/env python3
"""test_validate_claims.py — validate-claims.py 회귀 (R1 I-1, Codex 20회차: 음수·누락·manifest 불일치)."""
import importlib.util
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "vc", os.path.join(HERE, "validate-claims.py"))
vc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vc)

FM = """---
title: t
citation_status: verified
claims_total: {tot}
claims_attached: {att}
claims_dropped: {drp}
claims_source_needed: {sn}
claims_basis: {basis}
has_source_needed: {hsn}
---
body
"""


def note(tot=10, att=7, drp=2, sn=1, basis="legacy-ledger", hsn="true"):
    return FM.format(tot=tot, att=att, drp=drp, sn=sn, basis=basis, hsn=hsn)


def run(text):
    errors = []
    vc.check_note("X.md", text, errors)
    return errors


def test_ok():
    assert run(note()) == []


def test_arithmetic():
    errs = run(note(tot=11))
    assert any("산술 불일치" in e for e in errs), errs


def test_negative():
    errs = run(note(att=-1, tot=2))
    assert any("음수" in e for e in errs), errs


def test_missing_field():
    text = note().replace("claims_dropped: 2\n", "")
    errs = run(text)
    assert any("누락" in e for e in errs), errs


def test_hsn_mismatch():
    errs = run(note(hsn="false"))  # sn=1 인데 false
    assert any("정합 위반" in e for e in errs), errs
    errs2 = run(note(sn=0, drp=3, hsn="true"))  # sn=0 인데 true
    assert any("정합 위반" in e for e in errs2), errs2


def test_bad_basis():
    errs = run(note(basis="whatever"))
    assert any("claims_basis" in e for e in errs), errs


def test_manifest_missing():
    errs = run(note(basis="claim-manifest"))
    assert any("manifest 미실존" in e for e in errs), errs


def test_manifest_counts_and_dup():
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "m.yml")
        with open(p, "w", encoding="utf-8") as f:
            f.write("# disposition: attached | dropped 주석은 미계수\n")
            f.write("claims:\n")
            f.write("  - {id: c1, claim: a, disposition: attached, anchor: x}\n")
            f.write("  - {id: c2, claim: b, disposition: dropped, anchor: y}\n")
            f.write("  - {id: s1, claim: c, disposition: source-needed, anchor: z}\n")
        counts, err = vc.manifest_counts(p)
        assert err is None and counts == {"attached": 1, "dropped": 1, "source-needed": 1}, (counts, err)
        with open(p, "a", encoding="utf-8") as f:
            f.write("  - {id: c1, claim: dup, disposition: attached, anchor: w}\n")
        counts, err = vc.manifest_counts(p)
        assert err and "중복" in err, (counts, err)


if __name__ == "__main__":
    fails = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"  ok: {name}")
            except AssertionError as e:
                fails += 1
                print(f"  FAIL: {name} — {e}")
    print(f"[test_validate_claims] {'FAIL' if fails else 'OK'} ({fails} failures)")
    sys.exit(1 if fails else 0)
