# Celeris 노트 전수 검증 9

- 대상: `models/Celeris/source-analysis/celeris-pipeline-graph.md`.
- 범위: 검증 시작 시 `git diff -U0 HEAD -- models/Celeris/source-analysis/celeris-pipeline-graph.md`의 모든 추가 줄. Frontmatter와 빈 줄을 포함한다.
- 상태: 완료.
- 기계 확인 후보: 사용자 제공 후보 없음.

## celeris-pipeline-graph.md

- 대상 노트: [celeris-pipeline-graph.md](../../../models/Celeris/source-analysis/celeris-pipeline-graph.md).
- 대조한 줄 수: 시작 시점 diff의 추가 줄 205줄이다. Frontmatter 2줄과 빈 줄을 포함한다.
- 대상 줄: `5–6,14,32–34,47,53,80,82,90,98–102,126–129,145–146,154,167–182,187,195–359`.
- 정정 수: 6곳이다. 정정 표식이 있는 서로 다른 노트 줄을 셌다.
- 보완 수: 1곳이다. 보완 표식이 있는 서로 다른 노트 줄을 셌다.
- 이번 수정은 모두 기존 한 줄 안에서 이루어졌다. 검증 시작 시점과 완료 시점의 줄 번호는 같다.
- 미해결 항목: 없음.

### 대상 줄 전체 대조 기록

코드 경로는 `models/Celeris/raw/source_code/Celeris-WebGPU/` 기준이다. 현재 판은 사용자가 지정한 `ebca435`다. 이전 판은 해당 커밋의 파일을 `git show`로 열었다. 반영 전 노트는 `d8157c80`의 파일을 열었다.

| 노트 줄 | 대조 근거 | 판정 |
|---|---|---|
| 5–6 | `Celeris-notes-apply-9.md`의 해당 노트 절과 frontmatter 기록, `CONVENTIONS.md`의 인용 상태 규칙 | recovery 반영 날짜와 방법을 유지했다. 기존 검증 상태를 새로 승격하지 않았다. |
| 14 | `celeris-docs-architecture-vs-code.md` §1의 전체 커밋 해시·날짜, 판 검증 기록 | 본판 표기를 유지했다. |
| 32–34 | `js/main.js:2224–2229,2294–2334,2495–2498,2614–2631,4675`; 최종 CD1-1302·1334 | 시간식·엄격한 초과 조건·UI 갱신·중간 강도를 유지했다. 전체 frame_count와 UI 이후 카운터를 구별했다. |
| 47,53 | `js/main.js:1539–1550,2649,2678–2683`; `shaders/Pass2.wgsl:36–41`; callflow §6의 RF-013·pipeline 단계 | HLL/HLLC 구별과 현재 NLSW 호출 줄을 유지했다. |
| 80,82,154 | `js/main.js:2900–2907`; callflow §6의 state swap 수정안 | 상태 복사 용어와 복사 방향을 유지했다. |
| 90 | `js/main.js:2930–2931,2980,3033,3512–3518`; 최종 CD1-1336 | 시간 반복 밖의 프레임 처리 설명을 유지했다. |
| 98–102 | `js/main.js:1539–1551`; `transect_version/js/main.js:1033–1045`; `transect_version/shaders/Pass2_HighOrder.wgsl:191`; transect 제출 함수와 solver 원문; CT1-357 수정안 | 본판과 transect의 고차 flux·제출·y PCR 구별을 유지했다. 빈 줄도 확인했다. |
| 126–129 | `js/main.js:2247–2281,2672–2679,2757–2865`; Tavakkol 2017 p.3 이미지 §2.3·식 (16)·(19); CP1-156·CP2-167 수정안 | 한 번의 보정과 render_step/dt 구별을 유지했다. 논문의 첫 두 단계 Euler·반복 보정·F* 증분을 현재 경로와 구별했다. |
| 145–146 | `shaders/Pass_Breaking.wgsl:55`; `shaders/Pass3B_COULWAVE.wgsl:191`; `shaders/Pass3_Bous.wgsl:427`; `shaders/Pass2.wgsl:141–145`; `js/main.js:2649–2685,2783–2815,2895–2901`; 최종 RF-015 | 예측·보정 입력 시점과 첫 시간단계 예외를 유지했다. |
| 167–182 | `js/main.js:2638–2928,2980,3033,3515`; `js/Run_Tridiag_Solver.js:37–91`; Handler 파일과 main.js의 바인딩·파이프라인 연결 | Pass1 보정 조건과 처방 지형 시간 상한을 정정했다. 나머지 호출 위치를 유지했다. |
| 187 | `js/Run_Compute_Shader.js:38–52,78–89` | 두 복사 함수의 위치와 copyTextureToTexture 설명을 유지했다. |
| 195–204,237–240,278–280,319–326 | callflow §4·「Claude 렌더 확인 (11-04)」; 반영 기록; 최종 근거의 판·AI 분석 구별 | 절 제목·빈 줄·렌더 확인 기록·표 머리글·인용 기준을 확인했다. |
| 205–236 | callflow §4.1; `index.html:1597`; `js/main.js`의 시작·초기화·프레임·출력 호출과 각 피호출 함수 진입점 | 첫 Mermaid 블록 전체가 원본과 글자 단위로 같다. 상자의 코드 위치도 열어 확인했다. |
| 241–277 | callflow §4.2; `js/main.js:1539–1550,2638–2928`; `js/Run_Tridiag_Solver.js:37–91`; 해당 WGSL 진입점 | 둘째 Mermaid 블록 전체가 원본과 글자 단위로 같다. 반복 조건과 복사 방향을 확인했다. |
| 281–318 | callflow §4.3; `js/main.js:1558–1593,2638–2928`; `js/Run_Tridiag_Solver.js:37–91`; 해당 WGSL 진입점 | 셋째 Mermaid 블록 전체가 원본과 글자 단위로 같다. 모델·퇴적물 분기와 셰이더 선택을 확인했다. |
| 327–359 | 아래의 최종 결론 대조표, 각 행의 현재 코드·문서·과거 커밋·논문 이미지 | 차이 표 33행을 모두 대조했다. 설명의 인용 표기 3행과 보고서 내부 식별자 2행을 수정했다. |

### 차이 표 33행의 최종 근거 대조

최종 분류는 `Celeris-final-conclusions.tsv` 및 각 `Celeris-conclusion-verify-*.md`의 해당 행과 같다. 결론 문장은 최종 근거와 같다. 판 이름 추가와 코드 경로의 표기 정규화는 별도로 구별했다. 아래 표의 행 수 합계는 33행이다.

| 최종 근거 파일 | 대조한 행 ID | 결과 |
|---|---|---|
| `Celeris-conclusion-verify-CD1a.md` | CD1-139, CD1-140 | 통계·캐시·점 시계열의 반복 위치와 일시정지 조건이 같다. `984091f`의 문서·호스트도 열었다. |
| `Celeris-conclusion-verify-CD1c.md` | CD1-490 | 시간단계 진단과 프레임 캐시 구별이 같다. `afc1fe7`의 문서·호스트도 열었다. |
| `Celeris-conclusion-verify-CD1e.md` | CD1-868 | setRenderStep 초기화 대입문과 자동 조정 조건이 같다. |
| `Celeris-conclusion-verify-CD1f.md` | CD1-886, CD1-887, CD1-921, CD1-1019, CD1-1020 | 초기화·절대 시각·HTML 선택값이 같다. CD1-921의 설명 표기를 정정했다. |
| `Celeris-conclusion-verify-CD1h.md` | CD1-1238, CD1-1302, CD1-1308, CD1-1334, CD1-1336, CD1-1390 | HTML value 부재·시계 재계산·시간적분·프레임 처리·바닥 시간 제한이 같다. CD1-1302·1390의 설명 표기를 정정했다. |
| `Celeris-conclusion-verify-CD2.md` | CD2-454, CD2-460, CD2-463 | 퇴적물 이후 계수 갱신·설정 기반 dt·GPU 대기 조건이 같다. `f6fd78b`와 반영 전 노트도 열었다. |
| `Celeris-conclusion-verify-CP3RF.md` | RF-005, RF-015, RF-019, CP3-041, CP3-084, CP3-099, CP3-108, CP3-116 | 보정 횟수·도함수 시점·Fig.1 생략·추가 스킴·출력 판·제출·대기 조건이 같다. 관련 이전 커밋도 열었다. |
| `Celeris-conclusion-verify-CP1.md` | CP1-039, CP1-040 | 2017 구현과 현재 WebGPU의 보정·시작 단계 차이가 같다. `6f1272f`의 셰이더도 열었다. |
| `Celeris-conclusion-verify-CP2.md` | CP2-043, CP2-045, CP2-055, CP2-138, CP2-158 | Unity 구조·NLSW 적분·경계·프레임 반복 구별이 같다. CP2-055의 직접 인용을 보완했다. CP2-138의 보고서 내부 참조를 정정했다. |

차이 표의 분류를 직접 세면 A 7행, B 8행, C 17행, E 1행이다. A 행의 문서 판과 근거 커밋은 `Celeris-version-verify-AD1.md`·`AD2.md`와 대조했다. CP3-099의 `bb99fee` 경계·단일 출력과 `c4be488` 복수 출력을 해당 판의 원문으로 구별했다. 논문 게재일은 Lynett 2026 p.1 이미지에서 확인했다.

E 행 CD1-1302는 `Celeris-version-verify-E1.md`와도 대조했다. 강도는 중간이다. Courant UI와 dt 갱신은 현재 호출되는 경로다. 따라서 이 행에 「호출되지 않는 경로」를 붙이지 않았다. `Celeris-external-sources.md`의 「최종」 절에는 이 노트의 배정 행에 해당하는 결론이 없다.

논문은 제공된 쪽 이미지 7개를 직접 열었다. 대상 이미지는 Tavakkol 2017 p.1·3, Tavakkol 2020 p.4·6, Lynett 2026 p.1·4·5다. 시간적분 식·계수·처음 두 단계·UML·Fig.1·게재일은 이 이미지로 판정했다.

### 정정·보완 목록

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `models/Celeris/source-analysis/celeris-pipeline-graph.md:168` | 정정 | Pass1의 세 호출을 「항상」으로 묶음 → 예측·말미 진단과 조건부 보정 호출을 구별함 | `js/main.js:2757`의 `if (calc_constants.timeScheme == 2)` 안에 2775행 호출이 있다. 2641·2913행은 이 보정 조건 밖에 있다. |
| `models/Celeris/source-analysis/celeris-pipeline-graph.md:176` | 정정 | `disturbanceType==5`만 표시 → 시간 상한을 포함한 원문 조건을 표시함 | `js/main.js:2739`의 `if(calc_constants.disturbanceType == 5 && total_time <= 1.0e5 * calc_constants.dt)` 안에 2741행 호출이 있다. 최종 CD1-1390도 같은 조건을 적는다. |
| `models/Celeris/source-analysis/celeris-pipeline-graph.md:336` | 정정 | 「대상 8문서:구체식·검사 없음」「경계 시계열의 절대 시간」을 백틱 인용으로 표시 → 설명임을 밝히고 백틱을 제거함 | `docs/architecture/CONFIGURATION.md:53`은 공유 시간벡터를 설명한다. `docs/architecture/DATA_AND_TEXTURES.md:117–121`은 텍스처·보간을 설명한다. `js/File_Loader.js:458`은 `calc_constants.start_time_shift = 0.0;`다. 506행은 `calc_constants.start_time_shift = sharedTimes[0];`다. 한국어 항목명은 문서 원문이 아니다. |
| `models/Celeris/source-analysis/celeris-pipeline-graph.md:340` | 정정 | 「대상 문서·현재 코드:호출·조건 교차대조」「시간간격 UI 변경과 전체 모의 시간」을 백틱 인용으로 표시 → 호출·조건 대조 설명임을 명시함 | 최종 CD1-1302는 코드 경로를 교차 대조한 AI 결론이다. `js/main.js:2331`은 Courant 기반 dt 대입이다. 2624행은 `total_time = frame_count * calc_constants.dt + calc_constants.start_time_shift;`다. 한국어 항목명은 원문 인용이 아니다. |
| `models/Celeris/source-analysis/celeris-pipeline-graph.md:344` | 정정 | 「대상 8문서:구체식·분기 상세 없음」「이동 바닥 적용 시간 제한」을 백틱 인용으로 표시 → 해당 문장 부재를 나타내는 설명으로 바꿈 | 최종 CD1-1390은 문서에 호출 상한과 시간 고정 설명이 없다고 판정한다. `js/main.js:2739`는 호출 상한을 둔다. `shaders/AddDisturbance.wgsl:109–110`은 `if (time_local > 1.0e5*dt)`일 때 `time_local = 1.0e5*dt;`를 대입한다. |
| `models/Celeris/source-analysis/celeris-pipeline-graph.md:357` | 보완 | 보고서 내부 식별자 「N2·N9」와 Boussinesq 참조만 표시 → NLSW 우변·적분식의 직접 인용을 추가함 | `shaders/Pass3_NLSW.wgsl:250`의 `let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx + (yflux_south - yflux_here) * globals.one_over_dy + source_term + vorticity_dissipation;`와 261행의 `newState = in_state_here_UV + globals.dt / 12.0 * (23.0 * d_by_dt - 16.0 * oldies + 5.0 * oldOldies);`를 추가했다. 최종 CP2-055의 직접 근거 보완을 반영했다. |
| `models/Celeris/source-analysis/celeris-pipeline-graph.md:358` | 정정 | 「:2728–2730 아래 C10」 → 둘째 경계의 실제 조건·호출 위치를 명시함 | `js/main.js:2728`의 `if (calc_constants.NLSW_or_Bous > 0) {` 안에서 2729행이 `BoundaryPass_BindGroup_NewState`로 호출한다. 보정의 대응 호출은 2824·2858행이다. 이 노트의 그림 C10은 SedTrans_Pass3이므로 기존 참조는 맞지 않는다. |

각 수정 줄에 지정된 전수 검증 표식을 붙였다. 차이 표 행의 표식은 결론 문장 칸 끝에 붙였다.

### 기계 확인 후보와 마감 검사

- 사용자 제공 기계 확인 후보: 없음.
- 추가 자동 점검: 수정 전 표에서 인접한 `파일:줄`과 백틱 원문 쌍 247개를 추출했다. 파일을 직접 열어 대조한 결과 불일치는 0개였다. 인용 범위의 일부 발췌와 과거 노트 안의 코드 인용은 문맥을 별도로 대조했다.
- 설명을 백틱으로 감싼 CD1-921·1302·1390은 파일 인용 쌍 검사의 대상이 아니었다. 수동 대조에서 원문 인용이 아닌 것으로 판정하여 정정했다.
- 차이 표 33행의 분류·결론 문장을 수정 후 다시 비교했다. 최종 근거와의 불일치는 없다.
- Mermaid 블록 3개를 수정 후 다시 비교했다. callflow §4의 블록과 모두 글자 단위로 같다. 기존 렌더 완료 문장은 callflow의 「Claude 렌더 확인 (11-04)」에 근거한다.
- 노트의 상대 링크 36개를 노트 디렉터리 기준으로 확인했다. 서로 다른 대상 파일은 12개다. 끊어진 파일 링크는 없다.
- 노트에 `/home/firesinger/`, `~/`, `[[`는 없다. 「실행하지 않았다」「확인하지 않았다」「미검수」「후속 대상」도 없다.
- 쓰기 대상은 이 결과 파일과 대상 노트뿐이다. git 쓰기 명령·sudo·모델 실행은 수행하지 않았다.
