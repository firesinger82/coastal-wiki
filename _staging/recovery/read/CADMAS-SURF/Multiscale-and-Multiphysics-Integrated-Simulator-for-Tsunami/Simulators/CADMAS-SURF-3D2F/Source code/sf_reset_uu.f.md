---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_reset_uu.f
lines: 72
sha256: d55e1d7ccde98411b4ab8a7f70fdc8c9568f2139fbad7aa2d79ba0b85872efb5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_reset_uu.f — 판독 구간 기록

구간은 1행부터 72행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | SF_RESET_UU의 선언부다. 내부 셀을 순회한다(12–14). INDX=-1이면 UU=0으로 설정한다(16–18). 이전 INDXP/=0이고 현재 INDX=0이면 UU=0으로 설정한 뒤 CYCLE한다(20–24). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_RESET_UU(UU,INDXP,INDX,IXYZ,DBUF)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      INCLUDE 'VF_A0PRM.h'` (5); `      INCLUDE 'VF_ANUMBI.h'` (6); `      INCLUDE 'VF_APARAI.h'` (7); `      DIMENSION INDXP(NUMI,NUMJ,NUMK),INDX(NUMI,NUMJ,NUMK)` (9); `     &         ,UU(NUMI,NUMJ,NUMK),DBUF(*)` (10); `      DO K = 2, NUMK - 1` (12); `        DO J = MYJS, MYJE` (13); `          DO I = MYIS, MYIE` (14); `            IF( INDX(I,J,K) == -1 ) THEN` (16); `              UU(I,J,K) = 0.D0` (18); `            ELSEIF( INDXP(I,J,K) /= 0 .AND. INDX(I,J,K) == 0 ) THEN` (20); `              UU(I,J,K) = 0.D0` (22); `              CYCLE` (24). |
| 26–54 | 시작 시 `      DO K = 2, NUMK - 1` (12), `        DO J = MYJS, MYJE` (13), `          DO I = MYIS, MYIE` (14) 안이다. 이 루프들은 각각 68·67·66행 ENDDO에서 닫힌다. `            IF( INDX(I,J,K) == -1 ) THEN` (16)에서 시작한 사슬의 `            ELSEIF( INDXP(I,J,K) /= 0 .AND. INDX(I,J,K) == 0 ) THEN` (20) 분기 안이다. 이 사슬은 64행 ENDIF에서 닫힌다. 바로 앞 24행 CYCLE 때문에 이 분기에서 아래 이웃 탐색으로 진행하지 않는다. 뒤에 남아 있는 코드는 IDR=1..3과 IP=-1·1로 방향별 이웃을 선택하고 이전·현재 인덱스가 모두 0인 UU를 합산한다(26–53). 원문(연속 표시는 앞 문장에 이어짐): `              DO IDR = 1, 3` (26); `                IC = 0` (28); `                UUA = 0.` (29); `                DO IP = -1, 1, 2` (31); `                  SELECT CASE( IDR )` (33); `                  CASE( 1 )` (34); `                    II = I + IP` (35); `                    JJ = J` (36); `                    KK = K` (37); `                  CASE( 2 )` (38); `                    II = I` (39); `                    JJ = J + IP` (40); `                    KK = K` (41); `                  CASE( 3 )` (42); `                    II = I` (43); `                    JJ = J` (44); `                    KK = K + IP` (45); `                  END SELECT` (46); `                  IF( INDXP(II,JJ,KK)==0 .AND. INDX(II,JJ,KK)==0 ) THEN` (48); `                    IC = IC + 1` (49); `                    UUA = UUA + UU(II,JJ,KK)` (50); `                  ENDIF` (51); `                ENDDO` (53). [11-04 전수 검증 보완] |
| 55–72 | 시작 시 `      DO K = 2, NUMK - 1` (12), `        DO J = MYJS, MYJE` (13), `          DO I = MYIS, MYIE` (14) 안이다. 이 루프들은 각각 68·67·66행 ENDDO에서 닫힌다. `            IF( INDX(I,J,K) == -1 ) THEN` (16)에서 시작한 사슬의 `            ELSEIF( INDXP(I,J,K) /= 0 .AND. INDX(I,J,K) == 0 ) THEN` (20) 분기 안이다. 이 사슬은 64행 ENDIF에서 닫힌다. 추가로 `              DO IDR = 1, 3` (26) 안이다. IDR 루프는 60행 ENDDO에서 닫힌다. 24행 CYCLE 뒤에 놓인 평균 대입과 탐색 종료 코드다(55–62). 루프를 닫은 뒤 실행 흐름은 VF_P3SRD2(UU,DBUF,IXYZ)를 호출한다(64–70). 원문(연속 표시는 앞 문장에 이어짐): `                IF( IC > 0 ) THEN` (55); `                  UU(I,J,K) = UUA / DBLE(IC)` (56); `                  EXIT` (57); `                ENDIF` (58); `              ENDDO` (60); `              IF( IDR == 4 ) UU(I,J,K) = 0.D0` (62); `            ENDIF` (64); `          ENDDO` (66); `        ENDDO` (67); `      ENDDO` (68); `      CALL VF_P3SRD2(UU,DBUF,IXYZ)` (70); `      END` (72). 16–64행의 IF/ELSEIF에는 ELSE가 없다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20–26·55–62: ELSEIF 분기는 UU를 0으로 설정하고 CYCLE한다. 같은 분기 뒤의 이웃 탐색·평균 대입은 그 CYCLE을 통과하여 실행되지 않는다.
