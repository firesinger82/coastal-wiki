# ROMS 노트 전수 검증 14

검증 기준일: 2026-10-14.

검증 대상은 사용자 지정 노트 세 개다. 새 파일은 전체 줄을 대조한다. 기존 파일은 작업 시작 시 `git diff -U0 HEAD -- <노트>`의 추가 줄을 대조한다. frontmatter와 빈 줄도 대상 줄 수에 포함한다.

현재 코드와 위키 원문을 직접 확인한다. 차이 결론은 비교 보고서와 호출 흐름 보고서의 마지막 `전수 검증 기록 (10-14)`을 우선 적용한다. 과거 코드 인용은 지정 커밋의 원문을 확인한다.

기계 확인 불일치 후보: 사용자 제공 목록에 후보가 없다.

노트별 완료 기록은 검증을 마친 순서대로 아래에 덧붙인다.

## 작업 시작 시 대상 줄

아래 줄 번호는 정정 전 노트에서 셌다. 기존 노트의 대상 줄은 지정된 읽기 전용 `git diff -U0 HEAD`에서 추출했다.

| 노트 | 대상 줄 수 | 대상 줄 번호 |
|---|---:|---|
| `roms_analytical_functionals-differences-1.md` | 166 | 1–166 |
| `roms_bulk_flux_coare.md` | 148 | 6, 8, 73–78, 88, 95–118, 126–134, 138–179, 183–185, 191–194, 200, 202–207, 211–215, 217–261 |
| `roms_4dvar_drivers.md` | 93 | 7–8, 22, 36, 49, 56, 58–61, 65, 74–80, 82, 99, 110–111, 135, 143–144, 183, 185, 192–257 |

총 대상 줄 수는 위 표의 합계인 407줄이다.

## 완료: roms_analytical_functionals-differences-1.md

대조한 줄 수는 새 파일 전체인 166줄이다. frontmatter 1–19행을 포함한다. 정정은 5줄이다. 보완은 0줄이다. 정정 수는 이 노트의 `[10-14 전수 검증 정정]` 표지가 있는 고유 줄에서 셌다.

차이 표 134행은 `note-job-16.tsv`의 해당 노트 배정 134행과 일대일로 대응한다. 각 행의 분류와 결론 문장을 해당 보고서의 최종 결론에 대조했다. A 13행의 커밋과 날짜는 A7·A8·D1 및 최종 보고서에 대조했다. RT1-538·547·548은 최종 보고서가 D1의 B를 A로 바꾼 판정을 따른다. E 1행인 RT1-1067의 근거 강도는 최종 보고서와 E2의 강함 판정에 맞는다. 이 수량은 노트의 차이 표에서 분류별로 셌다.

현재 코드·과거 커밋·위키 인용을 원문에서 확인했다. 부정 조건·반복 범위·수치·단위·식은 원문과 맞는다. 위키의 HTML 줄바꿈이 여러 표시 줄로 풀린 인용은 원래 물리 줄 범위와 맞는다. 함수 헤더 42개는 `ROMS/Functionals/*.h`에서 다시 셌다. `analytical.F`에는 `ana_vegetation.h`를 포함하는 지시문이 없다. COD 사례와 FJORD 분기가 없다는 서술은 현재 원본 저장소의 이름 검색과 맞는다.

정정 목록의 줄 번호는 정정 후 노트의 번호이다. 이번 정정은 줄 수를 바꾸지 않았다.

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `roms_analytical_functionals-differences-1.md:33` | 현행 `roms_analytical_functionals.md:145`를 수정 전 호흡률 설명의 위치로 인용했다. | 수정 전 노트 인용임을 밝히고 biology 보고서 NT-022의 1536행으로 연결했다. | `roms-biology-vs-code.md:1536`은 수정 전 문장을 보존한다. 현재 부모 노트 145행은 개경계조건 제목이다. |
| `roms_analytical_functionals-differences-1.md:34` | 현행 부모 노트 176행을 수정 전 헤더 수 설명의 위치로 인용했다. | 수정 전 노트 인용임을 밝히고 build-options-history 보고서 RBH-3507의 3625행으로 연결했다. | `roms-build-options-history-vs-code.md:3625`은 수정 전 문장을 보존한다. 현재 부모 노트 176행은 CPP 조건 표의 머리행이다. |
| `roms_analytical_functionals-differences-1.md:39` | 문서 칸과 이력 칸에서 현행 부모 노트 135행을 수정 전 `ana_hmixcoef` 설명의 위치로 인용했다. | 두 위치 모두 수정 전 노트 인용임을 밝히고 mixing-bc-forcing 보고서 RMF1-952의 1600행으로 연결했다. | `roms-mixing-bc-forcing-vs-code.md:1600`은 수정 전 문장을 보존한다. 현재 부모 노트 135행은 `canyon.h`의 `ANA_SMFLUX` 인용이다. |
| `roms_analytical_functionals-differences-1.md:45` | 현행 부모 노트 92행을 수정 전 바닥 flux 단위 설명의 위치로 인용했다. | 수정 전 노트 인용임을 밝히고 mixing-bc-forcing 보고서 RMF1-949의 1597행으로 연결했다. | `roms-mixing-bc-forcing-vs-code.md:1597`은 수정 전 문장을 보존한다. 현재 부모 노트 92행은 빈 줄이다. |
| `roms_analytical_functionals-differences-1.md:46` | 현행 부모 노트 126행을 수정 전 대기 함수 공통 조건의 위치로 인용했다. | 수정 전 노트 인용임을 밝히고 mixing-bc-forcing 보고서 RMF1-951의 1599행으로 연결했다. | `roms-mixing-bc-forcing-vs-code.md:1599`은 수정 전 문장을 보존한다. 현재 부모 노트 126행은 표면 응력 0.1 Pa 설명이다. |

모든 정정 표지는 결론 문장 칸 끝에 붙였다. 상대 링크의 대상 파일은 모두 존재한다. 절대 경로와 이중 대괄호는 없다. Mermaid 블록은 없다. 검증을 유보하는 한계 문장은 없다.

기계 확인 후보 판정: 사용자 제공 목록에 후보가 없다.

이 노트의 대상 줄 대조를 완료했다. 미해결 항목은 없다.

## 완료: roms_bulk_flux_coare.md

대조한 줄 수는 작업 시작 시 추가·수정된 148줄이다. frontmatter의 6행과 8행을 포함한다. 정정은 14줄이다. 보완은 0줄이다. 정정 수는 이번 작업에서 이 노트에 붙인 정정 표지의 고유 줄에서 셌다.

차이 표 36행은 `note-job-15.tsv`의 해당 노트 배정 36행과 일대일로 대응한다. 분류와 결론은 각 보고서의 최종본과 맞는다. A 10행의 `a4a82c5f`와 2023-07-01은 A7·A8의 판정과 맞는다. E 1행인 RMF1-870은 최종 보고서와 E2의 강함 판정을 따른다. 이 수량은 노트의 차이 표에서 분류별로 셌다.

본문 수정은 RBH-3509·3510·3511, RMF1-958·959·960·961·970, OMD-N012·N013·N014의 수정안에 대조했다. 삭제된 지역 운영 일반화는 RBH-3511의 근거 범위 구분에 맞는다. 삭제된 호출 순서와 후속 작업 목록은 호출 흐름 보고서 및 현재 호출 위치로 대체되어 있다. 원문의 Qair 메타데이터, Hair 연결, RH 분기, 측정 높이 검사, 내부 단위, NetCDF 환산, 장파 분기, 해빙 강우 식을 확인했다. Fortran 블록 두 개는 `bulk_flux.F:1102–1104,1111–1113`과 글자가 같다. 파일 길이 1623줄과 헤더의 논문 8편도 현재 파일에서 확인했다.

정정 목록의 줄 번호는 정정 후 노트의 번호이다. 이번 정정은 줄 수를 바꾸지 않았다.

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `roms_bulk_flux_coare.md:183` | BULK_FLUXES만 호출 조건으로 적었다. | FOUR_DVAR와 PRIOR_BULK_FLUXES를 함께 정의한 경로의 `Nrun.eq.1` 조건을 명시했다. | `ROMS/Nonlinear/main3d.F:441–449`의 두 호출 분기. `ROMS-callflow-nonlinear.md:224–225`의 3D-pre-21·22. |
| `roms_bulk_flux_coare.md:202` | 호출 위치를 `main3d.F:448` 하나로 적었다. | 조건부 호출을 포함한 `main3d.F:446,448`로 고쳤다. | `ROMS/Nonlinear/main3d.F:446`의 `IF (Nrun.eq.1) CALL bulk_flux (ng, tile)`와 448행의 일반 호출. |
| `roms_bulk_flux_coare.md:193` | CPP 노트의 위치를 `§7 BULK_FLUXES`로 적었다. | `§2.1의 항목 7(BULK_FLUXES)`로 고쳤다. | `roms-wiki-cppdefs-options.md:51–63`의 범주 표. 해당 노트의 §7은 관련 자료이다. |
| `roms_bulk_flux_coare.md:214` | CPP 노트의 위치를 `§7 BULK_FLUXES`로 적었다. | `§2.1의 항목 7(BULK_FLUXES)`로 고쳤다. | `roms-wiki-cppdefs-options.md:51–63`의 범주 표. |
| `roms_bulk_flux_coare.md:215` | 공식 자료 노트 §3에 Large KPP와 Fairall COARE 인용이 있다고 적었다. | 실제로 있는 §3.4의 Large et al. (1994) KPP 인용을 가리키도록 고쳤다. | `roms-official-resources.md:56–59`. 해당 노트에는 Fairall 인용이 없다. Fairall 출처는 이 노트 217행의 코드 헤더 링크로 연결된다. |
| `roms_bulk_flux_coare.md:226` | 현행 노트 105·111행을 수정 전 옵션 표의 위치로 인용했다. | 수정 전 노트 인용임을 밝히고 build-options-history 보고서 RBH-3510의 3628행으로 연결했다. | `roms-build-options-history-vs-code.md:3628`의 수정 전 표 인용. |
| `roms_bulk_flux_coare.md:230` | 현행 노트 106행을 수정 전 LONGWAVE_OUT 설명의 위치로 인용했다. | 수정 전 노트 인용임을 밝히고 mixing-bc-forcing 보고서 RMF1-959의 1612행으로 연결했다. | `roms-mixing-bc-forcing-vs-code.md:1612`의 수정 전 표 인용. |
| `roms_bulk_flux_coare.md:231` | 현행 노트 82행을 수정 전 Qair 단위 표의 위치로 인용했다. | 수정 전 노트 인용임을 밝히고 mixing-bc-forcing 보고서 RMF1-970의 1633행으로 연결했다. | `roms-mixing-bc-forcing-vs-code.md:1633`의 수정 전 표 인용. |
| `roms_bulk_flux_coare.md:235` | 현행 노트 110행을 수정 전 SPECIFIC_HUMIDITY 설명의 위치로 인용했다. | 수정 전 노트 인용임을 밝히고 mixing-bc-forcing 보고서 RMF1-958의 1611행으로 연결했다. | `roms-mixing-bc-forcing-vs-code.md:1611`의 수정 전 표 인용. |
| `roms_bulk_flux_coare.md:238` | 현행 노트 93–99행을 수정 전 출력 단위 표의 위치로 인용했다. | 수정 전 노트 인용임을 밝히고 mixing-bc-forcing 보고서 RMF1-960의 1613행으로 연결했다. | `roms-mixing-bc-forcing-vs-code.md:1613`의 수정 전 표 인용. |
| `roms_bulk_flux_coare.md:239` | 현행 노트 40–42행을 sensible·latent·net heat 목록의 위치로 인용했다. | 수정 전 노트 인용임을 밝히고 mixing-bc-forcing 보고서 RMF1-961의 1614행으로 연결했다. | `roms-mixing-bc-forcing-vs-code.md:1614`의 수정 전 목록. 현행 목록의 해당 항목은 41–43행이다. |
| `roms_bulk_flux_coare.md:244` | 위키 링크의 대상 문자열과 구분자를 원문 표시 글자에 남겼다. | `Sea-Ice_Model`과 `Parkinson and Washington`만 표시하도록 고쳤다. | `Radiant_Heat_Fluxes.wiki:2`의 링크 표시 글자. |
| `roms_bulk_flux_coare.md:245` | 위키 링크의 대상 문자열과 구분자를 원문 표시 글자에 남겼다. | `Sea-Ice_Model`과 `Parkinson and Washington`만 표시하도록 고쳤다. | `Radiant_Heat_Fluxes.wiki:2`의 링크 표시 글자. |
| `roms_bulk_flux_coare.md:261` | Fairall 인용 앞에 위키 링크의 대상 문자열과 구분자를 남겼다. | `Fairall et al. (1996)`으로 고쳤다. | `Old_Intro.wiki:19`의 링크 표시 글자. |

모든 정정 줄에 정정 표지를 붙였다. 차이 표의 표지는 결론 문장 칸 끝에 붙였다. 상대 링크의 대상 파일은 모두 존재한다. 절대 경로와 이중 대괄호는 없다. Mermaid 블록은 없다. 검증을 유보하는 한계 문장은 없다.

기계 확인 후보 판정: 사용자 제공 목록에 후보가 없다. 위키 표시 글자 정정은 이번 직접 대조에서 찾았다.

이 노트의 대상 줄 대조를 완료했다. 미해결 항목은 없다.

## 완료: roms_4dvar_drivers.md

대조한 줄 수는 93줄이다. frontmatter 7–8행을 포함한다. 정정은 10줄이다. 보완은 6줄이다. 각 수는 이 노트의 전수 검증 표지가 있는 고유 줄에서 셌다.

차이 표 51행은 `note-job-20.tsv`의 해당 노트 배정 51행과 일대일로 대응한다. 분류와 결론은 각 보고서의 최종본과 맞는다. A 8행의 커밋과 날짜는 A6·A8의 판정과 맞는다. DA1-404는 E1의 중간 판정을 따른다. RT2-383은 E1과 최종 보고서의 강함 판정을 따른다. 이 수량은 노트의 차이 표에서 분류별로 셌다.

본문은 RF2-021·022·032, DA1-805·806·809, RT2-392·393의 수정안과 대조했다. PUBLIC 목록과 실제 호출 순서를 구분한 수정은 보고서와 맞는다. prior_error의 선행 호출과 조건부 posterior 호출을 현재 원문에서 확인했다. I4DVAR 감도의 첫 외부 반복, v-space 왕복, 관측오차 역분산 배율은 원문과 맞는다. 기존 최소화기 한계 목록은 RF2-032와 RT2-393의 호출·대입 근거로 대체되어 있다. FSV 식과 전방·역방 시간 구간도 원문과 맞는다.

정정 목록의 줄 번호는 정정 후 노트의 번호이다. 이번 정정은 줄 수를 바꾸지 않았다.

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `roms_4dvar_drivers.md:22` | driver 파일 선택을 `MyAppCPP`에서 시작하는 구조로 적었다. | `Master/roms_kernel.F`의 CPP 분기가 파일을 선택한다고 고쳤다. | `Master/roms_kernel.F:114–194`의 driver별 include 분기. RF2-001은 현행 선택 위치를 이 파일로 지정한다. |
| `roms_4dvar_drivers.md:36` | R4D-Var의 inner 행렬 작용을 조건 없이 ADM·공분산·TLM으로 적었다. | `DATALESS_LOOPS`를 정의하지 않은 경로라는 조건을 붙였다. | `ROMS/Drivers/r4dvar.F:879`의 `# ifndef DATALESS_LOOPS`와 `:1211–1215`의 TLM 호출. RF2-022의 최종 결론. |
| `roms_4dvar_drivers.md:65` | increment 설명의 인용 위치를 `i4dvar.F:33–35`로 적었다. | 실제 increment 설명인 `ROMS/Drivers/i4dvar.F:30–31`로 고쳤다. | `:30–31`은 Ninner 반복과 dXa 계산을 설명한다. `:33–35`는 analysis 설명이다. |
| `roms_4dvar_drivers.md:111` | 역관측오차 분산 배율을 감도 출력 전체의 설명으로 적었다. | I4DVAR 감도 출력으로 범위를 명시했다. | `ROMS/Utility/obs_write.F:1227`의 `#  ifdef I4DVAR_ANA_SENSITIVITY`와 `:1228`의 ObsErr 곱. DA1-806의 수정안. |
| `roms_4dvar_drivers.md:208` | 현행 노트 57행을 수정 전 PUBLIC 순서 문장의 위치로 인용했다. | 수정 전 노트 인용임을 밝히고 호출 흐름 보고서 RF2-021의 3719행으로 연결했다. | `ROMS-callflow-da.md:3719`의 수정 전 문장. |
| `roms_4dvar_drivers.md:209` | 현행 노트 171행을 수정 전 R4 커널 목록의 위치로 인용했다. | 수정 전 노트 인용임을 밝히고 호출 흐름 보고서 RF2-022의 3722행으로 연결했다. | `ROMS-callflow-da.md:3722`의 `NLM+RPM+ADM` 인용. |
| `roms_4dvar_drivers.md:210` | 수정 전 노트의 미추적·미검증 문구를 차이 표에 남겼다. | 수정 전 최소화기 호출과 생산·소비 위치의 누락으로 설명했다. | `ROMS-callflow-da.md:3726`의 RF2-032 수정안. 원래 한계 문장 대신 확보한 호출·대입 근거를 연결하도록 한다. |
| `roms_4dvar_drivers.md:234` | 현행 노트 101행을 수정 전 I4DVAR 감도 문장의 위치로 인용했다. | 수정 전 노트 인용임을 밝히고 da-4dvar 보고서 DA1-806의 876행으로 연결했다. | `roms-da-4dvar-vs-code.md:876`의 수정 전 감도 설명. |
| `roms_4dvar_drivers.md:252` | 현행 노트 91행을 수정 전 영향·감도 문장의 위치로 인용했다. | 수정 전 노트 인용임을 밝히고 da-representer 보고서 RT2-392의 735행으로 연결했다. | `roms-da-representer-vs-code.md:735`의 수정 전 설명. |
| `roms_4dvar_drivers.md:253` | solver 미추적 문구를 남겼다. 참조 보고서를 “이 보고서”로 적었다. | solver 선택·반복·가중치 근거의 누락으로 설명했다. da-representer 보고서 RT2-367–370으로 직접 연결했다. | `roms-da-representer-vs-code.md:736`의 RT2-393 수정안과 `:1129`의 최종 결론. |

아래 보완은 결론 문장을 바꾸지 않고 실제 호출·대입 인용을 보탠 것이다.

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `roms_4dvar_drivers.md:231` | SKIP_NLM과 BGQC의 전처리 조건만 인용했다. | LCZ에서 ObsScale을 읽는 호출을 보탰다. | `ROMS/Drivers/obs_sen_i4dvar_analysis.h:370–371`의 `netcdf_get_fvar`와 `Vname(1,idObsS), ObsScale`. DA1-703. |
| `roms_4dvar_drivers.md:233` | `ad_variability` 호출 하나를 인용했다. | 수반·접선 변환, 조건부 balance, Lanczos 내적·가중 합, 접선 적분의 호출·대입을 보탰다. | `ROMS/Drivers/obs_sen_i4dvar_analysis.h:685–689,801–804,855,857`. `ROMS/Utility/ini_lanczos.F:476,601,603,605`. DA1-717. |
| `roms_4dvar_drivers.md:240` | I4DVAR_ANA_SENSITIVITY의 전처리 조건만 인용했다. | 배율 대입과 ObsImpact_total 쓰기 조건·호출을 보탰다. | `ROMS/Utility/obs_write.F:1228,1624–1626,1630–1633`의 ObsErr 곱과 TLmodVal 출력. DA1-718. |
| `roms_4dvar_drivers.md:245` | background·외부 반복·공분산 호출만 인용했다. | DATALESS_LOOPS 조건과 ADM·TLM·RPM의 실제 호출을 보탰다. | `ROMS/Drivers/r4dvar.F:879,906,908,1074,1076,1212,1214,1694,1696`. RT2-365와 RF2-022. |
| `roms_4dvar_drivers.md:246` | 사후 오차 옵션 조건의 앞 두 줄만 인용했다. | POSTERIOR_ERROR_I 조건과 Nouter 검사·오류 대입·반환을 보탰다. | `ROMS/Utility/read_phypar.F:8025,8033,8038–8039`의 `IF (Nouter.gt.1) THEN`, `exit_flag=5`, `RETURN`. RT2-375. |
| `roms_4dvar_drivers.md:249` | ImpOrd의 1차·2차 설명 주석만 인용했다. | 실제 기본 대입인 `ImpOrd=3`을 보탰다. | `ROMS/Drivers/obs_sen_rbl4dvar_forecast.h:573`. RT2-378. |

현재 코드·과거 커밋·위키 인용을 원문에서 확인했다. 인용 뒤 발췌가 없는 경로도 해당 줄의 문맥에 대조했다. 모든 정정·보완 줄에 해당 표지를 붙였다. 차이 표의 표지는 결론 문장 칸 끝에 붙였다. 상대 링크의 대상 파일은 모두 존재한다. 절대 경로와 이중 대괄호는 없다. Mermaid 블록은 없다. 검증을 유보하는 한계 문장은 없다.

기계 확인 후보 판정: 사용자 제공 목록에 후보가 없다.

이 노트의 대상 줄 대조를 완료했다. 미해결 항목은 없다.

## 전체 완료 집계

| 노트 | 대조한 줄 수 | 정정 수 | 보완 수 |
|---|---:|---:|---:|
| `roms_analytical_functionals-differences-1.md` | 166 | 5 | 0 |
| `roms_bulk_flux_coare.md` | 148 | 14 | 0 |
| `roms_4dvar_drivers.md` | 93 | 10 | 6 |
| 합계 | 407 | 29 | 6 |

집계는 작업 시작 시 대상 줄과 이번 전수 검증 표지를 기준으로 했다. 작업 시작 시 노트와 수정 후 노트를 줄별로 비교했다. 이번 변경은 모두 대상 줄 안에 있다. 세 노트의 물리 줄 수는 바뀌지 않았다. 정정·보완한 줄은 합계 35줄이다. 이 수는 정정 29줄과 보완 6줄의 합이다. `git diff --check`는 오류 없이 끝났다.

대상 노트의 대상 줄을 모두 대조했다. 미해결 항목은 없다.
