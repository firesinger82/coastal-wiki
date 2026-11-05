---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/wt_restart0.f
lines: 62
sha256: 9d26738c5fc00a96b0d5f4fe5a1e75fab1e2d08cf2cb1f5f18d2373489f45479
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# wt_restart0.f — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | M_VAL·MPI_PARAM·암시적 배정밀도와 NNOW(100)·TNOW(100)를 선언한다(3–8). DATA INIT / 0 /을 둔다(10). ISEND를 받고 N=1로 시작한다(12–14). ICPL=2이고 ISEND=1이면 IROOTC에서 N을 받는다(16–17). 16행 분기 안에서 N이 양수이면 NNOW·TNOW를 받는다(18–21). 같은 분기 안에서 N은 양수 여부와 관계없이 방송한다(22). NNOW(N)는 N이 양수일 때만 방송한다(23). IRW=0이면 반환한다(26–28). 원문: `      SUBROUTINE WT_RESTART0(KK,IFL,FLNAME,NLEN)` (1); `      USE M_VAL` (3); `      USE MPI_PARAM` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      CHARACTER*256 FLNAME` (7); `      DIMENSION KK(*),IFL(*),NNOW(100),TNOW(100)` (8); `      DATA INIT / 0 /` (10); `      CALL M_MPI_RECV_I(ISEND,1,1)` (12); `      N = 1` (14); `      IF( ICPL == 2 .AND. ISEND == 1 ) THEN` (16); `        CALL C_MPI_RECV_I(N,1,IROOTC)` (17); `        IF( N > 0 ) THEN` (18); `          CALL C_MPI_RECV_I(NNOW,N,IROOTC)` (19); `          CALL C_MPI_RECV_D(TNOW,N,IROOTC)` (20); `        ENDIF` (21); `        CALL M_MPI_BCAST_I(N,1)` (22); `        IF( N > 0 ) CALL M_MPI_BCAST_I(NNOW(N),1)` (23); `      ENDIF` (24); `      CALL M_MPI_RECV_I(IRW,1,1)` (26); `      IF( IRW == 0 ) RETURN` (28). [11-04 전수 검증 정정] |
| 30–44 | 시작 시 1행 wt_restart0 루틴 안. INIT=0인 첫 출력 분기에서 INIT=1로 바꾸고 .rsto000 비형식(unformatted) 파일과 .rtm 파일을 연다(30–36). ICPL=2이면 두 모델의 단계·시간 열 제목을 쓴다(38–43). 원문: `      IF( INIT == 0 ) THEN` (30); `        INIT = 1` (32); `        OPEN(IFL(16),FILE=FLNAME(1:NLEN)//'.rsto000',FORM='UNFORMATTED')` (34); `        OPEN(IFL(18),FILE=FLNAME(1:NLEN)//'.rtm')` (36); `        IF( ICPL == 2 )` (38); `     &    WRITE(IFL(18),'(A/A/)')` (39); `     &    '     [ C A D M A S ]          [ S  T  R ]',` (40); `     &    '    STEP        TIME       STEP        TIME'` (41); `      ENDIF` (43). |
| 45–62 | 시작 시 1행 wt_restart0 루틴 안. 프로세스 1에서 ISTEP을 받아 ISTEP·NNOW(N)를 기록한다(45–47). KK(92) 양수이면 접촉·마찰 상태도 쓴다(49–50). TIM3를 받고 ICPL=2이면 I=1..N의 NNOW·TNOW와 STR 단계·시간을 쓴다(52–57). 나머지는 TIM3만 출력한다(58–60). 원문: `      CALL M_MPI_RECV_I(ISTEP,1,1)` (45); `      WRITE(IFL(16)) ISTEP,NNOW(N)` (47); `      IF( KK(92) > 0 )` (49); `     &  WRITE(IFL(16)) ISLV0,ISLVP,RSLV0,U0,RL0,IFRIC,ISTK,FRIC` (50); `      CALL M_MPI_RECV_D(TIM3,1,1)` (52); `      IF( ICPL == 2 ) THEN` (54); `        DO I = 1, N` (55); `          WRITE(IFL(18),'(2(I8,F15.6))') NNOW(I),TNOW(I),ISTEP,TIM3` (56); `        ENDDO` (57); `      ELSE` (58); `        WRITE(IFL(18),'(F15.6)') TIM3` (59); `      ENDIF` (60); `      END` (62). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8·17–20: NNOW와 TNOW의 선언 길이는 100이다. 수신 길이 N의 상한을 검사하는 문장은 이 파일에 없다.
- 14–24·47: NNOW 값을 받는 경로는 ICPL=2이고 ISEND=1이며 N>0인 분기이다. 그 분기 밖에서도 IRW가 0이 아니면 NNOW(N)을 기록한다.
- 30–43·62: 최초 출력 시 파일 두 개를 연다. 이 루틴에는 CLOSE 문이 없다.
