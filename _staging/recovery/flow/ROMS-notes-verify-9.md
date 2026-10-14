# ROMS 노트 전수 대조 기록 9

- 작업일: 2026-10-14.
- 대상: `models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-4.md`.
- 대상 범위: 새 파일의 전체 221줄이다. 작업 시작 시 파일의 물리 줄을 셌다. Frontmatter와 빈 줄을 포함한다.
- 대조 기준: 사용자 지정 원문과 대조 보고서의 최종 검증 기록이다.
- 기계 확인 불일치 후보: 사용자 제공 목록에 후보가 없다.

## 진행 기록

- 검증 기록 파일을 먼저 만들었다. 노트의 전체 줄 대조를 시작한다.

## roms-wiki-cppdefs-options-differences-4.md — 완료

- 대상 노트: [roms-wiki-cppdefs-options-differences-4.md](../../../models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-4.md).
- 대조한 줄 수: 221줄이다. 작업 시작 시의 1–221행 전체를 대조했다. Frontmatter와 빈 줄을 포함한다.
- 정정 수: 14줄이다. 노트의 `[10-14 전수 검증 정정]` 태그가 붙은 물리 줄을 셌다.
- 보완 수: 2줄이다. 노트의 `[10-14 전수 검증 보완]` 태그가 붙은 물리 줄을 셌다.
- 변경한 줄 수: 16줄이다. 정정 줄과 보완 줄은 중복되지 않는다.
- 수정 후에도 노트는 221줄이다. 아래 위치는 수정 전후에 같다.

### 전체 줄 대조 범위

아래 수량은 대상 노트의 물리 줄에서 셌다. 표의 구간은 서로 겹치지 않는다.

| 노트 줄 | 줄 수 | 대조 내용과 근거 |
|---|---:|---|
| 1–14 | 14 | Frontmatter를 부모 노트와 반영 기록에 대조했다. 날짜와 작성자 표기를 확인했다. |
| 15–24 | 10 | 부모 노트 링크, 제목, 빈 줄, 판본 설명, 표 머리말을 확인했다. 위키 manifest의 취득일은 2026-05-03이다. 코드 HEAD의 저자 날짜는 2026-09-18이다. `ROMS/Modules/mod_ncparam.F:653`의 version은 `4.3`이다. |
| 25–170 | 146 | 빌드·옵션 보고서의 §5와 마지막 전수 검증 기록을 대조했다. 현재 코드와 과거 커밋의 옵션·분기·계산식을 열었다. |
| 171 | 1 | 비선형 호출 흐름 보고서의 RF1-018과 RF1-002를 대조했다. 실제 step2d 헤더 포함문을 확인했다. |
| 172–177 | 6 | 4D-Var 보고서의 최종 결론과 과거 동화 옵션의 원문을 대조했다. OBS_IMPACT의 결합 조건을 확인했다. |
| 178 | 1 | Representer 보고서와 RBL4DVAR 드라이버 주석을 대조했다. |
| 179 | 1 | 입력 보고서와 makefile·read_phypar의 MyAppCPP 처리를 대조했다. |
| 180–192 | 13 | 혼합·경계·강제력 보고서와 현재·과거 코드 및 위키를 대조했다. |
| 193–196 | 4 | 출력·메타데이터 보고서와 진단·표면 응력·이력 출력 조건을 대조했다. |
| 197–202 | 6 | 퇴적물·해빙 보고서와 옵션 조건·층 계산·해빙 계산식을 대조했다. |
| 203–219 | 17 | 이론·수치 보고서와 위키 끌어오기·혼합 방향·이류 선택 원문을 대조했다. |
| 220–221 | 2 | 도구·안내 보고서와 경계 자료 선택 및 LBC 입력 원문을 대조했다. |

차이 표의 197행은 [note-job-8.tsv](../assign/note-job-8.tsv)의 해당 노트 배정과 일치한다. 누락과 중복은 없다. [반영 기록](ROMS-notes-apply-8.md)의 197행과도 일치한다.

A 분류 126행의 커밋 근거를 git 판정표 A4–A8과 대조했다. 노트에 적힌 서로 다른 커밋·날짜 쌍 23개를 `git show`의 저자 날짜와 대조했다. 날짜 불일치는 없다. 보고서가 보정한 Chapman 필드와 전처리 조건은 최종 보고서의 문장을 유지했다. 보고서가 git 판정표의 A를 B 또는 D로 바꾼 행도 최종 보고서 분류를 유지했다.

대상 노트에는 E 분류 행이 없다. RF1-018이 언급하는 RF1-002는 최종 보고서의 E 코드 결함 후보 판정에 해당한다. 이를 확정된 계산 오류로 바꾸지 않았다.

### 정정 목록

아래의 부모 노트는 [roms-wiki-cppdefs-options.md](../../../models/ROMS/manual-notes/roms-wiki-cppdefs-options.md)이다. 수정 전 부모 노트의 문장은 현재 부모 노트의 해당 줄과 다르다. 해당 인용을 보존한 보고서 §4의 위치로 출처를 바꿨다. 인용 앞에 `보고서 §4에 보존된 수정 전 노트`를 표시했다.

| 노트:줄 | 수정 전 | 수정 후 | 근거 원문 |
|---|---|---|---|
| roms-wiki-cppdefs-options-differences-4.md:164 | `Master/ocean_control.F:115`와 `:116`을 현재 코드로 인용했다. | 두 경로에 `68c7aa40^:`를 붙였다. | [빌드·옵션 보고서](../compare/roms-build-options-history-vs-code.md):3546·5798. `git show 68c7aa40^:Master/ocean_control.F`의 115행은 `#elif defined AFT_EIGENMODES`이다. 116행은 `# include "afte_ocean.h"`이다. |
| roms-wiki-cppdefs-options-differences-4.md:165 | 부모 노트 24행을 현재 원문으로 인용했다. | 보존된 수정 전 인용의 출처를 빌드·옵션 보고서 3590행으로 바꿨다. | [빌드·옵션 보고서](../compare/roms-build-options-history-vs-code.md):3590에는 `It is included at the top of every ROMS source file.`이 있다. 현재 부모 노트 24행은 빈 줄이다. |
| roms-wiki-cppdefs-options-differences-4.md:166 | 부모 노트 68행의 수직 혼합 목록을 인용했다. | 출처를 빌드·옵션 보고서 3593행으로 바꿨다. | [빌드·옵션 보고서](../compare/roms-build-options-history-vs-code.md):3593은 수정 전의 `(parent — 16-18 중 선택)`을 보존한다. 현재 부모 노트 68행은 표 구분선이다. |
| roms-wiki-cppdefs-options-differences-4.md:167 | 부모 노트 117행의 `rotated isobath`를 인용했다. | 출처를 빌드·옵션 보고서 3596행으로 바꿨다. | [빌드·옵션 보고서](../compare/roms-build-options-history-vs-code.md):3596은 `TS_DIF2 + MIX_GEO_TS`와 `rotated isobath`를 보존한다. 현재 부모 노트 117행은 EcoSim 목록이다. |
| roms-wiki-cppdefs-options-differences-4.md:168 | 부모 노트 146행의 `// #define SOLVE_SEDIMENT`를 인용했다. | 출처를 빌드·옵션 보고서 3598행으로 바꿨다. | [빌드·옵션 보고서](../compare/roms-build-options-history-vs-code.md):3598은 해당 예제 줄을 보존한다. 현재 부모 노트 146행은 COARE 3.5 설명이다. |
| roms-wiki-cppdefs-options-differences-4.md:169 | 부모 노트 154행의 `advection scheme`과 `binary fixed` 설명을 인용했다. | 출처를 빌드·옵션 보고서 3599행으로 바꿨다. | [빌드·옵션 보고서](../compare/roms-build-options-history-vs-code.md):3599은 수정 전 컴파일 시 선택 표를 보존한다. 현재 부모 노트 154행은 빈 줄이다. |
| roms-wiki-cppdefs-options-differences-4.md:190 | 부모 노트 113–115행의 KPP `default` 표기를 인용했다. | 출처를 혼합·경계·강제력 보고서 1616행으로 바꿨다. | [혼합·경계·강제력 보고서](../compare/roms-mixing-bc-forcing-vs-code.md):1616은 `Vertical mixing (default)`를 포함한 수정 전 표를 보존한다. 현재 부모 노트 113–115행은 생태계 모델 표이다. |
| roms-wiki-cppdefs-options-differences-4.md:191 | 부모 노트 117행의 `rotated isobath`를 인용했다. | 출처를 혼합·경계·강제력 보고서 1617행으로 바꿨다. | [혼합·경계·강제력 보고서](../compare/roms-mixing-bc-forcing-vs-code.md):1617은 수정 전 표를 보존한다. 현재 부모 노트 117행은 EcoSim 목록이다. |
| roms-wiki-cppdefs-options-differences-4.md:198 | 부모 노트 146행의 `// #define SOLVE_SEDIMENT`를 인용했다. | 출처를 퇴적물·해빙 보고서 1374행으로 바꿨다. | [퇴적물·해빙 보고서](../compare/roms-sediment-ice-vegetation-vs-code.md):1374은 해당 예제 줄과 `SEDIMENT`로 바꾸라는 수정안을 보존한다. 현재 부모 노트 146행은 COARE 3.5 설명이다. |
| roms-wiki-cppdefs-options-differences-4.md:199 | 부모 노트 154·155행의 컴파일 시 선택과 실행 시 입력 설명을 인용했다. | 두 인용의 출처를 퇴적물·해빙 보고서 1380행으로 바꿨다. | [퇴적물·해빙 보고서](../compare/roms-sediment-ice-vegetation-vs-code.md):1380은 수정 전 표의 두 줄을 보존한다. 현재 부모 노트 154행은 빈 줄이다. 155행은 적용 예시 절 제목이다. |
| roms-wiki-cppdefs-options-differences-4.md:203 | `UV_COR.wiki의 끌어오기 대상은 Options의 UV_COR 절이다.` | `UV_COR.wiki는 Options의 UV_ADV 절을 끌어온다. 끌어오기 대상을 Options의 UV_COR 절로 고친다.` 원 쪽 인용도 보탰다. | [UV_COR 원문](../../../models/ROMS/raw/manuals/wiki/wikitext/UV_COR.wiki):1은 `{{#lst:Options\|UV_ADV}}`이다. [이론·수치 보고서](../compare/roms-theory-numerics-vs-code.md):425·865도 실제 대상이 UV_ADV임을 적는다. B 분류와 UV_COR 절로 고치라는 결론은 유지했다. |
| roms-wiki-cppdefs-options-differences-4.md:217 | 부모 노트 117행의 `rotated isobath`를 인용했다. | 출처를 이론·수치 보고서 726행으로 바꿨다. | [이론·수치 보고서](../compare/roms-theory-numerics-vs-code.md):726은 수정 전 표와 geopotential 방향으로 바꾸라는 수정안을 보존한다. 현재 부모 노트 117행은 EcoSim 목록이다. |
| roms-wiki-cppdefs-options-differences-4.md:218 | 부모 노트 128행의 `// 한국 동해 minimal forecast`를 인용했다. | 출처를 이론·수치 보고서 727행으로 바꿨다. | [이론·수치 보고서](../compare/roms-theory-numerics-vs-code.md):727은 운동량 혼합 방향이 빠진 수정 전 예제를 보존한다. 현재 부모 노트 128행은 LMD_MIXING 설명이다. |
| roms-wiki-cppdefs-options-differences-4.md:219 | 부모 노트 154행의 `advection scheme`과 `binary fixed` 설명을 인용했다. | 출처를 이론·수치 보고서 728행으로 바꿨다. | [이론·수치 보고서](../compare/roms-theory-numerics-vs-code.md):728은 수정 전 컴파일 시 선택 표를 보존한다. 현재 부모 노트 154행은 빈 줄이다. |

### 보완 목록

| 노트:줄 | 보완 전 | 보완 후 | 근거 원문 |
|---|---|---|---|
| roms-wiki-cppdefs-options-differences-4.md:171 | Legacy 헤더를 고정으로 포함한다는 결론에 실제 포함문 인용이 없었다. | `ROMS/Nonlinear/step2d.F:20`의 포함문을 추가했다. | [step2d.F](../../../models/ROMS/raw/source_code/roms/ROMS/Nonlinear/step2d.F):20은 `# include "step2d_LF_AM3.h"`이다. [비선형 호출 흐름 보고서](ROMS-callflow-nonlinear.md):2189의 RF1-002와 2205의 RF1-018이 같은 근거를 연결한다. |
| roms-wiki-cppdefs-options-differences-4.md:201 | ICE_SHOREFAST의 열 플럭스 인용은 있었지만 항력과 염분 플럭스의 직접 인용은 없었다. | `ROMS/Nonlinear/SeaIce/ice_vbc.F:269–274`와 `ROMS/Nonlinear/SeaIce/ice_mk.h:772–778`을 추가했다. | [ice_vbc.F](../../../models/ROMS/raw/source_code/roms/ROMS/Nonlinear/SeaIce/ice_vbc.F):273–274는 얕은 물에서 `chuiw`를 조정한다. [ice_mk.h](../../../models/ROMS/raw/source_code/roms/ROMS/Nonlinear/SeaIce/ice_mk.h):772–778은 ICE_SHOREFAST 아래에서 `stflx(i,j,isalt)`를 갱신한다. [퇴적물·해빙 보고서](../compare/roms-sediment-ice-vegetation-vs-code.md):1643의 결론을 유지했다. |

### 기계 확인 후보 판정

- 사용자 제공 기계 확인 불일치 후보: 없음. 이번에 찾은 인용 위치 오류와 문장 정정은 위 정정 목록에 별도로 기록했다.

### 최종 확인

- 노트의 파일·판·줄 번호 표기 2,089회를 해당 원문에서 조회했다. 중복을 제거한 위치는 1,480개이다. 이 수는 수정 후 노트의 경로·줄 번호 표기를 추출하여 셌다.
- 경로 뒤의 백틱 인용 2,080회를 다시 대조했다. 불일치는 없다. 위키 표시 글자와 HTML 문자 참조는 원문에 맞게 해석했다.
- 바로 뒤에 인용이 없는 경로·줄 번호 표기 9회도 원문을 열었다. 이 수는 표의 항목명에 있는 8회와 계산식 사이의 빈 줄 인용 1회를 합한 값이다.
- 수정 후 차이 표 197행의 분류는 모두 최종 보고서와 같다. RTN-230의 문장은 실제 끌어오기와 수정 지시를 구분했다. 그 밖의 결론 문장은 검증 태그와 커밋 근거 문장을 제외하면 보고서와 같다.
- Frontmatter를 YAML로 읽었다. 표를 Markdown에서 HTML로 렌더했다. 표 머리말과 본문 197행은 모두 여섯 열이다.
- Markdown 상대 링크 199회가 가리키는 서로 다른 파일 12개는 모두 존재한다. Frontmatter의 related 경로도 존재한다. 링크 수는 수정 후 대상 노트에서 셌다.
- 대상 노트에는 Mermaid 블록이 없다. 따라서 대조할 Mermaid 상자와 흐름도는 없다.
- 대상 노트에는 사용자 홈 절대 경로와 이중 여는 대괄호가 없다. 사용자 지정 한계 문장도 없다.
- 미해결 항목: 없음. 대상 노트의 전체 줄 대조를 완료했다.
