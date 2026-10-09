---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.19_file.md
lines: 23
sha256: 2871b0c0a8c902be31616570c6a3b1d6bb45cd619191906f9c7e31d52235776e
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.19_file.md — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Fort.19 file / 역할·적용 조건 — 제목·판본·빈 줄을 포함한다(1–4). 수위 지정 경계 절점의 비주기적 시간 변화 수위 경계조건(non-periodic, time varying elevation boundary condition) 파일이라고 적는다(5). 이 파일을 읽는 두 조건을 함께 명시한다(5). 원문: `The fort.19 file contains non-periodic, time varying elevation boundary condition file for “elevation specified” boundary nodes. This file is only read when an “elevation specified” boundary condition has been specified in the [fort.14 file](/Fort.14_file) ([NOPE](/index.php?title=NOPE&action=edit&redlink=1)>0) and [NBFR](/index.php?title=NBFR&action=edit&redlink=1)=0 in the [fort.15 file](/Fort.15_file).` (5). |
| 7–18 | File Format — 입력 변수 한 행이 입력 자료 한 행을 나타내며 빈 줄은 가독성을 위한 것이라고 적는다(9). 시간 간격과 전체 수위 경계 절점에 대한 입력값 반복문을 제시한다(11–17). 원문: `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s). Blank lines are only to enhance readability. Loops indicate multiple lines of input. ` (9); `[ETIMINC](/index.php?title=ETIMINC&action=edit&redlink=1)` (11); `for k=1,[NETA](/index.php?title=NETA&action=edit&redlink=1)` (13); `[ESBIN(k)](/index.php?title=ESBIN(k)&action=edit&redlink=1)` (15); `end k loop` (17). |
| 19–23 | Notes — 첫 수위값 묶음의 시각과 후속 묶음의 시간 간격을 명시한다(21). 전체 실행 기간을 덮을 만큼 충분한 묶음을 제공해야 하며 그렇지 않으면 실행이 중단된다고 경고한다(23). 원문: `The first set of elevation values are provided at [TIME](/index.php?title=TIME&action=edit&redlink=1)=[STATIM](/index.php?title=STATIM&action=edit&redlink=1). Additional sets of elevation values are provided every [ETIMINC](/index.php?title=ETIMINC&action=edit&redlink=1).` (21); `Enough sets of elevation values must be provided to extend for the entire model run, otherwise the run will crash!` (23). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5·11·13·15·21: 변수 참조 URL에 `action=edit&redlink=1`이 들어 있다. 이 파일은 시간 간격과 수위 입력값의 단위를 정의하지 않는다.
