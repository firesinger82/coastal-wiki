---
file: models/ROMS/raw/source_code/roms/ROMS/Include/windbasin.h
lines: 27
sha256: 09f703275601def7008d9bfa87c87213d876f74dcfb3cb6e6e667f10af5a5353
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# windbasin.h — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 저작권·MIT/X 형식 라이선스 안내(1–7). 주석은 바람으로 구동하는 일정 코리올리(Coriolis) 분지 시험, 응용 플래그 WINDBASIN, 입력 파일 roms_windbasin.in을 적는다(9–12). |
| 15–27 | UV_ADV를 해제한다(15). UV_COR·UV_QDRAG·SPLINES_VDIFF·SPLINES_VVISC·SOLVE3D·AVERAGES·ANA_GRID·ANA_INITIAL·ANA_SMFLUX·ANA_STFLUX·ANA_BTFLUX를 무조건 정의한다(16–26). 마지막 빈 줄을 포함한다(27). 조건부 전처리 블록과 루틴 호출은 없다. 전처리 원문: `#undef UV_ADV` (15); `#define UV_COR` (16); `#define UV_QDRAG` (17); `#define SPLINES_VDIFF` (18); `#define SPLINES_VVISC` (19); `#define SOLVE3D` (20); `#define AVERAGES` (21); `#define ANA_GRID` (22); `#define ANA_INITIAL` (23); `#define ANA_SMFLUX` (24); `#define ANA_STFLUX` (25); `#define ANA_BTFLUX` (26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
