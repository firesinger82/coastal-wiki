# FUNWAVE 노트 전수 검증 4

대상 노트: [funwave-infrastructure.md](../../../models/FUNWAVE/source-analysis/funwave-infrastructure.md).

작업 상태: 완료.

## 대상 줄 확정

작업 시작 시 `git diff -U0 HEAD -- models/FUNWAVE/source-analysis/funwave-infrastructure.md`의 추가 줄은 286줄이다.
이 수에는 frontmatter와 빈 줄이 포함된다.
시작 시 노트는 336줄이다.
시작 시 노트 SHA-256은 `cedcfc006631f931aaefd1be88c80b29e2bdf85cbd93651d8e62c79bd14acb8c`다.

대상 줄은 시작 시 번호로 `5–6, 17–18, 25–29, 39–40, 42–49, 54–59, 64–67, 69–74, 83–95, 99–336`이다.

원문은 현재 TVD·GPU 코드와 지정한 과거 커밋의 코드다.
문서의 식과 숫자는 지정한 쪽 이미지로 판정한다.
결론은 대조 보고서의 최종 전수 검증 기록과 최종 집계를 기준으로 판정한다.

## 대조 결과

대상 노트의 286줄을 모두 대조했다.
정정은 17줄이다.
인용 보완은 4줄이다.
정정과 보완은 서로 다른 물리 줄로 집계했다.
표의 결론 칸에 붙인 검증 표지는 정정 수에 중복하여 더하지 않았다.
수정 뒤에도 전체 줄 수는 336줄이다.
이 기록의 줄 번호는 수정 뒤 노트의 줄 번호와 같다.

| 대상 노트 | 대조한 줄 | 정정한 줄 | 보완한 줄 | 미해결 항목 |
|---|---:|---:|---:|---:|
| models/FUNWAVE/source-analysis/funwave-infrastructure.md | 286 | 17 | 4 | 0 |

### 범위별 대조 기록

| 대상 줄 | 줄 수 | 대조 내용과 근거 |
|---|---:|---|
| 5–6 | 2 | frontmatter의 검증 방법·확인일을 [반영 기록 2](FUNWAVE-notes-apply-2.md)의 metadata와 대조했다. 기존 검증 이력에 recovery 반영 이력이 추가되었다. |
| 17–18 | 2 | 벽 경계·조파·중첩·주기 경계를 TVD bc.F:65–205와 io.F:870·2260에서 대조했다. |
| 25–29 | 5 | 초기화 요약과 Kappa 대입·전달·미사용을 init.F:280 이후, fluxes.F:473·583·724–728·780–784, io.F:2842–2854에서 대조했다. |
| 39–40 | 2 | io.F의 실제 5064줄과 READ_INPUT의 149–3773행을 대조했다. READ_INPUT은 양 끝을 포함하여 3625줄이다. |
| 42–49 | 8 | 관측점 열·건조점·버퍼·파일 입출력 분기를 io.F:3770–4290·4751–4925와 main.F:537–544에서 대조했다. |
| 54–59 | 6 | INI_SOL·LEF_SOL 입력과 alpha·중심 좌표를 io.F:890–924·1101–1184, samples.F:511–569, init.F:570–593·907–909에서 대조했다. |
| 64–67 | 4 | 결합 시작 시각·보간 가중치·제목행 갱신을 main.F:238과 nesting.F:53–104·367–401·485–498에서 대조했다. |
| 69–74 | 6 | CFL 분모·하한·고정 시간 간격·ghost 포함 범위·MPI_MIN을 misc.F:216–296와 io.F:2883–2895에서 대조했다. |
| 83–95 | 13 | 시간루프·RK 호출 순서와 조건을 main.F:160–550, fluxes.F:115, dispersion.F:289 및 호출 흐름 보고서 §4·§6.2에서 대조했다. 빈 줄과 흐름도 링크도 포함했다. |
| 99–109 | 11 | 제목·판본·보고서 링크·분류 설명·표 머리글을 대조했다. |
| 110–336 | 227 | 차이 표의 모든 행을 최종 결론·현재 코드·과거 코드·문서 원문과 대조했다. |
| 합계 | 286 | 누락된 대상 줄은 없다. |

### 차이 표 대조 결과

| 보고서 | 대조 행 수 | 최종 분류·결론 대조 |
|---|---:|---|
| [theory-numerics](../compare/funwave-theory-numerics-vs-code.md) | 17 | 일치 |
| [inputs](../compare/funwave-inputs-vs-code.md) | 42 | 일치 |
| [examples](../compare/funwave-examples-vs-code.md) | 23 | 일치 |
| [v21-manual](../compare/funwave-v21-manual-vs-code.md) | 45 | 일치 |
| [v21-examples](../compare/funwave-v21-examples-vs-code.md) | 18 | 일치 |
| [aux-docs-build](../compare/funwave-aux-docs-build-vs-code.md) | 27 | 일치 |
| [gpu-vs-tvd](../compare/funwave-gpu-vs-tvd.md) | 46 | 일치 |
| [callflow](FUNWAVE-callflow.md) | 9 | 일치 |
| 합계 | 227 | 누락·중복 없음 |

분류 집계는 A 34행, B 43행, C 77행, D 11행, E 20행, F 42행이다.
A 34행에 적힌 저장소·커밋·날짜 조합은 중복을 제거하면 50개이다.
이 날짜는 해당 커밋의 작성일과 모두 일치한다.
E 20행의 강도는 보고서 최종 판정과 모두 일치한다.
결론 문장은 인용 경로·문서명 확장·링크 위치·추가 검증 표지를 제외하면 보고서 최종 문장과 같다.
이번 정정은 결론 분류와 E 강도를 바꾸지 않는다.
현재 본문에서 교체한 과거 문장은 읽기 전용 diff의 삭제 줄과 보고서 수정안을 함께 대조했다.

### 정정 목록

아래의 `funwave-infrastructure.md:줄`은 대상 노트의 위치이다.
`T/`는 `models/FUNWAVE/raw/source_code/FUNWAVE-TVD/`이다.
`G/`는 `models/FUNWAVE/raw/source_code/FUNWAVE-GPU/`이다.
과거 커밋의 경로는 지정된 external/tvd 저장소에서 읽었다.

| 노트:줄 | 전 → 후 | 근거 원문 |
|---|---|---|
| funwave-infrastructure.md:49 | `PutFile(:4863/:4894, ASCII/binary)` → 병렬은 FIELD_IO_TYPE으로 형식을 선택한다. 직렬은 ASCII로 쓴다. | T/src/io.F:4853–4885의 PARALLEL·SELECT CASE와 4894–4925의 직렬 WRITE. GetFile 분배는 4751–4842. FV2-315의 조건과 일치한다. |
| funwave-infrastructure.md:88 | RK 단계에서 CAL_DISPERSION을 순서대로 실행한다 → `IF(DISPERSION)THEN`에서 호출한다. | T/src/main.F:382–384. 이후 FLUXES·SourceTerms·ESTIMATE_HUV·UPDATE_MASK는 395–417. 호출 흐름 보고서 §4의 분산 조건. |
| funwave-infrastructure.md:92 | `선택 거품·EXCHANGE·중첩·경계 조파·직접 스펀지` → FOAM·COUPLING 전처리 조건과 조파·DIRECT_SPONGE 조건을 각각 명시한다. | T/src/main.F:445–484. 조파 조건 원문은 `IF(WaveMaker(1:3)=='ABS' .OR. WaveMaker(1:12)=='TIME_SPECTRA') THEN`과 `IF(WaveMaker(1:11)=='LEFT_BC_IRR') THEN`이다. |
| funwave-infrastructure.md:93 | RK 뒤 `극값·CHECK_BLOWUP` 실행 → 극값은 여섯 출력 플래그의 OR 조건에서 호출한다. CHECK_BLOWUP은 그 뒤에 호출한다. | T/src/main.F:513–517의 `IF (OUT_Hmax.OR.OUT_Hmin.OR.OUT_Umax.OR.OUT_MFmax.OR.OUT_VORmax.OR.OUT_Time)THEN`. |
| funwave-infrastructure.md:112 | 식 (29)의 `(Hu)_\phi` → `(Hu)\phi`. 인쇄 위치 설명을 덧붙였다. | funwave_tvd_3.0.pdf p.20의 300 dpi 이미지. φ는 아래첨자가 아닌 본문 높이이다. 계수 대응을 설명하는 FT1-056의 F 결론은 유지했다. |
| funwave-infrastructure.md:175 | 괄호 문장 안에 백틱을 중첩한 인용 → `(i = 500, where i is grid number in x direction in Grid_A).`를 하나의 코드 인용으로 정리했다. | funwave_tvd_3.0.pdf p.76 마지막 줄과 p.77 첫 줄의 이미지. 격자 번호 결론은 유지했다. |
| funwave-infrastructure.md:179 | `436e692 ... ghost의 PHI_COLL 호출만 추가했다` → 직교 분기의 PHI_COLL 호출에 PERIODIC 인수를 추가했다. 경사 원점 식은 유지했다. | `436e692:src/init.F:685–690`과 해당 커밋 diff. [git 검증 E2](../compare/FUNWAVE-git-verify-E2.md)의 FX1-806도 기존 호출의 변경으로 판정한다. |
| funwave-infrastructure.md:223 | 문서 원문의 `선택 초기 유속 파일과 INI_UVZ` → U_FILE·V_FILE 설명과 인쇄된 `INT_UVZ`를 구분했다. | funwave_tvd_2.1_manual.pdf p.36의 이미지와 판독 기록. 코드의 실제 키 INI_UVZ와 FV1-473의 E 강함 결론은 유지했다. |
| funwave-infrastructure.md:283 | `T/src/bc.F:433`의 CARTESIAN 조건 → `T/src/bc.F:434`. | 433행은 빈 줄이다. 434행은 `# if defined (CARTESIAN)`이다. FG1-003의 A 결론은 유지했다. |
| funwave-infrastructure.md:255 | `bfc2f8c:src/misc.F` → `bfc2f8c:misc.F`. 다섯 인용을 정정했다. | `bfc2f8c:misc.F:154·168·170·184·192`의 CFL 분모·최솟값·DT 대입. |
| funwave-infrastructure.md:256 | `bfc2f8c:src/mod_param.F` → `bfc2f8c:mod_param.F`. 세 인용을 정정했다. | `bfc2f8c:mod_param.F:59–60·65`의 DOUBLE_PRECISION·SP=8·SELECTED_REAL_KIND. |
| funwave-infrastructure.md:257 | `bfc2f8c:src/misc.F:106` → `bfc2f8c:misc.F:106`. | 원문은 `Mloc=Mglob/px+2*Nghost`이다. |
| funwave-infrastructure.md:258 | `bfc2f8c:src/misc.F:107` → `bfc2f8c:misc.F:107`. | 원문은 `Nloc=Nglob/py+2*Nghost`이다. |
| funwave-infrastructure.md:259 | `bfc2f8c:src/misc.F:106·107` → 루트의 `misc.F:106·107`. 반복 인용을 포함하여 네 곳을 정정했다. | 해당 커밋의 두 정수 나눗셈 식. 현재 나머지 분배는 T/src/misc.F:132–133·197–203이다. |
| funwave-infrastructure.md:264 | `bfc2f8c:src/io.F` → `bfc2f8c:io.F`. 세 인용을 정정했다. | `bfc2f8c:io.F:67·69·1059`의 전처리 조건·CALL·SUBROUTINE. |
| funwave-infrastructure.md:265 | `bfc2f8c:src/` → `bfc2f8c:`. 반복 인용을 포함하여 18곳을 정정했다. | 해당 커밋의 misc.F:378, wavemaker.F:806·1091, sponge.F:246·248·415·417, io.F:1608·1648의 REAL 호출. |
| funwave-infrastructure.md:266 | `bfc2f8c:src/parallel.F` → `bfc2f8c:parallel.F`. 반복 인용을 포함하여 네 곳을 정정했다. | `bfc2f8c:parallel.F:490–491`의 MPI_Scatter 호출. |

`bfc2f8c`의 잘못된 경로 인용은 총 39곳이었다.
그 커밋의 파일은 `src/` 아래가 아니라 저장소 루트에 있다.
이 경로 정정은 노트의 물리 줄 8개로 집계했다.
모든 정정 줄 끝에 `[10-18 전수 검증 정정]`을 붙였다.
표 행에서는 결론 문장 칸 끝에 표지를 붙였다.

### 인용 보완 목록

| 노트:줄 | 전 → 후 | 보완한 근거 원문 |
|---|---|---|
| funwave-infrastructure.md:18 | 입력 위치만 인용 → 경계 분기 원문을 추가했다. | T/src/bc.F:65–94·105–141·147–205. |
| funwave-infrastructure.md:58 | samples.F:542의 ghost 주석만 인용 → 중심식·Xco 원점·Ibeg·Nghost의 근거를 추가했다. | T/src/samples.F:542–548, init.F:570–593, misc.F:171, mod_global.F:129. |
| funwave-infrastructure.md:70 | FN1-713으로만 연결 → 하한 분기 원문을 추가했다. | T/src/misc.F:244–256·260–272의 SMALL 분기. |
| funwave-infrastructure.md:102 | 판본 설명에 직접 연결된 보고서 없음 → 문서·코드 판본 보고서 링크를 추가했다. | [호출 흐름 §5.1](FUNWAVE-callflow.md#51-판본과-대조-시점), [GPU 대조 §1.1](../compare/funwave-gpu-vs-tvd.md#11-판본과-분기-기준). |

네 보완 줄 끝에 `[10-18 전수 검증 보완]`을 붙였다.

### 기계 확인 후보 판정

사용자가 제시한 순서를 유지했다.
중복으로 제시된 후보도 각각 한 줄로 기록했다.

| 번호 | 후보 | 판정과 근거 |
|---:|---|---|
| 1 | `src/mod_param.F:58` 뒤의 `의 배정도 분기는` | 오탐이다. 노트 117행은 `T/src/mod_param.F:58–68`과 `7b93138:src/mod_param.F:58–68`을 가리킨다. 두 범위의 배정도 분기는 `INTEGER, PARAMETER::SP=8`이다. |
| 2 | 과거 노트 16행의 `4방향 개방경계 P·Q=0` | 오탐이다. 노트 124행은 수정 전 문장을 인용한다. diff의 삭제 줄과 같다. 현재 설명 17행은 bc.F:65–205에 따라 벽 경계로 고쳐져 있다. |
| 3 | 과거 노트 45행의 `DT=CFL·min(DX/\|U+c\|,DY/\|V+c\|)` | 오탐이다. 노트 125행은 과거 오기를 인용한다. 현재 69–74행은 misc.F:243·259의 ABS(U)+파속과 ABS(V)+파속 및 하한·집계를 설명한다. |
| 4 | 과거 노트 23행의 `MUSCL kappa(SEC→−1/else→1/3)` | 오탐이다. 노트 126행의 과거 인용은 삭제 줄과 같다. 현재 26–29행은 init.F:389–393의 Kappa 대입과 fluxes.F:724–728·780–784의 미사용을 구분한다. |
| 5 | `fluxes.F:780` 뒤의 `FUNWAVE-TVD/src/io.F:2842–2854` | 오탐이다. 노트 126행은 서로 다른 두 원문 위치를 연속으로 인용한다. fluxes.F:780–781은 재구성식이다. io.F:2842–2854는 HIGH_ORDER 입력·기본값 분기이다. |
| 6 | 과거 CFL 식의 두 번째 제시 | 오탐이다. 노트 168행의 FI1-322도 수정 전 식을 인용한다. `7b93138:src/misc.F:154·170`과 현재 misc.F:243·259는 속도에만 ABS를 적용한다. |
| 7 | `src/init.F:589` 뒤의 `436e692 ... PHI_COLL 호출만 추가했다` | 노트 오류이다. 179행을 정정했다. `739a08d:src/init.F:589`의 직렬식은 맞다. `436e692:src/init.F:685–690`은 기존 호출의 직교 분기에 PERIODIC 인수를 추가한다. |
| 8 | `src/nesting.F:375` 뒤의 제목 건너뛰기 제거·시각 읽기 도입 | 오탐이다. 노트 184행의 인용은 `32203a2:src/nesting.F:375–377`이다. 375행의 이전 제목 READ는 주석이다. 376행은 TIME_COUPLING_2를 읽는다. 날짜는 2023-08-21이다. |
| 9 | `src/io.F:3630` 뒤의 2019-12-06 버퍼 분기 도입 | 오탐이다. 노트 185행의 `334bb51:src/io.F:3630`에는 BufferCount와 TIME 조건이 있다. 해당 커밋 diff가 버퍼 저장·flush 분기를 도입한다. |
| 10 | `src/io.F:3481` 뒤의 직접 쓰기·FOAM·시간 정밀도 이력 | 오탐이다. 노트 185행의 `334bb51^:src/io.F:3481`은 time·eta_sta·u_sta·v_sta를 직접 쓴다. a91643c의 FOAM 열 추가와 366dd5f의 시간 열 형식 변경은 버퍼 조건을 유지한다. |
| 11 | 과거 노트 35행의 `station 시계열(time,eta,u,v) 버퍼→ASCII` | 오탐이다. 노트 189행은 diff의 삭제 줄을 인용한다. 현재 42–48행은 io.F:4073–4097의 조건과 FOAM 열을 설명한다. |
| 12 | 같은 관측점 버퍼 문구의 두 번째 제시 | 오탐이다. 189행의 같은 과거 문구에 대한 재검사이다. 현재 표본의 저장·flush 분기는 io.F:4073–4097과 일치한다. |
| 13 | 과거 노트 39행의 `INITIAL_SOLITARY_WAVE` | 오탐이다. 노트 190·253행은 기존 초기파형 요약을 인용한다. 현재 54–59행은 init.F:907–909와 samples.F:511–569에 근거한 조건을 보탠 상태이다. |
| 14 | 같은 `INITIAL_SOLITARY_WAVE`의 두 번째 제시 | 오탐이다. 과거 요약의 루틴명은 실제 samples.F:511의 선언과 같다. INI_SOL 입력 구분은 io.F:1101–1184와 일치한다. |
| 15 | 과거 노트 43행의 `parent grid 경계 시계열 선형보간→ghost (one-way nesting)` | 오탐이다. 노트 191·254행은 기존 중첩 요약을 인용한다. 현재 64–67행은 main.F:238과 nesting.F:367–401·485–498의 시작 시각·보간 조건·제목행 문제를 구분한다. |
| 16 | 같은 중첩 요약의 두 번째 제시 | 오탐이다. nesting.F:485–498은 TIME과 두 자료 시각에 따라 가중치를 정한다. 과거 요약을 인용한 칸과 현재 조건 설명은 서로 다른 역할이다. |
| 17 | `src/io.F:1022` 뒤의 `와` | 오탐이다. 노트 242행은 현재 파일이 아닌 `24a88c3:src/io.F:1022`를 가리킨다. 원문은 `write(file_name(1:4),'(I4.4)') i`이다. |
| 18 | `src/io.F:3253` 뒤의 `의 원문은 각각` | 오탐이다. 노트 242행의 `fef45a7:src/io.F:3253`도 `write(file_name(1:4),'(I4.4)') i`이다. 서로 다른 두 커밋의 같은 파일명 형식을 설명한 문장이다. |

기계 확인 후보의 판정은 노트 오류 1건과 오탐 17건이다.
정정 목록의 나머지 항목은 전수 대조에서 별도로 확인했다.

### 최종 원문·형식 확인

경로를 명시한 현재·과거 원문 위치 1515회를 파일과 행 범위로 검사했다.
이 검사에 포함된 파일·판본 조합은 109개이다.
수정 뒤 존재하지 않는 파일과 범위를 벗어난 행 인용은 없다.
축약된 `:줄` 인용과 `436e692` 등 변경 설명은 별도로 원문을 대조했다.
지정 빌드 파일 39개에는 FILTERING 선택지가 없다.
TVD와 GPU의 FILTERING 전처리 조건은 각각 3곳이다.
이 수는 보고서 FN1-609와 같다.

문서의 식·숫자·인쇄 표기는 아래 70개 쪽 이미지로 대조했다.
같은 이미지를 다시 연 경우는 중복 집계하지 않았다.

| 문서 | 이미지로 대조한 PDF 쪽 | 쪽 수 |
|---|---|---:|
| funwave_tvd_3.0.pdf | 1, 19–21, 25, 32–45, 61, 69–70, 75–81, 85 | 30 |
| funwave_tvd_2.1_manual.pdf | 8, 20, 23–24, 26–27, 29–32, 34–43, 49, 60, 62, 65, 68–71 | 28 |
| Intro-to-FUNWAVE-CHL-TN.pdf | 8–9, 15, 17, 19, 22 | 6 |
| funwave_code_analysis.pdf | 3, 7, 10, 12–14 | 6 |
| 합계 | 지정된 300 dpi 쪽 이미지 | 70 |

각 문서의 대응 쪽별 판독 기록도 대조 근거로 사용했다.
수식·수치가 판독 기록과 충돌할 때는 쪽 이미지로 판정했다.
노트의 Markdown 링크 74개가 가리키는 파일은 모두 존재한다.
링크 목적지 문자열은 중복을 제거하면 22개이다.
노트에는 `/home/firesinger/` 절대 경로와 `[[`가 없다.
노트에는 사용자가 금지한 미완료·후속 대상 한계 문장이 없다.
노트 안의 mermaid 블록은 0개이다.
호출 흐름도 링크는 보고서 §4를 가리킨다.
호출 흐름 보고서 끝의 렌더 확인 기록도 대조했다.
검증 표지는 본문 줄 끝 또는 표의 결론 문장 칸 끝에 있다.
`git diff --check HEAD -- models/FUNWAVE/source-analysis/funwave-infrastructure.md`는 오류 없이 끝났다.

최종 노트 SHA-256은 `42c152958fa9a97637145d15a6f4f0289e6a46081ea83f97ee172e29acbe32a2`다.
완료한 노트: `models/FUNWAVE/source-analysis/funwave-infrastructure.md`.
미해결 항목: 없음.
