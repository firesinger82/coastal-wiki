---
file: models/ADCIRC/raw/source_code/adcirc/util/build13.F
lines: 205
sha256: 7cdb29309126606cc3f856e15459232391f6cfc632c200194bc93c85f2850f56
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# build13.F — 판독 구간 기록

구간은 1행부터 205행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | ADCIRC 이름·1994–2025 저작권·LGPL 3 이상·무보증 머리말(1–19). `program build13` 시작·implicit none(20–21). fort.12·fort.21 존재 플래그, 격자(mesh) 이름·크기·반복·임시 좌표와 iz0·수심(depth) dp·침수 상태(submergence state) startdry·canopy 계수(canopy coefficient) vcanopy·방향별 거칠기 길이(directional roughness length) z0land·tau0var·마찰(friction) fric 배열 선언(22–28). 주석은 ADCIRC v46용 fort.13 구성 도구이며 vjp 9/1/2006이라고 적는다(30–33). 빈 줄(34). |
| 35–63 | 시작 시 20행 build13 프로그램 안. fort.14에서 agrid·ne·np를 읽고 dp(np)를 할당한다(35–38). `do i=1,np` (39)에서 노드 번호·좌표는 임시 변수로, 수심은 dp(i)로 읽는다(40). 루프 종료·close(14)(41–42). fort.12 존재 여부 확인(44). `if (has_dry)  then` (45)이면 파일을 열고 agrid2·ne2·np2를 읽으며 startdry·vcanopy·z0land(np,12)·iz0(np)를 할당한다(46–49). `do i=1,np` (50)에서 임시 번호·좌표·startdry·12방향 z0land·vcanopy를 읽고 닫는다(51–54). tau0var(np) 할당(56), `do i=1,np` (57). 설정문은 `if(dp(i).le.10.0d0) tau0var(i)=0.02d0` (58), `if(dp(i).gt.10.0d0) tau0var(i)=0.005d0` (59), `if(startdry(i).lt.-60000.0d0) tau0var(i)=0.03d0` (60). 마지막 조건이 참이면 앞 수심별 대입을 덮어쓴다. 루프·has_dry 조건 종료·빈 줄(61–63). |
| 64–80 | 시작 시 20행 프로그램 안. fort.21 읽기 주석과 존재 여부 확인(64–66). `if (has_fric) then` (67)이면 파일 열기·fric(np) 할당·agrid3 읽기(68–70). `do i=1, np` (71)에서 입력 번호를 idumy로 읽고 fric(i)를 채운다(72). 루프·파일·조건을 닫는다(73–75). 변수 설명자(descriptor) 작성 주석·빈 줄(77–80). |
| 81–95 | 시작 시 20행 프로그램 안. fort.13을 열고 trim(agrid2)와 np를 쓴다(81–83). `if (has_dry .and. has_fric) then` (84)은 속성(attribute) 개수 6 출력(85). `elseif (has_dry .and. .not.has_fric) then` (86)은 5 출력(87). `elseif (has_fric .and. .not.has_dry) then` (88)은 1 출력(89). `else` (90)는 fort.12 또는 for.21을 찾지 못했다는 로그·stop(91–92). 조건 종료·빈 줄들(93–95). |
| 96–123 | 시작 시 20행 프로그램 안. `if (has_dry) then` (96)이면 다섯 속성 설명자를 쓴다. sea_surface_height_above_geoid는 단위 m·노드(node)당 값 1·기본값 `write(13,'(A7)')  "0.36576"` (100), surface_submergence_state는 단위 행 정수 1·값 개수 1·`write(13,'(A3)')  "0.0"` (105). surface_canopy_coefficient는 단위 행 정수 1·값 개수 1·`write(13,'(A4)')  " 1.0"` (110). primitive_weighting_in_continuity_equation은 단위 행 정수 1·값 개수 1·`write(13,'(A4)')  "0.0"` (115). surface_directional_effective_roughness_length는 단위 m·노드당 값 12(117–119). 기본값 출력의 원문 줄은 `write(13,'(A)')` (120), `&  "0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0 0.0  0.0"` (121). 조건 종료·빈 줄(122–123). |
| 124–134 | 시작 시 20행 프로그램 안. `if (has_fric) then` (124)이면 mannings_n_at_sea_floor 설명자를 출력한다(125). 단위 m·노드당 값 1(126–127). 기본값은 `write(13,'(A4)')  "0.0"` (128). 조건 종료·빈 줄·값 작성 주석(129–134). |
| 135–151 | 시작 시 20행 프로그램 안. `if (has_dry) then` (135). sea_surface_height_above_geoid 이름과 비기본 노드 수 0을 쓴다(137–139). surface_submergence_state 이름과 ntot=0 초기화(141–143). `do i=1, np` (144)에서 `if(startdry(i).eq.-88888.0d0) ntot = ntot+1` (145). 개수 출력 뒤 `do i=1, np` (148)에서 `if(startdry(i).eq.-88888.0d0) write(13,'(I7,2X,F3.1)')  i,1.0` (149). 루프 종료·빈 줄(150–151). has_dry 조건은 이어진다. |
| 152–169 | 시작 시 20행 프로그램·135행 has_dry 참 분기 안. canopy 이름·ntot=0(152–154). `do i=1, np` (155)에서 `if(vcanopy(i).ne.1.0d0) ntot = ntot+1` (156). 개수 출력(158) 뒤 `do i=1, np` (159)에서 `if(vcanopy(i).ne.1.0d0) write(13,'(I7,F4.1)') i,0.0` (160). primitive_weighting_in_continuity_equation 이름과 np를 출력한다(163–165). `do i=1,np` (166)에서 각 노드 번호·tau0var(i)를 I8,F8.3으로 쓴다(167). 루프 종료·빈 줄(168–169). |
| 170–191 | 시작 시 20행 프로그램·135행 has_dry 참 분기 안. 방향별 유효 거칠기 이름·ntot=0(170–172). `do i=1, np` (173)에서 iz0(i)=0(174), `do j=1, 12` (175), `if(z0land(i,j).ne.0.0d0) then` (176)이면 iz0(i)=1(177), `ntot = ntot+1` (178), exit(179). 조건·j/i 루프 종료(180–182). ntot 출력(183). `do i=1, np` (184) 안 `if (iz0(i).eq.1) then` (185)이면 I7,12E16.8 형식으로 노드 번호와 12방향 값을 쓴다(186). 조건·루프 종료(187–188). 빈 줄·has_dry 조건 종료·빈 줄(189–191). |
| 192–205 | 시작 시 20행 프로그램 안. `if (has_fric) then` (192)이면 mannings_n_at_sea_floor 이름과 np를 쓴다(194–196). `do i=1, np` (197)에서 I7,E16.8 형식으로 i·fric(i)를 출력한다(198). 루프·조건 종료·빈 줄(199–202). close(13)·stop·프로그램 종료(203–205). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 45–48·81–89: agrid2는 has_dry 분기에서 fort.12의 머리말을 읽을 때만 채운다. fort.13 머리말은 has_dry 검사 없이 agrid2를 쓴다. has_fric만 참인 속성 개수 분기도 있다.
- 37·48–52·71–72: fort.12의 ne2·np2를 읽지만 fort.14의 ne·np와 비교하지 않는다. fort.12와 fort.21 읽기 반복 범위는 fort.14의 np이다. 입력 노드 번호는 idumy에 읽고 배열 위치는 반복 번호 i를 사용한다.
- 58–60·145–149: tau0var의 침수 상태 조건은 startdry<-60000이다. 침수 상태 비기본값 출력 조건은 startdry=-88888이다.
- 58–60: tau0var는 수심 10.0 경계에서 0.02 또는 0.005로 설정한다. startdry 조건이 참이면 0.03으로 덮어쓴다. 세 계수와 수심 경계는 실행문에 고정되어 있다.
- 100·138–139: sea_surface_height_above_geoid의 기본값은 문자열 0.36576으로 고정한다. 이 속성의 비기본 노드 수는 0으로 출력한다.
- 156–160: vcanopy가 1.0과 다른 노드를 센다. 해당 노드의 출력 값은 입력 vcanopy(i)가 아닌 0.0이다.
- 49·52·119–121·175·186: 방향별 거칠기 배열 크기·입력·설명자·검색·출력의 방향 개수는 12로 고정되어 있다.
- 125–128: mannings_n_at_sea_floor 설명자의 단위 문자열은 m이다. 기본값 문자열은 0.0이다.
