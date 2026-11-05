---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/VF_ACPUTR.h
lines: 46
sha256: e7f519abb154b625a21864a80f3398687301048da307f7f95eddb9a60a5b010f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_ACPUTR.h — 판독 구간 기록

구간은 1행부터 46행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 고정형식 PARAMETER 문(2–10)은 하나의 문장으로 타이머(timer) 처리 플래그 0..3, 전체 종류 수 겸용 KCP0AL=22, 세부 종류 인덱스 1..21을 정의한다. `COMMON /VF_ACPUTR/ CPUS(KCP0AL), CPUW(KCP0AL)`(11)을 보존한다. CPU(Central Processing Unit) 시간 계측 관련 매개변수·실수라는 개요다. 원문: `C-*- mode:fortran; -*-` (1); `      PARAMETER (ICPUIN=  0, ICPUST=  1, ICPUEN=  2, ICPUOU=  3,` (2); `     &           KCP0AL= 22,` (3); `     &           KCP1PR=  1, KCP1CL=  2,` (4); `     &           KCP2FL=  3, KCP2VL=  4, KCP2TT=  5, KCP2SS=  6,` (5); `     &           KCP2KE=  7, KCP2FF=  8,` (6); `     &           KCPVFL=  9, KCPVGN= 10, KCPVEL= 11, KCPVPC= 12,` (7); `     &           KCPVPS= 13, KCPVMD= 14,` (8); `     &           KCPFFL= 15, KCPFEL= 16, KCPFMD= 17, KCPFNF= 18,` (9); `     &           KCP9PL= 19, KCP9M1= 20, KCP9NF= 21             )` (10); `      COMMON /VF_ACPUTR/ CPUS(KCP0AL), CPUW(KCP0AL)` (11); `CD=== 概要 ===========================================================` (13) (개요); `CDT   VF_ACPUTR.h:CPU時間の計測関連(CPU時間等):パラメータと実数` (15) (CPU(Central Processing Unit) 시간 계측 관련 매개변수와 실수); `C==== 内容 ===========================================================` (17) (내용) |
| 19–46 | 초기화·시작·정지 합산·출력 타이머 처리, 전체·전처리·계산부·파일 입출력·유속 압력·온도·스칼라(scalar)·k-ε·VOF(Volume of Fluid) 함수 및 개별 루틴별 타이머 종류를 설명한다. 일부 상세 종류는 원문도 ...뿐이다. CPUS는 합계 CPU 시간, CPUW는 타이머 시작 시각이다. 원문: `CD    ICPUIN : PRM : I*4 : タイマー処理フラグ(初期化)` (19) (타이머(timer) 초기화 처리 플래그); `CD    ICPUST : PRM : I*4 : タイマー処理フラグ(スタート)` (20) (타이머 시작 처리 플래그); `CD    ICPUEN : PRM : I*4 : タイマー処理フラグ(止めて,合計をとる)` (21) (타이머 정지·합계 처리 플래그); `CD    ICPUOU : PRM : I*4 : タイマー処理フラグ(CPU時間を出力する)` (22) (CPU 시간 출력 처리 플래그); `CD    KCP0AL : PRM : I*4 : タイマー種別フラグ(全体,種別フラグ数を兼ねる)` (23) (전체 타이머 종류이며 종류 수를 겸함); `CD    KCP1PR : PRM : I*4 : タイマー種別フラグ(前処理）` (24) (전처리 타이머 종류); `CD    KCP1CL : PRM : I*4 : タイマー種別フラグ(計算部）` (25) (계산부 타이머 종류); `CD    KCP2FL : PRM : I*4 : タイマー種別フラグ(計算部/ファイル入出力）` (26) (계산부 파일 입출력 타이머); `CD    KCP2VL : PRM : I*4 : タイマー種別フラグ(計算部/流速・圧力）` (27) (계산부 유속·압력 타이머); `CD    KCP2TT : PRM : I*4 : タイマー種別フラグ(計算部/温度）` (28) (계산부 온도 타이머); `CD    KCP2SS : PRM : I*4 : タイマー種別フラグ(計算部/スカラー）` (29) (계산부 스칼라(scalar) 타이머); `CD    KCP2KE : PRM : I*4 : タイマー種別フラグ(計算部/k-εモデル）` (30) (계산부 k-ε 모델 타이머); `CD    KCP2FF : PRM : I*4 : タイマー種別フラグ(計算部/VOF関数F）` (31) (계산부 VOF(Volume of Fluid) 함수 타이머); `CD    KCPVFL : PRM : I*4 : タイマー種別フラグ(流速・圧力関連）` (32) (유속·압력 관련 타이머 종류); `CD    KCPVGN : PRM : I*4 : ...` (33); `CD    KCPVEL : PRM : I*4 : ...` (34); `CD    KCPVPC : PRM : I*4 : ...` (35); `CD    KCPVPS : PRM : I*4 : ...` (36); `CD    KCPVMD : PRM : I*4 : ...` (37); `CD    KCPFFL : PRM : I*4 : タイマー種別フラグ(VOF関数F関連）` (38) (VOF 함수 관련 타이머 종류); `CD    KCPFEL : PRM : I*4 : ...` (39); `CD    KCPFMD : PRM : I*4 : ...` (40); `CD    KCPFNF : PRM : I*4 : ...` (41); `CD    KCP9PL : PRM : I*4 : タイマー種別フラグ(ルーチン/VF_P****）` (42) (VF_P**** 루틴 타이머); `CD    KCP9M1 : PRM : I*4 : タイマー種別フラグ(ルーチン/VF_M1BCGS）` (43) (VF_M1BCGS 루틴 타이머); `CD    KCP9NF : PRM : I*4 : タイマー種別フラグ(ルーチン/VF_FDROPF）` (44) (VF_FDROPF 루틴 타이머); `CD    CPUS(KCP0AL) : TRN : R*8 : CPU時間の合計` (45) (CPU 시간 합계); `CD    CPUW(KCP0AL) : TRN : R*8 : タイマーが起動された時間` (46) (타이머가 시작된 시각) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 3–10: KCP0AL은 22이며 나머지 타이머 종류 상수는 1..21로 정의되어 있다.
- 33–37·39–41: 해당 세부 타이머 항목의 설명은 ...로만 적혀 있다.
