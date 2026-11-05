---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/femap/fmp_rod.f
lines: 40
sha256: 89f8daf79b24607104eb7cc019b67a37d6f00199b907883643fc43ee74ad3886
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fmp_rod.f — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | FMP_ROD는 MPI_PARAM을 사용한다. IMPLICIT 및 SIGG(6*MGP,*)·IELM(NM,*) 선언은 아래와 같다. MYRANK=0과 NROD=0이 함께 성립하면 반환한다. NROD 크기의 IENO·SIG를 할당하고 NER 다음 요소들의 번호와 SIGG 첫 성분을 복사한다. 원문: `      SUBROUTINE FMP_ROD(IOUT,NER,NROD,IELM,NM,SIGG,MGP,IFL)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      CHARACTER*1 C /','/` (6); `      DIMENSION SIGG(6*MGP,*),IELM(NM,*)` (7); `      INTEGER, POINTER :: IENO(:)` (9); `      REAL(8), POINTER :: SIG(:)` (10); `      IF( MYRANK == 0 .AND. NROD == 0 ) RETURN` (12); `      ALLOCATE( IENO(NROD) )` (14); `      ALLOCATE( SIG(NROD) )` (15); `      IENO(:) = IELM(1,NER+1:NER+NROD)` (17); `      SIG(:) = SIGG(1,NER+1:NER+NROD)` (18) |
| 20–40 | MYRANK=0이면 결과 번호 80·Rod Axial Stress 제목을 쓰고 WT_VEC으로 축응력(axial stress)을 출력한다. ELSE는 NER·NROD·IENO·SIG를 목적지 0에 전송한다. 두 배열을 해제하고 루틴을 끝낸다. 원문: `      IF( MYRANK == 0 ) THEN` (20); `        WRITE(IFL,'(3(I0,A))') IOUT,C,80,C,1,C` (22); `        WRITE(IFL,'(A)') 'Rod Axial Stress'` (24); `        CALL WT_VEC(0,0,0,8,IENO,SIG,1,1,NROD,IFL)` (26); `      ELSE` (28); `       CALL M_MPI_SEND_I(NER,1,0)` (30); `       CALL M_MPI_SEND_I(NROD,1,0)` (31); `       CALL M_MPI_SEND_I(IENO,NROD,0)` (32); `       CALL M_MPI_SEND_D(SIG,NROD,0)` (33); `      ENDIF` (35); `      DEALLOCATE( IENO )` (37); `      DEALLOCATE( SIG )` (38); `      END` (40) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–18: NROD=0 조기 반환은 MYRANK=0에서만 적용한다.
