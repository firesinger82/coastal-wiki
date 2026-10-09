---
file: models/ADCIRC/raw/source_code/adcirc/util/build12.F
lines: 193
sha256: 7f3949c5ed0a6a230ba0cf5544fb2cd8970b2b34ae7d471a9d2cd8821535f7c1
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# build12.F — 판독 구간 기록

구간은 1행부터 193행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–42 | ADCIRC 이름·1994–2025 저작권·LGPL 3 이상·무보증 머리말(1–19). `program build12` 시작(20). 주석은 fort.13으로 fort.12와 fort.21을 구성하는 도구이며 vjp 8/1/2006이라고 적는다(21–24). implicit none과 격자(mesh) 크기·반복·속성(attribute) 개수·노드(node)·임시 변수·기본값 선언(25–32). 속성명 상수는 primitive_weighting_in_continuity_equation·mannings_n_at_sea_floor·surface_submergence_state·surface_canopy_coefficient·surface_directional_effective_roughness_length·sea_surface_height_above_geoid이다(33–38). x/y/dp와 초기 침수 상태(submergence state) startdry·canopy 계수(canopy coefficient) vcanopy·방향별 유효 거칠기 길이(directional effective roughness length) z0land·마찰(friction) fric 배열 선언·빈 줄(39–42). |
| 43–55 | 시작 시 20행 build12 프로그램 안. fort.14를 열고 격자명·ne·np를 읽는다(43–45). x/y/dp를 np 크기로 할당한다(47). `do i=1,np` (49)에서 입력 노드 번호를 idumy로 읽고 x(i)·y(i)·dp(i)를 읽는다(50). 루프 종료·파일 닫기(51–52). startdry·vcanopy·fric을 np 크기로, z0land를 np×12로 할당한다(54). 빈 줄(55). |
| 56–76 | 시작 시 20행 프로그램 안. 변수 설명자(descriptor) 판독 주석(56–58). fort.13을 열고 agrid2·np·nattr을 읽으며 로그를 출력한다(60–66). `do i=1, nattr` (67)에서 attr, 단위 문자열 inline, 노드당 값 개수 idumy를 읽고 출력한다(68–75). 빈 줄(76). 이 구간에서 속성 i 루프를 열어 둔다. |
| 77–103 | 시작 시 20행 프로그램·67행 속성 i 루프 안. `if (trim(attr).eq. prim_weight) then` (77)은 prim_weight_def 읽기·로그(78–79). `elseif (trim(attr).eq. mannings) then` (81)은 mannings_def(82–83). `elseif (trim(attr).eq. surface_substate) then` (85)은 surface_substate_def(86–87). `elseif (trim(attr).eq. surface_canopy) then` (89)은 surface_canopy_def(90–91). `elseif (trim(attr).eq. surface_derl) then` (93)은 surface_derl_def(1:12)를 읽는다(94). 이 분기의 출력문은 `print *, surface_derl(1:12)` (96). `elseif (trim(attr).eq. sea_surface_hag) then` (98)은 sea_surface_hag_def 읽기·로그(99–100). 조건·i 루프 종료·빈 줄(101–103). |
| 104–136 | 시작 시 20행 프로그램 안. 값 판독 주석과 `do i=1, nattr` (108), attr 읽기·로그(109–110). `if (trim(attr).eq. prim_weight) then` (111)은 ncount를 읽고 `do j=1, ncount` (114)에서 각 값을 문자열 inline으로 읽어 넘긴다(115). `elseif (trim(attr).eq. mannings) then` (117)은 `do j=1, np` (118)의 `fric(j) = mannings_def` (119)로 기본값을 채운다. ncount 읽기 뒤 `do j=1, ncount` (123)에서 inode·value를 읽고 fric(inode)에 value를 복사한다(124–125). `elseif (trim(attr).eq. surface_substate) then` (127)은 `do j=1, np` (128)의 `startdry(j) = surface_substate_def` (129)로 기본값을 채운다. ncount 읽기 뒤 `do j=1, ncount` (133)에서 inode·value를 읽지만 저장문은 `startdry(inode) = 1.0` (135). j 루프 종료(136). 바깥 i 루프와 속성 분기는 이어진다. |
| 137–167 | 시작 시 20행 프로그램·108행 i 루프·111행에서 시작한 속성 if/elseif 분기 안. `elseif (trim(attr).eq. surface_canopy) then` (137)은 `do j=1, np` (138)의 `vcanopy(j) = surface_canopy_def` (139)로 기본값을 채운다. ncount 읽기 뒤 `do j=1, ncount` (143)에서 inode·value를 읽고 vcanopy(inode)에 value를 복사한다(144–145). `elseif (trim(attr).eq. surface_derl) then` (147)은 `do j=1, np` (148)의 `z0land(j,1:12) = surface_derl_def(1:12)` (149). ncount 읽기 뒤 `do j=1, ncount` (153)에서 inode와 그 노드의 12방향 값을 직접 읽는다(154). `elseif (trim(attr).eq. sea_surface_hag) then` (156)은 ncount를 읽는다(157). 이 분기 안 `if (ncount .gt. 0) then` (159)이면 `do j=1, ncount` (160)에서 문자열 inline으로 값을 읽어 넘긴다(161). 내부 조건·속성 조건·i 루프 종료 및 close(13)·빈 줄(163–167). |
| 168–179 | 시작 시 20행 프로그램 안. fort.12 작성 주석·로그·open(168–171). agrid2와 ne·np를 쓴다(172–173). `do i=1,np` (174)에서 I8,16E17.9 형식으로 i·x(i)·y(i)·startdry(i), j=1..12의 z0land(i,j), vcanopy(i)를 쓴다(175–176). 루프 종료·close(12)·빈 줄(177–179). dp는 이 출력 목록에 없다. |
| 180–193 | 시작 시 20행 프로그램 안. fort.21 작성 주석·로그·open(180–183). fort.14에서 읽은 agrid를 머리말로 쓴다(184). `do i=1, np` (185)에서 I8,E17.9 형식으로 i·fric(i)를 쓴다(186). 루프 종료·close(21)·주석·stop·프로그램 종료·마지막 빈 줄들(187–193). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 45–54·63·173–176: 배열 크기는 fort.14의 np로 할당한다. fort.13의 np를 같은 변수에 다시 읽는다. 두 np를 비교하는 조건문은 이 파일에 없다. fort.12 머리말은 fort.14의 ne와 다시 읽은 np를 함께 쓴다.
- 54·77–101·117–150·175–186: 네 출력 속성 배열의 기본값 대입은 해당 속성이 발견된 분기 안에만 있다. 할당 직후 공통 초기화문과 필수 속성 존재 검사는 없다. fort.12·fort.21 출력은 해당 속성 발견 여부를 검사하지 않는다.
- 74–75·94·154: 노드당 값 개수를 idumy로 읽고 출력한다. 방향별 거칠기 길이는 idumy와 무관하게 1:12 범위로 읽는다.
- 94–96: surface_derl_def(1:12)를 읽는다. 다음 출력문은 실수 기본값 배열이 아닌 속성명 문자열 surface_derl의 1:12 부분을 출력한다.
- 134–135: 침수 상태의 inode와 value를 읽는다. startdry(inode)에 저장하는 값은 value가 아닌 1.0이다.
- 77–101·111–164: 두 속성 처리 조건은 여섯 이름만 포함한다. 그 밖의 속성에 대한 else 분기와 기본값·값 블록을 건너뛰는 공통 읽기 문장은 없다.
- 27–30·50·78·99·111–116·156–163·175–186: dp는 입력에서 채우지만 출력 목록에 없다. prim_weight_def와 sea_surface_hag_def는 읽기·로그에 사용한다. 두 속성의 비기본값 블록은 문자열로 읽어 넘긴다.
- 26–32: ne2·np2·ntot·xdumy·ydumy·agrid3는 선언 이후 실행문에서 사용되지 않는다.
