---
file: models/ROMS/raw/source_code/roms/ROMS/Tangent/tl_convolution.F
lines: 103
sha256: 68428011ae56466acd72afb8dcd94457186ef9b7f24d8c655b8ab410842b36d0
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# tl_convolution.F — 판독 구간 기록

구간은 1행부터 103행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 전처리 바깥에서 `#include "cppdefs.h"` (1)로 cppdefs.h를 포함하고 `#if defined TANGENT && defined FOUR_DVAR` (2) 조건을 연다. 저작권·라이선스 주석(3–9)이 있다. 배경 오차 공분산(background-error covariance) B의 영향을 제어 벡터(control vector)에 적용하는 접선 선형(tangent-linear) 유사 확산(pseudo-diffusion) 연산자라는 모듈 설명이 있다(11–17). 이 설명은 주석이다. |
| 19–42 | 시작 시 `#if defined TANGENT && defined FOUR_DVAR` (2) 안. 주석의 공분산·상관 행렬(correlation matrix)·제곱근 연산자 관계는 `!!   B = S C S                                                         !` (21), `!!   C = C^(1/2) C^(T/2)                                               !` (23), `!!   C^(1/2) = G L^(1/2) W^(-1/2)                               TLM    !` (25) `!!   C^(T/2) = W^(-1/2) L^(T/2) G                               ADM    !` (26)이다. S는 배경 오차 표준편차(standard deviation)의 대각 행렬이며, G는 C의 대각 분산(variance)을 1로 맞추는 정규화 계수(normalization coefficient)이고 W는 면적·체적 계량 대각 행렬이라는 설명이 있다(30–37). T/2는 제곱근 연산자의 전치(transpose)·수반(adjoint)을 뜻한다는 주석이다(39–40). 실행 대입식은 이 구간에 없다. |
| 43–81 | 시작 시 `#if defined TANGENT && defined FOUR_DVAR` (2) 안. 확산 계수 K가 상관 길이 스케일(correlation length scale)의 제곱에 비례하고, 스케일은 상수 또는 공간 가변일 수 있다는 주석이다(43–47). 다중 스케일(multiscale)은 여러 공간 스케일의 선형 결합, 단일 스케일(monoscale)은 한 스케일이라는 설명이 있다(49–56). 다중 스케일 수평 연산자는 음해법(implicit method)·켤레 기울기법(Conjugate Gradient, CG)·체비쇼프 반복(Chebyshev Iterations, CI)을 사용한다는 주석이다(58–60). 단일 스케일 수평 연산자는 양해법(explicit method), 수직 연산자는 두 방식에서 음해법이며 수평·수직 상관은 분리 가능하다는 주석이다(62–67). 가중합 설명은 `!! The multiscale concept, expressed as B = SUM(Wi*Bi), represents a   !` (69)이며 Wi의 합은 1, 상관은 Matern 계열이라고 적는다(70–74). 등방성(isotropic)·비등방성(anisotropic) 공간 가변 상관을 NetCDF에서 읽을 수 있다는 주석이다(76–80). 실행 대입식이나 호출은 없다. |
| 82–94 | 시작 시 `#if defined TANGENT && defined FOUR_DVAR` (2) 안. Weaver·Courtier(2001)와 Weaver·Tshimanga·Piacentini(2016)의 논문 제목·권·쪽·DOI를 주석으로 적는다(84–91). 주석 구분선과 빈 주석이 이어진다(92–94). |
| 95–103 | 시작 시 `#if defined TANGENT && defined FOUR_DVAR` (2) 안. `# ifdef MULTI_SCALE_B` (95)에서 `#  include "tl_convolution_multi.h"` (96)로 tl_convolution_multi.h를 포함한다. `# else` (97)에서는 `#  include "tl_convolution_mono.h"` (98)로 tl_convolution_mono.h를 포함한다. `# endif` (99)로 MULTI_SCALE_B를 닫는다. `#else` (100)는 2행 조건 불성립 분기이며 빈 tl_convolution_mod 모듈만 선언한다(101–102). `#endif` (103)로 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
