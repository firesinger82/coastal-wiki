---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/normalization.F
lines: 73
sha256: 780cdd60fe79ead20b2dbdf1df1870d97bf1832db07a85f707aa24970a56e608
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# normalization.F — 판독 구간 기록

구간은 1행부터 73행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 시작 시 열린 전처리 조건 없음. `#include "cppdefs.h"` (1)은 cppdefs.h를 끼워 넣는다. `#if defined FOUR_DVAR` (2)가 본문을 감싼다. 저작권·MIT/X 라이선스·License_ROMS.md 안내(3–9). 주석은 정규화 계수(normalization factor)가 배경 오차(background error)의 대칭 공분산 행렬(symmetric covariance matrix) B의 공간 퍼짐(spreading)을 모델링하며 대각 원소를 1로 맞춘다고 설명한다(11–14). 육지/해양 마스크(mask)를 쓰면 경계 부근의 공분산 구조를 크게 바꿀 수 있다는 주석(14–16). 빈 주석 포함(10·17). |
| 18–38 | 시작 시 2행 `#if defined FOUR_DVAR` 안. 실행 코드가 아닌 설명 주석이다. 공간 상관(spatial correlation) 공간의 유사 확산 연산자(pseudo-diffusion operator)로 퍼짐을 모델링한다(18–19). 확산 계수(diffusion coefficient) K는 상관 길이 척도(correlation length scale)의 제곱에 비례한다는 설명과 Daley, 1992 인용(19–20). 제어 벡터(control vector)의 변수별 상관 척도는 일정하거나 공간적으로 달라질 수 있다(21–22). B는 다중 척도(multiscale) 또는 단일 척도(monoscale)로 표현한다(22–29). 다중 척도는 큰 척도부터 작은 척도까지 선형 결합하여 넓은 구조·세부 구조를 표현하고 자료 동화(data assimilation) 비용 함수(cost function)의 척도 에일리어싱(scale aliasing)을 줄인다는 Weaver et al., 2016 인용 주석(24–28). 단일 척도는 척도 하나를 쓴다(29). 다중 척도의 수평 유사 확산은 음적(implicit) 연산자와 공액 기울기(Conjugate Gradient, CG)·체비쇼프 반복(Chebyshev Iterations, CI)을 쓴다(31–33). 기본 단일 척도 수평 방법은 양적(explicit) 알고리즘이라는 주석(33–34). 오차 상관은 수평·수직으로 분리 가능하다고 가정하며 수직 확산은 두 방법 모두 음적이라는 주석(34–37). 빈 주석 포함(30·38). |
| 39–51 | 시작 시 2행 `#if defined FOUR_DVAR` 안. 실행 코드가 아닌 설명 주석이다. 다중 척도 식은 원문 `B = SUM(Wi*Bi)` (39). 서로 다른 척도의 B를 가중합하며, 실용 적용은 보통 2–4개 척도를 결합한다는 주석(40–41). Wi의 합은 1이어야 한다는 제약(42). 결과 상관 함수는 복잡한 함수 형태를 허용하는 마테른 계열(Matern-class)이라는 설명(43–44). K 확산 계수에 수평 공간 변화가 있는 상관 길이 척도를 허용한다(46–47). 등방(isotropic) 또는 비등방(anisotropic) 상관의 수평 지도를 입력 NetCDF 파일에서 읽을 수 있다는 주석(47–49). 계산 효율을 위해 음적 확산 CG/CI 해법을 요구한다는 주석(49–50). 빈 주석 포함(45·51). |
| 52–64 | 시작 시 2행 `#if defined FOUR_DVAR` 안. 참고문헌 주석이다(52–64). Weaver와 Courtier의 2001년 구면 상관 모델링·일반화 확산 방정식 논문은 Q.J.R. Meteorol. Soc., 127, 1815–1846, doi:10.1002/qj.49712757518로 적혀 있다(54–56). Weaver·Tshimanga·Piacentini의 2016년 음적 확산 방정식·체비쇼프 반복 상관 연산자 논문은 같은 학술지 142, 455–471, doi:10.1002/qj.2664로 적혀 있다(58–61). 빈 주석·끝 구분선 포함(53·57·62–64). |
| 65–69 | 시작 시 2행 `#if defined FOUR_DVAR` 안. `# ifdef MULTI_SCALE_B` (65)의 참 분기는 `#  include "normalization_multi.h"` (66)로 normalization_multi.h를 끼워 넣는다. `# else` (67)의 불성립 분기는 `#  include "normalization_mono.h"` (68)로 normalization_mono.h를 끼워 넣는다. `# endif` (69)는 MULTI_SCALE_B 조건을 닫는다. 이 대상 파일에서는 두 포함 파일 내부를 판독하지 않았다. |
| 70–73 | 시작 시 2행 `#if defined FOUR_DVAR`의 참 분기 안. `#else` (70)는 FOUR_DVAR 불성립 분기로 전환한다. `MODULE normalization_mod` (71), `END MODULE normalization_mod` (72)로 내용 없는 모듈을 정의한다. `#endif` (73)는 2행 조건 전체를 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–50·65–69: 본문은 정규화·공분산·확산 방법을 주석으로 설명한다. FOUR_DVAR 참 분기는 MULTI_SCALE_B에 따라 normalization_multi.h 또는 normalization_mono.h를 포함한다. 이 파일 자체에는 정규화 계수를 계산하는 대입식이 없다.
- 20·28·52–61: 본문 주석은 Daley, 1992와 Weaver et al., 2016을 언급한다. References 목록은 Weaver·Courtier, 2001과 Weaver·Tshimanga·Piacentini, 2016을 적는다. Daley, 1992의 서지 항목은 이 목록에 없다.
