---
file: models/ROMS/raw/source_code/roms/ROMS/Modules/mod_eoscoef.F
lines: 68
sha256: 252d8b4c4dbdc0a71f7c40916db1b7216ee1e8191081b87fd519675a051fe84c
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# mod_eoscoef.F — 판독 구간 기록

구간은 1행부터 68행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 시작 시 열린 전처리 조건은 없다. cppdefs.h를 포함하고 mod_eoscoef 모듈을 연다(1–2). NONLIN_EOS 조건에서 본문을 구성한다(3). 저작권·MIT/X 라이선스 주석이 있다(5–10). 주석은 현장 밀도(in situ density) 및 관련량을 잠재수온(potential temperature)·염분(salinity)·압력(pressure)의 비선형 상태방정식(nonlinear equation of state)으로 구하는 다항식 전개 계수라고 설명한다(12–16). 주석은 Jackett·McDougall,1992를 적는다(15–16). mod_kinds를 사용하고 implicit none을 선언한다(20–22). 원문: `#include "cppdefs.h"` (1); `#ifdef NONLIN_EOS` (3). |
| 24–35 | 시작 시 3행 `#ifdef NONLIN_EOS` 및 2행 mod_eoscoef 모듈 안. A00..A04,B00..B03,D00..D02를 real(r8),parameter 상수로 선언한다(24–35). 각 부호·계수·r8 접미사를 원문대로 옮긴다. 이 구간에는 계산 실행문이나 루틴 호출이 없다. 원문: `real(r8), parameter :: A00 = +1.909256e+04_r8` (24); `real(r8), parameter :: A01 = +2.098925e+02_r8` (25); `real(r8), parameter :: A02 = -3.041638e+00_r8` (26); `real(r8), parameter :: A03 = -1.852732e-03_r8` (27); `real(r8), parameter :: A04 = -1.361629e-05_r8` (28); `real(r8), parameter :: B00 = +1.044077e+02_r8` (29); `real(r8), parameter :: B01 = -6.500517e+00_r8` (30); `real(r8), parameter :: B02 = +1.553190e-01_r8` (31); `real(r8), parameter :: B03 = +2.326469e-04_r8` (32); `real(r8), parameter :: D00 = -5.587545e+00_r8` (33); `real(r8), parameter :: D01 = +7.390729e-01_r8` (34); `real(r8), parameter :: D02 = -1.909078e-02_r8` (35). |
| 36–49 | 시작 시 3행 `#ifdef NONLIN_EOS` 및 2행 모듈 안. E00..E03,F00..F02,G00..G03,H00..H02를 real(r8),parameter 상수로 선언한다(36–49). 각 부호·계수·r8 접미사를 원문대로 옮긴다. 이 파일은 이 상수들을 대입하는 상태방정식 실행식을 포함하지 않는다. 원문: `real(r8), parameter :: E00 = +4.721788e-01_r8` (36); `real(r8), parameter :: E01 = +1.028859e-02_r8` (37); `real(r8), parameter :: E02 = -2.512549e-04_r8` (38); `real(r8), parameter :: E03 = -5.939910e-07_r8` (39); `real(r8), parameter :: F00 = -1.571896e-02_r8` (40); `real(r8), parameter :: F01 = -2.598241e-04_r8` (41); `real(r8), parameter :: F02 = +7.267926e-06_r8` (42); `real(r8), parameter :: G00 = +2.042967e-03_r8` (43); `real(r8), parameter :: G01 = +1.045941e-05_r8` (44); `real(r8), parameter :: G02 = -5.782165e-10_r8` (45); `real(r8), parameter :: G03 = +1.296821e-07_r8` (46); `real(r8), parameter :: H00 = -2.595994e-07_r8` (47); `real(r8), parameter :: H01 = -1.248266e-09_r8` (48); `real(r8), parameter :: H02 = -3.508914e-09_r8` (49). |
| 50–68 | 시작 시 3행 `#ifdef NONLIN_EOS` 및 2행 모듈 안. Q00..Q05,U00..U04,V00..V02,W00을 real(r8),parameter 상수로 선언한다(50–64). 각 부호·계수·r8 접미사를 원문대로 옮긴다. 빈 줄과 NONLIN_EOS 종료 및 모듈 종료가 있다(65–68). 원문: `real(r8), parameter :: Q00 = +9.99842594e+02_r8` (50); `real(r8), parameter :: Q01 = +6.793952e-02_r8` (51); `real(r8), parameter :: Q02 = -9.095290e-03_r8` (52); `real(r8), parameter :: Q03 = +1.001685e-04_r8` (53); `real(r8), parameter :: Q04 = -1.120083e-06_r8` (54); `real(r8), parameter :: Q05 = +6.536332e-09_r8` (55); `real(r8), parameter :: U00 = +8.24493e-01_r8` (56); `real(r8), parameter :: U01 = -4.08990e-03_r8` (57); `real(r8), parameter :: U02 = +7.64380e-05_r8` (58); `real(r8), parameter :: U03 = -8.24670e-07_r8` (59); `real(r8), parameter :: U04 = +5.38750e-09_r8` (60); `real(r8), parameter :: V00 = -5.72466e-03_r8` (61); `real(r8), parameter :: V01 = +1.02270e-04_r8` (62); `real(r8), parameter :: V02 = -1.65460e-06_r8` (63); `real(r8), parameter :: W00 = +4.8314e-04_r8` (64); `#endif` (66). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
