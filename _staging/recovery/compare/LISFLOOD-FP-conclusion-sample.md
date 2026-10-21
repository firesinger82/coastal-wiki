# LISFLOOD-FP 차이 결론 표본 35행 독립 검증

이 문서는 AI가 작성한 표본 검증 기록이다.
검증자는 문서 쪽 이미지와 코드 줄을 직접 열어 확인했다.
모델은 실행하지 않았다.
보고서·노트는 수정하지 않았다.
경로 약어는 다음과 같다. `현재:`는 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/`이다. `ext:`는 `_staging/recovery/extract/LISFLOOD-FP/external/`이다. `pdf`·`docx`·`bridge`는 쪽 이미지 `lf-manual-{pdf,docx,bridge-docx}-NNN.png`이다.
쪽 머리글의 판 표기를 이미지에서 읽었다. pdf와 docx는 `Code release 5.9.6`이고 bridge는 `Code release 4.3.6`이다.

| 행 ID | 최종 분류 | 판정 | 확인한 원문(파일:줄 또는 쪽) | 이유 |
|---|---|---|---|---|
| LV1-141 | A | 틀림 | docx p.31, bridge p.28, 현재:input.cpp:1920–1931, 현재:VersionHistory.h:107·453 | docx p.31의 3행 설명은 `either 'days', 'hours' or 'seconds'`이고 바로 아래 문장은 `Currently the only supported units are "seconds" and "hours"`이다. bridge p.28(4.3.6)에도 같은 모순이 있다. VersionHistory.h:453은 days를 2005년(2.6.4)에 추가했다고 적는다. 따라서 days는 두 문서보다 먼저 지원되었고, 같은 쪽의 days 표기를 "갱신된 지원 범위"로 설명한 확정 결론은 틀렸다. 문서 내부 모순이므로 days 부분은 B이다. minutes 부분만 5.9.25(2014, VersionHistory.h:107)가 문서 뒤이므로 A이다. |
| LB1-252 | B | 틀림 | bridge p.42, 현재:lisflood.h:728 | bridge p.42는 `int Nit,ts;`이고 머리글은 4.3.6이다. 현재 코드는 `long Nit, itCount;`이고 `ts`는 lisflood.h에 없다. 4.3.6의 선언문을 8.x 선언과 비교한 것이므로 판 차이(A)이다. "VersionHistory에 변경 기록이 없다"는 근거는 문서 오기를 증명하지 못한다. 변수 이름·형이 바뀌었다는 기록이 없다고 해서 4.3.6 문서가 틀렸다는 뜻이 아니다. |
| LT1-120 | C | 부분 | pdf p.13, ext:v8.0 README.md:25–33, 현재:CMakeLists.txt:67–69 | pdf p.13 원문 `A total of 14 files are deployed`와 코드 인용은 정확하다. 표 3은 파일 13행을 나열한다. 최종 문장은 이 13행·14 불일치와 "32·64비트 두 파일을 세면 14" 설명을 버렸다. 분류 C는 의문이다. 문서는 5.9.6 시기의 실행 파일 묶음을 설명하고 코드는 8.x CMake 소스 배포를 보여 주므로 A가 더 맞다. 변경 기록 부재 근거는 absence 근거이다. |
| LG1-081 | H | 틀림 | 현재:swe/dg2new.cpp:747–752, 현재:swe/flux.cpp:28, 현재:cuda/cuda_flow.cu:37, 현재:lisflood.cpp:790–796 | 인용은 모두 정확하다. dg2new `flux_y`의 첫 성분은 `HU,`이고 CPU `physical_flux_y`와 CUDA는 HV를 쓴다. `lisflood.cpp:796`의 `//solver.solve();`는 주석이므로 현재 진입점이 이 코드를 호출하지 않는다. 그러나 H의 정의(응용·성능·권장값·이론·외부 문헌)에 비활성 코드의 식 불일치는 들어 있지 않다. 이 행은 E(비활성, 강함 또는 중간)로 두고 "현재 실행 미도달"을 주석에 적는 편이 정의에 맞다. 이 판정은 정의 해석에 따른 것이다. |
| LN1-130 | F | 맞음 | 현재:VersionHistory.h:15–23, 현재:lisflood.cpp:859, ext:v8.2 lisflood.cpp:849, ext:v8.3 README.md:36–39, ext:v8.3 patch:294–304 | 8.2는 `LF_VersionMajor.Minor.Inc`(8.1.0)를 출력하고 8.3은 `LF_Release "8.3"`을 출력한다. VersionHistory.h:21–22의 주석이 내부 숫자 유지 이유(체크포인트 기록)를 적는다. 의미는 같고 표기 방식만 다르다는 F 분류는 수용 가능하다. 8.3 README 표가 이를 변경 항목으로 적는다는 점은 최종 문장에 없으나 결론을 바꾸지 않는다. |
| LV1-065 | A | 맞음 | docx p.22, 현재:pars.cpp:499–501, 현재:lisflood.cpp:220, 현재:iterateq.cpp:154, ext:v8.0 swe/fv1.cpp:43–50 | docx p.22의 `evaporation filename` 행에 밑줄 삽입 `except FV1, DG2, Roe`가 있다. 현재 코드에서 `calc_evap` 소비는 iterateq.cpp:154(고전 해법)와 lisflood2뿐이고 FV1·DG2 시간 루프에는 없다. 구판 PDF 기술과 코드의 차이는 8.0 해법 추가에 따른 A로 맞다. |
| LV1-122 | A | 맞음 | docx p.26, pdf p.21, 현재:pars.cpp:355–360, 현재:lisflood.cpp:243 | docx p.26의 hazard 행에 밑줄 삽입 `(except FV1, DG2)`가 있고 pdf p.21에는 없다. 현재:swe와 현재:cuda에는 `hazard` 참조가 없다. A 분류가 맞다. |
| LV1-171 | A | 맞음 | docx p.37, 현재:input.cpp:1244–1256, ext:v8.0 lisflood.h:75–87, VersionHistory.h:111 | docx p.37 원문은 `The binary data are in double precision except for the first two numbers`이다. 코드는 정수 2개 뒤 `NUMERIC_TYPE`으로 읽는다. 5.9.13(2014)이 double/float 컴파일 전환을 도입했고 문서 머리글은 5.9.6이므로 A가 맞다. |
| LI1-318 | A | 맞음 | 현재:cuda/cuda_boundary.cu:286–293·316–324, ext:v8.2 cuda/cuda_boundary.cu:284–294, ext:v8.3 patch:70–92 | 패치 79행·87행이 `if (Hold == C(0.0)) continue;`를 추가했고 8.2에는 없다. 현재 코드의 두 경로에 같은 줄이 있다. 8.2→8.3 차이이므로 A가 맞다. |
| LT1-124 | A | 맞음 | pdf p.13, 현재:CMakeLists.txt:210–216, 현재:VersionHistory.h:40 | pdf p.13 표의 `DLL FILE`·`Windows only`·`Check first whether lisflood will run without this file`을 확인했다. VersionHistory.h:40은 netCDF 추가(6.0, 2014)를 적고 문서보다 뒤이다. CMake는 `_NETCDF`일 때 `DLL's/*.dll`을 복사한다. A가 맞다. |
| RF-029 | B | 맞음 | 현재:pars.cpp:27, 현재:input.cpp:1330, 현재:lisflood.cpp:319, models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:55 | 노트 55행은 `본체 파서(input.cpp)`라고 적는다. 구성 파서는 `pars.cpp:27 ReadConfiguration`이고 lisflood.cpp:319가 호출한다. input.cpp:1330은 LoadDEM이다. 노트 오기(B)가 맞다. |
| LI2-105 | B | 맞음 | pdf p.33, pdf p.27 | pdf p.33 절차 1은 `described in section 4.2.6`이다. pdf p.27 제목은 `3.2.6 Digital Elevation Model file`이다. 문서 내부 절 번호 오기이므로 B가 맞다. |
| LV1-189 | B | 맞음 | docx p.19, docx p.40, 현재:lisflood.cpp:328–334·379–380 | docx p.19 `dirroot`는 `excluding the .chkpnt file`이고 p.40은 `in the directory from which the model was executed`이다. 코드는 `resrootname`(dirroot 포함)에 `.chkpnt`를 붙인다. 두 쪽 인용은 정확하다. 단 5.9.6 시점의 코드는 확인하지 못했고 근거는 v8.0·현재 코드와 변경 기록 부재뿐이다. |
| LB1-257 | B | 틀림 | bridge p.43, 현재:lisflood.h:378–395 | bridge p.43은 `char demfilename[80];` 등 80자 배열이고 머리글은 4.3.6이다. 현재 구조체는 256자·512자이다. 4.3.6 선언과 8.x 선언의 비교이므로 A이다. "모듈화 이력이 80→256 변경을 명시하지 않는다"는 근거는 문서 오기를 증명하지 못한다. 같은 쪽의 `Qfilename`은 현재 구조체에 없다. |
| LB1-255 | B | 맞음 | bridge p.43, 현재:input.cpp:1484·1490 | bridge p.43 원문은 `Top left, bottom right corners`이다. 코드는 `blx`를 xllcorner로 읽고(input.cpp:1484) `tlx = blx`, `tly = bly + ysz*dy`로 왼쪽 위를 만든다. blx·bly는 왼쪽 아래이다. bridge p.28도 xllcorner를 lower left로 적는다. B가 맞다. |
| LI1-274 | C | 맞음 | 현재:cuda/adaptive/classes/SolverParams.h:23·54–61, 현재:cuda/adaptive/input/read_keyword_real.cpp:1–45 | `tol_Krivo` 초기값 9999와 `limitslopes`일 때만 읽는 구조를 확인했다. 키워드가 없으면 `read_keyword_real`이 0.0을 반환한다. 문서에 없는 코드 동작(C)이 맞다. |
| LV1-132 | C | 맞음 | docx p.29, 현재:input.cpp:824–829 | docx p.29는 `for the main channel a boundary condition will have to be provided by the user – and you will be warned if it is not present`이다. 코드는 경계가 없으면 `FREE1`과 `Q_Val=-1`을 자동 설정하고 경고는 `verbose == ON`일 때만 낸다. 문서가 자동 FREE 대체를 적지 않으므로 C가 맞다. |
| LN1-091 | C | 부분 | 현재:cuda/common/helper_cuda.h:68·337, 같은 보고서 LN1-608 | 인용 줄은 정확하다. 그러나 이 매크로들은 NVIDIA SDK 헤더 판별용이다. 최종 문장도 "모델 기능의 누락 정의가 아니다"라고 적어 C(문서가 코드 동작을 생략)의 정의와 맞지 않는다. 외부 SDK 헤더이므로 H가 더 맞다. |
| LB1-356 | C | 맞음 | 현재:cuda/adaptive/classes/SolverParams.h:54 | `grading`을 `read_keyword_bool(..., "grading", 7)`로 읽는다. bridge 문서(4.3.6)에는 이 키워드가 없다. 코드에만 있는 항목(C)으로 수용한다. |
| LG1-141 | C | 맞음 | 현재:metal/fv1/metal_fv1_simulate.mm:1425–1445, grep 결과 | `CalcVirtualGauge` 호출은 iterateq.cpp:301, sgm_fast.cpp:4593, metal_fv1_simulate.mm:1432에만 있다. CPU FV1·DG2와 CUDA 시간 루프에는 없다. 1431–1440의 `discharge = unit_discharge * dx 또는 dy`도 확인했다. |
| LB1-099 | D | 틀림 | bridge p.8, 현재:pars.cpp:438–441 | bridge p.8 원문은 `parameter file keywords touput and qloutput ... output ascii raster grids with file extensions .Tx, .Ty, .QLx and .QLy`이다. 코드에는 `touput`가 없고 `toutput`(save_Ts)이 qloutput 바로 앞에 있다. `touput`는 `toutput`의 철자 오기이므로 B(또는 F)이다. 코드 어디에도 없는 별개 항목처럼 D로 둔 것은 틀렸다. |
| LV1-094 | D | 맞음 | docx p.24, 현재:lisflood.cpp:191, 현재:lisflood.h:755, grep 결과 | docx p.24에 밑줄 삽입 `speedthresh value`, `Default: 10^-9`, `FV1 and DG2 only`가 있다. 코드에서 `speedthresh`는 입력 키워드로 읽히지 않고 내부 필드 `SpeedThresh`(기본 1e-6, lisflood.cpp:191)만 있다. D가 맞다. 문서 기본값 10^-9와 코드 기본값 1e-6의 차이는 이 행에 적혀 있지 않다. |
| LB1-127 | E | 맞음 | bridge p.28, 현재:input.cpp:1969–2117, 현재:boundary.cpp:283·1393·1425 | bridge p.28은 `a warning is output (verbose mode only - see below) and the boundary defaults to zero flux`이다. 코드에서 "bdy names not found" 검사(2084–2107)는 `else`(bdyfilename이 없는 경우, 2080) 안에만 있다. bdy 파일이 있고 이름만 빠지면 `TimeSeries`가 NULL로 남고 `InterpolateTimeSeries`가 NULL을 역참조한다. NULL 처리 코드는 없다. 자기 주석·문서·소비 경로가 일치하므로 E가 맞다. |
| LG1-020 | E | 맞음 | 현재:metal/fv1/metal_fv1_kernels.metal:11·306·648, 현재:metal/fv1/metal_fv1_simulate.mm:291, 현재:swe/fv1.cpp:599 | CFL 건조 판별은 고정 `DEPTH_THRESH 1e-3f`이고 마찰(306)과 호스트 전달(simulate.mm:291)은 입력값을 쓴다. CPU와 CUDA는 입력값을 쓴다. 기본값은 lisflood.cpp:174에서 1e-3이므로 입력값이 기본일 때만 일치한다. E가 맞다. |
| LI1-044 | E | 맞음 | pdf p.16, 현재:pars.cpp:300–323·410–436 | pdf p.16의 세 인용(`Cannot be used in conjunction with sub-grid channels`, `cannot be used in non-adaptive time step model`, `don't use with "adaptoff"`)이 정확하다. 코드는 각 키워드를 읽은 뒤 `return;`하므로 318–323·430–436의 종료 분기는 도달할 수 없다. "Incompatible"은 두 곳에만 있다. E가 맞다. |
| LV1-264 | E | 맞음 | 현재:pars.cpp:300–323·410–436, 현재:source-analysis/lisflood-fp-io-boundary.md:55 | LI1-044와 같은 도달 불가 구조이다. 보고서의 `410–437`은 437행이 주석이라 436이 맞으나 결론에 영향이 없다. 노트 55행의 "exit(1)" 서술과 모순된다. E가 맞다. |
| LI1-141 | E | 부분 | pdf p.21, pdf p.37, 현재:iterateq.cpp:189–201·265, 현재:VersionHistory.h:301–302 | 인용 줄은 정확하다. 그러나 pdf p.37은 `mint_hk ... values over each time step for which the .mass file is written to (massint) instead ... computationally more efficient but less accurate`라고 적고 iterateq.cpp:189 주석도 같은 의도를 적는다. 줄어든 갱신 빈도로 totalHtm이 과소해지는 것은 문서가 밝힌 정확도 희생이다. 이 행은 E 중간보다 약한 후보이거나 C(문서가 총 침수시간 과소 영향을 명시하지 않음)에 가깝다. 강도를 낮추고 문서 근거를 주석에 적어야 한다. |
| LN1-128 | E | 맞음 | 현재:preprocess/generateDG2DEM.cpp:43–45, 현재:input.cpp:1517, 현재:lisflood.cpp:150, ext:v8.2 generateDG2DEM.cpp:43, ext:v8.3 patch:2981–2988 | 8.2의 `Pars pars;`는 `nodata_elevation`을 초기화하지 않고, `LoadDEMData`(input.cpp:1517)가 이를 읽는다. 8.3 패치와 README 38행이 같은 수정을 적는다. E가 맞다. |
| LG1-023 | E | 맞음 | 현재:swe/fv1.cpp:329·526·578, 현재:cuda/cuda_boundary.cu:333–369, 현재:metal/fv1/metal_fv1_kernels.metal:78–86 | CPU `HV_outside = HV_outside;`는 호출자가 0으로 둔 값(329)을 그대로 둔다. HFIX 분기(534)는 `HV_outside = HV_inside`이다. CUDA는 `U_outside`를 접선 성분까지 복사하고 Metal은 `out.Qt = in.Qt;`이다. 독립 구현 둘과 자기 분기가 모순이므로 E가 맞다. |
| LG1-043 | F | 맞음 | 현재:swe/dg2.cpp:826–835·948–994, 현재:swe/dg2/modifiedvars.cpp:401–412, 현재:cuda/dg2/cuda_dg2_solver.cu:153–169 | CPU `U_inc.HU = -(... + 2√3 g H* Zd/dx)`와 CUDA `Sbx.HU = -2√3 g H* Zd/dx`가 같다. 1x항은 CPU `-√3/dx*(... + 2 g H* Zd)`와 CUDA `-2√3 g H* Zd/dx`가 같다. `Zdagger`는 CPU `(neg-pos)/(2√3)`와 CUDA `(e-w)/(2√3)`로 같다. F가 맞다. |
| LG1-044 | F | 맞음 | 현재:swe/dg2.cpp:704–705·749–750, 현재:cuda/dg2/cuda_dg2_solver.cu:391–438 | 1단계는 CPU `Un + dt·L`이고 CUDA는 x 뒤 y를 연쇄해 `Uold + dt(Lx+Ly)`가 된다. 2단계는 CPU `0.5(Un+Uint+dt·L)`이고 CUDA는 `0.5(Uold+Uint+dt·Lx)` 뒤 `+0.5·dt·Ly`로 같다. 두 방향 모두 같은 입력 상태(Uold 또는 Uint)에서 L을 계산한다. F가 맞다. |
| LT1-546 | H | 맞음 | pdf p.45 | 원문 `HORRITT & BATES 2001 ... Predicting floodplain inundation: raster-based modelling versus the finite-element approach. Hydrological Processes, 15, 825-842`이 정확하다. 참고문헌이므로 H가 맞다. |
| LT1-541 | H | 맞음 | pdf p.45 | 원문 `GOUWELEEUW ... 2005. Flood forecasting using medium-range probabilistic weather prediction. Hydrology and Earth System Sciences, 9, 365-380`이 정확하다. H가 맞다. |
| LT1-514 | H | 맞음 | pdf p.43 | 원문 `DANKERS ... 2007. Evaluation of very high-resolution climate model data for simulating flood hazards in the Upper Danube Basin. Journal of Hydrology, 347, 319-331`이 정확하다. H가 맞다. |
| LB1-034 | H | 맞음 | bridge p.16–17 | 쪽 내용은 Hunter 등의 연구 결론(마찰 민감도, 보정 용이성, 침수 범위·도달시간 동시 검증, 격자 축소 시 계산비)이다. 코드로 재현하는 항목이 아니므로 H가 맞다. |

## 집계

| 판정 | 행 수 |
|---|---:|
| 맞음 | 27 |
| 부분 | 3 |
| 틀림 | 5 |
| 합계 | 35 |

## 판정이 갈릴 수 있는 점

- LV1-141, LB1-252, LB1-257은 같은 오류 유형이다. 변경 기록이 없다는 absence 근거로 구판 문서의 기술을 B로 확정했다. 구판 문서(4.3.6·5.9.6)와 8.x 코드는 판이 다르므로, 기록 부재만으로 문서 오기를 증명할 수 없다.
- LG1-081은 H의 정의 해석 문제이다. 정의를 넓게 읽어 "현재 실행 미도달 코드"를 H에 넣을 수 있다면 부분으로 낮출 수 있다.
- LV1-189는 5.9.6 시점의 체크포인트 경로 코드를 확인하지 못했다. 같은 absence 근거를 쓰므로 위 세 행과 같은 위험이 있다. 이 검증은 맞음으로 두었다.
- 쪽 이미지는 모든 인용 문서쪽(pdf p.13·16·21·27·33·37·43·45, docx p.19·22·24·26·29·31·37·40, bridge p.8·16·17·28·42·43)을 열어 확인했다.
- 실행·수치·물리 검증은 하지 않았다.
