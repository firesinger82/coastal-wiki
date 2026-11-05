---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/circhk.f
lines: 62
sha256: 154213af5bf1b649f07ee233fc661c449019915fb419cbdcc1677db74537b62b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# circhk.f — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | CIRCHK의 인수 배열과 고정 작업 배열 IP(4096)·IP0(4096)을 선언한다(1–6). ISLVG를 0으로 초기화한다(8). `ISLV(1,I) == 0`이면 건너뛴다(11). 나머지 항목은 `IG = INDC(I)`에 대해 ISLVG(1:2,IG)에 ISLV(:,I)를 복사하고 ISLVG(3,IG)에 I를 대입한다(12–14). 원문(연속 표시는 같은 문장의 이어지는 행이다): `      SUBROUTINE CIRCHK(ISLV,ISLVG,NNOD,NINDC,INDC,IEDG,IELC,IELQ,IFCQ` (1); `     &                 ,IEDQ,IVRQ)` (2); `      DIMENSION ISLVG(3,NNOD),ISLV(2,NINDC),INDC(NINDC),IEDG(6,*)` (4); `     &         ,IELC(3,*),IELQ(4,*),IVRQ(*),IEDQ(*),IFCQ(*),JP(4)` (5); `     &         ,IP(4096),IP0(4096)` (6); `      ISLVG(:,:) = 0` (8); `      DO I = 1, NINDC` (10); `        IF( ISLV(1,I) == 0 ) CYCLE` (11); `        IG = INDC(I)` (12); `        ISLVG(1:2,IG) = ISLV(:,I)` (13); `        ISLVG(3,IG) = I` (14); `      ENDDO` (15). [11-04 전수 검증 정정] |
| 17–62 | 시작 시 1–2행 CIRCHK 루틴 안. 각 I에 대해 `IG = INDC(I)`와 `IP(1) = IG`를 설정하고 무한 DO(24)를 수행한다(17–24). `JG = IP(J)`로 후보를 읽는다(30). `IST == 0`이면 J를 건너뛴다(35). 나머지 후보는 MSTNOD를 M·JP 등의 인수로 호출한다(37). `JP(K) == IG`이면 `ISLVG(1:2,JG)`와 `ISLV(:,ISLVG(3,JG))`를 0으로 정한다(40–42). `ISLVG(3,JG)`는 이 대입에서 바꾸지 않는다. `GOTO 10`은 50행의 J 루프 `ENDDO`로 이동한다(43). 나머지 후보를 IP0에 이어 붙이고 N0=0이면 종료하며 아니면 다음 후보로 복사한다(47–58). 원문(연속 표시는 같은 문장의 이어지는 행이다): `      DO I = 1, NINDC` (17); `        IG = INDC(I)` (19); `        N = 1` (21); `        IP(1) = IG` (22); `        DO` (24); `          N0 = 0` (26); `          DO J = 1, N` (28); `            JG = IP(J)` (30); `            IST = ISLVG(1,JG)` (32); `            MA = ISLVG(2,JG)` (33); `            IF( IST == 0 ) CYCLE` (35); `            CALL MSTNOD(M,JP,IST,MA,IELC,IEDG,IELQ,IFCQ,IEDQ,IVRQ)` (37); `            DO K = 1, M` (39); `              IF( JP(K) == IG ) THEN` (40); `                ISLVG(1:2,JG) = 0` (41); `                ISLV(:,ISLVG(3,JG)) = 0` (42); `                GOTO 10` (43); `              ENDIF` (44); `            ENDDO` (45); `            IP0(N0+1:N0+M) = JP(1:M)` (47); `            N0 = N0 + M` (48); `   10     ENDDO` (50); `          IF( N0 == 0 ) EXIT` (52); `          N = N0` (54); `          IP(1:N) = IP0(1:N0)` (56); `        ENDDO` (58); `      ENDDO` (60); `      END` (62). [11-04 전수 검증 보완] [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·47–56: IP·IP0의 크기는 4096으로 고정되어 있다. N0+M 또는 N을 4096과 비교하는 조건은 이 루틴에 없다.
- 24–58: 탐색 종료 조건은 N0==0이다(52). 이미 방문한 노드 집합을 별도로 저장하는 배열이나 조건은 이 루틴에 없다.
