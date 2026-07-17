---
title: "파랑 — 06 모델 적용 (SWAN · WW3 · XBeach · Delft3D-WAVE)"
topic: waves
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "AI cross-reference. SWAN 부분은 [models/SWAN/manual-notes/swan-action-balance.md] verified로 검증. **2026-06-18 갱신**: SWAN(29 SA+29 manual)·XBeach(32 SA)·Delft3D(38 SA)·FUNWAVE·Celeris 전수 검수 완료 — 'stub' stale 참조를 검수 source-analysis cross-link 로 정정(staleness sweep). WW3 만 미수록(models/WW3/ 미생성, research/watchlist 추적). 외부 공식 source 인용분(2026-05-21)은 유지."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 파랑 — 06 모델 적용

> **Canonical source 규칙** ([CONVENTIONS.md §3](../../CONVENTIONS.md)): 모델 메커닉은 `models/<model>/`이 진실의 원천. 본 페이지는 요약 + 링크만.

## 1. 모델 선택 (도메인별)

| 도메인 | 권장 모델 | Canonical |
|---|---|---|
| 대양·전 지구 hindcast | **WAVEWATCH III (WW3)** | [`models/`](../../models/) WW3 dir 미생성 (TBD) |
| 한국 연안 spectral (천해) | **SWAN** | [`models/SWAN/`](../../models/SWAN/) (STABLE, source-analysis 29 + manual-notes 29) |
| 천해 + 흐름 결합 (조류 영향) | SWAN with currents | 같음 |
| 폭풍 침식·범람 | **XBeach** | [`models/XBeach/`](../../models/XBeach/) (source-analysis 32 verified) |
| 항만 정온도·공명·다중반사 | 위상해상 Boussinesq (**FUNWAVE**·**Celeris**) / mild-slope (**ARTEMIS**) | [`models/FUNWAVE/`](../../models/FUNWAVE/) · [`models/Celeris/`](../../models/Celeris/) — §1.1 |
| 통합 풍파·조석·표사 시뮬 | Delft3D-WAVE + FLOW | [`models/Delft3D/`](../../models/Delft3D/) (source-analysis 48 verified) |

### 1.1 항만 정온도 (harbor agitation/tranquility) — 모델 선택 trade-off

**정온도 분석** = 다양한 입사조건(파향 × 주기 × 재현빈도 × 조위)에서 항내 파고를 평가(가동률·downtime, 항만 설계 표준 절차). 회절·반사·**공진(resonance)**을 해상해야 하므로 phase-resolving 또는 mild-slope 모델이 필요. **케이스 폭증 × 케이스당 비용**이 핵심 제약:

| 접근 | 모델 | 특성 | 라이선스 |
|---|---|---|---|
| **위상해상 Boussinesq** | FUNWAVE · Celeris · MIKE 21 BW | 비선형·IG파·공진 정확하나 **시간진행**으로 정상상태까지 반복 → **느림** | FUNWAVE/Celeris **open** / MIKE 21 BW **상용(DHI)** |
| **타원형 mild-slope** | ARTEMIS · CGWAVE | Berkhoff(mild-slope) **정상 조화해 직접**(시간진행 불요) → 케이스당 빠름, 단 선형·(준)단색파 | **ARTEMIS open**(GPLv3 openTELEMAC, harbor agitation 특화) / CGWAVE USACE-ERDC·**SMS 상용 GUI** 경유 |

→ 위상해상 Boussinesq의 **"정온도 다수 케이스 × 케이스당 느림" 곱셈 비용**을 **GPU가 상쇄**: [`models/FUNWAVE/`](../../models/FUNWAVE/) **FUNWAVE-GPU**(36-core 대비 4-10×) · [`models/Celeris/`](../../models/Celeris/) **real-time interactive**(항만 배치 탐색에 강함). **실무 권장**: 빠른 1차 스크리닝은 mild-slope(**ARTEMIS** open), 비선형·IG·공진 정밀 검증은 **GPU Boussinesq** — 상보적. (출처: ARTEMIS = openTELEMAC GPLv3 Berkhoff/harbor agitation [opentelemac.org]; FUNWAVE/Celeris = `models/`; 정온도 다중조건 = 항만 설계 practice)

→ **한국 설계 표준 정량값**(KDS 64 구조물 반사율·정온 기준파고 + 표준 SWAN nesting 워크플로): [`harbor-tranquility-kds64.md`](harbor-tranquility-kds64.md) ★. 실무는 SWAN이 표준(인허가), FUNWAVE/Celeris는 공진·정밀 검증 티어.

## 2. Nested SWAN 표준 흐름 (downscaling)

대양 hindcast → 연안 spectral 모델로 단계적 격자 세분화(nesting)하는 일반 다운스케일링 워크플로 (SWAN UserManual NESTOUT/NEST):

```
Layer 0: WW3 글로벌 hindcast (외해 spectrum)
   ↓ NESTOUT
Layer 1: SWAN coarse (광역, ~0.05° 격자)
   ↓ NESTOUT
Layer 2: SWAN middle (지역, ~0.005° = ~500 m)
   ↓ NESTOUT
Layer 3: SWAN detail (~50-100 m, 항만·연안)
   ↓
검증: 관측 정점 H_s·T_p·방향 비교
```

각 layer 입력 (일반):
- **수심**: GEBCO 등 외해 측심 + 정밀 연안 측심
- **바람**: 재분석/예보 바람장 (예: JMA-MSM 5 km)
- **경계 spectrum**: 상위 layer NESTOUT
- **조류** (선택): EFDC 또는 ADCIRC 출력 (`concepts/currents/06-model-application.md`)
- **수위** (선택): 약최고고조면 (AHHW) 보정

## 3. SWAN — Holthuijsen Ch.9 canonical

> **Canonical**: [`models/SWAN/`](../../models/SWAN/) + [`textbook/notes/waves-holthuijsen-toc.md`](../../textbook/notes/waves-holthuijsen-toc.md) §Ch.9
>
> Holthuijsen이 SWAN 공동 개발자라 Ch.9 전체가 algorithmic reference.

### 3.1 입력 카드 (요약)

상세는 [`models/SWAN/manual-notes/`](../../models/SWAN/manual-notes/) (29 노트 작성됨):

- `MODE STATIONARY/NONSTATIONARY` — 시간 모드
- `CGRID REGULAR/CURVILINEAR/UNSTRUCTURED` — 계산 격자
- `INPGRID BOTTOM/WIND/CURRENT/...` — 입력 격자
- `BOUND SPECTRUM FILE` — 경계 스펙트럼 입력
- `WIND` — 바람 강제
- `FRICTION` — 저면 마찰 옵션 (JONSWAP/Madsen/Collins)
- `BREAKING` — 깊이 유도 쇄파 (Battjes-Janssen 등)
- `OUTPUT BLOCK/SPECOUT/TABLE` — 출력

> 한국 연안 multi-domain nesting 운용 패턴은 바이블 검증(객관 데이터) 후 `experience/` 에 카테고리화 — 본 canonical 미수록. (citation_status: source-needed)

## 4. WAVEWATCH III (WW3)

> Canonical: `models/WW3/` (미생성, TBD)

- 한국 적용: 외해 forcing 계산 → SWAN nested
- 직접 사용 사례 드물 (한국에서는 SWAN이 표준 nearshore tool)

## 5. XBeach

> Canonical: [`models/XBeach/`](../../models/XBeach/) (source-analysis 32 + manual-notes 4 verified) — [[../../models/XBeach/source-analysis/xbeach_wave_action_balance]](surfbeat)·[[../../models/XBeach/source-analysis/xbeach_nonh]]·[[../../models/XBeach/source-analysis/xbeach_morphology]]

- 폭풍 침식·범람 사례 (10²-10³ km² 도메인, 시간 1-7 일) `[source-needed]` <!-- 값 재검토: 10³ km² 는 XBeach 통상 적용 규모 초과 의심 -->
- 입력: 외부 spectrum (SWAN 출력 또는 직접 measurement)
- 출력: 모래사장 단면 변화, 침수 범위, 인프라 피해 분석

## 6. Delft3D-WAVE (D3D-4 또는 FM)

> Canonical: [`models/Delft3D/`](../../models/Delft3D/) (source-analysis 48 + manual-notes 11 verified) — [[../../models/Delft3D/source-analysis/delft3d_wave_swan_module]]·[[../../models/Delft3D/source-analysis/wave/delft3d_flow_wave_coupling]]·[[../../models/Delft3D/manual-notes/delft3d-wave-user-manual]]

- D3D-4 WAVE = SWAN 통합 (Delft3D-FLOW + WAVE coupling)
- Delft3D FM (WAVE 부분 D-Waves)

## 7. 검증

### 7.1 검증 정점 (한국 공개 관측망)

- **MPT 74 정점** ([`05-examples.md` §1](05-examples.md)):
  - MOF (해양수산부) 34
  - KMA (기상청) 29
  - KHOA (국립해양조사원) 11
- **TW (KHOA 파랑 정점)**: 추가 60+ 정점

### 7.2 검증 메트릭

> ⚠ 아래 '일반 기준' 수치(RMSE·bias·상관계수·방향오차 임계)는 인용 근거 미확보 — 출처(검증 practice 문헌·기관 기준) 확보 전까지 참고값. (source-needed)

| 메트릭 | 정의 | 일반 기준 |
|---|---|---|
| RMSE H_s | √mean((Hs_model - Hs_obs)²) | < 0.3 m for typical |
| Bias H_s | mean(Hs_model - Hs_obs) | |bias| < 0.1 m |
| Pearson r (H_s) | 상관계수 | > 0.85 |
| RMSE T_p | √mean((Tp_model - Tp_obs)²) | < 1.5 s |
| Pearson r (T_p) | 상관계수 | > 0.7 |
| 방향 평균 절대 오차 | mean|Δθ| | < 20° |

> 특정 항만 SWAN 검증 사례(정량 RMSE·Bias·correlation)는 바이블 검증(객관 데이터) 후 `experience/` 에 카테고리화 — 본 canonical 미수록. (citation_status: source-needed)

## 7.5 쇄파 소산 — 5개 모델 cross-model 대조

깊이유발 쇄파(depth-induced breaking) 처리는 위상평균(SWAN·XBeach 통계적 Qb)과 위상해상(SWASH·FUNWAVE·Celeris 개별 파 onset)이 근본적으로 갈린다 — **[[wave-breaking-cross-model]]** 이 canonical. 요지: SWAN γ=0.73 Battjes-Janssen(기본 ON, Newton-implicit) vs XBeach γ=0.55 Roelvink(explicit+gammax) vs SWASH HFA(α=0.6, 정수압 전환+dry) vs FUNWAVE/Celeris Kennedy eddy viscosity(Cbrk 0.65/0.15). 위상해상 onset(α/Cbrk1≈0.6–0.65)은 전면 급경사로 수렴.

## 8. 다른 토픽과의 교차

- **tides** (`concepts/tides/`): 약최고고조면 (AHHW) 보정 — SWAN 수심 갱신 시 [`02-theory.md §8.2`](../tides/02-theory.md) DL+Z₀ 적용
- **currents** (`concepts/currents/`): SWAN current input (조류 → 파 분산 보정)
- **sediment-transport** (미작성): SWAN 출력 (radiation stress) → XBeach·SED 모델 연쇄
- **storm-surge** (미작성): SWAN + EFDC/ADCIRC + bottom friction coupling

## 9. 보강 — `verified` 승격 체크리스트

- [ ] `models/SWAN/manual-notes/` — Holthuijsen Ch.9 + SWAN UserManual 입력 카드 상세
- [ ] `models/SWAN/web-refs/swan-official-resources.md` — 공식 사이트·논문 인용
- [ ] `models/WW3/` 새 디렉토리 생성 + 정체카드
- [ ] `models/XBeach/manual-notes/` — XBeach surfbeat·non-hydrostatic 모드

## 10. 연결

- `01`~`05` — 도메인 지식
- 모델별 canonical (`models/`):
  - [`models/SWAN/`](../../models/SWAN/) (STABLE, source-analysis 29 + manual-notes 29)
  - `models/WW3/` (미생성 — research/watchlist/repo-noaa-emc-ww3 추적)
  - [`models/XBeach/`](../../models/XBeach/) (source-analysis 32 verified)
  - [`models/Delft3D/`](../../models/Delft3D/) (source-analysis 48 verified)
- 소스 노트:
  - [`textbook/notes/waves-holthuijsen-toc.md`](../../textbook/notes/waves-holthuijsen-toc.md) — Holthuijsen Ch.9 SWAN canonical
- 외부:
  - SWAN: [https://swanmodel.sourceforge.io/](https://swanmodel.sourceforge.io/)
  - WW3: [github.com/NOAA-EMC/WW3](https://github.com/NOAA-EMC/WW3)
  - XBeach: [xbeach.readthedocs.io](https://xbeach.readthedocs.io/)
