# ROMS 노트 전수 검증 3

- 대상 노트: `models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-1.md`.
- 검증 대상: 새 파일의 전체 225줄. 줄 수는 수정 전 파일의 `wc -l` 결과다.
- 검증 기준: 사용자가 지정한 원문과 보고서의 최종 검증 기록.
- 기계 확인 불일치 후보: 없음.

## 진행 기록

- 검증 기록 파일을 먼저 생성했다. 대상 노트의 대조 결과는 완료 후 덧붙인다.

## 완료: roms-wiki-cppdefs-options-differences-1.md

| 대상 노트 | 대조한 줄 수 | 정정한 줄 수 | 보완한 줄 수 | 결과 |
|---|---:|---:|---:|---|
| [roms-wiki-cppdefs-options-differences-1.md](../../../models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-1.md) | 225 | 3 | 0 | 전체 대조 완료 |

줄 수는 수정 전후 대상 노트의 전체 물리 줄을 센 값이다. 정정 수는 정정 표지가 붙은 고유 줄을 센 값이다. 한 표 행에 있는 인용 위치 9곳의 정정은 1줄로 셌다. 수정 전후 비교에서 바뀐 줄은 2·6·32줄이다.

### 대조 범위

| 노트 줄 | 대조 내용 | 판정 |
|---|---|---|
| 1–14 | frontmatter의 제목·검증 방법·날짜·작성자·부모 노트 연결 | 제목과 검증 방법을 정정했다. |
| 15–26 | 부모 노트 링크·보고서 링크·최종 검증 기록·문서 판·코드 판·표 형식 | 원문과 일치한다. |
| 27–32 | biology의 RB-006·RB-012·RB-014·RB-016·RB-017·NT-016 | 결론은 최종 보고서와 일치한다. NT-016의 부모 노트 인용 위치를 정정했다. |
| 33–53 | A4DVAR_TOY·드라이버·결합·ANA_BMFLUX | 원문과 최종 보고서에 일치한다. |
| 54–81 | 해석적 입력의 필수 조건·충돌·관련 옵션 | 원문과 최종 보고서에 일치한다. |
| 82–115 | 과거 ASSIMILATION 계열의 정의·입력·갱신·삭제 이력 | 원문과 최종 보고서에 일치한다. |
| 116–154 | ATM_PRESS·AVERAGES 계열의 조건·변수·파일명·삭제 이력 | 원문과 최종 보고서에 일치한다. |
| 155–175 | BACKGROUND부터 DIURNAL_SRFLUX까지의 옵션 조건과 이력 | 원문과 최종 보고서에 일치한다. |
| 176–225 | 동쪽 자유수면·난류·2차원 운동량 경계의 과거 CPP와 현재 LBC | 원문과 최종 보고서에 일치한다. |

차이 표의 199행을 [배정표](../assign/note-job-5.tsv) 및 [노트 반영 기록](ROMS-notes-apply-5.md)과 대조했다. 행 ID의 누락·추가·중복은 없다. 분류는 A 152행, B 39행, C 4행, D 1행, F 3행이다. 이 수량은 대상 노트의 차이 표에서 셌다.

199행의 분류와 결론 문장은 [biology 보고서 §5](../compare/roms-biology-vs-code.md#5-차이-결론) 및 [build-options-history 보고서 §5](../compare/roms-build-options-history-vs-code.md#5-차이-결론)의 최종 내용과 일치한다. 보고서의 검증 표지와 인라인 코드 표시만 정규화해 문장을 대조했다. 노트에 덧붙인 git 커밋 문장은 별도로 대조했다.

RB-006과 RB-017은 biology 보고서의 최종 검증 기록 2055줄을 따랐다. 해당 기록은 TALK_PROGNOSTIC의 계산 분기 삭제라는 이전 git 판정을 옵션 이름 변경으로 고쳤다. NT-016은 같은 보고서의 최종 검증 기록 2211줄을 따랐다.

### 정정 목록

1. `models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-1.md:2`.

   전: `title: "ROMS cppdefs.h — 32+ CPP option category 종합 (myroms.org/wiki/cppdefs.h) — 문서와 코드 차이 (10-14 대조)"`

   후: `title: "ROMS cppdefs.h — 대표 CPP 범주 (myroms.org/wiki/cppdefs.h) — 문서와 코드 차이 (10-14 대조)" # [10-14 전수 검증 정정]`

   근거: `roms-build-options-history-vs-code.md:3592`의 RBH-3479 수정안은 “대표 CPP 범주라는 편집 제목으로 표시한다.”이다. 부모 노트 2줄도 “대표 CPP 범주”를 사용한다.

2. `models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-1.md:6`.

   전: `verification_method: "models/ROMS/raw/manuals/wiki/markdown/cppdefs.h.md (myroms.org/wiki/cppdefs.h, _revid=5862_, fetched 2026-05-03) 본문 직접 인용 — Contents 의 32 numbered section 직접 추출 (momentum·tracers·pressure gradient·atmospheric BL·shortwave·Lagrangian·horizontal/vertical mixing·GLS·MY25·KPP·Richardson·3 BBL closures·lateral BC·tidal forcing·driver·TL/RPR/ADJ·6 biology models). 2026-10-14 ROMS recovery 대조 보고서 반영"`

   후: `verification_method: "이 노트의 전체 줄을 원문과 보고서에 대조했다. 인용 원문은 ROMS 위키 wikitext, 부모 노트, 현재 코드 57aecf58 및 인용한 과거 판이다. 결론은 biology·build-options-history 보고서의 최종 검증 기록과 git 판정 보고서에 대조했다." # [10-14 전수 검증 정정]`

   근거: 대상 노트 27–225줄은 문서와 코드의 차이 표이다. 원문 인용은 위키 wikitext·부모 노트·현재 코드·과거 판에 걸쳐 있다. 기존 검증 방법은 부모 노트의 Contents 발췌 설명이었다. 이번에 수행한 원문·최종 보고서 대조로 검증 방법을 고쳤다. 결론 대조 근거는 `roms-biology-vs-code.md:1556–1563,2024`와 `roms-build-options-history-vs-code.md`의 같은 행 ID를 가진 §5 표이다.

3. `models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-1.md:32`의 `biology:NT-016`.

   인용 대상은 `models/ROMS/manual-notes/roms-wiki-cppdefs-options.md`이다. 인용문은 유지했다. 아래 표의 줄 번호를 현재 원문 위치로 고쳤다. 결론 문장 칸 끝에 `[10-14 전수 검증 정정]`을 붙였다.

| 이전 인용 줄 | 정정한 인용 줄 | 정정 위치의 원문 |
|---:|---:|---|
| 96 | 110 | `### 2.7 Biology (27-32)` |
| 98 | 112 | `\| § \| Biology 모델 \| 출처 \|` |
| 99 | 113 | `\|---\|---\|---\|` |
| 100 | 114 | `\| 27 \| **Fennel et al. 2006** \| Fennel et al. (2006) "Nitrogen cycling..." \|` |
| 101 | 115 | `\| 28 \| Hypoxia ecosystem model \| \|` |
| 102 | 116 | `\| 29 \| **NPZD** (Nitrogen-Phytoplankton-Zooplankton-Detritus) \| 단순 4-box \|` |
| 103 | 117 | `\| 30 \| EcoSim bio-optical \| \|` |
| 104 | 118 | `\| 31 \| Nemuro lower trophic level \| \|` |
| 105 | 119 | `\| 32 \| Red tide biological \| \|` |

   근거: 부모 노트 110–119줄에 해당 제목과 생물 모델 표가 있다. `roms-biology-vs-code.md:2024`의 NT-016은 같은 생물 모델 묶음을 roms-4.2와 대조한다. 분류와 결론 문장은 유지했다.

### 수정 후 확인

- 대상 노트의 경로·줄 인용 3,166개를 원문에서 열었다. 중복을 제외한 인용 위치는 1,636곳이다. 판본을 구분해 센 인용 파일은 182개이다. 이 수량은 노트에서 추출한 경로·줄 인용을 집계했다.
- 현재 파일은 직접 읽었다. 과거 파일은 `git show REV:path`로 읽었다. 조건식·수식·부정·수량·단위·부호를 해당 원문 및 보고서의 결론과 대조했다.
- 수정 전 불일치는 NT-016의 부모 노트 인용 위치 9곳이었다. 수정 후 인용문과 지정 줄의 불일치는 없다. 인용문 없이 경로·줄만 적은 항목은 없다.
- A 152행에 적힌 커밋 해시와 날짜를 [A1](../compare/ROMS-git-verify-A1.md)·[A2](../compare/ROMS-git-verify-A2.md)·[A6](../compare/ROMS-git-verify-A6.md)·[D1](../compare/ROMS-git-verify-D1.md) 및 최종 대조 보고서와 확인했다. 서로 다른 커밋은 21개이다. 이 수량은 A 행의 결론 문장에 적힌 해시를 중복 없이 센 값이다. 21개 커밋의 저자 날짜도 읽기 전용 `git show -s`로 확인했다.
- 코드 판 `57aecf58`의 저자 날짜는 2026-09-18이다. 현재 `ROMS/Modules/mod_ncparam.F:653`의 원문은 `      character (len=5  )    :: version = '4.3  '`이다. 위키 manifest의 수집 날짜는 2026-05-03이다.
- 표의 199행은 모두 6열이다. YAML 파서가 frontmatter를 정상적으로 읽었다. 정정 표지는 frontmatter의 YAML 주석과 NT-016의 결론 문장 칸 끝에 있다.
- 노트 위치를 기준으로 상대 링크 39개를 확인했다. 연결 대상 파일은 모두 존재한다. 이 수량은 노트의 Markdown 링크 출현 수이다. 보고서 절 링크는 해당 제목과 연결된다.
- 대상 노트에는 E 행과 mermaid 블록이 없다. 외부 원문 보고서 끝의 “Claude 확인과 보완”에 이 노트의 행 ID는 없다.
- 대상 노트에는 사용자 홈 절대 경로와 이중 대괄호 위키 링크 구문이 없다. 사용자가 금지한 한계 문장도 없다.
- 수정한 3줄을 제외한 222줄은 수정 전 원문과 같다. 이 수량은 수정 전후 줄별 비교 결과이다.

### 기계 확인 후보 판정

- 사용자 제공 기계 확인 불일치 후보: 없음. 별도로 발견한 NT-016의 인용 위치 9곳은 위 정정 목록에 모두 기록했다.

대상 노트 전체 225줄의 대조를 완료했다. 미해결 항목은 없다.
