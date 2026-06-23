---
title: "CADMAS-SURF/3D 영문 매뉴얼 — 지배방정식 발췌 (Table 0-1-1 기능목록 + §2.1-2.4 porous Navier-Stokes·VOF·Sommerfeld·k-ε)"
model: CADMAS-SURF
component: manual-notes
canonical_source: self
verification_method: "번들 영문 매뉴얼 CADMAS-SURF3D_Manural_English.pdf 직접 pdftotext 추출(150p). Table 0-1-1 Function list(printed p.318-319) + §2.2 식(2.1)-(2.5) porous Navier-Stokes(p.321-322) + Rx 저항식(p.322) + §VOF 식(2.7) donor-acceptor·NASA-VOF 3D(p.323-325) + Sommerfeld 식(2.16)·energy damping zone 식(2.17-2.19)(p.326-328) + k-ε 상수 Cμ=0.09·σk=1.0·σε=1.3·C1=1.44·C2=1.92·C3=0(p.330). printed page 직접 인용. 소스 source-analysis 와 cross-confirm."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-23
related:
  - models/CADMAS-SURF/README.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-smac-velocity-pressure-solver.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-vof-free-surface.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-turbulence-and-porous-resistance.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-wave-generation-and-boundaries.md
---

# CADMAS-SURF/3D 영문 매뉴얼 — 지배방정식 발췌

> 번들 영문 매뉴얼 `Simulators/CADMAS-SURF-3D/Manual/CADMAS-SURF3D_Manural_English.pdf`(150p) Ch2 Analytical model 발췌. 인용은 PDF 내 **인쇄 페이지 번호**(p.318~). 본 매뉴얼이 [source-analysis](../source-analysis/cadmas-surf3d-architecture-source-map.md) 의 코드 발견을 식 단위로 확증 — 각 항목에 source 대조 표기.

## 1. Table 0-1-1 Function list — 물리모델 요약 (p.318-319)

매뉴얼이 모델 전체를 한 표로 권위있게 정의:

| 항목 | 매뉴얼 기술 (p.318) | source 대조 |
|---|---|---|
| Target to analyze | Complex flow with free surface | `vf_a1main.f:6` |
| **Basic equations** | **porous model 기반 3D 비압축 점성유체 Navier-Stokes + 연속식** | §2 below |
| Coordinate | Cartesian | `vf_a1main.f:8` |
| Free surface | **VOF method** | [vof-free-surface](../source-analysis/cadmas-surf3d-vof-free-surface.md) |
| Turbulence | **High Reynolds number k-ε** | [turbulence §A](../source-analysis/cadmas-surf3d-turbulence-and-porous-resistance.md#a-k-ε-2방정식-난류-모델) |
| Wave model | **Waveform boundary + Wave source** | [wave-gen §A](../source-analysis/cadmas-surf3d-wave-generation-and-boundaries.md#a-조파-造波--두-메커니즘) |
| Waveform function | **Stokes 5th / Cnoidal(Knoid) 3rd / flow-function method B / Matrix data** | `vf_cwmak0.f:17-20` |
| Nonreflective | **Sommerfeld radiation boundary + Energy damping zone** | `vf_bwuwn.f:482` |
| Scalar | Energy eq + multicomponent concentration transport | `vf_t1cal`·`vf_s1cal` |
| Discretization | **staggered mesh 차분 + porous model 형상근사** | [architecture](../source-analysis/cadmas-surf3d-architecture-source-map.md) |
| Time integration | **Euler method + SMAC method** | `vf_a1main.f:7` |
| Advection (non-VOF) | 1차 풍상 / 2차 중심 / **DONOR(①②hybrid)** 선택 | `vf_vflxdu.f:8` |
| VOF advection | **Donor·Acceptor / 경사고려법** 선택 | `vf_fconv.f:6` |
| Surface direction | **NASA-VOF 3D method 채용** | `vf_fnfprv.f` |
| Bubble/water drop | **TimerDoor method** | `vf_fbubup.f:5`·`vf_fdropf.f:7` |
| Linear solver | **MILU-BiCGSTAB method** | `vf_m1bcgs.f:9` |
| Time step | 고정입력 / 자동 | `vf_cdtcal.f` |

## 2. §2.2 porous-model Navier-Stokes (p.321-322)

> "the basic equations … include the continuous equation for 3D incompressible viscous fluid and the equation (2.1) obtained by extending the Navier-Stokes equations based on the **porous model**" (p.321)

- **연속식 (2.1)**: `∂(λₓu)/∂x + ∂(λ_yv)/∂y + ∂(λ_zw)/∂z = γᵥSₚ` — 면적투과율 λ 가중 (p.321)
- **운동량 (2.2)-(2.4)**: γᵥ ∂u/∂t + 이류 = −(γᵥ/ρ)∂p/∂x + 점성(λ·νₑ) + **−γᵥDₓu − Rₓ − γᵥSᵤ** (p.321-322)
- 기호(p.322): νₑ=분자동점성ν+渦점성νₜ 합, γᵥ=공극률, λₓ/λ_y/λ_z=x/y/z 면적투과율, Dₓ=energy damping zone 계수, Sᵤ=造波 source, Rₓ=porous body 저항

**Eq(2.5) 가상질량 관성** (p.322):
```
γᵥ = γᵥ + (1−γᵥ)Cₘ ,  λₓ = λₓ + (1−λₓ)Cₘ  (λ_y, λ_z 동형)
```
→ **소스 `vf_cglv.f:34` `GLV=GGV+(1-GGV)*CM0` 와 정확히 일치** ([turbulence §B-2](../source-analysis/cadmas-surf3d-turbulence-and-porous-resistance.md#b-2-가상질량-관성cm--명시적-力이-아니라-운동량-시간미분항을-곱하는-유효-공극-glv-로-folding)).

**porous body 저항 Rₓ** (p.322) — 유속 제곱 비례(Cᴅ=저항계수):
```
Rₓ = ½·(Cᴅ/λₓ)·(1−λₓ)·u·√(u²+v²+w²)   (R_y, R_z 동형)
```
→ **소스 `vf_vgene.f:110` `−0.5*CD*(1-GGX)*U*UVW` 와 일치**(½Cᴅ(1−λ)u|u| 구조), `|u|=√(u²+v²+w²)` `vf_vgene.f:108`.

## 3. VOF 자유수면 — 식(2.7) donor-acceptor (p.323-325)

> "The advection equation of the VOF function F based on the porous model" **식(2.7)**: `γᵥ ∂F/∂t + ∂(λₓuF)/∂x + ∂(λ_yvF)/∂y + ∂(λ_zwF)/∂z = γᵥSF` (p.323)
> "To discretize the advection equation, a **donor-acceptor method** specially devised because the surface is not blurred is used. Further, a **method considering the inclination of the interface** can also be selected." (p.323-324)
> "VOF function F is a function to express the **free surface sharply, unlike the void fraction** used in two-phase flow analysis" (p.324)

→ source `vf_fconv.f:6`(donor-acceptor 헤더) + `vf_fconvs.f`(경사고려 PLIC) 와 일치. 표면방향은 **NASA-VOF 3D method**(Table 0-1-1) = `vf_fnfprv.f`. ([vof-free-surface §1·§7](../source-analysis/cadmas-surf3d-vof-free-surface.md#1-스킴-판정--donor-acceptor-hirt-nichols-plic-아님기본))

## 4. 무반사 경계 (p.326-328)

**(1) Sommerfeld 방사경계 식(2.16)** (p.326-327): "Radiation conditions of Sommerfeld … are adopted" → `∂f/∂t + C·∂f/∂n = 0`. → source `vf_bwuwn.f:483-619` `ALN=MIN(C·Δt/Δx,1)` blend 와 일치 ([wave-gen §B-1](../source-analysis/cadmas-surf3d-wave-generation-and-boundaries.md#b-1-방사개경계--sommerfeld형-vf_bwuwnf483-619)).

**(2) Energy damping zone 식(2.17)-(2.19)** (p.327-328): 파에너지를 1~3 파장 영역에서 점감. 감쇠항 `−Dₓu` 가 식(2.2)-(2.4)에 추가, `Dₓ = αₓᵧ·√(g/h)·((N-1)·max(x-x₀,y-y₀)/l)^N` (p.328). h=수심, l·x₀=damping zone 폭·시점. → source `vf_vgene.f` Dx/Dy/Dz damping 계수.

## 5. k-ε 高Re 난류 — 상수 (p.328-330)

> "high Re type k-ε 2 equation model … defines turbulence energy k and turbulent energy dissipation ε … advection diffusion equation" (p.328)
> **상수** (p.330): "generally **C_μ=0.09, σk=1.00, σε=1.30, C₁=1.44, C₂=1.92, C₃=0.0** are adopted"

→ **source 디폴트 `vf_a2dflt.f:169-174` 와 정확히 일치** (표준 Launder-Spalding). 渦점성 νₜ=Cμk²/ε = `vf_cnut0.f:47`. 난류효과는 운동량식 점성항의 유효점성계수 νₑ=ν+νₜ 로 반영(p.330+ = `vf_cnu00.f:57`).

---

## 매뉴얼 ↔ 소스 일치 요약

| 식 | 매뉴얼 | 소스 | 일치 |
|---|---|---|---|
| 가상질량 (2.5) | p.322 γᵥ+(1−γᵥ)Cₘ | `vf_cglv.f:34` | ✅ |
| porous 저항 Rₓ | p.322 ½(Cᴅ/λ)(1−λ)u\|u\| | `vf_vgene.f:110` | ✅ |
| VOF 이류 (2.7) | p.323 donor-acceptor | `vf_fconv.f:6` | ✅ |
| Sommerfeld (2.16) | p.327 ∂f/∂t+C∂f/∂n=0 | `vf_bwuwn.f:513` | ✅ |
| k-ε 상수 | p.330 0.09/1.0/1.3/1.44/1.92 | `vf_a2dflt.f:169-173` | ✅ |
| SMAC + Euler | p.318 | `vf_a1main.f:7` | ✅ |
| MILU-BiCGSTAB | p.319 | `vf_m1bcgs.f:9` | ✅ |

> 참고문헌(매뉴얼): porous model = ref 2), high-Re k-ε = ref 9), 정전 = CDIT(2001) "Research and development of numerical wave channel" CDIT Library. 일문 매뉴얼 `CADMAS-SURF3D_Manual_Japanese.pdf`·STOC 결합 `STOC-CADMAS_Manual_Japanese.pdf` 동봉.
