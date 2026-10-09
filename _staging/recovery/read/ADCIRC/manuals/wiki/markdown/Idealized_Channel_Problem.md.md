---
file: models/ADCIRC/raw/manuals/wiki/markdown/Idealized_Channel_Problem.md
lines: 36
sha256: 8b16c7e0f0d01c088635a8ff1e80473ff040585dbb620ef875d650ce57ca3db4
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Idealized_Channel_Problem.md — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Idealized Channel Problem — ADCIRC 버전 55 이상에서 경사진 해변 중앙의 수로(channel)와 일주조(diurnal tide)를 시험하는 예제이다(5). 측면 주기 경계조건(periodic lateral boundary conditions)과 흡수·생성 스펀지층(absorption-generation sponge layer)을 시험한다(5). 원문은 2개 프로세서로 6시간 모의를 약 8분에 마친다고 적는다(5). 6시간 길이는 시험 모음의 실행 시간을 제한하기 위한 것이며 사용자가 늘릴 수 있다고 적는다(5). 제목·판본·빈 줄을 포함한다(1–6). 원문: `This example tests ADCIRC version 55 (and beyond). It tests the simulation of a diurnal tide on a sloping beach with a channel along its centerline (adapted from[&#91;1&#93;](#cite_note-Keith-1)). It tests lateral periodic boundary conditions and the absorption-generation sponge layer[&#91;2&#93;](#cite_note-Pringle-2)[&#91;3&#93;](#cite_note-Pringle2-3). The test finishes in about 8 minutes in parallel ADCIRC (2 processors) for 6 hours of simulation. Note that the short 6 hour length of the test is chosen only to limit simulation time for the [GitHub test suite](https://github.com/adcirc/adcirc-cg-testsuite/tree/v55/adcirc/adcirc_ideal_channel-2d-parallel) where the test case been found. Users may extend the simulation length to simulate more of the inundating phase of the incoming wave.  ` (5). |
| 7–13 | Mesh — 격자는 64,415개 꼭짓점과 127,784개 삼각 요소(triangular elements)로 이루어지며 해상도 범위를 적는다(9). 동서 대칭 격자로 반대 측면 절점을 대응시킨다(9). 남쪽에는 수위 지정 경계와 스펀지층을 둔다(9). 11행 캡션은 왼쪽 삼각 격자·해상도와 파란 수위 경계, 초록·노랑 주기 경계, 가운데 지형·수심, 오른쪽 스펀지 계수를 설명한다. 12행은 수위와 남북 속도 시계열 애니메이션 캡션이다. `IdealChannel.png`(11), `Channel_Elev.gif`(12), `Channel_Vel.gif`(12): 그림 파일 없음. 캡션만 읽었으며 그림의 축·기호·값은 확인하지 못했다. 원문: `The mesh is comprised of 64,415 vertices and 127,784 triangular elements, with resolution in the 10-60 m range. The mesh is symmetrical in the east-west direction so that the east and west lateral boundary vertices match for the application of the periodic lateral boundary conditions. An elevation specified boundary condition and absorption-generation sponge layer is prescribed at the southern end of the domain.` (9). |
| 14–29 | Options/Features Tested — 명시적 적분과 시간 간격, 필수 계수, 수위·유속·기상 netCDF4 출력 옵션을 적는다(16–24). 스펀지층은 유입 일주조를 생성하면서 유출 파를 흡수한다(26). 입력 파일과 OceanMesh2D 자동 생성 함수를 안내한다(26). IBTYPE=94는 반대 측면 경계의 절점 쌍에 주기 경계조건을 적용한다(28). 모든 값과 조건을 원문 그대로 옮긴다. 원문: ``- `[IM](/IM)` = 111112: Uses the explicit scheme (computational time step is 2 seconds).`` (16); ``- `[A00, B00, C00](/A00,_B00,_C00)` = 0.0, 1.0, 0.0: Must be used with explicit scheme.`` (18); ``- `[NOUTGE](/index.php?title=NOUTGE&action=edit&redlink=1)` = 5: Outputs the global elevations into a netCDF4 [fort.63 file](/Fort.63_file).`` (20); ``- `[NOUTGV](/index.php?title=NOUTGV&action=edit&redlink=1)` = 5: Outputs the global velocities into a netCDF4 [fort.64 file](/Fort.64_file).`` (22); ``- `[NOUTGM](/index.php?title=NOUTGM&action=edit&redlink=1)` = 5: Outputs the global meteorology into a netCDF4 [fort.73 file](/Fort.73_file) (pressure) and a netCDF4 [fort.74 file](/Fort.74_file) (velocity).`` (24); `- [sponge_generator_layer](/Fort.13_file#Absorption-generation_Sponge_Layer): Applies a sponge layer to absorb outgoing waves while generating incoming waves. In this case incoming diurnal tidal waves are generated using the [fort.53001](/index.php?title=Fort.53001&action=edit&redlink=1) and [fort.54001](/index.php?title=Fort.54001&action=edit&redlink=1) input files. [OceanMesh2D](/Grid_Development_and_Editing#OceanMesh2D) functions can be used to automatically generate the sponge_generator_layer attribute ([Calc_Sponge](https://github.com/CHLNDDEV/OceanMesh2D/blob/Projection/utilities/Calc_Sponge.m)) and the input files ([Make_f5354](https://github.com/CHLNDDEV/OceanMesh2D/blob/Projection/utilities/Make_f5354.m)).` (26); `- [IBTYPE=94](/Fort.14_file_format): Node pairs are matched along opposite lateral boundaries where a periodic (repeating) boundary condition is applied.` (28). |
| 30–36 | References — 동적 부하 균형(dynamic load balancing), 순압 모델의 조석 비교, 경압 결합 관련 논문 세 편의 서지와 DOI를 적는다(30–36). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 11행: `/File:IdealChannel.png`의 로컬 그림 파일 없음.
- 12행: `/File:Channel_Elev.gif`의 로컬 그림 파일 없음.
- 12행: `/File:Channel_Vel.gif`의 로컬 그림 파일 없음.
- 20·22·24·26행: NOUTGE, NOUTGV, NOUTGM, fort.53001, fort.54001 링크에 `action=edit&redlink=1`이 있다.
