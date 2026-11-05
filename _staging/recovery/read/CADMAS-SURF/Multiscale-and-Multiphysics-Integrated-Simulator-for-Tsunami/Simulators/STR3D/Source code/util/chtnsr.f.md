---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/chtnsr.f
lines: 78
sha256: 486ea31a8ca327573b1f3cd616349fd3ec3fd7e6f48aa23377cb3cd082ed8923
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# chtnsr.f — 판독 구간 기록

구간은 1행부터 78행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | CHTNSR의 주석은 X·SIG·EPS에 TE·A·B를 곱하는 관계와 A·B의 역행렬·전치 관계를 제시한다(3–7). 해석: X는 좌표로, SIG와 EPS는 각각 응력과 변형률로 볼 수 있다. 암시적 형과 TE(3,3)·A(6,6)·B(6,6)를 선언한다(9–10). TE 열의 성분을 RL·RM·RN 계열로 복사한다(12–20). 원문: `      SUBROUTINE CHTNSR(TE,A,B)` (1); `C     {X'}=[TE]*{X}` (3); `C     {SIG'}=[A]*{SIG}   [A_INV]=[B_TRANS]` (5); `C     {EPS'}=[B]*{EPS}   [B_INV]=[A_TRANS]` (7); `      IMPLICIT REAL*8(A-H,O-Z)` (9); `      DIMENSION TE(3,3),A(6,6),B(6,6)` (10); `      RL1=TE(1,1)` (12); `      RL2=TE(2,1)` (13); `      RL3=TE(3,1)` (14); `      RM1=TE(1,2)` (15); `      RM2=TE(2,2)` (16); `      RM3=TE(3,2)` (17); `      RN1=TE(1,3)` (18); `      RN2=TE(2,3)` (19); `      RN3=TE(3,3)` (20). [11-04 전수 검증 정정] |
| 22–42 | 시작 시 1행 CHTNSR 루틴 안. A의 첫 세 행을 TE 성분의 제곱과 2배 곱으로 구성한다(22–41). 행 사이의 주석을 포함한다. 원문: `      A(1,1)=RL1*RL1` (22); `      A(1,2)=RM1*RM1` (23); `      A(1,3)=RN1*RN1` (24); `      A(1,4)=2.D0*RL1*RM1` (25); `      A(1,5)=2.D0*RM1*RN1` (26); `      A(1,6)=2.D0*RN1*RL1` (27); `      A(2,1)=RL2*RL2` (29); `      A(2,2)=RM2*RM2` (30); `      A(2,3)=RN2*RN2` (31); `      A(2,4)=2.D0*RL2*RM2` (32); `      A(2,5)=2.D0*RM2*RN2` (33); `      A(2,6)=2.D0*RN2*RL2` (34); `      A(3,1)=RL3*RL3` (36); `      A(3,2)=RM3*RM3` (37); `      A(3,3)=RN3*RN3` (38); `      A(3,4)=2.D0*RL3*RM3` (39); `      A(3,5)=2.D0*RM3*RN3` (40); `      A(3,6)=2.D0*RN3*RL3` (41). [11-04 전수 검증 정정] |
| 43–63 | 시작 시 1행 CHTNSR 루틴 안. A의 뒤 세 행을 서로 다른 TE 성분의 곱과 곱의 합으로 구성한다(43–62). 구분 주석을 포함한다. 원문: `      A(4,1)=RL1*RL2` (43); `      A(4,2)=RM1*RM2` (44); `      A(4,3)=RN1*RN2` (45); `      A(4,4)=RL1*RM2+RM1*RL2` (46); `      A(4,5)=RM1*RN2+RN1*RM2` (47); `      A(4,6)=RN1*RL2+RL1*RN2` (48); `      A(5,1)=RL2*RL3` (50); `      A(5,2)=RM2*RM3` (51); `      A(5,3)=RN2*RN3` (52); `      A(5,4)=RL2*RM3+RM2*RL3` (53); `      A(5,5)=RM2*RN3+RN2*RM3` (54); `      A(5,6)=RN2*RL3+RL2*RN3` (55); `      A(6,1)=RL3*RL1` (57); `      A(6,2)=RM3*RM1` (58); `      A(6,3)=RN3*RN1` (59); `      A(6,4)=RL3*RM1+RM3*RL1` (60); `      A(6,5)=RM3*RN1+RN3*RM1` (61); `      A(6,6)=RN3*RL1+RL3*RN1` (62). |
| 64–78 | 시작 시 1행 CHTNSR 루틴 안. I=1..6, J=1..6의 각 성분에서 FACT를 정한다(64–72). 뒤 세 행·앞 세 열이면 2, 앞 세 행·뒤 세 열이면 0.5, 나머지는 1이다. B(I,J)에 FACT*A(I,J)를 대입한다(73). 루프 종료·주석·RETURN·END를 포함한다. 원문: `      DO 100 I=1,6` (64); `        DO 200 J=1,6` (65); `          IF(I.GE.4.AND.J.LE.3) THEN` (66); `            FACT=2.D0` (67); `          ELSEIF(I.LE.3.AND.J.GE.4) THEN` (68); `            FACT=0.5D0` (69); `          ELSE` (70); `            FACT=1.D0` (71); `          ENDIF` (72); `          B(I,J)=FACT*A(I,J)` (73); `  200   CONTINUE` (74); `  100 CONTINUE` (75); `      RETURN` (77); `      END` (78). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
