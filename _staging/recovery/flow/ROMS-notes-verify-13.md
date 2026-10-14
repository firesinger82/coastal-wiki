# ROMS 노트 전수 대조 13 (10-14)

## 대조 범위

- 대상은 사용자 지정 노트 5개다.
- `roms_include_cppdefs-differences-2.md`는 작업 시작 시 전체 줄을 대조한다.
- 나머지 노트는 작업 시작 시 `git diff -U0 HEAD -- <노트>`의 추가 줄을 대조한다.
- 대조 줄 수에는 frontmatter와 빈 줄을 포함한다.
- 정정 수와 보완 수는 수정한 대상 줄 수로 센다.
- 현재 코드와 위키 원문을 확인한다.
- 보고서 끝의 전수 검증 기록을 결론 판정에 우선 적용한다.
- 노트별 대조 결과는 완료한 순서대로 아래에 추가한다.

## roms_include_cppdefs-differences-2.md — 완료

- 대상: [roms_include_cppdefs-differences-2.md](../../../models/ROMS/source-analysis/roms_include_cppdefs-differences-2.md).
- 대조한 줄 수: 작업 시작 시 전체 258줄이다.
- 대조 범위: 1–28줄의 frontmatter·제목·판본·링크·표 머리글과 29–258줄의 차이 표 230행이다.
- 정정 수: 6줄이다.
- 보완 수: 0줄이다.
- 결론 근거: `roms-build-options-history-vs-code.md` §4.1·§5와 끝의 전수 검증 기록 작업 6/7·7/7이다.
- 차이 표의 분류 230개는 보고서 최종본과 같다.
- E 행 13개의 강도는 최종 검증 기록과 같다.
- E 행 중 RBH-3425–3434의 판정은 `ROMS-git-verify-E1.md:75–84`와 같다.
- A 행은 없다.
- 코드 인용의 조건·식·부정·주석을 현재 원문과 대조했다.
- 응용 헤더 35개는 `ROMS/Include/*.h`에서 `cppdefs.h`, `globaldefs.h`, `tile.h`, `set_bounds.h`, `set_bounds_xtr.h`를 제외하여 셌다.
- 코드 HEAD의 해시와 날짜는 `57aecf589a408b1e5490d2db7f9bd0196062a44e`, `2026-09-18`이다.
- 위키 수집일과 쪽별 판 정보는 `raw/manuals/wiki/manifest.json`과 같다.
- 상대 링크 14개는 실제 파일을 가리킨다.
- mermaid 블록과 금지한 한계 문장은 없다.
- 개인 절대 경로와 이중 대괄호 링크는 없다.

정정 목록의 노트 줄 번호는 작업 전후 동일하다.
아래 정정은 수정 전 노트의 인용문을 보존한 보고서로 출처를 바꾼다.
각 문서 원문 칸에 `반영 전 노트 인용`을 명시했다.
각 결론 문장 칸 끝에 `[10-14 전수 검증 정정]`을 붙였다.

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `roms_include_cppdefs-differences-2.md:253` | 현재 부모 노트 `roms_include_cppdefs.md:19` 인용 | 보고서 `roms-build-options-history-vs-code.md:3556`의 반영 전 노트 인용 | RBH-3448 문서 원문 칸에 기존의 “단일 빌드 = 단일 구성” 문장이 보존되어 있다. |
| `roms_include_cppdefs-differences-2.md:254` | 현재 부모 노트의 23·32·34줄 인용 | 같은 보고서 3557줄의 반영 전 노트 인용 | RBH-3449 문서 원문 칸에 카탈로그 설명 세 문구가 보존되어 있다. |
| `roms_include_cppdefs-differences-2.md:255` | 현재 부모 노트의 24·53줄 인용 | 같은 보고서 3558줄의 반영 전 노트 인용 | RBH-3450 문서 원문 칸에 자동 유도와 검증에 관한 두 문구가 보존되어 있다. |
| `roms_include_cppdefs-differences-2.md:256` | 현재 부모 노트의 25·56줄 인용 | 같은 보고서 3559줄의 반영 전 노트 인용 | RBH-3451 문서 원문 칸에 기존의 헤더 37개 설명이 보존되어 있다. |
| `roms_include_cppdefs-differences-2.md:257` | 현재 부모 노트의 40·42·45줄 인용 | 같은 보고서 3561줄의 반영 전 노트 인용 | RBH-3453 문서 원문 칸에 `//` 설명을 붙였던 코드 인용 세 줄이 보존되어 있다. |
| `roms_include_cppdefs-differences-2.md:258` | 현재 부모 노트의 53줄 인용 | 같은 보고서 3562줄의 반영 전 노트 인용 | RBH-3454 문서 원문 칸에 `ROMS_APPLICATION`의 기본값 위치를 잘못 적었던 문장이 보존되어 있다. |

기계 확인 후보: 이 노트에 지정된 후보는 없다.

## roms_grid_metrics.md — 완료

- 대상: [roms_grid_metrics.md](../../../models/ROMS/source-analysis/roms_grid_metrics.md).
- 대조한 줄 수: 작업 시작 시 `git diff -U0 HEAD`의 추가 103줄이다.
- 대조 범위: 6–7, 28–29, 41–43, 59–61, 101–102, 104–113, 125–126, 131–132, 174, 176, 182–190, 193–200, 206–209, 226–279줄이다.
- 정정 수: 6줄이다.
- 보완 수: 0줄이다.
- 차이 표 44행의 분류와 결론을 여섯 근거 보고서의 최종본에 대조했다.
- 본문은 RCN-1977–1980, RI1-1051–1053, RT1-1537, RTN-398, RTG-1978–1980의 수정안에 대조했다.
- 타일 수 검사에서 SP4DVAR·DISJOINTED·CONCURRENT_KERNEL·비동기 PIO의 조건을 확인했다.
- 타일 크기 식과 ghost 폭의 조건을 현재 코드에서 확인했다.
- 파일 격자의 spherical 입력과 SPHERICAL의 해석식 격자 적용 범위를 확인했다.
- pm·pn의 단위와 PSI no-slip 값 2를 원문에서 확인했다.
- 표의 원문 인용 504개를 현재 코드·과거 코드·위키와 대조했다.
- RCN-1381과 RCN-1383의 `4d0fa601`·`2012-05-12`는 `ROMS-git-verify-A6.md:42,44` 및 해당 커밋과 같다.
- 위키의 굵게 표시와 링크 마크업은 표시 글자로 비교했다.
- 수정 전 노트 문장은 보고서에 보존된 문장으로 판정했다.
- 상대 링크 8개는 실제 파일을 가리킨다.
- 대상 추가 줄에는 mermaid 블록과 금지한 한계 문장이 없다.
- 개인 절대 경로와 이중 대괄호 링크는 없다.

아래 정정은 문서 원문 칸의 출처를 보고서에 보존된 반영 전 노트 인용으로 바꾼다.
각 결론 문장 칸 끝에 `[10-14 전수 검증 정정]`을 붙였다.
노트 줄 번호는 작업 전후 동일하다.

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `roms_grid_metrics.md:250` | 현재 노트 95·166·176줄 인용 | `roms-coupling-nesting-parallel-vs-code.md:3310`의 반영 전 노트 인용 | RCN-1977에 일반 MPI 검사만 적었던 문장 세 개가 보존되어 있다. |
| `roms_grid_metrics.md:251` | 현재 노트 169줄 인용 | 같은 보고서 3312줄의 반영 전 노트 인용 | RCN-1979에 기존 ghost 폭 설명이 보존되어 있다. |
| `roms_grid_metrics.md:254` | 현재 노트 27·93줄 인용 | `roms-inputs-vs-code.md:1427`의 반영 전 노트 인용 | RI1-1051에 NtileJ 저장 줄을 빠뜨린 기존 인용이 보존되어 있다. |
| `roms_grid_metrics.md:255` | 현재 노트 169줄 인용 | 같은 보고서 1432줄의 반영 전 노트 인용 | RI1-1053에 기존 ghost 폭 설명이 보존되어 있다. |
| `roms_grid_metrics.md:278` | 현재 노트 35·37·154줄 인용 | `roms-tools-guides-vs-code.md:2220`의 반영 전 노트 인용 | RTG-1978에 기존 SPHERICAL 설명과 적용 표 행이 보존되어 있다. |
| `roms_grid_metrics.md:279` | 현재 노트 95·166줄 인용 | 같은 보고서 2222줄의 반영 전 노트 인용 | RTG-1980에 일반 MPI 검사만 적었던 문장 두 개가 보존되어 있다. |

기계 확인 후보: 이 노트에 지정된 후보는 없다.

## roms_equation_of_state.md — 완료

- 대상: [roms_equation_of_state.md](../../../models/ROMS/source-analysis/roms_equation_of_state.md).
- 대조한 줄 수: 작업 시작 시 `git diff -U0 HEAD`의 추가 32줄이다.
- 대조 범위: 6–7, 22, 28, 40, 66, 77, 92–95, 105, 119–122, 124–139줄이다.
- 정정 수: 3줄이다.
- 보완 수: 2줄이다.
- 차이 표 7행의 분류와 결론은 theory-numerics·inputs 보고서의 최종본과 같다.
- RTN-391의 물리 밀도와 저장 편차 구분을 본문에서 확인했다.
- 표의 원문 인용 93개를 코드와 위키에 대조했다.
- 비선형 밀도·bvf·선형 밀도의 원문을 열어 부호와 단위를 확인했다.
- 링크 변환으로 추가 줄이 된 EFDC 비교 문장도 두 모델의 계수와 주석에 대조했다.
- KPP와 연직혼합 루틴의 `bvf` 입력 선언을 확인했다.
- 압력구배 루틴의 `rho` 입력과 소비를 확인했다.
- frontmatter의 `rho_eos.F` 889줄과 계수·참고문헌 인용 위치를 확인했다.
- 상대 링크 18개는 실제 파일을 가리킨다.
- A·E 행과 mermaid 블록은 없다.
- 대상 추가 줄에는 금지한 한계 문장이 없다.
- 개인 절대 경로와 이중 대괄호 링크는 없다.

| 노트:줄 | 구분 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| `roms_equation_of_state.md:28` | 정정 | 염분항의 적용 조건 없이 선형식을 제시 | 요약식임을 명시하고 SALINITY 조건을 명시 | `ROMS/Nonlinear/rho_eos.F:701–704`는 `#  ifdef SALINITY` 안에서 염분항을 더한다. RTN-194도 같은 조건을 설명한다. |
| `roms_equation_of_state.md:40` | 정정 | 양 모델을 모두 재적합으로 설명하고 “인용은 소스에 없음”이라고 서술 | 계수의 일치를 직접 인용하고 각 소스의 문헌 설명을 구분 | `ROMS/Modules/mod_eoscoef.F:50,56,64`와 `calbuoy.f90:61,128,134`의 계수는 같다. `rho_eos.F:31–35`는 Jackett–McDougall 1995를 인용한다. `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calbuoy.f90:12–14`는 Mellor의 UNESCO 근사를 명시한다. |
| `roms_equation_of_state.md:94` | 보완 | 최종 rho·pden의 기준을 수정안 RTN-391만으로 인용 | rho와 pden의 실제 대입 줄을 추가 | `ROMS/Nonlinear/rho_eos.F:355,476–479,716–720`은 1000 기준 편차와 pden 저장을 보여 준다. |
| `roms_equation_of_state.md:105` | 보완 | pden의 대입 위치와 EFDC 기준밀도 출처가 없는 비교 행 | pden 대입과 EFDC 부력·참조밀도 계산 위치를 추가 | `rho_eos.F:477,720`은 pden을 저장한다. `calbuoy.f90:57–62,137`은 상수 참조온도의 참조밀도와 `B(L,K) = (RHO1/RHOO)-1._8`을 보여 준다. |
| `roms_equation_of_state.md:139` | 정정 | 현재 노트의 27·100줄을 수정 전 문장의 출처로 인용 | `roms-theory-numerics-vs-code.md:711`에 보존된 반영 전 노트 문장으로 출처 변경 | RTN-391 수정안은 선형식과 기존 baseline 행을 보존한다. |

기계 확인 후보: 이 노트에 지정된 후보는 없다.

## roms_analytical_functionals.md — 완료

- 대상: [roms_analytical_functionals.md](../../../models/ROMS/source-analysis/roms_analytical_functionals.md).
- 대조한 줄 수: 작업 시작 시 `git diff -U0 HEAD`의 추가 113줄이다.
- 대조 범위: 7–8, 18–20, 24–27, 64–66, 82–86, 105, 111–119, 121–127, 132–144, 158–163, 173–183, 192, 197–201, 208–215, 221, 240–249, 255–259, 263–281줄이다.
- 정정 수: 2줄이다.
- 보완 수: 2줄이다.
- 본문을 NT-021–022, RBH-3507, RMF1-949–952, DA1-819, RT1-1514–1521·1536의 수정안과 최종 기록에 대조했다.
- `ROMS/Functionals/*.h`의 파일 수는 42개이다.
- 현재 analytical.F에는 ana_vegetation.h의 include 문이 없다.
- ANA별 CPP 조건과 ANANAME 등록 조건을 원문에서 확인했다.
- 바닥·표면 플럭스 단위, BASIN·UPWELLING의 응력 식, 개방경계 acquire 조건을 확인했다.
- respiration의 농도 소비식과 1/day 단위 표기의 차이를 확인했다.
- RIVERPLUME2의 마지막 XI source와 초기 위치 설정 조건을 확인했다.
- ESTUARY_TEST·SED_TOY·LAKE_SIGNELL의 초기값과 호출 조건을 확인했다.
- `46f20897`의 날짜 `2014-03-13`을 확인했다.
- 과거 `0db3bdc5:ROMS/Functionals/ana_hmixcoef.h:171–175`와 현재 ini_hmixcoef의 격자 크기 조정을 대조했다.
- 두 차이 노트의 행 수와 분류 수는 배정표의 134행·133행과 같다.
- 수정 후 상대 링크 24개는 실제 파일을 가리킨다.
- 대상 추가 줄에는 mermaid 블록과 금지한 한계 문장이 없다.
- 개인 절대 경로와 이중 대괄호 링크는 없다.

| 노트:줄 | 구분 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| `roms_analytical_functionals.md:64` | 정정 | initial은 72줄의 인덱스 2, grid는 94·95줄의 인덱스 7·10, perturb는 56줄의 인덱스 48이라고 인용 | initial은 101줄의 `ANANAME(10)=MyFile`, grid는 94줄의 `ANANAME( 7)=MyFile`, perturb는 125줄의 `ANANAME(19)=MyFile`로 정정 | 현재 `ROMS/Functionals/ana_initial.h:101`, `ana_grid.h:94`, `ana_perturb.h:125`의 대입문을 그대로 옮겼다. smflux와 tobc도 실제 대입 줄을 붙였다. |
| `roms_analytical_functionals.md:112` | 보완 | “별도 코드 결함 후보와 연결한다”는 지시 문장 | RMF1-869 링크와 SOLVE3D·SALINITY 조건 및 강함 판정을 명시 | `roms-mixing-bc-forcing-vs-code.md:2025`의 최종 E 결론과 `ROMS/Nonlinear/set_vbc.F:24,363,402`가 근거다. |
| `roms_analytical_functionals.md:173` | 보완 | 함수별 조건 표의 공통 상위 조건을 생략 | 모든 해당 include가 `#ifdef ANALYTICAL` 안에 있음을 명시 | `ROMS/Functionals/analytical.F:84`가 표의 모든 분기를 감싼다. |
| `roms_analytical_functionals.md:281` | 정정 | 배정 디렉터리에 링크하고 부모 노트에 267행을 배정했다고 서술 | 두 배정 파일에 직접 링크하고 각 차이 노트의 134행·133행을 명시 | `note-job-16.tsv`와 `note-job-17.tsv`의 대상 경로·분류를 집계했다. 합계와 분류별 개수는 기존 값과 같다. |

기계 확인 후보 판정:

- `ana_initial.h:72`의 `ANANAME(2)`는 실제 불일치다. 72줄은 `OCEAN(ng) % tl_ubar` 인자다. 등록문은 101줄의 `ANANAME(10)=MyFile`이다. 노트 64줄을 정정했다.
- `ana_perturb.h:56`의 `ANANAME(48)=__FILE__`는 실제 불일치다. 56줄은 MyFile 초기화에 쓰는 `__FILE__`이다. 등록문은 125줄의 `ANANAME(19)=MyFile`이다. 노트 64줄을 정정했다.

## roms-wiki-cppdefs-options.md — 완료

- 대상: [roms-wiki-cppdefs-options.md](../../../models/ROMS/manual-notes/roms-wiki-cppdefs-options.md).
- 대조한 줄 수: 작업 시작 시 `git diff -U0 HEAD`의 추가 88줄이다.
- 대조 범위: 2, 6–7, 19, 21, 25–30, 44–49, 79, 84–86, 121–130, 134–136, 139–141, 144–150, 152–153, 155–157, 160, 165–166, 173, 181, 185–188, 191–197, 199, 201, 203–207, 211–226줄이다.
- 정정 수: 2줄이다.
- 보완 수: 3줄이다.
- 본문을 RBH-3476–3487, NT-016–017, RMF1-963, RTN-400–402·410, RT1-1530–1531, RN1-039–040, DA1-821, 비선형 흐름 N-05의 수정안에 대조했다.
- 위키 3줄의 표시 글자는 두 직접 인용문과 같다.
- 위키 manifest의 cppdefs.h 판 번호는 5862이다.
- 노트가 골라 적은 첫 32개 범주는 위키의 해당 제목 순서와 같다.
- cppdefs의 응용 헤더·globaldefs 포함 순서를 확인했다.
- yaml_parser.F와 get_env.F의 예외를 확인했다.
- ANA_VMIX·LMD_MIXING·BVF_MIXING의 배타적 선택 순서를 확인했다.
- COARE 3.5와 COARE_30의 구분을 확인했다.
- 권장 구성과 사용자 예시는 보고서의 권고 범위 안에 있다.
- 새로 추가한 UV_ADV·UV_COR·MIX_S_UV와 SEDIMENT 정정은 수정안에 부합한다.
- NT-016의 ECB 커밋 `d06fee85`와 날짜 `2025-06-27`은 `ROMS-git-verify-A6.md:18` 및 해당 커밋과 같다.
- `f3cd98c7:ROMS/Include/cppdefs.h:450,466,471,479,484,495`에서 roms-4.2의 생물 모델 묶음을 확인했다.
- 네 차이 노트의 합계 794행과 분류 수는 배정표 집계와 같다.
- 수정 후 상대 링크 40개는 실제 파일을 가리킨다.
- 대상 추가 줄에는 mermaid 블록과 금지한 한계 문장이 없다.
- 개인 절대 경로와 이중 대괄호 링크는 없다.

| 노트:줄 | 구분 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| `roms-wiki-cppdefs-options.md:149` | 보완 | MIX_S_TS의 방향 설명에 직접 인용 없음 | S-coordinate 면을 설명하는 구현 주석 추가 | `ROMS/Nonlinear/t3dmix2_s.h:10–11`은 S-coordinate 면을 따른 추적자 혼합을 명시한다. |
| `roms-wiki-cppdefs-options.md:150` | 보완 | MIX_ISO_TS 선택 파일의 include 위치만 인용 | isopycnic 면을 설명하는 구현 주석 추가 | `ROMS/Nonlinear/t3dmix2_iso.h:10–11`은 isopycnic 면을 따른 혼합을 명시한다. |
| `roms-wiki-cppdefs-options.md:195` | 정정 | Hadvection·Vadvection 입력의 SOLVE3D 조건 생략 | SOLVE3D 조건과 418줄을 명시 | `ROMS/Utility/read_phypar.F:418`의 `#ifdef SOLVE3D`가 419–442줄의 두 입력 분기를 감싼다. RBH-3486도 같은 조건을 명시한다. |
| `roms-wiki-cppdefs-options.md:197` | 보완 | 입력 자료·매개변수 목록에 원문 위치 없음 | DT·VISC2·VISC4·GRDNAME·BRYNAME의 입력 위치 추가 | `ROMS/Utility/read_phypar.F:593–594,839–842,4215–4218,4294–4295`가 각 입력을 처리한다. |
| `roms-wiki-cppdefs-options.md:226` | 정정 | 배정표 디렉터리에 링크 | 실제 `note-job-5.tsv`부터 `note-job-8.tsv`까지의 파일에 직접 링크 | 해당 파일의 차이 노트 배정은 각각 199·199·199·197행이다. 합계와 분류 수는 기존 값과 같다. |

기계 확인 후보: 이 노트에 지정된 후보는 없다.

## 최종 집계

| 노트 | 대조한 대상 줄 수 | 정정 줄 수 | 보완 줄 수 |
|---|---:|---:|---:|
| roms_include_cppdefs-differences-2.md | 258 | 6 | 0 |
| roms_grid_metrics.md | 103 | 6 | 0 |
| roms_equation_of_state.md | 32 | 3 | 2 |
| roms_analytical_functionals.md | 113 | 2 | 2 |
| roms-wiki-cppdefs-options.md | 88 | 2 | 3 |
| 합계 | 594 | 19 | 7 |

대조한 줄 수는 작업 시작 시 고정한 전체 줄과 git diff 추가 줄을 합산했다.
정정·보완 줄 수는 대상 노트의 `[10-14 전수 검증 정정]`·`[10-14 전수 검증 보완]` 태그가 있는 줄을 각각 셌다.
두 종류의 태그가 겹치는 줄은 없다.
모든 정정·보완은 작업 시작 시 대상 줄에 속한다.
작업 전후 대상 노트의 줄 수는 동일하다.
수정한 모든 표 행은 끝 칸 안에 검증 태그를 갖는다.
대상 노트의 상대 링크 104개는 파일과 절 앵커 검사를 통과했다.
현재 코드 판 설명의 4.3은 `ROMS/Modules/mod_ncparam.F:653`의 version 값과 같다.
현재 코드 저장소의 HEAD는 develop 브랜치를 가리킨다.
지정된 기계 확인 후보 2개는 모두 실제 오류로 판정하여 정정했다.
대상 줄의 미해결 항목은 0개이다.
작업 상태: 완료.
