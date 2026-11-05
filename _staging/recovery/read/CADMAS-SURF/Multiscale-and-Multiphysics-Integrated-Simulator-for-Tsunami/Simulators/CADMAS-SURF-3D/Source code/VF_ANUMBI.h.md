---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/VF_ANUMBI.h
lines: 26
sha256: 083c77097381ef367149306c1fbe9dffeed29b342e79b4fe917e4dac629a297f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_ANUMBI.h — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `COMMON /VF_ANUMBI/`의 전체 변수 목록을 보존한다(2–3). 6열 &로 이어진 두 줄은 하나의 COMMON 문이다. 개요는 배열 크기·격자 수 등 데이터 수 관련 정수다. 원문: `C-*- mode:fortran; -*-` (1); `      COMMON /VF_ANUMBI/ NUMI,NUMJ,NUMK,NUMB,NUMS,LEQK,LEQT,LEQC,NUMIJ` (2); `     &                  ,NUMBX` (3); `CD=== 概要 ===========================================================` (5) (개요); `CDT   VF_ANUMBI.h:データ数関連(配列サイズおよび格子数等):整数` (7) (배열 크기·격자 수 등 데이터 수 관련 정수); `C==== 内容 ===========================================================` (9) (내용) |
| 11–26 | NUMI/J/K는 각 방향 격자 수+1이자 셀 수+2, NUMB는 경계면 수, NUMS는 표면 셀 수다. LEQK·LEQT는 0이면 미계산·0 이외면 계산한다는 설명이며 LEQC는 0이면 미계산·1 이상이면 성분 수다. NUMIJ는 조파(wave generation) 소스용 수평 격자 수+1, NUMBX는 MAX(NUMB,1)이라는 주석이다. 원문: `CD    NUMI  : CNS : I*4 : x方向格子数+1(x方向セル数+2)` (11) (x 방향 격자 수+1이며 x 방향 셀 수+2); `CD    NUMJ  : CNS : I*4 : y方向格子数+1(y方向セル数+2)` (12) (y 방향 격자 수+1이며 y 방향 셀 수+2); `CD    NUMK  : CNS : I*4 : z方向格子数+1(z方向セル数+2)` (13) (z 방향 격자 수+1이며 z 방향 셀 수+2); `CD    NUMB  : CNS : I*4 : 境界面の数` (14) (경계면 수); `CD    NUMS  : TRN : I*4 : 表面セルの数` (15) (표면 셀 수); `CD    LEQK  : CNS : I*4 : k-εを計算するかしないか` (16) (k-ε 계산 여부); `CD                        = 0:計算しない` (17) (0은 계산하지 않음); `CD                        !=0:計算する` (18) (0 이외는 계산함); `CD    LEQT  : CNS : I*4 : 温度を計算するかしないか` (19) (온도 계산 여부); `CD                        = 0:計算しない` (20) (0은 계산하지 않음); `CD                        !=0:計算する` (21) (0 이외는 계산함); `CD    LEQC  : CNS : I*4 : 濃度を計算するかしないか` (22) (농도 계산 여부); `CD                        = 0:計算しない` (23) (0은 계산하지 않음); `CD                        >=1:成分数` (24) (1 이상은 성분 수); `CD    NUMIJ : CNS : I*4 : 造波ソース用水平方向格子数+1` (25) (조파(wave generation) 소스용 수평 방향 격자 수+1); `CD    NUMBX : CNS : I*4 : =MAX(NUMB,1)` (26) (MAX(NUMB,1)) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
