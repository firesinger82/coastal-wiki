---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/VF_A0PRM.h
lines: 52
sha256: 9d96de9b02166fbcb39f8215a1617f6f0ee20c61ccc83f7ec056518ef19a90f1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_A0PRM.h — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | PARAMETER의 1·4–5·7–15행은 주석을 사이에 둔 하나의 연속 문장이다. 버전·최대 크기·파일 번호·판정값·원주율을 상수로 정의한다. 3행의 이전 MAXBUF 선언은 주석 처리된 코드이다. MAXBUF 값은 원문의 곱셈식으로 보존한다. 원문: `      PARAMETER (IVR001=  0, IVR002=  2,` (1); `C----------------------------------------------------------for MG interface` (2); 주석 처리된 코드: `C    &           MAXNPI= 100, MAXNPJ= 100, MAXBUF=  8,` (3); `     &           MAXNPI= 100, MAXNPJ= 100, MAXBUF=  9*2*4,` (4); `     &           MFILEN= 10,` (5); `C----------------------------------------------------------for MG interface` (6); `     &           MFILIN= 11, MFILMT= 12, MFILRE= 13, MFILPR= 14,` (7); `     &           MFILLP= 21, MFILGR= 22, MFILRS= 23, MFILTR= 24,` (8); `     &           MFILTP= 25, MFILBT= 26,MFILBT2= 27,` (9); `     &           MAXCHR=256, MAXWDS=128, MAXG1 =  6, MAXB1 =  6,` (10); `     &           MAXBK1=  2, MAXBE1=  2, MAXNC = 10, MAXM1 =  5,` (11); `     &           MAXTR =10000, MAXTR1=  8, ` (12); `     &           MAXPRB= 10, MAXPVC=500,` (13); `     &           ZERO  =1.0D-20,ZEROG = 1.0D-6,` (14); `     &           PI    =3.141592653589794D0)` (15) |
| 17–52 | 상수의 용도·단위를 설명하는 일본어 주석이다. 공극률(porosity)의 시간 의존 자료·출력 파일 번호·배열 크기·영 판정값의 의미를 적는다. 아래 값 설명은 실행 대입문이 아니다. 원문: `CD=== 概要 ===========================================================` (17) (개요); `CDT   VF_A0PRM.h:PARAMETER文を集めたファイル` (19) (PARAMETER문을 모은 파일); `C==== 内容 ===========================================================` (21) (내용); `CD    IVR001 : PRM : I*4 : バージョンの1桁目` (23) (버전 첫째 자리); `CD    IVR002 : PRM : I*4 : バージョンの2桁目` (24) (버전 둘째 자리); `CD    MAXNPI : PRM : I*4 : x方向最大プロセス数(並列用)` (25) (병렬용 x방향 최대 프로세스 수); `CD    MAXNPJ : PRM : I*4 : y方向最大プロセス数(並列用)` (26) (병렬용 y방향 최대 프로세스 수); `CD    MAXBUF : PRM : I*4 : バッファ用データの本数(並列用)` (27) (병렬 버퍼용 데이터 묶음 수); `CD    MFILIN : PRM : I*4 : 入力ファイルのファイル番号` (28) (입력 파일 번호); `CD    MFILMT : PRM : I*4 : マトリクスデータファイルのファイル番号` (29) (매트릭스(matrix) 데이터 파일 번호); `CD    MFILRE : PRM : I*4 : リスタートファイルのファイル番号` (30) (재시작(restart) 파일 번호); `CD    MFILPR : PRM : I*4 : 時間依存型空隙率(or構造物データ)ファイルのファイル番号` (31) (시간 의존 공극률(porosity) 또는 구조물 데이터 파일 번호); `CD    MFILLP : PRM : I*4 : リストファイルのファイル番号` (32) (목록 파일 번호); `CD    MFILGR : PRM : I*4 : 図化ファイルのファイル番号` (33) (도식화 파일 번호); `CD    MFILRS : PRM : I*4 : 詳細ファイルのファイル番号` (34) (상세 파일 번호); `CD    MFILTR : PRM : I*4 : 時系列ファイルのファイル番号` (35) (시계열(time series) 파일 번호); `CD    MFILBT : PRM : I*4 : 水位変動量入力ファイルのファイル番号` (36) (수위 변동량 입력 파일 번호); `CD    MFILBT2: PRM : I*4 : 分割形式の水位変動量入力ファイルのファイル番号` (37) (분할 형식 수위 변동량 입력 파일 번호); `CD    MFILTP : PRM : I*4 : 構造物表面圧力ファイルのファイル番号` (38) (구조물 표면 압력 파일 번호); `CD    MAXCHR : PRM : I*4 : 1行の最大文字数(入力ファイル)` (39) (입력 파일 한 행의 최대 문자 수); `CD    MAXWDS : PRM : I*4 : 1行の最大単語数(入力ファイル)` (40) (입력 파일 한 행의 최대 단어 수); `CD    MAXG1  : PRM : I*4 : XX,YYおよびZZの第1配列サイズ` (41) (XX·YY·ZZ의 첫째 배열 차원 크기); `CD    MAXB1  : PRM : I*4 : INDBの第1配列サイズ` (42) (INDB의 첫째 배열 차원 크기); `CD    MAXBK1 : PRM : I*4 : INDBKの第1配列サイズ` (43) (INDBK의 첫째 배열 차원 크기); `CD    MAXBE1 : PRM : I*4 : INDBEの第1配列サイズ` (44) (INDBE의 첫째 배열 차원 크기); `CD    MAXNC  : PRM : I*4 : 濃度の最大成分数` (45) (농도 최대 성분 수); `CD    MAXM1  : PRM : I*4 : INDBMの第1配列サイズ` (46) (INDBM의 첫째 배열 차원 크기); `CD    MAXTR  : PRM : I*4 : 時系列ファイルへの出力対象データ最大数` (47) (시계열 파일에 출력할 최대 데이터 수); `CD    MAXTR1 : PRM : I*4 : ITRPRMの第1配列サイズ` (48) (ITRPRM의 첫째 배열 차원 크기); `CD    MAXPRB : PRM : I*4 : 時間依存型空隙率の空間ブロックの最大数` (49) (시간 의존 공극률(porosity)의 최대 공간 블록 수); `CD    ZERO   : PRM : R*8 : ゼロ判定値` (50) (영 판정값); `CD    ZEROG  : PRM : R*8 : ゼロ判定値(格子間隔判定用)` (51) (격자 간격용 영 판정값); `CD    PI     : PRM : R*8 : 円周率` (52) (원주율) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 3–4: 주석 처리된 MAXBUF 값은 8이다. 활성 PARAMETER의 MAXBUF 값은 9*2*4이다.
- 5·13 및 23–52: MFILEN과 MAXPVC는 PARAMETER에 있으나 이 파일의 변수별 설명 목록에는 없다.
