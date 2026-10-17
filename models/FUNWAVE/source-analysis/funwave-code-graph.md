---
title: "FUNWAVE-TVD 코드 관계성 — USE 의존·CALL 그래프 (전수조사 토대)"
model: FUNWAVE
citation_status: verified
verification_method: "models/FUNWAVE/raw/source_code/FUNWAVE-TVD/src/*.F 전수 grep(USE/CALL/SUBROUTINE) + 직접 read. 규모·그래프 수치는 src 기준 집계. 2026-06-13. 2026-10-18 FUNWAVE recovery 대조 보고서 반영"
last_source_check: "2026-10-18 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-13
source_scope: FUNWAVE-TVD
---

# FUNWAVE-TVD 코드 관계성

> `b4c322e`의 `src/*.F` 38개를 대상으로 LF 바이트는 33,760개이다. 논리 행은 33,761개이다. 대소문자를 무시한 행 시작 `SUBROUTINE`은 218개이다. 행 시작 `USE`는 414개이다. `MODULE PROCEDURE`를 제외한 모듈 선언은 15개이다. 행 시작 `CALL`은 1,301개이다. 근거: [aux-docs-build §4 FN1-903](../../../_staging/recovery/compare/funwave-aux-docs-build-vs-code.md#4-노트-대조와-수정안). [10-18 대조 정정]

빌드 대상은 `FUNWAVE-TVD/GNUMake/Essential/Make_Essential:204–211`의 MODS·MAIN 목록으로 정해진다. 이 선언 집계에는 대체 파일과 전처리 서명이 포함된다. 근거: [v21-manual §4 FV1-570](../../../_staging/recovery/compare/funwave-v21-manual-vs-code.md#4-노트-대조와-수정안), [callflow §6](../../../_staging/recovery/flow/FUNWAVE-callflow.md#6-기존-노트-대조와-수정안). [10-18 대조 정정]

서브루틴별 상세는 [funwave-source-map.md](funwave-source-map.md)와 아래 물리 소스 노트에 정리되어 있다. [10-18 대조 정정]

## 1. 모듈 USE 의존 (레이어링)

```
PARAM (mod_param, 상수·MPI)
  └→ GLOBAL (mod_global, 전역 배열·변수)
       └→ INPUT_READ (mod_input, input.txt 파서)
            └→ [feature 모듈] mod_tide·meteo·vessel·sediment·tracer·precipitation·subgrid·foam·bathy_correction·time_spectra
                 └→ main.F (상위 모듈 전부 use: TIDE/METEO/VESSEL/SEDIMENT/TRACER/PRECIPITATION/TIME_SPECTRA/MOD_FOAM)
```
- `USE` 를 쓰는 **38개 소스 중 23개**가 `PARAM`·`GLOBAL` 을 함께 의존하고, 나머지는 `GLOBAL` 만 쓰거나(대부분) 어느 쪽도 쓰지 않는다(`mod_param.F` 는 둘 다 없음, `mod_global.F` 는 `PARAM` 만). → **GLOBAL = 전역 상태 허브**(배열 U,V,Eta,H,depth 등 + nesting/dispersion 변수).
- 비-module .F(fluxes·dispersion·etauv_solver·bc·breaker·wavemaker·sponge·io·parallel 등)는 `USE GLOBAL`로 전역 상태 공유(F90 module + host association).
- 특이: mod_sediment→VESSEL_MODULE, mod_time_spectra→TIDE_MODULE (feature 간 의존).

## 2. CALL 그래프 — 지배 solver chain

각 RK 단계에서 `IF(DISPERSION)THEN`이 참이면 `CAL_DISPERSION`을 먼저 호출한다. 이어서 `FLUXES`, `SourceTerms`, `ESTIMATE_HUV`를 호출한다. 근거: `FUNWAVE-TVD/src/main.F:380–414`, [aux-docs-build §4 FN1-920](../../../_staging/recovery/compare/funwave-aux-docs-build-vs-code.md#4-노트-대조와-수정안). [10-18 대조 정정]

FLUXES의 직접 자식은 선택 재구성·WAVE_SPEED·선택 수치 플럭스·BOUNDARY_CONDITION이다. FLUX_AT_INTERFACE_HLL의 직접 자식은 HLL이다. HLL은 WAVE_SPEED를 호출하지 않는다. 근거: `FUNWAVE-TVD/src/fluxes.F:64,110,115,154`, callflow:RF-046. [10-18 대조 정정]

CAL_DISPERSION과 ESTIMATE_HUV는 주 프로그램의 서로 다른 직접 자식이다. ESTIMATE_HUV의 직접 자식은 GET_Eta_U_V_HU_HV다. GET_Eta_U_V_HU_HV는 전처리·주기 조건에 따라 삼중대각 루틴을 선택한다. 근거: `FUNWAVE-TVD/src/main.F:383,414`, `FUNWAVE-TVD/src/etauv_solver.F:348,398–545`, [callflow §6.2](../../../_staging/recovery/flow/FUNWAVE-callflow.md#62-우선-수정할-세-노트의-교체-문장). [10-18 대조 정정]

전체 실행 흐름은 [callflow §4의 흐름도](../../../_staging/recovery/flow/FUNWAVE-callflow.md#4-mermaid-흐름도)에 있다. 이 보고서의 렌더 확인은 10-18 기록에 있다.

## 3. CALL 허브 (관계 중심, 호출빈도)

| subroutine | 호출수 | 역할 |
|---|--:|---|
| READ_STRING / READ_LOGICAL / READ_INTEGER / READ_FLOAT | — | input.txt 파싱. 정의는 `FUNWAVE-TVD/src/mod_input.F:76,126,175,220`이다. Fortran 대소문자 차이를 다른 함수로 세지 않는다. [10-18 대조 정정] |
| **PHI_COLL** | 87 | 분산/nesting 변수 collection (bc.F; 분산 solve 전처리 허브) |
| PutFile | 92 | 출력 (io.F) |
| **CONSTRUCT_HO_X / _Y** | 39 / 39 | MUSCL 고차 재구성 (fluxes.F; flux 계산 허브) |
| DelxFun / DelyFun | 27 / 27 | 1차 미분의 정의 파일은 fluxes.F다. derivatives.F의 DERIVATIVE_X/Y와 구분한다. 근거: `FUNWAVE-TVD/src/fluxes.F:239,293`, `FUNWAVE-TVD/src/derivatives.F:123,158`, v21-manual:FV1-573. 호출 수는 `FUNWAVE-TVD/src/*.F`의 행 시작 `CALL DelxFun`·`CALL DelyFun`을 대소문자 없이 각각 센 값이다. [10-18 대조 정정] [10-18 전수 검증 보완] |
| MPI_FINALIZE/Gather | 102/29 | 병렬 (parallel.F) |

→ **물리 허브**: `CONSTRUCT_HO_*`(flux 재구성) · `PHI_COLL`(분산 수집) · `TRIDx/y`(tridiagonal 해) · `DERIVATIVE_*`(분산 미분). **인프라 허브**: READ_*(입력) · PutFile(출력) · MPI_*(병렬).

## 4. 파일별 subroutine 분포 (218개)

fluxes 23 · wavemaker 17 · fluxes_33v 17 · fluxes_21v 14 · io 13 · samples 11 · mod_meteo 10 · derivatives 10 · sponge 7 · mod_tide 7 · mod_foam_upwinding 7 · misc 7 · bc 6 · mod_tracer 6 · mod_input 6 · mod_foam 6 · tridiagnal 5 · mod_vessel 5 · mod_subgrid 5 · parallel 4 · mod_time_spectra 4 · mod_sediment 4 · init 3 · statistics 2 · nesting 2 · (그 외 main/etauv_solver/dispersion/breaker/sources/masks/mixing/mod_* 등)

## 5. 전수조사 진행 (체크리스트) — CPU 완료

- [x] 코드 관계성 그래프 (본 노트)
- [x] 모듈 인벤토리·흐름 ([`funwave-source-map.md`](funwave-source-map.md))
- [x] **flux·MUSCL-TVD**(fluxes 23subr+derivatives 10) → [`funwave-flux-tvd.md`](funwave-flux-tvd.md)
- [x] **분산·tridiagonal**(dispersion·etauv_solver·tridiagnal·PHI_COLL) → [`funwave-dispersion-solver.md`](funwave-dispersion-solver.md)
- [x] **물리 source**(breaker·wavemaker 17subr·sponge·sources·mixing·masks) → [`funwave-physics-sources.md`](funwave-physics-sources.md)
- [x] **feature 모듈 11종** → [`funwave-feature-modules.md`](funwave-feature-modules.md)
- [x] **인프라**(bc·init·parallel·io·samples·statistics·nesting·misc·mod_global/param/input) → [`funwave-infrastructure.md`](funwave-infrastructure.md)
- [x] **FUNWAVE-GPU**(CUDA Fortran *_gpu.F·mod_cuda) → [`funwave-gpu-source.md`](funwave-gpu-source.md) (cusparse·shared·stream·MGPU)

TVD의 218개는 위 집계 규칙에 따른 SUBROUTINE 선언 수다. 기존 GPU 노트의 판독 목록은 mod_cuda.F와 일곱 *_gpu.F다. recovery GPU 보고서는 41파일 목록을 대조한다. 근거: [gpu-vs-tvd §4 FG1-901](../../../_staging/recovery/compare/funwave-gpu-vs-tvd.md#4-노트-대조와-수정안). [10-18 대조 정정]

## 6. 연결

- [funwave-source-map.md](funwave-source-map.md) · [funwave-build-and-blackwell-port.md](funwave-build-and-blackwell-port.md) · [funwave-tvd-manual.md](../manual-notes/funwave-tvd-manual.md). 기본 GPU 경로는 x 방향 transpose와 자체 Thomas 풀이를 사용한다. cuSPARSE batched 호출은 TriSolver=1의 별도 경로다. MGPU에서는 sweep의 MPI 계수 전달이 남는다. 근거: [gpu-vs-tvd §4 FG1-802](../../../_staging/recovery/compare/funwave-gpu-vs-tvd.md#4-노트-대조와-수정안). [10-18 대조 정정]

## 문서와 코드 차이 (10-18 대조)

문서 판: FUNWAVE-TVD 3.0 문서 "Release Dec 2016"(공개 저장소 PDF 마지막 변경 `fef45a7`, 2018-02-24), 2.1 매뉴얼·code_analysis `b9c035d`(2016-11-03), Intro-TN 2015-07. 코드 판: 공개 저장소 `github.com/fengyanshi/FUNWAVE-TVD` HEAD `b4c322e`(2025-01-24), `FUNWAVE-TVD/src/main.F:47` `!    VERSION 3.0`.

근거 보고서: [inputs](../../../_staging/recovery/compare/funwave-inputs-vs-code.md#5-차이-결론), [v21-manual](../../../_staging/recovery/compare/funwave-v21-manual-vs-code.md#5-차이-결론), [aux-docs-build](../../../_staging/recovery/compare/funwave-aux-docs-build-vs-code.md#5-차이-결론), [callflow](../../../_staging/recovery/flow/FUNWAVE-callflow.md#8-차이-결론).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| inputs:FI1-323 | 입력 함수 네 종류 | `05fdbedb:models/FUNWAVE/source-analysis/funwave-code-graph.md:48`(반영 전 노트 줄) `READ_FLOAT/LOGICAL/STRING/Float` | 노트의 `READ_FLOAT/LOGICAL/STRING/Float`; `7b93138:src/mod_input.F:66` `Module Procedure READ_FLOAT`; `7b93138:src/mod_input.F:67` `Module Procedure READ_STRING`; `7b93138:src/mod_input.F:68` `Module Procedure READ_LOGICAL`; `7b93138:src/mod_input.F:69` `Module Procedure READ_INTEGER`; `fef45a7:src/mod_input.F:66` `Module Procedure READ_FLOAT`; `fef45a7:src/mod_input.F:69` `Module Procedure READ_INTEGER` 판정 기록: [AD1](../../../_staging/recovery/compare/FUNWAVE-git-verify-AD1.md) 같은 행. | B | 입력 함수는 READ_FLOAT, READ_STRING, READ_LOGICAL, READ_INTEGER이다. 노트의 중복 Float를 READ_INTEGER로 고친다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] [10-18 표본 정정] |
| v21-manual:FV1-134 | DelxFun | `funwave_tvd_2.1_manual.pdf` p.28: “DelxFun ... It is called by DelxFun.” | `FUNWAVE-TVD/src/fluxes.F:293` `SUBROUTINE DelxFun(DX,M,N,DIN,DOUT)`; `FUNWAVE-TVD/src/fluxes.F:213` `CALL DelxFun(DX,Mloc,Nloc,U,DelxU)`; [git 이력 판정](../../../_staging/recovery/compare/FUNWAVE-git-verify-AD2.md), `2e72b18:fluxes.F:182` `CALL DelxFun(DX,Mloc,Nloc,U,DelxU)` | B | 존재한다. 직접 호출자는 `DelxyFun`과 분산 보정 재구성 경로다. 자기 자신을 호출하지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| v21-manual:FV1-186 | WAVE_SPEED | `funwave_tvd_2.1_manual.pdf` p.31: “WAVE_SPEED ... It is called by MAIN.” | `FUNWAVE-TVD/src/fluxes.F:352–353` `SUBROUTINE WAVE_SPEED(M,N,M1,N1,UL,UR,VL,VR,HxL,HxR,HyL,HyR,&` / `SxL,SxR,SyL,SyR)`; [git 이력 판정](../../../_staging/recovery/compare/FUNWAVE-git-verify-AD2.md), `2e72b18:fluxes.F:70` `CALL WAVE_SPEED(Mloc,Nloc,Mloc1,Nloc1,UxL,UxR,VyL,VyR,HxL,HxR,HyL,HyR, &` | B | 존재한다. 직접 호출자는 `FLUXES`다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| v21-manual:FV1-570 | 노트 source-analysis/funwave-code-graph.md:13 | `05fdbedb:models/FUNWAVE/source-analysis/funwave-code-graph.md:13`(반영 전 노트 줄) `33,760줄` `218 subroutine` `15 module` `414 USE` `1338 CALL` | `FUNWAVE-TVD/GNUMake/Essential/Make_Essential:204–211`의 MODS·MAIN 선택 목록 | C | 노트 13행의 218 subroutine 등 수치는 그 노트에 기록된 정적 집계다. 빌드 대상은 Make_Essential의 MODS·MAIN 목록으로 정해진다. 따라서 그 수치를 현재 실행 파일에 포함되는 루틴 수로 사용하지 않는다. 이 C는 노트의 집계 범위 설명 누락이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 표본 정정] |
| v21-manual:FV1-571 | 노트 source-analysis/funwave-code-graph.md:34 | `05fdbedb:models/FUNWAVE/source-analysis/funwave-code-graph.md:34`(반영 전 노트 줄) `FLUX_AT_INTERFACE_HLL ─ HLL ─ WAVE_SPEED` | `2e72b18:fluxes.F:70` `CALL WAVE_SPEED(Mloc,Nloc,Mloc1,Nloc1,UxL,UxR,VyL,VyR,HxL,HxR,HyL,HyR, &`; `FUNWAVE-TVD/src/fluxes.F:64,110,154` | B | FLUXES가 재구성 다음 WAVE_SPEED를 호출한다. 그 뒤 FLUX_AT_INTERFACE_HLL을 호출한다. HLL이 WAVE_SPEED를 호출하는 연결을 삭제한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] [10-18 표본 정정] |
| v21-manual:FV1-572 | 노트 source-analysis/funwave-code-graph.md:48 | `05fdbedb:models/FUNWAVE/source-analysis/funwave-code-graph.md:48`(반영 전 노트 줄) `READ_FLOAT/LOGICAL/STRING/Float` | `2e72b18:io.F:131` `CALL READ_STRING(TITLE,FILE_NAME,'TITLE',ierr)`; `FUNWAVE-TVD/src/mod_input.F:76,126,175,220` | B | parser 네 종류를 READ_STRING,READ_LOGICAL,READ_INTEGER,READ_FLOAT로 적는다. Fortran 대소문자 차이를 다른 함수로 세지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] [10-18 표본 정정] |
| v21-manual:FV1-573 | 노트 source-analysis/funwave-code-graph.md:52 | `05fdbedb:models/FUNWAVE/source-analysis/funwave-code-graph.md:52`(반영 전 노트 줄) `DelxFun / DelyFun` `1차 미분 (derivatives.F)` | `2e72b18:fluxes.F:182` `CALL DelxFun(DX,Mloc,Nloc,U,DelxU)`; `FUNWAVE-TVD/src/fluxes.F:293` `SUBROUTINE DelxFun(DX,M,N,DIN,DOUT)` | B | DelxFun과 DelyFun의 정의 파일을 fluxes.F로 고친다. derivatives.F의 DERIVATIVE_X/Y와 구분한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] [10-18 표본 정정] |
| aux-docs-build:FN1-373 | Figure 11 호출 사슬 | funwave_code_analysis.pdf p.12: `FUNWAVE_TVD`, `INITIALIZATION`, `wall_time_secs`, `CALCULATE_FRICTION_SPONGE`, `CALCULATE_DIFFUSION_SPONGE`, `WAVEMAKER_INITIALIZATION`, `CALCULATE_TMA_Cm_Sm`, `WK_WAVEMAKER_IRREGULAR_WAVE`, `OUTPUT`, `CHECK_BLOWUP`, `PREVIEW`, `CALCULATE_MEAN`, `PREVIEW_MEAN`, `PutFile`, `real` | `bfc2f8c:main.F:163` `CALL INITIALIZATION`; `bfc2f8c:main.F:177` `CALL WALL_TIME_SECS(tbegin)`<br>`FUNWAVE-TVD/src/main.F:214` `CALL INITIALIZATION`; `FUNWAVE-TVD/src/main.F:278` `if(myid == 0) tbegin = MPI_Wtime( )`; `FUNWAVE-TVD/src/main.F:280` `CALL CPU_TIME(tbegin)`<br>`bfc2f8c:init.F:803` `CALL WAVEMAKER_INITIALIZATION`<br>`bfc2f8c:init.F:814` `CALL CALCULATE_DIFFUSION_SPONGE(Mloc,Nloc,Nghost,DX,DY,&`<br>`bfc2f8c:init.F:815` `Sponge_west_width,Sponge_east_width,&`<br>`bfc2f8c:init.F:816` `Sponge_south_width,Sponge_north_width, &`<br>`bfc2f8c:init.F:817` `R_sponge,A_sponge,nu_sponge)`<br>`bfc2f8c:init.F:825` `CALL CALCULATE_FRICTION_SPONGE(Mloc,Nloc,Nghost,DX,DY,&`<br>`bfc2f8c:init.F:826` `Sponge_west_width,Sponge_east_width,&`<br>`bfc2f8c:init.F:827` `Sponge_south_width,Sponge_north_width, &`<br>`bfc2f8c:init.F:828` `R_sponge,A_sponge,CD_4_SPONGE)`<br>`FUNWAVE-TVD/src/init.F:963` `CALL WAVEMAKER_INITIALIZATION`<br>`FUNWAVE-TVD/src/init.F:974` `CALL CALCULATE_DIFFUSION_SPONGE(Mloc,Nloc,Nghost,DX,DY,&`<br>`FUNWAVE-TVD/src/init.F:975` `Sponge_west_width,Sponge_east_width,&`<br>`FUNWAVE-TVD/src/init.F:976` `Sponge_south_width,Sponge_north_width, &`<br>`FUNWAVE-TVD/src/init.F:977` `R_sponge,A_sponge,nu_sponge)`<br>`FUNWAVE-TVD/src/init.F:985` `CALL CALCULATE_FRICTION_SPONGE(Mloc,Nloc,Nghost,DX,DY,&`<br>`FUNWAVE-TVD/src/init.F:986` `Sponge_west_width,Sponge_east_width,&`<br>`FUNWAVE-TVD/src/init.F:987` `Sponge_south_width,Sponge_north_width, &`<br>`FUNWAVE-TVD/src/init.F:988` `R_sponge,A_sponge,CD_4_SPONGE)`<br>`bfc2f8c:mixing.F:61` `CALL CALCULATE_MEAN(T_INTV_mean,T_sum,DT,Mloc,Nloc,U,V,ETA,ETA0,&`<br>`bfc2f8c:mixing.F:62` `Umean,Vmean,ETAmean,Usum,Vsum,ETAsum,WaveHeightRMS, &`<br>`bfc2f8c:mixing.F:63` `WaveHeightAve,Emax,Emin,Num_Zero_Up,Ibeg,Iend,Jbeg,Jend, &`<br>`bfc2f8c:mixing.F:64` `HrmsSum,HavgSum, &`<br>`bfc2f8c:mixing.F:65` `!ykchoi`<br>`bfc2f8c:mixing.F:66` `ETA2sum, ETA2mean, SigWaveHeight)`<br>`FUNWAVE-TVD/src/mixing.F:61` `CALL CALCULATE_MEAN`<br>`bfc2f8c:mixing.F:150` `CALL PREVIEW_MEAN`<br>`FUNWAVE-TVD/src/mixing.F:259` `CALL PREVIEW_MEAN`<br>`bfc2f8c:wavemaker.F:286` `CALL WK_WAVEMAKER_IRREGULAR_WAVE &`<br>`bfc2f8c:wavemaker.F:287` `(Nfreq,Ntheta,delta_WK,DEP_WK,FreqPeak,FreqMax,FreqMin,GammaTMA,Hmo,ThetaPeak, &`<br>`bfc2f8c:wavemaker.F:288` `sigma_theta,rlamda_ir,beta_gen_ir,D_gen_ir,Phase_ir,Width_WK,omgn_ir,&`<br>`bfc2f8c:wavemaker.F:289` `Periodic,DY,Nglob)`<br>`bfc2f8c:wavemaker.F:317` `CALL CALCULATE_TMA_Cm_Sm &`<br>`bfc2f8c:wavemaker.F:318` `(Nfreq,Ntheta,DEP_Ser,FreqPeak,FreqMax,FreqMin,GammaTMA,Hmo,ThetaPeak, &`<br>`bfc2f8c:wavemaker.F:319` `sigma_theta)`<br>`FUNWAVE-TVD/src/wavemaker.F:383` `CALL WK_WAVEMAKER_IRREGULAR_WAVE &`<br>`FUNWAVE-TVD/src/wavemaker.F:384` `(Nfreq,Ntheta,delta_WK,DEP_WK,FreqPeak,FreqMax,FreqMin,GammaTMA,Hmo,ThetaPeak, &`<br>`FUNWAVE-TVD/src/wavemaker.F:385` `sigma_theta,rlamda_ir,beta_gen_ir,D_gen_ir,Phase_ir,Width_WK,omgn_ir,&`<br>`FUNWAVE-TVD/src/wavemaker.F:386` `Periodic,DY,Nglob)`<br>`FUNWAVE-TVD/src/wavemaker.F:422` `CALL CALCULATE_TMA_Cm_Sm &`<br>`FUNWAVE-TVD/src/wavemaker.F:423` `(Nfreq,Ntheta,DEP_Ser,FreqPeak,FreqMax,FreqMin,GammaTMA,Hmo,ThetaPeak, &`<br>`FUNWAVE-TVD/src/wavemaker.F:424` `sigma_theta)`<br>`bfc2f8c:io.F:80` `CALL PREVIEW`<br>`FUNWAVE-TVD/src/io.F:99` `CALL PREVIEW`<br>`bfc2f8c:misc.F:349` `CALL PREVIEW`<br>`FUNWAVE-TVD/src/misc.F:420` `CALL PREVIEW`<br>`bfc2f8c:io.F:1321` `call PutFile(TMP_NAME,Eta)`<br>`FUNWAVE-TVD/src/io.F:4373` `call PutFile(TMP_NAME,Eta)`<br>`bfc2f8c:io.F:1458` `call PutFile(TMP_NAME,Umean)`<br>`FUNWAVE-TVD/src/io.F:4668` `call PutFile(TMP_NAME,Umean)`<br>funwave_code_analysis.pdf p.12: `FUNWAVE_TVD`, `INITIALIZATION`, `wall_time_secs`, `CALCULATE_FRICTION_SPONGE`, `CALCULATE_DIFFUSION_SPONGE`, `WAVEMAKER_INITIALIZATION`, `CALCULATE_TMA_Cm_Sm`, `WK_WAVEMAKER_IRREGULAR_WAVE`, `OUTPUT`, `CHECK_BLOWUP`, `PREVIEW`, `CALCULATE_MEAN`, `PREVIEW_MEAN`, `PutFile`, `real`<br>`2e72b18:main.F:177` `CALL WALL_TIME_SECS(tbegin)`<br>eccc669 2016-12-31 change tend and tbegin calculation based on fortran 90/95 standard<br>`eccc669:src/main.F:178` `if(myid == 0) tbegin = MPI_Wtime( )`<br>`eccc669:src/main.F:180` `CALL CPU_TIME(tbegin)`<br>`eccc669:src/main.F:284` `if(myid.eq.0) tend = MPI_Wtime( )`<br>`eccc669:src/main.F:286` `CALL CPU_TIME (tend)`<br>`FUNWAVE-TVD/src/main.F:278` `if(myid == 0) tbegin = MPI_Wtime( )`<br>`FUNWAVE-TVD/src/main.F:280` `CALL CPU_TIME(tbegin)` | A 판 차이 | `eccc669`(2016-12-31). 현재 주 프로그램의 시간 측정 호출은 병렬의 MPI_Wtime과 직렬의 CPU_TIME이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] [10-18 전수 검증 정정] |
| aux-docs-build:FN1-377 | Figure 14 REAL 소속 | funwave_code_analysis.pdf p.13: `real`과 `wall_time_secs`를 `misc.F` 상자에 표시; “where a program unit is defined” | `FUNWAVE-TVD/src/misc.F:451` `msecs = real(walltime(8))`<br>`FUNWAVE-TVD/src/misc.F:443` `SUBROUTINE wall_time_secs(tcurrent)`<br>`FUNWAVE-TVD/src/misc.F:444` `IMPLICIT NONE`<br>funwave_code_analysis.pdf p.12 Figure 12: wall_time_secs에서 real로 향하는 직접 호출선 | F 표기 차이 | Figure 14는 REAL을 misc.F 상자에 묶지만 해당 파일의 실제 코드는 wall_time_secs에서 REAL 형변환을 사용한다. 캡션의 정의 위치라는 표현은 내장 함수 REAL의 경우에 정확하지 않다. 사용 관계와 파일 묶음을 구분하는 F이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| aux-docs-build:FN1-558 | files.txt의 시간 측정 호출 | `FUNWAVE-TVD/src/files.txt:10` `call WALL_TIME_SECS`<br>`FUNWAVE-TVD/src/files.txt:30` `CALL WALL_TIME_SECS(tend)` | `bfc2f8c:main.F:177` `CALL WALL_TIME_SECS(tbegin)`<br>`bfc2f8c:main.F:279` `call WALL_TIME_SECS(tend)`<br>`FUNWAVE-TVD/src/main.F:278` `if(myid == 0) tbegin = MPI_Wtime( )`<br>`FUNWAVE-TVD/src/main.F:280` `CALL CPU_TIME(tbegin)`<br>`FUNWAVE-TVD/src/main.F:560` `if(myid.eq.0) tend = MPI_Wtime( )`<br>`FUNWAVE-TVD/src/main.F:562` `CALL CPU_TIME (tend)`<br>`FUNWAVE-TVD/src/files.txt:10` `call WALL_TIME_SECS`<br>`FUNWAVE-TVD/src/files.txt:30` `CALL WALL_TIME_SECS(tend)`<br>cab9425 2016-03-02 first add to repository<br>`cab9425:main.F:170` `CALL WALL_TIME_SECS(tbegin)`<br>`cab9425:main.F:264` `call WALL_TIME_SECS(tend)`<br>eccc669 2016-12-31 change tend and tbegin calculation based on fortran 90/95 standard<br>`eccc669:src/main.F:178` `if(myid == 0) tbegin = MPI_Wtime( )`<br>`eccc669:src/main.F:180` `CALL CPU_TIME(tbegin)`<br>`eccc669:src/main.F:284` `if(myid.eq.0) tend = MPI_Wtime( )`<br>`eccc669:src/main.F:286` `CALL CPU_TIME (tend)` | A 판 차이 | `eccc669`(2016-12-31). 현재 시간 측정은 병렬에서 MPI_Wtime을 사용한다. 직렬에서는 CPU_TIME을 사용한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] [10-18 전수 검증 정정] |
| aux-docs-build:FN1-903 | 정적 지표의 집계 범위 | `05fdbedb:models/FUNWAVE/source-analysis/funwave-code-graph.md:13`(반영 전 노트 줄) `33,760줄` `218 subroutine` `15 module` `414 USE` `1338 CALL` | `FUNWAVE-TVD/src/main.F:45` `Program FUNWAVE_TVD`; `FUNWAVE-TVD/src/fluxes_21v.F:53` `SUBROUTINE FLUXES`; 집계 정규식: `^\s*SUBROUTINE\b`, `^\s*USE\b`, `^\s*MODULE\s+(?!PROCEDURE\b)\w+`, `^\s*CALL\b`(대소문자 무시). | C 문서 누락 | b4c322e의 `src/*.F` 38개를 대상으로 LF 바이트는 33,760개이다. 논리 행은 33,761개이다. 대소문자를 무시한 행 시작 `SUBROUTINE`은 218개이고 `USE`는 414개이다. `MODULE PROCEDURE`를 제외한 모듈 선언은 15개이다. 행 시작 `CALL`은 1,301개이다. 노트의 `1338 CALL`에는 집계 규칙이 없으므로 호출 수의 정의를 보완한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 표본 정정] |
| callflow:RF-046 | 코드 그래프의 HLL·WAVE_SPEED 연결 | `05fdbedb:models/FUNWAVE/source-analysis/funwave-code-graph.md:34`(반영 전 노트 줄) `FLUX_AT_INTERFACE_HLL ─ HLL ─ WAVE_SPEED`; `funwave_code_analysis.pdf p.12 Figure 13` | `FUNWAVE-TVD/src/fluxes.F:64` `CALL WAVE_SPEED(Mloc,Nloc,Mloc1,Nloc1,UxL,UxR,VyL,VyR,HxL,HxR,HyL,HyR, &`<br>`SxL,SxR,SyL,SyR)`; `FUNWAVE-TVD/src/fluxes.F:110` `CALL FLUX_AT_INTERFACE_HLL`; `FUNWAVE-TVD/src/fluxes.F:154` `CALL HLL(Mloc1,Nloc,SxL,SxR,PL,PR,EtaRxL,EtaRxR,P)`; `FUNWAVE-TVD/src/main.F:383` `CALL Cal_Dispersion`; `FUNWAVE-TVD/src/main.F:414` `CALL ESTIMATE_HUV(ISTAGE)`; `FUNWAVE-TVD/src/etauv_solver.F:348` `CALL GET_Eta_U_V_HU_HV` | B 문서 오기 | FLUXES는 재구성 뒤에 WAVE_SPEED를 호출한다. 그 뒤 수치 플럭스 루틴과 BOUNDARY_CONDITION을 호출한다. HLL에서 WAVE_SPEED로 가는 호출선은 없다. 2.1의 중간 호출자 생략은 RF-023과 같다. [10-18 결론 검증 보완] [10-18 git 이력 판정] [10-18 표본 정정] |
