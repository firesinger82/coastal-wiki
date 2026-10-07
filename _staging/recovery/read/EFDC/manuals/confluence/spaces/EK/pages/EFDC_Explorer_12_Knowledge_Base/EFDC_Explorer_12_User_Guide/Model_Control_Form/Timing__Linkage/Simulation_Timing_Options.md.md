---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Timing__Linkage/Simulation_Timing_Options.md
lines: 31
sha256: b2d6d2e6462a97365a888d1fb769411755bff25b66ce14618c5aadff1ec0c189
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Simulation_Timing_Options.md — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — Simulation Timing Options의 페이지 ID, URL, 버전, 갱신 시각, 계층을 수록한다(1–9). |
| 10–13 | 시작·종료·참조 기간 — EE10 시간 설정은 Timing 메뉴 우클릭으로 연다(10). 기준시각(reference date/time), 상대 Julian day, 시작·종료 시각, 참조 기간(reference period)의 정의와 예시 원문: `In this form, specify the time to start and end the run, along with the time stepping options and duration of the period. The *Reference Date/Time* (also known as the Base Date) is the time from which all Julian days are counted. *Time of Start* is the number of Julian days, relative to the *Reference Date/Time*, at which to begin the simulation. Changing the *Time of Start* will automatically update *Start/Date Time*. The *End Date/time* is calculated by adding the *Number of Reference Periods* to the *Start Date/time*. The *Duration of Reference Period* is used to define a project-specific meaningful period. This is often set to 24 hours to select a one day long reference period. The duration of the simulation is then set by specifying the number of reference periods. Other important options include:` (12) |
| 14–16 | Time Step / Dynamic Timestep Options — CFL 조건(Courant–Friedrichs–Lewy condition)에 관한 시간 간격 권고, Initialize, 고정 및 동적 시간 간격(dynamic time stepping)의 의미를 설명한다(14). Safety Factor의 조건·권고·예외·고정 시간 조건 원문: `- The *Time Step* should be at least an order of magnitude below the [*CFL Time Step*](/wiki/spaces/EK/pages/258998449/Model+Metrics). An initial value can be suggested by clicking the *Initialize* button. If fixed time-steps are used, this value will be used for the whole run. If dynamic time stepping is being used, then the time step can be seen as an initial or minimum time step, as EFDC+ will use multiples of this value.` (14) `- The *Dynamic Timestep Options* sub-frame allows the user to engage auto stepping by setting the *Safety Factor* to a positive number >0 and <1. Generally, the safety factor ought to be less than 0.8, but some runs work with a safety factor >1, and some require a value <0.3. If set to 0, it will result in fixed time steps.` (15) |
| 17–23 | 동적 시간 간격 산정 — CFL, 이류 물질의 양성(positivity), 수심 변화율의 세 방법을 조합한다(17–21). 모듈 조건과 전체 셀 최소값·안전계수 적용 원문: `  - For the model with the dynamic time step option, the EFDC+ calculates the required minimum time step by combining the three methods below:` (17) `    - Method 1: based on Courant–Friedrichs–Lewy condition` (19) `    - Method 2: based on Positivity of advected material (when the model includes one of temperature, salinity, dye, etc. module)` (20) `    - Method 3: based on Limit rate of depth change` (21) `  - The final time step is chosen as the minimum of the three methods for all the grid cells, then multiplied by the *Safety Factor*.` (22) `  - It should be noted that the initial time step is usually set by a small value. Then, this initial time step will be updated over time during the model simulation based on the dynamic time-stepping process described above.` (23) |
| 24–28 | 동적 시간 간격 추가 옵션 — Ramp-Up Loops, Maximum dH/dT, Growth Step, Maximum Time Step의 정의와 적용 조건이다(24–27). EFDC.INP 카드와 단위·조건 원문: `- The number of *Ramp-Up Loops* should also be set by the user; this is the number of initial iterations for which to hold the time step to a constant value during ramp-up.` (24) `- The *Maximum dH/dT* option is ignored if set to zero, but if >0, then EFDC (CALSTEP routine) will use these additional criteria to set the dynamic timestep.` (25) `- *Growth Step* is the minimum number of iterations for each time step before increasing the time step for the dynamic time stepping (DTDYN in C7 of EFDC.INP).` (26) `- *Maximum Time Step* is the maximum allowed time step in seconds.  If this value is too high, the model will crash.` (27) |
| 29–31 | Figure 1 — 로컬 그림을 직접 열었다(29). Simulation Timing Options 설정 화면이며 캡션을 포함한다(31). 화면 예시 값은 `Reference Date/Time: 2008-01-01 00:00:00`, `Start Date/Time: 2008-01-01 00:00:00`, `End Date/Time: 2008-01-17 00:00:00`, `Time of Start (days): 0`, `Number of Reference Periods: 16`, `Duration of Reference Period (hours): 24`, `Time Step (seconds): 0.1`, `Safety Factor: 0`, `# Ramp-up Loops: 1000`, `Maximum dH/dT: 0.3`, `Growth Step: 2`, `Maximum Time Step: 3600`이다(29 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행: 다수의 색상 CSS가 본문 시작에 남아 있다.
- 15행: auto stepping 활성화 조건은 `>0 and <1`이다. 같은 행은 일부 실행이 `safety factor >1`로 작동한다고도 적는다.
- 12행: 종료시각 설명은 시작시각에 Number of Reference Periods를 더한다고 적는다. 같은 행은 Duration of Reference Period를 별도로 정의하지만 종료시각 설명에는 기간 길이를 곱하는 항을 적지 않는다.

