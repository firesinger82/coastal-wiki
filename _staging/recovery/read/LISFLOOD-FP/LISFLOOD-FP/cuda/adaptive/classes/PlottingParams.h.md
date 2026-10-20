---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/PlottingParams.h
lines: 62
sha256: 8c48a7f238c16272be4fd309eb76e3a5b129362e9225f4fa918bfbea3d0576c2
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# PlottingParams.h — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | `#pragma once` (1), read_keyword_bool.h·read_keyword_str.h 포함(3–4). 전처리 조건 분기는 없다. PlottingParams의 기본값 선언 전체 `bool vtk           = false;`<br>`bool c_prop        = false;`<br>`bool raster_out    = false;`<br>`bool voutput_stage = false;`<br>`bool voutput       = false;`<br>`bool qoutput       = false;`<br>`bool elevoff       = false;`<br>`bool depthoff      = false;`<br>`bool cumulative    = false;`<br>`char dirroot[128]  = {'\0'};`<br>`char resroot[128]  = {'\0'};` (8–18). vtk·c_prop·raster_out·voutput_stage·voutput·qoutput·elevoff·depthoff·cumulative는 false이고, dirroot·resroot는 128자 빈 문자열이다. |
| 20–37 | 시작 시 6–7행 PlottingParams 구조체 안. 생성자는 input_filename을 받는다(20–24). 키 이름과 길이 상수를 포함한 bool 판독 대입 전체 `this->vtk           = read_keyword_bool(input_filename, "vtk", 3);`<br>`this->c_prop        = read_keyword_bool(input_filename, "c_prop", 6);`<br>`this->raster_out    = read_keyword_bool(input_filename, "raster_out", 10);`<br>`this->voutput_stage = read_keyword_bool(input_filename, "voutput_stage", 13);`<br>`this->voutput       = read_keyword_bool(input_filename, "voutput", 7);`<br>`this->qoutput       = read_keyword_bool(input_filename, "qoutput", 7);`<br>`this->elevoff       = read_keyword_bool(input_filename, "elevoff", 7);`<br>`this->depthoff      = read_keyword_bool(input_filename, "depthoff", 7);`<br>`this->cumulative    = read_keyword_bool(input_filename, "cumulative", 10);` (25–33). resroot·dirroot 문자열은 길이 인수 7을 넘기는 read_keyword_str로 읽는다(35–36). 호출된 판독 함수의 내부 동작은 이 파일에 없다. |
| 38–54 | 시작 시 20–24행 PlottingParams 생성자 안. `if (this->resroot[0] == '\0')` (39)이면 기본 결과 접두사 설정 `sprintf(this->resroot, "%s", "res");` (42). 독립 조건 `if (this->dirroot[0] == '\0')` (46)이면 기본 결과 디렉터리 설정 `sprintf(this->dirroot, "%s", "res");` (49). 두 조건 밖에서 make_output_directory()를 호출한다(52). 생성자 종료(53). |
| 55–62 | 시작 시 6–7행 PlottingParams 구조체 안. make_output_directory는 255자 명령 버퍼를 초기화한다(55–57). 디렉터리 생성 명령 조립·실행 전체 `sprintf(sys_cmd_str_buf, "%s %s", "mkdir", this->dirroot);`<br>`system(sys_cmd_str_buf);` (58–59). 메서드·구조체 종료(60–62). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 55–59: make_output_directory는 mkdir와 dirroot를 공백 하나로 연결해 system에 넘긴다. 경로를 따옴표로 감싸는 코드와 system 반환값을 검사하는 코드는 없다.
