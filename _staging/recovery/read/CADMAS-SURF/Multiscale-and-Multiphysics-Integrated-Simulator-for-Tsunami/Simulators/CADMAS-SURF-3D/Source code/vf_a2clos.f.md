---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_a2clos.f
lines: 37
sha256: a3662fdcbb5488714f304584cd7de7a6ca6dc3efb83bed44252119da0f531e87
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_a2clos.f — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | VF_A2CLOS의 IMPLICIT와 공통 상수·파일 번호 INCLUDE 선언이다. 원문: `      SUBROUTINE VF_A2CLOS()` (1); `CD=== 概要 ===========================================================` (3) (개요); `CDT   VF_A2CLOS:ファイルをクローズする` (5) (파일 닫기); `C==== 宣言 ===========================================================` (7) (선언); `C     -- 大域型 --` (9) (전역 형); `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10); `C     -- 大域変数 --` (12) (전역 변수); `      INCLUDE 'VF_A0PRM.h'` (13); `      INCLUDE 'VF_AFILEI.h'` (14). |
| 16–29 | 1행 VF_A2CLOS 안. 각 파일 번호 IENFIL·IINFIL·IMTFIL·IMTFIL2·IREFIL·IPRFIL·ILPFIL·IGRFIL·IRSFIL·ITRFIL이 0이 아니면 CLOSE한다. 각 IF는 독립 조건이다. 원문: `C==== 実行 ===========================================================` (16) (실행); `CD    -- オープンされているファイルをクローズする --` (18) (열린 파일 닫기); `      IF (IENFIL.NE.0) CLOSE(IENFIL)` (19); `      IF (IINFIL.NE.0) CLOSE(IINFIL)` (20); `      IF (IMTFIL.NE.0) CLOSE(IMTFIL)` (21); `      IF (IMTFIL2.NE.0) CLOSE(IMTFIL2)` (22); `      IF (IREFIL.NE.0) CLOSE(IREFIL)` (23); `      IF (IPRFIL.NE.0) CLOSE(IPRFIL)` (24); `      IF (ILPFIL.NE.0) CLOSE(ILPFIL)` (25); `      IF (IGRFIL.NE.0) CLOSE(IGRFIL)` (26); `      IF (IRSFIL.NE.0) CLOSE(IRSFIL)` (27); `      IF (ITRFIL.NE.0) CLOSE(ITRFIL)` (28). |
| 30–37 | 1행 VF_A2CLOS 안. 9999로 이동하여 RETURN·END로 끝난다. 원문: `C     -- 実行文の終了 --` (30) (실행문 종료); `      GOTO 9999` (31); `C==== 終了 ===========================================================` (33) (종료); ` 9999 CONTINUE` (35); `      RETURN` (36); `      END` (37). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–28: CLOSE 뒤 파일 번호를 0으로 되돌리는 대입은 없다.
- 19–28: 이 루틴의 CLOSE 목록에는 IMMFIL이 없다.
