---
title: "ROMS 자료동화 framework — NLM/TLM/ADM/RPM 4 모델과 hand-coded 수반의 의도된 transpose 관계 + I4D-Var/R4D-Var/RBL4D-Var driver + observation sensitivity/array modes. 타 모델 DA 비교"
topic: roms
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/source_code/roms/ROMS/ 직하위 파일 목록: Adjoint/의 .F 65개(ad_*.F 63개와 adsen_*.F 2개), Tangent/의 tl_*.F 54개, Representer/의 rp_*.F 39개. Drivers/의 i4dvar_roms.h·r4dvar_roms.h·rbl4dvar_roms.h·obs_sen_*·array_modes.h·picard_roms.h와 ad_step3d_t.F 헤더를 대조했다. 2026-10-14 ROMS recovery 대조 보고서를 반영했다." # [10-14 전수 검증 정정]
last_source_check: "2026-10-14 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-04
verification_by: "Claude Opus 4.8 (1M context) — NLM/TLM/ADM/RPM + 4dvar driver 구조"
verification_date: 2026-06-04
related:
  - models/ROMS/source-analysis/roms_4dvar.md
  - models/ROMS/source-analysis/roms_support_modules.md
  - models/ROMS/source-analysis/roms_baroclinic_3d.md
---

# ROMS 자료동화(DA) framework

> ROMS `Adjoint/` 직하위의 `.F` 파일은 65개이다. `Tangent/` 직하위의 `.F` 파일은 54개이다. `Representer/` 직하위의 `.F` 파일은 39개이다. 이 수는 현재 코드의 각 디렉터리 파일 목록에서 셌다. [roms_4dvar](roms_4dvar.md)는 변분 자료동화 알고리즘을 설명한다. 본 노트는 **4 모델(NLM/TLM/ADM/RPM)과 driver** 구조를 설명한다. [10-14 전수 검증 정정]

## 1. 4 모델과 hand-coded 수반의 의도된 transpose 관계

ROMS 의 주요 NL 커널은 **3종 대응물**을 가진다 — `Nonlinear/` **69** `.F` 에 대해 `Tangent/` 54 · `Adjoint/` 65 · `Representer/` 39 로, 대응은 전면적이 아니라 커널별이다(주 드라이버 `tl_main3d.F`·`ad_main3d.F`·`rp_main3d.F` 는 모두 존재):

| 모델 | prefix | 역할 |
|---|---|---|
| **NLM** Nonlinear | (none) | 정방향 예보([roms_baroclinic_3d](roms_baroclinic_3d.md) step3d_t/step3d_uv 등) |
| **TLM** Tangent Linear | `tl_` | NLM 의 선형화(perturbation 전파). `Tangent/tl_step3d_t.F` 등 |
| **ADM** Adjoint | `ad_` | hand-coded 수반의 의도된 transpose 관계. [DA1-824](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md) |
| **RPM** Representer | `rp_` | dual-space(관측공간) finite-amplitude TLM. `Representer/` |

- 대응 커널 예: `ad_step2d`/`ad_step3d_t`/`ad_step3d_uv`/`ad_prsgrd`/`ad_rho_eos`/`ad_uv3dmix`… (NL의 prsgrd·rho_eos·advection을 손으로 adjoint coding). ad_main2d/3d = adjoint 시간역행 driver.
- hand-coded 수반은 TLM과 의도된 transpose 관계를 갖는다. ([DA1-824](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md))
- `ROMS/Adjoint/ad_main3d.F:266`의 원문은 `STEP_LOOP : DO istep=Nsteps,1,-1`이다. ([DA1-824](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md))

현재 AD/TL/RP 생물 dispatcher의 실행 include는 `NPZD_FRANKS`, `NPZD_IRON`, `NPZD_POWELL`이다. Fennel과 NEMURO의 include는 `!!`로 주석 처리했다. EcoSim, ECB, hypoxia_srm, red_tide 선택 분기도 없다. 수반 기반 입력 키워드가 존재한다는 사실과 해당 생물 모델의 수반 커널 지원을 구분한다. ([biology:CD-003](../../../_staging/recovery/compare/roms-biology-vs-code.md))

## 2. 변분 driver (Drivers/) — 3 방법

| driver | 방식 | space |
|---|---|---|
| **I4D-Var** (`i4dvar_roms.h`) | incremental 4D-Var(Courtier) | **primal**(model space, B-precond) |
| **R4D-Var** (`r4dvar_roms.h`) | **representer**(indirect) | **dual**(obs space) |
| **RBL4D-Var** (`rbl4dvar_roms.h`) | Restricted B-preconditioned Lanczos | **dual** |

- **inner loop**는 TLM/ADM과 CG/Lanczos로 이차 비용함수를 최소화한다 ([자료동화 호출 흐름](../../../_staging/recovery/flow/ROMS-callflow-da.md) §2). [roms_4dvar](roms_4dvar.md)의 Dirac Delta 시험은 별도의 상관모델 드라이버에 있다 (`ROMS/Drivers/correlation.h:427–448`). [10-14 전수 검증 정정]
- I4와 RBL은 비선형 기본 상태를 갱신한다. ([callflow-da:RF2-020](../../../_staging/recovery/flow/ROMS-callflow-da.md))
- R4는 첫 외부 반복에서 NLM 궤적을 사용한다. ([callflow-da:RF2-020](../../../_staging/recovery/flow/ROMS-callflow-da.md))
- R4는 이후 외부 반복에서 직전 분석 RPM 궤적을 사용한다. ([callflow-da:RF2-020](../../../_staging/recovery/flow/ROMS-callflow-da.md))
- `split_i4dvar` = 단계 분리 실행. `picard_roms.h` = R4D-Var 의 Picard 반복.
- **observation sensitivity**(`obs_sen_*`): 관측이 예보/분석에 미치는 영향(adjoint of forecast, OSE/OSSE). `array_modes.h` = stabilized representer.

## 3. Control variables

DA 가 조정하는 control: 초기조건(IC) + **boundary**(`obc_adjust`)·**surface forcing**(`frc_adjust`)([roms_support_modules](roms_support_modules.md) §6) increment. weak-constraint(model error) 옵션.

## 4. ★ 모델별 DA framework 비교 (cross-model)

| 모델 | DA 방식 | 근거 |
|---|---|---|
| **ROMS** | **native 변분(I4D/R4D/RBL4D-Var)** + NLM/TLM/ADM/RPM | 본 노트 (Adjoint/Tangent/Representer 158 .F) |
| **Delft3D-FLOW** | OpenDA 연동용 `flow2d3d_openda` DLL 인터페이스를 제공한다. | [OpenDA 연동 시험 설명](../../Delft3D/raw/source_code/Delft3D/src/third_party_open/openda/tests/doc/README.txt)의 3–7줄과 35–43줄은 DLL 함수로 여러 모델 인스턴스를 순차 진행하는 시험을 설명한다. [10-14 전수 검증 정정] |
| **XBeach** | Beach Wizard는 관측 동화 증분으로 바닥 높이를 갱신한다. BMI는 외부 제어 인터페이스를 제공한다. | [beachwizard.F90](../../XBeach/raw/source_code/trunk/src/xbeachlibrary/beachwizard.F90)의 589–603줄에서 `bchwiz`가 1 또는 2이면 `s%zb = s%zb - bw%dassim`을 적용한다. [xbeach_bmi.f90](../../XBeach/raw/source_code/trunk/src/xbeachlibrary/xbeach_bmi.f90)의 43–78줄은 C 바인딩 초기화·시간 진행 함수를 정의한다. [10-14 전수 검증 정정] |
| **ADCIRC** | **외부 ensemble**(ASGS, **built-in DA/adjoint 전무**) — Kalman/ensemble surge 는 외부 wrapper | src/ 55 .F 중 adjoint/variational/ensemble 0개(2026-06-10 전수 확인). `thirdparty/wgrib2/Ensemble.c`는 GRIB2 유틸(무관) |
| **SWAN** | 외부(없음, native DA 부재) | — |
| **EFDC** | 외부(없음) | — |

ROMS는 I4DVAR·R4DVAR·RBL4DVAR 변분 자료동화 드라이버를 제공한다 (`Master/roms_kernel.F:153–166`). [10-14 전수 검증 정정]

## 5. 연결

- [roms_4dvar](roms_4dvar.md)는 배경오차 공분산과 CG/Lanczos 최소화 알고리즘을 설명한다. [10-14 전수 검증 정정]
- [roms_stability_gst](roms_stability_gst.md) — GST(singular vector·optimal pert·stochastic optimal)·obs sensitivity(TLM/ADM 의 DA 외 사용)
- [roms_support_modules](roms_support_modules.md) — obc_adjust/frc_adjust(control), exchange
- [roms_baroclinic_3d](roms_baroclinic_3d.md) — NLM 커널(TLM/ADM 의 선형화 대상)
- [xbeach_beachwizard](../../XBeach/source-analysis/xbeach_beachwizard.md)는 관측 동화에 따른 바닥 높이 갱신을 설명한다. [delft3d_dflowfm_kernel_scheme](../../Delft3D/source-analysis/delft3d_dflowfm_kernel_scheme.md)는 D-Flow FM의 유동 수치해법을 설명한다. [10-14 전수 검증 정정]
- Moore et al. 2011 (ROMS 4D-Var system) / Courtier 1997(incremental) / Bennett(representer)

## 문서와 코드 차이 (10-14 대조)

출처: [ROMS 생물 문서와 코드 대조](../../../_staging/recovery/compare/roms-biology-vs-code.md) §3·§5와 최종 전수 검증 기록. [ROMS 자료동화 계산 흐름 대조](../../../_staging/recovery/flow/ROMS-callflow-da.md) §4·§6·§8과 최종 전수 검증 기록.

문서 판: ROMS 위키 wikitext, 2026-05-03 받음, 쪽별 revid는 [manifest.json](../raw/manuals/wiki/manifest.json). 코드 판: 원본 저장소 HEAD `57aecf58`, 2026-09-18, roms-4.2 이후 4.3 개발.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| biology:CD-003 | 지원하는 수반 생물 커널 범위 | 대상 문서에 대응 서술이 없다. | `ROMS/Adjoint/Biology/ad_biology.F:14` `# if defined BIO_FENNEL`<br>`ROMS/Adjoint/Biology/ad_biology.F:15` `!!#  include <ad_fennel.h>`<br>`ROMS/Adjoint/Biology/ad_biology.F:16` `# elif defined NEMURO`<br>`ROMS/Adjoint/Biology/ad_biology.F:17` `!!#  include <ad_nemuro.h>`<br>`ROMS/Adjoint/Biology/ad_biology.F:18` `# elif defined NPZD_FRANKS`<br>`ROMS/Adjoint/Biology/ad_biology.F:19` `#  include <ad_npzd_Franks.h>`<br>`ROMS/Adjoint/Biology/ad_biology.F:20` `# elif defined NPZD_IRON`<br>`ROMS/Adjoint/Biology/ad_biology.F:21` `#  include <ad_npzd_iron.h>`<br>`ROMS/Adjoint/Biology/ad_biology.F:22` `# elif defined NPZD_POWELL`<br>`ROMS/Adjoint/Biology/ad_biology.F:23` `#  include <ad_npzd_Powell.h>`<br>`ROMS/Adjoint/Biology/ad_biology.F:24` `# endif`<br>`ROMS/Tangent/Biology/tl_biology.F:14` `# if defined BIO_FENNEL`<br>`ROMS/Tangent/Biology/tl_biology.F:15` `!!#  include <tl_fennel.h>`<br>`ROMS/Tangent/Biology/tl_biology.F:16` `# elif defined NEMURO`<br>`ROMS/Tangent/Biology/tl_biology.F:17` `!!#  include <tl_nemuro.h>`<br>`ROMS/Tangent/Biology/tl_biology.F:18` `# elif defined NPZD_FRANKS`<br>`ROMS/Tangent/Biology/tl_biology.F:19` `#  include <tl_npzd_Franks.h>`<br>`ROMS/Tangent/Biology/tl_biology.F:20` `# elif defined NPZD_IRON`<br>`ROMS/Tangent/Biology/tl_biology.F:21` `#  include <tl_npzd_iron.h>`<br>`ROMS/Tangent/Biology/tl_biology.F:22` `# elif defined NPZD_POWELL`<br>`ROMS/Tangent/Biology/tl_biology.F:23` `#  include <tl_npzd_Powell.h>`<br>`ROMS/Tangent/Biology/tl_biology.F:24` `# endif`<br>`ROMS/Representer/Biology/rp_biology.F:14` `# if defined BIO_FENNEL`<br>`ROMS/Representer/Biology/rp_biology.F:15` `!!#  include <rp_fennel.h>`<br>`ROMS/Representer/Biology/rp_biology.F:16` `# elif defined NEMURO`<br>`ROMS/Representer/Biology/rp_biology.F:17` `!!#  include <rp_nemuro.h>`<br>`ROMS/Representer/Biology/rp_biology.F:18` `# elif defined NPZD_FRANKS`<br>`ROMS/Representer/Biology/rp_biology.F:19` `#  include <rp_npzd_Franks.h>`<br>`ROMS/Representer/Biology/rp_biology.F:20` `# elif defined NPZD_IRON`<br>`ROMS/Representer/Biology/rp_biology.F:21` `#  include <rp_npzd_iron.h>`<br>`ROMS/Representer/Biology/rp_biology.F:22` `# elif defined NPZD_POWELL`<br>`ROMS/Representer/Biology/rp_biology.F:23` `#  include <rp_npzd_Powell.h>`<br>`ROMS/Representer/Biology/rp_biology.F:24` `# endif` | C 문서 누락 | 수반 기반 입력 키워드가 존재한다는 사실과 해당 생물 모델의 수반 커널 지원을 구분한다. |
| callflow-da:RF2-020 | 모든 외부 반복을 NLM 재선형화로 설명한 노트 | `models/ROMS/source-analysis/roms_adjoint_framework.md:43` `**outer loop**(NLM 재선형화)`. | ROMS/Drivers/i4dvar_roms.h:292 `OUTER_LOOP : DO my_outer=1,Nouter`<br>ROMS/Drivers/i4dvar_roms.h:302 `CALL background (my_outer, RunInterval)`<br>`ROMS/Drivers/i4dvar.F:681` `# ifdef SOLVE3D`<br>`ROMS/Drivers/i4dvar.F:682` `CALL main3d (RunInterval)`<br>`ROMS/Drivers/i4dvar.F:683` `# else`<br>`ROMS/Drivers/i4dvar.F:684` `CALL main2d (RunInterval)`<br>`ROMS/Drivers/rbl4dvar.F:2687` `# ifdef SOLVE3D`<br>`ROMS/Drivers/rbl4dvar.F:2688` `CALL main3d (RunInterval)`<br>`ROMS/Drivers/rbl4dvar.F:2689` `# else`<br>`ROMS/Drivers/rbl4dvar.F:2690` `CALL main2d (RunInterval)`<br>`ROMS/Drivers/rbl4dvar.F:2713` `IF (DoneStepping) THEN`<br>`ROMS/Drivers/rbl4dvar.F:2742` `CALL edit_multifile ('HIS2FWD')`<br>`ROMS/Drivers/r4dvar.F:826` `IF (my_outer.eq.1) THEN`<br>`ROMS/Drivers/r4dvar.F:827` `CALL edit_multifile ('HIS2FWD')`<br>`ROMS/Drivers/r4dvar.F:828` `ELSE`<br>`ROMS/Drivers/r4dvar.F:829` `CALL edit_multifile ('TLM2FWD')`<br>`ROMS/Drivers/r4dvar.F:1693` `# ifdef SOLVE3D`<br>`ROMS/Drivers/r4dvar.F:1694` `CALL rp_main3d (RunInterval)`<br>`ROMS/Drivers/r4dvar.F:1695` `# else`<br>`ROMS/Drivers/r4dvar.F:1696` `CALL rp_main2d (RunInterval)` | B 문서 오기 | I4와 RBL은 비선형 기본 상태를 갱신한다. R4는 첫 외부 반복에서 NLM 궤적을 사용한다. R4는 이후 외부 반복에서 직전 분석 RPM 궤적을 사용한다. [10-14 결론 검증 보완] |
