---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/dirupdt.f
lines: 46
sha256: 51063304d125363a96d8f0429eedd823bd2b52023cb81520ab5e5ae938850735
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# dirupdt.f — 판독 구간 기록

구간은 1행부터 46행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | DIRUPDT의 벡터와 행렬 작업 배열을 선언한다. 해석: R은 회전행렬로 사용된다. DATA E는 3×3 단위행렬(identity matrix)이다. 원문: `      SUBROUTINE DIRUPDT(VG,VG0,NP,DUG,IGNL)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION THETA(3),NP(2),DUG(6,*),V(3,2),DV(3,2),VG(3,2,2)`<br>`     &         ,VG0(3,2,2),R(3,3),E(3,3),P(3,3),P2(3,3)` (4–5); `      DATA E / 1.D0, 0.D0, 0.D0,`<br>`     &         0.D0, 1.D0, 0.D0, `<br>`     &         0.D0, 0.D0, 1.D0 / ` (6–8); 주석 원문 `C-----------------------------------------------------------------------` (9). [11-04 전수 검증 정정] |
| 10–25 | 시작 시 1행 DIRUPDT 루틴 안. K=1,2에서 DUG(4:6,NP(K))를 THETA에 복사한다. 내적의 제곱근으로 OMEGA를 계산한다. OMEGA가 0이면 현재 K 반복을 건너뛴다. 해석: NP(K)는 절점 번호이며 THETA는 회전 벡터이다. 그 외에는 반대칭행렬(skew-symmetric matrix) P를 구성한다. 원문: `      DO K = 1, 2` (10); `        THETA(:) = DUG(4:6,NP(K))` (12); `        OMEGA = DSQRT( DOT_PRODUCT(THETA,THETA) )` (14); `        IF( OMEGA == 0. ) CYCLE` (16); `        P(:,:) = 0.` (18); `        P(1,2) = -THETA(3)` (19); `        P(1,3) =  THETA(2)` (20); `        P(2,3) = -THETA(1)` (21); `        P(2,1) = -P(1,2)` (22); `        P(3,1) = -P(1,3)` (23); `        P(3,2) = -P(2,3)` (24). [11-04 전수 검증 정정] |
| 26–46 | 시작 시 10행 `      DO K = 1, 2` 안이다. 이 루프는 44행 `      ENDDO`에서 닫힌다. IGNL이 양수이면 AXB(P2,P,P,3,3,3)를 호출한다. 사인 계수로 R을 계산한다. VG를 V에 복사한 뒤 AXB(VG(1,1,K),R,V,3,3,2)를 호출한다. ELSE에서는 AXB(DV,P,VG0(1,1,K),3,3,2)를 호출한 뒤 DV를 VG에 더한다. 해석: AXB가 행렬 곱을 수행한다면 양수 분기는 VG를 회전하며 ELSE 분기는 P와 VG0의 곱을 더한다. 분기·루프·루틴 끝을 포함한다. 원문: `        IF( IGNL > 0 ) THEN` (26); `          CALL AXB(P2,P,P,3,3,3)` (28); `          R(:,:) = E(:,:) + DSIN(OMEGA)/OMEGA*P(:,:) `<br>`     &             + .5D0*( DSIN(.5D0*OMEGA) / (.5D0*OMEGA) )**2.D0`<br>`     &               *P2(:,:)` (30–32); `          V(:,:) = VG(:,:,K)` (34); `          CALL AXB(VG(1,1,K),R,V,3,3,2)` (35); `        ELSE` (37); `          CALL AXB(DV,P,VG0(1,1,K),3,3,2)` (39); `          VG(:,:,K) = VG(:,:,K) + DV(:,:)` (40); `        ENDIF` (42); `      ENDDO` (44); `      END` (46). [11-04 전수 검증 보완] [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16·30–32: OMEGA=0일 때는 회전 계산을 건너뛴다. 0 이외의 OMEGA에 별도 작은 값 기준은 없다.
