---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Propwash/mod_Variables_Propwash.f90
lines: 70
sha256: dec4594e6a62dec437dfb96e1d73bfa9c7f76916e1986e91900756717f267f2c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_Variables_Propwash.f90 — 판독 구간 기록

구간은 1행부터 70행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | EFDC+ 출처·GPLv2·저작권과 Variables_Propwash 변경 이력(1–22). 이력은 초기 후류 구조, SEDZLJ·독성물질 연계, 후류 제트(jet) 운동량(momentum) 연계를 적는다(18–21). 모듈은 GLOBAL을 가져오고 implicit none을 사용한다(23–27). |
| 29–39 | 시작 시 23행 Variables_Propwash 모듈 안. 로그 장치 번호는 668이다(29). 후류 플래그·선박 수는 초기값 없이 선언한다(31–32). propwash_on 기본값은 false이다(34). 인접 셀 배열은 allocatable이고 반경·축방향 메시(mesh) 점 수는 integer(kind=rk4)이다(36–38). 계산·설정 원문: `integer, parameter :: prop_log_unit = 668` (29), `logical :: propwash_on = .FALSE.` (34), `integer(kind = rk4) :: num_radial_elems` (37), `integer(kind = rk4) :: num_axial_elems` (38). |
| 40–52 | 시작 시 23행 모듈 안. 실행시간 누적 변수 TPROPW에는 선언 초기값이 없다(40). 메시 폭·길이는 추진기(propeller) 지름의 30·60배이다(41–42). 유출(efflux) 구역·단일 추진기 유동 형성(flow establishment) 구역·쌍 추진기 영향 구역 배율은 아래 원문과 같다(43–45). ISPROPWASH=2의 속도 보정, 빠른 침강(fast settling) 분율·배율, epsilon·pi_prop 상수를 선언한다(46–51). 입력 범위 검사 실행문은 이 모듈에 없다. 계산·설정 원문: `real(kind = rkd) :: TPROPW` (40), `real(kind = rkd) :: mesh_width    = 30.` (41), `real(kind = rkd) :: mesh_Length   = 60.` (42), `real(kind = rkd) :: efflux_zone_mult    = 0.35` (43), `real(kind = rkd) :: flow_est_zone1_mult = 3.5` (44), `real(kind = rkd) :: flow_est_zone2_mult = 14.` (45), `real(kind = rkd) :: efflux_mag_mult     = 0.75` (46), `real(kind = rkd) :: fraction_fast       = 0.` (47), `real(kind = rkd) :: fast_multiplier     = 30.` (48), `real(kind = rkd), parameter :: epsilon = 1.e-3` (50), `real(kind = rkd), parameter :: pi_prop = 3.1415926535897932` (51). |
| 53–70 | 시작 시 23행 모듈 안. 활성 선박 수·메시 출력 플래그·최소 출력 간격은 0으로 시작하고 last_snapshot에는 선언 초기값이 없다(54–57). prop_ero·prop_bld는 등급별 셀 통합 침식(erosion)량(g/cm^2)이라는 주석의 allocatable 배열이다(60–61). 수층(water column)·퇴적층 대응과 빠른 침강 플래그 배열의 고정 길이는 100이다(63–65). contains 뒤 루틴 없이 모듈을 닫는다(67–70). 계산·설정 원문: `integer(kind = rk4) :: nactiveships = 0` (54), `integer(kind = rk4) :: iwrite_pwmesh = 0` (55), `real(kind = rkd)    :: freq_out_min = 0.` (56), `real(kind = rkd)    :: last_snapshot` (57), `real(kind = rkd), allocatable :: prop_ero(:,:)` (60), `real(kind = rkd), allocatable :: prop_bld(:,:)` (61). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 37–38·54–55: 메시 점 수와 활성 선박 수·출력 플래그는 integer(kind = rk4)로 선언되어 있다. rk4의 정의는 이 파일 안에 없다.
- 31–32·37–40·57·63–65: ISPROPWASH·total_ships·num_radial_elems·num_axial_elems·TPROPW·last_snapshot·세 매핑 배열에는 선언 초기값이 없다. 이 모듈에는 이 변수들을 초기화하는 실행 루틴도 없다.
- 63–65: IWC2BED·IBED2WC·IFASTCLASS 배열 길이를 모두 100으로 고정한다.
