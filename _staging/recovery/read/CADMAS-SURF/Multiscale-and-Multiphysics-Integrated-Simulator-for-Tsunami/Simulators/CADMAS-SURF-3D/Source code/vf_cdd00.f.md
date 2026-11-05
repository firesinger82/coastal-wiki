---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_cdd00.f
lines: 78
sha256: 07a82137455769d463fb4550e5609c0b9cc473ff2330614c368690b26d2cf1cd
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cdd00.f — 판독 구간 기록

구간은 1행부터 78행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 확산 계수 합 계산 루틴과 와동 점성 계수(eddy viscosity)·성분별 DD 배열을 선언한다. 원문: `      SUBROUTINE VF_CDD00(ANUT,DD,NF)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_CDD00:拡散係数と乱流拡散係数の和を計算する` (5) (VF_CDD00:확산 계수와 난류 확산 계수의 합 계산). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C     -- 大域変数 --` (12) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (13). `      INCLUDE 'VF_ANUMBI.h'` (14). `      INCLUDE 'VF_APARAI.h'` (15). `      INCLUDE 'VF_APHYSR.h'` (16). `CD    -- 引数 --` (18) (인수). `CD    ANUT(@FOR-3D@)    : IN  : R*8 : 渦動粘性係数νt` (19) (ANUT(@FOR-3D@)    : IN  : R*8 : 와동 점성 계수(eddy viscosity) νt). `CD    DD(@FOR-3D@,LEQC) : I/O : R*8 : 拡散係数と乱流拡散係数の和` (20) (DD(@FOR-3D@,LEQC) : I/O : R*8 : 확산 계수와 난류 확산 계수의 합). `CD    NF(@FOR-3D@)      : IN  : I*4 : セルの状態を示すインデックス` (21) (NF(@FOR-3D@)      : IN  : I*4 : 셀 상태 지표(index)). `      DIMENSION ANUT(NUMI,NUMJ,NUMK),DD(NUMI,NUMJ,NUMK,LEQC)` (22). `      DIMENSION NF  (NUMI,NUMJ,NUMK)` (23). `C==== 実行 ===========================================================` (25) (실행). |
| 27–52 | 시작 시 `      SUBROUTINE VF_CDD00(ANUT,DD,NF)` (1) 블록 안. 병렬 경계에 따라 x,y 범위를 정한다. LEQK=0이면 비장애물 셀은 CDF0(LC),장애물 셀은 0으로 설정한다. NF의 유체·기체·장애물 구분 근거는 vf_cindc.f:38–49의 주석과 조건이다. 원문: `CD    -- 並列時の範囲変更 --` (27) (병렬 처리 시 범위 변경). `      IA=1` (28). `      IB=NUMI` (29). `      JA=1` (30). `      JB=NUMJ` (31). `      IF (MYMIS.EQ.1) IA=2` (32). `      IF (MYMIE.EQ.1) IB=NUMI-1` (33). `      IF (MYMJS.EQ.1) JA=2` (34). `      IF (MYMJE.EQ.1) JB=NUMJ-1` (35). `CD    -- 乱流モデルを使用しない場合 --` (37) (난류 모델(turbulence model)을 사용하지 않을 때). `      IF (LEQK.EQ.0) THEN` (38). `        DO 130 LC=1,LEQC` (39). `          DO 120 K=2,NUMK-1` (40). `            DO 110 J=JA,JB` (41). `              DO 100 I=IA,IB` (42). `                IF (NF(I,J,K).NE.-1) THEN` (43). `                  DD(I,J,K,LC)=CDF0(LC)` (44). `                ELSE` (45). `                  DD(I,J,K,LC)=0.0D0` (46). `                ENDIF` (47). ` 100          CONTINUE` (48). ` 110        CONTINUE` (49). ` 120      CONTINUE` (50). ` 130    CONTINUE` (51). [11-04 전수 검증 보완] |
| 53–78 | 시작 시 `      SUBROUTINE VF_CDD00(ANUT,DD,NF)` (1), `      IF (LEQK.EQ.0) THEN` (38) 블록 안에서 시작한다. 54행 ELSE는 LEQK가 0이 아닌 분기이다. 38행 IF는 69행 ENDIF에서 닫힌다. 난류 모델(turbulence model)을 사용하면 각 성분에서 AKSM의 역수를 구하고 비장애물 셀의 확산 계수에 ANUT/AKSM을 더한다. 장애물은 0으로 한다. NF의 유체·기체·장애물 구분 근거는 vf_cindc.f:38–49의 주석과 조건이다. 원문: `CD    -- 乱流モデルを使用する場合 --` (53) (난류 모델(turbulence model)을 사용할 때). `      ELSE` (54). `        DO 230 LC=1,LEQC` (55). `          W=1.0D0/AKSM(LC)` (56). `          DO 220 K=2,NUMK-1` (57). `            DO 210 J=JA,JB` (58). `              DO 200 I=IA,IB` (59). `                IF (NF(I,J,K).NE.-1) THEN` (60). `                  DD(I,J,K,LC)=CDF0(LC)+ANUT(I,J,K)*W` (61). `                ELSE` (62). `                  DD(I,J,K,LC)=0.0D0` (63). `                ENDIF` (64). ` 200          CONTINUE` (65). ` 210        CONTINUE` (66). ` 220      CONTINUE` (67). ` 230    CONTINUE` (68). `      ENDIF` (69). `C     -- 実行文の終了 --` (71) (실행문 종료). `      GOTO 9999` (72). `C==== 終了 ===========================================================` (74) (종료). ` 9999 CONTINUE` (76). `      RETURN` (77). `      END` (78). [11-04 전수 검증 정정] [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 56·61: AKSM(LC)의 역수를 사용하며 이 루틴에는 AKSM(LC)=0 검사문이 없다.
