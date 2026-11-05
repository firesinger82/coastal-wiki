---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/VF_ACOMPI.h
lines: 41
sha256: eb75074ea88308456f4c43519013b535bbd4b9c6ec47c8e6187831836da589bc
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_ACOMPI.h — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | /VF_ACOMPI/는 수치해법 정수 제어값을 공유한다. 1–2·4행이 한 COMMON 연속 문장이며 ISCMC(MAXNC), ISTATE, MAXITR를 포함한다. 원문: `      COMMON /VF_ACOMPI/ ICGTYP,ICGMAX,ICGITR,ISCMVP,ISCMFF,` (1); `     &                   ISCMK,ISCMT,ISCMC(MAXNC),IBSUW0` (2); `     &                  ,ISTATE,MAXITR` (4) |
| 7–41 | 전처리(preconditioning) 종류·반복 횟수·이류(advection) 차분법·표면 셀 속도·기상 압축 제어값의 설명이다. 주석의 0·비영 값 설명은 초기값 설정이 아니다. 원문: `CD=== 概要 ===========================================================` (7) (개요); `CDT   VF_ACOMPI.h:数値解法関連(各種パラメータおよび反復回数等):整数` (9) (수치해법 관련 각종 매개변수와 반복 횟수 등의 정수); `C==== 内容 ===========================================================` (11) (내용); `CD    ICGTYP : CNS : I*4 : 連立1次方程式の解法の前処理の種類` (13) (연립 일차방정식 해법의 전처리 종류); `CD                         = 0:不完全LU分解(ILU)` (14) (0: 불완전 LU 분해(incomplete LU, ILU)); `CD                         !=0:修正不完全LU分解(MILU)` (15) (비영: 수정 불완전 LU 분해(modified ILU, MILU)); `CD    ICGMAX : CNS : I*4 : 連立1次方程式の解法の最大反復回数` (16) (연립 일차방정식 해법의 최대 반복 횟수); `CD    ICGITR : TRN : I*4 : 連立1次方程式の解法の反復回数` (17) (연립 일차방정식 해법의 반복 횟수); `CD    ISCMVP : CNS : I*4 : 流速の対流項の差分スキーム` (18) (유속 대류항의 차분법); `CD                         = 0:DONOR` (19); `CD                         !=0:????? CAKIY` (20); `CD    ISCMFF : CNS : I*4 : VOF関数Fの対流項の差分スキーム` (21) (VOF 함수 대류항의 차분법); `CD                         = 0:ドナー・アクセプタ法` (22) (0: 도너·억셉터법(donor–acceptor method)); `CD                         !=0:界面の傾きを考慮した方法` (23) (비영: 계면 경사를 고려하는 방법); `CD    ISCMK  : CNS : I*4 : k-εの移流項の差分スキーム` (24) (k-ε 이류항 차분법); `CD                         = 0:DONOR` (25); `CD                         !=0:?????` (26); `CD    ISCMT  : CNS : I*4 : 温度の移流項の差分スキーム` (27) (온도 이류항 차분법); `CD                         = 0:DONOR` (28); `CD                         !=0:?????` (29); `CD    ISCMC(MAXNC) : CNS : I*4 : 濃度の移流項の差分スキーム` (30) (농도 이류항 차분법); `CD                         = 0:DONOR` (31); `CD                         !=0:?????` (32); `CD    IBSUW0 : CNS : I*4 : 表面セルの流速計算法` (33) (표면 셀 유속 계산법); `CD                         =0 :流体側から補外できる場合は線形補外` (34) (0: 유체 쪽에서 외삽(extrapolation)할 수 있으면 선형 외삽); `CD                         !=0:勾配ゼロ` (35) (비영: 기울기 0); `CD    ISTATE : CNS : I*4 : 気相圧縮` (37) (기상 압축); `CD                         =0 :考慮しない` (38) (0: 고려하지 않음); `CD                         =1 :等温変化` (39) (1: 등온 변화); `CD    MAXITR : CNS : I*4 : 密度収束計算における最大反復回数` (40) (밀도 수렴 계산의 최대 반복 횟수) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
