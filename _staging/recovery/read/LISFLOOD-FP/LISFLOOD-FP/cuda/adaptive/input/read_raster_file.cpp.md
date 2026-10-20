---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_raster_file.cpp
lines: 48
sha256: 208938ea1b5d22d414e9d665b229d7c6e76388a5cd15808b1f81d848043fde32
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_raster_file.cpp — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | read_raster_file 헤더를 포함하고 래스터(raster) 입력 루틴을 정의한다(1–10). 인수는 파일명·실수 배열·정사각 격자 폭 mesh_dim·벽 높이 wall_height이다. 255바이트 buf와 nrows/ncols=0, dummy=C(0.0)를 준비하고 fopen으로 연다(11–18). 조건부 전처리 분기는 없다. |
| 19–32 | 시작 시 3행 read_raster_file 루틴 안. 파일 열기 실패 분기는 로그 후 배열을 변경하지 않고 반환한다(20–24). 첫 두 헤더에서 ncols와 nrows를 읽고 나머지 네 헤더의 수치를 dummy로 읽는다(26–31). 수치 입출력 서식에는 NUM_FRMT 매크로(macro)를 쓴다. 원문: `if (NULL == fp)` (20); `fscanf(fp, "%s %d", buf, &ncols);` (26); `fscanf(fp, "%s %d", buf, &nrows);` (27); `fscanf(fp, "%s %" NUM_FRMT, buf, &dummy);` (28); `fscanf(fp, "%s %" NUM_FRMT, buf, &dummy);` (29); `fscanf(fp, "%s %" NUM_FRMT, buf, &dummy);` (30); `fscanf(fp, "%s %" NUM_FRMT, buf, &dummy);` (31). |
| 33–48 | 시작 시 3행 read_raster_file 루틴 안. 행·열 루프(loop)를 돈다(33·35). -9999와의 차이가 C(1e-10) 미만이면 nodata로 표시한다(39). 행 순서를 뒤집은 주소에 nodata이면 wall_height, 아니면 dummy를 저장한다(41). 지역 정수 a를 1로 초기화한다(43). 두 루프를 닫고 fclose로 끝낸다(44–48). 원문: `for (int j = 0; j < nrows; j++)` (33); `for (int i = 0; i < ncols; i++)` (35); `bool nodata = ( fabs( dummy + C(9999.0) ) < C(1e-10) );` (39); `raster_array[ (nrows - 1 - j) * mesh_dim + i ] = (nodata) ? wall_height : dummy;` (41). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26–31·37: fscanf 반환값을 검사하는 문장이 없다. 읽은 nrows/ncols와 mesh_dim을 비교하는 조건도 없다.
- 28–31·39: 헤더의 네 수치는 같은 dummy에 덮어쓴다. nodata 판별 상수는 헤더 값과 별개인 C(9999.0)이다.
- 43: a는 1로 초기화된 뒤 이 파일에서 사용되지 않는다.
