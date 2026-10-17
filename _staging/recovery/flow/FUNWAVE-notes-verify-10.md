# FUNWAVE 노트 전수 대조 10

작업일: 2026-10-18.

대상은 사용자 지정 노트 7개다. 기존 노트의 대상은 작업 시작 시 `git diff -U0 HEAD -- <노트>`의 추가 줄이다. 새 파일 `funwave-v21-manual-differences.md`의 대상은 전체 줄이다. 빈 줄과 frontmatter도 센다.

각 줄은 보고서 최종 결론과 해당 원문에 대조한다. 문서의 식과 숫자는 300 dpi 쪽 이미지로 판정한다. 정정 표시는 `[10-18 전수 검증 정정]`이다. 인용 보완 표시는 `[10-18 전수 검증 보완]`이다.

## 진행 기록

완료: 아래 7개 노트의 대상 217줄을 모두 대조했다. 노트별 기록은 §1–7에 있다. 최종 집계는 문서 끝에 있다.

## 작업 시작 시 대상 줄

줄 번호는 정정 전 노트 기준이다. 대상 줄 수는 위 명령의 추가 줄과 새 파일 전체 줄에서 집계했다. 총 대상은 217줄이다.

| 노트 | 대상 줄 수 | 대상 줄 번호 |
|---|---:|---|
| source-analysis/funwave-build-and-blackwell-port.md | 51 | 5–6, 19–20, 33, 37, 39, 46–49, 53, 55, 59, 65–101 |
| manual-notes/funwave-v21-manual-differences.md | 31 | 1–31 |
| source-analysis/funwave-code-graph.md | 39 | 5–6, 14–18, 35–41, 47, 51, 71, 75–96 |
| source-analysis/funwave-wk-data2d-spectral-wavemaker.md | 37 | 6, 11, 22, 36–43, 68, 72, 82–83, 85–106 |
| manual-notes/funwave-validation-cases.md | 25 | 7–8, 86–88, 101, 135–153 |
| web-refs/funwave-foundational-papers.md | 20 | 5–7, 26–28, 40–42, 49, 51–60 |
| manual-notes/funwave-tvd-manual.md | 14 | 5–6, 36, 45–55 |

## 1. funwave-build-and-blackwell-port.md — 완료

대조한 대상은 51줄이다. 정정은 4줄이다. 인용 보완은 0줄이다. 줄 수는 작업 시작 시 대상 목록에서 셌다. 정정 수는 이번 작업에서 바꾼 원래 줄 번호의 수다.

| 대조 범위 | 대조 결과·원문 |
|---|---|
| 5–6 | 기존 2026-06-12 실행 기록과 2026-10-18 보고서 반영을 구분했다. `notes-apply-9`의 frontmatter 반영 기록과 일치한다. |
| 19–20, 33, 37, 39, 46–49, 53, 55, 59 | `aux-docs-build` §4 FN1-901·924와 `gpu-vs-tvd` §4 FG1-800·878·900·902·904를 대조했다. GPU 원자료의 공개 `7f892ba` 대비 diff를 읽었다. `mod_cuda.F:17,27–28`, `etauv_solver_gpu.F:93–158,910–942`, 두 Makefile의 36·38줄을 읽었다. 기존 사례의 진행 시각은 FG1-902에 기록된 범위와 같다. |
| 65–73 | 표지 이미지의 `Release Dec 2016`·`July 2015`와 AD1의 문서 기준표를 대조했다. 제목·빈 줄·표 머리글을 확인했다. |
| 74–101 | 차이 표 28행의 분류와 결론을 각 보고서 §5 및 마지막 검증 기록에 대조했다. A 행의 HASH·날짜는 AD1·AD2·AD3의 해당 행과 같다. FN1-549·551의 E 강도는 모두 강함이다. FN1-549의 반대 근거는 E2와 같다. |

문서 원문은 3.0 판독 기록 p.32–34·43–44·77, 2.1 판독 기록 p.34·70, code_analysis 판독 기록 p.8–9를 읽었다. 3.0 p.1·34·43·44, 2.1 p.34, Intro-TN p.1의 이미지를 열었다. 현재 Makefile·Make_Essential·gcc10 대체 파일의 인용 범위와 `fluxes_21v.F:719–722`를 읽었다. 과거 `24a88c3:src/Makefile`, `ca113a8:Makefile`, `ca113a8:GNUMake/Essential/Make_Essential`, `2e72b18:Makefile`, `b9c035d:src/Makefile`, `3d5c748:GNUMake/Essential/Make_Essential_gcc10`, GPU `7f892ba`·`5594984`의 인용 원문을 `git show`로 읽었다.

| 정정 위치 | 전 → 후 | 근거 원문 |
|---|---|---|
| `models/FUNWAVE/source-analysis/funwave-build-and-blackwell-port.md:19` | `(332M)` → `(2026-06-12 기존 기록: 332M)` | 노트의 `note_date`와 FG1-900의 정정 전 인용은 기존 기록이다. 현재 원자료의 `du -sh`는 336M이다. 과거 용량을 현재 측정치로 오독하지 않도록 기록 시점을 명시했다. |
| `models/FUNWAVE/source-analysis/funwave-build-and-blackwell-port.md:20` | `(92M)` → `(2026-06-12 기존 기록: 92M)` | FG1-900의 정정 전 인용은 기존 기록이다. 현재 원자료의 `du -sh`는 102M이다. 기존 실행 기록의 용량을 보존하고 기록 시점을 명시했다. |
| `models/FUNWAVE/source-analysis/funwave-build-and-blackwell-port.md:75` | `GPU 작업 트리 diff는 아래에 기록한다.` → `GPU 작업 트리 diff의 공개 기준과 로컬 수정 파일은 이 표의 FN1-550·924에 기록했다.` | 보고서 FT1-258의 상대 지시어를 옮기면서 노트에 없는 diff를 가리켰다. 노트의 FN1-550·924와 실제 GPU diff는 공개 기준과 로컬 수정 파일을 제시한다. |
| `models/FUNWAVE/source-analysis/funwave-build-and-blackwell-port.md:96` | 결론 칸의 `FUNWAVE-TVD/src/main.F:440`·`FUNWAVE-TVD/src/mod_cuda.F:367` → 각각 `FUNWAVE-GPU/` 경로 | GPU `main.F:438–441`의 TIMING 호출과 GPU `mod_cuda.F:367`의 정의가 원문이다. TVD `main.F:440`은 `# else`이다. TVD에는 `mod_cuda.F`가 없다. FN1-551의 분류·강도·결론 의미는 유지했다. |

기계 확인 후보 판정:

- `7f892ba:src/etauv_solver_gpu.F:910` 호출: 오판이다. 공개 GPU 커밋의 해당 줄은 노트의 `cusparseSgtsvStridedBatch` 호출과 일치한다.
- 정정 전 노트 `:18`의 `CPU/MPI Fortran, v3.6`: 오판이다. FN1-901의 문서 원문 칸은 정정 전 문장을 인용한다. 보고서 §4·§5와 AD3가 그 인용을 보존한다. 현재 설명은 19줄의 HEAD `b4c322e`와 `VERSION 3.0` 주석이다.

상대 링크 19개는 대상 파일이 존재한다. Mermaid 블록은 없다. 사용자 홈 절대 경로와 위키링크 구분자는 없다. 금지한 한계 문장은 없다. 미해결 항목은 없다.

## 2. funwave-v21-manual-differences.md — 완료

대조한 대상은 새 파일 전체 31줄이다. 정정은 0줄이다. 인용 보완은 0줄이다.

| 대조 범위 | 대조 결과·원문 |
|---|---|
| 1–13 | frontmatter의 제목·대상·작성자·날짜·AI 보고서 반영 방식은 `notes-apply-9`의 신규 노트 기록과 일치한다. |
| 14–30 | 제목·범위·빈 줄·표 머리글·보고서 링크를 확인했다. 문서·코드 판본은 AD1의 문서 기준표와 원자료 `main.F:47`에 맞는다. |
| 31 | RF-018의 D 분류와 결론 문장은 callflow §8의 최종 행과 같다. 2.1 매뉴얼 p.29의 GatherVariable, p.30의 ScatterVariable, p.31의 TRIDxyNoParallel을 쪽별 판독 원문에서 확인했다. `cab9425:etauv_solver.F:354–358`을 `git show`로 읽었다. PARALLEL 조건 아래의 TRIDx와 그 밖의 TRIDx_ser 호출은 인용과 같다. 현재 TVD·GPU Fortran 소스에서 세 이름의 대소문자 무시 검색은 모두 0건이다. 공개 이력 판정은 AD1의 RF-018과 일치한다. |

callflow 끝의 전수 검증 기록과 최종 집계를 확인했다. 노트에 인용된 RF-018의 결론을 바꾸는 후속 판정은 없다. 정정 목록은 없다. 이 노트에 배정된 기계 확인 후보는 없다. 상대 링크 2개는 대상 파일이 존재한다. Mermaid 블록은 없다. 금지 문자열과 한계 문장은 없다. 미해결 항목은 없다.

## 3. funwave-code-graph.md — 완료

대조한 대상은 39줄이다. 정정은 2줄이다. 인용 보완은 1줄이다.

| 대조 범위 | 대조 결과·원문 |
|---|---|
| 5–6, 14–18 | frontmatter는 반영 기록과 같다. 원자료 `src/*.F`를 다시 집계했다. 파일은 38개이다. LF 바이트는 33,760개이다. 논리 행은 33,761개이다. 보고서의 정규식으로 센 SUBROUTINE·USE·MODULE·CALL은 각각 218·414·15·1,301개이다. FN1-903의 최종 C 범위와 일치한다. Make_Essential:204–211의 선택 목록과 정적 선언 집계를 구분했다. |
| 35–41 | callflow §6.2의 교체 문장과 현재 `main.F:380–414`, `fluxes.F:52–117,150–194`, `etauv_solver.F:348,398–550`을 대조했다. 분산 조건과 RK 단계의 호출 순서는 일치한다. HLL 내부에는 WAVE_SPEED 호출이 없다. 기존 ASCII 호출 사슬을 교체할 근거는 RF-046과 FN1-920에 있다. |
| 47, 51 | mod_input.F:76·126·175·220에서 네 READ 루틴을 확인했다. fluxes.F:239·293과 derivatives.F:123·158에서 미분 루틴의 정의 파일을 확인했다. 전체 `src/*.F`의 행 시작 CALL을 세면 DelxFun과 DelyFun은 각각 27개이다. |
| 71, 75 | FG1-901의 기존 GPU 목록과 41파일 비교 범위를 대조했다. GPU `mod_cuda.F:17`, `etauv_solver_gpu.F:105–158`의 TriSolver 분기와 FG1-802의 transpose·Thomas·MPI sweep 설명을 대조했다. |
| 76–96 | 제목·빈 줄·판본·표 머리글과 차이 표 12행을 확인했다. 각 분류와 결론은 보고서 최종본과 같다. A인 FN1-373·558의 `eccc669`·2016-12-31은 AD3와 같다. code_analysis p.12–13 이미지는 호출 사슬과 REAL 파일 묶음을 보여 준다. 2.1 p.28–31 판독 기록은 호출자·루틴명 인용을 뒷받침한다. |

표의 현재 코드 인용과 과거 코드 인용을 열었다. 과거 인용은 `7b93138:src/mod_input.F`, `fef45a7:src/mod_input.F`, `2e72b18:fluxes.F,io.F,main.F`, `bfc2f8c:main.F,init.F,mixing.F,wavemaker.F,io.F,misc.F`, `eccc669:src/main.F`, `cab9425:main.F`의 명시 줄을 대조했다. `bfc2f8c`의 여섯 파일은 저장소 루트에 있다.

| 위치 | 전 → 후 | 근거 원문 |
|---|---|---|
| `models/FUNWAVE/source-analysis/funwave-code-graph.md:92` | FN1-373 코드 칸의 모든 `bfc2f8c:src/<파일>` → `bfc2f8c:<파일>` | 지정 커밋에 `src/` 경로가 없다. `git show bfc2f8c:<파일>`의 줄과 인용문은 일치한다. FN1-373의 A 결론은 유지했다. |
| `models/FUNWAVE/source-analysis/funwave-code-graph.md:94` | FN1-558의 `bfc2f8c:src/main.F:177,279` → `bfc2f8c:main.F:177,279` | 해당 커밋 루트 main.F의 두 줄은 WALL_TIME_SECS 호출이다. |
| `models/FUNWAVE/source-analysis/funwave-code-graph.md:51` | 보고서 ID만 인용 → 두 미분 루틴의 정의 줄과 호출 수 집계 규칙을 추가 | fluxes.F:239·293, derivatives.F:123·158. 행 시작 CALL의 대소문자 무시 집계는 27·27이다. |

기계 확인 후보 판정:

- `:48 READ_FLOAT/LOGICAL/STRING/Float` 첫 후보: 오판이다. FI1-323의 문서 원문 칸은 정정 전 노트의 인용이다. 보고서와 git의 네 READ 루틴을 대조했다. 현재 본문 47줄은 READ_INTEGER를 포함한다.
- `:13 33,760줄` 첫 후보: 오판이다. FV1-570은 정정 전 집계 문장을 인용한다. 현재 본문 14줄은 LF 바이트와 논리 행을 구분한다. 재집계 값은 현재 본문과 같다.
- `:34 FLUX_AT_INTERFACE_HLL ─ HLL ─ WAVE_SPEED` 첫 후보: 오판이다. FV1-571은 정정 전 호출선을 인용한다. 현재 본문 37줄과 fluxes.F는 FLUXES의 직접 WAVE_SPEED 호출을 보인다.
- `:48 READ_FLOAT/LOGICAL/STRING/Float` 두 번째 후보: 오판이다. FV1-572의 정정 전 인용이다. mod_input.F의 네 정의와 현재 본문은 일치한다.
- `:52 DelxFun / DelyFun` 후보: 오판이다. FV1-573의 문서 원문 칸은 정정 전 derivatives.F 설명을 인용한다. 현재 본문은 fluxes.F로 고쳐져 있다. 이번 작업은 정의 줄과 집계 규칙만 보완했다.
- `:13 33,760줄` 두 번째 후보: 오판이다. FN1-903의 문서 원문 칸은 정정 전 문장이다. 현재 LF·논리 행·CALL 집계는 원자료와 일치한다.
- `:34 FLUX_AT_INTERFACE_HLL ─ HLL ─ WAVE_SPEED` 두 번째 후보: 오판이다. RF-046의 문서 원문 칸은 정정 전 호출선이다. 현재 본문과 원문 호출 관계는 일치한다.

상대 링크 26개는 대상 파일이 존재한다. Mermaid 블록은 없다. callflow §4 링크와 끝의 렌더 확인 기록을 확인했다. 금지 문자열과 한계 문장은 없다. 미해결 항목은 없다.

## 4. funwave-wk-data2d-spectral-wavemaker.md — 완료

대조한 대상은 37줄이다. 정정은 4줄이다. 인용 보완은 1줄이다.

| 대조 범위 | 대조 결과·원문 |
|---|---|
| 6, 11, 22 | wavemaker.F의 논리 행 수는 3,299개이다. D_gen은 803–805줄에 있다. Wei–Kirby 주석은 824–825줄에 있다. sponge.F:103–106은 Salatin 등의 2021년 논문을 적는다. 연결 노트의 옛 줄 번호와 식이 없다는 설명은 현재 §2에 맞게 정정했다. |
| 36–43, 68, 72 | 빈 줄을 포함해 입력 설명을 대조했다. wavemaker.F:196–325를 읽었다. 둘째 행은 PeakPeriod이다. 진폭은 방향별 행에 주파수 성분을 놓는다. 방향 조건은 `.LT.60.0_SP`이다. 입력 위상 변환은 `IF(INPUT_WAVE_PHASE)THEN` 안에 있다. ELSE의 난수 위상은 INTEL·CRAY와 그 밖의 분기로 나뉜다. 원문 식·조건·단위는 노트와 일치한다. |
| 82–93 | 연결 파일·배정표·보고서·판본을 대조했다. 물리 노트와 분산 노트의 현재 설명에 맞게 링크 설명을 정정했다. |
| 94–106 | 표 머리글·빈 줄과 차이 표 10행을 대조했다. 분류·결론은 보고서 최종본과 같다. FG1-139의 `334bb51 2019-12-06`·`746ffdf 2021-11-01`은 GPU 보고서의 변경 이력과 같다. FG1-885의 F는 활성 Cm 국소식에 한정된다. |

3.0 p.30·37·38과 2.1 p.37의 300 dpi 이미지를 열었다. 첨두주기와 진폭 행렬 순서는 문서의 오기와 코드의 실제 입력을 구분한다. 현재 io.F:870·1850·1926, wavemaker.F:196–325·855–863, GPU wavemaker.F:650–659, moment_gpu.F:2274–2283을 읽었다. 과거 `7b93138`·`fef45a7`의 io.F·wavemaker.F, `2e72b18:wavemaker.F:204`, `e42e17d:src/sources.F:130–145`를 `git show`로 읽었다. TeX:1201–1211에는 선택 위상 배열이 없다.

| 위치 | 전 → 후 | 근거 원문 |
|---|---|---|
| `models/FUNWAVE/source-analysis/funwave-wk-data2d-spectral-wavemaker.md:6` | `funwave-physics-sources.md:26,29 는 1줄 표만` → 조파 개괄의 §2 참조 | 현재 연결 노트의 29–40줄에 §2와 D_gen 식·옵션 표가 있다. YAML 값 밖 주석에 정정 표시를 붙였다. |
| `models/FUNWAVE/source-analysis/funwave-wk-data2d-spectral-wavemaker.md:22` | 광역 연결의 핵심이라는 평가와 옛 줄·식 없음 설명 → 입력 배열·SWAN 변환 주석·현재 §2 참조 | wavemaker.F:196–243·291–293과 연결 노트 §2. FT1-255의 실제 WK_DATA2D 입력 경로와 같은 범위로 적었다. |
| `models/FUNWAVE/source-analysis/funwave-wk-data2d-spectral-wavemaker.md:82` | `:26/29 표` → §2의 조파 개괄 | 연결 노트 26줄은 쇄파 설명이다. 29줄은 조파 절 제목이다. |
| `models/FUNWAVE/source-analysis/funwave-wk-data2d-spectral-wavemaker.md:83` | `내부소스 fully-dispersive 와 동류 α` → Boussinesq 분산항과 삼중대각 풀이 | 연결한 분산 노트의 제목·§1·§2와 callflow §6의 분산·유속 복원 설명이 이 범위를 뒷받침한다. 근거 없는 fully-dispersive 동등성 표현을 제거했다. |
| `models/FUNWAVE/source-analysis/funwave-wk-data2d-spectral-wavemaker.md:105` | 과거 `e42e17d:src/sources.F:138` 인용 → 138–142 범위와 현재 sources.F:150–163 인용을 추가 | FG1-432는 GPU와 분기 기준 TVD의 국소식을 F로 판정한다. 보고서에는 현재 TVD가 이 조각을 변경했다는 설명도 있다. 현재 원문은 AA·BB2·CC2를 먼저 계산한다. |

기계 확인 후보 판정:

- `src/sources.F:138 WK_Source=WK_Source+TANH(...)`: 오판이다. 노트의 원래 인용에는 과거 커밋 `e42e17d`가 붙어 있다. 해당 커밋의 138줄은 인용과 일치한다. 현재 TVD 138줄과의 비교는 판본을 혼동한다. 이번 작업은 과거 인용 범위와 현재 대응식을 보완했다.

상대 링크 12개는 대상 파일이 존재한다. Mermaid 블록은 없다. 금지 문자열과 한계 문장은 없다. 미해결 항목은 없다.

## 5. funwave-validation-cases.md — 완료

대조한 대상은 25줄이다. 정정은 1줄이다. 인용 보완은 1줄이다.

| 대조 범위 | 대조 결과·원문 |
|---|---|
| 7–8 | `notes-apply-8`의 반영 날짜와 방법을 대조했다. 원자료의 PDF를 디렉터리별로 다시 세었다. benchmarks에는 30개가 있다. simple_cases에는 5개가 있다. doc에는 4개가 있다. 기존 35개 집계의 범위를 검증 그림 디렉터리로 명시했다. BM5_A_Plotter.m·BM7_loader.m과 morpho의 vessel 입력·rip_tracking의 입력 파일은 존재한다. |
| 86–88 | FV2-407의 수정안과 일치한다. 2.1 p.57·60·72와 3.0 p.69 이미지를 대조했다. 본문의 Briggs 연도는 1995이다. 참고문헌의 연도는 1994이다. 사례 A·B·C의 진폭은 0.0144·0.02912·0.05792 m이다. |
| 101 | FV2-408·FX1-917의 수정안과 일치한다. 2.1 p.69·70·73과 3.0 p.76·80 이미지를 대조했다. 원자료 solitary_nesting_v20.pdf의 Grid A·Grid B·nesting boundary·시각·축 텍스트는 매뉴얼 결과 그림과 같다. |
| 135–143 | 빈 줄·절 제목·판본·보고서 링크·표 머리글을 확인했다. 문서 판은 AD1의 기준표와 같다. 현재 main.F:47은 VERSION 3.0 주석이다. |
| 144–153 | 차이 표 10행의 분류와 결론은 examples·v21-examples의 최종 §5와 같다. 마지막 전수 검증 기록의 H→B 정정도 반영되어 있다. 모든 B 행의 오기 위치를 해당 이미지에서 확인했다. io.F:1132와 b9c035d:src/io.F:378의 AMP 읽기 인용은 원문과 같다. |

이미지 대조 범위는 3.0 p.53·65–66·69·73–74·76·80과 2.1 p.43–44·57–60·65–70·72–73이다. 3.0 그림 7의 음수 부호 누락과 두 판의 원뿔섬 캡션 오류를 확인했다. 두 판의 OSU 그림 내부 범례는 실선 data·파선 model이다. 중첩 예제의 본문 1 m와 입력 AMP=0.1은 서로 다르다. 2.1 p.44의 0.25 m 표기는 같은 예제의 0.025 m와 다르다. 결과의 과소·과대 예측 설명은 문서가 보고한 결과로 구분되어 있다.

| 위치 | 전 → 후 | 근거 원문 |
|---|---|---|
| `models/FUNWAVE/manual-notes/funwave-validation-cases.md:8` | `FUNWAVE-TVD 트리 35개 PDF` → `FUNWAVE-TVD/benchmarks/와 simple_cases/ 아래 검증 그림 PDF 35개` | 원자료 디렉터리별 PDF 집계는 30·5·4이다. 노트 133줄도 doc의 문서 4개를 카탈로그에서 제외한다고 명시한다. YAML 값 밖 주석에 정정 표시를 붙였다. |
| `models/FUNWAVE/manual-notes/funwave-validation-cases.md:86` | 본문 p.57–62만 인용 → 1994년 표기의 근거인 p.72 참고문헌을 추가 | 2.1 p.57 본문은 Briggs et al. (1995)이다. p.72 참고문헌은 Briggs, Synolakis and Harkins, 1994이다. 보고서 FV2-153도 이 연도 차이를 구분한다. |

이 노트에 배정된 기계 확인 후보는 없다. 상대 링크 6개는 대상 파일이 존재한다. Mermaid 블록은 없다. 대상 줄에 금지 문자열과 한계 문장은 없다. 기존 129–134줄은 작업 시작 시 diff의 추가 줄에 포함되지 않는다. 미해결 항목은 없다.

## 6. funwave-foundational-papers.md — 완료

대조한 대상은 20줄이다. 정정은 1줄이다. 인용 보완은 0줄이다.

| 대조 범위 | 대조 결과·원문 |
|---|---|
| 5–7 | `notes-apply-9`의 보고서 반영 기록과 일치한다. 과거 웹 서지 확인과 이번 PDF 서지 구분을 분리한다. |
| 26–28 | FT1-285·FV1-580의 수정안을 반영했다. 현재 masks.F:177–188의 ELSE 분기와 조건문은 글자 단위로 일치한다. io.F:2689–2691·2713–2715의 입력·기본값도 원문과 같다. 논문 서지와 소개 내용은 출판사·저자 소속 대학의 초록과 대조했다. MUSCL·HLL 설명은 3.0 p.23–24 판독 기록과 현재 fluxes.F의 대응 루틴에도 있다. |
| 40–42 | FV1-581의 수정안과 일치한다. 3.0 p.1의 CACR-11-03·Release Dec 2016, 2.1 p.1의 CACR-13-XX, Intro-TN p.24의 2013·CACR-11-04를 이미지에서 확인했다. |
| 49 | 연결 노트 §2는 같은 방정식 계열을 설명한다. 연결 노트의 source·§3은 식 대응을 구조 식별 수준으로 한정한다. 전체 식의 동일성을 단정한 표현을 방정식 계열로 정정했다. |
| 51–60 | 빈 줄·절 제목·판본·보고서 링크·표 머리글을 확인했다. FT1-285의 B 분류와 결론은 theory-numerics §5 최종본 및 AD1의 판정과 같다. 현재 main.F:47과 과거 7b93138:src/masks.F:130–131을 열었다. 마지막 전수 검증 기록과 최종 집계에 이 행을 바꾸는 판정은 없다. |

Shi 등 (2012)의 저자·권·쪽·DOI는 [University of Rhode Island의 저자 논문 기록](https://digitalcommons.uri.edu/oce_facpubs/147/)과 일치한다. 보존형 재구성·적응 Runge–Kutta·MUSCL-TVD 설명은 [출판사 초록·소개](https://www.sciencedirect.com/science/article/abs/pii/S1463500311002010)와 일치한다. 외부 원문 보고서의 Beta_2 판정은 이 노트의 단일 B 행과 다른 항목이다.

| 위치 | 전 → 후 | 근거 원문 |
|---|---|---|
| `models/FUNWAVE/web-refs/funwave-foundational-papers.md:49` | `Celeris COULWAVE 모드 = 동일 완전비선형 식` → `COULWAVE 모드는 완전비선형 Boussinesq 방정식 계열에 속한다.` | 연결한 celeris-coulwave-theory.md §2의 제목은 동일 방정식족이다. 본문은 같은 클래스라고 설명한다. source·§3은 식 대응의 근거를 구조 식별로 한정한다. |

기계 확인 후보 판정:

- `:24 Froude 임계 초과 시 NLSW 전환 쇄파`: 오판이다. FT1-285의 문서 원문 칸은 정정 전 노트를 인용한다. 현재 본문 28줄은 수면고·수심 비 조건을 적는다.
- `src/masks.F:130` 뒤의 B 결론 문장: 오판이다. 노트 인용은 과거 커밋 `7b93138`의 130–131줄이다. 그 원문은 ABS(Eta)/MAX(DEPTH,MinDepthFrc) 조건이다. 인용 뒤의 표 구분자와 결론 문장은 코드 인용에 속하지 않는다.

상대 링크 18개는 대상 파일이 존재한다. Mermaid 블록은 없다. 금지 문자열과 한계 문장은 없다. 미해결 항목은 없다.

## 7. funwave-tvd-manual.md — 완료

대조한 대상은 14줄이다. 정정은 1줄이다. 인용 보완은 0줄이다.

| 대조 범위 | 대조 결과·원문 |
|---|---|
| 5–6 | 기존 PDF 변환본은 존재한다. 변환본의 제목에 Version 3.0·Release Dec 2016이 있다. 기존 인용 방식과 2026-10-18 보고서 반영 기록은 구분되어 있다. |
| 36 | FV1-550의 ZALPHA·중첩 경계 구분은 반영되어 있다. 다만 세 루틴을 모두 삼중대각 경계조건으로 묶은 문장은 3.0 p.9와 다르다. p.9 이미지에서 PHI_COLL·CAL_DISPERSION의 경계조건 제거와 GET_Eta_U_V_HU_HV의 경계조건 추가를 구분했다. |
| 45–53 | 빈 줄·절 제목·판본·보고서 링크·표 머리글을 확인했다. 판본은 AD1의 기준표와 현재 main.F:47에 맞는다. |
| 54–55 | 두 B 행의 결론은 v21-manual §5 및 AD2와 같다. 2.1 p.29 이미지의 TRIG·TRIG_PERIODIC 표기를 확인했다. 현재 etauv_solver.F:365·464–470·541–554·580–589와 과거 2e72b18:etauv_solver.F:358을 읽었다. 직렬·병렬·주기 호출과 유속 상한 처리는 결론과 일치한다. |

현재 init.F:665–680은 구면 분기 안의 ZALPHA 계수 재대입을 보인다. bc.F:1031–1050은 COUPLING 중첩 경계에서 혼합미분의 경계값 대입을 건너뛴다. dispersion.F:189–211도 중첩 경계에서 혼합미분의 벽 경계조건을 건너뛴다. etauv_solver.F:424–434는 삼중대각 우변에 중첩 경계의 유속을 반영한다. 두 차이 행의 분류와 결론을 바꾸는 최종 검증 판정은 없다.

| 위치 | 전 → 후 | 근거 원문 |
|---|---|---|
| `models/FUNWAVE/manual-notes/funwave-tvd-manual.md:36` | 세 루틴의 삼중대각 경계조건에 보정 적용 → PHI_COLL·CAL_DISPERSION의 분산항 경계조건 제거와 GET_Eta_U_V_HU_HV의 삼중대각 경계조건 추가를 별도 문장으로 구분 | 3.0 p.9의 판 변경 설명과 FV1-017·550. 현재 init.F:665–680, bc.F:1031–1050, dispersion.F:189–211, etauv_solver.F:424–434를 함께 인용했다. |

이 노트에 배정된 기계 확인 후보는 없다. 상대 링크 7개는 대상 파일이 존재한다. Mermaid 블록은 없다. 금지 문자열과 한계 문장은 없다. 미해결 항목은 없다.

## 최종 집계

아래 수치는 작업 시작 시 대상 줄 목록과 이번 작업 전후의 줄별 비교에서 셌다. 정정과 인용 보완은 서로 다른 줄로 집계했다. 모든 노트의 줄 수는 작업 시작 시와 같다. 위 정정 목록의 줄 번호는 최종 파일에서도 같다.

| 노트 | 대조한 줄 | 정정한 줄 | 인용 보완 줄 | 상태 |
|---|---:|---:|---:|---|
| funwave-build-and-blackwell-port.md | 51 | 4 | 0 | 완료 |
| funwave-v21-manual-differences.md | 31 | 0 | 0 | 완료 |
| funwave-code-graph.md | 39 | 2 | 1 | 완료 |
| funwave-wk-data2d-spectral-wavemaker.md | 37 | 4 | 1 | 완료 |
| funwave-validation-cases.md | 25 | 1 | 1 | 완료 |
| funwave-foundational-papers.md | 20 | 1 | 0 | 완료 |
| funwave-tvd-manual.md | 14 | 1 | 0 | 완료 |
| 합계 | 217 | 13 | 3 | 완료 |

사용자 지정 기계 확인 후보 12건은 중복 제시된 항목도 각각 판정했다. 모두 정정 전 문장 인용 또는 과거 커밋 인용을 현재 본문·코드와 혼동한 오판이다. 후보별 원문 대조 결과는 해당 노트 절에 적었다.

최종 기계 확인에서 이번 변경 16줄은 모두 최초 대상 줄에 포함되었다. 16줄 모두 지정한 정정·보완 표시를 갖는다. 표의 표시는 결론 문장 칸 끝에 있다. YAML의 표시는 값 밖 주석에 있다. 노트의 상대 링크 90개는 모두 실제 파일 또는 디렉터리를 가리킨다. 대상 줄에는 사용자 홈 절대 경로와 위키링크 구분자가 없다. 대상 줄에는 금지한 한계 문장이 없다. E 표의 정적 대조 성격 설명은 유지했다. 대상 노트에 Mermaid 블록은 없다. 대상 노트와 이 기록의 `git diff --check`는 통과했다.

쓰기 범위는 대상 노트와 이 기록이다. 노트의 최초 대상 줄 밖에 추가한 변경은 없다. 지정한 대상 줄을 모두 대조했으므로 종료 조건을 충족한다. 미해결 항목은 없다.
