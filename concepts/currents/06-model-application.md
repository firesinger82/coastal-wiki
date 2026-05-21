---
title: "조류 — 06 모델 적용"
topic: currents
canonical_source: self
citation_status: source-needed
verification_method: "AI cross-reference. 본 문서는 요약 + 링크 중심 ([CONVENTIONS.md §3] canonical source 분리). 각 모델의 조류 입력·출력 디테일은 `models/<model>/` (현재 stub)이 진실의 원천. 채워짐에 따라 source-needed → verified."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: ""
verification_date: ""
---

# 조류 — 06 모델 적용

> **Canonical source 규칙** ([CONVENTIONS.md §3](../../CONVENTIONS.md)): 모델 메커닉은 `models/<model>/`이 진실의 원천. 본 페이지는 요약 + 링크만.

조위 ([`concepts/tides/06-model-application.md`](../tides/06-model-application.md))와 동일한 모델군이 조류도 함께 출력·입력. 본 페이지는 조류 특화 항목.

## 1. 모델별 조류 입출력

### 1.1 분조 forcing (Harmonic Current Boundary)

외해 개경계에서 조류 분조 forcing:
- 각 경계 셀에 분조별 (u_Lsmaj, u_Lsmin, u_θ, u_g) 4 parameter 또는 (u_진폭, u_위상, v_진폭, v_위상) 입력
- 데이터 출처: **TPXO·FES** (u, v 분조 모두 제공), **KHOA 수치조류도** (한국 해역 한정), 자체 ADCP 관측 조화분해

### 1.2 시계열 forcing (Time-series Current Boundary)

외해 경계 점에 (u(t), v(t)) 시계열 직접 입력. 비조석 효과 (해류·바람 흐름) 포함 시 사용.

### 1.3 모델 출력 조류 분석

모델 결과의 조류 (u, v) 시계열을 UTide 2D로 후처리 → 검증·진단:
- 분조별 (Lsmaj, Lsmin, θ, g) 추출
- 관측 ADCP·수치조류도 격자와 비교
- 잔류 흐름·비선형 분조 평가

## 2. EFDC

> Canonical: [`models/EFDC/`](../../models/EFDC/) (현재 stub)

### 2.1 조류 forcing

- 분조 forcing 또는 시계열 forcing 둘 다 지원
- 입력: `efdc.inp` 경계 카드 + `pser.inp` (수위 시계열) + 자체 보조 파일
- 정확한 카드명·포맷은 [`models/EFDC/manual-notes/`](../../models/EFDC/manual-notes/) (미작성) 채워지면 인용

### 2.2 조류 출력

- EFDC는 (u, v, w) 3D 흐름 출력 — 수직 평균 또는 층별
- 분석: snapshot 매 시간 / 시계열 추출 후 UTide 2D
- 검증: KHOA 수치조류도 격자 또는 ADCP 관측

→ EFDC 조류 적용 워크플로 상세는 `models/EFDC/source-analysis/` 채워지면 보강.

## 3. ADCIRC

> Canonical: [`models/ADCIRC/`](../../models/ADCIRC/) (현재 stub)

- `fort.15` 경계 분조 카드 (NBFR + amplitude·equilibrium argument)
- ADCIRC tidal database가 임의 mesh 경계점에 분조 보간 (조위 + u, v 분조 함께)
- → [`models/ADCIRC/web-refs/adcirc-tidal-database.md`](../../models/ADCIRC/web-refs/) (미작성) 보강

## 4. Delft3D

> Canonical: [`models/Delft3D/`](../../models/Delft3D/) (현재 stub)

- D3D-4 FLOW: `.bnd`, `.bca` (boundary, harmonic constituents) — 조위·조류 분조 직접 입력
- Delft3D FM: unstructured mesh, 동일 분조 지원

## 5. XBeach

> Canonical: [`models/XBeach/`](../../models/XBeach/) (현재 stub)

XBeach는 단기 폭풍 모델. 조류는 보통 수위 시계열 forcing의 부산물 또는 별도 background 흐름.

## 6. 글로벌 모델에서 조류 데이터 추출

[`concepts/tides/04-code-and-tools.md` §6](../tides/04-code-and-tools.md) 글로벌 모델별 조류 제공 여부:

| 모델 | 조류 (u, v) | 주 사용처 |
|---|---|---|
| **TPXO** | ✓ | 외해 분조 forcing 표준 |
| **FES2022** | ✓ (eastward·northward) | 유럽·CNES 미션 + 외해 forcing |
| **NAO.99Jb** | ✓ | 일본·한국 동해 권장 |
| **GOT5** | × (elevation only) | 위성 altimetry 보정 |
| **KHOA 수치조류도** | ✓ (단일 성분) | **한국 황해·남해 권장** (동해 미커버) |

→ pyTMD (`concepts/tides/04-code-and-tools.md` §5)는 조류 (u, v) 추출 지원.

## 7. 한국 해역 조류 forcing 권장

| 영역 | 외해 경계 forcing | 검증 |
|---|---|---|
| 서해 (황해) | **KHOA 수치조류도** (1°×1° 영역 3500+ 격자) | KHOA OpenAPI ADCP 관측 |
| 남해 | KHOA 수치조류도 + TPXO10 (보조) | KHOA 관측 |
| 동해 | **NAO.99Jb** (KHOA 수치조류도 미커버) | KHOA 관측 |
| 동중국해 | TPXO10 또는 KHOA 수치조류도 | — |

> 한국 EFDC·ADCIRC 시뮬에서 **혼합 forcing 권장**:
> - 황해 connectivity: KHOA 수치조류도
> - 외해 (동해·동중국해 경계): NAO.99Jb 또는 TPXO10
> - 두 datum + 위상 기준 일치 확인 필수

## 8. 모델 검증 — 조류 specific

| 항목 | 방법 |
|---|---|
| 분조별 진폭 정합 | UTide(모델 출력) vs KHOA 수치조류도 격자값 ±20% |
| 분조별 위상 정합 | 위상 기준 (G/g) 일치 후 ±10° 이내 |
| 잔류 흐름 | 모델·관측 시계열 평균 비교 |
| 창·낙조류 비대칭 | 비선형 분조 (M₄·MS₄) 진폭 비교 |
| Hodograph (vector trace) | 시각적 패턴 정합 (왕복성/회전성) |

## 9. 보강 — `verified` 승격 체크리스트

- [ ] `models/EFDC/manual-notes/` 작성 — §2 정확한 카드명·포맷
- [ ] `models/EFDC/source-analysis/` — 경계 처리 서브루틴 분석
- [ ] `models/ADCIRC/web-refs/adcirc-tidal-database.md` — u, v 분조 활용
- [ ] `models/Delft3D/manual-notes/` — `.bca` 조류 분조 포맷
- [ ] 한국 적용 사례 1건 verified (서해 EFDC 또는 동해 NAO.99Jb forcing)

## 10. 연결

- `01`~`05` — 조류 도메인 지식
- [`concepts/tides/06-model-application.md`](../tides/06-model-application.md) — 조위 모델 적용 (동일 모델군)
- `models/EFDC/`, `models/ADCIRC/`, `models/XBeach/`, `models/Delft3D/` — canonical source (stub)
- `concepts/tides/04-code-and-tools.md` §6 — 글로벌 조석/조류 모델
