---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/VF_A0PRM_mpversion.h
lines: 56
sha256: 8a6408fbffbe842da2258d9a211c1e59b769b3732feb989f5920c35d6f9ce914
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_A0PRM_mpversion.h — 판독 구간 기록

구간은 1행부터 56행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 고정형식 Fortran의 PARAMETER 문(2–17)은 6열 &로 이어지는 하나의 문장이다. 버전 자리 1·5, MAXNPI/MAXNPJ=10·MAXBUF=8·MAXLIN=100과 파일 번호·배열 한계·ZERO·ZEROG·PI를 정의한다. W-SRC 추가 구분 주석(12·15) 사이 MAXSRC=100·MAXSRCI=1000·MAXSRCJ=1000을 선언한다. 원문: `C-*- mode:fortran; -*-` (1); `      PARAMETER (IVR001=  1, IVR002=  5,` (2); `     &           MAXNPI= 10, MAXNPJ= 10, MAXBUF=  8,` (3); `     &           MFILIN= 11, MFILMT= 12, MFILRE= 13, MFILPR= 14,` (4); `     &           MFILLP= 21, MFILGR= 22, MFILRS= 23, MFILTR= 24,` (5); `     &           MAXCHR=256, MAXWDS=128, MAXG1 =  6, MAXB1 =  4,` (6); `     &           MAXNC = 10,` (7); `     &           MAXTR =10000, MAXTR1=  8,` (8); `     &           MAXPRB= 10, MAXPVC=500,` (9); `     &           MAXDRG= 10,` (10); `     &           MAXLIN=100,` (11); `c+++++  add W-SRC - start  ++++++++++++++++++++++++++++++++++++++++++++++` (12); `     &           MAXSRC= 100,` (13); `     &           MAXSRCI=1000, MAXSRCJ=1000,` (14); `c+++++  add W-SRC - end  ++++++++++++++++++++++++++++++++++++++++++++++++` (15); `     &           ZERO  =1.0D-20,ZEROG = 1.0D-6,` (16); `     &           PI    =3.141592653589794D0)` (17) |
| 19–47 | 개요·내용과 상수 의미 설명이다. 버전·병렬 프로세스 수·버퍼·각 파일 번호·입력 한계·배열 크기·농도·시계열·공극률(porosity)·기포·Dupuit-Forheimer 계수 수를 원문 주석대로 번역한다. 원문: `CD=== 概要 ===========================================================` (19) (개요); `CDT   VF_A0PRM.h:PARAMETER文を集めたファイル` (21) (PARAMETER 문을 모은 파일); `C==== 内容 ===========================================================` (23) (내용); `CD    IVR001 : PRM : I*4 : バージョンの1桁目` (25) (버전 첫째 자리); `CD    IVR002 : PRM : I*4 : バージョンの2桁目` (26) (버전 둘째 자리); `CD    MAXNPI : PRM : I*4 : x方向最大プロセス数(並列用)` (27) (병렬용 x 방향 최대 프로세스 수); `CD    MAXNPJ : PRM : I*4 : y方向最大プロセス数(並列用)` (28) (병렬용 y 방향 최대 프로세스 수); `CD    MAXBUF : PRM : I*4 : バッファ用データの本数(並列用)` (29) (병렬 버퍼 데이터 개수); `CD    MFILIN : PRM : I*4 : 入力ファイルのファイル番号` (30) (입력 파일 번호); `CD    MFILMT : PRM : I*4 : マトリクスデータファイルのファイル番号` (31) (행렬(matrix) 데이터 파일 번호); `CD    MFILRE : PRM : I*4 : リスタートファイルのファイル番号` (32) (재시작(restart) 파일 번호); `CD    MFILPR : PRM : I*4 : 時間依存型空隙率ファイルのファイル番号` (33) (시간 의존 공극률(porosity) 파일 번호); `CD    MFILLP : PRM : I*4 : リストファイルのファイル番号` (34) (목록 파일 번호); `CD    MFILGR : PRM : I*4 : 図化ファイルのファイル番号` (35) (도화 파일 번호); `CD    MFILRS : PRM : I*4 : 詳細ファイルのファイル番号` (36) (상세 파일 번호); `CD    MFILTR : PRM : I*4 : 時系列ファイルのファイル番号` (37) (시계열 파일 번호); `CD    MAXCHR : PRM : I*4 : 1行の最大文字数(入力ファイル)` (38) (입력 파일 한 행 최대 문자 수); `CD    MAXWDS : PRM : I*4 : 1行の最大単語数(入力ファイル)` (39) (입력 파일 한 행 최대 단어 수); `CD    MAXG1  : PRM : I*4 : XX,YYおよびZZの第1配列サイズ` (40) (XX·YY·ZZ 첫째 배열 크기); `CD    MAXB1  : PRM : I*4 : INDBの第1配列サイズ` (41) (INDB 첫째 배열 크기); `CD    MAXNC  : PRM : I*4 : 濃度の最大成分数` (42) (최대 농도 성분 수); `CD    MAXTR  : PRM : I*4 : 時系列ファイルへの出力対象データ最大数` (43) (시계열 파일 최대 출력 데이터 수); `CD    MAXTR1 : PRM : I*4 : ITRPRMの第1配列サイズ` (44) (ITRPRM 첫째 배열 크기); `CD    MAXPRB : PRM : I*4 : 時間依存型空隙率の空間ブロックの最大数` (45) (시간 의존 공극률 공간 블록 최대 수); `CD    MAXPVC : PRM : I*4 : 気泡の最大数(:空気圧計算用)` (46) (공기압 계산용 최대 기포 수); `CD    MAXDRG : PRM : I*4 : Dupuit-Forheimer式の係数の最大数` (47) (Dupuit-Forheimer 식 최대 계수 수) |
| 48–56 | 시작 시 실행 블록 밖인 설명부다. W-SRC 추가 구분 주석 사이 조파(wave generation) 소스 수와 x/y 방향 셀 수(49–51)를 설명한다. 묶음 입력 행 수·0 판정값·격자 간격 0 판정값·원주율 설명으로 끝난다. 원문: `c+++++  add W-SRC - start  ++++++++++++++++++++++++++++++++++++++++++++++` (48); `CD    MAXSRC : PRM : I*4 : 造波ソースの最大数` (49) (조파(wave generation) 소스 최대 수); `CD    MAXSRCI: PRM : I*4 : 造波ソースのx方向最大セル数` (50) (조파 소스의 x 방향 최대 셀 수); `CD    MAXSRCJ: PRM : I*4 : 造波ソースのy方向最大セル数` (51) (조파 소스의 y 방향 최대 셀 수); `c+++++  add W-SRC - end  ++++++++++++++++++++++++++++++++++++++++++++++++` (52); `CD    MAXLIN : PRM : I*4 : 入力データのまとめ読みの行数` (53) (입력 데이터를 묶어 읽는 행 수); `CD    ZERO   : PRM : R*8 : ゼロ判定値` (54) (0 판정값); `CD    ZEROG  : PRM : R*8 : ゼロ判定値(格子間隔判定用)` (55) (격자 간격용 0 판정값); `CD    PI     : PRM : R*8 : 円周率` (56) (원주율) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 21: 파일명은 VF_A0PRM_mpversion.h이지만 개요 주석에는 VF_A0PRM.h라고 적혀 있다.
- 2–17: 이 파일에는 MAXPRO·INMODE 매개변수가 없다. MAXSRC·MAXSRCI·MAXSRCJ는 있다.
