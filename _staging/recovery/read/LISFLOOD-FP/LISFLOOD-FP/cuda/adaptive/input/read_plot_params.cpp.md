---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_plot_params.cpp
lines: 38
sha256: 39033e4895519fa62e66b9b52723e9258d12030350c2a41c727e66c3d96b0b22
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_plot_params.cpp — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 자기 헤더 포함(1). read_plot_params는 입력 파일명을 받아 PlottingParams()로 객체를 생성한다(3–8). `plot_params.vtk           = read_keyword_bool(input_filename, "vtk", 3);` (10), `plot_params.c_prop        = read_keyword_bool(input_filename, "c_prop", 6);` (11), `plot_params.raster_out    = read_keyword_bool(input_filename, "raster_out", 10);` (12), `plot_params.voutput_stage = read_keyword_bool(input_filename, "voutput_stage", 13);` (13), `plot_params.cumulative    = read_keyword_bool(input_filename, "cumulative", 10);` (14)로 출력 표지를 판독한다. read_keyword_str로 resroot와 dirroot를 읽는다(16–17). 전처리 조건 분기는 없다. |
| 19–31 | 시작 시 3행 함수 안. `if (plot_params.resroot[0] == '\0')` (20)이면 기본 결과 파일 접두사(prefix)를 `sprintf(plot_params.resroot, "%s", "res");` (23)으로 설정한다. 별도 `if (plot_params.dirroot[0] == '\0')` (27)이면 기본 결과 디렉터리(directory)를 `sprintf(plot_params.dirroot, "%s", "res");` (30)으로 설정한다. 두 기본 문자열은 res다. |
| 32–38 | 시작 시 3행 함수 안. 명령 버퍼를 널 문자로 초기화한다(33). `sprintf(sys_cmd_str_buf, "%s%s", "mkdir ", plot_params.dirroot);` (34)로 mkdir 명령 문자열을 만들고 `system(sys_cmd_str_buf);` (35)로 실행한다. plot_params를 반환하고 함수를 닫는다(37–38). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 34–35: mkdir 명령 문자열은 "mkdir "와 dirroot를 직접 연결하여 만든다. 경로를 감싸는 따옴표를 추가하는 문장은 없다.
- 35: system 반환값을 저장하거나 검사하는 문장은 없다.
