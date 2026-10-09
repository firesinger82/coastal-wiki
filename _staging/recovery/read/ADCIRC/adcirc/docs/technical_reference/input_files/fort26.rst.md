---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort26.rst
lines: 57
sha256: 2f36f03fb8400da0c0bb39e22337b3c0f6a7a2714304f8afad6b40a89819fa4f
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort26.rst — 판독 구간 기록

구간은 1행부터 57행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | Fort.26: SWAN Runtime Parameters and Coupling File / File Structure — SWAN 실행 매개변수와 ADCIRC 결합(coupling) 정보를 담는 필수 파일이다(6). SWAN 기본 INPUT 파일의 ADCIRC 이름 및 Fortran 유닛(unit) 번호가 fort.26이라고 적는다(6). 형식은 SWAN 사용자 설명서 3장과 결합 실행 웹페이지를 참조한다(11–13). 원문: `The fort.26 file contains the SWAN runtime parameters as well as the coupling details between ADCIRC and SWAN. This file is required to run the ADCIRC+SWAN model. Note that the name "fort.26" is ADCIRC's name (and fortran unit number) for the SWAN input command file, typically named INPUT by default.` (6). |
| 15–19 | Specifying Input — 일반적으로 파랑 초기조건(initial conditions)을 강제하지 않는다고 적는다(18). SWAN 2차원 스펙트럼(spectra) 경계 입력 가능성은 아직 시험 또는 확인하지 않았으며 BOUNDSPEC 사용 가능성을 조건부로 설명한다(18). 불확실성을 원문 그대로 보존한다. 원문: `Typically, SWAN+ADCIRC runs do not force wave initial conditions. However, the SWAN portion of the model may be able to accommodate SWAN 2D spectral input as a boundary condition, though this has not yet been tested/confirmed. The BOUNDSPEC command could allow the user to identify the fort.14 boundary nodestring for applying the spectra and then define the spectral parameters. The SWAN manual includes documentation on ASCII file format for SWAN spectra, which applies to both input/output spectra: [2].` (18). |
| 20–26 | Specifying Output — SWAN 전체 출력은 ADCIRC 기상 출력 시각에 따르며 계산 간격과 출력 간격이 일치하지 않으면 SWAN 출력이 쓰이지 않는다고 적는다(23). QUANTITY 뒤 TEST 앞에서 지점 정의와 스펙트럼·표 시계열 출력을 지정하는 순서이다(25). 원문: ``Timing of SWAN global output files (swan_HS.63, swan_TPS.63, swan_TMM10.63, and swan_DIR.63) derives from the timing specified for ADCIRC global meteorological output in the :ref:`Model Parameter and Periodic Boundary Condition File <fort15>`. Note that the SWAN calculation interval in the fort.26 must coincide with the ADCIRC meteorological output interval or SWAN output will not be written.`` (23); `The fort.26 allows for output of wave parameters or 1D/2D spectra at user-specified points. For SWAN+ADCIRC applications, point output specification will typically occur after the QUANTITY command and before the TEST command. First, the user defines a group of points ('sname' from the SWAN manual) by either identifying their x and y coordinates directly in the fort.26 or within a separate file ('fname' in SWAN parlance). Next, the SPECOUT command triggers spectral output, and/or TABLE triggers time series output of desired wave parameters and time steps.` (25). |
| 27–48 | Example / 출력 명령 — 별도 좌표 파일, 1차원·2차원 스펙트럼과 파고·주기·방향 지점 출력 명령을 제시한다(30–40). 시작 날짜·1200초 간격·HHMMSS 표기와 해당 지점이 있는 PE 하위 격자 디렉터리(subgrid directories) 출력을 설명한다(43–47). 원문: `.. code-block:: none` (32); `   POINTS 'SpecPts' File 'SpecLongLat.loc'` (34); `   SPECout 'SpecPts' SPEC1D ABS '1DSpecOutABS' OUT 19640903.000000 1200 SEC` (36); `   SPECout 'SpecPts' SPEC2D ABS '2DSpecOutABS' OUT 19640903.000000 1200 SEC` (38); `   TABLE 'SpecPts' HEAD 'WavesOut.txt' HS TPS DIR OUT 19640903.000000 1200 SEC` (40); `In this example:` (42); `- Longitude/latitude coordinates are specified (space delimited without header) inside a file called SpecLongLat.loc` (43); `- The two SPECOUT lines request 1D and 2D spectra written to 1DSpecOutABS and 2DSpecOutABS` (44); `- A table of Hs, Tps, and Dir will be written to WavesOut.txt every 1200 seconds beginning 9/3/1964 at 00:00:00` (45); `- The six values after the date and decimal represent HHMMSS, not decimal day` (46); `- The output files will be written to the PE subgrid directories that contain the output location points` (47). |
| 49–57 | Example contents of SpecLongLat.loc — SpecLongLat.loc의 경도·위도(longitude/latitude) 좌표 다섯 줄을 헤더 없이 제시한다(49–57). 원문: `.. code-block:: none` (51); `   -81.299940 29.898530` (53); `   -81.303200 29.898450` (54); `   -81.303440 29.893390` (55); `   -81.300740 29.889340` (56); `   -81.295050 29.890450 ` (57). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 18행: SWAN 스펙트럼 형식을 가리키는 문장 끝에 `[2]`가 있다. 이 파일에는 그 번호의 참고문헌 또는 링크 정의가 없다.
