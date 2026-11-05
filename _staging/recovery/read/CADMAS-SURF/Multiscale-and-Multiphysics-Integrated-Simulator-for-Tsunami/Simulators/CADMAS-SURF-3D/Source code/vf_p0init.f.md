---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p0init.f
lines: 83
sha256: dc82ac5e2b8d923163c7c81c5f79da71b66953b790087660b1055573e44fd805
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_p0init.f — 판독 구간 기록

구간은 1행부터 83행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 병렬 환경 초기화 루틴의 암시적 형식과 병렬 정수·실수 정보 포함 파일을 선언한다. 원문: `      SUBROUTINE VF_P0INIT()` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_P0INIT:並列環境を初期化する` (5) (병렬 환경을 초기화한다). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형식). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C     -- 大域変数 --` (12) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (13). `      INCLUDE 'VF_APARAI.h'` (14). `      INCLUDE 'VF_APARAR.h'` (15). `C==== 実行 ===========================================================` (17) (실행). |
| 19–60 | 시작 시 1행 루틴 `SUBROUTINE VF_P0INIT` 안. MG 관련 스칼라와 프로세스·분할·소유 범위·버퍼 정보를 0으로 설정한다. MGNAME은 공백으로 채운다. 정수 배열은 VF_ZSETI1에 배열별 원소 수를 전달하여 0으로 설정한다. 원문: `C     -- VF_APARAI.hを初期化する --` (19) (VF_APARAI.h를 초기화한다). `      MGPROC=0` (20). `      MGRANK=0` (21). `      MGCOMM=0` (22). `      MGARAN=0` (23). `      DO 100 I=1,MAXPRO` (24). `        MGNAME(I)=' '` (25). ` 100  CONTINUE` (26). `      CALL VF_ZSETI1(MGNLEN,0,MAXPRO)` (27). `      CALL VF_ZSETI1(MGNPIN,0,MAXPRO)` (28). `      CALL VF_ZSETI1(MGPARE,0,MAXPRO)` (29). `      CALL VF_ZSETI1(MGAREA,0,MAXPRO)` (30). `      MGPRNK=0` (31). `      CALL VF_ZSETI1(MGPINF,0,9)` (32). `      MGCNUM=0` (33). `      CALL VF_ZSETI1(MGCRNK,0,  MAXPRO)` (34). `      CALL VF_ZSETI1(MGCINF,0,9*MAXPRO)` (35). `      CALL VF_ZSETI1(MGCPOS,0,6*MAXPRO)` (36). `      NPROCS=0` (37). `      NUMNPI=0` (38). `      NUMNPJ=0` (39). `      MYRANK=0` (40). `      MYRI  =0` (41). `      MYRJ  =0` (42). `      NUMI0 =0` (43). `      NUMJ0 =0` (44). `      MYIS  =0` (45). `      MYIE  =0` (46). `      MYJS  =0` (47). `      MYJE  =0` (48). `      MYMIS =0` (49). `      MYMIE =0` (50). `      MYMJS =0` (51). `      MYMJE =0` (52). `      MYGIS =0` (53). `      MYGIE =0` (54). `      MYGJS =0` (55). `      MYGJE =0` (56). `      NUMBUF=0` (57). `      CALL VF_ZSETI1(IPROCS,0,MAXNPI+1)` (58). `      CALL VF_ZSETI1(JPROCS,0,MAXNPJ+1)` (59). |
| 61–83 | 시작 시 1행 루틴 `SUBROUTINE VF_P0INIT` 안. 전역 x,y 영역 끝점을 0으로 초기화한다. VF_ZXMG_INIT로 환경을 초기화하고 VF_ZXMG_CSIZE 및 VF_ZXMG_CRANK로 MGPROC와 MGRANK를 얻은 뒤 반환한다. 원문: `C     -- VF_APARAR.hを初期化する --` (61) (VF_APARAR.h를 초기화한다). `      GLXMIN=0.0D0` (62). `      GLXMAX=0.0D0` (63). `      GLYMIN=0.0D0` (64). `      GLYMAX=0.0D0` (65). `C     -- 初期化する --` (67) (초기화한다). `      CALL VF_ZXMG_INIT(IERR)` (68). `C     -- プロセス数を得る --` (70) (프로세스 수를 구한다). `      CALL VF_ZXMG_CSIZE(MGPROC,IERR)` (71). `C     -- 自分のランクを得る --` (73) (자기 랭크를 구한다). `      CALL VF_ZXMG_CRANK(MGRANK,IERR)` (74). `C     -- 実行文の終了 --` (76) (실행문 종료). `      GOTO 9999` (77). `C==== 終了 ===========================================================` (79) (종료). ` 9999 CONTINUE` (81). `      RETURN` (82). `      END` (83). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20–59·68–74: MGPROC와 NPROCS는 모두 0으로 초기화한다. 이후 크기 질의 결과는 MGPROC에 받는다. 이 파일에서 NPROCS를 다시 설정하는 문장은 없다.
