---
file: models/ADCIRC/raw/manuals/wiki/markdown/Endrisinginun.63_file_format.md
lines: 23
sha256: f34d3c69e083fed59adf618838546087ae57dc07f416acd355592c4ad844f421
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Endrisinginun.63_file_format.md — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | 제목·판본 표기·빈 줄을 포함한다(1–4). 파일 구조 안내 — 출력의 각 줄을 변수 이름으로 표현하며 빈 줄은 가독성용이고 반복문은 여러 출력 줄을 뜻한다고 설명한다(5). |
| 7–18 | 출력 구조 — `RUNDES`·`RUNID`·`AGRID`, 상수 `1`·`NP`·`DTDP*NSPOOLGE`·`NSPOOLGE`·`IRTYPE`, `TIME`·`IT`, `k`·`endrisinginun(k)`를 쓰는 반복 구조를 제시한다(7–17). 헤더·변수·곱셈식·반복문·종료문을 원문 그대로 옮긴다. 원문: `[RUNDES](/index.php?title=RUNDES&action=edit&redlink=1), [RUNID](/index.php?title=RUNID&action=edit&redlink=1), [AGRID](/index.php?title=AGRID&action=edit&redlink=1)` (7); `1, [NP](/index.php?title=NP&action=edit&redlink=1), [DTDP](/DTDP)*[NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1), [NSPOOLGE](/index.php?title=NSPOOLGE&action=edit&redlink=1), [IRTYPE](/index.php?title=IRTYPE&action=edit&redlink=1)` (9); `[TIME](/index.php?title=TIME&action=edit&redlink=1), [IT](/index.php?title=IT&action=edit&redlink=1)` (11); `for k=1, [NP](/index.php?title=NP&action=edit&redlink=1)` (13); `k, [endrisinginun(k)](/index.php?title=Endrisinginun(k)&action=edit&redlink=1)` (15); `end k loop` (17). |
| 19–23 | Notes — ASCII 또는 netCDF는 `fort.15`의 `NOUTGE`에 의존한다(21). 시간 적분(timestepping)이 끝난 뒤 기록하며 재시작(hotstart)을 했어도 현재 실행만 반영한다(23). 초기 건조(initially dry) 절점에서만 상승 수위를 표시한다(23). 조건을 원문 그대로 옮긴다. 원문: `Output may be in ascii or netCDF format depending on how [NOUTGE](/index.php?title=NOUTGE&action=edit&redlink=1) is set in the [fort.15 file](/Fort.15_file)` (21); `The endrisinginun.63 file is written at the very end of the simulation, after timestepping is complete. The values only reflect the current run, even if the run was hotstarted. The data in the endrisinginun.63 file only flag rising water surface elevation in areas that are initially dry, according to the [initiallydry.63 file](/Initiallydry.63_file).` (23). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 7·9·11·13·15·21: RUNDES·RUNID·AGRID·NP·NSPOOLGE·IRTYPE·TIME·IT·endrisinginun(k)·NOUTGE 링크에는 `action=edit&redlink=1`이 붙어 있다.
