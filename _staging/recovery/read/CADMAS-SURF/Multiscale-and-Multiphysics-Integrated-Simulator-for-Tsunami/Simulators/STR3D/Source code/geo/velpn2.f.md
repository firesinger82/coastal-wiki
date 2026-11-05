---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/velpn2.f
lines: 12
sha256: 468f13e1c329508ec2be02f87d8ae36b437b7ed1dc56bdbdec852aca9d5272f8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# velpn2.f — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | VELPN2는 VEL·VELG를 전달할 루틴을 ND에 따라 선택한다. 해석: 삼각기둥(prism)의 절점 속도(velocity) 변환용으로 보인다. 실수 IMPLICIT와 VEL(3,ND)·VELG(3,*)를 선언한다. ND=6이면 VINTPN1, ELSE는 VINTPN2를 호출한다. 원문: `      SUBROUTINE VELPN2(VEL,VELG,ND)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION VEL(3,ND),VELG(3,*)` (4); `      IF( ND == 6 ) THEN` (6); `        CALL VINTPN1(VEL,VELG)` (7); `      ELSE` (8); `        CALL VINTPN2(VEL,VELG)` (9); `      ENDIF` (10); `      END` (12) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–10: ND=6 이외의 모든 값은 VINTPN2로 전달한다. 별도 ND 유효성 검사문은 없다.
