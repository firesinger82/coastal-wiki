---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_trns2.f
lines: 13
sha256: 003f9b1199f3e1f269544fb96b2f41234265d3132b4aed2468698e49fd38f550
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_trns2.f — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 암시적 실수·2차원 배열 선언(1–5). X의 세 열에서 X0를 빼서 DX에 넣는다(7–9). SF_AXB(X,TR,DX,2,2,3)를 호출한다(11). 해석: 이름과 인수로 볼 때 X를 변환하는 호출이다. 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      SUBROUTINE SF_TRNS2(X,X0,TR)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      DIMENSION DX(2,3),X(2,3),X0(2),TR(2,2)` (5)<br>`      DO I = 1, 3` (7)<br>`        DX(:,I) = X(:,I) - X0(:)` (8)<br>`      ENDDO` (9)<br>`      CALL SF_AXB(X,TR,DX,2,2,3)` (11)<br>`      END` (13) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
