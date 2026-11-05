---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/intpl.f
lines: 27
sha256: a77bf3a514fbe9feba96843f3699548390aa2bed09047d888382a83ee720dfa5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# intpl.f — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | INTPL의 인수와 암시적 형, X0(N)·Y0(N)·TBL(2,N)을 선언한다(1–4). I=1..N 루프에서 TBL의 두 행을 X0와 Y0에 복사한다(6–9). 구분 주석을 포함한다. 원문: `      SUBROUTINE INTPL(Y,X,TBL,N)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION X0(N),Y0(N),TBL(2,N)` (4); `      DO 200 I=1,N` (6); `        X0(I)=TBL(1,I)` (7); `        Y0(I)=TBL(2,I)` (8); `  200 CONTINUE` (9). |
| 11–22 | 시작 시 1행 INTPL 루틴 안. I=2..N-1을 순회하며 X<=X0(I)인 첫 위치에서 값을 정하고 반환한다(11–21). X가 X0(I)와 같고 다음 X0도 같으면 Y0(I)·Y0(I+1)의 평균을 사용한다(13–14). 그 외 I-1과 I 사이의 선형 보간(linear interpolation) 기울기 A와 Y를 계산한다(15–18). 루프 종료와 주석을 포함한다. 원문: `      DO 100 I=2,N-1` (11); `        IF( X .LE. X0(I) ) THEN` (12); `          IF( X .EQ. X0(I) .AND. X0(I) .EQ. X0(I+1) ) THEN` (13); `            Y = .5*( Y0(I) + Y0(I+1) )` (14); `          ELSE` (15); `            A = ( Y0(I) - Y0(I-1) ) / ( X0(I) - X0(I-1) )` (16); `            Y = A*( X - X0(I-1) ) + Y0(I-1)` (17); `          ENDIF` (18); `          RETURN` (19); `        ENDIF` (20); `  100 CONTINUE` (21). |
| 23–27 | 시작 시 1행 INTPL 루틴 안. 앞 루프에서 반환하지 않았으면 마지막 두 점으로 A와 Y를 계산한다(23–24). X에 대한 추가 조건 없이 계산한다. 주석·RETURN·END를 포함한다. 원문: `      A = ( Y0(N) - Y0(N-1) ) / ( X0(N) - X0(N-1) )` (23); `      Y = A*( X - X0(N-1) ) + Y0(N-1)` (24); `      RETURN` (26); `      END` (27). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–24: X를 표의 양 끝 값으로 제한하는 문장은 없다. 12행 `IF( X .LE. X0(I) ) THEN`에서 13행 `IF( X .EQ. X0(I) .AND. X0(I) .EQ. X0(I+1) ) THEN`까지 참이면 14행 `Y = .5*( Y0(I) + Y0(I+1) )`로 평균을 사용한다. 그 외에는 첫 해당 구간 또는 마지막 두 점의 선형식을 사용한다. [11-04 전수 검증 정정]
- 16·23: X0의 차이를 분모로 사용한다. 이 두 대입문 앞에는 해당 분모가 0인지 검사하는 문장이 없다.
