# FUNWAVE 노트 전수 대조 9

검증일: 2026-10-18.

대상은 사용자 지정 노트 네 개다. 기존 노트는 작업 시작 시 `git diff -U0 HEAD -- <노트>`의 추가 줄을 대조한다. 새 노트 두 개는 frontmatter와 빈 줄을 포함한 전체 줄을 대조한다. 줄 수와 정정 위치는 작업 시작 시 노트를 기준으로 기록한다.

현재 코드, 과거 커밋 원문, 문서 쪽별 판독 기록과 쪽 이미지, 지정 보고서의 최종 검증 기록을 근거로 사용한다. 정정과 인용 보완은 노트별로 구분하여 기록한다. 기계 확인 후보는 사용자 목록의 중복도 각각 기록한다.

## 진행 기록

네 노트의 대상 줄 대조를 완료했다. 노트별 결과와 최종 집계를 아래에 기록한다.


## 1. funwave-aux-docs-build-differences.md — 완료

- 노트: [funwave-aux-docs-build-differences.md](../../../models/FUNWAVE/manual-notes/funwave-aux-docs-build-differences.md).
- 대조한 줄 수: 86줄. 대상은 작업 시작 시 전체 1–86행이다.
- 정정 수: 1줄. 보완 수: 0줄. 집계는 이번 검증 태그를 붙인 고유 노트 줄을 기준으로 한다.
- 1–31행의 frontmatter·범위·판본·표 머리글을 반영 기록과 AD3의 판본 기록에 대조했다. 빈 줄과 구분선도 대상에 포함했다.
- 32–86행의 차이 표 55행을 v21-manual §5와 aux-docs-build §5의 최종 결론에 대조했다. 분류와 결론 문장은 모두 일치한다.
- 현재 원문 인용 627개 고유 조합과 과거 원문 인용 69개 고유 조합을 경로·줄·인용문으로 대조했다. 과거 원문은 공개 사본의 `git show`로 열었다. FN1-366의 루트 `2e72b18:fluxes.F:52,67,70`도 별도로 대조했다.
- FN1-509–534의 26개 Makefile에서 누락 모듈과 파일 줄 수를 직접 확인했다. A행 26개의 HASH·날짜는 AD3의 해당 판정과 일치한다.
- 2.1 매뉴얼 p.34와 code_analysis p.8·11·14의 판독 기록 및 300 dpi 이미지를 대조했다. FV1-780–803의 기계별 설정 누락과 FN1-366·372의 그림 캡션 오기를 확인했다.
- GPU_CHECK·SAMPLES·TMP의 현재 조건부 유무를 TVD·GPU 소스에서 검색했다. FN1-625와 FN1-632의 B 분류는 최종 검증 기록과 일치한다.
- 상대 파일 링크 3개는 모두 존재한다. Mermaid 블록은 없다. 사용자 금지 경로·위키링크·한계 문장은 없다.

### 정정 목록

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| funwave-aux-docs-build-differences.md:85 (FN1-625) | `bfc2f8c:src/samples.F:45` | `bfc2f8c:samples.F:45` | TVD 공개 사본 `git show bfc2f8c:samples.F`의 45행은 `# if defined(SAMPLES)`다. 이 커밋에는 `src/samples.F`가 없다. AD3 §1도 2016-11-03 이전 루트 경로를 명시한다. 결론 문장 끝에 정정 태그를 붙였다. |

### 기계 확인 후보 판정

- K07 — main.F:151 후보 1: 오판이다. 노트 62행(FN1-513)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K08 — main.F:151 후보 2: 오판이다. 노트 63행(FN1-514)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K09 — main.F:151 후보 3: 오판이다. 노트 64행(FN1-515)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K10 — main.F:151 후보 4: 오판이다. 노트 65행(FN1-516)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K11 — main.F:151 후보 5: 오판이다. 노트 66행(FN1-517)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K12 — main.F:151 후보 6: 오판이다. 노트 67행(FN1-518)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K13 — main.F:151 후보 7: 오판이다. 노트 68행(FN1-519)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K14 — main.F:151 후보 8: 오판이다. 노트 69행(FN1-520)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K15 — main.F:151 후보 9: 오판이다. 노트 70행(FN1-521)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K16 — main.F:151 후보 10: 오판이다. 노트 71행(FN1-522)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K17 — main.F:151 후보 11: 오판이다. 노트 72행(FN1-523)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K18 — main.F:151 후보 12: 오판이다. 노트 73행(FN1-524)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K19 — main.F:151 후보 13: 오판이다. 노트 74행(FN1-525)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K20 — main.F:151 후보 14: 오판이다. 노트 75행(FN1-526)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K21 — main.F:151 후보 15: 오판이다. 노트 76행(FN1-527)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K22 — main.F:151 후보 16: 오판이다. 노트 77행(FN1-528)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K23 — main.F:151 후보 17: 오판이다. 노트 78행(FN1-529)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K24 — main.F:151 후보 18: 오판이다. 노트 79행(FN1-530)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K25 — main.F:151 후보 19: 오판이다. 노트 80행(FN1-531)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K26 — main.F:151 후보 20: 오판이다. 노트 81행(FN1-532)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K27 — main.F:151 후보 21: 오판이다. 노트 82행(FN1-533)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K28 — main.F:151 후보 22: 오판이다. 노트 83행(FN1-534)은 `334bb51:src/main.F:151`을 가리킨다. 해당 과거 원문은 `USE TIDE_MODULE`이다. 현재 원문의 159행과 구분되어 있으므로 유지했다.
- K29 — samples.F:45: 실제 오류다. 노트 85행의 과거 경로를 `bfc2f8c:samples.F:45`로 고쳤다. 조건문과 B 분류는 유지했다.
- K30 — mod_vessel.F:347 후보 1: 오판이다. 노트 86행의 현재 GPU 원문은 `# elif defined (TMP)`다.
- K31 — mod_vessel.F:347 후보 2: 오판이다. 노트 86행의 TVD 과거 `e42e17d:src/mod_vessel.F:347`은 `# elif defined (TMP)`다. 같은 행 안의 반복 인용도 일치한다.
- K32 — mod_vessel.F:347 후보 3: 오판이다. 노트 86행의 GPU 과거 `7f892ba:src/mod_vessel.F:347`은 `# elif defined (TMP)`다.
- K33 — mod_vessel.F:353: 오판이다. 노트 86행의 TVD 과거 `5ab3402:src/mod_vessel.F:353`은 `IF(VesselType == 1.OR.VesselType == 2) THEN`이다.

이 노트의 미해결 항목은 없다.

## 2. funwave-gpu-cuda-port.md — 완료

- 노트: [funwave-gpu-cuda-port.md](../../../models/FUNWAVE/source-analysis/funwave-gpu-cuda-port.md).
- 대조한 줄 수: 83줄. 작업 시작 시 `git diff -U0 HEAD`의 추가 줄을 셌다.
- 대상 범위: 7–8, 20–21, 35, 39–40, 54, 135, 138, 171, 182, 199, 215, 221, 232, 238–293, 295–305행이다.
- 정정 수: 2줄. 보완 수: 0줄.
- frontmatter의 반영일과 반영 방법은 apply-8 기록과 일치한다. 본문 변경은 aux-docs-build §4의 FN1-923·924와 gpu-vs-tvd §4의 FG1-904·878·602·849·482 수정안에 대조했다.
- MGPU 플래그, shared 연령 적재 범위, MASK9 곱, 연속 host 버퍼 교환, 남북 주기 경계, Thomas·cuSPARSE 분기를 현재 원문에서 열었다. `Makefile_cuda.orig`와 현재 Makefile의 실제 차이는 FC·OPT 두 줄이다.
- 247–292행의 차이 표 46행은 최종 보고서의 분류와 결론에 일치한다. 백틱과 표의 이스케이프 표기는 같은 문장으로 판정했다.
- 현재 직접 인용 184개 고유 조합과 과거 직접 인용 23개 고유 조합을 대조했다. 이어지는 인용문을 포함한 1,292개 구간도 해당 파일의 인용 위치 이후 원문에 대조했다.
- E행 14개의 강도는 최종 결론과 git E3·callflow 판정에 일치한다. 비지원 TriSolver=1과 미호출 periodic helper의 중간·약한 강도를 보존했다.
- 2.1 매뉴얼 p.26·34의 판독 기록과 쪽 이미지에서 GPU 빌드 조건 누락을 확인했다. callflow §6의 수정안과 끝의 렌더 확인·최종 기록도 대조했다.
- 상대 파일 링크 28개는 모두 존재한다. Mermaid 블록은 없다. 사용자 금지 경로·위키링크·한계 문장은 없다.

### 정정 목록

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| funwave-gpu-cuda-port.md:283 (FG1-864) | `FUNWAVE-GPU/src/sponge.F:100` | `FUNWAVE-GPU/src/sponge.F:101` | 100행은 빈 줄이다. 인용한 `Uin2D(I,J) =Uin2D(I,J)+Cm_u(I,J,KK)*COS(pi/2.0_SP+Segma_Ser(KK)*TIME+Phase_Ser(KK)) &`는 101행이다. 결론 문장 끝에 정정 태그를 붙였다. |
| funwave-gpu-cuda-port.md:284 (FG1-865) | `FUNWAVE-GPU/src/wavemaker.F:2404` | `FUNWAVE-GPU/src/wavemaker.F:2405` | 2404행은 빈 줄이다. 인용한 `Uin2D(I,J) =Uin2D(I,J)+Cm_u(I,J,KK)*COS(pi/2.0_SP+Segma_Ser(KK)*RTIME+Phase_Ser(KK)) &`는 2405행이다. 결론 문장 끝에 정정 태그를 붙였다. |

### 기계 확인 후보 판정

- K01 — `5594984:src/etauv_solver_gpu.F:957`: 오판이다. 노트 254행은 GPU 과거 커밋을 가리킨다. 해당 원문 957행은 `subroutine periodic_triDy_cusparse`다. 현재 로컬 파일에서는 같은 선언이 963행이다. 두 판본의 인용을 유지했다.

이 노트의 미해결 항목은 없다.

## 3. funwave-gpu-source.md — 완료

- 노트: [funwave-gpu-source.md](../../../models/FUNWAVE/source-analysis/funwave-gpu-source.md).
- 대조한 줄 수: 86줄. 작업 시작 시 `git diff -U0 HEAD`의 추가 줄을 셌다.
- 대상 범위: 5–6, 14–18, 27, 30, 36, 43–44, 49–51, 54, 57, 61–77, 84–85, 87, 90–91, 96–142행이다.
- 정정 수: 2줄. 보완 수: 2줄.
- frontmatter와 판독 범위는 apply-9 및 gpu-vs-tvd §4의 FG1-900·901에 대조했다. 현재 GPU `src/*.F` 41개와 TVD와의 공통 파일 29개를 직접 셌다. 401커밋 비교의 기준과 최근접 커밋은 보고서 §1.1의 집계에 대조했다.
- 본문 수정 줄은 theory-numerics FT1-287, gpu-vs-tvd §4의 해당 수정안, callflow §6의 수정안에 대조했다. CudaMemUse의 두 STOP 조건, 정수 조파 코드와 배열 할당, RK 갱신, 경계 flux, shared 연령, 평균 초기화, 직접 스펀지, 장치 출력과 CPU MPI 경로를 현재 원문에서 열었다.
- 108–142행의 차이 표 35행은 최종 보고서의 분류와 결론에 일치한다. 경로 접두어 확장, 백틱, A행 앞의 커밋 정보는 내용 차이와 구분했다.
- 현재 직접 인용 120개 고유 조합과 과거 직접 인용 23개 고유 조합을 대조했다. 이어지는 인용문도 해당 파일 원문에 대조했다. 자동 추출기의 FT1-287 `의 AB_OUTPUT 블록;` 후보는 인용문 경계 오인으로 판정했다. 실제 AB_OUTPUT 블록은 TVD dispersion.F:386–395에 있다.
- A행 RF-002의 `38b74cc 2020-02-17`과 RF-033의 `36738b1 2019-07-02`는 AD1 판정과 일치한다. E행 8개의 강도는 최종 결론과 E3 판정에 일치한다.
- RF-002의 문서 흐름은 3.0 p.33 판독 기록과 쪽 이미지에 대조했다. 외부 원문 보고서의 Beta_2 원인은 FG1-600의 V2 속도 선택 원인과 구분했다.
- 상대 파일 링크 18개는 모두 존재한다. Mermaid 블록은 없다. 사용자 금지 경로·위키링크·한계 문장은 없다.

### 정정·보완 목록

| 노트:줄 | 구분 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| funwave-gpu-source.md:36 | 보완 | Eta·Ubar·Vbar 갱신에 `etauv_solver_gpu.F:1358`만 인용 | `etauv_solver_gpu.F:1358,1387,1409` 인용 | GPU 원문의 1358행은 Eta_d를 갱신한다. 1387행은 Ubar_d를 갱신한다. 1409행은 Vbar_d를 갱신한다. 줄 끝에 보완 태그를 붙였다. |
| funwave-gpu-source.md:49 | 보완 | 반복 할당·버퍼 공유·정밀도·주기 helper에 `FG1-608·609·616` 인용 | `FG1-608·609·610·616` 인용 | gpu-vs-tvd §2.5와 §5의 FG1-610이 주기 helper의 반복 밖 경계 대입을 다룬다. GPU etauv_solver_gpu.F:963 이후 구현과 driver의 153–158행 호출을 대조했다. 줄 끝에 보완 태그를 붙였다. |
| funwave-gpu-source.md:62 | 정정 | 초기 교환·습윤건조 커널·MASK9 커널·최종 교환을 조건 없이 열거 | 초기·최종 교환에 `MGPU` 정의 조건을 명시했다. MASK9 커널에 `VISCOSITY_BREAKING` 거짓 조건을 명시했다. | GPU masks_gpu.F:132–135·172–175의 `# if defined (MGPU)`와 157–170행의 `IF(VISCOSITY_BREAKING)THEN`·`ELSE`를 대조했다. 실행 순서와 RK 전 호출 위치는 유지했다. 줄 끝에 정정 태그를 붙였다. |
| funwave-gpu-source.md:134 (FG1-760) | 정정 | `FUNWAVE-GPU/src/io.F:2904` | `FUNWAVE-GPU/src/io.F:2905` | 2904행은 빈 줄이다. 2905행은 `IF(VISCOSITY_BREAKING) SHOW_BREAKING = .TRUE.`다. 결론 문장 끝에 정정 태그를 붙였다. |

### 기계 확인 후보 판정

- K02 — 옛 노트 13행 `비-gpu 파일은 CPU판 공유`: 오판이다. 현재 108행 FT1-287은 수정 전 문장을 인용한다. 읽기 전용 git diff의 HEAD 문맥에서 옛 13행을 확인했다. 현재 본문 15행은 두 판본의 차이를 설명한다.
- K03 — 옛 노트 39행 `cusparseSgtsv2StridedBatch_bufferSizeExt`: 오판이다. 현재 139행 RF-038은 수정 전 문장을 인용한다. git diff의 HEAD 문맥 39행과 현재 GPU etauv_solver_gpu.F:910의 호출이 모두 일치한다.
- K04 — 옛 노트 22행 `CudaMemUse`: 오판이다. 현재 140행 RF-039은 수정 전 문장을 인용한다. git diff의 HEAD 문맥 22행을 확인했다. 현재 본문 27행은 init_gpu.F:64–87의 두 STOP 경로를 명시한다.
- K05 — 옛 노트 13행 `비-gpu 파일은 CPU판 공유` 중복 후보: 오판이다. 현재 141행 RF-047은 수정 전 문장을 인용한다. 옛 13행 원문과 callflow의 수정안이 일치한다.
- K06 — 옛 노트 62행 `halo 교환`: 오판이다. 현재 142행 RF-048은 수정 전 표를 인용한다. git diff의 HEAD 문맥 62행을 확인했다. 현재 본문 84·90행은 CPU의 PARALLEL MPI 경로를 명시한다.

이 노트의 미해결 항목은 없다.

## 4. funwave-gpu-vs-tvd-differences.md — 완료

- 노트: [funwave-gpu-vs-tvd-differences.md](../../../models/FUNWAVE/source-analysis/funwave-gpu-vs-tvd-differences.md).
- 대조한 줄 수: 49줄. 대상은 작업 시작 시 전체 1–49행이다.
- 정정 수: 2줄. 보완 수: 0줄.
- 1–33행의 frontmatter·범위·판본·표 머리글은 apply-7, 배정표, 보고서 판본 기록에 대조했다. 빈 줄과 구분선도 대상에 포함했다.
- 34–49행의 차이 표 16행은 theory-numerics·aux-docs-build·gpu-vs-tvd·callflow의 최종 분류와 결론에 일치한다. E행 5개의 강도는 git E1·E3 및 각 최종 결론에 일치한다. A행은 없다.
- 현재 직접 인용은 정정 전 76개 고유 조합이었다. 과거 직접 인용은 8개 고유 조합이었다. 이어지는 인용문 522개 구간도 해당 파일 원문에 대조했다. FN1-704의 보고서 표 안 `||`는 표 구분자로 오인한 검사기 문제였다. 조건문 원문은 노트와 일치한다.
- 3.0 p.86 식 (112)와 p.89 식 (120)을 판독 기록과 300 dpi 쪽 이미지에 대조했다. 괄호·계수·미분 첨자·부호가 일치한다. GPU의 첫 tV와 CPU의 첫 U 차이는 별도 코드 원문에서 확인했다.
- 정밀도 설명은 3.0 p.32·34, 2.1 p.26·34, Intro-TN p.9의 판독 기록과 쪽 이미지에 대조했다. 재구성 흐름은 code_analysis p.13·14의 판독 기록과 쪽 이미지에 대조했다.
- TORSVIK의 조건부 2곳과 선박 입력을 원문에서 열었다. 지정 빌드 파일은 TVD 루트 Makefile 4개, src Makefile 2개, GNUMake 파일 27개, GPU src Makefile 6개로 총 39개다. 이 집합과 네 문서·tex 판독 기록에 TORSVIK 선택지가 없다.
- 정밀도 선언, MIXING 첨자, PGI 난수 분기, 깊이 PHI_COLL 인자, 질량 보정, Gamma3_d, FILTERING, 재구성 선택과 종료 station 호출을 원문에서 확인했다. 현재 코드와 과거 커밋의 인용 위치를 분리해서 판정했다.
- 상대 파일 링크 5개는 모두 존재한다. Mermaid 블록은 없다. 사용자 금지 경로·위키링크·한계 문장은 없다.

### 정정 목록

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| funwave-gpu-vs-tvd-differences.md:41 (FG1-485) | 같은 행 뒤쪽의 `FUNWAVE-GPU/src/init.F:674` | `FUNWAVE-GPU/src/init.F:675` | 현재 GPU init.F:674는 빈 줄이다. `VTYPE=1`은 675행이다. 앞쪽의 올바른 675행 인용은 유지했다. 결론 문장 끝에 정정 태그를 붙였다. |
| funwave-gpu-vs-tvd-differences.md:42 (FG1-487) | `FUNWAVE-GPU/src/masks.F:186` | `FUNWAVE-GPU/src/masks.F:187` | 현재 GPU masks.F:186은 빈 줄이다. `! calculate deta`는 187행이다. 결론 문장 끝에 정정 태그를 붙였다. |

### 기계 확인 후보 판정

- K34 — dispersion.F:445: 오판이다. 노트 38행의 `e42e17d:src/dispersion.F:445`는 `V2(I,J)=ken1*(U(I,J)*HUxxHVxy+V(I,J)*HUxyHVyy) &`다. 현재 GPU의 CPU 사본 445행도 같다. 현재 TVD의 461행과 구분한다.
- K35 — sources.F:309 후보 1: 오판이다. 노트 39행의 `e42e17d:src/sources.F:309`는 `SourceX(I,J) = SourceX(I,J) + 1.0_SP/DX*( &`다.
- K36 — wavemaker.F:279: 오판이다. 노트 40행의 `e42e17d:src/wavemaker.F:279`는 `DO I=1,NumDir`다. 현재 GPU 279행의 `DO J=1,NumFreq`와 다른 판본이다.
- K37 — init.F:675: 제시된 675행 후보는 오판이다. 현재 GPU와 `e42e17d:src/init.F:675`는 모두 `VTYPE=1`이다. 같은 노트 41행 뒤쪽의 별도 674행 인용은 실제 오류여서 675행으로 고쳤다.
- K38 — masks.F:161: 오판이다. 노트 42행의 `e42e17d:src/masks.F:161`은 `# if defined (CHECK_MASS_CONSERVATION)`이다. 현재 GPU의 CPU 사본 161행도 같다.
- K39 — sources.F:309 후보 2: 오판이다. 노트 43행의 `e42e17d:src/sources.F:309`도 같은 `SourceX(I,J) = SourceX(I,J) + 1.0_SP/DX*( &`를 인용한다.

이 노트의 미해결 항목은 없다.

## 최종 집계

| 노트 | 대조한 줄 수 | 정정 수 | 보완 수 | 상태 |
|---|---:|---:|---:|---|
| funwave-aux-docs-build-differences.md | 86 | 1 | 0 | 완료 |
| funwave-gpu-cuda-port.md | 83 | 2 | 0 | 완료 |
| funwave-gpu-source.md | 86 | 2 | 2 | 완료 |
| funwave-gpu-vs-tvd-differences.md | 49 | 2 | 0 | 완료 |
| 합계 | 304 | 7 | 2 | 완료 |

- 줄 수는 각 노트 절에 기록한 작업 시작 시 대상 범위의 합계다. 정정·보완 수는 이번 검증 태그를 붙인 고유 줄의 합계다. 노트의 줄 추가·삭제는 없다.
- 차이 표 152행의 분류와 결론 문장은 최종 보고서와 일치한다. 행 수는 위 노트 순서로 55·46·35·16행이다. A행의 HASH·날짜와 E행의 판정 강도도 해당 최종 판정에 대조했다.
- 기계 확인 후보는 중복을 포함하여 39건이다. K29의 과거 파일 경로 1건을 정정했다. 나머지 38건은 원문 판본 또는 과거 노트 인용을 구분하면 일치한다. K01–K39가 각각 한 번씩 기록되었음을 확인했다.
- 정정 후 현재 코드의 직접 인용과 보고서 결론을 다시 검사했다. 불일치는 없다. 상대 파일 링크 54개와 절 앵커 31개가 모두 유효하다. 링크 수는 위 노트 순서로 3·28·18·5개다. 앵커 수는 0·17·14·0개다.
- 변경 기록의 9줄만 작업 시작 시 내용으로 되돌린 메모리상의 파일 해시가 시작 시 해시와 일치한다. 이 검증에서 대상 노트에 가한 변경은 기록한 9줄뿐이다. 정정·보완 태그의 위치도 확인했다.
- 네 노트에는 Mermaid 블록이 없다. 사용자 지정 금지 경로·위키링크·한계 문장은 없다. 읽기 전용 `git diff --check`도 통과했다.

대상 304줄의 대조를 완료했다. 미해결 항목은 없다.
