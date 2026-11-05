---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/main/tstepset.f
lines: 41
sha256: 6120b1fc212f7f166aca194448f1abbfc478ce1a6eda652a7a207636d45c37ea
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# tstepset.f — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | TSTEPSET은 ISTP에서 ISID와 일치하는 시간 단계(time step) 세트를 검색한다(9–18). ADDSET3로 IS·IE를 얻고 NSTP(1,J)를 합산하여 NSTEP·KK(7)을 정한다(11–20). D_T·IOUT를 할당하고 IOUT를 0으로 초기화한다(22–25). 각 구간의 NI개 단계에 DELT(J)를 복사하고 MOD(K,NOI)=0 또는 K=NI이면 출력 표시를 1로 설정한다(29–37). KK(6)의 설정값은 50이다(39). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE TSTEPSET(ISID,KK)` (1) <br> `      USE M_VAL` (3) <br> `      IMPLICIT REAL*8(A-H,O-Z)` (5) <br> `      DIMENSION KK(*)` (7) <br> `      DO I = 1, KK(78)` (9) <br> `        IF( ISTP(1,I) == ISID ) THEN` (10) <br> `          CALL ADDSET3(IS,IE,ISTP,I)` (11) <br> `          NSTEP = 0` (12) <br> `          DO J = IS, IE` (13) <br> `            NSTEP = NSTEP + NSTP(1,J)` (14) <br> `          ENDDO` (15) <br> `          EXIT` (16) <br> `        ENDIF` (17) <br> `      ENDDO` (18) <br> `      KK(7) = NSTEP` (20) <br> `      ALLOCATE( D_T(NSTEP) )` (22) <br> `      ALLOCATE( IOUT(NSTEP) )` (23) <br> `      IOUT(:) = 0` (25) <br> `      IP = 0` (27) <br> `      DO J = IS, IE` (29) <br> `        NI = NSTP(1,J)` (30) <br> `        NOI = NSTP(2,J)` (31) <br> `        DO K = 1, NI` (32) <br> `          IP = IP + 1` (33) <br> `          D_T(IP) = DELT(J)` (34) <br> `          IF( MOD(K,NOI) == 0 .OR. K == NI ) IOUT(IP) = 1` (35) <br> `        ENDDO` (36) <br> `      ENDDO` (37) <br> `      KK(6) = 50` (39) <br> `      END` (41) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–20·29: 세트를 찾지 못하는 경우 NSTEP·IS·IE를 설정하는 기본 경로가 없다.
- 31–35: NOI를 MOD(K,NOI)의 두 번째 인수로 사용한다. 이 파일에는 NOI=0 검사 조건이 없다.
- 39: KK(6)에 상수 50을 대입한다.
