---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_and_project_modes_fv1.cu
lines: 60
sha256: ff68bfd86e344047daa91ac51c17d3c98f4b0c57ed66089677f9898536507ed5
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_and_project_modes_fv1.cu — 판독 구간 기록

구간은 1행부터 60행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 자기 선언 헤더 포함(1). `__host__` (3) 호스트 함수(host function)는 파일명·조립 해(assembled solution)·격자 크기·해법 매개변수를 받는다(4–10). 전처리 조건 분기는 없다. 수심·두 방향 유량·수치표고모형(digital elevation model, DEM) 파일명 버퍼를 널 문자로 초기화한다(12–15). DEMfile을 읽는다(17). `if (dem_filename_buf[0] == '\0')` (20)이면 오류 출력(22). startfile을 읽는다(25). |
| 27–48 | 시작 시 4행 함수 안. h·qx·qy·dem 배열을 조립 해 길이로 값 초기화하여 할당한다(27–30). `for (int i = 0; i < d_assem_sol.length; i++)` (32)에서 dem[i]에 wall_height를 복사한다(34). read_raster_file로 수심과 DEM을 읽는다(37–38). `if (solver_params.startq2d)` (40)이면 .Qx·.Qy 파일명을 만들고(42–43) 두 유량 래스터(raster)를 read_raster_file로 읽는다(45–46). |
| 49–60 | 시작 시 4행 함수 안. `size_t bytes = d_assem_sol.length * sizeof(real);` (49). copy_cuda로 h·qx·qy·dem을 d_assem_sol.h0·qx0·qy0·z0에 전달한다(51–54). 네 호스트 배열을 delete[]로 해제하고 함수를 닫는다(56–60). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20–23: DEM 파일명 버퍼가 비어 있으면 오류를 출력하지만 이 조건 블록에는 exit 또는 return이 없다.
