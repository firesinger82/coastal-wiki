---
file: models/ADCIRC/raw/source_code/adcirc/wind/precision.F
lines: 92
sha256: 8aa4f18876998350bd2df5f3bdbbaa99b74e24798447ca1b296ba9388a3f290f
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# precision.F — 판독 구간 기록

구간은 1행부터 92행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–43 | 저작권·LGPL 3 이상·무보증 머리말(1–19), 모듈 제목 장식 주석·빈 줄(20–29). 플랫폼 간 이식성을 위해 정밀도(precision)를 정의한다는 설명(30–32). C 전처리기(preprocessor) 매크로로 정밀도를 선택한다는 주석과 컴파일 예시 `f90 -O -c precision.F -DREAL8 -DINT2` (36), `xlf90 -O -c precision.F -WF,-DREAL8,-DINT2` (37). 2006-05-23 Craig Mattocks의 최초 작성 이력(39–43). 이 구간은 전부 주석·빈 줄이다. |
| 44–67 | `MODULE precision` (44), `IMPLICIT NONE` (49), `SAVE` (54) 및 설명 주석·빈 줄. kind 매개변수(kind parameter)는 `INTEGER, PARAMETER :: sp = SELECTED_REAL_KIND(p=6, r=37)` (60), `INTEGER, PARAMETER :: dp = SELECTED_REAL_KIND(p=15, r=307)` (66). 주석은 sp의 정확도를 6자리·지수 범위를 10^-37..10^37, dp의 정확도를 15자리·지수 범위를 10^-307..10^307로 설명한다(56–65). |
| 68–78 | 실수 선언의 sz 선택 주석·빈 줄(68–70). `#ifdef REAL8` (71)이면 `INTEGER, PARAMETER :: sz = dp` (73). `#else` (74)는 `INTEGER, PARAMETER :: sz = sp` (76). `#endif` (77), 빈 줄(78). 직접 수치 kind를 지정하는 `!        INTEGER, PARAMETER :: sz = 8` (72) 및 `!        INTEGER, PARAMETER :: sz = 4` (75)는 주석 처리되어 있다. REAL8이 정의되지 않은 기본 분기는 sp를 선택한다. |
| 79–92 | 정수 선언의 iz 선택 주석(79–81). `#ifdef INT8` (82)이면 `INTEGER, PARAMETER :: iz = 8` (83). `#elif INT2` (84)이면 `INTEGER, PARAMETER :: iz = 2` (85). `#elif INT1` (86)이면 `INTEGER, PARAMETER :: iz = 1` (87). `#else` (88)의 기본값은 `INTEGER, PARAMETER :: iz = 4` (89). `#endif` (90), 빈 줄·모듈 종료(91–92). 분기는 INT8·INT2·INT1 순서로 검사한다. 루틴 호출이나 실행문은 이 파일에 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 60·66·69·73·76: sz의 주석은 바이트 수를 설명한다. 실제 sz는 SELECTED_REAL_KIND 결과인 dp 또는 sp를 사용하며 직접 8/4를 지정하는 문장은 주석 처리되어 있다(72·75).
- 80·82–90: iz의 주석은 바이트 수를 설명한다. 실제 iz는 8·2·1·4의 정수 리터럴을 사용하며 이 파일에는 SELECTED_INT_KIND 호출이 없다.
