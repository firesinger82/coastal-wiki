# ShorelineS 판독 기록 전수 대조 3

대조일은 2026-10-12이다.

사용자가 지정한 판독 기록 24개를 대조했다. 각 구간 행의 원문을 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다. 원문은 ISO-8859-1로 해독했다. 원문 4,119행을 모두 대조했다. 판독 기록의 구간 표 192행을 모두 대조했다. 코드 사실 107행도 모두 대조했다. 행 수의 근거는 아래 파일별 집계이다.

조건·계산식·분기 범위·기본값·부정·수량·단위·처리 순서를 확인했다. 원문에 없는 용도 단정도 확인했다. 행 번호가 붙은 백틱 인용 1,901개는 해당 원문 행과 일치했다. 이 수는 지정 기록에서 추출한 인용과 원문의 문자열 대조 결과이다. 실행 조건과 대입식의 원문 인용 누락은 없었다.

대상 원문에는 `get_default`류 호출로 `S.xxx` 기본값을 설정하는 문장이 없다. `make_video.m:44–55`에서 참조하는 S의 필드 6개에는 기본값 대입이 없다. `make_tidefile.m:109–113`의 키 기본값을 대조했다. `plot_figureproperties.m:35–39`의 선택 인수 기본값을 대조했다.

정정·보완·이상 없음은 구간 표 한 행 또는 코드 사실 한 행을 단위로 센다. 한 행의 여러 오류는 정정 한 건으로 센다. 제목·frontmatter·빈 줄·표 머리글은 이 집계에서 제외한다. 기록 전체 행 수에는 이 행들도 포함한다. 기존 `[10-12 검증 정정]` 표시는 이번 정정 수에 합산하지 않았다.

| 기록 | 기록 전체 행 | 구간 표 행 | 코드 사실 행 | 원문 대조 행 | 정정 | 보완 | 이상 없음 |
|---|---:|---:|---:|---:|---:|---:|---:|
| [insert_section.m.md](shorelines/functions/insert_section.m.md) | 23 | 4 | 2 | 74 | 0 | 0 | 6 |
| [interpNANs.m.md](shorelines/functions/interpNANs.m.md) | 27 | 6 | 4 | 104 | 2 | 0 | 8 |
| [interpNANsDIR.m.md](shorelines/functions/interpNANsDIR.m.md) | 24 | 5 | 2 | 68 | 1 | 0 | 6 |
| [interpolate_props.m.md](shorelines/functions/interpolate_props.m.md) | 26 | 6 | 3 | 125 | 1 | 0 | 8 |
| [interpolate_tide.m.md](shorelines/functions/interpolate_tide.m.md) | 23 | 4 | 2 | 88 | 1 | 0 | 5 |
| [introduce_climatechange.m.md](shorelines/functions/introduce_climatechange.m.md) | 27 | 6 | 4 | 116 | 1 | 0 | 9 |
| [introduce_perm_structures.m.md](shorelines/functions/introduce_perm_structures.m.md) | 22 | 3 | 2 | 66 | 0 | 0 | 5 |
| [introduce_runup.m.md](shorelines/functions/introduce_runup.m.md) | 34 | 11 | 6 | 266 | 1 | 0 | 16 |
| [introduce_wave.m.md](shorelines/functions/introduce_wave.m.md) | 35 | 11 | 7 | 280 | 1 | 0 | 17 |
| [introduce_wind.m.md](shorelines/functions/introduce_wind.m.md) | 29 | 7 | 5 | 171 | 1 | 0 | 11 |
| [isoctave.m.md](shorelines/functions/isoctave.m.md) | 21 | 3 | 1 | 39 | 1 | 0 | 3 |
| [make_sgrid_mc.m.md](shorelines/functions/make_sgrid_mc.m.md) | 37 | 14 | 6 | 302 | 3 | 0 | 17 |
| [make_tide/make_tidefile.m.md](shorelines/functions/make_tide/make_tidefile.m.md) | 33 | 10 | 6 | 251 | 2 | 0 | 14 |
| [make_video.m.md](shorelines/functions/make_video.m.md) | 24 | 4 | 3 | 66 | 1 | 0 | 6 |
| [merge_coastlines.m.md](shorelines/functions/merge_coastlines.m.md) | 25 | 5 | 3 | 85 | 0 | 0 | 8 |
| [merge_coastlines_mc.m.md](shorelines/functions/merge_coastlines_mc.m.md) | 58 | 27 | 14 | 690 | 7 | 0 | 34 |
| [move_channel.m.md](shorelines/functions/move_channel.m.md) | 35 | 10 | 8 | 240 | 1 | 0 | 17 |
| [nc_readfromgroup.m.md](shorelines/functions/nc_readfromgroup.m.md) | 22 | 3 | 2 | 20 | 0 | 0 | 5 |
| [plot_coast.m.md](shorelines/functions/plot_coast.m.md) | 52 | 22 | 13 | 508 | 6 | 0 | 29 |
| [plot_debug.m.md](shorelines/functions/plot_debug.m.md) | 27 | 7 | 3 | 131 | 0 | 0 | 10 |
| [plot_figureproperties.m.md](shorelines/functions/plot_figureproperties.m.md) | 22 | 4 | 0 | 54 | 1 | 0 | 3 |
| [plot_fill_sections.m.md](shorelines/functions/plot_fill_sections.m.md) | 29 | 9 | 3 | 174 | 1 | 0 | 11 |
| [plot_insert_land_fill.m.md](shorelines/functions/plot_insert_land_fill.m.md) | 27 | 6 | 4 | 115 | 0 | 0 | 10 |
| [plot_profiles.m.md](shorelines/functions/plot_profiles.m.md) | 26 | 5 | 4 | 86 | 0 | 0 | 9 |
| 합계 | 708 | 192 | 107 | 4119 | 32 | 0 | 267 |

아래 목록은 이번에 정정한 행이다. 기록 이름 뒤의 숫자는 원문 구간이다. 코드 사실 항목은 기존의 인용 구간으로 식별한다. 원문 경로는 해당 기록 frontmatter의 `file:`을 따른다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [interpNANs.m.md](shorelines/functions/interpNANs.m.md):41–58 | 행 배열을 판별해 전치한다. | 열 수가 행 수와 2보다 모두 클 때 전치한다. | 46–49 |
| [interpNANs.m.md](shorelines/functions/interpNANs.m.md):95–104 | 두 열 입력이면 x와 ynew를 결합한다. | 앞선 전치 처리 후 data가 두 열일 때 결합한다. | 46–49, 95–103 |
| [interpNANsDIR.m.md](shorelines/functions/interpNANsDIR.m.md):40–47 | 행 배열을 판별해 전치한다. | 열 수가 행 수와 2보다 모두 클 때 전치한다. | 41–44 |
| [interpolate_props.m.md](shorelines/functions/interpolate_props.m.md):103–115 | 114–115행에서 두 조건과 DUNE 분기를 종료한다. | 114행은 104행 조건을 종료한다. 115행은 DUNE 분기를 종료한다. 107행 조건은 109행에서 이미 끝난다. | 104, 107–109, 114–115 |
| [interpolate_tide.m.md](shorelines/functions/interpolate_tide.m.md):1–26 | 관측 지원점에서 보간한다. | 조석 지원점에서 보간한다. 원문은 관측 자료로 한정하지 않는다. | 4, 8–9 |
| [introduce_climatechange.m.md](shorelines/functions/introduce_climatechange.m.md):코드 사실(9·77–79·84–88) | slrrate를 사용하는 분기를 시계열 구간 밖으로 한정했다. | 76행 조건을 만족하지 않을 때 slrrate를 사용한다. dt가 0인 경우도 이 분기에 포함된다. | 65, 76–88 |
| [introduce_runup.m.md](shorelines/functions/introduce_runup.m.md):220–239 | 표본이 충분하고 양 끝 시각이 일치하면 직접 사용한다. | 표본은 둘 이상이어야 한다. 양 끝 시각과의 최소 차이는 각각 eps 미만이어야 한다. DUNE.dt는 비어 있어야 한다. | 177, 221–225 |
| [introduce_wave.m.md](shorelines/functions/introduce_wave.m.md):125–153 | 가장 가까운 주기 오차를 검사한다. 비영 이동일 때 경고를 쓴다. | 검사값은 mod(dt,365.25)의 최솟값이다. 경고 조건은 WAVE.dtrewind의 합이 0이 아닌 경우이다. 나머지 위치 조건은 유지했다. | 129–135, 150–152 |
| [introduce_wind.m.md](shorelines/functions/introduce_wind.m.md):95–114 | 여러 표본과 양 끝 시각 일치를 요구한다. | 표본은 둘 이상이어야 한다. 양 끝 시각과의 최소 차이는 각각 eps 미만이어야 한다. WIND.dt는 비어 있어야 한다. | 82, 96–99 |
| [isoctave.m.md](shorelines/functions/isoctave.m.md):1–5 | 빈 주석의 범위를 2–5행으로 적었다. | 2행은 함수 시그니처 주석이다. 4행은 기능 설명이다. 빈 주석은 3·5행이다. | 2–5 |
| [make_sgrid_mc.m.md](shorelines/functions/make_sgrid_mc.m.md):1–51 | 출력 주석이 방향을 설명한다고 적었다. | clockwise의 출력 주석도 cyclic 여부라고 적혀 있다. | 26–50 |
| [make_sgrid_mc.m.md](shorelines/functions/make_sgrid_mc.m.md):136–160 | 147–152행을 sn이 양수인 경우의 배열 생성으로 묶었다. | s2와 id2의 생성은 sn>0 조건 안에 있다. snew와 idgrid에 덧붙이는 연산은 그 조건 밖에 있다. | 140–153 |
| [make_sgrid_mc.m.md](shorelines/functions/make_sgrid_mc.m.md):169–196 | eps보다 먼 점을 보존한다. | 첫 점은 항상 보존한다. 나머지 점은 원래 배열의 직전 점과의 거리가 eps보다 클 때 보존한다. 이 처리는 179행 분기 안에 있다. | 171, 179–185 |
| [make_tide/make_tidefile.m.md](shorelines/functions/make_tide/make_tidefile.m.md):1–45 | 조석 지점을 관측점으로 한정했다. | 조석 지점의 자료는 관측값 또는 모델값이다. 최소 지점 수는 2개이다. | 9–13, 32–35 |
| [make_tide/make_tidefile.m.md](shorelines/functions/make_tide/make_tidefile.m.md):202–235 | 위상 차이 범위를 -180부터 180까지로 적었다. | 보정 범위는 -180도 이상 180도 미만이다. | 218 |
| [make_video.m.md](shorelines/functions/make_video.m.md):58–66 | writeVideo 호출과 close 호출을 try 안의 처리로 묶었다. | writeVideo는 try 안에 있다. close는 try 밖에 있다. | 60–64 |
| [merge_coastlines_mc.m.md](shorelines/functions/merge_coastlines_mc.m.md):158–202 | 교차 자료 전체를 재정렬한다. | indi를 정렬한다. 그 순서로 indj·P·xx·yy를 재배열한다. | 197–201 |
| [merge_coastlines_mc.m.md](shorelines/functions/merge_coastlines_mc.m.md):314–337 | 326–330행을 계속 조건으로 적었다. ids2를 교차 사용 횟수로 단정했다. | 326–330행은 정지 조건이다. 319행은 ids2(ids)에 2가 있는지 검사한다. 정지 조건이 참이면 ids2(ids)를 1씩 증가시킨다. 첫 교차점 거리 항에는 cyclici 또는 cyclicj 조건이 있다. | 214, 319–335 |
| [merge_coastlines_mc.m.md](shorelines/functions/merge_coastlines_mc.m.md):465–483 | unique(x+y)가 3 미만이라고 적었다. 포함 비율을 0으로 만드는 구간의 역할이 불명확했다. | 3과 비교하는 값은 gg 구간의 x+y 고유값 개수이다. 좌표 합 일치 조건은 pp<gg를 함께 요구한다. 점 수 검사는 pp 구간에 적용한다. NaN 검사는 gg 구간의 x에 적용한다. | 469–475 |
| [merge_coastlines_mc.m.md](shorelines/functions/merge_coastlines_mc.m.md):507–541 | 두 구간의 길이를 비교한다. | 첫 두 새 구간의 점 수를 비교한다. 최솟값과 같은 점 수의 구간 인덱스를 IDcw에서 제외한다. 이 처리는 IDouter가 비고 indi가 비어 있지 않을 때 수행한다. | 518–523 |
| [merge_coastlines_mc.m.md](shorelines/functions/merge_coastlines_mc.m.md):542–565 | IDS가 2개보다 많으면 내부 구간 하나를 선택한다. 재결합과 unique를 같은 분기로 묶었다. | 내부 선택에는 IDinner가 둘 이상이라는 조건도 필요하다. 외곽선 선택도 IDS가 2개보다 많은 분기 안에 있다. 두 선택은 최댓값의 첫 구간을 취한다. unique는 이 분기 밖에 있다. | 543–561 |
| [merge_coastlines_mc.m.md](shorelines/functions/merge_coastlines_mc.m.md):595–636 | 원래 구간을 유지한다. 예외 안내와 저장의 조건을 한꺼번에 설명했다. | 현재 xi·yi·xj·yj를 복사한다. 이 좌표에는 앞선 교차점 삽입이 반영되어 있다. 예외 안내는 length(xx)~=1 조건 안에 있다. 저장은 그 안의 debug==1 조건 안에 있다. 좌표 복사는 예외 안내 조건 밖에 있다. | 223–226, 602–607, 621–632 |
| [merge_coastlines_mc.m.md](shorelines/functions/merge_coastlines_mc.m.md):676–690 | 첫 점이면 뒤에서 두 점을 건너뛴 부분을 보존한다. | 끝에서 두 번째 이후의 표식이면 표식 바로 앞 점부터 끝까지 제거한다. 682행 분기에서는 첫 두 점을 제거하고 세 번째부터 보존한다. | 679–684 |
| [move_channel.m.md](shorelines/functions/move_channel.m.md):182–206 | dw를 fac를 곱한 폭 부족으로 설명했다. | dw는 현재 반폭에서 목표 반폭을 뺀 값에 CHANNEL.fac(iriv)를 곱한 값이다. 뺄셈 순서를 명시했다. | 182–184 |
| [plot_coast.m.md](shorelines/functions/plot_coast.m.md):1–73 | wberm_mc를 사구 폭으로 적었다. xyt를 고정 출력 격자로 단정했다. | wberm_mc는 해빈 폭이다. xyt를 고정 격자로 적은 것은 출력 주석의 설명이다. 실행 코드는 현재 해안 좌표를 저장한다. | 17–20, 67–72, 503–504 |
| [plot_coast.m.md](shorelines/functions/plot_coast.m.md):102–134 | 대표 파고와 대표 파향의 표본 선택을 구분하지 않았다. 차폐 배열 길이 비교 대상을 생략했다. | 파고는 외해 파고에서 비-NaN 평균을 뺀 값이 eps보다 큰 위치를 사용한다. 방향은 외해 파고가 NaN이 아닌 위치를 사용한다. 길이 비교 대상은 shadowS_mc와 WAVE.HStdp_mc이다. | 117–131 |
| [plot_coast.m.md](shorelines/functions/plot_coast.m.md):256–290 | 수송점과 관측점의 거리로 가장 가까운 격자 인덱스를 정한다. | 상대 위치는 파랑 자료 위치이다. WVCid는 최소 거리의 첫 인덱스와 WAVE.PHIo_mc 길이 중 작은 값이다. | 269–272 |
| [plot_coast.m.md](shorelines/functions/plot_coast.m.md):339–367 | 화살표 표시 조건을 비차폐로 적었다. | 두 차폐 지표가 각각 1 미만이라는 조건이다. | 352–358 |
| [plot_coast.m.md](shorelines/functions/plot_coast.m.md):415–429 | 사구 폭의 방향 성분을 뺀다. | 해빈 폭 wberm_mc의 방향 성분을 뺀다. | 19, 422–426 |
| [plot_coast.m.md](shorelines/functions/plot_coast.m.md):코드 사실(132–154) | 대표 파랑 계산의 근거도 132–154행으로 적었다. | 대표 파랑 계산의 근거인 117–123행을 인용 범위에 포함했다. | 117–123, 132–134, 154 |
| [plot_figureproperties.m.md](shorelines/functions/plot_figureproperties.m.md):1–6 | 빈 주석의 범위를 2–6행으로 적었다. | 2행은 함수 시그니처 주석이다. 4–5행은 기능 설명이다. 빈 주석은 3·6행이다. | 2–6 |
| [plot_fill_sections.m.md](shorelines/functions/plot_fill_sections.m.md):36–56 | 시간 단계도 FORMAT에서 가져온다고 적었다. | 시간 단계는 TIME.it에서 가져온다. 육지 폭·범위·저장 경계·채움 옵션은 FORMAT에서 가져온다. | 36–52 |

누락 조건·계산식을 추가한 보완 항목은 없다.

정정한 기록 17개에서 변경 행 32개를 확인했다. 각 변경 행 끝의 `[10-12 전수 검증 정정]` 표시를 확인했다. 구간 경계와 frontmatter는 변경 전과 일치한다. 원문 24개의 행 수와 SHA-256은 기록 frontmatter와 일치한다. 원문의 SHA-256은 작업 시작 때와도 일치한다. 원문·노트·git은 수정하지 않았다. 모델은 실행하지 않았다.

정정 32, 보완 0, 이상 없음 267
