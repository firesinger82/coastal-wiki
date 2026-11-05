---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/facerl.f
lines: 14
sha256: e5776c7c0f90cf6c38836316e8da1cfc8a52ee90dacef7116405ca79d3191cba
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# facerl.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 루틴·암시적 자료형·배열 차원을 선언한다(1–4). SHIFT1로 접촉점과 면 세 절점 좌표를 XYZ에 모은다(6–9). AREACD로 면적 좌표(area coordinates) RL을 구한다(11). RETURN·END로 끝낸다(13–14). 원문: `      SUBROUTINE FACERL(RL,POSS,IELC,POS)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION RL(3),IELC(3),POS(3,*),XYZ(3,4),E(3),POSS(3)` (4); `      CALL SHIFT1(XYZ(1,4),POSS,3)` (6); `      DO 100 I=1,3` (7); `        CALL SHIFT1(XYZ(1,I),POS(1,IELC(I)),3)` (8); `      CALL AREACD(RL,E,H,XYZ)` (11). 복사 근거는 같은 STR3D 원문 트리의 `util/shift1.f:16–18`이다. RL의 면적 좌표 계산 근거는 같은 contact 디렉터리의 `areacd.f:28–44`이다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
