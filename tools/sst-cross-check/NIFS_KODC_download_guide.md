# NIFS KODC 정선해양관측 자료 수동 다운로드 가이드

> KODC 는 form-based 다운로드만 제공 (API 없음). 본 가이드는 본 위키의 한국 SST trend 분석을 보강하기 위해 어떤 자료를 받을지 정리.

## 1. 목적

`experience/khoa-sst-global-crosscheck.md` 의 미해결 항목:
- NIFS published 값 (Fish Aquat Sci 2023: 0.025 °C/yr) 만 인용 → raw 자료로 직접 검증 필요
- 동해 102정선·206정선 등 정선별 trend 와 KHOA 점 정점 trend 비교
- 다층 수온 (표층 vs 50m vs 100m) — 본 위키 미커버 영역

## 2. 다운로드 단계

### 2.1 사이트 접속

[https://www.nifs.go.kr/kodc/observe/line/data](https://www.nifs.go.kr/kodc/observe/line/data)

### 2.2 필터 설정

#### 권장 1차 다운로드 (동해 102정선 + 서해 311정선 + 남해 207정선 — 본 위키 13정점 인근)

| 필드 | 설정 |
|---|---|
| 해역 | 동해 (102정선) → 서해 (311정선) → 남해 (207정선) — 3회 분리 다운로드 |
| 정선 | 위 각각 |
| 정점 | 전체 (각 정선의 모든 정점) |
| 수심 | 전체 (표층 + 다층) |
| 측정 변수 | **수온 (°C)** + 염분 (psu) 필수, 영양염·DO 옵션 |
| 기간 | **1968-01 ~ 현재** (KODC archive 최장) |
| 사용자 분류 | 종사자 / 교육기관 / 연구자 (해당하는 것) |
| 용도 | "한국 연안 SST climate trend 분석" |
| 포맷 | CSV |

### 2.3 파일 저장 위치

```
/home/firesinger/coastal-wiki/data/sst-global/nifs-kodc/
├── nifs_donghae_102line_1968-2025.csv     # 동해 102정선
├── nifs_seohae_311line_1968-2025.csv      # 서해 311정선
└── nifs_namhae_207line_1968-2025.csv      # 남해 207정선
```

(파일명은 다운로드 시 KODC 가 주는 이름이 있을 수 있음 — 받은 후 위와 같이 rename 권장)

### 2.4 다운로드 후 처리

다음 분석 스크립트 작성:
- `tools/sst-cross-check/parse_nifs_kodc.py` — CSV 정규화 + 정선별 정점별 SST 시계열 추출
- `analyze_global_trends.py` 에 NIFS 데이터셋 추가 → 4-dataset cross-check (OISST + HadISST + COBE2 + NIFS in-situ raw)

## 3. 어떤 정선·정점이 한국 13정점에 매칭되나

본 위키의 KHOA 13정점 vs NIFS 정선·정점 대략 매칭 (인근 위치 기준):

| KHOA 정점 | 인근 NIFS 정선 | 비고 |
|---|---|---|
| 인천 | 서해 309정선 / 311정선 | 인천 외해 |
| 목포 | 서해 314정선 / 315정선 | 목포 외해 |
| 진도 | 남해 207정선 (서쪽 정점) | 진도 서수도 |
| 부산 | 남해 209정선 / 207정선 (동쪽) | 부산 외해 |
| 여수 | 남해 208정선 | 여수 외해 |
| 거제도 | 남해 207정선 (중앙) | 거제 남측 |
| 거문도 | 남해 206정선 | 거문도 외해 |
| 제주 | 남해 313정선 / 동중국해 314 | 제주 북측 |
| 서귀포 | 동중국해 315정선 | 제주 남측 |
| 울산 | 동해 104정선 / 105정선 | 울산 외해 |
| 포항 | 동해 103정선 / 102정선 | 포항 외해 |
| 묵호 | 동해 102정선 | 묵호 외해 |
| 속초 | 동해 101정선 | 속초 외해 |

→ 동해 101·102·103·104·105 + 서해 309·311·314·315 + 남해 206·207·208·209 + 동중국해 313·314·315 — 약 **15개 정선** 받으면 13정점 대부분 cover.

**우선 1차 다운로드 후보 (시간 절약)**:
- 동해 102정선 (포항·묵호 대표)
- 남해 207정선 (거제도·부산·진도)
- 서해 311정선 (인천·목포 인근)

## 4. NIFS published 결과 (참고)

다운로드 전에 기대값:
- 한국 평균 1968-2022 SST trend: **0.025 °C/year** = 0.25 °C/decade
- HadISST 1968-2022 한국 평균 0.27 °C/decade 와 일관

본 위키 cross-check (`experience/khoa-sst-global-crosscheck.md`) 에서 published 값으로 이미 인용 중.

## 5. 자동화 가능성 (향후)

KODC form 자동화 옵션:
- Selenium (Python) — 브라우저 자동화 (사용자 분류·용도 입력 자동)
- Playwright — 같은 목적
- 또는 NIFS 측에 OpenAPI 도입 요청

현재는 **수동 다운로드 → CSV 정규화** 가 가장 실용적.

## 6. 후속 작업 (다운로드 완료 후)

1. `data/sst-global/nifs-kodc/` 디렉토리에 CSV 저장
2. `tools/sst-cross-check/parse_nifs_kodc.py` 작성 (정선·정점·수심·변수 별 정규화)
3. `analyze_global_trends.py` 에 NIFS data 추가 (annual mean, 정선별 평균)
4. `experience/khoa-sst-global-crosscheck.md` 에 NIFS raw 결과 통합 (§2 표 갱신, NIFS 단순 인용 → NIFS 직접 분석)
5. (선택) `experience/nifs-vertical-profile-trends.md` — 다층 수온 trend 별도 노트
