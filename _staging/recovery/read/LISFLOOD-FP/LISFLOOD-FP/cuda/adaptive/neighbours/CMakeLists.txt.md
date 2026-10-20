---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/neighbours/CMakeLists.txt
lines: 9
sha256: 1ca1ba4ebf2d5a581f316d828a48bc72796bf7e11a3d07e61882c14ec80ab605
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# CMakeLists.txt — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–9 | `target_sources(` (1)의 대상은 `lisflood` (2), 가시성은 `PRIVATE` (3)이다. 이 하위 디렉터리의 컴파일 대상 파일 목록은 `add_ghost_cells.cu` (4), `compaction.cu` (5), `find_neighbours.cu` (6), `get_compaction_flags.cu` (7), `load_soln_and_nghbr_coeffs.cu` (8)이다. `)` (9)로 명령을 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
