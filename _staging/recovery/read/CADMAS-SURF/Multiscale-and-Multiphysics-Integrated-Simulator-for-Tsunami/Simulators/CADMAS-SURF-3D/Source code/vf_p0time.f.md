---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p0time.f
lines: 25
sha256: 8b618efe1fae9b7ecc7420ccdc7f35b0f7f72fe6b95d279b4786b1ae56d3ad3e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_p0time.f — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 경과시간(elapsed time) 루틴의 암시적 형식을 선언한다. 원문: `      SUBROUTINE VF_P0TIME(PT)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_P0TIME:経過時間を得る` (5) (경과시간(elapsed time)을 구한다). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형식). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C==== 実行 ===========================================================` (12) (실행). |
| 14–25 | 시작 시 1행 루틴 `SUBROUTINE VF_P0TIME` 안. PT를 0.0D0으로 설정한 뒤 VF_ZXMG_WTIME(PT)을 호출하고 반환한다. 원문: `C     -- 経過時間を得る --` (14) (경과시간(elapsed time)을 구한다). `      PT=0.0D0` (15). `      CALL VF_ZXMG_WTIME(PT)` (16). `C     -- 実行文の終了 --` (18) (실행문 종료). `      GOTO 9999` (19). `C==== 終了 ===========================================================` (21) (종료). ` 9999 CONTINUE` (23). `      RETURN` (24). `      END` (25). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
