---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_trm1.f
lines: 26
sha256: 1bfae4166b98731360b933b05d3d5094e8a00a52891ae55ee1fb1daffca51f7b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_trm1.f — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 해석: 이름과 배열 연산으로 볼 때 3차원 삼각형 좌표 변환을 구성한다. 두 차 벡터를 계산한다(7–8). SF_DIRCOS를 한 번 호출한다(10). SF_CROSS2를 두 번 호출한다(11–12). 해석: 이 호출들은 기저 구성에 해당한다. DO I=1,3에서 TR에 기저를 전치 복사하고 원점을 정한다. X2를 0으로 초기화한 뒤 SF_VECML 세 호출로 평면 좌표를 채운다(14–24). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      SUBROUTINE SF_TRM1(TR,X0,X2,X)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      DIMENSION V12(3),V13(3),X(3,3),E(3,3),TR(3,3),X0(3),X2(2,3)` (5)<br>`      V12(:) = X(:,2) - X(:,1)` (7)<br>`      V13(:) = X(:,3) - X(:,1)` (8)<br>`      CALL SF_DIRCOS(E(1,2),V12,3)` (10)<br>`      CALL SF_CROSS2(V13,V12,E(1,3))` (11)<br>`      CALL SF_CROSS2(E(1,2),E(1,3),E(1,1))` (12)<br>`      DO I = 1, 3` (14)<br>`        TR(I,:) = E(:,I)` (15)<br>`      ENDDO` (16)<br>`      X0(:) = X(:,1)` (18)<br>`      X2(:,:) = 0.` (20)<br>`      CALL SF_VECML(X2(2,2),V12,E(1,2),3)` (22)<br>`      CALL SF_VECML(X2(1,3),V13,E(1,1),3)` (23)<br>`      CALL SF_VECML(X2(2,3),V13,E(1,2),3)` (24)<br>`      END` (26) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
