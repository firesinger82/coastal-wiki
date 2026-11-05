---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/main/dirinit.f
lines: 15
sha256: 27825e7011d8a4867208eae409b3785efd2f99b6e4164524117f76cad19d54cf
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# dirinit.f — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | DIRINIT은 NP 두 절점의 좌표 차를 E 첫 열에 저장한다(6). DIRCOS, CROSS2, CROSS를 차례로 호출한다(7–9). E의 2:3열을 VG(:,:,1)과 VG(:,:,2)에 동일하게 복사한다(11–12). 해석: 호출 이름을 근거로 방향 코사인(direction cosine)과 단면 방향을 구성하는 과정으로 읽는다. E(3,3)·NP(2)·VG(3,2,2)·V(3) 선언과 마지막 빈 줄을 포함한다(4·15). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE DIRINIT(VG,NP,V,GRID)` (1) <br> `      IMPLICIT REAL*8(A-H,O-Z)` (3) <br> `      DIMENSION E(3,3),GRID(3,*),NP(2),VG(3,2,2),V(3)` (4) <br> `      E(:,1) = GRID(:,NP(2)) - GRID(:,NP(1))` (6) <br> `      CALL DIRCOS(E(1,1),E(1,1),3)` (7) <br> `      CALL CROSS2(E(1,1),V,E(1,3))` (8) <br> `      CALL CROSS(E(1,3),E(1,1),E(1,2))` (9) <br> `      VG(:,:,1) = E(:,2:3)` (11) <br> `      VG(:,:,2) = E(:,2:3)` (12) <br> `      END` (14) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
