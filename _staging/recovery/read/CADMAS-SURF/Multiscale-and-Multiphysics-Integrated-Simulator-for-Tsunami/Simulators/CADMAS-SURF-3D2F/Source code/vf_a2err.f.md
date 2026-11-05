---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_a2err.f
lines: 69
sha256: b55cbe622811eb9e0671496cd69cf4413be24662b303e33d68a5334a00e77106
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_a2err.f — 판독 구간 기록

구간은 1행부터 69행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | VF_A2ERR 시작. 일본어 주석 뜻: 개요(3), 오류 메시지 출력·실행 종료(5), 선언(7), 전역형(9), 전역 변수(12), 인수(17), 오류 발생 루틴 이름(18), 오류 메시지(19), 지역 변수(22), 실행(25). IMPLICIT·세 INCLUDE·문자 인수를 선언한다. 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      SUBROUTINE VF_A2ERR(CNAME,CMSG)` (1)<br>`CD=== 概要 ===========================================================` (3)<br>`CDT   VF_A2ERR:エラーメッセージの出力と実行終了` (5)<br>`C==== 宣言 ===========================================================` (7)<br>`C     -- 大域型 --` (9)<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10)<br>`C     -- 大域変数 --` (12)<br>`      INCLUDE 'VF_A0PRM.h'` (13)<br>`      INCLUDE 'VF_AFILEI.h'` (14)<br>`      INCLUDE 'VF_APARAI.h'` (15)<br>`CD    -- 引数 --` (17)<br>`CD    CNAME : IN : C*(*) : エラーの発生したルーチン名` (18)<br>`CD    CMSG  : IN : C*(*) : エラーメッセージ` (19)<br>`      CHARACTER*(*) CNAME,CMSG` (20)<br>`CD    -- 局所変数 --` (22)<br>`      CHARACTER*5 TEXTP` (23)<br>`C==== 実行 ===========================================================` (25) |
| 27–44 | 시작 시 1행 루틴 안. 27행 일본어는 오류 메시지 출력을 뜻한다. NPROCS=1과 병렬 경로를 나누어 목록파일이 열렸으면 해당 파일에도 출력한다. 병렬 경로는 5자리 MYRANK를 메시지에 붙인다(28–43). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `CD    -- エラーメッセージの出力 --` (27)<br>`      IF (NPROCS.EQ.1) THEN` (28)<br>`        IF (ILPFIL.NE.0) THEN` (29)<br>`          WRITE(ILPFIL,9510) CNAME,CMSG` (30)<br>`          WRITE(ILPFIL,9520)` (31)<br>`        ENDIF` (32)<br>`        WRITE(*     ,9510) CNAME,CMSG` (33)<br>`        WRITE(*     ,9520)` (34)<br>`      ELSE` (35)<br>`        WRITE(TEXTP,'(I5.5)') MYRANK` (36)<br>`        IF (ILPFIL.NE.0) THEN` (37)<br>`          WRITE(ILPFIL,9530) TEXTP,CNAME,CMSG` (38)<br>`          WRITE(ILPFIL,9540) TEXTP` (39)<br>`        ENDIF` (40)<br>`        WRITE(*     ,9530) TEXTP,CNAME,CMSG` (41)<br>`        WRITE(*     ,9540) TEXTP` (42)<br>`      ENDIF` (43) |
| 45–69 | 시작 시 1행 루틴 안. 일본어 주석 뜻: 파일 닫기(45), 병렬 환경 비정상 종료(48), 실행 종료(51), 실행문 종료(54), 형식문(58), 종료(65). VF_A2CLOS·VF_P1ENDA 호출 뒤 레이블 9000·9999를 거쳐 STOP한다. 네 오류 출력 형식을 적는다(46–69). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `CD    -- ファイルのクローズ --` (45)<br>`      CALL VF_A2CLOS()` (46)<br>`CD    -- 並列環境の異常終了 --` (48)<br>`      CALL VF_P1ENDA()` (49)<br>`CD    -- 実行を終了 --` (51)<br>`      GOTO 9000` (52)<br>`C     -- 実行文の終了 --` (54)<br>` 9000 CONTINUE` (55)<br>`      GOTO 9999` (56)<br>`C==== フォーマット文 =================================================` (58)<br>` 9510 FORMAT(/' ','>>>>> ERROR. [',A,'] : ',A)` (60)<br>` 9520 FORMAT(/' ','##### ABNORMAL END. #########################'/)` (61)<br>` 9530 FORMAT(/' ','>>>>> ERROR(P',A,'). [',A,'] : ',A)` (62)<br>` 9540 FORMAT(/' ','##### ABNORMAL END(P',A,'). #################'/)` (63)<br>`C==== 終了 ===========================================================` (65)<br>` 9999 CONTINUE` (67)<br>`      STOP` (68)<br>`      END` (69) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
