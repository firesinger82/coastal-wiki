---
file: models/ROMS/raw/source_code/roms/ROMS/Include/damee_4.h
lines: 38
sha256: b9e48c67c03adb620d1d4a3756531277df46160351fbd8b84633f23637b05e7a
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# damee_4.h — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스와 북대서양(North Atlantic) DAMEE의 3/4도 해상도 설정 주석을 포함한다(1–10). DAMEE_4·roms_damee_4.in을 적는다(11–12). 주석 종료·빈 줄을 포함한다(13–14). |
| 15–28 | 시작 시 열린 전처리 조건 없음. 운동량·DJ_GRADPS·수직 스플라인·비선형 상태방정식·염분·SOLVE3D·MASKING·QCORRECTION·SRELAXATION·CURVGRID·AVERAGES를 정의한다(15–28). 원문: `#define UV_ADV` (15); `#define UV_COR` (16); `#define UV_QDRAG` (17); `#define DJ_GRADPS` (18); `#define SPLINES_VDIFF` (19); `#define SPLINES_VVISC` (20); `#define NONLIN_EOS` (21); `#define SALINITY` (22); `#define SOLVE3D` (23); `#define MASKING` (24); `#define QCORRECTION` (25); `#define SRELAXATION` (26); `#define CURVGRID` (27); `#define AVERAGES` (28). |
| 29–38 | 시작 시 열린 전처리 조건 없음. LMD_MIXING을 정의하고 그 조건 안에서 LMD_RIMIX/LMD_CONVEC/LMD_SKPP/LMD_NONLOCAL/RI_SPLINES를 정의한다(29–36). ANA_BSFLUX·ANA_BTFLUX를 공통 정의한다(37–38). 원문: `#define LMD_MIXING` (29); `#ifdef LMD_MIXING` (30); `# define LMD_RIMIX` (31); `# define LMD_CONVEC` (32); `# define LMD_SKPP` (33); `# define LMD_NONLOCAL` (34); `# define RI_SPLINES` (35); `#endif` (36); `#define ANA_BSFLUX` (37); `#define ANA_BTFLUX` (38). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
