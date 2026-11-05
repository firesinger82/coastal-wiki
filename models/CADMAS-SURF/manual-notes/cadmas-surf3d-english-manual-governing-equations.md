---
title: "CADMAS-SURF/3D 영문 매뉴얼 — 지배방정식 발췌 (Table 0-1-1 기능목록 + §2.1-2.4 porous Navier-Stokes·VOF·Sommerfeld·k-ε)"
model: CADMAS-SURF
component: manual-notes
canonical_source: self
verification_method: "번들 영문 매뉴얼 CADMAS-SURF3D_Manural_English.pdf 직접 pdftotext 추출(150p). Table 0-1-1 Function list(printed p.318-319) + §2.2 식(2.1)-(2.5) porous Navier-Stokes(p.321-322) + Rx 저항식(p.322) + §VOF 식(2.7) donor-acceptor·NASA-VOF 3D(p.323-325) + Sommerfeld 식(2.16)·energy damping zone 식(2.17-2.19)(p.326-328) + k-ε 상수 Cμ=0.09·σk=1.0·σε=1.3·C1=1.44·C2=1.92·C3=0(p.330). printed page 직접 인용. 소스 source-analysis 와 cross-confirm. 2026-11-04 CADMAS-SURF recovery 대조 보고서 반영."
citation_status: verified
last_source_check: "2026-11-04 (recovery 대조 반영)"
has_source_needed: false
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-23
last_source_check: "2026-11-04 (recovery 대조 반영)"
related:
  - models/CADMAS-SURF/README.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-smac-velocity-pressure-solver.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-vof-free-surface.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-turbulence-and-porous-resistance.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-wave-generation-and-boundaries.md
source_scope: Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D
---

# CADMAS-SURF/3D 영문 매뉴얼 — 지배방정식 발췌

> 번들 영문 매뉴얼 `Simulators/CADMAS-SURF-3D/Manual/CADMAS-SURF3D_Manural_English.pdf`(150p) Ch2 Analytical model 발췌. [11-04 대조 정정]
> `3D manual p.N`은 PDF 쪽이다. [11-04 대조 정정]
> 기존 `p.N` 표기는 인쇄 쪽이다. [11-04 대조 정정]

매뉴얼의 지원식과 코드 구현의 대조 결과를 항목별로 기록한다. [11-04 대조 정정]
난류 부력 생성과 조파 스칼라 생성은 일치 목록에서 제외한다(3D manual p.17–19; `3D/vf_kgene.f:168`, `3D/vf_t1cal.f:90–91`, `3D/vf_s1cal.f:95–96`; [KS1-707 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS1.md)). [11-04 대조 정정]

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

## 2. §2.2 porous-model Navier-Stokes (3D manual p.10–11) [11-04 대조 정정]

> "the basic equations … include the continuous equation for 3D incompressible viscous fluid and the equation (2.1) obtained by extending the Navier-Stokes equations based on the **porous model**" (3D manual p.10) [11-04 대조 정정]

- **연속식 (2.1)**은 `∂(γxu)/∂x+∂(γyv)/∂y+∂(γzw)/∂z=γvSρ`다(3D manual p.10, 인쇄 p.322; `3D/vf_vpcoef.f:345–347`). [11-04 대조 정정]
- **운동량 (2.2)–(2.4)**의 시간항은 `λv∂u/∂t`다(3D manual p.10–11). [11-04 대조 정정]
- 점성항은 `γx/y/zνe`를 쓴다(3D manual p.10–11). [11-04 대조 정정]
- 소스는 `+γvSu`다(3D manual p.10–11). [11-04 대조 정정]
- γ는 공극률·면적 투과율이다(`3D/vf_a1main.f:67–74`). [11-04 대조 정정]
- 관성 가중값은 `λ=γ+(1−γ)CM`이다(`3D/vf_a1main.f:67–74`). [11-04 대조 정정]

**식 (2.5)**은 `λv=γv+(1−γv)CM`이다(3D manual p.11; `3D/vf_cglv.f:34`). [11-04 대조 정정]
각 방향은 `λx=γx+(1−γx)CM`의 형태다(3D manual p.11; `3D/vf_cglxyz.f:64–65`). [11-04 대조 정정]

**연속형 Rx**는 `1/2·(CD/Δx)·(1−γx)u√(u²+v²+w²)`다(3D manual p.11,31). [11-04 대조 정정]
x면 코드 저항에는 `XX(5,I)=1/δxi`가 포함된다(`3D/vf_vgene.f:103–110`). [11-04 대조 정정]
코드의 저항 대입 원문은 `&                    -0.5D0*CD*XX(5,I)*(1.0D0-GGX(I,J,K))*U*UVW`이다(`3D/vf_vgene.f:110`). [11-04 대조 정정]

## 3. VOF 자유수면 — 식(2.7) donor-acceptor (p.323-325)

**VOF 이류 면 계수**는 `γx/y/z`다(3D manual p.11,30,41–42; `3D/vf_fconv.f:60`). [11-04 대조 정정]
식 (2.7)·(3.37)과 식 (3.95)·QF 정의의 공극률 차이는 별도로 표시한다(`3D/vf_feuler.f:47–52`; [KS1-705 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS1.md)). [11-04 대조 정정]
> "To discretize the advection equation, a **donor-acceptor method** specially devised because the surface is not blurred is used. Further, a **method considering the inclination of the interface** can also be selected." (p.323-324)
> "VOF function F is a function to express the **free surface sharply, unlike the void fraction** used in two-phase flow analysis" (p.324)

→ source `vf_fconv.f:6`(donor-acceptor 헤더) + `vf_fconvs.f`(경사고려 PLIC) 와 일치. 표면방향은 **NASA-VOF 3D method**(Table 0-1-1) = `vf_fnfprv.f`. ([vof-free-surface §1·§7](../source-analysis/cadmas-surf3d-vof-free-surface.md#1-스킴-판정--donor-acceptor-hirt-nichols-plic-아님기본))

## 4. 무반사 경계 (p.326-328)

**(1) Sommerfeld 방사경계 식(2.16)** (p.326-327): "Radiation conditions of Sommerfeld … are adopted" → `∂f/∂t + C·∂f/∂n = 0`. → source `vf_bwuwn.f:483-619` `ALN=MIN(C·Δt/Δx,1)` blend 와 일치 ([wave-gen §B-1](../source-analysis/cadmas-surf3d-wave-generation-and-boundaries.md#b-1-방사개경계--sommerfeld형-vf_bwuwnf483-619)).

**(2) Energy damping zone 식 (2.17)–(2.19)**의 감쇠계수 원문은 `\theta_{xy}\sqrt{g/h}(N+1)[\max(\lvert x-x_0\rvert,\lvert y-y_0\rvert)/l]^N`이다(3D manual p.15–16; [KS1-706 수정안](../../../_staging/recovery/compare/cadmas-3d-manual-theory-vs-code.md)). [11-04 대조 정정]
감쇠계수의 `(N+1)`은 거듭제곱 밖에 있다(3D manual p.15–16). [11-04 대조 정정]
거리에는 절댓값을 쓴다(3D manual p.15–16). [11-04 대조 정정]
구현 근거는 `3D/vf_veuler.f:81–84,135–165`이다. [11-04 대조 정정]

## 5. k-ε 高Re 난류 — 상수 (p.328-330)

> "high Re type k-ε 2 equation model … defines turbulence energy k and turbulent energy dissipation ε … advection diffusion equation" (p.328)
> **상수** (p.330): "generally **C_μ=0.09, σk=1.00, σε=1.30, C₁=1.44, C₂=1.92, C₃=0.0** are adopted"

→ **source 디폴트 `vf_a2dflt.f:169-174` 와 정확히 일치** (표준 Launder-Spalding). 渦점성 νₜ=Cμk²/ε = `vf_cnut0.f:47`. 난류효과는 운동량식 점성항의 유효점성계수 νₑ=ν+νₜ 로 반영(p.330+ = `vf_cnu00.f:57`).

---

## 매뉴얼 ↔ 소스 대조 요약 [11-04 대조 정정]

| 식 | 매뉴얼 | 소스 | 대조 결과 [11-04 대조 정정] |
|---|---|---|---|
| 가상질량 (2.5) | 3D manual p.11 `λv=γv+(1−γv)CM` | `3D/vf_cglv.f:34` | 관성 가중값 [11-04 대조 정정] |
| porous 저항 Rx | 3D manual p.11,31 `1/2·(CD/Δx)·(1−γx)u√(u²+v²+w²)` | `3D/vf_vgene.f:110` | 코드에 `XX(5,I)=1/δxi` 포함 [11-04 대조 정정] |
| VOF 이류 (2.7) | 3D manual p.11,30,41–42 `γx/y/z` | `3D/vf_fconv.f:60`, `3D/vf_feuler.f:47–52` | QF 공극률 차이는 본문 참조 [11-04 대조 정정] |
| Sommerfeld (2.16) | p.327 ∂f/∂t+C∂f/∂n=0 | `vf_bwuwn.f:513` | ✅ |
| k-ε 상수 | p.330 0.09/1.0/1.3/1.44/1.92 | `vf_a2dflt.f:169-173` | ✅ |
| SMAC + Euler | p.318 | `vf_a1main.f:7` | ✅ |
| MILU-BiCGSTAB | p.319 | `vf_m1bcgs.f:9` | ✅ |

문서와 코드 차이 표는 [cadmas-surf3d-manual-differences.md](cadmas-surf3d-manual-differences.md)에 있다.

프로그램 구조의 대조 범위는 3D manual p.58–100이다([KS2-816 수정안](../../../_staging/recovery/compare/cadmas-3d-manual-program-vs-code.md)). [11-04 대조 정정]

## Chapter 5 입력·출력 대조

농도 성분 번호 LC는 I*4이다(3D manual p.108,111; `3D/vf_iimate.f:74–77`; [KS3-046 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS3.md)). [11-04 대조 정정]
공급 3D 코드의 PORO 공극률 레코드는 R*8을 요구한다(3D manual p.135,145; `3D/vf_ip1inp.f:10,21–24,81–94`; [KS3-251 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS3.md)). [11-04 대조 정정]
`!VD!`·`!B!`·`!R!`는 제곱합의 제곱근인 2-노름이다(3D manual p.140; `3D/vf_cdiv00.f:37–56`, `3D/vf_m1bcgs.f:249–250`; [KS3-234 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS3.md)). [11-04 대조 정정]

> 참고문헌(매뉴얼): porous model = ref 2), high-Re k-ε = ref 9), 정전 = CDIT(2001) "Research and development of numerical wave channel" CDIT Library. 일문 매뉴얼 `CADMAS-SURF3D_Manual_Japanese.pdf`·STOC 결합 `STOC-CADMAS_Manual_Japanese.pdf` 동봉.

## 문서와 코드 차이 (11-04 대조)

비교한 판: 코드는 github.com/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami `da7668f`(2024-08-30, 커밋 1개)의 Simulators/이며, 문서는 CADMAS-SURF3D_Manural_English이다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| 3d-theory:KS1-701 | 05fdbedb:models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:53; `3D/vf_vpcoef.f:345–347`; `3D manual p.10` (인쇄 p.322)<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS1.md) · [보고서](../../../_staging/recovery/compare/cadmas-3d-manual-theory-vs-code.md) | ``- **연속식 (2.1)**: `∂(λₓu)/∂x + ∂(λ_yv)/∂y + ∂(λ_zw)/∂z = γᵥSₚ` — 면적투과율 λ 가중 (p.321)`` | `3D/vf_vpcoef.f:345–347` `VD= AYZ*(GGX(IP,J,K)*UU(IP,J,K)-GGX(I,J,K)*UU(I,J,K))`<br>`&           +AXZ*(GGY(I,JP,K)*VV(I,JP,K)-GGY(I,J,K)*VV(I,J,K))`<br>`&           +AXY*(GGZ(I,J,KP)*WW(I,J,KP)-GGZ(I,J,K)*WW(I,J,K))` | B 문서 오기 | 연속식 (2.1)은 `∂(γxu)/∂x+∂(γyv)/∂y+∂(γzw)/∂z=γvSρ`다. 출처는 `3D manual p.10` (인쇄 p.322)다. |
| 3d-theory:KS1-702 | 05fdbedb:models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:54–55; `3D/vf_a1main.f:67–74`; `3D/vf_vgene.f:149–151`; `3D manual p.10–11`<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS1.md) · [보고서](../../../_staging/recovery/compare/cadmas-3d-manual-theory-vs-code.md) | `- **운동량 (2.2)-(2.4)**: γᵥ ∂u/∂t + 이류 = −(γᵥ/ρ)∂p/∂x + 점성(λ·νₑ) + **−γᵥDₓu − Rₓ − γᵥSᵤ** (p.321-322)`<br>`- 기호(p.322): νₑ=분자동점성ν+渦점성νₜ 합, γᵥ=공극률, λₓ/λ_y/λ_z=x/y/z 면적투과율, Dₓ=energy damping zone 계수, Sᵤ=造波 source, Rₓ=porous body 저항` | `3D/vf_a1main.f:67–74` `CD    GGV(@FOR-3D@)     : R*8 : 空隙率`<br>`CD    GGX(@FOR-3D@)     : R*8 : x方向面積透過率`<br>`CD    GGY(@FOR-3D@)     : R*8 : y方向面積透過率`<br>`CD    GGZ(@FOR-3D@)     : R*8 : z方向面積透過率`<br>`CD    GLV(@FOR-3D@)     : R*8 : =GGV+(1-GGV)*CM`<br>`CD    GLX(@FOR-3D@)     : R*8 : =GGX+(1-GGX)*CM`<br>`CD    GLY(@FOR-3D@)     : R*8 : =GGY+(1-GGY)*CM`<br>`CD    GLZ(@FOR-3D@)     : R*8 : =GGZ+(1-GGZ)*CM`<br>`3D/vf_vgene.f:149–151` `IF (IWS.EQ.I .OR. IWS+1.EQ.I) THEN`<br>`Q=2.0D0*XX(4,IWS)*SRCUV(J,K)`<br>`QU(I,J,K)=QU(I,J,K)+UU(I,J,K)*Q*XX(2,IWS)*XX(5,I)*0.5D0` | B 문서 오기 | 운동량 시간항은 `λv∂u/∂t`다. 점성항은 `γx/y/zνe`를 쓴다. 소스는 `+γvSu`다. γ는 공극률·면적 투과율이다. `λ=γ+(1−γ)CM`이다. |
| 3d-theory:KS1-703 | 05fdbedb:models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:59–61; `3D/vf_cglv.f:34`; `3D/vf_cglxyz.f:64–65`; `3D manual p.11`<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS1.md) · [보고서](../../../_staging/recovery/compare/cadmas-3d-manual-theory-vs-code.md) | `γᵥ = γᵥ + (1−γᵥ)Cₘ ,  λₓ = λₓ + (1−λₓ)Cₘ  (λ_y, λ_z 동형)`<br>``→ **소스 `vf_cglv.f:34` `GLV=GGV+(1-GGV)*CM0` 와 정확히 일치** ([turbulence §B-2](../source-analysis/cadmas-surf3d-turbulence-and-porous-resistance.md#b-2-가상질량-관성cm--명시적-力이-아니라-운동량-시간미분항을-곱하는-유효-공극-glv-로-folding)).`` | `3D/vf_cglv.f:34` `GLV(I,J,K)=GGV(I,J,K)+(1.0D0-GGV(I,J,K))*CM0(I,J,K)`<br>`3D/vf_cglxyz.f:64–65` `CM=XX(6,I)*(XX(2,I)*CM0(I,J,K)+XX(2,I-1)*CM0(I-1,J,K))`<br>`GLX(I,J,K)=GGX(I,J,K)+(1.0D0-GGX(I,J,K))*CM` | B 문서 오기 | 식 (2.5)은 `λv=γv+(1−γv)CM`이다. 각 방향은 `λx=γx+(1−γx)CM`의 형태다. |
| 3d-theory:KS1-704 | 05fdbedb:models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:65–67; `3D/vf_vgene.f:103–110`; `3D manual p.11,31`<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS1.md) · [보고서](../../../_staging/recovery/compare/cadmas-3d-manual-theory-vs-code.md) | `Rₓ = ½·(Cᴅ/λₓ)·(1−λₓ)·u·√(u²+v²+w²)   (R_y, R_z 동형)`<br>``→ **소스 `vf_vgene.f:110` `−0.5*CD*(1-GGX)*U*UVW` 와 일치**(½Cᴅ(1−λ)u\|u\| 구조), `\|u\|=√(u²+v²+w²)` `vf_vgene.f:108`.`` | `3D/vf_vgene.f:103–110` `U=UU(I,J,K)`<br>`V=XX(6,I)*( XX(2,I1)*(VV(I ,J,K)+VV(I ,J+1,K))`<br>`&                     +XX(2,I )*(VV(I1,J,K)+VV(I1,J+1,K)))*0.5D0`<br>`W=XX(6,I)*( XX(2,I1)*(WW(I ,J,K)+WW(I ,J,K+1))`<br>`&                     +XX(2,I )*(WW(I1,J,K)+WW(I1,J,K+1)))*0.5D0`<br>`UVW=SQRT(U*U+V*V+W*W)`<br>`QU(I,J,K)=QU(I,J,K)`<br>`&                    -0.5D0*CD*XX(5,I)*(1.0D0-GGX(I,J,K))*U*UVW` | B 문서 오기 | 연속형 Rx는 `1/2·(CD/Δx)·(1−γx)u√(u²+v²+w²)`다. x면 코드 저항에는 `XX(5,I)=1/δxi`가 포함된다. |
| 3d-theory:KS1-705 | 05fdbedb:models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:71; `3D/vf_fconv.f:60`; `3D/vf_feuler.f:47–52`; `3D manual p.11,30,41–42`<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS1.md) · [보고서](../../../_staging/recovery/compare/cadmas-3d-manual-theory-vs-code.md) | ``> "The advection equation of the VOF function F based on the porous model" **식(2.7)**: `γᵥ ∂F/∂t + ∂(λₓuF)/∂x + ∂(λ_yvF)/∂y + ∂(λ_zwF)/∂z = γᵥSF` (p.323)`` | `3D/vf_fconv.f:60` `C=DTNOW*GGX(I,J,K)*UU(I,J,K)`<br>`3D/vf_feuler.f:47–52` `G0=GGV(I,J,K)-(GGV(I,J,K)-GGV0(I,J,K))*DBLE(LOOPS)`<br>`DF=( XX(4,I)*(FLFU(I+1,J,K)-FLFU(I,J,K))`<br>`&            +YY(4,J)*(FLFV(I,J+1,K)-FLFV(I,J,K))`<br>`&            +ZZ(4,K)*(FLFW(I,J,K+1)-FLFW(I,J,K))`<br>`&            +DTNOW*QF(I,J,K)                    )`<br>`FF(I,J,K)=(G0*FF(I,J,K)+DF)/GGV(I,J,K)` | B 문서 오기 | VOF 이류 면 계수는 γx/y/z다. 식 (2.7)·(3.37)과 식 (3.95)·QF 정의의 공극률 차이는 별도로 표시한다. |
| 3d-theory:KS1-706 | 05fdbedb:models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:81; `3D/vf_veuler.f:81–84,135–165`; `3D manual p.15–16`<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS1.md) · [보고서](../../../_staging/recovery/compare/cadmas-3d-manual-theory-vs-code.md) | ``**(2) Energy damping zone 식(2.17)-(2.19)** (p.327-328): 파에너지를 1~3 파장 영역에서 점감. 감쇠항 `−Dₓu` 가 식(2.2)-(2.4)에 추가, `Dₓ = αₓᵧ·√(g/h)·((N-1)·max(x-x₀,y-y₀)/l)^N` (p.328). h=수심, l·x₀=damping zone 폭·시점. → source `vf_vgene.f` Dx/Dy/Dz damping 계수.`` | `3D/vf_veuler.f:81–84` `D  =SQRT(GRZ0/DAMP(4,1))`<br>`W1 =DAMP(3,1)`<br>`PX1=DBLE(IP1+1)*DAMP(1,1)*D`<br>`PZ1=DBLE(IP1+1)*DAMP(2,1)*D`<br>`3D/vf_veuler.f:135–165` `IF (IP1.GE.0) THEN`<br>`D=X-XMIN`<br>`IF (D.LE.W1) THEN`<br>`D=PX1*(1.0D0-D/W1)**IP1`<br>`IF (D.GT.DMAX) DMAX=D`<br>`ENDIF`<br>`ENDIF`<br>`IF (IP2.GE.0) THEN`<br>`D=XMAX-X`<br>`IF (D.LE.W2) THEN`<br>`D=PX2*(1.0D0-D/W2)**IP2`<br>`IF (D.GT.DMAX) DMAX=D`<br>`ENDIF`<br>`ENDIF`<br>`IF (IP3.GE.0) THEN`<br>`D=Y-YMIN`<br>`IF (D.LE.W3) THEN`<br>`D=PX3*(1.0D0-D/W3)**IP3`<br>`IF (D.GT.DMAX) DMAX=D`<br>`ENDIF`<br>`ENDIF`<br>`IF (IP4.GE.0) THEN`<br>`D=YMAX-Y`<br>`IF (D.LE.W4) THEN`<br>`D=PX4*(1.0D0-D/W4)**IP4`<br>`IF (D.GT.DMAX) DMAX=D`<br>`ENDIF`<br>`ENDIF`<br>`G=XX(6,I)*(XX(2,I)*GGV(I,J,K)+XX(2,I-1)*GGV(I-1,J,K))`<br>`D=GV0/(GV0+DTNOW*G*DMAX)`<br>`UU(I,J,K)=UU(I,J,K)*D` | B 문서 오기 | 감쇠계수의 `(N+1)`은 거듭제곱 밖에 있다. 거리에는 절댓값을 쓴다. 구현 근거는 vf_veuler.f다. |
| 3d-theory:KS1-707 | 05fdbedb:models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:23; `3D/vf_kgene.f:168`; `3D/vf_t1cal.f:90–91`; `3D/vf_s1cal.f:95–96`; `3D manual p.17–19`<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS1.md) · [보고서](../../../_staging/recovery/compare/cadmas-3d-manual-theory-vs-code.md) | ``> 번들 영문 매뉴얼 `Simulators/CADMAS-SURF-3D/Manual/CADMAS-SURF3D_Manural_English.pdf`(150p) Ch2 Analytical model 발췌. 인용은 PDF 내 **인쇄 페이지 번호**(p.318~). 본 매뉴얼이 [source-analysis](../source-analysis/cadmas-surf3d-architecture-source-map.md) 의 코드 발견을 식 단위로 확증 — 각 항목에 source 대조 표기.`` | `3D/vf_kgene.f:168` `GT =0.0D0`<br>`3D/vf_t1cal.f:90–91` `CD    -- 生成消滅項の計算 --`<br>`CAKIY CALL VF_TGENE`<br>`3D/vf_s1cal.f:95–96` `CD      -- 生成消滅項の計算 --`<br>`CAKIY   CALL VF_SGENE` | C 문서 누락 | 매뉴얼의 지원식과 코드 구현의 대조 결과를 항목별로 기록한다. 난류 부력 생성과 조파 스칼라 생성은 일치 목록에서 제외한다. |
