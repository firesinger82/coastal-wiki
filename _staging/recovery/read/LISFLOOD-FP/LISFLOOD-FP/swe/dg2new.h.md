---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/dg2new.h
lines: 179
sha256: d4460308b6fc413f41ecbcc56d9aea3fdd6b92204c721b19dbf8b304ef60d106
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# dg2new.h — 판독 구간 기록

구간은 1행부터 179행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | `#pragma once`(1)와 lisflood 헤더 포함(2) 후 dg2new 이름공간(namespace)을 연다(4–5). Increment는 H·HU·HV 각각의 평균·x·y 계수 아홉 개(6–17), LocalFaceValue는 H·ETA·HU·HV(19–25), FlowVector는 H·HU·HV(27–32)를 가진다. 구조체 멤버의 기본값은 없다. 조건부 전처리 분기는 없다. 원문: `#pragma once` (1); `#include "../lisflood.h"` (2). |
| 34–58 | 단항 음수·벡터 덧셈·벡터 뺄셈·스칼라 곱·스칼라 나눗셈 연산자(operator)를 inline 함수로 정의한다. 각 성분을 따로 계산하며 나눗셈의 영 분모 검사는 없다. 원문: `return { -u.H, -u.HU, -u.HV };` (36); `return { lhs.H + rhs.H, lhs.HU + rhs.HU, lhs.HV + rhs.HV };` (41); `return { lhs.H - rhs.H, lhs.HU - rhs.HU, lhs.HV - rhs.HV };` (46); `return { scalar * u.H, scalar * u.HU, scalar * u.HV };` (51); `return { u.H / scalar, u.HU / scalar, u.HV / scalar };` (56). |
| 59–104 | 시작 시 4행 dg2new 이름공간 안이다. DG2Solver 클래스(class)의 공개 생성자·solve·소멸자(59–77), 비공개 입력·시간 간격·마찰·Runge–Kutta 함수 원형(79–103)을 선언한다. 스칼라 마찰형은 두 NUMERIC_TYPE 참조 출력 인수를 갖는다(90–98). 기본 인수값·실행 조건문은 없다. |
| 105–150 | 시작 시 59행 DG2Solver 클래스의 비공개 영역(79) 안이다. 주석은 nmod 0을 RK 1단계, 1을 RK 2단계로 대응시킨다(105–108·132–136). 방향 번호는 1=북·2=동·3=남·4=서다(134). 공간 연산자·DG2 연산자·면값 재구성·습윤 건조(wetting and drying)·x/y 플럭스 원형을 선언한다(108–149). 이 구간의 nmod·ndir 대응은 주석이며 실행 if가 아니다. |
| 151–179 | 시작 시 59행 DG2Solver 클래스의 비공개 영역(79) 안이다. 두 시간 간격 함수, 질량 통계·출력·할당 함수(151–157), 외부 자료 포인터 여덟 개와 verbose(159–167), 새 상태 포인터 아홉 개(169–177)를 선언한다. 선언 내 포인터 초기값은 없다. 클래스와 이름공간을 닫는다(178–179). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 54–56: 벡터 나눗셈 연산자는 scalar가 0인지 검사하지 않고 각 성분을 나눈다.
- 159–177: 클래스 자료 멤버 선언에는 초기값이 없다. 초기화 실행 여부는 이 헤더만으로 정하지 않는다.
