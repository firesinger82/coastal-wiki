---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/facestk.f
lines: 19
sha256: 35bfcc5d677136c5a0d93cec634674a3f79f1bfde3c723f57352437352feabcf
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# facestk.f — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | 루틴·암시적 자료형·논리 함수 AREAIN과 배열을 선언한다(1–6). 세 면 절점과 접촉점 좌표로 AREACD를 호출한다(8–11). AREAIN(RL,0.D0)이 참이고 H의 절댓값이 EPS 미만이면 상태 15·면 번호 MA·RL을 저장한다(13–17). 루틴을 끝낸다(19). 원문: `      SUBROUTINE FACESTK(ISLV,RSLV,POSS,MA,IELC,POS,EPS)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      LOGICAL AREAIN` (4); `      DIMENSION X(3,4),POS(3,*),IELC(3),RL(3),E(3),ISLV(2),RSLV(3)` `     &         ,POSS(3)` (5–6, 하나의 고정형식 연속문); `      X(:,1:3) = POS(:,IELC(:))` (8); `      X(:,4) = POSS(:)` (9); `      CALL AREACD(RL,E,H,X)` (11); `      IF( AREAIN(RL,0.D0) .AND. DABS(H) < EPS ) THEN` (13); `        ISLV(1) = 15` (14); `        ISLV(2) = MA` (15); `        RSLV(:) = RL(:)` (16). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13–17: 조건이 거짓이면 ISLV와 RSLV에 대입하지 않는다.
