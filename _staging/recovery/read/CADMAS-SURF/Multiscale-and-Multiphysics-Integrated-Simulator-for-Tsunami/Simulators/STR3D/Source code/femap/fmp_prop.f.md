---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/femap/fmp_prop.f
lines: 25
sha256: b2bdd06592f77c4c5cac4b9623d6dfb0b571f7a0c7ae76c82a05da1743552ac5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fmp_prop.f — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | FMP_PROP는 ID·유형 ITYP를 속성 헤더에 넣고 WT_DATA에 넘긴다. 다음 줄은 ID이며 이후 레코드는 원문의 고정 정수·실수 문자열이다. 조건문·루프·물리량 계산식은 없다. 원문: `      SUBROUTINE FMP_PROP(ID,ITYP,IFL)` (1); `      CHARACTER*200 CHAR` (3); `      WRITE(CHAR,'(6I4)') ID,124,ID,ITYP,1,0` (5); `      CALL WT_DATA(CHAR,IFL)` (7); `      WRITE(IFL,'(I0)') ID` (9); `      WRITE(IFL,'(A)') '0,0,0,0,'` (11); `      WRITE(IFL,'(A)') '1,'` (13); `      WRITE(IFL,'(A)') '0,'` (15); `      WRITE(IFL,'(A)') '1,'` (17); `      WRITE(IFL,'(A)') '0.,'` (19); `      WRITE(IFL,'(A)') '0,'` (21); `      WRITE(IFL,'(A)') '0,'` (23); `      END` (25) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5: 속성 헤더에 같은 ID를 첫 번째와 세 번째 필드로 기록한다.
