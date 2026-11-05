---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_hqu1.f
lines: 14
sha256: 09983f4fb0f23ba718667fb1b66f5f6dd71e5580e2684fcc37ad7564009080bf
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_hqu1.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | SF_HQU1 선언과 H(4) 범위(1–4). XL·YL·X·Y로 R·S를 계산한다(6–7). H(1:4)를 아래 인용한 네 식으로 계산한다(9–12). 해석: R·S는 무차원 좌표이고 H(1:4)는 쌍선형 형상함수다. 원문: `      SUBROUTINE SF_HQU1(H,XL,YL,X,Y)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      DIMENSION H(4)` (4)<br>`      R = 2.D0 * X / XL - 1.D0` (6)<br>`      S = 2.D0 * Y / YL - 1.D0` (7)<br>`      H(1) = .25D0 * ( 1.D0 - R ) * ( 1.D0 - S )` (9)<br>`      H(2) = .25D0 * ( 1.D0 + R ) * ( 1.D0 - S )` (10)<br>`      H(3) = .25D0 * ( 1.D0 + R ) * ( 1.D0 + S )` (11)<br>`      H(4) = .25D0 * ( 1.D0 - R ) * ( 1.D0 + S )` (12)<br>`      END` (14) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–7: XL·YL을 분모에 쓰며 이 파일에는 0 검사나 X·Y 범위 제한이 없다.
