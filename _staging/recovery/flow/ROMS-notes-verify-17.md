# ROMS 노트 전수 대조 17 (2026-10-14)

대상은 `roms_sea_ice.md`, `roms_tidal_forcing.md`, `roms_global_state_modules.md`, `roms_biology.md`, `roms_adjoint_model.md`다.
기존 노트의 대상 줄은 작업 시작 시 `git diff -U0 HEAD -- <노트>`의 추가 줄 전체다.
대조 줄 수에는 frontmatter와 빈 줄을 포함한다.
정정 수와 보완 수는 수정한 대상 줄 수로 센다.
보고서 끝의 전수 검증 기록과 최종 보완을 우선한다.
기계 확인 불일치 후보는 사용자 제공 목록에 없다.

완료한 노트의 결과를 아래에 순서대로 기록한다.

## roms_sea_ice.md — 완료

- 대조한 대상 줄은 178줄이다. 작업 시작 시 diff의 추가 줄을 셌다.
- 정정은 4줄이다. 보완은 2줄이다.
- 차이 표 137행의 분류와 결론은 보고서 §5 최종본과 일치한다. A 17행의 `a4a82c5f 2023-07-01`은 `ROMS-git-verify-A7.md`와 일치한다. E 3행의 강도는 최종 보고서와 일치한다.
- 수정안 RN1-001부터 RN1-007까지의 반영을 대조했다. 현재 코드와 위키의 인용 위치를 열었다. 과거 판 인용은 읽기 전용 `git show`로 열었다. 차이 표의 기존 노트 인용은 변경 전 문장으로 대조했다.
- 대상 줄의 상대 링크 16개는 실제 파일을 가리킨다. Mermaid 블록은 없다. 절대 홈 경로와 이중 대괄호는 없다. 검토를 뒤로 미루는 본문 문장은 없다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `roms_sea_ice.md:6` | 정정 | 파일 인벤토리 `7682 라인` → 부정확한 줄 수 삭제 | 현재 `ROMS/Nonlinear/SeaIce/*.F` 18파일은 7,676줄이다. 같은 디렉터리의 `*.h` 5파일은 4,035줄이다. 파일별 줄 수를 합산했다. |
| `roms_sea_ice.md:40` | 정정 | 표면 열수지에서 융해·적설로 연결 → 융해 계산과 강수에서 얻은 적설 입력을 구분 | `ice_mk.h:519`의 `ws(i,j)=MAX(snow(i,j), 0.0_r8)`와 537–554의 Qsur·눈 융해 계산. 보고서 RIM1-029·RIT1-004·RIV1-075. |
| `roms_sea_ice.md:41` | 보완 | 저면 성장·융해 설명 → `icW_io` 계산 위치 추가 | `ice_mk.h:673–676`의 `(Qio/RhoSW+Cp_w*cht*(T0mk-temp_top))/hfus1`. 보고서 RIO1-014. |
| `roms_sea_ice.md:54` | 보완 | MPDATA 수송 설명 → 직접 출처 추가 | `ice_smolar.h:10–17`의 Smolarkiewicz 수송 설명과 positive-definite 알고리즘 문헌. |
| `roms_sea_ice.md:64` | 정정 | 열·운동량·염 플럭스를 공통 `(1-ai)`로 차단 → 농도 가중과 성장·융해 플럭스에 따른 수정 | `ice_mk.h:738–788`의 열·염 플럭스 식과 `ice_vbc.F:301–310`의 응력 식은 동일한 차단식이 아니다. 보고서 RIO1-010·RIO1-011·RN1-006. |
| `roms_sea_ice.md:77` | 정정 | 연결 설명의 표면 플럭스 차단 → 해빙-해양 결합의 표면 플럭스 수정 | 위 64줄과 같은 원문. |

기계 확인 후보 판정: 후보 없음.
미해결 항목: 없음.

## roms_tidal_forcing.md — 완료

- 대조한 대상 줄은 111줄이다. 작업 시작 시 diff의 추가 줄을 셌다.
- 정정은 2줄이다. 보완은 0줄이다.
- 차이 표 51행의 분류와 결론은 최종 보고서와 일치한다. A 행 RMF1-695의 `d2a88283 2021-09-09`는 `ROMS-git-verify-A7.md:65`와 일치한다. E 행 RMF1-668은 강함이다. RMF1-688은 중간이다. 외부 원문 보고서 끝의 보완과 혼합·경계·강제 보고서의 최종 기록을 함께 대조했다.
- RMF1-934부터 RMF1-938까지와 RTN-396의 본문 수정안을 대조했다. 시간 원점의 일·초 환산, 양수 주기 조건, 타원 성분의 부호, nodal 조건, 평균 구간과 fitting 구간을 원문과 대조했다. Fortran 블록 11줄은 `set_avg.F:5295–5305`와 일치한다.
- frontmatter의 `set_tides.F` 645줄은 현재 파일 줄 수와 같다. 대상 줄의 상대 링크 10개는 실제 파일을 가리킨다. Mermaid 블록은 없다. 절대 홈 경로와 이중 대괄호는 없다. 검토를 뒤로 미루는 본문 문장은 없다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `roms_tidal_forcing.md:45` | 정정 | 파일의 `zero_phase_date`가 있으면 재설정 → `ANA_TIDES` 제외와 세 조석 옵션 중 하나 이상이라는 경로 조건 명시 | `tides_date.F:2–4`의 전처리 조건과 140–173의 날짜 처리. 최종 보고서 RTN-358. |
| `roms_tidal_forcing.md:78` | 정정 | ROMS가 regional 모델이므로 경계 조석을 사용한다는 설명 → 경계·기후장 처리와 평형 조석 압력 항을 구분 | `set_tides.F:301–304,330–347`의 기후장·경계 대입과 `prsgrd32.h:285–286`의 `P(i,j,N(ng))=P(i,j,N(ng))-g*eq_tide(i,j)`. 보고서 RMF1-934. |

기계 확인 후보 판정: 후보 없음.
미해결 항목: 없음.

## roms_global_state_modules.md — 완료

- 대조한 대상 줄은 101줄이다. 작업 시작 시 diff의 추가 줄을 셌다.
- 정정은 7줄이다. 보완은 4줄이다.
- 차이 표 32행의 분류와 결론은 최종 보고서와 일치한다. A 6행의 커밋과 날짜는 A5·A8 및 보고서의 최종 판정과 일치한다. OMD-V065는 최종 기록의 B를 반영했다. OMD-K029를 참조한 본문의 중간 강도도 유지했다.
- NT-024, RBH-3506, DA1-810, RI1-1054, OMD-N031·032·033·049, RT1-1534·1535, RTN-371·372·383·391, N-04·RF1-032의 수정안을 대조했다.
- `ROMS/Modules/*.F` 목록에서 38파일을 확인했다. 선언·할당·단위·시간 인덱스·0번 층 소비·메타데이터 복사 경로를 원문과 대조했다. 과거 판 인용은 읽기 전용 `git show`로 열었다.
- 대상 줄의 상대 링크 48개는 실제 파일을 가리킨다. Mermaid 블록은 없다. 절대 홈 경로와 이중 대괄호는 없다. 대상 본문에 검토를 뒤로 미루는 문장은 없다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `roms_global_state_modules.md:84` | 정정 | ubar 할당 407 → ubar 408·vbar 411 | `mod_ocean.F:407`은 주석 줄이다. 408·411은 각각 3슬롯 할당문이다. 보고서 N-04의 현재 할당 위치 갱신 지시를 적용했다. |
| `roms_global_state_modules.md:87` | 정정 | pden 446·rho 449 → pden 447·rho 450 | `mod_ocean.F:446,449`는 주석 줄이다. 실제 할당은 447·450이다. |
| `roms_global_state_modules.md:92` | 정정 | 모든 2D 변수의 시간레벨이 3개 → zeta·ubar·vbar로 대상을 한정 | `mod_ocean.F:408,411,414`는 3슬롯이다. 399·402·405의 2D 우변 배열은 2슬롯이다. 보고서 N-04. |
| `roms_global_state_modules.md:108` | 정정 | f_t 312·tl_zeta 할당 559·tl_t 할당 606 → 313·560·607 | `mod_ocean.F:313,560,607`의 실제 선언·할당문. DA1-810이 유지하도록 한 상태 컨테이너 설명을 보존했다. |
| `roms_global_state_modules.md:156` | 보완 | pre_step3d의 이전 단계 기여만 인용 → 현재 단계 기여 위치 추가 | `pre_step3d.F:16–19`와 `step3d_uv.F:347–360`. 보고서 RTN-383. |
| `roms_global_state_modules.md:165` | 정정 | nrrec 선언 1192 → 1200 | `mod_scalars.F:1192`는 `#endif`이다. 1200은 `integer, allocatable :: nrrec(:)`이다. |
| `roms_global_state_modules.md:168` | 정정 | ntstart 계산식만 설명 → 계산 후 1 하한을 적용하는 조건 추가 | `get_state.F:436–437`의 계산문과 `IF (ntstart(ng).lt.1) ntstart(ng)=1`. |
| `roms_global_state_modules.md:194` | 보완 | Akv·Akt 선언만 인용 → 0:N과 NAT 차원을 정하는 할당문 추가 | `mod_mixing.F:548,551`의 실제 할당 차원. |
| `roms_global_state_modules.md:198` | 보완 | stflx 선언만 인용 → NT 차원을 정하는 할당문 추가 | `mod_forces.F:929`의 `stflx(LBi:UBi,LBj:UBj,NT(ng))`. |
| `roms_global_state_modules.md:204` | 정정 | `CELERITY_*` → `CELERITY_READ` 또는 `CELERITY_WRITE` | `mod_boundary.F:405–408`의 조건과 선언. 1462의 t_west 할당도 연결했다. |
| `roms_global_state_modules.md:211` | 보완 | 파일 객체의 2차원 선언만 인용 → max_Ffiles·Ngrids 할당 위치 추가 | `read_phypar.F:4283,4321,4373`의 BRY·CLM·FRC 할당. 보고서 OMD-N049. |

기계 확인 후보 판정: 후보 없음.
미해결 항목: 없음.

## roms_biology.md — 완료

- 대조한 대상 줄은 91줄이다. 작업 시작 시 diff의 추가 줄을 셌다.
- 정정은 5줄이다. 보완은 0줄이다.
- 차이 표는 이 파일에 없다. 연결한 두 차이 노트는 존재한다. `ROMS-assign-*.tsv`의 지정 열을 다시 세어 A 2·B 68·C 167·D 2·E 25·F 22, 합계 286행을 확인했다.
- NT-001부터 NT-011까지와 NT-019·025·026 및 RN1-041의 수정안을 대조했다. 기본 추적자 7개, CARBON별 침강 수 6·4, 철 제한별 NBT 6·4, 탈질의 4/16, TIC 상·하한 3000·400은 원문과 일치한다. 입력 소비 여부와 Vadvection 중복의 전처리 조건을 확인했다. UN-012·015의 B와 UN-013·014·016의 E는 최종 보고서와 일치한다.
- frontmatter와 카탈로그의 Fennel 2,375줄·Franks 589줄·Powell 663줄은 현재 파일과 같다. 모델 선택문의 파일·줄과 실제 `#elif` 조건을 대조했다.
- 작업 시작 대상 줄의 상대 링크 53개는 실제 파일을 가리킨다. Mermaid 블록은 없다. 절대 홈 경로와 이중 대괄호는 없다. 검토를 뒤로 미루는 본문 문장은 없다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `roms_biology.md:84` | 정정 | Zeebe–Wolf-Gladrow 또는 pCO2_RZ → pCO2_RZ가 Zeebe–Wolf-Gladrow를 선택하고 기본값은 OCMIP | `fennel.h:38–40`의 설명과 1201–1220의 `pCO2_water_RZ`·`pCO2_water` 호출 분기. |
| `roms_biology.md:114` | 정정 | T/S와 동일한 이류 스킴이라는 포괄 설명 → 공통 수송 루프와 추적자별 스킴 선택을 구분 | `step3d_t.F:405–412,432–472`의 `itrc=1,NT(ng)` 및 `Hadvection(itrc,ng)` 선택. `biology.F:109–126`의 모델별 커널. 보고서 NT-010. |
| `roms_biology.md:115` | 정정 | 모든 생물 모델에 적용하는 침강·PAR 설명 → Fennel의 PPM·WENO 침강과 PAR 광 제한으로 한정 | `fennel.h:1286–1295,1321–1340,701–736`. Franks는 `npzd_Franks.h:319–321`의 지수 광 제한을 사용한다. 보고서 NT-007·NT-019. |
| `roms_biology.md:116` | 정정 | 포괄적인 sediment·carbon 결합 가능 → BIO_SEDIMENT·CARBON의 쇄설물 탄소 복귀 | `fennel.h:1464,1512–1521`의 조건과 `Bio(i,1,iTIC_)=Bio(i,1,iTIC_)+cff1`. 보고서 RN1-041·NT-006의 저층 재광물화 조건을 적용했다. |
| `roms_biology.md:143` | 정정 | 연결 설명의 sediment-bio carbon 결합 → 퇴적물 물리 노트와 Fennel 저층 탄소 경로를 구분 | 위 116줄의 원문. 일반 SEDIMENT 호출은 `main3d.F:1038–1039`의 별도 조건이다. |

기계 확인 후보 판정: 후보 없음.
미해결 항목: 없음.

## roms_adjoint_model.md — 완료

- 대조한 대상 줄은 29줄이다. 작업 시작 시 diff의 추가 줄을 셌다.
- 정정은 1줄이다. 보완은 3줄이다.
- 차이 표 2행의 결론은 생물 보고서 최종본과 일치한다. ES-096은 B이다. CM-097은 E 중간이다. CM-097에 보강된 NPZD_FRANKS 저장 경로도 노트에 포함되어 있다.
- RTN-380, DA1-812, DA 흐름 보고서 §6, RBH-1335의 반영을 대조했다. 역순 루프, 감도 forcing, 관측 호출 분기, 압력 경사 선택, SANITY_CHECK 입력 및 순압 수반 호출을 원문과 대조했다. `316e5450`의 배율 소비 코드와 입력 설명을 읽기 전용 `git show`로 확인했다.
- 대상 줄의 상대 링크 6개는 실제 파일을 가리킨다. Mermaid 블록은 없다. 절대 홈 경로와 이중 대괄호는 없다. 검토를 뒤로 미루는 본문 문장은 없다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `roms_adjoint_model.md:48` | 보완 | obs_read의 697줄만 인용 → ad_htobs·ad_misfit 선택문 709–714 추가 | `ad_main3d.F:710–713`의 `WEAK_CONSTRAINT` 분기와 실제 호출. DA 흐름 보고서 §6. |
| `roms_adjoint_model.md:202` | 보완 | ad_step2d.F 경유 설명 → 실제 포함 헤더와 위치 추가 | `ad_step2d.F:20`의 `# include "ad_step2d_LF_AM3.h"`. |
| `roms_adjoint_model.md:205` | 정정 | `_NOT_YET` 조건을 요구하는 분기라는 설명 → 해당 USE 문이 주석임을 명시 | `ad_main3d.F:51,54,57,119`의 `!! USE` 문. 조건 이름만으로 사용 가능한 모듈 연결을 뜻하지 않는다. |
| `roms_adjoint_model.md:215` | 보완 | ES-096의 문서 근거에 위키만 인용 → 잘못된 키워드를 실제로 쓰는 입력 예제 추가 | `User/External/ecosim.in:552`의 `ad_AKT_BAK == 61*1.0d0`. 생물 보고서 §2의 ES-096(715줄)에 같은 입력 예제가 있다. `ecosim.in.wiki:307`과 `ecosim_inp.h:296`은 모두 ad_AKT_fac를 사용한다. 결론은 유지했다. |

기계 확인 후보 판정: 후보 없음.
미해결 항목: 없음.

## 최종 확인

아래 대상 줄 수는 작업 시작 시 각 노트의 `git diff -U0 HEAD` 추가 줄을 센 값이다. frontmatter와 빈 줄을 포함한다. 정정 수와 보완 수는 각 표시를 붙인 줄 수이다.

| 노트 | 대조한 줄 | 정정 | 보완 |
|---|---:|---:|---:|
| roms_sea_ice.md | 178 | 4 | 2 |
| roms_tidal_forcing.md | 111 | 2 | 0 |
| roms_global_state_modules.md | 101 | 7 | 4 |
| roms_biology.md | 91 | 5 | 0 |
| roms_adjoint_model.md | 29 | 1 | 3 |
| 합계 | 510 | 19 | 9 |

- 대상 510줄의 대조를 완료했다. 정정·보완 표시 28개는 위 목록과 일치한다.
- 차이 표 222행의 분류와 결론은 최종 보고서와 일치한다. A 행의 커밋·날짜와 E 행의 근거 강도도 대조했다.
- 노트별 기록의 링크 수는 수정 전 대상 줄 기준이다. 수정 후 대상 줄의 상대 링크 130개는 모두 실제 파일을 가리킨다.
- 다섯 노트의 frontmatter는 YAML 구문 검사를 통과했다. 차이 표는 모두 6열이다. 대상 파일의 `git diff --check`는 오류 없이 끝났다.
- 대상 줄에는 절대 홈 경로와 이중 대괄호가 없다. 검토를 뒤로 미루는 본문 문장도 없다. 대상 줄에 Mermaid 블록은 없다.
- 기계 확인 후보는 제공되지 않았다. 미해결 항목은 없다.
