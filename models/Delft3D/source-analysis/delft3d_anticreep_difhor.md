---
title: "Delft3D-FLOW anti-creep 수평확산 제한기 source-analysis — difhor.f90 (Van Leer 조화평균) + difacr.f90 (sigma dispatcher)"
topic: delft3d-anticreep-difhor
canonical_source: self
citation_status: verified
verification_method: "Delft3D raw source 직접 read: compute/difhor.f90(294)+difacr.f90(186) — Van Leer 제한기(:276-280)·limited flux+scatter(:286-289) file:line 직접 검증. 소스주석 primary Stelling-van Kester 1994 IJNMF18(:45-49)·Bijvelds-van Kester-Stelling 1999(:49-56). [[delft3d_difu_transport]] 가 wrapper(difacr)만 언급한 anti-creep 알고리즘 본체."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
verification_by: "Claude Opus 4.8 (1M context) — difhor.f90:274-291 직접 read 검증"
verification_date: 2026-07-04
related:
  - models/Delft3D/source-analysis/delft3d_difu_transport.md
  - models/Delft3D/source-analysis/delft3d_sigma_z.md
  - models/Delft3D/source-analysis/delft3d_adi_solver.md
---

# Delft3D-FLOW anti-creep 수평확산 제한기 — `difhor.f90` + `difacr.f90`

> 소스: [`.../compute/difhor.f90`](../raw/source_code/Delft3D/src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src/compute/difhor.f90)(294, 제한기 본체) + [`difacr.f90`](../raw/source_code/Delft3D/src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src/compute/difacr.f90)(186, sigma dispatcher).
> **정체**: 급경사 지형 sigma 좌표의 **가짜 수직확산(artificial vertical diffusion)** 을 없애는 **strictly-horizontal 확산 + Van Leer 단조 제한기** — Stelling-van Kester 1994 의 간판 알고리즘. [[delft3d_difu_transport]]:21,62 는 `difacr`(wrapper)만 이름 언급, **실제 min/max flux 재구성은 `difhor` 에** 있고 위키 전역 미커버였음.

## 0. difacr = dispatcher, difhor = 알고리즘 (★핵심 정정)

`difacr.f90`(186줄)은 **sigma dispatcher**:
- **sal/tem**: `dengra` 사전계산 gradient 를 `ddkl` 에 직접 가산(:125-140) → sal/tem 만 있으면 early-exit(`goto 1000` :142).
- **기타 constituent(유사/tracer)**: 전 wet U-면(:150-163)·V-면(:170-184)에서 `difhor` 호출.

> ★**sal/tem 과 기타 constituent 경로가 다름**: 문서화된 "anti-creep salinity" 는 실제 [[delft3d_sigma_z]] `dengra`(gradient 산출)의 것이고, `difhor` Van Leer 재구성은 **유사/tracer 에만** 적용(:210 `l>max(lsal,ltem)`).

## 1. difhor 위상 구조 (:34-293, 단일 subroutine)

| 라인 | 위상 |
|---|---|
| :34-56 | 헤더("strict horizontal planes·new limiter following Van Leer·preserves monotony") |
| :133-149 | 좌/우 컬럼 interface Z-level `polal/polar` (sigma→물리 Z 투영) |
| :151-174 | 두 컬럼 interface **merge-sort → monotone `point(0:2kmax+1)`** |
| :176-205 | flux-point 중점 `poflu` + layer k-index 매칭 `kicol/kicor` |
| :207-293 | constituent별 재구성 + Van Leer 제한기 + flux scatter |

### 1.1 Strictly-horizontal Z-plane 투영 (:135-149)
```fortran
h0 = max(sepnm+dpnm, 0.01)                          ! :136 ★dry-cell 하한(기하 왜곡)
polal(k) = (sig(k) - 0.5*thick(k))*h0 + sepnm        ! :135 좌컬럼 interface 물리Z
pocol(k) = 0.5*(polal(k-1)+polal(k))                 ! :139 셀중심 Z
```
= sigma 층을 **물리 Z 평면으로 투영** → 확산을 sigma-따라가 아닌 수평으로.

### 1.2 Van Leer 제한기 (:271-280) ★핵심
```fortran
grad1 = r0(nmu,krr,l) - cl ; grad2 = cr - r0(nm,kll,l)   ! :269-270 교차 interface gradient
grmax = max(grad1,grad2) ; grmin = min(grad1,grad2)      ! :271-272
! *** new limiter following Van Leer (:274)
if( grmax>=0.0 .and. grmin<=0.0 )then
   grad = 0.0                                            ! :277 부호반대=국소극값→flux 0(단조보존)
else
   grad = 2.*grad1*grad2/(grad1+grad2)                   ! :279 조화평균(harmonic mean)
endif
```
> ★**Van Leer 조화평균**이지 단순 min/max 아님. `grmax/grmin` 은 **부호반대 극값 판정용**(flux=0), 값 자체는 harmonic mean `2g₁g₂/(g₁+g₂)`(Van Leer MUSCL 계열). 매뉴얼의 "min/max limiter" 표현은 historical.

### 1.3 제한 flux + 명시 scatter (:284-289)
```fortran
flux = 0.5*(point(kf-1)-point(kf))*grad*guu(nm)*(difl+difr)/sigdif(l)/gvu(nm)   ! :286-287
ddkl(nm ,kll,l) += flux*abs(2-kcs(nmu))              ! :288 RHS 가산(difu/z_difu 소비)
ddkl(nmu,krr,l) -= flux*abs(2-kcs(nm))               ! :289
```
flux-point 두께 × 제한 gradient × 평균 eddy diffusivity `(difl+difr)` / Prandtl-Schmidt `sigdif` × 격자 metric. `dicuv`(diffusivity) 입력.

## 2. 주요 findings
- **Van Leer 조화평균 제한기**(min/max 아님) — grmax/grmin 은 극값판정, 값은 `2g₁g₂/(g₁+g₂)`.
- **sal/tem vs 유사/tracer 경로 분리**: sal/tem=dengra gradient 직접가산, difhor 제한기=유사/tracer(:210).
- **완전 EXPLICIT (U·V 양방향, :42-43)** — 연직 implicit 확산(difu/z_difu)과 달리 수평 anti-creep 은 명시적(급경사 대확산 안정성 관련).
- **interface 기하 floored** `h0=max(sep+dp,0.01)`(:136) — drying front 근처 평면위치 왜곡.
- **개방경계 비대칭** `abs(2-kcs)`(:288-289) — 경계셀(kcs=2) 한쪽 기여 0, 단측 적용.
- **difhor 계열 ≥3**: sigma `difhor.f90` · 비정수압-Z `z_difhor_nhfull.f90`(151) · in-line Z `z_difu_difhor_expl/impl`(z_difu.f90:1149-1286). "anti-creep"는 단일개념 아닌 좌표별 구현.

## 3. Primary sources (소스 verbatim)
- **Stelling & van Kester 1994**, "On the approximation of horizontal gradients in sigma co-ordinates for bathymetry with steep bottom slopes", IJNMF **18** — difhor.f90:45-49 · difacr.f90:44-48.
- **Bijvelds, van Kester & Stelling 1999**, "A comparison of two 3D shallow water models using sigma- and z-coordinates...", Proc. 6th Int. Conf. Estuarine and Coastal Modelling — difhor.f90:49-56 ("improved limiter", **위키 신규 인용**).
- Van Leer MUSCL 계열(제한기 basis, :40,:274, 정식인용 없음).

## 4. 관련
- [[delft3d_difu_transport]] — sigma transport(difu.f90), difacr/difhor 를 anti-creep 옵션으로 호출(§3 에서 본 노트 참조)
- [[delft3d_sigma_z]] — dengra(sal/tem gradient, difacr 의 sal/tem 경로)·Z-layer
- [[delft3d_adi_solver]] — momentum ADI(같은 flow2d3d 커널)
- **Primary**: Stelling-van Kester 1994 IJNMF 18 · Bijvelds et al. 1999 · Van Leer.
