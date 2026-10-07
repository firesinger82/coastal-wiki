---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/Input_Files/Time_Series_Files/Time_Series_Input_File_Formats/pser.md
lines: 36
sha256: d6f494b8cbc630b863dbd215387a0d00b70abdfadc49d16794f73a8b710ac711
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# pser.md — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 머리말 — 페이지 제목은 pser.inp이다(3). 페이지 ID, space, URL, 버전, 갱신 시각과 문서 경로를 기록한다(2–8). |
| 10–29 | pser.inp / 입력 구조 — NPSER번 반복하며 여섯 헤더 필드를 제시한다(12–16). ITYP=0이면 단일 값과 헤더 1줄, ITYP=1이면 HIGH LOW 분리와 헤더 2줄이라고 적는다(20–22). 뒤 데이터 형식을 MPSER(NS)번 반복한다고 적고 TPSER, PSER와 대괄호 안 PSERS를 제시한다(26–28). 유형·반복 횟수·형식 줄을 그대로 옮긴다. 원문: `C \*\* , pser.inp Time Series FILE,` (10); `C \*\* REPEATS NPSER TIMES` (12); `C \*\* ITYP(NS) MPSER(NS) TCPSER(NS) TAPSER(NS) RMULADJ(NS) ADDADJ(NS)` (16); `C \*\* ITYP = 0, SINGLE VALUE WITH 1 HEADER LINE` (20); `C \*\* = 1, HIGH LOW SEPARATED WITH 2 HEADER LINES` (22); `C \*\* THE FOLLOWING REPEATED MPSER(NS) TIMES` (26); `C \*\* TPSER(M,NS) PSER(M,1,NS) [ PSERS(M,1,NS) ]` (28). |
| 30–36 | pser 입력 예시 — 헤더와 시각 0.00, 10.00, 20.00의 데이터 줄을 그대로 옮긴다(30–36). 예시값을 기본값으로 정의하지 않는다. 원문: `0 2 86400 0 1 0 0 0 ! H` (30); `0.00 0.0000` (32); `10.00 2.000` (34); `20.00 3.000` (36). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 16·30행: 헤더 설명은 여섯 필드를 나열하지만 예시 헤더는 주석 앞에 숫자 여덟 개를 적는다. 추가 숫자 두 개의 필드 이름은 이 파일에 없다.
- 26·30·32–36행: MPSER(NS)번 반복한다고 적는다. 예시 헤더의 두 번째 값은 2이다. 뒤 데이터 행은 3개이다.
- 28행: 대괄호로 적힌 `PSERS(M,1,NS)`의 정의와 사용 조건은 이 파일에 없다.

