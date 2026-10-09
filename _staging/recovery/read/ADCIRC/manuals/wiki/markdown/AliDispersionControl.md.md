---
file: models/ADCIRC/raw/manuals/wiki/markdown/AliDispersionControl.md
lines: 110
sha256: 9ede6039688018042237cbb98f2e7dab91e09af78204c669ed94a71fe9796ebc
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# AliDispersionControl.md — 판독 구간 기록

구간은 1행부터 110행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 제목·판본 표기·빈 줄을 포함한다(1–4). 기능·Version — 탄성 지구(elastic Earth) 위 압축성 바다(compressible ocean)의 매우 긴 파에 대한 분산(dispersion) 보정이다(5). `fort.24`의 자기인력 및 하중 조석(self-attraction and loading tide)을 대신하여 사용할 목적과 `IM`의 적용 조건을 옮긴다(5). 버전 55 이상의 기술 미리보기(technical preview)이며 이론 작업이 진행 중이라고 적는다(9–15). 원문: `Ali's Dispersion Correction is a correction to the dispersive behavior of very long waves in a compressible ocean on an elastic Earth. It is intended to be used in lieu of the self-attraction and loading tide prescribed through the [fort.24 file](/Fort.24_file). It should be used with the sixth-digit of [IM](/IM) equal to 3 (fully implicit gravity wave term).` (5); ` &#8805;  55 ` (11); `This is considered a technical preview in version 55. Theoretical work is still ongoing.` (15). |
| 17–29 | Controlling Dispersive Behavior — `fort.15` 마지막의 namelist 존재로 기능을 시작한다(19). 예제의 실수들은 기본값이라고 명시한다(19–20). 논리 플래그의 기본값·음속 단위·음수의 의미·멱법칙(power law) 상수와 지수 이름을 원문 그대로 옮긴다(22–28). 예제의 `CAliDisp=T`와 논리 플래그 기본값 `F=false`를 구분한다. 원문: `The feature is triggered by the presence of the &AliDispersionControl namelist at the bottom of the [fort.15 file](/Fort.15_file). Here is an example of how this line is used (the following floats are the default values):` (19); `` `&AliDispersionControl CAliDisp=T, Cs=1500.0, Ad = 0.0050189, Bd = 0.23394/` `` (20); ``- `CAliDisp` logical flag to turn Ali's dispersion correction on (F=false by default).`` (22); ``- `Cs` is the speed of sound in water [m/s] for the Mach number based dispersive correction. Set Cs to a negative value to turn the Mach number based correction off.`` (24); ``- `Ad` the power law constant.`` (26); ``- `Bd` the power law exponent.`` (28). |
| 30–85 | Controlling Dispersive Behavior / 보정식 — 마하수(Mach number) 제곱과 수심 멱법칙 항을 사용하는 보정식의 펼쳐진 기호·빈 줄·완전한 LaTeX를 포함한다(30–85). 원문: `    {\displaystyle Correction=1-{\frac {Ma^{2}}{4}}-{A_{d}}H^{B_{d}}}` (84). |
| 86–110 | Controlling Dispersive Behavior / 마하수 — 마하수 식의 펼쳐진 기호와 완전한 LaTeX를 포함한다(87–109). H는 전체 수심이라고 정의한다(110). 원문: `    {\displaystyle Ma={\frac {\sqrt {gH}}{Cs}}}` (108); `) and H is the total water depth.` (110). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 108: 마하수 식의 `g`를 이 파일에서 정의하지 않는다.
