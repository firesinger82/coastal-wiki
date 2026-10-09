---
file: models/ADCIRC/raw/source_code/adcirc/docs/user_guide/tips_and_tricks/ramping_met_forcing_at_hotstart.rst
lines: 44
sha256: 79f17bea012c0689ecbf305d8b781f99319c035363d7d7bc6f79d31d7cb9d74d
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# ramping_met_forcing_at_hotstart.rst — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | Ramping Meteorological Forcing at Hotstart — 기상 외력(meteorological forcing)을 갑자기 도입하여 계에 충격을 주지 않도록 점진 적용(ramping)하는 것이 일반적으로 좋다고 적는다(4). 콜드스타트(cold-start) 기준 ramp 시작을 정하는 DRAMP 같은 매개변수와 별도로, 핫스타트(hotstart) 시각의 기상 자료 점진 적용을 위한 특수 매개변수가 있다고 설명한다(4). 원문의 일반적 권고와 적용 시점을 유지한다. 원문: ``` When running ADCIRC with meteorological forcing, it's generally best to ramp in forcing terms to avoid shocking the system. While parameters like ``DRAMP`` define the start of ramp time from cold-start, there is a special parameter to facilitate ramping of meteorological data at hotstart time. ``` (4). |
| 6–13 | Configuration — 핫스타트에서 기상 외력을 점진 적용하려면 fort.15의 NRAMP를 설정하고 DRAMP 줄에 DRAMPUnMete를 공급해야 한다고 적는다(9–12). DRAMPUnMete는 기상 외력의 점진 적용을 시작할 일수를 지정한다고 설명한다(12). 옵션과 단위를 원문대로 옮긴다. 원문: ` To enable meteorological ramping at hotstart, you need to: ` (9); ``` 1. Set ``NRAMP = 8`` in the fort.15 file ``` (11); ``` 2. Supply ``DRAMPUnMete`` on the ``DRAMP`` line, which specifies the number of days at which to start meteorological ramping ``` (12). |
| 14–22 | Example — 조석만으로 15일 실행하고 핫스타트 파일을 출력한 뒤, 실행 15.0일에 시작하는 기상 외력을 0.5일 동안 점진 적용하는 예시를 제시한다(17). fort.15의 DRAMP 입력 예시 전체와 주석의 매개변수 순서를 원문대로 옮긴다(19–21). 예시 값은 기본값으로 설명하지 않는다. 원문: ``` Let's say you run a 15-day tide-only simulation and output a hotstart file. To apply a 0.5-day ramp to the meteorological forcing starting at run day 15.0 (the hotstart simulation's start time), your ``DRAMP`` line in fort.15 would look like: ``` (17); ` .. code-block:: none ` (19); `    5 0 0 0 0 0 0.5 0 15 ! DRAMP, DRAMPExtFlux, FluxSettlingTime, DRAMPIntFlux, DRAMPElev, DRAMPTip, DRAMPMete, DRAMPWRad, DRAMPUnMete ` (21). |
| 23–37 | Parameter Description — DRAMP 입력 줄의 아홉 매개변수를 순서대로 설명한다(26–36). 일반 ramp, 외부 플럭스(external flux), 플럭스 정착 시간(flux settling time), 내부 플럭스(internal flux), 수위(elevation), 조석 퍼텐셜(tidal potential), 기상 외력, 파랑 복사 응력(wave radiation stress), 기상 외력 ramp 시작 일수를 구분한다(28–36). DRAMPMete의 지속 시간과 DRAMPUnMete의 시작 시점을 바꾸어 쓰지 않는다. 이름·의미·예제 단위를 원문대로 옮긴다. 원문: ``` - ``DRAMP``: General ramping parameter ``` (28); ``` - ``DRAMPExtFlux``: External flux ramping ``` (29); ``` - ``FluxSettlingTime``: Flux settling time ``` (30); ``` - ``DRAMPIntFlux``: Internal flux ramping ``` (31); ``` - ``DRAMPElev``: Elevation ramping ``` (32); ``` - ``DRAMPTip``: Tidal potential ramping ``` (33); ``` - ``DRAMPMete``: Meteorological forcing ramping (0.5 days in this example) ``` (34); ``` - ``DRAMPWRad``: Wave radiation stress ramping ``` (35); ``` - ``DRAMPUnMete``: Days at which to start meteorological ramping (15 days in this example) ``` (36). |
| 38–44 | Usage Notes — 핫스타트에서 기상 외력을 초기화할 때 유용하다고 적는다(41). 갑작스러운 외력 도입으로 생길 수 있는 수치 불안정(numerical instabilities)을 줄이는 데 도움이 된다고 적는다(42). 지속 시간과 시작 시점은 모의 필요에 따라 선택해야 한다고 적는다(43). DRAMPUnMete가 핫스타트 모의의 시작 시각과 일치해야 한다고 요구한다(44). 권고와 일치 조건을 원문대로 옮긴다. 원문: ` 1. This feature is particularly useful when initializing meteorological forcing at hotstart time ` (41); ` 2. The ramping helps prevent numerical instabilities that could arise from sudden introduction of meteorological forcing ` (42); ``` 3. The ramp duration (``DRAMPMete``) and start time (``DRAMPUnMete``) should be chosen based on your specific simulation needs ``` (43); ``` 4. Make sure the ``DRAMPUnMete`` value matches your hotstart simulation's start time  ``` (44). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
