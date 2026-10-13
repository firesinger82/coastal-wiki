---
file: models/ROMS/raw/source_code/roms/ROMS/Modules/mod_kinds.F
lines: 53
sha256: d4532c638cc8bf5f44b822f519da78ad566736c7df99ec12acccf1da239ac870
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# mod_kinds.F — 판독 구간 기록

구간은 1행부터 53행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | `#include "cppdefs.h"` (1)은 cppdefs.h를 끼워 넣는다. mod_kinds 시작(2). 저작권·라이선스 머리말(4–9). ESMF_LIB이면 ESMF 모듈 사용(11–14). implicit none(15), 빈 주석(16). 전처리 원문: `#include "cppdefs.h"` (1); `#ifdef ESMF_LIB` (11); `#endif` (14). |
| 17–31 | ESMF_LIB 분기의 정수·실수 종류(kind) 상수 선언. i1b/i2b의 ESMF_KIND_I1/I2 대입은 주석 처리(18·20). 실제 선언 원문: `integer, parameter :: i1b= SELECTED_INT_KIND(1)        !  8-bit` (19); `integer, parameter :: i2b= SELECTED_INT_KIND(2)        !  8-bit` (21); `integer, parameter :: i4b= ESMF_KIND_I4                ! 16-bit` (22); `integer, parameter :: i8b= ESMF_KIND_I8                ! 32-bit` (23); `integer, parameter :: c8 = SELECTED_REAL_KIND(6,30)    ! 32-bit` (24); `integer, parameter :: dp = ESMF_KIND_R8                ! 64-bit` (25); `integer, parameter :: r4 = ESMF_KIND_R4                ! 32-bit` (26). SINGLE_PRECISION이면 `integer, parameter :: r8 = ESMF_KIND_R4                ! 32-bit` (28), else는 `integer, parameter :: r8 = ESMF_KIND_R8                ! 64-bit` (30). 비트 수 표기는 각 선언의 원문 주석이다. 이 파일에서는 컴파일러가 반환하는 실제 kind 값이나 자료형 크기를 계산하지 않는다. 전처리 원문: `#ifdef ESMF_LIB` (17); `# ifdef SINGLE_PRECISION` (27); `# else` (29); `# endif` (31). |
| 32–45 | 시작 시 `#ifdef ESMF_LIB` (17) 안. 17행 ESMF_LIB 조건의 else 분기. 상수를 SELECTED_INT_KIND 및 SELECTED_REAL_KIND 인수로 정한다. 원문: `integer, parameter :: i1b= SELECTED_INT_KIND(1)        !  8-bit` (33); `integer, parameter :: i2b= SELECTED_INT_KIND(2)        !  8-bit` (34); `integer, parameter :: i4b= SELECTED_INT_KIND(4)        ! 16-bit` (35); `integer, parameter :: i8b= SELECTED_INT_KIND(8)        ! 32-bit` (36); `integer, parameter :: c8 = SELECTED_REAL_KIND(6,30)    ! 32-bit` (37); `integer, parameter :: dp = SELECTED_REAL_KIND(12,300)  ! 64-bit` (38); `integer, parameter :: r4 = SELECTED_REAL_KIND(6,30)    ! 32-bit` (39). SINGLE_PRECISION이면 `integer, parameter :: r8 = SELECTED_REAL_KIND(6,30)    ! 32-bit` (41), else는 `integer, parameter :: r8 = SELECTED_REAL_KIND(12,300)  ! 64-bit` (43). dp의 인수는 12,300이며 r8의 인수만 SINGLE_PRECISION 분기에서 6,30으로 바뀐다. ESMF_LIB 분기 종료(45). 전처리 원문: `#else` (32); `# ifdef SINGLE_PRECISION` (40); `# else` (42); `# endif` (44); `#endif` (45). |
| 46–53 | SUN·AIX·NEC·SGI·CRAYX1·DEC 중 하나가 정의되면 `integer, parameter :: r16 = SELECTED_REAL_KIND(24,270) !128-bit` (48). else는 `integer, parameter :: r16 = SELECTED_REAL_KIND(15,300) !128-bit` (50). 두 선언 모두 원문 주석은 128-bit이다. 전처리 분기 종료(51), 빈 줄(52), mod_kinds 종료(53). 실행 루틴이나 외부 호출은 없다. 전처리 원문: `#if defined SUN \|\| defined AIX \|\| defined NEC \|\| defined SGI \|\| \` (46); `defined CRAYX1 \|\| defined DEC` (47); `#else` (49); `#endif` (51). |


## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 46–51: r16의 SELECTED_REAL_KIND 인수는 지정 플랫폼 분기에서 (24,270), else에서 (15,300)이다. 두 선언의 주석은 모두 128-bit이다. 실제 kind 값과 저장 크기는 이 판독에서 실행 확인하지 않았다.
