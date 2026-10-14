# ROMS 노트 전수 검증 8

- 작업일: 2026-10-14.
- 대상 노트: `models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md`.
- 대상 범위: 새 파일의 전체 줄. frontmatter와 빈 줄을 포함한다.
- 판정 기준: 원문과 보고서 끝의 `전수 검증 기록 (10-14)`을 적용한 최종 결론.
- 기계 확인 불일치 후보: 사용자 제공 목록에 없음.
- 진행 상태: 완료.

## models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md

대상 노트는 [roms_include_cppdefs-differences-3.md](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md)이다.
작업 시작본과 완료본은 모두 336줄이다.
대조한 줄 수는 336줄이다.
이 수는 frontmatter와 빈 줄 38줄을 포함한 파일의 물리적 줄 수이다.

| 집계 항목 | 결과 | 집계 근거 |
|---|---:|---|
| 정정한 줄 수 | 17 | 이번 작업의 `[10-14 전수 검증 정정]` 태그가 있는 줄 |
| 보완한 줄 수 | 12 | 이번 작업의 `[10-14 전수 검증 보완]` 태그가 있는 줄 |
| 정정과 보완이 겹치는 줄 수 | 2 | 노트 246줄과 248줄 |
| 변경한 고유 줄 수 | 27 | 작업 시작본과 완료본의 같은 줄을 비교한 결과 |
| 차이 표 대조 행 수 | 229 | 노트 31–259줄과 `note-job-4.tsv`의 대상 파일 배정 행 |
| 부모 노트 수정안 문단 수 | 8 | 노트 264–336줄의 행 ID별 문단 |
| 최종 파일·줄 인용 수 | 2,048 | 현재 코드 1,591개, 위키 232개, 과거 코드 199개, 보고서 보존본 26개 |
| 최종 인용 조각 대조 수 | 2,733 | 각 파일·줄 인용 뒤의 연속 백틱 인용 조각을 각각 센 값 |
| 미해결 항목 수 | 0 | 원문·보고서·링크·형식 검사 결과 |

### 대조 범위와 판정

- 1–30줄의 frontmatter, 제목, 부모 링크, 출처 안내, 판본 표기와 표 머리글을 확인했다. 위키 수집일은 `models/ROMS/raw/manuals/wiki/manifest.json`의 `fetched_at`과 같다. 코드 HEAD는 `57aecf589a408b1e5490d2db7f9bd0196062a44e`이다. 작성일은 2026-09-18이다. `ROMS/Modules/mod_ncparam.F:653`의 버전 문자열은 `4.3`이다.
- 31–259줄의 항목, 분류, 결론을 연결된 보고서의 최종 결론과 대조했다. 보고서 끝의 `전수 검증 기록 (10-14)`을 함께 적용했다. 정정 태그와 서식 차이 및 별도로 보탠 git 판정 문구를 제외하면 결론은 모두 같다. 배정표의 누락 행과 중복 행은 없다.
- A 분류 55행의 커밋과 날짜를 확인했다. 49행은 `ROMS-git-verify-A6.md`, `ROMS-git-verify-A7.md`, `ROMS-git-verify-A8.md`, `ROMS-git-verify-D1.md`의 해당 판정과 대조했다. 나머지 6행은 outputs-metadata 보고서의 최종 A 판정을 적용했다. 이 6행의 기존 보고 분기 제거는 해당 커밋 전후의 `checkdefs.F` 원문으로 확인했다. `72c1c1d5` 뒤에 남은 SPLINES 검사는 폐기 옵션 오류 검사이다.
- E 분류는 RT2-384 한 행이다. FORWARD_MIXING의 누락된 `#`, 전처리 조건, 사전 정의와 JEDI의 대체 경로를 확인했다. 근거 강도는 representer 보고서와 `ROMS-git-verify-E1.md:97`의 강함을 유지했다. RN1-047에 포함된 염분 반응 결함 후보의 강도는 sediment-ice-vegetation 보고서의 중간을 유지했다.
- 260–336줄의 구조와 본문 및 원문 인용을 대조했다. NT-012, RBH-3448, RBH-3449, RBH-3450, RBH-3451, RBH-3453, RBH-3454, RT1-1536의 수정안 문장을 확인했다. 해석 초기장의 조건과 수치 및 0.01 m의 층 두께를 확인했다.
- 응용 헤더 계수는 `ROMS/Include/*.h`의 파일명 목록으로 재확인했다. 전체는 40개이다. 공통 헤더는 `cppdefs.h`, `globaldefs.h`, `set_bounds.h`, `set_bounds_xtr.h`, `tile.h`의 5개이다. 나머지 응용 헤더는 35개이다. `adria02.h`와 `nj_bight.h`는 이 목록에 없다.
- RTN-272의 수량은 원본 저장소의 `refs/tags/roms-*` 17개로 확인했다. 각 태그의 `globaldefs.h`를 git show로 열었다. 모든 태그에서 SOLVE3D는 COSINE2를 해제하고 POWER_LAW를 정의한다.
- 상대 링크 239개와 frontmatter의 관련 경로 2개를 확인했다. 링크 대상과 절 앵커가 모두 존재한다. Markdown을 메모리에서 렌더링한 표는 본문 229행이며 각 행은 6칸이다. YAML frontmatter도 파싱된다.
- 대상 노트에 mermaid 블록은 없다. 대상 노트에 사용자 홈 절대 경로와 `[[`는 없다. 대상 노트에 사용자가 금지한 한계 문장은 없다.

### 정정 목록

차이 표의 수정 전 부모 노트 인용 26곳이 현재 부모 노트의 해당 줄과 달랐다.
인용 출처를 같은 문장을 보존한 보고서 §4의 줄 번호로 바꿨다.
문서 원문 칸에는 `보고서에 보존된 수정 전 부모 노트`라는 표시를 붙였다.
아래 줄 번호는 대상 노트의 완료본 기준이다.

| 노트:줄 | 행 ID | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| [노트:31](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RBH-3457 | ` models/ROMS/source-analysis/roms_include_cppdefs.md:85 `<br>` models/ROMS/source-analysis/roms_include_cppdefs.md:88 ` | ` _staging/recovery/compare/roms-build-options-history-vs-code.md:3565 ` | 보존본의 인용: `` `globaldefs.h`는 사용자가 직접 만지면 안 되는 **자동 유도 정의** 모음이다. 헤더가 명시: `` |
| [노트:32](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RBH-3459 | ` models/ROMS/source-analysis/roms_include_cppdefs.md:94 ` | ` _staging/recovery/compare/roms-build-options-history-vs-code.md:3567 ` | 보존본의 인용: `` - MPI 통신 디폴트: `mp_boundary`/`mp_collect`/`mp_reduce` 가 사용자가 명시 안 하면 `*_ALLREDUCE` 변형을 기본 선… `` |
| [노트:33](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RBH-3461 | ` models/ROMS/source-analysis/roms_include_cppdefs.md:98 `<br>` models/ROMS/source-analysis/roms_include_cppdefs.md:101 `<br>` models/ROMS/source-analysis/roms_include_cppdefs.md:102 `<br>` models/ROMS/source-analysis/roms_include_cppdefs.md:103 `<br>` models/ROMS/source-analysis/roms_include_cppdefs.md:105 `<br>` models/ROMS/source-analysis/roms_include_cppdefs.md:106 ` | ` _staging/recovery/compare/roms-build-options-history-vs-code.md:3569 ` | 보존본의 인용: `` ROMS 4D-Var 동화의 거대한 OR 블록이 백미다. 수십 개 드라이버 옵션 중 **하나라도** 켜지면 내부 `TANGENT` / `ADJOINT` 가 정의된… `` |
| [노트:34](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RBH-3465 | ` models/ROMS/source-analysis/roms_include_cppdefs.md:123 ` | ` _staging/recovery/compare/roms-build-options-history-vs-code.md:3573 ` | 보존본의 인용: `` - 생물(biology): `BIO_FENNEL`/`ECOSIM`/`NEMURO`/`NPZD_*`/`RED_TIDE` 중 하나 → 내부 `BIOLOGY` (`gl… `` |
| [노트:35](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RBH-3467 | ` models/ROMS/source-analysis/roms_include_cppdefs.md:125 ` | ` _staging/recovery/compare/roms-build-options-history-vs-code.md:3575 ` | 보존본의 인용: `` - 점성 3D 계수: `UV_SMAGORINSKY`/`TS_SMAGORINSKY`/`VEG_HMIXING` → `VISC_3DCOEF`/`DIFF_3DCOEF` … `` |
| [노트:36](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RBH-3468 | ` models/ROMS/source-analysis/roms_include_cppdefs.md:130 ` | ` _staging/recovery/compare/roms-build-options-history-vs-code.md:3576 ` | 보존본의 인용: `` - `SOLVE3D` 정의 시 `COSINE2`(2D 시간평균필터) `#undef` (`globaldefs.h:119-120`). `` |
| [노트:37](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RBH-3471 | ` models/ROMS/source-analysis/roms_include_cppdefs.md:144 `<br>` models/ROMS/source-analysis/roms_include_cppdefs.md:145 `<br>` models/ROMS/source-analysis/roms_include_cppdefs.md:146 ` | ` _staging/recovery/compare/roms-build-options-history-vs-code.md:3579 ` | 보존본의 인용: `` - 물리 코어: `UV_ADV`/`UV_COR`/`UV_LDRAG`/`UV_VIS2`(`upwelling.h:15-18`), `DJ_GRADPS`(`:23`), … `` |
| [노트:38](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RBH-3475 | ` models/ROMS/source-analysis/roms_include_cppdefs.md:197 `<br>` models/ROMS/source-analysis/roms_include_cppdefs.md:208 ` | ` _staging/recovery/compare/roms-build-options-history-vs-code.md:3583 ` | 보존본의 인용: ` ├ (주석) 전 옵션 카탈로그 1~749 ` |
| [노트:52](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RCN-1982 | ` models/ROMS/source-analysis/roms_include_cppdefs.md:168 ` | ` _staging/recovery/compare/roms-coupling-nesting-parallel-vs-code.md:3318 ` | 보존본의 인용: `` 자동 private 저장배열의 수평 시작/끝 인덱스(`IminS`,`ImaxS`,`JminS`,`JmaxS`)와 배열 상하한(`LBi`,`UBi`,…)을 `BOU… `` |
| [노트:55](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | DA1-815 | ` models/ROMS/source-analysis/roms_include_cppdefs.md:98 ` | ` _staging/recovery/compare/roms-da-4dvar-vs-code.md:886 ` | 보존본의 인용: `` ROMS 4D-Var 동화의 거대한 OR 블록이 백미다. 수십 개 드라이버 옵션 중 **하나라도** 켜지면 내부 `TANGENT` / `ADJOINT` 가 정의된… `` |
| [노트:62](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RT2-395 | ` models/ROMS/source-analysis/roms_include_cppdefs.md:112 ` | ` _staging/recovery/compare/roms-da-representer-vs-code.md:738 ` | 보존본의 인용: `` - `WEAK_CONSTRAINT` — `RBL4DVAR`/`R4DVAR`/`SP4DVAR` 등 약제약 4D-Var 류에서 파생 (`globaldefs.h:560… `` |
| [노트:173](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | OMD-N024 | ` models/ROMS/source-analysis/roms_include_cppdefs.md:145 ` | ` _staging/recovery/compare/roms-outputs-metadata-vs-code.md:3503 ` | 보존본의 인용: `` - 출력: `AVERAGES`(`:31`), `DIAGNOSTICS_TS`/`DIAGNOSTICS_UV`(`:32-33`). `` |
| [노트:186](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RN1-047 | ` models/ROMS/source-analysis/roms_include_cppdefs.md:126 ` | ` _staging/recovery/compare/roms-sediment-ice-vegetation-vs-code.md:1392 ` | 보존본의 인용: `` - 부유 생물 거동: `FLOATS && FLOAT_OYSTER → FLOAT_BIOLOGY` (`globaldefs.h:833-836`). `` |
| [노트:246](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RT1-1522 | ` models/ROMS/source-analysis/roms_include_cppdefs.md:25 ` | ` _staging/recovery/compare/roms-testcases-vs-code.md:2624 ` | 보존본의 인용: `` \| `<app>.h` (37개) \| 응용별 옵션 묶음(사용자 선택) \| upwelling.h, wc13.h, double_gyre.h … \| `` |
| [노트:247](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RT1-1523 | ` models/ROMS/source-analysis/roms_include_cppdefs.md:53 ` | ` _staging/recovery/compare/roms-testcases-vs-code.md:2625 ` | 보존본의 인용: `` 따라서 **빌드 순서**는: makefile `ROMS_APPLICATION ?= UPWELLING` (`cppdefs.h:736`) → `ROMS_HEADER=… `` |
| [노트:248](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RT1-1524 | ` models/ROMS/source-analysis/roms_include_cppdefs.md:56 ` | ` _staging/recovery/compare/roms-testcases-vs-code.md:2626 ` | 보존본의 인용: `` cppdefs.h:684~713 이 동봉 예제 목록을 분류한다 — Idealized Test Problems(`cppdefs.h:682`)에 `BASIN`(`cp… `` |
| [노트:249](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RT1-1525 | ` models/ROMS/source-analysis/roms_include_cppdefs.md:146 ` | ` _staging/recovery/compare/roms-testcases-vs-code.md:2627 ` | 보존본의 인용: `` - 해석식 강제(이상화 → 외부파일 불필요): `ANA_GRID`/`ANA_INITIAL`/`ANA_SMFLUX`/`ANA_STFLUX`/… (`upwelling… `` |

### 보완 목록

현재 코드의 직접 인용 41개를 9개 표 행에 보탰다.
헤더 계수의 범위는 표 2행과 본문 1줄에 보탰다.
이 수는 아래 보완 목록의 인용과 줄 번호에서 셌다.

| 노트:줄 | 행 ID | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| [노트:40](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RF2-015 | WEAK_CONSTRAINT 대입만 인용했다. | R4DVAR·RBL4DVAR가 포함된 파생 조건을 보탰다. | ` ROMS/Include/globaldefs.h:559 ` ` #if !defined WEAK_CONSTRAINT          && \ `<br>` ROMS/Include/globaldefs.h:563 ` `      defined RBL4DVAR                 \|\| \ `<br>` ROMS/Include/globaldefs.h:566 ` `      defined R4DVAR                   \|\| \ ` |
| [노트:41](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RF2-030 | Nouter 검사만 인용했다. | WEAK_CONSTRAINT와 사후 오차 옵션의 전처리 조건을 보탰다. | ` ROMS/Utility/read_phypar.F:8023 ` ` #if defined WEAK_CONSTRAINT   && \ `<br>` ROMS/Utility/read_phypar.F:8024 ` `    (defined POSTERIOR_EOFS    \|\| defined POSTERIOR_ERROR_F \|\| \ `<br>` ROMS/Utility/read_phypar.F:8025 ` `     defined POSTERIOR_ERROR_I) ` |
| [노트:59](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RT2-362 | 내부 CPP 파생만 인용했다. | NSA 대입의 실행 조건과 SP4DVAR 분기를 보탰다. | ` ROMS/Utility/read_phypar.F:4745 ` ` # if defined CORRELATION \|\| defined WEAK_CONSTRAINT `<br>` ROMS/Utility/read_phypar.F:4746 ` ` #  ifdef SP4DVAR `<br>` ROMS/Utility/read_phypar.F:4747 ` `         NSA=2 `<br>` ROMS/Utility/read_phypar.F:4748 ` ` #  else `<br>` ROMS/Utility/read_phypar.F:4749 ` `         IF (nADJ(ng).lt.ntimes(ng)) THEN `<br>` ROMS/Utility/read_phypar.F:4750 ` `           NSA=2 `<br>` ROMS/Utility/read_phypar.F:4751 ` `         ELSE `<br>` ROMS/Utility/read_phypar.F:4752 ` `           NSA=1 `<br>` ROMS/Utility/read_phypar.F:4753 ` `         END IF ` |
| [노트:181](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RCO1-029 | SwimTimeNew 저장문만 인용했다. | 정착 크기 미만이라는 저장 조건을 보탰다. | ` ROMS/Nonlinear/Biology/oyster_floats.h:410 ` `           IF (track(isizf,nfp1,l).lt.settle_size(ng)) THEN ` |
| [노트:246](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RT1-1522 | 헤더 수에 계수 범위를 적지 않았다. | 공통 헤더 목록과 응용 헤더 계수 범위를 명시했다. | `ROMS/Include/*.h`의 파일명 목록. `_staging/recovery/compare/roms-build-options-history-vs-code.md:3559`은 전체 40개와 공통 헤더 5개 및 응용 헤더 35개를 구분한다. |
| [노트:248](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RT1-1524 | 응용 헤더 수에 계수 범위를 적지 않았다. | 공통 헤더 목록과 응용 헤더 계수 범위를 명시했다. | `ROMS/Include/*.h`의 파일명 목록. `_staging/recovery/compare/roms-build-options-history-vs-code.md:3559`은 전체 40개와 공통 헤더 5개 및 응용 헤더 35개를 구분한다. |
| [노트:250](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RTN-156 | COSINE2 해제문만 인용했다. | POWER_LAW 정의문을 보탰다. | ` ROMS/Include/globaldefs.h:121 ` ` # define POWER_LAW ` |
| [노트:251](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RTN-226 | 기본 수평 이류 설명만 인용했다. | 기본 3D 연직 이류 설명을 보탰다. | ` ROMS/Include/cppdefs.h:17 ` ` **   vertical advection is 4th-order centered for 3D momentum. If this       ** ` |
| [노트:255](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RTN-356 | PJ_GRADPQ4 분기만 인용했다. | NLM·SOLVE3D 조건과 나머지 선택 분기 및 기본 include를 보탰다. | ` ROMS/Nonlinear/prsgrd.F:2 ` ` #if defined NONLINEAR && defined SOLVE3D `<br>` ROMS/Nonlinear/prsgrd.F:18 ` ` # elif defined PJ_GRADPQ2 `<br>` ROMS/Nonlinear/prsgrd.F:19 ` ` #  include "prsgrd42.h" `<br>` ROMS/Nonlinear/prsgrd.F:20 ` ` # elif defined PJ_GRADP `<br>` ROMS/Nonlinear/prsgrd.F:21 ` ` #  include "prsgrd40.h" `<br>` ROMS/Nonlinear/prsgrd.F:22 ` ` # elif defined DJ_GRADPS `<br>` ROMS/Nonlinear/prsgrd.F:23 ` ` #  include "prsgrd32.h" `<br>` ROMS/Nonlinear/prsgrd.F:24 ` ` # else `<br>` ROMS/Nonlinear/prsgrd.F:25 ` ` #  include "prsgrd31.h" `<br>` ROMS/Nonlinear/prsgrd.F:26 ` ` # endif ` |
| [노트:256](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RTN-361 | VAR_RHO_2D 자동 정의만 인용했다. | 선형 커널 제한을 설명하는 원문 주석을 보탰다. | ` ROMS/Include/globaldefs.h:483 ` ` ** Activate bacroclinic pressure gradient response due to the `<br>` ROMS/Include/globaldefs.h:484 ` ` ** perturbation of free-surface in the presence of stratification `<br>` ROMS/Include/globaldefs.h:485 ` ` ** and bathymetry. This option does not pass the sanity check `<br>` ROMS/Include/globaldefs.h:486 ` ` ** in adjoint and tangent linear applications, so we use NOT_YET `<br>` ROMS/Include/globaldefs.h:487 ` ` ** in TLM, RPM, and ADM kernels. ` |
| [노트:257](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RTN-364 | PJ_GRADPQ4의 include만 인용했다. | PJ_GRADPQ2의 NLM·TLM·RPM·ADM include를 보탰다. | ` ROMS/Nonlinear/prsgrd.F:18 ` ` # elif defined PJ_GRADPQ2 `<br>` ROMS/Nonlinear/prsgrd.F:19 ` ` #  include "prsgrd42.h" `<br>` ROMS/Tangent/tl_prsgrd.F:18 ` ` # elif defined PJ_GRADPQ2 `<br>` ROMS/Tangent/tl_prsgrd.F:19 ` ` !!#  include "tl_prsgrd42.h" `<br>` ROMS/Representer/rp_prsgrd.F:18 ` ` # elif defined PJ_GRADPQ2 `<br>` ROMS/Representer/rp_prsgrd.F:19 ` ` !!#  include "rp_prsgrd42.h" `<br>` ROMS/Adjoint/ad_prsgrd.F:18 ` ` # elif defined PJ_GRADPQ2 `<br>` ROMS/Adjoint/ad_prsgrd.F:19 ` ` !!#  include "ad_prsgrd42.h" ` |
| [노트:304](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-3.md) | RBH-3451 | 현재 Include에는 응용 헤더 35개가 있다. | 응용 헤더 계수의 glob과 제외할 공통 헤더를 명시했다. | `ROMS/Include/*.h`의 파일명 목록. `_staging/recovery/compare/roms-build-options-history-vs-code.md:3559`은 전체 40개와 공통 헤더 5개 및 응용 헤더 35개를 구분한다. |

### 기계 확인 후보 판정

- 사용자 제공 불일치 후보: 없음. 후보를 이유로 정정한 줄은 없다.
- 추가 검사에서 `WET_DRY.wiki:16–17`의 줄바꿈과 노트 109줄의 `<br>`를 대조했다. 표시 글자는 같다. 노트 인용을 유지했다.
- 현재 부모 노트 인용의 불일치는 위 정정 목록의 17행에서 처리했다. 최종 파일·줄 인용 2,048개에 연결된 인용 조각 2,733개는 모두 원문에 대응한다. 위키 마크업과 Markdown 표의 파이프 이스케이프는 표시 글자로 대조했다.

### 완료 확인

대상 노트의 전체 336줄을 대조했다.
정정과 보완의 줄 번호는 최종 파일에서 다시 확인했다.
대상 노트의 부정, 조건, 수량, 단위와 부호를 확인했다.
퇴적층 두께의 m 단위는 `ROMS/External/varinfo.yaml:3607–3613`의 `bed_thickness`, `units: meter`, `idSbed(ithck)` 연결과도 같다.
외부 원문 보고서의 최종 `Claude 확인과 보완`에는 이번 대상 행에 적용할 별도 판정이 없다.
쓰기 대상은 지정한 노트와 이 기록 파일로 한정했다.
git 쓰기 명령, sudo와 모델 실행은 사용하지 않았다.
남은 대조 항목은 없다.
