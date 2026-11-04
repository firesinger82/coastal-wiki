# Celeris 문서 판독 기록 전수 검증 (11-04)

대상은 사용자 지정 문서 판독 기록 94개다.
원문은 각 기록 frontmatter의 `file:` 경로다.
대조한 행 수는 판독 표의 구간 행 수와 그 구간에 포함된 원문 행 수를 구분한다.
정정·보완·이상 없음은 구간 행 단위로 센다.
같은 구간에 정정과 보완이 함께 있으면 두 항목에 각각 센다.
표의 기록 경로는 `_staging/recovery/read/Celeris/Celeris-WebGPU/` 기준이다.
완료 목록의 94개 기록에서 판독 표 218행을 대조했다.
대조한 원문은 해당 구간에 포함된 3,156행이다.
각 구간은 `nl -ba <원문> | sed -n 'A,Bp'`로 열어 의미를 대조했다.
이 대상의 원문은 모두 설명 문서이며 설명 대상 JS/WGSL 구현 파일과 구별했다.
원문 파일 94개의 SHA-256은 각 기록의 frontmatter와 일치했다.
각 기록의 구간은 원문 첫 행부터 마지막 행까지 연속이었다.
정정과 보완이 함께 있는 구간은 10행이다.
모델 실행은 하지 않았다.

## 기록별 대조

| 기록 | 대조한 구간 행 수 | 대조한 원문 행 수 | 상태 |
|---|---:|---:|---|
| ARCHITECTURE.md.md | 5 | 109 | 완료 |
| README.md.md | 5 | 90 | 완료 |
| docs/README.md.md | 3 | 31 | 완료 |
| docs/architecture/CONFIGURATION.md.md | 4 | 105 | 완료 |
| docs/architecture/DATA_AND_TEXTURES.md.md | 5 | 131 | 완료 |
| docs/architecture/REFERENCE_PAPERS.md.md | 3 | 50 | 완료 |
| docs/architecture/SIMULATION_PIPELINE.md.md | 4 | 66 | 완료 |
| docs/architecture/WEBGPU_BINDING_PATTERN.md.md | 3 | 71 | 완료 |
| docs/source/externals/README.md.md | 1 | 5 | 완료 |
| docs/source/externals/geotiff_js.md.md | 2 | 15 | 완료 |
| docs/source/externals/gif_worker_js.md.md | 2 | 15 | 완료 |
| docs/source/js/Config_Pipelines_js.md.md | 2 | 31 | 완료 |
| docs/source/js/Copy_Data_to_Textures_js.md.md | 2 | 47 | 완료 |
| docs/source/js/Create_Textures_js.md.md | 2 | 32 | 완료 |
| docs/source/js/File_Loader_js.md.md | 3 | 43 | 완료 |
| docs/source/js/File_Writer_js.md.md | 2 | 30 | 완료 |
| docs/source/js/Handler_AddDisturbance_js.md.md | 2 | 26 | 완료 |
| docs/source/js/Handler_BoundaryPass_js.md.md | 2 | 32 | 완료 |
| docs/source/js/Handler_CalcMeans_js.md.md | 2 | 32 | 완료 |
| docs/source/js/Handler_CalcWaveHeight_js.md.md | 2 | 24 | 완료 |
| docs/source/js/Handler_Copytxf32_txf16_js.md.md | 2 | 27 | 완료 |
| docs/source/js/Handler_ExtractNestedBoundaryTimeSeries_js.md.md | 2 | 21 | 완료 |
| docs/source/js/Handler_ExtractTimeSeries_js.md.md | 2 | 27 | 완료 |
| docs/source/js/Handler_Model_js.md.md | 2 | 21 | 완료 |
| docs/source/js/Handler_MouseClickChange_js.md.md | 2 | 26 | 완료 |
| docs/source/js/Handler_Pass0_js.md.md | 2 | 22 | 완료 |
| docs/source/js/Handler_Pass1_js.md.md | 2 | 25 | 완료 |
| docs/source/js/Handler_Pass2_js.md.md | 2 | 31 | 완료 |
| docs/source/js/Handler_Pass3_js.md.md | 3 | 49 | 완료 |
| docs/source/js/Handler_PassBreaking_js.md.md | 2 | 27 | 완료 |
| docs/source/js/Handler_Render_js.md.md | 3 | 37 | 완료 |
| docs/source/js/Handler_SedTrans_Pass1_js.md.md | 2 | 26 | 완료 |
| docs/source/js/Handler_SedTrans_Pass3_js.md.md | 2 | 36 | 완료 |
| docs/source/js/Handler_SedTrans_UpdateBottom_js.md.md | 2 | 27 | 완료 |
| docs/source/js/Handler_Skybox_js.md.md | 2 | 21 | 완료 |
| docs/source/js/Handler_Tridiag_js.md.md | 2 | 25 | 완료 |
| docs/source/js/Handler_UpdateTrid_js.md.md | 2 | 23 | 완료 |
| docs/source/js/Handler_Updateneardry_js.md.md | 2 | 21 | 완료 |
| docs/source/js/Model_Loaders_js.md.md | 2 | 27 | 완료 |
| docs/source/js/README.md.md | 2 | 38 | 완료 |
| docs/source/js/Run_Compute_Shader_js.md.md | 2 | 27 | 완료 |
| docs/source/js/Run_Tridiag_Solver_js.md.md | 2 | 30 | 완료 |
| docs/source/js/Time_Series_js.md.md | 2 | 22 | 완료 |
| docs/source/js/Wave_Generator_js.md.md | 3 | 30 | 완료 |
| docs/source/js/agent_controls_js.md.md | 6 | 132 | 완료 |
| docs/source/js/constants_load_calc_js.md.md | 3 | 44 | 완료 |
| docs/source/js/display_parameters_js.md.md | 2 | 27 | 완료 |
| docs/source/js/main_js.md.md | 6 | 128 | 완료 |
| docs/source/js/site_js.md.md | 2 | 15 | 완료 |
| docs/source/shaders/AddDisturbance_wgsl.md.md | 2 | 28 | 완료 |
| docs/source/shaders/BoundaryPass_wgsl.md.md | 2 | 33 | 완료 |
| docs/source/shaders/CalcMeans_wgsl.md.md | 2 | 21 | 완료 |
| docs/source/shaders/CalcWaveHeight_wgsl.md.md | 2 | 24 | 완료 |
| docs/source/shaders/Copytxf32_txf16_wgsl.md.md | 2 | 34 | 완료 |
| docs/source/shaders/ExtractNestedBoundaryTimeSeries_wgsl.md.md | 2 | 24 | 완료 |
| docs/source/shaders/ExtractTimeSeries_wgsl.md.md | 2 | 29 | 완료 |
| docs/source/shaders/MouseClickChange_wgsl.md.md | 2 | 29 | 완료 |
| docs/source/shaders/Pass0_wgsl.md.md | 2 | 26 | 완료 |
| docs/source/shaders/Pass1_HighOrder_wgsl.md.md | 2 | 30 | 완료 |
| docs/source/shaders/Pass1_wgsl.md.md | 2 | 30 | 완료 |
| docs/source/shaders/Pass2_HighOrder_HLLC_wgsl.md.md | 2 | 23 | 완료 |
| docs/source/shaders/Pass2_HighOrder_HLLEM_wgsl.md.md | 2 | 23 | 완료 |
| docs/source/shaders/Pass2_wgsl.md.md | 2 | 23 | 완료 |
| docs/source/shaders/Pass3A_COULWAVE_wgsl.md.md | 2 | 29 | 완료 |
| docs/source/shaders/Pass3B_COULWAVE_wgsl.md.md | 2 | 24 | 완료 |
| docs/source/shaders/Pass3_Bous_wgsl.md.md | 2 | 28 | 완료 |
| docs/source/shaders/Pass3_COULWAVE_wgsl.md.md | 2 | 31 | 완료 |
| docs/source/shaders/Pass3_NLSW_Spherical_wgsl.md.md | 2 | 35 | 완료 |
| docs/source/shaders/Pass3_NLSW_wgsl.md.md | 2 | 31 | 완료 |
| docs/source/shaders/Pass_Breaking_wgsl.md.md | 2 | 22 | 완료 |
| docs/source/shaders/README.md.md | 3 | 46 | 완료 |
| docs/source/shaders/SedTrans_Pass1_wgsl.md.md | 2 | 24 | 완료 |
| docs/source/shaders/SedTrans_Pass3_old_wgsl.md.md | 2 | 19 | 완료 |
| docs/source/shaders/SedTrans_Pass3_wBedUpdate_wgsl.md.md | 2 | 19 | 완료 |
| docs/source/shaders/SedTrans_Pass3_wgsl.md.md | 2 | 33 | 완료 |
| docs/source/shaders/SedTrans_UpdateBottom_testing_wgsl.md.md | 2 | 19 | 완료 |
| docs/source/shaders/SedTrans_UpdateBottom_wgsl.md.md | 2 | 22 | 완료 |
| docs/source/shaders/TriDiag_PCRx_COULWAVE_wgsl.md.md | 2 | 21 | 완료 |
| docs/source/shaders/TriDiag_PCRx_wgsl.md.md | 2 | 33 | 완료 |
| docs/source/shaders/TriDiag_PCRy_COULWAVE_wgsl.md.md | 2 | 21 | 완료 |
| docs/source/shaders/TriDiag_PCRy_wgsl.md.md | 2 | 29 | 완료 |
| docs/source/shaders/Update_TriDiag_coef_COULWAVE_wgsl.md.md | 2 | 26 | 완료 |
| docs/source/shaders/Update_TriDiag_coef_wgsl.md.md | 2 | 26 | 완료 |
| docs/source/shaders/Update_neardry_wgsl.md.md | 2 | 28 | 완료 |
| docs/source/shaders/duck_fragment_wgsl.md.md | 2 | 21 | 완료 |
| docs/source/shaders/duck_vertex_wgsl.md.md | 2 | 19 | 완료 |
| docs/source/shaders/fragment_testing_wgsl.md.md | 2 | 19 | 완료 |
| docs/source/shaders/fragment_wgsl.md.md | 3 | 41 | 완료 |
| docs/source/shaders/model_fragment_wgsl.md.md | 2 | 15 | 완료 |
| docs/source/shaders/model_vertex_wgsl.md.md | 2 | 20 | 완료 |
| docs/source/shaders/skybox_fragment_wgsl.md.md | 2 | 18 | 완료 |
| docs/source/shaders/skybox_vertex_wgsl.md.md | 2 | 21 | 완료 |
| docs/source/shaders/vertex3D_wgsl.md.md | 2 | 22 | 완료 |
| docs/source/shaders/vertex_wgsl.md.md | 2 | 20 | 완료 |

## 정정·보완 목록

| 기록:구간 | 구분 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|---|
| ARCHITECTURE.md.md:1–22 | 보완 | GPU 상태 저장·역할·계약 설명 축약 | 상태 저장 위치와 세부 역할 및 usually 한정 복원 | 3–21 |
| ARCHITECTURE.md.md:23–38 | 보완 | 시작 단계 세부 대상 누락 | 입력·할당 대상·layout 계약·build artifact 부재 보충 | 28–37 |
| ARCHITECTURE.md.md:39–60 | 보완 | pass 순서만 기술 | 각 pass의 동작과 프레임당 하나 이상 조건 보충 | 41–57 |
| ARCHITECTURE.md.md:61–88 | 보완 | 경계 기능 세부 조건 누락 | 각 경계 동작·물과 퇴적물 판독·usually 한정 보충 | 66–87 |
| ARCHITECTURE.md.md:89–109 | 보완 | 렌더 묶음 목적·공유 binding 의미 등 누락 | 렌더 동작과 문서 지도 설명 보충 | 93–109 |
| README.md.md:1–12 | 보완 | 소개 문장 일부 누락 | 공개 소스·파랑 종류·설치 조건·사용자와 용도·기여 안내 보충 | 7–11 |
| README.md.md:13–26 | 보완 | 기능 목록의 입력 의미·예제 대응·표시 변수 등 누락 | 각 기능 설명의 세부 내용 보충 | 16–25 |
| README.md.md:27–52 | 보완 | 매개변수·출력 종류 축약 | 배포 방식·수치 매개변수·출력 종류 보충 | 31·49–50 |
| README.md.md:53–74 | 보완 | 기여 안내 일부 누락 | 기여 유형·커밋과 push 대상·지침 내용 보충 | 65–73 |
| README.md.md:75–90 | 보완 | 문의 경로 목적과 마지막 문장 축약 | 문의 유형·기여자 설명·끝인사 보충 | 77–90 |
| docs/README.md.md:1–6 | 보완 | 문서 목적 세부 설명 누락 | 세션 간 보존할 작업 지식의 범위 보충 | 3 |
| docs/README.md.md:7–21 | 보완 | 문서별 역할을 포괄적으로 기술 | 문서별 세부 역할과 분류 기준 보충 | 9–20 |
| docs/README.md.md:22–31 | 보완 | 활성 구별의 한정 누락 | 현재 코드 경로에서 확인 가능한 경우라는 한정 보충 | 31 |
| docs/architecture/CONFIGURATION.md.md:1–16 | 보완 | 병합 입력·파생값 일부 누락 | 업로드 설정·render 치수·colorbar layout 보충 | 11–12 |
| docs/architecture/CONFIGURATION.md.md:17–54 | 보완 | 강제파 입력·경계 파일 방식 일부 누락 | 단일 sine 성분·동일 control·패널 업로드 보충 | 49–53 |
| docs/architecture/CONFIGURATION.md.md:55–80 | 보완 | 표본 상한 적용 단위 불명확 | 다중 출력 명세와 사각형별 상한 명시 | 61–63 |
| docs/architecture/CONFIGURATION.md.md:81–105 | 보완 | uniform 수정 의무·파생값 입력과 점검 설명 누락 | 필드 변경 계약·파생 과정·점검 지침 보충 | 83–105 |
| docs/architecture/DATA_AND_TEXTURES.md.md:1–28 | 보완 | 텍스처 저장 비교·갱신 계기·누적 변위 종류 누락 | CPU 행렬 대응·모드 의존·갱신 계기·퇴적물 출력 명시 | 3–27 |
| docs/architecture/DATA_AND_TEXTURES.md.md:29–61 | 보완 | 속도 성분·채널 재사용·소산 목적 누락 | x/y 속도 구별·순서 주의·운동량 확산 보충 | 34–60 |
| docs/architecture/DATA_AND_TEXTURES.md.md:62–94 | 보완 | 계수 배치 한정·복사 목적지·국소 수심 누락 | generally 한정·ping-pong 읽기/쓰기·국소 수심 보충 | 71–93 |
| docs/architecture/DATA_AND_TEXTURES.md.md:95–116 | 보완 | 캐시 목적과 렌더 텍스처 세부 설명 누락 | rgba32float 부하 감소·현재 화면·canvas overlay 보충 | 103–108 |
| docs/architecture/DATA_AND_TEXTURES.md.md:117–131 | 보완 | 할당 시점·shader 재사용·시각 기록 누락 | capture 시작·사각형별 재사용·실제 시각 별도 기록 보충 | 125–131 |
| docs/architecture/REFERENCE_PAPERS.md.md:1–15 | 보완 | 기술 교체와 상호작용의 설계상 위치 누락 | 기존 shader 방식 대체·설계 일부라는 설명 보충 | 11–14 |
| docs/architecture/REFERENCE_PAPERS.md.md:16–36 | 보완 | 연구와 구현의 연결 의미 축약 | 논문별 설명·후처리와 핵심 목표 구별·동등 중요성 보충 | 18–35 |
| docs/architecture/REFERENCE_PAPERS.md.md:37–50 | 보완 | 권장 순서의 목적 누락 | 각 논문을 읽는 목적 보충 | 41–49 |
| ARCHITECTURE.md.md:1–22 | 정정 | 항상 세 계층 수정 의무 | usually 한정을 반영 | 21 |
| docs/architecture/SIMULATION_PIPELINE.md.md:1–21 | 보완 | 프레임 역할과 queue flush 목적 축약 | 고정 순서·적응 방향·flag 의미·출력 종류·flush 목적 보충 | 3–20 |
| docs/architecture/SIMULATION_PIPELINE.md.md:22–40 | 보완 | 단계별 동작 일부 누락 | 각 pass 계산 대상·명시 상태 정리·누적 바닥 변화 보충 | 24–37 |
| docs/architecture/SIMULATION_PIPELINE.md.md:41–54 | 보완 | 분산 이력 목적과 두 번째 경계 적용 시점 누락 | Pass3 보조항·운동량 변경 가능성·다음 상태 전 적용 보충 | 49–53 |
| docs/architecture/SIMULATION_PIPELINE.md.md:55–66 | 보완 | 설정별 fetch·compile 누락 | 파일 선택의 처리 동작 보충 | 57 |
| docs/architecture/WEBGPU_BINDING_PATTERN.md.md:1–24 | 보완 | 그룹 생성·dispatch 부정·분리 예외 누락 | 생성 대상·보통 dispatch하지 않음·임시 복사 예외 보충 | 3–22 |
| docs/architecture/WEBGPU_BINDING_PATTERN.md.md:25–47 | 보완 | 임시 출력·공유 layout 설명 축약 | 출력 종류·대상·공유 이유와 위험 보충 | 27–46 |
| docs/architecture/WEBGPU_BINDING_PATTERN.md.md:48–71 | 보완 | 점검 대상의 수량·format·변경 조건 누락 | 모든 호출·format·재사용 전 점검·계약 변경 조건 보충 | 52–71 |
| docs/source/js/Config_Pipelines_js.md.md:1–17 | 보완 | 생성 입력·3D fragment·model 용도 누락 | 입력과 descriptor 역할·main fragment·box/model 용도 보충 | 7–15 |
| docs/source/js/Config_Pipelines_js.md.md:18–31 | 보완 | 변경 지침 마지막 문장 누락 | 최소 descriptor·기존 방식 일치 지침 보충 | 31 |
| docs/source/js/Copy_Data_to_Textures_js.md.md:1–20 | 보완 | 함수 입력·대상·시점 일부 누락 | 정확한 채널 계약·업로드 전 처리·측면별 저장·계수 입력 보충 | 7–18 |
| docs/source/js/Copy_Data_to_Textures_js.md.md:21–47 | 보완 | 정렬 목적·placeholder·영행 용도·수치 영향 누락 | 패딩 대상·우변 대안·시간 범위·변경 영향 보충 | 23–47 |
| docs/source/js/Create_Textures_js.md.md:1–23 | 정정 | uniform buffer까지 모두 allTextures에 추가하는 것으로 읽힘 | 추적 대상을 생성한 텍스처로 한정 | 22 |
| docs/source/js/Create_Textures_js.md.md:1–23 | 보완 | 팩토리 용도·자원 할당 설명 누락 | format별 용도와 uniform usage flag 보충 | 7–20 |
| docs/source/js/Create_Textures_js.md.md:24–32 | 보완 | usage flag 설정 이유 누락 | 임시 쓰기·복사·후속 표본 판독 순서 보충 | 26 |
| docs/source/js/File_Loader_js.md.md:1–20 | 보완 | 지원 입력과 외곽 처리 목적 누락 | 번들/사용자 입력·후속 GPU 복사·민감도 감소 보충 | 7–11 |
| docs/source/js/File_Loader_js.md.md:21–30 | 보완 | 업로드 목적·지도 좌표 대응·localhost 설명 누락 | 외부 파일 지원·render 정렬·API origin 거절 가능성 보충 | 23–29 |
| docs/source/js/File_Writer_js.md.md:1–16 | 보완 | 채널 수·호출 횟수·임계값 우선순위 누락 | 한 채널·사각형당 한 번·fallback 명시 | 11–14 |
| docs/source/js/File_Writer_js.md.md:17–30 | 보완 | config helper 예시·파일 입력·사용 전 감사 누락 | 입출력 예시와 감사 지침 보충 | 26–30 |
| docs/source/js/Handler_AddDisturbance_js.md.md:9–26 | 보완 | binding 출력 방향·퇴적물 변화·관련 상태 한정 누락 | depth-change 출력·퇴적물 바닥 변화·관련 상태 명시 | 16–22 |
| docs/source/js/Handler_BoundaryPass_js.md.md:9–32 | 보완 | binding 입출력 방향·파랑 행·복사 시점 누락 | 입력/출력·파랑 강제 행·dispatch 후 복사 명시 | 12–28 |
| docs/source/js/Handler_CalcMeans_js.md.md:9–32 | 정정 | COULWAVE가 텍스처를 사용한다고 표현 | COULWAVE도 텍스처에 기록한다는 방향 명시 | 32 |
| docs/source/js/Handler_CalcMeans_js.md.md:9–32 | 보완 | 임시 출력 방향·속도 변경 지침 누락 | 출력 표시와 속도 정의 변경 주의 보충 | 19–32 |
| docs/source/js/Handler_CalcWaveHeight_js.md.md:9–24 | 보완 | 채널 의미의 소비 용도 누락 | 시각화·출력 계약 명시 | 24 |
| docs/source/js/Handler_ExtractNestedBoundaryTimeSeries_js.md.md:9–21 | 보완 | 격자 정보 종류·가장자리만 쓰는 제한 누락 | grid bounds·edge-only compact 출력 보충 | 11·21 |
| docs/source/js/Handler_Pass1_js.md.md:9–25 | 보완 | 새 물리량 추가 지침 누락 | 채널 순서 의존성에 따른 추가 주의 보충 | 25 |
| docs/source/js/Handler_Pass2_js.md.md:9–31 | 보완 | binding 자료 의미·변형 추가 지침 누락 | 면 수심·속도·농도·쇄파 강도와 호환성 보충 | 12–31 |
| docs/source/js/Handler_Pass3_js.md.md:1–8 | 보완 | layout 정의·중요도 설명 누락 | 정의 대상과 원문 평가 보충 | 7 |
| docs/source/js/Handler_Pass3_js.md.md:35–49 | 보완 | 공통 layout 설계 이유 누락 | 모든 계열 공유 목적 보충 | 49 |
| docs/source/js/Handler_PassBreaking_js.md.md:9–27 | 보완 | 확산 대상 축약 | 쇄파 운동량 확산과 사용 텍스처 명시 | 23 |
| docs/source/js/Handler_Render_js.md.md:1–8 | 보완 | layout 생성 누락 | layout 생성 책임 보충 | 7 |
| docs/source/js/Handler_Render_js.md.md:9–30 | 보완 | 배열 텍스처의 자료 의미 누락 | 영상·렌더 캐시 구별 | 27·29 |
| docs/source/js/Handler_SedTrans_Pass1_js.md.md:9–26 | 보완 | 네 binding 유지 지침의 예외 누락 | 전체 pipeline 축소 예외 보충 | 26 |
| docs/source/js/Handler_Skybox_js.md.md:15–21 | 정정 | 현재 의존하지 않는 구현 사실로 표현 | 의존하지 않아야 한다는 설계 지침으로 정정 | 21 |
| docs/source/js/Handler_Skybox_js.md.md:15–21 | 보완 | 독립성 유지 목적 누락 | 3D 환경과 모델 상태 분리 목적 보충 | 21 |
| docs/source/js/Handler_Tridiag_js.md.md:1–18 | 보완 | 계수 방향·임시 출력 명시 누락 | 방향별 입력과 두 출력 명시 | 12–16 |
| docs/source/js/Handler_Tridiag_js.md.md:19–25 | 보완 | binding 제거 금지의 조건 누락 | 경로 분리 없이 제거 금지 보충 | 25 |
| docs/source/js/Handler_UpdateTrid_js.md.md:17–23 | 정정 | 모든 상태 변경 시 갱신 | 새 계수가 필요할 만큼 바뀔 때로 한정 | 19 |
| docs/source/js/Model_Loaders_js.md.md:15–27 | 보완 | albedo 업로드·모델별 uniform·객체 역할 누락 | 업로드 동작과 모델별 계약·분리 목적 보충 | 17–27 |
| docs/source/js/README.md.md:1–17 | 보완 | 직접 수치계산 부정·파일별 책임 일부 누락 | 제어 역할과 bootstrap·buffer·파랑 생성 시점 보충 | 3–14 |
| docs/source/js/README.md.md:18–38 | 정정 | 셰이더 문서 확인 | 원문의 Update 지시로 정정 | 36 |
| docs/source/js/README.md.md:18–38 | 보완 | I/O·UI 세부 책임·handler 정의 누락 | 파일별 입출력 종류·로그 재지정·layout 정의 보충 | 20–29 |
| docs/source/js/Run_Compute_Shader_js.md.md:1–18 | 보완 | 중복 제거 목적·반환·실행 로드 이유 누락 | boilerplate 제거·encoder 반환·정적 비번들 앱 설명 보충 | 7–17 |
| docs/source/js/Run_Compute_Shader_js.md.md:19–27 | 보완 | 즉시 제출의 영향 누락 | 성능·동기화 가능성 보충 | 27 |
| docs/source/js/Run_Tridiag_Solver_js.md.md:1–19 | 보완 | PCR 계산 담당과 반복 제어 누락 | WGSL 계산과 JS 제어 책임 명시 | 7 |
| docs/source/js/Run_Tridiag_Solver_js.md.md:20–30 | 보완 | 경계 계수 목적·중간 출력·제출 방식 비교 누락 | 가장자리 제어·계수만 출력·활성 의존성 처리 보충 | 22–30 |
| docs/source/js/Time_Series_js.md.md:1–15 | 보완 | buffer 복사·구형 유틸리티의 비중 누락 | 판독 전 복사와 현재 비중 보충 | 11–14 |
| docs/source/js/Time_Series_js.md.md:16–22 | 보완 | 관측 slot 대응·소량 readback 계약 누락 | 인덱스 대응·전체장용이 아닌 제한 보충 | 18–22 |
| docs/source/js/Wave_Generator_js.md.md:16–23 | 보완 | TMA 방향 조정의 정확한 조건·시점·목적 누락 | 횡방향 두 경계·업로드 전·성분별 위상 일치 보충 | 22 |
| docs/source/js/agent_controls_js.md.md:1–16 | 보완 | 메시지 방식·응답 표시 위치·stale 위험·console 표시 누락 | postMessage·UI 소비처·getter 필요 이유·text stream 보충 | 9–15 |
| docs/source/js/agent_controls_js.md.md:17–50 | 보완 | 직접 변경 부정·registry 역할·패널 이름 누락 | 명령 계약과 catalog/handler 역할 보충 | 19–35 |
| docs/source/js/agent_controls_js.md.md:51–70 | 보완 | 표면 명령 선택 입력·편집 control 종류 누락 | radius/friction·네 control 종류 보충 | 51·55 |
| docs/source/js/agent_controls_js.md.md:71–99 | 보완 | hidden 버튼·키 대응·fullscreen 목적 누락 | 숨김 상태·semantic mapping·기존 동작 보존 보충 | 85–98 |
| docs/source/js/agent_controls_js.md.md:100–119 | 보완 | 자연어 부정·모드 전환·수치 보존·갱신 책임·측면 수량 누락 | 모드와 책임·기존 값 보존·한 측면 설정 명시 | 102–118 |
| docs/source/js/agent_controls_js.md.md:120–132 | 정정 | chartDataUpdate 초기화 금지 | chartDataUpdate 설정 금지로 정정 | 126 |
| docs/source/js/agent_controls_js.md.md:120–132 | 보완 | 우클릭 대상·payload 목적·가능한 경우 한정 누락 | 선택 관측 갱신·부모 solver 불필요·명령 확장 원칙 보충 | 126–132 |
| docs/source/js/constants_load_calc_js.md.md:1–13 | 보완 | 재계산 시점·저장 위치 누락 | 로드/편집 후 재계산·CPU 저장 명시 | 7–10 |
| docs/source/js/constants_load_calc_js.md.md:14–25 | 보완 | 출력 조건·선형 구조 필드·스키마 역할 누락 | 선택성·사각형별 상한·절단 조건·필드 의미 보충 | 20–24 |
| docs/source/js/constants_load_calc_js.md.md:26–44 | 보완 | 파생값 입력 금지·dispatch 입력·경계 종류 누락 | 독립 입력 제한과 계산 의미 보충 | 28–35 |
| docs/source/js/display_parameters_js.md.md:1–18 | 보완 | 부피 종류·run status·활성 한정 누락 | DOM 표시 대상 보충 | 7–13 |
| docs/source/js/display_parameters_js.md.md:19–27 | 보완 | 항목 제한 목적·부작용 금지 누락 | 페이지 크기 제어·표시 전용 원칙 보충 | 21–27 |
| docs/source/js/main_js.md.md:1–24 | 정정 | 로컬 예제 실행을 막지 않음 | local/example overlay loading으로 대상 정정 | 20 |
| docs/source/js/main_js.md.md:1–24 | 보완 | 자원 종류 누락 | uniform·texture 할당 대상 전부 보충 | 17–18 |
| docs/source/js/main_js.md.md:25–64 | 보완 | Agent 입력 형식·부정·역할 경계·chart reset 누락 | text/blob·동일 초기화·경로 불변·자연어 책임·창 이동 보충 | 27–63 |
| docs/source/js/main_js.md.md:65–81 | 보완 | 프레임 수량·조절 목적·PCR 시점 누락 | 하나 이상·응답성 균형·명시 pass 뒤 실행 보충 | 67–78 |
| docs/source/js/main_js.md.md:82–108 | 보완 | UI 세부 동작·좌표 변환 목적·검증·출력·부정 누락 | 물리 키·gesture·구면 camera·pointer 대응·끝점 검증 보충 | 92–107 |
| docs/source/js/main_js.md.md:109–117 | 보완 | 공통 layout 이유·할당 시점 누락 | binding 한도·capture 시작 명시 | 113·116 |
| docs/source/js/main_js.md.md:118–128 | 보완 | preview 시점·Design 그리기 순서·scissor 조건·실패 목적 누락 | render write 전·quad 뒤 footprint·표시 조건·순서 보존 보충 | 119–128 |
| docs/source/js/site_js.md.md:1–8 | 정정 | placeholder를 단정 | appears 불확실성 복원 | 7 |
| docs/source/shaders/BoundaryPass_wgsl.md.md:23–33 | 보완 | 조건·안정성 목적·경계 종류 누락 | 적절한 경우 한정·shoreline 안정성·경계 영역 명시 | 25–33 |
| docs/source/shaders/CalcMeans_wgsl.md.md:13–21 | 정정 | counter를 계수로 번역 | 단계 counter 조건으로 정정 | 15 |
| docs/source/shaders/CalcMeans_wgsl.md.md:13–21 | 보완 | 건조 placeholder 목적·자료 소비처 누락 | 유효 수면 오인 방지·렌더링/출력 제공 보충 | 17·21 |
| docs/source/shaders/CalcWaveHeight_wgsl.md.md:1–17 | 보완 | 표준편차 계산·추정 의미 누락 | 분산과 파고 사이 계산 단계 보충 | 11 |
| docs/source/shaders/CalcWaveHeight_wgsl.md.md:18–24 | 정정 | counter를 계수로 번역 | 외부 counter 초기화로 정정 | 24 |
| docs/source/shaders/ExtractNestedBoundaryTimeSeries_wgsl.md.md:1–17 | 보완 | 바닥 입력·영값 목적 누락 | 건조 판단 입력과 DEM 수면 오인 방지 보충 | 7·16 |
| docs/source/shaders/ExtractTimeSeries_wgsl.md.md:23–29 | 보완 | 변수 추가 시 양쪽 변경 의무 누락 | GPU/CPU 동시 수정 명시 | 29 |
| docs/source/shaders/MouseClickChange_wgsl.md.md:21–29 | 보완 | crest 정의·end cap 생성·임시 의미·shader 수정 누락 | 유한 선분 처리와 양측 변경 책임 보충 | 25–29 |
| docs/source/shaders/Pass0_wgsl.md.md:20–26 | 보완 | 사전 pass의 분리 목적 누락 | wet/dry 검사 분리 목적 보충 | 22 |
| docs/source/shaders/Pass1_HighOrder_wgsl.md.md:13–30 | 보완 | 동반 점검 이유 누락 | 표준보다 높은 경계·주기 민감도 보충 | 30 |
| docs/source/shaders/Pass2_HighOrder_HLLC_wgsl.md.md:13–23 | 보완 | 재구성 역할·변경 지침 대상 누락 | 고차 면 제공·속도/star-state 수정 범위 보충 | 19·23 |
| docs/source/shaders/Pass2_HighOrder_HLLEM_wgsl.md.md:13–23 | 정정 | 속도까지 flux와 혼합하는 것으로 읽힘 | HLL 계산·속도 추정·선형화 flux 구성·혼합 순서 구분 | 15 |
| docs/source/shaders/Pass2_wgsl.md.md:1–12 | 보완 | 파속 차원 누락 | one-dimensional 명시 | 11 |
| docs/source/shaders/Pass2_wgsl.md.md:13–23 | 보완 | 건조 처리 목적·변경 전파 의무 누락 | 불안정 교환 방지·소비 pass 변경 지침 보충 | 15·23 |
| docs/source/shaders/Pass3A_COULWAVE_wgsl.md.md:1–22 | 보완 | 보조항 소비처 누락 | 주 COULWAVE 소비처 명시 | 7 |
| docs/source/shaders/Pass3B_COULWAVE_wgsl.md.md:1–17 | 보완 | 출력과 포장의 수행 주체·순서 불명확 | shader 출력 후 JavaScript 포장 명시 | 11 |
| docs/source/shaders/Pass3_Bous_wgsl.md.md:15–28 | 보완 | NLSW 차이·선택 마찰·출력 용도 누락 | 차이·선택성·미분 소비처 보충 | 17–22 |
| docs/source/shaders/Pass3_COULWAVE_wgsl.md.md:1–12 | 보완 | 보조층 판독 목적 누락 | 고차 source term 추가 목적 보충 | 7 |
| docs/source/shaders/Pass3_COULWAVE_wgsl.md.md:13–31 | 정정 | 항상 동시 수정 의무 | usually 한정과 layer-copy sequence 복원 | 31 |
| docs/source/shaders/Pass3_COULWAVE_wgsl.md.md:13–31 | 보완 | 결합도 평가·확산 대상 누락 | 원문 평가와 운동량 확산 명시 | 20·31 |
| docs/source/shaders/Pass3_NLSW_Spherical_wgsl.md.md:1–21 | 보완 | 공유 계약 종류·uniform 목적 누락 | 계약 항목과 위도 압력 경사 목적 보충 | 7·18 |
| docs/source/shaders/Pass3_NLSW_Spherical_wgsl.md.md:22–35 | 보완 | 수식 항의 의미 누락 | 구면 압력 경사·곡률 명시 | 28 |
| docs/source/shaders/Pass3_NLSW_wgsl.md.md:1–20 | 보완 | 선택 강제·혼합 대상 누락 | 압력/수심 변화·운동량 혼합 보충 | 15–16 |
| docs/source/shaders/Pass3_NLSW_wgsl.md.md:21–31 | 보완 | 편측 경사의 목적 누락 | 잘못된 중심 경사 회피 보충 | 27 |
| docs/source/shaders/Pass_Breaking_wgsl.md.md:16–22 | 정정 | 세 입력으로 임계값·강도·와점성을 일괄 결정 | detadt 추정·임계값 선택·강도 변환 순서 구분 | 18 |
| docs/source/shaders/README.md.md:1–19 | 보완 | WGSL 계약·Pass3별 책임 축약 | 입출력·방정식별 source/time integration 보충 | 3·15–17 |
| docs/source/shaders/README.md.md:20–34 | 보완 | 퇴적물 파일별 역할·와점성 누락 | 세 pass 책임과 와점성 보충 | 23–32 |
| docs/source/shaders/README.md.md:35–46 | 보완 | 렌더 파일군별 의미 누락 | skybox·box·glTF textured model 명시 | 39–41 |
| docs/source/shaders/SedTrans_Pass3_old_wgsl.md.md:1–12 | 정정 | 차이 정도 생략 | slightly 한정 복원 | 7 |
| docs/source/shaders/SedTrans_Pass3_wgsl.md.md:20–33 | 보완 | 침식/소류사 출력 소비처 누락 | bottom update 용도 보충 | 28 |
| docs/source/shaders/SedTrans_UpdateBottom_wgsl.md.md:1–14 | 보완 | 경계 완화 목적 누락 | boundary artifact 방지 목적 보충 | 13 |
| docs/source/shaders/TriDiag_PCRx_COULWAVE_wgsl.md.md:17–21 | 보완 | 변환 시점 위험의 구체 설명 누락 | 조기/지연 변환 가능성 보충 | 19 |
| docs/source/shaders/TriDiag_PCRx_wgsl.md.md:1–22 | 보완 | P의 수량 의미 누락 | 전체 x 반복 수 명시 | 16 |
| docs/source/shaders/TriDiag_PCRx_wgsl.md.md:23–33 | 정정 | 두 자원의 읽기/쓰기 방향 불명확 | current_state 읽기·txtemp2 쓰기 구분 | 27 |
| docs/source/shaders/TriDiag_PCRx_wgsl.md.md:23–33 | 보완 | 중간 출력 생략·x만 갱신 제한 누락 | 중간 solution 생략·성분 한정 보충 | 27·33 |
| docs/source/shaders/TriDiag_PCRy_wgsl.md.md:23–29 | 정정 | 두 자원의 읽기/쓰기 방향 불명확 | current_state 읽기·txtemp2 쓰기 구분 | 25 |
| docs/source/shaders/Update_TriDiag_coef_COULWAVE_wgsl.md.md:1–19 | 보완 | 계수의 수직 좌표 의존성 누락 | vertical-coordinate-dependent 명시 | 7 |
| docs/source/shaders/Update_neardry_wgsl.md.md:18–28 | 정정 | 실행 구현 사실로 표현 | should run 지침으로 정정 | 28 |
| docs/source/shaders/duck_fragment_wgsl.md.md:15–21 | 정정 | 개선 필요 단정 | likely 한정 복원 | 21 |
| docs/source/shaders/fragment_testing_wgsl.md.md:1–12 | 보완 | 주 fragment와 대체로 같다는 설명 누락 | 유사성 정도와 차이 종류 보충 | 7 |
| docs/source/shaders/fragment_wgsl.md.md:21–28 | 보완 | 난류·plume 적용 동작 축약 | texture modulation·tinting 의미 보충 | 27 |
| docs/source/shaders/fragment_wgsl.md.md:29–41 | 보완 | 선분 거리 검사·배경 누락 | preview 선의 검사 방식·colorbar 배경 보충 | 35·37 |
| docs/source/shaders/skybox_fragment_wgsl.md.md:16–18 | 보완 | 작게 구성한 설계 설명 누락 | deliberately small 설명 보충 | 18 |
| docs/source/shaders/vertex3D_wgsl.md.md:16–22 | 보완 | 원천 점검의 선택지 누락 | cache/full state 선택 점검 명시 | 22 |
| docs/source/shaders/vertex_wgsl.md.md:1–13 | 보완 | UV 전달 대상 누락 | fragment로의 전달 명시 | 7 |

정정 19, 보완 120, 이상 없음 89
