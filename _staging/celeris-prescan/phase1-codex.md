**Celeris Phase 1 — 위키 주장 의미 검토**

대상은 pinned `f6fd78bd12af3aeeef11774a850b6b3d52be65b3` → upstream `ebca435d02b258768e0352fbaf27404f2f135799`이다. 입력 후보 13건과 추가 조사 A·B를 완료했다. 위키 본문·소스·권한은 변경하지 않았으며 문장 수정안이나 일괄 좌표 치환안은 작성하지 않았다.

**요약**

| 판정 | 건수 | ID |
|---|---:|---|
| UPDATE_REQUIRED | 6 | C1-1, C1-3, C1-4, C1-5, C1-6, C1-8 |
| REVIEW_ONLY | 2 | C1-7, C1-13 |
| NO_ACTION | 5 | C1-2, C1-9, C1-10, C1-11, C1-12 |
| UNRESOLVED | 0 | 없음 |

UPDATE의 근거는 경계 type 5가 빠진 덮어쓰기 순서, 단일 sine의 조건부 방향 보정, nested 입력의 시간 원점, timestep 말미의 nested 추출 패스, 구면 NLSW의 선택 매핑·모드 제약, 구면 격자의 dt 계산식이다. 기존 수력 패스들의 상대 순서, 세 방정식 계열이라는 수, 고정 dt 운용, 기존 텍스처들의 채널 규약은 유지된다. 세부 판정과 신구 소스 근거는 [phase1-codex.csv](phase1-codex.csv)에 있다.

여기서 `semantic_meaning_changed`는 코드가 조금이라도 바뀌었는지가 아니라 해당 인용이 뒷받침한 위키 주장에 수정할 의미가 생겼는지를 뜻한다. `REVIEW_ONLY`는 기존 주장이 유지되지만 인접한 새 조건·변형의 설명 범위를 검토할 가치가 있는 경우다. `NO_ACTION`은 의미 수정이 필요하지 않다는 판정이며 향후 snapshot 교체에 따른 인용 좌표 관리를 면제한다는 뜻은 아니다. UPDATE 행만 계약의 `reason_type`을 채웠다.

**근거의 판본과 검토 방법**

- 신구 소스의 `file:line`은 위 두 커밋의 Celeris 리포 루트 상대 경로다. old 원본은 [위키 raw snapshot](/home/firesinger/coastal-wiki/models/Celeris/raw/source_code/Celeris-WebGPU), new 원본은 [upstream checkout](/home/firesinger/.cache/coastal-snapshots/celeris-upstream)에 있다. checkout HEAD는 `ebca435`, 조사 전후 `git status --short`는 빈 출력이었다.
- 비교에 사용한 기존 파일 11개(main, Boundary handler/shader, Wave_Generator, Time_Series, constants, Pass3 handler/NLSW shader, ExtractTimeSeries handler/shader, Tridiag handler)의 위키 raw 바이트가 `git show f6fd78b:<path>`와 같음을 확인했다.
- [celeris-pipeline-graph.md](/home/firesinger/coastal-wiki/models/Celeris/source-analysis/celeris-pipeline-graph.md) 1–179행과 [celeris-source-map.md](/home/firesinger/coastal-wiki/models/Celeris/source-analysis/celeris-source-map.md) 1–201행을 전체 읽었다. 나머지 두 후보 노트는 후보가 속한 절·표와 실제 문장 전체를 대조했다. 특히 C1-2 입력의 잘린 `wiki_claim`은 CSV에 그대로 보존하되 판정에는 노트 184행 전체를 사용했다.
- hunk의 발췌만으로 판정하지 않고 실제 실행 선언·분기·호출자·피호출자를 확인했다. 주석으로 남은 옛 코드를 실행 코드로 간주하지 않았다. 이 결과는 정적 소스의 의미·구조 비교이며 브라우저 GPU 실행이나 수치 타당성 검증 결과가 아니다.

기계 매핑이 실패한 네 건은 다음과 같이 직접 재정박했다.

| ID | old | 확인한 new 실행 근거 |
|---|---|---|
| C1-2 | `js/Handler_BoundaryPass.js:100-147` | 함수 전체 `140-206`; state 입력 `150-152`, 출력 `166-180`. `138`은 옛 signature 주석이다. |
| C1-4 | `js/main.js:1881` | 실행 시간식 `2624`; `2622`는 옛 식 주석이다. |
| C1-8 | `js/main.js:1614` | `2294-2333`의 조건부 블록, spherical 대입 `2328`, Cartesian 대입 `2331`. 하나의 새 행으로 매핑하면 분기를 잃는다. |
| C1-13 | `js/Time_Series.js:58-115` | 함수 전체 `60-128`; epoch 검사는 `108-111`, push는 `114-118`. `58`은 옛 signature 주석이다. |

**A. NEW FILE RULE — 분리·이동 여부**

지정된 네 파일 중 기존 파일에서 기능을 제거하여 새 파일로 옮긴 경우는 확인되지 않았다. 다만 새 파일이라는 사실과 코드가 처음부터 독립 작성됐다는 주장은 다르다. 구면 shader는 기존 NLSW의 상당 부분을 재사용한 추가 변형이고, 새 handler는 기존 handler들과 공통 형식의 바인딩 코드를 쓴다.

| 파일 | 도입 커밋 | 판정 |
|---|---|---|
| `shaders/Pass3_NLSW_Spherical.wgsl` | `afc1fe7` | 기존 NLSW 골격을 재사용한 신규 구면 solver 변형. 기존 Cartesian 파일의 이동·대체가 아니다. |
| `js/Handler_ExtractNestedBoundaryTimeSeries.js` | `bb99fee` | 신규 rectangle 경계 출력 패스의 바인딩. 기존 point-series/PCR handler의 기능 이동이 아니다. |
| `shaders/ExtractNestedBoundaryTimeSeries.wgsl` | `bb99fee` | 신규 rectangle 네 변 시계열 추출 기능. 기존 point-series 추출을 옮긴 것이 아니다. |
| `js/agent_controls.js` | `0ee5174` | 기존 UI 함수를 호출하는 신규 agent 명령·상태 인터페이스. 수치 커널이나 main 오케스트레이터의 분리·이동이 아니다. |

구면 NLSW는 old `shaders/Pass3_NLSW.wgsl:41-64,67-93,253-265,282-285`의 바인딩 골격·마찰 계산·적분계수·출력 형태를 new 파일 `43-66,73-90,234-244,262-265`에서 재사용한다. 동시에 `151-178`의 구면 metric·압력 구배, `205-232`의 곡률·Coriolis·구면 flux divergence가 새 계산 경로를 만든다. `git diff --find-copies=40% --find-copies-harder --name-status f6fd78b ebca435 -- js shaders`는 이 파일을 기존 NLSW의 `C052` 유사 복사로 표시한다. 이는 보조 유사도 근거이며, 실제로 기존 `Pass3_NLSW.wgsl`은 양 커밋의 blob `7d183bc7ad974b4b5914368ff15768f2421b4ba8`이 동일하고 new `js/main.js:1562`에서 계속 선택된다. 따라서 기존 Cartesian NLSW 인용의 근거 위치가 빠져나간 것이 아니다. 위키 영향은 source-map `19-25,35,105,156`의 모드·파일 선택 범위다.

새 nested handler의 `4-67`은 uniform 0, 입력 state 1, 네 출력 2–5, bottom 6의 layout을 정의하고 `71-108`이 resources를 연결한다. new `js/main.js:2153`은 state 자리에 `txNewState`를 넘긴다. 같은 copy 탐지 명령은 handler를 `Handler_Tridiag.js`와 `C043`으로 연결하지만, 이는 반복적인 바인딩 문법의 유사성이다. `Handler_Tridiag.js`는 두 판본에서 같은 blob이며 새 파일은 PCR 계수나 solve를 수행하지 않는다. 기존 `Handler_ExtractTimeSeries.js`도 같은 blob이고 계속 사용된다. 두 기존 핸들러 인용에 대한 로직 유출은 없다.

새 nested shader는 `23-33`에서 state의 eta/hu/hv를 읽고 수심이 0 이하이면 0을 내보낸다. `36-50`은 `workgroup_size(16,1)`로 rectangle의 네 변을 각각 `(station_index, sample_index)`에 기록한다. 기존 `shaders/ExtractTimeSeries.wgsl:25-63`의 `workgroup_size(1,1)`, tooltip·개별 probe, `(time,eta,P,Q)` 1D 출력과 목적·레이아웃이 다르다. 기존 shader의 양 판본 blob `25864f0f014ed562499ea6173b638df99919eefd`는 동일하며 new `main.js:3515`에서 여전히 dispatch한다. source-map `77,127,169`의 기존 point-series 설명과 infrastructure `234-238`은 이 신규 기능 때문에 무효가 되지 않는다.

agent controls는 `274-286`에서 main의 `updateCalcConstants`, `updateAllUIElements`, `runExample` 등의 콜백을 받아 `346-385,519-569` 등에서 호출하고, `719-781`에서 명령을 라우팅한다. `820-923`의 `window.CelerisAgentControls` API와 `931-948`의 message 인터페이스는 신규다. main은 `46`에서 import, `4785-4823`에서 설치하며 기존 UI 함수는 old/new 각각 `updateCalcConstants 3567/4602`, `setupDropdownListeners 3599/4634`, `updateAllUIElements 3617/4652`에 남는다. 도입 커밋 `0ee5174`의 main diff에도 이 함수들을 삭제해 agent 파일로 옮긴 블록은 없다. source-map `55`의 main 역할 및 `145`의 main/handler 책임 분리는 유지되고, 파일 인벤토리 `51-89`에는 새 모듈이 빠져 있다. CelerisAgent의 부속 런타임·서비스 내부까지 조사 범위를 확장하지 않았다.

네 파일의 도입 커밋은 `git show --name-status <commit> -- <file>`에서 각각 `A`로 확인했다. pinned `js/`·`shaders/`에서 spherical metric/새 solver, nested 추출, agent 명령 인터페이스 식별자를 `git grep`한 결과는 모두 0건이었다. 식별자 부재만으로 판정하지 않고 위의 기존 파일 보존·실제 데이터 흐름과 함께 사용했다.

**B. 파이프라인 구조와 두 노트의 서술 차이**

패스 구성은 확장됐다. 구면 solver는 기존 Pass3 슬롯의 선택 변형이고, nested 경계 출력은 timestep 말미에 추가되는 조건부 compute 패스다. 기존 Cartesian 수력 패스들의 dispatch 순서는 유지된다.

그 근거로 아래 구간을 `git show`로 읽고 CRLF/LF를 정규화한 뒤 줄별 비교했다.

| old `js/main.js` | new `js/main.js` | 결과 |
|---|---|---|
| `1893-2144` | `2638-2889` | 동일. predictor, corrector, 선택적 CW/Sed, 경계/PCR와 Sed bottom 처리까지의 코드·순서가 유지된다. |
| `2145-2178` | `2895-2928` | 동일. gradient/state shift와 Pass1·CalcMeans·CalcWaveHeight의 순서가 유지된다. |

nested 입력은 `main.js:2629-2631`에서 현재 시각과 type-5 시간 보간 bracket을 갱신한다. `382-386`을 보면 이 helper는 uniform 값을 설정하며 별도 GPU dispatch가 아니다. 실제 경계 처리는 기존 BoundaryPass 호출 위치를 유지한 채 shader 내부에 type-5 분기(`shaders/BoundaryPass.wgsl:515-547`)를 추가했다.

nested 출력은 `main.js:2604-2607`의 trigger 때 rectangle별 텍스처·uniform·bind group을 만든다(`2089-2154`). 매 timestep에는 아래 흐름이 된다.

```text
기존 predictor [+ timeScheme==2이면 corrector]
→ [Sed] bottom / near-dry / 필요한 UpdateTrid                 main:2877-2888
→ [active rectangle & 표본 시각 도달] nested 경계 추출         main:2893 → 2181-2196
→ gradient history shift / state swap                       main:2895-2907
→ Pass1 / CalcMeans / CalcWaveHeight / submit                main:2913-2928
프레임 compute 루프 종료
→ [완료 출력 존재 & 활성 sampling 없음] readback/download      main:2951-2976
→ Copytxf32_txf16                                            main:2980
→ render pass                                               main:3033,3461-3464
→ 기존 ExtractTimeSeries                                    main:3515
```

추출의 실제 조건은 `state.active`, `sampleIndex < sampleCount`, `currentTime + 0.5*dt >= startTime + sampleIndex*outputDt`다(`main.js:2183-2196`). 따라서 모든 timestep에 항상 추가 dispatch하는 것으로 해석하면 안 된다. 각 rectangle은 독립 상태·sample clock을 가지며 완료 시 `pendingDownload`가 된다(`2201-2208`). CPU readback은 다른 rectangle이 아직 active이면 미뤄지고, GPU에 표본을 저장하는 패스 자체는 각 rectangle의 시각에 수행된다.

구면 solver는 `constants_load_calc.js:454-469`에서 NLSW·표준 재구성 경로로 제한하고 Sed 및 Cartesian breaking을 비활성화한다. `main.js:1558-1563`에서 구면 WGSL을 고르며 `1626`에서 기존 `Pass3_Pipeline_NLSW`를 생성한다. dispatch는 predictor `2678-2683`, corrector `2811-2816`의 원래 NLSW 분기다. 새 Pass3가 한 번 더 실행되는 구조가 아니다. `Run_Tridiag_Solver.js`도 같은 blob이며 NLSW의 `37-39` copy 단락을 유지한다.

Pass3 handler/layout도 그대로다. 달라진 부분은 `main.js:1078`이 binding 19의 자리에 spherical이면 `txSphericalMetrics`를 공급하고 `1119`에서 shared uniform tail에 `one_over_R`를 쓰는 것이다. 새 shader는 `65,151-157`에서 metric을 읽는다. metric은 `js/Copy_Data_to_Textures.js:351-381`에서 CPU 계산·업로드하므로 별도 metric compute pass가 늘어난 것은 아니다.

아래는 문장 수정안이 아닌, 현재 서술이 놓치는 내용과 그 위치다. 후보 13건 밖 위치는 CSV 행으로 추가하지 않았다.

| 노트 위치 | 현재 서술과 new 소스의 차이 | 처리 연결 |
|---|---|---|
| pipeline-graph `69-84`, 특히 `73→74` | Sed 처리에서 history shift로 곧바로 이어지는 전체 후처리 그래프가 활성 nested 추출을 누락한다. new `main:2893,2181-2196`. | C1-5 UPDATE_REQUIRED |
| pipeline-graph `86` | timestep 루프 이후를 f16→render→point-series로 요약한다. 그 세 패스의 상대 순서는 맞지만 완료 nested 출력의 readback/download가 f16 앞에 조건부로 들어왔다. new `main:2951-2980`. | B 별도 발견: 조건부 프레임 작업 누락 |
| pipeline-graph `90-107`의 모드 설명·표 | `NLSW_or_Bous`와 `Accuracy_mode`만으로는 `grid_type==2`의 shader 선택·강제 NLSW/Accuracy/Sed/Breaking 제약을 설명하지 못한다. 단, `98`의 NLSW pipeline 이름·PCR skip, `103`의 공통 layout은 유지된다. | B 별도 발견; C1-6 관련 |
| pipeline-graph `148` | 모든 handler가 초기화 시 1회 호출된다는 일반화는 새 nested bind group에 맞지 않는다. new `main:2605-2606`에서 출력 trigger를 처리하면서 `2089-2154`에서 rectangle별 생성한다. pipeline 생성은 여전히 초기화 때 한다. | B 별도 발견: bind-group 생성 시점 예외 |
| pipeline-graph `150-167` | handler/dispatch 표에 nested 추출 handler와 `main:2893 → 2196` 경로가 없다. 기존 행이 다른 파일로 이동한 것은 아니다. | B 별도 발견: 새 패스 대응 누락 |
| source-map `19-25`의 선택 설명·NLSW 행 | `23`은 활성 NLSW 파일을 Cartesian 하나로 적는다. new `main:1558-1563`은 구면 파일도 고르고 constants `454-469`는 가능한 모드를 제한한다. 3개 계열이라는 수는 유지된다. | C1-6 UPDATE_REQUIRED |
| source-map `27-39`, 특히 `35` | 수력 연산의 상대 순서는 유지된다. 다만 구체 Pass3 파일 목록에는 spherical 변형이 빠졌다. nested 추출은 이 축약 수력 골격 이후 작업이므로 hunk 겹침으로 골격 자체를 UPDATE하지 않았다. | C1-7 REVIEW_ONLY; B에서 파일 목록 누락 지목 |
| source-map `51-89`, `95-137`, `147-171` | 인벤토리와 대응표에 새 agent module, nested handler/shader, spherical shader가 없다. 특히 `105,156`의 NLSW 파일 매핑에는 변형이 빠졌다. `55`의 main 오케스트레이터 역할 및 `91,145`의 handler/pipeline 책임 분리는 유지된다. | A·B 별도 발견; C1-9/10은 NO_ACTION |
| pipeline-graph `30`; source-map `57` | 시간식은 nonzero nested 시작 시각에 달라지고 dt 공식은 spherical의 물리 간격을 사용한다. 기존의 per-step 적응 CFL 부재는 유지된다. | C1-4·C1-8 UPDATE_REQUIRED |

source-map `179-193`은 텍스처 규약의 ‘요약(브리프)’이다. old `main:341-426` 대비 new `449-536`에는 metric 할당 `508-509`만 추가됐고 기존 표의 항목은 그대로다. infrastructure `37-135`가 설명한 텍스처 할당도 old `341-456` 대비 new `449-576`에서 metric과 네 boundary input texture의 추가 이외에 바뀌지 않았다. 새 항목의 설명을 보강할 편집 결정과 기존 인용의 의미 변경을 구분하여 C1-11/12는 NO_ACTION으로 판정했다.

**시계열 수정에 대한 경계 판단 — C1-13**

버그 수정의 실질은 확인된다. `Time_Series.js:108-111`은 reset 이전 epoch의 비동기 readback을 버리고, reset은 `main.js:3483-3486,3506-3509`에서 동기로 수행된다. ordinary point gauge는 로컬 경과시간, type-5 nested gauge는 total_time을 쓴다(`main.js:1730-1733,3494-3496`). 다만 노트 `238`은 256B 복사·mapAsync·time/eta/P/Q 저장·텍스트 출력·1초 chart 갱신을 설명하며 reset 위치나 모든 readback의 무조건 저장, 시간 원점 0을 보장하지 않는다. 이 핵심은 유지되므로 자동으로 BUGFIX_AFFECTING_DOC를 부여하지 않았다. 경합 방지·nested 시각에 대한 설명 확장 여부는 REVIEW_ONLY로 남긴다.

**변경 전부터 존재한 관련 서술 — 별도 보고**

pipeline-graph `30`의 ‘프레임 시작 시 await ... 로 큐 플러시’는 매 프레임 무조건 대기한다는 뜻으로 읽으면 정확하지 않다. old `main.js:1542-1548`와 new `2224-2230` 모두 `nowFlush - lastGpuSyncTime > 600000` 조건 안에서 기다린다. 이는 이번 upstream 변경으로 생긴 차이가 아니며 C1-4의 UPDATE 근거에는 포함하지 않았다.

**UNRESOLVED**

없음. 13건과 A·B의 결론을 로컬 신구 소스·git 이력에서 확인했다. 신규 파일의 공통 코드 재사용은 이동과 구분해 적었고, 코드 유사도만으로 작성 경위나 알고리즘의 독립 창작을 단정하지 않았다.

**산출물 검증**

CSV는 입력의 13개 ID와 note/note_line/wiki_claim을 보존하고 요청된 11개 열을 갖는다. 네 REANCHOR 항목은 실행 코드의 새 위치를 제시했다. UPDATE 6건에는 계약에 열거된 reason_type을 기입했고 나머지는 빈 값으로 두었다. A의 4파일과 B의 두 노트에 대한 추가 발견은 이 보고서에만 기록했다. 작업 지시의 STOP CONDITION에 따라 여기서 종료한다.
