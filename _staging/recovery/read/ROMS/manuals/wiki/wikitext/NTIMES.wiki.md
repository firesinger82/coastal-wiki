---
file: models/ROMS/raw/manuals/wiki/wikitext/NTIMES.wiki
lines: 15
sha256: 07777ab8ed3519fb005223bb6282a400309701fe1c56b677401126f06f96b26c
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# NTIMES.wiki — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | ntimes / 정의 — 제목, Variables 구간 포함 지시문, 구분선과 정의를 포함한다(1–6). roms.in의 NTIMES가 현재 실행의 경압(baroclinic) 시간 단계 수를 설정한다(6). SOLVE3D를 정의하지 않은 순압 구성에서는 순압 시간 단계 수라고 설명한다(6). 기본값은 없다. 원문: `{{#lst:Variables\|ntimes}}` (2); `'''ntimes''' (set by <span class="blue">NTIMES</span> keyword in the [[roms.in]] file) is the total number of baroclinic timesteps in the current run. In a strictly barotropic configuration (i.e CPP option [[Options#SOLVE3D\|SOLVE3D]] is undefined) '''ntimes''' is the total number of barotropic timesteps. ` (6). |
| 8–15 | ntimes / 종료 단계와 기준 시각 — ntimes는 실행이 끝날 시간 단계를 정하며 계수가 항상 1에서 시작하지는 않는다고 강조한다(8). 초기 ocean_time이 0이 아닌 재시작이나 더 이른 기준 시각의 예를 든다(9–10). 2006년 4월 시작 예시의 시간·dt·ntimes 값과 즉시 종료 조건을 그대로 옮긴다(12). 내부 시간 기준을 옮길 때 dstart를 참고하라고 안내한다(15). 원문: `'''Note that ntimes determines the timestep on which the run will ''end'''''.  Be aware that time step counting does not necessarily always start from 1. This could be so if [[ocean_time]] in the initial conditions file is not zero such as when:` (8); `:# You restart a crashed run from a Restart or History file` (9); `:# You chose a reference time for [[ocean_time]] that precedes the time range you wish to simulate.` (10); `For example, if your forcing file data uses [[ocean_time]]&nbsp;=&nbsp;"seconds since 2006-01-01 00:00:00", but you wish only to model the period from 2006-04-01 onward, you would set [[ocean_time]]&nbsp;=&nbsp;7776000 (90 days since 2006-01-01 multiplied by 86400 seconds per day) in the initial conditions netcdf file. For [[Variables#dt\|dt]] of 180 seconds (480 timesteps per day) '''ntimes'''&nbsp;=&nbsp;7776480 would cause the run to conclude on 2006-04-02, i.e. it would only run for 1 day of simulated time.  If you set '''ntimes'''&nbsp;=&nbsp;480 thinking this would be 1 day of simulation you will find ROMS will simply end immediately saying it is already done because the end time you requested predates the initial conditions. ` (12); `However, see [[dstart]] for more information on how to shift the internal time keeping in ROMS without upsetting your [[ocean_time]]&nbsp;=&nbsp;"seconds since yyyy-mm-dd HH:MM:SS" convention.` (15). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12: 예시는 초기 `ocean_time`을 7776000초로 쓰고 `dt`를 180초로 쓴다. 예시는 `ntimes`를 7776480으로 지정하면 하루 뒤 종료한다고 쓴다. 7776480은 제시한 초 수 7776000에 하루의 시간 단계 수 480을 더한 값이다.
