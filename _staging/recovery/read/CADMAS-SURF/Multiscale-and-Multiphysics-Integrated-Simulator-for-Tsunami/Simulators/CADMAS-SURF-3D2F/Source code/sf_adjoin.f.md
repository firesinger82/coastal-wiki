---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_adjoin.f
lines: 79
sha256: 079052f8b5f5d4f8bd22f8d0b17d9d3ef013636d6fc26a2b203e83a9614c684f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_adjoin.f — 판독 구간 기록

구간은 1행부터 79행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 암시적 배정밀도(double precision)와 -1:1 작업 배열, 크기 7의 출력 인덱스 배열을 선언한다. DX·DY·DZ의 -1 성분은 각각 `G(1) - X1` (8), `G(2) - Y1` (11), `G(3) - Z1` (14)로 설정한다. +1 성분은 각각 `X2 - G(1)` (10), `Y2 - G(2)` (13), `Z2 - G(3)` (16)으로 설정한다. 0 성분은 0으로 설정한다. 해석: X1·X2 등의 쌍을 경계 좌표로 보면 각 값은 G와 경계 사이의 부호 있는 차이다. 원문: `      SUBROUTINE SF_ADJOIN(IP,JP,KP,G,X1,X2,Y1,Y2,Z1,Z2)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION DX(-1:1),DY(-1:1),DZ(-1:1),DIST(-1:1,-1:1,-1:1)` (5); `     &         ,ISKIP(-1:1,-1:1,-1:1),IP(7),JP(7),KP(7),G(3)` (6); `      DX(-1) = G(1) - X1` (8); `      DX( 0) = 0.` (9); `      DX( 1) = X2 - G(1)` (10); `      DY(-1) = G(2) - Y1` (11); `      DY( 0) = 0.` (12); `      DY( 1) = Y2 - G(2)` (13); `      DZ(-1) = G(3) - Z1` (14); `      DZ( 0) = 0.` (15); `      DZ( 1) = Z2 - G(3)` (16) [11-04 전수 검증 정정] |
| 18–49 | 시작 시 1행 SF_ADJOIN 루틴 안이다. DX·DY·DZ 각각의 -1 성분이 +1 성분보다 작으면 해당 첨자 범위를 -1:0으로 설정한다. 같거나 크면 해당 첨자 범위를 0:1로 설정한다. 이 비교는 절댓값 비교가 아니다. 세 중첩 루프에서 유클리드 거리(Euclidean distance)를 계산한다. 조건과 거리식을 모두 보존한다. 원문: `      IF( DX(-1) < DX(1) ) THEN` (18); `        IS = -1` (19); `        IE = 0` (20); `      ELSE` (21); `        IS = 0` (22); `        IE = 1` (23); `      ENDIF` (24); `      IF( DY(-1) < DY(1) ) THEN` (26); `        JS = -1` (27); `        JE = 0` (28); `      ELSE` (29); `        JS = 0` (30); `        JE = 1` (31); `      ENDIF` (32); `      IF( DZ(-1) < DZ(1) ) THEN` (34); `        KS = -1` (35); `        KE = 0` (36); `      ELSE` (37); `        KS = 0` (38); `        KE = 1` (39); `      ENDIF` (40); `      DO I = IS, IE` (42); `        DO J = JS, JE` (43); `          DO K = KS, KE` (44); `            DIST(I,J,K) = DSQRT(DX(I)*DX(I) + DY(J)*DY(J) + DZ(K)*DZ(K))` (45); `          ENDDO` (46); `        ENDDO` (47); `      ENDDO` (48) [11-04 전수 검증 정정] |
| 50–79 | 시작 시 1행 SF_ADJOIN 루틴 안이다. 중앙점을 ISKIP으로 제외한 뒤 1부터 7까지 반복한다. 각 반복에서 DIST_MIN=1.D20으로 두고 세 중첩 루프로 미선택 최솟값을 찾는다. IP·JP·KP로 선택 방향을 반환하고 선택점을 제외한다. 원문: `      ISKIP(:,:,:) = 0` (50); `      ISKIP(0,0,0) = 1` (52); `      DO IR = 1, 7` (54); `        DIST_MIN = 1.D20` (56); `        DO I = IS, IE` (58); `          DO J = JS, JE` (59); `            DO K = KS, KE` (60); `              IF( ISKIP(I,J,K) == 1 ) CYCLE` (61); `              IF( DIST(I,J,K) < DIST_MIN ) THEN` (62); `                DIST_MIN = DIST(I,J,K)` (63); `                I0 = I` (64); `                J0 = J` (65); `                K0 = K` (66); `              ENDIF` (67); `            ENDDO` (68); `          ENDDO` (69); `        ENDDO` (70); `        IP(IR) = I0` (72); `        JP(IR) = J0` (73); `        KP(IR) = K0` (74); `        ISKIP(I0,J0,K0) = 1` (75); `      ENDDO` (77); `      END` (79) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 56·62–75: 최솟값 탐색은 DIST_MIN=1.D20보다 작은 거리에서만 I0·J0·K0를 설정한다. 이 루틴에는 경계 거리 크기·부호·유한성 검사문이 없다.
