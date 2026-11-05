---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/vintpn1.f
lines: 20
sha256: 8e3cdbd91ea2c6385cf9b34e21688ee1acb3870cd5cb8e13186e1a32174a8040
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vintpn1.f — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | VINTPN1은 XG(3,3,2)로부터 XN(3,6)을 계산한다. 해석: 3×2개 적분점의 세 성분 값을 6개 절점으로 외삽(extrapolation)하는 용도로 보인다. 실수 IMPLICIT와 XG(3,3,2)·XD(3,6)·XN(3,6)를 선언한다. R=.5*(sqrt(3)-1)을 사용하여 XG의 세 번째 첨자 1·2를 결합한다. XD의 열 1–3과 4–6을 각각 계산한다. XN의 열 1–3은 XD의 열 1–3 중 두 개를 더하고 나머지 하나를 뺀 값이다. XN의 열 4–6은 XD의 열 4–6에 같은 방식을 적용한 값이다. 해석: 이 두 그룹은 양쪽 두께 위치의 삼각면에 해당하는 것으로 보인다. 모든 계수·첨자·계산식은 아래에 원문으로 적었다. 원문: `      SUBROUTINE VINTPN1(XN,XG)` (1); `C` (2); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION XG(3,3,2),XD(3,6),XN(3,6)` (4); `C-----------------------------------------------------------------------` (5); `      R = .5D0 * ( DSQRT(3.D0) - 1.D0 )` (6); `C` (7); `      DO I = 1, 3` (8); `        XD(:,I)   = ( 1.D0 + R ) * XG(:,I,1) - R * XG(:,I,2)` (9); `        XD(:,I+3) = ( 1.D0 + R ) * XG(:,I,2) - R * XG(:,I,1)` (10); `      ENDDO` (11); `C` (12); `      XN(:,1) = XD(:,3) + XD(:,1) - XD(:,2)` (13); `      XN(:,2) = XD(:,1) + XD(:,2) - XD(:,3)` (14); `      XN(:,3) = XD(:,2) + XD(:,3) - XD(:,1)` (15); `      XN(:,4) = XD(:,6) + XD(:,4) - XD(:,5)` (16); `      XN(:,5) = XD(:,4) + XD(:,5) - XD(:,6)` (17); `      XN(:,6) = XD(:,5) + XD(:,6) - XD(:,4)` (18); `C` (19); `      END` (20) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
