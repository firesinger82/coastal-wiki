---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/step2d.F
lines: 24
sha256: eda3c5a2c893f2cbe510ddaac58341d3e827aa1d5c345192cd3d9b4f02c8e3aa
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# step2d.F — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | 시작 시 열린 전처리 조건 없음; Fortran 루틴·모듈 밖. cppdefs.h를 포함한다(1). NONLINEAR에서 자유수면(free surface)과 2차원 비선형 운동량 방정식의 빠른 예측자/수정자(predictor/corrector) 시간 단계를 수행한다는 머리말이다(2–12). SOLVE3D 주석은 3차원 계산에서 고주파 신호(high frequency signal)를 감쇠하는 빠른 시간 단계 필터링(time filtering) 변수를 계산한다고 적는다(13–16). 저작권·라이선스·구분 주석과 빈 주석을 포함한다(3–19). 원문 전처리·조건·반복·대입: `#include "cppdefs.h"` (1); `#ifdef NONLINEAR` (2); `# ifdef SOLVE3D` (13); `# endif` (16). |
| 20–24 | 시작 시 전처리 조건 `#ifdef NONLINEAR` (2) 안; Fortran 루틴·모듈 밖. NONLINEAR 참 분기는 step2d_LF_AM3.h를 끼워 넣는다(20). 이 판독은 include 파일의 내부까지 확장하지 않았다. NONLINEAR else는 내용 없는 step2d_mod 모듈을 정의한다(21–23). 바깥 전처리 조건을 닫고 파일이 끝난다(24). 원문 전처리·조건·반복·대입: `# include "step2d_LF_AM3.h"` (20); `#else` (21); `#endif` (24). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
