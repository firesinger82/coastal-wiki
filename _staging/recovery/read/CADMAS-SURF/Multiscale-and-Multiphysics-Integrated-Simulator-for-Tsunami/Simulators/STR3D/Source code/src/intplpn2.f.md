---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/intplpn2.f
lines: 47
sha256: 5dafba2d3a93204efb4f36e7a7388b6f100d84ab6c4bfeb42febd66a438acb86
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# intplpn2.f — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | INTPLPN2의 배열 선언과 계수 준비 구간이다. XD의 마지막 첨자 1·2·3 위치를 계산한다. A·RA·B·RB를 계산한다. 해석: 세 축 방향 위치와 삼각형 방향 외삽(extrapolation)을 위한 계수이다. 원문: `      SUBROUTINE INTPLPN2(XN,XG)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； `      DIMENSION XG(6,7,3),XD(6,7,3),XN(6,15)` (4)； `      R = DSQRT(5.D0/3.D0)` (6)； `      XD(:,:,1) = R * XG(:,:,1) + ( 1.D0 - R ) * XG(:,:,2)` (8)； `      XD(:,:,2) = XG(:,:,2)` (9)； `      XD(:,:,3) = R * XG(:,:,3) + ( 1.D0 - R ) * XG(:,:,2)` (10)； `      A = ( 9.D0 + 2.D0 * DSQRT(15.D0) ) / 21.D0` (12)； `      RA = 2.D0/3.D0 / ( A - 1.D0/3.D0 )` (13)； `      B = ( 9.D0 - 2.D0 * DSQRT(15.D0) ) / 21.D0` (14)； `      RB = 1.D0/3.D0 / ( 1.D0/3.D0 - B )` (15)。 [11-04 전수 검증 정정] |
| 17–47 | 시작 시 1행 INTPLPN2 루틴 안이다. 첫 SELECT CASE는 J=1·2·3에 대해 I0를 각각 0·9·3으로 정한다. I=1..3에서 XN의 I0+I열을 계산한다. 따라서 열 범위는 각각 1:3·10:12·4:6이다. 두 번째 SELECT CASE는 J=2이면 CYCLE로 J 루프의 다음 반복으로 이동한다. J=1·3이면 I0를 각각 3·9로 정한다. I=4..6에서 XN의 7:9·13:15열을 각각 계산한다. 해석: 두 번째 계산은 두 끝면에 대응한다. 원문: `      DO J = 1, 3` (17)； `        SELECT CASE(J)` (19)； `        CASE(1)` (20)； `          I0 = 0` (21)； `        CASE(2)` (22)； `          I0 = 9` (23)； `        CASE(3)` (24)； `          I0 = 3` (25)； `        END SELECT` (26)； `        DO I = 1, 3` (28)； `          XN(:,I0+I) = RA * XD(:,I,J) + ( 1.D0 - RA ) * XD(:,7,J)` (29)； `        ENDDO` (30)； `        SELECT CASE(J)` (32)； `        CASE(1)` (33)； `          I0 = 3` (34)； `        CASE(2)` (35)； `          CYCLE` (36)； `        CASE(3)` (37)； `          I0 = 9` (38)； `        END SELECT` (39)； `        DO I = 4, 6` (41)； `          XN(:,I0+I) = RB * XD(:,I,J) + ( 1.D0 - RB ) * XD(:,7,J)` (42)； `        ENDDO` (43)； `      ENDDO` (45)； `      END` (47)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32–42: J=2이면 36행 CYCLE로 41–43행의 두 번째 I 루프를 건너뛴다. [11-04 전수 검증 정정]
