---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_iipara.f
lines: 57
sha256: 65a21efb43ef56b6ff51f41dcd059ee2ded7a6e523873aad2e04dfe7fc12cee0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_iipara.f — 판독 구간 기록

구간은 1행부터 57행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | PARALLEL 입력의 선언과 단어 수 검사(1–27). `      SUBROUTINE VF_IIPARA(IS,IE,NWD,TEXT)` (1) (원문) `CD=== 概要 ===========================================================` (3) (주석 뜻: 개요) `CDT   VF_IIPARA:並列制御データ(PARALLEL)を解釈する` (5) (주석 뜻: VF_IIPARA: 병렬 제어 자료(PARALLEL)를 해석한다) `C==== 宣言 ===========================================================` (7) (주석 뜻: 선언) `C     -- 大域型 --` (9) (주석 뜻: 전역형) `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10) (원문) `C     -- 大域変数 --` (12) (주석 뜻: 전역 변수) `      INCLUDE 'VF_A0PRM.h'` (13) (원문) `      INCLUDE 'VF_APARAI.h'` (14) (원문) `CD    -- 引数 --` (16) (주석 뜻: 인수) `CD    IS(MAXWDS) : IN  : I*4   : n番目の単語の開始位置` (17) (주석 뜻: n번째 단어 시작 위치) `CD    IE(MAXWDS) : IN  : I*4   : n番目の単語の終了位置` (18) (주석 뜻: n번째 단어 끝 위치) `CD    NWD        : IN  : I*4   : 単語の数` (19) (주석 뜻: 단어 수) `CD    TEXT       : IN  : C*(*) : 入力した文字列` (20) (주석 뜻: 입력 문자열) `      DIMENSION IS(MAXWDS),IE(MAXWDS)` (21) (원문) `      CHARACTER*(MAXCHR) TEXT` (22) (원문) `C==== 実行 ===========================================================` (24) (주석 뜻: 실행) `CD    -- 単語数のチェック --` (26) (주석 뜻: 단어 수 검사) `      IF (NWD.LT.2) CALL VF_A2ERR('VF_IIPARA','SYNTAX ERROR.')` (27) (원문) [11-04 전수 검증 정정] |
| 29–57 | 시작 시 1행 VF_IIPARA 루틴 안. X/Y 분기는 NUMNPI/NUMNPJ를 먼저 증가시키고 MAXNPI/MAXNPJ 이상이면 오류를 낸다(30–43). 세 번째 토큰을 IPROCS/JPROCS에 저장한다. 미지원 단어 오류와 종료부를 포함한다. `CD    -- PARALLEL Xを解釈する --` (29) (주석 뜻: PARALLEL X를 해석한다) `      IF     (TEXT(IS(2):IE(2)).EQ.'X') THEN` (30) (원문) `        IF (NWD.LT.3) CALL VF_A2ERR('VF_IIPARA','SYNTAX ERROR.')` (31) (원문) `        NUMNPI=NUMNPI+1` (32) (원문) `        IF (NUMNPI.GE.MAXNPI)` (33); `     &                CALL VF_A2ERR('VF_IIPARA','AREA IS FULL.')` (34) (원문(6열 연속 표시를 포함한 한 문장, 33–34행)) `        CALL VF_ZSTOI(IPROCS(NUMNPI),TEXT(IS(3):IE(3)))` (35) (원문) `CD    -- PARALLEL Yを解釈する --` (37) (주석 뜻: PARALLEL Y를 해석한다) `      ELSEIF (TEXT(IS(2):IE(2)).EQ.'Y') THEN` (38) (원문) `        IF (NWD.LT.3) CALL VF_A2ERR('VF_IIPARA','SYNTAX ERROR.')` (39) (원문) `        NUMNPJ=NUMNPJ+1` (40) (원문) `        IF (NUMNPJ.GE.MAXNPJ)` (41); `     &                CALL VF_A2ERR('VF_IIPARA','AREA IS FULL.')` (42) (원문(6열 연속 표시를 포함한 한 문장, 41–42행)) `        CALL VF_ZSTOI(JPROCS(NUMNPJ),TEXT(IS(3):IE(3)))` (43) (원문) `CD    -- 解釈できない単語によるエラー --` (45) (주석 뜻: 해석할 수 없는 단어 오류) `      ELSE` (46) (원문) `        CALL VF_A2ERR('VF_IIPARA','UNKNOWN WORD.')` (47) (원문) `      ENDIF` (48) (원문) `C     -- 実行文の終了 --` (50) (주석 뜻: 실행문 종료) `      GOTO 9999` (51) (원문) `C==== 終了 ===========================================================` (53) (주석 뜻: 종료) ` 9999 CONTINUE` (55) (원문) `      RETURN` (56) (원문) `      END` (57) (원문) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32–35·40–43: 카운터를 증가한 뒤 GE.MAXNPI 또는 GE.MAXNPJ로 검사한다. 해당 배열에 읽는 정수의 부호·정렬 조건 검사는 이 파일에 없다.
