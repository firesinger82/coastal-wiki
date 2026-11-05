---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/blmpn1s.f
lines: 49
sha256: 8490845b73f61ab8d2e6a7a9af562628d4a46eff2916ee68399df3b56a5c0128
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# blmpn1s.f — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | BLMPN1S의 인수와 배열을 선언하고 BL을 0으로 초기화한다. `積分点`은 적분점(integration point), `変換行列`은 변환행렬(transformation matrix)을 뜻한다. 3–4행은 BLS가 BL의 5·6행 성분임을 설명한다. 8행은 IGNL의 0을 미소변형(small deformation), 1을 대변형(large deformation)으로 설명한다. 원문: `      SUBROUTINE BLMPN1S(BLS,DNDX,DUDX,GQD,IGNL)` (1); 주석 원문 `C     BLS  : OUT : BLS(1,:,ig) = [BL]の5行目の成分(積分点ig)` (3); 주석 원문 `C                  BLS(2,:,ig) = [BL]の6行目の成分(積分点ig)` (4); 주석 원문 `C     DNDX : IN  : DNDX(i,j,ig) = ∂Nj/∂xi (積分点ig)` (5); 주석 원문 `C     DUDX : IN  : DUDX(i,j,ig) = ∂uj/∂xi (積分点ig)` (6); 주석 원문 `C     GQD  : IN  : [E] (γyz,γzxの変換行列)` (7); 주석 원문 `C     IGNL : IN  : =0:微小変形, =1:大変形` (8); `      IMPLICIT REAL*8(A-H,O-Z)` (10); `      DIMENSION BLS(2,18,3),DNDX(3,6,3),DUDX(3,3,3),BL(6,18),GQD(6,6)`<br>`     &         ,BLB(6,18)` (11–12); `      BL(:,:) = 0.` (14). |
| 16–40 | 시작 시 1행 BLMPN1S 루틴 안. I=1,3과 J=1,6을 순회하여 BL에 DNDX 성분을 배치한다. 해석: J는 절점 번호이며 BL의 해당 성분은 전단 성분에 해당한다. IGNL이 0이면 현재 절점의 비선형 보정을 건너뛴다. 나머지는 K 루프에서 DUDX와 DNDX의 곱을 더한다. 해석: 5–6행의 N과 u를 형상함수와 변위로 보면 두 배열은 그 공간 미분이다. 원문: `      DO I = 1, 3` (16); `        DO J = 1, 6` (18); `          J0 = 3 * ( J - 1 )` (20); `          BL(I  ,J0+2) = DNDX(3,J,I)` (22); `          BL(I  ,J0+3) = DNDX(2,J,I)` (23); `          BL(I+3,J0+1) = DNDX(3,J,I)` (24); `          BL(I+3,J0+3) = DNDX(1,J,I)` (25); `          IF( IGNL == 0 ) CYCLE` (27); `          DO K = 1, 3` (29); `            BL(I  ,J0+K) = BL(I  ,J0+K)`<br>`     &                     + DUDX(2,K,I) * DNDX(3,J,I)`<br>`     &                     + DUDX(3,K,I) * DNDX(2,J,I)` (30–32); `            BL(I+3,J0+K) = BL(I+3,J0+K)`<br>`     &                     + DUDX(3,K,I) * DNDX(1,J,I)`<br>`     &                     + DUDX(1,K,I) * DNDX(3,J,I)` (33–35); `          ENDDO` (36); `        ENDDO` (38); `      ENDDO` (40). [11-04 전수 검증 정정] |
| 41–49 | 시작 시 1행 BLMPN1S 루틴 안. AXB에 GQD와 BL을 전달하여 BLB를 만들고, 3개 적분점의 두 성분을 BLS에 복사한다. 루틴 끝을 포함한다. 원문: `      CALL AXB(BLB,GQD,BL,6,6,18)` (42); `      DO I = 1, 3` (44); `        BLS(1,:,I) = BLB(I,:)` (45); `        BLS(2,:,I) = BLB(I+3,:)` (46); `      ENDDO` (47); `      END` (49). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–12·16–25·42–46: I 루프 범위는 1,3이다. J 루프 범위는 1,6이다. GQD의 크기는 6×6이다. 3–7행 주석은 세 번째 첨자를 적분점으로 표시한다. 해석: J는 절점 번호에 해당한다. [11-04 전수 검증 정정]
