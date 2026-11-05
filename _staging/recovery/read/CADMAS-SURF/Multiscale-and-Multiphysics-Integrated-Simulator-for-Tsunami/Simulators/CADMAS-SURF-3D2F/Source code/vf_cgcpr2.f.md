---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_cgcpr2.f
lines: 36
sha256: 9c34d2660d67c0e2903de7f20917891b52c9b9edb2873f0680ed3fbcba634fe8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cgcpr2.f — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 이동 장애물용 2차원 경계값 배열 복사 루틴이다. 두 배열의 두 번째 차원은 3이다(18).<br>`      SUBROUTINE VF_CGCPR2(AA,BB,N1,N2)` (1).<br>`CD=== 概要 ===========================================================` (3) (개요).<br>`CDT   VF_CGCPR2:境界値の2次元配列を複写する（移動障害物処理用）` (5) (VF_CGCPR2:경계값 2차원 배열 복사(이동 장애물 처리용)).<br>`C==== 宣言 ===========================================================` (7) (선언).<br>`C     -- 大域型 --` (9) (전역 형).<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10).<br>`C     -- 大域変数 --` (12) (전역 변수).<br>`      INCLUDE 'VF_ANUMBI.h'` (13).<br>`CD    -- 引数 --` (15) (인수).<br>`CD    AA(N1,3) : OUT : R*8 : 2次元配列(複写先)` (16) (AA(N1,3) : OUT : R*8 : 2차원 배열(복사 대상)).<br>`CD    BB(N2,3) : IN  : R*8 : 2次元配列(複写基)` (17) (BB(N2,3) : IN  : R*8 : 2차원 배열(복사 원본)).<br>`      DIMENSION AA(N1,3),BB(N2,3)` (18).<br>`C==== 実行 ===========================================================` (20) (실행). |
| 21–36 | 시작 시 1행 SUBROUTINE VF_CGCPR2 루틴 안. NUMB0개 행의 세 열을 각각 BB에서 AA로 복사하고 종료한다(23–36).<br>`CD    -- 配列の全要素に代入 --` (22) (배열 전체 요소에 대입).<br>`      DO 100 L=1,NUMB0` (23).<br>`        AA(L,1)=BB(L,1)` (24).<br>`        AA(L,2)=BB(L,2)` (25).<br>`        AA(L,3)=BB(L,3)` (26).<br>` 100  CONTINUE` (27).<br>`C     -- 実行文の終了 --` (29) (실행문 종료).<br>`      GOTO 9999` (30).<br>`C==== 終了 ===========================================================` (32) (종료).<br>` 9999 CONTINUE` (34).<br>`      RETURN` (35).<br>`      END` (36). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18·23: 배열 첫 번째 차원은 N1·N2이지만 복사 상한은 NUMB0이다. 이 루틴에는 세 크기를 대조하는 검사가 없다.
