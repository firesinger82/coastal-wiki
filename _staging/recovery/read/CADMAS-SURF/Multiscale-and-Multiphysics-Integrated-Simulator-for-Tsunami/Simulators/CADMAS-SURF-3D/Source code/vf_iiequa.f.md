---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_iiequa.f
lines: 70
sha256: ded6bb84c18eb3fef7cab4e384b1505dd1f6178b7d7d86a8721be663b84e4e59
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_iiequa.f — 판독 구간 기록

구간은 1행부터 70행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | EQUATION 입력의 선언과 최소 단어 수 검사(1–27). `      SUBROUTINE VF_IIEQUA(IS,IE,NWD,TEXT)` (1) (원문) `CD=== 概要 ===========================================================` (3) (주석 뜻: 개요) `CDT   VF_IIEQUA:方程式制御データ(EQUATION)を解釈する` (5) (주석 뜻: VF_IIEQUA: 방정식 제어 자료(EQUATION)를 해석한다) `C==== 宣言 ===========================================================` (7) (주석 뜻: 선언) `C     -- 大域型 --` (9) (주석 뜻: 전역형) `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10) (원문) `C     -- 大域変数 --` (12) (주석 뜻: 전역 변수) `      INCLUDE 'VF_A0PRM.h'` (13) (원문) `      INCLUDE 'VF_ANUMBI.h'` (14) (원문) `CD    -- 引数 --` (16) (주석 뜻: 인수) `CD    IS(MAXWDS) : IN  : I*4   : n番目の単語の開始位置` (17) (주석 뜻: n번째 단어 시작 위치) `CD    IE(MAXWDS) : IN  : I*4   : n番目の単語の終了位置` (18) (주석 뜻: n번째 단어 끝 위치) `CD    NWD        : IN  : I*4   : 単語の数` (19) (주석 뜻: 단어 수) `CD    TEXT       : IN  : C*(*) : 入力した文字列` (20) (주석 뜻: 입력 문자열) `      DIMENSION IS(MAXWDS),IE(MAXWDS)` (21) (원문) `      CHARACTER*(MAXCHR) TEXT` (22) (원문) `C==== 実行 ===========================================================` (24) (주석 뜻: 실행) `CD    -- 単語数のチェック --` (26) (주석 뜻: 단어 수 검사) `      IF (NWD.LT.2) CALL VF_A2ERR('VF_IIEQUA','SYNTAX ERROR.')` (27) (원문) [11-04 전수 검증 정정] |
| 29–70 | 시작 시 1행 VF_IIEQUA 루틴 안. K-EPS와 TEMPERATURE는 NOCALC/CALC를 각각 0/1로 설정한다(30–49). CONCENTRATION은 LEQC를 정수로 읽고 0..MAXNC를 허용한다(52–56). 미지원 단어 오류와 종료부를 포함한다. `CD    -- EQUATION K-EPSを解釈する --` (29) (주석 뜻: EQUATION K-EPS를 해석한다) `      IF     (TEXT(IS(2):IE(2)).EQ.'K-EPS') THEN` (30) (원문) `        IF (NWD.LT.3) CALL VF_A2ERR('VF_IIEQUA','SYNTAX ERROR.')` (31) (원문) `        IF     (TEXT(IS(3):IE(3)).EQ.'NOCALC') THEN` (32) (원문) `          LEQK=0` (33) (원문) `        ELSEIF (TEXT(IS(3):IE(3)).EQ.'CALC'  ) THEN` (34) (원문) `          LEQK=1` (35) (원문) `        ELSE` (36) (원문) `          CALL VF_A2ERR('VF_IIEQUA','UNKNOWN WORD.')` (37) (원문) `        ENDIF` (38) (원문) `CD    -- EQUATION TEMPERATUREを解釈する --` (40) (주석 뜻: EQUATION TEMPERATURE를 해석한다) `      ELSEIF (TEXT(IS(2):IE(2)).EQ.'TEMPERATURE') THEN` (41) (원문) `        IF (NWD.LT.3) CALL VF_A2ERR('VF_IIEQUA','SYNTAX ERROR.')` (42) (원문) `        IF     (TEXT(IS(3):IE(3)).EQ.'NOCALC') THEN` (43) (원문) `          LEQT=0` (44) (원문) `        ELSEIF (TEXT(IS(3):IE(3)).EQ.'CALC'  ) THEN` (45) (원문) `          LEQT=1` (46) (원문) `        ELSE` (47) (원문) `          CALL VF_A2ERR('VF_IIEQUA','UNKNOWN WORD.')` (48) (원문) `        ENDIF` (49) (원문) `CD    -- EQUATION CONCENTRATIONを解釈する --` (51) (주석 뜻: EQUATION CONCENTRATION를 해석한다) `      ELSEIF (TEXT(IS(2):IE(2)).EQ.'CONCENTRATION') THEN` (52) (원문) `        IF (NWD.LT.3) CALL VF_A2ERR('VF_IIEQUA','SYNTAX ERROR.')` (53) (원문) `        CALL VF_ZSTOI(LEQC,TEXT(IS(3):IE(3)))` (54) (원문) `        IF (LEQC.LT.0    ) CALL VF_A2ERR('VF_IIEQUA','INVALID VALUE.')` (55) (원문) `        IF (LEQC.GT.MAXNC) CALL VF_A2ERR('VF_IIEQUA','INVALID VALUE.')` (56) (원문) `CD    -- 解釈できない単語によるエラー --` (58) (주석 뜻: 해석할 수 없는 단어 오류) `      ELSE` (59) (원문) `        CALL VF_A2ERR('VF_IIEQUA','UNKNOWN WORD.')` (60) (원문) `      ENDIF` (61) (원문) `C     -- 実行文の終了 --` (63) (주석 뜻: 실행문 종료) `      GOTO 9999` (64) (원문) `C==== 終了 ===========================================================` (66) (주석 뜻: 종료) ` 9999 CONTINUE` (68) (원문) `      RETURN` (69) (원문) `      END` (70) (원문) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
