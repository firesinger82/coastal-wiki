---
file: models/SFINCS/raw/source_code/sfincs/source/src/sfincs_bmi.f90
lines: 436
sha256: ec5ae2f36b87f852e7ad1abd05fe5ca69b03f73f7db7a1b47e66002fb271308a
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# sfincs_bmi.f90 — 판독 구간 기록

구간은 1행부터 436행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–55 | sfincs_bmi 모듈과 iso_c_binding·sfincs_lib·sfincs_data·sfincs_domain·sfincs_wave_enhanced_roughness 사용(1–7), implicit none·기본 private(9–10). 초기화·갱신·종료·변수 조회·시간 조회·바닥/거칠기 갱신·셀 조회 루틴 공개(14–30), 길이 상수 공개(34–39). C 바인딩 선언과 초기값은 `integer(c_int), bind(C, name="BMI_LENVARADDRESS") :: BMI_LENVARADDRESS = 64` (41), `integer(c_int), bind(C, name="BMI_LENVARTYPE") :: BMI_LENVARTYPE = 64` (43), `integer(c_int), bind(C, name="BMI_LENGRIDTYPE") :: BMI_LENGRIDTYPE = 64` (45), `integer(c_int), bind(C, name="BMI_LENCOMPONENTNAME") :: BMI_LENCOMPONENTNAME = 64` (47), `integer(c_int), bind(C, name="BMI_LENVERSION") :: BMI_LENVERSION = 256` (49), `integer(c_int), bind(C, name="BMI_LENERRMESSAGE") :: BMI_LENERRMESSAGE = 1024` (51). 문자열 최대 길이 주석과 DIR$ DLLEXPORT 지시문(41–52), 빈 줄·구분 주석·contains(2·8·11–13·31–33·40·53–55). |
| 56–94 | initialize C 바인딩 함수는 BMI·외부유량 플래그를 .true.로 설정(59–60), `ierr = sfincs_initialize()` (61). update C 바인딩 함수(65)는 한 시간 간격 실행 주석(69), `unused_t = -1.0` (70), `ierr = sfincs_update(unused_t)` (71). update_until C 바인딩 함수(75)는 value인 real(c_double) t_target을 받는다(77), `delta_t = t_target - t` (82), `ierr = sfincs_update(delta_t)` (83). finalize C 바인딩 함수(87)는 `ierr = sfincs_finalize()` (91). 각 함수 ierr 선언·DLLEXPORT 지시문·종료·빈 줄 포함(57–58·62–64·66–68·72–74·76·78–81·84–86·88–90·92–94). |
| 95–130 | get_value_ptr C 바인딩 입구·C 문자열·c_ptr·오류값·문자열 길이 선언(95–102), ierr=0(104). `c_strlen = strlen(c_var_name, BMI_LENVARADDRESS)` (106), `var_name = char_array_to_string(c_var_name, c_strlen)` (107). `select case(var_name)` (109). `case("z_xz")` (110)는 `c_data = c_loc(z_xz)` (111), `case("z_yz")` (112)는 `c_data = c_loc(z_yz)` (113), `case("zs")` (114)는 `c_data = c_loc(zs)` (115), `case("zb")` (116)는 `c_data = c_loc(zb)` (117), `case("subgrid_z_zmin")` (118)는 `c_data = c_loc(subgrid_z_zmin)` (119), `case("qext")` (120)는 `c_data = c_loc(qext)` (121), `case("uorb")` (122)는 `c_data = c_loc(uorb)` (123). `case default` (124)는 c_null_ptr와 ierr=-1(125–126). select·함수 종료·빈 줄(127–130). |
| 131–158 | get_var_shape C 바인딩 입구(131–132), 길이 6 정수 var_shape와 문자열·오류값 선언(134–137), ierr=0(139), char_array_to_string와 strlen 호출(141), `var_shape = (/0, 0, 0, 0, 0, 0/)` (142). `select case(var_name)` (144), `case("z_xz", "z_yz", "zs", "zb", "uorb")` (145)는 `var_shape(1) = size(zs)` (146). `case("subgrid_z_zmin")` (147)는 `var_shape(1) = size(subgrid_z_zmin)` (148). `case("z_index_z_n", "z_index_z_m")` (149)는 `var_shape(1) = size(z_index_z_n)` (150). `case("qext")` (151)는 `var_shape(1) = size(qext)` (152). `case default` (153)는 ierr=-1(154). select·함수 종료·빈 줄·지시문 포함(133·138·140·143·155–158). |
| 159–186 | get_var_type C 바인딩 함수와 C형식 출력 배열·길이 BMI_LENVARADDRESS-1 및 BMI_LENVARTYPE-1 문자열 선언(159–167). ierr=0, strlen·char_array_to_string 호출(169–170). `select case(var_name)` (172), `case("z_xz", "z_yz", "zb", "subgrid_z_zmin", "qext", "uorb")` (173)는 type_name="float"(174), `case("zs")` (175)는 "double"(176), `case("z_index_z_n", "z_index_z_m")` (177)는 "integer"(178), `case default` (179)는 ierr=-1(180). select 종료(181) 뒤 `c_type = string_to_char_array(trim(type_name), len(trim(type_name)))` (183). 함수 종료·빈 줄 포함(184–186). |
| 187–208 | get_var_rank C 바인딩 함수와 출력 rank·오류값·문자열 선언(187–194), ierr=0과 문자열 변환(196–198). `select case(var_name)` (200), `case("z_xz", "z_yz", "zs", "zb", "subgrid_z_zmin", "qext", "uorb")` (201)는 rank=1(202). `case default` (203)는 ierr=-1(204). select·함수 종료·빈 줄(205–208). |
| 209–236 | set_logical C 바인딩 함수와 입력 문자열·ival 배열·오류값·bval 선언(209–215), ierr=0, strlen·char_array_to_string 호출(217–219). `if (ival(1) == 0) then` (221)이면 bval=.false.(222), `else` (223)는 .true.(224). `select case(flag_name)` (227), `case("qext")` (228)는 use_qext에 bval 복사(229), 로그 문장은 주석 처리(230). `case default` (231)는 ierr=-1(232). 조건·select·함수 종료·구분 주석·빈 줄 포함(225–226·233–236). |
| 237–276 | get_start_time(237–245)은 t0를 tstart에 복사(242), get_end_time(247–255)은 t1을 tend에 복사(252), get_time_step(257–265)은 dt를 deltat에 복사(262), get_current_time(267–275)은 t를 tcurrent에 복사(272). 모두 C 바인딩과 DLLEXPORT 지시문, real(c_double) intent(out) 시간·정수 ierr 선언을 갖고 ierr=0을 반환한다(243·253·263·273). 함수 사이 빈 줄과 함수 종료 포함. |
| 277–298 | update_zbuv C 바인딩 함수(277)는 uv점 바닥 갱신 주석(278), `call compute_zbuvmx()` (281), ierr=0(282). update_apparent_roughness C 바인딩 함수(286)는 uorb 갱신 뒤 호출해야 한다는 주석(291), `call update_wave_enhanced_roughness()` (293), ierr=0(295). 각 함수 선언·DLLEXPORT·구분 주석·종료·빈 줄 포함(279–280·283–285·287–290·292·294·296–298). |
| 299–317 | get_sfincs_cell_index C 바인딩 함수, 1부터 시작하는 셀 인덱스 주석과 quadtree 사용(299–302). 배정밀도 x/y·정수 indx·ierr·nmq 선언(304–308). `nmq = find_quadtree_cell(real(x, kind=4), real(y, kind=4))` (311), `indx = index_sfincs_in_quadtree(nmq)` (312), ierr=0(314). 함수 종료·주석·빈 줄(303·309–310·313·315–317). |
| 318–350 | get_sfincs_cell_indices C 바인딩 함수·quadtree·길이 n의 x/y/indx·value n·지역변수 선언(318–329). `do iq = 1, n` (331)에서 `nmq = find_quadtree_cell(real(x(iq), kind=4), real(y(iq), kind=4))` (333), `if (nmq > 0.0) then` (335)이면 `indx(iq) = index_sfincs_in_quadtree(nmq)` (337), `else` (339)는 indx(iq)=0(341). 조건·루프 종료(343–345), ierr=0(347), 함수 종료·주석·빈 줄(346·348–350). |
| 351–374 | get_sfincs_cell_area C 바인딩 함수와 입력 정수 indx·출력 배정밀도 area·정수 ierr·real*4 a 선언(351–357). `if (crsgeo) then` (359)이면 `a = cell_area_m2(indx)` (361), `else` (363)는 `a = cell_area(z_flags_iref(indx))` (365). 조건 밖 `area = real(a, kind=8)` (369), ierr=0(371). 구분 주석·함수 종료·빈 줄 포함(358·360·362·364·366–368·370·372–374). |
| 375–388 | 마지막 오류를 문자 배열로 반환한다는 주석과 get_last_bmi_error C 바인딩 함수(375–380). 출력 길이 BMI_LENERRMESSAGE의 C 문자 배열·ierr 선언(381–382). `c_error = string_to_char_array("error handling not implemented", 30)` (384), ierr=0(385). 함수 종료·빈 줄(383·386–388). |
| 389–406 | 널 문자를 제외한 문자열 길이 주석과 pure strlen(char_array,max_len) 함수(389–391), 크기 max_len C 문자 배열·정수 결과/인덱스 선언(392–395), string_length=0(397). `do i = 1, size(char_array)` (398), `if (char_array(i) .eq. C_NULL_CHAR) then` (399)이면 `string_length = i - 1` (400), exit(401). 조건·루프·함수 종료·빈 줄(402–406). |
| 407–420 | C 문자열을 Fortran 문자열로 바꾸는 주석과 pure char_array_to_string(char_array,length) 함수(407–409), 길이 인수·입력 배열·결과 문자열·인덱스 선언(410–413). `do i = 1, length` (415)에서 각 문자를 f_string(i:i)에 복사(416). 루프·함수 종료·빈 줄(417–420). |
| 421–436 | Fortran 문자열을 C 문자열로 바꾸는 주석과 pure string_to_char_array(string,length) 함수(421–423), 길이 인수·입력 문자열·크기 length+1 출력 배열·인덱스 선언(424–427). `do i = 1, length` (429)에서 각 문자를 c_array(i)에 복사(430), 루프 종료(431). `c_array(length + 1) = C_NULL_CHAR` (432)로 종단 널을 붙인다. 함수 종료·빈 줄·모듈 종료(433–436). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10·14–30·209·378: 기본 접근성은 private이다. set_logical과 get_last_bmi_error에는 C 바인딩이 있지만 공개 루틴 목록에는 없다.
- 82–83: update_until은 t_target-t를 계산한 뒤 그대로 sfincs_update에 전달한다. 이 함수 안에는 목표 시간과 현재 시간의 대소 조건이 없다.
- 109–127·144–155·172–181·200–205: z_index_z_n/z_index_z_m은 shape와 type 조회의 case에 있다. 이 두 이름은 포인터와 rank 조회의 case에는 없다.
- 164–165·179–183: get_var_type의 default는 ierr만 설정한다. type_name 선언에는 초기값이 없으며 select 종료 뒤 type_name으로 출력 문자열을 만든다.
- 191·203–205: get_var_rank의 default는 ierr만 설정한다. 해당 분기에는 intent(out) rank 대입이 없다.
- 311–312·333–343: 단일 셀 조회는 nmq를 검사하지 않고 배열 인덱스로 쓴다. 여러 셀 조회는 nmq>0.0을 검사하고 불성립 시 0을 반환한다.
- 354–369: 셀 면적은 real*4 지역변수 a에 먼저 저장하고 kind=8로 변환한다. 이 함수 안에는 indx 범위 검사가 없다.
- 384–385: 마지막 오류 조회는 고정 문자열 error handling not implemented와 ierr=0을 반환한다.
- 397–403: strlen은 결과를 0으로 시작한다. 배열 안에서 C_NULL_CHAR를 찾았을 때만 i-1로 바꾸며, 널 문자를 찾지 못한 경우의 추가 대입은 없다.
