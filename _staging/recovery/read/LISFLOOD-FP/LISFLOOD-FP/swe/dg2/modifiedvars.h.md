---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/dg2/modifiedvars.h
lines: 314
sha256: d6098cab27dfbe6680478fe685b30debf9d44a73dd99dbc96cd68b2aa0df247c
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# modifiedvars.h — 판독 구간 기록

구간은 1행부터 314행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–59 | `#pragma once`(1)와 두 헤더 포함(2–3) 후 dg2 이름공간(namespace)을 연다(5–6). 이 파일에는 조건부 전처리 분기가 없다. `initialise_Zstar`(7–11), H·HU·HV 수정값 갱신 함수(13–35), 공통 유량 갱신 함수(37–50), `discharge_star`(52–58)의 원형을 선언한다. U는 `FlowCoefficients const&`이며 계산식·기본 인수값은 없다. 원문: `#pragma once` (1); `#include "../dg2.h"` (2); `#include "../../lisflood.h"` (3). |
| 60–123 | 시작 시 5행 dg2 이름공간 안이다. 수정 수심의 평균·일차 계수 `Hstar0x`·`Hstar0y`·`Hstar1x`·`Hstar1y`(60–90)와 수정 HU의 동형 함수(92–122)를 선언한다. 각 함수는 Pars·Arrays 포인터와 const int i·j를 받으며 NUMERIC_TYPE을 반환한다. 함수 실행문은 없다. |
| 124–173 | 시작 시 5행 dg2 이름공간 안이다. 수정 HV 계수 함수 네 개(124–154), `Zdagger1x`·`Zdagger1y`(156–172)를 선언한다. Zdagger 함수는 추가로 `FlowCoefficients const& U`를 받는다. 선언에는 조건·계산식이 없다. |
| 174–245 | 시작 시 5행 dg2 이름공간 안이다. 방향별 `Zdagger_neg_x`·`Zdagger_pos_x`·`Zdagger_neg_y`·`Zdagger_pos_y`(174–208) 및 `eta_neg_x`·`eta_pos_x`·`eta_neg_y`·`eta_pos_y`(210–244)의 원형을 선언한다. Pars·Arrays·U·i·j를 받으며 NUMERIC_TYPE을 반환한다. |
| 246–290 | 시작 시 5행 dg2 이름공간 안이다. `eta`·`eta1x`·`eta1y`(246–271)와 배열 인수형 `limit_neg`·`limit_pos`(273–289)를 선언한다. 후자는 상수 배열·기울기 배열·격자 정보·i·j를 받는다. |
| 291–314 | 시작 시 5행 dg2 이름공간 안이다. 배열 인수형 가우스점(Gauss point) 평가 `gauss_lower`·`gauss_upper`(291–307), 상수·기울기를 직접 받는 스칼라형 limit·gauss 함수 네 개(309–312)를 선언한다. 이름공간은 313행에서 닫히며 마지막 빈 줄도 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
