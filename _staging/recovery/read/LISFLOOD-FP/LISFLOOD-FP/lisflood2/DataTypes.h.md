---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/lisflood2/DataTypes.h
lines: 264
sha256: 3b25c19cf414e01bb62f054c19539ae4e498a06fda567f9e8344ff7563ec481f
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# DataTypes.h — 판독 구간 기록

구간은 1행부터 264행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | `#pragma once` (1). lisflood.h·utility.h·lisflood2.h 포함(3–5). 이 파일에는 조건부 전처리가 없으며 이후 선언은 정밀도 선택과 무관하게 포함된다. NUMERIC_TYPE은 lisflood.h:75–97에서 정해지고 같은 소스 루트 config.default.cmake:2의 `_NUMERIC_MODE=1`은 double을 선택한다. IndexRange는 start·end 정수(7–11). WetDryRowBound는 현재/이전 침수 경계·체적 갱신 범위·DEM 유효 범위의 IndexRange 포인터와 블록(block) 수·행 경계를 가진다(13–31). AllocateWetDryRowBound 원형(33). |
| 35–60 | 전처리 조건 밖. SubGridFlowLookup은 각 셀로 들어오고 나가는 흐름 인덱스(index)의 `int flow_add[4];` (43), `int flow_subtract[4];` (44)를 가진다. 주석은 인덱스 0=dx, 1=dy, 2=우측 45도, 3=좌측 45도인 d8 방향을 적는다(39–44). SubGridState는 하위 격자 수로(subgrid channel) 유량·속도 포인터를 선언한다(48–57). 이전 폭 포인터는 주석(53)이다. |
| 61–87 | 전처리 조건 밖. SubGridCellInfo는 할당 셀 수·x/y·격자 인덱스·셀 면적·DEM·분포 침투율(63–74), 수로 폭·만제 수심(bankfull depth)·만제 체적·형상 계수·그룹·큰 수로 여부를 선언한다(76–83). 큰 수로의 증발 계산 설명은 `//if SGC_width > C(0.5)*(row_cell_dx + row_cell_dy), then there is no flood plain cell calc for evap` (82)라는 주석이다. AllocateSubGridCellInfo·ZeroSubGridCellInfo 원형(85–86). |
| 88–112 | 전처리 조건 밖. WaterSource는 점 소스(point source)·경계조건 자료로 count·Ident·고정값 Val·시계열(time series) 포인터와 셀 정보 ws_cell을 가진다(89–102). 이전 범람원(floodplain)/수로 유량과 Manning 조도로 미리 계산한 두 마찰 계수 배열을 선언한다(104–108). 고정값이 아니면 -1, 가변 시계열이 아니면 NULL이라는 설명은 주석이며 선언 초기화가 아니다(96·99). AllocateWaterSource 원형(111). |
| 113–147 | 전처리 조건 밖. 주석은 Flow_ 배열 길이 flow_count, Cell_ 배열 길이 flow_count*2, 짝의 i*2가 출발 셀·i*2+1이 도착 셀이라고 적는다(113–118). SubGridFlowInfo는 유효 거리·중력 포함 조도 제곱·셀 짝·셀 상태 인덱스·셀별 흐름 인덱스 목록·ChannelRatio를 선언한다(119–136). 유효 거리는 `(dx or dy) * meander`라는 주석(121)이다. SuperGridLinksList는 연결 수와 SGC/2D 셀 좌표·인덱스·고도·조도·폭·이전 유량·거리·만제 수심을 가진다(139–144). InitSuperLinksStructure·AllocateSuperLinksMemory 원형(145–146). |
| 148–185 | 전처리 조건 밖. SubGridRowList는 패딩(padding) 후 행 길이·행별 흐름/셀 수·SubGridFlowInfo·SubGridCellInfo를 선언한다(148–183). 메모리 배치 설명은 `j * row_cols_padded + 0` (159·166)부터 `j * row_cols_padded + cell_row_count[j]` (160·167)까지라고 적는다. 주석 예시의 패딩 행 길이는 8, 네 행의 셀 수는 3·4·0·1(169–180)이다. 실행 루프나 초기화문은 없다. |
| 186–208 | 전처리 조건 밖. PointSourceRowList는 패딩 행 길이·행별 점 소스 수·WaterSource와 양/음 점 소스 유량을 선언한다(186–195). 주석의 유량 단위는 체적/초(193–194). BoundaryCondition은 WaterSource와 유입/유출·수로 유출·질량 간격 누적 유입/유출 체적을 가진다(197–206). |
| 209–247 | 전처리 조건 밖. WeirLayout은 패딩 행 길이·x/y 방향 행별 보(weir) 수·격자 위치에서 보 목록을 가리키는 인덱스·전체 보 수(209–227), 격자 인덱스·마루고·유량 계수·지수·폭·마찰·고정 방향·종류·이전 수로 유량·양쪽 흐름 인덱스·셀 짝을 선언한다(229–244). 주석은 `2 * weir_id` (240)를 북/서측, `2 * weir_id + 1` (241)을 남/동측으로 설명한다. AllocateWeir 원형(246). |
| 248–264 | 전처리 조건 밖. RouteDynamicList는 행별 x/y 유하(routing) 수와 x/y 유량 위치의 열 인덱스 배열을 가진다(248–262). 주석은 row_cols_padded 대신 grid_cols_padded를 최대 크기로 사용한다고 적는다(250–251). AllocateRoutingDynamicList 원형이 마지막 행(264)이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 157–167: flow_info 앞 주석은 행별 flow_row_count를 설명하지만 같은 블록의 끝 인덱스 설명에는 cell_row_count[j]를 사용한다. cell_info 앞에도 같은 끝 인덱스 설명이 있다.
- 248–255: RouteDynamicList의 행별 개수 주석에는 weirs라고 적혀 있으나 선언된 멤버 이름은 row_route_qx_count·row_route_qy_count이다.
