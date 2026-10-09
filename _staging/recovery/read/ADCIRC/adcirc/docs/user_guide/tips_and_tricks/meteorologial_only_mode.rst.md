---
file: models/ADCIRC/raw/source_code/adcirc/docs/user_guide/tips_and_tricks/meteorologial_only_mode.rst
lines: 52
sha256: 51167d8b41452f27fcd107863a42c5981401bb6032751497d5d7a3e7bbe55d26
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# meteorologial_only_mode.rst — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Meteorological-Only Mode — 기상 전용 모드(meteorological-only mode)는 유체역학 계산(hydrodynamic calculations)을 하지 않고 기상 자료 파일을 읽고 쓰는 방식이라고 적는다(4). 이 모드에서는 수위(water levels)와 속도(velocities)를 계산하지 않는다고 적는다(4). 모든 해양 상태 관련 출력을 끄고 파랑 결합(wave coupling)을 해제하여 이 모드를 얻는다고 설명한다(6). 원하는 기상 출력 시간 간격으로 DT를 설정하고 NSPOOLM 또는 NSPOOLGW를 설정하는 조건을 원문대로 옮긴다(6). 원문: ` ADCIRC can be run in "meteorological-only" mode, which is a quick and convenient way to read in and write out meteorological data files without performing hydrodynamic calculations. In this mode, only routines necessary for meteorological forcing are called - no water levels or velocities are computed. ` (4); ``` This mode is achieved by turning off all ocean state-related output and disabling wave coupling. Since only meteorological data is being output, you can set ``DT`` equal to the time interval at which you want meteorological data to be output, and then set the meteorological output intervals (``NSPOOLM`` and/or ``NSPOOLGW``) to ``1`` (i.e., output every time step). ``` (6). |
| 8–24 | Required Settings — 일반적인 2차원 ADCIRC 실행에서 fort.15에 설정할 항목을 제시한다(11). 관측점·전역 수위와 속도 출력, 핫스타트(hotstart) 출력, 관측점·전역 수위와 속도 조화 분석(harmonic analysis)을 끄는 아홉 입력 예시 행을 원문대로 옮긴다(15–23). 이 값은 요구 설정이며 기본값으로 설명하지 않는다. 원문: ` For typical 2D ADCIRC runs, set the following parameters in the fort.15 file: ` (11); ` .. code-block:: none ` (13); `    NOUTE = 0    ! No elevation station output ` (15); `    NOUTV = 0    ! No velocity station output   ` (16); `    NOUTGE = 0   ! No global elevation output ` (17); `    NOUTGV = 0   ! No global velocity output ` (18); `    NHSTAR = 0   ! No hotstart output ` (19); `    NHASE = 0    ! No harmonic analysis of elevations at stations ` (20); `    NHASV = 0    ! No harmonic analysis of velocities at stations ` (21); `    NHAGE = 0    ! No harmonic analysis of global elevations ` (22); `    NHAGV = 0    ! No harmonic analysis of global velocities ` (23). |
| 25–34 | Additional Settings / 수동 스칼라 — 수동 스칼라 수송(passive scalar transport)의 적용 조건과 추가 농도(concentration) 출력 설정을 제시한다(28–33). 관측점 농도와 전역 농도 출력을 끄는 예시를 원문대로 옮긴다(32–33). 원문: ``` For passive scalar transport (``IM = 10``), also set: ``` (28); ` .. code-block:: none ` (30); `    NOUTC = 0    ! No concentration station output ` (32); `    NOUTGC = 0   ! No global concentration output ` (33). |
| 35–45 | Additional Settings / 3차원 — 순압(barotropic) 또는 경압(baroclinic) 3차원 ADCIRC의 적용 조건을 제시한다(35). 관측점·전역 밀도(density), 속도, 수온(temperature) 출력을 끄는 여섯 입력 예시 행을 원문대로 옮긴다(39–44). 원문: ` For barotropic or baroclinic 3D ADCIRC, also set: ` (35); ` .. code-block:: none ` (37); `    I3DSD = 0    ! No 3D density station output ` (39); `    I3DSV = 0    ! No 3D velocity station output ` (40); `    I3DST = 0    ! No 3D temperature station output ` (41); `    I3DGD = 0    ! No 3D global density output ` (42); `    I3DGV = 0    ! No 3D global velocity output ` (43); `    I3DGT = 0    ! No 3D global temperature output ` (44). |
| 46–52 | Usage Notes — 전체 유체역학 모델 없이 기상 외력(meteorological forcing) 자료만 처리할 때 유용하다고 적는다(49). 원하는 출력 간격으로 DT를 설정하면 실행 속도를 높일 수 있다고 적는다(50). 기상 자료를 매 시간 단계(time step)에 출력하는 설정을 제시한다(51). 모든 유체역학 계산을 건너뛰므로 계산 시간이 크게 줄어든다고 설명한다(52). 적용 조건과 설정을 원문대로 옮긴다. 원문: ` 1. This mode is useful when you only need to process meteorological forcing data without running the full hydrodynamic model. ` (49); ``` 2. The simulation speed can be increased by setting ``DT`` equal to your desired meteorological output interval. ``` (50); ``` 3. Set ``NSPOOLM`` and/or ``NSPOOLGW`` to ``1`` to output meteorological data at every time step. ``` (51); ` 4. All hydrodynamic calculations are skipped, significantly reducing computational time.  ` (52). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 6·15–23·32–33·39–44행: 6행은 파랑 결합 해제를 요구한다. 뒤의 입력 예시에는 파랑 결합을 해제하는 매개변수가 제시되지 않는다.
