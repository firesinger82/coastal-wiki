---
last_source_check: "2026-10-15 (recovery 대조 반영)"
verification_method: "2026-10-15 SWASH recovery 대조 보고서 반영"
---

# models/SWASH

> **Canonical source**: 이 디렉토리(`models/SWASH/`)가 SWASH 모델의 구현·메커닉에 대한 진실의 원천. `concepts/swash-zone/04-code-and-tools.md`·`concepts/waves/` 등은 여기로의 링크만 가짐.
>
> **10-15 대조 보고서의 노트 집계**: 직접 Markdown 목록은 source-analysis 21개·manual-notes 3개·web-refs 1개이다 ([inputs-setup:SI1-710](../../_staging/recovery/compare/swash-inputs-setup-vs-code.md#4-노트-대조와-수정안)). [10-15 대조 정정]
>
> 2026-06-16의 소스 160파일 전수 검수(workflow)는 과거 기록이다 (theory-framework:ST1-332). [10-15 대조 정정]
>
> 이번 식 대조의 범위는 아래 차이 표의 보고서가 제시한다 (theory-framework:ST1-332). [10-15 대조 정정]

## 정체 카드

- **이름**: **SWASH** (Simulating WAves till SHore) — `Swash.ftn90` main program 주석
- **정의**: **non-hydrostatic free-surface wave-flow 모델** — 파·조석·부력·바람 구동 비정상 회전류 + transport. 심해→해빈/항만 파 변형, rapidly varied flow, 밀도류(하구·호소). (repo README introduction)
- **저자/관리주체**: **Marcel Zijlema** 외 SWASH team — **TU Delft**, Faculty of Civil Engineering and Geosciences, **Environmental Fluid Mechanics Section** (`Swash.ftn90`). v1.00 2009-12.
- **라이선스**: **GPL v3** (`raw/source_code/swash/LICENSE`)
- **버전**: **12.01** (repo README badge)
- **공식 사이트**: [swash.sourceforge.io](https://swash.sourceforge.io)
- **GitLab**: [gitlab.tudelft.nl/citg/wavemodels/swash](https://gitlab.tudelft.nl/citg/wavemodels/swash)
- **docs**: [delftwaves.github.io/swash-docs](https://delftwaves.github.io/swash-docs/) · **docker**: delftwaves/swash
- **canonical 논문**: **Zijlema, Stelling, Smit (2011)** *Coastal Engineering* 58(10):992-1012, **doi:10.1016/j.coastaleng.2011.05.015** (repo README DOI badge)
- **소스 위치 (본 위키)**: `raw/source_code/swash/`의 Fortran 원문은 `.ftn90` 152개와 `.ftn` 8개를 합친 160개다 (`src/srclist.cmake:2–161`; theory-framework:ST1-330). [10-15 대조 정정]
- **사용 도메인**: 위상해상 **비정수압 천수**(non-hydrostatic shallow water) — 연안 파 변형·surf zone·**처오름(swash)**·항만 정온·밀도류. SWAN(위상평균)이 못하는 개별 파·shoreline 운동 해상.
- **격자**: structured(curvilinear) + **unstructured**(SWAN grid 공유, `SwanReadADCGrid` = ADCIRC fort.14 reader). multi-layer(z) 또는 depth-averaged.
- **수치 기법**: 비정수압 압력 보정(pressure Poisson) + 천수방정식 finite-difference/volume. **explicit/implicit × depth/layer-averaged** 4×조합 solver. 시초 알고리즘 = **Stelling & Zijlema 2003**(non-hydrostatic free-surface FD).

## 모델 분류 — 위상해상 비정수압 (SWAN 계열 인프라)

- [`models/FUNWAVE/`](../FUNWAVE/)·[`models/Celeris/`](../Celeris/)(Boussinesq) 와 **같은 위상해상 class** 이나, SWASH 차별점 = **비정수압(non-hydrostatic) 다층 천수** 접근(Boussinesq 의 고차 분산항 대신 연직 층분할 + 비정수압 압력으로 분산 표현). 층 수 ↑ 시 깊은 물 분산 정확.
- **SWAN(위상평균)과 같은 TU Delft 그룹** — OCP(Ocean Pack) 인프라·MPI(`SWINITMPI`)·unstructured grid topology(`SwanGrid*`) 공유. SWAN(광역 spectral) → SWASH(항내·swash 위상해상) nesting 자연.
- 비구조 MPI는 지원하지 않는다 (원자료 `README.md:245`; `src/SwashReadInput.ftn90:2481–2484`; theory-unstructured:ST2-421). [10-15 대조 정정]
- [`concepts/swash-zone/04-code-and-tools.md §3`](../../concepts/swash-zone/04-code-and-tools.md) 에서 신설 후보로 식별 → 본 디렉토리로 충족.

## 핵심 논문 (web-refs 상세)

- **SWASH 원논문**: Zijlema, M., Stelling, G., Smit, P. (2011) "SWASH: An operational public domain code for simulating wave fields and rapidly varied flows in coastal waters" *Coastal Engineering* **58**(10):992-1012, doi:10.1016/j.coastaleng.2011.05.015
- **수치 시초**: Stelling, G., Zijlema, M. (2003) "An accurate and efficient finite-difference algorithm for non-hydrostatic free-surface flow with application to wave propagation" *Int. J. Numer. Methods Fluids* **43**:1-23
- **쇄파**: Smit, P., Zijlema, M., Stelling, G. (2013) "Depth-induced wave breaking in a non-hydrostatic, near-shore wave model" *Coastal Engineering* **76**:1-16

→ 상세: [`web-refs/swash-official-resources.md`](web-refs/swash-official-resources.md)

## 하위 디렉토리 현황

10-15 대조 보고서는 직접 Markdown 목록을 21개·3개·1개로 집계했다 (inputs-setup:SI1-710; theory-framework:ST1-332). 현재 `source-analysis/*.md`·`manual-notes/*.md`·`web-refs/*.md`의 직접 목록은 21개·4개·1개다. 매뉴얼 목록에는 [빌드·실행 파일 대조 노트](manual-notes/swash-build-run-differences.md)가 추가되어 있다. [10-15 전수 검증 정정]

| 경로 | 상태 | 비고 |
|---|---|---|
| `source-analysis/` | 보고서 집계 21개 | [아키텍처](source-analysis/swash-architecture-source-map.md), [비정수압 압력](source-analysis/swash-nonhydrostatic-pressure-solver.md), [출력 소스](source-analysis/swash-output.md). [10-15 대조 정정] |
| `manual-notes/` | 현재 직접 목록 4개 | [사용자 설명서](manual-notes/swash-user-manual.md), [기술문서 개요](manual-notes/swash-tech-documentation-overview.md), [기술문서 보존식](manual-notes/swash-tech-ch2-ch5-mimetic-conservation.md), [빌드·실행 파일 대조](manual-notes/swash-build-run-differences.md). [10-15 전수 검증 정정] |
| `web-refs/` | 보고서 집계 1개 | [공식 자료](web-refs/swash-official-resources.md). [10-15 대조 정정] |
| `raw/source_code/swash/` | Fortran 원문 160개 | `.ftn90` 152개와 `.ftn` 8개를 합친 수다 (`src/srclist.cmake:2–161`). [10-15 대조 정정] |

## 관련 판독 자료 [10-15 전수 검증 정정]

- `SwashImpDep2DHflow`는 비정수압 수심 평균 2D 시간 적분을 수행한다 (`src/SwashImpDep2DHflow.ftn90:40–61`). `SwashSolvers`에는 BiCGSTAB과 삼중대각 해법이 있다 (`src/SwashSolvers.ftn90:3312,4297`). `SwashBCtransferfnc`는 수면과 층평균 수평 속도의 2차 전달함수를 계산한다 (`src/SwashBCtransferfnc.ftn90:40–51`). [10-15 전수 검증 정정]
- manual-notes에는 사용자 설명서 노트와 기술문서 노트가 있다 (위 현황 표; theory-framework:ST1-331). [10-15 대조 정정]
- 빌드·실행 파일의 문서·코드 차이는 [별도 노트](manual-notes/swash-build-run-differences.md)에 정리되어 있다. [10-15 전수 검증 정정]
- [처오름대 모델 설명](../../concepts/swash-zone/04-code-and-tools.md)의 §3은 SWASH 노트에 연결되어 있다 (`concepts/swash-zone/04-code-and-tools.md:39–42`). [10-15 전수 검증 정정]

## 문서와 코드 차이 (10-15 대조)

문서 판: SWASH 12.01 매뉴얼 swashuse·swashtech(공개 저장소 `7949227`, 2026-05-06, "release v12.01"에서 마지막 변경); 코드 판: `VERNUM 12.01`, 공개 저장소 main `a486d5f`(2026-05-26, 12.01 뒤 `608ffd7`·`9554c98` 포함).

문서 인용의 인쇄 쪽은 PDF 쪽에서 8을 뺀 값이다. 다음 표의 `README.md:5,18,41,42,44`는 대조 전 `models/SWASH/README.md`의 줄 번호다. 표의 21개·3개·1개는 보고서 작성 시점의 직접 Markdown 목록이다. [10-15 전수 검증 보완]

근거 보고서: [inputs-setup](../../_staging/recovery/compare/swash-inputs-setup-vs-code.md#5-차이-결론), [outputs](../../_staging/recovery/compare/swash-outputs-vs-code.md#5-차이-결론), [theory-framework](../../_staging/recovery/compare/swash-theory-framework-vs-code.md#5-차이-결론), [theory-unstructured](../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#5-차이-결론).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| inputs-setup:SI1-710 | README 수량·하위 노트 상태 | `models/SWASH/README.md:5` “160 Fortran”, “source-analysis 19 + manual-notes 2”; `:18` “src/ 152 Fortran”; `:41` “2 verified”; `:42` “(미생성)” | 불일치(B). 읽기 전용 파일 목록에서 Fortran 160개·source-analysis 21개·manual-notes 3개·web-refs 1개이다. src 전체 파일은 162개이다. | B | 2026-10-15 파일 목록은 .ftn90 152개+.ftn 8개이다. CMake 파일 2개를 포함한 src 전체는 162개이다. 노트는 source-analysis 21개·manual-notes 3개·web-refs 1개이다. 파일 수를 검증 완료율로 바꾸지 않는다. |
| outputs:SO1-297 | 현재 노트의 현황 표 | models/SWASH/README.md:42 ``\| `manual-notes/` \| (미생성) \| swashuse/swashtech/swashimp 매뉴얼 — swash.sourceforge.io online_doc \|`` | models/SWASH/manual-notes/swash-user-manual.md:235 `## 11. 출력 (§4.6)`가 이미 존재한다. source-analysis/swash-output.md도 존재한다. | B 문서 오기 | manual-notes/swash-user-manual.md와 source-analysis/swash-output.md가 존재한다. README의 미생성 표기를 고쳐야 한다. [10-15 전수 검증 정정] |
| theory-framework:ST1-330 | Fortran 파일 수 | `README.md:18` `src/`와 `152 Fortran`; `README.md:44` `v12.01, src 152 Fortran`. | 원본 `src/` 직접 파일 목록은 `.ftn90` 152개·`.ftn` 8개이다. `src/CMakeLists.txt`와 `src/srclist.cmake`는 Fortran 파일이 아니다. `src/srclist.cmake:2–161`은 160개 항목을 등록한다. 공개 git의 모든 참조에 있는 92커밋을 `git show REV:src`로 읽으면 src가 있는 80개 트리의 Fortran 수는 143·148·156·158·159·160 중 하나이다. | B 문서 오기 (현재 노트) | 현재 Fortran 원문은 `.ftn90` 152개와 `.ftn` 8개를 합친 160개다. 직접 파일 전체는 빌드 파일 둘을 포함한 162개다. 공개 이력에서 전체 Fortran이 152개인 소스 트리는 없다. 152는 현재 `.ftn90`만 센 값이며 판 차이가 아니라 집계 범위의 오기이다. [git 판정 AD §3](../../_staging/recovery/compare/SWASH-git-verify-AD.md)의 B를 유지한다. |
| theory-framework:ST1-331 | manual-notes 존재 여부 | `README.md:42` `(미생성)` | `manual-notes/swash-tech-ch2-ch5-mimetic-conservation.md:14` `# swashtech Ch2·Ch5 — Hamiltonian·mimetic 이산화·보존 증명`; 현재 직접 목록에 `swash-tech-documentation-overview.md`, `swash-tech-ch2-ch5-mimetic-conservation.md`, `swash-user-manual.md`가 있다. | B 문서 오기 (현재 노트) | manual-notes에는 현재 세 파일이 있다. 미생성 표시를 제거한다. 검증 범위는 각 노트의 원문 근거와 이번 보고서 범위를 함께 적는다. [10-15 전수 검증 정정] |
| theory-framework:ST1-332 | 노트 현황과 과거 전수 주장 | `README.md:5` `**source-analysis 19 + manual-notes 2(swashtech·swashuse) + web-refs 1**`; 같은 줄 `소스 160파일 전수 검수(workflow)`. | `Path('models/SWASH', name).glob('*.md')`의 현재 직접 목록은 source-analysis 21·manual-notes 3·web-refs 1이다. 이번 문서 대조의 대상은 PDF p.1–66과 §2·3에 인용한 코드 경로이다. | C 문서 누락 (현재 노트) | 현황표에는 현재 파일 수 21·3·1과 집계 기준을 적는다. 과거 전수 검수 기록과 이번 식 대조의 범위를 구별한다. 파일 존재 개수를 새 검증 완료 개수로 바꾸지 않는다. |
| theory-unstructured:ST2-427 | 원문 파일 수·노트 현황의 집계 단위 | models/SWASH/README.md:18 ``- **소스 위치 (본 위키)**: ✅ `raw/source_code/swash/` (gitignore 로컬, GitLab clone — `src/` 152 Fortran)``; :41의 상태 셀 `✅ 2 verified`; :42의 상태 셀 `(미생성)` | `rg --files models/SWASH/raw/source_code/swash/src`의 파일 목록에서 `.ftn90`는 152파일이고 `.ftn`은 8파일이다. 두 CMake 파일을 포함한 `src` 일반 파일 수는 162다. 현재 `source-analysis/*.md`는 21파일이다. 대조 시점 `manual-notes/*.md`는 3파일이다. 10-15 반영으로 `manual-notes/swash-build-run-differences.md`가 더해져 현재 4파일이다. 이는 파일 목록 집계이며 코드 실행 결과가 아니다. | B 문서 오기(현재 노트) | src의 Fortran 원문은 .ftn90 152개와 .ftn 8개를 합친 160개다. CMake 파일 두 개를 포함하면 일반 파일은 162개다. source-analysis의 Markdown 파일은 21개다. manual-notes의 Markdown 파일은 대조 시점 3개, 10-15 반영 뒤 4개다(54행 현황 표와 같다). [10-15 표본 정정] 노트 파일의 존재 수와 검증 완료 수를 구별한다. [SWASH-git-verify-AD.md §3 ST2-427](../../_staging/recovery/compare/SWASH-git-verify-AD.md). 읽기 전용 `git log --all`의 92커밋에서 `git show REV:src`로 확인한 소스 트리 80개는 Fortran 파일 수가 143·148·156·158·159·160 중 하나다. 152개인 트리는 없다. main은 91커밋이다. 152는 현재 .ftn90만 센 값이므로 판 차이 A가 아니라 집계 범위의 B를 유지한다. |

## 코드 결함 후보 (10-15 대조)

문서 판: SWASH 12.01 매뉴얼 swashuse·swashtech(공개 저장소 `7949227`, 2026-05-06, "release v12.01"에서 마지막 변경); 코드 판: `VERNUM 12.01`, 공개 저장소 main `a486d5f`(2026-05-26, 12.01 뒤 `608ffd7`·`9554c98` 포함).

근거 보고서: [theory-framework](../../_staging/recovery/compare/swash-theory-framework-vs-code.md#5-차이-결론), [theory-unstructured](../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#5-차이-결론), [inputs-setup](../../_staging/recovery/compare/swash-inputs-setup-vs-code.md#5-차이-결론), [inputs-physics-numerics](../../_staging/recovery/compare/swash-inputs-physics-numerics-vs-code.md#5-차이-결론), [outputs](../../_staging/recovery/compare/swash-outputs-vs-code.md#5-차이-결론), [guide-syntax-build](../../_staging/recovery/compare/swash-guide-syntax-build-vs-code.md#5-차이-결론), [callflow](../../_staging/recovery/flow/SWASH-callflow.md#8-차이-결론).

이 표의 E는 위 보고서가 문서·소스의 정적 대조에서 분류한 코드 결함 후보이다. [10-15 전수 검증 정정]

| 행 ID | 위치(file:line) | 내용 한 문장 | 강도 | 상세 노트(상대 링크) |
|---|---|---|---|---|
| theory-framework:ST1-294 | `src/SwashWindStress.ftn90:984–989` | 문서는 최대 수위의 crest배를 쓰지만 코드는 1−crest배 미만의 응력을 0으로 만든다. | 중간 | [swash-bottom-friction-wind](source-analysis/swash-bottom-friction-wind.md) |
| theory-framework:ST1-310 | `src/SwashExpDep2DHflow.ftn90:4905`<br>`src/SwashExpDep1DHflow.ftn90:1626` | 진단은 `\sum_c\zeta_c`를 출력한다. | 중간 | [swash-explicit-depthavg-flow](source-analysis/swash-explicit-depthavg-flow.md) |
| theory-framework:ST1-333 | `src/SwashExpDep1DHflow.ftn90:1626`<br>`src/SwashExpDep2DHflow.ftn90:4905` | 구조 격자의 ITEST 체적 진단은 면적·길이를 곱하지 않은 수위 합을 출력한다. | 중간 | [swash-implicit-depthavg-flow](source-analysis/swash-implicit-depthavg-flow.md) |
| theory-unstructured:ST2-039 | `src/SwashExpDepUflow.ftn90:1741`<br>`src/SwashImpDepUflow.ftn90:1923`<br>`src/SwashExpLayUflow.ftn90:2865`<br>`src/SwashImpLayUflow.ftn90:3036` | 해석: 비구조 유동 네 경로의 ITEST 체적 진단은 셀 면적 없이 수위를 합한다. | 강함 | [swash-explicit-depthavg-flow](source-analysis/swash-explicit-depthavg-flow.md) |
| theory-unstructured:ST2-365 | `src/SwashExpDepUflow.ftn90:718,789`<br>`src/SwashImpDepUflow.ftn90:341,412` | 비구조 수심 평균의 명시적·반음해 유동은 마른 면에서 cbot 배열 전체를 0으로 만든다. | 강함 | [swash-implicit-depthavg-flow](source-analysis/swash-implicit-depthavg-flow.md) |
| theory-unstructured:ST2-371 | `src/SwashUWindStress.ftn90:458` | 코드는 `(1.-wcrstp) * smax(iface)`를 사용한다. | 중간 | [swash-bottom-friction-wind](source-analysis/swash-bottom-friction-wind.md) |
| theory-unstructured:ST2-403 | `src/SwashReadInput.ftn90:1540–1546` | SOLVER를 쓰고 MAXITER를 생략하면 상한은 100이다. | 중간 | [swash-linear-solvers](source-analysis/swash-linear-solvers.md) |
| theory-unstructured:ST2-416 | `src/SwashUpdateUData.ftn90:403–404` | 비구조 조파의 초기 상대좌표 계산은 y좌표에서 x0를 뺀다. | 강함 | [swash-boundary-wave-forcing](source-analysis/swash-boundary-wave-forcing.md) |
| inputs-setup:SI1-155 | `src/SwashReadInput.ftn90:2236–2238,2265–2268` | CGRID에서 EXCEPTION과 REPEATING을 함께 쓰면 코드는 REPEATING을 먼저 읽는다. | 중간 | [swash-user-manual](manual-notes/swash-user-manual.md) |
| inputs-setup:SI1-229 | `src/SwashInputField.ftn90:188`<br>`src/ocpmix.ftn:963–965` | 해석: 문서가 금지한 `fac=0`을 일반 입력장에서 사전 거부하지 않는다. | 약함 | [swash-initialization-grid](source-analysis/swash-initialization-grid.md) |
| inputs-setup:SI1-260 | `src/SwashInputField.ftn90:394–396` | READTRANS·READAMB의 다층 직접 파일 입력은 첫 층 뒤에 파일을 닫는다. | 강함 | [swash-initialization-grid](source-analysis/swash-initialization-grid.md) |
| inputs-setup:SI1-355 | `src/SwashReadInput.ftn90:981,983`<br>`src/ocpcre.ftn:342–348` | FLOAT의 위치 숫자는 INREAL에 도달하기 전에 필수 키워드 읽기에서 건너뛰어진다. | 강함 | [swash-input-parsing-check](source-analysis/swash-input-parsing-check.md) |
| inputs-setup:SI1-513 | `src/SwashInputGrid.ftn90:388` | 입력 격자 동일성 검사는 dxinp·dyinp를 비교하지 않는다. | 강함 | [swash-initialization-grid](source-analysis/swash-initialization-grid.md) |
| inputs-setup:SI1-534 | `src/SwashBounCond.ftn90:193,892,1402–1405` | LRIEMANN 뒤의 RIEMANN 명령은 lriem의 true 상태를 물려받을 수 있다. | 강함 | [swash-boundary-wave-forcing](source-analysis/swash-boundary-wave-forcing.md) |
| inputs-setup:SI1-535 | `src/SwashBounCond.ftn90:416–421` | 비정형 XY 경계점 검색이 실패하면 level 2 오류 뒤에 vert(-1)을 참조한다. | 강함 | [swash-boundary-wave-forcing](source-analysis/swash-boundary-wave-forcing.md) |
| inputs-setup:SI1-549 | `src/SwashCheckPrep.ftn90:591–601`<br>`src/SwashBCStokeswave.ftn90:101,166,245,334` | 파형 계산은 속도층 1–4만 구현하므로 속도 8층·압력 2층에서는 계수 0이 남는 E 후보이다. | 강함 | [swash-boundary-wave-forcing](source-analysis/swash-boundary-wave-forcing.md) |
| inputs-setup:SI1-560 | `src/SwashSpongeLayer.ftn90:100,112–113` | 구면 1D 스펀지는 미터 폭과 도 단위 dx를 함께 사용한다. | 강함 | [swash-boundary-wave-forcing](source-analysis/swash-boundary-wave-forcing.md) |
| inputs-setup:SI1-571 | `src/SwashBounCond.ftn90:293–296` | 주파수 모양을 생략한 BOUND SHAPE MEAN 반복은 PEAK 상태로 돌아갈 수 있다. | 강함 | [swash-user-manual](manual-notes/swash-user-manual.md) |
| inputs-physics-numerics:SI2-030 | `src/SwashWindStress.ftn90:984–987`<br>`src/SwashUWindStress.ftn90:458` | 두 코드 경로는 1−crest배를 사용한다. | 중간 | [swash-bottom-friction-wind](source-analysis/swash-bottom-friction-wind.md) |
| inputs-physics-numerics:SI2-111 | `src/SwashCheckPrep.ftn90:379–381` | 위도 0이면 명시한 비영 fpar도 선행 검사에서 해제된다. | 강함 | [swash-user-manual](manual-notes/swash-user-manual.md) |
| inputs-physics-numerics:SI2-141 | `src/SwashExpLay1DHtrans.ftn90:472` | 활성 침식 대입에는 rhos 환산이 없다. | 강함 | [swash-scalar-transport](source-analysis/swash-scalar-transport.md) |
| inputs-physics-numerics:SI2-181 | `src/SwashCheckPrep.ftn90:1273,1277`<br>`src/SwashExpDep1DHflow.ftn90:1250` | NONHYDROSTATIC `theta=0`은 준비 검사를 통과한다. | 강함 | [swash-nonhydrostatic-pressure-solver](source-analysis/swash-nonhydrostatic-pressure-solver.md) |
| inputs-physics-numerics:SI2-194 | `src/SwashReadInput.ftn90:1543,1546` | SOLVER를 쓰고 maxiter를 생략하면 상한은 100이다. | 중간 | [swash-user-manual](manual-notes/swash-user-manual.md) |
| outputs:SO1-067 | `src/SwashQuanOutp.ftn90:2430–2431,2453–2459` | Cartesian·QUANTITY FRAME의 VDIR은 회전한 VEL에 프레임 회전각을 다시 더한다. | 강함 | [swash-output](source-analysis/swash-output.md) |
| outputs:SO1-100 | `src/SwashInit.ftn90:111,680` | 헤더의 N/m2는 수치의 m²/s²와 맞지 않으므로 E 후보를 유지한다. | 강함 | [swash-output](source-analysis/swash-output.md) |
| outputs:SO1-115 | `src/SwashElemOutp.ftn90:304` | ELEMESH의 SED는 rp에 rhos를 곱하지 않는다. | 강함 | [swash-output](source-analysis/swash-output.md) |
| outputs:SO1-119 | `src/SwashAverOutp.ftn90:121` | HSIG는 제곱합만 `N−1`로 나눈 뒤 표본 평균의 제곱을 뺀다. | 강함 | [swash-output](source-analysis/swash-output.md) |
| outputs:SO1-128 | `src/SwashElemOutp.ftn90:425` | ELEMESH의 MSED는 mcons에 rhos를 곱하지 않는다. | 강함 | [swash-output](source-analysis/swash-output.md) |
| outputs:SO1-140 | `src/SwashElemOutp.ftn90:710` | ELEMESH의 SEDK는 rp에 rhos를 곱하지 않는다. | 강함 | [swash-output](source-analysis/swash-output.md) |
| outputs:SO1-149 | `src/SwashQuanOutp.ftn90:189,2277,3324` | 다층 속도 격자의 `ihydro=3`에서 PRESSK는 압력 계산을 생략한 보조배열의 0을 출력한다. | 중간 | [swash-output](source-analysis/swash-output.md) |
| outputs:SO1-150 | `src/SwashInit.ftn90:111,1356` | 헤더의 N/m2는 수치의 m²/s²와 맞지 않으므로 E 후보를 유지한다. | 강함 | [swash-output](source-analysis/swash-output.md) |
| outputs:SO1-158 | `src/SwashElemOutp.ftn90:734` | ELEMESH의 MSEDK는 mcons에 rhos를 곱하지 않는다. | 강함 | [swash-output](source-analysis/swash-output.md) |
| outputs:SO1-170 | `src/SwashQuanOutp.ftn90:2430–2431,2459` | Cartesian FRAME의 VDIR은 이미 회전한 VEL에 alcq를 다시 더한다. | 강함 | [swash-output](source-analysis/swash-output.md) |
| outputs:SO1-205 | `src/ocpmix.ftn:1242–1243,1251–1252` | 초기 `IENT=0`에서 양의 ITRACE는 지정 횟수보다 한 번 더 출력을 허용한다. | 강함 | [swash-grid-oceanpack-infra](source-analysis/swash-grid-oceanpack-infra.md) |
| outputs:SO1-220 | `src/SwashAverOutp.ftn90:96–97,119,121` | HSIG 식의 제곱합 분모는 `N−1`이고 평균 수위의 분모는 N이다. | 강함 | [swash-output](source-analysis/swash-output.md) |
| outputs:SO1-267 | `src/SwashInit.ftn90:485–488`<br>`src/SwashCheckPrep.ftn90:5773–5774,5807` | 반복 COMPUTE는 평균 합을 지우지만 평균 표본 카운터를 재설정하지 않는다. | 강함 | [swash-output](source-analysis/swash-output.md) |
| outputs:SO1-271 | `src/SwashReadTestpnts.ftn90:158–159,170–171,179–180` | TEST는 유효한 51번째 점을 배열에 쓴 뒤 최대 점 수를 검사한다. | 강함 | [swash-input-parsing-check](source-analysis/swash-input-parsing-check.md) |
| guide-syntax-build:SG1-612 | `src/SwashReadInput.ftn90:981–983,1218–1227` | FLOAT의 위치 수치 입력은 선행 INKEYW(REQ)에서 건너뛴다. | 강함 | [swash-floating-rigid-body](source-analysis/swash-floating-rigid-body.md) |
| guide-syntax-build:SG1-795 | `src/CMakeLists.txt:56,67,75` | 별도 모듈 경로가 필요한 일반 컴파일러 구성에서는 컴파일 조건이 빠질 수 있어 E 중간을 유지한다. | 중간 | [swash-build-run-differences](manual-notes/swash-build-run-differences.md) |
| guide-syntax-build:SG1-796 | `switch.pl:49–50`<br>`src/CMakeLists.txt:19` | 기존 생성 소스가 원문보다 새로우면 MPI 옵션 변경만으로 switch.pl의 재생성 조건을 만족하지 않는다. | 강함 | [swash-build-run-differences](manual-notes/swash-build-run-differences.md) |
| callflow:RF-016 | `src/SwashBackup.ftn90:300,310,316`<br>`src/SwashInitCond.ftn90:392,399,404` | 비구조 백업·재시작은 정점 수로 셀 수위와 면 속도 배열을 순회한다. | 강함 | [swash-output](source-analysis/swash-output.md) |
