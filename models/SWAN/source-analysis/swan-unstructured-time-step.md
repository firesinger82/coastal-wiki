---
title: "SWAN unstructured time-step driver — SwanCompUnstruc.ftn90 verified"
topic: swan
canonical_source: self
citation_status: verified
verification_method: "현재 src/SwanCompUnstruc.ftn90는 1678줄이다. 헤더 1–85줄과 본문의 인용 구현부를 원문 대조했다. 헤더 50–64줄의 변경 이력은 15항목이다. swantech 제8장의 인용 쪽과 R1·R8 최종 결론을 대조했다." # [10-13 전수 검증 정정]
last_source_check: "2026-10-13 (recovery 대조 반영)"
note_author: "Claude Opus 4.7 (1M context) raw source direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — full header verbatim + author 14명 + version history 13개"
verification_date: 2026-06-01
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
  - models/SWAN/source-analysis/swan-foundation.md
  - models/SWAN/source-analysis/swan-bragg-scattering.md
  - models/SWAN/source-analysis/swan-quasi-coherent.md
  - models/SWAN/source-analysis/swan-adcirc-coupling.md
  - models/SWAN/source-analysis/swan-gse-correction.md
---

## Scope

SwanCompUnstruc.ftn90 — **unstructured mesh 의 time-step driver** (1684 lines). SWAN unstructured (unSWAN) 의 핵심 entry. 40.80 (2007-07 Zijlema) 신설 → 41.91 (2022-02) 까지 13개 메이저 update. Tech Ch 8 (p.135-147).

## Source basis

- `SwanCompUnstruc.ftn90` (1684 lines, single subroutine + nested helpers)
- Tech Ch 8 (Unstructured mesh implementation, p.135-147)
- 8.1 Description / 8.2 Grid generation / 8.3 Numerical method (discretization + sweeping) / 8.4 Interpolation / 8.5 Force / 8.6 Diffusion-like / 8.7 Conservation of action

## 1. Header verbatim (line 1, 32-65)

```fortran
subroutine SwanCompUnstruc(ac2, ac1, compda, spcsig, spcdir, xytst, cross, it)
!   Programmer: Marcel Zijlema
!
!   Authors                                Updates
!   40.80: Marcel Zijlema                  40.80, July 2007: New subroutine
!   40.85: Marcel Zijlema                  40.85, August 2008: + propagation/generation/redistribution output
!   40.95: Marcel Zijlema                  40.95, June 2008: parallelization of unSWAN
!   41.02: Marcel Zijlema                  41.02, February 2009: implementation of diffraction
!   41.07: Marcel Zijlema                  41.07, August 2009: bug fix: never-ending sweep prevented
!   41.10: Marcel Zijlema                  41.10, August 2009: parallelization using OpenMP directives
!   **41.20: Casey Dietrich                41.20, June 2010: extension to tightly coupled ADCIRC+SWAN model**
!   41.60: Marcel Zijlema                  41.60, July 2015: more accurate gradients of depth/wave number for turning rate
!   41.63: Marcel Zijlema                  41.63, August 2015: efficiency improved; ONE sweep per iteration (vs undetermined)
!   41.67: Marcel Zijlema                  41.67, August 2017: more accurate gradients of ambient currents
!   41.68: Marcel Zijlema                  41.68, August 2015: fixed number of sweeps per iteration
!   **41.80: Dirk Rijnsdorp and Ad Reniers 41.80, September 2021: adding Bragg scattering**
!   **41.90: Gal Akrish, Pieter Smit and Marcel Zijlema 41.90, October 2021: adding QC scattering**
!   **41.91: Marcel Zijlema                41.91, February 2022: adding QC surf breaking**
```

헤더의 저자 이름은 중복을 제외하면 Marcel Zijlema, Casey Dietrich, Dirk Rijnsdorp, Ad Reniers, Gal Akrish, Pieter Smit의 6명이다. Casey Dietrich의 41.20 이력은 [ADCIRC+SWAN 결합](swan-adcirc-coupling.md)의 확장으로 적혀 있다. (`src/SwanCompUnstruc.ftn90:32–46,56`) [10-13 전수 검증 정정]

## 2. Purpose + Method (line 65-85 verbatim)

> "**Performs one time step for solution of wave action equation on unstructured grid**"
>
> "A vertex-based algorithm is employed in which the variables are stored at the vertices of the mesh. The equation is solved in each vertex assuming a constant spectral grid resolution in all vertices. **The propagation terms in both geographic and spectral spaces are integrated implicitly. Sources are treated explicitly and sinks implicitly**. The calculation of the source terms is carried out in the original SWAN routines, e.g., SOURCE."
>
> "The wave action equation is solved iteratively. A number of iterations are carried out until convergence is reached. In each iteration, **a fixed number of sweeps are carried out** (41.68). Per sweep direction, a loop over ordered vertices is executed. The solution of each vertex must be updated geographically before proceeding to the next one."

## 3. 핵심 algorithm 특성

### 3.1 Vertex-based storage

Tech §8.1 + 본 module: **action density `ac2` 는 vertex 에 저장** (cell-centered 아님). Triangle mesh 의 vertex = node.

### 3.2 Implicit propagation + Explicit/Implicit sources

| Term | 처리 |
|---|---|
| 공간 propagation (∇·c_g N) | **Implicit** |
| 스펙트럼 propagation (c_σ, c_θ in σ-θ space) | **Implicit** |
| Source 항 (S_in, S_nl) | **Explicit** |
| Sink 항 (S_ds dissipation) | **Implicit** |

→ Tech §3.3 Solution algorithm 의 unstructured 변형. Implicit propagation = sweep-based Gauss-Seidel iteration.

### 3.3 Sweep-based iteration

- **41.63 변화**: 이전 "undetermined number of sweeps per iteration" → "ONE sweep per iteration" (efficiency 개선)
- **41.68 이력 주석**: `src/SwanCompUnstruc.ftn90:59`의 원문은 `!   41.68,   August 2015: introduction of a fixed number of sweeps per iteration`이다. 첫 세 반복과 제한된 방향 구간은 nsweep을 쓴다. 전 방향 스펙트럼의 네 번째 이후 반복은 한 sweep을 쓴다. `src/SwanCompUnstruc.ftn90:124`의 원문은 `itswp = 4`이다. `src/SwanCompUnstruc.ftn90:825–831`의 `if ( iter < itswp ) then` 및 `elseif ( .not.FULCIR ) then`은 `n = nsweep`을 선택한다. 나머지는 `n = 1`이다.
- 각 sweep direction마다 ordered vertex loop. vertex order = sweep direction에 따라 다름 (Tech §8.3.2 sweeping algorithm).

## 4. 41.x history matrix

| Version | Year | Author | 변화 |
|---|---|---|---|
| 40.80 | 2007-07 | Zijlema | **신설** unstructured time-step |
| 40.85 | 2008-08 | Zijlema | propagation/generation/redistribution 출력 |
| 40.95 | 2008-06 | Zijlema | **unSWAN 병렬화** |
| 41.02 | 2009-02 | Zijlema | **diffraction** ([swan-diffraction-obstacles](swan-diffraction-obstacles.md)) 통합 |
| 41.07 | 2009-08 | Zijlema | never-ending sweep bug fix |
| 41.10 | 2009-08 | Zijlema | **OpenMP** 병렬화 |
| **41.20** | **2010-06** | **Casey Dietrich** | **tightly coupled ADCIRC+SWAN** ([swan-adcirc-coupling](swan-adcirc-coupling.md)) |
| 41.60 | 2015-07 | Zijlema | depth/wave number gradient 정확도 ↑ (turning rate) |
| 41.63 | 2015-08 | Zijlema | one sweep per iteration efficiency |
| 41.67 | 2017-08 | Zijlema | ambient current gradient 정확도 ↑ |
| 41.68 | 2015-08 | Zijlema | fixed sweep count per iteration |
| **41.80** | **2021-09** | **Rijnsdorp+Reniers** | **Bragg scattering** ([swan-bragg-scattering](swan-bragg-scattering.md)) 통합 |
| **41.90** | **2021-10** | **Akrish+Smit+Zijlema** | **QC scattering** ([swan-quasi-coherent](swan-quasi-coherent.md)) 통합 |
| 41.91 | 2022-02 | Zijlema | **QC surf breaking** 추가 |

`src/SwanCompUnstruc.ftn90` 전체에서 대소문자를 구분하지 않고 센 `QCM` 문자열은 12회이다. 이 문자열을 포함한 줄은 11줄이다. `Bragg` 문자열은 3회이다. `IEM`·`GSECorr`·`SpectPart` 문자열은 없다. [QC](swan-quasi-coherent.md)의 호출은 `src/SwanCompUnstruc.ftn90:1170`의 `call QCSOURCE`이다. [Bragg](swan-bragg-scattering.md)의 배열 `fbd`·`membrg`는 같은 파일 1134–1156줄의 SOURCE 호출에 전달된다. [10-13 전수 검증 정정]

## 5. Arguments (line 1)

| 인자 | 역할 |
|---|---|
| `ac2` | 비정렬 AC2의 차원 순서는 (MDC,MSC,nverts)이다. 꼭짓점은 세 번째 첨자이다. `src/SwanCompUnstruc.ftn90:112` `real, dimension(MDC,MSC,nverts), intent(inout) :: ac2`; `src/swmod2.ftn:1027` `REAL   , SAVE, ALLOCATABLE :: AC2(:,:,:)` |
| `ac1` | action density at previous time level |
| `compda` | computational data array (depth, current, wind, etc) |
| `spcsig` | spectral relative frequency σ array |
| `spcdir` | spectral direction θ array (+ trig functions) |
| `xytst` | test point coordinates (debugging) |
| `cross` | obstacle crossing array |
| `it` | time step counter |

→ Standard SWAN time-step interface. `compda` 가 depth 등 공간의존 정보를 carry한다(`SwanCompUnstruc.ftn90:111-115`); obstacle 정보 `cross` 등은 별도 인자이다(`SwanCompUnstruc.ftn90:106-109`).

## 6. Cross-references

- [swan-documentation-stack](../manual-notes/swan-documentation-stack.md) Ch 8 unstructured mesh
- [swan-source-coverage-audit](swan-source-coverage-audit.md) §3.4 신규 발견
- [swan-foundation](swan-foundation.md) — SWAN main entry
- [swan-bragg-scattering](swan-bragg-scattering.md) (41.80 통합 → 본 module hook)
- [swan-quasi-coherent](swan-quasi-coherent.md) (41.90 통합)
- [swan-surfbeat-iem](swan-surfbeat-iem.md) — `src/SwanIEM.ftn90:38`의 생성 이력은 `!   41.85, January 2019: New module`이다. [10-13 전수 검증 정정]
- [swan-adcirc-coupling](swan-adcirc-coupling.md) — **41.20 Casey Dietrich 기여** = 본 module 변화 핵심
- [swan-gse-correction](swan-gse-correction.md) — `src/SwanGSECorr.ftn90:36`의 생성 이력은 `!   41.00, February 2009: New subroutine`이다. SwanCompUnstruc의 생성 이력은 2007년 7월이다. (`src/SwanCompUnstruc.ftn90:50`) [10-13 전수 검증 정정]
- [swan-diffraction-obstacles](swan-diffraction-obstacles.md) — 41.02 통합
- Authors: 14명 (Zijlema 다수 + Dietrich + Rijnsdorp + Reniers + Akrish + Smit)

## 7. 계산 조건 (10-13 recovery 대조)

- 첫 세 반복과 제한된 방향 구간은 nsweep을 쓴다. 전 방향 스펙트럼의 네 번째 이후 반복은 한 sweep을 쓴다. 이력 주석과 `src/SwanCompUnstruc.ftn90:823`의 `! loop over a fixed number of sweeps through grid` 주석은 이 감소 조건을 생략한다. [R8:N1-007](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론).
- 미지정 sweep 수는 3을 시작값으로 하여 물리 옵션별로 4 또는 3으로 바꾼다. `src/swanmain.ftn:3762–3770`의 원문은 `nsweep = 3`, `IF ( IREFR == 0 ) nsweep = 4`, `IF ( IQUAD == 0 .AND. IWCAP == 0 .AND. ISURF == 0 ) nsweep = 4`, `IF ( OFFSRC ) nsweep = 4`, `IF ( IGEN == 4 .OR. IQCM /= 0 ) nsweep = 3`이다. 부분 방향 격자의 1 sweep 입력은 3으로 바꾼다. [R1:TN-203](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론).
- OpenMP parallelization (41.10) 의 PRIVATE/SHARED 변수 별도.
- QCSOURCE는 `src/SwanQCM.ftn90:1361`의 `if ( iter > 1 ) then` 안에서 `src/SwanQCM.ftn90:1363`의 `call SWQCSURF ( memqcb, ac2, dep2, cfd, wfd, wsavd, kwave, cgo, spcdir, spcsig )`를 호출한다. [R8:V25](../../../_staging/recovery/flow/SWAN-callflow.md#24-깊이-2-호출-목록).
- Casey Dietrich 41.20 ADCIRC integration 의 정확한 변경 부분 (line range) 식별 별도.
- 기본 patch B 빌드는 거리 정렬 결과에서 의존성 수준을 만든 flist를 순회한다. -fixfront 빌드는 vlist를 순회한다. 이 분기는 `0dabfa4`(2026-07-13)에서 추가되었다. `43e9bbb:src/SwanCompUnstruc.ftn90:848`의 원문은 `!GRAPH                ivert = flist(kvert,swpdir)`이다. `43e9bbb:src/SwanCompUnstruc.ftn90:849`의 원문은 `!FXFRO                ivert = vlist(kvert,swpdir)`이다. [R8:T1-014](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론).
- 각도 조건은 ITEST 조건이 붙은 경고이다. `src/SwanCheckGrid.ftn90:151`의 원문은 `if ( .not. cosphi1 > -0.8 .and. ITEST >= 100 ) then`이다. 코드는 오류 수준 1로 보고한다. [R1:TN-190](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론).

## 8. 관련 unstructured compute 보조 routine (전소스 커버, 2026-06-04)

본 `SwanCompUnstruc` 가 호출하는 vertex-based 보조 (swanimp Material 의 unstructured routine 군):
- SwanTranspAc는 행렬과 우변을 초기화한다. 이후 SwanTranspX의 지리·시간항과 방향·주파수 전파항을 조립한다. SwanTranspX는 SwanTranspAc의 하위 루틴이다. `src/SwanTranspAc.ftn90:117–118`의 원문은 `amat = 0.` 및 `rhs  = 0.`이다. `src/SwanTranspAc.ftn90:129`의 원문은 `call SwanTranspX ( amat   , rhs  , ac2   , ac1   , cax   , cay   , &`이다. [R8:N1-008](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론).
- SwanInterpolateAc는 꼭짓점의 작용밀도를 지정점으로 공간 보간한다. 장애물이 가로막은 꼭짓점의 가중치는 0으로 둔다. 각 스펙트럼 bin은 `acintp(:,:) = acintp(:,:) + ww(k) * ac2(:,:,v(k))`로 보간한다. (`src/SwanInterpolateAc.ftn90:42–49,273–290`) [10-13 전수 검증 정정]
- **`SwanInterpolateOutput.ftn90`** — 출력 위치(FRAME/POINTS)로의 비정형 보간([swan-output-formats](swan-output-formats.md) 의 unstructured 출력). (`src/SwanInterpolateOutput.ftn90:44–51`; `src/swanout1.ftn:1676`) [10-13 전수 검증 보완]
→ 모두 `SwanCompUnstruc` time-step loop 또는 출력 단계의 보조. 이론은 [swan-tech-ch8-unstructured-grid-scheme](../manual-notes/swan-tech-ch8-unstructured-grid-scheme.md)/[swan-tech-ch8-unstructured-ops](../manual-notes/swan-tech-ch8-unstructured-ops.md).

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R1:TN-190 | 삼각 격자 검사 수준 | swantech PDF 144쪽 / 인쇄 136쪽: 내부 절점의 셀 수는 4–10; $\cos\phi<-0.8$ 또는 $\phi>143^\circ$를 “do not allow” | `src/SwanCheckGrid.ftn90:106,111,118,151`의 셀 수 검사와 `call msgerr (1, ... )`; 각도 조건은 `if ( .not. cosphi1 > -0.8 .and. ITEST >= 100 ) then`.<br>웹 [CGRID UNSTRUCTURED](../raw/manuals/website/online_doc/swanuse/node25.html):702–708. | C 문서 누락 | 격자 검사와 오류 메시지 출력 자체는 swanuse에도 있다. C는 swantech §8.1의 `do not allow`에 실제 보고 수준과 시험 출력 조건이 없는 점이다. 코드는 오류 수준 1로 보고한다. 각도 조건은 `if ( .not. cosphi1 > -0.8 .and. ITEST >= 100 ) then`이다. 이 조건은 등호를 포함하며 `ITEST >= 100`을 요구한다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-203 | 미지정 비정렬 sweep 수 | swantech PDF 150쪽 / 인쇄 142쪽: “three sweeps is a good compromise” | `src/swanmain.ftn:3762–3770`: `nsweep = 3`; `IF ( IREFR == 0 ) nsweep = 4`; `IF ( IQUAD == 0 .AND. IWCAP == 0 .AND. ISURF == 0 ) nsweep = 4`; `IF ( OFFSRC ) nsweep = 4`; `IF ( IGEN == 4 .OR. IQCM /= 0 ) nsweep = 3`.<br>swanuse PDF 135쪽 및 웹 [SET 명령 도식](../raw/manuals/website/online_doc/swanuse/node49.html):62–65. | C 문서 누락 | swanuse의 SET 명령 도식에 `[nsweep]`가 있다. C는 swantech §8.3의 3 sweep 권고에 물리 옵션별 미지정 값 선택이 없는 점이다. 미지정 값은 물리 옵션에 따라 3 또는 4이다. 부분 방향 격자의 1 sweep 입력은 3으로 바꾼다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-204 | GRAPH/FIXFRONT 목록 | swantech PDF 151쪽 / 인쇄 143쪽: 정렬된 절점 목록을 차례로 진행한다 | `src/SwanVertlist.ftn90:243–244`: `!GRAPH       ! construct levels from a directed dependency graph`; `!GRAPH       ! note: each level contains vertices that are independent by construction`; `src/SwanCompUnstruc.ftn90:839–849`의 `!GRAPH`·`!FXFRO` front 루프. | C 문서 누락 | 기본 GRAPH는 의존 그래프로 독립 절점 수준을 만든다. `-fixfront`는 고정 front 목록을 선택한다. 문서는 이 두 실행 목록을 설명하지 않는다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TC-007 | 비정렬 반복의 주기 상대 변화량 | — | `src/SwanConvStopc.ftn90:187,195,219,225`: `tmcurr(ivert) = max ( 1.e-20, PI2*(m0/m1) )`; `tmabs = abs ( tmcurr(ivert) - tmprev(ivert) )`; `tmrel  = PNUMS( 1) * tmcurr(ivert)`; `( tmcurv <= curvat .and. tmabs <= max(tmrel,PNUMS(3)) )`. | C 문서 누락 | 비정렬 경로는 주기 단위로 상대 오차를 비교한다. 정렬 경로 TN-076의 `TMABS/SACC2`와 다르다. 이 차이는 TN-076 결함 후보의 반대 경로 근거이다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TC-016 | 비정렬 흐름 sweep의 최소 bin 수 | — | `src/SwanSweepSel.ftn90:277–280,315,317`: `if ( idtot < 3 ) then`; `iddtop = iddtop + 1`; `if ( idtot == 1 ) iddlow = iddlow - 1`; `idtot = 3`; `isslow = 1`; `if ( ICUR > 0 ) isstop = max(min(4,MSC),isstop)`.<br>swanuse PDF 24쪽 / 인쇄 16쪽 및 웹 [격자 선택](../raw/manuals/website/online_doc/swanuse/node11.html):345–348. | C 문서 누락 | C는 swantech §8.3에 흐름이 있는 sweep의 최소 bin 확장 절차가 없는 점이다. 방향 구간은 최소 3 bin이며 주파수 구간은 저주파부터 최소 `min(4,MSC)`까지 포함한다. swanuse의 방향 사분면당 최소 3 bin 요건 및 전체 주파수 최소 4개 권고와 각 sweep 내부의 강제 확장을 구분한다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R8:T1-009 | 비정렬 반복별 sweep 수 감소 | swantech PDF 150쪽·인쇄 142쪽: “a fixed number of sweeps (not necessarily 4) is introduced”. PDF 151쪽·인쇄 143쪽: “In each iteration, a number of sweeps through the vertices is executed”. swanuse PDF 135쪽·인쇄 127쪽과 `website/online_doc/swanuse/node49.html:65`에는 `[nsweep]` 구문이 있다. `website/modifications/modifications.htm:1346–1347`은 “only a few sweeps per iteration or time step is needed”라고 적는다 | `src/SwanCompUnstruc.ftn90:124`의 `itswp = 4`; `:825–831`은 `if ( iter < itswp ) then`에서 `n = nsweep`, `elseif ( .not.FULCIR ) then`에서 `n = nsweep`, `else`에서 `n = 1`을 대입한다. | C — 감소 조건 누락 | 비정렬 격자는 첫 세 반복에서 nsweep을 쓴다. 네 번째 이후 반복은 전 방향 스펙트럼이면 한 sweep을 쓴다. 제한된 방향 구간이면 nsweep을 유지한다. C는 이 반복 번호·FULCIR에 따른 감소 조건의 설명 누락에 한정한다. nsweep의 존재나 일반적인 sweep 최적화가 문서 전체에 없다는 뜻은 아니다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |
| R8:T1-014 | 비정렬 기본 wavefront 정렬 | swantech PDF 150쪽·인쇄 142쪽: “All the vertices are ordered according to their distances to the origin of the grid in ascending order.”; `7ee8981 2024-09-02 initial release (v 41.51)`; `7ee8981:src/SwanCompUnstruc.ftn90:851` `             ivert = vlist(kvert,swpdir)`; `7ee8981:src/SwanCompUnstruc.ftn90:852` `             !$ ivert = tlist(kvert)` | `0dabfa4 2026-07-13 updated src (patch B)`; `43e9bbb:src/SwanVertlist.ftn90:243` `!GRAPH       ! construct levels from a directed dependency graph`; `43e9bbb:src/SwanVertlist.ftn90:371` `!GRAPH          flist(l,swpdir) = k`; `43e9bbb:src/SwanCompUnstruc.ftn90:848` `!GRAPH                ivert = flist(kvert,swpdir)`; `43e9bbb:src/SwanCompUnstruc.ftn90:849` `!FXFRO                ivert = vlist(kvert,swpdir)`; `43e9bbb:switch.pl:87` `      if ($ffro=~/TRUE/) {$newline=~s/^!FXFRO//;}`; `43e9bbb:switch.pl:88` `      else               {$newline=~s/^!GRAPH//;}` | A — patch B 판 차이 | 기본 patch B 빌드는 거리 정렬 결과에서 의존성 수준을 만든 flist를 순회한다. 거리값은 꼭짓점 좌표의 sweep 방향 투영이다. -fixfront 빌드는 vlist를 순회한다. 이 분기는 0dabfa4에서 추가되었다. 변경 커밋은 `0dabfa4`(2026-07-13)이다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |
| R8:N1-006 | 비정렬 AC2 차원 순서 | `source-analysis/swan-unstructured-time-step.md:112` `action density at current time level (vertex × MDC × MSC)` | `src/SwanCompUnstruc.ftn90:112` `real, dimension(MDC,MSC,nverts), intent(inout) :: ac2`는 선언의 배열 차원을 명시한다. `:1218` `ac2(id,is,ivert) = rhs(id,is) / rval2`. `src/swmod2.ftn:1027`의 원 저장소 선언은 `REAL   , SAVE, ALLOCATABLE :: AC2(:,:,:)`이다. | B | 비정렬 AC2의 차원 순서는 (MDC,MSC,nverts)이다. 꼭짓점은 세 번째 첨자이다. 모듈의 rank 3 선언과 계산 루틴의 명시적 차원 선언을 함께 근거로 쓴다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |
| R8:N1-007 | 비정렬 현행 sweep 수 | `source-analysis/swan-unstructured-time-step.md:84`은 `"fixed number of sweeps per iteration" (현행)`을 적는다. | `src/SwanCompUnstruc.ftn90:59`의 이력 주석은 `!   41.68,   August 2015: introduction of a fixed number of sweeps per iteration`이다. `src/SwanCompUnstruc.ftn90:124`의 `itswp = 4`; `:825–831`의 `if ( iter < itswp ) then` 및 `elseif ( .not.FULCIR ) then`은 `n = nsweep`, 나머지는 `n = 1`이다. `src/swanmain.ftn:3757–3770`은 nsweep의 생략값과 예외를 정한다. | B — 노트·주석의 조건 생략 | 첫 세 반복과 제한된 방향 구간은 nsweep을 쓴다. 전 방향 스펙트럼의 네 번째 이후 반복은 한 sweep을 쓴다. 노트가 옮긴 이력 주석과 `:823`의 고정 sweep 수 주석은 이 감소 조건을 생략한다. 코드 내부에서도 주석과 실행 조건을 구별해야 한다. nsweep의 생략값과 물리별 예외는 SWPREP를 따른다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) [10-13 전수 검증 정정]
| R8:N1-008 | SwanTranspAc의 역할 | `source-analysis/swan-unstructured-time-step.md:147`은 SwanTranspX를 `` `SwanTranspAc`(spectral σ,θ transport)의 공간 대응 ``으로 설명한다 | `src/SwanTranspAc.ftn90:117–118`은 `amat = 0.` 및 `rhs  = 0.`을 수행한다. `:129`는 `call SwanTranspX ( amat   , rhs  , ac2   , ac1   , cax   , cay   , &`이다. `:143`, `:160`, `:169`에서 STRSD·STRSSI·STRSSB를 조건에 따라 호출한다. 하위 `src/SwanTranspX.ftn90:141–150`은 NSTATC와 ITERMX에 따라 시간항도 조립한다. | B | SwanTranspAc는 행렬과 우변을 초기화한다. 이후 SwanTranspX의 지리·시간항과 방향·주파수 전파항을 조립한다. SwanTranspX는 SwanTranspAc의 하위 루틴이다. [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |
