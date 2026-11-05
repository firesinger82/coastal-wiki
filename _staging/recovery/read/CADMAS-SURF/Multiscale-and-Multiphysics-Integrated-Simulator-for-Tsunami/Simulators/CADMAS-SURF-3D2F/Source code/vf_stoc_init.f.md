---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_stoc_init.f
lines: 90
sha256: d8382b62e898ed20b94e817a144adb1e6f9d69059653a65f7034c46f3270bf0b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_stoc_init.f — 판독 구간 기록

구간은 1행부터 90행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | STOC와의 통신 환경을 초기화한다. mod_comm의 지정 변수, mpif.h, VF_ASTOCI.h, VF_ASTOCR.h를 사용한다. MPI 상태 배열과 크기 512인 IWORK를 선언한다.<br>원문: `      SUBROUTINE VF_STOC_INIT(IERR)` (1); 주석: `CD=== 概要 ===========================================================` (3) (개요); 주석: `CDT   VF_STOC_INIT:STOCとの通信環境を初期化する` (5) (STOC와의 통신 환경을 초기화한다); 주석: `C==== 宣言 ===========================================================` (7) (선언); 주석: `C     -- 大域型 --` (9) (대역형); `      use mod_comm,only: nrank_all,comm_work_ic_mg,comm_ic_mg,my_model,` (10) / `     $                   l_cadmas_2fc` (11) (하나의 고정형식 연속문, 10–11행); `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (12); 주석: `C     -- 大域変数 --` (14) (대역변수); `      INCLUDE  'mpif.h'` (15); `      include 'VF_ASTOCI.h'` (16); `      include 'VF_ASTOCR.h'` (17); 주석: `C ... WORK VARIABLES` (18); `      INTEGER IERR,M,N,IRANK,ISIZE,ISTAT(MPI_STATUS_SIZE),IREQ,ITAG` (19); `      INTEGER IB_STOC0,ITMP,IWORK0,IWORK(512)` (20); 주석: `CD    -- 引数 --` (22) (인수); 주석: `CD    IERR : OUT : I*4 : 完了コード` (23) (완료 코드); 주석: `C==== 実行 ===========================================================` (25) (실행). |
| 27–43 | 시작 시 1행 루틴 안. IB_STOC=-1, NB_CADMAS=0, LB_CADMAS=0으로 설정하고 모든 IB_CADMAS를 -1로 채운다. my_model이 l_cadmas_2fc이면 NB_SC=0으로 설정하고 즉시 반환한다.<br>원문: 주석: `C     << STOC<-->CADMAS 通信用変数の設定 >>` (27) (STOC와 CADMAS 통신용 변수 설정); 주석: `C     IB_STOC, NB_CADMAS, IB_CADMASの3種を設定する` (28) (IB_STOC, NB_CADMAS, IB_CADMAS 세 종류를 설정한다); 주석: `C ... 初期化` (30) (초기화); `      IB_STOC = -1` (31); `      NB_CADMAS = 0` (32); `      LB_CADMAS = 0` (33); `      DO N=1,MAX_CADMAS` (34); `         IB_CADMAS(N) = -1` (35); `      ENDDO` (36); `      IWORK0 = -1` (37); `      if( my_model.eq.l_cadmas_2fc ) then` (39); `         NB_SC=0` (40); `         return` (41); `      endif` (42). |
| 44–62 | 시작 시 1행 루틴 안. MPI_COMM_SPLIT로 같은 NB_SC의 통신 그룹을 만든다. NB_SC=0이면 반환한다. 나머지는 MPI_COMM_SIZE/RANK로 그룹 크기와 순위(rank)를 얻고 NB_CADMAS=ITMP-1을 설정한다. IB_STOC0=-1을 MPI_MAX로 모두축약(all-reduce)하여 IB_STOC를 얻는다.<br>원문: 주석: `C ... 同じNB_SC値をもつSTOC <--> CADMAS通信のグループを一時的に作成` (44) (같은 NB_SC 값을 갖는 STOC와 CADMAS 통신 그룹을 임시로 만든다); `      CALL MPI_COMM_SPLIT(comm_work_ic_mg,NB_SC,NRANK_ALL,comm_ic_mg,` (45) / `     $                    IERR)` (46) (하나의 고정형식 연속문, 45–46행); 주석: `C ... STOC-CADMAS連成に関らないPEはRETURN` (48) (STOC-CADMAS 결합에 관여하지 않는 처리 요소(processing element)는 반환한다); `      IF( NB_SC.EQ.0 ) RETURN` (49); 주석: `C     <<< NB_CADMASの設定 >>>` (52) (NB_CADMAS 설정); `      CALL MPI_COMM_SIZE(comm_ic_mg,ITMP,IERR)` (53); `      CALL MPI_COMM_RANK(comm_ic_mg,IRANK,IERR)` (54); `      NB_CADMAS = ITMP-1` (55); 주석: `C     <<< IB_STOCの設定 >>>` (58) (IB_STOC 설정); `      IB_STOC0 = -1` (59); `      CALL MPI_ALLREDUCE(IB_STOC0,IB_STOC,1,MPI_INTEGER,MPI_MAX,` (60) / `     $                   comm_ic_mg,IERR)` (61) (하나의 고정형식 연속문, 60–61행). |
| 63–90 | 시작 시 1행 루틴 안. IRANK를 MPI_ALLGATHER로 모은다. NB_CADMAS+1개 값 중 0 이상인 순위를 IB_CADMAS에 채우고 자기 위치를 LB_CADMAS로 기록한다. 디버그 출력은 주석이며 정상 반환한다.<br>원문: 주석: `C     <<< IB_CADMASの設定 >>>` (64) (IB_CADMAS 설정); `      IWORK0 = IRANK` (65); `      CALL MPI_ALLGATHER(IWORK0,1,MPI_INTEGER,` (66) / `     $                   IWORK,1,MPI_INTEGER,comm_ic_mg,IERR)` (67) (하나의 고정형식 연속문, 66–67행); `      M = 0` (69); `      DO N=1,NB_CADMAS+1` (70); `         IF( IWORK(N).GE.0 ) THEN` (71); `            M = M + 1` (72); `            IB_CADMAS(M) = IWORK(N)` (73); `            IF( IRANK.EQ.IWORK(N) ) LB_CADMAS = M` (74); `         ENDIF` (75); `      ENDDO` (76); 주석: `CDEBUG      write(*,*) 'ib_stoc=0=',ib_stoc` (77); 주석: `CDEBUG      write(*,*) 'nb_cadmas=1=',nb_cadmas` (78); 주석: `CDEBUG      write(*,*) 'lb_cadmas=1=',lb_cadmas` (79); 주석: `CDEBUG      write(*,*) 'ib_cadmas=1=',ib_cadmas(1:nb_cadmas)` (80); 주석: `CDEBUG      write(*,*) 'nb_sc=1=',nb_sc` (81); 주석: `C     -- 実行文の終了 --` (83) (실행문 종료); `      GOTO 9999` (84); 주석: `C==== 終了 ===========================================================` (86) (종료); ` 9999 CONTINUE` (88); `      RETURN` (89); `      END` (90). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–20·66–70: IWORK 크기는 512로 고정되어 있다. MPI_ALLGATHER와 후속 루프 앞에는 통신자 크기가 512 이하인지 검사하는 문장이 없다.
- 39–41: CADMAS 2FC 조기 반환 분기에는 출력 인수 IERR에 값을 대입하는 실행문이 없다.
- 59–61: 이 루틴이 MPI_ALLREDUCE에 제공하는 IB_STOC0 값은 -1이다. 다른 참여 프로세스의 제공값은 판독 범위 밖이다.
