---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.26_file.md
lines: 40
sha256: 77bc648e6a95a2d63da1a7f82982f0f63742554954ccba8734d215ca1b4f5ce6
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.26_file.md — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Fort.26 file / 역할·필수 여부 — 제목·판본·빈 줄을 포함한다(1–4). SWAN 실행 매개변수(runtime parameters)와 ADCIRC-SWAN 결합(coupling) 정보를 담는 필수 파일이라고 명시한다(5). fort.26은 ADCIRC의 이름 및 Fortran 단위 번호(unit number)이며 SWAN 명령 입력 파일의 일반 기본 이름을 함께 적는다(5). 원문: `The fort.26 file contains the the SWAN runtime parameters as well as the "coupling" details between ADCIRC and SWAN.  This file is required to run the ADCIRC+SWAN model.  Note that the name "fort.26" is ADCIRC's name (and fortran unit number) for the SWAN input command file, typically named INPUT by default.  ` (5). |
| 7–12 | File Format — SWAN 사용자 설명서 3장과 ADCIRC+SWAN 실행 안내 웹페이지로 연결한다(9·11). 실제 파일 형식의 상세 내용은 이 구간에 없다. |
| 13–17 | Specifying Input — 보통 파랑 초기조건을 강제하지 않는다고 적는다(15). SWAN 2D 스펙트럼(spectrum) 경계 입력 가능성은 아직 시험·확인되지 않았다고 명시한다(15). 경계 절점열(nodestring)과 스펙트럼 매개변수를 지정할 수 있는 명령의 가능성을 설명하고 별도 ASCII 스펙트럼 형식 문서로 연결한다(15–16). 원문: `Typically, SWAN+ADCIRC runs do not force wave initial conditions. However, the SWAN portion of the model may be able to accommodate SWAN 2D spectral input as a boundary condition, though this has not yet been tested/confirmed. The BOUNDSPEC command could allow the user to identify the fort.14 boundary nodestring for applying the spectra and then define the spectral parameters. The SWAN manual includes documentation on ASCII file format for SWAN spectra, which applies to both input/output spectra:` (15). |
| 18–29 | Specifying Output / 제어·명령 예시 — SWAN 전체 격자 출력 시각은 ADCIRC 기상 출력 시각에서 나오며 계산 간격과 기상 출력 간격이 일치하지 않으면 출력하지 않는다고 명시한다(20). 지정점(point)의 좌표·별도 파일·스펙트럼·파랑 매개변수 시계열(time series)을 정의하는 순서와 명령 예시를 제시한다(20–28). 원문: `Timing of SWAN global output files (swan_HS.63, swan_TPS.63, swan_TMM10.63, and swan_DIR.63) derives from the timing specified for ADCIRC global meteorological output in the fort.15 run control file. Note that the SWAN calculation interval in the fort.26 must coincide with the ADCIRC meteorological output interval or SWAN output will not be written. The fort.26 allows for output of wave parameters or 1D/2D spectra at user-specified points. For SWAN+ADCIRC applications, point output specification will typically occur after the QUANTITY command and before the TEST command. First, the user defines a group of points (‘sname’ from the SWAN manual) by either identifying their x and y coordinates directly in the fort.26 or within a separate file (‘fname’ in SWAN parlance).  Next, the SPECOUT command triggers spectral output, and/or TABLE triggers time series output of desired wave parameters and time steps. The following lines show an example from a fort.26 that requests both spectral output and wave parameter point time series:` (20); `POINTS 'SpecPts' File 'SpecLongLat.loc'` (22); `SPECout 'SpecPts' SPEC1D ABS '1DSpecOutABS' OUT 19640903.000000 1200 SEC` (24); `SPECout 'SpecPts' SPEC2D ABS '2DSpecOutABS' OUT 19640903.000000 1200 SEC` (26); `TABLE   'SpecPts' HEAD 'WavesOut.txt' HS TPS DIR OUT 19640903.000000 1200 SEC` (28). |
| 30–40 | Specifying Output / 예시 해설·좌표 파일 — 헤더 없이 공백으로 구분한 경도·위도 파일, 1D·2D 스펙트럼 및 지정점 출력 파일과 시작 날짜·시간·간격을 설명한다(30). 소수점 뒤 여섯 자리는 HHMMSS이며 일의 소수가 아니라고 명시한다(30). 해당 지정점이 속한 PE 하위 격자 디렉터리에 출력하고 좌표 파일의 다섯 입력행을 제시한다(30–40). 원문: `In this example, longitude/latitude coordinates are specified (space delimited without header) inside a file called SpecLongLat.loc; the two SPECOUT lines request 1D and 2D spectra written to 1DSpecOutABS and 2DSpecOutABS; and a table of Hs, Tps, and Dir will be written to WavesOut.txt every 1200 seconds beginning 9/3/1964 at 00:00:00. The six values after the date and decimal represent HHMMSS, not decimal day. Note that the output files will be written to the PE subgrid directories that contain the output location points. Example contents of SpecLongLat.loc:` (30); `-81.299940 29.898530` (32); `-81.303200 29.898450` (34); `-81.303440 29.893390` (36); `-81.300740 29.889340` (38); `-81.295050 29.890450` (40). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 15: SWAN 2D 스펙트럼 경계 입력 가능성은 `this has not yet been tested/confirmed`라고 적혀 있다. 이 파일은 해당 기능의 확인 결과를 제공하지 않는다.
