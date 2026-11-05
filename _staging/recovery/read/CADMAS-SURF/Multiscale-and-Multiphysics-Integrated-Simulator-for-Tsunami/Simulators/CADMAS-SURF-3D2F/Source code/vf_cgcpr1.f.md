---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_cgcpr1.f
lines: 34
sha256: feceb38ade08975b2b497e246a2562d433ae01da58b81fce9ed1172db6b1bdc1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cgcpr1.f — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 이동 장애물용 1차원 경계값 배열 복사 루틴과 선언이다(1–18).<br>`      SUBROUTINE VF_CGCPR1(AA,BB,N1,N2)` (1).<br>`CD=== 概要 ===========================================================` (3) (개요).<br>`CDT   VF_CGCPR1:境界値の1次元配列を複写する（移動障害物処理用）` (5) (VF_CGCPR1:경계값 1차원 배열 복사(이동 장애물 처리용)).<br>`C==== 宣言 ===========================================================` (7) (선언).<br>`C     -- 大域型 --` (9) (전역 형).<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10).<br>`C     -- 大域変数 --` (12) (전역 변수).<br>`      INCLUDE 'VF_ANUMBI.h'` (13).<br>`CD    -- 引数 --` (15) (인수).<br>`CD    AA(N1) : OUT : R*8 : 1次元配列(複写先)` (16) (AA(N1) : OUT : R*8 : 1차원 배열(복사 대상)).<br>`CD    BB(N2) : IN  : R*8 : 1次元配列(複写基)` (17) (BB(N2) : IN  : R*8 : 1차원 배열(복사 원본)).<br>`      DIMENSION AA(N1),BB(N2)` (18).<br>`C==== 実行 ===========================================================` (20) (실행). |
| 21–34 | 시작 시 1행 SUBROUTINE VF_CGCPR1 루틴 안. NUMB0개 경계값을 BB에서 AA로 복사하고 종료한다(23–34).<br>`CD    -- 配列の全要素に代入 --` (22) (배열 전체 요소에 대입).<br>`      DO 100 L=1,NUMB0` (23).<br>`        AA(L)=BB(L)` (24).<br>` 100  CONTINUE` (25).<br>`C     -- 実行文の終了 --` (27) (실행문 종료).<br>`      GOTO 9999` (28).<br>`C==== 終了 ===========================================================` (30) (종료).<br>` 9999 CONTINUE` (32).<br>`      RETURN` (33).<br>`      END` (34). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18·23: 배열 길이는 N1·N2로 선언하지만 복사 상한은 NUMB0이다. 이 루틴에는 세 크기를 대조하는 검사가 없다.
