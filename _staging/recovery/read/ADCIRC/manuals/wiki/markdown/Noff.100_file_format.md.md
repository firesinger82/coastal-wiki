---
file: models/ADCIRC/raw/manuals/wiki/markdown/Noff.100_file_format.md
lines: 24
sha256: 069f78e0df256b135e1f92e832b22ab142d754a22f81991f70f56d355f067a25
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Noff.100_file_format.md — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Noff.100 file format — 제목·판본·빈 줄을 포함한다(1–6). 각 변수 줄은 출력 한 줄이며 빈 줄은 가독성을 위한 것이고 루프(loop)는 반복 출력 줄을 나타낸다고 설명한다(5). |
| 7–19 | Basic file structure — RUNDES·RUNID·AGRID와 NDSETSE·NE를 포함한 헤더(header)를 적는다(7·9). NDSETSE개 데이터 집합(dataset)마다 TIME·IT를 쓰고 NE개 요소의 k·NOFF(k)를 출력한다(11–18). 두 루프의 순서와 종료, 모든 형식 줄을 원문 그대로 옮긴다. 원문: `[RUNDES](/index.php?title=RUNDES&action=edit&redlink=1), [RUNID](/index.php?title=RUNID&action=edit&redlink=1), [AGRID](/index.php?title=AGRID&action=edit&redlink=1)` (7); `[NDSETSE](/index.php?title=NDSETSE&action=edit&redlink=1), [NE](/index.php?title=NE&action=edit&redlink=1), [DTDP](/DTDP)*[NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1), [NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1), [IRTYPE](/index.php?title=IRTYPE&action=edit&redlink=1)` (9); `for j=1, [NDSETSE](/index.php?title=NDSETSE&action=edit&redlink=1)` (11); `[TIME](/index.php?title=TIME&action=edit&redlink=1), [IT](/index.php?title=IT&action=edit&redlink=1)` (13); `for k=1, [NE](/index.php?title=NE&action=edit&redlink=1)` (14); `k, [NOFF(k)](/index.php?title=NOFF(k)&action=edit&redlink=1)` (15); `end k loop` (16); `end j loop ` (18). |
| 20–24 | Notes — ASCII 형식만 지원한다(22). fort.63과 같은 일정으로 출력하며 TOUTSGE·TOUTFGE·NSPOOLGE를 사용한다(22). 값은 정수(integer)이다(24). 원문은 이 파일이 절점(nodal) 자료 대신 요소 자료를 만드는 유일한 ADCIRC 출력 파일이라고 적는다(24). 원문: `Output is only available in the ascii format. The data are produced on the same schedule as the [fort.63  file](/Fort.63_file), i.e., the values of [TOUTSGE](/index.php?title=TOUTSGE&action=edit&redlink=1), [TOUTFGE](/index.php?title=TOUTFGE&action=edit&redlink=1), [NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1) are used.` (22); `The noff.100 file contains integer values. It is the only ADCIRC output file that produces elemental (as opposed to nodal) data` (24). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 7·9·11·13·14·15·22행: 출력 변수와 일정 매개변수의 위키 링크에 `action=edit&redlink=1`이 있다.
