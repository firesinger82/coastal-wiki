---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/rhsidxf.f
lines: 45
sha256: 670b9d2a56837d02a28195620d02dad636b2ce9f80003dade673269865666a51
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# rhsidxf.f — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | RHSIDXF는 전진 소거(forward elimination)를 위한 우변 열 주소를 구성한다. 원래 첫 행 열을 SHIFT0으로 복사하고 첫 두 IROW_R2 주소를 설정한다(7–10). 인수·배열 선언과 주석을 포함한다. 원문: 연속문(1–2): `      SUBROUTINE RHSIDXF(NROW,IROW_L,ICOL_L,IROW_R,ICOL_R,IROW_R2` (1); `     &                  ,ICOL_R2,NSIZ_R2)` (2). 연속문(4–5): `      DIMENSION IROW_R(NROW+1),ICOL_R(*),IROW_R2(NROW+1),ICOL_R2(*)` (4); `     &         ,IROW_L(NROW+1),ICOL_L(*)` (5). `      IROW_R2(1)=1` (7). `      N=IROW_R(2)-1` (8). `      CALL SHIFT0(ICOL_R2,ICOL_R,N)` (9). `      IROW_R2(2)=IROW_R2(1)+N` (10). |
| 12–37 | 시작 시 1–2행 RHSIDXF 루틴 안. I=2..NROW에서 원래 행의 우변 열을 복사한다(12–18). 좌변 열을 앞에서부터 훑어 대각 J=I에서 멈춘다(20–26). 이전 J행의 우변 열을 ORDER2로 현재 열 목록에 삽입한다(27–36). 원문: `      DO 100 I=2,NROW` (12). `        IS=IROW_R(I)` (14). `        IE=IROW_R(I+1)-1` (15). `        N=IE-IS+1` (16). `        IP0=IROW_R2(I)` (17). `        CALL SHIFT0(ICOL_R2(IP0),ICOL_R(IS),N)` (18). `        IS=IROW_L(I)` (20). `        IE=IROW_L(I+1)-1` (21). `        DO 110 IP=IS,IE` (23). `          J=ICOL_L(IP)` (25). `          IF( J .EQ. I ) EXIT` (26). `          JS=IROW_R2(J)` (27). `          JE=IROW_R2(J+1)-1` (28). `          KS=1` (29). `          DO 111 K=JS,JE` (31). `            IC=ICOL_R2(K)` (32). `            CALL ORDER2(N,KS,ICOL_R2(IP0),IC)` (33). `  111     CONTINUE` (34). `  110   CONTINUE` (36). ORDER2는 같은 열 번호가 이미 있으면 N을 늘리지 않는다. 이 설명의 근거는 동일 Source code의 `util/order2.f:5–22`이다. SHIFT0 복사의 근거는 `util/shift0.f:15–17`이다. [11-04 전수 검증 보완] |
| 38–45 | 시작 시 1–2행 RHSIDXF 루틴·12행 `DO 100 I=2,NROW` 안이며 23행 IP 루프 밖. I 루프는 40행 `100 CONTINUE`에서 닫힌다. 다음 행 주소를 갱신하고 I 루프를 닫는다(38–40). NSIZ_R2를 마지막 주소에서 1을 뺀 값으로 정한 뒤 반환한다(42–45). 원문: `        IROW_R2(I+1)=IROW_R2(I)+N` (38). `  100 CONTINUE` (40). `      NSIZ_R2=IROW_R2(NROW+1)-1` (42). `      RETURN` (44). `      END` (45). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–10: 첫 행의 항 수는 IROW_R(2)-1로 계산하며 IROW_R(1)을 식에 쓰지 않는다.
