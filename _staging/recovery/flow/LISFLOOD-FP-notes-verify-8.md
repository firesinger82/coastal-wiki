# LISFLOOD-FP 노트 추가·수정 줄 전수 대조 (2026-10-21)

## 대상과 집계 방법

대상은 `lisflood-fp-swe-fv1-dg2.md`와 `lisflood-fp-mwdg2-adaptive-mra.md`이다.
기존 노트의 대상 줄은 작업 시작 시 `git diff -U0 HEAD -- <노트>`의 모든 `+` 줄이다.
새 파일의 대상 줄은 전체 줄이다.
빈 줄과 frontmatter 줄도 대조 줄 수에 포함한다.
정정 수와 보완 수는 이번 작업에서 표시를 붙인 대상 줄 수로 센다.
노트별 완료 기록은 각 노트의 대조를 마친 뒤 아래에 추가한다.

## 진행 기록

- 검증 기록을 먼저 만들었다.
- 시작 시 읽기 전용 diff에서 SWE 노트의 대상 줄은 137줄이다.
- SWE 노트의 시작 시 대상 줄 번호는 `7–8, 12, 27–30, 34, 43–45, 142–144, 164–168, 175–180, 206–209, 253–259, 275, 278, 284–290, 309–311, 323–333, 337–344, 347–349, 353–419`이다.
- 시작 시 읽기 전용 diff에서 MWDG2 노트의 대상 줄은 128줄이다.
- MWDG2 노트의 시작 시 대상 줄 번호는 `7–8, 12–14, 20–21, 25, 46, 49–50, 56–72, 76–77, 80–177`이다.

## SWE 노트: 완료

대상은 [lisflood-fp-swe-fv1-dg2.md](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-swe-fv1-dg2.md)이다.
시작 시 diff의 대상 137줄을 모두 대조했다.
정정은 2줄이다.
보완은 3줄이다.
정정 수와 보완 수는 노트에 붙인 이번 검증 표시를 기준으로 집계했다.
줄 수를 바꾸지 않았으므로 아래 줄 번호는 시작 시 번호와 같다.

### 대조 범위와 근거

| 대상 줄 | 대조 내용과 원문 |
|---|---|
| 7–8, 12 | frontmatter의 과거 판독 범위와 이번 반영 날짜를 반영 기록 5와 대조했다. v8.2의 `lisflood.cpp:775–792`를 열었다. related 파일의 존재를 확인했다. |
| 27–30, 34, 43–45 | 현재 `lisflood.cpp:778–796`의 `METAL_ENABLED` 조건과 호출을 대조했다. `pars.cpp:708–727`과 DG2 필드 사용처를 대조했다. LN1-238·239, LB1-403, LI1-233·234·368의 수정안을 대조했다. |
| 142–144, 164–168, 175–180 | `swe/fv1.cpp:34–50,122–151,441–482`, `swe/fv1/modifiedvars.cpp:314–331`, CPU DG2·CUDA·Metal의 대응 경로를 대조했다. LG1-012와 LV1-094–096·284의 최종 결론을 대조했다. 네 판의 소스에서 입력 문자열 `"speedthresh"`가 없음을 확인했다. |
| 206–209, 253–259 | CPU DG2 마찰·CFL·limiter를 CUDA·dg2new와 대조했다. LG1-045–053의 수정안과 최종 강도를 대조했다. `thin_depth`의 입력 필드 식과 시간 간격 제한 식은 주석이다. |
| 275, 278, 284–290 | `swe/fv1.cpp:523–578`, `swe/dg2.cpp:140–157,658`, `cuda/cuda_boundary.cu:105–123,333–409`, `lisflood.h:75–96`을 대조했다. RF-022의 강함과 LG1-023의 강함을 유지했다. |
| 309–311, 323–333 | dg2new의 자료형·면 값·가우스점·y 플럭스·fixed 분기를 원문과 대조했다. CMake와 makefile의 포함 여부를 각각 대조했다. LG1-081·082의 비활성 경로 표시를 확인했다. |
| 337–344, 347–349 | CPU 두 반복문의 출력과 `swe/output.cpp`, `swe/stats.cpp`, DG2 기울기 writer를 대조했다. Metal의 `metal/fv1/metal_fv1_simulate.mm:1425–1477`을 대조했다. HLL 호출과 공통 HLL 식을 대조했다. LI2-318·331·332와 callflow §6의 수정안을 대조했다. |
| 353–367 | 문서 판 안내, 코드 판 안내, 상대 링크, 표 머리말과 빈 줄을 확인했다. DOCX의 p.1·5 쪽 이미지에서 판 표시 오류를 확인했다. |
| 368–419 | 차이 표 52행의 행 ID·분류·결론 문장을 최종 배정표와 지정 conclusion-verify 파일에 대조했다. 최우선 claude-final의 조정 대상은 이 표에 없다. A 행은 v8.0·v8.1·v8.2 원문과 8.3 패치에 대조했다. E 행의 강도와 비활성 경로 표시를 대조했다. 표의 코드 인용은 각 판의 원문을 열어 대조했다. `bf804e23:` 인용은 지정 커밋의 노트를 읽어 대조했다. |

문서의 수치·표는 쪽 이미지로 판정했다.
확인한 PDF 쪽은 p.1·11–12·15–22·31–32·36–38이다.
확인한 DOCX 변환본 쪽은 p.1·5·14–15·22–24·30·37이다.
확인한 bridge DOCX 변환본 쪽은 p.1·21–24·35이다.
쪽별 판독 기록과 수정안은 해당 문장의 판·위치 연결에 함께 사용했다.
노트에 mermaid 블록은 없다.
노트의 상대 링크는 실제 경로로 해석된다.
절대 홈 경로·`~/`·위키 링크 표기와 지정된 한계 문장은 없다.

### 정정·보완 목록

아래 코드 경로의 기준은 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/`이다.
`v8.2:`의 기준은 사용자 지정 이전 배포본이다.

| 종류 | 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| 보완 | [SWE:178](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-swe-fv1-dg2.md#L178) | CUDA 저속 운동량 제거의 근거가 LV1-096·284 링크뿐이었다. | CUDA FV1·DG2의 직접 코드 인용을 추가했다. | `cuda/fv1/cuda_fv1_solver.cu:232–237`, `cuda/dg2/cuda_dg2_solver.cu:616–622`는 저속 조건에서 `HU = C(0.0);`와 `HV = C(0.0);`을 실행한다. |
| 정정 | [SWE:356](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-swe-fv1-dg2.md#L356) | DOCX의 판 이력 맨 위를 5.9로 적었다. 8.3 패치에 DOI 13121119를 붙였다. | DOCX 표지의 수정 표시 8.0.0·2020-07-20과 판 이력 첫 행 8.0을 적었다. 문서 쪽과 코드 판 인용을 명시했다. 해당 원문이 뒷받침하지 않는 8.3 DOI 표기를 제거했다. | `lf-manual-docx-001.png`는 6.1.1·2013-11-25를 취소하고 8.0.0·2020-07-20을 추가한다. `lf-manual-docx-005.png` 첫 행은 `8.0 / Jul 20 2020`이다. `../LISFLOOD-FP-8.3-package/README.md:19–24`가 직접 적은 DOI는 8.2의 13121102이다. 최종 LB1-408의 인용 정정도 이 구분을 명시한다. |
| 정정 | [SWE:375](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-swe-fv1-dg2.md#L375), LN1-238 | 마지막 인용이 `lisflood.cpp:784–786`이었다. | 마지막 인용을 `v8.2:lisflood.cpp:784–786`으로 바꾸었다. 결론은 유지했다. | v8.2의 784–786행은 `//dg2new::DG2Solver`와 `//solver.solve();`이다. 현재 같은 호출 주석은 794–796행이다. 현재 784–786행은 Metal 호출 인수·`else`·`#endif`이다. |
| 보완 | [SWE:408](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-swe-fv1-dg2.md#L408), LV1-274 | DOCX 쪽 인용이 p.15·23이었다. | 제한기 설명이 있는 p.24를 추가했다. | `lf-manual-docx-024.png`의 표 10은 `limitslopes`, `krivodonovathresh`, `zero applies the slope limiter globally`를 적는다. |
| 보완 | [SWE:409](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-swe-fv1-dg2.md#L409), LV1-284 | DOCX p.23–24·37과 PDF p.18–19·31–32를 인용했다. | DOCX p.22와 PDF p.17을 추가했다. | `lf-manual-docx-022.png` 표 8은 `rainfall`, `dynamicrainfile`, `drain_nodata`를 적는다. `lf-manual-pdf-017.png` 표 8은 구판 `rainfall`의 적용 범위를 적는다. |

### 기계 확인 후보 판정

- SWE:406의 `v8.0:swe/dg2/slope_limiter.cpp:287` 인용은 원문의 `if (stencil_minH <= C(0.30)*Solverptr->maxH) return local_slope;`와 일치한다. 검사기 오판이다. 노트는 유지했다.

## MWDG2 노트: 완료

대상은 [lisflood-fp-mwdg2-adaptive-mra.md](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md)이다.
시작 시 diff의 대상 128줄을 모두 대조했다.
정정은 7줄이다.
보완은 3줄이다.
줄 수를 바꾸지 않았으므로 아래 줄 번호는 시작 시 번호와 같다.

### 대조 범위와 근거

| 대상 줄 | 대조 내용과 원문 |
|---|---|
| 7–8, 12–14 | frontmatter를 반영 기록 4와 대조했다. v8.2 driver의 마지막 줄과 개행 수를 확인했다. `mra/Filters.h`의 실제 경로를 확인했다. related 파일의 존재를 확인했다. |
| 20–21, 25, 46 | 현재·v8.2의 main 진입점과 utility 이름 변경을 대조했다. driver의 479행 재격자화 조건을 대조했다. 모식도 주석과 `init_nodal_values.cu:48–75`의 실제 좌표를 구분했다. `preflag_details.cu:24–88`과 `refine_high_wall.cu:12–53`의 방향·호출 조건을 대조했다. |
| 49–50, 56–57 | qy 분모의 qx0 입력, `AbsMax`, 하한 1, detail 최대값 결합을 대조했다. N의 signed max를 대조했다. `SolverParams`·`SimulationParams` 생성자와 실수 reader의 생략값을 대조했다. `pars.cpp`·`input.cpp`의 역할과 `LoadDEM` 호출 순서를 대조했다. |
| 58–72 | 제목과 빈 줄을 포함했다. LG2-039·045·065·068·070·087의 최종 강도를 대조했다. grading·고정 level 4 접근·Q 경계 덮어쓰기·시계열 row 접근·최초 H 원천 인덱스·stage 원점의 원문 조건을 각각 대조했다. 출력 함수와 stage·DG raster의 계수 읽기를 대조했다. |
| 76–77, 80–84 | 공식 자료 노트와 관련 노트의 실제 내용을 확인했다. 배포 README의 기반 DOI와 릴리스 표시를 구분했다. N driver의 초기 격자 구성과 시간 루프를 대조했다. N·M의 활성 필터와 scale 식 및 아홉 MW detail 식을 대조했다. Haar 활성 분기를 구분했다. |
| 85–97 | 문서 판 안내·코드 판 안내·기호 정의·근거 링크·표 머리말과 빈 줄을 확인했다. DOCX p.1·5 쪽 이미지와 `VersionHistory.h:16–23`을 대조했다. |
| 98–121 | bridge 문서의 키워드·명령행 표와 별도 parser를 대조했다. `_USE_TRACER`의 조건과 기본 빌드의 미정의를 확인했다. 전역 sync의 8.2 선언·8.3 변경·시스템 선언을 대조했다. tracer에 남은 호출의 비활성 조건을 유지했다. 과거 노트 인용을 지정 커밋의 7·20·54–55·60행과 대조했다. |
| 122–139 | scale·detail 정규화, signed max와 absmax, qy 입력, extra significance, decode, grading, leaf 순회, compaction, 작은 L, 바닥 원천, 마찰, 건조 운동량, 제한기, RK2, 허용값·CFL·중력 상수를 원문과 대조했다. 식의 부호와 조건을 각 갱신식과 함께 확인했다. |
| 140–148 | Q 경계·시계열·초기 원천·표본 시각·강우 호출 부재·출력·좌표·내장 사례·Monai/Oregon 분기를 원문과 대조했다. 실제 지형·finest·HFIX/HVAR 조건을 유지했다. |
| 149–155 | 매뉴얼의 키워드 표·명령행 표·출력 설명을 쪽 이미지와 대조했다. 별도 입력 구조체·출력 디렉터리·qy 분모·자체 출력 형식을 대조했다. A 행의 v8.2 원문과 현재 원문을 각각 확인했다. |
| 156–177 | 공통 플래그와 별도 생성자를 구분했다. 0–23 사례 번호, max_ref_lvl, nodata 식, grading, 조건부 옵션 읽기, 출력 플래그, 접두부 비교, 생략값, 저장 간격, DEM 헤더, 명령행과 옛 reader의 호출 여부를 대조했다. |

차이 표 80행의 행 ID·분류·결론 문장을 최종 배정표와 지정 conclusion-verify 파일에 대조했다.
최우선 claude-final의 조정 대상은 이 표에 없다.
결론 분류와 E 강도는 최종 근거와 일치한다.
LN1-126의 8.2 결함·8.3 수정 표시를 유지했다.
LN1-135의 기본 빌드 비활성 조건을 유지했다.
현재와 v8.2의 `cuda/adaptive/` 파일을 비교했다.
내용이 다른 파일은 `utilities/cuda_utils.cu`와 `utilities/cuda_utils.cuh`뿐이다.
`c_prop`의 압축률 출력 설명은 유지했다.
`write_c_prop_data.cu:19–30`이 호출하는 `write_cumulative_data.cpp:32–49`는 격자 감소율을 기록한다.

문서의 수치·표는 쪽 이미지로 판정했다.
확인한 PDF 쪽은 p.1·15–22·33–34·36–38이다.
확인한 DOCX 변환본 쪽은 p.1·5·19–26·38–39이다.
확인한 bridge DOCX 변환본 쪽은 p.1·21–24·35이다.
앞선 SWE 대조에서 확인한 같은 쪽 이미지도 사용했다.
노트에 mermaid 블록은 없다.

### 정정·보완 목록

아래 코드 경로의 기준은 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/`이다.
`v8.2:`와 `bf804e23:`는 사용자 지정 원문이다.

| 종류 | 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| 정정 | [MWDG2:7](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md#L7) | driver를 `(962)`로 표시했다. `Filters.h`를 `.cu` 파일 묶음 안에 넣었다. | 마지막 개행 없는 줄을 포함해 963줄임을 명시했다. `mra/Filters.h`를 별도 경로로 적었다. | v8.2의 `cuda/adaptive/cuda_adaptive_simulate.cu:963`은 개행 없는 마지막 주석이다. 개행 문자는 962개이다. 필터 파일은 `cuda/adaptive/mra/Filters.h`이다. |
| 보완 | [MWDG2:70](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md#L70) | 자체 parser의 인용이 옛 `read_plot_params.cpp`였다. | 현재 run이 사용하는 생성자와 호출 위치를 추가했다. | `cuda/adaptive/cuda_adaptive_simulate.cu:162–167`은 생성자를 호출한다. `cuda/adaptive/classes/PlottingParams.h:25–52`는 현재 출력 설정을 읽는다. |
| 정정 | [MWDG2:77](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md#L77) | 8.3 패치에 DOI 13121119를 붙였다. 전체 판 관계를 `VersionHistory.h:23`만으로 인용했다. | 근거가 없는 8.3 DOI 표기를 제거했다. 기반 판과 패치 관계는 배포 README로 인용했다. 릴리스 이름은 VersionHistory로 인용했다. | `../LISFLOOD-FP-8.3-package/README.md:19–24`는 8.2 DOI 13121102와 8.3 변경의 관계를 적는다. `VersionHistory.h:23`은 `LF_Release "8.3"`이다. 최종 LB1-408의 인용 정정도 이 구분을 명시한다. |
| 정정 | [MWDG2:88](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md#L88) | DOCX 판 이력 맨 위를 5.9로 적었다. 숫자 판 8.1.0의 근거를 `VersionHistory.h:21–23`으로 적었다. 8.3 DOI 13121119를 붙였다. | DOCX 표지 수정 표시 8.0.0·2020-07-20과 판 이력 첫 행 8.0을 적었다. 숫자 판의 인용을 16–18행으로 바꾸었다. 근거 없는 8.3 DOI를 제거했다. | `lf-manual-docx-001.png`, `lf-manual-docx-005.png`, `VersionHistory.h:16–18,23`, `../LISFLOOD-FP-8.3-package/README.md:19–24`. |
| 정정 | [MWDG2:112](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md#L112), LB1-406 | 과거 노트의 직접 인용 안에 `cuda/adaptive/classes/`를 추가했다. | 직접 인용을 원래의 `SolverParams.h:33-72`와 `SimulationParams.h:58-59`로 복원했다. 결론은 유지했다. | `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:55`에는 확장한 경로가 없다. 현재 코드 인용은 다른 칸에 그대로 남겼다. |
| 정정 | [MWDG2:118](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md#L118), LN1-126 | 시스템 헤더를 `/usr/include/unistd.h:999–1005`라는 절대 경로로 적었다. | 시스템 헤더 `unistd.h:999–1005`로 적었다. 원문 경로가 기록된 최종 근거 파일을 상대 링크로 연결했다. 결론과 강도는 유지했다. | 시스템 헤더 999행의 feature 조건과 1005행의 `extern void sync (void) __THROW;`를 직접 대조했다. 경로 기록은 `LISFLOOD-FP-conclusion-verify-LN1.md`의 LN1-126에 있다. |
| 정정 | [MWDG2:149](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md#L149), LV1-254 | DOCX p.19–26과 PDF p.15–21의 키워드 표를 모두 표 4–6으로 적었다. | 두 문서의 표 번호를 표 5–11로 고쳤다. 결론은 유지했다. | DOCX p.19와 PDF p.15의 본문은 키워드 표를 Table 5부터 Table 11까지로 열거한다. DOCX p.25와 PDF p.20의 출력 표 머리말은 Table 11이다. 최종 LV1-254에서 옮긴 표 번호 자체가 쪽 이미지와 다르다. |
| 보완 | [MWDG2:155](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md#L155), LI2-340 | 자체 parser 근거 목록에 현재 생성자 호출이 없었다. | 현재 run의 생성자 호출과 `PlottingParams`의 읽기 위치를 추가했다. A 분류와 결론은 유지했다. | `cuda/adaptive/cuda_adaptive_simulate.cu:162–167`, `cuda/adaptive/classes/PlottingParams.h:25–52`. 두 파일은 v8.2와 현재 판에서 같다. |
| 보완 | [MWDG2:176](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md#L176), LI1-292 | PDF의 매개변수 설명 p.15–22만 인용했다. | 명령행 표 14의 p.33–34를 추가했다. 결론은 유지했다. | `lf-manual-pdf-033.png`의 표 14 제목과 `lf-manual-pdf-034.png`의 실제 명령행 목록을 확인했다. `-solver`는 이 목록에 없다. |
| 정정 | [MWDG2:177](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md#L177), LI1-364 | 과거 노트의 직접 인용 안에 `cuda/adaptive/classes/`를 추가했다. | 직접 인용을 원래의 `SolverParams.h:33-72`와 `SimulationParams.h:58-59`로 복원했다. 결론은 유지했다. | `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-mwdg2-adaptive-mra.md:55`의 실제 문장을 대조했다. |

### 기계 확인 후보 판정

MWDG2 노트에 대해 사용자가 지정한 기계 확인 후보는 없다.

## 최종 집계와 검증

| 노트 | 대조한 대상 줄 수 | 정정한 줄 수 | 보완한 줄 수 |
|---|---:|---:|---:|
| SWE FV1·DG2 | 137 | 2 | 3 |
| MWDG2 adaptive MRA | 128 | 7 | 3 |
| 합계 | 265 | 9 | 6 |

집계는 시작 시 읽기 전용 diff의 대상 줄 목록과 최종 수정 표시를 기준으로 했다.
최종 diff의 대상 줄 목록은 시작 시 목록과 같다.
이번 작업의 변경은 위 정정·보완 목록에 있는 15줄뿐이다.
이 15줄은 모두 시작 시 대상 줄에 속한다.
차이 표 132행의 분류는 최종 배정표와 일치한다.
E 행의 강도는 최종 배정표와 일치한다.
모든 차이 표 행은 여섯 칸을 유지한다.
SWE의 상대 링크 31개와 MWDG2의 상대 링크 17개는 실제 파일 또는 디렉터리로 해석된다.
두 노트에 절대 파일시스템 경로·`~/`·위키 링크 표기는 없다.
두 노트에 지정된 한계 문장은 없다.
두 노트에 mermaid 블록은 없다.
기계 확인 후보 1건의 판정을 기록했다.
미해결 항목은 없다.
