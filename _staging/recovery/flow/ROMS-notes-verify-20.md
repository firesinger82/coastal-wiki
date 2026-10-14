# ROMS 노트 전수 검증 20 (2026-10-14)

## 검증 범위

- 기존 노트의 대상은 작업 시작 시 `git diff -U0 HEAD -- <노트>`가 표시한 모든 추가 줄이다.
- 새 노트 `roms-version-history-differences.md`의 대상은 파일 전체 줄이다.
- frontmatter와 빈 줄을 대조 줄 수에 포함한다.
- 원문과 보고서의 최종 검증 기록을 기준으로 판정한다.
- 노트별 완료 기록은 대조를 마친 뒤 추가한다.

## 기계 확인 후보 판정

- 사용자에게 받은 불일치 후보는 없다.

## roms_nonlinear_core_remaining.md 완료

- 대상 파일: `models/ROMS/source-analysis/roms_nonlinear_core_remaining.md`.
- 대조한 줄 수는 111줄이다. 작업 시작 diff의 추가 줄을 셌다.
- 차이 표 69행은 배정표 `note-job-20.tsv`의 해당 노트 행과 같다.
- 정정 수는 1줄이다. 보완 수는 1줄이다.
- 표의 분류와 결론 문장은 각 보고서의 최종 결론과 대조했다. 추가한 커밋 정보와 E 후보의 강도는 A8·E1·E2 판정과 대조했다.
- 본문은 보고서 수정안 21행과 대조했다. 삭제한 호출 순서와 구판 줄 번호 설명은 RF1-021·RF1-031·RTN-389의 수정 근거와 대조했다.
- 현재 코드와 위키의 인용 위치를 열었다. 과거 판 인용은 해당 커밋의 `git show`로 열었다. 표에 인용한 수정 전 노트 문장은 보고서와 diff의 삭제 줄로 대조했다.
- frontmatter의 반영 날짜와 방법을 확인했다. 상대 링크의 대상 파일이 존재한다. 금지된 절대 경로와 위키 링크 표기 및 한계 문장은 없다. 대상 줄에 mermaid 블록은 없다.

| 구분 | 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| 보완 | `roms_nonlinear_core_remaining.md:56` | DiaRU·DiaRV 저장의 근거를 `prsgrd31.h:241-243,287-289`로 인용했다. 이 위치에는 DiaRU만 있다. | DiaRV 저장 위치 `325-327,371-373`을 함께 인용했다. | `ROMS/Nonlinear/prsgrd31.h:326`의 `DiaRV(i,j,N(ng),nrhs,M3pgrd)=rv(i,j,N(ng),nrhs)`와 `372`의 `DiaRV(i,j,k,nrhs,M3pgrd)=rv(i,j,k,nrhs)`이다. 보고서 OMD-N009의 저장 설명을 뒷받침한다. |
| 정정 | `roms_nonlinear_core_remaining.md:140` | `IF (Master) THEN`이 TIME-STEP 열 제목과 자료를 함께 출력한다고 적었다. | 열 제목의 첫 출력·Master·격자 1 조건과 자료 행의 Master 조건을 구분했다. | `ROMS/Nonlinear/diag.F:445-447`의 `IF (first_time(ng).eq.0) THEN`과 `IF (Master.and.(ng.eq.1)) THEN`이다. 자료 행은 `471-497`의 `IF (Master) THEN`에서 출력한다. 보고서 OMD-N047의 출력 설명과 대조했다. |

- 기계 확인 후보 판정: 없음.
- 미해결 항목: 없음.

## roms_horizontal_mixing.md 완료

- 대상 파일: `models/ROMS/source-analysis/roms_horizontal_mixing.md`.
- 대조한 줄 수는 78줄이다. 작업 시작 diff의 추가 줄을 셌다.
- 차이 표 44행은 `note-job-13.tsv`의 해당 노트 배정과 같다. 분류와 결론은 최종 보고서와 같다. 이 표에는 A·E 행이 없다.
- 정정 수는 3줄이다. 보완 수는 1줄이다.
- 본문은 RMF1-928·RMF1-929·RMF1-930·RTN-399 수정안과 대조했다. 성능 일반화 문장의 삭제는 RMF1-929에 근거한다.
- 모든 대상 줄의 코드·위키 인용 위치를 열었다. Smagorinsky의 계수식과 제곱근 처리 및 TS_MIX_STABILITY·TS_MIX_CLIMA의 분기 순서를 확인했다.
- frontmatter에 적힌 hmixing.F의 835줄은 현재 파일의 줄 수와 같다. 상대 링크가 가리키는 파일은 모두 존재한다. 금지 문자열과 한계 문장은 없다. 대상 줄에 mermaid 블록은 없다.

| 구분 | 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| 정정 | `roms_horizontal_mixing.md:20` | hmixing의 동적 계수를 visc2·visc4·diff2·diff4와 연결했다. | Smagorinsky 경로의 저장 배열을 운동량 visc3d_r와 추적자 diff3d_r로 구분했다. | `ROMS/Nonlinear/hmixing.F:334-347,388-401`의 두 계수 대입이다. 보고서 RMF1-928·RTN-399는 초기 격자 계수와 변형률 계수의 경로를 구분한다. |
| 보완 | `roms_horizontal_mixing.md:32` | VISC_GRID·DIFF_GRID 설명에 VISC_GRID 위치만 인용했다. | DIFF_GRID 위치 `340-364`를 추가했다. | `ROMS/Utility/ini_hmixcoef.F:340`의 `#if defined DIFF_GRID && defined SOLVE3D`와 `351,361`의 diff2·diff4 대입이다. |
| 정정 | `roms_horizontal_mixing.md:47` | Hviscosity를 산출값으로 적었다. step3d_uv를 수평 혼합 호출 위치로 적었다. | Hviscosity와 Hdiffusion을 입력으로 구분했다. 수평 혼합 호출 위치를 rhs3d로 고쳤다. | `ROMS/Nonlinear/hmixing.F:192,195`의 두 `intent(in)` 선언이다. 호출은 `ROMS/Nonlinear/rhs3d.F:113,121,201,209`에 있다. |
| 정정 | `roms_horizontal_mixing.md:61` | 연결 설명에 Hviscosity를 운동량·추적자 확산의 산출값으로 적었다. | 연결 설명을 rhs3d의 운동량·추적자 수평 혼합 호출로 고쳤다. | `ROMS/Nonlinear/rhs3d.F:108-122,200-210`의 호출문이다. |

- 기계 확인 후보 판정: 없음.
- 미해결 항목: 없음.

## roms_atmospheric_forcing.md 완료

- 대상 파일: `models/ROMS/source-analysis/roms_atmospheric_forcing.md`.
- 대조한 줄 수는 95줄이다. 작업 시작 diff의 추가 줄을 셌다.
- 차이 표 42행은 `note-job-14.tsv`의 해당 노트 배정과 같다. 결론 분류와 문장은 최종 보고서와 같다.
- 정정 수는 0줄이다. 보완 수는 2줄이다.
- A 행의 a4a82c5f·df538798 커밋과 날짜는 A7·A8 판정서와 같다. 해당 과거 YAML도 열었다. 이 표에는 E 행이 없다.
- 본문은 적용 기록의 수정안 12행과 대조했다. COARE_30 조건과 WIND_MINUS_CURRENT 조건을 확인했다. 습도 분기와 열속 환산 및 출력 선택 조건을 확인했다. Working Rules의 적용 권고 삭제는 RMF1-962에 근거한다.
- 코드·위키·입력 예제·CDL의 인용 위치를 열었다. 자료 결합 경로의 단위·부호·배율은 최종 보고서와 대조했다.
- frontmatter의 반영 날짜와 방법을 확인했다. 상대 링크가 가리키는 파일은 모두 존재한다. 금지 문자열과 작업 한계 문장은 없다. 대상 줄에 mermaid 블록은 없다.

| 구분 | 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| 보완 | `roms_atmospheric_forcing.md:148` | 계수 배열이 9개 원소라고 설명하면서 수형 7까지만 나오는 `1635-1644`를 인용했다. | 수형 9까지의 목록과 세 배열의 `dimension(9)` 선언을 추가했다. | `ROMS/Modules/mod_scalars.F:1635-1646,1657-1667`이다. 보고서 RMF1-973도 세 배열 선언을 인용한다. |
| 보완 | `roms_atmospheric_forcing.md:197` | Qair에서 Hair로 읽는다는 설명에 HairG 판독 위치만 인용했다. | HairG를 Hair에 전달하는 set_data의 인용을 추가했다. | `ROMS/Nonlinear/get_data.F:530-539`는 HairG에 읽는다. `ROMS/Nonlinear/set_data.F:246-250`은 HairG와 Hair를 set_2dfld_tile에 전달한다. 보고서 RMF1-957의 변수 대응과 같다. |

- 기계 확인 후보 판정: 없음.
- 미해결 항목: 없음.

## roms_baroclinic_3d.md 완료

- 대상 파일: `models/ROMS/source-analysis/roms_baroclinic_3d.md`.
- 대조한 줄 수는 83줄이다. 작업 시작 diff의 추가 줄을 셌다.
- 차이 표 22행은 `note-job-12.tsv`의 해당 노트 배정과 같다. 분류와 결론 문장은 최종 보고서와 같다.
- 정정 수는 2줄이다. 보완 수는 0줄이다.
- E 후보 RI1-0670의 강함 판정은 E1 판정서와 같다. 이 표에는 A 행이 없다. RTN-274의 최종 B 판정을 유지했다.
- 본문은 입력·이론·생물·도구 보고서의 해당 수정안과 비선형 호출 흐름 보고서의 N-01·N-02·RF1-025를 대조했다. 성능 증가율 문장의 삭제는 RTN-408·RTG-1984에 근거한다.
- 현재 코드와 위키의 인용 위치를 열었다. dd995fa2의 과거 입력 검사를 열었다. Fennel 주석의 여섯 줄은 `fennel.h:1542-1547`과 같다.
- frontmatter의 반영 날짜와 방법을 확인했다. 상대 링크가 가리키는 파일은 모두 존재한다. 대상 줄에 금지 문자열과 작업 한계 문장은 없다. 대상 줄에 mermaid 블록은 없다.

| 구분 | 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| 정정 | `roms_baroclinic_3d.md:47` | GLS_MIXING만 gls_corstep의 선택 조건으로 적었다. | 앞선 MY25_MIXING 분기가 선택되지 않는 조건을 추가했다. | `ROMS/Nonlinear/main3d.F:1027-1030`의 `# ifdef MY25_MIXING` 다음에 `# elif defined GLS_MIXING`이 있다. 호출 흐름 보고서 N-02는 CPP 조건을 함께 인용하도록 요구한다. |
| 정정 | `roms_baroclinic_3d.md:106` | SALINITY와 SED_DENS 조건만으로 저장 rho 식을 설명했다. | NONLIN_EOS가 정의되지 않은 선형 분기의 마스크 적용 전 식으로 한정했다. | `ROMS/Nonlinear/rho_eos.F:699-716`의 선형 대입 뒤 `717-718`에서 MASKING에 따라 rmask를 곱한다. RTN-390·RF1-025의 선형 EOS 설명과 대조했다. |

- 기계 확인 후보 판정: 없음.
- 미해결 항목: 없음.

## roms-version-history-differences.md 완료

- 대상 파일: `models/ROMS/manual-notes/roms-version-history-differences.md`.
- 대조한 줄 수는 31줄이다. 새 파일 전체 줄을 셌다.
- 차이 표 2행은 `note-job-2.tsv`의 해당 노트 배정과 같다. RBH-3424의 C와 RTN-329의 A를 최종 보고서와 대조했다.
- 정정 수는 0줄이다. 보완 수는 1줄이다.
- 메모리 보고는 nl_roms.h의 호출부터 memory.F의 실제 출력 조건까지 대조했다. ChangeLog의 2026 링크는 연간 비교 링크이다.
- RTN-329의 커밋·날짜는 A8 판정서와 같다. 0a315abb의 ROMS/Version과 roms-4.0의 버전 문자열 및 fcba9f6d 부모 판의 ROMS/Version을 열었다. 현재 코드의 버전 문자열은 4.3이다.
- frontmatter 전체를 확인했다. related에 적힌 노트가 존재한다. 문서 판의 다운로드 날짜는 manifest.json과 같다. 코드 HEAD는 57aecf589a408b1e5490d2db7f9bd0196062a44e이다.
- 상대 링크가 가리키는 파일은 모두 존재한다. 금지 문자열과 작업 한계 문장은 없다. mermaid 블록은 없다.

| 구분 | 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| 보완 | `roms-version-history-differences.md:25` | 릴리스 표의 current 셀만 인용했다. | 같은 행의 revision·날짜·파일 수·줄 수 셀을 추가했다. | `Regional_Ocean_Modeling_System__ROMS_.wiki:190-193`의 표시 글자는 각각 `1123`, `2022-04-25`, `1,989`, `1,079,102`이다. RTN-329와 A8의 판정 범위를 직접 뒷받침한다. |

- 기계 확인 후보 판정: 없음.
- 미해결 항목: 없음.

## 최종 집계

| 노트 | 대조한 줄 수 | 정정 수 | 보완 수 | 차이 표 행 수 |
|---|---:|---:|---:|---:|
| roms_nonlinear_core_remaining.md | 111 | 1 | 1 | 69 |
| roms_horizontal_mixing.md | 78 | 3 | 1 | 44 |
| roms_atmospheric_forcing.md | 95 | 0 | 2 | 42 |
| roms_baroclinic_3d.md | 83 | 2 | 0 | 22 |
| roms-version-history-differences.md | 31 | 0 | 1 | 2 |
| 합계 | 398 | 6 | 5 | 179 |

- 대조 줄 수는 기존 노트의 작업 시작 diff 추가 줄 367개와 새 노트 전체 31줄의 합이다.
- 정정·보완 수는 이번에 붙인 `[10-14 전수 검증 정정]`·`[10-14 전수 검증 보완]` 태그가 있는 줄을 각각 센 값이다.
- 차이 표의 179행은 모두 6열이다. 분류와 결론은 최종 보고서의 의미를 유지한다.
- 대상 줄의 상대 링크 90개는 모두 실제 파일을 가리킨다. frontmatter는 YAML 파싱을 통과했다. 노트는 Markdown 파싱을 통과했다.
- 형식 검사와 작업 한계 문장 검사의 범위는 사용자 지정 대상 줄이다. 대상 줄에 mermaid 블록은 없다.
- 외부 원문 보고서의 마지막 「Claude 확인과 보완」에 있는 행 ID는 이번 차이 표에 없다.
- 대상 경로의 읽기 전용 `git diff --check HEAD`는 통과했다.
- 대상 노트와 이 기록만 수정했다. git 쓰기 명령과 sudo 및 모델 실행은 사용하지 않았다.
- 미해결 항목은 없다. 지정한 대상 줄의 대조를 모두 마쳤다.
