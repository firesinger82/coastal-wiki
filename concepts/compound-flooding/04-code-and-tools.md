---
title: "복합침수 외력 인터페이스 — 네 갈래를 한 시간축에 올리는 문제 (SFINCS·LISFLOOD-FP·ADCIRC 대조)"
topic: compound-flooding
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "[[03-analysis-methods]] §6 이 '확률 해석과 모델 강제를 잇는 고리가 비어 있다' 로 남긴 공백을 채운다. 본 노트의 모델 단언은 **전부 본 위키의 verified source-analysis·manual-notes 노트로 소급**한다(절대규칙 #6 — 모델 메커닉은 models/ 소관, 여기는 요약+링크): SFINCS [[sfincs_boundaries_forcing]](sfincs_boundaries.f90·sfincs_discharges.f90·sfincs_meteo.f90·sfincs_spiderweb.f90·sfincs_infiltration.f90 직접 read), LISFLOOD-FP [[lisflood-fp-io-boundary]](input.cpp·pars.cpp·boundary.cpp·infevap.cpp 직접 read), ADCIRC [[adcirc-met-forcing-implementation]]·[[adcirc-tidal-forcing]]·[[17-boundary-and-forcing-inputs]]. **본 세션에서 새로 실측한 것 1건**: LISFLOOD-FP C/C++/CUDA 소스 **전수 623개**(`*.cpp` 83 + `*.h` 388 + `*.cu` 152, 하위 디렉터리 포함 전부)에서 `tidal|harmonic|constituent` 매칭 **0개** — 조석 합성 부재를 '노트에 안 보인다' 가 아니라 수를 세어 확인했다. 계수는 `<!-- count: -->` 지시자로 G10(`tools/validate-counts.sh`)이 glob 실측 재현한다. ★첫 측정에서 `grep -v "^./test"` 가 `testing/` 과 `tests.cpp` 까지 걷어내 616으로 나왔다 — 제외 패턴을 다시 세어 623으로 정정했다(매칭 0은 세 변형 모두 동일). 부재의 반대증거로 Tauranga 시험사례 `testing/UoS/tauranga/preprocess.py` 가 외부 조위계 자료를 읽어 `tauranga.bdy` 를 **직접 생성**함을 확인했다. **한계**: Delft3D·EFDC 의 외력 인터페이스는 대조에 넣지 않았다(§6). 질량수지 회계는 LISFLOOD-FP 만 확인했다."
note_author: "Claude Opus 5 (1M context)"
note_date: 2026-09-22
related:
  - concepts/compound-flooding/03-analysis-methods.md
  - concepts/compound-flooding/06-model-application.md
  - concepts/compound-flooding/wetting-drying-cross-model.md
  - models/SFINCS/source-analysis/sfincs_boundaries_forcing.md
  - models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md
---

# 복합침수 외력 인터페이스

> [[06-model-application]] 은 **어떻게 푸는가**(솔버·격자·비용)로 모델을 갈랐다.
> 복합침수에서 실제로 사람을 다치게 하는 것은 그 앞단이다 — **네 갈래 외력을
> 하나의 시간축에 올려놓는 일.** [[03-analysis-methods]] §6 이 남긴 공백이 여기다.

## 1. 대조표 — 각 인자를 무엇으로 받는가

| 인자 | **SFINCS** | **LISFLOOD-FP** | **ADCIRC** |
|---|---|---|---|
| **조석** | `bca` 천문조 성분(진폭·위상) → nodal factor 적용 후 **모델 내부 합성**[^sf-bca] | **없음** — `.bdy` 수위 시계열로 외부 주입[^lf-notide] | tidal potential body-force + open-BC 조위, constituent 방식[^ad-tide] |
| **해일** | `bzs` 수위 시계열 + 기압역조 보정[^sf-patm] | `.bci` `HFIX`/`HVAR` 수위 경계[^lf-bci] | 기상강제로 **모델이 생성**(또는 경계 주입) |
| **파(IG)** | `bzi` incoming infragravity 시계열[^sf-bca] | 없음 | SWAN/STWAVE 결합 |
| **강우** | 격자(`ampr`)·시계열(`prcp`)·spiderweb 동반 강우[^sf-meteo] | 도메인 **균일** 시변율(`rainfall`)[^lf-rain] | (본 대조 범위 밖) |
| **강우손실** | 침투 **6종**(상수·공간변동·CN 구/신·Green-Ampt·modified Horton)[^sf-inf] | 균일 침투율 + 증발(분포형은 별도 마스크)[^lf-rain] | — |
| **하천** | 점소스 `src/dis` + 하류 하천 경계 `bdr`(kcs=5) + 배수구조물 5종[^sf-disc] | `.bci` point source·`QFIX`/`QVAR`, `Qfile`/`riverfile`, SGC 채널[^lf-bci] | 유입 flux 경계 |
| **태풍** | spiderweb `.spw` 극좌표 격자 — **Holland 류 모델은 내부에 없음**, 외부 생성물[^sf-spw] | 없음 | `NWS` 분기(OWI·parametric 등)[^ad-nws] |

한 줄로: **SFINCS 는 해양측 외력을 조립까지 해 주고, LISFLOOD-FP 는 완성된 수위 시계열을 요구하며,
ADCIRC 는 해일을 스스로 만든다.**

### ★ LISFLOOD-FP 에 조석이 없다는 것의 의미

이것은 노트에 안 보여서 내린 추정이 아니라 **센 것**이다. C/C++/CUDA 소스 **전수 623개**에서
`tidal|harmonic|constituent` 매칭이 **0개**다. 반대증거도 있다 —
Tauranga 시험사례의 전처리 스크립트가 외부 조위계 자료를 읽어 `tauranga.bdy` 를 직접 만든다.[^lf-notide]

<!-- count: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/**/*.cpp = 83 -->
<!-- count: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/**/*.h = 388 -->
<!-- count: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/**/*.cu = 152 -->

그래서 LISFLOOD-FP 로 복합침수를 하면 **조석+해일 합성이 모델 밖에서 일어난다.**
그 순간 [[03-analysis-methods]] §3 의 결합확률 문제 — 두 성분을 독립으로 볼 것인가, 조건부로 볼 것인가 —
가 통째로 **사용자 책임으로 넘어온다.** SFINCS 처럼 `bca`+`bzs` 를 모델이 합성하면 그 합성은
모델의 결정이고, `.bdy` 하나를 넣으면 그 합성은 전처리 스크립트의 결정이다.
**외력을 어디서 합치느냐가 확률 가정을 누가 지느냐를 정한다.**

## 2. ★ 시계열이 모자랄 때 — 세 갈래 운명

복합침수 실행에서 네 외력의 시계열은 출처가 제각각이라 **구간이 어긋나는 것이 정상**이다.
그때 모델이 하는 일이 정반대로 갈린다.

| 모델 | 시계열이 모의구간을 못 덮으면 | 시간축 형식 |
|---|---|---|
| **SFINCS** | **경고 후 첫/끝 시각을 `t0-1.0`/`t1+1.0` 으로 강제 보정** — 즉 값을 상수 연장해 계속 달린다[^sf-extend] | 불규칙 `value time` 허용 |
| **SFINCS**(spiderweb) | 범위 밖이면 첫/끝 시점 사용 + **6시간 ramp** spin-up[^sf-spinup] | 〃 |
| **LISFLOOD-FP** | `QVAR`/`HVAR` 로 선언됐는데 시계열이 없으면 **그 경계를 `NONE0`(닫힘)으로 비활성화**[^lf-noseries] | 불규칙 허용, **시간 단조증가 아니면 abort**[^lf-mono] |
| **ADCIRC** | — | 격자 기상은 **등간격 `WTIMINC` 전제**. 불균등 시각은 보간을 깨뜨린다[^ad-wtiminc] |

세 동작 모두 방어적이지만 **복합침수에서의 결과는 정반대다.**

- SFINCS 는 **부족한 외력을 상수로 늘려서 계속 켜 둔다.** 강우 파일이 짧으면 마지막 강우강도가
  모의 끝까지 유지될 수 있다 — 복합성은 유지되지만 값이 틀린다.
- LISFLOOD-FP 는 **부족한 외력을 꺼 버린다.** 조석 경계 시계열이 빠지면 그 변이 닫힌 경계가 되고,
  **복합침수가 조용히 단일 인자 침수로 강등된다.** 실행은 정상 종료한다.
- ADCIRC 는 형식 위반을 **입력 단계에서 드러낸다** — 다만 등간격 요구 자체가 이질적 외력을
  공통 시간축으로 리샘플링하도록 강제한다.

실무 함의: **실행 후 로그의 경고를 읽지 않으면 어느 외력이 실제로 작동했는지 알 수 없다.**
복합침수 run 의 검수 항목에 "네 외력이 모두 켜져 있었는가" 가 들어가야 하는 이유다.

## 3. ★ 조용한 실패 — 세 번째 사례

LISFLOOD-FP 의 parfile 파서는 **인식하지 못한 키워드를 abort 없이 무시**한다
("Unknown parameter ignored").[^lf-typo] `rainfall` 을 `rainfal` 로 치면 강우가 없는
run 이 정상 종료한다.

이것은 본 위키가 이미 두 번 만난 패턴이다.

| 모델 | 상황 | 처리 |
|---|---|---|
| ShorelineS | `runupform` 오타 | **조용히 Larson 식 적용** ([[../swash-zone/03-analysis-methods]] §2) |
| ADCIRC | 얼음 항력법 이름 미인식 | **`terminate(ADCIRC_EXIT_FAILURE)`** ([[../../models/ADCIRC/manual-notes/19-ice-coverage]] §4-②) |
| LISFLOOD-FP | parfile 키워드 미인식 | **경고 후 무시**[^lf-typo] |

복합침수에서는 대가가 더 크다. 오적용이 수치를 틀리게 하는 데 그치지 않고
**인자 하나를 통째로 빼기** 때문이다.

SFINCS 의 침투 설정에도 같은 성격의 결합이 있다. 침투법은 NetCDF 키워드 또는
**파일 존재 여부로 자동 선택**되고, 방법들은 stack 되도록 설계되지 않았다.
더 중요한 것은 소스 주석이 명시한 제약이다 — *"Infiltration only works when rainfall is activated"*.
강우 없이 침투만 쓰려면 **0.0 강우 파일을 넣어야 한다.**[^sf-inf]

## 4. pluvial 성분의 유효량은 침투가 정한다

[[03-analysis-methods]] §5 에서 LACPR 이 강우를 고정 10년 빈도로 부과한 것을 봤다.
그런데 격자에 들어간 강우가 곧 침수기여량은 아니다 — **침투를 뺀 나머지**가 유효강우다.

- **SFINCS**: `netprcp = prcp − qinfmap`. 침투법 6종 중 Curve Number(구/신)·Green-Ampt·
  modified Horton 은 SWMM 식을 따르고, 신 CN 과 Green-Ampt 는 **비강우 구간의 회복(recovery)** 까지 다룬다.[^sf-inf]
- **LISFLOOD-FP**: 도메인 **균일 침투율** `cell_inf = InfilRate × Tstep`(분포형은 별도 파일).
  게다가 `Rainfall` 은 **라우팅이 꺼져 있을 때만 호출**된다.[^lf-rain]

즉 같은 "10년 6시간 강우" 를 넣어도 **두 모델이 만드는 runoff 가 다르고, 그 차이는 솔버가 아니라
손실 모델에서 나온다.** [[06-model-application]] 의 정확도·비용 축으로는 보이지 않는 차이다.

## 5. 질량수지 회계 — 인자별 기여 분해

LISFLOOD-FP 는 경계 유입/유출(`Qin`/`Qout`), 하천·점소스(`Qpoint_pos/neg`),
침투손실(`InfilTotalLoss`)·증발손실(`EvapTotalLoss`)·강우(`RainTotalLoss`)를 **각각 따로 적산**하고
checkpoint 에도 저장한다.[^lf-mass] 복합침수에서 이것은 진단 자산이다 —
**침수 체적을 인자별로 분해해 "이번 사건에서 pluvial 이 몇 %였나" 를 사후에 물을 수 있다.**

> [!source-needed]
> SFINCS 의 대응 회계(외력별 누적 체적 출력)는 [[sfincs_boundaries_forcing]] 범위에서 확인되지 않았다.
> [[sfincs_io_data]] 확인 후 보강한다.

## 6. 남은 것

- **Delft3D·EFDC 미대조** — full-physics 두 모델의 외력 인터페이스는 본 표에 없다.
  [[06-model-application]] §2 가 솔버 수준에서만 다룬다. `source-needed`
- **SFINCS 질량수지 회계** — §5 콜아웃. `source-needed`
- **ADCIRC 강우·하천** — 본 대조는 ADCIRC 의 조석·기상만 다뤘다. ADCIRC 가 pluvial/fluvial 을
  어떻게 받는지(또는 받지 않는지)는 미조사. `source-needed`
- **오프라인 커플링 실무** — SFINCS·LISFLOOD-FP 를 ADCIRC/Delft3D 출력으로 강제하는
  실제 워크플로(격자 간 보간·시간 리샘플링 도구)는 본 위키에 없다. `source-needed`
- **§2 의 세 동작은 각 1개 경로 확인** — SFINCS 경계 시계열, LISFLOOD-FP bdy 매칭,
  ADCIRC NWS=2 fort.22. 모든 외력 경로가 같은 정책을 따르는지는 확인하지 않았다.

## 출처

본 노트의 모델 단언은 절대규칙 #6 에 따라 전부 `models/` 의 verified 노트로 소급한다.
아래 각주는 그 노트와, 해당 노트가 인용한 소스 위치를 함께 밝힌다.

[^sf-bca]: [[sfincs_boundaries_forcing]] §1.3·§1.4 — `bcafile` 천문조 성분 `(name, amplitude, phase)` 를 `[forcing]` 블록(=bnd 점당) 단위로 읽고, `update_nodal_factors` 로 nodal factor·주파수 산정 후 rad/s 변환(`sfincs_boundaries.f90:293-448`). 합성은 $z_{s,tb} = z_{s,bnd} + \sum_{ic} A_{ic}\cos(\omega_{ic} t - \phi_{ic})$ (`:736-744`). IG 시계열은 `bzifile` → `zsi_bnd`(`:126-141`), still water `zsb0` 와 total `zsb` 분리(`:865-866`).
[^sf-patm]: [[sfincs_boundaries_forcing]] §1.6 — kcs=2 경계에서 `patmos .and. pavbnd>1.0` 일 때 $z_s \mathrel{+}= (p_{av,bnd}-p_{atm,b})/(\rho_w \cdot 9.81)$ (`sfincs_boundaries.f90:820-826`).
[^sf-meteo]: [[sfincs_boundaries_forcing]] §3.1 — 격자 강우 `amprfile`/`netamprfile`(`sfincs_meteo.f90:170-188`), 시계열 강우 `prcpfile`(`:269`), spiderweb 강우는 `nquant==4` 일 때 포함(§4.1). 격자 강우는 `ampr_block` 기본 true 로 **block(계단)보간**(`:1142-1148`).
[^sf-inf]: [[sfincs_boundaries_forcing]] §5 — 핵심 주석 *"Infiltration only works when rainfall is activated"* (`sfincs_infiltration.f90:28`), 방법 stack 비설계(`:30`). 타입 `con`/`c2d`/`cna`/`cnb`/`gai`/`hor` 는 NetCDF `inftype` 또는 **파일 존재로 자동 선택**(`:74-135`). 회복률 SWMM Eq 4-36(`:374-375`), Green-Ampt SWMM Eq 4-27(`:856`), modified Horton 지수감쇠(`:967`,`:979`). 공통 후처리 `netprcp(nm) -= qinfmap(nm)`(`:661` 등).
[^sf-disc]: [[sfincs_boundaries_forcing]] §1.2·§2 — 하류 하천 경계 `bdrfile`, $\Delta z_{s,bdr} = -\,\text{slope}\times\text{distance}$ (`sfincs_boundaries.f90:217-268`), kcs=5. 점소스 `srcfile`+`disfile`, 배수구조물 5종(pump·culvert·check valve·controlled gate×2), `nsrcdrn = nsrc + 2\,n_{drn}` (`sfincs_discharges.f90:86,209-225`).
[^sf-spw]: [[sfincs_boundaries_forcing]] §4 — "태풍 parametric wind(Holland 류 등 외부 생성 .spw 극좌표 격자)을 읽는 저수준 I/O. **물리 모델(Holland)은 SFINCS 내부에 없음**" (`sfincs_spiderweb.f90` 전반). 바람은 land reduction(Westerink et al. 2008) 포함해 stress 로 변환(`sfincs_meteo.f90:709-740`).
[^sf-extend]: [[sfincs_boundaries_forcing]] §1.1 — "시계열이 시뮬레이션 구간을 못 덮으면 경고 후 첫/끝 시각을 `t0-1.0` / `t1+1.0` 으로 강제 보정"(`sfincs_boundaries.f90:143-164`).
[^sf-spinup]: [[sfincs_boundaries_forcing]] §3.3 — "spw 시간범위 밖이면 첫/끝 시점 사용 + **6시간(21600s) ramp** spin-up factor"(`sfincs_meteo.f90:476-494`). 별도로 meteo 전반 spin-up 은 `(t-t_0)/(t_{spinup}-t_0)` ramp(`:1336-1385`), 경계 수위도 `t<tspinup` 구간에 `zini` 와 가중평균 smoothing(`sfincs_boundaries.f90:851-862`).
[^lf-notide]: 본 세션 실측(2026-09-22, pinned snapshot): `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP` 하위 `*.cpp`(83)·`*.h`(388)·`*.cu`(152) **전수 623개**에 대해 `grep -ril "tidal\|harmonic\|constituent"` → **0개**. `test/` 디렉터리 6개를 빼도(617개) 결과는 같다. 매칭은 저장소 전체로 넓혔을 때 `testing/UoS/{hilo,tauranga}/*.py` 전·후처리 스크립트와 `test/catch.hpp`(확장자 `.hpp` 라 위 623 집합 밖)에만 존재한다. Tauranga 시험사례 `testing/UoS/tauranga/preprocess.py` 는 외부 `input-data/tide_gauge.txt` 를 읽어(`:18`) `tidal = total − tsunami` 로 분해하고(`:24` 등) `write_bdy_file`(`:203`)로 `tauranga.bdy` 를 생성해 parfile `bdyfile` 로 연결한다(`:356`). 즉 조석은 **모델 밖에서 만들어 주입**된다. 경계 종류 목록 자체는 [[lisflood-fp-io-boundary]] §3(`lisflood.h:177-190`)에 천문조 항목이 없다.
[^lf-bci]: [[lisflood-fp-io-boundary]] §3 — `ESourceType` enum(`lisflood.h:177-190`): `NONE0`/`FREE1`/`HFIX2`/`HVAR3`/`QFIX4`/`QVAR5`/`FREE6`/`TRIB7`/`RATE8`. `.bci` 라인은 `{N/S/E/W} start finish {TYPE}` 또는 `{P/F} px py {TYPE}`(`input.cpp:1584-1652`). `.bdy` 는 명명 시계열 블록을 `BC_Name`/`Q_Name`/`PS_Name` 과 strcmp 매칭해 연결(`input.cpp:2020-2059`).
[^lf-noseries]: [[lisflood-fp-io-boundary]] §3 — "bdy 파일 없으면 QVAR/HVAR로 지정됐는데 시계열 없는 경계는 `NONE0`으로 비활성화"(`input.cpp:2100-2116`). 미참조 bdy 시계열은 경고 후 폐기(`:2065-2074`).
[^lf-mono]: [[lisflood-fp-io-boundary]] §3 — `LoadTimeSeries` 가 시간 단조증가를 강제하고 위반 시 abort(`input.cpp:1905-1909`). 단위는 `seconds/minutes/hours/days` 인식 후 초 환산, **미인식 단위는 경고 후 초로 간주**(`:1920-1932`).
[^lf-rain]: [[lisflood-fp-io-boundary]] §5 — `Rainfall`(`infevap.cpp:91`)은 "라우팅 OFF일 때만 호출"(주석 `:88-89`), 도메인 균일 시변율 `InterpolateTimeSeries(rain,t)`, NODATA 표고 셀 제외(`:108`). `FPInfiltration`(`:14`)은 비채널·`H>DepthThresh` 셀에서 `cell_inf = InfilRate × Tstep`. 같은 노트 "한계·주의": "침투·증발·(라우팅 OFF)강우는 **도메인 균일율** (분포형은 별도 마스크/파일)". rain 파일 mm/hr → m/s, evap mm/day → m/s 환산.
[^lf-typo]: [[lisflood-fp-io-boundary]] §1 — "매칭 실패 라인은 마지막에 'Unknown parameter ignored' 경고만(`pars.cpp:1019`) — **오타가 조용히 무시됨**". 같은 노트 "한계·주의" 첫 항목도 동일 지적.
[^lf-mass]: [[lisflood-fp-io-boundary]] §3.1·§4·§5 — `BoundaryFlux`(`boundary.cpp:1327`)가 외곽 Qx/Qy 를 부호로 분류해 `Qin`/`Qout` 누적, 하천 QFIX/QVAR 유입(`:1390-1393`), point source `Qpoint_pos/neg`(`:1401-1402`), `VolInMT/VolOutMT` 적산(`:1405-1406`). 침투·증발·강우는 `InfilTotalLoss`/`EvapTotalLoss`/`RainTotalLoss` 로 각각 적산(`infevap.cpp:24-39,60-80,91-`). checkpoint 가 이 누적량을 저장(`chkpnt.cpp:109-308`).
[^ad-tide]: [[adcirc-tidal-forcing]] — "ADCIRC 조석 구동의 **body-force**(open-BC tidal elevation 과 별개): ① constituent tidal potential ② SAL ③ 직접 luni-solar ephemeris ④ internal tide wave drag ⑤ harmonic analysis"(`timestep.F:1531-1560` 외).
[^ad-nws]: [[adcirc-met-forcing-implementation]] §A — `NWS` 값이 기상 입력 포맷을 분기(NWS=2/12/13/14/15 등). NWS 부호가 `WSX/WSY` 를 응력으로 볼지 풍속으로 볼지 결정한다(Working Rules 2).
[^ad-wtiminc]: [[adcirc-met-forcing-implementation]] — "WTIMINC defines bracketing times `WTIME1/WTIME2`"(`src/wind.F:2172-2181,2189`), 선형보간 `WTRATIO = (TimeLoc - WTIME1)/WTIMINC`(`:2189-2199`). Working Rules 5: "**fort.22 ASCII (NWS=2) requires equal-time-step header** — uneven time stamps break `WTIMINC` interpolation." 입력파일 개관은 [[17-boundary-and-forcing-inputs]].
