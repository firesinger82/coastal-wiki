# LISFLOOD-FP 노트 전수 검증 — 1번째 몫

- 작업일: 2026-10-21.
- 대상 노트: `models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary-differences.md`.
- 시작 시 새 파일의 전체 줄 수는 304줄이다.
- 이번 배정은 시작 시 1–152줄의 152줄이다.
- 첫 줄은 frontmatter 시작 구분자이다.
- 마지막 줄은 `cpu-gpu-swe:LG1-143` 표 행이다.
- 줄 번호는 시작 시 기준으로 기록한다.
- 수정 직전에 해당 줄을 다시 읽는다.
- 기계 확인 불일치 후보: 사용자 지정 후보 없음.
- 상태: 담당 1–152줄 대조 완료.

## 대상 노트 대조 결과

대상은 [lisflood-fp-io-boundary-differences.md](../../../models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary-differences.md)의 시작 시 1–152줄이다.
이번 작업은 줄을 삽입하거나 삭제하지 않았다.
정정 수와 보완 수는 변경한 원래 줄을 한 번씩 세었다.

| 대조 범위 | 대조 줄 수 | 정정 줄 수 | 보완 줄 수 |
|---|---:|---:|---:|
| 1–16: frontmatter | 16 | 0 | 0 |
| 17–60: 제목·안내·판 정보·표 머리·빈 줄 | 44 | 1 | 1 |
| 61–128: bridge-docx | 68 | 4 | 0 |
| 129–135: build-83 | 7 | 3 | 0 |
| 136–142: callflow | 7 | 0 | 0 |
| 143–151: cpu-gpu-acc-adaptive | 9 | 1 | 0 |
| 152: cpu-gpu-swe | 1 | 0 | 1 |
| 합계 | 152 | 9 | 2 |

표의 92행은 A 15행, B 9행, C 53행, E 15행이다.
E의 근거 강도는 강함 12행과 중간 3행이다.
이 개수는 아래 행별 대조 목록과 대상 노트의 결론 칸을 세었다.
92행의 분류·강도·결론은 [최종 결론 배정표](../assign/LISFLOOD-FP-final-conclusions.tsv)와 각 재검증 행에 부합한다.
[Claude 최종 조정](../compare/LISFLOOD-FP-conclusion-claude-final.md)의 세 행은 이번 1–152줄에 없다.
[외부 출처 최종 절](../compare/LISFLOOD-FP-external-sources.md#claude-확인과-최종-결론-10-21)의 두 행도 이번 구간에 없다.

## 정정·보완 목록

아래 `노트:N`의 노트는 `models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary-differences.md`이다.
접두어 없는 코드 경로는 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/` 아래이다.
`v8.0:`과 `v8.1:`은 각각 `_staging/recovery/extract/LISFLOOD-FP/external/v8.0/LISFLOOD-FP-trunk/`와 `v8.1/LISFLOOD-FP-trunk/` 아래이다.
`v8.2:`는 `_staging/recovery/extract/LISFLOOD-FP/external/v8.2/LISFLOOD-FP/` 아래이다.
docx 쪽 번호는 LibreOffice 변환본 기준이다.

| 위치 | 종류 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| 노트:34 | 보완 | CPU·GPU의 M 정의만 있음 → bridge-docx의 M을 `iterateq.cpp:261`의 `.mass` 출력문으로 추가했다. | `lisflood-bridge-docx-vs-code.md:314–317`은 공통 근거 M을 정의한다. `iterateq.cpp:261`은 `fprintf(Fptr->mass_fp, ...)`의 출력문이다. |
| 노트:57 | 정정 | docx 판 이력 맨 위 `5.9` → `8.0`. 숫자 판 인용 `VersionHistory.h:31–34` → `:16–18`. 릴리스 이름에 `:23`을 붙였다. 근거 없는 8.3 패치 DOI 표기는 배포 README의 8.2 DOI와 8.3 변경 적용 설명으로 바꿨다. 표지 정보에 쪽 번호를 붙였다. | `lf-manual-docx-005.png`의 판 이력 첫 행은 8.0이다. `lf-manual-pdf-001.png`는 6.1.1·2013-11-25이다. `lf-manual-bridge-docx-001.png`는 4.3.6·2008-04-25이다. `VersionHistory.h:16–18`은 8·1·0이다. `:23`은 `LF_Release "8.3"`이다. `../LISFLOOD-FP-8.3-package/README.md:19–24`는 8.2 DOI와 8.3 변경을 명시한다. `LISFLOOD-FP-conclusion-verify-LB1b.md`의 LB1-408도 README에서 8.3 DOI를 도출하지 않는다. |
| 노트:71 / LB1-173 | 정정 | `user manual.pdf p.15·34` → `user manual.pdf p.16·34`. | `lf-manual-pdf-016.png`의 표 5에는 fpfric과 manningfile을 함께 지정하면 manningfile 값을 사용한다고 적혀 있다. `lf-manual-pdf-015.png`에는 해당 두 행이 없다. `lf-manual-pdf-034.png`에는 `-nfp`의 덮어쓰기 설명이 있다. 최종 재검증 행의 인용 쪽 번호 오류도 이미지에 따라 바로잡았다. |
| 노트:74 / LB1-191 | 정정 | 항목 칸과 문서 원문 칸의 `at every save interval (saveint)` → `at each save interval (saveint)`. | `lf-manual-bridge-docx-038.png`의 원문은 `at each save interval (saveint)`이다. `LISFLOOD-FP-conclusion-verify-LB1a.md`의 LB1-191도 인용 보정을 요구한다. `iterateq.cpp:325,339,348`의 저장 조건·호출·다음 저장 시각과 결론은 유지했다. |
| 노트:121 / LB1-375 | 정정 | `cuda/acc_nugrid/S 단면` → `N/S 단면`. | `input.cpp:2338–2343`은 North·South 길이를 y 경계로 제한한다. `util.cpp:242–249`의 North·South 적산은 `x++`를 쓴다. `:251–259`의 East·West 적산은 `y++`를 쓴다. `LISFLOOD-FP-conclusion-verify-LB1b.md`의 LB1-375 결론도 `N/S 단면`이다. |
| 노트:124 / LB1-401 | 정정 | 항목 칸 인용의 시작 백틱 3개·끝 백틱 2개 → 중복 백틱을 제거했다. | `git show bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md`의 142행을 읽었다. 문서 원문 칸과 같은 인용으로 바로잡았다. 인용 내용과 E 결론은 유지했다. |
| 노트:129 / LN1-128 | 정정 | `input.cpp:1488`; `pars.cpp:924` → `v8.0:input.cpp:1488`; `v8.0:pars.cpp:924`. | `v8.0:input.cpp:1488`은 DEM NoData를 `Parptr->nodata_elevation`으로 치환한다. `v8.0:pars.cpp:924`는 `nodata_elevation` 키워드를 읽는다. 현재 `input.cpp:1488`은 `dx_sqrt` 계산이다. 현재 `pars.cpp:924`는 `max_Froude` 분기의 여는 중괄호이다. `preprocess/generateDG2DEM.cpp:44`와 배포 패치 2981–2988행의 기본값 추가도 대조했다. |
| 노트:130 / LN1-129 | 정정 | `input.cpp:1517`; `pars.cpp:987` → `v8.1:input.cpp:1517`; `v8.1:pars.cpp:987`. | `v8.1:input.cpp:1517`은 DEM NoData 치환문이다. `v8.1:pars.cpp:987`은 `nodata_elevation` 키워드를 읽는다. 현재 `pars.cpp:987`은 다른 키워드 분기의 `return`이다. `preprocess/generateDG2start.cpp:44`와 배포 패치 2992–2999행의 기본값 추가도 대조했다. |
| 노트:134 / LN1-193 | 정정 | `-version 외의 일반 실행` → `-version·-compare_results 특수 실행을 제외한 일반 실행`. | `lisflood.cpp:289–319`에서 두 특수 경로는 설정 파일을 읽기 전에 끝난다. `pars.cpp:38–51`은 일반 실행의 마지막 parfile 인수 검사이다. `LISFLOOD-FP-conclusion-verify-LN1.md`의 LN1-193 결론은 두 예외를 모두 명시한다. |
| 노트:146 / LG2-077 | 정정 | `dynamicRain.update_H` → `dynamic_rain.update_H`. | `iterateq.cpp:157`의 원문은 `dynamic_rain.update_H(Parptr, Solverptr, Arrptr);`이다. `:146`의 FloodplainQ 이후 호출 순서와 E 강함 판정은 유지했다. |
| 노트:152 / LG1-143 | 보완 | CPU의 dx·dy 분리 사용 설명에 직접 인용 없음 → `swe/fv1.cpp:441–442`; `swe/dg2.cpp:819`를 붙였다. | 두 함수의 수심 갱신식은 `((H_e - H_w)/Parptr->dx + (H_n - H_s)/Parptr->dy)`를 사용한다. `cuda/io.cpp:18,70`과 `metal/fv1/metal_fv1_simulate.mm:278–279`도 대조했다. |

## 1–60줄 대조

| 원래 줄 | 대조 대상 | 판정 |
|---|---|---|
| 1–16 | frontmatter의 모델·구성요소·자체 출처·반영 검증 상태·날짜·작성자·관련 노트·소스 범위 | 노트 내용과 [반영 기록 1](LISFLOOD-FP-notes-apply-1.md)에 부합한다. related의 파일은 존재한다. |
| 17–33 | 제목·본문 연결·배정표·최종 근거 연결·비교 열의 의미·기준 커밋·코드 경로·구판 접두어·U/N 정의 | 배정표와 보고서의 정의에 부합한다. 빈 줄을 포함해 대조했다. |
| 34 | M 약칭 | CPU·GPU의 M과 bridge의 M을 구분하도록 보완했다. |
| 35–46 | 보고서 약칭과 링크 | 연결된 보고서 9개가 존재한다. 각 약칭은 배정표의 보고서 열에 대응한다. |
| 47–53 | A–F 분류 안내 | 최종 결론 배정표의 분류 의미에 부합한다. |
| 54–60 | 절 제목·판 정보·표 머리·구분자·빈 줄 | 57줄의 판 정보와 근거 위치를 정정했다. 표는 6개 열이다. |

## 61–152줄 행별 대조

각 행의 문서 원문·코드 원문·확인한 원문을 해당 파일에서 대조했다.
인용문 없이 경로와 줄만 적힌 근거도 열어 대조했다.
문서의 숫자·단위·표는 쪽 이미지로 판정했다.
기존 노트 인용은 `bf804e23`의 해당 줄을 읽어 대조했다.
아래 표의 원문 위치는 대조한 근거의 대표 위치이다.
전체 인용 범위는 대상 노트의 같은 행에 있다.
“일치”는 해당 원문과 최종 결론에 부합한다는 뜻이다.

재검증 약칭은 [LB1a](../compare/LISFLOOD-FP-conclusion-verify-LB1a.md), [LB1b](../compare/LISFLOOD-FP-conclusion-verify-LB1b.md), [LN1](../compare/LISFLOOD-FP-conclusion-verify-LN1.md), [RF](../compare/LISFLOOD-FP-conclusion-verify-RF.md), [LG2](../compare/LISFLOOD-FP-conclusion-verify-LG2.md), [LG1](../compare/LISFLOOD-FP-conclusion-verify-LG1.md)이다.

| 원래 줄 | 행 ID | 최종 분류·재검증 | 원문 대표 위치 | 결과 |
|---:|---|---|---|---|
| 61 | bridge-docx:LB1-051 | A 판 차이 / LB1a | bridge p.1·21; `pars.cpp:56`; `lisflood.h:101`; `pars.cpp:54–58,75–77` | 일치 |
| 62 | bridge-docx:LB1-055 | A 판 차이 / LB1a | bridge p.1·21; `pars.cpp:170–171`; `lisflood.cpp:332`; `v8.0:pars.cpp:170–171` | 일치 |
| 63 | bridge-docx:LB1-084 | E 코드 결함 후보(중간) / LB1a | bridge p.22·38; `pars.cpp:438–441`; `lisflood.h:603`; `v8.0:pars.cpp:427–430` | 일치 |
| 64 | bridge-docx:LB1-103 | B 문서 오기 / LB1a | bridge p.21·23–24; `lisflood.cpp:337`; `output.cpp:803`; `lisflood.cpp:332–337` | 일치 |
| 65 | bridge-docx:LB1-104 | B 문서 오기 / LB1a | bridge p.21·27·33; `input.cpp:1869`; `input.cpp:1869–1872,1898–1901,1993–1995` | 일치 |
| 66 | bridge-docx:LB1-123 | A 판 차이 / LB1a | bridge p.1·6·27; `boundary.cpp:189–196`; `boundary.cpp:189–196,279–287`; `VersionHistory.h:200–203` | 일치 |
| 67 | bridge-docx:LB1-126 | B 문서 오기 / LB1a | bridge p.28; `input.cpp:1923–1928`; `input.cpp:1920–1932`; `VersionHistory.h:453–454` | 일치 |
| 68 | bridge-docx:LB1-127 | E 코드 결함 후보(강함) / LB1a | bridge p.28; `input.cpp:2065–2067`; `input.cpp:1953–1980,2019–2058,2065–2117`; `boundary.cpp:279–287,1392–1393,1422–1429` | 일치 |
| 69 | bridge-docx:LB1-134 | C 문서 누락 / LB1a | bridge p.33; `infevap.cpp:64–69`; `infevap.cpp:51–79` | 일치 |
| 70 | bridge-docx:LB1-168 | A 판 차이 / LB1a | bridge p.1·35; `pars.cpp:895–898`; `output.cpp:179–182`; `pars.cpp:895–900` | 일치 |
| 71 | bridge-docx:LB1-173 | A 판 차이 / LB1a | PDF p.16·34 쪽 이미지; `pars.cpp:176–180`; `input.cpp:914–934` | 정정 후 일치 |
| 72 | bridge-docx:LB1-176 | A 판 차이 / LB1a | bridge p.1·35–36; `pars.cpp:563`; `pars.cpp:45–48,91–103,563–567,1027–1036`; `v8.0:pars.cpp:552–557` | 일치 |
| 73 | bridge-docx:LB1-187 | B 문서 오기 / LB1a | bridge p.6·37; `chkpnt.cpp:98–100`; `VersionHistory.h:295–298`; `chkpnt.cpp:93–110` | 일치 |
| 74 | bridge-docx:LB1-191 | B 문서 오기 / LB1a | bridge p.4·38 쪽 이미지; `iterateq.cpp:325,339,348` | 정정 후 일치 |
| 75 | bridge-docx:LB1-192 | B 문서 오기 / LB1a | bridge p.37; `iterateq.cpp:261`; `lisflood.cpp:603` | 일치 |
| 76 | bridge-docx:LB1-194 | A 판 차이 / LB1a | bridge p.1·37; `fp_flow.cpp:65`; `iterateq.cpp:143–146,261`; `v8.0:iterateq.cpp:261` | 일치 |
| 77 | bridge-docx:LB1-197 | A 판 차이 / LB1a | bridge p.1·37; `iterateq.cpp:254–257`; `input.cpp:1484–1489`; `iterateq.cpp:235–261` | 일치 |
| 78 | bridge-docx:LB1-204 | A 판 차이 / LB1a | bridge p.1·37; `infevap.cpp:39`; `infevap.cpp:24–39`; `iterateq.cpp:261` | 일치 |
| 79 | bridge-docx:LB1-206 | A 판 차이 / LB1a | bridge p.1·22·37; `iterateq.cpp:360`; `VersionHistory.h:192–196`; `iterateq.cpp:354–360,380–390` | 일치 |
| 80 | bridge-docx:LB1-208 | A 판 차이 / LB1a | bridge p.1·37–38; `lisflood.cpp:114`; `iterateq.cpp:344`; `VersionHistory.h:213,377–378` | 일치 |
| 81 | bridge-docx:LB1-250 | B 문서 오기 / LB1b | bridge p.42; `output.cpp:157–165`; `output.cpp:150–165`; `VersionHistory.h:102–106,428–430` | 일치 |
| 82 | bridge-docx:LB1-255 | B 문서 오기 / LB1b | bridge p.28·42·43; `input.cpp:1490`; `input.cpp:1486–1490` | 일치 |
| 83 | bridge-docx:LB1-266 | C 문서 누락 / LB1b | bridge p.21–24 표 5; `pars.cpp:151`; `pars.cpp:153`; `pars.cpp:154` | 일치 |
| 84 | bridge-docx:LB1-267 | C 문서 누락 / LB1b | bridge p.21–24 표 5; `pars.cpp:158`; `pars.cpp:160` | 일치 |
| 85 | bridge-docx:LB1-268 | C 문서 누락 / LB1b | bridge p.21–24 표 5; `pars.cpp:187`; `pars.cpp:189` | 일치 |
| 86 | bridge-docx:LB1-269 | C 문서 누락 / LB1b | bridge p.21–24 표 5; `pars.cpp:232` | 일치 |
| 87 | bridge-docx:LB1-274 | C 문서 누락 / LB1b | bridge p.21–24 표 5; `pars.cpp:294`; `pars.cpp:296` | 일치 |
| 88 | bridge-docx:LB1-276 | C 문서 누락 / LB1b | bridge p.21–24 표 5; `pars.cpp:333`; `pars.cpp:335` | 일치 |
| 89 | bridge-docx:LB1-277 | C 문서 누락 / LB1b | bridge p.21–24 표 5; `pars.cpp:344`; `pars.cpp:346`; `pars.cpp:347` | 일치 |
| 90 | bridge-docx:LB1-278 | C 문서 누락 / LB1b | bridge p.21–24 표 5; `pars.cpp:350`; `pars.cpp:352` | 일치 |
| 91 | bridge-docx:LB1-279 | C 문서 누락 / LB1b | bridge p.21–24 표 5; `pars.cpp:355`; `pars.cpp:357`; `pars.cpp:358` | 일치 |
| 92 | bridge-docx:LB1-280 | C 문서 누락 / LB1b | bridge p.21–24 표 5; `pars.cpp:379` | 일치 |
| 93 | bridge-docx:LB1-281 | C 문서 누락 / LB1b | bridge p.21–24 표 5; `pars.cpp:384` | 일치 |
| 94 | bridge-docx:LB1-282 | C 문서 누락 / LB1b | bridge p.21–24 표 5; `pars.cpp:390`; `pars.cpp:392` | 일치 |
| 95 | bridge-docx:LB1-283 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:397` | 일치 |
| 96 | bridge-docx:LB1-286 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:460`; `pars.cpp:462` | 일치 |
| 97 | bridge-docx:LB1-287 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:465`; `pars.cpp:467` | 일치 |
| 98 | bridge-docx:LB1-288 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:470`; `pars.cpp:472` | 일치 |
| 99 | bridge-docx:LB1-289 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:492`; `pars.cpp:494`; `pars.cpp:495` | 일치 |
| 100 | bridge-docx:LB1-290 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:506`; `pars.cpp:508` | 일치 |
| 101 | bridge-docx:LB1-291 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:513`; `pars.cpp:515` | 일치 |
| 102 | bridge-docx:LB1-292 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:519`; `pars.cpp:521` | 일치 |
| 103 | bridge-docx:LB1-293 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:527`; `pars.cpp:529`; `pars.cpp:530` | 일치 |
| 104 | bridge-docx:LB1-294 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:535`; `pars.cpp:537`; `pars.cpp:538` | 일치 |
| 105 | bridge-docx:LB1-295 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:543`; `pars.cpp:545` | 일치 |
| 106 | bridge-docx:LB1-296 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:550`; `pars.cpp:552` | 일치 |
| 107 | bridge-docx:LB1-326 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:799`; `pars.cpp:801` | 일치 |
| 108 | bridge-docx:LB1-338 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:880`; `pars.cpp:882` | 일치 |
| 109 | bridge-docx:LB1-339 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:907`; `pars.cpp:912` | 일치 |
| 110 | bridge-docx:LB1-340 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:915`; `pars.cpp:920` | 일치 |
| 111 | bridge-docx:LB1-342 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:934`; `pars.cpp:936`; `pars.cpp:937` | 일치 |
| 112 | bridge-docx:LB1-343 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:941`; `pars.cpp:943`; `pars.cpp:944` | 일치 |
| 113 | bridge-docx:LB1-350 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:990` | 일치 |
| 114 | bridge-docx:LB1-351 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:996`; `pars.cpp:998`; `pars.cpp:999–1002` | 일치 |
| 115 | bridge-docx:LB1-352 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:1006` | 일치 |
| 116 | bridge-docx:LB1-353 | C 문서 누락 / LB1b | bridge p.21–24 표 5·p.35 표 7; `pars.cpp:1012`; `pars.cpp:1014` | 일치 |
| 117 | bridge-docx:LB1-366 | C 문서 누락 / LB1b | bridge p.21의 알 수 없는 항목 무시 규칙; `pars.cpp:1114–1118` | 일치 |
| 118 | bridge-docx:LB1-367 | C 문서 누락 / LB1b | bridge p.27–28의 시계열 형식; `input.cpp:1905–1909` | 일치 |
| 119 | bridge-docx:LB1-368 | C 문서 누락 / LB1b | bridge p.27–28의 시계열 형식; `input.cpp:1920–1922`; `VersionHistory.h:107` | 일치 |
| 120 | bridge-docx:LB1-373 | E 코드 결함 후보(강함) / LB1b | `infevap.cpp:56–57`; `infevap.cpp:56–79,105–118`; `iterateq.cpp:132–155` | 일치 |
| 121 | bridge-docx:LB1-375 | E 코드 결함 후보(강함) / LB1b | `input.cpp:2338–2343`; `util.cpp:242–259` | 정정 후 일치 |
| 122 | bridge-docx:LB1-376 | E 코드 결함 후보(강함) / LB1b | bridge p.37–38; `iterateq.cpp:452`; `lisflood.cpp:810`; `chkpnt.cpp:251` | 일치 |
| 123 | bridge-docx:LB1-400 | C 문서 누락 / LB1b | `input.cpp:1978`; `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:97`; `input.cpp:1978–1980,2020–2059,2065–2116` | 일치 |
| 124 | bridge-docx:LB1-401 | E 코드 결함 후보(강함) / LB1b | bf804e23의 IO 노트 142행; `input.cpp:2126–2139`; `infevap.cpp:56–79` | 정정 후 일치 |
| 125 | bridge-docx:LB1-402 | A 판 차이 / LB1b | `pars.cpp:1080–1086`; `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:61`; `../LISFLOOD-FP-8.3-package/README.md:35` | 일치 |
| 126 | bridge-docx:LB1-417 | C 문서 누락 / LB1b | bridge p.27 표 6; `input.cpp:1646–1651`; `input.cpp:1646–1651,1777–1782` | 일치 |
| 127 | bridge-docx:LB1-418 | C 문서 누락 / LB1b | bridge p.38; `output.cpp:338`; `output.cpp:336–338,353,366` | 일치 |
| 128 | bridge-docx:LB1-423 | A 판 차이 / LB1b | bridge p.1·37; `VersionHistory.h:236–237`; `iterateq.cpp:261`; `VersionHistory.h:236–238` | 일치 |
| 129 | build-83:LN1-128 | E 코드 결함 후보(강함) / LN1 | `v8.0:input.cpp:1488`; `v8.0:pars.cpp:924`; `preprocess/generateDG2DEM.cpp:43–73` | 정정 후 일치 |
| 130 | build-83:LN1-129 | E 코드 결함 후보(강함) / LN1 | `v8.1:input.cpp:1517`; `v8.1:pars.cpp:987`; `preprocess/generateDG2start.cpp:43–73` | 정정 후 일치 |
| 131 | build-83:LN1-183 | C 문서 누락 / LN1 | `pars.cpp:1080–1086`; `pars.cpp:965–970,1080–1086` | 일치 |
| 132 | build-83:LN1-184 | C 문서 누락 / LN1 | `pars.cpp:923`; `pars.cpp:926–930`; `lisflood.cpp:144` | 일치 |
| 133 | build-83:LN1-192 | C 문서 누락 / LN1 | `pars.cpp:965–970`; `pars.cpp:582–589`; `lisflood.cpp:773–788` | 일치 |
| 134 | build-83:LN1-193 | C 문서 누락 / LN1 | `pars.cpp:38–51`; `lisflood.cpp:288–320` | 정정 후 일치 |
| 135 | build-83:LN1-241 | A 판 차이 / LN1 | `v8.2:pars.cpp:1079`; `pars.cpp:1080`; `../LISFLOOD-FP-8.3-package/lisflood-8.2-to-8.3.patch:2969–2977` | 일치 |
| 136 | callflow:RF-004 | A 판 차이 / RF | Word p.39; `v8.0:pars.cpp:574`; `pars.cpp:585`; `pars.cpp:975–978` | 일치 |
| 137 | callflow:RF-005 | E 코드 결함 후보(중간) / RF | PDF p.16; `pars.cpp:317`; `pars.cpp:305,314`; `pars.cpp:300–323,1041–1087` | 일치 |
| 138 | callflow:RF-019 | B 문서 오기 / RF | `pars.cpp:584`; `pars.cpp:632`; `lisflood.cpp:419–457,773–805` | 일치 |
| 139 | callflow:RF-020 | C 문서 누락 / RF | `pars.cpp:1053`; `pars.cpp:1058–1078`; `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:60–61` | 일치 |
| 140 | callflow:RF-021 | C 문서 누락 / RF | PDF p.36; `lisflood.cpp:457`; `chkpnt.cpp:248–254`; `lisflood2/sgm_fast.cpp:4601–4611` | 일치 |
| 141 | callflow:RF-026 | E 코드 결함 후보(강함) / RF | `iterateq.cpp:452`; `iterateq.cpp:469`; `chkpnt.cpp:140,251` | 일치 |
| 142 | callflow:RF-028 | C 문서 누락 / RF | PDF p.32 쪽 이미지; `iterateq.cpp:153–157`; `cuda/fv1/cuda_fv1_simulate.cu:151–153`; `cuda/fv2/cuda_fv2_solver.cu:754–759` | 일치 |
| 143 | cpu-gpu-acc-adaptive:LG2-074 | E 코드 결함 후보(강함) / LG2 | `rain/Rainfall_uniform.h:74`; `rain/Rainfall_uniform.h:90`; `cuda/acc_nugrid/RainfallUniform.h:79` | 일치 |
| 144 | cpu-gpu-acc-adaptive:LG2-075 | E 코드 결함 후보(중간) / LG2 | `rain/rain.tpp:118`; `rain/rain.tpp:120`; `cuda/acc_nugrid/rain.cu:33` | 일치 |
| 145 | cpu-gpu-acc-adaptive:LG2-076 | E 코드 결함 후보(강함) / LG2 | `rain/rain_stub.tpp:5-11`; `rain/rain.h:95`; `rain/rain.h:114` | 일치 |
| 146 | cpu-gpu-acc-adaptive:LG2-077 | E 코드 결함 후보(강함) / LG2 | `iterateq.cpp:146,152–157`; `cuda/acc/cuda_acc_simulate.cu:181–230` | 정정 후 일치 |
| 147 | cpu-gpu-acc-adaptive:LG2-078 | C 문서 누락 / LG2 | `cuda/cuda_rain.cu:110`; `cuda/acc_nugrid/rain_uniform.cu:41`; `rain/rain.tpp:178–184` | 일치 |
| 148 | cpu-gpu-acc-adaptive:LG2-079 | C 문서 누락 / LG2 | `rain/rain.tpp:207-230`; `rain/rain.tpp:227`; `rain/rain.tpp:199–232` | 일치 |
| 149 | cpu-gpu-acc-adaptive:LG2-090 | C 문서 누락 / LG2 | `cuda/acc_nugrid/read_chkpnt.cu:194-195`; `cuda/acc_nugrid/write_chkpnt.cu:50–87`; `cuda/acc_nugrid/read_chkpnt.cu:194–200` | 일치 |
| 150 | cpu-gpu-acc-adaptive:LG2-095 | E 코드 결함 후보(강함) / LG2 | `cuda/acc_nugrid/rain.cu:30-31`; `lisflood2/file_tool.cpp:353–370`; `rain/rain.tpp:25–29` | 일치 |
| 151 | cpu-gpu-acc-adaptive:LG2-096 | C 문서 누락 / LG2 | `cuda/acc_nugrid/rain_uniform.cu:33-37`; `cuda/acc_nugrid/rain_uniform.cu:39`; `cuda/acc/cuda_acc_solver.cu:165` | 일치 |
| 152 | cpu-gpu-swe:LG1-143 | C 문서 누락 / LG1 | `swe/fv1.cpp:441–442`; `swe/dg2.cpp:819`; `cuda/io.cpp:11–19,65–75` | 보완 후 일치 |

## 문서·조건·형식 확인

- 쪽 이미지 파일명은 사용자가 지정한 `lfpages/`의 `lf-manual-{pdf,docx,bridge-docx}-NNN.png` 형식이다.
- bridge-docx는 p.1·4·6·21–24·27–28·33·35–38·42–43을 대조했다.
- PDF는 p.1·15–16·22·27·32·34·36–37을 대조했다.
- docx는 p.5·20·37·39를 대조했다.
- A 행의 구판 범위와 현재 코드의 판 구분은 최종 재검증 결론을 유지했다.
- LN1-128·LN1-129의 `8.2 결함, 8.3에서 고침` 표시는 유지했다.
- LN1-128·LN1-129는 v8.2 소스와 현재 소스 및 8.3 배포 패치의 기본값 추가를 대조했다.
- RF-005의 검사 도달 불가 설명은 유지했다.
- RF-005의 강도는 최종 재검증에 따라 중간이다.
- `CUDA`·`METAL_ENABLED`·`_NETCDF`·`_CALCULATE_Q_MODE` 조건은 인용한 코드와 대조했다.
- 기존 노트 인용 행은 각 보고서의 노트 수정안과 대조했다.
- callflow 행은 실행 흐름 보고서의 §6 및 최종 재검증과 대조했다.
- 담당 구간에는 mermaid 블록이 없다.
- 담당 구간의 상대 링크는 105개이다.
- 상대 링크 105개의 대상 파일은 모두 존재한다.
- 담당 구간에는 금지된 절대 경로·홈 약식 경로·위키 링크 표기가 없다.
- 담당 구간에는 작업 미완료를 뜻하는 한계 문장이 없다.
- LG1-143의 “이 검사에서 확인하지 않는다”는 코드의 기하 검사 범위를 설명한다.
- LG1-143의 해당 문장은 `cuda/io.cpp:65–75`와 일치하므로 유지했다.
- 모든 변경 줄에 지정된 정정 또는 보완 표지를 붙였다.
- 표 행의 표지는 결론 문장 칸 끝에 붙였다.
- 대상 구간은 시작 시 152줄과 대조해 변경한 11줄만 달라졌다.

## 기계 확인 후보 판정

- 사용자 지정 불일치 후보: 없음.
- 추가 분류 대조: A–E 이름의 축약·괄호 표기를 정규화한 뒤 92행의 분류와 E 강도 및 근거 파일이 모두 일치했다.
- 추가 결론 대조: LN1-128·LN1-129의 8.3 수정 표시는 사용자 지정 규칙에 맞는 보강 문장이다.
- 추가 결론 대조: LN1-184의 전처리 매크로 코드 서식은 내용 차이가 아니다.
- 추가 문구 검사: LG1-143은 코드가 생략한 검사에 대한 설명이므로 작업 한계 문장으로 판정하지 않았다.

## 완료

- 담당한 1–152줄의 대조를 완료했다.
- 미해결 항목: 없음.
