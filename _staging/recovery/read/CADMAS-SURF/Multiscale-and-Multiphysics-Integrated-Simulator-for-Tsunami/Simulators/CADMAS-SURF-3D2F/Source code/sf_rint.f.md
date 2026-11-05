---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_rint.f
lines: 11
sha256: 4b26c5f6f382db21fcc867daded552f049c6b208bc85dbef30a502e7f2b4c843
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_rint.f — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | SF_RINT는 두 점의 I 성분을 독립 좌표로 사용하여 X 위치의 J 성분을 선형 보간(linear interpolation)한다(8–9). X1·X2는 마지막 차원 크기를 *로 표시한 assumed-size 배열이다(5). 분모는 X2(I)-X1(I)이다. 원문(연속 표시는 앞 문장에 이어짐): `      FUNCTION SF_RINT(X1,X2,I,J,X)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION X1(*), X2(*)` (5); `      SF_RINT = ( ( X2(I) - X ) * X1(J) + ( X - X1(I) ) * X2(J) )` (8); `     &       / ( X2(I) - X1(I) )` (9); `      END` (11). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–9: 분모가 0인지 검사하는 조건문과 X 범위 제한은 이 함수에 없다.
