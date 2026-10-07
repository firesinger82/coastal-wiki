---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/Data_Format_B-14_Concentration_Time_Series_Data.md
lines: 14
sha256: feb8ff548994e3ad84247f857e14a9ee8782a1bbc78476ca3afa001f4a6bf17f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-14_Concentration_Time_Series_Data.md — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.
그림 경로는 원문과 같은 space 폴더를 기준으로 적었다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 ID·제목·space·URL·버전·갱신 시각·경로와 frontmatter이다(1–9행). |
| 10–11 | `sser.inp`를 농도 시계열 자료 파일로 설명하며 염분(salinity) 모듈이 활성화될 때 생성된다는 조건이 있다. Noorinastaliq 글꼴·우르두어(Urdu) Nastaliq 문자·페이지 레이아웃 지원에 관한 문장도 원문에 있다(10행). 원문: `sser.inp is the concentration-time series data file. It contains text saved in the Noorinastaliq font, which displays Urdu in Nastaliq script. INP files also support standard page layout formatting. This file is created when the salinity module is active.` (10). |
| 12–14 | `Example` 표제·빈 줄과 입력 형식 예시 그림이다(12–14행). 그림의 필드·조건·단위·예시 행을 그대로 옮겼다. 그림 직접 확인: `attachments/1588723906/B-16.png` — `sser.inp`의 농도 시계열(concentration time series) 형식이다(14행). `INTYPE=1`은 층 가중치와 시간별 단일 값을 읽고, 다른 경우에는 층별 시간값을 읽는다는 조건이 있다. 주석·필드·설정과 보이는 모든 입력 행: `* SSER.INP - CONCENTRATION TIME SERIES DATA - Version: 10.3` (그림 1행); `* Project: EFDC+ Demonstration` (그림 2행); `*` (그림 3행); `* Time-series data repeats NCSER times` (그림 4행); `* INTYPE MCSER(NS) TCCSER(NS) TACSER(NS) RMULADJ(NS) ADDADJ(NS)` (그림 5행); `*` (그림 6행); `* IF INTYPE=1 READ LAYER WEIGHTS THEN A SINGLE VALUE FOR EACH TIME` (그림 7행); `* ELSE` (그림 8행); `* READ A VALUE FOR EACH LAYER FOR EACH TIME` (그림 9행); `*` (그림 10행); `* INTYPE=1 Structure` (그림 11행); `* WQ(K),K=1,KC ! WEIGHT MULTIPLIER FOR EACH LAYER` (그림 12행); `* TCSER(M,NS) CSER(M,1,NS) ! MCSER(NS) PAIRS FOR NS=1,NCSER SERIES` (그림 13행); `*` (그림 14행); `* INTYPE=0 Structure` (그림 15행); `* TCSER(M,NS) (CSER(M,K,NS),K=1,KC) ! (MCSER(NS) pairs)` (그림 16행); `*` (그림 17행); `* TIME LAYER_1` (그림 18행); `*Format: F3 F5` (그림 19행); `1 2905 86400.000 0.0000 1.0000 0.0000 ! Q_169_027` (그림 20행); `1.000000` (그림 21행); `516.000 0.00000` (그림 22행); `516.042 0.00000` (그림 23행); `516.083 0.00000` (그림 24행); `516.125 0.00000` (그림 25행); `516.167 0.00000` (그림 26행); `516.208 0.00000` (그림 27행); `516.250 0.00000` (그림 28행); `516.292 0.00000` (그림 29행); `516.333 0.00000` (그림 30행); `516.375 0.00000` (그림 31행); `516.417 0.00000` (그림 32행); `516.458 0.00000` (그림 33행); `516.500 0.00000` (그림 34행); `516.542 0.00000` (그림 35행); `516.583 0.00000` (그림 36행); `516.625 0.00000` (그림 37행); `516.667 0.00000` (그림 38행); `516.708 0.00000` (그림 39행); `516.750 0.00000` (그림 40행); `516.792 0.00000` (그림 41행); `516.833 0.00000` (그림 42행); `516.875 0.00000` (그림 43행); `516.917 0.00000` (그림 44행); `516.958 0.00000` (그림 45행); `517.000 0.00000` (그림 46행); `517.042 0.00000` (그림 47행); `517.083 0.00000` (그림 48행); `517.125 0.00000` (그림 49행). 그림에 농도 단위는 표시되지 않는다. 파일 줄 수는 `90137`이며 그림에는 1–49행만 보인다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 본문의 Noorinastaliq·우르두어·페이지 레이아웃 설명과 예시 그림의 영문 주석·숫자 자료 형식 사이의 관계는 설명하지 않는다(10,14행).
- 농도 자료의 단위와 `TCCSER`, `TACSER`, `RMULADJ`, `ADDADJ`의 정의는 이 문서에 없다(10,14행).
- 그림은 파일 전체 `90137`행 중 1–49행만 보여 준다(14행).

