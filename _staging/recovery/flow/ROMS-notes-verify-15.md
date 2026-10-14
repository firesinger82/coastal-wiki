# ROMS 노트 전수 대조 15

- 작업일: 2026-10-14.
- 대상: 사용자가 지정한 노트 네 개의 작업 시작 시점 `git diff -U0 HEAD -- <노트>` 추가 줄 전체. 새 파일은 전체 줄을 대상으로 한다.
- 집계에는 frontmatter, 표, 제목, 빈 줄, 코드 블록 구분자를 포함한다.
- 결론은 비교 보고서와 호출 흐름 보고서 끝의 `전수 검증 기록 (10-14)`를 적용한다. 외부 자료 보고서는 끝의 `Claude 확인과 보완`을 적용한다.
- 기계 확인 불일치 후보: 사용자 제공 목록에 후보가 없다.
- 아래 노트별 완료 기록은 각 노트의 대조가 끝난 뒤에 추가한다.

## roms-wiki-getting-started.md — 완료

- 파일: [roms-wiki-getting-started.md](../../../models/ROMS/manual-notes/roms-wiki-getting-started.md).
- 대조한 줄 수: 작업 시작 시점의 추가 줄 194줄이다.
- 대조 범위: `6–7, 24, 29–33, 70–71, 88, 94, 99–103, 109, 129, 142–152, 154, 162–165, 167, 171, 173–178, 193, 197–200, 204, 208–352`.
- 정정 수: 2줄이다. 보완 수: 0줄이다. 수량은 이 작업의 정정·보완 표지를 붙인 줄에서 셌다.
- 차이 표의 133행을 보고서 최종 결론과 대조했다. 분류와 결론의 뜻은 모두 같다.
- A 분류의 64행을 대조했다. git 판정서에 있는 58행의 HASH·날짜가 같다. 최종 보고서에서 H를 A로 바꾼 `RBH-2623·2624·2695·2696·2825·2826`의 6행은 최종 보고서의 결론과 커밋 근거를 따랐다.
- 본문은 보고서 §4의 수정안과 현재 코드·과거 코드·위키 원문을 대조했다. `ROMS/Drivers`의 파일 46개와 헤더 41개를 해당 디렉터리에서 다시 셌다. `manifest.json`의 페이지 수 326과 Getting Started의 revid 6667을 확인했다. frontmatter의 77줄은 원본 Markdown의 `wc -l` 값과 같다.
- 노트의 상대 링크 29개는 모두 실제 파일 또는 디렉터리를 가리킨다. Mermaid 블록은 없다. 절대 경로 `/home/firesinger/`와 이중 대괄호는 없다. 금지한 한계 문장은 없다.
- 기계 확인 후보 판정: 사용자 제공 목록에 후보가 없다.

| 정정 위치 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `models/ROMS/manual-notes/roms-wiki-getting-started.md:204` | NIFS 다층 수온 자료에 `ROMS forcing source` 역할을 붙였다. | NIFS 다층 수온 추세의 관련 경험 자료 링크로 한정했다. | `experience/nifs-vertical-sst-trends.md:27–35`는 NIFS KODC 수온 관측 분석을 소개한다. 같은 파일에는 ROMS 강제력 자료라는 설명이 없다. 대상 비교 보고서에도 이 역할의 근거가 없다. |
| `models/ROMS/manual-notes/roms-wiki-getting-started.md:318` | 결론 칸의 `<app>.h`에 코드 구분자가 없다. | 결론 칸의 `<app>.h`를 백틱으로 감쌌다. | `ROMS/Include/cppdefs.h:746–748`은 응용별 `*.h` 작성을 설명한다. `roms-build-options-history-vs-code.md`의 `RBH-3490`은 응용 헤더 이름을 `<app>.h`로 적는다. |

## roms_nonlinear_vegetation.md — 완료

- 파일: [roms_nonlinear_vegetation.md](../../../models/ROMS/source-analysis/roms_nonlinear_vegetation.md).
- 대조한 줄 수: 작업 시작 시점의 추가 줄 73줄이다.
- 대조 범위: `7–8, 102–106, 132–143, 147–156, 160–162, 170, 181–182, 184–188, 197–229`.
- 정정 수: 0줄이다. 보완 수: 1줄이다. 수량은 이 작업의 정정·보완 표지를 붙인 줄에서 셌다.
- 차이 표의 24행은 보고서 최종 분류와 결론이 같다. E 분류의 `RF1-004·OMD-Y652`는 중간이다. `RV1-026·RCO1-041`은 강함이다. 각 강도는 git 판정서 E2와 최종 보고서에 부합한다. A 행은 없다.
- 두 Fortran 코드 블록의 5줄은 `vegetation_turb.F:203–205, 237–238`과 글자 단위로 같다. `cff2`의 재대입, `inverse_dissip`의 MAX, `tauveg`의 MIN, `max_eps=1.0e14`, `max_L` 상한과 타입별 합산을 원문에서 확인했다.
- `vegetation_hmixing` 검색 결과는 USE 두 곳과 CALL 한 곳이다. 정의는 없다. `idTmsc`는 YAML 항목에만 있다. `Dout(M2fsgr)`와 `Dout(M3fsgr)`를 처리하는 CASE는 없다.
- 노트의 상대 링크 8개는 모두 실제 파일을 가리킨다. Mermaid 블록은 없다. 절대 경로 `/home/firesinger/`와 이중 대괄호는 없다. 작업 미완료를 뜻하는 한계 문장은 없다. 다중 식생 타입에 대한 불확실성은 코드 원문의 주석이므로 유지했다.
- 기계 확인 후보 판정: 사용자 제공 목록에 후보가 없다.

| 보완 위치 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `models/ROMS/source-analysis/roms_nonlinear_vegetation.md:160` | 호출 관계에 두 서브루틴의 선언 줄 `32,70`을 인용했다. | 실제 호출 줄 `49`를 추가했다. 호출 관계를 한국어 문장으로 적었다. | `ROMS/Nonlinear/Vegetation/vegetation_stream.F:49`의 `CALL vegetation_stream_tile (ng, tile, …)`가 호출 관계를 보인다. 선언은 32행과 70행에 있다. `roms-sediment-ice-vegetation-vs-code.md`의 `RN1-015`는 streaming 설명 유지를 지시한다. |

## roms_advection.md — 완료

- 파일: [roms_advection.md](../../../models/ROMS/source-analysis/roms_advection.md).
- 대조한 줄 수: 작업 시작 시점의 추가 줄 76줄이다.
- 대조 범위: `6, 8, 40–43, 54–58, 66–67, 80–83, 93, 95–99, 114–116, 120, 134, 136, 145, 154–160, 171–209`.
- 정정 수: 3줄이다. 보완 수: 10줄이다. 수량은 이 작업의 정정·보완 표지를 붙인 줄에서 셌다.
- 차이 표의 30행은 보고서 최종 분류와 결론이 같다. 생물 입력의 E 후보 9행과 퇴적물 입력의 E 후보 1행은 모두 근거 강함이다. git 판정서 E1·E2의 강도와 같다. A 행은 없다.
- 생물 입력 헤더 9개와 퇴적물 입력 헤더의 중복 `Vadvection` 선택자를 원문에서 확인했다. 과거 커밋의 같은 선택자도 대조했다. C4 계수, U3 곡률 선택, 방향별 입력, 초기 논리값과 호출 순서를 원문에서 확인했다.
- 노트의 상대 링크 20개는 모두 실제 파일을 가리킨다. Mermaid 블록은 없다. 대상 줄에는 절대 경로 `/home/firesinger/`, 이중 대괄호와 금지한 한계 문장이 없다.
- 기계 확인 후보 판정: 사용자 제공 목록에 후보가 없다.

| 구분·위치 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| 정정 `models/ROMS/source-analysis/roms_advection.md:40` | AKIMA4가 조건 없이 harmonic mean을 쓰는 설명이다. | `IF (cff.gt.eps) THEN`과 ELSE의 0 대입을 함께 적었다. | `ROMS/Nonlinear/step3d_t.F:669–675`. 최종 결론 `RTN-176`도 두 분기를 구분한다. |
| 정정 `models/ROMS/source-analysis/roms_advection.md:42` | 본문에도 harmonic mean 조건이 없다. | 표와 같은 조건과 0 대입을 적었다. | `ROMS/Nonlinear/step3d_t.F:669–675`, `RTN-176`. |
| 정정 `models/ROMS/source-analysis/roms_advection.md:43` | 수평 이류 절에서 SPLINES의 방향을 생략했다. | 인용한 SPLINES 분기가 연직 이류임을 명시했다. | `ROMS/Nonlinear/step3d_t.F:936`의 `Vadvection(itrc,ng)%SPLINES`와 938–940행의 연직 미분 설명. |
| 보완 `models/ROMS/source-analysis/roms_advection.md:194` | 위키 인용은 식 시작 태그만 담았다. 코드 인용은 계수 대입만 담았다. | G의 정의·식 (22)와 코드의 평균·보정식 범위를 추가했다. | `Numerical_Solution_Technique.wiki:571–596`, `ROMS/Nonlinear/step3d_t.F:676–700`. |
| 보완 `models/ROMS/source-analysis/roms_advection.md:195` | 위키 인용은 식 시작 태그만 담았다. 코드 인용에는 harmonic mean 대입 줄이 없다. | 세 gradient 식과 조건·대입의 전체 범위를 추가했다. | `Numerical_Solution_Technique.wiki:603–616`, `ROMS/Nonlinear/step3d_t.F:669–675`. |
| 보완 `models/ROMS/source-analysis/roms_advection.md:196` | 조건 일부와 계수 선언만 인용했다. | 평균 밖 보정 계수를 판별할 수 있는 전체 flux 식을 추가했다. | `ROMS/Nonlinear/step3d_t.F:683–684, 693–700`. |
| 보완 `models/ROMS/source-analysis/roms_advection.md:197` | 식 (23)의 안내 문장과 코드 식 앞부분만 인용했다. | 위키 식과 upstream 곡률을 포함하는 코드 식을 추가했다. | `Numerical_Solution_Technique.wiki:634–636`, `ROMS/Nonlinear/step3d_t.F:687–692`. |
| 보완 `models/ROMS/source-analysis/roms_advection.md:199` | 추적자 번호 증가 줄만 입력 근거로 인용했다. | Hadvection·Vadvection의 CASE와 load_tadv 호출 범위를 추가했다. | `ROMS/Utility/read_phypar.F:418–442`. |
| 보완 `models/ROMS/source-analysis/roms_advection.md:200` | 코드 계수 대입만 인용했다. | 내부면 범위와 계수 적용식을 추가했다. | `ROMS/Nonlinear/step3d_t.F:1153–1163`. |
| 보완 `models/ROMS/source-analysis/roms_advection.md:202` | 방향·추적자별 입력을 뒷받침하는 판독 줄이 없다. | 방향·추적자별 입력 범위를 추가했다. | `ROMS/Utility/read_phypar.F:418–442`. |
| 보완 `models/ROMS/source-analysis/roms_advection.md:203` | 각 방향의 처음 두 필드만 초기값 근거로 인용했다. | 전체 선택 필드의 초기값 범위를 추가했다. | `ROMS/Modules/mod_param.F:1816–1839`. |
| 보완 `models/ROMS/source-analysis/roms_advection.md:205` | SPLINES의 IF 조건과 빈 주석 줄만 인용했다. | parabolic spline의 직접 설명을 추가했다. | `ROMS/Nonlinear/step3d_t.F:938–940`. |
| 보완 `models/ROMS/source-analysis/roms_advection.md:206` | 공통 분기의 IF 조건만 인용했다. | 실제 중심 차분 flux 식까지 인용했다. | `ROMS/Nonlinear/step3d_t.F:1144–1163`. |

## roms_tangent_linear_model.md — 완료

- 파일: [roms_tangent_linear_model.md](../../../models/ROMS/source-analysis/roms_tangent_linear_model.md).
- 대조한 줄 수: 작업 시작 시점의 추가 줄 33줄이다.
- 대조 범위: `7–8, 31, 48, 54, 63–66, 92, 167–168, 187–193, 211, 213, 228–239`.
- 정정 수: 3줄이다. 보완 수: 6줄이다. 수량은 이 작업의 정정·보완 표지를 붙인 줄에서 셌다.
- 차이 표의 `RTN-381`은 최종 보고서와 같은 B 문서 오기이다. 기본 압력경도 헤더는 `tl_prsgrd31.h`이다. A 행과 E 행은 없다.
- 본문을 `RTN-381·383·384`, `DA1-811`과 호출 흐름 보고서의 TLM 진입 조건에 대조했다. 시간 슬롯과 LF-AM3·AB3를 구분했다. 공통 `lambda=1.0_r8`, 현재 단계 계수 0과 미래 단계의 암시 계산을 TLM 원문에서도 확인했다.
- `ROMS/Tangent/` 최상위의 `.F` 파일 54개와 `.h` 파일 18개를 다시 셌다. 합계는 72개이다.
- 노트의 상대 링크 7개는 모두 실제 파일을 가리킨다. Mermaid 블록은 없다. 대상 줄에는 절대 경로 `/home/firesinger/`, 이중 대괄호와 금지한 한계 문장이 없다.
- 기계 확인 후보 판정: 사용자 제공 목록에 후보가 없다.

| 구분·위치 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| 정정 `models/ROMS/source-analysis/roms_tangent_linear_model.md:31` | 개별 커널의 대응을 확인하지 않았다는 한계 문장이 남아 있다. | 드라이버의 역할과 직접 센 파일 수를 유지했다. 한계 문장은 제거했다. | `ROMS/Tangent/tl_main3d.F:12–15`와 해당 디렉터리의 파일 목록. `DA1-811`의 사실 설명은 유지했다. 보고서의 미확인 범위 유지 지시보다 최신 사용자 지시 6번을 우선했다. |
| 보완 `models/ROMS/source-analysis/roms_tangent_linear_model.md:48` | 진입 드라이버의 호출을 다른 노트 링크로만 설명했다. | `SOLVE3D` 조건과 실제 두 CALL의 인용을 추가했다. | `ROMS/Drivers/tl_roms.h:277–281`. |
| 보완 `models/ROMS/source-analysis/roms_tangent_linear_model.md:65` | n-1·n-2를 설명하는 헤더만으로 n까지의 조립을 설명했다. | 과거 단계 조립과 현재 단계 갱신의 TLM 계산식을 추가 인용했다. | `ROMS/Tangent/tl_pre_step3d.F:1559–1581`, `ROMS/Tangent/tl_step3d_uv.F:393–423`. `RTN-383`의 수정안과 같다. |
| 정정 `models/ROMS/source-analysis/roms_tangent_linear_model.md:92` | NLM과 CALL 시퀀스가 일치하며 TLM은 NLM의 줄단위 거울이라고 단정했다. | `tl_rhs3d` 뒤에 2D 예측·보정과 3D 운동량 갱신이 오는 대표 순서를 적었다. | `ROMS/Tangent/tl_main3d.F:554, 612, 659, 749`. `ROMS-callflow-da.md`의 `tl_main3d` 호출 표와 같다. `DA1-811`은 전체 커널 대응으로 확대하지 않는다. |
| 보완 `models/ROMS/source-analysis/roms_tangent_linear_model.md:191` | 현재 단계 확산의 0 기여에 NLM 계산식만 인용했다. | TLM의 같은 계수와 선형화된 확산 플럭스 식을 추가 인용했다. | `ROMS/Tangent/tl_pre_step3d.F:1292–1318`. 공통 가중치는 `ROMS/Modules/mod_scalars.F:760–765`이다. `RTN-384`의 결론을 유지했다. |
| 보완 `models/ROMS/source-analysis/roms_tangent_linear_model.md:192` | 미래 단계의 암시 계산에 NLM 계산식만 인용했다. | TLM의 미래 단계 확산과 삼중대각계 선형화 설명을 추가 인용했다. | `ROMS/Tangent/tl_step3d_t.F:1355–1373`. `RTN-384`의 결론을 유지했다. |
| 보완 `models/ROMS/source-analysis/roms_tangent_linear_model.md:211` | 최소화·합성곱 루틴의 역할에 직접 인용이 없다. | 켤레경사 알고리즘과 배경오차 공분산의 헤더 설명을 추가했다. | `ROMS/Tangent/tl_rpcg_lanczos.F:17–18`, `tl_congrad.F:18–19`, `tl_convolution.F:11–26`. `tl_conv_2d.F:14–17`, `tl_conv_3d.F:14–17`, `tl_conv_bry2d.F:13–16`, `tl_conv_bry3d.F:14–17`의 헤더도 역할과 같다. |
| 보완 `models/ROMS/source-analysis/roms_tangent_linear_model.md:213` | 수반·TLM의 전파 방향과 RPM 구분에 직접 인용이 없다. | 각 드라이버와 수반·전진 연산자 설명을 인용했다. RPM의 위키 설명도 인용했다. | `ROMS/Adjoint/ad_main3d.F:12–15`, `ROMS/Drivers/symmetry.h:12–16`, `ROMS/Representer/rp_main3d.F:12–15`, `Regional_Ocean_Modeling_System__ROMS_.wiki:11`. |
| 정정 `models/ROMS/source-analysis/roms_tangent_linear_model.md:228` | `source-needed`와 추후 확장 문장이 남아 있다. | 이미 있는 4D-Var 노트의 관련 설명을 안내했다. | `models/ROMS/source-analysis/roms_4dvar.md:47–88`은 내부 최소화와 배경오차 공분산을 다룬다. 최신 사용자 지시 6번에 따라 작업 한계 문장을 제거했다. |

## 최종 집계

| 노트 | 대조한 추가 줄 | 정정 줄 | 보완 줄 |
|---|---:|---:|---:|
| roms-wiki-getting-started.md | 194 | 2 | 0 |
| roms_nonlinear_vegetation.md | 73 | 0 | 1 |
| roms_advection.md | 76 | 3 | 10 |
| roms_tangent_linear_model.md | 33 | 3 | 6 |
| 합계 | 376 | 8 | 17 |

- 대상 376줄의 대조를 완료했다. 수량은 작업 시작 시점의 읽기 전용 `git diff -U0 HEAD` 추가 줄에서 셌다. 정정 후에도 추가 줄 번호와 수량은 같다.
- 차이 표 188행의 분류와 결론을 최종 보고서에 대조했다. git 근거 문장과 E 강도의 표시 위치 차이를 제외한 결론은 모두 같다. HASH·날짜와 E 강도는 각 노트의 완료 기록과 같이 대조했다.
- 상대 링크 64개는 모두 존재한다. 표의 열 수와 정정·보완 표지 위치를 확인했다. `git diff --check HEAD -- <대상 파일>`은 통과했다.
- 기계 확인 불일치 후보는 없다. 대상 줄의 미해결 항목은 없다.
