# 원자료 판독 사실표 (2026-10-02, 수습 2단계)

모델 폴더(`models/<모델>/raw/`)에 준 자료 중 무엇이 실제로 읽혔는지를, **이미 있는 기록**만으로 센 표다. 새로 읽은 것은 없다.

- 판독 기록: `_staging/total-read/records/**`, `_staging/total-read/model-audit/*/*.jsonl` (07-19~09 전수 판독). 07-24 감사에서 파서 출력으로 판정된 기록(`records-structural/`)은 판독으로 세지 않았다.
- 결함 감사: `_staging/total-read/codex-defect-reports/*.json` (08-29, ADCIRC·ROMS·Delft3D·EFDC·FUNWAVE 코어 일부). 파일별 판독 기록이 아니라 결함 탐색 기록이다.
- 노트 언급: `models/<모델>/` 노트(raw 제외)에 파일명이 나오는지. 이름 일치일 뿐 분석 증거가 아니다.
- 판독 기록의 **질**은 아직 확인하지 않았다(3단계 표본 대조).

## 모델별 요약 — 코드·문서

| 모델 | 원자료 | 코드 | 코드 LLM판독 | 코드 결함감사만 | 코드 노트언급 | 문서 | 문서 판독 |
|---|--:|--:|--:|--:|--:|--:|--:|
| ADCIRC | 10,725 | 1,505 | 0 | 32 | 139 | 1,751 | 1,263 |
| CADMAS-SURF | 1,376 | 1,310 | 1,310 | 0 | 336 | 36 | 10 |
| Celeris | 995 | 279 | 164 | 0 | 138 | 363 | 226 |
| Delft3D | 19,121 | 7,436 | 0 | 33 | 775 | 598 | 62 |
| EFDC | 10,012 | 563 | 555 | 0 | 168 | 737 | 729 |
| FUNWAVE | 1,376 | 277 | 34 | 4 | 85 | 380 | 41 |
| LISFLOOD-FP | 1,672 | 874 | 440 | 0 | 109 | 116 | 20 |
| ROMS | 11,681 | 6,583 | 0 | 41 | 618 | 1,307 | 1,221 |
| SFINCS | 493 | 265 | 265 | 0 | 38 | 48 | 47 |
| SWAN | 540 | 83 | 83 | 0 | 63 | 211 | 207 |
| SWASH | 176 | 164 | 164 | 0 | 146 | 5 | 3 |
| ShorelineS | 485 | 154 | 154 | 0 | 26 | 18 | 14 |
| XBeach | 543 | 167 | 167 | 0 | 84 | 78 | 60 |

- "코드"에는 외부 라이브러리·테스트·예제가 섞여 있다(예: ROMS `WRF/` 수천 파일, Delft3D `third_party_open/`). 모델 자체 코드만의 수는 아래 "분류 후" 절.
- "문서 판독"에는 웹 문서 사본(md·txt 미러)의 grok 판독이 포함된다. ADCIRC·ROMS 문서 판독 대부분이 이것이다. PDF 매뉴얼 판독 여부는 모델 표 파일 목록에서 확인.
- ADCIRC·ROMS·Delft3D는 코드 파일별 판독 기록이 **0**이다. 08-29 Codex 결함 감사가 코어 파일 32·41·33개를 다뤘을 뿐이다.

## 분류 후: 모델 자체 코드·매뉴얼만 (2026-10-02 추가)

폴더 구조를 보고 분류했다(규칙은 각 `<모델>-files.tsv`의 `category` 열). 외부 라이브러리(ROMS `WRF/`·`roms_libs/`, Delft3D `third_party*/`, XBeach `trunk/lib/`, EFDC `GOTM_*`·`lib/` 등)·테스트·예제·부속 도구(ADCIRC `asgs`·`adcircpy`, Delft3D `Delft-FIAT`·`hydromt` 등)는 제외.

| 모델 | 자체 코드 | 파일별 판독 기록 | 결함감사만 | 기록 없음 | 매뉴얼 PDF 판독 기록 |
|---|--:|--:|--:|--:|---|
| ADCIRC | 95 | 0 | 31 | 64 | PDF 97개 중 1 |
| CADMAS-SURF | 1,301 | 1,301 | 0 | 0 | PDF 26개 중 0 |
| Celeris | 152 | 148 | 0 | 4 | PDF 3개 중 0 |
| Delft3D | 6,164 | 0 | 33 | 6,128 | PDF 53개 중 0 |
| EFDC | 510 | 502 | 0 | 8 | PDF 6개 중 0 |
| FUNWAVE | 79 | 27 | 4 | 48 | PDF 39개 중 0 |
| LISFLOOD-FP | 558 | 440 | 0 | 118 | PDF 1개 중 0 |
| ROMS | 930 | 0 | 41 | 889 | PDF 10개 중 0 |
| SFINCS | 51 | 51 | 0 | 0 | PDF 1개 중 0 |
| SWAN | 76 | 76 | 0 | 0 | PDF 9개 중 7 |
| SWASH | 160 | 160 | 0 | 0 | PDF 2개 중 0 |
| ShorelineS | 136 | 136 | 0 | 0 | PDF 6개 중 2 |
| XBeach | 83 | 83 | 0 | 0 | 별도 감사(`model-audit/XBeach`)에서 1회 판독, 수식·그림 9경로 미판독 |

- **매뉴얼 PDF는 전수 판독에서 사실상 읽히지 않았다.** total-read의 PDF 기록 250개 중 판독 완료는 SWAN 7·ShorelineS 2·ADCIRC 1뿐이고 나머지는 기계 sweep 실패다. 위 "매뉴얼·문서 LLM판독" 숫자 대부분은 웹 문서 사본(HTML·md)이다. PDF 내용은 1차 노트(`manual-notes/`)에 페이지 인용으로 일부만 들어가 있다.
- **ADCIRC·ROMS·Delft3D 자체 코드는 파일별 판독 기록이 없다.**

## 판독 기록 표본 대조 (2026-10-02)

모델별 코드 판독 기록 최대 40개를 무작위로 골라 원본과 대조했다(기록의 행 수, 상수·파라미터·식이 적힌 줄 위치에 그 이름이 실제로 있는지).

| 모델 | 행 수 일치 | 위치 일치 |
|---|---|---|
| CADMAS-SURF | 34/40 | 327/328 |
| SWASH | 40/40 | 311/320 |
| SFINCS | 34/40 | 229/230 |
| XBeach | 35/40 | 171/180 |
| EFDC | 37/39 | 400/434 |
| SWAN | 36/40 | 219/255 |
| LISFLOOD-FP | 36/40 | 154/170 |
| Celeris | 35/40 | 204/223 |
| FUNWAVE | 37/37 | 326/378 |
| ShorelineS | 26/30 | 109/141 |

- 기록이 통째로 지어낸 것은 아니다: 대부분 실제 파일·실제 줄을 가리킨다. 행 수 불일치 다수는 끝 줄 차이(±1)다.
- 그러나 "complete"를 그대로 믿을 수 없다: 예) SWAN `SwanVertlist.ftn90` 기록은 187행이라고 적었지만 파일은 418행 — 절반만 읽고 완료로 찍었다. 위치 불일치는 이름 대신 설명문을 적은 경우와 실제 오기가 섞여 있다.
- 이 대조는 위치·형식만 본 것이다. **내용을 제대로 이해했는지는 확인하지 않았다.**

## 기록이 현재 파일과 안 맞는 것 (547)

Delft3D 487(기계 sweep 실패 471 + 웹 16, 09-22 스냅샷 교체 전 경로), Celeris·ShorelineS `.git` 내부 58, SWAN 2·EFDC 1(삭제·개명). 판독 손실은 아니다.

## 파일

- `<모델>.md` — 종류별·폴더별 집계
- `<모델>-files.tsv` — 파일별 목록 (`path`, `group`, `type`, `read`, `reader`, `note_mentions_name`, `category`)

## XBeach 자체 코드 재판독 (2026-10-02 완료)

`models/XBeach/raw/source_code/trunk/src/` 자체 코드 83파일(57,447행)을 1행부터 끝까지 다시 판독했다. 파일별 기록: [read/XBeach/](read/XBeach/).

- 판독: Codex `gpt-6.1-sol`, 파일당 200행 이하로 나눠 읽음. 구 형식 32파일(배치 1~3·vegetation)은 조건문·식 원문 인용 규칙으로 재판독해 덮어씀(이전판은 커밋 `8bc2f43`).
- 기계 확인(83/83 통과): 구간이 1행~마지막 행 빈틈없음, 행 수·sha256 일치, Codex 세션 로그상 빈 줄 외 모든 행이 실제로 출력됨, 원문 인용 20,987개가 해당 행과 일치.
- 내용 검증: Claude 서브에이전트(`fable` 1회, 이후 `sonnet`)가 배치마다 표본 구간·코드 사실을 원문과 대조. 약 600항목 중 틀림·불완전 18건을 원문 확인 후 정정(기록에 `[10-02 검증 정정]` 표시).
- 반복된 오류 유형: 요약 문장이 옆의 원문 식을 다르게 풀어 씀(합↔평균, clamp↔조건), 블록 안/밖·case 병렬 관계 오기. **노트로 옮길 때는 요약 문장보다 원문 인용을 근거로 쓴다.**
- 한계: "모든 행이 판독자에게 출력됨"과 "인용이 원문과 일치"는 기계로 확인했지만, 요약 문장의 이해 정확도는 표본 검증만 했다. 파일 간 연결(예: 변수의 실제 격자 위치)은 파일별 판독으로 잡히지 않는다 — vegetation 516·520의 u점 속력 사용은 교차 파일 사실로 따로 적었다.
- 남은 것: XBeach 매뉴얼·보고서(수식·그림 미판독 9경로), 파일 간 연결 분석.

## XBeach 매뉴얼·문서 판독 (2026-10-02~03 완료)

기록: `read/XBeach/manuals/`, `read/XBeach/source_code/trunk/doc/`, `read/XBeach/office-converted/`, `read/XBeach/office-compare/word-vs-pdf.md`. 추출본: `extract/XBeach/{pdf,pdf-md,office,marker}/`.

- 텍스트 문서(readthedocs rst 13·md 2·libxbeach.tex·Office 변환 3): Codex gpt-6.1-sol 행 단위 판독, 기계 확인 통과, sonnet 표본 검증(정정 3).
- Word 판 3종: PDF와 기계 대조 — Word에만 있는 실질 내용 없음.
- PDF 4종+슬라이드+adapted_front_0(389쪽): sonnet 1차 쪽 판독 → fable 표본 검증(표본 30쪽 중 8쪽 오류, 정정 27) → **전 쪽 재판독 완료(10-03)**. 쪽 이미지(300dpi) + Marker LaTeX 초안 대조, 원문 오기는 인쇄 그대로.
  - 재판독자: fable = 비정수압 69쪽, kingsday 19–36·109–141쪽. Codex `gpt-6.1-sol` = kingsday 나머지, master 145쪽, Parallellization_report, curvilinear, adapted_front_0.
  - 결과(대시보드 집계, 10-03): 389쪽 중 재판독에서 정정 193쪽, 일치 196쪽.
  - Codex 구간마다 기계 확인(`pdfcheck.py`, 23개 작업 모두 통과)과 sonnet 3~4쪽 이미지 대조. 표본에서 나온 정정: kingsday 2, master p.14·p.40 누락 보완·p.64 용어, curvilinear p.6 도식 설명(Claude가 이미지로 확인). adapted_front_0 1쪽은 Claude가 이미지로 대조.
  - 남은 판독 불가: master p.17 식 (2.1)의 사각형 3곳·p.15 잘린 축 라벨, p.25 (2.40)·p.26 (2.43) 깨진 글리프(PDF 자체 결함).
- 도구: 본문 텍스트 = opendataloader-pdf `-f markdown --use-struct-tree` (`-f text`는 목록을 빠뜨림). 수식 = Marker 1.10 (`~/.venvs/pdfocr`, GPU). Marker는 첨자는 잘 읽지만 괄호 구조·p/ρ 혼동이 있어 판정은 이미지로.

## SFINCS 재판독 (2026-10-07 완료)

기록: `read/SFINCS/sfincs/source/`(코드), `read/SFINCS/sfincs/docs/`(문서). 대상 목록은 `SFINCS-files.tsv`의 자체코드·매뉴얼·문서 분류. `third_party_open/`(netcdf·utils·bicgstab·Delft3D 조각)·빌드 스크립트·설정·dll은 범위 밖.

- 자체 코드 51파일 40,175행: Codex `gpt-6.1-sol` 11묶음(`scripts/sfincs-batches.json`, `codex exec` 병렬). 기계 확인 전부 통과(1행~끝 구간·sha·전 행 열람·원문 인용 8,083개 일치). sonnet 표본 34구간 대조, 정정 2·표현 보완 1. directional spreading을 '분산'으로 옮긴 곳을 '방향 퍼짐'으로 통일.
- 문서 15파일 4,187행(rst·txt, 그림 27개 열람 포함): 5묶음 병렬. 기계 확인 전부 통과(원문 인용 2,339개 일치). sonnet 표본 8구간과 그림 2장 대조, 틀림 0.
- 지시문 생성: 코드 `python3 scripts/mkprompt.py N MODEL BATCHFILE`, 문서 `python3 scripts/mkdocprompt_model.py MODEL BATCHFILE N`. 용어 규칙(spreading=방향 퍼짐, dispersion=분산)과 조건문·식 원문 인용 규칙 포함.
- 문서·코드 대조(`compare/SFINCS-docs-vs-code.md`, 불일치 39)와 시간 단계 흐름 분석(`flow/SFINCS-callflow.md`)을 마치고 노트 14개에 반영했다(`667408d`). 보고서·노트 인용은 `scripts/citecheck.py`로 기계 대조, 전부 일치.
- 확인하지 않은 것: 모델 실행. 불일치·지연이 결과에 주는 영향.

## EFDC 판독 (2026-10-07~08 완료)

기록: `read/EFDC/EFDCPlus_Stable/`(EFDC+ 코드), `read/EFDC/EFDC-GVC/`(옛 판 코드), `read/EFDC/manuals/confluence/`(Confluence), `read/EFDC/manuals/pdfs/`(PDF). 대상 목록은 `EFDC-files.tsv`의 자체코드·매뉴얼·문서 분류.

- 자체 코드 510파일 307,120행: EFDC+ 207파일 131,630행(34묶음), EFDC-GVC 303파일 175,490행(46묶음). Codex `gpt-6.1-sol`, `codex exec` 5개 동시. 기계 확인 전부 통과(1행~끝 구간·sha·전 행 열람·원문 인용). sonnet 표본 약 110구간 대조, 틀림 0, 인용·표현 보완 5.
- Confluence 721쪽(25묶음, 그림 2,682개 참조 중 로컬 2,574개 열람): 기계 확인 통과. 그림 로컬 사본 규칙(공백→_, 콜론·괄호 삭제)을 처음에 빠뜨려 한 번 재실행했다. 용량 오류로 끊긴 2묶음은 빠진 파일만 재실행. sonnet 표본 약 30구간·그림 10여 장 대조, 정정 2(그림 속 `WKQ` 오기, 오역).
- PDF 5종 634쪽(37작업): Codex가 300 dpi 쪽 이미지를 직접 판독(텍스트 추출본·Theory는 Marker 초안 참고). 기계 확인 전부 통과. sonnet 표본 36쪽·식 약 80개 대조, 정정: 식 (8.60) 곱 점 1, 서술·해석 정정 4.
- 범위 밖: `third_party_open`·`lib`·`redist`·`include` 외부 라이브러리, 빌드·설정, 바이너리, `manuals/refs/*.md`(이전 AI가 만든 요약·목록이라 원자료가 아님).
- 검사 도구 수정: `quotes.py` 짝짓기 결함(인용 0개 쪽을 골라 불일치를 숨김) 수정, 그림 줄 인용은 따로 셈. `pdfcheck.py --jobs`로 모델별 작업 목록.
- 문서·코드 대조 3종(`compare/EFDC-*.md`: 입력 카드 불일치 133, 이론 식 803개 중 불일치 284)과 흐름 분석 2종(`flow/EFDC-callflow.md`, `flow/EFDC-GVC-vs-plus.md`)을 마치고 노트 30개에 반영했다(`f3c6397a`). 보고서·노트 인용은 `citecheck.py`로 기계 대조.
- 확인하지 않은 것: 모델 실행. 문서와 코드 차이 중 어느 쪽이 맞는지(단위·정의에 따라 갈리는 항목은 해석으로 표시).

## ADCIRC 판독 (2026-10-09 시작, 진행 중)

대상 목록: `scripts/adcirc-batches.json`(코드 36묶음, 95파일 147,568행), `scripts/adcirc-docbatches.json`(문서 66묶음: 웹사이트 md 471쪽(중복 884 중 고유), 위키 161쪽, rst 150파일), `scripts/adcirc-website-canon.json`(웹사이트 중복 정리). PDF 42종과 pptx 3종은 1,933쪽이다(추출 `extract/ADCIRC/`). 범위 밖: asgs, adcircpy, StormEvents, `refs/subroutines.md`, `notes/adcirc-fort-files-reference.md`, 웹사이트 html(md와 중복), 웹사이트 PDF(manuals/pdfs와 중복), zip.

2026-10-09 22:51 기준 상태:
- 코드 묶음 1–7은 판독이 끝났고, 기계 확인(`runner/bcheck.sh`)을 통과했다. 인용 수는 726, 677, 707, 133, 1,185, 434, 1,059이고, 불일치는 0이다. sonnet 표본 대조는 하지 않았다. 커밋하지 않았다.
- 코드 묶음 8–36은 Codex가 분리 실행(`setsid nohup`, 5개 동시)으로 판독 중이다.
- 문서 66묶음은 코드가 끝나면(`ALLDONE-ac`) 자동으로 시작하도록 대기 중이다.
- Marker(`runner/admarker.sh`)가 PDF 초안을 만들고 있다. 끝나면 progress.txt에 `MARKER-ADCIRC-DONE`을 쓴다.
- `scripts/adcirc-pdfjobs.json`(18쪽 작업)은 아직 만들지 않았다.

이어받는 방법:
1. 실행 상태를 본다: `pgrep -fa "codex exec|codexone|ALLDONE"`. 진행 기록은 이전 세션 scratchpad `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/progress.txt`에 있다. 분리 실행 프로세스는 이 경로에 로그(`ac-N.log`, `ad-N.log`)를 쓴다. 쪽 이미지는 같은 곳의 `apages/`(1,933장)에 있다.
2. 프롬프트·스크립트·진행 기록 사본은 `~/.cache/coastal-recovery/adcirc-20261009/`에 있다. 옛 scratchpad가 지워졌으면 이 사본으로 남은 묶음을 다시 돌리고, 쪽 이미지는 `runner/adprep.sh`로 다시 만든다.
3. 끝난 코드 묶음마다 `bash runner/bcheck.sh ADCIRC _staging/recovery/scripts/adcirc-batches.json N ac-N`, 문서 묶음마다 `python3 scripts/dcheck.py ADCIRC scripts/adcirc-docbatches.json N <scratch>/ad-N.log`. 5묶음마다 sonnet 표본 대조 후 커밋.
4. PDF: `adcirc-pdfjobs.json`을 만든다(`manuals/pdfs/*.pdf`와 `extract/ADCIRC/office/*.pdf`, 18쪽 단위, `model: 'ADCIRC'`, Marker 초안 경로). `codexpdfread.py`로 프롬프트를 만들고 문서가 끝난 뒤(`ALLDONE-ad`) 돌린다. `pdfcheck.py --jobs`와 식 쪽 이미지 표본 대조.
5. 그 뒤: 문서·이론과 코드 대조, 흐름 분석, 노트 반영, 이 절 갱신, 대시보드 재생성(`dashboard_data.py`)과 재게시.

## 다음에 이어서 할 일

1. ~~매뉴얼과 코드 판독 기록 대조~~ — 10-03 완료(`compare/XBeach-manual-vs-code.md`, 노트 반영 `1da8d89`).
2. ~~XBeach 파일 간 계산 흐름 분석~~ — 10-07 완료(`flow/XBeach-callflow.md`, 노트 반영 `d89cd8b`). 판독 기록 검색은 `wiki_search` `path_class="records"`(`ce7b3ae`).
3. 다른 10개 모델(SFINCS·EFDC 완료, ADCIRC 진행 중, 나머지 9개 미착수): 같은 방식(고정 목록 → 1행/1쪽 판독 → 기계 확인 → 다른 모델 검증).
