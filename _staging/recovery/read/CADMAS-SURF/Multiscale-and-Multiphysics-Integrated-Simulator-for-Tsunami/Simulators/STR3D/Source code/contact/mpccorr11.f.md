---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/mpccorr11.f
lines: 11
sha256: 01167410c69b97a39593016030883aed4a73bbf3f78f519a001dccd18e40a688
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mpccorr11.f — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | 루틴·암시적 자료형·배열을 선언한다(1–4). 주절점(master node) MA와 종속 절점(slave node) NS의 좌표 차이를 DUG로 계산한다(6). 그 차이를 UG의 1:3 성분과 POS에 더하여 NS를 MA의 위치로 이동한다(8–9). 루틴을 끝낸다(11). 원문: `      SUBROUTINE MPCCORR11(UG,POS,NS,MA)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION POS(3,*),DUG(3),UG(6,*)` (4); `      DUG(:) = POS(:,MA) - POS(:,NS)` (6); `      UG(1:3,NS) = UG(1:3,NS) + DUG(:)` (8); `      POS(:,NS) = POS(:,NS) + DUG(:)` (9). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
