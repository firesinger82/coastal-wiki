---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_trns1.f
lines: 20
sha256: 9a09676cac3b2e9588b781d761e892e70b7dd630562855fe0befa01697d294f1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_trns1.f — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 암시적 실수·배열 범위 선언(1–5). X의 세 열에서 X0를 빼서 DX에 넣는다(7–9). SF_AXB를 호출한다(11). 해석: SF_AXB의 이름과 인수로 볼 때 3차원 변환에 해당한다. 변환한 두 변 벡터에 SF_CROSS2를 적용하고 EZ에 E(3)을 복사한다(13–18). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      SUBROUTINE SF_TRNS1(X,EZ,X0,TR)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      DIMENSION X(3,3),X0(3),DX(3,3),TR(3,3),V12(3),V13(3),E(3)` (5)<br>`      DO I = 1, 3` (7)<br>`        DX(:,I) = X(:,I) - X0(:)` (8)<br>`      ENDDO` (9)<br>`      CALL SF_AXB(X,TR,DX,3,3,3)` (11)<br>`      V12(:) = X(:,2) - X(:,1)` (13)<br>`      V13(:) = X(:,3) - X(:,1)` (14)<br>`      CALL SF_CROSS2(V12,V13,E)` (16)<br>`      EZ = E(3)` (18)<br>`      END` (20) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
