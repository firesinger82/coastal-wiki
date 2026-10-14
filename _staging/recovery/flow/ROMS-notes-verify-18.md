# ROMS 노트 전수 검증 18 (10-14)

대상은 사용자 지정 노트 6개이다. 기존 노트의 대상은 검증 시작 시 `git diff -U0 HEAD -- <노트>`의 추가 줄이다. 새 파일 `roms-tools-differences.md`는 전체 줄을 대상으로 한다. 아래 줄 번호와 줄 수는 정정 전 파일을 기준으로 한다. 빈 줄과 frontmatter를 포함한다.

| 노트 | 대상 줄 수 | 대상 줄 번호 |
|---|---:|---|
| `models/ROMS/source-analysis/roms_main_driver_dispatch.md` | 398 | 2, 6, 8, 23, 25–27, 33, 39–40, 45–47, 52–53, 55–63, 69, 71, 73, 76–80, 82–83, 87–92, 94–98, 100, 102, 104–106, 110–111, 114, 119–122, 124, 126–134, 136, 138, 140–146, 148, 150–153, 157–162, 164–474 |
| `models/ROMS/source-analysis/roms_wec.md` | 154 | 6–7, 47–50, 149–156, 171–185, 237–361 |
| `models/ROMS/source-analysis/roms_kpp_boundary_layer.md` | 59 | 6–7, 22, 81–82, 84–85, 89, 91–92, 111–112, 127, 129, 137–139, 141–182 |
| `models/ROMS/manual-notes/roms-wiki-overview.md` | 84 | 6, 8, 32–34, 41, 54–65, 75, 77–79, 98–101, 112–118, 126–127, 137–143, 145, 147–153, 159, 161–165, 167–171, 175–197 |
| `models/ROMS/source-analysis/roms_nonlinear_physics_modules.md` | 47 | 6–7, 28, 56, 58, 74, 84, 107, 116, 118, 120, 122, 128–134, 138, 140–142, 146–154, 157–171 |
| `models/ROMS/manual-notes/roms-tools-differences.md` | 30 | 1–30 |

대상 줄 수 합계는 위 표에서 센 772줄이다. 차이 표 행 수는 대상 줄에서 센 289행이다.

보고서의 `전수 검증 기록 (10-14)`과 외부 자료 보고서의 `Claude 확인과 보완`을 최종 판정으로 적용한다. 정정 수와 보완 수는 수정한 대상 줄 수로 센다. 정정 목록의 위치는 별도 표시가 없으면 정정 전 노트 줄 번호이다.

## 기계 확인 후보 판정

- 사용자 제공 불일치 후보는 없다.

## roms-tools-differences.md 완료

- 대조한 대상 줄은 1–30의 30줄이다. 정정은 0줄이다. 보완은 0줄이다.
- 차이 표 3행의 C 분류와 결론 문장은 `roms-build-options-history-vs-code.md:5751–5753`의 RBH-3400·3401·3402와 일치한다. 같은 보고서의 최종 검증 기록 `6088–6115`도 대조했다.
- 원문 `ROMS/Bin/cpp_clean:35–57`을 열어 제거 패턴, 경로 치환 정규식, 마지막 `&`의 인덱스 조건, 두 `substr` 분기를 대조했다. 정규식과 상수 72가 원문과 일치한다.
- frontmatter의 반영 날짜는 `ROMS-notes-apply-4.md:41–56`과 일치한다. 판본은 위키 `manifest.json`과 코드 저장소의 HEAD 참조 및 빌드 보고서 `5–11`과 대조했다.
- 상대 링크와 `related` 파일이 존재한다. 대상 줄에 `/home/firesinger/`, `[[`, 사용자 지정 한계 문장은 없다.
- 정정 목록은 없다. 기계 확인 불일치 후보는 없다. 미해결 항목은 없다.

## roms_kpp_boundary_layer.md 완료

- 대조한 대상 줄은 시작 표에 기록한 59줄이다. 정정은 0줄이다. 보완은 0줄이다.
- 차이 표 32행의 분류와 결론 문장을 입력 보고서 및 혼합·경계·강제 보고서의 최종 결론과 대조했다. A 분류 1행의 커밋과 날짜는 `ROMS-git-verify-A7.md:64`와 일치한다.
- 현재 원문 `lmd_skpp.F:1–4,249–250,264–271,454–471,483–517,580–623,741–780,831–898`, `lmd_vmix.F:326–415,524–554`, `lmd_swfrac.F:67–81`, `pre_step3d.F:929–944`, `read_phypar.F:5011,5557–5565`, `mod_scalars.F:473,1707–1732,1775–1784`, `ana_smflux.h:11–12`에서 인용 대상 줄을 대조했다.
- 위키 원문 `Vertical_Mixing_Parameterizations.wiki`, `Variables.wiki:1072`, `Jwtype.wiki:12`에서 표의 인용 범위를 대조했다. 부등호, 지수 부호, 계수, 단위, SALINITY·LMD 조건이 원문과 일치한다.
- 과거 원문은 `0db3bdc5:ROMS/Modules/mod_scalars.F:1204–1211`, `2bc0778d:ROMS/Modules/mod_scalars.F:1251`, `fc583754:ROMS/Nonlinear/lmd_swfrac.F:73`, `2d476a69^`와 `2d476a69`의 `ROMS/Modules/mod_scalars.F:375`를 `git show`로 대조했다.
- 본문 수정은 RMF1-923–927의 수정안과 일치한다. `FC(i,k-1)=Ritop-lmd_Ric*Ribot`은 `lmd_skpp.F:486`과 일치한다. κ² 설명은 혼합 보고서 최종 기록 `2276–2278`의 Solano and Fan (2022) 귀속을 따른다.
- frontmatter의 네 파일 줄 수는 현재 원문을 세어 확인했다. 상대 링크가 존재한다. 대상 줄에 `/home/firesinger/`, `[[`, 사용자 지정 한계 문장은 없다.
- 정정 목록은 없다. 기계 확인 불일치 후보는 없다. 미해결 항목은 없다.

## roms_nonlinear_physics_modules.md 완료

- 대조한 대상 줄은 시작 표에 기록한 47줄이다. 정정은 2줄이다. 보완은 0줄이다.
- 차이 표 5행은 NT-014·NT-015, RF1-016·RF1-022, OMD-N029의 최종 분류와 결론 문장을 유지한다. 생물 보고서의 최종 기록 `2211`과 `ROMS-git-verify-D1.md:20`에서 BEC 자료 이력과 계산 분기의 구분을 확인했다.
- `ROMS/Nonlinear/Biology/biology.F:109–127`, `ecb.h:11–12`, `main3d.F:364,600–605,641,999,1035–1039`, `diag.F:211`, `ROMS/Drivers/nl_roms.h:276`, `Numerical_Solution_Technique.wiki:119`의 원문을 대조했다. 본문 호출 순서와 출력 조건이 최종 수정안과 일치한다.
- frontmatter의 하위 디렉터리 6개를 현재 `ROMS/Nonlinear/`에서 확인했다. 연결된 노트와 상대 링크가 존재한다. 대상 줄에 `/home/firesinger/`, `[[`, 사용자 지정 한계 문장은 없다.

| 정정 위치 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:107` | KPP 또는 MY25 활성 시 bulk·bvf 파일들이 혼합을 보완한다. | `bvf_mix` 호출 조건을 `ANA_VMIX`·`LMD_MIXING` 미정의 및 `BVF_MIXING` 정의로 한정했다. | `ROMS/Nonlinear/main3d.F:533–538`의 `# if defined ANA_VMIX`, `# elif defined LMD_MIXING`, `# elif defined BVF_MIXING`, `CALL bvf_mix (ng, tile)`. `ROMS-callflow-nonlinear.md:237`의 3D-pre-34도 같은 조건을 적는다. |
| `models/ROMS/source-analysis/roms_nonlinear_physics_modules.md:129` | KPP·MY25는 Nonlinear 밖의 다른 하위 디렉터리일 수도 있다. | KPP와 MY25의 실제 모듈 파일을 `ROMS/Nonlinear/` 아래 경로로 명시했다. | `lmd_vmix.F:2–3`, `my25_prestep.F:2–3`, `my25_corstep.F:2–3`의 모듈 선언과 CPP 조건. `ROMS-callflow-nonlinear.md:236,250,419–420`의 호출·정의 연결. |

- 정정한 두 줄 끝에 `[10-14 전수 검증 정정]`을 붙였다. 기계 확인 불일치 후보는 없다. 미해결 항목은 없다.

## roms-wiki-overview.md 완료

- 대조한 대상 줄은 시작 표에 기록한 84줄이다. 정정은 3줄이다. 보완은 0줄이다.
- 차이 표 5행의 분류와 결론은 RT2-404·RT2-405, OMD-N040, RTN-404, RTG-1982의 최종본과 일치한다. `ROMS-notes-apply-9.md:49`에 열거한 수정안 14개의 본문 반영을 대조했다.
- `Standard_Output.wiki:1–2`, `Standard_Output_Files.wiki:1–7`, `Standard_Output_File.wiki:1`, `easygrid.wiki:3`, `IS4DVAR.wiki:1`을 열어 로그·색인·Matlab·리다이렉트 설명을 대조했다. 이론 쪽과 RBL4D-Var 쪽의 파일 및 제목을 확인했다.
- `i4dvar_roms.h:292–314`, `r4dvar_roms.h:293–323`, `rbl4dvar_roms.h:295–325`를 열어 외부 반복과 background 호출 위치를 대조했다. `Master/roms_kernel.F:159–162`와 `set_depth.F:222`도 표의 인용과 일치한다.
- frontmatter의 326쪽과 수집 날짜는 `manifest.json`과 일치한다. Markdown 파일 수는 `models/ROMS/raw/manuals/wiki/markdown/*.md`에서 센 321개와 일치한다. Options 링크의 절 식별자까지 확인했다.

| 정정 위치 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `models/ROMS/manual-notes/roms-wiki-overview.md:54` | 수집 파일로 `R4DVAR.md`를 열거했다. | 실제 I4DVAR 설명 문서와 두 옵션의 Options 원 절을 연결했다. | 수집 디렉터리에 `R4DVAR.md`가 없다. `I4DVAR.wiki:1`은 Incremental 4D-Var 제목이다. `Options.wiki:1399–1400,2538–2539`에 I4DVAR·R4DVAR 절이 있다. DA1-820의 원 절 연결 수정안. |
| `models/ROMS/manual-notes/roms-wiki-overview.md:56` | `FT_EIGENMODES.md`·`FSV_DRIVER.md`와 `Options.wiki#FSV_DRIVER`를 열거했다. | AFT_EIGENMODES·FT_EIGENMODES·FORCING_SV의 실제 Options 절을 연결했다. | 해당 두 Markdown 파일과 FSV_DRIVER 절이 없다. `Options.wiki:123–127,1288–1295,1342–1349`에 실제 세 절이 있다. DA1-820의 원 절 연결 수정안. |
| `models/ROMS/manual-notes/roms-wiki-overview.md:57` | `BG_NORMALIZATION.md`·`CORRELATION.md`와 `Options.wiki#BG_NORMALIZATION`를 열거했다. | 실제 정규화 Tutorial과 CORRELATION 절을 연결했다. | 해당 두 Markdown 파일과 BG_NORMALIZATION 절이 없다. `4DVar_Normalization_Tutorial.wiki:11–15`는 정규화 설명이다. `Options.wiki:794–801`은 상관 드라이버 옵션이다. |

- 정정한 세 줄 끝에 `[10-14 전수 검증 정정]`을 붙였다. 상대 링크가 실제 파일을 가리킨다. 대상 줄에 `/home/firesinger/`, `[[`, 사용자 지정 한계 문장은 없다. 기계 확인 불일치 후보는 없다. 미해결 항목은 없다.

## roms_wec.md 완료

- 대조한 대상 줄은 시작 표에 기록한 154줄이다. 정정은 3줄이다. 보완은 0줄이다.
- 차이 표 116행의 분류를 최종 보고서와 대조했다. A 분류 61행의 커밋·날짜 조합 6개는 해당 보고서와 git 판정에 일치한다. E 분류 3행의 근거 강도는 모두 강함으로 일치한다.
- 본문 수정안 RBH-3508, RT1-1527, RCN-1973–1976을 대조했다. `main3d.F:392–405`의 첫 단계 제외·격자 인덱스 조건과 `mct_roms_swan.h:324–575`의 변환·송신 분기가 본문과 일치한다.
- 표가 인용한 현재 코드와 위키 범위를 모두 열었다. `read_phypar.F`, `read_stapar.F`, `varinfo.yaml`, `esmf_roms.h`, `esmf_wav.F`에서 삭제된 선택자·메타데이터·CASE의 부재도 검색했다. 과거 인용은 해당 커밋과 부모 커밋의 `git show`로 대조했다.
- 과거 판 대조에는 `roms-4.1`, `roms-4.2`, `f4ef852c`, `df538798`과 그 부모, `57c231d3`, `f1d9e8e^`, `1cbc67d8^`를 사용했다. SHOREFACE의 과거 옵션과 현재 `WEC_VF` 옵션이 구별되어 있다.
- 아래 세 결론은 보고서 문장과 같았으나 같은 행의 현행 코드 인용과 모순되었다. 현행 원문과 `ROMS-git-verify-A8.md:23,27,32`를 기준으로 문자열을 정정했다. A 분류와 `df538798`의 날짜는 유지했다.

| 정정 위치 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `models/ROMS/source-analysis/roms_wec.md:351` · OMD-SN484 | u_stokes의 현행 문자열은 `sea_water_wave_stokes_drift_x_velocity`이다. | 현행 문자열은 `sea_water_stokes_x_velocity`이다. | `ROMS/External/varinfo.yaml:2471–2472`. `f4ef852c:ROMS/External/varinfo.yaml:1665–1666`은 변경 전 문자열이다. 출력 보고서 `3778`의 결론이 같은 행의 현행 인용과 모순된다. |
| `models/ROMS/source-analysis/roms_wec.md:355` · OMD-SN513 | vbar_stokes의 현행 문자열은 `sea_surface_barotropic_wave_stokes_drift_y_velocity`이다. | 현행 문자열은 `sea_water_barotropic_stokes_y_velocity`이다. | `ROMS/External/varinfo.yaml:2438–2439`. `f4ef852c:ROMS/External/varinfo.yaml:1643–1644`는 변경 전 문자열이다. 출력 보고서 `3782`의 결론이 같은 행의 현행 인용과 모순된다. |
| `models/ROMS/source-analysis/roms_wec.md:358` · OMD-SN538 | v_stokes의 현행 문자열은 `sea_water_wave_stokes_drift_y_velocity`이다. | 현행 문자열은 `sea_water_stokes_y_velocity`이다. | `ROMS/External/varinfo.yaml:2482–2483`. `f4ef852c:ROMS/External/varinfo.yaml:1687–1688`은 변경 전 문자열이다. 출력 보고서 `3787`의 결론이 같은 행의 현행 인용과 모순된다. |

- 정정한 세 행의 결론 문장 칸 끝에 `[10-14 전수 검증 정정]`을 붙였다. 상대 링크가 존재한다. 대상 줄에 `/home/firesinger/`, `[[`, 사용자 지정 한계 문장은 없다. 기계 확인 불일치 후보는 없다. 미해결 항목은 없다.

## roms_main_driver_dispatch.md 완료

- 대조한 대상 줄은 시작 표에 기록한 398줄이다. 정정은 원래 대상 줄 기준 4줄이다. 보완은 0줄이다. 원래 219줄의 연결 하나를 연결 세 줄로 고쳤다.
- 차이 표 128행의 분류와 결론은 최종 보고서와 일치한다. 분류별 행 수는 노트의 표에서 센 A 15행, B 56행, C 47행, E 2행, F 8행이다. A 행의 커밋·날짜를 git 판정과 대조했다. E 두 행의 근거 강도는 강함으로 일치한다.
- `ROMS-notes-apply-15.md:30–36`에 기록한 본문 수정안과 참조 연결을 대조했다. 드라이버 선택 조건, R4DVAR의 강제약·약제약 범위, IS4DVAR 호환 이름, 응용 헤더 입력 경로, MCT·native ESMF·CMEPS 진입 조건이 최종 수정안과 일치한다.
- frontmatter의 Drivers 파일 수는 전체 46개와 헤더 41개로 구분되어 있다. 현재 디렉터리의 파일명 목록과 대조했다. HESSIAN_FSV의 include 대상 파일 부재도 확인했다.
- 표와 본문이 인용한 현재 코드·위키·과거 커밋의 원문을 열었다. `Master/`의 자료형·문자열 길이·수신 CASE·회전 식·플럭스 부호·시각 조건·출력 조건을 대조했다. `ESM/coupling_esmf.dat`의 삭제 전 메타데이터는 `d2530aaa^` 원문과 대조했다.
- 부재 주장은 해당 구현 범위에서 별도로 검색했다. native ROMS cap에 표가 열거한 해빙 수신·송신 CASE가 없다. 현재 MCT 소스에는 `ROMS_import_mod`·`ROMS_export_mod`의 USE만 있다. CMEPS cap은 `forecast_length`·`coupling_step` YAML 키를 직접 읽지 않는다.
- E 근거인 `Master/mod_esmf_esm.F:3189–3202`와 `Master/mct_roms_wrf.h:501–516`을 주변 조건까지 열었다. 전자는 destination PETlist를 source nPETs만큼 복사한다. 후자는 BULK_FLUXES 비활성 heat 호출에서 A 다음 쉼표가 없다.
- 수정 전 Mermaid 블록 3개는 호출 흐름 보고서 §4와 동일했다. 상자의 원문 위치 329곳을 대조했다. 아래 정정 후 첫 블록만 보고서와 달라진다. 둘째·셋째 블록은 보고서와 같다.

| 정정 위치 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `models/ROMS/source-analysis/roms_main_driver_dispatch.md:172` | 기본 nl_roms.h 단독 실행으로만 그림 범위를 설명했다. | 그림에 인용한 step2d 호출이 속한 Legacy 조건을 명시했다. 두 FB 옵션이 모두 거짓인 경로이다. | `ROMS/Nonlinear/main3d.F:665,716,810–819`과 `main2d.F:426,458,519–527`의 두 FB 분기 뒤 ELSE. 그림의 호출 위치는 각각 `main3d.F:848,897`과 `main2d.F:551,599`이다. |
| `models/ROMS/source-analysis/roms_main_driver_dispatch.md:204` | `Utility/output.F:191,392,499,692`에 모든 출력 정의 호출을 묶었다. | `Nonlinear/output.F:191,217`의 history 정의·쓰기 순서로 고쳤다. | `ROMS/Utility/output.F`는 없다. `ROMS/Nonlinear/output.F:191`은 `CALL def_his (ng, NewFile)`이다. `:217`은 `CALL wrt_his (ng, tile)`이다. 보고서 `ROMS-callflow-nonlinear.md:1915`에도 같은 경로 오기가 있다. |
| `models/ROMS/source-analysis/roms_main_driver_dispatch.md:205` | `Utility/output.F:217,424,519,703`에 모든 출력 쓰기 호출을 묶었다. | 실제 Nonlinear 경로에서 quicksave·average·restart의 파일별 정의·쓰기 순서로 고쳤다. | `ROMS/Nonlinear/output.F:392,424,499,519,692,703`은 차례로 `def_quick`, `wrt_quick`, `def_avg`, `wrt_avg`, `def_rst`, `wrt_rst` 호출이다. 보고서 `ROMS-callflow-nonlinear.md:1916`의 정의·쓰기 묶음과 경로도 원문에 맞지 않는다. |
| `models/ROMS/source-analysis/roms_main_driver_dispatch.md:219` | 남은 시간 단계마다 시각 증가 상자에서 ntimesteps로 돌아갔다. | STEP_LOOP 안의 다음 단계는 main3d 또는 main2d의 단계 앞 처리로 연결했다. STEP_LOOP가 끝난 뒤 다음 격자 층·바깥 반복만 ntimesteps로 연결했다. | `ROMS/Nonlinear/main3d.F:194–235,1173–1177`과 `main2d.F:116–150,736–740`. ntimesteps는 STEP_LOOP 앞의 NEST_LAYER에 있다. 보고서 `ROMS-callflow-nonlinear.md:198,300`의 반복문 설명도 이 위치와 일치한다. |

- Mermaid 정정 표시는 구문을 유지하도록 바뀐 상자·화살표의 표시 글자 끝에 넣었다. 원래 219줄을 대체한 세 연결에도 각각 표시했다. 본문 정정 표시는 문장 끝에 넣었다.
- Mermaid 3개를 로컬 Mermaid와 JSDOM으로 메모리에서 SVG 렌더링했다. 각 SVG의 상자·연결 수는 각각 36·41, 53·57, 28·29이다. 파싱 오류와 좌표가 잘못된 상자는 없다. 이 수는 렌더링한 SVG의 `.node`·`.flowchart-link` 요소에서 셌다.
- 상대 링크가 존재한다. 대상 줄에 `/home/firesinger/`, `[[`, 사용자 지정 한계 문장은 없다. 기계 확인 불일치 후보는 없다. 미해결 항목은 없다.

## 최종 집계

| 노트 | 대조한 대상 줄 수 | 정정 수 | 보완 수 |
|---|---:|---:|---:|
| `roms_main_driver_dispatch.md` | 398 | 4 | 0 |
| `roms_wec.md` | 154 | 3 | 0 |
| `roms_kpp_boundary_layer.md` | 59 | 0 | 0 |
| `roms-wiki-overview.md` | 84 | 3 | 0 |
| `roms_nonlinear_physics_modules.md` | 47 | 2 | 0 |
| `roms-tools-differences.md` | 30 | 0 | 0 |
| 합계 | 772 | 12 | 0 |

- 위 집계는 검증 시작 시 대상 줄을 기준으로 한다. 주 실행 흐름도의 한 연결을 세 연결로 고쳐 현재 대상 diff와 새 파일의 줄 수 합계는 774줄이다. 정정 표시가 있는 현재 줄은 14줄이다.
- 차이 표 289행의 분류는 최종 보고서와 일치한다. 결론 문장의 실질적인 차이는 WEC의 standard_name 정정 3행이다. 커밋 날짜·인용 표시·보고서 링크를 정규화한 뒤 남은 다른 문자열 차이는 E 강도 명시와 상대 링크 경로이다.
- 대상 줄의 상대 파일 링크가 모두 존재한다. A 행의 날짜와 E 행의 근거 강도 표기가 모두 있다. 사용자 지정 금지 문자열과 한계 문장은 없다. 대상 파일에 대한 읽기 전용 `git diff --check HEAD -- ...`를 통과했다.
- 여섯 노트의 대상 줄 대조를 완료했다. 기계 확인 불일치 후보는 없다. 미해결 항목은 없다.
