# LISFLOOD-FP CUDA GPU 노트 추가 줄 전수 대조

- 대상 노트: `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md`.
- 시작 시 `git diff -U0 HEAD -- <대상 노트>`의 추가 줄은 261줄이다.
- 시작 시 대상 줄: 7–8, 12, 18–21, 25–26, 29–31, 33–35, 111–113, 115–116, 119–126, 128–130, 158–162, 181–185, 192–201, 207–215, 223–236, 249–258, 270–289, 293, 295–296, 298–300, 305–313, 319, 322–462.
- 상태: 완료.
- 판정 기준: 현재 코드, 지정된 이전 배포본, 배포본 패치, 문서 쪽 이미지, 최종 결론, 보고서 수정안.
- 정정 수와 보완 수는 변경한 노트 줄을 기준으로 센다.

## 대조 결과

| 노트 | 대조한 대상 줄 | 정정 | 보완 | 미해결 |
|---|---:|---:|---:|---:|
| [lisflood-fp-cuda-gpu.md](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md) | 261 | 20 | 10 | 0 |

- 대상 261줄은 본문·frontmatter·구조 줄 141줄과 차이 표 120행으로 구성된다.
- 수정 전후의 노트 줄 수는 같다. 아래 줄 번호는 수정 후에도 유효하다.
- 차이 표 120행의 분류는 최종 배정표와 일치한다. A 7행, B 6행, C 63행, E 38행, F 6행이다.
- E의 강도는 강함 33행, 중간 4행, 약함 1행이다. 최종 근거와 일치한다.
- LI2-352·LI1-369에는 [Claude 최종 조정](../compare/LISFLOOD-FP-conclusion-claude-final.md)을 우선 적용했다. 두 행의 E·강함과 “8.2 결함, 8.3에서 고침”을 유지했다.
- U·N·M을 해법 이름으로 풀어 쓴 문장은 최종 근거와 뜻이 같다. 최종 근거에 없는 모델 동작 주장은 추가하지 않았다.
- LG1-153의 작업 한계 문장은 사용자 기준 6에 따라 삭제했다. LI2-337의 “시간 격자 네 종류”는 원문의 실제 파일명으로 정정했다.
- 본문에서 삭제·교체된 기존 문장은 해당 보고서의 §4 수정안과 대조했다. 비분리 FV1 갱신, 바닥 원천항 괄호, 경계 내부·외부 상태, MaxField의 판 차이, acc_nugrid의 초기 격자 구분을 확인했다.
- 문서의 수치·표·판 표시는 지정된 쪽 이미지로 판정했다. DOCX 쪽 번호는 LibreOffice 변환본 기준이다.
- 상대 링크 327개와 frontmatter의 related 경로는 실제 파일을 가리킨다. 링크의 절 앵커도 맞는다.
- 코드 인용의 파일과 줄 범위는 모두 유효하다. 파일·줄 바로 뒤에 붙은 인용 439쌍은 공백과 표의 파이프 이스케이프를 정규화하면 원문 또는 원문의 연속 부분 문자열과 일치한다.
- 노트에 절대 홈 경로, 물결표 홈 경로, 위키 링크 문법은 없다. 작업 미완료를 뜻하는 한계 문장도 없다.
- 노트에 mermaid 블록은 없다. 실행 흐름 설명은 callflow §4의 10-21 Claude 수정본·렌더 확인 문단과 §6에 대조했다.
- 사용자가 별도로 지정한 기존 61행의 블록 크기 표기도 확인했다. 이 행은 최초 추가 줄 261줄에 포함되지 않는다.
- 기계 확인 후보 16건은 모두 원문과 일치하거나 유효한 축약 표기이다. 중복 후보도 제시 순서대로 따로 판정했다.
- 수정 후 읽기 전용 `git diff --check`는 오류 없이 끝났다.

### 대상 줄 대조 범위

아래 범위의 모든 줄을 대조했다. 빈 줄과 표 머리글도 대상 줄 수에 포함했다.

| 노트 줄 | 줄 수 | 대조 근거와 결과 |
|---|---:|---|
| 7–8 | 2 | 원문 파일 목록과 notes-apply-3의 반영 기록을 대조했다. frontmatter 값은 유지했다. |
| 12 | 1 | 노트 위치에서 architecture-source-map.md의 존재를 확인했다. |
| 18–21 | 4 | lisflood.cpp:419–450·778–788, LT1-419·RF-018, 보고서 §4를 대조했다. |
| 25–26 | 2 | FV1·FV2 HLL 호출과 FV2·DG2 공간 연산자를 대조했다. 26행을 보완했다. |
| 29–31 | 3 | acc_nugrid의 반복 전 격자 구성, adaptive:479의 조건, Metal 분기를 대조했다. |
| 33–35 | 3 | 세 SWE 해법의 HLL 호출과 ACC 관성식을 대조했다. 아키텍처 링크를 확인했다. |
| 111–113 | 3 | FV1 update_flow_variables와 LG1-011의 비분리 갱신 수정안을 대조했다. |
| 115–116 | 2 | FV1 x·y 커널의 Uold·Ux 인수와 갱신 순서를 대조했다. |
| 119–126 | 8 | 현재 FV1 flux·HU 식·양쪽 barrier를 8.2 코드와 8.3 패치에 대조했다. 121–123행을 정정했다. |
| 128–130 | 3 | y flux의 Uold와 누적 배열 Uint를 원문에 대조했다. |
| 158–162 | 5 | ACC dt_field 할당·CFL 조건·축약과 LG2-008을 대조했다. |
| 181–185 | 5 | 수위형 점 원천의 FMIN, CPU·CUDA·Metal의 수심식과 LG1-024를 대조했다. |
| 192–201 | 10 | 수위·유량·벽 경계의 내부·외부 상태와 임계값을 대조했다. 193행에 v8.0·v8.1 인용을 보완했다. |
| 207–215 | 9 | ACC 지역 유출 보정과 NoData 배수식을 대조했다. 8.3의 건조 셀 가산 생략을 패치와 대조했다. |
| 223–236 | 14 | RK 가중치, 시간·체적 장부, 침수 면적, 순간 점 원천, ghost 버퍼를 대조했다. 224·234행을 보완했다. |
| 249–258 | 10 | 8.2 MaxField 인수·할당과 8.3 device 할당·초기화·복사를 대조했다. Flow staging 근거를 보완했다. |
| 270–289 | 20 | 각 driver의 실제 최대 파일·checkpoint·snapshot·Metal 출력 호출을 대조했다. 280·283행을 보완했다. 288행을 정정했다. |
| 293 | 1 | acc_nugrid의 초기 격자라는 절 제목을 LG2-035·RF-014에 대조했다. |
| 295–296 | 2 | acc_nugrid 실행 루프와 주석 처리된 Haar 식, adaptive Haar 함수를 대조했다. |
| 298–300 | 3 | 활성 HH·GA·GB·GC 필터와 지형·사전 플래그·n/H detail을 대조했다. 299행을 보완했다. |
| 305–313 | 9 | 고정 초기 격자·조건부 재구성·0인 mass 인자·비활성 raster·자체 출력 값을 대조했다. 310·311행을 보완했다. |
| 319 | 1 | FV1 두 방향 기여의 비분리 갱신을 LG1-011과 코드에 대조했다. |
| 322–342 | 21 | 요약·인용 기준·배정 링크·문서 판·표 머리글을 대조했다. 326행의 조건과 339행의 DOCX 판을 정정했다. |
| 343–351 | 9 | bridge-docx의 배정 9행을 LB1b 최종 결론, 교량 DOCX 쪽 이미지, 인용 원문에 대조했다. |
| 352–361 | 10 | build-83의 배정 10행을 LN1 최종 결론, 각 판 코드, 배포 문서·패치에 대조했다. |
| 362–367 | 6 | callflow의 배정 6행을 RF 최종 결론, 반영 전 노트, 코드·패치, callflow §8.1에 대조했다. |
| 368–403 | 36 | ACC·adaptive의 배정 36행을 LG2 최종 결론과 CPU·균일 CUDA·비균일 CUDA·adaptive 원문에 대조했다. |
| 404–437 | 34 | SWE의 배정 34행을 LG1 최종 결론과 CPU·CUDA·Metal 원문에 대조했다. 호출되지 않는 경로의 표시도 대조했다. |
| 438–442 | 5 | DOCX의 배정 5행을 LV1 최종 결론, 문서 이미지, 과거 코드와 8.3 패치에 대조했다. |
| 443–452 | 10 | 입출력의 배정 10행을 LI2 최종 결론·Claude 조정, PDF 이미지, 과거·현재 writer에 대조했다. |
| 453–461 | 9 | 입력의 배정 9행을 LI1 최종 결론·Claude 조정, PDF 이미지, parser·driver·패치에 대조했다. |
| 462 | 1 | LT1-419를 최종 결론, 기존 노트, 현재·8.2 분기에 대조했다. |

## 정정·보완 목록

각 항목의 경로는 `models/LISFLOOD-FP/source-analysis/lisflood-fp-cuda-gpu.md`이다. 전·후는 변경한 부분을 적었다. 모든 변경 줄 끝에는 요청한 전수 검증 표지를 붙였다. 표 행의 표지는 결론 문장 칸 끝에 붙였다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| lisflood-fp-cuda-gpu.md:26 | 보완 | 전: `` cuda/fv2/cuda_fv2_solver.cu:221,695–709 ``<br>후: `` cuda/fv2/cuda_fv2_solver.cu:221,235–239,695–709`; `cuda/dg2/cuda_dg2_solver.cu:278–282 `` | FV2:235–239의 `Lx.set_0(...)`와 DG2:278–282의 `Lx.set_1x(...)`를 대조했다. |
| lisflood-fp-cuda-gpu.md:121 | 정정 | 전: `` cuda/fv1/cuda_fv1_solver.cu:375 ``<br>후: `` cuda/fv1/cuda_fv1_solver.cu:374 `` | 현재 `cuda/fv1/cuda_fv1_solver.cu:374`: `H = U0.H - cuda::dt * (F_e.H - F_w.H)/cuda::geometry.dx;`. |
| lisflood-fp-cuda-gpu.md:122 | 정정 | 전: `` cuda/fv1/cuda_fv1_solver.cu:376–377 ``<br>후: `` cuda/fv1/cuda_fv1_solver.cu:375–376 `` | 현재 `cuda/fv1/cuda_fv1_solver.cu:375–376`에 인용한 HU 갱신의 두 줄이 있다. |
| lisflood-fp-cuda-gpu.md:123 | 정정 | 전: `` cuda/fv1/cuda_fv1_solver.cu:376–377 ``<br>후: `` cuda/fv1/cuda_fv1_solver.cu:375–376 `` | 현재 `cuda/fv1/cuda_fv1_solver.cu:375–376`의 괄호에서 `bed_source_x(...)`는 flux 차분의 `/cuda::geometry.dx` 밖에 있다. LG1-011 수정안과 같다. |
| lisflood-fp-cuda-gpu.md:193 | 보완 | 전: `` `swe/fv1.cpp:531–532`; ``<br>후: `` `v8.0:swe/fv1.cpp:531–532,540–542`; `v8.1:swe/fv1.cpp:531–532,540–542`; `swe/fv1.cpp:531–532`; `` | v8.0:532·542의 `H_inside = H_outside;`가 v8.1:532·542에서 `//H_inside = H_outside;`로 바뀐다. |
| lisflood-fp-cuda-gpu.md:224 | 보완 | 전: `` cuda/dg2/cuda_dg2_solver.cu:262–264,391–438 ``<br>후: `` cuda/dg2/cuda_dg2_solver.cu:262–264,353,391–438 `` | 현재 `cuda/dg2/cuda_dg2_solver.cu:353`은 y 방향 질량 집계에도 `C(0.5)`를 전달한다. |
| lisflood-fp-cuda-gpu.md:234 | 보완 | 전: `` `cuda/cuda_stats.cu:14–19,92–118`; ``<br>후: `` `cuda/cuda_stats.cuh:36`; `cuda/cuda_stats.cu:14–19,92–118`; `` | `cuda/cuda_stats.cuh:36`: `MassStats* d_instantaneous_mass; /**< through BCs/PSs during timestep*/`. |
| lisflood-fp-cuda-gpu.md:253 | 보완 | 전: `` ([LI2-352 수정안] ``<br>후: `` (`cuda/fv1/cuda_fv1_simulate.cu:57–62`; `cuda/fv1/cuda_fv1_flow.cu:6–26`; `cuda/cuda_max_field.cu:96–98`; [LI2-352 수정안] `` | FV1 run:57–62는 Flow의 pinned H·HU·HV를 준비한다. MaxField:96–98은 별도의 maxH device 배열을 할당한다. |
| lisflood-fp-cuda-gpu.md:280 | 보완 | 전: `` `v8.1:cuda/fv2/cuda_fv2_snapshot.cu:30–48`; ``<br>후: `` `v8.1:cuda/fv2/cuda_fv2_snapshot.cu:30–48`; `cuda/fv1/cuda_fv1_snapshot.cu:30–42`; `cuda/fv2/cuda_fv2_snapshot.cu:30–48`; `cuda/dg2/cuda_dg2_snapshot.cu:36–54`; `cuda/io.templates.cpp:15–28,118–121`; `` | 현재 SWE snapshot은 outflag=0을 전달한다. `cuda/io.templates.cpp:15–28`은 DEM과 같은 ncols·nrows를 쓰며 :120은 AsciiRaster::write를 호출한다. |
| lisflood-fp-cuda-gpu.md:283 | 보완 | 전: `` (`cuda/acc/cuda_acc_snapshot.cu:41–42`; ``<br>후: `` (`v8.1:cuda/acc/cuda_acc_snapshot.cu:41–42`; `v8.1:cuda/acc/cuda_acc_solver.cu:605–606`; `cuda/acc/cuda_acc_snapshot.cu:41–42`; `` | v8.1 snapshot:41–42와 현재 snapshot:41–42는 Qxold·Qyold를 쓴다. v8.1·현재 solver:605–606은 dx로 나누어 m²/s를 반환한다고 적는다. |
| lisflood-fp-cuda-gpu.md:288 | 정정 | 전: `` Metal FV1은 v8.3에 추가한 공유 SWE 출력 함수를 호출한다. ``<br>후: `` 8.3에 추가된 Metal FV1은 공유 SWE 출력 함수를 호출한다. ``<br>전: `` `metal/fv1/metal_fv1_simulate.mm:1347–1354,1453–1459,1472–1477` ``<br>후: `` `VersionHistory.h:31–32`; `metal/fv1/metal_fv1_simulate.mm:1453–1459,1472–1477` `` | LI2-341 최종 문장은 Metal FV1의 8.3 추가를 말한다. VersionHistory:31–32가 이를 적는다. Metal simulate:1453–1459·1472–1477은 공유 SWE writer를 호출한다. |
| lisflood-fp-cuda-gpu.md:299 | 보완 | 전: `` `cuda/acc_nugrid/preflag_topo.cu:15–23`; ``<br>후: `` `cuda/acc_nugrid/preflag_topo.cu:15–23`; `cuda/acc_nugrid/cuda_acc_nugrid_simulate.cu:154`; `cuda/acc_nugrid/preflag_details.cu:20–71`; `` | simulate:154는 boundaries·point_sources·gauge_points를 preflag_details에 넘긴다. preflag_details:20–71은 세 종류의 위치를 true로 표시한다. |
| lisflood-fp-cuda-gpu.md:310 | 보완 | 전: `` `v8.2:cuda/adaptive/output/write_cumulative_data.cpp:18–28`; ``<br>후: `` `v8.2:cuda/adaptive/classes/SolverParams.h:33–46`; `v8.2:cuda/adaptive/output/write_cumulative_data.cpp:18–28`; `cuda/adaptive/classes/SolverParams.h:33–46`; `cuda/adaptive/output/write_cumulative_data.cpp:18–28`; `` | v8.2·현재 SolverParams:33–46은 자체 키워드를 읽는다. 두 판의 write_cumulative_data:18·28은 .cumu 이름과 CSV 머리글을 쓴다. |
| lisflood-fp-cuda-gpu.md:311 | 보완 | 전: `` `cuda/adaptive/output/write_raster_file.cu:17`; ``<br>후: `` `cuda/adaptive/output/write_raster_file.cu:17,30–48`; `cuda/adaptive/output/write_all_raster_maps_fv1.cu:71–74,115–136`; `cuda/adaptive/output/write_all_raster_maps_dg2.cu:102–135,176–198`; `` | FV1 writer:120·131과 DG2 writer:181·192는 소문자 qx·qy를 전달한다. DG2 writer:104·108은 각 raster 셀의 중앙 좌표를 평가한다. |
| lisflood-fp-cuda-gpu.md:326 | 정정 | 전: `` adaptive는 유동 detail로 시간 반복 중 격자를 갱신한다. ``<br>후: `` adaptive는 `if (solver_params.epsilon > C(0.0) \|\| first_t_step)`에서 유동 detail로 격자를 갱신한다. `` | 현재 `cuda/adaptive/cuda_adaptive_simulate.cu:479`의 조건을 그대로 반영했다. LG2-035 최종 결론과 같다. |
| lisflood-fp-cuda-gpu.md:339 | 정정 | 전: `` 문서 판: 2013 PDF 매뉴얼(표지 Code release 6.1.1, 2013-11-25), user manual.docx(판 이력 맨 위 5.9), user manual +bridge.docx(Code release 4.3.6, 2008-04-25); 코드 판: Zenodo 8.2 `10.5281/zenodo.13121102`에 공식 8.3 패치 `10.5281/zenodo.13121119`를 적용한 8.3(8.2 + 공식 패치), `VersionHistory.h:16–23`의 숫자 판 8.1.0과 릴리스 이름 8.3. ``<br>후: `` PDF 매뉴얼 표지는 Code release 6.1.1과 2013-11-25를 적는다. user manual.docx 표지에는 6.1.1 삭제와 8.0.0 삽입의 변경 추적이 있다. 이 DOCX의 판 이력 최상단은 8.0(2020-07-20)이다. user manual +bridge.docx 표지는 Code release 4.3.6과 2008-04-25를 적는다. DOCX 쪽 번호는 LibreOffice 변환본 기준이다. (PDF p.1; DOCX p.1·5; 교량 DOCX p.1; [판 대조 기록](../../../_staging/recovery/compare/LISFLOOD-FP-version-verify-AD1.md)) 현재 코드는 Zenodo 8.2 `10.5281/zenodo.13121102`에 공식 8.3 패치 `10.5281/zenodo.13121119`를 적용한 8.3이다. ([빌드·8.3 보고서](../../../_staging/recovery/compare/lisflood-build-83-vs-code.md)) `VersionHistory.h:16–23`의 숫자 판은 8.1.0이다. 같은 파일의 릴리스 이름은 8.3이다. `` | DOCX p.1·5 쪽 이미지와 AD1:41–43을 대조했다. p.5의 5.9 위에 `8.0`, `Jul 20 2020` 행이 있다. PDF·교량 DOCX p.1과 VersionHistory:16–23도 대조했다. |
| lisflood-fp-cuda-gpu.md:353 | 정정 | 전: `` `cuda/cuda_max_field.cu:21–26,96–107` ``<br>후: `` `v8.2:cuda/cuda_max_field.cu:21–26,96–107` `` | 8.2 host 분기 근거는 v8.2 max_field:96–107이다. 현재 max_field:96–98은 device 할당이다. |
| lisflood-fp-cuda-gpu.md:355 | 정정 | 전: `` `cuda/dg2/cuda_dg2_solver.cu:230–252` ``<br>후: `` `v8.0:cuda/dg2/cuda_dg2_solver.cu:230–252` `` | v8.0 DG2:230–252에 쓰기 후 barrier·lane continue·기울기 갱신이 있다. 이 범위 끝에는 reader barrier가 없다. 현재 같은 행 범위는 다른 코드이다. |
| lisflood-fp-cuda-gpu.md:356 | 정정 | 전: `` 8.2: `lisflood.h:75–97` ``<br>후: `` 8.2: `v8.2:lisflood.h:75–97` ``<br>전: `` `config.float.cmake:2` ``<br>후: `` `../LISFLOOD-FP-8.3-package/config.float.cmake:2` `` | v8.2 lisflood.h:75–97은 _NUMERIC_MODE에 따라 double·float를 고른다. 배포본 config.float.cmake:2는 `add_compile_definitions(_NUMERIC_MODE=0)`이다. 이 파일은 현재 코드 루트가 아니라 8.3-package에 있다. |
| lisflood-fp-cuda-gpu.md:362 | 정정 | 전: `` Hold가 0이고 dt가 유한 양수이면 이 식은 0이다. ``<br>후: `` Hold가 0이고 격자 치수가 유한하며 dt가 유한 양수이면 이 식은 0이다. `` | 현재 `cuda/cuda_boundary.cu:291–292`는 `-Hold * dx * dy / dt`이다. RF-013 최종 결론의 유한 격자 치수 조건을 코드 설명 칸에도 반영했다. |
| lisflood-fp-cuda-gpu.md:363 | 정정 | 전: `` `source-analysis/lisflood-fp-architecture-source-map.md:68` ``<br>후: `` `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:68` ``<br>전: `` `노트:source-analysis/lisflood-fp-architecture-source-map.md:7,39,68` ``<br>후: `` `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:7,39,68` ``<br>전: `` `노트:README.md:11` ``<br>후: `` `bf804e23:models/LISFLOOD-FP/README.md:11` `` | 지정 커밋의 architecture 노트:39·68에는 동적 해상도 설명이 있다. 같은 커밋의 모델 README:11에는 acc_nugrid를 dynamic resolution adaptivity로 적은 문장이 있다. |
| lisflood-fp-cuda-gpu.md:365 | 정정 | 전: `` `노트:source-analysis/lisflood-fp-architecture-source-map.md:68` ``<br>후: `` `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:68` `` | 지정 커밋의 architecture 노트:68은 FV2·adaptive가 빠진 CUDA 디렉터리 목록이다. |
| lisflood-fp-cuda-gpu.md:366 | 정정 | 전: `` 커널의 ghost 인덱스와 크기 대조는 §8.1. ``<br>후: `` 커널의 ghost 인덱스와 크기 대조는 [실행 흐름 보고서 §8.1](../../../_staging/recovery/flow/LISFLOOD-FP-callflow.md#81-코드-결함-후보의-반대-근거-확인)에 있다. `` | callflow:1141의 `### 8.1 코드 결함 후보의 반대 근거 확인`이 대상이다. 노트 자체의 §8.1은 입력·출력 절이다. |
| lisflood-fp-cuda-gpu.md:367 | 정정 | 전: `` 반대 근거는 §8.1. ``<br>후: `` 반대 근거는 [실행 흐름 보고서 §8.1](../../../_staging/recovery/flow/LISFLOOD-FP-callflow.md#81-코드-결함-후보의-반대-근거-확인)에 있다. `` | callflow §8.1은 flux reader barrier와 8.3 패치를 대조한다. 노트 자체의 §8.1을 가리키던 표현을 고쳤다. |
| lisflood-fp-cuda-gpu.md:425 | 정정 | 전: `` `cuda/cuda_stats.cu:159`, `cuda/cuda_stats.cu:176` ``<br>후: `` `cuda/fv1/cuda_fv1_simulate.cu:159`, `cuda/fv1/cuda_fv1_simulate.cu:176` `` | 현재 FV1 simulate:159·176의 원문은 각각 `stats_collector.accumulate_mass();`이다. cuda_stats.cu에는 176행이 없다. |
| lisflood-fp-cuda-gpu.md:432 | 정정 | 전: `` CPU: 기본 CPU 초기화·출력과의 전체 checkpoint 대조는 이 작업의 목적이 아니다. ``<br>후: `` — `` | 작업 범위를 말하는 한계 문장이다. 사용자 검사 기준 6에 따라 삭제했다. 공통 checkpoint 정의와 현재 driver의 미호출 결론은 원문과 맞으므로 유지했다. |
| lisflood-fp-cuda-gpu.md:437 | 정정 | 전: ``  ACC 전용 계산은 선택한 SWE 경로의 비교 완료 조건에 포함하지 않는다. ``<br>후: 삭제 | 작업 완료 조건을 말하는 한계 문장이다. 사용자 검사 기준 6에 따라 삭제했다. FV1·FV2·DG2 driver가 ACC 전용 함수를 호출하지 않는다는 코드 사실은 유지했다. |
| lisflood-fp-cuda-gpu.md:441 | 정정 | 전: `` user manual.docx p.40–44(변환본) 표 15; user manual.pdf p.35–39 표 15 ``<br>후: `` user manual.docx p.40–44(변환본) §5.1–5.2; user manual.pdf p.35–39 §5.1–5.2 `` | 해당 DOCX·PDF 쪽 이미지에는 checkpointing과 output file formats 절이 있다. 표 15는 없다. DG2 모드 파일 누락과 실제 driver의 .max 호출 판정은 유지했다. |
| lisflood-fp-cuda-gpu.md:448 | 정정 | 전: `` 종료 시 시간 격자 네 종류를 쓰며 mxe 호출은 주석이다. ``<br>후: `` 종료 시 `.inittm`·`.totaltm`·`.max`·`.maxtm`을 쓴다. `.mxe` 호출은 주석이다. `` | 현재 ACC snapshot:54–57의 네 파일 중 .max는 최대 수심이다. ACC simulate:329가 writer를 호출한다. :343의 .mxe 호출은 주석이다. |
| lisflood-fp-cuda-gpu.md:454 | 정정 | 전: `` `lisflood.cpp:433` `{`<br>`lisflood.cpp:434` `lis::cuda::dg2::Simulation simulation;`<br>`lisflood.cpp:435` `simulation.run(ParFp, SimStates, Params, ParSolver, verbosemode);`<br>`lisflood.cpp:436` `}`<br>`lisflood.cpp:437` `else if (Statesptr->acceleration == ON)`<br>`lisflood.cpp:438` `{`<br>`lisflood.cpp:439` `lis::cuda::acc::Simulation simulation;` ``<br>후: `` `lisflood.cpp:427` `else if (Statesptr->fv2 == ON)`<br>`lisflood.cpp:428` `{`<br>`lisflood.cpp:429` `lis::cuda::fv2::Simulation simulation;`<br>`lisflood.cpp:430` `simulation.run(ParFp, SimStates, Params, ParSolver, verbosemode);`<br>`lisflood.cpp:431` `}` `` | 현재 lisflood.cpp:427–431이 FV2 분기이다. 기존 인용 :433–439는 DG2·ACC 분기이다. LI1-226 최종 이유도 :427–430으로 정정하도록 적는다. |

## 기계 확인 후보 판정

사용자가 제시한 후보 순서대로 기록한다.

`v8.2:` 원문은 지정된 이전 배포본의 `external/v8.2/LISFLOOD-FP/`에서 열었다. 반복된 후보를 합치지 않았다.

| 순서 | 후보 | 판정 |
|---:|---|---|
| 1 | `cuda_solver.cuh:2` `CUDA_BLOCK_SIZE_X/Y=16` | 유지. 노트 61행은 :2–4를 인용한다. 원문 :2는 X=16, :3은 Y=16, :4는 BLOCK_SIZE=256이다. X/Y는 두 매크로를 묶은 설명이다. |
| 2 | `v8.2:cuda/cuda_max_field.cu:97` `maxH = GhostRaster::allocate_pinned_H(geometry); //// change to allocate_pinned_` | 유지. 원문 97행과 코드가 같다. 후보는 뒤쪽 주석을 중간에서 자른 것이다. |
| 3 | `v8.2:cuda/fv1/cuda_fv1_solver.cu:361` `if (threadIdx.x == 0) continue;` | 유지. v8.2의 361행과 정확히 일치한다. 현재 8.3의 lane 조건과 구분되어 있다. |
| 4 | `v8.2:cuda/cuda_max_field.cu:97` `maxH = GhostRaster::allocate_pinned_H(geometry); //// change to allocate_pinned_` | 유지. 2번과 같은 중복 후보이다. 원문 97행과 코드가 같다. |
| 5 | `v8.2:cuda/cuda_max_field.cu:97` `maxH = GhostRaster::allocate_pinned_H(geometry);` | 유지. 원문의 실행문 전체이다. 뒤의 주석을 제외한 인용이다. |
| 6 | `v8.2:cuda/cuda_max_field.cu:96` `if (acceleration) {` | 유지. 원문 96행과 정확히 일치한다. |
| 7 | `v8.2:cuda/cuda_max_field.cu:97` `maxH = GhostRaster::allocate_pinned_H(geometry); //// change to allocate_pinned_` | 유지. 2·4번과 같은 중복 후보이다. 원문 97행과 코드가 같다. |
| 8 | `v8.2:cuda/cuda_max_field.cu:98` `totalHtm = GhostRaster::allocate_pinned_H(geometry);` | 유지. 원문 98행과 정확히 일치한다. |
| 9 | `v8.2:cuda/cuda_max_field.cu:99` `maxHtm = GhostRaster::allocate_pinned_H(geometry);` | 유지. 원문 99행과 정확히 일치한다. |
| 10 | `v8.2:cuda/cuda_max_field.cu:100` `initHtm = GhostRaster::allocate_pinned_H(geometry);` | 유지. 원문 100행과 정확히 일치한다. |
| 11 | `v8.2:cuda/cuda_max_field.cu:101` `}` | 유지. 원문 101행과 정확히 일치한다. |
| 12 | `v8.2:cuda/cuda_max_field.cu:102` `else {` | 유지. 원문 102행과 정확히 일치한다. |
| 13 | `v8.2:cuda/cuda_max_field.cu:103` `maxH = GhostRaster::allocate_pinned(geometry); //// change to allocate_pinned_H(` | 유지. 원문 103행과 실행문이 같다. 원문 주석의 끝은 `allocate_pinned_H()`이다. |
| 14 | `v8.2:cuda/cuda_max_field.cu:104` `totalHtm = GhostRaster::allocate_pinned(geometry);` | 유지. 원문 104행과 정확히 일치한다. |
| 15 | `v8.2:cuda/cuda_max_field.cu:105` `maxHtm = GhostRaster::allocate_pinned(geometry);` | 유지. 원문 105행과 정확히 일치한다. |
| 16 | `v8.2:cuda/cuda_max_field.cu:106` `initHtm = GhostRaster::allocate_pinned(geometry);` | 유지. 원문 106행과 정확히 일치한다. |

## 근거 파일과 쪽 이미지

- `파일:N`은 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/`를 기준으로 한다. 배포본 문서·패치는 인접한 `LISFLOOD-FP-8.3-package/`를 기준으로 한다.
- 과거 코드는 사용자가 지정한 v8.0·v8.1·v8.2 추출본에서 열었다. 반영 전 노트는 지정 커밋 `bf804e23`에서 읽었다.
- PDF 이미지: `lf-manual-pdf-001.png`, p.15–22, p.32, p.35–39.
- DOCX 이미지: `lf-manual-docx-001.png`, p.5, p.22–24, p.37, p.40–44.
- 교량 DOCX 이미지: `lf-manual-bridge-docx-001.png`, p.21–24, p.35, p.38.
- 이미지 파일은 사용자가 지정한 `scratchpad/lfpages/`의 파일이다. 식·수치·표의 판정에는 이미지를 사용했다.
- [최종 분류 배정표](../assign/LISFLOOD-FP-final-conclusions.tsv), [노트 배정표](../assign/LISFLOOD-FP-note-job-3.tsv), [노트 반영 기록](LISFLOOD-FP-notes-apply-3.md)을 대조했다.
- 최종 결론: [LB1b](../compare/LISFLOOD-FP-conclusion-verify-LB1b.md), [LN1](../compare/LISFLOOD-FP-conclusion-verify-LN1.md), [RF](../compare/LISFLOOD-FP-conclusion-verify-RF.md), [LG2](../compare/LISFLOOD-FP-conclusion-verify-LG2.md), [LG1](../compare/LISFLOOD-FP-conclusion-verify-LG1.md), [LV1](../compare/LISFLOOD-FP-conclusion-verify-LV1.md), [LI2](../compare/LISFLOOD-FP-conclusion-verify-LI2.md), [LI1](../compare/LISFLOOD-FP-conclusion-verify-LI1.md), [LT1](../compare/LISFLOOD-FP-conclusion-verify-LT1.md), [Claude 최종 조정](../compare/LISFLOOD-FP-conclusion-claude-final.md)을 대조했다.
- [외부 근거 기록](../compare/LISFLOOD-FP-external-sources.md)의 마지막 절도 확인했다. 그 절의 LI2-203·LB1-235는 이 노트의 배정 행이 아니다.
- 수정안: [교량 DOCX](../compare/lisflood-bridge-docx-vs-code.md#4-노트-대조와-수정안), [빌드·8.3](../compare/lisflood-build-83-vs-code.md#4-노트-대조와-수정안), [DOCX](../compare/lisflood-docx-manual-vs-code.md#4-노트-대조와-수정안), [입출력](../compare/lisflood-files-output-vs-code.md#4-노트-대조와-수정안), [입력](../compare/lisflood-par-vs-code.md#4-노트-대조와-수정안), [이론](../compare/lisflood-theory-vs-code.md#4-노트-대조와-수정안), [SWE](../compare/lisflood-cpu-gpu-swe.md#4-노트-대조와-수정안), [ACC·adaptive](../compare/lisflood-cpu-gpu-acc-adaptive.md#42-cuda-노트)를 대조했다.
- [실행 흐름 보고서](LISFLOOD-FP-callflow.md)의 §4·§6·§8.1과 [판 대조 기록](../compare/LISFLOOD-FP-version-verify-AD1.md)의 문서 판 근거를 대조했다.
