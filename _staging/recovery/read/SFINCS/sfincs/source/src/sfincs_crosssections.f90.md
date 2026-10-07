---
file: models/SFINCS/raw/source_code/sfincs/source/src/sfincs_crosssections.f90
lines: 178
sha256: 31bd577e50b20e7f6f3f489a3087fcd290f6a454ebba8c98066e67f10c94ce2f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# sfincs_crosssections.f90 — 판독 구간 기록

구간은 1행부터 178행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–39 | sfincs_crosssections 모듈, sfincs_log·sfincs_error 사용·contains(1–6). read_crs_file 입구와 crs 판독 주석(8–11), sfincs_data·geometry·quadtree·implicit none(12–16). 인덱스·파일 크기/상태·실수 dummy/각도·길이 256 cdummy·파일 검사 logical 선언(18–26). xcrs/ycrs와 uv_indices/vertices는 allocatable 1차원 배열, xp/yp는 길이 2 배열(28–33). ncrs/nrcrosssections=0(37–38). 빈 줄·구분 주석·판독 주석 포함(2·5·7·9·15·17·19·25·27·34–36·39). |
| 40–69 | 시작 시 8행 read_crs_file 안. `if (crsfile(1:4) /= 'none') then` (40)이면 write_log(42), check_file_exists(...,.true.)(44), 단위 500으로 파일 open(48). `do while(.true.)` (49)에서 이름 판독(50), `if (stat<0) exit` (51), nrows/ncols 판독(52), `if (stat<0) exit` (53), `ncrs = ncrs + 1` (54). `do irow = 1, nrows` (55)에서 dummy로 점 행 건너뛰기(56). rewind(59), nrcrosssections 복사(61), crs_uv_index(1000,ncrs)·crs_idir(1000,ncrs)·crs_nr(ncrs)·namecrs(ncrs) 할당(63–66). 구분 주석·polyline 루프 안내(67–69). |
| 70–98 | 시작 시 8행 read_crs_file·40행 crsfile 참 분기 안. `do icrs = 1, ncrs` (70), crs_nr와 nr=0(72–73), 이름과 nrows/ncols를 iostat로 판독(75–76), `if (stat<0) exit` (77). xcrs/ycrs(nrows) 할당(78–79), `do irow = 1, nrows` (80)에서 좌표 판독(81). namecrs에 이름 저장(84), `call find_uv_points_intersected_by_polyline(uv_indices, vertices, nr_points, xcrs, ycrs, nrows)` (86). `do iuv = 1, nr_points` (90)에서 indx/irow 복사(92–93), `nr                     = nr + 1` (95), crs_nr와 crs_uv_index 저장(96–97), 구분 주석(98). |
| 99–129 | 시작 시 8행 read_crs_file·40행 crsfile 참 분기·70행 icrs 루프·90행 iuv 루프 안. 양쪽 수위점 nm/nmu 읽기(101–102). `phiuv = atan2(z_yz(nmu) - z_yz(nm), z_xz(nmu) - z_xz(nm))` (104), `phic  = atan2(ycrs(irow + 1) - ycrs(irow), xcrs(irow + 1) - xcrs(irow))` (105), `dphi  = phiuv - phic` (106). `if (dphi<0.0)  dphi = dphi + 2*pi` (107), `if (dphi>2*pi) dphi = dphi - 2*pi` (108). `if (dphi<=pi) then` (110)이면 crs_idir=1(111), `else` (112)는 -1(113). 조건·iuv 루프 종료(114–116), xcrs/ycrs 해제(118–119), icrs 루프 종료·close(121–123), crsfile 조건·루틴 종료·빈 줄(125–129). |
| 130–178 | get_discharges_through_crosssections(qq) 입구, sfincs_data·implicit none, allocatable 실수 qq와 인덱스·횡단 폭 선언(130–139). qq(nrcrosssections) 할당·0 초기화(141–143). `do icrs = 1, nrcrosssections` (145), `do ip = 1, crs_nr(icrs)` (147)에서 교차 uv 인덱스·세분화 수준·방향(0=u,1=v) 복사(149–151). `if (iuv==0) then` (153)이면 dxycrs=dyrm(iref)(157). `else` (159) 안에서 `if (crsgeo) then` (163)이면 `dxycrs = 1.0 / dxminv(indx)` (164), `else` (165)는 dxycrs=dxrm(iref)(166). 방향 조건 밖 `qq(icrs) = qq(icrs) + q(indx)*crs_idir(ip, icrs)*dxycrs` (171). 두 루프·루틴·모듈 종료·빈 줄·구분 주석(173–178). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 63–64·90–97: 단면당 저장 배열 첫 차원은 1000으로 고정되어 있다. 교차점 루프에는 nr<=1000 검사 조건이 없다.
- 49–58·75–77: iostat 검사 조건은 stat<0이다. stat>0을 처리하는 분기는 없다. 두 번째 판독의 이름 read 뒤에는 별도 상태 검사 없이 다음 read가 이어진다.
- 18·30–31·52·76: read_crs_file의 ip와 길이 2 xp/yp는 선언 이후 사용되지 않는다. ncols는 파일에서 읽지만 뒤 계산에 참조되지 않는다.
- 93·105: 반환 vertices 값을 irow로 사용하고 각도식에서 irow+1 좌표를 참조한다. 이 블록 안에는 irow 범위 검사가 없다.
- 136·141–143: qq는 allocatable 인수이며 호출 때 할당한다. 할당 전 allocated 검사나 기존 qq 해제 문장은 이 루틴에 없다.
