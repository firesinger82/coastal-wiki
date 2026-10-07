---
file: models/EFDC/raw/source_code/EFDC-GVC/ludcmp.for
lines: 79
sha256: a07fe267d8d5a214eb7fbcbfabce006f08c4bdbdee33571a07cd5e63c05fed9c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# ludcmp.for — 판독 구간 기록

구간은 1행부터 79행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 구분 주석과 `SUBROUTINE LUDCMP(A,N,NP,INDX,D)` 입구(1–6). EFDC-FULL 1.0a와 2001년 11월 1일 수정 기록 및 변경 이력 머리말(7–20). LU 분해(LU decomposition)의 작업 상수는 `PARAMETER (NMAX=100,TINY=1.0E-20)` (21). A는 NP×NP, INDX는 N, 행 스케일(row scaling) VV는 NMAX 크기로 선언한다(22). |
| 23–31 | 시작 시 6행 LUDCMP 안. 부호 D의 초기값은 `D=1.` (23). I=1..N 및 J=1..N 루프(24·26)에서 행의 최대 절댓값을 찾는다. 조건과 대입은 `IF(ABS(A(I,J)).GT.AAMAX) AAMAX=ABS(A(I,J))` (27). `IF(AAMAX.EQ.0.) PAUSE 'SINGULAR MATRIX.'` (29)로 영행에서 PAUSE를 실행한다. 행 스케일은 `VV(I)=1./AAMAX` (30). 두 루프의 종료문도 이 구간에 포함된다(28·31). |
| 32–43 | 시작 시 6행 LUDCMP 안. J=1..N 열 루프를 연다(32). `IF(J.GT.1)THEN` (33) 안에서 I=1..J−1을 순회한다(34). SUM에 A(I,J)를 복사한다(35). `IF(I.GT.1)THEN` (36) 안에서 K=1..I−1 루프(37)의 `SUM=SUM-A(I,K)*A(K,J)` (38)로 상삼각(upper triangular) 성분을 계산한다. A(I,J)에 SUM을 복사하고 내부 조건과 I 루프를 닫는다(39–43). |
| 44–58 | 시작 시 6행 LUDCMP·32행 J 루프 안. AAMAX를 0으로 초기화하고 I=J..N을 순회한다(44–45). SUM에 A(I,J)를 복사한다(46). `IF(J.GT.1)THEN` (47) 안에서 K=1..J−1 루프(48)의 `SUM=SUM-A(I,K)*A(K,J)` (49)를 누적하여 A(I,J)에 복사한다(51). 조건 밖에서 `DUM=VV(I)*ABS(SUM)` (53)을 계산한다. `IF(DUM.GE.AAMAX)THEN` (54)이면 IMAX와 AAMAX를 현재 I와 DUM으로 바꾼다(55–56). I 루프를 닫는다(58). |
| 59–79 | 시작 시 6행 LUDCMP·32행 J 루프 안. `IF(J.NE.IMAX)THEN` (59)이면 K=1..N에서 두 행을 교환한다(60–64). 같은 분기에서 `D=-D` (65)로 부호를 뒤집고 VV(IMAX)에 VV(J)를 복사한다(66). INDX(J)에 IMAX를 저장한다(68). `IF(J.NE.N)THEN` (69) 안에서 `IF(A(J,J).EQ.0.)A(J,J)=TINY` (70), `DUM=1./A(J,J)` (71)를 실행한다. I=J+1..N 루프(72)의 `A(I,J)=A(I,J)*DUM` (73)로 하삼각(lower triangular) 성분을 정규화(normalization)한다. J 루프 종료(76) 뒤 `IF(A(N,N).EQ.0.)A(N,N)=TINY` (77)를 실행하고 RETURN·END로 끝낸다(78–79). 외부 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 21–24·30: VV의 크기는 NMAX=100으로 고정된다. VV(I) 접근 전 N<=NMAX를 검사하는 문장은 이 파일에 없다.
- 29–30: AAMAX=0일 때 PAUSE를 실행한다. 바로 다음 문장은 VV(I)=1./AAMAX이며, 이 사이에 RETURN이나 AAMAX를 바꾸는 문장은 없다.
- 70·77: 대각 성분이 정확히 0일 때 TINY=1.0E-20으로 바꾼다. 마지막 대각 성분 검사는 J 루프 밖에 별도로 있다.
