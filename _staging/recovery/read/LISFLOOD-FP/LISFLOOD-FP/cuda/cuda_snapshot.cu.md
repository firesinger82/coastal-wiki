---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_snapshot.cu
lines: 47
sha256: 3af6dfce2ea19b6fb08fe81483953204e7963ef658ed4142d29d25ac50ed35b5
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_snapshot.cu — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `#include "cuda_snapshot.cuh"` (1), `#include "io.h"` (2)와 빈 줄이다. 파일 내부에 전처리 조건 분기는 없다. `VelocityWriter` 생성자는 수심 H, 단위 폭 유량(discharge), 수심 임계값 DepthThresh를 멤버에 복사한다(4–14). |
| 16–30 | `VelocityWriter::operator[]`는 `if (H[idx] > DepthThresh)` (21)일 때 `return discharge[idx] / H[idx];` (23)로 유속(velocity)을 반환한다. `else` (25)는 `return C(0.0);` (27)이다. 함수 끝과 빈 줄을 포함한다(28–30). |
| 31–40 | `ElevationWriter` 생성자는 const 수심 포인터 H와 지형고(digital elevation model, DEM) 포인터 DEM을 멤버에 복사한다(31–39). 빈 줄을 포함한다(40). |
| 41–47 | const `ElevationWriter::operator[]`는 수위(elevation)를 `return DEM[idx] + H[idx];` (46)로 반환한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
