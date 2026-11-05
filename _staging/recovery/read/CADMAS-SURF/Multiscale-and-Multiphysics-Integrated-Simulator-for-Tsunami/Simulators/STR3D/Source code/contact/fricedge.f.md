---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/fricedge.f
lines: 16
sha256: e0595c54f9d2dfda146a9b8d55bf65cf29d3f9250787b0cfdf9b1c86c928ad72
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fricedge.f — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 루틴·암시적 자료형·배열을 선언한다(1–4). 모서리(edge) 끝점 두 개와 접촉점의 UG 1:3 성분을 U0에 저장한다(6–7). 대응 좌표로 LENCD를 호출하여 RL0(2)를 구한 뒤 RL0(1)=1-RL0(2)를 계산한다(9–14). 루틴을 끝낸다(16). 원문: `      SUBROUTINE FRICEDGE(U0,RL0,NS,IG,UG,POS)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION X(3,3),POS(3,*),IG(2),RL0(2),V(3),U0(3,3),UG(6,*)` (4); `      U0(:,1:2) = UG(1:3,IG(:))` (6); `      U0(:,3)   = UG(1:3,NS)` (7); `      X(:,1:2) = POS(:,IG(:))` (9); `      X(:,3)   = POS(:,NS)` (10); `      CALL LENCD(RL0(2),V,X)` (12); `      RL0(1) = 1.D0 - RL0(2)` (14). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
