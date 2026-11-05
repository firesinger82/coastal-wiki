---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/intplpn1.f
lines: 20
sha256: 1a80e9b2aa38568312fb83ef4b04538ef7161914c0ab7c5aa0a9d5ee94a60709
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# intplpn1.f — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | INTPLPN1은 6×6 입력 XG를 XN으로 변환한다. R을 계산한다. I=1..3에서 XG의 I열과 I+3열을 조합하여 XD의 두 열을 계산한다. XD의 1:3열과 4:6열을 각각 조합하여 XN의 여섯 열을 계산한다. 해석: 축 방향 외삽(extrapolation) 뒤 위아래 면의 절점 값을 계산한다. 원문: `      SUBROUTINE INTPLPN1(XN,XG)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； `      DIMENSION XG(6,6),XD(6,6),XN(6,6)` (4)； `      R = .5D0 * ( DSQRT(3.D0) - 1.D0 )` (6)； `      DO I = 1, 3` (8)； `        XD(:,I)   = ( 1.D0 + R ) * XG(:,I)   - R * XG(:,I+3)` (9)； `        XD(:,I+3) = ( 1.D0 + R ) * XG(:,I+3) - R * XG(:,I)` (10)； `      ENDDO` (11)； `      XN(:,1) = XD(:,3) + XD(:,1) - XD(:,2)` (13)； `      XN(:,2) = XD(:,1) + XD(:,2) - XD(:,3)` (14)； `      XN(:,3) = XD(:,2) + XD(:,3) - XD(:,1)` (15)； `      XN(:,4) = XD(:,6) + XD(:,4) - XD(:,5)` (16)； `      XN(:,5) = XD(:,4) + XD(:,5) - XD(:,6)` (17)； `      XN(:,6) = XD(:,5) + XD(:,6) - XD(:,4)` (18)； `      END` (20)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4·8–18: XG·XD·XN의 두 차원 크기는 모두 6이다. 해석: XN은 여섯 절점의 여섯 성분을 저장한다. [11-04 전수 검증 정정]
