---
title: "파랑 — 06 모델 적용 (SWAN · WW3 · XBeach · Delft3D-WAVE)"
topic: waves
canonical_source: self
citation_status: source-needed
verification_method: "AI cross-reference. 본 문서는 요약 + 링크 ([CONVENTIONS.md §3] canonical source 분리). 모델 디테일은 `models/<model>/`이 진실의 원천 — SWAN은 stub 존재, 나머지 stub. 채워지면 source-needed → verified."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: ""
verification_date: ""
---

# 파랑 — 06 모델 적용

> **Canonical source 규칙** ([CONVENTIONS.md §3](../../CONVENTIONS.md)): 모델 메커닉은 `models/<model>/`이 진실의 원천. 본 페이지는 요약 + 링크만.

## 1. 모델 선택 (도메인별)

| 도메인 | 권장 모델 | Canonical |
|---|---|---|
| 대양·전 지구 hindcast | **WAVEWATCH III (WW3)** | [`models/`](../../models/) WW3 dir 미생성 (TBD) |
| 한국 연안 spectral (천해) | **SWAN** | [`models/SWAN/`](../../models/SWAN/) ← STUB |
| 천해 + 흐름 결합 (조류 영향) | SWAN with currents | 같음 |
| 폭풍 침식·범람 | **XBeach** | [`models/XBeach/`](../../models/XBeach/) (stub) |
| 항만 공명·다중 반사 | Boussinesq (Funwave 등) | (별도 모델 추가 검토) |
| 통합 풍파·조석·표사 시뮬 | Delft3D-WAVE + FLOW | [`models/Delft3D/`](../../models/Delft3D/) (stub) |

## 2. 한국 적용 표준 흐름 — Nested SWAN

(`swan-library-firesinger` WINK 패턴, [`04-code-and-tools.md` §2.4](04-code-and-tools.md))

```
Layer 0: WW3 글로벌 hindcast (외해 spectrum)
   ↓ NESTOUT
Layer 1: SWAN coarse (한국 인근, 0.05° 격자)
   ↓ NESTOUT
Layer 2: SWAN middle (WINK 영역, 0.005° = ~500 m)
   ↓ NESTOUT
Layer 3: SWAN detail (사용자 정의, ~50-100 m, 항만·연안)
   ↓
검증: MPT/TW 정점 H_s·T_p·방향 비교
```

각 layer 입력:
- **수심**: BADA2024/GEBCO (외해) + 대표수심_MSL.parquet (사용자, 정밀 연안)
- **바람**: JMA-MSM 5 km (`swan-library-firesinger/tools/build_jma_uv_monthly.py`)
- **경계 spectrum**: 상위 layer NESTOUT 또는 spectrum_archive (`05-examples.md` §6)
- **조류** (선택): EFDC 또는 ADCIRC 출력 (`concepts/currents/06-model-application.md`)
- **수위** (선택): 약최고고조면 (AHHW) 보정 — `tools/build_ahhw_depths.py`

## 3. SWAN — Holthuijsen Ch.9 canonical

> **Canonical**: [`models/SWAN/`](../../models/SWAN/) + [`textbook/notes/waves-holthuijsen-toc.md`](../../textbook/notes/waves-holthuijsen-toc.md) §Ch.9
>
> Holthuijsen이 SWAN 공동 개발자라 Ch.9 전체가 algorithmic reference.

### 3.1 입력 카드 (요약)

상세는 [`models/SWAN/manual-notes/`](../../models/SWAN/manual-notes/) (작성 예정):

- `MODE STATIONARY/NONSTATIONARY` — 시간 모드
- `CGRID REGULAR/CURVILINEAR/UNSTRUCTURED` — 계산 격자
- `INPGRID BOTTOM/WIND/CURRENT/...` — 입력 격자
- `BOUND SPECTRUM FILE` — 경계 스펙트럼 입력
- `WIND` — 바람 강제
- `FRICTION` — 저면 마찰 옵션 (JONSWAP/Madsen/Collins)
- `BREAKING` — 깊이 유도 쇄파 (Battjes-Janssen 등)
- `OUTPUT BLOCK/SPECOUT/TABLE` — 출력

### 3.2 사용자 WINK 패턴

13개 한국 연안 middle 도메인 + detail 도메인 (`swan-library-firesinger/metadata/`). 사용자 본인이 운용 중이라 검증된 입력 set.

상세는 [`models/SWAN/source-analysis/wink-pattern.md`](../../models/SWAN/source-analysis/) (작성 예정).

### 3.3 spectrum_archive (재사용)

3-layer 비전:
1. WINK-compatible baseline
2. General coastal spectrum archive (임의 detail boundary)
3. Suitability checker

→ 새 프로젝트마다 외부 SWAN 재실행 불필요 (사용자 비전).

## 4. WAVEWATCH III (WW3)

> Canonical: `models/WW3/` (미생성, TBD)

- 한국 적용: 외해 forcing 계산 → SWAN nested
- 직접 사용 사례 드물 (한국에서는 SWAN이 표준 nearshore tool)

## 5. XBeach

> Canonical: [`models/XBeach/`](../../models/XBeach/) (stub)

- 폭풍 침식·범람 사례 (10²-10³ km² 도메인, 시간 1-7 일)
- 입력: 외부 spectrum (SWAN 출력 또는 직접 measurement)
- 출력: 모래사장 단면 변화, 침수 범위, 인프라 피해 분석

## 6. Delft3D-WAVE (D3D-4 또는 FM)

> Canonical: [`models/Delft3D/`](../../models/Delft3D/) (stub)

- D3D-4 WAVE = SWAN 통합 (Delft3D-FLOW + WAVE coupling)
- Delft3D FM (WAVE 부분 D-Waves)

## 7. 검증 (한국 사례)

### 7.1 검증 정점

- **MPT 74 정점** ([`05-examples.md` §1](05-examples.md)):
  - MOF (해양수산부) 34
  - KMA (기상청) 29
  - KHOA (국립해양조사원) 11
- **TW (KHOA 파랑 정점)**: 추가 60+ 정점

### 7.2 검증 메트릭

| 메트릭 | 정의 | 일반 기준 |
|---|---|---|
| RMSE H_s | √mean((Hs_model - Hs_obs)²) | < 0.3 m for typical |
| Bias H_s | mean(Hs_model - Hs_obs) | |bias| < 0.1 m |
| Pearson r (H_s) | 상관계수 | > 0.85 |
| RMSE T_p | √mean((Tp_model - Tp_obs)²) | < 1.5 s |
| Pearson r (T_p) | 상관계수 | > 0.7 |
| 방향 평균 절대 오차 | mean|Δθ| | < 20° |

### 7.3 사용자 축산항 사례

축산항 SWAN 시뮬 검증:
- MPT238 영덕(고래불, ~7.5 km), TW_0095 고래불해수욕장(~7.7 km)
- 자료: `swan-library-firesinger/metadata/validation_stations_chuksan.csv`

## 8. 다른 토픽과의 교차

- **tides** (`concepts/tides/`): 약최고고조면 (AHHW) 보정 — SWAN 수심 갱신 시 [`02-theory.md §8.2`](../tides/02-theory.md) DL+Z₀ 적용
- **currents** (`concepts/currents/`): SWAN current input (조류 → 파 분산 보정)
- **sediment-transport** (미작성): SWAN 출력 (radiation stress) → XBeach·SED 모델 연쇄
- **storm-surge** (미작성): SWAN + EFDC/ADCIRC + bottom friction coupling

## 9. 보강 — `verified` 승격 체크리스트

- [ ] `models/SWAN/manual-notes/` — Holthuijsen Ch.9 + SWAN UserManual 입력 카드 상세
- [ ] `models/SWAN/source-analysis/wink-pattern.md` — 사용자 WINK 13개 도메인 분석
- [ ] `models/SWAN/source-analysis/jma-msm-wind-workflow.md` — 사용자 바람 파이프라인
- [ ] `models/SWAN/web-refs/swan-official-resources.md` — 공식 사이트·논문 인용
- [ ] `models/WW3/` 새 디렉토리 생성 + 정체카드
- [ ] `models/XBeach/manual-notes/` — XBeach surfbeat·non-hydrostatic 모드
- [ ] 한국 축산항 SWAN 검증 사례 → `experience/` (RMSE·Bias·correlation 정량)

## 10. 연결

- `01`~`05` — 도메인 지식
- 모델별 canonical (`models/`):
  - [`models/SWAN/`](../../models/SWAN/) (stub, 활발히 작성 예정)
  - `models/WW3/` (미생성)
  - [`models/XBeach/`](../../models/XBeach/) (stub)
  - [`models/Delft3D/`](../../models/Delft3D/) (stub)
- 소스 노트:
  - [`textbook/notes/waves-holthuijsen-toc.md`](../../textbook/notes/waves-holthuijsen-toc.md) — Holthuijsen Ch.9 SWAN canonical
- 외부:
  - SWAN: [https://swanmodel.sourceforge.io/](https://swanmodel.sourceforge.io/)
  - WW3: [github.com/NOAA-EMC/WW3](https://github.com/NOAA-EMC/WW3)
  - XBeach: [xbeach.readthedocs.io](https://xbeach.readthedocs.io/)
  - `swan-library-firesinger` (사용자 본인 SWAN 인프라)
