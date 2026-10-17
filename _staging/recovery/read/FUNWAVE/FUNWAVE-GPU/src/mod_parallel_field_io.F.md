---
file: models/FUNWAVE/raw/source_code/FUNWAVE-GPU/src/mod_parallel_field_io.F
lines: 226
sha256: adf351591ca83f95bebb943c05217e5178ab7c00ae5a4918835e2e64bf4b1240
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# mod_parallel_field_io.F — 판독 구간 기록

구간은 1행부터 226행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–52 | 파일명·FUNWAVE-TVD 소속·2016년 저작권·Simplified BSD 재배포 조건·무보증 머리말(1–44). 장(field) 자료를 여러 형식으로 출력하는 모듈이라는 설명과 2017년 이력(45–51). 빈 줄(52). 이 구간은 전처리 조건 밖이다. |
| 53–93 | 전처리 조건 `# if defined (PARALLEL) \|\| defined (MGPU)` (53)으로 PARALLEL 또는 MGPU가 정의될 때만 모듈 전체를 컴파일한다. 두 플래그가 모두 없으면 모듈을 제외하며 `#else`는 없다. `MODULE PARALLEL_FIELD_IO`·`USE GLOBAL`·`CONTAINS` (55–58). `PutFileASCII(FILE,PHI)`는 길이 80 파일명과 `REAL(SP),DIMENSION(Mloc,Nloc),INTENT(IN) :: PHI` (64)를 선언한다(60–64). 순위(rank)·구간 끝점·MPI 상태·지역 배열과 `(MGlob,NGlob)` PHIGLOB 선언, 이전 선언의 주석 처리(66–80). `LOGICAL :: FirstCallPutFile = .TRUE.` (81), SAVE (82). `IF(FirstCallPutFile)THEN` (85)이면 `FirstCallPutFile = .FALSE.` (86)를 대입하고 `FORMAT_LEN`에 Mglob와 `E16.6`을 조합한 출력 형식을 만든다(86–92). SP는 mod_param.F의 정밀도 전처리 분기에 따라 정해진다(해당 파일 58–68). 따라서 PHI를 단정도로 고정할 수 없다. [10-17 전수 검증 정정] [10-17 전수 검증 보완] |
| 94–141 | 시작 시 `# if defined (PARALLEL) \|\| defined (MGPU)` (53)의 참 구간·55행 모듈·60행 PutFileASCII 안이며 `IF(FirstCallPutFile)THEN` (85)이 `ENDIF` (92)로 닫힌 뒤이다. 이전 MPI_Gather는 주석(94–98). 내부 영역 `(Mloc-2*Nghost,Nloc-2*Nghost)`을 할당하고 PHI의 `Ibeg:Iend,Jbeg:Jend`를 복사한다(99–100). nprocs 크기의 끝점 배열을 할당하고 MPI_Gather 4회로 iista·iiend·jjsta·jjend를 순위 0에 모은다(102–111). `if( myid == 0 ) then` (113)이면 자기 영역을 PHIGLOB에 복사한다(114–115). `do irank=1, px*py-1` (117)에서 `if( myid == 0 ) then` (119)이면 `lenx = iiends(irank+1) - iistas(irank+1) + 1` (120), `leny = jjends(irank+1) - jjstas(irank+1) + 1` (121), `lenxy = lenx*leny` (122)를 계산한다. xx를 할당하고 mpi_irecv·mpi_wait로 수신한 뒤 전역 위치에 복사하고 xx를 해제한다(123–129). 같은 분기의 `elseif( myid == irank ) then` (131)이면 `lenxy = ( iiend-iista+1 )*( jjend-jjsta+1 )` (133)을 계산하고 mpi_isend·mpi_wait로 LocalPHI를 순위 0에 보낸다(134–137). 순위 루프 종료와 지역 배열 해제(139–141). 복사식은 `LocalPHI=PHI(Ibeg:Iend,Jbeg:Jend)` (100)이다. 순위 0의 복사식은 `PHIGLOB( iista:iiend, jjsta:jjend ) = LocalPHI` (114)이다. 수신 후 복사식은 `PHIGLOB( iistas(irank+1):iiends(irank+1), jjstas(irank+1):jjends(irank+1) ) = xx` (128)이다. 119–137행 분기 사슬에는 ELSE가 없다. 바깥 전처리는 `# endif` (225)로 닫힌다. [10-17 전수 검증 보완] |
| 142–160 | 시작 시 `# if defined (PARALLEL) \|\| defined (MGPU)` (53)의 참 구간·55행 모듈·60행 PutFileASCII 안이며 순위 루프 밖이다. `if (myid.eq.0) then` (143)이면 장치 1로 파일을 연다(144). `DO J=1,NGlob,OUTPUT_RES` (145)와 `WRITE(1,FORMAT_LEN)(real(PHIGLOB(I,J)),I=1,MGlob,OUTPUT_RES)` (146)로 두 방향 모두 OUTPUT_RES 간격의 ASCII(American Standard Code for Information Interchange) 자료를 출력한다. 이전 유령 격자점(ghost point) 포함 출력과 고정 형식은 주석(148–152). CLOSE·조건 종료·루틴 종료(153–157). 다음 이진 출력의 William D. Gropp 강의 유래 주석(159–160). 주석 처리된 인덱스 범위는 `!DO J=Nghost+1,NGlob+NGhost,OUTPUT_RES` (148)과 `!   WRITE(1,FORMAT_LEN)(real(PHIGLOB(I,J)),I=Nghost+1,MGlob+Nghost,OUTPUT_RES)` (149)이다. 바깥 전처리는 `# endif` (225)로 닫힌다. [10-17 전수 검증 보완] |
| 161–198 | 시작 시 `# if defined (PARALLEL) \|\| defined (MGPU)` (53)의 참 구간·55행 모듈 안이다. `PutFileBinary(FILE_NAME,PHI)` 입구, 길이 80 파일명·REAL(SP)형 PHI·PHITEST·MPI 자료형 핸들·`INTEGER(8) :: offset` (169)·ndims 크기 영역 배열 선언(161–171). `offset = 0` (173). 지역 크기는 Mloc·Nloc(178–179), 내부 크기는 `subsizes_loc(1) =  sizes_loc(1) - 2*Nghost` (181), `subsizes_loc(2) =  sizes_loc(2) - 2*Nghost` (182)이다. 지역 시작 인덱스는 두 방향 모두 Nghost이며 0 기준이라는 주석이 있다(184–185). 전역 크기는 Mglob·Nglob(189–190), 전역 내부 크기는 지역 내부 크기의 복사(192–193). `start_index_glob(1) = iista - 1 ! 0 start index even in Fortran` (195), `start_index_glob(2) = jjsta - 1 ! 0 start index even in Fortran` (196)로 전역 시작 인덱스를 정한다. `sizes_loc(1) = Mloc` (178)과 `sizes_loc(2) = Nloc` (179)를 대입한다. `start_index_loc(1) = Nghost  ! 0 start index even in Fortran` (184)과 `start_index_loc(2) = Nghost  ! 0 start index even in Fortran` (185)을 대입한다. `sizes_glob(1) = Mglob` (189)과 `sizes_glob(2) = Nglob` (190)를 대입한다. `subsizes_glob(1) =   subsizes_loc(1)` (192)과 `subsizes_glob(2) =   subsizes_loc(2)` (193)를 대입한다. REAL(SP)의 정밀도는 mod_param.F 58–68행에서 선택한다. 바깥 전처리는 `# endif` (225)로 닫힌다. [10-17 전수 검증 정정] [10-17 전수 검증 보완] |
| 199–226 | 시작 시 `# if defined (PARALLEL) \|\| defined (MGPU)` (53)의 참 구간·55행 모듈·161행 PutFileBinary 안이다. MPI_TYPE_CREATE_SUBARRAY·MPI_TYPE_COMMIT을 지역 메모리와 전역 파일 배치에 각각 호출하며 MPI_ORDER_FORTRAN·mpi_sp를 쓴다(199–206). `CALL MPI_FILE_OPEN(MPI_COMM_WORLD, FILE_NAME , &` (209); `MPI_MODE_WRONLY + MPI_MODE_CREATE, &` (210); `MPI_INFO_NULL, file_handler , ierr)` (211)로 파일을 연다. MPI_FILE_SET_VIEW는 offset=0·native 표현·전역 자료형을 사용한다(213). MPI_FILE_WRITE_ALL은 PHI에서 지역 자료형 1개를 집합적으로 기록하고 MPI_FILE_CLOSE를 호출한다(216–218). 루틴·모듈 종료(221–223). `# endif` (225)로 53행 전처리를 닫고 종료 주석(226). [10-17 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 102·117: 끝점 배열의 크기는 nprocs이다. 수신 순위 루프의 상한은 px*py-1이다.
- 145–146·199–216: ASCII 출력은 OUTPUT_RES 간격을 사용한다. 이진 출력의 부분 배열 설정과 쓰기에는 OUTPUT_RES가 등장하지 않는다.
- 166: PHITEST는 선언 뒤 이 파일에서 사용되지 않는다.
- 199–221: 메모리·파일 MPI 자료형을 생성하고 commit한다. 이 루틴에는 MPI_TYPE_FREE 호출이 없다.
- 104–135·199–218: MPI 호출은 ier 또는 ierr를 받는다. 이 파일에는 반환 코드에 따른 조건 분기가 없다.
