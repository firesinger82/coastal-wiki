---
title: "adcirc preprocessing foundation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC 공식 문서(adcirc.github.io / adcirc.org) 기반 전처리 레이어 정리. file 의미·NWS·전처리 도구 생태계는 공식 docs 근거. (2026-06-18 canonical 정화: 개인 프로젝트 내용 — wide6·JMA-MSM 로컬 분기·로컬 경로·local-workflow 링크 — 제거. 개인 ADCIRC 운영 자료는 experience/ 레이어.)"
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 마이그레이션 2026-05-23 → 2026-06-18 정화 (Opus 4.8)"
note_date: 2026-04~05 (original) / 2026-05-23 (promote) / 2026-06-18 (purify)
verification_by: "공식 ADCIRC 문서 cross-ref"
verification_date: 2026-06-18
last_source_check: 2026-10-12 (recovery 차이 결론 반영)
---

# ADCIRC Preprocessing Foundation

Purpose:
- define the preprocessing layer that must be stabilized before serious ADCIRC project work
- separate mesh generation, bathymetry construction, and forcing ingestion from later parameter tuning

This note is a foundation note, not a run recipe.

## Why This Comes First

The hardest early failure modes in ADCIRC work usually do not start in `DT` or `TAU0`.
They start earlier:
- the wrong meshing toolchain is chosen
- bathymetry and coastline data are assembled inconsistently
- boundary strings are assigned incorrectly
- meteorological forcing is available, but not in a schema ADCIRC actually accepts

That means preprocessing is the first system to stabilize.

## Core Observation From Official Docs

Official ADCIRC documentation puts a large fraction of project setup pressure on the preprocessing layer:
- `fort.14` is required and contains the finite element grid, bathymetry, and boundary information
- boundary locations are defined in `fort.14`
- periodic and non-periodic boundary forcing are split across `fort.15`, `fort.19`, and `fort.20`
- meteorological forcing is selected through `NWS` and usually depends on a `fort.22` family input

| 항목 | 문서·코드 대조 | 출처와 원문 | 결론 |
| --- | --- | --- | --- |
| <a id="cvb-l43"></a> CLI-10 -Mft MESH_FILE_TYPE | 코드는 -MFT·-mft만 비교한다. 문서의 -Mft는 일치하지 않는다. | `[file=docs/user_guide/running_adcirc/command_line_options.rst line=41]` ``` ``-Mft MESH_FILE_TYPE`` ```<br>`[file=docs/user_guide/running_adcirc/command_line_options.rst line=42]` ` The MESH_FILE_TYPE can be specified as ascii (the default) or xdmf (introduced in ADCIRC v51). `<br>`[file=src/sizes.F line=234]` ` case("-MFT","-mft") ! mesh file type `<br>`[file=src/sizes.F line=236]` ` call GET_COMMAND_ARGUMENT(i, CMDLINEARG) `<br>`[file=src/sizes.F line=238]` ` case("ASCII","Ascii","ascii") `<br>`[file=src/sizes.F line=240]` ` case("XDMF","Xdmf","xdmf") `<br>`models/ADCIRC/raw/source_code/adcirc/docs/user_guide/running_adcirc/command_line_options.rst:41` ``` ``-Mft MESH_FILE_TYPE`` ```<br>`models/ADCIRC/raw/source_code/adcirc/src/sizes.F:234` `case("-MFT","-mft") ! mesh file type`<br>`models/ADCIRC/raw/source_code/adcirc/docs/user_guide/running_adcirc/command_line_options.rst:44` ``` ``-Mfn MESH_FILE_NAME`` ```<br>`models/ADCIRC/raw/source_code/adcirc/docs/user_guide/running_adcirc/command_line_options.rst:74` `mpirun -np 16 ./padcirc -Mfn my_custom_mesh.grd`<br>`models/ADCIRC/raw/source_code/adcirc/src/sizes.F:249` `case("-MFN","-mfn") ! mesh file name`<br>`models/ADCIRC/raw/source_code/adcirc/docs/user_guide/running_adcirc/command_line_options.rst:47` ``` ``-Nft NODAL_ATTRIBUTES_FILE_TYPE`` ```<br>`models/ADCIRC/raw/source_code/adcirc/src/sizes.F:271` `case("-NFT","-nft") ! nodal attributes file type`<br>`models/ADCIRC/raw/source_code/adcirc/docs/user_guide/running_adcirc/command_line_options.rst:50` ``` ``-Nfn NODAL_ATTRIBUTES_FILE_NAME`` ```<br>`models/ADCIRC/raw/source_code/adcirc/src/sizes.F:287` `case("-NFN","-nfn") ! nodal attributes file name`<br>동봉 문서와 예제의 혼합 대소문자는 실제 CASE 문자열과 일치하지 않는다. 해석: 옵션 이름의 문서 오기이다. | B 문서 오기. v56.2.1은 파일 이름·유형 옵션에 대문자 또는 소문자 별칭을 요구한다.<br>[inputfiles 보고서 §5 CLI-10, CLI-11, CLI-12, CLI-13](../../../_staging/recovery/compare/ADCIRC-inputfiles-vs-code.md#5-차이-결론) [10-12 결론 검증 보완] |
| CLI-11 -Mfn MESH_FILE_NAME | 코드는 -MFN·-mfn만 비교한다. 문서의 예제도 -Mfn을 사용한다. | `[file=docs/user_guide/running_adcirc/command_line_options.rst line=44]` ``` ``-Mfn MESH_FILE_NAME`` ```<br>`[file=docs/user_guide/running_adcirc/command_line_options.rst line=45]` ` Search for a full domain mesh file named MESH_FILE_NAME rather than the default mesh file name fort.14. `<br>`[file=docs/user_guide/running_adcirc/command_line_options.rst line=74]` ` mpirun -np 16 ./padcirc -Mfn my_custom_mesh.grd `<br>`[file=src/sizes.F line=249]` ` case("-MFN","-mfn") ! mesh file name `<br>`[file=src/sizes.F line=250]` ` meshFileNameSpecified = .true. `<br>`[file=src/sizes.F line=252]` ` call GET_COMMAND_ARGUMENT(i,meshFileName) `<br>[근거·판정 정본](#cvb-l43) | [근거·판정 정본](#cvb-l43) [10-12 결론 검증 보완] |
| CLI-12 -Nft NODAL_ATTRIBUTES_FILE_TYPE | 코드는 -NFT·-nft만 비교한다. 문서의 -Nft는 일치하지 않는다. | `[file=docs/user_guide/running_adcirc/command_line_options.rst line=47]` ``` ``-Nft NODAL_ATTRIBUTES_FILE_TYPE`` ```<br>`[file=docs/user_guide/running_adcirc/command_line_options.rst line=48]` ` The NODAL_ATTRIBUTES_FILE_TYPE can be specified as ascii (the default) or xdmf (introduced in ADCIRC v51). `<br>`[file=src/sizes.F line=271]` ` case("-NFT","-nft") ! nodal attributes file type `<br>`[file=src/sizes.F line=273]` ` call GET_COMMAND_ARGUMENT(i, CMDLINEARG) `<br>`[file=src/sizes.F line=275]` ` case("ASCII","Ascii","ascii") `<br>`[file=src/sizes.F line=277]` ` case("XDMF","Xdmf","xdmf") `<br>[근거·판정 정본](#cvb-l43) | [근거·판정 정본](#cvb-l43) [10-12 결론 검증 보완] |
| CLI-13 -Nfn NODAL_ATTRIBUTES_FILE_NAME | 코드는 -NFN·-nfn만 비교한다. 문서의 -Nfn은 일치하지 않는다. | `[file=docs/user_guide/running_adcirc/command_line_options.rst line=50]` ``` ``-Nfn NODAL_ATTRIBUTES_FILE_NAME`` ```<br>`[file=docs/user_guide/running_adcirc/command_line_options.rst line=51]` ` Search for a full domain nodal attributes file named NODAL_ATTRIBUTES_FILE_NAME rather than the default nodal attributes file name fort.13. `<br>`[file=src/sizes.F line=287]` ` case("-NFN","-nfn") ! nodal attributes file name `<br>`[file=src/sizes.F line=288]` ` naFileNameSpecified = .true. `<br>`[file=src/sizes.F line=290]` ` call GET_COMMAND_ARGUMENT(i,naFileName) `<br>[근거·판정 정본](#cvb-l43) | [근거·판정 정본](#cvb-l43) [10-12 결론 검증 보완] |
| <a id="cvb-l47"></a> CLI-14 -U·소문자 별칭 | -U는 지역 출력만 설정한다. 코드 비교문은 나열한 소문자 별칭도 받는다. | 대상 명령줄 문서는 -U와 -i·-o·-l·-s·-r·-m 별칭을 적지 않는다.<br>`[file=src/sizes.F line=191]` ` case("-I","-i") `<br>`[file=src/sizes.F line=198]` ` case("-O","-o") `<br>`[file=src/sizes.F line=205]` ` case("-L","-l") `<br>`[file=src/sizes.F line=211]` ` case("-U","-u") `<br>`[file=src/sizes.F line=212]` ` WRITE_LOCAL_FILES = .TRUE. `<br>`[file=src/sizes.F line=216]` ` case("-S","-s") `<br>`[file=src/sizes.F line=221]` ` case("-R","-r") `<br>`[file=src/sizes.F line=231]` ` case("-M","-m") `<br>`models/ADCIRC/raw/source_code/adcirc/src/sizes.F:191` `case("-I","-i")`<br>`models/ADCIRC/raw/source_code/adcirc/src/sizes.F:198` `case("-O","-o")`<br>`models/ADCIRC/raw/source_code/adcirc/src/sizes.F:205` `case("-L","-l")`<br>`models/ADCIRC/raw/source_code/adcirc/src/sizes.F:211` `case("-U","-u")`<br>`models/ADCIRC/raw/source_code/adcirc/src/sizes.F:212` `WRITE_LOCAL_FILES = .TRUE.`<br>`models/ADCIRC/raw/source_code/adcirc/src/sizes.F:216` `case("-S","-s")`<br>`models/ADCIRC/raw/source_code/adcirc/src/sizes.F:221` `case("-R","-r")`<br>`models/ADCIRC/raw/source_code/adcirc/src/sizes.F:231` `case("-M","-m")`<br>`models/ADCIRC/raw/source_code/adcirc/src/adcirc.F:185` `case("-h","--help")`<br>`models/ADCIRC/raw/source_code/adcirc/src/adcirc.F:186` `call PRINT_HELP()`<br>`models/ADCIRC/raw/source_code/adcirc/src/adcirc.F:188` `case("-V","-v","--version")`<br>`models/ADCIRC/raw/source_code/adcirc/src/adcirc.F:194` `case("--hash")`<br>`models/ADCIRC/raw/source_code/adcirc/src/adcirc.F:195` `write(*,'(a)') trim(adc_hash)`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:198` `CASE("--partmesh_npart_from_epart")`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:199` `PARTITION = .TRUE.`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:200` `PARTITION_APPROACH = 2`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:211` `CASE("--strict-boundaries")`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:212` `strictBoundaries = .true.`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:217` `case("-MFT","-mft","--MFT","--mft") ! mesh file type`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:231` `case("-MFN","-mfn","--MFN","--mfn") ! mesh file name`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:235` `case("-NFT","-nft","--NFT","--nft") ! nodal attributes file type`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:250` `case("-NFN","--nfn") ! nodal attributes file name`<br>`models/ADCIRC/raw/source_code/adcirc/src/sizes.F:299` `write(*,*) "WARNING: The command line option '",`<br>`models/ADCIRC/raw/source_code/adcirc/src/sizes.F:300` `&             cmdlinearg(1:2),"' is not valid and will be ignored."`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:254` `case default`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:255` `write(*,'(3A)') "ERROR: The command line option '",`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:256` `&                  trim(cmdlinearg),"' is not valid."`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:257` `call exit(1)`<br>대조한 명령줄 문서는 실제 parser의 모든 별칭·도움말·분할 옵션·오류 처리를 나열하지 않는다. 해석: 명령줄 규칙의 문서 누락이다. adcprep의 -NFN·--nfn 조합은 코드 그대로 남긴다. | C 문서 누락. v56.2.1의 추가 명령줄 옵션과 오류 처리는 각 실행 파일의 CASE 목록을 따른다.<br>[inputfiles 보고서 §5 CLI-14, CLI-15, CLI-23, CLI-24, CLI-25](../../../_staging/recovery/compare/ADCIRC-inputfiles-vs-code.md#5-차이-결론) [10-12 결론 검증 보완] |
| CLI-15 -h·--help·-V·-v·--version·--hash | 코드는 도움말·판·hash를 출력하고 종료한다. | 대상 명령줄 문서에서 이 조회 옵션들을 찾지 못했다.<br>`[file=src/adcirc.F line=185]` ` case("-h","--help") `<br>`[file=src/adcirc.F line=186]` ` call PRINT_HELP() `<br>`[file=src/adcirc.F line=188]` ` case("-V","-v","--version") `<br>`[file=src/adcirc.F line=192]` ` write(*,'(a)') trim(adc_version) `<br>`[file=src/adcirc.F line=194]` ` case("--hash") `<br>`[file=src/adcirc.F line=195]` ` write(*,'(a)') trim(adc_hash) `<br>`[file=src/adcirc.F line=196]` ` call exit(ADCIRC_EXIT_SUCCESS) `<br>[근거·판정 정본](#cvb-l47) | [근거·판정 정본](#cvb-l47) [10-12 결론 검증 보완] |
| CLI-22 adcprep --prep88 | 확인하지 않음. 옵션 분기를 주석 처리했다. 실행 코드는 이 옵션을 알 수 없는 옵션으로 처리한다. | `[file=docs/user_guide/running_adcirc/command_line_options.rst line=99]` ``` ``--prep88`` ```<br>`[file=docs/user_guide/running_adcirc/command_line_options.rst line=100]` ` Only redecompose the upland river initialization file (fort.88). Requires that prepall step has already been performed. `<br>`[file=prep/adcprep.F line=209]` ` !            CASE("--prep88") `<br>`[file=prep/adcprep.F line=210]` ` !               PREP_88 = .TRUE. `<br>`[file=prep/adcprep.F line=254]` ` case default `<br>`[file=prep/adcprep.F line=255]` ` write(*,'(3A)') "ERROR: The command line option '", `<br>`[file=prep/adcprep.F line=256]` ` &                  trim(cmdlinearg),"' is not valid." `<br>`[file=prep/adcprep.F line=257]` ` call exit(1) `<br>`models/ADCIRC/raw/source_code/adcirc/docs/user_guide/running_adcirc/command_line_options.rst:99` ``` ``--prep88`` ```<br>`models/ADCIRC/raw/source_code/adcirc/docs/user_guide/running_adcirc/command_line_options.rst:100` `Only redecompose the upland river initialization file (fort.88). Requires that prepall step has already been performed.`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:209` `!            CASE("--prep88")`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:210` `!               PREP_88 = .TRUE.`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:254` `case default`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:255` `write(*,'(3A)') "ERROR: The command line option '",`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:256` `&                  trim(cmdlinearg),"' is not valid."`<br>`models/ADCIRC/raw/source_code/adcirc/prep/adcprep.F:257` `call exit(1)`<br>`models/ADCIRC/raw/source_code/adcirc/prep/presizes.F:262` `!LOGICAL :: PREP_88  ! .true. if user specified --prep88 cmd line option !commented out by tcm v51.27`<br>문서는 활성 옵션으로 나열한다. parser CASE는 주석이다. presizes의 주석은 tcm v51.27에서 주석 처리했음을 명시한다. 해석: 문서가 제거 전의 옵션을 남겼다. | A 판 차이. v56.2.1의 adcprep는 --prep88을 활성 옵션으로 받지 않는다.<br>[inputfiles 보고서 §5 CLI-22](../../../_staging/recovery/compare/ADCIRC-inputfiles-vs-code.md#5-차이-결론) |
| CLI-23 adcprep --partmesh_npart_from_epart·--strict-boundaries | 분할 접근법 2와 엄격한 경계 플래그를 선택한다. | 대상 명령줄 문서에서 이 옵션을 찾지 못했다.<br>`[file=prep/adcprep.F line=198]` ` CASE("--partmesh_npart_from_epart") `<br>`[file=prep/adcprep.F line=199]` ` PARTITION = .TRUE. `<br>`[file=prep/adcprep.F line=200]` ` PARTITION_APPROACH = 2 `<br>`[file=prep/adcprep.F line=211]` ` CASE("--strict-boundaries") `<br>`[file=prep/adcprep.F line=212]` ` strictBoundaries = .true. `<br>[근거·판정 정본](#cvb-l47) | [근거·판정 정본](#cvb-l47) [10-12 결론 검증 보완] |
| CLI-24 adcprep의 파일 유형·이름 옵션 | adcprep은 인용한 대소문자 조합을 비교한다. -NFN·--nfn 조합은 다른 이름 옵션의 네 가지 별칭과 다르다. | 전용 adcprep 절은 이 옵션을 적지 않는다.<br>`[file=prep/adcprep.F line=217]` ` case("-MFT","-mft","--MFT","--mft") ! mesh file type `<br>`[file=prep/adcprep.F line=231]` ` case("-MFN","-mfn","--MFN","--mfn") ! mesh file name `<br>`[file=prep/adcprep.F line=235]` ` case("-NFT","-nft","--NFT","--nft") ! nodal attributes file type `<br>`[file=prep/adcprep.F line=250]` ` case("-NFN","--nfn") ! nodal attributes file name `<br>[근거·판정 정본](#cvb-l47) | [근거·판정 정본](#cvb-l47) [10-12 결론 검증 보완] |
| <a id="cvb-l52"></a> CLI-26 aswip의 추가 단일 옵션 | -h는 도움말을 호출한다. -A·-V·-S·-B·-C·-D는 출력 선택 플래그를 바꾼다. -E는 요소 파일의 이름을 받는다. -F는 frame을 받는다. -G는 geostrophic 선택값을 받는다. -h 이외에는 대문자·소문자 별칭을 비교한다. | fort22.rst는 -n·-m·-z를 설명한다. MET-31의 원문을 참조한다.<br>`[file=wind/aswip.F line=2860]` ` CASE("-h") ! display help and exit `<br>`[file=wind/aswip.F line=2863]` ` CASE("-A","-a") ! Rmw and Azimuth vals req. (360 deg/1deg incr.) `<br>`[file=wind/aswip.F line=2865]` ` CASE("-V","-v") ! radial V and P values requested `<br>`[file=wind/aswip.F line=2867]` ` CASE("-S","-s") ! spatial V and P unstructured mesh vals requested `<br>`[file=wind/aswip.F line=2869]` ` CASE("-B","-b") ! uvp at given node location xy `<br>`[file=wind/aswip.F line=2871]` ` CASE("-C","-c") ! spatial xy&uvp,unstructured mesh vals requested `<br>`[file=wind/aswip.F line=2873]` ` CASE("-D","-d") ! don't write NWS19 fort.22 `<br>`[file=wind/aswip.F line=2875]` ` CASE("-E","-e")  ! providing an element table for spatial output `<br>`[file=wind/aswip.F line=2880]` ` CASE("-F","-f")  ! selecting a particular frame to render `<br>`[file=wind/aswip.F line=2884]` ` CASE("-G","-g")  ! selecting geostrophic or cyclostrophic `<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2860` `CASE("-h") ! display help and exit`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2863` `CASE("-A","-a") ! Rmw and Azimuth vals req. (360 deg/1deg incr.)`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2865` `CASE("-V","-v") ! radial V and P values requested`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2867` `CASE("-S","-s") ! spatial V and P unstructured mesh vals requested`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2869` `CASE("-B","-b") ! uvp at given node location xy`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2871` `CASE("-C","-c") ! spatial xy&uvp,unstructured mesh vals requested`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2873` `CASE("-D","-d") ! don't write NWS19 fort.22`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2875` `CASE("-E","-e")  ! providing an element table for spatial output`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2880` `CASE("-F","-f")  ! selecting a particular frame to render`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2884` `CASE("-G","-g")  ! selecting geostrophic or cyclostrophic`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2892` `CASE("-I","-i")  ! input fort.14 file containing mesh locations`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2895` `meshFileName = trim(CMDLINEARG)`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2897` `CASE("-L","-l")  ! input text file containing station locations`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2900` `meshFileName = trim(CMDLINEARG)`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2910` `CASE("-O","-o")  ! time increment for writing output (seconds)`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2914` `READ(CMDLINEARG,*) output_increment`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2919` `CASE("-P","-p")  ! percent change of rmax relative to calculated val`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2922` `READ(CMDLINEARG,*) rmax_percent`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2926` `CASE("-X","-x")  ! percent change of vmax relative to given val`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2929` `READ(CMDLINEARG,*) vmax_percent`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2930` `CASE("-T","-t")  ! time offset (like hotstart time)`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2933` `READ(CMDLINEARG,*) timeOffset`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2935` `CASE("-R","-r")  ! constant forecastRmax`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2938` `READ(CMDLINEARG,*) forecastRmax`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2945` `CASE("-W","-w") ! the name of the track file to read`<br>`models/ADCIRC/raw/source_code/adcirc/wind/aswip.F:2948` `CALL GET_COMMAND_ARGUMENT(I,CMDLINEARG)`<br>대조한 명령줄 문서는 aswip의 모든 출력·입력·시간·트랙 조정 옵션을 나열하지 않는다. 실제 CASE가 값을 저장한다. 해석: 도구 옵션의 문서 누락이다. | C 문서 누락. v56.2.1의 aswip는 CLI-26·CLI-27에 열거한 추가 옵션을 처리한다.<br>[inputfiles 보고서 §5 CLI-26, CLI-27](../../../_staging/recovery/compare/ADCIRC-inputfiles-vs-code.md#5-차이-결론) [10-12 결론 검증 보완] |
| CLI-27 aswip의 추가 값 옵션 | -I는 fort.14 파일명을 받는다. -L은 관측점 위치 파일명을 받는다. -O는 출력 시간 간격을 초로 받는다. -P는 rmax 비율을 받는다. -X는 vmax 비율을 받는다. -T는 시간 offset을 받는다. -R은 일정한 forecastRmax를 받는다. -W는 트랙 파일명을 받는다. 각 옵션은 대문자·소문자 별칭을 비교한다. | fort22.rst는 -n·-m·-z를 설명한다. MET-31의 원문을 참조한다.<br>`[file=wind/aswip.F line=2892]` ` CASE("-I","-i")  ! input fort.14 file containing mesh locations `<br>`[file=wind/aswip.F line=2895]` ` meshFileName = trim(CMDLINEARG) `<br>`[file=wind/aswip.F line=2897]` ` CASE("-L","-l")  ! input text file containing station locations `<br>`[file=wind/aswip.F line=2900]` ` meshFileName = trim(CMDLINEARG) `<br>`[file=wind/aswip.F line=2910]` ` CASE("-O","-o")  ! time increment for writing output (seconds) `<br>`[file=wind/aswip.F line=2914]` ` READ(CMDLINEARG,*) output_increment `<br>`[file=wind/aswip.F line=2919]` ` CASE("-P","-p")  ! percent change of rmax relative to calculated val `<br>`[file=wind/aswip.F line=2922]` ` READ(CMDLINEARG,*) rmax_percent `<br>`[file=wind/aswip.F line=2926]` ` CASE("-X","-x")  ! percent change of vmax relative to given val `<br>`[file=wind/aswip.F line=2929]` ` READ(CMDLINEARG,*) vmax_percent `<br>`[file=wind/aswip.F line=2930]` ` CASE("-T","-t")  ! time offset (like hotstart time) `<br>`[file=wind/aswip.F line=2933]` ` READ(CMDLINEARG,*) timeOffset `<br>`[file=wind/aswip.F line=2935]` ` CASE("-R","-r")  ! constant forecastRmax `<br>`[file=wind/aswip.F line=2938]` ` READ(CMDLINEARG,*) forecastRmax `<br>`[file=wind/aswip.F line=2945]` ` CASE("-W","-w") ! the name of the track file to read `<br>`[file=wind/aswip.F line=2948]` ` CALL GET_COMMAND_ARGUMENT(I,CMDLINEARG) `<br>[근거·판정 정본](#cvb-l52) | [근거·판정 정본](#cvb-l52) [10-12 결론 검증 보완] |

- the official tools page explicitly separates mesh generation, forcing acquisition, and automation into different tool families

## Three Foundation Axes

### 1. Mesh Generation And Boundary Construction

Questions:
- which tool should be used to build or edit the mesh?
- how are shoreline, open-ocean, river, and barrier boundaries turned into node strings?
- how reproducible is the mesh-generation path?

Primary outputs:
- `fort.14`
- sometimes `fort.13`
- sometimes helper geometry, GIS, or project files outside ADCIRC itself

Primary note:
- 공식 메시 생성 도구는 아래 "What The Official Tooling Map Implies" 참조 (SMS / OceanMesh2D / SubgridADCIRCUtility).

### 2. Bathymetry And Topography Assembly

Questions:
- which DEM, chart, or survey sources define the bed and land elevations?
- what datum are they in?
- how are they transferred into `DP` at each node in `fort.14`?

Primary outputs:
- bathymetric `DP` values in `fort.14`
- possibly `fort.13` nodal attributes
- possibly `fort.141` when time-varying bathymetry is actually part of the problem

Primary note:
- `adcirc-bathymetry-input-foundation.md`

### 3. External Forcing Ingestion

Questions:
- which boundary forcing data are needed?
- which meteorological forcing family should be used?
- what conversion step is needed between raw source data and ADCIRC-readable files?

Primary outputs:
- boundary forcing setup in `fort.14`, `fort.15`, `fort.19`, `fort.20`
- meteorological forcing through `fort.22` or related files (NWS 모드별)

Primary note:
- met forcing 메커닉 → `[[adcirc-met-forcing-implementation]]`

## What The Official Tooling Map Implies

The docs do not present one single universal preprocessor. Instead they expose an ecosystem:
- `SMS` as a broad GUI-based commercial environment
- `OceanMesh2D` as an open MATLAB-based end-to-end mesh-generation path
- `SubgridADCIRCUtility` as a specialized terrain/subgrid enhancement path
- `MetGet` as a meteorological forcing acquisition and development system
- `f13builder` and related utility programs for nodal attributes

This implies that tool choice is itself part of the project design, not a minor implementation detail.

## Next Notes To Keep Linked

- `adcirc-bathymetry-input-foundation.md`
- met forcing → `[[adcirc-met-forcing-implementation]]`
