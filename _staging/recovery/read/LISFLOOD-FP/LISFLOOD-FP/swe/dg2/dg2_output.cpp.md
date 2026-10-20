---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/dg2/dg2_output.cpp
lines: 26
sha256: 8ccf402b94042f85106953e9c943187efe17613199773d69afcc8197b11146d1
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# dg2_output.cpp — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | dg2_output.h와 상위 output.h를 포함한다(1–2). write_solution_slopes는 파일명·상태·격자·해석기·배열 포인터를 받는다(4–11). `if (Statesptr->save_depth == ON)` (13)이면 `write_field(Arrptr->H1x, ".wd1x", ".wd1xb", Fnameptr, Statesptr, Parptr);` (15), `write_field(Arrptr->H1y, ".wd1y", ".wd1yb", Fnameptr, Statesptr, Parptr);` (16)의 write_field로 H1x·H1y를 .wd1x/.wd1xb·.wd1y/.wd1yb에 쓴다. 확장자 선택 내부는 이 함수 밖이다. 이 파일에는 전처리 조건이 없다. |
| 19–26 | 시작 시 4행 write_solution_slopes 안. `if (Statesptr->save_Qs == ON)` (19)이면 `write_field(Arrptr->HU1x, ".Qx1x", ".Qx1xb", Fnameptr, Statesptr, Parptr);` (21), `write_field(Arrptr->HU1y, ".Qx1y", ".Qx1yb", Fnameptr, Statesptr, Parptr);` (22), `write_field(Arrptr->HV1x, ".Qy1x", ".Qy1xb", Fnameptr, Statesptr, Parptr);` (23), `write_field(Arrptr->HV1y, ".Qy1y", ".Qy1yb", Fnameptr, Statesptr, Parptr);` (24)의 write_field로 HU1x·HU1y·HV1x·HV1y를 각 .Qx1x/.Qx1xb·.Qx1y/.Qx1yb·.Qy1x/.Qy1xb·.Qy1y/.Qy1yb 이름으로 쓴다. 분기·함수를 닫는다(25–26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9·12–26: Solverptr 인수는 함수 본문에서 사용되지 않는다.
