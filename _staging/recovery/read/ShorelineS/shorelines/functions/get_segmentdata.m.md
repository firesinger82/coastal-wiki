---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_segmentdata.m
lines: 159
sha256: 0a5d07e413d687c6acf31c205ab8a2016838e2ae741a6d8026bf488d8571a777
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_segmentdata.m — 판독 구간 기록

구간은 1행부터 159행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–44 | 함수 시그니처는 `function [COAST,WAVE,TRANSP,i1,i2]=get_segmentdata(COAST,WAVE,TRANSP,DUNE,MUD,i_mc)` (1). 전체 해안 요소(coastal element)의 _mc 자료에서 활성 i_mc 구간을 가져온다는 주석이 있다(2–6). COAST 좌표·누적 거리·점 간격·활성 단면 높이(active profile height), WAVE 파고(wave height)·주기(wave period)·파향(wave direction)·회절(diffraction) 표식, TRANSP 수송·차폐(shadowing), DUNE 사구(dune)·MUD 갯벌(mudflat)·맹그로브(mangrove) 필드와 i_mc 입력을 설명한다(7–44). |
| 45–112 | 시작 시 1행 get_segmentdata 함수 안. 출력 주석은 COAST의 구간 좌표·점 수·수송점(transport point) 수·순환 여부·구간 경계·사구·갯벌 자료, WAVE 파고·주기·방향·회절, TRANSP 수송·차폐를 설명한다(45–84). 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(85–112). |
| 113–141 | 시작 시 1행 get_segmentdata 함수 안. 활성 구간 설정과 기본 자료 get_one_polygon 호출은 `COAST.i_mc=i_mc;` (113); `[ COAST.x,COAST.y,COAST.n_mc,i1,i2 ] = get_one_polygon( COAST.x_mc,COAST.y_mc,i_mc );` (114); `[ COAST.s ] = get_one_polygon(COAST.s_mc,i_mc);` (115); `[ COAST.ds ] = get_one_polygon(COAST.ds_mc,i_mc);` (116); `[ COAST.h0 ] = get_one_polygon(COAST.h0_mc,i_mc);` (117); `[ COAST.PHIcxy ] = get_one_polygon(COAST.PHIcxy_mc,i_mc);` (118); `[ COAST.PHIcxy0 ] = get_one_polygon(COAST.PHIcxy0_mc,i_mc);` (119); `[ WAVE.HSo ] = get_one_polygon( WAVE.HSo_mc,i_mc);` (120); `[ WAVE.TP ] = get_one_polygon( WAVE.TP_mc,i_mc);` (121). `if DUNE.used` (122)이면 사구 자료를 COAST 필드에서 추출하는 호출은 `[ COAST.qs ]       = get_one_polygon( COAST.qs_mc,i_mc);` (123); `[ COAST.qss ]      = get_one_polygon( COAST.qss_mc,i_mc);` (124); `[ COAST.ql ]       = get_one_polygon( COAST.ql_mc,i_mc);` (125); `[ COAST.qw ]       = get_one_polygon( COAST.qw_mc,i_mc);` (126); `[ COAST.R ]        = get_one_polygon( COAST.R_mc,i_mc);` (127); `[ COAST.SWL ]      = get_one_polygon( COAST.SWL_mc,i_mc);` (128); `[ COAST.wberm ]    = get_one_polygon( COAST.wberm_mc,i_mc);` (129); `[ COAST.dfelev ]   = get_one_polygon( COAST.dfelev_mc,i_mc);` (130); `[ COAST.dcelev ]   = get_one_polygon( COAST.dcelev_mc,i_mc);` (131). `if MUD.used` (133)이면 갯벌·맹그로브 자료 호출은 `[ COAST.dndt_mud ] = get_one_polygon( COAST.dndt_mudmc,i_mc);` (134); `[ COAST.dBfdt ]    = get_one_polygon( COAST.dBfdt_mc,i_mc);` (135); `[ COAST.dBmdt ]    = get_one_polygon( COAST.dBmdt_mc,i_mc);` (136); `[ COAST.dBfmdt ]   = get_one_polygon( COAST.dBfmdt_mc,i_mc);` (137); `[ COAST.Bf ]       = get_one_polygon( COAST.Bf_mc,i_mc);` (138); `[ COAST.Bm ]       = get_one_polygon( COAST.Bm_mc,i_mc);` (139); `[ COAST.Bfm ]      = get_one_polygon( COAST.Bfm_mc,i_mc);` (140). 각각의 분기를 닫는다(132·141). |
| 142–159 | 시작 시 1행 get_segmentdata 함수 안. 수송식(transport formulation) 선택은 `if (strcmpi(TRANSP.trform,'CERC') \|\| strcmpi(TRANSP.trform,'CERC2'))` (142). 참이면 QS와 PHItdp_mc 추출 호출 `[ TRANSP.QS,WAVE.PHI ] = get_one_polygon(TRANSP.QS_mc,WAVE.PHItdp_mc,i_mc);` (143). `else` (144)이면 PHIbr_mc를 쓰는 호출 `[ TRANSP.QS,WAVE.PHI ] = get_one_polygon(TRANSP.QS_mc,WAVE.PHIbr_mc,i_mc);` (145). COAST에 전체 차폐를 복사한다(147). 차폐 구간 호출은 `[ TRANSP.shadow ] = get_one_polygon(TRANSP.shadow_mc,i_mc);` (148); `[ TRANSP.shadowS_hD ] = get_one_polygon(TRANSP.shadowS_hD_mc,i_mc);` (149). COAST.shadow를 복사한다(150). 회절 추출·순환 검사·점 수 식은 `[ ~, WAVE.diff ] = get_one_polygon(WAVE.PHIbr_mc,WAVE.diff_mc,i_mc);` (151); `COAST.cyclic = get_cyclic(COAST.x,COAST.y,COAST.ds0);` (152); `COAST.n=length(COAST.x);` (153); `COAST.nq=length(TRANSP.QS);` (154). i_mc·i1·i2를 COAST에 보관한다(155–157). 빈 줄·함수 종료를 포함한다(158–159). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26–42·122–140: 사구·갯벌 입력 설명은 DUNE·MUD 필드를 적는다. 실행 추출 호출은 COAST의 해당 _mc 필드를 사용한다. DUNE·MUD에서는 used만 참조한다.
- 36·134: 주석의 필드명은 dndt_mud_mc이다. 실행문은 COAST.dndt_mudmc를 참조한다.
- 54·152: 출력 주석은 COAST.cyclic을 설명한다. 이 함수는 get_cyclic의 결과를 COAST.cyclic 전체 필드에 대입한다.
