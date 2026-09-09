---
title: "XBeach non-hydrostatic model draft report (2010)"
model: XBeach
layer: 2
depends_on: []
canonical_source: self
citation_status: verified
has_source_needed: false
verification_method: "Exhaustive locator/provenance cross-reference for XH001-XH207 using OpenDataLoader v2.4.7 page-aware PDF extraction, original DOCX document-order blocks, and original-bound OLE DOC text extracts; semantic dispositions inherited from immutable X00 with targeted independent spot checks"
verification_by: "Codex (cross-ref)"
verification_date: 2026-09-09
note_author: "Codex"
note_date: 2026-09-09
source_scope: "XBeach non-hydrostatic model draft report 2010"
---

# XBeach non-hydrostatic model draft report (2010)

이 문서는 XBeach 문서 전수검수의 HIGH 207건 중 이 출처에 속하는 판본 한정 판정을 통합한다. 문서의 설명은 다른 판본이나 현재 코드의 기본값으로 자동 확장하지 않는다. PDF 인용은 physical page와 문서 자체의 printed page를 구분한다. DOCX locator는 원본 문서의 문단·표 행 순서와 직접 인용을 쓰며 PDF page를 부여하지 않는다. OLE DOC의 부분 정렬 항목은 원본에 결박된 text extract의 행·해시·직접 인용과 보고서 printed section만 기록하고 physical page를 주장하지 않는다. 같은 work의 reciprocal DOC/DOCX↔PDF 후보는 공동검토 묶음으로 배치했지만 두 finding은 독립 원장 항목이며 묶음이 의미 동일성을 주장하지 않는다.

## 검증 범위

XH001-XH207의 원본 정체·해시·표현 행·페이지 또는 문서 block locator는 전수 확인했다. `cross-format-partial` 15건은 불완전한 PDF 정렬을 citation으로 쓰지 않고, DOCX 9건은 원본 block, OLE DOC 6건은 원본에 결박된 text-extract 행과 직접 인용으로 대체했다. 의미 판정은 immutable X00 전수독해 결과를 보존하며, 별도의 독립 의미 재독해는 posdwn, 손상된 vardens, standing-wave, 1D solver, NetCDF와 DOCX retrieval 표본에 집중했다. 따라서 공동검토 묶음은 중복 제거를 위한 의미 동치 판정이 아니다.

## 출처 고정

- `models/XBeach/raw/source_code/trunk/doc/reports/non-hydrostatic_report_draft.doc` — SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`
- `models/XBeach/raw/source_code/trunk/doc/reports/non-hydrostatic_report_draft.pdf` — SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`

## 비정수압 검증 사례

<a id="xh162"></a>
### N-001 — XH162

**판정:** 2010 초안의 사실·한계로 채택.

- The draft reports underestimated surf-zone energy dissipation and overestimated high-frequency energy and wave heights because depth averaging omits vertical structure including undertow and rollers.

**출처 locator:**

- XH162: non-hydrostatic_report_draft.doc, DOC/DOCX→동일 work PDF 정렬, physical PDF p.3, 19, printed page/frontmatter frontmatter-physical-3, 9, audit extract lines 21-22,689; 원본 SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`.
<a id="xh172"></a>
<a id="xh196"></a>
### N-002 — XH172, XH196

**판정:** 2010 초안의 사실·한계로 채택.

- The frictionless dam-break comparison disables non-hydrostatic corrections and uses '2000' points over '100 m', upstream depth '1 m', wet downstream depth '0.1 m' and 'CFL=0.4'.
- The oscillating-basin test uses kH=0.5 and CFL=0.5, the solitary-wave test uses depth 1 m with 160 points per wavelength and CFL=0.9, and the 2000-point dam-break test uses CFL=0.4 with non-hydrostatic corrections disabled.

**출처 locator:**

- XH172: non-hydrostatic_report_draft.doc, DOC/DOCX→동일 work PDF 정렬, physical PDF p.35, 41, 43, 44, printed page/frontmatter 25, 31, 33, 34, audit extract lines 1481-1488,1670-1672,1745-1757; 원본 SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`.
- XH196: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.43, 44, printed page/frontmatter 33, 34, audit extract lines 3891-3901; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
<a id="xh174"></a>
<a id="xh197"></a>
### N-003 — XH174, XH197

**판정:** 2010 초안의 사실·한계로 채택.

- The shoal test uses a '35 by 20 m' tank, '1 Hz' waves of height '4.64 cm', about '60 points per wavelength' over the shoal and a '60 s' simulation, but significantly underpredicts the focusing peak at transect 5, 'x=9'.
- The shoal test specifies a 35-by-20 m tank, 1 Hz waves of height 4.64 cm, approximately 60 points per wavelength near the shoal, a 60 s run and an underpredicted focusing peak at transect 5, x=9 m.

**출처 locator:**

- XH174: non-hydrostatic_report_draft.doc, DOC/DOCX→동일 work PDF 정렬, physical PDF p.46, 47, printed page/frontmatter 36, 37, audit extract lines 1792-1827; 원본 SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`.
- XH197: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.46, 47, printed page/frontmatter 36, 37, audit extract lines 4143-4163; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
<a id="xh193"></a>
### N-004 — XH193

**판정:** 2010 초안의 사실·한계로 채택.

- The standing-wave test uses 'L=100 m', 'kH=0.5', '100x100' grid points and 'CFL=0.5', with a separate dispersion sweep over '0.1<=kh<=7'.

**출처 locator:**

- XH193: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.35, printed page/frontmatter 25, audit extract lines 3390-3394; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
<a id="xh195"></a>
### N-005 — XH195

**판정:** 2010 초안의 사실·한계로 채택.

- The solitary-wave test uses '1 m' depth, '160 points per wavelength', 'CFL=0.9' and amplitude ratios '0.1, 0.2, 0.4', with noticeably reduced amplitude at 0.4 and initial profile adjustment over about '10 Lsol'.

**출처 locator:**

- XH195: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.41, 42, printed page/frontmatter 31, 32, audit extract lines 3804-3825; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
## 비정수압 물리·수치법

<a id="xh163"></a>
### N-006 — XH163

**판정:** 2010 초안의 사실·한계로 채택.

- The formulation assumes incompressible homogeneous Newtonian flow, a single-valued free surface, negligible bed-motion time derivative, zero uniform atmospheric pressure, no surface tension or local wind-wave generation, and zero normal velocity at closed boundaries.

**출처 locator:**

- XH163: non-hydrostatic_report_draft.doc, DOC/DOCX→동일 work PDF 정렬, physical PDF p.13, 14, 15, 17, printed page/frontmatter 3, 4, 5, 7, audit extract lines 394-402,463-478,617-642; 원본 SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`.
<a id="xh165"></a>
### N-007 — XH165

**판정:** 2010 초안의 사실·한계로 채택.

- The Smagorinsky constant is stated to be typically 0.1–0.3 and the filter length depends on mesh size, with little added dissipation in smooth flow.

**출처 locator:**

- XH165: non-hydrostatic_report_draft.doc 원본 OLE DOC text extract lines 690-723 (DOC SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`; extract SHA-256 `54f1444c6f52371894f49ed6e1367ef86fedcbd2acaa7cef694a76f25b7dd9db`); 직접 인용: L723 “Because the magnitude of the eddy viscosity depends on the gradients in the velocity field the Smagorinsky sub-grid model adds very little dissipation in …”; L713 “is the characteristic length scale of the smallest resolvable eddy. The characteristic length scale is essentially the filter width employed and is therefore dependent …”; L711 “is the Smagorinsky constant (typically ~0.1-0.3) and”; 대응 printed section 9, 10. 불완전한 PDF 정렬은 citation에서 폐기하며 DOC 또는 PDF physical page를 주장하지 않음.
<a id="xh166"></a>
### N-008 — XH166

**판정:** 2010 초안의 사실·한계로 채택.

- Central differences on nonuniform grids can become first order, the minmod predictor-corrector becomes first order near discontinuities, and explicit Euler treatment of stresses makes formal time accuracy first order despite the abstract's second-order claim.

**출처 locator:**

- XH166: non-hydrostatic_report_draft.doc 원본 OLE DOC text extract lines 779-850,876,1013 (DOC SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`; extract SHA-256 `54f1444c6f52371894f49ed6e1367ef86fedcbd2acaa7cef694a76f25b7dd9db`); 직접 인용: L876 “is used. This scheme consists of a first order predictor step and a flux limited corrector step. The hydrostatic pressure is integrated using the …”; L850 “The predictor-corrector set is second order accurate in regions where the solution is smooth, and reduces locally to first order accuracy near discontinuities. Furthermore, …”; L1013 “The predictor-corrector set is second order accurate in regions where the solution is smooth, and reduces to first order accuracy near sharp gradients in …”; 대응 printed section 12, 13, 14, 16. 불완전한 PDF 정렬은 citation에서 폐기하며 DOC 또는 PDF physical page를 주장하지 않음.
<a id="xh167"></a>
<a id="xh187"></a>
### N-009 — XH167, XH187

**판정:** 2010 초안의 사실·한계로 채택.

- The vertical pressure treatment uses the surface condition 'p=0' and is described as equivalent to the Keller-box/Hermitian approach.
- Dynamic pressure at the free surface is exactly zero and the pressure discretization is stated to be numerically equivalent to Keller-box or Hermitian formulations.

**출처 locator:**

- XH167: non-hydrostatic_report_draft.doc 원본 OLE DOC text extract lines 1025-1112 (DOC SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`; extract SHA-256 `54f1444c6f52371894f49ed6e1367ef86fedcbd2acaa7cef694a76f25b7dd9db`); 직접 인용: L1025 “The pressures are defined on the cell faces and therefore do not have to be interpolated. Furthermore, we can exactly set the dynamic pressure …”; L1104 “. This is mainly due to the application of the McCormack scheme for the advection. The discretisation of the pressure term is numerically fully …”; L1029 “needs to be expressed in terms of the bottom and surface velocities. Using a simple central approximation gives”; 대응 printed section 16, 17. 불완전한 PDF 정렬은 citation에서 폐기하며 DOC 또는 PDF physical page를 주장하지 않음.
- XH187: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.26, 27, printed page/frontmatter 16, 17, audit extract lines 2477,2764; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
<a id="xh169"></a>
<a id="xh189"></a>
### N-010 — XH169, XH189

**판정:** 2010 초안의 사실·한계로 채택.

- Dry points receive zero velocity and a pressure equation with diagonal '1' and right-hand side '0', while higher-order reconstruction requires all three stencil surface levels to exceed all three bed levels.
- Dry velocity points are set to zero, fully dry pressure rows use diagonal 1 and right-hand side 0, higher-order reconstruction is disabled unless the lowest stencil surface exceeds the highest bed, and shallow-water pressure-point removal defaults to zero.

**출처 locator:**

- XH169: non-hydrostatic_report_draft.doc, DOC/DOCX→동일 work PDF 정렬, physical PDF p.29, 30, printed page/frontmatter 19, 20, audit extract lines 1205-1242; 원본 SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`.
- XH189: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.29, 30, printed page/frontmatter 19, 20, audit extract lines 2914-2927; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
<a id="xh170"></a>
### N-011 — XH170

**판정:** 2010 초안의 사실·한계로 채택.

- The pressure system is pentadiagonal in 2D, SIP requires relaxation below 1 without guaranteed convergence, the last iterate is accepted at the iteration cap, and Thomas solution is recommended for 1D.

**출처 locator:**

- XH170: non-hydrostatic_report_draft.doc 원본 OLE DOC text extract lines 1263-1313 (DOC SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`; extract SHA-256 `54f1444c6f52371894f49ed6e1367ef86fedcbd2acaa7cef694a76f25b7dd9db`); 직접 인용: L1313 “For one-dimensional situations (e.g. when simulation a flume experiment) the linear system reduces to a tri-diagonal system. For such linear systems a direct solver, …”; L1275 “has been used. This method was specifically designed for elliptic problems and sparse banded matrices. In general SIP solver requires more iterations per time …”; L1309 “iterations the iteration process is also terminated and the last iterative solution is used. By default this is set to”; 대응 printed section 21, 22. 불완전한 PDF 정렬은 citation에서 폐기하며 DOC 또는 PDF physical page를 주장하지 않음.
<a id="xh171"></a>
<a id="xh192"></a>
### N-012 — XH171, XH192

**판정:** 2010 초안의 사실·한계로 채택.

- For 'kd<1' the untuned one-layer dispersion errors remain approximately below '5%', but for 'kd>1' they grow rapidly and additional vertical resolution is required.
- The draft states that dispersion-related relative error stays approximately below 5% for kd<1 and grows rapidly for kd>1, requiring greater vertical resolution for shorter waves.

**출처 locator:**

- XH171: non-hydrostatic_report_draft.doc, DOC/DOCX→동일 work PDF 정렬, physical PDF p.33, printed page/frontmatter 23, audit extract lines 1456; 원본 SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`.
- XH192: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.33, printed page/frontmatter 23, audit extract lines 3214; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
<a id="xh173"></a>
<a id="xh194"></a>
### N-013 — XH173, XH194

**판정:** 2010 초안의 사실·한계로 채택.

- For the interval '0<kH<1' the report gives an optimum dispersion coefficient 'alpha approximately 0.8', but says its effects on nonlinear interactions are unknown and single-frequency optimization can worsen other components.
- Dispersion tuning targets 0<kH<kHmax with kHmax approximately 1, can worsen longer-wave errors when optimized for large kH, and has an explicitly unknown influence on nonlinear interactions.

**출처 locator:**

- XH173: non-hydrostatic_report_draft.doc, DOC/DOCX→동일 work PDF 정렬, physical PDF p.37, 38, 39, printed page/frontmatter 27, 28, 29, audit extract lines 1516-1620; 원본 SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`.
- XH194: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.37, 38, 39, printed page/frontmatter 27, 28, 29, audit extract lines 3524,3546,3647,3715; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
<a id="xh178"></a>
<a id="xh202"></a>
### N-014 — XH178, XH202

**판정:** 2010 초안의 사실·한계로 채택.

- The recommended short-wave setup uses velocity and surface forcing with 'instat=8', 'front=4', 'arc=1' and 'secorder=1', with about '30 meshes per wavelength', while instat=3 is limited to sufficiently long waves.
- The recommended configuration uses instat=8 with velocity and surface elevation for front=4/arc=1, secorder=1, and approximately 30 meshes per wavelength.

**출처 locator:**

- XH178: non-hydrostatic_report_draft.doc, DOC/DOCX→동일 work PDF 정렬, physical PDF p.54, printed page/frontmatter 44, audit extract lines 1895-1898; 원본 SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`.
- XH202: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.53, 54, printed page/frontmatter 43, 44, audit extract lines 4293-4305; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
<a id="xh182"></a>
### N-015 — XH182

**판정:** 2010 초안의 사실·한계로 채택.

- The single-layer formulation assumes homogeneous incompressible Newtonian flow and decomposes pressure as 'P=rho*g*(eta-z)+rho*p+p0'.

**출처 locator:**

- XH182: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.11, 14, printed page/frontmatter 1, 4, audit extract lines 248,320,336,373; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
<a id="xh183"></a>
### N-016 — XH183

**판정:** 2010 초안의 사실·한계로 채택.

- The derivation neglects bed time variation and surface tension, imposes surface non-hydrostatic pressure 'p=0' and zero wall-normal velocity, and requires more vertical resolution to represent undertow.

**출처 locator:**

- XH183: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.15, 16, 17, printed page/frontmatter 5, 6, 7, audit extract lines 424,530,662-674; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
<a id="xh186"></a>
### N-017 — XH186

**판정:** 2010 초안의 사실·한계로 채택.

- The minmod limiter is 'psi=max(0,min(r,1))', giving second-order behavior in smooth regions and first order at discontinuities, while explicit Euler stress terms make the overall method formally first order despite the introductory second-order claim.

**출처 locator:**

- XH186: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.22, 23, 24, printed page/frontmatter 12, 13, 14, audit extract lines 823-829,1055,1130,1206; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
<a id="xh190"></a>
### N-018 — XH190

**판정:** 2010 초안의 사실·한계로 채택.

- Pressure-point removal uses the shortest resolved wavelength 'L=2*Delta x' and a wave-shortness threshold kdmin whose default is '0.0', disabling this removal.

**출처 locator:**

- XH190: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.30, 63, printed page/frontmatter 20, 53, audit extract lines 2933-2953,4825; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
<a id="xh205"></a>
### N-019 — XH205

**판정:** 2010 초안의 사실·한계로 채택.

- The dispersion coefficient defaults to 'dispc=1'; positive values are spatially constant and negative values optimize locally using 'Topt', whose default is '10 s'.

**출처 locator:**

- XH205: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.62, printed page/frontmatter 52, audit extract lines 4808-4809; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
## 파랑 경계·스펙트럼

<a id="xh181"></a>
### N-020 — XH181

**판정:** 2010 초안의 사실·한계로 채택.

- Boun_U.bcf accepts 2–4 variables including time and mandatory U, interpolates between supplied times, and repeats its last row indefinitely after the final timestamp.

**출처 locator:**

- XH181: non-hydrostatic_report_draft.doc, DOC/DOCX→동일 work PDF 정렬, physical PDF p.65, 66, printed page/frontmatter 55, 56, audit extract lines 2261-2303; 원본 SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`.
## 혼합 매개변수 기본값·입력 규약

<a id="xh164"></a>
### N-021 — XH164

**판정:** 2010 초안의 사실·한계로 채택.

- The depth-averaged approximation requires weak vertical velocity-profile variation and explicitly calls for additional vertical resolution when undertow produces a nonuniform profile.

**출처 locator:**

- XH164: non-hydrostatic_report_draft.doc, DOC/DOCX→동일 work PDF 정렬, physical PDF p.16, printed page/frontmatter 6, audit extract lines 529; 원본 SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`.
<a id="xh206"></a>
### N-022 — XH206

**판정:** 2010 초안의 사실·한계로 채택.

- The boundary file contains '2 to 4' variables with time and horizontal velocity mandatory, requires surface elevation for 'front=4, arc=1', interpolates between records and repeats the last record indefinitely after its final time.

**출처 locator:**

- XH206: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.65, printed page/frontmatter 55, audit extract lines 4852-4867; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
## 흐름 마찰·점성

<a id="xh185"></a>
### N-023 — XH185

**판정:** 2010 초안의 사실·한계로 채택.

- The Smagorinsky coefficient is described as 'Cs approximately 0.1–0.3', with nuh representing Cs when smag=1 and background viscosity otherwise.

**출처 locator:**

- XH185: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.20, 63, printed page/frontmatter 10, 53, audit extract lines 749-751,4816-4818; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
## 흐름·조석·유량 경계

<a id="xh168"></a>
<a id="xh188"></a>
### N-024 — XH168, XH188

**판정:** 2010 초안의 사실·한계로 채택.

- The radiation-boundary derivation assumes a straight boundary, flat bed and linear waves with long reflected waves normal to the boundary, and warns of errors for oblique reflections and complex geometry.
- The absorbing-generating boundary assumes a straight boundary, locally flat bed, linear incoming waves and long reflected waves perpendicular to the boundary, with significant errors expected for more complex geometries.

**출처 locator:**

- XH168: non-hydrostatic_report_draft.doc, DOC/DOCX→동일 work PDF 정렬, physical PDF p.27, 28, 29, printed page/frontmatter 17, 18, 19, audit extract lines 1114-1200; 원본 SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`.
- XH188: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.27, 28, 29, printed page/frontmatter 17, 18, 19, audit extract lines 2770,2840,2868,2906; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
