---
file: models/ADCIRC/raw/manuals/wiki/markdown/ADCIRC2D_.md
lines: 399
sha256: 87e79b1a0d1b95e9354f2aeda3fb0c6bd3ae8fdf9daf1b96970561b4e73b7e47
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# ADCIRC2D_.md — 판독 구간 기록

구간은 1행부터 399행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 제목·판본 표기·개발 중 경고·빈 줄·목차를 포함한다(1–18). ADCIRC2D+ — 순압(barotropic) 수심 평균 체계에 밀도 구동 경압(baroclinic) 효과를 넣는 모드이다(7). 더 성긴 해양 대순환모델(Ocean General Circulation Model, OGCM)의 수온·염분장과 결합하는 방식과 관련 논문을 소개한다(7). |
| 19–26 | Version — 버전 56 이상을 표시한다(21–23). 일부 기능은 v55에 있으나 개선·수정된 기능은 v56 이상에만 있다고 설명한다(25). 원문: ` &#8805;  56 ` (23); `Some of the capability of ADCIRC2D+ is available in v55; however improvements and modifications were made that are present only in v56 and above.` (25). |
| 27–100 | Governing Equations / 운동량식 시작 — GWCE를 사용하는 수정 천수방정식(shallow water equations)을 설명한다(29). 운동량 방정식에는 경압 압력경사와 내부파 항력(internal wave drag) 항이 포함된다(29). 운동량식의 펼쳐진 기호 전반부를 포함하며 식은 다음 구간으로 이어진다(31–100). |
| 101–170 | Governing Equations / 운동량식 계속 — 자유수면·조석 항, 경압 압력경사, 표면·저면 응력과 내부파 항력 항을 포함한 운동량식의 펼쳐진 기호 후반부와 완전한 LaTeX를 포함한다(101–169). 원문: `    {\displaystyle {\frac {\partial \mathbf {U} }{\partial t}}+\mathbf {U} \cdot \nabla \mathbf {U} +f\mathbf {k} \times \mathbf {U} =-\nabla \left({\frac {p_{s}}{\rho _{0}}}+g(\eta -\eta _{EQ}-\eta _{SAL})\right)-{\frac {\text{BPG}}{H}}+{\frac {{\boldsymbol {\tau }}_{s}-{\boldsymbol {\tau }}_{b}}{\rho _{0}H}}-\gamma _{D}\mathbf {C} \mathbf {U} }` (168). |
| 171–250 | Governing Equations / 기호 정의·경압 압력경사 시작 — BPG는 수심 적분 경압 압력경사, γD는 내부파 항력 축척 매개변수, C는 내부파 항력 텐서(tensor)이다(173–177). 경압 압력경사식의 펼쳐진 기호 전반부를 포함하며 식은 다음 구간으로 이어진다(179–250). 원문: `- BPG is the depth-integrated baroclinic pressure gradient` (173); `- γD is a scaling parameter for internal wave drag` (175); `- C is the internal wave drag tensor` (177). |
| 251–274 | Governing Equations / 경압 압력경사 계속 — 적분항과 자유수면 밀도 항을 갖는 BPG식의 펼쳐진 기호 후반부와 완전한 LaTeX를 포함한다(251–273). 원문: `    {\displaystyle {\text{BPG}}={\frac {g}{\rho _{0}}}\left[\int _{-h}^{0}\nabla \left(\int _{0}^{z}(\rho -\rho _{0})\,dz'\right)dz+\eta \nabla [\eta (\rho _{s}-\rho _{0})]\right]}` (272). |
| 275–354 | Governing Equations / 소산 비율 시작 — 내부 조석 항력 텐서를 소산 비율(dissipation ratio) γD로 조절한다고 설명한다(275–289). 비율식의 펼쳐진 기호 전반부를 포함하며 식은 다음 구간으로 이어진다(291–354). 원문: `    {\displaystyle \gamma _{D}}` (287). |
| 355–368 | Governing Equations / 소산 비율 계속 — 조석 소산과 전체 소산의 비율 및 속도·텐서 표현의 완전한 LaTeX를 포함한다(355–365). 지연된 25시간 필터의 결과 평균 신호를 전체 속도에서 제거하여 조석 속도를 추정한다고 적는다(367). 내부파 항력 소산이 주로 조석 주파수에서 발생하도록 하는 목적을 설명한다(367). 원문: `    {\displaystyle \gamma _{D}={\frac {{\text{Diss}}_{\text{tidal}}}{{\text{Diss}}_{\text{total}}}}={\frac {\mathbf {U} _{\text{tidal}}\cdot \mathbf {C} \cdot \mathbf {U} _{\text{tidal}}}{\mathbf {U} \cdot \mathbf {C} \cdot \mathbf {U} }}}` (364); `Tidal velocity is estimated using a lagged 25-hour filter and removing the resultant mean signal from the total velocity. This ensures that dissipation from internal wave drag occurs predominantly at tidal frequencies, preserving tidal fidelity in the coupled model.` (367). |
| 369–377 | densityControl Namelist / 활성화 — namelist로 ADCIRC2D+를 활성화한다(371). `densityRunType`의 자료형·기본값·선택지를 옮긴다(373–376). 기본 `'none'`에서는 나머지 namelist 값이 중요하지 않다고 적는다(374). 원문: ``Activating ADCIRC2D+ is accomplished through the use of the `densityControl` namelist.This namelist has the following options and defaults (denoted by `(D)`)`` (371); ``- `densityRunType` (string)`` (373); `` `'none' (D)`: By default ADCIRC2D+ is not active. If `densityRunType='none'` the rest of the namelist values do not matter. `` (374); `` `'prognostic'` `` (375); `` `'diagnostic'` `` (376). |
| 378–394 | densityControl Namelist / 입력장·읽기 간격·강제 유형 — 사전 계산 압력경사·성층(stratification) 정보를 읽는 파일, 읽기 보폭(stride)의 정수 설정과 시간 예를 설명한다(378–380). 강제 유형의 문자열 선택지 9개와 내부 `IDEN` 변환 설명을 원문 그대로 옮긴다(382–393). 원문: ``- `densityFileName` (string): The name of the file from which pre-computed baroclinic pressure gradients and stratification information are read.`` (378); ``- `densityTimeIterator` (integer): The stride used when reading in `densityFileName`. For example, if `densityFileName` contains data at hourly timesteps and `densityTimeIterator=2` then data will be read in every two hours.`` (380); ``- `densityForcingType` (string)`` (382); `` `'SigmaT'` `` (383); `` `'Salinity'` `` (384); `` `'Temperature'` `` (385); `` `'SalinityTemperature'` `` (386); `` `'Baroclinicgradients'` `` (387); `` `'BaroclinicgradientsDispersion'` `` (388); `` `'Buoyancyfrequencies'` `` (389); `` `'BCForcingOnADCIRCGrid'` `` (390); `` `'BuoyancyFrequenciesOnGrid'` `` (391); `Within the ADCIRC code, the various settings of these namelist parameters is internally translated to an IDEN value which determines the baroclinic terms in the shallow water equations to include.` (393). |
| 395–399 | References — Pringle 등(2019)의 경압 결합 논문과 Blakely 등(2024)의 소산 비율 내부파 항력 논문 및 DOI를 제공한다(397–399). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 168·272: 수식의 `\mathbf{U}`, `f`, `\mathbf{k}`, `p_s`, `\rho_0`, `g`, `\eta`, `\eta_{EQ}`, `\eta_{SAL}`, `\boldsymbol{\tau}_s`, `\boldsymbol{\tau}_b`, `H`, `h`, `\rho`, `\rho_s`를 이 파일에서 별도로 정의하지 않는다. 173–177행은 BPG·γD·C만 정의한다.
- 371–392: 설명은 옵션과 기본값을 제시한다고 적지만 `(D)` 표시는 `densityRunType`의 `'none'`에만 있다. 나머지 옵션의 기본값은 이 파일에 없다.
