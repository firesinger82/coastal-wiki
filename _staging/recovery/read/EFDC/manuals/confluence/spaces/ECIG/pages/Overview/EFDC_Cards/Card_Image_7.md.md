---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_7.md
lines: 53
sha256: 6340d7b76385f68416c64b260ec3edb90ab0ee4635627cf83134ae91f5c4efe6
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_7.md — 판독 구간 기록

구간은 1행부터 53행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 원문 메타데이터(frontmatter) — 문서 ID·제목·space·URL·버전·갱신 시각·계층 경로를 적는다(1–9). |
| 10–28 | C7 TIME-RELATED INTEGER PARAMETERS / 기간·출력·보정 — 기준 시간 기간(reference time period)의 수, 기간당 시간 단계(time step) 수, 선형화 기간과 완전 비선형으로 이행하는 기간을 설명한다(14–20). 전체 출력 파일의 출력 간격과 두 시간 준위 사다리꼴 보정(two time level trapezoidal correction)의 사용 간격을 제시한다(22–28). 두 설명의 `NLTC` 이름을 원문대로 유지한다(18·20). 주석 표식과 빈 줄을 포함한다(11–28). 원문: `C7 TIME-RELATED INTEGER PARAMETERS` (10); `\* NTC: NUMBER OF REFERENCE TIME PERIODS IN RUN` (14); `\* NTSPTC: NUMBER OF TIME STEPS PER REFERENCE TIME PERIOD` (16); `\* NLTC: NUMBER OF LINEARIZED REFERENCE TIME PERIODS` (18); `\* NLTC: NUMBER OF TRANSITION REF TIME PERIODS TO FULLY NONLINEAR` (20); `\* NTCPP: NUMBER OF REFERENCE TIME PERIODS BETWEEN FULL PRINTED OUTPUT` (22); `\*              TO FILE EFDC.OUT` (24); `\* NTSTBC: NUMBER OF TIME STEPS BETWEEN USING A TWO TIME LEVEL TRAPEZOIDAL` (26); `\*                CORRECTION TIME STEP, \*\* MASS BALANCE PRINT INTERVAL \*\*` (28). |
| 29–48 | C7 TIME-RELATED INTEGER PARAMETERS / 부력·평균·건조·시간 간격 — 미사용 부력 강제력(buoyancy forcing) 설정과 가변 부력 강제력 기간을 적는다(30–32). 질량 수지 잔차(mass balance residual) 또는 평균 질량 수송 변수(mean mass transport variable)의 평균 단계 수를 설명한다(34–36). 연구용 설정, 셀의 최소 건조 유지 단계 수와 물 제거 활성화 조건, 동적 시간 단계(dynamic time-stepping)의 초기 고정 반복 수와 시간 간격 증가의 최소 반복 수를 적는다(38–46). 주석 표식과 빈 줄을 포함한다(29–48). 원문: `\* NTCNB: NUMBER OF REFERENCE TIME PERIODS WITH NO BUOYANCY FORCING (NOT USED)` (30); `\* NTCVB: NUMBER OF REF TIME PERIODS WITH VARIABLE BUOYANCY FORCING` (32); `\* NTSMMT: NUMBER OF NUMBER OF TIME STEPS TO AVERAGE OVER TO OBTAIN` (34); `\*                 MASS BALANCE RESIDUALS OR MEAN MASS TRANSPORT VARIABLES (e.g. WASP Linkage)` (36); `\* NFLTMT: USE 1 (FOR RESEARCH PURPOSES)` (38); `\* NDRYSTP: MIN NO. OF TIME STEPS A CELL REMAINS DRY AFTER INTIAL DRYING` (40); `\*                   -NDRYSTP FOR ISDRY=-99 TO ACTIVATE WASTING WATER IN DRY CELLS` (42); `\* NRAMPUP: NUMBER OF INITIAL LOOPS TO HOLD TIMESTEP CONSTANT FOR DYNNAMIC TIME-STEPPING` (44); `\* NUPSTEP: MINIMUM NUMBER OF INTERATIONS FOR EACH TIME STEP WHEN GROWING DTDYN` (46). |
| 49–53 | C7 입력 표 — 빈 표 머리글·구분선·입력 열 제목·수치 값 행을 제시한다(50–53). 값 행은 원문 예시이며 기본값이라는 표시는 없다. 앞 빈 줄을 포함한다(49). 원문: `\|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|` (50); `\| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \|` (51); `\| C7 \| NTC \| NTSPTC \| NLTC \| NTTC \| NTCPP \| NTSTBC \| NTCNB \| NTCVB \| NTSMMT \| NFLTMT \| NDRYSTP \| NRAMPUP \| NUPSTEP \|` (52); `\|  \| 28 \| 8640 \| 0 \| 0 \| 10 \| 4 \| 0 \| 0 \| 288 \| 1 \| 16 \| 1000 \| 2 \|` (53). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 18·20·52행: 서로 다른 설명이 모두 `NLTC`로 시작한다. 입력 표에는 `NLTC`와 `NTTC`가 각각 있으며 `NTTC` 이름으로 된 설명은 없다.
- 42·46행: `ISDRY`와 `DTDYN`을 사용하지만 이 파일에는 두 이름의 정의가 없다.

