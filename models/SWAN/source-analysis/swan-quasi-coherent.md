---
title: "SWAN Quasi-Coherent Modelling (QCM) — SwanQCM.ftn90 verified"
topic: swan
canonical_source: self
citation_status: verified
last_source_check: "2026-10-13 (recovery 대조 반영)"
verification_method: "raw `models/SWAN/raw/source_code/swan/src/SwanQCM.ftn90`의 인용 구간을 대조했다. 파일은 3464줄이며 subroutine 선언은 12개이다. swantech PDF 68–70·74–75·111–114쪽과 swanuse PDF 37·90–91·94쪽을 대조했다. Akrish 외 (2020) A2-4–A2-6의 작용 변수와 정규화를 대조했다. 2026-10-13 recovery 대조 보고서 R1–R8 반영" # [10-13 전수 검증 정정]
note_author: "Claude Opus 4.7 (1M context) raw source direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — header verbatim + subroutine map"
verification_date: 2026-06-01
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
  - models/SWAN/manual-notes/swan-action-balance.md
  - models/SWAN/source-analysis/swan-bragg-scattering.md
---

## Scope

소스 주석의 41.90은 내부 변경 표기다. 이를 공개판 최소 버전으로 옮기지 않는다. swanuse SCAT 절은 도입 버전을 41.41이라고 적는다. 이 보고서의 코드 대조 버전은 41.51이다. 근거: swanuse PDF 90쪽 / 인쇄 82쪽 SCAT 절; `src/swanmain.ftn:965` `VERNUM = 41.51`.

## Source basis

- `SwanQCM.ftn90` (3464 lines) — module + 12 subroutines
- Tech §2.7 Quasi-coherent modelling (p.58-64): Wigner distribution / evolution eq / QC approx
- Tech §3.9 QC implementation (p.102)
- User cmd `SCAT` (p.81)

## 1. Module header (line 34-46)

```
module SwanQCM
!   Authors
!   41.90: Gal Akrish, Pieter Smit and Marcel Zijlema
!   Updates
!   41.90, June 2021: New module
!   Purpose
!   Contains data with respect to quasi-coherent modelling
```

## 2. Module data (line 54-78)

```fortran
integer :: mkxc, mkyc        ! wavenumber space size (x, y)
integer :: mxd, myd          ! dissipation grid size (x, y)
integer :: ncoz              ! coherent region / scattering wavenumber space size

integer :: lensav, lensvd, lenwfd, lenwft  ! FFT work array sizes

real, allocatable :: disbk0(:), disbk1(:)  ! bulk dissipation surf-breaking (previous + current iter)
real, allocatable :: kx(:), ky(:)          ! wavenumber components
real, allocatable :: xpsc(:)               ! coherent scattering region for FFT
real, allocatable :: xpd(:), ypd(:)        ! spatial lag grid (surf breaking)
real, allocatable :: kxd(:), kyd(:)        ! wavenumber 공간 (lag grid)
```

핵심: **dual grid system** — 일반 spectral grid (mkxc·mkyc) + **spatial lag grid** (mxd·myd, surf breaking dissipation 전용) + coherent scattering wavenumber (ncoz). FFT 4개 (lensav/lensvd/lenwfd/lenwft).

## 3. Subroutine inventory (12 sub-routines)

| Line | Subroutine | Purpose (Tech §2.7/§3.9 매핑) |
|---|---|---|
| **83** | `SWQCINIT(BGRIDP, COMPDA)` | QCM framework 초기화 (FFT 준비 + wavenumber 격자) |
| **697** | `SWQCDFT(sigft, cgft, dep2, kwave, cgo, cft, rft, sft, wft, wsave)` | `SWQCDFT`는 국소점 주변의 고유주파수·군속도 변동을 공간에서 매질 파수 q공간으로 변환한다. `SWQCUFT`는 흐름 변동을 같은 방식으로 변환한다. 작용밀도 자체의 FFT가 아니다. `src/SwanQCM.ftn90:863` `rft(i,j) = sig - sigp`; `src/SwanQCM.ftn90:881` `cft = cmplx(rft)` |
| **943** | `SWQCUFT(uxft, uyft, dep2, ux2, uy2, cft, rft, sft, wft, wsave)` | `SWQCUFT`는 흐름 변동을 같은 방식으로 변환한다. `src/SwanQCM.ftn90:1097` `rft(i,j) = uu - uxp`; `src/SwanQCM.ftn90:1098` `sft(i,j) = vv - uyp` |
| **1165** | `QCSOURCE(imatra, imatda, iter, ac2, dep2, ux2, uy2, ...)` | **QC source term assembly** — main contribution to S |
| **1417** | `SWQCWIG(W, dwdx, dwdy, ac2, dep2, rdx, rdy, spcdir, spcsig)` | **Wigner distribution W 계산** + 공간 gradient |
| **1656** | `SwanGradWig(W, dwdx, dwdy, ac2, dep2, spcdir, spcsig)` | Wigner gradient (unstructured grid 변형) |
| **2050** | `SWQCSCAT(memqcm, W, dwdx, dwdy, sigft, cgft, uxft, uyft, dep2, kwave, cgo, spcdir, spcsig)` | **QC scattering source** (W 기반 산란) |
| **2367** | `SWQCSURF(memqcb, ac2, dep2, cfd, wfd, wsavd, kwave, cgo, spcdir, spcsig)` | **QC surf breaking** (공간 lag grid + 일관된 dissipation) |
| **2698** | `bdiss` (nested, in SWQCSURF) | Bulk dissipation 계산 |
| **3106** | `varchk` (nested) | Variance check (numerical safety) |
| **3187** | `FILQCM(imatra, idcmin, idcmax, isstop, memqcm, memqcb, plqcs, plwbrk, redc0, dissc0)` | `FILQCM`은 QC 산란항을 수지식 우변에 더한다. QC 쇄파항과 진단 출력도 처리한다. 출력 전용 함수로 분류하지 않는다. `src/SwanQCM.ftn90:3270–3282,3304–3316` |
| **3342** | `tukeywin(a, n)` | Tukey window function (FFT 주변 effect 억제) |

## 4. 이론 (Tech §2.7)

### 4.1 Wigner distribution (Tech §2.7.1, p.58)

스펙트럼 action density $N(\sigma, \theta; x, t)$ 가 **Wigner distribution** $W(k; x, t)$ 로 변환:

$$W(\vec x,\vec k)=\frac1{4\pi^2}\int\Gamma(\vec x,\vec\xi)e^{-i\vec k\cdot\vec\xi}d\vec\xi \quad \text{(2.147)}$$

swantech 2.7의 수면 높이 변수와 Akrish 외의 작용 변수 $\psi$를 구분한다. swantech 원문을 전사할 때는 $W=(4\pi^2)^{-1}\int\Gamma e^{-i\vec k\cdot\vec\xi}d\vec\xi$를 유지한다. 코드는 분산 기준 작용밀도를 $W_k=(c_g/k)W_{\sigma\theta}$로 변환한다. 역 야코비안 $k/c_g$는 산란항에 적용한다(`src/SwanQCM.ftn90:2360` `memqcm(id,is,KCGRD(1)) = ctb * kwave(is,1) / cgo(is,1)`). 이 차이를 코드 결함으로 분류하지 않는다. 근거: swantech PDF 68쪽 / 인쇄 60쪽 (2.147); Akrish 외 (2020), §2.1–2.2, A2-4–A2-6의 원문은 [외부 원문 대조](../../../_staging/recovery/compare/SWAN-external-sources.md)에 있다. `src/SwanQCM.ftn90:1593` `W(iky,ikx,ic) = ctb * cg / k`.

swantech 2.7의 수면 높이 변수와 Akrish 외의 작용 변수 $\psi$를 구분한다. 근거: swantech PDF 68쪽 / 인쇄 60쪽; [외부 원문 대조](../../../_staging/recovery/compare/SWAN-external-sources.md).

**Wigner 의 장점**: 일반 spectral action density 가 모든 점에서 **음이 아닌(non-negative)** 값인 반면, W 는 **interference pattern (음의 lobe 포함)** 도 표현 가능 → diffraction·focusing 등 phase 효과 자연 표현.

### 4.2 Evolution equation (Tech §2.7.3, swantech PDF 74쪽 / 인쇄 66쪽)

$$\partial_tW+\nabla_k\omega\cdot\nabla_xW=S_{qc} \quad \text{(2.154)}$$

이론 진화식은 $\partial_tW+\nabla_k\omega\cdot\nabla_xW=S_{qc}$다. 기본 QC는 굴절을 산란항에 포함한다. 주파수·방향 격자에서는 (3.44)의 보존형 전파와 $J^{-1}S_{qc}$를 사용한다. 근거: swantech PDF 74쪽 / 인쇄 66쪽 (2.154); PDF 111쪽 / 인쇄 103쪽 (3.44); `src/swanmain.ftn:3825` `IF (IQCM.EQ.1) IREFR = 0`.

### 4.3 QC approximation (Tech §2.7.3, p.64)

QC는 $\mu$에 대해 1차 근사를 취한다. 파수 이동 $W(\vec k-\vec q/2)$는 유지한다. 근거: swantech PDF 74쪽 / 인쇄 66쪽 (2.153).

swantech PDF 74쪽 / 인쇄 66쪽, (2.153): $\partial_tW(\vec x,\vec k)=-i\int\hat\omega(\vec q,\vec k)e^{i\vec q\cdot\vec x}(1-\tfrac i2\overleftarrow\nabla_{\vec k}\cdot\overrightarrow\nabla_{\vec x})W(\vec x,\vec k-\vec q/2)d\vec q+\mathrm{c.c.}$

`ncoz`는 매질 변동 FFT 격자의 한 축 점 수다. 근거: `src/SwanQCM.ftn90:577` `ncoz = 2*floor(ceiling(qmax)/2.)`.

## 5. Implementation (Tech §3.9, p.102)

1. **SWQCINIT** — FFT 준비, wavenumber 격자 초기화
2. **SWQCWIG** — Wigner W 계산 (current 시점)
3. `SWQCDFT`는 국소점 주변의 고유주파수·군속도 변동을 공간에서 매질 파수 q공간으로 변환한다. `SWQCUFT`는 흐름 변동을 같은 방식으로 변환한다. 작용밀도 자체의 FFT가 아니다. 근거: `src/SwanQCM.ftn90:863` `rft(i,j) = sig - sigp`; `src/SwanQCM.ftn90:1097` `rft(i,j) = uu - uxp`.
4. **SWQCSCAT** — scattering source term (W 기반)
5. **SWQCSURF** — surf breaking 의 quasi-coherent 처리 (`disbk0/disbk1` iteration)
6. `src/SwanQCM.ftn90:1413` `call FILQCM ( imatra, idcmin, idcmax, isstop, memqcm, memqcb, plqcs, plwbrk, redc0, dissc0 )`. QCSOURCE의 반환 배열과 이후 행렬 누적을 구분한다.
7. `FILQCM`은 QC 산란항을 수지식 우변에 더한다. QC 쇄파항과 진단 출력도 처리한다. 출력 전용 함수로 분류하지 않는다. 근거: `src/SwanQCM.ftn90:3270–3282,3304–3316`.

iteration 반복: `disbk0` (previous) → `disbk1` (current) → convergence.

## 6. User cmd `SCAT` (swanuse.pdf p.81)

흐름이 없으면 IQCM>1은 1로 바뀐다. 근거: `src/swanmain.ftn:6448` `IF ( ICUR.EQ.0 .AND. IQCM.GT.1 ) THEN`; `src/swanmain.ftn:6451` `IQCM = 1`.

RFAC는 파수 격자 간격을 나누는 값이다. 작은 QC 절단 범위에는 이산 하한이 적용된다. 근거: `src/SwanQCM.ftn90:521` `dkx  = sdev / rfac`; `src/SwanQCM.ftn90:522` `dky  = sdev / rfac`; `src/SwanQCM.ftn90:573` `if ( qmax < 2. ) then`; `src/SwanQCM.ftn90:575` `qmax = 2.`.

## 7. Cross-references

- [swan-documentation-stack](../manual-notes/swan-documentation-stack.md) §2.7 Wigner + §3.9 implementation
- [swan-action-balance](../manual-notes/swan-action-balance.md) — 표준 spectral N(σ,θ;x,t).
- [swan-diffraction-obstacles](swan-diffraction-obstacles.md) — 별도 mild-slope diffraction (Holthuijsen 2003) vs QC 회절
- [swan-bragg-scattering](swan-bragg-scattering.md) — k-k' 산란 (Bragg) vs spatial coherence (QC) 의 서로 다른 산란 mechanism
- 소스 주석의 41.90은 내부 변경 표기다. 이를 공개판 최소 버전으로 옮기지 않는다. 근거: swanuse PDF 90쪽 / 인쇄 82쪽 SCAT 절; `src/swanmain.ftn:965` `VERNUM = 41.51`.
- Akrish 외 (2020), §2.1–2.2, A2-4–A2-6의 작용 변수와 정규화 원문은 [외부 원문 대조](../../../_staging/recovery/compare/SWAN-external-sources.md)에 있다.

## 8. 한계

- 코드는 분산 기준 작용밀도를 $W_k=(c_g/k)W_{\sigma\theta}$로 변환한다. 역 야코비안 $k/c_g$는 산란항에 적용한다. 근거: `src/SwanQCM.ftn90:1593` `W(iky,ikx,ic) = ctb * cg / k`; `src/SwanQCM.ftn90:2360` `memqcm(id,is,KCGRD(1)) = ctb * kwave(is,1) / cgo(is,1)`.
- $x\pm\xi/2$에서 이전 반복의 총소산을 보간한 평균을 상관함수에 곱한다. 양의 적분 소산이 나오면 최대 두 번 양의 항을 0.99배, 음의 항을 1.01배 한다. 이후 `varD<0`이고 `varW>0`이면 총소산에 맞춰 재정규화한다. 아니면 소산을 0으로 만든다. 3.9는 이 계산 자체를 미포함으로 기술한다. 정확한 제어 조건은 `src/SwanQCM.ftn90:3121`의 `if ( varD > 0. .and. j < maxit ) then`과 3173행의 `if( varD < 0. .and. varW > 0. ) then`이다. swanuse PDF 90·SCAT 절도 QC 쇄파를 장래 포함 대상으로 적는다. C는 swantech 3.9와 이 사용자 문서에 없는 GEN4 전용 QC 쇄파 구현을 뜻한다. 근거: [R3 대조](../../../_staging/recovery/compare/swan-theory-obstacles-setup-qc-bc-vs-code.md), CP-017.
- swantech 2.7의 수면 높이 변수와 Akrish 외의 작용 변수 $\psi$를 구분한다. 근거: swantech PDF 68쪽 / 인쇄 60쪽; [외부 원문 대조](../../../_staging/recovery/compare/SWAN-external-sources.md).
- 줄 수와 함수 수를 실행 비용의 정량 근거로 사용하지 않는다. 근거: [R3 대조](../../../_staging/recovery/compare/swan-theory-obstacles-setup-qc-bc-vs-code.md), NT-038.

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R1:TC-009 | QC 산란항 계산의 생략 기준 | — (문서 누락) | `src/SwanQCM.ftn90:871,873`: `if ( k*hmin > 2.3 ) cycle`; `if ( (hmax-hmin)/(xpsc(ncoz)-xpsc(1)) < 0.001 ) cycle`. | C 문서 누락 | C는 swantech §3.9에 두 생략 문턱이 없는 점이다. `if ( k*hmin > 2.3 ) cycle`은 깊은 coherent zone을 건너뛴다. `if ( (hmax-hmin)/(xpsc(ncoz)-xpsc(1)) < 0.001 ) cycle`은 zone 길이로 나눈 수심 차이를 검사한다. 이를 수심 자체로 정규화한 상대 변화라고 쓰지 않는다. |
| R3:CP-010 | 매질 변동 계산 생략 | — (문서 누락) | 매질 변동 계산 생략. `src/SwanQCM.ftn90:871` `if ( k*hmin > 2.3 ) cycle`; `src/SwanQCM.ftn90:873` `if ( (hmax-hmin)/(xpsc(ncoz)-xpsc(1)) < 0.001 ) cycle`; `src/SwanQCM.ftn90:847` `if ( d /= EXCFLD(1) ) then`. | C 문서 누락 | 가장 얕은 수심에서도 심해인 주파수와 작은 평균 바닥 변화율은 수심 산란 FFT를 생략한다. 제외 수심에서는 초기 영 변동을 남긴다. (3.45) 앞의 차분식에는 이 두 임계값이 없다. C의 범위는 swantech 3.9의 매질 차분식과 swanuse SCAT 절이다. 두 절은 깊은 수심의 `if ( k*hmin > 2.3 ) cycle` 및 작은 변화율의 `if ( (hmax-hmin)/(xpsc(ncoz)-xpsc(1)) < 0.001 ) cycle`을 설명하지 않는다. |
| R3:CP-011 | 흐름 회전과 상한 | — (문서 누락) | 흐름 회전과 상한. `src/SwanQCM.ftn90:1066` `cgmx = PNUMS(18) * sqrt( GRAV*dp )`; `src/SwanQCM.ftn90:1086` `uu = u*COSVC + v*SINVC`; `src/SwanQCM.ftn90:1087` `vv = -u*SINVC + v*COSVC`; `src/SwanQCM.ftn90:1092` `fac = cgmx / vtot`; `src/SwanQCM.ftn90:1093` `uu = fac * uu`. | C 문서 누락 | 입력 흐름을 계산 좌표로 회전한다. `if ( vtot > cgmx ) then`에서 두 성분을 같은 비율로 줄인다(`src/SwanQCM.ftn90:1091–1094`). swanuse PDF 37·SET 절(node23:451–478)은 FROUDMAX에 따른 유속 상한을 이미 설명한다. C는 swantech 3.9와 swanuse SCAT 절에 없는 QC FFT 표본 처리에 한정한다. 1062·1066행은 현재 계산점 수심 `dp`로 `cgmx = PNUMS(18) * sqrt( GRAV*dp )`를 정하고 주변 표본에도 그 상한을 쓴다. 실제 영 유속 차분 생략은 QC-086의 별도 E 판정이다. |
| R3:CP-012 | 파수→방향 변환의 주기 연결 누락 | — (문서 누락) | 파수→방향 변환의 주기 연결 누락. `src/SwanQCM.ftn90:1541` `dir = atan2 ( ky(iky), kx(ikx) )`; `src/SwanQCM.ftn90:1568` `jkb = ( dir - spcdir(1,1) ) / DDIR`; 1570의 음수 인덱스 검사는 `outsid = .true.`로 이어진다. `src/swanpre1.ftn:1778` `SPDIR1 = ALPC + 0.5 * DDIR`; `src/swanpre1.ftn:4706` `SPCDIR(ID,1) = SPDIR1 + FLOAT(ID-1)*DDIR`. | E 코드 결함 후보 · 강함 | 직교 격자 `ALPC=0`, 전 방향에서 `ATAN2`의 음의 각도는 양의 스펙트럼 원점보다 작다. 코드가 $2\pi$를 더하지 않아 아래 반평면의 유효 성분을 외부로 판정한다. 반대 근거: 방향 부채꼴에서는 외부 0 처리가 필요하다. 그러나 이 루틴에 `FULCIR` 예외가 없다. 4장의 원형 공간 조건 및 `STRSD`의 modulo 경로와 모순된다. 비구조 변환 1859행에도 같은 처리다. `src/swancom1.ftn:3589–3590`의 QC 호출 뒤 `src/SwanQCM.ftn90:1396`에서 이 변환을 수행한다. `src/swancom5.ftn:3956–3957`은 `IF (FULCIR .OR. ID.GT.1) THEN`에서 `IIDM = MOD (IDDUM-2+MDC, MDC) + 1`을 쓰지만 QC 변환에는 이 주기 연결이 없다. git 최초 반입 `b2ae30e`의 1563행과 `7ee8981`·`43e9bbb`의 1568–1574행은 같은 분기다. E·강함을 유지한다. 노트에는 ALPC=0인 전 방향 격자에서도 음의 ATAN2 각도를 영역 밖으로 판정해 0으로 만든다고 적는다. |
| R3:CP-013 | `PROPSL=3`의 QC 기울기 | — (문서 누락) | `PROPSL=3`의 QC 기울기. `src/SwanQCM.ftn90:1608` `if (PROPSL == 2 ) then`; `src/SwanQCM.ftn90:1630` `elseif (PROPSL == 1 ) then`; `src/SwanQCM.ftn90:1652` `endif`; `src/swanmain.ftn:1180` `PROPSN = 3`; `src/swanmain.ftn:6355` `PROPSC = PROPSN`. | E 코드 결함 후보 · 강함 | `SWQCWIG`는 `PROPSL=3`에서 `dwdx,dwdy`를 대입하지 않는다. 1475–1476행은 두 배열을 `intent(out)`으로 선언한다. 호출부 1396행 뒤 1404행이 이를 산란항으로 넘긴다. 반대 근거: 경계·장애물 근처는 `PROPSL=1`로 낮추는 경로가 있다. 격자 내부의 S&L 스텐실은 3을 유지한다. 3.9의 비정상 S&L 권고와 114쪽의 기울기 계산 설명 및 같은 함수의 1·2 분기와 모순된다. 도달 경로는 `src/swanmain.ftn:6354–6355`의 `IF (NSTATC.EQ.1) THEN` → `PROPSC = PROPSN`, `src/swancom1.ftn:3052`의 `PROPSL = PROPSC`, 3589–3590행의 QC 호출이다. 젖은 내부 S&L 스텐실은 3136·3139행의 BSBT 전환을 거치지 않는다. `src/SwanQCM.ftn90:2218`은 이어서 `ctb = cax * dwdx(iky,ikx) + cay * dwdy(iky,ikx)`로 배열을 읽는다. 전처리 제외 조건은 없다. git 최초 반입 `b2ae30e`의 1625행과 `7ee8981`·`43e9bbb`의 1630행까지 1·2 분기만 유지된다. E·강함을 유지한다. 노트에는 비정상 S&L 내부점에서 정의되지 않은 기울기를 산란항이 읽는다고 적는다. |
| R3:CP-014 | 자동 파수 범위의 수심 선택 | — (문서 누락) | 자동 파수 범위의 수심 선택. `src/SwanQCM.ftn90:388` `! next, compute minimum and maximum absolute wave numbers ...`; `src/SwanQCM.ftn90:390` `call KSCIP1 ( 1, spcsig(  1), hmin, k, cg, arr, arr )`; `src/SwanQCM.ftn90:391` `kmin = k(1)`; `src/SwanQCM.ftn90:393` `call KSCIP1 ( 1, spcsig(MSC), hmax, k, cg, arr, arr )`; `src/SwanQCM.ftn90:394` `kmax = k(1)`. | E 코드 결함 후보 · 강함 | 해석: 고정 $\sigma$에서 $\sigma^2=gk\tanh(kh)$의 해 $k$는 수심이 깊어질수록 작아진다. 전체 최소는 최저 주파수·최대 수심에서 구해야 한다. 전체 최대는 최고 주파수·최소 수심에서 구해야 한다. 코드 주석의 극값 목적과 (2.149)의 분산 관계에 반한다. 반대 근거: 일정 수심이면 문제가 사라진다. 사용자 지정 범위는 이 자동 경로를 우회한다. 자동 구성 조건은 `src/SwanQCM.ftn90:361`의 `if ( .not. kxlen /= 0. .and. .not. kylen /= 0. ) then`이다. 376–377행의 젖은 격자 수심 극값으로 390·393행을 실행한다. 전처리 제외 조건은 없다. git 최초 반입 `b2ae30e`, `7ee8981:src/SwanQCM.ftn90:390–394`, `43e9bbb`에 같은 수심 선택이 남아 있다. E·강함을 유지한다. 노트에는 수심이 변하는 영역의 전체 파수 범위를 구하려면 최소 파수에 최대 수심, 최대 파수에 최소 수심을 써야 한다고 적는다. |
| R3:CP-015 | 사용자 비등방 파수 격자 | — (문서 누락) | 사용자 비등방 파수 격자. `src/SwanQCM.ftn90:526` `dkx = kxlen / float(mkxc)`; `src/SwanQCM.ftn90:527` `dky = kylen / float(mkyc)`; `src/SwanQCM.ftn90:561` `clen = PI2 / max(dkx,dky)`; `src/SwanQCM.ftn90:578` `dxps = clen / real(ncoz) / 2.`; 2234의 `W(iky-jk,ikx-ik)`. | E 코드 결함 후보 · 강함 | x′·y′ FFT는 같은 간격이므로 두 q간격은 모두 $2\max(dkx,dky)$다. 그러나 이동 인덱스는 각각 `dkx,dky` 한 칸을 쓴다. 둘이 다르면 한 축에서 $q/2$와 W 이동량이 달라진다. 반대 근거: 기본 WIDTH 격자는 등방이다. 수동 격자 파서 3595–3600행은 이 동등성을 강제하지 않는다. (3.45)의 이동량 및 등방 경로의 정확한 대응과 모순된다. `src/SwanQCM.ftn90:1078–1079`는 `x = xp + xpsc(i)`, `y = yp + xpsc(j)`로 같은 공간 간격을 두 축에 쓴다. `src/swanpre1.ftn:3597–3600`은 `KXLEN`, `KYLEN`, `MKXC`, `MKYC`를 따로 받는다. 이 경로를 전처리로 끄지 않는다. git 최초 반입 `b2ae30e`부터 `7ee8981:src/SwanQCM.ftn90:561`, `43e9bbb`까지 `clen = PI2 / max(dkx,dky)`가 유지된다. E·강함을 유지한다. 노트에는 수동 격자의 `dkx≠dky`에서만 두 이동 간격이 맞지 않으며 WIDTH 기본 격자는 이 후보를 피한다고 적는다. |
| R3:CP-016 | QC 격자·보간·영값·반복 제어 | — (문서 누락) | QC 격자·보간·영값·반복 제어. `src/SwanQCM.ftn90:1553` `ikb = log( sig/spcsig(1) ) / FRINTF`; `src/SwanQCM.ftn90:1584` `ctb = 0.`; 1588의 네 점 쌍선형 보간; `src/SwanQCM.ftn90:1613` `if ( W(iky,ikx,1) /= 0. ) then`; `src/SwanQCM.ftn90:2222` `do ik = 0, min(ikx-1,ish-1)`; 1381–1384는 sweep·경계 위치로 산란 재계산을 선택한다. 350 `PNUMS(2) = PNUMS(2) * hsi`; `src/SwanQCM.ftn90:523` `mkxc = 1 + nint(kxlen/dkx)`. | C 문서 누락 | 주파수는 로그 좌표에서 보간한다. 영역 밖과 $k=0$은 0으로 둔다. 중심 W가 0이면 기울기를 0으로 만든다. 합은 W 배열 경계와 q범위의 교집합만 읽는다. 계산한 `memqcm`을 다른 sweep에서 재사용한다. 초기화는 절대 멈춤 기준에 입사 파고 척도 `hsi`를 곱한다. 자동 파수 격자의 점 수는 길이와 간격의 비를 가장 가까운 정수로 반올림한 뒤 1을 더한다. 대상 절에는 이 세부 규칙이 없다. C의 문서 범위는 swantech 3.9와 swanuse SCAT 절이다. swanuse PDF 94쪽 / 인쇄 86쪽은 QC의 절대 종료 기준을 `[dabs] × Hinc`로 명시한다. 입사파고 배율은 문서 누락에서 제외한다. C는 앞서 열거한 격자·보간·영값·sweep 재사용의 구현 세부에 한정한다. `PROPSL=3`의 기울기 미정의는 CP-013의 별도 E 판정이다. [10-13 전수 검증 정정]
| R3:CP-017 | QC 쇄파의 상관함수·재정규화 | — (문서 누락) | QC 쇄파의 상관함수·재정규화. `src/SwanQCM.ftn90:2572`의 역 FFT; `src/SwanQCM.ftn90:2610` `cfd(iys,ixs) = disqc(iyd,ixd) * cfd(iys,ixs)`; 2618의 정 FFT; `src/SwanQCM.ftn90:3100` `disqc = 0.5 * ( dpos + dneg )`; `src/SwanQCM.ftn90:3112` `integer, parameter :: maxit = 2`; `src/SwanQCM.ftn90:3113` `real, parameter :: larger = 1.01`; `src/SwanQCM.ftn90:3114` `real, parameter :: smaller = 0.99`; `src/SwanQCM.ftn90:3175` `disqc = disqc * varW * disbk / varD`. | C 문서 누락 | $x\pm\xi/2$에서 이전 반복의 총소산을 보간한 평균을 상관함수에 곱한다. 양의 적분 소산이 나오면 최대 두 번 양의 항을 0.99배, 음의 항을 1.01배 한다. 이후 `varD<0`이고 `varW>0`이면 총소산에 맞춰 재정규화한다. 아니면 소산을 0으로 만든다. 3.9는 이 계산 자체를 미포함으로 기술한다. 정확한 제어 조건은 `src/SwanQCM.ftn90:3121`의 `if ( varD > 0. .and. j < maxit ) then`과 3173행의 `if( varD < 0. .and. varW > 0. ) then`이다. swanuse PDF 90·SCAT 절도 QC 쇄파를 장래 포함 대상으로 적는다. C는 swantech 3.9와 이 사용자 문서에 없는 GEN4 전용 QC 쇄파 구현을 뜻한다. |
| R3:NT-024 | QC FFT의 변환 대상·방향 | 현재 노트의 수정 전 원문: `source-analysis/swan-quasi-coherent.md:64` `Direct FFT — spectral → 공간 (action density)`; 106 `spectral ↔ spatial 변환`. | `src/SwanQCM.ftn90:863` `rft(i,j) = sig - sigp`; `src/SwanQCM.ftn90:881` `cft = cmplx(rft)`; 883의 정 FFT. | B 문서 오기 | `SWQCDFT`는 국소점 주변의 고유주파수·군속도 변동을 공간에서 매질 파수 q공간으로 변환한다. `SWQCUFT`는 흐름 변동을 같은 방식으로 변환한다. 작용밀도 자체의 FFT가 아니다. |
| R3:NT-025 | Wigner 정의의 정규화·변수 | 현재 노트의 수정 전 원문: `source-analysis/swan-quasi-coherent.md:82` `W(\vec{k}, \vec{x}, t) = \int`; 84 `complex envelope`. | `src/SwanQCM.ftn90:1593` `W(iky,ikx,ic) = ctb * cg / k`; `src/SwanQCM.ftn90:2360` `memqcm(id,is,KCGRD(1)) = ctb * kwave(is,1) / cgo(is,1)`. Akrish et al. (2020), 1차 논문 ([외부 원문 대조](../../../_staging/recovery/compare/SWAN-external-sources.md)), A2-4–A2-6, 식 (2.2)–(2.4), (2.10)–(2.12); swantech PDF 111, 식 (3.44); [외부 원문 판정](../../../_staging/recovery/compare/SWAN-external-sources.md). | F 표기 차이 | swantech 2.7의 수면 높이 변수와 Akrish 외의 작용 변수 $\psi$를 구분한다. swantech 원문을 전사할 때는 $W=(4\pi^2)^{-1}\int\Gamma e^{-i\vec k\cdot\vec\xi}d\vec\xi$를 유지한다. 코드는 분산 기준 작용밀도를 $W_k=(c_g/k)W_{\sigma\theta}$로 변환한다. 역 야코비안 $k/c_g$는 산란항에 적용한다(`src/SwanQCM.ftn90:2360` `memqcm(id,is,KCGRD(1)) = ctb * kwave(is,1) / cgo(is,1)`). 이 차이를 코드 결함으로 분류하지 않는다. |
| R3:NT-026 | QC 진화식의 전사 | 현재 노트의 수정 전 원문: `source-analysis/swan-quasi-coherent.md:90` `\vec{c}_\theta \cdot \nabla_k W`. | `src/swancom1.ftn:5402`의 `CALL SORDUP`; `src/SwanQCM.ftn90:2360` `memqcm(id,is,KCGRD(1)) = ctb * kwave(is,1) / cgo(is,1)`. `src/swancom1.ftn:5401–5404`; swantech PDF 111쪽 / 인쇄 103쪽, 식 (3.44).<br>`src/swanmain.ftn:3825` `IF (IQCM.EQ.1) IREFR = 0`; `src/swanmain.ftn:3828` `ITFRE = 0`. | B 문서 오기 | 이론 진화식은 $\partial_tW+\nabla_k\omega\cdot\nabla_xW=S_{qc}$다. 기본 QC는 굴절을 산란항에 포함한다. 주파수·방향 격자에서는 (3.44)의 보존형 전파와 $J^{-1}S_{qc}$를 사용한다. |
| R3:NT-027 | 근거 없는 W의 두 성분 분해 | 현재 노트의 수정 전 원문: `source-analysis/swan-quasi-coherent.md:98` `W = N_0 + W_c`; 100 `이 분리의 격자 크기`; `manual-notes/swan-tech-ch2-7-qcm-theory.md:106` `W = N_0 + W_c 분리`. | `src/SwanQCM.ftn90:573` `if ( qmax < 2. ) then`; `src/SwanQCM.ftn90:575` `qmax = 2.`; `src/SwanQCM.ftn90:577` `ncoz = 2*floor(ceiling(qmax)/2.)`; `src/SwanQCM.ftn90:578` `dxps = clen / real(ncoz) / 2.`. | B 문서 오기 | QC는 $\mu$에 대해 1차 근사를 취한다. 파수 이동 $W(\vec k-\vec q/2)$는 유지한다. $W=N_0+W_c$ 및 작은 진폭 성분이라는 설명은 삭제한다. `ncoz`는 매질 변동 FFT 격자의 한 축 점 수다. |
| R3:NT-037 | FILQCM의 우변 조립 | 현재 노트의 수정 전 원문: `source-analysis/swan-quasi-coherent.md:73` `Source term filtering + output`; 110 `FILQCM` 뒤 `출력`. | `src/SwanQCM.ftn90:3270–3282`는 QC 산란항을 `imatra`와 `redc0`에 더한다. 3304–3316행은 GEN4 쇄파항을 `imatra`와 `dissc0`에 더한다. 진단 출력은 TESTFL 조건으로 함께 수행한다. 이 루틴의 주 동작을 필터링·출력으로만 표현한 기능 분류를 B로 정정한다. | B 문서 오기 | `FILQCM`은 QC 산란항을 수지식 우변에 더한다. QC 쇄파항과 진단 출력도 처리한다. 출력 전용 함수로 분류하지 않는다. |
| R3:NT-038 | QC 실행 비용 주장 | 현재 노트의 수정 전 원문: `source-analysis/swan-quasi-coherent.md:132` `cost (3464 lines, 12 subroutines, 4 FFT) 가 spectral SWAN 대비 큼`. | — | H 코드 대조 대상 아님 | 줄 수와 함수 수를 실행 비용의 정량 근거로 사용하지 않는다. |
| R3:QC-069 | QC 모드별 굴절 처리 | swantech PDF 75쪽 / 인쇄 67쪽, 각주 11: $-\nabla_{\vec x}\omega\cdot\nabla_{\vec k}W$를 좌변에 넣는 방법에 대해 “we will not do so here.” | `src/swanmain.ftn:3825` `IF (IQCM.EQ.1) IREFR = 0`; `src/swanmain.ftn:3828` `ITFRE = 0`. | C 문서 누락 | 기본 `IQCM=1`은 각주 11과 같다. `src/SwanQCM.ftn90:1388`의 `if ( IQCM == 1 ) call SWQCDFT`는 수심 산란을 이 모드에 한정한다. swanuse PDF 90–91과 `website/online_doc/swanuse/node28.html:3421–3446`은 모드 1·2의 물리 범위를 이미 설명한다. C는 swantech 각주에 없는 모드별 `IREFR` 및 모든 활성 QC의 `ITFRE = 0` 처리로 한정한다. |
| R3:QC-086 | 주변 영 흐름의 차분 생략 | swantech PDF 113쪽 / 인쇄 105쪽, 번호 없음: $\Delta\vec u=\mathcal W(x')\mathcal W(y')[\vec u(x+x',y+y')-\vec u(x,y)]$. | `src/SwanQCM.ftn90:1084` `if ( .not. u /= 0. .and. .not. v /= 0. ) cycle`; `src/SwanQCM.ftn90:1097` `rft(i,j) = uu - uxp`; `src/SwanQCM.ftn90:1098` `sft(i,j) = vv - uyp`. | E 코드 결함 후보 · 강함 | 주변 흐름이 정확히 0이고 현재점 흐름이 0이 아니면 식은 $-\vec u(x,y)$다. 코드는 초기값 0을 남긴다. 1070행의 “compute modulation of currents” 및 비영 흐름에서의 차분 경로와 모순된다. 입력 밖의 0을 피하려는 가능성은 있지만 실제 영 유속과 구분하는 조건은 없다. `src/SwanQCM.ftn90:1377–1389`에서 `IQCM > 0` 및 `ICUR == 1`인 호출 경로에 도달한다. `src/swanmain.ftn:5560–5561`의 영역 밖 0 반환과 실제 영 유속을 호출부가 구별하지 않는다. 이 조건문은 `b2ae30e`의 1080행과 `7ee8981`·`43e9bbb`의 1084행에 있다. [SWAN-git-verify-E.md](../../../_staging/recovery/compare/SWAN-git-verify-E.md)의 E 유지(강함)를 반영한다. QC 유속 변조는 주변 두 성분이 정확히 0이면 차분을 생략한다. 현재점 유속이 비영이면 실제 영 유속 지점의 변조량을 잘못 0으로 둔다. |
| R5:PN-157 | QC 최소 범위 | — (문서 누락) | `src/SwanQCM.ftn90:572` `qmax = min (qmu, alfa * kmean) / max(dkx,dky)`, `src/SwanQCM.ftn90:573` `if ( qmax < 2. ) then`, `src/SwanQCM.ftn90:575` `qmax = 2.`, `src/SwanQCM.ftn90:577` `ncoz = 2*floor(ceiling(qmax)/2.)`. | C | QC 절단 범위에는 격자 간격으로 정규화한 최소값 2가 적용된다. |
