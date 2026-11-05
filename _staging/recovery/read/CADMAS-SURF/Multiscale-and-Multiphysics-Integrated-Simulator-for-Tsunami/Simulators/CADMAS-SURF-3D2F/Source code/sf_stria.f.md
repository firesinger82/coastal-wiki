---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_stria.f
lines: 16
sha256: 1a4877251232570360eb3afdc099638e9889dd8438beae142cad97f08d4d27dc
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_stria.f — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 해석: 이름과 계산식으로 볼 때 삼각형 면적 계산이다. 8–12행 분기에는 ELSE가 없다. 따라서 N이 2도 3도 아니면 이 분기에서 S를 설정하지 않고 13행 `S = S*.5D0`을 수행한다. 암시적 실수 및 COOD(N,3), V12(3), V13(3)을 선언한다(1–4). 두 변 벡터를 구한다(6–7). N=3이면 SF_CROSS1, N=2이면 평면 행렬식 절댓값을 구한 뒤 S를 절반으로 만든다(8–13). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      SUBROUTINE SF_STRIA(S,COOD,N)` (1)<br>`C` (2)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      DIMENSION COOD(N,3),V12(3),V13(3)` (4)<br>`C-----------------------------------------------------------------------` (5)<br>`      V12(1:N) = COOD(1:N,2) - COOD(1:N,1)` (6)<br>`      V13(1:N) = COOD(1:N,3) - COOD(1:N,1)` (7)<br>`      IF( N .EQ. 3 ) THEN` (8)<br>`        CALL SF_CROSS1(V12,V13,S)` (9)<br>`      ELSEIF( N .EQ. 2 ) THEN` (10)<br>`        S = DABS( V12(1)*V13(2) - V12(2)*V13(1) )` (11)<br>`      ENDIF` (12)<br>`      S = S*.5D0` (13)<br>`C` (14)<br>`      RETURN` (15)<br>`      END` (16) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–13: N이 2 또는 3이 아닐 때 S를 설정하는 분기는 없다. S*.5D0 계산은 분기 밖에 있다.
