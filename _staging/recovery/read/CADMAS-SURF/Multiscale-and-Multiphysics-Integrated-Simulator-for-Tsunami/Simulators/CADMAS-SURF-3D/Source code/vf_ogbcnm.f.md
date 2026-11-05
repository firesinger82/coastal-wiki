---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_ogbcnm.f
lines: 89
sha256: c0a435401ab44a1720b25b25e6e2813d3788bf5093aa4f7cb741a32e2c5f2b0b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_ogbcnm.f — 판독 구간 기록

구간은 1행부터 89행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 도화 경계 개수 계산 루틴의 형식·포함 파일과 INDB 배열 범위를 선언한다. 원문: `      SUBROUTINE VF_OGBCNM(INDB,NBX,NBY,NBZ)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_OGBCNM:図化用の境界の数を数える` (5) (도화용 경계 수를 센다). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형식). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C     -- 大域変数 --` (12) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (13). `      INCLUDE 'VF_AFILEI.h'` (14). `      INCLUDE 'VF_ANUMBI.h'` (15). `      INCLUDE 'VF_APARAI.h'` (16). `CD    -- 引数 --` (18) (인수). `CD    INDB (MAXB1,NUMB) : IN  : I*4 : 境界面のインデックス` (19) (경계면 인덱스(index)). `CD    NBX               : OUT : I*4 : x方向境界面の数` (20) (x방향 경계면 수). `CD    NBY               : OUT : I*4 : y方向境界面の数` (21) (y방향 경계면 수). `CD    NBZ               : OUT : I*4 : z方向境界面の数` (22) (z방향 경계면 수). `      DIMENSION INDB(MAXB1,NUMB)` (23). `C==== 実行 ===========================================================` (25) (실행). |
| 27–40 | 시작 시 1행 루틴 `SUBROUTINE VF_OGBCNM` 안. 출력 영역을 지역 소유 범위로 제한하고 면별 상한 및 방향별 개수의 초깃값을 설정한다. 원문: `CD    -- 初期設定 --` (27) (초기 설정). `      I1=MAX(IGRARA(1)-(MYGIS-1),MYIS)` (28). `      J1=MAX(IGRARA(2)-(MYGJS-1),MYJS)` (29). `      K1=IGRARA(3)` (30). `      I2=MIN(IGRARA(4)-(MYGIS-1),MYIE)` (31). `      J2=MIN(IGRARA(5)-(MYGJS-1),MYJE)` (32). `      K2=IGRARA(6)` (33). `      IX=I2+1` (34). `      JY=J2+1` (35). `      KZ=K2+1` (36). `      NBX=0` (37). `      NBY=0` (38). `      NBZ=0` (39). |
| 41–68 | 시작 시 1행 루틴 `SUBROUTINE VF_OGBCNM` 안. 경계를 순회하며 선형 인덱스(linear index)를 I,J,K로 변환한다. NS와 방향별 두께·출력 범위 조건으로 NBX와 NBY를 센다. 원문: `CD    -- 数を数える --` (41) (수를 센다). `      DO 100 L=1,NUMB` (42). `        IJK=INDB(1,L)` (43). `        NS =INDB(2,L)` (44). `        K  =(IJK-1)/(NUMI*NUMJ)+1` (45). `        IJK=IJK-NUMI*NUMJ*(K-1)` (46). `        J  =(IJK-1)/NUMI+1` (47). `        I  =IJK-NUMI*(J-1)` (48). `        IF     (NS.EQ.1 .OR. NS.EQ.2) THEN` (49). `          IF (I1.NE.I2) THEN` (50). `            IF (I1.LE.I .AND. I.LE.IX) THEN` (51). `              IF (J1.LE.J .AND. J.LE.J2) THEN` (52). `                IF (K1.LE.K .AND. K.LE.K2) THEN` (53). `                  NBX=NBX+1` (54). `                ENDIF` (55). `              ENDIF` (56). `            ENDIF` (57). `          ENDIF` (58). `        ELSEIF (NS.EQ.3 .OR. NS.EQ.4) THEN` (59). `          IF (J1.NE.J2) THEN` (60). `            IF (I1.LE.I .AND. I.LE.I2) THEN` (61). `              IF (J1.LE.J .AND. J.LE.JY) THEN` (62). `                IF (K1.LE.K .AND. K.LE.K2) THEN` (63). `                  NBY=NBY+1` (64). `                ENDIF` (65). `              ENDIF` (66). `            ENDIF` (67). `          ENDIF` (68). |
| 69–89 | 시작 시 1행 루틴 `SUBROUTINE VF_OGBCNM`, 42행 DO 루프 100 `DO 100 L=1,NUMB`, 49행 `IF     (NS.EQ.1 .OR. NS.EQ.2) THEN`에서 열린 분기문 안. 이 구간의 69행 ELSE는 앞선 조건과 `ELSEIF (NS.EQ.3 .OR. NS.EQ.4) THEN`이 모두 거짓일 때의 분기이다. 이 IF는 79행 ENDIF에서 닫힌다. L 루프는 80행 레이블 100에서 닫힌다. 나머지 NS는 z면 분기로 처리하여 NBZ를 센다. 루프 종료 뒤 반환한다. 원문: `        ELSE` (69). `          IF (K1.NE.K2) THEN` (70). `            IF (I1.LE.I .AND. I.LE.I2) THEN` (71). `              IF (J1.LE.J .AND. J.LE.J2) THEN` (72). `                IF (K1.LE.K .AND. K.LE.KZ) THEN` (73). `                  NBZ=NBZ+1` (74). `                ENDIF` (75). `              ENDIF` (76). `            ENDIF` (77). `          ENDIF` (78). `        ENDIF` (79). ` 100  CONTINUE` (80). `C     -- 実行文の終了 --` (82) (실행문 종료). `      GOTO 9999` (83). `C==== 終了 ===========================================================` (85) (종료). ` 9999 CONTINUE` (87). `      RETURN` (88). `      END` (89). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 49–78: NS=1,2는 x면, NS=3,4는 y면으로 처리한다. 나머지 값은 ELSE에서 z면으로 처리한다.
- 50·60·70: 출력 영역의 해당 방향 시작과 끝이 같으면 그 방향 경계 수를 증가시키지 않는다.
