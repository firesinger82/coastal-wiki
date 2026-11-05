---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/crh2vrtx.f
lines: 12
sha256: 63d2d448e2609a928d754ba96145a42356946faab07009407eec249e7ca191e2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# crh2vrtx.f — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 루틴·암시적 자료형·가변 길이 CRH를 선언한다(1–4). IVRQ=0이면 CRH(1:3)을 1.D0으로 설정하고 ELSE에서는 CRH(1:12)를 .25D0으로 설정한다(6–10). 루틴을 끝낸다(12). 원문: `      SUBROUTINE CRH2VRTX(CRH,IVRQ)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION CRH(*)` (4); `      IF( IVRQ == 0 ) THEN` (6); `        CRH(1:3) = 1.D0` (7); `      ELSE` (8); `        CRH(1:12) = .25D0` (9). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
