---
title: "KHOA Annual Report 2019 §3 — 태풍 링링 (Lingling, 제13호) + 미탁 (Mitag, 제18호) 서해안 surge"
source_id: khoa-annual-reports
chapter: "§3 자료 분석 결과 — line 2892 최저기압 정성 + line 3576 5 태풍 영향 + 표 3-48·3-49 인천 조위 9-10월 spike"
pages: "—"
page_offset_applied: false
topic: storm-surge
canonical_source: self
citation_status: verified
verification_method: "E:\\KHOA_연간백서\\markdowns\\Annual_Report(2019).md 직접 인용 — line 2892 (서해안 최저기압 -10.7 hPa 누년대비 + 링링·미탁 영향), line 3576 (2019년 한반도 영향 5 태풍 식별), line 4244-4262 (표 3-49 인천 9월 고극조위 957 cm vs 누년 946 cm = +11 cm 편차)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — markdown 직접 인용"
verification_date: 2026-06-01
related:
  - concepts/storm-surge/05-examples.md
  - textbook/notes/khoa-annual-2012-bolaven-surge.md
  - textbook/notes/khoa-annual-2022-hinnamnor-surge.md
---

# KHOA Annual Report 2019 §3 — 태풍 링링 2019 서해안 + 미탁 한반도 상륙 surge

> 출처: `E:\KHOA_연간백서\markdowns\Annual_Report(2019).md`, source_id `khoa-annual-reports`.

## 1. Case 식별

| 항목 | 값 | 출처 |
|---|---|---|
| 2019년 한반도 영향 태풍 | **5개** (다나스 5호 / 프란시스코 8호 / **링링 13호** / 타파 17호 / **미탁 18호**) | KHOA 2019 line 3576 |
| 링링 (LINGLING) 경로 | **서해안 진입** | KHOA 2019 line 2892 |
| 미탁 (MITAG) 경로 | **한반도 상륙** | KHOA 2019 line 2892 |
| 서해안 최저기압 누년대비 (2019) | **-10.7 hPa** (링링·미탁 영향) | KHOA 2019 line 2892 |
| 한반도 전 해역 최저기압 (2019) | 967.8 hPa (누년 평균 +0.6 hPa) | KHOA 2019 line 2892 |

KHOA 본문 정성 인용 (line 2892):

> "한반도 전 해역의 2019년 최고기압의 평균은 1037.6 hPa로 나타났고, 누년 대비 1.9 hPa 낮았다. 최저기압의 경우 967.8 hPa로 산정되었으며, 누년평균 대비 0.6 hPa 높게 나타났다. 해역별로는 **서해안에서 ­10.7 hPa 낮게 나타났는데, 이는 태풍(서해안으로 진입한 제13호 태풍 링링(LINGLING), 한반도에 상륙했던 제18호 태풍 미탁(MITAG) 등)의 영향**으로 판단된다."

> "2019년에 발생한 태풍 중 한반도에 큰 영향을 준 태풍의 개수는 총 5개(다나스(제5호), 프란시스코(제8호), 링링(제 13호), 타파(제17호), 미탁(제18호))임" (line 3576)

## 2. 인천 조위관측소 9-10월 surge spike (표 3-48 + 3-49, line 4244-4262)

2019년 월별 인천 조위관측소 고극조위 (단위 cm):

| 월 | 2019 고극조위 | 누년 평균 | 편차 |
|---|---|---|---|
| 1월 | 934.0 | 904.6 | +29.4 |
| 2월 | 923.0 | 912.3 | +10.7 |
| 6월 | 899.0 | 930.2 | -31.2 |
| 7월 | 927.0 | 943.6 | -16.6 |
| 8월 | 944.0 | 954.8 | -10.8 |
| **9월** | **957.0** | **946.0** | **+11.0** ← **링링 (2019-09-07 서해 통과)** |
| **10월** | **954.0** | **940.8** | **+13.2** ← **미탁 (2019-10-02 상륙)** |
| 11월 | 909.0 | 933.2 | -24.2 |
| 12월 | 886.0 | 908.4 | -22.4 |

핵심: 8월 -10.8 cm 음의 편차에서 **9월 +11.0 / 10월 +13.2 cm 양의 편차로 전환** — Lingling (9월) + Mitag (10월) 연달아 서해안 영향의 정량 신호. 11월 -24.2 cm 로 다시 음의 편차.

**Bolaven 2012 vs Lingling 2019 서해 case 대비** (모두 서해 통과 패턴):
- Bolaven 2012-08-29: 군산 외해 ADCP 잔차류 (KHOA 2012 vol.1 §7.3, [[khoa-annual-2012-bolaven-surge]])
- Lingling 2019-09-07 + Mitag 2019-10-02: 인천 조위 +11/+13 cm 편차 spike (KHOA 2019 §3 직접)

두 case 가 모두 서해안 surge 패턴이지만 자료 형태 다름 (전자: 외해 잔차류, 후자: 조위 정점 편차).

## 3. 본 위키 storm-surge 적용

### 3.1 storm-surge 5 인자 매핑

| Pugh §6 인자 | 링링·미탁 2019 매핑 |
|---|---|
| §2.1 IB (대기압 surge) | 서해안 최저기압 -10.7 hPa 누년대비 → IB 양의 기여 |
| §2.2 Wind stress | 서풍·북서풍 → 인천 조위 wind set-up |
| §2.3 Tide-surge interaction | 인천 천해 (~15 m) 강한 비선형 |
| §2.4 Wave setup | 서해안 wave fetch 제한 (Bolaven 2012 와 동일) |
| §2.5 Coriolis | 북상 typhoon + Coriolis → 우측 강풍 (서해안) |

### 3.2 [[01-concept]] §3.2 Lingling 항목 verified 가능

기존: "Lingling (링링) | 2019 | 서해 북상 | ~1.0 m 인천 (source-needed)"

→ KHOA 2019 인천 9월 고극조위 957 cm = 누년대비 **+11 cm 편차 (=0.11 m)**. ~1.0 m 가 surge peak 전체이면 대조기 천문조 + IB + wind set-up 의 합이며, 편차 +11 cm 는 추세 비교만 가능. 직접 surge peak 매핑은 시간별 데이터 (KHOA 2019 § 시계열 또는 KHOA 2019 §3 조위편차 별표) 필요.

## 4. 인용 정형

- `(KHOA Annual Report 2019 §3, line 2892)` — 서해안 최저기압 -10.7 hPa + 링링·미탁 정성
- `(KHOA Annual Report 2019 §3, line 3576)` — 2019 5 태풍 식별
- `(KHOA Annual Report 2019 표 3-49)` — 인천 9월 +11 cm / 10월 +13.2 cm 편차

source_id 매니페스트: [`textbook/sources.yml`](../sources.yml) — `khoa-annual-reports`.

## 5. 한계

- **시간별 surge 시계열 부재** — 표 3-49 는 월별 통계만. 9월·10월 시간별 peak 는 별도 source (KHOA OpenAPI archive 도 1년 한계로 불가)
- 다나스·프란시스코·타파 (5호·8호·17호) 영향은 본 노트 미조사
- Lingling vs Mitag 각각의 단독 기여 분리 불가 (월별 통계는 합산)

## 6. 연결

- [[khoa-annual-2012-bolaven-surge]] — 서해 case 비교 (외해 ADCP)
- [[khoa-annual-2022-hinnamnor-surge]] — 동해 case 비교 (조위 정점)
- [`concepts/storm-surge/05-examples.md §4 추가 한국 case`](../../concepts/storm-surge/05-examples.md) — Lingling 항목
- [[khoa-annual-reports-overview]] — KHOA 백서 통합 §
