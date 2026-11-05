---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Count_data/Ct_PLOAD2.f
lines: 17
sha256: 4650b561a87d52ad7896e48c2ab3c1bf8b54cbc8ad01f18b47fac9a457a9524d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Ct_PLOAD2.f — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 논리형 THRU·80자 CHAR·IDE(6)를 선언한다(3–5). CHAR(33:40)에 대한 THRU 호출이 참이면 N_PL4를 1 늘린다(7–8). ELSE는 6개 요소 번호(element ID)를 읽어 I=1..6에서 첫 0 앞까지 개수를 늘린다(9–15). 원문: `      SUBROUTINE CT_PLOAD2( N_PL4, CHAR )` (1); `      LOGICAL THRU` (3); `      CHARACTER*80 CHAR` (4); `      DIMENSION IDE(6)` (5); `      IF( THRU( CHAR(33:40) ) ) THEN` (7); `        N_PL4 = N_PL4 + 1` (8); `      ELSE` (9); `        READ(CHAR,'(BN,24X,6I8)') IDE(:)` (10); `        DO I = 1, 6` (11); `          IF( IDE(I) == 0 ) EXIT` (12); `          N_PL4 = N_PL4 + 1` (13); `        ENDDO` (14); `      ENDIF` (15); `      END` (17). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–13: THRU 참 분기는 지정 범위 길이를 계산하지 않고 N_PL4에 1을 더한다.
