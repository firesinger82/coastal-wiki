---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_elem_range.f
lines: 105
sha256: 5288c880f92007205abb4415eb92aa61822329d802231865b17adf1802a990d2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_elem_range.f — 판독 구간 기록

구간은 1행부터 105행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | SF_ELEM_RANGE 선언, INCLUDE 세 개와 배열 범위(1–11). XMIN=1.D20·XMAX=-1.D20에서 요소의 N개 절점(node) 좌표 최솟값·최댓값을 구한다(13–21). x방향 시작 셀 IS를 순방향으로 찾고 찾지 못하면 ISKIP=1로 반환한다(23–33). 원문: 연속문: `      SUBROUTINE SF_ELEM_RANGE(ISKIP,IS,IE,JS,JE,KS,KE,XX,YY,ZZ,EPS,N,NP` (1); `     &                        ,GRID)` (2)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (4)<br>`      INCLUDE 'VF_A0PRM.h'` (6)<br>`      INCLUDE 'VF_ANUMBI.h'` (7)<br>`      INCLUDE 'VF_APARAI.h'` (8)<br>연속문: `      DIMENSION XX(MAXG1,NUMI),YY(MAXG1,NUMJ),ZZ(MAXG1,NUMK),NP(N)` (10); `     &         ,GRID(3,*),XMIN(3),XMAX(3)` (11)<br>`      XMIN(:) =  1.D20` (13)<br>`      XMAX(:) = -1.D20` (14)<br>`      DO I = 1, N` (16)<br>`        DO J = 1, 3` (17)<br>`          XMIN(J) = DMIN1( XMIN(J), GRID(J,NP(I)) )` (18)<br>`          XMAX(J) = DMAX1( XMAX(J), GRID(J,NP(I)) )` (19)<br>`        ENDDO` (20)<br>`      ENDDO` (21)<br>`      ISKIP = 1` (23)<br>`      DO I = MYIS + 1, MYIE + 1` (25)<br>`        IF( XX(1,I) - EPS  >= XMIN(1) ) THEN` (26)<br>`          IS = I - 1` (27)<br>`          ISKIP = 0` (28)<br>`          EXIT` (29)<br>`        ENDIF` (30)<br>`      ENDDO` (31)<br>`      IF( ISKIP == 1 ) RETURN` (33) |
| 35–82 | 시작 시 1행 SF_ELEM_RANGE 루틴 안. MYMIE에 따라 끝 면 포함 여부 IP를 정하고 역방향으로 IE를 찾는다(35–51). y방향 시작 JS를 순방향으로 찾는다(53–63). MYMJE에 따라 JP를 정하고 JE를 역방향으로 찾는다(65–81). 각 탐색은 ISKIP를 다시 1로 설정하고 처음 맞는 위치에서 0으로 바꾸어 EXIT한다. 원문: `      IF( MYMIE == 1 ) THEN` (35)<br>`        IP = 1` (36)<br>`      ELSE` (37)<br>`        IP = 0` (38)<br>`      ENDIF` (39)<br>`      ISKIP = 1` (41)<br>`      DO I = MYIE + IP, MYIS, -1` (43)<br>`        IF( XX(1,I) - EPS < XMAX(1) ) THEN` (44)<br>`          IE = I` (45)<br>`          ISKIP = 0` (46)<br>`          EXIT` (47)<br>`        ENDIF` (48)<br>`      ENDDO` (49)<br>`      IF( ISKIP == 1 ) RETURN` (51)<br>`      ISKIP = 1` (53)<br>`      DO J = MYJS + 1, MYJE + 1` (55)<br>`        IF( YY(1,J) - EPS  >= XMIN(2) ) THEN` (56)<br>`          JS = J - 1` (57)<br>`          ISKIP = 0` (58)<br>`          EXIT` (59)<br>`        ENDIF` (60)<br>`      ENDDO` (61)<br>`      IF( ISKIP == 1 ) RETURN` (63)<br>`      IF( MYMJE == 1 ) THEN` (65)<br>`        JP = 1` (66)<br>`      ELSE` (67)<br>`        JP = 0` (68)<br>`      ENDIF` (69)<br>`      ISKIP = 1` (71)<br>`      DO J = MYJE + JP, MYJS, -1` (73)<br>`        IF( YY(1,J) - EPS < XMAX(2) ) THEN` (74)<br>`          JE = J` (75)<br>`          ISKIP = 0` (76)<br>`          EXIT` (77)<br>`        ENDIF` (78)<br>`      ENDDO` (79)<br>`      IF( ISKIP == 1 ) RETURN` (81) |
| 83–105 | 시작 시 1행 SF_ELEM_RANGE 루틴 안. K=3:NUMK를 순방향으로 순회하여 KS를 구하고 찾지 못하면 반환한다(83–93). K=NUMK:2를 역방향으로 순회하여 KE를 구한다(95–103). 각 조건은 좌표에서 EPS를 뺀 값과 XMIN(3)·XMAX(3)을 비교한다. 원문: `      ISKIP = 1` (83)<br>`      DO K = 3, NUMK` (85)<br>`        IF( ZZ(1,K) - EPS  >= XMIN(3) ) THEN` (86)<br>`          KS = K - 1` (87)<br>`          ISKIP = 0` (88)<br>`          EXIT` (89)<br>`        ENDIF` (90)<br>`      ENDDO` (91)<br>`      IF( ISKIP == 1 ) RETURN` (93)<br>`      ISKIP = 1` (95)<br>`      DO K = NUMK, 2, -1` (97)<br>`        IF( ZZ(1,K) - EPS < XMAX(3) ) THEN` (98)<br>`          KE = K` (99)<br>`          ISKIP = 0` (100)<br>`          EXIT` (101)<br>`        ENDIF` (102)<br>`      ENDDO` (103)<br>`      END` (105) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23–103: 각 범위 탐색은 실패 시 ISKIP=1을 유지한다. 실패한 축과 아직 탐색하지 않은 축의 출력 범위에는 별도 기본값을 대입하지 않는다.
