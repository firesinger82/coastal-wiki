# FUNWAVE 노트 전수 검증 3

작업일: 2026-10-18.
대상 노트: `models/FUNWAVE/source-analysis/funwave-source-map.md`.
상태: 완료.

## 대상 확정

- 작업 시작 시 읽기 전용 `git diff -U0 HEAD -- models/FUNWAVE/source-analysis/funwave-source-map.md`의 추가 줄은 319줄이다.
- 시작 시 노트 줄 번호 기준 대상은 5–6, 14–15, 25–31, 33, 39, 44, 60–360, 364–367이다.
- 대상에는 frontmatter, 빈 줄, 표 구분선, Mermaid 코드 블록의 모든 줄을 포함한다.
- 검증 기준은 사용자 지정 원문과 보고서의 최종 검증 기록이다.
- 쓰기 대상은 이 기록과 대상 노트다.

## 노트별 결과

| 대상 노트 | 대조한 줄 수 | 정정 수 | 보완 수 | 미해결 수 |
|---|---:|---:|---:|---:|
| [funwave-source-map.md](../../../models/FUNWAVE/source-analysis/funwave-source-map.md) | 319 | 4 | 1 | 0 |

대조 수는 시작 시 diff의 추가 줄을 기준으로 센다.
정정 수와 보완 수는 이번 작업에서 해당 태그를 붙인 노트의 물리적 줄 수다.
정정한 줄은 28, 88, 93, 367이다.
보완한 줄은 268이다.
정정·보완 집계에는 중복 줄이 없다.
작업 전후 노트의 전체 길이는 모두 367줄이다.
작업 후 diff의 대상 줄 수와 줄 번호 범위도 시작 시 집계와 같다.

### 대상 줄의 대조 기록

| 노트 줄 | 줄 수 | 대조 내용과 근거 | 결과 |
|---|---:|---|---|
| 5–6 | 2 | frontmatter의 날짜와 반영 범위를 `FUNWAVE-notes-apply-8.md`와 대조했다. 파일 수를 현재 TVD `src/*.F` 목록과 FN1-902·FV1-574·RF-044에 대조했다. | 파일 수 38개가 일치한다. |
| 14–15, 25–31, 33, 39, 44 | 12 | TVD `main.F`, `io.F`, `mod_input.F`, `etauv_solver.F`, `fluxes.F`, `mixing.F`, `mixing_salatin.F`와 `Make_Essential:204–211`을 열었다. 각 수정안을 FN1-901·902·920, FV1-574–578, RF-043–045와 대조했다. 교체된 원문은 읽기 전용 diff의 삭제 줄로 확인했다. | 28행의 HLL 선택 조건을 정정했다. 파일 수 38개와 기본 선택 목록 34개가 일치한다. 39·44행의 파일별 줄 수도 원자료와 일치한다. |
| 60–71 | 12 | PDF 표지, 문서 파일 목록, 공개 사본의 커밋 정보와 보고서의 판본 설명을 대조했다. TVD·GPU의 로컬 `src/`와 공개 사본의 `src/`도 파일 내용으로 대조했다. | 문서·코드 판본이 일치한다. GPU에서 다른 파일은 `Makefile_cuda`, `mod_cuda.F`, `etauv_solver_gpu.F`다. |
| 72–97 | 26 | 배정표의 소스 지도 노트 26개 ID를 최종 결론 표의 같은 ID와 대조했다. 현재 코드와 과거 커밋의 원문 인용을 열었다. A 행의 커밋·날짜와 E 행의 강도를 대조했다. | 분류를 모두 유지했다. 88행의 과거 경로와 93행의 HLL 선택 조건을 정정했다. |
| 98–105, 173–175, 267–269 | 14 | 흐름도 절 제목, 원문 링크, 그림 식별자와 callflow의 끝 `렌더 확인 (10-18, Claude)` 절을 대조했다. 빈 줄도 대상에 포함했다. | 268행에 `CONSTRUCTION_GPU`의 정의문 위치를 보완했다. |
| 106–172, 176–266, 270–360 | 249 | Mermaid 블록 3개의 본문과 코드 울타리를 callflow §4와 글자 단위로 대조했다. 상자 114개의 코드 위치를 열었다. TVD·GPU의 호출 순서와 전처리·런타임 조건을 대조했다. | 블록 본문은 각각 65·89·89줄이다. 세 블록은 보고서와 모두 일치한다. `c16`의 1136행은 같은 서브루틴 내부 줄이며 정의문은 1135행이다. |
| 364–367 | 4 | 상대 링크의 대상 파일을 확인했다. GPU 기본 경로를 `mod_cuda.F:17`, `etauv_solver_gpu.F:127–177,183–316,565–595,897–953`과 FG1-802 참조 수정안에 대조했다. XBeach 링크의 모델 분류는 연결 노트와 그 인용 원문을 대조했다. | 367행의 모델 분류를 정정했다. |

위 표의 줄 수 합계는 319줄이다.

### 정정·보완 목록

아래 위치는 모두 `models/FUNWAVE/source-analysis/funwave-source-map.md`의 작업 후 줄 번호다.

| 노트:줄 | 종류 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| `funwave-source-map.md:28` | 정정 | `FLUXES`는 `WAVE_SPEED`를 거친 뒤 계면 HLL 유량을 계산한다. | `WAVE_SPEED` 호출 뒤 `IF(CONSTR(1:3)=='HLL')THEN`이면 `FLUX_AT_INTERFACE_HLL`을 호출한다. `ELSE`에서는 `FLUX_AT_INTERFACE`를 호출한다. | `FUNWAVE-TVD/src/fluxes.F:64–65,109–115`의 호출·분기 원문이다. callflow §4의 b17·b18도 같은 조건을 표시한다. |
| `funwave-source-map.md:88` | 정정 | `bfc2f8c:src/main.F:194` `CALL UPDATE_MASK` | `bfc2f8c:main.F:194` `CALL UPDATE_MASK` | 공개 TVD 사본에서 `git show bfc2f8c:main.F`의 194행을 열었다. 해당 커밋에는 `src/main.F`가 없다. AD3의 FN1-205에 적힌 `38b74cc`와 2020-02-17은 일치한다. 결론 A는 유지했다. |
| `funwave-source-map.md:93` | 정정 | FN1-920의 결론은 `FLUXES`가 HLL 유량을 계산한다고 조건 없이 적었다. | 결론에 `IF(CONSTR(1:3)=='HLL')THEN`과 `ELSE`의 서로 다른 호출을 적었다. 코드 원문 칸에 109–112행을 추가했다. | `FUNWAVE-TVD/src/fluxes.F:109`은 `IF(CONSTR(1:3)=='HLL')THEN`이다. 110행은 `CALL FLUX_AT_INTERFACE_HLL`이다. 111행은 `ELSE`다. 112행은 `CALL FLUX_AT_INTERFACE`다. callflow §4의 b17·b18도 이 분기를 표시한다. 결론 B는 유지했다. |
| `funwave-source-map.md:268` | 보완 | 그림 (c)의 소개에는 `CONSTRUCTION_GPU`의 정의문 인용이 없었다. 블록은 보고서와 같이 1136행을 가리켰다. | 그림 소개에 `FUNWAVE-GPU/src/moment_gpu.F:1135`의 정의문 위치를 보탰다. 1136행이 같은 서브루틴 내부의 `implicit none`임을 명시했다. | `FUNWAVE-GPU/src/moment_gpu.F:1135`는 `subroutine CONSTRUCTION_GPU`다. 1136행은 `implicit none`이다. callflow:2653의 c16 블록은 그대로 보존했다. |
| `funwave-source-map.md:367` | 정정 | `동일계열: xbeach_nonh (Boussinesq-type)` | `관련 비정수압 모델: xbeach_nonh의 압력 보정 설명을 참조한다.` | 연결 노트 `models/XBeach/source-analysis/xbeach_nonh.md`는 비정수압 보정을 설명한다. 인용 원문 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/nonh.F90:11–17,28–30`도 non-hydrostatic model과 동압 계산을 명시한다. 683–697행에는 `dp` 선형계 풀이와 압력·속도 보정이 있다. 기존 Boussinesq 동일계열 분류의 근거는 대상 FUNWAVE 수정안에 없다. |

FN1-920의 보고서 결론 문장은 HLL 선택 조건을 생략했다.
이 노트에는 코드 원문과 callflow의 같은 분기를 기준으로 조건을 복원했다.
다른 차이 표 행의 결론 문장은 기존 상태를 유지했다.
기존 A 행에 덧붙인 커밋·날짜는 보고서의 근거 칸과 공개 커밋 정보에 일치한다.

### 기계 확인 후보 판정

- 후보 1: `source-analysis/funwave-source-map.md:24`의 `READ_INPUT(mod_input)`은 오판이다. 노트 73행 FT1-289의 문서 원문 칸은 HEAD의 옛 24행을 인용한다. 읽기 전용 diff의 삭제 줄과 theory-numerics §4 FT1-289의 인용이 일치한다. 현재 설명은 노트 25행에서 `FUNWAVE-TVD/src/io.F:149`의 `SUBROUTINE READ_INPUT`을 따른다. 정정하지 않았다.
- 후보 2: 중복 제시된 `source-analysis/funwave-source-map.md:24`의 `READ_INPUT(mod_input)`도 오판이다. 노트 75행 FI1-319의 문서 원문 칸은 같은 옛 24행을 인용한다. inputs §4 FI1-319와 공개 원문 `7b93138:src/io.F:95`, `7b93138:src/mod_input.F:53`을 대조했다. 이 인용은 수정 전 오류를 제시하는 것이므로 유지했다.

### 최종 확인

검증 방식은 문서·소스·공개 커밋의 정적 원문 대조다.
차이 표의 26개 ID는 `FUNWAVE-note-job-8.tsv`의 소스 지도 노트 배정 목록과 일치한다.
보고서 끝의 전수 검증 기록과 최종 집계를 적용했다.

| 보고서 | 대조한 행 ID와 최종 분류 |
|---|---|
| theory-numerics §5 | FT1-245 C, FT1-289 B |
| inputs §5 | FI1-148 B, FI1-319 B, FI1-320 B |
| v21-manual §5 | FV1-197 F, FV1-199 A, FV1-458 C, FV1-574 B, FV1-575 C, FV1-576 B, FV1-577 A, FV1-578 E(중간), FV1-579 C |
| v21-examples §5 | FV2-309 C |
| aux-docs-build §5 | FN1-204 D, FN1-205 A, FN1-206 A(최초 커밋 이전 판), FN1-398 C, FN1-722 C, FN1-902 B, FN1-920 B |
| gpu-vs-tvd §5 | FG1-053 A |
| callflow §8 | RF-043 B, RF-044 B, RF-045 B |

위 표의 분류별 합계는 A 5, B 11, C 7, D 1, E 1, F 1이다.
FV1-578의 중간 강도는 E2와 v21-manual의 최종 검증 기록에 일치한다.
외부 원문 보고서의 Beta_2 배수 판정은 FV1-578의 Smagorinsky 생산 누락과 다른 원인이다.

문서 판독 기록에서는 3.0 p.1·11·25·27·32·33·40, 2.1 p.26–31·34·39, Intro-TN p.1·13·16, code_analysis p.8·9·11–15를 대조했다.
쪽 이미지는 사용자 지정 `fwpages`의 원본 PNG를 열었다.
열어 대조한 이미지는 3.0 p.1·11·25·27·32·33·40, 2.1 p.27, Intro-TN p.1·16, code_analysis p.8·13·14·15의 14쪽이다.

- 수정 후 노트의 명시적 코드 위치 바로 뒤 직접 인용 171건이 해당 원문과 일치한다. 서로 다른 인용 위치는 103곳이다. 이 수는 같은 경로·줄의 중복 인용을 구분하여 센 값이다.
- 코드 위치 바로 뒤에 인용문이 없는 본문과 흐름도도 해당 원문을 열어 대조했다. RF-045의 이어지는 삼중대각 호출·대입·전처리 줄도 대조했다.
- A 행의 커밋 HASH와 날짜는 공개 사본의 읽기 전용 커밋 조회 결과와 일치한다. FN1-206의 최초 공개 커밋 이전 판 구분은 aux-docs-build의 최종 검증 기록과 AD1의 FT1-121 근거를 따른다.
- Mermaid 블록 3개는 수정 후에도 callflow §4의 블록과 글자 단위로 일치한다. 기존 렌더 확인 표기는 callflow 끝의 렌더 확인 기록에 근거한다.
- 차이 표 26행은 모두 6열이다.
- 노트의 상대 링크 30건은 모두 실제 파일을 가리킨다. 중복을 제거한 링크 대상은 19개다. 보고서 링크의 절 앵커도 존재한다.
- 노트 전체에서 홈 디렉터리 절대 경로, 이중 대괄호, 사용자 지정 한계 문구는 각각 0건이다.
- 대상 노트는 읽기 전용 `git diff --check`를 통과했다.
- 시작 내용을 세션 메모리에 보관하여 수정 후와 비교했다. 차이가 있는 줄은 정정·보완 목록의 5줄뿐이다.

대상 319줄의 대조를 완료했다.
미해결 항목은 없다.
