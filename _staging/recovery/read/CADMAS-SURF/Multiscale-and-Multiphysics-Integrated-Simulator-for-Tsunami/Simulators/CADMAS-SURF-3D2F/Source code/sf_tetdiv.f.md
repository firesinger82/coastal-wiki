---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_tetdiv.f
lines: 45
sha256: 8b14a6e8d3e06472ce39f4d98bead63251d05b45a197aad45630dc066b574227
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_tetdiv.f — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | 해석: 이름과 배열 형태로 볼 때 사면체 분할 루틴이다. 인수와 배열을 선언한다(1–5). 7–30행 `SELECT CASE( N )`에는 CASE DEFAULT가 없다. SELECT CASE(N)은 4·10절점에 NT=1, 6·15절점에 NT=11과 SF_MKTEPN·SF_GSFPN, 8·20절점에 NT=24와 SF_MKTEHX·SF_GSFHX를 선택한다(7–30). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      SUBROUTINE SF_TETDIV(NT,P,N,NP,XX)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      DIMENSION P(3,4,24),NP(N),XX(3,*),IP(4,24),XG(3,6)` (5)<br>`!-----------------------------------------------------------------------` (6)<br>`      SELECT CASE( N )` (7)<br>`      CASE( 4, 10 )` (8)<br>`        NT = 1` (10)<br>`        IP(:,1) = NP(1:4)` (12)<br>`      CASE( 6, 15 )` (14)<br>`        NT = 11` (16)<br>`        CALL SF_MKTEPN(IP,NP)` (18)<br>`        CALL SF_GSFPN(XG,XX,NP)` (20)<br>`      CASE( 8, 20 )` (22)<br>`        NT = 24` (24)<br>`        CALL SF_MKTEHX(IP,NP)` (26)<br>`        CALL SF_GSFHX(XG,XX,NP)` (28)<br>`      END SELECT` (30) [11-04 전수 검증 보완] |
| 31–45 | 시작 시 1행 루틴 안. 각 사면체의 네 점을 순회한다. IG>0이면 원 좌표, IG<0이면 생성 좌표를 복사한다. IG=0 경로는 VF_A2ERR를 호출한다(32–43). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      DO I = 1, NT` (32)<br>`        DO J = 1, 4` (33)<br>`          IG = IP(J,I)` (34)<br>`          IF( IG > 0 ) THEN` (35)<br>`            P(:,J,I) = XX(:,IG)` (36)<br>`          ELSEIF( IG < 0 ) THEN` (37)<br>`            P(:,J,I) = XG(:,-IG)` (38)<br>`          ELSE` (39)<br>`            CALL VF_A2ERR('SF_TETDIV','P.G ERROR.')` (40)<br>`          ENDIF` (41)<br>`        ENDDO` (42)<br>`      ENDDO` (43)<br>`      END` (45) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–30: SELECT CASE(N)에 CASE DEFAULT는 없다.
