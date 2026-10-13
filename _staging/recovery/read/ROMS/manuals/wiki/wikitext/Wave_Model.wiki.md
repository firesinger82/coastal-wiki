---
file: models/ROMS/raw/manuals/wiki/wikitext/Wave_Model.wiki
lines: 18
sha256: 83fd19b043df1f7860fd453c46acec8962f8cd5d260f9b977d94d5a60f9bc31e
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# Wave_Model.wiki — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | SWAN / 파랑 정보 — 문서는 파랑 에너지, 전파 방향과 파장을 사용하는 운동량 방정식을 소개한다(1–3). 저면 경계 및 난류 모듈도 파 주기, 저면 궤도 속도(bottom orbital velocity)와 파랑 에너지 소산률을 요구할 수 있다고 적는다(3). 분석 함수, NetCDF 강제력 파일(forcing file) 또는 파랑 모델 결합으로 정보를 제공할 수 있다고 적는다(3). |
| 5–16 | SWAN / 파랑 작용 수송식 — 파랑 평균 모델(wave-averaged model)은 에너지 밀도를 상대 주파수(relative frequency)로 나눈 파랑 작용 밀도(wave action density)의 수송식을 푼다고 적는다(5). 수송식의 LaTeX를 행별로 옮긴다(7–15). 원문: LaTeX: `N` (5); `\frac{{\partial N}}` (8); `{{\partial t}} + \frac{{\partial \,c_x N}}` (9); `{{\partial x}} + \frac{{\partial \,c_y N}}` (10); `{{\partial y}} + \frac{{\partial \,c_\sigma  N}}` (11); `{{\partial \sigma }} + \frac{{\partial \,c_\theta  N}}` (12); `{{\partial \theta }} = \frac{{S_w }}` (13); `{\sigma }` (14). |
| 17–18 | SWAN / 과정과 결합 조건 — 문서는 위치·상대 주파수·방향 기호를 정의한다(17). 천수화(shoaling), 굴절(refraction), 발생·쇄파·저면 소산·비선형 파랑 상호작용 및 회절(diffraction)·부분 투과·반사를 설명한다(17). 일방향 결합(one-way coupling) 또는 쌍방향 결합(two-way coupling)을 설명한다(17). 결합 시 SWAN은 ROMS와 같은 격자에서 계산해야 한다고 적는다(18). 각 모델에 서로 다른 프로세서 수를 할당할 수 있으며 Model Coupling Toolkit을 사용한다고 적는다(18). 원문: LaTeX: `c_x` (17); `c_y` (17); `x` (17); `y` (17); `\sigma` (17); `\theta` (17); `c_x` (17); `c_y` (17); `S_w` (17); `When ROMS and SWAN are run in coupled mode, the current limitation is that SWAN needs to be computed on the same grid as ROMS. Each model can be allocated an independent number of different processors. The models are coupled using the Model Coupling Toolkit.` (18). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 8–14·17: 수송식의 c_sigma와 c_theta는 이 파일에서 정의하지 않는다. 17행은 c_x와 c_y를 전파 속도로 정의한다.
