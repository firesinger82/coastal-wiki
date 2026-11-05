---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/fricint.f
lines: 43
sha256: 21992bbed0858dff3fba61ac51ac222923b21abaddf4d42a1171344984d9728a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fricint.f — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–43 | 루틴과 배열 차원을 선언한다(1–5). 접촉점을 순회하면서 비활성 마찰과 INDC<=NNODI 접촉은 건너뛴다(7–11). 상태 2·12는 IEDQ 여부에 따라 사각 면 4절점 또는 모서리 2절점, 상태 3·13은 IFCQ 여부에 따라 사각 면 4절점 또는 삼각 면 3절점을 모은다(13–33). 모은 절점 중 NNODI 이하가 하나라도 있으면 유지하고, 없으면 IFRIC(1,I)=0으로 비활성화한다(35–41). 루틴을 끝낸다(43). 원문: `      SUBROUTINE FRICINT(IFRIC,NNODI,NINDC,ISLV,INDC,IELC,IEDG,IELQ,IFCQ` `     &                  ,IEDQ)` (1–2, 하나의 고정형식 연속문); `      DIMENSION IFRIC(10,NINDC),ISLV(2,NINDC),INDC(NINDC),IELC(3,*)` `     &         ,IEDG(6,*),IELQ(4,*),IFCQ(*),IEDQ(*),IG(4)` (4–5, 하나의 고정형식 연속문); `      DO I = 1, NINDC` (7); `        IF( IFRIC(1,I) == 0 ) CYCLE` (9); `        IF( INDC(I) <= NNODI ) CYCLE` (11); `        IST = ISLV(1,I)` (13); `        MST = ISLV(2,I)` (14); `        SELECT CASE( IST )` (16); `        CASE( 2, 12 )` (17); `          IF( IEDQ(MST) > 0 ) THEN` (18); `            N = 4` (19); `            IG(:) = IELQ(:,IEDQ(MST))` (20); `          ELSE` (21); `            N = 2` (22); `            IG(1:2) = IEDG(1:2,MST)` (23); `        CASE( 3, 13 )` (25); `          IF( IFCQ(MST) > 0 ) THEN` (26); `            N = 4` (27); `            IG(:) = IELQ(:,IFCQ(MST))` (28); `          ELSE` (29); `            N = 3` (30); `            IG(1:3) = IELC(:,MST)` (31); `        DO J = 1, N` (35); `          IF( IG(J) <= NNODI ) GOTO 10` (36); `        IFRIC(1,I) = 0` (39); `   10 ENDDO` (41). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–33: 상태 선택에는 2·12와 3·13만 있고 CASE DEFAULT는 없다.
