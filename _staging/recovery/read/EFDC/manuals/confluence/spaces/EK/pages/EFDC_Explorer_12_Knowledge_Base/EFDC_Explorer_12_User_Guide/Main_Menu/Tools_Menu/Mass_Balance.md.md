---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Main_Menu/Tools_Menu/Mass_Balance.md
lines: 20
sha256: f60e2d526d242fb053fc916bced59f560bf9dd95f3d0f3c639fdf28f182a7aeb
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Mass_Balance.md — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각, 문서 계층 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–13 | Mass Balance — 질량 수지(mass balance) 도구가 전체 모델의 물 부피와 경계별 질량 플럭스(mass flux)를 평가한다(10). 출력 스냅숏(output snapshot)의 간격이 작을수록 보고 결과가 더 정확하다고 설명한다(10). 보존성 성분(conservative constituent)과 비보존성 성분(non-conservative constituent)의 정확도, 제외하는 과정·경계와 주의 대상은 `The *Mass Balance* tool allow*s* the user to evaluate the total model’s water volume as well as determine the mass fluxes through each boundary. Mass balance is calculated based on model output snapshots written to the EE\_BC.OUT file. The smaller the output snapshot interval the more accurate the reported results will be. An example of mass balance for a model of the Caloosahatchee Estuary is shown in [Mass Balance#Figure 1](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/2122153985#MassBalance-Figure1). It should be noted that conservative constituents, such as water, salinity, and dye will be reported accurately. However, for non-conservative constituents, the tool only provides approximate loadings. This is because the kinetic, atmospheric, and bottom processes are not accounted for. Surface and bed boundaries are ignored in the calculations, so values for temperature, sediment, and water quality should be regarded with caution. ` (10)이다. `3.jpg`를 열었다(12). 모델 결과의 이용 가능한 시간을 표시하고 계산 기간과 성분을 선택하는 대화상자이다(12). 그림의 설정값은 `Begin Time (days): 2922.0000`, `End Time (days): 2932.0000`, `Constituent: Water`이며 `Show Time Series Plot`은 선택되지 않았다(12, 그림). |
| 14–17 | 경계 그룹(boundary group)과 전체 영역의 통계 보고 — `Mass balance through each boundary group and the whole domain is calculated and reported as statistics as shown in [Mass Balance#Figure 2](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/2122153985#MassBalance-Figure2) below.` (14)이다. `4.jpg`를 열었다(16). `Water Mass Balance` 보고서의 계산 기간은 `2922.000 days to 2932.000 days`이다(16, 그림). 부피의 표시 단위는 `10⁶m³`이다(16, 그림). 행별 값은 `Model Initial Volume: 1 536.8835`, `Model Final Volume: 1 350.7211`, `Model Volume Change: -186.1624`, `Flow Boundaries: 153.1278`, `Structure: 0.0000`, `South Open Boundaries: 34.3963`, `East Open Boundaries: 0.0000`, `West Open Boundaries: -321.0219`, `North Open Boundaries: 3.2210`, `Groundwater: 0.0000`, `Net Balance: -55.8856`이다(16, 그림). 마지막 행의 추가 표시는 `Loss (-3.6363% of Initial Mass)`이다(16, 그림). |
| 18–20 | 경계 그룹별 시계열(time series) — 선택 조건은 `View the mass balance through each boundary group time series by checking the *Show Time Series Plot*checkbox in [Mass Balance#Figure 1](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/2122153985#MassBalance-Figure1). This will produce a plot similar to that shown in [Mass Balance#Figure 3](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/2122153985#MassBalance-Figure3) below.` (18)이다. `5.jpg`를 열었다(20). 가로축 `Time (days)`의 눈금은 `2922`부터 `2932`까지 1일 간격이다(20, 그림). 세로축 `Salinity (kg/s)`의 눈금은 `-30000`, `-20000`, `-10000`, `0`, `10000`, `20000`, `30000`이다(20, 그림). 범례는 빨강 `Flow Boundaries`, 파랑 `South Open Boundary`, 초록 `East Open Boundary`, 자홍 `West Open Boundary`, 청록 `North Open Boundary`이다(20, 그림). 서쪽·남쪽 경계 곡선은 크게 진동하며 나머지 곡선은 0 부근에 표시된다(20, 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·14·18행의 `#MassBalance-Figure1`, `#MassBalance-Figure2`, `#MassBalance-Figure3` 참조에 대응하는 앵커 정의와 Figure 번호 캡션이 이 Markdown에 없다.
- 12행 그림의 `Constituent`와 16행 보고서의 제목은 `Water`이다. 20행 그래프의 세로축은 `Salinity (kg/s)`이다. 그림들 사이에서 성분이 바뀌는 단계는 본문에 설명되어 있지 않다.

