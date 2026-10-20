---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/read_point_srcs.cu
lines: 92
sha256: 9e69f97353d2e38daaa08402fdc12d48a98ab315dc8f7e165857b79b0e30e6d1
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_point_srcs.cu — 판독 구간 기록

구간은 1행부터 92행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | 대응 헤더 포함과 read_point_srcs 정의(1–12). 두 파일명, Pars·time_now 상수 참조, PointSources 참조 및 BoundCs 상수 참조를 받는다(5–10). str[255] 선언(13). `if (strlen(bcifilename) == 0)` (15)이면 로그는 주석인 채 반환한다(17–18). fopen으로 경계 조건(boundary condition) 파일을 읽기 모드로 연다(21). `if (NULL == fp)` (23)이면 오류 출력 후 exit(-1)한다(25–26). 조건 닫기와 빈 줄도 포함한다. 이 파일 전체에는 조건부 전처리 분기가 없다. |
| 31–55 | 시작 시 3–12행 read_point_srcs 함수 안. 기본값은 `NUMERIC_TYPE x_stage = C(0.0);` (31); `NUMERIC_TYPE y_stage = C(0.0);` (32)·`int x = 0;` (34); `int y = 0;` (35)·`char point = '\0';` (37); `char inlet_type_buf[8] = { '\0' };` (38); `int  srcs_counted = 0;` (39)이다. `while (srcs_counted < point_sources.num_srcs)` (41)에서 fgets를 호출하고(43), `sscanf(str, "%c %" NUM_FMT " %" NUM_FMT " %s", &point, &x_stage, &y_stage, inlet_type_buf);` (45)로 줄을 해석한다. `if (point == 'P')` (47)일 때 이전 좌표식 `//			x =                  (x_stage - params.xmin) / params.cell_size;` (49); `//			y = params.ysz - (y_stage - params.ymin) / params.cell_size;` (50)은 주석이고 활성 변환식은 `x = (x_stage - pars.blx) / pars.dx;` (51); `y = (y_stage - pars.bly) / pars.dx;` (52)이다. `point_sources.h_codes[srcs_counted] = generate_morton_code(x, y);` (54)로 점 유입원(point source)의 Morton 코드(Morton code)를 저장한다. 반복과 P 조건은 다음 구간까지 이어진다. |
| 56–80 | 시작 시 3–12행 read_point_srcs 함수·41행 srcs_counted 반복·47행 point == 'P' 참 분기 안. `if (!strncmp(inlet_type_buf, "HFIX", 4))` (56)이면 HFIX 형식을 저장하고(58), `sscanf(str, "%c %" NUM_FMT " %" NUM_FMT " %s %" NUM_FMT, &point, &x_stage, &y_stage, inlet_type_buf, &point_sources.h_srcs[srcs_counted]);` (59)로 고정값을 읽는다. `else if (!strncmp(inlet_type_buf, "HVAR", 4))` (61)이면 HVAR 형식을 저장하고(63), `sscanf(str, "%c %" NUM_FMT " %" NUM_FMT " %s %s", &point, &x_stage, &y_stage, inlet_type_buf, &point_sources.timeseries[srcs_counted * 32]);` (64)로 시계열(time series) 이름을 읽는다. `else if (!strncmp(inlet_type_buf, "QFIX", 4))` (66)이면 QFIX 형식을 저장하고(68), `sscanf(str, "%c %" NUM_FMT " %" NUM_FMT " %s %" NUM_FMT, &point, &x_stage, &y_stage, inlet_type_buf, &point_sources.h_srcs[srcs_counted]);` (69)로 고정값을 읽는다. `else if (!strncmp(inlet_type_buf, "QVAR", 4))` (71)이면 QVAR 형식을 저장하고(73), `sscanf(str, "%c %" NUM_FMT " %" NUM_FMT " %s %s", &point, &x_stage, &y_stage, inlet_type_buf, &point_sources.timeseries[srcs_counted * 32]);` (74)로 시계열 이름을 읽는다. 각 else if는 이전 조건이 모두 거짓일 때 평가한다. 최종 else는 없다. P 분기에서는 형식과 관계없이 `srcs_counted++;` (77)을 실행한다. P 조건과 반복을 닫고 빈 줄을 포함한다(78–80). |
| 81–92 | 시작 시 3–12행 read_point_srcs 함수 안이며 41행 반복 밖. fclose로 파일을 닫는다(81). 전송 바이트 수 원문은 `size_t bytes_codes = sizeof(MortonCode) * point_sources.num_srcs;` (83); `size_t bytes_srcs = sizeof(NUMERIC_TYPE) * point_sources.num_srcs;` (84); `size_t bytes_src_types = sizeof(int) * point_sources.num_srcs;` (85)이다. copy_cuda를 세 번 호출하여 h_codes·h_srcs·h_src_types를 각각 d_codes·d_srcs·d_src_types에 복사한다(87–89). point_sources.update_all_sources(bdyfilename, time_now, boundCs)를 호출한다(91). 함수 닫기와 빈 줄도 포함한다(86·90·92). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41–45·77: 반복 종료 조건은 읽은 P 기록 수이다. fgets와 sscanf의 반환값을 검사하는 분기 또는 EOF 처리 분기는 없다.
- 47·56–77: HFIX·HVAR·QFIX·QVAR 중 어느 형식에도 일치하지 않는 P 기록도 srcs_counted를 증가시킨다. 마지막 else에서 형식이나 유입값을 설정하는 문장은 없다.
- 38·45·59·64·69·74: inlet_type_buf의 크기는 8이며 시계열 저장 위치는 srcs_counted * 32로 정한다. 문자열을 읽는 %s에는 필드 폭이 없다.
- 51–54: x와 y 인덱스 모두 pars.dx로 나눈다. Morton 코드 생성 전에 영역 범위를 검사하는 분기는 없다.
