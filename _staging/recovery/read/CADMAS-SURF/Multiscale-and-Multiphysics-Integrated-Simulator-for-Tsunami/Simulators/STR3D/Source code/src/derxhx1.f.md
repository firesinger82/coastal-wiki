---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/derxhx1.f
lines: 42
sha256: 8432ebd9713cce253785d4ea683118875783d0e74549c91aab6bc2ff59c26b92
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# derxhx1.f — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | DERXHX1의 입출력과 배열을 선언한다. `節点座標`는 절점좌표(nodal coordinate)다. 주석은 DNDX의 네 평가 위치와 첫 평가 위치의 야코비안(Jacobian) 행렬식 DETG를 설명한다. 원문: `      SUBROUTINE DERXHX1(DNDX,DETG,XG1,XG2,XG3,X,ITO)` (1); 주석 원문 `!     DNDX : OUT : DNDX(i,j,1) = ∂Nj/∂xi at (XG1,XG2,XG3)` (3); 주석 원문 `!                  DNDX(i,j,2) = ∂Nj/∂xi at (0,0,XG3)` (4); 주석 원문 `!                  DNDX(i,j,3) = ∂Nj/∂xi at (XG1,0,0)` (5); 주석 원문 `!                  DNDX(i,j,4) = ∂Nj/∂xi at (0,XG2,0)` (6); 주석 원문 `!     DETG : OUT : \|J\| ( Jij = ∂xj/∂ξi ) at (XG1,XG2,XG3)` (7); 주석 원문 `!     XGi  : IN  : ξi` (8); 주석 원문 `!     X    : IN  : 節点座標` (9); `      IMPLICIT REAL*8(A-H,O-Z)` (11); `      DIMENSION DNDX(3,8,4),X(3,8),XG(3),P(3,8),XJI(3,3)` (12). |
| 14–34 | 시작 시 1행 DERXHX1 루틴 안. I=1..4 루프의 SELECT CASE에서 입력 좌표 (XG1,XG2,XG3), (0,0,XG3), (XG1,0,0), (0,XG2,0)을 차례로 XG에 넣는다. 이 SELECT에는 CASE DEFAULT가 없다. 원문: `      DO I = 1, 4` (14); `        SELECT CASE( I )` (16); `        CASE( 1 )` (17); `          XG(1) = XG1` (18); `          XG(2) = XG2` (19); `          XG(3) = XG3` (20); `        CASE( 2 )` (21); `          XG(1) = 0.` (22); `          XG(2) = 0.` (23); `          XG(3) = XG3` (24); `        CASE( 3 )` (25); `          XG(1) = XG1` (26); `          XG(2) = 0.` (27); `          XG(3) = 0.` (28); `        CASE( 4 )` (29); `          XG(1) = 0.` (30); `          XG(2) = XG2` (31); `          XG(3) = 0.` (32); `        END SELECT` (33). [11-04 전수 검증 정정] [11-04 전수 검증 보완] |
| 35–42 | 시작 시 14행 `      DO I = 1, 4` 안이다. 이 루프는 40행 `      ENDDO      `에서 닫힌다. DERHX2를 8절점으로 호출하고 JACOB3로 변환 정보를 구한다. I=1에서만 DET를 DETG에 복사한다. AXB로 각 위치의 공간 미분을 계산한다. 루프와 루틴 끝을 포함한다. 원문: `        CALL DERHX2(XG(1),XG(2),XG(3),8,P)` (35); `        CALL JACOB3(8,P,X,XJI,DET,ITO)` (36); `        IF( I == 1 ) DETG = DET` (37); `        CALL AXB(DNDX(1,1,I),XJI,P,3,3,8)` (38); `      ENDDO      ` (40); `      END` (42). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12·14·35–38: 절점 수 8과 평가 위치 수 4가 배열 크기·루프·호출 인수에 고정되어 있다.
