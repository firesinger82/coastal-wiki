---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/fmp_rod0.f
lines: 52
sha256: cc2f850b12be3d2915feab081fbc09421f5b1465f2a8cfa5c4183d7c9d600f53
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fmp_rod0.f — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | MPI_PARAM·M_PART와 번호·응력 포인터를 선언한다(3–8). 네 배열을 NROD 크기로 할당하고 IENO를 0으로 초기화한다(10–16). 원문: `      SUBROUTINE FMP_ROD0(IOUT,NER,NROD,IFL)` (1); `      USE MPI_PARAM` (3); `      USE M_PART` (4); `      CHARACTER*1 C /','/` (6); `      INTEGER, POINTER :: IENO(:),IENOW(:)` (7); `      REAL(8), POINTER :: SIG(:),SIGW(:)` (8); `      ALLOCATE( IENO(NROD) )` (10); `      ALLOCATE( SIG(NROD) )` (11); `      ALLOCATE( IENOW(NROD) )` (13); `      ALLOCATE( SIGW(NROD) )` (14); `      IENO(:) = 0` (16). |
| 18–35 | 시작 시 1행 fmp_rod0 루틴 안. 각 작업 프로세스에서 NERW·NRODW·번호·응력을 받는다(18–23). IEL(NERW+I,IP)로 전역 요소를 얻고 NER를 빼 봉 위치 IR을 계산한다(25–27). IENO(IR)가 0일 때만 번호·응력을 대입한다(28–31). 원문: `      DO IP = 1, NPROCS - 1` (18); `        CALL M_MPI_RECV_I(NERW,1,IP)` (20); `        CALL M_MPI_RECV_I(NRODW,1,IP)` (21); `        CALL M_MPI_RECV_I(IENOW,NRODW,IP)` (22); `        CALL M_MPI_RECV_D(SIGW,NRODW,IP)` (23); `        DO I = 1, NRODW` (25); `          IE = IEL(NERW+I,IP)` (26); `          IR = IE - NER` (27); `          IF( IENO(IR) == 0 ) THEN` (28); `            IENO(IR) = IENOW(I)` (29); `            SIG(IR) = SIGW(I)` (30); `          ENDIF` (31); `        ENDDO` (32); `      ENDDO` (34). |
| 36–52 | 시작 시 1행 fmp_rod0 루틴 안. NROD 양수 분기에서 항목 80과 봉 축응력(axial stress) 제목을 쓰고 WT_VEC으로 출력한다(36–44). 네 배열을 해제하고 종료한다(46–52). 원문: `      IF( NROD > 0 ) THEN` (36); `        WRITE(IFL,'(3(I0,A))') IOUT,C,80,C,1,C` (38); `        WRITE(IFL,'(A)') 'Rod Axial Stress'` (40); `        CALL WT_VEC(0,0,0,8,IENO,SIG,1,1,NROD,IFL)` (42); `      ENDIF` (44); `      DEALLOCATE( IENO )` (46); `      DEALLOCATE( SIG )` (47); `      DEALLOCATE( IENOW )` (49); `      DEALLOCATE( SIGW )` (50); `      END` (52). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16·28–30: 번호가 0인 위치만 응력을 채운다. SIG 전체 초기화는 이 파일에 없다.
