---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/edgestk.f
lines: 19
sha256: d79f9d0f4aee4253030b40b68c23bafea9878a6fd59241e09a69eec3656db847
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# edgestk.f — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | 루틴·암시적 자료형·배열을 선언한다(1–4). 두 끝점과 접촉점 좌표로 LENCD를 호출하고 VECML2로 V의 크기 A를 구한다(6–11). T가 열린 구간 (0,1)에 있고 A<EPS이면 상태 14와 MA를 저장하고 RSLV(1)에 T를 넣는다(13–17). 루틴을 끝낸다(19). 원문: `      SUBROUTINE EDGESTK(ISLV,RSLV,POSS,MA,IG,POS,EPS)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION X(3,3),POS(3,*),IG(2),V(3),ISLV(2),RSLV(3),POSS(3)` (4); `      X(:,1:2) = POS(:,IG(:))` (6); `      X(:,3) = POSS(:)` (7); `      CALL LENCD(T,V,X)` (9); `      CALL VECML2(A,V,3)` (11); `      IF( T > 0.D0 .AND. T < 1.D0 .AND. A < EPS ) THEN` (13); `        ISLV(1) = 14` (14); `        ISLV(2) = MA` (15); `        RSLV(1) = T` (16). T·V의 투영 계산 근거는 같은 contact 디렉터리의 `lencd.f:6–14`이다. V의 크기 계산 근거는 같은 STR3D 원문 트리의 `util/vecml2.f:6–10`이다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13–17: 조건이 거짓이면 ISLV와 RSLV에 대입하지 않는다.
