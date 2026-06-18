---
title: "LISFLOOD-FP IO·외력 — parfile/DEM/bci/bdy 입력, 수심/flux 출력, 경계조건, checkpoint, 침투·증발·강우"
model: LISFLOOD-FP
component: io-boundary (input.cpp · output.cpp · boundary.cpp · pars.cpp · chkpnt.cpp · infevap.cpp)
canonical_source: self
citation_status: verified
verification_method: "전 6파일 직접 Read. 핵심 단언은 file:line 직접 확인 — pars.cpp:136-1019(CheckParam 키워드 디스패치)·1090-1145(parfile 파서), input.cpp:1330-1521(DEM)·1526-1837(bci)·1848-2122(bdy/TimeSeries), output.cpp:39-186(ascii)·497-625(binary)·756-998(write_regular_output), boundary.cpp:16-559(BCs)·1327-1410(BoundaryFlux)·1422-1474(InterpolateTimeSeries), chkpnt.cpp:34-314, infevap.cpp:14-126. BC enum lisflood.h:177-190."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "[[lisflood-fp-architecture-source-map]]"
---

# LISFLOOD-FP IO·외력 (input/output/boundary/pars/chkpnt/infevap)

전체 솔버 구조·main 흐름은 [[lisflood-fp-architecture-source-map]] 참조. 본 노트는 **외부 파일과 모델 간 인터페이스**(파라미터·DEM·경계·시계열·재시작·수문 외력)에 집중.

## 1. 파라미터 파일 파싱 (`pars.cpp`)

### 진입·디스패치 구조
`ReadConfiguration`(pars.cpp:27) → `ReadParamFile`(parfile) → `ReadCommandLine` → `CheckParams`(검증). 명령행 인자 마지막이 par 파일이며 `-`로 시작하면 거부 (pars.cpp:39-43). `-v`는 별도로 `ReadVerboseMode`(pars.cpp:17)가 먼저 스캔.

`ReadParamFile`(pars.cpp:1090)는 라인 단위로 읽어 (`LINE_BUFFER_LEN` 버퍼) 첫 토큰을 `param_name`(최대 79자)으로, 나머지를 `param_value_ptr`로 분리(pars.cpp:1123-1135). `#`·빈 줄·CRLF-only 줄은 skip (pars.cpp:1118-1120). 그 후 `CheckParam`으로 디스패치.

### 키워드 디스패치 (`CheckParam`, pars.cpp:136-1020)
하나의 거대한 if-체인. 4종 헬퍼로 매칭(대소문자 무시 `STRCMPi`):

| 헬퍼 | pars.cpp | 형식 |
|---|---|---|
| `read_string_param` | 54 | `%255s` 파일명 (255자 초과 시 abort) |
| `read_numeric_param` | 75 / 93 | `NUM_FMT`(float/double); 93은 실패 시 default 사용 |
| `read_integer_param` | 108 | `%i` |
| `read_empty_param` | 124 | 값 없는 플래그 키워드 |

매칭되면 대응 `Fnameptr`/`Parptr`/`Solverptr` 필드를 채우고 관련 `Statesptr` 플래그를 ON. 매칭 실패 라인은 마지막에 "Unknown parameter ignored" 경고만(pars.cpp:1019) — **오타가 조용히 무시됨**.

### 주요 입력 파일 키워드 → 파일명 필드
| parfile 키워드 | 필드 / 효과 | pars.cpp |
|---|---|---|
| `DEMfile` | `demfilename` | 143 |
| `startfile` / `binarystartfile` | 초기 수심 재시작 (ascii/binary 상호배타) | 145-157 |
| `startelev` | 재시작값을 수면표고로 해석 | 158 |
| `resroot` / `dirroot`(=`dir`) | 출력 prefix / 폴더 | 164-175 |
| `Qfile`,`manningfile`,`riverfile` | 유량/조도/하천망 | 232-247 |
| `bcifile` / `bdyfile` | 경계 식별 / 시변 경계 시계열 | 248-251 |
| `weirfile`(=`weir`) | 위어 | 252 |
| `infiltration`(=`inf`) / `infilfile` | 균일/분포 침투 → `calc_infiltration` ON | 486-497 |
| `evaporation` / `rainfall` / `rainfallmask` | 증발/강우/강우 마스크 | 499-517 |
| `SGCwidth`,`SGCbed`,`SGCchanprams`… | sub-grid channel 입력군 | 814-852 |
| `checkpoint [hrs]` / `loadcheck` | 재시작 빈도 / 대체 체크파일 | 563-574 |
| `damfile`,`dammask` | 댐 (SGC 전용) | 907-922 |

### 솔버 선택 키워드 (상호배타, cfl/DepthThresh 자동설정)
`acceleration`(307), `Roe`/`Roe_slow`(410-429), `fv1`/`fv2`(582-599), `dg2`(630), `acc_nugrid`(600), `mwdg2`(610), `hwfv1`(620). 각각 충돌 조합(`adaptoff`+`acceleration` 등)은 `exit(1)` (pars.cpp:317-323, 430-436).

### 출력 형식 키워드
`ascii_out`/`binary_out`/`netcdf_out`(pars.cpp:384-402), `depthoff`/`elevoff`/`vtkoff`(283-298), `qoutput`(329), `voutput`/`hazard`(338-363), `maxdepthonly`(333), `gzip`(895). `netcdf_out`의 실제 NetCDF I/O는 본 6파일이 아니라 `lisflood2/`·`rain/` 하위(예: lisflood2/lis2_output.cpp)에 `_NETCDF` 매크로 가드로 존재 — 본 노트 범위 밖. `dynamicrainfall`은 NetCDF 미컴파일 시 abort (pars.cpp:998-1001).

### 후처리 검증 (`CheckParams`, pars.cpp:1040)
출력형식 전부 OFF면 ascii로 강제(1043-1048). `routing`은 inertial/SGC 없으면 비활성(1052), `latlong`·`DamMode`는 SGC 필수(1057-1066), CUDA 미컴파일 시 `cuda` 옵션 abort(1079-1085).

## 2. DEM·도메인 기하 (`input.cpp`)

### `LoadDomainGeometry` (input.cpp:1470) — Arc/Info ASCII grid 헤더
6줄 헤더를 `fscanf`로 키-값 쌍 파싱(키워드 문자열 `dum`은 버림): `xsz`, `ysz`, `blx`, `bly`, `dx`(cellsize), `NODATA_value`(input.cpp:1482-1491). 정사각 셀 가정 `dy=dx`, `dA=dx*dy`(1489). 좌상단 `tly = bly + ysz*dy`(1490). `dx_sqrt` 미리 계산(1488).

### `LoadDEM` (input.cpp:1330) — 메모리 할당 + 데이터
모든 격자 배열(`H`, `Qx/Qy`는 (xsz+1)×(ysz+1), `maxH`, `DEM`, `ChanMask`/`SegMask` 등) 할당. 솔버별 추가 배열: Roe면 HU/HV/플럭스군(1341-1359), fv1·dg2 전용 할당(1360-1367). `ChanMask`/`SegMask` 초기값 -1(input.cpp:1459-1460). 실제 데이터는 `LoadDEMData`(1502)가 행우선 `fscanf`, **NODATA 셀은 `Parptr->nodata_elevation`로 치환**(input.cpp:1515-1518).

## 3. 경계조건 — 종류와 파싱

### BC 식별자 enum (`lisflood.h:177-190`, `ESourceType`)
| 값 | 상수 | 의미 |
|---|---|---|
| 0 | `NONE0` | 닫힌(zero-flux) 경계 |
| 1 | `FREE1` | 자유유출 (정규유동, 사용자 또는 국지 경사) |
| 2 | `HFIX2` | 고정 수위(수면표고) |
| 3 | `HVAR3` | 시변 수위 (bdy 시계열) |
| 4 | `QFIX4` | 고정 유량 |
| 5 | `QVAR5` | 시변 유량 (bdy 시계열) |
| 6 | `FREE6` | point FREE (SGC 내부 경계) |
| 7/8 | `TRIB7`/`RATE8` | 하천(지류/율) |

### `.bci` 파싱 (`LoadBCs`, input.cpp:1526)
경계 셀 배열 크기 `numBCs = 2*xsz + 2*ysz`(input.cpp:1558) — 도메인 외곽을 1차원으로 펼친 인덱스. 모든 경계 기본값 `NONE0`, `BC_Val=-1`(1564-1569). bci 파일 미지정이면 전부 닫힘(1571-1575).

각 라인 첫 문자로 분기:
- `N`/`W`/`S`/`E` + start/finish 좌표 → 해당 변의 경계 인덱스 구간 `[BCi1,BCi2]` 계산. 도메인 밖 좌표는 clamp (input.cpp:1584-1643). 변별 인덱싱 공식은 BCs 함수와 정확히 대응(아래 §3.1).
- `P`(point source)/`F`(point free) → 셀 인덱스 `xpi/ypi` 계산 `(px-blx)/dx`, `(tly-py)/dy` (input.cpp:1646-1652).

다음 토큰이 BC 종류: `FREE`/`HFIX`/`QFIX`/`QVAR`/`HVAR`. 변 경계는 `BC_Ident[i]` 세팅, point는 `PS_Ident[pi]`(input.cpp:1665-1783). `FREE`의 경사값 처리: adaptive/qlim 모드면 `sqrt(slope)` 미리 저장, 그 외는 raw slope(input.cpp:1680-1688). point는 변 경계 뒤에 와야 함(주석 input.cpp:1742-1744). 잘못된 라인은 경고만(1786). 끝에서 point source 배열을 실제 개수 `pi`로 재할당(input.cpp:1792-1828), `numPS` 확정.

### `.bdy` 시변 경계 (`LoadBCVar`, input.cpp:1944)
bdy 파일은 명명된 시계열 블록들의 모음. `LoadTimeSeries`(input.cpp:1848)가 각 블록을 파싱: 헤더 라인에서 `count`+단위 읽고, `count`개의 `value time` 쌍을 읽음. 시간은 단조증가 강제(아님 시 abort, input.cpp:1905-1909). 단위 `seconds/minutes/hours/days` 인식하여 초로 환산(input.cpp:1920-1932, 미인식 단위는 경고 후 초로 간주).

`LoadBCVar`는 각 시계열의 이름을 `BC_Name`(변)·`Q_Name`(하천)·`PS_Name`(point)과 strcmp 매칭하여 `BC_TimeSeries[i]` 등에 포인터 연결(input.cpp:2020-2059). 미참조 bdy는 경고 후 폐기(2065-2074). bdy 파일 없으면 QVAR/HVAR로 지정됐는데 시계열 없는 경계는 `NONE0`으로 비활성화(input.cpp:2100-2116).

> 주의: `InterpolateTimeSeries`는 `prev_index` 커서를 수정하므로 **thread-safe 아님**(boundary.cpp:1420 주석).

## 3.1 경계 플럭스 계산 (`boundary.cpp`)

### `BCs` (boundary.cpp:16) — 외곽 Qx/Qy 설정
먼저 4변 전부 zero-flux로 초기화(boundary.cpp:32-39). 그 후 `numBCs`개 경계 인덱스를 순회, 변별로 셀 인덱스 `p0`(경계 셀), `p1`(안쪽 셀), 부호 `sign`, 방향 `dir`, `edge`(1=N,2=E,3=S,4=W), 플럭스 포인터 `qptr`를 설정(boundary.cpp:48-95). 닫힌 경계는 Roe 솔버가 아닌 한 skip(boundary.cpp:43).

BC 종류별 처리:
- **FREE1**(boundary.cpp:98): acceleration이면 반-음함적 운동량식, 그 외(원조 LISFLOOD)는 Manning 확산파. 경사 미지정(`BC_Val<-0.999`)이면 국지 수면경사 사용, 아니면 사용자 경사(boundary.cpp:112-157). 유출 방향이 잘못되면 0으로(boundary.cpp:180-183).
- **HFIX2**(boundary.cpp:189): `hflow = max(H[p0], BC_Val - DEM[p0])`. acceleration / 원조 분기(boundary.cpp:229-253).
- **HVAR3**(boundary.cpp:279): `h0 = InterpolateTimeSeries(BC_TimeSeries[BCi], t)`로 시변 수위 보간(boundary.cpp:283). Roe면 RoeBCx/y, 아니면 acceleration/원조(boundary.cpp:291-407).
- **QFIX4**(boundary.cpp:414): `*qptr = -BC_Val * sign * dx` (단위유량×폭).
- **QVAR5**(boundary.cpp:420): `h0 = InterpolateTimeSeries(...)`로 시변 유량(boundary.cpp:422-424), Roe 시 추가 처리.

운동량식(acceleration·HVAR/HFIX) 일반형:
$$ q^{n+1} = \frac{q^n - g\,\Delta t\, h_{flow}\, S_f}{1 + g\,\Delta t\, h_{flow}\, n^2 |q^n| / h_{flow}^{10/3}} $$
(boundary.cpp:236, 369 등). 원조 확산파는
$$ q = \mathrm{sign}\cdot \frac{h_{flow}^{5/3}\, S_f\, \Delta y}{n} $$
(boundary.cpp:157, 252). adaptive_ts면 안정 timestep $0.25\,\Delta y^2/\alpha$로 제약(boundary.cpp:161), qlim면 $Q_{lim}=Q_{limfact}\,dA\,|dh|/(8\Delta t)$로 절단(boundary.cpp:168).

### Roe 경계 (`RoeBCx`/`RoeBCy`, boundary.cpp:563/971)
2D SWE용 Roe 근사 리만 해법의 경계 ghost-cell 버전. 양셀 wet/dry/overtopping/wall 케이스 분기, Roe 평균(`ubarra`,`cbarra`)과 고유값(`a1=u±c`)으로 플럭스 `FHx/FHUx/FHVx` 계산(boundary.cpp:583-667). entropy fix는 `maximum()`로 epsilon 적용(boundary.cpp:609-616).

### `BoundaryFlux` (boundary.cpp:1327) — 질량수지 집계
외곽 4변의 Qx/Qy를 부호로 분류해 `BCptr->Qin`/`Qout` 누적(채널 셀 제외, boundary.cpp:1343-1379). Qy는 북→남 양, Qx는 서→동 양(주석 boundary.cpp:1334, 1356). 하천 QFIX/QVAR 유입(boundary.cpp:1390-1393), point source `Qpoint_pos/neg`(1401-1402), `VolInMT/VolOutMT` 적산(1405-1406).

### `drain_nodata` (boundary.cpp:1476)
`drain_nodata` 옵션 ON 시 NODATA 표고 셀의 물을 제거하고 `Qout`으로 계상(boundary.cpp:1494-1505).

## 4. Checkpoint 재시작 (`chkpnt.cpp`)

바이너리 형식(정밀도 보존, chkpnt.cpp:222). 헤더로 `LF_CheckVersion`+LISFLOOD 버전 기록(chkpnt.cpp:229-230). 버전 불일치·zero-size·도메인 치수(`xsz/ysz`) 불일치 시 처음부터 시작 또는 abort(chkpnt.cpp:98-134).

저장 내용: 시뮬레이션 시간/iteration/MassTotal/Tstep, 격자 `H`·`Qx`·`Qy`·`maxH`·`maxHtm`·`initHtm`·(v>1)`totalHtm`, `ChanMask`/`SegMask`, 경계 누적량 `Qin/Qout/QChanOut/Qpoint_pos/neg`, 기하(dx/dy/dA/코너), 부피·오차, (v>2) 침투/증발 누적손실, 채널 세그먼트별 `ChanQ/A/NewA/JunctionH`(chkpnt.cpp:109-308).

읽기(`ReadCheckpoint`, chkpnt.cpp:34): 기본 체크파일(`checkpointfilename`)을 먼저 시도 — 존재하면 중단된 run 의미. 없으면 `loadcheck` 대체파일(chkpnt.cpp:48-78). 기본파일이 대체보다 우선(chkpnt.cpp:71-75). 쓰기(`WriteCheckpoint`, chkpnt.cpp:211)는 `checkfreq`(시간) 간격 + 종료 시. 파일 열기 실패 시 checkpointing OFF(chkpnt.cpp:223-226).

## 5. 침투·증발·강우·라우팅 (`infevap.cpp`)

### `FPInfiltration` (infevap.cpp:14)
비채널 셀(`ChanMask==-1`)만, `H>DepthThresh`일 때 `cell_inf = InfilRate * Tstep`(깊이율)만큼 감소. 음수 방지 후 `InfilTotalLoss += cell_inf*dA` 질량수지(infevap.cpp:24-39). **균일 율** — 분포 침투는 input.cpp `LoadDistInfil`로 별도.

### `Evaporation` (infevap.cpp:51)
`evap_rate = InterpolateTimeSeries(evap, t)`로 도메인 균일 시변율(infevap.cpp:56). 비채널·wet 셀에서 감소, `EvapTotalLoss` 적산(infevap.cpp:60-80). evap 파일은 mm/day → m/s 환산(input.cpp LoadEvap, `/= 1000*24*3600`).

### `Rainfall` (infevap.cpp:91)
라우팅 OFF일 때만 호출(주석 infevap.cpp:88-89). 도메인 균일 시변율(`InterpolateTimeSeries(rain,t)`), NODATA 표고 셀 제외(`DEM != nodata_elevation`, infevap.cpp:108), `RainTotalLoss` 적산. OpenMP 병렬(infevap.cpp:99). rain 파일은 mm/hr → m/s 환산(input.cpp LoadRain). evap·rain 시계열은 첫 줄 skip(`LoadTimeSeries(..., ON)`).

### `FlowDirDEM` / `Routing` (infevap.cpp:131 / 310)
얕은 강우류 라우팅용 D4 최저이웃 방향맵 생성. 경계·point source·위어·SGC 채널 셀은 자기자신으로 설정해 라우팅 비활성(infevap.cpp:251-296). `RouteInt = d/Routing_Speed` (dist_routing이면 경사의존 속도, infevap.cpp:185-237). `Routing`은 friction slope가 `RouteSfThresh` 초과 또는 수심 `<DepthThresh`일 때 최저이웃으로 수면표고차 기반 유량을 `flow_fraction = Tstep/RouteInt`만큼 이동(infevap.cpp:371-391).

## 6. 출력 래스터 (`output.cpp`)

### ASCII (`write_ascfile`, output.cpp:39)
파일명 = `root[-SaveNumber]extension` (SaveNumber 0–9999는 4자리 zero-pad, output.cpp:64-66). Arc/Info ASCII 헤더(ncols/nrows/xll/yll/cellsize/NODATA)를 `outflag`에 맞춰 작성. `outflag`:
- 0: 셀 중심값 (xsz×ysz)
- 1: Qx 플럭스 (xsz+1, 원점 -dx/2 오프셋, output.cpp:113-115)
- 2: Qy 플럭스 (ysz+1, 원점 -dy/2)
- 3: 수면표고 = DEM+H, `H<=depth_thresh` 셀은 NULLVAL(output.cpp:150-172)

`alt_ascheader` ON 시 사용자 헤더 6줄 사용(output.cpp:79-85). `gzip` ON이면 `system("gzip -9 -f ...")`(output.cpp:179-182).

### Binary (`write_binrasterfile`, output.cpp:506)
동일 outflag 의미를 바이너리로: 헤더는 int xsz/ysz + NUMERIC_TYPE blx/bly/dx/no_data, 이후 raw 배열(output.cpp:551-617). no_data는 항상 -9999(output.cpp:521).

### 출력 오케스트레이션 (`write_regular_output`, output.cpp:756)
States 플래그별 호출. binary_out이면 `b` 접미 확장자:

| State | 확장자(asc/bin) | 내용 | output.cpp |
|---|---|---|---|
| `save_depth` | `.wd`/`.wdb` | 수심 H (+SGC면 `.wdfp` 범람 깊이) | 763-774 |
| `save_elev` | `.elev`/`.elevb` | 수면표고 DEM+H (SGC는 `SGCz` 기준) | 777-791 |
| `save_Qs` | `.Qx/.Qy` (+SGC `.Qcx/.Qcy/.Fwidth`) | flux | 794-835 |
| `voutput` | `.Vx/.Vy` | 속도 | 838-850 |
| `SGCvoutput` | `.SGCVx/.SGCVy/.SGCVc` | SGC 채널속도 (inertial식 재계산) | 852-979 |
| `save_QLs` | `.QLx/.QLy` | Q-limit | 981-993 |

### 최종 통계 (`fileoutput`, output.cpp:394)
SaveNumber=-1(번호 없음)로 최댓값 계열 1회 기록: `.inittm`(최초 침수시각), `.totaltm`(총 침수시간), `.max`(최대수심), `.maxtm`(최대수심 시각), voutput이면 `.maxVx/.maxVy`, hazard면 `.maxVc/.maxVcd/.maxHaz`(output.cpp:399-442). `debugfileoutput`(447)은 debug 모드에서 채널/SGC 마스크 덤프.

## 7. 입력 파일 포맷 요약

| 파일 | 포맷 | 핵심 구조 |
|---|---|---|
| DEM | Arc/Info ASCII grid | 6줄 헤더 + 행우선 값, NODATA→`nodata_elevation` |
| `.bci` | 텍스트 라인 | `{N/S/E/W} start finish {TYPE} [val/name]` 또는 `{P/F} px py {TYPE} ...` |
| `.bdy` | 명명 시계열 블록 | 이름 줄 + `count units` + `value time` 쌍 (단위 자동환산) |
| `.evap` | 시계열 (mm/day) | 첫 줄 skip, m/s 환산 |
| `.rain` | 시계열 (mm/hr) | 첫 줄 skip, m/s 환산 |
| checkpoint(`.chkpnt`) | 바이너리 | 버전 헤더 + 상태/격자/경계 누적/채널 전수 |

## 한계·주의

- 알 수 없는 parfile 키워드는 abort 없이 무시 — 오타 위험(pars.cpp:1019).
- `InterpolateTimeSeries` non-thread-safe(boundary.cpp:1420).
- 침투·증발·(라우팅 OFF)강우는 **도메인 균일율** (분포형은 별도 마스크/파일).
- NetCDF 실제 I/O는 본 6파일이 아니라 `lisflood2/`·`rain/`(`_NETCDF` 가드) — 범위 밖.
