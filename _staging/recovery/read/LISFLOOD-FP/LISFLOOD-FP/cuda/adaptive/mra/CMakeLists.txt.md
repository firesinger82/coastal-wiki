---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/CMakeLists.txt
lines: 28
sha256: b5a8d07728d1295bfd661fe2fa4fb116aa313b9758cfac789b7be475529e23d1
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# CMakeLists.txt — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–28 | `target_sources(` (1)의 대상은 `lisflood` (2), 가시성은 `PRIVATE` (3)이다. 이 하위 디렉터리의 컴파일 대상 파일 목록은 `decoding.cu` (4), `decoding_all.cu` (5), `encode_and_thresh_flow.cu` (6), `encode_and_thresh_topo.cu` (7), `encoding_all.cu` (8), `extra_significance.cu` (9), `get_max_from_array.cu` (10), `get_max_scale_coeffs.cu` (11), `get_modal_values.cu` (12), `get_nodal_values.cu` (13), `get_reg_tree.cu` (14), `init_eta_temp.cu` (15), `init_nodal_values.cu` (16), `init_sig_details.cu` (17), `insert_point_srcs.cu` (18), `modal_projections.cu` (19), `preflag_details.cu` (20), `preflag_topo.cu` (21), `regularisation.cu` (22), `refine_high_wall.cu` (23), `reinsert_assem_sol.cu` (24), `reinsert_point_srcs.cu` (25), `traverse_tree_of_sig_details.cu` (26), `zero_details.cu` (27)이다. `)` (28)로 명령을 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
