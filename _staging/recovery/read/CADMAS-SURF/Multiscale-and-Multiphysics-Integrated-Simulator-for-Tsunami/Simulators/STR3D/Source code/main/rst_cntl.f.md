---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/main/rst_cntl.f
lines: 109
sha256: a9cc87a49e720a95439b3120dc13685cbd06fbe805aa7409a2b0df557910b752
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# rst_cntl.f — 판독 구간 기록

구간은 1행부터 109행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | RST_CNTL은 D_T 누적합을 TIME에 저장한다(11–20). RTIM(1)>0이면 재시작(restart) 입력 시각과 각 TIME의 절대 차를 비교한다(22–35). 오차가 줄어들 때만 계속 탐색하고 그 외에는 EXIT한다(30–34). 선택 단계는 J-1이며 KK(84)에 저장한다(37). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE RST_CNTL(KK)` (1) <br> `      USE M_VAL` (3) <br> `      IMPLICIT REAL*8(A-H,O-Z)` (5) <br> `      DIMENSION KK(*)` (7) <br> `      REAL(8), POINTER :: TIME(:)` (9) <br> `      NSTEP = KK(7)` (11) <br> `      NRST = KK(83)` (12) <br> `      ALLOCATE( TIME(NSTEP) )` (14) <br> `      TIME(1) = D_T(1)` (16) <br> `      DO I = 2, NSTEP` (18) <br> `        TIME(I) = TIME(I-1) + D_T(I)` (19) <br> `      ENDDO` (20) <br> `      IF( RTIM(1) > 0. ) THEN` (22) <br> `        RTIME = RTIM(1)` (24) <br> `        EPS_MIN = DABS( RTIME - TIME(1) )` (26) <br> `        DO J = 2, NSTEP` (28) <br> `          EPS = DABS( RTIME - TIME(J) )` (29) <br> `          IF( EPS < EPS_MIN ) THEN` (30) <br> `            EPS_MIN = EPS` (31) <br> `          ELSE` (32) <br> `            EXIT` (33) <br> `          ENDIF` (34) <br> `        ENDDO` (35) <br> `        KK(84) = J - 1` (37) <br> `      ENDIF` (39) |
| 41–79 | 시작 시 RST_CNTL(1) 안이며 앞 조건 밖이다. IROUT를 0으로 초기화한다(41–43). RTIM(2)>0이면 RDT 간격으로 RTIME을 증가시킨다(45–55). JS+1:NSTEP에서 절대 오차가 감소하는 동안 탐색하여 J-1 위치를 표시한다(57–68). J=NSTEP+1이면 53–74행의 DO 루프를 EXIT로 빠져나온다. 그 외에는 JS=J로 다음 시각을 검색한다(70–74). 표시 개수를 KK(83)에 더한다(76–78). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      ALLOCATE( IROUT(NSTEP) )` (41) <br> `      IROUT(:) = 0` (43) <br> `      IF( RTIM(2) > 0. ) THEN` (45) <br> `        RDT = RTIM(2)` (47) <br> `        RTIME = 0.` (49) <br> `        JS = 1` (51) <br> `        DO` (53) <br> `          RTIME = RTIME + RDT` (55) <br> `          EPS_MIN = DABS( RTIME - TIME(JS) )` (57) <br> `          DO J = JS + 1, NSTEP` (59) <br> `            EPS = DABS( RTIME - TIME(J) )` (60) <br> `            IF( EPS < EPS_MIN ) THEN` (61) <br> `              EPS_MIN = EPS` (62) <br> `            ELSE` (63) <br> `              EXIT` (64) <br> `            ENDIF` (65) <br> `          ENDDO` (66) <br> `          IROUT( J - 1 ) = 1` (68) <br> `          IF( J == NSTEP + 1 ) EXIT` (70) <br> `          JS = J` (72) <br> `        ENDDO` (74) <br> `        DO J = 1, NSTEP` (76) <br> `          IF( IROUT(J) == 1 ) KK(83) = KK(83) + 1` (77) <br> `        ENDDO` (78) [11-04 전수 검증 정정] |
| 80–109 | 시작 시 RST_CNTL(1)·45행 `IF( RTIM(2) > 0. ) THEN`에서 시작한 IF 사슬의 `ELSEIF( NRST > 0 ) THEN`에서 시작한다(80). 이 분기는 RTIM(2) > 0.이 거짓이고 NRST > 0일 때 실행한다. 이 IF 사슬은 마지막 ELSE 없이 105행 ENDIF에서 닫힌다. 해석: 이 분기는 명시적 출력 시각 목록을 처리하는 경로로 읽는다(80–86). RTIM(2+I)마다 절대 오차 감소 탐색을 수행하고 J-1의 IROUT를 1로 설정하며 JS=J로 갱신한다(88–103). 조건을 닫고 TIME을 해제한다(105–107). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      ELSEIF( NRST > 0 ) THEN` (80) <br> `        JS = 1` (82) <br> `        DO I = 1, NRST` (84) <br> `          RTIME = RTIM(2+I)` (86) <br> `          EPS_MIN = DABS( RTIME - TIME(JS) )` (88) <br> `          DO J = JS + 1, NSTEP` (90) <br> `            EPS = DABS( RTIME - TIME(J) )` (91) <br> `            IF( EPS < EPS_MIN ) THEN` (92) <br> `              EPS_MIN = EPS` (93) <br> `            ELSE` (94) <br> `              EXIT` (95) <br> `            ENDIF` (96) <br> `          ENDDO` (97) <br> `          IROUT( J - 1 ) = 1` (99) <br> `          JS = J` (101) <br> `        ENDDO` (103) <br> `      ENDIF` (105) <br> `      DEALLOCATE( TIME )` (107) <br> `      END` (109) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–16: TIME을 NSTEP 크기로 할당한 직후 TIME(1)에 대입한다. NSTEP=0을 검사하는 분기는 이 파일에 없다.
- 12·76–78: NRST는 입구의 KK(83)을 복사한다. 간격 지정 경로는 표시 개수를 기존 KK(83)에 더하며 그 앞 KK(83)=0 대입은 없다.
- 30–34·61–65·92–96: 오차가 같은 경우는 ELSE로 들어가 검색을 종료한다.
