---
file: models/SFINCS/raw/source_code/sfincs/source/src/sfincs_bathtub.f90
lines: 216
sha256: 64bad655368b0df5ccd0fdb1134409a36c9796a5a6951806596c52e79811e93f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# sfincs_bathtub.f90 — 판독 구간 기록

구간은 1행부터 216행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | sfincs_bathtub 모듈(1), 격자 보간 인덱스 bathtub_i1/i2·가중치 bathtub_w1 선언(3–5). SnapWave 경계점 수, x/y/hs 배열, 경계 보간 i1/i2/w1 배열 선언(6–12). 배열은 allocatable이며 선언에 초기값이 없다. 빈 줄·contains·구분 주석(2·13–15). |
| 16–58 | initialize_bathtub 입구와 경계·가중치 생성 주석(16–19), sfincs_data·geometry·quadtree·sfincs_error·sfincs_log 사용, implicit none, 인덱스·가중치·파고·배정밀도 시간 선언(20–32). `if (bathtub_snapwave) then` (34) 안에서 변수 이름 중복 때문에 SnapWave 모듈을 직접 사용하지 않는다는 주석(36–37), `call read_snapwave_boundary_data()` (39). 경계점 수 nbnd로 보간 배열 3개 할당(43–45). `do ib = 1, nbnd` (49)에서 `call interp_segment(bathtub_snapwave_x_bwv, bathtub_snapwave_y_bwv, bathtub_snapwave_nwbnd, x_bnd(ib), y_bnd(ib), i1, i2, w1, w2)` (51), i1/i2/w1 저장(53–55), 루프 종료·주석(57–58). |
| 59–85 | 시작 시 16행 initialize_bathtub·34행 bathtub_snapwave 참 분기 안. bzs 시간별로 f*Hm0를 더하며 보통 f=0.2라는 주석(59). `do itb = 1, ntbnd` (61)에서 t_bnd를 real*8 t8에 복사(65), `call update_snapwave_boundary_data(t8)` (67). `do ib = 1, nbnd` (71)에서 저장 인덱스로 h1/h2·w1을 읽는다(73–75). `w2 = 1.0 - w1` (76), `zs_bnd(ib, itb) = zs_bnd(ib, itb) + bathtub_fac_hs * (w1 * h1 + w2 * h2)` (78). 두 루프·bathtub_snapwave 조건 종료 및 구분 주석(80–85). |
| 86–116 | 시작 시 16행 initialize_bathtub 안이며 SnapWave 조건 밖. np 크기의 격자 보간 배열 할당(88–90). `do ip = 1, np` (92)에서 `call interp_segment(x_bnd, y_bnd, nbnd, z_xz(ip), z_yz(ip), i1, i2, w1, w2)` (94), i1/i2/w1 저장(96–98), 루프 종료(100). meteo3d·wind·store_meteo·store_wind·store_wind_max·precip·patmos·snapwave·infiltration·store_velocity·store_maximum_velocity를 모두 .false.로 설정(102–112). 루틴 종료·빈 줄·주석(113–116). |
| 117–174 | bathtub_compute_water_levels(tloop) 입구와 sfincs_data·geometry·implicit none·지역변수 선언(117–131), `call system_clock(count0, count_rate, count_max)` (133). OpenMP private(nm,i1,i2,w1,w2), dynamic,256(135–137). `do nm = 1, np` (138)에서 i1/i2/w1 읽기(140–142), `w2 = 1.0 - w1` (143), `zbt = w1 * zst_bnd(i1) + w2 * zst_bnd(i2)` (145). `if (subgrid) then` (147)이면 `zs(nm) = max(subgrid_z_zmin(nm), zbt)` (149), `else` (151)는 `zs(nm) = max(zb(nm), zbt)` (153). 별도 `if (store_maximum_waterlevel) then` (157)이면 `zsmax(nm) = max(zsmax(nm), zs(nm))` (161). 조건·루프·병렬 종료(163–167), `!$acc update device( zs, zsmax )` (169), `call system_clock(count1, count_rate, count_max)` (171), `tloop = tloop + 1.0 * (count1 - count0) / count_rate` (172), 루틴 종료·구분 주석(173–174). |
| 175–200 | 빈 줄과 read_snapwave_boundary_data 입구(175–176), snapwave_data·snapwave_boundaries·sfincs_snapwave 사용(178–180). 입력 파일명 저장 설명과 `call read_snapwave_input()` (182–184), 경계 판독 설명과 `call read_boundary_data()` (186–188). nwbnd 크기의 x/y/hs 배열 할당(190–192), nwbnd와 x_bwv/y_bwv를 bathtub 전용 변수에 복사(194–196). 구분 주석·루틴 종료·빈 줄(197–200). |
| 201–216 | update_snapwave_boundary_data(tb) 입구(201), snapwave_data·snapwave_boundaries 사용·implicit none·real*8 tb 선언(203–208). `call update_boundary_points(tb, .true.)` (210), hst_bwv를 bathtub_snapwave_hs_bwv에 복사(212). 구분 주석·루틴 종료·빈 줄·모듈 종료(213–216). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 131·135–145: zbt를 지역 실수로 선언하고 OpenMP 루프에서 매 셀 대입한다. 명시된 private 목록에는 zbt가 없다.
- 51–55·76·94–98·143: interp_segment는 w1과 w2를 모두 반환하지만 저장 배열에는 w1만 넣는다. 후속 계산의 w2는 1.0-w1로 다시 계산한다.
- 43–45·88–90·190–192: 배열을 할당하는 문장 앞에 allocated 검사는 없다. 이 모듈 안에는 해당 배열의 deallocate 문장이 없다.
