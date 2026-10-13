---
file: models/ROMS/raw/source_code/roms/ROMS/Include/channel.h
lines: 77
sha256: 75cf8a8457ad840fd45913dbd6e84f5adb0ecef6e792b3953e4609a96f5571af
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# channel.h — 판독 구간 기록

구간은 1행부터 77행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·주기적 균일 수로(periodic uniform channel) 설정과 CHANNEL·roms_channel.in 주석을 포함한다(1–14). 주석은 build.sh의 MY_CPP_FLAGS로 구동기(driver) 하나를 선택하도록 적고 사용 가능한 수반(adjoint)·접선 선형(tangent linear)·4D-Var·검사 옵션을 열거한다(15–34). 빈 줄을 포함한다(35–36). |
| 37–60 | 시작 시 열린 전처리 조건 없음. 비선형 기본 상태(nonlinear basic state) 구분 주석 뒤 UV_ADV/UV_COR/UV_LDRAG/UV_VIS2·ANA_GRID/ANA_INITIAL을 정의한다(37–49). SOLVE3D 조건에서 DJ_GRADPS/TS_DIF2/MIX_S_TS/MIX_S_UV와 해석 표면 운동량/추적자·바닥 추적자 플럭스를 정의한다(51–59). 빈 줄을 포함한다(60). 원문: `#define UV_ADV` (43); `#define UV_COR` (44); `#define UV_LDRAG` (45); `#define UV_VIS2` (46); `#define ANA_GRID` (48); `#define ANA_INITIAL` (49); `#ifdef SOLVE3D` (51); `# define DJ_GRADPS` (52); `# define TS_DIF2` (53); `# define MIX_S_TS` (54); `# define MIX_S_UV` (55); `# define ANA_SMFLUX` (56); `# define ANA_STFLUX` (57); `# define ANA_BTFLUX` (58); `#endif` (59). |
| 61–77 | 시작 시 열린 전처리 조건 없음. NLM_DRIVER이면 AVERAGES를 정의한다(61–63). OUT_DOUBLE을 공통 정의한다(65). 수반 기반 알고리즘 구분 주석 뒤 OPT_PERTURBATION 조건에서 FORWARD_READ와 FORWARD_MIXING을 정의한다(67–76). 마지막 빈 줄을 포함한다(77). 원문: `#ifdef NLM_DRIVER` (61); `# define AVERAGES` (62); `#endif` (63); `#define OUT_DOUBLE` (65); `#ifdef OPT_PERTURBATION` (73); `# define FORWARD_READ` (74); `# define FORWARD_MIXING` (75); `#endif` (76). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
