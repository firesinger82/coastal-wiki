---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Transport/mod_quickest.f90
lines: 115
sha256: a7752a1d4198e21e406f25d577b9686a10cdb2fcbec75938061f5205356b1e9f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_quickest.f90 — 판독 구간 기록

구간은 1행부터 115행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | QUICKEST(Quadratic Upstream Interpolation for Convective Kinematics with Estimated Streaming Terms) 수송법 머리말(1–6). Leonard 1979·1991 및 GOTM P2_PDM 제한자(limiter)를 참고문헌으로 적는다(7–14). 날짜 주석은 2025-12-19이다(15). `MODULE MOD_QUICKEST`, GLOBAL 사용, implicit none, contains와 빈 줄(18–23). |
| 24–59 | `QUICKEST_FACE(Cu, Cc, Cd, cfl)` 함수 안내와 선언(24–47). Cu는 면에서 두 셀 상류, Cc는 한 셀 상류, Cd는 하류 농도라는 주석이다(30–34). Courant 수(Courant number)의 주석식은 `!   cfl  - Courant number at face (\|U\|*dt/dx, always positive)` (34). 입력과 반환값은 REAL(RKD)이다(40·44–47). 농도차·기울기비·제한자·x·cfl_safe 선언(49–55). 작은 수의 원문 기본값은 `REAL(RKD), PARAMETER :: EPSILON = 1.0E-30_RKD` (58). |
| 60–79 | 시작 시 40행 QUICKEST_FACE 함수 안. 농도차 원문은 `deltaf  = Cd - Cc` (61), `deltafu = Cc - Cu` (62). 원문 조건은 `IF( deltaf * deltafu <= 0.0_RKD )THEN` (67). 참이면 Cc를 반환값으로 복사하고 즉시 return한다(69–70). 조건 밖에서 `ratio = deltafu / (deltaf + EPSILON)` (74), `cfl_safe = MIN(MAX(cfl, EPSILON), 0.999_RKD)` (78). cfl_safe를 EPSILON부터 0.999_RKD까지 제한한다. |
| 80–104 | 시작 시 40행 QUICKEST_FACE 함수 안이며 67행 조건 밖. 원문은 `x = (1.0_RKD - 2.0_RKD*cfl_safe) / 6.0_RKD` (84), `limiter = (0.5_RKD + x) + (0.5_RKD - x) * ratio` (87). 주석은 총변동감소(total variation diminishing, TVD)를 위한 세 제약을 적는다(89–93). 실행 제약은 `limiter = MIN(2.0_RKD * ratio / (cfl_safe + EPSILON), limiter)` (94), `limiter = MIN(limiter, 2.0_RKD / (1.0_RKD - cfl_safe))` (95), `limiter = MAX(limiter, 0.0_RKD)` (98). 면 농도는 `QUICKEST_FACE = Cc + 0.5_RKD * limiter * (1.0_RKD - cfl_safe) * deltaf` (101). 함수 종료와 빈 줄(103–104). |
| 105–115 | 초기화 루틴 안내(105–109), `SUBROUTINE QUICKEST_INIT()` 및 implicit none(110–111). 실행문 없이 루틴을 끝낸다(113). 빈 줄과 모듈 종료(114–115). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 74·78: 기울기비 분모에는 부호를 따로 처리하지 않고 deltaf+EPSILON을 사용한다. cfl_safe에는 입력 cfl과 별도로 하한 EPSILON과 상한 0.999_RKD를 적용한다.
- 110–113: QUICKEST_INIT에는 실행문이 없다.
