---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_3.md
lines: 53
sha256: 54294584d5d7a5cfa5f043bb3c80acbe37f37bae9b09020ad03bb1fef923d1cf
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_3.md — 판독 구간 기록

구간은 1행부터 53행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | C3 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 외부 모드(external mode) 해법의 옵션 매개변수와 스위치 제목을 제시한다(10). 빈 줄과 주석 표식도 포함한다(11–13). 원문: ` C3 EXTERNAL MODE SOLUTION OPTION PARAMETERS AND SWITCHES ` (10). |
| 14–29 | 반복 해법(iterative solution) — 과잉 이완(over relaxation) 매개변수, 목표 제곱 잔차(square residual), 최대 반복 수를 정의한다(14–18). 켤레 기울기법(conjugate gradient)에 척도화(scaling)를 적용하지 않는 옵션, 최소 대각 성분을 기준으로 척도화하는 옵션, 정규형(normal form)으로 척도화하는 옵션을 제시한다(20–24). 빈 줄과 반복 주석 표식도 포함한다. 원문: ` \* RP: OVER RELAXATION PARAMETER ` (14); ` \* RSQM: TARGET SQUARE RESIDUAL OF ITERATIVE SOLUTION SCHEME ` (16); ` \* ITERM: MAXIMUN NUMBER OF ITERATIONS ` (18); ` \* IRVEC: 0 CONJUGATE GRADIENT SOLUTION - NO SCALING ` (20); ` \*             9 CONJUGATE GRADIENT SOLUTION - SCALE BY MINIMUM DIAGONAL ` (22); ` \*           99 CONJUGATE GRADIENT SOLUTION - SCALE TO NORMAL FORM ` (24). |
| 30–37 | 대기압과 기타 항목 — CALPUV 해법에서 대기압(atmospheric pressure)을 사용하지 않는 옵션과 NASER > 1일 때 사용하는 옵션을 구분한다(30–32). RSQMADJ는 미사용이라고 적으며 DUMMY 항목은 설명이 비어 있다(34–36). 원문: ` \* IATMP: 0 DO NOT USE ATMOSPHERIC PRESSURE IN THE CALPUV SOLUTION ` (30); ` \*             1 USE ATMOSPHERIC PRESSURE IN THE CALPUV SOLUTION IF NASER > 1 ` (32); ` \* RSQMADJ: NOT USED ` (34); ` \* DUMMY: ` (36). |
| 38–49 | 습윤·건조(wetting and drying)·진단·필터 — 강한 비선형 습윤·건조 방식의 최대 반복 수와 건조 검사 반복 간격의 적용 조건 및 제한을 제시한다(38–42). 외부 모드 해법 진단 파일 활성화와 세 시간 수준(three time levels) 명시적 방식의 필터 계수(filter coefficient)를 정의한다(44–46). 원문: ` \* ITERHPM: MAXIMUM ITERATIONS FOR STRONGLY NONLINER DRYING AND WETTING ` (38); ` \* SCHEME (ISDRY=3 OR OR 4) ITERHPM.LE.4 ` (40); ` \* IDRYCK: ITERATIONS PER DRYING CHECK (ISDRY.GE.1) 2.LE.IDRYCK.LE.20 ` (42); ` \* ISDSOLV: 1 TO WRITE DIAGNOSTICS FILES FOR EXTERNAL MODE SOLVER ` (44); ` \* FILT3TL: FILTER COEFFICIENT FOR 3 TIME LEVEL EXPLICIT ( 0.0625 ) ` (46). |
| 50–53 | C3 입력 예시 — Markdown의 빈 표 머리글과 구분선(50–51), 열 이름(52), 입력 값(53)을 제시한다. 원문: ` \| C3 \| RP \| RSQM \| ITERM \| IRVEC \| IATMP \| RSQMADJ \| DUMMY \| ITERHPM \| IDRYCK \| ISDSOLV \| FILT3TL \| ` (52); ` \|  \| 1.8 \| 1.00E-14 \| 200 \| 9 \| 0 \| 1.00E-16 \| 0 \| 0 \| 20 \| 0 \| 0.0625 \| ` (53). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 36행: `DUMMY:` 항목의 콜론 뒤에는 설명이 없다.
- 32·40·42행: 대기압 및 습윤·건조 옵션의 적용 조건에 `NASER`와 `ISDRY`가 나오지만 이 파일은 두 매개변수를 정의하지 않는다.
