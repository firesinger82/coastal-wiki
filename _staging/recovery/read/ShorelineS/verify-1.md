ShorelineS 판독 기록 전수 대조 결과 — 2026-10-12

대상은 사용자 지정 기록 34개다. 각 기록의 구간마다 frontmatter의 `file:` 원문을 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다. 원문은 ISO-8859-1로 표시하여 대조했다. 모든 구간의 조건·계산식·기본값·분기 의미·수량·단위·순서·바깥 블록을 확인했다. 표 아래 코드 사실 항목도 같은 원문과 대조했다.

기록 물리행 878행을 확인했다. 구간 행은 165개다. 코드 사실 항목은 134개다. 원문 대조 범위는 아래 파일별 행 수의 합계 4,102행이다.

정정과 보완은 해당 표시가 붙은 기록 행 수로 센다. 같은 기록 행에 두 표시가 있으면 양쪽에 각각 센다. 두 표시가 함께 있는 행은 3개다. 이상 없음은 이번 표시가 없는 구간 행과 코드 사실 항목 수다. frontmatter·머리말·표제·빈 줄은 기록 물리행 수에만 포함한다. 기존 `[10-12 검증 정정]` 표시는 이번 정정 수에 포함하지 않는다.

기록별 대조 결과다. 각 원문은 1행부터 아래 마지막 행까지 확인했다.

| 기록 | 기록 물리행 | 구간 행 | 코드 사실 항목 | 원문 마지막 행 | 정정 | 보완 | 이상 없음 |
|---|---:|---:|---:|---:|---:|---:|---:|
| [ShorelineS.m.md](shorelines/functions/ShorelineS.m.md) | 31 | 10 | 4 | 293 | 0 | 1 | 13 |
| [cleanup_nans.m.md](shorelines/functions/cleanup_nans.m.md) | 27 | 6 | 4 | 122 | 0 | 1 | 9 |
| [coastline_change.m.md](shorelines/functions/coastline_change.m.md) | 40 | 14 | 9 | 440 | 0 | 3 | 20 |
| [collect_variables.m.md](shorelines/functions/collect_variables.m.md) | 27 | 6 | 4 | 151 | 0 | 4 | 6 |
| [dune_erosion.m.md](shorelines/functions/dune_erosion.m.md) | 27 | 6 | 4 | 152 | 0 | 1 | 9 |
| [dune_flux.m.md](shorelines/functions/dune_flux.m.md) | 29 | 6 | 6 | 203 | 1 | 3 | 8 |
| [dune_growth.m.md](shorelines/functions/dune_growth.m.md) | 23 | 4 | 2 | 92 | 1 | 1 | 4 |
| [extract_berm.m.md](shorelines/functions/extract_berm.m.md) | 23 | 3 | 3 | 79 | 0 | 0 | 6 |
| [extract_shoreline.m.md](shorelines/functions/extract_shoreline.m.md) | 26 | 5 | 4 | 96 | 1 | 2 | 7 |
| [find_in_grid.m.md](shorelines/functions/find_in_grid.m.md) | 22 | 2 | 3 | 39 | 0 | 0 | 5 |
| [find_neighbours.m.md](shorelines/functions/find_neighbours.m.md) | 23 | 3 | 3 | 66 | 0 | 0 | 6 |
| [find_overwash_mc.m.md](shorelines/functions/find_overwash_mc.m.md) | 33 | 7 | 9 | 206 | 0 | 1 | 15 |
| [find_shadows_mc.m.md](shorelines/functions/find_shadows_mc.m.md) | 28 | 6 | 5 | 124 | 1 | 2 | 8 |
| [get_Sphimax.m.md](shorelines/functions/get_Sphimax.m.md) | 28 | 5 | 6 | 162 | 0 | 3 | 8 |
| [get_active_profile.m.md](shorelines/functions/get_active_profile.m.md) | 24 | 4 | 3 | 97 | 0 | 3 | 4 |
| [get_aggregatedtimeseries.m.md](shorelines/functions/get_aggregatedtimeseries.m.md) | 26 | 5 | 4 | 109 | 1 | 0 | 8 |
| [get_clockpoly.m.md](shorelines/functions/get_clockpoly.m.md) | 24 | 5 | 2 | 97 | 0 | 2 | 5 |
| [get_coastline_orientation.m.md](shorelines/functions/get_coastline_orientation.m.md) | 25 | 5 | 3 | 112 | 0 | 1 | 7 |
| [get_coastlineupdate_timestep.m.md](shorelines/functions/get_coastlineupdate_timestep.m.md) | 27 | 6 | 4 | 129 | 1 | 1 | 8 |
| [get_cumdist.m.md](shorelines/functions/get_cumdist.m.md) | 20 | 2 | 1 | 37 | 0 | 0 | 3 |
| [get_cyclic.m.md](shorelines/functions/get_cyclic.m.md) | 21 | 2 | 2 | 40 | 0 | 0 | 4 |
| [get_dirspr_prob.m.md](shorelines/functions/get_dirspr_prob.m.md) | 23 | 3 | 3 | 58 | 0 | 0 | 6 |
| [get_disper.m.md](shorelines/functions/get_disper.m.md) | 21 | 2 | 2 | 45 | 0 | 0 | 4 |
| [get_disttopolyline.m.md](shorelines/functions/get_disttopolyline.m.md) | 22 | 2 | 3 | 53 | 0 | 0 | 5 |
| [get_fallvelocity.m.md](shorelines/functions/get_fallvelocity.m.md) | 21 | 2 | 2 | 39 | 0 | 0 | 4 |
| [get_fields.m.md](shorelines/functions/get_fields.m.md) | 20 | 2 | 0 | 41 | 0 | 0 | 2 |
| [get_fnourishment.m.md](shorelines/functions/get_fnourishment.m.md) | 28 | 6 | 5 | 143 | 2 | 2 | 7 |
| [get_fnourishment_diffusion.m.md](shorelines/functions/get_fnourishment_diffusion.m.md) | 20 | 2 | 1 | 44 | 0 | 0 | 3 |
| [get_fnourishment_fraction.m.md](shorelines/functions/get_fnourishment_fraction.m.md) | 26 | 4 | 5 | 105 | 1 | 3 | 5 |
| [get_fnourishment_rate.m.md](shorelines/functions/get_fnourishment_rate.m.md) | 26 | 4 | 5 | 86 | 2 | 2 | 6 |
| [get_foreshore_orientation.m.md](shorelines/functions/get_foreshore_orientation.m.md) | 28 | 6 | 5 | 140 | 0 | 5 | 6 |
| [get_gridprojection.m.md](shorelines/functions/get_gridprojection.m.md) | 23 | 4 | 2 | 74 | 0 | 2 | 4 |
| [get_gridsize.m.md](shorelines/functions/get_gridsize.m.md) | 22 | 3 | 2 | 60 | 0 | 1 | 4 |
| [get_inputfiledata.m.md](shorelines/functions/get_inputfiledata.m.md) | 44 | 13 | 14 | 368 | 1 | 7 | 20 |
| 합계 | 878 | 165 | 134 | 4102 | 12 | 51 | 239 |

정정 목록이다. 원문 행은 각 기록의 `file:` 경로를 기준으로 한다. “사실”은 표 아래 코드 사실 항목을 가리킨다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [dune_flux.m.md](shorelines/functions/dune_flux.m.md):144–175 | HSo1을 외해 파고로 단정. | 원문 주석의 동적 단면 하단 가능성과 의문을 보존. | 162–165 |
| [dune_growth.m.md](shorelines/functions/dune_growth.m.md):78–88 | cosphiwndloc를 육지 방향 풍향으로 단정. | phic와 phiwndi의 차이에 대한 코사인으로 설명. | 22–23·86 |
| [extract_shoreline.m.md](shorelines/functions/extract_shoreline.m.md):63–78 | slplot 네 번째 열을 날짜로 단정. | 원문에 나타난 열 번호와 연결 순서를 명시. | 68 |
| [find_shadows_mc.m.md](shorelines/functions/find_shadows_mc.m.md):65–74 | distw를 관측점 거리로 서술. | 원문 주석의 파랑 출력 지점 거리로 정정. | 69–72 |
| [get_aggregatedtimeseries.m.md](shorelines/functions/get_aggregatedtimeseries.m.md):76–93 | 정규화 뒤 mean을 적용한 값을 파고 가중 평균으로 서술. | 파고 제곱합으로 나눈 항에 mean을 적용함을 명시. | 85–90 |
| [get_coastlineupdate_timestep.m.md](shorelines/functions/get_coastlineupdate_timestep.m.md):사실 71–75·82–119 | dtnew 대입 자체가 TIME.tc>0 경로에만 있다고 기록. | TIME.dt에 dtnew를 대입하는 문장으로 대상을 한정. | 71–75·82–89 |
| [get_fnourishment.m.md](shorelines/functions/get_fnourishment.m.md):67–94 | 69행의 <= 조건을 모델 이전으로 한정. 82행 분기를 모델 이후 시작 양빈으로 한정. | 모델 시작 시각과 같은 경우도 포함. 69행 분기 미선택과 실제 총 체적 0 조건으로 설명. | 69 / 69·82–86 |
| [get_fnourishment.m.md](shorelines/functions/get_fnourishment.m.md):사실 82·85·110 | Vt(n,t)를 초기 체적으로 설명. | 해당 시각 총 체적과 분기 조건을 명시. | 69·82–85 |
| [get_fnourishment_fraction.m.md](shorelines/functions/get_fnourishment_fraction.m.md):사실 90–100 | 관련 없는 구간의 idx와 dxnour를 모두 비운다고 서술. | idx의 빈 배열 대입과 dxnour의 0 대입을 구분. | 98–100 |
| [get_fnourishment_rate.m.md](shorelines/functions/get_fnourishment_rate.m.md):36–48 | 42행 else를 모델 이전 평가로 한정. | 실제 분기 조건 dtsteps~=1로 설명. | 37·42 |
| [get_fnourishment_rate.m.md](shorelines/functions/get_fnourishment_rate.m.md):49–67 | 바깥 else를 모델 이전 평가로 한정. WVC 좌표를 관측점으로 단정. | 실제 dtsteps 분기를 명시. 원문이 제공하는 파랑 자료 지점으로 설명. | 37·42 / 49–58 |
| [get_inputfiledata.m.md](shorelines/functions/get_inputfiledata.m.md):117–152 | NetCDF station 좌표를 관측점으로 단정. | SnapWave 입력의 파랑 자료 지점으로 설명. | 124–140 |

보완 목록이다. 원문 행은 각 기록의 `file:` 경로를 기준으로 한다. “사실”은 표 아래 코드 사실 항목을 가리킨다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [ShorelineS.m.md](shorelines/functions/ShorelineS.m.md):197–213 | 시간 간격 기록을 뜻으로만 기록. | TIME.it+1 위치의 대입 원문을 추가. | 197 |
| [cleanup_nans.m.md](shorelines/functions/cleanup_nans.m.md):61–78 | 끝 NaN 분기의 좌표 선택식을 뜻으로만 기록. | 1:i-1 선택식 두 개를 추가. | 65–67 |
| [coastline_change.m.md](shorelines/functions/coastline_change.m.md):219–250 | catch 경로의 인덱스 제한을 뜻으로만 기록. | min/max로 제한하는 인덱스 원문을 추가. | 233 |
| [coastline_change.m.md](shorelines/functions/coastline_change.m.md):385–411 | x0·y0의 열 벡터 변환식의 원문 인용이 없음. | x0·y0의 열 벡터 변환식을 원문 그대로 추가. | 386·387 |
| [coastline_change.m.md](shorelines/functions/coastline_change.m.md):412–440 | dSds_mc 연결을 뜻으로만 기록. | NaN 구분자를 포함한 연결식을 추가. | 423 |
| [collect_variables.m.md](shorelines/functions/collect_variables.m.md):50–65 | 사구 필드 제거·연결식을 뜻으로만 기록. 진흙 필드의 연결식의 원문 인용이 없음. | 1:end-1 선택식과 필드 연결식을 추가. 진흙 필드의 연결식을 원문 그대로 추가. | 56·58 / 61 |
| [collect_variables.m.md](shorelines/functions/collect_variables.m.md):66–98 | _mc 필드 이름 구성식과 PHI를 HS로 바꾸는 식의 원문 인용이 없음. | _mc 필드 이름 구성식과 PHI를 HS로 바꾸는 식을 원문 그대로 추가. | 68·75·87·95 |
| [collect_variables.m.md](shorelines/functions/collect_variables.m.md):99–118 | COAST·WAVE·TRANSP 배열의 NaN 구분자 연결식의 원문 인용이 없음. | COAST·WAVE·TRANSP 배열의 NaN 구분자 연결식을 원문 그대로 추가. | 101·108·115 |
| [collect_variables.m.md](shorelines/functions/collect_variables.m.md):119–139 | diff_mc의 NaN 치환식과 logical 변환식의 원문 인용이 없음. | diff_mc의 NaN 치환식과 logical 변환식을 원문 그대로 추가. | 120·121 |
| [dune_erosion.m.md](shorelines/functions/dune_erosion.m.md):125–147 | 비침식점의 qs·qd·qds·qss·ql을 0으로 만드는 마스크 대입식의 원문 인용이 없음. | 비침식점의 qs·qd·qds·qss·ql을 0으로 만드는 마스크 대입식을 원문 그대로 추가. | 130·131·132·133·134 |
| [dune_flux.m.md](shorelines/functions/dune_flux.m.md):85–122 | phic의 길이와 cs·cstill의 행 벡터 변환식의 원문 인용이 없음. | phic의 길이와 cs·cstill의 행 벡터 변환식을 원문 그대로 추가. | 96·106·107 |
| [dune_flux.m.md](shorelines/functions/dune_flux.m.md):176–193 | 세 차폐 마스크에서 qs·qss·ql을 0으로 만드는 대입식의 원문 인용이 없음. | 세 차폐 마스크에서 qs·qss·ql을 0으로 만드는 대입식을 원문 그대로 추가. | 184·185·186·187·188·189·190·191·192 |
| [dune_flux.m.md](shorelines/functions/dune_flux.m.md):사실 88–93·154 | dtnum 상한 설명에 DUNE.dt가 빈 경우를 생략. | DUNE.dt 유무에 따른 분기와 1/365/48 상한을 명시. | 88–93·154 |
| [dune_growth.m.md](shorelines/functions/dune_growth.m.md):64–77 | phic의 길이 계산식의 원문 인용이 없음. | phic의 길이 계산식을 원문 그대로 추가. | 64 |
| [extract_shoreline.m.md](shorelines/functions/extract_shoreline.m.md):45–62 | L2Name의 end+1 위치에 이름을 추가하는 식의 원문 인용이 없음. | L2Name의 end+1 위치에 이름을 추가하는 식을 원문 그대로 추가. | 61 |
| [extract_shoreline.m.md](shorelines/functions/extract_shoreline.m.md):63–78 | 69행 else의 파일 이름 변환식의 원문 인용이 없음. | 69행 else의 파일 이름 변환식을 원문 그대로 추가. | 70 |
| [find_overwash_mc.m.md](shorelines/functions/find_overwash_mc.m.md):179–206 | dxt·dyt의 NaN을 0으로 바꾸는 마스크 대입식의 원문 인용이 없음. | dxt·dyt의 NaN을 0으로 바꾸는 마스크 대입식을 원문 그대로 추가. | 196·197 |
| [find_shadows_mc.m.md](shorelines/functions/find_shadows_mc.m.md):50–64 | 수송점 수 nq의 계산식의 원문 인용이 없음. | 수송점 수 nq의 계산식을 원문 그대로 추가. | 51 |
| [find_shadows_mc.m.md](shorelines/functions/find_shadows_mc.m.md):92–112 | 차폐 구간 번호에 unique를 적용하는 식의 원문 인용이 없음. | 차폐 구간 번호에 unique를 적용하는 식을 원문 그대로 추가. | 109 |
| [get_Sphimax.m.md](shorelines/functions/get_Sphimax.m.md):52–87 | 파랑 조건 수 nw와 격자 수 nq의 계산식의 원문 인용이 없음. | 파랑 조건 수 nw와 격자 수 nq의 계산식을 원문 그대로 추가. | 56·57 |
| [get_Sphimax.m.md](shorelines/functions/get_Sphimax.m.md):88–115 | 갱신 마스크 in에서 행·열 인덱스를 찾는 식의 원문 인용이 없음. | 갱신 마스크 in에서 행·열 인덱스를 찾는 식을 원문 그대로 추가. | 103 |
| [get_Sphimax.m.md](shorelines/functions/get_Sphimax.m.md):116–136 | 표본 교체를 부등식 마스크라는 말로만 기록. 각도 999를 NaN으로 바꾸는 마스크 대입식의 원문 인용이 없음. | 각 마스크와 갱신 순서의 원문 네 식을 추가. 각도 999를 NaN으로 바꾸는 마스크 대입식을 원문 그대로 추가. | 117–120 / 127 |
| [get_active_profile.m.md](shorelines/functions/get_active_profile.m.md):47–65 | load의 지역 변수 대입식과 COAST.h0input의 세 열 전치식의 원문 인용이 없음. | load의 지역 변수 대입식과 COAST.h0input의 세 열 전치식을 원문 그대로 추가. | 51·52·53·54 |
| [get_active_profile.m.md](shorelines/functions/get_active_profile.m.md):66–87 | 구간 시작의 바깥 조건 연쇄를 생략. 수치 입력의 세 열 전치식의 원문 인용이 없음. | 47행 if/elseif 연쇄 안임을 명시. 수치 입력의 세 열 전치식을 원문 그대로 추가. | 47·66–87 / 74·75·76 |
| [get_active_profile.m.md](shorelines/functions/get_active_profile.m.md):88–97 | 구간 시작의 바깥 조건 연쇄를 생략. | 47행 if/elseif 연쇄 안임을 명시. | 47·88–90 |
| [get_clockpoly.m.md](shorelines/functions/get_clockpoly.m.md):46–58 | x·y의 열 벡터 변환식의 원문 인용이 없음. | x·y의 열 벡터 변환식을 원문 그대로 추가. | 46·47 |
| [get_clockpoly.m.md](shorelines/functions/get_clockpoly.m.md):59–72 | 수직 변 xd의 NaN 대입식의 원문 인용이 없음. | 수직 변 xd의 NaN 대입식을 원문 그대로 추가. | 60 |
| [get_coastline_orientation.m.md](shorelines/functions/get_coastline_orientation.m.md):49–64 | 순환·비순환 경계의 PHIc 연결식의 원문 인용이 없음. | 순환·비순환 경계의 PHIc 연결식을 원문 그대로 추가. | 59·63 |
| [get_coastlineupdate_timestep.m.md](shorelines/functions/get_coastlineupdate_timestep.m.md):122–129 | 비활성 디버그 블록의 TIME.dts 연결식의 원문 인용이 없음. | 비활성 디버그 블록의 TIME.dts 연결식을 원문 그대로 추가. | 125 |
| [get_fnourishment.m.md](shorelines/functions/get_fnourishment.m.md):95–122 | 침식 계산을 하지 않는 분기의 t+1 체적 대입식의 원문 인용이 없음. | 침식 계산을 하지 않는 분기의 t+1 체적 대입식을 원문 그대로 추가. | 114 |
| [get_fnourishment.m.md](shorelines/functions/get_fnourishment.m.md):135–143 | q_tot_mc의 NaN 구분자 연결식의 원문 인용이 없음. | q_tot_mc의 NaN 구분자 연결식을 원문 그대로 추가. | 139 |
| [get_fnourishment_fraction.m.md](shorelines/functions/get_fnourishment_fraction.m.md):49–73 | dsc의 NaN을 0으로 바꾸는 식의 원문 인용이 없음. | dsc의 NaN을 0으로 바꾸는 식을 원문 그대로 추가. | 65 |
| [get_fnourishment_fraction.m.md](shorelines/functions/get_fnourishment_fraction.m.md):74–88 | 차폐점 검색·membership·idx 삭제식의 원문 인용이 없음. | 차폐점 검색·membership·idx 삭제식을 원문 그대로 추가. | 76·77·78 |
| [get_fnourishment_fraction.m.md](shorelines/functions/get_fnourishment_fraction.m.md):89–105 | 관련 구간 배열 구성·중복 축소·삭제 목록 구성·교집합·제외 및 0 대입식의 원문 인용이 없음. | 관련 구간 배열 구성·중복 축소·삭제 목록 구성·교집합·제외 및 0 대입식을 원문 그대로 추가. | 92·94·96·97·98·99·100 |
| [get_fnourishment_rate.m.md](shorelines/functions/get_fnourishment_rate.m.md):49–67 | 구간 시작의 44행 조건 연쇄를 생략. WVC의 x·y 좌표 연결식의 원문 인용이 없음. | 44행 if/elseif 연쇄 안임을 명시. WVC의 x·y 좌표 연결식을 원문 그대로 추가. | 44·49 / 51·52 |
| [get_fnourishment_rate.m.md](shorelines/functions/get_fnourishment_rate.m.md):사실 44–65 | H·T 미대입 설명에 바깥 dtsteps 분기를 생략. | 37행 조건이 거짓인 경로로 한정. | 37·42–65 |
| [get_foreshore_orientation.m.md](shorelines/functions/get_foreshore_orientation.m.md):46–75 | nl 계산식과 xq·yq의 열 벡터 변환식의 원문 인용이 없음. | nl 계산식과 xq·yq의 열 벡터 변환식을 원문 그대로 추가. | 60·61·62 |
| [get_foreshore_orientation.m.md](shorelines/functions/get_foreshore_orientation.m.md):76–86 | 네 열 임시표 구성·연결·첫 세 열 선택식의 원문 인용이 없음. | 네 열 임시표 구성·연결·첫 세 열 선택식을 원문 그대로 추가. | 78·80·83 |
| [get_foreshore_orientation.m.md](shorelines/functions/get_foreshore_orientation.m.md):87–104 | 순환 분기에서 nl을 계산하는 식의 원문 인용이 없음. | 순환 분기에서 nl을 계산하는 식을 원문 그대로 추가. | 93 |
| [get_foreshore_orientation.m.md](shorelines/functions/get_foreshore_orientation.m.md):105–116 | 다섯 셀 구성·좌표 및 방향 연결·세 열 표 변환식의 원문 인용이 없음. | 다섯 셀 구성·좌표 및 방향 연결·세 열 표 변환식을 원문 그대로 추가. | 106·108·109·110·113 |
| [get_foreshore_orientation.m.md](shorelines/functions/get_foreshore_orientation.m.md):117–140 | 방향 표의 세 열 추출·전치식의 원문 인용이 없음. | 방향 표의 세 열 추출·전치식을 원문 그대로 추가. | 126·127·128 |
| [get_gridprojection.m.md](shorelines/functions/get_gridprojection.m.md):47–59 | WAVE·TRANSP·COAST 스칼라 자료의 _mc 필드 선택식의 원문 인용이 없음. | WAVE·TRANSP·COAST 스칼라 자료의 _mc 필드 선택식을 원문 그대로 추가. | 51·53·55 |
| [get_gridprojection.m.md](shorelines/functions/get_gridprojection.m.md):60–71 | WAVE·TRANSP·COAST 방향 자료의 _mc 필드 선택식의 원문 인용이 없음. | WAVE·TRANSP·COAST 방향 자료의 _mc 필드 선택식을 원문 그대로 추가. | 64·66·68 |
| [get_gridsize.m.md](shorelines/functions/get_gridsize.m.md):52–60 | NaN 검색·중심 배열 선택·두 출력의 행 벡터 변환식의 원문 인용이 없음. | NaN 검색·중심 배열 선택·두 출력의 행 벡터 변환식을 원문 그대로 추가. | 53·55·58·59 |
| [get_inputfiledata.m.md](shorelines/functions/get_inputfiledata.m.md):36–50 | 문자 입력의 셀 변환식과 가로 목록 전치식의 원문 인용이 없음. | 문자 입력의 셀 변환식과 가로 목록 전치식을 원문 그대로 추가. | 40·43 |
| [get_inputfiledata.m.md](shorelines/functions/get_inputfiledata.m.md):51–89 | 결측값 마스크를 뜻으로만 기록. textscan의 첫 열 형식을 생략. 대체 textscan 형식과 재배열 순서를 생략. 참조 파일 경로의 연결식의 원문 인용이 없음. | -999 이하의 마스크 원문을 추가. 문자열과 수치 네 열의 판독 형식을 추가. 수치 두 열 뒤 문자열을 읽는 형식과 셀 재배열식을 추가. 참조 파일 경로의 연결식을 원문 그대로 추가. | 53 / 65 / 67–68 / 80 |
| [get_inputfiledata.m.md](shorelines/functions/get_inputfiledata.m.md):90–116 | GKL 입력의 RAY 파일 경로 연결식의 원문 인용이 없음. | GKL 입력의 RAY 파일 경로 연결식을 원문 그대로 추가. | 99 |
| [get_inputfiledata.m.md](shorelines/functions/get_inputfiledata.m.md):117–152 | time의 열 벡터 변환식과 NetCDF 배열의 차원별 squeeze·전치식의 원문 인용이 없음. | time의 열 벡터 변환식과 NetCDF 배열의 차원별 squeeze·전치식을 원문 그대로 추가. | 139·141·142·143·145·146·147 |
| [get_inputfiledata.m.md](shorelines/functions/get_inputfiledata.m.md):213–240 | 수위 기후 자료의 열 수 계산식의 원문 인용이 없음. | 수위 기후 자료의 열 수 계산식을 원문 그대로 추가. | 226 |
| [get_inputfiledata.m.md](shorelines/functions/get_inputfiledata.m.md):241–276 | 바람 기후 자료의 열 수 계산식의 원문 인용이 없음. | 바람 기후 자료의 열 수 계산식을 원문 그대로 추가. | 262 |
| [get_inputfiledata.m.md](shorelines/functions/get_inputfiledata.m.md):302–332 | WaveDA_record 첫 열의 timenum 대입식의 원문 인용이 없음. | WaveDA_record 첫 열의 timenum 대입식을 원문 그대로 추가. | 309 |

원문의 모든 구간은 빈틈과 중복 없이 이어진다. 기록의 `file:` 경로와 원문 행 수를 확인했다. 원문 SHA-256은 대상 기록 34개의 frontmatter와 일치한다. 기존 인용 1,060개를 해당 원문 행과 대조했다. 수정 후에는 행 번호가 붙은 백틱 인용 1,183개가 해당 원문과 일치한다. 인용 비교에서는 Markdown 표의 `\|` 이스케이프를 원문 `|`로 복원했다.

대상 원문에는 `S.xxx` 필드별 기본값을 실행 대입하는 문장이 없다. `ShorelineS.m:55`는 `initialize_defaultvalues(S0)`를 호출한다. 다른 입력의 생략값과 배열 초기값은 해당 구간에서 확인했다.

기록의 구간 경계와 frontmatter는 바꾸지 않았다. 원문과 노트는 수정하지 않았다. Git 작업은 하지 않았다. 모델은 실행하지 않았다.

정정 12, 보완 51, 이상 없음 239
