---
file: models/ROMS/raw/source_code/roms/ROMS/Adjoint/ad_convolution.F
lines: 103
sha256: 4a3dc149b0c8da9f73c7459681d3f50833f7cad8ee1c9a6c99923b0f1613d877
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ad_convolution.F — 판독 구간 기록

구간은 1행부터 103행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 시작 시 열린 전처리 조건 없음. cppdefs.h를 포함한다(1). ADJOINT와 FOUR_DVAR가 모두 정의된 분기에서 자료동화(data assimilation) 제어벡터(control vector)의 각 변수에 일반화된 의사 확산(pseudo diffusion) 수반(adjoint) 연산자를 적용한다는 모듈 주석을 시작한다(2–17). 저작권·MIT/X 라이선스 안내를 둔다(5–9). 원문 조건·반복 범위·대입식·호출·전처리 지시: `#include "cppdefs.h"` (1); `#if defined ADJOINT && defined FOUR_DVAR` (2). |
| 19–41 | 시작 시 전처리 `#if defined ADJOINT && defined FOUR_DVAR` (2) 안. 주석의 공분산(covariance) 분해식은 `B = S C S` (21), `C = C^(1/2) C^(T/2)` (23), `C^(1/2) = G L^(1/2) W^(-1/2)                               TLM` (25), `C^(T/2) = W^(-1/2) L^(T/2) G                               ADM` (26)이다. S는 배경오차 표준편차(standard deviation) 대각행렬이며 G는 C의 대각 분산(variance)을 1로 맞추는 정규화(normalization) 계수이다(31–34). L은 접선형(tangent linear)·수반 확산 연산자, W는 면적·체적 계량(metric)의 대각행렬이다(35–37). T/2를 제곱근 연산자의 전치(transpose)로 설명한다(39–40). 이 구간은 실행식이 아닌 설명 주석이다. |
| 42–68 | 시작 시 전처리 `#if defined ADJOINT && defined FOUR_DVAR` (2) 안. 공간 상관의 퍼짐(spreading)을 의사 확산으로 모델링한다는 주석이다(43–47). 확산 계수는 상관 길이 척도(correlation length scale)의 제곱에 비례한다고 적는다(44–45). 다중 척도(multiscale)는 여러 공간 척도의 선형 결합이고 단일 척도(monoscale)는 하나의 척도를 사용한다(49–56). 다중 척도의 수평 연산자는 음해법(implicit)·켤레기울기법(Conjugate Gradient, CG)·체비쇼프 반복(Chebyshev Iterations, CI), 단일 척도의 수평 연산자는 양해법(explicit)이라고 적는다(58–63). 수평·수직 상관을 분리하고 두 접근의 수직 연산자는 음해법이라고 적는다(65–67). |
| 69–94 | 시작 시 전처리 `#if defined ADJOINT && defined FOUR_DVAR` (2) 안. 다중 척도 주석 식은 `B = SUM(Wi*Bi)` (69)이다. 가중치 Wi의 합을 1로 제한한다는 주석을 둔다(72). 공간적으로 변하는 등방성(isotropic)·비등방성(anisotropic) 수평 상관 지도는 NetCDF 입력으로 읽고 효율을 위해 CG/CI 음해법을 사용한다고 설명한다(76–80). Weaver·Courtier 2001과 Weaver·Tshimanga·Piacentini 2016 문헌의 서지·DOI를 적는다(84–91). 실행문은 없다. |
| 95–99 | 시작 시 전처리 `#if defined ADJOINT && defined FOUR_DVAR` (2) 안. MULTI_SCALE_B가 정의되면 ad_convolution_multi.h를 끼워 넣는다(95–96). 해당 else는 ad_convolution_mono.h를 끼워 넣는다(97–98). 척도 선택 전처리 분기를 닫는다(99). 포함 파일 내부를 이 파일의 행으로 계산하지 않는다. 원문 조건·반복 범위·대입식·호출·전처리 지시: `# ifdef MULTI_SCALE_B` (95); `#  include "ad_convolution_multi.h"` (96); `# else` (97); `#  include "ad_convolution_mono.h"` (98); `# endif` (99). |
| 100–103 | 시작 시 전처리 `#if defined ADJOINT && defined FOUR_DVAR` (2) 안. 상단 ADJOINT·FOUR_DVAR 조건의 else이다(100). 내용이 없는 ad_convolution_mod를 선언하고 종료한다(101–102). 상단 전처리 조건을 닫는다(103). 원문 조건·반복 범위·대입식·호출·전처리 지시: `#else` (100); `#endif` (103). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
