---
title: "Delft3D-FLOW Z-layer 스칼라 transport solver source-analysis — z_difu.f90 (Van Leer-2 advection·same-layer diffusion·plain Jacobi)"
topic: delft3d-z-difu-transport
canonical_source: self
citation_status: verified
verification_method: "Delft3D raw source 직접 read: compute/z_difu.f90(1543) — Van Leer-2 limiter(:863-877)·plain Jacobi iteration(:1418) file:line 직접 검증. 소스주석 primary Bijvelds-van Kester-Stelling 1999(:78-80). sigma difu.f90([[delft3d_difu_transport]])의 Z-좌표 counterpart. sigma_z.md 는 flux 형태·mass-conservation init 만 커버."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
verification_by: "Claude Opus 4.8 (1M context) — z_difu.f90:863-877·1416-1429 직접 read 검증"
verification_date: 2026-07-04
related:
  - models/Delft3D/source-analysis/delft3d_difu_transport.md
  - models/Delft3D/source-analysis/delft3d_sigma_z.md
  - models/Delft3D/source-analysis/delft3d_anticreep_difhor.md
---

# Delft3D-FLOW Z-layer 스칼라 transport — `z_difu.f90`

> 소스: [`.../compute/z_difu.f90`](../raw/source_code/Delft3D/src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src/compute/z_difu.f90) (1543).
> **정체**: **Z-layer(고정 수평층) 스칼라 transport** — sigma [[delft3d_difu_transport]](difu.f90)의 Z-좌표 counterpart. 호출 `z_trisol.f90:1705,2507`(hydrostatic X/Y sweep)·`z_trisol_nhfull.f90`. dispatch `trasol='van leer-2'`(explicit) vs `'iupw'`(implicit).
> [[delft3d_sigma_z]] 는 z_difu 의 flux 형태·mass-conservation init(:362-389)만 커버 → 나머지(transport 스킴·6 서브루틴·Van Leer-2·plain Jacobi) 미커버.

## 0. 구조 (host + 6 internal, `contains` :838)

| 서브루틴 | 라인 | 역할 |
|---|---|---|
| `z_difu`(host) | 1-834 | 행렬조립: mass-conservation init·source/sink·연직 advection/diffusion·BC·row-scaling |
| `z_difu_horadv_expl` | 845-967 | **Van Leer-2** explicit 수평 advection(X→Y) |
| `z_difu_horadv_impl` | 971-1145 | 1차 upwind implicit 수평 advection |
| `z_difu_difhor_expl` | 1149-1212 | **same-Z-layer** 수평 diffusion(★anti-creep 아님) |
| `z_difu_difhor_impl` | 1216-1286 | implicit same-layer diffusion(off-diag) |
| `z_difu_solv_expl` | 1290-1360 | Thomas 연직 소거+back sweep |
| `z_difu_solv_impl` | 1364-1539 | **plain Jacobi** 수평 반복(max 50) + Thomas |

## 1. Van Leer-2 수평 advection (:863-877)
```fortran
cfl = u(nm,k)*timest/gvu(nm)                              ! :865
rr1 = |r0(nmd)-2*r0(nm)+r0(nmu)| ; rr2 = |r0(nmd)-r0(nmu)|  ! :868-869 단조성 guard
if( ... .or. rr1>=rr2 .or. rr2<eps .or. kcs==3 )then
   r00 = r0(nm)                                            ! :871 donor(비단조→1차 강등)
else
   r00 = r0(nm) + (1-cfl)*(r0(nm)-r0(nmd))*(r0(nmu)-r0(nm))/(r0(nmu)-r0(nmd))   ! :873-876 CFL가중 2차
endif
flux = qxk(nm,k)*r00                                       ! :878
```

## 2. 연직 advection/diffusion (:484-566)
- 연직 advection: `kfw` bottom/top 계면 upwind 스위치(:488-492) 외 **2차 central**(:498-512, adza/adzc 부호분할). ★헤더(:59)는 "first order upwind"라 적었으나 실제는 central+경계blend(comment≠code).
- 연직 diffusion: `delz=max(1e-4, 0.5(dzs1(k)+dzs1(k+1)))`(:533) 실제 metric 거리 + internal-wave `difiwe=0.2√bruvai·xlo²`(:537), `reddic(vicww/sigdif)`(유사=seddif bypass) → `ddzc=gsqs·diz1/delz`(:558).

## 3. same-layer 수평 diffusion (`difhor_expl/impl`, :1149-1286) — ★anti-creep 아님
```fortran
! kfsz0(nm,k)*kfsz0(nmu,k)==1 (양 셀 같은 Z-층 k 에서 wet)
flux = 0.5*(cr-cl)*(difl+difr)/(0.7*gvu)                   ! :1172-1181 (★0.7 Prandtl-Schmidt 하드코딩)
```
> ★**이름은 difhor 지만 anti-creep 재구성 아님**: Z-층이 이미 수평평면이라 "diffusion along Z-planes"(:61)는 **구성상 자동으로 strictly-horizontal** — interface merge-sort·Van Leer 제한기 불요(sigma [[delft3d_anticreep_difhor]] `difhor.f90` 와 대조). 진짜 Z anti-creep 재구성은 비정수압 sibling `z_difhor_nhfull.f90`(151)에만. **0.7 = SIGDIF 하드코딩**(:1177,1245, per-constituent sigdif 배열 우회).

## 4. plain Jacobi 수평 반복 (`solv_impl`, :1418-1527) — ★red-black 아님
```
! ITERATIVE SOLUTION METHOD (JACOBI ITERATION) IN HORIZONTAL DIRECTION  (:1418)
```
4-이웃 `bdx/bdy/buy/bux` RHS(:1443), 수렴 `epsitr=max(1e-8,0.5e-3·|r1|)`(:1504), `itr` 전역 max `dfreduce_gdp`(:1521), cap `iter<50`(:1523), 미수렴 error S206(:1525). **색깔 없는(uncolored) Jacobi** — 매 sweep 전 셀 old-iterate 이웃에서 갱신(sigma difu 의 red-black checkerboard [[delft3d_difu_transport]] §5 와 대조).

## 5. 기타
- Thomas(explicit-advection 경로) `bi=1/(bbkl-aakl*cckl(k-1))`(:1299) + back sweep.
- mass-conservation seed `bbkl=volum1/timest`·`ddkl=volum0*r0/timest`(:350) + top-layer fold(grow :362 / shrink→kmin :384).
- **tiny-volume 정규화**(:721-731): `bbkl<dzmin` 시 대각+dzmin(near-dry 나눗셈 blowup 방지).
- **★timest=2*hdt (full non-hydrostatic, :307)** — X+Y 1회 transport(hydrostatic half-step ADI 와 다름).
- **실험적 nudging**(:781-831, `nnudge=4`·`nudgefac=10`, `nudge==1` 게이트, 미문서).
- **forester filter 는 별 파일** `z_forfil.f90`(357, Forester 1977) — z_trisol 이 z_difu 후 호출, 본 노트 범위 밖.

## 6. 주요 findings
- **difhor same-layer = anti-creep 아님**(sigma 는 재구성, Z hydrostatic 은 trivial same-layer flux). 매뉴얼 단일 "anti-creep" 표현이 은폐.
- **plain Jacobi(uncolored) ≠ sigma red-black**.
- **0.7 Prandtl-Schmidt 하드코딩**(per-constituent sigdif 우회).
- **연직 advection = 2차 central**(헤더 "1차 upwind" 오기).
- **timest 배증**(full non-hydrostatic X+Y 1콜).

## 7. 관련
- [[delft3d_difu_transport]] — sigma difu.f90(★해법 대조: red-black vs plain Jacobi, cyclic vs Van Leer-2)
- [[delft3d_sigma_z]] — Z/sigma flux 형태·층 mechanics(z_difu init 인용)
- [[delft3d_anticreep_difhor]] — sigma difhor(진짜 anti-creep, Z difhor 와 대조)
- **Primary**: Bijvelds-van Kester-Stelling 1999(Z-model 구현) · Van Leer(제한기, uncited) · Forester 1977(z_forfil sibling).
