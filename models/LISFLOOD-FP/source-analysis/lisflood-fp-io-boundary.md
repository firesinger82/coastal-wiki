---
title: "LISFLOOD-FP IO·외력 — parfile/DEM/bci/bdy 입력, 수심/flux 출력, 경계조건, checkpoint, 침투·증발·강우"
model: LISFLOOD-FP
component: io-boundary (input.cpp · output.cpp · boundary.cpp · pars.cpp · chkpnt.cpp · infevap.cpp)
canonical_source: self
citation_status: verified
last_source_check: "2026-10-21 (recovery 대조 반영)"
verification_method: "전 6파일 직접 Read. 핵심 단언은 file:line 직접 확인 — pars.cpp:136-1019(CheckParam 키워드 디스패치)·1090-1145(parfile 파서), input.cpp:1330-1521(DEM)·1526-1837(bci)·1848-2122(bdy/TimeSeries), output.cpp:39-186(ascii)·497-625(binary)·756-998(write_regular_output), boundary.cpp:16-559(BCs)·1327-1410(BoundaryFlux)·1422-1474(InterpolateTimeSeries), chkpnt.cpp:34-314, infevap.cpp:14-126. BC enum lisflood.h:177-190. 2026-10-21 LISFLOOD-FP recovery 대조 보고서 반영."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "lisflood-fp-architecture-source-map.md"
source_scope: LISFLOOD-FP/*
---

# LISFLOOD-FP IO·외력 (input/output/boundary/pars/chkpnt/infevap)

전체 솔버 구조와 main 흐름은 [lisflood-fp-architecture-source-map.md](lisflood-fp-architecture-source-map.md)에 있다.
본 노트는 외부 파일과 모델 간 인터페이스를 다룬다.
분석 기준은 8.3(8.2 + 공식 패치)이다. (`VersionHistory.h:31–34`; [build-83 보고서](../../../_staging/recovery/compare/lisflood-build-83-vs-code.md#1-요약)) [10-21 대조 정정]

## 1. 파라미터 파일 파싱 (`pars.cpp`)

### 진입·디스패치 구조
구성 읽기는 `.par` 파일을 먼저 처리한다. (`pars.cpp:45–48`) [10-21 대조 정정]
명령행 재설정은 그 뒤 같은 `CheckParam`을 거친다. (`pars.cpp:1027–1036`) [10-21 대조 정정]
`CheckParams`는 마지막에 실행한다. (`pars.cpp:45–51`) [10-21 대조 정정]
일반 실행은 마지막 인수에 parfile을 요구한다. (`pars.cpp:38–43`) [10-21 대조 정정]
`if (argc == 1 || argv[argc - 1][0] == '-')`이면 종료한다. (`pars.cpp:38–43`) [10-21 대조 정정]
`-version`은 그 전에 반환한다. (`lisflood.cpp:288–320`; [LN1-193 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LN1.md)) [10-21 대조 정정]
`-compare_results`도 설정 파일을 읽기 전에 종료한다. (`lisflood.cpp:288–320`) [10-21 대조 정정]
`-v`는 `ReadVerboseMode`가 먼저 스캔한다. (`pars.cpp:17–24`) [10-21 대조 정정]

`ReadParamFile`은 `LINE_BUFFER_LEN` 크기의 버퍼로 행 단위로 읽는다. (`pars.cpp:1093,1110`) [10-21 대조 정정] [10-21 전수 검증 정정]
첫 토큰은 `sscanf(line_buffer, "%79s ", param_name);`으로 읽는다. (`pars.cpp:1123–1124`) [10-21 전수 검증 정정]
키워드 입력 버퍼는 80글자이다. (`pars.cpp:1093–1095`) [10-21 대조 정정]
`if (param_name_len == 79)`이면 종료한다. (`pars.cpp:1130–1135`) [10-21 대조 정정]
허용 키워드 길이는 78글자이다. (`pars.cpp:1130–1135`) [10-21 대조 정정]
`#`·빈 줄·CRLF-only 줄은 건너뛴다. (`pars.cpp:1119–1121`) [10-21 대조 정정] [10-21 전수 검증 보완]
값 포인터는 `param_value_ptr = line_buffer + param_name_len;`으로 설정한다. (`pars.cpp:1136`) [10-21 전수 검증 정정]
파서는 `CheckParam`으로 디스패치한다. (`pars.cpp:1138`) [10-21 대조 정정]

### 키워드 디스패치 (`CheckParam`, pars.cpp:136-1020)
하나의 거대한 if-체인. 4종 헬퍼로 매칭(대소문자 무시 `STRCMPi`):

| 헬퍼 | pars.cpp | 형식 |
|---|---|---|
| `read_string_param` | 54 | `%255s`로 읽은 문자열 길이가 255이면 거부한다. 허용 길이는 254글자이다. 인자 변환 실패 검사는 주석이다. (`pars.cpp:58–67`) [10-21 대조 정정] |
| `read_numeric_param` | 75 / 93 | `NUM_FMT`(float/double); 93은 실패 시 default 사용 |
| `read_integer_param` | 108 | `%i` |
| `read_empty_param` | 124 | 값 없는 플래그 키워드 |

알 수 없는 키워드는 무시한다. (`pars.cpp:1020`) [10-21 대조 정정]
`if (verbose == ON)`일 때 `Unknown parameter ignored: %s.` 진단을 출력한다. (`pars.cpp:1020`) [10-21 대조 정정]
필수 숫자값을 읽지 못하면 종료한다. (`pars.cpp:79–84,112–117`) [10-21 대조 정정]
기본값을 받는 숫자 파서는 읽기 실패 때 지정된 기본값을 대입한다. (`pars.cpp:93–105`) [10-21 대조 정정]

### 주요 입력 파일 키워드 → 파일명 필드
| parfile 키워드 | 필드 / 효과 | pars.cpp |
|---|---|---|
| `DEMfile` | `demfilename` | 143 |
| `startfile` / `binarystartfile` | 초기 수심 재시작 (ascii/binary 상호배타) | 145-157 |
| `startelev` | 재시작값을 수면표고로 해석 | 158 |
| `resroot` / `dirroot`(=`dir`) | 출력 prefix / 폴더 | 164-175 |
| `Qfile`,`manningfile`,`riverfile` | `qfilename` 저장 / 조도 / 하천망 | 232-247 [10-21 대조 정정] |
| `bcifile` / `bdyfile` | 경계 식별 / 시변 경계 시계열 | 248-251 |
| `weirfile`(=`weir`) | 위어 | 252 |
| `infiltration`(=`inf`) / `infilfile` | 균일/분포 침투 → `calc_infiltration` ON | 486-497 |
| `evaporation` / `rainfall` / `rainfallmask` | 증발/강우/강우 마스크 | 499-517 |
| `SGCwidth`,`SGCbed`,`SGCchanprams`… | sub-grid channel 입력군 | 814-852 |
| `checkpoint [hrs]` / `loadcheck` | 재시작 빈도 / 대체 체크파일 | 563-574 |
| `damfile`,`dammask` | 댐 (SGC 전용) | 907-922 |

`Qfile`은 `qfilename`만 저장한다. (`pars.cpp:232–233`; `lisflood.h:388`) [10-21 대조 정정]
현재 소스에서 `qfilename`의 활성 파일 읽기·계산 소비는 없다. ([LI1-360 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI1.md)) [10-21 대조 정정]

### 솔버 선택 키워드와 분기 우선순위 [10-21 대조 정정]
`acceleration`(`pars.cpp:307`), `Roe`·`Roe_slow`(`pars.cpp:410–429`), `fv1`·`fv2`(`pars.cpp:582–599`), `dg2`(`pars.cpp:630`), `acc_nugrid`(`pars.cpp:600`), `mwdg2`(`pars.cpp:610`), `hwfv1`(`pars.cpp:620`)를 읽는다. [10-21 대조 정정]
해법 플래그 설정은 전체 상호배타성을 보장하지 않는다. (`pars.cpp:300–323,582–639`) [10-21 대조 정정]
`adaptoff`·`acceleration`·Roe 키워드는 앞선 분기의 `return;`으로 끝난다. (`pars.cpp:300–315,410–429`) [10-21 대조 정정]
뒤의 충돌 검사 종료 분기는 현재 실행 경로에서 호출되지 않는다. (`pars.cpp:318–322,430–435`) [10-21 대조 정정]
CUDA 분기는 FV1, FV2, DG2, ACC, acc_nugrid, adaptive 순서로 검사한다. (`lisflood.cpp:419–457`) [10-21 대조 정정]
main 후반부는 SGC, FV1, DG2, 나머지 `IterateQ` 순서로 분기한다. (`lisflood.cpp:773–805`) [10-21 대조 정정]
FV1 선택은 `Solverptr->cfl = C(0.5);`를 대입한다. (`pars.cpp:585`) [10-21 대조 정정]
`cfl`은 해법 선택 뒤에 지정한다. (`pars.cpp:582–647`; [RF-004 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-RF.md)) [10-21 대조 정정]
`limitslopes`는 `if (Statesptr->dg2 == OFF && Statesptr->mwdg2 == OFF && Statesptr->fv2 == OFF)`이면 오류 종료한다. (`pars.cpp:973–982`) [10-21 대조 정정]
`limitslopes`를 읽을 때는 적용할 해법 플래그가 이미 켜져 있어야 한다. (`pars.cpp:973–982`) [10-21 대조 정정]

### 출력 형식 키워드
출력 키워드는 `ascii_out`·`binary_out`·`netcdf_out`(`pars.cpp:384–402`), `depthoff`·`elevoff`·`vtkoff`(`pars.cpp:283–298`), `qoutput`(`pars.cpp:329`), `voutput`·`hazard`(`pars.cpp:338–363`), `maxdepthonly`(`pars.cpp:333`), `gzip`(`pars.cpp:895`)이다. [10-21 대조 정정]
NetCDF 출력 경로는 `lisflood2/lis2_output.cpp`에 있다. (`lisflood2/lis2_output.cpp:154–159`; [par 보고서 LI1-136 원문](../../../_staging/recovery/compare/lisflood-par-vs-code.md#28-표-11의-출력과-출력-제어)) [10-21 대조 정정]
강우 입력 키워드는 `dynamicrainfile`이다. (`pars.cpp:996–1004`) [10-21 대조 정정]
`dynamicrainfall`은 내부 상태 필드이다. (`pars.cpp:998`) [10-21 대조 정정]
`dynamicrainfile`은 `#if (_NETCDF != 1)`에서 종료한다. (`pars.cpp:999–1002`) [10-21 대조 정정]
NetCDF의 `rainfall_depth`를 읽는 구현은 `rain/rain.tpp`에 있다. (`rain/rain.tpp:20,65–74`) [10-21 대조 정정]

### 후처리 검증 (`CheckParams`, pars.cpp:1040)
출력 형식이 모두 OFF이면 ASCII 출력을 켠다. (`pars.cpp:1043–1049`) [10-21 대조 정정]
`routing`은 `if (Statesptr->routing == ON && Statesptr->acceleration == OFF && Statesptr->SGC == OFF && verbose == ON)`에서 OFF로 바뀐다. (`pars.cpp:1053–1057`) [10-21 대조 정정]
`latlong` 검사는 `if (Statesptr->latlong == ON && Statesptr->SGC == OFF && verbose == ON)`에서 `exit(1);`을 실행한다. (`pars.cpp:1058–1062`) [10-21 대조 정정]
`DamMode`의 SGC 검사는 `if (Statesptr->DamMode == ON && verbose == ON && Statesptr->SGC == OFF)`에서 `exit(1);`을 실행한다. (`pars.cpp:1063–1067`) [10-21 대조 정정]
`DamMode`의 마스크 검사는 `if (Statesptr->DamMode == ON && verbose == ON && Statesptr->DammaskRead == OFF)`에서 `exit(1);`을 실행한다. (`pars.cpp:1068–1072`) [10-21 대조 정정]
반대 조합 검사는 `if (Statesptr->DammaskRead == ON && Statesptr->DamMode == OFF && verbose == ON)`에서 `exit(1);`을 실행한다. (`pars.cpp:1074–1078`) [10-21 대조 정정]
이 검사들의 결함 후보 강도는 강함이다. ([LI1-359 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI1.md)) [10-21 대조 정정]
GPU 미지원 검사는 verbose와 무관하다. (`pars.cpp:1080–1086`) [10-21 대조 정정]
v8.2의 `#ifndef CUDA` 검사는 8.3에서 `#if !defined(CUDA) && !defined(METAL_ENABLED)`로 바뀌었다. (`v8.2:pars.cpp:1079–1085`; `pars.cpp:1080–1086`) [10-21 대조 정정]
현재 GPU 미지원 검사는 CUDA와 Metal의 동시 부재를 검사한다. (`pars.cpp:1080–1086`) [10-21 대조 정정]
`cuda`·`metal` 키워드는 같은 GPU 요청을 켠다. (`pars.cpp:965–970`) [10-21 대조 정정]
`fv1` 분기는 GPU 요청과 Metal 가용성을 함께 검사한다. (`lisflood.cpp:778–788`; [LB1-380 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LB1b.md)) [10-21 대조 정정]

## 2. DEM·도메인 기하 (`input.cpp`)

### `LoadDomainGeometry` (input.cpp:1470) — Arc/Info ASCII grid 헤더
6줄 헤더를 `fscanf`로 키-값 쌍 파싱(키워드 문자열 `dum`은 버림): `xsz`, `ysz`, `blx`, `bly`, `dx`(cellsize), `NODATA_value`(input.cpp:1482-1491). 정사각 셀 가정 `dy=dx`, `dA=dx*dy`(1489). 좌상단 `tly = bly + ysz*dy`(1490). `dx_sqrt` 미리 계산(1488).

### `LoadDEM` (input.cpp:1330) — 메모리 할당 + 데이터
격자 배열을 할당한다(`H`·`maxH`는 xsz×ysz, `Qx/Qy`는 (xsz+1)×(ysz+1); `input.cpp:1339,1369-1372`). 솔버별 추가 배열: Roe면 HU/HV/플럭스군(1341-1359), fv1·dg2 전용 할당(1360-1367). `ChanMask`/`SegMask` 초기값 -1(input.cpp:1459-1460). 실제 데이터는 `LoadDEMData`(1502)가 행우선 `fscanf`, **NODATA 셀은 `Parptr->nodata_elevation`로 치환**(input.cpp:1515-1518).

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

`LoadBCVar`는 시계열 이름을 `BC_Name`·`Q_Name`·`PS_Name`과 매칭하여 포인터를 연결한다. (`input.cpp:2020–2059`) [10-21 대조 정정]
참조되지 않은 bdy 자료의 경고에는 verbose 조건이 없다. (`input.cpp:2065–2069`) [10-21 대조 정정]
참조되지 않은 시계열 자료는 `FreeTimeSeries(*timeSeries);`로 해제한다. (`input.cpp:2065–2069`) [10-21 전수 검증 정정]
해당 자료는 `BCptr->allTimeSeries.pop_back();`으로 목록에서 제외한다. (`input.cpp:2071`) [10-21 전수 검증 정정]
누락 참조의 비활성화 검사는 `bdyfilename`이 빈 경우의 `else`에 있다. (`input.cpp:1978–1980,2080–2116`) [10-21 대조 정정]
파일이 있는데 참조한 시계열 이름이 빠진 경우에는 이 검사를 거치지 않는다. (`input.cpp:1978–1980,2080–2116`) [10-21 대조 정정]
활성 HVAR 경로는 NULL 시계열을 `InterpolateTimeSeries`에 전달할 수 있다. (`boundary.cpp:279–283`) [10-21 대조 정정]
보간 함수는 `if (t == timeSeries->prev_time)`에서 이를 역참조한다. (`boundary.cpp:1422–1425`) [10-21 대조 정정]
이 결함 후보의 강도는 강함이다. ([LV1-143 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LV1.md)) [10-21 대조 정정]
첫 시각 전은 첫 값이다. (`boundary.cpp:1432–1444`) [10-21 대조 정정]
마지막 시각 이후는 마지막 값이다. (`boundary.cpp:1432–1444`) [10-21 대조 정정]
`if (timeSeries.time[i] <= prev_time)`이면 종료한다. (`input.cpp:1905–1909`) [10-21 대조 정정]
선언한 개수보다 자료가 적어도 종료한다. (`input.cpp:1914–1918`) [10-21 대조 정정]

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

Checkpoint는 바이너리 형식이다. (`chkpnt.cpp:222`) [10-21 대조 정정]
헤더는 `LF_CheckVersion`과 LISFLOOD 숫자 판을 기록한다. (`chkpnt.cpp:229–230`) [10-21 대조 정정]
빈 체크포인트 파일은 상태 읽기를 건너뛰고 새 계산으로 간다. (`chkpnt.cpp:94–100`) [10-21 전수 검증 정정]
체크포인트 형식 판이 다르면 그 파일의 상태 읽기를 건너뛰고 새 계산으로 간다. (`chkpnt.cpp:98–109`) [10-21 대조 정정]
형식 판이 같고 모델 숫자 판만 다르면 읽기를 계속한다. (`chkpnt.cpp:98–109`) [10-21 대조 정정]
이때 판 불일치 경고의 출력 조건은 `if(verbose == ON)`이다. (`chkpnt.cpp:98–109`) [10-21 대조 정정]
격자 치수 `xsz`·`ysz`가 다르면 종료한다. (`chkpnt.cpp:125–133`) [10-21 대조 정정]

공통 writer는 시간·반복·시간 간격·경계 유량·격자 기하를 기록한다. (`chkpnt.cpp:232–281`; `boundary.cpp:1330,1401–1406`) [10-21 대조 정정] [10-21 전수 검증 정정]
하도 세그먼트 상태는 `if(Statesptr->ChannelPresent==ON)`일 때 기록한다. (`chkpnt.cpp:288–308`) [10-21 전수 검증 정정]
공통 writer는 `H`·`Qx`·`Qy`·`maxH`·`maxHtm`·`initHtm`을 쓴다. (`chkpnt.cpp:248–254`) [10-21 대조 정정]
`totalHtm` 저장 조건은 `if(checkv>1)`이다. (`chkpnt.cpp:254`) [10-21 대조 정정]
누적 침투·증발 저장 조건은 `if(checkv>2)`이다. (`chkpnt.cpp:283–286`) [10-21 대조 정정]
현재 `LF_CheckVersion` 0에서는 총 침수 시간과 누적 침투·증발 손실을 저장하지 않는다. (`VersionHistory.h:19`; `chkpnt.cpp:254,283–286`) [10-21 대조 정정]
공통 writer는 `Qxold`·`Qyold`·SWE 운동량·DG2 계수를 쓰지 않는다. (`chkpnt.cpp:211–314`; [RF-021 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-RF.md)) [10-21 대조 정정]

`ReadCheckpoint`는 기본 파일 `checkpointfilename`을 먼저 연다. 기본 파일을 열지 못하고 `Statesptr->checkfile == ON`이면 `loadCheckpointFilename`을 시도한다. 기본 파일을 열면 대체 파일보다 우선한다. (`chkpnt.cpp:48–78`) [10-21 전수 검증 정정]
현재 기본 체크포인트 경로는 `resrootname`에 `.chkpnt`를 붙여 만든다. `dirroot`를 지정한 경우 `resrootname`에 그 디렉터리를 포함한다. (`lisflood.cpp:323–338,379–380`) [10-21 대조 정정] [10-21 전수 검증 정정]
현재 명령 줄 `-checkpoint`는 숫자 간격을 받는다. (`pars.cpp:45–48,97–100,563,1036`) [10-21 대조 정정]
값이 없으면 1시간을 대입한다. (`pars.cpp:97–100,563–567`; `iterateq.cpp:318`) [10-21 대조 정정] [10-21 전수 검증 보완]
이 값은 먼저 읽은 `.par`의 간격을 덮어쓴다. (`pars.cpp:45–48,563–567,1036`) [10-21 대조 정정]
고전 CPU는 mass 출력 시점에 계산 경과시간을 검사한다. (`iterateq.cpp:212,309–320`) [10-21 대조 정정]
고전 CPU의 반복 체크포인트는 checkpoint가 켜진 상태에서 계산시간 기준을 만족하면 기록된다. (`iterateq.cpp:309–320`) [10-21 대조 정정]
main의 최종 공통 저장은 `if (SimStates.checkpoint == ON)`일 때 호출된다. (`lisflood.cpp:809–810`) [10-21 대조 정정]
CUDA 분기는 main의 최종 공통 저장 전에 반환한다. (`lisflood.cpp:419–457`) [10-21 대조 정정]
`acc_nugrid`에는 별도의 `write_chkpnt` 호출이 있다. (`cuda/acc_nugrid/cuda_acc_nugrid_simulate.cu:700–714`) [10-21 대조 정정]
이 체크포인트는 비균일 셀의 h와 면 목록의 q를 저장한다. (`cuda/acc_nugrid/write_chkpnt.cu:50–87`) [10-21 대조 정정]
읽기 경로는 h와 q를 해당 장치 배열로 복원한다. (`cuda/acc_nugrid/read_chkpnt.cu:194–200`) [10-21 대조 정정]
`lisflood2`의 반복 `WriteCheckpoint` 블록은 주석 처리되어 있다. (`lisflood2/sgm_fast.cpp:4600–4611`) [10-21 대조 정정]
공통 checkpoint 파일 열기에 실패하면 checkpointing을 끈다. (`chkpnt.cpp:223–226`) [10-21 대조 정정]

### 최종 체크포인트의 상태

고전 CPU의 `IterateQ`는 종료 출력에서 `if (Arrptr->maxH[ptr]>1e-3) Arrptr->maxH[ptr] += Arrptr->DEM[ptr]; else Arrptr->maxH[ptr] = NULLVAL;`을 실행한다. (`iterateq.cpp:449–477`) [10-21 대조 정정]
반환 뒤 `if (SimStates.checkpoint == ON)`이면 바뀐 `maxH`를 최종 체크포인트에 저장한다. (`lisflood.cpp:809–810`; `chkpnt.cpp:248–254`) [10-21 대조 정정]
재시작은 이 배열을 최대 수심으로 읽는다. (`chkpnt.cpp:137–143`; `iterateq.cpp:203–205`) [10-21 대조 정정]
반복 중 체크포인트는 이 종료 변환보다 먼저 기록한다. (`iterateq.cpp:309–320`; [LV1-266 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LV1.md)) [10-21 대조 정정]
이 결함 후보의 강도는 강함이다. ([LV1-266 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LV1.md)) [10-21 대조 정정]
기본 빠른 SGC는 공통 체크포인트 배열을 해제하고 NULL로 만든다. (`lisflood2/lisflood_processing.cpp:1536–1572,2092–2122`; `utility.cpp:43–50`) [10-21 대조 정정]
checkpoint가 켜진 최종 writer는 NULL 배열을 사용하는 결함 후보이다. (`lisflood.cpp:773–775,810`; `chkpnt.cpp:248–251`) [10-21 대조 정정]
`RESULT_CHECK`를 정의한 빌드는 이 해제 조건에서 제외된다. (`lisflood2/lisflood_processing.cpp:1536–1572,2092–2122`) [10-21 대조 정정]
이 결함 후보의 강도는 강함이다. ([LI2-349 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI2.md)) [10-21 대조 정정]

## 5. 침투·증발·강우·라우팅 (`infevap.cpp`)

### `FPInfiltration` (infevap.cpp:14)
비채널 셀(`ChanMask==-1`)만, `H>DepthThresh`일 때 `cell_inf = InfilRate * Tstep`(깊이율)만큼 감소. 음수 방지 후 `InfilTotalLoss += cell_inf*dA` 질량수지(infevap.cpp:24-39). **균일 율** — 분포 침투는 input.cpp `LoadDistInfil`로 별도.

### `Evaporation` (infevap.cpp:51)
고전 증발은 `evap_rate=InterpolateTimeSeries(Arrptr->evap,Solverptr->t);`로 공간 균일 시변율을 구한다. (`infevap.cpp:56`) [10-21 대조 정정] [10-21 전수 검증 정정]
고전 증발은 `if(Arrptr->ChanMask[i+j*Parptr->xsz]==-1)` 안에서 `if(h0>Solverptr->DepthThresh)`를 만족하는 셀에 적용한다. (`infevap.cpp:64–79`) [10-21 대조 정정]
고전 증발은 `Parptr->EvapTotalLoss+=cell_evap*Parptr->dA;`로 제거 체적을 누적한다. (`infevap.cpp:79`) [10-21 전수 검증 정정]
입력 증발율은 mm/day에서 m/s로 환산한다. 환산식은 `Arrptr->evap->value[i] /= (1000 * 24 * 3600);`이다. (`input.cpp:2137–2139`) [10-21 대조 정정] [10-21 전수 검증 정정]
고전 `Evaporation`은 얕은 셀에서 `cell_evap+=h0;`으로 줄인 값을 다음 셀에도 재사용할 수 있다. (`infevap.cpp:56–79`) [10-21 대조 정정]
뒤의 모든 젖은 셀에서 원래 증발율에 따른 제거량을 사용한다고 단정하지 않는다. ([LB1-401 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LB1b.md)) [10-21 대조 정정]
이 결함 후보의 강도는 강함이다. ([LB1-401 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LB1b.md)) [10-21 대조 정정]
이 결함 후보의 범위는 비SGC 고전 증발 경로이다. (`iterateq.cpp:141–156`; [LT1-314 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LT1.md)) [10-21 대조 정정]

### `Rainfall` (infevap.cpp:91)
이 절은 고전 CPU `Rainfall`을 설명한다. (`iterateq.cpp:153–157`; `infevap.cpp:91–124`) [10-21 대조 정정]
직접 호출 조건은 `Statesptr->rainfall == ON && Statesptr->routing == OFF`이다. (`iterateq.cpp:155–156`) [10-21 대조 정정]
고전 `Rainfall`은 `rain_rate=InterpolateTimeSeries(Arrptr->rain,Solverptr->t);`로 공간 균일 시변율을 구한다. (`infevap.cpp:96`) [10-21 전수 검증 정정]
고전 `Rainfall`의 셀 루프에는 OpenMP 병렬 지시문이 있다. (`infevap.cpp:99`) [10-21 전수 검증 정정]
`LoadRain`은 `Arrptr->rain->value[i] /= (1000 * 3600);`으로 입력 강우율을 mm/hr에서 m/s로 환산한다. (`input.cpp:2157–2159`) [10-21 전수 검증 정정]
`LoadEvap`과 `LoadRain`의 시계열 읽기는 첫 줄을 건너뛴다. (`input.cpp:1869–1872,2134,2154`) [10-21 전수 검증 정정]
균일 강우의 일반 CPU `Rainfall` 경로는 `if (Arrptr->DEM[p0] != Parptr->nodata_elevation)`을 만족하는 셀에 적용한다. (`infevap.cpp:105–124`) [10-21 대조 정정]
CPU `Rainfall`은 강우 체적을 `RainTotalLoss`에 누적한다. (`infevap.cpp:105–124`) [10-21 대조 정정]
CPU `DynamicRain`도 실제 단계 dt와 셀 면적으로 강우 체적을 누적한다. (`rain/rain.tpp:178–184`; [ACC·adaptive 보고서 외력 수정안](../../../_staging/recovery/compare/lisflood-cpu-gpu-acc-adaptive.md#44-cpu-accsgc외력-노트)) [10-21 대조 정정]
GPU ACC 강우 갱신은 CPU `RainTotalLoss` 장부를 누적하지 않는다. (`cuda/cuda_rain.cu:98–114`; `cuda/acc_nugrid/rain.cu:56–78`; `cuda/acc_nugrid/rain_uniform.cu:24–41`; `cuda/acc/cuda_acc_solver.cu:154–165`) [10-21 대조 정정] [10-21 전수 검증 보완]
GPU 균일 강우 reader는 구간 전진 시 분·시간을 혼합해 보간하는 결함 후보이다. (`rain/Rainfall_uniform.h:60–91`; `cuda/acc_nugrid/RainfallUniform.h:65–96`) [10-21 대조 정정]
이 결함 후보의 강도는 강함이다. ([LG2-074 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG2.md)) [10-21 대조 정정]
균일 GPU ACC의 동적 강우와 비균일 GPU ACC의 강우는 유동·시각 증가에 사용할 새 dt보다 먼저 이전 dt로 적분하는 결함 후보이다. (`cuda/acc/cuda_acc_simulate.cu:181–230`; `cuda/acc_nugrid/cuda_acc_nugrid_simulate.cu:551–578,621`; [LG2-077 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG2.md)) [10-21 대조 정정]
이 결함 후보의 강도는 강함이다. ([LG2-077 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG2.md)) [10-21 대조 정정]
균일·비균일 GPU ACC의 균일 강우는 CPU의 강우 직후 음수 제한을 생략한다. (`infevap.cpp:105–124`; `cuda/acc_nugrid/rain_uniform.cu:24–41`; `cuda/acc/cuda_acc_solver.cu:154–165`) [10-21 대조 정정] [10-21 전수 검증 정정]
CUDA FV1은 `if (states.rainfall == ON)` 안에서 `solve->update_uniform_rain(rainfall_uniform.value);`를 호출한다. (`cuda/fv1/cuda_fv1_simulate.cu:140–153`) [10-21 대조 정정]
CUDA FV2의 `update_uniform_rain` 본문은 `return;`이다. (`cuda/fv2/cuda_fv2_solver.cu:754–760`) [10-21 대조 정정]
CUDA FV2의 동적 강우는 `if (rain.enabled())` 안에서 갱신한다. (`cuda/fv2/cuda_fv2_simulate.cu:132–175`) [10-21 대조 정정]
CPU·GPU 공간 강우는 `tile_j` 상한을 검사하지 않는 결함 후보이다. (`rain/rain.tpp:21–29,35–54,113–124,141–152`; `cuda/cuda_rain.cu:73–81`; `cuda/acc_nugrid/rain.cu:28–39`) [10-21 대조 정정]
이 결함 후보의 강도는 중간이다. ([LG2-075 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG2.md)) [10-21 대조 정정]
CPU와 균일 GPU ACC의 아래쪽 초과 주장은 문서의 같은 원점 조건을 벗어난 입력에 한정한다. (user manual.docx p.37(변환본); [LG2-075 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG2.md)) [10-21 대조 정정]
NetCDF를 끈 GPU ACC 빌드는 설정하지 않은 `enabled_`를 읽는 결함 후보이다. (`rain/rain_stub.tpp:5–11`; `rain/rain.h:89–114`; `cuda/acc/cuda_acc_simulate.cu:181`; `cuda/acc_nugrid/cuda_acc_nugrid_simulate.cu:551`) [10-21 대조 정정]
이 결함 후보의 강도는 강함이다. ([LG2-076 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG2.md)) [10-21 대조 정정]
빈 강우 커널은 GPU ACC 호스트의 상태 읽기를 없애지 않는다. (`cuda/cuda_rain.cu:5–9,98–114`; `cuda/acc_nugrid/rain.cu:6–10,56–78`) [10-21 대조 정정]

### `FlowDirDEM` / `Routing` (infevap.cpp:131 / 310)
`FlowDirDEM`은 얕은 강우류 라우팅용 D4 최저이웃 방향맵을 만든다. (`infevap.cpp:131–296`) [10-21 대조 정정]
경계 셀은 `if (BCptr->BC_Ident[BCi] != NONE0)`일 때 자기 자신을 이동 대상으로 설정한다. (`infevap.cpp:263–288`) [10-21 대조 정정] [10-21 전수 검증 정정]
점원 셀은 자기 자신을 이동 대상으로 설정한다. (`infevap.cpp:291–296`) [10-21 전수 검증 정정]
선택한 이동 면에 위어가 있으면 `Statesptr->weirs == ON`일 때 자기 자신을 이동 대상으로 설정한다. (`infevap.cpp:176–180,192–196,208–212,224–228`) [10-21 전수 검증 정정]
SGC 채널 셀은 `if (Statesptr->SGC==ON)` 안에서 `if (Arrptr->SGCwidth[p0]>C(0.0))`를 만족하면 자기 자신을 이동 대상으로 설정한다. (`infevap.cpp:249–256`) [10-21 전수 검증 정정]
기본 `Routing`은 고정 속도이다. (`infevap.cpp:185–237`) [10-21 대조 정정]
`dist_routing` 모드는 DEM 경사의 제곱근을 속도에 곱한다. (`infevap.cpp:185–189`; [LT1-305 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LT1.md)) [10-21 대조 정정]
북·남 방향의 이동 시간은 `Arrptr->RouteInt[p0] = dy / Routing_Speed;`로 설정한다. 동·서 방향은 `Arrptr->RouteInt[p0] = dx / Routing_Speed;`로 설정한다. (`infevap.cpp:189,205,221,237`) [10-21 전수 검증 정정]
`Routing`의 조건은 `if(h0<Solverptr->DepthThresh || Sfy>=Parptr->RouteSfThresh || Sfx>=Parptr->RouteSfThresh)`이다. (`infevap.cpp:371`) [10-21 대조 정정]
기본 `DepthThresh`는 1e-3이다. (`lisflood.cpp:174`) [10-21 대조 정정]
기본 `RouteSfThresh`는 0.1이다. (`lisflood.cpp:138`) [10-21 대조 정정]
이동 방향은 최저 DEM 이웃으로 정한다. (`infevap.cpp:131–296`; [DOCX 보고서 IO 수정안](../../../_staging/recovery/compare/lisflood-docx-manual-vs-code.md#42-소스-분석-노트)) [10-21 대조 정정]
현재 수면차는 `flow=(z0+h0)-(z1+h1);`로 계산한다. (`infevap.cpp:377–383`) [10-21 대조 정정]
이동량에는 `if(flow>h0) {flow=h0;}`를 적용한다. (`infevap.cpp:377–383`) [10-21 대조 정정]
이동량에는 `if(flow<0) {flow=0;}`를 적용한다. (`infevap.cpp:377–383`) [10-21 대조 정정]
이동 비율은 `flow_fraction=Solverptr->Tstep/Arrptr->RouteInt[p0];`로 계산한다. (`infevap.cpp:385`) [10-21 전수 검증 정정]
이동 비율에는 `if(flow_fraction>1) flow_fraction=1;`을 적용한다. (`infevap.cpp:386`) [10-21 전수 검증 정정]
실제 이동 수심은 `flow=flow*flow_fraction;`으로 정한다. (`infevap.cpp:388–391`) [10-21 전수 검증 정정]

## 6. 출력 래스터 (`output.cpp`)

### ASCII (`write_ascfile`, output.cpp:39)
파일명 = `root[-SaveNumber]extension` (SaveNumber 0–9999는 4자리 zero-pad, output.cpp:64-66). Arc/Info ASCII 헤더(ncols/nrows/xll/yll/cellsize/NODATA)를 `outflag`에 맞춰 작성. `outflag`:
- 0: 셀 중심값 (xsz×ysz)
- 1: Qx 플럭스 (xsz+1, 원점 -dx/2 오프셋, output.cpp:113-115)
- 2: Qy 플럭스 (ysz+1, 원점 -dy/2)
- 3: 수면표고 = DEM+H, `H<=depth_thresh` 셀은 NULLVAL(output.cpp:150-172)

`alt_ascheader` ON 시 사용자 헤더 6줄 사용(output.cpp:79-85). `gzip` ON이면 `system("gzip -9 -f ...")`(output.cpp:179-182).
일반 flux ASCII에서 `ascheader`와 `outflag` 1·2를 함께 쓰면 헤더를 12행으로 만드는 결함 후보이다. (`output.cpp:79–85,110–144`; [LI2-344 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI2.md)) [10-21 대조 정정]
이 결함 후보의 강도는 강함이다. ([LI2-344 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI2.md)) [10-21 대조 정정]

### Binary (`write_binrasterfile`, output.cpp:506)
Binary 격자의 첫 두 값은 `int`형 열 수와 행 수이다. (`output.cpp:551–617`; `input.cpp:1244–1256`) [10-21 대조 정정] [10-21 전수 검증 정정]
그 뒤 좌표·격자 간격·NoData·자료의 저장 형식은 `NUMERIC_TYPE`이다. (`output.cpp:551–617`) [10-21 대조 정정] [10-21 전수 검증 정정]
`NUMERIC_TYPE`은 빌드에 따라 double 또는 float이다. (`lisflood.h:75–97`; [LV1-171 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LV1.md)) [10-21 대조 정정]
이진 격자의 읽기와 쓰기는 같은 수치 모드를 사용해야 한다. (`input.cpp:1244–1256`; `output.cpp:551–617`; [files-output 수정안](../../../_staging/recovery/compare/lisflood-files-output-vs-code.md#4-노트-대조와-수정안)) [10-21 대조 정정]
일반 binary flux는 선언한 격자 크기와 자료 길이가 다른 결함 후보이다. (`output.cpp:568–596`) [10-21 대조 정정]
x 헤더는 `(xsz+1)*ysz`이다. (`output.cpp:568–596`) [10-21 대조 정정]
y 헤더는 `xsz*(ysz+1)`이다. (`output.cpp:568–596`) [10-21 대조 정정]
두 분기는 `(Parptr->xsz+1)*(Parptr->ysz+1)`개를 쓴다. (`output.cpp:568–596`) [10-21 대조 정정]
이 결함 후보의 강도는 강함이다. ([LI2-345 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI2.md)) [10-21 대조 정정]
Windows binary 시작 로더의 text 모드는 바이트 변환 결함 후보이다. (`input.cpp:18–32,1241–1256`) [10-21 대조 정정]
이 결함 후보의 강도는 중간이다. ([LI2-343 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI2.md)) [10-21 대조 정정]
출력 NoData 값은 -9999이다. (`output.cpp:521`) [10-21 대조 정정]

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
표시용 DEM의 기본 출력은 5.9.23에서 추가되었다. (`VersionHistory.h:109`) [10-21 대조 정정]
현재 `maxdepthonly`가 아닌 CPU 전처리 경로에서는 debug 없이도 `.dem`을 쓴다. (`lisflood.cpp:756–768`) [10-21 대조 정정]
현재 SGC `.dem`의 데이터는 `SGCz`이다. (`lisflood.cpp:765–768`) [10-21 대조 정정]
이 데이터는 입력 범람원 DEM과 항상 같지 않다. (`lisflood.cpp:765–768`; [LV1-216 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LV1.md)) [10-21 대조 정정]

## 7. 입력 파일 포맷 요약

| 파일 | 포맷 | 핵심 구조 |
|---|---|---|
| DEM | Arc/Info ASCII grid | 6줄 헤더 + 행우선 값, NODATA→`nodata_elevation` |
| `.bci` | 텍스트 라인 | `{N/S/E/W} start finish {TYPE} [val/name]` 또는 `{P/F} px py {TYPE} ...` |
| `.bdy` | 명명 시계열 블록 | 이름 줄 + `count units` + `value time` 쌍 (단위 자동환산) |
| `.evap` | 시계열 (mm/day) | 첫 줄 skip, m/s 환산 |
| `.rain` | 시계열 (mm/hr) | 첫 줄 skip, m/s 환산 |
| checkpoint(`.chkpnt`) | 바이너리 | 형식 판·driver별 저장 상태를 구분한다. (`chkpnt.cpp:211–314`; `cuda/acc_nugrid/write_chkpnt.cu:75–87`) [10-21 대조 정정] [10-21 전수 검증 보완] |

문서와 코드 차이 표는 [lisflood-fp-io-boundary-differences.md](lisflood-fp-io-boundary-differences.md)에 있다.

## 한계·주의

- 알 수 없는 parfile 키워드는 무시한다. 진단 출력에는 `if (verbose == ON)` 조건이 있다. (`pars.cpp:1020`) [10-21 대조 정정]
- `InterpolateTimeSeries` non-thread-safe(boundary.cpp:1420).
- 고전 침투·증발은 비하도 셀과 수심 문턱을 따른다. (`infevap.cpp:24–39,64–79`) [10-21 대조 정정]
- `netcdf_out`의 효과는 빌드와 출력 경로에 의존한다. 미지원 격자는 ASCII로 대체한다. (`lisflood2/file_tool.cpp:764–788`; [LI1-136 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI1.md)) [10-21 대조 정정]
