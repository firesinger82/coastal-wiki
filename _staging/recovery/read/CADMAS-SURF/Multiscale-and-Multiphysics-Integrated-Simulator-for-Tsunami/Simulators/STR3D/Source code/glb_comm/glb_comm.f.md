---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/glb_comm.f
lines: 68
sha256: c9714e048b1fa8addab9fe64700359e5f36cbb8cfcd853c1004fc3aed127fc75
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# glb_comm.f — 판독 구간 기록

구간은 1행부터 68행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | M_VAL·암시적 배정밀도·파일명과 KK·RR·IFL 배열을 선언한다(1–9). 원문: `      SUBROUTINE GLB_COMM(KK,RR,IFL,FLNAME,NLEN,ICHK)` (1); `      USE M_VAL` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      CHARACTER*256 FLNAME` (7); `      DIMENSION KK(*),RR(*),IFL(*)` (9). |
| 11–33 | 시작 시 1행 glb_comm 루틴 안. 무한 DO 루프에서 프로세스 1의 작업 번호 IOP를 수신한다(11–13). SELECT CASE의 0은 반환, 1·2는 KK·RR 수신, 3·4는 RESFRC0·NPFLOW0, 5는 FEMAP_OUT0, 6·7은 ENS_GEOM0·ENS_CASE_T, 8은 OUTPUT0을 호출한다(15–33). 원문: `      DO` (11); `        CALL M_MPI_RECV_I(IOP,1,1)` (13); `        SELECT CASE( IOP )` (15); `        CASE( 0 ) ` (16); `          RETURN` (17); `        CASE( 1 ) ` (18); `          CALL RECV_KK(KK)` (19); `        CASE( 2 ) ` (20); `          CALL RECV_RR(RR)` (21); `        CASE( 3 ) ` (22); `          CALL RESFRC0(RR,IFL(11))` (23); `        CASE( 4 ) ` (24); `          CALL NPFLOW0(IFL(11))` (25); `        CASE( 5 )` (26); `          CALL FEMAP_OUT0(KK,INDG,IFL(15))` (27); `        CASE( 6 )` (28); `          CALL ENS_GEOM0(KK,IFL(20),FLNAME,NLEN,ICHK)` (29); `        CASE( 7 )` (30); `          CALL ENS_CASE_T(KK,IFL(20),FLNAME,NLEN,ICHK)` (31); `        CASE( 8 )` (32); `          CALL OUTPUT0(KK,IFL,FLNAME,NLEN,ICHK)` (33). |
| 34–57 | 시작 시 1행 glb_comm 루틴 안. 시작 시 11행 `DO` 안이며 이 루프는 66행 `ENDDO`에서 닫힌다. 시작 시 15행 `SELECT CASE( IOP )` 안이며 이 블록은 64행 `END SELECT`에서 닫힌다. 작업 10은 RDPRESS0, 11·12는 RECV_SURF0·RECV_PRES0, 14는 SEND_POS0, 15·16은 RMSH_INIT0·REMESH0을 호출한다(34–45). 작업 20..25의 명시된 CASE는 BCTSET0·SEND_CONT0·CONT_INIT_0·PART_SEND_TBLX·CONTACT0·MDPRESS0을 호출한다(46–57). 원문: `        CASE( 10 )` (34); `          CALL RDPRESS0(KK,RR,IFL(14),FLNAME,NLEN,ICHK)` (35); `        CASE( 11 )` (36); `          CALL RECV_SURF0(KK,RR,ICHK)` (37); `        CASE( 12 )` (38); `          CALL RECV_PRES0(KK)` (39); `        CASE( 14 )` (40); `          CALL SEND_POS0(KK(8),KK(10),KK(25))` (41); `        CASE( 15 )` (42); `          CALL RMSH_INIT0(KK,ICHK)` (43); `        CASE( 16 )` (44); `          CALL REMESH0(KK)` (45); `        CASE( 20 )` (46); `          CALL BCTSET0(KK)` (47); `        CASE( 21 )` (48); `          CALL SEND_CONT0(KK)` (49); `        CASE( 22 )` (50); `          CALL CONT_INIT_0(KK)` (51); `        CASE( 23 )` (52); `          CALL PART_SEND_TBLX(KK)` (53); `        CASE( 24 )` (54); `          CALL CONTACT0(KK,RR,IFL(11))` (55); `        CASE( 25 )` (56); `          CALL MDPRESS0(KK)` (57). [11-04 전수 검증 보완] |
| 58–68 | 시작 시 1행 glb_comm 루틴 안. 시작 시 11행 `DO` 안이며 이 루프는 66행 `ENDDO`에서 닫힌다. 시작 시 15행 `SELECT CASE( IOP )` 안이며 이 블록은 64행 `END SELECT`에서 닫힌다. 작업 30·31·32는 WT_RESTART0·RD_RESTART0·RECV_RST0을 호출한다(58–63). SELECT와 루프를 닫고 종료한다(64–68). 원문: `        CASE( 30 )` (58); `          CALL WT_RESTART0(KK,IFL,FLNAME,NLEN)` (59); `        CASE( 31 )` (60); `          CALL RD_RESTART0(KK,IFL(17),FLNAME,NLEN)` (61); `        CASE( 32 )` (62); `          CALL RECV_RST0()` (63); `        END SELECT` (64); `      ENDDO` (66); `      END` (68). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–66: SELECT CASE에는 CASE DEFAULT가 없다. 명시되지 않은 IOP는 루프의 다음 수신으로 이어진다.
