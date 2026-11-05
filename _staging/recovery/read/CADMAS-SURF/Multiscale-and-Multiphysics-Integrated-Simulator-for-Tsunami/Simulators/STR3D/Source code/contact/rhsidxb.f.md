---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/rhsidxb.f
lines: 50
sha256: 0a03aa46274d6708edcf97b7a785d9bc4c53940d77b8c833dcedcf36d18f5601
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# rhsidxb.f — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | RHSIDXB는 후진 소거(backward elimination)를 위한 우변 열 주소를 행 역순으로 구성한다. 원래 마지막 행의 열을 SHIFT0으로 복사하고 첫 두 IROW_R3 주소를 설정한다(7–12). 배열 선언과 주석을 포함한다. 원문: 연속문(1–2): `      SUBROUTINE RHSIDXB(NROW,IROW_L,ICOL_L,IROW_R2,ICOL_R2,IROW_R3` (1); `     &                  ,ICOL_R3,NSIZ_R3)` (2). 연속문(4–5): `      DIMENSION IROW_R2(NROW+1),ICOL_R2(*),IROW_R3(NROW+1),ICOL_R3(*)` (4); `     &         ,IROW_L(NROW+1),ICOL_L(*)` (5). `      IROW_R3(1)=1` (7). `      IS=IROW_R2(NROW)` (8). `      IE=IROW_R2(NROW+1)-1` (9). `      N=IE-IS+1` (10). `      CALL SHIFT0(ICOL_R3,ICOL_R2(IS),N)` (11). `      IROW_R3(2)=IROW_R3(1)+N` (12). |
| 14–42 | 시작 시 1–2행 RHSIDXB 루틴 안. II=2..NROW에서 대응 원래 행 I를 역순으로 정하고 원래 우변 열을 복사한다(14–22). 좌변 열을 역순으로 훑으며 대각 J=I에서 멈춘다(24–30). 각 J행의 역순 주소 JJ에서 열을 읽어 ORDER2로 현재 열 목록에 삽입한다(31–41). 원문: `      DO 100 II=2,NROW` (14). `        I=NROW+1-II` (16). `        IS=IROW_R2(I)` (18). `        IE=IROW_R2(I+1)-1` (19). `        N=IE-IS+1` (20). `        IP0=IROW_R3(II)` (21). `        CALL SHIFT0(ICOL_R3(IP0),ICOL_R2(IS),N)` (22). `        IS=IROW_L(I)` (24). `        IE=IROW_L(I+1)-1` (25). `        DO 110 IP=IE,IS,-1` (27). `          J=ICOL_L(IP)` (29). `          IF( J .EQ. I ) EXIT` (30). `          JJ=NROW+1-J` (31). `          JS=IROW_R3(JJ)` (32). `          JE=IROW_R3(JJ+1)-1` (33). `          KS=1` (34). `          DO 111 K=JS,JE` (36). `            IC=ICOL_R3(K)` (37). `            CALL ORDER2(N,KS,ICOL_R3(IP0),IC)` (38). `  111     CONTINUE` (39). `  110   CONTINUE` (41). ORDER2는 같은 열 번호가 이미 있으면 N을 늘리지 않는다. 이 설명의 근거는 동일 Source code의 `util/order2.f:5–22`이다. SHIFT0 복사의 근거는 `util/shift0.f:15–17`이다. [11-04 전수 검증 보완] |
| 43–50 | 시작 시 1–2행 RHSIDXB 루틴·14행 `DO 100 II=2,NROW` 안이며 27행 IP 루프 밖. II 루프는 45행 `100 CONTINUE`에서 닫힌다. IROW_R3의 다음 행 주소를 갱신하고 II 루프를 닫는다(43–45). NSIZ_R3를 마지막 주소에서 1을 뺀 값으로 정한 뒤 반환한다(47–50). 원문: `        IROW_R3(II+1)=IROW_R3(II)+N` (43). `  100 CONTINUE` (45). `      NSIZ_R3=IROW_R3(NROW+1)-1` (47). `      RETURN` (49). `      END` (50). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–12: NROW>0 검사 없이 NROW 행과 IROW_R3(2)에 접근한다.
