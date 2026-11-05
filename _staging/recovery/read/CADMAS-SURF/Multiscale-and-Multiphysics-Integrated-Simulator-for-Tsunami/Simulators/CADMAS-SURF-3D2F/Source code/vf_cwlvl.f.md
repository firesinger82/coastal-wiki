---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_cwlvl.f
lines: 68
sha256: 05d1f2ab0a890d38bda5e85c08e480039d663bcbd452b89d4cf75933ee572aa5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cwlvl.f — 판독 구간 기록

구간은 1행부터 68행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | 지정 수평 위치의 수위 변동 계산 루틴과 선언이다(1–27).<br>`      SUBROUTINE VF_CWLVL(ZZ,FF,VAL,NF,IIN,JIN)` (1).<br>`CD=== 概要 ===========================================================` (3) (개요).<br>`CDT   VF_CWLVL:水位変動を計算する` (5) (VF_CWLVL:수위 변동을 계산한다).<br>`C==== 宣言 ===========================================================` (7) (선언).<br>`C     -- 大域型 --` (9) (전역 형).<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10).<br>`C     -- 大域変数 --` (12) (전역 변수).<br>`      INCLUDE 'VF_A0PRM.h'` (13).<br>`      INCLUDE 'VF_ANUMBI.h'` (14).<br>`      INCLUDE 'VF_APARAI.h'` (15).<br>`      INCLUDE 'VF_APHYSR.h'` (16).<br>`CD    -- 引数 --` (18) (인수).<br>`CD    ZZ(MAXG1,NUMK) : IN  : R*8 : z方向格子座標等` (19) (ZZ(MAXG1,NUMK) : IN  : R*8 : z방향 격자 좌표 등).<br>`CD    FF(@FOR-3D@)   : IN  : R*8 : VOF関数F` (20) (FF(@FOR-3D@)   : IN  : R*8 : VOF 함수).<br>`CD    VAL            : OUT : R*8 : 水面の高さ` (21) (VAL            : OUT : R*8 : 수면 높이).<br>`CD    NF(@FOR-3D@)   : IN  : I*4 : セルの状態を示すインデックス` (22) (NF(@FOR-3D@)   : IN  : I*4 : 셀 상태를 나타내는 인덱스).<br>`CD    IIN            : IN  : I*4 : x方向セル番号` (23) (IIN            : IN  : I*4 : x방향 셀 번호).<br>`CD    JIN            : IN  : I*4 : y方向セル番号` (24) (JIN            : IN  : I*4 : y방향 셀 번호).<br>`      DIMENSION ZZ(MAXG1,NUMK)` (25).<br>`      DIMENSION FF(NUMI,NUMJ,NUMK)` (26).<br>`      DIMENSION NF(NUMI,NUMJ,NUMK)` (27).<br>`C==== 実行 ===========================================================` (29) (실행). |
| 31–51 | 시작 시 1행 SUBROUTINE VF_CWLVL 루틴 안. 전역 IIN/JIN을 로컬 위치로 옮기고 담당 영역 여부를 검사한다(32–36). NF<0 셀은 두께 전체, 나머지는 두께×F를 더한 뒤 초기 수위 기준을 뺀다(39–50).<br>`CD    -- 並列時のシフト分等 --` (31) (병렬 실행 시 인덱스 이동량 등).<br>`      IP=IIN-(MYGIS-1)` (32).<br>`      JP=JIN-(MYGJS-1)` (33).<br>연속행 문장: `      IF (MYIS.LE.IP .AND. IP.LE.MYIE .AND.` (35); `     &    MYJS.LE.JP .AND. JP.LE.MYJE      ) THEN` (36).<br>`CD      -- VOF関数Fをz方向に加える --` (38) (VOF 함수를 z방향으로 더한다).<br>`        SF=0.0D0` (39).<br>`        DO 100 K=2,NUMK-1` (40).<br>주석 원문(실행하지 않음): `CBUG      IF (NF(IP,JP,K).EQ.-1) THEN` (41).<br>`          IF (NF(IP,JP,K).LT.0) THEN` (42).<br>`            SF=SF+ZZ(2,K)*1.0D0` (43).<br>`          ELSE` (44).<br>`            SF=SF+ZZ(2,K)*FF(IP,JP,K)` (45).<br>`          ENDIF` (46).<br>` 100    CONTINUE` (47).<br>`CD      -- 初期水面の位置を基準とする --` (49) (초기 수면 위치를 기준으로 한다).<br>`        VAL=SF-(WVLVL-ZZ(1,2))` (50). |
| 52–68 | 시작 시 1행 SUBROUTINE VF_CWLVL 루틴·35행 조건 안. 담당 영역 밖은 VAL=0으로 둔다(52–56). W에 VAL을 복사한 뒤 `CALL VF_P1SUMD(W,VAL)`을 호출한다(58–59). 해석: 이 호출은 각 담당 영역의 값을 합산하기 위한 것으로 보인다.<br>`      ELSE` (52).<br>`        VAL=0.0D0` (54).<br>`      ENDIF` (56).<br>`      W=VAL` (58).<br>`      CALL VF_P1SUMD(W,VAL)` (59).<br>`C     -- 実行文の終了 --` (61) (실행문 종료).<br>`      GOTO 9999` (62).<br>`C==== 終了 ===========================================================` (64) (종료).<br>` 9999 CONTINUE` (66).<br>`      RETURN` (67).<br>`      END` (68).<br>바깥 조건 전체는 35–36행 `IF (MYIS.LE.IP .AND. IP.LE.MYIE .AND.`와 연속행 `     &    MYJS.LE.JP .AND. JP.LE.MYJE      ) THEN`이다. 52행 ELSE는 이 복합 조건이 거짓인 경로이다. 이 IF는 56행에서 닫힌다. [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41–45: NF=-1만 검사하던 조건은 CBUG 주석이다. 실행 조건은 NF<0이므로 음의 NF 모두에서 셀 두께 전체를 누적한다.
- 21·50: VAL 설명은 수면 높이이다. 실제 계산은 초기 수위 기준을 뺀 변동값이다.
