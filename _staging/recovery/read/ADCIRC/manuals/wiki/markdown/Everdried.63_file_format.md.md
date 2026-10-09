---
file: models/ADCIRC/raw/manuals/wiki/markdown/Everdried.63_file_format.md
lines: 31
sha256: 43a11894e951dd13e043af7ef6f538f7ad6c34b030bc26f256dac5dab97f1d87
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Everdried.63_file_format.md — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | 제목·판본 표기·빈 줄을 포함한다(1–4). 파일 구조 안내 — 출력의 각 줄을 변수 이름으로 표현하며 빈 줄은 가독성용이고 반복문은 여러 출력 줄을 뜻한다고 설명한다(5). |
| 7–18 | 첫 자료집합 — `RUNDES`·`RUNID`·`AGRID`, 상수 `2`·`NP`·`DTDP*NSPOOLGE`·`NSPOOLGE`·`IRTYPE`, `TIME`·`IT`, `k`·`everdried(k)`를 쓰는 반복 구조를 제시한다(7–17). 헤더·변수·곱셈식·반복문·종료문을 원문 그대로 옮긴다. 원문: `[RUNDES](/index.php?title=RUNDES&action=edit&redlink=1), [RUNID](/index.php?title=RUNID&action=edit&redlink=1), [AGRID](/index.php?title=AGRID&action=edit&redlink=1)` (7); `2, [NP](/index.php?title=NP&action=edit&redlink=1), [DTDP](/DTDP)*[NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1), [NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1), [IRTYPE](/index.php?title=IRTYPE&action=edit&redlink=1)` (9); `[TIME](/index.php?title=TIME&action=edit&redlink=1), [IT](/index.php?title=IT&action=edit&redlink=1)` (11); `for k=1, [NP](/index.php?title=NP&action=edit&redlink=1)` (13); `k, [everdried(k)](/index.php?title=Everdried(k)&action=edit&redlink=1)` (15); `end k loop` (17). |
| 19–26 | 둘째 자료집합 — `TIME`·`IT`, `k`·`driedtime(k)`를 쓰는 반복 구조를 제시한다(19–25). 헤더·변수·반복문·종료문을 원문 그대로 옮긴다. 원문: `[TIME](/index.php?title=TIME&action=edit&redlink=1), [IT](/index.php?title=IT&action=edit&redlink=1)` (19); `for k=1, [NP](/index.php?title=NP&action=edit&redlink=1)` (21); `k, [driedtime(k)](/index.php?title=Driedtime(k)&action=edit&redlink=1)` (23); `end k loop` (25). |
| 27–31 | Notes — ASCII 또는 netCDF는 `fort.15`의 `NOUTGE`에 의존한다(29). 시간 적분(timestepping)이 끝난 뒤 기록하며 재시작(hotstart)을 했어도 현재 실행만 반영한다(31). 원문: `Output may be in ascii or netCDF format depending on how [NOUTGE](/index.php?title=NOUTGE&action=edit&redlink=1) is set in the [fort.15 file](/Fort.15_file).` (29); `The everdried.63 file is written at the very end of the simulation, after timestepping is complete. The values only reflect the current run, even if the run was hotstarted.` (31). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 7·9·11·13·15·19·21·23·29: RUNDES·RUNID·AGRID·NP·NSPOOLGE·IRTYPE·TIME·IT·everdried(k)·driedtime(k)·NOUTGE 링크에는 `action=edit&redlink=1`이 붙어 있다.
