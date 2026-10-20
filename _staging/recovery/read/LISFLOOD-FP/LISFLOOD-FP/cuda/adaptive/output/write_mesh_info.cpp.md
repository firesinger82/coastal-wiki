---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_mesh_info.cpp
lines: 38
sha256: 8a1cb5997b31ec47d3588778b2e839a66ac9b1c547ee590709a6fabad1c1db94
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_mesh_info.cpp — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | `#include "write_mesh_info.h"` (1)와 `write_mesh_info` 정의·인수(3–9). 모의 설정, 격자(mesh) 차원, 디렉터리를 받는다(5–7). 길이 255의 경로 버퍼를 초기화한다(10). `sprintf(fullpath, "%s%c%s", dirroot, '/', "mesh_info.csv");` (12)로 경로를 만들고 `fopen(fullpath, "w")`로 연다(14). `if (NULL == fp)` (16)이면 표준 오류 출력 뒤 `exit(-1)`을 호출한다(18–19). 빈 줄도 포함된다. 이 파일에는 조건부 전처리 분기가 없다. |
| 22–38 | 시작 시 3–9행 `write_mesh_info` 본문 안이며 16행 오류 분기 밖. `mesh_dim,xmin,xmax,ymin,ymax,xsz,ysz` 열 이름을 출력한다(22). `fprintf` (24–35)는 정수 형식과 `NUM_FRMT` (27)를 사용한다. 값은 `mesh_dim`, `sim_params.xmin`, `sim_params.xmax`, `sim_params.ymin`, `sim_params.ymax`, `sim_params.xsz`, `sim_params.ysz` 순서다(28–34). `fclose(fp)`를 호출하고 루틴을 닫는다(37–38). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10·12: 경로 버퍼 크기는 255로 고정되어 있다. 경로 작성에는 `sprintf`를 사용한다. 이 함수에는 경로 길이 검사문이 없다.
