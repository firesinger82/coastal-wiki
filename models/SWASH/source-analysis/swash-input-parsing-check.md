---
title: "SWASH 입력 파싱 + prep 검사 — ReadInput 키워드 디스패치 + CheckPrep 정합성 검증"
model: SWASH
component: src (input parsing / consistency check / grid check)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashReadInput.ftn90(키워드 디스패치 루프 286-2890·CGRID 2171-2335·READ 2463-2600·TEST 2780-2807)·SwashCheckPrep.ftn90(정합성 msgerr 카탈로그 185-1272·구조 178-274)·SwashCheckGrid.ftn90(전문)·SwashReadTestpnts.ftn90(전문)·SwashPrintSettings.ftn90(전문)·SwashPrintGridInfo.ftn90(전문)·SwashBndTopology.ftn90(전문) file:line 인용. 호출 관계는 grep로 caller 확인(SwashMain·SwanGridTopology·SwashInitCompUgrid)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/SWASH/source-analysis/swash-architecture-source-map.md
  - models/SWASH/README.md
---

# SWASH 입력 파싱 + prep 검사

> 명령파일을 키워드로 파싱(ReadInput)하고, 계산 시작 전 설정 정합성을 검증·보정(CheckPrep)하는 전처리 계층. 경로: raw/source_code/swash/src/

## 0. 호출 관계 (전체 흐름)

`SwashMain.ftn90`이 다음 순서로 호출한다:
`SwashReadInput(comput)` → `SwashCheckPrep` → (`ITEST>0`이면) `SwashPrintSettings` (`SwashMain.ftn90:140,158,183`).

- ReadInput은 `comput`(='COMP'/'NOCO'/'STOP')을 채워 반환 → Main이 이 값으로 계산 여부 분기 (`SwashMain.ftn90:146`, `SwashReadInput.ftn90:78-81`).
- CheckGrid·PrintGridInfo·BndTopology는 ReadInput에서 직접 부르지 않고 **비정형 격자 빌드 경로**에서 호출된다 (§6):
  - `SwashBndTopology` ← `SwanGridTopology.ftn90`
  - `SwashPrintGridInfo` ← `SwanGridTopology.ftn90`
  - `SwashCheckGrid` ← `SwashInitCompUgrid.ftn90`
- ReadTestpnts는 ReadInput의 `TEST POI` 명령에서 호출 (`SwashReadInput.ftn90:2799`).

| 서브루틴 | 줄 수 | 역할 | caller |
|---|---|---|---|
| SwashReadInput | 2902 | 명령파일 키워드 파싱·common var 설정 | SwashMain |
| SwashCheckPrep | 6006 | 설정 정합성 검사 + 계산 전 준비 | SwashMain |
| SwashCheckGrid | 257 | 비정형 mesh 품질 검사 | SwashInitCompUgrid |
| SwashReadTestpnts | 298 | test point 읽기 + TESTPNTS point set 생성 | SwashReadInput(TEST POI) |
| SwashPrintSettings | 447 | run 설정 PRINT 파일 출력 | SwashMain |
| SwashPrintGridInfo | 176 | mesh 통계 PRINT 출력 | SwanGridTopology |
| SwashBndTopology | 144 | 경계 cell/face 토폴로지 셋업 | SwanGridTopology |

---

## 1. ReadInput — 파싱 메커니즘

### 1.1 Purpose / Method (verbatim)

`SwashReadInput.ftn90:38-53`:
```
!   Purpose
!   Reading and processing of the user commands describing the model
!   Method
!   A new line is read, in which the main keyword determines what the
!   command is. The command is read and processed. Common variables are
!   given proper values. After processing the command the routine returns
!   to label 100, to process the next command. This is repeated until the
!   command STOP is found or the end of input file is reached.
```

### 1.2 메인 루프 구조

라벨 `100`에서 시작하는 read-process 루프 (`SwashReadInput.ftn90:257`):
1. `call NWLINE` — 새 줄 읽기 (`:257`)
2. `ELTYPE == 'EOF'`이면 included 파일에서 빠져나옴; 최상위(`inclev==0`)에서 EOF면 `msgerr(4,'unexpected end of command input')` (`:259-274`)
3. `call INKEYW ('REQ',' ')` — 첫 토큰을 주 키워드로 읽음 (`:276`)
4. `KEYWIS('XXX')`로 키워드 매칭 → 해당 블록 처리 → `goto 100`으로 복귀 (`:286` 이하)
5. 매칭 안 되면 마지막 fall-through에서 출력 명령으로 재해석 시도, 그래도 실패하면 에러 (§4.3)

`KEYWIS`는 user manual 키워드 매칭 함수(logical, `:179` 선언). `INKEYW(status, default)`에서 `'REQ'`=필수, `'STA'`=옵션(default 적용), `'UNC'`=조건부.

### 1.3 INCLUDE 처리

`INCL 'FILE'` 명령: include 레벨 `inclev`를 1 증가, 새 unit으로 `FOR(...,'OF',...)` open, `INPUTF`를 바꿈 (`:304-317`). 최대 include 레벨 `mxincl=10` (`:86`); 초과 시 `msgerr(4,'too many INCLUDE levels')` (`:309-310`). EOF 시 `close`하고 한 단계 복귀 (`:264-265`).

---

## 2. ReadInput — 명령 키워드 카탈로그

최상위 디스패치(4-칸 들여쓰기 `if (KEYWIS(...))`)는 `SwashReadInput.ftn90`에서 다음과 같다 (grep `^    if ( KEYWIS`로 확인한 전체 목록):

| 키워드 | 라인 | 의미 (소스 주석/동작 근거) |
|---|---|---|
| STOP | 286 | `runmade`면 `comput='STOP'`, 아니면 'NOCO' + 'No computation requested' (`:286-294`) |
| INCL | 304 | include 파일 (§1.3) |
| PROJ | 333 | 프로젝트 명/번호 + title1-3 (`:333-345`) |
| OUTP OPT | 357 | 출력 옵션: TAB [field], BLO [ndec][len] (`:357-373`) |
| MODE | 395 | NONST/DYN vs STAT, ONED/TWOD, SKIPMOM, LIN (선형 SWE) (`:395-431`) |
| COMP | 450 | 계산 명령 → `runmade` 셋, STAT/시간 윈도 파싱 (`:450-456`) |
| SET | 524 | NAUT/CART 방향관습, CC 등 (`:524-557`) |
| COORD | 577 | CART vs SPHE(QC/CCM 구면 옵션) (`:577-610`) |
| QUANT | 639 | 출력량 정의 (PROBLEM/USER, FRAME) (`:639-671`) |
| FRIC | 777 | 바닥마찰: CON/CHEZ/MANN/LOG(SMOOTH·ROUGH)/COLE/LIN (`:777-801`) |
| WIND | 830 | 바람: CON/CHARN/LIN(WU·GARR·SMI·CHE)/FIT, REL(W) (`:830-895`) |
| BRE | 909 | wave breaking 제어 (`:909`) |
| AMB | 943 | ambient current (S/C) (`:943-949`) |
| PORO | 965 | porosity (`:965`) |
| SHIP/VESS/WEC/FLOAT/BODY/PONT/PFLOW | 981 | 부유체/강체: METH·SOLV(NEW/HHT/WBZ), DIM, DOF(SU/SW/HE/RO/PI/YA/ALL), MLI(mooring), FEN(fender) (`:981-1166`) |
| VISC | 1253 | 점성: V/FULL(KEPS LIN/NONL), H(CON/SMAG/MIX) (`:1253-1289`) |
| VEGE | 1305 | 식생 (MASS/INER, PORO, V) (`:1305-1355`) |
| CORI | 1382 | Coriolis (`:1382`) |
| TRANSP/CONST | 1406 | 수송: COH/MUD(점착) vs NONC(비점착) (`:1406-1414`) |
| NONHYD | 1499 | 비정수압 모드 옵션 (`:1499`) |
| SPON | 1595 | sponge layer (side 선택) (`:1595`) |
| VERT | 1782 | 수직 층 분할 (`:1782`) |
| TIMEI | 1858 | 시간 적분 방식 (`:1858`) |
| DISCRET | 1959 | 이산화 스킴(advection/eqn) (`:1959`) |
| DPS/BOTC | 2144 | bottom level (`:2144`) |
| CGRID/GRID | 2171 | 계산격자 (§3) (`:2171`) |
| INP | 2350 | 입력격자(BOT/CUR/VX/VY/FR/WI/PR/CORI/PORO/...) REG/CURV/UNSTRUC (`:2350-2346 주석`) |
| READ | 2463 | 격자좌표·입력장·비정형격자 읽기 (§3.3) (`:2463`) |
| SOUR/LINE | 2618 | 내부 wave 생성 (REGular/SPECTrum, SMOO) (`:2618`) |
| TEST | 2780 | 테스트 레벨/추적/POI 테스트점 (§5) (`:2780`) |
| REST/BACK/HOTF/SAVE | 2811 | hot-start 백업 출력 (`:2811`) |
| INIT | 2825 | 초기조건 (`SwashInitCond` 위임) (`:2825`) |
| BOU | 2833 | 경계조건 (`SwashBounCond` 위임, 전역 격자 dim 임시 치환) (`:2833-2844`) |

> ⚠ 위 표의 "의미"는 코드의 분기·서브키워드와 줄 번호에 근거; manual의 정식 신택스 전체 전개는 source-needed(여기서는 해당 명령 블록 진입 라인만 검증).

---

## 3. ReadInput — 격자 명령 상세 (CGRID / INP / READ)

### 3.1 CGRID — 계산격자 타입 (`:2171-2335`)

`logcom(2)=.true.`로 "CGRID 수행됨" 마킹 (`:2173`). 격자 타입 `optg`:
- `CURV` → `optg=3` (curvilinear) (`:2175-2176`)
- `UNSTRUC` → `optg=5` (unstructured), 이후 `goto 130`으로 셀 수 파싱 skip (`:2182-2183, 2216`)
- 기본 `REG` → `optg=1` (rectilinear), `XPC/YPC/ALPC/XLENC/YLENC` 읽음. 구면(`kspher/=0`)이면 XPC/YPC 'REQ' (`:2189-2208`)
- `alpc`는 $-\pi \sim \pi$로 정규화: `alpc = pi2*(alpc/360. - nint(alpc/360.))` (`:2213`)

셀 수: 사용자 `MXC=mxs`, `MYC=mys`. 가상 셀 포함하여 `mxc=mxs+2`, `myc=mys+2` (`:2253,2256`). 메쉬 크기 `dx=xclen/mxs`, `dy=yclen/mys`; 1D면 `dy=dx` (`:2254-2261`).

1D 모드(`oned`) 보정: `MYC/=0`이면 `msgerr(1,'1D simulation: [myc] set to zero !')` 후 `mys=0`; `YLENC/=0`도 동일 경고 (`:2202-2206, 2227-2231`).

REPeating/PERiodic 격자: `REP`/`PER` + X/Y로 `lreptx`/`lrepty` 셋. 1D에서 y-repeat는 경고 후 무시 (`:2237-2250`).

rectilinear(`optg==1`)이면 좌표 직접 생성: `xcgrid(i,j)=xpc+cospc*(i-1)*dx-sinpc*(j-1)*dy` (`:2285-2293`). 계산격자는 출력 데이터 'COMPGRID' point set으로 등록 (`:2298-2332`).

### 3.2 INP — 입력격자 (`:2350` 이하)

`INPgrid` 다음 서브키워드로 `igrd`(필드 종류)와 `psname` 설정: BOT→1/'BOTTGRID', CUR/VEL→2&3('VXGRID', `inituf/initvf=.true.`), VX→2, VY→3 (`:2355-2370`). 명령 주석에 전체 필드 목록(WLEV/CURRENT/FRic/WInd/PRes/CORI/PORO/PSIZ/HSTRUC/NPLAnts/DRAFt/LABel/SAL/TEMP/SED/MWL/ACUR/AVX/AVY)과 REG/CURV/UNSTRUC + NONSTAT 시간 신택스 명시 (`:2339-2346`).

### 3.3 READ — 좌표·입력장·비정형격자 읽기 (`:2463-2600`)

선행조건: `logcom(2)`(CGRID) 없으면 `msgerr(3,'define computational grid before reading coordinates or input grids')` (`:2467-2468`).

`READ UNSTRUC` 분기 (`:2472-2508`):
- `optg/=5`면 에러 (`:2474-2475`); 1D면 `msgerr(4,'1D simulation cannot be done with unstructured grid')` (`:2477-2479`); 병렬이면 `msgerr(4,'unstructured grid is not supported in parallel run')` (`:2481-2483`)
- generator: `ADC`→`meth_adcirc` (fort.14에서 수심도 가져옴: `logcom(3)=.true.`, `igtype(1)=3`, `leds(1)=2`), `TRIA`→`meth_triangle`, `EASY`→`meth_easy` (`:2490-2503`)
- `call SwanReadGrid(FILENM,LENFNM)` (`:2505`)

그 외엔 `call SwashInputField(logcom)` (`:2510`).

**계산격자 초기화 게이트** (라벨 140, `:2515-2598`): `logcom` 플래그로 좌표·수심 둘 다 준비되면 초기화 호출.
- `optg==1`(rectilinear): `logcom(3) .and. .not.logcom(6)`이면 `SwashInitCompGrid` (`:2517-2519`)
- `optg==3`(curvilinear): 좌표(`logcom(4)`) 선행 필요; 누락 시 `msgerr(3,'give CGRID command and read curvilinear coordinates before reading the bottom grid')` (`:2523-2526`)
- `optg==5`(unstructured): `logcom(5)`(grid 읽음) 필요. 충족 시 `SwanCreateEdges`→`SwanGridTopology`→`SwashInitCompUgrid` 호출 후 'COMPGRID'(U타입)·'ELEMESH'(셀 중심) point set 등록 (`:2534-2596`)

`logcom` 의미(주석 `:181-188`): (2)CGRID, (3)READINP BOTTOM, (4)READ COOR, (5)READ UNSTRUC, (6)s1·u1·v1 할당됨.

---

## 4. ReadInput — 종료·위임·fall-through

- **STOP**: `runmade`(COMP가 한 번이라도 실행됨) 여부로 `comput` 결정 후 `return` (`:286-294`).
- **위임 명령**: INIT→`SwashInitCond` (`:2826`), BOU→`SwashBounCond` (격자 dim을 `MXCGL/MYCGL/MCGRDGL` 전역값으로 임시 치환 후 복원, `:2834-2844`).
- **빈 줄**: `KEYWRD == '    '`이면 `goto 100` (`:2850`).
- **fall-through(미인식 키워드)** (`:2852-2890`): 'NOGRID' single-point set 등록 후 → `SwashReqOutL`(출력 위치) → `SwashReqOutQ`(출력량)로 재해석 시도. 둘 다 `found=.false.`면 `LEVERR=max(LEVERR,3)` + `WRNKEY`(unknown keyword 경고) (`:2876-2888`).

---

## 5. ReadTestpnts — 테스트점 읽기 (`SwashReadTestpnts.ftn90`)

Purpose: "Reads test points and generates point set TESTPNTS" (`:40`).

- 호출: ReadInput의 `TEST ... POI`에서 `SwashReadTestpnts(ipp*mptst, iarr)`; `ipp=2`(정형, ix·iy 쌍) / `ipp=1`(`optg==5` 비정형, vertex 1개) (`SwashReadInput.ftn90:2795-2799`). `mptst=50` (`SwashReadInput.ftn90:85`).
- 입력 형식: `XY`(좌표) vs `IJ`(인덱스) 선택; 선행 READ BOT/UNSTRUC 없으면 `msgerr(3,...)` (`SwashReadTestpnts.ftn90:97-108`).
- 좌표→격자 변환: 정형은 `CVMESH`로 broken index 산출 후 `ix=nint(xc)+MXF` (`:117-126`), 비정형은 `SwanFindPoint`로 vertex `k` (`:129-137`).
- 활성 점 검사: 정형은 `kgrpnt(ix,iy) > 1`이어야 등록 (`:156-160`); 도메인 내인데 비활성이면 `msgerr(1,'test point is not active')` (`:177`), `nptst>mptst`면 `msgerr(2,'too many test points')` (`:179-180`).
- TESTPNTS point set 생성: `psname='TESTPNTS'`, `pstype='P'`, opsdat 링크드리스트에 추가 (`:184-212`).
- DIAGNOSTIC 파일 출력: `FNAME`(기본 'DIAGNOSTIC'), 병렬이면 노드번호 append, 헤더(버전·프로젝트·시간/반복·좌표계·위치·QUANT 헤더 ovsnam(6/11/12/14)) 작성 (`:216-285`).

---

## 6. 비정형 격자 검사·토폴로지·출력

### 6.1 CheckGrid — mesh 품질 검사 (`SwashCheckGrid.ftn90`)

Purpose: "Checks whether the mesh is suited for computation" (`:40`). Method 주석(`:44-54`)에 3개 검사 명시 + Bank(1998) PLTMG·OceanMesh2D 참조.

1. **vertex 둘레 셀 수**: 내부 vertex(`vmark(i)==0`)에서 `4 ≤ noc ≤ 10`이어야 함; 위반 시 `badvertex=.true.` → `msgerr(1,'number of cells around vertex is smaller than 4 or larger than 10')` (`:122-141`).
2. **삼각형 예각 검사**: 세 각의 cosine(`cosphi1/2/3`) 계산, 90°(`cosphi≤0`) 초과 시 `ITEST>=100`에서 각도 경고 (`:149-191`). 전체가 예각이면 `msgerr(0,'The grid contains solely acute triangles ')` (`:195`).
3. **mesh quality** (`:197-249`): 각 셀 품질 $q_e = \dfrac{4\sqrt{3}\,A}{\sum_f \ell_f^2}$ (등변삼각형=1, 퇴화=0). `fac=4.*sqrt(3.)`, `qe(i)=fac*area/lsq` (`:200,224`). 평균 `qem`·표준편차 `qstd` 산출, `mshq = qem - 3.*qstd` (`:230-242`). `mshq>0.75 .or. qem>0.9`면 'high quality', 아니면 `msgerr(1,'The grid is of poor quality (may contain degenerated elements)')` (`:245-249`). 평균품질 % 출력 (`:250,255`).

### 6.2 BndTopology — 경계 토폴로지 (`SwashBndTopology.ftn90`)

Purpose: "Setups the boundary topology" (`:40`). cell/face 객체에서 marker로 경계 요소 수집:
- 경계 cell: `cell(icell)%atti(CMARKER) /= 0`인 셀을 linked list로 모아 `ncellsb` 카운트 후 `jbcell(ncellsb)` 배열에 인덱스 저장 (`:90-114`).
- 경계 face: `face(iface)%atti(FMARKER) /= 0`인 face를 동일 방식으로 `nfacesb`·`jbface` (`:118-142`).

### 6.3 PrintGridInfo — mesh 통계 출력 (`SwashPrintGridInfo.ftn90`)

Purpose: "Prints some relevant information concerning the mesh" (`:40`).
- generator 라벨: `meth_adcirc`→'SMS/ADCIRC', `meth_triangle`→'Triangle', `meth_easy`→'Easymesh' (`:80-106`).
- 내부 수 산출: `nfacesi=nfaces-nfacesb`, `ncellsi=ncells-ncellsb` (`:110-111`); vertices/cells/faces 통계 PRINT (`:115-116`).
- 격자 크기: 내부 face(`FMARKER==0`)의 `FACEDISTG`(인접 centroid 거리 역수 `rdx`)에서 `gridsize=1./rdx` 산출, min/max/avg 집계 후 출력 (`:120-160`).

---

## 7. CheckPrep — 정합성 검사 + 계산 전 준비

### 7.1 Purpose (verbatim)

`SwashCheckPrep.ftn90:56-59`:
```
!   Purpose
!   Checks inconsistencies in settings and changes if necessary
!   Does some preparations before computation is started
```

### 7.2 구조

6006줄의 대부분은 `! check <항목>` 주석으로 구획된 **순차적 정합성 검사 블록**들이다(grep로 50+개 `! check` 섹션 확인). 패턴은 `msgerr(level, msg)` 호출:
- level **3/4**: 치명적 — 계산 불가(설정 모순)
- level **2**: 심각 경고
- level **1**: 경고 + 흔히 기본값으로 자동 보정
- level **0**: 정보성 안내

검사 직후 loop bound 설정(`mf/mfu/ml/mlu`, `nf/nfu/nl/nlu`)·병렬 halo 보정(`IHALOX/IHALOY`)·계산 준비를 수행 (`:219-263`).

### 7.3 주요 검사 항목 카탈로그

grep `call msgerr`로 확인한 대표 검사들 (file:line은 msgerr 호출 라인):

| 카테고리 | 검사 내용 (요지) | 라인 / level |
|---|---|---|
| 계산격자 | `mxc<=1 & optg/=5` → 'no valid computational grid; check command CGRID' | 185 / 3 |
| 계산격자 | `mcgrd<=1 & nverts<=0` → READ BOT/UNSTRU 확인 | 186 / 3 |
| 병렬 repeat | ORB 분할 + repeat grid 금지 | 198 / 3 |
| repeat+dim | 1D repeat 금지, unstruc repeat 불가, MXC/MYC 최소값 | 205-212 / 3 |
| 격자분할 | 2DH 수심평균 비정수압은 stripwise 분할 필요 | 217 / 3 |
| 입력장 | bottom grid 미정의/미입력 | 276-277 / 3 |
| 입력장 짝 | VX 읽었는데 VY 없음(WY/AVY/DRAFT/ACUR도) | 280,289,306,311,321 / 3 |
| 바람/압력 | space-varying wind 없는데 pressure 읽음 | 331 / 3 |
| 모멘텀 skip | SKIPMOM인데 transport 미지정·layer-averaged 불가 | 360-361 / 3 |
| Coriolis | 1D에서 Coriolis 없음(경고) / 구면 무시 | 375,386-387 / 1 |
| 초기조건 | hot-start에 ramp 적용 부적절 | 396-398 / 1 |
| 수직격자 | 가변 두께 층 최소 1개 필요 | 441 / 3 |
| subgrid | 부유체·unstruc와 subgrid 비호환, 가변층만 허용 | 491-495 / 3 |
| 비정수압 | 수심평균/1압력층에서 box 스킴만 | 563 / 1 |
| reduced PPE | standard layout·floating과 비호환, 층수 과다 | 572-582 / 1,3 |
| 시간적분 | mimetic은 semi-implicit 필요 | 712 / 3 |
| 난류 | 3D 난류 + roughness/log-law/k-eps/비정수압 정합 | 735-753 / 3 |
| 식생 | 입력 필요, added mass 계수 | 769,773 / 1,3 |
| 수송 | 입력격자 필요, return time | 784,790 / 1,3 |
| anti-creep | Stelling–Van Kester는 repeat 금지 | 799 / 3 |
| 퇴적물 | k-eps·log-law 필요, settling velocity/diameter | 845-848,826,833 / 1,3 |
| ambient | semi-implicit·unstruc와 비호환 | 873-874 / 3 |
| drying | `epsdry`: 음수/0이면 5e-5, 1cm 초과면 0.01로 보정 | 1185-1190 / 1 |
| runup | `hrunp`·`delrp`: 양수 아니면 `epsdry`로 보정 | 1197,1210 / 1 |
| porosity | grain size·structure height·friction 계수 | 1226-1238 / 1,2 |
| CFL | `pnums(2)`(low)·`pnums(3)`(high) ∈(0,1), high>low; 위반 시 0.4/0.8로 보정 | 1245-1256 / 1 |
| implicitness | `pnums(1)/(4)` θ ∈[0.5,1], 위반 시 0.5 | 1265-1271 / 1 |

CFL 보정 후 `cflmax = 0.5*(pnums(2)+pnums(3))` 초기화 (`:1261`).

### 7.4 계산 전 준비(prep) 동작

검사 외에 CheckPrep은 여러 초기화/준비를 수행한다(끝부분 인용, `:6006` 부근):
- `SwashForcesRigidBod` 호출(강체 force) (`tail`)
- 준정상류면 `SwashInitSteady`(Chezy 기반 유속 초기화, `optg/=5 & instead`) (`tail`)
- subgrid면 coarse(pressure) 격자로 유속 사영: `u1p(:,i) = Σ hku*u1 / hkuc` (`tail`)

---

## 8. PrintSettings — 설정 출력 (`SwashPrintSettings.ftn90`)

Purpose: "Prints all the settings used in SWASH run" (`:40`). `ITEST>0`일 때 SwashMain이 호출 (`SwashMain.ftn90:183`).

PRINT 파일에 모드별 설정을 출력: 1D/linearized SWE/non-hydrostatic/depth-averaged·층수·reduced pressure(`qmax`)·approx dispersion·mimetic (`:67-119`); 좌표계(nautical/Cartesian·spherical) (`:121-131`); 격자(rectilinear/curvilinear/unstructured·MXC/MYC/MCGRD·DX/DY) (`:133-155`); 물리상수(GRAV/RHOW/RHOA/DYNVIS) (`:163-164`); 바람(`iwind` 1-4)·바닥마찰(`irough` 1-11)·식생·breaking·밀도·Coriolis·transport·점성(`ihvisc`/`iturb`)·porosity (`:166-290`); 수치 스킴(leap-frog/semi-implicit θ·advection PROPSC/KAPPA per term)·projection(`iproj`)·rigid body solver(Newmark/Chung-Hulbert/HHT/WBZ)·sponge 폭·참조시각 (`:292-384`). 포맷 라벨 201-254 (`:386-445`).

---

## 9. 핵심 관찰 / 설계 노트

1. **단일 거대 dispatcher**: ReadInput은 ~34개 최상위 키워드를 `KEYWIS` 연쇄로 처리하는 flat dispatch. 미인식 키워드는 출력 명령(SwashReqOutL/Q)으로 fall-through, 최종 실패 시 `LEVERR=3` (`:2885-2887`).
2. **`logcom` 게이트**: 격자 좌표·수심이 모두 준비되어야 `SwashInitCompGrid/Ugrid`가 호출되는 lazy-init 패턴 (`:2515-2598`).
3. **검사-보정 이원화**: CheckPrep은 level 3/4로 abort하거나 level 1로 자동 기본값 보정(epsdry·CFL·θ 등)을 일관 적용 — 사용자 실수에 robust.
4. **비정형 격자 분리 경로**: CheckGrid/BndTopology/PrintGridInfo는 ReadInput이 아니라 Swan* 토폴로지 빌더 체인에서 호출되어 SWAN 비정형 인프라를 재사용 (§0).

> source-needed: 각 명령의 manual 정식 신택스 전체(예: SOUR/SPON/DISCRET 내부 파라미터 의미)는 본 노트에서 진입 라인만 검증; 세부 파라미터 매핑은 별도 manual-notes 필요.
