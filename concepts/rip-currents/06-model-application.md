---
title: "이안류 모델 표현 cross-model 대조 — 위상해상 자연발생 vs radiation stress 파력 vs vortex force (9모델)"
topic: rip-currents
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "전 행이 각 모델 verified source-analysis 노트로 소급한다(셀에 노트 링크 + 그 노트가 확보한 file:line). 본 노트는 대조 축만 만들고 상세는 각 모델 노트가 진실의 원천(CONVENTIONS §3). 분류 경계(위상해상/위상평균)는 [[wave-breaking-cross-model]] 의 검증된 구분을 따른다. SFINCS SnapWave·LISFLOOD-FP 포함 여부는 소스 확인 후 판정 — §5 참조."
note_author: "Claude Opus 5"
note_date: 2026-09-22
related:
  - concepts/rip-currents/02-theory.md
  - concepts/waves/wave-breaking-cross-model.md
  - models/XBeach/source-analysis/xbeach_wave_functions.md
  - models/ROMS/source-analysis/roms_wec.md
  - models/Delft3D/source-analysis/delft3d_dflowfm_waves.md
  - models/SFINCS/source-analysis/sfincs_snapwave.md
---

# 이안류 모델 표현 cross-model 대조

> **Canonical source 규칙**: 각 모델 상세는 해당 `source-analysis` 노트가 진실의 원천 — 본 노트는 **대조 축**만 만든다.
> **대조의 핵심**: 이안류는 모델이 직접 푸는 대상이 아니다. **연안방향으로 불균일한 파랑 강제**가 있으면
> 2DH 흐름해가 스스로 만들어내는 순환이다. 따라서 "이안류를 지원하는가" 가 아니라
> **"파랑이 흐름을 어떻게 구동하는가"** 가 모델을 가른다.

## 1. 이안류가 성립할 조건

[[02-theory]] 의 형성 메커니즘 — 쇄파에 의한 평균수위 상승(setup)이 **연안방향으로 불균일**하면
그 수위경사가 연안류를 수렴시키고, 수렴점에서 외해로 빠져나가는 보상류가 이안류다.

모델이 이것을 재현하려면 셋이 동시에 필요하다.

| 요건 | 없으면 |
|---|---|
| **2DH 이상**(연안·횡단 2방향 흐름) | 1D 단면 모델은 순환 자체가 불가 |
| **연안방향 불균일 파랑 강제** | 균일 강제면 setup 도 균일 → 순환 없음 |
| **그 강제가 운동량식에 들어가는 경로** | 파는 풀리지만 흐름을 밀지 못함 |

셋째 조건의 **구현 방식**이 아래 세 갈래다.

## 2. 세 갈래

| | A. 위상해상 | B. 파력(radiation stress) | C. vortex force |
|---|---|---|---|
| 파 표현 | 격자 위 순간 수면 η | 스펙트럼/파작용 N(σ,θ) | 스펙트럼 + Stokes 분리 |
| 흐름 구동 | **자동** — 해상된 파운동에 이미 포함 | $F_x=-\partial S_{xx}/\partial x-\partial S_{xy}/\partial y$ 를 운동량식에 가산 | Stokes drift 와 와도의 상호작용항 |
| 이안류 | 지형·구조물만 주면 **창발** | 파력장 불균일에서 발생 | 같음(정식화가 다름) |
| 대가 | 격자·시간 해상도 비쌈 | 파-흐름 분리 가정 | 구현 복잡 |

분류 경계(위상해상/위상평균)는 [[wave-breaking-cross-model]] 의 검증된 구분을 그대로 쓴다.

## 3. 모델별

### A. 위상해상 — 이안류가 창발한다

| 모델 | 근거 |
|---|---|
| **SWASH** | 비정수압 층분할, 순간 η 해상. 쇄파는 HFA 정수압 전환(`SwashBreakPoint.ftn90:119`) — [[swash-explicit-depthavg-flow]] |
| **FUNWAVE** | Boussinesq, 쇄파 Kennedy eddy viscosity(`breaker.F:151`) + roller — [[funwave-physics-sources]] |
| **Celeris** | Boussinesq GPU(WGSL), 쇄파 `Pass_Breaking.wgsl:100` — [[celeris-boussinesq-solver]] |

이 셋은 **파력 항이 따로 없다.** 파봉을 직접 풀므로 setup·연안류·이안류가 같은 운동량식의 해로 나온다.
바꿔 말해 **이안류 재현 여부는 격자·시간 해상도와 쇄파 모델의 문제**이지 결합의 문제가 아니다.

### B. 파력(radiation stress) — 파랑해를 흐름에 전달한다

| 모델 | 전달 경로 | 근거 |
|---|---|---|
| **XBeach**(surfbeat) | `compute_wave_forces`: 파+roller 에너지(ee+rr)로 $S_{xx}/S_{xy}/S_{yy}$ → $F_x=-\partial S_{xx}/\partial x-\partial S_{xy}/\partial y$. Stokes drift 는 GLM 보정(`ue=u+us`) | [[xbeach_wave_functions]] §4 |
| **Delft3D D-Flow FM** | `WAVEFORCING_*` 모드 — 0=없음 / 1=radiation stress / 2=dissipation total / 3=dissipation 3D (`m_waveconst.f90:18-21`) | [[delft3d_dflowfm_waves]] |
| **ADCIRC + SWAN** | SWAN 의 radiation stress 경사를 절점 파력 `SWAN_RSNX2/SWAN_RSNY2` 로 변환(`:360-364, 399-404, 421-427`) | [[adcirc-swan-coupling]] §C |
| **EFDC+** | 내부 wind-wave(SPM fetch) 또는 SWAN 결합(GETSWAN) → `WAVESXY` 로 radiation stress 강제 | [[efdc_waves]] |
| **SFINCS + SnapWave** | SnapWave 가 파력을 SFINCS 단위로 환산해 넘긴다 — `snapwave_Fx = Fx * rho * depth`(`:563-564`) | [[sfincs_snapwave]] |

**XBeach 의 위치가 특수하다.** surfbeat 모드는 파를 위상평균하되 **파군(wave group) 시간규모는 해상**하므로,
파력이 파군 주기로 변동한다 → 이안류의 **저주파 맥동(VLF pulsation)** 까지 표현할 여지가 있다.
이는 정상상태 파랑을 쓰는 B 계열 다른 모델과 구분되는 지점이다.

### C. vortex force — ROMS

| 모델 | 정식화 | 근거 |
|---|---|---|
| **ROMS** | WEC(Wave Effects on Currents) **vortex-force** 정식화 — `WEC_VF`(`WEC/wec_vf.F:1-905`), Stokes drift 별도(`WEC/wec_stokes.F:1-723`). 이 트리에 **`WEC_MELLOR` 심볼은 없다** | [[roms_wec]] |

radiation stress 형(B)과 vortex force 형(C)은 **같은 물리의 다른 분해**다. 후자는 파의 질량수송(Stokes drift)과
평균흐름 와도의 상호작용으로 쓰므로 3D 연직구조에서 해석이 깔끔하다. 어느 쪽이 이안류를 더 잘 내는지는
본 위키가 판정하지 않는다 — 근거가 없다.

## 4. 대조표

| 모델 | 파 표현 | 흐름 구동 | 파군 시간규모 | 이안류 |
|---|---|---|---|---|
| SWASH · FUNWAVE · Celeris | 위상해상 η | 내재 | 해상 | **창발** |
| XBeach (surfbeat) | 위상평균 + 파군 | radiation stress 파력 | **해상** | 파력 불균일에서 발생, 맥동 여지 |
| Delft3D FM · ADCIRC+SWAN · EFDC+ | 위상평균 | radiation stress 파력 | 미해상 | 평균 순환 |
| SFINCS + SnapWave | 위상평균, **정상상태** 파솔버 | radiation stress 파력 | 미해상 | 평균 순환 |
| ROMS | 위상평균 | **vortex force** | 미해상 | 평균 순환 |
| LISFLOOD-FP | — | — | — | **불가**(§5) |

## 5. 경계 사례 — 확인한 것과 확인하지 않은 것

**LISFLOOD-FP 는 대상이 아니다.** 소스의 "wave" 는 `diffusive wave`, 즉 홍수 추적 근사다
(`fp_flow.cpp:122-349` `CalcFPQx/y`, [[lisflood-fp-classic-acc-flow]] §4). 파랑 강제 자체가 없다.

**SFINCS 는 처음 제외했다가 정정했다.** SnapWave 가 SFINCS 와 한 바이너리로 통합돼 파력을 넘긴다.
다만 SnapWave 는 **정상상태 솔버**이므로([[sfincs_snapwave]] 제목·§개요) 파군·IG 시간규모의 변동은
파랑 쪽에서 오지 않는다. 평균 이안류 순환과 맥동을 구분해서 생각해야 한다.

**판정하지 않은 것**: 각 모델이 실제 이안류를 **얼마나 정확히** 내는지. 그것은 검증 사례 비교이고
본 위키에 그 근거가 없다. 본 노트는 **구동 경로의 유무와 형태**만 대조한다.
