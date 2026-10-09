---
file: models/ADCIRC/raw/source_code/adcirc/docs/user_guide/examples/global_astronomical_m2_tide.rst
lines: 48
sha256: db4cd18af57359ae4e58ba2f10a09cf8d7069d11c3726fcf4349ad48d30401bb
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# global_astronomical_m2_tide.rst — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | Global Astronomical M2 Tide — 메타 지시문과 제목을 포함한다(1–6). ADCIRC v55 이상의 구면 지구에서 평형조석과 자기인력 및 하중조석(self-attraction and loading tide)을 포함한 M2 분조(tidal constituent)를 시험한다고 적는다(8–10). 최소제곱 조화분석(least-squares harmonic analysis)의 수위·유속 진폭과 위상을 관심 결과로 적는다(11–12). 한 달 모의의 직렬 실행 시간이 약 5분이라고 적는다(13). 원문: `This example tests ADCIRC version 55 (and beyond). It tests the simulation of` (8); `the astronomical M2 tidal constituent on the spherical Earth under equilibrium` (9); `tidal forcing with the inclusion of the self-attraction and loading tide. The` (10); `results of interest are the M2 tidal constituent amplitudes and phases of` (11); `elevations and velocities from the least-squares harmonic analysis. The test` (12); `finishes in about 5 minutes in serial ADCIRC for a full month of simulation.` (13); ``Find the test at the `GitHub test`` (14); ``suite <https://github.com/adcirc/adcirc-cg-testsuite/tree/v55/adcirc/adcirc_global-tide-2d>`__.`` (15). |
| 17–23 | Mesh — 구면 지구를 나타내는 성긴 격자의 최소 해상도와 정점·삼각 요소 수를 제시한다(20–22). 원문: `The mesh is a coarse representation of the spherical Earth with minimum` (20); `resolution of approximately 50 km, comprised of 27,330 vertices and 50,859` (21); `triangular elements.` (22). |
| 24–48 | Options/Features Tested — 극점 특이성을 제거하는 Mercator 투영(projection)의 좌표 회전과 fort.rotm 조건을 제시한다(27–29). 완전 음해법(fully implicit scheme)의 시간 간격, 조석 입력, 계수, Smagorinsky 난류 폐쇄(turbulence closure), 조화분석 출력 및 공간 가변 마찰 속성을 설명한다(30–48). 각 매개변수와 적용 조건을 원문대로 옮긴다. 원문: ``-  :ref:`ICS <ICS>` = -22: Uses the Mercator projection with a coordinate`` (27); `   rotation to remove the pole singularity (need to provide a` (28); ``   :ref:`fort.rotm <fortrotm>`).`` (29); ``-  :ref:`IM <IM>` = 513113: Uses the fully implicit scheme for the gravity wave`` (30); `   term (computational time step is 12 minutes).` (31); ``-  :ref:`NTIP <NTIP>` = 2: equilibrium tide + self-attraction and loading tide`` (32); ``   forcing (read from a :ref:`fort.24 file <fort24>`).`` (33); ``-  :ref:`A00 <A00>`, :ref:`B00 <B00>`, :ref:`C00 <C00>` = 0.5, 0.5, 0:`` (34); `   Ensures that the fully implicit scheme is stable with a large time step.` (35); ``-  :ref:`ESLM <ESLM>` = -0.2: enables the Smagorinsky turbulence closure with a`` (36); `   coefficient of 0.2.` (37); ``-  :ref:`NHAGE <NHAGE>` = 5: outputs the harmonic constituent elevations into a`` (38); ``   netCDF4 :ref:`fort.53 file <fort53>`.`` (39); ``-  :ref:`NHAGV <NHAGV>` = 5: outputs the harmonic constituent velocities into a`` (40); ``   netCDF4 :ref:`fort.54 file <fort54>`.`` (41); ``-  :ref:`internal_tide_friction <internal_tide_friction>`:`` (42); ``   spatially varying linear wave drag :ref:`fort.13 file <fort13>` attribute`` (43); `   accounting for energy conversion due to internal tide generation in the deep` (44); `   ocean.` (45); ``-  :ref:`quadratic_friction_coefficient <quadratic_friction_coefficient_at_sea_floor>`:`` (46); ``    spatially varying quadratic bottom friction :ref:`fort.13 file <fort13>` `` (47); `   attribute.` (48). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
