---
file: models/SWAN/raw/source_code/swan/src/SwanCrossObstacle.ftn90
lines: 113
sha256: e1e4ffc2c547715a35d2119e4ced77430b1e6d93b0ec8c5aeb5b479aa343f4ea
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanCrossObstacle.ftn90 — 판독 구간 기록

구간은 1행부터 113행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–51 | 논리 함수 `SwanCrossObstacle` 입구(1). 기관·GPL 3 이상·무보증·작성자·갱신 이력(3–36). 장애물 선(obstacle line)과 계산 격자 면의 교차를 검사한다는 목적(38–40). 방법은 기술 문서(Technical documentation)를 참조하라는 주석이다(42–44). `ocpcomm4` 사용과 `implicit none`(48–50). |
| 52–80 | 시작 시 1행 함수 안. 장애물 선분(line segment)과 격자 면의 두 끝점 좌표 `xobs,yobs,xv,yv`를 입력으로 선언한다(54–57). 저장 변수 초기값은 `ient = 0`이다(61). 좌표차·행렬식(determinant)·선분 매개변수 `p,q`, 실수 동등 비교 함수 `EQREAL` 선언(63–73). 구조·소스 안내 주석(75–80). [10-13 전수 검증 보완] |
| 81–113 | 시작 시 1행 함수 안. 추적 조건·호출은 `if (ltrace) call strace (ient,'SwanCrossObstacle')` (81)이다. `SwanCrossObstacle = .true.`(85)로 교차 반환값을 초기화한다. 좌표차 식은 `a = xv(1) - xobs(1)` (87); `b = yv(1) - yobs(1)` (88), `c = xv(2) - xv(1)` (90); `d = yv(2) - yv(1)` (91), `e = xobs(2) - xobs(1)` (93); `f = yobs(2) - yobs(1)` (94)이다. 행렬식은 `det = e*d - f*c` (98)이다. 비영 행렬식 조건은 `if ( .not.EQREAL(det,0.) ) then` (100)이다. 참 분기의 교차 매개변수 식은 `p = (a*d - b*c)/det` (102); `q = (a*f - b*e)/det` (103)이다. 선분 범위 검사·거짓 반환 조건은 `if ( p<0. .or. p>1. .or. q<0. .or. q>1. ) SwanCrossObstacle = .false.` (105)이다. `else` (107) 분기는 `SwanCrossObstacle = .false.`(109)로 교차를 거짓으로 설정한다. 조건·함수 종료(111–113). [10-13 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 100–109: `EQREAL(det,0.)`가 참이면 교차 결과를 거짓으로 둔다. 이 분기에는 같은 직선 위의 두 선분 겹침을 별도로 검사하는 문장이 없다.
- 105: `p`와 `q`의 범위 검사는 0보다 작거나 1보다 큰 경우만 제외한다. 끝점 값 0과 1은 이 조건에서 제외하지 않는다.
