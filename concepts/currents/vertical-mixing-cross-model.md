---
title: "연직혼합·난류종결(vertical mixing / turbulence closure) cross-model 대조 — 5개 3D 모델 (스킴·안정함수·배경하한·경계조건)"
topic: currents
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "전 행이 각 모델 verified source-analysis 노트로 소급(셀에 노트 링크+file:line). 대표 anchor 직접 재확인(2026-07-07): EFDC calavb.f90:45(SFAV0=0.392010)·SWASH SwashKepsMod1DH.ftn90:84-89(ceps1 1.44/ceps2 1.92/cmu 0.09/sigmak 1.0/sigmae 1.3/sigrho 0.5)·Delft3D turclo.f90:350-359(algebraic fl=exp(-2.3Ri)·fs 감쇠함수). 미커버 셀은 §5 disclosed."
note_author: "Claude Fable 5"
note_date: 2026-07-07
related:
  - models/ROMS/source-analysis/roms_vertical_mixing.md
  - models/ROMS/source-analysis/roms_kpp_boundary_layer.md
  - models/EFDC/source-analysis/efdc_turbulence.md
  - models/Delft3D/source-analysis/delft3d_turbulence.md
  - models/SWASH/source-analysis/swash-turbulence-closure.md
  - models/ADCIRC/source-analysis/adcirc-3d-mode.md
---

# 연직혼합·난류종결 cross-model 대조 (5모델)

> **Canonical source 규칙**: 각 모델 상세는 source-analysis 노트가 진실의 원천 — 본 노트는 대조 축만. cross-model 시리즈 4탄(EOS·스칼라 transport·[[bottom-friction-cross-model]] 후속).
> **범위**: 연직 eddy viscosity/diffusivity 를 예후·진단하는 3D(다층) 모델만 — ROMS·Delft3D·EFDC·SWASH·ADCIRC(3D 모드). 2DH 모델(SFINCS·LISFLOOD-FP·FUNWAVE·Celeris·XBeach 2DH·SWAN)은 연직혼합 자체가 없음(수평 점성·breaking 별도 축).

## 1. 종결 스킴·핵심 구조 대조

| 모델 | 스킴 선택지(기본) | 예후변수 | 안정함수 | 배경 하한·상한 | 근거 |
|---|---|---|---|---|---|
| **ROMS** | GLS(k-ε/k-ω/k-kl/generic 단일솔버) / MY2.5 / **KPP(진단)** — 컴파일 상호배타(cppdefs.h:233-240) | GLS `tke`+`gls`(ψ), MY `tke`+`q²l` | GLS: Canuto A/B·Kantha-Clayson·Galperin(gls_corstep.F:1084-1126); MY: Galperin/KC(my25_corstep.F:716-730) | KPP interior 내부파 `lmd_iwm=1e-6/√bvf`(운동량, tracer 는 1e-7 — 10× 비대칭) | [[roms_vertical_mixing]]·[[roms_kpp_boundary_layer]] |
| **Delft3D-FLOW** | `Tkemod`: **algebraic(기본)**/k-l/k-ε/constant(turclo.f90:190-199, dimrd.f90:439-464) | k(`RTUR1`)+ε(`RTUR2`) | algebraic 만 Ri 감쇠 `fl=exp(−2.3Ri)`·`fs=(1+3.33Ri)^{1.5}/(1+10Ri)^{0.5}`(turclo.f90:350-359 직접 확인); k-ε는 `ν=c_μk²/ε` 고정 | `vicoww/dicoww`(1e-6~1e-5 관례) floor 강제(redvic.f90:68-77)·초기 k/ε 1e-7·cap 10 m²/s(turclo.f90:512-517) | [[delft3d_turbulence]] |
| **EFDC+** | **MY2.5+Galperin(기본)** / `ISTOPT(0)=2` KC1994 / `=3` Kantha2003 / `ISGOTM>0` GOTM(k-ε 등) | `QQ`(q²)+`QQL`(q²l) | `SFAV=0.392010·(1+7.76Ri)/…` Galperin 계열 유리함수(calavb.f90:45,153-156 — SFAV0 직접 확인) | `AVO/ABO`(card C12, ~1e-5 관례) + cap `AVMX`(~0.5) ×HPI(calavb.f90:273-276) | [[efdc_turbulence]] |
| **SWASH** | 표준 k-ε(`iturb=1`, `VISC V KEPS`) / full 3D k-ε 선형(`=2`, `VISC FULL KEPS LIN`) / +Speziale 비선형(`=3`, `NONL`) — SwashReadInput.ftn90:1252-1276 | k+ε(`rtur`) | 없음(C_μ=0.09 고정) — 상수 1.44/1.92/0.09/1.0/1.3/0.5(SwashKepsMod1DH.ftn90:84-89 직접 확인) | `bvisc` floor+분자점성 가산+cap 10(SwashVertVisc.ftn90:78-86); ★비선형(iturb=3)은 floor/cap 생략 | [[swash-turbulence-closure]] |
| **ADCIRC(3D)** | `IEVC` 경험식 5종(상수·ωH²·κu*z 등) / **MY2.5 quasi-eq**(`IEVC=50/51`, vsmy.F:2035,2403) — 2방정식은 MY뿐 | q²+q²l | MY2.5 Sm(수치 미커버) | `EVMin`(수치 미커버) | [[adcirc-3d-mode]] |

## 2. 계보 — 세 갈래

1. **Mellor-Yamada q²-q²l 계열**: EFDC(기본)·ADCIRC 3D(유일 2-eq)·ROMS MY25(레거시) — 1980년대 해양모델 표준의 잔존. 안정함수만 세대교체(Galperin 1988 → Kantha-Clayson 1994 → Kantha 2003 → Canuto 2001).
2. **k-ε/GLS 계열**: Delft3D(k-ε)·SWASH(표준 k-ε)·ROMS GLS(Umlauf-Burchard 2003 일반화)·EFDC GOTM 연동 — GLS 는 `(p,m,n)` 지수로 k-ε/k-ω/k-kl 을 한 솔버에서 전환. **GOTM/GLS 프레임워크가 사실상 공통 참조점**(EFDC ISGOTM·ROMS GLS 모두 Umlauf-Burchard 계보).
3. **진단(비예후) KPP**: ROMS 전용(LMD) — TKE 방정식 없이 bulk-Ri 로 혼합층 깊이 진단 + shape function + **비국소(counter-gradient) 플럭스 ghats**. 5모델 중 비국소 수송은 KPP 만.

## 3. 경계조건 대조 (표면 파랑 주입이 최대 분기)

| 모델 | 표면 | 저면 | 파랑 TKE 주입 |
|---|---|---|---|
| ROMS GLS | Dirichlet + **Charnok/Craig-Banner 옵션**(파랑 dissipation 주입) | log-wall | **있음** — 강풍 시 Charnok 미사용하면 표면 TKE 과소(노트 명시) |
| Delft3D | 풍응력 기반 `tkewin`(tratur.f90:942-955) | log-wall `k=U²/(s²√c_μ)`(:978-991), 조도 선택 연동 | 없음(풍 경로만) |
| EFDC | `q²=B₁^{2/3}·|τ_s|`(hdmt2t.f90:875-889) | `q²=B₁^{2/3}·|τ_b|` — 파랑은 wave-current 저면응력 경로(:939-964) | 표면 주입 없음(저면 응력 경유만) |
| SWASH | k Neumann + ε Dirichlet(:748-772) | Dirichlet `k=u*²/√c_μ` 또는 log-law 직접해(`irough=4`, :801-816) | k-ε 주입 없음 — ★breaking 소산은 **수평** HorzVisc(`ihvisc=4`) 경로(위상해상이라 애초 별도) |
| ADCIRC | 미커버 | 3D BBL 응력(2D Manning 아님 — pitfall) | 없음 |

## 4. 수치 처리 공통점

전 모델이 연직확산·소산을 **implicit(tridiagonal)** 처리(소산 Newton 선형화: Delft3D tratur:904-924·SWASH :503-632·EFDC 대각 :353-355), 생산은 explicit — wet-dry·성층에서의 stiffness 대응이 공통 설계. 예외: ROMS KPP(방정식 자체가 없음), ADCIRC 는 운동량 연직확산이 **복소 tridiagonal** 로 확인(2026-07-12 갱신, [[adcirc-3d-vssol-vertical-scheme]] — MY2.5 q² 방정식 자체의 처리는 TURB 내부 미커버).

## 5. ★함정·미커버 (disclosed gaps)

- **ROMS**: closure 3종 컴파일 상호배타 — 플래그 혼용 시 무음 오선택 위험. `tke/gls` prognostic → **restart 파일 필수**(cold-start 특이 소산). ★`LMD_KPP` 플래그는 존재하지 않음(`LMD_MIXING`+`SKPP/BKPP`가 실제). bottom KPP 는 Monin-Obukhov 상한 없음(표면과 비대칭).
- **Delft3D**: 키워드는 `Tkemod`(★`TKEDIS` 아님 — tkedis 는 내부파 소산 배열). `Algebraic`(기본)은 균일혼합이 아니라 Ri-감쇠 혼합길이(균일은 `Constant`). 스칼라 쪽 내부파 혼합 `difiwe=0.2√bruvai·xlo²` 는 transport 커널 별도 항. ~~Z-model(z_turclo/z_tratur) 상세 미커버~~ — **해소(2026-07-12, 소스 대조)**: σ판과 동일 closure(ltur 0/1/2)·동일 Ri-감쇠 상수(`exp(−2.3Ri)`·`1+3.33Ri`, z_turclo.f90:398-399,454,538-539 = turclo.f90:350-359), 차이는 Z-layer 인덱싱뿐([[delft3d_turbulence]] 갱신).
- **EFDC**: 이론 Table 2.1 은 4옵션(MY1982 원본 포함)이나 **코드는 3옵션 — MY1982 원 상수 선택 불가**(calavb 분기 2/3만). `AV/AB`는 depth-normalized(물리단위는 ×수심). 파랑 표면 TKE 주입 부재 여부는 미확정(노트에 없음).
- **SWASH**: ~~`iturb==2` 의미 미확인(source-needed)~~ — **해소(2026-07-12)**: `=2` = full 3D k-ε 선형(`VISC FULL KEPS LIN`, SwashReadInput.ftn90:1265-1276; print 라벨 '3D viscosity with linear k-eps model' SwashPrintSettings.ftn90:276 — [[swash-turbulence-closure]] 갱신). 비선형 모드는 background floor/cap 을 건너뜀 — 저에너지 영역 ν 소실 가능.
- **ADCIRC**: 커버 최약 — MY2.5 안정함수 수치·표면/저면 q² BC 식은 미커버 잔존(vsmy.F `TURB` 내부, [[adcirc-3d-mode]] §F 카탈로그 수준). **부분 해소(2026-07-12)**: ~~`EVMin` 기본값~~ → 기본값 없음, fort.15 3D 블록 필수 필드(`READ(15,*) IEVC,EVMin,EVCon`, read_input.F:5237)이며 docs 가 "연직 점성 ≥ EVMIN 강제"(floor) 명시(paramdef:1349-1356); ~~운동량 연직확산 implicit 여부~~ → 복소 tridiagonal 확인([[adcirc-3d-vssol-vertical-scheme]], 2026-07-11).

## 6. 관련

- [[roms_vertical_mixing]]·[[roms_kpp_boundary_layer]]·[[efdc_turbulence]]·[[delft3d_turbulence]]·[[swash-turbulence-closure]]·[[adcirc-3d-mode]] — 모델별 canonical
- [[bottom-friction-cross-model]] — 저면 응력(본 노트 저면 BC 의 u* 공급원)
- `concepts/currents/06-model-application.md` §0.4-0.5 — wrapper 링크
