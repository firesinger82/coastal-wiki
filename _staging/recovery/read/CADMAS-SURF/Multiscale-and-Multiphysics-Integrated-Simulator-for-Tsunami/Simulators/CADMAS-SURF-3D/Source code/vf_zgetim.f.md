---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zgetim.f
lines: 87
sha256: d31dae235c108ad1358e8320aec2e37bc21b6dec7456ae10f084fb85734e40af
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zgetim.f — 판독 구간 기록

구간은 1행부터 87행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 한 줄을 읽어 단어로 나누는 루틴이다. 주석은 구분자를 하나 이상의 공백, # 이후를 주석으로 규정한다. n번째 단어는 TEXT(IS(n):IE(n))이며 빈 줄·주석 줄은 NWD=0이다. 탭 등 특수문자는 판정하지 않는다고 적는다. IMPLICIT 형식과 INCLUDE 두 개를 선언한다. 원문: `      SUBROUTINE VF_ZGETIM(IS,IE,MWD,NWD,IFIL,IEOF,TEXT)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZGETIM:テキストデータを1行を読み込み、単語に分解する` (5) (텍스트 데이터 한 줄을 읽어 단어로 나눈다)。 `CD      (1)区切りは1つ以上の空白` (6) (구분자는 하나 이상의 공백)。 `CD      (2)「#」以降はコメント` (7) (# 이후는 주석)。 `CD      (3)n番目の単語は TEXT(IS(n):IE(n)) の形式で参照する` (8) (n번째 단어는 TEXT(IS(n):IE(n)) 형식으로 참조한다)。 `CD      (4)空白行とコメント行はNWD=0` (9) (빈 줄과 주석 줄은 NWD=0)。 `CD      (5)ダブ等の特殊文字は判定していない(注意)` (10) (탭 등 특수문자는 판정하지 않음에 주의)。 `C==== 宣言 ===========================================================` (12) (선언)。 `C     -- 大域型 --` (14) (전역 형식)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (15)。 `C     -- 大域変数 --` (17) (전역 변수)。 `      INCLUDE 'VF_A0PRM.h'` (18)。 `      INCLUDE 'VF_APARAI.h'` (19)。 |
| 21–40 | 시작 시 1행 SUBROUTINE VF_ZGETIM 루틴 안. IS·IE는 각 단어의 시작·끝 위치이고 MWD는 최대 단어 수다. NWD·IEOF·TEXT를 초기화하고 NC=LEN(TEXT)로 입력 버퍼 길이를 정한다. 원문: `CD    -- 引数 --` (21) (인수)。 `CD    IS(MWD) : OUT : I*4   : n番目の単語の開始位置` (22) (n번째 단어의 시작 위치)。 `CD    IE(MWD) : OUT : I*4   : n番目の単語の終了位置` (23) (n번째 단어의 끝 위치)。 `CD    MWD     : IN  : I*4   : 単語の最大数` (24) (단어의 최대 수)。 `CD    NWD     : OUT : I*4   : 単語の数` (25) (단어의 수)。 `CD    IFIL    : IN  : I*4   : ファイル番号` (26) (파일 번호)。 `CD    IEOF    : OUT : I*4   : = 0:EOFを読み込んでいない` (27) (0: EOF를 읽지 않았다)。 `CD                            !=0:EOFを読み込んだ` (28) (0 이외: EOF를 읽었다)。 `CD    TEXT    : OUT : C*(*) : 入力した文字列` (29) (입력 문자열)。 `      DIMENSION IS(MWD),IE(MWD)` (30)。 `      CHARACTER*(*) TEXT` (31)。 `C==== 実行 ===========================================================` (33) (실행)。 `CD    -- 初期設定 --` (35) (초기 설정)。 `      NWD =0` (36)。 `      IEOF=0` (37)。 `      TEXT=' '` (38)。 `      NC  =LEN(TEXT)` (39)。 |
| 41–53 | 시작 시 1행 SUBROUTINE VF_ZGETIM 루틴 안. MYRANK=0에서만 FORMAT(A)로 READ한다. EOF는 IEOF=1로 표시하고 읽기 오류는 9010번으로 이동한다. NPROCS!=1이면 VF_P1BCSC로 문자열을, VF_P1BCSI로 EOF 값을 배포한다. 원문: `CD    -- 1行を読み込む --` (41) (한 줄을 읽는다)。 `      IF (MYRANK.EQ.0) THEN` (42)。 `        READ(IFIL,9510,END=100,ERR=9010) TEXT` (43)。 `        GOTO 110` (44)。 ` 100    CONTINUE` (45)。 `        IEOF=1` (46)。 ` 110    CONTINUE` (47)。 `      ENDIF` (48)。 `      IF (NPROCS.NE.1) THEN` (49)。 `        CALL VF_P1BCSC(TEXT,NC,0)` (50)。 `        CALL VF_P1BCSI(IEOF, 1,0)` (51)。 `      ENDIF` (52)。 |
| 54–68 | 시작 시 1행 SUBROUTINE VF_ZGETIM 루틴 안. I=1..NC에서 최초 비공백 ION과 최초 # 위치 ICM을 찾는다. 빈 줄과 첫 유효 문자가 #인 줄은 9000번으로 간다. #이 없으면 ICM=NC+1이다. 유효 부분을 TEXT 앞쪽으로 옮기고 VF_ZSTOWS에 부분 문자열을 전달한다. 원문: `CD    -- 空白行とコメント行はスキップ --` (54) (빈 줄과 주석 줄은 건너뛴다)。 `      ION=0` (55)。 `      ICM=0` (56)。 `      DO 200 I=1,NC` (57)。 `        IF (ION.EQ.0 .AND. TEXT(I:I).NE.' ') ION=I` (58)。 `        IF (ICM.EQ.0 .AND. TEXT(I:I).EQ.'#') ICM=I` (59)。 ` 200  CONTINUE` (60)。 `      IF (ION.EQ.0  ) GOTO 9000` (61)。 `      IF (ION.EQ.ICM) GOTO 9000` (62)。 `CD    -- 有効行を単語に分解 --` (64) (유효한 줄을 단어로 나눈다)。 `      IF (ICM.EQ.0) ICM=NC+1` (65)。 `      TEXT=TEXT(ION:ICM-1)` (66)。 `      CALL VF_ZSTOWS(IS,IE,MWD,NWD,TEXT(1:ICM-ION))` (67)。 |
| 69–87 | 시작 시 1행 SUBROUTINE VF_ZGETIM 루틴 안. 정상 종료 경로는 9000·9999를 거친다. 읽기 오류 경로는 VF_A2ERR('VF_ZGETIM','I/O ERROR(text data).')를 호출한다. FORMAT 9510은 A이고 최종 RETURN으로 끝난다. 원문: `C     -- 実行文の終了 --` (69) (실행문 종료)。 ` 9000 CONTINUE` (70)。 `      GOTO 9999` (71)。 `C==== ファイル関連エラー処理 =========================================` (73) (파일 관련 오류 처리)。 ` 9010 CONTINUE` (75)。 `      CALL VF_A2ERR('VF_ZGETIM','I/O ERROR(text data).')` (76)。 `      GOTO 9999` (77)。 `C==== フォーマット文 =================================================` (79) (FORMAT 문)。 ` 9510 FORMAT(A)` (81)。 `C==== 終了 ===========================================================` (83) (종료)。 ` 9999 CONTINUE` (85)。 `      RETURN` (86)。 `      END` (87)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41–52: 파일 READ는 MYRANK=0에서 수행한다. 문자열과 EOF의 배포 호출은 NPROCS.NE.1일 때 수행한다.
- 5–10·57–67: 주석은 탭 등 특수문자를 판정하지 않는다고 명시한다. 실제 선행 공백 검사도 문자 리터럴 ' '와 비교한다.
