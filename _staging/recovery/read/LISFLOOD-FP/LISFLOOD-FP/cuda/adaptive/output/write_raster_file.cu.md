---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_raster_file.cu
lines: 55
sha256: 74b262f9ec931df999c48eed0a34510c29879399b93fd6f3b9eefeae83308d64
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_raster_file.cu — 판독 구간 기록

구간은 1행부터 55행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | `#include "write_raster_file.cuh"` (1), CUDA 호스트(host) 지시 `__host__` (3), `write_raster_file` 정의·인수(4–14). 출력 설정, 확장자, 래스터(raster) 실수 배열, 모의 설정, 저장 간격, 최세 격자 간격, 격자 차원을 받는다(6–12). 255바이트 경로 버퍼를 초기화한다(15). 번호 계산을 포함한 원문은 `sprintf(fullpath, "%s%c%s%c%d%c%s", plot_params.dirroot, '/', plot_params.resroot, '-', saveint.count - 1, '.', file_extension);` (17)다. `fopen(fullpath, "w")` (19) 뒤 `if (NULL == fp)` (21)이면 오류 출력과 `exit(-1)`을 실행한다(23–24). 이 파일에는 조건부 전처리 분기가 없다. |
| 26–41 | 시작 시 4–14행 `write_raster_file` 본문 안이며 21행 오류 분기 밖. `xllcorner`·`yllcorner`를 `sim_params.xmin`·`sim_params.ymin`에서 가져온다(27–28). `ncols`·`nrows`를 `sim_params.xsz`·`sim_params.ysz`에서 가져온다(30–31). 결측값(no-data value) 표지는 `int NODATA_value = -9999;` (33)다. 열 수, 행 수, 왼쪽 아래 좌표, `dx_finest` 셀 크기, 결측값 표지를 헤더에 쓴다(35–40). 실수 헤더에는 `NUM_FRMT`를 사용한다(37–39). |
| 42–55 | 시작 시 4–14행 `write_raster_file` 본문 안. `for (int j = 0; j < nrows; j++)` (42) 안에 `for (int i = 0; i < ncols; i++)` (44)가 있다. 인덱스 식은 `int idx = (nrows - 1 - j) * mesh_dim + i;` (46)다. `fprintf(fp, "%" NUM_FIG NUM_FRMT " ", raster[idx]);` (48)로 행 순서를 뒤집어 값을 쓰고, 내부 루프 종료 후 줄바꿈을 출력한다(49–51). 외부 루프 종료 뒤 `fclose(fp)`를 호출하고 루틴을 닫는다(52–55). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 33·40·46–48: 결측값 표지는 `-9999`로 고정되어 있다. 값 출력 루프는 `raster[idx]`를 그대로 쓰며 결측값으로 변환하는 분기는 없다.
- 15·17: 경로 버퍼 크기는 255로 고정되어 있다. 경로 작성에는 `sprintf`를 사용한다. 이 함수에는 경로 길이 검사문이 없다.
