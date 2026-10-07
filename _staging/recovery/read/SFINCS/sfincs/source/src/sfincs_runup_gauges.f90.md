---
file: models/SFINCS/raw/source_code/sfincs/source/src/sfincs_runup_gauges.f90
lines: 188
sha256: ae7af29b792abb03d8419d01ffe5babb582a12b3faeec6aa1e18cc9923643ea3
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# sfincs_runup_gauges.f90 — 판독 구간 기록

구간은 1행부터 188행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | sfincs_runup_gauges 모듈·contains·빈 줄(1–4). `read_rug_file()`은 rug 파일을 읽는다는 주석과 sfincs_data·geometry·quadtree·sfincs_error/log 사용을 포함한다(5–15). 행·열·관측선·격자 인덱스·stat·최대 표본 수, 양 끝 좌표·표본 좌표·길이·간격, 길이 256 cdummy, ok를 선언한다(17–25). cross sections 파일 판독 주석(27) 뒤 nr_runup_gauges=0으로 초기화한다(29). |
| 31–61 | 시작 시 5행 read_rug_file 루틴 안. `if (rugfile(1:4) /= 'none') then` (31)에서 시작 로그(33), `ok = check_file_exists(obsfile, 'Run-up gauge rug file', .true.)` (35)을 수행한다. rugfile을 유닛 500으로 연다(39). `do while(.true.)` (40)의 이름 read(41) 뒤 `if (stat<0) exit` (42), 행·열 수 read(43) 뒤 `if (stat<0) exit` (44)를 검사한다. `if (nrows > 2) then` (45)이면 두 점만 허용하고 gauge를 건너뛴다는 경고를 쓴다(46). 조건 밖에서 `nr_runup_gauges = nr_runup_gauges + 1` (48)을 수행하고 `do irow = 1, nrows` (49)에서 행을 읽는다(50). rewind(53) 뒤 `if (nr_runup_gauges == 0) then` (55)이면 유효 gauge 없음 경고·return(57–58). 끝 주석을 포함한다(61). |
| 62–91 | 시작 시 5행 루틴·31행 rugfile 조건 안. nrpmx=0(64), `dxstep = 0.2 * dxyr(nref)` (66)로 표본 간격을 정한다. `do irug = 1, nr_runup_gauges` (68)에서 이름·행/열을 읽고 `if (stat<0) exit` (72)를 검사한다. 양 끝 두 점을 읽는다(73–74). `rdx = xru1 - xru0` (75), `rdy = yru1 - yru0` (76), `rlen = sqrt(rdx**2 + rdy**2)` (77), `nrpmx = max(nrpmx, int(rlen / dxstep) + 1)` (78)로 최대 표본 수를 구한다. 루프 종료·rewind(80–81) 뒤 runup_gauge_nm(nrpmx,nr_runup_gauges), 이름·표본 수 배열을 할당한다(83–85). nm/nrp는 0으로 초기화한다(87–88). 다음 polyline 루프 주석을 포함한다(90–91). |
| 92–109 | 시작 시 5행 루틴·31행 rugfile 조건 안. `do irug = 1, nr_runup_gauges` (92)에서 이름·행/열을 읽고 `if (stat<0) exit` (96)를 검사한다. 처음 두 꼭짓점만 쓴다는 주석(98) 뒤 두 좌표를 읽고(100–101) `runup_gauge_name(irug) = trim(cdummy)` (103)로 이름을 저장한다. `rdx = xru1 - xru0` (105), `rdy = yru1 - yru0` (106), `rlen = sqrt(rdx**2 + rdy**2)` (107), `runup_gauge_nrp(irug) = int(rlen / dxstep) + 1` (108)로 표본 수를 정한다. |
| 110–137 | 시작 시 5행 루틴·31행 rugfile 조건·92행 irug 루프 안. `do ip = 1, runup_gauge_nrp(irug)` (110)에서 `x = xru0 + (ip - 1) * dxstep * rdx / rlen` (112), `y = yru0 + (ip - 1) * dxstep * rdy / rlen` (113)로 표본 좌표를 구한다. `nmq = find_quadtree_cell(x, y)` (117)을 호출한다. `if (nmq > 0) then` (119)이면 runup_gauge_nm에 index_sfincs_in_quadtree(nmq)를 복사한다(123). 조건·표본·gauge 루프 종료(125–129), close(500)(131), 파일 조건·루틴 종료·빈 줄을 포함한다(133–137). |
| 138–188 | `get_runup_levels(zru)`은 sfincs_data를 사용하고 allocatable real*4 zru와 인덱스·임시 바닥고를 선언한다(138–147). zru를 gauge 수로 할당하고 `zru = -999.0` (151)로 기본값을 채운다(149–151). `do irug = 1, nr_runup_gauges` (153)·`do ip = 1, runup_gauge_nrp(irug)` (155)에서 저장 셀 nm를 얻는다(157). `if (subgrid) then` (159)은 subgrid_z_zmin에서 zbt를 복사한다(161). `else` (163)는 zb에서 복사한다(165). `if (zs(nm) > zbt + runup_gauge_depth) then` (169)이면 zru(irug)=zs(nm)(173)로 복사한다. `else` (175)는 수심이 문턱보다 작다는 주석만 가지며 `!exit` (179)는 주석 처리되어 있다. 조건·두 루프·루틴·모듈 종료와 빈 줄을 포함한다(181–188). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 31·35·39: 파일 조건과 open은 rugfile을 사용한다. check_file_exists의 파일 인수는 obsfile이다.
- 45–50·68–80·92–129: nrows>2 경고는 gauge를 건너뛴다고 적는다. 그 뒤 gauge 수는 조건 밖에서 증가한다. 첫 계수 루프는 nrows개 행을 소비한다. 뒤의 최대 표본 수·좌표 판독 루프는 두 좌표만 읽으며 나머지 꼭짓점을 소비하는 문장이 없다.
- 39·55–58·131: 유효 gauge 수가 0인 return은 close(500)보다 앞에 있다. 해당 return 분기에는 close가 없다.
- 66·77–78·107–113: 표본 수 계산은 dxstep으로 나눈다. 좌표 계산은 rlen으로 나눈다. 이 식 앞에 dxstep/rlen의 양수 여부를 검사하는 조건은 없다.
- 87·119–125·157–169: 셀 대응은 0으로 초기화하고 nmq>0일 때만 갱신한다. get_runup_levels는 nm를 얻은 뒤 nm>0 검사 없이 바닥고·zs를 참조한다.
- 153–184: get_runup_levels는 수심 조건을 만족할 때마다 zru를 현재 zs로 덮어쓴다. 이 루틴에는 max 누적이 없다. 얕은 점에서의 exit는 주석 처리되어 있다.
- 144·149: get_runup_levels의 zru 인수는 allocatable이며 intent(out) 선언이 없다. allocate(zru(...)) 앞에는 allocated 검사나 deallocate가 없다. 호출자의 배열 상태는 이 파일 판독 범위에서 확인하지 않았다.
