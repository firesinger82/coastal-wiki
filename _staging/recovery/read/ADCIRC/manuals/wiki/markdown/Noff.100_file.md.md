---
file: models/ADCIRC/raw/manuals/wiki/markdown/Noff.100_file.md
lines: 13
sha256: 4fba206a76623b4de312a2f393c199a9247f71f51c920681ed53bb273b0fe85e
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Noff.100_file.md — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | Noff.100 file — 각 요소(element)의 출력 시각 습윤·건조 상태(wet/dry state)를 기록한다(5). 1은 습윤(wet), 0은 건조(dry)이며 내부 배열(array)의 이름은 NOFF이다(5). 원문은 실험적 습윤·건조 알고리즘을 개발하는 ADCIRC 개발자에게 주로 유용하다고 적는다(7). fort.15의 선택 네임리스트(namelist)에서 출력 활성화 조건을 정한다(9). 제목·판본·빈 줄을 포함한다(1–10). 원문: `The noff.100 file records the wet/dry state of elements where 1 indicates an element is categorized as wet on the time step that the dataset was written while a value of 0 indicates that an element is categorized as dry. The name of the elemental wet/dry array in ADCIRC is [NOFF](/index.php?title=NOFF&action=edit&redlink=1).` (5); `The writing of the noff.100 output file is activated when the [outputNOFF](/index.php?title=OutputNOFF&action=edit&redlink=1) parameter is set to .true. in the optional [wetDryContol namelist](/index.php?title=WetDryContol_namelist&action=edit&redlink=1) at the bottom of the [fort.15 file](/Fort.15_file).` (9). |
| 11–13 | File Format — `noff.100 file format` 문서로 연결한다(11–13). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5·9행: NOFF, outputNOFF와 wetDryContol namelist 링크에 `action=edit&redlink=1`이 있다. 9행의 네임리스트 이름은 `wetDryContol`이다.
