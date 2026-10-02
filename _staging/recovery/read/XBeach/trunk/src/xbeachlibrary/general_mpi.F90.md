---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/general_mpi.F90
lines: 611
sha256: 5012b441a56ebeb2a0275201ccc480587ae4f68d2dbbc4285ddab1957481483e
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# general_mpi.F90 — 판독 구간 기록

구간은 1행부터 611행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–44 | `general_mpi_module`은 implicit none·save(1–3), 타이머 define은 주석(5–6). USEMPI 아래 구현·interface(8). 경계 제외 내부 b를 master에 보내되 물리 경계는 포함한다는 주석(11–21). matrix_distr·matrix_coll은 real8/정수, shift_borders는 real8, vector_distr는 벡터/블록 벡터 절차로 연결(25–42), contains(44). |
| 45–77 | `vector_distr_real8`: 프로세스 P가 `a(is(P):is(P)+lm(P)-1)`을 받는다는 설명(48–55). 비연속 인자와 MPI_Alltoallw 호출 시 배열 연속화에 관한 주석(59–61), root=0 요구(63). a 입력·b 출력·is/lm·root/comm과 MPI 통신 배열·1차원 부분배열 크기 선언(65–76). |
| 78–109 | basic_type=DOUBLE_PRECISION, `MPI_Comm_size/rank` 호출(78–80). root≠0이면 오류 출력·`MPI_Abort(MPI_COMM_WORLD,1,ier)`(82–85). sz 크기의 송수신 타입·개수·변위 배열 할당(87–92), 변위·개수=0, 타입=MPI_CHARACTER(94–99). MPI 부분배열 API 설명 주석(105–108). |
| 110–149 | 수신: sizes=shape(b)·subsizes=lm(ra+1)·starts=0, `MPI_Type_create_subarray`·commit으로 recvtypes(1) 생성, recvcounts(1)=1(112–118). root는 각 목적지에 sizes=shape(a)·subsizes=lm(i)·starts=is(i)−1, 전체 sendcounts=1 및 타입 생성·commit(122–134). `MPI_Alltoallw`(136–137), MPI_CHARACTER가 아닌 송수신 타입만 `MPI_Type_free`(139–146), 루틴 끝(148). |
| 150–183 | `block_vector_distr_real8`: P가 `a(is(P):is(P)+lm(P)-1,:)`를 받는다는 설명(154–163), 비연속 배열·root=0 주석(165–169). a/b는 2D real8, 위치·길이 배열·root/comm, MPI 타입/개수/변위 배열 및 2D sizes/subsizes/starts 선언(171–182). |
| 184–218 | DOUBLE_PRECISION·communicator 크기/rank 확인(184–186), root≠0은 WORLD abort(188–191). 통신 배열 할당(193–198), 변위·개수=0, 타입=CHARACTER(200–205). 부분배열 API·root로부터만 수신한다는 주석(211–218). |
| 219–257 | 블록 수신 타입: shape(b), subsizes=(lm(ra+1),size(b,2)), starts=0, Fortran 순서 부분배열·commit 및 count=1(219–225). root의 목적지별 타입은 shape(a), (lm(i),size(a,2)), (is(i)−1,0), 전체 sendcounts=1(228–239). Alltoallw(242–243), 생성된 송수신 타입 해제(245–252), 루틴 끝(254). |
| 258–300 | `matrix_distr_real8`: root는 자신에게 송신/복사하지 않고 root=0이며 root에는 b가 없다는 설명(261–276). b(1,1)이 a(is(p),js(p))와 대응하며 b의 lm×ln을 채운다는 주석(267–271). 2D real8 a/b·인덱스/크기·통신 변수 선언(279–291), basic_type=DOUBLE_PRECISION(293), 구현은 `genmpi_distr.inc` 포함(295), 루틴 끝(297). include 내부는 이 판독 대상에 포함하지 않았다. |
| 301–343 | `matrix_distr_integer`: 실수형과 같은 분배 계약 주석(304–319). a/b는 2D 정수(324–325), 위치·크기·통신 인자 및 작업 배열 선언(326–334). basic_type=MPI_INTEGER(336), `genmpi_distr.inc` 포함(338), 루틴 끝(340). |
| 344–395 | `matrix_coll_real8`: 비root들로부터 root에 수집, 출력 a는 호출자가 준비하고 이 루틴에서 할당하지 않는다는 주석(346–352). b(1,1)과 a(is(rank+1),js(rank+1))의 대응·lm/ln·물리경계 flag·root=0 설명(353–367). a 출력·b 입력·경계 배열 선언(371–376). `nbord=2`, `nover=2*nbord`(386–387); basic_type=DOUBLE_PRECISION, `genmpi_coll.inc` 포함(389–391), 루틴 끝(393). include 내부 동작은 읽지 않았다. |
| 396–427 | `matrix_coll_integer`: 설명은 실수형 참조(398). 정수 a 출력·b 입력, 위치·크기·경계 flag·root/comm 선언(401–406), MPI 작업 배열(408–412). `nbord=2`·`nover=2*nbord`, MPI_INTEGER(416–419), `genmpi_coll.inc` 포함(421), 루틴 끝(423). |
| 428–453 | `decomp`: MPICH의 MPE_Decomp1d에서 왔다는 주석(430). 정수 1..n을 numprocs 구간에 가능한 균등하게 나누는 목적(432–441), communicator 크기·rank 취득 후 시작 s와 끝 e를 반복 범위로 쓰는 예제 주석(443–452). |
| 454–472 | decomp 입력 n·numprocs·myid, 출력 s/e(454–455). 정수 `nlocal=n/numprocs`, `s=myid*nlocal+1`, `deficit=mod(n,numprocs)`, `s+=min(myid,deficit)`(459–462). myid<deficit이면 nlocal+1(463–465), `e=s+nlocal-1`; e>n 또는 마지막 rank이면 e=n(466–469). |
| 473–520 | `det_submatrices`: ma×na 행렬을 mp×np 프로세스에 나누는 인자·출력 위치/크기 설명(475–487), 첫/마지막 열·행과 맞닿는 flag 설명(488–499). 부분행렬 겹침의 도식·겹침 4·예시 부분행렬 차수 9,13,11·전체 차수25 주석(501–519). |
| 521–548 | 행렬/프로세스 크기 입력·위치/길이/경계 배열 출력 선언(522–526), `nover=4`(527), flag 전체 false(529–532). i=1..mp마다 `decomp(ma-nover,mp,i-1,s,e)`(534–535). j=1..np의 인덱스 i+k에서 j=1/np이면 left/right=true, is=s·lm=e−s+nover+1, k는 mp씩 증가(537–546). |
| 549–566 | j=1..np마다 `decomp(na-nover,np,j-1,s,e)`(550–551). i=1/mp일 때 top/bot=true(553–558), `js(i+k)=s`, `ln(i+k)=e-s+nover+1`(559–560); 각 j 뒤 k+=mp(562). 루틴 끝(565). |
| 567–594 | `shift_borders_matrix_real8`: a inout·left/right/top/bot/comm 입력(567–574), datatype=DOUBLE_PRECISION, ma/na=ubound(a,1/2)(576–580). MPI_Sendrecv 태그1로 `a(2:ma-1,2)`를 left에 보내고 right에서 `a(2:ma-1,na)` 수신(583–587). 태그2는 `a(2:ma-1,na-1)`를 right에 보내고 left에서 열1 수신(589–593). 각 count=ma−2, 상태는 MPI_STATUS_IGNORE. |
| 595–611 | MPI_Sendrecv 태그3으로 `a(ma-1,:)`를 bot에 보내고 top에서 `a(1,:)` 수신(596–600); 태그4로 `a(2,:)`를 top에 보내고 bot에서 `a(ma,:)` 수신(602–606). 각 count=na·전체 열 포함·MPI_STATUS_IGNORE. 루틴 끝, USEMPI endif·모듈 끝(608–611). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 82–85·188–191: 두 벡터 분배 루틴은 root=0을 강제하며, 다른 communicator를 인자로 받아도 이 오류 경로의 abort에는 MPI_COMM_WORLD를 사용한다.
- 129·235: 목적지별 타입 생성 루프에서 `sendcounts(i)=1`이 아니라 전체 배열 `sendcounts=1`을 반복 대입한다.
- 11–18·386–387·416–417·527: 모듈 머리 주석은 한 겹 경계와 내부 `b(2:mb-1,2:nb-1)`을 설명하지만 수집 선언은 nbord=2·nover=4, 부분행렬 분할은 nover=4를 사용한다. include 내부는 읽지 않아 수집 범위는 확인하지 않았다.
- 491–499: 마지막 열 설명의 표기는 `a(ma,:)`(493), 마지막 행 설명의 표기는 `a(na,:)`(499)이다. 같은 루틴 입력 설명은 ma를 첫 차원·na를 둘째 차원으로 적는다(476–477).
- 459·535·551: decomp는 n/numprocs를 직접 계산하고, 분할 호출은 ma−4·na−4를 전달한다. 이 파일의 해당 루틴 안에는 numprocs의 양수 여부나 최소 행렬 크기를 검사하는 분기가 없다.
- 79–80·115–117·136–144·583–606: MPI 상태를 ier/ierror로 받지만 이 호출들 뒤에 오류값에 따라 분기하는 실행문은 없다.
