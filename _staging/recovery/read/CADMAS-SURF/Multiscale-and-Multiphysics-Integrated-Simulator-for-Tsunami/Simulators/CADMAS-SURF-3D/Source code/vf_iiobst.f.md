---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_iiobst.f
lines: 64
sha256: 1fe1e8a78aaa2d8ef04fd9a8db413cee6df9487f57bca689e74ace8a5a9a66ad
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_iiobst.f — 판독 구간 기록

구간은 1행부터 64행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | OBST 장애물(obstacle) 입력의 선언과 병렬 인덱스 이동량(1–31). NF는 NUMI·NUMJ·NUMK 배열이다. `      SUBROUTINE VF_IIOBST(NF,IS,IE,NWD,TEXT)` (1) (원문) `CD=== 概要 ===========================================================` (3) (주석 뜻: 개요) `CDT   VF_IIOBST:障害物データ(OBST)を解釈する` (5) (주석 뜻: VF_IIOBST: 장애물 자료(OBST)를 해석한다) `C==== 宣言 ===========================================================` (7) (주석 뜻: 선언) `C     -- 大域型 --` (9) (주석 뜻: 전역형) `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10) (원문) `C     -- 大域変数 --` (12) (주석 뜻: 전역 변수) `      INCLUDE 'VF_A0PRM.h'` (13) (원문) `      INCLUDE 'VF_ANUMBI.h'` (14) (원문) `      INCLUDE 'VF_APARAI.h'` (15) (원문) `CD    -- 引数 --` (17) (주석 뜻: 인수) `CD    NF(@FOR-3D@) : I/O : I*4 : セルの状態を示すインデックス` (18) (주석 뜻: 셀 상태를 나타내는 인덱스) `CD    IS(MAXWDS)   : IN  : I*4   : n番目の単語の開始位置` (19) (주석 뜻: n번째 단어 시작 위치) `CD    IE(MAXWDS)   : IN  : I*4   : n番目の単語の終了位置` (20) (주석 뜻: n번째 단어 끝 위치) `CD    NWD          : IN  : I*4   : 単語の数` (21) (주석 뜻: 단어 수) `CD    TEXT         : IN  : C*(*) : 入力した文字列` (22) (주석 뜻: 입력 문자열) `      DIMENSION NF(NUMI,NUMJ,NUMK)` (23) (원문) `      DIMENSION IS(MAXWDS),IE(MAXWDS)` (24) (원문) `      CHARACTER*(MAXCHR) TEXT` (25) (원문) `C==== 実行 ===========================================================` (27) (주석 뜻: 실행) `CD    -- 並列時のシフト分 --` (29) (주석 뜻: 병렬 처리 시 이동량) `      IP=MYGIS-1` (30) (원문) `      JP=MYGJS-1` (31) (원문) [11-04 전수 검증 정정] |
| 33–64 | 시작 시 1행 VF_IIOBST 루틴 안. 여섯 끝점을 정수로 읽고 내부 격자 범위와 순서를 검사한다(34–44). 인덱스에 1을 더한 범위를 순회하며 담당 지역에 속한 셀의 NF를 -1로 설정한다(45–55). 종료부를 포함한다. `CD    -- OBSTを解釈する --` (33) (주석 뜻: OBST를 해석한다) `      IF (NWD.LT.7) CALL VF_A2ERR('VF_IIOBST','SYNTAX ERROR.')` (34) (원문) `      CALL VF_ZSTOI(I1,TEXT(IS(2):IE(2)))` (35) (원문) `      CALL VF_ZSTOI(J1,TEXT(IS(3):IE(3)))` (36) (원문) `      CALL VF_ZSTOI(K1,TEXT(IS(4):IE(4)))` (37) (원문) `      CALL VF_ZSTOI(I2,TEXT(IS(5):IE(5)))` (38) (원문) `      CALL VF_ZSTOI(J2,TEXT(IS(6):IE(6)))` (39) (원문) `      CALL VF_ZSTOI(K2,TEXT(IS(7):IE(7)))` (40) (원문) `      IF (I1.LT.1 .OR. I2.GT.NUMI0-2 .OR. I1.GT.I2 .OR.` (41); `     &    J1.LT.1 .OR. J2.GT.NUMJ0-2 .OR. J1.GT.J2 .OR.` (42); `     &    K1.LT.1 .OR. K2.GT.NUMK -2 .OR. K1.GT.K2     ) ` (43); `     &                CALL VF_A2ERR('VF_IIOBST','INVALID VALUE.')` (44) (원문(6열 연속 표시를 포함한 한 문장, 41–44행)) `      DO 220 K=K1+1,K2+1` (45) (원문) `        DO 210 J=J1+1,J2+1` (46) (원문) `          IF (MYGJS.LE.J .AND. J.LE.MYGJE) THEN` (47) (원문) `            DO 200 I=I1+1,I2+1` (48) (원문) `              IF (MYGIS.LE.I .AND. I.LE.MYGIE) THEN` (49) (원문) `                NF(I-IP,J-JP,K)=-1` (50) (원문) `              ENDIF` (51) (원문) ` 200        CONTINUE` (52) (원문) `          ENDIF` (53) (원문) ` 210    CONTINUE` (54) (원문) ` 220  CONTINUE` (55) (원문) `C     -- 実行文の終了 --` (57) (주석 뜻: 실행문 종료) `      GOTO 9999` (58) (원문) `C==== 終了 ===========================================================` (60) (주석 뜻: 종료) ` 9999 CONTINUE` (62) (원문) `      RETURN` (63) (원문) `      END` (64) (원문) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
