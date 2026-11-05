---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Count_data/tb_end.f
lines: 19
sha256: 79e5155b39d63ee81042b0dbc543bf708deba0558de9d8bd18f74fa6ea00715a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# tb_end.f — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | TB_END는 LOGICAL ENDT와 80자 CHAR를 선언한다(1–4). 6·7행 중첩 루프(loop)가 8·9행 식으로 8자 필드(field)를 선택한다. ENDT 호출 결과가 참이면 바깥 루프 인덱스 I를 N으로 반환한다(10–12). 검출하지 못하면 N=4이다(17). 원문: `      SUBROUTINE TB_END( N, CHAR )` (1); `      LOGICAL ENDT` (3); `      CHARACTER*80 CHAR` (4); `      DO I = 0, 3` (6); `        DO J = 0, 1` (7); `          IS = 8 + 16 * I + 8 * J + 1` (8); `          IE = IS + 7` (9); `          IF( ENDT( CHAR(IS:IE) ) ) THEN` (10); `            N = I` (11); `            RETURN` (12); `          ENDIF` (13); `        ENDDO` (14); `      ENDDO` (15); `      N = 4` (17); `      END` (19). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10–12: 안쪽 루프 인덱스 J와 관계없이 N에는 바깥 루프 인덱스 I를 대입한다.
