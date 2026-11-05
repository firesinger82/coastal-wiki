---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/edgedl.f
lines: 23
sha256: d52aee71b376957887879895df22214a46e93fca73daf931e329da7126f93a0f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# edgedl.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 루틴·암시적 자료형·배열을 선언한다(1–4). 접촉점과 두 끝점 좌표를 SHIFT1로 모은 뒤 LENCD를 호출한다(6–12). RT>1이면 초과량 RT-1을, RT<0이면 RT 자체를, 나머지 범위에서는 0을 DL로 반환한다(14–20). 루틴을 끝낸다(22–23). 원문: `      SUBROUTINE EDGEDL(DL,POSS,IEDG,POS)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION IEDG(6),POS(3,*),XYZ(3,3),V(3),POSS(3)` (4); `      CALL SHIFT1(XYZ(1,3),POSS,3)` (6); `      IG1=IEDG(1) ` (7); `      IG2=IEDG(2)` (8); `      CALL SHIFT1(XYZ(1,1),POS(1,IG1),3)` (9); `      CALL SHIFT1(XYZ(1,2),POS(1,IG2),3)` (10); `      CALL LENCD(RT,V,XYZ)` (12); `      IF( RT .GT. 1.D0 ) THEN` (14); `        DL = RT -1.D0` (15); `      ELSEIF( RT .LT. 0.D0 ) THEN` (16); `        DL = RT` (17); `      ELSE` (18); `        DL = 0.` (19). 좌표 복사의 근거는 같은 STR3D 원문 트리의 `util/shift1.f:16–18`이다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
