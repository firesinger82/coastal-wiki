---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/Input_Files/Time_Series_Files/Time_Series_Input_File_Formats/tser.md
lines: 46
sha256: f3e14fe7eaebdb0199d26a560099bc0ad7f8879eb1d1a8c5576c83540e38d8be
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# tser.md — 판독 구간 기록

구간은 1행부터 46행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 머리말 — 페이지 제목은 tser.inp이다(3). 페이지 ID, space, URL, 버전, 갱신 시각과 문서 경로를 기록한다(2–8). |
| 10–24 | tser.inp / 헤더·입력 유형 — EFDC_DSI Testing 시계열 파일이며 NCSER(2)번 반복한다고 적는다(10–12). 여섯 헤더 필드를 제시한다(16). InType.EQ.1이면 깊이 가중치(depth weights)와 단일 온도(Temp) 값을 읽고, 그 외에는 각 층의 온도(TEMP) 값을 읽는다(20–22). 조건과 이름을 그대로 옮긴다. 원문: `C \*\* EFDC\_DSI Testing, tser.inp Time Series FILE` (10); `C \*\* REPEATS NCSER(2) TIMES` (12); `C \*\* InType MCSER(NS) TCCSER(NS) TACSER(NS) RMULADJ(NS) ADDADJ(NS)` (16); `C \*\* IF InType.EQ.1 THEN READ DEPTH WEIGHTS AND SINGLE VALUE OF Temp` (20); `C \*\* ELSE READ A VALUE OF TEMP FOR EACH LAYER` (22). |
| 25–39 | InType=1 / InType=0 Structure — InType=1의 WKQ(K), K=1,KC 가중치와 시간·단일 값 쌍을 제시한다(26–30). InType=0의 시간·층별 값 형식을 제시한다(34–36). 반복 횟수·배열 첨자를 그대로 옮긴다. 빈 줄과 주석을 포함한다. 원문: `C \*\* InType=1 Structure` (26); `C \*\* WKQ(K),K=1,KC` (28); `C \*\* TCSER(M,NS) CSER(M,1,NS) !(MCSER(NS,2) PAIRS FOR NS=1,NCSER(2) SERIES)` (30); `C \*\* InType=0 Structure` (34); `C \*\* TCSER(M,NS) (CSER(M,K,NS),K=1,KC) !(MCSER(NS) PAIRS)` (36). |
| 40–46 | 온도 입력 예시 — Discharge라는 주석이 붙은 헤더와 가중치, 시각 0.00·200.00의 데이터 줄을 그대로 옮긴다(40–46). 데이터 값은 두 줄 모두 11.0000이다(44·46). 예시값을 기본값으로 정의하지 않는다. 원문: `1        2      86400       0        1        0 !         Discharge` (40); `1.0 1.0` (42); `       0.00         11.0000` (44); `   200.00         11.0000` (46). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 20–22·40행: 유형 설명은 Temp·TEMP를 읽는다고 적지만 예시 헤더의 주석은 `Discharge`이다.
- 16·30행: 헤더에서 `MCSER(NS)`로 적은 이름을 InType=1 형식의 반복 수 설명에서는 `MCSER(NS,2)`로 적는다.
- 16·40–46행: TCCSER, TACSER, RMULADJ, ADDADJ의 의미·단위와 온도 데이터 단위는 이 파일에 정의되어 있지 않다.

