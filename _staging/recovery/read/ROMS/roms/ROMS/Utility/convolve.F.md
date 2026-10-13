---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/convolve.F
lines: 99
sha256: 7bc300de3f6b858fecb775cb7627a017baac094f5fb8090949ed38ab54b2c482
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# convolve.F — 판독 구간 기록

구간은 1행부터 99행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | `#include "cppdefs.h"` (1)로 cppdefs.h를 포함한다. `#ifdef FOUR_DVAR` (2)는 아래 설명과 구현 포함을 감싼다. 저작권·MIT/X 라이선스(4–9). 주석은 배경오차 공분산(background-error covariance) B의 퍼짐(spreading)·평활화(smoothing)를 제어벡터(control vector)에 적용한다고 적는다(11–13). 큰 B를 직접 계산하지 않고 상관 길이 척도(correlation length scale)의 제곱에 비례하는 확산계수(diffusion coefficient)의 의사 확산(pseudo-diffusion) 연산자 합성곱(convolution)으로 모델링한다는 Daley 1992 인용 주석(14–17). 지정 상관함수(correlation function)로 관측정보를 공간 배분한다는 설명(18–20). |
| 22–44 | 시작 시 2행 `#ifdef FOUR_DVAR` 안. 배경오차 공분산과 제곱근 분해(square-root factorization)의 주석 식 원문: `!!   B = S C S                                                         !` (24); `!!   C = C^(1/2) C^(T/2)                                               !` (26); `!!   C^(1/2) = G L^(1/2) W^(-1/2)                               TLM    !` (28); `!!   C^(T/2) = W^(-1/2) L^(T/2) G                               ADM    !` (29). B는 공분산, S는 배경오차 표준편차(standard deviation) 대각행렬, C는 대칭 상관행렬, G는 C의 대각 분산(variance)을 1로 맞추는 정규화(normalization), L은 접선선형(tangent linear)·수반(adjoint) 확산 연산자, W는 국소 면적·체적 계량(metric) 대각행렬이라는 설명(33–40). T/2는 제곱근 연산자의 전치(transpose)·수반이라는 주석(42–43). |
| 45–77 | 시작 시 2행 `#ifdef FOUR_DVAR` 안. 주석은 다중 척도(multiscale)의 큰/작은 공간 척도 선형결합이 넓은 구조와 미세 특징을 나타내고 척도 앨리어싱(scale aliasing)을 줄인다고 적으며 Weaver 등 2016을 인용한다(45–52). 다중 척도 수평 의사 확산은 공액기울기(conjugate gradient, CG)와 Chebyshev 반복(Chebyshev iteration, CI)을 쓰는 음해법(implicit), 단일 척도(monoscale)는 양해법(explicit)(54–59). 수평·수직 오차상관은 분리 가능(separable)하며 수직 확산은 두 방법 모두 음해법이라는 주석(61–63). 다중 척도 가중합 식 원문은 `!! The multiscale concept, expressed as B = SUM(Wi*Bi), represents a   !` (65). 주석은 Wi 합이 1이며 상관함수가 Matern 계열이라고 적는다(66–70). 수평에서 공간적으로 변하는 등방성(isotropic)·비등방성(anisotropic) 상관 길이 지도는 NetCDF 입력으로 지정하며 음해법 CG/CI가 필요하다고 적는다(72–76). 이 구간은 실행문 없이 설명 주석이다. |
| 78–90 | 시작 시 2행 `#ifdef FOUR_DVAR` 안. 참고문헌 주석은 Weaver/Courtier 2001의 일반화 확산방정식(generalized diffusion equation)·구면 상관 모델링과 DOI 10.1002/qj.49712757518(80–82), Weaver/Tshimanga/Piacentini 2016의 음해법 확산방정식·Chebyshev 반복과 DOI 10.1002/qj.2664(84–87)를 적는다. 구분 주석·빈 주석도 포함(78–79·83·88–90). |
| 91–99 | 시작 시 2행 `#ifdef FOUR_DVAR` 안. MULTI_SCALE_B이면 convolve_multi.h, 그 else이면 convolve_mono.h를 포함한다(91–95). 포함 파일 내부는 이 대상 파일의 판독 범위에 포함하지 않았다. FOUR_DVAR의 else(96)는 내용 없는 convolve_mod의 시작/종료를 직접 둔다(97–98). FOUR_DVAR 조건 종료(99). 전처리 원문: `# ifdef MULTI_SCALE_B` (91); `#  include "convolve_multi.h"` (92); `# else` (93); `#  include "convolve_mono.h"` (94); `# endif` (95); `#else` (96); `#endif` (99). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 17·78–87: 확산계수 설명은 Daley, 1992를 인용한다. 이 파일의 References 절은 Weaver/Courtier 2001과 Weaver/Tshimanga/Piacentini 2016만 열거한다.
