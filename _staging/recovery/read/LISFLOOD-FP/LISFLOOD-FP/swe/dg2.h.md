---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/dg2.h
lines: 304
sha256: d24fb9bf698d6a4c1f53b6c437d76a0b1d978067578d17691b7f32d1231c32cf
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# dg2.h — 판독 구간 기록

구간은 1행부터 304행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | `#pragma once` (1)로 중복 포함을 막고 lisflood.h와 rain.h를 포함한다(2–3). dg2 이름공간(namespace)을 연다(5–6). FlowCoefficients는 H·HU·HV와 각각의 1x·1y 계수 배열을 가리키는 NUMERIC_TYPE 포인터 9개를 가진다(7–18). Increment는 같은 이름의 NUMERIC_TYPE 값 9개를 가진다(20–31). 이 헤더에는 추가 전처리 분기나 필드 초기값이 없다. |
| 33–68 | 시작 시 5행 dg2 이름공간 안. zero_thin_depth_slopes는 Pars·Solver·Arrays를 받는다(33–38). solve는 파일명·파일·상태·격자·해석기·경계·관측 지점·배열과 const int verbose를 받는다(40–51). update_point_sources와 update_boundary_values는 Pars·Solver·BoundCs·Arrays 포인터를 받는다(53–67). 함수 본문은 없다. |
| 69–101 | 시작 시 5행 dg2 이름공간 안. Runge–Kutta 단계(Runge–Kutta stage) rk_stage1·rk_stage2 원형은 Pars·Solver·BoundCs·Arrays를 받는다(69–83). update_fluxes는 이 중 경계 포인터 없이 FlowCoefficients const& U를 받고(85–91), update_fluxes_on_boundaries는 BoundCs와 같은 U 참조를 받는다(93–100). |
| 102–141 | 시작 시 5행 dg2 이름공간 안. set_boundary_values는 경계 번호·HU 부호·Zstar·셀 평균과 내부·외부 H·HU·HV 참조를 받는다(102–119). H_const는 참조이고 HU_const·HV_const는 값 인수다(110–112). update_intermediate_coefficients는 셀 i·j와 Increment const&를 받고(121–129), 단일 계수 함수 update_intermediate_coefficient는 field_n·field_int 포인터와 increment를 받는다(131–140). |
| 142–174 | 시작 시 5행 dg2 이름공간 안. update_final_coefficients와 update_final_coefficient는 최종 계수 갱신용 원형이다(142–161). 전자는 Increment const&, 후자는 이전·중간 필드 포인터와 increment를 받는다. set_initial_coefficients와 set_intermediate_coefficients는 Arrays와 FlowCoefficients 참조를 받는다(163–173). |
| 175–218 | 시작 시 5행 dg2 이름공간 안. L·L0·L1x·L1y는 모두 Pars·Solver·Arrays·const int i·j·FlowCoefficients const&·Increment&를 받는 void 원형이다(175–217). 계산식은 이 선언에 없다. |
| 219–258 | 시작 시 5행 dg2 이름공간 안. bed_source_0x·bed_source_0y·bed_source_1x·bed_source_1y는 모두 NUMERIC_TYPE을 반환하고 Pars·Solver·Arrays·FlowCoefficients const&와 셀 i·j를 받는다(219–257). 바닥 경사 생성항(bed source term) 계산 본문은 없다. |
| 259–287 | 시작 시 5행 dg2 이름공간 안. maxH는 Pars·Arrays에서 NUMERIC_TYPE을 반환한다(259–263). thin_depth는 Solver와 H에서 bool을 반환한다(265–269). Tstep_from_cfl은 Pars·Solver·Arrays, min_dt는 dt·H·HU·HV·Pars·Solver를 받는다(271–286). Courant–Friedrichs–Lewy 조건(CFL condition)의 실제 식은 이 헤더에 없다. |
| 288–304 | 시작 시 5행 dg2 이름공간 안. zero_discharge는 Pars·Solver·i·j와 H·H1x·H1y·HU·HU1x·HU1y·HV·HV1x·HV1y의 포인터 9개를 받는 void 원형이다(288–303). 이름공간을 닫는다(304). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
