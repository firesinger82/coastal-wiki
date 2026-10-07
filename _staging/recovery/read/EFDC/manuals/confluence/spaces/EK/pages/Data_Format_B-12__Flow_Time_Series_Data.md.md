---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/Data_Format_B-12__Flow_Time_Series_Data.md
lines: 14
sha256: ce032d11b71f97d5fd36e2b2ffafae03cd6fb797491c682ecc2709ee487de74b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-12__Flow_Time_Series_Data.md — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.
그림 경로는 원문과 같은 space 폴더를 기준으로 적었다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 ID·제목·space·URL·버전·갱신 시각·경로와 frontmatter이다(1–9행). |
| 10–11 | `qser.inp`를 유량 시계열(flow time series) 자료 파일로 설명한다. Noorinastaliq 글꼴·우르두어(Urdu) Nastaliq 문자·페이지 레이아웃 지원에 관한 문장도 원문에 있다(10행). 원문: `qser.inp is the flow time series data file. It contains text saved in the Noorinastaliq font, which displays Urdu in Nastaliq script. INP files also support standard page layout formatting.` (10). |
| 12–14 | `Example` 표제·빈 줄과 입력 형식 예시 그림이다(12–14행). 그림의 필드·조건·단위·예시 행을 그대로 옮겼다. 그림 직접 확인: `attachments/1588723883/B-14.png` — `qser.inp`의 두 입력 모드, 시간·유량 변환계수와 자료를 보여 준다(14행). `INTYPE = 1`은 총유량과 층별 분할을 입력하고, `INTYPE = 0`은 층별 유량을 입력한다. 그림의 원문 행: `* QSER.INP - FLOW TIME SERIES DATA - Version: 10.3` (그림 1행); `* Project: EFDC+ Demonstration` (그림 2행); `*` (그림 3행); `* INTYPE = 1 ! INPUT TOTAL FLOW AND SPLIT FOR EACH LAYER` (그림 4행); `* WQ(K),K=1,KC ! FLOW SPLITS FOR EACH LAYER` (그림 5행); `* TQSER(M,NS) QSERT(M,NS) ! TOTAL FLOW FOR CURRENT TIME` (그림 6행); `*` (그림 7행); `* INTYPE = 0 ! INPUT FLOWS FOR EACH LAYER` (그림 8행); `* TQSER(M,NS) (QSER(M,K,NS),K=1,KC) !` (그림 9행); `*` (그림 10행); `* MQSER: NUMBER OF DATA POINTS IN SERIES` (그림 11행); `* TCQSER: TIME CONVERSION TO SECONDS - MULTIPLIER TQSER = (TQSER + TAQSER)*TCQSER` (그림 12행); `* TAQSER: TIME CONVERSION TO SECONDS - OFFSET TQSER = (TQSER + TAQSER)*TCQSER` (그림 13행); `* RMULADU: FLOW CONVERSION TO M^3/S - MULTIPLIER QSER = (QSER + ADDADJ)*RMULADJ` (그림 14행); `* ADDADJ: FLOW CONVERSION TO M^3/S - OFFSET QSER = (QSER + ADDADJ)*RMULADJ` (그림 15행); `* ICHGQS: 0 - USE FLOWS AS INPUT (DEFAULT), 1 - MAX(QSER,0), -1 - MIN(QSER,0)` (그림 16행); `*` (그림 17행); `*` (그림 18행); `* REPEAT FOR EACH SERIES` (그림 19행); `* InType MQSER TCQSER TAQSER RMULADU ADDADJ ICHGQS ! ID` (그림 20행); `*` (그림 21행); `*Format: F3 F4` (그림 22행); `1 2905 86400.000 0 1 0 0 ! Q_169_027` (그림 23행); `1 ! Layer Splits` (그림 24행); `516.000 0.0000` (그림 25행); `516.042 0.8468` (그림 26행); `516.083 4.7310` (그림 27행); `516.125 4.3978` (그림 28행); `516.167 3.3794` (그림 29행); `516.208 1.0329` (그림 30행); `516.250 2.2101` (그림 31행); `516.292 1.9290` (그림 32행); `516.333 1.8987` (그림 33행); `516.375 2.1476` (그림 34행); `516.417 2.1907` (그림 35행); `516.458 2.1836` (그림 36행); `516.500 -2.9459` (그림 37행); `516.542 -3.3115` (그림 38행); `516.583 -3.2471` (그림 39행); `516.625 -4.1271` (그림 40행); `516.667 -4.9045` (그림 41행); `516.708 -5.5963` (그림 42행); `516.750 -3.0109` (그림 43행); `516.792 2.8751` (그림 44행); `516.833 4.6031` (그림 45행); `516.875 4.1070` (그림 46행); `516.917 4.4095` (그림 47행); `516.958 4.4785` (그림 48행); `517.000 4.3585` (그림 49행). 식의 LaTeX 표기는 `\(\mathrm{TQSER}=(\mathrm{TQSER}+\mathrm{TAQSER})*\mathrm{TCQSER}\)` (그림 12–13행), `\(\mathrm{QSER}=(\mathrm{QSER}+\mathrm{ADDADJ})*\mathrm{RMULADJ}\)` (그림 14–15행)이다. 파일 줄 수는 `58163`이며 그림에는 1–49행만 보인다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 본문의 Noorinastaliq·우르두어·페이지 레이아웃 설명과 예시 그림의 영문 주석·숫자 자료 형식 사이의 관계는 설명하지 않는다(10,14행).
- 변환계수 이름은 주석·헤더에서 `RMULADU`이고 유량 변환식에서는 `RMULADJ`이다. 총유량 입력 행에는 `QSERT(M,NS)`가 있으며 뒤의 변환식은 `QSER`를 쓴다(14행, 그림 6,14–15,20행).
- 그림은 파일 전체 `58163`행 중 1–49행만 보여 준다(14행).

