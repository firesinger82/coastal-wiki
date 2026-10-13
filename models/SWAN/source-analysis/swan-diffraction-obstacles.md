---
title: "swan diffraction obstacles"
topic: general
canonical_source: self
citation_status: verified
last_source_check: "2026-10-13 (recovery 대조 반영)"
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-diffraction-obstacles.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시. 2026-10-13 recovery 대조 보고서 R1–R8 반영"
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

The phase-decoupled diffraction approximation (`DIFFRAC`) — eikonal-based formulation, the smoothing parameters `SMPAR/SMNUM`, where it modifies propagation velocities (not as a separate source term), the `OBSTACLE` polyline syntax, transmission (`TRANS`) vs reflection (`REFL`) options, specular vs scattered reflection (`RSPEC` vs `RDIFF`), how structured grids use orthogonal `CROSS(2,MCGRD)` link marking (no diagonal), how unstructured face-based `SwanFindObstacles` works, and the limitations (no phase-resolving). Use this when configuring breakwaters, harbor entrances, or coastal structures.

## Source basis

- `src/swanpre1.ftn:944–1286, 2106–2120` — `OBSTACLE`과 `DIFFRAC`의 명령 판독 구간이다. [10-13 전수 검증 보완]
- `src/SwanDiffPar.ftn90:44-204` — eikonal diffraction.
- `src/swancom5.ftn:1077–1086, 1606–1631, 2148–2188, 5527–5775, 5883–5893` — 전파속도 보정과 평활화의 코드 구간이다. [10-13 전수 검증 보완]
- `src/swanser.ftn:2420-3699` — structured obstacle marking, reflection.
- `src/SwanPrepComp.ftn90:90`, `src/SwanFindObstacles.ftn90:103–127`, `src/SwanCompUnstruc.ftn90:777–1077`, `src/SwanPropvelX.ftn90:94–98`, `src/SwanPropvelS.ftn90:270` — 비구조 격자의 장애물·회절 처리 근거다. [10-13 전수 검증 정정]
- `src/swanmain.ftn:6394–6457` — GEN4와 QC의 회절 비활성화 검사 구간이다. [10-13 전수 검증 보완]

## A. DIFFRAC activation / formulation

회절 명령의 구문은 `DIFFRac [idiffr] [smpar] [smnum] [cgmod]`다. 근거: `src/swanpre1.ftn:2110–2118`. [10-13 전수 검증 정정]

Defaults when keyword present (`:2114`):
- `IDIFFR=1`.
- `SMPAR=0`.
- `SMNUM=0`.
- `CGMOD=1`.

Disabled for GEN4/QC scattering (`src/swanmain.ftn:6394, 6454`).

Eikonal 근사식은 다음과 같다. 근거: `src/SwanDiffPar.ftn90:44–68`. [10-13 전수 검증 보완]
```
K = k · √(1 + δ)
delta = D.(pDH)/(k^2 pH)
p = cc_g
```

구조 격자는 `IF (TMP.LT.-1.) THEN`이면 `DIFPARAM(IND) = 0.`을 대입한다. 그 외에는 `DIFPARAM(IND) = SQRT(1.+TMP)`를 대입한다. 근거: `src/swancom5.ftn:5889–5892`. [10-13 전수 검증 정정]

회절 매개변수는 $\delta=\nabla\cdot(p\nabla H)/(k^2pH)$다. 여기서 $p=cc_g$다. $H$는 파고에 비례한다. 매뉴얼 (2.138)의 인쇄 분모에는 $k^2$가 빠졌다. 근거: `src/SwanDiffPar.ftn90:54–68` `p = cc_g` / `delta = D.(pDH)/(k^2 pH)`; `src/SwanDiffPar.ftn90:350` `denom = k(ivert)*cg(ivert)*hs(ivert)`.

$K/k=\sqrt{1+\delta}$를 사용한다. 코드는 $K$ 배열을 별도로 갱신하지 않고 전파속도에 이 비를 적용한다. `src/swancom5.ftn:1082–1083`은 지리 전파속도에 곱하고 1608–1610행은 방향 전파속도를 보정한다. 근거: `src/swancom5.ftn:5892` `DIFPARAM(IND) = SQRT(1.+TMP)`; `src/SwanDiffPar.ftn90:62` `! K = k (1+delta)^0.5`.

## B. Smoothing (SMPAR, SMNUM)

Structured grids smooth energy field before computing diffraction:
```
E(i,j) = (1−4α)·E(i,j) + α·(E(i−1,j)+E(i+1,j)+E(i,j−1)+E(i,j+1))
```
근거: `src/swancom5.ftn:5529–5530`. [10-13 전수 검증 정정]

- `SMNUM` controls iteration count: `DO ISM = 1, INT(PDIFFR(2))` (`:5683-5685`).
- `SMPAR` is `α`: `TMP = PDIFFR(1)` (`:5709`).

Smoothing avoids crossing land/obstacles by checking `CROSS` and depth before applying neighbor contributions (`:5710-5717`).

코드 생략값은 `SMPAR=0`, `SMNUM=0`이다. swantech PDF 65쪽 / 인쇄 57쪽은 $n=6$을 권고한다. 근거: `src/swanpre1.ftn:2116` `CALL INREAL ('SMPAR', PDIFFR(1), 'STA', 0.0)`; `src/swanpre1.ftn:2117` `CALL INREAL ('SMNUM', PDIFFR(2), 'STA', 0.)`.

## C. OBSTACLE: TRANS vs REFL

`OBSTACLE` 구문은 투과 선택과 선택적인 `REFLec`를 포함한다. 근거: `src/swanpre1.ftn:944–964`. [10-13 전수 검증 보완]

`LINE` 좌표는 옵션 뒤에 둔다. `RDIFF`의 지수는 필수 입력이다. 근거: `src/swanpre1.ftn:1163` `CALL INREAL ('POWN', POWN, 'REQ', 1.)`; `src/swanpre1.ftn:1256–1263`.

FREEBOARD의 첫 인수는 HGT다. 근거: `src/swanpre1.ftn:1214` `CALL INREAL ('HGT'   , HGT , 'REQ', 0.)`.

**`TRANS`**: reads coefficient in `[0,1]`, stored in `TRCOEF(1)` (`:1082-1089`). Default = 0 (full obstacle) (`:1111`).

**`REFL`**: enables reflection only with full-circle directions; reads `REFLC` (`:1147-1150`). Defaults to no reflection when absent (`:1203`).

입력 투과·반사계수의 백분율은 파고비라고 명시한다. 일정 계수이고 FREEBOARD 보정이 없는 경우 `TRANS 0.5`, `REFL 0.7`, `REFL 0.6`의 에너지비는 각각 0.25, 0.49, 0.36이다. 난반사의 방향별 분배와 전체 반사비를 구분한다. 근거: swanuse PDF 83–84쪽 / 인쇄 75–76쪽; `src/swanser.ftn:3114` `TRCF(1,1) = OBHKT * OBHKT`; `src/swanser.ftn:3318` `REFLCOEF = SQRTREF * SQRTREF`.

## D. Specular vs scattered reflection (RSPEC vs RDIFF)

- `RDIFF` sets `LREFDIFF=1`; reads integer nonneg `POWN` (`src/swanpre1.ftn:1161-1173`).
- `RSPEC` (default) is ignored; `LREFDIFF=0`.

In `REFLECT`:
- `LREFDIFF=0`이면 단일 방향 필터를 할당한다. 이때 `PRDIF(0) = 1.`이다. 근거: `src/swanser.ftn:3655–3658`. [10-13 전수 검증 정정]
- `LREFDIFF=1` → cosine-power scattering: `PRDIF(ID) = COS(ID*DDIR)^POWN`, normalized by `SUMRD` (`:3685-3699`).

Use `RDIFF` for rough breakwaters or natural shorelines where reflection is diffuse.

## E. Obstacle segment definition (LINE)

Obstacles are polylines: `LINE` reads repeated corner points into `XCRP/YCRP`, requires ≥ 2 points (`src/swanpre1.ftn:1251-1286`).

Structured obstacle detection marks **only two orthogonal grid links per point** in `CROSS(2, MCGRD)`:
- Link 1 = x-neighbor.
- Link 2 = y-neighbor.

(`src/swanser.ftn:2420-2512`).

**There is no diagonal-link representation in structured SWAN**. Obstacles are approximated as orthogonal grid-edge crossings.

반사 루틴의 주석은 계산 격자 셀당 교차점을 하나로 제한한다. 다음 줄은 장애물의 날카로운 모서리를 피하라고 권고한다. 근거: `src/swanser.ftn:3619–3620`. [10-13 전수 검증 정정]

## F. Quadtree / unstructured obstacles

**No quadtree-specific obstacle index** found.

Unstructured handling is face-based:
- `SwanPrepComp`는 `SwanFindObstacles`를 호출한다. 근거: `src/SwanPrepComp.ftn90:90` `call SwanFindObstacles ( cross )`. [10-13 전수 검증 정정]
- Loops over obstacle segments + non-boundary faces (`src/SwanFindObstacles.ftn90:103-127`).
- Marks `cross(iface) = j` when face and obstacle segment intersect.

During unstructured computation, crossed faces mapped to two local stencil links and passed to `SWTRCF` (`src/SwanCompUnstruc.ftn90:1036-1077`).

So unstructured obstacle handling is more flexible than structured (any face can be crossed; no orthogonality restriction).

## G. Where diffraction enters

**Diffraction is NOT a separate source term** — it modifies propagation velocities.

Structured grids:
- `SPROXY`는 `IF (IDIFFR.EQ.1 .AND. PDIFFR(3).NE.0.) THEN`에서 `CAX/CAY`에 `DIFPARAM`을 곱한다. 근거: `src/swancom5.ftn:1079–1083`. [10-13 전수 검증 정정]
- Directional propagation `CAD` adjusted using `DIFPARAM, DIFPARDX, DIFPARDY` (`:1606-1608`).

Velocities enter transport matrix via `STRSXY` — `CAX/CAY` form `FXY1/FXY2` added to `IMATDA/IMATRA` (`:2148-2188`).

Unstructured:
- Diffraction computed before transport.
- `SwanCompUnstruc`는 보정된 전파속도 `cax/cay/cad/cas`를 `SwanTranspAc`에 전달한다. 근거: `src/SwanCompUnstruc.ftn90:1080–1085`. [10-13 전수 검증 정정]

## H. Limitations

This is **phase-decoupled, not phase-resolving** (`src/swanmain.ftn:6395, 6455`).

회절 상태는 격자점별 `DIFPARAM`과 그 공간 미분으로 저장한다. 이 값은 위상 대신 작용밀도·에너지·파고에서 유도한다. 근거: `src/swmod2.ftn:1325–1331`; `src/SwanDiffPar.ftn90:174–208`. [10-13 전수 검증 보완]

For phase-resolving wave models (BoussInes/MILDSLP/full Navier-Stokes), use a different model (Boussinesq, BOUSS, FUNWAVE).

Disabled in:
- GEN4. `src/swanpre1.ftn:3093` `IDIFFR = 0`.
- QC scattering.

## Decision Guide

| Goal | Setup |
|---|---|
| Harbor with breakwaters | `OBSTACLE TRANS 0.0 REFL 0.6 RDIFF 4 LINE x1 y1 x2 y2` (파고 반사비 60%, 에너지 반사비 0.36) |
| Submerged reef partial transmission | `OBSTACLE TRANS 0.5 LINE ...` |
| Sharp breakwater specular reflection | `OBSTACLE REFL 0.8 RSPEC LINE ...` (default) |
| Diffraction near coastal structures | `DIFFRAC`의 코드 생략값은 `SMPAR=0`, `SMNUM=0`이다. |
| Phase-resolving short-wave detail | Don't use SWAN; use Boussinesq model |
| Shallow-water surf zone | `GEN4` (auto-disables DIFFRAC) |
| Storm with main interest in offshore | Skip DIFFRAC (default off); structures don't matter at coarse grid |

## Working Rules

- For most coastal applications, DIFFRAC is unnecessary — leave default off.
- 이 문장들은 적용·성능 권고다. 보편적 최적값이나 준비 시간의 근거는 적용 사례와 검증 문헌이다. 이 권고를 코드가 강제하는 규칙으로 쓰지 않는다. 근거: [R5 대조](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md), PN-186.
- Obstacle polylines: 2 points (line segment) is the simplest; many points trace curved structures.
- Avoid structures that exactly diagonal-cross grid cells — structured SWAN can only cross orthogonal links.


- Output `BLOCK ... DIFPARAM` to verify diffraction is active and not pathological.

## Common Pitfalls

- ▢ Setting `OBSTACLE LINE` without `TRANS` — defaults to fully blocking; if you wanted partial pass, set `TRANS=0.5`.
- ▢ `OBSTACLE` near boundary — interactions with BC; result undefined.
- 같은 계산 격자 셀의 여러 장애물 교차는 반사 루틴 주석의 사용 제한에 해당한다. 근거: `src/swanser.ftn:3619–3620`. swanuse PDF 83쪽 / 인쇄 75쪽은 같은 격자선의 여러 장애물 교차를 SWAN이 탐지하지 못한다고 설명한다. [10-13 전수 검증 정정]
- GEN4 명령 해석 단계의 회절 해제는 조용히 수행된다. 실행 전 검사까지 IDIFFR가 양수이면 GEN4 안내문이 나온다. QC와 회절이 함께 켜진 실행 전 검사에서는 경고가 나온다. 입력 순서와 검사 시점의 IDIFFR에 따라 출력 여부가 달라지므로 항상 무음 또는 항상 안내문이라고 쓰지 않는다. 근거: `src/swanpre1.ftn:3093` `IDIFFR = 0`; `src/swanmain.ftn:6394–6398`; `src/swanmain.ftn:6454–6457` `IF ( IQCM.NE.0 .AND. IDIFFR.GT.0 ) THEN`.
- ▢ Expecting full diffraction pattern (interference, side-lobes) — phase-decoupled doesn't reproduce these; only intensity-modulation.
- ▢ Setting `SMPAR > 0.25` — over-smoothing; physical features lost.
- ▢ Polyline with collinear points — degenerate; obstacle not detected.
- ▢ Unstructured with `OBSTACLE`: face crossings count, but if obstacle is along a vertex (no face crossing), not detected.

## Next expansion

- Comparison vs Boussinesq for harbor agitation problem.
- DIFFRAC `SMPAR/SMNUM` tuning recipe.
- Multiple-obstacle interaction validation case.

## References

- Holthuijsen et al. 2003 (phase-decoupled diffraction).
- SWAN User Manual (Obstacles and Diffraction).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/swan/source_code/swan/src`. Auto-draft = false; review_required = true.

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R3:CP-001 | 장애물 파고 하한과 폭 0 | — (문서 누락) | 장애물 파고 하한과 폭 0. `src/swanser.ftn:3070`의 파고 하한 `0.1E-4`; `src/swanser.ftn:3175` `IF (BVH.EQ.0.) THEN`; `src/swanser.ftn:3176` `OBHKT= -0.40*FVH`. 3177–3178은 0.075와 0.9로 제한한다. | C 문서 누락 | swantech PDF 62쪽 / 인쇄 54쪽, (2.132)의 음의 거듭제곱은 폭 0에서 정의되지 않는다. 코드가 별도 유한값을 택한다. |
| R3:CP-002 | 반사 방향 필터 | — (문서 누락) | 반사 방향 필터. `src/swanser.ftn:3691` `PRDIF(ID) = (COS(ID*DDIR))**POWN`; `src/swanser.ftn:3692` `IF (PRDIF(ID).GT.0.01) THEN`; `src/swanser.ftn:3693` `SUMRD = SUMRD + 2.*PRDIF(ID)`; `src/swanser.ftn:3700` `PRDIF(ID) = PRDIF(ID) / SUMRD`; `src/swanser.ftn:3740` `TH_INC = 2.*BETA - TH_OUT`. 3746–3751은 두 입사 방향 사이를 보간한다. | C 문서 누락 | swanuse PDF 84·OBSTACLE 절(node28:2617–2642)은 cos 거듭제곱 분포와 `Default: [pown] = 1.`을 이미 적는다. C는 swantech 2.5와 swanuse OBSTACLE 절에 없는 0.01 절단·이산 정규화·두 입사 방향 보간에 한정한다. `src/swanpre1.ftn:1163`은 `CALL INREAL ('POWN', POWN, 'REQ', 1.)`다. `src/ocpcre.ftn:656,668,676`은 값 생략 시 오류 수준 3을 보고한 뒤 1을 대입한다. 따라서 문서의 1을 무오류 생략 기본값으로 안내하지 않는다. 음수와 비정수도 `src/swanpre1.ftn:1164–1169`에서 오류로 보고한다. |
| R3:CP-003 | 주파수 의존 반사 | — (문서 누락) | 주파수 의존 반사. `src/swanser.ftn:3714–3715` `REF0 = FD1 +` / `FD2/PI * ATAN2(PI*FD3*(SPCSIG(IS)-FD4),FD2)`; 3716–3717은 0–1로 제한한다. 3718 `! >>> should REF0 not be squared? <<<`. | E 코드 결함 후보 · 중간 | 이 경로는 제곱하지 않은 `REF0`를 작용밀도에 곱한다. 고정 반사는 3318행에서 제곱한다. swantech PDF 63쪽 / 인쇄 55쪽의 반사계수도 파고비다. 반대 근거: FD 계수를 에너지비로 정의했을 가능성은 있다. 그러나 코드 주석이 제곱 누락을 직접 의심한다. `src/swanser.ftn:3087`의 `!          NOTE: these factors only to be applied to constant coeffs`는 자유고 배율을 일정 계수에만 적용한다고 명시한다. 따라서 RFD에서 자유고 배율이 사라지는 사실은 제곱 누락의 근거로 사용하지 않는다. `src/swanpre1.ftn:1181–1197`은 RFD 입력을 `LRFRD=1`로 저장한다. `src/swanser.ftn:3712`의 `IF (LRFRD.EQ.1) THEN`에서 계산한 값은 3761행에서 실제 작용밀도에 곱해진다. 3547행의 `REF0 ... reflection coefficient in terms of action density` 선언 주석은 반대 근거다. FD 입력을 파고비로 확정하지 않으므로 E·중간을 유지한다. git 최초 반입 `b2ae30e:src/swanser.ftn:4157–4161`에도 제곱 없는 식과 의문 주석이 있다. `7ee8981` 및 `43e9bbb`의 3714–3718행까지 유지된다. 노트에는 일정 반사의 제곱과 RFD의 직접 곱셈을 구분하고 제곱 누락 후보의 강도는 중간이라고 적는다. |
| R3:CP-004 | FREEBOARD 형상계수 하한 | — (문서 누락) | FREEBOARD 형상계수 하한. `src/swanpre1.ftn:1220` `ELSEIF ( GAMT.LT.0.1 ) THEN`; `src/swanpre1.ftn:1222` `GAMT = 0.1`; `src/swanpre1.ftn:1223` `ELSEIF ( GAMR.LT.0.1 ) THEN`; `src/swanpre1.ftn:1225` `GAMR = 0.1`. | E 코드 결함 후보 · 강함 | `IF ( GAMT.LT.0. .OR. GAMR.LT.0. ) THEN`은 음수만 오류로 보고한다. $0\leq GAMT<0.1$, $0\leq GAMR<0.1$이면 `ELSEIF ( GAMT.LT.0.1 ) THEN`만 실행하므로 `GAMR`를 보정하지 않는다. 두 값이 0이면 GAMR가 0인 채 `src/swanser.ftn:3089`의 `FBR = 0.5 * ( 1. + TANH(2.*FVH/GAMR) )`에 들어간다. FREE 입력은 `src/swanpre1.ftn:1212–1216`에서 이 경로를 활성화한다. 전처리로 제거되는 분기가 아니다. git 최초 반입 `b2ae30e:src/swanpre1.ftn:1200–1208`과 `7ee8981`·`43e9bbb`의 1217–1225행이 같다. E·강함을 유지한다. 노트에는 두 비음수 형상계수가 동시에 0.1 미만일 때 GAMT만 보정되고 GAMR의 분모가 보호되지 않는다고 적는다. |
| R3:CP-005 | 에너지비 합 검사 | — (문서 누락) | 에너지비 합 검사. `src/swanpre1.ftn:1246` `IF (LFREE.EQ.0 .AND. ITRAS.EQ.0 .AND. LREF.EQ.1) THEN`; `src/swanpre1.ftn:1247` `DUM = TRCF*TRCF + REF0*REF0`; `src/swanpre1.ftn:1248` `IF (DUM.GT.1.) CALL MSGERR(3,'Kt^2 + Kr^2 > 1 ')`; `src/swanser.ftn:3722` `IF ((REF0 + OBREDF(ID,IS,ILINK)) .GT. 1.) THEN`. | C 문서 누락 | swanuse PDF 84·node28:2590–2598은 파고비 제곱 합 검사를 이미 적는다. C는 그 문서와 swantech 2.5에 없는 적용 조건·초과 처리에 한정한다. 입력 검사는 `IF (LFREE.EQ.0 .AND. ITRAS.EQ.0 .AND. LREF.EQ.1) THEN`에서만 시행한다. FREEBOARD 등은 이 검사에서 제외한다. 실행 중 `IF ((REF0 + OBREDF(ID,IS,ILINK)) .GT. 1.) THEN`은 `REFLTST=.FALSE.`로 표시하며 합을 1로 재정규화하지 않는다. |
| R3:CP-007 | 회절 평균 파수·군속도의 고주파 꼬리 | — (문서 누락) | 회절 평균 파수·군속도의 고주파 꼬리. `src/swancom5.ftn:5652` `EKTOTL = EKTOTL + KLOC (IS) * EAD`; `src/swancom5.ftn:5653` `ECGTOT = ECGTOT + CGLOC(IS) * EAD`; `src/swancom5.ftn:5664` `EKTOTL = EKTOTL + CKTAIL * EAD`; `src/swancom5.ftn:5665` `ECGTOT = ECGTOT + CKTAIL * EAD`. | E 코드 결함 후보 · 강함 | 꼬리 항에는 각각 `KLOC(MSC)`와 `CGLOC(MSC)` 단위가 없다. 에너지에 파수 또는 속도를 곱한 내부 합에 에너지 단위의 값이 더해진다. 같은 함수의 5652–5653행 및 `src/SwanIntgratSpc.ftn90:336`의 `wpar(MSC)**p` 경로와 모순된다. 반대 근거: `MSC>3`에서만 꼬리 분기를 실행한다. GEN4는 회절 자체를 끈다. `src/swancom5.ftn:5662`의 `CKTAIL = 1. / (PPTAIL * (1. + PPTAIL * (FRINTH-1.)))`는 무차원이다. 일반 회절에서는 이 조건이 단위 오류를 복원하지 않는다. 실제 호출은 `src/swancom1.ftn:1675–1677`의 `IF ( IDIFFR.GT.0 )`와 `CALL DIFPAR`다. 이 호출과 꼬리 합에는 전처리 제외 표지가 없다. git 최초 반입 `b2ae30e`부터 `7ee8981:src/swancom5.ftn:5658–5665`, `43e9bbb`까지 같은 합이 유지된다. E·강함을 유지한다. 노트에는 이 후보를 `MSC>3`인 일반 회절 경로에 한정하고, 내부 합과 꼬리 항의 파수·군속도 단위가 다르다고 적는다. |
| R3:CP-008 | 회절 에너지·경계 보호와 지리 속도 선택 | — (문서 누락) | 회절 에너지·경계 보호와 지리 속도 선택. `src/swancom5.ftn:5674` `EN(IND) = MAX(ETOT,1.E-8)`; `src/swancom5.ftn:5887` `TMP = 0.`; `src/swanpre1.ftn:2118` `CALL INREAL ('CGMOD', PDIFFR(3), 'STA', 1.)`. 5685–5775는 젖고 장애물을 건너지 않는 이웃끼리만 평활한다. | C 문서 누락 | 분모가 양수가 아니면 내부 회절 매개변수 $\delta$를 0으로 둔다. 에너지에는 `EN(IND) = MAX(ETOT,1.E-8)` 하한을 적용한다. 평활화는 젖고 장애물을 건너지 않는 이웃끼리 수행한다. swanuse PDF 88·node28:3155–3164는 `CGMOD=0`일 때 지리 전파속도를 조정하지 않는다고 이미 적는다. 방향 굴절 보정에는 이 스위치를 적용하지 않는다(`src/swancom5.ftn:1603–1631`). C는 swantech 2.5.4와 swanuse DIFFRACTION 절에 없는 에너지·분모·이웃 보호 조건에 한정한다. |
| R3:CP-028 | 회절의 스펙트럼 평균과 흐름 병용 | — (문서 누락) | 회절의 스펙트럼 평균과 흐름 병용. `src/swancom5.ftn:5650` `EAD = SUM(AC2(:,IS,IND)) * DDIR * SPCSIG(IS)**2`; `src/swancom5.ftn:5672` `K (IND) = EKTOTL / ETOT`; `src/swancom5.ftn:5673` `CG(IND) = ECGTOT / ETOT`; 1627행의 `DIFPARAM(KCG1)*CAST5`는 주파수 이동의 흐름 변형항에 적용된다. | C 문서 누락 | `IF (ETOT.LE.0.) THEN`에서는 `K (IND) = 10.`, `CG(IND) = 0.`, `EN(IND) = 0.`이다(`src/swancom5.ftn:5667–5670`). 양의 ETOT 분기는 에너지 가중 합으로 평균 파수·군속도를 구한다. 매 주파수마다 별도 회절장을 풀지 않는다. swantech (2.136)은 무류 설명이지만 코드 1622–1628행은 회절과 흐름을 함께 적용한다. C는 swantech 2.5.4와 swanuse DIFFRACTION 절에 없는 평균장 구성·흐름 병용의 구현 세부에 한정한다. 꼬리 합의 단위 불일치는 CP-007의 별도 E 판정이다. |
| R3:CP-030 | 회절의 전파법 변경 | — (문서 누락) | 회절의 전파법 변경. `src/swanmain.ftn:4090` `IF ( IDIFFR.EQ.1 ) THEN`; `src/swanmain.ftn:4094` `PROPSN = 1`; `src/swanmain.ftn:4095` `PROPSS = 1`. | C 문서 누락 | `IF ( IDIFFR.EQ.1 ) THEN`에서 `PROPSN = 1`, `PROPSS = 1`을 대입하여 정상·비정상 전파법을 BSBT로 바꾼다. 이 대입에는 안내문이 없다. 양의 모든 IDIFFR 값으로 조건을 넓히지 않는다. C는 swantech 2.5.4의 (2.136)–(2.142)와 swanuse DIFFRACTION 절에 없는 이 전파법 대입에 한정한다. |
| R3:NT-001 | 회절 노트의 δ 분모 | 현재 노트의 수정 전 원문: `source-analysis/swan-diffraction-obstacles.md:41` `δ = D · ∇(D∇H) / (k² · H)` | `src/swancom5.ftn:5823–5825` `TMP = 0.5*(CG(INDL)/K(INDL)+CG(IND)/K(IND)) *` / `DYLOC * (EN(IND)-EN(INDL)) / DXLOC` / `EAD = DXLOC * DYLOC * EN(IND)*CG(IND)*K(IND)`; `src/swancom5.ftn:5885` `TMP = 2.*LAPE(IND)/DENOM(IND)`. `src/SwanDiffPar.ftn90:68` `! k^2 pH`. `src/SwanDiffPar.ftn90:319–320,350–353`의 실행문. 웹 `online_doc/swantech/node29.html`도 분모에 $k^2$를 적지 않는다. | B 문서 오기 | 회절 매개변수는 $\delta=\nabla\cdot(p\nabla H)/(k^2pH)$다. 여기서 $p=cc_g$다. $H$는 파고에 비례한다. 매뉴얼 (2.138)의 인쇄 분모에는 $k^2$가 빠졌다. |
| R3:NT-002 | 회절·반사 노트의 권고 수치 | 현재 노트의 수정 전 원문: `source-analysis/swan-diffraction-obstacles.md:61` `Typical settings:` 뒤 `SMPAR=0.2, SMNUM=5`; 155 `ensure mesh resolution ≥ structure scale × 4.`; 156 `sand: 4; rocky: 8`. | — | H 코드 대조 대상 아님 | 코드 생략값은 `SMPAR=0`, `SMNUM=0`이다. swantech PDF 65쪽 / 인쇄 57쪽은 $n=6$을 권고한다. 5회, 구조물 크기의 4배, 모래 4·암석 8이라는 수치는 출처를 붙이기 전까지 권고에서 삭제한다. |
| R3:NT-003 | 장애물 계수의 파고비·에너지비 | 현재 노트의 수정 전 원문: `source-analysis/swan-diffraction-obstacles.md:71` `(50% pass-through)`와 `(70% reflection)`; 141 `(60% reflection, diffuse)`. | `src/swanser.ftn:3114`는 `TRCF(1,1) = OBHKT * OBHKT`이고 3318행은 `REFLCOEF = SQRTREF * SQRTREF`다. | F 표기 차이 | 입력 투과·반사계수의 백분율은 파고비라고 명시한다. 일정 계수이고 FREEBOARD 보정이 없는 경우 `TRANS 0.5`, `REFL 0.7`, `REFL 0.6`의 에너지비는 각각 0.25, 0.49, 0.36이다. 난반사의 방향별 분배와 전체 반사비를 구분한다. |
| R3:NT-004 | 장애물 예제의 옵션 순서 | 현재 노트의 수정 전 원문: `source-analysis/swan-diffraction-obstacles.md:141` `OBSTACLE LINE x1 y1 x2 y2 TRANS 0.0 REFL 0.6 RDIFF 4`; 142–143도 `LINE` 뒤에 계수를 적는다. | `src/swanpre1.ftn:952–964`는 투과·반사·FREEBOARD 옵션 뒤에 LINE을 둔다. 실제 파서는 1150–1229행에서 계수를 읽은 뒤 1256–1263행에서 LINE 좌표를 읽는다. 1163행의 `CALL INREAL ('POWN', POWN, 'REQ', 1.)`은 생략 시 `src/ocpcre.ftn:656–676`에서 오류를 보고한다. | B 문서 오기 | 명령 예는 `OBSTACLE TRANS 0.0 REFL 0.6 RDIFF 4 LINE x1 y1 x2 y2`로 고친다. `LINE` 좌표는 옵션 뒤에 둔다. `RDIFF`의 지수는 필수 입력이다. |
| R3:NT-005 | 회절 비활성화의 출력 메시지 | 현재 노트의 수정 전 원문: `source-analysis/swan-diffraction-obstacles.md:164` `auto-disabled silently.` | `src/swanpre1.ftn:3093`의 GEN4 해석은 `IDIFFR = 0`을 대입한다. 실행 전 검사 `src/swanmain.ftn:6394–6398`은 GEN4에서 `IF ( IDIFFR.GT.0 ) THEN`일 때만 수준 0 안내문을 내고 이후 `IDIFFR = 0`으로 둔다. 6454–6457행은 `IF ( IQCM.NE.0 .AND. IDIFFR.GT.0 ) THEN`에서 수준 1 경고 뒤 회절을 끈다. | B 문서 오기 | GEN4 명령 해석 단계의 회절 해제는 조용히 수행된다. 실행 전 검사까지 IDIFFR가 양수이면 GEN4 안내문이 나온다. QC와 회절이 함께 켜진 실행 전 검사에서는 경고가 나온다. 입력 순서와 검사 시점의 IDIFFR에 따라 출력 여부가 달라지므로 항상 무음 또는 항상 안내문이라고 쓰지 않는다. |
| R5:PN-183 | 입력 순서·반사비 | 현재 노트의 수정 전 원문: `source-analysis/swan-diffraction-obstacles.md:141` `OBSTACLE LINE x1 y1 x2 y2 TRANS 0.0 REFL 0.6 RDIFF 4` | `src/swanser.ftn:3318` `REFLCOEF = SQRTREF * SQRTREF`. | B | OBSTACLE 선택은 LINE보다 먼저 쓴다. 반사계수는 파고 비다. BREAKING과 FREEBOARD의 누락 인수도 보충한다. | [10-13 전수 검증 정정]
