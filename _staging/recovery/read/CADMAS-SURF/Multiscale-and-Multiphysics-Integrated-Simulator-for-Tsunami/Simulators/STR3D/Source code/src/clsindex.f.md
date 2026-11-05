---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/clsindex.f
lines: 77
sha256: cd2d35cac46f6a51a60e13e9d19952353a4160310ce94d3b80b32949c370f22b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# clsindex.f — 판독 구간 기록

구간은 1행부터 77행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | CLSINDEX에서 M_VAL·MPC_WORK·M_MUMPS를 사용한다. KK(87)이 양수이면 11–24행에 열거한 배열을 해제한다. 해석: 이 배열들은 제약 관련 자료이다. 이후 RHV·X·IDSK·IDCG를 해제한다. 원문: `      SUBROUTINE CLSINDEX(KK,IFMTX1,IFMTX2)` (1); `      USE M_VAL` (3); `      USE MPC_WORK` (4); `      USE M_MUMPS` (5); `      REAL*8 DDUM` (7); `      DIMENSION KK(*)` (8); 주석 원문 `C----&------------------------------------------------------------------` (9); `      IF( KK(87) > 0 ) THEN` (10); `        DEALLOCATE(IDEP)` (11); `        DEALLOCATE(CIDP)` (12); `        DEALLOCATE(IDX)` (13); `        DEALLOCATE(IRH)` (14); `        DEALLOCATE(IFRH)` (15); `        DEALLOCATE(CRH)` (16); `        DEALLOCATE(IDL)` (17); `        DEALLOCATE(ROWL)` (18); `        DEALLOCATE(COLL)` (19); `        DEALLOCATE(ROWR)` (20); `        DEALLOCATE(COLR)` (21); `        DEALLOCATE(B)` (22); `        DEALLOCATE(MPCF)` (23); `        DEALLOCATE(RMPC)` (24); `      ENDIF` (25); `      DEALLOCATE(RHV)` (27); `      DEALLOCATE(X)` (28); `      DEALLOCATE(IDSK)` (30); `      DEALLOCATE(IDCG)` (31). [11-04 전수 검증 정정] |
| 33–50 | 시작 시 1행 CLSINDEX 루틴 안. KK(21)의 SELECT CASE에서 1·11은 CGWK와 STF를 해제하고 1에서만 LOW를 해제한다. 2에서는 작업 배열들과 STF·SYM·NUM을 해제하며 IFMTX1·IFMTX2 파일을 STATUS='DELETE'로 닫는다. 원문: `      SELECT CASE( KK(21) )` (33); `      CASE( 1, 11 )` (34); `        DEALLOCATE(CGWK)` (36); `        DEALLOCATE(STF)` (37); `        IF( KK(21) == 1 ) DEALLOCATE(LOW)` (38); `      CASE( 2 )` (40); `        DEALLOCATE(IASEWK)` (42); `        DEALLOCATE(ASEWK)` (43); `        DEALLOCATE(STF)` (44); `        DEALLOCATE(SYM)` (45); `        DEALLOCATE(NUM)` (46); `        CLOSE(IFMTX1,STATUS='DELETE')` (48); `        CLOSE(IFMTX2,STATUS='DELETE')` (49). |
| 51–77 | 시작 시 33행 `      SELECT CASE( KK(21) )` 안이다. 이 SELECT는 75행 `      END SELECT`에서 닫힌다. CASE DEFAULT는 없다. 3·13에서는 STF를 해제하고 MTYPE을 각각 -2·11로 정한다. 61–62행 PARDISO 호출은 주석 처리된 코드다. 4·14에서는 MUMPS의 IRN과 STF를 해제하고 JOB=-2를 설정한다. M_MPI_BCAST_I로 JOB을 전달한 뒤 DMUMPS를 호출한다. SELECT와 루틴 끝을 포함한다. 원문: `      CASE( 3, 13 )` (51); `        DEALLOCATE( STF )` (53); `        IF( KK(21) == 3 ) THEN` (55); `          MTYPE = -2` (56); `        ELSE` (57); `          MTYPE = 11` (58); `        ENDIF` (59); 주석 원문 `!        CALL PARDISO(PT,1,1,MTYPE,-1,KK(19),DDUM,IDUM,IDUM,IDUM,1,IPARM` (61); 주석 원문 `!     &              ,0,DDUM,DDUM,IERR)` (62); `      CASE( 4, 14 )` (64); `        DEALLOCATE( MUMPS_PAR%IRN )` (66); `        DEALLOCATE( STF )` (67); `        MUMPS_PAR%JOB = -2` (69); `        CALL M_MPI_BCAST_I(MUMPS_PAR%JOB,1)` (71); `        CALL DMUMPS(MUMPS_PAR)` (73); `      END SELECT` (75); `      END` (77). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 55–62: MTYPE을 설정하지만 MTYPE을 전달하는 PARDISO 호출은 주석 처리되어 있다.
- 10–31·36–46·53·66–67: DEALLOCATE 앞에 ALLOCATED 검사는 이 파일에 없다.
