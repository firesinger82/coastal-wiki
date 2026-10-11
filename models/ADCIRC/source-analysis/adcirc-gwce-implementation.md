---
title: "adcirc gwce implementation"
topic: general
canonical_source: self
citation_status: verified
last_source_check: 2026-10-11 (recovery 재판독 대조)
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-gwce-implementation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC GWCE solver — matrix assembly, time integration, JCG solve

## Scope

The Generalized Wave Continuity Equation is ADCIRC's mass-conservation equation for water surface elevation. This note documents matrix assembly, lumped vs consistent mass, time integration scheme, JCG solver dispatch, boundary contributions, and SAL (self-attraction & loading) integration.

## A. Matrix assembly

- Primary routine: `GWCE_New` at `[file=src/gwce.F line=237]`. Rebuild gated by `NCIFBLCK` at `[file=src/gwce.F line=427]` (`IF(NCChange.GT.0 .or. CGWCE_HDP)`).
- Lumping weights at `[file=src/gwce.F line=418-420]`:
  - `OnDiag = (1+ILump)*2`, `OffDiag = (1-ILump)`
  - `ILump=0` → consistent mass; `ILump=1` → diagonal-only (lumped)
- Mass + tau0 factors at `[file=src/gwce.F line=538-540]`: `MsFacLOnDiag`, `MsFacLOffDiag`
- Flux-gradient stiffness: `GA00DPAvgOAreaIE4*FDX/FDY` products into `Coef` at `[file=src/gwce.F line=564-592]`
- Friction/`Tau0Var` enters via `Tau0Avg[_S]` in mass-like factors at `[file=src/gwce.F line=517, 538-539, 607, 623]` — affects both consistent and lumped paths
- LHS assembly at `[file=src/gwce.F line=429-636]` (`Coef`/`Coefd`)
- RHS forcing assembly at `[file=src/gwce.F line=998-1617]`
- Boundary elimination modifies LHS at `[file=src/gwce.F line=638-673]`; RHS compensation via `OBCCoef` at `[file=src/gwce.F line=1846-1854]`
- `ILump` switch points: `[file=src/gwce.F line=141, 430, 455, 595, 709, 1846, 1856]`
- Memory allocation: `alloc_main11` (consistent) vs `alloc_main11_lumped` at `[file=src/gwce.F line=141-154]`

## B. Time integration

- `DT` enters matrix terms directly at `[file=src/gwce.F line=538-539, 623, 1429, 1741, 1758]`
- GWCE 조립은 `DT`를 사용한다 (`[file=src/gwce.F line=538]` `MsFacLOnDiag =OnDiag*AreaIE*(1.d0/DT+Tau0Avg_S/2.d0)/DT/12.d0`). 양수 `DTDP` 입력은 `DT`에 그대로 대입한다 (`[file=src/read_input.F line=2535]` `DT=DTDP`). 음수 `DTDP` 입력은 predictor-corrector를 켠다 (`[file=src/read_input.F line=2522]` `IF(DTDP.LT.0.d0) THEN`; `[file=src/read_input.F line=2523]` `CPRECOR    = .TRUE.`). 이 분기는 `DT`와 `DTDP`를 같은 양수 값으로 바꾼다 (`[file=src/read_input.F line=2528]` `DT=-DTDP`; `[file=src/read_input.F line=2529]` `DTDP=DT`).
- Three-time-level state in `GWCE_New_pc`: `ETA0, ETA1, ETA2` at `[file=src/gwce.F line=2514-2522]`
- Time weighting: `C00` (n-1) + `(A00+B00)` (n) for free-surface RHS at `[file=src/gwce.F line=1540-1543]`; corrector at `[file=src/gwce.F line=2851-2852]`
- State shift each step: `Eta1=Eta2`, optionally `Eta0=Eta1` at `[file=src/gwce.F line=1622-1631]`
- ETA2 update at `[file=src/gwce.F line=2007]` or `[file=src/gwce.F line=2020]`

GWCE는 θ라는 이름의 별도 입력값을 읽지 않는다 (`[file=src/read_input.F line=3010]` `READ(15,*) A00,B00,C00`). `A00·B00·C00`는 중력항의 새·현재·이전 수위 시간 가중치다 (`[file=src/read_input.F line=3010]` `READ(15,*) A00,B00,C00`; `[file=src/gwce.F line=516]` `GA00DPAvgOAreaIE4 = ALPHAL(IE)*A00*G*DPAvg*Cfac/AreaIE4`; `[file=src/gwce.F line=1540]` `&        - GDPAvgOAreaIE4_S0*( C00*( SFCXADJ*FDX1*E0XGrad2A+`; `[file=src/gwce.F line=1543]` `&                                    SFCYADJ*FDY1*E1YGrad2A ) )`). `A00`가 비영이면 새 수위 강성항이 좌변에 들어간다 (`[file=src/gwce.F line=516]` `GA00DPAvgOAreaIE4 = ALPHAL(IE)*A00*G*DPAvg*Cfac/AreaIE4`). 해석: θ라는 이름이 없다는 사실은 GWCE가 명시적이라는 뜻이 아니다 (`[file=src/gwce.F line=516]` `GA00DPAvgOAreaIE4 = ALPHAL(IE)*A00*G*DPAvg*Cfac/AreaIE4`). `FTHETA`는 혼합 바닥 마찰 법칙의 지수다 (`[file=src/nodalattr.F line=2471]` `&                     IFHYBF*(1+(HBREAK/H1)**FTHETA)**(FGAMMA/FTHETA)) ), ! hybrid`).

## C. Solver

- 일반 `GWCE_New`의 `ILump.eq.0` 경로는 `JCG`를 호출한다 (`[file=src/gwce.F line=2000]` `IF (ILump.eq.0) THEN ! default, fully consistent LHS`; `[file=src/gwce.F line=2003]` `CALL JCG(NP,MNP,MNEI,NEITAB,COEF,GWCE_LV,ETAS,`).
- 일반 `GWCE_New`의 `ELSE` 경로는 대각 역산을 수행한다 (`[file=src/gwce.F line=2009]` `ELSE ! lumped LHS`; `[file=src/gwce.F line=2016]` `ETAS(I) = GWCE_LV(I) * RDIAG`).
- `ITMAX` cap: `IPARM(1)=ITMAX` at `[file=src/gwce.F line=146]`, `[file=src/gwce.F line=2002]`
- Convergence tolerance: `RPARM(1)=CONVCR` at `[file=src/gwce.F line=150]`
- Iteration count returned in `IPARM(1)` → captured as `NUMITR` at `[file=src/gwce.F line=2005]`

## D. Boundary contributions

- Open-boundary harmonic synthesis: `ETA2(NBDI) += EMO*FF*RampElev*cos(AMIG*timeh + FACE - EFA)` at `[file=src/gwce.F line=1638-1650]`, driven by `NBFR`
- Aperiodic `fort.19` interpolation at `[file=src/gwce.F line=1659-1673]` using `ESBIN1/ESBIN2`
- Boundary topology (`NOPE, NETA, NBD, NBV, LBCODEI`) consumed via `USE BOUNDARIES` at `[file=src/gwce.F line=270-271]`, `[file=src/cstart.F line=64]`, `[file=src/hstart.F line=58]`
- Normal-flow / radiation / gradient boundary fluxes contribute to RHS at `[file=src/gwce.F line=1725-1834]`, per-`LBCODEI` formulas, `Tau0Var` coupling at `[file=src/gwce.F line=1740-1764, 1782-1805]`
- Elevation-specified boundaries: row/column modification on LHS at `[file=src/gwce.F line=652-673]`; scaled RHS enforcement at `[file=src/gwce.F line=1840-1861]`
- No-flux land suppression via `NODECODE` masking at `[file=src/gwce.F line=474-477, 1010-1015]`; dry/landlocked nodes init in cold start at `[file=src/cstart.F line=1221-1223, 1258-1260]`

## E. SAL integration (NTIP=2 path)

- Reader: `readSelfAttractionAndLoadingFile` at `[file=src/adcirc.F line=292-293]` — comment notes `fort.24`
- SAL added to tidal potential in hot start: `+ SALTMUL * SALTAMP(J,I) * COS(ARGSALT)` at `[file=src/hstart.F line=1522, 1530-1532]`
- GWCE consumes via `TiP1`/`TiPN*` at `[file=src/gwce.F line=1181-1184]`, used in forcing gradients at `[file=src/gwce.F line=1450-1452, 1462-1464]`
- So SAL-modified tidal potential propagates into GWCE RHS

## F. Wetting-drying mask

- Element wet/dry mask: `NCELE = NC1*NC2*NC3*NOFF(IE)` at `[file=src/gwce.F line=477, 605, 1015, 1074]`
- Any dry node (`NODECODE=0`) nulls that element's contribution
- Subgrid wetting/drying: `wetFracVertETA1/2` modifies LHS at `[file=src/gwce.F line=465-473, 541-547]` and RHS at `[file=src/gwce.F line=1055-1063, 1436-1439]`
- Initial dry-node logic in cold start: `[file=src/cstart.F line=1221-1231, 1258-1268]`
- No separate dry-node check inside GWCE — purely multiplicative masking via `NODECODE`

## Decision Guide — 진단 (트러블슈팅)

| Symptom | Likely cause | Source-level investigation |
|---------|--------------|----------------------------|
| Tidal amplitude wrong (지역 bias) | flux-gradient term + tau0 + bottom-friction interaction | Check `Tau0Var` + `FRIC` flow into `Coef` (`gwce.F:538-592`) |
| Iteration count high | poor preconditioning or stiff diagonals | `NUMITR` in stdout; tighten `CONVCR` |
| Boundary spike | tide block format wrong in fort.15 | `NBFR` block mismatch (`gwce.F:1638-1650`) |
| Mass loss at wet/dry front | `NCELE` masking issue | `gwce.F:477` dry-element zeroing |

## Working Rules

1. GWCE 행렬의 시간 간격은 `DT`다 (`[file=src/gwce.F line=538]` `MsFacLOnDiag =OnDiag*AreaIE*(1.d0/DT+Tau0Avg_S/2.d0)/DT/12.d0`). 입력 reader는 양수 `DTDP`를 `DT`에 대입한다 (`[file=src/read_input.F line=2535]` `DT=DTDP`). 음수 입력 경로도 부호 변환 뒤 `DTDP=DT`로 대입한다 (`[file=src/read_input.F line=2528]` `DT=-DTDP`; `[file=src/read_input.F line=2529]` `DTDP=DT`).
2. 일반 `GWCE_New`는 `ILump.eq.0`에서 `JCG`를 호출한다 (`[file=src/gwce.F line=2000]` `IF (ILump.eq.0) THEN ! default, fully consistent LHS`; `[file=src/gwce.F line=2003]` `CALL JCG(NP,MNP,MNEI,NEITAB,COEF,GWCE_LV,ETAS,`). 그 `ELSE` 경로는 대각 역산을 수행한다 (`[file=src/gwce.F line=2009]` `ELSE ! lumped LHS`; `[file=src/gwce.F line=2016]` `ETAS(I) = GWCE_LV(I) * RDIAG`). `GWCE_New_pc`는 같은 `ILump` 게이트 없이 `JCG`를 별도로 호출한다 (`[file=src/gwce.F line=3070]` `CALL JCG(NP,MNP,MNEI,NEITAB,COEF,GWCE_LV,ETAS,`). 확인하지 않음: 임의 `ILump·CPRECOR` 조합의 실행 지원과 성능.
3. **`Tau0Var` enters mass factors, not friction directly.** It weights the GWCE matrix; friction is separate via `FRIC` from Manning conversion.
4. **SAL = `fort.24` ASCII or NetCDF** with one block per tide constituent. NTIP=2 must be set.
5. **NUMITR > 50 iteration suggests stiff matrix** — increase `ITMAX`, tighten mesh, or check very-shallow elements.

## Common Pitfalls

- `IF ( (Tau0.le.-5.d0).and.(Tau0.gt.-6.d0) ) THEN`이면 다음 위치 입력 줄의 `Tau0FullDomainMin, Tau0FullDomainMax`를 읽는다 (`[file=src/read_input.F line=2505]` `IF ( (Tau0.le.-5.d0).and.(Tau0.gt.-6.d0) ) THEN`; `[file=src/read_input.F line=2506]` `READ(15,*) Tau0FullDomainMin, Tau0FullDomainMax`). 이 `READ`에는 생략을 허용하는 `IOSTAT` 처리가 없다 (`[file=src/read_input.F line=2506]` `READ(15,*) Tau0FullDomainMin, Tau0FullDomainMax`). 해석: 입력 줄을 생략하면 reader가 다음 위치 입력을 이 두 값으로 소비한다 (`[file=src/read_input.F line=2506]` `READ(15,*) Tau0FullDomainMin, Tau0FullDomainMax`). `LoadTau0MinMax`가 거짓이면 후속 경로는 두 위치 입력값을 절점 최소·최대 값에 복사한다 (`[file=src/nodalattr.F line=1979]` `IF ( .not.LoadTau0MinMax ) THEN`; `[file=src/nodalattr.F line=1981]` `Tau0MinMax(I,1) = Tau0FullDomainMin`; `[file=src/nodalattr.F line=1982]` `Tau0MinMax(I,2) = Tau0FullDomainMax`).
- **Boundary ELEVALPHA wrong** — phases shifted across NBFR block; check `read_input.F:3445-3470` parse order.
- **Hot-restart with different `ILump`** — matrix shape differs; restart fails or silently runs lumped.
- **NTIP=2 without fort.24** — runtime error or zero SAL contribution.

## References

- `src/gwce.F` — main solver.
- `src/momentum.F` — companion momentum equations.
- `src/cstart.F` / `src/hstart.F` — cold/hot start paths.
- `src/adcirc.F` — high-level driver, NTIP/SAL init.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-07 |
| Codex scan | 30+ file:line citations |
| Coverage | matrix assembly, time integration, JCG, boundary, SAL, wet/dry mask |
| Review status | `review_required: true` |
