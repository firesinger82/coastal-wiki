---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/flux.cpp
lines: 54
sha256: 8ba3b770c6db1e3a65d23499562abcce95514eb930bf383cc57b10809221830f
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# flux.cpp — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | 헤더를 포함한다(1). x방향 물리 플럭스(physical flux) 함수는 HU·HV 순서로 공통 함수를 호출한다(14). y방향 함수는 입력 HU·HV와 출력 HU_flux·HV_flux의 순서를 함께 뒤집는다(28). 조건부 전처리 분기는 없다. 원문: `physical_flux(Solverptr, H, HU, HV, H_flux, HU_flux, HV_flux);` (14); `physical_flux(Solverptr, H, HV, HU, H_flux, HV_flux, HU_flux);` (28). |
| 31–54 | 공통 `physical_flux`는 수심이 DepthThresh 이하이면 세 플럭스를 0으로 설정한다. else에서는 질량·법선 운동량·접선 운동량 플럭스를 계산한다. 원문: `if (H <= Solverptr->DepthThresh)` (42); `{` (43); `H_flux = C(0.0);` (44); `HU_flux = C(0.0);` (45); `HV_flux = C(0.0);` (46); `}` (47); `else` (48); `{` (49); `H_flux = HU;` (50); `HU_flux = HU*HU/H + C(0.5)*Solverptr->g*H*H;` (51); `HV_flux = HU*HV/H;` (52); `}` (53). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
