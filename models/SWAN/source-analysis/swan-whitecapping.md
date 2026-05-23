---
title: "swan whitecapping"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-whitecapping.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How SWAN dispatches whitecapping (Sds) via `GEN1/GEN2/GEN3` and the four sub-options Komen / Janssen / Westhuysen / ST6, what the actual default is in this version (Westhuysen, **not Komen**), how `IWIND/IWCAP` integer codes map to formulations, the formulae implemented in `SWCAP` and `SWCAP8`, the wind-input pairing requirements (Janssen wind ↔ Janssen whitecapping; Yan wind ↔ Westhuysen), where Sds enters the action balance via `IMATDA`, and the recommended choices per code-comment guidance ("we prefer GEN3 BABANIN"). Use this when calibrating wave dissipation, debugging GEN3 sub-option mismatches, or interpreting CDS2 vs CDSV vs A1SDS parameters.

**Note**: source-term assembly is in `SOURCE` subroutine of `swancom1.ftn` (no `sources.f` file in this tree).

## Source basis

- `swanmain.ftn:1110-1112, 1340-1491` — defaults, `IGEN=3, IQUAD=2, IWCAP=7`.
- `swanpre1.ftn:2461-3088` — GEN dispatch, parameter parsing.
- `swmod1.ftn:2295-2300, 2728` — `IWCAP` codes.
- `swancom1.ftn:7287-7511` — Sds insertion in source-term assembly.
- `swancom2.ftn:2290-2897` — `SWCAP` (Komen, Janssen, Westhuysen).
- `swancom3.ftn:1907-2860` — wind-input formulas.
- `SdsBabanin.ftn90:44-256` — ST6/Babanin.

## A. GEN dispatch

**Default state** in this version (`swanmain.ftn:1110-1112`):
```
IGEN=3, IQUAD=2, IWCAP=7
```
So default is **Westhuysen / Alves-Banner**, not Komen.

| Command | Effect |
|---|---|
| `GEN1` | First-gen wind, **disables quadruplets and whitecapping** (`swanpre1.ftn:2808-2814`) |
| `GEN2` | Second-gen wind, disables quadruplets and whitecapping (`:2843-2849`) |
| `GEN3 KOM` | `IWIND=3, IWCAP=1` (Komen) (`:3036-3040`) |
| `GEN3 JANS` | `IWIND=4, IWCAP=2` (Janssen / WAM Cycle 4) (`:2908-2912`) |
| `GEN3 WESTH` | `IWIND=5, IWCAP=7` (Yan + Alves-Banner / Westhuysen, default) (`:2935-2940`) |
| `GEN3 ST6` | `IWIND=8, IWCAP=8` (Babanin/Rogers ST6) (`:2983-2991`) |
| `GEN4` | Shallow-water; **disables wind, quadruplets, whitecapping** (`:3074-3088`) |

## B. Komen (IWCAP=1)

`IWCAP=1` = "standard WAM formulation (Komen et al., 1984)" (`swmod1.ftn:2295-2297`).

Inputs: `CDS2, STPM, POWST, DELTA, POWK` (`swanpre1.ftn:2461-2472`).

Defaults (`swanmain.ftn:1340-1345`):
- `PWCAP(1) = 2.36e-5` (CDS2).
- `PWCAP(2) = 3.02e-3` (STPM).
- `PWCAP(9) = 2` (POWST).
- `PWCAP(10) = 1` (DELTA).
- `PWCAP(11) = 1` (POWK).

Formula (comments):
```
S_wc(σ, θ) = -C_wc · E(σ, θ)
C_K = C1 · [(1−δ) + δ(k/k̄)^n1] · (S̄/S_PM)^n2
```
(`swancom2.ftn:2290-2303`).

Implementation (`:2485-2614`):
```
STP_OV = KM_WAM * sqrt(ETOT)
STP_PM = sqrt(PWCAP(2))
N1 = PWCAP(11), N2 = 2*PWCAP(9)
WCAP(IS) = C_K(IS) * SIGM_10 * (KWAVE(IS,1)/KM_WAM)
```

**`CDSV` is NOT a Komen parameter** — it's used by Babanin/swell physics (`swmod1.ftn:2728`, `swanmain.ftn:1382`).

## C. Janssen / WAM Cycle 4 (IWCAP=2)

`IWCAP=2` = Janssen whitecapping (`swmod1.ftn:2298-2300`).

`GEN3 JANS` reads `CDS1` and `DELTA`, maps into generalized Komen coefficients used by `SWCAP`:
```
PWCAP(1) = PWCAP(3) * (PWCAP(2)^PWCAP(9))
PWCAP(10) = PWCAP(4)
```
(`swanpre1.ftn:2912-2919`).

Defaults: `CFJANS=4.5, DELTA=0.5` (`swanmain.ftn:1350-1351`).

**Consistency check**: WAM Cycle 4 requires Janssen wind input with Janssen whitecapping (`swanmain.ftn:6440-6444`).

## D. Westhuysen / Saturation-based (IWCAP=7, default)

`GEN3 WESTH` uses Yan wind input + Alves-Banner whitecapping (`swanpre1.ftn:2935-2940`).

Defaults: `CDS2=5.0e-5, BR=1.75e-3` (`:2941-2942`).

In `SWCAP`, this is "Alves and Banner (2003)" (`swancom2.ftn:2536-2538`).

Saturation-based formula (`:2573-2592`):
```
B = (1/2π) · CG · k³ · E(f)                      ! saturation
FBR = 0.5 · (1 + tanh(10·(√(B/BRKD) − 1)))       ! breaking fraction
P = 3 + tanh(25.76·(u*·k/σ − 0.1))               ! exponent
```
Final rate blends saturation dissipation with Komen fallback (`:2590-2592`).

**Requires Yan wind** when `IWCAP=7` (`swanmain.ftn:6426-6428`).

## E. ST6 / Babanin (IWCAP=8)

`GEN3 ST6` sets Babanin/Rogers wind input + whitecapping (`swanpre1.ftn:2983-2991`).

Parameters: `A1SDS, A2SDS, P1SDS, P2SDS` (defaults: `2.8e-6, 3.5e-5, 4, 4`) (`swanpre1.ftn:2992-2995`, `swanmain.ftn:1376-1380`).

Globally initialized: `UPWARDS=.TRUE.` (`swanmain.ftn:1380`).

ST6 wind options (`swanpre1.ftn:3003-3027`):
- `HWANG, FAN, ECMWF` (drag formula).
- `VECTAU, SCATAU` (vector vs scalar tau).
- `TRUE10, U10P` (true 10-m vs proxy).
- Optional `DEB CDFAC`.

`SWCAP8` calls `CALC_SDS` (`swancom2.ftn:2693-2859`).

`CALC_SDS` defines `KDS = Sds/E(f) = T1 + T2` (`SdsBabanin.ftn90:44-53`):
```
T1 = A1SDS * f * ANAR * NDEDENS^P1SDS         (inherent breaking)
T2 = A2SDS * ASUM                              (cumulative)
KDS = T1 + T2
```
(`SdsBabanin.ftn90:225-256`).

## F. CDS2 / wind-input relations

For Komen/Snyder:
- Snyder-Komen wind input combined with Komen dissipation (`swancom3.ftn:1907-1911`).
- Coefficient: `B = max(0, 0.25·ρ_aw·(28U*·cos/(σ/k) − 1))·σ` (`:1918-1927`).
- Implemented as (`:2043-2059`):
```
TEMP1 = 0.25 * PWIND(9)
TEMP2 = 28 * UFRIC
SWINEB = TEMP1 * (TEMP3 * COSDIF − 1)
SWINEB = max(0, SWINEB * sigma)
```

For Westhuysen, Yan coefficients modified when `IWCAP=7` (`:2854-2860`).

## G. Where Sds enters action balance

`SOURCE` subroutine in `swancom1.ftn` initializes `IMATRA, IMATDA` (`:7287-7293`).

Order:
1. Wind input assembled first (`:7410-7480`).
2. Whitecapping called if `IWCAP >= 1` (`:7502-7511`):
   - `IWCAP <= 7` → `SWCAP`.
   - `IWCAP = 8` → `SWCAP8`.

`SWCAP` adds dissipation to matrix diagonal `IMATDA` and output dissipation bucket (`swancom2.ftn:2637-2646`); `SWCAP8` analogous for ST6 (`:2887-2897`).

## H. Defaults / recommendations

Source-code default: **`GEN3 WESTH`** (`IWCAP=7`).

Defaults table:

| Option | Parameters |
|---|---|
| Komen | CDS2=2.36e-5, STPM=3.02e-3, POWST=2, DELTA=1, POWK=1 |
| WESTH | CDS2=5.0e-5, BR=1.75e-3 |
| ST6 | A1SDS=2.8e-6, A2SDS=3.5e-5, P1=P2=4, CDSV=1.2, WNDSCL=32, VECTOR_TAU=T, TRUE_U10=F |

Code's explicit recommendation: **"We prefer that you use GEN3 BABANIN"** (`swanpre1.ftn:3031-3034`).

## Decision Guide

| Application | Recommendation |
|---|---|
| Default / general use | `GEN3 WESTH` (current default) |
| Best-tested production | `GEN3 BABANIN` (per source comment) |
| Hindcast comparison with WAM Cycle 4 | `GEN3 JANSSEN` |
| Reproducing legacy SWAN papers | `GEN3 KOMEN` |
| Shallow water / coastal | `GEN4` (disables open-ocean physics; uses wave-induced breaking only) |
| Korean coastal hindcast | `GEN3 WESTH` (default) or `GEN3 ST6` (if validated) |
| Tuned single-site case | Adjust `CDS2` (Westh) or `A1SDS, A2SDS` (ST6) |

## Working Rules

- Default is **Westhuysen**, not Komen — explicitly set `GEN3 KOM` if you want Komen.
- ST6 (`GEN3 ST6 BABANIN`) is the most modern; recommended for new applications per source comment.
- Pair wind input with consistent whitecapping (Janssen-Janssen, Yan-Westhuysen, Babanin-Babanin); SWAN enforces.
- For `GEN1/GEN2`, whitecapping and quadruplets are **disabled**; useful only for first-gen / DIA-free benchmarks.
- For `GEN4` (shallow), no open-ocean physics; use only when domain is purely surf-zone.
- Output Sds dissipation via `BLOCK DISWCAP` for diagnostic.

## Common Pitfalls

- ▢ Setting `GEN3 KOM` thinking it's the default — actual default is `WESTH`.
- ▢ Using `GEN3 KOM` with Janssen wind input — enforced inconsistency, runtime warning.
- ▢ Confusing `CDS2` (whitecapping) with `CDSV` (swell, Babanin physics).
- ▢ Adjusting `A1SDS/A2SDS` in `GEN3 WESTH` run — those are ST6 parameters, ignored.
- ▢ Expecting whitecapping with `GEN1/GEN2` — disabled.
- ▢ Cold-start `GEN3 ST6` with very short spin-up — Babanin cumulative term needs ~1 day to spin up.
- ▢ Not pairing `GEN3 ST6` with `BABANIN` or `WAVE_BREAKING` — incomplete physics.

## Next expansion

- Quantitative comparison Komen vs Westhuysen vs ST6 on identical buoy-validation case.
- ST6 wind-input drag formula details (HWANG / FAN / ECMWF).
- WAM Cycle 4 (Janssen) historical context.

## References

- Komen et al. 1984 (whitecapping baseline).
- Janssen 1991 (WAM Cycle 4).
- van der Westhuysen et al. 2007 (saturation-based).
- Babanin & Young 2005 (cumulative dissipation, ST6).
- Rogers et al. 2012 (ST6 implementation in SWAN).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/swan/source_code/swan/src`. Auto-draft = false; review_required = true.
