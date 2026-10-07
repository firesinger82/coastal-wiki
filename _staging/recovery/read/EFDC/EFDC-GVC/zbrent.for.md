---
file: models/EFDC/raw/source_code/EFDC-GVC/zbrent.for
lines: 92
sha256: 0d49bea6aa44ce1493fe0a1fba343009ed0bbf4a4af5ccff8bb42923829b591e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# zbrent.for — 판독 구간 기록

구간은 1행부터 92행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 구분 주석 뒤 `FUNCTION ZBRENT(ISMERR)` (6)으로 함수를 시작한다. 브렌트 방법(Brent's method)으로 RMIN..RMAX 사이의 SEDFLUX 근(root)을 TOL 정확도로 구한다는 주석과 Numerical Recipe p.253 문구를 포함한다(10–12). `EXTERNAL SEDFLUX` (16)으로 SEDFLUX를 외부 함수로 선언한다. `PARAMETER (IZMAX=100,EPS=3.0E-8,TOL=1.0E-5,` (18); `&             RMIN=1.0E-4,RMAX=100.0)` (19)는 최대 반복 100회, EPS=3.0E-8, TOL=1.0E-5, 고정 탐색 범위 1.0E-4..100.0을 지정한다. 주석·빈 줄을 포함한다. |
| 21–31 | 시작 시 6행 ZBRENT 함수 안. ISMERR을 0으로 초기화하고 A=RMIN, B=RMAX를 복사한다(21–23). `FA = SEDFLUX(A)` (24); `FB = SEDFLUX(B)` (25)로 양 끝의 SEDFLUX를 평가한다. `IF(FA*FB.GT.0.0)THEN` (26) 참 분기는 ISMERR=1을 설정한 뒤 반환한다(27–28). 조건 종료와 구분 주석 뒤 FC=FB를 복사한다(29–31). |
| 32–52 | 시작 시 6행 ZBRENT 함수 안. `DO II=1,IZMAX` (32)로 최대 IZMAX회 반복한다. `IF(FB*FC.GT.0.0)THEN` (33)일 때 C=A, FC=FA, E=D를 복사하고 `D = B-A` (36)로 구간 차를 둔다(34–38). `IF(ABS(FC).LT.ABS(FB))THEN` (39)일 때 `A = B` (40); `B = C` (41); `C = A` (42); `FA = FB` (43); `FB = FC` (44); `FC = FA` (45)를 이 순서대로 실행한다. 허용 오차(tolerance)와 구간 반폭은 `TOL1 = 2.0*EPS*ABS(B) + 0.5*TOL` (47); `XM = 0.5 * (C-B)` (48)이다. `IF(ABS(XM).LE.TOL1 .OR. FB.EQ.0.0)THEN` (49)일 때 ZBRENT=B를 설정하고 반환한다(50–51). 조건 종료를 포함한다(46·52). 반복은 다음 구간으로 이어진다. |
| 53–77 | 시작 시 6행 ZBRENT 함수·32행 II 루프 안. `IF(ABS(E).GE.TOL1 .AND. ABS(FA).GT.ABS(FB))THEN` (53) 참 분기는 `S = FB / FA` (54)로 함수값 비를 구한다. 내부 `IF(A.EQ.C)THEN` (55) 분기는 할선법(secant method) 식 `P = 2.0 * XM * S` (56); `Q = 1.0 - S` (57)을 사용한다. `ELSE` (58) 분기는 역이차 보간(inverse quadratic interpolation) 식 `Q = FA / FC` (59); `R = FB / FC` (60); `P = S * (2.0*XM*Q*(Q-R) - (B-A)*(R-1.0))` (61); `Q = (Q-1.0) * (R-1.0) * (S-1.0)` (62)을 사용한다. 내부 조건 종료 뒤 `IF(P.GT.0.0) Q = -Q` (64); `P = ABS(P)` (65)로 Q 부호와 P 절댓값을 정한다(63–65). `IF(2.0*P .LT. MIN(3.0*XM*Q-ABS(TOL1*Q), ABS(E*Q)))THEN` (66)이면 E=D 복사 뒤 `D = P / Q` (68)을 사용한다. `ELSE` (69) 분기는 D=XM, E=D로 이분법(bisection) 이동을 선택한다(70–71). 53행 조건의 `ELSE` (73) 분기도 D=XM, E=D를 사용한다(74–75). 조건 종료와 구분 주석을 포함한다(72·76–77). |
| 78–92 | 시작 시 6행 ZBRENT 함수·32행 II 루프 안. A=B, FA=FB를 복사한다(78–79). `IF(ABS(D).GT.TOL1)THEN` (80)이면 `B = B + D` (81)로 이동한다. `ELSE` (82) 분기는 `B = B + SIGN(TOL1,XM)` (83)으로 최소 허용 오차 크기의 이동을 적용한다. 조건 종료 후 `FB = SEDFLUX(B)` (85)로 새 함수값을 평가하고 II 루프를 닫는다(84–86). 반복을 모두 소진하면 ISMERR=2, ZBRENT=B를 설정한다(88–89). 구분 주석, RETURN, END를 포함한다(87·90–92). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–19: 최대 반복 수, EPS, TOL, RMIN, RMAX가 PARAMETER 상수로 고정되어 있다. 이 함수의 인수는 ISMERR 하나다(6).
- 26–28: FA*FB>0.0 분기는 ISMERR=1을 설정하고 반환한다. 이 반환 경로 앞에는 ZBRENT 함수값을 대입하는 문장이 없다.
- 31·33–37·47–49: FC의 초기값은 FB이다. C·D·E의 첫 대입은 FB*FC>0.0 참 분기 안에 있다. 이 조건 밖에서 XM 계산은 C를 참조한다. FB=0.0 검사는 XM 계산 뒤에 있다.
- 40–45: A=B, B=C, C=A와 FA=FB, FB=FC, FC=FA는 순차 대입이다. 이 교체 블록에는 원래 A·FA를 보관하는 임시 변수 대입이 없다.
