---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Water_Quality_EEMS12/Initial_Conditions_-_WQ_EEMS12.md
lines: 18
sha256: c89dba23a09269e806eea507e528b0fd58f3b5c4e9ed2f6b096a0abf5155628a
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Initial_Conditions_-_WQ_EEMS12.md — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Initial Conditions - WQ (EEMS12) — 페이지 메타데이터를 담은 frontmatter이다(1–9). |
| 10–11 | 수질 초기조건(initial condition) — 공간 일정·공간 변화 선택, 보간(interpolation) 의무, `WQWCRST.INP` 또는 `ICIFN` 입력 형식 선택, 전체 영역 초기화 조건은 `The WQ *Initial Conditions* option provides access to the initial conditions settings for water quality. Here, the user may select spatially constant ([Initial Conditions - WQ (EEMS12)#Figure 1](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/2220785775#InitialConditions-WQ(EEMS12)-Figure1)) or spatially varying initial conditions ([Initial Conditions - WQ (EEMS12)#Figure 2](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/2220785775#InitialConditions-WQ(EEMS12)-Figure2)) for each of the water quality parameters. To set *Spatially* *Varying IC's* for the water quality parameters, the user must interpolate data onto the model cells using the *Interpolated Classed Data* utility. If the EFDC model uses *Spatially Varying IC's*, then the user must specify which input data format to use, i.e. WQWCRST.INP or the ICIFN format. EE will generate the IC's in the specified format. The *Initialize IC's* button is used to assign all parameters in the entire domain from the values specified as the *Spatially Constant* IC's.` (10). |
| 12–15 | Figure 1 / Spatially Constant — 12행 로컬 그림 `attachments/2220785775/Constant.png`을 열었다. `ID`/`Initial Const.` 표에서 완전히 보이는 1–8번 항목은 `Refractory Particulate Organic Carbon (mg/L)` = `0.1`; `Labile Particulate Organic Carbon (mg /L)` = `0.1`; `Dissolved Organic Carbon (mg/L)` = `0.1`; `Refractory Particulate Organic Phosphorus (mg/L)` = `0.001`; `Labile Particulate Organic Phosphorus (mg/L)` = `0.003`; `Dissolved Organic Phosphorus (mg/L)` = `0.004`; `Total Phosphate (mg/L)` = `0.016`; `Refractory Particulate Organic Nitrogen (mg/L)` = `0.014`이다(12행 그림). 9번 행은 하단에서 잘려 이름·단위의 전체 모양을 확인하지 못했다. 그림은 공간 일정 초기조건에서 공간 변화용 버튼이 비활성임을 보여 준다(12–14). |
| 16–18 | Figure 2 / Spatially Varying — 16행 로컬 그림 `attachments/2220785775/From_Restart.png`을 열었다. `Options:` = `Spatially Varying IC's (WQWCRST.INP)`를 선택하고 Initialize IC's·Assign IC's·Import WQWCRST.INP가 활성인 화면이다(16행 그림). `Average Value` 표에서 완전히 보이는 1–8번 항목은 `Refractory Particulate Organic Carbon (mg/L)` = `0.000`; `Labile Particulate Organic Carbon (mg /L)` = `0.000`; `Dissolved Organic Carbon (mg/L)` = `0.000`; `Refractory Particulate Organic Phosphorus (mg/L)` = `0.000`; `Labile Particulate Organic Phosphorus (mg/L)` = `0.000`; `Dissolved Organic Phosphorus (mg/L)` = `0.000`; `Total Phosphate (mg/L)` = `0.000`; `Refractory Particulate Organic Nitrogen (mg/L)` = `0.000`이다(16행 그림). 9번 이후 행은 일부 또는 전부 화면 밖에 있다(16–18). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행: Figure 1·2 링크의 조각 식별자에 대응하는 명시적 앵커 정의가 이 Markdown 파일에 없다.

