---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/CMakeLists.txt
lines: 10
sha256: 3b1aaed7bc1bb3fbd51c0124cd8cf96c2dc60d2762db47501d23b7f6610b47b8
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# CMakeLists.txt — 판독 구간 기록

구간은 1행부터 10행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–10 | `target_sources(` (1)의 대상은 `lisflood` (2), 가시성은 `PRIVATE` (3)이다. 이 하위 디렉터리의 컴파일 대상 파일 목록은 `copy_to_buf_assem_sol.cu` (4), `dg2_update.cu` (5), `friction_implicit.cu` (6), `fv1_update.cu` (7), `get_dt_CFL.cu` (8), `limit_slopes.cu` (9)이다. `)` (10)로 명령을 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
