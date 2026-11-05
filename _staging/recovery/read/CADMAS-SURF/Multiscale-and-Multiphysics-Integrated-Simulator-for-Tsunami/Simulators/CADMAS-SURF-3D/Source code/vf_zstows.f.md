---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zstows.f
lines: 63
sha256: 40c30177dd456e13058e6bce78a3ec55117d63953ded7ffee9b5ad11f67e231f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zstows.f — 판독 구간 기록

구간은 1행부터 63행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 문자열을 공백 구분 단어로 나눈다. n번째 단어는 TEXT(IS(n):IE(n))로 참조한다. IMPLICIT, IS(MWD)·IE(MWD) 및 가변 길이 TEXT를 선언한다. 원문: `      SUBROUTINE VF_ZSTOWS(IS,IE,MWD,NWD,TEXT)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZSTOWS:文字列を単語に分解する` (5) (문자열을 단어로 나눈다)。 `CD      (1)区切りは1つ以上の空白` (6) (구분자는 하나 이상의 공백)。 `CD      (2)n番目の単語は TEXT(IS(n):IE(n)) の形式で参照する` (7) (n번째 단어는 TEXT(IS(n):IE(n)) 형식으로 참조한다)。 `C==== 宣言 ===========================================================` (9) (선언)。 `C     -- 大域型 --` (11) (전역 형식)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (12)。 `CD    -- 引数 --` (14) (인수)。 `CD    IS(MWD)  : OUT : I*4   : n番目の単語の開始位置` (15) (n번째 단어의 시작 위치)。 `CD    IE(MWD)  : OUT : I*4   : n番目の単語の終了位置` (16) (n번째 단어의 끝 위치)。 `CD    MWD      : IN  : I*4   : 単語の最大数` (17) (단어의 최대 수)。 `CD    NWD      : OUT : I*4   : 単語の数` (18) (단어의 수)。 `CD    TEXT     : IN  : C*(*) : 分解する文字列` (19) (분해할 문자열)。 `      DIMENSION IS(MWD),IE(MWD)` (20)。 `      CHARACTER*(*) TEXT` (21)。 `C==== 実行 ===========================================================` (23) (실행)。 |
| 25–34 | 시작 시 1행 SUBROUTINE VF_ZSTOWS 루틴 안. NWD=0으로 시작한다. 최대 단어 수 MWD<=0 또는 문자열 길이 NC<=0이면 56행 레이블 9000으로 이동한다. 57행 `GOTO 9999`는 61행으로 이동한다. 62행 `RETURN`으로 반환한다. 원문: `CD    -- 初期設定 --` (25) (초기 설정)。 `      NWD=0` (26)。 `CD    -- 単語の最大数がゼロ以下なら終了 --` (28) (최대 단어 수가 0 이하이면 종료)。 `      IF (MWD.LE.0) GOTO 9000` (29)。 `CD    -- 1行の文字数がゼロ以下なら終了 --` (31) (한 줄의 문자 수가 0 이하이면 종료)。 `      NC=LEN(TEXT)` (32)。 `      IF (NC.LE.0) GOTO 9000` (33)。 [11-04 전수 검증 보완] |
| 35–54 | 시작 시 1행 SUBROUTINE VF_ZSTOWS 루틴 안. ION=0에서 I=1..NC를 순회한다. 공백이고 단어 안이면 IE(NWD)=I−1로 끝 위치를 기록하고 ION=0으로 둔다. NWD>=MWD이면 더 읽지 않는다. 비공백이고 단어 밖이면 NWD를 늘려 시작 위치를 기록한다. 문자열 끝까지 단어가 열려 있으면 IE(NWD)=NC로 닫는다. 원문: `CD    -- 文字列を分解 --` (35) (문자열 분해)。 `      ION=0` (36)。 `      DO 100 I=1,NC` (37)。 `        IF (TEXT(I:I).EQ.' ') THEN` (38)。 `          IF (ION.NE.0) THEN` (39)。 `            IE(NWD)=I-1` (40)。 `            ION=0` (41)。 `            IF (NWD.GE.MWD) GOTO 110` (42)。 `          ENDIF` (43)。 `        ELSE` (44)。 `          IF (ION.EQ.0) THEN` (45)。 `            NWD=NWD+1` (46)。 `            IS(NWD)=I` (47)。 `            ION=1` (48)。 `          ENDIF` (49)。 `        ENDIF` (50)。 ` 100  CONTINUE` (51)。 ` 110  CONTINUE` (52)。 `      IF (ION.NE.0) IE(NWD)=NC` (53)。 |
| 55–63 | 시작 시 1행 SUBROUTINE VF_ZSTOWS 루틴 안. 9000·9999 종료 표지를 거쳐 RETURN으로 반환한다. 원문: `C     -- 実行文の終了 --` (55) (실행문 종료)。 ` 9000 CONTINUE` (56)。 `      GOTO 9999` (57)。 `C==== 終了 ===========================================================` (59) (종료)。 ` 9999 CONTINUE` (61)。 `      RETURN` (62)。 `      END` (63)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 38–53: 구분자는 공백 문자 하나와 비교한다. 최대 단어 수에 도달한 뒤 해당 단어의 끝 공백을 만나면 110번으로 이동하며 추가 단어에 대한 오류 호출은 없다.
