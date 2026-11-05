---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_p0init.f
lines: 97
sha256: 18617d4b08dd0017cbace6488da5d1ae8ed92f2959d906506cb451d0aa34cf6d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_p0init.f — 판독 구간 기록

구간은 1행부터 97행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | 병렬 환경을 초기화하는 VF_P0INIT의 개요·대역형·대역변수 선언이다(5–18). mod_comm·mod_dem을 사용한다(9–10). 원문: `      SUBROUTINE VF_P0INIT()` (1) / `CD=== 概要 ===========================================================` (개요) (3) / `CDT   VF_P0INIT:並列環境を初期化する` (병렬 환경 초기화) (5) / `C==== 宣言 ===========================================================` (선언) (7) / `      use mod_comm` (9) / `      use mod_dem` (10) / `C     -- 大域型 --` (대역형) (12) / `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (13) / `C     -- 大域変数 --` (대역변수) (15) / `      INCLUDE 'VF_A0PRM.h'` (16) / `      INCLUDE 'VF_APARAI.h'` (17) / `      INCLUDE 'VF_APARAR.h'` (18) / `C==== 実行 ===========================================================` (실행) (20) |
| 22–65 | 시작 시 1행 루틴 안. VF_APARAI.h 초기화 주석 아래 MGPROC·MGRANK·MGCOMM·MGARAN을 비롯한 인용된 정수 변수에 0을 대입한다(22–64). MGNAME은 MAXPRO 범위에서 공백으로 설정하고 정수 배열은 VF_ZSETI1으로 초기화한다. 원문: `C     -- VF_APARAI.hを初期化する --` (VF_APARAI.h 초기화) (22) / `      MGPROC=0` (23) / `      MGRANK=0` (24) / `      MGCOMM=0` (25) / `      MGARAN=0` (26) / `      DO 100 I=1,MAXPRO` (27) / `        MGNAME(I)=' '` (28) / ` 100  CONTINUE` (29) / `      CALL VF_ZSETI1(MGNLEN,0,MAXPRO)` (30) / `      CALL VF_ZSETI1(MGNPIN,0,MAXPRO)` (31) / `      CALL VF_ZSETI1(MGPARE,0,MAXPRO)` (32) / `      CALL VF_ZSETI1(MGAREA,0,MAXPRO)` (33) / `      MGPRNK=0` (34) / `      CALL VF_ZSETI1(MGPINF,0,9)` (35) / `      MGCNUM=0` (36) / `      CALL VF_ZSETI1(MGCRNK,0,  MAXPRO)` (37) / `      CALL VF_ZSETI1(MGCINF,0,9*MAXPRO)` (38) / `      CALL VF_ZSETI1(MGCPOS,0,6*MAXPRO)` (39) / `      NPROCS=0` (40) / `      NUMNPI=0` (41) / `      NUMNPJ=0` (42) / `      MYRANK=0` (43) / `      MYRI  =0` (44) / `      MYRJ  =0` (45) / `      NUMI0 =0` (46) / `      NUMJ0 =0` (47) / `      MYIS  =0` (48) / `      MYIE  =0` (49) / `      MYJS  =0` (50) / `      MYJE  =0` (51) / `      MYMIS =0` (52) / `      MYMIE =0` (53) / `      MYMJS =0` (54) / `      MYMJE =0` (55) / `      MYGIS =0` (56) / `      MYGIE =0` (57) / `      MYGJS =0` (58) / `      MYGJE =0` (59) / `      NUMBUF=0` (60) / `      CALL VF_ZSETI1(IPROCS,0,MAXNPI+1)` (61) / `      CALL VF_ZSETI1(JPROCS,0,MAXNPJ+1)` (62) / `      MYHOST=0` (64) [11-04 전수 검증 정정] |
| 66–97 | 시작 시 1행 루틴 안. VF_APARAR.h 초기화로 GLXMIN·GLXMAX·GLYMIN·GLYMAX에 0.0D0을 대입한다(66–70). VF_ZXMG_INIT으로 초기화하고 VF_ZXMG_CSIZE·VF_ZXMG_CRANK로 프로세스 수·자기 순위를 얻는다(72–79). VF_AHIDEMI.h 초기화 주석 아래 NPRWLD=1·MYRWLD=0을 둔다(81–83). 전체 위치를 얻는 주석 아래 통신자(communicator)를 복사하고 MPI_COMM_SIZE·MPI_COMM_RANK를 호출한다(85–88). 실행문 종료·종료부다(90–97). 원문: `C     -- VF_APARAR.hを初期化する --` (VF_APARAR.h 초기화) (66) / `      GLXMIN=0.0D0` (67) / `      GLXMAX=0.0D0` (68) / `      GLYMIN=0.0D0` (69) / `      GLYMAX=0.0D0` (70) / `C     -- 初期化する --` (초기화함) (72) / `      CALL VF_ZXMG_INIT(IERR)` (73) / `C     -- プロセス数を得る --` (프로세스 수 취득) (75) / `      CALL VF_ZXMG_CSIZE(MGPROC,IERR)` (76) / `C     -- 自分のランクを得る --` (자신의 순위(rank) 취득) (78) / `      CALL VF_ZXMG_CRANK(MGRANK,IERR)` (79) / `C     -- VF_AHIDEMI.hを初期化する --` (VF_AHIDEMI.h 초기화) (81) / `      NPRWLD=1` (82) / `      MYRWLD=0` (83) / `C     -- 全体の位置付けを得る --` (전체 통신자 내 위치 취득) (85) / `      comm_2fc_dem=comm_work_2fc_dem` (86) / `      CALL MPI_COMM_SIZE(comm_2fc_dem,NPRWLD,IERR)` (87) / `      CALL MPI_COMM_RANK(comm_2fc_dem,MYRWLD,IERR)` (88) / `C     -- 実行文の終了 --` (실행문 종료) (90) / `      GOTO 9999` (91) / `C==== 終了 ===========================================================` (종료) (93) / ` 9999 CONTINUE` (95) / `      RETURN` (96) / `      END` (97) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 87–88: MPI_COMM_SIZE·MPI_COMM_RANK를 직접 호출한다. 이 파일에는 mpif.h INCLUDE가 없다.
- 81: 초기화 주석은 VF_AHIDEMI.h를 언급한다. 이 파일의 INCLUDE 목록에는 그 헤더가 없다.
