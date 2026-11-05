---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/VF_ASTOCR.h
lines: 20
sha256: 15ecbd357530d6700939faf7fb6fc76fd3fd5ae65e17c13ea6f536c6b18514af
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_ASTOCR.h — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | STOC가 주는 서·동·남·북 경계 배열을 REAL(8)로 선언한다. 서·동 배열은 (MAX_NJST,MAX_NKST,4), 남·북 배열은 (MAX_NIST,MAX_NKST,4)이다. 마지막 첨자는 면 중심 U·V·W·F값 순서이다. 원문: `      REAL(8):: UWST(MAX_NJST,MAX_NKST,4),UEST(MAX_NJST,MAX_NKST,4)` (1); `      REAL(8):: VSST(MAX_NIST,MAX_NKST,4),VNST(MAX_NIST,MAX_NKST,4)` (2); `      COMMON /VF_ASTOCR/UWST,UEST,VSST,VNST` (3); `CD=== 概要 ===========================================================` (5) (개요); `CDT   VF_ASTOCR.h:CADMAS-STOC連成関連:実数` (7) (CADMAS-STOC 연성 관련 실수); `C==== 内容 ===========================================================` (9) (내용); `CD    -- STOCとCADMASの境界条件に関する変数 --` (11) (STOC와 CADMAS 경계조건 변수); `CD    UWST(NJST,NKST,4): TRN : R*8 : STOCから受け取る西側境界値` (12) (STOC에서 받는 서쪽 경계값); `CD    UEST(NJST,NKST,4): TRN : R*8 : STOCから受け取る東側境界値` (13) (STOC에서 받는 동쪽 경계값); `CD    VSST(NIST,NKST,4): TRN : R*8 : STOCから受け取る南側境界値` (14) (STOC에서 받는 남쪽 경계값); `CD    VNST(NIST,NKST,4): TRN : R*8 : STOCから受け取る北側境界値` (15) (STOC에서 받는 북쪽 경계값); `CD                                   上記4配列の内容は全て以下の通り` (16) (네 배열은 모두 아래 내용을 가짐); `CD                                   (*,*,1)：境界面の面中心の流速U` (17) (경계면 중심 유속 U); `CD                                   (*,*,2)：境界面の面中心の流速V` (18) (경계면 중심 유속 V); `CD                                   (*,*,3)：境界面の面中心の流速W` (19) (경계면 중심 유속 W); `CD                                   (*,*,4)：境界面の面中心のF値` (20) (경계면 중심 F값). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
