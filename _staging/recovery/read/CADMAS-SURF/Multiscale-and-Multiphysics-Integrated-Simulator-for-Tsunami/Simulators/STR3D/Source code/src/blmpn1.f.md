---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/blmpn1.f
lines: 37
sha256: 6d932dbe839a52f7d9f3c1f32f29b5da5f7211ba9b744114b72f698a65df1283
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# blmpn1.f — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | BLMPN1의 인수와 배열 크기를 선언한다. 6행의 `微小変形`은 미소변형(small deformation), `大変形`은 대변형(large deformation)을 뜻한다. 해석: 4–5행의 N과 u를 각각 형상함수와 변위로 보면 DNDX와 DUDX는 그 공간 미분이다. 원문: `      SUBROUTINE BLMPN1(BL,DNDX,DUDX,IGNL)` (1); 주석 원문 `C     BL   : OUT : [BL]` (3); 주석 원문 `C     DNDX : IN  : DNDX(i,j) = ∂Nj/∂xi` (4); 주석 원문 `C     DUDX : IN  : DUDX(i,j) = ∂uj/∂xi` (5); 주석 원문 `C     IGNL : IN  : =0:微小変形, =1:大変形` (6); `      IMPLICIT REAL*8(A-H,O-Z)` (8); `      DIMENSION BL(6,3*6),DNDX(3,6),DUDX(3,3)` (9). [11-04 전수 검증 정정] |
| 11–24 | 시작 시 1행 BLMPN1 루틴 안. CLEAR1으로 BL을 초기화한다. J=1,6에서 BL의 1–4행에 DNDX 성분을 배치한다. 해석: J를 절점 번호로 보면 이 대입은 선형 성분 배치에 해당한다. IGNL이 0이면 반환한다. 원문: `      CALL CLEAR1(BL,6*3*6)` (11); `      DO 100 J=1,6` (13); `        J0=3*(J-1)` (15); `        BL(1,J0+1)=DNDX(1,J)` (16); `        BL(2,J0+2)=DNDX(2,J)` (17); `        BL(3,J0+3)=DNDX(3,J)` (18); `        BL(4,J0+1)=DNDX(2,J)` (19); `        BL(4,J0+2)=DNDX(1,J)` (20); `  100 CONTINUE` (22); `      IF(IGNL .EQ. 0) RETURN` (24). [11-04 전수 검증 정정] |
| 25–37 | 시작 시 1행 BLMPN1 루틴 안. 24행에서 반환하지 않은 경우 절점·성분 루프에서 DUDX와 DNDX의 곱을 BL의 1–4행에 더한다. 반환문과 루틴 끝을 포함한다. 원문: `      DO 200 J=1,6` (26); `        J0=3*(J-1)` (27); `        DO 210 K=1,3` (28); `          DO 220 I=1,3` (29); `            BL(I,J0+K)=BL(I,J0+K)+DUDX(I,K)*DNDX(I,J)` (30); `  220     CONTINUE` (31); `          BL(4,J0+K)=BL(4,J0+K)+DUDX(1,K)*DNDX(2,J)+DUDX(2,K)*DNDX(1,J)` (32); `  210   CONTINUE` (33); `  200 CONTINUE` (34); `      RETURN` (36); `      END` (37). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9·11·16–20·30–32: BL의 첫 번째 차원은 6이다. CLEAR1 호출 뒤의 대입은 BL의 1–4행에만 있다.
