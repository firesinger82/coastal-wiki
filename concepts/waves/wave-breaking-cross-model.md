---
title: "파랑 쇄파 소산(depth-induced wave breaking) cross-model 대조 — 5개 모델 (위상평균 통계 Qb vs 위상해상 HFA/eddy viscosity)"
topic: waves
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "전 행이 각 모델 verified source-analysis·manual-notes 노트로 소급(셀에 노트 링크+file:line). 대표 anchor 직접 재확인(2026-07-07): SWASH SwashBreakPoint.ftn90:119,123(dsdt>α·√gh→q=0)·FUNWAVE breaker.F:124-142,151(tmp1=Cbrk1·√gh, onset ETAt≥tmp1). 미커버 셀 §5 disclosed."
note_author: "Claude Fable 5"
note_date: 2026-07-07
related:
  - models/SWAN/manual-notes/swan-tech-ch2-dissipation-detailed.md
  - models/XBeach/source-analysis/xbeach_wave_breaking.md
  - models/SWASH/source-analysis/swash-wetting-drying-runup.md
  - models/FUNWAVE/source-analysis/funwave-physics-sources.md
  - models/Celeris/source-analysis/celeris-breaking-boundary.md
---

# 파랑 쇄파 소산 cross-model 대조 (5모델)

> **Canonical source 규칙**: 각 모델 상세는 source-analysis/manual-notes 노트가 진실의 원천 — 본 노트는 대조 축만. cross-model 시리즈 6탄(EOS·transport·저면마찰·연직혼합·[[wetting-drying-cross-model]] 후속). **파랑 물리 첫 대조**.
> **최대 분기**: 파를 **개별 해상하느냐**가 쇄파 처리 전체를 가른다 — 위상평균(SWAN·XBeach)은 통계적 쇄파비율 Qb, 위상해상(SWASH·FUNWAVE·Celeris)은 개별 파봉의 표면상승률 판정.

## 1. 두 패러다임

| | 위상평균(phase-averaged) | 위상해상(phase-resolving) |
|---|---|---|
| 모델 | SWAN, XBeach(surfbeat) | SWASH, FUNWAVE, Celeris |
| 파 표현 | 스펙트럼/파작용 N(σ,θ) — 개별 파 미해상 | 격자 위 순간 수면 η — 개별 파봉 해상 |
| 쇄파 판정 | **통계적 Qb**(Rayleigh 분포서 H>H_max 비율) | **순간 ∂η/∂t** vs √(gh)(전면 급경사 탐지) |
| 소산 형태 | bulk D_tot → 스펙트럼 sink | 정수압 전환(HFA) 또는 eddy viscosity |
| 판정 스칼라 | H_rms/H_max (파고비) | ∂η/∂t (표면 상승률) |

## 2. 위상평균 — 통계적 Qb bulk 소산

| 모델 | 정식화(기본) | Qb·소산식 | γ 기본 | 수치 | 근거 |
|---|---|---|---|---|---|
| **SWAN** | **Battjes-Janssen 1978** bore(기본, `OFF BREAKING`으로만 해제) | `(1−Qb)/lnQb = −8E_tot/H_max²`, `D_tot=−α_BJ·Qb·σ̃·H_max²/8π`, H_max=γd | **γ 0.73**(Battjes-Stive 1985), α_BJ 1.0 | ★Newton-implicit positivity(∂S/∂E<0 해석보장, swantech §3.17) | [[swan-tech-ch2-dissipation-detailed]]·[[swan-source-terms-implementation]] |
| **XBeach** | **Roelvink** 확률형(surfbeat)/Baldock(stationary), 5종 | `Qb=1−exp(−(H/γh)^n)`(roelvink.F90:79-84), `D=Qb·2α·E/T_rep`(×H/h roelvink2) | **γ 0.55**·n 10·α 1.0 | explicit + gammax=2.0 limiter(H>γ_max·h clip) | [[xbeach_wave_breaking]]·[[xbeach_wave_action_balance]] |

**소산 주입**: SWAN 은 bulk 을 스펙트럼 bin 에 **에너지 비례배분** `S_ds,br=(D_tot/E_tot)·E(σ,θ)`(Eldeberky-Battjes 1995, Eq 2.68). XBeach 는 파작용 sink `−D/σ` **이자 roller 에너지 source**(이중역할, Svendsen 1984 roller 로 radiation stress 지연전달).

## 3. 위상해상 — 개별 파 onset 판정

| 모델 | 방식 | onset 판정 | onset/persist 기본 | 소산 주입 | 근거 |
|---|---|---|---|---|---|
| **SWASH** | **HFA**(정수압 전환) | `∂ζ/∂t > α·√(gh)`(SwashBreakPoint.ftn90:119) → `q=0`(:123) | **α 0.6 / β 0.3**(hysteresis) | 비정수압 제거→bore 자동소산(운동량 보존), ★brks→wets=0 dry 표시(:238) | [[swash-wetting-drying-runup]] |
| **FUNWAVE** | **Kennedy 2000 eddy viscosity** | `η_t ≥ Cbrk1·√(gh)`(breaker.F:151, tmp1=Cbrk1·√gh :124-125) | **Cbrk1 0.65 / Cbrk2 0.15** | `ν_br=cap1·Cbrk2√gh·(1+B)`(:142) 운동량 확산항(BreakSourceX), AGE 나이추적 | [[funwave-physics-sources]] |
| **Celeris** | Kennedy eddy viscosity(WGSL) | `∂η/∂t > dzdt_I_coef·c`(Pass_Breaking.wgsl:100) | dzdt_I/F_coef·T_star(**기본값 미커버**) | `ν_br=min(dxdy/dt, B·δ_b·h·∂η/∂t)`→Pass3 운동량 확산, t_here 상류3셀 advect | [[celeris-breaking-boundary]] |

**HFA vs eddy viscosity**: SWASH 는 소산항을 명시 주입하지 **않고** 비정수압을 끄면 NLSW bore 가 운동량보존 이산화로 자동 소산 — "무파라미터" 접근(α 만). FUNWAVE·Celeris 는 Kennedy eddy viscosity `ν∝h·∂η/∂t` 를 운동량 확산으로 명시 주입. 셋 다 개별 파봉의 **breaking age**(SWASH iwrk 인접전파 / FUNWAVE AGE / Celeris t_here advect)로 hysteresis 전파.

## 4. ★공통 구조 — onset > persistence hysteresis

전 모델이 **개시 임계 > 지속 임계** 이중값으로 채터링 억제:
- 위상평균: XBeach roelvink_daly(γ 시작 > γ2 종료 0.3). SWAN 은 통계형이라 순간 hysteresis 대신 Qb 연속.
- 위상해상: SWASH α 0.6 > β 0.3, FUNWAVE Cbrk1 0.65 > Cbrk2 0.15, Celeris dzdt_I > dzdt_F. **한 번 깨진 파의 후면은 낮은 임계로 breaking 유지** → 물리적 bore 지속.

계수 유사성: **위상해상 onset α/Cbrk1 ≈ 0.6–0.65 수렴**(전면 급경사 ~25°). 위상평균 γ 는 0.55(XBeach)~0.73(SWAN) — 정식화·calibration 따라 갈림.

## 5. ★함정·미커버 (disclosed gaps)

- **SWAN 기본 ON**: BREAKING command 없어도 항상 활성(`OFF BREAKING`으로만 해제) — SWAN 저면마찰이 기본 OFF 인 것과 반대([[bottom-friction-cross-model]] §5 대조). γ 0.73 이 swantech Eq 2.68 Battjes-Stive 와 자기정합.
- **XBeach 기본 정식 ≠ calibration**: 매뉴얼 기본 `break=roelvink2`(H³/h)이나 γ 0.55·n 10 표준값은 **roelvink1 기준 calibration** — roelvink2 사용 시 재보정 필요(문서 자체 경고).
- **★FUNWAVE 소스 ≠ 매뉴얼 배수**: 소스 onset `ETAt ≥ Cbrk1·√(gh)`(1배, breaker.F:124-151)이나 매뉴얼 §3.4 는 `η_t^(I)=0.65·2√(gh)`(2배) 표기 — **소스 기준 1배**가 실제. 임계값 인용 시 소스 확인.
- **미커버**: Celeris breaking 계수(dzdt_I/F_coef·T_star_coef·δ_b) 기본값 노트 미기재(config/globals source-needed). SWAN Thornton-Guza·XBeach Janssen-Battjes 는 이론노트에만(command·식 상세 얕음). ~~SWASH psurf 배열 소스 초기값 위치 미커버~~ — **해소(2026-07-12)**: α=0.6·β=**-1 sentinel**·nufac=1.0(SwashInit.ftn90:326-329, BRE 카드 동일 SwashReadInput.ftn90:916-918); ★매뉴얼 "β 기본 0.3" 의 실체는 CheckPrep 자동선택 — BDF 이류 스킴이면 **0.15**, 아니면 0.3(SwashCheckPrep.ftn90:1065-1090, [[swash-wetting-drying-runup]] §2.1 갱신).

## 6. 관련

- [[swan-tech-ch2-dissipation-detailed]]·[[xbeach_wave_breaking]]·[[swash-wetting-drying-runup]]·[[funwave-physics-sources]]·[[celeris-breaking-boundary]] — 모델별 canonical
- [[bottom-friction-cross-model]]·[[vertical-mixing-cross-model]]·[[wetting-drying-cross-model]] — cross-model 시리즈
- `concepts/waves/06-model-application.md` §8 — wrapper 링크
- [[harbor-tranquility-kds64]] — 위상해상(FUNWAVE/Celeris) vs 위상평균(SWAN) 선택 맥락
