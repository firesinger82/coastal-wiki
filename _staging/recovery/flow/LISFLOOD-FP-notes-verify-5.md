# LISFLOOD-FP 노트 전수 대조 5

검증일: 2026-10-21.
대상은 사용자 지정 노트 두 파일이다.
기존 노트의 대상은 작업 시작 시 `git diff -U0 HEAD -- models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md`의 추가 줄이다.
새 노트의 대상은 작업 시작 시 파일 전체 줄이다.
빈 줄과 frontmatter 줄을 줄 수에 포함한다.
정정 수와 보완 수는 이번 검증에서 해당 표식을 붙인 최종 노트 줄 수로 센다.

## 대상 확정

| 노트 | 대조할 줄 수 | 작업 시작 시 대상 줄 | 상태 |
|---|---:|---|---|
| `models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md` | 172 | 7–8, 12, 18–20, 25–39, 46, 51–54, 63, 72–85, 88–93, 96–107, 143–153, 186–225, 233–239, 242–261, 264–274, 286–287, 290–301, 317–320, 331–333, 337, 339–340 | 완료 |
| `models/LISFLOOD-FP/source-analysis/lisflood-fp-cpu-gpu-differences.md` | 46 | 1–46 | 완료 |

줄 수는 위 명령의 추가 줄과 새 파일의 물리적 줄을 각각 세었다.

## 기계 확인 후보 판정

사용자가 제시한 기계 확인 불일치 후보는 없다.

## IO 본문 대조 완료

노트: [lisflood-fp-io-boundary.md](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md).
대조한 대상은 작업 시작 시 추가 줄 172줄이다.
정정은 최종 노트의 정정 표식 기준 28줄이다.
보완은 최종 노트의 보완 표식 기준 4줄이다.
정정·보완 목록은 원래 대상 위치별로 묶은 21건이다.
복원·분리로 늘어난 줄은 18줄이다.
최종 노트는 358줄이다.
이 수는 작업 시작 시 340줄과 이번 패치 결과를 대조하여 확인했다.

### 대상 줄별 대조 범위

아래 줄 번호는 작업 시작 시 노트의 줄 번호이다.
각 범위에서는 대상 확정 표에 적힌 추가 줄만 센다.
원문 경로의 기준은 사용자 지정 현재 소스 루트이다.
보고서 이름의 기준은 `_staging/recovery/compare/`이다.

| 대상 범위 | 대조한 줄 수 | 원문과 최종 근거 | 판정 |
|---|---:|---|---|
| 7–20 | 6 | `bf804e23` 노트 frontmatter; `LISFLOOD-FP-notes-apply-1.md`; `VersionHistory.h:16–34`; 8.3 패키지 `README.md:19–24` | 기존 판독 이력·반영 날짜·범위·기준 판·상대 링크가 대응한다. |
| 25–54 | 20 | `pars.cpp:17–117,1020–1038,1091–1138`; `lisflood.cpp:284–320`; LI1-356·357, LN1-193 | 길이 제한과 처리 순서가 대응한다. 생략된 토큰 읽기 설명을 복원했다. |
| 63, 72–85 | 15 | `pars.cpp:232–247,300–323,410–436,582–647,973–982`; `lisflood.cpp:419–457,773–805`; `lisflood.h:388`; LI1-358·360, RF-004 | Qfile의 선언·대입 두 검색 결과를 확인했다. 충돌 검사 종료 분기의 도달 불가와 해법 우선순위가 대응한다. |
| 88–107 | 18 | `pars.cpp:283–402,895,965–1086`; `lisflood2/lis2_output.cpp:154–159`; `rain/rain.tpp:20,65–74`; `v8.2:pars.cpp:1079–1085`; LI1-136·359·361, LB1-380 | 출력·강우 키워드와 verbose 조건이 대응한다. 8.2의 CUDA 전용 가드와 8.3의 CUDA·Metal 가드를 구분했다. |
| 143–153 | 11 | `input.cpp:1848–1918,1952–2117`; `boundary.cpp:279–283,1422–1474`; LV1-143·268, LB1-400 | 이름 누락 경로와 끝 값 유지가 대응한다. 미참조 자료 폐기 설명을 복원했다. |
| 186–225 | 40 | `chkpnt.cpp:34–314`; `iterateq.cpp:203–205,212,309–320,449–477`; `lisflood.cpp:323–338,379–380,419–457,773–810`; `lisflood2/lisflood_processing.cpp:1536–1572,2092–2122`; `utility.cpp:43–50`; `lisflood2/sgm_fast.cpp:4600–4611`; 비균일 ACC 체크포인트 읽기·쓰기; RF-021, LV1-191·194·266, LI2-349 | 빈 파일·형식 판·숫자 판·치수 검사를 구분했다. 경계 유량과 체적 누계를 구분했다. 최종 저장 후보의 강함과 RESULT_CHECK 예외가 대응한다. |
| 233–239 | 7 | `input.cpp:2126–2139`; `infevap.cpp:51–83`; `iterateq.cpp:141–156`; LB1-401, LT1-314 | 비SGC 경로와 cell_evap 재사용 후보의 강함이 대응한다. 보간·단위·제거 체적 설명을 복원했다. |
| 242–261 | 20 | `infevap.cpp:91–124`; `rain/rain.tpp:1–184`; `rain/rain.h:93–114`; `rain/rain_stub.tpp:5–11`; U·N 강우 reader·커널·시간 반복; CUDA FV1·FV2 강우 코드; DOCX p.37 쪽 이미지; LG2-074–078·096 | 강우량·시간 간격·장부·매크로 조건이 대응한다. LG2-075는 중간이다. LG2-074·076·077은 강함이다. 같은 원점 조건의 한정을 유지했다. |
| 264–274 | 11 | `infevap.cpp:131–296,310–391`; `lisflood.cpp:138,174`; LT1-305, DOCX 보고서 §4.2 | 라우팅 비활성화 조건을 고쳤다. 이동 시간과 이동 비율을 복원했다. 비교 연산자와 수면차 제한은 원문과 같다. |
| 286–301 | 14 | `output.cpp:39–147,506–625`; `input.cpp:18–32,1241–1256`; `lisflood.h:75–97`; LI2-343–345, LV1-171 | ASCII 이중 헤더와 binary 자료 길이 후보가 대응한다. 첫 두 정수를 열·행 수로 고쳤다. Windows 후보의 중간 강도를 유지했다. |
| 317–320 | 4 | `VersionHistory.h:109`; `lisflood.cpp:756–768`; LV1-216 | 5.9.23의 기본 표시용 DEM 출력과 현재 SGCz 출력이 대응한다. |
| 331–340 | 6 | 공통·비균일 ACC writer; `pars.cpp:1020`; `infevap.cpp:24–39,64–79`; `lisflood2/file_tool.cpp:764–788`; LI1-136 | driver별 저장 상태 인용을 보완했다. 키워드 경고·수심 문턱·ASCII 대체 조건이 대응한다. |

대조 범위 표의 줄 수 합계는 172줄이다.
각 후보의 분류와 강도는 최종 결론 TSV 및 해당 conclusion-verify 행과 대조했다.
Claude 최종 조정의 LI2-352·LI1-369·LN1-127은 이 본문의 대상 후보가 아니다.
외부 출처 파일 끝 절의 LI2-203·LB1-235도 이 본문의 대상 후보가 아니다.
본문 교체의 근거는 각 보고서 §4와 callflow §6을 `bf804e23`의 교체 전 문장에 대조했다.
삭제를 뒷받침하지 않는 기존 설명은 아래 목록처럼 복원했다.

### 정정·보완 목록

아래 위치는 최종 노트의 줄 번호이다.
전후 문장에서 기존 작업 표식은 생략한다.
원래 대상 위치도 함께 적어 줄 이동을 추적한다.

| 최종 노트:줄 / 원래 대상 줄 | 구분 | 전 | 후 | 근거 원문과 판정 |
|---|---|---|---|---|
| `lisflood-fp-io-boundary.md:34,35` / 34 | 정정 | `ReadParamFile`은 행 단위로 읽는다. (`pars.cpp:1090–1138`) | `ReadParamFile`은 `LINE_BUFFER_LEN` 크기의 버퍼로 행 단위로 읽는다. (`pars.cpp:1093,1110`)  <br>첫 토큰은 `sscanf(line_buffer, "%79s ", param_name);`으로 읽는다. (`pars.cpp:1123–1124`) | pars.cpp:1093,1110,1123–1124; lisflood-par-vs-code.md:568. 수정안은 키워드 최대 길이를 고치도록 했다. 교체 과정에서 빠진 버퍼와 첫 토큰 읽기 설명을 복원했다. |
| `lisflood-fp-io-boundary.md:39` / 38 | 보완 | `#`·빈 줄·CRLF-only 줄은 건너뛴다. (`pars.cpp:1118–1120`) | `#`·빈 줄·CRLF-only 줄은 건너뛴다. (`pars.cpp:1119–1121`) | pars.cpp:1119–1121. 건너뛰기 조건과 continue를 함께 인용했다. |
| `lisflood-fp-io-boundary.md:40` / 39 | 정정 | 파서는 `CheckParam`으로 디스패치한다. (`pars.cpp:1138`) | 값 포인터는 `param_value_ptr = line_buffer + param_name_len;`으로 설정한다. (`pars.cpp:1136`) <br>파서는 `CheckParam`으로 디스패치한다. (`pars.cpp:1138`) | pars.cpp:1136; bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:24. 본문 교체에서 빠진 값 포인터 설정을 원문 대입식으로 복원했다. |
| `lisflood-fp-io-boundary.md:147,148` / 144 | 정정 | 참조되지 않은 bdy 자료의 경고에는 verbose 조건이 없다. (`input.cpp:2065–2069`) | 참조되지 않은 bdy 자료의 경고에는 verbose 조건이 없다. (`input.cpp:2065–2069`) <br>참조되지 않은 시계열 자료는 `FreeTimeSeries(*timeSeries);`로 해제한다. (`input.cpp:2065–2069`) <br>해당 자료는 `BCptr->allTimeSeries.pop_back();`으로 목록에서 제외한다. (`input.cpp:2071`) | input.cpp:2065–2074; bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:97; lisflood-bridge-docx-vs-code.md:592. 경고 설명을 고치면서 빠진 미참조 자료 폐기 설명을 복원했다. |
| `lisflood-fp-io-boundary.md:192` / 188 | 정정 | 체크포인트 형식 판이 다르면 그 파일의 상태 읽기를 건너뛰고 새 계산으로 간다. (`chkpnt.cpp:98–109`) | 빈 체크포인트 파일은 상태 읽기를 건너뛰고 새 계산으로 간다. (`chkpnt.cpp:94–100`) <br>체크포인트 형식 판이 다르면 그 파일의 상태 읽기를 건너뛰고 새 계산으로 간다. (`chkpnt.cpp:98–109`) | chkpnt.cpp:94–100; bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:130; lisflood-docx-manual-vs-code.md:452. 판 불일치 처리를 나누면서 빠진 빈 파일의 처리 결과를 복원했다. |
| `lisflood-fp-io-boundary.md:198,199` / 193 | 정정 | 공통 writer는 시간·반복·시간 간격·경계 누적량·격자 기하·하도 세그먼트 상태를 기록한다. (`chkpnt.cpp:211–314`) | 공통 writer는 시간·반복·시간 간격·경계 유량·격자 기하를 기록한다. (`chkpnt.cpp:232–281`; `boundary.cpp:1330,1401–1406`)  <br>하도 세그먼트 상태는 `if(Statesptr->ChannelPresent==ON)`일 때 기록한다. (`chkpnt.cpp:288–308`) | chkpnt.cpp:262–267,288–308; boundary.cpp:1330,1401–1406. 저장되는 Qin·Qout은 유량이다. 체적 누계 VolInMT·VolOutMT는 이 writer의 저장 목록에 없다. 하도 상태의 저장 조건을 명시했다. |
| `lisflood-fp-io-boundary.md:206` / 200 | 정정 | 읽기(`ReadCheckpoint`, chkpnt.cpp:34): 기본 체크파일(`checkpointfilename`)을 먼저 시도 — 존재하면 중단된 run 의미. 없으면 `loadcheck` 대체파일(chkpnt.cpp:48-78). 기본파일이 대체보다 우선(chkpnt.cpp:71-75). | `ReadCheckpoint`는 기본 파일 `checkpointfilename`을 먼저 연다. 기본 파일을 열지 못하고 `Statesptr->checkfile == ON`이면 `loadCheckpointFilename`을 시도한다. 기본 파일을 열면 대체 파일보다 우선한다. (`chkpnt.cpp:48–78`) | chkpnt.cpp:48–78,223; lisflood.cpp:809–810; lisflood-par-vs-code.md:574. 기본 파일의 존재를 중단된 실행의 증거로 단정한 설명을 제거했다. 정상 종료에도 main이 같은 파일을 저장한다. |
| `lisflood-fp-io-boundary.md:207` / 201 | 정정 | 현재 기본 체크포인트 경로는 `dirroot`가 포함된 `resrootname`에 `.chkpnt`를 붙여 만든다. (`lisflood.cpp:332,379–380`) | 현재 기본 체크포인트 경로는 `resrootname`에 `.chkpnt`를 붙여 만든다. `dirroot`를 지정한 경우 `resrootname`에 그 디렉터리를 포함한다. (`lisflood.cpp:323–338,379–380`) | lisflood.cpp:323–338,379–380. dirroot를 지정하지 않은 분기는 res_prefix만 사용한다. 디렉터리를 항상 포함한다는 표현을 조건부로 고쳤다. |
| `lisflood-fp-io-boundary.md:209` / 203 | 보완 | 값이 없으면 1시간을 대입한다. (`pars.cpp:97–100,563–567`) | 값이 없으면 1시간을 대입한다. (`pars.cpp:97–100,563–567`; `iterateq.cpp:318`) | pars.cpp:563; iterateq.cpp:318. 기본 숫자 1.0을 1시간으로 해석하는 근거인 checkfreq * 3600을 보탰다. |
| `lisflood-fp-io-boundary.md:239` / 233 | 정정 | 입력 증발율은 공간 균일하다. (`infevap.cpp:56`; `input.cpp:2126–2139`) | 고전 증발은 `evap_rate=InterpolateTimeSeries(Arrptr->evap,Solverptr->t);`로 공간 균일 시변율을 구한다. (`infevap.cpp:56`) | infevap.cpp:56; bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:142. 균일율 설명을 유지하면서 빠진 시계열 보간을 복원했다. |
| `lisflood-fp-io-boundary.md:241` / 234 | 정정 | 고전 증발은 `if(Arrptr->ChanMask[i+j*Parptr->xsz]==-1)` 안에서 `if(h0>Solverptr->DepthThresh)`를 만족하는 셀에 적용한다. (`infevap.cpp:64–79`) | 고전 증발은 `if(Arrptr->ChanMask[i+j*Parptr->xsz]==-1)` 안에서 `if(h0>Solverptr->DepthThresh)`를 만족하는 셀에 적용한다. (`infevap.cpp:64–79`) <br>고전 증발은 `Parptr->EvapTotalLoss+=cell_evap*Parptr->dA;`로 제거 체적을 누적한다. (`infevap.cpp:79`) | infevap.cpp:79; bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:142; lisflood-bridge-docx-vs-code.md:593. cell_evap 재사용 후보를 추가하면서 빠진 증발 체적 누적 설명을 복원했다. |
| `lisflood-fp-io-boundary.md:242` / 235 | 정정 | 환산식은 `Arrptr->evap->value[i] /= (1000 * 24 * 3600);`이다. (`input.cpp:2126–2139`) | 입력 증발율은 mm/day에서 m/s로 환산한다. 환산식은 `Arrptr->evap->value[i] /= (1000 * 24 * 3600);`이다. (`input.cpp:2137–2139`) | input.cpp:2137–2139; bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:142. 식만 남기면서 빠진 입력·계산 단위를 복원했다. |
| `lisflood-fp-io-boundary.md:251,252,253,254` / 243 | 정정 | 직접 호출 조건은 `Statesptr->rainfall == ON && Statesptr->routing == OFF`이다. (`iterateq.cpp:155–156`) | 직접 호출 조건은 `Statesptr->rainfall == ON && Statesptr->routing == OFF`이다. (`iterateq.cpp:155–156`) <br>고전 `Rainfall`은 `rain_rate=InterpolateTimeSeries(Arrptr->rain,Solverptr->t);`로 공간 균일 시변율을 구한다. (`infevap.cpp:96`) <br>고전 `Rainfall`의 셀 루프에는 OpenMP 병렬 지시문이 있다. (`infevap.cpp:99`) <br>`LoadRain`은 `Arrptr->rain->value[i] /= (1000 * 3600);`으로 입력 강우율을 mm/hr에서 m/s로 환산한다. (`input.cpp:2157–2159`) <br>`LoadEvap`과 `LoadRain`의 시계열 읽기는 첫 줄을 건너뛴다. (`input.cpp:1869–1872,2134,2154`) | infevap.cpp:96,99; input.cpp:1869–1872,2134,2154–2159; bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:145; lisflood-cpu-gpu-acc-adaptive.md:784–788. CPU Rainfall 범위를 명시하면서 빠진 보간·병렬 루프·단위 환산·첫 줄 건너뛰기를 복원했다. |
| `lisflood-fp-io-boundary.md:258` / 247 | 보완 | GPU ACC 강우 갱신은 CPU `RainTotalLoss` 장부를 누적하지 않는다. (`cuda/cuda_rain.cu:98–114`; `cuda/acc_nugrid/rain.cu:56–78`; `cuda/acc_nugrid/rain_uniform.cu:24–41`) | GPU ACC 강우 갱신은 CPU `RainTotalLoss` 장부를 누적하지 않는다. (`cuda/cuda_rain.cu:98–114`; `cuda/acc_nugrid/rain.cu:56–78`; `cuda/acc_nugrid/rain_uniform.cu:24–41`; `cuda/acc/cuda_acc_solver.cu:154–165`) | cuda/acc/cuda_acc_solver.cu:154–165; LISFLOOD-FP-conclusion-verify-LG2.md:130 (LG2-078). GPU ACC 전체 강우 설명에 균일 격자 ACC의 균일 강우 구현 인용도 보탰다. |
| `lisflood-fp-io-boundary.md:263` / 252 | 정정 | GPU 균일 강우는 CPU의 강우 직후 음수 제한을 생략한다. (`infevap.cpp:105–124`; `cuda/acc_nugrid/rain_uniform.cu:24–41`; `cuda/acc/cuda_acc_solver.cu:154–165`) | 균일·비균일 GPU ACC의 균일 강우는 CPU의 강우 직후 음수 제한을 생략한다. (`infevap.cpp:105–124`; `cuda/acc_nugrid/rain_uniform.cu:24–41`; `cuda/acc/cuda_acc_solver.cu:154–165`) | cuda/acc/cuda_acc_solver.cu:154–165; cuda/acc_nugrid/rain_uniform.cu:24–41; LISFLOOD-FP-conclusion-verify-LG2.md:148. 인용된 구현과 LG2-096의 적용 범위가 균일·비균일 ACC임을 명시했다. |
| `lisflood-fp-io-boundary.md:276,277,278,279` / 265 | 정정 | 경계·점원·위어·SGC 채널 셀은 자기 자신으로 설정해 라우팅을 비활성화한다. (`infevap.cpp:251–296`) | 경계 셀은 `if (BCptr->BC_Ident[BCi] != NONE0)`일 때 자기 자신을 이동 대상으로 설정한다. (`infevap.cpp:263–288`)  <br>점원 셀은 자기 자신을 이동 대상으로 설정한다. (`infevap.cpp:291–296`) <br>선택한 이동 면에 위어가 있으면 `Statesptr->weirs == ON`일 때 자기 자신을 이동 대상으로 설정한다. (`infevap.cpp:176–180,192–196,208–212,224–228`) <br>SGC 채널 셀은 `if (Statesptr->SGC==ON)` 안에서 `if (Arrptr->SGCwidth[p0]>C(0.0))`를 만족하면 자기 자신을 이동 대상으로 설정한다. (`infevap.cpp:249–256`) | infevap.cpp:176–180,192–196,208–212,224–228,249–296. 모든 경계·위어 셀에 무조건 적용하는 표현을 실제 조건으로 나누었다. 기존 인용 251–296에는 위어 분기가 없었다. |
| `lisflood-fp-io-boundary.md:282` / 267 | 정정 | `dist_routing` 모드는 DEM 경사의 제곱근을 속도에 곱한다. (`infevap.cpp:185–189`; [LT1-305 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LT1.md)) | `dist_routing` 모드는 DEM 경사의 제곱근을 속도에 곱한다. (`infevap.cpp:185–189`; [LT1-305 최종 결론](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LT1.md)) <br>북·남 방향의 이동 시간은 `Arrptr->RouteInt[p0] = dy / Routing_Speed;`로 설정한다. 동·서 방향은 `Arrptr->RouteInt[p0] = dx / Routing_Speed;`로 설정한다. (`infevap.cpp:189,205,221,237`) | infevap.cpp:189,205,221,237; bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:148. 본문 교체에서 빠진 이동 시간의 거리·속도 관계를 실제 방향별 대입식으로 복원했다. |
| `lisflood-fp-io-boundary.md:290,291,292` / 274 | 정정 | 이동량에는 `if(flow<0) {flow=0;}`를 적용한다. (`infevap.cpp:377–383`) | 이동량에는 `if(flow<0) {flow=0;}`를 적용한다. (`infevap.cpp:377–383`) <br>이동 비율은 `flow_fraction=Solverptr->Tstep/Arrptr->RouteInt[p0];`로 계산한다. (`infevap.cpp:385`) <br>이동 비율에는 `if(flow_fraction>1) flow_fraction=1;`을 적용한다. (`infevap.cpp:386`) <br>실제 이동 수심은 `flow=flow*flow_fraction;`으로 정한다. (`infevap.cpp:388–391`) | infevap.cpp:385–391; bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:148; lisflood-docx-manual-vs-code.md:453. 수면차 제한 설명을 추가하면서 빠진 시간 비율을 복원했다. 원문의 비율 상한도 함께 명시했다. |
| `lisflood-fp-io-boundary.md:308` / 290 | 정정 | Binary 격자의 첫 두 값은 `int`형 `xsz`·`ysz`이다. (`output.cpp:551–617`; `input.cpp:1244–1256`) | Binary 격자의 첫 두 값은 `int`형 열 수와 행 수이다. (`output.cpp:551–617`; `input.cpp:1244–1256`) | output.cpp:553–554,571–574,587–589. flux 분기는 xsz+1 또는 ysz+1을 기록하므로 첫 두 값을 항상 xsz·ysz로 부를 수 없다. |
| `lisflood-fp-io-boundary.md:309` / 291 | 정정 | 그 뒤 좌표·NoData·자료의 저장 형식은 `NUMERIC_TYPE`이다. (`output.cpp:551–617`) | 그 뒤 좌표·격자 간격·NoData·자료의 저장 형식은 `NUMERIC_TYPE`이다. (`output.cpp:551–617`) | output.cpp:555–558,575–579,590–594; bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:162. 원래 헤더 설명의 dx가 누락되어 격자 간격을 복원했다. |
| `lisflood-fp-io-boundary.md:349` / 331 | 보완 | \| checkpoint(`.chkpnt`) \| 바이너리 \| 형식 판·driver별 저장 상태를 구분한다. (`chkpnt.cpp:211–314`)  \| | \| checkpoint(`.chkpnt`) \| 바이너리 \| 형식 판·driver별 저장 상태를 구분한다. (`chkpnt.cpp:211–314`; `cuda/acc_nugrid/write_chkpnt.cu:75–87`)   \| | chkpnt.cpp:248–254; cuda/acc_nugrid/write_chkpnt.cu:75–87. driver별 저장 상태를 구분하는 표 요약에 비균일 ACC writer 근거를 보탰다. |

### IO 형식 확인

Markdown 상대 링크 34개를 노트 위치에서 해석했다.
서로 다른 링크 대상은 15개이다.
파일 누락과 절 앵커 불일치는 없다.
이 수는 최종 노트의 Markdown 링크를 추출하여 셌다.
인용 파일의 존재와 줄 범위 상한을 추가로 확인했다.
절대 사용자 경로·홈 경로·위키 링크 표기는 없다.
작업 한계 문장은 없다.
Mermaid 블록은 없다.
`git diff --check -- models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md`는 통과했다.
IO 노트의 미해결 항목은 없다.

## CPU·CUDA·Metal 차이 노트 대조 완료

노트: [lisflood-fp-cpu-gpu-differences.md](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-cpu-gpu-differences.md).
대조한 대상은 작업 시작 시 전체 46줄이다.
정정은 최종 노트의 정정 표식 기준 7줄이다.
인용 보완만 한 줄은 없다.
원래 31행의 판 설명을 7행으로 나누어 고쳤다.
최종 노트는 52줄이다.
이 수는 작업 시작 시 46줄과 이번 패치 결과를 대조하여 확인했다.

### 대상 줄별 대조 범위

아래 줄 번호는 작업 시작 시 노트의 줄 번호이다.

| 대상 줄 | 대조한 줄 수 | 근거 원문 | 판정 |
|---|---:|---|---|
| 1–19 | 19 | `LISFLOOD-FP-notes-apply-6.md:60–67`; `LISFLOOD-FP-note-job-6.tsv:101–102`; 본문 두 행의 실제 원문 | frontmatter의 작성자·날짜·반영 방법·주제·코드 범위가 대응한다. related의 네 파일이 존재한다. |
| 20–30 | 11 | 두 차이 표의 열 구성과 원문 파일 위치 | AI 정리와 원문 인용의 구분이 대응한다. 코드 기준 상대 경로가 실제 소스 루트를 가리킨다. 빈 줄과 제목도 포함했다. |
| 31 | 1 | PDF p.1; DOCX 변환본 p.1·5; bridge DOCX 변환본 p.1 쪽 이미지; DOCX 보고서 §1.1; callflow §5.1; 8.3 패키지 `README.md:19–24`; `VersionHistory.h:16–23`; 최종 LB1-408 | DOCX 최상단 판을 고쳤다. 근거 없는 8.3 DOI 귀속을 제거했다. 판 식별의 출처를 문장마다 붙였다. |
| 32–34 | 3 | 본문 표 형식 | 빈 줄·표 머리글·구분선을 확인했다. |
| 35 | 1 | 최종 RF-007; 최종 결론 TSV의 RF-007; 배정표 6의 RF-007; PDF p.16·DOCX p.20·bridge DOCX p.21 쪽 이미지; `swe/fv1.cpp:23–30,43–64`; `cuda/fv1/cuda_fv1_simulate.cu:93–94,161–170`; `cuda/cuda_solver.templates.cu:19,36–39,74–84`; `cuda/adaptive/cuda_adaptive_simulate.cu:184,422–430,798` | C 문서 누락 분류가 같다. 결론 문장 전체가 최종 결론과 같다. adaptive 조건과 종료 시각 초과 보정의 대입 순서가 원문과 같다. |
| 36 | 1 | 최종 LG1-002; 최종 결론 TSV의 LG1-002; 배정표 6의 LG1-002; `lisflood.h:75–97`; `config.default.cmake:2`; `cuda/cuda_flow.cuh:11–13`; `cuda/cuda_flow.cu:4–12`; `metal/fv1/metal_fv1_kernels.metal:115–118`; `metal/fv1/metal_fv1_simulate.mm:575–580` | 최종 C 분류가 같다. 이전 보고서의 F를 사용하지 않았다. 결론 문장 전체가 최종 결론과 같다. double·float 조건과 Metal 보존변수 형식이 원문과 같다. |
| 37–46 | 10 | 아키텍처 맵; Metal FV1 노트; callflow와 CPU·GPU SWE 보고서; RF·LG1 최종 근거 파일 | 연결 문장의 내용과 링크 대상이 대응한다. 근거 목록·제목·빈 줄을 확인했다. |

대조 범위 표의 줄 수 합계는 46줄이다.
차이 표의 두 행은 각각 6열이다.
두 행의 최종 결론 문장은 문자열 대조에서도 일치했다.
이 노트에는 A 행과 E 행이 없다.
Claude 최종 조정의 세 행과 외부 출처 파일 끝 절의 두 행은 이 차이 표의 대상이 아니다.
CPU·GPU SWE 보고서 §4와 callflow §6에는 이 새 노트를 직접 지목한 기존 문장 교체안이 없다.

### 정정 목록

아래 위치는 최종 노트의 줄 번호이다.
아래 일곱 줄의 원래 대상 위치는 모두 31행이다.

| 최종 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `lisflood-fp-cpu-gpu-differences.md:31` | 한 문장에 문서 세 판과 코드 판을 압축했다. PDF 표지의 쪽 인용이 없었다. | PDF 표지의 `Code release 6.1.1`과 표지 날짜 2013-11-25를 문장으로 나누었다. p.1을 인용했다. | `lf-manual-pdf-001.png`의 `Code release 6.1.1`과 `25th November 2013`. |
| `lisflood-fp-cpu-gpu-differences.md:32` | DOCX는 판 이력의 5.9만 적었다. | 표지의 `6.1.1` 삭제와 `8.0.0` 추가를 명시했다. | `lf-manual-docx-001.png`; DOCX 판독 기록 `p001-018.md:15`. |
| `lisflood-fp-cpu-gpu-differences.md:33` | `user manual.docx는 판 이력 맨 위 5.9` | 최상단은 변경 추적으로 추가한 `8.0 Jul 20 2020`이다. 기존 5.9는 그 아래이다. | `lf-manual-docx-005.png`; DOCX 판독 기록 `p001-018.md:19`; `lisflood-docx-manual-vs-code.md` §1.1; callflow §5.1. |
| `lisflood-fp-cpu-gpu-differences.md:34` | bridge 표지의 판·날짜에 쪽 인용이 없었다. | 표지의 `Code release 4.3.6`과 표지 날짜 2008-04-25를 문장으로 나누었다. 변환본 p.1을 인용했다. | `lf-manual-bridge-docx-001.png`의 `Code release 4.3.6`과 `25th April 2008`. |
| `lisflood-fp-cpu-gpu-differences.md:35` | `공식 8.3 패치(10.5281/zenodo.13121119)` | 확인된 8.2 DOI와 8.3 변경 적용 관계를 적었다. 8.3 DOI 귀속은 제거했다. | 8.3 패키지 `README.md:19–24`의 DOI는 8.2 `13121102`이다. 최종 LB1-408은 이 줄을 8.3 `13121119`의 근거로 쓰지 않도록 정정한다. |
| `lisflood-fp-cpu-gpu-differences.md:36` | `VersionHistory.h:16–23`의 숫자 판 8.1.0과 릴리스 이름을 함께 적었다. | 내부 숫자 판 8.1.0을 별도 문장과 직접 인용으로 적었다. | `VersionHistory.h:16–18`: `LF_VersionMajor 8`, `LF_VersionMinor 1`, `LF_VersionInc 0`. |
| `lisflood-fp-cpu-gpu-differences.md:37` | 릴리스 이름 8.3이 압축된 판 설명 끝에 있었다. | 릴리스 이름 8.3을 별도 문장과 직접 인용으로 적었다. | `VersionHistory.h:21–23`: 체크포인트 숫자 유지 주석과 `#define LF_Release "8.3"`. |

### CPU·CUDA·Metal 형식 확인

최종 노트의 Markdown 상대 링크 8개는 모두 다른 대상이다.
파일 누락과 절 앵커 불일치는 없다.
이 수는 최종 노트의 Markdown 링크를 추출하여 셌다.
인용 코드 파일과 줄 범위가 존재한다.
절대 사용자 경로·홈 경로·위키 링크 표기는 없다.
작업 한계 문장은 없다.
Mermaid 블록은 없다.
CPU·CUDA·Metal 노트의 미해결 항목은 없다.

## 최종 집계

| 노트 | 작업 시작 시 대상 줄 수 | 대조한 줄 수 | 정정 표식 줄 수 | 보완 표식 줄 수 | 미해결 항목 |
|---|---:|---:|---:|---:|---:|
| IO 본문 | 172 | 172 | 28 | 4 | 0 |
| CPU·CUDA·Metal 차이 | 46 | 46 | 7 | 0 | 0 |
| 합계 | 218 | 218 | 35 | 4 | 0 |

대상 줄 수는 작업 시작 시 확정한 diff와 새 파일에서 센 값이다.
정정·보완 줄 수는 최종 노트의 이번 작업 표식에서 센 값이다.
기계 확인 불일치 후보는 사용자 지정대로 없다.
쓰기 대상은 두 노트와 이 DELIVERABLE뿐이다.
두 노트의 최종 내용은 작업 시작 시 내용에 기록한 패치만 적용한 결과와 일치한다.
모든 패치 위치는 작업 시작 시 대상 줄에 연결된다.
조건문·대입문 인용은 공백을 정규화한 코드 대조에서 불일치가 없다.
두 노트와 DELIVERABLE을 대상으로 한 최종 `git diff --check`는 통과했다.
원문 대조에는 읽기 전용 `git diff`와 지정 커밋의 `git show`를 사용했다.
모델 실행과 git 쓰기 명령은 수행하지 않았다.
지정한 대상 줄의 대조를 모두 마쳤으므로 작업을 종료한다.
