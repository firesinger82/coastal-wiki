---
file: models/SWASH/raw/source_code/swash/src/SwashDensity.ftn90
lines: 183
sha256: 2fb3406eacaca05f6c885b92dfafee66776e28517c665476a83a6f86913df46c
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashDensity.ftn90 — 판독 구간 기록

구간은 1행부터 183행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–57 | `SwashDensity` 입구(1).기관·저작권 2010–2026·GPL 3 이상·무보증 안내(2–29). 저자 Marcel Zijlema, 2013년 5월 신설(30–36). 온도·염분·퇴적물로 기준 밀도(reference density)에 대한 물의 밀도를 구한다는 목적(38–40). Eckart 상태방정식(equation of state)과 1958년 논문 서지 주석(42–48). 공통 데이터, rho/rp 유동 배열과 격자 모듈 사용·implicit none(50–57). |
| 58–94 | 시작 시 1행 SwashDensity 루틴 안. 추적 계수 `integer, save :: ient = 0 ! number of entries in this subroutine` (61), 수직층·격자 요소 개수용 정수, 농도·계수·다항식(polynomial)·염분·온도용 real*8 선언(62–74). 구조·소스 구분 주석(76–81). `if (ltrace) call strace (ient,'SwashDensity')` (82). `if ( optg /= 5 ) then` (84)이면 `ntot = mcgrd` (85)를 설정한다. `else` (86)는 `ntot = ncells` (87)를 설정한다. `s = dble(salw )` (92), `t = dble(tempw)` (93)로 상수 염분·온도를 준비한다. [10-15 전수 검증 보완] |
| 95–112 | 시작 시 1행 SwashDensity 루틴 안. `if ( lsal > 0 .and. ltemp > 0 ) then` (95)은 염분과 온도가 모두 공간 변동하는 경로이다. k=1..kmax·n=1..ntot 루프(99–100)에서 `s = dble(rp(n,k,lsal ))` (102)로 염분을 배정밀도로 읽는다. `t = dble(rp(n,k,ltemp))` (103)로 온도를 배정밀도로 읽는다. `p0        =  5890d0  + (  38d0  - 375d-3*t)*t +              3d0*s` (105), `lambda    = 17795d-1 + (1125d-2 - 745d-4*t)*t - (38d-1 + 1d-2*t)*s` (106), `rho(n,k) = p0/(lambda+0.698*p0)` (108). 두 루프 종료·주석(110–112). [10-15 전수 검증 보완] |
| 113–133 | 시작 시 1행 SwashDensity 루틴·95행 `if ( lsal > 0 .and. ltemp > 0 ) then`으로 시작한 분기 사슬 안. `else if ( lsal > 0 ) then` (113)은 염분만 공간 변동하는 경로이다. `rval1 =  5890d0  + (  38d0  - 375d-3*t)*t` (117), `rval2 = 17795d-1 + (1125d-2 - 745d-4*t)*t` (118), `rval3 =    38d-1 +                 1d-2*t` (119). k=1..kmax·n=1..ntot(121–122)에서 `s = dble(rp(n,k,lsal))` (124)로 염분을 읽는다. `p0        = rval1 +   3d0*s` (126), `lambda    = rval2 - rval3*s` (127), `rho(n,k) = p0/(lambda+0.698*p0)` (129). 루프 종료·주석(131–133). [10-15 전수 검증 보완] |
| 134–158 | 시작 시 1행 SwashDensity 루틴·95행 `if ( lsal > 0 .and. ltemp > 0 ) then`으로 시작한 분기 사슬 안. `else if ( ltemp > 0 ) then` (134)은 온도만 공간 변동하는 경로이다. `rval1 =  5890d0  +   3d0*s` (138), `rval2 = 17795d-1 - 38d-1*s` (139). k=1..kmax·n=1..ntot(141–142)에서 `t = dble(rp(n,k,ltemp))` (144)로 온도를 읽는다. `p0        = rval1 + (  38d0           - 375d-3*t)*t` (146), `lambda    = rval2 + (1125d-2 - 1d-2*s - 745d-4*t)*t` (147), `rho(n,k) = p0/(lambda+0.698*p0)` (149). 루프 종료(151–152). `else` (154)는 `rho = 0.` (156)으로 배열 전체를 설정한다. 전체 분기 종료(158). [10-15 전수 검증 보완] |
| 159–183 | 시작 시 1행 SwashDensity 루틴 안. Eckart 밀도의 g/ml를 g/l로 바꾸고 기준 밀도를 뺀다는 주석(160–161). `if ( lsal > 0 .or. ltemp > 0 ) rho = 1000.*rho - rhow` (163). `if ( lsed > 0 .and. lmixt ) then` (165)이면 퇴적물을 고려한다. `fac = dble(rhos-rhow)` (169). k=1..kmax·n=1..ntot(171–172)에서 `c = dble(rp(n,k,lsed))` (174)로 체적 농도(volume concentration)를 읽는다. `rho(n,k) = c * fac + rho(n,k) * (1d0 - c)` (176). 루프·분기·루틴 종료(178–183). [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 105–108·126–129·146–149: 세 밀도 경로는 모두 고정 계수 0.698을 사용한다. 이 루틴에는 온도·염분 범위 검사나 밀도식 분모 검사가 없다.
- 165–176: 퇴적물 체적 농도 c는 rp 값을 그대로 변환해 사용한다. 이 루틴에는 c를 0..1로 제한하는 문장이 없다.
