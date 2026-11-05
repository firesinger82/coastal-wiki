---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/VF_ACOMPR.h
lines: 48
sha256: 83d438f773c68afdcdfa9431e02ea4d6b76d83db9d5af2f5e2b1ba894189af04
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_ACOMPR.h — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | /VF_ACOMPR/는 수치해법 실수 제어값·노름(norm)·VOF 함수 한계값·차분 계수·상태방정식(equation of state) 계수를 공유한다. 1–3·5행이 하나의 COMMON 문장이다. 배열 SCMC(MAXNC)·SPARAM(MAXWDS-3)를 포함한다. 원문: `      COMMON /VF_ACOMPR/ CGPARA,CGEPSA,CGEPSR,CGDIV ,CGBNRM,CGXNRM,` (1); `     &                   FEPS  ,FLOWER,FUPPER,FSUM  ,FCUT  ,PLOWER,` (2); `     &                   SCMVP ,SCMK  ,SCMT  ,SCMC(MAXNC)` (3); `     &                  ,SPARAM(MAXWDS-3),SERROR,SRELAX` (5) |
| 8–38 | MILU 계수·수렴/발산 판정·VOF 함수 적분·포러스 값 하한·DONOR 계수의 설명이다. 0.0은 2차 중심차분이고 1.0은 1차 상류차분이라는 주석이다. 원문: `CD=== 概要 ===========================================================` (8) (개요); `CDT   VF_ACOMPR.h:数値解法関連(各種パラメータおよび反復回数等):実数` (10) (수치해법 관련 각종 매개변수와 반복 횟수 등의 실수); `C==== 内容 ===========================================================` (12) (내용); `CD    CGPARA : CNS : R*8 : 連立1次方程式の解法のMILU用パラメータ` (14) (연립 일차방정식 해법의 MILU 매개변수); `CD    CGEPSA : CNS : R*8 : 連立1次方程式の解法の収束判定値(絶対誤差)` (15) (연립 일차방정식 해법의 절대 오차 수렴 판정값); `CD    CGEPSR : CNS : R*8 : 連立1次方程式の解法の収束判定値(相対誤差)` (16) (연립 일차방정식 해법의 상대 오차 수렴 판정값); `CD    CGDIV  : CNS : R*8 : 連立1次方程式の解法の発散判定値` (17) (연립 일차방정식 해법의 발산 판정값); `CD    CGBNRM : TRN : R*8 : 連立1次方程式の解法の右辺のノルム` (18) (연립 일차방정식 해법 우변의 노름(norm)); `CD    CGXNRM : TRN : R*8 : 連立1次方程式の解法の残差のノルム` (19) (연립 일차방정식 해법 잔차의 노름(norm)); `CD    FEPS   : CNS : R*8 : VOF関数Fのゼロ判定値` (20) (VOF 함수의 영 판정값); `CD    FLOWER : CNS : R*8 : VOF関数Fの下限値` (21) (VOF 함수 하한); `CD    FUPPER : CNS : R*8 : VOF関数Fの上限値` (22) (VOF 함수 상한); `CD    FSUM   : TRN : R*8 : VOF関数Fの空間積分値` (23) (VOF 함수 공간 적분값); `CD    FCUT   : TRN : R*8 : VOF関数Fのカットオフ値` (24) (VOF 함수 절단값(cutoff)); `CD    PLOWER : CNS : R*8 : ポーラス値の下限値` (25) (포러스 값 하한); `CD    SCMVP  : CNS : R*8 : DONORスキームのパラメータ(流速用)` (26) (유속용 DONOR 차분법 매개변수); `CD                         =0.0:2次中心` (27) (0.0: 2차 중심차분); `CD                         =1.0:1次風上` (28) (1.0: 1차 상류차분); `CD    SCMK   : CNS : R*8 : DONORスキームのパラメータ(k-ε用)` (29) (k-ε용 DONOR 차분법 매개변수); `CD                         =0.0:2次中心` (30) (0.0: 2차 중심차분); `CD                         =1.0:1次風上` (31) (1.0: 1차 상류차분); `CD    SCMT   : CNS : R*8 : DONORスキームのパラメータ(温度用)` (32) (온도용 DONOR 차분법 매개변수); `CD                         =0.0:2次中心` (33) (0.0: 2차 중심차분); `CD                         =1.0:1次風上` (34) (1.0: 1차 상류차분); `CD    SCMC(MAXNC) : CNS : R*8 : DONORスキームのパラメータ(濃度用)` (35) (농도용 DONOR 차분법 매개변수); `CD                         =0.0:2次中心` (36) (0.0: 2차 중심차분); `CD                         =1.0:1次風上` (37) (1.0: 1차 상류차분) [11-04 전수 검증 정정] |
| 39–48 | 시작 시 열린 실행 블록은 없다. SPARAM의 상태방정식과 ISTATE=1일 때 p0·R·T의 대응, 밀도 상대 수렴 오차·완화 계수(relaxation factor)의 설명이다. 이 파일에는 값 대입문이 없다. 원문: `CD    SPARAM : CNS : R*8 : 圧縮効果を現す状態方程式のパラメータ` (39) (압축 효과를 나타내는 상태방정식 매개변수); `CD                         ISTATE=1のとき` (40) (ISTATE=1일 때); `CD                              (p+p0)=ρRT` (41); `CD                         で` (42) (다음 대응에서); `CD                         SPARAM(1) = p0  : 基準圧力[Pa]` (43) (SPARAM(1)은 기준 압력 p0 [Pa]); `CD                         SPARAM(2) = R   : 気体定数[J/kg/K]` (44) (SPARAM(2)는 기체 상수 R [J/kg/K]); `CD                         SPARAM(3) = T   : 温度[K]` (45) (SPARAM(3)은 온도 T [K]); `CD    SERROR : CNS : R*8 : 密度収束計算における相対収束判定誤差[-]` (46) (밀도 수렴 계산의 상대 수렴 판정 오차 [-]); `CD    SRELAX : CNS : R*8 : 密度の緩和係数[-]` (47) (밀도 완화 계수 [-]) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
