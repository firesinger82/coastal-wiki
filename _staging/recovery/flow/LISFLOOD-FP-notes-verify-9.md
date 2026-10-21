# LISFLOOD-FP 노트 전수 대조 9

작업일: 2026-10-21.

대상 줄은 작업 시작 시 각 노트의 `git diff -U0 HEAD -- <노트>`에서 센 추가 줄이다. 빈 줄과 frontmatter를 포함한다. 정정 수와 보완 수는 각각 표시를 붙인 대상 줄 수로 집계한다. 완료 후 줄 번호는 최종 노트를 기준으로 적는다.

| 노트 | 시작 시 대상 줄 수 | 시작 시 대상 줄 범위 | 상태 |
|---|---:|---|---|
| `models/LISFLOOD-FP/source-analysis/lisflood-fp-lisflood2-driver.md` | 119 | 7–8, 12, 21–23, 27, 42–43, 65–67, 86, 95–96, 100–107, 124–128, 159–162, 174, 176–179, 188, 190–270 | 완료 |
| `models/LISFLOOD-FP/source-analysis/lisflood-fp-classic-acc-flow.md` | 118 | 7–8, 12–13, 18, 32, 40–41, 43, 47–50, 54, 58–70, 129–133, 215–218, 248–249, 278–281, 285–295, 313–315, 338, 343–403 | 완료 |

기계 확인 후보 판정: 사용자 제공 후보 없음.

노트별 완료 결과는 아래에 덧붙인다.

## lisflood-fp-lisflood2-driver.md — 완료

[대상 노트](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-lisflood2-driver.md)의 대상 119줄을 모두 대조했다. 정정은 8줄이다. 인용 보완은 2줄이다. 아래 줄 번호는 이 노트의 최종 줄 번호이다. 코드 경로는 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/` 기준이다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `lisflood-fp-lisflood2-driver.md:86` | 정정 | `_CALCULATE_Q_MODE=1`의 인용 `config.default.cmake:4` → `config.default.cmake:6` | 4행은 `add_compile_definitions(_PROFILE_MODE=0)`이다. 6행은 `add_compile_definitions(_CALCULATE_Q_MODE=1)`이다. |
| `lisflood-fp-lisflood2-driver.md:159` | 보완 | `.Vx`·`.Vy`의 인용 `lis2_output.cpp:357–371` → `lis2_output.cpp:357–371,382–396` | `lisflood2/lis2_output.cpp:357–371`은 x 방향을 처리한다. 382–396행은 y 방향을 처리한다. 각 분기는 large sub-grid 셀의 면 유속을 0으로 쓴다. |
| `lisflood-fp-lisflood2-driver.md:176` | 정정 | 루트 파일처럼 적은 `file_tool.cpp`와 축약 인용 → `lisflood2/file_tool.cpp`의 기능별 정확한 범위. 차원·압축 설명을 문장별로 분리했다. | `lisflood2/file_tool.cpp:150–153`의 `NC_NETCDF4`, 164–165행의 `NC_UNLIMITED`, 229–241행의 y·x·y_edge·x_edge 정의, 191–217행의 `#ifdef LATLONGMODE`, 44–47·80–82행의 `nc_def_var_deflate`, 169–189행의 time 변수 정의를 대조했다. |
| `lisflood-fp-lisflood2-driver.md:197` | 보완 | H·Q 해제 인용 `lisflood_processing.cpp:2092–2123` → `lisflood_processing.cpp:1536–1542,2092–2123` | `lisflood2/lisflood_processing.cpp:1536–1542`의 `#ifndef RESULT_CHECK` 안에서 원래 Qx·Qy를 해제한다. 2092–2123행의 같은 조건 안에서 원래 H를 해제한다. |
| `lisflood-fp-lisflood2-driver.md:203` | 정정 | DOCX 판 이력의 맨 위가 5.9 → p.5(변환본)의 맨 위에 밑줄로 추가한 8.0이 있음 | `lf-manual-docx-005.png`의 판 이력 첫 행은 밑줄로 표시한 `8.0`이다. 다음 행이 `5.9`이다. |
| `lisflood-fp-lisflood2-driver.md:236` | 정정 | LV1-251의 DOCX·PDF 인용 `표 4–6` → `표 5–11` | DOCX p.19–26 및 PDF p.15–21 쪽 이미지의 매개변수 목록은 표 5–11이다. `SGC_enable`·`SGCd8` 누락 판정은 유지한다. |
| `lisflood-fp-lisflood2-driver.md:237` | 정정 | LV1-256의 DOCX·PDF 인용 `표 4–6` → `표 5–11` | 같은 쪽 이미지에서 `ascii_out`·`standard_extensions_out`의 부재를 대조했다. |
| `lisflood-fp-lisflood2-driver.md:238` | 정정 | LV1-259의 DOCX·PDF 인용 `표 4–6` → `표 5–11` | 같은 쪽 이미지에서 `damfile`·`dammask`의 부재를 대조했다. |
| `lisflood-fp-lisflood2-driver.md:239` | 정정 | LV1-261의 DOCX·PDF 인용 `표 4–6` → `표 5–11` | 같은 쪽 이미지에서 `max_Froude`의 부재를 대조했다. |
| `lisflood-fp-lisflood2-driver.md:240` | 정정 | LV1-262의 DOCX·PDF 인용 `표 4–6` → `표 5–11` | 같은 쪽 이미지에서 `saveint_max`·`maxint`의 부재를 대조했다. |

차이 표 58행의 최종 분류와 결론을 `LISFLOOD-FP-final-conclusions.tsv` 및 지정된 `conclusion-verify` 행과 대조했다. E 행의 강도도 일치한다. `conclusion-claude-final.md`의 세 조정 행과 `external-sources.md` 끝 절의 조정 행은 이 노트의 배정 행에 포함되지 않는다. A 행은 이전 배포본과 판 이력으로 대조했다. 8.3 패치의 변경 파일 목록을 함께 대조했다.

본문 수정은 관련 보고서 §4, callflow §6 및 `notes-apply-5.md`와 대조했다. 변경 전 설명은 `bf804e23`의 노트 원문과 대조했다. 조건·부호·매크로·수량은 인용 파일의 문맥을 열어 대조했다. 문서의 식·숫자·표는 쪽 이미지로 판정했다. frontmatter와 제목·빈 줄·표 구분선도 대상 줄 집계에 포함했다.

이 노트에는 Mermaid 블록이 없다. Markdown 상대 링크와 frontmatter의 관련 노트 경로는 모두 존재한다. 지정된 절대 경로·홈 경로·위키 링크 문자열은 없다. 금지된 한계 문장은 없다. 기계 확인 후보 판정: 사용자 제공 후보 없음. 미해결 항목은 없다.

## lisflood-fp-classic-acc-flow.md — 완료

[대상 노트](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-classic-acc-flow.md)의 대상 118줄을 모두 대조했다. 정정은 3줄이다. 인용 보완은 0줄이다. 아래 줄 번호는 이 노트의 최종 줄 번호이다. 코드 경로는 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/` 기준이다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `lisflood-fp-classic-acc-flow.md:32` | 정정 | 파일 생성 이력의 `VersionHistory.h:293` → `VersionHistory.h:299–300`. 아키텍처 맵의 옛 “Trent — 추가 dynamic 처리”를 대체하라는 문장 → 현재 맵도 Roe 해법으로 분류한다는 문장 | v8.2의 이력은 `VersionHistory.h:293–294`에 있다. 현재 이력은 299–300행의 `Nov 10 2008 4.1.0` 및 `New file fp_trent.cpp`이다. `fp_trent.cpp:3`은 `ROE APPROXIMATE RIEMANN SOLVER 1st ORDER SCHEME`이다. `fp_flow.cpp:50`은 `CalcFPQxRoe`를 호출한다. `lisflood-theory-vs-code.md` §4의 LT1-413 수정안과 현재 아키텍처 맵 §2.1이 같은 분류를 쓴다. |
| `lisflood-fp-classic-acc-flow.md:343` | 정정 | `물리 충실도: diffusive < ACC < Roe < (FV1/DG2)` → 확산파·ACC의 생략 항과 Roe·FV1·DG2의 완전 천수방정식 분류. θ=1의 ACC 식 설명은 유지했다. | `lf-manual-pdf-010.png` 표 1은 확산파의 국소·이류 가속도 생략과 ACC의 이류 가속도 생략을 구분한다. `lf-manual-docx-013.png` 표 1의 Roe·FV1·DG2는 모두 `All terms`·`None`이다. `lisflood-docx-manual-vs-code.md`의 LV1-012·013·020은 생략 항과 성능 주장을 구분한다. `lisflood-theory-vs-code.md`의 LT1-075는 Roe 유량과 두 운동량 갱신을 확인한다. 이 근거에는 Roe보다 FV1·DG2의 물리 충실도가 높다는 순위가 없다. `fp_acc.cpp:88,93–94`는 θ=1의 식 대응을 뒷받침한다. |
| `lisflood-fp-classic-acc-flow.md:347` | 정정 | DOCX 판 이력의 맨 위가 5.9 → p.5(변환본)의 맨 위에 밑줄로 추가한 8.0이 있음 | `lf-manual-docx-005.png`의 판 이력 첫 행은 밑줄로 표시한 `8.0`이다. 다음 행이 `5.9`이다. |

차이 표 47행의 분류와 결론을 `LISFLOOD-FP-final-conclusions.tsv` 및 지정된 `conclusion-verify` 행과 대조했다. 문서 이름의 풀어쓰기와 수식 인용 기호를 제외하면 결론 문장이 일치한다. E 행 LB1-374의 강도는 중간으로 일치한다. `conclusion-claude-final.md`와 `external-sources.md` 끝 절의 조정 행은 이 노트의 배정 행에 포함되지 않는다.

A 행의 문서 판은 표지와 쪽 이미지로 대조했다. drychecking·MomentumThresh의 기본값은 v8.0·v8.1·v8.2의 실제 대입과 대조했다. resettimeinit은 v8.0과 현재 `iterateq.cpp:177–201`의 조건·NULLVAL·시간 환산을 대조했다. Metal FV1은 v8.2의 CPU 호출과 8.3 패치 282–295행을 구분했다.

본문 수정은 보고서 §4의 LN1-240·LI1-366·LT1-412·LB1-399·LV1-017·272·LG2-008 및 callflow §6과 대조했다. 변경 전 설명은 `bf804e23`의 노트 원문과 대조했다. `if(MH > Solverptr->DepthThresh)`의 반대 분기는 등호를 포함한다. QL 제한식의 분모 8과 부호 보존은 코드와 일치한다. bridge 문서 식 [9]의 분모 4와 반대 부호는 p.48 이미지로 대조했다. 식 [16]·[17]은 p.49–50 이미지로 대조했다. `mint_hk`의 표본화와 시간 단위는 실제 누적식과 대조했다. 하도 호출과 BankQ의 읽기 순서는 `iterateq.cpp`·`ch_flow.cpp`에서 대조했다. 초기 Q 배열은 `input.cpp:1371–1372`와 `utility.cpp:6–16`에서 확인했다. 체크포인트 Q 복구는 `chkpnt.cpp:138–139`에서 확인했다.

frontmatter와 링크만 바뀐 줄도 원문 대조에 포함했다. 빈 줄과 표 구분선도 대상 줄 집계에 포함했다. 이 노트에는 Mermaid 블록이 없다. Markdown 상대 링크와 frontmatter의 관련 노트 경로는 모두 존재한다. 지정된 절대 경로·홈 경로·위키 링크 문자열은 없다. 금지된 한계 문장은 없다. 기계 확인 후보 판정: 사용자 제공 후보 없음. 미해결 항목은 없다.

## 최종 집계

| 노트 | 대조한 대상 줄 | 정정 줄 | 보완 줄 | 상태 |
|---|---:|---:|---:|---|
| lisflood-fp-lisflood2-driver.md | 119 | 8 | 2 | 완료 |
| lisflood-fp-classic-acc-flow.md | 118 | 3 | 0 | 완료 |
| 합계 | 237 | 11 | 2 | 완료 |

집계 근거는 작업 시작 시 저장한 두 노트의 추가 줄 목록과 최종 표시이다. 정정·보완한 13줄은 모두 시작 시 대상 줄에 속한다. 수정 후 읽기 전용 `git diff -U0 HEAD -- <노트>`의 추가 줄 수는 각각 119줄과 118줄이다. 차이 표 105행의 분류·E 강도·결론 문장 대조에서 불일치는 없다. 표의 열 수와 정정 표시 위치도 점검했다. 사용자 제공 기계 확인 후보는 없다. 대상 줄 대조를 완료했으므로 작업을 종료한다.
