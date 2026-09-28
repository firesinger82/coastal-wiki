---
title: "KHOA 수치조류도 조화상수 CSV — `지각` 위상 기준 판별 (g = 135°E, 44정점 데이터 검정)"
topic: currents
canonical_source: self
citation_status: verified
verification_method: "AI programmatic validation: (1) data.go.kr 파일데이터 15145955 '해양수산부 국립해양조사원_수치조류도 기반 조화상수_20250814.csv'(cp949, 813,703행, 14분조 진폭·지각 + 좌표) — CSV 헤더와 포털 컬럼 설명('조화상수의 지각정보') 모두 위상 기준 미기재를 2026-09-28 직접 확인. (2) 조위 G 위상 = [[khoa-49-station-16yr-utide-2026]] 의 49정점 16년 UTide(UTC 입력) 결과, KHOA 공표 pha_kst−9a 와 0.2–0.5° 이내 일치. (3) 정점별 최근접 격자점(≤5 km, 44정점) 에서 8분조(M2 S2 N2 K2 K1 O1 P1 Q1) 조류 위상 − 조위 G 위상을 비교 — 교차 대역 6쌍 + 시간대 오프셋 H 스캔(0–24 h, 0.25 h 간격) + 부트스트랩 10,000회. 스크립트·입력표·출력: tools/khoa-validation/current_phase_reference_test.py, results/current_phase_reference_rows.csv, results/current_phase_reference_test.txt."
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

## 4. 한계

- **정점 해상도는 약 ±1 h 수준** — 스캔 곡선이 8.5–9.5 h 에서 평평하다(0.821–0.830). 9 h 대 0 h 판별은 확실하지만,
  9 h 가 8.5 h 보다 낫다는 것은 이 검정만으로는 약하다. 135°E 라는 값 자체는 기관 표준에 기댄다.
- **`진폭` 이 어느 성분인지(장축 유속? u/v?)는 풀리지 않는다** — 이 검정은 위상만 쓴다.
- 분조 간 $\Delta_c$ 가 같다는 전제는 근사다(개별 쌍 R 0.60–0.67). 결론은 44정점 평균의 방향에 기댄다.
- 조위 G 는 16년 UTide 결과다(공표값과 대조 완료). KHOA 통합 DB(`khoa_harmonic_db.csv`)의 G 열은
  `g − G` 가 이론값 $9a$ 와 정점마다 어긋나(M2 중앙값 268.3° 대 260.86°) 이 검정에 쓰지 않았다.

## 5. 부수 발견 — 동해 연안은 수치조류도 밖이다

동해안 5정점은 최근접 격자점이 멀어 제외됐다: 묵호 158 km · 후포 59 km · 속초 171 km · 울릉도 172 km · 동해항 152 km.
CSV 의 경도 범위(117.59–129.97°E)가 동해안을 포함하는데도 격자가 없다 — **수치조류도는 동해 연안을 거의 덮지 않는다.**

## 6. 재현

```bash
cd tools/khoa-validation
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
