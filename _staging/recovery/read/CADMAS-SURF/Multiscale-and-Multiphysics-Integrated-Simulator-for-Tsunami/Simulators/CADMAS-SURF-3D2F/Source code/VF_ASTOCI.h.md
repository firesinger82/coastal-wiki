---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/VF_ASTOCI.h
lines: 46
sha256: 53caf7eddb551f096e82ab98abf9c87bbbd6e40becc691f9fb3be26309aaa73b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# VF_ASTOCI.h — 판독 구간 기록

구간은 1행부터 46행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | MAX_CADMAS=256, MAX_NIST=500, MAX_NJST=500, MAX_NKST=100을 PARAMETER로 정의한다. MIST·MJST·MKST 차원에는 각 최댓값+1을 쓴다. /VF_ASTOCI/의 변수 목록은 15–17행의 한 COMMON 문장이다. 원문: `      INTEGER MAX_CADMAS` (1); `      INTEGER MAX_NIST,MAX_NJST,MAX_NKST` (2); `      PARAMETER ( MAX_CADMAS = 256 )` (4); `      PARAMETER ( MAX_NIST = 500 )` (5); `      PARAMETER ( MAX_NJST = 500 )` (6); `      PARAMETER ( MAX_NKST = 100 )` (7); `      INTEGER IB_STOC` (9); `      INTEGER NB_CADMAS,LB_CADMAS,IB_CADMAS(MAX_CADMAS)` (10); `      INTEGER NB_SC` (11); `      INTEGER NIST,NJST,NKST,IWST,IEST,JSST,JNST` (12); `      INTEGER MIST(MAX_NIST+1),MJST(MAX_NJST+1),MKST(MAX_NKST+1)` (13); `      COMMON /VF_ASTOCI/IB_STOC,NB_CADMAS,LB_CADMAS,IB_CADMAS,NB_SC` (15); `     &                 ,NIST,NJST,NKST,IWST,IEST,JSST,JNST` (16); `     &                 ,MIST,MJST,MKST` (17) |
| 19–35 | CADMAS–STOC 결합(coupling) 통신의 순위(rank)·접속 PE 수·접속 순서·참여 여부를 설명한다. LB_CADMAS는 접속 시 1부터 NB_CADMAS이고 그 외 PE에서 0이라고 적는다. 원문: `CD=== 概要 ===========================================================` (19) (개요); `CDT   VF_ASTOCI.h:CADMAS-STOC連成関連:整数` (21) (CADMAS–STOC 결합 관련 정수); `C==== 内容 ===========================================================` (23) (내용); `CD    -- STOCとの通信に関する変数 --` (25) (STOC 통신 관련 변수); `CD    IB_STOC          : CNS : I*4 : comm_ic_mgにおけるSTOC-ICのランク` (26) (comm_ic_mg에서 STOC-IC 순위); `CD    NB_CADMAS        : CNS : I*4 : STOC-ICと接続しているCADMASのPE数` (27) (STOC-IC와 접속한 CADMAS 처리 요소(processing element, PE) 수); `CD    LB_CADMAS        : CNS : I*4 : STOCと接続しているCADMASのPEの順番付け` (28) (STOC와 접속한 CADMAS PE 순서); `CD                                   値は1～NB_CADMAS(STOCのPE及びSTOCと接続しないCADMASのPEでは0)` (29) (값은 1부터 NB_CADMAS이며 STOC PE와 비접속 CADMAS PE에서는 0); `CD                                   IB_CADMASやIB_SC参照時に使用` (30) (IB_CADMAS 또는 IB_SC 참조 시 사용); `CD    IB_CADMAS        : CNS : I*4 : STOCと接続しているCADMASのPEの、MPI_COMM_WORLDにおけるランク` (31) (STOC 접속 CADMAS PE의 MPI_COMM_WORLD 순위); `CD       (NB_CADMAS)` (32); `CD    NB_SC            : CNS : I*4 : STOC-CADMAS接続に参加しているか` (33) (STOC–CADMAS 접속 참여 여부); `CD                                      (=0:参加していない、>0:参加している）` (34) (0: 불참, 양수: 참여) |
| 36–46 | STOC와 CADMAS 격자(mesh)의 대응과 분할 수, 격자선 매핑(mapping) 배열·서동남북 접속 플래그(flag)의 주석이다. 실행 대입·통신 호출은 없다. 원문: `CD    -- STOCとCADMASのメッシュの対応関係に関する変数 --` (36) (STOC와 CADMAS 격자 대응 관련 변수); `CD    NIST             : CNS : I*4 : 自領域をSTOC側のメッシュで分割した場合のX方向分割数` (37) (자기 영역을 STOC 격자로 분할할 때 X방향 분할 수); `CD    NJST             : CNS : I*4 : 自領域をSTOC側のメッシュで分割した場合のY方向分割数` (38) (자기 영역을 STOC 격자로 분할할 때 Y방향 분할 수); `CD    NKST             : CNS : I*4 : 自領域をSTOC側のメッシュで分割した場合のZ方向分割数` (39) (자기 영역을 STOC 격자로 분할할 때 Z방향 분할 수); `CD    MIST(NIST+1)     : CNS : I*4 : STOCのI番目の格子線位置が、CADMASの格子点インデックスのいくつに相当するか(X方向)` (40) (STOC의 I번째 격자선이 대응하는 CADMAS X방향 격자점 인덱스); `CD    MJST(NJST+1)     : CNS : I*4 : STOCのJ番目の格子線位置が、CADMASの格子点インデックスのいくつに相当するか(Y方向)` (41) (STOC의 J번째 격자선이 대응하는 CADMAS Y방향 격자점 인덱스); `CD    MKST(NKST+1)     : CNS : I*4 : STOCのK番目の格子線位置が、CADMASの格子点インデックスのいくつに相当するか(Z方向)` (42) (STOC의 K번째 격자선이 대응하는 CADMAS Z방향 격자점 인덱스); `CD    IWST             : CNS : I*4 : 西側境界でSTOCと接続するか否か(=1：接続する、=0：接続しない)` (43) (서쪽 STOC 접속: 1 접속, 0 비접속); `CD    IEST             : CNS : I*4 : 東側境界でSTOCと接続するか否か(=1：接続する、=0：接続しない)` (44) (동쪽 STOC 접속: 1 접속, 0 비접속); `CD    JSST             : CNS : I*4 : 南側境界でSTOCと接続するか否か(=1：接続する、=0：接続しない)` (45) (남쪽 STOC 접속: 1 접속, 0 비접속); `CD    JNST             : CNS : I*4 : 北側境界でSTOCと接続するか否か(=1：接続する、=0：接続しない)` (46) (북쪽 STOC 접속: 1 접속, 0 비접속) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 29–30: LB_CADMAS 설명에는 IB_SC 참조가 언급되지만 이 파일의 선언과 COMMON에는 IB_SC가 없다.
