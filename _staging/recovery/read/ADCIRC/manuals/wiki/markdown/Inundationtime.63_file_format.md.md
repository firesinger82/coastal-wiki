---
file: models/ADCIRC/raw/manuals/wiki/markdown/Inundationtime.63_file_format.md
lines: 31
sha256: 910b2e9e9d65afdbe0b2dedbb7153305189df0ee3a6220b0d55460409b1e761e
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Inundationtime.63_file_format.md — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Inundationtime.63 file format — 제목·판본·빈 줄을 포함한다(1–6). 각 변수 줄은 출력 한 줄이며 빈 줄은 가독성을 위한 것이고 루프(loop)는 반복 출력 줄을 나타낸다고 설명한다(5). |
| 7–26 | Basic file structure — RUNDES·RUNID·AGRID와 데이터 집합 수 2의 헤더(header)를 적는다(7·9). 첫 집합은 TIME·IT 다음 NP개 절점의 inundationtime(k)를 적는다(11–17). 둘째 집합은 TIME·IT 다음 NP개 절점의 inundation_onset(k)를 적는다(19–25). 줄 순서와 각 이름을 원문 그대로 옮긴다. 원문: `[RUNDES](/index.php?title=RUNDES&action=edit&redlink=1), [RUNID](/index.php?title=RUNID&action=edit&redlink=1), [AGRID](/index.php?title=AGRID&action=edit&redlink=1)` (7); `2, [NP](/index.php?title=NP&action=edit&redlink=1), [DTDP](/DTDP)*[NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1), [NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1), [IRTYPE](/index.php?title=IRTYPE&action=edit&redlink=1)` (9); `[TIME](/index.php?title=TIME&action=edit&redlink=1), [IT](/index.php?title=IT&action=edit&redlink=1)` (11); `for k=1, [NP](/index.php?title=NP&action=edit&redlink=1)` (13); `k, [inundationtime(k)](/index.php?title=Inundationtime(k)&action=edit&redlink=1)` (15); `end k loop` (17); `[TIME](/index.php?title=TIME&action=edit&redlink=1), [IT](/index.php?title=IT&action=edit&redlink=1)` (19); `for k=1, [NP](/index.php?title=NP&action=edit&redlink=1)` (21); `k, [inundation_onset(k)](/index.php?title=Inundation_onset(k)&action=edit&redlink=1)` (23); `end k loop` (25). |
| 27–31 | Notes — NOUTGE에 따라 ASCII 또는 netCDF 형식일 수 있다(29). 시간 단계 계산(timestepping)이 끝난 뒤 모의 종료 시점에 파일을 쓴다(31). 핫스타트(hot start)여도 값은 현재 실행만 반영한다(31). 31행의 마지막 문장은 initiallydry.63 기준으로 처음 건조한 영역의 `maximum inundation depth`만 기록한다고 적는다. 원문: `Output may be in ascii or netCDF format depending on how NOUTGE is set in the [fort.15 file](/Fort.15_file).` (29); `The inundationtime.63 file is written at the very end of the simulation, after timestepping is complete. The values only reflect the current run, even if the run was hotstarted. The data in the inundationtime.63 file only record maximum inundation depth in areas that are initially dry, according to the [initiallydry.63 file](/Initiallydry.63_file).` (31). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 15·23·31행: 자료 줄은 `inundationtime(k)`와 `inundation_onset(k)`를 제시한다. 마지막 설명은 `only record maximum inundation depth`라고 적는다.
- 7·9·11·13·15·19·21·23행: 출력 변수의 위키 링크에 `action=edit&redlink=1`이 있다.
