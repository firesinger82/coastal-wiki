---
title: "LISFLOOD-FP User Manual — parfile 키워드·솔버 선택·입력파일(.river/.bci/.bdy/DEM)·출력·CMake 빌드"
model: LISFLOOD-FP
doc: "LISFLOOD-FP User Manual (Code release 6.1.1, 25 Nov 2013, Bates·Trigg·Neal·Dabrowa) + INSTALL.md + README.md"
canonical_source: manual
citation_status: verified
verification_method: "raw/source_code/LISFLOOD-FP/'LISFLOOD-FP user manual.pdf' pdftotext -layout 추출 후 page 직접 확인 (p.10–48). README.md·INSTALL.md 직접 Read. 키워드·기본값은 PDF 표(Table 5–14) verbatim."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "[[../source-analysis/lisflood-fp-classic-acc-flow]]"
  - "[[../source-analysis/lisflood-fp-io-boundary]]"
  - "[[../source-analysis/lisflood-fp-swe-fv1-dg2]]"
  - "[[../source-analysis/lisflood-fp-architecture-source-map]]"
---

# LISFLOOD-FP User Manual 정리

대상: 공식 User Manual PDF (표지 "Code release 6.1.1", 페이지 footer 잔류 "5.9.6", 2013-11-25) + 저장소 `README.md`·`INSTALL.md`. PDF는 classic CPU 솔버 시대 문서이며, full-SWE `fv1`/`dg2` 솔버와 CUDA·CMake 빌드는 PDF에는 없고 README/INSTALL(현대 코드)에 기술된다 — 본 노트 §6 참조.

> 코드 측 대응: parfile 파싱·BC·IO는 [[../source-analysis/lisflood-fp-io-boundary]], classic floodplain flux 솔버(acceleration/diffusive/Roe)는 [[../source-analysis/lisflood-fp-classic-acc-flow]], FV1/DG2 full SWE는 [[../source-analysis/lisflood-fp-swe-fv1-dg2]].

---

## 1. 모델 개요와 솔버 선택 (p.10–12)

raster 기반 침수 모델. 1D 채널(kinematic/diffusive/subgrid) + 2D 범람원(storage-cell) 결합. 표준 SI 단위(길이 m, 시간 s, flux m³s⁻¹) (p.12).

### 1.1 범람원(floodplain) 솔버 — Table 1 (p.10)

| 솔버 | 차원 | 포함 SWE 항 | 무시 항 | time step | 참고 |
|---|---|---|---|---|---|
| Routing | 1D on 2D grid | 사용자 지정 속도·bed slope 방향만 | 전부 | Adaptive | Sampson et al., 2012 |
| Flow-limited | 1D on 2D grid | friction·water slope | local·convective accel | Fixed | Bates & De Roo, 2000 |
| Adaptive | 1D on 2D grid | 위와 동일 | 위와 동일 | Adaptive | Hunter et al., 2005 |
| Acceleration | 1D on 2D grid, friction 2D | friction·water slope, local accel | convective accel | Adaptive | Bates et al., 2010; De Almeida et al., 2012 |
| Roe | 2D | 전체 항 | 없음 | Adaptive | Neal et al., 2012b |

- **Routing**: 매우 얕은 수심(<1 mm 기본 또는 사용자 지정) 또는 큰 water slope(>1 in 10) 셀에만 적용, SWE 대체. 사전 계산 흐름 방향맵으로 최저 인접셀로 고정 속도 흐름 (p.11).
- **Acceleration**(inertial): convective accel만 무시. 1차 공간·explicit, friction은 semi-implicit. time step은 CFL 조건, ∆x에 선형 → adaptive보다 빠름 (p.11).
- **Roe**: Godunov + Roe 근사 Riemann, full SWE shock-capturing. ghost cell 경계. "테스트 케이스 제한적, 덜 robust할 수 있음" 경고 (p.11).

### 1.2 채널(channel) 솔버 — Table 2 (p.10–11)

| 솔버 | 차원 | 포함 | 무시 | 참고 |
|---|---|---|---|---|
| Kinematic | 1D | friction slope + bed gradient(dz/dx)만 | local·convective accel, 자유표면 gradient(dh/dx) | Bates & De Roo, 2000 |
| Diffusive | 1D | friction slope + bed·자유표면 gradient (d[z+h]/dx) | local·convective accel | Trigg et al., 2009 |
| Sub-grid channel | 1D | friction·water slope, local accel | convective accel | Neal et al., 2012a |

1D 채널은 bankfull 도달 시 인접 범람원 셀로 routing — **질량만 전달, 운동량 전달 없음** (p.12). full 1D SWE 운동량/연속식은 식(1)(2) (p.10):

$$\underbrace{\frac{\partial Q_x}{\partial t}}_{\text{local accel}} + \underbrace{\frac{\partial}{\partial x}\!\left(\frac{Q_x^2}{A}\right)}_{\text{convective accel}} + \underbrace{gA\,\frac{\partial(h+z)}{\partial x}}_{\text{water slope}} + \underbrace{\frac{gn^2 Q_x^2}{R^{4/3}A}}_{\text{friction slope}} = 0, \qquad \frac{\partial A}{\partial t} + \frac{\partial Q_x}{\partial x} = 0$$

여기서 $Q_x$=x방향 유량, $A$=흐름 단면적, $h$=수심, $z$=하상고, $n$=Manning's n, $R$=수리반경 (p.11).

### 1.3 주요 한계 (p.12–13)

- kinematic/diffusive: 채널 단면을 직사각형 단순화, wide-and-shallow 가정(wetted perimeter≈width) (p.12).
- 1D↔범람원 운동량 교환 없음, 측방 friction 무시 (p.12).
- flow-limited은 파속 과소·정확도 낮음 → 비교 실험용만. adaptive는 고해상도에 계산비용 과다 (p.12).
- Roe 제외 전 솔버: 매우 낮은 Manning's n / 높은 Froude에서 파속 과소(de Almeida & Bates 2013). acceleration은 낮은 n에서 불안정 → numerical diffusion 항 필요 (p.12–13).
- routing: `depththresh` > 10 mm 설정 시 불안정 가능 (p.13).

---

## 2. parameter file (.par) — 일반 규칙 (p.15)

- **대소문자 구분**(case sensitive), 한 줄 한 항목.
- 인식 안 되는 항목은 에러 없이 무시. 키워드 미기재 시 코드 내장 기본값 사용.
- 순서 무관. 줄 첫 칸에 `#` → 주석 처리.
- 솔버 선택 키워드를 **아무것도** 안 넣으면: 채널=1D kinematic, 범람원=2D adaptive (Table 6 캡션, p.16).

> parfile 파서·디스패치 코드: [[../source-analysis/lisflood-fp-io-boundary]] §1 (`pars.cpp` CheckParam).

### 2.1 기본·상용 키워드 — Table 5 (p.15)

| 키워드 | 설명 | 기본값(Buscot) | 적용 |
|---|---|---|---|
| `DEMfile` filename | DEM 파일명 | 기본 없음 | 전 솔버 |
| `resroot` name | 결과파일 명 root (root.op, root-0001.wd…) | `out` | 전 모델 |
| `dirroot` foldername | 결과 디렉토리(상대/절대), 없으면 생성. 생략 시 실행 디렉토리 | 실행 디렉토리 | 전 모델 |
| `saveint` value | 결과파일 저장 간격(초), 순번 stamp | 1000 | 전 모델 |
| `massint` value | .mass 파일 기록 간격(초) | 100 | 전 모델 |
| `sim_time` value | 총 시뮬레이션 길이(초, real) | 3600 | 전 솔버 |
| `initial_tstep` value | fixed: 시간스텝(초). accel/adaptive: 최적·최대 추정 초기값 | 10 | 전 솔버 |
| `bcifile` filename | 범람원 경계조건 타입 파일 | 기본 없음 | 전 솔버 |
| `bdyfile` filename | 시변 경계조건 파일 | 기본 없음 | 전 솔버 |
| `fpfric` value | 공간 균일 범람원 Manning's n (manningfile와 동시 지정 시 fpfric 무시) | 0.06 | 2D 솔버만 |
| `manningfile` filename | 공간 가변 범람원 n 격자(ARC ascii) | 기본 없음 | 2D 솔버만 |

### 2.2 솔버 on/off 키워드 — Table 6 (p.16)

| 키워드 | 동작 | 적용 |
|---|---|---|
| `diffusive` | 채널을 kinematic 대신 diffusive 솔버로 | 1D Diffusive |
| `adaptoff` | adaptive time-stepping 억제 → fixed time step. **subgrid와 병용 불가**(subgrid는 inertial 사용) | 2D Fixed timestep |
| `acceleration` | 2D inertial(local inertia) 정식. subgrid엔 불필요, non-adaptive와 병용 불가 | 2D inertial |
| `routing` | routing 스킴 활성. depth<`depththresh` 또는 water slope>`routesfthresh`일 때만. **Subgrid 또는 2D inertial과만 병용** | Subgrid·2D inertial |
| `SGCwidth` filename | sub-grid 채널 폭 파일 — 지정 시 subgrid 모델로 전환(범람원은 2D inertial). 다른 SGC 키워드 동반 필수 | Subgrid |
| `Roe` | 2D full shallow water(Roe) 활성. **`adaptoff`와 병용 금지** | 2D shallow water |

> 코드상 acceleration/diffusive/Roe 솔버 식·이산화: [[../source-analysis/lisflood-fp-classic-acc-flow]]. subgrid 채널: [[../source-analysis/lisflood-fp-channel-sgc]].

### 2.3 채널 위치·물성 키워드 — Table 7 (p.17)

| 키워드 | 설명 | 기본값 |
|---|---|---|
| `riverfile` filename | 채널 geometry·BC 파일(채널 없으면 생략) | — (1D diffusive/kinematic) |
| `multiriverfile` filename | 다중 1D river network 인덱스(.rivers) | — |
| `SGCbank` filename | subgrid 채널 bank 높이(DEM 가능, 필수) | 없음 |
| `SGCbed` filename | subgrid 채널 bed 고도(없으면 파라미터로 추정) | 추정값 |
| `SGCchangroup` / `SGCchanprams` filename | subgrid 채널 region / parameter region 파일 | 없음 |
| `SGCn` value | global 채널 Manning's n | 0.035 |
| `SGCr` value | subgrid 채널 깊이 계산 global 파라미터 | 0.3 |
| `SGCp` value | subgrid 채널 깊이 계산 global 파라미터 (depth = r·width^p) | 0.76 |
| `SGCchan` value | subgrid 채널 shape type(정수, 1=직사각형) | 1 |
| `SGCs` value | 일부 shape type용 global 파라미터(2=parabolic) | 2 |

### 2.4 추가 물 입출력 — Table 8 (p.17)

| 키워드 | 설명 | 기본값 | 적용 |
|---|---|---|---|
| `rainfall` filename | 공간 균일 강우 시계열(.rain). 급경사 DEM이면 routing 병용 권장 | off | 전 2D |
| `infiltration` value | 공간 균일 침투율(ms⁻¹) | 0 (Buscot 0.0000001) | 2D except Roe |
| `evaporation` filename | 증발 시계열 파일 | off | 2D except Roe |

### 2.5 시작 조건 — Table 9 (p.18)

| 키워드 | 설명 | 기본값 |
|---|---|---|
| `tstart` value | 시뮬레이션 시작 시각(초) | 0 |
| `checkpoint` value | checkpointing 활성 + 계산시간 간격(시간). 값 없으면 1hr | off (1hr) |
| `loadcheck` filename | 덮어쓰이지 않는 대체 checkpoint 시작 파일 | off |
| `ch_start_h` value | 채널 초기 수심(전 채널) | 2 (m) |
| `startq` | kinematic: 유입 기반 각 단면 수위 계산 / diffusive: 정상상태로 iterate. spin-up 단축 | off |
| `ch_dynamic` | startq의 full dynamic 정상상태(startq와만 병용) | off |
| `startfile` filename | 이전 결과(수심, ARC ascii)로 초기조건 | off (except Roe) |
| `startelev` filename | 수면 고도로 초기화(DEM으로 수심 변환) | off |
| `binarystartfile` filename | startfile의 binary 버전 | off |

### 2.6 덜 쓰이는 설정 — Table 10 (p.18–19, 발췌)

| 키워드 | 설명 | 기본값 | 적용 |
|---|---|---|---|
| `ts_multiple` value | 채널·범람원 timestep 분리, 채널 timestep 증가(x10까지 거의 동일) | 1 | 1D diff/kin |
| `htol` value | bank smoothing 기본 1m override | 1 (m) | 1D diff/kin |
| `chainageoff` | river chainage를 cell 크기 무관 직선거리로(구버전 복귀 키워드) | (Buscot 사용) | 1D diff/kin |
| `depththresh` value | 셀을 wet으로 보는 수심(m). rainfall routing 임계도 제어 | 0.001 | 2D·subgrid |
| `weirfile` filename | weir/bridge 링크 파일(.weir) | 없음 | weir 전부, bridge는 subgrid만 |
| `cfl` value | time step 안정 계수 | 0.7 | 2D inertial·SWE·subgrid |
| `drycheckon` / `drycheckoff` | drycheck on/off (Bates & de Roo 2000) | off | 2D adaptive·fixed·inertial |
| `routingspeed` value | routing 흐름 속도(ms⁻¹) | (routing 시 0.1) | subgrid·2D inertial |
| `routesfthresh` value | routing 발생 water slope 임계 | 0.1 | subgrid·2D inertial |
| `diffusive_froude_thresh` value | Froude 초과 시 diffusive 전환 | off | subgrid |
| `dhlin` value | adaptive 선형화 임계(dx×0.0002, Cunge 1980·Hunter 2005) | 자동 계산 | 2D adaptive |
| `1Dfriction` | inertial 모델에서 1D friction 처리로 전환 | off(2D friction) | 2D inertia |
| `theta` value | inertial 모델에 numerical diffusion 추가(<1일 때) | 1 | 2D inertial |
| `momentumthresh` value | Roe 솔버 momentum 식 임계 | 0.001 | 2D SWE |
| `qlimfact` value | fixed-timestep 2D 솔버 flow limit 배율 | 1 | 2D fixed |
| `gravity` value | 중력값(ms⁻²) | 9.81 | 2D inertia·subgrid |
| `latlong` | 좌표·셀 치수를 decimal degrees로(개발 중). flux는 m³s⁻¹ | off | subgrid |
| `maxdepthonly` | 최대 수심만 출력 | off | 전 모델 |

### 2.7 출력 관련 키워드 — Table 11 (p.20–21, 발췌)

| 키워드 | 설명 | 기본값 |
|---|---|---|
| `overpass` value | 관측 영상 시각(초)에 .op/.opelev 출력 | off |
| `overpassfile` filename | 다중 위성 overpass 시각 파일(.opts) | 없음 |
| `stagefile` filename | stage 지점 수심 시계열(massint마다, *.stage) | 없음 |
| `depthoff` / `elevoff` | *.wd / *.elev 출력 억제(logical) | off |
| `mint_hk` | maxH·maxHtm 등을 매 timestep 대신 massint에 계산(병렬 효율) | off |
| `comp_out` | model/computation time ratio를 stdout 출력 | off |
| `profiles` | 채널 수면 profile(*.profile) saveint마다 출력 | off |
| `qoutput` / `voutput` | flux(*.Qx,*.Qy) / velocity(*.Vx,*.Vy) ascii 격자 출력 | off |
| `SGCvoutput` | subgrid 채널 속도(*.SGCVx 등) | off |
| `gaugefile` filename | virtual gauge 단면 discharge(*.discharge) | off |
| `binary_out` | 격자 출력을 binary로, 파일명에 "b" 접미(*.wd→*.wdb) | off |
| `netcdf_out` | 격자 출력을 netcdf로 | off |
| `hazard` | 속도·최대속도·hazard 격자(*.maxHaz 등) | off |
| `qloutput` | flow limiter 격자(*.QLx,*.QLy) | off |
| `debug` | DEM/채널마스크 등 디버그 격자(*.dem,*.chmask,*.segmask; subgrid 시 *_SGC_*) | off |

Buscot 예제 .par (p.21): `diffusive`+`adaptoff`로 정상상태·fixed-timestep, `fpfric 0.06`, weir 포함, `elevoff`(수심만 출력).

---

## 3. 입력 파일 형식 (p.15–32)

파일 확장자는 강제 아님, 주석은 .par에서만 가능, 전부 case sensitive (p.15).

### 3.1 채널 파일 (.river) (p.22–24)

채널 중심선 벡터를 raster에 보간. 한 DEM 셀에 벡터점 ≤1, 도메인 경계 밖 점 ≤1 (p.22). 각 점에 width·n·bed elevation. 형식:

```
Line 1: Tribs <채널 세그먼트 수>   (생략 시 단일 reach)
Line 2: <벡터 데이터 점 수 i>
Line 3: X1 Y1 Width1 n1 BedElev1 BC Value   (첫 점에 유입 BC 필수)
Line k: Xk Yk [Widthk nk BedElevk] [Lateral inflow]   (중간점 width/n/bed는 선택)
```

- 유입 BC: `QFIX <값>`(정상 유입 m³s⁻¹) 또는 `QVAR <식별자>`(시변, .bdy 참조) (p.23).
- lateral inflow: reach 임의 점에 source 항으로 소규모 지류 (p.23).
- kinematic은 하류 bed slope가 음(내리막)이어야 — 오르막이면 경고 후 내리막 취급. diffusive는 오르막 허용 (p.23).
- **Tributary**: main stem이 segment 0. 합류점에서 `Trib <세그먼트번호>`, 각 지류 마지막 점에 `QOUT <합류 세그먼트>` (p.23–24).
- **Diffusive 채널 하류 BC**(kinematic과 달리 필수): `FREE [slope]`(normal depth, slope 생략 시 마지막 두 단면 기울기 사용/지정이 더 안정), `HFIX <고도 m>`(정상 수위), `HVAR <식별자>`(시변) (p.24).

### 3.2 다중 비연결 채널 (.rivers) (p.25)

`multiriverfile` 키워드로 읽힘. 1행=.river 개수, 이후 각 .river 파일명. 같은 main stem 지류망엔 불필요(.river 하나로 처리), 서로 다른 main stem river가 한 도메인에 있을 때만 필요.

### 3.3 경계조건 타입 파일 (.bci) (p.25)

채널과 무관한 경계조건. 5열: 식별자(N/E/S/W/F/P), 시작좌표, 끝좌표, BC 타입, 값.

| BC 타입 | 설명 | 5열 값 (Table 12, p.25) |
|---|---|---|
| `CLOSED` | zero-flux (기본) | 없음 |
| `FREE` | uniform flow | free surface/valley slope (선택) |
| `HFIX` | 고정 수면 고도 | 고도(m) |
| `HVAR` | 시변 수면 고도 | .bdy 식별자 |
| `QFIX` | 고정 유입 | 단위폭당 mass flux(m²s⁻¹); 경계 segment는 길이, point source는 셀폭 곱해 m³s⁻¹. latlong 시 m³s⁻¹ |
| `QVAR` | 시변 유입 | .bdy 식별자 |

> BC enum·코드 처리: [[../source-analysis/lisflood-fp-io-boundary]] §(boundary.cpp), lisflood.h:177–190.

### 3.4 시변 경계조건 파일 (.bdy) (p.26)

QVAR/HVAR용. 형식: 1행 주석, 2행 식별자, 3행 `<시점 수> <단위 days/hours/seconds>`, 이후 `Value Time` 쌍. HVAR는 수면고도(m). QVAR는 **.river 지정이면 m³s⁻¹, .bci 지정이면 m²s⁻¹**(코드가 segment 길이/셀 크기 곱함). 코드는 시점 사이 선형 보간. 미매칭 식별자는 zero-flux로 (p.26).

### 3.5 DEM 파일 (.dem.ascii) (p.27)

ARC ascii raster. 6행 헤더 + i행×j열 고도값:

```
ncols 76 / nrows 48 / xllcorner 22950 / yllcorner -2400 / cellsize 50.0 / NODATA_value -9999
```

latlong 지정 시 xllcorner·yllcorner·cellsize는 decimal degrees (p.27).

### 3.6 기타 입력 파일 (p.27–32)

| 파일 | 키워드 | 내용 |
|---|---|---|
| `.n.ascii` | `manningfile` | 공간 가변 범람원 Manning's n 격자(ARC ascii) (p.27) |
| `.width.asc` | `SGCwidth` | subgrid 채널 폭, 채널 없는 셀은 0/NoData (p.28) |
| `.bed.asc` | `SGCbed` | subgrid 채널 bed 고도(선택), NoData 시 파라미터로 추정 (p.28) |
| `.bank.asc` | `SGCbank` | bank 고도(bed 계산용, 범람 overtop은 DEM으로 결정) (p.28) |
| `.region.asc` | `SGCchangroup` | subgrid 채널 region(정수, 0부터) (p.28) |
| `.pram` | `SGCchanprams` | region별 채널 파라미터: Region Type p r s nch m. depth=r·width^p, Type 1=직사각형·2=power. m=meander(기본1) (p.28–29) |
| `.weir` | `weirfile` | weir/bridge 셀 링크 (§3.7) |
| `.opts` | `overpassfile` | 다중 위성 overpass 시각(초) (p.30) |
| `.stage` | `stagefile` | 수심 시계열 출력 x,y 지점 (p.30) |
| `.gauge` | `gaugefile` | discharge 측정 단면 X Y Direction Width (p.31) |
| `.evap` | `evaporation` | 증발율 시계열(mm day⁻¹, 선형보간) (p.31) |
| `.rain` | `rainfall` | 강우율 시계열(mm hr⁻¹, 선형보간) (p.32) |
| `.head` | `ascheader` | ascii 출력용 대체 6행 헤더 (p.31) |
| `.start`/`.startb` | `startfile`/`binarystartfile` | 초기 수심(ascii/binary double) (p.32) |
| (수면고도 start) | `startelev` | 초기 수면고도(ARC ascii) (p.32) |
| `.chkpnt` | `checkpoint` | 재시작 상태(binary) (§5) |

### 3.7 Weir·Bridge 파일 (.weir) (p.29–30)

direction 형식으로 weir/bridge 구분. **Weir**: `X Y Direction C CrestHeight ModularLimit [Width]`. Direction=N/E/S/W(단방향은 NF/EF/SF/WF), C=weir 계수(0.5–1.7, broad-crested 기본 1.4), modular limit 보통 0.9, width 생략 시 grid 크기 (p.29). **Bridge**(subgrid만): `X Y Direction Cd SoffitElev TransitionZone Width`, direction에 b 접미(nb,sb,…), Cd=완전수몰 압력류 토수계수(보통 0.8), transition zone 보통 1.5 (p.30).

---

## 4. 시뮬레이션 설정 절차 (p.33)

DEM(.dem.ascii) → (선택)공간가변 friction(.n.ascii) → 채널 중심선 벡터 → .river(채널·BC) → .bci/.bdy → (선택).weir → .par(run 파라미터·파일명) → (선택)초기조건 생성(이전 결과를 startfile로) (p.33).

---

## 5. 실행·command line·출력 (p.33–39)

### 5.1 실행 (p.33)

명령행에서 실행(더블클릭 아님). Windows `lisflood_win [옵션] model.par`, Linux `./lisflood_win [옵션] model.par`. parameter 파일은 항상 마지막 인자 (p.33–34).

### 5.2 Command line 옵션 — Table 14 (p.33–34)

| 옵션 | 설명 |
|---|---|
| `-v` | verbose(런타임 진단 메시지) |
| `-version` | parfile 생략 시 버전 확인 |
| `-gzip` | 출력 saveint마다 gzip 압축(Linux only) |
| `-dir` dirname | 결과 디렉토리(parfile dirroot override) |
| `-resroot` | 결과파일 root |
| `-simtime` value | sim_time override(초) |
| `-nch` value | 공간균일 채널 Manning's n(.river override) |
| `-nfp` value | 공간균일 범람원 n(fpfric/.n.ascii override) |
| `-inf` value | 공간균일 침투(ms⁻¹, infiltration override) |
| `-weir` filename | weirfile override |
| `-checkpoint` | checkpointing on(기본 1hr) |
| `-loadcheck` filename | 대체 checkpoint로 시작(checkpointing도 on) |
| `-log` | 화면 출력을 결과 디렉토리 로그파일로 |
| `-debug` | *.dem·*.chmask·*.segmask 출력 |
| `-dynsw` | 1D diffusive의 full dynamic wave 정상상태 초기해 |
| `-dhlin` value | adaptive 선형화 임계 override |
| `-kill` value | 계산시간(시간) 경과 후 강제 종료(클러스터용) |
| `-acceleration` | 2D acceleration 솔버 사용 |
| `-cfl` | acceleration/Roe/subgrid CFL override(기본 0.7) |
| `-theta` | acceleration theta override(기본 1) |
| `-steady` | 정상상태 도달 시 자동 종료(Qout≈Qin within 0.0005 m³s⁻¹) |
| `-steadytol` | 사용자 지정 정상상태 허용오차 |

옵션 순서 무관, parfile은 마지막 (p.34). 병렬: 기본적으로 호스트의 모든 공유메모리 코어 사용(OpenMP, Neal et al. 2009), `OMP_NUM_THREADS` 환경변수로 코어 수 지정 (p.34).

### 5.3 Checkpointing (p.34–35)

계산시간 간격마다 모델 상태를 binary로 기록·덮어쓰기. crash 시 마지막 checkpoint부터 재시작. 시작 시 `"resroot".chkpnt`를 자동 탐색·읽기. binary endian/버전 불일치 시 crash·exit(경고). 재시작 후 .mass는 append(checkpoint break line 삽입) (p.34–35).

### 5.4 출력 파일 (p.36–39)

| 파일 | 내용 | 활성 |
|---|---|---|
| `.mass` | 질량수지(12열: Time, Tstep, MinTstep, NumTsteps, Area, Vol, Qin, Hds, Qout, Qerror, Verror, Rain-Inf+Evap), massint마다 | 항상(억제 키워드 없음) (p.36) |
| `.op`/`.opelev` | overpass 시각 수심/수면고도 격자 | overpass/overpassfile (p.36) |
| `.profile` | 채널 수면 profile(11열) saveint마다 | profiles (p.37) |
| `-xxxx.wd`/`.elev`/`.wdfp` | saveint별 수심/수면고도 격자(.wdfp는 subgrid 범람원 수심) | 기본 on, depthoff/elevoff로 억제 (p.37) |
| `.mxe`/`.max` | 최대 수면고도/수심 | 항상 (p.37) |
| `.inittm`/`.maxtm`/`.totaltm` | 초기침수/최대수심/총침수 시각(시간) | 항상 (p.37–38) |
| `.Qx/.Qy/.Qcx/.Qcy/.Vx/.Vy/.SGCVx/.SGCVy` | cell-interface 유량·속도 격자 | qoutput·voutput (p.38) |
| `.maxVx/.maxVy/.maxVc/.maxVcd/.maxHaz` | 최대속도·hazard. Haz=H·(Vc+1.5) (DEFRA 2003) | hazard (p.38) |
| `.QLx/.QLy` | flow limiter 값 | qloutput (p.38) |
| `.stage` | stage 지점 수심 시계열(massint) | stagefile (p.39) |
| `.discharge` | gauge 단면 discharge(massint), 범람원만(subgrid 시 채널+범람원) | gaugefile (p.39) |

cell velocity (식 3, p.38): $V_{c\,i,j} = \big([\max(V_{i-1/2,j}, V_{i+1/2,j})]^2 + [\max(V_{i,j-1/2}, V_{i,j+1/2})]^2\big)^{1/2}$

> 출력 IO 코드: [[../source-analysis/lisflood-fp-io-boundary]] §(output.cpp).

### 5.5 Weir·Bridge 계산식 (Appendix, p.40–48)

- Weir (식 5, p.40): $Q = CL(2gH)^{1.5}$ — C=weir 계수(기본 1.4), L=weir 폭, H=상류 energy head. 현재 코드는 energy head 대신 수심 사용(접근속도 무시), 낮은 Fr 근사 (p.40).
- Bridge (식 6, p.40, pressure/orifice flow): $Q = C_d A(2gH)^{0.5}$ — Cd=완전수몰 토수계수(기본 0.8), A=교량 개구 단면적, H=상하류 energy/수위차. HEC-RAS 기본법과 동일, 검증됨. subgrid 채널 버전만 (p.40).

---

## 6. 빌드·의존성 (README.md · INSTALL.md)

> PDF(6.1.1)는 pre-compiled exe 배포(LISFLOOD-WIN.EXE 등, p.13) 시대. 현대 저장소는 **CMake ≥ 3.13** 소스 빌드이며 full-SWE FV1/DG2·CUDA 솔버를 포함 — 이는 PDF에 **없는** 내용이다 (README.md:1–2).

### 6.1 Windows (README.md:4–14)
- **MSVC**: Visual Studio 2019에서 `lisflood-fp` 폴더 열고 `msvc-x64-Debug`/`msvc-x64-Release` 구성 → Rebuild All.
- **Intel**: `launch_vs2019_intel64.bat` 실행(VS2019 Community 가정, Intel 컴파일러 환경변수 설정) 후 `intel-x64-Debug`/`intel-x64-Release` 구성. 한 번 .bat로 실행하면 VS에서 MSVC/Intel 둘 다 선택 가능.
- 실행/디버그: Solution Explorer를 CMake Targets View로 전환, Debug Configuration을 `lisflood (executable)`로.

### 6.2 Linux (README.md:16–39)
- CMake 최신 + `libnuma-dev` 필수. **NetCDF 출력·dynamic rainfall** 지원엔 `libnetcdf-dev` 추가. Ubuntu:
  ```bash
  sudo snap install cmake --classic
  sudo apt install libnuma-dev libnetcdf-dev
  ```
- 빌드:
  ```bash
  cmake -S . -B build
  cmake --build build
  ```
  `lisflood` 실행파일은 `build/`에 생성. libnuma 비표준 경로면 `-DNUMA_ROOT=<path>`.

### 6.3 빌드 커스터마이즈·CUDA (README.md:41–65)
- 기본 구성은 `config.default.cmake`. 복사·수정 후 Windows는 `CMakeSettings.json`의 `cmakeCommandArgs`에 `-D_CONFIG=<filename>`, Linux는 `cmake -S . -B build -D_CONFIG=<filename>`.
- **NVIDIA CUDA**: CUDA Toolkit 설치 시 CMake가 FV1·DG2 CUDA 솔버를 자동 컴파일. compute capability는 `config.default.cmake`에서 조정.
- (구) Makefile: `INSTALL.md` — `CONFIG=config/<file> make -f Makefile.new <target>`.

> FV1/DG2 full-SWE 솔버 자체: [[../source-analysis/lisflood-fp-swe-fv1-dg2]]. CUDA GPU 경로: [[../source-analysis/lisflood-fp-cuda-gpu]].

---

## 7. 코드↔문서 cross-link 요약

| 매뉴얼 항목 | 소스 분석 노트 |
|---|---|
| .par 키워드 파싱·기본값 | [[../source-analysis/lisflood-fp-io-boundary]] (pars.cpp CheckParam) |
| .bci/.bdy/DEM 입력·BC | [[../source-analysis/lisflood-fp-io-boundary]] (input.cpp·boundary.cpp) |
| 출력 격자(.wd/.mass/binary/netcdf) | [[../source-analysis/lisflood-fp-io-boundary]] (output.cpp) |
| acceleration/diffusive/Roe 솔버 식 | [[../source-analysis/lisflood-fp-classic-acc-flow]] |
| subgrid 채널(SGC*) | [[../source-analysis/lisflood-fp-channel-sgc]] |
| FV1/DG2 (PDF 외, 현대 빌드) | [[../source-analysis/lisflood-fp-swe-fv1-dg2]] |
| CUDA 빌드(README §6.3) | [[../source-analysis/lisflood-fp-cuda-gpu]] |
| 전체 구조 | [[../source-analysis/lisflood-fp-architecture-source-map]] |
