---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.36_file_format.md
lines: 13
sha256: bbd2f59fd5b82cd9e73997d72f3b1cccb616be99170152ca7eddf30cfc5392f1
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.36_file_format.md — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | Fort.36 file format — 문서 제목(1)과 판본 표기 `_revid=464_` (3)를 포함한다. 빈 줄(2·4)을 포함한다. |
| 5–6 | 입력 형식 안내 — 이어지는 줄을 fort.36 입력 파일 형식으로 소개한다(5). |
| 7–13 | 파일 형식 — 자료 묶음(data set) 반복 안에 날짜 주석 줄과 해양 경계 절점(ocean boundary node) 반복을 둔다(7–13). 절점별 줄은 k와 m=1,NFEN에 대한 SALBC(k,m)을 나열한다(11). 빈 줄(8)을 포함한다. 원문: `for i=1 to numberOfDataSets` (7); `comment line (date)` (9); `for k=1 to number_of_ocean_boundary_nodes` (10); `k, (SALBC(k,m), m=1,NFEN)` (11); `end k loop` (12); `end i loop` (13). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 7·10–11: `numberOfDataSets`, `number_of_ocean_boundary_nodes`, `SALBC`, `NFEN`의 정의는 이 파일에 없다. `SALBC`의 단위도 이 파일에 없다.
