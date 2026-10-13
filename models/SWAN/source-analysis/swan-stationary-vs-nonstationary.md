---
title: "swan stationary vs nonstationary"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-stationary-vs-nonstationary.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시. 2026-10-13 recovery 대조 보고서 R1–R8 반영"
last_source_check: "2026-10-13 (recovery 대조 반영)"
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How SWAN dispatches between stationary (`MODE STAT`) and non-stationary (`MODE NONST/DYN`) computation, the relationship between intent (`NSTATM`) and actual computation (`NSTATC`), the four-quadrant Gauss-Seidel sweep order (WS-SE-EN-NW), how `MXITST` (default 50) vs `MXITNS` (default 1) iteration limits work, the convergence test (`STOPC`/`ACCUR`/`PNUMS`), the propagation scheme dispatch (`PROPSC=1` BSBT, `2` SORDUP, `3` S&L), how the time-derivative enters the transport matrix only in non-stationary mode, and the memory implications for AC1/AC2 storage. Use this when picking a mode for a domain, debugging stationary convergence, or estimating memory for long unstructured runs.

## Source basis

- `swanpre1.ftn:738-936, 791-795, 1913-1979, 4007-4554` — `MODE`, `COMPUTE`, `NUMERIC STOPC/ACCUR`, propagation flags.
- `swanmain.ftn:266-693, 493-628, 1092-1095, 6889-6904` — main loop, AC1/AC2 alloc, sweep dispatch.
- `swancom1.ftn:724-2356, 5393-5411, 9618-9928` — sweep order, accuracy tests, `STRSXY/SACCUR/SWSTPC`.
- `swancom5.ftn:2148-2904, 2629-2700` — propagation scheme implementations.
- `swmod1.ftn:2272-2403, 2869-2874` — defaults, `PROPSC` codes.
- `swmod2.ftn:990-1028` — AC2 storage.
- `SwanCompUnstruc.ftn90:777-1077`, `SwanVertlist.ftn90:48-217` — unstructured.

## A. Top-level dispatch

`MODE` sets intent (`swanpre1.ftn:738-752`):
- `MODE NONST/DYN` → `NSTATM=1`.
- `MODE STAT` → `NSTATM=0`.

`COMPUTE` sets actual computation (`:879-936`):

| Mode | Settings |
|---|---|
| Stationary | `DT=1e10, RDTIM=0, NSTATC=0, MTC=1` |
| Non-stationary | Reads `tbeg, DELTC, tend`; `NSTATC=1, RDTIM=1/DT`, computes `MTC` |

Iteration limits: `ITERMX = MXITST` for stationary, `MXITNS` for non-stationary (`:930-936`).

`SWMAIN` runs time-step loop `DO 500 IT = IT0, MTC` (`swanmain.ftn:571`):
- Stationary: `IT0=1`.
- Non-stationary: `IT0=0` for initial conditions (`:544-559`).

Structured grids → `SWCOMP`; unstructured → `SwanCompUnstruc` (`:610-628`). Time advances only for non-stationary (`:686-695`).

## B. Stationary iteration

Defaults: `MXITST=50, MXITNS=1, ITERMX=MXITST` (`swanmain.ftn:1092-1095`).

`NUMERIC STOPC/ACCUR` parses convergence tolerances + `NPNTS` + max iterations (`swanpre1.ftn:1913-1979`).

Default `PNUMS` (`swmod1.ftn:2393-2403`):
- Relative Hs/Tm01.
- Absolute Hs/Tm01.
- Required percent wet points.

Structured stationary: `DO 450 ITER = 1, ITERMX` (`swancom1.ftn:1487`):
- `ACCUR` mode → calls `SACCUR`.
- `STOPC` mode → calls `SWSTPC` (`:2270-2284`).

Termination: `ACCUR >= PNUMS(4)`, with guard preventing `STOPC` from stopping on iteration 1 (`:2349-2356`).

구조 격자의 TMREL은 TMABS/SACC2로 계산된다. SACC2는 평균 각주파수다. 같은 출력의 주기 정규화와 단위가 다르므로 코드 결함 후보로 기록한다. 기본 DTABS=1000은 이 차이를 가릴 수 있다. `src/swancom1.ftn:9855`의 원문은 `TMREL = TMABS / SACC2(INDX)`이다. `src/swancom1.ftn:9873`의 `IF ( IQCM.EQ.0 ) THEN`에 속한 주기 판정이 TMREL을 사용한다. QC 분기는 이 값을 합격 조건에 쓰지 않는다. `b2ae30e`(2022-08-10, 저장소 최초 반입)부터 같은 식이 남는다. [R5:PN-085 수정안](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#4-노트-대조와-수정안), [코드 결함 후보 표](swan-foundation.md#코드-결함-후보-정적-판독).

## C. Stationary sweeping (4-quadrant Gauss-Seidel)

Comments define 4 sweep directions WS-SE-EN-NW (`swancom1.ftn:724-740`).

Documented order (`:761-793`):
1. `KSX=−1, KSY=−1`, forward `IX/IY` (sweeping toward NE).
2. `KSX=+1, KSY=−1`, reverse `IX`, forward `IY` (toward NW).
3. `KSX=+1, KSY=+1`, reverse both (toward SW).
4. `KSX=−1, KSY=+1`, forward `IX`, reverse `IY` (toward SE).

Executable sweep-direction branches at `swancom1.ftn:1741-1817`. Each grid point calls `SWOMPU` for actual solve (`:2000-2033`).

This means **each iteration solves all four sweeps**; convergence requires multiple iterations until all directional information has propagated through the domain.

## D. Non-stationary time stepping

Wraps same sweep machinery inside explicit time steps:
1. `SNEXTI` updates BC/input (`swanmain.ftn:586-595`).
2. `SWCOMP` / `SwanCompUnstruc` computes (`:610-628`).
3. `TIMCO` advances by `DT` (`:686-695`).

Default: **one iteration per time step** (`MXITNS=1`).

Time derivative enters transport matrix only when `NSTATC=1`: `STRSXY` adds `ACOLD*RDTIM` to RHS, `RDTIM` to diagonal (`swancom5.ftn:2177-2188`).

With one iteration: uses `AC2` as old action.
With multiple iterations: uses `AC1` (`:2177-2184`).

## E. BSBT / SORDUP / S&L

`PROPSC` codes (`swmod1.ftn:2869-2874`):

| `PROPSC` | Scheme | Order |
|---|---|---|
| `1` | BSBT (Backward Space Backward Time) | 1st-order upwind |
| `2` | SORDUP (Second-Order UPwind) | 2nd-order |
| `3` | S&L (Stelling & Leendertse) | 3rd-order space-time |

`PROP BSBT` sets both stationary and non-stationary to first-order (`swanpre1.ftn:791-795`).

In `SWOMPU`, stencil sizes (`swancom1.ftn:3052-3078`):
- BSBT: smallest.
- SORDUP: larger.
- S&L: largest.

Code falls back to lower-order schemes near boundaries, dry points, obstacles (`:3079-3235`).

Dispatch (`swancom1.ftn:5393-5411`):
- `PROPSL=3` → `SANDL`.
- `PROPSL=2` → `SORDUP`.
- else → `STRSXY`/BSBT.

`SORDUP` is **stationary-only**; warns/errors if used non-stationary (`swancom5.ftn:2304-2422`).

`SANDL` warns on large non-stationary CFL (`:2889-2904`).

## F. Stationary unstructured grid

For unstructured (`OPTG=5`):
- `SWMAIN` builds vertex list (`swanmain.ftn:493-495`).
- Calls `SwanCompUnstruc` (`:623-627`).

`SwanVertlist` creates vertex orderings aligned with sweep directions (`SwanVertlist.ftn90:48-217`):
- First sweep direction follows user/wave/wind direction.
- Allocates `vlist(nverts, nsweep)`.
- Projects vertices onto each sweep direction; sorts by distance.

`SwanCompUnstruc` iterates over sweeps + ordered vertices (`SwanCompUnstruc.ftn90:823-984`):
- Identifies upwave vertices from cell topology.
- Selects spectral sector for each sweep.

This is the unstructured analogue of the structured-grid dependence chain.

## G. Memory: AC1 / AC2

`AC2` = present-time action density storage (`swmod2.ftn:990-1028`); allocated in preprocessing (`swanpre1.ftn:4979-4989`).

`AC1` = local previous-time action density in `SWMAIN` (`swanmain.ftn:266, 296`).

AC1의 전체 크기 할당은 NSTATM·MXITNS·PROPSC 조건을 따른다. `src/swanmain.ftn:500`의 원문은 `IF ( NSTATM.EQ.1 .AND. MXITNS.GT.1 .OR. PROPSC.EQ.3 ) THEN`이다. 나머지 경로의 최초 할당은 0 크기이다. `src/swanmain.ftn:518`의 원문은 `IF(.NOT.ALLOCATED(AC1)) ALLOCATE(AC1(0,0,0))`이다. 이미 할당된 AC1은 이 ELSE에서 해제하지 않는다.

SNEXTI의 시간 복사는 별도의 NSTATC·ITERMX·PROPSC 조건을 따른다. `src/swanmain.ftn:6892`의 `IF (NSTATC.EQ.1) THEN` 안에서 `src/swanmain.ftn:6893–6895`의 `IF (ITERMX.GT.1`<br>`&       .OR. PROPSC.EQ.3`<br>`&                                 ) THEN`을 만족할 때 복사한다. `src/swanmain.ftn:6899`의 원문은 `AC1(IDD,ISS,IXY) = AC2(IDD,ISS,IXY)`이다. [R8:N1-001](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론).

## H. Recommended choice

**Stationary mode** when:
- Forcing/BC/currents/water level/depth steady enough for equilibrium snapshot.
- Steady design cases.
- Small domains where propagation lag negligible.

Code embeds rule of thumb: stationary often acceptable for domains smaller than ~100 km or 1° per side (`swancom5.ftn:2899-2904`).

**Non-stationary mode** when:
- Time history matters: storms, moving wind, tides/surge, time-varying BCs.
- Large domains (arrival-time effects).
- Coupling to hydrodynamics.

SWAN enforces non-stationary input fields require `MODE NONSTAT` (`swanpre1.ftn:4007-4010, 4553-4554`).

## Decision Guide

| Domain / Situation | Mode + Settings |
|---|---|
| 정상 기본 전파법 | SORDUP이다. `src/swanmain.ftn:1179` `PROPSS = 2` |
| Tidal bay with wave-current interaction | `MODE NONSTAT`, `DELTC=15-30 min`, `BSBT`, `MXITNS=1` |
| Storm hindcast (wide domain) | `MODE NONSTAT`, `DELTC=30-60 min`, `BSBT` |
| Surf-zone resolved (very fine grid) | `MODE NONSTAT`, `DELTC` matching wave period × 5-10 |
| Stratified shelf, accuracy critical | `MODE NONSTAT`, `S&L` propagation |
| ADCIRC coupled (NWS=320) | `MODE NONSTAT`, `DELTC` matches `Flpp` from ADCIRC |
| Memory-tight large grid | Stationary BSBT (only AC2) |
| Multiple iterations needed for convergence (sub-domain) | `MXITNS > 1`, accept doubled memory (AC1+AC2) |

## Working Rules

- 반복 횟수 축소는 적용 권고다. 이를 코드가 강제하는 규칙으로 쓰지 않는다. [R5:PN-186](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론).
- For non-stationary, `MXITNS=1` is the production default; only raise for special cases.
- 일반 구조 격자의 기본 전파법은 정상 SORDUP과 비정상 S&L이다. PROP BSBT를 쓰면 두 모드를 BSBT로 지정한다. DIFFRACTION은 두 선택을 BSBT로 덮어쓴다. `src/swanmain.ftn:1179–1180`의 원문은 `PROPSS = 2`와 `PROPSN = 3`이다. `src/swanpre1.ftn:794–795`의 원문은 `PROPSN = 1`과 `PROPSS = 1`이다. 회절의 조건은 `src/swanmain.ftn:4090`의 `IF ( IDIFFR.EQ.1 ) THEN`이다. [R5 §4](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#4-노트-대조와-수정안).
- Convergence criterion: `STOPC` more rigorous than `ACCUR`; recommend `STOPC` for production.
- For unstructured grids, sweep ordering matters — first sweep along dominant wave direction speeds convergence.
- Output `BLOCK 'sname' ITERMAX HSIGN ...` to monitor iteration count and Hs convergence per stationary call.
- For coupled runs, ensure `DELTC` ≥ ADCIRC coupling interval × 1-2; otherwise wave field over-iterated.

## Common Pitfalls

- ▢ Using `MODE STAT` with time-varying wind/water level — input parser refuses; need `MODE NONSTAT`.
- ▢ `MODE NONSTAT` with `DELTC=1 s` — extremely expensive; SWAN doesn't need that fine timestep for kinematic waves.
- ▢ Setting `MXITST=1` for stationary — single sweep insufficient; use `MXITST >= 30`.
- ▢ Using SORDUP in non-stationary — runtime error.
- ▢ Expecting `MXITNS > 1` to add accuracy without memory cost — `AC1` allocated, doubles spectrum memory.
- ▢ Confusing `NSTATM` (intent) and `NSTATC` (actual) — both must be set; `NSTATC=NSTATM` typically.
- ▢ For unstructured stationary, expecting same `MXITST` as structured — unstructured may need more (40-80) for similar convergence.

## Next expansion

- ITERMAX block-output diagnostic for stationary convergence monitoring.
- Convergence parameter (PNUMS) tuning recipe.
- BSBT vs S&L comparison on canonical wave-current refraction case.

## References

- Booij et al. 1999 (SWAN baseline + sweeping).
- Stelling & Leendertse 1992 (S&L scheme).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/swan/source_code/swan/src`. Auto-draft = false; 2026-10-13 recovery 대조 보고서 R1–R8 반영.

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R4:T1-303 | MODE 모순 무시 | `source-analysis/swan-command-file-reference.md:214`의 `ignores the inconsistency and assumes nonstationary` | `src/swanpre1.ftn:879` `IF (NSTATM.LE.0 .OR. KEYWIS('STAT')) THEN`. | B 문서 오기 | NSTATM≤0이면 COMPUTE의 정상 분기로 간다. 비정상 모드에서는 COMPUTE STAT도 허용한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R5:PN-087 | NONSTAT MXITNS | swanuse PDF 94쪽 / 인쇄 86쪽 `Default: [mxitns] = 1.` | `src/swanpre1.ftn:1959` `CALL ININTG ('MXITNS' , MXITNS   , 'REQ', 0 )`. | B | NUMERIC STOPC NONSTAT을 적으면 최대 반복 횟수를 명시해야 한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-155 | ITERMX | — | `src/swanpre1.ftn:1956` `MXITNS = MXITST`, 1957 `'[itermx] is replaced; see user manual'`. | C | ITERMX는 경고를 내지만 두 모드의 반복 상한에 값을 대입한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-180 | BSBT 기본값 주장 | `source-analysis/swan-stationary-vs-nonstationary.md:189` `BSBT is the default` | `src/swanmain.ftn:1179` `PROPSS = 2`, 1180 `PROPSN = 3`. | B | 일반 구조 격자의 기본값은 정상 SORDUP·비정상 S&L이다. 회절의 BSBT 덮어쓰기는 별도 조건이다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
