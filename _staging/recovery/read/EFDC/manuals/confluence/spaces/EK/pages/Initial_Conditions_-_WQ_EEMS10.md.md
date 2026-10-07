---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/Initial_Conditions_-_WQ_EEMS10.md
lines: 13
sha256: 0da8196c37d1725fb66a35a9bd4ccbee3afddb7dcf46db4f5ab7470f60d117bd
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Initial_Conditions_-_WQ_EEMS10.md — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 ID, EEMS10.2 제목, space, 원문 URL, 판본, 갱신 시각과 경로를 담은 frontmatter를 읽었다(1–9). |
| 10–13 | Initial Conditions — 수질(water quality, WQ) 매개변수마다 공간적으로 일정한 초기조건(initial conditions, IC) 또는 공간적으로 변하는 초기조건을 선택한다(10). 공간적으로 변하는 IC는 `Interpolated Classed Data`로 모델 셀에 자료를 보간해야 한다(10). 입력 데이터 형식 선택과 전체 영역 초기화 의무·동작 원문: `The WQ *Initial Conditions* tab is shown in Figure 1 provides access to the initial conditions settings for water quality. Here the user may select spatially constant or spatially varying initial conditions for each of the water quality parameters. To set *Spatially* *Varying IC's* for the water quality parameters, the user must interpolate data onto the model cells using the *Interpolated Classed Data* utility. If the EFDC model uses *Spatially Varying IC's*, then the user must specify which input data format to use, i.e. WQWCRST.INP or the ICIFN format. EFDC\_Explorer will generate the IC's in the specified format. The *Initialize IC's* button is to assign all parameters in the entire domain from the values specified as the *Spatially Constant* IC's.` (10). Figure 1의 `attachments/246644845/5-10-2019_10-54-33_AM.jpg`를 열었다(12). 그림은 초기농도와 `IC Flag` 표, `Options: Spatially Constant`, `Const IC's`, `Varying IC's`, `Initialize IC's`를 보여 준다(12 그림). 표의 보이는 행을 표시명과 표시값 그대로 옮긴다. `Cyanobacteria`: `0.000`; `Diatom Algae`: `0.000`; `Green Algae`: `0.000`; `Refractory Particulate...`: `0.100`; `Labile Particulate Org...`: `0.100`; `Dissolved Organic Ca...`: `0.100`; 마지막 `Refractory Particulate...`: `0.001`(12 그림). 보이는 `IC Flag` 체크박스는 모두 해제되어 있다(12 그림). 본문은 이 그림의 농도를 기본값으로 명시하지 않는다. 마지막 캡션을 포함한다(13). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12: 그림의 일부 매개변수 표시명이 열 너비 때문에 잘려 있다. 특히 두 행의 표시명이 모두 `Refractory Particulate...`로 보여서 완전한 이름을 구분할 수 없다.
