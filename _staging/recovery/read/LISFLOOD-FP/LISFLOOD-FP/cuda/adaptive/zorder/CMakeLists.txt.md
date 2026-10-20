---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/CMakeLists.txt
lines: 12
sha256: 669bedd995e791fd5e83f8dde59eb79e0f021f9df1cb0a380cc12dcc1ffe6efc
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# CMakeLists.txt — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–12 | `target_sources(` (1)의 대상은 `lisflood` (2), 가시성은 `PRIVATE` (3)이다. 이 하위 디렉터리의 컴파일 대상 파일 목록은 `copy_finest_coefficients.cu` (4), `generate_all_morton_codes.cu` (5), `get_sorting_indices.cu` (6), `rev_z_order_act_idcs.cu` (7), `rev_z_order_assem_sol.cu` (8), `rev_z_order_reals.cu` (9), `sort_finest_scale_coeffs_z_order.cu` (10), `sort_neighbours_z_order.cu` (11)이다. `)` (12)로 명령을 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
