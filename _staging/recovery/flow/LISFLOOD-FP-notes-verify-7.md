# LISFLOOD-FP 노트 전수 검증 7

검증일: 2026-10-21.
대상은 사용자가 지정한 신규 노트 두 파일의 전체 줄이다.
원문 코드와 최종 결론 근거를 대조한다.
수정은 대상 노트와 이 기록에만 적용한다.

| 대상 노트 | 상태 | 대조한 원래 줄 수 | 정정 수 | 보완 수 |
|---|---|---:|---:|---:|
| `models/LISFLOOD-FP/source-analysis/lisflood-fp-build-and-83-release.md` | 완료 | 127 | 11 | 2 |
| `models/LISFLOOD-FP/source-analysis/lisflood-fp-metal-fv1.md` | 완료 | 83 | 5 | 1 |

줄 수는 검증 시작 시 파일의 전체 줄을 센 값으로 기록한다.
정정 수와 보완 수는 각각 표식을 붙인 수정 줄 수로 기록한다.
정정 목록의 줄 번호는 수정 후 노트를 기준으로 기록한다.

## 빌드 구성과 8.3 릴리스 노트 완료

대상: [lisflood-fp-build-and-83-release.md](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-build-and-83-release.md).
전체 127줄을 대조했다.
정정 표식은 11줄이다.
보완 표식은 2줄이다.
이 수는 검증 시작 시 전체 줄과 수정 후 표식을 각각 세어 얻었다.
배정표 job-5의 해당 43행은 노트의 차이 표 43행과 일치한다.
최종 분류는 43행 모두 배정표와 일치한다.
LN1-127은 claude-final의 E·중간을 유지했다.
LG1-130·131은 E·강함과 8.2 결함의 8.3 수정 표시를 유지했다.

| 대조한 원래 줄 | 대조 내용과 근거 |
|---|---|
| 1–17 | frontmatter 전체를 CONVENTIONS §2, notes-apply-5 및 job-5와 대조했다. 관련 노트 세 경로가 존재한다. |
| 18–28 | 제목·판·DOI·체크포인트 번호를 배포 README:19–26, VersionHistory.h:16–23, 최종 LN1-230·LB1-408과 대조했다. |
| 29–51 | CMakeLists.txt, config.default.cmake, lisflood.h, sgm_fast.cpp, FindNUMA.cmake, makefile, INSTALL.md, pars.cpp, file_tool.cpp를 직접 열었다. 기본값·조건·실행 대상·TESTING 정의를 대조했다. |
| 52–69 | 현재 CUDA 코드와 v8.0·v8.1·v8.2의 해당 배열 할당·해법 호출·패스 끝을 직접 열었다. 배포 패치의 대응 hunk 및 최종 LG1-130–132·LN1-127·231과 대조했다. |
| 70–84 | 문서 표지·DOCX 판 이력·접두어·분류 설명·최종 근거 링크를 대조했다. 문서 쪽 번호는 LibreOffice 변환본 기준으로 명시했다. |
| 85–100 | LB1-036·037·049·239·265·381 및 LN1-012·016·017·084·093·101–104·127의 모든 칸을 최종 결론과 원문에 대조했다. 구판 README·설정·INSTALL·makefile·format도 직접 열었다. |
| 101–114 | LN1-130·151·152·181·185·230·231, LG1-130–132·160, LV1-175·276·291의 모든 칸을 대조했다. 배포 루트와 source 하위의 .git 부재도 확인했다. |
| 115–127 | LI1-294–296·340, LT1-120–124·135·180·301·400의 모든 칸을 대조했다. bf804e23의 README:1–14를 git show로 열었다. |

수치·판·표는 PDF p.1·5·13·40·41, DOCX p.1·5, 교량 DOCX p.1·5·6·18·19·41의 쪽 이미지를 판독했다.
나머지 문서 인용은 해당 쪽 판독 기록과 최종 결론 행을 대조했다.
빌드·CPU/GPU 보고서 §4의 적용 판 수정안과 notes-apply-5의 연결 행을 대조했다.
외부 출처 보고서의 최종 두 행은 이 노트에 해당하지 않는다.
Mermaid 블록은 없다.
상대 링크의 대상은 모두 존재한다.
절대 경로·홈 축약·위키 링크·검수 유보 문장은 없다.

### 정정·보완 목록

아래 경로의 줄 번호는 수정 후에도 원래 줄 번호와 같다.
표식은 본문 줄 끝 또는 표의 결론 문장 칸 끝에 붙였다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| [lisflood-fp-build-and-83-release.md:25](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-build-and-83-release.md#L25) | 정정 | 8.3 DOI를 단정한 문장과 이를 뒷받침하지 않는 보고서 §1 인용을 패치 제공 관계로 교체했다. | 배포 README:19–24는 8.2 DOI 13121102와 8.3 패치 적용 명령을 적는다. 최종 LB1-408은 이 대목을 8.3 DOI의 근거로 쓰지 않도록 한다. |
| [lisflood-fp-build-and-83-release.md:36](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-build-and-83-release.md#L36) | 정정 | config.default.cmake:4 → config.default.cmake:6. | 4행은 add_compile_definitions(_PROFILE_MODE=0)이다. 6행은 add_compile_definitions(_CALCULATE_Q_MODE=1)이다. |
| [lisflood-fp-build-and-83-release.md:68](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-build-and-83-release.md#L68) | 보완 | Metal 정의 위치에 Apple 분기와 두 프레임워크 조건의 인용을 추가했다. | CMakeLists.txt:232는 if (APPLE)이다. metal/CMakeLists.txt:6은 if(METAL_FRAMEWORK AND FOUNDATION_FRAMEWORK)이다. 같은 파일 29행이 METAL_ENABLED를 정의한다. |
| [lisflood-fp-build-and-83-release.md:73](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-build-and-83-release.md#L73) | 정정 | DOCX 판 이력 맨 위 5.9 → 8.0·2020-07-20 및 표지 변경 추적. 8.3 DOI 귀속을 제거하고 문서별 쪽 인용을 붙였다. | DOCX p.1·5 쪽 이미지에는 8.0.0 삽입과 8.0 Jul 20 2020 행이 있다. PDF·교량 DOCX p.1 이미지, AD1:41–43, 배포 README:19–24, VersionHistory.h:16–23을 대조했다. |
| [lisflood-fp-build-and-83-release.md:75](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-build-and-83-release.md#L75) | 보완 | 구판 접두어 설명에 실제 배포본 상대 링크를 붙였다. v8.3 접두어를 추가했다. | 사용자가 지정한 네 추출 경로와 각 README.md 파일의 존재를 확인했다. |
| [lisflood-fp-build-and-83-release.md:85](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-build-and-83-release.md#L85) | 정정 | only the executable files → only the executable is distributed. 생략한 BUSCOT 파일명 접두어를 복원했다. | 교량 DOCX p.18 이미지의 표 3과 바로 아래 문장은 전체 파일명과 only the executable is distributed를 적는다. 최종 LB1-036도 이 인용을 교정한다. |
| [lisflood-fp-build-and-83-release.md:91](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-build-and-83-release.md#L91) | 정정 | 구판 README와 짝인 탐색 모듈 인용에 v8.0을 명시했다. | v8.0:cmake/Modules/FindNUMA.cmake:10,14도 NUMA_ROOT_DIR를 사용한다. 최종 LN1-012는 같은 v8.0 배포본끼리 대조한다. |
| [lisflood-fp-build-and-83-release.md:92](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-build-and-83-release.md#L92) | 정정 | config.default.cmake:9 → v8.0:config.default.cmake:9. | 현재 기본 설정은 8줄이다. v8.0·v8.1의 9행은 CMAKE_CUDA_FLAGS를 지정한다. 최종 LN1-016과 일치한다. |
| [lisflood-fp-build-and-83-release.md:93](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-build-and-83-release.md#L93) | 정정 | 구판 INSTALL과 짝인 makefile 인용에 v8.0을 명시했다. | v8.0:INSTALL.md:3은 Makefile.new를 지정한다. 실제 v8.0:makefile:1은 -include $(CONFIG)이다. |
| [lisflood-fp-build-and-83-release.md:98](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-build-and-83-release.md#L98) | 정정 | float 설정:2 → ../LISFLOOD-FP-8.3-package/config.float.cmake:2. | 배포 config.float.cmake:2는 add_compile_definitions(_NUMERIC_MODE=0)이다. |
| [lisflood-fp-build-and-83-release.md:100](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-build-and-83-release.md#L100) | 정정 | 현재 소스 루트에 없는 패치 파일 인용을 배포 경로로 바꿨다. 최우선 LN1-127 조정에 직접 링크했다. | 배포 패치:264–268은 format의 5 한 줄을 삭제한다. claude-final:13은 E·중간과 8.2 결함의 8.3 수정을 지정한다. |
| [lisflood-fp-build-and-83-release.md:106](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-build-and-83-release.md#L106) | 정정 | 패치 인용에 ../LISFLOOD-FP-8.3-package/를 붙였다. | 배포 패치:33–35는 체크포인트 번호 유지 주석과 LF_Release 8.3을 추가한다. |
| [lisflood-fp-build-and-83-release.md:118](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-build-and-83-release.md#L118) | 정정 | 반영 전 노트 인용에서 현재 판 비교와 무관한 GitHub 미확인 문장을 제외했다. | git show bf804e23:models/LISFLOOD-FP/README.md의 14행에서 DOI와 v8.2 아카이브 문장만 인용했다. 사용자 검사 항목 6을 적용했다. |

### 기계 확인 후보 판정

사용자가 열거한 순서를 유지했다.
같은 파일·줄이 다시 나온 후보도 별도 행으로 기록했다.
후보의 들여쓰기·줄 끝 문자·Markdown 백틱은 내용과 구분했다.
LN1-016의 구판 설정 인용은 위 정정 목록에서 별도로 고쳤다.

| 번호 | 노트 줄 | 원문 파일:줄과 확인한 내용 | 판정 |
|---|---:|---|---|
| 1 | 86 | CMakeLists.txt:26 — target_sources(lisflood-base INTERFACE | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 2 | 88 | CMakeLists.txt:19 — set(CMAKE_CXX_STANDARD 14) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 3 | 92 | README.md:65 — To customise the CUDA compute capabilities, see &#96;config.default.cmake&#96;. | 서식 차이이다. 원문은 config.default.cmake를 백틱으로 둘렀다. 문구와 줄 번호는 맞으므로 유지했다. |
| 4 | 92 | CMakeLists.txt:4 — if(NOT DEFINED CMAKE_CUDA_ARCHITECTURES) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 5 | 107 | CMakeLists.txt:204 — if (UNIX AND NOT APPLE) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 6 | 108 | v8.2:cuda/cuda_max_field.cu:96 — if (acceleration) { | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 7 | 112 | CMakeLists.txt:67 — add_executable(lisflood) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 8 | 115 | CMakeLists.txt:210 — if (_NETCDF) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 9 | 115 | CMakeLists.txt:211 — if (WIN32) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 10 | 115 | CMakeLists.txt:212 — target_include_directories(lisflood-base INTERFACE windep/netCDF4-64/include) # TODO: x64 only | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 11 | 115 | CMakeLists.txt:213 — target_link_directories(lisflood-base INTERFACE windep/netCDF4-64/lib) # TODO: x64 only | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 12 | 115 | CMakeLists.txt:214 — target_link_libraries(lisflood-base INTERFACE netcdf) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 13 | 115 | CMakeLists.txt:215 — file(GLOB DLLS "DLL's/*.dll") | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 14 | 115 | CMakeLists.txt:216 — file(COPY ${DLLS} DESTINATION ${CMAKE_BINARY_DIR}) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 15 | 115 | CMakeLists.txt:217 — else() | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 16 | 115 | CMakeLists.txt:218 — find_package(NetCDF REQUIRED) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 17 | 115 | CMakeLists.txt:219 — target_include_directories(lisflood-base INTERFACE ${NetCDF_INCLUDE_DIRS}) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 18 | 115 | CMakeLists.txt:220 — target_link_libraries(lisflood-base INTERFACE NetCDF::NetCDF) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 19 | 115 | CMakeLists.txt:221 — endif() | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 20 | 115 | CMakeLists.txt:222 — target_compile_definitions(lisflood-base INTERFACE _NETCDF=1) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 21 | 115 | CMakeLists.txt:223 — else() | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 22 | 115 | CMakeLists.txt:224 — target_compile_definitions(lisflood-base INTERFACE _NETCDF=0) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 23 | 115 | CMakeLists.txt:225 — endif() | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 24 | 116 | CMakeLists.txt:72 — check_language(CUDA) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 25 | 116 | CMakeLists.txt:73 — if (CMAKE_CUDA_COMPILER) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 26 | 116 | CMakeLists.txt:74 — enable_language(CUDA) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 27 | 116 | CMakeLists.txt:75 — set_property(TARGET lisflood PROPERTY CUDA_SEPARABLE_COMPILATION ON) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 28 | 116 | CMakeLists.txt:77 — add_compile_definitions(CUDA THRUST_IGNORE_CUB_VERSION_CHECK) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 29 | 116 | CMakeLists.txt:231 — # Metal GPU back end for FV1 (Apple Silicon) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 30 | 116 | CMakeLists.txt:232 — if (APPLE) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 31 | 116 | CMakeLists.txt:233 — add_subdirectory(metal) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 32 | 116 | CMakeLists.txt:234 — if (METAL_ENABLED) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 33 | 116 | CMakeLists.txt:235 — target_link_libraries(lisflood PRIVATE ${METAL_LIBRARY}) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 34 | 116 | CMakeLists.txt:236 — endif() | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 35 | 116 | CMakeLists.txt:237 — endif() | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 36 | 119 | CMakeLists.txt:67 — add_executable(lisflood) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 37 | 121 | CMakeLists.txt:231 — # Metal GPU back end for FV1 (Apple Silicon) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 38 | 123 | CMakeLists.txt:210 — if (_NETCDF) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |
| 39 | 124 | CMakeLists.txt:204 — if (UNIX AND NOT APPLE) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |


## Metal FV1 노트 완료

대상: [lisflood-fp-metal-fv1.md](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-metal-fv1.md).
검증 시작 시 전체 83줄을 대조했다.
누락된 frontmatter 필드 두 줄을 추가하여 수정 후에는 85줄이다.
정정 표식은 5줄이다.
보완 표식은 1줄이다.
이 수는 파일의 전체 줄과 표식을 직접 세어 얻었다.
배정표 job-6의 해당 29행은 노트의 차이 표 29행과 일치한다.
분류·강도·결론 문장은 최종 근거와 일치한다.
LV1-290은 결론을 유지하고 문서 쪽 인용을 정정했다.

| 대조한 원래 줄 | 대조 내용과 근거 |
|---|---|
| 1–17 | frontmatter 전체를 CONVENTIONS §2·§8.1과 notes-apply-6에 대조했다. 관련 노트 경로와 source_scope가 존재한다. 신규 파일의 layer·depends_on 누락을 고쳤다. |
| 18–34 | AI 정리·원문 구분·코드 경로·패키지 경로·문서 판을 대조했다. DOCX 표지와 판 이력은 쪽 이미지로 판정했다. |
| 35–45 | LB1-347·380과 LN1-137–139·186–191의 모든 칸을 최종 근거와 원문에 대조했다. 빌드·실행·초기화·강우 거부·기준면·부호·배열 복사 조건을 확인했다. |
| 46–54 | LG1-009·010·014·015·019·020·026–028의 모든 칸을 대조했다. HLL·마찰·수심 절단·CFL·점 원천·NoData의 조건과 식을 CPU·CUDA·Metal 원문에서 확인했다. |
| 55–59 | LG1-124–126·149·151의 모든 칸을 대조했다. 강우 원점·범위·부호·업로드 조건과 FREE6를 확인했다. updateBoundaryFluxes는 정의만 있다. accumulateOutflowPipeline은 선언·생성·유효성 검사만 있다. 실제 질량 집계는 account_boundary 호출을 사용한다. |
| 60–63 | LV1-285·290, LI2-341, LI1-255의 모든 칸을 대조했다. 공유 출력 함수·가상 단면·최대 수심 복사와 8.3 패치의 metal 별칭을 확인했다. |
| 64–75 | 본문의 실행 선택을 lisflood.cpp:778–788과 metal_integrate.cpp:7–14에 대조했다. 연결한 구현 차이 노트의 자료형·시간 간격 항목과 아키텍처 맵의 실행 분기를 확인했다. |
| 76–83 | 보고서와 최종 근거의 상대 링크를 모두 확인했다. |

문서 판은 PDF p.1, DOCX p.1·5, 교량 DOCX p.1의 쪽 이미지를 사용했다.
강우 원점 조건은 DOCX p.37 이미지로 판정했다.
LV1-290의 기존 DOCX p.32·41 및 PDF p.27·36을 이미지로 확인했다.
대체 인용인 DOCX p.36·42 및 PDF p.31·37도 이미지로 확인했다.
입력·해법 표의 Metal 누락은 해당 쪽 판독 기록과 최종 근거에 대조했다.
본문의 실행 분기는 callflow §4의 10-21 Claude 수정본과 일치한다.
보고서 §4·callflow §6에는 이 새 노트 경로를 직접 지목한 수정안이 없다.
Mermaid 블록은 없다.
상대 링크의 대상은 모두 존재한다.
절대 경로·홈 축약·위키 링크·검수 유보 문장은 없다.


### 정정·보완 목록

원래 13행 이후의 줄 번호는 frontmatter 필드 추가로 2씩 증가했다.
아래 줄 번호는 수정 후 노트의 번호다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| [lisflood-fp-metal-fv1.md:13](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-metal-fv1.md#L13) | 정정 | layer 필드 없음 → layer: 2. | CONVENTIONS.md:184–190은 신규 노트의 layer를 요구한다. 모델 구현 분석이므로 레이어 2이다. |
| [lisflood-fp-metal-fv1.md:14](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-metal-fv1.md#L14) | 정정 | depends_on 필드 없음 → depends_on: []. | CONVENTIONS.md:190–191은 신규 파일의 근거 의존 경로 목록을 요구한다. 이 노트는 원문 코드·문서와 판독 근거를 사용한다. 관련 canonical 노트는 탐색 링크이다. |
| [lisflood-fp-metal-fv1.md:33](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-metal-fv1.md#L33) | 정정 | 판 이력 맨 위 5.9 → 8.0·2020-07-20 및 표지 변경 추적. 근거가 없는 8.3 DOI 귀속을 제거했다. | DOCX p.1·5, PDF p.1, 교량 DOCX p.1 쪽 이미지. AD1:41–43. 최종 LB1-408. 배포 README:19–24와 VersionHistory.h:16–23. |
| [lisflood-fp-metal-fv1.md:63](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-metal-fv1.md#L63) | 정정 | gauge·최대 수심의 문서 인용을 DOCX p.32·41 / PDF p.27·36에서 DOCX p.36·42 / PDF p.31·37로 고쳤다. | 원래 인용 쪽은 DEM·공극률 또는 mass·overpass 출력 절이다. 새 인용 쪽 이미지에는 3.2.19 Virtual gauge와 5.2.5 Maximum water depth 절이 있다. LV1-290의 결론은 유지했다. |
| [lisflood-fp-metal-fv1.md:72](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-metal-fv1.md#L72) | 정정 | FV1 분기 설명에 METAL_ENABLED 전처리 조건을 명시했다. | lisflood.cpp:780의 #ifdef METAL_ENABLED와 782행의 런타임 조건. 최종 LI1-255. callflow §4의 Metal 시작 분기 및 Claude 10-21 수정 문단. |
| [lisflood-fp-metal-fv1.md:73](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-metal-fv1.md#L73) | 보완 | 초기화 실패 반환 인용에 wrapper와 main 호출부 인용을 추가했다. | simulate:1359–1364는 실패 시 return한다. metal_integrate.cpp:12–14는 simulate 호출 뒤 끝난다. main:782–788의 CPU 호출은 Metal 선택 조건의 else이다. |

### 기계 확인 후보 판정

| 번호 | 노트 줄 | 원문 파일:줄과 확인한 내용 | 판정 |
|---|---:|---|---|
| 40 | 38 (원래 36) | CMakeLists.txt:232 — if (APPLE) | 원문과 일치한다. 노트의 해당 인용을 유지했다. |

## 완료 집계

검증 시작 시 대상 줄은 127 + 83 = 210줄이다.
추가한 frontmatter 2줄도 작성 규칙과 대조했다.
수정 후 노트는 127 + 85 = 212줄이다.
정정 표식은 11 + 5 = 16줄이다.
보완 표식은 2 + 1 = 3줄이다.
차이 표는 43 + 29 = 72행이다.
기계 확인 후보는 39 + 1 = 40건이다.
후보 40건을 사용자가 제시한 순서대로 판정했다.
수정 후 내용은 원래 내용에 위 정정·보완 목록만 적용한 결과와 일치한다.
두 노트의 frontmatter는 YAML로 해석된다.
상대 링크의 대상은 모두 존재한다.
수정 표식의 위치는 본문 줄 끝 또는 결론 문장 칸 끝이다.
frontmatter의 수정 표식은 YAML 주석이다.
검증 방식은 원문 문서·코드·최종 결론의 정적 대조이다.
대상 노트 두 파일의 전수 대조를 완료했다.
미해결 항목은 0건이다.
