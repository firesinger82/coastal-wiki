---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_iihidm.f
lines: 50
sha256: b1f2429dae308ad500d286c9b710415f375c2db2aa053dff4343bf89cc564dc4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_iihidm.f — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | VF_IIHIDM의 선언이다. mod_dem을 사용하고 HIDEM 결합(coupling) 제어 명령의 단어 위치와 문자열을 받는다.<br>`      SUBROUTINE VF_IIHIDM(IS,IE,NWD,TEXT)` (1)<br>`CD=== 概要 ===========================================================` (3) (개요)<br>`CDT   VF_IIHIDM:HiDEMプログラムとの連成制御データ(HIDEM)を解釈する` (5) (HiDEM 프로그램과의 결합 제어 데이터 HIDEM 해석)<br>`C==== 宣言 ===========================================================` (7) (선언)<br>`      use mod_dem` (9)<br>`C     -- 大域型 --` (11) (전역 형)<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (12)<br>`C     -- 大域変数 --` (14) (전역 변수)<br>`      INCLUDE 'VF_A0PRM.h'` (15)<br>`CD    -- 引数 --` (17) (인수)<br>`CD    IS(MAXWDS) : IN  : I*4   : n番目の単語の開始位置` (18) (n번째 단어 시작 위치)<br>`CD    IE(MAXWDS) : IN  : I*4   : n番目の単語の終了位置` (19) (n번째 단어 종료 위치)<br>`CD    NWD        : IN  : I*4   : 単語の数` (20) (단어 수)<br>`CD    TEXT       : IN  : C*(*) : 入力した文字列` (21) (입력 문자열)<br>`      DIMENSION IS(MAXWDS),IE(MAXWDS)` (22)<br>`      CHARACTER*(MAXCHR) TEXT` (23)<br>`C==== 実行 ===========================================================` (25) (실행) |
| 27–50 | 시작 시 1행 VF_IIHIDM 안. NWD>=2를 검사한다. YES이면 IHIDEM=1, NO이면 IHIDEM=0이다. 나머지는 VF_A2ERR를 호출한다.<br>`CD    -- 単語数のチェック --` (27) (단어 수 검사)<br>`      IF (NWD.LT.2) CALL VF_A2ERR('VF_IIPARA','SYNTAX ERROR.')` (28)<br>`CD    -- HIDEM YESを解釈する --` (30) (HIDEM YES 해석)<br>`      IF     (TEXT(IS(2):IE(2)).EQ.'YES') THEN` (31)<br>`        IHIDEM=1` (32)<br>`CD    -- HIDEM NOを解釈する --` (34) (HIDEM NO 해석)<br>`      ELSE IF(TEXT(IS(2):IE(2)).EQ.'NO') THEN` (35)<br>`        IHIDEM=0` (36)<br>`CD    -- 解釈できない単語によるエラー --` (38) (해석할 수 없는 단어 오류)<br>`      ELSE` (39)<br>`        CALL VF_A2ERR('VF_IIPARA','UNKNOWN WORD.')` (40)<br>`      ENDIF` (41)<br>`C     -- 実行文の終了 --` (43) (실행문 종료)<br>`      GOTO 9999` (44)<br>`C==== 終了 ===========================================================` (46) (종료)<br>` 9999 CONTINUE` (48)<br>`      RETURN` (49)<br>`      END` (50) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28·40: VF_A2ERR의 루틴명 문자열은 VF_IIHIDM이 아니라 VF_IIPARA이다.
