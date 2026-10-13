---
title: "SWAN Bragg scattering — SwanBraggScat.ftn90 verified"
topic: swan
canonical_source: self
citation_status: verified
verification_method: "SwanBraggScat.ftn90의 인용 실행문과 호출·입력 분기를 대조했다. swantech PDF 57–58쪽과 swanuse PDF 79–81쪽을 대조했다. R2·R5 최종 결론과 대조했다." # [10-13 전수 검증 정정]
note_author: "Claude Opus 4.7 (1M context) raw source direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — header verbatim + grep subroutines"
verification_date: 2026-06-01
last_source_check: 2026-10-13 (recovery 대조 반영)
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
  - models/SWAN/manual-notes/swan-booij-1999-jgr-foundational.md
---

## Scope

SwanBraggScat.ftn90 모듈의 SWAN Bragg scattering 구현. 배포판 41.51과 파일 내부 변경 번호 41.80을 구별한다. (`src/swanmain.ftn:965` `VERNUM = 41.51`)

## Source basis

- `models/SWAN/raw/source_code/swan/src/SwanBraggScat.ftn90` (1491 lines)
- Tech §2.3.7 (swantech.pdf p.48) — Bragg scattering theory
- User cmd BRAGG (swanuse.pdf p.71)

## 1. Module header (line 30-45 verbatim)

```
module SwanBraggScat
!   Authors
!   41.80: Dirk Rijnsdorp and Ad Reniers
!   Updates
!   41.80, September 2021: New module
!   Purpose
!   Contains data with respect to Bragg scattering
```

## 2. Module-level data (line 53-65)

```fortran
integer :: mkbx, mkby                              ! wave number space size (x, y) for bottom spectrum
real    :: dkbx, dkby                              ! wave number space resolution
real, allocatable :: botspc(:,:)                   ! bottom spectrum (user-provided)
real, allocatable :: dpmean(:)                     ! mean depth at computational grid points
real, allocatable :: fb(:,:,:)                     ! bed elevation spectrum at computational grid points
real, allocatable :: fbdxy(:,:,:,:)                ! bottom spectrum at wave number difference k-k' for all grid points
```

차이 파수에서 바닥 스펙트럼을 이중 선형 보간한다. `fbdxy` 자체를 별도의 합성곱 계산 결과로 설명하지 않는다. (`src/SwanBraggScat.ftn90:63` `bottom spectrum at wave number difference k - k'`; `src/SwanBraggScat.ftn90:755`의 `fbdxy(ida,id,is,ic)` 대입)

## 3. Subroutine inventory (7 sub-routines, line 69-1491)

| Line | Subroutine | Purpose |
|---|---|---|
| **69** | `SWBRBOT` | 평균 수심 + bed elevation spectrum 계산 (computational grid 별) |
| **524** | `fit2(x,y,z,n,a,b,c,ierr)` | 평면 적합. 수심 변동에서 빼는 식은 `p0+p1*x+p2*y`이다. (`src/SwanBraggScat.ftn90:339` `r(ix-ixs+1,iy-iys+1) = DEPTH(ip) - p0 - p1*x(k) - p2*y(k)`) |
| **561** | `SWFBXY(dep2, mudl2, spcsig, spcdir)` | Wave number difference spectrum 계산 |
| **771** | `SWFB(fbd, dep2, kwave, ecos, esin)` | Bed elevation spectrum 보간 (wave dir·freq 별) |
| **942** | `SWBRAGG1` | Bragg source term version 1 |
| **1094** | `SWBRAGG2` | 같은 Bragg 물리식을 sweep별 보간으로 조립한다. (swanuse PDF 80쪽 / 인쇄 72쪽) |
| **1247** | `SWBRAGG3` | 같은 Bragg 물리식을 반복별 보간으로 조립한다. 원천항을 `membrg`에 저장한다. (swanuse PDF 80쪽 / 인쇄 72쪽; `src/SwanBraggScat.ftn90:1368` `membrg(id,is,KCGRD(1)) = cf * DDIR * sbragg`) [10-13 전수 검증 보완] |
| **1382** | `FILBRG` | 저장한 원천항을 sweep의 우변에 더한다. (`src/SwanBraggScat.ftn90:1466` `imatra(id,is) = imatra(id,is) + membrg(id,is,KCGRD(1))`) |

## 4. SWBRBOT — mean depth + bed elevation spectrum (line 69-)

핵심 use clause:
```fortran
use ocpcomm4
use swcomm2
use swcomm3, only: pbrag, PI, MXC, MYC, MCGRD
use m_genarr, only: DEPTH, XCGRID, YCGRID, KGRPNT
use SwanGriddata, only: nverts, xcugrd, ycugrd
```

→ `DEPTH`, `XCGRID/YCGRID`, `KGRPNT` (input depth grid + computational grid mapping) + `SwanGriddata` (unstructured vertex coord).

Local 변수 핵심:
- `nreg` = region of depth points around comp grid point (size for mean + spectrum)
- `ix, iy` loop counter (depth grid window)
- `ixc, iyc` loop counter (comp grid)
- `vard` = variance of small scale bed elevation
- `src/SwanBraggScat.ftn90:350` `call cfft2b ( nreg, nreg, nreg, c, wsave, lensav, work, lenwrk, ierr )`
- `p0, p1, p2` = polynomial fit coefficients (real*8)

코드는 평면을 뺀 바닥의 공간 분산과 Fourier 스펙트럼 적분을 맞춘다. (`src/SwanBraggScat.ftn90:339` `r(ix-ixs+1,iy-iys+1) = DEPTH(ip) - p0 - p1*x(k) - p2*y(k)`; `src/SwanBraggScat.ftn90:358`의 `0.5 * abs(c)**2`; `src/SwanBraggScat.ftn90:364`의 `vard / vars`)

## 5. 3 Bragg source term variants (`SWBRAGG1/2/3`)

세 루틴은 같은 Bragg 물리식을 서로 다른 보간·저장 방식으로 조립한다. `membrg`는 source 저장 배열이다. (swanuse PDF 80쪽 / 인쇄 72쪽; `src/SwanBraggScat.ftn90:1068`·`src/SwanBraggScat.ftn90:1221`·`src/SwanBraggScat.ftn90:1364`의 `cosdif**2. * fbdif * edif`)

각 `SWBRAGG*` 인자:
- `IMATRA`는 행렬 대각이 아니라 우변이다. (`src/SwanBraggScat.ftn90:1466` `imatra(id,is) = imatra(id,is) + membrg(id,is,KCGRD(1))`; `src/swancom1.ftn:7824–7827`의 `store in right hand vector` 주석과 FILBRG 호출) [10-13 전수 검증 보완]
- `ac2` = action density spectrum
- `dep2` = depth
- `kwave, cgo` = wave number + group velocity
- `fbd` = bed elevation spectrum (SWFB 의 출력)
- `idcmin/idcmax/isstop` = directional index bounds
- `ecos/esin` = direction cosine/sine arrays
- `plbrag` = print/diagnostic
- `redc0` = reduction coefficient

`FILBRG`는 저장한 원천항을 sweep의 우변에 더한다. 이 루틴은 필터를 계산하지 않는다. (`src/SwanBraggScat.ftn90:1466` `imatra(id,is) = imatra(id,is) + membrg(id,is,KCGRD(1))`)

## 6. User cmd BRAGG (swanuse.pdf p.71)

FT는 계산 수심에서 바닥 스펙트럼을 만든다. FILE은 외부 스펙트럼을 읽는다. 원천항 갱신은 IBRAG에 따라 sweep별 또는 반복별이다. (swanuse PDF 80–81쪽 / 인쇄 72–73쪽)
수심 변동에서 빼는 식은 `p0+p1*x+p2*y`다. (`src/SwanBraggScat.ftn90:339` `r(ix-ixs+1,iy-iys+1) = DEPTH(ip) - p0 - p1*x(k) - p2*y(k)`)
IBRAG=4의 원천항 분기는 비어 있다. (`src/swancom1.ftn:7830` `ELSE IF ( IBRAG.EQ.4 ) THEN`; `src/swancom1.ftn:7835` `ENDIF`)

## 7. 이론적 기반

**Bragg scattering** = bottom topography (랜덤 또는 결정적) 와 wave 의 **k-k' 공명 산란**:

$$\vec l=\vec k-\vec k'$$

일반 Bragg 관계는 $\vec l=\vec k-\vec k'$이다. 두 파랑 방향이 정반대일 때 $\lvert\vec l\rvert=2k$가 된다. 파장의 절반 조건은 이 후방 산란의 경우에 한정한다. (swantech PDF 57–58쪽 / 인쇄 49–50쪽; `src/SwanBraggScat.ftn90:893` `lx = k * ( ecos(id) - ecos(ida) )`)

해안공학 응용: sand bar field, ripple field 위 wave 전파 시 wave energy redistribution.

## 8. Cross-references

- [swan-documentation-stack](../manual-notes/swan-documentation-stack.md) §2.3.7 Bragg scattering theory
- [swan-source-terms-implementation](wave/swan-source-terms-implementation.md) — S_total = S_in + S_ds + S_nl + **S_bragg** 통합
- [swan-source-coverage-audit](swan-source-coverage-audit.md) §3.1 신규 발견 식별
- User Manual BRAGG cmd (p.71)
- Authors: Dirk Rijnsdorp + Ad Reniers (41.80, 2021-09)

## 9. 원문 대조

- 필요한 바닥 파수가 입력 격자 밖이면 끝값을 사용한다. (`src/SwanBraggScat.ftn90:901–918`의 격자 끝 인덱스·가중치 설정)
- (2.117) 외에 깊은 물 절단을 적용한다. (`src/SwanBraggScat.ftn90:1049` `if ( kd < 5. ) then`)
- 세 루틴은 같은 Bragg 물리식을 서로 다른 보간·저장 방식으로 조립한다. (swanuse PDF 80쪽 / 인쇄 72쪽)


## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

대조 보고서: [R2](../../../_staging/recovery/compare/swan-theory-sources-vs-code.md) · [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R2:SS-731 | 노트 · source-analysis/swan-bragg-scattering.md:19 | `source-analysis/swan-bragg-scattering.md:19` `SWAN 41.80 (2021-09 Rijnsdorp+Reniers)`; `manual-notes/swan-tech-ch2-vegetation-ice-bragg-gen12.md:299`의 같은 판 표기. | `src/swanmain.ftn:965` `VERNUM = 41.51`. Bragg 파일의 41.80은 내부 변경 이력 표기이다 | B | 배포판 41.51과 파일 내부 변경 번호 41.80을 구별한다. 내부 번호만으로 배포판의 출시 순서를 만들지 않는다. |
| R2:SS-524 | Bragg의 $kd<5$ 절단과 입력 바닥 스펙트럼 격자 밖의 보간 처리 | swanuse PDF 80쪽 / 인쇄 72쪽은 세 `IBRAG` 값의 보간·저장·갱신 시점을 설명한다. | `src/SwanBraggScat.ftn90:1049` `if ( kd < 5. ) then`; 901–918의 격자 끝 인덱스·가중치 설정; `src/SwanBraggScat.ftn90:1374` 의 `membrg` 초기화 | C | (2.117) 외에 깊은 물 절단을 적용한다. 필요한 바닥 파수가 입력 격자 밖이면 끝값을 사용한다. `SWBRAGG3`의 `membrg`는 계산된 source 저장 배열이다. 물리적 막을 뜻하지 않는다. C는 swantech PDF 57–58쪽 / 인쇄 49–50쪽에 `kd < 5.` 절단과 입력 격자 끝값 처리의 세부가 없는 점이다. 세 구현의 존재·저장 방식 자체는 사용자 매뉴얼에 있다. [10-13 결론 검증 보완] [10-13 전수 검증 정정] |
| R2:SS-525 | Bragg 바닥 스펙트럼의 국소 창·평면 제거·분산 정규화 | swantech PDF 57–58쪽 / 인쇄 49–50쪽과 swanuse PDF 80–81쪽 / 인쇄 72–73쪽은 격자점 주위의 고정 정사각형 영역·완만한 저면 제거·Fourier 변환을 설명한다. | `src/SwanBraggScat.ftn90:339`의 `r(ix-ixs+1,iy-iys+1) = DEPTH(ip) - p0 - p1*x(k) - p2*y(k)`; `src/SwanBraggScat.ftn90:358` 의 `0.5 * abs(c)**2`; `src/SwanBraggScat.ftn90:364` 의 `vard / vars` | C | 코드는 평면을 뺀 바닥의 공간 분산과 Fourier 스펙트럼 적분을 맞춘다. `cfft2b` 이름만으로 FFT 정규화를 판단하지 않는다. 뒤의 분산 배율까지 포함해야 한다. 국소 영역과 저면 제거·FFT 자체는 문서에 있다. C는 이 설명에 `p0+p1*x+p2*y` 평면의 실제 대입과 `vard/vars` 분산 정규화가 없는 점으로 좁힌다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-727 | 노트 · source-analysis/swan-bragg-scattering.md:94 | `source-analysis/swan-bragg-scattering.md:94` `3 가지 Bragg source term 식 구현 추정`; 96 `extended (mud layer`; 97 `membrane-like reflection?`. | `src/SwanBraggScat.ftn90:1068`·1221·1364의 같은 `cosdif**2. * fbdif * edif` | B | 세 루틴은 같은 Bragg 물리식을 서로 다른 보간·저장 방식으로 조립한다. `membrg`는 source 저장 배열이다. 진흙 전용식·막 반사식이라는 추정은 삭제한다. [10-13 결론 검증 보완] |
| R2:SS-728 | 노트 · source-analysis/swan-bragg-scattering.md:63 | `source-analysis/swan-bragg-scattering.md:63` `filtering / output`; 110 `diagonal/off-diagonal 항 추가`. | `src/SwanBraggScat.ftn90:1466` `imatra(id,is) = imatra(id,is) + membrg(id,is,KCGRD(1))` | B | `FILBRG`는 저장한 원천항을 sweep의 우변에 더한다. 이 루틴은 필터를 계산하지 않는다. `IMATRA`는 행렬 대각이 아니라 우변이다. |
| R2:SS-729 | 노트 · source-analysis/swan-bragg-scattering.md:120 | `source-analysis/swan-bragg-scattering.md:120` `k_1 + k_2 = K_b`; 124 `$\lambda_{wave}/2 \approx \lambda_{bottom}$`. | `src/SwanBraggScat.ftn90:893` `lx = k * ( ecos(id) - ecos(ida) )` | B | 일반 Bragg 관계는 $\vec l=\vec k-\vec k'$이다. 두 파랑 방향이 정반대일 때 $\lvert\vec l\rvert=2k$가 된다. 파장의 절반 조건은 이 후방 산란의 경우에 한정한다. |
| R2:SS-730 | 노트 · source-analysis/swan-bragg-scattering.md:50 | `source-analysis/swan-bragg-scattering.md:50` `convolution-based`. | `src/SwanBraggScat.ftn90:928`의 이중 선형 보간. `src/SwanBraggScat.ftn90:63`은 `fbdxy`를 `bottom spectrum at wave number difference k - k'`로 설명한다. 755행은 네 격자값의 이중 선형 보간으로 `fbdxy(ida,id,is,ic)`를 대입한다 | F | 노트의 `convolution-based`는 차이 파수 의존성을 느슨하게 표현한 말이다. 이 말만으로 별도 물리식 오류를 단정하지 않는다. 배열 생성의 정확한 설명은 차이 파수에서 바닥 스펙트럼을 이중 선형 보간한다는 것이다. `fbdxy` 자체를 별도의 합성곱 계산 결과로 설명하지 않는다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R5:PN-051 | Bragg 평활 수심 | swanuse PDF 80쪽 / 인쇄 72쪽 `bilinear fit` | `src/SwanBraggScat.ftn90:339` `r(ix-ixs+1,iy-iys+1) = DEPTH(ip) - p0 - p1*x(k) - p2*y(k)` | F | swanuse PDF 80쪽 / 인쇄 72쪽과 swantech PDF 57쪽의 `bilinear fit`은 코드의 평면 적합에 대한 느슨한 명칭이다. 구현은 `r(ix-ixs+1,iy-iys+1) = DEPTH(ip) - p0 - p1*x(k) - p2*y(k)`이며 xy 교차항이 없다. [10-13 결론 검증 정정] [10-13 전수 검증 정정] |
| R5:PN-158 | IBRAG=4 | swanuse PDF 80쪽 / 인쇄 72쪽은 `IBRAG=1/2/3`을 설명한다. | `src/swanpre1.ftn:3490` `CALL ININTG ('IBRAG' , IBRAG   , 'STA', 1 )`. `src/swancom1.ftn:7830` `ELSE IF ( IBRAG.EQ.4 ) THEN` 뒤에는 주석과 ENDIF만 있다 | C | IBRAG=4는 읽을 수 있지만 원천항 계산 분기는 비어 있다. [10-13 전수 검증 보완] |
