---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_reset_ff.f
lines: 72
sha256: f373fcf32797a796ac7f16ae8355fa678611e18c84dfc42cdc8ae56fd9d87578
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_reset_ff.f — 판독 구간 기록

구간은 1행부터 72행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | SF_RESET_FF의 선언부다. 내부 셀을 순회한다(12–14). NF<0이면 FF를 0으로 만든다(17–19). 이전 NFP<0이고 현재 NF=0이면 복원 분기로 들어간다(22). NF=-2에 한정한 이전 두 조건은 주석 처리되어 있다(16·21). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_RESET_FF(FF,NFP,NF,DBUF)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      INCLUDE 'VF_A0PRM.h'` (5); `      INCLUDE 'VF_ANUMBI.h'` (6); `      INCLUDE 'VF_APARAI.h'` (7); `      DIMENSION NFP(NUMI,NUMJ,NUMK),NF(NUMI,NUMJ,NUMK)` (9); `     &         ,FF(NUMI,NUMJ,NUMK),DBUF(*)` (10); `      DO K = 2, NUMK - 1` (12); `        DO J = MYJS, MYJE` (13); `          DO I = MYIS, MYIE` (14); 주석 처리된 코드: `!           IF( NF(I,J,K) == -2 ) THEN` (16); `            IF( NF(I,J,K) < 0 ) THEN  ! FOR CADMAS-STM` (17); `              FF(I,J,K) = 0.` (19); 주석 처리된 코드: `!           ELSEIF( NFP(I,J,K) == -2 .AND. NF(I,J,K) == 0 ) THEN` (21); `            ELSEIF( NFP(I,J,K) < 0 .AND. NF(I,J,K) == 0 ) THEN  ! FOR CADMAS-STM` (22). 해석: FF는 VOF 함수로 읽힌다. [11-04 전수 검증 정정] |
| 24–54 | 시작 시 `      DO K = 2, NUMK - 1` (12), `        DO J = MYJS, MYJE` (13), `          DO I = MYIS, MYIE` (14) 안이다. 이 루프들은 각각 68·67·66행 ENDDO에서 닫힌다. `            IF( NF(I,J,K) < 0 ) THEN  ! FOR CADMAS-STM` (17)에서 시작한 사슬의 `            ELSEIF( NFP(I,J,K) < 0 .AND. NF(I,J,K) == 0 ) THEN  ! FOR CADMAS-STM` (22) 분기 안이다. 이 사슬은 64행 ENDIF에서 닫힌다. IDR=1부터 3까지 탐색한다(24). IDR/=2일 때만 IC·FFA를 초기화한다(26–29). IP=-1·1과 방향 선택으로 이웃 첨자를 만들고 이전·현재 분류가 모두 음수가 아닌 이웃의 FF를 합산한다(31–53). 원문(연속 표시는 앞 문장에 이어짐): `              DO IDR = 1, 3` (24); `                IF( IDR /= 2 ) THEN` (26); `                  IC = 0` (27); `                  FFA = 0.` (28); `                ENDIF` (29); `                DO IP = -1, 1, 2` (31); `                  SELECT CASE( IDR )` (33); `                  CASE( 1 )` (34); `                    II = I + IP` (35); `                    JJ = J` (36); `                    KK = K` (37); `                  CASE( 2 )` (38); `                    II = I` (39); `                    JJ = J + IP` (40); `                    KK = K` (41); `                  CASE( 3 )` (42); `                    II = I` (43); `                    JJ = J` (44); `                    KK = K + IP` (45); `                  END SELECT` (46); `                  IF( NFP(II,JJ,KK) >= 0 .AND. NF(II,JJ,KK) >= 0 ) THEN` (48); `                    IC = IC + 1` (49); `                    FFA = FFA + FF(II,JJ,KK)` (50); `                  ENDIF` (51); `                ENDDO` (53). [11-04 전수 검증 보완] |
| 55–72 | 시작 시 `      DO K = 2, NUMK - 1` (12), `        DO J = MYJS, MYJE` (13), `          DO I = MYIS, MYIE` (14) 안이다. 이 루프들은 각각 68·67·66행 ENDDO에서 닫힌다. `            IF( NF(I,J,K) < 0 ) THEN  ! FOR CADMAS-STM` (17)에서 시작한 사슬의 `            ELSEIF( NFP(I,J,K) < 0 .AND. NF(I,J,K) == 0 ) THEN  ! FOR CADMAS-STM` (22) 분기 안이다. 이 사슬은 64행 ENDIF에서 닫힌다. 추가로 `              DO IDR = 1, 3` (24) 안이다. IDR 루프는 60행 ENDDO에서 닫힌다. IDR>=2이고 IC>0이면 평균을 FF에 넣고 방향 루프를 나간다(55–58). 세 방향에서 못 찾으면 FF=1로 설정한다(62). 셀 루프를 닫고 VF_P3SRD2를 호출한다(64–70). 원문(연속 표시는 앞 문장에 이어짐): `                IF( IDR >= 2 .AND. IC > 0 ) THEN` (55); `                  FF(I,J,K) = FFA / DBLE(IC)` (56); `                  EXIT` (57); `                ENDIF` (58); `              ENDDO` (60); `              IF( IDR == 4 ) FF(I,J,K) = 1.D0` (62); `            ENDIF` (64); `          ENDDO` (66); `        ENDDO` (67); `      ENDDO` (68); `      CALL VF_P3SRD2(FF,DBUF,0)` (70); `      END` (72). 17–64행의 IF/ELSEIF에는 ELSE가 없다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24–29·55–58: IDR=2일 때 IC·FFA를 초기화하지 않는다. 따라서 두 번째 방향의 평균 검사는 첫 번째 방향 누계를 포함한다.
- 16·21–22: 주석 처리된 두 조건은 NF=-2 또는 NFP=-2에 한정되지만 실행 조건은 NF<0 또는 NFP<0이다.
