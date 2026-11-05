---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/VF_ACOMPR.h
lines: 35
sha256: 8b4ac631d7d225bc14676d8b7173cb4c680de2e192c8ebbf2315fe7981ddf799
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_ACOMPR.h — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | `COMMON /VF_ACOMPR/`의 전체 변수 목록 및 SCMC(MAXNC)를 보존한다(2–4). 6열 &로 이어진 세 줄은 하나의 COMMON 문이다. 개요는 수치해법 관련 실수라고 설명한다. 원문: `C-*- mode:fortran; -*-` (1); `      COMMON /VF_ACOMPR/ CGPARA,CGEPSA,CGEPSR,CGDIV ,CGBNRM,CGXNRM,` (2); `     &                   FEPS  ,FLOWER,FUPPER,FSUM  ,FCUT  ,PLOWER,` (3); `     &                   SCMVP ,SCMK  ,SCMT  ,SCMC(MAXNC)` (4); `CD=== 概要 ===========================================================` (6) (개요); `CDT   VF_ACOMPR.h:数値解法関連(各種パラメータおよび反復回数等):実数` (8) (수치해법 매개변수·반복 횟수 관련 실수); `C==== 内容 ===========================================================` (10) (내용) |
| 12–23 | MILU(Modified Incomplete LU) 매개변수·절대/상대 수렴 한계·발산 한계·우변 및 잔차 노름(norm), VOF(Volume of Fluid) 함수의 0 판정·하한·상한·공간 적분·절단값(cutoff), 다공성 값 하한에 관한 일본어 주석과 한국어 뜻이다. 원문: `CD    CGPARA : CNS : R*8 : 連立1次方程式の解法のMILU用パラメータ` (12) (연립 일차방정식 해법의 MILU 매개변수); `CD    CGEPSA : CNS : R*8 : 連立1次方程式の解法の収束判定値(絶対誤差)` (13) (연립 일차방정식 해법 절대오차 수렴 판정값); `CD    CGEPSR : CNS : R*8 : 連立1次方程式の解法の収束判定値(相対誤差)` (14) (연립 일차방정식 해법 상대오차 수렴 판정값); `CD    CGDIV  : CNS : R*8 : 連立1次方程式の解法の発散判定値` (15) (연립 일차방정식 해법 발산 판정값); `CD    CGBNRM : TRN : R*8 : 連立1次方程式の解法の右辺のノルム` (16) (연립 일차방정식 우변 노름(norm)); `CD    CGXNRM : TRN : R*8 : 連立1次方程式の解法の残差のノルム` (17) (연립 일차방정식 잔차 노름); `CD    FEPS   : CNS : R*8 : VOF関数Fのゼロ判定値` (18) (VOF(Volume of Fluid) 함수 0 판정값); `CD    FLOWER : CNS : R*8 : VOF関数Fの下限値` (19) (VOF 함수 하한값); `CD    FUPPER : CNS : R*8 : VOF関数Fの上限値` (20) (VOF 함수 상한값); `CD    FSUM   : TRN : R*8 : VOF関数Fの空間積分値` (21) (VOF 함수 공간 적분값); `CD    FCUT   : TRN : R*8 : VOF関数Fのカットオフ値` (22) (VOF 함수 절단값(cutoff)); `CD    PLOWER : CNS : R*8 : ポーラス値の下限値` (23) (다공성 값 하한) |
| 24–35 | 시작 시 실행 블록 밖인 설명부다. 유속·k-ε·온도·농도 DONOR 차분법 매개변수의 0.0=이차 중앙차분·1.0=일차 상류차분 설명이다. 이 숫자는 해당 주석의 의미 설명이며 이 헤더에서 값을 대입하지 않는다. 원문: `CD    SCMVP  : CNS : R*8 : DONORスキームのパラメータ(流速用)` (24) (유속용 DONOR 차분법 매개변수); `CD                         =0.0:2次中心` (25) (0.0은 이차 중앙차분); `CD                         =1.0:1次風上` (26) (1.0은 일차 상류차분); `CD    SCMK   : CNS : R*8 : DONORスキームのパラメータ(k-ε用)` (27) (k-ε용 DONOR 차분법 매개변수); `CD                         =0.0:2次中心` (28) (0.0은 이차 중앙차분); `CD                         =1.0:1次風上` (29) (1.0은 일차 상류차분); `CD    SCMT   : CNS : R*8 : DONORスキームのパラメータ(温度用)` (30) (온도용 DONOR 차분법 매개변수); `CD                         =0.0:2次中心` (31) (0.0은 이차 중앙차분); `CD                         =1.0:1次風上` (32) (1.0은 일차 상류차분); `CD    SCMC(MAXNC) : CNS : R*8 : DONORスキームのパラメータ(濃度用)` (33) (농도용 DONOR 차분법 매개변수); `CD                         =0.0:2次中心` (34) (0.0은 이차 중앙차분); `CD                         =1.0:1次風上` (35) (1.0은 일차 상류차분) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
