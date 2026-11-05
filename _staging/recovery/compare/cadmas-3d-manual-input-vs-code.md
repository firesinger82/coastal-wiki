# CADMAS-SURF/3D manual p.101–150 입력·출력 대조

## 1 요약

분류별 개수(5.4의 91행 기준): A 2, B 37, C 33, D 1, E 3, F 0, H 15, X 0.

2절의 대조 행은 219개이다. 2절의 판정은 일치 152행, 불일치 52행, 문서에만 15행이다. 3절의 코드 전용 처리 행은 20개이다. 4절의 노트 대조 행은 9개이다. 이 중 불일치 4행을 5절에 포함했다. 5절의 E 3행은 서로 다른 결함 후보 2개를 다룬다. 이 수는 보고서 표의 행 수이며 문서의 입력 인수 총수가 아니다.

이 보고서는 AI가 원문과 코드를 대조한 기록이다. 매뉴얼 원문과 해석을 각 행에서 구분한다. 대상은 `3D manual p.101–150`이다. p.101은 Chapter 4의 마지막 도식이다. Chapter 5는 p.102에서 시작한다. 대상의 인쇄 쪽은 413–462이다. 각 PDF 쪽 이미지 `cad-3d-manual-NNN.png`를 직접 확인한다. 모델은 실행하지 않는다. 다른 노트는 수정하지 않는다.

경로 약칭 `3D`는 `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/`이다. `3D2F`는 같은 Simulators 아래 `CADMAS-SURF-3D2F/Source code/`이다. 코드 인용에서 약칭을 생략한 파일은 모두 `3D` 파일이다. `A11111.in`은 실행 예제의 복사본이 아니다. 이 파일의 첫머리는 `A11111.in:2` `CADMAS-SURF/3Dの入力ファイル(テキスト)のフォーマット`이다. 한국어 뜻은 “CADMAS-SURF/3D 입력 파일(텍스트)의 형식”이다. 이 보고서는 매뉴얼 예제의 각 명령을 이 형식 명세와 읽기 루틴에 대조한다.

매뉴얼 판 근거는 p.135·143의 출력 예제 `CADMAS-SURF/3D-MG Ver. 1.0`이다. 코드의 날짜 표지는 `vf_a1main.f:33` `C----------------------------------------------------------2012.03 start`이다. 버전 상수는 `VF_A0PRM.h:2` `PARAMETER (IVR001=  0, IVR002=  1,`이다. 이 상수의 계속 줄은 2.14의 원문 증거에 있다. 날짜 표지 하나를 해당 불일치의 변경 이력으로 해석하지 않는다.

## 2 대조 표

표의 원문에서 공백이 들어간 숫자와 구두점은 인쇄를 보존한다. 코드 블록의 `<br>`는 실제 고정형식 연속 줄의 줄바꿈을 나타낸다. 기본값이 없는 필수 입력의 `-`는 임의 기본값을 뜻하지 않는다. 같은 행에서 여러 인수를 나열하면 각 인수의 순서를 유지한다. 각 절 제목의 괄호는 인쇄 쪽이다.

### 2.1 p.101–103 (413–415): 도식·상한

| 행 ID | 문서(위치, 원문) | 코드(파일:줄 원문) | 판정 | 이유 |
|---|---|---|---|---|
| KS3-001 | p.101 Fig.0-4-10 `INDC`; 장애물·기체 `-1`, 표면·유체 `0`; 반복 `K=2,NUMK-1`, `J=2,NUMJ-1`, `I=2,NUMI-1`, `IF (INDC(I,J,K).EQ.0) THEN` | `vf_cindc.f:39–49` `IF     (NF(I,J,K).EQ. 0) THEN` / `INDC(I,J,K)=0` / `ELSEIF (NF(I,J,K).EQ. 8) THEN` / `INDC(I,J,K)=-1` / `ELSEIF (NF(I,J,K).EQ.-1) THEN` / `INDC(I,J,K)=-1` / `ELSE` / `INDC(I,J,K)=0` | 일치 | 값과 셀 분류가 같다. 그림은 물리 경계의 안쪽 셀을 보인다. 병렬 내부 경계 범위는 KS3-301에서 다룬다. |
| KS3-002 | p.101 Fig.0-4-11 `DO 100 L=1,NUMS`, `IJK=INDS(L)`, `K=(IJK-1)/(NUMI*NUMJ)+1`, `IJK=IJK-NUMI*NUMJ*(K-1)`, `J=(IJK-1)/NUMI+1`, `I=IJK-NUMI*(J-1)` | `vf_fnfini.f:154–159` `DO 1300 L=1,NUMS` / `IJK=INDS(L)` / `K  =(IJK-1)/(NUMI*NUMJ)+1` / `IJK=IJK-NUMI*NUMJ*(K-1)` / `J  =(IJK-1)/NUMI+1` / `I  =IJK-NUMI*(J-1)` | 일치 | 1부터 시작하는 일차원 첨자와 역변환이 같다. |
| KS3-003 | p.101 `INDS is the I, K coordinates of the cell of ◎.` | `vf_fnfini.f:122` `INDS(NS)=I+NUMI*(J-1)+NUMI*NUMJ*(K-1)` | 불일치 | 설명은 J를 빠뜨린다. 같은 그림의 역변환은 I·J·K를 모두 계산한다. B. |
| KS3-004 | p.102 `dynamic allocation of arrays`; 격자·경계면 수는 메모리가 허용하는 범위 | `vf_a1main.f:412–415` `ALLOCATE(XX  (MAXG1,NUMI)    ,STAT=IERR)` / `ALLOCATE(YY  (MAXG1,NUMJ)    ,STAT=IERR)` / `ALLOCATE(ZZ  (MAXG1,NUMK)    ,STAT=IERR)` / `ALLOCATE(UU  (NUMI,NUMJ,NUMK),STAT=IERR)`; `:598` `ALLOCATE(INDB (MAXB1,NUMBX),STAT=IERR)` | 일치 | 실행 시 정한 격자 수와 경계면 수를 할당 크기로 쓴다. |
| KS3-005 | p.102 `MAXNPI ... default is 10`, `MAXNPJ ... default is 10` | `VF_A0PRM.h:4–8` `C----------------------------------------------------------2011.04 start`<br>`C    &           MAXNPI= 100, MAXNPJ= 100, MAXBUF=  8,`<br>`     &           MAXNPI= 100, MAXNPJ= 100, MAXBUF=  9*2*4,`<br>`     &           MAXLIN= 50,`<br>`C----------------------------------------------------------2011.04 end` | 불일치 | 문서는 각 10이다. 코드는 각 100이다. 해석: 문서 예제 Ver.1.0과 코드 배너 상수 0.1의 서로 다른 판에 속한 상한값 차이 A이다. 2011.04는 이 상수를 포함한 구간의 날짜 표지이다. 주석 처리한 이전 줄도 100이므로 이 표지를 10에서 100으로 바꾼 날짜로 쓰지 않는다. |
| KS3-006 | p.102 `MAXCHR ... 256`, `MAXWDS ... 128`; `VF_A0PRM.h`의 PARAMETER 변경 후 전체 재컴파일 | `VF_A0PRM.h:16` `     &           MAXCHR=256, MAXWDS=128, MAXG1 =  6, MAXB1 =  4,` | 일치 | 문자 수와 단어 수 상한이 같다. 컴파일 상수이다. |
| KS3-007 | p.103 `MAXNC ... 10`, `MAXTR ... 10000`, `MAXPRB ... 10`, `MAXPVC ... 500` | `VF_A0PRM.h:17–19` `     &           MAXNC = 10,`<br>`     &           MAXTR =10000, MAXTR1=  8,`<br>`     &           MAXPRB= 10, MAXPVC=500,` | 일치 | 농도 성분·시계열 항목·시간 의존 공극률 블록·기포 수의 상한이 같다. 모두 컴파일 상수이다. |
| KS3-008 | p.103 `MAXDR ... 10` / `Dupuit-Forheimer` | `VF_A0PRM.h:20` `     &           MAXDRG= 10,`; `:64` `CD    MAXDRG : PRM : I*4 : Dupuit-Forheimer式の係数の最大数` | 불일치 | 주석 뜻은 “Dupuit-Forheimer 식의 계수 최대 수”이다. 값은 같지만 변수명 끝 G가 문서에서 빠졌다. B. |

### 2.2 p.104–108 (416–420): 입력 예제·문법

| 행 ID | 문서(위치, 원문) | 코드(파일:줄 원문) | 판정 | 이유 |
|---|---|---|---|---|
| KS3-009 | p.104 `File name is data. In, it is a text file.` | `vf_ii1inp.f:132–134` `OPEN(MFILIN,ERR=9010,`<br>`     &       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.in',`<br>`     &       STATUS='OLD',FORM='FORMATTED'  )` | 일치 | `data`는 실행 데이터 이름의 자리표시자이다. 확장자는 소문자 `.in`이다. 인쇄의 `data. In`을 파일명 대소문자 규칙으로 읽지 않는다. |
| KS3-010 | p.104 재시작에도 입력 파일 필요; 시간 간격 초기값 무효; 구조·경계 변경 금지 | 같은 `vf_ii1inp.f:132–134`; 재시작 세부 근거는 KS3-144 | 일치 | 파일은 재시작 선택을 읽기 전에도 필요하다. 변경 금지는 사용 제약이며 코드 검사를 뜻하지 않는다. |
| KS3-011 | p.104 예제 `# TEST DATA`; `PARALLEL X 100`, `200`, `300` | `vf_zgetln.f:81` `IF (ICM.EQ.0 .AND. TEXT(I:I).EQ.'#') ICM=I`; `vf_iipara.f:30–35` `IF     (TEXT(IS(2):IE(2)).EQ.'X') THEN` / `CALL VF_ZSTOI(IPROCS(NUMNPI),TEXT(IS(3):IE(3)))`; `A11111.in:19` `PARALLEL X  [IC]` | 일치 | 세 경계는 x 방향 네 프로세스를 만든다. 주석은 읽지 않는다. |
| KS3-012 | p.104 `TIME AUTO 0.001 0.20`, `TIME LIMIT 1.0D-5 0.05`, `TIME END 999999 40.1` | `vf_iitime.f:38` `ELSEIF (TEXT(IS(2):IE(2)).EQ.'AUTO') THEN`; `:40–41` `CALL VF_ZSTOR(DTINIT,TEXT(IS(3):IE(3)))` / `CALL VF_ZSTOR(DTSAFE,TEXT(IS(4):IE(4)))`; `:47` `ELSEIF (TEXT(IS(2):IE(2)).EQ.'LIMIT') THEN`; `:55` `ELSEIF (TEXT(IS(2):IE(2)).EQ.'END') THEN`; `A11111.in:54–56` `TIME AUTO  [DTINIT] [DTSAFE]` / `TIME LIMIT [DTMIN]  [DTMAX]` / `TIME END   [NEND]   [TEND]` | 일치 | 인수 순서가 같다. 각 값은 p.109의 허용 범위 안이다. 인쇄 숫자 안의 조판 공백은 입력 공백이 아니다. |
| KS3-013 | p.104 `MATE W-LEVEL 10.0`, `DENSITY 1000.0`, `K-VISC 0.0`, `GRAVITY 9.8`, `I.C. V 0.0 0.0 0.0` | `vf_iimate.f:31,36,42,48,93,96` 문자열 `'W-LEVEL'`, `'DENSITY'`, `'K-VISC'`, `'GRAVITY'`, `'I.C.'`, `'V'`; `:98–100` `CALL VF_ZSTOR(UINI,TEXT(IS(4):IE(4)))` / `CALL VF_ZSTOR(VINI,TEXT(IS(5):IE(5)))` / `CALL VF_ZSTOR(WINI,TEXT(IS(6):IE(6)))`; `A11111.in:78–82` 동일 형식 | 일치 | 물성값과 초기 세 속도의 형식·허용 범위가 같다. 문서의 `I. C.`를 실제 두 단어로 분리하면 읽지 못한다. 문법 문자열은 `I.C.`이다. |
| KS3-014 | p.104–105 `MODEL WAVE-BC X- FUNC STREAM 5`, `DEPTH 10.0`, `HEIGHT 4.0`, `PERIOD 8.007`, `AMPL 2.0` | 키워드·인수·범위의 원문 줄은 KS3-055–068; `A11111.in:128–134`의 WAVE-BC 형식 | 일치 | STREAM 차수·수심·파고·주기·증폭 주기 수 순서가 명세와 같다. |
| KS3-015 | p.105 `MODEL DAMP X+ DEGREE 2`, `PARAM-XY 0.6`, `PARAM-Z 0.6`, `WIDTH 146.0804`, `DEPTH 10.0` | 원문 줄은 KS3-072–077; `A11111.in`의 `MODEL DAMP` 형식 | 일치 | 위치와 다섯 설정을 각각 읽는다. 예제의 폭은 이 예제의 값이다. |
| KS3-016 | p.105 `MODEL OPEN-BC X+ FUNC TYPE1`, `DEPTH 10.0`, `PERIOD 8.007` | 원문 줄은 KS3-069–070; `A11111.in`의 `MODEL OPEN-BC` 형식 | 일치 | TYPE1의 필수 수심과 주기를 지정한다. |
| KS3-017 | p.105 `COMP SCHM VP-DONOR 0.2`; `COMP MTRX M-ILUBCGSTAB 0.95`, `MAX-ITR 500`, `A-ERROR 1.0D-12`, `R-ERROR 1.0D-10` | 원문 줄은 KS3-089–095; `A11111.in`의 `COMP SCHM`, `COMP MTRX` 형식 | 일치 | 예제의 수렴 허용치는 기본값과 달라도 유효하다. |
| KS3-018 | p.105–106 `GRID X` 0.00000000…365.20100000; `GRID Y` 0.00 1.00; `GRID Z` 0.000…20.000; 각 `END` | `vf_ii1inp.f:196,200,204` 문자열 `'X'`, `'Y'`, `'Z'`; `vf_iigrid.f:76` `IF (TEXT(IS(I):IE(I)).EQ.'END') THEN`; `:84` `CALL VF_ZSTOR(XNOW,TEXT(IS(I):IE(I)))` | 일치 | 인쇄 예제는 중간 값을 `Omitted`로 생략한다. 생략 문구를 입력하면 안 된다. X 좌표 간격은 0.91300250이고 Z 좌표 간격은 0.400이다. 실행 입력 전체를 제공하는 표가 아니다. |
| KS3-019 | p.106 `B.C. D VP SLIP`, `B.C. D F FREE` | `vf_ii1inp.f:262,267` 문자열 `'B.C.'`, `'D'`; 경계 종류 원문은 KS3-125–127 | 일치 | `B. C.`는 조판 표기이다. 실제 키워드는 `B.C.`이다. 기본 경계 지정 형식과 같다. |
| KS3-020 | p.106 `FILE L/P AREA XZ 1 1`; `FILE L/P OFF` 뒤 `OBST`, `BC-IND`, `CM0`, `NF`, `F`, `V`, `P`, `VISC`, `BC` | 목록 출력 원문 줄은 KS3-148–153; `A11111.in`의 L/P 형식 | 일치 | 단면과 셀·면 번호를 지정한다. 각 OFF는 해당 출력 플래그를 끈다. |
| KS3-021 | p.106 `FILE GRP TIME 0.0 9999.9 8.007`; `FILE TRN STEP 0 999999 1`; `FILE TRN W-LEVEL ANS X-`; 관측 셀 `(1,1)`, `(81,1)`, `(321,1)`, `(400,1)` | 원문 줄은 KS3-155, KS3-165–169; `A11111.in`의 GRP·TRN 형식 | 일치 | 시간 간격·단계 간격·이론 수위·네 계산 수위의 입력 형식이 같다. 출력 예제의 일곱 항목과는 차이가 있다(KS3-235). |
| KS3-022 | p.106 `OPTION T-DOOR BUB OFF`, `OPTION T-DOOR DROP OFF` | 원문 줄은 KS3-192–193; `A11111.in`의 T-DOOR 형식 | 일치 | 두 시간문 처리를 각각 끈다. |
| KS3-023 | p.107 빈 줄·선행 공백·`#` 이후 무시; 한 개 이상 공백으로 단어 분리; 탭을 판별하지 않음 | `vf_zgetln.f:80–89` `IF (ION.EQ.0 .AND. TEXT(I:I).NE.' ') ION=I` / `IF (ICM.EQ.0 .AND. TEXT(I:I).EQ.'#') ICM=I` / `IF (ION.EQ.0  ) GOTO 9000` / `IF (ION.EQ.ICM) GOTO 9000` / `TEXT=TEXT(ION:ICM-1)` / `CALL VF_ZSTOWS(IS,IE,MWD,NWD,TEXT(1:ICM-ION))` | 일치 | 주석과 공백을 제거한 범위만 단어 분리기에 준다. 문자·단어 상한은 KS3-006과 같다. |
| KS3-024 | p.107 `Characters after the last word valid in grammar` 무시 | 예: `vf_iitime.f:39` `IF (NWD.LT.4) CALL VF_A2ERR('VF_IITIME','SYNTAX ERROR.')`; 반례 `vf_iigrid.f:76–77` `IF (TEXT(IS(I):IE(I)).EQ.'END') THEN` / `IF (I.NE.NWD) CALL VF_A2ERR('VF_IIGRID','SYNTAX ERROR.')` | 불일치 | 일반 명령은 최소 단어 수만 검사하지만 GRID의 END 뒤 단어는 오류이다. 무조건 무시한다는 설명에는 예외가 필요하다. C. |
| KS3-025 | p.107 `There is no rule of order of input data.` | `vf_ii1inp.f:109–114` `C     * LEVEL=<0:格子数を読み込む(格子数を決定する)` / `C     * LEVEL= 1:格子座標と障害物データを読み込む(境界面数を決定する)` / `C     * LEVEL>=2:その他のデータを読み込む`; `vf_iigrid.f:46` `IF (NL.NE.0) CALL VF_A2ERR('VF_IIGRID','SECOND TIMES.')` | 일치 | 주석 뜻은 격자 수, 격자·장애물, 기타 자료를 세 번에 나누어 읽는다는 것이다. 해석: 서로 다른 명령의 배치는 자유이다. 같은 명령의 중복과 GRID 내부의 END 구조는 별도 제약이다. |
| KS3-026 | p.107 Fig.0-5-1 `do not include virtual cells`; NI·NJ·NK는 입력 좌표 수; 셀 1…N−1, 격자면 1…N | `vf_iigrid.f:47,81` `NL  =1` / `NL=NL+1`; `vf_iiobst.f`와 `vf_iiboun.f`의 입력 첨자 +1 변환은 KS3-103·122 | 일치 | 내부 배열에는 가상 셀을 포함한다. 입력 번호와 내부 첨자 사이의 +1을 구분한다. 그림은 xz·yz 단면과 스칼라 중심·속도면을 보인다. |
| KS3-027 | p.108 `PARALLEL X [IC]`, `PARALLEL Y [JC]`; I*4; 기본값 `-`; `2=<IC=<NI-2`, `2=<JC=<NJ-2`; 입력 수+1이 프로세스 수 | `vf_iipara.f:30,38` `IF     (TEXT(IS(2):IE(2)).EQ.'X') THEN` / `ELSEIF (TEXT(IS(2):IE(2)).EQ.'Y') THEN`; `:35,43` `CALL VF_ZSTOI(IPROCS(NUMNPI),TEXT(IS(3):IE(3)))` / `CALL VF_ZSTOI(JPROCS(NUMNPJ),TEXT(IS(3):IE(3)))`; `vf_cpara.f:20–21` `NUMNPI=NUMNPI+1` / `NUMNPJ=NUMNPJ+1` | 일치 | 방향별 정수 경계와 수를 읽는다. 간격의 추가 검사는 KS3-302이다. |
| KS3-028 | p.108 `EQUATION K-EPS {ISW}`, `TEMPERATURE {ISW}`; C*(*); `NOCALC`, `CALC`; 기본은 계산하지 않음 | `vf_iiequa.f:30–35` `IF     (TEXT(IS(2):IE(2)).EQ.'K-EPS') THEN` / `IF     (TEXT(IS(3):IE(3)).EQ.'NOCALC') THEN` / `LEQK=0` / `ELSEIF (TEXT(IS(3):IE(3)).EQ.'CALC'  ) THEN` / `LEQK=1`; `:41–46` TEMPERATURE도 같은 분기; `vf_a2dflt.f:139–140` `LEQK =0` / `LEQT =0` | 일치 | 두 방정식의 선택 문자열과 기본 비활성이 같다. |
| KS3-029 | p.108 `EQUATION CONCENTRATION [NC]`; I*4; 기본 0; `0=<NC=<MAXNC`; `When NS = 0` | `vf_iiequa.f:52–56` `ELSEIF (TEXT(IS(2):IE(2)).EQ.'CONCENTRATION') THEN` / `CALL VF_ZSTOI(LEQC,TEXT(IS(3):IE(3)))` / `IF (LEQC.LT.0    ) CALL VF_A2ERR('VF_IIEQUA','INVALID VALUE.')` / `IF (LEQC.GT.MAXNC) CALL VF_A2ERR('VF_IIEQUA','INVALID VALUE.')`; `vf_a2dflt.f:141` `LEQC =0` | 불일치 | 값·형·허용 범위는 같다. 설명의 NS는 이 표의 NC와 달라 변수명 오기이다. B. |

### 2.3 p.109–111 (421–423): 시간·물성

| 행 ID | 문서(위치, 원문) | 코드(파일:줄 원문) | 판정 | 이유 |
|---|---|---|---|---|
| KS3-030 | p.109 `TIME CONST [DTCNST]`; R*8, s, `1.0D-3`, `DTCNST>=ZERO` | `vf_iitime.f:31–35` `IF (TEXT(IS(2):IE(2)).EQ.'CONST') THEN` / `CALL VF_ZSTOR(DTCNST,TEXT(IS(3):IE(3)))` / `IF (DTCNST.LT.ZERO) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')` / `IDTTYP=0`; `vf_a2dflt.f:230` `DTCNST=1.0D-3` | 일치 | 상수 시간 간격의 형·단위·기본값·조건이 같다. |
| KS3-031 | p.109 `TIME AUTO [DTINIT] [DTSAFE]`; R*8; s·무차원; `1.0D-6`, `1.0D-1`; 각 `>=ZERO`; 기본 AUTO | `vf_iitime.f:38–44` `ELSEIF (TEXT(IS(2):IE(2)).EQ.'AUTO') THEN` / `CALL VF_ZSTOR(DTINIT,TEXT(IS(3):IE(3)))` / `CALL VF_ZSTOR(DTSAFE,TEXT(IS(4):IE(4)))` / `IF (DTINIT.LT.ZERO) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')` / `IF (DTSAFE.LT.ZERO) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')` / `IDTTYP=1`; `vf_a2dflt.f:223,231,234` `IDTTYP=1` / `DTINIT=1.0D-6` / `DTSAFE=1.0D-1` | 일치 | 두 기본값과 제한이 같다. |
| KS3-032 | p.109 `TIME LIMIT [DTMIN] [DTMAX]`; R*8, s; `ZERO`, `1.0D0/ZERO`; `ZERO=<DTMIN=<DTMAX` | `vf_iitime.f:47,49–52` `ELSEIF (TEXT(IS(2):IE(2)).EQ.'LIMIT') THEN` / `CALL VF_ZSTOR(DTMIN,TEXT(IS(3):IE(3)))` / `CALL VF_ZSTOR(DTMAX,TEXT(IS(4):IE(4)))` / `IF (DTMIN.LT.ZERO ) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')` / `IF (DTMIN.GT.DTMAX) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')`; `vf_a2dflt.f:232–233` `DTMIN =ZERO` / `DTMAX =1.0D0/ZERO` | 일치 | ZERO는 `VF_A0PRM.h:22`의 `ZERO  =1.0D-20`이다. 상한 기본값은 10²⁰ s이다. |
| KS3-033 | p.109 `TIME END [NEND] [TEND]`; I*4·R*8; 단계·s; 기본 0·0.0D0; 각 비음수 | `vf_iitime.f:55,57–60` `ELSEIF (TEXT(IS(2):IE(2)).EQ.'END') THEN` / `CALL VF_ZSTOI(NEND,TEXT(IS(3):IE(3)))` / `CALL VF_ZSTOR(TEND,TEXT(IS(4):IE(4)))` / `IF (NEND.LT.0    ) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')` / `IF (TEND.LT.0.0D0) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')`; `vf_a2dflt.f:221,227` `NEND  =0` / `TEND  =0.0D0` | 일치 | 종료 조건 두 인수를 해당 형으로 읽는다. |
| KS3-034 | p.109 `AUTO does not consider limitation by wave velocity`; 재시작 초기값 무효 | `vf_cdtcal.f:130,133–134` `DT=V/MAX(FL1,FL2,FL3,FL4,FL5,FL6,V/DT)` / `V=0.5D0/(1.0D0/(DX*DX)+1.0D0/(DY*DY)+1.0D0/(DZ*DZ))` / `DT=V/MAX(WK01(I,J,K),V/DT)`; `:145–147` `W=DTNOW` / `IF (NNOW.EQ.0) W=DTINIT` / `DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)`; `vf_ir1inp.f:184` `READ(IREFIL,END=1000,ERR=9020) NNOW,TNOW,DTNOW` | 일치 | 이류·확산 제약을 사용한다. 재시작 파일의 단계와 시간 간격을 복원한다. 초기 단계에서만 DTINIT를 사용한다. |
| KS3-035 | p.109–110 `MATE W-LEVEL [WVLVL]`; R*8, m, 기본 0.0D0, 제한 없음 | `vf_iimate.f:31,33` `IF     (TEXT(IS(2):IE(2)).EQ.'W-LEVEL') THEN` / `CALL VF_ZSTOR(WVLVL,TEXT(IS(3):IE(3)))`; `vf_a2dflt.f:164` `WVLVL =0.0D0` | 일치 | 실수 초기 수위이다. |
| KS3-036 | p.110 `MATE DENSITY [RHO0]`; R*8, kg/m3, 1.0D+3, `RHO0>=ZERO` | `vf_iimate.f:36,38–39` `ELSEIF (TEXT(IS(2):IE(2)).EQ.'DENSITY') THEN` / `CALL VF_ZSTOR(RHO0,TEXT(IS(3):IE(3)))` / `IF (RHO0.LT.ZERO) CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')`; `vf_a2dflt.f:161` `RHO0  =1.0D+3` | 일치 | 값·형·조건이 같다. |
| KS3-037 | p.110 `MATE K-VISC [ANU0]`; R*8, m2/s, 1.0D-6, `ANU0>=0.0` | `vf_iimate.f:42,44–45` `ELSEIF (TEXT(IS(2):IE(2)).EQ.'K-VISC') THEN` / `CALL VF_ZSTOR(ANU0,TEXT(IS(3):IE(3)))` / `IF (ANU0.LT.0.0D0) CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')`; `vf_a2dflt.f:162` `ANU0  =1.0D-6` | 일치 | 動粘性係数는 동점성계수이다. |
| KS3-038 | p.110 `MATE GRAVITY [GRZ0]`; R*8, m/s2, 9.8; 제한 `GZR0>=0.0` | `vf_iimate.f:48,50–51` `ELSEIF (TEXT(IS(2):IE(2)).EQ.'GRAVITY') THEN` / `CALL VF_ZSTOR(GRZ0,TEXT(IS(3):IE(3)))` / `IF (GRZ0.LT.0.0D0) CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')`; `vf_a2dflt.f:163` `GRZ0  =9.8D0` | 불일치 | 제한의 GZR0는 GRZ0의 문자 순서 오기이다. 값과 비음수 조건은 같다. B. |
| KS3-039 | p.110 `MATE I.C. V [UINI] [VINI] [WINI]`; 각각 R*8, m/s, 0.0, 제한 없음 | `vf_iimate.f:93,96,98–100` `'I.C.'` / `'V'` / `CALL VF_ZSTOR(UINI,TEXT(IS(4):IE(4)))` / `CALL VF_ZSTOR(VINI,TEXT(IS(5):IE(5)))` / `CALL VF_ZSTOR(WINI,TEXT(IS(6):IE(6)))`; `vf_a2dflt.f:158–160` `UINI  =0.0D0` / `VINI  =0.0D0` / `WINI  =0.0D0` | 일치 | 세 방향별 초기 속도의 인수 순서와 기본값이 같다. |
| KS3-040 | p.110 `MATE I.C. KE [AKINI] [AEINI]`; R*8, m2/s2·m2/s3, ZERO, 각 `>=ZERO` | `vf_iimate.f:102,104–109` `ELSEIF (TEXT(IS(3):IE(3)).EQ.'KE') THEN` / `CALL VF_ZSTOR(AKINIK,TEXT(IS(4):IE(4)))` / `CALL VF_ZSTOR(AKINIE,TEXT(IS(5):IE(5)))` / `IF (AKINIK.LT.ZERO)`<br>`     &                 CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')`<br>`          IF (AKINIE.LT.ZERO)`<br>`     &                 CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')`; `vf_a2dflt.f:167–168` `AKINIK=ZERO` / `AKINIE=ZERO` | 일치 | 문서의 자리표시자와 내부 이름은 다르지만 에너지·소산의 순서가 같다. |
| KS3-041 | p.110 `MATE S-HEAT [CP]`; R*8, J/K/kg, 4.2D+3, `CP>=ZERO` | `vf_iimate.f:54,56–57` `'S-HEAT'` / `CALL VF_ZSTOR(TCP0,TEXT(IS(3):IE(3)))` / `IF (TCP0.LT.ZERO) CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')`; `vf_a2dflt.f:180` `TCP0 =4.2D+3` | 일치 | CP는 코드 TCP0에 대응한다. |
| KS3-042 | p.110 `MATE T-COND [TC]`; R*8, W/m/K, 5.7D-1, `TC>=ZERO` | `vf_iimate.f:60,62–63` `'T-COND'` / `CALL VF_ZSTOR(TCN0,TEXT(IS(3):IE(3)))` / `IF (TCN0.LT.ZERO) CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')`; `vf_a2dflt.f:181` `TCN0 =5.7D-1` | 일치 | TC는 코드 TCN0에 대응한다. |
| KS3-043 | p.110–111 `MATE T-DENS [T0] [DRDT]`; R*8, K·kg/m3/K, 2.73D+2·1.5D-1, 제한 없음 | `vf_iimate.f:66,68–69` `'T-DENS'` / `CALL VF_ZSTOR(TDT0,TEXT(IS(3):IE(3)))` / `CALL VF_ZSTOR(TDR0,TEXT(IS(4):IE(4)))`; `vf_a2dflt.f:182–183` `TDT0 =2.73D+2` / `TDR0 =1.5D-1` | 일치 | 기준 온도와 밀도 기울기를 이 순서로 읽는다. |
| KS3-044 | p.110–111 `MATE I.C. T [TINI]`; R*8, K, 2.73D+2, 제한 없음 | `vf_iimate.f:111,113` `'T'` / `CALL VF_ZSTOR(TINI,TEXT(IS(4):IE(4)))`; `vf_a2dflt.f:179` `TINI =2.73D+2` | 일치 | 초기 온도이다. |
| KS3-045 | p.111 `MATE DIFFUS [LC] [DF]`; DF R*8, m2/s, 기본 `-`, `DF>=ZERO` | `vf_iimate.f:72,74–79` `'DIFFUS'` / `CALL VF_ZSTOI(LC,TEXT(IS(3):IE(3)))` / `CALL VF_ZSTOR(SC,TEXT(IS(4):IE(4)))` / `IF (LC.LE.0 .OR. LC.GT.LEQC)`<br>`     &                  CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')`<br>`        IF (SC.LT.ZERO) CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')` / `CDF0(LC)=SC`; `vf_a2dflt.f:185` `CALL VF_ZSETR1(CDF0,0.0D0,MAXNC)` | 불일치 | 입력 검사는 같다. 문서는 생략 시 확산계수 0.0D0을 적지 않는다. C. |
| KS3-046 | p.111 LC `R*8`, `1=<LS=<NS` | `vf_iimate.f:74` `CALL VF_ZSTOI(LC,TEXT(IS(3):IE(3)))`; `:76–77` `IF (LC.LE.0 .OR. LC.GT.LEQC)`<br>`     &                  CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')` | 불일치 | LC는 정수이다. 제한의 LS·NS는 LC·NC에 맞추어야 한다. `A11111.in:113`에도 같은 오기가 있다. B. |
| KS3-047 | p.110–111 `MATE C-DENS [LC] [C0] [DRDC]`; 두 실수 R*8, 무차원·kg/m3, 각 0.0D0 | `vf_iimate.f:82,84–90` `'C-DENS'` / `CALL VF_ZSTOI(LC,TEXT(IS(3):IE(3)))` / `CALL VF_ZSTOR(SC,TEXT(IS(4):IE(4)))` / `CALL VF_ZSTOR(SR,TEXT(IS(5):IE(5)))` / `CDC0(LC)=SC` / `CDR0(LC)=SR`; `vf_a2dflt.f:186–187` `CALL VF_ZSETR1(CDC0,0.0D0,MAXNC)` / `CALL VF_ZSETR1(CDR0,0.0D0,MAXNC)` | 일치 | C0·DRDC의 기본값과 인수 순서가 같다. LC의 오기는 KS3-046에 분리했다. |
| KS3-048 | p.110–111 `MATE I.C. C [LC] [CINI]`; R*8, 0.0D0, 제한 없음, 단위 `[K]` | `vf_iimate.f:115,117–121` `'C'` / `CALL VF_ZSTOI(LC,TEXT(IS(4):IE(4)))` / `CALL VF_ZSTOR(SC,TEXT(IS(5):IE(5)))` / `CINI(LC)=SC`; `vf_a2dflt.f:184` `CALL VF_ZSETR1(CINI,0.0D0,MAXNC)` | 불일치 | 값과 형식은 같다. CINI는 농도이므로 K가 아니다. 같은 문서의 C0·BC는 무차원이다. B. |
| KS3-049 | p.111 번호 없는 식 \(\mathrm{RHO}=\mathrm{RHO0}-\mathrm{DRDT}*(T-\mathrm{T0})-\mathrm{DRDC}*(C-\mathrm{C0})\) | `vf_vgene.f:318–327` `DR=0.0D0` / `DR=DR-TDR0*(T-TDT0)` / `DO 300 LC=1,LEQC` / `C=ZZ(6,K)*(ZZ(2,K)*CC(I,J,K1,LC)+ZZ(2,K1)*CC(I,J,K,LC))` / `DR=DR-CDR0(LC)*(C-CDC0(LC))` / `QW(I,J,K)=QW(I,J,K)-GV*GRZ0*DR/RHO0` | 불일치 | 한 성분일 때 부호가 같다. 코드는 농도 성분 전체를 합산하지만 식은 성분 합을 적지 않는다. C. |
| KS3-050 | p.111 `gravitational acceleration ... shall be 9.8` | `vf_a2dflt.f:163` `GRZ0  =9.8D0`; `vf_csetup.f:103` `IF (D.GE.ZERO) WUS=GRZ0*H*T*T/D/D` | 문서에만 | 파형 모델의 사용 제약이다. 사용자에게 9.8을 요구하는 문장을 임의 중력 금지 검사로 바꾸지 않는다. H. |

### 2.4 p.111–115 (423–427): 모델 입력

| 행 ID | 문서(위치, 원문) | 코드(파일:줄 원문) | 판정 | 이유 |
|---|---|---|---|---|
| KS3-055 | p.111–112 `MODEL WAVE-BC {DIR}`; C*(*), `X-`, `X+`, `Y-`, `Y+`; 수심·파고·주기 기본 `-` | `vf_iimdl.f:34–43` `'WAVE-BC'` / `'X-'` JD=1 / `'X+'` JD=2 / `'Y-'` JD=3 / `'Y+'` JD=4; `vf_a2dflt.f:149,188` `CALL VF_ZSETI2(IBCTYP, 0,4,4)` / `CALL VF_ZSETR2(BCTYP,0.0D0,11,4)` | 일치 | 경계 네 위치와 선택 문자열이 같다. 미지정 모델은 비활성이다. |
| KS3-056 | p.111–112 `FUNC STREAM [N]`; I*4, `1=<N=<22` | `vf_iimdl.f:51–57` `'FUNC'` / `'STREAM'` / `CALL VF_ZSTOI(IVAL,TEXT(IS(6):IE(6)))` / `IF (IVAL.LT.1 .OR. IVAL.GT.22)`<br>`     &                    CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')` / `IBCTYP(2,JD)=IVAL` | 일치 | 정수 차수 제한이 같다. |
| KS3-057 | p.112 `STK-CND`, `STOKES`, `CNOIDAL`, `MATRIX`, `MATRIX2 (only BC)`; p.113 기본 STK-CND | `vf_iimdl.f:58–69` `'STK-CND'` → `IBCTYP(2,JD)= 0`; `'STOKES'` → −2; `'CNOIDAL'` → −1; `'MATRIX'` → −3; `'MATRIX2'` → −4; `vf_a2dflt.f:149` `CALL VF_ZSETI2(IBCTYP, 0,4,4)` | 일치 | 0은 설정 시 Stokes·cnoidal 자동 선택이다. 매트릭스 두 종류를 구분한다. `STK - CND`는 조판 공백이다. |
| KS3-058 | p.111–112 `DEPTH [D]`; R*8, m, `D>=ZERO` | `vf_iimdl.f:73–77` `'DEPTH'` / `CALL VF_ZSTOR(VAL,TEXT(IS(5):IE(5)))` / `IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')` / `BCTYP(1,JD)=VAL` | 일치 | 수심을 첫 슬롯에 저장한다. |
| KS3-059 | p.111–112 `HEIGHT [H]`; R*8, m, `H>=ZERO`; 설명 `Wave depth` | `vf_iimdl.f:78–82` `'HEIGHT'` / `CALL VF_ZSTOR(VAL,TEXT(IS(5):IE(5)))` / `IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')` / `BCTYP(2,JD)=VAL`; `vf_csetup.f:65` `H =BCTYP (2,JD)` | 불일치 | 수심 DEPTH와 별도인 파고 HEIGHT이다. 같은 문서 p.113도 wave height라고 쓴다. 설명의 depth는 오기이다. B. |
| KS3-060 | p.111–112 `PERIOD [T]`; R*8, s, `T>=ZERO` | `vf_iimdl.f:83–87` `'PERIOD'` / `CALL VF_ZSTOR(VAL,TEXT(IS(5):IE(5)))` / `IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')` / `BCTYP(3,JD)=VAL` | 일치 | 주기와 검사값이 같다. |
| KS3-061 | p.111–113 `AMPL [A]`; R*8, 기본 0.0; `A<ZERO`이면 처음부터 정해진 파 | `vf_iimdl.f:88–91` `'AMPL'` / `CALL VF_ZSTOR(VAL,TEXT(IS(5):IE(5)))` / `BCTYP(8,JD)=VAL`; `vf_a2dflt.f:188` `CALL VF_ZSETR2(BCTYP,0.0D0,11,4)` | 일치 | 음수를 허용한다. 증폭 적용 근거는 아래 보충 원문에 둔다. |
| KS3-062 | p.111–113 `AREA [LC1] [LC2]`; I*4; X 경계는 y 셀 1…NJ−1, Y 경계는 x 셀 1…NI−1; 기본 전체 | `vf_iimdl.f:92–106` `'AREA'` / `CALL VF_ZSTOI(L1,TEXT(IS(5):IE(5)))` / `CALL VF_ZSTOI(L2,TEXT(IS(6):IE(6)))` / `L1=L1+1` / `L2=L2+1`; `:99–103` `IF (L1.LT.2 .OR. L2.GT.NUMJ0-1 .OR. L1.GT.L2)`<br>`     &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')`<br>`          ELSE`<br>`            IF (L1.LT.2 .OR. L2.GT.NUMI0-1 .OR. L1.GT.L2)`<br>`     &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')` | 일치 | 가상 셀 한 칸을 더한 내부 번호로 검사한다. 기본 0은 setup에서 전체 범위로 바꾼다. |
| KS3-063 | p.111–113 `ANGLE [ANG] [X0] [Y0]`; R*8, DEG·m·m; ANG 기본 0; 반시계; \(\lvert\mathrm{ANG}\rvert\mathrel{=<}\mathrm{ZERO}\)일 때 기준점 미사용; 매트릭스에는 ANG 불가 | `vf_iimdl.f:107–111` `'ANGLE'` / `CALL VF_ZSTOR(BCTYP( 9,JD),TEXT(IS(5):IE(5)))` / `CALL VF_ZSTOR(BCTYP(10,JD),TEXT(IS(6):IE(6)))` / `CALL VF_ZSTOR(BCTYP(11,JD),TEXT(IS(7):IE(7)))`; `vf_csetup.f:97–99` `IF (N.EQ.-3 .OR. N.EQ.-4) THEN` / `IF (ABS(BCTYP(9,JD)).GT.ZERO)`<br>`     &        CALL VF_A2ERR('VF_CSETUP','(WAVE-BC ANGLE) CAN NOT USE.')`; 기본 `vf_a2dflt.f:188` 전 슬롯 0 | 일치 | 각도와 두 기준점 인수를 읽는다. 0 각도의 매트릭스는 금지하지 않는다. |
| KS3-064 | p.111–112 `MODEL WAVE-SRC {DIR2} [LC]`; `X`, `Y`; LC I*4, 셀 1…NI−1 또는 NJ−1 | `vf_iimdl.f:117–132` `'WAVE-SRC'` / `'X'` / `CALL VF_ZSTOI(L1,TEXT(IS(4):IE(4)))` / `L1=L1+1` / `IF (L1.LT.2 .OR. L1.GT.NUMI0-1)`<br>`     &                  CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')` / `ISCTYP(1)=L1`; Y는 `:126–132` / `IF (L1.LT.2 .OR. L1.GT.NUMJ0-1)`<br>`     &                  CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')` / `ISCTYP(1)=-L1` | 일치 | 부호로 X·Y 방향을 구분한다. |
| KS3-065 | p.111–112 WAVE-SRC `FUNC STREAM [N]`, `STK-CND`, `STOKES`, `CNOIDAL`, `MATRIX`; MATRIX2 제외 | `vf_iimdl.f:133–149` `'FUNC'` / `'STREAM'` / `CALL VF_ZSTOI(IVAL,TEXT(IS(5):IE(5)))` / `IF (IVAL.LT.1 .OR. IVAL.GT.22)`<br>`     &                    CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')`; `:141,143,145,147` `'STK-CND'`, `'STOKES'`, `'CNOIDAL'`, `'MATRIX'`; `vf_a2dflt.f:152` `CALL VF_ZSETI1(ISCTYP, 0,2)` | 일치 | 기본과 차수 및 선택지가 같다. |
| KS3-066 | p.111–112 WAVE-SRC `DEPTH [D]`, `HEIGHT [H]`, `PERIOD [T]`, `AMPL [A]`; D·H·T R*8 각 `>=ZERO`; A R*8 기본 0 | `vf_iimdl.f:153–171` `'DEPTH'` / `SCTYP(1)=VAL`; `'HEIGHT'` / `SCTYP(2)=VAL`; `'PERIOD'` / `SCTYP(3)=VAL`; `'AMPL'` / `SCTYP(8)=VAL`; `:156,161,166` `IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')`; `vf_a2dflt.f:206` `CALL VF_ZSETR1(SCTYP,0.0D0,8)` | 일치 | 경계 입력보다 인수 위치가 한 칸 앞이다. 단위는 D·H가 m이고 T가 s이다. |
| KS3-067 | p.113 파형 함수에는 수심·파고·주기 필수; MATRIX의 수위/유량에는 D·T, 속도에는 T, 수위에는 T 필수 | `vf_csetup.f:67–95`의 MTBTYP=1·2·3 및 MTBTYP2=1·2·3 분기; 예 `:68–71` `IF (D.LT.ZERO)`<br>`     &        CALL VF_A2ERR('VF_CSETUP','(WAVE-BC DEPTH) NOT FOUND.')`<br>`            IF (T.LT.ZERO)`<br>`     &        CALL VF_A2ERR('VF_CSETUP','(WAVE-BC PERIOD) NOT FOUND.')` | 일치 | 수위/유량에서만 D를 요구한다. 일반 파형은 H도 요구한다. |
| KS3-068 | p.113 MATRIX 수위만 사용하는 자료는 조파 소스에서 사용 불가 | `vf_csetup.f:267` `ELSEIF (N.EQ.-3 .AND. MTBTYP.EQ.3) THEN` | 일치 | 소스의 수위 전용 매트릭스는 setup 오류 경로이다. 아래 보충 원문에 오류 호출까지 제시한다. |
| KS3-069 | p.113 `MODEL OPEN-BC {DIR} FUNC {TYPE}`; DIR 네 방향; TYPE1 | `vf_iimdl.f:177–198` `'OPEN-BC'`; `:179,181,183,185` `'X-'`, `'X+'`, `'Y-'`, `'Y+'`; `:196–198` `'FUNC'` / `'TYPE1'` / `IBCTYP(2,JD)= 0` | 일치 | 네 경계에서 소진폭 방사 경계를 선택한다. |
| KS3-070 | p.113 OPEN-BC `DEPTH [D]`, `PERIOD [T]`; R*8, m·s; 각 `>=ZERO`; TYPE1이면 필수 | `vf_iimdl.f:202–211` `'DEPTH'` / `BCTYP(1,JD)=VAL`; `'PERIOD'` / `BCTYP(3,JD)=VAL`; `:205,210` `IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')` | 일치 | 필수 두 값을 같은 슬롯에 저장한다. |
| KS3-072 | p.114 `MODEL DAMP {DIR}`; `X-`, `X+`, `Y-`, `Y+` | `vf_iimdl.f:217–226` `'DAMP'` / `'X-'` / `'X+'` / `'Y-'` / `'Y+'`; `vf_a2dflt.f:150` `CALL VF_ZSETI1(IDAMP ,-1,4)` | 일치 | -1은 미사용이다. |
| KS3-073 | p.114 `DEGREE [N]`; I*4, 무차원, 기본 `-`, `N>=0` | `vf_iimdl.f:232–236` `'DEGREE'` / `CALL VF_ZSTOI(IVAL,TEXT(IS(5):IE(5)))` / `IF (IVAL.LT.0) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')` / `IDAMP(JD)=IVAL` | 일치 | 차수 0을 허용한다. |
| KS3-074 | p.114 `PARAM-XY [PXY]`, `PARAM-Z [PZ]`; R*8, 무차원, 각 0.6, 각 `>=ZERO` | `vf_iimdl.f:237–246` `'PARAM-XY'` / `DAMP(1,JD)=VAL`; `'PARAM-Z'` / `DAMP(2,JD)=VAL`; `:240,245` `IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')`; `vf_a2dflt.f:189–202` 각 방향 `DAMP(1,JD)=0.6D0`, `DAMP(2,JD)=0.6D0` | 일치 | 수평·수직 계수 기본값이 같다. |
| KS3-075 | p.114 `WIDTH [W]`, `DEPTH [D]`; R*8, m, 기본 `-`, 각 `>=ZERO` | `vf_iimdl.f:247–256` `'WIDTH'` / `DAMP(3,JD)=VAL`; `'DEPTH'` / `DAMP(4,JD)=VAL`; `:250,255` `IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')` | 일치 | 폭과 수심을 별도로 읽는다. |
| KS3-076 | p.114 `degree, width and water depth are essential` | `vf_iimdl.f:230` `IF (IDAMP(JD).EQ.-1) IDAMP(JD)=-2`; 기본 폭·수심 `vf_a2dflt.f:191–192` `DAMP(3,1)=0.0D0` / `DAMP(4,1)=0.0D0` | 일치 | 다른 DAMP 입력만 주면 차수 미정 -2를 남긴다. setup의 필수 검사와 함께 읽는다. |
| KS3-077 | p.114 권고 차수 2; 폭 두 파장일 때 기본 감쇠계수 권고 | 입력 검사는 KS3-073–075 | 문서에만 | 권고값과 적용 권고 조건이다. 구현과의 일치 여부로 성능을 검증하지 않는다. H. |
| KS3-078 | p.114–115 `MODEL K-EPS LIM [AKMIN] [AEMIN]`; R*8, m2/s2·m2/s3; ZERO; 각 `>=ZERO` | `vf_iimdl.f:262,264,266–271` `'K-EPS'` / `'LIM'` / `CALL VF_ZSTOR(AKMINK,TEXT(IS(4):IE(4)))` / `CALL VF_ZSTOR(AKMINE,TEXT(IS(5):IE(5)))` / `IF (AKMINK.LT.ZERO)`<br>`     &                  CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')`<br>`          IF (AKMINE.LT.ZERO)`<br>`     &                  CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')`; `vf_a2dflt.f:165–166` `AKMINK=ZERO` / `AKMINE=ZERO` | 일치 | 두 하한이 같다. |
| KS3-079 | p.114–115 `PARAMETER [CMU] [SGK] [SGE] [C1] [C2] [C3]`; R*8, 무차원; 0.09·1.0·1.3·1.44·1.92·0.0; 앞 셋 `>=ZERO`, 뒤 셋 `>=0.0` | `vf_iimdl.f:272–285` `'PARAMETER'`; `:274–279` `CALL VF_ZSTOR(AKCMU,TEXT(IS(4):IE(4)))` / `CALL VF_ZSTOR(AKSGK,TEXT(IS(5):IE(5)))` / `CALL VF_ZSTOR(AKSGE,TEXT(IS(6):IE(6)))` / `CALL VF_ZSTOR(AKC1 ,TEXT(IS(7):IE(7)))` / `CALL VF_ZSTOR(AKC2 ,TEXT(IS(8):IE(8)))` / `CALL VF_ZSTOR(AKC3 ,TEXT(IS(9):IE(9)))`; `vf_a2dflt.f:169–174` `AKCMU =0.09D0` / `AKSGK =1.0D0` / `AKSGE =1.3D0` / `AKC1  =1.44D0` / `AKC2  =1.92D0` / `AKC3  =0.0D0` | 일치 | 계수 여섯 개의 순서·기본값·비음수 검사가 같다. |
| KS3-080 | p.114–115 `LOG-LAW [K0] [A0]`; R*8, 무차원; 0.4·5.5; 각 `>=ZERO` | `vf_iimdl.f:286,288–291` `'LOG-LAW'` / `CALL VF_ZSTOR(AKK0,TEXT(IS(4):IE(4)))` / `CALL VF_ZSTOR(AKA0,TEXT(IS(5):IE(5)))` / `IF (AKK0.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')` / `IF (AKA0.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')`; `vf_a2dflt.f:175–176` `AKK0  =0.4D0` / `AKA0  =5.5D0` | 일치 | 대수법칙 상수 둘이 같다. |
| KS3-081 | p.114–115 `PRANDTL [PR]`; R*8, 무차원, 1.0D0, `PR>=ZERO` | `vf_iimdl.f:292,294–295` `'PRANDTL'` / `CALL VF_ZSTOR(AKPR,TEXT(IS(4):IE(4)))` / `IF (AKPR.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')`; `vf_a2dflt.f:177` `AKPR  =1.0D0` | 일치 | 난류 Prandtl 수이다. |
| KS3-082 | p.114–115 `SCHMIDT [LC] [SM]`; SM R*8, 무차원, 1.0D0, `SM>=ZERO` | `vf_iimdl.f:296,298–303` `'SCHMIDT'` / `CALL VF_ZSTOI(LC,TEXT(IS(4):IE(4)))` / `CALL VF_ZSTOR(SC,TEXT(IS(5):IE(5)))` / `IF (LC.LE.0 .OR. LC.GT.LEQC)`<br>`     &                    CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')` / `IF (SC.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')` / `AKSM(LC)=SC`; `vf_a2dflt.f:178` `CALL VF_ZSETR1(AKSM,1.0D0,MAXNC)` | 일치 | 성분별 Schmidt 수의 기본값과 검사가 같다. |
| KS3-083 | p.115 LC `R*8`, `1=<LS=<NS` | `vf_iimdl.f:298` `CALL VF_ZSTOI(LC,TEXT(IS(4):IE(4)))` | 불일치 | LC 정수와 표의 R*8이 다르다. LS·NS도 잘못된 이름이다. B. |

### 2.5 p.115–119 (427–431): 수치·격자·장애물·공극률

| 행 ID | 문서(위치, 원문) | 코드(파일:줄 원문) | 판정 | 이유 |
|---|---|---|---|---|
| KS3-089 | p.115 `COMP SCHM VP-DONOR [SCMVP]`; R*8, 1.0, `0.0=<SCMVP=<1.0` | `vf_iicomp.f:35,37–39` `'VP-DONOR'` / `CALL VF_ZSTOR(SCMVP,TEXT(IS(4):IE(4)))` / `IF (SCMVP.LT.0.0D0 .OR. SCMVP.GT.1.0D0)`<br>`     &                 CALL VF_A2ERR('VF_IICOMP','INVALID VALUE.')`; `vf_a2dflt.f:60` `SCMVP =1.0D0` | 일치 | 유속·압력 이류 차분 계수이다. |
| KS3-090 | p.115 `COMP SCHM FF-DN-AC`, `COMP SCHM FF-SLOPE` | `vf_iicomp.f:42–46` `ELSEIF (TEXT(IS(3):IE(3)).EQ.'FF-DN-AC') THEN` / `ISCMFF=0` / `ELSEIF (TEXT(IS(3):IE(3)).EQ.'FF-SLOPE') THEN` / `ISCMFF=1`; `vf_a2dflt.f:41` `ISCMFF=0` | 일치 | 두 VOF 이류법을 선택한다. 기본은 FF-DN-AC이다. |
| KS3-091 | p.115–116 `KE-DONOR [SCMK]`, `T-DONOR [SCMT]`, `C-DONOR [LC] [SCMC]`; 실수 각 1.0, 각 0…1 | `vf_iicomp.f:48,55,62` `'KE-DONOR'`, `'T-DONOR'`, `'C-DONOR'`; `:50,57,65` `CALL VF_ZSTOR(SCMK,TEXT(IS(4):IE(4)))` / `CALL VF_ZSTOR(SCMT,TEXT(IS(4):IE(4)))` / `CALL VF_ZSTOR(SC,TEXT(IS(5):IE(5)))`; `vf_a2dflt.f:61–63` `SCMK  =1.0D0` / `SCMT  =1.0D0` / `CALL VF_ZSETR1(SCMC,1.0D0,MAXNC)` | 일치 | 각 변수의 R*8 계수와 기본 DONOR가 같다. 각 범위 검사는 vf_iicomp.f:51–52·58–59·68–69에 있다. |
| KS3-092 | p.116 LC `R*8`, `1=<LS=<NS` | `vf_iicomp.f:64,66–67` `CALL VF_ZSTOI(LC,TEXT(IS(4):IE(4)))` / `IF (LC.LE.0 .OR. LC.GT.LEQC)`<br>`     &                 CALL VF_A2ERR('VF_IICOMP','INVALID VALUE.')` | 불일치 | 성분 번호는 I*4이다. 제한의 이름도 잘못되었다. B. |
| KS3-093 | p.115–116 `COMP MTRX ILUBCGSTAB`, `M-ILUBCGSTAB [CGPARA]`; 기본 M-ILUBCGSTAB; CGPARA R*8, 0.95, 0…1 | `vf_iicomp.f:78,81–89` `'MTRX'` / `'ILUBCGSTAB'` / `ICGTYP=0` / `'M-ILUBCGSTAB'` / `CALL VF_ZSTOR(CGPARA,TEXT(IS(4):IE(4)))` / `IF (CGPARA.LT.0.0D0 .OR. CGPARA.GT.1.0D0)`<br>`     &                 CALL VF_A2ERR('VF_IICOMP','INVALID VALUE.')` / `ICGTYP=1`; `vf_a2dflt.f:37,48` `ICGTYP=1` / `CGPARA=0.95D0` | 일치 | 두 전처리법 선택이다. |
| KS3-094 | p.115 `MAX-ITR [ICGMAX]`; p.116 `ICGMAT`, I*4, 500, `ICGMAX>=0` | `vf_iicomp.f:91,93–94` `'MAX-ITR'` / `CALL VF_ZSTOI(ICGMAX,TEXT(IS(4):IE(4)))` / `IF (ICGMAX.LT.0) CALL VF_A2ERR('VF_IICOMP','INVALID VALUE.')`; `vf_a2dflt.f:38` `ICGMAX=500` | 불일치 | 표의 ICGMAT는 ICGMAX의 오기이다. B. |
| KS3-095 | p.115–116 `A-ERROR [CGEPSA]`, `R-ERROR [CGEPSR]`; R*8, 무차원, 1.0D-15·1.0D-12, 각 비음수 | `vf_iicomp.f:96,98–100` `'A-ERROR'` / `CALL VF_ZSTOR(CGEPSA,TEXT(IS(4):IE(4)))` / `IF (CGEPSA.LT.0.0D0)`<br>`     &                 CALL VF_A2ERR('VF_IICOMP','INVALID VALUE.')`; `:102,104–106` `'R-ERROR'` / `CALL VF_ZSTOR(CGEPSR,TEXT(IS(4):IE(4)))` / `IF (CGEPSR.LT.0.0D0)`<br>`     &                 CALL VF_A2ERR('VF_IICOMP','INVALID VALUE.')`; `vf_a2dflt.f:49–50` `CGEPSA=1.0D-15` / `CGEPSR=1.0D-12` | 일치 | 절대·상대 수렴 기준을 구분한다. |
| KS3-099 | p.116–117 `GRID {COORD} [S(1)] ... [S(N)] END`; X·Y·Z, S R*8 m, `S(i)-S(i-1)>=ZEROG`, N I*4 `N>=2`; 한 줄 수 임의; N은 입력값 개수 | `vf_iigrid.f:76,81,84,86–87,121` `'END'` / `NL=NL+1` / `CALL VF_ZSTOR(XNOW,TEXT(IS(I):IE(I)))` / `IF (XNOW-XOLD.LT.ZEROG)`<br>`     &                  CALL VF_A2ERR('VF_IIGRID','INVALID VALUE.')` / `IF (NL.LT.3) CALL VF_A2ERR('VF_IIGRID','2 > NUMBER OF GRID.')`; `VF_A0PRM.h:22` `     &           ZERO  =1.0D-20,ZEROG = 1.0D-6,` | 일치 | NL은 1에서 시작하므로 N=NL−1이다. 최소 두 좌표와 10⁻⁶ m 간격을 요구한다. |
| KS3-100 | p.117 `Input must be 1 degree` | `vf_iigrid.f:46` `IF (NL.NE.0) CALL VF_A2ERR('VF_IIGRID','SECOND TIMES.')` | 불일치 | 각도 1도가 아니라 각 방향 GRID를 한 번만 입력한다는 뜻이다. B. |
| KS3-101 | p.117 `OBST FILE {FILE}`; C*(*), 기본 `-`; 기존 OBST 행을 외부 파일로 분리 | `vf_ii1inp.f:213–220` `'OBST'` / `'FILE'` / `OPEN(MFILOB,ERR=9020,FILE=TEXT(IS(3):IE(3)),`<br>`     &                 STATUS='OLD',FORM='FORMATTED'  )`; `:147` `IINFIL=MFILOB`; 기본 `:99–100` `INTEGER MODEOBS` / `DATA MODEOBS /0/` | 일치 | 명시한 파일에서 OBST 명령을 읽는다. |
| KS3-103 | p.117 `OBST [IC1] [JC1] [KC1] [IC2] [JC2] [KC2]`; 각 I*4, 기본 `-`; 각 시작≤끝, 셀 1…NI−1·NJ−1·NK−1 | `vf_iiobst.f:35–44` `CALL VF_ZSTOI(I1,TEXT(IS(2):IE(2)))`부터 K2까지 정수 변환; `IF (I1.LT.1 .OR. I2.GT.NUMI0-2 .OR. I1.GT.I2 .OR.`<br>`     &    J1.LT.1 .OR. J2.GT.NUMJ0-2 .OR. J1.GT.J2 .OR.`<br>`     &    K1.LT.1 .OR. K2.GT.NUMK -2 .OR. K1.GT.K2     )`<br>`     &                CALL VF_A2ERR('VF_IIOBST','INVALID VALUE.')`; `:45–50` `DO 220 K=K1+1,K2+1` / `DO 210 J=J1+1,J2+1` / `DO 200 I=I1+1,I2+1` / `NF(I-IP,J-JP,K)=-1` | 일치 | 내부 좌표 수는 입력 좌표 수보다 1 크다. 따라서 NUMI0−2는 문서 NI−1이다. |
| KS3-104 | p.118 `POROUS FILE {FILE}`; 외부 POROUS 행; C*(*), 기본 `-` | `vf_ii1inp.f:237–244` `'POROUS'` / `'FILE'` / `OPEN(MFILPS,ERR=9030,FILE=TEXT(IS(3):IE(3)),`<br>`     &                 STATUS='OLD',FORM='FORMATTED'  )`; `:159` `IINFIL=MFILPS`; 기본 `:102` `DATA MODEPRS /0/` | 일치 | 외부 파일 명령과 전환이 구현되어 있다. |
| KS3-105 | p.118–119 `POROUS LIM [PL]`; R*8, 무차원, 기본 인쇄 `1 0 D - 4`; `ZERO=<PL=<1.0` | `vf_iiporo.f:52,54–56` `'LIM'` / `CALL VF_ZSTOR(PLOWER,TEXT(IS(3):IE(3)))` / `IF (PLOWER.LT.ZERO ) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')` / `IF (PLOWER.GT.1.0D0) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')`; `vf_a2dflt.f:59` `PLOWER=1.0D-4` | 불일치 | 기본값 인쇄에서 1 뒤 소수점이 없다. `1.0D-4`로 고친다. B. |
| KS3-106 | p.118–119 `POROUS V [IC1] [JC1] [KC1] [IC2] [JC2] [KC2] [V1] [V2]`; 셀 여섯 개 I*4, V1·V2 R*8 | `vf_iiporo.f:59,61–69` `'V'`; I1·J1·K1·I2·J2·K2는 `VF_ZSTOI`; `CALL VF_ZSTOR(V1,TEXT(IS( 9):IE( 9)))` / `CALL VF_ZSTOR(V2,TEXT(IS(10):IE(10)))` / `VAL=MAX(V2+(1.0D0-V2)*V1,PLOWER)` | 일치 | 셀 공극률을 입력한다. 여섯 셀 제한은 KS3-103과 같다. |
| KS3-107 | p.118–119 `POROUS X [IG1] [JC1] [KC1] [IG2] [JC2] [KC2] [V1] [V2]`; IG는 1…NI, 나머지 셀은 1…N−1 | `vf_iiporo.f:92,103–107` `'X'`; `IF (I1.LT.1  .OR. I2.GT.NUMI0-1 .OR.`<br>`     &      J1.LT.1  .OR. J2.GT.NUMJ0-2 .OR.`<br>`     &      K1.LT.1  .OR. K2.GT.NUMK -2 .OR.`<br>`     &      I1.GT.I2 .OR. J1.GT.J2 .OR. K1.GT.K2)`<br>`     &                    CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')`; `:117` `IF (INDX(I-IP,J-JP,K).NE.-1) GGX(I-IP,J-JP,K)=VAL` | 일치 | x 면의 투과율이다. |
| KS3-108 | p.118–119 `POROUS Y [IC1] [JG1] [KC1] [IC2] [JG2] [KC2] [V1] [V2]`; JG는 1…NJ | `vf_iiporo.f:125,136–140` `'Y'`; `IF (I1.LT.1  .OR. I2.GT.NUMI0-2 .OR.`<br>`     &      J1.LT.1  .OR. J2.GT.NUMJ0-1 .OR.`<br>`     &      K1.LT.1  .OR. K2.GT.NUMK -2 .OR.`<br>`     &      I1.GT.I2 .OR. J1.GT.J2 .OR. K1.GT.K2)`<br>`     &                    CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')`; `:150` `IF (INDY(I-IP,J-JP,K).NE.-1) GGY(I-IP,J-JP,K)=VAL` | 일치 | y 면의 투과율이다. |
| KS3-109 | p.118–119 `POROUS Z [IC1] [JC1] [KG1] [IC2] [JC2] [KG2] [V1] [V2]`; KG는 1…NK | `vf_iiporo.f:158,169–173` `'Z'`; `IF (I1.LT.1  .OR. I2.GT.NUMI0-2 .OR.`<br>`     &      J1.LT.1  .OR. J2.GT.NUMJ0-2 .OR.`<br>`     &      K1.LT.1  .OR. K2.GT.NUMK -1 .OR.`<br>`     &      I1.GT.I2 .OR. J1.GT.J2 .OR. K1.GT.K2)`<br>`     &                    CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')`; `:183` `IF (INDZ(I-IP,J-JP,K).NE.-1) GGZ(I-IP,J-JP,K)=VAL` | 일치 | z 면의 투과율이다. |
| KS3-110 | p.118–119 `POROUS CM`와 `POROUS CD`; 여섯 셀 뒤 실수 계수; R*8 무차원, 기본 `-`, 각각 비음수 | `vf_iiporo.f:191,199,205,211` `'CM'` / `CALL VF_ZSTOR(CM,TEXT(IS(9):IE(9)))` / `IF (CM.LT.0.0D0) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')` / `IF (NF(I-IP,J-JP,K).NE.-1) CM0(I-IP,J-JP,K)=CM`; `:219,227,233,239` `'CD'` / `CALL VF_ZSTOR(CD,TEXT(IS(9):IE(9)))` / `IF (CD.LT.0.0D0) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')` / `IF (NF(I-IP,J-JP,K).NE.-1) CD0(I-IP,J-JP,K)=CD` | 일치 | 같은 셀 상자에 관성·저항 계수를 저장한다. DRAG-DF 사용 시 CD의 뜻은 KS3-204로 바뀐다. |
| KS3-111 | p.119 번호 없는 식 \(\mathrm{PL}\mathrel{=<}\text{Water proportion}=\mathrm{V2}+(1.0-\mathrm{V2})*\mathrm{V1}\mathrel{=<}1.0\); PL 미만이면 PL로 대체 | `vf_iiporo.f:69` `VAL=MAX(V2+(1.0D0-V2)*V1,PLOWER)`; `:102,135,168`도 동일 | 일치 | 합성식의 부호·계수가 같다. 하한 처리를 포함한다. |
| KS3-112 | p.119 V1·V2 각각 `0.0=<V1=<1.0`, `0.0=<V2=<1.0` | `vf_iiporo.f:75–78` `IF (V1 .LT.0.0D0) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')` / `IF (V1 .GT.1.0D0) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')` / `IF (VAL.LT.ZERO ) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')` / `IF (VAL.GT.1.0D0) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')` | 불일치 | V2 대신 합성·하한 적용 후 VAL만 검사한다. V1=1이면 V2가 범위 밖이어도 VAL=1이다. 문서가 적지 않은 허용 동작 C로 분류한다. 입력 의무를 검사로 보장하지 않는다는 사실을 기록한다. |
| KS3-113 | p.119 장애물 이외에 설정; 장애물 표면에는 설정 가능 | `vf_iiporo.f:84` `IF (NF(I-IP,J-JP,K).NE.-1) GGV(I-IP,J-JP,K)=VAL`; `:117,150,183` 면 인덱스가 −1이 아닐 때 GGX·GGY·GGZ를 대입 | 일치 | 셀 내부의 장애물과 장애물 경계면을 구분한다. |

### 2.6 p.119–122 (431–434): 경계 입력

| 행 ID | 문서(위치, 원문) | 코드(파일:줄 원문) | 판정 | 이유 |
|---|---|---|---|---|
| KS3-122 | p.119–120 `B.C. D {BC}`; X·Y·Z별 여섯 첨자와 BC; IG·JG·KG는 1…N, IC·JC·KC는 1…N−1; 모두 I*4, 기본 `-` | `vf_ii1inp.f:262,267,281,287,293` `'B.C.'`, `'D'`, `'X'`, `'Y'`, `'Z'`; `vf_iiboun.f:98–102` `IF (I1.LT.1  .OR. I2.GT.NUMI0-1 .OR.`<br>`     &      J1.LT.1  .OR. J2.GT.NUMJ0-2 .OR.`<br>`     &      K1.LT.1  .OR. K2.GT.NUMK -2 .OR.`<br>`     &      I1.GT.I2 .OR. J1.GT.J2 .OR. K1.GT.K2)`<br>`     &                 CALL VF_A2ERR('VF_IIBOUN','INVALID VALUE.')`; `:112–116,126–130`는 각각 Y·Z 면만 N까지 허용; `:134–139` 각 첨자 +1 | 일치 | D는 전체 면을 지정한다. X·Y·Z의 법선 방향만 격자 번호이다. |
| KS3-123 | p.120 KC1 제한의 독립 `1=`와 `1=<KC1=<KC2=<NK-1` | `vf_iiboun.f:100` `     &      K1.LT.1  .OR. K2.GT.NUMK -2 .OR.`; 전체 조건은 KS3-122 | 불일치 | 독립 `1=`는 식의 일부가 아니다. 뒤의 완전한 범위식으로 정리한다. B. |
| KS3-125 | p.120–121 VP `SLIP`, `NON-S`, `FIX-V [BU] [BV] [BW]`, `FREE`, `LOG`, `LOG-KS [KS]`; BU·BV·BW R*8 m/s; KS R*8 m `>=ZERO`; 모두 기본 `-` | `vf_iiboun.f:146,149,156,163,172,179,186` `'VP'`, `'SLIP'`, `'NON-S'`, `'FIX-V'`, `'FREE'`, `'LOG'`, `'LOG-KS'`; `:167–169` `CALL VF_ZSTOR(BU,TEXT(IS(IP-2):IE(IP-2)))` / `CALL VF_ZSTOR(BV,TEXT(IS(IP-1):IE(IP-1)))` / `CALL VF_ZSTOR(BW,TEXT(IS(IP  ):IE(IP  )))`; `:194–195` `CALL VF_ZSTOR(BT,TEXT(IS(IP):IE(IP)))` / `IF (BT.LT.ZERO) CALL VF_A2ERR('VF_IIBOUN','INVALID VALUE.')` | 일치 | 종류 코드 1·2·3·4·6·8로 구분한다. 고정 속도 세 성분과 거칠기 인수를 해당 순서로 읽는다. |
| KS3-126 | p.121 `Slip: F FIX [BF]`, `Slip: F FREE` | `vf_iiboun.f:220,223,227,230–232` `'F'` / `'FIX'` / `CALL VF_ZSTOR(BF,TEXT(IS(IP):IE(IP)))` / `'FREE'` / `IB=2` / `BF=0.0D0` | 불일치 | 두 설명의 Slip은 VOF 고정·자유 경계의 설명이 아니다. B. |
| KS3-127 | p.122 BF R*8 무차원, 제한 `-` | `vf_iiboun.f:228–229` `IF (BF.LT.0.0D0 .OR. BF.GT.1.0D0)`<br>`     &                   CALL VF_A2ERR('VF_IIBOUN','INVALID VALUE.')` | 불일치 | FIX BF에는 0…1 제약이 있다. C. |
| KS3-128 | p.121–122 K·E 각각 `FIX-A`, `FIX + A`, `FREE-A`, `FREE + A`; BK·BE R*8, m²/s²·m²/s³, 각 `>=ZERO` | `vf_iiboun.f:253,256,262,268,271` `'K'`, `'FIX-A'`, `'FIX+A'`, `'FREE-A'`, `'FREE+A'`; `:296,299,305,311,314` E도 동일; `:260–261,266–267,303–304,309–310` `CALL VF_ZSTOR(BT,TEXT(IS(IP):IE(IP)))` / `IF (BT.LT.ZERO) CALL VF_A2ERR('VF_IIBOUN','INVALID VALUE.')` | 일치 | 조판 공백을 제외한 실제 문자열은 FIX+A·FREE+A이다. 부호와 값 고정·영 기울기를 구분한다. |
| KS3-129 | p.121–122 T의 `FIX±A [BT]`, `FREE±A`, `FLUX±A [BTQ]`, `TRAN±A [BTH] [BT0]`; R*8, K·W/m²·W/m²/K·K; BTH `>=ZERO` | `vf_iiboun.f:339,342,349,356,361,366,373,380,388` `'T'`, `'FIX-A'`, `'FIX+A'`, `'FREE-A'`, `'FREE+A'`, `'FLUX-A'`, `'FLUX+A'`, `'TRAN-A'`, `'TRAN+A'`; `:385–387` `CALL VF_ZSTOR(BH ,TEXT(IS(IP  ):IE(IP  )))` / `CALL VF_ZSTOR(BT0,TEXT(IS(IP+1):IE(IP+1)))` / `IF (BH.LT.ZERO) CALL VF_A2ERR('VF_IIBOUN','INVALID VALUE.')` | 일치 | 고정 온도·열유속·열전달의 인수 수를 구분한다. |
| KS3-130 | p.121–122 `C [LC]`의 FIX±A·FREE±A·FLUX±A·TRAN±A; BC·BC0 무차원, BCQ·BCH m/s; R*8; BCH `>=ZERO` | `vf_iiboun.f:420,428,435,442,447,452,459,466,474` `'C'`, `'FIX-A'`, `'FIX+A'`, `'FREE-A'`, `'FREE+A'`, `'FLUX-A'`, `'FLUX+A'`, `'TRAN-A'`, `'TRAN+A'`; `:471–473` `CALL VF_ZSTOR(BH ,TEXT(IS(IP  ):IE(IP  )))` / `CALL VF_ZSTOR(BT0,TEXT(IS(IP+1):IE(IP+1)))` / `IF (BH.LT.ZERO) CALL VF_A2ERR('VF_IIBOUN','INVALID VALUE.')` | 일치 | 성분 번호 다음에 종류를 읽는다. 값·유속 차원의 플럭스·전달계수를 구분한다. |
| KS3-131 | p.122 LC `R*8`, `1=<LS=<NS` | `vf_iiboun.f:423–425` `CALL VF_ZSTOI(LC,TEXT(IS(IP):IE(IP)))` / `IF (LC.LE.0 .OR. LC.GT.LEQC)`<br>`     &                  CALL VF_A2ERR('VF_IIBOUN','INVALID VALUE.')` | 불일치 | 성분 번호는 정수이다. LS·NS는 LC·NC로 고친다. B. |
| KS3-132 | p.122 지정 상자 내부의 경계면에 설정 | `vf_iiboun.f:204–211` `L=INDXYZ(I-IPP,J-JPP,K)` / `IF (L.GE.1) THEN` / `INDB(3,L)=IB` / `BCU (  L)=BU` / `BCV (  L)=BV` / `BCW (  L)=BW` / `BCP (  L)=BP` / `BCVI(  L)=BT` | 일치 | 면 목록에 있는 위치에만 적용한다. |
| KS3-133 | p.122 조파·개방 경계 우선; LOG·LOG-KS이면 난류량도 같은 경계 | `vf_iiboun.f:206` `INDB(3,L)=IB`; 이후 `vf_csetup.f`의 특수 경계 설정과 난류 경계 보정 | 일치 | 입력 직후 경계와 setup 후 경계를 구분한다. 보충 원문에서 최종 대입을 인용한다. |
| KS3-134 | p.122 `[+ A]`는 이류 시 경계 스칼라 유입; `[-A]`는 유입하지 않음 | `vf_iiboun.f:259,265,269,272` `IB=-1` / `IB= 1` / `IB=-2` / `IB= 2` | 일치 | 이류 플래그를 부호로 저장한다. 확산 경계 종류는 절댓값으로 구분한다. 이류 루틴 원문은 보충 표에 둔다. |

### 2.7 p.122–129 (434–441): 파일 제어

출력 간격의 공통 표기에서 `ISTR IEND ISTEP`은 I*4 단계이고 `TSTR TEND TSTEP`은 R*8 초이다. 문서의 각 제한은 \(\mathrm{ISTR}\mathrel{=<}\mathrm{IEND}\), \(\mathrm{ISTEP}>0\), \(\mathrm{TSTR}\mathrel{=<}\mathrm{TEND}\), \(\mathrm{TSTEP}>0.0\)이다. 각 행의 STEP·TIME은 이 인수 세 개를 이 순서로 가진다. 기본 `-`는 출력 예약을 지정하지 않았다는 뜻이다.

| 행 ID | 문서(위치, 원문) | 코드(파일:줄 원문) | 판정 | 이유 |
|---|---|---|---|---|
| KS3-141 | p.122 `FILE OBS {FLAG}`; C*(*), OFF, `OFF または ON` | `vf_ii1inp.f:104` `DATA MODEORS /0/`; `:366,369–372` `'OBS'` / `'ON'` / `MODEORS=1` / `'OFF'` / `MODEORS=0` | 일치 | 일본어 뜻은 “OFF 또는 ON”이다. 기본은 담당 영역 지형 파일을 사용하지 않음이다. |
| KS3-142 | p.122–123 ON이면 최초에 obs 저장, 재시작 때 obs 읽기; OBST·POROUS 헤더 무시; 외부 파일일 때만 읽기 감소 | `vf_ii1inp.f:145–163`에서 LEVEL별 MFILOB·MFILPS 전환; `:214–220,238–244` 외부 FILE 열기; `:341–350` AUTO의 ars 단계 읽기 | 일치 | 외부 파일 분리와 재시작 정보 조기 판독을 함께 써야 한다. 정확한 생략 조건은 보충 원문에 둔다. |
| KS3-143 | p.123 읽기 횟수는 외부 분리 전 3, 분리 후 1, `FILE RES AUTO`이면 0 | `vf_ii1inp.f:109–111` LEVEL 0·1·2의 세 번 판독; `:145` `IF (LEVEL.EQ.1.AND.MODEOBS.EQ.1 ) THEN`; `:157` `ELSEIF (LEVEL.GE.2 .AND.MODEPRS.EQ.1 ) THEN` | 일치 | 문장의 범위는 지형자료 파일의 헤더 읽기이다. 일반 `.in` 파일 전체를 읽지 않는다는 뜻이 아니다. FILE OBS ON과 유효한 재시작을 전제로 한다. |
| KS3-144 | p.123 `FILE RES [ISTEP]`, `FILE RES AUTO`; I*4 단계, `ISTEP>=0`; ars 읽기 실패 시 최초 계산; 시간 간격 초기값 무효; 구조·경계 변경 금지·검사 안 함 | `vf_ii1inp.f:336,341,343–350` `'RES'` / `'AUTO'` / `IRETYP=-1` / `OPEN(MFILAR,ERR=310,`<br>`     &               FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.ars',`<br>`     &               STATUS='OLD',FORM='FORMATTED'  )` / `READ(MFILAR,*,ERR=310) II,TT` / `IRETYP=II`; `:359–361` `CALL VF_ZSTOI(IRETYP,TEXT(IS(3):IE(3)))` / `IF (IRETYP.LT.0)`<br>`     &          CALL VF_A2ERR('VF_II1INP','INVALID VALUE.')`; `vf_a2dflt.f:99` `IRETYP=-1` | 일치 | -1이면 최초 계산이다. 저장 배열을 읽어 덮으므로 구조·경계 변경 금지는 사용자가 지켜야 한다. AUTO의 종료 표지는 KS3-304이다. |
| KS3-145 | p.123·126 AUTO와 ELAPSE 조합 권고 | `vf_ii1inp.f:341` `'AUTO'`; `vf_iifile.f:231` `'ELAPSE'` | 문서에만 | 재시작 운용 권고이다. H. |
| KS3-148 | p.123–124 `FILE L/P STEP`, `FILE L/P TIME`; 기본 미출력 | `vf_iifile.f:33,36,45` `'L/P'`, `'STEP'`, `'TIME'`; `:38–43` `CALL VF_ZSTOI(ILPTRN(1),TEXT(IS(4):IE(4)))` / `CALL VF_ZSTOI(ILPTRN(2),TEXT(IS(5):IE(5)))` / `CALL VF_ZSTOI(ILPTRN(3),TEXT(IS(6):IE(6)))` / `ILPTYP=1` / `IF (ILPTRN(1).GT.ILPTRN(2) .OR. ILPTRN(3).LE.0)`<br>`     &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')`; `:47–52` RLPTRN에 VF_ZSTOR 후 동일 시간 검사; `vf_a2dflt.f:89` `ILPTYP=0` | 일치 | 시작·끝·간격과 자료형 및 비활성 기본값이 같다. |
| KS3-149 | p.123–124 `FILE L/P AREA {SECT} [IJKC] [IJKG]`; SECT C*(*) 기본 XY; XY·XZ·YZ·YX·ZX·ZY; IJKC·IJKG I*4 기본 0, 범위 0…N−1·0…N | `vf_iifile.f:54,56,58,60,62,64,66` `'AREA'`, `'XY'`, `'XZ'`, `'YZ'`, `'YX'`, `'ZX'`, `'ZY'`; `:71–74` `CALL VF_ZSTOI(ILPARA(2),TEXT(IS(5):IE(5)))` / `CALL VF_ZSTOI(ILPARA(3),TEXT(IS(6):IE(6)))` / `ILPARA(2)=ILPARA(2)+1` / `ILPARA(3)=ILPARA(3)+1`; `vf_a2dflt.f:91` `CALL VF_ZSETI1(ILPARA,1,3)` | 일치 | 내부 1이 입력 0의 전체 단면 선택이다. 단면별 상한 검사도 가상 셀 한 칸을 고려한다. |
| KS3-150 | p.124–125 `FILE L/P ON {PHYS}`, `OFF {PHYS}`; 기본 모든 물리량 미출력 | `vf_iifile.f:92–96` `ELSEIF (TEXT(IS(3):IE(3)).EQ.'ON' .OR.`<br>`     &          TEXT(IS(3):IE(3)).EQ.'OFF'    ) THEN` / `IF (TEXT(IS(3):IE(3)).EQ.'ON') ISW=1`; `vf_a2dflt.f:92` `CALL VF_ZSETI1(ILPON ,0,19)`; `VF_AFILEI.h:4` `     &                   ILPTYP,ILPTRN(3),ILPARA(3),ILPON(21),` | 불일치 | 21개 출력 플래그 중 19개만 명시적으로 초기화한다. 공기압용 두 플래그의 초기화 누락은 E 후보이다. 반대 근거와 강도는 5절에 적는다. |
| KS3-151 | p.124 PHYS `OBST`, `BC-IND`, `CM 0`, `CD 0`, `POROUS`, `LAMBDA`, `NF`, `F`, `V`, `P`, `K`, `E`, `VISC-T`, `VISC`, `T`, `T-COND`, `C`, `DIFFUS`, `BC`, `IPVC`, `PPPVC` | `vf_iifile.f:97–138` 각 `.EQ.` 문자열은 `'OBST'`, `'BC-IND'`, `'CM0'`, `'CD0'`, `'POROUS'`, `'LAMBDA'`, `'NF'`, `'F'`, `'V'`, `'P'`, `'VISC'`, `'BC'`, `'T'`, `'T-COND'`, `'C'`, `'DIFFUS'`, `'K'`, `'E'`, `'VISC-T'`, `'IPVC'`, `'PPPVC'`; 각 `ILPON(index)=ISW` | 일치 | CM0·CD0의 조판 공백을 제외하면 21개 문자열과 출력 대상이 같다. `VISC`는 ANU이고 동점성계수 차원 m²/s이다. |
| KS3-152 | p.124 `LAMBDA: GLV, GLX, GLZ` | `vf_a1main.f:236` `DOUBLE PRECISION, DIMENSION(:,:,:), ALLOCATABLE :: GLV,GLX,GLY,GLZ`; LAMBDA 출력은 보충 원문 | 불일치 | 설명에서 GLY 하나가 빠졌다. C. |
| KS3-153 | p.125 IJKC=0이면 \(0\mathrel{=<}\mathrm{IJKC}\mathrel{=<}N\), IJKG=0이면 \(0\mathrel{=<}\mathrm{IJKG}\mathrel{=<}N\) 출력 | `vf_ol3dr.f:33–35` `IF (ILPARA(2).EQ.1) THEN` / `M1=1` / `M2=0`; `:52,61` `IF (M2.EQ.0) M2=NUMK` / `WRITE(ILPFIL,9510) 'K=',M-1` | 일치 | p.124의 선택 가능한 물리 셀 번호 상한과 달리 전체 출력은 가상 셀도 포함한다. N 상한을 단순 오기로 고치면 안 된다. |
| KS3-155 | p.125 `FILE GRP STEP`, `FILE GRP TIME`; 기본 미출력 | `vf_iifile.f:148,151,160` `'GRP'`, `'STEP'`, `'TIME'`; `:153–158` IGRTRN 정수 세 개와 `IF (IGRTRN(1).GT.IGRTRN(2) .OR. IGRTRN(3).LE.0)`<br>`     &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')`; `:162–167` RGRTRN 실수 세 개와 `IF (RGRTRN(1).GT.RGRTRN(2) .OR. RGRTRN(3).LE.0.0D0)`<br>`     &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')`; `vf_a2dflt.f:93` `IGRTYP=0` | 일치 | 공통 일정 형식과 제한이 같다. |
| KS3-156 | p.125 `FILE GRP AREA [IC1] [JC1] [KC1] [IC2] [JC2] [KC]`; 표에는 KC2 | `vf_iifile.f:169–173` `'AREA'` / `DO 100 I=1,6` / `CALL VF_ZSTOI(IGRARA(I),TEXT(IS(I+3):IE(I+3)))` / `IGRARA(I)=IGRARA(I)+1` | 불일치 | 마지막 인수 KC는 KC2의 오기이다. B. |
| KS3-157 | p.125 IC1·JC1·KC1 기본 1, IC2·JC2·KC2 기본 NI−1·NJ−1·NK−1; 모두 I*4; 끝점 제한은 각각 `<NI-1`, `<NJ-1`, `<NK-1` | `vf_iifile.f:181–187` `IF ((IGRARA(1).GT.IGRARA(4)) .OR.`<br>`     &        (IGRARA(2).GT.IGRARA(5)) .OR.`<br>`     &        (IGRARA(3).GT.IGRARA(6)) .OR.`<br>`     &        (IGRARA(4).GE.NUMI0    ) .OR.`<br>`     &        (IGRARA(5).GE.NUMJ0    ) .OR.`<br>`     &        (IGRARA(6).GE.NUMK     )     )`<br>`     &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')` | 불일치 | 입력 끝점 NI−1·NJ−1·NK−1을 허용한다. 문서의 엄격 부등호는 같은 표 기본값과 모순이다. B. |
| KS3-158 | p.126 `[* c1 =<0]`이면 1, `[* c2 <=0]`이면 N−1; 기본 전체 | `vf_iifile.f:175–180` `IF (IGRARA(1).LE.1) IGRARA(1)=2` / `IF (IGRARA(2).LE.1) IGRARA(2)=2` / `IF (IGRARA(3).LE.1) IGRARA(3)=2` / `IF (IGRARA(4).LE.1) IGRARA(4)=NUMI0-1` / `IF (IGRARA(5).LE.1) IGRARA(5)=NUMJ0-1` / `IF (IGRARA(6).LE.1) IGRARA(6)=NUMK -1`; `vf_a2dflt.f:95` `CALL VF_ZSETI1(IGRARA,1,6)` | 일치 | +1 이후의 조건이다. 기본값도 이 규칙으로 전체 영역이 된다. |
| KS3-159 | p.125–126 `FILE GRP ON VORT`, `OFF VORT`; 기본 OFF; 농도 성분 [+1]…[+3]에 와도 | `vf_iifile.f:189–200` `'ON'` / `'VORT'` / `IGRVOR=1`; `'OFF'` / `'VORT'` / `IGRVOR=0`; `vf_a2dflt.f:96` `IGRVOR=0`; `vf_og1ini.f:96–98` `LS=0` / `IF (LEQC .GT.0) LS=LEQC` / `IF (IGRVOR.NE.0) LS=LS+3` | 불일치 | 구현은 농도 성분 뒤에 와도 세 성분을 추가한다. p.126의 `density component`는 concentration component의 번역 오기이다. B. |
| KS3-160 | p.126 최소 2×2 셀; 1셀 방향은 그리지 않음 | `vf_og1ini.f:61–72` 격자 크기와 출력 범위를 기록 | 문서에만 | 뷰어 표시 제약이다. 입력 읽기 루틴이 두 방향에 2셀 이상을 강제한다는 뜻이 아니다. H. |
| KS3-161 | p.126 `FILE RSL STEP`, `FILE RSL TIME`; 기본 미출력 | `vf_iifile.f:210,213,222` `'RSL'`, `'STEP'`, `'TIME'`; `:219–220` `IF (IRSTRN(1).GT.IRSTRN(2) .OR. IRSTRN(3).LE.0)`<br>`     &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')`; `:228–229` `IF (RRSTRN(1).GT.RRSTRN(2) .OR. RRSTRN(3).LE.0.0D0)`<br>`     &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')`; `vf_a2dflt.f:97` `IRSTYP=0` | 일치 | 공통 일정 형식과 자료형이 같다. |
| KS3-162 | p.126 `FILE RSL ELAPSE [ETIME]`; R*8 s; `ETIME>0.0`; 기본 `-`; STEP·TIME과 중복 가능 | `vf_iifile.f:231–233` `'ELAPSE'` / `CALL VF_ZSTOR(ETIME,TEXT(IS(4):IE(4)))`; `vf_a2dflt.f:131` `ETIME=1.0D30` | 불일치 | 코드는 ETIME의 양수 검사를 하지 않는다. 생략 기본값은 10³⁰ s이다. 문서는 이 두 동작을 적지 않는다. C. |
| KS3-163 | p.126 매 단계 경과시간이 ETIME를 초과하면 재시작·ars 출력 후 종료 | `vf_a1main.f:1000–1007` `CALL VF_P0TIME(WTM2)` / `IEND1(2)=0` / `IF(WTM2-WTM1.GT.ETIME) IEND1(2)=1` / `CALL MPI_ALLREDUCE(IEND1,IEND,2,MPI_INTEGER,MPI_MAX,`<br>`     $                     comm_mlicdsmg2fc,IERR)` / `IE = IEND(1)` / `IEE= IEND(2)` / `IF (IE.EQ.1 .OR. IEE.EQ.1) GOTO 1000` | 일치 | 경과시간 초과를 전체 프로세스에 합친다. 종료 출력 호출은 보충 원문에 둔다. |
| KS3-165 | p.126–127 `FILE TRN STEP`, `FILE TRN TIME`; ISTR·IEND·ISTEP I*4, TSTR·TEND R*8, TSTEP 인쇄 `*8`; 동일 일정 제한 | `vf_iifile.f:247,250,259` `'TRN'`, `'STEP'`, `'TIME'`; `vf_a2dflt.f:100` `ITRTYP=0` | 불일치 | 시간 간격 TSTEP의 자료형에서 R이 빠졌다. 실수 읽기 원문은 보충 표에 둔다. B. |
| KS3-166 | p.126–128 `FILE TRN W-LEVEL ANS {DIR}`; C*(*), X−·X+·Y−·Y+·SRC | `vf_iifile.f:268,275–285` `'W-LEVEL'` / `'ANS'` / `'X-'` / `'X+'` / `'Y-'` / `'Y+'` / `'SRC'`; `ITRPRM(3,ITRNUM)`에 −1…−5 저장 | 일치 | 조파 네 경계와 조파 소스의 이론 수위를 구분한다. |
| KS3-167 | p.126 `FILE TRN W-LEVEL [IC1] [JC1]`; I*4, 셀 범위 | `vf_iifile.f:297–298` `ITRPRM(3,ITRNUM)=I1+1` / `ITRPRM(4,ITRNUM)=J1+1`; `vf_ot1trn.f:94` `CALL VF_CWLVL(ZZ,FF,RTRVAL(L),NF,ITRPRM(3,L),ITRPRM(4,L))` | 일치 | 지정 수직 열의 계산 수위를 출력한다. |
| KS3-168 | p.126–128 `FILE TRN FORCE {FDIR} [IC1] [JC1] [KC1] [IC2] [JC2] [KC2]`; C*(*) 여섯 방향; 여섯 I*4 셀 범위 | `vf_iifile.f:330,340,342,344,346,348,350` `'FORCE'`, `'X-'`, `'X+'`, `'Y-'`, `'Y+'`, `'Z-'`, `'Z+'`; 종류 코드 11…16; `:431–434` `IF (I2.LT.I1 .OR. I2.GT.NUMI0-2 .OR.`<br>`     &          J2.LT.J1 .OR. J2.GT.NUMJ0-2 .OR.`<br>`     &          K2.LT.K1 .OR. K2.GT.NUMK -2     )`<br>`     &          CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')` | 일치 | 장애물에 작용하는 방향별 힘과 상자를 지정한다. |
| KS3-169 | p.127–128 `FILE TRN POINT {PHY} [I1] [J1] [K1]`; U·V·W·P·F·K·E·T·C [LC]; 좌표 I*4; U의 I·V의 J·W의 K만 격자 번호 | `vf_iifile.f:310` `'POINT'`; `:356–378` `'U'`, `'V'`, `'W'`, `'P'`, `'F'`, `'K'`, `'E'`, `'T'`, `'C'`; `:405–408` `IF (I1.LT.1 .OR. I1.GT.NUMI0-1 .OR.`<br>`     &          J1.LT.1 .OR. J1.GT.NUMJ0-2 .OR.`<br>`     &          K1.LT.1 .OR. K1.GT.NUMK -2     )`<br>`     &          CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')`; V·W는 :411–420에서 해당 방향만 한 칸 더 허용 | 일치 | 속도는 면 중심, 나머지는 셀 중심이다. |
| KS3-170 | p.127–128 `FILE TRN POINT VORT-X/Y/Z [IC1] [JC1] [KC1]` | `vf_iifile.f:380–391` `'VORT-X'` / 17, `'VORT-Y'` / 18, `'VORT-Z'` / 19; 각 `IF (ITRPRM(1,ITRNUM).NE.1)`<br>`     &                      CALL VF_A2ERR('VF_IIFILE','{PHY} ERROR.')` | 일치 | 와도는 POINT에서만 허용한다. |
| KS3-171 | p.127–128 `FILE TRN {CALC} {PHY} [IC1] [JC1] [KC1] [IC2] [JC2] [KC2]`; MIN·MAX·AV·INT; 부피 평균·적분 | `vf_iifile.f:314,318,322,326` `'MIN'`, `'MAX'`, `'AV'`, `'INT'`; `ITRPRM(1,ITRNUM)=2,3,4,5`; `:428–434` 끝점 정수 읽기와 상자 검사 | 일치 | 계산 방법 네 개와 셀 상자를 읽는다. 실제 부피 가중 계산은 보충 원문에 둔다. |
| KS3-172 | p.128 LC `R*8`, `1=<LS=<NS` | `vf_iifile.f:375–377` `CALL VF_ZSTOI(LC,TEXT(IS(5):IE(5)))` / `IF (LC.LE.0 .OR. LC.GT.LEQC)`<br>`     &                     CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')` | 불일치 | LC는 정수 성분 번호이다. B. |
| KS3-173 | p.128 \(\mathrm{VORT-X}: @w/@y-@v/@z\), \(\mathrm{VORT-Y}: @u/@z-@w/@x\), \(\mathrm{VORT-Z}: @v/@x-@u/@y\) | `vf_iifile.f:380,384,388` 해당 문자열; `VF_CVORT` 계산 원문은 보충 표 | 일치 | 세 회전 성분의 부호와 순서가 같다. 원문의 @는 편미분 기호로 인쇄한 표기이다. |
| KS3-174 | p.128 병렬 MIN 상한 `1.0D+30`; MAX 하한은 인쇄 문장 `-1. Limited to 0 D + 30` | `vf_ot1trn.f`의 지역 최솟값·최댓값 초기화와 전역 축약은 보충 원문 | 불일치 | MAX의 의도한 하한은 −1.0D+30이다. 인쇄 문장이 소수점을 잘못 끊었다. B. |
| KS3-181 | p.129 `FILE PORO [NT]`; I*4, 0, `>=0`; NT=0 미독입, NT=1 시간 불변 | `vf_iifile.f:471,473–474` `'PORO'` / `CALL VF_ZSTOI(IPRNT,TEXT(IS(3):IE(3)))` / `IF (IPRNT.LT.0) CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')`; `vf_a2dflt.f:106` `IPRNT=0`; `vf_ip1inp.f:29` `IF (IPRNT.GE.1 .AND. IPRIT.LT.0) THEN`; `vf_cggv.f:42–44` `IF (IPRNT.EQ.1) THEN` / `AOLD=0.0D0` / `ANOW=1.0D0` | 일치 | 시간 블록 수와 한 블록 고정 처리가 같다. |
| KS3-182 | p.129 `エージェントモデル用出力制御データ`; `FILE MAM STEP`, `FILE MAM TIME`; 기본 미출력; 공통 일정 인수·형·제한 | `vf_iifile.f:445,448,457` `'MAM'`, `'STEP'`, `'TIME'`; `:454–455` `IF (IMMTRN(1).GT.IMMTRN(2) .OR. IMMTRN(3).LE.0)`<br>`     &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')`; `:463–464` `IF (RMMTRN(1).GT.RMMTRN(2) .OR. RMMTRN(3).LE.0.0D0)`<br>`     &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')`; `vf_a2dflt.f:104` `IMMTYP=0` | 일치 | 일본어 뜻은 “에이전트 모델용 출력 제어 데이터”이다. 정수 단계 또는 실수 시간으로 예약한다. |

### 2.8 p.129–135 (441–447): 선택 옵션·디버그

| 행 ID | 문서(위치, 원문) | 코드(파일:줄 원문) | 판정 | 이유 |
|---|---|---|---|---|
| KS3-192 | p.129–130 `OPTION T-DOOR BUB OFF`, `OPTION T-DOOR BUB [WBUB]`; R*8, m/s, 0.2, `WBUB>=ZERO`; 기본 상승 | `vf_iiopt.f:58,60–65` `'T-DOOR'` / `'BUB'` / `'OFF'` / `WBUB=0.0D0` / `CALL VF_ZSTOR(WBUB,TEXT(IS(4):IE(4)))` / `IF (WBUB.LT.ZERO) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')`; `vf_a2dflt.f:205` `WBUB =0.2D0` | 일치 | OFF는 0으로 설정한다. 실수 입력 0은 ZERO 미만이므로 OFF 대신 쓸 수 없다. |
| KS3-193 | p.130 `OPTION T-DOOR DROP OFF`, `FREE-RUNDOWN` | `vf_iiopt.f:67–71` `'DROP'` / `'OFF'` / `IDROP=0` / `'FREE-RUNDOWN'` / `IDROP=1`; `vf_a2dflt.f:151` `IDROP=1` | 일치 | 자유낙하 처리를 켜거나 끈다. 생략 시 FREE-RUNDOWN이다. 기본값 누락은 KS3-307이다. |
| KS3-194 | p.130 `OPTION S-CELL-VEL DU=0`, `D2U=0`; 영 기울기·속도 외삽 | `vf_iiopt.f:47–52` `'S-CELL-VEL'` / `'DU=0'` / `IBSUW0=1` / `'D2U=0'` / `IBSUW0=0`; `vf_a2dflt.f:45` `IBSUW0=0` | 일치 | 두 선택지의 플래그가 다르다. 기본 D2U=0은 p.138 출력 예제에도 보인다. |
| KS3-195 | p.130 `OPTION SUB-LOOP [LOOP]`; I*4, 기본 1, `LOOP>=1`; 1이면 보통 계산과 같음 | `vf_iiopt.f:41,43–44` `'SUB-LOOP'` / `CALL VF_ZSTOI(LOOPS,TEXT(IS(3):IE(3)))` / `IF (LOOPS.LT.1) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')`; `vf_a2dflt.f:224` `LOOPS =1`; `vf_a1main.f:1029` `DTNOW=DT/DBLE(LOOPS)` | 일치 | 압력·속도 적분의 시간 간격을 하위 반복 수로 나눈다. |
| KS3-196 | p.130–131 `OPTION PV=CONST [PVCP0] [PVCGM]`; R*8, Pa·무차원, 기본 `-`; `PVCP0>=ZERO`, `PVCGM>=1.0` | `vf_iiopt.f:80,82–85` `'PV=CONST'` / `CALL VF_ZSTOR(PVCP0,TEXT(IS(3):IE(3)))` / `CALL VF_ZSTOR(PVCGM,TEXT(IS(4):IE(4)))` / `IF (PVCP0.LT.ZERO ) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')` / `IF (PVCGM.LT.1.0D0) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')`; `vf_a2dflt.f:207–208` `PVCP0=0.0D0` / `PVCGM=0.0D0` | 일치 | 명령을 주면 두 인수가 필수이다. 생략하면 공기압 모델 비활성이다. |
| KS3-197 | p.131 `The air bubbles contacting the wave formation, radiation, free are set to atmospheric pressure` | `vf_fpvcpp.f:77` `IF (M.EQ.4 .OR. M.EQ.5 .OR. M.EQ.7) IPVCBC(L)=1`; `:183–184` `IF (IPVCBC(L).NE.0) THEN` / `PVCPES(L)=0.0D0` | 일치 | 자유·조파·放射 경계와 접촉한 기포의 게이지 압력을 0으로 둔다. 放射는 방사라는 뜻이다. 압력 차감 방향의 영어 문장은 KS3-280에서 별도로 판정한다. |
| KS3-201 | p.131 `OPTION DRAG-DF [YU] [N]`; YU R*8 m²/s `>0.0`, N I*4 `>0`, N≤10 | `vf_iiopt.f:88–94` `'DRAG-DF'` / `CALL VF_ZSTOR(DRGYU,TEXT(IS(3):IE(3)))` / `IF (DRGYU.LE.0.0D0) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')` / `CALL VF_ZSTOI(IDRGN,TEXT(IS(4):IE(4)))` / `IF (IDRGN.LE.0) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')` / `IF (IDRGN.GT.MAXDRG) CALL VF_A2ERR('VF_IIOPT','AREA IS FULL.')`; `VF_A0PRM.h:20` `     &           MAXDRG= 10,` | 일치 | 동점성계수와 계수 구간 수를 읽는다. 기본은 비활성 IDRGN=0이다(`vf_a2dflt.f:155` `IDRGN=0`). |
| KS3-202 | p.131 다음 N행 `[DRi] [APi] [BTi]`; R*8, m·무차원·무차원; DRi>0, APi·BTi≥0 | `vf_iiopt.f:95–108` `DO 100 I=1,IDRGN` / `CALL VF_ZGETLN(IS,IE,MAXWDS,NWD,IFIL,IEOF,TEXT)` / `IF (NWD.NE.3) CALL VF_A2ERR('VF_IIOPT','SYNTAX ERROR.')` / `CALL VF_ZSTOR(DRGDR(I),TEXT(IS(1):IE(1)))` / `CALL VF_ZSTOR(DRGAP(I),TEXT(IS(2):IE(2)))` / `CALL VF_ZSTOR(DRGBT(I),TEXT(IS(3):IE(3)))` / `IF (DRGDR(I).LE.0.0D0)`<br>`     &            CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')`<br>`          IF (DRGAP(I).LT.0.0D0)`<br>`     &            CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')`<br>`          IF (DRGBT(I).LT.0.0D0)`<br>`     &            CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')` | 일치 | 각 행이 정확히 세 단어여야 한다. |
| KS3-203 | p.131 \(0.0<\mathrm{DR}\le\mathrm{DR1}\): \(\alpha0=0.0,\beta0=0.0\); \(\mathrm{DR1}<\mathrm{DR}\le\mathrm{DR2}\): AP1·BT1; \(\mathrm{DR2}<\mathrm{DR}\le\mathrm{DR3}\): AP2·BT2; \(\mathrm{DRN}<\mathrm{DR}\): APN·BTN | `vf_vgene.f:112–126` `IF (GV.LE.PLOWER .OR. CD.LE.DRGDR(1)) THEN` / `RN=PLOWER` / `DR=DRGDR(1)` / `AP=0.0D0` / `BT=0.0D0`; 그 외 `DR=CD`, `AP=DRGAP(IDRGN)`, `BT=DRGBT(IDRGN)`; `DO 150 L=2,IDRGN` / `IF (DR.LE.DRGDR(L)) THEN` / `AP=DRGAP(L-1)` / `BT=DRGBT(L-1)` | 일치 | 구간 끝점에서 앞 구간 계수를 쓰는 조건이 같다. 공극률 하한 분기는 KS3-309이다. |
| KS3-204 | p.131 CD0는 사석 입경 m; YU는 MATE K-VISC와 별도; 설명 `Dynamic viscosity coefficient` | `vf_vgene.f:119,131,133–134` `DR=CD` / `YU =DRGYU` / `ALPHAX=AP*RN1*RN1*RN1*YU/(RN*RN*DR*DR)` / `BETAX =BT*RN1/(RN*RN*RN*DR)` | 불일치 | 입경과 별도 입력은 같다. m²/s의 YU는 동점성계수이다. dynamic viscosity라는 설명은 같은 표의 kinematic 및 단위와 모순이다. B. |
| KS3-205 | p.131 `Comment lines and blank lines are not allowed ... [N] lines` | `vf_iiopt.f:98–99` `CALL VF_ZGETLN(IS,IE,MAXWDS,NWD,IFIL,IEOF,TEXT)` / `IF (NWD.NE.3) CALL VF_A2ERR('VF_IIOPT','SYNTAX ERROR.')` | 일치 | 주석만 있는 행과 빈 행은 NWD=0이 되어 오류이다. 행 끝 주석은 허용한다. |
| KS3-206 | p.132 `OPTION SEA-BOTTOM OFF`, `ON`, `CALC`; ON sbt, CALC fault_cad.txt | `vf_iiopt.f:113–121` `'SEA-BOTTOM'` / `'ON'` / `ISEABT = 1` / `'OFF'` / `ISEABT = 0` / `cadd 20130703(s)` / `'CALC'` / `ISEABT = -1`; `vf_a2dflt.f:237` `ISEABT = 0`; `VF_ASEABT.h:3` `COMMON/VF_ASEABI/ISEABT` | 일치 | 일반 수위 변동 읽기와 단층 매개변수 계산을 구분한다. 2012.03·20130703 날짜 표지가 있다. |
| KS3-207 | p.132 `tomographic parameters` | `mod_fault.f:59` `INTEGER:: JSYSTEM=2 ! 断層パラメータの測地系の番号(1-3)` | 불일치 | 일본어 뜻은 “단층 매개변수의 측지계 번호(1–3)”이다. tomographic은 단층 촬영을 뜻하므로 fault parameters로 고친다. B. |
| KS3-208 | p.132 `OPTION COORDINATE JAPAN-PLANE-RECTANGULAR [ICOORD]`; I*4, 1≤ICOORD≤19, CALC에만 유효 | `vf_iiopt.f:130,132–135` `'COORDINATE'` / `'JAPAN-PLANE-RECTANGULAR'` / `CALL VF_ZSTOI(ICOORD,TEXT(IS(4):IE(4)))` / `IF (ICOORD.LT.1.OR.ICOORD.GT.19)`<br>`     $      CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')` | 일치 | 일본 평면직각 좌표계 구역 번호를 지정한다. |
| KS3-209 | p.132–133 `OPTION COORDINATE UTM [LC_DEG]`; R*8 degree, \(0\le\mathrm{LC\_DEG}<360\); CALC에만 유효 | `vf_iiopt.f:136–138` `'UTM'` / `CALL VF_ZSTOR(LC_DEG,TEXT(IS(4):IE(4)))` / `CALL SET_UTM(LC_DEG)`; `mod_fault.f:209,213` `REAL(8),INTENT(IN):: LC_DEG` / `ORI_L(0) = LC_DEG*D2R` | 불일치 | 코드에는 이 범위 검사가 없다. 각도를 그대로 라디안으로 바꾼다. 문서 누락 C로 판정한다. 문서의 입력 의무 자체를 코드가 보장하지 않는다. |
| KS3-210 | p.133 `OPTION FAULT-SYSTEM {SYS}`, `OPTION GRID-SYSTEM {SYS}`; C*(*), JGD2000; TOKYO·JGD2000·WGS84; CALC에만 유효 | `vf_iiopt.f:144,146,148,150` `'FAULT-SYSTEM'`, `'TOKYO'`, `'JGD2000'`, `'WGS84'`; `:157,159,161,163` `'GRID-SYSTEM'`, `'TOKYO'`, `'JGD2000'`, `'WGS84'`; `mod_fault.f:58–59` `INTEGER:: ISYSTEM=2 ! 計算メッシュの測地系の番号(1-3)` / `INTEGER:: JSYSTEM=2 ! 断層パラメータの測地系の番号(1-3)` | 일치 | 일본어 뜻은 각각 계산 격자와 단층 매개변수의 측지계 번호이다. 기본 2가 JGD2000이다. |
| KS3-211 | p.133 `OPTION MAX-VELOCITY [VVMAX]`; R*8, 기본 `-`, `0<VVMAX`; 가속도 적분 후 임시 속도에 적용 | `vf_iiopt.f:170,172–173` `'MAX-VELOCITY'` / `CALL VF_ZSTOR(VVMAX,TEXT(IS(3):IE(3)))` / `IF (VVMAX.LE.ZERO ) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')`; `vf_a2dflt.f:218` `VVMAX=30.0D0`; `vf_veuler.f:127–128` `IF (UU(I,J,K).GT. VVMAX) UU(I,J,K)= VVMAX` / `IF (UU(I,J,K).LT.-VVMAX) UU(I,J,K)=-VVMAX` | 불일치 | 기본 제한 30 m/s를 문서가 적지 않는다. 검사는 단순 양수보다 강한 VVMAX>ZERO이다. C. |
| KS3-212 | p.133 설명 `Flow rate limit` | `vf_veuler.f:127–128`의 UU 성분 제한; VV `:184–185`, WW `:241–242`도 같은 ±VVMAX 제한 | 불일치 | 제한 대상은 유량이 아니라 속도 각 성분이다. 단위는 m/s이다. B. |
| KS3-215 | p.134 `DEBUG F-BOX [IC1] [JC1] [KC1] [IC2] [JC2] [KC2] [FF]`; 좌표 I*4 1…N−1, FF R*8 0…1; 마지막 한 상자 | `vf_iidbg.f:33,35–37` `'F-BOX'` / `DO 100 I=1,6` / `CALL VF_ZSTOI(IDBGF(I),TEXT(IS(I+2):IE(I+2)))` / `IDBGF(I)=IDBGF(I)+1`; `:49–52` `CALL VF_ZSTOR(RDBGF,TEXT(IS(9):IE(9)))` / `IF ((RDBGF.LT.0.0D0) .OR.`<br>`     &      (RDBGF.GT.1.0D0)     )`<br>`     &                CALL VF_A2ERR('VF_IIDBG','INVALID VALUE.')`; `vf_a2dflt.f:69,73` `CALL VF_ZSETI1(IDBGF ,0,6)` / `RDBGF=0.0D0` | 일치 | 같은 저장 슬롯을 덮으므로 마지막 상자만 남는다. |
| KS3-216 | p.134–135 `DEBUG TD-VEL [IC1] [JC1] [KC1] [IC2] [JC2] [KC2] [U] [V] [W]`; 좌표 I*4 1…N−1; 속도 R*8 제한 없음; 마지막 한 상자 | `vf_iidbg.f:55,57–59,71–73` `'TD-VEL'` / `DO 200 I=1,6` / `CALL VF_ZSTOI(IDBGTD(I),TEXT(IS(I+2):IE(I+2)))` / `IDBGTD(I)=IDBGTD(I)+1` / `CALL VF_ZSTOR(RDBGTD(1),TEXT(IS( 9):IE( 9)))` / `CALL VF_ZSTOR(RDBGTD(2),TEXT(IS(10):IE(10)))` / `CALL VF_ZSTOR(RDBGTD(3),TEXT(IS(11):IE(11)))`; `vf_a2dflt.f:70,74` `CALL VF_ZSETI1(IDBGTD,0,6)` / `CALL VF_ZSETR1(RDBGTD,0.0D0,3)` | 일치 | 두 디버그 상자는 별도 저장한다. 방향별 속도 인수는 U·V·W 순서이다. |

### 2.9 p.135–143 (447–455): 출력 파일·예제

문서 예제의 계산값은 실행 재현의 증거로 사용하지 않는다. 아래 표는 출력 항목과 형식 및 정적으로 계산 가능한 관계를 대조한다. `Omitted`는 모든 표에서 생략 표지이다. p.141에는 ITR 정의 한 문장만 있다. 이 쪽을 빈 쪽으로 세지 않는다.

| 행 ID | 문서(위치, 원문) | 코드(파일:줄 원문) | 판정 | 이유 |
|---|---|---|---|---|
| KS3-221 | p.135 §5.3 텍스트 `data.List`; 물리 시간·BiCGSTAB 반복 수 출력 | `vf_a1main.f:372–374` `OPEN(MFILLP,ERR=9010,`<br>`     &       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.list',`<br>`     &       STATUS='NEW',FORM='FORMATTED' )`; 단계 형식은 아래 보충 원문 | 일치 | 단일 프로세스 확장자는 `.list`이다. 소문자 확장자를 실제 입력·출력 이름에 사용한다. |
| KS3-222 | p.135 예제 `Ver.1.0 START`·MYRANK·DEFAULT·INPUT-DATA; p.136 SETUP·CONDITION; p.139 INITIAL·CALCULATION·NORMAL END | `VF_A0PRM.h:2` `PARAMETER (IVR001=  0, IVR002=  1,`; `vf_a1main.f:1208–1209` `9510 FORMAT(/' ',`<br>`     &       '##### CADMAS-SURF/3D-MG Ver.',I1,'.',I1,' START. ######')`; `:1234` `9990 FORMAT(/' ','##### NORMAL END. ###########################'/)` | 불일치 | 출력 단계의 의미는 같다. 공급 코드가 인쇄하는 버전은 0.1이며 예제는 1.0이다. 버전 문자열은 판 표기의 차이 A이다. |
| KS3-223 | p.135–136 INPUT-LEVEL=0·1·2; 대괄호 명령 에코; 격자 에코의 `&` | `vf_ii1inp.f:115` `WRITE(ILPFIL,9510) '## INPUT-LEVEL=',LEVEL`; `:537` `9520 FORMAT( ' ',100('[',A,']':))`; `vf_iigrid.f:144` `9510 FORMAT(' ','& ',100('[',A,']':))` | 일치 | 격자 수·경계 수·기타 자료의 세 판독 단계를 구분한다. |
| KS3-224 | p.136 PARALLEL NPROCS=4, NPI/NPJ=4/1, MYRANK=0, MYI/MYJ=1/1, CELL-X=400·Y=1·Z=50; x 담당 1…100, y 1…1, z 1…50; 방정식 셋 NOCALC; 시간 SAFE=.2, INIT=.001, MIN=1e−5, MAX=.05, END=999999·40.1 | `vf_ol1ini.f`의 PARALLEL·EQUATION·TIME 출력; 입력·분할 원문은 KS3-011–012·027–034 | 일치 | 예제 입력·기본값과 출력 항목의 대응이 같다. X는 401 좌표이고 내부 전체 크기는 402이다. 네 부분영역의 첫 부분은 100셀이다. |
| KS3-225 | p.137 MATERIAL: 수위10, 밀도1000, 점성0, 중력9.8, 초기 속도셋0; STREAM 차수5·D10·H4·T8.007·A2; DAMP 차수2·.6·.6·146.0804·10 | `vf_ol1ini.f:133–140` 물성 출력; `:219` `WRITE(ILPFIL,9540) '  AMPL       [-]=',BCTYP(8,JD)`; 입력 근거 KS3-013–016 | 일치 | 지정값을 같은 물리량으로 출력한다. 단위는 물성표와 같다. |
| KS3-226 | p.137 계산 결과 예 `LENGTH=7.30402E+01`, `URSELL NUMB=2.51319E+01`, `0.0=WAVE(x)=7.97690E-01`; OPEN-BC 길이70.9303·속도8.85853 | `vf_csetup.f:103,113,116,123–125` `IF (D.GE.ZERO) WUS=GRZ0*H*T*T/D/D` / `CALL VF_CWMAK0(D,T,H,WLN,N)` / `CALL VF_CWZERO(WT0,N)` / `BCTYP(4,JD)=WLN` / `BCTYP(5,JD)=WUS` / `BCTYP(6,JD)=WT0` | 문서에만 | 예제 수치는 특정 계산의 결과이다. Ursell 수는 9.8×4×8.007²/10²=25.131923208로 표와 반올림이 맞는다. 나머지 수치의 재현 실행은 하지 않았다. H. |
| KS3-227 | p.137 `OPEN-BC ... VELOCITY [-]` | `vf_csetup.f`의 파장/주기 파속 저장; `vf_ol1ini.f`의 속도 단위 원문은 보충 표 | 불일치 | 70.9303 m/8.007 s=8.85853 m/s이다. 코드 출력 라벨도 `[-]`이다. 자기 주석의 파속 및 WLN/T 계산과 모순인 출력 라벨 E 후보이다. KS3-279와 같은 후보이다. |
| KS3-228 | p.138 VP-DNR .2; FF-DN-AC; MILU-BCGSTAB .95·500·1e−12·1e−10; RES NOT READ; L/P NOT WRITE; GRP BY TIME 0…9999.9, 8.007; AREA1 (1,1,1), AREA2 (400,1,50); RSL NOT WRITE; TRN BY STEP 0…999999,1; PORO NOT READ; LOOP1·D2U=0·BUB/DROP NOT USE | 입력 근거 KS3-017·020–022; 기본값 `vf_a2dflt.f:37–63,89–106,151,224`; 출력 원문은 `vf_ol1ini.f`의 COMPUTATION·FILE CONTROL·OPTION | 일치 | 옵션 출력과 각 설정값이 같은 의미를 나타낸다. 키워드 `M-ILUBCGSTAB`를 출력 설명에서는 MILU-BCGSTAB로 표시한다. |
| KS3-229 | p.138 `NUMBER OF GRID-X=102`; I·X·DX·CX; 첫 행 I=0, X=−.913003, DX=.913003, CX=0; `Omitted` 뒤 인쇄 행 51·20.0·.4·.4 | `vf_cpara.f:79,89` `NUMI =MYGIE-MYGIS+1` / `NUMI =NUMI+MYMIS+MYMIE`; `vf_iigrid.f:47` `NL  =1`; `vf_ol1ini.f:467` `WRITE(ILPFIL,9530) 'NUMBER OF GRID-X =',NUMI-1`; `:477` `WRITE(ILPFIL,9530) 'NUMBER OF GRID-Z =',NUMK-1` | 일치 | 100개 담당 셀에 물리 경계 가상 셀 1개와 내부 통신 셀 2개를 더하면 NUMI=103이다. GRID-X 출력은 NUMI−1=102이다. 해석: Omitted는 중간 Y·Z 표제까지 생략할 수 있다. 51·20.0은 Z 표의 끝 행과 맞는다. 생략 범위를 X 표 안으로 한정하여 오기로 판정하지 않는다. |
| KS3-230 | p.139–140 OBSTACLE·BOUNDARY, FILE-GRP INITIAL·OUT, 단계 정보, CPU TIME 계층, NORMAL END | `vf_og1ini.f:55` `WRITE(ILPFIL,9510)`; `vf_a1main.f:956,958` `WRITE(ILPFIL,9540) NNOW,TNOW,DTNOW,FSUM,FCUT,DV` / `WRITE(ILPFIL,9550) CGBNRM,CGXNRM,ICGITR`; `vf_a2cput.f:93` `9510 FORMAT(/' ','##### CPU TIME [S] ##########################')` | 일치 | 입력 읽기와 초기화·적분·파일 출력·종료 순서의 설명이 같다. |
| KS3-231 | p.139–140 예제 STEP918…920·물리시간·DT·B·R·ITR·각 CPU 초; TOTAL117.65, PRE .10, CALC117.55, I/O1.25, VELO&PRES105.42, CONV&VISC4.08, GENERATION1.26, INTEGRATION2.27, POISSON COEF2.53, SOLV82.84, MODIF1.33, 기타11.11; T/C/K0, VOF9.06, VOF하위1.84·.50·.85·1.14·4.74, 기타1.82·0; VF_P*****36.32·M1BCGS82.77·FDROPF0 | `vf_a2cput.f:93–96` CPU 출력 형식; `vf_a1main.f:1214–1223` 단계·노름·반복 출력 형식 | 문서에만 | 이 값들은 특정 실행의 시간·수렴 결과이다. 성능·수치 재현을 이 보고서에서 주장하지 않는다. H. |
| KS3-232 | p.140 STEP 계산 단계, TIME 물리 시간, DT `= tn - tn - 1`; p.141 ITR `Number of repetitions of solving simultaneous linear equations` | `vf_a1main.f:955–958` `IF (MGRANK.EQ.0) WRITE(*,9530) NNOW,TNOW,DTNOW` / `WRITE(ILPFIL,9540) NNOW,TNOW,DTNOW,FSUM,FCUT,DV` / `WRITE(ILPFIL,9550) CGBNRM,CGXNRM,ICGITR` | 일치 | DT 식은 \(t_n-t_{n-1}\)를 뜻한다. 단계·시간·시간 간격·반복 수의 출력 변수가 같다. |
| KS3-233 | p.140 FSUM `sum of (VOF function F value × cell area)`; FCUT `cutoff VOF function F value × cell area` | `vf_fcut01.f:40–48` `V=XX(2,I)*YY(2,J)*ZZ(2,K)*GGV(I,J,K)` / `FCUT=FCUT+(FF(I,J,K)-1.0D0)*V` / `FCUT=FCUT+(FF(I,J,K)-0.0D0)*V` / `FSUM=FSUM+FF(I,J,K)*V` | 불일치 | 3차원 셀 체적에 공극률을 곱한다. 면적이 아니다. FCUT는 절단 전 값과 절단 후 값 차이의 부호 있는 합이며 FSUM은 절단 후 물 체적이다. B. |
| KS3-234 | p.140 `!VD!: The square of the (divergence × cell area)`; `!B!: Squared norm`; `!R!: The square of the final residual vector` | `vf_cdiv00.f:49,55–56` `VAL=VAL+VD*VD` / `CALL VF_P1SUMD(W,VAL)` / `VAL=SQRT(VAL)`; `vf_m1bcgs.f:249–250` `BNORM=SQRT(BNORM)` / `XNORM=SQRT(XNORM)` | 불일치 | 출력은 제곱합의 제곱근인 2-노름이다. 제곱 노름이 아니다. VD의 내부 값은 면적을 곱한 면속도 차의 합이다. B. |
| KS3-235 | p.142 `.tran` 머리글의 W-LEVEL 관측 (161,1)·(241,1)을 포함한 7항목; p.106 예제에는 두 관측이 없음 | `vf_ot1ini.f:35` `DO 100 L=1,ITRNUM`; `:134` `WRITE(ITRFIL,9530) 'TIME',(L,L=1,ITRNUM)` | 불일치 | 코드는 입력한 항목 수만 출력한다. 입력 예제의 5항목과 출력 예제의 7항목은 같은 입력의 결과가 아니다. B. |
| KS3-236 | p.142 `data.Tran` 텍스트; 항목 번호·종류·좌표·TIME·계산값 열; 미사용 좌표 −1 | `vf_ot1ini.f:29–31` `OPEN(MFILTR,ERR=9010,`<br>`     &     FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.tran',`<br>`     &     STATUS='NEW',FORM='FORMATTED' )`; `:108–111` `WRITE(ITRFIL,9520) L,TEXT1,TEXT2,`<br>`     &          'X-'         ,ITRPRM(4,L)-1,ITRPRM(5,L)-1,`<br>`     &          ITRPRM(6,L)-1,ITRPRM(7,L)-1,ITRPRM(8,L)-1`; `vf_ot1trn.f:333` `IF (MYRANK.EQ.0) WRITE(ITRFIL,9510) TNOW,(RTRVAL(L),L=1,ITRNUM)` | 일치 | 미사용 내부 0을 외부 −1로 출력한다. 자료 열 순서는 시간 다음 항목 번호 순서이다. |
| KS3-237 | p.142 시간 0·.0012·.00264·.004368…40.1016249와 이론·계산 수위 예; p.143 STEP0…920의 TIME·DT 예 | `vf_cdtcal.f:147` `DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)` | 문서에만 | 첫 세 DT는 .001×1.2, .0012×1.2, .00144×1.2와 맞는다. 나머지는 실행 사례 수치이므로 H이다. |
| KS3-238 | p.143 표준출력 계산 정보, 특정 파일명을 지정하지 않음; DEFAULT·INPUT-DATA·SETUP·CONDITION·INITIAL·CALCULATION·STEP·NORMAL END | `vf_a1main.f:955` `IF (MGRANK.EQ.0) WRITE(*,9530) NNOW,TNOW,DTNOW`; `:1211–1213` `9530 FORMAT( ' ','STEP='    ,I6,`<br>`     &            ' : TIME= ',1PE12.5,`<br>`     &            ' : DT  = ',1PE12.5 )` | 일치 | 콘솔 단계 정보에는 FSUM·FCUT·노름·반복 수를 붙이지 않는다. 버전 불일치는 KS3-222에 포함했다. |

### 2.10 p.144–146 (456–458): 매트릭스·공극률·환경 파일

| 행 ID | 문서(위치, 원문) | 코드(파일:줄 원문) | 판정 | 이유 |
|---|---|---|---|---|
| KS3-241 | p.144 §5.5 Matrix data file; 임의 파형 수위·속도 텍스트 `data.Mtb` | `vf_im1inp.f:44–46` `OPEN(MFILMT,ERR=9010,`<br>`     &       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.mtb',`<br>`     &       STATUS='OLD',FORM='FORMATTED'  )` | 일치 | 실제 확장자는 소문자 `.mtb`이다. 앞 절도 5.5이므로 절 번호 중복은 편집 문제이다. |
| KS3-242 | p.144 `LEVEL-ON [nz] [nt] [T0]`, z좌표열, `T [Ti] [ei]`, 각 z의 `[ui] [wi]` | `vf_im1inp.f:61–62` `IF     (TEXT(IS(IP):IE(IP)).EQ.'LEVEL-ON'  ) THEN` / `MTBTYP=1`; `:79,90,100` `CALL VF_ZSTOI(MTBZZ,TEXT(IS(IP):IE(IP)))` / `CALL VF_ZSTOI(MTBTT,TEXT(IS(IP):IE(IP)))` / `CALL VF_ZSTOR(DMTBT0,TEXT(IS(IP):IE(IP)))`; `:155,165,172` 수위·수평·수직 속도 실수 읽기 | 일치 | nz·nt는 정수 개수이다. 나머지는 배정밀도 실수이다. 이 순서로 읽는다. |
| KS3-243 | p.144 `LEVEL-OFF [nz] [nt] [T0]`, z좌표, `T [Ti]`, `[ui] [wi]`; `LEVEL-ONLY [nt] [T0]`, `T [Ti] [ei]` | `vf_im1inp.f:63–66` `ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'LEVEL-OFF' ) THEN` / `MTBTYP=2` / `ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'LEVEL-ONLY') THEN` / `MTBTYP=3`; `:72,108,148,157` `IF (MTBTYP.NE.3) THEN` / `IF (MTBTYP.NE.3) THEN` / `IF (MTBTYP.NE.2) THEN` / `IF (MTBTYP.NE.3) THEN` | 일치 | OFF는 수위를 읽지 않는다. ONLY는 수심 좌표와 속도를 읽지 않는다. |
| KS3-244 | p.144 설명에서 `[w*]`를 `a vertical position with zero mean water level`로 적고 끝에 `z direction flow velocity`를 분리 | `vf_im1inp.f:20,23` `CD    DMTBZZ(MTBZZ)       : OUT : R*8 : マトリクスデータのz座標` / `CD    DMTBUT(MTBZZ,MTBTT) : OUT : R*8 : マトリクスデータの鉛直方向流速` | 불일치 | 일본어 뜻은 각각 매트릭스 z좌표와 수직 속도이다. z는 평균 수위를 기준으로 한 좌표이고 w는 수직 속도이다. 문서 설명의 대응이 어긋났다. B. |
| KS3-245 | p.144 \(0.0\le[T*]\le1.0\); `dimensionless phase decreases with the progression` | `vf_im1inp.f:142–146` `IF (DMTBTT(I).LT.0.0D0 .OR. DMTBTT(I).GT.1.0D0)`<br>`     &                    CALL VF_A2ERR('VF_IM1INP','INVALID VALUE.')` / `IF (I.GT.1) THEN` / `IF (DMTBTT(I).LE.DMTBTT(I-1))`<br>`     &                    CALL VF_A2ERR('VF_IM1INP','INVALID VALUE.')` | 일치 | 시간에 따른 참조 위상 감소와 파일 자료의 나열 순서는 다르다. 파일 위상은 증가순으로 입력한다. 문서가 시간 진행을 말하는 문장을 역순 입력 지시로 바꾸지 않는다. 증가순 누락은 KS3-311이다. |
| KS3-246 | p.144 위상·공간 보간; 격자·시간 간격 일치 불필요; \(t<t1\)이면 t1 값, \(t>t2\)이면 t2 값; 공간도 같음 | `vf_cwmtb1.f:29–36` `IF     (WVT.LE.DMTBTT(1)    ) THEN` / `MTBNOW=1` / `W1=1.0D0` / `W2=0.0D0` / `ELSEIF (WVT.GE.DMTBTT(MTBTT)) THEN` / `MTBNOW=MTBTT-1` / `W1=0.0D0` / `W2=1.0D0`; `:67` `WVZ=W1*DMTBHH(MTBNOW)+W2*DMTBHH(MTBNOW+1)`; `vf_cwmtb2.f:31–38` ZC에 같은 끝값 규칙 | 일치 | 위상과 z의 선형 보간 및 끝값 유지가 같다. |
| KS3-247 | p.144 `T`는 위상별 자료 시작·개수 검사; 예 `LEVEL-ON 31 101 0.796345000`, z=−10…5, T=0·e=2.57121, 속도1.42074/0·1.42190/0…4.12557/0 | `vf_im1inp.f:132–133` `IF (TEXT(IS(IP):IE(IP)).NE.'T' )`<br>`     &                    CALL VF_A2ERR('VF_IM1INP','UNKNOWN WORD.')`; `:125` `DO 210 I=1,MTBTT`; `:158` `DO 200 K=1,MTBZZ` | 일치 | 두 개수를 이용한 반복과 T 구분자를 확인했다. 예제의 중간 자료는 생략되어 실행 파일 전체가 아니다. |
| KS3-248 | p.145 `.poro` 이진; 초기 블록 다음 m개 시간 블록 | `vf_ip1inp.f:29,32–37` `IF (IPRNT.GE.1 .AND. IPRIT.LT.0) THEN` / `OPEN(MFILPR,ERR=9010,`<br>`     &         FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.poro',`<br>`     &         STATUS='OLD',FORM='UNFORMATTED' )` / `READ(IPRFIL,END=9020,ERR=9030) IPRNB,ISW1,ISW2,ISW3,ISW4` | 일치 | Fortran 순차 unformatted 레코드이다. 파일명·블록 순서가 같다. |
| KS3-249 | p.145 초기 레코드1 `NB,ISW1,ISW2,ISW3,ISW4`; 각 I*4; 확장 플래그는 당분간 0; 레코드2…NB+1은 각 IB의 I1·J1·K1·I2·J2·K2 I*4 | `vf_ip1inp.f:37` 같은 다섯 정수 읽기; `:44–46` `DO 110 IB=1,IPRNB` / `READ(IPRFIL,END=9020,ERR=9030) (IPRARA(I,IB),I=1,6)`; `:52` `IPRARA(I,IB)=IPRARA(I,IB)+1` | 일치 | 여섯 좌표의 순서와 외부 셀 번호 +1 변환이 같다. 확장 플래그를 0으로 쓰는 것은 파일 작성 규약이다. |
| KS3-250 | p.145 시간 블록 레코드1 `TIME,JSW1,JSW2,JSW3,JSW4`; TIME R*8, 나머지 I*4, 당분간 0 | `vf_ip1inp.f:81` `READ(IPRFIL,END=9020,ERR=9030) PRTNOW,JSW1,JSW2,JSW3,JSW4` | 일치 | 시각과 네 정수 플래그의 형과 순서가 같다. |
| KS3-251 | p.145 시간 블록 레코드2…NB+1 `GGV(I,J,K)` R*4; I 안쪽·J 중간·K 바깥 반복 | `vf_ip1inp.f:10,24,88–90` `IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` / `DIMENSION GGVOLD(IPRNP),GGVNOW(IPRNP)` / `READ(IPRFIL,END=9020,ERR=9030)`<br>`     &               (((GGVNOW(NP+I+NI*(J-1)+NI*NJ*(K-1)),`<br>`     &                  I=1,NI),J=1,NJ),K=1,NK)` | 불일치 | 반복 순서는 같다. 코드의 GGVNOW는 R*8이며 R*4 변환 버퍼를 거치지 않는다. R*4로 작성한 레코드는 이 읽기 형식과 다르다. B. |
| KS3-252 | p.146 시간 선형 보간; 처음 전·마지막 후에는 끝값 | `vf_cggv.f:46–54` `IF     (T0.LE.PRTOLD) THEN` / `AOLD=1.0D0` / `ANOW=0.0D0` / `ELSEIF (T0.GE.PRTNOW) THEN` / `AOLD=0.0D0` / `ANOW=1.0D0` / `ELSE` / `ANOW=(T0-PRTOLD)/(PRTNOW-PRTOLD)` / `AOLD=1.0D0-ANOW`; `:68–69` `IF (NF(I-IP,J-JP,K).NE.-1)`<br>`     &                   GGV(I-IP,J-JP,K)=GGVOLD(L)*AOLD+GGVNOW(L)*ANOW` | 일치 | NT=1도 별도로 현재값을 고정한다. |
| KS3-253 | p.146 면 투과율은 파일에 입력하지 않음; 양쪽 셀 공극률 중 작은 값 | `vf_cggxyz.f:77,103,126` `GGX(IW,JW,K)=MIN(GGV(IW,JW,K),GGV(IW-1,JW,K))` / `GGY(IW,JW,K)=MIN(GGV(IW,JW,K),GGV(IW,JW-1,K))` / `GGZ(IW,JW,K)=MIN(GGV(IW,JW,K),GGV(IW,JW,K-1))` | 일치 | 세 방향 모두 같은 최소값 규칙이다. 경계면 예외는 KS3-313이다. |
| KS3-254 | p.146 향후 확장 플래그를 사용하여 면 투과율 입력 개선 | 현재 파일 읽기는 KS3-249–251 | 문서에만 | 향후 계획이다. 현재 기능으로 기록하지 않는다. H. |
| KS3-255 | p.146 `data.Env` 텍스트; 예 `2`, `'edata-pr' 1 0`, `'edata-ch' 2 1`; 영역명·영역 PE 수·부모 영역; 0이면 부모 없음, −1이면 STOC-IC | `vf_pmginp.f:25–33` `OPEN(MFILEN,ERR=9010,FILE='data.env',`<br>`     &         STATUS='OLD',FORM='FORMATTED' )` / `READ(IENFIL,*,END=9020,ERR=9020) MGARAN` / `DO 120 I=1,MGARAN` / `READ(IENFIL,*,END=9020,ERR=9020) MGNAME(I),MGNPIN(I),MGPARE(I)` | 일치 | 두 영역과 총 세 PE를 지정한다. 첫 줄은 영역 수이며 중첩 깊이가 아니다. |
| KS3-256 | p.146 첫 줄 화살표 `A number of nesting` | `vf_pmginp.f:28` `READ(IENFIL,*,END=9020,ERR=9020) MGARAN`; `:32` `DO 120 I=1,MGARAN` | 불일치 | 실제로는 분석 영역 수이다. 2가 부모·자식 연결 수 또는 중첩 단계 수라는 뜻은 아니다. B. |
| KS3-257 | p.146 영역명+확장자; 병렬 목록·도화는 영역명+PE번호+확장자; 예 `edata-ch000000.list` | `vf_a1main.f:376–379` `WRITE(TEXTP,'(I5.5)') MYRANK` / `OPEN(MFILLP,ERR=9010,`<br>`     &       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.list'//TEXTP,`<br>`     &       STATUS='NEW',FORM='FORMATTED' )`; `vf_og1ini.f:49–52` `WRITE(TEXTP,'(I5.5)') MYRANK` / `OPEN(MFILGR,ERR=9010,`<br>`     &       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.grp'//TEXTP,`<br>`     &       STATUS='NEW',FORM='UNFORMATTED' )` | 불일치 | 코드는 확장자 뒤에 5자리 PE 번호를 붙인다. 예는 `edata-ch.list00000`, `edata-ch.grp00000`이다. 3D2F도 같은 순서와 자리수를 쓴다. 문서의 6자리·확장자 앞 번호 규칙은 전체 Simulators 검색에서 구현을 찾지 못했다. D. 검색어와 결과는 5.2에 적는다. |

### 2.11 p.147–150 (459–462): 그림·사용법·참고문헌

| 행 ID | 문서(위치, 원문) | 코드(파일:줄 원문) | 판정 | 이유 |
|---|---|---|---|---|
| KS3-261 | p.147 Fig.0-5-2 `edata-pr (Region Number 1)` 안에 `edata-ch (Region Number 2)`; 자식 안의 점선은 두 PE | `vf_pmginp.f:33` `READ(IENFIL,*,END=9020,ERR=9020) MGNAME(I),MGNPIN(I),MGPARE(I)`; p.146 예의 부모 0·1 및 PE 수1·2 | 일치 | 두 영역의 포함 관계와 자식 영역의 이분할이 입력 예와 같다. |
| KS3-262 | p.147 Graphic unit의 (1) Command area, (2) Main drawing area, (3) Sub Drawing Area | 코드 대조 대상 아님 | 문서에만 | 외부 도화 도구의 화면 구획 설명이다. H. |
| KS3-263 | p.147 `Control key + mouse drag → enlarge`, `Shift key + mouse drag → move`; 옵션 버튼으로 물리량 전환; Enter로 텍스트 입력 적용 | 코드 대조 대상 아님 | 문서에만 | 외부 도구 조작법이다. H. |
| KS3-264 | p.148 Fig.0-5-3 GUI 이미지의 ①·②·③; Fig.0-5-4 (a)General (b)Velocity (c)Equivalence (d)Numerical value | 코드 대조 대상 아님 | 문서에만 | 그림 쪽이다. 명령·주 도화·보조 도화 및 물리량 선택 화면을 직접 확인했다. H. |
| KS3-265 | p.149 참고문헌 (1) CDIT 2001, *Research and development of numerical wave channel*, CDIT Library(12); (2) Sakakiyama·Abe·Kajima 1990, JSCE37,554–558; (3) Hirt·Nichols 1981, JCP39,201–225; (4) Torrey·Mjolsness·Stein 1987, NASA-VOF3D, LA11009-MS; (5) Isobe·Nishimura·Horikawa 1978, II,760–761 | 코드 대조 대상 아님 | 문서에만 | 서지 5건이다. 이 쪽에는 식·계수·입력 명령이 없다. H. |
| KS3-266 | p.149 참고문헌 (6) Dean1965, J.Geopys.Res.70(18),4561–4572; (7) Iwata·Kawasaki·Kim1994,42,781–785; (8) Cruz et al.1993, *Nonreflecting boundary conditions for non-linear wave equation*; (9) Numerical Fluid Dynamics Editorial Board1995, *Turbulence Analysis*; (10) Shimada·Nakadai·Akiyama1992, *Incompressible fluid analysis module I* | 코드 대조 대상 아님 | 문서에만 | 서지 5건이다. (10)의 권·호·쪽은 다음 쪽으로 이어진다. H. |
| KS3-267 | p.150 (10) 계속 `1, pp.88-99`; (11) Yamazaki1992,3(1),131–146; (12) Takahashi1982, *Computerised Fluid Dynamics (Exercises)*; (13) Roache1978, *Computational Fluid Dynamics*; (14) Gueyffier et al.1999, JCP152,423–456; (15) Fujino1991, II,622–624 | 코드 대조 대상 아님 | 문서에만 | (10)의 계속과 나머지 서지 5건이다. 원문의 `Smoothed Surfase Stress Methods for Tree-Dimensional Flows` 철자는 이 보고서에서 외부 원문과 교정하지 않는다. H. |

대상 50쪽 중 완전한 빈 쪽은 없다. p.101·107·147·148은 도식을 포함한다. p.141은 짧은 정의만 있다. p.149–150은 참고문헌이다. 대상에는 별도 Appendix가 없다.

### 2.12 조건·표기 보충

| 행 ID | 문서(위치, 원문) | 코드(파일:줄 원문) | 판정 | 이유 |
|---|---|---|---|---|
| KS3-271 | p.113 증폭 A<ZERO, ANG 기준점 조건; p.144 참조 위상 감소 | `vf_bwuwn.f:273–275` `TN=T0-TNOW/T` / `TN=TN-DBLE(INT(TN))` / `IF (TN.LT.0.0D0) TN=TN+1.0D0`; `:280–284` `AW=1.0D0` / `IF (A.GE.ZERO) THEN` / `A=TNOW/T/A` / `IF (A.LT.1.0D0) AW=0.5D0*SIN(PI*(A-0.5D0))+0.5D0` / `ENDIF`; `:325–328` `SA=SA*PI/180.0D0` / `SB=SIN(SA)` / `SA=COS(SA)` / `SC=-(SA*SX+SB*SY)` | 일치 | A<ZERO이면 AW=1을 유지한다. ANG를 반시계 방향 삼각함수에 넣는다. 참조 위상은 시간과 함께 감소한다. |
| KS3-272 | p.113 조파 소스의 수위 전용 자료 금지; TYPE1 D·T 필수; p.114 DAMP 차수·폭·수심 필수 | `vf_csetup.f:267–268` `ELSEIF (N.EQ.-3 .AND. MTBTYP.EQ.3) THEN` / `CALL VF_A2ERR('VF_CSETUP','(WAVE-SRC) MTBTYP ERROR.')`; `:134–137` `IF (D.LT.ZERO)`<br>`     &        CALL VF_A2ERR('VF_CSETUP','(OPEN-BC DEPTH) NOT FOUND.')`<br>`          IF (T.LT.ZERO)`<br>`     &        CALL VF_A2ERR('VF_CSETUP','(OPEN-BC PERIOD) NOT FOUND.')`; `:227–232` `IF (N.LT.0)`<br>`     &        CALL VF_A2ERR('VF_CSETUP','(DAMP DEGREE) NOT FOUND.')`<br>`          IF (W.LT.ZERO)`<br>`     &        CALL VF_A2ERR('VF_CSETUP','(DAMP WIDTH) NOT FOUND.')`<br>`          IF (D.LT.ZERO)`<br>`     &        CALL VF_A2ERR('VF_CSETUP','(DAMP DEPTH) NOT FOUND.')` | 일치 | 읽은 뒤 setup에서 필수값을 검사한다. |
| KS3-273 | p.122 조파·개방 경계 우선·난류 벽면 경계 연동·이류 ±A | `vf_csetup.f:147–150` `IF     (IBCTYP(1,JD).EQ.1) THEN` / `IB=5` / `ELSEIF (IBCTYP(1,JD).EQ.2) THEN` / `IB=7`; `:204,209` `INDB(3,L)=IB` / `INDB(4,L)=IB`; `:239–248` VP 코드6·8에 따라 INDBK·INDBE도6·8 대입; `vf_sconvd.f:86–87` `ELSEIF (INDBC(IND).GE.1) THEN` / `FLC=WIN*BCC(IND)` | 일치 | 특수 경계를 나중에 덮어쓴다. 양수 스칼라 경계에서만 경계값 이류 분기에 들어간다. |
| KS3-274 | p.122–123 obs 초기 저장·재시작 읽기; p.126 경과시간 종료 출력 | `vf_ii1inp.f:442–446` `WRITE(TEXTP,'(I5.5)') MYRANK` / `OPEN(MFILOR,FORM='UNFORMATTED',STATUS='UNKNOWN',ERR=9040,`<br>`     &         FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.obs'//TEXTP)` / `WRITE(MFILOR) NF`; `:466` `READ(MFILOR,ERR=9050) NF`; `vf_a1main.f:1152–1155` `IRSTYP=1` / `IRSTRN(1)=NNOW` / `IRSTRN(2)=NNOW` / `IRSTRN(3)=1`; `:1166` `WRITE(MFILAR,'(I10,1X,F10.2)') NNOW,TNOW`; `vf_or1trn.f:105` `WRITE(IRSFIL,ERR=9010) NNOW,TNOW,DTNOW` | 일치 | 지형 파일에도 5자리 PE 번호를 뒤에 붙인다. 시간 초과 때 현재 단계를 재시작 대상으로 기록한다. |
| KS3-275 | p.128 와도 세 식·병렬 MIN/MAX 제한 | `vf_cvort.f:109,152,195` `VORT=YY(4,J0)*(WYP-WYM)-ZZ(4,K0)*(VZP-VZM)` / `VORT=ZZ(4,K0)*(UZP-UZM)-XX(4,I0)*(WXP-WXM)` / `VORT=XX(4,I0)*(VXP-VXM)-YY(4,J0)*(UYP-UYM)`; `vf_careap.f:200–203` `W= 1.0D+30` / `CALL VF_P1MIND(W,VMIN)` / `W=-1.0D+30` / `CALL VF_P1MAXD(W,VMAX)` | 일치 | 차분의 축·부호가 문서의 회전과 같다. 지역에 유효 셀이 없는 프로세스가 극값 축약에 넣는 기본값이 문서 제한값이다. |
| KS3-276 | p.128 AV `Volume average value`, INT `volume integrated value` | `vf_careap.f:175–180`의 유효 셀 처리 중 `AR  =XX(2,I)*YY(2,J)*ZZ(2,K)*GGV(I,J,K)*FF(I,J,K)` / `VAV =VAV +AR` / `VINT=VINT+AR*VAL(I,J,K)`; `:198` `IF (VAV.GT.0.0D0) VAV=VINT/VAV` | 불일치 | 일반 스칼라는 공극률과 F를 포함한 물 체적으로 가중한다. 문서는 어느 체적인지 적지 않는다. F 자체의 별도 경로와 함께 KS3-310에서 적는다. C. |
| KS3-277 | p.101 INDC 반복 예의 `DO 120 K=2,NUMK-1` 뒤에 `100 CONTINUE`, `110 CONTINUE`만 인쇄 | `vf_cindc.f:51–53` `100      CONTINUE` / `110    CONTINUE` / `120  CONTINUE` | 불일치 | 도식의 예제는 120 종료 행을 빠뜨린다. 완전한 Fortran 루틴으로 복사할 수 없다. B. |
| KS3-278 | p.124 VISC `sum of molecular dynamic viscosity and vortical viscosity coefficient` | `vf_ol1trn.f:172–173` `WRITE(ILPFIL,9510) 'VISC',NNOW,TNOW` / `CALL VF_OL3DR(ANU,0)`; `vf_a1main.f:64` ANU의 선언 주석은 보충 원문 | 불일치 | ANU는 분자·와 동점성계수의 합이다. dynamic viscosity가 아니라 kinematic viscosity이다. B. |
| KS3-279 | p.137 개방 경계 VELOCITY의 `[-]` 표기 | `vf_csetup.f:143` `BCTYP(6,JD)=WLN/T`; `VF_APHYSR.h:73` `CD                             (6,*):波速`; `vf_ol1ini.f:247` `WRITE(ILPFIL,9540) '  VELOCITY   [-]=',BCTYP(6,JD)` | 불일치 | 일본어 뜻은 “파속”이다. 코드의 출력 단위도 틀렸다. 단위 및 자기 주석·계산식과 모순인 출력 라벨 E 후보이다. KS3-227은 같은 발견의 문서 측 행이다. |
| KS3-280 | p.131 `Pressure value output by L / P output etc is subtracted from atmospheric pressure` | `vf_fpvcpp.f:191` `PVCPES(L)=(PAV+PVCP0)/(1.0D0+PVCGM*DTNOW*PVCDIV(L))-PVCP0`; `A11111.in:776` `注）L/P出力等で出力される圧力値は大気圧分が差し引かれている` | 불일치 | 영어 문장을 그대로 읽으면 대기압에서 출력 압력을 뺀다. 일본어 뜻은 “L/P 등으로 출력하는 압력값에는 대기압분을 빼 놓았다”이다. 코드는 절대압에서 PVCP0를 뺀다. 영어의 차감 방향은 B이다. |
| KS3-281 | p.143 `5.5. Calculation information file`; p.144 `5.5. Matrix data file` | 코드 대조 대상 아님. p.143 표준출력은 KS3-238이고 p.144 파일은 KS3-241이다. | 불일치 | 서로 다른 연속 절에 같은 번호를 인쇄했다. 문서 내부 편집 오기 B이다. 파일 확장자와 자료형 판정에는 영향을 주지 않는다. |
| KS3-282 | p.113 `Water level / flow rate: depth and period are essential`; p.144 표제 `Water level and flow rate are given`, `When only flow rate is given` | `vf_im1inp.f:22` `CD    DMTBUN(MTBZZ,MTBTT) : OUT : R*8 : マトリクスデータの水平方向流速`; `A11111.in:184` `水位／流速：水深と周期が必須` | 불일치 | 일본어 뜻은 각각 “매트릭스 자료의 수평 방향 속도”와 “수위/속도: 수심과 주기가 필수”이다. 표의 u·w는 속도이다. flow rate는 flow velocity의 번역 오기 B이다. 필수값 조건 자체는 KS3-067과 일치한다. |
| KS3-283 | p.148 GUI의 `ファイル制御`, `断面制御`, `物理量制御`, `画面制御`, `解析`; `各種`, `流速`, `等値`, `数値`; `自由表面`, `計算格子`, `透過構造`, `圧力`, `格子番号`, `セル番号`, `横方向流速`, `縦方向流速` | 코드 대조 대상 아님 | 문서에만 | 일본어 뜻은 파일·단면·물리량·화면 제어, 해석, 여러 종류·속도·등치·수치, 자유수면·계산격자·투과구조·압력·격자번호·셀번호·가로속도·세로속도이다. 나머지 스크롤·시간 이동·비트맵 출력·최솟값/최댓값·분할 수·배율·표시 토글과 그림 안 숫자는 외부 도화 도구 화면의 사례이다. H. 도구 내부를 판독하지 않았다. |
| KS3-284 | p.123 `If reading from the ars file can not be performed, initial calculation is performed instead of restart calculation` | `vf_ii1inp.f:343–351` `IRETYP=-1` / `OPEN(MFILAR,ERR=310,`<br>`     &               FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.ars',`<br>`     &               STATUS='OLD',FORM='FORMATTED'  )`<br>`                  READ(MFILAR,*,ERR=310) II,TT`<br>`                  CLOSE(MFILAR)`<br>`CCC                  IF( II.GE.0 ) IRETYP=II`<br>`                  IRETYP=II`<br>`  310             CONTINUE` | 불일치 | OPEN 오류와 READ의 ERR 분기는 최초 계산으로 돌아간다. READ에는 `END=310`이 없다. EOF까지 같은 복귀를 보장한다는 설명에는 예외가 필요하다. C. 빈 ars 파일을 실행하여 시험하지 않았다. |

### 2.13 쪽별 확인표

아래 50개 행은 `cad-3d-manual-101.png`부터 `cad-3d-manual-150.png`까지 직접 연 쪽 이미지의 색인이다. 쪽 이미지의 공통 디렉터리는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/`이다. 각 PDF 쪽의 인쇄 쪽 번호는 PDF 쪽 번호에 312를 더한 값이다. 본문 행에서 `p.N`은 모두 `3D manual p.N`의 약칭이다.

| PDF 쪽 | 인쇄 쪽 | 확인 항목 | 대조 행 |
|---|---|---|---|
| p.101 | 413 | INDC·INDS 도식과 반복문 | KS3-001–003, 277, 301 |
| p.102 | 414 | Chapter 5 시작, 동적 할당, 상수 상한 | KS3-004–006 |
| p.103 | 415 | 나머지 상수 상한 | KS3-007–008 |
| p.104 | 416 | 입력 파일 설명, 주석·병렬·시간·물성·조파 예제 | KS3-009–014 |
| p.105 | 417 | 조파·감쇠·개방·수치·격자 예제 | KS3-014–018 |
| p.106 | 418 | 격자 끝, 경계·출력·시간문 예제 | KS3-018–022, 235 |
| p.107 | 419 | 문법, Fig.0-5-1 첨자·격자 위치 | KS3-023–026, 316–317 |
| p.108 | 420 | 병렬·방정식 제어 | KS3-027–029, 302 |
| p.109 | 421 | 시간 제어, 물성 명령 시작 | KS3-030–035, 303 |
| p.110 | 422 | 물성·초기값·온도·농도 명령 | KS3-035–044, 047–048 |
| p.111 | 423 | 물성 표 끝, 부력 식, 조파 명령 | KS3-043–050, 055–066 |
| p.112 | 424 | 조파 인수·종류·범위 | KS3-055–066, 318 |
| p.113 | 425 | 조파 필수값·각도, 개방 경계 | KS3-063, 067–070, 271–272, 282, 308 |
| p.114 | 426 | 감쇠·난류 명령과 표 시작 | KS3-072–082, 272 |
| p.115 | 427 | 난류 상수 표, 수치 명령 | KS3-078–095 |
| p.116 | 428 | 수치 표·기본값, 격자 명령 | KS3-091–099 |
| p.117 | 429 | 격자 절차, 외부·직사각형 장애물 | KS3-099–103, 317 |
| p.118 | 430 | 외부 공극률·하한·셀·면·관성 입력 | KS3-104–110, 319 |
| p.119 | 431 | 저항·공극률 표·합성식, 경계 명령 시작 | KS3-105–113, 122, 319 |
| p.120 | 432 | 경계 첨자 표·속도/압력 종류 | KS3-122–125 |
| p.121 | 433 | VOF·난류·온도·농도 경계 종류 | KS3-125–130 |
| p.122 | 434 | 경계 인수·우선순위·이류, OBS | KS3-127–134, 141–142, 273–274 |
| p.123 | 435 | 외부 지형 읽기, 재시작, 목록 출력 | KS3-142–149, 274, 284, 304, 306 |
| p.124 | 436 | 목록 단면·물리량 21개·미출력 기본 | KS3-148–152, 278 |
| p.125 | 437 | 목록 전체 단면·기본, 도화 제어 | KS3-150, 153, 155–159 |
| p.126 | 438 | 도화 제한, 상세·시계열 출력 | KS3-158–168, 305 |
| p.127 | 439 | 시계열 POINT·와도·영역·좌표·DIR | KS3-165–172 |
| p.128 | 440 | FORCE·PHY·CALC·LC·와도 식·병렬 한계 | KS3-168–174, 275–276, 310, 315 |
| p.129 | 441 | PORO·MAM 제어, 기포 시간문 시작 | KS3-181–182, 192, 320 |
| p.130 | 442 | 시간문·표면 속도·하위 반복·공기압 | KS3-192–196, 307 |
| p.131 | 443 | 공기압·Dupuit-Forheimer 표·조건 | KS3-196–205, 280, 309 |
| p.132 | 444 | 수위 변동·단층·좌표계 | KS3-206–209 |
| p.133 | 445 | 측지계·최대 속도·DEBUG 제목 | KS3-209–212, 215 |
| p.134 | 446 | DEBUG 두 상자·인수 표 | KS3-215–216 |
| p.135 | 447 | DEBUG 속도 표, 목록 파일·머리글 | KS3-216, 221–223 |
| p.136 | 448 | 입력 단계·분할·방정식·시간 출력 | KS3-223–224 |
| p.137 | 449 | 물성·파형·개방·감쇠·수치 출력 | KS3-225–227, 279 |
| p.138 | 450 | 수치·파일·옵션·격자 출력 | KS3-228–229 |
| p.139 | 451 | 초기화·단계·도화·CPU 표 시작 | KS3-222, 230–231 |
| p.140 | 452 | CPU 표 끝·정상 종료·진단량 정의 | KS3-222, 231–234 |
| p.141 | 453 | ITR 정의 한 문장 | KS3-232 |
| p.142 | 454 | 시계열 파일·항목·계산값 예제 | KS3-235–237 |
| p.143 | 455 | 표준출력 단계 예제 | KS3-237–238, 281 |
| p.144 | 456 | 매트릭스 세 형식·변수·보간·예제 | KS3-241–247, 271, 281–282, 311, 318 |
| p.145 | 457 | 공극률 블록 도식·레코드·자료형 | KS3-248–251, 312 |
| p.146 | 458 | 공극률·면 보간, 환경 파일·이름 규칙 | KS3-252–257, 313–314 |
| p.147 | 459 | 영역 도식, 도화 도구 설명 | KS3-261–263 |
| p.148 | 460 | 도화 도구 GUI 그림 두 개 | KS3-264, 283 |
| p.149 | 461 | Chapter 6 참고문헌 (1)–(10) | KS3-265–266 |
| p.150 | 462 | 참고문헌 (10) 계속·(11)–(15) | KS3-267 |

### 2.14 원문 증거

아래에는 표의 축약된 문자열 인용을 보완하는 원문 줄을 둔다. 행 번호는 `nl -ba`와 같다. 조건·식의 고정형식 연속 줄은 모두 포함한다. 표의 해석은 이 원문에 근거한다.

일본어 인라인 주석의 뜻은 다음과 같다. `mod_fault.f:58–59`는 계산 격자와 단층 매개변수의 측지계 번호이다. `vf_ii1inp.f:146,158`의 `1回目のEOFでファイルを切り替え`는 첫 EOF에서 파일 전환이라는 뜻이다. `:149,161`의 `2回目のEOFでループ抜け`는 두 번째 EOF에서 반복 종료라는 뜻이다.

#### 3D A11111.in

```text
    2  CADMAS-SURF/3Dの入力ファイル(テキスト)のフォーマット
    3  ======================================================================
   19    PARALLEL X  [IC]
   20    PARALLEL Y  [JC]
   53    TIME CONST [DTCNST]
   54    TIME AUTO  [DTINIT] [DTSAFE]
   55    TIME LIMIT [DTMIN]  [DTMAX]
   56    TIME END   [NEND]   [TEND]
   78    MATE W-LEVEL   [WVLVL]
   79    MATE DENSITY   [RHO0]
   80    MATE K-VISC    [ANU0]
   81    MATE GRAVITY   [GRZ0]
   82    MATE I.C.    V [UINI] [VINI] [WINI]
   85    MATE I.C.    KE [AKINI]  [AEINI]
   88    MATE S-HEAT    [CP]
   89    MATE T-COND    [TC]
   90    MATE T-DENS    [T0]  [DRDT]
   91    MATE I.C.    T [TINI]
   94    MATE DIFFUS    [LC]  [DF]
   95    MATE C-DENS    [LC]  [C0]  [DRDC]
   96    MATE I.C.    C [LC]  [CINI]
  113      LC       濃度の成分番号                R*8    -           1=<LS=<NS
  128    MODEL WAVE-BC  {DIR}  FUNC    STREAM  [N]
  129    MODEL WAVE-BC  {DIR}  FUNC    {TYPE}
  130    MODEL WAVE-BC  {DIR}  DEPTH      [D]
  131    MODEL WAVE-BC  {DIR}  HEIGHT     [H]
  132    MODEL WAVE-BC  {DIR}  PERIOD     [T]
  133    MODEL WAVE-BC  {DIR}  AMPL       [A]
  134    MODEL WAVE-BC  {DIR}  AREA   [LC1]  [LC2]
  135    MODEL WAVE-BC  {DIR}  ANGLE  [ANG]   [X0]   [Y0]
  136    MODEL WAVE-SRC {DIR2}           [LC]
  137    MODEL WAVE-SRC        FUNC    STREAM  [N]
  138    MODEL WAVE-SRC        FUNC    {TYPE}
  139    MODEL WAVE-SRC        DEPTH      [D]
  140    MODEL WAVE-SRC        HEIGHT     [H]
  141    MODEL WAVE-SRC        PERIOD     [T]
  142    MODEL WAVE-SRC        AMPL       [A]
  184             水位／流速：水深と周期が必須
  195    MODEL OPEN-BC {DIR} FUNC    {TYPE}
  196    MODEL OPEN-BC {DIR} DEPTH      [D]
  197    MODEL OPEN-BC {DIR} PERIOD     [T]
  214    MODEL DAMP {DIR} DEGREE   [N]
  215    MODEL DAMP {DIR} PARAM-XY [PXY]
  216    MODEL DAMP {DIR} PARAM-Z  [PZ]
  217    MODEL DAMP {DIR} WIDTH    [W]
  218    MODEL DAMP {DIR} DEPTH    [D]
  265    COMP SCHM VP-DONOR     [SCMVP]
  266    COMP SCHM FF-DN-AC
  267    COMP SCHM FF-SLOPE
  268    COMP SCHM KE-DONOR     [SCMK]
  269    COMP SCHM T-DONOR      [SCMT]
  270    COMP SCHM C-DONOR [LC] [SCMC]
  271    COMP MTRX ILUBCGSTAB
  272    COMP MTRX M-ILUBCGSTAB [CGPARA]
  273    COMP MTRX MAX-ITR      [ICGMAX]
  274    COMP MTRX A-ERROR      [CGEPSA]
  275    COMP MTRX R-ERROR      [CGEPSR]
  410    B.C. D                                     {BC}
  411    B.C. X [IG1] [JC1] [KC1] [IG2] [JC2] [KC2] {BC}
  412    B.C. Y [IC1] [JG1] [KC1] [IC2] [JG2] [KC2] {BC}
  413    B.C. Z [IC1] [JC1] [KG1] [IC2] [JC2] [KG2] {BC}
  515    FILE RES [ISTEP]
  516    FILE RES AUTO
  583    FILE GRP STEP [ISTR] [IEND] [ISTEP]
  584    FILE GRP TIME [TSTR] [TEND] [TSTEP]
  585    FILE GRP AREA [IC1] [JC1] [KC1] [IC2] [JC2] [KC]
  586    FILE GRP ON   VORT   
  587    FILE GRP OFF  VORT 
  713    FILE MAM STEP [ISTR] [IEND] [ISTEP]
  714    FILE MAM TIME [TSTR] [TEND] [TSTEP]
  726  ======================================================================
  728  ======================================================================
  732    OPTION T-DOOR BUB  OFF
  736    OPTION T-DOOR BUB [WBUB]
  776      注）L/P出力等で出力される圧力値は大気圧分が差し引かれている
  777          造波、放射、フリーに接する気泡は大気圧とする
  804         * 動粘性係数は「MATE K-VISC」とは別に入力する
```

#### 3D VF_A0PRM.h

```text
    2        PARAMETER (IVR001=  0, IVR002=  1,
    3       &           MAXPRO= 1000,
    4  C----------------------------------------------------------2011.04 start
    5  C    &           MAXNPI= 100, MAXNPJ= 100, MAXBUF=  8,
    6       &           MAXNPI= 100, MAXNPJ= 100, MAXBUF=  9*2*4,
    7       &           MAXLIN= 50,
    8  C----------------------------------------------------------2011.04 end
    9       &           MFILEN= 10,
   10       &           MFILIN= 11, MFILMT= 12, MFILRE= 13, MFILPR= 14,
   11       &           MFILMT2=15,
   12       &           MFILLP= 21, MFILGR= 22, MFILRS= 23, MFILTR= 24,
   13       &           MFILMM= 25,
   14       &           MFILBT= 26,MFILBT2= 27, MFILOB= 28, MFILPS= 29,
   15       &           MFILAR= 30, MFILOR= 31,
   16       &           MAXCHR=256, MAXWDS=128, MAXG1 =  6, MAXB1 =  4,
   17       &           MAXNC = 10,
   18       &           MAXTR =10000, MAXTR1=  8,
   19       &           MAXPRB= 10, MAXPVC=500,
   20       &           MAXDRG= 10,
   21       &           INMODE=  0,
   22       &           ZERO  =1.0D-20,ZEROG = 1.0D-6,
   23       &           PI    =3.141592653589794D0)
```

#### 3D VF_AFILEI.h

```text
    2        COMMON /VF_AFILEI/ IENFIL,IINFIL,IMTFIL,IMTFIL2,IREFIL,IPRFIL,
    3       &                   ILPFIL,IGRFIL,IRSFIL,ITRFIL,IMMFIL,
    4       &                   ILPTYP,ILPTRN(3),ILPARA(3),ILPON(21),
    5       &                   IGRTYP,IGRTRN(3),IGRARA(6),IGRVOR,
    6       &                   IRSTYP,IRSTRN(3),IRETYP,
    7       &                   ITRTYP,ITRTRN(3),ITRNUM,ITRPRM(MAXTR1,MAXTR),
    8       &                   IMMTYP,IMMTRN(3),
    9       &                   IPRNT,IPRNB,IPRNP,IPRARA(6,MAXPRB),IPRIT,
   10       &                   MTBTYP ,MTBTT ,MTBZZ ,MTBNOW ,
   11       &                   MTBTYP2,MTBTT2,MTBZZ2,MTBNOW2
   44  CD    ILPON(21) : CNS : I*4 : リストファイルへの出力/非出力
```

#### 3D VF_ASEABT.h

```text
    3        COMMON/VF_ASEABI/ISEABT
```

#### 3D mod_fault.f

```text
   58        INTEGER:: ISYSTEM=2 ! 計算メッシュの測地系の番号(1-3)
   59        INTEGER:: JSYSTEM=2 ! 断層パラメータの測地系の番号(1-3)
  209        REAL(8),INTENT(IN):: LC_DEG
  213        ORI_L(0) = LC_DEG*D2R
```

#### 3D vf_a1main.f

```text
  236        DOUBLE PRECISION, DIMENSION(:,:,:), ALLOCATABLE :: GLV,GLX,GLY,GLZ
  372          OPEN(MFILLP,ERR=9010,
  373       &       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.list',
  374       &       STATUS='NEW',FORM='FORMATTED'    )
  376          WRITE(TEXTP,'(I5.5)') MYRANK
  377          OPEN(MFILLP,ERR=9010,
  378       &       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.list'//TEXTP,
  379       &       STATUS='NEW',FORM='FORMATTED'    )
  390        CALL VF_A2DFLT()
  412        ALLOCATE(XX  (MAXG1,NUMI)    ,STAT=IERR)
  413        ALLOCATE(YY  (MAXG1,NUMJ)    ,STAT=IERR)
  414        ALLOCATE(ZZ  (MAXG1,NUMK)    ,STAT=IERR)
  415        ALLOCATE(UU  (NUMI,NUMJ,NUMK),STAT=IERR)
  501        CALL VF_ZSETR3(CM0 ,0.0D0,NUMI,NUMJ,NUMK)
  502        CALL VF_ZSETR3(CD0 ,0.0D0,NUMI,NUMJ,NUMK)
  503        CALL VF_ZSETR3(GGV ,1.0D0,NUMI,NUMJ,NUMK)
  504        CALL VF_ZSETR3(GGX ,1.0D0,NUMI,NUMJ,NUMK)
  505        CALL VF_ZSETR3(GGY ,1.0D0,NUMI,NUMJ,NUMK)
  506        CALL VF_ZSETR3(GGZ ,1.0D0,NUMI,NUMJ,NUMK)
  756          CALL VF_IM2INP(DMTBTT2,DMTBZZ2,DMTBHH2,DMTBUN2,DMTBUT2)
  778          CALL VF_IM2INP(DMTBTT2,DMTBZZ2,DMTBHH2,DMTBUN2,DMTBUT2)
  790        CALL VF_OL1INI(XX,YY,ZZ,
  791       &               CM0,CD0,GGV,GGX,GGY,GGZ,GLV,GLX,GLY,GLZ,
  792       &               BCU,BCV,BCW,BCP,BCF,BCK,BCE,BCT,BCTI,BCC,BCCI,
  793       &               NF,INDX,INDY,INDZ,INDB,INDBK,INDBE,INDBT,INDBC)
  955          IF (MGRANK.EQ.0) WRITE(*,9530) NNOW,TNOW,DTNOW
  956          WRITE(ILPFIL,9540) NNOW,TNOW,DTNOW,FSUM,FCUT,DV
  957          IF (PVCP0.LT.ZERO) THEN
  958            WRITE(ILPFIL,9550) CGBNRM,CGXNRM,ICGITR
  962          CALL VF_OL1TRN(DT ,
  963       &                 UU ,VV ,WW ,PP ,FF ,ANU,
  964       &                 GGV,GGX,GGY,GGZ,GLV,GLX,GLY,GLZ,
  965       &                 BCU,BCV,BCW,BCP,BCF,
  966       &                 ANUT,AK,AE,BCK,BCE,
  967       &                 TT,ALM,BCT,BCTI,CC,DD,BCC,BCCI,PPPVC,
  968       &                 NF ,INDB,INDBK,INDBE,INDBT,INDBC,IPVC)
 1000          CALL VF_P0TIME(WTM2)
 1001          IEND1(2)=0
 1002          IF(WTM2-WTM1.GT.ETIME) IEND1(2)=1
 1003          CALL MPI_ALLREDUCE(IEND1,IEND,2,MPI_INTEGER,MPI_MAX,
 1004       $                     comm_mlicdsmg2fc,IERR)
 1005          IE = IEND(1)
 1006          IEE= IEND(2)
 1007          IF (IE.EQ.1 .OR. IEE.EQ.1) GOTO 1000
 1029          DTNOW=DT/DBLE(LOOPS)
 1149        IF ( IE.EQ.1.AND.ETIME.LT.1.0D30 ) IEE=1
 1150        IF ( IEE.EQ.1 ) THEN
 1151          WRITE(ILPFIL,*) 'ETIME=',WTM2-WTM1
 1152          IRSTYP=1
 1153          IRSTRN(1)=NNOW
 1154          IRSTRN(2)=NNOW
 1155          IRSTRN(3)=1
 1156          IF (MYRANK.EQ.0) THEN
 1157            OPEN(MFILAR,
 1158       &         FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.ars',
 1159       &         STATUS='UNKNOWN',FORM='FORMATTED'  )
 1160            IF (IE.EQ.1)THEN
 1161              WRITE(MFILAR,'(I10,1X,F10.2)') -999,TNOW
 1162              CLOSE(MFILAR)
 1163              OPEN(IFLAR,FILE='stop_ars',STATUS='UNKNOWN')
 1164              CLOSE(IFLAR)
 1165            ELSE
 1166              WRITE(MFILAR,'(I10,1X,F10.2)') NNOW,TNOW
 1167              CLOSE(MFILAR)
 1168            ENDIF
 1169          ENDIF
 1170          CALL VF_OR1TRN(DT,UU,VV,WW,PP,FF,GGV,BCU,BCV,BCW,BCP,BCF,
 1171       &                 AK,AE,BCK,BCE,TT,BCT,CC,BCC,
 1172       &                 TBUB,DROPTX,DROPTY,DROPTZ,
 1173       &                 DROPUU,DROPVV,DROPWW,
 1174       &                 FFLXX,FFLXY,DELH,
 1175       &                 NF)
 1176        ENDIF
 1208   9510 FORMAT(/' ',
 1209       &       '##### CADMAS-SURF/3D-MG Ver.',I1,'.',I1,' START. ######')
 1214   9540 FORMAT( ' ','STEP='    ,I6,
 1215       &            ' : TIME= ',1PE12.5,
 1216       &            ' : DT  = ',1PE12.5,
 1217       &            ' : FSUM= ',1PE12.5,
 1218       &            ' : FCUT= ',1PE12.5,
 1219       &            ' : !VD!= ',1PE12.5 )
 1220   9550 FORMAT( ' ',11X,
 1221       &            ' : !B! = ',1PE12.5,
 1222       &            ' : !R! = ',1PE12.5,
 1223       &            ' : ITR = ',I6      )
```

#### 3D vf_a2cput.f

```text
   93   9510 FORMAT(/' ','##### CPU TIME [S] ##########################')
   94   9520 FORMAT(/' ','##  <<FLOW>>')
   95   9530 FORMAT( ' ','##  TOTAL                      ',F11.2)
   96   9540 FORMAT( ' ','##  +-- PRE PROCESS            ',F11.2)
```


#### 3D vf_a2dflt.f

```text
   37        ICGTYP=1
   38        ICGMAX=500
   39        ICGITR=0
   40        ISCMVP=0
   41        ISCMFF=0
   42        ISCMK =0
   43        ISCMT =0
   44        CALL VF_ZSETI1(ISCMC,0,MAXNC)
   45        IBSUW0=0
   48        CGPARA=0.95D0
   49        CGEPSA=1.0D-15
   50        CGEPSR=1.0D-12
   51        CGDIV =1.0D+30
   52        CGBNRM=0.0D0
   53        CGXNRM=0.0D0
   54        FEPS  =1.0D-6
   55        FLOWER=FEPS
   56        FUPPER=1.0D0-FEPS
   57        FSUM  =0.0D0
   58        FCUT  =0.0D0
   59        PLOWER=1.0D-4
   60        SCMVP =1.0D0
   61        SCMK  =1.0D0
   62        SCMT  =1.0D0
   63        CALL VF_ZSETR1(SCMC,1.0D0,MAXNC)
   69        CALL VF_ZSETI1(IDBGF ,0,6)
   70        CALL VF_ZSETI1(IDBGTD,0,6)
   73        RDBGF=0.0D0
   74        CALL VF_ZSETR1(RDBGTD,0.0D0,3)
   78        IENFIL=IENFIL
   79        IINFIL=0
   80        IMTFIL=0
   81        IMTFIL2=0
   82        IREFIL=0
   83        IPRFIL=0
   84        ILPFIL=ILPFIL
   85        IGRFIL=0
   86        IRSFIL=0
   87        ITRFIL=0
   88        IMMFIL=0
   89        ILPTYP=0
   90        CALL VF_ZSETI1(ILPTRN,0,3)
   91        CALL VF_ZSETI1(ILPARA,1,3)
   92        CALL VF_ZSETI1(ILPON ,0,19)
   93        IGRTYP=0
   94        CALL VF_ZSETI1(IGRTRN,0,3)
   95        CALL VF_ZSETI1(IGRARA,1,6)
   96        IGRVOR=0
   97        IRSTYP=0
   98        CALL VF_ZSETI1(IRSTRN,0,3)
   99        IRETYP=-1
  100        ITRTYP=0
  101        CALL VF_ZSETI1(ITRTRN,0,3)
  102        ITRNUM=0
  103        CALL VF_ZSETI2(ITRPRM,0,MAXTR1,MAXTR)
  104        IMMTYP=0
  105        CALL VF_ZSETI1(IMMTRN,0,3)
  106        IPRNT=0
  107        IPRNB=0
  108        IPRNP=0
  109        CALL VF_ZSETI2(IPRARA,0,6,MAXPRB)
  121        CALL VF_ZSETR1(RLPTRN,0.0D0,4)
  122        CALL VF_ZSETR1(RGRTRN,0.0D0,4)
  123        CALL VF_ZSETR1(RRSTRN,0.0D0,4)
  124        CALL VF_ZSETR1(RTRTRN,0.0D0,4)
  125        CALL VF_ZSETR1(RTRVAL,0.0D0,MAXTR)
  126        CALL VF_ZSETR1(RMMTRN,0.0D0,4)
  127        PRTOLD=0.0D0
  128        PRTNOW=0.0D0
  129        DMTBT0=0.0D0
  130        DMTBT02=0.0D0
  131        ETIME=1.0D30
  134        NUMI =0
  135        NUMJ =0
  136        NUMK =0
  137        NUMB =0
  138        NUMS =0
  139        LEQK =0
  140        LEQT =0
  141        LEQC =0
  149        CALL VF_ZSETI2(IBCTYP, 0,4,4)
  150        CALL VF_ZSETI1(IDAMP ,-1,4)
  151        IDROP=1
  152        CALL VF_ZSETI1(ISCTYP, 0,2)
  153        NPVCB=0
  154        CALL VF_ZSETI1(IPVCBC, 0,MAXPVC)
  155        IDRGN=0
  158        UINI  =0.0D0
  159        VINI  =0.0D0
  160        WINI  =0.0D0
  161        RHO0  =1.0D+3
  162        ANU0  =1.0D-6
  163        GRZ0  =9.8D0
  164        WVLVL =0.0D0
  165        AKMINK=ZERO
  166        AKMINE=ZERO
  167        AKINIK=ZERO
  168        AKINIE=ZERO
  169        AKCMU =0.09D0
  170        AKSGK =1.0D0
  171        AKSGE =1.3D0
  172        AKC1  =1.44D0
  173        AKC2  =1.92D0
  174        AKC3  =0.0D0
  175        AKK0  =0.4D0
  176        AKA0  =5.5D0
  177        AKPR  =1.0D0
  178        CALL VF_ZSETR1(AKSM,1.0D0,MAXNC)
  179        TINI =2.73D+2
  180        TCP0 =4.2D+3
  181        TCN0 =5.7D-1
  182        TDT0 =2.73D+2
  183        TDR0 =1.5D-1
  184        CALL VF_ZSETR1(CINI,0.0D0,MAXNC)
  185        CALL VF_ZSETR1(CDF0,0.0D0,MAXNC)
  186        CALL VF_ZSETR1(CDC0,0.0D0,MAXNC)
  187        CALL VF_ZSETR1(CDR0,0.0D0,MAXNC)
  188        CALL VF_ZSETR2(BCTYP,0.0D0,11,4)
  189        DAMP(1,1)=0.6D0
  190        DAMP(2,1)=0.6D0
  191        DAMP(3,1)=0.0D0
  192        DAMP(4,1)=0.0D0
  193        DAMP(1,2)=0.6D0
  194        DAMP(2,2)=0.6D0
  195        DAMP(3,2)=0.0D0
  196        DAMP(4,2)=0.0D0
  197        DAMP(1,3)=0.6D0
  198        DAMP(2,3)=0.6D0
  199        DAMP(3,3)=0.0D0
  200        DAMP(4,3)=0.0D0
  201        DAMP(1,4)=0.6D0
  202        DAMP(2,4)=0.6D0
  203        DAMP(3,4)=0.0D0
  204        DAMP(4,4)=0.0D0
  205        WBUB =0.2D0
  206        CALL VF_ZSETR1(SCTYP,0.0D0,8)
  207        PVCP0=0.0D0
  208        PVCGM=0.0D0
  209        CALL VF_ZSETR1(PVCDIV,0.0D0,MAXPVC)
  210        CALL VF_ZSETR1(PVCPES,0.0D0,MAXPVC)
  211        CALL VF_ZSETR1(PVCPFS,0.0D0,MAXPVC)
  212        CALL VF_ZSETR1(PVCVES,0.0D0,MAXPVC)
  213        CALL VF_ZSETR1(PVCVFS,0.0D0,MAXPVC)
  214        DRGYU=0.0D0
  215        CALL VF_ZSETR1(DRGDR,0.0D0,MAXDRG)
  216        CALL VF_ZSETR1(DRGAP,0.0D0,MAXDRG)
  217        CALL VF_ZSETR1(DRGBT,0.0D0,MAXDRG)
  218        VVMAX=30.0D0
  221        NEND  =0
  222        NNOW  =0
  223        IDTTYP=1
  224        LOOPS =1
  227        TEND  =0.0D0
  228        TNOW  =0.0D0
  229        DTNOW =0.0D0
  230        DTCNST=1.0D-3
  231        DTINIT=1.0D-6
  232        DTMIN =ZERO
  233        DTMAX =1.0D0/ZERO
  234        DTSAFE=1.0D-1
  237        ISEABT = 0
```

#### 3D vf_bwuwn.f

```text
  273            TN=T0-TNOW/T
  274            TN=TN-DBLE(INT(TN))
  275            IF (TN.LT.0.0D0) TN=TN+1.0D0
```

#### 3D vf_careap.f

```text
  143        ELSEIF (ISW.EQ.5) THEN
  144          DO 420 K=K1,K2
  145            DO 410 J=J1,J2
  146              DO 400 I=I1,I2
  147                IF (NF(I,J,K).NE.-1) THEN
  148                  IP=IP+1
  149                  IF (IP.EQ.1) THEN
  150                    VMIN=FF(I,J,K)
  151                    VMAX=FF(I,J,K)
  152                  ELSE
  153                    VMIN=MIN(VMIN,FF(I,J,K))
  154                    VMAX=MAX(VMAX,FF(I,J,K))
  155                  ENDIF
  156                  AR  =XX(2,I)*YY(2,J)*ZZ(2,K)*GGV(I,J,K)
  157                  VAV =VAV +AR
  158                  VINT=VINT+AR*FF(I,J,K)
  159                ENDIF
  160   400        CONTINUE
  161   410      CONTINUE
  162   420    CONTINUE
  165        ELSE
  166          DO 520 K=K1,K2
  167            DO 510 J=J1,J2
  168              DO 500 I=I1,I2
  169                IF (NF(I,J,K).NE.-1 .AND. NF(I,J,K).NE.8) THEN
  170                  IP=IP+1
  171                  IF (IP.EQ.1) THEN
  172                    VMIN=VAL(I,J,K)
  173                    VMAX=VAL(I,J,K)
  174                  ELSE
  175                    VMIN=MIN(VMIN,VAL(I,J,K))
  176                    VMAX=MAX(VMAX,VAL(I,J,K))
  177                  ENDIF
  178                  AR  =XX(2,I)*YY(2,J)*ZZ(2,K)*GGV(I,J,K)*FF(I,J,K)
  179                  VAV =VAV +AR
  180                  VINT=VINT+AR*VAL(I,J,K)
  181                ENDIF
  182   500        CONTINUE
  183   510      CONTINUE
  184   520    CONTINUE
  186        ENDIF
  189        IF (IP.NE.0) THEN
  190          W=VMIN
  191          CALL VF_P1MIND(W,VMIN)
  192          W=VMAX
  193          CALL VF_P1MAXD(W,VMAX)
  194          W=VAV
  195          CALL VF_P1SUMD(W,VAV)
  196          W=VINT
  197          CALL VF_P1SUMD(W,VINT)
  198          IF (VAV.GT.0.0D0) VAV=VINT/VAV
  199        ELSE
  200          W= 1.0D+30
  201          CALL VF_P1MIND(W,VMIN)
  202          W=-1.0D+30
  203          CALL VF_P1MAXD(W,VMAX)
  204          W=0.0D0
  205          CALL VF_P1SUMD(W,VAV)
  206          W=0.0D0
  207          CALL VF_P1SUMD(W,VINT)
  208          IF (VAV.GT.0.0D0) VAV=VINT/VAV
```

#### 3D vf_cdiv00.f

```text
   49                VAL=VAL+VD*VD
   55        CALL VF_P1SUMD(W,VAL)
   56        VAL=SQRT(VAL)
```

#### 3D vf_cdtcal.f

```text
  130                DT=V/MAX(FL1,FL2,FL3,FL4,FL5,FL6,V/DT)
  133                V=0.5D0/(1.0D0/(DX*DX)+1.0D0/(DY*DY)+1.0D0/(DZ*DZ))
  134                DT=V/MAX(WK01(I,J,K),V/DT)
  147        DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)
```

#### 3D vf_cggv.f

```text
   42        IF (IPRNT.EQ.1) THEN
   43          AOLD=0.0D0
   44          ANOW=1.0D0
   46          IF     (T0.LE.PRTOLD) THEN
   47            AOLD=1.0D0
   48            ANOW=0.0D0
   49          ELSEIF (T0.GE.PRTNOW) THEN
   50            AOLD=0.0D0
   51            ANOW=1.0D0
   52          ELSE
   53            ANOW=(T0-PRTOLD)/(PRTNOW-PRTOLD)
   54            AOLD=1.0D0-ANOW
```

#### 3D vf_cggxyz.f

```text
   77                      GGX(IW,JW,K)=MIN(GGV(IW,JW,K),GGV(IW-1,JW,K))
  103                      GGY(IW,JW,K)=MIN(GGV(IW,JW,K),GGV(IW,JW-1,K))
  126                      GGZ(IW,JW,K)=MIN(GGV(IW,JW,K),GGV(IW,JW,K-1))
```

#### 3D vf_cindc.f

```text
   39              IF     (NF(I,J,K).EQ. 0) THEN
   40                INDC(I,J,K)=0
   42              ELSEIF (NF(I,J,K).EQ. 8) THEN
   43                INDC(I,J,K)=-1
   45              ELSEIF (NF(I,J,K).EQ.-1) THEN
   46                INDC(I,J,K)=-1
   48              ELSE
   49                INDC(I,J,K)=0
   51   100      CONTINUE
   52   110    CONTINUE
   53   120  CONTINUE
```

#### 3D vf_cpara.f

```text
   20        NUMNPI=NUMNPI+1
   21        NUMNPJ=NUMNPJ+1
   79        NUMI =MYGIE-MYGIS+1
   89        NUMI =NUMI+MYMIS+MYMIE
```


#### 3D vf_csetup.f

```text
   65            H =BCTYP (2,JD)
   67            IF     (N.EQ.-3 .AND. MTBTYP.EQ.1) THEN
   68              IF (D.LT.ZERO)
   69       &        CALL VF_A2ERR('VF_CSETUP','(WAVE-BC DEPTH) NOT FOUND.')
   70              IF (T.LT.ZERO)
   71       &        CALL VF_A2ERR('VF_CSETUP','(WAVE-BC PERIOD) NOT FOUND.')
   72            ELSEIF (N.EQ.-3 .AND. MTBTYP.EQ.2) THEN
   73              IF (T.LT.ZERO)
   74       &        CALL VF_A2ERR('VF_CSETUP','(WAVE-BC PERIOD) NOT FOUND.')
   75            ELSEIF (N.EQ.-3 .AND. MTBTYP.EQ.3) THEN
   76              IF (T.LT.ZERO)
   77       &        CALL VF_A2ERR('VF_CSETUP','(WAVE-BC PERIOD) NOT FOUND.')
   78            ELSEIF (N.EQ.-4 .AND. MTBTYP2.EQ.1) THEN
   79              IF (D.LT.ZERO)
   80       &        CALL VF_A2ERR('VF_CSETUP','(WAVE-BC DEPTH) NOT FOUND.')
   81              IF (T.LT.ZERO)
   82       &        CALL VF_A2ERR('VF_CSETUP','(WAVE-BC PERIOD) NOT FOUND.')
   83            ELSEIF (N.EQ.-4 .AND. MTBTYP2.EQ.2) THEN
   84              IF (T.LT.ZERO)
   85       &        CALL VF_A2ERR('VF_CSETUP','(WAVE-BC PERIOD) NOT FOUND.')
   86            ELSEIF (N.EQ.-4 .AND. MTBTYP2.EQ.3) THEN
   87              IF (T.LT.ZERO)
   88       &        CALL VF_A2ERR('VF_CSETUP','(WAVE-BC PERIOD) NOT FOUND.')
   89            ELSE
   90              IF (D.LT.ZERO)
   91       &        CALL VF_A2ERR('VF_CSETUP','(WAVE-BC DEPTH) NOT FOUND.')
   92              IF (H.LT.ZERO)
   93       &        CALL VF_A2ERR('VF_CSETUP','(WAVE-BC HEIGHT) NOT FOUND.')
   94              IF (T.LT.ZERO)
   95       &        CALL VF_A2ERR('VF_CSETUP','(WAVE-BC PERIOD) NOT FOUND.')
   97            IF (N.EQ.-3 .OR. N.EQ.-4) THEN
   98              IF (ABS(BCTYP(9,JD)).GT.ZERO)
   99       &        CALL VF_A2ERR('VF_CSETUP','(WAVE-BC ANGLE) CAN NOT USE.')
  103            IF (D.GE.ZERO) WUS=GRZ0*H*T*T/D/D
  113            CALL VF_CWMAK0(D,T,H,WLN,N)
  116              CALL VF_CWZERO(WT0,N)
  123            BCTYP(4,JD)=WLN
  124            BCTYP(5,JD)=WUS
  125            BCTYP(6,JD)=WT0
  128          ELSEIF (IBCTYP(1,JD).EQ.2) THEN
  129            N =IBCTYP(2,JD)
  130            L1=IBCTYP(3,JD)
  131            L2=IBCTYP(4,JD)
  132            D =BCTYP (1,JD)
  133            T =BCTYP (3,JD)
  134            IF (D.LT.ZERO)
  135       &        CALL VF_A2ERR('VF_CSETUP','(OPEN-BC DEPTH) NOT FOUND.')
  136            IF (T.LT.ZERO)
  137       &        CALL VF_A2ERR('VF_CSETUP','(OPEN-BC PERIOD) NOT FOUND.')
  139            CALL VF_COMAK0(D,T,PI,GRZ0,WLN,N)
  140            BCTYP(2,JD)=0.0D0
  141            BCTYP(4,JD)=WLN
  142            BCTYP(5,JD)=0.0D0
  143            BCTYP(6,JD)=WLN/T
  144          ENDIF
  147          IF     (IBCTYP(1,JD).EQ.1) THEN
  148            IB=5
  149          ELSEIF (IBCTYP(1,JD).EQ.2) THEN
  150            IB=7
  151          ELSE
  152            IB=0
  153          ENDIF
  154          IF (IB.NE.0) THEN
  155            IF (JD.EQ.1 .OR. JD.EQ.2) THEN
  156              IF (JD.EQ.1) THEN
  157                I=2
  158              ELSE
  159                I=NUMI0
  160              ENDIF
  161              IF (L1.LE.0) THEN
  162                L1=2
  163                L2=NUMJ0-1
  164                IBCTYP(3,JD)=L1
  165                IBCTYP(4,JD)=L2
  166              ENDIF
  167              IF (MYGIS.LE.I .AND. I.LE.MYGIE) THEN
  168                DO 110 K=2,NUMK-1
  169                  DO 100 J=L1,L2
  170                    IF (MYGJS.LE.J .AND. J.LE.MYGJE) THEN
  171                      L=INDX(I-IP,J-JP,K)
  172                      IF (L.GE.1) THEN
  173                        INDB(3,L)=IB
  174                        BCU (  L)=0.0D0
  175                        BCV (  L)=0.0D0
  176                        BCW (  L)=0.0D0
  222        DO 200 JD=1,4
  223          IF (IDAMP(JD).NE.-1) THEN
  224            N =IDAMP(  JD)
  225            W =DAMP (3,JD)
  226            D =DAMP (4,JD)
  227            IF (N.LT.0)
  228       &        CALL VF_A2ERR('VF_CSETUP','(DAMP DEGREE) NOT FOUND.')
  229            IF (W.LT.ZERO)
  230       &        CALL VF_A2ERR('VF_CSETUP','(DAMP WIDTH) NOT FOUND.')
  231            IF (D.LT.ZERO)
  232       &        CALL VF_A2ERR('VF_CSETUP','(DAMP DEPTH) NOT FOUND.')
  233          ENDIF
  234   200  CONTINUE
  237        IF (LEQK.NE.0) THEN
  238          DO 300 L=1,NUMB
  239            IF (INDB(3,L).EQ.6) THEN
  240              INDBK(L)=6
  241              BCK  (L)=0.0D0
  242              INDBE(L)=6
  243              BCE  (L)=0.0D0
  244            ELSEIF (INDB(3,L).EQ.8) THEN
  245              INDBK(L)=8
  246              BCK  (L)=0.0D0
  247              INDBE(L)=8
  248              BCE  (L)=0.0D0
  249            ENDIF
  250   300    CONTINUE
  267          ELSEIF (N.EQ.-3 .AND. MTBTYP.EQ.3) THEN
  268            CALL VF_A2ERR('VF_CSETUP','(WAVE-SRC) MTBTYP ERROR.')
```

#### 3D vf_cvort.f

```text
  109              VORT=YY(4,J0)*(WYP-WYM)-ZZ(4,K0)*(VZP-VZM)
  152              VORT=ZZ(4,K0)*(UZP-UZM)-XX(4,I0)*(WXP-WXM)
  195              VORT=XX(4,I0)*(VXP-VXM)-YY(4,J0)*(UYP-UYM)
```

#### 3D vf_cwmtb1.f

```text
   29        IF     (WVT.LE.DMTBTT(1)    ) THEN
   30          MTBNOW=1
   31          W1=1.0D0
   32          W2=0.0D0
   33        ELSEIF (WVT.GE.DMTBTT(MTBTT)) THEN
   34          MTBNOW=MTBTT-1
   35          W1=0.0D0
   36          W2=1.0D0
```

#### 3D vf_cwmtb2.f

```text
   31        IF     (ZC.LE.DMTBZZ(1)    ) THEN
   32          KM=1
   33          W1=1.0D0
   34          W2=0.0D0
   35        ELSEIF (ZC.GE.DMTBZZ(MTBZZ)) THEN
   36          KM=MTBZZ-1
   37          W1=0.0D0
   38          W2=1.0D0
```

#### 3D vf_fcut01.f

```text
   40                V=XX(2,I)*YY(2,J)*ZZ(2,K)*GGV(I,J,K)
   41                IF     (FF(I,J,K).GT.FUPPER) THEN
   42                  FCUT=FCUT+(FF(I,J,K)-1.0D0)*V
   43                  FF(I,J,K)=1.0D0
   44                ELSEIF (FF(I,J,K).LT.FLOWER) THEN
   45                  FCUT=FCUT+(FF(I,J,K)-0.0D0)*V
   46                  FF(I,J,K)=0.0D0
   47                ENDIF
   48                FSUM=FSUM+FF(I,J,K)*V
```

#### 3D vf_fnfini.f

```text
  122                      INDS(NS)=I+NUMI*(J-1)+NUMI*NUMJ*(K-1)
  154          DO 1300 L=1,NUMS
  155            IJK=INDS(L)
  156            K  =(IJK-1)/(NUMI*NUMJ)+1
  157            IJK=IJK-NUMI*NUMJ*(K-1)
  158            J  =(IJK-1)/NUMI+1
  159            I  =IJK-NUMI*(J-1)
```

#### 3D vf_fpvcpp.f

```text
   74                M=INDX(I ,J,K)
   75                IF (M.GE.1) THEN
   76                  M=INDB(3,M)
   77                  IF (M.EQ.4 .OR. M.EQ.5 .OR. M.EQ.7) IPVCBC(L)=1
  182        DO 440 L=1,NPVCB
  183          IF (IPVCBC(L).NE.0) THEN
  184            PVCPES(L)=0.0D0
  185          ELSE
  186            IF (PVCVES(L).GT.0.0D0) THEN
  187              PAV=PVCPES(L)/PVCVES(L)
  188            ELSE
  189              PAV=PVCPFS(L)/PVCVFS(L)
  190            ENDIF
  191            PVCPES(L)=(PAV+PVCP0)/(1.0D0+PVCGM*DTNOW*PVCDIV(L))-PVCP0
  192          ENDIF
```

#### 3D vf_ii1inp.f

```text
  104        DATA MODEORS /0/
  112        LEVEL=0
  113        IF (NUMI0.GT.0) LEVEL=1
  114        IF (NUMBX.GT.0) LEVEL=2
  115        WRITE(ILPFIL,9510) '## INPUT-LEVEL=',LEVEL
  132          OPEN(MFILIN,ERR=9010,
  133       &       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.in',
  134       &       STATUS='OLD',FORM='FORMATTED'  )
  145            IF (LEVEL.EQ.1.AND.MODEOBS.EQ.1 ) THEN
  146              IF(IINFIL.EQ.MFILIN) THEN ! 1回目のEOFでファイルを切り替え
  147                IINFIL=MFILOB
  148                IEOF=0
  149              ELSEIF(IINFIL.EQ.MFILOB) THEN  ! 2回目のEOFでループ抜け
  150                IINFIL=MFILIN
  151                GOTO 5010
  152              ELSE
  153                CALL VF_A2ERR('VF_II1INP','UNEXPECTED ERROR 1.')
  154              ENDIF
  157            ELSEIF (LEVEL.GE.2 .AND.MODEPRS.EQ.1 ) THEN
  158              IF(IINFIL.EQ.MFILIN) THEN ! 1回目のEOFでファイルを切り替え
  159                IINFIL=MFILPS
  160                IEOF=0
  161              ELSEIF(IINFIL.EQ.MFILPS) THEN  ! 2回目のEOFでループ抜け
  162                IINFIL=MFILIN
  163                GOTO 5010
  196            IF     (TEXT(IS(2):IE(2)).EQ.'X') THEN
  200            ELSEIF (TEXT(IS(2):IE(2)).EQ.'Y') THEN
  204            ELSEIF (TEXT(IS(2):IE(2)).EQ.'Z') THEN
  213          ELSEIF (TEXT(IS(1):IE(1)).EQ.'OBST') THEN
  214            IF(TEXT(IS(2):IE(2)).EQ.'FILE') THEN
  215              IF (LEVEL.LE.0) THEN
  216                IF(MODEOBS.EQ.0) THEN
  217                  WRITE(ILPFIL,9520) (TEXT(IS(I):IE(I)),I=1,NWD)
  218                  IF (MYRANK.EQ.0.OR.INMODE.EQ.1) THEN
  219                    OPEN(MFILOB,ERR=9020,FILE=TEXT(IS(3):IE(3)),
  220       &                 STATUS='OLD',FORM='FORMATTED'  )
  237          ELSEIF (TEXT(IS(1):IE(1)).EQ.'POROUS') THEN
  238            IF(TEXT(IS(2):IE(2)).EQ.'FILE') THEN
  239              IF (LEVEL.LE.0) THEN
  240                IF(MODEPRS.EQ.0) THEN
  241                  WRITE(ILPFIL,9520) (TEXT(IS(I):IE(I)),I=1,NWD)
  242                  IF (MYRANK.EQ.0.OR.INMODE.EQ.1) THEN
  243                    OPEN(MFILPS,ERR=9030,FILE=TEXT(IS(3):IE(3)),
  244       &                 STATUS='OLD',FORM='FORMATTED'  )
  262          ELSEIF (TEXT(IS(1):IE(1)).EQ.'B.C.') THEN
  267              IF     (TEXT(IS(2):IE(2)).EQ.'D') THEN
  281              ELSEIF (TEXT(IS(2):IE(2)).EQ.'X') THEN
  287              ELSEIF (TEXT(IS(2):IE(2)).EQ.'Y') THEN
  293              ELSEIF (TEXT(IS(2):IE(2)).EQ.'Z') THEN
  336            IF( TEXT(IS(2):IE(2)).EQ.'RES' ) THEN
  341                IF( TEXT(IS(3):IE(3)).EQ.'AUTO' ) THEN
  343                    IRETYP=-1
  344                    OPEN(MFILAR,ERR=310,
  345       &               FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.ars',
  346       &               STATUS='OLD',FORM='FORMATTED'  )
  347                    READ(MFILAR,*,ERR=310) II,TT
  348                    CLOSE(MFILAR)
  350                    IRETYP=II
  442              WRITE(TEXTP,'(I5.5)') MYRANK
  443              OPEN(MFILOR,FORM='UNFORMATTED',STATUS='UNKNOWN',ERR=9040,
  444       &         FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.obs'//TEXTP)
  446              WRITE(MFILOR) NF
```

#### 3D vf_iiboun.f

```text
   98          IF (I1.LT.1  .OR. I2.GT.NUMI0-1 .OR.
   99       &      J1.LT.1  .OR. J2.GT.NUMJ0-2 .OR.
  100       &      K1.LT.1  .OR. K2.GT.NUMK -2 .OR.
  101       &      I1.GT.I2 .OR. J1.GT.J2 .OR. K1.GT.K2)
  102       &                 CALL VF_A2ERR('VF_IIBOUN','INVALID VALUE.')
  146        IF     (TEXT(IS(IP):IE(IP)).EQ.'VP') THEN
  149          IF     (TEXT(IS(IP):IE(IP)).EQ.'SLIP') THEN
  156          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'NON-S') THEN
  163          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'FIX-V') THEN
  172          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'FREE') THEN
  179          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'LOG') THEN
  186          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'LOG-KS') THEN
  204                    L=INDXYZ(I-IPP,J-JPP,K)
  205                    IF (L.GE.1) THEN
  206                      INDB(3,L)=IB
  207                      BCU (  L)=BU
  208                      BCV (  L)=BV
  209                      BCW (  L)=BW
  210                      BCP (  L)=BP
  211                      BCVI(  L)=BT
  220        ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'F') THEN
  223          IF     (TEXT(IS(IP):IE(IP)).EQ.'FIX') THEN
  227            CALL VF_ZSTOR(BF,TEXT(IS(IP):IE(IP)))
  228            IF (BF.LT.0.0D0 .OR. BF.GT.1.0D0)
  229       &                   CALL VF_A2ERR('VF_IIBOUN','INVALID VALUE.')
  230          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'FREE') THEN
  231            IB=2
  232            BF=0.0D0
  253        ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'K') THEN
  256          IF     (TEXT(IS(IP):IE(IP)).EQ.'FIX-A'  ) THEN
  259            IB=-1
  262          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'FIX+A'  ) THEN
  265            IB= 1
  268          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'FREE-A' ) THEN
  269            IB=-2
  271          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'FREE+A' ) THEN
  272            IB= 2
  339        ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'T') THEN
  342          IF     (TEXT(IS(IP):IE(IP)).EQ.'FIX-A'  ) THEN
  349          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'FIX+A'  ) THEN
  356          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'FREE-A' ) THEN
  361          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'FREE+A' ) THEN
  366          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'FLUX-A' ) THEN
  373          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'FLUX+A' ) THEN
  380          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'TRAN-A' ) THEN
  388          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'TRAN+A' ) THEN
  420        ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'C') THEN
  423          CALL VF_ZSTOI(LC,TEXT(IS(IP):IE(IP)))
  424          IF (LC.LE.0 .OR. LC.GT.LEQC)
  425       &                  CALL VF_A2ERR('VF_IIBOUN','INVALID VALUE.')
  428          IF     (TEXT(IS(IP):IE(IP)).EQ.'FIX-A'  ) THEN
  435          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'FIX+A'  ) THEN
  442          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'FREE-A' ) THEN
  447          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'FREE+A' ) THEN
  452          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'FLUX-A' ) THEN
  459          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'FLUX+A' ) THEN
  466          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'TRAN-A' ) THEN
  474          ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'TRAN+A' ) THEN
```


#### 3D vf_iicomp.f

```text
   35          IF     (TEXT(IS(3):IE(3)).EQ.'VP-DONOR') THEN
   37            CALL VF_ZSTOR(SCMVP,TEXT(IS(4):IE(4)))
   38            IF (SCMVP.LT.0.0D0 .OR. SCMVP.GT.1.0D0)
   39       &                 CALL VF_A2ERR('VF_IICOMP','INVALID VALUE.')
   42          ELSEIF (TEXT(IS(3):IE(3)).EQ.'FF-DN-AC') THEN
   43            ISCMFF=0
   45          ELSEIF (TEXT(IS(3):IE(3)).EQ.'FF-SLOPE') THEN
   46            ISCMFF=1
   48          ELSEIF (TEXT(IS(3):IE(3)).EQ.'KE-DONOR') THEN
   51            IF (SCMK.LT.0.0D0 .OR. SCMK.GT.1.0D0)
   52       &                 CALL VF_A2ERR('VF_IICOMP','INVALID VALUE.')
   55          ELSEIF (TEXT(IS(3):IE(3)).EQ.'T-DONOR') THEN
   62          ELSEIF (TEXT(IS(3):IE(3)).EQ.'C-DONOR') THEN
   64            CALL VF_ZSTOI(LC,TEXT(IS(4):IE(4)))
   66            IF (LC.LE.0 .OR. LC.GT.LEQC)
   67       &                 CALL VF_A2ERR('VF_IICOMP','INVALID VALUE.')
   78        ELSEIF (TEXT(IS(2):IE(2)).EQ.'MTRX') THEN
   81          IF     (TEXT(IS(3):IE(3)).EQ.'ILUBCGSTAB') THEN
   82            ICGTYP=0
   84          ELSEIF (TEXT(IS(3):IE(3)).EQ.'M-ILUBCGSTAB') THEN
   85            IF (NWD.LT.4) CALL VF_A2ERR('VF_IICOMP','SYNTAX ERROR.')
   86            CALL VF_ZSTOR(CGPARA,TEXT(IS(4):IE(4)))
   87            IF (CGPARA.LT.0.0D0 .OR. CGPARA.GT.1.0D0)
   88       &                 CALL VF_A2ERR('VF_IICOMP','INVALID VALUE.')
   89            ICGTYP=1
   91          ELSEIF (TEXT(IS(3):IE(3)).EQ.'MAX-ITR') THEN
   93            CALL VF_ZSTOI(ICGMAX,TEXT(IS(4):IE(4)))
   94            IF (ICGMAX.LT.0) CALL VF_A2ERR('VF_IICOMP','INVALID VALUE.')
   96          ELSEIF (TEXT(IS(3):IE(3)).EQ.'A-ERROR') THEN
   98            CALL VF_ZSTOR(CGEPSA,TEXT(IS(4):IE(4)))
   99            IF (CGEPSA.LT.0.0D0)
  100       &                 CALL VF_A2ERR('VF_IICOMP','INVALID VALUE.')
```

#### 3D vf_iidbg.f

```text
   33        IF     (TEXT(IS(2):IE(2)).EQ.'F-BOX') THEN
   35          DO 100 I=1,6
   36            CALL VF_ZSTOI(IDBGF(I),TEXT(IS(I+2):IE(I+2)))
   37            IDBGF(I)=IDBGF(I)+1
   55        ELSEIF (TEXT(IS(2):IE(2)).EQ.'TD-VEL') THEN
   57          DO 200 I=1,6
   58            CALL VF_ZSTOI(IDBGTD(I),TEXT(IS(I+2):IE(I+2)))
   59            IDBGTD(I)=IDBGTD(I)+1
   71          CALL VF_ZSTOR(RDBGTD(1),TEXT(IS( 9):IE( 9)))
   72          CALL VF_ZSTOR(RDBGTD(2),TEXT(IS(10):IE(10)))
   73          CALL VF_ZSTOR(RDBGTD(3),TEXT(IS(11):IE(11)))
```

#### 3D vf_iiequa.f

```text
   30        IF     (TEXT(IS(2):IE(2)).EQ.'K-EPS') THEN
   31          IF (NWD.LT.3) CALL VF_A2ERR('VF_IIEQUA','SYNTAX ERROR.')
   32          IF     (TEXT(IS(3):IE(3)).EQ.'NOCALC') THEN
   33            LEQK=0
   34          ELSEIF (TEXT(IS(3):IE(3)).EQ.'CALC'  ) THEN
   35            LEQK=1
   52        ELSEIF (TEXT(IS(2):IE(2)).EQ.'CONCENTRATION') THEN
   53          IF (NWD.LT.3) CALL VF_A2ERR('VF_IIEQUA','SYNTAX ERROR.')
   54          CALL VF_ZSTOI(LEQC,TEXT(IS(3):IE(3)))
   55          IF (LEQC.LT.0    ) CALL VF_A2ERR('VF_IIEQUA','INVALID VALUE.')
   56          IF (LEQC.GT.MAXNC) CALL VF_A2ERR('VF_IIEQUA','INVALID VALUE.')
```

#### 3D vf_iifile.f

```text
   33        IF     (TEXT(IS(2):IE(2)).EQ.'L/P') THEN
   36          IF     (TEXT(IS(3):IE(3)).EQ.'STEP') THEN
   45          ELSEIF (TEXT(IS(3):IE(3)).EQ.'TIME') THEN
   54          ELSEIF (TEXT(IS(3):IE(3)).EQ.'AREA') THEN
   56            IF     (TEXT(IS(4):IE(4)).EQ.'XY') THEN
   58            ELSEIF (TEXT(IS(4):IE(4)).EQ.'XZ') THEN
   60            ELSEIF (TEXT(IS(4):IE(4)).EQ.'YZ') THEN
   62            ELSEIF (TEXT(IS(4):IE(4)).EQ.'YX') THEN
   64            ELSEIF (TEXT(IS(4):IE(4)).EQ.'ZX') THEN
   66            ELSEIF (TEXT(IS(4):IE(4)).EQ.'ZY') THEN
   92          ELSEIF (TEXT(IS(3):IE(3)).EQ.'ON' .OR.
   93       &          TEXT(IS(3):IE(3)).EQ.'OFF'    ) THEN
   94            IF (NWD.LT.4) CALL VF_A2ERR('VF_IIFILE','SYNTAX ERROR.')
   95            ISW=0
   96            IF (TEXT(IS(3):IE(3)).EQ.'ON') ISW=1
   97            IF     (TEXT(IS(4):IE(4)).EQ.'OBST'  ) THEN
   98              ILPON( 1)=ISW
   99            ELSEIF (TEXT(IS(4):IE(4)).EQ.'BC-IND') THEN
  100              ILPON( 2)=ISW
  101            ELSEIF (TEXT(IS(4):IE(4)).EQ.'CM0'   ) THEN
  102              ILPON( 3)=ISW
  103            ELSEIF (TEXT(IS(4):IE(4)).EQ.'CD0'   ) THEN
  104              ILPON( 4)=ISW
  105            ELSEIF (TEXT(IS(4):IE(4)).EQ.'POROUS') THEN
  106              ILPON( 5)=ISW
  107            ELSEIF (TEXT(IS(4):IE(4)).EQ.'LAMBDA') THEN
  108              ILPON( 6)=ISW
  109            ELSEIF (TEXT(IS(4):IE(4)).EQ.'NF'    ) THEN
  110              ILPON( 7)=ISW
  111            ELSEIF (TEXT(IS(4):IE(4)).EQ.'F'     ) THEN
  112              ILPON( 8)=ISW
  113            ELSEIF (TEXT(IS(4):IE(4)).EQ.'V'     ) THEN
  114              ILPON( 9)=ISW
  115            ELSEIF (TEXT(IS(4):IE(4)).EQ.'P'     ) THEN
  116              ILPON(10)=ISW
  117            ELSEIF (TEXT(IS(4):IE(4)).EQ.'VISC'  ) THEN
  118              ILPON(11)=ISW
  119            ELSEIF (TEXT(IS(4):IE(4)).EQ.'BC'    ) THEN
  120              ILPON(12)=ISW
  121            ELSEIF (TEXT(IS(4):IE(4)).EQ.'T'     ) THEN
  122              ILPON(13)=ISW
  123            ELSEIF (TEXT(IS(4):IE(4)).EQ.'T-COND') THEN
  124              ILPON(14)=ISW
  125            ELSEIF (TEXT(IS(4):IE(4)).EQ.'C'     ) THEN
  126              ILPON(15)=ISW
  127            ELSEIF (TEXT(IS(4):IE(4)).EQ.'DIFFUS') THEN
  128              ILPON(16)=ISW
  129            ELSEIF (TEXT(IS(4):IE(4)).EQ.'K'     ) THEN
  130              ILPON(17)=ISW
  131            ELSEIF (TEXT(IS(4):IE(4)).EQ.'E'     ) THEN
  132              ILPON(18)=ISW
  133            ELSEIF (TEXT(IS(4):IE(4)).EQ.'VISC-T') THEN
  134              ILPON(19)=ISW
  135            ELSEIF (TEXT(IS(4):IE(4)).EQ.'IPVC'  ) THEN
  136              ILPON(20)=ISW
  137            ELSEIF (TEXT(IS(4):IE(4)).EQ.'PPPVC' ) THEN
  138              ILPON(21)=ISW
  148        ELSEIF (TEXT(IS(2):IE(2)).EQ.'GRP') THEN
  151          IF     (TEXT(IS(3):IE(3)).EQ.'STEP') THEN
  160          ELSEIF (TEXT(IS(3):IE(3)).EQ.'TIME') THEN
  169          ELSEIF (TEXT(IS(3):IE(3)).EQ.'AREA') THEN
  170            IF (NWD.LT.9) CALL VF_A2ERR('VF_IIFILE','SYNTAX ERROR.')
  171            DO 100 I=1,6
  172              CALL VF_ZSTOI(IGRARA(I),TEXT(IS(I+3):IE(I+3)))
  173              IGRARA(I)=IGRARA(I)+1
  175            IF (IGRARA(1).LE.1) IGRARA(1)=2
  176            IF (IGRARA(2).LE.1) IGRARA(2)=2
  177            IF (IGRARA(3).LE.1) IGRARA(3)=2
  178            IF (IGRARA(4).LE.1) IGRARA(4)=NUMI0-1
  179            IF (IGRARA(5).LE.1) IGRARA(5)=NUMJ0-1
  180            IF (IGRARA(6).LE.1) IGRARA(6)=NUMK -1
  181            IF ((IGRARA(1).GT.IGRARA(4)) .OR.
  182       &        (IGRARA(2).GT.IGRARA(5)) .OR.
  183       &        (IGRARA(3).GT.IGRARA(6)) .OR.
  184       &        (IGRARA(4).GE.NUMI0    ) .OR.
  185       &        (IGRARA(5).GE.NUMJ0    ) .OR.
  186       &        (IGRARA(6).GE.NUMK     )     )
  187       &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')
  189          ELSEIF (TEXT(IS(3):IE(3)).EQ.'ON' ) THEN
  190            IF (NWD.LT.4) CALL VF_A2ERR('VF_IIFILE','SYNTAX ERROR.')
  191            IF (TEXT(IS(4):IE(4)).EQ.'VORT') THEN
  192              IGRVOR=1
  193            ELSE
  194              CALL VF_A2ERR('VF_IIFILE','UNKNOWN WORD.')
  195            ENDIF
  197          ELSEIF (TEXT(IS(3):IE(3)).EQ.'OFF') THEN
  198            IF (NWD.LT.4) CALL VF_A2ERR('VF_IIFILE','SYNTAX ERROR.')
  199            IF (TEXT(IS(4):IE(4)).EQ.'VORT') THEN
  200              IGRVOR=0
  210        ELSEIF (TEXT(IS(2):IE(2)).EQ.'RSL') THEN
  213          IF     (TEXT(IS(3):IE(3)).EQ.'STEP') THEN
  222          ELSEIF (TEXT(IS(3):IE(3)).EQ.'TIME') THEN
  231          ELSEIF (TEXT(IS(3):IE(3)).EQ.'ELAPSE') THEN
  232            IF (NWD.LT.4) CALL VF_A2ERR('VF_IIFILE','SYNTAX ERROR.')
  233            CALL VF_ZSTOR(ETIME,TEXT(IS(4):IE(4)))
  247        ELSEIF (TEXT(IS(2):IE(2)).EQ.'TRN') THEN
  248          IF (NWD.LT.3) CALL VF_A2ERR('VF_IIFILE','SYNTAX ERROR.')
  250          IF     (TEXT(IS(3):IE(3)).EQ.'STEP') THEN
  251            IF (NWD.LT.6) CALL VF_A2ERR('VF_IIFILE','SYNTAX ERROR.')
  252            CALL VF_ZSTOI(ITRTRN(1),TEXT(IS(4):IE(4)))
  253            CALL VF_ZSTOI(ITRTRN(2),TEXT(IS(5):IE(5)))
  254            CALL VF_ZSTOI(ITRTRN(3),TEXT(IS(6):IE(6)))
  255            ITRTYP=1
  256            IF (ITRTRN(1).GT.ITRTRN(2) .OR. ITRTRN(3).LE.0)
  257       &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')
  259          ELSEIF (TEXT(IS(3):IE(3)).EQ.'TIME') THEN
  260            IF (NWD.LT.6) CALL VF_A2ERR('VF_IIFILE','SYNTAX ERROR.')
  261            CALL VF_ZSTOR(RTRTRN(1),TEXT(IS(4):IE(4)))
  262            CALL VF_ZSTOR(RTRTRN(2),TEXT(IS(5):IE(5)))
  263            CALL VF_ZSTOR(RTRTRN(3),TEXT(IS(6):IE(6)))
  264            ITRTYP=2
  265            IF (RTRTRN(1).GT.RTRTRN(2) .OR. RTRTRN(3).LE.0.0D0)
  266       &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')
  268          ELSEIF (TEXT(IS(3):IE(3)).EQ.'W-LEVEL') THEN
  269            IF (NWD.LT.5) CALL VF_A2ERR('VF_IIFILE','SYNTAX ERROR.')
  270            IF (ITRNUM.GE.MAXTR)
  271       &                  CALL VF_A2ERR('VF_IIFILE','AREA IS FULL.')
  272            ITRNUM=ITRNUM+1
  273            ITRPRM(1,ITRNUM)=0
  274            ITRPRM(2,ITRNUM)=0
  275            IF (TEXT(IS(4):IE(4)).EQ.'ANS') THEN
  276              IF     (TEXT(IS(5):IE(5)).EQ.'X-') THEN
  277                ITRPRM(3,ITRNUM)=-1
  278              ELSEIF (TEXT(IS(5):IE(5)).EQ.'X+') THEN
  279                ITRPRM(3,ITRNUM)=-2
  280              ELSEIF (TEXT(IS(5):IE(5)).EQ.'Y-') THEN
  281                ITRPRM(3,ITRNUM)=-3
  282              ELSEIF (TEXT(IS(5):IE(5)).EQ.'Y+') THEN
  283                ITRPRM(3,ITRNUM)=-4
  284              ELSEIF (TEXT(IS(5):IE(5)).EQ.'SRC') THEN
  285                ITRPRM(3,ITRNUM)=-5
  286              ELSE
  287                CALL VF_A2ERR('VF_IIFILE','UNKNOWN WORD.')
  288              ENDIF
  289              ITRPRM(4,ITRNUM)=0
  290            ELSE
  291              CALL VF_ZSTOI(I1,TEXT(IS(4):IE(4)))
  292              CALL VF_ZSTOI(J1,TEXT(IS(5):IE(5)))
  293              IF (I1.LT.1 .OR. I1.GT.NUMI0-2)
  294       &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')
  295              IF (J1.LT.1 .OR. J1.GT.NUMJ0-2)
  296       &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')
  297              ITRPRM(3,ITRNUM)=I1+1
  298              ITRPRM(4,ITRNUM)=J1+1
  299            ENDIF
  300            ITRPRM(5,ITRNUM)=0
  301            ITRPRM(6,ITRNUM)=0
  302            ITRPRM(7,ITRNUM)=0
  303            ITRPRM(8,ITRNUM)=0
  310            IF     (TEXT(IS(3):IE(3)).EQ.'POINT') THEN
  314            ELSEIF (TEXT(IS(3):IE(3)).EQ.'MIN'  ) THEN
  318            ELSEIF (TEXT(IS(3):IE(3)).EQ.'MAX'  ) THEN
  322            ELSEIF (TEXT(IS(3):IE(3)).EQ.'AV'   ) THEN
  326            ELSEIF (TEXT(IS(3):IE(3)).EQ.'INT'  ) THEN
  330            ELSEIF (TEXT(IS(3):IE(3)).EQ.'FORCE') THEN
  340              IF     (TEXT(IS(4):IE(4)).EQ.'X-') THEN
  342              ELSEIF (TEXT(IS(4):IE(4)).EQ.'X+') THEN
  344              ELSEIF (TEXT(IS(4):IE(4)).EQ.'Y-') THEN
  346              ELSEIF (TEXT(IS(4):IE(4)).EQ.'Y+') THEN
  348              ELSEIF (TEXT(IS(4):IE(4)).EQ.'Z-') THEN
  350              ELSEIF (TEXT(IS(4):IE(4)).EQ.'Z+') THEN
  375                CALL VF_ZSTOI(LC,TEXT(IS(5):IE(5)))
  376                IF (LC.LE.0 .OR. LC.GT.LEQC)
  377       &                     CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')
  380              ELSEIF (TEXT(IS(4):IE(4)).EQ.'VORT-X') THEN
  381                ITRPRM(2,ITRNUM)=17
  382                IF (ITRPRM(1,ITRNUM).NE.1) 
  383       &                      CALL VF_A2ERR('VF_IIFILE','{PHY} ERROR.')
  384              ELSEIF (TEXT(IS(4):IE(4)).EQ.'VORT-Y') THEN
  385                ITRPRM(2,ITRNUM)=18
  386                IF (ITRPRM(1,ITRNUM).NE.1) 
  387       &                      CALL VF_A2ERR('VF_IIFILE','{PHY} ERROR.')
  388              ELSEIF (TEXT(IS(4):IE(4)).EQ.'VORT-Z') THEN
  389                ITRPRM(2,ITRNUM)=19
  390                IF (ITRPRM(1,ITRNUM).NE.1) 
  391       &                      CALL VF_A2ERR('VF_IIFILE','{PHY} ERROR.')
  445        ELSEIF (TEXT(IS(2):IE(2)).EQ.'MAM') THEN
  446          IF (NWD.LT.3) CALL VF_A2ERR('VF_IIFILE','SYNTAX ERROR.')
  448          IF     (TEXT(IS(3):IE(3)).EQ.'STEP') THEN
  449            IF (NWD.LT.6) CALL VF_A2ERR('VF_IIFILE','SYNTAX ERROR.')
  450            CALL VF_ZSTOI(IMMTRN(1),TEXT(IS(4):IE(4)))
  451            CALL VF_ZSTOI(IMMTRN(2),TEXT(IS(5):IE(5)))
  452            CALL VF_ZSTOI(IMMTRN(3),TEXT(IS(6):IE(6)))
  453            IMMTYP=1
  454            IF (IMMTRN(1).GT.IMMTRN(2) .OR. IMMTRN(3).LE.0)
  455       &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')
  457          ELSEIF (TEXT(IS(3):IE(3)).EQ.'TIME') THEN
  458            IF (NWD.LT.6) CALL VF_A2ERR('VF_IIFILE','SYNTAX ERROR.')
  459            CALL VF_ZSTOR(RMMTRN(1),TEXT(IS(4):IE(4)))
  460            CALL VF_ZSTOR(RMMTRN(2),TEXT(IS(5):IE(5)))
  461            CALL VF_ZSTOR(RMMTRN(3),TEXT(IS(6):IE(6)))
  462            IMMTYP=2
  463            IF (RMMTRN(1).GT.RMMTRN(2) .OR. RMMTRN(3).LE.0.0D0)
  464       &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')
  466          ELSE
  467            CALL VF_A2ERR('VF_IIFILE','UNKNOWN WORD.')
  468          ENDIF
  471        ELSEIF (TEXT(IS(2):IE(2)).EQ.'PORO') THEN
  472          IF (NWD.LT.3) CALL VF_A2ERR('VF_IIFILE','SYNTAX ERROR.')
  473          CALL VF_ZSTOI(IPRNT,TEXT(IS(3):IE(3)))
  474          IF (IPRNT.LT.0) CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')
```


#### 3D vf_iigrid.f

```text
   46        IF (NL.NE.0) CALL VF_A2ERR('VF_IIGRID','SECOND TIMES.')
   47        NL  =1
   48        IEND=0
   49        IP  =3
   50        X1  =0.0D0
   51        X2  =0.0D0
   53        XOLD=0.0D0
   54        IF     (ISW.EQ.1) THEN
   55          NUML0=NUMI0
   56          LG0=MYGIS
   57          LG2=MYGIE
   58        ELSEIF (ISW.EQ.2) THEN
   59          NUML0=NUMJ0
   60          LG0=MYGJS
   61          LG2=MYGJE
   62        ELSE
   63          NUML0=NUML
   64          LG0=1
   65          LG2=NUML0
   66        ENDIF
   67        LG1=LG0
   68        IF (LG1.EQ.1) LG1=2
   72   100  CONTINUE
   75          DO 200 I=IP,NWD
   76            IF (TEXT(IS(I):IE(I)).EQ.'END') THEN
   77              IF (I.NE.NWD) CALL VF_A2ERR('VF_IIGRID','SYNTAX ERROR.')
   78              IEND=I
   79              GOTO 210
   80            ELSE
   81              NL=NL+1
   82              IF ((LEVEL.GE.1) .AND. (NL.GT.NUML0)) 
   83       &                CALL VF_A2ERR('VF_IIGRID','FILE WAS CHANGED.')
   84              CALL VF_ZSTOR(XNOW,TEXT(IS(I):IE(I)))
   85              IF (NL.GE.3) THEN
   86                IF (XNOW-XOLD.LT.ZEROG)
   87       &                  CALL VF_A2ERR('VF_IIGRID','INVALID VALUE.')
   88              ENDIF
   89              IF (LEVEL.EQ.1) THEN
   90                IF     (LG1.LE.NL .AND. NL.LE.LG2) THEN
   91                  XYZ(1,NL-LG0+1)=XNOW
   92                ELSEIF (NL.EQ.LG2+1              ) THEN
   94                  XBUF=XNOW
   95                ENDIF
   97                XYZWK(NL-1)=XNOW
   98              ENDIF
   99              XOLD=XNOW
  100              IF (NL.EQ.2) X1=XNOW
  101              X2=XNOW
  102            ENDIF
  103   200    CONTINUE
  104   210    CONTINUE
  107          IF (IEND.NE.0) GOTO 300
  108          IF (IEOF.NE.0) CALL VF_A2ERR('VF_IIGRID','NOT FOUND (END).')
  111          CALL VF_ZGETLN(IS,IE,MAXWDS,NWD,IINFIL,IEOF,TEXT)
  112          IF (NWD.GT.0 .AND. LEVEL.LE.0)
  113       &               WRITE(ILPFIL,9510) (TEXT(IS(I):IE(I)),I=1,NWD)
  114          IP=1
  117          GOTO 100
  118   300  CONTINUE
  121        IF (NL.LT.3) CALL VF_A2ERR('VF_IIGRID','2 > NUMBER OF GRID.')
  144   9510 FORMAT(' ','& ',100('[',A,']':))
```

#### 3D vf_iimate.f

```text
   31        IF     (TEXT(IS(2):IE(2)).EQ.'W-LEVEL') THEN
   33          CALL VF_ZSTOR(WVLVL,TEXT(IS(3):IE(3)))
   36        ELSEIF (TEXT(IS(2):IE(2)).EQ.'DENSITY') THEN
   38          CALL VF_ZSTOR(RHO0,TEXT(IS(3):IE(3)))
   39          IF (RHO0.LT.ZERO) CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')
   42        ELSEIF (TEXT(IS(2):IE(2)).EQ.'K-VISC') THEN
   44          CALL VF_ZSTOR(ANU0,TEXT(IS(3):IE(3)))
   45          IF (ANU0.LT.0.0D0) CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')
   48        ELSEIF (TEXT(IS(2):IE(2)).EQ.'GRAVITY') THEN
   50          CALL VF_ZSTOR(GRZ0,TEXT(IS(3):IE(3)))
   51          IF (GRZ0.LT.0.0D0) CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')
   54        ELSEIF (TEXT(IS(2):IE(2)).EQ.'S-HEAT') THEN
   56          CALL VF_ZSTOR(TCP0,TEXT(IS(3):IE(3)))
   57          IF (TCP0.LT.ZERO) CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')
   60        ELSEIF (TEXT(IS(2):IE(2)).EQ.'T-COND') THEN
   62          CALL VF_ZSTOR(TCN0,TEXT(IS(3):IE(3)))
   63          IF (TCN0.LT.ZERO) CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')
   66        ELSEIF (TEXT(IS(2):IE(2)).EQ.'T-DENS') THEN
   68          CALL VF_ZSTOR(TDT0,TEXT(IS(3):IE(3)))
   69          CALL VF_ZSTOR(TDR0,TEXT(IS(4):IE(4)))
   72        ELSEIF (TEXT(IS(2):IE(2)).EQ.'DIFFUS') THEN
   74          CALL VF_ZSTOI(LC,TEXT(IS(3):IE(3)))
   75          CALL VF_ZSTOR(SC,TEXT(IS(4):IE(4)))
   76          IF (LC.LE.0 .OR. LC.GT.LEQC)
   77       &                  CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')
   78          IF (SC.LT.ZERO) CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')
   79          CDF0(LC)=SC
   82        ELSEIF (TEXT(IS(2):IE(2)).EQ.'C-DENS') THEN
   84          CALL VF_ZSTOI(LC,TEXT(IS(3):IE(3)))
   85          CALL VF_ZSTOR(SC,TEXT(IS(4):IE(4)))
   86          CALL VF_ZSTOR(SR,TEXT(IS(5):IE(5)))
   87          IF (LC.LE.0 .OR. LC.GT.LEQC)
   88       &                  CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')
   89          CDC0(LC)=SC
   90          CDR0(LC)=SR
   93        ELSEIF (TEXT(IS(2):IE(2)).EQ.'I.C.') THEN
   96          IF     (TEXT(IS(3):IE(3)).EQ.'V') THEN
   98            CALL VF_ZSTOR(UINI,TEXT(IS(4):IE(4)))
   99            CALL VF_ZSTOR(VINI,TEXT(IS(5):IE(5)))
  100            CALL VF_ZSTOR(WINI,TEXT(IS(6):IE(6)))
  102          ELSEIF (TEXT(IS(3):IE(3)).EQ.'KE') THEN
  104            CALL VF_ZSTOR(AKINIK,TEXT(IS(4):IE(4)))
  105            CALL VF_ZSTOR(AKINIE,TEXT(IS(5):IE(5)))
  106            IF (AKINIK.LT.ZERO)
  107       &                 CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')
  108            IF (AKINIE.LT.ZERO)
  109       &                 CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')
  111          ELSEIF (TEXT(IS(3):IE(3)).EQ.'T') THEN
  113            CALL VF_ZSTOR(TINI,TEXT(IS(4):IE(4)))
  115          ELSEIF (TEXT(IS(3):IE(3)).EQ.'C') THEN
  117            CALL VF_ZSTOI(LC,TEXT(IS(4):IE(4)))
  118            CALL VF_ZSTOR(SC,TEXT(IS(5):IE(5)))
  119            IF (LC.LE.0 .OR. LC.GT.LEQC)
  120       &                 CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')
  121            CINI(LC)=SC
```


#### 3D vf_iimdl.f

```text
   31        IF (NWD.LT.2) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
   34        IF     (TEXT(IS(2):IE(2)).EQ.'WAVE-BC') THEN
   35          IF (NWD.LT.3) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
   36          IF     (TEXT(IS(3):IE(3)).EQ.'X-') THEN
   37            JD=1
   38          ELSEIF (TEXT(IS(3):IE(3)).EQ.'X+') THEN
   39            JD=2
   40          ELSEIF (TEXT(IS(3):IE(3)).EQ.'Y-') THEN
   41            JD=3
   42          ELSEIF (TEXT(IS(3):IE(3)).EQ.'Y+') THEN
   43            JD=4
   44          ELSE
   45            CALL VF_A2ERR('VF_IIMDL','UNKNOWN WORD.')
   46          ENDIF
   47          IF (IBCTYP(1,JD).NE.0 .AND. IBCTYP(1,JD).NE.1)
   48       &              CALL VF_A2ERR('VF_IIMDL','DEFINED DOUBLY.')
   49          IBCTYP(1,JD)=1
   50          IF (NWD.LT.4) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
   51          IF     (TEXT(IS(4):IE(4)).EQ.'FUNC'  ) THEN
   52            IF     (TEXT(IS(5):IE(5)).EQ.'STREAM' ) THEN
   53              IF (NWD.LT.6) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
   54              CALL VF_ZSTOI(IVAL,TEXT(IS(6):IE(6)))
   55              IF (IVAL.LT.1 .OR. IVAL.GT.22)
   56       &                    CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
   57              IBCTYP(2,JD)=IVAL
   58            ELSEIF (TEXT(IS(5):IE(5)).EQ.'STK-CND') THEN
   59              IBCTYP(2,JD)= 0
   60            ELSEIF (TEXT(IS(5):IE(5)).EQ.'STOKES' ) THEN
   61              IBCTYP(2,JD)=-2
   62            ELSEIF (TEXT(IS(5):IE(5)).EQ.'CNOIDAL') THEN
   63              IBCTYP(2,JD)=-1
   64            ELSEIF (TEXT(IS(5):IE(5)).EQ.'MATRIX' ) THEN
   65              IBCTYP(2,JD)=-3
   66              MTBTYP=1
   67            ELSEIF (TEXT(IS(5):IE(5)).EQ.'MATRIX2') THEN
   68              IBCTYP(2,JD)=-4
   69              MTBTYP2=1
   70            ELSE
   71              CALL VF_A2ERR('VF_IIMDL','UNKNOWN WORD.')
   72            ENDIF
   73          ELSEIF (TEXT(IS(4):IE(4)).EQ.'DEPTH' ) THEN
   74            IF (NWD.LT.5) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
   75            CALL VF_ZSTOR(VAL,TEXT(IS(5):IE(5)))
   76            IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
   77            BCTYP(1,JD)=VAL
   78          ELSEIF (TEXT(IS(4):IE(4)).EQ.'HEIGHT') THEN
   79            IF (NWD.LT.5) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
   80            CALL VF_ZSTOR(VAL,TEXT(IS(5):IE(5)))
   81            IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
   82            BCTYP(2,JD)=VAL
   83          ELSEIF (TEXT(IS(4):IE(4)).EQ.'PERIOD') THEN
   84            IF (NWD.LT.5) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
   85            CALL VF_ZSTOR(VAL,TEXT(IS(5):IE(5)))
   86            IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
   87            BCTYP(3,JD)=VAL
   88          ELSEIF (TEXT(IS(4):IE(4)).EQ.'AMPL'  ) THEN
   89            IF (NWD.LT.5) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
   90            CALL VF_ZSTOR(VAL,TEXT(IS(5):IE(5)))
   91            BCTYP(8,JD)=VAL
   92          ELSEIF (TEXT(IS(4):IE(4)).EQ.'AREA'  ) THEN
   93            IF (NWD.LT.6) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
   94            CALL VF_ZSTOI(L1,TEXT(IS(5):IE(5)))
   95            CALL VF_ZSTOI(L2,TEXT(IS(6):IE(6)))
   96            L1=L1+1
   97            L2=L2+1
   98            IF (JD.EQ.1 .OR. JD.EQ.2) THEN
   99              IF (L1.LT.2 .OR. L2.GT.NUMJ0-1 .OR. L1.GT.L2)
  100       &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')
  101            ELSE
  102              IF (L1.LT.2 .OR. L2.GT.NUMI0-1 .OR. L1.GT.L2)
  103       &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')
  104            ENDIF
  105            IBCTYP(3,JD)=L1
  106            IBCTYP(4,JD)=L2
  107          ELSEIF (TEXT(IS(4):IE(4)).EQ.'ANGLE' ) THEN
  108            IF (NWD.LT.7) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  109            CALL VF_ZSTOR(BCTYP( 9,JD),TEXT(IS(5):IE(5)))
  110            CALL VF_ZSTOR(BCTYP(10,JD),TEXT(IS(6):IE(6)))
  111            CALL VF_ZSTOR(BCTYP(11,JD),TEXT(IS(7):IE(7)))
  112          ELSE
  113            CALL VF_A2ERR('VF_IIMDL','UNKNOWN WORD.')
  114          ENDIF
  117        ELSEIF   (TEXT(IS(2):IE(2)).EQ.'WAVE-SRC') THEN
  118          IF (NWD.LT.3) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  119          IF     (TEXT(IS(3):IE(3)).EQ.'X') THEN
  120            IF (NWD.LT.4) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  121            CALL VF_ZSTOI(L1,TEXT(IS(4):IE(4)))
  122            L1=L1+1
  123            IF (L1.LT.2 .OR. L1.GT.NUMI0-1)
  124       &                  CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')
  125            ISCTYP(1)=L1
  126          ELSEIF (TEXT(IS(3):IE(3)).EQ.'Y') THEN
  127            IF (NWD.LT.4) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  128            CALL VF_ZSTOI(L1,TEXT(IS(4):IE(4)))
  129            L1=L1+1
  130            IF (L1.LT.2 .OR. L1.GT.NUMJ0-1)
  131       &                  CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')
  132            ISCTYP(1)=-L1
  133          ELSEIF (TEXT(IS(3):IE(3)).EQ.'FUNC'  ) THEN
  134            IF (NWD.LT.4) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  135            IF     (TEXT(IS(4):IE(4)).EQ.'STREAM' ) THEN
  136              IF (NWD.LT.5) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  137              CALL VF_ZSTOI(IVAL,TEXT(IS(5):IE(5)))
  138              IF (IVAL.LT.1 .OR. IVAL.GT.22)
  139       &                    CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  140              ISCTYP(2)=IVAL
  141            ELSEIF (TEXT(IS(4):IE(4)).EQ.'STK-CND') THEN
  142              ISCTYP(2)= 0
  143            ELSEIF (TEXT(IS(4):IE(4)).EQ.'STOKES' ) THEN
  144              ISCTYP(2)=-2
  145            ELSEIF (TEXT(IS(4):IE(4)).EQ.'CNOIDAL') THEN
  146              ISCTYP(2)=-1
  147            ELSEIF (TEXT(IS(4):IE(4)).EQ.'MATRIX' ) THEN
  148              ISCTYP(2)=-3
  149              MTBTYP=1
  150            ELSE
  151              CALL VF_A2ERR('VF_IIMDL','UNKNOWN WORD.')
  152            ENDIF
  153          ELSEIF (TEXT(IS(3):IE(3)).EQ.'DEPTH' ) THEN
  154            IF (NWD.LT.4) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  155            CALL VF_ZSTOR(VAL,TEXT(IS(4):IE(4)))
  156            IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  157            SCTYP(1)=VAL
  158          ELSEIF (TEXT(IS(3):IE(3)).EQ.'HEIGHT') THEN
  159            IF (NWD.LT.4) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  160            CALL VF_ZSTOR(VAL,TEXT(IS(4):IE(4)))
  161            IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  162            SCTYP(2)=VAL
  163          ELSEIF (TEXT(IS(3):IE(3)).EQ.'PERIOD') THEN
  164            IF (NWD.LT.4) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  165            CALL VF_ZSTOR(VAL,TEXT(IS(4):IE(4)))
  166            IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  167            SCTYP(3)=VAL
  168          ELSEIF (TEXT(IS(3):IE(3)).EQ.'AMPL'  ) THEN
  169            IF (NWD.LT.4) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  170            CALL VF_ZSTOR(VAL,TEXT(IS(4):IE(4)))
  171            SCTYP(8)=VAL
  172          ELSE
  173            CALL VF_A2ERR('VF_IIMDL','UNKNOWN WORD.')
  174          ENDIF
  177        ELSEIF (TEXT(IS(2):IE(2)).EQ.'OPEN-BC') THEN
  178          IF (NWD.LT.3) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  179          IF     (TEXT(IS(3):IE(3)).EQ.'X-') THEN
  180            JD=1
  181          ELSEIF (TEXT(IS(3):IE(3)).EQ.'X+') THEN
  182            JD=2
  183          ELSEIF (TEXT(IS(3):IE(3)).EQ.'Y-') THEN
  184            JD=3
  185          ELSEIF (TEXT(IS(3):IE(3)).EQ.'Y+') THEN
  186            JD=4
  187          ELSE
  188            CALL VF_A2ERR('VF_IIMDL','UNKNOWN WORD.')
  189          ENDIF
  190          IF (IBCTYP(1,JD).NE.0 .AND. IBCTYP(1,JD).NE.2)
  191       &              CALL VF_A2ERR('VF_IIMDL','DEFINED DOUBLY.')
  192          IBCTYP(1,JD)=2
  193          IBCTYP(3,JD)=0
  194          IBCTYP(4,JD)=0
  195          IF (NWD.LT.4) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  196          IF     (TEXT(IS(4):IE(4)).EQ.'FUNC'  ) THEN
  197            IF     (TEXT(IS(5):IE(5)).EQ.'TYPE1' ) THEN
  198              IBCTYP(2,JD)= 0
  199            ELSE
  200              CALL VF_A2ERR('VF_IIMDL','UNKNOWN WORD.')
  201            ENDIF
  202          ELSEIF (TEXT(IS(4):IE(4)).EQ.'DEPTH' ) THEN
  203            IF (NWD.LT.5) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  204            CALL VF_ZSTOR(VAL,TEXT(IS(5):IE(5)))
  205            IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  206            BCTYP(1,JD)=VAL
  207          ELSEIF (TEXT(IS(4):IE(4)).EQ.'PERIOD') THEN
  208            IF (NWD.LT.5) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  209            CALL VF_ZSTOR(VAL,TEXT(IS(5):IE(5)))
  210            IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  211            BCTYP(3,JD)=VAL
  212          ELSE
  213            CALL VF_A2ERR('VF_IIMDL','UNKNOWN WORD.')
  214          ENDIF
  217        ELSEIF (TEXT(IS(2):IE(2)).EQ.'DAMP') THEN
  218          IF (NWD.LT.3) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  219          IF     (TEXT(IS(3):IE(3)).EQ.'X-') THEN
  220            JD=1
  221          ELSEIF (TEXT(IS(3):IE(3)).EQ.'X+') THEN
  222            JD=2
  223          ELSEIF (TEXT(IS(3):IE(3)).EQ.'Y-') THEN
  224            JD=3
  225          ELSEIF (TEXT(IS(3):IE(3)).EQ.'Y+') THEN
  226            JD=4
  227          ELSE
  228            CALL VF_A2ERR('VF_IIMDL','UNKNOWN WORD.')
  229          ENDIF
  230          IF (IDAMP(JD).EQ.-1) IDAMP(JD)=-2
  231          IF (NWD.LT.4) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  232          IF     (TEXT(IS(4):IE(4)).EQ.'DEGREE'  ) THEN
  233            IF (NWD.LT.5) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  234            CALL VF_ZSTOI(IVAL,TEXT(IS(5):IE(5)))
  235            IF (IVAL.LT.0) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  236            IDAMP(JD)=IVAL
  237          ELSEIF (TEXT(IS(4):IE(4)).EQ.'PARAM-XY') THEN
  238            IF (NWD.LT.5) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  239            CALL VF_ZSTOR(VAL,TEXT(IS(5):IE(5)))
  240            IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  241            DAMP(1,JD)=VAL
  242          ELSEIF (TEXT(IS(4):IE(4)).EQ.'PARAM-Z' ) THEN
  243            IF (NWD.LT.5) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  244            CALL VF_ZSTOR(VAL,TEXT(IS(5):IE(5)))
  245            IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  246            DAMP(2,JD)=VAL
  247          ELSEIF (TEXT(IS(4):IE(4)).EQ.'WIDTH'   ) THEN
  248            IF (NWD.LT.5) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  249            CALL VF_ZSTOR(VAL,TEXT(IS(5):IE(5)))
  250            IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  251            DAMP(3,JD)=VAL
  252          ELSEIF (TEXT(IS(4):IE(4)).EQ.'DEPTH'   ) THEN
  253            IF (NWD.LT.5) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  254            CALL VF_ZSTOR(VAL,TEXT(IS(5):IE(5)))
  255            IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  256            DAMP(4,JD)=VAL
  257          ELSE
  258            CALL VF_A2ERR('VF_IIMDL','UNKNOWN WORD.')
  259          ENDIF
  262        ELSEIF (TEXT(IS(2):IE(2)).EQ.'K-EPS') THEN
  263          IF (NWD.LT.3) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  264          IF     (TEXT(IS(3):IE(3)).EQ.'LIM'      ) THEN
  265            IF (NWD.LT.5) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  266            CALL VF_ZSTOR(AKMINK,TEXT(IS(4):IE(4)))
  267            CALL VF_ZSTOR(AKMINE,TEXT(IS(5):IE(5)))
  268            IF (AKMINK.LT.ZERO)
  269       &                  CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  270            IF (AKMINE.LT.ZERO)
  271       &                  CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  272          ELSEIF (TEXT(IS(3):IE(3)).EQ.'PARAMETER') THEN
  273            IF (NWD.LT.9) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  274            CALL VF_ZSTOR(AKCMU,TEXT(IS(4):IE(4)))
  275            CALL VF_ZSTOR(AKSGK,TEXT(IS(5):IE(5)))
  276            CALL VF_ZSTOR(AKSGE,TEXT(IS(6):IE(6)))
  277            CALL VF_ZSTOR(AKC1 ,TEXT(IS(7):IE(7)))
  278            CALL VF_ZSTOR(AKC2 ,TEXT(IS(8):IE(8)))
  279            CALL VF_ZSTOR(AKC3 ,TEXT(IS(9):IE(9)))
  280            IF (AKCMU.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  281            IF (AKSGK.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  282            IF (AKSGE.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  283            IF (AKC1.LT.0.0D0) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  284            IF (AKC2.LT.0.0D0) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  285            IF (AKC3.LT.0.0D0) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  286          ELSEIF (TEXT(IS(3):IE(3)).EQ.'LOG-LAW'  ) THEN
  287            IF (NWD.LT.5) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  288            CALL VF_ZSTOR(AKK0,TEXT(IS(4):IE(4)))
  289            CALL VF_ZSTOR(AKA0,TEXT(IS(5):IE(5)))
  290            IF (AKK0.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  291            IF (AKA0.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  292          ELSEIF (TEXT(IS(3):IE(3)).EQ.'PRANDTL'  ) THEN
  293            IF (NWD.LT.4) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  294            CALL VF_ZSTOR(AKPR,TEXT(IS(4):IE(4)))
  295            IF (AKPR.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  296          ELSEIF (TEXT(IS(3):IE(3)).EQ.'SCHMIDT'  ) THEN
  297            IF (NWD.LT.5) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')
  298            CALL VF_ZSTOI(LC,TEXT(IS(4):IE(4)))
  299            CALL VF_ZSTOR(SC,TEXT(IS(5):IE(5)))
  300            IF (LC.LE.0 .OR. LC.GT.LEQC)
  301       &                    CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  302            IF (SC.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')
  303            AKSM(LC)=SC
  304          ELSE
  305            CALL VF_A2ERR('VF_IIMDL','UNKNOWN WORD.')
  306          ENDIF
  309        ELSE
  310          CALL VF_A2ERR('VF_IIMDL','UNKNOWN WORD.')
  311        ENDIF
```

#### 3D vf_iiobst.f

```text
   35        CALL VF_ZSTOI(I1,TEXT(IS(2):IE(2)))
   36        CALL VF_ZSTOI(J1,TEXT(IS(3):IE(3)))
   37        CALL VF_ZSTOI(K1,TEXT(IS(4):IE(4)))
   38        CALL VF_ZSTOI(I2,TEXT(IS(5):IE(5)))
   39        CALL VF_ZSTOI(J2,TEXT(IS(6):IE(6)))
   40        CALL VF_ZSTOI(K2,TEXT(IS(7):IE(7)))
   41        IF (I1.LT.1 .OR. I2.GT.NUMI0-2 .OR. I1.GT.I2 .OR.
   42       &    J1.LT.1 .OR. J2.GT.NUMJ0-2 .OR. J1.GT.J2 .OR.
   43       &    K1.LT.1 .OR. K2.GT.NUMK -2 .OR. K1.GT.K2     ) 
   44       &                CALL VF_A2ERR('VF_IIOBST','INVALID VALUE.')
```


#### 3D vf_iiopt.f

```text
   41        IF     (TEXT(IS(2):IE(2)).EQ.'SUB-LOOP') THEN
   43          CALL VF_ZSTOI(LOOPS,TEXT(IS(3):IE(3)))
   44          IF (LOOPS.LT.1) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')
   47        ELSEIF (TEXT(IS(2):IE(2)).EQ.'S-CELL-VEL') THEN
   48          IF (NWD.LT.3) CALL VF_A2ERR('VF_IIOPT','SYNTAX ERROR.')
   49          IF     (TEXT(IS(3):IE(3)).EQ.'DU=0' ) THEN
   50            IBSUW0=1
   51          ELSEIF (TEXT(IS(3):IE(3)).EQ.'D2U=0') THEN
   52            IBSUW0=0
   58        ELSEIF (TEXT(IS(2):IE(2)).EQ.'T-DOOR') THEN
   60          IF     (TEXT(IS(3):IE(3)).EQ.'BUB' ) THEN
   61            IF (TEXT(IS(4):IE(4)).EQ.'OFF' ) THEN
   62              WBUB=0.0D0
   63            ELSE
   64              CALL VF_ZSTOR(WBUB,TEXT(IS(4):IE(4)))
   65              IF (WBUB.LT.ZERO) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')
   67          ELSEIF (TEXT(IS(3):IE(3)).EQ.'DROP') THEN
   68            IF     (TEXT(IS(4):IE(4)).EQ.'OFF'         ) THEN
   69              IDROP=0
   70            ELSEIF (TEXT(IS(4):IE(4)).EQ.'FREE-RUNDOWN') THEN
   71              IDROP=1
   80        ELSEIF (TEXT(IS(2):IE(2)).EQ.'PV=CONST') THEN
   82          CALL VF_ZSTOR(PVCP0,TEXT(IS(3):IE(3)))
   83          CALL VF_ZSTOR(PVCGM,TEXT(IS(4):IE(4)))
   84          IF (PVCP0.LT.ZERO ) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')
   85          IF (PVCGM.LT.1.0D0) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')
   88        ELSEIF (TEXT(IS(2):IE(2)).EQ.'DRAG-DF') THEN
   89          IF (NWD.LT.4) CALL VF_A2ERR('VF_IIOPT','SYNTAX ERROR.')
   90          CALL VF_ZSTOR(DRGYU,TEXT(IS(3):IE(3)))
   91          IF (DRGYU.LE.0.0D0) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')
   92          CALL VF_ZSTOI(IDRGN,TEXT(IS(4):IE(4)))
   93          IF (IDRGN.LE.0) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')
   94          IF (IDRGN.GT.MAXDRG) CALL VF_A2ERR('VF_IIOPT','AREA IS FULL.')
   95          DO 100 I=1,IDRGN
   96            IF (IEOF.NE.0) CALL VF_A2ERR('VF_IIOPT','SYNTAX ERROR.')
   98            CALL VF_ZGETLN(IS,IE,MAXWDS,NWD,IFIL,IEOF,TEXT)
   99            IF (NWD.NE.3) CALL VF_A2ERR('VF_IIOPT','SYNTAX ERROR.')
  100            CALL VF_ZSTOR(DRGDR(I),TEXT(IS(1):IE(1)))
  101            CALL VF_ZSTOR(DRGAP(I),TEXT(IS(2):IE(2)))
  102            CALL VF_ZSTOR(DRGBT(I),TEXT(IS(3):IE(3)))
  103            IF (DRGDR(I).LE.0.0D0)
  104       &            CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')
  105            IF (DRGAP(I).LT.0.0D0)
  106       &            CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')
  107            IF (DRGBT(I).LT.0.0D0)
  108       &            CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')
  113        ELSEIF (TEXT(IS(2):IE(2)).EQ.'SEA-BOTTOM') THEN
  114          IF (NWD.LT.3) CALL VF_A2ERR('VF_IIOPT','SYNTAX ERROR.')
  115          IF (TEXT(IS(3):IE(3)).EQ.'ON' ) THEN
  116            ISEABT = 1
  117          ELSEIF (TEXT(IS(3):IE(3)).EQ.'OFF' ) THEN
  118            ISEABT = 0
  120          ELSEIF (TEXT(IS(3):IE(3)).EQ.'CALC' ) THEN
  121            ISEABT = -1
  130        ELSEIF (TEXT(IS(2):IE(2)).EQ.'COORDINATE') THEN
  132          IF     (TEXT(IS(3):IE(3)).EQ.'JAPAN-PLANE-RECTANGULAR' ) THEN
  133            CALL VF_ZSTOI(ICOORD,TEXT(IS(4):IE(4)))
  134            IF (ICOORD.LT.1.OR.ICOORD.GT.19)
  135       $      CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')
  136          ELSEIF (TEXT(IS(3):IE(3)).EQ.'UTM') THEN
  137            CALL VF_ZSTOR(LC_DEG,TEXT(IS(4):IE(4)))
  138            CALL SET_UTM(LC_DEG)
  144        ELSEIF (TEXT(IS(2):IE(2)).EQ.'FAULT-SYSTEM') THEN
  146          IF     (TEXT(IS(3):IE(3)).EQ.'TOKYO' ) THEN
  148          ELSEIF (TEXT(IS(3):IE(3)).EQ.'JGD2000') THEN
  150          ELSEIF (TEXT(IS(3):IE(3)).EQ.'WGS84') THEN
  170        ELSEIF (TEXT(IS(2):IE(2)).EQ.'MAX-VELOCITY') THEN
  172          CALL VF_ZSTOR(VVMAX,TEXT(IS(3):IE(3)))
  173          IF (VVMAX.LE.ZERO ) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')
```

#### 3D vf_iipara.f

```text
   30        IF     (TEXT(IS(2):IE(2)).EQ.'X') THEN
   31          IF (NWD.LT.3) CALL VF_A2ERR('VF_IIPARA','SYNTAX ERROR.')
   32          NUMNPI=NUMNPI+1
   33          IF (NUMNPI.GE.MAXNPI)
   34       &                CALL VF_A2ERR('VF_IIPARA','AREA IS FULL.')
   35          CALL VF_ZSTOI(IPROCS(NUMNPI),TEXT(IS(3):IE(3)))
   38        ELSEIF (TEXT(IS(2):IE(2)).EQ.'Y') THEN
```

#### 3D vf_iiporo.f

```text
   52        IF     (TEXT(IS(2):IE(2)).EQ.'LIM') THEN
   54          CALL VF_ZSTOR(PLOWER,TEXT(IS(3):IE(3)))
   55          IF (PLOWER.LT.ZERO ) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')
   56          IF (PLOWER.GT.1.0D0) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')
   59        ELSEIF (TEXT(IS(2):IE(2)).EQ.'V') THEN
   61          CALL VF_ZSTOI(I1,TEXT(IS( 3):IE( 3)))
   62          CALL VF_ZSTOI(J1,TEXT(IS( 4):IE( 4)))
   63          CALL VF_ZSTOI(K1,TEXT(IS( 5):IE( 5)))
   64          CALL VF_ZSTOI(I2,TEXT(IS( 6):IE( 6)))
   65          CALL VF_ZSTOI(J2,TEXT(IS( 7):IE( 7)))
   66          CALL VF_ZSTOI(K2,TEXT(IS( 8):IE( 8)))
   67          CALL VF_ZSTOR(V1,TEXT(IS( 9):IE( 9)))
   68          CALL VF_ZSTOR(V2,TEXT(IS(10):IE(10)))
   69          VAL=MAX(V2+(1.0D0-V2)*V1,PLOWER)
   75          IF (V1 .LT.0.0D0) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')
   76          IF (V1 .GT.1.0D0) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')
   77          IF (VAL.LT.ZERO ) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')
   78          IF (VAL.GT.1.0D0) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')
   84                    IF (NF(I-IP,J-JP,K).NE.-1) GGV(I-IP,J-JP,K)=VAL
   92        ELSEIF (TEXT(IS(2):IE(2)).EQ.'X') THEN
  103          IF (I1.LT.1  .OR. I2.GT.NUMI0-1 .OR.
  104       &      J1.LT.1  .OR. J2.GT.NUMJ0-2 .OR.
  105       &      K1.LT.1  .OR. K2.GT.NUMK -2 .OR.
  106       &      I1.GT.I2 .OR. J1.GT.J2 .OR. K1.GT.K2)
  107       &                    CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')
  125        ELSEIF (TEXT(IS(2):IE(2)).EQ.'Y') THEN
  136          IF (I1.LT.1  .OR. I2.GT.NUMI0-2 .OR.
  137       &      J1.LT.1  .OR. J2.GT.NUMJ0-1 .OR.
  138       &      K1.LT.1  .OR. K2.GT.NUMK -2 .OR.
  139       &      I1.GT.I2 .OR. J1.GT.J2 .OR. K1.GT.K2)
  140       &                    CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')
  158        ELSEIF (TEXT(IS(2):IE(2)).EQ.'Z') THEN
  169          IF (I1.LT.1  .OR. I2.GT.NUMI0-2 .OR.
  170       &      J1.LT.1  .OR. J2.GT.NUMJ0-2 .OR.
  171       &      K1.LT.1  .OR. K2.GT.NUMK -1 .OR.
  172       &      I1.GT.I2 .OR. J1.GT.J2 .OR. K1.GT.K2)
  173       &                    CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')
  191        ELSEIF (TEXT(IS(2):IE(2)).EQ.'CM') THEN
  199          CALL VF_ZSTOR(CM,TEXT(IS(9):IE(9)))
  205          IF (CM.LT.0.0D0) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')
  211                    IF (NF(I-IP,J-JP,K).NE.-1) CM0(I-IP,J-JP,K)=CM
```

#### 3D vf_iitime.f

```text
   31        IF (TEXT(IS(2):IE(2)).EQ.'CONST') THEN
   32          IF (NWD.LT.3) CALL VF_A2ERR('VF_IITIME','SYNTAX ERROR.')
   33          CALL VF_ZSTOR(DTCNST,TEXT(IS(3):IE(3)))
   34          IF (DTCNST.LT.ZERO) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')
   35          IDTTYP=0
   38        ELSEIF (TEXT(IS(2):IE(2)).EQ.'AUTO') THEN
   39          IF (NWD.LT.4) CALL VF_A2ERR('VF_IITIME','SYNTAX ERROR.')
   40          CALL VF_ZSTOR(DTINIT,TEXT(IS(3):IE(3)))
   41          CALL VF_ZSTOR(DTSAFE,TEXT(IS(4):IE(4)))
   42          IF (DTINIT.LT.ZERO) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')
   43          IF (DTSAFE.LT.ZERO) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')
   44          IDTTYP=1
   47        ELSEIF (TEXT(IS(2):IE(2)).EQ.'LIMIT') THEN
   49          CALL VF_ZSTOR(DTMIN,TEXT(IS(3):IE(3)))
   50          CALL VF_ZSTOR(DTMAX,TEXT(IS(4):IE(4)))
   51          IF (DTMIN.LT.ZERO ) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')
   52          IF (DTMIN.GT.DTMAX) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')
   55        ELSEIF (TEXT(IS(2):IE(2)).EQ.'END') THEN
   57          CALL VF_ZSTOI(NEND,TEXT(IS(3):IE(3)))
   58          CALL VF_ZSTOR(TEND,TEXT(IS(4):IE(4)))
   59          IF (NEND.LT.0    ) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')
   60          IF (TEND.LT.0.0D0) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')
```

#### 3D vf_im1inp.f

```text
   44          OPEN(MFILMT,ERR=9010,
   45       &       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.mtb',
   46       &       STATUS='OLD',FORM='FORMATTED'  )
   61        IF     (TEXT(IS(IP):IE(IP)).EQ.'LEVEL-ON'  ) THEN
   62          MTBTYP=1
   63        ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'LEVEL-OFF' ) THEN
   64          MTBTYP=2
   65        ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'LEVEL-ONLY') THEN
   66          MTBTYP=3
  132            IF (TEXT(IS(IP):IE(IP)).NE.'T' )
  133       &                    CALL VF_A2ERR('VF_IM1INP','UNKNOWN WORD.')
  142            IF (DMTBTT(I).LT.0.0D0 .OR. DMTBTT(I).GT.1.0D0)
  143       &                    CALL VF_A2ERR('VF_IM1INP','INVALID VALUE.')
  144            IF (I.GT.1) THEN
  145              IF (DMTBTT(I).LE.DMTBTT(I-1))
  146       &                    CALL VF_A2ERR('VF_IM1INP','INVALID VALUE.')
```

#### 3D vf_ip1inp.f

```text
   10        IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)
   13        INCLUDE 'VF_A0PRM.h'
   14        INCLUDE 'VF_ACOMPR.h'
   15        INCLUDE 'VF_AFILEI.h'
   16        INCLUDE 'VF_AFILER.h'
   17        INCLUDE 'VF_ANUMBI.h'
   18        INCLUDE 'VF_APARAI.h'
   24        DIMENSION GGVOLD(IPRNP),GGVNOW(IPRNP)
   29        IF (IPRNT.GE.1 .AND. IPRIT.LT.0) THEN
   30          IPRFIL=0
   31          IF (MYRANK.EQ.0) THEN
   32            OPEN(MFILPR,ERR=9010,
   33       &         FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.poro',
   34       &         STATUS='OLD',FORM='UNFORMATTED' )
   35            IPRFIL=MFILPR
   36            WRITE(ILPFIL,9510)
   37            READ(IPRFIL,END=9020,ERR=9030) IPRNB,ISW1,ISW2,ISW3,ISW4
   38          ENDIF
   39          IF (NPROCS.NE.1) THEN
   40            CALL VF_P1BCSI(IPRNB,1,0)
   41          ENDIF
   42          IF (IPRNB.GT.MAXPRB) CALL VF_A2ERR('VF_IP1INP','AREA IS FULL.')
   43          IPRNP=0
   44          DO 110 IB=1,IPRNB
   45            IF (MYRANK.EQ.0) THEN
   46              READ(IPRFIL,END=9020,ERR=9030) (IPRARA(I,IB),I=1,6)
   47            ENDIF
   48            IF (NPROCS.NE.1) THEN
   49              CALL VF_P1BCSI(IPRARA(1,IB),6,0)
   50            ENDIF
   51            DO 100 I=1,6
   52              IPRARA(I,IB)=IPRARA(I,IB)+1
   53   100      CONTINUE
   54            IF ((IPRARA(1,IB).GT.IPRARA(4,IB)) .OR.
   55       &        (IPRARA(2,IB).GT.IPRARA(5,IB)) .OR.
   56       &        (IPRARA(3,IB).GT.IPRARA(6,IB)) .OR.
   57       &        (IPRARA(1,IB).LE.1           ) .OR.
   58       &        (IPRARA(2,IB).LE.1           ) .OR.
   59       &        (IPRARA(3,IB).LE.1           ) .OR.
   60       &        (IPRARA(4,IB).GE.NUMI0       ) .OR.
   61       &        (IPRARA(5,IB).GE.NUMJ0       ) .OR.
   62       &        (IPRARA(6,IB).GE.NUMK        )     )
   63       &                 CALL VF_A2ERR('VF_IP1INP','INVALID VALUE.')
   64            IPRNP=IPRNP+ (IPRARA(4,IB)-IPRARA(1,IB)+1)
   65       &                *(IPRARA(5,IB)-IPRARA(2,IB)+1)
   66       &                *(IPRARA(6,IB)-IPRARA(3,IB)+1)
   67   110    CONTINUE
   68          IPRIT=0
   71        ELSEIF (IPRNT.GE.1) THEN
   72          IF (MYRANK.EQ.0) THEN
   73   200      CONTINUE
   74              IF ((IPRIT.NE.0 .AND. PRTNOW.GE.T0) .OR.
   75       &          IPRNT.LE.IPRIT                      ) GOTO 240
   76              IPRIT=IPRIT+1
   77              PRTOLD=PRTNOW
   78              DO 210 L=1,IPRNP
   79                GGVOLD(L)=GGVNOW(L)
   80   210        CONTINUE
   81              READ(IPRFIL,END=9020,ERR=9030) PRTNOW,JSW1,JSW2,JSW3,JSW4
   82              WRITE(ILPFIL,9520) IPRIT,PRTNOW
   83              NP=0
   84              DO 220 IB=1,IPRNB
   85                NI=IPRARA(4,IB)-IPRARA(1,IB)+1
   86                NJ=IPRARA(5,IB)-IPRARA(2,IB)+1
   87                NK=IPRARA(6,IB)-IPRARA(3,IB)+1
   88                READ(IPRFIL,END=9020,ERR=9030)
   89       &               (((GGVNOW(NP+I+NI*(J-1)+NI*NJ*(K-1)),
   90       &                  I=1,NI),J=1,NJ),K=1,NK)
   91                NP=NP+NI*NJ*NK
   92   220        CONTINUE
   93              DO 230 L=1,IPRNP
   94                GGVNOW(L)=MAX(GGVNOW(L),PLOWER)
   95   230        CONTINUE
   96              GOTO 200
   97   240      CONTINUE
   98            IF (IPRIT.EQ.1) THEN
   99              PRTOLD=PRTNOW
  100              DO 250 L=1,IPRNP
  101                GGVOLD(L)=GGVNOW(L)
  102   250        CONTINUE
  103            ENDIF
  104          ENDIF
  105          IF (NPROCS.NE.1) THEN
  106            CALL VF_P1BCSI(IPRIT ,    1,0)
  107            CALL VF_P1BCSD(PRTOLD,    1,0)
  108            CALL VF_P1BCSD(PRTNOW,    1,0)
  109            CALL VF_P1BCSD(GGVOLD,IPRNP,0)
  110            CALL VF_P1BCSD(GGVNOW,IPRNP,0)
```

#### 3D vf_ir1inp.f

```text
  154        READ(IREFIL,ERR=9020) LN,LV,LP,LF,LK,LT,LS,LG,LD,L1
  155        IF (LK.NE.LEQK)
  156       &    CALL VF_A2ERR('VF_IR1INP','INVALID EQUATION (K-EPS).')
  157        IF (LT.NE.LEQT)
  158       &    CALL VF_A2ERR('VF_IR1INP','INVALID EQUATION (TEMP).')
  159        IF (LS.NE.LEQC)
  160       &    CALL VF_A2ERR('VF_IR1INP','INVALID EQUATION (CONC).')
  184          READ(IREFIL,END=1000,ERR=9020) NNOW,TNOW,DTNOW
```

#### 3D vf_m1bcgs.f

```text
  249        BNORM=SQRT(BNORM)
  250        XNORM=SQRT(XNORM)
```

#### 3D vf_og1ini.f

```text
   49          WRITE(TEXTP,'(I5.5)') MYRANK
   50          OPEN(MFILGR,ERR=9010,
   51       &       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.grp'//TEXTP,
   52       &       STATUS='NEW',FORM='UNFORMATTED' )
   55        WRITE(ILPFIL,9510)
   61        WRITE(IGRFIL,ERR=9020) NUMI0-1,NUMJ0-1,NUMK-1
   62        WRITE(IGRFIL,ERR=9020) GLXMIN,GLYMIN,ZZ(1,   2)
   63        WRITE(IGRFIL,ERR=9020) GLXMAX,GLYMAX,ZZ(1,NUMK)
   66        I1=IGRARA(1)
   67        J1=IGRARA(2)
   68        K1=IGRARA(3)
   69        I2=IGRARA(4)
   70        J2=IGRARA(5)
   71        K2=IGRARA(6)
   72        WRITE(IGRFIL,ERR=9020) I1,J1,K1,I2,J2,K2
   96        LS=0
   97        IF (LEQC .GT.0) LS=LEQC
   98        IF (IGRVOR.NE.0) LS=LS+3
```


#### 3D vf_ol1ini.f

```text
   85        WRITE(ILPFIL,9510) '-- PARALLEL --'
   86        WRITE(ILPFIL,9530) 'NPROCS      [-] =',NPROCS
   87        WRITE(ILPFIL,9530) '    NPI,NPJ [-] =',NUMNPI,NUMNPJ
   88        WRITE(ILPFIL,9530) 'MYRANK      [-] =',MYRANK
   89        WRITE(ILPFIL,9530) '    MYI,MYJ [-] =',MYRI,MYRJ
   90        WRITE(ILPFIL,9530) 'CELL-X(ALL) [-] =',NUMI0-2
   91        WRITE(ILPFIL,9530) '    ICS,ICE [-] =',MYGIS+MYMIS-1,MYGIE-MYMIE-1
   92        WRITE(ILPFIL,9530) 'CELL-Y(ALL) [-] =',NUMJ0-2
   93        WRITE(ILPFIL,9530) '    JCS,JCE [-] =',MYGJS+MYMJS-1,MYGJE-MYMJE-1
   94        WRITE(ILPFIL,9530) 'CELL-Z(ALL) [-] =',NUMK -2
   95        WRITE(ILPFIL,9530) '    KCS,KCE [-] =',1,NUMK-2
   98        WRITE(ILPFIL,9510) '-- EQUATION --'
   99        IF (LEQK.EQ.0) THEN
  100          WRITE(ILPFIL,9520) 'K-EPS           = NOCALC'
  101        ELSE
  102          WRITE(ILPFIL,9520) 'K-EPS           = CALC'
  103        ENDIF
  104        IF (LEQT.EQ.0) THEN
  105          WRITE(ILPFIL,9520) 'TEMPERATURE     = NOCALC'
  106        ELSE
  107          WRITE(ILPFIL,9520) 'TEMPERATURE     = CALC'
  108        ENDIF
  109        IF (LEQC.EQ.0) THEN
  110          WRITE(ILPFIL,9520) 'CONCENTRATION   = NOCALC'
  111        ELSE
  112          WRITE(ILPFIL,9530) 'CONCENTRATION[-]=',LEQC
  113        ENDIF
  116        WRITE(ILPFIL,9510) '-- TIME CONTROL --'
  117        IF (IDTTYP.EQ.0) THEN
  118          WRITE(ILPFIL,9520) 'DT     TYPE     = CONSTANT'
  119          WRITE(ILPFIL,9540) '       DELTA[S] =',DTCNST
  120        ELSE
  121          WRITE(ILPFIL,9520) 'DT     TYPE     = AUTO'
  122          WRITE(ILPFIL,9540) '       SAFE [-] =',DTSAFE
  123          WRITE(ILPFIL,9540) '       INIT [S] =',DTINIT
  124          WRITE(ILPFIL,9540) '       MIN  [S] =',DTMIN
  125          WRITE(ILPFIL,9540) '       MAX  [S] =',DTMAX
  126        ENDIF
  127        WRITE(ILPFIL,9530) 'END    STEP [-] =',NEND
  128        WRITE(ILPFIL,9540) '       TIME [S] =',TEND
  131        WRITE(ILPFIL,9510) '-- MATERIAL --'
  132        WRITE(ILPFIL,9540) 'W-LEVEL     [M] =',WVLVL
  133        WRITE(ILPFIL,9540) 'DENSITY [KG/M3] =',RHO0
  134        WRITE(ILPFIL,9540) 'K-VISC   [M2/S] =',ANU0
  135        WRITE(ILPFIL,9540) 'GRAVITY  [M/S2] =',GRZ0
  136        IF (LEQT.NE.0) THEN
  137          WRITE(ILPFIL,9540) 'S-HEAT [J/K/kg] =',TCP0
  138          WRITE(ILPFIL,9540) 'T-COND  [W/M/K] =',TCN0
  139          WRITE(ILPFIL,9540) 'T-D T0      [K] =',TDT0
  140          WRITE(ILPFIL,9540) 'T-D DR[KG/M3/K] =',TDR0
  141        ENDIF
  142        DO 100 LC=1,LEQC
  143          WRITE(ILPFIL,9540) 'DIFFUS   [M2/S] =',CDF0(LC)
  144          IF (CDF0(LC).LT.ZERO)
  145       &               CALL VF_A2ERR('VF_OL1INI','INVALID VALUE.')
  146   100  CONTINUE
  147        DO 110 LC=1,LEQC
  148          WRITE(ILPFIL,9540) 'C-D C0      [-] =',CDC0(LC)
  149   110  CONTINUE
  150        DO 120 LC=1,LEQC
  151          WRITE(ILPFIL,9540) 'C-D DR  [KG/M3] =',CDR0(LC)
  152   120  CONTINUE
  201            ELSEIF (JD.EQ.4) THEN
  202              WRITE(ILPFIL,9520) 'WAVE-BC Y+'
  203            ENDIF
  204            IF     (IBCTYP(2,JD).EQ.-2) THEN
  205              WRITE(ILPFIL,9520) '  FUNC          = STOKES(5TH)'
  206            ELSEIF (IBCTYP(2,JD).EQ.-1) THEN
  207              WRITE(ILPFIL,9520) '  FUNC          = CNOIDAL(3RD)'
  208            ELSEIF (IBCTYP(2,JD).GE. 1) THEN
  209              WRITE(ILPFIL,9520) '  FUNC          = STREAM'
  210              WRITE(ILPFIL,9530) '            N[-]=',IBCTYP(2,JD)
  211            ELSEIF (IBCTYP(2,JD).EQ.-3) THEN
  212              WRITE(ILPFIL,9520) '  FUNC          = MATRIX'
  213            ELSEIF (IBCTYP(2,JD).EQ.-4) THEN
  214              WRITE(ILPFIL,9520) '  FUNC          = MATRIX2'
  215            ENDIF
  216            WRITE(ILPFIL,9540) '  DEPTH      [M]=',BCTYP(1,JD)
  217            WRITE(ILPFIL,9540) '  HEIGHT     [M]=',BCTYP(2,JD)
  218            WRITE(ILPFIL,9540) '  PERIOD     [S]=',BCTYP(3,JD)
  219            WRITE(ILPFIL,9540) '  AMPL       [-]=',BCTYP(8,JD)
  220            IF (ABS(BCTYP(9,JD)).GE.ZERO) THEN
  221              WRITE(ILPFIL,9540) '  ANGLE    [DEG]=',BCTYP(9,JD)
  222              WRITE(ILPFIL,9540) '  X0         [M]=',BCTYP(10,JD)
  223              WRITE(ILPFIL,9540) '  Y0         [M]=',BCTYP(11,JD)
  224            ENDIF
  225            WRITE(ILPFIL,9540) '  LENGTH     [M]=',BCTYP(4,JD)
  226            WRITE(ILPFIL,9540) '  URSELL NUMB[-]=',BCTYP(5,JD)
  227            WRITE(ILPFIL,9540) '  0.0=WAVE(x)[-]=',BCTYP(6,JD)
  228          ENDIF
  229   200  CONTINUE
  230        DO 210 JD=1,4
  231          IF (IBCTYP(1,JD).EQ.2) THEN
  232            IF     (JD.EQ.1) THEN
  233              WRITE(ILPFIL,9520) 'OPEN-BC X-'
  234            ELSEIF (JD.EQ.2) THEN
  235              WRITE(ILPFIL,9520) 'OPEN-BC X+'
  236            ELSEIF (JD.EQ.3) THEN
  237              WRITE(ILPFIL,9520) 'OPEN-BC Y-'
  238            ELSEIF (JD.EQ.4) THEN
  239              WRITE(ILPFIL,9520) 'OPEN-BC Y+'
  240            ENDIF
  241            IF     (IBCTYP(2,JD).EQ.0) THEN
  242              WRITE(ILPFIL,9520) '  FUNC          = TYPE1'
  243            ENDIF
  244            WRITE(ILPFIL,9540) '  DEPTH      [M]=',BCTYP(1,JD)
  245            WRITE(ILPFIL,9540) '  PERIOD     [S]=',BCTYP(3,JD)
  246            WRITE(ILPFIL,9540) '  LENGTH     [M]=',BCTYP(4,JD)
  247            WRITE(ILPFIL,9540) '  VELOCITY   [-]=',BCTYP(6,JD)
  248          ENDIF
  249   210  CONTINUE
  250        DO 220 JD=1,4
  251          IF (IDAMP(JD).GE.0) THEN
  252            IF     (JD.EQ.1) THEN
  253              WRITE(ILPFIL,9520) 'DAMP    X-'
  254            ELSEIF (JD.EQ.2) THEN
  255              WRITE(ILPFIL,9520) 'DAMP    X+'
  256            ELSEIF (JD.EQ.3) THEN
  257              WRITE(ILPFIL,9520) 'DAMP    Y-'
  258            ELSEIF (JD.EQ.4) THEN
  300          ENDIF
  301        ENDIF
  302        IF (LEQT.NE.0) THEN
  303          IF (ISCMT.EQ.0) THEN
  304            WRITE(ILPFIL,9540) '      T-DNR [-] =',SCMT
  305          ENDIF
  306        ENDIF
  307        DO 300 LC=1,LEQC
  308          IF (ISCMC(LC).EQ.0) THEN
  309            WRITE(ILPFIL,9540) '      C-DNR [-] =',SCMC(LC)
  310          ENDIF
  311   300  CONTINUE
  312        IF (ICGTYP.EQ.0) THEN
  313          WRITE(ILPFIL,9520) 'MTRX  TYPE      = ILU-BCGSTAB'
  314        ELSE
  315          WRITE(ILPFIL,9520) 'MTRX  TYPE      = MILU-BCGSTAB'
  316          WRITE(ILPFIL,9540) '      PARAM [-] =',CGPARA
  317        ENDIF
  318        WRITE(ILPFIL,9530) '      I-MAX [-] =',ICGMAX
  319        WRITE(ILPFIL,9540) '      A-ERR [-] =',CGEPSA
  320        WRITE(ILPFIL,9540) '      R-ERR [-] =',CGEPSR
  323        WRITE(ILPFIL,9510) '-- FILE CONTROL --'
  324        IF (IRETYP.LT.0) THEN
  325          WRITE(ILPFIL,9520) 'RES             = NOT READ'
  326        ELSE
  327          WRITE(ILPFIL,9520) 'RES   TYPE      = BY STEP'
  328          WRITE(ILPFIL,9530) '      START [-] =',IRETYP
  329        ENDIF
  330        IF (ILPTYP.EQ.0) THEN
  331          WRITE(ILPFIL,9520) 'L/P   TYPE      = NOT WRITE'
  332        ELSE
  333          IF (ILPTYP.EQ.1) THEN
  334            WRITE(ILPFIL,9520) 'L/P   TYPE      = BY STEP'
  335            WRITE(ILPFIL,9530) '      START [-] =',ILPTRN(1)
  336            WRITE(ILPFIL,9530) '      END   [-] =',ILPTRN(2)
  337            WRITE(ILPFIL,9530) '      DELTA [-] =',ILPTRN(3)
  338          ELSE
  339            WRITE(ILPFIL,9520) 'L/P   TYPE      = BY TIME'
  340            WRITE(ILPFIL,9540) '      START [S] =',RLPTRN(1)
  341            WRITE(ILPFIL,9540) '      END   [S] =',RLPTRN(2)
  342            WRITE(ILPFIL,9540) '      DELTA [S] =',RLPTRN(3)
  343          ENDIF
  344          IF     (ILPARA(1).EQ.1) THEN
  345            WRITE(ILPFIL,9530) '      XY    [-] =',(ILPARA(I)-1,I=2,3)
  346          ELSEIF (ILPARA(1).EQ.2) THEN
  347            WRITE(ILPFIL,9530) '      XZ    [-] =',(ILPARA(I)-1,I=2,3)
  348          ELSEIF (ILPARA(1).EQ.3) THEN
  349            WRITE(ILPFIL,9530) '      YZ    [-] =',(ILPARA(I)-1,I=2,3)
  350          ELSEIF (ILPARA(1).EQ.4) THEN
  351            WRITE(ILPFIL,9530) '      YX    [-] =',(ILPARA(I)-1,I=2,3)
  352          ELSEIF (ILPARA(1).EQ.5) THEN
  353            WRITE(ILPFIL,9530) '      ZX    [-] =',(ILPARA(I)-1,I=2,3)
  354          ELSEIF (ILPARA(1).EQ.6) THEN
  355            WRITE(ILPFIL,9530) '      ZY    [-] =',(ILPARA(I)-1,I=2,3)
  356          ENDIF
  357        ENDIF
  358        IF (IGRTYP.EQ.0) THEN
  359          WRITE(ILPFIL,9520) 'GRP   TYPE      = NOT WRITE'
  360        ELSE
  361          IF (IGRTYP.EQ.1) THEN
  362            WRITE(ILPFIL,9520) 'GRP   TYPE      = BY STEP'
  363            WRITE(ILPFIL,9530) '      START [-] =',IGRTRN(1)
  364            WRITE(ILPFIL,9530) '      END   [-] =',IGRTRN(2)
  365            WRITE(ILPFIL,9530) '      DELTA [-] =',IGRTRN(3)
  366          ELSE
  367            WRITE(ILPFIL,9520) 'GRP   TYPE      = BY TIME'
  368            WRITE(ILPFIL,9540) '      START [S] =',RGRTRN(1)
  369            WRITE(ILPFIL,9540) '      END   [S] =',RGRTRN(2)
  370            WRITE(ILPFIL,9540) '      DELTA [S] =',RGRTRN(3)
  371          ENDIF
  372          IF (IGRARA(1).LE.1) IGRARA(1)=2
  373          IF (IGRARA(2).LE.1) IGRARA(2)=2
  374          IF (IGRARA(3).LE.1) IGRARA(3)=2
  375          IF (IGRARA(4).LE.1) IGRARA(4)=NUMI0-1
  376          IF (IGRARA(5).LE.1) IGRARA(5)=NUMJ0-1
  377          IF (IGRARA(6).LE.1) IGRARA(6)=NUMK -1
  378          WRITE(ILPFIL,9530) '      AREA1 [-] =',(IGRARA(I)-1,I=1,3)
  379          WRITE(ILPFIL,9530) '      AREA2 [-] =',(IGRARA(I)-1,I=4,6)
  380          L=0
  381          IF (IGRARA(1).EQ.IGRARA(4)) L=L+1
  382          IF (IGRARA(2).EQ.IGRARA(5)) L=L+1
  383          IF (IGRARA(3).EQ.IGRARA(6)) L=L+1
  384          IF (L.GE.2) CALL VF_A2ERR('VF_OL1INI','INVALID VALUE.')
  385        ENDIF
  386        IF (IRSTYP.EQ.0) THEN
  387          WRITE(ILPFIL,9520) 'RSL   TYPE      = NOT WRITE'
  388        ELSE
  389          IF (IRSTYP.EQ.1) THEN
  390            WRITE(ILPFIL,9520) 'RSL   TYPE      = BY STEP'
  391            WRITE(ILPFIL,9530) '      START [-] =',IRSTRN(1)
  392            WRITE(ILPFIL,9530) '      END   [-] =',IRSTRN(2)
  393            WRITE(ILPFIL,9530) '      DELTA [-] =',IRSTRN(3)
  394          ELSE
  395            WRITE(ILPFIL,9520) 'RSL   TYPE      = BY TIME'
  396            WRITE(ILPFIL,9540) '      START [S] =',RRSTRN(1)
  397            WRITE(ILPFIL,9540) '      END   [S] =',RRSTRN(2)
  398            WRITE(ILPFIL,9540) '      DELTA [S] =',RRSTRN(3)
  399          ENDIF
  400        ENDIF
  401        IF (ITRTYP.EQ.0) THEN
  402          WRITE(ILPFIL,9520) 'TRN   TYPE      = NOT WRITE'
  403        ELSE
  404          IF (ITRTYP.EQ.1) THEN
  405            WRITE(ILPFIL,9520) 'TRN   TYPE      = BY STEP'
  406            WRITE(ILPFIL,9530) '      START [-] =',ITRTRN(1)
  407            WRITE(ILPFIL,9530) '      END   [-] =',ITRTRN(2)
  408            WRITE(ILPFIL,9530) '      DELTA [-] =',ITRTRN(3)
  409          ELSE
  410            WRITE(ILPFIL,9520) 'TRN   TYPE      = BY TIME'
  411            WRITE(ILPFIL,9540) '      START [S] =',RTRTRN(1)
  412            WRITE(ILPFIL,9540) '      END   [S] =',RTRTRN(2)
  413            WRITE(ILPFIL,9540) '      DELTA [S] =',RTRTRN(3)
  414          ENDIF
  415        ENDIF
  416        IF     (IPRNT.EQ.0) THEN
  417          WRITE(ILPFIL,9520) 'PORO  TYPE      = NOT READ'
  418        ELSEIF (IPRNT.EQ.1) THEN
  419          WRITE(ILPFIL,9520) 'PORO  TYPE      = CONST'
  420        ELSE
  467        WRITE(ILPFIL,9530) 'NUMBER OF GRID-X =',NUMI-1
  468        WRITE(ILPFIL,9550) 'I','X','DX','CX'
  469        DO 500 I=1,NUMI
  470          WRITE(ILPFIL,9560) I-1+IP,(XX(L,I),L=1,3)
  471   500  CONTINUE
  472        WRITE(ILPFIL,9530) 'NUMBER OF GRID-Y =',NUMJ-1
  473        WRITE(ILPFIL,9550) 'J','Y','DY','CY'
  474        DO 510 J=1,NUMJ
  475          WRITE(ILPFIL,9560) J-1+JP,(YY(L,J),L=1,3)
  476   510  CONTINUE
  477        WRITE(ILPFIL,9530) 'NUMBER OF GRID-Z =',NUMK-1
  478        WRITE(ILPFIL,9550) 'K','Z','DZ','CZ'
  479        DO 520 K=1,NUMK
  480          WRITE(ILPFIL,9560) K-1   ,(ZZ(L,K),L=1,3)
  481   520  CONTINUE
  507        IF (ILPON(6).NE.0 .AND. IPRNT.LE.1) THEN
  508          WRITE(ILPFIL,9510) '<<GLV>>'
  509          CALL VF_OL3DR(GLV,0)
  510          WRITE(ILPFIL,9510) '<<GLX>>'
  511          CALL VF_OL3DR(GLX,1)
  512          WRITE(ILPFIL,9510) '<<GLY>>'
  513          CALL VF_OL3DR(GLY,1)
  514          WRITE(ILPFIL,9510) '<<GLZ>>'
  515          CALL VF_OL3DR(GLZ,1)
  516        ENDIF
```

#### 3D vf_ol1trn.f

```text
  113        IF (ILPON(7).NE.0) THEN
  114          WRITE(ILPFIL,9510) 'NF',NNOW,TNOW
  115          CALL VF_OL3DNF(NF)
  116        ENDIF
  117  
  118  CD    -- 空気圧の計算用インデックスを出力する --
  119        IF (ILPON(20).NE.0 .AND. PVCP0.GE.ZERO) THEN
  120          WRITE(ILPFIL,9510) 'IPVC',NNOW,TNOW
  121          CALL VF_OL3DI(IPVC,0)
  143          CALL VF_OL3DR(PP,0)
  147        IF (ILPON(21).NE.0 .AND. PVCP0.GE.ZERO) THEN
  148          WRITE(ILPFIL,9510) 'PPPVC',NNOW,TNOW
  149          CALL VF_OL3DR(PPPVC,0)
  170  CD    -- 分子動粘性係数と渦動粘性係数の和を出力する --
  171        IF (ILPON(11).NE.0) THEN
  172          WRITE(ILPFIL,9510) 'VISC',NNOW,TNOW
  173          CALL VF_OL3DR(ANU,0)
```

#### 3D vf_ol3dr.f

```text
   33          IF (ILPARA(2).EQ.1) THEN
   34            M1=1
   35            M2=0
```

#### 3D vf_or1trn.f

```text
  105        WRITE(IRSFIL,ERR=9010) NNOW,TNOW,DTNOW
```

#### 3D vf_ot1ini.f

```text
   29        OPEN(MFILTR,ERR=9010,
   30       &     FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.tran',
   31       &     STATUS='NEW',FORM='FORMATTED' )
   35        DO 100 L=1,ITRNUM
```

#### 3D vf_ot1trn.f

```text
   94              CALL VF_CWLVL(ZZ,FF,RTRVAL(L),NF,ITRPRM(3,L),ITRPRM(4,L))
  333        IF (MYRANK.EQ.0) WRITE(ITRFIL,9510) TNOW,(RTRVAL(L),L=1,ITRNUM)
```

#### 3D vf_pmginp.f

```text
   25          OPEN(MFILEN,ERR=9010,FILE='data.env',
   26       &         STATUS='OLD',FORM='FORMATTED' )
   27          IENFIL=MFILEN
   28          READ(IENFIL,*,END=9020,ERR=9020) MGARAN
   29          IF (MGARAN.GT.MAXPRO) GOTO 9030
   30          IF (MGARAN.LE.0     ) GOTO 9040
   31          N=0
   32          DO 120 I=1,MGARAN
   33            READ(IENFIL,*,END=9020,ERR=9020) MGNAME(I),MGNPIN(I),MGPARE(I)
```

#### 3D vf_sconvd.f

```text
   86                ELSEIF (INDBC(IND).GE.1) THEN
   87                  FLC=WIN*BCC(IND)
```


#### 3D vf_veuler.f

```text
  127                IF (UU(I,J,K).GT. VVMAX) UU(I,J,K)= VVMAX
  128                IF (UU(I,J,K).LT.-VVMAX) UU(I,J,K)=-VVMAX
```

#### 3D vf_vgene.f

```text
  112                  IF (GV.LE.PLOWER .OR. CD.LE.DRGDR(1)) THEN
  113                    RN=PLOWER
  114                    DR=DRGDR(1)
  115                    AP=0.0D0
  116                    BT=0.0D0
  117                  ELSE
  118                    RN=GV
  119                    DR=CD
  120                    AP=DRGAP(IDRGN)
  121                    BT=DRGBT(IDRGN)
  122                    DO 150 L=2,IDRGN
  123                      IF (DR.LE.DRGDR(L)) THEN
  124                        AP=DRGAP(L-1)
  125                        BT=DRGBT(L-1)
  126                        GOTO 160
  131                  YU =DRGYU
  133                  ALPHAX=AP*RN1*RN1*RN1*YU/(RN*RN*DR*DR)
  134                  BETAX =BT*RN1/(RN*RN*RN*DR)
  318                DR=0.0D0
  319                IF (LEQT.NE.0) THEN
  320                  T=ZZ(6,K)*(ZZ(2,K)*TT(I,J,K1)+ZZ(2,K1)*TT(I,J,K))
  321                  DR=DR-TDR0*(T-TDT0)
  322                ENDIF
  323                DO 300 LC=1,LEQC
  324                  C=ZZ(6,K)*(ZZ(2,K)*CC(I,J,K1,LC)+ZZ(2,K1)*CC(I,J,K,LC))
  325                  DR=DR-CDR0(LC)*(C-CDC0(LC))
  326   300          CONTINUE
  327                QW(I,J,K)=QW(I,J,K)-GV*GRZ0*DR/RHO0
```

#### 3D vf_zgetln.f

```text
   80          IF (ION.EQ.0 .AND. TEXT(I:I).NE.' ') ION=I
   81          IF (ICM.EQ.0 .AND. TEXT(I:I).EQ.'#') ICM=I
   82   200  CONTINUE
   83        IF (ION.EQ.0  ) GOTO 9000
   84        IF (ION.EQ.ICM) GOTO 9000
   87        IF (ICM.EQ.0) ICM=NC+1
   88        TEXT=TEXT(ION:ICM-1)
   89        CALL VF_ZSTOWS(IS,IE,MWD,NWD,TEXT(1:ICM-ION))
```


#### 3D vf_im2inp.f

```text
   44          OPEN(MFILMT2,ERR=9010,
   45       &       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.mtb2',
   46       &       STATUS='OLD',FORM='FORMATTED'  )
   47          IMTFIL2=MFILMT2
   61        IF     (TEXT(IS(IP):IE(IP)).EQ.'LEVEL-ON'  ) THEN
   62          MTBTYP2=1
   63        ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'LEVEL-OFF' ) THEN
   64          MTBTYP2=2
   65        ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'LEVEL-ONLY') THEN
   66          MTBTYP2=3
```

#### 3D vf_om1ini.f

```text
   28        DIMENSION XX(MAXG1,NUMI),YY(MAXG1,NUMJ),ZZ(MAXG1,NUMK)
   29        DIMENSION GGV(NUMI,NUMJ,NUMK)
   30        DIMENSION NF(NUMI,NUMJ,NUMK)
   31        REAL WK01(2:NUMI-1,2:NUMJ-1,NUMK)
  130        IF (NPROCS.EQ.1) THEN
  131          OPEN(MFILMM,ERR=9010,
  132       $       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.ma',
  133       &       STATUS='NEW',FORM='UNFORMATTED' )
  134        ELSE
  135          WRITE(TEXTP,'(I5.5)') MYRANK
  136          OPEN(MFILMM,ERR=9010,
  137       $       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.ma'//TEXTP,
  138       &       STATUS='NEW',FORM='UNFORMATTED' )
  139        ENDIF
  140        IMMFIL=MFILMM
  141        WRITE(ILPFIL,9510)
  142  
  143  CD    -- セル数を出力 --
  144        WRITE(IMMFIL,ERR=9020) NUMI-2,NUMJ-2
  145  
  146  CD    -- 格子座標を出力 --
  147        WRITE(IMMFIL,ERR=9020) (XX(1,I),I=2,NUMI)
  148        WRITE(IMMFIL,ERR=9020) (YY(1,J),J=2,NUMJ)
  149  
  150  CD    -- 標高の出力 --
  151        WRITE(IMMFIL,ERR=9020)
  152       &             ((WK01(I,J,1),I=2,NUMI-1),J=2,NUMJ-1)
```

#### 3D vf_om1trn.f

```text
   39        REAL WK01(2:NUMI-1,2:NUMJ-1,NUMK)
   40        REAL TIMWK
   73        DO 120 J=2,NUMJ-1
   74          DO 110 I=2,NUMI-1
   75            DWK=0.0D0
   76            UWK=0.0D0
   77            VWK=0.0D0
   78            DO 100 K=2,NUMK-1
   79              IF (NF(I,J,K).NE.-1) THEN
   80                ZF=GGV(I,J,K)*FF(I,J,K)*ZZ(2,K)
   81                DWK=DWK+ZF
   82                UWK=UWK+(UU(I,J,K)+UU(I+1,J,K))*ZF
   83                VWK=VWK+(VV(I,J,K)+VV(I,J+1,K))*ZF
   84              ENDIF
   85   100      CONTINUE
   86            WK01(I,J,1)=REAL(DWK)
   87            WK01(I,J,2)=REAL(UWK*0.5D0)
   88            WK01(I,J,3)=REAL(VWK*0.5D0)
  120        WRITE(IMMFIL,ERR=9010) REAL(TNOW)
  121  
  122  CD    -- 水深等の出力 --
  123        WRITE(IMMFIL,ERR=9010)
  124       &             ((WK01(I,J,1),I=2,NUMI-1),J=2,NUMJ-1)
  125        WRITE(IMMFIL,ERR=9010)
  126       &             ((WK01(I,J,2),I=2,NUMI-1),J=2,NUMJ-1)
  127        WRITE(IMMFIL,ERR=9010)
  128       &             ((WK01(I,J,3),I=2,NUMI-1),J=2,NUMJ-1)
```

#### 3D vf_zseti1.f

```text
   16        DIMENSION IA(N)
   17  
   18  C==== 実行 ===========================================================
   19  
   20  CD    -- 配列の全要素に代入 --
   21        DO 100 I=1,N
   22          IA(I)=IVAL
   23   100  CONTINUE
```

#### 3D Makefile

```text
   10  FC = mpif90
   11  FFLAGS = -O -fpconstant
```

#### 3D2F vf_a1main.f

```text
   33  C----------------------------------------------------------2016.09 start
   34        INCLUDE 'VF_ASEABT.h'
   35  C----------------------------------------------------------2016.09 end
  313        ELSE
  314          WRITE(TEXTP,'(I5.5)') MYRANK
  315  C----------------------------------------------------for MG/2FC coupling
  316  C       OPEN(MFILLP,ERR=9010,FILE='data.list'//TEXTP,
  317          OPEN(MFILLP,ERR=9010,
  318       &       FILE=TRIM(MGNAME(MGRANK+1))//'.list'//TEXTP,
  319  C----------------------------------------------------for MG/2FC coupling
  320       &       STATUS='NEW',FORM='FORMATTED'    )
```

#### 3D2F VF_AFILEI.h

```text
    1        COMMON /VF_AFILEI/ IINFIL,IMTFIL,IREFIL,IPRFIL,
    2       &                   ILPFIL,IGRFIL,IRSFIL,ITRFIL,ITPFIL,
    3       &                   IMMFIL,
    4       &                   ILPTYP,ILPTRN(3),ILPARA(3),ILPON(19),
    5       &                   IGRTYP,IGRTRN(3),IGRARA(6),IGRVOR,
    6       &                   IRSTYP,IRSTRN(3),IRETYP,
    7       &                   ITRTYP,ITRTRN(3),ITRNUM,ITRPRM(MAXTR1,MAXTR),
    8       &                   IMMTYP,IMMTRN(3),
    9       &                   IPRNT,IPRNB,IPRNP,IPRARA(6,MAXPRB),IPRIT,
   10       &                   MTBTYP,MTBTT,MTBZZ,MTBNOW
   11  
```

#### 3D2F vf_a2dflt.f

```text
  100        ILPTYP=0
  101        CALL VF_ZSETI1(ILPTRN,0,3)
  102        CALL VF_ZSETI1(ILPARA,1,3)
  103        CALL VF_ZSETI1(ILPON ,0,19)
```

#### 3D2F vf_ol1ini.f

```text
  222            WRITE(ILPFIL,9540) '  VELOCITY   [-]=',BCTYP(6,JD)
```

#### 3D2F vf_og1ini.f

```text
   52          WRITE(TEXTP,'(I5.5)') MYRANK
   53  C----------------------------------------------------for MG/2FC coupling
   54  C       OPEN(MFILGR,ERR=9010,FILE='data.grp'//TEXTP,
   55          OPEN(MFILGR,ERR=9010,FILE=TRIM(MGNAME(MGRANK+1))//'.grp'//TEXTP,
   56  C----------------------------------------------------for MG/2FC coupling
   57       &       STATUS='NEW',FORM='UNFORMATTED' )
```

## 3 코드에만 있는 처리

이 절의 “문서 없음”은 p.101–150에 같은 세부 설명이 없다는 뜻이다. 앞 장 전체의 미기재를 뜻하지 않는다. 입력 읽기·기본값·관련 출력 경로만 대상으로 삼았다. 이 절의 모든 행은 판정 `코드에만`이며 결론 C이다. 기존 차이 행의 세부 근거를 반복할 때에는 해당 ID를 함께 적는다.

| 행 ID | 항목·문서 위치 | 코드(파일:줄 원문) | 문서에 추가할 사실 |
|---|---|---|---|
| KS3-301 | p.101 INDC 그림의 병렬 내부 범위 | `vf_cindc.f:26–32` `IB=NUMI` / `JA=1` / `JB=NUMJ` / `IF (MYMIS.EQ.1) IA=2` / `IF (MYMIE.EQ.1) IB=NUMI-1` / `IF (MYMJS.EQ.1) JA=2` / `IF (MYMJE.EQ.1) JB=NUMJ-1` | 물리 경계에서만 끝 셀을 제외한다. 내부 병렬 경계의 통신 셀은 그림의 단순 2…N−1 범위와 구분한다. |
| KS3-302 | p.108 PARALLEL 추가 검사 | `vf_iipara.f:33–34` `IF (NUMNPI.GE.MAXNPI)`<br>`     &                CALL VF_A2ERR('VF_IIPARA','AREA IS FULL.')`; `vf_cpara.f:39–40` `IF (IPROCS(I)-IPROCS(I-1).LT.2)`<br>`     &                      CALL VF_A2ERR('VF_CPARA','2 > IC2-IC1.')`; `:45–46` `IF (JPROCS(J)-JPROCS(J-1).LT.2)`<br>`     &                      CALL VF_A2ERR('VF_CPARA','2 > JC2-JC1.')`; `:59–60` `IF (NPROCS.NE.NUMNPI*NUMNPJ)`<br>`     &                CALL VF_A2ERR('VF_CPARA','NPROCS <> NPI*NPJ.')` | 각 분할 폭은 적어도 2셀이어야 한다. 프로세스 수는 방향별 수의 곱과 같아야 한다. |
| KS3-303 | p.109 AUTO 증가 한도 | `vf_cdtcal.f:59` `DT=DTMAX/DTSAFE`; `:145–147` `W=DTNOW` / `IF (NNOW.EQ.0) W=DTINIT` / `DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)` | 다음 시간 간격은 이전 시간 간격의 1.20배 이하이다. 최소 시간 간격이 이 제한보다 크면 최소값을 우선한다. |
| KS3-304 | p.123 AUTO의 정상 종료 표지 | `vf_ii1inp.f:356–357` `IF (IRETYP.EQ.-999)`<br>`     &          CALL VF_A2ERR('VF_II1INP','CALCULATION END.')`; `vf_a1main.f:1149` `IF ( IE.EQ.1.AND.ETIME.LT.1.0D30 ) IEE=1`; `:1161–1164` `WRITE(MFILAR,'(I10,1X,F10.2)') -999,TNOW` / `CLOSE(MFILAR)` / `OPEN(IFLAR,FILE='stop_ars',STATUS='UNKNOWN')` / `CLOSE(IFLAR)` | 정상 종료이며 `ETIME.LT.1.0D30`이면 ars에 −999와 `stop_ars` 파일을 남긴다. 다음 AUTO는 최초 계산으로 되돌아가지 않고 종료 오류를 낸다. |
| KS3-305 | p.124–129 TIME 출력의 단계 선택 | `vf_ot1trn.f:66–72` `Cmod20130605        IF (TNOW.GE.RTRTRN(1)-ZERO .AND. TNOW.LE.RTRTRN(2)+ZERO) THEN` / `IF (TNOW.GE.RTRTRN(1)-0.5D0*DT .AND.`<br>`     $      TNOW.LE.RTRTRN(2)+0.5D0*DT) THEN` / `W=(TNOW+0.5D0*DT)-RTRTRN(4)` / `IF (W.GE.0.0D0) THEN` / `IO=1` / `RTRTRN(4)=RTRTRN(4)+DBLE(INT(W/RTRTRN(3))+1)*RTRTRN(3)` | 예약 시간에 보간한 결과를 출력하는 방식이 아니다. 다음 시간 간격의 절반을 이용하여 실제 단계의 결과를 선택한다. 20130605 변경 표지가 있다. |
| KS3-306 | p.104·123 재시작 시 방정식 검사 | `vf_ir1inp.f:154–160` `READ(IREFIL,ERR=9020) LN,LV,LP,LF,LK,LT,LS,LG,LD,L1` / `IF (LK.NE.LEQK)`<br>`     &    CALL VF_A2ERR('VF_IR1INP','INVALID EQUATION (K-EPS).')`<br>`      IF (LT.NE.LEQT)`<br>`     &    CALL VF_A2ERR('VF_IR1INP','INVALID EQUATION (TEMP).')`<br>`      IF (LS.NE.LEQC)`<br>`     &    CALL VF_A2ERR('VF_IR1INP','INVALID EQUATION (CONC).')` | 재시작 파일의 난류·온도·농도 활성 상태가 현재 입력과 같아야 한다. “대부분 변경 가능”에는 이 예외가 있다. |
| KS3-307 | p.130 DROP·표면 속도의 생략 기본값 | `vf_a2dflt.f:45,151` `IBSUW0=0` / `IDROP=1`; `vf_iiopt.f:51–52,70–71` `ELSEIF (TEXT(IS(3):IE(3)).EQ.'D2U=0') THEN` / `IBSUW0=0` / `ELSEIF (TEXT(IS(4):IE(4)).EQ.'FREE-RUNDOWN') THEN` / `IDROP=1` | 생략 시 표면 속도는 D2U=0이며 물방울 시간문은 FREE-RUNDOWN이다. p.138 예제는 전자를 보여 주지만 옵션 정의에는 기본값을 명시하지 않는다. |
| KS3-308 | p.113 STK-CND의 선택 기준 | `vf_csetup.f:103–110` `IF (D.GE.ZERO) WUS=GRZ0*H*T*T/D/D` / `IF (N.EQ.0) THEN` / `IF (WUS.LE.25.0D0) THEN` / `N=-2` / `ELSE` / `N=-1` / `ENDIF` / `IBCTYP(2,JD)=N` | Ursell 수가 25 이하이면 Stokes를 선택한다. 25보다 크면 cnoidal을 선택한다. |
| KS3-309 | p.131 DRAG-DF의 공극률 하한 분기 | `vf_vgene.f:112–116` `IF (GV.LE.PLOWER .OR. CD.LE.DRGDR(1)) THEN` / `RN=PLOWER` / `DR=DRGDR(1)` / `AP=0.0D0` / `BT=0.0D0` | 공극률이 PLOWER 이하이면 입경에 관계없이 두 저항계수를 0으로 둔다. DR 구간표만으로 동작 전체를 설명할 수 없다. |
| KS3-310 | p.128 AV·INT의 F 특례·면속도 | `vf_careap.f:156–158` `AR  =XX(2,I)*YY(2,J)*ZZ(2,K)*GGV(I,J,K)` / `VAV =VAV +AR` / `VINT=VINT+AR*FF(I,J,K)`; 속도는 `:88` `VINT=VINT+AR*(P1+P2)*0.5D0` | F는 장애물이 아닌 셀의 공극 체적으로 가중한다. 일반 스칼라·속도는 물 체적으로 가중한다. 속도 적분은 양쪽 면속도의 평균을 쓴다. |
| KS3-311 | p.144 매트릭스의 증가순·초기 위상 검사 | `vf_im1inp.f:101–102` `IF (DMTBT0.LT.0.0D0 .OR. DMTBT0.GT.1.0D0)`<br>`     &                CALL VF_A2ERR('VF_IM1INP','INVALID VALUE.')`; `:118–119` `IF (DMTBZZ(K).LE.DMTBZZ(K-1))`<br>`     &                 CALL VF_A2ERR('VF_IM1INP','INVALID VALUE.')`; `:145–146` `IF (DMTBTT(I).LE.DMTBTT(I-1))`<br>`     &                    CALL VF_A2ERR('VF_IM1INP','INVALID VALUE.')` | z좌표와 위상 자료는 각각 엄격 증가순이다. 초기 위상도 0…1을 요구한다. |
| KS3-312 | p.145 .poro의 추가 범위·하한 처리 | `vf_ip1inp.f:42` `IF (IPRNB.GT.MAXPRB) CALL VF_A2ERR('VF_IP1INP','AREA IS FULL.')`; `:94` `GGVNOW(L)=MAX(GGVNOW(L),PLOWER)` | 블록 수는 MAXPRB를 넘지 못한다. 읽은 공극률은 PLOWER 이상으로 바꾼다. |
| KS3-313 | p.146 면 투과율의 경계 예외 | `vf_cggxyz.f:74–77` `IF     (INDX(IW,JW,K).EQ.-1) THEN` / `GGX(IW,JW,K)=1.0D0` / `ELSEIF (INDX(IW,JW,K).EQ. 0) THEN` / `GGX(IW,JW,K)=MIN(GGV(IW,JW,K),GGV(IW-1,JW,K))` | 두 셀 최소값 규칙은 일반 내부 면에 적용한다. 장애물 내부 면은 1이며 경계면의 지정 투과율은 이 분기에서 덮어쓰지 않는다. Y·Z도 같다. |
| KS3-314 | p.146 환경 파일 검사 | `vf_pmginp.f:29–30,43,45–46,51–52` `IF (MGARAN.GT.MAXPRO) GOTO 9030` / `IF (MGARAN.LE.0     ) GOTO 9040` / `IF (MGNPIN(I).LE.0     ) GOTO 9040` / `IF (MGPARE(I).GT.MGARAN) GOTO 9040` / `IF (MGPARE(I).EQ.I     ) GOTO 9040` / `IF (N.GT.MAXPRO) GOTO 9030` / `IF (N.NE.MGPROC) GOTO 9050`; `:75,82` `IF (N.GT.0) GOTO 9040` / `IF (MGNAME(I).EQ.MGNAME(L)) GOTO 9040` | 영역 수·PE 총수·부모 범위·자기 부모·부모 순환·중복 영역명을 검사한다. |
| KS3-315 | p.127–128 와도 출력의 셀 제한 | `vf_cvort.f:66,72` `VORT=0.0D0` / `IF (NF(I0,J0,K0).EQ.0) THEN` | 와도 계산은 완전 유체 셀에서 수행한다. 표면·기체·장애물 셀에는 초기 0을 남긴다. |
| KS3-316 | p.107 허용 키워드·대소문자 | `vf_ii1inp.f:178` `IF     (TEXT(IS(1):IE(1)).EQ.'PARALLEL') THEN`; `:410–413` `CD      -- 解釈できないヘッダーによるエラー --` / `ELSE` / `WRITE(ILPFIL,9520) (TEXT(IS(I):IE(I)),I=1,NWD)` / `CALL VF_A2ERR('VF_II1INP','UNKNOWN HEADER.')` | 일본어 주석 뜻은 “해석할 수 없는 헤더 오류”이다. 문자열 비교는 대소문자를 구분한다. 소문자 명령을 대문자로 바꾸는 처리는 없다. |
| KS3-317 | p.116–117 GRID 내부 검사 예외 | `vf_iigrid.f:76–77` `IF (TEXT(IS(I):IE(I)).EQ.'END') THEN` / `IF (I.NE.NWD) CALL VF_A2ERR('VF_IIGRID','SYNTAX ERROR.')`; `:108` `IF (IEOF.NE.0) CALL VF_A2ERR('VF_IIGRID','NOT FOUND (END).')` | END 뒤 추가 단어를 금지한다. END를 만나기 전 EOF이면 오류이다. KS3-024의 근거이다. |
| KS3-318 | p.112 MATRIX2와 p.144 파일 설명 사이의 별도 파일 | `vf_im2inp.f:44–47` `OPEN(MFILMT2,ERR=9010,`<br>`     &       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.mtb2',`<br>`     &       STATUS='OLD',FORM='FORMATTED'  )`<br>`        IMTFIL2=MFILMT2`; `:61–66` `IF     (TEXT(IS(IP):IE(IP)).EQ.'LEVEL-ON'  ) THEN` / `MTBTYP2=1` / `ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'LEVEL-OFF' ) THEN` / `MTBTYP2=2` / `ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'LEVEL-ONLY') THEN` / `MTBTYP2=3` | MATRIX2는 `.mtb2`를 읽는다. p.144는 `.mtb`만 설명한다. 두 파일은 각자 LEVEL-ON·LEVEL-OFF·LEVEL-ONLY를 읽는다. 파일 번호는 `VF_A0PRM.h:10–11`의 MFILMT=12와 MFILMT2=15이다. |
| KS3-319 | p.118–119에 없는 공간장 초기값 | `vf_a1main.f:501–506` `CALL VF_ZSETR3(CM0 ,0.0D0,NUMI,NUMJ,NUMK)` / `CALL VF_ZSETR3(CD0 ,0.0D0,NUMI,NUMJ,NUMK)` / `CALL VF_ZSETR3(GGV ,1.0D0,NUMI,NUMJ,NUMK)` / `CALL VF_ZSETR3(GGX ,1.0D0,NUMI,NUMJ,NUMK)` / `CALL VF_ZSETR3(GGY ,1.0D0,NUMI,NUMJ,NUMK)` / `CALL VF_ZSETR3(GGZ ,1.0D0,NUMI,NUMJ,NUMK)` | POROUS 명령을 대입하기 전 관성·저항계수는 0이다. 공극률과 세 면 투과율은 1이다. 표의 각 직사각형 입력 인수에 기본값이 없다는 사실과 전체 공간장의 초기값을 구분한다. |
| KS3-320 | p.129 MAM 출력 파일명·레코드 | `vf_om1ini.f:131–138` 단일 프로세스 `OPEN(MFILMM,ERR=9010,`<br>`     $       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.ma',`<br>`     &       STATUS='NEW',FORM='UNFORMATTED' )`; 병렬 `WRITE(TEXTP,'(I5.5)') MYRANK` / `OPEN(MFILMM,ERR=9010,`<br>`     $       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.ma'//TEXTP,`<br>`     &       STATUS='NEW',FORM='UNFORMATTED' )`; `:144,147–148` `WRITE(IMMFIL,ERR=9020) NUMI-2,NUMJ-2` / `WRITE(IMMFIL,ERR=9020) (XX(1,I),I=2,NUMI)` / `WRITE(IMMFIL,ERR=9020) (YY(1,J),J=2,NUMJ)`; `vf_om1trn.f:39` `REAL WK01(2:NUMI-1,2:NUMJ-1,NUMK)`; `:86–88` `WK01(I,J,1)=REAL(DWK)` / `WK01(I,J,2)=REAL(UWK*0.5D0)` / `WK01(I,J,3)=REAL(VWK*0.5D0)`; `:120` `WRITE(IMMFIL,ERR=9010) REAL(TNOW)` | p.129는 출력 예약만 설명한다. 코드는 `.ma` 또는 `.ma`+5자리 PE 번호를 쓴다. 초기 레코드는 수평 셀 수·격자 좌표·지표고이다. 단계 레코드는 단정밀도 시간·수심·수심 적분 속도 두 성분이다. 좌표 레코드는 배정밀도이다. 지표고·수심·수심 적분 속도는 REAL WK01 배열로 쓴다. `:80–83`의 ZF 가중합에는 수심으로 나누는 연산이 없다. |

## 4 노트 대조와 수정안

아래 수정안은 지정 보고서에만 기록했다. 현재 노트 파일을 수정하지 않았다. 지배식의 앞 장 대조는 이번 범위가 아니므로 해당 식의 기존 판정은 바꾸지 않는다.

| 행 ID | 현재 노트(파일:줄 원문) | 대조 결과 | 노트 수정안 |
|---|---|---|---|
| KS3-401 | `models/CADMAS-SURF/source-analysis/cadmas-surf3d-turbulence-and-porous-resistance.md:81` 원문 발췌 ``가 입력파일 키워드 `'CM0'`/`'CD0'`(`vf_iifile.f:101-103`)로 설정.`` | 불일치. CM0·CD0는 FILE L/P 출력 선택 문자열이다. `vf_iiporo.f:191,219`의 실제 입력은 CM·CD이다. B. | “관성계수는 `POROUS CM`으로 입력한다. 저항계수는 `POROUS CD`로 입력한다. `FILE L/P ON CM0`와 `FILE L/P ON CD0`는 목록 출력을 선택한다. DRAG-DF를 켜면 CD0를 입경 m으로 해석한다(3D manual p.118–119·131; vf_iiporo.f:191–239; vf_iifile.f:101–104).” |
| KS3-402 | `models/CADMAS-SURF/source-analysis/cadmas-surf3d-vof-free-surface.md:66` 원문 발췌 ``셀체적 `V=Δx·Δy·Δz·GGV`(`:40`):``; `:69` 원문 발췌 `` `FSUM += F*V`(클리핑 후, `:48`)``; `:71` `클리핑이 주입/제거한 유체체적` | 일치. KS3-233은 문서의 면적 설명을 고친다. | “FSUM은 절단 후 물 체적의 전역 합이다. FCUT는 `(절단 전 F−절단 후 F)×공극 체적`의 전역 합이다. FCUT의 양수는 절단으로 제거한 물 체적이다. 음수는 절단으로 추가한 물 체적이다(vf_fcut01.f:40–56).” |
| KS3-403 | `models/CADMAS-SURF/source-analysis/cadmas-surf3d-stier-and-auxiliary-physics.md:25` 원문 발췌 `` `vf_iifile`(FILE 출력제어 `:35-249`)``; 같은 줄 `물리 없음.` | 불일치. 현재 파일은 488행이며 PORO 읽기 옵션까지 포함한다. C. 해석: 파서는 물리 방정식을 적분하지 않지만 이 설명에는 파일별 형식·검사·보간 연결이 빠졌다. | “FILE 파서는 vf_iifile.f:33–474에서 L/P·GRP·RSL·TRN·MAM·PORO를 읽는다. RES·OBS는 vf_ii1inp.f:335–375에서 먼저 읽는다. 매트릭스 자료의 증가순 검사와 공극률의 배정밀도 이진 읽기를 별도 설명한다(3D manual p.123–129·144–146).” |
| KS3-404 | 같은 노트 `:28` 원문 발췌 ``리스타트 `vf_or1*`·시계열 `vf_ot1*`. 직렬화만.`` | 불일치. 시계열 출력은 수위·와도·평균·적분·파력을 계산한다. C. | “시계열 출력은 지정 단계의 값을 선택한다. VF_OT1TRN은 VF_CWLVL·VF_CVORT·VF_CAREAP·VF_CFORCE를 호출한다. AV·INT는 물 체적과 공극 체적의 가중 규칙을 구분한다(vf_ot1trn.f:81–323; vf_careap.f:142–208).” |
| KS3-405 | `models/CADMAS-SURF/source-analysis/cadmas-surf3d-stier-and-auxiliary-physics.md:55` 원문 발췌 `갇힌 공기/2상 압력 효과`; `VOF 자유수면 위 폐쇄 공기영역 압력.` | 일치. 조파·방사·자유 경계에 닿으면 대기 개방이다. | “`OPTION PV=CONST PVCP0 PVCGM`은 닫힌 기포의 압력을 계산한다. 출력 압력은 대기압을 뺀 값이다. VP 코드4·5·7에 닿은 기포는 게이지 압력을 0으로 둔다(3D manual p.130–131; vf_fpvcpp.f:77·183–191).” |
| KS3-406 | `models/CADMAS-SURF/source-analysis/cadmas-surf3d-timestep-nesting-stoc-coupling.md:47` 원문 발췌 `` `data.env`에서 영역명·프로세스수·**親 영역번호** `MGPARE`(`:33`), 자기自身 親 금지(`:46`)`` | 일치. 영역 수·이름·파일명 설명을 보강할 수 있다. | “`data.env`의 첫 정수는 영역 수이다. 각 영역의 이름·PE 수·부모 번호가 뒤따른다. 공급 3D 코드의 병렬 목록 파일은 `<영역명>.list<5자리 PE>`이다. 매뉴얼 p.146의 `<영역명><6자리 PE>.list`와 다르다(vf_pmginp.f:25–52; vf_a1main.f:376–379).” |
| KS3-407 | `models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:23` 원문 발췌 `Ch2 Analytical model 발췌.`; `의 코드 발견을 식 단위로 확증 — 각 항목에 source 대조 표기.` | 일치. 이 노트는 p.101–150 입력·출력을 아직 설명하지 않는다. | 별도 절에 “Chapter 5 입력·출력 대조에서는 농도 성분 번호는 정수임을 확인했다. PORO의 GGV 레코드는 공급 코드에서 R*8이다. p.140의 제곱 노름 설명은 실제 2-노름과 다르다”를 추가한다. 근거는 KS3-046·234·251이다. |
| KS3-408 | `models/CADMAS-SURF/README.md:40` `코드 100% 포섭`; `:41` `26 PDF 전수` | 일치. 현재 파일에는 이 문구가 있다. 이 보고서는 파일 목록의 포섭률을 다시 계산하지 않았다. 해석: 이 문구를 항목별 문서·코드 일치 완료로 확대해서 읽으면 안 된다. | “소스·문서별 노트 목록을 구축했다. 문서 항목별 대조 범위는 각 비교 보고서에 적는다. 3D manual p.101–150의 대조 결과는 이 보고서 5절에 기록했다”를 보충한다. 기존 포섭률의 진위를 이번 대조만으로 판정하지 않는다. |
| KS3-409 | `models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md:105` 원문 발췌 `` `FCUT`(클리핑 질량오차)·`!VD!`(발산)·`!B!`/`!R!`(Poisson 잔차)`` | 불일치. FCUT는 밀도를 곱하지 않은 부호 있는 체적이다. !B!는 우변 벡터의 노름이다. !R!만 잔차 벡터의 노름이다. B. | “FCUT는 VOF 절단 전후 차이에 공극 체적을 곱한 전역 합이다. !VD!는 공극 면 유량 차 합의 전역 2-노름이다. !B!는 Poisson 우변의 2-노름이다. !R!는 최종 잔차의 2-노름이다(3D manual p.140의 용어 오기는 KS3-233–234; vf_fcut01.f:40–56; vf_cdiv00.f:43–56; vf_m1bcgs.f:249–250).” |

## 5 차이 결론

### 5.1 분류와 판 근거

이 절은 2절의 일치가 아닌 행과 3절의 코드 전용 행을 모두 분류한다. 이 절은 4절의 불일치 행도 분류한다. 같은 발견을 서로 다른 문서 위치에서 다룬 행은 각 ID를 유지한다. KS3-227과 KS3-279는 같은 출력 단위 결함 후보이다. 따라서 E의 행 수와 서로 다른 결함 후보 수는 다르다.

A는 문서와 배포 코드의 판 차이이다. p.135·143의 출력 예제는 `Ver. 1.0`이다. `3D VF_A0PRM.h:2`는 `PARAMETER (IVR001=  0, IVR002=  1,`로 시작한다. `3D vf_a1main.f:382`는 `WRITE(ILPFIL,9510) IVR001,IVR002`이다. `:1208–1209`는 `9510 FORMAT(/' ',`와 계속 줄 `     &       '##### CADMAS-SURF/3D-MG Ver.',I1,'.',I1,' START. ######')`이다. 배포 코드의 이 배너는 0.1이다. 같은 파일의 별도 `ver4.9.1` 진단 문자열을 이 배너 상수와 혼합하지 않는다.

`3D vf_a1main.f:33`은 `C----------------------------------------------------------2012.03 start`이다. `3D2F vf_a1main.f:33`은 `C----------------------------------------------------------2016.09 start`이다. 두 줄은 각 사본의 수정 구간 날짜 표지이다. 이 날짜를 프로그램 전체의 정식 발행일로 쓰지 않는다. KS3-005의 A는 서로 다른 문서·코드 판의 상한값을 구분하는 해석이다. `VF_A0PRM.h:5`의 주석 처리한 줄도 MAXNPI·MAXNPJ를 100으로 적는다. 10에서 100으로 바뀐 시점은 이 줄로 주장하지 않는다. 두 판 번호의 시간적 선후도 숫자 크기로 추정하지 않는다.

B는 문서 내부의 모순·오기·번역 오기이다. C는 대상 쪽이 생략한 코드 동작이다. 입력 의무와 입력 검사를 구분한다. KS3-112·209의 C는 문서 밖 입력의 허용 여부를 코드가 별도로 검사하지 않는다는 뜻이다. 문서가 요구한 V2·중앙 자오선 범위를 완화하여 권고하는 결론이 아니다. KS3-162·284도 검사와 오류 복귀의 예외를 기록한다.

D는 전체 Simulators 검색 후에도 구현을 찾지 못한 문서의 규칙이다. E는 정적 근거가 있는 코드 결함 후보이다. F는 같은 동작의 식·표기 차이이다. H는 사용 권고·실행 사례·도화 도구·서지처럼 코드 일치 판정의 대상이 아닌 항목이다. X는 외부 원문이 있어야 식·계수를 가를 수 있는 경우이다. 이번 대상에서는 외부 논문의 식·계수를 가져와야 판정할 행이 없다. 참고문헌 목록 자체는 H로 분류한다.

### 5.2 D의 전체 검색

검색 루트는 `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators` 전체이다. 검색은 `rg -n -i`로 수행했다. 검색 범위에는 네 시뮬레이터의 모든 하위 디렉터리를 포함했다. 검색을 위해 범위 밖 전후처리기 내부를 열지 않았다.

| 연결 행 | 검색어 | 결과 | 판정에 쓴 원문 |
|---|---|---|---|
| KS3-257 | `edata-ch000000` | 적중 0행, 종료 코드 1 | 문서 p.146의 `edata-ch000000.list` 예에 해당하는 파일명 문자열이 없다. 이 검색만으로 일반 파일명 규칙의 부재를 판정하지 않았다. |
| KS3-257 | `I6[.]6` | 적중 0행, 종료 코드 1 | 여섯 자리 정수 출력 형식을 찾지 못했다. 다음 파일명 결합 검색과 함께 판단했다. |
| KS3-257 | `TEXTP.*[.]list\|[.]list.*TEXTP` | 적중 3행, 종료 코드 0 | `3D vf_a1main.f:378` `     &       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.list'//TEXTP,`; `3D2F vf_a1main.f:316` `C       OPEN(MFILLP,ERR=9010,FILE='data.list'//TEXTP,`; `:318` `     &       FILE=TRIM(MGNAME(MGRANK+1))//'.list'//TEXTP,` |

검색어의 `\|`는 Markdown 표에서 파이프를 이스케이프한 것이다. 실제 rg 정규식은 `TEXTP.*[.]list`와 `[.]list.*TEXTP`의 OR이다. 두 활성 경로는 모두 확장자 뒤에 번호를 붙인다. `3D vf_a1main.f:376`과 `3D2F vf_a1main.f:314`의 실제 형식은 모두 `WRITE(TEXTP,'(I5.5)') MYRANK`이다. 도화 파일도 `3D vf_og1ini.f:49–52`와 `3D2F vf_og1ini.f:52–57`에서 같은 5자리 접미 규칙을 쓴다. 따라서 문서의 6자리·확장자 앞 번호 규칙을 현재 코드의 파일명으로 사용하면 안 된다.

### 5.3 E의 반대 근거와 강도

먼저 초기화 보정·의도 변경·사본 차이를 찾았다. 전체 Simulators의 `rg -n -i ILPON` 검색은 94행을 찾았다. 3D의 두 플래그를 초기화하는 별도 BLOCK DATA 또는 추가 대입 경로는 이 검색에 없다. `rg -n -i 'VELOCITY.*\[-\]'` 검색은 3D와 3D2F의 출력 라벨 두 행을 찾았다. 아래 후보는 모델 실행으로 재현하지 않았다.

| 후보 | 반대 근거를 먼저 확인한 결과 | 모순 근거 | 강도·실행 경로 |
|---|---|---|---|
| KS3-150: ILPON(20:21) 초기화 | `3D vf_iifile.f:135–138`의 IPVC·PPPVC 명시 ON/OFF는 두 플래그를 각각 설정한다. 두 명령을 주면 이 초기화 누락을 피한다. `3D vf_ol1trn.f:119,147`은 PVCP0가 ZERO 이상일 때만 두 값을 사용한다. 공급 Makefile의 `:10–11`은 `FC = mpif90`와 `FFLAGS = -O -fpconstant`이다. 명시적인 전체 정수 0 초기화 옵션은 없다. 로더가 COMMON 저장소를 0으로 채워 증상을 가릴 가능성은 실행 시험으로 확인하지 않았다. | `3D VF_AFILEI.h:4` `     &                   ILPTYP,ILPTRN(3),ILPARA(3),ILPON(21),`와 `:44` `CD    ILPON(21) : CNS : I*4 : リストファイルへの出力/非出力`는 배열 21개를 선언·설명한다. 주석 뜻은 “목록 파일 출력/미출력”이다. `3D vf_a2dflt.f:92` `CALL VF_ZSETI1(ILPON ,0,19)`는 19개만 지정한다. p.125는 `By default all quantities are non-output`이라고 적는다. 3D2F는 `VF_AFILEI.h:4`의 ILPON(19)와 `vf_a2dflt.f:103`의 초기화 19개가 서로 맞는다. | **중간**. 선언·자기 주석, 문서 기본값, 3D2F의 일관된 19개 경로가 근거이다. 환경의 암묵적인 0 초기화 때문에 실제 오출력을 단정하지 않는다. `3D vf_a1main.f:390` `CALL VF_A2DFLT()` 후 `:962`에서 VF_OL1TRN을 호출한다. 현재 실행 경로에서 호출되는 루틴이다. |
| KS3-227·279: 파속 단위 라벨 | `3D vf_csetup.f:139` `CALL VF_COMAK0(D,T,PI,GRZ0,WLN,N)` 후 `:143`은 `BCTYP(6,JD)=WLN/T`이다. 라벨 출력 전에 무차원화하는 나눗셈은 없다. `3D2F vf_ol1ini.f:222`도 `WRITE(ILPFIL,9540) '  VELOCITY   [-]=',BCTYP(6,JD)`이다. 단위만 바꾸려는 날짜 표지·보정 경로를 찾지 못했다. | `3D VF_APHYSR.h:73` `CD                             (6,*):波速`의 뜻은 “파속”이다. 파장 m을 주기 s로 나누므로 단위는 m/s이다. `3D vf_ol1ini.f:247`은 같은 값을 `[-]`로 출력한다. p.137의 70.9303/8.007=8.85853도 이 값이다. 자기 주석·단위·계산식과 출력 라벨이 모순이다. | **강함**. 결함 후보는 표시 단위이다. 파속 계산식의 수치 결함을 주장하지 않는다. `3D vf_a1main.f:790–793`의 VF_OL1INI 호출로 이 출력 경로에 도달한다. 현재 실행 경로에서 호출되는 루틴이다. |

### 5.4 행별 최종 결론

각 행에는 최종 분류 하나만 부여한다. 아래 표의 근거가 여러 원문 줄로 이어지면 2.14의 같은 파일 원문 블록에서 고정형식 연속 줄 전체를 확인할 수 있다.

| 행 ID | 항목 | 결론 | 근거(원문 인용) | 노트에 쓸 결론 문장 |
|---|---|---|---|---|
| KS3-003 | INDS의 J 설명 | B | `vf_fnfini.f:122` `INDS(NS)=I+NUMI*(J-1)+NUMI*NUMJ*(K-1)` | INDS는 I·J·K를 함께 부호화한 셀 번호이다. |
| KS3-005 | 방향별 프로세스 상한 | A | `VF_A0PRM.h:4–8` `C----------------------------------------------------------2011.04 start`<br>`C    &           MAXNPI= 100, MAXNPJ= 100, MAXBUF=  8,`<br>`     &           MAXNPI= 100, MAXNPJ= 100, MAXBUF=  9*2*4,`<br>`     &           MAXLIN= 50,`<br>`C----------------------------------------------------------2011.04 end` | 매뉴얼의 MAXNPI·MAXNPJ는 각 10이다. 공급 코드의 두 상한은 각 100이다. 두 판의 값을 구분하여 인용한다. |
| KS3-008 | MAXDR 변수명 | B | `VF_A0PRM.h:20` `     &           MAXDRG= 10,`; `:64` `CD    MAXDRG : PRM : I*4 : Dupuit-Forheimer式の係数の最大数` | 상수 이름은 MAXDRG이며 값은 10이다. |
| KS3-024 | 명령 끝 단어 무시의 예외 | C | 예: `vf_iitime.f:39` `IF (NWD.LT.4) CALL VF_A2ERR('VF_IITIME','SYNTAX ERROR.')`; 반례 `vf_iigrid.f:76–77` `IF (TEXT(IS(I):IE(I)).EQ.'END') THEN` / `IF (I.NE.NWD) CALL VF_A2ERR('VF_IIGRID','SYNTAX ERROR.')` | 일반 명령은 유효 인수 뒤 단어를 무시한다. GRID의 END 뒤 단어와 DRAG-DF 계수 행은 이 규칙의 예외이다. |
| KS3-029 | 농도 성분 수 NS/NC | B | `vf_iiequa.f:52–56` `ELSEIF (TEXT(IS(2):IE(2)).EQ.'CONCENTRATION') THEN` / `CALL VF_ZSTOI(LEQC,TEXT(IS(3):IE(3)))` / `IF (LEQC.LT.0    ) CALL VF_A2ERR('VF_IIEQUA','INVALID VALUE.')` / `IF (LEQC.GT.MAXNC) CALL VF_A2ERR('VF_IIEQUA','INVALID VALUE.')`; `vf_a2dflt.f:141` `LEQC =0` | 농도 방정식 설명의 NS는 NC로 고친다. |
| KS3-038 | GRZ0 이름 | B | `vf_iimate.f:48,50–51` `ELSEIF (TEXT(IS(2):IE(2)).EQ.'GRAVITY') THEN` / `CALL VF_ZSTOR(GRZ0,TEXT(IS(3):IE(3)))` / `IF (GRZ0.LT.0.0D0) CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')`; `vf_a2dflt.f:163` `GRZ0  =9.8D0` | 중력가속도 변수명은 GRZ0이다. |
| KS3-045 | 농도 확산계수 생략값 | C | `vf_iimate.f:72,74–79` `'DIFFUS'` / `CALL VF_ZSTOI(LC,TEXT(IS(3):IE(3)))` / `CALL VF_ZSTOR(SC,TEXT(IS(4):IE(4)))` / `IF (LC.LE.0 .OR. LC.GT.LEQC)`<br>`     &                  CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')`<br>`        IF (SC.LT.ZERO) CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')` / `CDF0(LC)=SC`; `vf_a2dflt.f:185` `CALL VF_ZSETR1(CDF0,0.0D0,MAXNC)` | MATE DIFFUS를 생략한 성분의 확산계수 초기값은 0이다. |
| KS3-046 | LC 자료형·범위 | B | `vf_iimate.f:74` `CALL VF_ZSTOI(LC,TEXT(IS(3):IE(3)))`; `:76–77` `IF (LC.LE.0 .OR. LC.GT.LEQC)`<br>`     &                  CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')` | LC는 I*4이다. 범위는 1부터 활성 농도 성분 수 NC까지이다. |
| KS3-048 | CINI 단위 | B | `vf_iimate.f:115,117–121` `'C'` / `CALL VF_ZSTOI(LC,TEXT(IS(4):IE(4)))` / `CALL VF_ZSTOR(SC,TEXT(IS(5):IE(5)))` / `CINI(LC)=SC`; `vf_a2dflt.f:184` `CALL VF_ZSETR1(CINI,0.0D0,MAXNC)` | CINI는 농도이며 이 표에서는 무차원이다. |
| KS3-049 | 다성분 부력 합 | C | `vf_vgene.f:318–327` `DR=0.0D0` / `DR=DR-TDR0*(T-TDT0)` / `DO 300 LC=1,LEQC` / `C=ZZ(6,K)*(ZZ(2,K)*CC(I,J,K1,LC)+ZZ(2,K1)*CC(I,J,K,LC))` / `DR=DR-CDR0(LC)*(C-CDC0(LC))` / `QW(I,J,K)=QW(I,J,K)-GV*GRZ0*DR/RHO0` | 부력의 농도 기여는 활성 성분 전체의 합이다. |
| KS3-050 | 파형 모델 중력 사용 의무 | H | 3D manual p.111 `The gravitational acceleration when using the wave form model shall be 9.8`. | 매뉴얼은 파형 모델 사용 시 중력가속도 9.8 m/s²를 요구한다. 이 문장은 사용 의무이다. |
| KS3-059 | 파고 HEIGHT 설명 | B | `vf_iimdl.f:78–82` `'HEIGHT'` / `CALL VF_ZSTOR(VAL,TEXT(IS(5):IE(5)))` / `IF (VAL.LT.ZERO) CALL VF_A2ERR('VF_IIMDL','INVALID VALUE.')` / `BCTYP(2,JD)=VAL`; `vf_csetup.f:65` `H =BCTYP (2,JD)` | HEIGHT의 H는 수심이 아니라 파고이다. |
| KS3-077 | 감쇠 차수·폭 권고 | H | 3D manual p.114 `The recommended value of the order of the attenuation function is 2`; `when the width of the region is two wavelengths`. | 매뉴얼은 감쇠 차수 2를 권고한다. 기본 감쇠계수 0.6은 감쇠 폭을 두 파장으로 둔 경우의 권고값이다. |
| KS3-083 | SCHMIDT의 LC 형 | B | `vf_iimdl.f:298` `CALL VF_ZSTOI(LC,TEXT(IS(4):IE(4)))` | SCHMIDT의 LC는 I*4이며 1부터 NC까지이다. |
| KS3-092 | C-DONOR의 LC 형 | B | `vf_iicomp.f:64,66–67` `CALL VF_ZSTOI(LC,TEXT(IS(4):IE(4)))` / `IF (LC.LE.0 .OR. LC.GT.LEQC)`<br>`     &                 CALL VF_A2ERR('VF_IICOMP','INVALID VALUE.')` | C-DONOR의 LC는 I*4이며 1부터 NC까지이다. |
| KS3-094 | 반복 수 이름 | B | `vf_iicomp.f:91,93–94` `'MAX-ITR'` / `CALL VF_ZSTOI(ICGMAX,TEXT(IS(4):IE(4)))` / `IF (ICGMAX.LT.0) CALL VF_A2ERR('VF_IICOMP','INVALID VALUE.')`; `vf_a2dflt.f:38` `ICGMAX=500` | 최대 반복 수의 이름은 ICGMAX이다. |
| KS3-100 | GRID 한 번 입력 | B | `vf_iigrid.f:46` `IF (NL.NE.0) CALL VF_A2ERR('VF_IIGRID','SECOND TIMES.')` | 각 방향의 GRID는 한 번만 입력한다. |
| KS3-105 | 공극률 하한 기본값 인쇄 | B | `vf_iiporo.f:52,54–56` `'LIM'` / `CALL VF_ZSTOR(PLOWER,TEXT(IS(3):IE(3)))` / `IF (PLOWER.LT.ZERO ) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')` / `IF (PLOWER.GT.1.0D0) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')`; `vf_a2dflt.f:59` `PLOWER=1.0D-4` | POROUS LIM의 기본값은 1.0D-4이다. |
| KS3-112 | V2 검사와 합성값 검사 | C | `vf_iiporo.f:75–78` `IF (V1 .LT.0.0D0) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')` / `IF (V1 .GT.1.0D0) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')` / `IF (VAL.LT.ZERO ) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')` / `IF (VAL.GT.1.0D0) CALL VF_A2ERR('VF_IIPORO','INVALID VALUE.')` | 코드는 V2 자체 대신 합성 후 VAL의 범위를 검사한다. 문서의 V2 범위 의무는 별도로 지켜야 한다. |
| KS3-123 | KC1 범위 조판 | B | `vf_iiboun.f:100` `     &      K1.LT.1  .OR. K2.GT.NUMK -2 .OR.`; 전체 조건은 KS3-122 | KC1의 제한은 1=<KC1=<KC2=<NK-1이다. 따로 인쇄한 1=는 제거한다. |
| KS3-126 | F FIX/FREE 설명 | B | `vf_iiboun.f:220,223,227,230–232` `'F'` / `'FIX'` / `CALL VF_ZSTOR(BF,TEXT(IS(IP):IE(IP)))` / `'FREE'` / `IB=2` / `BF=0.0D0` | F FIX는 VOF 값 고정 경계이다. F FREE는 VOF 자유 경계이다. |
| KS3-127 | BF 고정값 범위 | C | `vf_iiboun.f:228–229` `IF (BF.LT.0.0D0 .OR. BF.GT.1.0D0)`<br>`     &                   CALL VF_A2ERR('VF_IIBOUN','INVALID VALUE.')` | F FIX의 BF는 0 이상 1 이하이어야 한다. |
| KS3-131 | 농도 경계 LC 형 | B | `vf_iiboun.f:423–425` `CALL VF_ZSTOI(LC,TEXT(IS(IP):IE(IP)))` / `IF (LC.LE.0 .OR. LC.GT.LEQC)`<br>`     &                  CALL VF_A2ERR('VF_IIBOUN','INVALID VALUE.')` | 농도 경계의 LC는 I*4이며 1부터 NC까지이다. |
| KS3-145 | AUTO·ELAPSE 조합 권고 | H | 3D manual p.123 `It is preferable to use the function of AUTO in combination with specification of FILE RSL ELAPSE`. | 매뉴얼은 FILE RES AUTO를 FILE RSL ELAPSE와 함께 쓰기를 권한다. |
| KS3-150 | 공기압 출력 플래그 초기화 | E · 중간 | `vf_iifile.f:92–96` `ELSEIF (TEXT(IS(3):IE(3)).EQ.'ON' .OR.`<br>`     &          TEXT(IS(3):IE(3)).EQ.'OFF'    ) THEN` / `IF (TEXT(IS(3):IE(3)).EQ.'ON') ISW=1`; `vf_a2dflt.f:92` `CALL VF_ZSETI1(ILPON ,0,19)`; `VF_AFILEI.h:4` `     &                   ILPTYP,ILPTRN(3),ILPARA(3),ILPON(21),` | ILPON(20:21)의 명시적인 기본 초기화가 빠졌다. 실제 오출력 여부는 실행 환경에서 확인해야 한다. |
| KS3-152 | LAMBDA의 GLY 누락 | C | `vf_a1main.f:236` `DOUBLE PRECISION, DIMENSION(:,:,:), ALLOCATABLE :: GLV,GLX,GLY,GLZ`; LAMBDA 출력은 보충 원문 | LAMBDA는 GLV·GLX·GLY·GLZ 네 배열을 출력한다. |
| KS3-156 | GRP AREA 끝 인수 | B | `vf_iifile.f:169–173` `'AREA'` / `DO 100 I=1,6` / `CALL VF_ZSTOI(IGRARA(I),TEXT(IS(I+3):IE(I+3)))` / `IGRARA(I)=IGRARA(I)+1` | FILE GRP AREA의 마지막 인수는 KC2이다. |
| KS3-157 | GRP AREA 끝점 부등호 | B | `vf_iifile.f:181–187` `IF ((IGRARA(1).GT.IGRARA(4)) .OR.`<br>`     &        (IGRARA(2).GT.IGRARA(5)) .OR.`<br>`     &        (IGRARA(3).GT.IGRARA(6)) .OR.`<br>`     &        (IGRARA(4).GE.NUMI0    ) .OR.`<br>`     &        (IGRARA(5).GE.NUMJ0    ) .OR.`<br>`     &        (IGRARA(6).GE.NUMK     )     )`<br>`     &                 CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')` | FILE GRP AREA는 끝점 NI-1·NJ-1·NK-1을 포함한다. |
| KS3-159 | 와도를 넣는 농도 성분 | B | `vf_iifile.f:189–200` `'ON'` / `'VORT'` / `IGRVOR=1`; `'OFF'` / `'VORT'` / `IGRVOR=0`; `vf_a2dflt.f:96` `IGRVOR=0`; `vf_og1ini.f:96–98` `LS=0` / `IF (LEQC .GT.0) LS=LEQC` / `IF (IGRVOR.NE.0) LS=LS+3` | 와도 세 성분은 기존 농도 성분 뒤에 추가한다. |
| KS3-160 | 도화 최소 셀 수 | H | 3D manual p.126 `A region of at least 2 × 2 cells is necessary (the direction of 1 cell is not shown)`. | 매뉴얼의 최소 2×2 셀과 한 셀 방향 미표시는 도화 도구의 제약이다. |
| KS3-162 | ETIME 생략값·양수 검사 | C | `vf_iifile.f:231–233` `'ELAPSE'` / `CALL VF_ZSTOR(ETIME,TEXT(IS(4):IE(4)))`; `vf_a2dflt.f:131` `ETIME=1.0D30` | ETIME 생략값은 1.0D30 s이다. 입력 읽기 코드는 ETIME의 양수 여부를 검사하지 않는다. 문서의 ETIME>0.0 의무를 유지한다. |
| KS3-165 | TRN 시간 간격 자료형 | B | `vf_iifile.f:261–263` `CALL VF_ZSTOR(RTRTRN(1),TEXT(IS(4):IE(4)))` / `CALL VF_ZSTOR(RTRTRN(2),TEXT(IS(5):IE(5)))` / `CALL VF_ZSTOR(RTRTRN(3),TEXT(IS(6):IE(6)))`. | TRN의 TSTEP 자료형은 R*8이다. |
| KS3-172 | 시계열 농도 LC 형 | B | `vf_iifile.f:375–377` `CALL VF_ZSTOI(LC,TEXT(IS(5):IE(5)))` / `IF (LC.LE.0 .OR. LC.GT.LEQC)`<br>`     &                     CALL VF_A2ERR('VF_IIFILE','INVALID VALUE.')` | 시계열 농도의 LC는 I*4이며 1부터 NC까지이다. |
| KS3-174 | 병렬 MAX 하한 조판 | B | `vf_careap.f:200–203` `W= 1.0D+30` / `CALL VF_P1MIND(W,VMIN)` / `W=-1.0D+30` / `CALL VF_P1MAXD(W,VMAX)`. | 병렬 MAX의 비교 하한은 -1.0D+30이다. |
| KS3-204 | DRAG-DF YU 단위 | B | `vf_vgene.f:119,131,133–134` `DR=CD` / `YU =DRGYU` / `ALPHAX=AP*RN1*RN1*RN1*YU/(RN*RN*DR*DR)` / `BETAX =BT*RN1/(RN*RN*RN*DR)` | DRAG-DF의 YU는 m²/s 단위의 동점성계수이다. |
| KS3-207 | 단층 매개변수 번역 | B | `mod_fault.f:59` `INTEGER:: JSYSTEM=2 ! 断層パラメータの測地系の番号(1-3)` | SEA-BOTTOM CALC는 단층 매개변수로 수위 변동을 계산한다. |
| KS3-209 | UTM 중앙 자오선 범위 검사 | C | `vf_iiopt.f:136–138` `'UTM'` / `CALL VF_ZSTOR(LC_DEG,TEXT(IS(4):IE(4)))` / `CALL SET_UTM(LC_DEG)`; `mod_fault.f:209,213` `REAL(8),INTENT(IN):: LC_DEG` / `ORI_L(0) = LC_DEG*D2R` | UTM 중앙 자오선은 코드에서 범위 검사 없이 라디안으로 변환한다. 문서의 0≤LC_DEG<360 의무는 별도로 지켜야 한다. |
| KS3-211 | 최대 속도 기본값·하한 | C | `vf_iiopt.f:170,172–173` `'MAX-VELOCITY'` / `CALL VF_ZSTOR(VVMAX,TEXT(IS(3):IE(3)))` / `IF (VVMAX.LE.ZERO ) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')`; `vf_a2dflt.f:218` `VVMAX=30.0D0`; `vf_veuler.f:127–128` `IF (UU(I,J,K).GT. VVMAX) UU(I,J,K)= VVMAX` / `IF (UU(I,J,K).LT.-VVMAX) UU(I,J,K)=-VVMAX` | 임시 속도의 각 성분 제한 기본값은 30 m/s이다. 입력 검사는 VVMAX>ZERO를 요구한다. |
| KS3-212 | 속도와 유량 용어 | B | `vf_veuler.f:127–128`의 UU 성분 제한; VV `:184–185`, WW `:241–242`도 같은 ±VVMAX 제한 | MAX-VELOCITY는 유량이 아니라 속도 각 성분을 제한한다. |
| KS3-222 | 시작 배너 판 번호 | A | `VF_A0PRM.h:2` `PARAMETER (IVR001=  0, IVR002=  1,`; `vf_a1main.f:1208–1209` `9510 FORMAT(/' ',`<br>`     &       '##### CADMAS-SURF/3D-MG Ver.',I1,'.',I1,' START. ######')`; `:1234` `9990 FORMAT(/' ','##### NORMAL END. ###########################'/)` | 매뉴얼 출력 예제의 배너는 1.0이다. 공급 코드의 같은 배너 상수는 0.1이다. |
| KS3-226 | 파형 계산값 예제 | H | 3D manual p.137 `LENGTH [M]= 7.30402E+01`, `URSELL NUMB[-]= 2.51319E+01`, `VELOCITY [-]= 8.85853E+00`. 단위 라벨은 E로 별도 판정했다. | 파형·파장 예제 수치는 실행 사례이다. 이 보고서는 수치 재현을 수행하지 않았다. |
| KS3-227 | 개방 경계 파속 출력 단위 | E · 강함 | `vf_csetup.f:143` `BCTYP(6,JD)=WLN/T`; `vf_ol1ini.f:247` `WRITE(ILPFIL,9540) '  VELOCITY   [-]=',BCTYP(6,JD)`. 5.3의 반대 근거 검토를 적용한다. | 개방 경계 파속 출력 라벨의 단위는 m/s로 고쳐야 한다. 수치 계산식의 결함은 확인하지 않았다. |
| KS3-231 | CPU·수렴 출력 사례 | H | 3D manual p.139–140 `TOTAL 117.65`, `PRE PROCESS 0.10`, `CALCULATION 117.55`, `VF_M1BCGS 82.77`. | CPU 시간과 반복 수는 매뉴얼의 실행 사례이다. 이 값으로 현재 판의 성능을 단정하지 않는다. |
| KS3-233 | FSUM·FCUT의 체적·부호 | B | `vf_fcut01.f:40–48` `V=XX(2,I)*YY(2,J)*ZZ(2,K)*GGV(I,J,K)` / `FCUT=FCUT+(FF(I,J,K)-1.0D0)*V` / `FCUT=FCUT+(FF(I,J,K)-0.0D0)*V` / `FSUM=FSUM+FF(I,J,K)*V` | FSUM은 절단 후 물 체적이다. FCUT는 절단 전후 F 차이에 공극 체적을 곱한 부호 있는 합이다. |
| KS3-234 | 진단량의 2-노름 | B | `vf_cdiv00.f:49,55–56` `VAL=VAL+VD*VD` / `CALL VF_P1SUMD(W,VAL)` / `VAL=SQRT(VAL)`; `vf_m1bcgs.f:249–250` `BNORM=SQRT(BNORM)` / `XNORM=SQRT(XNORM)` | !VD!·!B!·!R!는 제곱합의 제곱근인 2-노름이다. |
| KS3-235 | 시계열 입력·출력 예제 개수 | B | `vf_ot1ini.f:35` `DO 100 L=1,ITRNUM`; `:134` `WRITE(ITRFIL,9530) 'TIME',(L,L=1,ITRNUM)` | p.106의 다섯 시계열 항목과 p.142의 일곱 항목은 동일 입력의 출력으로 연결하면 안 된다. |
| KS3-237 | 시간 진행 수치 사례 | H | 3D manual p.143 `STEP= 1 : TIME= 1.20000E-03 : DT = 1.20000E-03`; `STEP= 2 : TIME= 2.64000E-03 : DT = 1.44000E-03`. | 인쇄한 시간 진행은 실행 사례이다. 첫 세 시간 간격의 1.2배 관계만 정적으로 확인했다. |
| KS3-244 | 매트릭스 w·z 설명 | B | `vf_im1inp.f:20,23` `CD    DMTBZZ(MTBZZ)       : OUT : R*8 : マトリクスデータのz座標` / `CD    DMTBUT(MTBZZ,MTBTT) : OUT : R*8 : マトリクスデータの鉛直方向流速` | 매트릭스 z는 평균 수위 기준 수직 좌표이다. w는 수직 속도이다. |
| KS3-251 | 공극률 이진 자료형 | B | `vf_ip1inp.f:10,24,88–90` `IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` / `DIMENSION GGVOLD(IPRNP),GGVNOW(IPRNP)` / `READ(IPRFIL,END=9020,ERR=9030)`<br>`     &               (((GGVNOW(NP+I+NI*(J-1)+NI*NJ*(K-1)),`<br>`     &                  I=1,NI),J=1,NJ),K=1,NK)` | 공급 코드의 poro 공극률 레코드는 R*8이다. p.145의 R*4 표와 다르다. |
| KS3-254 | 면 투과율 확장 계획 | H | 3D manual p.146 `In the future, when the file input becomes necessary, the flag for extension will be used and improves the program`. | 확장 플래그를 이용한 면 투과율 입력은 문서의 향후 계획이다. |
| KS3-256 | 환경 파일 첫 정수 | B | `vf_pmginp.f:28` `READ(IENFIL,*,END=9020,ERR=9020) MGARAN`; `:32` `DO 120 I=1,MGARAN` | data.env 첫 정수는 전체 해석 영역 수이다. |
| KS3-257 | 병렬 파일명 번호 규칙 | D | `vf_a1main.f:376–379` `WRITE(TEXTP,'(I5.5)') MYRANK` / `OPEN(MFILLP,ERR=9010,`<br>`     &       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.list'//TEXTP,`<br>`     &       STATUS='NEW',FORM='FORMATTED' )`; `vf_og1ini.f:49–52` `WRITE(TEXTP,'(I5.5)') MYRANK` / `OPEN(MFILGR,ERR=9010,`<br>`     &       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.grp'//TEXTP,`<br>`     &       STATUS='NEW',FORM='UNFORMATTED' )` | 공급 코드의 병렬 목록·도화 파일명은 영역명+확장자+5자리 PE 번호이다. 문서의 6자리·확장자 앞 번호 규칙을 적용하면 안 된다. |
| KS3-262 | 도화 도구 화면 구획 | H | 3D manual p.147 `(1) Command area`, `(2) Main drawing area`, `(3) Sub Drawing Area`. | 도화 도구 화면은 명령·주 도화·보조 도화 영역으로 나뉜다. |
| KS3-263 | 도화 도구 조작법 | H | 3D manual p.147 `Control key + mouse drag → enlarge`; `Shift key + mouse drag → move`; `pressing the "Enter" key at the end`. | 확대·이동·옵션 버튼·Enter 적용은 외부 도화 도구 사용법이다. |
| KS3-264 | 도화 도구 그림 | H | 3D manual p.148 `Figure 0-5-3 Image of graphic unit`; `Figure 0-5-4 Switching of physical quantity control command`. | p.148은 도화 도구 화면과 물리량 선택 화면의 그림 쪽이다. |
| KS3-265 | 참고문헌 (1)–(5) | H | 3D manual p.149 `(1) Coastal Development Institute of Technology. (2001)`에서 `(5) M. Isobe, H. Nishimura and S. Horikawa`까지의 서지. | p.149의 참고문헌 (1)–(5)는 서지이다. 이 쪽은 식 대조 대상이 아니다. |
| KS3-266 | 참고문헌 (6)–(10) | H | 3D manual p.149 `(6) Dean, R. G. (1965)`에서 `(10) Shimada, A., Nakadai, Y. and Akiyama, M. (1992)`까지의 서지. | p.149의 참고문헌 (6)–(10)는 서지이다. (10)은 다음 쪽으로 이어진다. |
| KS3-267 | 참고문헌 (10) 계속·(11)–(15) | H | 3D manual p.150 `(11) Noboru Yamazaki (1992)`부터 `(15) Fujino, S. (1991)`까지의 서지와 (10)의 계속. | p.150은 참고문헌 (10)의 계속과 (11)–(15)이다. |
| KS3-276 | 영역 평균·적분의 가중 체적 | C | `vf_careap.f:175–180`의 유효 셀 처리 중 `AR  =XX(2,I)*YY(2,J)*ZZ(2,K)*GGV(I,J,K)*FF(I,J,K)` / `VAV =VAV +AR` / `VINT=VINT+AR*VAL(I,J,K)`; `:198` `IF (VAV.GT.0.0D0) VAV=VINT/VAV` | AV·INT의 일반 스칼라는 공극률과 F를 포함한 물 체적으로 가중한다. |
| KS3-277 | INDC 반복문 종료 행 | B | `vf_cindc.f:51–53` `100      CONTINUE` / `110    CONTINUE` / `120  CONTINUE` | INDC 예제의 바깥 DO 120에는 120 CONTINUE가 필요하다. |
| KS3-278 | VISC 동점성계수 | B | `vf_ol1trn.f:170` `CD    -- 分子動粘性係数と渦動粘性係数の和を出力する --`; `:173` `CALL VF_OL3DR(ANU,0)`. 주석 뜻은 “분자 동점성계수와 와 동점성계수의 합을 출력한다”이다. | VISC는 분자 동점성계수와 와 동점성계수의 합이다. |
| KS3-279 | 파속 단위의 코드 측 근거 | E · 강함 | `vf_csetup.f:143` `BCTYP(6,JD)=WLN/T`; `VF_APHYSR.h:73` `CD                             (6,*):波速`; `vf_ol1ini.f:247` `WRITE(ILPFIL,9540) '  VELOCITY   [-]=',BCTYP(6,JD)` | BCTYP(6,JD)는 파속이며 단위는 m/s이다. 출력의 [-] 라벨은 코드 결함 후보이다. |
| KS3-280 | 출력 압력의 차감 방향 | B | `vf_fpvcpp.f:191` `PVCPES(L)=(PAV+PVCP0)/(1.0D0+PVCGM*DTNOW*PVCDIV(L))-PVCP0`; `A11111.in:776` `注）L/P出力等で出力される圧力値は大気圧分が差し引かれている` | 출력 압력은 절대압에서 대기압을 뺀 값이다. p.131 영어 문장의 차감 방향을 바로잡는다. |
| KS3-281 | 5.5 절 번호 중복 | B | 코드 대조 대상 아님. p.143 표준출력은 KS3-238이고 p.144 파일은 KS3-241이다. | p.143과 p.144의 중복 절 번호 5.5를 편집상 구분한다. |
| KS3-282 | 매트릭스 속도·유량 번역 | B | `vf_im1inp.f:22` `CD    DMTBUN(MTBZZ,MTBTT) : OUT : R*8 : マトリクスデータの水平方向流速`; `A11111.in:184` `水位／流速：水深と周期が必須` | 매트릭스의 u·w는 유량이 아니라 속도이다. |
| KS3-283 | GUI의 표시 항목 | H | 3D manual p.148의 `物理量制御`(물리량 제어)·`自由表面`(자유수면)·`流速`(속도)·`圧力`(압력)·`数値`(수치) 표시. | p.148의 GUI 제어·표시 항목은 외부 도화 도구 사용법으로 기록한다. |
| KS3-284 | AUTO의 ars EOF 예외 | C | `vf_ii1inp.f:343–351` `IRETYP=-1` / `OPEN(MFILAR,ERR=310,`<br>`     &               FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.ars',`<br>`     &               STATUS='OLD',FORM='FORMATTED'  )`<br>`                  READ(MFILAR,*,ERR=310) II,TT`<br>`                  CLOSE(MFILAR)`<br>`CCC                  IF( II.GE.0 ) IRETYP=II`<br>`                  IRETYP=II`<br>`  310             CONTINUE` | AUTO의 ars 읽기에는 ERR=310이 있지만 END=310은 없다. EOF의 최초 계산 복귀를 보장한다고 쓰지 않는다. |
| KS3-301 | INDC의 병렬 내부 범위 | C | `vf_cindc.f:26–32` `IB=NUMI` / `JA=1` / `JB=NUMJ` / `IF (MYMIS.EQ.1) IA=2` / `IF (MYMIE.EQ.1) IB=NUMI-1` / `IF (MYMJS.EQ.1) JA=2` / `IF (MYMJE.EQ.1) JB=NUMJ-1` | 물리 경계에서만 끝 셀을 제외한다. 내부 병렬 경계의 통신 셀은 그림의 단순 2…N−1 범위와 구분한다. |
| KS3-302 | 병렬 분할 추가 검사 | C | `vf_iipara.f:33–34` `IF (NUMNPI.GE.MAXNPI)`<br>`     &                CALL VF_A2ERR('VF_IIPARA','AREA IS FULL.')`; `vf_cpara.f:39–40` `IF (IPROCS(I)-IPROCS(I-1).LT.2)`<br>`     &                      CALL VF_A2ERR('VF_CPARA','2 > IC2-IC1.')`; `:45–46` `IF (JPROCS(J)-JPROCS(J-1).LT.2)`<br>`     &                      CALL VF_A2ERR('VF_CPARA','2 > JC2-JC1.')`; `:59–60` `IF (NPROCS.NE.NUMNPI*NUMNPJ)`<br>`     &                CALL VF_A2ERR('VF_CPARA','NPROCS <> NPI*NPJ.')` | 각 분할 폭은 적어도 2셀이어야 한다. 프로세스 수는 방향별 수의 곱과 같아야 한다. |
| KS3-303 | AUTO 시간 간격 증가 한도 | C | `vf_cdtcal.f:59` `DT=DTMAX/DTSAFE`; `:145–147` `W=DTNOW` / `IF (NNOW.EQ.0) W=DTINIT` / `DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)` | 다음 시간 간격은 이전 시간 간격의 1.20배 이하이다. 최소 시간 간격이 이 제한보다 크면 최소값을 우선한다. |
| KS3-304 | 자동 재시작의 정상 종료 표지 | C | `vf_ii1inp.f:356–357` `IF (IRETYP.EQ.-999)`<br>`     &          CALL VF_A2ERR('VF_II1INP','CALCULATION END.')`; `vf_a1main.f:1149` `IF ( IE.EQ.1.AND.ETIME.LT.1.0D30 ) IEE=1`; `:1161–1164` `WRITE(MFILAR,'(I10,1X,F10.2)') -999,TNOW` / `CLOSE(MFILAR)` / `OPEN(IFLAR,FILE='stop_ars',STATUS='UNKNOWN')` / `CLOSE(IFLAR)` | 정상 종료이며 `ETIME.LT.1.0D30`이면 ars에 −999와 `stop_ars` 파일을 남긴다. 다음 AUTO는 최초 계산으로 되돌아가지 않고 종료 오류를 낸다. |
| KS3-305 | TIME 출력 단계 선택 | C | `vf_ot1trn.f:66–72` `Cmod20130605        IF (TNOW.GE.RTRTRN(1)-ZERO .AND. TNOW.LE.RTRTRN(2)+ZERO) THEN` / `IF (TNOW.GE.RTRTRN(1)-0.5D0*DT .AND.`<br>`     $      TNOW.LE.RTRTRN(2)+0.5D0*DT) THEN` / `W=(TNOW+0.5D0*DT)-RTRTRN(4)` / `IF (W.GE.0.0D0) THEN` / `IO=1` / `RTRTRN(4)=RTRTRN(4)+DBLE(INT(W/RTRTRN(3))+1)*RTRTRN(3)` | 예약 시간에 보간한 결과를 출력하는 방식이 아니다. 다음 시간 간격의 절반을 이용하여 실제 단계의 결과를 선택한다. 20130605 변경 표지가 있다. |
| KS3-306 | 재시작 방정식 일관성 검사 | C | `vf_ir1inp.f:154–160` `READ(IREFIL,ERR=9020) LN,LV,LP,LF,LK,LT,LS,LG,LD,L1` / `IF (LK.NE.LEQK)`<br>`     &    CALL VF_A2ERR('VF_IR1INP','INVALID EQUATION (K-EPS).')`<br>`      IF (LT.NE.LEQT)`<br>`     &    CALL VF_A2ERR('VF_IR1INP','INVALID EQUATION (TEMP).')`<br>`      IF (LS.NE.LEQC)`<br>`     &    CALL VF_A2ERR('VF_IR1INP','INVALID EQUATION (CONC).')` | 재시작 파일의 난류·온도·농도 활성 상태가 현재 입력과 같아야 한다. “대부분 변경 가능”에는 이 예외가 있다. |
| KS3-307 | 물방울·표면 속도 기본 선택 | C | `vf_a2dflt.f:45,151` `IBSUW0=0` / `IDROP=1`; `vf_iiopt.f:51–52,70–71` `ELSEIF (TEXT(IS(3):IE(3)).EQ.'D2U=0') THEN` / `IBSUW0=0` / `ELSEIF (TEXT(IS(4):IE(4)).EQ.'FREE-RUNDOWN') THEN` / `IDROP=1` | 생략 시 표면 속도는 D2U=0이며 물방울 시간문은 FREE-RUNDOWN이다. p.138 예제는 전자를 보여 주지만 옵션 정의에는 기본값을 명시하지 않는다. |
| KS3-308 | STK-CND 자동 선택 기준 | C | `vf_csetup.f:103–110` `IF (D.GE.ZERO) WUS=GRZ0*H*T*T/D/D` / `IF (N.EQ.0) THEN` / `IF (WUS.LE.25.0D0) THEN` / `N=-2` / `ELSE` / `N=-1` / `ENDIF` / `IBCTYP(2,JD)=N` | Ursell 수가 25 이하이면 Stokes를 선택한다. 25보다 크면 cnoidal을 선택한다. |
| KS3-309 | DRAG-DF 공극률 하한 분기 | C | `vf_vgene.f:112–116` `IF (GV.LE.PLOWER .OR. CD.LE.DRGDR(1)) THEN` / `RN=PLOWER` / `DR=DRGDR(1)` / `AP=0.0D0` / `BT=0.0D0` | 공극률이 PLOWER 이하이면 입경에 관계없이 두 저항계수를 0으로 둔다. DR 구간표만으로 동작 전체를 설명할 수 없다. |
| KS3-310 | 영역 통계의 F·속도 특례 | C | `vf_careap.f:156–158` `AR  =XX(2,I)*YY(2,J)*ZZ(2,K)*GGV(I,J,K)` / `VAV =VAV +AR` / `VINT=VINT+AR*FF(I,J,K)`; 속도는 `:88` `VINT=VINT+AR*(P1+P2)*0.5D0` | F는 장애물이 아닌 셀의 공극 체적으로 가중한다. 일반 스칼라·속도는 물 체적으로 가중한다. 속도 적분은 양쪽 면속도의 평균을 쓴다. |
| KS3-311 | 매트릭스 증가순·초기 위상 검사 | C | `vf_im1inp.f:101–102` `IF (DMTBT0.LT.0.0D0 .OR. DMTBT0.GT.1.0D0)`<br>`     &                CALL VF_A2ERR('VF_IM1INP','INVALID VALUE.')`; `:118–119` `IF (DMTBZZ(K).LE.DMTBZZ(K-1))`<br>`     &                 CALL VF_A2ERR('VF_IM1INP','INVALID VALUE.')`; `:145–146` `IF (DMTBTT(I).LE.DMTBTT(I-1))`<br>`     &                    CALL VF_A2ERR('VF_IM1INP','INVALID VALUE.')` | z좌표와 위상 자료는 각각 엄격 증가순이다. 초기 위상도 0…1을 요구한다. |
| KS3-312 | 공극률 파일 상한·하한 | C | `vf_ip1inp.f:42` `IF (IPRNB.GT.MAXPRB) CALL VF_A2ERR('VF_IP1INP','AREA IS FULL.')`; `:94` `GGVNOW(L)=MAX(GGVNOW(L),PLOWER)` | 블록 수는 MAXPRB를 넘지 못한다. 읽은 공극률은 PLOWER 이상으로 바꾼다. |
| KS3-313 | 면 투과율의 경계 예외 | C | `vf_cggxyz.f:74–77` `IF     (INDX(IW,JW,K).EQ.-1) THEN` / `GGX(IW,JW,K)=1.0D0` / `ELSEIF (INDX(IW,JW,K).EQ. 0) THEN` / `GGX(IW,JW,K)=MIN(GGV(IW,JW,K),GGV(IW-1,JW,K))` | 두 셀 최소값 규칙은 일반 내부 면에 적용한다. 장애물 내부 면은 1이며 경계면의 지정 투과율은 이 분기에서 덮어쓰지 않는다. Y·Z도 같다. |
| KS3-314 | 환경 파일 추가 검사 | C | `vf_pmginp.f:29–30,43,45–46,51–52` `IF (MGARAN.GT.MAXPRO) GOTO 9030` / `IF (MGARAN.LE.0     ) GOTO 9040` / `IF (MGNPIN(I).LE.0     ) GOTO 9040` / `IF (MGPARE(I).GT.MGARAN) GOTO 9040` / `IF (MGPARE(I).EQ.I     ) GOTO 9040` / `IF (N.GT.MAXPRO) GOTO 9030` / `IF (N.NE.MGPROC) GOTO 9050`; `:75,82` `IF (N.GT.0) GOTO 9040` / `IF (MGNAME(I).EQ.MGNAME(L)) GOTO 9040` | 영역 수·PE 총수·부모 범위·자기 부모·부모 순환·중복 영역명을 검사한다. |
| KS3-315 | 와도의 셀 상태 제한 | C | `vf_cvort.f:66,72` `VORT=0.0D0` / `IF (NF(I0,J0,K0).EQ.0) THEN` | 와도 계산은 완전 유체 셀에서 수행한다. 표면·기체·장애물 셀에는 초기 0을 남긴다. |
| KS3-316 | 명령 대소문자 | C | `vf_ii1inp.f:178` `IF     (TEXT(IS(1):IE(1)).EQ.'PARALLEL') THEN`; `:410–413` `CD      -- 解釈できないヘッダーによるエラー --` / `ELSE` / `WRITE(ILPFIL,9520) (TEXT(IS(I):IE(I)),I=1,NWD)` / `CALL VF_A2ERR('VF_II1INP','UNKNOWN HEADER.')` | 일본어 주석 뜻은 “해석할 수 없는 헤더 오류”이다. 문자열 비교는 대소문자를 구분한다. 소문자 명령을 대문자로 바꾸는 처리는 없다. |
| KS3-317 | GRID END 추가 검사 | C | `vf_iigrid.f:76–77` `IF (TEXT(IS(I):IE(I)).EQ.'END') THEN` / `IF (I.NE.NWD) CALL VF_A2ERR('VF_IIGRID','SYNTAX ERROR.')`; `:108` `IF (IEOF.NE.0) CALL VF_A2ERR('VF_IIGRID','NOT FOUND (END).')` | END 뒤 추가 단어를 금지한다. END를 만나기 전 EOF이면 오류이다. KS3-024의 근거이다. |
| KS3-318 | MATRIX2 별도 파일 | C | `vf_im2inp.f:44–47` `OPEN(MFILMT2,ERR=9010,`<br>`     &       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.mtb2',`<br>`     &       STATUS='OLD',FORM='FORMATTED'  )`<br>`        IMTFIL2=MFILMT2`; `:61–66` `IF     (TEXT(IS(IP):IE(IP)).EQ.'LEVEL-ON'  ) THEN` / `MTBTYP2=1` / `ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'LEVEL-OFF' ) THEN` / `MTBTYP2=2` / `ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'LEVEL-ONLY') THEN` / `MTBTYP2=3` | MATRIX2는 `.mtb2`를 읽는다. p.144는 `.mtb`만 설명한다. 두 파일은 각자 LEVEL-ON·LEVEL-OFF·LEVEL-ONLY를 읽는다. 파일 번호는 `VF_A0PRM.h:10–11`의 MFILMT=12와 MFILMT2=15이다. |
| KS3-319 | 공극률·관성·저항의 초기 공간장 | C | `vf_a1main.f:501–506` `CALL VF_ZSETR3(CM0 ,0.0D0,NUMI,NUMJ,NUMK)` / `CALL VF_ZSETR3(CD0 ,0.0D0,NUMI,NUMJ,NUMK)` / `CALL VF_ZSETR3(GGV ,1.0D0,NUMI,NUMJ,NUMK)` / `CALL VF_ZSETR3(GGX ,1.0D0,NUMI,NUMJ,NUMK)` / `CALL VF_ZSETR3(GGY ,1.0D0,NUMI,NUMJ,NUMK)` / `CALL VF_ZSETR3(GGZ ,1.0D0,NUMI,NUMJ,NUMK)` | POROUS 명령을 대입하기 전 관성·저항계수는 0이다. 공극률과 세 면 투과율은 1이다. 표의 각 직사각형 입력 인수에 기본값이 없다는 사실과 전체 공간장의 초기값을 구분한다. |
| KS3-320 | MAM 파일명·형식·물리량 | C | `vf_om1ini.f:131–138` 단일 프로세스 `OPEN(MFILMM,ERR=9010,`<br>`     $       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.ma',`<br>`     &       STATUS='NEW',FORM='UNFORMATTED' )`; 병렬 `WRITE(TEXTP,'(I5.5)') MYRANK` / `OPEN(MFILMM,ERR=9010,`<br>`     $       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.ma'//TEXTP,`<br>`     &       STATUS='NEW',FORM='UNFORMATTED' )`; `:144,147–148` `WRITE(IMMFIL,ERR=9020) NUMI-2,NUMJ-2` / `WRITE(IMMFIL,ERR=9020) (XX(1,I),I=2,NUMI)` / `WRITE(IMMFIL,ERR=9020) (YY(1,J),J=2,NUMJ)`; `vf_om1trn.f:39` `REAL WK01(2:NUMI-1,2:NUMJ-1,NUMK)`; `:86–88` `WK01(I,J,1)=REAL(DWK)` / `WK01(I,J,2)=REAL(UWK*0.5D0)` / `WK01(I,J,3)=REAL(VWK*0.5D0)`; `:120` `WRITE(IMMFIL,ERR=9010) REAL(TNOW)` | p.129는 출력 예약만 설명한다. 코드는 `.ma` 또는 `.ma`+5자리 PE 번호를 쓴다. 초기 레코드는 수평 셀 수·격자 좌표·지표고이다. 단계 레코드는 단정밀도 시간·수심·수심 적분 속도 두 성분이다. 좌표 레코드는 배정밀도이다. 지표고·수심·수심 적분 속도는 REAL WK01 배열로 쓴다. `:80–83`의 ZF 가중합에는 수심으로 나누는 연산이 없다. |
| KS3-401 | 현재 노트의 CM0/CD0 입력 설명 | B | `vf_iiporo.f:191` `ELSEIF (TEXT(IS(2):IE(2)).EQ.'CM') THEN`; `:219` `ELSEIF (TEXT(IS(2):IE(2)).EQ.'CD') THEN`; `vf_iifile.f:101–104`는 CM0·CD0의 ILPON 출력 플래그 대입이다. | 관성·저항의 입력 키워드는 POROUS CM과 POROUS CD이다. FILE L/P의 CM0·CD0는 출력 선택이다. |
| KS3-403 | 현재 노트의 FILE 파서 범위 | C | `vf_iifile.f:471` `ELSEIF (TEXT(IS(2):IE(2)).EQ.'PORO') THEN`; `:473` `CALL VF_ZSTOI(IPRNT,TEXT(IS(3):IE(3)))`; `vf_ii1inp.f:336` `IF( TEXT(IS(2):IE(2)).EQ.'RES' ) THEN`. | FILE 파서는 L/P·GRP·RSL·TRN·MAM·PORO를 읽는다. RES·OBS는 상위 입력 루틴이 먼저 읽는다. |
| KS3-404 | 현재 노트의 직렬화 설명 | C | `vf_ot1trn.f:94` `CALL VF_CWLVL(ZZ,FF,RTRVAL(L),NF,ITRPRM(3,L),ITRPRM(4,L))`; `vf_careap.f:198` `IF (VAV.GT.0.0D0) VAV=VINT/VAV`. | 시계열 출력은 직렬화에 앞서 수위·와도·평균·적분·파력을 계산한다. |
| KS3-409 | 현재 노트의 FCUT·!B! 정의 | B | `vf_fcut01.f:40` `V=XX(2,I)*YY(2,J)*ZZ(2,K)*GGV(I,J,K)`; `vf_m1bcgs.f:249–250` `BNORM=SQRT(BNORM)` / `XNORM=SQRT(XNORM)`. 3D manual p.140은 !B!의 대상을 `right-hand vector`라고 적는다. | FCUT는 질량이 아닌 부호 있는 체적이다. !B!는 우변 벡터의 노름이고 !R!는 잔차 벡터의 노름이다. |

### 5.5 대조 종료 확인

2.13의 쪽별 확인표는 p.101–150의 50쪽을 빠짐없이 포함한다. 본문 대조 표는 각 쪽의 식·입력 형식·계수·기본값·변수·제한·출력·도식·절차를 다룬다. 입력 예제의 명령은 A11111.in의 형식 명세와 입력 읽기 문자열에 대조했다. A11111.in의 설명 자체에도 LC 자료형 등의 오기가 있으므로 이 파일만을 구현 근거로 쓰지 않았다.

2.14에 실은 행 번호가 붙은 원문 2118행을 실제 소스의 같은 줄과 기계적으로 대조했다. 이 대조에서 다른 원문 줄은 없었다. 고정형식 Fortran 인용의 계속 줄도 확인했다. Makefile은 고정형식 Fortran 검사 대상에서 제외했다. 5.4의 91행은 일치가 아닌 모든 대상 행과 일대일로 연결된다. 누락된 결론 ID는 없다. 같은 ID에 두 분류를 부여하지 않았다.

모델 실행·컴파일·예제 재현은 수행하지 않았다. 수치적·물리적 검증은 수행하지 않았다. 현재 노트의 수정안은 4절에 기록했다. 현재 노트 파일은 수정하지 않았다. 이 작업에서는 지정한 비교 보고서 파일만 수정했다.

분류별 개수(5.4의 91행 기준): A 2, B 37, C 33, D 1, E 3, F 0, H 15, X 0. 열지 못한 대상 파일: 없음.
