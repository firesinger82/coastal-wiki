---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/read_raster_file.cpp
lines: 50
sha256: 28a51af9ff9bf3699b06032a8238e0ec92e2f1b8478d54a2813751c9e75f41a7
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_raster_file.cpp — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | read_raster_file.h와 cmath를 포함한다(1–2). read_raster_file은 파일명·래스터(raster) 배열 포인터·mesh_dim 상수 참조·no_data 상수 참조를 받는다(4–11). buf[255]를 선언하고(12), 기본값은 `int nrows = 0;` (14); `int ncols = 0;` (15); `NUMERIC_TYPE dummy = C(0.0);` (17); `NUMERIC_TYPE nodata = C(0.0);` (18)이다. 파일을 읽기 모드로 연다(20). `if (NULL == fp)` (22)이면 기본값을 사용한다는 로그를 출력하고 반환한다(24–25). 조건 닫기와 빈 줄도 포함한다. 이 파일 전체에는 조건부 전처리 분기가 없다. |
| 28–50 | 시작 시 4–11행 read_raster_file 함수 안. fscanf로 ncols·nrows, dummy 세 값, nodata를 순서대로 읽는다(28–33). 헤더(header) 키 문자열은 buf에 받는다. `for (int j = 0; j < nrows; j++)` (35) 및 `for (int i = 0; i < ncols; i++)` (37)에서 `fscanf( fp, "%" NUM_FMT, &raster_array[(nrows - 1 - j) * mesh_dim + i] );` (39)로 행 순서를 뒤집어 mesh_dim 간격의 배열에 저장한다. 행 순서를 뒤집지 않는 `//			fscanf( fp, "%" NUM_FMT, &raster_array[j * mesh_dim + i] );` (40)은 주석이다. `if (FABS(raster_array[(nrows - 1 - j) * mesh_dim + i] - nodata) < 1e-5 )` (41)일 때 `raster_array[(nrows - 1 - j) * mesh_dim + i] = no_data;` (43)으로 입력 결측값을 no_data로 치환한다. 허용 오차는 원문 그대로 1e-5이다. 조건·반복을 닫고 fclose 후 함수를 닫는다(44–50). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22–25: 파일을 열지 못하면 기본값을 사용한다는 로그를 출력한다. 해당 분기에는 raster_array에 값을 대입하는 문장이 없다.
- 28–39: 입력 nrows·ncols와 mesh_dim 또는 배열 크기를 비교하는 분기가 없다.
- 28–33·39: fscanf 반환값을 검사하지 않는다. 헤더 키를 읽는 %s에 필드 폭이 없고, 읽은 키 문자열의 내용도 비교하지 않는다.
