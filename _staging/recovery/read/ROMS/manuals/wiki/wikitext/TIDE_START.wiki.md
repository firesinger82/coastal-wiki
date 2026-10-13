---
file: models/ROMS/raw/manuals/wiki/wikitext/TIDE_START.wiki
lines: 21
sha256: 51a9a360c808724e66b74ad164f897cb008a466ebf35f77276238d81918ad5f4
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# TIDE_START.wiki — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | tide_start / 조석 기준 시각 — 제목·Variables 전재 호출·구분선 뒤, 조화 조석 성분(harmonic tidal constituents)과 ROMS의 시간 원점이 다르면 위상 오차가 생길 수 있다고 설명한다(1–6). roms.in의 days 단위 tide_start로 위상을 이동하며 set_tides.F에서 초로 바꿔 사용하는 합성식을 제시한다(8–10). 원문: `{{#lst:Variables\|tide_start}}` (2); `If the time origin for the harmonic tidal constituents is not the same as the time origin used internally by ROMS then the tidal phase will be in error. To accommodate this possibility, the parameter '''tide_start''' in units of '''days''' can be used to make the appropriate shift to the phase of the harmonic tidal forcing. The value set in [[roms.in]].` (6); `The parameter is used in routine [[set_tides.F]] after conversion into seconds:` (8); `\eta = \sum_{i=1}^{N} A_i \cos \frac{2\pi (t-\text{tide}{\_}\text{start} - \phi_i)}{T_i}` (10). |
| 13–21 | tide_start / 입력 예제·적용 조건 — ROMS 기준일과 조석 기준일이 다른 예제, TIDE_START의 입력값·단위를 제시한다(13–15). 이전 조석 기준일이면 대체로 음수가 되며 DSTART는 사용자 설정 방식에 영향을 주지 않는다고 적는다(17–19). SSH_TIDES·UV_TIDES 옵션과 조화 조석 NetCDF 파일을 요구한다(21). 원문: `For example, if the date corresponding to <math>\text{tdays}=0</math> in ROMS is 1-Jan-2006, i.e. [[ocean_time]] has the netcdf units attribute "days since 2006-01-01 00:00:00", but the harmonic forcing data was computed assuming a base date for time of 2005-01-01 00:00:00, then set the value in your [[roms.in]] with` (13); `      TIDE_START = -365.0d0              ! days` (15); `Note that TIDE_START will typically be negative for tide harmonic reference times that predate the model time origin.` (17); `The value of [[dstart\|DSTART]] '''does not''' affect how the user sets '''tide_start'''.` (19); `Tidal forcing is activated by CPP options [[SSH_TIDES]] and [[UV_TIDES]] and requires a tide harmonic forcing netcdf file.` (21); `\text{tdays}=0` (13). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행: 합성식의 `N`, `A_i`, `\phi_i`, `T_i`는 이 파일에 별도 정의가 없다.
