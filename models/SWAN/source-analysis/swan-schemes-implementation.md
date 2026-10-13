---
title: "swan schemes implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-schemes-implementation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시. 2026-10-13 recovery 대조 보고서 R1–R8 반영"
last_source_check: "2026-10-13 (recovery 대조 반영)"
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# SWAN higher-order schemes — SORDUP, SANDL, GSE, FLUXLIM

## Scope note

정렬 격자의 정상 기본은 SORDUP이다. 정렬 격자의 비정상 기본은 S&L이다. 비정렬 공간 수송은 BSBT이다. `src/swanmain.ftn:1179–1180`의 원문은 `PROPSS = 2`와 `PROPSN = 3`이다. [R1 §4](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#4-노트-대조와-수정안).

## Source basis

Codex deep scan 2026-05-06 of `src/swancom1.ftn` (ACTION dispatch + flag management), `src/swancom5.ftn` (`STRSXY`, `SORDUP`, `SANDL`, `SWFLXD`), `src/swanpre1.ftn` (PROP parser).

## A. `PROPSL` flag — values and life cycle

| Variable | Default | Meaning |
|----------|---------|---------|
| `PROPSC` | 1 (set per stationary/nonstat) | global selection: `PROPSS` (stat) or `PROPSN` (nonstat) |
| `PROPSS` | 2 (SORDUP) | stationary scheme |
| `PROPSN` | 3 (SANDL) | nonstationary scheme |
| `PROPSL` | 1 (BSBT) | local-per-point scheme; degraded from PROPSC when stencil leaves domain |

Defaults at `[file=src/swanmain.ftn line=1179-1183]`. Stationary/nonstat selection at `[file=src/swanmain.ftn line=6354-6358]`.

`PROPSL = PROPSC` initialized at `[file=src/swancom1.ftn line=3052]`. Then locally degraded:
- to BSBT (`1`) or even no propagation (`0`) at points where the higher-order stencil hits domain edge / dry / obstacle — `[file=src/swancom1.ftn line=3099-3233]`

`PROP BSBT` parser branch sets both `PROPSN=1` and `PROPSS=1` at `[file=src/swanpre1.ftn line=793-795]`. **No parser branch explicitly sets `PROPSC=2` or `PROPSC=3`** — those values come from defaults; user choice is "use BSBT or use the defaults". DIFFRACTION command silently forces both to BSBT at `[file=src/swanmain.ftn line=4094-4095]`. 적용 조건은 `src/swanmain.ftn:4090`의 `IF ( IDIFFR.EQ.1 ) THEN`이다. `src/swanmain.ftn:4094–4095`의 원문은 `PROPSN = 1`과 `PROPSS = 1`이다. GEN4/QC와 병용할 때 회절을 끄는 안내·경고와 별도 동작이다. [R3:NT-048](../../../_staging/recovery/compare/swan-theory-obstacles-setup-qc-bc-vs-code.md#4-노트-대조와-수정안).

## B. SORDUP (`PROPSL = 2`, stationary higher-order)

- Dispatch: `[file=src/swancom1.ftn line=5401-5404]` — `IF (PROPSL.EQ.2) CALL SORDUP(...)`
- Subroutine entry: `SUBROUTINE SORDUP` at `[file=src/swancom5.ftn line=2238]`
- Adds 2nd-order upwind stencil with extra points `KCGRD(6)`, `KCGRD(7)`:
  - Form: `1.5 φ_i - 2 φ_{i-1} + 0.5 φ_{i-2}` (3-point upwind)
  - Diagonal scaling: `+1.5` `[file=src/swancom5.ftn line=2467, 2473-2476]`
  - RHS: `+2`, `-0.5` `[file=src/swancom5.ftn line=2498, 2504-2507]`
- Stencil expansion: ICMAX from 3 (BSBT) to **7** for SORDUP at `[file=src/swancom1.ftn line=999-1001]`

**Stationary-only enforcement**: hard error if `NSTATC == 1` at `[file=src/swancom5.ftn line=2420-2422]`. (Use SANDL for nonstationary higher-order.)

## C. SANDL — Stelling & Leendertse (`PROPSL = 3`, nonstationary higher-order)

The "SecondOrder" scheme isn't named that in code; the actual subroutine is `SANDL`.

- Dispatch: `[file=src/swancom1.ftn line=5396-5400]` — `IF (PROPSL.EQ.3) CALL SANDL(...)`
- Subroutine: `SUBROUTINE SANDL` at `[file=src/swancom5.ftn line=2566]`
- Stencil: ICMAX = **13** at `[file=src/swancom1.ftn line=996-998]` (largest of the three schemes)

### Implicit time integration

`SANDL` adds time term to matrix at `[file=src/swancom5.ftn line=3033-3034]`:
```
IMATDA += FXY1 + RDTIM
IMATRA += FXY2 + ACOLD * RDTIM
```
`ACOLD` selection mirrors BSBT: `AC2` if `ITERMX==1` else `AC1` `[file=src/swancom5.ftn line=3028-3032]`.

### Mixed old/new-time transport

Old-time velocities `CAX1, CAY1` are pre-computed in ACTION for nonstat `PROPSL=3` at `[file=src/swancom1.ftn line=3302-3333]`. They appear in RHS terms at `[file=src/swancom5.ftn line=2964-2971, 2982-2997, 3028-3032]`.

### Higher-order coefficients

Fractional weights `0.83333, 1.25, -0.5, 0.08333, 0.25` at `[file=src/swancom5.ftn line=2940-2971, 2975-2997, 3033-3034]` — these implement the Stelling & Leendertse 4-point scheme.

### Hard mode-compatibility checks

- `PROPSC=2` (SORDUP) **disallowed in nonstat** at `[file=src/swanmain.ftn line=6564-6568]`
- `PROPSC=3` (SANDL) **disallowed in stat** — same place

SORDUP와 비정상 모드의 충돌은 오류 수준 3이다. `src/swanmain.ftn:6564–6568`의 원문은 `IF (PROPSC.EQ.2 .AND. NSTATC.GT.0) THEN`, `CALL MSGERR (3, 'SORDUP scheme only in stationary run')`, `IF (PROPSC.EQ.3 .AND. NSTATC.EQ.0) THEN`, `CALL MSGERR (3, 'S&L scheme not in stationary run')`이다.

## D. Choice consequences (matrix & stability)

| Scheme | Stencil | Diagonal | RHS | CFL note |
|--------|---------|----------|-----|----------|
| BSBT (`PROPSL=1`) | `ICMAX=3` (3-point upwind) | `FXY1` from local coeffs | `FXY2` from points 2/3 | unconditionally stable (implicit BSBT) |
| SORDUP (`PROPSL=2`) | `ICMAX=7` | `+1.5 ×` higher-order | mixed `+2/-0.5` | stationary only; iteration convergence may slow |
| SANDL (`PROPSL=3`) | `ICMAX=13` | mixed old/new-time | fractional 0.83/1.25/-0.5/0.08/0.25 | nonstat; CFL warning fires if MYU>10 |

`STRSXY` (BSBT) coeff assembly: `[file=src/swancom5.ftn line=2148-2156, 2183-2190]`.

## E. GSE (Garden Sprinkler Effect) handling

GSE is unphysical "spreading" of swell into rays/spokes when angular resolution is coarse. Anti-GSE diffusion smooths it out.

- Parser: `PROP GSE [WAVEAGE]` at `[file=src/swanpre1.ftn line=796-802]`. Warns if context is non-SANDL (`PROPSN.NE.3`) at `[file=src/swanpre1.ftn line=797-800]`.
- S&L 내부 적용은 정렬 격자에 한정한다. `IF (WAVAGE.GT.0.)` 블록은 `[file=src/swancom5.ftn line=2916-2935]`에 있다:
  - `DSS, DNN` (along-spoke, across-spoke diffusion magnitudes from wave age)
  - `DXX, DYY, DXY` (anisotropic 2D diffusion tensor)
- Adds anti-GSE diffusion correction to RHS via second-derivative-like terms: `FXY2 += ...` using `D11AC, D12AC, D22AC` at `[file=src/swancom5.ftn line=3000-3017]`.

비정렬 경로는 SwanTranspAc에서 SwanGSECorr를 호출한다. `src/SwanTranspAc.ftn90:135`의 원문은 `if ( WAVAGE > 0. ) call SwanGSECorr ( rhs, ac2, cgo, spcdir, idcmin, idcmax, isslow, isstop, trac0 )`이다. 비정렬 GSE는 현재 갱신 중인 `ac2`를 사용한다. 정렬 S&L의 이전 시간 `AC1` 보정과 다르다. 경계 절점에는 보정을 적용하지 않는다. `src/SwanGSECorr.ftn90:127`의 원문은 `if ( vert(ivert)%atti(VMARKER) == 1 ) return`이다. [R1 §4](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#4-노트-대조와-수정안).

## F. FLUXLIM (slope-limited theta-direction transport)

- Parser: `PROP FLUXLIM` sets `PROPFL=1`, `PNUMS(6)=0` at `[file=src/swanpre1.ftn line=803-805]`.
- Applied **only in directional `D` transport dispatch in ACTION** at `[file=src/swancom1.ftn line=5471-5479]`:
  - `PROPFL=0` → `STRSD` (default)
  - `PROPFL=1` → `SWFLXD` (limiter version)
- Not used in `STRSXY`/`SORDUP`/`SANDL` (XY propagation).

### Limiter formula in `SWFLXD`

PL-kappa slope limiter with `XKAP = PNUMS(6)`:
```
FACT = MIN(2., 0.5*(1+XKAP)*R + 0.5*(1-XKAP))
XLIM = MAX(0., MIN(2*R, FACT))
```
Anti-diffusive correction:
```
DFCOR = 0.5 * (CAP*XLIMP*(ACT0-ACT1) - CAN*XLIMN*(ACT3-ACT2))
```
at `[file=src/swancom5.ftn line=5308, 5352-5363, 5408-5418]`.

## Decision Guide

| Use case | Recommended scheme | Why |
|----------|-------------------|-----|
| Stationary engineering hindcast | SORDUP (default `PROPSS=2`) | better accuracy than BSBT, no time-step constraint |
| Stationary with spectral surf-zone breaking | BSBT (`PROP BSBT`) | SORDUP iteration may stall on stiff source terms |
| Nonstationary storm hindcast | SANDL (default `PROPSN=3`) + GSE | accurate for swell propagation, GSE prevents spokes |
| Nonstat with large CFL (DT cannot be reduced) | BSBT (`PROP BSBT`) | unconditionally stable but more dissipative |
| Theta-direction sharp gradients (refraction near coast) | enable `PROP FLUXLIM` | slope-limited transport in θ |
| Diffraction needed | (forced) BSBT | SWAN auto-disables higher-order with diffraction |

## Working Rules

1. **`PROPSL` is per-grid-point**, demoted from `PROPSC` near edges/obstacles. So a "SORDUP" run actually runs BSBT at the boundaries — visible in spurious results if you analyze near boundaries.
2. S&L 내부 적용은 정렬 격자에 한정한다. 비정렬 경로는 SwanTranspAc에서 SwanGSECorr를 호출한다. `src/SwanTranspAc.ftn90:135`의 원문은 `if ( WAVAGE > 0. ) call SwanGSECorr ( rhs, ac2, cgo, spcdir, idcmin, idcmax, isslow, isstop, trac0 )`이다.
3. **`FLUXLIM` is θ-only** — it doesn't affect XY propagation.
4. **DIFFRACTION forces BSBT** — silently. If accuracy matters and you need higher-order, drop diffraction.
5. SORDUP와 비정상 모드의 충돌은 오류 수준 3이다. `src/swanmain.ftn:6564–6565`의 원문은 `IF (PROPSC.EQ.2 .AND. NSTATC.GT.0) THEN`과 `CALL MSGERR (3, 'SORDUP scheme only in stationary run')`이다.

## Common Pitfalls

- S&L 내부 적용은 정렬 격자에 한정한다. 비정렬 경로는 SwanTranspAc에서 SwanGSECorr를 호출한다. [R1 §4](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#4-노트-대조와-수정안).
- Comparing SORDUP vs BSBT residuals across boundary points — SORDUP degrades to BSBT there, so the comparison is degenerate near boundaries.
- `FLUXLIM` with PNUMS(6) at default 0 — gives the most diffusive limiter; tune `PNUMS(6)` toward 0.5–1 for sharper transport.
- Switching `PROPSS` ↔ `PROPSN` mid-run via successive `PROP` commands — only the LAST one applied wins (parser overwrites globals).

## References

- `src/swanpre1.ftn` — `PROP` parser.
- `src/swancom1.ftn` — ACTION dispatch, `PROPSL` degradation logic, ICMAX selection.
- `src/swancom5.ftn` — `STRSXY` (BSBT), `SORDUP`, `SANDL`, `SWFLXD` (FLUXLIM).
- `src/swanmain.ftn` — defaults, `PROPSC = PROPSS/PROPSN` selection, mode-compatibility checks.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex scan | 30+ file:line citations |
| Coverage | flag values, SORDUP, SANDL, GSE, FLUXLIM, mode compatibility |
| Review status | 2026-10-13 recovery 대조 보고서 R1–R8 반영 |

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R1:TN-044 | 문서 식 (3.9) | swantech PDF 81쪽 / 인쇄 73쪽, (3.9): $\left(\frac{10(c_xN)_i-15(c_xN)_{i-1}+6(c_xN)_{i-2}-(c_xN)_{i-3}}{12\Delta x}\right)_{j,l,m}^{n}+\left(\frac{(c_xN)_{i+1}-(c_xN)_{i-1}}{4\Delta x}\right)_{j,l,m}^{n-1}$. 첫 sweep의 $c_x>0$, $c_y>0$ 조건이다. | `src/swancom5.ftn:2940`: `FXY1 = 0.83333*(RDX(1)+RDX(2)) * CAX(ID,IS,1)`; 2951·2955·2959의 `+1.25`, `-0.5`, `+0.08333`; 2964–2965: `+(0.25*RDX(1)) * (CAX1(ID,IS,2) * AC1(ID,IS,IND2)`와 하류항 차감. | C 문서 누락 | 식 구조와 부호는 같다. 코드는 $10/12$, $1/12$를 각각 `0.83333`, `0.08333`으로 절단한다. C는 swantech §3.2.1이 이 소수 계수 절단을 적지 않는 점이다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) | [10-13 전수 검증 정정]
| R1:TN-045 | 문서 식 (3.10) | swantech PDF 81쪽 / 인쇄 73쪽, (3.10): $\left(\frac{10(c_yN)_j-15(c_yN)_{j-1}+6(c_yN)_{j-2}-(c_yN)_{j-3}}{12\Delta y}\right)_{i,l,m}^{n}+\left(\frac{(c_yN)_{j+1}-(c_yN)_{j-1}}{4\Delta y}\right)_{i,l,m}^{n-1}$. 첫 sweep의 $c_x>0$, $c_y>0$ 조건이다. | `src/swancom5.ftn:2941`: `&         + 0.83333*(RDY(1)+RDY(2)) * CAY(ID,IS,1)`; 2954·2958·2962·2970–2971의 같은 계수. | C 문서 누락 | 코드의 y 방향 식도 TN-044와 같은 소수 계수 절단을 사용한다. C는 swantech §3.2.1의 이 절단값 누락이다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) | [10-13 전수 검증 정정]
| R1:TN-058 | 문서 식 (3.14) | swantech PDF 84쪽 / 인쇄 76쪽, (3.14): $c_\sigma N\big\vert_{i,j,l+1/2,m}=\begin{cases}(1-0.5\mu)c_\sigma N\big\vert_{i,j,l,m}+0.5\mu c_\sigma N\big\vert_{i,j,l+1,m},&\text{if shifting to higher frequencies}\\(1-0.5\mu)c_\sigma N\big\vert_{i,j,l+1,m}+0.5\mu c_\sigma N\big\vert_{i,j,l,m},&\text{if shifting to lower frequencies}\end{cases}$ | `src/swancom5.ftn:3290–3292`: `PNH = 1. / (2. * DS)`; `PN1 =  (1. - PNUMS(7) ) * PNH`; `PN2 =  (1. + PNUMS(7) ) * PNH`. | F 표기 차이 | 해석: $\mu=1-\mathrm{PNUMS}(7)$이면 풍상 계수 $(1+\mathrm{PNUMS}(7))/2=1-\mu/2$이다. 코드 기본 대입은 `src/swanmain.ftn:1234`의 `PNUMS(7)  = 0.5`이다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-059 | 문서 식 (3.15) | swantech PDF 84쪽 / 인쇄 76쪽, (3.15): $c_\theta N\big\vert_{i,j,l,m+1/2}=\begin{cases}(1-0.5\nu)c_\theta N\big\vert_{i,j,l,m}+0.5\nu c_\theta N\big\vert_{i,j,l,m+1},&\text{if counter-clockwise}\\(1-0.5\nu)c_\theta N\big\vert_{i,j,l,m+1}+0.5\nu c_\theta N\big\vert_{i,j,l,m},&\text{if clockwise}\end{cases}$ | `src/swancom5.ftn:3946–3948`: `PNH = 1. / (2. * DD)`; `PN1 =  (1. - PNUMS(6) ) * PNH`; `PN2 =  (1. + PNUMS(6) ) * PNH`. | F 표기 차이 | 해석: $\nu=1-\mathrm{PNUMS}(6)$이다. 기본 대입은 `src/swanmain.ftn:1232`의 `PNUMS(6)  = 0.5`이다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-063 | 부호 전환의 중심차분 | swantech PDF 85쪽 / 인쇄 77쪽: “central differences ($\nu=0$)”. 쪽 이미지 확인 | `src/swancom5.ftn:3988`: `PCD1 = PNH * C1`. | B 문서 오기 | 해석: 이 문장의 $\nu=0$은 (3.15)의 정의와 모순된다. 문서의 중심차분 값은 $\nu=1$이어야 한다. 코드의 `PNUMS(6)=0`과 혼동하면 안 된다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TC-018 | 선택적 방향 플럭스 제한기 SWFLXD | — | `src/swancom5.ftn:5308,5352–5362,5417`: `XKAP = PNUMS(6)`; `RAP = (ACT2-ACT0+1.E-12)/(ACT0-ACT1+1.E-12)`; `FACT  = MIN( 2., 0.5*(1.+XKAP)*RAP + 0.5*(1.-XKAP) )`; `XLIMP = MAX( 0., MIN(2.*RAP,FACT) )`; `DFCOR = 0.5*(CAP*XLIMP*(ACT0-ACT1)-CAN*XLIMN*(ACT3-ACT2))`.<br>`src/swancom1.ftn:5470–5479`의 실제 선택 호출. | C 문서 누락 | C는 swantech §3.2의 선형 혼합 플럭스 설명에 SWFLXD의 비선형 기울기 제한식이 없는 점이다. `IF ( IREFR.NE.0 ) THEN` 안의 `ELSE IF ( PROPFL.EQ.1 ) THEN`에서 호출한다. 비율의 분자와 분모에 각각 $10^{-12}$를 더한다. 방향 수송에 적용하는 선택 경로이다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TC-019 | 공간 stencil의 국소 차수 변경 | — | `src/swancom1.ftn:3099–3103,3134–3139`: `IF (IC.LE.3) THEN`; `PROPSL = 0`; `IF (PROPSC.GT.1) PROPSL = 1`; `IF (COMPDA(KCGRD(IC),JDP2).LE.DEPMIN) PROPSL = 1`; 비정상에서는 `IF (COMPDA(KCGRD(IC),JDP1).LE.DEPMIN) PROPSL = 1`. | C 문서 누락 | 고차 stencil의 영역 이탈·건조점에서 국소 BSBT로 바꾼다. 기본 세 점 자체가 없으면 공간 전파를 끄는 분기도 있다. 비정상 경로는 이전 시간 수심도 검사한다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TC-020 | 기법·시간 모드의 불일치 검사 | — | `src/swanmain.ftn:6564–6568`: `IF (PROPSC.EQ.2 .AND. NSTATC.GT.0) THEN`; `CALL MSGERR (3, 'SORDUP scheme only in stationary run')`; `IF (PROPSC.EQ.3 .AND. NSTATC.EQ.0) THEN`; `CALL MSGERR (3, 'S&L scheme not in stationary run')`.<br>swanuse PDF 92쪽 / 인쇄 84쪽의 PROP 설명. | C 문서 누락 | SORDUP의 정상 모드와 S&L의 비정상 모드 구분은 swanuse에도 있다. C는 swantech의 기법 설명에 모드 불일치 시 오류 수준 3을 보고하는 입력 검사 절차가 없는 점이다. 두 조건은 `IF (PROPSC.EQ.2 .AND. NSTATC.GT.0) THEN`과 `IF (PROPSC.EQ.3 .AND. NSTATC.EQ.0) THEN`이다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R5:PN-081 | 회절의 PROP 덮어쓰기 | PROP 기본값의 DIFFRACTION 예외. swanuse PDF 92쪽 / 인쇄 84쪽의 `default S&L` / `default SORDUP`. | `src/swanmain.ftn:4090` `IF ( IDIFFR.EQ.1 ) THEN`에서 대입한다. `src/swanmain.ftn:4094` `PROPSN = 1`, 4095 `PROPSS = 1`. | C | DIFFRACTION을 켜면 정상·비정상 전파 선택은 BSBT로 바뀐다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) | [10-13 전수 검증 보완]
| R5:PN-151 | PROP FLUXLIM | — | `src/swanpre1.ftn:804` `PROPFL   = 1`, 805 `PNUMS(6) = 0.`. | C | PROP FLUXLIM은 방향 플럭스 제한을 켜고 CDD를 0으로 만든다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
