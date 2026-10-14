# ROMS 노트 전수 대조 7

- 대상: `models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-3.md`.
- 대상 범위: 새 파일 전체 줄. Frontmatter와 빈 줄을 포함한다.
- 판정 기준: 원문과 보고서 끝의 `전수 검증 기록 (10-14)`을 적용한 최종 결론.
- 기계 확인 불일치 후보: 사용자 제공 목록에 없음.
- 상태: 완료.

## 노트별 결과

| 노트 | 대조한 줄 수 | 정정 수 | 보완 수 | 결과 |
|---|---:|---:|---:|---|
| [roms-wiki-cppdefs-options-differences-3.md](../../../models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-3.md) | 226 | 2 | 0 | 전체 대조 완료 |

줄 수는 대상 파일의 물리 줄을 센 값이다. 수정 전후 줄 수는 모두 226줄이다. 정정 수는 이번 작업의 정정 표식을 붙인 고유 줄 수이다. 보완 수는 이번 작업의 보완 표식을 붙인 고유 줄 수이다.

## 대조 범위와 결과

| 대상 줄 | 대조 내용 | 결과 |
|---|---|---|
| 1–16 | Frontmatter 전체를 작성 규약과 [반영 기록 7](ROMS-notes-apply-7.md)에 대조했다. `related`의 저장소 상대 경로를 확인했다. | 기존 내용을 유지했다. |
| 17–27 | 제목·부모 노트·보고서 링크·판본 설명·표 머리글·빈 줄을 확인했다. 수집일은 `manifest.json`의 `fetched_at`에 대조했다. 코드 HASH와 날짜는 원본 저장소의 HEAD에 대조했다. 버전은 `ROMS/Modules/mod_ncparam.F:653`과 `roms-4.2` 커밋에 대조했다. | 기존 내용을 유지했다. |
| 28–226 | 차이 표 전체를 [대조 보고서 §5](../compare/roms-build-options-history-vs-code.md#5-차이-결론)와 마지막 전수 검증 기록의 작업 3/7에 대조했다. 각 행의 위키 원문과 현재·과거 코드 인용을 열었다. 조건·부정·수량·단위·부호·식을 대조했다. | 45줄과 78줄의 분류 설명을 정정했다. |

표의 199행은 [배정표](../assign/note-job-7.tsv)의 해당 노트 배정 ID와 순서까지 일치한다. 고유 행 ID의 누락과 중복은 없다. 이 파일을 대상으로 하는 보고서 §4의 본문 수정안은 없다.

199행의 결론 문장은 최종 보고서와 일치한다. 보고서 이력 표식과 노트에 추가한 git 판정 근거는 분리해서 대조했다. E행의 분류 칸에 덧붙인 `(중간)`은 보고서의 근거 강도와 일치한다. 두 D행의 분류 설명을 정정한 뒤 분류에도 의미 차이가 없다.

A행 116개의 HASH·날짜는 [git 판정 A3](../compare/ROMS-git-verify-A3.md)의 해당 31행과 [git 판정 A4](../compare/ROMS-git-verify-A4.md)의 해당 85행에 대조했다. A행에 기재된 고유 커밋 17개의 저자 날짜도 `git show`로 확인했다. 불일치는 없다. 수량은 대상 표의 A행과 해당 git 판정 행을 연결하여 센 값이다.

E행은 RBH-1534와 RBH-1535이다. 두 행의 조건과 근거 강도는 보고서 4374–4375줄 및 최종 검증 기록 5946줄과 일치한다. `tke_dif[24]`와 `tkenu[24]`를 현재 코드의 Fortran·헤더 파일에서 검색했다. 검색 결과에 비선형 계산 루틴의 사용 줄은 없다. `inp_par.F:652`의 제곱근 변환과 `wrt_info.F:492`의 제곱 기록도 원문과 일치한다.

대상 표의 인용은 2,667곳이다. 중복을 제외한 원문 위치는 1,699곳이다. 수량은 표 안의 `경로:줄` 참조를 센 값이다. 고유 위치 집계에서는 현재 코드 참조와 `57aecf58` 참조를 같은 판으로 처리했다. 모든 인용을 지정 원문에 대조했다. 위키 표시 문법과 Markdown 표의 파이프 이스케이프를 해석한 뒤 불일치는 없다. 보고서의 태그를 커밋 HASH로 대응시킨 뒤 각 행의 인용 위치 집합도 최종 보고서와 일치한다.

상대 Markdown 링크 3개는 노트 위치에서 실제 파일을 가리킨다. 보고서 링크의 절 제목도 존재한다. 대상 노트에 Mermaid 블록은 없다. 금지한 절대 로컬 경로와 이중 대괄호 문자열은 없다. 작업 한계를 남기는 문장도 없다.

## 정정 목록

| 노트:줄 | 행 ID | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-3.md:45` | RBH-1302 | 결론 칸의 `D 문서에만 있음`을 `D 구현 근거 없음`으로 정정했다. 결론 문장 칸 끝에 `[10-14 전수 검증 정정]`을 붙였다. | `roms-build-options-history-vs-code.md:4223`의 최종 분류는 `D 구현 근거 없음`이다. `ROMS/Include/cppdefs.h:374`에 `PSEUDOSPECTRA` 설명이 있다. `ROMS/Include/globaldefs.h:531`에 `defined PSEUDOSPECTRA` 조건이 있다. `Master/roms_kernel.F:114–196`에는 전용 드라이버 선택이 없다. 이름이 코드에도 있으므로 기존 분류 설명은 부정확하다. |
| `models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-3.md:78` | RBH-1368 | 결론 칸의 `D 문서에만 있음`을 `D 구현 근거 없음`으로 정정했다. 결론 문장 칸 끝에 `[10-14 전수 검증 정정]`을 붙였다. | `roms-build-options-history-vs-code.md:4256`의 최종 분류는 `D 구현 근거 없음`이다. 같은 보고서 5946줄은 활성 드라이버와 계산 연결 근거의 부재를 D 판정 이유로 명시한다. `ROMS/Include/cppdefs.h:384`에 `SO_TRACE` 설명이 있다. `Master/propagator.F:59`의 원문은 `!!#  include "propagator_so_trace.h"`이다. 이름이 코드에도 있으므로 기존 분류 설명은 부정확하다. |

위 표의 코드 경로는 `models/ROMS/raw/source_code/roms/`를 기준으로 한다. 보고서 경로는 `_staging/recovery/compare/`를 기준으로 한다.

## 기계 확인 후보 판정

- 없음: 사용자 제공 불일치 후보 목록이 비어 있다. 별도 후보 정정은 없다.

## 완료 확인

대상 226줄을 모두 대조했다. 정정한 두 표 행의 결론 문장 칸 끝에 지정 표식이 있다. 모든 차이 표 행은 6개 칸을 유지한다. 미해결 항목은 0개이다.
