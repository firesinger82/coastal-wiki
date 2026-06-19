---
title: "adcirc swan coupling"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-swan-coupling.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시. **SWAN Temporal Controls (PR #498) 절 추가 (2026-05-28)**: GitHub API `gh pr view 498 -R adcirc/adcirc` + `gh pr diff 498` 직접 fetch — PR body verbatim 인용 (SWANTimeControl namelist + RunStartDateTime + fort.26 COMPUTE 카드) + presizes.F / prep.F / couple2swan.F diff hunk 직접 인용 (SwanTimeStep offset 계산 + [1, SWAN_MTC] range gate + sentinel/radiation-stress fallback)."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23 + SWAN Temporal Controls 절 2026-05-28"
note_date: 2026-04~05 (original) / 2026-05-23 (promote) / 2026-05-28 (PR #498 절)
verification_by: "사용자 + codex source-code analysis + Claude Opus 4.7 (1M context) — PR #498 GitHub API 직접 fetch"
verification_date: 2026-04 (base) / 2026-05-28 (PR #498)
---

## Scope

How the `padcswan` binary couples ADCIRC and SWAN over a shared unstructured mesh, the actual NWS encoding (`3xx` for `NRS=3`, **not literal `NWS=83/84`**), how time-stepping is coordinated by integer ratio `SWAN_DT/DT`, what fields are exchanged each direction, how the build system selects SWAN sources for the coupled binary, and the hot-start protocol for the combined run. Use this when wiring a coupled tide+wave simulation, debugging coupling interval mismatches, or interpreting `NRS=3` log entries.

## Source basis

- `couple2swan.F:67-1236` — main coupling module: init, run, finalize, RS computation.
- `driver.F:30-57` — `CSWAN` driver entry/finalize.
- `adcirc.F:428-483` — main loop coupling call.
- `read_input.F:1080-1083, 1790-1817, 2255-2261` — `NRS` parsing and encoding.
- `wind.F:52-60` — allowable NWS table.
- `timestep.F:664-682, 695-725, 1214-1218` — wind passing, RS interpolation, hotfile timing.
- `hstart.F:325-337`, `write_output.F:4969-5112`, `netcdfio.F90:5555-7045, 8017-8085` — hot-start.
- `../thirdparty/swan/SwanReadADCGrid.ftn90:44-153` — SWAN reads `fort.14`.
- `../thirdparty/swan/swanmain.ftn:895-902, 8696-8983` — SWAN-side coupling hooks.
- `../work/makefile:195-663` — build targets.

## A. Entry points

| Routine | Purpose | Lines |
|---|---|---|
| `PADCSWAN_INIT` | Initialize SWAN, exchange grids/initial state | `couple2swan.F:947` |
| `PADCSWAN_RUN(ITIME)` | Per-coupling-step SWAN run + RS update | `:1092` |
| `PADCSWAN_FINAL` | Cleanup | `:1236` |
| `ComputeRadiationStresses` | Integrate SWAN spectra to RS components | `:112` |
| `ComputeWaveDrivenForces` | Convert RS gradients to nodal forces | `:210` |

Driver glue (`driver.F:30-57`): imports `CSWAN` driver, calls `PADCSWAN_INIT` then `PADCSWAN_FINAL`.

Time-loop call (`adcirc.F:428-483`):
```
if (mod(ITIME, CouplingInterval) == 0) call PADCSWAN_RUN(ITIME)
```

SWAN-side hooks activated by `switch.pl -adcirc` — only present in coupled binary (`makefile:232-233, 558-560`).

## B. Time stepping

- ADCIRC runs every `DT`; SWAN `DT` imported as `SWAN_DT` (`couple2swan.F:950, 965`).
- **Coupling interval = integer ratio** `SWAN_DT / DT` (`:1079-1081`).
- ADCIRC calls SWAN only on that interval (`adcirc.F:475-483`).
- During SWAN run, interpolation midpoint used for time-centering (`couple2swan.F:1212-1215`).

**Note**: there is **no `CWTIM_INC` symbol** in this tree; coupling interval comes from SWAN `TIMECOMM:DT` block divided by ADCIRC `DT`.

## C. SWAN → ADCIRC (radiation stress)

1. SWAN spectra integrated into `ADCIRC_SXX/SXY/SYY` (`couple2swan.F:112-119, 177-196`).
2. Gradients converted to nodal wave forces in `SWAN_RSNX2/SWAN_RSNY2` (`:360-364, 399-404, 421-427`).
3. ADCIRC extrapolates/interpolates into `RSNX2/RSNY2` for `NRS=3` (`timestep.F:695-703`).
4. Added to wind stress in momentum (`timestep.F:721-725`).

## D. ADCIRC → SWAN (water level, currents, wind)

Allocated arrays (`couple2swan.F:67-75, 974-982`):
- `SWAN_ETA2` — water level.
- `SWAN_UU2`, `SWAN_VV2` — currents.
- `SWAN_WX2`, `SWAN_WY2` — winds (if `COUPWIND`).

Init copies ADCIRC `ETA2/UU2/VV2` plus winds (`:993-1009`).

Each coupling step:
- WL/currents updated from ADCIRC (`:1128-1142`).
- Dry nodes set depth zero / current zero.
- Wind passed from ADCIRC met → SWAN if `COUPWIND` (`timestep.F:664-682`).

SWAN-side memory grab post-preprocess (`../thirdparty/swan/swanmain.ftn:8696-8983`).

## E. Mesh sharing

SWAN unstructured ADCIRC reader explicitly opens `fort.14` (`SwanReadADCGrid.ftn90:44-103`):
- Reads `ncells, nverts`, node coords + depth, triangles (`:114-153`).

Coupler uses SWAN `nverts/xcugrd/ycugrd` for output/exchange (`couple2swan.F:596-598, 800-835`).

So **same `fort.14` is used by both ADCIRC and SWAN** — single mesh, no interpolation needed.

## F. NWS encoding (NWS=3xx, not 83/84)

**Important**: `wind.F:52-60` allowable base `NWS` list **excludes 83/84**.

Instead, `read_input.F:1790-1817` parses radiation-stress coupling from **hundreds digit**:
```
NRS = ABS(NWS / 100)        ! strip hundreds
NWS = NWS − 100*sign*NRS    ! remaining is base met forcing
```

`NRS=3` is documented as "WAVES WILL BE COUPLED TO SWAN" (`:2255-2261`).

So:

| Input NWS | NRS | Effective base NWS | Meaning |
|---|---:|---:|---|
| `308` | `3` | `8` | OWI hindcast met + SWAN waves |
| `312` | `3` | `12` | OWI WIN/PRE + SWAN |
| `320` | `3` | `20` | GAHM vortex + SWAN |
| `300` | `3` | `0` | No met, only SWAN waves |
| `8` | `0` | `8` | OWI met only, no waves |

Literal `NWS=83/84` is **invalid** in this code path.

## G. Build / link

`makefile` distinguishes:

| Target | Flags | SWAN |
|---|---|---|
| `padcirc` (parallel ADCIRC) | `FFLAGS3 $(DP)`, no SWAN VPATH | Not built |
| `padcswan` (coupled) | parallel + `-DCSWAN`, SWAN VPATH, SWAN switch `-pun -adcirc` | Built and linked |

References: `makefile:195-233, 480-509, 634-635, 661-663`.

So **always use `padcswan` for coupled runs**; `padcirc` even with `NRS=3` won't have SWAN linked.

## H. Hot-start

ADCIRC hot-start reads base `RSNX/RSNY`; for `NRS=3` also reads `SWAN_RSNX/RSNY` history (`hstart.F:325-337`).

Binary hot-start writes:
- Base RS arrays.
- If `NRS=3`: SWAN RS arrays (`write_output.F:4969-5112`).

NetCDF hot-start defines `swan_rsx1/rsy1/rsx2/rsy2` (`netcdfio.F90:5555-5568`); writes for `nrs==3` (`:6966-7045`).

SWAN spectral hot-start is **separate**:
- ADCIRC sets `SwanHotStartUnit` (`read_input.F:1080-1083`).
- `timestep.F:1214-1218` defers SWAN hotfile write until after next SWAN step.
- SWAN calls `BACKUP` then clears flag (`swanmain.ftn:895-902`).

**Possible issue noted in code**: NetCDF read path inquires SWAN variable IDs but reads `hs%rs1/rs2` IDs into `swan_*` arrays — not `hs%swan_rs*` (`netcdfio.F90:8017-8085`). This may indicate a latent bug in NetCDF restart of SWAN-coupled runs; verify before relying on it.

## Decision Guide

| Goal | Setup |
|---|---|
| Tide + wave coupling, OWI met | Compile `padcswan`; set `NWS=312` (or `308` for OWI ASCII met) |
| GAHM hurricane + waves | `NWS=320` (NRS=3, base=20 GAHM) |
| Wave-only test (no met) | `NWS=300` |
| Coupling interval (5 min, ADCIRC dt=2s) | `SWAN_DT=300` in SWAN input → ratio 150 |
| Tight coupling (every ADCIRC step) | `SWAN_DT = DT` — expensive, rarely needed |
| Hot-start coupled run | `IHOT=67/68` for ADCIRC; SWAN auto via `SwanHotStartUnit` |
| Restart NetCDF coupled | Verify `swan_rs*` arrays write/read correctly; possible latent bug |

## Working Rules

- Use `padcswan` binary; verify with `padcswan --help` or check link map for `swan` symbols.
- `SWAN_DT` typically 60-1800 s; ADCIRC `DT` 0.5-5 s. Ratio 100-300 is normal.
- Set ADCIRC `OutputControl` and SWAN `BLOCK` outputs at compatible intervals for diagnostic plots.
- In log, look for "WAVES WILL BE COUPLED TO SWAN" confirming `NRS=3` parsed.
- `COUPWIND` flag in `couple2swan.F`: if true, ADCIRC met goes to SWAN; if false, SWAN reads its own wind file (rarely used).
- For ADCIRC v55+, NetCDF hot-start is preferred; for older versions, fort.67/68 binary is more stable.
- SWAN spectral hot-start (`HOTSTART` in SWAN input) is separate from ADCIRC hot-start; both must align on time.

## Common Pitfalls

- ▢ Setting `NWS=83` literally — invalid; use `NWS=308` etc.
- ▢ Using `padcirc` with `NWS=308` — base met works but no SWAN linked; runs without waves silently.
- ▢ `SWAN_DT` not divisible by `DT` — coupling interval rounds; output frequency anomalies.
- ▢ Hot-start ADCIRC at time T but SWAN cold-start — wave field absent for first SWAN step; spurious zero RS.
- ▢ Hot-start SWAN before ADCIRC catches up — cyclic dependency; ensure both at same `TIMELOC`.
- ▢ Met forcing time alignment — `STATIM/REFTIM` apply to ADCIRC; SWAN reads `INPGRID` time block independently. Match epochs.
- ▢ NetCDF restart with `NRS=3` — possible bug at `netcdfio.F90:8017-8085` (`hs%rs1/rs2` vs `hs%swan_rs*`); test on small case before production.

## SWAN Temporal Controls (PR #498, phase 1 of 2)

PR [#498](https://github.com/adcirc/adcirc/pull/498) (OPEN, branch `Spatial-and-Temporal-Controls`, +274 -30, 17 files). 사용자가 ADCIRC+SWAN coupled simulation 의 SWAN computation 시간을 storm landfall 즈음으로 제한 가능 → 전체 mesh + 전체 timeframe SWAN 호출 회피로 wall-clock 절감. Spatial controls 은 phase 2 예정. 외부 docs: [CCHT-NCSU/Spatial-Temporal-Controls](https://github.com/ccht-ncsu/Spatial-Temporal-Controls).

### 사용자 입력 (PR body verbatim)

- **fort.15 (ADCIRC)** 끝에 namelist 추가:
  ```
  &SWANTimeControl RunStartDateTime='YYYYMMDD.HHMMSS' /
  ```
  `RunStartDateTime` 은 현 ADCIRC 시뮬레이션의 시작 시각

- **fort.26 (SWAN)** 의 `COMPUTE` 카드를 desired range 로 변경:
  ```
  COMPUTE YYYYMMDD.HHMMSS 1200 SEC YYYYMMDD.HHMMSS
  ```

→ namelist 없거나 `RunStartDateTime` 에 `-` 포함 (default sentinel `"-99999"`) 시 **기존 동작 그대로 (전체 시간 SWAN)**. backward-compat.

### 코드 변경 (PR diff 직접 fetch 2026-05-28)

| 파일 | 변경 | 역할 |
|---|---|---|
| `prep/presizes.F` | +RunStartDateTime 변수 + SWANTimeControl namelist + SIZEUP15 read with default `"-99999"` | namelist 정의 + fort.15 parse |
| `prep/prep.F` | `PREP15` 에서 `SWANTimeControl` namelist write | 파티션 prep 단계 출력 보존 |
| `src/couple2swan.F` | `SwanTimeStep` 초기값 = 0 명시; `PADCSWAN_INIT` 에서 `RunStartDateTime` 파싱 → `SwanTimeStep = NINT((AdcircStartTime - SWAN_TINIC) / SWAN_DT)`; `PADCSWAN_RUN` 에서 `[1, SWAN_MTC]` 범위 밖이면 `SWMAIN` skip + wave output sentinel + radiation stress 0 | 핵심 coupling 제어 |
| 그 외 14 files | (테스트 / build / docs) | (본 노트 scope 밖) |

### Algorithm 요점 (couple2swan.F PADCSWAN_INIT/RUN)

```fortran
! INIT: SWAN timestep offset 결정
IF( INDEX( RunStartDateTime, "-") .GT. 0 ) THEN  ! default sentinel
   SwanTimeStep = 0   ! 기존 동작 (전체 시간 SWAN)
ELSE
   CALL DTRETI( RunStartDateTime, 1, AdcircStartTime )
   SwanTimeStep = NINT( ( AdcircStartTime - SWAN_TINIC ) / SWAN_DT )
ENDIF

! RUN: 매 ADCIRC time step
SwanTimeStep = SwanTimeStep + 1
IF((SwanTimeStep.GE.1).AND.(SwanTimeStep.LE.SWAN_MTC))THEN
   CALL SWMAIN(ITIME,SwanTimeStep)        ! SWAN 실제 호출
ENDIF
IF((SwanTimeStep.LT.1).OR.(SwanTimeStep.GT.SWAN_MTC))THEN
   ! SWAN 호출 skip 한 시점: output 변수 sentinel + radiation stress 0
   Swan_HSOut(:) = -99999.D0  ! 등 6개 출력 sentinel
   ADCIRC_SXX/SXY/SYY(:,:) = 0.D0  ! radiation stress 0 → 파-induced 응력 없음
ENDIF
```

→ 핵심 `SWAN_MTC` 는 SWAN 측 (fort.26) `COMPUTE` 카드로부터 도출되는 MTC (Maximum Time-step Counter). 사용자 fort.26 의 COMPUTE range 가 짧을수록 `SWAN_MTC` 작음 → SWAN 호출 시간 윈도우 짧음.

### 의의 + 한계

- **속도 절감**: storm landfall 시간 (~24-72h) 만 SWAN 실행, 그 외 시간 ADCIRC 만 → 전체 wall-clock 큰 폭 감소 (PR body 명시: "yielded faster run times and similar accuracies")
- **정확성**: storm 외 시간의 wave-induced radiation stress 가 0 으로 설정 → tide-driven 일반 시간 surge response 만 평가. ADCIRC-only 시뮬레이션 효과 (해당 시간 window 에서)
- **Backward compat**: namelist 미지정 시 동작 동일
- **Spatial control 은 phase 2 예정** — landfall 인근 mesh 영역에만 SWAN compute 제한 가능 예정

### 운영 권고

- 사용 시 storm landfall 시각 (best track / fort.22 GAHM record) 으로부터 적절한 buffer (예: ±24h) 잡고 `COMPUTE` 카드 범위 설정
- buffer 너무 좁으면 long-period swell 의 영향 미흡 가능 (off-landfall arrival)
- 검증: 동일 fort.15 + 동일 SWAN COMPUTE 전체 vs 일부 두 run 비교 후 peak surge / wave height 차이 정량화 (PR body 가 명시: latest source code 로 default 시간 frame 동일 시 차이 없음)

## Next expansion

- Build recipe for `padcswan` on Linux/Intel.
- COUPWIND vs separate SWAN met forcing recipe.
- NetCDF hot-start verification test.
- Comparison vs older NWS=83 (legacy) coupling.
- Spatial controls (PR phase 2) 가 merge 되면 본 노트 보강.

## References

- Dietrich et al. 2011 (ADCIRC+SWAN unstructured coupling).
- Booij et al. 1999 (SWAN baseline).
- PR #498 <https://github.com/adcirc/adcirc/pull/498> (OPEN 2026-05-18 update).
- CCHT-NCSU temporal/spatial controls docs <https://github.com/ccht-ncsu/Spatial-Temporal-Controls>.
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/adcirc/source_code/adcirc/src`. Auto-draft = false; review_required = true.
