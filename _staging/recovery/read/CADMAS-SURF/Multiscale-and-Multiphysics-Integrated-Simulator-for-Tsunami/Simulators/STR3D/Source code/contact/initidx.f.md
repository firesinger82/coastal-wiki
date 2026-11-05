---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/initidx.f
lines: 58
sha256: 5098d96a489dc58a2b6d1a20bc3e8889d454d90b9d669586f48a6e8baa6a8b59
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# initidx.f — 판독 구간 기록

구간은 1행부터 58행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | 루틴·배열 차원을 선언한다(1–5). NROW=NIDEP로 두고 좌우 행 포인터(row pointer)의 시작을 1로 초기화한다(7–10). 원문: `      SUBROUTINE INITIDX(IROW_L,ICOL_L,IROW_R,ICOL_R,NSIZ_L,NSIZ_R,IDEP` `     &                  ,IDX,IRH,INDP,NIDEP,NINDP,ITO)` (1–2, 하나의 고정형식 연속문); `      DIMENSION IROW_L(*),ICOL_L(*),IROW_R(*),ICOL_R(*),IDEP(2,NIDEP)` `     &         ,IDX(2,NIDEP),IRH(2,*),INDP(2,NINDP)` (4–5, 하나의 고정형식 연속문); `      NROW=NIDEP` (7); `      IROW_L(1)=1` (9); `      IROW_R(1)=1` (10). |
| 12–58 | 시작 시 1행 INITIDX 루틴 안이다. 각 행의 왼쪽 목록에 자기 행 번호를 먼저 넣고 IDX 구간을 순회한다(12–25). IRH의 절점·자유도(degree of freedom)가 IDEP에 있으면 ORDER로 왼쪽 목록에, INDP에 있으면 오른쪽 목록에 정렬 삽입한다(27–42). 둘 다 찾지 못하면 오류 메시지를 쓴다(44). 이어서 ERRSTP(90,ITO)를 호출한다(45). NL·NR로 다음 행 포인터를 계산하고 마지막 포인터에서 1을 빼 NSIZ_L·NSIZ_R를 구한다(49–55). RETURN·END로 끝낸다(57–58). 원문: `      DO 100 I=1,NROW` (12); `        NL=0` (14); `        NR=0` (15); `        IPL=IROW_L(I)` (16); `        IPR=IROW_R(I)` (17); `        ICOL_L(IPL)=I` (19); `        NL=NL+1` (20); `        IS=IDX(1,I)` (22); `        IE=IDX(2,I)` (23); `        DO 110 J=IS,IE` (25); `          NODE=IRH(1,J)` (27); `          IFR =IRH(2,J)` (28); `          DO 111 K=1,NIDEP` (30); `            IF( NODE .EQ. IDEP(1,K) .AND. IFR .EQ. IDEP(2,K) ) THEN` (31); `              CALL ORDER(NL,ICOL_L(IPL),K)` (32); `              GOTO 110` (33); `          DO 112 K=1,NINDP` (37); `            IF( NODE .EQ. INDP(1,K) .AND. IFR .EQ. INDP(2,K) ) THEN` (38); `              CALL ORDER(NR,ICOL_R(IPR),K)` (39); `              GOTO 110` (40); `          WRITE(ITO,*) 'STOP IN SUB. INITIDX!'` (44); `          CALL ERRSTP(90,ITO)` (45); `        IROW_L(I+1)=IROW_L(I)+NL` (49); `        IROW_R(I+1)=IROW_R(I)+NR` (50); `      NSIZ_L=IROW_L(NROW+1)-1` (54); `      NSIZ_R=IROW_R(NROW+1)-1` (55). 두 `GOTO 110`의 대상은 `  110   CONTINUE`(47)이며 25행 `DO 110 J=IS,IE`의 종료점이다. 30행 `DO 111 K=1,NIDEP`는 35행 `111 CONTINUE`에서 끝난다. 37행 `DO 112 K=1,NINDP`는 42행 `112 CONTINUE`에서 끝난다. 12행 `DO 100 I=1,NROW`는 52행 `100 CONTINUE`에서 끝난다. ORDER의 정렬 삽입과 중복 값 제외의 근거는 같은 STR3D 원문 트리의 `util/order.f:5–17`이다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
