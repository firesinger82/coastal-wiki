# ADCIRC 묶음 B — 10-12 결론 검증

검증 기준일은 2026-10-12이다. 작업 시작 시 각 노트의 `git diff -U0 HEAD -- <노트>`에서 파일 헤더를 제외한 `+` 줄을 고정했다. 고정 대상은 906줄이다. 빈 줄 45개를 포함한다. 중복 문장도 출현 위치별로 계산했다. 수정 후 새로 생긴 줄은 이 분모에 다시 넣지 않았다.

각 줄의 문서·코드 인용과 조건·연산자·값·분기를 대조했다. 텍스트 원문은 `nl -ba`로 열었다. `[file=… line=…]` 인용은 해당 원문 줄과도 비교했다. PDF 근거는 제공된 판독 기록의 해당 PDF 쪽을 사용했다. 외부 논문과 태그의 대조에는 `external-results-ad.md`의 T09·N01 원문 판정과 그 접근 한계를 사용했다. 새 외부 원문 조회와 모델 실행은 하지 않았다.

쓰기 대상은 지정 노트와 inputfiles·outputs 보고서의 §5 및 이 기록으로 제한했다. git은 상태·diff 조회와 diff 검증에만 사용했다. 원 코드와 판독 기록은 수정하지 않았다.

`src/`·`prep/`·`wind/`·`docs/`·`thirdparty/`는 `models/ADCIRC/raw/source_code/adcirc/` 아래이다. `raw/`는 `models/ADCIRC/raw/`이다. 아래의 ‘초기 줄’은 고정한 작업 시작 시 줄 번호이다. 노트 링크는 정정 후 대응 위치를 가리킨다.

## 노트별 대조 수

| 노트 | 대상 + 줄 | 비어 있지 않은 줄 | 정정 | 보완 | 이상 없음 |
|---|---:|---:|---:|---:|---:|
| [README.md](/home/firesinger/coastal-wiki/models/ADCIRC/README.md:1) | 13 | 10 | 1 | 2 | 10 |
| [manual-notes/05-input-files-reference.md](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/05-input-files-reference.md:1) | 20 | 20 | 0 | 9 | 11 |
| [manual-notes/06-parameter-definitions.md](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/06-parameter-definitions.md:1) | 5 | 3 | 0 | 0 | 5 |
| [manual-notes/14-fort14-grid-bathymetry-boundaries.md](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:1) | 13 | 11 | 0 | 5 | 8 |
| [manual-notes/16-bathymetry-and-subgrid-paths.md](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:1) | 18 | 18 | 4 | 5 | 9 |
| [manual-notes/17-boundary-and-forcing-inputs.md](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:1) | 13 | 11 | 0 | 4 | 9 |
| [source-analysis/adcirc-bathymetry-input-foundation.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:1) | 29 | 27 | 6 | 7 | 16 |
| [source-analysis/adcirc-fort-files-reference.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:1) | 270 | 267 | 4 | 90 | 176 |
| [source-analysis/adcirc-hotstart.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:1) | 117 | 112 | 37 | 43 | 37 |
| [source-analysis/adcirc-nodal-attributes.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:1) | 80 | 66 | 8 | 9 | 63 |
| [source-analysis/adcirc-output-writers-implementation.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:1) | 275 | 267 | 12 | 116 | 147 |
| [source-analysis/adcirc-parameter-glossary-v1.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:1) | 5 | 3 | 0 | 0 | 5 |
| [source-analysis/adcirc-preprocessing-foundation.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:1) | 14 | 14 | 0 | 10 | 4 |
| [source-analysis/adcirc-topic-map.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-topic-map.md:1) | 34 | 32 | 3 | 4 | 27 |
| 합계 | 906 | 861 | 75 | 304 | 527 |

정정·보완·이상 없음은 초기 + 줄을 나눈 상호 배타적인 수이다. 정정과 보완이 겹친 줄은 정정으로 셌다. 보완에는 중복 문단의 정본 앵커와 링크 정리가 포함된다. 분류 변경은 이 줄 수와 다른 단위인 기존 보고서 행 ID 수이다.

## 주요 정정과 새 후보

- 보조 프로그램을 포함한 검색에서 ASGS의 `tau0_gen.f90`와 adcircpy의 재구현을 확인했다. 구현 부재 D를 철회했다. 문서가 생략한 등호 조건을 C로 기록했다.
- 외부 subgrid 생성 도구와 경험식·수심·검증 사례의 권고는 H로 고쳤다. ADCIRC 본체의 subgrid 읽기는 C로 유지했다.
- 핫스타트의 2차원·3차원 배열 순서에 붙인 A를 B로 통일했다. 함수 추가 주석은 저장 순서의 판 변경 근거로 사용하지 않았다.
- netCDF 노드 변수의 근거를 case 63·64·73으로 바꿨다. pressure 정의를 추가했다. XDMF 최종화는 `min(nt-it, nt-endTimeStep)`의 계산 구조로 E를 유지했다. NP와 NP_G의 실제 차이는 조건부 미확인으로 남겼다.
- subgrid 길이 단위는 `eta2(i).LT.wetFracVertTab(i,j)`의 사용 줄로 입증했다. 동적 수위 보정 램프의 두 기본값 `0.d0`을 추가했다.
- 문서가 가리키지 못하는 절 번호를 행 ID나 정본 링크로 바꿨다. 동일 근거와 판정 문단은 정본에 남겼다.

| 신규 ID | 별도 E 후보 | 기존 판정 | 정본 |
|---|---|---|---|
| CVB-BATH-TIME | 시변 수심의 시간 단위 비교 | BATH-04·05·06의 C 유지 | [조건과 식](../../../models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md#cvb-bath-time) |
| CVB-XDMF-PIPE | XDMF 관 경계의 배열 선택 | XDMF-02의 C 유지 | [조건과 식](../../../models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md#cvb-xdmf-pipe) |
| CVB-HS-SWAN | 직렬 netCDF 핫스타트의 SWAN 변수 ID | HSNC-04의 C 유지 | [조건과 식](../../../models/ADCIRC/source-analysis/adcirc-hotstart.md#cvb-hs-swan) |
| CVB-HS-LOCAL | 지역 3차원 binary 핫스타트의 출력 플래그 | D51의 배열 배치 B와 별도 | [조건과 식](../../../models/ADCIRC/source-analysis/adcirc-hotstart.md#cvb-hs-local) |
| CVB-WIND7-UNITS | NWS=±7 netCDF 출력의 풍속 단위 속성 | D12·D29의 B 유지 | [조건과 식](../../../models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md#cvb-wind7-units) |

신규 E 5개는 기존 행의 분류 변경 52개에 합산하지 않았다. inputfiles §5에는 신규 E 4개를 별도 표로 추가했다. outputs §5에는 신규 E 1개를 별도 표로 추가했다.

## 분류를 바꾼 행

| 보고서 행 ID | 개수 | 이전 → 새 | 이유 | 보고서 반영 |
|---|---:|---|---|---|
| ADCIRC-outputs-vs-code.md §5 L1079–L1084 | 6 | A → B | 저장 순서의 판 변경 근거 부재 | §5 수정 완료 |
| ADCIRC-outputs-vs-code.md §5 L1112–L1126, L1194–L1208 | 30 | A → B | 배열 저장 루프는 과거 판의 변경 이력을 입증하지 않음 | §5 수정 완료 |
| ADCIRC-features-vs-code.md §5 P06, P07, P15 | 3 | D → H | 경험식 적용 조건·실무 권고 | 노트 수정 완료. 보고서는 쓰기 허용 범위 밖. |
| ADCIRC-features-vs-code.md §5 T02, T03 | 2 | D → H | 적용 수심·강제력 권고 | 노트 수정 완료. 보고서는 쓰기 허용 범위 밖. |
| ADCIRC-features-vs-code.md §5 G01–G07 | 7 | D → H | 외부 생성 도구의 알고리즘 | 노트 수정 완료. 보고서는 쓰기 허용 범위 밖. |
| ADCIRC-features-vs-code.md §5 기존 §5 732줄 | 1 | D → H | 역사적 검증 사례·성능 | 노트 수정 완료. 보고서는 쓰기 허용 범위 밖. |
| ADCIRC-features-vs-code.md §5 기존 §5 733줄 | 1 | D → H | 외부 subgrid 생성 도구 | 노트 수정 완료. 보고서는 쓰기 허용 범위 밖. |
| ADCIRC-features-vs-code.md §5 T09 | 1 | D+C → C | 문서에 생성식이 없는 것은 C | 노트 수정 완료. 보고서는 쓰기 허용 범위 밖. |
| ADCIRC-fort15-vs-code.md §5 U01 (L876) | 1 | D → C | ASGS 구현 존재; 문서는 등호 조건을 생략 | 노트 수정 완료. 보고서는 쓰기 허용 범위 밖. |

outputs 보고서의 기존 820개 ID 집계는 A 33, B 107, C 642, D 2, E 35, F 1, G 0, H 0, X 0이다. A에서 B로 바꾼 ID는 36개이다. 쓰기 범위 밖 보고서에 대응하는 노트의 변경 ID는 16개이다. 해당 features·fort15 보고서는 수정하지 않았다. 이들 보고서의 이전 D 또는 복합 분류보다 이번 노트 정정을 우선해 읽어야 한다.

## D 전 줄의 raw 전체 재검색

검색 명령은 `rg -n -i --hidden --no-ignore -g '!**/.git/**' '<식>' models/ADCIRC/raw`이다. raw가 git 무시 대상이므로 `--no-ignore`를 사용했다. 아래 일치 수는 문서·데이터·보조 프로그램을 포함한 전체 텍스트 검색 결과의 줄 수이다. 코드 구현 수로 해석하지 않는다.

| 대상 초기 줄·행 ID | 검색식 | 일치 줄 | 결과와 결론 |
|---|---|---:|---|
| manual05:33 · F10-04 | `fort[._ ]?10\|\bNVN\b\|\bNVP\b\|\bNHNN\b\|\bNVNN\b` | 1099 | prep/prep.F:125–132의 3D 분할 reader를 포함해 확인했다. 모델의 read_input.F:3138–3148 경로와 구분했다. 모델 3D 읽기의 D를 유지했다. |
| manual14:33, fort-files:257 · F14-12 | `IBTYPEE` | 155 | ASGS PERL/AdcGrid.pm:262의 읽기를 확인했다. 모델 mesh.F:418은 NVDLL만 읽는다. D의 범위를 모델 ASCII reader로 한정했다. |
| bathymetry:117, topic-map:74 · G01–G07·기존 §5 733줄 | `SubgridADCIRCUtility\|cmfVertex\|cfVertex\|wetFractionVertex` | 7 | 외부 Python 도구 링크와 subgridLookup.F의 세 변수 읽기만 일치했다. 생성 알고리즘은 확인하지 못했다. 외부 도구 동작은 H로 바꿨다. |
| nodal:92 · NA-38 | `ESLNodes\|ESLDescript\|ESLCOUNT` | 119 | ASGS output/asgsio.f90:612–615,1526–1529의 출력 분류·변환을 확인했다. 본체 핫스타트 복원은 찾지 못했다. D를 유지했다. |
| nodal:104 · P06·P07·P15 | `Yarnell\|Henderson\|three rows\|BridgePilings\|BALPHA` | 382 | 교각 입력 소비와 역사적 권고를 구분했다. 권고의 유효성을 코드로 판단하지 않으므로 H로 바꿨다. |
| nodal:157 · T02·T03 | `internal_tide_friction\|deep ocean\|100-500` | 162 | 속성 소비식과 시험 입력을 확인했다. 권고 수심·강제력은 자동 허용 문턱이 아니다. H로 바꿨다. |
| topic-map:62 · C42 | `DG_HYDRO_TIMESTEP\|MODULE DG\b\|dg_integration\|dg\.f90` | 0 | 별도 DG 구현 식별자 일치는 없다. 공백을 허용한 MODULE 검색도 0개였다. D는 로컬 사본의 구현 부재에 한정했다. |
| topic-map:73 · 기존 §5 732줄 | `tests showed\|generalized to all\|Preliminary evaluation\|subcritical` | 196 | 원문의 사례·제한과 testsuite 목적을 구분했다. 검증 성능을 정적 코드로 재현 판정하지 않으므로 H로 바꿨다. |
| fort-files:449 · L761 | `\bWRAMP\b` | 1 | nws_parameters.rst:309 한 곳이다. 코드 구현 일치는 없다. D를 유지했다. |
| fort-files:454 · U01(L876) | `tau0_gen\|\b1750\b` | 2102 | ASGS tau0_gen.f90:94–106과 adcircpy/mesh/mesh.py:167–202에 구현이 있다. D를 철회했다. 문서의 등호 조건 누락을 C로 기록했다. |
| outputs:460·462 · L135·L136 | `\bNOUTGC\b` | 242 | 보조 도구의 입력 생성·형식 검사도 확인했다. 본체 read_input.F:4310–4320의 허용값은 0과 ±1이다. 현재 모델 입력 범위의 D를 유지했다. |
| nodal:168 · T09의 D+C | `IT_Fric\|Pringle\|Nycander\|internal_tide_friction` | 369 | 본체 소비식과 ASGS 속성 등록·설정을 확인했다. J·Green 함수·필터 길이의 생성식은 찾지 못했다. ‘문서에 식이 없음’의 분류는 C로 고쳤다. 입력 정규화의 실제 생성값은 확인하지 않았다. |

## E의 반대 근거와 보정 경로 확인

아래의 경로 확인은 해당 + 줄이 주장한 조건에 한정한다. 독립 SWAN과 XDMF 라이브러리 내부를 모델 완료 조건으로 삼지 않았다.

| 후보 | 확인한 반대 근거·보정 가능 경로 | 판정 |
|---|---|---|
| ROT-04 | mesh.F:104의 단위행렬 초기화가 있다. rotation_matrix 입력은 :4406에서 셋째 열만 채운다. :4559–4565의 소비 전에 행 전체를 다시 읽는 경로는 찾지 못했다. | E 유지 |
| F14-21·F14-30·F14-32 | boundaries.F:353과 mesh.F:446의 CASE 목록을 대조했다. read_global.F:253의 관 경계 n2 매핑은 :239의 4·24·64 입력을 고치지 않는다. decomp.F:599와 prep.F:1347은 IBCONNR를 그대로 인덱스로 소비한다. | 조건부 E 유지 |
| NA-18 | FoundEVC의 false 초기화 :467과 종료 조건 :936을 확인했다. true 대입은 XDMF 분기 :688뿐이었다. ASCII 헤더 :1277–1280에는 대입이 없다. | E 유지. 주석 대신 사용 줄로 보완 |
| NA-35·NA-37 | nodalattr.F:255의 기본값 배열은 3개이다. :1322는 파일의 IT_FricNoOfVals까지 읽는다. :2651·2661의 5성분 소비가 기본값 배열을 확장하지 않는다. | 5성분 ASCII 조건의 E 유지 |
| MET-47 | prep.F:3415에는 고정 폭 READ가 주석으로 남아 있다. 활성 :3416은 list-directed이다. ghost node 변경 주석은 wind.F:3400의 고정 폭 reader와 입력 허용 범위를 같게 만들지 않는다. | E 유지 |
| F200-06·F200-07 | io.F90:100–101은 FORM을 지정하지 않는다. wind.F:4195–4196은 unformatted READ이다. 압력 변환의 의도 주석 :4209와 실제 :4165·4228 및 다른 NWS의 :3411을 비교했다. | 문서의 mbar 입력 조건에서 E 유지 |
| WEIR-06·SCH-03 | weir_boundary.F90:1147–1154의 기본값 대입은 :1133–1143의 존재 검사 뒤이다. 일반 경로 :1439–1444는 TimeEndSec를 쓰지만 schedule 경로 :1382–1386은 TimeStartSec를 쓴다. | E 유지 |
| fort15 L518–L521 | read_input.F:563–586의 TVW 상속 뒤에 위치 입력의 NOUTGE·TOUTSGE·TOUTFGE·NSPOOLGE 읽기가 있다. raw 검색에서 이후의 재상속 대입은 찾지 못했다. | E 유지 |
| fort15 L141·L343·L346·L348 | NWS=29의 READ 목록과 CICE_TIMINC 소비를 대조했다. -19의 양수 전용 경로와 ABS 경로를 구분했다. NCICE 검사의 양수 비교와 -2·-7 경로를 대조했다. | 원문에 적힌 조합의 E 유지 |
| fort15 L498 | subdomainOn 선언과 namelist 실패 경로를 검색했다. ASGS·prep 입력 생성과 모델의 명시적 기본값 대입을 구분했다. finit-logical·finit-local-zero 보정은 찾지 못했다. | 정의 전 사용의 E 유지 |
| fort15 L759 | ASGS의 03-DEBUG_WARN_ELEV.patch도 읽었다. 현재 read_input.F:830의 변환은 legacy 정수 READ :991보다 앞이다. namelist의 논리값 직접 입력은 별도 경로이다. | E 유지 |
| D05·D38 | globalio.F의 ASCII 식별자는 mesh labels이다. 관측소 합치기의 식별자와 NOFF의 요소 매핑을 대조했다. write_output.F:697의 NP_G 할당은 요소 수를 보장하지 않는다. | 해당 수·라벨이 다른 조건의 E 유지 |
| D10 | write_output.F:1191·1222의 divideByDepth 플래그를 확인했다. :2080의 나눗셈은 관측소 보간 경로이다. globalio의 전역 storeOne에는 대응 나눗셈이 없다. | E 유지 |
| D17·D21 | POST41의 NVar별 할당과 post.F:4338의 고정 두 원소를 대조했다. cstart.F:1036–1043의 IDEN별 재대입은 음수 IDEN에서 실행되지 않는다. | 분기 조건을 유지한 E |
| D32·D35·D37 | everDried_time의 -99999 초기화와 DTDP 누적을 대조했다. 핫스타트의 기존 값 읽기는 최초 실행의 오프셋을 고치지 않는다. 반복 출력 헤더 갱신과 endrisinginun의 ASCII 헤더 쓰기 경로는 찾지 못했다. | E 유지 |
| D39·D40·D41·D44 | 누적 배열·기준면 계산과 netCDF의 units·long_name·positive 속성을 각각 비교했다. 속성 helper는 값을 변환하지 않는다. | 메타데이터 E 유지 |
| D47 | weir_dz의 node 단일 차원과 시계열 start/count 전달을 대조했다. 라이브러리의 실제 오류나 파일 결과는 판정하지 않았다. | 정적 모순의 E 유지 |
| D60·D66 | putUnitsAttribute의 G 분기는 문자열만 바꾼다(netcdfio.F90:10444–10460). raw 전체 Fahrenheit·온도 변환 검색에서 세 속성 문자열만 코드에 일치했다. English Cartesian 길이와 3D scalar 입력을 별도로 구분했다. | 조건부 메타데이터 E 유지 |
| D63·D65·L1499 | POSTHOT 쓰기 종료와 RS·조화 상태 위치를 대조했다. POST71·91·43의 지역 헤더 수와 전역 반복 상한을 대조했다. DUU의 MNP 할당과 np_g 길이는 NP_G>MNP 조건의 후보로 유지했다. | 조건부 E 유지 |
| L593·L594·L595·L1504 | 응력/물 기준 밀도의 차원은 L² T⁻²이다. u 속성의 두 번 대입은 v 출력 호출로 보정되지 않는다. NCICE=14·17의 100배 값과 iceaf 저장 사이에서 재정규화를 찾지 못했다. | 범위를 한정한 E 유지 |
| P13·P14·C14 | 교각의 2D·3D Fr 정의와 식을 대조했다. 구판 PDF의 Fr² 정의를 확인했다. 두 코드 분기의 반복은 추가 제곱을 해소하지 않는다. | E 유지 |
| L952·L1501 | raw 전체 finalizeOutputFileXDMF 검색에서 호출은 xdmfio.F:340 하나였다. 출력 창을 제한하는 write_output.F:1861–1862와 min 식을 비교했다. NP와 NP_G의 런타임 차이는 확인하지 않았다. | 최종화 E 유지. 병렬 크기는 조건부 미확인 |
| L1192 | writer.F:674–675의 AND count와 :683–685의 OR 기록 조건을 비교했다. 같은 배열 마스크를 사용한다. 주석을 독립 근거로 세지 않았다. | E 유지 |

신규 E 5개의 반대 근거 확인은 위 정본 링크와 두 보고서 §5.1에 기록했다.

## sonnet 수정 목록의 반영 여부

| 번호 | 반영 여부 | 위치·판정 |
|---:|---|---|
| 1 | 코드 존재 재확인. B + 줄에 해당 행 없음. | wind/p15.F:1482–1520의 BLOWUQ와 work/makefile:249–250,453을 확인했다. 자체 해법 부재 D는 근거가 없다. Blain 원문 식 대응과 ADCIRC-theory-vs-code.md §5 수정은 이번 노트 집합·허용 보고서 범위 밖이다. |
| 2 | 대상 밖 | EFDC ISVARSETTLE 행은 이번 ADCIRC 묶음에 없다. |
| 3 | 반영 | CVB-BATH-TIME을 추가했다. 시변 수심 입력 규칙의 C는 유지했다. |
| 4 | 인용 위치 재확인. B + 줄에 해당 행 없음. | adcirc_theory_2004_12_08.pdf/p001-018.md:27이 PDF p.15의 Duv 정의이다. :15는 해당 정의의 근거가 아니다. 이 묶음의 추가 줄에는 잘못된 Duv 인용이 없었다. |
| 5 | 대상 밖 | EFDC 식 5.13 행은 이번 ADCIRC 묶음에 없다. |
| 6 | 반영 | outputs 노트 초기552줄과 outputs §5 L636 등 묶음의 근거를 nodal case63·64·73으로 교체했다. pressure :2285를 포함했다. |
| 7 | 반영 | outputs 노트 초기563줄과 outputs §5 L952·L1501을 고쳤다. 자기 주석 대신 실제 min 식을 사용했다. np 대 np_g는 조건부 미확인이다. |
| 8 | 대상 밖 | EFDC TOXS/DYES 행은 이번 ADCIRC 묶음에 없다. |
| 9 | 반영 | bathymetry 초기116줄과 중복 SG 행 및 inputfiles §5 U-03에서 :67 주석을 제외했다. subgridLookup.F:375 비교식을 사용했다. |
| 10 | 반영 | topic-map 초기60줄에 wind.F:243–244의 두 0.d0 기본값을 추가했다. |
| 11 | 해당 SFINCS 행은 대상 밖. 같은 오류 유형은 반영. | ADCIRC의 SG·XDMF·binary 핫스타트·출력 결론 중복을 정본과 링크로 줄였다. |
| 12 | 반영 | 2.7·2.12·2.14의 고립된 지시어를 삭제하거나 보고서 행 ID·노트 링크로 교체했다. |
| 13 | 대상 밖 | EFDC mhkpwr.f90 행은 이번 ADCIRC 묶음에 없다. |

## 정정·보완 목록

각 행은 초기 + 줄 하나에 대응한다. ‘새 요지’가 정본 지정 또는 링크 축약인 행은 사실 판정을 바꾼 행과 구별한다. 한 줄에서 여러 조치를 한 경우 같은 행에 적었다.

| 노트:초기 줄 | 구분 | 이전 요지 | 새 요지 | 근거 |
|---|---|---|---|---|
| [README.md:43](/home/firesinger/coastal-wiki/models/ADCIRC/README.md:43) | 정정 | `manual-notes/` | 같은 노트의 B 확정과 충돌하는 가능성 표현 정리 | _staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_modifications_for_ice.pdf/p001-010.md:14–15; src/wind.F:761–763 |
| [README.md:47](/home/firesinger/coastal-wiki/models/ADCIRC/README.md:47) | 보완 | ICE-10 기본 얼음 drag 공식 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 ICE-10 |
| [README.md:48](/home/firesinger/coastal-wiki/models/ADCIRC/README.md:48) | 보완 | ICE-11 IceCube의 IC=0 수치·IC 정의 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 ICE-11 |
| [manual-notes/05-input-files-reference.md:33](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/05-input-files-reference.md:33) | 보완 | F10-04 3D NVN,NVP; NHNN,NVNN,CONC | D 판정의 전체 raw 검색 결과와 본체·보조 도구 범위 명시 | F10-04 |
| [manual-notes/05-input-files-reference.md:34](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/05-input-files-reference.md:34) | 보완 | F11-08 2DDI 둘째 헤더 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 F11-08 |
| [manual-notes/05-input-files-reference.md:35](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/05-input-files-reference.md:35) | 보완 | F11NC-01 파일 이름·time·strlen·날짜 문자열 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 F11-11, F11NC-01, F11NC-02, F11NC-03 |
| [manual-notes/05-input-files-reference.md:36](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/05-input-files-reference.md:36) | 보완 | F11NC-02 격자 차원·좌표 | 중복 근거·판정을 models/ADCIRC/manual-notes/05-input-files-reference.md:35 정본 링크로 축약 | models/ADCIRC/manual-notes/05-input-files-reference.md:35 |
| [manual-notes/05-input-files-reference.md:37](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/05-input-files-reference.md:37) | 보완 | F11NC-03 BPGX·BPGY·SigTS·NB·NM·MLD·CDisp·DispX·DispY 조건 | 중복 근거·판정을 models/ADCIRC/manual-notes/05-input-files-reference.md:35 정본 링크로 축약 | models/ADCIRC/manual-notes/05-input-files-reference.md:35 |
| [manual-notes/05-input-files-reference.md:41](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/05-input-files-reference.md:41) | 보완 | ROT-04 rotation_matrix: 3×3 행렬 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 ROT-04 |
| [manual-notes/05-input-files-reference.md:46](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/05-input-files-reference.md:46) | 보완 | STA-05 세 번째 필드: 관측점 이름 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 STA-05 |
| [manual-notes/05-input-files-reference.md:47](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/05-input-files-reference.md:47) | 보완 | FORT36-01 fort36: 사용 조건 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 FORT36-01, FORT37-01 |
| [manual-notes/05-input-files-reference.md:48](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/05-input-files-reference.md:48) | 보완 | FORT37-01 fort37: 사용 조건 | 중복 근거·판정을 models/ADCIRC/manual-notes/05-input-files-reference.md:47 정본 링크로 축약 | models/ADCIRC/manual-notes/05-input-files-reference.md:47 |
| [manual-notes/14-fort14-grid-bathymetry-boundaries.md:33](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:33) | 보완 | F14-12 IBTYPEE | D 판정의 전체 raw 검색 결과와 본체·보조 도구 범위 명시 / 중복 설명의 정본 앵커 지정 | F14-12; ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 F14-12 |
| [manual-notes/14-fort14-grid-bathymetry-boundaries.md:35](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:35) | 보완 | F14-28 장벽 높이의 허용 등호 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 F14-28, F14-29 |
| [manual-notes/14-fort14-grid-bathymetry-boundaries.md:36](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:36) | 보완 | F14-29 내부 장벽 뒷면의 지형고 검사 | 중복 근거·판정을 models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:35 정본 링크로 축약 | models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:35 |
| [manual-notes/14-fort14-grid-bathymetry-boundaries.md:37](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:37) | 보완 | F14-30 IBTYPE=102·112·122: 읽기와 할당의 차이 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 F14-30 |
| [manual-notes/14-fort14-grid-bathymetry-boundaries.md:39](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:39) | 보완 | F14-32 IBTYPE=4·24·64의 IBCONN 라벨 처리 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 F14-32 |
| [manual-notes/16-bathymetry-and-subgrid-paths.md:33](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:33) | 보완 | BATH-01 NDDT 설정 위치·사용 조건 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:67 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:67 |
| [manual-notes/16-bathymetry-and-subgrid-paths.md:36](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:36) | 보완 | BATH-04 NDDT=±2: 고정 형식·-99999 sentinel | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:70 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:70 |
| [manual-notes/16-bathymetry-and-subgrid-paths.md:37](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:37) | 보완 | BATH-05 시작 프레임·생략 노드 유지·부호별 시간 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:70 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:70 |
| [manual-notes/16-bathymetry-and-subgrid-paths.md:44](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:44) | 정정 | SG-01 lookup netCDF: numNode·numPhi·phiSet | subgrid 단위 근거에서 주석 67을 제외하고 ETA2 비교 375를 사용 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:86 정본 링크로 축약 | src/subgridLookup.F:375,410–416; models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:86 |
| [manual-notes/16-bathymetry-and-subgrid-paths.md:45](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:45) | 정정 | SG-02 cmfVertex·cfVertex·cadvVertex | subgrid 단위 근거에서 주석 67을 제외하고 ETA2 비교 375를 사용 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:86 정본 링크로 축약 | src/subgridLookup.F:375,410–416; models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:86 |
| [manual-notes/16-bathymetry-and-subgrid-paths.md:46](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:46) | 정정 | SG-03 gridTotWatDepthVertex·wetTotWatDepthVertex·wetFractionVertex·binaryVertexList | subgrid 단위 근거에서 주석 67을 제외하고 ETA2 비교 375를 사용 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:86 정본 링크로 축약 | src/subgridLookup.F:375,410–416; models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:86 |
| [manual-notes/16-bathymetry-and-subgrid-paths.md:52](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:52) | 보완 | XDMF-01 격자 파일의 geometry·depth·topology | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:104 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:104 |
| [manual-notes/16-bathymetry-and-subgrid-paths.md:53](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:53) | 보완 | XDMF-02 boundary Set·Information·property·Attribute | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:104 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:104 |
| [manual-notes/16-bathymetry-and-subgrid-paths.md:54](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:54) | 정정 | XDMF-03 노드 속성의 units·number_of_values·default_values·배열 | 노트 안에 없는 2.7·2.14 지시어 교체 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:104 정본 링크로 축약 | inputfiles §5 XDMF-03; models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:104 |
| [manual-notes/17-boundary-and-forcing-inputs.md:34](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:34) | 보완 | F19-01 fort.19 읽기 조건 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 F19-01 |
| [manual-notes/17-boundary-and-forcing-inputs.md:35](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:35) | 보완 | F19-05 ETIMINC 반복 여부 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 F19-05, F20-06 |
| [manual-notes/17-boundary-and-forcing-inputs.md:41](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:41) | 보완 | F20-01 읽기 조건 NFFR | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 F20-01 |
| [manual-notes/17-boundary-and-forcing-inputs.md:42](/home/firesinger/coastal-wiki/models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:42) | 보완 | F20-06 FTIMINC 반복 여부 | 중복 근거·판정을 models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:35 정본 링크로 축약 | models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:35 |
| [source-analysis/adcirc-bathymetry-input-foundation.md:67](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:67) | 보완 | BATH-01 NDDT 설정 위치·사용 조건 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 BATH-01 |
| [source-analysis/adcirc-bathymetry-input-foundation.md:70](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:70) | 보완 | BATH-04 NDDT=±2: 고정 형식·-99999 sentinel | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 BATH-04, BATH-05, BATH-06 |
| [source-analysis/adcirc-bathymetry-input-foundation.md:71](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:71) | 보완 | BATH-05 시작 프레임·생략 노드 유지·부호별 시간 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:70 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:70 |
| [source-analysis/adcirc-bathymetry-input-foundation.md:86](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:86) | 정정 | SG-01 lookup netCDF: numNode·numPhi·phiSet | subgrid 단위 근거에서 주석 67을 제외하고 ETA2 비교 375를 사용 / 중복 설명의 정본 앵커 지정 | src/subgridLookup.F:375,410–416; ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 SG-01, SG-02, SG-03 |
| [source-analysis/adcirc-bathymetry-input-foundation.md:87](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:87) | 정정 | SG-02 cmfVertex·cfVertex·cadvVertex | subgrid 단위 근거에서 주석 67을 제외하고 ETA2 비교 375를 사용 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:86 정본 링크로 축약 | src/subgridLookup.F:375,410–416; models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:86 |
| [source-analysis/adcirc-bathymetry-input-foundation.md:88](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:88) | 정정 | SG-03 gridTotWatDepthVertex·wetTotWatDepthVertex·wetFractionVertex·binaryVertexList | subgrid 단위 근거에서 주석 67을 제외하고 ETA2 비교 375를 사용 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:86 정본 링크로 축약 | src/subgridLookup.F:375,410–416; models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:86 |
| [source-analysis/adcirc-bathymetry-input-foundation.md:94](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:94) | 보완 | K74 subgrid | 중복 설명의 정본 앵커 지정 | ADCIRC-features-vs-code.md#5-차이-결론\|features 보고서 §5 K74 (638줄)<br>C43 (692줄) |
| [source-analysis/adcirc-bathymetry-input-foundation.md:104](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:104) | 보완 | XDMF-01 격자 파일의 geometry·depth·topology | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 XDMF-01, XDMF-02, XDMF-03 |
| [source-analysis/adcirc-bathymetry-input-foundation.md:105](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:105) | 보완 | XDMF-02 boundary Set·Information·property·Attribute | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:104 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:104 |
| [source-analysis/adcirc-bathymetry-input-foundation.md:106](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:106) | 정정 | XDMF-03 노드 속성의 units·number_of_values·default_values·배열 | 노트 안에 없는 2.7·2.14 지시어 교체 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:104 정본 링크로 축약 | inputfiles §5 XDMF-03; models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:104 |
| [source-analysis/adcirc-bathymetry-input-foundation.md:116](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:116) | 정정 | subgrid 값의 의미·차원 | subgrid 단위 근거에서 주석 67을 제외하고 ETA2 비교 375를 사용 | src/subgridLookup.F:375,410–416 |
| [source-analysis/adcirc-bathymetry-input-foundation.md:117](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:117) | 정정 | 외부 subgrid 표 생성 기능 | G01–G07 외부 생성 도구 D→H; 전체 raw 검색 보완 / 중복 문단의 정본 앵커 지정 | docs/tools/subgrid_adcirc_utility.rst:6–18; src/subgridLookup.F:193–204,232,243,301,375; models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:117 |
| [source-analysis/adcirc-bathymetry-input-foundation.md:118](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:118) | 보완 | 빈 줄 | CVB-BATH-TIME 신규 E 후보; 기존 결론과 분리 / CVB-XDMF-PIPE 신규 E 후보; 기존 결론과 분리 | src/wetdry.F:841–845; src/timestep.F:473–494; src/hstart.F:1244–1258; src/mesh.F:507–525,1240–1301; src/boundaries.F:364–383 |
| [source-analysis/adcirc-fort-files-reference.md:44](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:44) | 보완 | ROT-04 rotation_matrix: 3×3 행렬 | 중복 근거·판정을 models/ADCIRC/manual-notes/05-input-files-reference.md:41 정본 링크로 축약 | models/ADCIRC/manual-notes/05-input-files-reference.md:41 |
| [source-analysis/adcirc-fort-files-reference.md:49](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:49) | 보완 | STA-05 세 번째 필드: 관측점 이름 | 중복 근거·판정을 models/ADCIRC/manual-notes/05-input-files-reference.md:46 정본 링크로 축약 | models/ADCIRC/manual-notes/05-input-files-reference.md:46 |
| [source-analysis/adcirc-fort-files-reference.md:197](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:197) | 보완 | NC13-02 NWS=±13의 입력 종류 설명 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 NC13-02 |
| [source-analysis/adcirc-fort-files-reference.md:198](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:198) | 보완 | NC13-08 time: 날짜 문자열 접두사 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 NC13-08 |
| [source-analysis/adcirc-fort-files-reference.md:199](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:199) | 보완 | NC13-12 -I 경로 예외 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 MET-32, F200-10, NC13-12, NC14-12 |
| [source-analysis/adcirc-fort-files-reference.md:210](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:210) | 보완 | MET-02 NWS=2: WTIMINC 레코드 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 MET-02 |
| [source-analysis/adcirc-fort-files-reference.md:211](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:211) | 보완 | MET-05 NWS=3의 좌표계 의무 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 MET-05 |
| [source-analysis/adcirc-fort-files-reference.md:212](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:212) | 보완 | MET-07 NWS=±4: PRN의 단위 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 MET-07 |
| [source-analysis/adcirc-fort-files-reference.md:213](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:213) | 보완 | MET-09 NWS=6: 날짜·시각 여섯 필드 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 MET-09 |
| [source-analysis/adcirc-fort-files-reference.md:214](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:214) | 보완 | MET-41 NWS=±7의 WVXFN·WVYFN 단위 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 MET-41 |
| [source-analysis/adcirc-fort-files-reference.md:215](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:215) | 보완 | MET-47 NWS=±4의 prep 입력: list-directed | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 MET-47 |
| [source-analysis/adcirc-fort-files-reference.md:216](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:216) | 보완 | MET-32 NWS=15·16: 입력 디렉터리 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:199 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:199 |
| [source-analysis/adcirc-fort-files-reference.md:217](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:217) | 보완 | MET-34 NWS=15: HWind 격자 간격 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 MET-34 |
| [source-analysis/adcirc-fort-files-reference.md:218](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:218) | 보완 | MET-38 NWS=16: 예제의 Pc 열 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 MET-38 |
| [source-analysis/adcirc-fort-files-reference.md:219](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:219) | 보완 | MET-42 NWS=16: NCELLS의 형식 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 MET-42, MET-44 |
| [source-analysis/adcirc-fort-files-reference.md:220](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:220) | 보완 | F200-05 NWS=11: UE·VE·PE의 저장 순서 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 F200-05 |
| [source-analysis/adcirc-fort-files-reference.md:221](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:221) | 보완 | F200-06 NWS=11: binary OPEN의 FORM | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 F200-06 |
| [source-analysis/adcirc-fort-files-reference.md:222](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:222) | 보완 | F200-07 NWS=11: 기압 단위 주장 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 F200-07 |
| [source-analysis/adcirc-fort-files-reference.md:223](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:223) | 보완 | F200-09 NWS=11: WTIMINC당 dataset 수 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 F200-09 |
| [source-analysis/adcirc-fort-files-reference.md:224](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:224) | 보완 | F200-10 NWS=11: -I 입력 경로 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:199 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:199 |
| [source-analysis/adcirc-fort-files-reference.md:239](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:239) | 보완 | fort.15 / ` NOUTE ` | 중복 설명의 정본 앵커 지정 | ADCIRC-fort15-vs-code.md#5-차이-결론\|fort15 보고서 §5 L180, L187, L201, L208, L212, L220, L293, L300, L307, L314, L318, L322, C07 (L845) |
| [source-analysis/adcirc-fort-files-reference.md:240](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:240) | 보완 | fort.15 / ` I3DSD ` | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:239 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:239 |
| [source-analysis/adcirc-fort-files-reference.md:242](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:242) | 보완 | fort.15 / ` BCSTATIM ` | 중복 설명의 정본 앵커 지정 | ADCIRC-fort15-vs-code.md#5-차이-결론\|fort15 보고서 §5 L276, L278, L280, L282 |
| [source-analysis/adcirc-fort-files-reference.md:243](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:243) | 보완 | fort.15 / ` SBCSTATIM ` | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:242 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:242 |
| [source-analysis/adcirc-fort-files-reference.md:244](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:244) | 보완 | fort.15 / ` TBCSTATIM ` | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:242 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:242 |
| [source-analysis/adcirc-fort-files-reference.md:245](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:245) | 보완 | fort.15 / ` TTBCSTATIM ` | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:242 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:242 |
| [source-analysis/adcirc-fort-files-reference.md:249](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:249) | 보완 | fort.15 / ` TVWControl.NOUT_TVW ` | 중복 설명의 정본 앵커 지정 | ADCIRC-fort15-vs-code.md#5-차이-결론\|fort15 보고서 §5 L518, L519, L520, L521 |
| [source-analysis/adcirc-fort-files-reference.md:250](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:250) | 보완 | fort.15 / ` TVWControl.TOUTS_TVW ` | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:249 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:249 |
| [source-analysis/adcirc-fort-files-reference.md:251](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:251) | 보완 | fort.15 / ` TVWControl.TOUTF_TVW ` | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:249 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:249 |
| [source-analysis/adcirc-fort-files-reference.md:252](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:252) | 보완 | fort.15 / ` TVWControl.NSPOOL_TVW ` | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:249 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:249 |
| [source-analysis/adcirc-fort-files-reference.md:257](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:257) | 보완 | F14-12 / IBTYPEE | 중복 근거·판정을 models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:33 정본 링크로 축약 | models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:33 |
| [source-analysis/adcirc-fort-files-reference.md:258](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:258) | 보완 | F14-28 / 장벽 높이의 허용 등호 | 중복 근거·판정을 models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:35 정본 링크로 축약 | models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:35 |
| [source-analysis/adcirc-fort-files-reference.md:259](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:259) | 보완 | F14-29 / 내부 장벽 뒷면의 지형고 검사 | 중복 근거·판정을 models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:35 정본 링크로 축약 | models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:35 |
| [source-analysis/adcirc-fort-files-reference.md:260](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:260) | 보완 | F11-08 / 2DDI 둘째 헤더 | 중복 근거·판정을 models/ADCIRC/manual-notes/05-input-files-reference.md:34 정본 링크로 축약 | models/ADCIRC/manual-notes/05-input-files-reference.md:34 |
| [source-analysis/adcirc-fort-files-reference.md:261](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:261) | 보완 | F19-01 / fort.19 읽기 조건 | 중복 근거·판정을 models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:34 정본 링크로 축약 | models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:34 |
| [source-analysis/adcirc-fort-files-reference.md:262](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:262) | 보완 | F19-05 / ETIMINC 반복 여부 | 중복 근거·판정을 models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:35 정본 링크로 축약 | models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:35 |
| [source-analysis/adcirc-fort-files-reference.md:263](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:263) | 보완 | F20-01 / 읽기 조건 NFFR | 중복 근거·판정을 models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:41 정본 링크로 축약 | models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:41 |
| [source-analysis/adcirc-fort-files-reference.md:264](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:264) | 보완 | F20-06 / FTIMINC 반복 여부 | 중복 근거·판정을 models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:35 정본 링크로 축약 | models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:35 |
| [source-analysis/adcirc-fort-files-reference.md:268](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:268) | 보완 | NA-06 / quadratic_friction_coefficient_at_sea_floor | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 NA-06, NA-12, NA-13 |
| [source-analysis/adcirc-fort-files-reference.md:270](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:270) | 보완 | NA-12 / mannings_n_at_sea_floor: NOLIBF·0 이하 값 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:268 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:268 |
| [source-analysis/adcirc-fort-files-reference.md:271](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:271) | 보완 | NA-13 / chezy_friction_coefficient_at_sea_floor | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:268 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:268 |
| [source-analysis/adcirc-fort-files-reference.md:272](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:272) | 보완 | NA-16 / average_horizontal_eddy_viscosity_in_sea_water_wrt_depth: 변수·전역 대체값 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:60 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:60 |
| [source-analysis/adcirc-fort-files-reference.md:273](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:273) | 보완 | NA-17 / average_horizontal_eddy_viscosity_in_sea_water_wrt_depth: Smagorinsky 단위 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:61 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:61 |
| [source-analysis/adcirc-fort-files-reference.md:275](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:275) | 보완 | FORT36-01 / fort36: 사용 조건 | 중복 근거·판정을 models/ADCIRC/manual-notes/05-input-files-reference.md:47 정본 링크로 축약 | models/ADCIRC/manual-notes/05-input-files-reference.md:47 |
| [source-analysis/adcirc-fort-files-reference.md:276](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:276) | 보완 | FORT37-01 / fort37: 사용 조건 | 중복 근거·판정을 models/ADCIRC/manual-notes/05-input-files-reference.md:47 정본 링크로 축약 | models/ADCIRC/manual-notes/05-input-files-reference.md:47 |
| [source-analysis/adcirc-fort-files-reference.md:279](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:279) | 보완 | F14-30 / IBTYPE=102·112·122: 읽기와 할당의 차이 | 중복 근거·판정을 models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:37 정본 링크로 축약 | models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:37 |
| [source-analysis/adcirc-fort-files-reference.md:280](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:280) | 보완 | BATH-01 / NDDT 설정 위치·사용 조건 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:67 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:67 |
| [source-analysis/adcirc-fort-files-reference.md:285](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:285) | 보완 | ROT-04 / rotation_matrix: 3×3 행렬 | 중복 근거·판정을 models/ADCIRC/manual-notes/05-input-files-reference.md:41 정본 링크로 축약 | models/ADCIRC/manual-notes/05-input-files-reference.md:41 |
| [source-analysis/adcirc-fort-files-reference.md:286](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:286) | 보완 | CLI-10 / -Mft MESH_FILE_TYPE | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:43 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:43 |
| [source-analysis/adcirc-fort-files-reference.md:287](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:287) | 보완 | CLI-11 / -Mfn MESH_FILE_NAME | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:43 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:43 |
| [source-analysis/adcirc-fort-files-reference.md:288](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:288) | 보완 | CLI-12 / -Nft NODAL_ATTRIBUTES_FILE_TYPE | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:43 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:43 |
| [source-analysis/adcirc-fort-files-reference.md:289](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:289) | 보완 | CLI-13 / -Nfn NODAL_ATTRIBUTES_FILE_NAME | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:43 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:43 |
| [source-analysis/adcirc-fort-files-reference.md:290](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:290) | 보완 | NA-28 / EVM의 Smagorinsky 사용 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:61 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:61 |
| [source-analysis/adcirc-fort-files-reference.md:302](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:302) | 보완 | MET-02 / NWS=2: WTIMINC 레코드 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:210 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:210 |
| [source-analysis/adcirc-fort-files-reference.md:303](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:303) | 보완 | MET-05 / NWS=3의 좌표계 의무 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:211 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:211 |
| [source-analysis/adcirc-fort-files-reference.md:304](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:304) | 보완 | MET-07 / NWS=±4: PRN의 단위 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:212 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:212 |
| [source-analysis/adcirc-fort-files-reference.md:305](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:305) | 보완 | MET-09 / NWS=6: 날짜·시각 여섯 필드 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:213 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:213 |
| [source-analysis/adcirc-fort-files-reference.md:308](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:308) | 보완 | MET-32 / NWS=15·16: 입력 디렉터리 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:199 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:199 |
| [source-analysis/adcirc-fort-files-reference.md:309](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:309) | 보완 | MET-34 / NWS=15: HWind 격자 간격 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:217 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:217 |
| [source-analysis/adcirc-fort-files-reference.md:310](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:310) | 보완 | MET-38 / NWS=16: 예제의 Pc 열 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:218 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:218 |
| [source-analysis/adcirc-fort-files-reference.md:311](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:311) | 보완 | MET-42 / NWS=16: NCELLS의 형식 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:219 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:219 |
| [source-analysis/adcirc-fort-files-reference.md:312](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:312) | 보완 | F200-05 / NWS=11: UE·VE·PE의 저장 순서 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:220 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:220 |
| [source-analysis/adcirc-fort-files-reference.md:313](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:313) | 보완 | F200-06 / NWS=11: binary OPEN의 FORM | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:221 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:221 |
| [source-analysis/adcirc-fort-files-reference.md:314](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:314) | 보완 | F200-07 / NWS=11: 기압 단위 주장 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:222 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:222 |
| [source-analysis/adcirc-fort-files-reference.md:315](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:315) | 보완 | F200-09 / NWS=11: WTIMINC당 dataset 수 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:223 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:223 |
| [source-analysis/adcirc-fort-files-reference.md:316](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:316) | 보완 | F200-10 / NWS=11: -I 입력 경로 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:199 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:199 |
| [source-analysis/adcirc-fort-files-reference.md:318](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:318) | 보완 | NC13-02 / NWS=±13의 입력 종류 설명 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:197 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:197 |
| [source-analysis/adcirc-fort-files-reference.md:319](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:319) | 보완 | NC13-08 / time: 날짜 문자열 접두사 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:198 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:198 |
| [source-analysis/adcirc-fort-files-reference.md:320](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:320) | 보완 | NC13-12 / -I 경로 예외 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:199 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:199 |
| [source-analysis/adcirc-fort-files-reference.md:323](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:323) | 보완 | NC14-07 / NWS=-14의 netCDF 지원 주장 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 NC14-07, NC14-08 |
| [source-analysis/adcirc-fort-files-reference.md:324](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:324) | 보완 | NC14-08 / NWS=-14의 의미 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:323 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:323 |
| [source-analysis/adcirc-fort-files-reference.md:325](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:325) | 보완 | NC14-12 / -I의 경로 예외 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:199 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:199 |
| [source-analysis/adcirc-fort-files-reference.md:326](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:326) | 보완 | MET-41 / NWS=±7의 WVXFN·WVYFN 단위 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:214 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:214 |
| [source-analysis/adcirc-fort-files-reference.md:331](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:331) | 보완 | ICE-10 / 기본 얼음 drag 공식 | 중복 근거·판정을 models/ADCIRC/README.md:47 정본 링크로 축약 | models/ADCIRC/README.md:47 |
| [source-analysis/adcirc-fort-files-reference.md:332](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:332) | 보완 | ICE-11 / IceCube의 IC=0 수치·IC 정의 | 중복 근거·판정을 models/ADCIRC/README.md:48 정본 링크로 축약 | models/ADCIRC/README.md:48 |
| [source-analysis/adcirc-fort-files-reference.md:335](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:335) | 보완 | HS-04 / ETA1·ETA2·UU2·VV2·CH1·NODECODE: 저장 순서 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:139 정본 링크로 축약 / 중복 문단을 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:139; models/ADCIRC/source-analysis/adcirc-hotstart.md:54 |
| [source-analysis/adcirc-fort-files-reference.md:336](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:336) | 보완 | HS-08 / EP·IESTP·IVSTP·ICSTP·IPSTP·IWSTP·IGEP·IGVP·IGCP·IGPP·IGWP·NSCOU* | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:155 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:155 |
| [source-analysis/adcirc-fort-files-reference.md:337](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:337) | 보완 | HS-09 / 3D 블록의 조건 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:161 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:161 |
| [source-analysis/adcirc-fort-files-reference.md:338](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:338) | 보완 | HS-11 / DUU·DUV·DVV·UU·VV·BSX·BSY: 저장 순서 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:139 정본 링크로 축약 / 중복 문단을 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:139; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-fort-files-reference.md:339](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:339) | 보완 | HS-12 / REAL(Q)·AIMAG(Q)·WZ·q20·l·밀도 필드: 저장 순서 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:139 정본 링크로 축약 / 중복 문단을 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:139; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-fort-files-reference.md:340](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:340) | 보완 | HS-13 / IDEN 부호와 밀도 종류 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:161 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:161 |
| [source-analysis/adcirc-fort-files-reference.md:341](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:341) | 보완 | HS-16 / harmonic 블록의 실제 시작 조건 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:161 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:161 |
| [source-analysis/adcirc-fort-files-reference.md:342](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:342) | 보완 | HS-20 / STAELV·STAULV·STAVLV·GLOELV·GLOULV·GLOVLV 조건 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:162 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:162 |
| [source-analysis/adcirc-fort-files-reference.md:343](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:343) | 보완 | HS-21 / NTSTEPS·ELAV·ELVA·XVELAV·YVELAV·XVELVA·YVELVA 조건 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:161 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:161 |
| [source-analysis/adcirc-fort-files-reference.md:344](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:344) | 보완 | HS-22 / model timestep 변경 제한 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:116 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:116 |
| [source-analysis/adcirc-fort-files-reference.md:345](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:345) | 보완 | F14-32 / IBTYPE=4·24·64의 IBCONN 라벨 처리 | 중복 근거·판정을 models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:39 정본 링크로 축약 | models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:39 |
| [source-analysis/adcirc-fort-files-reference.md:346](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:346) | 보완 | MET-47 / NWS=±4의 prep 입력: list-directed | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:215 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:215 |
| [source-analysis/adcirc-fort-files-reference.md:360](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:360) | 보완 | NWS=29 계열의 얼음 시간 간격 | 행 번호의 보고서 명시 | fort15 §5 L343,L348 |
| [source-analysis/adcirc-fort-files-reference.md:368](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:368) | 정정 | 조화 분석 형식 2–5와 보정 경고 | 조화 출력 2–5 netCDF 일반화를 3·5 writer 조건으로 정정 | src/harm.F:401; src/write_output.F:2758–2828 |
| [source-analysis/adcirc-fort-files-reference.md:374](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:374) | 정정 | 음수 RES_BC_FLAG의 열 경계 시간 줄 | 이미 C로 바뀐 U04를 G로 가리키는 문장 정정 | src/read_input.F:5622–5624; fort15 §5 U04(L879) |
| [source-analysis/adcirc-fort-files-reference.md:449](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:449) | 보완 | WRAMP 입력의 부재 | WRAMP 전체 raw 검색 결과 추가 | docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst:309 |
| [source-analysis/adcirc-fort-files-reference.md:454](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:454) | 정정 | tau0_gen.f 생성 유틸리티 | tau0_gen D 철회; ASGS·adcircpy 구현과 등호 조건 C / 보조 프로그램 근거 경로를 저장소 루트 기준으로 명시 | raw/source_code/asgs/util/input/nodalattr/tau0_gen.f90:33–37,87–106; raw/source_code/adcircpy/adcircpy/mesh/mesh.py:167–202; docs/technical_reference/parameter_definitions/index.rst:513–519; models/ADCIRC/raw/source_code/asgs/util/input/nodalattr/tau0_gen.f90:33–37,94–106 |
| [source-analysis/adcirc-fort-files-reference.md:456](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:456) | 정정 | NCDATE 시간대 접미부의 수용 | datetime_fortran 근거의 생략 경로·고립된 줄 번호를 실제 경로로 교체 | thirdparty/datetime_fortran/src/lib/mod_datetime.f90:1247–1281; thirdparty/datetime_fortran/src/tests/datetime_tests.f90:427–443 |
| [source-analysis/adcirc-fort-files-reference.md:459](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:459) | 보완 | N06·N15·N16 · 형식 제어 부호 | 중복 문단을 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:575 |
| [source-analysis/adcirc-hotstart.md:50](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:50) | 보완 | D48 / binary IM 레코드 위치 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L1071, L1072, L1073, L1074, L1075, L1076, L1077, L1078, L1189 |
| [source-analysis/adcirc-hotstart.md:51](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:51) | 보완 | D48 / binary TIME 레코드 위치 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:50 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:50 |
| [source-analysis/adcirc-hotstart.md:52](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:52) | 보완 | D48 / binary IT 레코드 위치 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:50 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:50 |
| [source-analysis/adcirc-hotstart.md:53](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:53) | 보완 | D48 / POSTHOT / binary 헤더·상태 배열 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:50 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:50 |
| [source-analysis/adcirc-hotstart.md:54](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:54) | 정정 | D49 / binary 상태 ETA1 | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 설명의 정본 앵커 지정 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L1079, L1080, L1081, L1082, L1083, L1084 |
| [source-analysis/adcirc-hotstart.md:55](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:55) | 정정 | D49 / binary 상태 ETA2 | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:54 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:54 |
| [source-analysis/adcirc-hotstart.md:56](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:56) | 정정 | D49 / binary 상태 UU2 | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:54 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:54 |
| [source-analysis/adcirc-hotstart.md:57](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:57) | 정정 | D49 / binary 상태 VV2 | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:54 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:54 |
| [source-analysis/adcirc-hotstart.md:58](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:58) | 정정 | D49 / binary 상태 CH1 | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:54 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:54 |
| [source-analysis/adcirc-hotstart.md:59](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:59) | 정정 | D49 / binary 상태 NODECODE | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:54 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:54 |
| [source-analysis/adcirc-hotstart.md:60](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:60) | 보완 | D49 / POSTHOT / binary 헤더·상태 배열 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:50 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:50 |
| [source-analysis/adcirc-hotstart.md:61](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:61) | 보완 | D50 / binary EP / IESTP / NSCOUE | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L1096, L1097, L1098, L1099, L1100, L1101, L1102, L1103 |
| [source-analysis/adcirc-hotstart.md:62](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:62) | 보완 | D50 / binary IVSTP / NSCOUV | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:61 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:61 |
| [source-analysis/adcirc-hotstart.md:63](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:63) | 보완 | D50 / binary ICSTP / NSCOUC | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:61 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:61 |
| [source-analysis/adcirc-hotstart.md:64](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:64) | 보완 | D50 / binary IGEP / NSCOUGE | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:61 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:61 |
| [source-analysis/adcirc-hotstart.md:65](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:65) | 보완 | D50 / binary IGVP / NSCOUGV | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:61 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:61 |
| [source-analysis/adcirc-hotstart.md:66](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:66) | 보완 | D50 / binary IGCP / NSCOUGC | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:61 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:61 |
| [source-analysis/adcirc-hotstart.md:67](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:67) | 보완 | D50 / binary IPSTP / IWSTP / NSCOUM | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:61 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:61 |
| [source-analysis/adcirc-hotstart.md:68](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:68) | 보완 | D50 / binary IGPP / IGWP / NSCOUGW | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:61 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:61 |
| [source-analysis/adcirc-hotstart.md:69](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:69) | 정정 | D51 / 3차원 binary DUU 배열 | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 설명의 정본 앵커 지정 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L1112, L1113, L1114, L1115, L1116, L1117, L1118, L1119, L1120, L1121, L1122, L1123, L1124, L1125, L1126, L1194, L1195, L1196, L1197, L1198, L1199, L1200, L1201, L1202, L1203, L1204, L1205, L1206, L1207, L1208 |
| [source-analysis/adcirc-hotstart.md:70](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:70) | 정정 | D51 / 3차원 binary DUV 배열 | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:71](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:71) | 정정 | D51 / 3차원 binary DVV 배열 | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:72](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:72) | 정정 | D51 / 3차원 binary UU 배열 | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:73](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:73) | 정정 | D51 / 3차원 binary VV 배열 | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:74](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:74) | 정정 | D51 / 3차원 binary BSX 배열 | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:75](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:75) | 정정 | D51 / 3차원 binary BSY 배열 | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:76](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:76) | 정정 | D51 / 3차원 binary 층 자료 REAL(Q) | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:77](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:77) | 정정 | D51 / 3차원 binary 층 자료 AIMAG(Q) | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:78](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:78) | 정정 | D51 / 3차원 binary 층 자료 WZ | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:79](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:79) | 정정 | D51 / 3차원 binary 층 자료 q20 | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:80](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:80) | 정정 | D51 / 3차원 binary 층 자료 l | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:81](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:81) | 정정 | D51 / 3차원 binary 층 자료 SIGT | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:82](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:82) | 정정 | D51 / 3차원 binary 층 자료 SAL | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:83](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:83) | 정정 | D51 / 3차원 binary 층 자료 TEMP | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:84](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:84) | 정정 | D51 / POSTHOT / 3차원 DUU | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:85](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:85) | 정정 | D51 / POSTHOT / 3차원 DUV | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:86](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:86) | 정정 | D51 / POSTHOT / 3차원 DVV | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:87](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:87) | 정정 | D51 / POSTHOT / 3차원 UU | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:88](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:88) | 정정 | D51 / POSTHOT / 3차원 VV | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:89](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:89) | 정정 | D51 / POSTHOT / 3차원 BSX | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:90](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:90) | 정정 | D51 / POSTHOT / 3차원 BSY | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:91](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:91) | 정정 | D51 / POSTHOT / 3차원 REALQ | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:92](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:92) | 정정 | D51 / POSTHOT / 3차원 IMAGQ | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:93](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:93) | 정정 | D51 / POSTHOT / 3차원 WZ | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:94](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:94) | 정정 | D51 / POSTHOT / 3차원 q20 | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:95](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:95) | 정정 | D51 / POSTHOT / 3차원 l | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:96](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:96) | 정정 | D51 / POSTHOT / 3차원 SIGT | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:97](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:97) | 정정 | D51 / POSTHOT / 3차원 SAL | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:98](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:98) | 정정 | D51 / POSTHOT / 3차원 TEMP | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:99](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:99) | 보완 | D52 / 조화 상태의 전체 쓰기 조건 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L1127 |
| [source-analysis/adcirc-hotstart.md:100](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:100) | 보완 | D53 / 조화 상태 STAELV 조건 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L1136, L1137, L1138, L1139 |
| [source-analysis/adcirc-hotstart.md:101](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:101) | 보완 | D53 / 조화 상태 STAULV / STAVLV 조건 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:100 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:100 |
| [source-analysis/adcirc-hotstart.md:102](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:102) | 보완 | D53 / 조화 상태 GLOELV 조건 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:100 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:100 |
| [source-analysis/adcirc-hotstart.md:103](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:103) | 보완 | D53 / 조화 상태 GLOULV / GLOVLV 조건 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:100 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:100 |
| [source-analysis/adcirc-hotstart.md:104](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:104) | 보완 | D54 / 평균·분산(variance) 상태의 binary 쓰기 조건 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L1140 |
| [source-analysis/adcirc-hotstart.md:105](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:105) | 보완 | D55 / NHSTAR=3/5 / binary-only 파일 장 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L1148 |
| [source-analysis/adcirc-hotstart.md:106](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:106) | 보완 | D57 / 재시작에서 DTDP 변경 제한 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L1152 |
| [source-analysis/adcirc-hotstart.md:107](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:107) | 보완 | D63 / 핫스타트 전용 writer / netCDF 조건 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L1150, L1151 |
| [source-analysis/adcirc-hotstart.md:108](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:108) | 보완 | D63 / 핫스타트 전용 writer / 3차원·조화 상태 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:107 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:107 |
| [source-analysis/adcirc-hotstart.md:116](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:116) | 보완 | HS-22 model timestep 변경 제한 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 HS-22 |
| [source-analysis/adcirc-hotstart.md:139](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:139) | 보완 | HS-04 ETA1·ETA2·UU2·VV2·CH1·NODECODE: 저장 순서 | 중복 설명의 정본 앵커 지정 / 중복 문단을 정본 링크로 축약 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 HS-04, HS-11, HS-12; models/ADCIRC/source-analysis/adcirc-hotstart.md:54 |
| [source-analysis/adcirc-hotstart.md:155](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:155) | 보완 | HS-08 EP·IESTP·IVSTP·ICSTP·IPSTP·IWSTP·IGEP·IGVP·IGCP·IGPP·IGWP·NSCOU* | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 HS-08 |
| [source-analysis/adcirc-hotstart.md:161](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:161) | 보완 | HS-16 harmonic 블록의 실제 시작 조건 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 HS-09, HS-13, HS-16, HS-21 |
| [source-analysis/adcirc-hotstart.md:162](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:162) | 보완 | HS-20 STAELV·STAULV·STAVLV·GLOELV·GLOULV·GLOVLV 조건 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 HS-20 |
| [source-analysis/adcirc-hotstart.md:163](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:163) | 보완 | HS-21 NTSTEPS·ELAV·ELVA·XVELAV·YVELAV·XVELVA·YVELVA 조건 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:161 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:161 |
| [source-analysis/adcirc-hotstart.md:169](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:169) | 보완 | HS-09 3D 블록의 조건 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:161 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:161 |
| [source-analysis/adcirc-hotstart.md:170](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:170) | 보완 | HS-11 DUU·DUV·DVV·UU·VV·BSX·BSY: 저장 순서 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:139 정본 링크로 축약 / 중복 문단을 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:139; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:171](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:171) | 보완 | HS-12 REAL(Q)·AIMAG(Q)·WZ·q20·l·밀도 필드: 저장 순서 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:139 정본 링크로 축약 / 중복 문단을 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:139; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-hotstart.md:172](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:172) | 보완 | HS-13 IDEN 부호와 밀도 종류 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:161 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:161 |
| [source-analysis/adcirc-hotstart.md:223](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:223) | 보완 | HSNC-02 time·imhs·iths·출력 계수 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 HSNC-01, HSNC-02, HSNC-03, HSNC-04 |
| [source-analysis/adcirc-hotstart.md:224](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:224) | 보완 | HSNC-03 zeta1·zeta2·zetad·u-vel·v-vel·nodecode·noff·h1·h2 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:223 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:223 |
| [source-analysis/adcirc-hotstart.md:225](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:225) | 보완 | HSNC-04 rsx1·rsy1·rsx2·rsy2·swan_rsx1·swan_rsy1·swan_rsx2·swan_rsy2 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:223 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:223 |
| [source-analysis/adcirc-hotstart.md:226](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:226) | 보완 | HSNC-05 harmonic 차원·벡터·설정·주파수·행렬 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 HSNC-05, HSNC-06, HSNC-07 |
| [source-analysis/adcirc-hotstart.md:227](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:227) | 보완 | HSNC-06 harmonic station/global 부하 벡터 이름 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:226 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:226 |
| [source-analysis/adcirc-hotstart.md:228](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:228) | 보완 | HSNC-07 평균·분산(variance) 누적 상태 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:226 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:226 |
| [source-analysis/adcirc-hotstart.md:229](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:229) | 보완 | HSNC-08 3D의 duu·duv·dvv·uu·vv·bsx·bsy | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 HSNC-08, HSNC-09, HSNC-10 |
| [source-analysis/adcirc-hotstart.md:230](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:230) | 보완 | HSNC-09 3D의 sigt·salinity·temperature·u-vel3D·v-vel3D·w-vel3D·q20·l | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:229 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:229 |
| [source-analysis/adcirc-hotstart.md:231](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:231) | 보완 | HSNC-10 3D 출력 계수·레코드 번호 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:229 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:229 |
| [source-analysis/adcirc-hotstart.md:235](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:235) | 정정 | netCDF 핫스타트의 2차원 상태 schema·저장 | 노트 안에 없는 보고서 절 번호 삭제 / 인용의 위치 지시를 정확히 표현 | outputs §5 L720–L791 |
| [source-analysis/adcirc-hotstart.md:239](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-hotstart.md:239) | 보완 | 빈 줄 | CVB-HS-SWAN 신규 E 후보; 기존 결론과 분리 / CVB-HS-LOCAL 신규 E 후보; 기존 결론과 분리 | src/netcdfio.F90:6966–6977,8016–8024,8035,8073–8086,8137–8144; src/vsmy.F:3615–3626,3679–3692,3745–3763; src/sizes.F:138–140,161–166,205–217 |
| [source-analysis/adcirc-nodal-attributes.md:54](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:54) | 정정 | `sponge_generator_layer` | sponge 둘째 성분 미확인 문장을 확인된 유형 선택으로 정정 / pointer는 행렬 전체의 연결임을 명시 | src/nodalattr.F:1560–1563; src/sponge_layer.F90:274–395; src/nodalattr.F:1560–1562 |
| [source-analysis/adcirc-nodal-attributes.md:60](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:60) | 보완 | NA-16 average_horizontal_eddy_viscosity_in_sea_water_wrt_depth: 변수·전역 대체값 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 NA-16 |
| [source-analysis/adcirc-nodal-attributes.md:61](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:61) | 보완 | NA-17 average_horizontal_eddy_viscosity_in_sea_water_wrt_depth: Smagorinsky 단위 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 NA-17, NA-28 |
| [source-analysis/adcirc-nodal-attributes.md:62](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:62) | 보완 | NA-28 EVM의 Smagorinsky 사용 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:61 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:61 |
| [source-analysis/adcirc-nodal-attributes.md:73](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:73) | 정정 | SG-01 lookup netCDF: numNode·numPhi·phiSet | subgrid 단위 근거에서 주석 67을 제외하고 ETA2 비교 375를 사용 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:86 정본 링크로 축약 | src/subgridLookup.F:375,410–416; models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:86 |
| [source-analysis/adcirc-nodal-attributes.md:74](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:74) | 정정 | SG-02 cmfVertex·cfVertex·cadvVertex | subgrid 단위 근거에서 주석 67을 제외하고 ETA2 비교 375를 사용 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:86 정본 링크로 축약 | src/subgridLookup.F:375,410–416; models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:86 |
| [source-analysis/adcirc-nodal-attributes.md:75](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:75) | 정정 | SG-03 gridTotWatDepthVertex·wetTotWatDepthVertex·wetFractionVertex·binaryVertexList | subgrid 단위 근거에서 주석 67을 제외하고 ETA2 비교 375를 사용 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:86 정본 링크로 축약 | src/subgridLookup.F:375,410–416; models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:86 |
| [source-analysis/adcirc-nodal-attributes.md:81](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:81) | 보완 | XDMF-01 격자 파일의 geometry·depth·topology | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:104 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:104 |
| [source-analysis/adcirc-nodal-attributes.md:82](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:82) | 보완 | XDMF-02 boundary Set·Information·property·Attribute | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:104 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:104 |
| [source-analysis/adcirc-nodal-attributes.md:83](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:83) | 정정 | XDMF-03 노드 속성의 units·number_of_values·default_values·배열 | 노트 안에 없는 2.7·2.14 지시어 교체 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:104 정본 링크로 축약 | inputfiles §5 XDMF-03; models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:104 |
| [source-analysis/adcirc-nodal-attributes.md:90](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:90) | 보완 | ASCII 확산 속성의 발견 플래그 | 복사 가능 주석 대신 초기화·소비 조건으로 E 입증 | src/nodalattr.F:467,688,936,1277–1281 |
| [source-analysis/adcirc-nodal-attributes.md:92](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:92) | 보완 | ESLNodes.63 핫스타트 재입력 | D 판정의 전체 raw 검색 결과와 본체·보조 도구 범위 명시 | NA-38 |
| [source-analysis/adcirc-nodal-attributes.md:104](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:104) | 정정 | 교각 관계의 유효 범위·입력 권고 | P06·P07·P15의 실무 권고를 D에서 H로 변경 | docs/user_guide/special_features/bridge_piers.rst:39–58; src/nodalattr.F:2484–2486 |
| [source-analysis/adcirc-nodal-attributes.md:107](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:107) | 보완 | 교각 Fr의 중복 제곱 | 중복 문단의 정본 앵커 지정 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:107 |
| [source-analysis/adcirc-nodal-attributes.md:157](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:157) | 정정 | 내부 조석 변환의 강제력·수심 권고 | T02·T03 적용 권고 D→H | docs/user_guide/model_configuration/tides/internal_tide_energy_conversion.rst:38–53 |
| [source-analysis/adcirc-nodal-attributes.md:168](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:168) | 정정 | features 보고서 §5 T09 (423줄) | T09의 D 정의 오용 정정 | _staging/recovery/compare/external-results-ad.md:10; docs/user_guide/model_configuration/tides/internal_tide_energy_conversion.rst:58–62 |
| [source-analysis/adcirc-nodal-attributes.md:176](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:176) | 보완 | `src/nodalattr.F:2673–2684`의 Fit·TKM 구조는 Pringle et al.(2018) 식 (7)의 비국소형 행렬과 같다 (식 (7), PDF p.2–4; [외부 판정 T09](../../../_staging/recov | 입력 정규화의 조건과 전체 raw 검색 결과 명시 | src/nodalattr.F:2673–2684,2708–2721; raw/source_code/asgs/util/input/nodalattr/nodalattr.f90; _staging/recovery/compare/external-results-ad.md:10 |
| [source-analysis/adcirc-output-writers-implementation.md:73](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:73) | 보완 | D22 / fort.51–54 / NHASE·NHASV·NHAGE·NHAGV=3 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L410, L412, L416 |
| [source-analysis/adcirc-output-writers-implementation.md:74](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:74) | 보완 | D22 / fort.51–54 / NHASE·NHASV·NHAGE·NHAGV=5 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:73 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:73 |
| [source-analysis/adcirc-output-writers-implementation.md:75](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:75) | 보완 | D22 / fort.51–54 / 파일별 ASCII 전용 표기 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:73 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:73 |
| [source-analysis/adcirc-output-writers-implementation.md:76](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:76) | 보완 | D23 / fort.51 / 관측소 식별자 레코드 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L423, L432, L1181, L1182 |
| [source-analysis/adcirc-output-writers-implementation.md:77](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:77) | 보완 | D23 / fort.52 / 관측소 식별자 레코드 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:76 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:76 |
| [source-analysis/adcirc-output-writers-implementation.md:78](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:78) | 보완 | D23 / POST51 / 주파수·공간 수·식별자·진폭/위상 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:76 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:76 |
| [source-analysis/adcirc-output-writers-implementation.md:79](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:79) | 보완 | D23 / POST52 / 주파수·공간 수·식별자·진폭/위상 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:76 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:76 |
| [source-analysis/adcirc-output-writers-implementation.md:80](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:80) | 보완 | D24 / fort.55 / 수위 식별자 j와 자료 줄 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L461, L468, L1186 |
| [source-analysis/adcirc-output-writers-implementation.md:81](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:81) | 보완 | D24 / fort.55 / 속도 12개 자료의 줄 구분 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:80 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:80 |
| [source-analysis/adcirc-output-writers-implementation.md:82](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:82) | 보완 | D24 / POST55 / 수위·유속 줄 구조 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:80 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:80 |
| [source-analysis/adcirc-output-writers-implementation.md:83](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:83) | 보완 | D25 / 조화분석 속도 진폭 단위 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L458, L600 |
| [source-analysis/adcirc-output-writers-implementation.md:84](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:84) | 보완 | D25 / fort.51–54.nc / 진폭·위상 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:83 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:83 |
| [source-analysis/adcirc-output-writers-implementation.md:85](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:85) | 보완 | D26 / fort.55 / EAVDIF·EVADIF 의미 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L485 |
| [source-analysis/adcirc-output-writers-implementation.md:103](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:103) | 보완 | D14 / fort.41–46 / I3D 제어값 ±3 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L306, L308 |
| [source-analysis/adcirc-output-writers-implementation.md:104](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:104) | 보완 | D14 / fort.41–46 / I3D 제어값 ±5 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:103 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:103 |
| [source-analysis/adcirc-output-writers-implementation.md:105](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:105) | 보완 | D15 / fort.41 / IDEN=±4 / SIGTSTA | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L359, L360, L361 |
| [source-analysis/adcirc-output-writers-implementation.md:106](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:106) | 보완 | D15 / fort.41 / IDEN=±4 / TEMPSTA | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:105 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:105 |
| [source-analysis/adcirc-output-writers-implementation.md:107](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:107) | 보완 | D15 / fort.41 / IDEN=±4 / SALSTA | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:105 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:105 |
| [source-analysis/adcirc-output-writers-implementation.md:109](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:109) | 보완 | D16 / POST44 / 밀도 헤더·조건·좌표·값 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L1179 |
| [source-analysis/adcirc-output-writers-implementation.md:110](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:110) | 보완 | D17 / fort.44 / IDEN=±2 / TIME, IT, SIGMA | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L364, L367, L370 |
| [source-analysis/adcirc-output-writers-implementation.md:111](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:111) | 보완 | D17 / fort.44 / IDEN=±3 / TIME, IT, SIGMA | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:110 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:110 |
| [source-analysis/adcirc-output-writers-implementation.md:112](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:112) | 보완 | D17 / fort.44 / IDEN=±4 / TIME, IT, SIGMA | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:110 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:110 |
| [source-analysis/adcirc-output-writers-implementation.md:114](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:114) | 보완 | D17 / POST44 / 밀도 헤더·조건·좌표·값 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:109 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:109 |
| [source-analysis/adcirc-output-writers-implementation.md:115](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:115) | 보완 | D18 / fort.43 / ISTA → lSta | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L380 |
| [source-analysis/adcirc-output-writers-implementation.md:116](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:116) | 보완 | D19 / fort.43·46 / EV 의미 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L392 |
| [source-analysis/adcirc-output-writers-implementation.md:117](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:117) | 보완 | D20 / fort.47 / 생성 조건·출력 간격 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L394, L397, L398, L1180 |
| [source-analysis/adcirc-output-writers-implementation.md:118](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:118) | 보완 | D20 / fort.47 / 헤더 DTDP*NSPO3DGD | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:117 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:117 |
| [source-analysis/adcirc-output-writers-implementation.md:119](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:119) | 보완 | D20 / fort.47 / 헤더 NSPO3DGD | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:117 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:117 |
| [source-analysis/adcirc-output-writers-implementation.md:120](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:120) | 보완 | D20 / POST47 / 헤더·TIME/IT·수온 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:117 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:117 |
| [source-analysis/adcirc-output-writers-implementation.md:121](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:121) | 보완 | D21 / fort.45·46 / IRTYPE=3 의미 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L349 |
| [source-analysis/adcirc-output-writers-implementation.md:122](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:122) | 보완 | D44 / fort.42.nc·fort.45.nc / Cartesian 수직 유속 방향 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L598 |
| [source-analysis/adcirc-output-writers-implementation.md:123](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:123) | 보완 | D66 / fort.41.nc·fort.44.nc / G의 otherwise 단위 속성 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L609 |
| [source-analysis/adcirc-output-writers-implementation.md:139](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:139) | 보완 | D27 / max/min / 공통 NOUTGE 형식 설명 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L504, L510, L513, L516, L519 |
| [source-analysis/adcirc-output-writers-implementation.md:140](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:140) | 보완 | D27 / maxvel.63 / 형식·활성 조건 NOUTGV | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:139 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:139 |
| [source-analysis/adcirc-output-writers-implementation.md:141](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:141) | 보완 | D27 / minpr.63 / 형식·활성 조건 NOUTGW | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:139 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:139 |
| [source-analysis/adcirc-output-writers-implementation.md:142](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:142) | 보완 | D27 / maxwvel.63 / 형식·활성 조건 NOUTGW | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:139 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:139 |
| [source-analysis/adcirc-output-writers-implementation.md:143](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:143) | 보완 | D27 / maxrs.63 / 형식·활성 조건 NOUTGW | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:139 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:139 |
| [source-analysis/adcirc-output-writers-implementation.md:144](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:144) | 보완 | D28 / max/min / DTDP*NSPOOLGE | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L497, L498, L528, L529, L534, L535, L540, L541 |
| [source-analysis/adcirc-output-writers-implementation.md:145](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:145) | 보완 | D28 / max/min / NSPOOLGE | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:144 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:144 |
| [source-analysis/adcirc-output-writers-implementation.md:146](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:146) | 보완 | D28 / maxinundepth.63 / 헤더 DTDP*NSPOOLGE | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:144 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:144 |
| [source-analysis/adcirc-output-writers-implementation.md:147](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:147) | 보완 | D28 / maxinundepth.63 / 헤더 NSPOOLGE | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:144 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:144 |
| [source-analysis/adcirc-output-writers-implementation.md:148](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:148) | 보완 | D28 / everdried.63 / 헤더 DTDP*NSPOOLGE | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:144 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:144 |
| [source-analysis/adcirc-output-writers-implementation.md:149](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:149) | 보완 | D28 / everdried.63 / 헤더 NSPOOLGE | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:144 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:144 |
| [source-analysis/adcirc-output-writers-implementation.md:150](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:150) | 보완 | D28 / inundationtime.63 / 헤더 DTDP*NSPOOLGE | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:144 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:144 |
| [source-analysis/adcirc-output-writers-implementation.md:151](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:151) | 보완 | D28 / inundationtime.63 / 헤더 NSPOOLGE | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:144 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:144 |
| [source-analysis/adcirc-output-writers-implementation.md:152](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:152) | 보완 | D29 / maxwvel.63 / 값 WVNOUTMAX | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L286, L514 |
| [source-analysis/adcirc-output-writers-implementation.md:153](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:153) | 보완 | D30 / maxrs.63 / 값 RSNMAX | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L517 |
| [source-analysis/adcirc-output-writers-implementation.md:154](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:154) | 보완 | D35 / nodecode.63·noff.100 / 자료 세트 수 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L563 |
| [source-analysis/adcirc-output-writers-implementation.md:155](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:155) | 보완 | D36 / initiallydry.63 / 숫자 헤더·TIME·IT | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L555 |
| [source-analysis/adcirc-output-writers-implementation.md:156](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:156) | 보완 | D37 / endrisinginun.63 / ASCII 헤더 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L559 |
| [source-analysis/adcirc-output-writers-implementation.md:157](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:157) | 보완 | D38 / noff.100 / 요소 식별자 i | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L564, L565 |
| [source-analysis/adcirc-output-writers-implementation.md:158](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:158) | 보완 | D32 / everdried.63 / 총 건조 시간 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L549 |
| [source-analysis/adcirc-output-writers-implementation.md:159](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:159) | 보완 | D33 / inundationtime.63 / 누적 시간 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L550 |
| [source-analysis/adcirc-output-writers-implementation.md:160](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:160) | 보완 | D34 / inundationtime.63 / 자료 종류 설명 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L552 |
| [source-analysis/adcirc-output-writers-implementation.md:161](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:161) | 보완 | D39 / inundationtime.63.nc / inun_time 단위 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L602 |
| [source-analysis/adcirc-output-writers-implementation.md:162](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:162) | 보완 | D40 / maxinundepth.63.nc / 기준면 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L604 |
| [source-analysis/adcirc-output-writers-implementation.md:163](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:163) | 보완 | D41 / everdried.63.nc / 시간 변수 의미 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L605 |
| [source-analysis/adcirc-output-writers-implementation.md:164](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:164) | 보완 | D67 / maxinundepth.63.nc / inun_max의 English 단위 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L589 |
| [source-analysis/adcirc-output-writers-implementation.md:175](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:175) | 보완 | D31 / maxinundepth·inundationtime·everdried / hot start 누적 범위 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L546 |
| [source-analysis/adcirc-output-writers-implementation.md:185](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:185) | 보완 | D42 / netCDF 출력의 격자 포함 설명 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L583 |
| [source-analysis/adcirc-output-writers-implementation.md:186](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:186) | 보완 | D47 / fort.77.nc / 시간 차원 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L607, L1502 |
| [source-analysis/adcirc-output-writers-implementation.md:187](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:187) | 보완 | D60 / depth / English 길이 단위 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L587, L588 |
| [source-analysis/adcirc-output-writers-implementation.md:188](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:188) | 보완 | D60 / barht·pipediam / English 길이 단위 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:187 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:187 |
| [source-analysis/adcirc-output-writers-implementation.md:287](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:287) | 보완 | D61 / SWAN 출력 개수 제한 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L1217 |
| [source-analysis/adcirc-output-writers-implementation.md:288](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:288) | 보완 | D64 / windDrag.173 / 이름·조건·간격 | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L1226 |
| [source-analysis/adcirc-output-writers-implementation.md:289](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:289) | 보완 | D65 / POST71 / 헤더 NSTAM | 중복 설명의 정본 앵커 지정 | ADCIRC-outputs-vs-code.md#5-차이-결론\|outputs 보고서 §5 L1167, L1168, L1174, L1178 |
| [source-analysis/adcirc-output-writers-implementation.md:290](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:290) | 보완 | D65 / POST91 / 헤더 NSTAM | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:289 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:289 |
| [source-analysis/adcirc-output-writers-implementation.md:291](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:291) | 보완 | D65 / POST43 / 헤더 관측소 수 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:289 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:289 |
| [source-analysis/adcirc-output-writers-implementation.md:460](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:460) | 보완 | D01 / 관측소 `-2`와 `+2` / 전역 `-2`와 `+2` / 농도 전역 `NOUTGC=0,±1,±2,±4,±5,±7` | D 판정의 전체 raw 검색 결과와 본체·보조 도구 범위 명시 | NOUTGC |
| [source-analysis/adcirc-output-writers-implementation.md:470](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:470) | 보완 | D12 / fort.72 / 단위 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:152 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:152 |
| [source-analysis/adcirc-output-writers-implementation.md:472](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:472) | 보완 | D14 / fort.41–46 / I3D 제어값 ±3 / fort.41–46 / I3D 제어값 ±5 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:103 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:103 |
| [source-analysis/adcirc-output-writers-implementation.md:473](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:473) | 보완 | D15 / fort.41 / IDEN=±4 / SIGTSTA / fort.41 / IDEN=±4 / TEMPSTA / fort.41 / IDEN=±4 / SALSTA | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:105 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:105 |
| [source-analysis/adcirc-output-writers-implementation.md:476](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:476) | 보완 | D18 / fort.43 / ISTA → lSta | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:115 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:115 |
| [source-analysis/adcirc-output-writers-implementation.md:477](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:477) | 보완 | D19 / fort.43·46 / EV 의미 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:116 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:116 |
| [source-analysis/adcirc-output-writers-implementation.md:478](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:478) | 보완 | D20 / fort.47 / 생성 조건·출력 간격 / fort.47 / 헤더 DTDP*NSPO3DGD / fort.47 / 헤더 NSPO3DGD / POST47 / 헤더·TIME/IT·수온 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:117 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:117 |
| [source-analysis/adcirc-output-writers-implementation.md:479](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:479) | 보완 | D21 / fort.45·46 / IRTYPE=3 의미 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:121 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:121 |
| [source-analysis/adcirc-output-writers-implementation.md:480](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:480) | 보완 | D22 / fort.51–54 / NHASE·NHASV·NHAGE·NHAGV=3 / fort.51–54 / NHASE·NHASV·NHAGE·NHAGV=5 / fort.51–54 / 파일별 ASCII 전용 표기 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:73 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:73 |
| [source-analysis/adcirc-output-writers-implementation.md:481](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:481) | 보완 | D23 / fort.51 / 관측소 식별자 레코드 / fort.52 / 관측소 식별자 레코드 / POST51 / 주파수·공간 수·식별자·진폭/위상 / POST52 / 주파수·공간 수·식별자·진폭/위상 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:76 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:76 |
| [source-analysis/adcirc-output-writers-implementation.md:482](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:482) | 보완 | D24 / fort.55 / 수위 식별자 j와 자료 줄 / fort.55 / 속도 12개 자료의 줄 구분 / POST55 / 수위·유속 줄 구조 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:80 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:80 |
| [source-analysis/adcirc-output-writers-implementation.md:483](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:483) | 보완 | D25 / 조화분석 속도 진폭 단위 / fort.51–54.nc / 진폭·위상 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:83 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:83 |
| [source-analysis/adcirc-output-writers-implementation.md:484](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:484) | 보완 | D26 / fort.55 / EAVDIF·EVADIF 의미 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:85 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:85 |
| [source-analysis/adcirc-output-writers-implementation.md:485](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:485) | 보완 | D27 / max/min / 공통 NOUTGE 형식 설명 / maxvel.63 / 형식·활성 조건 NOUTGV / minpr.63 / 형식·활성 조건 NOUTGW / maxwvel.63 / 형식·활성 조건 NOUTGW / maxrs.63 / 형식·활성 조건 NOUTGW | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:139 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:139 |
| [source-analysis/adcirc-output-writers-implementation.md:486](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:486) | 보완 | D28 / max/min / DTDP*NSPOOLGE / max/min / NSPOOLGE / maxinundepth.63 / 헤더 DTDP*NSPOOLGE / maxinundepth.63 / 헤더 NSPOOLGE / everdried.63 / 헤더 DTDP*NSPOOLGE / everdried.63 / 헤더 NSPOOLGE / inundationtime.63 / 헤더 DTDP*NSPOOLGE / inundationtime.63 / 헤더 NSPOOLGE | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:144 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:144 |
| [source-analysis/adcirc-output-writers-implementation.md:487](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:487) | 보완 | D29 / maxwvel.63 / 값 WVNOUTMAX | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:152 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:152 |
| [source-analysis/adcirc-output-writers-implementation.md:488](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:488) | 보완 | D30 / maxrs.63 / 값 RSNMAX | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:153 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:153 |
| [source-analysis/adcirc-output-writers-implementation.md:489](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:489) | 보완 | D31 / maxinundepth·inundationtime·everdried / hot start 누적 범위 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:175 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:175 |
| [source-analysis/adcirc-output-writers-implementation.md:490](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:490) | 보완 | D32 / everdried.63 / 총 건조 시간 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:158 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:158 |
| [source-analysis/adcirc-output-writers-implementation.md:491](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:491) | 보완 | D33 / inundationtime.63 / 누적 시간 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:159 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:159 |
| [source-analysis/adcirc-output-writers-implementation.md:492](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:492) | 보완 | D34 / inundationtime.63 / 자료 종류 설명 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:160 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:160 |
| [source-analysis/adcirc-output-writers-implementation.md:493](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:493) | 보완 | D35 / nodecode.63·noff.100 / 자료 세트 수 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:154 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:154 |
| [source-analysis/adcirc-output-writers-implementation.md:494](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:494) | 보완 | D36 / initiallydry.63 / 숫자 헤더·TIME·IT | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:155 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:155 |
| [source-analysis/adcirc-output-writers-implementation.md:495](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:495) | 보완 | D37 / endrisinginun.63 / ASCII 헤더 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:156 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:156 |
| [source-analysis/adcirc-output-writers-implementation.md:496](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:496) | 보완 | D38 / noff.100 / 요소 식별자 i | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:157 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:157 |
| [source-analysis/adcirc-output-writers-implementation.md:497](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:497) | 보완 | D39 / inundationtime.63.nc / inun_time 단위 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:161 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:161 |
| [source-analysis/adcirc-output-writers-implementation.md:498](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:498) | 보완 | D40 / maxinundepth.63.nc / 기준면 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:162 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:162 |
| [source-analysis/adcirc-output-writers-implementation.md:499](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:499) | 보완 | D41 / everdried.63.nc / 시간 변수 의미 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:163 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:163 |
| [source-analysis/adcirc-output-writers-implementation.md:500](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:500) | 보완 | D42 / netCDF 출력의 격자 포함 설명 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:185 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:185 |
| [source-analysis/adcirc-output-writers-implementation.md:501](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:501) | 보완 | D44 / fort.42.nc·fort.45.nc / Cartesian 수직 유속 방향 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:122 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:122 |
| [source-analysis/adcirc-output-writers-implementation.md:502](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:502) | 보완 | D47 / fort.77.nc / 시간 차원 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:186 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:186 |
| [source-analysis/adcirc-output-writers-implementation.md:503](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:503) | 보완 | D48 / binary IM 레코드 위치 / binary TIME 레코드 위치 / binary IT 레코드 위치 / POSTHOT / binary 헤더·상태 배열 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:50 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:50 |
| [source-analysis/adcirc-output-writers-implementation.md:504](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:504) | 정정 | D49 / binary 상태 ETA1 / binary 상태 ETA2 / binary 상태 UU2 / binary 상태 VV2 / binary 상태 CH1 / binary 상태 NODECODE / POSTHOT / binary 헤더·상태 배열 | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148 |
| [source-analysis/adcirc-output-writers-implementation.md:505](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:505) | 보완 | D50 / binary EP / IESTP / NSCOUE / binary IVSTP / NSCOUV / binary ICSTP / NSCOUC / binary IGEP / NSCOUGE / binary IGVP / NSCOUGV / binary IGCP / NSCOUGC / binary IPSTP / IWSTP / NSCOUM / binary IGPP / IGWP / NSCOUGW | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:61 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:61 |
| [source-analysis/adcirc-output-writers-implementation.md:506](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:506) | 정정 | D51 / 3차원 binary DUU 배열 / 3차원 binary DUV 배열 / 3차원 binary DVV 배열 / 3차원 binary UU 배열 / 3차원 binary VV 배열 / 3차원 binary BSX 배열 / 3차원 binary BSY 배열 / 3차원 binary 층 자료 REAL(Q) / 3차원 binary 층 자료 AIMAG(Q) / 3차원 binary 층 자료 WZ / 3차원 binary 층 자료 q20 / 3차원 binary 층 자료 l / 3차원 binary 층 자료 SIGT / 3차원 binary 층 자료 SAL / 3차원 binary 층 자료 TEMP / POSTHOT / 3차원 DUU / POSTHOT / 3차원 DUV / POSTHOT / 3차원 DVV / POSTHOT / 3차원 UU / POSTHOT / 3차원 VV / POSTHOT / 3차원 BSX / POSTHOT / 3차원 BSY / POSTHOT / 3차원 REALQ / POSTHOT / 3차원 IMAGQ / POSTHOT / 3차원 WZ / POSTHOT / 3차원 q20 / POSTHOT / 3차원 l / POSTHOT / 3차원 SIGT / POSTHOT / 3차원 SAL / POSTHOT / 3차원 TEMP | D49·D51의 근거 없는 판 변경 해석을 B로 통일; 2D 배열과 층 배열 구분 / 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:69 정본 링크로 축약 | docs/technical_reference/input_files/fort6768.rst:33–40,64–83; src/hstart.F:524–546,608–618; src/write_output.F:5122–5149; src/vsmy.F:3563–3579,3617–3626,5293–5295; prep/post.F:4060–4148; models/ADCIRC/source-analysis/adcirc-hotstart.md:69 |
| [source-analysis/adcirc-output-writers-implementation.md:507](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:507) | 보완 | D52 / 조화 상태의 전체 쓰기 조건 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:99 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:99 |
| [source-analysis/adcirc-output-writers-implementation.md:508](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:508) | 보완 | D53 / 조화 상태 STAELV 조건 / 조화 상태 STAULV / STAVLV 조건 / 조화 상태 GLOELV 조건 / 조화 상태 GLOULV / GLOVLV 조건 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:100 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:100 |
| [source-analysis/adcirc-output-writers-implementation.md:509](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:509) | 보완 | D54 / 평균·분산(variance) 상태의 binary 쓰기 조건 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:104 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:104 |
| [source-analysis/adcirc-output-writers-implementation.md:510](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:510) | 보완 | D55 / NHSTAR=3/5 / binary-only 파일 장 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:105 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:105 |
| [source-analysis/adcirc-output-writers-implementation.md:511](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:511) | 보완 | D57 / 재시작에서 DTDP 변경 제한 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-hotstart.md:106 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-hotstart.md:106 |
| [source-analysis/adcirc-output-writers-implementation.md:513](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:513) | 보완 | D60 / depth / English 길이 단위 / barht·pipediam / English 길이 단위 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:187 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:187 |
| [source-analysis/adcirc-output-writers-implementation.md:514](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:514) | 보완 | D61 / SWAN 출력 개수 제한 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:287 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:287 |
| [source-analysis/adcirc-output-writers-implementation.md:516](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:516) | 보완 | D64 / windDrag.173 / 이름·조건·간격 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:288 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:288 |
| [source-analysis/adcirc-output-writers-implementation.md:517](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:517) | 보완 | D65 / POST71 / 헤더 NSTAM / POST91 / 헤더 NSTAM / POST43 / 헤더 관측소 수 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:289 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:289 |
| [source-analysis/adcirc-output-writers-implementation.md:518](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:518) | 보완 | D66 / fort.41.nc·fort.44.nc / G의 otherwise 단위 속성 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:123 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:123 |
| [source-analysis/adcirc-output-writers-implementation.md:519](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:519) | 보완 | D67 / maxinundepth.63.nc / inun_max의 English 단위 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:164 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:164 |
| [source-analysis/adcirc-output-writers-implementation.md:539](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:539) | 정정 | 3차원 netCDF 변수 schema | 노트 안에 없는 2.7 지시어를 항목 ID로 교체 | outputs §5 L598,L602,L604,L605,L609,L680,L1390 |
| [source-analysis/adcirc-output-writers-implementation.md:551](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:551) | 정정 | 조화분석 netCDF 변수 schema | 노트 안에 없는 2.7 지시어를 항목 ID로 교체 | outputs §5 L598,L602,L604,L605,L609,L680,L1390 |
| [source-analysis/adcirc-output-writers-implementation.md:552](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:552) | 정정 | 2차원 수위·유속·기압·TAU0·drag schema | 노트 안에 없는 2.7 지시어를 항목 ID로 교체 / 2D nodal 변수의 station 인용을 case63·64·73으로 교체; pressure 직접 인용 | outputs §5 L598,L602,L604,L605,L609,L680,L1390; src/netcdfio.F90:1972–1977,2081–2090,2284–2291 |
| [source-analysis/adcirc-output-writers-implementation.md:553](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:553) | 정정 | 기상·얼음 netCDF 변수 schema | 노트 안에 없는 2.7 지시어를 항목 ID로 교체 | outputs §5 L598,L602,L604,L605,L609,L680,L1390 |
| [source-analysis/adcirc-output-writers-implementation.md:555](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:555) | 정정 | 표층 수온·경압 기울기·복사응력 기울기 schema | 노트 안에 없는 2.7 지시어를 항목 ID로 교체 | outputs §5 L598,L602,L604,L605,L609,L680,L1390 |
| [source-analysis/adcirc-output-writers-implementation.md:556](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:556) | 정정 | 극값·침수 netCDF 변수 schema | 노트 안에 없는 2.7 지시어를 항목 ID로 교체 | outputs §5 L598,L602,L604,L605,L609,L680,L1390 |
| [source-analysis/adcirc-output-writers-implementation.md:557](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:557) | 정정 | fort.77.nc 변수 이름 정의 | 노트 안에 없는 2.7 지시어를 항목 ID로 교체 | outputs §5 L598,L602,L604,L605,L609,L680,L1390 |
| [source-analysis/adcirc-output-writers-implementation.md:558](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:558) | 정정 | SWAN 추가 파일·최대값·netCDF schema | SWAN 배열 지시어를 보고서 ID로 교체 | outputs §5 L684–L698 |
| [source-analysis/adcirc-output-writers-implementation.md:559](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:559) | 정정 | netCDF 격자·경계 schema | 노트 안에 없는 2.7 지시어를 항목 ID로 교체 | outputs §5 L598,L602,L604,L605,L609,L680,L1390 |
| [source-analysis/adcirc-output-writers-implementation.md:563](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:563) | 정정 | XDMF 출력 창의 최종화·병렬 자료 수 | XDMF E 근거를 식과 호출 조건으로 교체; np 대 np_g는 조건부 미확인 | src/xdmfio.F:151–178,264–270,329–341; src/write_output.F:484,1861–1862 |
| [source-analysis/adcirc-output-writers-implementation.md:568](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:568) | 보완 | 전용 sparse vector의 기록 수 | sparse vector E를 주석 대신 AND·OR 실제 식으로 입증 | src/writer.F:674–685 |
| [source-analysis/adcirc-output-writers-implementation.md:569](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:569) | 보완 | fort.56 디버그 구현의 호출 | fort.56 호출 부재의 검색 범위를 raw 전체로 확장 | src/harm.F:359,366,384 |
| [source-analysis/adcirc-output-writers-implementation.md:575](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:575) | 보완 | N06·N15·N16 · 형식 제어 부호 | 중복 문단의 정본 앵커 지정 | models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:575 |
| [source-analysis/adcirc-output-writers-implementation.md:589](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:589) | 보완 | 로컬 `src/read_input.F:3634–3636`은 `Binary format output is no longer supported.` 메시지와 `terminate(exit_code=...)`를 사용한다 ([outputs 보고서 §5  | CVB-WIND7-UNITS 신규 E 후보; 기존 결론과 분리 | src/wind.F:1142–1165; src/write_output.F:803–808,936–939,2068–2086; src/netcdfio.F90:1267–1271,2472–2482 |
| [source-analysis/adcirc-preprocessing-foundation.md:43](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:43) | 보완 | CLI-10 -Mft MESH_FILE_TYPE | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 CLI-10, CLI-11, CLI-12, CLI-13 |
| [source-analysis/adcirc-preprocessing-foundation.md:44](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:44) | 보완 | CLI-11 -Mfn MESH_FILE_NAME | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:43 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:43 |
| [source-analysis/adcirc-preprocessing-foundation.md:45](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:45) | 보완 | CLI-12 -Nft NODAL_ATTRIBUTES_FILE_TYPE | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:43 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:43 |
| [source-analysis/adcirc-preprocessing-foundation.md:46](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:46) | 보완 | CLI-13 -Nfn NODAL_ATTRIBUTES_FILE_NAME | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:43 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:43 |
| [source-analysis/adcirc-preprocessing-foundation.md:47](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:47) | 보완 | CLI-14 -U·소문자 별칭 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 CLI-14, CLI-15, CLI-23, CLI-24, CLI-25 |
| [source-analysis/adcirc-preprocessing-foundation.md:48](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:48) | 보완 | CLI-15 -h·--help·-V·-v·--version·--hash | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:47 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:47 |
| [source-analysis/adcirc-preprocessing-foundation.md:50](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:50) | 보완 | CLI-23 adcprep --partmesh_npart_from_epart·--strict-boundaries | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:47 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:47 |
| [source-analysis/adcirc-preprocessing-foundation.md:51](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:51) | 보완 | CLI-24 adcprep의 파일 유형·이름 옵션 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:47 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:47 |
| [source-analysis/adcirc-preprocessing-foundation.md:52](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:52) | 보완 | CLI-26 aswip의 추가 단일 옵션 | 중복 설명의 정본 앵커 지정 | ADCIRC-inputfiles-vs-code.md#5-차이-결론\|inputfiles 보고서 §5 CLI-26, CLI-27 |
| [source-analysis/adcirc-preprocessing-foundation.md:53](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:53) | 보완 | CLI-27 aswip의 추가 값 옵션 | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:52 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:52 |
| [source-analysis/adcirc-topic-map.md:59](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-topic-map.md:59) | 보완 | F17 교각 식 | 중복 문단을 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:107 |
| [source-analysis/adcirc-topic-map.md:60](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-topic-map.md:60) | 보완 | F17 동적 수위 보정 | 동적 수위 보정 램프의 기본값 근거 추가 | src/wind.F:243–244 |
| [source-analysis/adcirc-topic-map.md:62](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-topic-map.md:62) | 보완 | F18 DG·ALI 분산·subgrid·시변 지형/위어 | D 판정의 전체 raw 검색 결과와 본체·보조 도구 범위 명시 | C42-DG |
| [source-analysis/adcirc-topic-map.md:64](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-topic-map.md:64) | 보완 | F18 subgrid | 중복 근거·판정을 models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:94 정본 링크로 축약 | models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:94 |
| [source-analysis/adcirc-topic-map.md:66](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-topic-map.md:66) | 정정 | F18 sponge | sponge 확인 상태를 U-06과 일치시킴 | inputfiles §5 U-06 |
| [source-analysis/adcirc-topic-map.md:73](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-topic-map.md:73) | 정정 | 문서상 검증 사례의 판과 적용 조건 | 검증 사례의 적용·성능 판정 D→H | _staging/recovery/read/ADCIRC/manuals/pdfs/1999_Luettich01.pdf/p001-009.md:19 |
| [source-analysis/adcirc-topic-map.md:74](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-topic-map.md:74) | 정정 | 외부 subgrid 생성 도구와 ADCIRC의 읽기 범위 | 외부 subgrid 생성 기능 D→H / 중복 문단을 정본 링크로 축약 | docs/tools/subgrid_adcirc_utility.rst:6–18; src/subgridLookup.F:193–204; models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:117 |

## 전 줄 대조대장

이 대장의 모든 줄은 작업 시작 시 + 줄이다. 중복 줄의 원문 근거도 그 위치에서 확인했다. ‘구조·참조’는 제목·빈 줄·표 구분선·메타데이터·정본 링크처럼 독립된 코드 동작을 주장하지 않는 줄이다. 원문 위치는 초기 인용에 연결된 줄을 범위로 묶었다. 잘못된 인용의 새 근거는 위 정정 목록과 수정 노트에 기록했다.

### README.md

| 초기 줄 | 결과 | 대조한 원문·참조 |
|---:|---|---|
| 2 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 11 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 12 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 15 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 16 | 이상 없음 | `src/read_input.F:1775–1776,2316` |
| 17 | 이상 없음 | `src/read_input.F:1775–1776,2316`<br>`docs/technical_reference/input_files/fort25.rst:43,47`<br>`src/wind.F:132,139,520,762–763,767,778` |
| 18 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 43 | 정정 | `src/read_input.F:2316–2317`<br>`src/wind.F:132,139,758–759,761–764,767` |
| 45 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 46 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 47 | 보완 | `docs/technical_reference/input_files/fort25.rst:7,43,47`<br>`src/wind.F:124–127,132,736,767–778` |
| 48 | 보완 | `docs/technical_reference/input_files/fort25.rst:39,47,49`<br>`src/wind.F:761–763` |
| 50 | 이상 없음 | `docs/technical_reference/input_files/fort25.rst:21`<br>`src/wind.F:761,1395–1397,1682,1726–1727` |

### manual-notes/05-input-files-reference.md

| 초기 줄 | 결과 | 대조한 원문·참조 |
|---:|---|---|
| 9 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 31 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 32 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 33 | 보완 | `docs/technical_reference/input_files/fort10.rst:18,24,27`<br>`src/read_input.F:3135,3139,3148`<br>`prep/prep.F:124–133` |
| 34 | 보완 | `docs/technical_reference/input_files/fort11.rst:20,31,42,53`<br>`src/read_input.F:3086,3091,3093–3095` |
| 35 | 보완 | `src/read_input.F:882,3089`<br>`src/couple2baroclinic3D.F:108,121,127,134,137,139,141,144,146,148,151–152,154,157,159–165,193,195,205–206,210,213–216,220–223,225–228,230,243–244,246,253,255,267,280,282,284–285,288–289,501–512` |
| 36 | 보완 | `src/couple2baroclinic3D.F:121,134,137,139,141,144,146,148,151–152,154,157,159–165,213,215,228,253,255–258,267–270,280,282,284–285,288–289,297–305,307–309,501–512`<br>`src/read_input.F:882,3089` |
| 37 | 보완 | `src/couple2baroclinic3D.F:121,134,137,139,141,144,146,148,151–152,154–155,157–165,213,215,228,253,255,267,280,282,284–285,288–289,499,501–512`<br>`src/read_input.F:882,3089` |
| 38 | 이상 없음 | `docs/technical_reference/input_files/fortrotm.rst:10,21–22`<br>`src/mesh.F:4369,4371,4374` |
| 39 | 이상 없음 | `docs/technical_reference/input_files/fortrotm.rst:24,26`<br>`src/mesh.F:4382–4383,4393` |
| 40 | 이상 없음 | `docs/technical_reference/input_files/fortrotm.rst:28,30`<br>`src/mesh.F:4394–4395,4403` |
| 41 | 보완 | `docs/technical_reference/input_files/fortrotm.rst:32,34–36`<br>`src/mesh.F:4404–4406,4414–4418,4773–4775,4777,4791–4793,4795` |
| 42 | 이상 없음 | `docs/technical_reference/input_files/elev_stat151.rst:6,13,15,21`<br>`src/read_input.F:3690,3698,3700–3702,5986,5988,5993–5994,5996–5999` |
| 43 | 이상 없음 | `docs/technical_reference/input_files/vel_stat151.rst:6,13,15,21`<br>`src/read_input.F:3814,3822,3824–3826,5986,5988,5993–5994,5996–5999` |
| 44 | 이상 없음 | `docs/technical_reference/input_files/conc_stat151.rst:6,13,15,21`<br>`src/read_input.F:3870,3942,3950,3952–3954,5986,5988,5993–5994,5996–5999` |
| 45 | 이상 없음 | `docs/technical_reference/input_files/met_stat151.rst:6,13,15,21`<br>`src/read_input.F:4000,4074,4082,4084–4086,5986,5988,5993–5994,5996–5999` |
| 46 | 보완 | `src/read_input.F:5988–5990` |
| 47 | 보완 | `docs/technical_reference/input_files/fort36.rst:6,25`<br>`src/cstart.F:835–838,859–863,875–878,940–941`<br>`docs/technical_reference/input_files/fort37.rst:6` |
| 48 | 보완 | `docs/technical_reference/input_files/fort37.rst:6,25`<br>`src/cstart.F:835–838,859–863,875–878,940–941`<br>`docs/technical_reference/input_files/fort36.rst:6` |
| 49 | 이상 없음 | `docs/technical_reference/input_files/fort38.rst:6,42`<br>`src/cstart.F:700–701,835,875–876,890–891,900,905,920,925`<br>`src/read_input.F:5621–5624` |

### manual-notes/06-parameter-definitions.md

| 초기 줄 | 결과 | 대조한 원문·참조 |
|---:|---|---|
| 9 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 33 | 이상 없음 | `src/read_input.F:4622–4623,5274–5275` |
| 39 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 40 | 이상 없음 | `docs/technical_reference/input_files/fort15.rst:138`<br>`src/read_input.F:5274–5275`<br>`src/vsmy.F:2875,2883,2885` |
| 41 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |

### manual-notes/14-fort14-grid-bathymetry-boundaries.md

| 초기 줄 | 결과 | 대조한 원문·참조 |
|---:|---|---|
| 9 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 31 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 32 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 33 | 보완 | `docs/technical_reference/input_files/fort14.rst:26`<br>`docs/technical_reference/parameter_definitions/index.rst:118`<br>`src/mesh.F:418`<br>`prep/read_global.F:154–158` |
| 34 | 이상 없음 | `docs/technical_reference/input_files/fort14.rst:37`<br>`docs/technical_reference/parameter_definitions/index.rst:33,38`<br>`src/mesh.F:460,463–466` |
| 35 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:28,38`<br>`src/mesh.F:2608,2627,2646` |
| 36 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:28,38`<br>`src/mesh.F:2608,2627,2640,2646` |
| 37 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:113`<br>`src/mesh.F:446,1405`<br>`src/boundaries.F:353–354` |
| 38 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:105,107`<br>`prep/read_global.F:224–230`<br>`src/mesh.F:446,551,554,2071–2100` |
| 39 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:63`<br>`docs/technical_reference/input_files/fort14.rst:38`<br>`src/mesh.F:482–487,490–491`<br>`prep/read_global.F:237,239–241,245,249–251,253` |
| 44 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 45 | 이상 없음 | `src/mesh.F:446,449,529,541–543` |
| 46 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |

### manual-notes/16-bathymetry-and-subgrid-paths.md

| 초기 줄 | 결과 | 대조한 원문·참조 |
|---:|---|---|
| 9 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 31 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 32 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 33 | 보완 | `docs/technical_reference/input_files/time_varying_bathymetry.rst:6,43`<br>`src/read_input.F:323,422,2380–2381`<br>`src/cstart.F:122,134` |
| 34 | 이상 없음 | `docs/technical_reference/input_files/time_varying_bathymetry.rst:11,17,24,45–46`<br>`src/cstart.F:125–126,148–150` |
| 35 | 이상 없음 | `docs/technical_reference/input_files/time_varying_bathymetry.rst:29,34,36,48–49`<br>`src/globalio.F:1676–1677,1682–1683` |
| 36 | 보완 | `docs/technical_reference/input_files/time_varying_bathymetry.rst:36`<br>`src/cstart.F:125–126,156`<br>`src/globalio.F:1680–1681`<br>`src/read_input.F:2393–2400,2404–2412`<br>`prep/prep.F:4069–4070,4075,4078` |
| 37 | 보완 | `docs/technical_reference/input_files/time_varying_bathymetry.rst:36,48`<br>`src/cstart.F:125–126,128–129,156`<br>`src/read_input.F:2393–2400,2404–2412,2421,2432`<br>`src/globalio.F:1680–1681`<br>`prep/prep.F:4069–4070,4075,4078` |
| 42 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 43 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 44 | 정정 | `src/subgridLookup.F:53–68,162,193,195–196,198–199,204–205,231–232,243,257–258,273,287,301–302,309,316–317,374–382,394`<br>`docs/tools/subgrid_adcirc_utility.rst:11–18` |
| 45 | 정정 | `src/subgridLookup.F:53–68,193,195–196,198–199,204–205,229,231–233,235–238,240,243–244,257–259,273,287,301–302,309,316–317,374–382`<br>`docs/tools/subgrid_adcirc_utility.rst:11–18` |
| 46 | 정정 | `src/subgridLookup.F:53–68,193,195–196,198–199,204–205,231–232,243,257–258,273–274,287–288,301–302,309,314,316–317,374–382`<br>`docs/tools/subgrid_adcirc_utility.rst:11–18` |
| 50 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 51 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 52 | 보완 | `src/mesh.F:153–157,745,747–749,867,869–872,887–888,890–891,907–909,943–945,952,1003–1004,1006,1009,1016–1017,1020,1143–1145,1181–1188,1211,1213–1215,1218–1229,1278–1292,1300–1301`<br>`src/nodalattr.F:625,638–639,642,650–651,653–654,657,733–734,753–754,756,758,765–766` |
| 53 | 보완 | `src/mesh.F:153–157,867,869–872,887–888,890–891,907–909,943–945,952,1003–1004,1006,1009,1016–1017,1020,1140,1143–1145,1151,1154,1166,1181–1188,1197,1211,1213–1215,1218–1229,1240,1261,1278–1292,1300–1301`<br>`src/nodalattr.F:625,638–639,642,650–651,653–654,657,733–734,753–754,756,758,765–766` |
| 54 | 정정 | `src/nodalattr.F:578–579,583,625,638–639,642,650–651,653–654,657,733–734,753–754,756,758,765–766`<br>`src/mesh.F:153–157,867,869–872,887–888,890–891,907–909,943–945,952,1003–1004,1006,1009,1016–1017,1020,1143–1145,1181–1188,1211,1213–1215,1218–1229,1278–1292,1300–1301` |

### manual-notes/17-boundary-and-forcing-inputs.md

| 초기 줄 | 결과 | 대조한 원문·참조 |
|---:|---|---|
| 9 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 32 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 33 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 34 | 보완 | `docs/technical_reference/input_files/fort19.rst:6`<br>`src/read_input.F:3427,3429`<br>`src/cstart.F:198,207` |
| 35 | 보완 | `docs/technical_reference/input_files/fort19.rst:20,36–42`<br>`src/cstart.F:198,206,208,210,213,233,239,248`<br>`src/hstart.F:884–885,888`<br>`docs/technical_reference/input_files/fort20.rst:20` |
| 39 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 40 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 41 | 보완 | `docs/technical_reference/input_files/fort20.rst:6`<br>`docs/technical_reference/parameter_definitions/index.rst:811`<br>`src/cstart.F:226`<br>`src/hstart.F:981,987,989` |
| 42 | 보완 | `docs/technical_reference/input_files/fort20.rst:20`<br>`src/cstart.F:208,210,213,233,238–239,241–242,248,250–251`<br>`docs/technical_reference/input_files/fort19.rst:20,36–42` |
| 61 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 62 | 이상 없음 | `docs/technical_reference/input_files/fort20.rst:17`<br>`src/cstart.F:241–243` |
| 63 | 이상 없음 | `prep/prep.F:3011–3012,3032,3041,3050,3068,3139,3152,3175` |
| 64 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |

### source-analysis/adcirc-bathymetry-input-foundation.md

| 초기 줄 | 결과 | 대조한 원문·참조 |
|---:|---|---|
| 11 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 65 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 66 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 67 | 보완 | `docs/technical_reference/input_files/time_varying_bathymetry.rst:6,43`<br>`src/read_input.F:323,422,2380–2381`<br>`src/cstart.F:122,134` |
| 68 | 이상 없음 | `docs/technical_reference/input_files/time_varying_bathymetry.rst:11,17,24,45–46`<br>`src/cstart.F:125–126,148–150` |
| 69 | 이상 없음 | `docs/technical_reference/input_files/time_varying_bathymetry.rst:29,34,36,48–49`<br>`src/globalio.F:1676–1677,1682–1683` |
| 70 | 보완 | `docs/technical_reference/input_files/time_varying_bathymetry.rst:36`<br>`src/cstart.F:125–126,156`<br>`src/globalio.F:1680–1681`<br>`src/read_input.F:2393–2400,2404–2412`<br>`prep/prep.F:4069–4070,4075,4078` |
| 71 | 보완 | `docs/technical_reference/input_files/time_varying_bathymetry.rst:36,48`<br>`src/cstart.F:125–126,128–129,156`<br>`src/read_input.F:2393–2400,2404–2412,2421,2432`<br>`src/globalio.F:1680–1681`<br>`prep/prep.F:4069–4070,4075,4078` |
| 84 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 85 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 86 | 정정 | `src/subgridLookup.F:53–68,162,193,195–196,198–199,204–205,231–232,243,257–258,273,287,301–302,309,316–317,374–382,394`<br>`docs/tools/subgrid_adcirc_utility.rst:11–18` |
| 87 | 정정 | `src/subgridLookup.F:53–68,193,195–196,198–199,204–205,229,231–233,235–238,240,243–244,257–259,273,287,301–302,309,316–317,374–382`<br>`docs/tools/subgrid_adcirc_utility.rst:11–18` |
| 88 | 정정 | `src/subgridLookup.F:53–68,193,195–196,198–199,204–205,231–232,243,257–258,273–274,287–288,301–302,309,314,316–317,374–382`<br>`docs/tools/subgrid_adcirc_utility.rst:11–18` |
| 92 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 93 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 94 | 보완 | `src/subgridLookup.F:195,198,204,273,287,301,316` |
| 95 | 이상 없음 | `src/subgridLookup.F:231–232,236,240,243,257–258` |
| 96 | 이상 없음 | `src/subgridLookup.F:375,379,382–384,391,394–398,400–401,403` |
| 97 | 이상 없음 | `src/subgridLookup.F:405,409–417,424,431–432,439,446–447` |
| 98 | 이상 없음 | `src/subgridLookup.F:405,409,455,458–460,470,473–475` |
| 102 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 103 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 104 | 보완 | `src/mesh.F:153–157,745,747–749,867,869–872,887–888,890–891,907–909,943–945,952,1003–1004,1006,1009,1016–1017,1020,1143–1145,1181–1188,1211,1213–1215,1218–1229,1278–1292,1300–1301`<br>`src/nodalattr.F:625,638–639,642,650–651,653–654,657,733–734,753–754,756,758,765–766` |
| 105 | 보완 | `src/mesh.F:153–157,867,869–872,887–888,890–891,907–909,943–945,952,1003–1004,1006,1009,1016–1017,1020,1140,1143–1145,1151,1154,1166,1181–1188,1197,1211,1213–1215,1218–1229,1240,1261,1278–1292,1300–1301`<br>`src/nodalattr.F:625,638–639,642,650–651,653–654,657,733–734,753–754,756,758,765–766` |
| 106 | 정정 | `src/nodalattr.F:578–579,583,625,638–639,642,650–651,653–654,657,733–734,753–754,756,758,765–766`<br>`src/mesh.F:153–157,867,869–872,887–888,890–891,907–909,943–945,952,1003–1004,1006,1009,1016–1017,1020,1143–1145,1181–1188,1211,1213–1215,1218–1229,1278–1292,1300–1301` |
| 115 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 116 | 정정 | `src/subgridLookup.F:53–68,204–205,232,243,258,273,287,301,316–317,319–325,374–375,394–398`<br>`src/nodalattr.F:2375–2388`<br>`src/gwce.F:1050–1053,1483–1495` |
| 117 | 정정 | `docs/tools/subgrid_adcirc_utility.rst:6,11–17`<br>`src/subgridLookup.F:193,195,198,204–205,232,243,375,410–416` |
| 118 | 보완 | 구조·참조 또는 같은 절의 원문 연결 |

### source-analysis/adcirc-fort-files-reference.md

| 초기 줄 | 결과 | 대조한 원문·참조 |
|---:|---|---|
| 12 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 39 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 40 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 41 | 이상 없음 | `docs/technical_reference/input_files/fortrotm.rst:10,21–22`<br>`src/mesh.F:4369,4371,4374` |
| 42 | 이상 없음 | `docs/technical_reference/input_files/fortrotm.rst:24,26`<br>`src/mesh.F:4382–4383,4393` |
| 43 | 이상 없음 | `docs/technical_reference/input_files/fortrotm.rst:28,30`<br>`src/mesh.F:4394–4395,4403` |
| 44 | 보완 | `docs/technical_reference/input_files/fortrotm.rst:32,34–36`<br>`src/mesh.F:4404–4406,4414–4418,4773–4775,4777,4791–4793,4795` |
| 45 | 이상 없음 | `docs/technical_reference/input_files/elev_stat151.rst:6,13,15,21`<br>`src/read_input.F:3690,3698,3700–3702,5986,5988,5993–5994,5996–5999` |
| 46 | 이상 없음 | `docs/technical_reference/input_files/vel_stat151.rst:6,13,15,21`<br>`src/read_input.F:3814,3822,3824–3826,5986,5988,5993–5994,5996–5999` |
| 47 | 이상 없음 | `docs/technical_reference/input_files/conc_stat151.rst:6,13,15,21`<br>`src/read_input.F:3870,3942,3950,3952–3954,5986,5988,5993–5994,5996–5999` |
| 48 | 이상 없음 | `docs/technical_reference/input_files/met_stat151.rst:6,13,15,21`<br>`src/read_input.F:4000,4074,4082,4084–4086,5986,5988,5993–5994,5996–5999` |
| 49 | 보완 | `src/read_input.F:5988–5990` |
| 69 | 이상 없음 | `src/read_input.F:6367–6368,6376–6379,6381,6389,6391–6392,6394,6400–6403,6405,6409,6468,6471,6476–6478,6482,6486`<br>`docs/technical_reference/input_files/fort24.rst:21,30,32`<br>`prep/prep.F:3638–3639,3646` |
| 70 | 이상 없음 | `src/owi_ice.F:132,158,367–371,374–376,379,381,385`<br>`docs/technical_reference/input_files/fort25.rst:3,8,21`<br>`src/read_input.F:1775–1776` |
| 175 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:858`<br>`src/netcdfio.F90:3887–3890,3897,3902–3903,3905,3911–3913` |
| 195 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 196 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 197 | 보완 | `docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst:93–96,308–309`<br>`src/wind.F:2041,2045–2046`<br>`src/owiwind_netcdf.F:262,265`<br>`docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:1–3,5,7–8,10,12` |
| 198 | 보완 | `docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:97–98,129`<br>`src/owiwind_netcdf.F:319–322` |
| 199 | 보완 | `docs/user_guide/running_adcirc/command_line_options.rst:11–12`<br>`src/owiwind_netcdf.F:262`<br>`src/wind.F:4184,4187,6258,6971,8021–8022,8030–8031,8243` |
| 208 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 209 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 210 | 보완 | `docs/technical_reference/input_files/fort22.rst:119,124,133`<br>`src/wind.F:1816–1818` |
| 211 | 보완 | `docs/technical_reference/input_files/fort22.rst:170`<br>`src/wind.F:3326–3328,3330–3332` |
| 212 | 보완 | `docs/technical_reference/input_files/fort22.rst:217,224–225`<br>`src/wind.F:3411–3412` |
| 213 | 보완 | `docs/technical_reference/input_files/fort22.rst:274`<br>`src/wind.F:3520–3524` |
| 214 | 보완 | `docs/technical_reference/input_files/fort22.rst:310,322`<br>`docs/technical_reference/parameter_definitions/index.rst:2002`<br>`src/wind.F:1155–1158,3652,3691` |
| 215 | 보완 | `docs/technical_reference/input_files/fort22.rst:214–215`<br>`prep/prep.F:3396,3406–3407,3416`<br>`src/wind.F:3400–3401` |
| 216 | 보완 | `docs/user_guide/running_adcirc/command_line_options.rst:11–12`<br>`src/wind.F:4184,4187,6258,6971,8021–8022,8030–8031,8243`<br>`src/owiwind_netcdf.F:262` |
| 217 | 보완 | `docs/technical_reference/input_files/fort22.rst:496`<br>`src/wind.F:6723–6726,6786–6787` |
| 218 | 보완 | `docs/technical_reference/input_files/fort22.rst:535,569–570`<br>`src/wind.F:7009–7012` |
| 219 | 보완 | `docs/technical_reference/input_files/fort22.rst:545,556`<br>`src/wind.F:7251–7253,7256,7264–7267` |
| 220 | 보완 | `docs/technical_reference/input_files/fort200.rst:27–29`<br>`src/wind.F:4196,4201` |
| 221 | 보완 | `docs/technical_reference/input_files/fort200.rst:81`<br>`src/wind.F:4113–4114,4187,4195–4196`<br>`src/io.F90:100–101` |
| 222 | 보완 | `docs/technical_reference/input_files/fort200.rst:84,101`<br>`src/wind.F:3411,4113–4114,4165,4209,4227–4228` |
| 223 | 보완 | `docs/technical_reference/input_files/fort200.rst:74,109,111`<br>`src/wind.F:4205` |
| 224 | 보완 | `docs/user_guide/running_adcirc/command_line_options.rst:11–12`<br>`src/wind.F:4184,4187,6258,6971,8021–8022,8030–8031,8243`<br>`src/owiwind_netcdf.F:262` |
| 231 | 이상 없음 | fort.15 대조 보고서 §1<br>입력 파일 대조 보고서 §1 |
| 232 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 233 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 234 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 235 | 이상 없음 | `docs/user_guide/model_configuration/model_parameters/im.rst:38,41,44,47,50,53,56,59,62,76–80,88–89,94–95`<br>`docs/technical_reference/input_files/fort15.rst:22`<br>`src/read_input.F:1149,1184–1191,1222–1224,1233,1267,1270–1271,1274,1277–1279,1286,1297,1323,1337,1347,1362–1363,1365–1366,1368,1370,1372–1373,1377–1378` |
| 236 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:387,389,391,393,395`<br>`docs/user_guide/model_configuration/model_parameters/nolibf.rst:47–51`<br>`src/read_input.F:1484–1485,1498,1503,1505,1507,1512–1515,3168,3196–3197`<br>`src/nodalattr.F:1850–1851,1855,2028` |
| 237 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:754`<br>`docs/technical_reference/input_files/fort15.rst:61`<br>`raw/manuals/wiki/markdown/Fort.15_file_format.md:81`<br>`raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/model-parameter-and-periodic-boundary-condition-file-fort-15.md:502`<br>`src/read_input.F:3315–3318,3326` |
| 238 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:497,499,501,503,505,507,509,511,521,525,531`<br>`docs/user_guide/model_configuration/model_parameters/tau0.rst:166,169,182–183,188–190,204–205,212–214,227,229,245,248,252–254,262–266,270–271,313–316`<br>`src/read_input.F:2500,2505–2506`<br>`src/nodalattr.F:1829–1832,1863–1864,1868,1909–1910,1914,1919,1966–1968,1977,1979,1981–1982,1989–1990,2004,2009,2149,2151–2153,2155,2158–2159,2190,2194–2195,2201–2202,2204–2205,2213,2215,2221,2229–2230`<br>`src/gwce.F:425–427,437–439,441–443,445` |
| 239 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:848,850,852,854,856,858,860,862,873,1460`<br>`src/read_input.F:3621,3627–3652,3688,4138,4163–4165,4386,4388,4395,4397,5863–5865,5871,5875`<br>`src/hstart.F:1562–1563,1571,1573` |
| 240 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:848,852,873,1456,1458,1460`<br>`src/read_input.F:3634–3636,3642,3646,3688,4138,4163–4165,4386,4388,4395,4397,5315,5319,5857–5884` |
| 241 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:1237,1239,1241,1261`<br>`src/read_input.F:1349–1350,1352–1353,4581`<br>`src/gwce.F:141,145,2000,2003–2004,2009` |
| 242 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:1653,1663,1673,1683`<br>`docs/technical_reference/input_files/fort15.rst:159,162,165,168,171–172`<br>`src/read_input.F:4622–4623,5528,5535–5536,5541–5545,5549–5553,5558–5561,5570–5571,5573–5576,5584–5586`<br>`src/cstart.F:839–840,863–864,879–880,892–893` |
| 243 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:1653,1663,1673,1683`<br>`docs/technical_reference/input_files/fort15.rst:159,162,165,168,171–172`<br>`src/read_input.F:4622–4623,5528,5535–5536,5558–5561,5570–5571,5583–5586`<br>`src/cstart.F:839–840,863–864,879–880,892–893` |
| 244 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:1653,1663,1673,1683`<br>`docs/technical_reference/input_files/fort15.rst:159,162,165,168,171–172`<br>`src/read_input.F:4622–4623,5528,5535–5536,5570–5571,5573–5576,5583–5586`<br>`src/cstart.F:839–840,863–864,879–880,892–893` |
| 245 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:1653,1663,1673,1683`<br>`docs/technical_reference/input_files/fort15.rst:159,162,165,168,171–172`<br>`src/read_input.F:4622–4623,5528,5535–5536,5585–5586,5621–5624`<br>`src/cstart.F:839–840,863–864,879–880,892–893` |
| 246 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:2869`<br>`src/read_input.F:242,499`<br>`src/constants.F90:64–70` |
| 247 | 이상 없음 | `src/read_input.F:333–334,593`<br>`src/constants.F90:119`<br>`docs/technical_reference/input_files/fort15.rst:206`<br>`docs/technical_reference/parameter_definitions/index.rst:2888` |
| 248 | 이상 없음 | `docs/technical_reference/input_files/fort15.rst:203`<br>`docs/user_guide/examples/alaskan_winter_storm_with_ice.rst:57,59`<br>`src/read_input.F:242–244,323,499`<br>`src/gwce.F:114` |
| 249 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:2989`<br>`src/read_input.F:257,563,567,574–586,4132,4276,4279–4280,4282–4283,4285` |
| 250 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:2989,2994`<br>`src/read_input.F:257,564,567,574–586,4132,4276,4279–4280,4282–4283,4285` |
| 251 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:2989,2999`<br>`src/read_input.F:257,565,567,574–586,4132,4276,4279–4280,4282–4283,4285` |
| 252 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:2989,3004`<br>`src/read_input.F:257,566–567,574–586,4132,4276,4279–4280,4282–4283,4285` |
| 253 | 이상 없음 | `docs/user_guide/model_configuration/meteorological_forcing/moteorological_parameter_line.rst:86–87,93,111,117`<br>`src/read_input.F:2568–2569,2575–2582`<br>`src/wind.F:53`<br>`docs/technical_reference/parameter_definitions/index.rst:609` |
| 254 | 이상 없음 | `docs/user_guide/model_configuration/meteorological_forcing/moteorological_parameter_line.rst:278–279`<br>`src/read_input.F:2598–2608`<br>`src/wind.F:53`<br>`docs/technical_reference/parameter_definitions/index.rst:609` |
| 255 | 이상 없음 | `docs/user_guide/model_configuration/meteorological_forcing/moteorological_parameter_line.rst:348,350–351`<br>`src/read_input.F:1782–1784,1792,2316–2317,2322–2323,2328,2562–2563,2568,2600,2652,2660,2808`<br>`src/wind.F:52–53,55–56,59–60`<br>`docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst:275–276` |
| 256 | 이상 없음 | `docs/user_guide/model_configuration/meteorological_forcing/moteorological_parameter_line.rst:740–741`<br>`src/read_input.F:2660,2663,2760–2774`<br>`src/wind.F:53`<br>`docs/user_guide/model_configuration/meteorological_forcing/wtiminc.rst:17` |
| 257 | 보완 | `docs/technical_reference/input_files/fort14.rst:26`<br>`docs/technical_reference/parameter_definitions/index.rst:118`<br>`src/mesh.F:418`<br>`prep/read_global.F:154–158` |
| 258 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:28,38`<br>`src/mesh.F:2608,2627,2646` |
| 259 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:28,38`<br>`src/mesh.F:2608,2627,2640,2646` |
| 260 | 보완 | `docs/technical_reference/input_files/fort11.rst:20,31,42,53`<br>`src/read_input.F:3086,3091,3093–3095` |
| 261 | 보완 | `docs/technical_reference/input_files/fort19.rst:6`<br>`src/read_input.F:3427,3429`<br>`src/cstart.F:198,207` |
| 262 | 보완 | `docs/technical_reference/input_files/fort19.rst:20,36–42`<br>`src/cstart.F:198,206,208,210,213,233,239,248`<br>`src/hstart.F:884–885,888`<br>`docs/technical_reference/input_files/fort20.rst:20` |
| 263 | 보완 | `docs/technical_reference/input_files/fort20.rst:6`<br>`docs/technical_reference/parameter_definitions/index.rst:811`<br>`src/cstart.F:226`<br>`src/hstart.F:981,987,989` |
| 264 | 보완 | `docs/technical_reference/input_files/fort20.rst:20`<br>`src/cstart.F:208,210,213,233,238–239,241–242,248,250–251`<br>`docs/technical_reference/input_files/fort19.rst:20,36–42` |
| 265 | 이상 없음 | `docs/technical_reference/input_files/fort24.rst:18,30`<br>`src/read_input.F:6468` |
| 266 | 이상 없음 | `docs/technical_reference/input_files/fort24.rst:21,30,32`<br>`src/read_input.F:6471,6477–6478,6482,6486` |
| 267 | 이상 없음 | `docs/technical_reference/input_files/fort13.rst:64,68,70`<br>`raw/manuals/wiki/markdown/Fort.13_file.md:180`<br>`src/nodalattr.F:497,1214–1216,1371–1374,1909–1910,1914,1919`<br>`src/gwce.F:1740–1741` |
| 268 | 보완 | `docs/technical_reference/input_files/fort13.rst:111,115,117,174,182,189`<br>`src/nodalattr.F:506,1224–1226,1387,1850–1851,2423,2435` |
| 269 | 이상 없음 | `docs/technical_reference/input_files/fort13.rst:153`<br>`raw/manuals/wiki/markdown/Fort.13_file.md:79`<br>`src/nodalattr.F:1096,1244` |
| 270 | 보완 | `docs/technical_reference/input_files/fort13.rst:111,174,182,189`<br>`src/nodalattr.F:1850–1851,2376,2379,2393,2406–2408,2414–2415,2422–2423,2435` |
| 271 | 보완 | `docs/technical_reference/input_files/fort13.rst:111,174,182,189,193,195,197`<br>`src/nodalattr.F:510,1262–1264,1850–1851,2376,2423,2433,2435` |
| 272 | 보완 | `docs/technical_reference/input_files/fort13.rst:231,234,238,240,242`<br>`src/nodalattr.F:513,1273–1280,1456–1457,2114` |
| 273 | 보완 | `docs/technical_reference/input_files/fort13.rst:238`<br>`raw/manuals/wiki/markdown/Fort.13_file.md:101`<br>`docs/technical_reference/parameter_definitions/index.rst:743`<br>`src/gwce.F:828,831–834,840` |
| 274 | 이상 없음 | `docs/technical_reference/input_files/fort13.rst:283,285,287,289,291`<br>`raw/manuals/wiki/markdown/Fort.13_file.md:138,141`<br>`src/nodalattr.F:520,1314–1316`<br>`src/cstart.F:1156,1182–1184,1188` |
| 275 | 보완 | `docs/technical_reference/input_files/fort36.rst:6,25`<br>`src/cstart.F:835–838,859–863,875–878,940–941`<br>`docs/technical_reference/input_files/fort37.rst:6` |
| 276 | 보완 | `docs/technical_reference/input_files/fort37.rst:6,25`<br>`src/cstart.F:835–838,859–863,875–878,940–941`<br>`docs/technical_reference/input_files/fort36.rst:6` |
| 277 | 이상 없음 | `docs/technical_reference/input_files/fort39.rst:6,30`<br>`src/mesh.F:1405–1406,1422`<br>`src/cstart.F:700–701,961–964`<br>`docs/technical_reference/parameter_definitions/index.rst:113` |
| 278 | 이상 없음 | `docs/technical_reference/input_files/fort39.rst:25`<br>`src/cstart.F:863–864,965–966` |
| 279 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:113`<br>`src/mesh.F:446,1405`<br>`src/boundaries.F:353–354` |
| 280 | 보완 | `docs/technical_reference/input_files/time_varying_bathymetry.rst:6,43`<br>`src/read_input.F:323,422,2380–2381`<br>`src/cstart.F:122,134` |
| 281 | 이상 없음 | `docs/technical_reference/input_files/time_varying_weirs.rst:3`<br>`src/global.F:324`<br>`src/weir_boundary.F90:997–998` |
| 282 | 이상 없음 | `docs/technical_reference/input_files/time_varying_weirs.rst:40,45,49`<br>`src/weir_boundary.F90:1133–1136,1140–1143,1433–1444` |
| 283 | 이상 없음 | `docs/technical_reference/input_files/time_varying_weirs.rst:77–80`<br>`src/weir_boundary.F90:1095–1098,1104–1110,1117–1118` |
| 284 | 이상 없음 | `raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/schedule-file/index.md:415–418`<br>`src/weir_boundary.F90:154–158,1328–1331,1359–1362,1382–1386,1439–1444`<br>`docs/technical_reference/input_files/time_varying_weirs.rst:50` |
| 285 | 보완 | `docs/technical_reference/input_files/fortrotm.rst:32,34–36`<br>`src/mesh.F:4404–4406,4414–4418,4773–4775,4777,4791–4793,4795` |
| 286 | 보완 | `docs/user_guide/running_adcirc/command_line_options.rst:41–42,44,47,50,74`<br>`src/sizes.F:234,236,238,240,249,271,287` |
| 287 | 보완 | `docs/user_guide/running_adcirc/command_line_options.rst:41,44–45,47,50,74`<br>`src/sizes.F:234,249–250,252,271,287` |
| 288 | 보완 | `docs/user_guide/running_adcirc/command_line_options.rst:41,44,47–48,50,74`<br>`src/sizes.F:234,249,271,273,275,277,287` |
| 289 | 보완 | `docs/user_guide/running_adcirc/command_line_options.rst:41,44,47,50–51,74`<br>`src/sizes.F:234,249,271,287–288,290` |
| 290 | 보완 | `docs/technical_reference/input_files/fort13.rst:238`<br>`raw/manuals/wiki/markdown/Fort.13_file.md:101`<br>`src/gwce.F:828,831–834,837–838,840`<br>`docs/technical_reference/parameter_definitions/index.rst:743` |
| 291 | 이상 없음 | `docs/technical_reference/input_files/fort13.rst:249,257`<br>`src/gwce.F:3129–3135,3185–3186,3194–3195,3204,3206,3210,3216–3217` |
| 292 | 이상 없음 | `raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/nws-values-table/index.md:410`<br>`src/read_input.F:1775–1776,1829–1830,2244,2316,2322–2323,2328`<br>`src/wind.F:1811,2153` |
| 293 | 이상 없음 | `raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/nws-values-table/index.md:411`<br>`src/read_input.F:1775–1776,1829–1830,2244,2316,2322–2323,2328`<br>`src/wind.F:1815,1817,2203,2207` |
| 294 | 이상 없음 | `raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/nws-values-table/index.md:416`<br>`src/read_input.F:1775–1776,1829–1830,2244,2316,2322–2323,2328`<br>`src/wind.F:1892,3652` |
| 295 | 이상 없음 | `docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst:141`<br>`src/read_input.F:1775–1776,1829–1830,2271,2316,2322–2323,2328`<br>`src/wind.F:1811,2153` |
| 296 | 이상 없음 | `docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst:147`<br>`src/read_input.F:1775–1776,1829–1830,2271,2316,2322–2323,2328`<br>`src/wind.F:1815,1817,2203,2207` |
| 297 | 이상 없음 | `docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst:177`<br>`src/read_input.F:1775–1776,1829–1830,2271,2316,2322–2323,2328`<br>`src/wind.F:1892,3652` |
| 298 | 이상 없음 | `raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/nws-values-table/index.md:410`<br>`src/read_input.F:1775–1776,1829–1830,2279,2316,2322–2323,2328`<br>`src/wind.F:1811,2153` |
| 299 | 이상 없음 | `raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/nws-values-table/index.md:411`<br>`src/read_input.F:1775–1776,1829–1830,2279,2316,2322–2323,2328`<br>`src/wind.F:1815,1817,2203,2207` |
| 300 | 이상 없음 | `raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/nws-values-table/index.md:416`<br>`src/read_input.F:1775–1776,1829–1830,2279,2316,2322–2323,2328`<br>`src/wind.F:1892,3652` |
| 301 | 이상 없음 | `raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/nws-values-table/index.md:408`<br>`src/cstart.F:312–313` |
| 302 | 보완 | `docs/technical_reference/input_files/fort22.rst:119,124,133`<br>`src/wind.F:1816–1818` |
| 303 | 보완 | `docs/technical_reference/input_files/fort22.rst:170`<br>`src/wind.F:3326–3328,3330–3332` |
| 304 | 보완 | `docs/technical_reference/input_files/fort22.rst:217,224–225`<br>`src/wind.F:3411–3412` |
| 305 | 보완 | `docs/technical_reference/input_files/fort22.rst:274`<br>`src/wind.F:3520–3524` |
| 306 | 이상 없음 | `docs/technical_reference/input_files/fort22.rst:342,353`<br>`src/nws08.F90:20–26,946,1047–1050,1052–1053` |
| 307 | 이상 없음 | `docs/technical_reference/input_files/fort22.rst:330,333`<br>`src/nws08.F90:20–21,37–40,531,562` |
| 308 | 보완 | `docs/user_guide/running_adcirc/command_line_options.rst:11–12`<br>`src/wind.F:4184,4187,6258,6971,8021–8022,8030–8031,8243`<br>`src/owiwind_netcdf.F:262` |
| 309 | 보완 | `docs/technical_reference/input_files/fort22.rst:496`<br>`src/wind.F:6723–6726,6786–6787` |
| 310 | 보완 | `docs/technical_reference/input_files/fort22.rst:535,569–570`<br>`src/wind.F:7009–7012` |
| 311 | 보완 | `docs/technical_reference/input_files/fort22.rst:545,556`<br>`src/wind.F:7251–7253,7256,7264–7267` |
| 312 | 보완 | `docs/technical_reference/input_files/fort200.rst:27–29`<br>`src/wind.F:4196,4201` |
| 313 | 보완 | `docs/technical_reference/input_files/fort200.rst:81`<br>`src/wind.F:4113–4114,4187,4195–4196`<br>`src/io.F90:100–101` |
| 314 | 보완 | `docs/technical_reference/input_files/fort200.rst:84,101`<br>`src/wind.F:3411,4113–4114,4165,4209,4227–4228` |
| 315 | 보완 | `docs/technical_reference/input_files/fort200.rst:74,109,111`<br>`src/wind.F:4205` |
| 316 | 보완 | `docs/user_guide/running_adcirc/command_line_options.rst:11–12`<br>`src/wind.F:4184,4187,6258,6971,8021–8022,8030–8031,8243`<br>`src/owiwind_netcdf.F:262` |
| 317 | 이상 없음 | `docs/user_guide/model_configuration/meteorological_forcing/nws12.rst:108–113`<br>`src/owiwind.F:940–941,943` |
| 318 | 보완 | `docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst:93–96,308–309`<br>`src/wind.F:2041,2045–2046`<br>`src/owiwind_netcdf.F:262,265`<br>`docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:1–3,5,7–8,10,12` |
| 319 | 보완 | `docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:97–98,129`<br>`src/owiwind_netcdf.F:319–322` |
| 320 | 보완 | `docs/user_guide/running_adcirc/command_line_options.rst:11–12`<br>`src/owiwind_netcdf.F:262`<br>`src/wind.F:4184,4187,6258,6971,8021–8022,8030–8031,8243` |
| 321 | 이상 없음 | `docs/technical_reference/input_files/fort22.rst:444`<br>`src/wind.F:8259–8260` |
| 322 | 이상 없음 | `docs/technical_reference/input_files/fort22.rst:436,466`<br>`src/wind.F:9262,9269–9277` |
| 323 | 보완 | `docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst:312`<br>`src/wind.F:2014–2016,2028,8235,8238–8240` |
| 324 | 보완 | `docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst:312`<br>`src/wind.F:2014–2016,2028,8235,8238–8240` |
| 325 | 보완 | `docs/user_guide/running_adcirc/command_line_options.rst:11–12`<br>`src/wind.F:4184,4187,6258,6971,8021–8022,8030–8031,8243`<br>`src/owiwind_netcdf.F:262` |
| 326 | 보완 | `docs/technical_reference/input_files/fort22.rst:310,322`<br>`docs/technical_reference/parameter_definitions/index.rst:2002`<br>`src/wind.F:1155–1158,3652,3691` |
| 327 | 이상 없음 | `docs/technical_reference/input_files/fort22.rst:222,258`<br>`docs/technical_reference/input_files/fort200.rst:93`<br>`src/wind.F:119–122,537` |
| 328 | 이상 없음 | `docs/technical_reference/input_files/fort25.rst:3,21`<br>`src/owi_ice.F:132,158` |
| 329 | 이상 없음 | `docs/technical_reference/input_files/fort25.rst:8`<br>`src/read_input.F:1775–1776` |
| 330 | 이상 없음 | `docs/technical_reference/input_files/fort25.rst:21`<br>`src/owi_ice.F:364–381,385` |
| 331 | 보완 | `docs/technical_reference/input_files/fort25.rst:7,43,47`<br>`src/wind.F:124–127,132,736,767–778` |
| 332 | 보완 | `docs/technical_reference/input_files/fort25.rst:39,47,49`<br>`src/wind.F:761–763` |
| 333 | 이상 없음 | `docs/user_guide/model_configuration/meteorological_forcing/wind_stress.rst:65`<br>`src/nodalattr.F:2950` |
| 334 | 이상 없음 | `docs/technical_reference/input_files/fort23.rst:6`<br>`src/cstart.F:312–313,317–318`<br>`src/hstart.F:1466–1467,1471,1476–1477`<br>`src/read_input.F:2271,2274` |
| 335 | 보완 | `docs/technical_reference/input_files/fort6768.rst:33–40,64–68,70–76`<br>`src/hstart.F:526–527,537–540,542,601–607,612–614,616–618,2726–2728`<br>`src/harm.F:2057–2060` |
| 336 | 보완 | `docs/technical_reference/input_files/fort6768.rst:46–53`<br>`src/hstart.F:26,547–564` |
| 337 | 보완 | `docs/technical_reference/input_files/fort6768.rst:55,77,79,81,83,88,136`<br>`src/hstart.F:568,633,637,639,641,643,657–658,663–664,666–667`<br>`src/read_input.F:1190–1191,1267,1270,1274,1277`<br>`src/harm.F:1760–1761,1763,1771` |
| 338 | 보완 | `docs/technical_reference/input_files/fort6768.rst:33–40,64–68,70–76`<br>`docs/technical_reference/parameter_definitions/index.rst:2529,2534,2540`<br>`src/hstart.F:526–527,537–540,542,601–607,612–614,616–618,2726–2728`<br>`src/harm.F:2057–2060` |
| 339 | 보완 | `docs/technical_reference/input_files/fort6768.rst:33–40,64–68,70–76,78,80,82,84`<br>`src/hstart.F:526–527,537–540,542,601–607,612–614,616–618,2726–2728,3101`<br>`src/harm.F:2057–2060` |
| 340 | 보완 | `docs/technical_reference/input_files/fort6768.rst:55,77–84,88,136`<br>`src/hstart.F:568,633,637–645,657–658,663–664,666–667`<br>`src/read_input.F:1267,1270,1274,1277`<br>`src/harm.F:1760–1761,1763,1771` |
| 341 | 보완 | `docs/technical_reference/input_files/fort6768.rst:55,77,79,81,83,88–89,136`<br>`src/hstart.F:568,633,637,639,641,643,657–658,663–664,666–667`<br>`src/read_input.F:1267,1270,1274,1277`<br>`src/harm.F:1760–1761,1763,1771` |
| 342 | 보완 | `docs/technical_reference/input_files/fort6768.rst:108,111,115,118,122,125,129,132`<br>`src/harm.F:1732–1733,1736,1739–1740,1746–1747,1750,1753–1754` |
| 343 | 보완 | `docs/technical_reference/input_files/fort6768.rst:55,77,79,81,83,88,136–137,139,142–143`<br>`src/harm.F:1760–1763,1765,1767,1771,1773,1775,1777,1779`<br>`src/hstart.F:568,633,637,639,641,643,657–658,663–664,666–667`<br>`src/read_input.F:1267,1270,1274,1277` |
| 344 | 보완 | `docs/technical_reference/input_files/fort6768.rst:16,152`<br>`src/hstart.F:714–718,721,725,727–732,734–735,737–740,744–747` |
| 345 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:63`<br>`docs/technical_reference/input_files/fort14.rst:38`<br>`src/mesh.F:482–487,490–491`<br>`prep/read_global.F:237,239–241,245,249–251,253` |
| 346 | 보완 | `docs/technical_reference/input_files/fort22.rst:214–215`<br>`prep/prep.F:3396,3406–3407,3416`<br>`src/wind.F:3400–3401` |
| 347 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 348 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 349 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:228,233`<br>`src/read_input.F:963–964`<br>`src/global.F:463` |
| 350 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:250`<br>`src/read_input.F:816,818,990` |
| 351 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:308`<br>`src/read_input.F:1037,1039,1045` |
| 352 | 이상 없음 | `docs/user_guide/model_configuration/model_parameters/ics.rst:74`<br>`src/read_input.F:1111–1113,1117–1118` |
| 353 | 이상 없음 | `docs/technical_reference/input_files/fort15.rst:23`<br>`src/read_input.F:902,931–932,1383–1385` |
| 354 | 이상 없음 | `docs/technical_reference/input_files/fort15.rst:54`<br>`src/read_input.F:1520,1531,1534–1536,1541,1545–1546`<br>`docs/user_guide/model_configuration/model_parameters/nolifa.rst:50`<br>`docs/technical_reference/parameter_definitions/index.rst:400` |
| 355 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:342`<br>`src/read_input.F:1698–1699,1724–1725` |
| 356 | 이상 없음 | `docs/technical_reference/input_files/fort15.rst:44`<br>`src/read_input.F:2908,2910` |
| 357 | 이상 없음 | `docs/technical_reference/input_files/fort15.rst:59–60`<br>`docs/technical_reference/parameter_definitions/index.rst:743`<br>`src/read_input.F:3282–3283,3287–3290` |
| 358 | 이상 없음 | `docs/technical_reference/input_files/fort15.rst:87`<br>`src/read_input.F:3585–3587` |
| 359 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:581`<br>`src/read_input.F:1775–1776,1829–1830,2562` |
| 360 | 보완 | `docs/technical_reference/input_files/fort25.rst:8`<br>`src/read_input.F:2746–2749,2751–2753,2768–2770,2820` |
| 361 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:631`<br>`src/timestep.F:257,301,347` |
| 362 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:475`<br>`src/timestep.F:245,314–316,323` |
| 363 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:864,1173`<br>`src/read_input.F:3661–3662,3787–3788,4046–4047,4177–4178,4251,4330,4408,4474–4477` |
| 364 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:3014,3019`<br>`src/read_input.F:3698,3822,3950,4082` |
| 365 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:885`<br>`src/read_input.F:6138,6143,6148–6149` |
| 366 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:938,942,1098`<br>`docs/technical_reference/output_files/fort83.rst:1`<br>`src/read_input.F:3883,3888–3889,3893,3898,4315–4320` |
| 367 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:1257`<br>`src/gwce.F:150`<br>`src/itpackv.F:223–224,232,876,880–881,883–886` |
| 368 | 정정 | `docs/technical_reference/parameter_definitions/index.rst:1201,1205,1209,1213`<br>`src/harm.F:401,403–405,409,413,416–417,421,433,441,453,461,473` |
| 369 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:1287,1291`<br>`src/vsmy.F:942,949–950,997,1002,1008–1015`<br>`src/nodalattr.F:2555–2557,2559,2570–2572` |
| 370 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:1301`<br>`src/nodalattr.F:1098` |
| 371 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:1374`<br>`src/read_input.F:5254–5263` |
| 372 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:1625`<br>`src/read_input.F:5535–5536,5550–5553` |
| 373 | 이상 없음 | `docs/technical_reference/input_files/fort15.rst:157,174`<br>`src/read_input.F:1274,1277,1279,1372–1373,4622–4623,5528–5529,5721–5725` |
| 374 | 정정 | `docs/technical_reference/parameter_definitions/index.rst:1688`<br>`docs/technical_reference/input_files/fort15.rst:171`<br>`src/read_input.F:5621–5624` |
| 375 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:1699`<br>`src/read_input.F:5637–5638,5641–5642`<br>`src/cstart.F:485,490` |
| 376 | 이상 없음 | `docs/technical_reference/input_files/fort15.rst:171–173`<br>`src/read_input.F:5621–5624` |
| 377 | 이상 없음 | `docs/technical_reference/input_files/fort15.rst:181–182`<br>`src/read_input.F:5783–5785,5787`<br>`prep/pre_global.F:218` |
| 378 | 이상 없음 | `docs/technical_reference/input_files/fort15.rst:159,162,165,168`<br>`src/read_input.F:5543–5544,5550–5552,5559–5560,5574–5575,5584–5585` |
| 379 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:1475,1539`<br>`src/read_input.F:5315,5412` |
| 380 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:1486`<br>`docs/technical_reference/input_files/fort15.rst:141,146,151`<br>`src/read_input.F:5358–5359,5403–5404,5446–5447` |
| 381 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:1504–1505`<br>`docs/technical_reference/input_files/fort15.rst:144`<br>`src/read_input.F:5369,5373,5904` |
| 382 | 이상 없음 | `docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst:331`<br>`src/read_input.F:1782–1784,2568,2693`<br>`src/wind.F:1472–1473,1914–1916,2622–2624` |
| 383 | 이상 없음 | `docs/user_guide/model_configuration/meteorological_forcing/moteorological_parameter_line.rst:838–839`<br>`src/read_input.F:2322–2323,2327,2599,2605–2606` |
| 384 | 이상 없음 | `docs/user_guide/model_configuration/meteorological_forcing/moteorological_parameter_line.rst:44,50,56`<br>`src/read_input.F:2289–2291` |
| 385 | 이상 없음 | `src/read_input.F:240,477–478` |
| 386 | 이상 없음 | `src/read_input.F:242,244,499`<br>`src/owiwind.F:100,232` |
| 387 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:2934`<br>`src/subdomain.F:44`<br>`src/read_input.F:489–492,494`<br>`src/global.F:1601–1635`<br>`src/cstart.F:105–117`<br>`prep/subprep.F:42–100` |
| 388 | 이상 없음 | `src/read_input.F:246–247,638`<br>`src/global.F:697` |
| 389 | 이상 없음 | `src/read_input.F:246–247,638`<br>`src/global.F:698` |
| 390 | 이상 없음 | `src/read_input.F:246,250,638`<br>`src/global.F:804` |
| 391 | 이상 없음 | `src/read_input.F:246,250,638`<br>`src/global.F:805` |
| 392 | 이상 없음 | `src/read_input.F:246,250,638`<br>`src/global.F:807` |
| 393 | 이상 없음 | `src/read_input.F:246,250,638`<br>`src/global.F:807` |
| 394 | 이상 없음 | `src/read_input.F:253–254,789`<br>`src/weir_boundary.F90:52,260` |
| 395 | 이상 없음 | `src/read_input.F:253–254,789`<br>`src/weir_boundary.F90:53,259` |
| 396 | 이상 없음 | `src/read_input.F:253–254,789`<br>`src/weir_boundary.F90:54` |
| 397 | 이상 없음 | `src/read_input.F:253,255,789`<br>`src/weir_boundary.F90:55` |
| 398 | 이상 없음 | `src/read_input.F:253,255,789`<br>`src/weir_boundary.F90:56` |
| 399 | 이상 없음 | `src/read_input.F:259,261,743`<br>`src/wind.F:241` |
| 400 | 이상 없음 | `docs/user_guide/model_configuration/tides/ali_dispersion_conrtol.rst:36–37`<br>`src/read_input.F:858,1362,1365,1368–1369` |
| 401 | 이상 없음 | `docs/user_guide/special_features/adcirc2d_plus.rst:94`<br>`src/read_input.F:926–928` |
| 402 | 이상 없음 | `src/read_input.F:277,678`<br>`src/subgridLookup.F:41` |
| 403 | 이상 없음 | `src/read_input.F:277,678` |
| 404 | 이상 없음 | `src/read_input.F:277,678` |
| 405 | 이상 없음 | `src/read_input.F:277–278,678`<br>`src/subgridLookup.F:47` |
| 406 | 이상 없음 | `src/read_input.F:280,553`<br>`src/wind.F:282` |
| 407 | 이상 없음 | `src/read_input.F:283,514`<br>`src/global.F:529` |
| 408 | 이상 없음 | `src/read_input.F:283,514` |
| 409 | 이상 없음 | `src/read_input.F:283,514` |
| 410 | 이상 없음 | `src/read_input.F:283–284,514` |
| 411 | 이상 없음 | `src/read_input.F:222,299,936` |
| 412 | 이상 없음 | `src/read_input.F:223,299,936` |
| 413 | 이상 없음 | `src/read_input.F:224,299–300,936` |
| 414 | 이상 없음 | `src/read_input.F:225,299–300,936` |
| 415 | 이상 없음 | `src/read_input.F:226,299–300,936` |
| 416 | 이상 없음 | `src/read_input.F:227,299,301,936` |
| 417 | 이상 없음 | `src/read_input.F:228,299,301,936` |
| 418 | 이상 없음 | `src/read_input.F:229,299,301,936` |
| 419 | 이상 없음 | `src/read_input.F:230,299,301,936` |
| 420 | 이상 없음 | `docs/user_guide/model_configuration/physics_parameters/horizontal_eddy_viscosity.rst:64–66,86–87`<br>`src/global.F:694`<br>`src/read_input.F:703,720–721` |
| 421 | 이상 없음 | `src/read_input.F:333–334,593`<br>`src/global.F:71` |
| 422 | 이상 없음 | `src/read_input.F:333–334,593`<br>`src/constants.F90:122` |
| 423 | 이상 없음 | `src/global_3dvs.F:370,379`<br>`src/read_input.F:609` |
| 424 | 이상 없음 | `src/global_3dvs.F:371,379–380`<br>`src/read_input.F:609` |
| 425 | 이상 없음 | `src/global_3dvs.F:372,379–380`<br>`src/read_input.F:609` |
| 426 | 이상 없음 | `src/global_3dvs.F:373,379,381`<br>`src/read_input.F:609` |
| 427 | 이상 없음 | `src/global_3dvs.F:374,379,381`<br>`src/read_input.F:609` |
| 428 | 이상 없음 | `src/global_3dvs.F:375,379,382`<br>`src/read_input.F:609` |
| 429 | 이상 없음 | `src/global_3dvs.F:376,379,382`<br>`src/read_input.F:609` |
| 430 | 이상 없음 | `src/global_3dvs.F:377,379,383`<br>`src/read_input.F:609` |
| 431 | 이상 없음 | `src/global_3dvs.F:378–379,385`<br>`src/read_input.F:609` |
| 432 | 이상 없음 | `src/nws08.F90:333–334,353,366` |
| 433 | 이상 없음 | `src/nws08.F90:333,335,354,366` |
| 434 | 이상 없음 | `src/nws08.F90:333,336,355,366` |
| 435 | 이상 없음 | `src/nws08.F90:333,337,356,366` |
| 436 | 이상 없음 | `src/nws08.F90:333,338,357,366` |
| 437 | 이상 없음 | `src/nws08.F90:333,339,358,366` |
| 438 | 이상 없음 | `src/nws08.F90:333,340,359,366,411` |
| 439 | 이상 없음 | `src/nws08.F90:333,341,360,366` |
| 440 | 이상 없음 | `src/nws08.F90:333,342,361,366` |
| 441 | 이상 없음 | `src/nws08.F90:333,343,362,366` |
| 442 | 이상 없음 | `src/nodalattr.F:1081,1092–1093` |
| 443 | 이상 없음 | `src/nodalattr.F:1081,1109–1111` |
| 444 | 이상 없음 | `src/nodalattr.F:1081,1130–1131` |
| 445 | 이상 없음 | `src/nodalattr.F:1081,1132–1133` |
| 446 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:1447`<br>`docs/technical_reference/input_files/fort15.rst:138`<br>`src/read_input.F:5274–5275` |
| 447 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:266`<br>`src/read_input.F:809–810,818,830,985,991–992`<br>`src/timestep.F:1307,1310,1313` |
| 448 | 이상 없음 | `docs/technical_reference/input_files/fort15.rst:94`<br>`src/read_input.F:5988–5990` |
| 449 | 보완 | `docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst:309`<br>`docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:208,210,214`<br>`src/read_input.F:273–274,2952–2953` |
| 450 | 이상 없음 | `src/nodalattr.F:1829,1832,1977,1979,1981–1982,1989–1990`<br>`src/read_input.F:2505–2506` |
| 451 | 이상 없음 | `src/read_input.F:3627`<br>`docs/technical_reference/parameter_definitions/index.rst:850,858`<br>`src/hstart.F:1562–1563,1571`<br>`src/netcdfio.F90:3881–3976` |
| 452 | 이상 없음 | `src/read_input.F:4522,4535,4553,4556–4558`<br>`src/hstart.F:238–240`<br>`src/timestep.F:1196,1200`<br>`src/write_output.F:4986,4989,5010` |
| 453 | 이상 없음 | `docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst:298–299`<br>`docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:208,214`<br>`src/read_input.F:1769,1782–1784,1792`<br>`src/hstart.F:240,1439–1448`<br>`src/wind.F:2085,2800–2803,2807` |
| 454 | 정정 | `docs/technical_reference/parameter_definitions/index.rst:513`<br>`docs/user_guide/model_configuration/model_parameters/tau0.rst:282,286,289–290` |
| 455 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:499,501`<br>`docs/user_guide/model_configuration/model_parameters/tau0.rst:188–190`<br>`src/nodalattr.F:1909–1910,1912` |
| 456 | 정정 | `docs/technical_reference/parameter_definitions/index.rst:2854`<br>`src/read_input.F:4804,4806,4808–4809,4811–4812,4814`<br>`src/lib/mod_datetime.f90:1258–1259,1279`<br>`src/lib/mod_strftime.f90:68–85`<br>`src/tests/datetime_tests.f90:427–443` |
| 457 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:1692`<br>`docs/technical_reference/input_files/fort38.rst:45–48`<br>`src/cstart.F:900,905–910,920,925–929`<br>`src/transport.F:466–469,495–497,1076–1080` |
| 458 | 이상 없음 | `src/rs2.F:89,93,95–96,98–99,438,440–441,458,460,462,464,469,471,473–474,476–477,484–485,1014,1020–1021,1027,1043–1045` |
| 459 | 보완 | `src/read_input.F:3627,3632,3634,3637,3642`<br>`src/hstart.F:1562,1573`<br>`src/netcdfio.F90:3888–3889` |
| 460 | 이상 없음 | `prep/post.F:1315,1325–1327,1338–1339` |
| 461 | 이상 없음 | `src/write_output.F:2765,5012`<br>`docs/technical_reference/output_files/fort51.rst:13` |
| 462 | 이상 없음 | `docs/technical_reference/output_files/fort73.rst:3,6`<br>`docs/technical_reference/output_files/fort93.rst:4` |
| 463 | 이상 없음 | `src/write_output.F:512,548,1214`<br>`src/read_input.F:4535,4538` |

### source-analysis/adcirc-hotstart.md

| 초기 줄 | 결과 | 대조한 원문·참조 |
|---:|---|---|
| 11 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 46 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 47 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 48 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 49 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 50 | 보완 | `src/write_output.F:5011–5020`<br>`docs/technical_reference/input_files/fort6768.rst:30–32`<br>`src/hstart.F:179,509,511,524` |
| 51 | 보완 | `src/write_output.F:5012,5014–5020`<br>`docs/technical_reference/input_files/fort6768.rst:30–32`<br>`src/hstart.F:179,509,511,524` |
| 52 | 보완 | `src/write_output.F:5011–5012,5014–5020`<br>`docs/technical_reference/input_files/fort6768.rst:30–32`<br>`src/hstart.F:179,509,511,524` |
| 53 | 보완 | `docs/technical_reference/input_files/fort6768.rst:30–35`<br>`prep/post.F:3977,3979,3981,3983,3985,3987,3989,3991,3993,3997,4001,4005,4009,4014,4019,4023`<br>`src/hstart.F:179,509,511,524`<br>`src/write_output.F:5012,5014–5020` |
| 54 | 정정 | `docs/technical_reference/input_files/fort6768.rst:33–36,40`<br>`src/write_output.F:4575,5120–5123,5125–5127,5129–5130,5134–5135,5138–5139,5142–5144,5148–5149`<br>`src/hstart.F:524,526–527` |
| 55 | 정정 | `docs/technical_reference/input_files/fort6768.rst:33–36,40`<br>`src/write_output.F:4584,5120–5123,5125–5127,5129–5130,5134–5135,5138–5139,5142–5144,5148–5149`<br>`src/hstart.F:524,526–527` |
| 56 | 정정 | `docs/technical_reference/input_files/fort6768.rst:33–36,40`<br>`src/write_output.F:4593,5120–5123,5125–5127,5129–5130,5134–5135,5138–5139,5142–5144,5148–5149`<br>`src/hstart.F:524,526–527` |
| 57 | 정정 | `docs/technical_reference/input_files/fort6768.rst:33–37,40`<br>`src/write_output.F:4594,5120–5123,5125–5127,5129–5130,5134–5135,5138–5139,5142–5144,5148–5149`<br>`src/hstart.F:524,526–527` |
| 58 | 정정 | `docs/technical_reference/input_files/fort6768.rst:33–36,38,40`<br>`src/write_output.F:4690,5120–5123,5125–5127,5129–5130,5134–5135,5138–5139,5142–5144,5148–5149`<br>`src/hstart.F:524,526–527` |
| 59 | 정정 | `docs/technical_reference/input_files/fort6768.rst:33–36,39–40`<br>`src/write_output.F:4709,5120–5123,5125–5127,5129–5130,5134–5135,5138–5139,5142–5144,5148–5149`<br>`src/hstart.F:524,526–527` |
| 60 | 보완 | `docs/technical_reference/input_files/fort6768.rst:30–35`<br>`prep/post.F:3977,3979,3981,3983,3985,3987,3989,3991,3993,3997,4001,4005,4009,4014,4019,4023`<br>`src/hstart.F:179,509,511,524`<br>`src/write_output.F:5012,5014–5020` |
| 61 | 보완 | `docs/technical_reference/input_files/fort6768.rst:46`<br>`src/write_output.F:5220–5223,5228–5230`<br>`src/writer.F:1423–1424`<br>`src/hstart.F:26` |
| 62 | 보완 | `docs/technical_reference/input_files/fort6768.rst:46–47`<br>`src/write_output.F:5220–5223,5228–5230`<br>`src/hstart.F:26` |
| 63 | 보완 | `docs/technical_reference/input_files/fort6768.rst:46,48`<br>`src/write_output.F:5220–5223,5225–5226,5228–5230`<br>`src/hstart.F:26` |
| 64 | 보완 | `docs/technical_reference/input_files/fort6768.rst:46,50`<br>`src/write_output.F:5220–5223,5228–5230,5232–5233`<br>`src/hstart.F:26` |
| 65 | 보완 | `docs/technical_reference/input_files/fort6768.rst:46,51`<br>`src/write_output.F:5220–5223,5228–5230,5235–5236`<br>`src/hstart.F:26` |
| 66 | 보완 | `docs/technical_reference/input_files/fort6768.rst:46,52`<br>`src/write_output.F:5220–5223,5228–5230,5238–5239`<br>`src/hstart.F:26` |
| 67 | 보완 | `docs/technical_reference/input_files/fort6768.rst:46,49`<br>`src/write_output.F:5220–5223,5228–5230`<br>`src/hstart.F:26` |
| 68 | 보완 | `docs/technical_reference/input_files/fort6768.rst:46,53`<br>`src/write_output.F:5220–5223,5228–5230,5241–5243`<br>`src/hstart.F:26` |
| 69 | 정정 | `docs/technical_reference/input_files/fort6768.rst:64–65,68,70–71`<br>`src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5295`<br>`prep/post.F:4060–4061,4120–4121` |
| 70 | 정정 | `docs/technical_reference/input_files/fort6768.rst:64–65,68,70–71`<br>`src/vsmy.F:3563,3573–3574,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5295`<br>`prep/post.F:4060–4061,4120–4121` |
| 71 | 정정 | `docs/technical_reference/input_files/fort6768.rst:64–65,68,70–71`<br>`src/vsmy.F:3563,3573,3575,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5295`<br>`prep/post.F:4060–4061,4120–4121` |
| 72 | 정정 | `docs/technical_reference/input_files/fort6768.rst:64,66,68,70–71`<br>`src/vsmy.F:3563,3573,3576,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5295`<br>`prep/post.F:4060–4061,4120–4121` |
| 73 | 정정 | `docs/technical_reference/input_files/fort6768.rst:64,66,68,70–71`<br>`src/vsmy.F:3563,3573,3577,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5295`<br>`prep/post.F:4060–4061,4120–4121` |
| 74 | 정정 | `docs/technical_reference/input_files/fort6768.rst:64,67–68,70–71`<br>`src/vsmy.F:3563,3573,3578,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5295`<br>`prep/post.F:4060–4061,4120–4121` |
| 75 | 정정 | `docs/technical_reference/input_files/fort6768.rst:64,67–68,70–71`<br>`src/vsmy.F:3563,3573,3579,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5295`<br>`prep/post.F:4060–4061,4120–4121` |
| 76 | 정정 | `src/vsmy.F:3563,3573,3617–3619,3621,3623,3625–3626,3751,3753,3756,3758,5276–5277,5285,5293–5295`<br>`docs/technical_reference/input_files/fort6768.rst:64,70–72`<br>`prep/post.F:4060–4061,4120–4121` |
| 77 | 정정 | `src/vsmy.F:3563,3573,3617,3619,3621–3623,3625–3626,3751,3753,3756,3758,5276–5277,5285,5293–5295`<br>`docs/technical_reference/input_files/fort6768.rst:64,70–71,73`<br>`prep/post.F:4060–4061,4120–4121` |
| 78 | 정정 | `src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,3751,3753,3756,3758,5276–5277,5285,5293–5295`<br>`docs/technical_reference/input_files/fort6768.rst:64,70–71,74`<br>`prep/post.F:4060–4061,4120–4121` |
| 79 | 정정 | `src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,3680–3681,3751,3753,3756,3758,5276–5277,5285,5293–5295`<br>`docs/technical_reference/input_files/fort6768.rst:64,70–71,75`<br>`prep/post.F:4060–4061,4120–4121` |
| 80 | 정정 | `src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,3683–3684,3751,3753,3756,3758,5276–5277,5285,5293–5295`<br>`docs/technical_reference/input_files/fort6768.rst:64,70–71,76`<br>`prep/post.F:4060–4061,4120–4121` |
| 81 | 정정 | `src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,3746–3748,3751,3753,3756,3758,5276–5277,5285,5293–5295`<br>`docs/technical_reference/input_files/fort6768.rst:64,70–71,78`<br>`prep/post.F:4060–4061,4120–4121` |
| 82 | 정정 | `src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,3751–3753,3756,3758,5276–5277,5285,5293–5295`<br>`docs/technical_reference/input_files/fort6768.rst:64,70–71,80`<br>`prep/post.F:4060–4061,4120–4121` |
| 83 | 정정 | `src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,3751,3753,3756–3758,5276–5277,5285,5293–5295`<br>`docs/technical_reference/input_files/fort6768.rst:64,70–71,82`<br>`prep/post.F:4060–4061,4120–4121` |
| 84 | 정정 | `docs/technical_reference/input_files/fort6768.rst:57–62,64,70–76`<br>`prep/post.F:4044–4045,4060–4062,4120–4121`<br>`src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5294` |
| 85 | 정정 | `docs/technical_reference/input_files/fort6768.rst:57–62,64,70–76`<br>`prep/post.F:4044–4045,4060–4061,4064–4066,4120–4121`<br>`src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5294` |
| 86 | 정정 | `docs/technical_reference/input_files/fort6768.rst:57–62,64,70–76`<br>`prep/post.F:4044–4045,4060–4061,4068–4070,4120–4121`<br>`src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5294` |
| 87 | 정정 | `docs/technical_reference/input_files/fort6768.rst:57–62,64,70–76`<br>`prep/post.F:4044–4045,4060–4061,4072–4074,4120–4121`<br>`src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5294` |
| 88 | 정정 | `docs/technical_reference/input_files/fort6768.rst:57–62,64,70–76`<br>`prep/post.F:4044–4045,4060–4061,4076–4078,4120–4121`<br>`src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5294` |
| 89 | 정정 | `docs/technical_reference/input_files/fort6768.rst:57–62,64,70–76`<br>`prep/post.F:4044–4045,4060–4061,4080–4082,4120–4121`<br>`src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5294` |
| 90 | 정정 | `docs/technical_reference/input_files/fort6768.rst:57–62,64,70–76`<br>`prep/post.F:4044–4045,4060–4061,4084–4086,4120–4121`<br>`src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5294` |
| 91 | 정정 | `docs/technical_reference/input_files/fort6768.rst:57–62,64,70–76`<br>`prep/post.F:4044–4045,4060–4061,4089–4091,4120–4121`<br>`src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5294` |
| 92 | 정정 | `docs/technical_reference/input_files/fort6768.rst:57–62,64,70–76`<br>`prep/post.F:4044–4045,4060–4061,4095–4097,4120–4121`<br>`src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5294` |
| 93 | 정정 | `docs/technical_reference/input_files/fort6768.rst:57–62,64,70–76`<br>`prep/post.F:4044–4045,4060–4061,4101–4103,4120–4121`<br>`src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5294` |
| 94 | 정정 | `docs/technical_reference/input_files/fort6768.rst:57–62,64,70–76`<br>`prep/post.F:4044–4045,4060–4061,4107–4109,4120–4121`<br>`src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5294` |
| 95 | 정정 | `docs/technical_reference/input_files/fort6768.rst:57–62,64,70–76`<br>`prep/post.F:4044–4045,4060–4061,4113–4115,4120–4121`<br>`src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5294` |
| 96 | 정정 | `docs/technical_reference/input_files/fort6768.rst:57–62,64,70–76`<br>`prep/post.F:4044–4045,4060–4061,4120–4122`<br>`src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5294` |
| 97 | 정정 | `docs/technical_reference/input_files/fort6768.rst:57–62,64,70–76`<br>`prep/post.F:4044–4045,4060–4061,4120–4121,4127–4129`<br>`src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5294` |
| 98 | 정정 | `docs/technical_reference/input_files/fort6768.rst:57–62,64,70–76`<br>`prep/post.F:4044–4045,4060–4061,4120–4121,4134–4136`<br>`src/vsmy.F:3563,3573,3617,3619,3621,3623,3625–3626,5276–5277,5285,5293–5294` |
| 99 | 보완 | `docs/technical_reference/input_files/fort6768.rst:88`<br>`src/write_output.F:5255,5596–5597` |
| 100 | 보완 | `docs/technical_reference/input_files/fort6768.rst:108,111`<br>`src/write_output.F:5316,5319,5324,5334,5342`<br>`docs/technical_reference/parameter_definitions/index.rst:1201,1205,1209,1213` |
| 101 | 보완 | `docs/technical_reference/input_files/fort6768.rst:108,111,115,118`<br>`src/write_output.F:5316,5324,5327,5329,5334,5342`<br>`docs/technical_reference/parameter_definitions/index.rst:1201,1205,1209,1213` |
| 102 | 보완 | `docs/technical_reference/input_files/fort6768.rst:108,111,122,125`<br>`src/write_output.F:5316,5324,5334,5337,5342`<br>`docs/technical_reference/parameter_definitions/index.rst:1201,1205,1209,1213` |
| 103 | 보완 | `docs/technical_reference/input_files/fort6768.rst:108,111,129,132`<br>`src/write_output.F:5316,5324,5334,5342,5345,5347`<br>`docs/technical_reference/parameter_definitions/index.rst:1201,1205,1209,1213` |
| 104 | 보완 | `docs/technical_reference/input_files/fort6768.rst:136`<br>`src/write_output.F:5405,5408,5410,5418` |
| 105 | 보완 | `docs/technical_reference/input_files/fort6768.rst:26,149`<br>`docs/technical_reference/parameter_definitions/index.rst:1225,1227`<br>`src/write_output.F:5587,5591,5595`<br>`src/netcdfio.F90:6869,6876–6877` |
| 106 | 보완 | `docs/technical_reference/input_files/fort6768.rst:16,152`<br>`src/hstart.F:714–716,721,725,727–732,735–736,744–747` |
| 107 | 보완 | `src/timestep.F:1200–1204,1207`<br>`docs/technical_reference/parameter_definitions/index.rst:1225,1227`<br>`src/writer.F:1358,1360,1449–1450,1452–1453,1455–1458` |
| 108 | 보완 | `docs/technical_reference/input_files/fort6768.rst:55,88`<br>`src/timestep.F:1201–1202,1204,1207`<br>`src/writer.F:1360,1375,1387,1391,1395,1399,1403,1413,1417,1447,1452–1453,1455,1457,1459,1464,1516` |
| 109 | 이상 없음 | `docs/technical_reference/input_files/fort6768.rst:88–89,100,104`<br>`prep/post.F:3454–3456,3616,3649,3886,3895,3904,3906,4023,4026,4153,4155`<br>`src/write_output.F:5153,5156,5158,5174,5186,5204,5220,5255,5305` |
| 114 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 115 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 116 | 보완 | `docs/technical_reference/input_files/fort6768.rst:16,152`<br>`src/hstart.F:714–718,721,725,727–732,734–735,737–740,744–747` |
| 137 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 138 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 139 | 보완 | `docs/technical_reference/input_files/fort6768.rst:33–40,64–68,70–76`<br>`src/hstart.F:526–527,537–540,542,601–607,612–614,616–618,2726–2728`<br>`src/harm.F:2057–2060` |
| 153 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 154 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 155 | 보완 | `docs/technical_reference/input_files/fort6768.rst:46–53`<br>`src/hstart.F:26,547–564` |
| 159 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 160 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 161 | 보완 | `docs/technical_reference/input_files/fort6768.rst:55,77,79,81,83,88–89,136`<br>`src/hstart.F:568,633,637,639,641,643,657–658,663–664,666–667`<br>`src/read_input.F:1267,1270,1274,1277`<br>`src/harm.F:1760–1761,1763,1771` |
| 162 | 보완 | `docs/technical_reference/input_files/fort6768.rst:108,111,115,118,122,125,129,132`<br>`src/harm.F:1732–1733,1736,1739–1740,1746–1747,1750,1753–1754` |
| 163 | 보완 | `docs/technical_reference/input_files/fort6768.rst:55,77,79,81,83,88,136–137,139,142–143`<br>`src/harm.F:1760–1763,1765,1767,1771,1773,1775,1777,1779`<br>`src/hstart.F:568,633,637,639,641,643,657–658,663–664,666–667`<br>`src/read_input.F:1267,1270,1274,1277` |
| 167 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 168 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 169 | 보완 | `docs/technical_reference/input_files/fort6768.rst:55,77,79,81,83,88,136`<br>`src/hstart.F:568,633,637,639,641,643,657–658,663–664,666–667`<br>`src/read_input.F:1190–1191,1267,1270,1274,1277`<br>`src/harm.F:1760–1761,1763,1771` |
| 170 | 보완 | `docs/technical_reference/input_files/fort6768.rst:33–40,64–68,70–76`<br>`docs/technical_reference/parameter_definitions/index.rst:2529,2534,2540`<br>`src/hstart.F:526–527,537–540,542,601–607,612–614,616–618,2726–2728`<br>`src/harm.F:2057–2060` |
| 171 | 보완 | `docs/technical_reference/input_files/fort6768.rst:33–40,64–68,70–76,78,80,82,84`<br>`src/hstart.F:526–527,537–540,542,601–607,612–614,616–618,2726–2728,3101`<br>`src/harm.F:2057–2060` |
| 172 | 보완 | `docs/technical_reference/input_files/fort6768.rst:55,77–84,88,136`<br>`src/hstart.F:568,633,637–645,657–658,663–664,666–667`<br>`src/read_input.F:1267,1270,1274,1277`<br>`src/harm.F:1760–1761,1763,1771` |
| 176 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 177 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:1221,1223,1225,1227`<br>`src/read_input.F:4529–4532,4538,4541,4544,4548`<br>`src/timestep.F:1210–1212` |
| 178 | 이상 없음 | `docs/technical_reference/input_files/fort6768.rst:30`<br>`src/hstart.F:509–513,519–522,532–533,536,626–627,629–630,633` |
| 179 | 이상 없음 | `src/read_input.F:4530–4532,4552–4553`<br>`src/timestep.F:1200`<br>`src/write_output.F:5471,5638,5640,5642,5665–5667` |
| 180 | 이상 없음 | `src/write_output.F:4700,4992–4997,4999–5000,5130–5132,5156,5158,5174,5186,5204` |
| 181 | 이상 없음 | `src/timestep.F:1639`<br>`src/netcdfio.F90:5463,5466,5479,5481–5482,5494,5496–5497` |
| 182 | 이상 없음 | `src/write_output.F:5149,5153`<br>`src/hstart.F:542,544–545` |
| 183 | 이상 없음 | `src/write_output.F:5632–5633,5635,5638,5640,5642,5665–5667` |
| 184 | 이상 없음 | `prep/read_global.F:1925–1926`<br>`src/adcirc.F:540–541`<br>`docs/technical_reference/parameter_definitions/index.rst:1173,1175,1177` |
| 185 | 이상 없음 | `src/timestep.F:1200–1202,1204,1207`<br>`src/writer.F:1360,1452–1453,1455,1457` |
| 186 | 이상 없음 | `src/global_3dvs.F:417–418,488–489`<br>`src/vsmy.F:3571–3574,3617,3619,5285,5293–5294`<br>`docs/technical_reference/input_files/fort6768.rst:64` |
| 187 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 217 | 이상 없음 | `src/netcdfio.F90:8007–8008,8010,8012,8014,8016–8018,8020,8022,8024,8035,8073–8076,8081–8082,8107,8127–8129,8136–8138,8140–8142,8144` |
| 221 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 222 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 223 | 보완 | `src/netcdfio.F90:7943,7956,7982,7986–7987,7990,7993,7995,7997,7999,8001,8003,8005,8007–8008,8010,8012,8014,8016–8018,8020,8022,8024,8029,8031,8163,8165,8167,8169,8171,8173,8175,8177,8179–8180,8182,8185,8187,8189,8191,8193,8195,8197–8198,8200,8203`<br>`docs/technical_reference/input_files/fort6768.rst:26`<br>`src/hstart.F:674–677,679` |
| 224 | 보완 | `src/netcdfio.F90:7943,7956,7982,7993,7995,7997,7999,8001,8003,8005,8007–8008,8010,8012,8014,8016–8018,8020,8022,8024,8029,8031,8115,8117,8119,8121,8123,8125,8150,8154,8158,8163,8167,8171,8175,8179–8180,8185,8189,8193,8197–8198,8203`<br>`docs/technical_reference/input_files/fort6768.rst:26`<br>`src/hstart.F:674–677,679` |
| 225 | 보완 | `src/netcdfio.F90:7943,7956,7982,7993,7995,7997,7999,8001,8003,8005,8007–8008,8010,8012,8014,8016–8018,8020,8022,8024,8029,8031,8035,8073–8076,8081–8082,8107,8127–8129,8136–8138,8140–8142,8144,8163,8167,8171,8175,8179–8180,8185,8189,8193,8197–8198,8203`<br>`docs/technical_reference/input_files/fort6768.rst:26`<br>`src/hstart.F:674–677,679` |
| 226 | 보완 | `src/hstart.F:684–685`<br>`src/netcdfio.F90:8798–8800,8819–8821,8861,8876,8878,8899,8922–8923,8925–8926,8950,8954,8958,8962,8966,8970,8974,8978,8982,8986,8990,8994,8998,9002,9016,9018,9021,9028,9036,9038,9040,9042,9044,9046,9115–9116,9118,9134–9135,9137,9139,9141,9169` |
| 227 | 보완 | `src/hstart.F:684–685`<br>`src/netcdfio.F90:8798–8800,8819–8821,8861,8864–8865,8876,8878,8899,8903–8904,8922–8923,8925–8926,8950,8954,8958,8962,8974,8978,8982,8986,8990,8994,8998,9002,9016,9021,9036,9040,9044,9115–9116,9118,9134–9135,9137,9139,9141,9169` |
| 228 | 보완 | `src/hstart.F:684,686–688`<br>`src/netcdfio.F90:8798–8800,8819–8821,8861,8876,8878,8899,8922–8923,8925–8926,8950,8954,8958,8962,8974,8978,8982,8986,8990,8994,8998,9002,9016,9021,9036,9040,9044,9115–9116,9118,9134–9135,9137,9139,9141,9169` |
| 229 | 보완 | `src/netcdfio.F90:9257,9259,9261,9263,9265,9267,9269,9272–9273,9319–9320,9332–9334,9346–9348,9362,9364,9366,9390,9394,9396,9415,9419,9423,9427,9431,9435,9439,9443,9447,9451,9455,9459` |
| 230 | 보완 | `src/netcdfio.F90:9257,9259,9261,9263,9265,9267,9269,9319–9320,9323–9324,9332–9334,9337–9338,9346–9348,9362,9364,9366,9390,9394,9396,9399–9400,9415,9419,9423,9427,9431,9435,9439,9443,9447,9451,9455,9459` |
| 231 | 보완 | `src/netcdfio.F90:9257,9259,9261,9263,9265,9267,9269,9319–9320,9332–9334,9346–9348,9362,9364,9366,9390,9394,9396,9415,9417,9419,9421,9423,9427,9431,9435,9439,9443,9447,9451,9455,9459` |
| 234 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 235 | 정정 | `src/netcdfio.F90:5291–5293,5358–5360,5492–5494,6869,6872,6875–6877,6907,6995–6997,7066–7067,7092,7110`<br>`src/write_output.F:5590–5591` |
| 236 | 이상 없음 | `src/netcdfio.F90:5857–5860,5864,5900–5901,7213,7237,7239–7240,7270–7271,7365,7367`<br>`src/write_output.F:5596–5597` |
| 237 | 이상 없음 | `src/netcdfio.F90:6215–6218,6237–6238,6263,7464,7483–7485,7508–7509`<br>`src/write_output.F:5602–5603` |
| 238 | 이상 없음 | `src/netcdfio.F90:6460–6462,6473–6474,6487–6488,6729,7606,7623–7624,7645–7646,7783,7785,7788–7789,7791–7792`<br>`src/write_output.F:5608–5609` |
| 239 | 보완 | 구조·참조 또는 같은 절의 원문 연결 |
| 248 | 이상 없음 | `src/write_output.F:5587,5589`<br>`src/netcdfio.F90:3945–3946` |
| 249 | 이상 없음 | `src/write_output.F:5589`<br>`src/netcdfio.F90:3947–3951,3966` |

### source-analysis/adcirc-nodal-attributes.md

| 초기 줄 | 결과 | 대조한 원문·참조 |
|---:|---|---|
| 16 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 30 | 이상 없음 | `docs/technical_reference/input_files/fort13.rst:64,68,70`<br>`raw/manuals/wiki/markdown/Fort.13_file.md:180`<br>`src/nodalattr.F:497,1214–1216,1909–1910,1914,1919` |
| 38 | 이상 없음 | `docs/technical_reference/input_files/fort13.rst:126,130,132,134`<br>`src/nodalattr.F:500,1229–1232,2904,2928–2929,2958–2959,2971–2974,2978–2979` |
| 48 | 이상 없음 | `src/nodalattr.F:1003,1325–1327,1530,2962–2965` |
| 51 | 이상 없음 | `src/nodalattr.F:480,503–504,1235–1238,1403,2040,2046` |
| 54 | 정정 | `src/nodalattr.F:547,1337–1339` |
| 58 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 59 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 60 | 보완 | `docs/technical_reference/input_files/fort13.rst:231,234,238,240,242`<br>`src/nodalattr.F:513,1273–1280,1456–1457,2114` |
| 61 | 보완 | `docs/technical_reference/input_files/fort13.rst:238`<br>`raw/manuals/wiki/markdown/Fort.13_file.md:101`<br>`docs/technical_reference/parameter_definitions/index.rst:743`<br>`src/gwce.F:828,831–834,840` |
| 62 | 보완 | `docs/technical_reference/input_files/fort13.rst:238`<br>`raw/manuals/wiki/markdown/Fort.13_file.md:101`<br>`src/gwce.F:828,831–834,837–838,840`<br>`docs/technical_reference/parameter_definitions/index.rst:743` |
| 63 | 이상 없음 | `src/nodalattr.F:515–516,1283–1286` |
| 64 | 이상 없음 | `src/nodalattr.F:255,1321–1322,2651,2656,2661,2663–2664,2681–2684` |
| 71 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 72 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 73 | 정정 | `src/subgridLookup.F:53–68,162,193,195–196,198–199,204–205,231–232,243,257–258,273,287,301–302,309,316–317,374–382,394`<br>`docs/tools/subgrid_adcirc_utility.rst:11–18` |
| 74 | 정정 | `src/subgridLookup.F:53–68,193,195–196,198–199,204–205,229,231–233,235–238,240,243–244,257–259,273,287,301–302,309,316–317,374–382`<br>`docs/tools/subgrid_adcirc_utility.rst:11–18` |
| 75 | 정정 | `src/subgridLookup.F:53–68,193,195–196,198–199,204–205,231–232,243,257–258,273–274,287–288,301–302,309,314,316–317,374–382`<br>`docs/tools/subgrid_adcirc_utility.rst:11–18` |
| 79 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 80 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 81 | 보완 | `src/mesh.F:153–157,745,747–749,867,869–872,887–888,890–891,907–909,943–945,952,1003–1004,1006,1009,1016–1017,1020,1143–1145,1181–1188,1211,1213–1215,1218–1229,1278–1292,1300–1301`<br>`src/nodalattr.F:625,638–639,642,650–651,653–654,657,733–734,753–754,756,758,765–766` |
| 82 | 보완 | `src/mesh.F:153–157,867,869–872,887–888,890–891,907–909,943–945,952,1003–1004,1006,1009,1016–1017,1020,1140,1143–1145,1151,1154,1166,1181–1188,1197,1211,1213–1215,1218–1229,1240,1261,1278–1292,1300–1301`<br>`src/nodalattr.F:625,638–639,642,650–651,653–654,657,733–734,753–754,756,758,765–766` |
| 83 | 정정 | `src/nodalattr.F:578–579,583,625,638–639,642,650–651,653–654,657,733–734,753–754,756,758,765–766`<br>`src/mesh.F:153–157,867,869–872,887–888,890–891,907–909,943–945,952,1003–1004,1006,1009,1016–1017,1020,1143–1145,1181–1188,1211,1213–1215,1218–1229,1278–1292,1300–1301` |
| 88 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 89 | 이상 없음 | `docs/technical_reference/input_files/fort13.rst:40`<br>`src/nodalattr.F:1340,1347–1349,1583,1594` |
| 90 | 보완 | `src/nodalattr.F:467,686–688,905–907,916–936,954–955,1278–1280,1353–1355` |
| 91 | 이상 없음 | `src/nodalattr.F:495,522,1330–1332,2367,2407–2410`<br>`src/wetdry.F:1510,1517–1519,1525` |
| 92 | 보완 | `docs/technical_reference/input_files/fort13.rst:249`<br>`src/write_output.F:1425–1426,1428`<br>`src/nodalattr.F:995,997,999` |
| 93 | 이상 없음 | `docs/technical_reference/input_files/fort13.rst:338`<br>`src/nodalattr.F:547,1337–1339,1555–1558` |
| 94 | 이상 없음 | `src/internaltide.F90:80,93,103–104,108–111` |
| 95 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 100 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 101 | 이상 없음 | `src/nodalattr.F:2399,2407,2409,2415–2416,2423–2425,2427` |
| 102 | 이상 없음 | `docs/technical_reference/input_files/fort13.rst:153,162`<br>`src/nodalattr.F:484,1417` |
| 103 | 이상 없음 | `docs/user_guide/special_features/bridge_piers.rst:18,28,67,69`<br>`src/nodalattr.F:2102–2103,2483,2487–2488` |
| 104 | 정정 | `docs/user_guide/special_features/bridge_piers.rst:39`<br>`src/nodalattr.F:2484–2486` |
| 105 | 이상 없음 | `docs/user_guide/special_features/bridge_piers.rst:63,65`<br>`src/nodalattr.F:2489` |
| 106 | 이상 없음 | `src/nodalattr.F:2481,2489`<br>`docs/user_guide/special_features/bridge_piers.rst:18` |
| 107 | 보완 | `src/nodalattr.F:2481–2483,2487–2488,2562` |
| 108 | 이상 없음 | `src/nodalattr.F:1417,1419–1420` |
| 109 | 이상 없음 | `src/nodalattr.F:2101–2103` |
| 110 | 이상 없음 | `src/nodalattr.F:2487–2489` |
| 111 | 이상 없음 | `src/nodalattr.F:2397–2399,2424–2425` |
| 112 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 118 | 이상 없음 | `src/nodalattr.F:2376,2379,2393,2406–2408,2414–2415,2422–2424` |
| 122 | 이상 없음 | `src/nodalattr.F:2376,2433,2435` |
| 124 | 이상 없음 | `src/nodalattr.F:2376,2393,2395–2396,2399–2401,2403–2404,2416–2417,2424–2425` |
| 125 | 이상 없음 | `src/nodalattr.F:2376,2393,2406–2410` |
| 134 | 이상 없음 | `src/nodalattr.F:489,1285–1286` |
| 139 | 이상 없음 | `src/nodalattr.F:2904,2958–2959,2971–2974,2978–2979` |
| 144 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 145 | 이상 없음 | `src/nodalattr.F:503–504,1003,1235–1238,1325–1327,2962–2965` |
| 146 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 149 | 이상 없음 | `src/nodalattr.F:2619,2656,2687,2693,2697–2698,2700–2702,2725,2733–2739,2741,2745–2747` |
| 151 | 이상 없음 | `src/nodalattr.F:2619,2656,2755,2757,2762–2764,2766` |
| 152 | 이상 없음 | `src/nodalattr.F:2619,2656,2661,2663–2664,2666,2668–2670,2680–2684` |
| 153 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 154 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 155 | 이상 없음 | `docs/technical_reference/input_files/fort13.rst:302,304,306`<br>`src/nodalattr.F:1318–1322,2656,2661–2684` |
| 156 | 이상 없음 | `_staging/recovery/read/ADCIRC/manuals/wiki/markdown/Internal_Tide_Energy_Conversion.md.md:15` |
| 157 | 정정 | `docs/user_guide/model_configuration/tides/internal_tide_energy_conversion.rst:38–44`<br>`src/nodalattr.F:1520–1523` |
| 158 | 이상 없음 | `docs/user_guide/model_configuration/tides/internal_tide_energy_conversion.rst:47`<br>`src/nodalattr.F:2661,2663–2664,2681–2684` |
| 159 | 이상 없음 | `docs/user_guide/model_configuration/tides/internal_tide_energy_conversion.rst:49–51`<br>`src/nodalattr.F:1522–1524,2762,2769` |
| 160 | 이상 없음 | `docs/user_guide/model_configuration/tides/internal_tide_energy_conversion.rst:58–59`<br>`src/nodalattr.F:2673–2674,2676–2678,2680–2684,2708,2711,2714,2716,2718,2721–2722` |
| 161 | 이상 없음 | `src/nodalattr.F:2661,2666,2668–2669` |
| 162 | 이상 없음 | `src/nodalattr.F:2694–2698,2700–2701` |
| 163 | 이상 없음 | `src/internaltide.F90:137–139,149–150`<br>`src/nodalattr.F:2659` |
| 164 | 이상 없음 | `src/nodalattr.F:2730,2733–2735,2739,2745–2747` |
| 165 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 166 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 167 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 168 | 정정 | features 보고서 §5 T09 (423줄) |
| 169 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 170 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 171 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 172 | 이상 없음 | `docs/user_guide/model_configuration/tides/internal_tide_energy_conversion.rst:58–62`<br>`src/nodalattr.F:2662–2664,2673–2684,2708–2721` |
| 173 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 174 | 이상 없음 | `src/nodalattr.F:2676–2678,2680` |
| 175 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 176 | 보완 | `src/nodalattr.F:2673–2684,2708–2721` |

### source-analysis/adcirc-output-writers-implementation.md

| 초기 줄 | 결과 | 대조한 원문·참조 |
|---:|---|---|
| 11 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 23 | 이상 없음 | `src/write_output.F:1850–1851,1855–1856,1861–1864` |
| 30 | 이상 없음 | `src/read_input.F:3634–3636` |
| 71 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 72 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 73 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:1199,1201,1203,1205,1207,1209,1211,1213`<br>`src/harm.F:401,409,413`<br>`src/write_output.F:2177,2728,2730,2758,2760,2811–2813,2815,2821–2822,2825,2828`<br>`docs/technical_reference/output_files/fort51.rst:28`<br>`docs/technical_reference/output_files/fort52.rst:28`<br>`docs/technical_reference/output_files/fort53.rst:31`<br>`docs/technical_reference/output_files/fort54.rst:31` |
| 74 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:1199,1201,1203,1205,1207,1209,1211,1213`<br>`src/harm.F:401,409,413`<br>`src/write_output.F:2177,2728,2730,2758,2760,2811–2813,2815,2821–2822,2825,2828`<br>`docs/technical_reference/output_files/fort51.rst:28`<br>`docs/technical_reference/output_files/fort52.rst:28`<br>`docs/technical_reference/output_files/fort53.rst:31`<br>`docs/technical_reference/output_files/fort54.rst:31` |
| 75 | 보완 | `docs/technical_reference/output_files/fort51.rst:28`<br>`docs/technical_reference/output_files/fort52.rst:28`<br>`docs/technical_reference/output_files/fort53.rst:31`<br>`docs/technical_reference/output_files/fort54.rst:31`<br>`src/write_output.F:2177,2728,2730,2758,2760,2811,2815,2817`<br>`docs/user_guide/examples/global_astronomical_m2_tide.rst:39,41` |
| 76 | 보완 | `docs/technical_reference/output_files/fort51.rst:21`<br>`src/write_output.F:2771,2796`<br>`prep/post.F:1353,1357` |
| 77 | 보완 | `docs/technical_reference/output_files/fort52.rst:21`<br>`src/write_output.F:2771,2796`<br>`docs/technical_reference/output_files/fort51.rst:21`<br>`prep/post.F:1353,1357` |
| 78 | 보완 | `docs/technical_reference/output_files/fort51.rst:13,15,21`<br>`prep/post.F:1322,1353,1357`<br>`src/write_output.F:2771,2796` |
| 79 | 보완 | `docs/technical_reference/output_files/fort52.rst:13,15`<br>`prep/post.F:1353,1357,1436,1467,1471`<br>`docs/technical_reference/output_files/fort51.rst:21`<br>`src/write_output.F:2771,2796` |
| 80 | 보완 | `docs/technical_reference/output_files/fort55.rst:15`<br>`src/write_output.F:2703–2705,2708–2712` |
| 81 | 보완 | `docs/technical_reference/output_files/fort55.rst:15,19–20`<br>`src/write_output.F:2703–2705,2708–2712` |
| 82 | 보완 | `docs/technical_reference/output_files/fort55.rst:13,15,19–20`<br>`prep/post.F:1772,1795,1797,1825,1828–1829`<br>`src/write_output.F:2703–2705,2708–2712` |
| 83 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:2151,2161,2171`<br>`src/netcdfio.F90:1889,1941` |
| 84 | 보완 | `docs/technical_reference/output_files/fort51.rst:21`<br>`docs/technical_reference/output_files/fort52.rst:21`<br>`docs/technical_reference/parameter_definitions/index.rst:2151,2161,2171`<br>`src/netcdfio.F90:909,921,926,938,949,971,1812,1833,1838,1859,1868,1889,1894,1915,1920,1941,1946,1967` |
| 85 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:2191,2201`<br>`src/harm.F:1351–1353,1355,1357–1359,1361` |
| 101 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 102 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 103 | 보완 | `docs/technical_reference/output_files/fort41.rst:82`<br>`docs/technical_reference/output_files/fort42.rst:28`<br>`docs/technical_reference/output_files/fort43.rst:28`<br>`docs/technical_reference/output_files/fort45.rst:28`<br>`docs/technical_reference/output_files/fort46.rst:30`<br>`src/read_input.F:5866–5871`<br>`src/write_output.F:3423,3426,3602,3604–3605,3710,3712,3803,3805,4008,4010,4129,4131,4201,4203` |
| 104 | 보완 | `docs/technical_reference/output_files/fort41.rst:82`<br>`docs/technical_reference/output_files/fort46.rst:30`<br>`src/read_input.F:5866,5871–5875`<br>`src/write_output.F:3423,3426,3602,3604–3605,4008,4129,4201`<br>`src/netcdfio.F90:3887–3890,3897,3903,3905,3911–3913` |
| 105 | 보완 | `docs/technical_reference/output_files/fort41.rst:75`<br>`src/write_output.F:3546–3547,3604–3605` |
| 106 | 보완 | `docs/technical_reference/output_files/fort41.rst:75`<br>`src/write_output.F:3546–3547,3604–3605` |
| 107 | 보완 | `docs/technical_reference/output_files/fort41.rst:75`<br>`src/write_output.F:3546–3547,3604–3605` |
| 108 | 이상 없음 | `docs/technical_reference/output_files/fort44.rst:21,35,49,63`<br>`src/cstart.F:1044,1050–1051` |
| 109 | 보완 | `docs/technical_reference/output_files/fort44.rst:21,35,37,49,51,63,65`<br>`prep/post.F:4765–4766,4768,4782–4783,4797,4808–4809,4823,4837–4839,4854`<br>`src/cstart.F:1050–1051`<br>`src/write_output.F:3902–3903` |
| 110 | 보완 | `docs/technical_reference/output_files/fort44.rst:37,65`<br>`src/write_output.F:3902–3903,3918–3919`<br>`docs/technical_reference/output_files/fort41.rst:38,72` |
| 111 | 보완 | `docs/technical_reference/output_files/fort44.rst:37,51,65`<br>`src/write_output.F:3902–3903,3910–3911,3918–3919`<br>`docs/technical_reference/output_files/fort41.rst:38,72` |
| 112 | 보완 | `docs/technical_reference/output_files/fort44.rst:37,65`<br>`src/write_output.F:3902–3903,3918–3919`<br>`docs/technical_reference/output_files/fort41.rst:38,72` |
| 113 | 이상 없음 | `docs/technical_reference/output_files/fort41.rst:21,38,55`<br>`prep/post.F:4290,4292–4297,4305,4336–4338`<br>`src/write_output.F:3524–3525,3528–3529` |
| 114 | 보완 | `docs/technical_reference/output_files/fort44.rst:21,35,37,49,51,63,65`<br>`prep/post.F:4765–4766,4768,4782–4783,4797,4808–4809,4823,4837–4839,4854`<br>`src/cstart.F:1050–1051`<br>`src/write_output.F:3902–3903` |
| 115 | 보완 | `docs/technical_reference/output_files/fort43.rst:21`<br>`src/write_output.F:3747–3748,3781–3782`<br>`docs/technical_reference/parameter_definitions/index.rst:2748–2749` |
| 116 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:2754,2784`<br>`src/write_output.F:3749–3750`<br>`src/netcdfio.F90:885,891,900–901`<br>`docs/technical_reference/output_files/fort46.rst:6` |
| 117 | 보완 | `docs/technical_reference/output_files/fort47.rst:6,17`<br>`src/cstart.F:1053,1055–1056,1059`<br>`src/write_output.F:3880–3882,4014–4015,4029` |
| 118 | 보완 | `docs/technical_reference/output_files/fort47.rst:6,17`<br>`src/cstart.F:1053,1055–1056,1058–1059`<br>`src/write_output.F:4014–4015,4029` |
| 119 | 보완 | `docs/technical_reference/output_files/fort47.rst:6,17`<br>`src/cstart.F:1053,1055–1056,1058–1059`<br>`src/write_output.F:4014–4015,4029` |
| 120 | 보완 | `docs/technical_reference/output_files/fort47.rst:6,17`<br>`prep/post.F:5241–5242,5248,5258–5259`<br>`src/cstart.F:1053,1055–1056,1059`<br>`src/write_output.F:4014–4015,4029` |
| 121 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:2250`<br>`src/cstart.F:1031,1036,1041–1043,1081–1082,1085–1086` |
| 122 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:2734`<br>`src/netcdfio.F90:830,835–837,1685,1690–1692,4388,4397–4398`<br>`src/global_3dvs.F:109,272`<br>`src/write_output.F:3157` |
| 123 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:2704,2709,2714`<br>`src/netcdfio.F90:700,715,732,1570,1582,1595,4344–4345,4348–4349,4351–4352,4356–4358,4361–4362,4370–4372,4375–4376,10455–10458` |
| 137 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 138 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 139 | 보완 | `docs/technical_reference/output_files/maxmin63.rst:53`<br>`src/write_output.F:1243,1275,1310,1346,1383–1386,1961` |
| 140 | 보완 | `docs/technical_reference/output_files/maxmin63.rst:53`<br>`src/write_output.F:1243,1275,1310,1346,1383–1384,1386,1954–1955,1961` |
| 141 | 보완 | `docs/technical_reference/output_files/maxmin63.rst:53`<br>`src/write_output.F:1243,1275,1310,1346,1383–1384,1386,1949,1958–1959,1961,1963–1964` |
| 142 | 보완 | `docs/technical_reference/output_files/maxmin63.rst:53`<br>`src/write_output.F:1243,1275,1310,1346,1383–1384,1386,1949,1958,1961,1963–1964` |
| 143 | 보완 | `docs/technical_reference/output_files/maxmin63.rst:53`<br>`src/write_output.F:1243,1275,1310,1346,1383–1384,1386,1949,1958,1961,1963–1964` |
| 144 | 보완 | `docs/technical_reference/output_files/maxmin63.rst:36`<br>`src/globalio.F:1043–1045` |
| 145 | 보완 | `docs/technical_reference/output_files/maxmin63.rst:36`<br>`src/globalio.F:1043–1045` |
| 146 | 보완 | `docs/technical_reference/output_files/maxinundepth63.rst:20`<br>`src/globalio.F:1043–1045`<br>`docs/technical_reference/output_files/maxmin63.rst:36` |
| 147 | 보완 | `docs/technical_reference/output_files/maxinundepth63.rst:20`<br>`src/globalio.F:1043–1045`<br>`docs/technical_reference/output_files/maxmin63.rst:36` |
| 148 | 보완 | `docs/technical_reference/output_files/everdried63.rst:22`<br>`src/globalio.F:1043–1045`<br>`docs/technical_reference/output_files/maxmin63.rst:36` |
| 149 | 보완 | `docs/technical_reference/output_files/everdried63.rst:22`<br>`src/globalio.F:1043–1045`<br>`docs/technical_reference/output_files/maxmin63.rst:36` |
| 150 | 보완 | `docs/technical_reference/output_files/inundationtime63.rst:20`<br>`src/globalio.F:1043–1045`<br>`docs/technical_reference/output_files/maxmin63.rst:36` |
| 151 | 보완 | `docs/technical_reference/output_files/inundationtime63.rst:20`<br>`src/globalio.F:1043–1045`<br>`docs/technical_reference/output_files/maxmin63.rst:36` |
| 152 | 보완 | `docs/technical_reference/output_files/maxwvel63.rst:8`<br>`src/write_output.F:1348,6475–6477`<br>`docs/technical_reference/parameter_definitions/index.rst:2327`<br>`docs/technical_reference/output_files/fort72.rst:30`<br>`src/wind.F:908,917,926,948,1142,1164` |
| 153 | 보완 | `docs/technical_reference/output_files/maxrs63.rst:8`<br>`src/write_output.F:1392,6481,6483–6487`<br>`src/netcdfio.F90:2635` |
| 154 | 보완 | `docs/technical_reference/output_files/nodecode63.rst:18`<br>`docs/technical_reference/output_files/noff100.rst:17`<br>`src/globalio.F:1464–1465,1467–1468`<br>`src/write_output.F:1861–1862,1921` |
| 155 | 보완 | `docs/technical_reference/output_files/initiallydry63.rst:18–19`<br>`src/globalio.F:1469–1470`<br>`src/write_output.F:6207–6209,6327–6328` |
| 156 | 보완 | `docs/technical_reference/output_files/endrisinginun63.rst:18`<br>`src/write_output.F:1515,1523,1528,1531–1532,1633–1634,1662–1663,1672,2000,6296,6301`<br>`src/globalio.F:568–571` |
| 157 | 보완 | `docs/technical_reference/output_files/noff100.rst:21–22`<br>`src/write_output.F:697,709–712,4717–4718`<br>`src/globalio.F:619,850`<br>`src/mesh.F:72` |
| 158 | 보완 | `docs/technical_reference/output_files/everdried63.rst:12,30`<br>`src/write_output.F:6245,6248,6411–6415` |
| 159 | 보완 | `docs/technical_reference/output_files/inundationtime63.rst:4,9,23`<br>`src/write_output.F:6245,6361–6364,6378,6380–6384`<br>`src/timestep.F:1170–1171` |
| 160 | 보완 | `docs/technical_reference/output_files/inundationtime63.rst:4,9,37`<br>`src/write_output.F:1453,1455,6364` |
| 161 | 보완 | `docs/technical_reference/output_files/inundationtime63.rst:9`<br>`src/write_output.F:6363–6364`<br>`src/netcdfio.F90:3341,3344–3345,3351,3383–3384,5031–5032` |
| 162 | 보완 | `docs/technical_reference/output_files/maxinundepth63.rst:4`<br>`src/write_output.F:6361–6363,6368,6372–6373`<br>`src/netcdfio.F90:3395,3405–3406,3409–3410,3438,3440`<br>`src/timestep.F:1170–1171` |
| 163 | 보완 | `docs/technical_reference/output_files/everdried63.rst:12`<br>`src/write_output.F:6248,6411–6413,6415`<br>`src/netcdfio.F90:3505,3518,3525,3548,5034–5035` |
| 164 | 보완 | `docs/technical_reference/output_files/maxinundepth63.rst:4`<br>`src/netcdfio.F90:3394–3395,3437–3438,10455–10458`<br>`src/write_output.F:6372–6373` |
| 173 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 174 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 175 | 보완 | `docs/technical_reference/output_files/maxinundepth63.rst:36`<br>`docs/technical_reference/output_files/inundationtime63.rst:36`<br>`docs/technical_reference/output_files/everdried63.rst:38`<br>`src/write_output.F:1462,1497,1565,1689–1690,1692,1699,1702,1706,1708–1710,1731`<br>`src/globalio.F:1545,1551,1555,1560`<br>`src/netcdfio.F90:8374,8380,8384,8395` |
| 177 | 이상 없음 | `src/write_output.F:1949–1951` |
| 183 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 184 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 185 | 보완 | `docs/user_guide/tips_and_tricks/visualization.rst:41–42`<br>`src/netcdfio.F90:629,650,656,660,666,1534,9494,9553,9575,9585` |
| 186 | 보완 | `docs/technical_reference/output_files/fort77.rst:4,17,20`<br>`src/netcdfio.F90:2677–2680,2695,4640–4643,5064,5073–5074` |
| 187 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:58,492`<br>`src/netcdfio.F90:4095–4096,4098,4100,4103,4105,4110,9691–9693,9712,9721,9805,9811,9840,9853,9990,10019–10020,10029,10032,10455–10458` |
| 188 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:28,38,58,123,133,492`<br>`src/netcdfio.F90:4095–4096,4098,4100,4103,4105,4110,9691–9693,9712,9721,9805,9811,9840,9853,9990,10019–10020,10029,10032,10455–10458` |
| 195 | 이상 없음 | `src/netcdfio.F90:675,678–679,683–684` |
| 206 | 이상 없음 | `src/netcdfio.F90:1547,1550–1551,1555–1556` |
| 251 | 이상 없음 | `src/netcdfio.F90:5293,5315,5337,5360,5379,5398,5429,5460,5463,5479,5494,5509,5511,5516,5518,5558,5560,5565,5567,5632,5641,5652,5665,5674–5675,5687,5700,5711,5722–5723,5735` |
| 252 | 이상 없음 | `src/netcdfio.F90:5859,5865,5876,5887,5902,5912,5916,5936,5940,5958,5978,5986,6006,6015,6035` |
| 253 | 이상 없음 | `src/netcdfio.F90:6213,6217,6239,6261,6265,6288,6311,6335` |
| 254 | 이상 없음 | `src/netcdfio.F90:6461,6475,6489,6503,6517,6531,6545,6562–6563,6574–6575,6587–6588,6606,6618,6630,6647,6659` |
| 256 | 이상 없음 | `src/netcdfio.F90:9502,9508,9541,9546,9553,9558` |
| 257 | 이상 없음 | `src/netcdfio.F90:9573,9575,9579,9585,9604,9606,9610,9615,9618–9619,9622,9624,9626,9629,9632–9633,9636,9639` |
| 285 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 286 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 287 | 보완 | `docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:77,163–164,168–169`<br>`src/write_output.F:1949,1977–1978,1980,1982,1984,1986,1988,1990,5793,5868–5871,5884,5914,5930,5960,5976,6006,6022,6052,6070,6100,6116,6146,6162` |
| 288 | 보완 | `docs/user_guide/model_configuration/meteorological_forcing/wind_stress.rst:142–148`<br>`src/write_output.F:955–959,963–964,966` |
| 289 | 보완 | `docs/technical_reference/output_files/fort71.rst:16`<br>`prep/post.F:1898,1913–1914,1924,1937–1938,1940,2993,3007,4610,4644`<br>`docs/technical_reference/output_files/fort43.rst:15` |
| 290 | 보완 | `docs/technical_reference/output_files/fort91.rst:14`<br>`prep/post.F:1924,1938,2967,2982–2983,2993,3006–3007,3009,4610,4644`<br>`docs/technical_reference/output_files/fort43.rst:15` |
| 291 | 보완 | `docs/technical_reference/output_files/fort43.rst:15,20`<br>`prep/post.F:1924,1938,2993,3007,4594,4610,4644–4645` |
| 296 | 이상 없음 | `src/xdmfio.F:88,698` |
| 313 | 이상 없음 | `src/xdmfio.F:744–747` |
| 319 | 이상 없음 | `src/xdmfio.F:765–769` |
| 322 | 이상 없음 | `src/xdmfio.F:778–780,782–784` |
| 326 | 이상 없음 | `src/xdmfio.F:794–798` |
| 330 | 이상 없음 | `src/xdmfio.F:812,817–821` |
| 331 | 이상 없음 | `src/xdmfio.F:812–813,815,817,824,827,830,835,838,840,843,845,848,850–852` |
| 333 | 이상 없음 | `src/xdmfio.F:860–861,864,868,872,877,881,885,891,897,899,901–902` |
| 335 | 이상 없음 | `src/xdmfio.F:907–912` |
| 336 | 이상 없음 | `src/xdmfio.F:907,913–916` |
| 339 | 이상 없음 | `src/xdmfio.F:921,926–929` |
| 340 | 이상 없음 | `src/xdmfio.F:921,930–934` |
| 341 | 이상 없음 | `src/xdmfio.F:940–943` |
| 342 | 이상 없음 | `src/xdmfio.F:940,944–947` |
| 345 | 이상 없음 | `src/xdmfio.F:955–959` |
| 346 | 이상 없음 | `src/xdmfio.F:955,960–964` |
| 348 | 이상 없음 | `src/xdmfio.F:970–974` |
| 349 | 이상 없음 | `src/xdmfio.F:970,975–979` |
| 350 | 이상 없음 | `src/xdmfio.F:981–985` |
| 351 | 이상 없음 | `src/xdmfio.F:981,986–991` |
| 353 | 이상 없음 | `src/xdmfio.F:997–1000` |
| 354 | 이상 없음 | `src/xdmfio.F:997,1001–1006` |
| 355 | 이상 없음 | `src/xdmfio.F:997,1001–1002,1007–1012` |
| 356 | 이상 없음 | `src/xdmfio.F:997,1001,1014–1018` |
| 357 | 이상 없음 | `src/xdmfio.F:997,1001,1014,1019–1026` |
| 362 | 이상 없음 | `src/xdmfio.F:1055–1058` |
| 363 | 이상 없음 | `src/xdmfio.F:1055,1059–1061` |
| 364 | 이상 없음 | `src/xdmfio.F:1065–1068` |
| 365 | 이상 없음 | `src/xdmfio.F:1065,1069–1071` |
| 368 | 이상 없음 | `src/xdmfio.F:1082–1085` |
| 369 | 이상 없음 | `src/xdmfio.F:1087–1090` |
| 371 | 이상 없음 | `src/xdmfio.F:1096–1101` |
| 372 | 이상 없음 | `src/xdmfio.F:1096–1097,1102–1107` |
| 377 | 이상 없음 | `src/xdmfio.F:1129–1131` |
| 378 | 이상 없음 | `src/xdmfio.F:1129,1132–1133` |
| 379 | 이상 없음 | `src/xdmfio.F:1129,1134–1135` |
| 380 | 이상 없음 | `src/xdmfio.F:1129,1136–1137` |
| 381 | 이상 없음 | `src/xdmfio.F:1129,1138–1139` |
| 382 | 이상 없음 | `src/xdmfio.F:1129,1140–1141` |
| 383 | 이상 없음 | `src/xdmfio.F:1129,1142–1143` |
| 384 | 이상 없음 | `src/xdmfio.F:1129,1144–1145` |
| 385 | 이상 없음 | `src/xdmfio.F:1129,1146–1147` |
| 386 | 이상 없음 | `src/xdmfio.F:1129,1148–1149` |
| 426 | 이상 없음 | `src/hstart.F:1562,1573–1575`<br>`src/netcdfio.F90:3887–3890,3897,3903,3905,3911–3914,5188–5189,5228`<br>`docs/technical_reference/parameter_definitions/index.rst:858` |
| 430 | 이상 없음 | `src/write_output.F:1949–1951,1955`<br>`src/adcirc.F:485–487` |
| 454 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 455 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 456 | 이상 없음 | 출력 대조 보고서 §1 |
| 457 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 458 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 459 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 460 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:852,860,1030,1038,1088,1090,1092,1094,1096,1098`<br>`src/read_input.F:3634–3636,3763–3765,3890–3892,4020–4022,4145–4147,4219–4221,4297,4301–4302,4310–4311,4315–4320,4377–4379`<br>`prep/read_global.F:2040–2044` |
| 461 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:1086,1088,1090,1094,1096`<br>`src/write_output.F:1213–1214`<br>`docs/technical_reference/output_files/fort93.rst:4` |
| 462 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:1088,1090,1092,1094,1096,1098`<br>`src/read_input.F:4297,4301–4302,4310–4311,4315–4320`<br>`prep/read_global.F:2040–2044` |
| 463 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:848,858,873`<br>`src/read_input.F:3627,3632,3637,3642` |
| 464 | 이상 없음 | `docs/technical_reference/output_files/fort61.rst:16–17`<br>`src/globalio.F:850,852`<br>`src/write_output.F:2771,2796`<br>`src/mesh.F:72`<br>`prep/post.F:1353` |
| 465 | 이상 없음 | `docs/technical_reference/output_files/fort16.rst:19,21–22,24,26–29`<br>`src/logging.F90:343,401` |
| 466 | 이상 없음 | `docs/technical_reference/output_files/fort33.rst:6`<br>`docs/technical_reference/parameter_definitions/index.rst:1245`<br>`src/gwce.F:147–149`<br>`src/itpackv.F:215–217`<br>`src/logging.F90:93,343` |
| 467 | 이상 없음 | `docs/technical_reference/output_files/fort77.rst:15`<br>`src/globalio.F:1188–1189` |
| 468 | 이상 없음 | `docs/technical_reference/output_files/fort72.rst:19`<br>`src/write_output.F:803,805,807–808`<br>`src/globalio.F:920`<br>`src/wind.F:917,948` |
| 469 | 이상 없음 | `docs/technical_reference/output_files/fort83.rst:23`<br>`docs/technical_reference/parameter_definitions/index.rst:2348`<br>`src/write_output.F:1219,1222,2080–2082`<br>`src/globalio.F:833,845,852`<br>`src/timestep.F:1639` |
| 470 | 보완 | `docs/technical_reference/output_files/fort72.rst:30`<br>`docs/technical_reference/parameter_definitions/index.rst:2327,2343`<br>`src/netcdfio.F90:1180,1184,1267–1276`<br>`docs/technical_reference/output_files/maxwvel63.rst:8`<br>`src/wind.F:908,917–918,926,948–949,1142,1164–1165`<br>`src/write_output.F:6475–6476` |
| 471 | 이상 없음 | `src/write_output.F:1048,1053`<br>`docs/technical_reference/output_files/fort77.rst:20` |
| 472 | 보완 | `docs/technical_reference/output_files/fort41.rst:82`<br>`docs/technical_reference/output_files/fort42.rst:28`<br>`docs/technical_reference/output_files/fort43.rst:28`<br>`docs/technical_reference/output_files/fort45.rst:28`<br>`docs/technical_reference/output_files/fort46.rst:30`<br>`src/read_input.F:5866–5875`<br>`src/write_output.F:3423,3426,3602,3604–3605,3710,3712,3803,3805,4008,4010,4129,4131,4201,4203`<br>`src/netcdfio.F90:3887–3890,3897,3903,3905,3911–3913` |
| 473 | 보완 | `docs/technical_reference/output_files/fort41.rst:75`<br>`src/write_output.F:3546–3547,3604–3605` |
| 474 | 이상 없음 | `docs/technical_reference/output_files/fort44.rst:21,35,37,49,51,63,65`<br>`src/cstart.F:1044,1050–1051`<br>`prep/post.F:4765–4766,4768,4782–4783,4797,4808–4809,4823,4837–4839,4854`<br>`src/write_output.F:3902–3903` |
| 475 | 이상 없음 | `docs/technical_reference/output_files/fort44.rst:21,35,37,49,51,63,65`<br>`docs/technical_reference/output_files/fort41.rst:21,38,55,72`<br>`src/write_output.F:3524–3525,3528–3529,3902–3903,3910–3911,3918–3919`<br>`prep/post.F:4290,4292–4297,4305,4336–4338,4765–4766,4768,4782–4783,4797,4808–4809,4823,4837–4839,4854`<br>`src/cstart.F:1050–1051` |
| 476 | 보완 | `docs/technical_reference/output_files/fort43.rst:21`<br>`src/write_output.F:3747–3748,3781–3782`<br>`docs/technical_reference/parameter_definitions/index.rst:2748–2749` |
| 477 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:2754,2784`<br>`src/write_output.F:3749–3750`<br>`src/netcdfio.F90:885,891,900–901`<br>`docs/technical_reference/output_files/fort46.rst:6` |
| 478 | 보완 | `docs/technical_reference/output_files/fort47.rst:6,17`<br>`src/cstart.F:1053,1055–1056,1058–1059`<br>`src/write_output.F:3880–3882,4014–4015,4029`<br>`prep/post.F:5241–5242,5248,5258–5259` |
| 479 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:2250`<br>`src/cstart.F:1031,1036,1041–1043,1081–1082,1085–1086` |
| 480 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:1199,1201,1203,1205,1207,1209,1211,1213`<br>`docs/technical_reference/output_files/fort51.rst:28`<br>`docs/technical_reference/output_files/fort52.rst:28`<br>`docs/technical_reference/output_files/fort53.rst:31`<br>`docs/technical_reference/output_files/fort54.rst:31`<br>`src/harm.F:401,409,413`<br>`src/write_output.F:2177,2728,2730,2758,2760,2811–2813,2815,2817,2821–2822,2825,2828`<br>`docs/user_guide/examples/global_astronomical_m2_tide.rst:39,41` |
| 481 | 보완 | `docs/technical_reference/output_files/fort51.rst:13,15,21`<br>`docs/technical_reference/output_files/fort52.rst:13,15,21`<br>`src/write_output.F:2771,2796`<br>`prep/post.F:1322,1353,1357,1436,1467,1471` |
| 482 | 보완 | `docs/technical_reference/output_files/fort55.rst:13,15,19–20`<br>`src/write_output.F:2703–2705,2708–2712`<br>`prep/post.F:1772,1795,1797,1825,1828–1829` |
| 483 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:2151,2161,2171`<br>`docs/technical_reference/output_files/fort51.rst:21`<br>`docs/technical_reference/output_files/fort52.rst:21`<br>`src/netcdfio.F90:909,921,926,938,949,971,1812,1833,1838,1859,1868,1889,1894,1915,1920,1941,1946,1967` |
| 484 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:2191,2201`<br>`src/harm.F:1351–1353,1355,1357–1359,1361` |
| 485 | 보완 | `docs/technical_reference/output_files/maxmin63.rst:53`<br>`src/write_output.F:1243,1275,1310,1346,1383–1386,1949,1954–1955,1958–1959,1961,1963–1964` |
| 486 | 보완 | `docs/technical_reference/output_files/maxmin63.rst:36`<br>`docs/technical_reference/output_files/maxinundepth63.rst:20`<br>`docs/technical_reference/output_files/everdried63.rst:22`<br>`docs/technical_reference/output_files/inundationtime63.rst:20`<br>`src/globalio.F:1043–1045` |
| 487 | 보완 | `docs/technical_reference/output_files/maxwvel63.rst:8`<br>`src/write_output.F:1348,6475–6477`<br>`docs/technical_reference/parameter_definitions/index.rst:2327`<br>`docs/technical_reference/output_files/fort72.rst:30`<br>`src/wind.F:908,917,926,948,1142,1164` |
| 488 | 보완 | `docs/technical_reference/output_files/maxrs63.rst:8`<br>`src/write_output.F:1392,6481,6483–6487`<br>`src/netcdfio.F90:2635` |
| 489 | 보완 | `docs/technical_reference/output_files/maxinundepth63.rst:36`<br>`docs/technical_reference/output_files/inundationtime63.rst:36`<br>`docs/technical_reference/output_files/everdried63.rst:38`<br>`src/write_output.F:1462,1497,1565,1689–1690,1692,1699,1702,1706,1708–1710,1731`<br>`src/globalio.F:1545,1551,1555,1560`<br>`src/netcdfio.F90:8374,8380,8384,8395` |
| 490 | 보완 | `docs/technical_reference/output_files/everdried63.rst:12,30`<br>`src/write_output.F:6245,6248,6411–6415` |
| 491 | 보완 | `docs/technical_reference/output_files/inundationtime63.rst:4,9,23`<br>`src/write_output.F:6245,6361–6364,6378,6380–6384`<br>`src/timestep.F:1170–1171` |
| 492 | 보완 | `docs/technical_reference/output_files/inundationtime63.rst:4,9,37`<br>`src/write_output.F:1453,1455,6364` |
| 493 | 보완 | `docs/technical_reference/output_files/nodecode63.rst:18`<br>`docs/technical_reference/output_files/noff100.rst:17`<br>`src/globalio.F:1464–1465,1467–1468`<br>`src/write_output.F:1861–1862,1921` |
| 494 | 보완 | `docs/technical_reference/output_files/initiallydry63.rst:18–19`<br>`src/globalio.F:1469–1470`<br>`src/write_output.F:6207–6209,6327–6328` |
| 495 | 보완 | `docs/technical_reference/output_files/endrisinginun63.rst:18`<br>`src/write_output.F:1515,1523,1528,1531–1532,1633–1634,1662–1663,1672,2000,6296,6301`<br>`src/globalio.F:568–571` |
| 496 | 보완 | `docs/technical_reference/output_files/noff100.rst:21–22`<br>`src/write_output.F:697,709–712,4717–4718`<br>`src/globalio.F:619,850`<br>`src/mesh.F:72` |
| 497 | 보완 | `docs/technical_reference/output_files/inundationtime63.rst:9`<br>`src/write_output.F:6363–6364`<br>`src/netcdfio.F90:3341,3344–3345,3351,3383–3384,5031–5032` |
| 498 | 보완 | `docs/technical_reference/output_files/maxinundepth63.rst:4`<br>`src/write_output.F:6361–6363,6368,6372–6373`<br>`src/netcdfio.F90:3395,3405–3406,3409–3410,3438,3440`<br>`src/timestep.F:1170–1171` |
| 499 | 보완 | `docs/technical_reference/output_files/everdried63.rst:12`<br>`src/write_output.F:6248,6411–6413,6415`<br>`src/netcdfio.F90:3505,3518,3525,3548,5034–5035` |
| 500 | 보완 | `docs/user_guide/tips_and_tricks/visualization.rst:41–42`<br>`src/netcdfio.F90:629,650,656,660,666,1534,9494,9553,9575,9585` |
| 501 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:2734`<br>`src/netcdfio.F90:830,835–837,1685,1690–1692,4388,4397–4398`<br>`src/global_3dvs.F:109,272`<br>`src/write_output.F:3157` |
| 502 | 보완 | `docs/technical_reference/output_files/fort77.rst:4,17,20`<br>`src/netcdfio.F90:2677–2680,2695,4640–4643,5064,5073–5074` |
| 503 | 보완 | `docs/technical_reference/input_files/fort6768.rst:30–35`<br>`src/write_output.F:5011–5020`<br>`prep/post.F:3977,3979,3981,3983,3985,3987,3989,3991,3993,3997,4001,4005,4009,4014,4019,4023`<br>`src/hstart.F:179,509,511,524` |
| 504 | 정정 | `docs/technical_reference/input_files/fort6768.rst:30–40`<br>`src/write_output.F:4575,4584,4593–4594,4690,4709,5012,5014–5020,5120–5123,5125–5127,5129–5130,5134–5135,5138–5139,5142–5144,5148–5149`<br>`prep/post.F:3977,3979,3981,3983,3985,3987,3989,3991,3993,3997,4001,4005,4009,4014,4019,4023`<br>`src/hstart.F:179,509,511,524,526–527` |
| 505 | 보완 | `docs/technical_reference/input_files/fort6768.rst:46–53`<br>`src/write_output.F:5220–5223,5225–5226,5228–5230,5232–5233,5235–5236,5238–5239,5241–5243`<br>`src/writer.F:1423–1424`<br>`src/hstart.F:26` |
| 506 | 정정 | `docs/technical_reference/input_files/fort6768.rst:57–62,64–68,70–76,78,80,82`<br>`src/vsmy.F:3563,3573–3579,3617–3619,3621–3623,3625–3626,3680–3681,3683–3684,3746–3748,3751–3753,3756–3758,5276–5277,5285,5293–5295`<br>`prep/post.F:4044–4045,4060–4062,4064–4066,4068–4070,4072–4074,4076–4078,4080–4082,4084–4086,4089–4091,4095–4097,4101–4103,4107–4109,4113–4115,4118,4120–4122,4125,4127–4129,4132,4134–4136,4139,4142,4148` |
| 507 | 보완 | `docs/technical_reference/input_files/fort6768.rst:88`<br>`src/write_output.F:5255,5596–5597` |
| 508 | 보완 | `docs/technical_reference/input_files/fort6768.rst:108,111,115,118,122,125,129,132`<br>`src/write_output.F:5255,5316,5319,5324,5327,5329,5334,5337,5342,5345,5347`<br>`docs/technical_reference/parameter_definitions/index.rst:1201,1205,1209,1213` |
| 509 | 보완 | `docs/technical_reference/input_files/fort6768.rst:136`<br>`src/write_output.F:5405,5408,5410,5418` |
| 510 | 보완 | `docs/technical_reference/input_files/fort6768.rst:26,149`<br>`docs/technical_reference/parameter_definitions/index.rst:1225,1227`<br>`src/write_output.F:5587,5591,5595`<br>`src/netcdfio.F90:6869,6876–6877` |
| 511 | 보완 | `docs/technical_reference/input_files/fort6768.rst:16,152`<br>`src/hstart.F:714–716,720–723,725,727–732,735–736,744–747` |
| 512 | 이상 없음 | `docs/technical_reference/output_files/noff100.rst:28`<br>`src/netcdfio.F90:5492–5494,5496–5497` |
| 513 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:28,38,58,123,133,492`<br>`src/netcdfio.F90:4095–4096,4098,4100,4103,4105,4110,9691–9693,9712,9721,9805,9811,9840,9853,9990,10019–10020,10029,10032,10455–10458` |
| 514 | 보완 | `docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:77,163–164,168–169`<br>`src/write_output.F:1949,1977–1978,1980,1982,1984,1986,1988,1990,5793,5868–5871,5884,5914,5930,5960,5976,6006,6022,6052,6070,6100,6116,6146,6162` |
| 515 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:1225,1227`<br>`docs/technical_reference/input_files/fort6768.rst:55,88–89,100,104`<br>`src/timestep.F:1196,1200–1204,1207`<br>`src/writer.F:1358,1360,1375,1387,1391,1395,1399,1403,1413,1417,1447,1449–1450,1452–1453,1455–1459,1464,1516`<br>`prep/post.F:3454–3456,3616,3649,3886,3895,3904,3906,4023,4026,4153,4155`<br>`src/write_output.F:5153,5156,5158,5174,5186,5204,5220,5255,5305` |
| 516 | 보완 | `docs/user_guide/model_configuration/meteorological_forcing/wind_stress.rst:142–148`<br>`src/write_output.F:955–959,963–964,966` |
| 517 | 보완 | `docs/technical_reference/output_files/fort71.rst:16`<br>`docs/technical_reference/output_files/fort91.rst:14`<br>`docs/technical_reference/output_files/fort43.rst:15,20`<br>`prep/post.F:1898,1913–1914,1924,1937–1938,1940,2967,2982–2983,2993,3006–3007,3009,4594,4610,4644–4645` |
| 518 | 보완 | `docs/technical_reference/parameter_definitions/index.rst:2704,2709,2714`<br>`src/netcdfio.F90:700,715,732,1570,1582,1595,4344–4345,4348–4349,4351–4352,4356–4358,4361–4362,4370–4372,4375–4376,10455–10458` |
| 519 | 보완 | `docs/technical_reference/output_files/maxinundepth63.rst:4`<br>`src/netcdfio.F90:3394–3395,3437–3438,10455–10458`<br>`src/write_output.F:6372–6373` |
| 520 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 521 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 522 | 이상 없음 | `src/read_input.F:3647,3650,4154,4156,4228,4230,4386,4388` |
| 523 | 이상 없음 | `src/read_input.F:4756–4759` |
| 524 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:850,858,1028,1036`<br>`src/hstart.F:1562–1563,1571` |
| 525 | 이상 없음 | `src/read_input.F:3642,3647,4154`<br>`src/hstart.F:1562,1573`<br>`src/netcdfio.F90:3888–3889` |
| 526 | 이상 없음 | `src/globalio.F:972–973,1020–1021`<br>`docs/technical_reference/output_files/fort63.rst:15` |
| 527 | 이상 없음 | `src/globalio.F:641,698,731` |
| 528 | 이상 없음 | `src/write_output.F:488`<br>`src/globalio.F:834–835,839` |
| 529 | 이상 없음 | `src/xdmfio.F:60–61,77,138,184,202,334,339` |
| 530 | 이상 없음 | `src/write_output.F:636–640,646` |
| 531 | 이상 없음 | `src/write_output.F:560,568–569,571–572,734–736,738–739` |
| 532 | 이상 없음 | `src/write_output.F:979,1019,1027`<br>`src/netcdfio.F90:547–550,4270–4273`<br>`src/read_input.F:3893,3898` |
| 533 | 이상 없음 | `src/write_output.F:1027,1033–1034` |
| 534 | 이상 없음 | `docs/technical_reference/output_files/fort81.rst:7`<br>`docs/technical_reference/output_files/fort83.rst:7`<br>`src/read_input.F:3870,3877,4297,4304`<br>`src/write_output.F:434–435,1182–1192,1200–1202,1213–1225,1850–1856` |
| 535 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:1456,1491,1520,1549,1573,1597`<br>`src/read_input.F:5857–5860` |
| 536 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:1460,1495,1524,1553,1577,1601`<br>`src/read_input.F:5863–5865` |
| 537 | 이상 없음 | `src/read_input.F:5876,5882,5889,5897` |
| 538 | 이상 없음 | `src/cstart.F:1024–1026` |
| 539 | 정정 | `src/netcdfio.F90:675–676,737–738,849–850,1544–1548` |
| 540 | 이상 없음 | `docs/technical_reference/output_files/fort47.rst:6`<br>`src/cstart.F:1053–1056,1064–1065` |
| 541 | 이상 없음 | `src/write_output.F:4008,4014–4015,4029`<br>`src/netcdfio.F90:1757,1770` |
| 542 | 이상 없음 | `src/harm.F:401,409,413`<br>`src/write_output.F:2758,2760,2811` |
| 543 | 이상 없음 | `src/harm.F:1527–1529,1531,1533–1535,1537,1539–1541,1543,1545–1547,1549` |
| 544 | 이상 없음 | `src/write_output.F:1255–1256,1463–1464,1498–1499,1566–1567,4416,4424,4465,4472,4479,4497` |
| 545 | 이상 없음 | `src/timestep.F:1170–1171`<br>`src/write_output.F:1995–1996,1998,2000,2002,6291,6294,6307,6320–6322,6327` |
| 546 | 이상 없음 | `src/netcdfio.F90:81–82,1340–1341,1343–1344,2698` |
| 547 | 이상 없음 | `src/netcdfio.F90:3987–3989,5228,10061,10064,10066–10068,10071` |
| 548 | 이상 없음 | `src/netcdfio.F90:620–622,624–625,647–648,650–651,655–657,9913,9916,9918,9920,9922,9925,9927,9929,9931,9935–9936,9938,9941–9942,9945–9946,9948,9950–9952` |
| 549 | 이상 없음 | `docs/technical_reference/input_files/fort22.rst:102–103,135,137`<br>`src/wind.F:917,948`<br>`src/netcdfio.F90:1273–1276,2475,2588,3124,4549–4550,4552–4553` |
| 550 | 이상 없음 | `docs/technical_reference/output_files/fort93.rst:28`<br>`src/wind.F:1396–1397,1399,1727,1729`<br>`src/netcdfio.F90:1299,1302,2718,2722,5073–5074` |
| 551 | 정정 | `src/netcdfio.F90:906–907,909–910,947–950,1865–1866,1868–1870,3756–3757,3764–3765,3768` |
| 552 | 정정 | `src/netcdfio.F90:1034–1037,1058–1061,2000–2004,2257–2261` |
| 553 | 정정 | `src/netcdfio.F90:1167–1170,1172–1173,1289–1290,1292–1293,1302,2705–2707,2709–2710` |
| 554 | 이상 없음 | `src/netcdfio.F90:1314–1317,3557–3561`<br>`src/write_output.F:865–869,871,873–876` |
| 555 | 정정 | `src/netcdfio.F90:1755–1759,1776–1780,2741–2746,2748–2749` |
| 556 | 정정 | `src/netcdfio.F90:2027–2031,2033–2034,3341,3343–3345,3505–3506,3510–3511` |
| 557 | 정정 | `src/netcdfio.F90:2677–2680` |
| 558 | 정정 | `docs/user_guide/tips_and_tricks/coupled_adcirc_swan.rst:186–187`<br>`src/write_output.F:1979,1991,5893–5894,5909,5954,6000,6046,6094,6140,6186`<br>`src/netcdfio.F90:3159–3162` |
| 559 | 정정 | `src/netcdfio.F90:9507,9540,9545,9551–9552,9574,9578–9580,9584,9605,9609,9691–9693,9721` |
| 560 | 이상 없음 | `src/netcdfio.F90:6786,6788,6790–6791,10124,10126,10189–10190,10293–10294` |
| 561 | 이상 없음 | `src/xdmfio.F:80–81,187,193,259,351,369–370` |
| 562 | 이상 없음 | `src/xdmfio.F:217–219,222,224–225,231–232,235,237–238,244–245,248,250–252,259,265–270,279,283,290–291,293,298–299,301–305` |
| 563 | 정정 | `src/write_output.F:484–485,1861–1862,4310–4312,4348–4349`<br>`src/xdmfio.F:151,154,166,173–175,178,264–265,269–270,284–285,329–332,335,338,340,351,359–361,369–370,375` |
| 564 | 이상 없음 | `src/write_output.F:1648,1650–1651`<br>`src/xdmfio.F:721–722,778,780,782–784,1035–1038,1148–1149` |
| 565 | 이상 없음 | `src/xdmfio.F:473–474,483–484,505,510,519,545,554,559,564,569,574,579` |
| 566 | 이상 없음 | `prep/post.F:1315,1325–1327,1338–1339` |
| 567 | 이상 없음 | `prep/post.F:5348,5350–5351,5379,5396–5397,5400–5401,5420–5422,5470,5477,5483,5489,5494,5522,5524,5527,5533,5538–5539,5542`<br>`prep/post_global.F:108,118–121,123` |
| 568 | 보완 | `src/writer.F:559,665–666,674–675,679,683–685` |
| 569 | 보완 | `src/harm.F:359,368,371,374` |
| 570 | 이상 없음 | `src/write_output.F:1420–1422,1424–1426,1971–1973` |
| 571 | 이상 없음 | `src/write_output.F:5743–5744,5751–5753,5756–5759` |
| 572 | 이상 없음 | `src/read_input.F:3647–3650,4023,4029,4035–4036,4154,4386,4395` |
| 573 | 이상 없음 | `src/globalio.F:972–973,1020–1021` |
| 574 | 이상 없음 | `src/write_output.F:4341–4343`<br>`src/writer.F:715–717` |
| 575 | 보완 | `src/read_input.F:3627,3632,3634,3637,3642`<br>`src/hstart.F:1562,1573`<br>`src/netcdfio.F90:3888–3889` |
| 576 | 이상 없음 | `src/write_output.F:3043,3517,3524,3528,3546–3547,3687–3689` |
| 577 | 이상 없음 | `src/xdmfio.F:52,78,369–370` |
| 578 | 이상 없음 | `src/netcdfio.F90:81–82,2698,5605–5606` |
| 579 | 이상 없음 | `src/write_output.F:1462,1497,1565,1699,1702,1706,1731` |
| 580 | 이상 없음 | `prep/post.F:1924,1938,2993,3007,4336–4338,4610,4644` |
| 581 | 이상 없음 | `docs/technical_reference/parameter_definitions/index.rst:536,545,864,866`<br>`src/read_input.F:3657,3661–3662` |
| 582 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 583 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 584 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 585 | 이상 없음 | outputs 보고서 §5 L1446(N01)<br>outputs 보고서 §5 L1446 |
| 586 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 587 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 588 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 589 | 보완 | `src/read_input.F:3634–3636` |

### source-analysis/adcirc-parameter-glossary-v1.md

| 초기 줄 | 결과 | 대조한 원문·참조 |
|---:|---|---|
| 15 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 71 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 72 | 이상 없음 | `docs/user_guide/model_configuration/model_parameters/tau0.rst:204–205,212–214`<br>`src/nodalattr.F:2149,2151–2153,2155,2158–2159` |
| 73 | 이상 없음 | `src/nodalattr.F:2149,2151–2153,2155,2158–2159` |
| 74 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |

### source-analysis/adcirc-preprocessing-foundation.md

| 초기 줄 | 결과 | 대조한 원문·참조 |
|---:|---|---|
| 11 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 41 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 42 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 43 | 보완 | `docs/user_guide/running_adcirc/command_line_options.rst:41–42,44,47,50,74`<br>`src/sizes.F:234,236,238,240,249,271,287` |
| 44 | 보완 | `docs/user_guide/running_adcirc/command_line_options.rst:41,44–45,47,50,74`<br>`src/sizes.F:234,249–250,252,271,287` |
| 45 | 보완 | `docs/user_guide/running_adcirc/command_line_options.rst:41,44,47–48,50,74`<br>`src/sizes.F:234,249,271,273,275,277,287` |
| 46 | 보완 | `docs/user_guide/running_adcirc/command_line_options.rst:41,44,47,50–51,74`<br>`src/sizes.F:234,249,271,287–288,290` |
| 47 | 보완 | `src/sizes.F:191,198,205,211–212,216,221,231,299–300`<br>`src/adcirc.F:185–186,188,194–195`<br>`prep/adcprep.F:198–200,211–212,217,231,235,250,254–257` |
| 48 | 보완 | `src/adcirc.F:185–186,188,192,194–196`<br>`src/sizes.F:191,198,205,211–212,216,221,231,299–300`<br>`prep/adcprep.F:198–200,211–212,217,231,235,250,254–257` |
| 49 | 이상 없음 | `docs/user_guide/running_adcirc/command_line_options.rst:99–100`<br>`prep/adcprep.F:209–210,254–257`<br>`prep/presizes.F:262` |
| 50 | 보완 | `prep/adcprep.F:198–200,211–212,217,231,235,250,254–257`<br>`src/sizes.F:191,198,205,211–212,216,221,231,299–300`<br>`src/adcirc.F:185–186,188,194–195` |
| 51 | 보완 | `prep/adcprep.F:198–200,211–212,217,231,235,250,254–257`<br>`src/sizes.F:191,198,205,211–212,216,221,231,299–300`<br>`src/adcirc.F:185–186,188,194–195` |
| 52 | 보완 | `wind/aswip.F:2860,2863,2865,2867,2869,2871,2873,2875,2880,2884,2892,2895,2897,2900,2910,2914,2919,2922,2926,2929–2930,2933,2935,2938,2945,2948` |
| 53 | 보완 | `wind/aswip.F:2860,2863,2865,2867,2869,2871,2873,2875,2880,2884,2892,2895,2897,2900,2910,2914,2919,2922,2926,2929–2930,2933,2935,2938,2945,2948` |

### source-analysis/adcirc-topic-map.md

| 초기 줄 | 결과 | 대조한 원문·참조 |
|---:|---|---|
| 21 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 40 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 41 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 42 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 43 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 44 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 45 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 46 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 47 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 48 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 49 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 50 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 51 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 52 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 53 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 54 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 55 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 56 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 57 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 58 | 이상 없음 | `src/nodalattr.F:2487–2489`<br>`docs/user_guide/special_features/dynamic_water_level_correction.rst:12–14`<br>`src/wind.F:241–242`<br>`src/read_input.F:769–772`<br>`src/timestep.F:648–649`<br>`src/gwce.F:2007,2020`<br>`src/write_output.F:757,764,797,807,839,846,928,936` |
| 59 | 보완 | `src/nodalattr.F:2481–2483,2487–2489,2562` |
| 60 | 보완 | `docs/user_guide/special_features/dynamic_water_level_correction.rst:12–14,31,98–100`<br>`src/write_output.F:874–875,1596–1597,1601–1602`<br>`src/wind.F:241–242`<br>`src/read_input.F:769–772`<br>`src/timestep.F:648–649`<br>`src/gwce.F:2007,2020` |
| 61 | 이상 없음 | `docs/technical_reference/input_files/fort25.rst:42–43,47`<br>`src/wind.F:124,126,132,139,764,767,772,778`<br>`src/read_input.F:1775–1776,2316`<br>`src/write_output.F:757,764,797,807,839,846,928,936,1071–1075,1078,1096–1097,1105–1107` |
| 62 | 보완 | `src/timestep.F:468,495–502,519,531` |
| 63 | 이상 없음 | `docs/user_guide/model_configuration/tides/ali_dispersion_conrtol.rst:23–24,36–37,41–42,45,47–48`<br>`src/read_input.F:1233,1362–1368`<br>`src/momentum.F:459–468,470`<br>`src/gwce.F:511–516` |
| 64 | 보완 | `src/subgridLookup.F:195,198,204,231–232,236,240,243,257–258,273,287,301,316,375,379,382–384,391,394–398,400–401,403,410–417,424,432,439` |
| 65 | 이상 없음 | `docs/technical_reference/input_files/time_varying_weirs.rst:3,40,43–50`<br>`src/global.F:324`<br>`src/weir_boundary.F90:997–998,1097,1133–1135,1140–1142,1163`<br>`docs/user_guide/special_features/vertical_element_walls.rst:18,77`<br>`src/momentum.F:1020,1089`<br>`docs/technical_reference/parameter_definitions/index.rst:357`<br>`src/read_input.F:1352–1354,3010`<br>`src/gwce.F:1941,2014–2016`<br>`src/vew1d.F90:150–151,156,159,161,170–171,189` |
| 66 | 정정 | `docs/technical_reference/parameter_definitions/index.rst:1699`<br>`src/read_input.F:4622–4623,5637–5638,5641–5642,5646,5705,5707,5715`<br>`src/wind.F:1675`<br>`src/vsmy.F:742`<br>`src/transport.F:867`<br>`src/cstart.F:490`<br>`docs/technical_reference/input_files/fort13.rst:338`<br>`src/nodalattr.F:547–548,1337–1339,1555–1556`<br>`src/gwce.F:525–527` |
| 67 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 68 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 72 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |
| 73 | 정정 | `docs/user_guide/model_configuration/meteorological_forcing/generalized_asymmetric_holland_model.rst:605–610` |
| 74 | 정정 | `docs/tools/subgrid_adcirc_utility.rst:11,18`<br>`src/subgridLookup.F:195–196,198–199,201–202,204–205,273–274,287–288,301–302,316–317` |
| 75 | 이상 없음 | 구조·참조 또는 같은 절의 원문 연결 |

## 검증 종료 확인

초기 대상 906줄을 대조대장에 모두 배정했다. 정정·보완 표의 379개 초기 줄은 노트 수정과 대응한다. 새 E 후보는 해당 입력·출력 조건을 명시했다. 기존 E의 실행 실패와 영향 크기를 확정하지 않았다. 지정 파일의 `git diff --check`는 통과했다. 모델 실행과 git 상태 변경은 하지 않았다.

정정 75, 보완 304, 분류 변경 52, 이상 없음 527

