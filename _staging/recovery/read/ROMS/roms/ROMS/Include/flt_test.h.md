---
file: models/ROMS/raw/source_code/roms/ROMS/Include/flt_test.h
lines: 34
sha256: 28ad8da944cb36509896992d6236fb258b2835cb2925b1fc1acb4aa10258042a
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# flt_test.h — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·표류자 추적(floats tracking) 시험 주석과 FLT_TEST·2차원/3차원 ROMS 및 floats 입력 파일명을 포함한다(1–14). 빈 줄을 포함한다(15). |
| 16–25 | 시작 시 열린 전처리 조건 없음. UV_ADV/UV_QDRAG/UV_VIS2/MIX_S_UV·FLOATS·MASKING·해석 격자/초기 조건/표면 운동량 플럭스를 정의한다(16–24). 빈 줄을 포함한다(25). 원문: `#define UV_ADV` (16); `#define UV_QDRAG` (17); `#define UV_VIS2` (18); `#define MIX_S_UV` (19); `#define FLOATS` (20); `#define MASKING` (21); `#define ANA_GRID` (22); `#define ANA_INITIAL` (23); `#define ANA_SMFLUX` (24). |
| 26–34 | 시작 시 열린 전처리 조건 없음. SOLVE3D 조건에서 DJ_GRADPS·SPLINES_VDIFF/SPLINES_VVISC·BODYFORCE·ANA_BTFLUX/ANA_STFLUX를 정의한다(26–33). 마지막 빈 줄을 포함한다(34). 원문: `#ifdef SOLVE3D` (26); `# define DJ_GRADPS` (27); `# define SPLINES_VDIFF` (28); `# define SPLINES_VVISC` (29); `# define BODYFORCE` (30); `# define ANA_BTFLUX` (31); `# define ANA_STFLUX` (32); `#endif` (33). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
