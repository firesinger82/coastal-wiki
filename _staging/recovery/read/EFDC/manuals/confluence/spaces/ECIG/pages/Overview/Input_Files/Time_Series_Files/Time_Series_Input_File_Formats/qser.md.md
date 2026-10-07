---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/Input_Files/Time_Series_Files/Time_Series_Input_File_Formats/qser.md
lines: 44
sha256: cb116e6caf5e1188ef44f3a7ee629647ca58fe13b1bcc7c3488e3f483e3bf01e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# qser.md — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 머리말 — 페이지 제목은 qser.inp이다(3). 페이지 ID, space, URL, 버전, 갱신 시각과 문서 경로를 기록한다(2–8). |
| 10–22 | qser.inp / 헤더·입력 유형 — EFDC_DSI Testing 시계열 파일의 헤더는 InType부터 ICHGQS까지 일곱 필드이다(10–14). InType.EQ.1이면 깊이 가중치(depth weights)와 단일 QSER 값을 읽고, 그 외에는 각 층의 QSER 값을 읽는다(18–20). 조건과 이름을 그대로 옮긴다. 원문: `C \*\* EFDC\_DSI Testing, qser.inp Time Series FILE` (10); `C \*\* InType MQSER(NS) TCQSER(NS) TAQSER(NS) RMULADJ(NS) ADDADJ(NS) ICHGQS` (14); `C \*\* IF InType.EQ.1 THEN READ DEPTH WEIGHTS AND SINGLE VALUE OF QSER` (18); `C \*\* ELSE READ A VALUE OF QSER FOR EACH LAYER` (20). |
| 23–37 | InType=1 / InType=0 Structure — InType=1의 WKQ(K), K=1,KC 가중치와 시간·단일 유량값 쌍을 제시한다(24–28). InType=0의 시간·층별 값 형식을 제시한다(32–34). MQSER 반복 수와 NS=1,NQSER 조건을 그대로 옮긴다. 빈 줄과 주석을 포함한다. 원문: `C \*\* InType=1 Structure` (24); `C \*\* WKQ(K),K=1,KC` (26); `C \*\* TQSER(M,NS) QSER(M,1,NS) !(MQSER(NS) PAIRS FOR NS=1,NQSER SERIES)` (28); `C \*\* InType=0 Structure` (32); `C \*\* TQSER(M,NS) (QSER(M,K,NS),K=1,KC) !(MQSER(NS) PAIRS)` (34). |
| 38–44 | 유량(discharge) 입력 예시 — 헤더, 가중치 0.5·0.5와 시각 0.00·200.00의 입력 줄을 그대로 옮긴다(38–44). 예시값을 기본값으로 정의하지 않는다. 원문: `1 2 86400 0 1 0 0 ! Discharge` (38); `0.5 0.5` (40); `0.00        0.1002` (42); `200.00    0.1002` (44). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14행: ICHGQS의 정의와 사용 조건은 이 파일에 없다. TCQSER, TAQSER, RMULADJ, ADDADJ의 의미·단위 설명도 이 파일에 없다.

