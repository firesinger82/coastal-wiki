---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/edgechk.f
lines: 15
sha256: f810dd43c68242f73cf474b5b68e57193c405d4da7cbdf2a88e241ef3a7146af
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# edgechk.f — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 루틴·암시적 자료형·배열을 선언한다(1–4). EDGEDL로 DL을 계산한다(6). 절댓값이 1.D-10 이하이면 EDGESLIP, ELSE이면 EDGEOUT을 호출한다(8–12). RETURN·END로 끝낸다(14–15). 원문: `      SUBROUTINE EDGECHK(ISLV,POSS,MASTER,FC,EN,IELC,IEDG,POS,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION IEDG(6,*),POS(3,*),FC(3),EN(3),IELC(3,*),ISLV(2),POSS(3)` (4); `      CALL EDGEDL(DL,POSS,IEDG(1,MASTER),POS)` (6); `      IF( DABS(DL) .LE. 1.D-10 ) THEN` (8); `        CALL EDGESLIP(ISLV,FC,EN,MASTER,IEDG(1,MASTER),IELC,POS,ITO)` (9); `      ELSE` (10); `        CALL EDGEOUT(ISLV,DL,IEDG(1,MASTER))` (11). DL의 기하학적 판정 근거는 같은 contact 디렉터리의 `edgedl.f:12–20`과 `lencd.f:6–14`이다. EDGEDL은 투영 비율이 0 이상 1 이하이면 DL=0을 반환한다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8: 모서리 내부 판정 허용값은 1.D-10으로 고정되어 있다.
