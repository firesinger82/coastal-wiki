---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.18_file.md
lines: 5
sha256: 0b2949b7de7cfc59621c278fbac945dc87abccd12fdfad0290b288209e12b668
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.18_file.md — 판독 구간 기록

구간은 1행부터 5행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | Fort.18 file / 역할·생성·배치 — 제목·판본·빈 줄을 포함한다(1–4). ADCIRC의 MPI 병렬 실행(parallel execution), 통상 PADCIRC라고 부르는 실행에 필요한 정보를 담는다고 적는다(5). 병렬 실행 전에 adcprep이 만들며 주 실행 디렉터리 대신 adcprep이 만든 각 PE 하위 디렉터리에 사본 하나씩 둔다고 명시한다(5). 원문: `The fort.18 file is a file with information needed for parallel (MPI) execution of ADCIRC (commonly termed PADCIRC).  The file is created by the [adcprep](/index.php?title=Adcprep&action=edit&redlink=1) executable, which is run prior to launching a parallel ADCIRC run.  The file is not located in the main run directory, but instead there is one copy of the file in each of the PE* (PE0000, PE0001, etc.) subdirectories created by adcprep.` (5). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5: `adcprep` 참조 URL에 `action=edit&redlink=1`이 들어 있다.
