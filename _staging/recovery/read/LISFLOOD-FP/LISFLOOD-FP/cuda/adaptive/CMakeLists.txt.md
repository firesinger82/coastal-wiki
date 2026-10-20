---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/CMakeLists.txt
lines: 13
sha256: 0265163c269a53d7788617587a7be56e931f6be10cf0b34b8d74fc3149042b3f
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# CMakeLists.txt — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–8 | 적응형(adaptive) CUDA 빌드의 하위 디렉터리 등록 명령은 `add_subdirectory(input)` (1), `add_subdirectory(mra)` (2), `add_subdirectory(neighbours)` (3), `add_subdirectory(operators)` (4), `add_subdirectory(output)` (5), `add_subdirectory(utilities)` (6), `add_subdirectory(zorder)` (7)이다. 8행은 빈 줄이다. |
| 9–13 | `target_sources(` (9)의 대상은 `lisflood` (10), 가시성은 `PRIVATE` (11)이다. 컴파일 대상 파일은 `cuda_adaptive_simulate.cu` (12)이며 `)` (13)로 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
