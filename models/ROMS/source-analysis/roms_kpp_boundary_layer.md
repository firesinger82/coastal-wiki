---
title: "ROMS KPP 연직혼합 deep — lmd_vmix/lmd_skpp/lmd_bkpp/lmd_swfrac (Large-McWilliams-Doney 1994)"
topic: roms-kpp-boundary-layer
canonical_source: self
citation_status: verified
verification_method: "ROMS raw source 직접 read: ROMS/Nonlinear/{lmd_vmix.F(664),lmd_skpp.F(930),lmd_bkpp.F(809),lmd_swfrac.F(91)} — file:line 인용 직접 검증(w-scale·bulk-Ri·shape function·nonlocal·interior mixing 재확인). Primary source = 소스 헤더 인용 Large-McWilliams-Doney 1994 Rev Geophys 32:363-403. CPP 플래그 cppdefs.h 대조. [[roms_vertical_mixing]] §D 의 KPP 심층 확장(기존은 GLS/MY25 대비 얕음)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
verification_by: "Claude Opus 4.8 (1M context) — lmd_skpp.F:442-531·860-921 + lmd_vmix.F:315-357 직접 read 검증"
verification_date: 2026-07-04
related:
  - models/ROMS/source-analysis/roms_vertical_mixing.md
  - models/ROMS/source-analysis/roms_baroclinic_3d.md
  - concepts/currents/04-code-and-tools.md
---

# ROMS KPP 연직혼합 deep — `lmd_*` (Large-McWilliams-Doney 1994)

> 소스: [`ROMS/Nonlinear/lmd_vmix.F`](../raw/source_code/roms/ROMS/Nonlinear/lmd_vmix.F)(664) · [`lmd_skpp.F`](../raw/source_code/roms/ROMS/Nonlinear/lmd_skpp.F)(930) · [`lmd_bkpp.F`](../raw/source_code/roms/ROMS/Nonlinear/lmd_bkpp.F)(809) · [`lmd_swfrac.F`](../raw/source_code/roms/ROMS/Nonlinear/lmd_swfrac.F)(91).
> Primary source (소스 헤더 lmd_vmix.F:19-21 등 verbatim): **Large, W.G., J.C. McWilliams, S.C. Doney, 1994. A Review and model with a nonlocal boundary layer parameterization. Reviews of Geophysics, 32, 363-403.**
> [[roms_vertical_mixing]] §D 의 KPP 심층 확장 — 기존 노트는 GLS/MY25 대비 KPP 를 ~10줄로만 다룸.

## 0. 3-티어 구조 + CPP 플래그

KPP = **interior mixing (전 수심) + surface BL (hsbl) + bottom BL (hbbl)** 3 티어. 마스터 스위치 `LMD_MIXING` (cppdefs.h), boundary layer 선택 `LMD_SKPP`/`LMD_BKPP`.

> ⚠ **플래그 정정**: `LMD_KPP` 플래그는 **존재하지 않음**(기존 노트 §D/§E 및 통상 오명). 실제 = `LMD_MIXING`(interior 마스터) + `LMD_SKPP`/`LMD_BKPP`(경계층) + `LMD_NONLOCAL`(ghats) + `LMD_RIMIX`(Ri shear) + `LMD_CONVEC`·`LMD_DDMIX`(대류·이중확산) + `RI_HORAVG`/`RI_VERAVG`/`RI_SPLINES`(Ri 평활/재구성).

| 파일 | 서브루틴 | 역할 |
|---|---|---|
| lmd_vmix.F | `lmd_vmix_tile`(:99-434) + `lmd_finish_tile`(:465-662) | interior 혼합 + interior/BL 결합 |
| lmd_skpp.F | `lmd_skpp_tile`(:98-928) | surface BL 전 알고리즘 (단일 대형 루틴) |
| lmd_bkpp.F | `lmd_bkpp_tile`(:95-807) | bottom BL |
| lmd_swfrac.F | `lmd_swfrac_tile`(:6-85) | Jerlov 단파 침투 swdk (KPP 부력강제 입력) |

> ⚠ **`lmd_wscale.F` 파일 없음**: turbulent velocity scale($w_m$/$w_s$)은 별도 파일 아니라 `lmd_skpp.F:442-471` / `lmd_bkpp.F:416+` 에 **인라인**.

## 1. Interior mixing (`lmd_vmix.F`) — 3 프로세스 중첩

전 수심 diffusivity = **shear instability + internal wave breaking + double diffusion** 중첩 (:315-317 주석).

### 1.1 Gradient Richardson number
`Rig = bvf/(shear²+eps)` (:225-226, W-point) → `RI_HORAVG`(수평 :280-292)·`RI_VERAVG`(연직 1-2-1 :299-306) 평활.

### 1.2 Shear-instability (`LMD_RIMIX`, :326-336)
```fortran
cff   = MIN(1., MAX(0., Rig)/lmd_Ri0)   ! Ri0 임계
nu_sx = 1. - cff*cff                    ! (1-(Ri/Ri0)²)
nu_sx = nu_sx*nu_sx*nu_sx               ! → ³제곱 (LMD Eq 28형)
shear2= bvf/(Rig+eps)
cff   = shear2²/(shear2²+16e-10)        ! Polzin 1996 magnitude factor
nu_sx = cff*nu_sx
```

### 1.3 Internal-wave background (Gargett-Holloway, :344-346)
`lmd_iwm=1e-6/√(max(bvf,1e-7))`, `lmd_iws=1e-7/√(...)` (momentum 10× tracer).

### 1.4 Assembly (:353-354)
`Akv = lmd_iwm + lmd_nu0m·nu_sx`, `Akt = lmd_iws + lmd_nu0s·nu_sx`.

### 1.5 Double diffusion (`LMD_DDMIX`, :360-414)
밀도비 `Rrho`(:376) → salt-fingering(:380-388) vs diffusive-convection(:397-414) 분기.

## 2. Surface boundary layer (`lmd_skpp.F`)

### 2.1 Turbulent velocity scale $w_m$/$w_s$ (인라인 wscale, :442-473) — Monin-Obukhov 유사

```fortran
Ustar3  = Ustar³
zetahat = vonKar*sigma*Bflux          ! :455  안정도 인자 (Bflux=부력 flux)
zetapar = zetahat/(Ustar3+small)      ! :456  ζ = d/L (Monin-Obukhov)
! 안정 (zetahat≥0):
wm = vonKar*Ustar/(1+5*zetapar)       ! :458   ws=wm
! 불안정 (zetahat<0):
wm = vonKar*Ustar*(1-16*zetapar)^0.25 ! :463 (zetapar>lmd_zetam)
   = vonKar*(lmd_am*Ustar3-lmd_cm*zetahat)^(1/3) ! :465 (그 이하, free-convection)
ws = vonKar*Ustar*(1-16*zetapar)^0.5  ! :468 / (lmd_as*Ustar3-lmd_cs*zetahat)^(1/3) :471
```

### 2.2 Bulk Richardson number → hsbl (:475-490)
```fortran
Ritop = -gorho0*(Rref-Rk)*depth                         ! :482  분자 (부력차)
Ribot = (Uref-Uk)²+(Vref-Vk)²+ Vtc*depth*ws*√|bvf|      ! :483-484  분모: resolved shear + ★unresolved turbulent shear(Vtc 항)
FC    = Ritop/(Ribot+eps)   [또는 SASHA: Ritop-lmd_Ric*Ribot]  ! :486-488
```
- **`Vtc` 항** (:249-250 정의, :484 사용) = LMD unresolved turbulent shear — bulk-Ri 분모의 핵심 (기존 노트 누락).
- **hsbl** = `Rib=Ric` 지점: 선형보간(:503-504) 또는 `QUADRATIC` Bill Large 이차보간(:515-531).

### 2.3 Ekman / Monin-Obukhov depth limiting (:581-591)
`hekman = lmd_cekman·Ustar/|f|`, `hmonob = lmd_cmonob·Ustar³/(vonKar·Bfsfc)`, `hsbl = MIN(hekman, hmonob, hsbl)`.

### 2.4 Nondimensional shape function G(σ) (:865-878)
```fortran
sigma = depth/(zbl+eps)
a1 = sigma-2 ; a2 = 3-2*sigma ; a3 = sigma-1        ! :869-871 cubic 계수
Gm = a1 + a2*Gm1 + a3*dGm1dS                         ! :875 (Gt,Gs 동형)
```
- **matching at BL base** (:748-780): `Gm1 = K_bl/(zbl·wm+eps)`(:753), `dGm1dS = MIN(0, -dK_bl/wm - K_bl·f1)`(:757) — interior `Akv/Akt`(:751-752) 를 BL 바닥에서 연속 접합.

### 2.5 BL diffusivity 조립 (:884-899)
```fortran
Akv = depth*wm*(1+sigma*Gm)          ! :894  (LMD_BOUND 시 MIN(lmd_nu0c, ...) 대류 상한 :885)
Akt = depth*ws*(1+sigma*Gt)
```

### 2.6 Nonlocal transport ghats (`LMD_NONLOCAL`, :319-324·900-919)
초기화(:319-324): `ghats(temp)=-cff·(stflx-srflx+srflx·(1-swdk))`, `ghats(salt)=cff·stflx`. 스케일(:904-905): `cff=lmd_Cg·(1-(0.5+SIGN(0.5,Bflux)))/(zbl·ws+eps)`. 안정/BL밖 = 0 (:917-919). → **비국소 counter-gradient flux**(불안정 대류 시 gradient 반대방향 수송) = KPP 의 정체성.

### 2.7 부력강제-태양복사 결합
`Bfsfc = Bo + Bosol·(1-swdk)`(:315,573), `Bosol=g·alpha·srflx`(:293), `swdk` = `lmd_swfrac` 호출(:312).

## 3. Bottom boundary layer (`lmd_bkpp.F`)
Surface 대칭 — `Ustar` from `bustr/bvstr`(:254-255), bulk-Ri/hbbl(:306-307,376-396), w-scale(:416+), Ekman 상한 `hekman`. **비대칭**: bottom 경로는 **Monin-Obukhov `hmonob` 없음**(Ekman만) — surface 와 물리적 차이.

## 4. Solar penetration (`lmd_swfrac.F`) — Jerlov 2-band
```fortran
swdk = EXP(Z*fac1)*fac3 + EXP(Z*fac2)*(1-fac3)   ! :80-81  두 지수 감쇠
Jwtype = 1-9 clamp                                 ! :73  Jerlov 수형
```
KPP 부력강제(`Bfsfc`·`Bflux`·온도 `ghats`)로 직접 결합. 위키 미커버 → 향후 확장 후보.

## 5. 검증 정정 (기존 [[roms_vertical_mixing]] 대상)
1. **`LMD_KPP` 플래그 오명** → `LMD_MIXING`+`LMD_SKPP`/`LMD_BKPP`.
2. **`lmd_wscale.F` 없음** → w-scale 인라인(:442-471).
3. **§E line 95 오분류**: `RI_HORAVG/RI_VERAVG/RI_SPLINES` 를 "stability functions/anisotropy" 로 묶었으나 실제 = `lmd_vmix.F:280-306` Ri 평활/재구성 옵션(stability function 무관).
4. **`Vtc` unresolved shear 항**(:484) — bulk-Ri 분모 핵심, 기존 누락.
5. **bottom BL 은 Monin-Obukhov 상한 없음**(surface 만) — 물리적 비대칭.

## 6. 관련
- [[roms_vertical_mixing]] — GLS/MY25/KPP 개괄 (본 노트가 KPP 심층 보완, §D 확장 대상)
- [[roms_baroclinic_3d]] — 연직 diffusivity Akv/Akt 소비처 (step3d_t/step3d_uv)
- `concepts/currents/04-code-and-tools.md` — 연직혼합 도메인 관점 (cross-model: MY2.5 [[efdc_turbulence]], GOTM)
- **Primary**: Large-McWilliams-Doney 1994 Rev Geophys 32:363-403 · Polzin 1996 JPO(shear magnitude) · Gargett-Holloway(internal wave).
