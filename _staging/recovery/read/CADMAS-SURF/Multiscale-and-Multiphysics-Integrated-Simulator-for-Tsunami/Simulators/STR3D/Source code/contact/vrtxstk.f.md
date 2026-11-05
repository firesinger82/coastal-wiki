---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/vrtxstk.f
lines: 13
sha256: f638f00f1bcc41123bb251832dbb173be1cc404752c8d36f4ff453591860a9a2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vrtxstk.f — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | VRTXSTK는 LENGTH로 POSS와 MA 절점의 거리(distance) XL을 구한다(6). XL<EPS일 때만 ISLV를 정점(vertex) 상태 11과 MA로 설정한다(8–11). 암시적 형·배열 선언, 빈 줄과 END를 포함한다. 원문: `      SUBROUTINE VRTXSTK(ISLV,POSS,MA,POS,EPS)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). `      DIMENSION POS(3,*),ISLV(2),POSS(3)` (4). `      CALL LENGTH(XL,POSS,POS(1,MA),3)` (6). `      IF( XL < EPS ) THEN` (8). `        ISLV(1) = 11` (9). `        ISLV(2) = MA` (10). `      ENDIF` (11). `      END` (13). 이 기록의 보조 루틴 설명 근거(동일 Source code 기준): `util/length.f:6–12`(거리). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–11: XL=EPS이거나 더 큰 경우에는 ISLV를 변경하지 않는다.
