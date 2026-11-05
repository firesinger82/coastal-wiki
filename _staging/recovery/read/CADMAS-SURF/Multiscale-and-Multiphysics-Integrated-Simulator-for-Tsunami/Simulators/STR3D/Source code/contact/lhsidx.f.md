---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/lhsidx.f
lines: 54
sha256: d7f82baf7478584ef393609cf402ffcc4575b5da174cc67ef5fdbe6c439ea682
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# lhsidx.f — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | 루틴·배열을 선언한다(1–4). 첫 행의 열 목록을 SHIFT0으로 복사하고 다음 행 포인터(row pointer)를 계산한다(6–9). 원문: `      SUBROUTINE LHSIDX(NROW,IROW_L,ICOL_L,IROW_L2,ICOL_L2,NSIZ_L2,IDL)` (1); `      DIMENSION IROW_L(NROW+1),ICOL_L(*),IROW_L2(NROW+1),ICOL_L2(*)` `     &         ,IDL(NROW)` (3–4, 하나의 고정형식 연속문); `      IROW_L2(1)=1` (6); `      N=IROW_L(2)-1` (7); `      CALL SHIFT0(ICOL_L2,ICOL_L,N)` (8); `      IROW_L2(2)=IROW_L2(1)+N` (9). |
| 11–54 | 시작 시 1행 LHSIDX 루틴 안이다. I=2..NROW에서 원래 열 목록을 복사한다(11–18). 라벨 110으로 목록을 순회하며 자기 행 번호를 만나면 라벨 120으로 이동한다(20–24). 그 전 열 J의 확장 목록에서 IC>J인 항을 ORDER2로 삽입하고 반복한다(25–34). 다음 행 포인터와 총 저장 길이를 계산한다(36–40). 마지막 루프는 각 행의 대각 열 위치를 찾아 IDL에 저장한다(42–51). RETURN·END로 끝낸다(53–54). 원문: `      DO 100 I=2,NROW` (11); `        IS=IROW_L(I)` (13); `        IE=IROW_L(I+1)-1` (14); `        N=IE-IS+1` (15); `        IP0=IROW_L2(I)` (16); `        CALL SHIFT0(ICOL_L2(IP0),ICOL_L(IS),N)` (17); `        IP=IP0-1` (18); `          IP=IP+1` (22); `          J=ICOL_L2(IP)` (23); `          IF( J .EQ. I ) GOTO 120` (24); `          IS=IROW_L2(J)` (25); `          IE=IROW_L2(J+1)-1` (26); `          KS=1` (27); `          DO 111 K=IS,IE` (29); `            IC=ICOL_L2(K)` (30); `            IF( IC .GT. J ) CALL ORDER2(N,KS,ICOL_L2(IP0),IC)` (31); `        GOTO 110` (34); `  120   IROW_L2(I+1)=IROW_L2(I)+N` (36); `      NSIZ_L2=IROW_L2(NROW+1)-1` (40); `      DO 200 I=1,NROW` (42); `        IS=IROW_L2(I)` (43); `        IE=IROW_L2(I+1)-1` (44); `        DO 210 J=IS,IE` (45); `          IF( ICOL_L2(J) .EQ. I ) THEN` (46); `            IDL(I)=J` (47); `            EXIT` (48). `GOTO 110`의 대상은 `  110   CONTINUE`(20)이다. 11행 `DO 100 I=2,NROW`는 38행 `100 CONTINUE`에서 끝난다. 29행 `DO 111 K=IS,IE`는 32행 `111 CONTINUE`에서 끝난다. 45행 `DO 210 J=IS,IE`는 50행 `210 CONTINUE`에서 끝난다. 48행 EXIT는 이 J 루프를 벗어난다. 42행 `DO 200 I=1,NROW`는 51행 `200 CONTINUE`에서 끝난다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–9: NROW 값 검사 없이 IROW_L(2)·IROW_L2(2)를 참조한다.
- 22–34: 라벨 110 반복은 자기 행 번호 J==I를 만나면 종료하며 IP의 행 끝을 검사하는 별도 조건은 없다.
- 42–51: 대각 열을 찾지 못한 행의 IDL 값을 지정하는 ELSE나 초기화 문장은 없다.
