---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Propwash/Propwash_Calc_Sequence.f90
lines: 147
sha256: df5016580862b6f59281c233acfe37458bfb9b6b122fd510923ea401d09cbdc0
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Propwash_Calc_Sequence.f90 — 판독 구간 기록

구간은 1행부터 147행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | EFDC+ 출처·GPLv2·저작권과 추진기 후류(propeller wash)의 퇴적층 영향 계산 목적(1–15). Propwash_Calc_Sequence는 ieffluxonly를 입력받는다(16·27). GLOBAL의 timeday와 Variables_Propwash·Mod_Active_Ship·Variables_Ship을 사용한다(18–22). pos_ids는 SAVE allocatable track_ids 배열이고 DSTIME은 외부 함수이다(34·39). 계산·설정 원문: `real(kind = rkd) :: start_time, end_time, effvel, ttds` (32). |
| 41–64 | 시작 시 16행 Propwash_Calc_Sequence 루틴 안. 최초 pos_ids 할당에서 total_ships 크기를 사용하고 Det_Adjacent_Cells를 호출한다(42–47). 퇴적물 수송 설정에 따라 DTSEDJ에 DTSED 또는 DT를 복사한다(49–53). DEBUGGING 전처리 분기는 local_debug를 true/false로 설정한다. 원문 전처리 조건은 `#ifdef DEBUGGING` (55), `#else` (57), `#endif` (59)이다. DSTIME으로 계산시간 시작점을 얻는다(61). 최소 출력 간격은 100000., 메시(mesh) 출력 플래그는 0이다(62–63). 조건·반복 원문: `if( .not. allocated(pos_ids) )then` (42), `if( (istran(6) + istran(7)) > 0 )then` (49), `else` (51). 계산·설정 원문: `DTSEDJ = DTSED` (50), `DTSEDJ = DT` (52), `local_debug = .true.` (56), `local_debug = .false.` (58), `TTDS = DSTIME(0)` (61), `freq_out_min  = 100000.` (62), `iwrite_pwmesh = 0` (63). 호출 원문: `call Det_Adjacent_Cells` (46). |
| 65–90 | 시작 시 16행 루틴 안. 활성 선박 수를 지우고 선박마다 시간과 유출 속도(efflux velocity)를 갱신한다(66–74). det_if_in_track 호출 뒤 항적(track) 안의 선박 수를 먼저 늘린다(76–80). det_pos_in_track과 interp_track을 호출한다(83·87). 동력이 0이거나 셀 번호가 2보다 작으면 선박 반복의 나머지를 건너뛴다(89). 조건·반복 원문: `do i = 1, total_ships` (67), `if( in_track )then` (79), `if( all_ships(i).power == 0.0 .or. all_ships(i).pos.cell < 2 ) cycle` (89). 계산·설정 원문: `nactiveships = 0` (66), `in_track = .FALSE.` (68), `track_id = 1` (69), `all_ships(i).pos.time = timeday` (72), `all_ships(i).efflux_vel = 0.0` (73), `nactiveships = nactiveships + 1` (80). 호출 원문: `call all_ships(i).det_if_in_track(track_id, in_track)` (76), `call all_ships(i).det_pos_in_track(track_id, pos_ids(i).prev, pos_ids(i).next)` (83), `call all_ships(i).interp_track(track_id, pos_ids(i).prev, pos_ids(i).next)` (87). |
| 91–117 | 시작 시 16행 루틴·67행 i 루프·79행 in_track 참 분기 안. ieffluxonly=0이면 setup_mesh와 calc_erosive_flux를 호출한다(91–96). else는 calc_velocity에 두 개의 10._RKD 좌표와 ieffluxonly를 전달한다(97–99). 디버그 코드는 주석이다(100–103). 출력 간격·현재 시각·동력/스냅숏(snapshot) 조건을 통과하면 setup_mesh(.false.)와 calc_erosive_flux(.false.)를 호출한다(107–116). ieffluxonly 분기를 닫는다(117). 조건·반복 원문: `if( ieffluxonly == 0 )then` (91), `else` (97), `if( all_ships(i).freq_out > 0. )then` (107), `if( timeday >= all_ships(i).timesnap )then` (108), `if( all_ships(i).power /= 0.0 .or. all_ships(i).nsnap == 0 )then` (109). 호출 원문: `call all_ships(i).setup_mesh(local_debug)` (93), `call all_ships(i).calc_erosive_flux(local_debug)` (96), `call all_ships(i).calc_velocity(10._RKD, 10._RKD, effvel, ieffluxonly)` (99), `call all_ships(i).setup_mesh(.false.)` (110), `call all_ships(i).calc_erosive_flux(.false.)` (113). |
| 118–129 | 시작 시 16행 루틴·67행 i 루프·79행 in_track 분기 안. 118행 else는 항적 밖일 때 prev=1·next=2로 되돌린다(118–122). 항적 분기 밖에서 양수 출력 간격의 최솟값을 갱신한다(125–127). 선박 반복을 닫는다(129). 조건·반복 원문: `else` (118), `if( all_ships(i).freq_out > 0. )then` (125). 계산·설정 원문: `pos_ids(i).prev = 1` (120), `pos_ids(i).next = 2` (121), `freq_out_min = min(all_ships(i).freq_out, freq_out_min)` (126). |
| 130–147 | 시작 시 16행 루틴 안. 활성 선박·ieffluxonly·퇴적물 수송 조건을 통과하면 셀별 1:NSEDS 침식(erosion)량을 0번째 열에 합한다(132–135). icalc_bl이 양수이면 소류사(bedload)량도 prop_ero의 0번째 열에 더하고 prop_bld 합계를 저장한다(136–141). DSTIME 차이를 TPROPW에 누적한다(144). 루틴 종료·마지막 빈 줄을 포함한다(146–147). 조건·반복 원문: `if( nactiveships > 0 .and. ieffluxonly == 0 .and. (istran(6) > 0 .or. istran(7) > 0) )then` (132), `do l = 2,la` (133), `if( icalc_bl > 0 )then` (136), `do l = 2,la` (137). 계산·설정 원문: `prop_ero(l,0) = sum(prop_ero(l,1:NSEDS))` (134), `prop_ero(l,0) = prop_ero(l,0) + sum(prop_bld(l,1:NSEDS))` (138), `prop_bld(l,0) = sum(prop_bld(l,1:NSEDS))` (139), `TPROPW = TPROPW + (DSTIME(0)-TTDS)` (144). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30–33: prev_id·next_id·start_time·end_time·final_track_pos_id는 선언 이후 이 파일의 실행문에서 사용되지 않는다.
- 27·91–99·107–113: ieffluxonly 주석은 양수 입력이 field/erosion 계산을 우회한다고 적는다. 양수 경로도 출력 시각 조건을 통과하면 setup_mesh와 calc_erosive_flux를 호출한다.
- 80·89: nactiveships 증가가 power 또는 cell에 따른 cycle보다 먼저 실행된다.
- 89·125–127: cycle이 실행되면 해당 선박은 freq_out_min 갱신에도 도달하지 않는다.
- 132–142: prop_ero(l,0)·prop_bld(l,0)의 합계 대입은 바깥 조건이 참일 때만 있다. 바깥 조건이 거짓일 때 합계를 지우는 else는 이 루틴에 없다.
