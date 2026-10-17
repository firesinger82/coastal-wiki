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

## EFDC 판독 (2026-10-07~08 완료)

기록: `read/EFDC/EFDCPlus_Stable/`(EFDC+ 코드), `read/EFDC/EFDC-GVC/`(옛 판 코드), `read/EFDC/manuals/confluence/`(Confluence), `read/EFDC/manuals/pdfs/`(PDF). 대상 목록은 `EFDC-files.tsv`의 자체코드·매뉴얼·문서 분류.

- 자체 코드 510파일 307,120행: EFDC+ 207파일 131,630행(34묶음), EFDC-GVC 303파일 175,490행(46묶음). Codex `gpt-6.1-sol`, `codex exec` 5개 동시. 기계 확인 전부 통과(1행~끝 구간·sha·전 행 열람·원문 인용). sonnet 표본 약 110구간 대조, 틀림 0, 인용·표현 보완 5.
- Confluence 721쪽(25묶음, 그림 2,682개 참조 중 로컬 2,574개 열람): 기계 확인 통과. 그림 로컬 사본 규칙(공백→_, 콜론·괄호 삭제)을 처음에 빠뜨려 한 번 재실행했다. 용량 오류로 끊긴 2묶음은 빠진 파일만 재실행. sonnet 표본 약 30구간·그림 10여 장 대조, 정정 2(그림 속 `WKQ` 오기, 오역).
- PDF 5종 634쪽(37작업): Codex가 300 dpi 쪽 이미지를 직접 판독(텍스트 추출본·Theory는 Marker 초안 참고). 기계 확인 전부 통과. sonnet 표본 36쪽·식 약 80개 대조, 정정: 식 (8.60) 곱 점 1, 서술·해석 정정 4.
- 범위 밖: `third_party_open`·`lib`·`redist`·`include` 외부 라이브러리, 빌드·설정, 바이너리, `manuals/refs/*.md`(이전 AI가 만든 요약·목록이라 원자료가 아님).
- 검사 도구 수정: `quotes.py` 짝짓기 결함(인용 0개 쪽을 골라 불일치를 숨김) 수정, 그림 줄 인용은 따로 셈. `pdfcheck.py --jobs`로 모델별 작업 목록.
- 문서·코드 대조 3종(`compare/EFDC-*.md`: 입력 카드 불일치 133, 이론 식 803개 중 불일치 284)과 흐름 분석 2종(`flow/EFDC-callflow.md`, `flow/EFDC-GVC-vs-plus.md`)을 마치고 노트 30개에 반영했다(`f3c6397a`). 보고서·노트 인용은 `citecheck.py`로 기계 대조.
- 문서와 코드 차이의 결론은 아래 "노트 반영분 전수 대조와 차이 결론(10-12)" 절.

## ADCIRC 판독 (2026-10-09~10 판독 완료)

기록: `read/ADCIRC/adcirc/`(코드), `read/ADCIRC/manuals/website_markdown/`(웹사이트), `read/ADCIRC/manuals/wiki/`(위키), `read/ADCIRC/adcirc/docs/`(rst), `read/ADCIRC/manuals/pdfs/`·`read/ADCIRC/manuals/office/`(PDF·pptx). 대상 목록은 `scripts/adcirc-batches.json`, `scripts/adcirc-docbatches.json`, `scripts/adcirc-website-canon.json`(웹사이트 중복 884쪽 중 고유 471쪽), `scripts/adcirc-pdfjobs.json`.

- 자체 코드 95파일 147,568행(36묶음). Codex `gpt-6.1-sol` 5개 동시, 분리 실행. 기계 확인 전부 통과(인용 불일치 0). sonnet 표본 87구간 대조, 틀림 0, 보완 5(빠진 대입문, 축약한 FORMAT, 표시 없는 해석) 반영.
- 문서 66묶음: 웹사이트 471쪽, 위키 161쪽, rst 150파일. 전 행 열람·인용 대조 통과. sonnet 표본 대조는 한국어 요약의 뜻(동사·조건·부정·수량·의무)까지 봤다. 뜻이 바뀐 요약 4건(removed→수정, some→모든, error will result→종료, 치명적 오류)과 결과절이 빠진 요약 여러 건을 고쳤다. 표본 밖 요약에도 같은 종류의 오류가 남아 있을 수 있다.
- PDF 42종과 pptx 3종 1,933쪽(130작업). Codex가 300 dpi 쪽 이미지로 판독(Marker 초안 참고). 1990년대 보고서 대부분은 스캔본이라 인용의 기계 대조가 불가능하고, 검증은 쪽 이미지 표본 대조뿐이다. 이미지 표본 약 75쪽 대조, 틀림 1(xdmf2 p.5 'Internal'을 'Intertidal'로 읽음) 수정. 텍스트 층이 깨졌거나 그림 안 문구라 기계 대조에서 걸린 인용 약 35건은 이미지로 확인해 `visual-ok.txt`에 등록했다.
- 범위 밖: asgs, adcircpy, StormEvents, `refs/subroutines.md`, `notes/adcirc-fort-files-reference.md`(이전 AI 요약), 웹사이트 html(md와 중복), 웹사이트 PDF(manuals/pdfs와 중복), zip, `website_markdown/wp-json/index.md`(WordPress API 응답 JSON 한 줄, 기록은 있으나 전 행 열람·인용 대조 미통과).
- 사고: 10-10 04:00 L4 감사 cron 가드(`tools/llm-wiki-audit/run-audit-cron.sh` 82행)가 실행 중 새로 생긴 untracked 판독 기록 12개를 지웠다. 문서 묶음 42를 다시 판독했다. 가드가 `_staging/recovery/`를 복원·삭제하지 않게 고쳤다(`ba88e244`, 사용자 결정 10-10, 복제본에서 가짜 claude로 시험).
- 검사 도구 수정: `quotes.py` Markdown 이스케이프 무시, `pdfcheck.py` Marker 이미지 링크를 쪽 글자로 세지 않음, 공백만 있는 쪽 텍스트 무시.
- 문서·코드 대조 5종(10-10, Codex `gpt-6.1-sol` 5개 동시): `compare/ADCIRC-fort15-vs-code.md`(주 표 358행 중 불일치 131, NWS 보충 줄 126행 중 21), `ADCIRC-inputfiles-vs-code.md`(516행 중 불일치 90), `ADCIRC-outputs-vs-code.md`(불일치 60유형 145행), `ADCIRC-theory-vs-code.md`(번호 식 456개 등, 2004 이론 매뉴얼 136행 중 불일치 39), `ADCIRC-features-vs-code.md`(351행 중 불일치 80). 문서는 rst(현행)·위키·웹 v53·PDF(v44.XX와 1990년대 보고서) 순으로 보고, 코드는 v56.2.1이다. 판 차이는 판정 이유에 적었다.
  - 기계 확인: `scripts/citecheck_path.py`(경로 인용·`.F`·`.md`·링크형·역순 `이름 — 경로:줄` 지원)로 인용 25,477개 대조, 일치 25,475, 불일치 2(노트 문장 안의 인용을 잡은 검사 오판).
  - sonnet 표본 50행(보고서마다 10행) 대조: 맞음 43, 부분 5, 틀림 2. 틀림 2는 sponge 층 '코드에서 찾지 못함'(실제 `read_input.F:5637–5718`에 구현)과 fort.15 NWS=6 계열 '불일치'였다. NWS=6은 이웃 행 이유를 복사한 오류로 같은 표 8행에 퍼져 있었고, 표 전체를 스크립트로 대조해 8행만 해당함을 확인했다. 모두 원문 확인 후 정정(`[10-10 검증 정정]`·`[10-10 검증 보완]`), 요약 표 수 갱신. 표본 오판율로 보아 표본 밖 행에도 틀린 판정이 남아 있을 수 있다.
- 흐름 분석(10-11, Codex `gpt-6.1-sol`): `flow/ADCIRC-callflow.md`. driver.F → ADCIRC_Init → ADCIRC_Run → TIMESTEP의 직접 호출 64행과 2단계 호출, 변수 생산·소비 37행, 문서(code_architecture.rst·DevGuide·SDD)와 노트 대조, 노트 수정안. mermaid 2개(초기화·시간 반복, TIMESTEP 내부)를 렌더해 확인했고, 상자의 `src/파일:줄` 100개를 원문과 대조했다.
  - 기계 확인: 인용 6,553개 일치. `citecheck_path.py`에 '`이름` `경로:줄`'(정의 위치) 형식을 추가했다. 이 형식은 앞 이름이 그 줄에 있으면 통과하므로 뒤 인용의 오기를 놓칠 수 있다.
  - sonnet 표본 18행: 맞음 16, 부분 2, 틀림 0. 맞음 중 1행(F:1430)은 호출 사슬 일부를 끝까지 따라가지 않았다. 부분 2(핫스타트 분기를 둘로 적음, 마찰 노트 대조의 이유 부족)를 원문 확인 후 정정·보완(`[10-11 검증 정정]`·`[10-11 검증 보완]`).
- 노트 반영(10-11, Codex `gpt-6.1-sol` 3개 동시, 노트 묶음을 겹치지 않게 나눔): 노트 35개를 고쳤다. 반영 기록은 `flow/ADCIRC-notes-apply-{A,B,C}.md`다. 대조 보고서 5종과 흐름 보고서의 수정안 행 ID를 모두 처리했다. 처리하지 않은 행은 보고서가 "판정하지 못한 세부 주장"·"판정을 제한한 항목"·"수정 불필요"로 둔 행뿐이다(스크립트로 대조). 새 절: `adcirc-timestep-orchestration.md` 시간 단계 호출 흐름(mermaid 2개, 렌더 확인), `adcirc-fort-files-reference.md` 문서와 코드 입력 차이, `adcirc-output-writers-implementation.md` 문서와 코드 출력 차이, `04-theory-pdf-v44xx.md` 이론 식 차이.
  - 기계 확인: 노트의 `[file=경로 line=N]` 형식을 `경로:N`으로 바꾼 임시 사본에서 `citecheck_path.py`로 인용 약 7,000개를 대조했다. 불일치는 이번에 고치지 않은 기존 줄 1건(검사 짝짓기 오판)이다. `tools/validate-all.sh` 통과.
  - sonnet 표본 24줄(추가된 1,144줄에서 무작위): 맞음 20, 부분 4(핫스타트 레코드 순서 표현, XDMF tau의 `NOLIBF=0` 조건, RaysIce·IceCube의 max·음수 분기 누락). 4건 모두 원문을 열어 확인하고 고쳤다. 표본 밖에도 조건 누락이 남아 있을 수 있다.
- 문서와 코드 차이의 결론은 아래 "노트 반영분 전수 대조와 차이 결론(10-12)" 절.

## ShorelineS 판독 (2026-10-12)

기록: `read/ShorelineS/shorelines/`(코드·문서), `read/ShorelineS/shorelines/doc/*.pdf/`(PDF). 대상 목록: `scripts/shorelines-batches.json`(자체 코드 `functions/` MATLAB 136파일 + `compiled/launchShorelineS.sh`, 137파일 19,941행), `scripts/shorelines-docbatches.json`(README 2·출판 목록·`compiled/input.txt`·`ShorelineS.ipynb`), `scripts/shorelines-pdfjobs.json`(매뉴얼 v1.0 66쪽, FAQ 15쪽, FMarS2020 20쪽, ICEC2018 10쪽 = 111쪽). 테스트·예제(`script/` 333파일, 대부분 그림)는 다른 모델과 같은 기준으로 제외.

- 코드·문서: Codex `gpt-6.1-sol` 6묶음. 기계 확인 142기록 전부 통과(1행~끝 구간·sha·행 수). sonnet 표본 30구간: 맞음 26, 부분 4(변수 용도 단정, 루프 순서 해석, 삭제 대상 반대, 점 개수) → 고침. 표본 오류율을 보고 전 기록을 `gpt-6-astra`로 의미까지 전수 대조: 정정 93, 보완 80(`read/ShorelineS/verify-*.md`). 원문 인용 6,938개 중 불일치 1(원문 한 줄에 UTF-8과 ISO-8859가 섞인 검사 오판).
- PDF 111쪽(7작업): Codex가 300 dpi 쪽 이미지로 판독(Marker 초안 참고). 용량 오류로 끊긴 2작업은 재실행. 기계 확인 7작업 전부 통과. sonnet 쪽 이미지 표본 12쪽 모두 맞음, 빠진 구절 2곳 보완(FAQ p.5는 Claude가 이미지로 확인).
- 검사 도구 수정: `quotes.py`가 UTF-8로 읽지 못하는 원문(ISO-8859)을 latin-1로 다시 읽는다.

## ShorelineS 대조·흐름·노트 반영 (2026-10-12 완료)

- 대조 보고서 3종(Codex `gpt-6.1-sol`): `compare/ShorelineS-theory-vs-code.md`(매뉴얼 v1.0 식 (1)~(78)·FAQ·2018/2020 논문 식 대 코드), `compare/ShorelineS-inputs-vs-code.md`(S 필드·입력 파일 형식), `flow/ShorelineS-callflow.md`(초기화·시간 단계 호출 순서, mermaid 2개 — 렌더 확인).
- 외부 원문(sonnet 웹 조회, 5묶음): Seabrook & Hall 1998 식 (4)·Hallin 학위논문 식 3.23·3.49·Vitousek & Barnard 2015는 원문을 직접 읽음. SPM 1984·Stockdon 2006은 2차 문헌 기준. 결과: 매뉴얼 식 (73) Stockdon `/2` 위치 B, 식 (58) 지수 부호 B, 코드 `wave_transmission.m:94` 선형 두 항 부호 E(강함), `dune_growth.m:75` 입경비 역수 E(강함), CERC3 `gamma.^-0.52` E(중간).
- git 이력 판정(Codex `gpt-6-astra`): 원본 저장소(`raw/.../shorelines`, HEAD `f3ec8638`, 47커밋, 2018-05-24~2026-08-13, 작업 트리 변경 없음, `7bf4481` 이후 변경은 매뉴얼 PDF 추가 하나)의 문서 날짜 직전 커밋과 대조. 이론·흐름의 A 10행은 문서 시점 코드도 현재와 같아 A 0(B 4·C 6으로 변경). D 39행 중 18행은 과거 코드에 있다가 지워진 기능이라 A로 변경(대부분 `f5f12430` 2024-06-14 "Midsummer 2024 beta release"). E 32행은 도입 커밋과 반대 증거를 찾아 모두 유지(외부 원문 판정으로 이론 E 4행 추가). 기록: `compare/ShorelineS-git-verify*.md`.
- 결론 전수 재검증(Codex `gpt-6-astra`, sonnet 표본 22행 중 부분 4를 보고 전수로): 398행. 최종 분류 — 이론 189행 A0·B16·C104·D4·E11·F33·H21, 입력 166행 A18·B27·C76·D18·E19·F4·H4, 흐름 43행 A1·B11·C20·D1·E6·F3·H1. G·X 0.
- 노트 반영(Codex `gpt-6.1-sol`, 스트림 끊김 1회 이어서 재실행): 노트 9개, 각 노트 "문서와 코드 차이 (10-12 대조)" 표, 대표 노트 `shorelines-architecture-map.md`에 흐름도 2개와 "코드 결함 후보 (정적 판독)" 28행(E 36행을 원인별로 묶음). 기록: `flow/ShorelineS-notes-apply-{1,2}.md`.
- 추가 줄 전수 대조(Codex `gpt-6-astra`): 1,002줄, 정정 74·보완 29(`flow/ShorelineS-notes-verify-{1,2}.md`). sonnet 표본 24줄: 맞음 22, 부분 2(각도 제한 줄 인용 누락, `dsdn` 설명) → 고침. 같은 표본에서 보고서의 `Kw=4.2` 목록 쪽(PDF 50 → 51) 정정.
- 기계 확인: 현재 코드 인용(보고서 6,874·노트 2,809)과 과거 커밋 인용(`HASH:path:N`, 보고서 398·노트 317, `git show`로 대조) 불일치 0. 남은 경고는 같은 이름 README 2개로 인한 검사기 오판.

## SWAN 판독 (2026-10-12~13)

기록: `read/SWAN/swan/`(코드·스크립트), `read/SWAN/manuals/website/`(웹 문서), `read/SWAN/manuals/pdfs/*.pdf/`(PDF), 전수 검증 결과 `read/SWAN/verify/`. 대상 목록: `scripts/swan-batches.json`(자체 코드 `src/*.ftn*`·`bin/swanrun`·`switch.pl`·`src/CMakeLists.txt`, 75파일 122,313행; `fftpack51.ftn90`·`agioncmd.ftn90`·`nctablemd.ftn90`은 범용 라이브러리라 제외), `scripts/swan-docbatches.json`(README·`modifications.htm`·`patches/41.51.A`·`problems_and_fixes.htm`·`swan.edt`·`swanrun.bat`·웹 문서·설정 예제 24파일), `scripts/swan-pdfjobs.json`(Cycle III 41.51 매뉴얼 swanuse 154쪽, swantech 176쪽, swanimp 35쪽, swanpgr 51쪽 = 416쪽). 웹 `online_doc`·`website_markdown`(같은 41.51 매뉴얼의 HTML 사본), 이전 AI 요약, 바이너리·압축본, `doc/*.pdf` 중복본, `tools/`는 제외. 코드 판 = `VERNUM = 41.51`(`swanmain.ftn:965`).

- 코드·문서: Codex `gpt-6.1-sol` 20작업. 스트림 끊김 4작업(큰 파일 swancom4·swanmain·swanout1·swanser)은 400행마다 기록을 덧붙이게 해서 재실행. 기계 확인 99기록 전부 통과(1행~끝 구간·sha·행 수, 읽은 범위 로그 확인). 행 첫머리 `!JAC`·`!WFR`·`!MPI` 등 전처리 표시는 `switch.pl` 82–105행 규칙에 따라 어느 스위치에서 사는 행인지 함께 적었다.
- PDF 416쪽(24작업): Codex가 300 dpi 쪽 이미지로 판독(Marker·opendataloader 추출 참고). 끊긴 작업 2개는 재실행·이어 쓰기. 기계 확인 24작업 전부 통과.
- sonnet 표본 21건(코드·문서 14구간, PDF 7쪽): 맞음 17, 부분 4(인덱스 계산을 코드에 없는 말로 씀, 주석 속 차분식 누락, 바깥 IF 범위 오기, 쪽 원문의 한정 표현 누락) → 표본 오류율을 보고 전 기록을 `gpt-6-astra` 53작업으로 의미까지 전수 대조: 정정 701, 보완 1,668, 이상 없음 1,491(작업별 요약 줄 합계).
- 정정분 sonnet 표본 20건: 맞음 19, 부분 1(swanpre1 1832–1908 첫 문장의 바깥 블록 표기) → Claude가 고침. 앞 표본의 부분 4건은 모두 고쳐진 것을 확인.
- 최종 기계 확인: 원문 인용 34,739개 중 불일치 2. 둘 다 swancom2 679·719행이다. 원문은 `\|`이고 기록은 표 칸 안 이스케이프로 `\\|`라고 썼다. 렌더 결과는 원문과 같으므로 검사 오판이다.

## ROMS 판독 (2026-10-13~14)

기록: `read/ROMS/roms/`(코드·입력 예제), `read/ROMS/manuals/wiki/wikitext/`(ROMS 위키 321쪽), `read/ROMS/`의 나머지(Data/ROMS/CDL 등). 대상 목록: `scripts/roms-batches.json`(ROMS/{Adjoint,Tangent,Representer,Nonlinear,Utility,Modules,Drivers,Functionals,Include,Programs}·Master의 .F/.h, makefile, CMakeLists.txt, `ROMS/Bin/build_roms.sh` — 881파일 971,495행, 192작업; 사용자 지시로 자료동화 코드 Adjoint·Tangent·Representer 포함; Utility 범용 라이브러리 11파일 lapack_mod·nrutil·erf·ran_state·gasdev·ran1·round·ludcmp·lubksb·sqlq·yaml_parser와 Obsolete·External 코드 제외), `scripts/roms-docbatches.json`(위키 wikitext 321쪽, User/External의 roms_* 아닌 .in, ROMS/External의 varinfo.yaml·ice.in·vegetation.in·coupling_mct.dat, docs/README.md, ROMS_ChangeLog.md, License_ROMS.md, Data/ROMS/CDL 24 — 368파일 64,986행, 19작업). WRF, roms_test, roms_matlab, roms-jedi, website(forum·blog), website_markdown, AI 요약 refs/subroutines.md, 응용 .in, Compilers, ESM은 제외. 원본 저장소 `raw/source_code/roms` HEAD `57aecf58`.

- Codex `gpt-6.1-sol` 211작업, 6개 동시. cpp 지시문(`#if`·`#ifdef`·`#ifndef`·`#elif`·`#else`·`#endif`·`#define`·`#undef`·`#include`)은 원문 그대로 인용하고, 구간 첫머리에 감싸는 전처리 조건을 적게 했다. 400행마다 덧붙여 저장하고 끊기면 이어 읽는다. 용량 오류("Selected model is at capacity")로 끊긴 11작업(rr-61·63·69·70·72·76·80·96·111·162·172)은 이어 쓰기로 재실행해 모두 끝났다.
- 기계 확인 1,249기록 전부 통과: 1행~끝 구간·sha·행 수, 전 행 열람(재실행 작업은 두 세션 로그를 합쳐 확인). 위키 2쪽(I4DVAR_ANA_SENSITIVITY, I4DVAR_Observation_Impact_Tutorial_2010)은 열람 로그로 확인되지 않아 Codex가 `nl -ba`로 다시 읽고 기록을 고쳤다(참고문헌·목차 보완, 축약 식·그림 부재 단언 정정). 원문 인용 454,411개 중 불일치 41개는 모두 검사기 오판이다: 위키 `\<br />` 이음 행(coupling.in 17·coupling_esmf.in 21), 표 칸 안 `\|` 이스케이프(I4DVAR 1), 굵은 글씨 표기 생략(NUOPC_Cap 1), 다른 파일 행 번호 인용(fennel_var.h 기록의 `fennel_mod.h:101`, 1).
- sonnet 표본 24구간(코드 18·문서 6, 무작위): 맞음 24. 사소한 행 범위 표기 1건(get_ngfld.F 361–364의 END IF 행)을 원문 확인 후 고쳤다(`[10-14 표본 정정]`). 표본 오류가 없어 전수 의미 대조는 하지 않았다.

## ROMS 대조·흐름·노트 반영 (2026-10-14 완료)

- 대조 보고서 12종(Codex `gpt-6.1-sol`): `compare/roms-{theory-numerics,mixing-bc-forcing,biology,sediment-ice-vegetation,da-4dvar,da-representer,inputs,outputs-metadata,coupling-nesting-parallel,build-options-history,testcases,tools-guides}-vs-code.md`. 흐름 분석 2종: `flow/ROMS-callflow-nonlinear.md`(비선형 시작·계산 순서), `flow/ROMS-callflow-da.md`(4D-Var·representer). 각 mermaid 3개, 렌더 확인.
- 외부 원문: 7행. RMF1-239 B, RMF1-816 B, RMF1-688 E 중간(`ROMS/Utility/equilibrium_tide.F:276`의 `/36524.25_r8`, 위키는 `/ 36525`), RMF1-837 F, RMF1-837a C(새 행, `sed_bedload.F:504–509` `IF (ABS(phi_x2).gt.phi_x1)`, 원식 MAX는 주석, `5e82991c` 2008-08-19), XR-001 D, XR-002 F. 기록: `compare/ROMS-external-sources.md`.
- git 이력 판정(Codex `gpt-6-astra` 11작업): 원본 저장소(`raw/source_code/roms`, 1,005커밋, 태그 roms-2.0~4.2, HEAD `57aecf58` 2026-09-18)에서 1,241행. A 후보 954행 → A 848·B 52·C 20·D 6·F 7·H 2. D 133행 → A 36·D 71·B 14·F 12. E 154행 → E 144·B 8·C 1·A 1. 기록: `compare/ROMS-git-verify-{A1..A8,D1,E1,E2}.md`.
- 결론 표본(sonnet 30행): OK 23·부분 4·틀림 3. 틀림 유형은 git 판정 미반영(RBH-0821·RBH-1588), 코드에 없는 동작 단언(RBH-1535), 근거 줄 오기다. 이 유형을 넣어 결론 전수 재검증을 했다(Codex `gpt-6-astra` 28작업, 보고서별 "## 전수 검증 기록 (10-14)"). 전수 검증이 git 판정 B를 A로 바꾼 3행(RT1-538·547·548)은 Claude가 `roms-3.0`의 `ana_fsobc.h`·`ana_m2obc.h` WEDDELL 블록에서 문서 식과 반복문을 확인했다. 기록: `compare/ROMS-conclusion-sample.md`.
- 최종 결론(차이 결론 절 9,269행, 결론 열에서 셈): 일치 327·A 935·B 861·C 1,597·D 85·E 157·F 303·H 5,004. G·X 0.
- 노트 반영(Codex `gpt-6.1-sol`): 먼저 보고서별 14작업으로 노트에 넣을 3,938행(H·일치 제외)마다 담당 파일 하나를 정했다(`assign/ROMS-assign-*.tsv`). 이어 20작업이 반영했다(`assign/note-job-*.tsv`, `flow/ROMS-notes-apply-{1..20}.md`). 기존 노트 42개를 고쳤다. 차이 행이 150개를 넘는 노트 5개(cppdefs 2·io_netcdf·biology·analytical_functionals)는 표를 차이 파일 12개로 나눴고, 새 노트 3개(version-history·test-cases·tools differences)를 만들었다. 대표 노트: `roms_main_driver_dispatch.md`(비선형 흐름도), `roms_4dvar.md`(자료동화 흐름도), `models/ROMS/README.md`(코드 결함 후보 E 157행 표). 행 ID 대조로 3,938행이 모두 배정 파일에 한 번씩 있고 분류가 보고서와 같음을 확인했다.
- 추가 줄 전수 대조(Codex `gpt-6-astra` 20작업): 정정 274줄·보완 89줄(`flow/ROMS-notes-verify-{1..20}.md`, 노트 태그 수). 예: `roms_analytical_functionals.md`의 `ana_initial.h:72` `ANANAME(2)` 인용을 101행 `ANANAME(10)=MyFile`로 정정.
- 기계 확인: 바뀐 노트 57개의 `경로:줄` 인용 31,835개 중 불일치 표시 28개는 위키 마크업(링크 대괄호·작은따옴표 세 개 굵게 표시·`&nbsp;`·`<math>`) 생략과 "수정 전 노트 인용"이다. 하나씩 원문을 열어 확인했다. 위키 튜토리얼 원문의 홈 디렉터리 경로 2곳은 인용에서 `~`를 `…`로 줄이고 그 사실을 적었다(G8b). `tools/validate-all.sh` 통과.
- sonnet 표본 38건(표 행 30·본문 수정 8): OK 37·부분 1(CD-010 근거 인용 누락) → `hypoxia_srm.h:342·359·361·364` 인용을 노트와 보고서에 보탰다(`[10-14 표본 보완]`). 선택 지적 1건(`roms_open_boundaries.md`의 `obc_volcons.F:207·227` 인용)도 넣었다. 기록: `compare/ROMS-notes-sample.md`.

## SWAN 대조·흐름·노트 반영 (2026-10-13 완료)

- 대조 보고서 7종(Codex `gpt-6.1-sol`): `compare/swan-theory-{numerics,sources,obstacles-setup-qc-bc}-vs-code.md`(swantech 식 대 코드), `compare/swan-inputs-{setup,physics-numerics}-vs-code.md`(swanuse 명령 대 `swanpre1`·`swanmain`), `compare/swan-outputs-vs-code.md`(출력 변수·형식), `compare/swan-implementation-history-vs-code.md`(swanimp·swanpgr·웹 수정 이력·패치·설정 예제). 흐름 분석 `flow/SWAN-callflow.md`(mermaid 3개 — 렌더 확인).
- 외부 원문(sonnet 웹 조회) 3행: TN-089(Hersbach & Janssen 1999 제한기, 논문 본문은 접근 차단으로 WW3·ECWAM 코드와 ECMWF IFS Cy48r1 문서로 판정) H, QC-020(Akrish et al. 2020 식 (2.2)) F, SS-537(Zieger 너울 소산 계수 B1Z) F. 기록: `compare/SWAN-external-sources.md`.
- git 이력 판정(Codex `gpt-6-astra`): 원본 저장소(`raw/source_code/swan`, 98커밋, 2022-07-30~2026-07-13, HEAD `43e9bbb`, 실제 patch B 변경 `0dabfa4`)에서 문서 시점(41.51 공개 `7ee8981` 2024-09-02)과 41.45 공개(`2980d1a`~`122b595`, 2023-02-27~28)를 대조. A 후보 105행 중 A 26·B 5·C 44·D 22·H 8. D 45행 중 D 43·F 2(QC-050·QC-058). E 39행은 도입 커밋(대부분 `b2ae30e` 최초 반입)·수정 기록·반대 증거를 찾아 모두 유지(강함 31·중간 7·약함 1). 기록: `compare/SWAN-git-verify-{A,D,E}.md`.
- 결론 전수 재검증(Codex `gpt-6-astra` 10작업, sonnet 표본 26행에서 OK 17·부분 8·틀림 1을 보고 전수로): 보고서 8종 1,134행. 최종 분류 일치 19·A 26·B 246·C 405·D 34·E 39·F 93·H 272. G·X 0. QC 이론 정의(Weyl·Moyal 등) D 31행은 구현 지시가 아니라 H로, 2행은 F로 바꾸고 이유를 적었다. 기록: 각 보고서 "## 최종 집계"와 `compare/SWAN-conclusion-sample.md`.
- 노트 반영(Codex `gpt-6.1-sol` 7작업 + 누락 보완 1작업): 노트 60개에 "문서와 코드 차이 (10-13 대조)" 표. 대표 노트 `source-analysis/swan-foundation.md`에 흐름도 3개와 "코드 결함 후보 (정적 판독)" E 39행. 작업 사이에 넘긴 15행이 어느 노트에도 안 들어간 것을 행 ID 대조로 찾아 지정 노트에 넣었다(`flow/SWAN-notes-apply-8.md`). 결론 행 1,115행(일치 19행 제외)이 모두 노트에 있다.
- 추가 줄 전수 대조(Codex `gpt-6-astra` 12작업): 정정 233줄·보완 95줄(`flow/SWAN-notes-verify-{1..12}.md`, 노트 태그 수). sonnet 표본 25줄(정정 줄 10 포함): 맞음 23, 부분 2(1D 갱신식 인용 줄, 수정 전 노트 줄을 현재 줄처럼 인용) → 고침. 같은 표본에서 보고서 R3 SU-042의 줄 번호 11864 → 11863 정정. 표본 검증자가 확인하지 못한 3항목(비구조 COMPGRID 정점값, (8.44)–(8.45)의 반변 기저 차원, (5.24) 화살표)은 Claude가 쪽 이미지·코드로 확인했다(`flow/SWAN-notes-sample.md`).
- 기계 확인: 바뀐 노트의 과거 커밋 인용(`HASH:path:N`) 820개 불일치 0. 현재 코드·문서 인용 불일치 표시는 검사기 오판(여러 줄 HTML 문장, Fortran 연속 줄과 줄 끝 판 번호, 노트 자기 경로, 같은 이름 README, 인용 짝짓기)이며, 87건 후보는 전수 대조 작업이 하나씩 판정했다. `tools/validate-all.sh` 통과.

## SWASH 판독 (2026-10-14~15)

기록: `read/SWASH/swash/`(코드·빌드·문서), `read/SWASH/swash/doc/*.pdf/`(PDF), 전수 검증 결과 `read/SWASH/verify/`. 대상 목록: `scripts/swash-batches.json`(자체 코드 `src/*` 162파일과 `switch.pl`·`bin/swashrun`, 164파일 180,232행, 40작업), `scripts/swash-docbatches.json`(README.md·Makefile·CMakeLists.txt·clobber.cmake·`bin/swashrun.bat`·`misc/swash.edt`·`misc/machinefile` 7파일), `scripts/swash-pdfjobs.json`(swashuse 167쪽, swashtech 128쪽 = 295쪽, 16작업). `tools/*.m`(SWAN과 같은 기준)과 LICENSE는 제외. 코드 판 = `VERNUM = 12.01`(`src/SwashInit.ftn90:79`), 매뉴얼 표지 = "SWASH version 12.01".

- 코드·문서: Codex `gpt-6.1-sol` 41작업. 행 첫머리 `!TIMG`·`!MPI`·`!F95` 등 전처리 표시는 `switch.pl` 57–66행 규칙에 따라 어느 스위치에서 사는 행인지 함께 적었다. `!DIFF`·`!MUD`·`!TEST`·`!VEGE`는 규칙에 없어 주석으로 남는다고 적었다. 기계 확인 171기록 전부 통과(1행~끝 구간·sha·행 수, 전 행 열람).
- PDF 295쪽: Codex가 300 dpi 쪽 이미지로 판독(Marker·opendataloader 추출 참고). 세션 로그로 295쪽 이미지를 모두 연 것을 확인했다. 기계 확인 16작업 전부 통과.
- sonnet 표본: 코드 20구간 중 맞음 18, 부분 2(SwashImpLayP2DHflow 1346행 `k-1`을 "아래층"으로 씀 — SWASH는 k=1이 맨 위층; SwashImpLayP1DHflow 1366행 분기를 조건식 `if ( propsc /= 1 ) then` 없이 씀). PDF 16쪽 중 맞음 12, 부분 4(쪽에 없는 말 추가, τ_cd를 τ_ce로 씀, 괄호 설명을 적용 조건으로 읽음, 앞 쪽 내용 끌어옴). 표본 오류를 보고 전 기록을 `gpt-6-astra`로 의미까지 전수 대조했다. 코드 58작업: 정정 410, 보완 3,502, 이상 없음 1,342. PDF 8작업: 정정 164, 보완 59(작업별 요약 줄 합계). swashtech p.54 그림 2.8의 첨자 하나는 1과 l을 구별할 수 없어 `[원문 인쇄 판독 불가]`로 남겼다.
- 정정분 sonnet 표본 24행: 맞음 24. 앞 표본의 부분 6건은 모두 고쳐진 것을 확인했다.
- 최종 기계 확인: 원문 인용 64,615개 중 불일치 0.

## SWASH 대조·흐름·노트 반영 (2026-10-15 완료)

- 대조 보고서 6종(Codex `gpt-6.1-sol`): `compare/swash-{theory-framework,theory-unstructured,inputs-setup,inputs-physics-numerics,outputs,guide-syntax-build}-vs-code.md`. 흐름 분석 `flow/SWASH-callflow.md`(시작·입력 읽기 순서, 계산 순서, 변수 생산·소비, 문서 대조). mermaid 3개(전체, 구조 격자 한 단계, 비구조 격자 한 단계)는 렌더해 확인했다.
- 외부 원문: 위키 원자료는 커밋 1개짜리 얕은 사본이다. 공개 저장소(gitlab.tudelft.nl/citg/wavemodels/swash)를 `extract/SWASH/external/gl`에 받았다. main은 91커밋(2022-07-30 `744735e` ~ 2026-05-26 `a486d5f`)이고 HEAD의 src는 원자료와 같다. 매뉴얼 PDF의 마지막 변경은 `7949227` 2026-05-06 "release v12.01"이다. 그 뒤 코드 커밋은 `608ffd7`·`9554c98` 둘(5파일, 41줄)이다. 웹 `swash-12.01.tar.gz`의 src 162파일은 원자료와 바이트 단위로 같다. 웹 PDF 텍스트도 원자료와 같다. `swash-11.01.tar.gz`·`modifications.htm`·`problems_and_fixes.htm`도 받았다(extract는 커밋하지 않는다).
- git 이력 판정(Codex `gpt-6-astra` 3작업): E 39행 → E 37·C 2. A 후보(12.01 뒤 변경 덩어리를 인용한 283행, 문서 지연 후보 B 123행) → A 2(SI1-259 LAYERS 파일 교체 문장은 `9d03fff` 이전 동작, SO1-293 출력 키워드 94개는 9.01 `5d279d7`의 수, 10.01 `9b8a012`부터 96개 — Claude가 두 판에서 직접 셈). D 3행은 모두 D 유지. 기록: `compare/SWASH-git-verify-{E1,E2,AD}.md`.
- 결론 표본(sonnet 30행): OK 26·부분 3·틀림 1. 유형은 기본값만 보고 H로 둠(SI1-017, `stricthead`는 UMOM HEAD로 켜짐), 다른 매뉴얼에 있는 내용을 C로 둠(ST1-287), 코드 대조한 행을 H로 둠(SI1-143), 같은 사실을 두 행이 다르게 분류함(SO1-295·SO1-100). Claude가 세 위치를 원문에서 확인했다. 이 유형을 넣어 결론 전수 재검증(Codex `gpt-6-astra` 10작업): 1,438행, 정정 344·보완 441·분류 변경 79(작업 요약 줄 합계). 기록: `compare/SWASH-conclusion-sample.md`, 보고서별 "## 전수 검증 기록 (10-15, …)".
- 최종 결론(차이 결론 절 1,438행, 결론 열에서 Claude가 셈): 일치 30·A 2·B 150·C 428·D 3·E 41·F 109·H 675. G·X 0. 보고서의 분류별 개수 줄을 이 값으로 바꿨다.
- 노트 반영(Codex `gpt-6.1-sol`): 보고서별 7작업이 A–F 733행마다 담당 노트 하나를 정했다(`assign/SWASH-assign-*.tsv`). 8작업이 반영했다(`assign/SWASH-note-job-*.tsv`, `flow/SWASH-notes-apply-{1..8}.md`). 기존 노트 26개를 고쳤고 새 노트 `manual-notes/swash-build-run-differences.md`를 만들었다. 흐름도 3개는 `swash-timestepping-update-driver.md`에 옮겼다(보고서 블록과 글자 단위로 같음). `models/SWASH/README.md`에 코드 결함 후보 E 41행 표를 넣었다. 이 표는 작업 8이 지시문의 경로 누락으로 저장소 루트 README에 넣은 것을 Claude가 옮긴 것이다. 행 ID 대조로 733행이 모두 배정 파일에 한 번씩 있고 분류가 보고서와 같음을 확인했다.
- 추가 줄 전수 대조(Codex `gpt-6-astra` 8작업): 2,039줄, 정정 131·보완 46(`flow/SWASH-notes-verify-{1..8}.md`, 노트 태그 수와 같음).
- 기계 확인: 바뀐 노트 27개의 `경로:줄` 인용 2,174개 중 불일치 표시 147개다. 과거 커밋 인용(`8756667:src/...`, Claude가 7개를 직접 열어 확인), 두 백틱 사이 문장, 노트 자기 인용, 수정 전 줄 인용이 섞인 검사 오판이다. 전수 대조 작업이 후보를 하나씩 판정했다. `tools/validate-all.sh` 통과.
- sonnet 표본 30줄(표 22·본문 8): OK 29·부분 1(README.md:80 manual-notes 파일 수 3 → 반영 뒤 4) → 고쳤다(`[10-15 표본 정정]`). 표본이 찾은 보고서 쪽 번호 오기(SG1-875 p.37 → p.38)도 보고서에서 고쳤다. 기록: `compare/SWASH-notes-sample.md`.

## FUNWAVE 판독 (2026-10-17)

기록: `read/FUNWAVE/FUNWAVE-{TVD,GPU}/`(코드·빌드·tex), `read/FUNWAVE/FUNWAVE-TVD/doc/*.pdf/`(PDF), 전수 검증 결과 `read/FUNWAVE/verify/`. 대상 목록: `scripts/funwave-batches.json`(자체 코드 FUNWAVE-TVD `src/*.F` 38파일과 FUNWAVE-GPU `src/*.F` 41파일, 79파일 67,922행, 14작업), `scripts/funwave-docbatches.json`(README.md, 빌드 파일 41개, `doc/funwave_tvd_3.0.tex` 2,829행, 3작업), `scripts/funwave-pdfjobs.json`(funwave_tvd_3.0 89쪽, funwave_tvd_2.1_manual 77쪽, Intro-to-FUNWAVE-CHL-TN 24쪽, funwave_code_analysis 15쪽 = 205쪽, 12작업). 제외: 테스트·예제(`simple_cases/`·`benchmarks/`, 다른 모델과 같은 기준), `tools/*.m`(부속 도구), `funwave-work/build/pre/*.f90`(빌드가 만든 전처리 사본), `.o`·`.mod`, LICENSE, `manuals/funwave_tvd_3.0.md`(같은 3.0 PDF의 텍스트 변환본). 코드 판 = `FUNWAVE-TVD/src/main.F:47` `!    VERSION 3.0`, README "This version is a beta version.". 위키 원자료 두 저장소는 커밋 1개짜리 얕은 사본이다(TVD `b4c322e` 2025-01-24, GPU `7f892ba` 2019-11-26). GPU 작업 트리는 `src/etauv_solver_gpu.F`·`src/mod_cuda.F`·`src/Makefile_cuda`가 커밋과 다르다(커밋하지 않은 로컬 수정, 21줄 추가·7줄 삭제).

- 코드·문서: Codex `gpt-6.1-sol` 17작업. C 전처리 조건(`# if defined (CARTESIAN)` 등)은 원문 그대로 인용하고 어느 플래그 조합에서 컴파일되는지 적었다. 기계 확인 121기록 전부 통과(1행~끝 구간·sha·행 수, 세션 로그로 전 행 열람 확인).
- PDF 205쪽: Codex가 300 dpi 쪽 이미지로 판독(Marker·opendataloader 추출, 3.0은 tex 원고 참고). 기계 확인 12작업 통과. 인용 없는 쪽 3.0 p.87–89는 식만 있는 쪽이다(추출 텍스트에도 6단어 이상 문장 없음). Intro-TN p.12 인용 1개는 표 칸 텍스트 층이 깨진 것이라 Claude가 쪽 이미지로 확인해 `visual-ok.txt`에 넣었다.
- sonnet 표본: 코드 20구간 맞음 20(보완 후보 1: `fluxes_21v.F` 892–906이 `# if defined (CARTESIAN)` (884) 안이라는 점이 모호 → Claude가 고침). PDF 16쪽 맞음 15·부분 1(3.0 p.73 캡션 "Solid line: model, stars: data."와 그림 범례(실선=data, 파선=model)의 모순을 적지 않음). 앞 모델과 같이 전 기록을 `gpt-6-astra`로 의미까지 전수 대조했다. 코드 22작업: 정정 213, 보완 1,513, 이상 없음 895. PDF 6작업: 정정 141, 보완 95, 이상 없음 36(작업별 요약 줄 합계).
- 정정분 sonnet 표본 28행(코드 14, PDF 14): 맞음 27, 새 오류 1(2.1 p.14 본문과 식 (7)의 $\overline{\mathbf{u}}_2$ 상선이 다르다고 씀 — Claude가 쪽 이미지로 두 곳 모두 상선이 있음을 확인하고 고침). 과잉 정정 0.
- 최종 기계 확인: 원문 인용 32,018개 중 불일치 표시 5개. tex 원본에 이미 있는 U+FFFD 문자 4개(기록과 바이트가 같음)와 행 번호가 인용 바로 뒤에 오지 않은 문장 1개로, 검사기 오판이다.

## FUNWAVE 대조·흐름·노트 반영 (2026-10-17~18)

- 외부 원문: 위키 원자료 두 저장소는 커밋 1개짜리 얕은 사본이다. 공개 저장소 github.com/fengyanshi/FUNWAVE-TVD(554커밋, 2016-03-02 `cab9425` ~ 2025-01-24 `b4c322e`, 태그 v3.0 `b569dfe` 2017-04-18 ~ Version_3.6 `e8c9474` 2021-05-19)와 github.com/dryuanye/FUNWAVE-GPU(3커밋, 2019-11-26 `7f892ba`)를 `extract/FUNWAVE/external/{tvd,gpu}`에 받았다(extract는 커밋하지 않는다). TVD HEAD의 src는 원자료와 같다. GPU 원자료는 3파일에 커밋하지 않은 로컬 수정이 있다. 문서 커밋: 3.0 PDF 마지막 변경 `fef45a7` 2018-02-24, tex `24a88c3` 2016-11-18, 2.1 매뉴얼·code_analysis `b9c035d` 2016-11-03, Intro-TN `80ac086` 2016-11-10.
- 대조 보고서 7종(Codex `gpt-6.1-sol`, 처음부터 git 이력을 근거로 줌): `compare/funwave-{theory-numerics,inputs,examples,v21-manual,v21-examples,aux-docs-build}-vs-code.md`, `compare/funwave-gpu-vs-tvd.md`(GPU 판 대 TVD 판 코드 대조, 문서 없음). 흐름 분석 `flow/FUNWAVE-callflow.md`(TVD·GPU 시작·입력 읽기, 계산 순서, 변수 생산·소비, 문서 대조). mermaid 3개(TVD 전체, TVD 한 시간 단계, GPU 한 시간 단계)는 렌더해 확인했다. 렌더 확인에서 RK 반복 끝 상자 2개의 코드에 없는 조건 `(ISTAGE<3)`을 원문 `DO ISTAGE=1,3`의 `ENDDO`로 고쳤다.
- git 이력 판정(Codex `gpt-6-astra` 6작업): E 116행 모두 유지. A 101행 확정, B→A 6행, 보조 문서·빌드 보고서에서 그 밖 재분류 37행. 기록: `compare/FUNWAVE-git-verify-{E1,E2,E3,AD1,AD2,AD3}.md`.
- 외부 원문(sonnet 웹 조회): E 행 중 비선형 분산 항의 `Beta_2` 배수(`init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`, 주석 `! kennedy equation`, 최초 커밋 `cab9425:init.F:497`부터 있음)에서 나온 행들은 원인이 하나다. Kennedy et al. ICCE 2000 학회판과 2.1 매뉴얼에 이 배수가 없고, GitHub 이슈 #46(2021-04-01)이 같은 질문을 했으며 조회 시점에 답이 없다. E(강함) 유지. Wave Motion 2001·Ocean Modelling 2012 본문은 유료라 학회판과 매뉴얼로 판정했다. 기록: `compare/FUNWAVE-external-sources.md`.
- 결론 표본(sonnet 30행): OK 28·부분 1·틀림 1(FN1-644 보고서에 git 판정 미반영, FN1-768 근거 없는 부연). 결론 전수 재검증(Codex `gpt-6-astra` 12작업): 1,741행, 정정 668·보완 1,298·분류 변경 259(작업 요약 줄 합계). 기록: `compare/FUNWAVE-conclusion-sample.md`, 보고서별 "## 전수 검증 기록 (10-18, …)".
- 최종 결론(차이 결론 절 1,741행, 결론 열에서 Claude가 셈, 보고서 끝 "## 최종 집계"): 일치 66·A 186·B 316·C 467·D 44·E 122·F 289·H 251. G·X 0.
- 노트 반영(Codex `gpt-6.1-sol`): 보고서별 8작업이 A–F 1,424행마다 담당 노트 하나를 정했다(`assign/FUNWAVE-assign-*.tsv`). 9작업이 반영했다(`assign/FUNWAVE-note-job-*.tsv`, `flow/FUNWAVE-notes-apply-{1..9}.md`). 기존 노트 16개를 고쳤고 새 노트 3개(`source-analysis/funwave-gpu-vs-tvd-differences.md`, `manual-notes/funwave-aux-docs-build-differences.md`, `manual-notes/funwave-v21-manual-differences.md`)를 만들었다. 흐름도 3개는 `source-analysis/funwave-source-map.md`에, 코드 결함 후보 E 122행 표는 `models/FUNWAVE/README.md`에 넣었다. 행 ID 대조로 1,424행이 모두 배정 노트의 표에 한 번 이상 있고 분류가 배정표와 같음을 확인했다. 저장소 루트 README는 바뀌지 않았다.
- 추가 줄 전수 대조(Codex `gpt-6-astra` 10작업): 2,420줄(기존 노트 + 줄 2,254, 새 노트 166), 정정 181·보완 59(노트 태그 수).
- 기계 확인: 바뀐 노트 19개의 `경로:줄` 인용 5,031개 중 불일치 표시 217개다. 과거 커밋 인용(`334bb51:src/main.F:151`, `7b93138:src/init.F:488`, `cab9425:init.F:497` 등은 Claude가 해당 커밋을 열어 원문과 같음을 확인), 인용 사이 문장 조각, TVD·GPU 같은 이름 파일이 섞인 검사 오판이다. 전수 대조 작업이 후보를 하나씩 판정했다. `tools/validate-all.sh` 통과(경고 1건은 기존 ROMS 노트).
- sonnet 표본 30줄(표 22·본문 8): OK 28·부분 2. FroudeCap=10 중첩 예제 서술은 Claude가 2.1 p.71–72에서 확인(노트 맞음). 노트가 반영 전 노트 줄을 현재 줄처럼 인용한 유형(`funwave-user-manual-full.md:232`)은 Claude가 전수 기계 대조로 66곳(64줄)을 찾아 `HASH:models/FUNWAVE/<노트>:줄`(반영 전 노트 줄)로 고쳤다(`[10-18 표본 정정]`). 기록: `compare/FUNWAVE-notes-sample.md`. 고친 뒤 `tools/validate-all.sh` 통과.
- Claude 정정: 외부 원문 기록에 `Beta_2` 줄이 `b9c035d`부터 있다고 쓴 것을 최초 커밋 `cab9425`로 고쳤다(`b9c035d`는 파일을 `src/`로 옮긴 커밋). 노트와 보고서는 이미 `cab9425`로 적혀 있었다.

## 노트 반영분 전수 대조와 차이 결론 (2026-10-12)

사용자 지시(10-12): 확인하지 않은 것을 한계로 남기지 말고 해결한 뒤 다음 모델로 간다. 모델 실행은 위키 범위가 아니므로 한계로 적지 않는다.

- 노트 반영분 전수 대조(Codex `gpt-6-astra`): 노트 반영 커밋이 넣은 줄을 모두 원문과 대조했다. ADCIRC(`8a943078`) 정정 40·보완 264·이상 없음 1,423, XBeach·SFINCS(`1da8d89`·`d89cd8b`·`c41c3037`·`667408d`) 정정 30·보완 83·이상 없음 437, EFDC(`f3c6397a`) 정정 19·보완 60·이상 없음 568. 기록: `flow/*-notes-verify*.md`. sonnet 표본 48줄(ADCIRC 24, 나머지 24) 모두 맞음, 표본에서 나온 경미한 조건 누락 2건은 원문 확인 후 보완.
- 차이 결론(Codex `gpt-6-astra`): 대조 보고서 10개의 §5 "차이 결론"에 차이 행마다 A 판 차이·B 문서 오기·C 문서 누락·D 문서에만·E 코드 결함 후보·F 표기 차이·H 코드 대조 대상 아님(적용 사례·성능 주장)을 근거와 함께 달았다. 처음 G(근거 부족) 171행은 재판정 → 기준 정리(H 신설, 지원 범위 질문은 코드 동작으로 판정) → 외부 원문(sonnet 웹 판독, `compare/external-results-*.md`: GitHub 태그 소스, Fofonoff 1985 Table 3, Garcia & Gordon 1992, van Rijn 1984 Part I, Hamill & Kee 2016 저자 원고, SnapWave 프리프린트, GMD 2025 등)으로 0행이 됐다. 2차 문헌으로 판정한 행(Lee & Cheung 1990, Chapra 1997)은 노트에 "2차 문헌 기준"으로 표시했다.
- 코드 결함 후보 표본(sonnet 24행): 23행 E 유지, 1행(ADCIRC ISLIP 3D 마찰)은 `vsmy.F:942` 의도 변경 주석으로 C로 바꿈. 강한 후보 예: ADCIRC EOS-80 계수 부호(`vsmy.F:3964` `c24=0.00000082467d0`, Fofonoff 1985 Table 3은 −8.2467E-7; Claude 원문 확인).
- 노트 반영: 각 모델 노트의 문서·코드 차이 표에 결론을 붙이고 대표 노트에 "코드 결함 후보 (정적 판독)" 절을 만들었다(`flow/*-conclusions-apply.md`, `flow/*-external-apply.md`).
- 기계 확인: 바뀐 노트 82개의 인용을 `citecheck_path.py`·`citecheck.py`로 대조. 원문을 줄여 옮긴 기존 인용 6곳을 원문 그대로 고쳤다. 남은 경고는 검사기 오판(표 안 `\|`, 탭 표기, 원문과 글자 단위로 같은 문헌 인용)이다. `tools/validate-canonical-hygiene.py`의 홈 경로 규칙이 Perl `=~/`를 경로로 잡아 `=` 뒤를 제외했다(시험 33개 통과).

## 다음에 이어서 할 일

1. ~~매뉴얼과 코드 판독 기록 대조~~ — 10-03 완료(`compare/XBeach-manual-vs-code.md`, 노트 반영 `1da8d89`).
2. ~~XBeach 파일 간 계산 흐름 분석~~ — 10-07 완료(`flow/XBeach-callflow.md`, 노트 반영 `d89cd8b`). 판독 기록 검색은 `wiki_search` `path_class="records"`(`ce7b3ae`).
3. 다른 10개 모델(SFINCS·EFDC·ADCIRC 완료, ShorelineS 10-12 완료, SWAN 10-13 완료, ROMS 10-14 완료, SWASH 10-15 완료, FUNWAVE 10-18 완료, 나머지 4개 미착수 — 순서 LISFLOOD-FP·Delft3D·Celeris·CADMAS-SURF): 같은 방식(고정 목록 → 1행/1쪽 판독 → 기계 확인 → 다른 모델 검증).
