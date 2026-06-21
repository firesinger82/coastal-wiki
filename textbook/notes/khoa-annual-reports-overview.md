---
title: "KHOA 국가해양관측망 연간백서 2012-2025 — 통합 개관"
source_id: khoa-annual-reports
chapter: "15권 통합 개관 (Annual Report 2012-2025)"
pages: "—"
page_offset_applied: false
topic: khoa-official
canonical_source: self
citation_status: verified
verification_method: "AI cross-reference against  15 .md files (총 188,929 줄). 2025 보고서 구조 + 조석 비조화 공식 정의 confirmed."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-23
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-23
---

# KHOA 국가해양관측망 연간백서 (2012-2025)

> 출처: `khoa-annual-reports` = `` (15권, 188,929 줄 markdown)

## 1. 백서 list

| 연도 | 파일 | 줄 수 |
|---|---|---|
| 2012 vol.1 | Annual_Report(2012.vol.1).md | 10,985 |
| 2012 vol.2 | Annual_Report(2012.vol.2).md | 2,606 |
| 2013 | Annual_Report(2013).md | 11,793 |
| 2014 | Annual_Report(2014).md | 8,800 |
| 2015 | Annual_Report(2015).md | 8,310 |
| 2016 | Annual_Report(2016).md | 10,791 |
| 2017 | Annual_Report(2017).md | 11,009 |
| 2018 | Year_report(2018).md | 11,450 |
| 2019 | Annual_Report(2019).md | 16,720 |
| 2020 | Annual_Report(2020).md | 18,418 |
| 2021 | Annual_Report(2021).md | 18,849 |
| 2022 | Annual_Report(2022).md | 18,816 |
| 2023 | Annual_Report(2023).md | 13,433 |
| 2024 | Annual_Report(2024).md | 12,859 |
| 2025 | Annual_Report(2025).md | 14,090 |

> 2020-2022 가장 두꺼움 (~18K 줄). 2018-2019 사이에 보고서 형식 일부 변경 가능 (Year_report → Annual_Report).

## 2. 표준 구조 (2025 기준)

각 백서 3 챕터:

### 제1장 국가해양관측망 현황 — 정점 인벤토리
- (1) 조위관측소 (`tideObs`, DT_xxxx 코드)
- (2) 해양관측소 (KMA·MOF·KHOA buoy)
- (3) 해양관측부이 (주요해역·항로)
- (4) 해수유동관측소 (HF-Radar)
- (5) 해양과학기지 (이어도·소청초·가거초)

### 제2장 자료수집 현황 — 정점별 수집률·결측
- 각 정점 가동률·결측 통계
- 통신·장비 fail 사례

### 제3장 자료 분석 결과 — 연간 climate 통계
- (1) 조위 (조화상수·비조화상수)
- (2) 기압·기온·수온·염분
- (3) 바람 (풍향·풍속)
- (4) 파랑 (파고·파주기·파향)
- (5) 해수유동
- (6) 유의파고 (별도)

## 2A. 관측망 분류·관측 표준·자료 품질관리(QC) — KHOA 공식 (2025 발췌)

> reference 자료. 출처 `khoa-annual-reports`, Annual Report 2025 제1장·제2장.

### 2A.1 국가해양관측망 정의·정점 분류 (5종)

국가해양관측망 = "해양관측을 실시하고, 해양관측 자료를 수집·가공·저장·검색·표출·송수신·활용할 수 있도록 구축·운영하는 해양관측시설의 조합" (Annual Report 2025 L1515). **2025.12 기준 총 140개소**(정보공개 120 + 공개제한 20) 운영 (L1515, 표 1-1 L1517).

| 구분 | 정점 수 (2025) | 비고 |
|---|---|---|
| ① 조위관측소 | 55 (서28·남19·동8) | 조위·기압 필수, 수온/염분/기온/바람 선택 (L1535) |
| ② 해양관측소 | 2 | |
| ③ 해양관측부이 | 주요해역·이안류·주요항로 3유형 | 수집주기 유형별 상이(아래) |
| ④ 해양과학기지 | 3 | 이어도·소청초·가거초 |
| ⑤ 해수유동관측소(HF-Radar) | 32 | radial→total vector 1시간 합성 |

**조위관측장비 4종** (L1537): 디지털부표식(D.부표식, 검조우물, 인천·목포·진도 등 17개소) / 레이더식(극초단파 Microwave, 강화대교·장항 등 검조우물 곤란지) / 레이저식 / 압력식(Water Pressure). 제주·목포·부산 등 **32개소는 2종 이상 듀얼 조위계** 운용(비교검증).

### 2A.2 자료수집 주기 표준 (표 2-1, L1904–1916, 단위 분)

| 시설 | 조위 | 기압/기온/수온 | 바람 | 파랑 | 해수유동 |
|---|---|---|---|---|---|
| 조위관측소 | 1 | 1 | 1 | — | — |
| 해양관측소 | 1 | 1(수온/염분 미설치) | 1 | 20 | — |
| 해양관측부이 주요해역 | — | 30 | 30 | 30 | 30 |
| 해양관측부이 이안류 | — | 5 | 5 | 5 | 5 |
| 해양관측부이 주요항로 | — | 10 | 10 | 10 | 10 |
| 해수유동관측소 | — | — | — | — | 60 |
| 해양과학기지 | 1 | 1 | 1 | 20 | — |

### 2A.3 자료 품질관리(QC) 수집률 공식 (L1919–1935)

해양관측자료 DB의 **2차 품질처리 완료 자료**를 재분석, 결측 제외·정상/오측 구분하여 관측항목별·월별 산정. 6개 개수 정의 + 4개 율 공식:

- 이론수집 = 관측주기상 수집되어야 할 개수 / 실제수집 = 수집된 개수 / 정상 = 결측·오류 미분류 / 오류 = 품질검사 오류 / 결측 = 수집됐으나 NULL / 미수집 = 이론−실제.
- **자료수집률(%)** = (실제수집 / 이론수집) × 100
- **정상자료율(%)** = ((실제수집 − 결측 − 오류) / 이론수집) × 100
- **결측자료율(%)** = ((결측 + 미수집) / 이론수집) × 100
- **오류자료율(%)** = (오류 / 이론수집) × 100

**분석 제외 임계**: 정상자료율 **80% 미만** 자료 + 품질이상 자료는 분석 제외. **단 해수유동관측소(HF-Radar)는 정점별 정상자료율 50% 미만 제외** (L1935). 누년 = 과거 10년 월통계 중 정상수집률 80%↑ 월만 산입(10년 미만은 관측개시~전년, L2406).

> **연혁 변형**(survey): 2013/2018 백서는 QC 지표가 "원시자료/정상자료 수집률" 2개 + 목표/수집/결측/이상 자료수 용어였으나, 2022→2025에서 이론/실제수집 기반 4지표 체계로 재정의. 비조화상수도 약최저저조면이 2013 미수록→2018+ 추가.

## 3. 조위 조화상수·비조화상수 공식 (2025 보고서 발췌)

(KHOA 공식 정의 확인 — `tides-khoa-nonharmonic-research.md` 와 정합)

| 한글명 | 영문명 | 계산식 |
|---|---|---|
| 천문조평균해수면 | Mean Sea Level (M.S.L.) | (M2+S2+K1+O1 등) |
| **약최고고조면** | **Approx. Highest High Water** | MSL + Z₀ |
| **대조차** | Spring Range | 2·(H_M2 + H_S2) |
| 평균조차 | Mean Range | 2·H_M2 |
| 소조차 | Neap Range | 2·(H_M2 − H_S2) |
| **약최저저조면** | **Approx. Lowest Low Water** | MSL − Z₀ |
| 조석형태수 | Form Factor | (H_K1 + H_O1)/(H_M2 + H_S2) |

### 3.1 조석형태수 — 한국 공식 분류 (KHOA 2025 인용)

> **0 – 0.25**: 반일주조형 (semidiurnal)
> **0.25 – 1.50**: 반일주조가 우세한 혼합형 (mixed mainly semidiurnal)
> **1.50 – 3.00**: 일주조가 우세한 혼합형 (mixed mainly diurnal)
> **3.00 이상**: 일주조형 (diurnal)

→ DASHBOARD research doc 의 공식과 **완전 일치**. 또 하나의 KHOA 공식 source 확보.

### 3.2 KHOA 표준 — 62개 조화상수

각 정점 분석은 **62개 조화상수**를 표준으로 산출 (Annual Report 2025 §3.1 표 3-25, 3-28, 3-31 등에서 확인). 주요 4대분조 + satellite·천해 비선형 분조 다수. Foreman 1977 appendix (146 분조)의 부분집합.

## 4. 2025년 한국 wave climate (Annual Report §3.19 발췌)

| 통계 | 값 (m) | 비고 |
|---|---|---|
| 월별 최대 유의파고 평균 | **3월 3.97 m** | 전 해역 평균 |
| 해역별 최대 (3월) | **동해안 4.55 m** | |
| 누년 편차 (2025 − 누년) | 전반적 음의 편차 | 2025 = lower wave activity year |
| 가장 큰 음의 편차 | **9월 −4.37 m** | 태풍 시즌 |

→ 14년 시계열 추적 시 한국 wave climate change 정량 가능.

## 4. 활용 — 각 토픽별

### 4.1 tides
- 정점별 조화·비조화 연간 통계 (DASHBOARD 자료와 cross-check)
- 약최고/저조면 시계열 (장기 추세)
- 조석형태수 분류 (한국 해역별)
- 조석 관측 정점 신규/폐쇄 (연도별 변동)

### 4.2 waves
- 정점별 유의파고 H_s 연간 통계 (P95·P99·max)
- 파주기 T_p 분포
- 파향 통계 (장미도)
- 해양관측부이 가동률 (MPT 정점 신뢰도)

### 4.3 currents
- HF-Radar 해수유동 자료 (광역 표층 흐름)
- 연안 조류 ADCP 측정 정점

### 4.4 sediment-transport (간접)
- 직접 사항은 적으나 KHOA 다른 자료 (저질조사) 연계
- 부유사 OBS 정점 (있을 경우)

### 4.5 storm-surge (미작성 토픽)
- 태풍 case study (각 백서 끝 부분)
- 비조석 잔차 (residual) 통계
- 해수면 이상 (sea level anomaly) 연간

## 5. 시계열 비교 가능성 (2012-2025, 14년)

같은 정점에서 연간 백서를 추적하면:
- 조화상수 안정성 (M2·S2·K1·O1 amplitude·phase 시간적 변동)
- 평균해면 추세 (sea level rise 한국 정량)
- 풍·파 climate 변동 (extreme 빈도 증가 여부)
- 조석형태수 변화 (지형 변화 영향)

→ 위 분석은 14권 markdown에 PDF에서 직접 추출 가능 (검증 후 별도 노트 또는 experience/).

## 6. 보강·미해결

- 2025 보고서 §3.1 조위 분석 정점별 정량 표 추출 (조화·비조화)
- 정점별 H_s P95·P99 통계 (2025) 추출
- 14년 시계열 추세 분석 → `experience/khoa-annual-climate-trend.md` 작성 검토
- 정점 list 변동 (신규·폐쇄) — 사용자 인천·부산·축산 등 주요 정점 일관성 확인
- 태풍·이상기상 case study 발췌

## 7. 연결

- `concepts/tides/` — 조위·비조화 연간 통계
- `concepts/waves/` — H_s·T_p climate
- `concepts/currents/` — HF-Radar
- `textbook/notes/tides-khoa-nonharmonic-research.md` — DASHBOARD doc과 정합 cross-check
- `textbook/notes/tides-khoa-cross-verification.md` — 산재값 검증 추가 source
- `experience/khoa-multi-station-tide-validation-2026.md` — UTide 검증 reference
- 외부:
  - KHOA 바다누리: [http://www.khoa.go.kr/oceangrid/khoa/](http://www.khoa.go.kr/oceangrid/khoa/)
  - 국가해양관측망 자료 공개: 같은 사이트
