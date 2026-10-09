---
file: models/ADCIRC/raw/manuals/wiki/markdown/Nodecode.63_file.md
lines: 11
sha256: 37a06741fde6e04e8ea5bd510367b2786be2b25906c4355c25366904b49db9f9
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Nodecode.63_file.md — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | Nodecode.63 file — 각 절점의 출력 시각 습윤·건조 상태(wet/dry state)를 기록한다(5). 1은 습윤(wet), 0은 건조(dry)이다(5). 원문은 실험적 습윤·건조 알고리즘을 개발하는 ADCIRC 개발자에게 주로 유용하다고 적는다(5). fort.15의 선택 네임리스트(namelist)에서 출력 활성화 조건을 정한다(7). 제목·판본·빈 줄을 포함한다(1–8). 원문: `The nodecode.63 file records the wet/dry state of nodes where 1 indicates a node is categorized as wet on the timestep that the dataset was written while a value of 0 indicates that a node is categorized as dry. These data are generally only valuable to ADCIRC developers who are working on experimental wet/dry algorithms.` (5); `The writing of the nodecode.63 output file is activated when the [outputNodeCode](/index.php?title=OutputNodeCode&action=edit&redlink=1) parameter is set to .true. in the optional [wetDryContol namelist](/index.php?title=WetDryContol_namelist&action=edit&redlink=1) at the bottom of the [fort.15 file](/Fort.15_file).` (7). |
| 9–11 | File Format — `nodecode.63 file format` 문서로 연결한다(9–11). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 7행: 네임리스트 이름은 `wetDryContol`이다. 해당 네임리스트와 outputNodeCode 링크에 `action=edit&redlink=1`이 있다.
