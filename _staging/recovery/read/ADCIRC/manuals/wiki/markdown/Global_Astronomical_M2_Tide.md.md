---
file: models/ADCIRC/raw/manuals/wiki/markdown/Global_Astronomical_M2_Tide.md
lines: 29
sha256: c6112b4ab51f0d98c193b4d7bcba6eecee15e690113836dee5c24fb778b9e9fc
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Global_Astronomical_M2_Tide.md — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Global Astronomical M2 Tide — 제목과 판본 표기 `_revid=1036_`(1–3)을 포함한다. ADCIRC 55 이후 판본에서 구면 지구(spherical Earth)의 M2 분조(tidal constituent)를 평형 조석(equilibrium tide)과 자기 인력 및 하중 조석(self-attraction and loading tide) 강제력으로 시험한다고 적는다(5). 최소제곱 조화분해(least-squares harmonic analysis)로 구한 수위·유속의 M2 진폭(amplitude)과 위상(phase)을 관심 결과로 제시한다(5). 한 달 모의를 직렬(serial) ADCIRC에서 약 5분에 마친다는 문서 설명과 시험 저장소 링크가 있다(5). 시험 조건과 시간 원문: `This example tests ADCIRC version 55 (and beyond). It tests the simulation of the astronomical M2 tidal constituent on the spherical Earth under equilibrium tidal forcing with the inclusion of the self-attraction and loading tide. The results of interest are the M2 tidal constituent amplitudes and phases of elevations and velocities from the least-squares harmonic analysis. The test finishes in about 5 minutes in serial ADCIRC for a full month of simulation. Find the test at the [GitHub test suite](https://github.com/adcirc/adcirc-cg-testsuite/tree/v55/adcirc/adcirc_global-tide-2d).` (5). |
| 7–10 | Mesh — 최소 해상도가 약 50 km인 구면 지구의 성긴 격자(mesh)를 설명한다(9). 꼭짓점(vertices) 27,330개와 삼각형 요소(triangular elements) 50,859개라고 적는다(9). 수치 원문: `The mesh is a coarse representation of the spherical Earth with minimum resolution of approximately 50 km, comprised of 27,330 vertices and 50,859 triangular elements.  ` (9). |
| 11–29 | Options/Features Tested — 좌표 회전(coordinate rotation)이 있는 Mercator 투영(projection), 중력파 항의 완전 암시적 해법(fully implicit scheme), 조석 강제력, 가중 계수와 Smagorinsky 난류 폐합(turbulence closure)을 시험한다(13–21). NetCDF4 조화성분 수위·유속 출력과 fort.13의 내부 조석 에너지 변환(internal tide energy conversion)·이차 저면 마찰(quadratic bottom friction) 속성을 제시한다(23–29). 각 옵션의 값·조건·시간 간격·입출력 파일 원문: ``- `[ICS](/ICS)` = -22: Uses the Mercator projection with a coordinate rotation to remove the pole singularity (need to provide a [fort.rotm](/Fort.rotm)).`` (13); ``- `[IM](/IM)` = 513113: Uses the fully implicit scheme for the gravity wave term (computational time step is 12 minutes).`` (15); ``- `[NTIP](/NTIP)` = 2: equilibrium tide + self-attraction and loading tide forcing (read from a [fort.24 file](/Fort.24_file)).`` (17); ``- `[A00, B00, C00](/A00,_B00,_C00)` = 0.5, 0.5, 0: Ensures that the fully implicit scheme is stable with a large time step.`` (19); ``- `[ESLM](/ESLM)` = -0.2: enables the Smagorinsky turbulence closure with a coefficient of 0.2.`` (21); ``- `[NHAGE](/index.php?title=NHAGE&action=edit&redlink=1)` = 5: outputs the harmonic constituent elevations into a netCDF4 [fort.53 file](/index.php?title=Fort.53_file&action=edit&redlink=1).`` (23); ``- `[NHAGV](/index.php?title=NHAGV&action=edit&redlink=1)` = 5: outputs the harmonic constituent velocities into a netCDF4 [fort.54 file](/index.php?title=Fort.54_file&action=edit&redlink=1).`` (25); `- [internal_tide_friction](/Fort.13_file#Internal_Tide_Energy_Conversion): spatially varying linear wave drag [fort.13 file](/Fort.13_file) attribute accounting for energy conversion due to internal tide generation in the deep ocean.` (27); `- [quadratic_friction_coefficient](/Fort.13_file#Quadratic_Friction_coefficient): spatially varying quadratic bottom friction [fort.13 file](/Fort.13_file) attribute.` (29). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 23–25행: NHAGE·NHAGV·fort.53·fort.54 참조 URL에 `action=edit&redlink=1`이 들어 있다.
