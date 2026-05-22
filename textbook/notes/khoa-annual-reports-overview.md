---
title: "KHOA 국가해양관측망 연간백서 2012-2025 — 통합 개관"
source_id: khoa-annual-reports
chapter: "15권 통합 개관 (Annual Report 2012-2025)"
pages: "—"
page_offset_applied: false
topic: khoa-official
canonical_source: self
citation_status: verified
verification_method: "AI cross-reference against D:\\Numerical_models\\00_Common\\KHOA_WHITE_PAPER\\markdowns\\ 15 .md files (총 188,929 줄). 2025 보고서 구조 + 조석 비조화 공식 정의 confirmed."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-23
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-23
---

# KHOA 국가해양관측망 연간백서 (2012-2025)

> 출처: `khoa-annual-reports` = `D:\Numerical_models\00_Common\KHOA_WHITE_PAPER\markdowns\` (15권, 188,929 줄 markdown)

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
| (별도) | | F ≥ 3.00 → 일주조형 |

→ DASHBOARD research doc (`tides-khoa-nonharmonic-research.md`) 의 공식과 **완전 일치**. 또 하나의 KHOA 공식 source 확보.

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
