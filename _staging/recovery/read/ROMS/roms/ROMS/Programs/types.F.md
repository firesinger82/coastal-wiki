---
file: models/ROMS/raw/source_code/roms/ROMS/Programs/types.F
lines: 172
sha256: 7a7e948a4d07175c218f7169f0df6eba71329d464d6960fbb1caab58ff8886e5
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# types.F — 판독 구간 기록

구간은 1행부터 172행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | `PROGRAM types` 시작(1), 저작권·라이선스·컴퓨터 구조별 실수 정밀도(precision)와 표현 범위(range)를 확인한다는 주석(2–18), `implicit none`(19). 정수 상수는 `integer, parameter :: i  = 1` (21), `integer, parameter :: i1b = selected_int_kind(1)       !  8-bit` (22), `integer, parameter :: i2b = selected_int_kind(2)       !  8-bit` (23), `integer, parameter :: i4b = selected_int_kind(4)       !  16-bit` (24), `integer, parameter :: i8b = selected_int_kind(8)       !  32-bit` (25). 실수 종류(kind) 선택은 `integer, parameter :: r4  = selected_real_kind(6,30)` (27), `integer, parameter :: r8  = selected_real_kind(12,300)` (28). 컴파일러의 REAL*16 지원에 관한 설명은 원문 주석이다(13–15). |
| 29–41 | `#ifdef REAL16` (29) 안의 `# if defined SUN \|\| defined AIX` (30)는 `integer, parameter :: r16 = selected_real_kind(16,3000)` (31)을 선택한다. `# else` (32)는 `integer, parameter :: r16 = selected_real_kind(15,3000)` (33)을 선택하고 `# endif` (34)로 닫는다. 바깥 `#else` (35) 안의 `# if defined SUN \|\| defined AIX` (36)는 `integer, parameter :: r16 = selected_real_kind(16,300)` (37)을 선택한다. `# else` (38)는 `integer, parameter :: r16 = selected_real_kind(15,300)` (39)을 선택한다. `# endif` (40)와 `#endif` (41)가 두 조건을 닫는다. |
| 42–68 | 기본 정수와 i1b/i2b/i4b/i8b 정수 배열은 각각 길이 1이다(43–47). a04/a08/a16은 r4/r8/r16 실수이며 b04/b08은 kind=4/8 실수이다(49–54). `#ifdef CRAY` (55)는 b16을 kind=8로 선언한다(56). `#else` (57) 안의 `# ifdef REAL16` (58)는 b16을 kind=16으로 선언한다(59). `# else` (60)는 b16을 real(r16)으로 선언한다(61). `# endif` (62), `#endif` (63), 수치 표현 보고 주석과 빈 줄(64–68). |
| 69–97 | 정수 KIND와 STORAGE_SIZE를 표준 출력에 쓴다(69–78). 실수의 최소 양수 TINY를 b04/b08/b16과 a04/a08에 대해 출력한다(80–91). `#ifdef REAL16` (92)는 a16의 출력 표제를 K(16,3000)으로 정한다(93). `#else` (94)는 K(16,300)으로 정한다(95). `#endif` (96), 빈 줄(97). |
| 98–125 | 최대 수 HUGE의 출력(98–105). `#ifdef REAL16` (106), `#else` (108), `#endif` (110)는 a16의 HUGE 출력 표제를 K(16,3000)/K(16,300)으로 선택한다(107·109). 십진 지수 범위 RANGE의 출력(112–119). `#ifdef REAL16` (120), `#else` (122), `#endif` (124)는 a16의 RANGE 출력 표제를 같은 방식으로 선택한다(121·123). 빈 줄도 포함한다(111·125). |
| 126–153 | 십진 정밀도 PRECISION의 출력(126–133). `#ifdef REAL16` (134), `#else` (136), `#endif` (138)는 a16의 PRECISION 출력 표제를 K(16,3000)/K(16,300)으로 선택한다(135·137). EPSILON 출력의 표제는 negligible number, zero라고 적혀 있다(140–147). `#ifdef REAL16` (148), `#else` (150), `#endif` (152)는 a16의 EPSILON 출력 표제를 같은 방식으로 선택한다(149·151). 빈 줄도 포함한다(139·153). |
| 154–172 | 정수 i=1에 FLOAT(i), REAL(i), REAL(i,r8), REAL(i,r16)을 적용하여 출력한다(154–160). 선택된 r4/r8/r16 종류 번호를 출력한다(162–167). 빈 줄과 STOP(168–170), `END PROGRAM types`(171), 마지막 빈 줄(172). 별도 사용자 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27·90·104·118·132·146: r4의 선언은 selected_real_kind(6,30)을 사용한다. r4 변수의 출력 표제는 K( 6,38 )을 사용한다.
- 31–39·92–96·106–110·120–124·134–138·148–152: SUN/AIX 이외의 r16 선언은 정밀도 인수 15를 사용한다. a16의 출력 표제는 정밀도 인수 자리에 16을 표시한다.
- 55–63·89·103·117·131·145: CRAY 분기의 b16 선언은 kind=8이다. b16의 출력 표제는 (kind=16)이다.
- 70·73–77: 정수 출력의 머리말은 bytes와 bits를 표시한다. 각 출력문은 KIND와 STORAGE_SIZE를 출력하며, bytes를 계산하는 별도 식은 없다.
