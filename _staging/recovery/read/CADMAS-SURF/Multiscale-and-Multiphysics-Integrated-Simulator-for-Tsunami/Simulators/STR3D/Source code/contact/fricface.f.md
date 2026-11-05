---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/fricface.f
lines: 14
sha256: fb3c7f0f0cb50e39589b11792749c69dcefa7cc2c6a51d2fe2e66bb2a6ea3406
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fricface.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 루틴·암시적 자료형·배열을 선언한다(1–4). 면 세 절점과 접촉점의 UG 1:3 성분을 U0에 저장하고 대응 좌표를 X에 모은다(6–10). AREACD로 RL0을 구한다(12). 루틴을 끝낸다(14). 원문: `      SUBROUTINE FRICFACE(U0,RL0,NS,IELC,UG,POS)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION X(3,4),POS(3,*),IELC(3),RL0(3),E(3),U0(3,4),UG(6,*)` (4); `      U0(:,1:3) = UG(1:3,IELC(:))` (6); `      U0(:,4)   = UG(1:3,NS)` (7); `      X(:,1:3) = POS(:,IELC(:))` (9); `      X(:,4)   = POS(:,NS)` (10); `      CALL AREACD(RL0,E,H,X)` (12). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
