---
title: "Delft3D WAQ 입출력 + 프로세스 전처리 — 10블록 입력 파서 → proc_preprocess(라이브러리→활성 프로세스 선택) → 워크파일"
model: Delft3D
component: waq/waq_io + waq_proc_preprocess
canonical_source: self
citation_status: verified
verification_method: "Delft3D 소스 직접 read (src/engines_gpl/waq/). 입력 블록 드라이버 delwaq1_read_input_data.F90:55-179, 블록 리더 inputs_block_1/7.f90, 전처리 오케스트레이터 dlwqp1.f90:53-829, 프로세스 라이브러리 NEFIS 리더 rd_tabs.f90·process_lib_data.f90, 활성 프로세스 선택 set_active.f90·prprop.f90, 활성화 판단 makbar.f90·primpro.f90·getinv.f90, 통계 프로세스 delwaq_statistical_process.f90·read_statistical_specs.f90 의 헤더 주석·인자 선언·호출 시퀀스를 file:line 인용. 일부 하위 table 리더(rd_tabr3~8)·setopo/setopp/partab 내부 알고리즘은 헤더만 확인(source-needed 표기)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/source-analysis/delft3d_delwaq.md
  - models/Delft3D/README.md
---

# Delft3D WAQ 입출력 + 프로세스 전처리

> DELWAQ(D-Water Quality) 의 `delwaq1` 전처리 단계 — ASCII 입력 10블록 파싱 → 프로세스 라이브러리(NEFIS) 로딩 → 사용자가 켠 물질·상수·출력에 맞는 활성 프로세스 집합 자동 선정 → 바이너리 워크파일 생성. (경로: `src/engines_gpl/waq/waq_preprocessor/`, `waq_io/`, `waq_proc_preprocess/`)

WAQ 솔버 자체(`waq_kernel`)와 수질 반응식(`waq_process`)은 별도 노트 영역. 본 노트는 **입력 파싱 + 프로세스 선택 전처리**에 집중한다. 모델 전체 구조는 [[delft3d_delwaq]], 엔진 맵은 [[delft3d_engines_overview]] 참조.

---

## 1. 큰 그림: delwaq1 = 전처리기

DELWAQ 은 두 단계 실행이다: **`delwaq1`(전처리)** 가 ASCII 입력과 프로세스 라이브러리를 읽어 바이너리 워크파일을 만들고, `delwaq2`(시뮬레이션) 가 워크파일을 읽어 적분한다. 본 노트가 다루는 `waq_io`/`waq_proc_preprocess` 는 전부 `delwaq1` 안에서 호출된다.

전처리의 메인 드라이버는 `waq_preprocessor/delwaq1_read_input_data.F90` 으로, 두 큰 단계를 순차 호출한다:

1. **블록 1~9 + 통계 블록 10 입력 파싱** (`waq_io` 의 `read_block_N_*`)
2. **프로세스 스티어링 정의** `dlwqp1` (`waq_proc_preprocess`)

호출 시퀀스 (`delwaq1_read_input_data.F90:59-176`):

| 호출 | 라인 | 역할 |
|---|---|---|
| `read_block_1_from_input` | :59 | 모델 ID + 물질명 |
| `read_block_2_from_input` | :90 | 타임프레임·모니터링·통합옵션 |
| `read_block_3_grid_layout` | :97 | 격자/레이아웃 |
| `read_block_4_flow_dims_pointers` | :107 | 흐름 차원·교환 포인터·이송 |
| `read_block_5_boundary_conditions` | :119 | 개방경계 |
| `read_block_6_waste_loads_withdrawals` | :128 | 오염부하·취수 |
| `read_block_7_process_parameters` | :142 | **프로세스 파라미터(상수/함수)** |
| `read_block_8_initial_conditions` | :151 | 초기조건 |
| `read_block_9` | :155 | 출력 옵션 |
| `setup_statistical` | :159 | **통계(시간평균) 프로세스 정의** |
| `dlwqp1` | :170 | **프로세스 스티어링 전처리** |

---

## 2. 입력 블록 파서 (`waq_io`)

### 2.1 블록 구조 개요
`waq_io/src` 는 블록별 리더로 구성된다(`inputs_block_1.f90` ~ `inputs_block_9.f90`). 각 블록은 토큰화 입력(`rd_token` 모듈)으로 읽는다. 보조 유틸: `read_block.f90`(프로세스 파라미터·초기조건용 공통 데이터 블록 리더, `read_block.f90:38` "Reads a block of input items ( procesparameters, initial conditions )"), `usefor.f90`(USEFOR 매핑 압축), `boundary_conditions.f90`, `initial_conditions.f90`, `read_hydfile.f90`(hyd-파일 파싱, `read_hydfile.f90:36` "Reads the hyd-file and extracts relevant information").

### 2.2 블록 1 — 모델 식별 + 물질
`read_block_1_from_input` (`inputs_block_1.f90:40`) 헤더 주석이 읽는 항목을 verbatim 명시 (`inputs_block_1.f90:45-52`):

```
!> This routine reads:
!>    - the first non tokenized line with line lengthes and comment character
!>    - the version number of the input file
!>    - the 3 40 character strings with model documentation
!>    - a 4th 40 character strings with the optional absolute reference time
!>    - number of transported and passive substances
!>    - the substance names (need not necessarily be process library reserved names)
!>      the names may end with *nn to indicate a multiple occurence of the substance
```

- 핵심 출력 인자: `num_substances_transported`(이송 물질 수), `num_substances_total`(전체=이송+passive), `syname`(물질명 배열) (`inputs_block_1.f90:63,72-73`).
- 물질명의 `*nn` 접미사 → **multiple substance** 행정으로 분리됨 (`nomult`, `multp`, `inputs_block_1.f90:70-71`). 이 multiple 물질은 후속 `dlwqp1` 에서 fraction 프로세스로 전개됨(§4.6).
- 사용 logical unit 매핑도 주석에 명시: `file_unit_list(26)`=사용자 입력, `(27)`=stripped 입력, `(29)`=포맷 출력, `(2)`=중간 시스템 파일 (`inputs_block_1.f90:54-57`).

### 2.3 블록 7 — 프로세스 파라미터
`read_block_7_process_parameters` (`inputs_block_7.f90:35`, 주석 "Reads block 7 of input, process parameters") 가 프로세스가 소비할 **상수(constants)·파라미터(parameters)·시간함수(functions)·segment-함수(segfuncs)** 를 읽어 `t_waq_item` 자료구조에 적재 (`inputs_block_7.f90:69-75`). 이 데이터가 §4 의 활성 프로세스 판단(`makbar`)·입력 포인터 해소(`getinv`) 의 가용 변수 풀이 된다. SURF·LENGTH 존재 검사 플래그 `chkpar(2)` 전달 (`inputs_block_7.f90:62`).

### 2.4 통계 프로세스 블록(블록 10)
`setup_statistical` (`statistical_processes/delwaq_statistical_process.f90:43`, 주석 "Defines process steering for statistical output processing"). 내부에서 먼저 `rdstat`(`read_statistical_specs.f90:33`, "Reads statistical output spec. block 10") 로 키-값 블록을 읽는다. 인식 최상위 키 (`read_statistical_specs.f90:93-96`):

```
keys(1) = 'VERSION'
keys(2) = 'MINOR'
keys(3) = 'PERIOD'
keys(4) = 'OUTPUT-OPERATION'
```

각 `OUTPUT-OPERATION` 의 값으로 통계 연산 종류를 분기 (`delwaq_statistical_process.f90:118-132`): `STADAY`(일평균), `STADPT`, `STADSC`, 그리고 (이후 라인의) `STAGEO`(기하평균)·`STAMEA`(평균)·`STADEV`(표준편차)·`STAPRC`·`STAQTL`(분위수) — 대응 setter 모듈이 `delwaq_statistical_process.f90:26-33` 에 use 됨 (`m_setqtl, m_setprc, m_setgeo, m_setdsc, m_setmea, m_setdev, m_setdpt, m_setday`). 결과는 `statprocesdef`(통계 프로세스 정의 컬렉션) 로 적재되어 §4 의 일반 프로세스 정의와 합쳐진다.

---

## 3. 프로세스 라이브러리 = NEFIS 테이블

활성 프로세스 선택은 **프로세스 정의 파일(proces definition file, 기본 `proc_def`)** 에 기반한다. 이는 NEFIS 바이너리 포맷.

### 3.1 라이브러리 적재 `rd_tabs`
`rd_tabs` (`rd_tabs.f90:32`, 주석 "read process definition tables from nefis format", `:37`) 가 NEFIS 그룹 P1~P5 + R1~R8 + M1 을 순차로 읽는다 (`rd_tabs.f90:43-56` 의 `use m_rd_tabp1..5, m_rd_tabr1..8, m_rd_tabm1`). 확장자 유무로 단일 파일 vs `.dat`/`.def` 쌍을 판별 (`rd_tabs.f90:106-126`), NEFIS `crenef` 로 read-only 오픈 (`rd_tabs.f90:133-135`). `dlwqp1.f90:359` 에서 호출되며 실패 시 `-p`(파일경로)/`-np`(프로세스 없음) 옵션 안내 후 중단 (`dlwqp1.f90:360-372`).

### 3.2 테이블 스키마 (`process_lib_data.f90`)
읽힌 테이블은 `m_process_lib_data` 의 공통블록에 저장된다. 각 테이블의 FUNCTION 주석(verbatim):

| 테이블 | 리더 | 내용 (주석) | 자료구조 |
|---|---|---|---|
| P1 | `rd_tabp1.f90:41` "Read TABLE_P1 group" | substance groups | `sgrpid, sgrpnm` (`process_lib_data.f90:50-51`) |
| P2 | `rd_tabp2.f90:46` | items (모든 항목 메타: 단위·이름·기본값) | `itemid, itemun, itemnm, itemde, itemgr...` (`:68-78`) |
| P3 | `rd_tabp3.f90:41` "Maximum number of FORTRAN process modules" | FORTRAN 서브루틴 | `fortid, fort_i` (`:86-87`) |
| P4 | `rd_tabp4.f90:42` "maximum number of processes" | **프로세스** | `procid, procfo, procnm, procco` (`:93-95`) |
| P5 | `rd_tabp5.f90:41` "maximum number of configurations" | configurations | `confid, confnm` (`:109-110`) |
| R1 | `rd_tabr1.f90:41` "configurations * processes" | **config↔process 매트릭스** | `conpro(nconfm,nprocm), r1_cid, r1_pid` (`:122-125`) |
| R2 | `rd_tabr2.f90:41` | config↔substance | `r2_cid, r2_sid, r2_iin` (`:131-133`) |
| R3 | `rd_tabr3.f90:43` | **입력 아이템** (프로세스의 input) | `inpupr, inpuit, inpude, inpunm...` (`:139-142`) |
| R4 | `rd_tabr4.f90:43` | **출력 아이템** | `outppr, outpit, outpnm...` (`:149-152`) |
| R5 | `rd_tabr5.f90:42` | **출력 flux** | `outfpr, outffl...` (`:159-161`) |
| R6 | `rd_tabr6.f90:42` | **stochi(화학량론) 라인** | `stocfl, stocsu, stocsc` (`:167-168`) |
| R7 | `rd_tabr7.f90:42` | velocity 라인 | `veloit, velosu, velosc` (`:175-176`) |
| R8 | `rd_tabr8.f90:42` | dispersion 라인 | `dispit, dispsu, dispsc` (`:183-185`) |
| M1 | `rd_tabm1.f90:50` "Read TABLE_M1 (old_items)" | 구→신 이름/기본값 변환 | `old_items_*` (`:199-204`) |

여기서 P4(프로세스)·R3(입력)·R4(출력)·R5(flux)·R6(stochi) 가 프로세스 선택의 핵심: 각 프로세스가 **무엇을 필요로 하고(R3) 무엇을 만드는지(R4/R5)** 와 **flux 가 어떤 물질에 어떤 계수로 작용하는지(R6)** 를 정의한다.

> ⚠ rd_tabr3~r8 의 내부 NEFIS 읽기 루프 세부는 헤더 FUNCTION 주석만 확인. 필드별 읽기 순서는 source-needed.

### 3.3 old_items 변환 테이블 (M1)
`process_lib_data.f90:197-204` 에 명시: 구 버전 입력 이름/기본값을 신규로 변환. 필드 `old_items_old_name`, `_new_name`, `_old_default`, `_configuration`, `_serial`(이 이름이 쓰이던 라이브러리 직렬번호), `_action_type`(rename / param rename / default change). `dlwqp1.f90:382` 의 `fill_old_items` 로 채워지고 `set_old_items`(`dlwqp1.f90:538`) 가 사용자 입력 이름을 라이브러리 기준으로 치환. `-target_serial` 옵션으로 대상 직렬 지정 가능 (`dlwqp1.f90:389-404`).

---

## 4. 프로세스 스티어링 전처리 `dlwqp1`

`dlwqp1` (`dlwqp1.f90:53`) 헤더 주석이 목적을 명시 (`dlwqp1.f90:59-66`):

```
!> Defines process steering for all water quality processing
!> This routine processes all information of
!>    - processes that have been switched on
!>    - constants and functions that have been supplied
!>    - output variables that have been asked to become available
!>      to a consistent set of sequential processes for the simulation part
```

즉 **사용자가 켠 것 + 입력 가용 변수 + 요청 출력** → 일관된 순차 프로세스 집합으로 변환. 버전 상수 `versip = 5.07`, 최대 프로세스 `nbprm = 1750`, 최대 변수 `novarm = 15000` (`dlwqp1.f90:105-108`).

### 4.1 활성 프로세스 모드 결정
두 가지 선택 모드:
- **active-only 모드** (`laswi=.true.`): 사용자가 `ACTIVE_<name>` 형식 상수 또는 `only_active` 상수를 주면 켜짐 (`dlwqp1.f90:588-596`). `set_active` 가 상수 리스트에서 `active`로 시작하는 이름을 스캔해 활성 리스트 `actlst` 구성 (`set_active.f90:38` "makes list of active processes", `:74-93`). 이름은 8번째 문자부터 추출 (`set_active.f90:79` `name10 = constants%name(ico)(8:17)`). bloom 활성 시 `phy_blo` 출력 프로세스 자동 추가 (`set_active.f90:97-115`, 메시지 "Automatic activation of BLOOM ouput process Phy_Blo" `:121`).
- **configuration 모드** (`laswi=.false.`): `-conf` 옵션 또는 기본값. eco 모드면 `'eco'`, 아니면 `'waq'` (`dlwqp1.f90:608-616`).

> 참고: `prprop.f90:113` 에서 `laswi = .true.` 를 강제 설정하며, 그 위 주석은 구 라이센스 시스템 잔재 제거 표시("MDK 27-05-2022: this is a remnant of an old licensing system. To be removed", `prprop.f90:111`). 즉 현재 실효적으로 config 라이센스 체크는 우회됨.

### 4.2 라이브러리→정의 구조 변환 `prprop`
`prprop` (`prprop.f90:32`, 주석 "fills proces properties from PB nefis tables", `:38`) 가 §3 의 NEFIS 테이블을 순회해 활성 대상 프로세스를 `procesdef`(타입 `procespropcoll`) 구조로 적재 (`dlwqp1.f90:631-634`). 각 프로세스의 input(R3)·output(R4)·fluxoutput(R5)·flux stochi(R6)·velo/disp stochi(R7/R8) 컬렉션을 채운다 (`prprop.f90:67-76` 의 `input_item, output_item, FluxOutput, FluxStochi, VeloStochi, DispStochi`).

이후 통계 프로세스(`statprocesdef`)도 같은 `procesdef`에 병합 (`dlwqp1.f90:641-649`).

### 4.3 BLOOM(조류) eco 모드
`-eco` 옵션 또는 `ACTIVE_BLOOM_P` 상수 존재 시 eco 모드 활성 (`dlwqp1.f90:427-457`). `reaalg`(`dlwqp1.f90:498`)가 BLOOM 종 정의 파일(.spe)을 읽어 조류 타입/그룹/계수를 적재. proto 프로세스를 실제 프로세스로 치환: `actrep`(상수 리스트, `dlwqp1.f90:582`), `cnfrep`(config 정보, `:626`), `algrep`(프로세스 파라미터 이름, `:678`). BLOOM efficiency 파일 `bloominp.frm` 생성 (`blmeff`, `dlwqp1.f90:685-686`).

### 4.4 프로세스 정렬 `prsort`
`prsort` (`prsort.f90:34`, 주석 "sort processes according to input - output relation, simpel linear sort at the moment", `:38`) — 한 프로세스의 출력이 다른 프로세스의 입력이 되는 의존관계를 따라 실행 순서를 위상정렬(현재는 단순 선형정렬). `dlwqp1.f90:658` 호출.

### 4.5 활성화 가능성 판단 `makbar`
`makbar` (`makbar.f90:35`, 주석 "Checks which processes can be activated", `:41`) — 각 프로세스의 모든 입력 아이템이 가용한지(물질 syname / 상수 / 파라미터 paname / 함수 funame / segment함수 sfname / 분산 diname / 속도 vename 중에서 찾을 수 있는지) 검사해, 입력이 충족되면 켤 수 있다고 판정. 프로세스당 최대 누락변수 `mismax=50` (`makbar.f90:79`). `dlwqp1.f90:702-706` 호출. (Cf. "barrier" 의미 — 활성화 차단 여부.)

### 4.6 1차 프로세스 + 화학량론 `primpro`
`primpro` (`primpro.f90:33`, 주석 "detect and activate primary processes (which act directly on substances)", `:38`) — 물질에 직접 작용하는 1차 프로세스를 검출. 물질별로(`primpro.f90:98` `do isys = 1, num_substances_total`) 모든 프로세스의 flux stochi 를 훑어, 계수가 0 이 아니고(`abs(...)>1e-10`, `:117`) 해당 물질에 작용하는 flux 를 찾아 연결 (`primpro.f90:107-130`). 동시에 분산(disp)·속도(velo) stochi 를 처리해 `dsto`/`vsto` 계수 배열과 신규 결합 분산/속도 포인터(`idpnw, ivpnw`)를 구성 (`primpro.f90:55-60`, `dlwqp1.f90:720-723`).

물질 fraction 전개(`*nn` multiple 물질, §2.2)는 `set_fraction`(`dlwqp1.f90:653`)이 `procesdef`에 프로세스·flux 를 추가/변경하며 처리.

### 4.7 입력 포인터 해소 `getinv`
`getinv` (`getinv.f90:34`, 주석 `:40-42`):
```
! sets the i/o pointers for every proces
! if nessacary turns on secondary processes
! fills defaults in defaul array
```
각 프로세스 입력을 WAQ 데이터 공간(상수/파라미터/함수/세그먼트함수/물질/local) 의 인덱스로 매핑 (`valpoi`/`vxlpoi` 사용, `getinv.f90:24-27`). 다른 프로세스의 출력으로만 채워지는 입력이면 그 출력 프로세스를 **2차 프로세스로 자동 활성화**. 충족 못 하면 기본값(`defaul`) 적용 또는 누락 카운트 `nmis` 증가. `nopred=6`개의 사전정의 기본값(예: ITSTRT, ITSTOP) 존재 (`getinv.f90:104`, `dlwqp1.f90:734,738-739`). `nmis>0` 이면 시뮬레이션 불가로 중단 (`dlwqp1.f90:781-788`).

출력 포인터 설정은 `setopp`(요청 출력 위한 프로세스 켜기, `setopp.f90:31-34` "sets processes for requested output", `dlwqp1.f90:727`) + `setopo`(출력 포인터를 parloc/defaul/flux 배열에 설정, `setopo.f90:33-35`, `dlwqp1.f90:777`).

### 4.8 병렬 처리 참조표 `partab`
`partab` (`partable` 모듈, `partab.f90:38`, 주석 "Makes a parallel processing reference table to ensure resolved inputs with parallel processing", `:47-48`) — OpenMP 병렬 실행 시 입력이 미리 해소되도록 선택 프로세스의 참조표 `proref` 를 만든다. 결과 `num_input_ref`, `nothread` (`dlwqp1.f90:768-771`).

---

## 5. 출력: 프로세스 워크파일 `wr_proceswrk`

전처리 결과는 `wr_proceswrk` (`wr_proceswrk.f90:37`, 주석 "write proces work file", `:50`) 로 바이너리 워크파일에 기록 (`dlwqp1.f90:801-809`). 내부에서 `wripro`(프로세스), `wrstoc`(stochi), `setvat`, `intoou` 를 호출 (`wr_proceswrk.f90:54-58`). 기록 내용: 프로세스 정의·기본값 배열 `defaul`·신규 분산/속도 포인터(`idpnw, ivpnw`)·stochi 계수(`dsto, vsto`)·local 변수명·각종 카운트(상수/파라미터/함수/물질 수). 이 워크파일을 `delwaq2` 솔버가 읽어 매 시간스텝 프로세스를 실행한다.

부수 산출: `repuse`(입력 사용 리포트, `repuse.f90:35-36` "report on the use of the delwaq input", `dlwqp1.f90:763`), `proc_totals`(input/output/flux/stochi/disp/velo 총개수 집계, `proc_totals.f90:31`, `dlwqp1.f90:693`), `outbo2`(출력 부트 차원, `dlwqp1.f90:668`).

---

## 6. 전체 파이프라인 요약

```
delwaq1_read_input_data.F90
 ├─ read_block_1..9 (waq_io)          ← ASCII 입력 토큰 파싱
 │    └─ block1: 물질명·multiple(*nn)
 │       block7: 상수/파라미터/함수
 ├─ setup_statistical                 ← 블록10 통계 프로세스 → statprocesdef
 └─ dlwqp1 (waq_proc_preprocess)      ← 프로세스 스티어링
      ├─ rd_tabs → process_lib_data   ← NEFIS proc_def (P1..5, R1..8, M1)
      ├─ set_old_items                ← 구→신 이름 변환(M1)
      ├─ set_active / config 결정      ← 어떤 프로세스 후보?
      ├─ prprop                        ← 라이브러리 → procesdef 구조
      ├─ + statprocesdef 병합 / set_fraction (multiple 물질)
      ├─ prsort                        ← 입출력 의존 정렬
      ├─ makbar                        ← 입력 충족 여부 → 활성화 가능 판단
      ├─ primpro                       ← 물질 직접작용 1차 프로세스 + stochi
      ├─ getinv                        ← 입출력 포인터 해소 + 2차 프로세스 자동활성
      ├─ partab                        ← 병렬 참조표
      └─ wr_proceswrk                  ← 바이너리 프로세스 워크파일 (→ delwaq2)
```

핵심: 사용자는 물질과 "ACTIVE_xxx" 상수만 지정하고, 전처리기가 **프로세스 라이브러리의 입출력 의존 그래프를 풀어** 필요한 모든 1차·2차 프로세스를 자동 선택·정렬·연결한다.

---

## 미확인 / source-needed
- rd_tabr3~r8 의 NEFIS 필드별 읽기 루프 세부 (헤더 FUNCTION 주석만 확인).
- `setopo`/`setopp`/`partab`/`getinv` 의 포인터 산술 세부 인덱싱 (offset 계산 `ioff = nopred + num_constants + ... ` `dlwqp1.f90:698,711` 외 내부 루프 미정독).
- 통계 setter(`setday`/`setmea`/`setgeo`/`setqtl` 등) 의 개별 연산 정의 (모듈 use 만 확인, 본문 미정독).
- `set_fraction` 의 fraction 프로세스 생성 알고리즘 세부 (호출 지점만 확인).
- WAQ 솔버 적분(`delwaq2`)·수질 반응식 본체(`waq_process`) 는 본 노트 범위 밖 → [[delft3d_delwaq]] 영역.
