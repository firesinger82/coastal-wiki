---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/psfwt.f
lines: 12
sha256: 275fc63e310edbfa1061e7970b3f4d4f01fcf85739f0b11951d725c844fecbe9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# psfwt.f — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | PSFWT의 인수와 암시적 형(implicit typing)을 선언한다(1–3). 무조건 RETURN을 실행한다(5). 구분 주석을 포함한다. 원문: `      SUBROUTINE PSFWT(IST,P1,P2,ISTEP,NSTEP,ITER,IFL)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      RETURN` (5). |
| 7–12 | 시작 시 1행 PSFWT 루틴 안. 5행 RETURN 뒤에 REWIND(IFL), IST·P1·P2·ISTEP·NSTEP·ITER의 WRITE와 쉼표로 구분하는 FORMAT이 남아 있다(7–10). 이 부분은 주석 처리된 코드가 아니다. 주석·END를 포함한다. 원문: `      REWIND(IFL)` (7); `      WRITE(IFL,1000) IST,P1,P2,ISTEP,NSTEP,ITER` (9); ` 1000 FORMAT(I1,',',F5.2,',',F5.2,',',I8,',',I8,',',I8)` (10); `      END` (12). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5–10: 유일한 루틴 입구(1)에서 무조건 RETURN(5)을 먼저 실행하므로 뒤의 REWIND·WRITE에 도달하는 실행 경로는 없다.
