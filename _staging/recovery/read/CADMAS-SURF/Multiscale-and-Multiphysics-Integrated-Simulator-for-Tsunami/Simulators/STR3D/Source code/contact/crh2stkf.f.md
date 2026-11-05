---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/crh2stkf.f
lines: 39
sha256: 0670b2784d0a13c493907262322398b3a2052bc4332cb2d7c189a8788121a641
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# crh2stkf.f — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–39 | 루틴·암시적 자료형·배열을 선언한다(1–4). 세 면 절점과 접촉점 좌표로 AREACD를 호출한다(6–9). IFCQ=0이면 RL 세 성분을 세 번 저장한다(11–20). ELSE에서는 각 묶음의 앞 두 항에 RL(J)+.25D0*RL(3)을, 뒤 두 항에 .25D0*RL(3)을 저장하여 총 12개를 만든다(22–35). 분기·루틴을 닫는다(37–39). 원문: `      SUBROUTINE CRH2STKF(CRH,NS,IELC,IFCQ,POS)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION X(3,4),POS(3,*),IELC(3),RL(3),E(3),CRH(*)` (4); `      X(:,1:3) = POS(:,IELC(:))` (6); `      X(:,4) = POS(:,NS)` (7); `      CALL AREACD(RL,E,H,X)` (9); `      IF( IFCQ == 0 ) THEN` (11); `        IP = 0` (13); `        DO I = 1, 3` (15); `          DO J = 1, 3` (16); `            IP = IP + 1` (17); `            CRH(IP) = RL(J)` (18); `      ELSE` (22); `        IP = 0` (24); `        DO I = 1, 3` (26); `          DO J = 1, 2` (27); `            IP = IP + 1` (28); `            CRH(IP) = RL(J) + .25D0 * RL(3)` (29); `          DO J = 3, 4` (31); `            IP = IP + 1` (32); `            CRH(IP) = .25D0 * RL(3)` (33). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
