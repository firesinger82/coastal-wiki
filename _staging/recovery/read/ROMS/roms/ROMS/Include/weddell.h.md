---
file: models/ROMS/raw/source_code/roms/ROMS/Include/weddell.h
lines: 41
sha256: a7600087b5a7e9c1cfdfc41547703e359794012384b5e948b07871d25174410f
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# weddell.h — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 저작권·MIT/X 형식 라이선스 안내(1–7). 주석은 이상화한 Weddell Sea의 조석(tides)·빙붕(ice shelf) 시험, 응용 플래그 WEDDELL, 입력 파일 roms_wedell.in을 적는다(9–12). |
| 15–31 | UV_ADV·DJ_GRADPS·UV_COR·UV_QDRAG·SPLINES_VDIFF·SPLINES_VVISC·SOLVE3D·SALINITY·NONLIN_EOS·CURVGRID·ICESHELF·AVERAGES·RADIATION_2D를 정의한다(15–31). UV_VIS4·MIX_S_UV·TS_DIF4·MIX_GEO_TS는 해제한다(19–20·23–24). 조건부 전처리 블록은 없다. 전처리 원문: `#define UV_ADV` (15); `#define DJ_GRADPS` (16); `#define UV_COR` (17); `#define UV_QDRAG` (18); `#undef  UV_VIS4` (19); `#undef  MIX_S_UV` (20); `#define SPLINES_VDIFF` (21); `#define SPLINES_VVISC` (22); `#undef  TS_DIF4` (23); `#undef  MIX_GEO_TS` (24); `#define SOLVE3D` (25); `#define SALINITY` (26); `#define NONLIN_EOS` (27); `#define CURVGRID` (28); `#define ICESHELF` (29); `#define AVERAGES` (30); `#define RADIATION_2D` (31). |
| 32–41 | ANA_GRID·ANA_INITIAL·ANA_FSOBC·ANA_M2OBC·ANA_SMFLUX·ANA_STFLUX·ANA_SSFLUX·ANA_SRFLUX·ANA_BSFLUX·ANA_BTFLUX를 무조건 정의한다(32–41). 루틴 호출과 수치 계산식은 없다. 전처리 원문: `#define ANA_GRID` (32); `#define ANA_INITIAL` (33); `#define ANA_FSOBC` (34); `#define ANA_M2OBC` (35); `#define ANA_SMFLUX` (36); `#define ANA_STFLUX` (37); `#define ANA_SSFLUX` (38); `#define ANA_SRFLUX` (39); `#define ANA_BSFLUX` (40); `#define ANA_BTFLUX` (41). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9·11–12: 시험 이름과 응용 플래그에는 Weddell·WEDDELL을 쓰지만 입력 파일 주석은 `roms_wedell.in` (12)으로 적혀 있다. 입력 파일의 실제 존재와 이름은 이 파일에서 확인하지 않았다.
