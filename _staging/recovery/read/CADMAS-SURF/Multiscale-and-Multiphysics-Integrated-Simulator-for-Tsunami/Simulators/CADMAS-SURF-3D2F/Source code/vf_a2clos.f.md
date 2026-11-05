---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_a2clos.f
lines: 36
sha256: e777fb24507920170db072dc046049b0400471874db74d2167c82bba074e96ac
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_a2clos.f — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | VF_A2CLOS 시작. 일본어 주석 뜻: 개요(3), 파일 닫기(5), 선언(7), 전역형(9), 전역 변수(12), 실행(16). IMPLICIT 및 두 INCLUDE를 적는다(10·13–14). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      SUBROUTINE VF_A2CLOS()` (1)<br>`CD=== 概要 ===========================================================` (3)<br>`CDT   VF_A2CLOS:ファイルをクローズする` (5)<br>`C==== 宣言 ===========================================================` (7)<br>`C     -- 大域型 --` (9)<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10)<br>`C     -- 大域変数 --` (12)<br>`      INCLUDE 'VF_A0PRM.h'` (13)<br>`      INCLUDE 'VF_AFILEI.h'` (14)<br>`C==== 実行 ===========================================================` (16) |
| 17–36 | 시작 시 1행 루틴 안. 일본어 주석 뜻: 열린 파일 닫기(18), 실행문 종료(29), 종료(32). 아홉 파일 단위 번호가 0이 아닐 때 각각 CLOSE하고 9999로 이동하여 반환한다(19–35). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `CD    -- オープンされているファイルをクローズする --` (18)<br>`      IF (IINFIL.NE.0) CLOSE(IINFIL)` (19)<br>`      IF (IMTFIL.NE.0) CLOSE(IMTFIL)` (20)<br>`      IF (IREFIL.NE.0) CLOSE(IREFIL)` (21)<br>`      IF (IPRFIL.NE.0) CLOSE(IPRFIL)` (22)<br>`      IF (ILPFIL.NE.0) CLOSE(ILPFIL)` (23)<br>`      IF (IGRFIL.NE.0) CLOSE(IGRFIL)` (24)<br>`      IF (IRSFIL.NE.0) CLOSE(IRSFIL)` (25)<br>`      IF (ITRFIL.NE.0) CLOSE(ITRFIL)` (26)<br>`      IF (ITPFIL.NE.0) CLOSE(ITPFIL)` (27)<br>`C     -- 実行文の終了 --` (29)<br>`      GOTO 9999` (30)<br>`C==== 終了 ===========================================================` (32)<br>` 9999 CONTINUE` (34)<br>`      RETURN` (35)<br>`      END` (36) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–27: 조건부 CLOSE 대상은 IINFIL·IMTFIL·IREFIL·IPRFIL·ILPFIL·IGRFIL·IRSFIL·ITRFIL·ITPFIL이다.
