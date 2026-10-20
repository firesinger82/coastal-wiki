---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/metal/metal_integrate.cpp
lines: 14
sha256: a0c34666c88f28c7d8f4d1836b6fd34610179e147f48e003e608e90c762729ec
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# metal_integrate.cpp — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Metal 그래픽 처리 장치(graphics processing unit, GPU) 진입점(entry point)이라는 주석(1), metal_integrate.h와 fv1/metal_fv1_simulate.h 포함(2–3), 빈 줄(4·6). `metal_is_available()`은 `return lis::metal::fv1::Simulator::is_available();` (5)로 가용 여부를 반환한다. 이 파일 자체에는 조건부 컴파일 전처리문이 없다. |
| 7–14 | `run_metal_fv1`이 파일명·파일·상태·매개변수·해법(solver)·경계조건(boundary condition)·지점·배열·verbose를 받는다(7–9). `if (verbose)` (10)이면 Apple Silicon의 Metal GPU로 FV1 해법을 실행한다는 로그를 출력한다(11). 분기 밖에서 `lis::metal::fv1::simulate(filenames, files, states, pars, solver, boundCs,` (12); `stage, arrays, verbose);` (13)를 호출한다. 함수 종료(14). 조건부 컴파일 전처리문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 2–5·12–13: 이 파일에는 `__APPLE__` 조건부 컴파일문이 없으며 `Simulator::is_available()`과 `simulate()`를 직접 참조한다. 이 파일을 빌드에 포함하는 조건은 이 파일 내부에 없다.
