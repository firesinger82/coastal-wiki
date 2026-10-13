---
title: "SWAN Garden-Sprinkler Effect correction — SwanGSECorr.ftn90 verified"
topic: swan
canonical_source: self
citation_status: verified
last_source_check: "2026-10-13 (recovery 대조 반영)"
verification_method: "SwanGSECorr.ftn90의 전체 280줄과 인용 호출·정렬 GSE·회절 비교 실행문을 대조했다. swantech §3.2.1–3.2.2의 PDF 81–83쪽과 §8.6의 PDF 154쪽을 대조했다. R1 최종 결론과 R8:V12를 대조했다." # [10-13 전수 검증 정정]
note_author: "Claude Opus 4.7 (1M context) raw source direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — full header verbatim + 변수 정의 발췌"
verification_date: 2026-06-01
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
  - models/SWAN/source-analysis/swan-propagation-implementation.md
  - models/SWAN/manual-notes/swan-action-balance.md
---

## Scope

SwanGSECorr.ftn90 — **Garden-Sprinkler Effect (GSE)** correction subroutine (280 lines). SWAN 41.00 (2009-02 Marcel Zijlema). Tech §3.8 refraction approximation (p.92-101) + Ch 8 unstructured §8.6 diffusion-like terms (p.146). User cmd 명시 없음 (internal numerical correction).

## Source basis

- `SwanGSECorr.ftn90` (280 lines, 단일 subroutine)
- Tech §3.8 Refraction approximation (p.92-101)
- Tech §8.6 Calculation of diffusion-like terms (p.146)
- Booij-Holthuijsen 1987 *Coastal Engineering* — GSE 원논문 (추정)

## 1. Header (line 1-40 verbatim)

```
subroutine SwanGSECorr(rhs, ac2, cgo, spcdir, idcmin, idcmax, isslow, isstop, trac0)
!   Programmer: Marcel Zijlema
!   Authors
!   41.00: Marcel Zijlema
!   Updates
!   41.00, February 2009: New subroutine
!   Purpose
!   Computes waveage-dependent diffusion terms in x-y space to counteract the garden-sprinkler effect
```

## 2. Arguments (line 56-71)

| 인자 | 방향 | 타입 | 역할 |
|---|---|---|---|
| `rhs(MDC, MSC)` | inout | real | 시스템 (σ,θ) 공간 RHS — GSE diffusion 더해짐 |
| `ac2(MDC, MSC, nverts)` | in | real | action density (current time, unstructured) |
| `cgo(MSC, ICMAX)` | in | real | group velocity |
| `spcdir(MDC, 6)` | in | real | spectral direction (radians, cos, sin, cos², cos·sin, sin²) |
| `idcmin/idcmax(MSC)` | in | integer | 주파수별 directional counter min/max |
| `isslow/isstop` | in | integer | sweep 안 전파되는 min/max 주파수 |
| `trac0(MDC, MSC, MTRNP)` | out | real | explicit propagation 부분 (출력) |

→ 본 subroutine은 sweep 안에서 호출되며 **각 vertex 마다 rhs(MDC, MSC) 에 GSE diffusion term 더함**.

## 3. Local 변수 핵심 (line 75-110)

```fortran
real :: dnn         ! waveage-dependent diffusion coefficient normal to propagation direction
real :: dss         ! waveage-dependent diffusion coefficient in propagation direction
real :: dgx0/dgx1   ! x-component diffusion gradient (present/next cell)
real :: dgy0/dgy1   ! y-component diffusion gradient
real :: dac2dx, dac2dy   ! action density 의 공간 derivative
real :: dgxdx, dgydy     ! diffusion gradient 의 공간 derivative
real :: dcg         ! group velocity difference across frequency bin
real :: cslat       ! cosine latitude (spherical)
integer :: icell, jcell    ! present, next cell index
integer, dimension(3) :: v ! present cell vertices
double precision :: carea  ! 2×centroid dual area
```

→ **dnn** (normal) + **dss** (streamwise) diffusion coefficient — propagation direction 에 따라 anisotropic. 각 cell 의 diffusion gradient (dgx/dgy) 의 spatial gradient (dgxdx/dgydy) 가 GSE term.

## 4. GSE 이론 (Booij-Holthuijsen 1987)

### 4.1 GSE 발생 mechanism

SWAN 의 spectral propagation 은 **discrete directional bins** (MDC, 보통 36 bins = 10° 분해능). 각 bin이 wave packet 처럼 directional 전파 → bin 사이에 공간 에너지 gap → **discrete directional rays** 가 정원용 sprinkler 의 노즐처럼 individual ray로 보임.

문제: 격자 해상도 < ray separation 시 numerical artifact (GSE) — 실제 wave field에는 없는 "줄무늬" 출현.

### 4.2 Wave-age dependent diffusion

해결: **wave-age 의존 spatial diffusion** 항을 추가 → 인접 directional bin 의 action density 가 smooth하게 spread.

$$D_{ss}=(\Delta c_g)^2\,\mathrm{WAVAGE}/12$$

$$D_{nn}=(c_g\Delta\theta)^2\,\mathrm{WAVAGE}/12$$

근거: swantech PDF 81–82쪽 / 인쇄 73–74쪽; `src/swancom5.ftn:2930` `DSS = DCG**2*WAVAGE/12.`; `src/swancom5.ftn:2931` `DNN = (CGO(IS,IC)*DDIR)**2 * WAVAGE/12.`.

`WAVAGE`는 GSE의 전파 시간이다. 근거: swantech PDF 81쪽 / 인쇄 73쪽의 $D_{ss}=\Delta c_g^2T/12$; `src/swancom5.ftn:2930` `DSS = DCG**2*WAVAGE/12.`.

### 4.3 기법 선택 권고

적용 규모별 예시와 기법 선택 권고이다. GSE 보정은 기본으로 켜지지 않는다. 근거: swantech PDF 83쪽 / 인쇄 75쪽; `src/swanmain.ftn:1184`: `WAVAGE = 0.`; `src/SwanTranspAc.ftn90:135`의 `WAVAGE > 0.` 호출 조건. [10-13 전수 검증 보완]

## 5. Algorithm overview

1. **Loop over vertices** (`ivert`) — unstructured grid
2. Cell 별 (`icell/jcell`) action density gradient (`dac2dx/dac2dy`) 계산
3. wave-age 평가 → `dnn/dss` 계산
4. Diffusion gradient (`dgx/dgy`) construct
5. Spatial gradient (`dgxdx/dgydy`) → rhs 더함

`carea` (double precision 2×centroid dual area) 사용 → centroid dual control volume 방식 (Tech §8.3.1 discretization procedure).

비정렬 GSE는 현재 갱신 중인 `ac2`를 사용한다. 정렬 S&L의 이전 시간 `AC1` 보정과 다르다. 경계 절점에는 보정을 적용하지 않는다. 근거: `src/SwanGSECorr.ftn90:127,181,271`: `if ( vert(ivert)%atti(VMARKER) == 1 ) return`; `dac2dx = 0.5*( ac2(id,is,v(1))*(ycugrd(v(2))-ycugrd(v(3))) + &`; `rhs  (id,is  ) = rhs  (id,is  ) + dgxdx + dgydy`. `src/SwanGSECorr.ftn90:62`는 `ac2`를 현재 시간 수준으로 정의한다. 정렬 S&L의 근거는 `src/swancom5.ftn:3000–3010`의 `AC1` 차분이다. [10-13 전수 검증 보완]

GSE는 현재 절점의 확산 텐서를 둘러싼 모든 셀에 공통 적용한다. 회절처럼 셀 중심에서 계수를 다시 평균하지 않는다. 문서는 이 경로 차이를 적지 않는다. 근거: `src/SwanGSECorr.ftn90:140,143–144,200,238`: `dcg = 0.5 * abs(cgo(is+1,1)-cgo(is-1,1))`; `dss = dcg**2*WAVAGE/12.`; `dnn = (cgo(is,1)*DDIR)**2 * WAVAGE/12.`; `dgx0 = dxx*dac2dx + dxy*dac2dy`; `dgx1 = dxx*dac2dx + dxy*dac2dy`. 회절 비교의 근거는 `src/SwanDiffPar.ftn90:252–253,295–296`의 셀별 군속도·파수 평균과 276·319행의 확산 기울기다. [10-13 전수 검증 보완]

## 6. Cross-references

- [swan-documentation-stack](../manual-notes/swan-documentation-stack.md) — GSE의 근거는 swantech §3.2.1–3.2.2와 §8.6이다. 해당 본문은 PDF 81–83·154쪽이다. [10-13 전수 검증 정정]
- [swan-propagation-implementation](swan-propagation-implementation.md) — 지리 공간·스펙트럼 공간의 전파 구현. [10-13 전수 검증 정정]
- [swan-action-balance](../manual-notes/swan-action-balance.md) — action density 정의
- [swan-source-coverage-audit](swan-source-coverage-audit.md) §3.1 신규 발견
- [swan-bragg-scattering](swan-bragg-scattering.md) / [swan-quasi-coherent](swan-quasi-coherent.md) / [swan-surfbeat-iem](swan-surfbeat-iem.md) — Bragg·준결맞음·surfbeat 구현 노트. [10-13 전수 검증 정정]
- Author: Marcel Zijlema (41.00, 2009-02) — TU Delft SWAN team lead
- 원논문 추정: **Booij·Holthuijsen 1987** "Propagation of ocean waves in discrete spectral wave models" *J. Comput. Phys.* 68, 307-326

## 7. 한계

- 비정렬 GSE는 현재 갱신 중인 `ac2`를 사용한다. 정렬 S&L의 이전 시간 `AC1` 보정과 다르다. 경계 절점에는 보정을 적용하지 않는다. 근거: `src/SwanGSECorr.ftn90:127` `if ( vert(ivert)%atti(VMARKER) == 1 ) return`; `src/SwanGSECorr.ftn90:181` `dac2dx = 0.5*( ac2(id,is,v(1))*(ycugrd(v(2))-ycugrd(v(3))) + &`. `src/SwanGSECorr.ftn90:62`는 `ac2`를 현재 시간 수준으로 정의한다. 정렬 S&L의 근거는 `src/swancom5.ftn:3000–3010`의 `AC1` 차분이다. [10-13 전수 검증 보완]
- `src/SwanTranspAc.ftn90:135` `if ( WAVAGE > 0. ) call SwanGSECorr ( rhs, ac2, cgo, spcdir, idcmin, idcmax, isslow, isstop, trac0 )`. 근거: [SWAN 호출 흐름](../../../_staging/recovery/flow/SWAN-callflow.md), V12.
- `WAVAGE`는 GSE의 전파 시간이다. 근거: swantech PDF 81쪽 / 인쇄 73쪽; `src/swancom5.ftn:2930` `DSS = DCG**2*WAVAGE/12.`.
- Booij-Holthuijsen 1987 원논문 DOI 검증 필요

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R1:TC-008 | 비정렬 GSE의 시간 수준과 경계점 | — (문서 누락) | `src/SwanGSECorr.ftn90:127,181,271`: `if ( vert(ivert)%atti(VMARKER) == 1 ) return`; `dac2dx = 0.5*( ac2(id,is,v(1))*(ycugrd(v(2))-ycugrd(v(3))) + &`; `rhs  (id,is  ) = rhs  (id,is  ) + dgxdx + dgydy`. `src/SwanGSECorr.ftn90:62`는 `ac2`를 현재 시간 수준으로 정의한다. 정렬 S&L의 근거는 `src/swancom5.ftn:3000–3010`의 `AC1` 차분이다. | C 문서 누락 | 비정렬 GSE는 현재 갱신 중인 `ac2`를 사용한다. 정렬 S&L의 이전 시간 `AC1` 보정과 다르다. 경계 절점에는 보정을 적용하지 않는다. [10-13 전수 검증 보완] |
| R1:TN-055 | GSE 교차차분 | swantech PDF 82쪽 / 인쇄 74쪽, 번호 없음: $D_{xy}(N_{i,j}-N_{i-1,j}-N_{i,j-1}+N_{i-1,j-1})^{n-1}/(\Delta x\Delta y)$. | `src/swancom5.ftn:3003–3008`: `!           old method`; 기존 식은 주석이다. `!           new method`; `D12AC = 0.25*(AC1(ID,IS,IND12) - AC1(ID,IS,IND11)`; `&                   -AC1(ID,IS,IND13) + AC1(ID,IS,IND10))`. | B 문서 오기 | 해석: 활성 식은 네 대각 이웃의 중심 교차차분이다. 문서는 주석으로 남은 구식을 적는다. 구식도 해당 절점에서 2차 중심차분이 아니다. 의도 변경 주석이 있으므로 코드 결함으로 판정하지 않는다. |
| R1:TN-057 | GSE 안정성·규모별 권고 | swantech PDF 83쪽 / 인쇄 75쪽, §3.2.2 및 번호 없는 권고: $\mu\approx1/2,\ Q\le1/4,\ \Delta\theta\sim10^\circ,\ \bar L/\Delta x\sim200$; 지역 $\mu=\mathcal O(1)$; 국소 $\mathcal O(10-100)$. | `src/swanmain.ftn:1184`: `WAVAGE = 0.`. | H 코드 대조 대상 아님 | 적용 규모별 예시와 기법 선택 권고이다. GSE 보정은 기본으로 켜지지 않는다. |
| R1:TN-218 | 문서 식 (8.39) | swantech PDF 154쪽 / 인쇄 146쪽, (8.39)의 GSE 적용도 “$\kappa$ as given in the centroid”. | `src/SwanGSECorr.ftn90:140,143–144,200,238`: `dcg = 0.5 * abs(cgo(is+1,1)-cgo(is-1,1))`; `dss = dcg**2*WAVAGE/12.`; `dnn = (cgo(is,1)*DDIR)**2 * WAVAGE/12.`; `dgx0 = dxx*dac2dx + dxy*dac2dy`; `dgx1 = dxx*dac2dx + dxy*dac2dy`. 회절 비교의 근거는 `src/SwanDiffPar.ftn90:252–253,295–296`의 셀별 군속도·파수 평균과 276·319행의 확산 기울기다. | C 문서 누락 | GSE는 현재 절점의 확산 텐서를 둘러싼 모든 셀에 공통 적용한다. 회절처럼 셀 중심에서 계수를 다시 평균하지 않는다. 문서는 이 경로 차이를 적지 않는다. [10-13 전수 검증 보완] |
