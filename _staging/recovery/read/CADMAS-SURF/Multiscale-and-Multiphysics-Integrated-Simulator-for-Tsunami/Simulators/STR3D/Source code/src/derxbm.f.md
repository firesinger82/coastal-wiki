---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/derxbm.f
lines: 30
sha256: c523e4aace8ebd22e291e795c3a5db51e5564b2fb8dc1c104fc8b721df7ede14
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# derxbm.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | DERXBM의 암시적 형과 BX·UX·U·VS·VT·AS·AT의 크기를 선언한다. 해석: U·VS·VT의 두 열은 두 절점에 대응하며 AS·AT는 변환 배열이다. 원문: `      SUBROUTINE DERXBM(BX,UX,S,T,RL,D1,D2,U,VS,VT,AS,AT)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION BX(3,12),UX(3),U(3,2),VS(3,2),VT(3,2),AS(3,3,2)`<br>`     &         ,AT(3,3,2)` (4–5). [11-04 전수 검증 정정] |
| 7–22 | 시작 시 1행 DERXBM 루틴 안. BX를 0으로 초기화한다. BX(1,1)·BX(2,2)·BX(3,3)에 -1을 배치한다. BX(1,7)·BX(2,8)·BX(3,9)에 1을 배치한다. BX의 4:6열과 10:12열을 S·T·D1·D2 및 AS·AT로 계산한다. 해석: 이 열 구분은 양 끝 절점의 병진 성분과 회전 성분에 해당한다. 전체 BX를 RL로 나눈다. 원문: `      BX(:,:) = 0.` (7); `      BX(1,1) = -1.D0` (9); `      BX(2,2) = -1.D0` (10); `      BX(3,3) = -1.D0` (11); `      BX(:,4:6) = -.5D0 * ( S * D1 * AS(:,:,1) + T * D2 * AT(:,:,1) )` (13); `      BX(1,7) = 1.D0` (15); `      BX(2,8) = 1.D0` (16); `      BX(3,9) = 1.D0` (17); `      BX(:,10:12) = .5D0 * ( S * D1 * AS(:,:,2) + T * D2 * AT(:,:,2) )` (19); `      BX(:,:) = BX(:,:) / RL` (21). [11-04 전수 검증 정정] |
| 23–30 | 시작 시 1행 DERXBM 루틴 안. 두 절점 U·VS·VT 차이를 결합하여 UX를 계산하고 RL로 나눈다. 연속행·루틴 끝·끝의 빈 줄을 포함한다. 원문: `      UX(:) = -U(:,1) + U(:,2) + S * .5D0 * D1 * ( -VS(:,1) + VS(:,2) )`<br>`     &                         + T * .5D0 * D2 * ( -VT(:,1) + VT(:,2) )` (23–24); `      UX(:) = UX(:) / RL` (26); `      END` (28). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 21·26: BX와 UX를 RL로 나누기 전에 RL=0을 검사하는 조건문은 없다.
