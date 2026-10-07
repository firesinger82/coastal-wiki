---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Mapping/Mod_Assign_Loc_Glob_For_Write.f90
lines: 383
sha256: 3c7d9656e7fb9f9ab054890188e006b809d287aeb3c38a78fb10e480163e0c39
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Mod_Assign_Loc_Glob_For_Write.f90 — 판독 구간 기록

구간은 1행부터 383행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–54 | EFDC+ 출처·저작권·GPLv2 머리말(1–8). EE_*.OUT 이진(binary) 출력 전에 지역(local)·전역(global) 해 배열의 포인터(pointer)를 등록한다는 설명과 인수·저자·날짜 주석(9–25). 모듈 시작(26), GLOBAL·MPI 변수·매핑·MapGatherSort 모듈 사용(28–31), implicit none·save(33–35). 공개 일반 인터페이스(generic interface) `Assign_Loc_Glob_For_Write`가 1·2·3차원 각각 real(4)·real(rkd)·integer의 아홉 절차를 연결한다(37–52). contains와 빈 줄(53–54). |
| 55–86 | 시작 시 26행 Mod_Assign_Loc_Glob_For_Write 모듈 안. 1차원 실수 절차의 주석과 `Assign_Loc_Glob_For_Write_1D_Real` 시작(55–70). index·지역/전역 첫 차원은 intent(in), 두 해 배열은 real(4)·Target·intent(inout)(72–79). 지역·전역 1D_Real 등록 배열의 index.val을 각각 Soln_Local·Soln_Global에 포인터 연결한다(82–83). `Dim_Array_Written_Out(index) = 1` (84). 루틴 종료(86). 조건 분기·외부 호출은 없다. |
| 87–119 | 시작 시 26행 모듈 안. 주석과 `Assign_Loc_Glob_For_Write_1D_Real_RK8` 시작(87–102), GLOBAL 사용(103). 정수 차원·index와 real(rkd)·Target·intent(inout) 해 배열 선언(105–112). 지역·전역 1D_Real_RK8 등록 배열의 index.val을 두 해 배열에 포인터 연결한다(115–116). `Dim_Array_Written_Out(index) = 100 + rkd` (117). 루틴 종료(119). |
| 120–151 | 시작 시 26행 모듈 안. 주석과 `Assign_Loc_Glob_For_Write_1D_Int` 시작(120–135). index·지역/전역 첫 차원은 intent(in), 해 배열은 integer·Target·intent(inout)(137–144). 지역·전역 1D_Int 등록 배열의 index.val을 포인터 연결한다(147–148). `Dim_Array_Written_Out(index) = 10` (149). 루틴 종료(151). |
| 152–187 | 시작 시 26행 모듈 안. 주석과 `Assign_Loc_Glob_For_Write_2D_Real` 시작(152–169). index와 지역/전역 두 차원은 intent(in), 해 배열은 각 두 차원의 real(4)·Target·intent(inout)(171–180). 지역·전역 2D_Real 등록 배열의 index.val을 포인터 연결한다(183–184). `Dim_Array_Written_Out(index) = 2` (185). 루틴 종료(187). |
| 188–224 | 시작 시 26행 모듈 안. 주석과 `Assign_Loc_Glob_For_Write_2D_Real_RK8` 시작(188–205), GLOBAL 사용(206). index·두 지역/전역 차원과 real(rkd)·Target·intent(inout) 해 배열 선언(208–217). 지역·전역 2D_Real_RK8 등록 배열의 index.val을 포인터 연결한다(220–221). `Dim_Array_Written_Out(index) = 200 + rkd` (222). 루틴 종료(224). |
| 225–260 | 시작 시 26행 모듈 안. 주석과 `Assign_Loc_Glob_For_Write_2D_Int` 시작(225–242). index·두 지역/전역 차원과 integer·Target·intent(inout) 해 배열 선언(244–253). 지역·전역 2D_Int 등록 배열의 index.val을 포인터 연결한다(256–257). `Dim_Array_Written_Out(index) = 20` (258). 루틴 종료(260). |
| 261–300 | 시작 시 26행 모듈 안. 주석과 `Assign_Loc_Glob_For_Write_3D_Real` 시작(261–280). index·세 지역/전역 차원과 real(4)·Target·intent(inout) 해 배열 선언(282–293). 지역·전역 3D_Real 등록 배열의 index.val을 포인터 연결한다(296–297). `Dim_Array_Written_Out(index) = 3` (298). 루틴 종료(300). |
| 301–341 | 시작 시 26행 모듈 안. 주석과 `Assign_Loc_Glob_For_Write_3D_Real_RK8` 시작(301–320), GLOBAL 사용(321). index·세 지역/전역 차원과 real(rkd)·Target·intent(inout) 해 배열 선언(323–334). 지역·전역 3D_Real_RK8 등록 배열의 index.val을 포인터 연결한다(337–338). `Dim_Array_Written_Out(index) = 300 + rkd` (339). 루틴 종료(341). |
| 342–383 | 시작 시 26행 모듈 안. 주석과 `Assign_Loc_Glob_For_Write_3D_Int` 시작(342–361). index·세 지역/전역 차원과 integer·Target·intent(inout) 해 배열 선언(363–374). 지역·전역 3D_Int 등록 배열의 index.val을 포인터 연결한다(377–378). `Dim_Array_Written_Out(index) = 30` (379). 루틴·모듈 종료와 빈 줄(381–383). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–21·62–64 및 77–79: 해 배열 설명 주석은 param[in]을 사용한다. 실제 인수 선언은 Target·intent(inout)이다. 나머지 차원·자료형 절차도 같은 선언 형태를 사용한다(110–112·142–144·177–180·214–217·250–253·289–293·330–334·370–374).
- 88·101·189·204·302·319: RK8 절차 앞의 Subroutine 제목 주석은 각각 1D_Real·2D_Real·3D_Real로 적혀 있다. 실제 절차 이름에는 _RK8이 붙는다.
