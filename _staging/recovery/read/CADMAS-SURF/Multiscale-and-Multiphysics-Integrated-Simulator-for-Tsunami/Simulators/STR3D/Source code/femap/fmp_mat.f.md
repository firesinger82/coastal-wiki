---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/femap/fmp_mat.f
lines: 21
sha256: 5496d5107d35e58e2ef365a36117739c95760612f2cd43fcc13dc02471a50a16
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fmp_mat.f — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | FMP_MAT는 ID와 고정 필드로 재료 헤더를 작성하고 WT_DATA로 내보낸다. ID 레코드 뒤 WT_ZERO_I로 10·25개 정수 영값, WT_ZERO_R로 200개 실수 영값, 다시 WT_ZERO_I로 50·70개 정수 영값을 기록한다. 원문: `      SUBROUTINE FMP_MAT(ID,IFL)` (1); `      CHARACTER*200 CHAR` (3); `      WRITE(CHAR,'(7I5)') ID,-601,124,0,0,1,0` (5); `      CALL WT_DATA(CHAR,IFL)` (7); `      WRITE(IFL,'(I0)') ID` (9); `      CALL WT_ZERO_I(10,IFL)` (11); `      CALL WT_ZERO_I(25,IFL)` (13); `      CALL WT_ZERO_R(200,IFL)` (15); `      CALL WT_ZERO_I(50,IFL)` (17); `      CALL WT_ZERO_I(70,IFL)` (19); `      END` (21) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5–19: 이 루틴의 입력은 ID·IFL이며 재료의 물리 상수 인수는 없다. 나머지 필드는 고정 헤더와 영값 출력 호출로 구성한다.
