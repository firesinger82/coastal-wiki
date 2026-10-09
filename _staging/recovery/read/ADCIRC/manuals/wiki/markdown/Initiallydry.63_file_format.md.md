---
file: models/ADCIRC/raw/manuals/wiki/markdown/Initiallydry.63_file_format.md
lines: 23
sha256: 5f40c2e2bed535aef28f91332b43076967d57d5780a179428e19b3bd444eec09
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Initiallydry.63_file_format.md — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Initiallydry.63 file format — 제목·판본·빈 줄을 포함한다(1–6). 원문은 아래 각 줄이 출력 변수 줄에 해당하며 빈 줄은 가독성을 위한 것이고 루프(loop)는 여러 출력 줄을 나타낸다고 설명한다(5). |
| 7–18 | Basic file structure — RUNDES·RUNID·AGRID, 데이터 집합 수 1을 포함한 헤더(header), TIME·IT, NP개 절점의 k와 initiallydry(k)를 순서대로 제시한다(7–17). 파일 형식의 각 줄과 루프 종료를 원문 그대로 옮긴다. 원문: `[RUNDES](/index.php?title=RUNDES&action=edit&redlink=1), [RUNID](/index.php?title=RUNID&action=edit&redlink=1), [AGRID](/index.php?title=AGRID&action=edit&redlink=1)` (7); `1, [NP](/index.php?title=NP&action=edit&redlink=1), [DTDP](/DTDP)*[NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1), [NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1), [IRTYPE](/index.php?title=IRTYPE&action=edit&redlink=1)` (9); `[TIME](/index.php?title=TIME&action=edit&redlink=1), [IT](/index.php?title=IT&action=edit&redlink=1)` (11); `for k=1, [NP](/index.php?title=NP&action=edit&redlink=1)` (13); `k, [initiallydry(k)](/index.php?title=Initiallydry(k)&action=edit&redlink=1)` (15); `end k loop` (17). |
| 19–23 | Notes — NOUTGE에 따라 ASCII 또는 netCDF 형식일 수 있다(21). 시간 단계 계산(timestepping)을 시작하기 전 모의 시작 시점에 파일을 쓴다(23). 원문: `Output may be in ascii or netCDF format depending on how [NOUTGE](/index.php?title=NOUTGE&action=edit&redlink=1) is set in the [fort.15 file](/Fort.15_file).` (21); `The initiallydry.63 is written at the very beginning of a simulation run, before timestepping begins.` (23). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 7·9·11·13·15·21행: 출력 변수와 NOUTGE의 위키 링크에 `action=edit&redlink=1`이 있다.
