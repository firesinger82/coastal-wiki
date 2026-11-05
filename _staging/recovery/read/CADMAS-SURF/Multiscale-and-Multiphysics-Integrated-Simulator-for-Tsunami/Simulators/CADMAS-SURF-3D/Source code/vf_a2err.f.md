---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_a2err.f
lines: 69
sha256: 63eb4e9dbac31516b94ba73928b7f91994c7929463bcb42a5ba8b20e288b28b4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_a2err.f — 판독 구간 기록

구간은 1행부터 69행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | VF_A2ERR는 길이 미정 문자열 CNAME·CMSG와 5자리 랭크 문자열 TEXTP를 선언한다. IMPLICIT·INCLUDE 목록은 아래와 같다. 원문: `      SUBROUTINE VF_A2ERR(CNAME,CMSG)` (1); `CD=== 概要 ===========================================================` (3) (개요); `CDT   VF_A2ERR:エラーメッセージの出力と実行終了` (5) (오류 메시지 출력·실행 종료); `C==== 宣言 ===========================================================` (7) (선언); `C     -- 大域型 --` (9) (전역 형); `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10); `C     -- 大域変数 --` (12) (전역 변수); `      INCLUDE 'VF_A0PRM.h'` (13); `      INCLUDE 'VF_AFILEI.h'` (14); `      INCLUDE 'VF_APARAI.h'` (15); `CD    -- 引数 --` (17) (인수); `CD    CNAME : IN : C*(*) : エラーの発生したルーチン名` (18) (오류 발생 루틴 이름); `CD    CMSG  : IN : C*(*) : エラーメッセージ` (19) (오류 메시지); `      CHARACTER*(*) CNAME,CMSG` (20); `CD    -- 局所変数 --` (22) (국소 변수); `      CHARACTER*5 TEXTP` (23); `C==== 実行 ===========================================================` (25) (실행). |
| 27–44 | 1행 VF_A2ERR 안. MGPROC.EQ.1은 랭크 없는 오류를, ELSE는 MGRANK를 5자리로 넣은 오류를 출력한다. ILPFIL.NE.0이면 리스트에도 출력하며 표준 출력은 두 분기 모두 사용한다. 원문: `CD    -- エラーメッセージの出力 --` (27) (오류 메시지 출력); `      IF (MGPROC.EQ.1) THEN` (28); `        IF (ILPFIL.NE.0) THEN` (29); `          WRITE(ILPFIL,9510) CNAME,CMSG` (30); `          WRITE(ILPFIL,9520)` (31); `        ENDIF` (32); `        WRITE(*     ,9510) CNAME,CMSG` (33); `        WRITE(*     ,9520)` (34); `      ELSE` (35); `        WRITE(TEXTP,'(I5.5)') MGRANK` (36); `        IF (ILPFIL.NE.0) THEN` (37); `          WRITE(ILPFIL,9530) TEXTP,CNAME,CMSG` (38); `          WRITE(ILPFIL,9540) TEXTP` (39); `        ENDIF` (40); `        WRITE(*     ,9530) TEXTP,CNAME,CMSG` (41); `        WRITE(*     ,9540) TEXTP` (42); `      ENDIF` (43). |
| 45–69 | 1행 VF_A2ERR 안이며 오류 표시 분기 밖. VF_A2CLOS로 파일을 닫고 VF_P0ENDA로 병렬 비정상 종료를 요청한다. 9000·9999를 거쳐 STOP한다. 네 출력 FORMAT을 정의한다. 원문: `CD    -- ファイルのクローズ --` (45) (파일 닫기); `      CALL VF_A2CLOS()` (46); `CD    -- 並列環境の異常終了 --` (48) (병렬 환경 비정상 종료); `      CALL VF_P0ENDA()` (49); `CD    -- 実行を終了 --` (51) (실행 종료); `      GOTO 9000` (52); `C     -- 実行文の終了 --` (54) (실행문 종료); ` 9000 CONTINUE` (55); `      GOTO 9999` (56); `C==== フォーマット文 =================================================` (58) (형식문); ` 9510 FORMAT(/' ','>>>>> ERROR. [',A,'] : ',A)` (60); ` 9520 FORMAT(/' ','##### ABNORMAL END. #########################'/)` (61); ` 9530 FORMAT(/' ','>>>>> ERROR(MG',A,'). [',A,'] : ',A)` (62); ` 9540 FORMAT(/' ','##### ABNORMAL END(MG',A,'). #################'/)` (63); `C==== 終了 ===========================================================` (65) (종료); ` 9999 CONTINUE` (67); `      STOP` (68); `      END` (69). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
