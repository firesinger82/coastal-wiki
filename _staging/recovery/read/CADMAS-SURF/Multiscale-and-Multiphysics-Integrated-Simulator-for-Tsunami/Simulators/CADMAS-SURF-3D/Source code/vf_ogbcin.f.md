---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_ogbcin.f
lines: 93
sha256: 358287eec099485f36b395cfd5e0f35e5fbc520d20a4726dd0a117b25a4136e4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_ogbcin.f — 판독 구간 기록

구간은 1행부터 93행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | 도화 경계 인덱스 구성 루틴의 형식·포함 파일과 경계 배열을 선언한다. 원문: `      SUBROUTINE VF_OGBCIN(INDB,NWKBC,NBX,NBY,NBZ)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_OGBCIN:図化用の境界のインデックスを配列に格納する` (5) (도화용 경계 인덱스를 배열에 저장한다). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형식). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C     -- 大域変数 --` (12) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (13). `      INCLUDE 'VF_AFILEI.h'` (14). `      INCLUDE 'VF_ANUMBI.h'` (15). `      INCLUDE 'VF_APARAI.h'` (16). `CD    -- 引数 --` (18) (인수). `CD    INDB (MAXB1,NUMB) : IN  : I*4 : 境界面のインデックス` (19) (경계면 인덱스(index)). `CD    NWKBC(NUMB)       : OUT : I*4 : ワーク配列` (20) (작업 배열). `CD    NBX               : IN  : I*4 : x方向境界面の数` (21) (x방향 경계면 수). `CD    NBY               : IN  : I*4 : y方向境界面の数` (22) (y방향 경계면 수). `CD    NBZ               : IN  : I*4 : z方向境界面の数` (23) (z방향 경계면 수). `      DIMENSION INDB(MAXB1,NUMB),NWKBC(NUMB)` (24). `C==== 実行 ===========================================================` (26) (실행). |
| 28–41 | 시작 시 1행 루틴 `SUBROUTINE VF_OGBCIN` 안. 전역 출력 범위를 지역 I,J 소유 범위로 제한한다. 면별 상한은 IX=I2+1, JY=J2+1, KZ=K2+1로 설정한다. x,y,z 저장 구간의 시작 카운터를 설정한다. 원문: `CD    -- 初期設定 --` (28) (초기 설정). `      I1=MAX(IGRARA(1)-(MYGIS-1),MYIS)` (29). `      J1=MAX(IGRARA(2)-(MYGJS-1),MYJS)` (30). `      K1=IGRARA(3)` (31). `      I2=MIN(IGRARA(4)-(MYGIS-1),MYIE)` (32). `      J2=MIN(IGRARA(5)-(MYGJS-1),MYJE)` (33). `      K2=IGRARA(6)` (34). `      IX=I2+1` (35). `      JY=J2+1` (36). `      KZ=K2+1` (37). `      NX=0` (38). `      NY=NBX` (39). `      NZ=NBX+NBY` (40). |
| 42–71 | 시작 시 1행 루틴 `SUBROUTINE VF_OGBCIN` 안. NUMB 경계를 순회하며 선형 인덱스(linear index)를 I,J,K로 풀어낸다. NS=1,2는 x면, NS=3,4는 y면으로 판정한다. 방향별 두께 및 영역 조건을 통과한 인덱스를 각 구간에 저장한다. 원문: `CD    -- 数を数える --` (42) (수를 센다). `      DO 100 L=1,NUMB` (43). `        IJK=INDB(1,L)` (44). `        NS =INDB(2,L)` (45). `        K  =(IJK-1)/(NUMI*NUMJ)+1` (46). `        IJK=IJK-NUMI*NUMJ*(K-1)` (47). `        J  =(IJK-1)/NUMI+1` (48). `        I  =IJK-NUMI*(J-1)` (49). `        IF     (NS.EQ.1 .OR. NS.EQ.2) THEN` (50). `          IF (I1.NE.I2) THEN` (51). `            IF (I1.LE.I .AND. I.LE.IX) THEN` (52). `              IF (J1.LE.J .AND. J.LE.J2) THEN` (53). `                IF (K1.LE.K .AND. K.LE.K2) THEN` (54). `                  NX=NX+1` (55). `                  NWKBC(NX)=INDB(1,L)` (56). `                ENDIF` (57). `              ENDIF` (58). `            ENDIF` (59). `          ENDIF` (60). `        ELSEIF (NS.EQ.3 .OR. NS.EQ.4) THEN` (61). `          IF (J1.NE.J2) THEN` (62). `            IF (I1.LE.I .AND. I.LE.I2) THEN` (63). `              IF (J1.LE.J .AND. J.LE.JY) THEN` (64). `                IF (K1.LE.K .AND. K.LE.K2) THEN` (65). `                  NY=NY+1` (66). `                  NWKBC(NY)=INDB(1,L)` (67). `                ENDIF` (68). `              ENDIF` (69). `            ENDIF` (70). `          ENDIF` (71). |
| 72–93 | 시작 시 1행 루틴 `SUBROUTINE VF_OGBCIN`, 43행 DO 루프 100 `DO 100 L=1,NUMB`, 50행 `IF     (NS.EQ.1 .OR. NS.EQ.2) THEN`에서 열린 분기문 안. 이 구간의 72행 ELSE는 앞선 조건과 `ELSEIF (NS.EQ.3 .OR. NS.EQ.4) THEN`이 모두 거짓일 때의 분기이다. 이 IF는 83행 ENDIF에서 닫힌다. L 루프는 84행 레이블 100에서 닫힌다. 나머지 NS는 z면 분기로 처리한다. z방향 두께 및 출력 범위 조건을 통과한 인덱스를 저장한 뒤 반환한다. 원문: `        ELSE` (72). `          IF (K1.NE.K2) THEN` (73). `            IF (I1.LE.I .AND. I.LE.I2) THEN` (74). `              IF (J1.LE.J .AND. J.LE.J2) THEN` (75). `                IF (K1.LE.K .AND. K.LE.KZ) THEN` (76). `                  NZ=NZ+1` (77). `                  NWKBC(NZ)=INDB(1,L)` (78). `                ENDIF` (79). `              ENDIF` (80). `            ENDIF` (81). `          ENDIF` (82). `        ENDIF` (83). ` 100  CONTINUE` (84). `C     -- 実行文の終了 --` (86) (실행문 종료). `      GOTO 9999` (87). `C==== 終了 ===========================================================` (89) (종료). ` 9999 CONTINUE` (91). `      RETURN` (92). `      END` (93). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 50–82: x면은 I1!=I2, y면은 J1!=J2, z면은 K1!=K2인 경우에만 수록한다.
- 61–78: NS=1,2,3,4 이외의 값은 별도 NS=5,6 검사 없이 ELSE의 z면 처리로 들어간다.
