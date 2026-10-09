---
file: models/ADCIRC/raw/manuals/wiki/markdown/Nodecode.63_file_format.md
lines: 24
sha256: 9e9c5e4e11ccb045f65394f8d360bb1cf360943194eb375468da3c39e1083bfc
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Nodecode.63_file_format.md — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Nodecode.63 file format — 제목·판본·빈 줄을 포함한다(1–6). 각 변수 줄은 출력 한 줄이며 빈 줄은 가독성을 위한 것이고 루프(loop)는 반복 출력 줄을 나타낸다고 설명한다(5). |
| 7–19 | Basic file structure — RUNDES·RUNID·AGRID와 NDSETSE·NP를 포함한 헤더(header)를 적는다(7·9). NDSETSE개 데이터 집합(dataset)마다 TIME·IT를 쓰고 NP개 절점의 k·nodecode(k)를 출력한다(11–18). 두 루프의 순서와 종료, 모든 형식 줄을 원문 그대로 옮긴다. 원문: `[RUNDES](/index.php?title=RUNDES&action=edit&redlink=1), [RUNID](/index.php?title=RUNID&action=edit&redlink=1), [AGRID](/index.php?title=AGRID&action=edit&redlink=1)` (7); `[NDSETSE](/index.php?title=NDSETSE&action=edit&redlink=1), [NP](/index.php?title=NP&action=edit&redlink=1), [DTDP](/DTDP)*[NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1), [NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1), [IRTYPE](/index.php?title=IRTYPE&action=edit&redlink=1)` (9); `for j=1, [NDSETSE](/index.php?title=NDSETSE&action=edit&redlink=1)` (11); `[TIME](/index.php?title=TIME&action=edit&redlink=1), [IT](/index.php?title=IT&action=edit&redlink=1)` (13); `for k=1, [NP](/index.php?title=NP&action=edit&redlink=1)` (14); `k, [nodecode(k)](/index.php?title=Nodecode(k)&action=edit&redlink=1)` (15); `end k loop` (16); `end j loop` (18). |
| 20–24 | Notes — ASCII 형식만 지원한다(22). 전체 영역 수면 고도(full domain water surface elevation) fort.63과 같은 일정으로 출력한다고 적는다(22). TOUTSGE·TOUTFGE·NSPOOLGE 이름이 나온다(22). 값은 정수(integer)이다(24). 원문의 일정 문장을 그대로 옮긴다. 원문: `Output is only available in the ascii format. The data are produced on the same schedule as the full domain water surface elevation (fort.63) file, i.e., the values of [TOUTSGE](/index.php?title=TOUTSGE&action=edit&redlink=1), [TOUTFGE](/index.php?title=TOUTFGE&action=edit&redlink=1), are used [NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1).` (22); `The nodecode.63 file contains integer values.` (24). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 22행: 일정 설명의 끝은 `are used [NSPOOLGE]` 순서이다. NSPOOLGE 앞에 열거를 이어 주는 문구가 없다.
- 7·9·11·13·14·15·22행: 출력 변수와 일정 매개변수의 위키 링크에 `action=edit&redlink=1`이 있다.
