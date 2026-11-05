---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_debug.f
lines: 61
sha256: 51337e73c77f58dab793c34c29c904fcf8a62fcab448307afecd5aaf7066638c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_debug.f — 판독 구간 기록

구간은 1행부터 61행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | 디버그(debug) 출력 루틴의 문자 인수와 NF·FF·GGV 배열 선언이다(1–27).<br>`      SUBROUTINE VF_DEBUG(CR,NF,FF,GGV,I,J,K)` (1).<br>`CD=== 概要 ===========================================================` (3) (개요).<br>`CDT   VF_DEBUG:デバッグ出力を行う` (5) (VF_DEBUG:디버그(debug) 출력을 수행한다).<br>`C==== 宣言 ===========================================================` (7) (선언).<br>`C     -- 大域型 --` (9) (전역 형).<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10).<br>`C     -- 大域変数 --` (12) (전역 변수).<br>`      INCLUDE 'VF_A0PRM.h'` (13).<br>`      INCLUDE 'VF_ANUMBI.h'` (14).<br>`      INCLUDE 'VF_APARAI.h'` (15).<br>`      INCLUDE 'VF_AFILEI.h'` (16).<br>`      INCLUDE 'VF_ACOMPR.h'` (17).<br>`      INCLUDE 'VF_ATIMEI.h'` (18).<br>`      INCLUDE 'VF_ATIMER.h'` (19).<br>`CD    -- 引数 --` (21) (인수).<br>`CD    NF(@FOR-3D@)        : I/O : I*4 : セルの状態を示すインデックス` (22) (NF(@FOR-3D@)        : I/O : I*4 : 셀 상태를 나타내는 인덱스).<br>`CD    FF(@FOR-3D@)        : I/O  : R*8 : VOF関数F` (23) (FF(@FOR-3D@)        : I/O  : R*8 : VOF 함수).<br>`      CHARACTER*(*) CR` (24).<br>`      DIMENSION NF (NUMI,NUMJ,NUMK)` (25).<br>`      DIMENSION FF (NUMI,NUMJ,NUMK)` (26).<br>`      DIMENSION GGV(NUMI,NUMJ,NUMK)` (27).<br>`C==== 実行 ===========================================================` (29) (실행). |
| 31–53 | 시작 시 1행 SUBROUTINE VF_DEBUG 루틴 안. 요청 전역 위치가 담당 영역 밖이면 반환한다(36–37). 순위별 출력 장치 2001+MYRANK에 시각·임계값과 3×3×3 이웃의 F·공극률(porosity)·NF를 출력한다(40–52).<br>`CD    -- 並列時のシフト分 --` (31) (병렬 실행 시 인덱스 이동량).<br>`      IP=MYGIS-1` (32).<br>`      JP=MYGJS-1` (33).<br>`CD    -- 並列時で担当領域に含まれていなければ何もしない --` (35) (병렬 실행에서 담당 영역 밖이면 아무것도 하지 않는다).<br>`      IF (MYGIS.GT.I .OR. I.GT.MYGIE) GOTO 9999` (36).<br>`      IF (MYGJS.GT.J .OR. J.GT.MYGJE) GOTO 9999` (37).<br>`CD    -- デバッグ出力 --` (39) (디버그(debug) 출력).<br>`      IDBGF=2001+MYRANK` (40).<br>연속행 문장: `      WRITE(IDBGF,'(3A,I5,A,I3,1P,2(A,E12.5))')` (41); `     & ' SUBROUTINE(',CR,') NS=',NNOW,'(',ILOOP,') T=',TNOW,` (42); `     & ' PLOWER=',PLOWER` (43).<br>`      DO JD=J-1,J+1` (44).<br>`        WRITE(IDBGF,'(A,I4,A,3(I12,:,'',''))') 'J=',JD,' I=',I-1,I,I+1` (45).<br>`        DO KD=K+1,K-1,-1` (46).<br>연속행 문장: `          WRITE(IDBGF,'(A,I4,2(A,1P,3(E12.4,:,'','')),A,3(I2,:,'',''))')` (47); `     &                '  K=',KD,':',(FF (ID,JD,KD),ID=I-1,I+1),` (48); `     &                          ':',(GGV(ID,JD,KD),ID=I-1,I+1),` (49); `     &                          ':',(NF (ID,JD,KD),ID=I-1,I+1)` (50).<br>`        ENDDO` (51).<br>`      ENDDO` (52). |
| 54–61 | 시작 시 1행 SUBROUTINE VF_DEBUG 루틴 안. 종료 레이블로 이동하여 반환한다(55–61).<br>`C     -- 実行文の終了 --` (54) (실행문 종료).<br>`      GOTO 9999` (55).<br>`C==== 終了 ===========================================================` (57) (종료).<br>` 9999 CONTINUE` (59).<br>`      RETURN` (60).<br>`      END` (61). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32–33·44–50: IP·JP를 계산하지만 출력 배열 첨자는 I/J에서 직접 만든 ID/JD이다. IP·JP를 배열 접근에 적용하지 않는다.
- 36–37·44–50: 중심 I/J의 담당 범위는 검사한다. 이 루틴에는 이웃 I±1·J±1 및 K±1의 배열 범위 검사가 없다.
