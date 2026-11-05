---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/VF_ACPUTR.h
lines: 45
sha256: 5f881cca1b390d5067308bb68df04e4f7f7103ec236e192e874140103b696743
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_ACPUTR.h — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | 타이머(timer) 동작 상수 0–3과 측정 항목 상수 1–22를 PARAMETER의 한 연속 문장으로 정의한다(1–9). /VF_ACPUTR/는 CPUS(KCP0AL)·CPUW(KCP0AL)를 공유한다(10). 원문: `      PARAMETER (ICPUIN=  0, ICPUST=  1, ICPUEN=  2, ICPUOU=  3,` (1); `     &           KCP0AL= 22,` (2); `     &           KCP1PR=  1, KCP1CL=  2,` (3); `     &           KCP2FL=  3, KCP2VL=  4, KCP2TT=  5, KCP2SS=  6,` (4); `     &           KCP2KE=  7, KCP2FF=  8,` (5); `     &           KCPVFL=  9, KCPVGN= 10, KCPVEL= 11, KCPVPC= 12,` (6); `     &           KCPVPS= 13, KCPVMD= 14,` (7); `     &           KCPFFL= 15, KCPFEL= 16, KCPFMD= 17, KCPFNF= 18,` (8); `     &           KCP9PL= 19, KCP9M1= 20, KCP9NF= 21             )` (9); `      COMMON /VF_ACPUTR/ CPUS(KCP0AL), CPUW(KCP0AL)` (10) |
| 12–45 | 타이머 동작과 항목별 의미·배열 의미를 설명한다. 이 파일은 실제 시간 측정 호출이나 배열 초기화를 수행하지 않는다. 원문: `CD=== 概要 ===========================================================` (12) (개요); `CDT   VF_ACPUTR.h:CPU時間の計測関連(CPU時間等):パラメータと実数` (14) (CPU 시간 측정 관련 매개변수와 실수); `C==== 内容 ===========================================================` (16) (내용); `CD    ICPUIN : PRM : I*4 : タイマー処理フラグ(初期化)` (18) (타이머 처리 플래그(flag): 초기화); `CD    ICPUST : PRM : I*4 : タイマー処理フラグ(スタート)` (19) (타이머 처리 플래그: 시작); `CD    ICPUEN : PRM : I*4 : タイマー処理フラグ(止めて,合計をとる)` (20) (타이머 처리 플래그: 중단 후 합계); `CD    ICPUOU : PRM : I*4 : タイマー処理フラグ(CPU時間を出力する)` (21) (타이머 처리 플래그: CPU 시간 출력); `CD    KCP0AL : PRM : I*4 : タイマー種別フラグ(全体,種別フラグ数を兼ねる)` (22) (타이머 종류 플래그: 전체이며 종류 플래그 수도 겸함); `CD    KCP1PR : PRM : I*4 : タイマー種別フラグ(前処理）` (23) (타이머 종류 플래그: 전처리); `CD    KCP1CL : PRM : I*4 : タイマー種別フラグ(計算部）` (24) (타이머 종류 플래그: 계산부); `CD    KCP2FL : PRM : I*4 : タイマー種別フラグ(計算部/ファイル入出力）` (25) (타이머 종류 플래그: 계산부/파일 입출력); `CD    KCP2VL : PRM : I*4 : タイマー種別フラグ(計算部/流速・圧力）` (26) (타이머 종류 플래그: 계산부/유속·압력); `CD    KCP2TT : PRM : I*4 : タイマー種別フラグ(計算部/温度）` (27) (타이머 종류 플래그: 계산부/온도); `CD    KCP2SS : PRM : I*4 : タイマー種別フラグ(計算部/スカラー）` (28) (타이머 종류 플래그: 계산부/스칼라(scalar)); `CD    KCP2KE : PRM : I*4 : タイマー種別フラグ(計算部/k-εモデル）` (29) (타이머 종류 플래그: 계산부/k-ε 모델); `CD    KCP2FF : PRM : I*4 : タイマー種別フラグ(計算部/VOF関数F）` (30) (타이머 종류 플래그: 계산부/VOF 함수); `CD    KCPVFL : PRM : I*4 : タイマー種別フラグ(流速・圧力関連）` (31) (타이머 종류 플래그: 유속·압력 관련); `CD    KCPVGN : PRM : I*4 : ...` (32); `CD    KCPVEL : PRM : I*4 : ...` (33); `CD    KCPVPC : PRM : I*4 : ...` (34); `CD    KCPVPS : PRM : I*4 : ...` (35); `CD    KCPVMD : PRM : I*4 : ...` (36); `CD    KCPFFL : PRM : I*4 : タイマー種別フラグ(VOF関数F関連）` (37) (타이머 종류 플래그: VOF 함수 관련); `CD    KCPFEL : PRM : I*4 : ...` (38); `CD    KCPFMD : PRM : I*4 : ...` (39); `CD    KCPFNF : PRM : I*4 : ...` (40); `CD    KCP9PL : PRM : I*4 : タイマー種別フラグ(ルーチン/VF_P****）` (41) (타이머 종류 플래그: 루틴/VF_P****); `CD    KCP9M1 : PRM : I*4 : タイマー種別フラグ(ルーチン/VF_M1BCGS）` (42) (타이머 종류 플래그: 루틴/VF_M1BCGS); `CD    KCP9NF : PRM : I*4 : タイマー種別フラグ(ルーチン/VF_FDROPF）` (43) (타이머 종류 플래그: 루틴/VF_FDROPF); `CD    CPUS(KCP0AL) : TRN : R*8 : CPU時間の合計` (44) (CPU 시간 합계); `CD    CPUW(KCP0AL) : TRN : R*8 : タイマーが起動された時間` (45) (타이머가 시작된 시각) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32–36·38–40: 일부 측정 항목의 설명은 생략 기호 ...만 적혀 있다.
