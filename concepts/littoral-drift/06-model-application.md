---
title: "연안표사 — 06 모델 적용 (Delft3D · XBeach · EFDC · ROMS 의 longshore drift 계산 경로 비교)"
topic: littoral-drift
canonical_source: self
citation_status: verified
verification_method: "각 모델 source-analysis 노트 직접 read 후 longshore-drift 적용 정합 확인 + cross-link. Delft3D: delft3d_flow_wave_coupling.md (wave force fxw/fyw·radstr.f90:304·roller massfl.f90:113) + delft3d_sediment_morphology.md (erosed.f90·bott3d.f90 Exner bed update). XBeach: xbeach_morphology.md (transus/bed_update morphevolution.F90, Soulsby-Van Rijn, avalanching). EFDC: efdc_sediment.md (SedTran-Original ISTRAN(6/7) vs SEDZLJ, ssedtox.f90:868-880). ROMS: roms_sediment.md (CSTMS bedload/suspended) + roms_wec.md (vortex-force wec_vf.F·SWAN coupling mct_roms_swan.h). CONVENTIONS.md §3 — 모델 메커닉 디테일은 models/<model>/source-analysis/ 가 진실의 원천, 본 페이지는 요약 + 링크. 인과 chain (radiation stress→longshore current→sediment flux→morphology) 은 01-concept/02-theory (Holthuijsen §7.4.2-3·Bowen 1969·Battjes 1974) 의 검증된 도메인 이론."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
verification_by: "Claude Opus 4.8 (1M context) — 4 모델 source-analysis 노트 직접 read + longshore 적용 정합 확인"
verification_date: 2026-06-18
related:
  - concepts/littoral-drift/01-concept.md
  - concepts/littoral-drift/02-theory.md
  - concepts/sediment-transport/06-model-application.md
  - models/Delft3D/source-analysis/delft3d_sediment_morphology.md
  - models/XBeach/source-analysis/xbeach_morphology.md
  - models/EFDC/source-analysis/sediment/efdc_sediment.md
  - models/ROMS/source-analysis/sediment/roms_sediment.md
---

# 연안표사 — 06 모델 적용 (longshore drift 모델 계산 경로)

> **Canonical source 규칙** ([CONVENTIONS.md §3](../../CONVENTIONS.md)): 각 모델의 transport·morphology 메커닉 디테일은 `models/<model>/source-analysis/` 가 진실의 원천. 본 페이지는 **연안표사(longshore drift) 관점의 link-hub** — 각 모델이 동일한 인과 chain 을 어떤 서브루틴으로 구현하는지 비교 + cross-link.

## 1. 공통 인과 chain — process-based 모델은 CERC formula 를 쓰지 않는다

[`01-concept.md §3`](01-concept.md#3-cerc-formula-1984-shore-protection-manual) 의 CERC/Komar empirical formula 는 wave 통계만으로 $Q_l$ 을 **한 식으로** 추정한다. 반면 아래 4개 process-based 모델은 longshore drift 를 **명시적으로 계산하지 않고**, 다음 물리 chain 을 격자에서 풀어 그 결과로 alongshore sediment flux 가 emergent 하게 나타난다 ([`02-theory.md §5`](02-theory.md#5-에너지--s_xy--current-의-인과-chain) 의 chain 과 동일):

$$
\underbrace{\tfrac{1}{8}\rho g H^2}_{E}
\xrightarrow{\text{wave model}}
\underbrace{S_{xy}=E\,n\cos\theta\sin\theta}_{\text{radiation stress / vortex force}}
\xrightarrow{-\partial S_{xy}/\partial x}
\underbrace{v_l}_{\text{longshore current}}
\xrightarrow{\text{bed shear} + \text{wave stirring}}
\underbrace{q_b+q_s}_{\text{bed-load + suspended flux}}
\xrightarrow{\text{Exner}}
\underbrace{\partial z_b/\partial t}_{\text{morphology / shoreline}}
$$

핵심 차이는 **단계 2 (파→흐름 forcing)** 와 **단계 4-5 (flux→bed update)** 의 결합 방식이다. 단계 1 (radiation stress 유도) 은 [`02-theory.md §2`](02-theory.md#2-radiation-stress-holthuijsen-742), 단계 3 (longshore current 평형) 은 [`02-theory.md §4`](02-theory.md#4-longshore-current-bowen-1969-battjes-1974) 에서 도메인 이론으로 검증됨 (Holthuijsen §7.4.2-3, Bowen 1969, Battjes 1974).

## 2. 비교표 — 4개 모델의 longshore drift 경로

| 모델 | 파→흐름 forcing (단계 2) | longshore current 담당 | transport 공식 (단계 4) | morphology 결합 (단계 5) | 연안표사 적용 비고 |
|---|---|---|---|---|---|
| **Delft3D-FLOW + WAVE** | SWAN-기반 WAVE 가 wave force `fxw/fyw` + surface stress `wsu/wsv` 를 COM 파일로 FLOW 에 전달; roller path 가 radiation stress 계산 (`radstr.f90:304`) | FLOW 의 3D 운동량식에 wave force 주입 (`uzd.f90:668`) → alongshore current | Van Rijn 1984/2007 (bed+susp), Partheniades-Krone (점착) — `erosed.f90` | **online morphology** (Exner bed update `bott3d.f90`), MorFac 가속 | breaker zone alongshore current + bed update 직접 — surf-zone 분해 시 roller 권장 |
| **XBeach** | surfbeat 모드: short-wave action balance → roller → radiation-stress gradient 가 NLSWE flow 구동 (wave-group scale) | NLSWE shallow-water flow (surf-beat·infragravity 포함) | Soulsby-Van Rijn / Van Thiel-Van Rijn / Van Rijn 1993 (`sedtransform`) — skewness·asymmetry `ua` 포함 | bed update `dzg = morfac·dt/(1−por)·∇·flux` (`morphevolution.F90:737-748`) + **avalanching** (사면붕괴) | dune erosion·overwash·breaching 폭풍 사건 특화 (수일~수주); longshore 보다 cross-shore + 2DH storm impact 강점 |
| **EFDC** | hydrodynamic core 가 흐름 계산; wave 는 외부(SWAN) wave-current bottom shear 로 결합 (Christoffersen-Jonsson, SEDZLJ) | EFDC 자체 3D 흐름 solver (조류·바람·밀도 구동) | **SedTran-Original** (`ISTRAN(6)` cohesive `CALSED` / `ISTRAN(7)` noncohesive `CALSND`) 또는 **SEDZLJ** unified multi-bed-layer (`ssedtox.f90:868-880`) | bed-water 결합 + multi-bed-layer 동역학 | 흐름(조류)·하구 표사 주력; 순수 wave-driven longshore current 는 외부 wave coupling 의존 |
| **ROMS (+WEC, CSTMS)** | **WEC vortex-force** 정식 (`wec_vf.F`); SWAN coupling 시 spectral Stokes drift + wave dissipation (`mct_roms_swan.h`) | ROMS 3D primitive-equation 흐름 + WEC 가 surf-zone alongshore/rip current 구동 | CSTMS: bedload (Meyer-Peter-Müller·Soulsby-Damgaard·Van der A 2013) + suspended (tracer) — `roms_sediment.md` | active-layer bed model + Exner; COAWST(ROMS+SWAN) 통합 | regional shelf~surf zone 광역; vortex-force 로 longshore·rip current 물리 정밀 (Uchiyama et al. 2010) |

(각 셀의 file:line·서브루틴은 아래 §3-§6 의 canonical 노트에서 검증)

## 3. Delft3D-FLOW + WAVE — radiation stress → 흐름 → bed update

> Canonical: [`delft3d_flow_wave_coupling.md`](../../models/Delft3D/source-analysis/wave/delft3d_flow_wave_coupling.md) (파→흐름) + [`delft3d_sediment_morphology.md`](../../models/Delft3D/source-analysis/delft3d_sediment_morphology.md) (bed update).

**단계 2 (파→흐름)**: Delft3D-WAVE(SWAN 기반)가 FLOW 와 COM 파일로 통신. FLOW 가 읽는 wave 필드에 wave force `FX/FY`, wave-induced bottom shear `WSBU/WSBV` 포함 ([`delft3d_flow_wave_coupling.md §C`](../../models/Delft3D/source-analysis/wave/delft3d_flow_wave_coupling.md)). 운동량식 주입은 `uzd.f90:668` (surface wave stress `wsu` + body force `fxw`). roller 활성 시 radiation-stress path 가 `wsu/wsv`·`fxw/fyw` 를 계산 (`radstr.f90:304`), roller 가 mass flux `(Ewave + 2·Eroll)/ρ/c` 를 추가 (`massfl.f90:113`) — surf-zone breaking momentum 재분배 (rip current·undertow).

**단계 4-5 (flux→bed)**: online morphology 커널 `compute_sediment` 패키지. `erosed.f90` 가 침식/퇴적 + bedload + 부유확산 source/sink 계산, `bott3d.f90` 가 Exner bed update (BODSED 변화) 수행. canonical 알고리즘 = Lesser et al. 2004 (Coastal Engineering 51:883-915). → **연안표사**: alongshore current 가 만든 bed shear + wave stirring 으로 longshore sediment flux 발생, MorFac 로 장기 가속.

## 4. XBeach — surfbeat + morphevolution (dune erosion·overwash·avalanching)

> Canonical: [`xbeach_morphology.md`](../../models/XBeach/source-analysis/xbeach_morphology.md).

**단계 2-3**: surfbeat 모드는 short-wave action balance + roller → radiation-stress gradient 가 NLSWE flow 를 wave-group scale 로 구동 (infragravity·surf-beat 포함). 실행 순서: wave → flow → `transus` (`libxbeach.F90:301-307`).

**단계 4**: `transus` → `sedtransform` 가 Soulsby-Van Rijn / Van Thiel-Van Rijn / Van Rijn 1993 중 선택 (`morphevolution.F90:173-176`); suspended `Susg/Svsg` 와 bed-load `Subg/Svbg` 분리. wave skewness/asymmetry 속도 `ua` 가 advection 에 더해짐 (Ruessink-Van Rijn, `:3032-3039`).

**단계 5**: `bed_update` 가 보존형 flux-gradient `dzg = morfac·dt/(1−por)·∇·flux` (`:737-748`) + bed-slope 보정 (Roelvink·Soulsby·Talmon) + **avalanching** (사면 한계 초과 시 붕괴 재분배, `:863`).

→ **연안표사 적용**: XBeach 의 강점은 cross-shore + 2DH **폭풍 사건** (dune erosion·overwash·breaching, Maemi·Hinnamnor 등 수일~수주 scale, [`sediment-transport/06 §4`](../sediment-transport/06-model-application.md#4-xbeach-sediment)). longshore drift 자체는 2DH 격자에서 alongshore current·flux 로 나타나지만, 장기 연안수지보다 단기 storm impact 가 주 용도.

## 5. EFDC — 2 분기 sediment (SEDZLJ / Original) + 외부 wave coupling

> Canonical: [`efdc_sediment.md`](../../models/EFDC/source-analysis/sediment/efdc_sediment.md).

**단계 4-5**: 두 분기 system ([`sediment-transport/06 §2`](../sediment-transport/06-model-application.md#2-efdc-sed-사용자-주력--2-분기-모델) 와 동일 canonical):
- **SedTran-Original**: `ISTRAN(6)≥1` cohesive → `CALSED` (Krone-Partheniades), `ISTRAN(7)≥1` noncohesive → `CALSND` (Van Rijn 1984·Engelund-Hansen). 분기 `ssedtox.f90:868-880`.
- **SEDZLJ**: size-class unified cohesive+noncohesive, multi-bed-layer, **Christoffersen-Jonsson wave-current shear stress**.

**단계 2 (파→흐름) 한계**: EFDC 의 hydrodynamic core 는 조류·바람·밀도 구동 흐름이 주력. 순수 wave-driven longshore current (radiation stress → surf-zone alongshore current) 는 **외부 SWAN wave coupling 의 wave-current bottom shear** 로만 들어온다 — Delft3D/ROMS 처럼 wave force 를 운동량식에 직접 주입하는 surf-zone radiation-stress driver 는 본 source-analysis 노트 범위에서 확인되지 않음 (source-needed). → 하구·조류 우세 표사에 강점, breaker-zone longshore drift 전용 도구로는 wave coupling 구성 필요.

## 6. ROMS — WEC vortex-force + CSTMS

> Canonical: [`roms_sediment.md`](../../models/ROMS/source-analysis/sediment/roms_sediment.md) (transport) + [`roms_wec.md`](../../models/ROMS/source-analysis/roms_wec.md) (파→흐름).

**단계 2-3**: ROMS WEC(Wave Effects on Currents) 모듈이 **vortex-force 정식** `wec_vf.F` 으로 wave-current interaction 구현 (`WEC_VF` flag, Mellor radiation-stress 형식은 이 tree 에 없음). 3D 운동량에 WEC stress `rustr3d/rvstr3d` 주입 (`rhs3d.F:1068-1087`). SWAN coupling 시 spectral Stokes drift + dissipation (`mct_roms_swan.h:153-163`). surf-zone resolved 시 `WEC_VF + roller + streaming + breaking dissipation` → alongshore·rip current 생성 (Uchiyama et al. 2010, McWilliams et al. 2004).

**단계 4-5**: CSTMS — bedload (Meyer-Peter-Müller·Soulsby-Damgaard·Van der A 2013) + suspended (`step3d_t` tracer) + active-layer bed model. wave-enhanced BBL (SSW/MB/SG) 가 combined wave-current bottom stress 제공.

→ **연안표사 적용**: vortex-force 로 longshore·rip current 물리가 가장 정밀; COAWST(ROMS+SWAN+atmos) 통합으로 regional shelf ~ surf zone 광역 동시 ([`sediment-transport/06 §5`](../sediment-transport/06-model-application.md#5-roms-sediment)).

## 7. 모델 선택 가이드 — 연안표사 목적별

| 목적 | 권장 | 근거 |
|---|---|---|
| 항만 인근 longshore drift + 장기 bed 변화 | **Delft3D-FLOW+WAVE** (roller + online morph + MorFac) | wave force 운동량 주입 + Exner bed update + 장기 가속 (§3) |
| 폭풍 dune erosion·overwash·breaching | **XBeach** surfbeat (수일~수주) | avalanching + skewness/asymmetry, storm impact 특화 (§4) |
| 하구·조류 우세 + 점착성 표사 | **EFDC** (SEDZLJ 또는 Original) | 조류 구동 흐름 + multi-bed-layer (§5) |
| Regional shelf~surf 광역 + rip current 물리 | **ROMS** WEC_VF + CSTMS (COAWST) | vortex-force longshore/rip current 정밀 (§6) |
| 빠른 1차 연안수지 추정 (격자 불필요) | CERC / Kamphuis empirical | [`01-concept.md §3,§5`](01-concept.md#3-cerc-formula-1984-shore-protection-manual) |
| shoreline 1-line 장기 예측 | GENESIS·UNIBEST-LT (one-line) | [`01-concept.md §9.2`](01-concept.md#92-간접-model) — 본 위키 미보유 (source-needed) |

## 8. 검증·한국 적용 (source-needed)

- 위 비교표·서브루틴 경로는 **모델 source-code level 로 verified** (각 canonical 노트 file:line).
- **한국 해변 longshore drift 정량 검증** (안목항·낙산 등, [`01-concept.md §8`](01-concept.md#8-한국-적용-사례-citation-todo)) 의 **모델 적용 케이스·calibration 결과**는 본 페이지 범위 밖이며 개별 사례 출처 확보 전까지 **source-needed**. ("내가 해보니" 화법은 [CLAUDE.md 규칙 4](../../CLAUDE.md) 에 따라 `experience/` 로 — 객관 데이터 3조건 통과 시.)
- 모델별 longshore transport vs CERC formula **정량 비교** (예: Delft3D 산출 $Q_l$ 이 CERC $K=0.39$ 추정과 몇 % 차이) 도 본 위키 내 재현 데이터 미보유 → **source-needed**.

## 9. 연결

- 도메인 layer: [`01-concept.md`](01-concept.md) (CERC·Komar·sediment budget·한국 사례) · [`02-theory.md`](02-theory.md) (radiation stress→set-up→longshore current 유도)
- 인접 토픽: [`concepts/sediment-transport/06-model-application.md`](../sediment-transport/06-model-application.md) (일반 표사 모델 적용 — 본 페이지의 longshore 특화 대응) · [`concepts/waves/02-theory.md`](../waves/02-theory.md) (wave driver) · [`concepts/storm-surge/01-concept.md`](../storm-surge/01-concept.md) (폭풍 시 drift 폭증)
- 모델 canonical (source-code 분석):
  - [`models/Delft3D/source-analysis/delft3d_sediment_morphology.md`](../../models/Delft3D/source-analysis/delft3d_sediment_morphology.md) · [`delft3d_flow_wave_coupling.md`](../../models/Delft3D/source-analysis/wave/delft3d_flow_wave_coupling.md)
  - [`models/XBeach/source-analysis/xbeach_morphology.md`](../../models/XBeach/source-analysis/xbeach_morphology.md)
  - [`models/EFDC/source-analysis/sediment/efdc_sediment.md`](../../models/EFDC/source-analysis/sediment/efdc_sediment.md)
  - [`models/ROMS/source-analysis/sediment/roms_sediment.md`](../../models/ROMS/source-analysis/sediment/roms_sediment.md) · [`roms_wec.md`](../../models/ROMS/source-analysis/roms_wec.md)
