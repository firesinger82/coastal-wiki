---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/ichsky.f
lines: 49
sha256: a73d809e30d52b862f67c5cfcc930d98f12760629630feda6f307f8dbffa8c15
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ichsky.f — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | ICHSKY의 배열 선언과 IROW 반복이다. IS=IDSK(IROW)+1부터 IE=IDSK(IROW+1)-1까지 순회한다. 해석: 비대각 구간을 사용하는 행별 불완전 분해(incomplete factorization) 계산이다. ICOL == 1이면 다음 I로 이동한다. 공통 열을 탐색하여 RLOW에서 곱을 뺀다. 열 순서 비교에 따라 탐색 시작 위치를 바꾸고 GOTO로 반복을 제어한다. 원문: `      SUBROUTINE ICHSKY(D,A,RLOW,NEQ,IDSK,IDCG,ITO)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； `      DIMENSION IDSK(NEQ+1),IDCG(*),RLOW(*),A(*),D(NEQ)` (4)； `      DO 1000 IROW=1,NEQ` (6)； `        IS=IDSK(IROW)+1` (7)； `        IE=IDSK(IROW+1)-1` (8)； `        DO 1100 I=IS,IE` (11)； `          ICOL=IDCG(I)` (12)； `          RLOW(I)=A(I)` (13)； `          IF(ICOL.EQ.1) GOTO 1100` (14)； `          ISS0=IS` (16)； `          DO 1500 K=IDSK(ICOL)+1,IDSK(ICOL+1)-1` (17)； `            KCOL=IDCG(K)` (18)； `            ISS=ISS0` (19)； `            DO 1600 KK=ISS,IE` (20)； `              IF(IDCG(KK).EQ.KCOL) THEN` (21)； `                RLOW(I)=RLOW(I)-RLOW(K)*RLOW(KK)*D(KCOL)` (22)； `                ISS0=KK+1` (23)； `                GOTO 1500` (24)； `              ELSEIF(IDCG(KK).LT.KCOL) THEN` (25)； `                GOTO 1600` (26)； `              ELSE` (27)； `                ISS0=KK` (28)； `                GOTO 1500` (29)； `              ENDIF` (30)； ` 1600       CONTINUE` (31)； ` 1500     CONTINUE` (32)； ` 1100   CONTINUE` (34)。 [11-04 전수 검증 정정] |
| 36–49 | 시작 시 1행 ICHSKY 루틴과 6행 `DO 1000 IROW=1,NEQ` 안이다. 이 바깥 루프는 46행 `1000 CONTINUE`에서 닫힌다. 대각 위치 IP에 A를 복사하고 해당 행 비대각 성분들의 제곱·D 곱을 뺀다. 그 대각값의 역수를 D에 저장한 뒤 행 루프와 루틴을 끝낸다. 원문: `        IP=IDSK(IROW)` (37)； `        RLOW(IP)=A(IP)` (38)； `        DO 1200 K=IS,IE` (40)； `          KCOL=IDCG(K)` (41)； `          RLOW(IP)=RLOW(IP)-RLOW(K)*RLOW(K)*D(KCOL)` (42)； ` 1200   CONTINUE` (43)； `        D(IROW)=1.D0/RLOW(IP)` (45)； ` 1000 CONTINUE` (46)； `      RETURN` (48)； `      END` (49)。 [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 45: D(IROW)=1.D0/RLOW(IP) 앞에 RLOW(IP)의 부호 또는 0 여부를 검사하는 조건이 없다.
- 1·49: ITO는 인수이지만 이 파일의 실행문에는 쓰이지 않는다.
