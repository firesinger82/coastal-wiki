---
file: models/ADCIRC/raw/source_code/adcirc/docs/user_guide/examples/global_storm_tide_katrina.rst
lines: 61
sha256: 9dae5ee1bf3a2de12f277e6d69bb7f2fb8192a29c49639f458ad4e15965367bc
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# global_storm_tide_katrina.rst — 판독 구간 기록

구간은 1행부터 61행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | Global Storm Tide - Hurricane Katrina — 메타 지시문과 제목을 포함한다(1–6). ADCIRC v55 이상의 구면 지구에서 2005년 8월 Katrina 당시 천문·대기 강제력에 따른 폭풍 조위(storm tide)를 시험한다고 적는다(8–10). 전역 수위·유속·기상과 한 달 모의의 직렬 실행 약 5분을 설명한다(11–14). 원문: `This example tests ADCIRC version 55 (and beyond). It tests the simulation of` (8); `the storm tides on the spherical Earth under astronomical and atmospheric` (9); `forcing during August 2005 when Hurricane Katrina impacted the Gulf of Mexico.` (10); `The results of interest are the global elevations, velocities and meteorology.` (11); `The test finishes in about 5 minutes in serial ADCIRC for a full month of` (12); ``simulation. Find the test at the `GitHub test`` (13); ``suite <https://github.com/adcirc/adcirc-cg-testsuite/tree/v55/adcirc/adcirc_global-tide%2Bsurge-2d>`__.`` (14). |
| 16–24 | Mesh — 구면 지구의 성긴 격자에 대한 최소 해상도와 정점·삼각 요소 수를 제시한다(19–21). 다음 절의 앵커를 포함한다(23). 원문: `The mesh is a coarse representation of the spherical Earth with minimum` (19); `resolution of approximately 50 km, comprised of 27,330 vertices and 50,859` (20); `triangular elements.` (21). |
| 25–61 | Options/Features Tested — Mercator 좌표 회전, 완전 음해법(fully implicit scheme), 조석 입력과 NWS=-14 기상 입력을 제시한다(28–39). GRIB2 6시간 입력과 Katrina 상륙 지역 OWI ASCII 3시간 입력의 시간 간격 및 계수를 설명한다(36–46). 출력 설정과 공간 가변 내부조석 마찰(internal tide friction)·이차 저면 마찰(quadratic bottom friction) 속성을 제시한다(47–60). 원문: ``-  :ref:`ICS <ICS>` = -22: Uses the Mercator projection with a coordinate`` (28); `   rotation to remove the pole singularity (need to provide a` (29); ``   :ref:`fort.rotm <fortrotm>`).`` (30); ``-  :ref:`IM <IM>` = 513113: Uses the fully implicit scheme for the gravity wave`` (31); `   term (computational time step is 12 minutes).` (32); ``-  :ref:`NTIP <NTIP>` = 2: Equilibrium tide + self-attraction and loading tide`` (33); ``   (read from a :ref:`fort.24 file <fort24>` forcing for 10 tidal`` (34); `   constituents.` (35); ``-  :ref:`NWS <NWS>` = -14: Reads from GRIB2 files that specify the global`` (36); `   atmospheric forcing (6-hourly CFS reanalysis data) in addition to OWI ASCII` (37); `   files that specify the 3-hourly atmospheric forcing in the Hurricane Katrina` (38); `   landfall region.` (39); ``-  :ref:`WTIMINC <WTIMINC>` = 21600, 10800: First value gives the temporal`` (40); `   interval of the GRIB2 met data (6 hours), second value gives the temporal` (41); `   interval of the OWI met data (3 hours) in seconds.` (42); ``-  :ref:`A00 <A00>`, :ref:`B00 <B00>`, :ref:`C00 <C00>` = 0.5, 0.5, 0:`` (43); `   Ensures that the fully implicit scheme is stable with a large time step.` (44); ``-  :ref:`ESLM <ESLM>` = -0.2: Enables the Smagorinsky turbulence closure with a`` (45); `   coefficient of 0.2.` (46); ``-  :ref:`NOUTGE <NOUTGE>` = 5: Outputs the global elevations into a netCDF4`` (47); ``   :ref:`fort.63 file <fort63>`.`` (48); ``-  :ref:`NOUTGV <NOUTGV>` = 5: Outputs the global velocities into a netCDF4`` (49); ``   :ref:`fort.64 file <fort64>`.`` (50); ``-  :ref:`NOUTGW <NOUTGW>` = 5: Outputs the global meteorology into a netCDF4`` (51); ``   :ref:`fort.73 file <fort73>` (pressure) and a netCDF4 :ref:`fort.74`` (52); ``   file <fort74>` (velocity).`` (53); ``-  :ref:`internal_tide_friction <internal_tide_friction>`:`` (54); ``   Spatially varying linear wave drag :ref:`fort.13 file <fort13>` attribute`` (55); `   accounting for energy conversion due to internal tide generation in the deep` (56); `   ocean.` (57); ``-  :ref:`quadratic_friction_coefficient_at_sea_floor <quadratic_friction_coefficient_at_sea_floor>`:`` (58); ``    Spatially varying quadratic bottom friction :ref:`fort.13 file <fort13>` `` (59); `   attribute.` (60). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 33–35: `NTIP` 설명은 `(read from a`로 괄호를 열지만 `constituents.`까지 닫는 괄호가 없다.
