---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/faceon.f
lines: 91
sha256: b4dadbdf6637baeea88e22536e6ddb77fb0808f7c939ba09440fa899b97e9696
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# faceon.f — 판독 구간 기록

구간은 1행부터 91행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | 루틴·암시적 자료형·논리 함수 AREAIN·VOLIN3와 배열을 선언한다(1–8). 원래 면의 법선(normal vector)을 NRMVEC로 구하고 접촉점 좌표를 X에 넣는다(10–15). 이전 상태 11에서는 한 절점, 12에서는 모서리 양 끝점 두 개를 검사 대상으로 정한다(17–24). 원문: `      SUBROUTINE FACEON(ISLV,RSLV,POSS,MA,IELC,IEDG,ICELA,ICEL,IBTE` `     &                 ,ICFCA,ICFC,POS,THETA)` (1–2, 하나의 고정형식 연속문); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      LOGICAL AREAIN,VOLIN3` (5); `      DIMENSION IG(2),X0(3,3),X(3,4),RN0(3),RN(3),RL(4),POSS(3),POS(3,*)` `     &         ,IEDG(6,*),IELC(3,*),ICFCA(2,*),ICFC(*),ISLV(2),RSLV(3)` `     &         ,ICELA(2,*),ICEL(*),IBTE(4,*)` (6–8, 하나의 고정형식 연속문); `      IST = ISLV(1)` (10); `      X0(:,:) = POS(:,IELC(:,MA))` (12); `      CALL NRMVEC(RN0,X0)` (13); `      X(:,4) = POSS(:)` (15); `      SELECT CASE( IST )` (17); `      CASE( 11 )` (18); `        N = 1` (19); `        IG(1) = ISLV(2)` (20); `      CASE( 12 )` (21); `        N = 2` (22); `        IG(:) = IEDG(1:2,ISLV(2))` (23). 법선 계산의 근거는 같은 contact 디렉터리의 `nrmvec.f:6–8`과 같은 STR3D 원문 트리의 `util/cross2.f:9–16`이다. [11-04 전수 검증 보완] |
| 26–68 | 시작 시 1행 FACEON 루틴 안이다. 검사 절점에 인접한 면을 순회하되 원래 면은 건너뛴다(26–35). AREACD 결과에서 법선 내적과 면 내부 조건이 참이면 상태 13과 면 번호를 저장한다(37–45). 이전 상태 11은 절점 좌표, 12는 RSLV(1)의 선형 보간 좌표를 X(:,4)에 넣는다(47–53). AREACD를 다시 호출해 RSLV를 저장하고 GOTO로 루프를 벗어난 뒤 상태 13이면 반환한다(55–67). 원문: `      DO I = 1, N` (26); `        JS = ICFCA(1,IG(I))` (28); `        JE = ICFCA(2,IG(I))` (29); `        DO J = JS, JE` (31); `          IFC = ICFC(J)` (33); `          IF( IFC == MA ) CYCLE` (35); `          X(:,1:3) = POS(:,IELC(:,IFC))` (37); `          CALL AREACD(RL,RN,H,X)` (39); `          IF( DOT_PRODUCT(RN0,RN) > DCOS(THETA) .AND.` `     &        AREAIN(RL,1.D-10) ) THEN` (41–42, 하나의 고정형식 연속문); `            ISLV(1) = 13` (44); `            ISLV(2) = IFC` (45); `            SELECT CASE( IST )` (47); `            CASE( 11 )` (48); `              X(:,4) = POS(:,IG(1))` (49); `            CASE( 12 )` (50); `              T = RSLV(1)` (51); `              X(:,4) = ( 1.D0 - T ) * POS(:,IG(1)) + T * POS(:,IG(2))` (52); `            CALL AREACD(RL,RN,H,X)` (55); `            RSLV(:) = RL(1:3)` (57); `            GOTO 10` (59); `   10 IF( ISLV(1) == 13 ) RETURN` (67). RN과 RL 계산의 근거는 같은 contact 디렉터리의 `areacd.f:7–48`이다. 면 내부 판정의 근거는 `areain.f:6–12`이다. 47행 SELECT에는 CASE DEFAULT가 없으며 53행 END SELECT로 닫힌다. [11-04 전수 검증 보완] |
| 69–91 | 시작 시 1행 FACEON 루틴 안이다. 인접 사면체(tetrahedron)를 순회하며 VOLCD로 좌표를 구하고 VOLIN3가 참이면 반환한다(69–86). 이 경로에서도 내부가 아니면 상태·국소 좌표를 모두 0으로 지운다(88–89). 루틴을 끝낸다(91). 원문: `      DO I = 1, N` (69); `        JS = ICELA(1,IG(I))` (71); `        JE = ICELA(2,IG(I))` (72); `        DO J = JS, JE` (74); `          K = ICEL(J)` (76); `          X(:,:) = POS(:,IBTE(:,K))` (78); `          CALL VOLCD(RL,X,POSS)` (80); `          IF( VOLIN3(RL,1.D-10) ) RETURN` (82); `      ISLV(:) = 0` (88); `      RSLV(:) = 0.` (89). 사면체 좌표 계산과 내부 판정의 근거는 같은 contact 디렉터리의 `volcd.f:19–49`와 `volin3.f:6–13`이다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 17–24: 초기 상태 선택에는 11·12만 있고 CASE DEFAULT가 없다.
- 41–42·82: 면·체적 내부 판정 허용값은 각각 1.D-10으로 고정되어 있다.
