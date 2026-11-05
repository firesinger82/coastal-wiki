---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/gauss_ln_3.h
lines: 8
sha256: b935c14a8e0310d04e5dd99d6bdf971ac43dff5b2c7953eff75b2dbb99526eb4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gauss_ln_3.h — 판독 구간 기록

구간은 1행부터 8행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | XG·WG 배열과 DATA를 선언한다. 해석: 각 열은 1점·2점·3점 가우스 적분(Gaussian quadrature)의 좌표와 가중치를 저장한다. 모든 DATA 연속행을 포함한다. 원문: `      DIMENSION XG(3,3),WG(3,3)` (1)； 연속문(2–4): `      DATA XG / 3*0.0D0` (2)； `     &        , -.577350269189626D0, .577350269189626D0, 0.0D0` (3)； `     &        , -.774596669241483D0, 0.0D0, .774596669241483D0 /` (4)； 연속문(5–8): `      DATA WG / 2.0D0, 2*0.0D0` (5)； `     &        , 2*1.0D0, 0.0D0` (6)； `     &        , 0.55555555555555556D0, 0.88888888888888889D0` (7)； `     &        , 0.55555555555555556D0 /` (8)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1–8: XG·WG의 첫 열 2:3행과 두 번째 열 3행의 값은 0이다. 해석: 이 위치는 각 적분법에서 사용하지 않는 슬롯이다. [11-04 전수 검증 정정]
