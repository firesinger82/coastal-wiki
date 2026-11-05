---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/seq/clsindex_s.f
lines: 71
sha256: 92d113e6930f80647e163ae7299e13d31836f6e0d36969dbb50302468e40ca3e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# clsindex_s.f — 판독 구간 기록

구간은 1행부터 71행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | CLSINDEX_S의 모듈·실수·배열 선언. ISEEP=0이고 I_BCT>0이며 KK(87)>0이면 다점 구속(multipoint constraint) 작업 배열들을 해제한다. RHV·X·IDSK·IDCG는 조건 없이 해제한다. 원문: `      SUBROUTINE CLSINDEX_S(I_BCT,ISEEP,KK,IFMTX1,IFMTX2)` (1); `      USE M_VAL` (3); `      USE MPC_WORK` (4); `      USE M_MUMPS` (5); `      REAL*8 DDUM` (7); `      DIMENSION KK(*)` (8); `C----&------------------------------------------------------------------` (9); `      IF( ISEEP == 0 .AND. I_BCT > 0 .AND. KK(87) > 0 ) THEN` (10); `        DEALLOCATE(IDEP)` (11); `        DEALLOCATE(CIDP)` (12); `        DEALLOCATE(IDX)` (13); `        DEALLOCATE(IRH)` (14); `        DEALLOCATE(IFRH)` (15); `        DEALLOCATE(CRH)` (16); `        DEALLOCATE(IDL)` (17); `        DEALLOCATE(ROWL)` (18); `        DEALLOCATE(COLL)` (19); `        DEALLOCATE(ROWR)` (20); `        DEALLOCATE(COLR)` (21); `        DEALLOCATE(B)` (22); `        DEALLOCATE(MPCF)` (23); `        DEALLOCATE(RMPC)` (24); `      ENDIF` (25); `      DEALLOCATE(RHV)` (27); `      DEALLOCATE(X)` (28); `      DEALLOCATE(IDSK)` (30); `      DEALLOCATE(IDCG)` (31). |
| 33–71 | CLSINDEX_S 루틴 안. KK(21)의 1·2·3·4에 따라 풀이기 배열을 해제한다. 유형 2는 행렬 파일을 삭제하며 닫는다. 55–56행 PARDISO 호출은 주석 처리된 코드다. 유형 4는 MUMPS의 JOB=-2를 방송한 뒤 DMUMPS를 호출한다. 원문: `      SELECT CASE( KK(21) )` (33); `      CASE( 1 )` (34); `        DEALLOCATE(CGWK)` (36); `        DEALLOCATE(STF)` (37); `        DEALLOCATE(LOW)` (38); `      CASE( 2 )` (40); `        DEALLOCATE(IASEWK)` (42); `        DEALLOCATE(ASEWK)` (43); `        DEALLOCATE(STF)` (44); `        DEALLOCATE(SYM)` (45); `        DEALLOCATE(NUM)` (46); `        CLOSE(IFMTX1,STATUS='DELETE')` (48); `        CLOSE(IFMTX2,STATUS='DELETE')` (49); `      CASE( 3 )` (51); `        DEALLOCATE( STF )` (53); `!        CALL PARDISO(PT,1,1,-2,-1,KK(19),DDUM,IDUM,IDUM,IDUM,1,IPARM` (55); `!     &              ,0,DDUM,DDUM,IERR)` (56); `      CASE( 4 )` (58); `        DEALLOCATE( MUMPS_PAR%IRN )` (60); `        DEALLOCATE( STF )` (61); `        MUMPS_PAR%JOB = -2` (63); `        CALL M_MPI_BCAST_I(MUMPS_PAR%JOB,1)` (65); `        CALL DMUMPS(MUMPS_PAR)` (67); `      END SELECT` (69); `      END` (71). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 55–56: PARDISO 정리 호출은 주석 처리되어 있다.
- 7·55–56: DDUM은 선언되지만 실행 코드에서는 참조하지 않는다.
