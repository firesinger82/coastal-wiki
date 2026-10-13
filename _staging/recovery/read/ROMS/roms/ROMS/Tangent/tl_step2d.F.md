---
file: models/ROMS/raw/source_code/roms/ROMS/Tangent/tl_step2d.F
lines: 24
sha256: 2bfab91997ba27a3d22fd02ce9f5b7193e8b52870cf13e0e50401a3a11e8dbdc
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# tl_step2d.F — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 시작 시 전처리 조건 없음; 열린 바깥 블록 없음. `cppdefs.h`를 포함하고 TANGENT 조건을 연다(1–2). 저작권·라이선스 주석(4–9). 자유수면(free surface)과 2차원 운동량의 접선 선형(tangent linear) 방정식에 예측자/수정자(predictor/corrector)의 빠른 시간 단계(fast time step)를 수행한다는 주석(11–12). 원문: `#include "cppdefs.h"` (1); `#ifdef TANGENT` (2). |
| 13–24 | 시작 시 전처리 조건 2행 `#ifdef TANGENT` 안; 열린 바깥 블록 없음. SOLVE3D 주석은 3차원 실행에서 모든 빠른 시간 단계의 시간 필터링(time filtering) 변수를 계산하여 고주파 신호를 감쇠한다고 적는다(13–16). 구분 주석·빈 주석(17–19). TANGENT 경로의 실제 구현은 `tl_step2d_LF_AM3.h`를 끼워 넣는다(20). 포함 파일 내부는 이번 대상에 없으므로 판독하지 않았다. TANGENT의 #else에는 비어 있는 tl_step2d_mod 모듈만 정의된다(21–23). 전처리 조건 종료(24). 원문: `# ifdef SOLVE3D` (13); `# endif` (16); `# include "tl_step2d_LF_AM3.h"` (20); `#else` (21); `#endif` (24). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
