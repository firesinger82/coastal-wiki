---
title: "Delft3D-FLOW Forester anti-oscillation 필터 source-analysis — forfil.f90(sigma) + z_forfil.f90(Z) (음수제거 + Peclet 수직 monotone)"
topic: delft3d-forfil-forester-filter
canonical_source: self
citation_status: verified
verification_method: "Delft3D raw source 직접 read: compute/forfil.f90(411)+z_forfil.f90(357) — rmneg/maxfil(:167,169)·2차류 skip(:177) vs z tighten(:158)·Peclet gate>2(:322) file:line 직접 검증. 소스주석 primary Forester 1977 JCP 23(:52-54). difu/z_difu transport 직후 호출. [[delft3d_z_difu_transport]] 가 sibling 으로 명시(범위 밖)한 갭."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-07
verification_by: "Claude Opus 4.8 (1M context) — forfil.f90:165-178·318-326 + z_forfil.f90:155-158 직접 read 검증"
verification_date: 2026-07-07
related:
  - models/Delft3D/source-analysis/delft3d_difu_transport.md
  - models/Delft3D/source-analysis/delft3d_z_difu_transport.md
  - models/Delft3D/source-analysis/delft3d_sigma_z.md
---

# Delft3D-FLOW Forester anti-oscillation 필터 — `forfil.f90` + `z_forfil.f90`

> 소스: [`.../compute/forfil.f90`](../raw/source_code/Delft3D/src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src/compute/forfil.f90)(411, sigma) + [`z_forfil.f90`](../raw/source_code/Delft3D/src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src/compute/z_forfil.f90)(357, Z-layer).
> **정체**: transport([[delft3d_difu_transport]]/[[delft3d_z_difu_transport]]) 직후 **음수 농도 제거 + 수직 wiggle 평활**(Forester 1977). 호출 `trisol.f90:2104,3177`(sigma)·`z_trisol.f90:1774,2616`(Z). [[delft3d_z_difu_transport]]:70,83 이 sibling(범위 밖) 으로 명시한 갭. ※WAQ `vertical_forester_filter.f90`·dflowfm `doforester.f90` 는 별 엔진(무관).

## 0. 2-pass 구조 (각 파일 단일 subroutine)

| pass | forfil(sigma) | z_forfil(Z) | 조건 |
|---|---|---|---|
| **수평 음수제거** | :161-266 | :149-234 | `forfuv=='Y'` |
| **수직 monotone/Peclet** | :270-410 | :238-356 | `forfww=='Y'` |

## 1. 수평 음수제거 pass

```fortran
rmneg(l) = -1.0e-2                        ! :167(sigma)/:155(z) 음수 임계
maxfil   = 100                            ! :169/:157 반복 상한(★하드코딩)
if( r0 < rmneg ) idifu(nm)=1              ! :196/:181 음수셀 탐지
if( ifil==0 ) exit                        ! :201/:186 음수 소진 시 조기종료
! 4-이웃 0.125 diffusion(부피가중 cofnmu/nmd/num/ndm):
r1 = r0*(1-Σcof) + Σ(neighbor*cof)        ! :231-251/:199-219
! subdomain interface(kcu/kcv==3) → cof=0  :242/:210
! 미수렴(itfil==maxfil) → prterr U190 "Negative concentrations"  :258/:226
```

### ★2차류(secondary flow) 처리 — sigma vs Z 상이
```fortran
forfil(sigma) :177 : if( l==lsecfl ) cycle          ! 수평 pass 에서 2차류 완전 skip
z_forfil(Z)   :158 : if( lsecfl>0 ) rmneg(lsecfl) = -1.0e-8   ! skip 안 하고 임계만 강화
```

## 2. 수직 monotone/Peclet pass

```fortran
rmneg(l) = 1.0e-6 ; maxfil = 1000                   ! :287-288/:254-255 수직 임계·상한
! local max/min overshoot 검사(이웃 ± rmneg)         :295,342/:261,298
peclz = |w1(nm,k)| * coef / diz                     ! :318/:272 수직 Peclet
if( peclz > 2.0 )then                                ! :322/:277 ★수치 wiggle 만 필터
   r1(nm,k)  -= coef*dr/dz1                           ! :324/:279 보존적 재분배
   r1(nm,ku) += coef*dr/dz2                           ! :325/:280
endif
if( ifil==0 ) exit                                   ! :392/:338
! 미수렴 → prterr U190 "Vertical wiggle"  :399/:345
```

## 3. ★code≠code (sigma vs Z, 헤더는 동일 boilerplate)

두 파일 헤더 설명(:36-54 = :37-55)은 **동일**하나 실제 코드가 갈림:

| 항목 | forfil(sigma) | z_forfil(Z) |
|---|---|---|
| 수직필터 대상 | sal/tem **+ flbcktemp tracer**(:275) | sal/tem 만(:243) — 헤더와 일치 |
| 2차류(수평) | **skip**(:177) — 헤더와 일치 | 임계 tighten -1e-8(:158) — 헤더 overstates |
| 수직 diffusivity | 분자+internal-wave `difiwe=0.2√bv·xlo²`(:302)+vicww via reddic | 단순 `dicww/sigdif + vicmol/sigmol`(:273), internal-wave·reddic 無 |
| depth guard | `h0=s1+dps>0.01m`(:295,342) | 층두께 `coef>0.001`(1mm)(:277) |

- **헤더 "Vertical filter only for salinity and temperature"** = Z 만 정확, sigma 는 flbcktemp tracer 로 확장(헤더 위반).
- **iteration cap(maxfil 100/1000) 하드코딩 magic number** — 입력파일 제어 없음(매뉴얼 tunability 주장과 대조).
- pseudo-code/references 섹션 = 둘 다 literally `NONE`(:56,:57) — 유일 알고리즘 인용 = Forester 1977.

## 4. Primary source (소스 verbatim)
- **C.K. Forester, "Higher Order Monotonic Convective Difference Schemes", J. Computational Phys. 23, 1977** — forfil.f90:52-54·z_forfil.f90:53-55. (JCP 23(1):1-22, 1977 — ★1979 아님, 소스 in-code = 1977.)

## 5. 관련
- [[delft3d_difu_transport]] · [[delft3d_z_difu_transport]] — transport solver(Forester 는 직후 후처리 필터, trisol/z_trisol 이 순차 호출)
- [[delft3d_sigma_z]] — sigma/Z 좌표 mechanics
- **Primary**: Forester 1977 JCP 23.
