---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/write_raster_maps.cu
lines: 202
sha256: 62fa83fd4cd718773f53716f03bf705ecac8339a75d3f95b38877641227fc943
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_raster_maps.cu — 판독 구간 기록

구간은 1행부터 202행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | 헤더 포함(1), 호스트(host) 함수 `__host__ void lis::cuda::acc_nugrid::write_raster_maps` (3)의 인수·작업 배열 선언(4–37). 파일 내 전처리 조건 분기는 없다. 셀 크기와 원점은 pars.dx·blx·bly, 출력 크기는 pars.xsz·ysz에서 받는다(19–29). 결측값 기본 설정 `int NODATA_value = -9999;` (24). 호스트 배열 h·z0의 길이는 각각 `NUMERIC_TYPE* h  = new NUMERIC_TYPE[mesh_dim * mesh_dim];`<br>`NUMERIC_TYPE* z0  = new NUMERIC_TYPE[mesh_dim * mesh_dim];` (31–32), 복사 바이트 수는 `size_t bytes = mesh_dim * mesh_dim * sizeof(NUMERIC_TYPE);` (34). copy_cuda로 두 배열을 복사한다(36–37). |
| 39–73 | 수심(water depth) 출력 블록. SaveNo를 4자리 형식으로 붙인 .wd 파일을 wb로 연다(41–43). `if (NULL == fp)` (45)이면 오류 출력 후 exit(-1)(47–48). 열·행·원점·셀 크기·결측값 머리를 쓴다(51–56). `for (int j = 0; j < nrows; j++)` (58), `for (int i = 0; i < ncols; i++)` (60)에서 `int idx = (nrows - 1 - j) * mesh_dim + i;` (62)로 행 방향을 뒤집는다. 주석의 대체 인덱스는 `//			int idx = j * mesh_dim + i;` (63). 출력의 삼항 연산자는 `fprintf(fp, "%.*" NUM_FMT "\t", precision, (h[idx] < C(0.0)) ? C(0.0) : h[idx]);` (65)이며, 음수 수심은 C(0.0)으로 쓴다. 행 끝 개행·fclose(68–71). |
| 74–108 | 시작 시 3–12행 write_raster_maps 함수 안. 수위(water elevation) 출력은 전부 주석이다(75–106). 주석 조건 `//if (NULL == fp)` (81), 주석 루프 `//for (int j = 0; j < nrows; j++)` (94), `//	for (int i = 0; i < ncols; i++)` (96), 주석 인덱스 `//		int idx = j * mesh_dim + i;` (98), 주석 출력식 `//		fprintf(fp, "%.15" NUM_FRMT " ", h[idx] + z[idx]);` (100)을 포함한다. 이 블록은 파일을 열거나 쓰지 않는다. |
| 109–148 | 시작 시 3–12행 write_raster_maps 함수 안. x방향 속도 출력은 전부 주석이다(110–146). 주석 조건 `//if (NULL == fp)` (119), 주석 루프 `//for (int j = 0; j < nrows; j++)` (132), `//	for (int i = 0; i < ncols; i++)` (134), 주석 인덱스 `//		int idx = j * mesh_dim + i;` (136), 주석 계산식 `//		NUMERIC_TYPE vx = qx[idx] / h[idx];` (138)을 포함한다. 경로 문자열 초기화·열기·머리·값 출력·닫기도 주석이다. |
| 149–188 | 시작 시 3–12행 write_raster_maps 함수 안. y방향 속도 출력은 전부 주석이다(150–186). 주석 조건 `//if (NULL == fp)` (159), 주석 루프 `//for (int j = 0; j < nrows; j++)` (172), `//	for (int i = 0; i < ncols; i++)` (174), 주석 인덱스 `//		int idx = j * mesh_dim + i;` (176), 주석 계산식 `//		NUMERIC_TYPE vy = qy[idx] / h[idx];` (178)을 포함한다. 경로 문자열 초기화·열기·머리·값 출력·닫기도 주석이다. |
| 189–202 | 시작 시 3–12행 write_raster_maps 함수 안. `if (call_gzip == ON)` (191)이면 sprintf로 gzip 명령을 조립하고 system으로 실행한다(193–194). h만 delete[]로 해제한다(197). qx·qy 해제문은 주석(198–199). 구분 주석·함수 종료(201–202). ON의 정의·값은 이 파일에 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 31–37·197–202: z0는 할당·copy_cuda 후 출력식에서 사용되지 않는다. 함수 말미의 실행되는 delete[]는 h에 대해서만 있다.
- 75–186: 수위와 x·y방향 속도 출력 블록은 모두 주석이다. 실행되는 래스터 출력은 .wd 블록(39–71)이다.
- 13–14·41·193–194: 출력 경로 버퍼는 800자이고 gzip 명령 버퍼는 255자이다. gzip 명령 조립에는 길이 제한 인수가 없는 sprintf를 쓴다.
- 24·65: NODATA_value 머리는 -9999이다. 데이터 출력은 h[idx]가 음수이면 C(0.0)으로 바꾼다.
