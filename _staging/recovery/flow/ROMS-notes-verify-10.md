# ROMS 노트 전수 대조 기록 10

검증일: 2026-10-14.

대상은 `models/ROMS/README.md`, `models/ROMS/source-analysis/roms_support_modules.md`, `models/ROMS/source-analysis/roms_include_cppdefs.md`, `models/ROMS/source-analysis/roms_io_netcdf.md`이다.

기존 노트의 대조 범위는 검증 시작 시 `git diff -U0 HEAD -- <노트>`의 모든 추가 줄이다. 새 파일의 대조 범위는 전체 줄이다. 대조 줄 수에는 frontmatter와 빈 줄을 포함한다. 정정 수와 보완 수는 수정한 대상 줄 수로 센다.

기계 확인 불일치 후보: 사용자가 제시한 후보는 없다.

노트별 완료 기록은 아래에 순서대로 덧붙인다.

## models/ROMS/README.md — 완료

- 대조한 대상 줄: 234줄. 시작 시 diff의 추가 줄을 셌다.
- 대상 줄 범위: 1–8, 18–19, 21–22, 26, 34, 41–44, 51–254, 256, 258–268.
- 정정: 31줄. 보완: 0줄. 아래 정정 목록의 행 수를 셌다.
- 일반 차이 표의 RBH-3512는 최종 보고서의 B 분류와 같다. 코드 루트에서 직접 센 `*.F`는 552개이다. `*.h`는 398개이다.
- 결함 후보 표의 157개 ID는 배정표의 E 행 집합과 같다. 각 행의 최종 분류와 강도를 보고서 결론 및 끝 검증 기록과 대조했다.
- 코드 위치 칸의 원문 위치 4,800개를 열었다. 이 수는 중복 인용을 포함한다. 결론의 적용 조건·부정·수량·단위를 최종 결론과 대조했다. 정정 행의 핵심 식과 조건은 원문에서 별도로 확인했다.
- 본문 수정안은 apply-14의 README 배정 기록과 보고서의 해당 수정안에 대조했다. frontmatter의 반영 날짜, 코드 HEAD, 위키 수집 날짜, 파일 수의 집계 범위를 확인했다.
- 대상 상대 링크는 모두 존재한다. 대상 줄에 Mermaid 블록은 없다. 노트에 사용자 홈 절대 경로, 이중 대괄호, 지정한 작업 한계 문장은 없다.
- 기계 확인 후보 판정: 후보 없음.

### 정정 목록

줄 번호는 정정 후 노트를 기준으로 한다. 이번 정정은 줄 수를 바꾸지 않았다. 표의 원문 경로는 `models/ROMS/raw/source_code/roms/`를 기준으로 한다.

| 노트:줄 | 전 | 후 | 근거 원문·최종 보고서 |
|---|---|---|---|
| README.md:91 | 내용 한 문장은 각 보고서의 최종 결론 문장에서 옮겼다. | 결론 문장은 각 보고서의 최종 결론에 근거한다. | 결함 설명 복원으로 여러 문장을 사용한 아래 행 |
| README.md:95 | 내용 한 문장 | 결론 문장 | 같은 표의 결론 문장 칸 |
| README.md:120 (biology:UN-006) | BIO_FENNEL 및 SOLVE3D를 켠 출력에서 fennel의 K_Phy는 농도 제곱 단위이다. | BIO_FENNEL 및 SOLVE3D를 켠 출력에서 fennel의 K_Phy는 농도 제곱 단위이다. day-1을 기록하는 출력 메타데이터는 결함 후보이다. | ROMS/Nonlinear/Biology/fennel_mod.h:135 `(mmol_N/m3)^2`; fennel_def.h:105 `Vinfo( 3)='day-1'`. [최종 결론](../compare/roms-biology-vs-code.md)의 UN-006. |
| README.md:121 (biology:UN-007) | ECB 및 SOLVE3D를 켠 출력에서 ecb의 K_Phy는 농도 제곱 단위이다. | ECB 및 SOLVE3D를 켠 출력에서 ecb의 K_Phy는 농도 제곱 단위이다. day-1을 기록하는 출력 메타데이터는 결함 후보이다. | ROMS/Nonlinear/Biology/ecb_mod.h:149 `(mmol_N/m3)^2`; ecb_def.h:107 `Vinfo( 3)='day-1'`. [최종 결론](../compare/roms-biology-vs-code.md)의 UN-007. |
| README.md:122 (biology:UN-008) | BIO_FENNEL 및 SOLVE3D를 켠 출력에서 Fennel의 CoagR는 농도 역수와 시간 역수의 단위를 갖는다. | BIO_FENNEL 및 SOLVE3D를 켠 출력에서 Fennel의 CoagR는 농도 역수와 시간 역수의 단위를 갖는다. day-1만 기록하는 출력 단위는 결함 후보이다. | ROMS/Nonlinear/Biology/fennel.h:987 `fac1=dtdays*CoagR(ng)`; fennel_def.h:248 `Vinfo( 3)='day-1'`. [최종 결론](../compare/roms-biology-vs-code.md)의 UN-008. |
| README.md:126 (biology:CF-078) | BioIter가 양수이고 유한한 양의 세균 성장 증가량이 있어도 이 블록의 분배량은 0이 되는 E 강함 후보이다. | NONLINEAR·BIOLOGY 조건에서 ECOSIM이 선택될 때의 계산이다. ECOSIM은 세균 원소별 Bio_new를 자기 자신만큼 빼서 먼저 0으로 만든다. 뒤의 fecal·DOM·무기물 분배식은 그 0이 된 값을 다시 사용한다. BioIter가 양수이고 유한한 양의 세균 성장 증가량이 있어도 이 블록의 분배량은 0이 되는 E 강함 후보이다. | ROMS/Nonlinear/Biology/ecosim.h:1943–1948의 Bio_new 자기 차감과 후속 분배식. [최종 결론](../compare/roms-biology-vs-code.md)의 CF-078. |
| README.md:127 (biology:CF-079) | BioIter가 양수이고 Regen_flag=F이면 미대입 지역 배열을 읽는 E 강함 후보이다. | NONLINEAR·BIOLOGY 조건에서 ECOSIM이 선택될 때의 계산이다. ECOSIM은 Regen_flag가 참일 때만 지역 Regen_C·Regen_N·Regen_S·Regen_P·Regen_F 배열을 대입한다. 뒤의 fecal 재광물화 루프에는 같은 가드가 없다. BioIter가 양수이고 Regen_flag=F이면 미대입 지역 배열을 읽는 E 강함 후보이다. 입력 후처리의 RegCR 등 매개변수 0 대입은 이 지역 배열을 초기화하지 않는다. | ROMS/Nonlinear/Biology/ecosim.h:485 `IF (Regen_flag(ng)) THEN`; :491–495의 대입; :2028의 Regen_C 소비. [최종 결론](../compare/roms-biology-vs-code.md)의 CF-079. |
| README.md:133 (build-options-history:RBH-3048) | roms_kernel.F가 RBL4DVAR 비분할 드라이버를 선택하고 MODEL_COUPLING이 없는 구성에서 increment 다음에 analysis를 호출한다. | roms_kernel.F가 RBL4DVAR 비분할 드라이버를 선택하고 MODEL_COUPLING이 없는 구성에서 increment 다음에 analysis를 호출한다. FRC_FILE·FORWARD_FLUXES가 정의되고 CORRELATION이 없을 때, FRC_FILES 오기 때문에 LreadFRC를 참으로 복원하는 줄이 제외될 수 있다. analysis_initialize가 initial을 호출하면 거짓으로 남은 LreadFRC가 check_multifile의 FRC 처리를 막는 후보이다. 최초 시작에서는 mod_scalars의 FRC_FILE 초기값이 반대 근거다. | ROMS/Drivers/rbl4dvar.F:2259 `# ifdef FRC_FILES`; ROMS/Utility/check_multifile.F:183 `IF (LreadFRC(ng)) THEN`. [최종 결론](../compare/roms-build-options-history-vs-code.md)의 RBH-3048. |
| README.md:134 (build-options-history:RBH-3049) | FT_EIGENMODES는 PROPAGATOR를 정의하고 inp_par를 거쳐 NCV 입력 검사에 도달한다. | FT_EIGENMODES는 PROPAGATOR를 정의하고 inp_par를 거쳐 NCV 입력 검사에 도달한다. FT_EIGENMMODES와 AFT_EIGENMODES가 없는 FT_EIGENMODES 경로는 오기 때문에 `IF (NCV.lt.(2*NEV+1)) THEN` 대신 `IF (NCV.lt.NEV) THEN`을 선택한다. 입력 검사 조건 누락 후보이다. AFT_EIGENMODES 경로에는 같은 누락을 적용하지 않는다. | ROMS/Utility/read_phypar.F:635 `# if defined FT_EIGENMMODES \|\| defined AFT_EIGENMODES`; :636·643의 서로 다른 NCV 검사. [최종 결론](../compare/roms-build-options-history-vs-code.md)의 RBH-3049. |
| README.md:135 (build-options-history:RBH-3134) | NO_SCORRECTION_ICE·ICE_MODEL·SOLVE3D 조건은 checkdefs.F의 설명 출력과 Coptions 기록에 있다. | NO_SCORRECTION_ICE·ICE_MODEL·SOLVE3D 조건은 checkdefs.F의 설명 출력과 Coptions 기록에 있다. 현재 계산 코드에는 NO_SCORRECTION_ICE를 검사하는 줄이 없다. NONLINEAR·SOLVE3D·SALINITY·SCORRECTION 경로의 set_vbc는 이 옵션과 무관하게 염분 보정 항을 포함한다. 보고된 옵션과 계산 조건의 불일치 후보이다. SCORRECTION과 SRELAXATION이 없는 구성에는 보정 생략의 효과 차이를 주장하지 않는다. | ROMS/Utility/checkdefs.F:1940의 NO_SCORRECTION_ICE 조건; ROMS/Nonlinear/set_vbc.F:377 `#   if defined SCORRECTION`. [최종 결론](../compare/roms-build-options-history-vs-code.md)의 RBH-3134. |
| README.md:136 (build-options-history:RBH-3166) | SOLVE3D와 WEC_ROLLER가 정의된 wec_roller.F는 Wave_break 인수 선택에서 `# if defined ROLLER_SVENDSEN \|\| ROLLER_MONO`를 쓴다. | SOLVE3D와 WEC_ROLLER가 정의된 wec_roller.F는 Wave_break 인수 선택에서 `# if defined ROLLER_SVENDSEN \|\| ROLLER_MONO`를 쓴다. ROLLER_MONO는 값으로 검사되지만 계산 분기는 `# elif defined ROLLER_MONO`를 쓴다. ROLLER_SVENDSEN 없이 ROLLER_MONO를 빈 매크로나 0으로 정의하면 인수 조건과 계산 조건이 맞지 않는 후보이다. 값 1이면 두 조건이 맞는다. main3d.F의 NONLINEAR·SOLVE3D·WEC_VF·WEC_ROLLER 경로가 wec_roller를 호출한다. | ROMS/Nonlinear/WEC/wec_roller.F:83의 `defined ROLLER_SVENDSEN \|\| ROLLER_MONO`; :229의 `defined ROLLER_MONO`. [최종 결론](../compare/roms-build-options-history-vs-code.md)의 RBH-3166. |
| README.md:137 (build-options-history:RBH-3208) | ADJOINT·FOUR_DVAR·MULTI_SCALE_B 경로에서 ad_convolution_multi.h의 `#ifndef SOLV3D`는 SOLVE3D를 검사하지 않는다. | ADJOINT·FOUR_DVAR·MULTI_SCALE_B 경로에서 ad_convolution_multi.h의 `#ifndef SOLV3D`는 SOLVE3D를 검사하지 않는다. SOLV3D가 없으면 3차원 구성에도 ad_ubar·ad_vbar의 면적 정규화가 포함된다. 같은 파일의 앞선 2차원 필터와 접선형 정규화는 SOLVE3D를 검사한다. 조건 오기에 따른 추가 연산 후보이다. 2차원 구성에는 같은 차이를 적용하지 않는다. | ROMS/Adjoint/ad_convolution_multi.h:1163 `#ifndef SOLV3D`; :1178·1189의 ad_ubar·ad_vbar 정규화. [최종 결론](../compare/roms-build-options-history-vs-code.md)의 RBH-3208. |
| README.md:138 (build-options-history:RBH-3214) | FOUR_DVAR 또는 VERIFICATION, OBSERVATIONS, WEAK_CONSTRAINT가 정의되고 RPCG가 없는 초기화 경로는 `#   if !defined RPCG && !defined SPLIT_EXCUTABLE`를 검사한다. | FOUR_DVAR 또는 VERIFICATION, OBSERVATIONS, WEAK_CONSTRAINT가 정의되고 RPCG가 없는 초기화 경로는 `#   if !defined RPCG && !defined SPLIT_EXCUTABLE`를 검사한다. SPLIT_EXECUTABLE의 정의는 이 오기 조건을 끄지 못하므로 cg_pxsave 할당이 남는다. 불필요한 할당 후보이다. cg_pxsave 선언은 존재하므로 미선언 변수 오류로 판정하지 않는다. | ROMS/Modules/mod_fourdvar.F:2431 `#   if !defined RPCG && !defined SPLIT_EXCUTABLE`; :2434의 cg_pxsave 할당. [최종 결론](../compare/roms-build-options-history-vs-code.md)의 RBH-3214. |
| README.md:139 (build-options-history:RBH-3285) | NONLINEAR·SOLVE3D의 step3d_uv는 u3dbc_tile을 호출한다. | NONLINEAR·SOLVE3D의 step3d_uv는 u3dbc_tile을 호출한다. 남쪽 gradient 경계의 습윤 마스크 곱셈은 WET_DRY 대신 WET_MASK를 검사한다. WET_DRY만 정의한 구성에서는 이 곱셈이 제외되는 코드 결함 후보이다. | ROMS/Nonlinear/u3dbc_im.F:487의 남쪽 gradient 분기; :496 `# ifdef WET_MASK`; :498의 umask_wet 곱셈. [최종 결론](../compare/roms-build-options-history-vs-code.md)의 RBH-3285. |
| README.md:155 (callflow-nonlinear:RF1-004) | VEGETATION과 VEG_HMIXING을 함께 정의한 비선형 구성은 vegetation_hmixing_mod를 요구한다. | VEGETATION과 VEG_HMIXING을 함께 정의한 비선형 구성은 vegetation_hmixing_mod를 요구한다. 해당 모듈과 vegetation_hmixing_cal 정의는 동봉 소스에 없다. hmixing의 호출은 SOLVE3D와 수평 혼합 계수 조건도 요구한다. VEG_HMIXING은 VISC_3DCOEF를 정의한다. 조건부 빌드 결함 후보를 E 중간으로 유지한다. | ROMS/Nonlinear/hmixing.F:64의 `USE vegetation_hmixing_mod`; :85의 호출; ROMS/Include/globaldefs.h:1252의 VISC_3DCOEF 정의; 동봉 소스의 해당 MODULE·SUBROUTINE 정의 검색 결과 0개. [최종 결론](ROMS-callflow-nonlinear.md)의 RF1-004. |
| README.md:162 (da-4dvar:DA1-411) | WEAK_CONSTRAINT·CLIPPING·RPCG를 정의하고 ARRAY_MODES 분기를 선택하지 않으면 rep_clip에 Ninner-1을 전달한다. | WEAK_CONSTRAINT·CLIPPING·RPCG를 정의하고 ARRAY_MODES 분기를 선택하지 않으면 rep_clip에 Ninner-1을 전달한다. 이때 zu 배열 길이보다 큰 Ninner 인덱스를 쓰는 결함 후보가 있다. | ROMS/Drivers/array_modes.h:1461의 `Ninner-1` 전달; ROMS/Utility/array_modes.F:259의 `dimension(NinnLoop) :: zu`; :276–296의 Ninner까지 순회와 zu(ivec) 대입. [최종 결론](../compare/roms-da-4dvar-vs-code.md)의 DA1-411. |
| README.md:182 (inputs:RI1-0670) | Vtransform과 Vstretching의 전단 검사는 0을 허용한다. | Vtransform과 Vstretching의 전단 검사는 0을 허용한다. SOLVE3D의 수직 좌표 계산에는 0에 대응하는 분기가 없으므로 허용값 검사 결함 후보이다. | ROMS/Utility/read_phypar.F:985·997의 `.lt.0` 검사; ROMS/Nonlinear/set_depth.F:147·192의 1·2 분기; ROMS/Utility/set_scoord.F:184·240·322·393·486의 1–5 분기. [최종 결론](../compare/roms-inputs-vs-code.md)의 RI1-0670. |
| README.md:186 (inputs:RI1-0984) | FLOATS에서 Lfloats(ng)가 TRUE이고 Fprint(ng)가 FALSE이면 NFLOATS 합계 검사를 건너뛰지만 입자 전개는 계속된다. | FLOATS에서 Lfloats(ng)가 TRUE이고 Fprint(ng)가 FALSE이면 NFLOATS 합계 검사를 건너뛰지만 입자 전개는 계속된다. 합계가 큰 입력의 검사 누락은 결함 후보이다. | ROMS/Utility/read_fltpar.F:188 `IF (Lfloats(ng).and.Fprint(ng)) THEN`; :189의 Nfloats 합계 검사. [최종 결론](../compare/roms-inputs-vs-code.md)의 RI1-0984. |
| README.md:192 (outputs-metadata:OMD-Y217) | v_stokes의 YAML type은 df538798의 블록 재배치에서 u3dvar가 됐다. | v_stokes의 YAML type은 df538798의 블록 재배치에서 u3dvar가 됐다. 실제 이력 출력 격자는 v격자이다. def_his의 호출 조건은 `#if defined WEC_VF && defined SOLVE3D`이다. globaldefs는 WEC_VF에서 WEC를 정의한다. 출력 선택은 `IF (VarOut(idV3Sd,ng)) THEN`이다. 쓰기 루틴은 `gtype=gfactor*v3dvar`를 명시한다. YAML type의 모순을 배열 쓰기 실패로 확대하지 않는다. | ROMS/External/varinfo.yaml:2489 `type:           u3dvar`; ROMS/Nonlinear/WEC/wec_output.F:1783 `gtype=gfactor*v3dvar`. [최종 결론](../compare/roms-outputs-metadata-vs-code.md)의 OMD-Y217. |
| README.md:214 (outputs-metadata:OMD-Y652) | marsh_flux_out_의 클래스 생성은 standard_name 슬롯을 채우지 않는다. | marsh_flux_out_의 클래스 생성은 standard_name 슬롯을 채우지 않는다. 출력부는 그 슬롯을 소비한다. 생성은 SEDIMENT 또는 BBL_MODEL의 포함부 안에서 VEGETATION이 있고 NST가 양수일 때 해당 marsh_flux_out_ 이름 조건으로 실행한다. 출력 소비에는 VEGETATION, SOLVE3D, MARSH_DYNAMICS, MARSH_WAVE_THRUST, MARSH_SED_EROSION이 모두 필요하다. 출력 선택은 `IF (Lrestart.or.VarOut(idTmfo(i),ng)) THEN`이다. | ROMS/Nonlinear/Sediment/sediment_var.h:280–283의 marsh_flux_out_ 생성; ROMS/Nonlinear/Vegetation/vegetation_output.F:298 `Vinfo(21)=Vname(6,idTmfo(i))`. [최종 결론](../compare/roms-outputs-metadata-vs-code.md)의 OMD-Y652. |
| README.md:236 (outputs-metadata:OMD-K028) | MULTI_SCALE_B와 NONUNIFORM_SCALES를 함께 정의하면 correlation 드라이버에서 multiscale_get_scales에 도달한다. | MULTI_SCALE_B와 NONUNIFORM_SCALES를 함께 정의하면 correlation 드라이버에서 multiscale_get_scales에 도달한다. icSvar(i).gt.0이고 해당 변수가 파일에 있으면 ns=1,Nscale을 순회한다. 각 ns의 배열 포인터에 nf90_fread3d의 레코드 인자 1로 읽은 값을 저장한다. reader는 start(4)=tindex로 Nscale 축을 선택한다. 따라서 Nscale>1이면 첫 규모 자료가 각 ns 슬롯에 반복된다. Nscale=1인 제공 CDL에서는 차이가 없다. 두 전처리 옵션이 없거나 해당 변수를 읽지 않는 경우도 이 후보의 적용 범위 밖이다. f03bcbbf(2026-06-10)가 이 호출을 도입했다. f65a834a(2026-08-29)의 포인터 초기화 변경은 레코드 인자를 고치지 않았다. | ROMS/Utility/roms_multiscale.F:1110의 ns 반복; :1178–1180의 레코드 인자 1; ROMS/Utility/nf_fread3d.F:323 `start(4)=tindex`. [최종 결론](../compare/roms-outputs-metadata-vs-code.md)의 OMD-K028. |
| README.md:237 (outputs-metadata:OMD-K029) | 퇴적물 클래스의 standard_name 생성은 d2530aaa(2022-02-27)에 추가됐고 1cbc67d8(2025-06-05)에서 삭제됐다. | 퇴적물 클래스의 standard_name 생성은 d2530aaa(2022-02-27)에 추가됐고 1cbc67d8(2025-06-05)에서 삭제됐다. 현재 SEDIMENT 또는 BBL_MODEL의 sediment_var.h 경로에서 NCS.gt.0인 mud 클래스는 Vname(1:5)를 만들지만 Vname(6)을 대입하지 않는다. load=.FALSE.이므로 일반 메타데이터 복사도 이를 보정하지 않는다. SOLVE3D의 Hout(idTvar(itrc),ng)이 참인 출력은 그 여섯째 슬롯을 Vinfo(21)에 전달한다. BEDLOAD 출력과 퇴적물 분율 출력도 각각 활성화·선택된 경우 같은 슬롯을 소비한다. 출력 선택이 꺼지면 이 속성 출력 문제는 발생하지 않는다. 입력 단위 변환과 빈 속성 생략은 빠진 이름을 복원하지 않는다. 이름 생성의 의도적 폐지라는 근거가 없어 메타데이터 누락 후보로 남긴다. | ROMS/Nonlinear/Sediment/sediment_var.h:136 `load=.FALSE.`와 :146–155의 Vname(1:5) 생성; ROMS/Utility/def_his.F:1444 `Vinfo(21)=Vname(6,idTvar(itrc))`. [최종 결론](../compare/roms-outputs-metadata-vs-code.md)의 OMD-K029. |
| README.md:238 (outputs-metadata:OMD-K030) | d2530aaa(2022-02-27)가 도입한 DAT 호환 경로는 없는 standard_name을 nulvar로 채운다. | d2530aaa(2022-02-27)가 도입한 DAT 호환 경로는 없는 standard_name을 nulvar로 채운다. 일반 Vname 복사와 선택된 HIS 변수 정의를 거치면 이 문자열이 Vinfo(21)에 전달된다. NetCDF 출력부는 nulval만 제외하므로 nulvar가 속성으로 기록될 수 있다. YAML을 선택하면 이 DAT 경로는 실행되지 않는다. PIO 출력부의 실제 조건은 IF (latt.gt.0) THEN이며 nulval 비교가 없다. PIO에서도 비어 있지 않은 nulvar를 생략하지 않는다는 후보 자체는 유지한다. | ROMS/Utility/get_metadata.F:1011 `Vinfo(6)='nulvar'`; ROMS/Utility/def_var.F:364의 nulval 검사와 :1819 `IF (latt.gt.0) THEN`. [최종 결론](../compare/roms-outputs-metadata-vs-code.md)의 OMD-K030. |
| README.md:244 (sediment-ice-vegetation:RBO1-009) | 염분 증가 식은 이전 SwimTime에 변화를 누적한다. | 염분 증가 식은 이전 SwimTime에 변화를 누적한다. 문서의 절편식과 다른 후보를 E로 유지한다. | ROMS/Nonlinear/Biology/oyster_floats.h:356 `SwimTimeNew=MIN(SwimTime+dsalt*slope_Sinc(ng),swim_Tmax(ng))`. [최종 결론](../compare/roms-sediment-ice-vegetation-vs-code.md)의 RBO1-009. |
| README.md:245 (sediment-ice-vegetation:RBO1-010) | 굴 유생의 비양수 dsalt 분기는 이전 SwimTime에 변화를 누적한다. | 굴 유생의 비양수 dsalt 분기는 이전 SwimTime에 변화를 누적한다. 문서의 감소 염분 절편식과 다른 후보를 E로 유지한다. | ROMS/Nonlinear/Biology/oyster_floats.h:358 `SwimTimeNew=MAX(SwimTime+dsalt*slope_Sdec(ng),swim_Tmin(ng))`. [최종 결론](../compare/roms-sediment-ice-vegetation-vs-code.md)의 RBO1-010. |
| README.md:246 (sediment-ice-vegetation:RSD1-025) | MIXED_BED 예제의 TRANSC=0.03과 TRANSN=0.2는 코드에서 응집성 가중치의 감소 전이를 만든다. | MIXED_BED 예제의 TRANSC=0.03과 TRANSN=0.2는 코드에서 응집성 가중치의 감소 전이를 만든다. 입력 설명과의 모순 후보를 E로 유지한다. | ROMS/Nonlinear/Sediment/sed_bed_cohesive.F:889–890의 `(cff1-transN(ng))/(transC(ng)-transN(ng))`. [최종 결론](../compare/roms-sediment-ice-vegetation-vs-code.md)의 RSD1-025. |
| README.md:247 (sediment-ice-vegetation:RSD1-026) | MIXED_BED의 층 임계응력 식은 비응집성 항에 pcoh-1을 곱한다. | MIXED_BED의 층 임계응력 식은 비응집성 항에 pcoh-1을 곱한다. 양의 혼합 가중치와 모순되는 후보를 E로 유지한다. | ROMS/Nonlinear/Sediment/sed_bed_cohesive.F:376·397의 `(pcoh-1.0_r8)`; ROMS/Nonlinear/Sediment/sed_fluxes.F:271의 `(1.0_r8-bottom(i,j,idprp))`. [최종 결론](../compare/roms-sediment-ice-vegetation-vs-code.md)의 RSD1-026. |
| README.md:250 (theory-numerics:RTN-362) | SOLVE3D의 수직 좌표 선택값 0은 입력 검사를 통과한다. | SOLVE3D의 수직 좌표 선택값 0은 입력 검사를 통과한다. 현재 좌표 계산에는 0의 정의가 없다. | ROMS/Utility/read_phypar.F:985·997의 `.lt.0` 검사; ROMS/Utility/set_scoord.F와 ROMS/Nonlinear/set_depth.F의 0 없는 선택 분기. [최종 결론](../compare/roms-theory-numerics-vs-code.md)의 RTN-362. |
| README.md:251 (theory-numerics:RTN-363) | NONLINEAR와 SOLVE3D가 정의된 main3d에서 STEP2D_FB_AB3_AM4 제어는 네 시간 슬롯을 사용한다. | NONLINEAR와 SOLVE3D가 정의된 main3d에서 STEP2D_FB_AB3_AM4 제어는 네 시간 슬롯을 사용한다. 현재 wrapper와 상태 배열은 기존 LF-AM3 구성을 유지한다. | ROMS/Nonlinear/main3d.F:665–687의 네 슬롯 제어; ROMS/Nonlinear/step2d.F:20의 LF-AM3 헤더; ROMS/Modules/mod_ocean.F:408·411·414의 세 슬롯 할당. [최종 결론](../compare/roms-theory-numerics-vs-code.md)의 RTN-363. |
| README.md:252 (tools-guides:RTG-1970) | 다중 파일 전환의 범위 이탈 조건은 .and.로 결합돼 있다. | 다중 파일 전환의 범위 이탈 조건은 .and.로 결합돼 있다. 파일 수가 양수이면 이 검사는 범위 이탈을 잡지 못한다. | ROMS/Utility/inquiry.F:146 `IF ((1.gt.Fcount).and.(Fcount.gt.S(ifile)%Nfiles)) THEN`. [최종 결론](../compare/roms-tools-guides-vs-code.md)의 RTG-1970. |
| README.md:253 (tools-guides:RTG-1971) | SOLVE3D의 수직좌표 선택값 0은 입력 검사를 통과한다. | SOLVE3D의 수직좌표 선택값 0은 입력 검사를 통과한다. 현재 좌표 계산에는 0의 정의가 없다. | ROMS/Utility/read_phypar.F:985·997의 `.lt.0` 검사; ROMS/Utility/set_scoord.F와 ROMS/Nonlinear/set_depth.F의 0 없는 선택 분기. [최종 결론](../compare/roms-tools-guides-vs-code.md)의 RTG-1971. |

## models/ROMS/source-analysis/roms_support_modules.md — 완료

- 대조한 대상 줄: 74줄. 시작 시 diff의 추가 줄을 셌다.
- 대상 줄 범위: 2, 6, 8, 30–36, 39–48, 50, 52–55, 57–61, 63–66, 70, 74, 78, 82–118.
- 정정: 5줄. 보완: 2줄. 아래 목록의 수정 줄을 셌다.
- 차이 표 24행의 분류와 결론은 최종 보고서와 같다. 코드 서식과 E 강도 표기 추가는 결론의 뜻을 바꾸지 않는다. E 행 RI1-0745와 RI1-0984의 강함 판정을 확인했다. A 행은 없다.
- 차이 표에 인용한 코드 위치 251개와 위키 위치 39개를 열었다. 이 수는 중복 인용을 포함한다. 본문의 12열 POS, 시각 환산, 주기 경계 복사, MPI 수신, 격자·너징·조석 주기 읽기 조건을 해당 코드와 대조했다.
- frontmatter에 남은 파일 줄 수는 현재 원문 줄 수와 같다. 기존 문장 교체는 RI1-1055, RCN-1983, RF1-026 수정안과 대조했다. 링크만 바꾼 줄의 설명도 원문과 대조했다.
- 상대 링크는 모두 존재한다. 대상 줄에 Mermaid 블록은 없다. 노트에 사용자 홈 절대 경로, 이중 대괄호, 지정한 작업 한계 문장은 없다.
- 기계 확인 후보 판정: 후보 없음.

| 노트:줄 | 종류 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| roms_support_modules.md:33 | 정정 | 위치 좌표 변환의 조건 | station 경위도 좌표 변환의 조건 | grid_coords.F:199의 STATIONS 분기와 :202의 station 설명. :206의 spherical 조건. 입력 보고서 최종 RI1-1055도 stations를 명시한다. |
| roms_support_modules.md:34 | 정정 | 후속 조건 | station의 FLAG 조건 | grid_coords.F:208–209의 Nstation 순회와 SCALARS(ng)%Sflag 검사. float 변환은 :91–104의 별도 경로이다. |
| roms_support_modules.md:52 | 보완 | 초기장 설정 설명에 직접 코드 인용 없음 | ROMS/Nonlinear/ini_fields.F:12–14,547–563 인용 추가 | 2D 운동량 초기화 설명과 PerfectRST 조건의 tracer 초기화 코드. |
| roms_support_modules.md:53 | 정정 | 자유표면 ζ를 초기화하거나 갱신한다. | 자유표면 ζ를 빠른 시간 간격의 평균값으로 설정한다. | set_zeta.F:13 `sets free-surface to its fast-time averaged value`; :103–104의 Zt_avg1 대입. |
| roms_support_modules.md:54 | 보완 | 초기화 후 처리 설명에 직접 코드 인용 없음 | ROMS/Nonlinear/post_initial.F:13–16 인용 추가 | 첫 시간 단계의 깊이·층 두께·상태 초기화와 측면 경계조건 설명. |
| roms_support_modules.md:70 | 정정 | TLM/ADJ 경계 control과 일반 forcing 조정 | 4D-Var 증분을 비선형 모델의 개방경계 배열과 표면 외력에 적용한다. | obc_adjust.F:13–16과 frc_adjust.F:13–16은 nonlinear model을 명시한다. |
| roms_support_modules.md:74 | 정정 | implicit 경계조건, 표면/저면 wall function·flux BC | 난류 운동에너지와 난류 길이 척도의 측면 경계조건 | tkebc_im.F:12–14 `sets lateral boundary conditions` |

## models/ROMS/source-analysis/roms_include_cppdefs.md — 완료

- 대조한 대상 줄: 68줄. 시작 시 diff의 추가 줄을 셌다.
- 대상 줄 범위: 7–8, 20, 24–26, 29–31, 36, 40, 44, 46, 50, 55, 58, 81, 87, 92, 96, 100, 102, 106, 114–115, 119, 121–124, 127–128, 132, 140–141, 149–150, 155–157, 159, 164–167, 177, 181–184, 186–189, 212, 223, 228–239.
- 정정: 2줄. 보완: 0줄.
- apply-20에 기록한 수정안 48개를 보고서의 해당 수정안 또는 최종 결론에 대조했다. 카탈로그·실행 입력·전처리 파생·호환 이름·경계 폭·예제 수치의 원문을 열었다. 코드 블록은 cppdefs.h, upwelling.h, tile.h의 해당 줄과 같다.
- Include의 `*.h` 파일명은 40개이다. 지정한 공통 헤더 5개를 제외한 응용 헤더는 35개이다. adria02.h와 nj_bight.h는 해당 디렉터리에 없다.
- 배정표에서 지정한 3열을 다시 집계했다. A 56개, B 34개, C 533개, E 20개, F 46개로 합계 689개이다. D는 0개이다. 차이 파일 링크 세 개는 실제 파일을 가리킨다.
- `9e75e6e9:ROMS/Include/globaldefs.h`를 열어 구 옵션 이름의 호환 정의를 확인했다. 이 노트의 대상 줄에는 직접적인 A·E 차이 표 행이 없다.
- 상대 링크는 모두 존재한다. 대상 줄에 Mermaid 블록은 없다. 노트에 사용자 홈 절대 경로, 이중 대괄호, 지정한 작업 한계 문장은 없다.
- 기계 확인 후보 판정: 후보 없음.

| 노트:줄 | 전 | 후 | 근거 원문·최종 보고서 |
|---|---|---|---|
| roms_include_cppdefs.md:7 | frontmatter가 globaldefs.h의 역할을 내부 파생 매크로·일관성 체크·error로 설명함 | globaldefs.h는 내부 파생 매크로·옵션 조정으로 설명한다. 별도 오류 검사에는 ROMS/Utility/checkdefs.F를 명시한다. | build-options-history의 RBH-3450. checkdefs.F:3819–3829의 Q_PSOURCE 오류 처리와 exit_flag=5 대입. |
| roms_include_cppdefs.md:106 | nADJ<ntimes이면 NSA=2, 그 밖은 NSA=1로만 설명함 | CORRELATION 또는 WEAK_CONSTRAINT 경로의 SP4DVAR는 NSA=2를 설정한다. nADJ 조건은 SP4DVAR가 없는 분기에 적용한다. | ROMS/Utility/read_phypar.F:4745–4753의 `# if defined CORRELATION \|\| defined WEAK_CONSTRAINT`, `#  ifdef SP4DVAR`, `NSA=2`, `#  else`. RT2-395의 NSA 구분에 선행 분기를 복원했다. |

## models/ROMS/source-analysis/roms_io_netcdf.md — 완료

- 대조한 대상 줄: 77줄. 시작 시 diff의 추가 줄을 셌다.
- 대상 줄 범위: 7–8, 21–25, 37, 39–41, 47–49, 80–83, 105–110, 153, 163–169, 175–185, 205–207, 212–215, 225–230, 236–254, 256–257.
- 정정: 8줄. 보완: 2줄.
- apply-5의 수정안·유지 항목을 보고서 최종본에 대조했다. generic 인터페이스, DAI 용도, 생성 모드, Vinfo 슬롯, 병렬 I/O, 결합 입력 로더, 정규화 파일, LCZ 레코드의 인용 원문을 열었다. 인용 없이 파일명만 적은 시간보간 설명도 두 루틴의 계산식에서 확인했다.
- Utility의 `nf_fread*.F` 파일은 7개이다. `nf_fwrite*.F` 파일은 5개이다. 두 패턴의 합계는 12개이다.
- 배정표에서 지정한 3열을 다시 집계했다. A 37행, B 85행, C 67행, D 27행, E 5행, F 16행으로 합계 237행이다. 차이 파일 링크는 실제 파일을 가리킨다. 이 노트의 대상 줄에는 직접적인 A·E 차이 표 행이 없다.
- DA1-818의 과거 수정안은 상세 미확인 표기 유지를 요구했다. 이번 사용자 지시는 한계 문장을 남기지 말라는 지시이다. 최신 지시에 따라 해당 줄은 실제 관련 노트의 링크 안내로 고쳤다.
- 상대 링크는 모두 존재한다. 대상 줄에 Mermaid 블록은 없다. 노트에 사용자 홈 절대 경로, 이중 대괄호, 지정한 작업 한계 문장은 없다.
- 기계 확인 후보 판정: 후보 없음.

| 노트:줄 | 종류 | 전 | 후 | 근거 원문·최종 보고서 |
|---|---|---|---|---|
| roms_io_netcdf.md:39 | 정정 | def_*와 wrt_*가 출력 파일별로 1:1 쌍을 이룬다고 일반화함 | 열거한 출력 종류에 같은 접미사의 def_*·wrt_* 파일이 있다고 한정함 | Utility의 열거한 10종 파일 쌍을 확인했다. def_lanczos.F와 def_norm.F에는 같은 이름의 wrt_lanczos.F·wrt_norm.F가 없으므로 모든 정의 파일로 일반화할 수 없다. |
| roms_io_netcdf.md:178 | 정정 | 보간이 필요하면 mp_bcastf 후 regrid 경로를 따른다. | DISTRIBUTE가 정의된 보간 경로에서 mp_bcastf를 호출한다. 보간은 regrid_nf90 경로를 따른다. | nf_fread2d.F:1070–1085의 DISTRIBUTE·ELSE·interpolate 조건. OMD-N021의 요약에 실제 전처리 조건을 명시했다. |
| roms_io_netcdf.md:179 | 정정 | DISTRIBUTE가 없으면 배열을 직접 푼다. | .not.interpolate 분기 안에서 DISTRIBUTE가 없으면 배열을 직접 푼다. | nf_fread2d.F:1030–1045. |
| roms_io_netcdf.md:206 | 정정 | 현재 원문은 8243줄이다. | 코드 HEAD 57aecf58과 Ngrids 입력 CASE 위치를 기록한다. | inputs 최종 RI1-1044는 총 줄 수 대신 코드 판과 CASE 줄을 기록하도록 요구한다. read_phypar.F:171–173에서 Ngrids를 읽는다. |
| roms_io_netcdf.md:229 | 정정 | 보간 경로는 broadcast를 사용한다. | 표준 NetCDF 보간 경로에서 DISTRIBUTE가 정의되면 broadcast를 사용한다. | nf_fread2d.F:1070–1074. |
| roms_io_netcdf.md:230 | 정정 | 비분산 읽기 경로는 배열을 직접 푼다. | 비분산 읽기 경로의 .not.interpolate 분기에서 배열을 직접 푼다. | nf_fread2d.F:1030–1045. |
| roms_io_netcdf.md:239 | 보완 | set_2dfld·set_3dfld 이름만 제시함 | fac1·fac2 적용식의 직접 코드 인용을 추가함 | set_2dfld.F:116–124와 set_3dfld.F:126–135의 Fout 대입식. |
| roms_io_netcdf.md:240 | 정정 | 상세 구조 링크 뒤에 source-needed를 남김 | 실제 자료동화 관련 노트의 링크 안내로 바꿈 | 최신 사용자 지시의 한계 문장 제거 요구. 두 상대 링크의 실제 파일을 확인했다. |
| roms_io_netcdf.md:241 | 정정 | UGRID 위상 속성 | SGRID 위상 속성 | def_var.F:196 `Define special attributes for SGRID conventions variable`와 :200–201의 cf_role=grid_topology. face_dimensions 기록은 :232–233이다. |
| roms_io_netcdf.md:248 | 보완 | 기존 파일의 변수·차원 조회 근거를 1094–1108로 인용함 | 인용을 1094–1114로 확장함 | def_norm.F:1107은 netcdf_check_dim 호출이다. 변수 조회 netcdf_inq_var 호출은 :1113–1114이다. |

## 전체 완료 결과

| 대상 노트 | 대조한 대상 줄 수 | 정정 수 | 보완 수 |
|---|---:|---:|---:|
| models/ROMS/README.md | 234 | 31 | 0 |
| models/ROMS/source-analysis/roms_support_modules.md | 74 | 5 | 2 |
| models/ROMS/source-analysis/roms_include_cppdefs.md | 68 | 2 | 0 |
| models/ROMS/source-analysis/roms_io_netcdf.md | 77 | 8 | 2 |
| 합계 | 453 | 46 | 4 |

대상 줄 수는 각 노트의 `git diff -U0 HEAD` 추가 줄에서 집계했다. 정정 수와 보완 수는 노트에 붙인 검증 표식에서 집계했다. 모든 정정·보완 줄은 대상 줄에 포함된다.

네 노트의 대상 줄을 모두 대조했다. 미해결 항목은 없다. 제공된 기계 확인 불일치 후보는 없다.

네 노트의 frontmatter를 YAML로 읽었다. 노트와 이 기록의 상대 링크가 가리키는 파일을 확인했다. 표의 열 수와 정정 목록의 줄 번호를 확인했다. `git diff --check`는 오류 없이 끝났다.
