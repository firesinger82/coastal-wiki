---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Hydrodynamics_Module/Numerical_Options.md
lines: 20
sha256: 83c2596101c29933e5c8313e011ddb6bd23f9d67d258dfac9abcae5dc4b27e27
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Numerical_Options.md — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Numerical Options / 메타데이터 — 페이지 식별자 `244088848` (2), 제목·space·URL·버전·갱신 시각·상위 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–12 | Numerical Solution Option / 시간 단계 — 주요 방식 원문은 `2-Time Level`, `3-Time Level` (10)이다. 부력 강제력(buoyancy forcing)의 표준 선택은 `Buoyancy Forcing`, `Internal Pressure Gradient` (10)이다. 다른 옵션은 `EFDC.INP` (10)에서 설정할 수 있지만 옵션을 이해하고 선택한 하위 모형이 맞는지 확인해야 한다고 적는다. 2TL은 영역 분할(domain decomposition)을 허용한다(12). `EFDC\_GVC`와 `GVC layering` (12)을 쓰면 가능한 방식은 3TL뿐이다. 본문은 다가오는 EEMS12에서 3TL 영역 분할이 가능할 것이라고 적는다(12). 3TL의 자기 보정 사다리꼴 단계(self-correcting trapezoidal step)로 더 큰 `time step (delta T)` (12)를 사용할 수 있다고 적는다. |
| 13–20 | Momentum Options / 권장·제한 — 3TL 선택 시 `Momentum Options`와 `(ISCDMA)` (14)를 반드시 지정한다. 권장 방식은 `Upwind Difference` (14)이다. `Central Difference`, `Experimental Upwind Difference`, `(ISCDMA>2)` (14)는 실험적이고 충분히 시험하지 않았으며 현재 권하지 않는다고 적는다. 대부분 적용에는 영역 분할을 지원하는 2TL을 권한다(16). 로컬 `Numerical.jpg`를 열었다(18). 화면은 3-time Level, Upwind Difference와 `Trapezoidal Correction Timing: 4`를 보여 준다(18, 그림). 빈 줄·Figure 1 캡션을 포함한다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12: EEMS12의 3TL 영역 분할 지원을 미래형 `With the coming EEMS12`로 적는다. 이 판독에서는 이후 구현 상태를 확인하지 않았다.

