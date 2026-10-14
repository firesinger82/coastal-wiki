# ROMS 노트 전수 대조 기록 — 6

- 대상 노트: `models/ROMS/source-analysis/roms_analytical_functionals-differences-2.md`.
- 대상 범위: 새 파일의 전체 163줄이다. 이 수는 작업 시작 시 `splitlines()`로 센 값이다. frontmatter 1–19행과 빈 줄을 포함한다.
- 대조 기준: 현재 원문 코드와 위키 원문을 사용한다. 보고서 결론은 끝의 `전수 검증 기록 (10-14)`을 반영한 최종본을 사용한다.
- 작업 시작일: 2026-10-14.

## roms_analytical_functionals-differences-2.md 대조 결과

대상은 [해석 함수 차이 노트](../../../models/ROMS/source-analysis/roms_analytical_functionals-differences-2.md)다.
작업 시작 시 전체 163줄을 대조했다.
정정 후 전체 164줄도 확인했다.
추가한 1줄은 frontmatter의 `has_source_needed`다.

| 집계 항목 | 결과 | 집계 기준 |
|---|---:|---|
| 대조한 대상 줄 | 163 | 작업 시작 파일의 1–163행이다. 빈 줄과 frontmatter를 포함한다. |
| 정정 | 5행 | 최종 노트의 `[10-14 전수 검증 정정]` 태그를 센 값이다. 최종 7·161·162·163·164행이다. |
| 보완 | 5행 | 최종 노트의 `[10-14 전수 검증 보완]` 태그를 센 값이다. 최종 26·161·162·163·164행이다. |
| 정정·보완 중복 | 4행 | 최종 161–164행에 두 태그가 함께 있다. |
| 변경한 고유 줄 | 6행 | 수정한 기존 5줄과 추가한 frontmatter 1줄이다. |
| 차이 표 결론 | 133행 일치 | [배정표](../assign/note-job-17.tsv)의 대상 ID 133개를 [최종 보고서 §5](../compare/roms-testcases-vs-code.md#5-차이-결론)와 대조했다. |

표의 최종 분류는 B 6행과 C 127행이다.
이 수는 대상 노트의 결론 분류 칸에서 셌다.
분류와 결론 문장의 내용은 바꾸지 않았다.
보고서 끝의 `전수 검증 기록 (10-14)` 중 작업 3/3을 적용했다.
RT1-1388의 표본 조정도 반영되어 있다.

### 정정·보완 목록

아래 위치는 `models/ROMS/source-analysis/roms_analytical_functionals-differences-2.md`의 최종 줄 번호다.
기존 25·160·161·162·163행은 frontmatter 추가 뒤 26·161·162·163·164행이 되었다.
표에는 바뀐 부분만 적었다.

| 노트:줄 | 종류 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| `roms_analytical_functionals-differences-2.md:7` | 정정 | `has_source_needed` 필드가 없었다. | `has_source_needed: false`를 추가했다. | `CONVENTIONS.md` §2.0은 감사한 verified 문서에 완전 출처 상태도 false로 명시하도록 정한다. 이번 대조에서 전체 대상 줄의 출처를 확인했다. |
| `roms_analytical_functionals-differences-2.md:26` | 보완 | 코드 판 문장에 버전 선언과 개발 브랜치 설명의 원문 인용이 없었다. | 보고서 §1 링크와 `ROMS/Modules/mod_ncparam.F:653`, `docs/README.md:40`의 원문을 덧붙였다. | `roms-testcases-vs-code.md:5–9`는 HEAD와 날짜를 명시한다. `ROMS/Modules/mod_ncparam.F:653`은 `character (len=5  )    :: version = '4.3  '`이다. `docs/README.md:40`은 develop을 개발 브랜치로 설명한다. 읽기 전용 `git diff roms-4.2 HEAD -- ROMS/Modules/mod_ncparam.F`도 버전 선언의 4.2에서 4.3으로의 변경을 보여 준다. |
| `roms_analytical_functionals-differences-2.md:161` | 정정·보완 | 수정 전 인용의 `ana_initial.h:72`, `ana_grid.h:94`, `ana_tobc.h:48`, `ana_perturb.h:56`, `ana_btflux.h:39-43` 앞에 원문에 없는 `ROMS/Functionals/`가 붙어 있었다. 인용 판의 설명이 없었다. | 해당 접두어 5곳을 삭제했다. `수정 전 노트 인용: 보고서 §4 RT1-1515` 링크를 붙였다. | `roms-testcases-vs-code.md:2612`의 수정 전 노트 인용과 부모 노트 HEAD 58행은 모두 짧은 파일명을 사용한다. 읽기 전용 diff의 삭제 줄도 같은 원문이다. 현재 등록 조건은 `ROMS/Functionals/ana_btflux.h:39–44`와 같다. |
| `roms_analytical_functionals-differences-2.md:162` | 정정·보완 | 수정 전 인용의 `ana_smflux.h:142-147` 앞에 `ROMS/Functionals/`가 붙어 있었다. 바깥 백틱은 2개로 열고 3개로 닫혀 있었다. 인용 판의 설명이 없었다. | 접두어를 삭제했다. 바깥 백틱 2개와 안쪽 백틱을 공백으로 분리했다. `수정 전 노트 인용: 보고서 §4 RT1-1517` 링크를 붙였다. | `roms-testcases-vs-code.md:2614`와 부모 노트 HEAD 99행의 문장은 짧은 파일명을 사용한다. 수정 후 HTML의 코드 인용은 HEAD 99행 전체와 같다. BASIN과 UPWELLING의 현재 분기는 `ROMS/Functionals/ana_smflux.h:141–147,306–324`에서 확인했다. |
| `roms_analytical_functionals-differences-2.md:163` | 정정·보완 | 수정 전 인용의 `ana_psource.h:175-183` 앞에 `ROMS/Functionals/`가 붙어 있었다. 인용 판의 설명이 없었다. | 접두어를 삭제했다. `수정 전 노트 인용: 보고서 §4 RT1-1521` 링크를 붙였다. | `roms-testcases-vs-code.md:2623`과 부모 노트 HEAD 170행은 짧은 파일명을 사용한다. 마지막 XI source의 현재 대입은 `ROMS/Functionals/ana_psource.h:175–190`에 있다. |
| `roms_analytical_functionals-differences-2.md:164` | 정정·보완 | 수정 전 인용의 `ana_grid.h:237-398` 앞에 `ROMS/Functionals/`가 붙어 있었다. 두 노트 인용의 판 설명이 없었다. | 접두어를 삭제했다. 두 인용 앞에 `수정 전 노트 인용: 보고서 §4 RT1-1536` 링크를 붙였다. | `roms-testcases-vs-code.md:2648`은 부모 노트 HEAD 178행과 `roms_include_cppdefs.md` HEAD 142행을 인용한다. 두 인용을 읽기 전용 diff로 복원한 HEAD 원문과 대조했다. |

### 기계 확인 후보 판정

- `roms_analytical_functionals-differences-2.md:161`의 `ROMS/Functionals/ana_initial.h:72`·`ANANAME(2)` 후보: 현재 코드의 직접 인용으로 탐지한 오판이다. `ROMS/Functionals/ana_initial.h:72`는 `OCEAN(ng) % tl_ubar` 인자다. 실제 등록은 같은 파일 101행의 `ANANAME(10)=MyFile`이다. 후보 문구는 보고서 2612행과 수정 전 부모 노트 58행의 인용이므로 보존했다. 원문에 없던 경로 접두어를 삭제하고 수정 전 인용의 출처를 명시했다.
- `roms_analytical_functionals-differences-2.md:161`의 `ROMS/Functionals/ana_perturb.h:56`·`ANANAME(48)=__FILE__` 후보: 현재 코드의 직접 인용으로 탐지한 오판이다. `ROMS/Functionals/ana_perturb.h:55–56`은 `MyFile` 선언과 `__FILE__` 대입의 연결 줄이다. 실제 등록은 같은 파일 125행의 `ANANAME(19)=MyFile`이다. 후보 문구는 보고서 2612행과 수정 전 부모 노트 58행의 인용이므로 보존했다. 원문에 없던 경로 접두어를 삭제하고 수정 전 인용의 출처를 명시했다.

### 전체 줄 대조 범위

이 표의 줄 번호는 작업 시작 시 노트를 기준으로 한다.

| 대상 줄 | 대조 내용 |
|---|---|
| 1–19 | frontmatter 전체를 확인했다. 작성일과 대조일은 노트 반영 기록 및 현재 작업일과 같다. 관련 파일 3개는 모두 존재한다. |
| 20–30 | 빈 줄·제목·문서 판·코드 판·출처 링크·표 머리글을 확인했다. 위키 manifest의 수집일과 현재 코드 HEAD를 확인했다. |
| 31–54 | RT1-1363–1386의 초기장 분기와 헤더 선택을 대조했다. model·SOLVE3D·SALINITY·restart 조건을 확인했다. |
| 55–71 | RT1-1387–1403의 응력 식을 대조했다. BULK_FLUXES와 TL_IOMS 조건을 확인했다. 3000초 경계와 응력의 부호·단위를 확인했다. |
| 72–93 | RT1-1404–1425의 혼합 계수·마스크 식을 대조했다. ANA_VMIX·SOLVE3D 및 ANA_GRID·MASKING의 결합 조건을 확인했다. |
| 94–104 | RT1-1426–1436의 점원 대입을 대조했다. 위치 설정·MOMENTUM·TRACERS 조건과 마지막 XI source를 확인했다. |
| 105–117 | RT1-1437–1449의 기상장·회전력·마찰·climatology·scope를 대조했다. analytical.F의 include 조건과 사례 헤더의 정의·해제를 확인했다. |
| 118–146 | RT1-1450–1478의 경계·퇴적물·파랑·플럭스·진단을 대조했다. acquire·DOMAIN edge 조건을 확인했다. bed 두께의 mm와 m를 구분했다. 유량 계수와 SIN 항 부호를 확인했다. |
| 147–159 | 공통 include·기본값·restart·파일명 등록·flux·컴파일 오류용 텍스트·퇴적물 초기화·경계 ramp·선형 초기장을 대조했다. INLET_TEST의 Red와 FSOBC_REDUCED에 따른 수면 acquire 설정을 확인했다. |
| 160–163 | RT1-1515·1517·1521·1536의 수정안과 최종 결론을 대조했다. 수정 전 노트 인용 5개를 HEAD 원문과 대조했다. |

### 최종 확인

- 최종 노트의 직접 원문 인용은 3,133건이다. 코드·저장소 문서 인용 2,832건과 위키 인용 301건이다. `경로:줄` 뒤 백틱 인용을 추출하여 해당 원문 줄과 대조한 수다. 표의 수정 전 노트 인용은 이 집계에서 제외했다.
- 직접 인용은 원문 파일 89개와 고유 원문 줄 2,052개를 가리킨다. 파일 경로와 줄 번호의 중복을 제거하여 셌다. 인용문 불일치는 0건이다.
- 수정 전 노트 인용 5개는 읽기 전용 `git diff -U0 HEAD -- <부모 노트>`로 복원한 원문과 일치한다. RT1-1517의 인용도 HTML 렌더 뒤 전체 문장이 원문과 일치한다.
- 표 133행의 분류와 결론은 보고서 최종본과 일치한다. 비교에서는 경로를 풀어 쓴 표기와 이번 검증 태그만 정규화했다. 배정 ID의 누락과 중복은 없다.
- YAML을 파싱했다. Markdown을 HTML로 렌더했다. 표는 머리글 1행과 본문 133행으로 구성된다. 본문 각 행은 6칸이다.
- 상대 링크 8개는 모두 실제 파일을 가리킨다. 링크의 보고서 §1·§4·§5 제목도 존재한다. frontmatter의 관련 파일 3개도 모두 존재한다.
- 대상 노트의 절대 홈 경로와 이중 대괄호는 0건이다. 사용자 지정 한계 문장의 잔존도 0건이다.
- 대상 노트에는 A·E 판정행과 과거 코드 `HASH:path:N` 인용 및 mermaid 블록이 없다.
- 작업 시작 원문과 최종 파일을 비교했다. 정정·보완 목록의 기존 5줄과 추가 1줄 외에는 바뀐 줄이 없다.

완료 상태: 완료.
대상 노트의 전체 대상 줄을 대조했다.
미해결 항목은 0건이다.
