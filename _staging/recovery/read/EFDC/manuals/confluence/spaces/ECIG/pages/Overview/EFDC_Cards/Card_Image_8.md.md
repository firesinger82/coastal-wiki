---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_8.md
lines: 43
sha256: 964de14d3635eba7a0516f4d2955f43c44925a0128829709fa2c3fd1b3b7d587
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_8.md — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 원문 메타데이터(frontmatter) — 문서 ID·제목·space·URL·버전·갱신 시각·계층 경로를 적는다(1–9). |
| 10–24 | C8 TIME-RELATED REAL PARAMETERS / 시간 기준·Coriolis — 실수형 시간 매개변수(real parameter) 중 시간 원점(time origin)을 초(seconds)로 바꾸는 승수(multiplier), 실행 시간 원점, 초 단위의 기준 시간 기간(reference time period)을 설명한다(14–18). 상수 Coriolis 매개변수(Coriolis parameter)의 단위와 계산식을 적는다(20). 가변 계수를 읽는 파일과 최대 Coriolis·곡률 가속도(curvature acceleration) 진단 출력 설정을 제시한다(22–24). 주석 표식과 빈 줄을 포함한다(11–24). 원문: `C8 TIME-RELATED REAL PARAMETERS` (10); `\* TCON: CONVERSION MULTIPLIER TO CHANGE TBEGIN TO SECONDS` (14); `\* TBEGIN: TIME ORIGIN OF RUN` (16); `\* TREF: REFERENCE TIME PERIOD IN sec (i.e. 44714.16S OR 86400S)` (18); `\* CORIOLIS: CONSTANT CORIOLIS PARAMETER IN 1/sec =2\*7.29E-5\*SIN(LAT)` (20); `\* ISCORV: 1 TO READ VARIABLE CORIOLIS COEFFICIENT FROM LXLY.INP FILE` (22); `\* ISCCA: WRITE DIAGNOSTICS FOR MAX CORIOLIS-CURV ACCEL TO FILEEFDC.LOG` (24). |
| 25–38 | C8 TIME-RELATED REAL PARAMETERS / 진단·동적 시간 단계 — 최대 이론 시간 단계(theoretical time step)의 진단 출력 옵션과 최대 시간 단계 위치 지도 작성 옵션을 적는다(26–30). 동적 시간 단계(dynamic time stepping)의 활성화 조건과 수심 변화율 인자, 초 단위 최대 시간 단계를 정의한다(32–36). 주석 표식과 빈 줄을 포함한다(25–38). 원문: `\* ISCFL: 1 WRITE DIAGNOSTICS OF MAX THEORETICAL TIME STEP TO CFL.OUT` (26); `\*            GT 1 TIME STEP ONLY AT INTERVAL ISCFL FOR ENTIRE RUN` (28); `\* ISCFLM: 1 TO MAP LOCATIONS OF MAX TIME STEPS OVER ENTIRE RUN` (30); `\* DTSSFAC: DYNAMIC TIME STEPPING IF DTSSFAC > 0.0` (32); `\* DTSSDHDT: DYNAMIC TIME STEPPING RATE OF DEPTH CHANGE FACTOR (USED WHEN > 0)` (34); `\* DTMAX: MAXIMUM TIME STEP FOR DYNAMIC STEPPING (SECONDS)` (36). |
| 39–43 | C8 입력 표 — 빈 표 머리글·구분선·입력 열 제목·수치 값 행을 제시한다(40–43). 값 행은 원문 예시이며 기본값이라는 표시는 없다. 앞 빈 줄을 포함한다(39). 원문: `\|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|` (40); `\| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \|` (41); `\| C8 \| TCON \| TBEGIN \| TREF \| CORIOLIS \| ISCORV \| ISCCA \| ISCFL \| ISCFLM \| DTSSFAC \| DTSSDHDT \| DTMAX \|` (42); `\|  \| 86400 \| 136.75 \| 86400 \| 6.59E-05 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| 3600 \|` (43). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 20행: `SIN(LAT)`의 `LAT`를 이 파일에서 정의하지 않는다. 각도의 단위도 이 파일에 없다.

