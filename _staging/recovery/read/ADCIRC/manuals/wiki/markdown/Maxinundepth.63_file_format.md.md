---
file: models/ADCIRC/raw/manuals/wiki/markdown/Maxinundepth.63_file_format.md
lines: 31
sha256: 3f874b964b372626eae2a46d2b0e0811f02b3fb41716b05fe1e6d2b6e239d460
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Maxinundepth.63_file_format.md — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Maxinundepth.63 file format — 제목·판본·빈 줄을 포함한다(1–6). 각 변수 줄은 출력 한 줄이며 빈 줄은 가독성을 위한 것이고 루프(loop)는 반복 출력 줄을 나타낸다고 설명한다(5). |
| 7–26 | Basic file structure — RUNDES·RUNID·AGRID와 데이터 집합 수 2의 헤더(header)를 적는다(7·9). 첫 집합은 TIME·IT 다음 NP개 절점의 maxinundepth(k)를 적는다(11–17). 둘째 집합은 TIME·IT 다음 NP개 절점의 maxinundepth_time(k)를 적는다(19–25). 줄 순서와 이름을 원문 그대로 옮긴다. 원문: `[RUNDES](/index.php?title=RUNDES&action=edit&redlink=1), [RUNID](/index.php?title=RUNID&action=edit&redlink=1), [AGRID](/index.php?title=AGRID&action=edit&redlink=1)` (7); `2, [NP](/index.php?title=NP&action=edit&redlink=1), [DTDP](/DTDP)*[NSPOOLGW](/index.php?title=NSPOOLGW&action=edit&redlink=1), [NSPOOLGW](/index.php?title=NSPOOLGW&action=edit&redlink=1), [IRTYPE](/index.php?title=IRTYPE&action=edit&redlink=1)` (9); `[TIME](/index.php?title=TIME&action=edit&redlink=1), [IT](/index.php?title=IT&action=edit&redlink=1)` (11); `for k=1, [NP](/index.php?title=NP&action=edit&redlink=1)` (13); `k, [maxinundepth(k)](/index.php?title=Maxinundepth(k)&action=edit&redlink=1)` (15); `end k loop` (17); `[TIME](/index.php?title=TIME&action=edit&redlink=1), [IT](/index.php?title=IT&action=edit&redlink=1)` (19); `for k=1, [NP](/index.php?title=NP&action=edit&redlink=1)` (21); `k, [maxinundepth_time(k)](/index.php?title=Maxinundepth_time(k)&action=edit&redlink=1)` (23); `end k loop` (25). |
| 27–31 | Notes — NOUTGE에 따라 ASCII 또는 netCDF 형식일 수 있다(29). 시간 단계 계산(timestepping)이 끝난 뒤 모의 종료 시점에 파일을 쓴다(31). 핫스타트(hot start)여도 값은 현재 실행만 반영한다(31). initiallydry.63 기준으로 처음 건조한 영역만 기록한다(31). 원문: `Output may be in ascii or netCDF format depending on how [NOUTGE](/index.php?title=NOUTGE&action=edit&redlink=1) is set in the [fort.15 file](/Fort.15_file).` (29); `The maxinundepth.63 file is written at the very end of the simulation, after timestepping is complete. The values only reflect the current run, even if the run was hotstarted. The data in the maxinundepth.63 file only record maximum inundation depth in areas that are initially dry, according to the [initiallydry.63 file](/Initiallydry.63_file).` (31). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 7·9·11·13·15·19·21·23·29행: 출력 변수와 NOUTGE의 위키 링크에 `action=edit&redlink=1`이 있다.
