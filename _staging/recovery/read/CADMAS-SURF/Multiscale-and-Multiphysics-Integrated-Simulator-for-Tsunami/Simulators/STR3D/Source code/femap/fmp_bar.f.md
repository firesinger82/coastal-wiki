---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/femap/fmp_bar.f
lines: 40
sha256: 16a68cfc1195ed96ea124e7259d71089baf1ab24128c118e09f4d8628c885376
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fmp_bar.f — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | FMP_BAR는 MPI_PARAM을 사용한다. IMPLICIT 선언과 배열 SIGG(6*MGP,*)·IELM(NM,*)를 아래에 그대로 적었다. MYRANK=0이며 NBAR=0일 때 반환한다. 요소 번호와 SIGG의 13번째 성분을 NBAR 크기 포인터 배열로 모은다. 원문: `      SUBROUTINE FMP_BAR(IOUT,NEB,NBAR,IELM,NM,SIGG,MGP,IFL)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      CHARACTER*1 C /','/` (6); `      DIMENSION SIGG(6*MGP,*),IELM(NM,*)` (7); `      INTEGER, POINTER :: IENO(:)` (9); `      REAL(8), POINTER :: SIG(:)` (10); `      IF( MYRANK == 0 .AND. NBAR == 0 ) RETURN` (12); `      ALLOCATE( IENO(NBAR) )` (14); `      ALLOCATE( SIG(NBAR) )` (15); `      IENO(:) = IELM(1,NEB+1:NEB+NBAR)` (17); `      SIG(:) = SIGG(13,NEB+1:NEB+NBAR)` (18) |
| 20–40 | MYRANK=0이면 결과 번호 81과 Bar Axial Stress 제목을 쓰고 WT_VEC으로 출력한다. ELSE는 NEB·NBAR·IENO·SIG를 목적지 0에 보낸다. 전송 호출과 인수를 아래에 그대로 적었다. 두 포인터를 해제하고 끝낸다. 원문: `      IF( MYRANK == 0 ) THEN` (20); `        WRITE(IFL,'(3(I0,A))') IOUT,C,81,C,1,C` (22); `        WRITE(IFL,'(A)') 'Bar Axial Stress'` (24); `        CALL WT_VEC(0,0,0,8,IENO,SIG,1,1,NBAR,IFL)` (26); `      ELSE` (28); `       CALL M_MPI_SEND_I(NEB,1,0)` (30); `       CALL M_MPI_SEND_I(NBAR,1,0)` (31); `       CALL M_MPI_SEND_I(IENO,NBAR,0)` (32); `       CALL M_MPI_SEND_D(SIG,NBAR,0)` (33); `      ENDIF` (35); `      DEALLOCATE( IENO )` (37); `      DEALLOCATE( SIG )` (38); `      END` (40) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7·18: SIGG의 첫 차원은 6*MGP이며 추출 성분은 고정된 13이다.
- 12–18: NBAR=0 조기 반환은 MYRANK=0에서만 적용한다.
