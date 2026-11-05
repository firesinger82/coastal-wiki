---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/grazeel.f
lines: 39
sha256: 3c3d4a571515aef0c79799f35ac5f8800bdbcd7f8e8a6da5235d929439ed3278
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# grazeel.f — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–39 | 루틴·암시적 자료형·논리 함수 VOLIN3과 배열을 선언한다(1–6). RL의 첫 번째 임계값 미만 성분에 대응하는 맞은편 모서리(edge)의 두 절점을 고른다(8–16). 어느 성분도 임계값 미만이 아니면 ICHK=1로 반환한다(17–20). 고른 절점에 인접한 사면체(tetrahedron)를 순회하며 VOLCD·VOLIN3로 내부 여부를 확인한다(22–35). 내부이면 ICHK=1로 반환하고 끝까지 찾지 못하면 0으로 둔다(30–37). 루틴을 끝낸다(39). 원문: `      SUBROUTINE GRAZEEL(ICHK,POSS,RL,IELC,ICELA,ICEL,IBTE,POS)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      LOGICAL VOLIN3` (4); `      DIMENSION RL(3),RN(4),IELC(3),NOD(2),POS(3,*),G(3,4),ICELA(2,*)` `     &         ,ICEL(*),IBTE(4,*),POSS(3)` (5–6, 하나의 고정형식 연속문); `      IF( RL(1) < 1.D-10 ) THEN` (8); `        NOD(1) = IELC(2)` (9); `        NOD(2) = IELC(3)` (10); `      ELSEIF( RL(2) < 1.D-10 ) THEN` (11); `        NOD(1) = IELC(3)` (12); `        NOD(2) = IELC(1)` (13); `      ELSEIF( RL(3) < 1.D-10 ) THEN` (14); `        NOD(1) = IELC(1)` (15); `        NOD(2) = IELC(2)` (16); `      ELSE` (17); `        ICHK = 1` (18); `      DO I = 1, 2` (22); `        NODE = NOD(I)` (23); `        JS = ICELA(1,NODE)` (24); `        JE = ICELA(2,NODE)` (25); `        DO J = JS, JE` (26); `          K = ICEL(J)` (27); `          G(:,:) = POS( :, IBTE(:,K) )` (28); `          CALL VOLCD(RN,G,POSS)` (29); `          IF( VOLIN3(RN,1.D-10) )THEN` (30); `            ICHK = 1` (31); `      ICHK = 0` (37). 사면체 좌표 계산과 내부 판정의 근거는 같은 contact 디렉터리의 `volcd.f:19–49`와 `volin3.f:6–13`이다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8·11·14·30: 좌표 성분 판정과 체적 내부 판정의 허용값은 모두 1.D-10이다.
