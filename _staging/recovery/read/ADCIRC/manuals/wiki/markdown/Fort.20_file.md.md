---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.20_file.md
lines: 23
sha256: 41cdad23033a17d33f8a17aa7488218692beebdda55a782adc496fbbfbbc0d3f
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.20_file.md — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Fort.20 file / 역할·적용 조건 — 제목·판본·빈 줄을 포함한다(1–4). 0이 아닌 법선 유량(normal flow)을 지정한 경계 절점의 비주기적 경계조건 파일이라고 적는다(5). 경계 유형과 비주기 옵션의 조건을 함께 명시한다(5). 원문: `Non-periodic, normal flow boundary condition file for “specified non-zero normal flow” boundary nodes. This file is only read when a “specified non-zero normal flow” boundary condition has been specified in the Grid and Boundary Information File ([IBTYPE](/index.php?title=IBTYPE&action=edit&redlink=1) =2, 12 or 22) and [NFFR](/index.php?title=NFFR&action=edit&redlink=1) =0 in the [fort.15 file](/Fort.15_file).` (5). |
| 7–18 | File Format — 입력행과 빈 줄·반복문의 표기 규칙을 설명하며 변수 정의는 링크로 제공한다고 적는다(9). 시간 간격·경계 절점 반복 수·법선 유량의 입력행을 제시한다(11–17). 원문: `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s). Blank lines are only to enhance readability. Loops indicate multiple lines of input. Definitions of each variable are provided via hot links.` (9); `FTIMINC` (11); `for k=1,NFLBN` (13); `QNIN(k)` (15); `end k loop` (17). |
| 19–23 | Notes — 첫 유량값 묶음의 시각과 후속 시간 간격을 명시한다(21). 전체 실행 기간을 덮을 만큼 충분한 묶음이 필요하며 부족하면 실행이 중단된다고 경고한다(23). 원문: `The first set of normal flow values is provided at TIME=STATIM. Additional sets of normal flow values are provided every FTIMINC` (21); `Enough sets of normal flow values must be provided to extend for the entire model run, otherwise the run will crash!` (23). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 9·11·13·15: 9행은 변수 정의를 링크로 제공한다고 적는다. 그러나 입력 형식의 `FTIMINC`, `NFLBN`, `QNIN(k)`에는 링크가 없으며 이 파일에 정의·단위도 없다.
- 5: `IBTYPE`과 `NFFR`의 참조 URL에 `action=edit&redlink=1`이 들어 있다.
