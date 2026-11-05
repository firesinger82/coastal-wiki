---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/facechk.f
lines: 27
sha256: 328d6a83149b93857c4b8d47838b4d5ece04241a33d20f1865179f2f815cb118
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# facechk.f — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | 루틴·암시적 자료형·논리 함수 AREAIN과 배열 차원을 선언한다(1–9). FACERL로 새 좌표의 면적 좌표(area coordinates) RL을 구한다(11). AREAIN(RL,1.D-3)이 참이거나 ISTK=1이면 FACESEPA를 호출한다(13–15). ELSE에서는 이전 좌표 기반 FACEOUT을 호출한 뒤 새 좌표 기반 FACEON을 호출한다(17–23). 분기·루틴을 닫는다(25–27). 원문: `      SUBROUTINE FACECHK(ISLV,RSLV,POSSO,POSSN,MASTER,FC,FTOL,IELC,IEDG` `     &                  ,IELA,ICELA,ICEL,IBTE,ICFCA,ICFC,POSO,POSN,ISTK` `     &                  ,TOL,ITO)` (1–3, 하나의 고정형식 연속문); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      LOGICAL AREAIN` (6); `      DIMENSION RL(3),IELC(3,*),POSO(3,*),POSN(3,*),ISLV(2),FC(3)` `     &         ,IEDG(6,*),RSLV(3),IELA(3,*),POSSO(3),POSSN(3),ICFCA(2,*)` `     &         ,ICFC(*),ICELA(2,*),ICEL(*),IBTE(4,*)` (7–9, 하나의 고정형식 연속문); `      CALL FACERL(RL,POSSN,IELC(1,MASTER),POSN)` (11); `      IF( AREAIN(RL,1.D-3) .OR. ISTK == 1 ) THEN` (13); `        CALL FACESEPA(ISLV,FC,FTOL,MASTER,IELC(1,MASTER),POSN)` (15); `      ELSE` (17); `        CALL FACEOUT(ISLV,RSLV,POSSO,RL,IELC(1,MASTER),IEDG` `     &              ,IELA(1,MASTER),POSO,ITO)` (19–20, 하나의 고정형식 연속문); `        CALL FACEON(ISLV,RSLV,POSSN,MASTER,IELC,IEDG,ICELA,ICEL,IBTE` `     &             ,ICFCA,ICFC,POSN,TOL)` (22–23, 하나의 고정형식 연속문). 면적 좌표 계산의 근거는 같은 contact 디렉터리의 `facerl.f:6–11`과 `areacd.f:28–44`이다. AREAIN의 판정 근거는 같은 디렉터리의 `areain.f:6–12`이다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13: 면 내부 판정 허용값은 1.D-3으로 고정되어 있다. ISTK==1도 같은 분기로 들어간다.
