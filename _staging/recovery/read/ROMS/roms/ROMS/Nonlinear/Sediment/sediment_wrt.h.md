---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Sediment/sediment_wrt.h
lines: 105
sha256: 94f2ffc4e4743fa879a51768cba0ca43657a4a27148335fb955c8b0e65c0016c
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# sediment_wrt.h — 판독 구간 기록

구간은 1행부터 105행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–17 | 파일 내부에서 열린 전처리 조건 없음. 저작권·MIT/X 라이선스 머리말(1–13), 빈 줄과 퇴적물 입력 매개변수(sediment input parameter) 출력 구분 주석(14–17). NetCDF 파일에 입력 매개변수를 쓰고 wrt_info.F에 포함된다는 주석(9–10). 독립 루틴 선언은 이 파일에 없다. |
| 18–30 | 파일 내부에서 열린 전처리 조건 없음. `netcdf_put_fvar`로 minlayer_thick(ng)(18–20), newlayer_thick(ng)(23–25), sg_zwbl(ng)(27–29)을 같은 이름의 스칼라 변수로 출력. 모든 호출은 시작·개수 인수 (/0/)·(/0/)와 ncid=ncid 사용. `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (21·26·30)로 호출 후 오류가 있으면 반환. 매개변수 계산이나 기본값 설정은 이 블록에 없다. 빈 줄(22) 포함. |
| 31–63 | 파일 내부에서 열린 전처리 조건 없음. `#ifdef BEDLOAD` (31)에서 `netcdf_put_fvar`로 bedload_coeff(ng)(32–34) 출력. `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (35). `!# ifdef BEDLOAD_VANDERA` (37)는 Fortran 주석이다. sedslope_crit_wet(38–40), sedslope_crit_dry(42–44), slopefac_wet(46–48), slopefac_dry(50–52), bedload_vandera_alphaw(54–56), bedload_vandera_alphac(58–60)를 각 (ng) 값·(/0/)·(/0/)·ncid 인수로 출력. `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (41·45·49·53·57·61). `!# endif` (62)도 주석. 실제 BEDLOAD 종료는 `#endif` (63). |
| 64–80 | 파일 내부에서 열린 전처리 조건 없음. 빈 줄(64·70·75), `!#ifdef ANA_SEDIMENT` (65)는 Fortran 주석. `netcdf_put_fvar`로 Sd50(:,ng)(66–68), Srho(:,ng)(71–73), Csed(:,ng)(76–78)를 출력. 시작 (/1/)·크기 (/NST/)·ncid=ncid 사용. `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (69·74·79). `!#endif` (80)는 주석. 이 구간에는 실행되는 ANA_SEDIMENT 전처리 조건이 없다. |
| 81–105 | 파일 내부에서 열린 전처리 조건 없음. `netcdf_put_fvar`로 Wsed(:,ng)(82–84), Erate(:,ng)(87–89), tau_ce(:,ng)(92–94), tau_cd(:,ng)(97–99), poros(:,ng)(102–104)를 같은 이름의 입도별 배열로 출력. 각 호출은 시작 (/1/)·크기 (/NST/)·ncid=ncid 사용. `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (85·90·95·100·105). 빈 줄(81·86·91·96·101) 포함. 배열 값의 계산·단위 변환·기본값 대입은 이 파일에 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 31–63: BEDLOAD는 실제 전처리 조건이다. BEDLOAD_VANDERA의 시작·끝처럼 보이는 37·62행은 !로 시작하는 주석이다. 따라서 해당 줄은 CPP 조건을 열거나 닫지 않는다.
- 65–80: ANA_SEDIMENT의 시작·끝처럼 보이는 65·80행은 !로 시작하는 주석이다. Sd50·Srho·Csed 출력 호출은 이 파일 내부의 ANA_SEDIMENT 전처리 조건으로 감싸져 있지 않다.
