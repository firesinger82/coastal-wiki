# LISFLOOD-FP 노트 추가 줄 표본 검증 (30줄)

검증자는 각 줄을 노트에서 열고 인용된 코드·문서 쪽 이미지·최종 결론 파일을 직접 확인했다.
확인하지 않은 것: 모델 실행, 수치 재현. PDF 쪽 15–22의 `ascii_out`·`damfile` 부재는 쪽 이미지가 아니라 pdftotext 텍스트 검색으로 확인했다.

| 노트:줄 | 판정 | 확인한 원문 | 이유 |
|---|---|---|---|
| docx-manual-differences:45 (LV1-039) | 맞음 | docx p.20 표 5, pdf p.16 표 5, `pars.cpp:202`, `lisflood.cpp:165`, `v8.0:lisflood.cpp:158`, `VersionHistory.h:34` | 두 문서 모두 `Default: 10`이다. Word 쪽만 `Acceleration, Adaptive, FV1 and DG2 solvers`를 적는다. 분류 A가 최종 결론과 같다. |
| user-manual:159 (startelev) | 맞음 | pdf p.18 표 9, pdf p.32 3.2.24, `pars.cpp:145–163`, `input.cpp:1168–1187` | `startelev`는 `read_empty_param`이다. SGC는 `H-SGCz`, 일반 경로는 `H-DEM`이며 둘 다 `getmax(…,0)`이다. 문서 기본값은 off이다. |
| user-manual:489 (LG1-123) | 맞음 | docx p.22 표 8, `swe/fv1.cpp:43–45`, `swe/dg2.cpp:62–74`, `cuda_fv1_simulate.cu:142–158`, `cuda_dg2_simulate.cu:140–157`, `metal_fv1_simulate.mm:1046·1050·1072` | docx는 균일 강우를 FV1·DG2에서 제외한다. 코드 순서가 결론 문장과 같다. CPU 균일 강우 경로는 swe에 없다. |
| user-manual:526 (LV1-229) | 맞음 | docx p.46, pdf p.41–42, `weir_flow.cpp:153–169`, `weir_flow.cpp:115` | 인용한 `if`·`else if` 문이 153·158·162행에 있다. `Tz = Arrptr->Weir_m[weir_id]`이므로 Tz는 고정 1.5가 아니다. |
| build-and-83-release:31 | 맞음 | `README.md:29–30` | 29행 `cmake -S . -B build`, 30행 `cmake --build build`이다. |
| build-and-83-release:108 (LG1-130) | 맞음 | `v8.2:cuda_max_field.cu:94–100`, 현재 `cuda_max_field.cu:95–100`, v8.0/v8.1/v8.2 `*_simulate.cu` MaxField 호출, `lisflood-8.2-to-8.3.patch:94–133`, 패키지 `README.md:32` | 인용 줄 번호와 문장이 정확하다. v8.0은 `allocate_pinned`(초기화 없음), v8.1 FV2·v8.2 FV1/DG2는 `pars.output_precision`이 `acceleration` 자리로 들어가 작은 배열을 고른다. |
| build-and-83-release:122 (LT1-123) | 맞음 | pdf p.13 표 3, `README.md:33`, `v8.0:README.md:33` | 표에 `LISFLOOD-LIN.EXE`가 있다. README 33행이 `build` 디렉터리 출력을 말한다. |
| channel-sgc:94 | 부분 | `sgc.cpp:942·961–969·726`, `lisflood.h:60`, `sgc.cpp:862–882·979–998·1390–1406` | 주 주장은 맞다. 다만 `sgc.cpp:1390–1406`은 `w0 < cell_width`와 `cell_width - w0`를 함께 써서 폭 불일치 증거가 아니다. 이 구간은 `SGC_BCs` 경계 함수이다(`1291–1297`에서 cell_width를 방향별로 정한다). |
| channel-sgc:232 (LB1-136) | 맞음 | bridge p.29, pdf p.40 식 (5), `weir_flow.cpp:79–88`, `sgm_fast.cpp:537–546`, `input.cpp:161–163`, `v8.0:weir_flow.cpp:79–88`, `VersionHistory.h:493` | 인쇄식 `Q = CL(2gH)^1.5`이다. 현재 식은 `Cd*w*pow(hu,1.5)`이다. `(2g)^1.5`배 설명이 맞다. 분류 A가 최종 결론과 같다. |
| channel-sgc:307 (LI2-316) | 맞음 | pdf p.32, `input.cpp:1169–1187` | 인용 코드가 1178–1184행과 문자까지 같다. pdf p.32는 SGC를 말하지 않아 C가 맞다. |
| classic-acc-flow:385 (LI1-097) | 맞음 | pdf p.19, pdf p.1, `lisflood.cpp:240`, `iterateq.cpp:150`, `v8.0:230`, `v8.1:236`, `v8.2:237`, `VersionHistory.h:244–247` | pdf p.19는 drycheckon·drycheckoff 두 행에 `Default: drycheck is off`를 적는다. 코드는 ON이다. 표지 6.1.1이다. |
| cuda-gpu:128 | 맞음 | `cuda/fv1/cuda_fv1_solver.cu:424–428` | 424·428행이 `Uold[(j+1)…]`·`Uold[j…]`를 읽는다. |
| cuda-gpu:158 | 맞음 | `cuda_solver.templates.cu:43–70`, `cuda_geometry.cu:46–52` | `DynamicTimestepACC` 생성자가 `elements_H` 크기로 `allocate_device_H`를 호출한다. |
| cuda-gpu:196 (LG1-022) | 맞음 | `cuda_boundary.cu:333–360·395–410`, `cuda_fv1_solver.cu:342`, verify-LG1 | `inside_x`가 `{ U_outside.H, U_outside.HU, U_const.HV }`를 반환하고 FV1 호출에서 U_const는 내부 상태이다. 외부 접선은 `outside_x`에서 0이다. |
| cuda-gpu:207 (LG2-060) | 맞음 | `cuda_boundary.cu:237–240·252–261` | `update_H`가 네 면 유량을 지역 변수로 복사한다. |
| cuda-gpu:323 (RF-016) | 맞음 | `cuda_acc_solver.cu:723–729`, `acc_nugrid/compute_q.cu:235–237` | 두 곳 모두 관성식(`q0`·`g*dt*hflow*Sf` 분모 마찰)이다. |
| cuda-gpu:362 (RF-013) | 맞음 | patch `:79·87`, `cuda_boundary.cu:283–293·315–325`, 패키지 `README.md:33`, `cuda_boundary.cu:80–91` | 패치 추가 줄이 일치한다. 현행 291–292행의 Q 식이 일치한다. `accumulate_point_source_stats`는 Q=0에서 0을 더한다. |
| cuda-gpu:411 (LG1-025) | 맞음 | `swe/fv1.cpp:228`, `cuda_boundary.cu:128·131`, `cuda/io.cpp:18`, `metal_fv1_simulate.mm:938·944` | 모든 인용 행이 일치한다. CPU는 `Q*dx*dt/dA`이고 `dy=dx`일 때만 CUDA·Metal과 같다. |
| io-boundary-differences:65 (LB1-104) | 맞음 | bridge p.21·27·33, `input.cpp:1869·1898·1993–1995` | p.21에 `comments can only be used in the parameter file (.par)` 문장이 있다. p.27·33은 `.bdy`·`.evap` 1행을 `Comment line`이라 적는다. 분류 B가 같다. |
| io-boundary-differences:72 (LB1-176) | 맞음 | bridge p.35–36, `pars.cpp:45–48·91–103·563·1027–1036`, `v8.0:pars.cpp:552–557` | p.36이 `-checkpoint`는 간격을 줄 수 없다고 적는다. 현재 `read_numeric_param`은 숫자가 아니면 기본값 1.0을 대입한다. 마지막 인수 par 파일 이름이 `-checkpoint` 뒤에 오므로 par 간격이 1로 덮이는 설명도 맞다. |
| io-boundary-differences:102 (LB1-292) | 맞음 | bridge p.21–24 표 5, p.35 표 7, `pars.cpp:519–521` | 표 5와 표 7에 `routing`이 없다. 코드 두 줄이 일치한다. |
| io-boundary-differences:110 (LB1-340) | 맞음 | bridge p.21–24, p.35, `pars.cpp:915·920` | 표에 `dammask`가 없다. 코드 두 줄이 일치한다. |
| lisflood2-driver:249 (LI1-215) | 맞음 | pdf p.15–22(텍스트 검색), `pars.cpp:397·1044–1049`, `lisflood.cpp:99`, `file_tool.cpp:787–791` | `ascii_out`이 표에 없다. 인용 줄 번호와 문장이 모두 일치한다. |
| lisflood2-driver:253 (LI1-247) | 맞음 | pdf p.1, `VersionHistory.h:38`, `pars.cpp:907·1058–1077`, `lisflood.cpp:262·461–464`, `input.cpp:2428`, `v8.0:pars.cpp:826` | 6.2 저수지 추가이다. 표지 6.1.1보다 뒤다. SGC 검사와 마스크 누락 검사가 `verbose == ON` 조건이다. |
| mwdg2-adaptive-mra:66 (LG2-087) | 맞음 | `StagePoints.h:129–136`, `write_stage_point_data.cu:53–74·105–106`, `write_soln_vtk.cu:92–101` | 입력은 `xmin`을 빼고, stage 헤더는 `i*dx_finest + dx_finest/2`만 쓰며, VTK는 `xmin +`를 더한다. |
| swe-fv1-dg2:310 | 부분 | `swe/dg2new.h:6–32` | 6–32행에 `Increment`·`LocalFaceValue`·`FlowVector` 세 구조체가 있다. 문장은 둘만 적고 `LocalFaceValue`(19–25행)를 빠뜨렸다. |
| swe-fv1-dg2:376 (LN1-239) | 맞음 | `bf804e23` 노트 26–27, `v8.2:lisflood.cpp:775–783`, 현재 `lisflood.cpp:778–793`, patch `:282–295` | 8.3 패치가 `#ifdef METAL_ENABLED` 안에 `if (Statesptr->cuda == ON && metal_is_available())`를 넣는다. |
| swe-fv1-dg2:396 (LG1-083) | 맞음 | `dg2new.cpp:42·45·300·304–306`, `dg2.cpp:217–220`, `cuda_dg2_solver.cu:515–516`, `lisflood.cpp:794–796` | 인용 줄과 `// FIXME: BC treatment`가 일치한다. 호출부가 주석 처리돼 있다. |
| swe-fv1-dg2:412 (LI2-332) | 맞음 | `swe/fv1.cpp:66·74–76·99`, `dg2.cpp:78·119`, `swe/output.cpp:148–165`, `v8.0:swe/fv1.cpp:66·76–79·99`, `VersionHistory.h:34`, `iterateq.cpp` 출력 블록 | 두 반복문에 overpass·profile·hazard·checkpoint·gauge 호출이 없다. 줄 번호가 일치한다. |
| web-refs/official-resources:47 (LV1-287) | 맞음 | `v8.2:cuda_fv1_solver.cu:328–383`, 현재 `cuda_fv1_solver.cu:350–383`, 패키지 `README.md:34` | v8.2 범위에는 pass 끝 barrier가 없고 현재판에는 끝 `__syncthreads()`가 있다. |

## 집계

- 맞음 28, 부분 2, 틀림 0 (총 30).
- 부분: `channel-sgc:94`, `swe-fv1-dg2:310`.

## 부분 줄의 수정안

- `channel-sgc:94`: 근거 구간 `1390–1406`을 `…,862–882,979–998)`에서 뺀다. 1390–1406은 `if (hflow>Solverptr->DepthThresh && w0 < cell_width)`와 `Qfp = (*qoldptr) * (cell_width - w0);`를 쓰며 폭 불일치가 없다.
- `swe-fv1-dg2:310`: `자료형은 FlowVector·Increment이다`를 `자료형은 Increment·LocalFaceValue·FlowVector이다`로 바꾼다.
