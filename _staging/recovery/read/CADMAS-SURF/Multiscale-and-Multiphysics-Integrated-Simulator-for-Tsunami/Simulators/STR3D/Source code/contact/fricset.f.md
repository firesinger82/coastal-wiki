---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/fricset.f
lines: 34
sha256: bac3dd0ff65c5714930bb033397bf2c4223e3ff471e7497f7193c0e87aff1fc5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fricset.f — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | 루틴·암시적 자료형·배열을 선언한다(1–6). 접촉점을 순회하며 IFRIC(2,I)=3을 1로 바꾸고 IFRIC(7,I)=1을 둔다(8–11). `IFRIC(1,I) == 1`이면 NS·IST·MA를 읽는다(13–19). 그렇지 않아도 `IDYN == 1`, `IFRIC(1,I) == 2`, `ITER2 == 1`이 모두 참이고 `IFRIC(3,I) == 0` 또는 `ISTEP == 1`이 참이면 같은 대입을 수행한다(14–19). IST=2이면 FRICEDGE를 호출한다(21–22). IST=3이면 FRICFACE를 호출한다(23–24). 두 호출에 U0와 RL0을 전달한다. 그 바깥 조건 안에서 IFRIC(2,I)·IFRIC(9,I)를 1로 둔다(27–28). 루프·루틴을 끝낸다(30–34). 원문: `      SUBROUTINE FRICSET(U0,RL0,IFRIC,NINDC,ISLV,INDC,IEDG,IELC,UG,POS` `     &                  ,ISTEP,ITER2,IDYN)` (1–2, 하나의 고정형식 연속문); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION U0(3,4,NINDC),RL0(3,NINDC),ISLV(2,NINDC),INDC(NINDC)` `     &         ,IEDG(6,*),IELC(3,*),UG(6,*),POS(3,*),IFRIC(10,NINDC)` (5–6, 하나의 고정형식 연속문); `      DO I = 1, NINDC` (8); `        IF( IFRIC(2,I) == 3 ) IFRIC(2,I) = 1` (10); `        IFRIC(7,I) = 1` (11); `        IF( IFRIC(1,I) == 1 .OR.` `     &      ( IDYN == 1 .AND. IFRIC(1,I) == 2 .AND. ITER2 == 1 .AND.` `     &        ( IFRIC(3,I) == 0 .OR. ISTEP == 1 ) ) ) THEN` (13–15, 하나의 고정형식 연속문); `          NS = INDC(I)` (17); `          IST = ISLV(1,I)` (18); `          MA  = ISLV(2,I)` (19); `          IF( IST == 2 ) THEN` (21); `            CALL FRICEDGE(U0(1,1,I),RL0(1,I),NS,IEDG(1,MA),UG,POS)` (22); `          ELSEIF( IST == 3 ) THEN` (23); `            CALL FRICFACE(U0(1,1,I),RL0(1,I),NS,IELC(1,MA),UG,POS)` (24); `          IFRIC(2,I) = 1` (27); `          IFRIC(9,I) = 1` (28). 21·23행 분기 사슬에는 ELSE가 없으며 25행 ENDIF로 닫힌다. [11-04 전수 검증 정정] [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 21–28: 상태 2·3 이외에는 초기화 루틴을 호출하지 않지만 바깥 조건이 참이면 IFRIC(2,I)·IFRIC(9,I)는 1로 설정한다.
