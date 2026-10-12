# ShorelineS 노트의 추가 줄 전수 검증 — 2026-10-12

이 기록은 AI가 원문과 노트의 추가 줄을 대조한 결과이다.
백틱 안의 발췌문은 원문이다.
전·후 표시는 이번에 바꾼 구절을 기준으로 한다.
검증 범위는 각 대상 파일의 `git diff -U0 HEAD -- <노트>`에서 얻은 모든 `+` 줄이다.
빈 줄과 표의 구분 줄도 대조 수에 포함했다.
노트의 줄 번호는 이번 정정 후 파일을 기준으로 한다.
이번 작업은 한 줄을 한 줄로 교체했으므로 착수 시 줄 번호와 정정 후 줄 번호가 같다.

| 노트 | 대조한 + 줄 | 빈 줄 | 정정 줄 | 보완 줄 |
|---|---:|---:|---:|---:|
| [기술 매뉴얼](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md) | 318 | 35 | 9 | 11 |
| [FAQ](../../../models/ShorelineS/manual-notes/shorelines-faq-operational.md) | 64 | 14 | 1 | 1 |
| [2020 논문](../../../models/ShorelineS/manual-notes/shorelines-roelvink2020-frontiers.md) | 80 | 8 | 2 | 3 |
| [README](../../../models/ShorelineS/README.md) | 26 | 6 | 1 | 3 |
| 합계 | 488 | 63 | 13 | 18 |

정정·보완 수는 이번에 바꾼 고유 줄 수이다.
내용 정정과 인용 추가가 함께 있는 줄은 정정으로 한 번 센다.
수정 후에도 네 파일의 추가 줄 집합은 착수 시의 488줄과 같다.

## 대조 범위와 판정

| 노트 | 대조한 + 줄 번호 |
|---|---|
| 기술 매뉴얼 | 7–8, 24, 28, 60–62, 66–72, 76–85, 98–100, 102–104, 108, 113–117, 129–131, 140–141, 145–147, 150–154, 156, 158–160, 165–169, 173–179, 183–185, 187, 191, 199, 217, 235–236, 239–240, 243, 249, 262–501 |
| FAQ | 7–8, 29–32, 45, 49, 56–111 |
| 2020 논문 | 7–8, 21, 25, 28, 32–33, 35, 37–38, 40, 42, 48–115 |
| README | 1–5, 10, 18, 21, 26, 28, 30–32, 45, 49–60 |

빈 줄을 제외한 425줄의 문장·수식·인용·링크를 확인했다.
현재 코드 인용은 Latin-1을 UTF-8로 변환한 원문과 대조했다.
과거 코드 인용은 해당 커밋의 `git show HASH:path` 결과와 대조했다.
코드의 들여쓰기와 줄 끝 공백은 인용 대조에서 제외했다.
CRLF의 CR과 Markdown 표의 `\|` 이스케이프는 대조할 때 정규화했다.
PDF의 수식과 그림 표기는 쪽 이미지로 대조했다.
PDF의 본문·목록·기본값은 해당 쪽의 이미지 또는 `pdftotext -layout` 결과로 대조했다.
외부 문헌 판정은 사용자가 지정한 `sl-external-results.md`와 R1·R2의 최종 외부 원문 판정에 대조했다.
결론 분류와 문장의 기준은 [R1 이론 대조](../compare/ShorelineS-theory-vs-code.md#5-차이-결론), [R2 입력 대조](../compare/ShorelineS-inputs-vs-code.md#5-차이-결론), [R3 호출 흐름](ShorelineS-callflow.md#8-차이-결론)의 최종 표이다.

| 노트 | 정정 후 코드 원문 인용 수 | 최종 보고서와 대조한 행 ID 수 | 상대 링크 수 |
|---|---:|---:|---:|
| 기술 매뉴얼 | 1135 | 208 | 24 |
| FAQ | 112 | 27 | 4 |
| 2020 논문 | 137 | 49 | 7 |
| README | 24 | 3 | 20 |
| 합계 | 1408 | 287 | 55 |

코드 인용 수는 파일·줄 참조 바로 뒤에 붙은 백틱 원문을 기준으로 한다.
같은 원문을 다시 인용한 경우도 각각 센 값이다.
정정 후 코드 원문 인용 1408개는 모두 지정된 파일·커밋·줄과 일치한다.
행 ID 287개의 결론 분류는 최종 보고서와 일치한다.
결론 문장 285개는 최종 보고서와 일치한다.
R2:P129와 R2:N08의 결론 문장은 원문 PDF에 따라 쪽 번호를 50에서 51로 정정했다.
두 행의 B 분류와 나머지 결론 내용은 최종 보고서와 일치한다.
R2 보고서의 쪽 번호 오류는 [매뉴얼 PDF 51쪽](../../../models/ShorelineS/raw/source_code/shorelines/doc/ShorelineS_manual_v1.0.pdf#page=51)의 `Kw=4.2` 목록으로 판정했다.
[R1:MU18](../compare/ShorelineS-theory-vs-code.md:459)도 같은 목록을 PDF 51쪽으로 인용한다.
상대 링크 55개는 실제 파일 또는 디렉터리를 가리킨다.
절 링크 41개의 대상 절이 존재한다.
대상 노트에는 mermaid 블록이 없다.
따라서 mermaid 상자의 호출 위치 대조 건수는 0건이다.
대상 노트에서 사용자 금지 절대 경로와 이중 대괄호는 0건이다.
대상 노트에서 실행·확인 미완료 또는 미검수 한계 문장은 0건이다.
H 분류의 적용 사례 지표 문장은 원문의 지표 성격을 설명하는 결론이다.
이 문장은 검수 미완료를 뜻하지 않는다.

## 기술 매뉴얼 정정·보완 목록

- [기술 매뉴얼:83](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:83) — 정정.

  전: 고정 간격의 파고는 제곱 평균의 제곱근이며, 파향은 파고 제곱으로 가중한 벡터 방향이다.

  후: 앞서 제시한 초기화 집약 조건이 성립하면 파고는 제곱 평균의 제곱근으로 집약된다. 파향은 파고 제곱으로 가중한 벡터 방향으로 집약된다.

  근거 원문: [get_aggregatedtimeseries.m:38](../../../models/ShorelineS/raw/source_code/shorelines/functions/get_aggregatedtimeseries.m:38) `if ~isempty(D(1).timenum) && TIME.tc==0`; [get_aggregatedtimeseries.m:51](../../../models/ShorelineS/raw/source_code/shorelines/functions/get_aggregatedtimeseries.m:51) `if factor>2`; [get_aggregatedtimeseries.m:40](../../../models/ShorelineS/raw/source_code/shorelines/functions/get_aggregatedtimeseries.m:40) `fldsc = {'Hs' 'Tp' 'c1' 'c2' 'h0' 'fshape' 'QSoffset'};`; [get_aggregatedtimeseries.m:41](../../../models/ShorelineS/raw/source_code/shorelines/functions/get_aggregatedtimeseries.m:41) `sfac = [2.0 1.0 1.0 1.0 1.0 1.0 1.0]; %scaling factors for scalars`; [get_aggregatedtimeseries.m:85](../../../models/ShorelineS/raw/source_code/shorelines/functions/get_aggregatedtimeseries.m:85) `HSfac = sfac(1);`. 지수 정의 세 줄의 인용도 보탰다.

- [기술 매뉴얼:145](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:145) — 정정.

  전: 적용범위 식 59-60 밖에서는 발산

  후: B가 매우 크거나 작으면 이 식은 발산할 수 있다. 적용범위 식 (59)~(60) 밖에서는 주의가 필요하다.

  근거 원문: [매뉴얼 PDF 40쪽 / 인쇄 40 of 66](../../../models/ShorelineS/raw/source_code/shorelines/doc/ShorelineS_manual_v1.0.pdf#page=40): `equation does however become unbounded when B becomes very large or very small`. 식 (59)~(60) 직전 문장은 적용범위 밖에서 주의하여 사용할 것을 요구한다.

- [기술 매뉴얼:187](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:187) — 보완.

  전: O·P 구조체 설명과 누적 수송 조건에 직접 쪽 인용이 없었다.

  후: **O 구조체**는 시간에 따라 격자 크기가 변하는 원시 결과를 저장한다. O 구조체의 값은 순간값이다. **P 구조체**는 사용자가 지정한 고정 격자에 재보간한 결과를 저장한다. O 구조체로 누적 수송을 계산하려면 출력 시간 간격이 충분히 촘촘해야 한다. (매뉴얼 PDF 56쪽 / 인쇄 56 of 66, §9.1)

  근거 원문: [매뉴얼 PDF 56쪽 / 인쇄 56 of 66, §9.1](../../../models/ShorelineS/raw/source_code/shorelines/doc/ShorelineS_manual_v1.0.pdf#page=56): `the O-structure stores the instanteneous data`; `calculation of the cumulative transport can only be done when sufficient output timesteps are used.` P의 격자는 `The grid is fixed in time and space.`로 설명한다.

- [기술 매뉴얼:291](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:291) — 정정.

  전: 구형 월류 함수는 이동량을 `.1*(s(2)-s(1))` 이하로 제한했다. 이 상한과 호출 경로는 `f5f12430 2024-06-14 Midsummer 2024 beta release`에서 제거됐다. 매뉴얼 발행 시점의 코드도 이미 폭 부족량에 비례하는 이동량을 사용했다. 삭제는 매뉴얼 발행일인 2024-10-15보다 앞선다.

  후: 구형 월류 함수는 이동량을 `.1*(s(2)-s(1))` 이하로 제한했다. 이 상한과 호출 경로는 `f5f12430 2024-06-14 Midsummer 2024 beta release`에서 제거됐다. 매뉴얼 발행 시점의 코드도 이미 폭 부족량에 비례하는 이동량을 사용했다.

  근거 원문: [R3:994](ShorelineS-callflow.md:994)의 `` 구형 월류 함수는 이동량을 `.1*(s(2)-s(1))` 이하로 제한했다. 이 상한과 호출 경로는 `f5f12430 2024-06-14 Midsummer 2024 beta release`에서 제거됐다. 매뉴얼 발행 시점의 코드도 이미 폭 부족량에 비례하는 이동량을 사용했다. ``. 보고서의 최종 결론 뒤에 덧붙인 발행일 비교 문장을 제거했다.

- [기술 매뉴얼:296](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:296) — 보완.

  전: manual-notes/shorelines-technical-manual-v1.md:68

  후: HEAD 기준 변경 전 노트 manual-notes/shorelines-technical-manual-v1.md:68

  근거 원문: 루트 `git diff -U0 HEAD -- models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md`의 변경 전 68행은 `` - **고정 시간증분** (p15 §3.2.3): `tc=0`+`dt`(년 단위, `dt=1/365`=1일). ``로 시작한다. 노트에 보존한 인용문 전체가 해당 변경 전 줄과 일치한다.

- [기술 매뉴얼:297](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:297) — 보완.

  전: manual-notes/shorelines-technical-manual-v1.md:69

  후: HEAD 기준 변경 전 노트 manual-notes/shorelines-technical-manual-v1.md:69

  근거 원문: 루트 `git diff -U0 HEAD -- models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md`의 변경 전 69행은 `` - **사구 부증분 `dtdune`** (p15 §3.2.4): 연 단위 분수. 해안선 증분보다 클 수 없다. ``로 시작한다. 노트에 보존한 인용문 전체가 해당 변경 전 줄과 일치한다.

- [기술 매뉴얼:329](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:329) — 정정.

  전: 과거 S.sources_sinks는 소스·싱크 처리 분기를 선택했다. f5f1243(2024-06-14)은 해당 함수와 호출을 삭제했다. 현재 sourcessinks는 기본값만 남은 입력이다. 이 삭제는 매뉴얼 발행일 2024-10-15보다 앞선다.

  후: 과거 S.sources_sinks는 소스·싱크 처리 분기를 선택했다. f5f1243(2024-06-14)은 해당 함수와 호출을 삭제했다. 현재 sourcessinks는 기본값만 남은 입력이다.

  근거 원문: [R2:554](../compare/ShorelineS-inputs-vs-code.md:554)의 `과거 S.sources_sinks는 소스·싱크 처리 분기를 선택했다. f5f1243(2024-06-14)은 해당 함수와 호출을 삭제했다. 현재 sourcessinks는 기본값만 남은 입력이다.`. 보고서의 최종 결론 뒤에 덧붙인 발행일 비교 문장을 제거했다.

- [기술 매뉴얼:330](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:330) — 정정.

  전: f5f1243(2024-06-14)은 S.SSfile을 읽던 Sources_Sinks를 삭제했다. 현재 ssfile 소비 부재는 과거 기능 삭제에 따른 판 차이다. 이 삭제는 매뉴얼 발행일 2024-10-15보다 앞선다.

  후: f5f1243(2024-06-14)은 S.SSfile을 읽던 Sources_Sinks를 삭제했다. 현재 ssfile 소비 부재는 과거 기능 삭제에 따른 판 차이다.

  근거 원문: [R2:555](../compare/ShorelineS-inputs-vs-code.md:555)의 `f5f1243(2024-06-14)은 S.SSfile을 읽던 Sources_Sinks를 삭제했다. 현재 ssfile 소비 부재는 과거 기능 삭제에 따른 판 차이다.`. 보고서의 최종 결론 뒤에 덧붙인 발행일 비교 문장을 제거했다.

- [기술 매뉴얼:333](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:333) — 정정.

  전: PDF 50의 목록

  후: PDF 51의 목록

  근거 원문: [매뉴얼 PDF 51쪽 / 인쇄 51 of 66](../../../models/ShorelineS/raw/source_code/shorelines/doc/ShorelineS_manual_v1.0.pdf#page=51)의 원문은 `Kw=4.2 Empirical coefficient (Sherman et al. 2013)`이다. PDF 50쪽에는 이 목록이 없다. R2 최종 보고서의 [R2:558](../compare/ShorelineS-inputs-vs-code.md:558)에 남아 있는 쪽 번호보다 원문 PDF를 우선했다.

- [기술 매뉴얼:351](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:351) — 정정.

  전: pauselength는 과거 모델 본문에서 pause에 전달됐다. f5f1243(2024-06-14)은 해당 소비를 삭제했다. A로 재분류한다. 이 삭제는 매뉴얼 발행일 2024-10-15보다 앞선다.

  후: pauselength는 과거 모델 본문에서 pause에 전달됐다. f5f1243(2024-06-14)은 해당 소비를 삭제했다. A로 재분류한다.

  근거 원문: [R2:577](../compare/ShorelineS-inputs-vs-code.md:577)의 `pauselength는 과거 모델 본문에서 pause에 전달됐다. f5f1243(2024-06-14)은 해당 소비를 삭제했다. A로 재분류한다.`. 보고서의 최종 결론 뒤에 덧붙인 발행일 비교 문장을 제거했다.

- [기술 매뉴얼:354](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:354) — 보완.

  전: functions/initialize_plot_variables.m:64; functions/initialize_plot_variables.m:65

  후: 0894269e:functions/initialize_plot_variables.m:64; 0894269e:functions/initialize_plot_variables.m:65

  근거 원문: 각 인용은 `git show 0894269e:functions/<파일>`의 지정 줄과 일치한다. 원문: `0894269e:functions/initialize_plot_variables.m:64` `if S.dune && S.bermw_plot`; `0894269e:functions/initialize_plot_variables.m:65` `BWplot=timenum0;                                                       % for extracting beach berm width at a certain transect(s)`. 삭제 이력은 [입력 git 판정](../compare/ShorelineS-git-verify-inputs.md:69)에 기록되어 있다.

- [기술 매뉴얼:355](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:355) — 보완.

  전: functions/Plot_berm_width.m:49; functions/Plot_berm_width.m:50

  후: 0894269e:functions/Plot_berm_width.m:49; 0894269e:functions/Plot_berm_width.m:50

  근거 원문: 각 인용은 `git show 0894269e:functions/<파일>`의 지정 줄과 일치한다. 원문: `0894269e:functions/Plot_berm_width.m:49` `BWplot_t=datetime(BWplot,'ConvertFrom','datenum','Format','yyyy-MM-dd');`; `0894269e:functions/Plot_berm_width.m:50` `BWplot=BWplot_t+calmonths(S.bermw_plot_int);`. 삭제 이력은 [입력 git 판정](../compare/ShorelineS-git-verify-inputs.md:69)에 기록되어 있다.

- [기술 매뉴얼:356](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:356) — 보완.

  전: functions/initialize_plot_variables.m:59; functions/initialize_plot_variables.m:60; functions/initialize_plot_variables.m:90; functions/initialize_plot_variables.m:91

  후: 0894269e:functions/initialize_plot_variables.m:59; 0894269e:functions/initialize_plot_variables.m:60; 0894269e:functions/initialize_plot_variables.m:90; 0894269e:functions/initialize_plot_variables.m:91

  근거 원문: 각 인용은 `git show 0894269e:functions/<파일>`의 지정 줄과 일치한다. 원문: `0894269e:functions/initialize_plot_variables.m:59` `if S.dune && S.qplot                                                         % for extracting wave and wind transport rates at a certain transect(s)`; `0894269e:functions/initialize_plot_variables.m:60` `innt=1;`; `0894269e:functions/initialize_plot_variables.m:90` `if S.CLplot ||S.bermw_plot ||S.qplot`; `0894269e:functions/initialize_plot_variables.m:91` `[x_trans,y_trans,n_trans]=prepare_transects(S,x_mc,y_mc,x_hard,y_hard,x_dune,y_dune,xl,yl);`. 삭제 이력은 [입력 git 판정](../compare/ShorelineS-git-verify-inputs.md:69)에 기록되어 있다.

- [기술 매뉴얼:357](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:357) — 보완.

  전: functions/prepare_transects.m:35; functions/prepare_transects.m:36; functions/prepare_transects.m:37; functions/prepare_transects.m:38

  후: 0894269e:functions/prepare_transects.m:35; 0894269e:functions/prepare_transects.m:36; 0894269e:functions/prepare_transects.m:37; 0894269e:functions/prepare_transects.m:38

  근거 원문: 각 인용은 `git show 0894269e:functions/<파일>`의 지정 줄과 일치한다. 원문: `0894269e:functions/prepare_transects.m:35` `if  ~isempty(S.transect)`; `0894269e:functions/prepare_transects.m:36` `xy_trans=load(S.transect);`; `0894269e:functions/prepare_transects.m:37` `x_trans=xy_trans(:,1);`; `0894269e:functions/prepare_transects.m:38` `y_trans=xy_trans(:,2);`. 삭제 이력은 [입력 git 판정](../compare/ShorelineS-git-verify-inputs.md:69)에 기록되어 있다.

- [기술 매뉴얼:358](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:358) — 보완.

  전: functions/initialize_plot_variables.m:73; functions/initialize_plot_variables.m:74

  후: 0894269e:functions/initialize_plot_variables.m:73; 0894269e:functions/initialize_plot_variables.m:74

  근거 원문: 각 인용은 `git show 0894269e:functions/<파일>`의 지정 줄과 일치한다. 원문: `0894269e:functions/initialize_plot_variables.m:73` `if S.CLplot`; `0894269e:functions/initialize_plot_variables.m:74` `CLplot=timenum0;                                                       % for extracting coastline position relative to the initial coastline at a certain transect(s)`. 삭제 이력은 [입력 git 판정](../compare/ShorelineS-git-verify-inputs.md:69)에 기록되어 있다.

- [기술 매뉴얼:359](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:359) — 보완.

  전: functions/plot_coastline_transect.m:46; functions/plot_coastline_transect.m:47

  후: 0894269e:functions/plot_coastline_transect.m:46; 0894269e:functions/plot_coastline_transect.m:47

  근거 원문: 각 인용은 `git show 0894269e:functions/<파일>`의 지정 줄과 일치한다. 원문: `0894269e:functions/plot_coastline_transect.m:46` `CLplot_t=datetime(CLplot,'ConvertFrom','datenum','Format','yyyy-MM-dd');`; `0894269e:functions/plot_coastline_transect.m:47` `CLplot=CLplot_t+calmonths(S.CLplot_int);`. 삭제 이력은 [입력 git 판정](../compare/ShorelineS-git-verify-inputs.md:69)에 기록되어 있다.

- [기술 매뉴얼:389](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:389) — 정정.

  전: PDF 50의 목록

  후: PDF 51의 목록

  근거 원문: [매뉴얼 PDF 51쪽 / 인쇄 51 of 66](../../../models/ShorelineS/raw/source_code/shorelines/doc/ShorelineS_manual_v1.0.pdf#page=51)의 원문은 `Kw=4.2 Empirical coefficient (Sherman et al. 2013)`이다. PDF 50쪽에는 이 목록이 없다. R2 최종 보고서의 [R2:671](../compare/ShorelineS-inputs-vs-code.md:671)에 남아 있는 쪽 번호보다 원문 PDF를 우선했다.

- [기술 매뉴얼:399](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:399) — 보완.

  전: manual-notes/shorelines-technical-manual-v1.md:175

  후: HEAD 기준 변경 전 노트 manual-notes/shorelines-technical-manual-v1.md:175

  근거 원문: 루트 `git diff -U0 HEAD -- models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md`의 변경 전 175행은 `매뉴얼 본문과 Appendix B 기본값 표가 어긋나는 지점이 셋 있다. **전부 코드를 직접 읽어 판정했다.**`로 시작한다. 노트에 보존한 인용문 전체가 해당 변경 전 줄과 일치한다.

- [기술 매뉴얼:400](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:400) — 정정.

  전: ssfile 파일 입력의 소비는 과거 Sources_Sinks에 있었다. f5f1243(2024-06-14)은 해당 함수를 삭제했다. F34를 A로 재분류한다. 이 삭제는 매뉴얼 발행일 2024-10-15보다 앞선다.

  후: ssfile 파일 입력의 소비는 과거 Sources_Sinks에 있었다. f5f1243(2024-06-14)은 해당 함수를 삭제했다. F34를 A로 재분류한다.

  근거 원문: [R2:686](../compare/ShorelineS-inputs-vs-code.md:686)의 `ssfile 파일 입력의 소비는 과거 Sources_Sinks에 있었다. f5f1243(2024-06-14)은 해당 함수를 삭제했다. F34를 A로 재분류한다.`. 보고서의 최종 결론 뒤에 덧붙인 발행일 비교 문장을 제거했다.

- [기술 매뉴얼:401](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:401) — 보완.

  전: functions/prepare_transects.m:35; functions/prepare_transects.m:36; functions/prepare_transects.m:37; functions/prepare_transects.m:38

  후: 0894269e:functions/prepare_transects.m:35; 0894269e:functions/prepare_transects.m:36; 0894269e:functions/prepare_transects.m:37; 0894269e:functions/prepare_transects.m:38

  근거 원문: 각 인용은 `git show 0894269e:functions/<파일>`의 지정 줄과 일치한다. 원문: `0894269e:functions/prepare_transects.m:35` `if  ~isempty(S.transect)`; `0894269e:functions/prepare_transects.m:36` `xy_trans=load(S.transect);`; `0894269e:functions/prepare_transects.m:37` `x_trans=xy_trans(:,1);`; `0894269e:functions/prepare_transects.m:38` `y_trans=xy_trans(:,2);`. 삭제 이력은 [입력 git 판정](../compare/ShorelineS-git-verify-inputs.md:69)에 기록되어 있다.

## FAQ 정정·보완 목록

- [FAQ:32](../../../models/ShorelineS/manual-notes/shorelines-faq-operational.md:32) — 정정.

  전: 고정 간격의 파고는 제곱 평균의 제곱근이며, 파향은 파고 제곱으로 가중한 벡터 방향이다.

  후: 앞서 제시한 초기화 집약 조건이 성립하면 파고는 제곱 평균의 제곱근으로 집약된다. 파향은 파고 제곱으로 가중한 벡터 방향으로 집약된다.

  근거 원문: [get_aggregatedtimeseries.m:38](../../../models/ShorelineS/raw/source_code/shorelines/functions/get_aggregatedtimeseries.m:38) `if ~isempty(D(1).timenum) && TIME.tc==0`; [get_aggregatedtimeseries.m:51](../../../models/ShorelineS/raw/source_code/shorelines/functions/get_aggregatedtimeseries.m:51) `if factor>2`; [get_aggregatedtimeseries.m:40](../../../models/ShorelineS/raw/source_code/shorelines/functions/get_aggregatedtimeseries.m:40) `fldsc = {'Hs' 'Tp' 'c1' 'c2' 'h0' 'fshape' 'QSoffset'};`; [get_aggregatedtimeseries.m:41](../../../models/ShorelineS/raw/source_code/shorelines/functions/get_aggregatedtimeseries.m:41) `sfac = [2.0 1.0 1.0 1.0 1.0 1.0 1.0]; %scaling factors for scalars`; [get_aggregatedtimeseries.m:85](../../../models/ShorelineS/raw/source_code/shorelines/functions/get_aggregatedtimeseries.m:85) `HSfac = sfac(1);`. 지수 정의 세 줄의 인용도 보탰다.

- [FAQ:67](../../../models/ShorelineS/manual-notes/shorelines-faq-operational.md:67) — 보완.

  전: manual-notes/shorelines-faq-operational.md:29

  후: HEAD 기준 변경 전 노트 manual-notes/shorelines-faq-operational.md:29

  근거 원문: 루트 `git diff -U0 HEAD -- models/ShorelineS/manual-notes/shorelines-faq-operational.md`의 변경 전 29행은 `` - 고정 dt: `S.tc=0` + `S.dt`[yr]. **전형 dt = 3시간~1일**. 고정 dt 사용 시 dt 내 파랑조건들을 **'에너지 벡터' 합산 평균**으로 집약. ``로 시작한다. 노트에 보존한 인용문 전체가 해당 변경 전 줄과 일치한다.

## 2020 논문 정정·보완 목록

- [2020 논문:7](../../../models/ShorelineS/manual-notes/shorelines-roelvink2020-frontiers.md:7) — 정정.

  전: 논문 내 쪽번호(1-19, Frontiers Vol.7 Art.535)

  후: 논문 내 쪽번호(1-20, Frontiers Vol.7 Art.535)

  근거 원문: [2020 논문 마지막 PDF 쪽](../../../models/ShorelineS/raw/source_code/shorelines/doc/FMarS2020_Roelvink_etal.pdf#page=20)의 인쇄 쪽 번호는 `20`이다. PDF의 전체 쪽 수도 20이다.

- [2020 논문:25](../../../models/ShorelineS/manual-notes/shorelines-roelvink2020-frontiers.md:25) — 정정.

  전: n=횡단(cross-shore) 좌표·s=연안 좌표·Dc=능동 단면고·Qs=연안수송[m³/yr]·tanβ=평균 단면경사·RSLR=상대해수면상승·qi=소스항(양빈 등).

  후: n은 횡단(cross-shore) 좌표이다. s는 연안 좌표이다. Dc는 능동 단면고이다. Qs는 연안수송[m³/yr]이다. tanβ는 사구 또는 배리어 마루에서 폐합수심까지의 평균 단면경사이다. RSLR은 상대해수면상승률[m/yr]이다. qi는 소스·싱크 항[m³/m/yr]이다. (2020 논문 PDF 3쪽 / 인쇄 3, 식 (1))

  근거 원문: [2020 논문 PDF 3쪽 / 인쇄 3, 식 (1)](../../../models/ShorelineS/raw/source_code/shorelines/doc/FMarS2020_Roelvink_etal.pdf#page=3): `qi is the source/sink term`; 상대해수면상승의 단위는 `m/yr`이다. qi의 단위는 `m³/m/yr`이다. 평균 경사의 구간은 `between the dune or barrier crest and the depth of closure`이다.

- [2020 논문:113](../../../models/ShorelineS/manual-notes/shorelines-roelvink2020-frontiers.md:113) — 보완.

  전: manual-notes/shorelines-roelvink2020-frontiers.md:47

  후: HEAD 기준 변경 전 노트 manual-notes/shorelines-roelvink2020-frontiers.md:47

  근거 원문: 루트 `git diff -U0 HEAD -- models/ShorelineS/manual-notes/shorelines-roelvink2020-frontiers.md`의 변경 전 47행은 `- 수송공식 목록은 Table 1(p.5) — 코드 실분기 7종`로 시작한다. 노트에 보존한 인용문 전체가 해당 변경 전 줄과 일치한다.

- [2020 논문:114](../../../models/ShorelineS/manual-notes/shorelines-roelvink2020-frontiers.md:114) — 보완.

  전: manual-notes/shorelines-roelvink2020-frontiers.md:36

  후: HEAD 기준 변경 전 노트 manual-notes/shorelines-roelvink2020-frontiers.md:36

  근거 원문: 루트 `git diff -U0 HEAD -- models/ShorelineS/manual-notes/shorelines-roelvink2020-frontiers.md`의 변경 전 36행은 `- 국소각이 임계각 초과 + updrift 측은 미만이면 **downdrift 점 수송을 최대수송(또는 임계각)으로 고정**`로 시작한다. 노트에 보존한 인용문 전체가 해당 변경 전 줄과 일치한다.

- [2020 논문:115](../../../models/ShorelineS/manual-notes/shorelines-roelvink2020-frontiers.md:115) — 보완.

  전: manual-notes/shorelines-roelvink2020-frontiers.md:41

  후: HEAD 기준 변경 전 노트 manual-notes/shorelines-roelvink2020-frontiers.md:41

  근거 원문: 루트 `git diff -U0 HEAD -- models/ShorelineS/manual-notes/shorelines-roelvink2020-frontiers.md`의 변경 전 41행은 `- Ashton-Murray(2006)의 **최소 배리어폭** 개념: 임계폭 미만 구간은 해측 침식분을 육측에 퇴적해 폭 유지(Leatherman 1979 인용).`로 시작한다. 노트에 보존한 인용문 전체가 해당 변경 전 줄과 일치한다.

## README 정정·보완 목록

- [README:18](../../../models/ShorelineS/README.md:18) — 정정.

  전: 공식 사이트 www.shorelines.nl (Roelvink et al. 2020 §Data Availability)

  후: 2020 논문은 MATLAB 소스 배포 주소로 `www.shorelines.nl`을 기재한다. (Roelvink et al. 2020, PDF 18쪽 / 인쇄 18, §Data Availability Statement)

  근거 원문: [2020 논문 PDF 18쪽 / 인쇄 18](../../../models/ShorelineS/raw/source_code/shorelines/doc/FMarS2020_Roelvink_etal.pdf#page=18): `Matlab source code for the ShorelineS model is available at www.shorelines.nl.` GitHub 저장소의 출처는 기존 [공식 리소스 기록](../../../models/ShorelineS/web-refs/shorelines-official-resources.md)이다.

- [README:30](../../../models/ShorelineS/README.md:30) — 보완.

  전: 프로세스 모듈 목록에 직접 인용이 없었다.

  후: [R3 초기화·시간 단계 순서](ShorelineS-callflow.md#1-초기화-순서) 인용을 보탰다.

  근거 원문: [ShorelineS.m:59](../../../models/ShorelineS/raw/source_code/shorelines/functions/ShorelineS.m:59) `[DUNE]    = prepare_dunes(S,COAST);`; [ShorelineS.m:242](../../../models/ShorelineS/raw/source_code/shorelines/functions/ShorelineS.m:242) `[COAST,SPIT]=find_overwash_mc(COAST,WAVE,SPIT,STRUC,TRANSP,DUNE,MUD,TIME);`; [ShorelineS.m:245](../../../models/ShorelineS/raw/source_code/shorelines/functions/ShorelineS.m:245) `[CHANNEL,COAST]=move_channel(CHANNEL,COAST,TIME);`. [R3 §1~2](ShorelineS-callflow.md#1-초기화-순서)의 초기화와 시간 단계 표에서 목록의 각 모듈을 대조했다.

- [README:59](../../../models/ShorelineS/README.md:59) — 보완.

  전: README.md:23

  후: HEAD 기준 변경 전 노트 README.md:23

  근거 원문: 루트 `git diff -U0 HEAD -- models/ShorelineS/README.md`의 변경 전 23행은 `` - **transport 공식 4종 선택**: `S.trform` = **CERC / KAMP(Kamphuis) / MILH(Mil-Homens) / VR14(Van Rijn 2014)** ``로 시작한다. 노트에 보존한 인용문 전체가 해당 변경 전 줄과 일치한다.

- [README:60](../../../models/ShorelineS/README.md:60) — 보완.

  전: README.md:25

  후: HEAD 기준 변경 전 노트 README.md:25

  근거 원문: 루트 `git diff -U0 HEAD -- models/ShorelineS/README.md`의 변경 전 25행은 `- **프로세스 모듈**: 사구(dune_erosion/flux/growth)·스핏/월류(prepare_spit·find_overwash_mc)`로 시작한다. 노트에 보존한 인용문 전체가 해당 변경 전 줄과 일치한다.

## 최종 확인

노트의 정정 13줄 끝에 `[10-12 전수 검증 정정]`을 붙였다.
노트의 인용 보완 18줄 끝에 `[10-12 전수 검증 보완]`을 붙였다.
앞머리 YAML의 정정 표시는 주석으로 붙였다.
착수 시 추가 줄 중 이번에 바뀐 줄은 기록한 31줄과 일치한다.
결론 분류·원문 인용·쪽 번호·과거 판 표시·상대 링크의 검증을 완료했다.
미해결 항목은 0건이다.
