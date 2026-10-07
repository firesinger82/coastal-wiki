---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Hydrodynamics_Module/Shallow_Water.md
lines: 28
sha256: 2ddcfe43b93ca0768e4ef649eee191cd57122acfb8eee75c3b7328a84f573a3d
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Shallow_Water.md — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Shallow Water / 메타데이터 — 페이지 식별자 `243630129` (2), 제목·space·URL·버전·갱신 시각·상위 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–17 | Shallow Water / 습윤·건조 옵션 — 천수(shallow water)에서 수면고 변화에 따른 습윤·건조(wetting and drying) 모의 필요성을 설명한다(10). EFDC+ 10부터 옵션을 단순화하고 모든 옵션에서 셀 건너뛰기(cell skipping)를 쓴다고 적는다(12). 원문 목록은 `Do not allow cells to wet and dry (ISDRY = 0)` (14); `Use wet/dry with non-linear iterations (ISDRY = 11)` (15); `Use wet/dry with non-linear iterations and face masking (ISDRY = 99)` (16)이다. 빈 줄·목록 마크업을 포함한다. |
| 18–23 | Dry Depth / 차단·고립 셀 — `Dry Depth` (18)보다 셀 중심 수심이 낮으면 면 유량을 0으로 차단한다. `ISDRY = 11` (18)은 건조 셀의 네 면을 막는다. `ISDRY = 99` (18)는 젖은 이웃 셀이 있으면 공유 면을 열어 재습윤을 허용한다. 초기조건 원문은 `Minimum Height`, `Water Depth ICs (Legacy)`, `should be less than the *Dry Depth*.` (20)이다. 이 조건이 아니면 건조해야 하는 셀도 초기 수심 때문에 모두 젖은 상태가 된다(20). 고립 또는 높은 위치에 있고 수심이 매우 작은 젖은 셀은 `Number of Time Steps Before Water in Cell Goes Dry` (22)로 지정한 단계 동안 유입이 없으면 물을 제거한다. 기간의 원문은 `(number of dry steps) x (model time step)` (22)이다. `The dry step should be a positive number.` (22)이며 제거 체적은 질량 수지(mass balance)에 계속 추적한다. |
| 24–28 | SUB/SVB / Moving QSER Inflow — 비선형 옵션에서 `Only Reset SUB/SVB Flags When Needed` (24)를 선택할 수 있다. 기본은 `the SUB/SVB flags are reset to open/wet every iteration.` (24)이다. CALPUV/CONGRAD가 건조 셀을 판정한다(24). 필요할 때만 초기화하면 반복이 빨라지지만 결과가 약간 달라지며 `available for 2TL only.` (24)이다. EEMS12.0의 `Moving QSER Inflow` (26)는 경계 셀 수심이 건조 수심 아래여도 인접한 더 깊은 셀을 임시로 이용하여 유입을 유지한다. 비활성 조건은 `If the minimum depth in the text box is set to zero, then this option is disabled.` (26)이다. 로컬 `image2024-5-22_14-11-3.png`를 열었다(28). 화면 값은 `Dry Depth (m): 0.1`; `Number of Time Steps Before Water in Cell Goes Dry (Isolated Cells Only): 2000`; `Minimum Depth for All Withdrawals: 0.2`; `Minimum Depth Before Moving QSER Inflow to Adjacent Cell (m): 0`이다(28, 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12: `#Figure1`을 참조하지만 이 Markdown 파일에는 해당 앵커 선언이나 Figure 1 캡션이 없다.
- 28: `Minimum Depth for All Withdrawals`에는 단위가 표시되어 있지 않다.

