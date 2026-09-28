---
title: "KHOA 수치조류도 조화상수 CSV — `지각` = g(135°E), `진폭·지각` = 남북(v) 성분 (데이터 검정)"
topic: currents
canonical_source: self
citation_status: verified
verification_method: "AI programmatic validation: (1) data.go.kr 파일데이터 15145955 '해양수산부 국립해양조사원_수치조류도 기반 조화상수_20250814.csv'(cp949, 813,703행, 14분조 진폭·지각 + 좌표) — CSV 헤더와 포털 컬럼 설명('조화상수의 지각정보') 모두 위상 기준 미기재를 2026-09-28 직접 확인. (2) 조위 G 위상 = [[khoa-49-station-16yr-utide-2026]] 의 49정점 16년 UTide(UTC 입력) 결과, KHOA 공표 pha_kst−9a 와 0.2–0.5° 이내 일치. (3) 정점별 최근접 격자점(≤5 km, 44정점) 에서 8분조(M2 S2 N2 K2 K1 O1 P1 Q1) 조류 위상 − 조위 G 위상을 비교 — 교차 대역 6쌍 + 시간대 오프셋 H 스캔(0–24 h, 0.25 h 간격) + 부트스트랩 10,000회. 스크립트·입력표·출력: tools/khoa-validation/current_phase_reference_test.py, results/current_phase_reference_rows.csv, results/current_phase_reference_test.txt. (4) 성분 판별(2026-09-28 추가): data.go.kr 파일데이터 15130143 해양수산부_수치조류도(예측 유속·유향 연도별 CSV, 지점당 하루 1표본) 과 동일 격자 대조 — ½ΣA²(S2 제외 13분조) 대 예측 u·v·장축·전체 분산 비(2021-2024, 연 2,005-2,020점) + UTide FUV 로 CSV 분조 합성 후 표본시각 스캔 상관(2024, 142점). 스크립트 tools/khoa-validation/current_component_test.py, 출력 results/current_component_test.txt. (5) API 시각 지정 대조(2026-09-28 추가): KHOA 바다누리 OpenAPI tidalCurrentArea 를 2024-04-21~22 매시 48회(126.0–126.3E·36.0–36.3N, 209점) 호출 — CSV 13분조 UTide 합성 v 와 API 벡터 비교, API 시각 KST/UTC 두 가정. 스냅샷 results/current_api_snapshots_20240421-22.csv, 스크립트 current_component_test.py api."
note_author: "Claude Opus 5.5 + 사용자 합의"
note_date: 2026-09-28
verification_by: "Claude Opus 5.5 — 3검정(교차쌍·오프셋 스캔·부트스트랩) + 포털 메타데이터 직접 확인"
verification_date: 2026-09-28
experience_evidence:
  repeated_observation: true   # 44 정점 독립 + 교차 대역 6쌍 모두 같은 방향 + 오프셋 스캔 단일 정점
  objective_data: true         # KHOA 공개 CSV(data.go.kr 15145955) + KHOA 조위 16년 UTide(공표값 대조 완료)
  reproducible: true           # tools/khoa-validation/current_phase_reference_test.py build/test
---

# KHOA 수치조류도 조화상수 — `지각` 은 g(135°E) 기준

> **3조건 통과** ([BOUNDARY.md](../BOUNDARY.md)):
> 1. 반복 관찰 ✓ — 44정점 독립, 교차 대역 6쌍 전부 같은 결론, 오프셋 스캔 정점 하나
> 2. 객관 데이터 근거 ✓ — KHOA 공개 CSV + KHOA 조위 16년 UTide(공표 조화상수와 대조 완료)
> 3. 재현 가능 ✓ — `tools/khoa-validation/current_phase_reference_test.py`

## 1. 질문

수치조류도 기반 조화상수 CSV 의 컬럼은 `m2_진폭`, `m2_지각` … 뿐이고, data.go.kr 컬럼 설명도
*"조화상수의 지각정보"* 이다. **지각이 그리니치(G)인지 한국 표준 135°E(g)인지 어디에도 적혀 있지 않다.**
두 기준은 분조별로 $g = G + 9a$ ($a$ = 각속도 °/h) 만큼 다르다 — M2 260.86°, K1 135.37°.
모델 조류를 UTide(UTC 입력 → G)로 분해해 이 CSV 와 비교할 때 기준을 틀리면 M2 위상이 약 261° 어긋난다.

## 2. 방법

같은 정점에서 조류 위상과 조위 위상의 차이 $\Delta_c = \phi^{cur}_c - \phi^{elev,G}_c$ 는
진행파(동위상)·정상파(±90°) 어느 쪽이든 **분조 대역이 달라도 비슷해야** 한다. CSV 가 g 기준이면
$\Delta_c$ 에 $9a_c$ 가 섞여 반일주조–일주조 사이에 약 125–140° 차이가 생긴다.

- 조위 G: 49정점 16년 UTide(UTC 입력) — KHOA 공표 `pha_kst − 9a` 와 0.2–0.5° 이내 일치 ([[khoa-49-station-16yr-utide-2026]]).
- 조류: 각 정점의 최근접 격자점(≤ 5 km). 중앙 거리 0.52 km, **44정점 사용**.
- 장축 부호 모호성(180°)은 각도를 두 배로 해 원형 평균으로 처리.

## 3. 결과

**교차 대역 6쌍** — $(\Delta_a - \Delta_b) \bmod 180$ 의 원형 평균:

| 쌍 | 관측 평균 | G 가설 기대 0° 와의 차 | g 가설 기대값 | g 와의 차 |
|---|---|---|---|---|
| M2–K1 | 141.5° | 38.5° | 125.5° | 16.0° |
| M2–O1 | 149.1° | 30.9° | 135.4° | 13.8° |
| S2–K1 | 149.2° | 30.8° | 134.6° | 14.6° |
| N2–O1 | 131.9° | 48.1° | 130.5° | **1.5°** |
| K2–P1 | 136.9° | 43.1° | 136.1° | **0.8°** |
| M2–Q1 | 135.1° | 44.9° | 140.3° | 5.1° |

6쌍 모두 g 가설 쪽이 가깝다.

**시간대 오프셋 스캔** — $\phi^{cur}_c - H\,a_c - \phi^{elev,G}_c$ 의 정점별 8분조 일관성(평균 R)을 $H$ = 0–24 h 로 훑음:

| H (h) | 0 | 3 | 6 | 8 | **9** | 10 | 12 |
|---|---|---|---|---|---|---|---|
| 평균 R | 0.654 | 0.300 | 0.598 | 0.799 | **0.830** | 0.811 | 0.644 |

최대는 **H = 9.00 h** (UTC+9 = 동경 135°). 기준을 가정하지 않고 스캔했는데 9 h 에서 정점이 나온다.

**부트스트랩** — 정점별 R(9h) − R(0h): 44정점 중 35정점에서 양수, 평균 +0.177, 95% 구간 [0.104, 0.248].

→ **CSV 의 `지각` 은 g(135°E, KST) 기준이다.** KHOA 공식 조석 위상 표준(동경 135° 기준 g)과 일치한다.

## 3b. `진폭`·`지각` 은 남북(v) 유속 성분이다

같은 격자의 KHOA 예측 유속·유향 아카이브(data.go.kr 15130143, 지점당 하루 1표본)와 대조했다.
유향은 진북 기준 시계방향(흐르는 방향)으로 보고 $u=s\sin\theta$, $v=s\cos\theta$.

**분산 대조** — CSV 의 $\tfrac12\sum A_c^2$ (S2 제외 13분조: 하루 1회 표본에서 S2 위상은 매일 같아 분산에 기여하지 않는다) 을
예측 성분 분산으로 나눈 비의 중앙값 [사분위]:

| 연도 | 지점 | v | u | 장축 | 전체 | log 상관 (v) |
|---|---|---|---|---|---|---|
| 2021 | 2,020 | **1.013** [0.979, 1.028] | 1.215 [0.78, 2.73] | 0.770 | 0.552 | 0.997 |
| 2022 | 2,020 | **0.990** [0.970, 1.011] | 1.240 | 0.770 | 0.546 | 0.996 |
| 2023 | 2,005 | **1.008** [0.969, 1.034] | 1.233 | 0.780 | 0.551 | 0.996 |
| 2024 | 2,012 | **1.014** [0.980, 1.041] | 1.249 | 0.788 | 0.556 | 0.996 |

**시계열 재구성** — UTide `FUV`(nodal·천문인수)로 CSV 13분조를 합성해 표본 시각을 0–24 h 훑었다(2024, 무작위 142점):
최적 시각에서 관측 **v 와 상관 중앙 0.990** [0.989, 0.991], RMSE 4.9 cm/s, **u 와는 −0.28**.

→ **CSV 는 남북 성분 하나만 담는다.** 예측 조류 자체는 회전성이다(연간 표본의 단축/장축 표준편차 비 중앙 0.45) —
동서 성분 없이는 이 CSV 로 조류 벡터·타원을 재구성할 수 없다. 모델 조류 검증에 쓸 때는 모델의 v 성분과만 비교해야 한다.

- 재구성 검정은 위상 기준을 따로 판별하지 않는다 — g↔G 변환은 표본 시각 9 h 이동과 수학적으로 같아 스캔이 흡수한다.
  위상 기준 근거는 §3(조위 대조)이다. 최적 시각 21 UTC 는 g 가정일 때의 값이다.
- 유향 규약(진북 기준 시계방향, 흐르는 방향)을 가정했다. 이 규약이 다르면 "v" 가 가리키는 물리 축도 달라진다.

## 3c. 시각을 지정한 API 대조 — API 는 KST, 유향은 흐르는 방향

KHOA 바다누리 OpenAPI `tidalCurrentArea` 로 같은 격자를 **시각을 지정해** 받았다(2024-04-21~22 매시 48회, 126.0–126.3°E·36.0–36.3°N, 209점).
CSV 13분조를 UTide `FUV` 로 합성($G = g - 9a$)해 API 벡터와 비교:

| API 시각 가정 | corr(합성, API v) | corr(합성, API u) | RMSE (v) |
|---|---|---|---|
| **KST** | **1.000** (최소 0.999) | 0.555 | **0.80 cm/s** |
| UTC | −0.099 | −0.872 | 48.15 cm/s |

- **API 의 `Date`·`Hour` 는 KST** 이고, CSV 를 g 로 읽을 때 API 예측을 반올림 수준(0.8 cm/s — API 유속은 정수)으로 재현한다.
  API 와 CSV 는 같은 조화상수에서 나온 산출물로 보인다. API 는 u·v 벡터를 주고, 공개 CSV 는 그중 v 만 담는다.
- **유향은 흐르는 방향(진북 기준 시계방향)** — 반대 규약이면 상관이 −1 이 된다. 백서 2025 도 *"유향은 진북을 기준으로"* 라 쓴다.
- 이 검정만으로는 "CSV=g·API=KST" 와 "CSV=G·API=UTC" 를 가를 수 없다(둘 다 같은 9 h 이동). §3 조위 대조가 CSV=g 를 정하므로 API=KST 가 따라 나온다.

## 4. 한계

- **정점 해상도는 약 ±1 h 수준** — 스캔 곡선이 8.5–9.5 h 에서 평평하다(0.821–0.830). 9 h 대 0 h 판별은 확실하지만,
  9 h 가 8.5 h 보다 낫다는 것은 이 검정만으로는 약하다. 135°E 라는 값 자체는 기관 표준에 기댄다.
- 분조 간 $\Delta_c$ 가 같다는 전제는 근사다(개별 쌍 R 0.60–0.67). 결론은 44정점 평균의 방향에 기댄다.
- 조위 G 는 16년 UTide 결과다(공표값과 대조 완료). KHOA 통합 DB(`khoa_harmonic_db.csv`)는 `g − G` 가 이론값 $9a$ 와
  **576행 전부** 어긋난다(M2 중앙 +7.5°, S2 +16.5°, K1 +8.2°, O1 −1.6°). 조위관측소 49정점에서 DB 의 G 열은 UTide G 와
  중앙 0.4° 로 일치하고 **g 열이 틀렸다** — 이 검정은 DB 를 쓰지 않았다.

## 5. 부수 발견 — 동해 연안은 수치조류도 밖이다

동해안 5정점은 최근접 격자점이 멀어 제외됐다: 묵호 158 km · 후포 59 km · 속초 171 km · 울릉도 172 km · 동해항 152 km.
CSV 의 경도 범위(117.59–129.97°E)가 동해안을 포함하는데도 격자가 없다 — **수치조류도는 동해 연안을 거의 덮지 않는다.**

## 6. 재현

```bash
cd tools/khoa-validation
# 성분 판별 (utide 필요, 원본 두 파일 필요). api 모드는 저장소 스냅샷만 있으면 된다(--fetch 시 KHOA_OCEANDATA_KEY 필요)
python3 current_component_test.py api --harm <조화상수.csv>
python3 current_component_test.py variance --harm <조화상수.csv> --pred <수치조류도.zip>
python3 current_component_test.py recon --harm <조화상수.csv> --pred <수치조류도.zip> --year 2024
# (1) 입력표 생성 — CSV 는 data.go.kr 15145955 에서 받는다(296 MB, 저장소 미포함)
python3 current_phase_reference_test.py build --csv <수치조류도_조화상수.csv> --utide <49정점 UTide JSON 디렉터리>
# (2) 검정 — 저장소의 입력표만으로 실행 가능
python3 current_phase_reference_test.py test
```

입력표 `results/current_phase_reference_rows.csv`(49정점 × 8분조 조위 G·조류 위상·진폭, 20 KB)는 저장소에 있으므로
(2) 단계는 원본 CSV 없이 재현된다. 기대 출력: `results/current_phase_reference_test.txt`.

## 7. 연결

- [[khoa-49-station-16yr-utide-2026]] — 조위 G 위상 출처
- `concepts/currents/05-examples.md` — 이 CSV 를 쓰는 예제(위상 해석 줄)
- `concepts/currents/03-analysis-methods.md` §1.3 — KHOA 공식 조류 분석 절차(위상 기준 g 서술)
