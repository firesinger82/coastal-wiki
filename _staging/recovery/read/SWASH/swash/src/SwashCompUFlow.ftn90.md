---
file: models/SWASH/raw/source_code/swash/src/SwashCompUFlow.ftn90
lines: 112
sha256: b2155ff7ca2d6696b8b6e6adfe196c728e5a301fe256a49cdf250ed7a3883d0d
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashCompUFlow.ftn90 — 판독 구간 기록

구간은 1행부터 112행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | `SwashCompUFlow` 입구(1). 기관·저작권 2010–2026·GPL 3 이상·무보증 주석(3–27), 작성자·2017년 신설(30–36). 삼각 격자(triangular mesh)의 천수방정식(shallow water equations)으로 수위와 유속을 계산한다는 목적(38–40). 중력파에 대해 무조건 안정이라는 반음해법(semi-implicit approach) 설명과 수위경사·수심적분 연속방정식을 양해적 리프프로그법(explicit leap-frog technique)으로 처리하는 대안은 방법 주석이다(42–47). |
| 49–69 | 시작 시 1행 루틴 안. ocpcomm4·SwashCommdata3·outp_data의 lwavoutp/lcuroutp·SwashFlowdata 사용(51–54). `integer, save :: ient = 0 ! number of entries in this subroutine` (60). 구조·소스 구분 주석(62–67). `if (ltrace) call strace (ient,'SwashCompUFlow')` (68). |
| 70–87 | 시작 시 1행 루틴 안. `if ( kmax == 1 ) then` (70)은 수심적분 경로. `if ( mtimei == 1 ) then` (74)은 `call SwashExpDepUflow ( u1(1,1), u0(1,1), uvc(1,1,1), qn(1,1), quf(1,1,1), q(1,1), dq(1,1), gmatu(1,1,1), rho(1,1) )` (78). `else if ( mtimei == 2 ) then` (80)은 같은 인수의 `call SwashImpDepUflow ( u1(1,1), u0(1,1), uvc(1,1,1), qn(1,1), quf(1,1,1), q(1,1), dq(1,1), gmatu(1,1,1), rho(1,1) )` (84). 내부 분기 종료(86). |
| 88–107 | 시작 시 1행 루틴·70행 `if ( kmax == 1 ) then` 안에서 `else` (88)로 고정 층수의 층평균(layer-averaged) 경로. `if ( mtimei == 1 ) then` (92)은 `call SwashExpLayUflow` (96), `else if ( mtimei == 2 ) then` (98)은 `call SwashImpLayUflow` (102). 시간적분 분기·층수 분기 종료(104·106). 92행 사슬에는 최종 `else`가 없다. 90행 주석은 비정수압 층평균 천수방정식을 명시한다. [10-15 전수 검증 보완] |
| 108–112 | 시작 시 1행 루틴 안. 출력용 평균 수위 상승(wave setup)·파고·평균 흐름 갱신 주석(108–109). `if ( lwavoutp .or. lcuroutp ) call SwashAverOutp ( 1 )` (110). 루틴 종료(112). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 74–86·92–104·110: 두 층수 경로는 mtimei=1/2만 처리하며 마지막 else가 없다. 출력 평균 호출은 mtimei 분기 밖에 있다.
