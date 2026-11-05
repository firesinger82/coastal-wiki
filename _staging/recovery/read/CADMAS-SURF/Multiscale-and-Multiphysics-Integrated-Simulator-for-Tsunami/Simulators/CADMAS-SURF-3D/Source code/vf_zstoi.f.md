---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zstoi.f
lines: 86
sha256: 2c27244358156425823a11e2685ff2504939407bc94bf07de85b43271f3ea9a2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zstoi.f — 판독 구간 기록

구간은 1행부터 86행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 문자열을 정수(integer)로 변환한다. 선행 공백을 무시하고 부호·숫자가 아닌 문자부터는 인식하지 않는다는 주석이다. IMPLICIT 형식과 가변 길이 문자 인수를 선언한다. 원문: `      SUBROUTINE VF_ZSTOI(IVAL,TEXT)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZSTOI:文字列を整数に変換する` (5) (문자열을 정수로 변환한다)。 `CD      (1)前の空白は無視する` (6) (앞의 공백은 무시한다)。 `CD      (2)符号および数字以外の文字以降は認識しない` (7) (부호·숫자 이외 문자가 나온 뒤는 인식하지 않는다)。 `C==== 宣言 ===========================================================` (9) (선언)。 `C     -- 大域型 --` (11) (전역 형식)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (12)。 `CD    -- 引数 --` (14) (인수)。 `CD    IVAL : OUT : I*4   : 変換した整数` (15) (변환된 정수)。 `CD    TEXT : IN  : C*(*) : 変換する文字列` (16) (변환할 문자열)。 `      CHARACTER*(*) TEXT` (17)。 `C==== 実行 ===========================================================` (19) (실행)。 |
| 21–46 | 시작 시 1행 SUBROUTINE VF_ZSTOI 루틴 안. IVAL=0, ISG=1, IP=0으로 초기화하고 NC=LEN(TEXT)를 정한다. I=1..NC에서 첫 비공백을 찾는다. 없으면 종료한다. 첫 문자가 +이면 위치만 이동하고 −이면 ISG=−1과 위치 이동을 수행한다. 40–45행의 부호 분기에는 ELSE가 없다. 두 조건이 모두 거짓이면 IP와 ISG를 유지한다. 31행의 이동 대상은 34행 레이블 110이다. 37행의 이동 대상은 79행 레이블 9000이다. 원문: `CD    -- 初期設定 --` (21) (초기 설정)。 `      IVAL=0` (22)。 `      ISG =1` (23)。 `      IP  =0` (24)。 `      NC  =LEN(TEXT)` (25)。 `CD    -- 空白でない文字の開始位置 --` (27) (공백이 아닌 문자의 시작 위치)。 `      DO 100 I=1,NC` (28)。 `        IF (TEXT(I:I).NE.' ') THEN` (29)。 `          IP=I` (30)。 `          GOTO 110` (31)。 `        ENDIF` (32)。 `  100 CONTINUE` (33)。 `  110 CONTINUE` (34)。 `CD    -- 空白行なら終了 --` (36) (빈 줄이면 종료)。 `      IF (IP.EQ.0) GOTO 9000` (37)。 `CD    -- 符号を識別 --` (39) (부호 식별)。 `      IF (TEXT(IP:IP).EQ.'+') THEN` (40)。 `        IP=IP+1` (41)。 `      ELSEIF (TEXT(IP:IP).EQ.'-') THEN` (42)。 `        ISG=-1` (43)。 `        IP=IP+1` (44)。 `      ENDIF` (45)。 [11-04 전수 검증 보완] |
| 47–74 | 시작 시 1행 SUBROUTINE VF_ZSTOI 루틴 안. I=IP..NC에서 문자 0..9에 대해 각각 IVAL=10*IVAL+숫자를 누적한다. 다른 문자가 나오면 210번으로 이동한다. 각 IF·ELSEIF 조건과 계산식은 원문대로 인용한다. 원문: `CD    -- 絶対値を識別 --` (47) (절댓값 식별)。 `      DO 200 I=IP,NC` (48)。 `        IF (TEXT(I:I).EQ.'0') THEN` (49)。 `          IVAL=10*IVAL+0` (50)。 `        ELSEIF (TEXT(I:I).EQ.'1') THEN` (51)。 `          IVAL=10*IVAL+1` (52)。 `        ELSEIF (TEXT(I:I).EQ.'2') THEN` (53)。 `          IVAL=10*IVAL+2` (54)。 `        ELSEIF (TEXT(I:I).EQ.'3') THEN` (55)。 `          IVAL=10*IVAL+3` (56)。 `        ELSEIF (TEXT(I:I).EQ.'4') THEN` (57)。 `          IVAL=10*IVAL+4` (58)。 `        ELSEIF (TEXT(I:I).EQ.'5') THEN` (59)。 `          IVAL=10*IVAL+5` (60)。 `        ELSEIF (TEXT(I:I).EQ.'6') THEN` (61)。 `          IVAL=10*IVAL+6` (62)。 `        ELSEIF (TEXT(I:I).EQ.'7') THEN` (63)。 `          IVAL=10*IVAL+7` (64)。 `        ELSEIF (TEXT(I:I).EQ.'8') THEN` (65)。 `          IVAL=10*IVAL+8` (66)。 `        ELSEIF (TEXT(I:I).EQ.'9') THEN` (67)。 `          IVAL=10*IVAL+9` (68)。 `        ELSE` (69)。 `          GOTO 210` (70)。 `        ENDIF` (71)。 ` 200  CONTINUE` (72)。 ` 210  CONTINUE` (73)。 |
| 75–86 | 시작 시 1행 SUBROUTINE VF_ZSTOI 루틴 안. IVAL=ISG*IVAL로 부호를 적용한다. 9000·9999를 거쳐 반환한다. 원문: `CD    -- 符号*絶対値を計算 --` (75) (부호와 절댓값의 곱 계산)。 `      IVAL=ISG*IVAL` (76)。 `C     -- 実行文の終了 --` (78) (실행문 종료)。 ` 9000 CONTINUE` (79)。 `      GOTO 9999` (80)。 `C==== 終了 ===========================================================` (82) (종료)。 ` 9999 CONTINUE` (84)。 `      RETURN` (85)。 `      END` (86)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 48–70: 숫자가 아닌 문자는 오류 호출 없이 누적을 중단시킨다. 이 루프에는 정수 범위 초과 검사가 없다.
