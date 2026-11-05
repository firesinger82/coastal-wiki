---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/edgquad.f
lines: 22
sha256: f8d6bf92371060f5cfdb96c6d48622b5d6b9f2852f8296041adb3d1984b71268
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# edgquad.f — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 루틴과 IEDG(6,4)·IELC(3,4)를 선언한다(1–3). 각 삼각 면의 두 절점을 모서리 끝점으로 복사한다(5). 국소 번호를 1·2로 정하고 네 모서리의 인접 면 번호를 IP부터 IP+3까지 순환하도록 구성한다(7–20). 루틴을 끝낸다(22). 원문: `      SUBROUTINE EDGQUAD(IEDG,IELC,IP)` (1); `      DIMENSION IEDG(6,4),IELC(3,4)` (3); `      IEDG(1:2,:) = IELC(2:3,:)` (5); `      IEDG(4,:) = 1` (7); `      IEDG(6,:) = 2` (8); `      IEDG(3,1) = IP` (10); `      IEDG(5,1) = IP + 1` (11); `      IEDG(3,2) = IP + 1` (13); `      IEDG(5,2) = IP + 2` (14); `      IEDG(3,3) = IP + 2` (16); `      IEDG(5,3) = IP + 3` (17); `      IEDG(3,4) = IP + 3` (19); `      IEDG(5,4) = IP` (20). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
