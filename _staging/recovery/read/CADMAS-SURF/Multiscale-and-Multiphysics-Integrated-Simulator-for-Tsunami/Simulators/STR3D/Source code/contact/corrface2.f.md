---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/corrface2.f
lines: 43
sha256: 2b4d26d001d53b95cbefb5efbb57ea669ade906a8b28876ed0d72a5cccf4e889
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# corrface2.f — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 루틴·암시적 자료형·배열 차원을 선언한다(1–4). 주석의 자유(free)·구속(constraint)·종속(slave) 성분을 IC 값 0·1·2로 각각 선택한다(7–19). 원문: `      SUBROUTINE CORRFACE2(DUG,IC,XYZ)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION IC(3),X(4),Y(4),Z(4),XYZ(3,4),DUG(3)` (4); 주석 원문: `C     IFR1 : FREE` (7); 주석 원문: `C     IFR2 : CONSTRAINT` (8); 주석 원문: `C     IFR3 : SLAVE` (9); `      DO 100 I=1,3` (11); `        IF( IC(I) .EQ. 0 ) THEN` (12); `          IFR1=I` (13); `        ELSEIF( IC(I) .EQ. 1 ) THEN` (14); `          IFR2=I` (15); `        ELSEIF( IC(I) .EQ. 2 ) THEN` (16); `          IFR3=I` (17). 12행 IF와 14·16행 ELSEIF 사슬에는 ELSE가 없다(18행 ENDIF). 11행 `DO 100 I=1,3`은 19행 `100 CONTINUE`에서 끝난다. [11-04 전수 검증 보완] |
| 21–43 | 시작 시 1행 CORRFACE2 루틴 안이다. 네 점의 좌표 성분을 재배열하고 두 행렬식 R로 A1·B1·A2·B2를 계산한다(21–33). A·B를 조합하여 DUG의 자유·종속 성분을 계산하고 구속 성분은 0으로 둔다(35–40). 루틴을 끝낸다(42–43). 원문: `      DO 200 I=1,4` (21); `        X(I)=XYZ(IFR1,I)` (22); `        Y(I)=XYZ(IFR2,I)` (23); `        Z(I)=XYZ(IFR3,I)` (24); `      R  = (X(1)-X(3))*(Y(2)-Y(3)) - (X(2)-X(3))*(Y(1)-Y(3))` (27); `      A1 = (Y(2)-Y(3))/R` (28); `      B1 = ( (X(4)-X(3))*(Y(2)-Y(3)) - (X(2)-X(3))*(Y(4)-Y(3)) ) / R` (29); `      R  = (X(2)-X(3))*(Y(1)-Y(3)) - (X(1)-X(3))*(Y(2)-Y(3))` (31); `      A2 = (Y(1)-Y(3))/R` (32); `      B2 = ( (X(4)-X(3))*(Y(1)-Y(3)) - (X(1)-X(3))*(Y(4)-Y(3)) ) / R` (33); `      A = (Z(1)-Z(3))*A1 + (Z(2)-Z(3))*A2` (35); `      B = (Z(1)-Z(3))*B1 + (Z(2)-Z(3))*B2 + (Z(3)-Z(4))` (36); `      DUG(IFR1) = -A*B/(A*A+1.)` (38); `      DUG(IFR2) = 0.` (39); `      DUG(IFR3) = B/(A*A+1.)` (40). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–19: IC 값 0·1·2의 존재 여부나 중복을 검사하는 별도 문장이 없다.
- 27–33: 두 R을 분모로 쓰기 전에 0 여부를 검사하지 않는다.
