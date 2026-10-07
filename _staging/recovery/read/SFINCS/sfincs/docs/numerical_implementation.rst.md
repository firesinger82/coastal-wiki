---
file: models/SFINCS/raw/source_code/sfincs/docs/numerical_implementation.rst
lines: 95
sha256: 07350e4760615f35814bb4403eb600bc3326f1490e833ee5122986d292e44ed5
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# numerical_implementation.rst — 판독 구간 기록

구간은 1행부터 95행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Numerical implementation / Introduction — 문서 제목·Introduction 제목·구분선·빈 줄을 포함한다(1–6·8–9). 소개 본문은 Leijnse (2018)에 기반한다는 한 줄이다(7). 원문: `Based on Leijnse (2018)` (7). |
| 10–16 | Flow-related processes / Shallow water equations — 상위 절과 천수방정식 소절 제목·구분선·빈 줄만 있다(10–16). 천수방정식의 수식이나 설명 본문은 없다. |
| 17–20 | Numerical grid — 격자 소절 제목·구분선·빈 줄만 있다(17–20). 격자 배치 설명이나 그림 지시문은 없다. |
| 21–25 | Momentum equations — 운동량 방정식 소절 제목·구분선·빈 줄만 있다(21–25). 수식이나 해법 설명은 없다. |
| 26–30 | Advection — 이류 소절 제목·구분선·빈 줄만 있다(26–30). 이류항 수식이나 이산화 설명은 없다. |
| 31–35 | Continuity equation — 연속방정식 소절 제목·구분선·빈 줄만 있다(31–35). 수식이나 갱신 절차 설명은 없다. |
| 36–39 | Stability conditions — 안정성 조건 소절 제목·구분선·빈 줄만 있다(36–39). 안정성 조건식이나 시간 간격 제한값은 없다. |
| 40–49 | Wave-related processes / Swash zone modelling approach — 파랑 관련 상위 절과 swash zone 모델링 소절 제목·구분선·빈 줄만 있다(40–49). 모델링 접근법 본문은 없다. |
| 50–54 | Weakly reflective generating-absorbing boundary condition — 경계조건 소절 제목·구분선·빈 줄만 있다(50–54). 생성·흡수 경계의 식이나 적용 옵션 설명은 없다. |
| 55–60 | Wave generation — 파랑 생성 소절 제목·구분선과 작업 중 표기, 빈 줄을 포함한다(55–60). 작업 중 표기는 원문 그대로 옮긴다(57). 생성 수식이나 입력 형식은 없다. 원문: `(Work in progress)` (57). |
| 61–65 | Wave-induced setup — 파랑에 의한 setup 소절 제목·구분선과 작업 중 표기, 빈 줄을 포함한다(61–65). 작업 중 표기는 원문 그대로 옮긴다(63). setup 계산식은 없다. 원문: `(Work in progress)` (63). |
| 66–70 | Other processes — 기타 과정 상위 절 제목·구분선·빈 줄만 있다(66–70). 이 구간에 설명 본문은 없다. |
| 71–75 | Infiltration — 침투 소절 제목·구분선·빈 줄만 있다(71–75). 침투 계산식·매개변수·옵션 설명은 없다. |
| 76–79 | Precipitation — 강수 소절 제목·구분선·빈 줄만 있다(76–79). 강수 입력·계산 설명은 없다. |
| 80–83 | Discharge points — 유량 지점 소절 제목·구분선·빈 줄만 있다(80–83). 유량 지점의 입력 형식·계산 설명은 없다. |
| 84–87 | Wind forcing — 바람 외력 소절 제목·구분선·빈 줄만 있다(84–87). 외력 수식·매개변수·단위 설명은 없다. |
| 88–92 | Model limitations — 모델 한계 절 제목·구분선·빈 줄만 있다(88–92). 구체적인 모델 한계는 서술되어 있지 않다. |
| 93–95 | Computational efficiency — 계산 효율 절 제목·구분선과 마지막 빈 줄만 있다(93–95). 계산 시간·성능 수치나 비교 본문은 없다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 13–54·66–95행: 각 수치 과정·모델 한계·계산 효율 절에 상세 설명 본문이 없다. 55–65행의 Wave generation과 Wave-induced setup에는 각각 57·63행의 (Work in progress)만 본문으로 적혀 있다.
- 1–2·10–11·13–14·17–18·21–22·26–27·31–32·36–37·40–41·44–45·50–51·55–56·61–62·66–67·71–72·76–77·80–81·84–85·88–89·93–94행: 제목 밑줄은 각 제목의 끝 공백을 제외한 문자 수보다 짧다.
