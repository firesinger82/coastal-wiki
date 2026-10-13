---
file: models/ROMS/raw/source_code/roms/ROMS/Include/basin.h
lines: 29
sha256: 5029d4be5c557ad9c933fa6f26c6eee4bf5cbe3e779809b2dc76a11c823b16de
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# basin.h — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·Big Bad Basin 설정 주석을 포함한다(1–10). 적용 매크로 BASIN과 입력 roms_basin.in을 적는다(11–12). 주석 종료·빈 줄을 포함한다(13–14). |
| 15–24 | 시작 시 열린 전처리 조건 없음. 운동량 이류(momentum advection) UV_ADV·코리올리(Coriolis) UV_COR·바닥 이차 항력(quadratic bottom drag) UV_QDRAG·4차 수평 점성(biharmonic viscosity) UV_VIS4·MIX_S_UV를 정의한다(15–19). DJ_GRADPS·수직 스플라인(spline) SPLINES_VDIFF/SPLINES_VVISC·SOLVE3D·BODYFORCE를 정의한다(20–24). 원문: `#define UV_ADV` (15); `#define UV_COR` (16); `#define UV_QDRAG` (17); `#define UV_VIS4` (18); `#define MIX_S_UV` (19); `#define DJ_GRADPS` (20); `#define SPLINES_VDIFF` (21); `#define SPLINES_VVISC` (22); `#define SOLVE3D` (23); `#define BODYFORCE` (24). |
| 25–29 | 시작 시 열린 전처리 조건 없음. 해석 격자·초기 조건·표면 운동량 플럭스·표면 추적자 플럭스·바닥 추적자 플럭스용 ANA_GRID/ANA_INITIAL/ANA_SMFLUX/ANA_STFLUX/ANA_BTFLUX를 정의한다(25–29). 원문: `#define ANA_GRID` (25); `#define ANA_INITIAL` (26); `#define ANA_SMFLUX` (27); `#define ANA_STFLUX` (28); `#define ANA_BTFLUX` (29). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
