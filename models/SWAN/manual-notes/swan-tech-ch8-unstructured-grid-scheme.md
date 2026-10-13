---
title: "SWAN swantech Ch 8.1-8.3 Unstructured grid description + numerical method (vertex-based BSBT/N-scheme + crest sweeping) verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) Ch 8 §8.1 Description of an unstructured grid + §8.2 grid generation + §8.3 Numerical method, doc p.135-142 (Eq 8.1-8.16). References: Zijlema 2009·2010, Shewchuk 1996 (Triangle), Struijs 1994 (N-scheme)."
citation_status: verified
verification_method: "swantech.pdf (v41.51) Ch 8 §8.1-8.3 직접 read via pdftotext (식 번호 context-verified: Euler relation 8.1-8.3·angle 8.4·F lumping 8.5·implicit Euler 8.6·base vectors 8.7-8.10·propagation expand 8.11-8.14·base vec 8.15·vertex update 8.16) + website_markdown node84-92.md LaTeX alt-text. Ch 8은 chapter-local 번호 → website=PDF 일치(offset 0).; 2026-10-13 recovery 대조 보고서 R1–R8 반영"
last_source_check: "2026-10-13 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 8.1-8.16 + C≈2V/φ>143°/3-sweep 120° verbatim, PDF 식 번호 context-검증"
verification_date: 2026-06-02
related:
  - models/SWAN/source-analysis/swan-unstructured-time-step.md
  - models/SWAN/source-analysis/swan-grid-readers.md
  - models/SWAN/manual-notes/swan-tech-ch3-discretization.md
  - models/SWAN/manual-notes/swan-tech-ch8-unstructured-ops.md
---

# swantech Ch 8.1-8.3 Unstructured grid + numerical method — verified verbatim

> swantech.pdf (v41.51) Ch 8 §8.1-8.3 직접 read. **비구조(삼각) 격자 SWAN** — nested 대안, 국소 refinement. Grid 정의/조건 + **vertex-based BSBT 이산화** + crest-ordering sweeping. 소스 구현 [swan-unstructured-time-step](../source-analysis/swan-unstructured-time-step.md) (SwanCompUnstruc) + [swan-grid-readers](../source-analysis/swan-grid-readers.md). Zijlema(2009·2010). BSBT와 N-scheme의 일치는 사각형의 대각선을 파랑 특성선과 최대한 나란하게 삼각분할한 정규 격자에 한정된다. 근거: swantech PDF 149쪽 / 인쇄 141쪽; R1:TN-201. [10-13 전수 검증 정정]
>
> **식 번호 주의**: Ch 8은 chapter-local → **website = PDF 일치 (offset 0)**.

## 0. 도입

심해→천해 wind wave 의 다양한 공간스케일 → **flexible grid** 로 국소 refinement (estuary/fjord 강한 bathymetry 변화). Nested 대안(복잡 프로그래밍·계산비 ↑ 회피). 비구조 격자: 국소 refinement(adaptive/fixed) + coastline/island 유연 생성. 점당 CPU 비용은 높으나 격자점 수 감소로 상쇄. **구조격자 four-direction Gauss-Seidel + 완전 implicit 시간(§3.3)을 비구조에 적용 → 임의 time step 안정.**

## 1. §8.1.1 Definitions

- **structured**: quadrilateral (rectilinear/curvilinear), 내부 vertex 당 항상 **4 cell**
- **unstructured**: 제약 해제. 보통 삼각형 또는 삼각+사각(hybrid). **SWAN 은 삼각형(cell)만** — 변 = **face**

## 2. §8.1.2 Cell/vertex/face 관계 (Eq 8.1-8.3)

삼각 mesh: cell $C$, boundary face $E_b$, internal face $E_i$:
$$E_b + 2E_i = 3C \quad \text{(8.1)}$$
총 face $E = E_i + E_b$. Vertex $V$, hole(island) $H$ → **Euler 관계**:
$$C + V - E = 1 - H \quad \text{(8.2)}$$
$E_b \ll E_i$, $H$ 무시 시:
$$C \approx 2V,\quad E \approx 3V \quad \text{(8.3)}$$
> **cell 이 vertex 의 약 2배** → action 을 **vertex 에 저장**이 unknown 최소(주어진 격자서) → 물리과정(생성·소산·재분배) 평가 계산시간 대폭 절약.

## 3. §8.1.3 Grid 조건 (Eq 8.4)

badly-shaped 회피:
- **내부 vertex 당 cell 수: 최소 4, 최대 10**
- 삼각형 내각 제한 (face tangent $\vec{a},\vec{b}$):
$$\cos\phi = \frac{\vec{a}\cdot\vec{b}}{|\vec{a}||\vec{b}|} \quad \text{(8.4)}$$
> 코드는 오류 수준 1로 보고한다. 각도 조건은 `if ( .not. cosphi1 > -0.8 .and. ITEST >= 100 ) then`이다. 이 조건은 등호를 포함하며 `ITEST >= 100`을 요구한다. (swantech PDF 144쪽 / 인쇄 136쪽; `src/SwanCheckGrid.ftn90:151`; R1:TN-190)

## 4. §8.2 Grid generation (서술)

coarse→fine refinement. 최적 격자 = bathymetry/wave 급변역 고해상도. **Triangle (Shewchuk 1996)** — free 2D Delaunay triangulator (Matlab/Python interface), acute 삼각형만. Refinement 기준:
- **$h$-refinement**: wavelength/grid size 비 크게 유지 (천수서 wavelength↓ → cell↓). $h$ = 수심
- **topographic length scale**: $\Delta h/h < 1$ ($\Delta h$ = 삼각형 max-min 수심차, $h$ = 평균). 큰 $\Delta h/h$ = steep bottom → 세분 필요
- **min area constraint** 병행 (너무 작은 삼각형 방지). 반복 refinement.

## 5. §8.3.1 Discretization procedure (Eq 8.5-8.16)

Eq 2.16 의 time-deriv + geographic propagation 외 전부를 $F(\vec{x},\sigma,\theta)$ 로 묶음:
$$\frac{\partial N}{\partial t} + \nabla_{\vec{x}}\cdot[\vec{c}_{\vec{x}}N] = F \quad \text{(8.5)}$$
($\vec{c}_{\vec{x}} = \vec{c}_g + \vec{u}$). 삼각 mesh (hybrid 도 가능). **Vertex-based**: action $N$ 을 vertex 에 저장, 각 vertex 서 (8.5) 풂 (boundary vertex 값 고정).

**1차 implicit Euler**:
$$\frac{N^n - N^{n-1}}{\Delta t} + \nabla_{\vec{x}}\cdot[\vec{c}_{\vec{x}}N^n] = F^n \quad \text{(8.6)}$$
> **CFL 무제약** (explicit spectral 모델과 달리), time step 은 정확도만 제한. 대형 계 → **point-by-point multi-directional Gauss-Seidel** (iteration 중 신규 vertex 값 활용, **locally implicit globally explicit** → 대형 행렬 불필요 + 임의 time step 안정).

### 5.1 Vector calculus (Eq 8.7-8.10)

Vertex 1서 local $\vec{\xi}=(\xi,\eta)$ → Cartesian $\vec{x}=(x,y)$ 매핑. 접선 base vector:
$$\vec{e}_{(1)} = \frac{\partial\vec{x}}{\partial\xi},\quad \vec{e}_{(2)} = \frac{\partial\vec{x}}{\partial\eta} \quad \text{(8.7)}$$
법선 (등ξ/η면):
$$\vec{e}^{(1)} = \text{grad}\,\xi,\quad \vec{e}^{(2)} = \text{grad}\,\eta \quad \text{(8.8)}$$
reciprocal: $\vec{e}_{(\alpha)}\cdot\vec{e}^{(\beta)} = \delta_\alpha^\beta$ **(8.9)**. Cramer:
$$\vec{e}^{(1)} = \frac{1}{D}(e^2_{(2)}, -e^1_{(2)})^\top,\ \vec{e}^{(2)} = \frac{1}{D}(\cdots, e^1_{(1)})^\top,\ D = e^2_{(2)}e^1_{(1)} - e^2_{(1)}e^1_{(2)} \quad \text{(8.10)}$$

### 5.2 Propagation 이산화 (Eq 8.11-8.16)

$$\nabla_{\vec{x}}\cdot[\vec{c}_{\vec{x}}N] = \frac{\partial c_x N}{\partial x} + \frac{\partial c_y N}{\partial y} \quad \text{(8.11)}$$
chain rule:
$$\nabla_{\vec{x}}\cdot[\vec{c}_{\vec{x}}N] = e^{(1)}_1\frac{\partial c_x N}{\partial\xi} + e^{(2)}_1\frac{\partial c_x N}{\partial\eta} + e^{(1)}_2\frac{\partial c_y N}{\partial\xi} + e^{(2)}_2\frac{\partial c_y N}{\partial\eta} \quad \text{(8.12)}$$
**1차 one-sided 차분** (vertex 1,2,3 의 $N_1,N_2,N_3$, $\Delta\xi=\Delta\eta=1$): $\frac{\partial c_x N}{\partial\xi} \approx \frac{c_x N_1 - c_x N_2}{\Delta\xi}$ 등 **(8.13)** → (8.12) 대입:
$$\nabla_{\vec{x}}\cdot[\vec{c}_{\vec{x}}N] \approx c_x N|_2^1 e^{(1)}_1 + c_x N|_3^1 e^{(2)}_1 + c_y N|_2^1 e^{(1)}_2 + c_y N|_3^1 e^{(2)}_2 \quad \text{(8.14)}$$
base vector: $\vec{e}_{(1)} = \vec{x}_1 - \vec{x}_2$, $\vec{e}_{(2)} = \vec{x}_1 - \vec{x}_3$ **(8.15)**.

> 최저차 정확·**action 보존**(§8.7). **BSBT upwind 3 이유**: ① compact (1 삼각형만) ② characteristic 따라 전파 강제 (multidimensional·최소 cross-diffusion) ③ monotone ($N>0$ 보장). **정삼각 격자(대각선이 characteristic 정렬)서 N(arrow) scheme(fluctuation splitting)과 동일** (Struijs 1994 pp.63-64) — multidimensional·1차·monotone·conservative·narrow stencil·characteristic 일치(§3.2.1) 공유(완전 동일은 아님).

Vertex 1 갱신 (삼각형 △123, $N_2^n, N_3^n$ 주어짐):
$$\left[\frac{1}{\Delta t} + c_{x,1}(e^{(1)}_1 + e^{(2)}_1) + c_{y,1}(e^{(1)}_2 + e^{(2)}_2)\right]N_1^n = \frac{N_1^{n-1}}{\Delta t} + (c_{x,2}e^{(1)}_1 + c_{y,2}e^{(1)}_2)N_2^n + (c_{x,3}e^{(2)}_1 + c_{y,3}e^{(2)}_2)N_3^n + F^n \quad \text{(8.16)}$$
> Face $\vec{e}_{(1)},\vec{e}_{(2)}$ 사이 방향($\theta_1$~$\theta_2$ shaded sector) = (8.16)의 **domain of dependence**. Characteristic 가 이 sector 내 → **CFL 안정 무관**(causality). $F^n$ 은 sector 내 implicit 이산화 (spectral 근사·source 선형화 §3.3). 모든 둘러싼 cell 처리 시 vertex 1 갱신 완료. Refraction·nonlinear 로 sector 간 shift → 반복 수렴.

## 6. §8.3.2 Sweeping algorithm

각 vertex 는 다음 진행 전 geographic 갱신 필요 (upwave vertex 2,3 갱신 후만 → causality). 구조격자는 four-sweep natural ordering. **비구조는 distinct direction 없음** → vertex 를 번호순(랜덤) 정렬하면 최신해 미활용.

문서는 “All the vertices are ordered according to their distances to the origin of the grid in ascending order.”라고 적는다. (swantech PDF 150쪽 / 인쇄 142쪽; R8:T1-014)

기본 patch B 빌드는 거리 정렬 결과에서 의존성 수준을 만든 flist를 순회한다. 거리값은 꼭짓점 좌표의 sweep 방향 투영이다. -fixfront 빌드는 vlist를 순회한다. 이 분기는 0dabfa4(2026-07-13)에서 추가되었다. (`src/SwanVertlist.ftn90:185` `dist(j,swpdir) = vert(j)%attr(VERTX) * cos(sdir) + vert(j)%attr(VERTY) * sin(sdir)`; `src/SwanCompUnstruc.ftn90:848–849` `!GRAPH                ivert = flist(kvert,swpdir)`; `!FXFRO                ivert = vlist(kvert,swpdir)`; [git A 판정](../../../_staging/recovery/compare/SWAN-git-verify-A.md); R8:T1-014)

**M sweep** (4 불필요), 각 sweep = $2\pi/M$ 방향범위. 예: **3 sweep × 120°** (1st = dominant, 2nd = +120°, 3rd = -120°) → 3 vertex ordering → 타 방향 전파도 커버. sweep ↑ → 방향간격 ↓ → iteration ↓ (단 계산량 ↑). **3 sweep 이 좋은 절충**.

미지정 sweep 수는 3을 시작값으로 하여 물리 옵션별로 4 또는 3으로 바꾼다. 부분 방향 격자의 1 sweep 입력은 3으로 바꾼다. (`src/swanmain.ftn:3762–3770` `nsweep = 3`; `IF ( IREFR == 0 ) nsweep = 4`; `IF ( IQUAD == 0 .AND. IWCAP == 0 .AND. ISURF == 0 ) nsweep = 4`; `IF ( OFFSRC ) nsweep = 4`; `IF ( IGEN == 4 .OR. IQCM /= 0 ) nsweep = 3`; R1:TN-203)

비정렬 격자는 첫 세 반복에서 nsweep을 쓴다. 네 번째 이후 반복은 전 방향 스펙트럼이면 한 sweep을 쓴다. 제한된 방향 구간이면 nsweep을 유지한다. (`src/SwanCompUnstruc.ftn90:124` `itswp = 4`; `src/SwanCompUnstruc.ftn90:825–831` `if ( iter < itswp ) then`; `n = nsweep`; `elseif ( .not.FULCIR ) then`; `n = nsweep`; `else`; `n = 1`; R8:T1-009)

## 7. SWAN 옵션 매핑

| Tech (PDF §8) | User cmd | 비고 |
|---|---|---|
| §8.1 grid | `CGRID UNSTRUCTURED` + `READGRID UNSTRUCTURED ADCIRC/TRIANGLE/EASYMESH` | [swan-grid-readers](../source-analysis/swan-grid-readers.md) |
| §8.3 vertex BSBT | (internal, 임의 time step) | N-scheme 유사 |
| §8.3.2 sweeps | `SET`의 `[nsweep]` | 미지정 값은 물리 옵션에 따라 3 또는 4이다. (R1:TN-203) |

## 8. 한계

- 식 (8.16)은 SwanTranspX의 기초식과 일치한다. (swantech PDF 149쪽 / 인쇄 141쪽; `src/SwanTranspX.ftn90:128–150`; R8 §6의 유지 행)
- §8.4-8.7 (interpolation·force·diffusion·action conservation, Eq 8.17-8.45) → [swan-tech-ch8-unstructured-ops](swan-tech-ch8-unstructured-ops.md) (다음).
- 소스 구현(vertex loop·sweep·contributor) 상세는 [swan-unstructured-time-step](../source-analysis/swan-unstructured-time-step.md) (SwanCompUnstruc.ftn90).

## 9. 연결

- [swan-unstructured-time-step](../source-analysis/swan-unstructured-time-step.md) — SwanCompUnstruc.ftn90 (vertex sweep 구현, Casey Dietrich 41.20)
- [swan-grid-readers](../source-analysis/swan-grid-readers.md) — ADCIRC/Triangle/Easymesh reader
- [swan-tech-ch3-discretization](swan-tech-ch3-discretization.md) — §3.2 구조격자 BSBT (semi-Lagrangian 공유)
- [swan-tech-ch3-solution-iteration-limiter](swan-tech-ch3-solution-iteration-limiter.md) — §3.3 four-sweep + source 선형화 (8.16 의 F^n)
- [swan-tech-ch8-unstructured-ops](swan-tech-ch8-unstructured-ops.md) — §8.4-8.7 (interpolation·force·diffusion·action conservation)

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

확정 결론과 원문 인용: [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론), [R8](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론), [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R1:TN-186 | 문서 식 (8.1) | swantech PDF 144쪽 / 인쇄 136쪽, (8.1): $E_b+2E_i=3C$; $E=E_i+E_b$. | — | H 코드 대조 대상 아님 | 평면 삼각 격자의 면 수 항등식이다. 매 시간 계산하는 파랑 식이 아니다. |
| R1:TN-187 | 문서 식 (8.2) | swantech PDF 144쪽 / 인쇄 136쪽, (8.2): $C+V-E=1-H$. | `src/SwanParallel.ftn90:327` `nv = nvertsg` | H 코드 대조 대상 아님 | 연결된 평면 영역의 Euler 관계이다. 이를 사용해 셀 수를 정하는 구현이라고 말하지 않는다. |
| R1:TN-188 | 문서 식 (8.3) | swantech PDF 144쪽 / 인쇄 136쪽, (8.3): $C\approx2V,\ E\approx3V$ if $E_b\ll E_i$ and $H$ negligibly small. | — | H 코드 대조 대상 아님 | 절점 기반 미지수 선택의 계산량 설명이다. 유한 경계가 있는 모든 격자의 정확한 수량이 아니다. |
| R1:TN-190 | 삼각 격자 검사 수준 | swantech PDF 144쪽 / 인쇄 136쪽: 내부 절점의 셀 수는 4–10; $\cos\phi<-0.8$ 또는 $\phi>143^\circ$를 “do not allow”.<br>웹 [CGRID UNSTRUCTURED](../raw/manuals/website/online_doc/swanuse/node25.html):702–708. | `src/SwanCheckGrid.ftn90:106` `if ( noc > 0 .and. noc < 4 .and. vmark(i) == 0 ) then`; `src/SwanCheckGrid.ftn90:111` `if ( noc > 10 ) then`; `src/SwanCheckGrid.ftn90:118` `if ( badvertex ) call msgerr (1, 'number of cells around vertex is smaller than 4 or larger than 10')`; `src/SwanCheckGrid.ftn90:151` `if ( .not. cosphi1 > -0.8 .and. ITEST >= 100 ) then` | C 문서 누락 | 격자 검사와 오류 메시지 출력 자체는 swanuse에도 있다. C는 swantech §8.1의 `do not allow`에 실제 보고 수준과 시험 출력 조건이 없는 점이다. 코드는 오류 수준 1로 보고한다. 각도 조건은 `if ( .not. cosphi1 > -0.8 .and. ITEST >= 100 ) then`이다. 이 조건은 등호를 포함하며 `ITEST >= 100`을 요구한다. [10-13 전수 검증 보완]
| R1:TN-191 | 외부 격자 생성 권고 | swantech PDF 145쪽 / 인쇄 137쪽, §8.2: $\Delta h/h<1$; $h$는 셀 평균 수심이다. 예각 삼각분할·파장별 세분화·최소 면적 권고. | — | H 코드 대조 대상 아님 | 외부 격자 생성 절차와 권고이다. SWAN의 자동 적응 격자 재생성식으로 제시되지 않았다. |
| R1:TN-194 | 문서 식 (8.7)·(8.8)·(8.9) | swantech PDF 147쪽 / 인쇄 139쪽, (8.7): $\vec e_{(1)}=\partial_\xi\vec x,\ \vec e_{(2)}=\partial_\eta\vec x$; (8.8): $\vec e^{(1)}=\nabla\xi,\ \vec e^{(2)}=\nabla\eta$; (8.9): $\vec e_{(\alpha)}\cdot\vec e^{(\beta)}=\delta_\alpha^\beta,\ \alpha,\beta=\{1,2\}$. | — | H 코드 대조 대상 아님 | 국소 좌표 기저의 정의와 역행렬 관계이다. 구현 계수는 다음 행에서 대조한다. |
| R1:TN-201 | BSBT 성질 주장 | swantech PDF 149쪽 / 인쇄 141쪽: $N>0$; N(arrow) 기법과의 조건부 관계; 무조건 안정성과 적은 교차 확산. | — | H 코드 대조 대상 아님 | 수송 기법의 성질과 제한된 격자에서의 비교이다. 스펙트럼 중심차분·원천항·QC까지 포함한 전체 해의 양수성 보증이 아니다. |
| R1:TN-203 | 미지정 비정렬 sweep 수 | swantech PDF 150쪽 / 인쇄 142쪽: “three sweeps is a good compromise”.<br>swanuse PDF 135 및 웹 [SET 명령 도식](../raw/manuals/website/online_doc/swanuse/node49.html):62–65. | `src/swanmain.ftn:3762–3770` `nsweep = 3`; `IF ( IREFR == 0 ) nsweep = 4`; `IF ( IQUAD == 0 .AND. IWCAP == 0 .AND. ISURF == 0 ) nsweep = 4`; `IF ( OFFSRC ) nsweep = 4`; `IF ( IGEN == 4 .OR. IQCM /= 0 ) nsweep = 3` | C 문서 누락 | swanuse의 SET 명령 도식에 `[nsweep]`가 있다. C는 swantech §8.3의 3 sweep 권고에 물리 옵션별 미지정 값 선택이 없는 점이다. 미지정 값은 물리 옵션에 따라 3 또는 4이다. 부분 방향 격자의 1 sweep 입력은 3으로 바꾼다. |
| R1:TN-204 | GRAPH/FIXFRONT 목록 | swantech PDF 151쪽 / 인쇄 143쪽: 정렬된 절점 목록을 차례로 진행한다. | `src/SwanVertlist.ftn90:243–244` `!GRAPH       ! construct levels from a directed dependency graph`; `!GRAPH       ! note: each level contains vertices that are independent by construction`<br>`src/SwanCompUnstruc.ftn90:839–849` `!GRAPH`; `!FXFRO` | C 문서 누락 | 기본 GRAPH는 의존 그래프로 독립 절점 수준을 만든다. `-fixfront`는 고정 front 목록을 선택한다. 문서는 이 두 실행 목록을 설명하지 않는다. |
| R1:TC-016 | 비정렬 흐름 sweep의 최소 bin 수 | swanuse PDF 24쪽 / 인쇄 16쪽 및 웹 [격자 선택](../raw/manuals/website/online_doc/swanuse/node11.html):345–348. | `src/SwanSweepSel.ftn90:277–280,315,317` `if ( idtot < 3 ) then`; `iddtop = iddtop + 1`; `if ( idtot == 1 ) iddlow = iddlow - 1`; `idtot = 3`; `isslow = 1`; `if ( ICUR > 0 ) isstop = max(min(4,MSC),isstop)` | C 문서 누락 | C는 swantech §8.3에 흐름이 있는 sweep의 최소 bin 확장 절차가 없는 점이다. 방향 구간은 최소 3 bin이며 주파수 구간은 저주파부터 최소 `min(4,MSC)`까지 포함한다. swanuse의 방향 사분면당 최소 3 bin 요건 및 전체 주파수 최소 4개 권고와 각 sweep 내부의 강제 확장을 구분한다. |
| R8:T1-009 | 비정렬 반복별 sweep 수 감소 | swantech PDF 150쪽·인쇄 142쪽: “a fixed number of sweeps (not necessarily 4) is introduced”. PDF 151쪽·인쇄 143쪽: “In each iteration, a number of sweeps through the vertices is executed”. swanuse PDF 135쪽·인쇄 127쪽과 `website/online_doc/swanuse/node49.html:65`에는 `[nsweep]` 구문이 있다. `website/modifications/modifications.htm:1346–1347`은 “only a few sweeps per iteration or time step is needed”라고 적는다. | `src/SwanCompUnstruc.ftn90:124` `itswp = 4`<br>`src/SwanCompUnstruc.ftn90:825–831` `if ( iter < itswp ) then`; `n = nsweep`; `elseif ( .not.FULCIR ) then`; `n = nsweep`; `n = 1` | C — 감소 조건 누락 | 비정렬 격자는 첫 세 반복에서 nsweep을 쓴다. 네 번째 이후 반복은 전 방향 스펙트럼이면 한 sweep을 쓴다. 제한된 방향 구간이면 nsweep을 유지한다. C는 이 반복 번호·FULCIR에 따른 감소 조건의 설명 누락에 한정한다. nsweep의 존재나 일반적인 sweep 최적화가 문서 전체에 없다는 뜻은 아니다. |
| R8:T1-012 | sweep 수·DIA 비용의 성능 설명 | swantech PDF 150쪽·인쇄 142쪽: “three sweeps is a good compromise”. PDF 96쪽·인쇄 88쪽은 인접 두 사분면의 약 33° 구간을 추가 계산하는 DIA 방법의 계산시간을 “a factor of about 1.66”으로 설명한다. | `src/swanmain.ftn:3757–3768` `IF ( nsweep.EQ.-999 ) THEN`; `nsweep = 3` | H | 세 sweep은 반복 수 감소와 계산 시간 증가 사이의 문서상 경험적 권고이다. 약 1.66배는 해당 DIA 방법의 계산 비용에 관한 문서 설명이다. 두 문장을 모든 설정의 고정 sweep 수나 실행 시간 보장으로 바꾸지 않는다. |
| R8:T1-014 | 비정렬 기본 wavefront 정렬 | swantech PDF 150쪽 / 인쇄 142쪽: “All the vertices are ordered according to their distances to the origin of the grid in ascending order.” | `src/SwanVertlist.ftn90:185` `dist(j,swpdir) = vert(j)%attr(VERTX) * cos(sdir) + vert(j)%attr(VERTY) * sin(sdir)`<br>`src/SwanVertlist.ftn90:243` `!GRAPH       ! construct levels from a directed dependency graph`<br>`src/SwanVertlist.ftn90:371` `!GRAPH          flist(l,swpdir) = k`<br>`src/SwanCompUnstruc.ftn90:848` `!GRAPH                ivert = flist(kvert,swpdir)`<br>`src/SwanCompUnstruc.ftn90:849` `!FXFRO                ivert = vlist(kvert,swpdir)`<br>`switch.pl:87–88` `if ($ffro=~/TRUE/) {$newline=~s/^!FXFRO//;}`; `else               {$newline=~s/^!GRAPH//;}`<br>`7ee8981:src/SwanCompUnstruc.ftn90:851` `             ivert = vlist(kvert,swpdir)`<br>`7ee8981:src/SwanCompUnstruc.ftn90:852` `             !$ ivert = tlist(kvert)` | A — patch B 판 차이 | 기본 patch B 빌드는 거리 정렬 결과에서 의존성 수준을 만든 flist를 순회한다. 거리값은 꼭짓점 좌표의 sweep 방향 투영이다. -fixfront 빌드는 vlist를 순회한다. 이 분기는 0dabfa4(2026-07-13)에서 추가되었다. |
| R7:H-534 | 비구조 1 sweep | `website/modifications/modifications.htm:534` `Efficiency UnSWAN solution algorithm improved by taking 1 sweep per iteration instead of undetermined number of sweeps.` | `src/swanmain.ftn:3762` `nsweep = 3                                                       41.68`<br>`122b595:src/SwanCompUnstruc.ftn90:120` `integer, parameter                    :: itswp = 4 ! the number of iterations needed prior to switch to a lower number of sweeps`<br>`122b595:src/SwanCompUnstruc.ftn90:808` `if ( iter < itswp ) then`<br>`122b595:src/SwanCompUnstruc.ftn90:810` `elseif ( .not.FULCIR ) then`<br>`122b595:src/SwanCompUnstruc.ftn90:813` `n = 1`<br>`src/SwanCompUnstruc.ftn90:124` `integer, parameter                    :: itswp = 4 ! the number of iterations needed prior to switch to a lower number of sweeps`<br>`src/SwanCompUnstruc.ftn90:825–831` `if ( iter < itswp ) then`; `n = nsweep`; `elseif ( .not.FULCIR ) then`; `n = nsweep`; `n = 1` | H 현재 반영된 이력 기록 | 41.10의 1 sweep 경로는 현재도 남아 있다. 현재 전 방향 계산은 네 번째 반복부터 1 sweep을 사용한다. 초기 반복과 제한된 방향 구간은 nsweep을 사용한다. nsweep=3만으로 1 sweep 이력이 폐기되었다고 판단하지 않는다. |
| R7:H-1346 | 비구조 적은 sweep의 효율 | `website/modifications/modifications.htm:1346–1347` `Unstructured mesh computation is made more efficient, i.e. only a few sweeps per iteration or time step is needed.` | — | H 코드 대조 대상 아님 | 반복당 sweep 수에 따른 효율 주장이다. 현행 nsweep의 상한 있는 루프는 R7:H-1357에서 판정한다. |
| R7:H-1358 | 경계 없는 격자의 가장 깊은 기준점 | `website/modifications/modifications.htm:1358–1359` `assign reference point to deepest point in case of no boundary condition in unstructured mesh cases,` | `src/SwanVertlist.ftn90:44` `!   41.68,   April 2018: removal of the wavefront approach (based on reference point)`; `122b595 2023-02-28 initial release (v 41.45)`<br>`122b595:src/SwanVertlist.ftn90:43` `!   41.68,  April 2018: removal of the wavefront approach (based on reference point)`<br>`122b595:src/SwanVertlist.ftn90:146` `          dist(j,swpdir) = vert(j)%attr(VERTX) * cos(sdir) + vert(j)%attr(VERTY) * sin(sdir)`<br>`43e9bbb:src/SwanVertlist.ftn90:44` `!   41.68,   April 2018: removal of the wavefront approach (based on reference point)`<br>`43e9bbb:src/SwanVertlist.ftn90:185` `          dist(j,swpdir) = vert(j)%attr(VERTX) * cos(sdir) + vert(j)%attr(VERTY) * sin(sdir)` | D 현재 해당 구현 없음 | 가장 깊은 점을 기준점으로 삼는 구판 경로는 현재 코드에 없다. 41.45 비교 코드도 기준점 기반 wavefront 제거를 기록한다. 현재 거리값은 좌표의 sweep 방향 투영이다. 내부 변경 번호 41.68을 공개 배포판 번호로 쓰지 않는다. |
