---
file: models/ROMS/raw/source_code/roms/ROMS/Include/riverplume2.h
lines: 49
sha256: 85d39dde71a263acd5a49f598cf820d27382b055e3d65f517951b4f6cadf4678
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# riverplume2.h — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·Hyatt와 Signell의 하천 플룸 예시 설명 및 관련 URL 주석을 포함한다(1–11). RIVERPLUME2·roms_riverplume2.in·주석 종료·빈 줄을 포함한다(12–15). 주석의 URL 내용은 이 소스 파일 판독 범위에 포함하지 않았다. |
| 16–29 | 시작 시 열린 전처리 조건 없음. 운동량·DJ_GRADPS·수직 스플라인·TS_DIF2/MIX_GEO_TS·NONLIN_EOS·SALINITY·MASKING·SOLVE3D·AVERAGES를 정의한다(16–28). 빈 줄을 포함한다(29). 원문: `#define UV_ADV` (16); `#define UV_COR` (17); `#define UV_QDRAG` (18); `#define DJ_GRADPS` (19); `#define SPLINES_VDIFF` (20); `#define SPLINES_VVISC` (21); `#define TS_DIF2` (22); `#define MIX_GEO_TS` (23); `#define NONLIN_EOS` (24); `#define SALINITY` (25); `#define MASKING` (26); `#define SOLVE3D` (27); `#define AVERAGES` (28). |
| 30–39 | 시작 시 열린 전처리 조건 없음. LMD_MIXING을 정의한다(30). 해당 조건에서 LMD_RIMIX/LMD_CONVEC/LMD_SKPP/LMD_BKPP/LMD_NONLOCAL/RI_SPLINES를 정의한다(31–38). 빈 줄을 포함한다(39). 원문: `#define LMD_MIXING` (30); `#ifdef LMD_MIXING` (31); `# define LMD_RIMIX` (32); `# define LMD_CONVEC` (33); `# define LMD_SKPP` (34); `# define LMD_BKPP` (35); `# define LMD_NONLOCAL` (36); `# define RI_SPLINES` (37); `#endif` (38). |
| 40–49 | 시작 시 열린 전처리 조건 없음. 해석 격자·초기 조건·점원·표면 운동량/복사/염분/추적자 플럭스·바닥 염분/추적자 플럭스 옵션을 정의한다(40–48). 마지막 빈 줄을 포함한다(49). 원문: `#define ANA_GRID` (40); `#define ANA_INITIAL` (41); `#define ANA_PSOURCE` (42); `#define ANA_SMFLUX` (43); `#define ANA_SRFLUX` (44); `#define ANA_SSFLUX` (45); `#define ANA_STFLUX` (46); `#define ANA_BSFLUX` (47); `#define ANA_BTFLUX` (48). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
