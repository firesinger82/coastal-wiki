---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_trm2.f
lines: 35
sha256: fe411794b04701d3bb27f4d2c7d686c802095d703c51ec9afd62d460145d760c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_trm2.f — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 2차원 변환 구성의 암시적 실수·배열 선언과 두 변 벡터(1–8). 두 차 벡터에 SF_DIRCOS를 적용한다(10–12). E의 성분을 복사하고 부호를 바꿔 첫 열을 채운다(14–15). E의 두 열을 TR의 두 행으로 복사한다(17–18). 해석: SF_DIRCOS의 이름으로 볼 때 방향 코사인을 구하는 호출이다. 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      SUBROUTINE SF_TRM2(TR,X0,X)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      DIMENSION V(2,2),X(2,3),E(2,2),TR(2,2,2),T(2,2),X0(2,2)` (5)<br>`      V(:,1) = X(:,3) - X(:,2)` (7)<br>`      V(:,2) = X(:,1) - X(:,3)` (8)<br>`      DO I = 1, 2` (10)<br>`        CALL SF_DIRCOS(E(1,2),V(1,I),2)` (12)<br>`        E(1,1) =  E(2,2)` (14)<br>`        E(2,1) = -E(1,2)` (15)<br>`        TR(1,:,I) = E(:,1)` (17)<br>`        TR(2,:,I) = E(:,2)` (18)<br>`      ENDDO` (20) [11-04 전수 검증 정정] |
| 21–35 | 시작 시 1행 루틴 안. SF_AXBT 결과를 두 번째 TR에 복사한다(22–24). SF_LENGTH를 두 번 호출한다(26–27). X0의 각 열의 첫 성분을 0으로 설정한다(29,32). 둘째 성분에는 각각 Y2와 Y3을 설정한다(30,33). 해석: SF_LENGTH의 이름으로 볼 때 Y2와 Y3은 길이에 해당한다. 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      CALL SF_AXBT(T,TR(1,1,2),TR(1,1,1),2,2,2)` (22)<br>`      TR(:,:,2) = T(:,:)` (24)<br>`      CALL SF_LENGTH(Y2,X(1,1),X(1,2),2)` (26)<br>`      CALL SF_LENGTH(Y3,X(1,2),X(1,3),2)` (27)<br>`      X0(1,1) = 0.` (29)<br>`      X0(2,1) = Y2` (30)<br>`      X0(1,2) = 0.` (32)<br>`      X0(2,2) = Y3` (33)<br>`      END` (35) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
