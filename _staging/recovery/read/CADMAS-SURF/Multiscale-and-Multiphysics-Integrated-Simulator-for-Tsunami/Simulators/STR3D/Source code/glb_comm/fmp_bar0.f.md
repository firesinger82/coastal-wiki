---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/fmp_bar0.f
lines: 52
sha256: 5773d114cd2e3a14eb02c4ec6fcaa310f1437502d26390e4a90843b398f3f5d7
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fmp_bar0.f — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | MPI_PARAM·M_PART를 사용한다(3–4). 요소 번호와 응력의 전역·수신 포인터 배열을 NBAR 크기로 할당한다(7–14). IENO를 0으로 초기화한다(16). 원문: `      SUBROUTINE FMP_BAR0(IOUT,NEB,NBAR,IFL)` (1); `      USE MPI_PARAM` (3); `      USE M_PART` (4); `      CHARACTER*1 C /','/` (6); `      INTEGER, POINTER :: IENO(:),IENOW(:)` (7); `      REAL(8), POINTER :: SIG(:),SIGW(:)` (8); `      ALLOCATE( IENO(NBAR) )` (10); `      ALLOCATE( SIG(NBAR) )` (11); `      ALLOCATE( IENOW(NBAR) )` (13); `      ALLOCATE( SIGW(NBAR) )` (14); `      IENO(:) = 0` (16). |
| 18–35 | 시작 시 1행 fmp_bar0 루틴 안. IP 루프로 각 작업 프로세스의 NEBW·NBARW·요소 번호·응력을 M_MPI_RECV_I/D로 받는다(18–23). I 루프에서 IEL로 전역 요소를 찾고 NEB를 빼서 보 위치를 계산한다(25–27). 전역 번호가 아직 0일 때만 번호·응력을 채운다(28–31). 원문: `      DO IP = 1, NPROCS - 1` (18); `        CALL M_MPI_RECV_I(NEBW,1,IP)` (20); `        CALL M_MPI_RECV_I(NBARW,1,IP)` (21); `        CALL M_MPI_RECV_I(IENOW,NBARW,IP)` (22); `        CALL M_MPI_RECV_D(SIGW,NBARW,IP)` (23); `        DO I = 1, NBARW` (25); `          IE = IEL(NEBW+I,IP)` (26); `          IB = IE - NEB` (27); `          IF( IENO(IB) == 0 ) THEN` (28); `            IENO(IB) = IENOW(I)` (29); `            SIG(IB) = SIGW(I)` (30); `          ENDIF` (31); `        ENDDO` (32); `      ENDDO` (34). |
| 36–52 | 시작 시 1행 fmp_bar0 루틴 안. NBAR가 양수일 때 항목 번호 81과 보 축응력(axial stress) 제목을 쓰고 WT_VEC으로 결과를 출력한다(36–44). 네 포인터 배열을 해제하고 종료한다(46–52). 원문: `      IF( NBAR > 0 ) THEN` (36); `        WRITE(IFL,'(3(I0,A))') IOUT,C,81,C,1,C` (38); `        WRITE(IFL,'(A)') 'Bar Axial Stress'` (40); `        CALL WT_VEC(0,0,0,8,IENO,SIG,1,1,NBAR,IFL)` (42); `      ENDIF` (44); `      DEALLOCATE( IENO )` (46); `      DEALLOCATE( SIG )` (47); `      DEALLOCATE( IENOW )` (49); `      DEALLOCATE( SIGW )` (50); `      END` (52). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16·28–30: 중복된 보 위치에서는 IENO가 0인 경우에만 응력을 대입한다. SIG 전체 초기화는 이 파일에 없다.
