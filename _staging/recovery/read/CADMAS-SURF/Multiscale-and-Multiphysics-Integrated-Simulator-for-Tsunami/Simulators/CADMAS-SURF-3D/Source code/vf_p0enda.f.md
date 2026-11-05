---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p0enda.f
lines: 27
sha256: 4b03caedf97a116e80e13d70f2ee456f7d54de3894b28a1b300fb654b769777f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_p0enda.f — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 병렬 환경 비정상 종료 루틴의 암시적 형식을 선언한다. 원문: `      SUBROUTINE VF_P0ENDA()` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_P0ENDA:並列環境を異常終了する` (5) (병렬 환경을 비정상 종료한다). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형식). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C==== 実行 ===========================================================` (12) (실행). |
| 14–27 | 시작 시 1행 루틴 `SUBROUTINE VF_P0ENDA` 안. VF_ZXMG_ABORT(IERR) 호출 뒤 VF_ZXMG_FINAL(IERR)을 호출하고 반환하도록 작성되어 있다. 원문: `C     -- 異常終了する --` (14) (비정상 종료한다). `      CALL VF_ZXMG_ABORT(IERR)` (15). `C     -- 終了する --` (17) (종료한다). `      CALL VF_ZXMG_FINAL(IERR)` (18). `C     -- 実行文の終了 --` (20) (실행문 종료). `      GOTO 9999` (21). `C==== 終了 ===========================================================` (23) (종료). ` 9999 CONTINUE` (25). `      RETURN` (26). `      END` (27). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–18: VF_ZXMG_ABORT 뒤에 VF_ZXMG_FINAL 호출문이 있다. VF_ZXMG_ABORT 내부의 반환 여부는 이 파일에서 확인하지 않았다.
