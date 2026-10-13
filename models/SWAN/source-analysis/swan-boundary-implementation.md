---
title: "swan boundary implementation"
topic: currents
canonical_source: self
citation_status: verified
verification_method: "2026-10-13 HEAD 대비 추가·수정 줄을 SWAN 경계 파서·스펙트럼 재분배·경계값 갱신 소스와 보관 매뉴얼·HTML에 대조했다. 결론은 recovery R3·R4·R7 최종본과 git A·E 판정에 대조했다. H-566의 과거 실행문과 날짜는 원본 저장소의 git show로 확인했다." # [10-13 전수 검증 정정]
last_source_check: 2026-10-13 (recovery 대조 반영)
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# SWAN boundary processing — SWBOUN parsing + nest file readers + runtime injection

## Scope note

End-to-end mapping of SWAN's boundary system: how a `BOUND` line in the command file gets parsed (`SWBOUN`), how external spectrum files (NESTOUT, WAM-NEST, WAVEWATCH III) are read, how stored boundary spectra get applied to the model state `AC2` at boundary points during the run, and the internal data structures that connect them.

Companion to `swan-command-file-reference.md` (covers BOUND command syntax) and `swan-source-terms-implementation.md` (covers source-term injection elsewhere in the matrix). This note covers the boundary-only path.

## Source basis

- **Codex deep code analysis** 2026-05-06 of:
  - `models/swan/source_code/swan/src/swanpre1.ftn` — top-level `SWREAD` dispatch
  - `swanpre2.ftn` — `SWBOUN` body (parametric shapes, segments, sides), `BCFILE`/`BCWAMN`/`BCWW3N` (file readers)
  - `swanmain.ftn` — runtime injection (`SNEXTI`, `RBFILE`, `SINTRP`)
  - `swmod2.ftn` — boundary type definitions

## A. SWBOUN body — parsing flow

### Dispatch from SWREAD

`SWREAD` swaps in **global** grid dimensions before calling `SWBOUN`, so all boundary parsing operates on global grid indexing (relevant for parallel runs):

```fortran
swanpre1.ftn:1873-1883
  swap MXC/MYC/MCGRD/NGRBND <- MXCGL/MYCGL/MCGRDGL/NGRBGL
  CALL SWBOUN(...)
  swap back
```

### Top-level parse order (within SWBOUN)

`SWBOUN` body at `[file=src/swanpre2.ftn line=2779-3002]` dispatches in this order:
1. `SHAP...` (shape defaults)
2. `WAMN...` (WAM-NEST file)
3. `WW3` / `WWIII` (WaveWatch III file)
4. `NE...` (SWAN nest file)
5. (else) — fall through to side/segment definitions

BOUND SHAPE를 생략하면 기본 모양을 사용한다. 뒤에 BOUND SHAPE가 나왔다고 명령 파서 자체가 실패하지는 않는다. `src/swanmain.ftn:1039` `FSHAPE = 2`; `src/swanpre2.ftn:3654` `BSTMP%FSHAPE = FSHAPE`.

### Parametric frequency-shape dispatch

At `[file=src/swanpre2.ftn line=2802-2819]`:
- `JON` → `FSHAPE = 2` (+ optional `GAMMA`)
- `PM` → `FSHAPE = 1`
- `GAUS` → `FSHAPE = 4` (+ `SIGFR` stored to `PSHAPE(2)` in rad/s)
- `BIN` → `FSHAPE = 3`
- `TMA` → `FSHAPE = 5` (+ `GAMMA`, `D`)

### Frequency convention and DSPR

At `[file=src/swanpre2.ftn line=2821-2835]`:
- `MEAN` flips sign of `FSHAPE` (negative encodes mean period instead of peak); default is `PEAK`
- `DSPR DEGR` → `DSHAPE = 1` (degrees)
- `DSPR POW` → `DSHAPE = 2` (power)

MEAN은 입력 주기를 Tm01로 해석한다. SSHAPE는 적분한 평균주기가 입력값에 맞도록 피크주기를 반복 조정한다. `src/swanser.ftn:4161` `MPER = PI2 * AM0 / AM1`; `src/swanser.ftn:4171` `PKPER = (SPPARM(2) / MPER) * PKPER`.

### SEGMENT path

At `[file=src/swanpre2.ftn line=3063-3191]`:
- Coordinate mode parsed: `XY/LOC` (geographic) or `IJ/GRI/K` (grid index)
- Reads segment endpoint pairs via `READXY` (geographic) or `ININTG` (integer)
- Converts geographic to grid indices via `CVMESH` / `SwanFindPoint`
- Stores selected boundary points as a linked list under `TMP%JX/JY`

### SIDE path

At `[file=src/swanpre2.ftn line=3329-3519]`:
- Side keyword parsed: `N/NW/W/SW/S/SE/E/NE`
- Direction modifier: `CCW` (default) or `CLOCKW`
- Computes best matching computational side index `ISIDM`
- Resolves end indices `(IX1, IY1) → (IX2, IY2)`
- Optionally swaps endpoints based on orientation
- Walks that side accumulating boundary points

### Boundary-point mapping records

Each computational boundary point gets a 6-element tuple stored in `BGPTMP%BGP(1..6)` at `[file=src/swanpre2.ftn line=3692-3702]` and `[file=src/swanpre2.ftn line=3836-3847]`:
- `BGP(1)` — grid point index
- `BGP(2)` — type flag
- `BGP(3), BGP(4)` — weight1, spectrum1 (interpolation source)
- `BGP(5), BGP(6)` — weight2, spectrum2

This is the linkage between geographic boundary points and spectral storage.

## B. Boundary spectrum file readers

### NESTOUT format (.bnd, SWAN-native)

- Header reader: `BCFILE` at `[file=src/swanpre2.ftn line=3878-4366]` reads SWAN/TPAR header, locations, `FREQ` grid, `DIR` grid, quantity metadata into `BSPFIL` structures.
- Runtime spectrum loop: `RBFILE` calling `RESPEC` at `[file=src/swanmain.ftn line=7796-7963]` per boundary point per time step.

### WAM-NEST format

- Header reader: `BCWAMN` at `[file=src/swanpre2.ftn line=4369-4952]` reads WAM resolution/header, pre-scans points; per-point read at `[file=src/swanpre2.ftn line=4709-4756]`.
- Runtime: `[file=src/swanmain.ftn line=7823-7847]` and `[file=src/swanmain.ftn line=7961-7963]`.

### WAVEWATCH III format

- Header reader: `BCWW3N` at `[file=src/swanpre2.ftn line=4956-5468]` reads WW3 header/freq/dir + point metadata; per-point loop `[file=src/swanpre2.ftn line=5327-5392]`.
- Runtime: `[file=src/swanmain.ftn line=7848-7873]`, `[file=src/swanmain.ftn line=7883-7891]`, `[file=src/swanmain.ftn line=8403-8418]`.

### Spectral grid consistency — IMPORTANT

**No hard equality check** between file's frequency/direction grid and computational `SPCSIG`/`SPCDIR`. Instead spectra are remapped via `CHGBAS`:
- Direction interpolation: `[file=src/swanmain.ftn line=8450-8453]`
- Frequency interpolation: `[file=src/swanmain.ftn line=8481-8483]`

`CHGBAS`는 구간별 상수 밀도를 겹치는 구간 길이에 따라 재분배한다. 스펙트럼 격자를 맞추려면 `CGRID`의 주파수·방향 설정을 맞춘다. `src/swanser.ftn:5354` `Y2(I2) = Y2(I2) + Y1(I1) * (RUPP-RLOW)`; `src/swanser.ftn:5382` `Y2(I2) = Y2(I2) / CELLEN`.

The reader does validate **coordinate-type compatibility** (Cartesian vs spherical) at `[file=src/swanpre2.ftn line=4125-4129]` (`LOC` vs `LONLAT` against `KSPHER`).

## C. Boundary application during the run

### Time-stepped update (nonstationary)

`SNEXTI` at `[file=src/swanmain.ftn line=6908-6919]` updates each boundary file via `RBFILE`. `RBFILE` refreshes/interpolates `BSPECS(:,:,:,1)` to current model time `TIMCO`.

### Injection into AC2

`[file=src/swanmain.ftn line=6937-6946]` is the actual injection:
- For each boundary grid point, spatial interpolation between two stored boundary spectra (`K1`, `K2`, weights from `BGRIDP`) is computed.
- Result is written **directly** into `AC2(1, 1, INDXGR)` via `SINTRP`.

경계 입력 단계는 보간한 스펙트럼으로 AC2의 경계값을 덮어쓴다. 노트의 덮어쓰기는 기존 AC2와 더하거나 평균하지 않는다는 뜻이다. 입력 스펙트럼 사이의 보간을 부정하는 문장이 아니다. `src/swanmain.ftn:6941` `W1 = 0.001 * REAL(BGRIDP(6*IBGRID-3))`; `src/swanmain.ftn:6943` `W2 = 1.-W1`. `src/swanmain.ftn:6945–6946`의 `CALL SINTRP`는 결과 배열로 `AC2(1,1,INDXGR)`를 넘긴다. `src/swanser.ftn:4412,4418,4535`는 출력 배열 `FL`을 대입하거나 0으로 초기화한다. [10-13 전수 검증 보완]

전파 단계의 유입·유출 처리는 별도로 설명한다. swanuse PDF 20쪽 / 인쇄 12쪽: “accepts only … incoming … replaces … outgoing … with computed outgoing components”. `src/swancom1.ftn:3299` `IF (KCGRD(2) .LE. 1) RETURN`; `src/swancom1.ftn:3300` `IF (.NOT.ONED .AND. (KCGRD(3).LE.1)) RETURN`.

### STAT vs NONSTAT in RBFILE

At `[file=src/swanmain.ftn line=7724-7750]` and `[file=src/swanmain.ftn line=8033-8057]`:
- Stationary file → single spectrum, no time interpolation
- Nonstationary file → maintains old + new spectra, linearly interpolates in time using weight `W1` before `SNEXTI` applies them

## D. Internal data structures

### BSPCDAT (per-file metadata)

`[file=src/swmod2.ftn line=672-677]`:
```fortran
TYPE BSPCDAT
  INTEGER :: BFILED(20)
  INTEGER :: BSPLOC(:)
  REAL    :: BSPDIR(:), BSPFRQ(:)
END TYPE
```
- `BFILED` — file unit + flags
- `BSPLOC` — mapping into global `BSPECS` index
- `BSPDIR/BSPFRQ` — file's spectral grid (used by CHGBAS for remapping)

### BSDAT (parametric spec definitions)

`[file=src/swmod2.ftn line=682-687]`:
```fortran
TYPE BSDAT
  INTEGER :: NBS
  INTEGER :: FSHAPE, DSHAPE
  REAL    :: SPPARM(4)   ! Hs, Tp, dir, dspr/power
END TYPE
```

### BGPDAT (point mapping)

`[file=src/swmod2.ftn line=692-695]`:
```fortran
TYPE BGPDAT
  INTEGER :: BGP(6)   ! the 6-tuple from SWBOUN
END TYPE
```

### Runtime arrays in swanmain

`[file=src/swanmain.ftn line=433-435]` and `[file=src/swanmain.ftn line=3673-3674]`:
- `BSPECS(MDC, MSC, NBSPEC, 2)` — old/new boundary spectra
- `BGRIDP(6 * NBGRPT)` — flattened mapping (`BGP` records concatenated)

### Boundary-point ID assignment

At `[file=src/swanpre2.ftn line=5629]`, `[file=src/swanpre2.ftn line=5717-5720]`, `[file=src/swanpre2.ftn line=5794-5797]`, `IBSP1`/`IBSP2` get assigned (= `NBSPEC + ...`) and weighted indexes are stored into `BGP(3..6)` for each computational boundary point.

## E. SHAPESPEC defaults

- **JONSWAP/TMA `GAMMA`**: 3.3 if not given — `[file=src/swanpre2.ftn line=2805]` and `[file=src/swanpre2.ftn line=2817]`.
- **Period convention**: `PEAK` is default; `MEAN` is encoded by **negating `FSHAPE`** — `[file=src/swanpre2.ftn line=2821-2825]`.
- **`DSPR` mode**: parsed at `[file=src/swanpre2.ftn line=2828-2835]`; spread/power stored in `SPPARM(4)` via `DD` input at `[file=src/swanpre2.ftn line=3626-3635]`.

## Decision Guide — boundary debugging

| Symptom | Likely cause | Where to look |
|---------|--------------|---------------|
| Wrong wave height at boundary | Wrong shape: `MEAN` vs `PEAK` | `FSHAPE` sign at `swanpre2.ftn:2821-2825` |
| Nesting from coarse run loses high frequencies | 파일의 에너지밀도를 계산 격자로 재분배한 뒤 고유주파수로 나눈다. 입력 주파수 범위 위에는 작용밀도 꼬리를 붙인다. | `src/swanmain.ftn:8489` `LSPEC(ID,IS) = BAUX4(IS)/SPCSIG(IS)`; `src/swanmain.ftn:8495` `(SPCSIG(ISIGTA)/SPCSIG(IS))**(PWTAIL(1)+1)` |
| Boundary file format mismatch (WAM/WW3/SWAN) | Wrong reader called | Check `BOUND` keyword (`NE` vs `WAMN` vs `WW3`) at `swanpre2.ftn:2779-3002` |
| Spectrum injected at wrong points | Side/segment mismatch in coordinates | `SEG`/`SIDE` parse at `swanpre2.ftn:3063` (SEG) and `3329` (SIDE) |
| Time alignment wrong (nonstat) | `TIMCO` mismatch with file | `RBFILE` interpolation at `swanmain.ftn:8033-8057` |
| Nested run hangs at boundary | File length too short for run window | `RBFILE` end-of-file handling (search for IOSTAT) |

## Working Rules

1. 권고 순서와 선행 자료 의존성을 구분한다. BOUND SHAPE를 생략하면 기본 모양을 사용한다. `src/swanmain.ftn:1039` `FSHAPE = 2`.
2. 주파수와 방향의 스펙트럼 격자는 CGRID에서 지정한다. SET FREQ·SET DIR·SET TIMEFORMAT은 지원하는 명령문이 아니다. `src/swanpre1.ftn:1730` `CALL ININTG('MDC',MDC,'RQI',0)`; `src/swanpre1.ftn:1739` `CALL INREAL('FLOW',FRLOW,'STA',-999.)`; `src/swanpre1.ftn:1740` `CALL INREAL('FHIGH',FRHIG,'STA',-999.)`. SET의 전체 선택 분기는 `src/swanpre1.ftn:2169–2213`이다. [10-13 전수 검증 보완]
3. **Coordinate mode** (`LOC` vs `IJ`) must match the grid type chosen at `CGRID`. The SEGMENT path checks; the SIDE path infers.
4. Boundary spectra in `BSPECS` are **overwriting** `AC2` at boundary points each time step, not added. So a stale time stamp in the file silently propagates the wrong spectrum.

## Common Pitfalls

- **`MEAN` typo** — accidentally typing `MEAN` when you wanted `PEAK` flips frequency interpretation through the `FSHAPE` sign trick; result quietly wrong.
- `CHGBAS`는 구간별 상수 밀도를 겹치는 구간 길이에 따라 재분배한다. 스펙트럼 격자를 맞추려면 `CGRID`의 주파수·방향 설정을 맞춘다. `src/swanser.ftn:5354` `Y2(I2) = Y2(I2) + Y1(I1) * (RUPP-RLOW)`.
- **No CGRID consistency error** — SWAN won't fail on grid mismatch; you must check the `BSPDIR`/`BSPFRQ` recorded in the boundary file vs your run's `SPCSIG`/`SPCDIR`.
- **Side `CCW` vs `CLOCKW` confusion** — produces inverted endpoint order; spectra get swapped along the boundary.

## Next expansion

- `RBFILE` internals (the per-time-step header/spectrum read with all branches).
- ADCIRC-SWAN coupled boundary handling (separate, depends on the unstructured path).
- WAM-NEST format detail (the most fragile reader; older format).

## References

### Source files (Codex deep scan, 2026-05-06)

- `src/swanpre1.ftn` — `SWREAD` boundary dispatch, global-grid swap.
- `src/swanpre2.ftn` — `SWBOUN`, `BCFILE`, `BCWAMN`, `BCWW3N` (parsers + readers).
- `src/swanmain.ftn` — `SNEXTI`, `RBFILE`, `SINTRP` (runtime injection).
- `src/swmod2.ftn` — `BSPCDAT`, `BSDAT`, `BGPDAT` type definitions.

### Manual cross-reference

- `[file=pdf:swan:swantech]` ch.4 page 125 — Wave boundary and initial conditions.
- `[file=website:swan:node27]` — Boundary and initial conditions section.
- `[file=website:swan:node64]` — Wave boundary and initial conditions detail.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex source scan | 30+ file:line citations |
| Coverage | parsing flow, three nest readers, runtime injection, internal types, SHAPESPEC defaults |
| Out of scope | RBFILE per-format internals, ADCIRC-SWAN coupling |
| Review status | `review_required: true` |

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

빈 인용 칸은 `—`로 표시한다. 표의 절 번호는 각 행이 링크한 대조 보고서의 절 번호다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R3:CP-023 | 경계 파일 재분배와 꼬리 보간 | — | `src/swanmain.ftn:8482` `CALL CHGBAS (BSPFRQ, SPCSIG, 0., BAUX3, BAUX4, NFRE, MSC,`; `src/swanmain.ftn:8489` `LSPEC(ID,IS) = BAUX4(IS)/SPCSIG(IS)`; `src/swanmain.ftn:8495` `(SPCSIG(ISIGTA)/SPCSIG(IS))**(PWTAIL(1)+1)`; `src/swanmain.ftn:6941` `W1 = 0.001 * REAL(BGRIDP(6*IBGRID-3))`; `src/swanmain.ftn:6943` `W2 = 1.-W1` | C 문서 누락 | 파일의 에너지밀도를 계산 격자로 재분배한 뒤 고유주파수로 나눈다. 입력 주파수 범위 위에는 작용밀도 꼬리를 붙인다. 경계 위치의 정수 가중값은 0.001배 한다. 4장에는 이 계산식이 없다. [R3](../../../_staging/recovery/compare/swan-theory-obstacles-setup-qc-bc-vs-code.md#5-차이-결론) |
| R3:CP-024 | 평균주기→첨두주기와 방향 퍼짐 | swantech PDF 125–126쪽 / 인쇄 117–118쪽의 4장; `online_doc/swanuse/node27.html:138–189`의 MEAN·DSPR 정의. | `src/swanser.ftn:4161` `MPER = PI2 * AM0 / AM1`; `src/swanser.ftn:4169` `IF (ABS(MPER-SPPARM(2)) .GT. 0.01*SPPARM(2)) THEN`; `src/swanser.ftn:4171` `PKPER = (SPPARM(2) / MPER) * PKPER`; `src/swanser.ftn:4194` `MS = MAX (FAC*DSPR**(-2) - 2., 1.)`; `src/swanser.ftn:4199` `CTOT = GAMMAF(0.5*MS+1.) / (SQRT(PI) * GAMMAF(0.5*MS+0.5))`; `src/swanser.ftn:4201` `CTOT = SQRT (0.5*MS/PI) / (1. - 0.25/MS)`; 평균주기 반복 조건은 `src/swanser.ftn:4141`이다. 방향 분기는 `src/swanser.ftn:4184–4202,4216–4224`다. | C 문서 누락 | swanuse BOUND SHAPESPEC 절(node27:138–189)은 MEAN과 DSPR의 의미를 이미 설명한다. C는 swantech 4장과 그 절에 없는 변환 알고리즘의 수치 조건에 한정한다. `IF (.NOT.LOGPM .AND. ITPER.LT.10) THEN`에서 평균주기를 구하고 `IF (ABS(MPER-SPPARM(2)) .GT. 0.01*SPPARM(2)) THEN`이면 첨두주기를 조정한다. `IF (DD.GT.23.) THEN`, `ELSEIF (DD.GT.17.) THEN`, 나머지 분기의 `FAC`는 각각 1.2, 1.096, 1.01이다. `IF (MS.LT.12.) THEN`은 감마함수 정규화를 쓰고 나머지는 근사식을 쓴다. `IF (ACOS .GT. 0.) THEN`에서 `CDIR = CTOT * MAX (ACOS**MS, 1.E-10)`이다. 반대 반원에서는 `CDIR = 0.`이다. [R3](../../../_staging/recovery/compare/swan-theory-obstacles-setup-qc-bc-vs-code.md#5-차이-결론) [10-13 전수 검증 보완] |
| R3:NT-041 | 평균주기·첨두주기 오차 배율 | `source-analysis/swan-boundary-implementation.md:69` `half/twice the intended frequency`. | `src/swanser.ftn:4171` `PKPER = (SPPARM(2) / MPER) * PKPER` | B 문서 오기 | MEAN 입력은 지정 평균주기에 맞도록 첨두주기를 반복 조정한다. PEAK와 MEAN을 혼동했을 때의 주파수 오차를 항상 2배 또는 절반으로 정할 수 없다. [R3](../../../_staging/recovery/compare/swan-theory-obstacles-setup-qc-bc-vs-code.md#5-차이-결론) |
| R3:NT-042 | 경계 재분배와 격자 설정 명령 | `source-analysis/swan-boundary-implementation.md:122` `linear remapping`과 `SET FREQ` 및 `SET DIR`. | `src/swanser.ftn:5354` `Y2(I2) = Y2(I2) + Y1(I1) * (RUPP-RLOW)`; `src/swanser.ftn:5382` `Y2(I2) = Y2(I2) / CELLEN` | B 문서 오기 | `CHGBAS`는 구간별 상수 밀도를 겹치는 구간 길이에 따라 재분배한다. 스펙트럼 격자를 맞추려면 `CGRID`의 주파수·방향 설정을 맞춘다. `SET FREQ`와 `SET DIR` 명령 예는 삭제한다. [R3](../../../_staging/recovery/compare/swan-theory-obstacles-setup-qc-bc-vs-code.md#5-차이-결론) |
| R3:NT-043 | 경계 입력과 유출 전파 | `source-analysis/swan-boundary-implementation.md:138` `boundary spectra **overwrite**` 및 `not added, not averaged.` 노트 134–138행은 두 경계 스펙트럼의 위치 가중 보간을 명시한 뒤 그 결과를 AC2에 직접 쓴다고 설명한다. | `src/swanmain.ftn:6941` `W1 = 0.001 * REAL(BGRIDP(6*IBGRID-3))`; `src/swanmain.ftn:6943` `W2 = 1.-W1`; `src/swanmain.ftn:6945` `CALL SINTRP (W1, W2, BSPECS(1,1,K1,1), BSPECS(1,1,K2,1),`; `src/swanmain.ftn:6946` `&                    AC2(1,1,INDXGR), SPCDIR, SPCSIG)` | F 표기 차이 | 경계 입력 단계는 보간한 스펙트럼으로 AC2의 경계값을 덮어쓴다. 전파 단계의 유입·유출 처리는 별도로 설명한다. 노트의 덮어쓰기는 기존 AC2와 더하거나 평균하지 않는다는 뜻이다. 입력 스펙트럼 사이의 보간을 부정하는 문장이 아니다. [R3](../../../_staging/recovery/compare/swan-theory-obstacles-setup-qc-bc-vs-code.md#5-차이-결론) |
| R4:T1-174 | SEGMENT X·Y 이름 | swanuse PDF 56·58쪽 / 인쇄 48·50쪽: `XY < [x] [y] >`; swanuse PDF 132쪽 / 인쇄 124쪽: “Copy the name of the variable … literally followed by an = sign”. | `src/swanpre2.ftn:3079` `CALL READXY ('XP','YP',XP,YP, 'REP', -1.E10, -1.E10)`; `src/swanser.ftn:156` `CALL INDBLE (NAMX, XTMP, KONT, DBLE(XSTA)+DBLE(XOFFS))`; `src/ocpcre.ftn:608` `LENNM = LEN(NAAM)`; `src/ocpcre.ftn:609` `IF (NAAM.NE.ELTEXT(1:LENNM)) GOTO 20` | E 코드 결함 후보·강함 | BOUND SEGMENT XY의 이름 입력은 문서의 X·Y와 달리 XP·YP를 요구한다. INDBLE은 이 이름을 축약어로 매칭하지 않는다. 위치 숫자 입력은 수용한다. 코드 자체 문법 주석도 X·Y이므로 주석과 구현이 불일치한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-175 | 병렬 비정규 경계 제한 | swanuse PDF 57쪽 / 인쇄 49쪽: “SEGMENT and VARIABLE are not supported … unstructured … in parallel mode.” | `src/swanpre2.ftn:3102` `IF ( PARLL ) THEN`; `src/swanpre2.ftn:3104` `IXG2 = ivertg(IX2)`; `src/swanpre2.ftn:3108` `CALL SWREDUCE( IXG2, 1, SWINT, SWMAX )`; `src/swanpre2.ftn:3210` `ITMP = MINLOC(ABS(blist(:,JBG)-IXG2))`; `src/swanpre2.ftn:3826` `XC2 = xcugrdgl(IX)` | B 문서 오기 | 병렬 비정규 SEGMENT·VARIABLE 경로가 있다. 문서의 일괄 미지원 문장은 수정해야 한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-176 | 비정규 경계 순서 | swanuse PDF 58쪽 / 인쇄 50쪽: “The order must be counterclockwise!” | `src/swanpre2.ftn:3224` `!                 1) the wave spectrum along the given segment can be`; `src/swanpre2.ftn:3225` `!                    imposed in counterclockwise or clockwise direction`; `src/swanpre2.ftn:3268` `DET= (Y3-Y1)*(X2-X1)-(Y2-Y1)*(X3-X1)`; `src/swanpre2.ftn:3269` `IF (DET.GT.0.) THEN`; `src/swanpre2.ftn:3272` `IXB1 = MOD(IXB1,nbpt(JBG))+1`; `src/swanpre2.ftn:3275` `IXB1 = nbpt(JBG)-MOD(nbpt(JBG)+1-IXB1,nbpt(JBG))` | B 문서 오기 | 비정규 SEGMENT는 시계·반시계 방향의 경계 목록 순회를 모두 구현한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-182 | WAM CRAY 생략 | swanuse PDF 61쪽 / 인쇄 53쪽의 문법표는 `UNFormatted` 아래 `-> CRAY`를 표시한다. | `src/swanpre2.ftn:4615` `CALL INKEYW ('REQ', ' ')`; `src/ocpcre.ftn:342` `IF (ELTYPE.EQ.'INT') THEN`; `src/ocpcre.ftn:343` `CALL MSGERR (2, 'Data field skipped:'//ELTEXT)`; `src/swanpre2.ftn:4619` `CALL IGNORE ('CRAY')`; `src/swanpre2.ftn:4641` `CALL INDBLE('XGC',XLON0,'STA',-999.D0)` | E 코드 결함 후보·강함 | WAM UNFORMATTED 뒤에서 기본 CRAY를 생략하고 위치 숫자를 쓰면 INKEYW의 REQ 읽기가 그 숫자를 건너뛴다. 뒤의 CRAY 기본 분기는 이미 소비한 좌표를 복원하지 않는다. CRAY를 명시한 경우와 줄 끝에서 기본 분기로 가는 경우는 이 숫자 소비 문제와 구분한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-185 | YGC의 좌표 종류 | swanuse PDF 62–63쪽 / 인쇄 54–55쪽: 두 YGC 설명 모두 “longitude of south-west corner”. | `src/swanpre2.ftn:4642` `CALL INDBLE('YGC',XLAT0,'STA',-999.D0)`; `src/swanpre2.ftn:5365` `CALL INDBLE('YGC',XLAT0,'REQ',-999.D0)`; `src/swanpre2.ftn:4774` `YP1 = YPC + LENDEG*(YPWAM(IBNC1)-XLAT0)`; `src/swanpre2.ftn:5373` `YP2 = YPC + LENDEG*(XLAT-XLAT0)` | B 문서 오기 | WAM·WW3의 YGC는 남서쪽 기준점의 위도이다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-187 | WW3 기준점 기본값 | swanuse PDF 63–64쪽 / 인쇄 55–56쪽은 “Default: the location of the first spectrum”이라고 적는다. 같은 PDF 64 / 인쇄 56은 “if … Cartesian … values must be provided”라고 적는다. | `src/swanpre2.ftn:5358` `IF (KSPHER.EQ.0) THEN`; `src/swanpre2.ftn:5363` `IF (IBOUNC.EQ.1) THEN`; `src/swanpre2.ftn:5364` `CALL INDBLE('XGC',XLON0,'REQ',-999.D0)`; `src/swanpre2.ftn:5365` `CALL INDBLE('YGC',XLAT0,'REQ',-999.D0)` | B 문서 오기 | 직교좌표 WW3 입력의 XGC·YGC는 필수이다. 같은 문서의 마지막 주의문을 따른다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-238 | FORMAT 2 문자열 | — | `src/ocpmix.ftn:723` `CALL ININTG ('IDFM', IDFM, 'NSKP', 2)`; `src/ocpmix.ftn:728` `CALL INCSTR ('FORM', RFORM, 'REQ', ' ')` | C 문서 누락 | FORMAT 2 뒤에 Fortran 형식 문자열을 지정할 수 있다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-239 | 목록 첫 이름의 36자 제한 | — | `src/ocpmix.ftn:684` `READ(NDSL, '(A36)') FILENM`; `src/ocpmix.ftn:1054` `READ (NDSL, '(A)', END=930) FILENM`; `src/swanpre2.ftn:4610` `READ (NDSL,'(A36)') FILENM`; `src/swmod1.ftn:232` `PARAMETER (LENFNM=140)` | C 문서 누락 | SERIES·WAM 목록의 첫 파일 이름은 36자만 읽는다. SERIES의 후속 이름은 140자 버퍼 길이까지 읽는다. 문서에 없는 항목별 제한으로 적는다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-241 | dd 검사·FILE 재사용 | — | `src/swanpre2.ftn:3627` `IF ((SPPARM(4).GT.360. .OR. SPPARM(4).LT. 0.).AND.`; `src/swanpre2.ftn:3628` `&            .NOT.(EQREAL(SPPARM(4),OVEXCV(16)))) THEN`; `src/swanpre2.ftn:3635` `IF (SPPARM(4).LE. 0.) THEN`; `src/swanpre2.ftn:3640` `&            SPPARM(4)*DDIR**2/2. .GT. 1.) THEN`; `src/swanpre2.ftn:3789` `CALL INCSTR ('FNAME', FILENM, 'STA', ' ')`; `src/swanpre2.ftn:3791` `IF (FILENM.NE.'    ') THEN` | C 문서 누락 | BOUND PAR의 POWER에서 dd가 0 이하이면 오류를 낸다. VARIABLE FILE의 첫 이름은 필수이다. 후속 빈 이름은 직전 파일을 계속 참조한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-301 | MEAN·PEAK의 고정 배수 | `source-analysis/swan-boundary-implementation.md:69`의 `half/twice` | `src/swanser.ftn:4171` `PKPER = (SPPARM(2) / MPER) * PKPER` | B 문서 오기 | MEAN 입력은 적분 평균주기에 맞춰 피크주기를 반복 조정한다. 항상 절반·두 배라는 관계는 없다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R7:H-566 | WAM CDATE 컴파일 지정 | `website/modifications/modifications.htm:567` `The format of CDATE for WAM nesting can be specified at the compile level. See the Implementation Manual.`; `website/modifications/modifications.htm:550–555`의 40.85 기록: `Note that the format of CDATE cannot be specified at the compile level anymore.` | `src/swanpre2.ftn:4643` `CALL ININTG('LWDATE',LWDATE,'STA',12)                               41.13`; `122b595:src/swanpre2.ftn:4471` `CALL ININTG('LWDATE',LWDATE,'STA',12)                               41.13`; `src/swanpre2.ftn:4730` `READ(NDSD) XLON, XLAT, CDATE(1:LWDATE), EMEAN, THQ, FMEAN` | A 판 차이 | 40.81의 CDATE 컴파일 설정은 40.85의 LWDATE 실행 입력으로 대체되었다. 41.45와 현재 코드도 LWDATE로 읽을 문자열 길이를 정한다. git 대조 기준 커밋은 `122b595`(2023-02-28 공개 41.45)이다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) [10-13 전수 검증 정정] |
