---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Utilities/Setup_MPI_Topology.f90
lines: 191
sha256: 3342511f0dc3b4f8dbe9f03e91e6f31a2aa21e66a15dbcf10cc87ba4b0339c7a
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Setup_MPI_Topology.f90 — 판독 구간 기록

구간은 1행부터 191행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | EFDC+ 표제·저작권·GPLv2·개발사 안내(1–11). MPI 통신자(communicator)·토폴로지(topology)의 2×2 프로세스 예시·참고 주소·저자·날짜 주석(12–25). Setup_MPI_Topology 입구(27). MPI·GLOBAL·Variables_MPI 사용·implicit none(29–33). 정수 작업 변수·차원 ndim·할당 가능한 index/NearestNeighbor/edges 배열 선언(35–40). 빈 줄 포함. |
| 42–80 | 시작 시 27행 Setup_MPI_Topology 안. WriteBreak와 가상 좌표(virtual coordinates) 예시를 로그에 출력한다(42–51). 설정은 `ndim = 2 ! 2D topology is set` (53), `is_periodic = .FALSE. !< no periodic boundary condition` (54), `reorder     = .FALSE. !< Do not allow MPI to reoreder the location of processes for additional optimizations` (55)이다. dimensions(1/2)에 n_x_partitions/n_y_partitions를 복사한다(58–59). `if( .false. )then` (62)의 참 분기는 MPI_Cart_Create와 MPI_Comm_Rank를 호출한다(65·68). 전처리 `#ifdef GNU` (71)이면 MPI_Cart_Coords에 ierr를 전달한다(72). 전처리 else(73)의 호출에는 ierr 인수가 없다(74). MPI_Cart_Shift로 서·동·남·북 이웃을 구한다(78–79). else가 80행에서 열린다. |
| 81–124 | 시작 시 27행 Setup_MPI_Topology·62행 조건의 80행 else 안. 그래프(graph) 토폴로지에서 nnodes=active_domains(83), `maxsize = n_x_partitions * n_y_partitions       ! *** nnodes` (84)이다. index/NearestNeighbor는 maxsize, edges는 maxsize*4 크기로 할당한다(85–87). index/NearestNeighbor=0, edges=-1, inode/iedge=0 초기화(88–94). j=1..n_y_partitions·i=1..n_x_partitions 루프(95–96)에서 `if( decomp_active(i,j) == 1 )then` (97)이면 `inode = inode + 1` (99). 이웃 조건은 `if( decomp_active(i-1,j) == 1 )then                       ! *** West` (102), `if( decomp_active(i+1,j) == 1 )then                       ! *** East` (107), `if( decomp_active(i,j-1) == 1 )then                       ! *** South` (112), `if( decomp_active(i,j+1) == 1 )then                       ! *** North` (117)이다. 각 참 분기의 증가식은 `NearestNeighbor(inode) = NearestNeighbor(inode) + 1` (103)와 같은 식(108·113·118), `iedge = iedge + 1` (104)와 같은 식(109·114·119)이다. 대응 process_map(i-1,j)/(i+1,j)/(i,j-1)/(i,j+1)을 edges(iedge)에 복사한다(105·110·115·120). 조건·루프 종료(121–124). |
| 125–149 | 시작 시 27행 Setup_MPI_Topology·80행 그래프 else 안. `if(inode /= nnodes )then` (126)이면 경고 후 nnodes=inode(127–128). `if(iedge > 2*nnodes) write(*,*) 'actual nedges = ',iedge,'>',2*nnodes` (130)는 간선(edge) 수 경고이다. index(1)=NearestNeighbor(1)(133) 뒤 2..nnodes 루프에서 `index(i) = index(i-1) + NearestNeighbor(i)` (135)로 누적 간선 수를 만든다(134–136). MPI_Graph_Create는 MPI_Comm_World·nnodes·index·edges·.false.·DSIcomm·ierr를 받는다(139). MPI_Comm_Rank로 새 통신자의 process_id를 얻는다(142). 네 방향 nbr 변수를 -1로 초기화한다(145–148). |
| 150–164 | 시작 시 27행 Setup_MPI_Topology·80행 그래프 else 안. j=1..n_y_partitions·i=1..n_x_partitions 루프(151–152)에서 `if( process_map(i,j) == process_id )then` (153)이면 process_map의 서·동·남·북 위치를 nbr_west/nbr_east/nbr_south/nbr_north에 복사한다(155–158). exit는 내부 i 루프를 벗어난다(159). 조건·루프·62행 if 종료·빈 줄(160–164). |
| 165–191 | 시작 시 27행 Setup_MPI_Topology 안이며 62행 조건 밖. domain_coords(1)=-1(166). j/i 파티션(partition) 루프(167–168)에서 `if( process_id == process_map(i,j) )then` (169)이면 `domain_coords(1) = i-1` (170), `domain_coords(2) = j-1` (171)로 0 기반 좌표를 정하고 내부 루프 exit(172). 외부 j 루프의 종료 조건은 `if( domain_coords(1) /= -1 ) exit` (175)이다. 좌표·분할 수·네 이웃·-1 의미·종료 안내를 출력한다(178–186). WriteInteger 호출 6개와 WriteBreak 호출을 포함한다(179–184·187). MPI_Barrier(DSIcomm,ierr)와 루틴 종료(189–191). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 36: i1과 edge는 선언 이후 이 파일의 실행문에 등장하지 않는다.
- 62–80: 토폴로지 선택 조건은 .false. 상수이다. 카르테시안(Cartesian) 호출 경로는 참 분기에 있고 그래프 호출 경로는 else에 있다.
- 71–75: GNU 분기의 MPI_Cart_Coords 호출은 ierr 인수를 가진다. 전처리 else의 호출은 해당 인수를 생략한다.
- 84–90·130: edges 할당 크기는 maxsize*4이다. 130행의 경고 비교 기준은 2*nnodes이다.
- 151–162: 이웃 연결 검색에서 일치하면 내부 i 루프만 exit한다. 같은 블록의 외부 j 루프에는 별도 exit 조건이 없다.
- 166–176: 좌표 검색 앞에서는 domain_coords(1)만 -1로 설정한다. domain_coords(2)는 일치 조건 안에서만 대입한다.

