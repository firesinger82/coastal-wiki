---
title: "XBeach document discrepancies and version drift"
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
source_scope: "three historical XBeach works plus frozen source snapshot"
---

# XBeach document discrepancies and version drift

이 문서는 XBeach 문서 전수검수의 HIGH 207건 중 이 출처에 속하는 판본 한정 판정을 통합한다. 문서의 설명은 다른 판본이나 현재 코드의 기본값으로 자동 확장하지 않는다. PDF 인용은 physical page와 문서 자체의 printed page를 구분한다. DOCX locator는 원본 문서의 문단·표 행 순서와 직접 인용을 쓰며 PDF page를 부여하지 않는다. OLE DOC의 부분 정렬 항목은 원본에 결박된 text extract의 행·해시·직접 인용과 보고서 printed section만 기록하고 physical page를 주장하지 않는다. 같은 work의 reciprocal DOC/DOCX↔PDF 후보는 공동검토 묶음으로 배치했지만 두 finding은 독립 원장 항목이며 묶음이 의미 동일성을 주장하지 않는다.

## 검증 범위

XH001-XH207의 원본 정체·해시·표현 행·페이지 또는 문서 block locator는 전수 확인했다. `cross-format-partial` 15건은 불완전한 PDF 정렬을 citation으로 쓰지 않고, DOCX 9건은 원본 block, OLE DOC 6건은 원본에 결박된 text-extract 행과 직접 인용으로 대체했다. 의미 판정은 immutable X00 전수독해 결과를 보존하며, 별도의 독립 의미 재독해는 posdwn, 손상된 vardens, standing-wave, 1D solver, NetCDF와 DOCX retrieval 표본에 집중했다. 따라서 공동검토 묶음은 중복 제거를 위한 의미 동치 판정이 아니다.

## 출처 고정

- `models/XBeach/raw/source_code/trunk/doc/manual/XBeach_manual_kingsday.docx` — SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`
- `models/XBeach/raw/source_code/trunk/doc/manual/XBeach_manual_kingsday.pdf` — SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`
- `models/XBeach/raw/source_code/trunk/doc/manual/XBeach_manual_master.docx` — SHA-256 `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236`
- `models/XBeach/raw/source_code/trunk/doc/manual/XBeach_manual_master.pdf` — SHA-256 `6e594e6fff7cf285c74c1877573061fed460f70658541cd29dd986475517c7f7`
- `models/XBeach/raw/source_code/trunk/doc/reports/non-hydrostatic_report_draft.doc` — SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`
- `models/XBeach/raw/source_code/trunk/doc/reports/non-hydrostatic_report_draft.pdf` — SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`
- 고정 source-adjudication digest — SHA-256 `56075b0e74b75050881292c5a95cca17813b4570457f3585a614d7f34c9f16fa`. 아래 8개 판정의 repo-relative source line과 원문 SHA가 구현 근거다.

## 고정 소스 snapshot 판정

이 8개 판정은 문서 모순을 지우지 않는다. 보관 source snapshot에서 확인되는 구현 동작만 정하며, 각 역사 문서의 양측 진술은 해당 XH 항목에 그대로 남긴다.

<a id="source-adjudication-wci"></a>
### `wci`

기록된 소스 snapshot의 surfbeat 경로에서 wci=1은 흐름에 따른 파랑 굴절/수심 처리를 활성화하고, 0은 흐름 유속 기울기를 0으로 둔다. 입력 기본값은 0이다. 문서의 wci=1을 no interaction으로 설명한 문구를 현재 구현 설명으로 사용하지 않는다.

소스 근거: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_instationary.F90:131-138 (SHA-256 `9584b6ec2138353aba65991a4ec570b4b794554485cea43915c6071e9e2ed45a`); models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_instationary.F90:167-177 (SHA-256 `9584b6ec2138353aba65991a4ec570b4b794554485cea43915c6071e9e2ed45a`); models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90:669-674 (SHA-256 `73648b5733a8f90a8f18cda32743bdc2ef42f649e39c521e28e06584ee63c359`).

<a id="source-adjudication-nuh"></a>
### `nuh`

nuh는 smag 분기에 따라 의미가 달라진다. smag=1에서 par%nuh는 무차원 Smagorinsky 계수로 제곱되어 격자면적·변형률에 곱해지고, smag=0에서는 출력 점성계수 s%nuh에 직접 대입되어 m²/s 값으로 쓰인다. 해당 snapshot 입력 기본값은 nuh=0.1, smag=1이다. s%nuh 출력의 단위와 par%nuh 입력의 조건부 단위를 구분한다.

소스 근거: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/flow_timestep.F90:365-377 (SHA-256 `50742b601cc8feccd513cf742ca772b6021f1d4f5ffe074c4e8ffc90907dd2b2`); models/XBeach/raw/source_code/trunk/src/xbeachlibrary/flow_timestep.F90:1008-1023 (SHA-256 `50742b601cc8feccd513cf742ca772b6021f1d4f5ffe074c4e8ffc90907dd2b2`); models/XBeach/raw/source_code/trunk/src/xbeachlibrary/flow_timestep.F90:1047-1062 (SHA-256 `50742b601cc8feccd513cf742ca772b6021f1d4f5ffe074c4e8ffc90907dd2b2`); models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90:743-748 (SHA-256 `73648b5733a8f90a8f18cda32743bdc2ef42f649e39c521e28e06584ee63c359`).

<a id="source-adjudication-bedfriction"></a>
### `bedfriction`

마찰 파일을 쓰지 않는 조건에서 기본 계수는 선택한 마찰식에 종속된다: Chezy는 55, cf는 0.003, Manning은 0.02, White-Colebrook은 0.01이다. Chezy 분기는 g/C²로 cf를 계산하므로 Chezy C에 0.003을 넣는 것은 cf=0.003과 동등하지 않다. 문서 변환으로 깨진 마찰 공식은 이 소스식으로 원문을 복원했다고 주장하지 않고 별도 제외한다.

소스 근거: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90:707-727 (SHA-256 `73648b5733a8f90a8f18cda32743bdc2ef42f649e39c521e28e06584ee63c359`); models/XBeach/raw/source_code/trunk/src/xbeachlibrary/bedroughness.F90:68-75 (SHA-256 `508ccef2919d203a716f831f4ffd80a57068562eab747a00a94da802a840dfef`).

<a id="source-adjudication-dilatancy"></a>
### `dilatancy`

이 snapshot에서 dilatancy=1일 때 srfRhee는 erosion velocity와 (pormax-por), rheeA 등에 비례한다. 양의 침투계수·밀도비 및 pormax>=por 조건에서는 srfRhee>=0이고, 경사 효과를 끄면 srfTotal=1+srfRhee이다. 이에 따라 임계 bed-load 속도는 Ucr*sqrt(srfTotal), 경사 total 모드가 아닌 suspended-load 속도는 Ucr*(1+sqrt(srfRhee))로 증가한다. 코드 주석의 A는 단일입자 3/4, 연속체 1/(1-n0)이며 입력 rheeA 기본값은 0.75이다. 문서의 감소 설명과 수식/주석 모순은 이 구현과 구분해 기록한다.

소스 근거: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/morphevolution.F90:1539-1553 (SHA-256 `765f474008f7cb843353dc0790cc3f3ebdc00631353da7592e2bb0508e968391`); models/XBeach/raw/source_code/trunk/src/xbeachlibrary/morphevolution.F90:1593-1599 (SHA-256 `765f474008f7cb843353dc0790cc3f3ebdc00631353da7592e2bb0508e968391`); models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90:1114-1119 (SHA-256 `73648b5733a8f90a8f18cda32743bdc2ef42f649e39c521e28e06584ee63c359`).

<a id="source-adjudication-adaptation-time"></a>
### `adaptation-time`

기록된 구현은 먼저 Ts=tsfac*hloc/w를 계산하고 oldTsmin=1이면 max(Ts,Tsmin), 그 밖에는 max(Ts,dtlimTs*dt)를 취한다. 더하기가 아니다. snapshot의 oldTsmin 기본값은 0, dtlimTs는 5이며 이 조건에서 Tsmin을 공통 고정 하한이라고 설명하지 않는다.

소스 근거: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/morphevolution.F90:1506-1513 (SHA-256 `765f474008f7cb843353dc0790cc3f3ebdc00631353da7592e2bb0508e968391`); models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90:1420-1425 (SHA-256 `73648b5733a8f90a8f18cda32743bdc2ef42f649e39c521e28e06584ee63c359`).

<a id="source-adjudication-posdwn"></a>
### `posdwn`

문서의 규약은 양의 아래 방향 수심 posdwn=1, 양의 위 방향 고도 posdwn=-1로 구분해야 한다. 실제 snapshot은 s%zb=-s%zb*s%posdwn으로 내부 바닥고를 만들며 ±1에서 이 규약을 따른다. 예제의 posdwn=0을 그대로 넣으면 변환 곱이 0이 되어 해당 초기화 경로의 바닥고가 0으로 소거된다. 0을 -1의 별칭으로 보지 않는다.

소스 근거: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90:155-160 (SHA-256 `73648b5733a8f90a8f18cda32743bdc2ef42f649e39c521e28e06584ee63c359`); models/XBeach/raw/source_code/trunk/src/xbeachlibrary/initialize.F90:40-55 (SHA-256 `9803067bd2fa4962d9e2247f6e8b5f87e18a9860802595424183994a715523cd`); models/XBeach/raw/source_code/trunk/src/xbeachlibrary/initialize.F90:240-249 (SHA-256 `9803067bd2fa4962d9e2247f6e8b5f87e18a9860802595424183994a715523cd`).

<a id="source-adjudication-dthetaS_XB"></a>
### `dthetaS_XB`

SWAN 스펙트럼을 읽는 이 코드에서 dthetaS_XB는 Cartesian SWAN x축에서 East x축으로 회전하는 반시계 각도이다. Cartesian 입력은 specin%ang에서 이 값을 빼고, nautical 입력은 270-angle로 변환하는 별도 분기를 쓴다. 매뉴얼 산문의 XBeach x축 표기를 이 매개변수의 실제 참조축으로 일반화하지 않는다.

소스 근거: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_boundary_update.f90:910-919 (SHA-256 `9c364a2c916f034338044b542c0231f412553812a16c11346a6bcc98319a80c7`); models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90:481-485 (SHA-256 `73648b5733a8f90a8f18cda32743bdc2ef42f649e39c521e28e06584ee63c359`).

<a id="source-adjudication-secorder"></a>
### `secorder`

2010 보고서의 sec_order 표기는 현재 보관 snapshot의 secorder와 구분한다. 소스는 secorder=1일 때 2차 이류 보정을 호출하며 nonh 입력 기본값은 1(그 밖은 0)이다. nonh에서 0을 넣어도 일관성 검사에서 1로 강제한다. 이 사실은 2010 코드의 동작을 역으로 입증하지 않으며 보고서 안의 상반된 옵션 설명은 역사적 문서 모순으로 기록한다.

소스 근거: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90:1406-1410 (SHA-256 `73648b5733a8f90a8f18cda32743bdc2ef42f649e39c521e28e06584ee63c359`); models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90:1739-1746 (SHA-256 `73648b5733a8f90a8f18cda32743bdc2ef42f649e39c521e28e06584ee63c359`); models/XBeach/raw/source_code/trunk/src/xbeachlibrary/flow_timestep.F90:645-652 (SHA-256 `50742b601cc8feccd513cf742ca772b6021f1d4f5ffe074c4e8ffc90907dd2b2`).

## 모드·격자·좌표

<a id="xh021"></a>
<a id="xh075"></a>
### D-001 — XH021, XH075

**판정:** 판본 한정 사실로 채택; 문서 모순 보존; 고정 소스 snapshot의 구현 판정 별도 적용.

- Grid arrays require (nx+1)×(ny+1) entries and positive-up bathymetry is documented as posdwn=-1, but the example uses posdwn=0.
- Input arrays have size '(nx+1)×(ny+1)', bathymetry defaults positive downward, and the table specifies 'posdwn=−1' for positive-up bathymetry.

**고정 소스 snapshot 판정:**

- [[#source-adjudication-posdwn|`posdwn` 구현 판정]]을 적용한다.

**출처 locator:**

- XH021: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.55, 56, printed page/frontmatter 53, 54, audit extract lines 994-1005,2148; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH075: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.53, 55, 56, 57, printed page/frontmatter 51, 53, 54, 55, audit extract lines 2859,2960-3064; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh022"></a>
### D-002 — XH022

**판정:** 문서 모순 보존; 고정 소스 snapshot의 구현 판정 별도 적용.

- The example uses negative underwater elevations with 'posdwn=0', while the table specifies '−1' for positive-up data.

**고정 소스 snapshot 판정:**

- [[#source-adjudication-posdwn|`posdwn` 구현 판정]]을 적용한다.

**출처 locator:**

- XH022: XBeach_manual_kingsday.docx, 원본 DOCX 문서순 block B546, B547, B616, B633 (SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`; audit extract lines 945-946,1008,2148); 직접 인용: “posdwn | Bathymetry is specified positive down (1) or positive up (-1) | 1.0 | -1.0 - 1.0 | -”; “-20.00 -20.00 -19.90 -19.80 -19.70 ... 14 14 15 15 15”; “posdwn       = 0”. PDF page는 주장하지 않음. 불완전한 PDF 정렬은 citation에서 폐기함.
<a id="xh112"></a>
<a id="xh147"></a>
### D-003 — XH112, XH147

**판정:** 문서 모순 보존; 고정 소스 snapshot의 구현 판정 별도 적용.

- The examples and tables disagree on the upward-positive posdwn value and the angular reference axis, while Tm01switch defaults to 0 here versus 1 in Kingsday's prose.
- The negative-depth example sets posdwn=0 although the parameter definition requires -1 for positive-up bathymetry.

**고정 소스 snapshot 판정:**

- [[#source-adjudication-posdwn|`posdwn` 구현 판정]]을 적용한다.
- [[#source-adjudication-dthetaS_XB|`dthetaS_XB` 구현 판정]]을 적용한다.

**출처 locator:**

- XH112: XBeach_manual_master.docx, 원본 DOCX 문서순 block B527, B589, B606 (SHA-256 `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236`; audit extract lines 940,998,2201); 직접 인용: “posdwn | Bathymetry is specified positive down (1) or positive up (-1) | 1.0 | -1.0 - 1.0 | -”; “-20.00 -20.00 -19.90 -19.80 -19.70 ... 14 14 15 15 15”; “posdwn       = 0”. PDF page는 주장하지 않음. 불완전한 PDF 정렬은 citation에서 폐기함.
- XH147: XBeach_manual_master.pdf, 직접 PDF, physical PDF p.54, 57, 61, 65, printed page/frontmatter 50, 53, 57, 61, audit extract lines 2904,3068,3159-3175,3361; 원본 SHA-256 `6e594e6fff7cf285c74c1877573061fed460f70658541cd29dd986475517c7f7`.
## 비정수압 검증 사례

<a id="xh198"></a>
### D-004 — XH198

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- The shoal setup says grid spacing was 'increased' from '0.025 m' to '0.004 m', an inconsistent numerical description that must be checked before reproducing the mesh.

**출처 locator:**

- XH198: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.47, printed page/frontmatter 37, audit extract lines 4157; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
## 비정수압 물리·수치법

<a id="xh011"></a>
### D-005 — XH011

**판정:** 역사 판본·매개변수 드리프트로 종결; 현재 동작으로 일반화 금지.

- The pressure section instructs 'waveform=nonh', but the tables enable non-hydrostatic pressure with 'nonh' and restrict waveform to 'ruessink_vanrijn' or 'vanthiel'.

**출처 locator:**

- XH011: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.30, 113, 114, printed page/frontmatter 28, 111, 112, audit extract lines 524,2125,2626; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
<a id="xh101"></a>
### D-006 — XH101

**판정:** 역사 판본·매개변수 드리프트로 종결; 현재 동작으로 일반화 금지.

- The non-hydrostatic section says waveform=nonh and swave=0, despite wavemodel=nonh elsewhere and a waveform table allowing only ruessink_vanrijn or vanthiel.

**출처 locator:**

- XH101: XBeach_manual_master.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.30, printed page/frontmatter 26, audit extract lines 520,2182,2618; 원본 SHA-256 `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236`.
<a id="xh176"></a>
<a id="xh200"></a>
### D-007 — XH176, XH200

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- The program description says wave_timestep is disabled automatically for non-hydrostatic computations, whereas the usage section instructs users to disable it manually or supply zero short-wave energy.
- The program-structure section says wave_timestep is disabled for non-hydrostatic calculations, while the usage section asks users to disable it manually or supply zero short-wave energy.

**출처 locator:**

- XH176: non-hydrostatic_report_draft.doc, DOC/DOCX→동일 work PDF 정렬, physical PDF p.50, 51, 53, printed page/frontmatter 40, 41, 43, audit extract lines 1851,1870-1871; 원본 SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`.
- XH200: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.50, 51, 53, printed page/frontmatter 40, 41, 43, audit extract lines 4213-4217,4285; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
<a id="xh177"></a>
<a id="xh203"></a>
### D-008 — XH177, XH203

**판정:** 역사 판본·매개변수 드리프트로 종결; 현재 동작으로 일반화 금지.

- The draft recommends the direct Thomas solver 'solver=2' for one-dimensional 'ny=2' and SIP 'solver=1' for 'ny>2', unlike the later manuals' ny=0 one-dimensional convention.
- The draft uses nonh=1, instat=3 or 8, front=4 with arc=1, ny=2 for 1D, and numeric solver=1/2 rather than the later manuals' named wave-boundary and solver options and ny=0 convention.

**출처 locator:**

- XH177: non-hydrostatic_report_draft.doc 원본 OLE DOC text extract lines 1870-1898 (DOC SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`; extract SHA-256 `54f1444c6f52371894f49ed6e1367ef86fedcbd2acaa7cef694a76f25b7dd9db`); 직접 인용: L1898 “For one dimensional simulations (ny=2) the use of the tri-diagonal solver is recommended (set solver=2). This solver is substantially faster than the SIP solver …”; L1895 “To enable this formulation the user should first set front = 4 and activate the reflection compensation by setting arc = 1 (note that …”; L1883 “In principle any of the non-reflective formulations (e.g set front to 0,1 or 4) can be used with the non-hydrostatic model, but experience has …”; 대응 printed section 43, 44. 불완전한 PDF 정렬은 citation에서 폐기하며 DOC 또는 PDF physical page를 주장하지 않음.
- XH203: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.54, 63, printed page/frontmatter 44, 53, audit extract lines 4307,4827; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
<a id="xh179"></a>
<a id="xh204"></a>
### D-009 — XH179, XH204

**판정:** 문서 모순 보존; 고정 소스 snapshot의 구현 판정 별도 적용.

- The procedure descriptions say corrections are 'Not called when sec_order=1', contradicting the recommendation and parameter table that 'secorder=1' enables them and also changing the keyword spelling.
- Procedure descriptions say second-order corrections are 'Not called when sec_order=1', contradicting the documented enabling value secorder=1 and introducing an underscore spelling drift.

**고정 소스 snapshot 판정:**

- [[#source-adjudication-secorder|`secorder` 구현 판정]]을 적용한다.

**출처 locator:**

- XH179: non-hydrostatic_report_draft.doc, DOC/DOCX→동일 work PDF 정렬, physical PDF p.59, 63, printed page/frontmatter 49, 53, audit extract lines 2039,2048,2067,2196-2199; 원본 SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`.
- XH204: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.54, 59, 63, printed page/frontmatter 44, 49, 53, audit extract lines 4305,4711-4731,4823; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
<a id="xh180"></a>
<a id="xh191"></a>
### D-010 — XH180, XH191

**판정:** 역사 판본·매개변수 드리프트로 종결; 현재 동작으로 일반화 금지.

- The five-point pressure system uses SIP with default 'solver=1', 'solver_urelax=0.92', 'solver_acc=0.005' and 'solver_maxit=20', accepting the final iterate at the cap, whereas later manuals document a cap of 30.
- Defaults are dispc=1, Topt=10 s when dispc<0, nonh=0, smag=0, secorder=0, kdmin=0, solver=1, solver_acc=0.005 and solver_maxit=20, with the iteration cap differing from the later manuals' 30.

**출처 locator:**

- XH180: non-hydrostatic_report_draft.doc, DOC/DOCX→동일 work PDF 정렬, physical PDF p.62, 63, printed page/frontmatter 52, 53, audit extract lines 2177-2230; 원본 SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`.
- XH191: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.31, 32, 63, printed page/frontmatter 21, 22, 53, audit extract lines 2967-2995,4826-4829; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
## 빌드·MPI·버전 범위

<a id="xh025"></a>
### D-011 — XH025

**판정:** 변환 손상값을 사실 승격에서 제외; 경고만 보존.

깨진 식·수치 자체는 canonical 사실로 사용하지 않는다. 아래 문장에는 제외 이유와 문서가 보여 주는 손상 범위만 남긴다.

- The variance-density example declares 15 frequencies and 13 directions but presents 16 density rows with only 12 values in most rows, so it is not a trustworthy input template.

**출처 locator:**

- XH025: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.67, 68, printed page/frontmatter 65, 66, audit extract lines 1164-1209; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
<a id="xh036"></a>
<a id="xh083"></a>
### D-012 — XH036, XH083

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- The overview claims single-precision NetCDF output, while later sections describe default Fortran output and double-precision fields.
- Release notes announce single-precision NetCDF output by default, while the parameter table defaults to 'fortran' and the NetCDF example declares double-precision physical fields.

**출처 locator:**

- XH036: XBeach_manual_kingsday.docx, 원본 DOCX 문서순 block B172, B173, B1581, B1582, B1583, B1584, B1585, B1586, B1587, B1588, B1589, B1590, B1219 (SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`; audit extract lines 197-198,1572-1581,2323); 직접 인용: “outputformat+ | Output file format | fortran | fortran, netcdf, debug”; “Default outputformat NetCDF”; “Output is single precision”. PDF page는 주장하지 않음. 불완전한 PDF 정렬은 citation에서 폐기함.
- XH083: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.9, 87, 100, printed page/frontmatter 7, 85, 98, audit extract lines 284-285,4184-4186,4844; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh094"></a>
<a id="xh128"></a>
### D-013 — XH094, XH128

**판정:** 역사 판본·매개변수 드리프트로 종결; 현재 동작으로 일반화 금지.

- The document retains release 1.22 revision 4567 while replacing the Kingsday manual's instat interface with wavemodel and wbctype, so the release label alone does not identify the documented parameter interface.
- Although still labeled version 1.22 revision 4567, this edition replaces Kingsday instat selection with wavemodel and wbctype while retaining the older nonh process switch.

**출처 locator:**

- XH094: XBeach_manual_master.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.9, 11, 12, printed page/frontmatter 5, 7, 8, audit extract lines 169,186-188,197,2182,2231; 원본 SHA-256 `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236`.
- XH128: XBeach_manual_master.pdf, 직접 PDF, physical PDF p.9, 10, 11, 12, printed page/frontmatter 5, 6, 7, 8, audit extract lines 258-300; 원본 SHA-256 `6e594e6fff7cf285c74c1877573061fed460f70658541cd29dd986475517c7f7`.
<a id="xh108"></a>
### D-014 — XH108

**판정:** 역사 판본·매개변수 드리프트로 종결; 현재 동작으로 일반화 금지.

- Wave entry remains seaward-only and abs1d is restricted to 1D, but cyclic=1 is now said to work across MPI domains, relaxing Kingsday's single-domain restriction.

**출처 locator:**

- XH108: XBeach_manual_master.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.47, 48, 49, 50, 52, printed page/frontmatter 43, 44, 45, 46, 48, audit extract lines 832,865,874-876,911; 원본 SHA-256 `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236`.
<a id="xh152"></a>
### D-015 — XH152

**판정:** 역사 판본·매개변수 드리프트로 종결; 현재 동작으로 일반화 금지.

- The output default is Fortran rather than the Kingsday overview's NetCDF, the tintm default expression is malformed, and this edition specifies double-precision NetCDF fields.

**출처 locator:**

- XH152: XBeach_manual_master.pdf, 직접 PDF, physical PDF p.84, 93, 96, printed page/frontmatter 80, 89, 92, audit extract lines 4027,4055-4057,4595,4657; 원본 SHA-256 `6e594e6fff7cf285c74c1877573061fed460f70658541cd29dd986475517c7f7`.
<a id="xh161"></a>
<a id="xh184"></a>
### D-016 — XH161, XH184

**판정:** 역사 판본·매개변수 드리프트로 종결; 현재 동작으로 일반화 금지.

- Breaking is represented as a bore without an empirical maximum-steepness parameter, unlike the later manuals' non-hydrostatic breaking thresholds, and the draft reports underestimated dissipation and excessive high-frequency energy.
- The draft describes a single-layer model that captures breaking without a separate breaking model or maximum-steepness parameter, whereas the later manuals document empirical non-hydrostatic breaking thresholds.

**출처 locator:**

- XH161: non-hydrostatic_report_draft.doc 원본 OLE DOC text extract lines 12,326,676-689 (DOC SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`; extract SHA-256 `54f1444c6f52371894f49ed6e1367ef86fedcbd2acaa7cef694a76f25b7dd9db`); 직접 인용: L326 “The absence of a separate breaking model was the main motivation to choose to implement the non-hydrostatic model into XBeach. However, because XBeach is …”; L681 “where the authors show that their non-hydrostatic model is capable of predicting the breakpoint accurately using a conservative scheme for mass and momentum. The …”; L682 “This stands in contrast to the Boussinesq models that have been equally successful in modelling waves before breaking. In Boussinesq models the dispersive effects …”; 대응 printed section frontmatter-physical-3, 1, 2, 8, 9. 불완전한 PDF 정렬은 citation에서 폐기하며 DOC 또는 PDF physical page를 주장하지 않음.
- XH184: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.18, 19, printed page/frontmatter 8, 9, audit extract lines 686-704; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
<a id="xh175"></a>
<a id="xh199"></a>
### D-017 — XH175, XH199

**판정:** 역사 판본·매개변수 드리프트로 종결; 현재 동작으로 일반화 금지; 2010 초안의 사실·한계로 채택.

- MPI builds explicitly disable non-hydrostatic, second-order and Smagorinsky routines regardless of their runtime switches, whose documented defaults are all '0'.
- MPI compilation disables non-hydrostatic, second-order and Smagorinsky corrections irrespective of their switches in this draft, an edition-specific restriction that must not be generalized to later manuals.

**출처 locator:**

- XH175: non-hydrostatic_report_draft.doc, DOC/DOCX→동일 work PDF 정렬, physical PDF p.50, 53, 62, 63, printed page/frontmatter 40, 43, 52, 53, audit extract lines 1843,1872,2174,2187,2197; 원본 SHA-256 `07428e686eb4d2211448dcae7b7f77cdae8281affa020f68dacf42df19aa19ec`.
- XH199: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.50, 53, 62, 63, printed page/frontmatter 40, 43, 52, 53, audit extract lines 4203,4287,4806,4816,4823; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
<a id="xh201"></a>
### D-018 — XH201

**판정:** 역사 판본·매개변수 드리프트로 종결; 현재 동작으로 일반화 금지.

- This draft enables non-hydrostatic mode with 'nonh=1' and restricts forcing to 'instat=3' or 'instat=8', predating the later manual's wavemodel/wbctype interface.

**출처 locator:**

- XH201: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.53, 54, printed page/frontmatter 43, 44, audit extract lines 4283,4291-4301; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
## 식생·선박

<a id="xh033"></a>
<a id="xh082"></a>
### D-019 — XH033, XH082

**판정:** 해당 판본이 밝힌 미구현·적용 한계로 종결.

- Ship compute_motion is stated to be unimplemented although the example sets compute_motion=1, and the documented array dimensions disagree with indexing through nx+1.
- Ships must remain within the domain and moving-ship forces may be unreliable, while 'compute_motion' is explicitly unimplemented despite the example setting it to '1'.

**출처 locator:**

- XH033: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.85, 86, printed page/frontmatter 83, 84, audit extract lines 1406-1408,1424; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH082: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.85, 86, printed page/frontmatter 83, 84, audit extract lines 4088-4110; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh034"></a>
### D-020 — XH034

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- Ship geometry is specified as '(nx+1)×(ny+1)', but its zero-based example runs through 'nx+1' and 'ny+1', implying one extra row and column.

**출처 locator:**

- XH034: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.85, 86, printed page/frontmatter 83, 84, audit extract lines 1405,1425-1430; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
<a id="xh116"></a>
<a id="xh151"></a>
### D-021 — XH116, XH151

**판정:** 해당 판본이 밝힌 미구현·적용 한계로 종결.

- Ship input gives inconsistent grid extents, prohibits boundary intersection, and documents compute_motion=1 despite stating that motion computation is unimplemented and moving-ship forces are unreliable.
- compute_motion is unimplemented despite an example value of 1, moving-ship forces are called unreliable, and the ship-grid example indexes 0 through nx+1 despite stated nx+1 dimensions.

**출처 locator:**

- XH116: XBeach_manual_master.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.81, 82, printed page/frontmatter 77, 78, audit extract lines 1371-1396; 원본 SHA-256 `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236`.
- XH151: XBeach_manual_master.pdf, 직접 PDF, physical PDF p.81, 82, 83, printed page/frontmatter 77, 78, 79, audit extract lines 3920-3967; 원본 SHA-256 `6e594e6fff7cf285c74c1877573061fed460f70658541cd29dd986475517c7f7`.
## 지형변화·지층·avalanching

<a id="xh017"></a>
<a id="xh071"></a>
### D-022 — XH017, XH071

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- The conceptual description permits the breathing layer at the top or bottom, while setup requires at least three layers and the ndvar table has a minimum of 2.
- The bed-composition description permits the breathing layer to be the top or bottom layer, whereas the input discussion requires all three layer classes and the table restricts 'nd_var' to '2–nd'.

**출처 locator:**

- XH017: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.43, 44, 78, 116, printed page/frontmatter 41, 42, 76, 114, audit extract lines 816,1308,2281,2635; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH071: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.43, 44, 78, 116, printed page/frontmatter 41, 42, 76, 114, audit extract lines 2672-2674,3815,5333; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh070"></a>
### D-023 — XH070

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- The prose calls morstart and morstop hydrodynamic times, whereas their table labels them morphological times.

**출처 locator:**

- XH070: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.80, 81, printed page/frontmatter 78, 79, audit extract lines 3895,3927-3935; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh095"></a>
<a id="xh129"></a>
### D-024 — XH095, XH129

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- The general claim that all times are morphological conflicts with the statement that dtbc is unaffected by morphological acceleration.
- The blanket claim that all input times are divided by morfac conflicts with dtbc=1 s being explicitly unaffected by morfac.

**출처 locator:**

- XH095: XBeach_manual_master.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.11, printed page/frontmatter 7, audit extract lines 190,2228; 원본 SHA-256 `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236`.
- XH129: XBeach_manual_master.pdf, 직접 PDF, physical PDF p.11, 61, printed page/frontmatter 7, 57, audit extract lines 291,3171-3173; 원본 SHA-256 `6e594e6fff7cf285c74c1877573061fed460f70658541cd29dd986475517c7f7`.
<a id="xh106"></a>
<a id="xh156"></a>
### D-025 — XH106, XH156

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- morstart and morstop are described as hydrodynamic times in prose but morphological times in their entries, with defaults 120 and 2000, and setbathy overrides depfile when morphology is disabled.
- morstart=120 s and morstop=2000 s are labeled morphological times in the table but hydrodynamic times in the prose.

**출처 locator:**

- XH106: XBeach_manual_master.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.116, printed page/frontmatter 112, audit extract lines 1741,2635-2636; 원본 SHA-256 `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236`.
- XH156: XBeach_manual_master.pdf, 직접 PDF, physical PDF p.116, 117, 118, printed page/frontmatter 112, 113, 114, audit extract lines 5354-5431; 원본 SHA-256 `6e594e6fff7cf285c74c1877573061fed460f70658541cd29dd986475517c7f7`.
<a id="xh107"></a>
<a id="xh143"></a>
### D-026 — XH107, XH143

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함; 역사 판본·매개변수 드리프트로 종결; 현재 동작으로 일반화 금지.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- The breathing-layer scheme requires at least three layers and documents frac_dz=0.7, merge=0.01, nd_var=2 and split=1.01, with nd_var replacing Kingsday's ndvar spelling.
- The breathing layer may supposedly occupy the uppermost layer, but setup requires at least three layer types and nd_var has minimum index 2.

**출처 locator:**

- XH107: XBeach_manual_master.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.44, 76, printed page/frontmatter 40, 72, audit extract lines 812,1280,2643; 원본 SHA-256 `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236`.
- XH143: XBeach_manual_master.pdf, 직접 PDF, physical PDF p.44, 76, 118, 119, printed page/frontmatter 40, 72, 114, 115, audit extract lines 2712,3717,5436-5462; 원본 SHA-256 `6e594e6fff7cf285c74c1877573061fed460f70658541cd29dd986475517c7f7`.
## 출력

<a id="xh035"></a>
<a id="xh084"></a>
### D-027 — XH035, XH084

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- The extracted tintm default is a collapsed tstop/tstart expression in the table, whereas the later output description says mean and point intervals inherit tintg.
- Output prose uses 'tspoint' instead of table/example 'tspoints' and says missing tintm inherits tintg, while the table defaults tintm to 'tstop−tstart'.

**출처 locator:**

- XH035: XBeach_manual_kingsday.docx, 원본 DOCX 문서순 block B1509, B1517, B538, B1519, B1520, B1224, B1225, B1226, B1227, B1228, B1229 (SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`; audit extract lines 1500,1508-1511,2328-2333); 직접 인용: “… keywords for the interval of time-averaged spatial output and point output are tintm and tintp respectively, where tintp is used both for fixed point …”; “tintm | Interval time of mean, var, max, min output | tstop- tstart | 1 – [tstop – start] | s”; “… instantaneous spatial output using the tsglobal keyword. The keywords for time series files for time-averaged spatial output and point output are tsmean and tspoint …”. PDF page는 주장하지 않음.
- XH084: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.88, 97, printed page/frontmatter 86, 95, audit extract lines 4216,4787; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh073"></a>
### D-028 — XH073

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- Tide-corner ordering differs between prose and output tables, tideloc=1 is described both as all corners and offshore only, tideloc=3 appears only in the table, and paulrevere changes from numeric 0/1 to land/sea.

**출처 locator:**

- XH073: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.50, 73, 74, 94, printed page/frontmatter 48, 71, 72, 92, audit extract lines 2808,3601-3628,4689-4726; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh117"></a>
### D-029 — XH117

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- The output prose makes unspecified tintm inherit tintg=1 s, whereas the table defaults tintm to tstop-tstart.

**출처 locator:**

- XH117: XBeach_manual_master.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.93, printed page/frontmatter 89, audit extract lines 1465,2351; 원본 SHA-256 `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236`.
## 파동작용·쇄파·롤러·단파 마찰

<a id="xh003"></a>
<a id="xh053"></a>
### D-030 — XH003, XH053

**판정:** 문서 모순 보존; 고정 소스 snapshot의 구현 판정 별도 적용.

- The physics prose says wci=1 disables wave-current interaction, whereas the parameter table gives wci=0 as the default disabling switch.
- The prose associates 'wci=1' with no wave-current interaction, whereas the parameter table describes wci as enabling interaction and gives default '0'.

**고정 소스 snapshot 판정:**

- [[#source-adjudication-wci|`wci` 구현 판정]]을 적용한다.

**출처 locator:**

- XH003: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.18, 109, printed page/frontmatter 16, 107, audit extract lines 284,2588; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH053: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.18, 109, printed page/frontmatter 16, 107, audit extract lines 470,5085-5087; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh097"></a>
<a id="xh131"></a>
### D-031 — XH097, XH131

**판정:** 문서 모순 보존; 고정 소스 snapshot의 구현 판정 별도 적용.

- The physics text associates wci=1 with no wave-current interaction, whereas the parameter table describes switching interaction on and gives default wci=0.
- The wave-action prose associates wci=1 with no interaction, whereas the exercise and parameter table associate it with enabled interaction.

**고정 소스 snapshot 판정:**

- [[#source-adjudication-wci|`wci` 구현 판정]]을 적용한다.

**출처 locator:**

- XH097: XBeach_manual_master.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.17, 106, printed page/frontmatter 13, 102, audit extract lines 252,1706,2571; 원본 SHA-256 `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236`.
- XH131: XBeach_manual_master.pdf, 직접 PDF, physical PDF p.17, 106, 109, printed page/frontmatter 13, 102, 105, audit extract lines 446,4937,5068-5070; 원본 SHA-256 `6e594e6fff7cf285c74c1877573061fed460f70658541cd29dd986475517c7f7`.
## 파랑 경계·스펙트럼

<a id="xh023"></a>
### D-032 — XH023

**판정:** 문서 모순 보존; 고정 소스 snapshot의 구현 판정 별도 적용.

- The prose defines dthetaS_XB as rotation from SWAN to the XBeach x-axis, whereas the parameter table defines rotation to the east-pointing axis.

**고정 소스 snapshot 판정:**

- [[#source-adjudication-dthetaS_XB|`dthetaS_XB` 구현 판정]]을 적용한다.

**출처 locator:**

- XH023: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.65, printed page/frontmatter 63, audit extract lines 1060,2179; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
<a id="xh024"></a>
<a id="xh078"></a>
### D-033 — XH024, XH078

**판정:** 판본 한정 사실로 채택; 문서 모순 보존; 고정 소스 snapshot의 구현 판정 별도 적용.

- dthetaS_XB is described relative to East in one place and model x in another, while vardens uses Cartesian directions 0° along +x and 90° along +y.
- Variance-density directions must increase and use the XBeach Cartesian frame, with '0°' along +x and '90°' along +y.

**고정 소스 snapshot 판정:**

- [[#source-adjudication-dthetaS_XB|`dthetaS_XB` 구현 판정]]을 적용한다.

**출처 locator:**

- XH024: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.67, printed page/frontmatter 65, audit extract lines 1161; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH078: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.61, 65, 67, printed page/frontmatter 59, 63, 65, audit extract lines 3170,3357,3386; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh026"></a>
<a id="xh079"></a>
### D-034 — XH026, XH079

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- The ts_nonh column requirements differ between the boundary description and input section, particularly for transverse and vertical velocities.
- The ts_nonh prose alternately describes optional vertical velocity and elevation or required horizontal u/v velocities and elevation, while the detached format lists 't,U,Zs,W'.

**출처 locator:**

- XH026: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.47, 69, printed page/frontmatter 45, 67, audit extract lines 857,1225,2206-2208; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH079: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.47, 69, 70, printed page/frontmatter 45, 67, 68, audit extract lines 2735,3469-3473; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh109"></a>
<a id="xh144"></a>
### D-035 — XH109, XH144

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- The ts_nonh descriptions disagree on whether vertical velocity is optional and on the column ordering, while separate bichromatic frequencies remain a future capability.
- ts_nonh requirements alternate between optional vertical velocity/surface elevation, mandatory u/v velocities and a t,U,Zs,W variable list.

**출처 locator:**

- XH109: XBeach_manual_master.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.48, 69, printed page/frontmatter 44, 65, audit extract lines 853,1206,2259-2261; 원본 SHA-256 `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236`.
- XH144: XBeach_manual_master.pdf, 직접 PDF, physical PDF p.48, 69, 70, printed page/frontmatter 44, 65, 66, audit extract lines 2777,3472-3484; 원본 SHA-256 `6e594e6fff7cf285c74c1877573061fed460f70658541cd29dd986475517c7f7`.
<a id="xh113"></a>
### D-036 — XH113

**판정:** 문서 모순 보존; 고정 소스 snapshot의 구현 판정 별도 적용.

- dthetaS_XB rotates SWAN x into model x in the prose but into East in the table.

**고정 소스 snapshot 판정:**

- [[#source-adjudication-dthetaS_XB|`dthetaS_XB` 구현 판정]]을 적용한다.

**출처 locator:**

- XH113: XBeach_manual_master.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.64, 65, printed page/frontmatter 60, 61, audit extract lines 1043,2229; 원본 SHA-256 `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236`.
## 표사이동

<a id="xh012"></a>
<a id="xh066"></a>
### D-037 — XH012, XH066

**판정:** 판본 한정 사실로 채택; 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- At the stated T=20°C and ν=10^-6 m²/s, extracted critical-velocity branches show D50≤0.0005 m versus D50>0.05 m and overlapping current-threshold intervals, so their applicability bounds need source verification.
- Sediment calculations assume '20 degrees Celsius' and constant kinematic viscosity '10⁻6 m²/s'.

**출처 locator:**

- XH012: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.38, printed page/frontmatter 36, audit extract lines 703; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH066: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.38, 39, printed page/frontmatter 36, 37, audit extract lines 2120,2138-2164,2277-2310; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh013"></a>
<a id="xh067"></a>
### D-038 — XH013, XH067

**판정:** 문서 모순 보존; 고정 소스 snapshot의 구현 판정 별도 적용.

- The dilatancy prose says critical Shields stress is reduced while describing inhibited erosion, and the accompanying positive correction uses rheeA=0.75 for continuum motion or 1.7 otherwise with pormax=0.5.
- Dilatancy is said to hinder erosion by reducing the critical Shields number, a direction requiring verification, with 'rheeA=0.75' by default versus approximately '1.7' for a continuum and 'pormax=0.5'.

**고정 소스 snapshot 판정:**

- [[#source-adjudication-dilatancy|`dilatancy` 구현 판정]]을 적용한다.

**출처 locator:**

- XH013: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.40, 112, 113, printed page/frontmatter 38, 110, 111, audit extract lines 747-751,2607,2618-2620; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH067: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.40, 113, printed page/frontmatter 38, 111, audit extract lines 2368-2422,5230-5240; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh014"></a>
<a id="xh068"></a>
### D-039 — XH014, XH068

**판정:** 역사 판본·매개변수 드리프트로 종결; 현재 동작으로 일반화 금지.

- The slope correction gives facsl=1.6 but repeats soulsby_total where the two transport-specific slope options should be distinguished.
- The slope correction defaults to 'facsl=1.6' and 'bdslpeffmag=roelvink_total', but the prose repeats 'soulsby_total' for bed-only transport where the table lists 'soulsby_bed'.

**출처 locator:**

- XH014: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.41, 111, 112, printed page/frontmatter 39, 109, 110, audit extract lines 772-776,2603,2611; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH068: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.41, printed page/frontmatter 39, audit extract lines 2464-2480; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh103"></a>
<a id="xh141"></a>
### D-040 — XH103, XH141

**판정:** 문서 모순 보존; 고정 소스 snapshot의 구현 판정 별도 적용.

- The text assumes T=20 and nu=1e-6, defines ua=(fSk*Sk-fAs*As)*urms, and assigns dilatancy A=0.75 to a single particle and A=1.7 to a continuum, reversing the Kingsday assignments.
- The sediment calculation fixes T=20°C and ν=10^-6 m²/s, while dilatancy still claims to reduce critical Shields stress and assigns A=0.75 to individual particles and 1.7 to a continuum, reversing the Kingsday assignment.

**고정 소스 snapshot 판정:**

- [[#source-adjudication-dilatancy|`dilatancy` 구현 판정]]을 적용한다.

**출처 locator:**

- XH103: XBeach_manual_master.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.38, 40, 41, printed page/frontmatter 34, 36, 37, audit extract lines 697,741-745; 원본 SHA-256 `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236`.
- XH141: XBeach_manual_master.pdf, 직접 PDF, physical PDF p.38, 40, 41, printed page/frontmatter 34, 36, 37, audit extract lines 2162,2406-2447; 원본 SHA-256 `6e594e6fff7cf285c74c1877573061fed460f70658541cd29dd986475517c7f7`.
<a id="xh104"></a>
### D-041 — XH104

**판정:** 역사 판본·매개변수 드리프트로 종결; 현재 동작으로 일반화 금지.

- The slope-effect prose repeats soulsby_total for bed-only transport although the table explicitly provides soulsby_bed.

**출처 locator:**

- XH104: XBeach_manual_master.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.41, printed page/frontmatter 37, audit extract lines 772,2594; 원본 SHA-256 `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236`.
<a id="xh140"></a>
### D-042 — XH140

**판정:** 변환 손상값을 사실 승격에서 제외; 경고만 보존.

깨진 식·수치 자체는 canonical 사실로 사용하지 않는다. 아래 문장에는 제외 이유와 문서가 보여 주는 손상 범위만 남긴다.

- The critical-velocity branches include D50<=0.0005 versus D50>0.05 and overlapping D50 limits in the later formulation, leaving gaps or overlaps that must be checked against the original.

**출처 locator:**

- XH140: XBeach_manual_master.pdf, 직접 PDF, physical PDF p.38, 39, 40, printed page/frontmatter 34, 35, 36, audit extract lines 2118-2378; 원본 SHA-256 `6e594e6fff7cf285c74c1877573061fed460f70658541cd29dd986475517c7f7`.
## 혼합 매개변수 기본값·입력 규약

<a id="xh004"></a>
<a id="xh054"></a>
### D-043 — XH004, XH054

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- The physics prose calls Tm01switch=1 the default, but the parameter table gives 0.
- The prose calls 'Tm01switch=1' the default representative-period convention, but the parameter table gives 'Tm01switch=0', corresponding to Tm−1,0.

**출처 locator:**

- XH004: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.20, 36, printed page/frontmatter 18, 34, audit extract lines 318,664,2175,2200; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH054: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.20, 36, 61, printed page/frontmatter 18, 34, 59, audit extract lines 613,1962,3152-3154; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh030"></a>
### D-044 — XH030

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- The early four-corner ordering is offshore-left, backshore-left, backshore-right, offshore-right, whereas the later explicit ordering is '(1,1),(1,N),(N,N),(N,1)'.

**출처 locator:**

- XH030: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.50, 74, 94, printed page/frontmatter 48, 72, 92, audit extract lines 904,1271,2552-2555; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
<a id="xh063"></a>
### D-045 — XH063

**판정:** 문서 모순 보존; 고정 소스 snapshot의 구현 판정 별도 적용.

- The adaptation-time equation uses Ts=max(fTs h/ws,Tsmin), whereas the parameter description prints Ts=tsfac+h/ws, an operator discrepancy requiring original-page verification.

**고정 소스 snapshot 판정:**

- [[#source-adjudication-adaptation-time|`adaptation-time` 구현 판정]]을 적용한다.

**출처 locator:**

- XH063: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.35, 36, 113, printed page/frontmatter 33, 34, 111, audit extract lines 1894-1920,5250; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh114"></a>
### D-046 — XH114

**판정:** 변환 손상값을 사실 승격에서 제외; 경고만 보존.

깨진 식·수치 자체는 canonical 사실로 사용하지 않는다. 아래 문장에는 제외 이유와 문서가 보여 주는 손상 범위만 남긴다.

- The vardens example declares 15 frequencies and 13 directions but supplies 16 matrix rows with 12 values each.

**출처 locator:**

- XH114: XBeach_manual_master.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.67, 68, printed page/frontmatter 63, 64, audit extract lines 1147-1192; 원본 SHA-256 `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236`.
<a id="xh138"></a>
### D-047 — XH138

**판정:** 문서 모순 보존; 고정 소스 snapshot의 구현 판정 별도 적용.

- The adaptation-time formulation uses max(fTs*h/ws,Tsmin), but the parameter table prints tsfac+h/ws with default tsfac=0.1.

**고정 소스 snapshot 판정:**

- [[#source-adjudication-adaptation-time|`adaptation-time` 구현 판정]]을 적용한다.

**출처 locator:**

- XH138: XBeach_manual_master.pdf, 직접 PDF, physical PDF p.36, 114, printed page/frontmatter 32, 110, audit extract lines 1953-1963,5279; 원본 SHA-256 `6e594e6fff7cf285c74c1877573061fed460f70658541cd29dd986475517c7f7`.
<a id="xh207"></a>
### D-048 — XH207

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- The scalar example specifies velocity '0.010 m/s' at 't=2' but its explanation gives '0.020 m/s'.

**출처 locator:**

- XH207: non-hydrostatic_report_draft.pdf, 직접 PDF, physical PDF p.66, printed page/frontmatter 56, audit extract lines 4875-4878; 원본 SHA-256 `d170530492ec5f4052f450eec28f7965ae44ac10276248e24cad41b5f6e41005`.
## 흐름 마찰·점성

<a id="xh008"></a>
<a id="xh059"></a>
### D-049 — XH008, XH059

**판정:** 문서 모순 보존; 고정 소스 snapshot의 구현 판정 별도 적용.

- The Smagorinsky description treats nuh=0.1 as a dimensionless coefficient, whereas its parameter table assigns nuh units of m²/s.
- The prose identifies 'nuh=0.1' as the dimensionless Smagorinsky constant when 'smag=1', but the table labels the same input as background viscosity in m²/s.

**고정 소스 snapshot 판정:**

- [[#source-adjudication-nuh|`nuh` 구현 판정]]을 적용한다.

**출처 locator:**

- XH008: XBeach_manual_kingsday.docx, 원본 DOCX 문서순 block B303, B1002, B1008, B1009, B1010, B1011 (SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`; audit extract lines 480,1292,2264-2267); 직접 인용: “nuh | Horizontal background viscosity | 0.1 | 0.0 - 1.0 | m^2s^-1”; “… the roller dissipation tuned by nuhfac. In the alongshore direction the viscosity may be multiplied by a factor nuhv to account for additional advective …”; “… all model simulations. It is also possible to use a user-defined value for the horizontal viscosity by turning off the Smagorinsky model (keyword: smag …”. PDF page는 주장하지 않음. 불완전한 PDF 정렬은 citation에서 폐기함.
- XH059: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.27, 77, printed page/frontmatter 25, 75, audit extract lines 1373,3758-3772; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh009"></a>
<a id="xh060"></a>
### D-050 — XH009, XH060

**판정:** 문서 모순 보존; 고정 소스 snapshot의 구현 판정 별도 적용.

- The prose gives cf=0.003 and Chezy C=55 with cf=g/C², but the table pairs default bedfriction=chezy with bedfriccoef=0.003.
- The friction table pairs 'chezy' with '55 m½/s' and 'cf' with '0.003', but the input table defaults to 'bedfriction=chezy' and 'bedfriccoef=0.003'.

**고정 소스 snapshot 판정:**

- [[#source-adjudication-bedfriction|`bedfriction` 구현 판정]]을 적용한다.

**출처 locator:**

- XH009: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.28, 29, printed page/frontmatter 26, 27, audit extract lines 490-506,2113-2118,2261-2263; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH060: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.28, 29, 77, printed page/frontmatter 26, 27, 75, audit extract lines 1413-1482,3742-3754; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh100"></a>
<a id="xh135"></a>
### D-051 — XH100, XH135

**판정:** 문서 모순 보존; 고정 소스 snapshot의 구현 판정 별도 적용.

- The text gives Chezy C=55 and Manning n=0.02, while the default bedfriccoef is 0.01 rather than Kingsday's 0.003 and nuh=0.1 is described both as a coefficient and as a dimensional viscosity.
- Typical Chezy C=55, Manning n=0.02 and ks=0.01–0.15 m conflict with default chezy/bedfriccoef=0.01, changed from Kingsday 0.003, while nuh=0.1 is described both as a Smagorinsky constant and dimensional viscosity.

**고정 소스 snapshot 판정:**

- [[#source-adjudication-nuh|`nuh` 구현 판정]]을 적용한다.
- [[#source-adjudication-bedfriction|`bedfriction` 구현 판정]]을 적용한다.

**출처 locator:**

- XH100: XBeach_manual_master.docx, 원본 DOCX 문서순 block B284, B295, B296, B297, B1664, B1665, B1666, B1667, B1668, B1669, B1670 (SHA-256 `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236`; audit extract lines 476,486-494,2573-2579); 직접 인용: “… (n) must be specified. The dimensionless friction coefficient is calculated from . Manning can be seen as a depth-dependent Chézy value and a typical …”; “… The dimensionless friction coefficient is calculated from The White-Colebrook formulation has al log relation with the water depth and a typical ks value for …”; “The dimensionless friction coefficient can be calculated from the Chézy value with . A typical Chézy value for sandy coasts is in the order …”. PDF page는 주장하지 않음. 불완전한 PDF 정렬은 citation에서 폐기함.
- XH135: XBeach_manual_master.pdf, 직접 PDF, physical PDF p.28, 29, 110, printed page/frontmatter 24, 25, 106, audit extract lines 1439,1486-1542,5085-5099; 원본 SHA-256 `6e594e6fff7cf285c74c1877573061fed460f70658541cd29dd986475517c7f7`.
<a id="xh136"></a>
### D-052 — XH136

**판정:** 깨진 변환식 제외; 구현은 소스 snapshot으로 별도 판정.

깨진 식·수치 자체는 canonical 사실로 사용하지 않는다. 아래 문장에는 제외 이유와 문서가 보여 주는 손상 범위만 남긴다.

- The extracted friction formulas show cf=g/C and a Manning exponent of 1/12, differing from expected squared-C notation and Kingsday's 1/3 exponent, requiring verification against the original equations before use.

**고정 소스 snapshot 판정:**

- [[#source-adjudication-bedfriction|`bedfriction` 구현 판정]]을 적용한다.

**출처 locator:**

- XH136: XBeach_manual_master.pdf, 직접 PDF, physical PDF p.28, printed page/frontmatter 24, audit extract lines 1488-1498; 원본 SHA-256 `6e594e6fff7cf285c74c1877573061fed460f70658541cd29dd986475517c7f7`.
## 흐름·조석·유량 경계

<a id="xh028"></a>
### D-053 — XH028

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- The same paragraph says 'tideloc=1' applies the signal to all four corners and also says it applies only offshore with fixed zs0 landward.

**출처 locator:**

- XH028: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.73, printed page/frontmatter 71, audit extract lines 1269; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
<a id="xh029"></a>
### D-054 — XH029

**판정:** 역사 판본·매개변수 드리프트로 종결; 현재 동작으로 일반화 금지.

- Two-signal tidal forcing is first described as sea/land only, later selected by numeric 'paulrevere=0/1', and finally tabulated using string values 'land, sea' with default 'sea'.

**출처 locator:**

- XH029: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.50, 51, 73, 74, printed page/frontmatter 48, 49, 71, 72, audit extract lines 912,1270,2238; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
<a id="xh031"></a>
### D-055 — XH031

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- The prose explicitly excludes 'tideloc=3', but the parameter table includes 3 in its range.

**출처 locator:**

- XH031: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.73, printed page/frontmatter 71, audit extract lines 1269,2239; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
<a id="xh110"></a>
<a id="xh145"></a>
### D-056 — XH110, XH145

**판정:** 같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함.

동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.

- Tide descriptions disagree on corner order and tideloc=1 boundary coverage, the paulrevere default is land rather than Kingsday's sea, and cyclic boundaries are now described as available across MPI domains.
- Tide descriptions disagree on corner order and tideloc=1 landward forcing, retain numeric paulrevere=0/1 versus land/sea, and change its default from Kingsday sea to land.

**출처 locator:**

- XH110: XBeach_manual_master.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.51, 73, 74, printed page/frontmatter 47, 69, 70, audit extract lines 894-902,1250-1262,2292-2293; 원본 SHA-256 `9f142b89e0659e71066054c3d61b4d6f29ba3c10c5984e26e9a2d37d2fae3236`.
- XH145: XBeach_manual_master.pdf, 직접 PDF, physical PDF p.49, 50, 51, 52, 73, 74, printed page/frontmatter 45, 46, 47, 48, 69, 70, audit extract lines 2814-2866,3606-3634; 원본 SHA-256 `6e594e6fff7cf285c74c1877573061fed460f70658541cd29dd986475517c7f7`.
