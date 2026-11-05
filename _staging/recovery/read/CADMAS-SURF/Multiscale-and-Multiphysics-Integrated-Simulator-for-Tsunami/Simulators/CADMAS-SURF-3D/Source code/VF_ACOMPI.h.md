---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/VF_ACOMPI.h
lines: 33
sha256: 2b116bc65228480b4ea678f6247d5de57bb502da81ad9ba7e9e8662ef5269c27
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_ACOMPI.h — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `COMMON /VF_ACOMPI/`의 전체 변수 목록과 ISCMC(MAXNC)를 보존한다(2–3). 6열 &의 두 줄은 하나의 COMMON 문이다. 개요는 수치해법 관련 정수이며 각종 매개변수·반복 횟수 등을 담는다고 한다. 원문: `C-*- mode:fortran; -*-` (1); `      COMMON /VF_ACOMPI/ ICGTYP,ICGMAX,ICGITR,ISCMVP,ISCMFF,` (2); `     &                   ISCMK,ISCMT,ISCMC(MAXNC),IBSUW0` (3); `CD=== 概要 ===========================================================` (5) (개요); `CDT   VF_ACOMPI.h:数値解法関連(各種パラメータおよび反復回数等):整数` (7) (수치해법의 매개변수·반복 횟수 관련 정수); `C==== 内容 ===========================================================` (9) (내용) |
| 11–33 | 전처리 ILU·MILU, 반복 최대 횟수·현재 횟수, 유속·VOF(Volume of Fluid) 함수·k-ε·온도·농도 대류 또는 이류 차분법, 표면 셀 유속 계산법을 설명한다. 주석의 =0·!=0 구분과 미기재 ????? 문구를 그대로 보존한다. 일본어 뜻을 각 행에 덧붙인다. 원문: `CD    ICGTYP : CNS : I*4 : 連立1次方程式の解法の前処理の種類` (11) (연립 일차방정식 해법의 전처리 종류); `CD                         = 0:不完全LU分解(ILU)` (12) (0은 불완전 LU 분해(ILU)); `CD                         !=0:修正不完全LU分解(MILU)` (13) (0 이외는 수정 불완전 LU 분해(MILU)); `CD    ICGMAX : CNS : I*4 : 連立1次方程式の解法の最大反復回数` (14) (연립 일차방정식 해법 최대 반복 횟수); `CD    ICGITR : TRN : I*4 : 連立1次方程式の解法の反復回数` (15) (연립 일차방정식 해법 반복 횟수); `CD    ISCMVP : CNS : I*4 : 流速の対流項の差分スキーム` (16) (유속 대류항 차분법); `CD                         = 0:DONOR` (17) (0은 DONOR); `CD                         !=0:????? CAKIY` (18) (0 이외는 원문에 ????? CAKIY라고 표기); `CD    ISCMFF : CNS : I*4 : VOF関数Fの対流項の差分スキーム` (19) (VOF(Volume of Fluid) 함수의 대류항 차분법); `CD                         = 0:ドナー・アクセプタ法` (20) (0은 도너 액셉터법(donor-acceptor method)); `CD                         !=0:界面の傾きを考慮した方法` (21) (0 이외는 계면 기울기를 고려하는 방법); `CD    ISCMK  : CNS : I*4 : k-εの移流項の差分スキーム` (22) (k-ε 이류항 차분법); `CD                         = 0:DONOR` (23) (0은 DONOR); `CD                         !=0:?????` (24) (0 이외는 원문에 ?????로 표기); `CD    ISCMT  : CNS : I*4 : 温度の移流項の差分スキーム` (25) (온도 이류항 차분법); `CD                         = 0:DONOR` (26) (0은 DONOR); `CD                         !=0:?????` (27) (0 이외는 원문에 ?????로 표기); `CD    ISCMC(MAXNC) : CNS : I*4 : 濃度の移流項の差分スキーム` (28) (농도 이류항 차분법); `CD                         = 0:DONOR` (29) (0은 DONOR); `CD                         !=0:?????` (30) (0 이외는 원문에 ?????로 표기); `CD    IBSUW0 : CNS : I*4 : 表面セルの流速計算法` (31) (표면 셀 유속 계산법); `CD                         =0 :流体側から補外できる場合は線形補外` (32) (0은 유체 쪽에서 외삽(extrapolation)할 수 있으면 선형 외삽); `CD                         !=0:勾配ゼロ` (33) (0 이외는 기울기 0) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18·24·27·30: 0 이외 차분법 설명에 ?????가 남아 있다.
- 2–3: COMMON 목록을 선언하며 이 파일 안에는 각 변수의 초기값 대입이 없다.
