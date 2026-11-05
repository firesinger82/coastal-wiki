---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/ncrset2.f
lines: 30
sha256: 0b33f54f07fec7350176fac898656657ee4bdd843dc31143ab54c9caaca36069
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ncrset2.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | NCRSET2의 배열 선언과 요소 수 추출 구간이다. NCRMAX를 초기화하고 전체 요소를 순회한다. NELMC에 해당하는 가운데 구간은 CYCLE한다. ITYP가 1 또는 4이면 NDF=6, ELSE이면 NDF=3으로 하여 ND*NDF의 최댓값을 갱신한다. 원문: `      SUBROUTINE NCRSET2(KK,IELM,NM)` (1)； `      DIMENSION KK(*),IELM(NM,*)` (3)； `C     ----- NCRMAX, NESTF -----` (5)； `      NELM = KK(12)` (7)； `      NELMC = KK(29)` (8)； `      NELMX = KK(32)` (9)； `      NCRMAX = 0` (11)； `      DO I = 1, NELM + NELMC + NELMX` (13)； `        IF( I > NELM .AND. I <= NELM + NELMC ) CYCLE` (14)； `        ITYP = IELM(2,I)` (15)； `        IF( ITYP == 1 .OR. ITYP == 4 ) THEN` (16)； `          NDF = 6` (17)； `        ELSE` (18)； `          NDF = 3` (19)； `        ENDIF` (20)； `        ND = IELM(3,I)` (21)； `        NCRMAX = MAX0( NCRMAX, ND*NDF )` (22)； `      ENDDO` (23)。 |
| 25–30 | 시작 시 1행 NCRSET2 루틴 안이며 13행 요소 루프 밖이다. NCRMAX로 `NESTF = ( NCRMAX + 1 ) * NCRMAX / 2`를 계산한다. 해석: NESTF는 대칭행렬 상삼각(upper triangle) 저장 크기이다. KK(33)에 NESTF, KK(34)에 NCRMAX를 저장한다. 원문: `      NESTF = ( NCRMAX + 1 ) * NCRMAX / 2` (25)； `      KK(33) = NESTF` (27)； `      KK(34) = NCRMAX` (28)； `      END` (30)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1–30: 이 파일에는 IMPLICIT 선언이 없다.
- 13–25: 모든 요소가 건너뛰어지거나 반복이 실행되지 않으면 NCRMAX는 초기값 0이며 NESTF도 0으로 계산된다.
