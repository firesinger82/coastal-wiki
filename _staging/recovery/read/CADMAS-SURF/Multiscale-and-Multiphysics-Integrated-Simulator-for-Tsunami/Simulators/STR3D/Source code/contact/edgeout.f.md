---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/edgeout.f
lines: 16
sha256: 037a6dbd878a6202e3b71df6489240de7b1a1cacb48d61872f1dd312c2aa04f9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# edgeout.f — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 루틴·암시적 자료형·배열을 선언한다(1–4). DL이 양수이면 두 번째 끝점, ELSE이면 첫 번째 끝점을 IM으로 선택한다(6–10). 상태를 11로 바꾸고 선택한 절점 번호를 ISLV(2)에 넣는다(12–13). 루틴을 끝낸다(15–16). 원문: `      SUBROUTINE EDGEOUT(ISLV,DL,IEDG)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION IEDG(6),ISLV(2)` (4); `      IF(DL .GT. 0.) THEN` (6); `        IM=IEDG(2)` (7); `      ELSE` (8); `        IM=IEDG(1)` (9); `      ISLV(1)=11` (12); `      ISLV(2)=IM` (13). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
