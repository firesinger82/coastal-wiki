---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Propwash/Mod_Position_Cell.f90
lines: 112
sha256: d6a0b8e7d1c1bf75b1af5a04cdd29ca1fa34594648e4c8e72e39d3e45303b5b2
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Mod_Position_Cell.f90 — 판독 구간 기록

구간은 1행부터 112행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–45 | EFDC+·GPLv2·저작권 머리말(1–8). Mod_Position_Cell 시작(9), GLOBAL의 RKD/RK4·MPI 보조·Mod_Position 사용(11–13), implicit none·기본 private·position_cell 공개(15–18). position_cell은 position을 확장(20–21). cell·sub_domain_id 기본값 0, freq_out·speed·course·heading·draft·rps·power 기본값 0.0(23–31). 출력 빈도는 양수이면 선박 정의값을 덮고, speed는 m/s·draft는 m라는 주석(25–29). power 주석 범위는 0..1 최대 출력 비율, 음수 -1..0 최대 rps 비율, -999는 선박 속성으로 계산하는 TBD(31–33). write_out_cell 결합·형식 종료·생성자 인터페이스(interface)·모듈 contains(34–45). 원문: `Integer(kind = RK4) :: cell          = 0     !< L cell index the ship is in` (23); `Integer(kind = RK4) :: sub_domain_id = 0     !< sub-domain the ship currently belongs in` (24); `real(kind = rkd)    :: freq_out      = 0.0   !< If > 0, overwrites the ship defined output freqency` (25); `real(kind = rkd)    :: speed         = 0.0   !< [meters/second]` (26); `real(kind = rkd)    :: course        = 0.0   !< Compass direction the ship is moving toward` (27); `real(kind = rkd)    :: heading       = 0.0   !< Compass direction the ship is pointed` (28); `real(kind = rkd)    :: draft         = 0.0   !< Draft below water (used with prop_offset to set shaft depth) [meters]` (29); `real(kind = rkd)    :: rps           = 0.0   !< Applied revolutions per second` (30); `real(kind = rkd)    :: power         = 0.0   !< Applied power:  0.0 to  1.0:  Fraction of max_power` (31). |
| 46–85 | 시작 시 9행 Mod_Position_Cell 안. 사용자 지정 생성자(constructor) 주석과 position_cell_constructor 시작(46–53). x_position·y_position·curr_time 입력, 선택 인수 test·지역 cell 선언(55–61). 좌표와 시각을 self에 복사(63–65). present(test)이면 테스트용으로 self.cell·self.sub_domain_id=0(68–70). else는 get_nearest_cell 호출(73). self.cell<2이면 STOPP를 경고 문자열과 호출(76–77), else는 get_subdomain_id로 소속 영역을 구한다(78–80). 조건·함수 종료·빈 줄(81–85). 원문: `real(kind = RKD), intent(in) :: x_position` (56); `real(kind = RKD), intent(in) :: y_position` (57); `real(kind = RKD), intent(in) :: curr_time` (58); `self.x_pos = x_position` (63); `self.y_pos = y_position` (64); `self.time  = curr_time` (65); `if(present(test) )then` (68); `self.cell = 0` (69); `self.sub_domain_id = 0` (70); `self.cell  = get_nearest_cell(x_position, y_position)` (73); `if(self.cell < 2  )then` (76); `self.sub_domain_id = get_subdomain_id(self.cell)` (80). |
| 86–112 | 시작 시 9행 Mod_Position_Cell 안. write_out_cell 시작(87), 입력 self·선택 입력 unit_num 선언(91–92). present(unit_num)이면 그 단위에 x·y·time·sub_domain_id·cell을 쓴다(94–100). else는 같은 항목을 고정 단위 884에 쓴다(101–107). 실수는 f15.5, 영역 ID는 i4, 셀은 i8 출력 형식(96–107). 조건·루틴·모듈 종료·빈 줄(108–112). 원문: `if(present(unit_num) )then` (94). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 59·68–73: test 인수의 존재 여부만 검사한다. test의 논리값은 검사하지 않으므로 인수가 있으면 지리 조회를 우회하는 분기로 들어간다.
- 61–84: 생성자의 지역 정수 cell은 선언 이후 참조하지 않는다. 실행문은 구성 요소 self.cell을 사용한다.
