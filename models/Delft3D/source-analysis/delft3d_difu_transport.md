---
title: "Delft3D-FLOW 스칼라 transport ADI solver source-analysis — difu.f90 (advection-diffusion, red-black Jacobi + Thomas)"
topic: delft3d-difu-transport
canonical_source: self
citation_status: verified
verification_method: "Delft3D raw source 직접 read: engines_gpl/flow2d3d/.../compute/difu.f90(1096줄) — cyclic X-advection 6/3/1 stencil(:379-409)·red-black checkerboard color(:843-849) file:line 직접 검증. 소스주석 primary Stelling-van Kester 1994 IJNMF 18(:54-58)·Thatcher-Harleman(:74-77). momentum ADI [[delft3d_adi_solver]] 의 transport 짝."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
verification_by: "Claude Opus 4.8 (1M context) — difu.f90:379-412·841-852 직접 read 검증"
verification_date: 2026-07-04
related:
  - models/Delft3D/source-analysis/delft3d_adi_solver.md
  - models/Delft3D/source-analysis/delft3d_sigma_z.md
  - models/Delft3D/source-analysis/delft3d_turbulence.md
---

# Delft3D-FLOW 스칼라 transport ADI solver — `difu.f90`

> 소스: [`.../flow2d3d/packages/flow2d3d_kernel/src/compute/difu.f90`](../raw/source_code/Delft3D/src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src/compute/difu.f90) (1096줄, 단일 subroutine).
> **정체**: 염분·수온·유사·나선류강도·수동tracer 의 이류-확산(advection-diffusion). [[delft3d_adi_solver]](momentum SUD/UZD)의 **transport 짝** — 구조격자 curvilinear FLOW 커널. 기존 노트들은 difu 를 이름만 언급(adi_solver:50)하거나 sigma-vs-Z flux 형태만(sigma_z), transport 스킴/반복/행렬조립은 미커버.
> 호출부속 파일: `difacr.f90`(anti-creep Z-plane diffusion)·`dif_ws.f90`(유사 settling)·`secbou.f90`(나선류 BC).

## 0. ADI half-step + 방향 분할

`timest` = **half integration time step** (:150,336) — ADI 반스텝. 방향 `icx/icy` 스위치(:116-120)로 X-implicit/Y-explicit 교번 (momentum ADI 와 동일 방향분할이나 **해법이 다름**, §5 참조).

| 라인 | 단계 |
|---|---|
| :299-361 | init — 주대각 `bbk=volum1/timest`, RHS `ddkl=volum0·r0/timest` |
| :363-412 | X-advection (implicit higher-order upwind) |
| :414-444 | Y-advection (explicit central) |
| :453-523 | horizontal diffusion (sigma-plane / anti-creep) |
| :524-614 | vertical advection+diffusion (implicit) + internal-wave |
| :619-694 | dif_ws 유사 settling + open-bnd(Thatcher-Harleman) |
| :695-741 | sources(explicit)/sinks(implicit) |
| :767-1025 | row-scaling + Thomas 연직 + red-black Jacobi 반복 |
| :1047-1093 | open-boundary nudging |

## 1. X-advection — higher-order upwind "cyclic" 6/3/1 stencil (:379-409)

⚠ **flux limiter 없음** (van Leer/MinMod 아님 — 그건 unstructured dflowfm 경로). 고정 고차 upwind:
```fortran
qxu = qxk(nm,k)/6.0                          ! :379
iad1 = kfu(nm)*kadu(nm,k)                     ! :381 활성면 마스크
iad2 = iad1*kfu(nmd)*kadu(nmd,k)             ! :382
iad3 = iad2*kfu(nmdd)*kadu(nmdd,k)          ! :383
j1 = 6*iad1 + 3*iad2 + iad3                   ! :385 stencil 계수
j2 =        - 3*iad2 - 2*iad3                 ! :386
j3 =                     iad3                 ! :387
bbk(nm,k) += qxu*j1 ; bdx(nm,k) += qxu*j2 ; bddx(nm,k) += qxu*j3   ! :389-391 (7-band)
```
`iad1/iad2/iad3` = `kfu·kadu` 면마스크 — 닫힌/마른 면 근처에서 스텐실 차수 자동 강등(near-wall 1차로). 7-대각 `bdddx/bddx/bdx/bux/buux/buuux` 로 nm±1,±2,±3 결합(:168-185).

## 2. Y-advection — explicit central (:414-444)
```fortran
d0k = 0.5*qyv*((2*iad1-iad2)*r0(up) + iad2*r0(down))   ! :432-440 → ddkl(RHS)
```
안정한계 `DT ≤ DX²/(2·DICUV)`(:447-448) 때문에 확산은 implicit(아래).

## 3. Horizontal diffusion — sigma-plane / anti-creep (:453-523)
- **sigma-plane** (기본): implicit X `flux = 0.5(difl+difr)/(0.7·gvu)` — **0.7 = Prandtl/Schmidt σ**(:469-475), explicit Y(:496-503).
- **anti-creep** (`icreep/=0 .and. kmax>1`): `difacr` 로 strictly-horizontal 확산(:508-522) — 급경사 지형 sigma 가짜확산 억제. **알고리즘 본체(Van Leer 조화평균 제한기)는 [[delft3d_anticreep_difhor]] `difhor.f90`** (difacr 는 dispatcher).
  - 근거 (소스주석 :54-58): **Stelling & van Kester 1994, "On the approximation of horizontal gradients in sigma co-ordinates for bathymetry with steep bottom slopes", Int. J. Num. Methods Fluids 18.**

## 4. Vertical advection+diffusion + internal-wave (:524-614)
- implicit central 연직 이류(`kfw` 상/하계면 upwind 스위치, :526-551) → `aak/bbk/cck`.
- implicit 연직 확산(:566-614) + **internal-wave 혼합**:
```fortran
difiwe = 0.2*sqrt(bruvai)*xlo**2       ! :587 내부파 혼합 (bruvai=Brunt-Väisälä²)
```
`vicww/sigdif` 에 가산 후 `reddic`(dicoww 제한) 통과 — **유사(sediment)는 reddic bypass**(:595). ★`reddic` 이 TURCLO 아닌 difu 로 이동(:599-602) — [[delft3d_turbulence]] vicww/dicww 결합 미묘점.

## 5. 해법 — row-scaling + Thomas 연직 + red-black Jacobi 수평반복 (:767-1032)

⚠ **핵심 차이(momentum ADI 와)**: 수평은 direct band solve 가 **아니라 iterative red-black Jacobi 외부루프**, 각 반복 내에서 연직은 exact Thomas. 즉 "X-implicit/Y-explicit"의 실제 의미 = 연직 direct + 수평 relaxation.
```fortran
rscale = 1.0/bbkl                            ! :793 대각 정규화(k=1 pivot 나눗셈 회피)
bi = 1.0/(bbkl - aakl*cckl(k-1))             ! :812 Thomas forward elim
! red-black 시작색 = 서브도메인 parity:
if( mod(mfg+nfg,2)==1 ) nmsta=1 else nmsta=2 ! :843-849
nmsta = 3 - nmsta                            ! :888,957 색 교대(2 half-sweep/iter)
epsitr = max(ad_epsabs, ad_epsrel*abs(r1))   ! :939 수렴기준
call dfreduce_gdp(itr,...,dfmax)             ! :1023 병렬 전역 max
! goto while itr>0 .and. iter<ad_itrmax ; 미수렴→error S206 (:1030)
```

## 6. Boundary + nudging (:631-694, 1047-1093)
- **Thatcher-Harleman** open-bnd(:74-77,659-672): outflow=내부 반사, inflow=`rbnd` 값. `thahbc.for` 연계.
- **nudging**: `nnudge=4`셀 relaxation, `mu(jj)=mu(jj-1)/10`, `r1 = rp + mu·(rb-rp)`(:1047-1093).

## 7. 주요 findings
- **flux limiter 없음** — 고정 고차 upwind(6/3/1). van Leer/MinMod 는 dflowfm(unstructured) 경로. 매뉴얼→코드 오매핑 방지.
- **수평 = iterative red-black Jacobi**(direct 아님), 연직 = exact Thomas. `ad_itrmax/ad_epsabs/ad_epsrel` 지배. momentum ADI double-sweep 과 구조적 상이.
- `reddic` dicoww-restriction 이 non-sediment constituent 에 대해 TURCLO→difu 이동(:599-602).
- 비활성/영구건조 셀 `bbk=1.0`(비체적스케일) + 나선류강도 0(:342-343) — 출력 해석 masking.

## 8. 관련
- [[delft3d_adi_solver]] — momentum SUD/UZD ADI (본 노트의 짝, 동일 방향분할 다른 해법)
- [[delft3d_sigma_z]] — sigma/Z flux 형태(difu/difuvl/z_difu 층 mechanics)
- [[delft3d_turbulence]] — k-ε(tratur/turclo), vicww/dicww 가 difu 연직확산 공급
- **Primary(소스 verbatim)**: Stelling-van Kester 1994 IJNMF 18(anti-creep) · Thatcher-Harleman(open-bnd).
