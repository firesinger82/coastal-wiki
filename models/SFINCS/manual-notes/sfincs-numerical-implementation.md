---
title: "SFINCS 모델 개요 + 수치 구현 — 공식 readthedocs RST 발췌 (overview·numerical_implementation·developments)"
model: SFINCS
doc: "docs/overview.rst · docs/numerical_implementation.rst · docs/developments.rst (readthedocs source)"
canonical_source: manual
citation_status: verified
verification_method: >
  /home/firesinger/coastal-wiki/models/SFINCS/raw/source_code/sfincs/docs/ 의
  overview.rst, numerical_implementation.rst, developments.rst 3개 RST 파일을 직접 Read.
  인용한 모든 section 제목·기본값·식·문단은 작성 전 해당 RST 본문에서 직접 확인.
  RST 는 page 가 없으므로 section heading 으로 인용.
  주의: numerical_implementation.rst 는 작성 시점에 section heading 만 존재하고
  본문이 비어 있는 skeleton 상태 — 본 노트는 그 사실을 명시하고, 실제 수치 메커닉은
  overview.rst / developments.rst 의 서술 + changelog 기본값에서만 인용.
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "[[../source-analysis/sfincs_flow_solver]]"
  - "[[../source-analysis/sfincs_subgrid_quadtree]]"
  - "[[../source-analysis/sfincs-architecture-source-map]]"
---

# SFINCS 모델 개요 + 수치 구현 (공식 문서)

공식 readthedocs RST 소스 3개의 발췌·정리. **이론(문서)↔코드(source-analysis) 대응**을 함께 기록한다.

> ⚠️ **문서 상태 경고 (검증된 관찰)**: `numerical_implementation.rst` 는 작성 시점에 모든 section 제목만 존재하고 **본문이 비어 있다** (skeleton). 즉 `docs/numerical_implementation.rst §Shallow water equations`, `§Momentum equations`, `§Advection`, `§Continuity equation`, `§Stability conditions` 등은 제목만 있고 식·서술이 없다. 따라서 아래 수치 메커닉 단언은 **`overview.rst` 및 `developments.rst` 의 서술 + changelog 기본값**에서만 인용했고, 실제 식·이산화는 source-analysis(`self` canonical) 노트로 cross-link 한다. 문서 본문이 채워지면 보강 필요.

---

## 1. SFINCS 정체 — reduced-complexity / reduced-physics

| 항목 | 내용 | 출처 |
|---|---|---|
| 약자 | Super-Fast INundation of CoastS | `docs/overview.rst §What is SFINCS?` |
| 분류 | reduced-complexity model, compound flooding 시뮬레이션 | 동 |
| 설계 철학 | "high computational efficiency balanced with an adequate accuracy" | 동 |
| 수치 베이스 | momentum·continuity 방정식을 **first order explicit scheme** 으로 풂, **Bates et al. (2010)** 기반 | 동 |
| 원논문 | Leijnse et al. (2020), https://doi.org/10.1016/j.coastaleng.2020.103796 | 동 |

`docs/overview.rst §What is SFINCS?` 의 핵심 문장 그대로(verbatim 키워드):
> "a set of momentum and continuity equations are solved with a **first order explicit scheme** based on Bates et al. (2010)."

### 1.1 두 가지 운동량 버전 (LIE vs SSWE)

`docs/overview.rst §What is SFINCS?`:

| 버전 | 이류항(advection) | 적용 조건 |
|---|---|---|
| **SFINCS-LIE** (traditional) | **neglect** (advection 무시) | sub-critical flow 에 일반적으로 정당화됨 |
| **SFINCS-SSWE** | **포함** (advection 포함) | super-critical flow 또는 wave 모델링 시 필요 |

> LIE = Linear Inertial Equations, SSWE = (Simplified) Shallow Water Equations 의 함의. 문서는 약자를 풀어쓰지 않고 "SFINCS-LIE"/"SFINCS-SSWE" 로만 표기. → **코드 대응**: 이류항 on/off 및 advection scheme(`upw1`/`original`)은 [[../source-analysis/sfincs_flow_solver]] 의 `compute_fluxes`/`sfincs_advection_diffusion.f90` 참조.

### 1.2 왜 SFINCS인가 — 속도/정확도 trade-off 의 위치

`docs/overview.rst §Why SFINCS?`:
- 기존 접근: **bathtub** = 빠르지만 너무 단순 / **Delft3D, XBeach** = 정확하지만 너무 느림.
- SFINCS = 그 중간. 확률론적(stochastic) 대량 시나리오, 고해상도, 대규모에 적합 → quickscan 도구.
- 매우 고상세(형태역학·염분 등)가 필요하면 Delft3D FM Suite 를 쓰라고 명시 (scope 분리).

---

## 2. Compound flooding 구성요소

`docs/overview.rst §Compound flooding?`:
- 정의: 연안에서 **high sea levels + large river discharges + local precipitation** 의 상호작용으로 (극한) 홍수 발생 (Wahl et al., 2015).
- SFINCS 가 포함하는 forcing(verbatim):
  > "SFINCS includes **fluvial, pluvial, tidal, wind- and wave-driven processes**!"

| Forcing | 의미 |
|---|---|
| fluvial | 하천 유량 |
| pluvial | 국지 강우 |
| tidal | 조석 |
| wind-driven | 바람 setup |
| wave-driven | 파랑 구동 |

### 2.1 적용 모델 유형 (`docs/overview.rst §Application areas`)

| 유형 (section) | 주 forcing / 특징 |
|---|---|
| Coastal model | 조석·storm surge·국지 wind setup·wave; 보통 offshore 경계를 swash zone(약 수심 2 m)에 둠; 2 m 보다 깊은 셀은 inactive 처리로 가속 |
| Coral reef model | 개별 파(individual waves)로 wave-driven flooding 계산; SIDS 에 큰 기여 |
| Tsunami model | 보통 overland 모델, offshore 모델 결과를 tsunami wave 로 입력; Robke et al. 2021 에서 offshore propagation 도 SFINCS 로 계산 |
| Storm surge model | offshore storm surge (열대저기압) 테스트 단계 |
| Riverine model | 상류 discharge 점 시계열 + 하류 water level 시계열(sub-critical 시 상류 영향) + 국지 강우 |
| Urban model | 공간변화 manning roughness·infiltration; **curve number** 침투; thin dam·levee·sea wall·pump·culvert 구조물 |
| Flash flood model | 단시간 강우 + 급경사 → 큰 수심·유속 |
| Compound flooding model | 위 모든 forcing 을 한 도메인에 결합 |

출처: `docs/overview.rst §Coastal model`, `§Coral reef model`, `§Tsunami model`, `§Storm surge model`, `§Riverine model`, `§Urban model`, `§Flash flood model`, `§Compound flooding model`.

---

## 3. 수치 구현 — 문서 구조 + 코드 대응

> 아래 표의 "문서 본문" 컬럼이 **(skeleton)** 인 항목은 `numerical_implementation.rst` 에 제목만 존재. 실제 식·구현은 source-analysis(코드 직접) 로 대체 cross-link.

`docs/numerical_implementation.rst` 의 section 트리 (직접 확인한 heading):

| Section (RST heading) | 문서 본문 | 코드 대응 (source-analysis) |
|---|---|---|
| `§Introduction` | "Based on Leijnse (2018)" 한 줄만 | — |
| Flow-related processes › `§Shallow water equations` | (skeleton) | [[../source-analysis/sfincs_flow_solver]] |
| › `§Numerical grid` | (skeleton) | [[../source-analysis/sfincs_subgrid_quadtree]] (quadtree/staggered) |
| › `§Momentum equations` | (skeleton) | `sfincs_momentum.f90` → flow_solver §운동량 |
| › `§Advection` | (skeleton) | `sfincs_advection_diffusion.f90` → flow_solver |
| › `§Continuity equation` | (skeleton) | `sfincs_continuity.f90` → flow_solver |
| › `§Stability conditions` | (skeleton) | CFL/uvmax → §3.3 아래 |
| Wave-related processes › `§Swash zone modelling approach` | (skeleton) | [[../source-analysis/sfincs_snapwave]] |
| › `§Weakly reflective generating-absorbing boundary condition` | (skeleton) | [[../source-analysis/sfincs_nonhydrostatic_wavemaker]] |
| › `§Wave generation` | "(Work in progress)" | wavemaker |
| › `§Wave-induced setup` | "(Work in progress)" | SnapWave wave forces |
| Other processes › `§Infiltration`/`§Precipitation`/`§Discharge points`/`§Wind forcing` | (skeleton) | [[../source-analysis/sfincs_boundaries_forcing]] |
| `§Model limitations` / `§Computational efficiency` | (skeleton) | — |

출처: `docs/numerical_implementation.rst` (section heading 전체를 직접 Read 로 확인; 본문 부재도 확인).

### 3.1 지배방정식 (reduced SWE) — 문서가 명시한 수준

문서가 **본문으로 단언한** 것은 §1.1 의 두 가지뿐:
- reduced SWE = momentum + continuity, **1차 explicit**, Bates et al. (2010) 기반 (`overview.rst §What is SFINCS?`).
- advection 포함 여부로 LIE/SSWE 분기 (동).

> 운동량/연속 방정식의 구체적 형태(식)는 RST 본문에 없음 → **날조 금지**. 식 레벨은 [[../source-analysis/sfincs_flow_solver]] (코드 직접) 및 원논문 Leijnse et al. (2021) 참조. Linear Inertial Equation 의 subgrid 보정 식은 Van Ormondt et al. (2025), https://doi.org/10.5194/gmd-18-843-2025 (`overview.rst §Publications`, `developments.rst §col d'Eze`).

### 3.2 Subgrid (문서가 서술한 메커닉) — `developments.rst`

`numerical_implementation.rst` 는 비었지만, `developments.rst §Recent advancements in accuracy: subgrid mode` 에 subgrid 의 **개념 서술**이 존재한다 (검증됨):

| 질문 (RST sub-section) | 핵심 (요약) |
|---|---|
| `§What are subgrid features?` | flux 계산은 **거친 격자**, water level 갱신은 **훨씬 고해상도**. 고해상도 지형정보를 유지하며 가속 |
| `§Why subgrid features?` | grid 를 2배 정세화하면 CFL 시간스텝 제약 때문에 runtime 이 $2^3$ 배. subgrid 로 continuity 갱신을 우회 |
| `§How does it work?` | 전처리에서 셀별 **water level↔volume 관계 table** 을 고해상도 지형으로 도출 → 런타임에 거친 격자 flux 후 정확한 수위 추정; flux 용으로는 대표 수심(representative water depth) 결정 |
| `§Increase in computational efficiency?` | 100 m → 200 m 격자로 flux 계산 시 약 **factor 8** 가속 (CFL 제약상) |

식 표현 (문서의 $2^3$ 서술을 LaTeX 로):
$$\text{runtime} \propto \left(\frac{1}{\Delta x}\right)^{3} \quad\Rightarrow\quad \Delta x:100\to200\,\text{m} \;\Rightarrow\; \text{speedup} \approx 2^3 = 8$$

출처: `developments.rst §What are subgrid features?`, `§Why subgrid features?`, `§How does it work?`, `§Increase in computational efficiency?`.

> **코드 대응**: subgrid look-up table 도출·소비(volume↔level, depth↔level 1D 보간)는 [[../source-analysis/sfincs_subgrid_quadtree]] (sfincs_subgrid.F90, 소비측 sfincs_continuity.f90 / sfincs_momentum.f90). subgrid 방법론은 v2.0.0 Alpe d'Huez(2022-11-16)에서 추가 (`developments.rst §v2.0.0 Alpe d'Huez release`), v2.2.0 col d'Eze 에서 van Ormondt et al. (2025) 논문과 일관되게 정비 (`developments.rst §col d'Eze release`), v2.1.1 Dollerup 에서 wet fraction 포함 신 방법론 도입 (`developments.rst §v2.1.1 Dollerup release`).

### 3.3 안정조건 (stability) — changelog 가 명시한 키워드·기본값

`numerical_implementation.rst §Stability conditions` 는 비어 있으나, `developments.rst §col d'Eze release` 의 "Detailed overview additions/changes" 에 **안정성 키워드·기본값이 verbatim 으로** 존재한다 (검증됨):

| 키워드 | 기본값 | 설명 (문서 verbatim 요약) |
|---|---|---|
| `stopdepth` | — (**REMOVED** v2.2.0) | 구 안정성 기준. `uvmax` 로 대체 — 수심이 아닌 **유속** 기반으로 불안정 판정 |
| `uvmax` | `1000` m/s | 최대 flux 유속. 이 값으로 최소 timestep 결정, 미만이면 unstable 로 분류·정지. `stopdepth` 대체 |
| `hmin_cfl` | — | CFL 조건으로 최대 timestep 결정 시 사용하는 **최소 수심** |
| `uvlim` | `10` m/s | flux 유속 limiter |
| `slopelim` | `9999.9` (= off) | `dzdx` slope limiter (기본 꺼짐) |
| `advlim` | `1.0` (on) | advection limiter, 신 기본값에서 기본 켜짐 |
| `coriolis` | projected 계는 `latitude≠0` 일 때만 on (`latitude=0.0` 기본=off); spherical 대규모는 기본 on | 운동량 방정식 coriolis 항 사용 여부 |

출처: `developments.rst §col d'Eze release` (Detailed overview additions/changes: stopdepth/uvmax/hmin_cfl/uvlim/slopelim/advlim/coriolis).

추가 안정성 기본값 (`developments.rst §v2.1.1 Dollerup release` Added functionality):
- `advection_scheme = upw1` → **신 기본값** (구 구현은 `original`).
- `friction2d = true` → 마찰항 2D 성분 포함, **신 기본값**.
- 신 권장 조합: **`alpha=0.50, theta=1.0, advection=1`(항상 2D), `viscosity=1`**.

`viscosity` 관련 (`developments.rst §v2.0.2 Blockhaus release`):
- `viscosity = 1` 로 `theta=1.0` 운용 가능; `nuvisc` 는 격자 해상도 기반 자동결정(로그 출력), `nuvisc=value` 직접지정 또는 `nuviscdim=2` 로 배수 가능.

`timestep_analysis` (`developments.rst §v2.4.0 Galibier release`):
- `timestep_analysis = 1` → `average_required_timestep`·`percentage_limiting_timestep` 를 `sfincs_map.nc`/화면에 기록해 **global timestep 을 제약하는 셀** 분석.
- `huvmin` → 유속 계산용 최소 수심: $uv = q / \max(hu,\ huvmin)$ (output·advection 에 사용).

> **코드 대응**: CFL/uvmax 기반 timestep 결정·timestep_analysis 출력은 [[../source-analysis/sfincs_flow_solver]] (sfincs_lib.f90 시간루프, sfincs_timestep_analysis.f90).

### 3.4 Quadtree (적응 격자) — 문서 단서

`numerical_implementation.rst §Numerical grid` 는 비어 있다. quadtree 에 대한 **문서 본문 서술은 RST 3파일에 없음** (changelog 에 `dyrinvc`·`quadtree netcdf output` 버그/기능 언급만: `developments.rst §mt. Faber release` bugfix "quadtree variable dyrinvc", `§Galibier release` "Quadtree netcdf output sfincs_map.nc ... QGIS"). quadtree 자료구조·refine 규칙의 실체는 [[../source-analysis/sfincs_subgrid_quadtree]] (sfincs_quadtree.F90) 로만 검증 가능 — 본 manual-notes 에서 quadtree 메커닉을 단언하지 않는다(날조 금지).

### 3.5 비정수압(nonhydrostatic) — alpha 기능

`developments.rst §col d'Eze release` (Advanced user options, alpha/beta):
- Nonhydrostatic pressure correction (tsunami wave 모델링용), 키워드 `nonh = yes` (기본 `no`), 부수 키워드 `nh_tstop`, `nh_fnudge`, `nh_tol`, `nh_itermax`. `nonh_mask` 로 도메인 일부만 적용 가능.

> **코드 대응**: [[../source-analysis/sfincs_nonhydrostatic_wavemaker]].

---

## 4. 시간 적분 요약 (문서 근거 한정)

문서가 명시적으로 단언하는 시간적분 속성:
1. **first order explicit** (`overview.rst §What is SFINCS?`).
2. Bates et al. (2010) 기반 (동).
3. timestep 은 CFL/`uvmax`/`hmin_cfl` 로 제약 (`developments.rst §col d'Eze release`).
4. 부피 갱신을 subgrid table 로 우회해 거친 격자에서 가속 (`developments.rst §subgrid mode`).

staggered grid, momentum→continuity 순서의 1 step 알고리즘 레벨 상세는 RST 본문에 없으므로 [[../source-analysis/sfincs_flow_solver]] (self canonical) 에서만 단언.

---

## 5. 개발/릴리스 맥락 (`developments.rst`)

| 릴리스 | 코드/날짜 | 수치 관련 핵심 |
|---|---|---|
| v2.4.0 Galibier | 2026.01 | timestep_analysis, huvmin, snapwave wave force factor |
| v2.3.0 mt. Faber | 2025.02 | 파일 존재 체크, volfile, Neumann/하류 riverine BC(alpha) |
| v2.2.0 col d'Eze | 2025.01 | **안정성 대개편**(uvmax/hmin_cfl/uvlim/slopelim/advlim, stopdepth 제거), subgrid 정비(van Ormondt 2025), nonh(alpha) |
| v2.1.1 Dollerup | 2024.01 | `advection_scheme=upw1` 기본, `friction2d=true` 기본, wet-fraction subgrid |
| v2.0.0 Alpe d'Huez | 2022-11-16 | **subgrid mode + 첫 GPU(openacc)** 오픈소스화 |
| v1 (pre-release) | subversion | regular mode 전 기능 (예: trunk revision 141, Leijnse et al. 2021) |

출처: `developments.rst §Releases Changelog` 하위 각 release section.

### 5.1 알려진 이슈 (수치 관련, `developments.rst §Known issues`)
- v2.3.0 mt Faber: Curve Number infiltration + `storecumprcp=0`(기본) → 침투 비정상 처리 가능 → 임시해법 `storecumprcp=1`. **v2.4.0 Galibier 에서 수정**.
- 2023 Cauberg 이전 restartfile 은 재생성 권장 (flux 읽기 mismatch).

출처: `developments.rst §Known issues`, `§col d'Eze release` bugfixes, `§mt. Faber release` bugfixes.

---

## 6. 이론↔코드 cross-link 요약

| 문서 개념 | RST 출처 | source-analysis (코드) |
|---|---|---|
| reduced SWE, explicit, LIE/SSWE | `overview.rst §What is SFINCS?` | [[../source-analysis/sfincs_flow_solver]] |
| subgrid look-up table | `developments.rst §subgrid mode` | [[../source-analysis/sfincs_subgrid_quadtree]] |
| 안정조건(uvmax/CFL/limiter) | `developments.rst §col d'Eze release` | [[../source-analysis/sfincs_flow_solver]] |
| nonhydrostatic / wavemaker | `developments.rst §col d'Eze release` | [[../source-analysis/sfincs_nonhydrostatic_wavemaker]] |
| swash/wave setup (WIP 문서) | `numerical_implementation.rst §Swash zone modelling approach` (skeleton) | [[../source-analysis/sfincs_snapwave]] |
| forcing(fluvial/pluvial/tidal/wind/wave) | `overview.rst §Compound flooding?` | [[../source-analysis/sfincs_boundaries_forcing]] |
| 전체 모듈 맵 | — | [[../source-analysis/sfincs-architecture-source-map]] |

---

## 7. 검증 메모

- 인용한 모든 section heading 은 RST 3파일 직접 Read 로 확인 (heading 명 verbatim).
- `numerical_implementation.rst` 의 **본문 부재(skeleton)** 는 반복 가능한 객관 관찰 → 문서가 채워지면 §3.1·§3.3·§3.4 보강 대상.
- 수치 메커닉 식·이산화는 RST 본문에 없어 단언하지 않음(`source-needed` 가 아니라 **문서 자체에 없음**); 식 레벨은 source-analysis(self) 와 Leijnse et al. (2021)·van Ormondt et al. (2025) 원논문이 canonical.

## 8. readthedocs 라이브 사이트

본 노트의 RST 소스(`raw/source_code/sfincs/docs/*.rst`)는 **공식 readthedocs 사이트를 빌드하는 동일 소스**다. 라이브 매핑 `docs/<name>.rst` → `https://sfincs.readthedocs.io/en/latest/<name>.html`:

- overview → <https://sfincs.readthedocs.io/en/latest/overview.html> — ✅ **2026-06-18 직접 fetch 대조**: "momentum and continuity equations ... first order explicit scheme based on Bates et al. (2010)" verbatim 일치, SFINCS-LIE(advection 무시, sub-critical)/SSWE(advection 포함, super-critical·wave) 구분·compound flooding 5요소(fluvial·pluvial·tidal·wind·wave) 확인.
- numerical_implementation → <https://sfincs.readthedocs.io/en/latest/numerical_implementation.html> — 라이브도 식 본문 skeleton 동일.
- developments → <https://sfincs.readthedocs.io/en/latest/developments.html>

→ 로컬 RST(버전 고정·재현)를 1차, readthedocs URL을 라이브 참조로 병기. 둘은 동일 repo docs/ 빌드라 동치.
