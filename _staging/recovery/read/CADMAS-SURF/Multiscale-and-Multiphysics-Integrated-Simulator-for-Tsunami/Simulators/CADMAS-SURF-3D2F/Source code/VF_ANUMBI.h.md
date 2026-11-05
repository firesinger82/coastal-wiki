---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/VF_ANUMBI.h
lines: 23
sha256: cb96f0732445da6a40903737655affa00f1d0efcd28aef810d9aec821eace6ac
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_ANUMBI.h — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | /VF_ANUMBI/는 격자·경계·표면 셀 수와 방정식 계산 플래그(flag)를 공유한다. 원문: `      COMMON /VF_ANUMBI/ NUMI,NUMJ,NUMK,NUMB,NUMB0,NUMS,LEQK,LEQT,LEQC` (1); `CD=== 概要 ===========================================================` (3) (개요); `CDT   VF_ANUMBI.h:データ数関連(配列サイズおよび格子数等):整数` (5) (배열 크기와 격자 수 등 데이터 수 관련 정수); `C==== 内容 ===========================================================` (7) (내용) |
| 9–23 | NUMI·NUMJ·NUMK는 방향별 격자 수+1, 셀 수+2로 설명된다. NUMB·NUMB0·NUMS와 k-ε·온도·농도 계산 제어의 의미를 설명한다. 설정값을 대입하지 않는다. 원문: `CD    NUMI  : CNS : I*4 : x方向格子数+1(x方向セル数+2)` (9) (x방향 격자 수+1, x방향 셀 수+2); `CD    NUMJ  : CNS : I*4 : y方向格子数+1(y方向セル数+2)` (10) (y방향 격자 수+1, y방향 셀 수+2); `CD    NUMK  : CNS : I*4 : z方向格子数+1(z方向セル数+2)` (11) (z방향 격자 수+1, z방향 셀 수+2); `CD    NUMB  : CNS : I*4 : 境界面の数` (12) (경계면 수); `CD    NUMB0 : CNS : I*4 : 境界面の数(移動障害物処理用)` (13) (이동 장애물 처리용 경계면 수); `CD    NUMS  : TRN : I*4 : 表面セルの数` (14) (표면 셀 수); `CD    LEQK  : CNS : I*4 : k-εを計算するかしないか` (15) (k-ε 계산 여부); `CD                        = 0:計算しない` (16) (0: 계산하지 않음); `CD                        !=0:計算する` (17) (비영: 계산); `CD    LEQT  : CNS : I*4 : 温度を計算するかしないか` (18) (온도 계산 여부); `CD                        = 0:計算しない` (19) (0: 계산하지 않음); `CD                        !=0:計算する` (20) (비영: 계산); `CD    LEQC  : CNS : I*4 : 濃度を計算するかしないか` (21) (농도 계산 여부); `CD                        = 0:計算しない` (22) (0: 계산하지 않음); `CD                        >=1:成分数` (23) (1 이상: 성분 수) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
