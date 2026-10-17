# FUNWAVE 노트 전수 검증 6

대상 노트는 `models/FUNWAVE/source-analysis/funwave-dispersion-solver.md`다.
검증 기준은 작업 시작 시 `git diff -U0 HEAD -- models/FUNWAVE/source-analysis/funwave-dispersion-solver.md`의 추가 줄이다.
이 diff에서 대상 줄 211개를 셌다.
대상에는 frontmatter 2줄과 차이 표 데이터 164줄이 포함된다.
대상 줄 번호는 수정 전 노트를 기준으로 한다.
대상 구간은 5–6, 14, 19–26, 28, 41–45, 48–52, 62–64, 77–86, 89–264행이다.

## 진행 기록

- 2026-10-18: DELIVERABLE을 먼저 만들었다.
- 노트 상태: 대조 완료.
- 차이 표 164행의 분류와 결론 문장을 보고서의 최종 결론 표와 대조했다.
- E 행 56개의 강도는 최종 결론 표와 일치했다.
- FT1-256의 GPU 경로 다섯 곳을 정정했다.
- FN1-013·016·018·019·020·022의 `cab9425:src/` 인용 13곳을 루트 경로로 정정했다.
- 본문 81행의 소비 대상을 `nu_break`로 명시했다.
- 본문 81행에 소비 조건과 호출 순서의 직접 인용을 보탰다.

## 대조 결과

| 노트 | 대조한 대상 줄 | 정정 줄 | 보완 줄 | 실제 변경 줄 | 미해결 항목 |
|---|---:|---:|---:|---:|---:|
| [funwave-dispersion-solver.md](../../../models/FUNWAVE/source-analysis/funwave-dispersion-solver.md) | 211 | 8 | 1 | 8 | 0 |

정정·보완 수는 각각 표시를 붙인 물리적 줄 수다.
81행은 정정과 보완을 함께 포함한다.
대상 줄 211개는 frontmatter 2줄, 본문 35줄, 차이 표 데이터 164줄, 빈 줄 7줄, 절 제목 1줄, 표 머리·구분선 2줄로 구성된다.
이 수는 작업 시작 diff의 추가 줄에서 셌다.
수정 후에도 노트의 물리적 줄 수는 264개다.

차이 표의 분류는 A 4개, B 8개, C 18개, D 8개, E 56개, F 70개다.
이 수는 노트 101–264행의 결론 칸에서 셌다.
모든 행의 분류와 결론 문장은 해당 보고서의 최종 결론 표와 일치한다.
E 행 56개의 강도도 최종 보고서와 일치한다.
A 행의 커밋 HASH와 날짜는 외부 TVD 저장소의 해당 커밋 원문과 일치한다.
각 보고서 끝의 전수 검증 기록과 최종 집계를 우선 기준으로 적용했다.

기계 확인 후보는 사용자 목록의 중복을 포함해 63건이다.
63건 모두 인용 대상 판본이나 설명 문맥을 잘못 적용한 오판이다.
정정한 8줄의 오류는 아래 정정·보완 목록에 별도로 기록했다.

## 대상 줄 대조 기록

| 노트 줄 | 줄 수 | 대조 근거와 판정 |
|---|---:|---|
| 5–6 | 2 | 기존 `verification_method` 부분은 HEAD와 같다. 추가한 recovery 반영일은 `FUNWAVE-notes-apply-5.md`와 맞는다. |
| 14 | 1 | GPU 설명은 gpu-vs-tvd §4 FG1-802 수정안과 맞는다. RK 호출 순서는 TVD `main.F:380–414`와 맞는다. |
| 19–26, 28 | 9 | v21-manual §4 FV1-552·553과 aux-docs-build FN1-921을 적용했다. TVD `dispersion.F:295–499`의 분기·계수와 PDF 식을 대조했다. |
| 41–45 | 5 | TVD `etauv_solver.F:402–411`의 최소깊이·세 대각 계수·우변과 맞는다. FV1-554와 theory-numerics K03의 수정 근거를 확인했다. |
| 48–52 | 5 | TVD `etauv_solver.F:570–589`의 젖은 셀 조건·HU/HV·총속도 제한과 맞는다. `io.F:2898–2900`의 입력 누락값은 3.0이다. |
| 62–64 | 3 | GPU `mod_cuda.F:17`의 기본값은 `TriSolver=0`이다. `etauv_solver_gpu.F:127–158,565–595,910–942`의 분기·전치·Thomas·cuSPARSE 호출을 대조했다. MGPU의 MPI 계수 전달도 원문과 맞는다. |
| 77–86 | 10 | callflow §3.1·§6 및 TVD `init.F:534–535`, `dispersion.F:114`, `main.F:380–487`, `sources.F:196–198`을 대조했다. 81행의 소비 대상과 인용을 고쳤다. 빈 줄도 대상에 포함했다. |
| 89–100 | 12 | 판본·보고서 연결·표 머리·빈 줄을 대조했다. 커밋 날짜와 문서 표지는 맞는다. 표의 두 원문 칸에 대한 설명도 gpu-vs-tvd의 구성과 맞는다. |
| 101–154 | 54 | theory-numerics §5의 해당 54개 ID를 대조했다. FT1-256의 GPU 경로를 고쳤다. |
| 155–156 | 2 | inputs §5의 FI1-154·292를 대조했다. Froude 권고 범위와 누락 기본값을 구분했다. COUPLING 북쪽 분기의 도달 불능 조건과 수치 영향 조건은 원문과 맞는다. |
| 157–191 | 35 | v21-manual §5의 해당 35개 ID를 대조했다. 2.1 PDF와 현재·과거 TVD 원문의 조건·부호·계수를 확인했다. |
| 192–216 | 25 | aux-docs-build §5의 해당 25개 ID를 대조했다. 최초 커밋의 인용 경로를 고쳤다. 지정 빌드 파일 39개와 네 문서·TeX의 선택지 누락 근거도 확인했다. |
| 217–261 | 45 | gpu-vs-tvd §5의 해당 45개 ID를 대조했다. 현재 GPU와 TVD 분기 기준 `e42e17d`의 국소 식·전처리 조건을 확인했다. 로컬 cuSPARSE 수정 네 곳은 공개 `7f892ba`와 대조했다. |
| 262–264 | 3 | callflow §8의 RF-007·015·017을 대조했다. RK 계수, CAL_DISPERSION 호출, 삼중대각 루틴 이름은 원문과 맞는다. |

위 표의 줄 수 합계는 211개다.
차이 표의 ID 집합은 `FUNWAVE-note-job-5.tsv` 및 `FUNWAVE-notes-apply-5.md`의 이 노트 배정 164개와 같다.
HEAD에서 삭제·교체된 기존 7줄도 해당 보고서 수정안과 대조했다.
삭제·교체 근거는 frontmatter 반영 기록, FG1-802, FV1-552·553·554·555다.

## 정정·보완 목록

아래의 노트 이름은 `models/FUNWAVE/source-analysis/funwave-dispersion-solver.md`를 뜻한다.
현재 코드 경로는 `models/FUNWAVE/raw/source_code/`를 기준으로 한다.
과거 커밋은 `_staging/recovery/extract/FUNWAVE/external/tvd`의 `git show` 원문을 기준으로 한다.

| 종류 | 노트:줄 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| 정정 | funwave-dispersion-solver.md:81 | `**nu_break·AGE_BREAKING**: SourceTerms가 이번 WAVE_BREAKING보다 먼저 읽는다.` → `SourceTerms`의 소비 대상을 `nu_break`로 명시했다. | TVD `src/sources.F:198`은 `nu_vis = nu_break`다. 이 파일에는 AGE_BREAKING 소비가 없다. [callflow §6](FUNWAVE-callflow.md#6-기존-노트-대조와-수정안)의 2973행 수정안은 `SourceTerms의 nu_break 지연`을 보강하도록 적었다. |
| 보완 | funwave-dispersion-solver.md:81 | 기존 소비·생산 위치 인용 → 소비 조건 `IF(VISCOSITY_BREAKING .OR. WAVEMAKER_VIS)THEN`과 `src/sources.F:196–198`, `src/main.F:404,435`를 보탰다. | TVD `src/main.F:404`의 `CALL SourceTerms`가 435행의 `CALL WAVE_BREAKING`보다 앞선다. `src/sources.F:196`은 본문에 보탠 조건문과 같다. |
| 정정 | funwave-dispersion-solver.md:153 | FT1-256의 `FUNWAVE-TVD/src/io.F:2490–2521`, `main.F:305–311`, `moment_gpu.F:552–575`, `init.F:555`, `moment_gpu.F:579–586` → 다섯 인용의 접두사를 `FUNWAVE-GPU`로 바꿨다. | [theory-numerics FT1-256](../compare/funwave-theory-numerics-vs-code.md#5-차이-결론)은 GPU 원문을 인용한다. GPU `src/init.F:555`가 Beta_2를 대입한다. GPU `src/moment_gpu.F:552–575`는 CARTESIAN 비선형 보정이다. 579–586행은 ZALPHA 재대입이다. |
| 정정 | funwave-dispersion-solver.md:192 | FN1-013의 `cab9425:src/init.F:497` → `cab9425:init.F:497`. | 최초 커밋은 루트 `init.F:497`에 `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`를 둔다. `src/init.F`는 이 커밋에 없다. |
| 정정 | funwave-dispersion-solver.md:193 | FN1-016의 `cab9425:src/dispersion.F:379`, `:380`, `cab9425:src/init.F:497` → 세 인용에서 `src/`를 제거했다. | 루트 `dispersion.F:379–380`은 ken1의 Beta_2·Beta_2 제곱 항이다. 루트 `init.F:497`은 Beta_2 대입이다. |
| 정정 | funwave-dispersion-solver.md:194 | FN1-018의 `cab9425:src/dispersion.F:388`, `:413`, `cab9425:src/init.F:497` → 세 인용에서 `src/`를 제거했다. | 루트 `dispersion.F:388`은 U1pp의 대입이다. 413행은 U2의 대입이다. 인용한 식은 각 줄과 같다. |
| 정정 | funwave-dispersion-solver.md:195 | FN1-019의 `cab9425:src/dispersion.F:457`, `:462`, `cab9425:src/init.F:497` → 세 인용에서 `src/`를 제거했다. | 루트 `dispersion.F:457`은 U3의 대입이다. 462행은 V3의 대입이다. 외적의 음·양 부호가 노트와 같다. |
| 정정 | funwave-dispersion-solver.md:196 | FN1-020의 `cab9425:src/dispersion.F:441`, `cab9425:src/init.F:497` → 두 인용에서 `src/`를 제거했다. | 루트 `dispersion.F:441–442`는 omega_1의 두 항이다. Beta_2 배율을 포함한 인용은 원문과 같다. |
| 정정 | funwave-dispersion-solver.md:197 | FN1-022의 `cab9425:src/init.F:497` → `cab9425:init.F:497`. | 최초 커밋의 루트 `init.F:497`에 인용한 Beta_2 대입이 있다. |

192–197행에서 경로를 바로잡은 인용은 합계 13곳이다.
[aux-docs-build §1](../compare/funwave-aux-docs-build-vs-code.md#1-요약)의 21행은 초기 커밋의 실제 객체가 저장소 루트에 있음을 명시한다.
실제 `git show cab9425:init.F`와 `git show cab9425:dispersion.F`로 줄 번호와 식을 확인했다.
각 정정 줄에 `[10-18 전수 검증 정정]`을 붙였다.
81행에는 `[10-18 전수 검증 보완]`도 붙였다.
차이 표의 표시는 결론 문장 칸 끝에 붙였다.

## 기계 확인 후보 판정

번호는 사용자 목록의 순서를 따른다.
같은 후보의 반복도 별도 행으로 기록했다.
후보의 경로에는 노트에 적힌 커밋 HASH를 복원했다.
26–63번은 지정 커밋의 원문 줄과 후보 문자열을 직접 대조했다.

| 번호 | 노트 줄·행 ID | 후보의 완전한 원문 위치·문자열 | 판정 |
|---|---|---|---|
| 01 | 101 · FT1-021 | `7b93138:src/init.F:488` · `도 같은` | 오판. 인용 뒤 조사다. 원문은 `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`다. |
| 02 | 102 · FT1-024 | `7b93138:src/init.F:488` · `도 같은` | 오판. 인용 뒤 조사다. 원문은 `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`다. |
| 03 | 103 · FT1-028 | `7b93138:src/init.F:488` · `도 같은` | 오판. 인용 뒤 조사다. 원문은 `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`다. |
| 04 | 104 · FT1-029 | `7b93138:src/init.F:488` · `도 같은` | 오판. 인용 뒤 조사다. 원문은 `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`다. |
| 05 | 105 · FT1-031 | `7b93138:src/init.F:488` · `도 같은` | 오판. 인용 뒤 조사다. 원문은 `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`다. |
| 06 | 106 · FT1-034 | `7b93138:src/init.F:488` · `도 같은` | 오판. 인용 뒤 조사다. 원문은 `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`다. |
| 07 | 111 · FT1-051 | `7b93138:src/dispersion.F:318–348` · `과` | 오판. 두 원문 범위를 연결하는 조사다. 해당 범위의 U1p·V1p와 SPH_EXTRA_DISP를 확인했다. |
| 08 | 112 · FT1-052 | `7b93138:src/dispersion.F:318–348` · `과` | 오판. 두 원문 범위를 연결하는 조사다. 해당 범위의 U1p·V1p와 SPH_EXTRA_DISP를 확인했다. |
| 09 | 113 · FT1-062 | `7b93138:src/dispersion.F:318–348` · `과` | 오판. 두 원문 범위를 연결하는 조사다. 해당 범위의 U1p·V1p와 SPH_EXTRA_DISP를 확인했다. |
| 10 | 114 · FT1-064 | `7b93138:src/dispersion.F:318–348` · `과` | 오판. 두 원문 범위를 연결하는 조사다. 해당 범위의 U1p·V1p와 SPH_EXTRA_DISP를 확인했다. |
| 11 | 115 · FT1-068 | `7b93138:src/dispersion.F:318–348` · `과` | 오판. 두 원문 범위를 연결하는 조사다. 해당 범위의 U1p·V1p와 SPH_EXTRA_DISP를 확인했다. |
| 12 | 116 · FT1-069 | `7b93138:src/dispersion.F:318–348` · `과` | 오판. 두 원문 범위를 연결하는 조사다. 해당 범위의 U1p·V1p와 SPH_EXTRA_DISP를 확인했다. |
| 13 | 117 · FT1-070 | `7b93138:src/dispersion.F:318–348` · `과` | 오판. 두 원문 범위를 연결하는 조사다. 해당 범위의 U1p·V1p와 SPH_EXTRA_DISP를 확인했다. |
| 14 | 118 · FT1-071 | `7b93138:src/dispersion.F:318–348` · `과` | 오판. 두 원문 범위를 연결하는 조사다. 해당 범위의 U1p·V1p와 SPH_EXTRA_DISP를 확인했다. |
| 15 | 119 · FT1-074 | `7b93138:src/dispersion.F:318–348` · `과` | 오판. 두 원문 범위를 연결하는 조사다. 해당 범위의 U1p·V1p와 SPH_EXTRA_DISP를 확인했다. |
| 16 | 120 · FT1-075 | `7b93138:src/dispersion.F:318–348` · `과` | 오판. 두 원문 범위를 연결하는 조사다. 해당 범위의 U1p·V1p와 SPH_EXTRA_DISP를 확인했다. |
| 17 | 121 · FT1-076 | `7b93138:src/dispersion.F:318–348` · `과` | 오판. 두 원문 범위를 연결하는 조사다. 해당 범위의 U1p·V1p와 SPH_EXTRA_DISP를 확인했다. |
| 18 | 122 · FT1-077 | `7b93138:src/dispersion.F:318–348` · `과` | 오판. 두 원문 범위를 연결하는 조사다. 해당 범위의 U1p·V1p와 SPH_EXTRA_DISP를 확인했다. |
| 19 | 123 · FT1-079 | `7b93138:src/sources.F:362–378` · `에도 곡률 질량 소스의 곱이 없다.` | 오판. 원문의 발산 곱에는 곡률 질량 소스가 없다. 원문에 대한 설명이다. |
| 20 | 124 · FT1-081 | `7b93138:src/dispersion.F:318–348` · `과` | 오판. 두 원문 범위를 연결하는 조사다. 해당 범위의 U1p·V1p와 SPH_EXTRA_DISP를 확인했다. |
| 21 | 125 · FT1-082 | `7b93138:src/dispersion.F:318–348` · `과` | 오판. 두 원문 범위를 연결하는 조사다. 해당 범위의 U1p·V1p와 SPH_EXTRA_DISP를 확인했다. |
| 22 | 126 · FT1-083 | `7b93138:src/sources.F:362–378` · `에도 곡률 질량 소스의 곱이 없다.` | 오판. 원문의 발산 곱에는 곡률 질량 소스가 없다. 원문에 대한 설명이다. |
| 23 | 127 · FT1-084 | `7b93138:src/sources.F:362–378` · `에도 곡률 질량 소스의 곱이 없다.` | 오판. 원문의 발산 곱에는 곡률 질량 소스가 없다. 원문에 대한 설명이다. |
| 24 | 129 · FT1-121 | `7b93138:src/mod_param.F:87–88` · `의 선언과` | 오판. 선언과 주 루프를 연결하는 조사다. 원문은 `ITER_NUM = 2`와 `ERRORi = 0.0001_SP`다. |
| 25 | 154 · FT1-279 | `HEAD의 funwave-dispersion-solver.md:18` · `**선형 분산항 V4**(:296-329 ...)` | 오판. 수정 전 노트의 인용이다. 읽기 전용 diff의 삭제 줄과 일치한다. 현재 본문의 정정은 19–23행에 있다. |
| 26 | 201 · FN1-207 | `80ac086:src/init.F:847` · `Ubar=HU+gamma1*U1p*H` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 27 | 201 · FN1-207 | `80ac086:src/init.F:848` · `Vbar=HV+gamma1*V1p*H` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 28 | 201 · FN1-207 | `7948152:src/init.F:847` · `Ubar=HU+gamma1*U1p*H` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 29 | 201 · FN1-207 | `7948152:src/init.F:848` · `Vbar=HV+gamma1*V1p*H` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 30 | 201 · FN1-207 | `7948152:src/etauv_solver.F:316` · `tmp4=Ubar(I,J)*MASK(I,J)/Max(H(I,J),MinDepthFrc)  &` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 31 | 201 · FN1-207 | `7948152:src/etauv_solver.F:317` · `+ Gamma1*MASK9(I,J)*( -b1/2.0_SP*dep*dep*Vxy(I,J)-b2*dep*DVxy(I,J))` | 오판. 지정 커밋의 부호와 계수가 일치한다. |
| 32 | 202 · FN1-311 | `b0c72bf:src/etauv_solver.F:273` · `SUBROUTINE GET_Eta_U_V_HU_HV` | 오판. 지정 커밋의 선언 줄과 일치한다. |
| 33 | 206 · FN1-343 | `37e5749:src/init.F:492` · `a1=ZERO` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 34 | 207 · FN1-344 | `37e5749:src/init.F:493` · `a2=ZERO` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 35 | 218 · FG1-019 | `e42e17d:src/etauv_solver.F:73` · `DXg=DX` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 36 | 218 · FG1-019 | `e42e17d:src/etauv_solver.F:74` · `DYg=DY` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 37 | 218 · FG1-019 | `e42e17d:src/etauv_solver.F:77` · `DXg=DX(1,1)` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 38 | 218 · FG1-019 | `e42e17d:src/etauv_solver.F:78` · `DYg=DY(1,1)` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 39 | 220 · FG1-215 | `e42e17d:src/etauv_solver.F:225` · `Eta(I,J)=ALPHA(ISTEP)*Eta0(I,J)+BETA(ISTEP)*(Eta(I,J)+DT*R1(I,J))` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 40 | 220 · FG1-215 | `e42e17d:src/etauv_solver.F:256` · `Ubar(I,J)=ALPHA(ISTEP)*Ubar0(I,J)+BETA(ISTEP)*(Ubar(I,J)+DT*R2(I,J))` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 41 | 221 · FG1-216 | `e42e17d:src/etauv_solver.F:301` · `SUBROUTINE GET_Eta_U_V_HU_HV` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 42 | 221 · FG1-216 | `e42e17d:src/etauv_solver.F:337` · `dep=Max(Depth(I,J),MinDepthFrc)` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 43 | 222 · FG1-218 | `e42e17d:src/etauv_solver.F:301` · `SUBROUTINE GET_Eta_U_V_HU_HV` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 44 | 222 · FG1-218 | `e42e17d:src/etauv_solver.F:437` · `tmp1=Gamma1*MASK9(I,J)*(b1/2.0_SP/DY/DY*dep*dep + b2/DY/DY*depl*dep)` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 45 | 222 · FG1-218 | `e42e17d:src/etauv_solver.F:424` · `tmp1=Gamma1*MASK9(I,J)*(b1/2.0_SP/DY/DY*dep*dep + b2/DY/DY*depl*dep) &` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 46 | 229 · FG1-227 | `e42e17d:src/etauv_solver.F:301` · `SUBROUTINE GET_Eta_U_V_HU_HV` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 47 | 229 · FG1-227 | `e42e17d:src/etauv_solver.F:513` · `HU(I,J)=Max(H(I,J),MinDepthFrc)*U(I,J)` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 48 | 234 · FG1-293 | `e42e17d:src/dispersion.F:292` · `U4(I,J)=(1.0_SP/3.0_SP-Beta_1+0.5_SP*Beta_1*Beta_1)*DEPTH(I,J)*DEPTH(I,J)*(Uxx(I` | 오판. 잘린 후보 문자열은 지정 커밋 해당 줄의 앞부분과 일치한다. |
| 49 | 234 · FG1-293 | `e42e17d:src/dispersion.F:308` · `ken1 = ( 1.0_SP/6.0_SP - Beta_1 + Beta_1*Beta_1 )*rh*reta*Beta_2   &` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 50 | 234 · FG1-293 | `e42e17d:src/dispersion.F:333` · `U1p(I,J)=0.5_SP*(1.0_SP-Beta_1)*(1.0_SP-Beta_1)  &` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 51 | 235 · FG1-294 | `e42e17d:src/dispersion.F:406` · `U1pp(I,J)=-reta*Beta_2*ETAx(I,J)*Beta_2*(Utx(I,J)+Vty(I,J)) - 0.5_SP*reta*reta*B` | 오판. 잘린 후보 문자열은 지정 커밋 해당 줄의 앞부분과 일치한다. |
| 52 | 238 · FG1-407 | `e42e17d:src/dispersion.F:292` · `U4(I,J)=(1.0_SP/3.0_SP-Beta_1+0.5_SP*Beta_1*Beta_1)*DEPTH(I,J)*DEPTH(I,J)*(Uxx(I` | 오판. 잘린 후보 문자열은 지정 커밋 해당 줄의 앞부분과 일치한다. |
| 53 | 239 · FG1-408 | `e42e17d:src/dispersion.F:308` · `ken1 = ( 1.0_SP/6.0_SP - Beta_1 + Beta_1*Beta_1 )*rh*reta*Beta_2   &` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 54 | 240 · FG1-409 | `e42e17d:src/dispersion.F:333` · `U1p(I,J)=0.5_SP*(1.0_SP-Beta_1)*(1.0_SP-Beta_1)  &` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 55 | 241 · FG1-410 | `e42e17d:src/dispersion.F:406` · `U1pp(I,J)=-reta*Beta_2*ETAx(I,J)*Beta_2*(Utx(I,J)+Vty(I,J)) - 0.5_SP*reta*reta*B` | 오판. 잘린 후보 문자열은 지정 커밋 해당 줄의 앞부분과 일치한다. |
| 56 | 242 · FG1-411 | `e42e17d:src/dispersion.F:422` · `ken1=(Beta_1-1.0_SP)*(rhx+ETAx(I,J))*Beta_2` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 57 | 243 · FG1-412 | `e42e17d:src/dispersion.F:455` · `omega_0=Vx(I,J)-Uy(I,J)` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 58 | 244 · FG1-413 | `e42e17d:src/dispersion.F:470` · `ken1=((Beta_1-1.0_SP/2.0_SP)*(reta+rh)*Beta_2)` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 59 | 245 · FG1-443 | `e42e17d:src/etauv_solver.F:256` · `Ubar(I,J)=ALPHA(ISTEP)*Ubar0(I,J)+BETA(ISTEP)*(Ubar(I,J)+DT*R2(I,J))` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 60 | 246 · FG1-444 | `e42e17d:src/etauv_solver.F:337` · `dep=Max(Depth(I,J),MinDepthFrc)` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 61 | 247 · FG1-445 | `e42e17d:src/etauv_solver.F:437` · `tmp1=Gamma1*MASK9(I,J)*(b1/2.0_SP/DY/DY*dep*dep + b2/DY/DY*depl*dep)` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 62 | 248 · FG1-446 | `e42e17d:src/etauv_solver.F:424` · `tmp1=Gamma1*MASK9(I,J)*(b1/2.0_SP/DY/DY*dep*dep + b2/DY/DY*depl*dep) &` | 오판. 지정 커밋의 해당 줄과 일치한다. |
| 63 | 253 · FG1-451 | `e42e17d:src/etauv_solver.F:513` · `HU(I,J)=Max(H(I,J),MinDepthFrc)*U(I,J)` | 오판. 지정 커밋의 해당 줄과 일치한다. |

## 최종 확인

식과 숫자는 지정된 300 dpi 쪽 이미지에서 판정했다.
직접 대조한 이미지 쪽은 다음과 같다.

| 문서 | 이미지 쪽 |
|---|---|
| funwave_tvd_3.0 | 1, 15, 16, 18, 19, 20, 21, 22, 25, 41, 81, 86, 87, 88, 89 |
| funwave_tvd_2.1_manual | 13, 14, 16, 17, 23, 24, 25, 32, 40 |
| Intro-to-FUNWAVE-CHL-TN | 1, 5, 6, 7, 8, 12, 13, 16 |
| funwave_code_analysis | 3, 7 |

현재·과거 코드 인용의 실제 경로와 줄 번호를 확인했다.
인용 바로 뒤에 코드가 없는 설명 문장도 해당 원문 범위와 대조했다.
조건·부정·수량·단위·부호·전처리 플래그에서 남은 불일치는 없다.
노트의 상대 링크 155개는 노트 위치를 기준으로 모두 실제 파일을 가리킨다.
이 링크들은 서로 다른 파일 13개를 가리킨다.
노트에 `/home/firesinger/`와 `[[`는 없다.
작업 한계를 나타내는 금지 문장은 없다.
대상 노트에 Mermaid 블록은 없다.
85행의 흐름도 링크는 최종 렌더 확인을 마친 callflow §4.2를 가리킨다.
기존 71–75행의 일반 코드 블록은 추가·수정 줄에 포함되지 않는다.

## 최종 집계

대상 노트 1개를 완료했다.
대상 211줄을 모두 대조했다.
정정은 8줄이다.
인용 보완은 정정 줄과 중복되는 1줄이다.
기계 확인 후보 63건을 모두 판정했다.
미해결 항목은 0개다.
