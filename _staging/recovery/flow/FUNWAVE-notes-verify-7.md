# FUNWAVE 노트 전수 검증 7

검증일: 2026-10-18.
대상 노트: `models/FUNWAVE/source-analysis/funwave-feature-modules.md`.
대상 줄은 작업 시작 시 `git -C /home/firesinger/coastal-wiki diff -U0 HEAD -- models/FUNWAVE/source-analysis/funwave-feature-modules.md`의 추가 줄로 확정했다.
대상 줄은 5–6행과 69–257행이다.
대상 줄 수는 191줄이다.
이 수는 frontmatter 2줄과 본문·표·빈 줄 189줄을 포함한다.

## 진행 기록

- 대상 줄을 확정한 뒤 이 기록 파일을 먼저 만들었다.
- 대상 노트의 모든 대상 줄을 대조했다.
- 작업 상태: 완료.

## 기계 확인 후보 판정

- 사용자 제공 후보: 없음.

## 노트별 완료 결과

### funwave-feature-modules.md

| 항목 | 결과 | 집계 기준 |
|---|---:|---|
| 대조한 줄 수 | 191줄 | 시작 시 diff의 5–6행과 69–257행 |
| 정정 수 | 5줄 | 이번 정정 표지가 있는 195·197·199·206·238행 |
| 보완 수 | 1줄 | 이번 보완 표지가 있는 206행 |
| 수정한 고유 줄 수 | 5줄 | 정정과 보완의 중복을 제거한 물리 줄 수 |
| 미해결 항목 | 0개 | 아래 정정 목록과 자체 점검 판정 |

206행은 경로 정정과 보고서 절 링크 보완을 함께 포함한다.
정정 수와 보완 수는 이 행을 각각 센다.
작업 후에도 대상 노트의 물리 줄 번호는 같다.

| 노트 줄 | 대조한 줄 수 | 대조 근거와 결과 |
|---|---:|---|
| 5–6 | 2 | frontmatter를 반영 기록 4와 대조했다. 기존 verification_method 내용과 recovery 반영 구절을 구분했다. 열거한 모듈 파일 11개의 존재를 확인했다. YAML 구문은 유효하다. |
| 69–79 | 11 | 빈 줄·제목·표 머리·보고서 링크·A 정의·판본 설명을 확인했다. GPU 보고서 §1.1과 §5, AD1·AD2·AD3, callflow의 문서 판본 기록과 대조했다. 3.0 표지와 Intro-TN 쪽 이미지의 발행 표기를 확인했다. |
| 80 | 1 | theory-numerics의 FT1-184 최종 결론과 대조했다. METEO 입력·파봉 마스크·풍응력 원문을 확인했다. |
| 81–88 | 8 | inputs의 배정 행 8개를 최종 결론과 대조했다. 지형 보정·조석·시간 스펙트럼·기상 입력의 조건과 누락값을 원문에서 확인했다. |
| 89–194 | 106 | v21-manual의 배정 행 106개를 최종 결론과 대조했다. 각 READ 호출과 호출 조건을 확인했다. 입력 목록의 누락 범위와 DEPTH_FILE의 SUBGRID 한정 설명을 판독 기록에 대조했다. |
| 195–228 | 34 | aux-docs-build의 배정 행 34개를 최종 결론과 대조했다. 현재·과거 바람 경로와 추가 입력·전처리 조건을 확인했다. 보고서 §2.5의 빌드 파일 39개를 열어 지정 플래그의 부재를 확인했다. |
| 229–257 | 29 | gpu-vs-tvd의 배정 행 29개를 최종 결론과 대조했다. e42e17d의 해당 원문과 현재 TVD·GPU 원문을 비교했다. 새 모듈의 식·조건·입력·기본 소스 선택을 확인했다. |
| 합계 | 191 | 위 범위는 시작 시 대상 줄 전체와 일치한다. |

차이 표 178행의 분류는 A 36행, B 2행, C 140행이다.
이 수는 대상 노트 80–257행의 결론 칸에서 셌다.
E 행은 없다.
배정표 4의 178행과 노트의 고유 행 ID 178개가 일치한다.
배정표에는 머리행이 없다.
보고서의 끝 전수 검증 기록과 최종 집계를 기준으로 최종 결론을 확인했다.
각 보고서 §4와 callflow §6에는 이 노트를 직접 가리키는 수정안이 없다.

## 정정·보완 목록

아래 줄 번호는 `models/FUNWAVE/source-analysis/funwave-feature-modules.md`를 가리킨다.
현재 코드의 `FUNWAVE-TVD/`와 `FUNWAVE-GPU/`는 `models/FUNWAVE/raw/source_code/` 아래 경로이다.
과거 커밋의 원문은 `_staging/recovery/extract/FUNWAVE/external/tvd`에서 읽었다.

| 노트:줄 | 종류 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| funwave-feature-modules.md:195 | 정정 | `bfc2f8c:src/misc.F:252` | `bfc2f8c:misc.F:252` | 실제 git 객체 `bfc2f8c:misc.F`의 252행은 `IF(ETA(I,J)<HeightMax(I,J)*(1-WindCrestPercent))MASK_WIND(I,J)=0`이다. 보고서 aux-docs-build:21은 이 커밋의 실제 경로가 저장소 루트임을 밝힌다. |
| funwave-feature-modules.md:197 | 정정 | `bfc2f8c:src/io.F:308` | `bfc2f8c:io.F:308` | 실제 git 객체 `bfc2f8c:io.F`의 308행은 `CALL READ_STRING(WIND_FILE,FILE_NAME,'WIND_FILE',ierr)`이다. |
| funwave-feature-modules.md:199 | 정정 | `bfc2f8c:src/main.F:222`, `bfc2f8c:src/main.F:224`, `bfc2f8c:src/misc.F:208` | `bfc2f8c:main.F:222`, `bfc2f8c:main.F:224`, `bfc2f8c:misc.F:208` | 실제 main.F의 222행은 `# if defined (WIND)`이다. 224행은 `CALL WIND_EFFECT`이다. 실제 misc.F의 208행은 `SUBROUTINE WIND_EFFECT`이다. |
| funwave-feature-modules.md:206 | 정정 | 문서·코드 칸의 `FUNWAVE-TVD/src/Makefile:16·108` 및 `FUNWAVE-TVD/src/Makefile.onyx:16·108` 8곳과 `bfc2f8c:src/main.F:222` | `FUNWAVE-TVD/Makefile:16·108` 및 `FUNWAVE-TVD/Makefile.onyx:16·108`와 `bfc2f8c:main.F:222` | 현재 두 Makefile은 TVD 루트에 있다. 두 파일의 16행은 `# FLAG_6  = -DWIND`이다. 108행은 `# # FLAG_6  = -DWIND`이다. 과거 main.F의 실제 객체 경로와 222행도 확인했다. |
| funwave-feature-modules.md:238 | 정정 | 문맥의 부분 인용인 `# if defined (VESSEL)` 뒤에 인용 밖의 `&& defined (PROPELLER)`를 연결했다. | 문맥에서도 `# if defined (VESSEL) && defined (PROPELLER)` 전체를 원문 그대로 인용했다. | `FUNWAVE-TVD/src/mod_sediment.F:67`은 두 조건을 하나의 전처리 조건문에 쓴다. 조건의 의미와 A 결론은 유지했다. |
| funwave-feature-modules.md:206 | 보완 | `나머지 빌드 위치는 2.5절의 각 파일 행에 있다.` | `2.5절`을 `대조 보고서 §2.5`라는 상대 링크로 연결했다. | [aux-docs-build §2.5](../compare/funwave-aux-docs-build-vs-code.md#25-readme와-빌드-파일)에 해당 빌드 파일별 원문 행이 있다. 대상 노트에는 2.5절이 없다. |

각 정정 행의 결론 문장 칸 끝에 `[10-18 전수 검증 정정]`을 붙였다.
206행의 같은 칸 끝에는 `[10-18 전수 검증 보완]`도 붙였다.
결론 분류·결론 문장·커밋 HASH·날짜는 변경하지 않았다.

## 자체 추출 점검의 후보 판정

사용자가 제공한 기계 확인 후보는 없다.
다음은 이번 대조에서 자체 추출한 후보의 판정이다.

| 노트 줄 | 후보 | 원문 판정 |
|---|---|---|
| 81 | `e1d6b42 2017-05-17 add storm module`을 코드 문장으로 인식했다. | 검사기 오판이다. 이 문자열은 커밋 메타데이터이다. AD1의 FI1-072와 일치한다. |
| 81 | `2fcff96 2017-06-07 add module meteo and remove module storm`을 코드 문장으로 인식했다. | 검사기 오판이다. AD1의 FI1-072가 같은 변경 이력을 인용한다. |
| 82 | 같은 `2fcff96` 설명을 코드 문장으로 인식했다. | 검사기 오판이다. AD1의 FI1-073과 일치한다. |
| 195 | `bfc2f8c:src/misc.F` 객체가 없다. | 실제 객체는 `bfc2f8c:misc.F`이다. 노트의 경로를 정정했다. |
| 197 | `bfc2f8c:src/io.F` 객체가 없다. | 실제 객체는 `bfc2f8c:io.F`이다. 노트의 경로를 정정했다. |
| 199 | `bfc2f8c:src/main.F`와 `bfc2f8c:src/misc.F` 객체가 없다. | 실제 객체는 저장소 루트에 있다. 해당 인용 3곳을 정정했다. |
| 206 | 현재 `FUNWAVE-TVD/src/Makefile`과 `src/Makefile.onyx`가 없다. | 두 파일은 TVD 루트에 있다. 해당 인용 8곳을 정정했다. |
| 206 | `bfc2f8c:src/main.F` 객체가 없다. | 실제 객체는 `bfc2f8c:main.F`이다. 노트의 경로를 정정했다. |
| 238 | 문맥 인용의 `# if defined (VESSEL)`만으로는 실제 코드 한 줄과 일치하지 않는다. | 실제 67행은 `# if defined (VESSEL) && defined (PROPELLER)`이다. 조건문 전체를 원문 인용으로 맞췄다. |
| 241 | 문맥의 CARTESIAN 조건이 인용 코드 다음 줄에 없다. | 검사기 오판이다. `mod_sediment.F:1535`의 CARTESIAN 조건과 1539행의 `# else`가 1540–1542행을 감싼다. 문맥 설명은 옳다. |
| 244 | DEEP_DRAFT_VESSEL 문맥 인용 2곳이 바로 다음 줄에 없다. | 검사기 오판이다. `mod_vessel.F:161`의 조건이 163–164행을 감싼다. 문맥 설명은 옳다. |
| 245 | PROPELLER 문맥 인용 3곳이 바로 다음 줄에 없다. | 검사기 오판이다. `mod_vessel.F:467`의 조건이 468–470행을 감싼다. 문맥 설명은 옳다. |

## 최종 확인

- 코드 원문 칸과 빌드 원문 칸의 직접 코드 인용 1,231개를 해당 줄부터의 실제 원문과 대조했다. 이 수는 경로 표기·커밋 메타데이터·별도 문맥 인용을 제외한 백틱 인용 개수이다. 정정 후 불일치는 0개이다.
- 별도 문맥 인용 7개는 전처리 분기의 앞뒤 원문에 대조했다. 238행 1개를 정정했다. 나머지 6개는 유지했다.
- 코드 인용 없이 경로와 줄 범위만 제시한 80·83–89행도 해당 원문 범위를 열어 확인했다.
- 현재·과거 원문을 읽는 직접 인용 검사는 판본과 경로의 조합 48개를 사용했다. 추가 문맥은 초기화·소스·빌드·sponge 원문에서 확인했다.
- 3.0·2.1·Intro-TN·code_analysis의 쪽별 판독 기록과 tex 기록에서 입력 누락 범위를 대조했다. 추가 입력 키는 3.0 tex 원문에도 재검색했다.
- 300 dpi 쪽 이미지로 3.0 p.1·31·36·37, 2.1 p.37, Intro-TN p.9·11의 인용과 판본 표기를 확인했다. 노트의 계산식·수량·부호·단위는 해당 코드 원문에 대조했다.
- A 36행의 커밋 HASH·날짜 집합은 최종 보고서의 같은 행과 일치한다. 해당 행이 있는 AD1·AD2·AD3 판정도 확인했다.
- 차이 표 178행의 분류와 결론은 최종 보고서와 일치한다. 링크·백틱 표기와 이번 검증 표지는 문장 내용 비교에서 분리했다.
- 노트 전체의 상대 링크 14개는 모두 실제 파일을 가리킨다. 절 주소도 해당 제목과 일치한다. 이 중 대상 추가 줄의 링크는 11개이다.
- 대상 노트의 절대 경로와 `[[`는 각각 0개이다.
- 대상 노트의 `실행하지 않았다`, `확인하지 않았다`, `미검수`, `후속 대상`은 각각 0개이다.
- 대상 노트의 mermaid 블록은 0개이다.
- 차이 표의 모든 행은 6개 칸을 유지한다.
- 대상 노트의 `git diff --check HEAD -- <노트>`를 통과했다.
- 이번 작업의 쓰기 대상은 대상 노트와 이 기록 파일이다. 사용한 git 명령은 읽기 전용 diff와 과거 객체 show이다.
- 대상 191줄의 대조를 모두 마쳤다. 미해결 항목은 없다.
