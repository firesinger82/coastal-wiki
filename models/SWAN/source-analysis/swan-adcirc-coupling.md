---
title: "swan adcirc coupling"
topic: general
canonical_source: self
citation_status: verified
verification_method: "2026-10-13 HEAD 대비 추가·수정 19줄을 R5·R7 최종 보고서, git 판정 A, 현재·과거 코드와 웹 HTML에 대조했다." # [10-13 전수 검증 정정]
last_source_check: 2026-10-13 (recovery 대조 반영)
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

SWAN-side mechanism for sharing the ADCIRC unstructured mesh (`fort.14`), how `READ UNSTRUC ADC` parses, where boundary spectra are interpolated to vertex AC2, time-stepping in coupled mode (host owns MPI/time advance), how wave-induced forces (`fx, fy`) are passed back to ADCIRC via `SwanComputeForce`, and the build path (SWAN library linked into `padcswan`). Use this when debugging the SWAN side of `padcswan`, configuring nesting on unstructured grids, or interpreting SWAN-side BC reads.

## Source basis

- `swanpre1.ftn:1462-1492, 1344-1350, 944-1286, 791-3074` — `READ UNSTRUC`, input grid types, propagation flags.
- `SwanReadADCGrid.ftn90:42-176`, `SwanGriddata.ftn90:54-72`, `SwanReadGrid.ftn90:73-78` — ADCIRC mesh reader.
- `swanmain.ftn:101-104, 128, 266-695, 1105-1109, 1110-1112, 4037-6960, 5053-5161, 8798-8823` — main loop, coupling flags.
- `src/swanparll.ftn:140` `!MPI!NCOH      CALL MPI_INIT ( IERR )` — MPI_INIT의 COH 전처리 표식.
- `swanpre2.ftn:2702-3151` — boundary list / segment validation.
- `SwanComputeForce.ftn90:35-307` — wave-driven force computation.
- `switch.pl:33,97-100` — `-adcirc` switch.
- `src/CMakeLists.txt:30-121`, `srclist.cmake:28-63` — SWAN library build.

## A. Unstructured mesh (READ UNSTRUC ADC)

`READ UNSTRUC` parser at `swanpre1.ftn:1462-1492`:
- Default keyword: `ADC` → `grid_generator = meth_adcirc`, depth source `IGTYPE(1)=3`, calls `SwanReadGrid`.
- fname은 Triangle·Easymesh의 확장자 없는 이름이다. `src/swanpre1.ftn:1485` `ELSEIF (KEYWIS('TRIA')) THEN`; `src/swanpre1.ftn:1488` `ELSEIF (KEYWIS('EASY')) THEN`. 확장자 결합은 `src/SwanReadTriangleGrid.ftn90:87,136`의 `.node`·`.ele`와 `src/SwanReadEasymeshGrid.ftn90:80,114`의 `.n`·`.e`에 있다. [10-13 전수 검증 보완]

`SwanReadADCGrid.ftn90:42-176`:
- Hard-codes `grdfil = 'fort.14'` and opens it (`:91-97`).
- Reads `ncells, nverts`, vertex coords + depth (`:103-123`).
- Reads triangle connectivity `kvertc(1:3, cell)` (`:126-136`).
- Loads ADCIRC open/land boundary markers into `vmark` (`:146-176`).

So **ADCIRC's `fort.14` is the single shared mesh** — no separate SWAN mesh file in coupled runs.

## B. Coupling interface (PADCSWAN_RUN, no `couple2adcirc`)

Standalone SWAN `PROGRAM` is **bypassed** in coupled mode (`swanmain.ftn:101-104`). ADCIRC's `couple2swan.F` calls SWAN via `PADCSWAN_INIT` / `PADCSWAN_RUN`; SWAN-side workhorse is `SWMAIN` (`swanmain.ftn:128`).

There is **no `couple2adcirc.F` in the SWAN tree** — coupling logic lives in ADCIRC's `couple2swan.F` (covered in `adcirc-swan-coupling.md`).

ADCIRC-specific preprocessing switch: `-adcirc` (`switch.pl:33,97-98`); applied by uncommenting `!ADC` lines.

41.01 patch A의 항목은 ADCIRC 결합 시의 기본값을 말한다. 현재 Git 소스에는 그 결합 초기 대입이 없다. 현재 독립 초기값 IDRAG=1을 ADCIRC 결합 기본값의 변경 증거로 쓰지 않는다. `43e9bbb:src/swanmain.ftn:1109` `      IDRAG  = 1                                                          42.00 41.49 41.33`; `43e9bbb:src/swanmain.ftn:1108` `!     when coupled with ADCIRC, the default is to use ADCIRC drag formulation`.

## C. Time stepping / MPI

SWAN normal loop (`swanmain.ftn:569-694`):
1. `SNEXTI` updates BC/input fields (`:586-595`).
2. Compute (`SWCOMP` for structured, `SwanCompUnstruc` for unstructured `OPTG=5`) (`:610-628`).
3. Output.
4. Advance: `TIMCO = TIMCO + DT`; printed as "Time of computation" (`:686-694`).

`DT, TINIC, TFINC, TIMCO` globals at `swmod1.ftn:2978-2993`.

**Coupled mode**: ADCIRC passes timestep to SWAN per source comment; **no return-timestep API** in this SWAN tree (`swanmain.ftn:101-104`). ADCIRC controls when SWAN runs.

MPI_INIT 행 자체의 표식은 !MPI!NCOH이다. 이 행을 -adcirc가 직접 제거한다고 쓰지 않는다. `src/swanparll.ftn:140` `!MPI!NCOH      CALL MPI_INIT ( IERR )`. ADCIRC 결합에서 주 프로그램을 우회한다는 설명은 별도의 호출 구조이다. `src/swanmain.ftn:101` `!     In case of coupling with ADCIRC, this program will not be executed`; `src/swanmain.ftn:102` `!     Instead, SWAN initialization and run will be done by PADCSWAN_INIT`.

## D. Boundary / nesting on unstructured

Boundary command initializes unstructured boundary list via `SwanBpntlist` (`swanpre2.ftn:2702-2709`).

Parallel/local boundary global map: `bvertg` (`:2744-2768`).

Segment boundary accepts XY or vertex index `K`; validates vertex on unstructured boundary (`:3095-3151`).

`BGRIDP` built for unstructured boundary vertices using global-to-local map (`swanmain.ftn:4037-4058`).

Boundary spectra applied to boundary vertices by interpolation into `AC2` (`swanmain.ftn:6932-6960`).

So nesting works the same way as structured SWAN — parent dumps `NESTOUT`, child reads via `BOUND NEST` — but vertex-based.

## E. Wind / current / water level from ADCIRC

Input grid types: `CUR, WIND, WLEV`, unstructured (`swanpre1.ftn:1344-1350`).

Storage slots (`swmod1.ftn:1935-1947`):
- Currents: `JVX*, JVY*`.
- Water level: `JWLV*`.
- Wind: `JWX*, JWY*`.

Direct mesh input uses global/local vertex index `JVERT` (`swanmain.ftn:5053-5062`).

Per-step updates:
- Water level → `COMPDA(...,JWLV2)`; depth → `JDP2` (`:5077-5094`).
- Currents → `JVX2/JVY2` (`:5098-5130`).
- Wind → `JWX2/JWY2` (`:5145-5161`).

Time-varying unstructured fields use direct `ARR(JVERT)` when `IGTYPE==3` (`:8798-8823`).

This means ADCIRC writes directly into SWAN vertex-indexed arrays each coupling step — no spatial interpolation.

## F. Wave-driven forces back to ADCIRC

`SwanComputeForce.ftn90:35-307`:
- Coupled ADCIRC extension noted (`:35-39`).
- API returns `fx, fy` as `intent(out)` wave-induced forces (`:61-67`).
- Computes radiation stresses from `AC2` over frequency/direction (`:150-199`).
- Computes stress gradients on vertex duals (`:206-289`).
- Final forcing (`:304-307`):
```
fx = -ρ * g * (∂Sxx/∂x + ∂Sxy/∂y)
fy = -ρ * g * (∂Sxy/∂x + ∂Syy/∂y)
```

Handoff to ADCIRC is via caller-owned `fx/fy`; caller is `couple2swan.F` (outside this tree).

## G. Build / link

This SWAN checkout builds static library `swan${VERSION}` (`src/CMakeLists.txt:97-109`).

SWAN executable links library (`:112-117`).

Source list includes ADCIRC mesh reader, unstructured solver, force routine (`srclist.cmake:28-63`).

NetCDF source list includes same (`srclistnc.cmake:31-66`).

`padcswan` target is **not** present in this SWAN checkout; ADCIRC-side build must link against this SWAN library or compiled objects (see `adcirc-swan-coupling.md` for ADCIRC `padcswan` makefile target).

## Decision Guide

| Need | Setting |
|---|---|
| ADCIRC unstructured mesh sharing | `READ UNSTRUC ADC` (default keyword); needs `fort.14` |
| Coupled hot-start | SWAN `HOTSTART` synchronized via ADCIRC `SwanHotStartUnit` |
| Nesting child of coupled parent | `BOUND NEST 'parent.spec'` (coarser SWAN parent) |
| ADCIRC와 COH 전처리 구분 | -adcirc는 !ADC를 제거하고 !NADC를 남긴다. MPI_INIT 행 자체의 표식은 !MPI!NCOH이다. `switch.pl:97` `if ($adc=~/TRUE/) {$newline=~s/^!ADC//;}`; `src/swanparll.ftn:140` `!MPI!NCOH      CALL MPI_INIT ( IERR )`. |
| Disable wind-input from ADCIRC met | Set SWAN's own `INPGRID WIND` instead of `COUPWIND` in ADCIRC |
| Output radiation stresses for diagnostic | Use `BLOCK ... 'fname' ...FX FY...` (or compute from `HSIGN`, `DIR`) |

## Working Rules

- `padcswan` build expects this SWAN library; do not modify SWAN source without rebuilding the library.
- If you change SWAN source, rebuild library AND relink `padcswan`.
- For nesting unstructured child from structured parent: standard NESTOUT/BOUND NEST works; spectra interpolate to vertices.
- `vmark` carries ADCIRC's open/land boundary markers — use these to debug missing BC application.
- For Korean coast unstructured runs: same `fort.14` for ADCIRC tide and SWAN waves; ensure boundary type strings (`open` vs `land`) consistent.
- SWAN side uses `JVERT` (vertex index) directly — no IJ-grid concept on unstructured.

## Common Pitfalls

- ▢ Specifying separate SWAN mesh file in coupled mode — ignored; SWAN reads `fort.14`.
- ▢ Building SWAN library without `-adcirc` switch — coupled-build features missing.
- ▢ Looking for `couple2adcirc.F` in SWAN tree — doesn't exist; logic is on ADCIRC side.
- ▢ Setting SWAN `MODE NONSTAT` with mismatched `DELTC` — ADCIRC controls timestep; SWAN's internal `DT` must align.
- ▢ Hot-start ADCIRC alone without SWAN spectral file — wave init at zero; first SWAN step has no wave history.
- ▢ Expecting return timestep API — none; ADCIRC commands SWAN unilaterally.

## Next expansion

- BSBT vs SORDUP vs S&L performance on coastal unstructured (cross-link to `swan_modes_dispatch.md`).
- COAWST-style 3-way coupling (ROMS+SWAN+WW3) reference.
- SWAN library build flags walkthrough.

## References

- Booij et al. 1999 (SWAN third-generation).
- Dietrich et al. 2011 (ADCIRC+SWAN unstructured).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/swan/source_code/swan/src`. Auto-draft = false; review_required = true.

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

빈 인용 칸은 `—`로 표시한다. 표의 절 번호는 각 행이 링크한 대조 보고서의 절 번호다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R5:PN-144 | CICE ADCICE | — | `src/swanpre1.ftn:2342` `IF (KEYWIS('CICE')) THEN`; `src/swanpre1.ftn:2346` `IICE=2`; `src/swanpre1.ftn:2347` `CALL INREAL('WBICETH',WBICETH,'STA',70.0)`; `src/swmod1.ftn:2674` `! WBICETH[  70.0] Minimum ice concentration (percentage out of 100.0)` | C 문서 누락 | CICE ADCICE 입력은 존재한다. WBICETH=70%의 읽기와 독립 실행 소산 구현은 구분한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R7:H-1204 | ADCIRC 항력 기본 | `website/modifications/modifications.htm:1204` `when coupled with ADCIRC, the default is to use ADCIRC drag formulation` | `src/swanmain.ftn:1109` `IDRAG  = 1                                                          42.00 41.49 41.33`; `122b595:src/swanmain.ftn:1096` `      IDRAG  = 1                                                          42.00 41.49 41.33`; `43e9bbb:src/swanmain.ftn:1109` `      IDRAG  = 1                                                          42.00 41.49 41.33`; `43e9bbb:src/swanmain.ftn:101` `!     In case of coupling with ADCIRC, this program will not be executed  41.20`; `43e9bbb:src/swanmain.ftn:102` `!     Instead, SWAN initialization and run will be done by PADCSWAN_INIT  41.20`; `43e9bbb:src/swanmain.ftn:1108` `!     when coupled with ADCIRC, the default is to use ADCIRC drag formulation` | D 현재 해당 구현 없음 | 41.01 patch A의 항목은 ADCIRC 결합 시의 기본값을 말한다. 현재 Git 소스에는 그 결합 초기 대입이 없다. 현재 독립 초기값 IDRAG=1을 ADCIRC 결합 기본값의 변경 증거로 쓰지 않는다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) [10-13 전수 검증 정정] |
| R7:N-030 | ADCIRC와 COH 전처리 구분 | `swan-adcirc-coupling.md:134` ``\| Disable SWAN-side MPI init in coupled \| Use `-adcirc` switch in `switch.pl` \|`` | `src/swanparll.ftn:140` `!MPI!NCOH      CALL MPI_INIT ( IERR )` | B 문서 오기 | -adcirc는 !ADC를 제거하고 !NADC를 남긴다. MPI_INIT 행 자체의 표식은 !MPI!NCOH이다. 이 행을 -adcirc가 직접 제거한다고 쓰지 않는다. ADCIRC 결합에서 주 프로그램을 우회한다는 설명은 별도의 호출 구조이다. 노트 64행의 coupled 표기도 COH와 ADCIRC를 구분하도록 고친다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
