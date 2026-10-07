---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Utilities/mod_Variables_MPI_MapGatherSort.f90
lines: 105
sha256: e35abf24cd9882bca13f63709535819a042aa925990e54bcee2187c72541fa0c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_Variables_MPI_MapGatherSort.f90 — 판독 구간 기록

구간은 1행부터 105행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | EFDC+ 표제·저작권·GPLv2 안내(1–8). Variables_MPI_MapGatherSort 머리말·저자·2019-01-09 날짜(9–16). 모듈 시작·GLOBAL 사용·implicit none·빈 줄(17–22). |
| 23–33 | 시작 시 17행 Variables_MPI_MapGatherSort 선언부 안. 지역(local) 해(solution)를 펼친 real(4) Soln_Local_1D와 정렬 전 전역(global) 해 Soln_Global_1D를 선언한다(23–24). 지역 L에서 전역 L로의 매핑(mapping) 정수 Map_Local_L_to_Global와 전체 프로세스 수집 Global_Local_L_to_Global(25–26). 정수 해 Int_Soln_Local_1D/Int_Soln_Global_1D(28–29), real(rkd) 해 Soln_Local_1D_RK8/Soln_Global_1D_RK8(31–32). 모두 1차원 allocatable 배열이며 빈 줄 포함(27·30·33). |
| 34–59 | 시작 시 17행 Variables_MPI_MapGatherSort 선언부 안. real(4) 1·2·3차원 포인터(pointer) 형식 pointer_soln_1D/2D/3D_Real(35–45). 기본 포인터 연결 상태는 `real(4), Pointer :: val(:) => null()` (36), `real(4), Pointer :: val(:,:) => null()` (40), `real(4), Pointer :: val(:,:,:) => null()` (44)이다. RK8 이름 형식은 real(rkd) 1·2·3차원을 사용한다(48–58). 기본 상태는 `real(rkd), Pointer :: val(:) => null()` (49), `real(rkd), Pointer :: val(:,:) => null()` (53), `real(rkd), Pointer :: val(:,:,:) => null()` (57)이다. 구분 주석·빈 줄(34·38·42·46–47·51·55·59). |
| 60–72 | 시작 시 17행 Variables_MPI_MapGatherSort 선언부 안. 정수 1·2·3차원 포인터 형식 pointer_soln_1D/2D/3D_Int를 선언한다(61–71). 기본 상태는 `integer, Pointer :: val(:) => null()` (62), `integer, Pointer :: val(:,:) => null()` (66), `integer, Pointer :: val(:,:,:) => null()` (70)이다. 구분 주석·빈 줄(60·64·68·72). |
| 73–92 | 시작 시 17행 Variables_MPI_MapGatherSort 선언부 안. real(4)의 1·2·3차원 포인터 형식별로 Local_Arrays_to_Write와 Global_Arrays_to_Write 배열을 각각 Dimension(100)으로 선언한다(74–81). real(rkd)의 RK8 이름 1·2·3차원 형식에도 지역·전역 배열을 각각 Dimension(100)으로 선언한다(84–91). 자료형 구분 주석과 빈 줄을 포함한다(73·76·79·82–83·86·89·92). |
| 93–105 | 시작 시 17행 Variables_MPI_MapGatherSort 선언부 안. 정수 포인터 형식의 1·2·3차원 각각에 지역·전역 등록 배열을 Dimension(100)으로 선언한다(94–101). 자료형·차원 구분용 정수 Dim_Array_Written_Out도 Dimension(100)이며 선언 초기값은 없다(103). 빈 줄·모듈 종료(102·104–105). 이 파일은 선언만 포함하고 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 43·56·69: 3D 이름 포인터 형식의 설명 주석은 각각 “2D arrays”라고 적는다. 실제 val 선언은 세 차원이다(44·57·70).
- 74–103: 모든 Local/Global_Arrays_to_Write 배열과 Dim_Array_Written_Out의 크기는 100으로 고정되어 있다.
- 36–70·103: 포인터 val 필드 9개는 null()로 선언 초기화한다. Dim_Array_Written_Out 선언에는 초기값이 없다.

