---
file: models/ADCIRC/raw/source_code/adcirc/src/gl2loc_mapping.F90
lines: 179
sha256: 5ce27211189fa83d5d89b0b79d325d1fa85eeb412fefabbbbc4f56c07913bc87
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# gl2loc_mapping.F90 — 판독 구간 기록

구간은 1행부터 179행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | ADCIRC 저작권(1994–2025)·LGPL v3 이상·무보증 고지(1–19), 구분 주석(20). |
| 21–57 | `module GL2LOC_MAPPING` 시작(21). 프로세스(process) 0에서 입력을 읽어 각 부분 영역(subdomain)에 분배하며, GOFS의 전 영역 경압 강제력(global baroclinic forcing) NetCDF 자료와 느슨한 단방향 결합(loose one-way coupling)에 처음 사용했다는 목적·Coleman Blakely 11/2022 주석(22–31). SIZES의 MNPROC/MYPROC, MESH의 로컬 절점 수 NP, GLOBAL의 nodes_lg/np_g/COMM 및 mpi_f08의 정수 자료형·브로드캐스트(broadcast)·수집(gather)·가변 길이 수집(MPI_Gatherv)·분배(MPI_Scatterv) 루틴 사용(32–37). implicit none·기본 private(39–41). 전역에서 로컬로의 매핑(mapping) GL2LOC, real(8) 송수신 버퍼(buffer), SENDCOUNTS·DISPLS·RECVCOUNT 선언(43–51). MAPTOLOCAL_REAL·BcastToLocal_Int·BcastToLocal_2DRealArray 공개·contains·빈 줄·주석(53–57). |
| 58–84 | 시작 시 21행 GL2LOC_MAPPING 모듈 안. MAPTOLOCAL_REAL(GLOBALDATA,LOCALDATA) 루틴, MPI_DOUBLE_PRECISION·real(8) 입출력 배열·kk 선언(58–63). 첫 호출에 매핑을 구축한다는 주석과 `BUILD_GL2LOC()` (65–66) 호출, 더미 배열(dummy array) 관련 주석(67–69). `if (MYPROC == 0) then` (71)이면 `do kk = 1, sum(SENDCOUNTS)` (73)에서 SENDBUF_REAL(kk)=GLOBALDATA(GL2LOC(kk)) 복사(74). 루프·분기 종료(75–76). `MPI_SCATTERV`에 SENDBUF_REAL·SENDCOUNTS·DISPLS·MPI_DOUBLE_PRECISION·RECVBUF_REAL·RECVCOUNT·루트 0·COMM을 전달(77–79). LOCALDATA=RECVBUF_REAL 복사(80). 루틴 종료·빈 줄·구분 주석(82–84). |
| 85–115 | 시작 시 21행 GL2LOC_MAPPING 모듈 안. BUILD_GL2LOC 루틴·implicit none(85–86), `logical, save :: first_call = .true.` (88), kk·local_gl2loc 선언(89–90). `if (first_call .eqv. .false.) return` (93) 후 first_call=false(94). `if (MYPROC == 0) then` (96)이면 SENDCOUNTS·DISPLS를 MNPROC 크기로 할당(97–98), `else` (99)이면 각각 크기 1로 할당(100–101). RECVCOUNT=NP(104), RECVBUF_REAL·local_gl2loc을 RECVCOUNT 크기로 할당(106·108). kk=1..RECVCOUNT 루프의 `local_gl2loc(kk) = abs(nodes_lg(kk))` (110). `MPI_GATHER`로 각 RECVCOUNT를 MPI_INTEGER·루트 0·COMM을 사용해 SENDCOUNTS로 수집(113–115). |
| 116–135 | 시작 시 21행 모듈·85행 BUILD_GL2LOC 루틴 안. `if (MYPROC == 0) then` (116)이면 DISPLS(1)=0(117). kk=2..MNPROC 루프의 `DISPLS(kk) = sum(SENDCOUNTS(1:kk - 1))` (119). GL2LOC·SENDBUF_REAL을 sum(SENDCOUNTS) 크기로 할당(122–123). `else` (124)는 SENDBUF_REAL·gl2loc을 크기 1로 할당(125–126). 조건 종료(127). `MPI_GATHERV`로 local_gl2loc·RECVCOUNT를 MPI_INTEGER·GL2LOC·SENDCOUNTS·DISPLS·루트 0·COMM으로 수집(129–131). local_gl2loc 해제·루틴 종료·구분 주석·빈 줄(132–135). |
| 136–146 | 시작 시 21행 GL2LOC_MAPPING 모듈 안. 구분 주석과 BcastToLocal_Int(Val) 루틴·implicit none·정수 intent(inout) 선언(136–140). `MPI_BCast(Val, 1, MPI_Integer, 0, COMM)` (141) 호출. 주석·루틴 종료·빈 줄(142–146). |
| 147–179 | 시작 시 21행 GL2LOC_MAPPING 모듈 안. BcastToLocal_2DRealArray(Val,NX,NY) 루틴·MPI_REAL·implicit none(147–149). Val(:, :)와 TMP(:)는 real(4), NX/NY 입력 및 정수 작업 변수 선언(150–153). `NumVals = NX*NY` (155), TMP(NumVals) 할당(156). `if (MYPROC == 0) then` (157)이면 kk=1(158), `do ii = 1, NX` (159)·`do jj = 1, NY` (160)에서 TMP(kk)=Val(ii,jj) 복사(161), `kk = kk + 1` (162). 루프·분기 종료(163–165). `MPI_BCAST(TMP, NumVals, MPI_REAL, 0, COMM)` (166) 호출. kk=NumVals(167), `do ii = NX, 1, -1` (168)·`do jj = NY, 1, -1` (169)에서 Val(ii,jj)=TMP(kk) 복사(170), `kk = kk - 1` (171). 루프 종료·TMP 해제·루틴 종료·주석·모듈 종료·마지막 주석(172–179). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 34: 가져온 np_g는 이 파일의 실행문에서 참조하지 않는다.
- 88–94·133: BUILD_GL2LOC의 first_call은 save이며 최초 true에서 false로 바뀐다. 이 파일에는 first_call을 다시 true로 설정하거나 NP·nodes_lg·MNPROC 변화 뒤 매핑을 재구축하는 문장이 없다.
- 73–74·109–110: 매핑은 abs(nodes_lg(kk))로 만든다. GLOBALDATA(GL2LOC(kk)) 접근 전에 이 인덱스의 1 이상·GLOBALDATA 크기 이하 여부를 검사하는 문장은 이 루틴에 없다.
- 96–102·116–127: 프로세스 0 이외에서는 SENDCOUNTS·DISPLS·GL2LOC·SENDBUF_REAL을 크기 1로 할당한다. SENDCOUNTS·DISPLS에 로컬 값을 대입하는 문장은 해당 분기에 없다. 이 배열들은 이후 MPI 집합 통신(collective communication)의 인수로 전달된다(113–115·129–131·77–79). MPI 구현 내부는 이 파일 판독 범위에 포함하지 않았다.
- 150–171: BcastToLocal_2DRealArray는 assumed-shape Val에 별도 NX·NY로 접근한다. NX·NY와 Val의 실제 두 차원 크기를 비교하는 문장은 이 루틴에 없다.

