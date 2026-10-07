---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Propwash/Mod_Ship.f90
lines: 118
sha256: 1415cc24ce4e47d762a2f0841b646c9b5a8d2e4c4332ee8d85aef683e182e686
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Mod_Ship.f90 — 판독 구간 기록

구간은 1행부터 118행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | EFDC+ 출처·GPLv2·저작권 머리말(1–16). Mod_Ship은 GLOBAL의 rkd·rk4·ik4를 가져온다(17–21). 기본 접근은 private이고 ship_type만 공개한다(23–25). |
| 27–59 | 시작 시 17행 Mod_Ship 모듈 안. 선박 형식(ship type)은 식별자·이름·동력원·길이·폭·흘수(draft)·마력(horsepower)·초당 회전수(revolutions per second)를 선언한다(28–37). 자동식별시스템(Automatic Identification System, AIS) 안테나부터 선미까지 거리, 추진기(propeller) 간격·선미 거리·축 깊이 오프셋(offset)을 선언한다(38–41). 추진기 수·날개 수·덕트(duct) 여부·추력계수(thrust coefficient)·지름·허브(hub) 지름·날개 면적비·피치비(pitch ratio)·출력 간격을 선언한다(43–52). 동력원 주석은 0=마력, 1=RPM이고 덕트 주석은 0=없음, 1=있음이다(31·45). mesh_count·fixed_cells·fixed_frac는 allocatable이다(54–58). 스칼라 기본값은 아래 원문과 같다. 계산·설정 원문: `integer                :: mmsi               = 0` (29), `character(len = 100)     :: name               = ' '` (30), `integer (kind = ik4)   :: power_source       = 0` (31), `real    (kind = rkd)   :: length             = 0.0` (32), `real    (kind = rkd)   :: beam               = 0.0` (33), `real    (kind = rkd)   :: max_draft          = 0.0` (34), `real    (kind = rkd)   :: min_draft          = 0.0` (35), `real    (kind = rkd)   :: max_power          = 0.0` (36), `real    (kind = rkd)   :: max_rps            = 0.0` (37), `real    (kind = rkd)   :: ais_to_stern       = 0.0` (38), `real    (kind = rkd)   :: dist_between_props = 0.0` (39), `real    (kind = rkd)   :: dist_from_stern    = 0.0` (40), `real    (kind = rkd)   :: prop_offset        = 0.0` (41), `integer (kind = ik4)   :: num_props          = 0` (43), `integer (kind = ik4)   :: num_blades         = 0` (44), `integer (kind = ik4)   :: ducted             = 0` (45), `real    (kind = rkd)   :: thrust_coeff       = 0.0` (46), `real    (kind = rkd)   :: prop_diam          = 0.0` (47), `real    (kind = rkd)   :: prop_hub_diam      = 0.0` (48), `real    (kind = rkd)   :: blade_area_ratio   = 0.0` (49), `real    (kind = rkd)   :: pitch_ratio        = 0.0` (50), `real    (kind = rkd)   :: freq_out           = 0.0` (52), `integer (kind = ik4), allocatable :: mesh_count(:)` (54), `integer (kind = ik4)   :: num_fixed_cells     = 0` (56), `integer (kind = ik4), allocatable :: fixed_cells(:)` (57), `real    (kind = RK4), allocatable :: fixed_frac(:)` (58). |
| 60–93 | 시작 시 17행 모듈·28행 ship_type 형식 안. self를 전달하는 write_out 바인딩(binding)을 선언하고 형식을 닫는다(60–64). 모듈 contains 뒤 생성자(constructor) interface와 함수 초안 전체는 주석이다(67–87). write_out 목적·인수·작성자 주석을 포함한다(89–93). |
| 94–118 | 시작 시 17행 모듈 안. write_out은 self와 출력 장치 번호를 받는다(94–99). 추력계수를 출력한다(101·104). power_source=0이면 최대 마력, 1이면 최대 초당 회전수를 출력한다(105–109). 이후 추진기·허브 지름, 날개 면적비, 피치비, 날개 수를 출력한다(110–114). MMSI·이름 출력은 주석이다(102–103). 루틴·모듈 종료와 빈 줄을 포함한다(115–118). 조건·반복 원문: `if( self.power_source == 0 )then` (105), `elseif( self.power_source == 1 )then` (107). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–14·30·54–58: 머리말은 시작값을 모두 zero로 초기화한다고 적는다. name의 기본값은 공백이다. allocatable 배열에는 선언 시 원소값 대입이 없다.
- 31·105–109: power_source 주석은 값 1을 Propeller RPM으로 적는다. 해당 출력 분기는 max_rps를 Max RPS Prop라는 이름으로 출력한다.
- 98–99: self 선언의 주석은 파일 unit number라고 적는다. self의 실제 형식은 class(ship_type)이고 unit_num은 별도 정수 인수이다.
