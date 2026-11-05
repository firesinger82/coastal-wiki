---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/gauss_pn_32.h
lines: 4
sha256: 9e4cde746abdcaf3606b98aba6047d8046ca66c98dc3d4072c21ac21b0a8d017
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gauss_pn_32.h — 판독 구간 기록

구간은 1행부터 4행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | RG(3)·SG(3)·TG(2)를 선언하고 DATA 값을 설정한다. 해석: RG·SG는 삼각형의 세 적분점 좌표이고 TG는 축 방향의 두 적분점 좌표이다. 원문: `      DIMENSION RG(3),SG(3),TG(2)` (1)； `      DATA RG / .5D0, .5D0, 0.D0 /` (2)； `      DATA SG / 0.D0, .5D0, .5D0 /` (3)； `      DATA TG / -.577350269189626D0, .577350269189626D0 /` (4)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1–4: 이 포함 파일은 RG·SG·TG만 선언한다. 해석: 좌표만 선언하고 가중치 배열은 선언하지 않는다. [11-04 전수 검증 정정]
