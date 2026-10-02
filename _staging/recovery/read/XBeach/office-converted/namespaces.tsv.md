---
file: _staging/recovery/extract/XBeach/office/namespaces.tsv
lines: 60
sha256: f208e6f531415a67bf64d213e8da70b417387b83beac4db2e84e29ce25962717
reader: codex gpt-6.1-sol
read_date: 2026-10-02
original: models/XBeach/raw/source_code/trunk/doc/misc/namespaces.xls
---

# namespaces.tsv — 판독 구간 기록

구간은 1행부터 60행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Sheet1 변환 헤더(1)는 57행×6열로 표시된다. 열 표제 category·namespaces·source files와 뒤의 숫자(2). applications and libraries(3)의 네임스페이스는 하이픈이고 xbeach·libxbeach·동적 라이브러리·include 생성 파일을 나열(3–6). 7행은 빈 셀 행이다. 원문: `### sheet Sheet1 (57x6)` (1), `category	namespaces	source files		43.0	47.0` (2), `applications and libraries	-	xbeach.F90` (3), `libxbeach.F90` (4), `libxbeach_dynamic.F90` (5), `makeincludes.F90` (6). |
| 8–18 | model input and output(8). input은 입력 및 입력 읽기 파일(8–9), output은 출력·후처리·Fortran·NetCDF 파일(11–14), fileio는 파일 I/O·로그 파일(16–17)에 대응한다. 10·15·18행은 빈 셀 행이다. 원문: `model input and output	input	input.F90` (8), `input_read.F90` (9), `output	output.F90` (11), `output_postprocess.F90` (12), `output_fortran.F90` (13), `output_netcdf.F90` (14), `fileio	fileio.F90` (16), `fileio_log.F90` (17). |
| 19–24 | boundary conditions의 bc는 파랑·파랑 스펙트럼·흐름 경계 파일(19–21)에 대응한다. time management의 time은 시간 파일(23)에 대응하며, 22·24행은 빈 셀 행이다. 원문: `boundary conditions	bc	bc_wave.F90` (19), `bc_wave_spectral.F90` (20), `bc_flow.F90` (21), `time management	time	time.F90` (23). |
| 25–29 | physics / wave(25). 파랑 본체·소산·이류·선박파 파일(25–28)을 묶고 29행은 빈 셀 행이다. 원문: `physics	wave	wave.F90` (25), `wave_dissipation.F90` (26), `wave_advection.F90` (27), `wave_ship.F90` (28). |
| 30–37 | physics의 flow(30). 흐름 본체·비정수압·2차 보정·해법·drifter·유량·지하수 파일(30–36)을 묶는다. 범주 셀은 비어 있으며 physics 표기는 앞 25행에 있다. 37행은 빈 셀 행이다. 원문: `flow	flow.F90` (30), `flow_nonh.F90` (31), `flow_secondorder.F90` (32), `flow_solver.F90` (33), `flow_drifters.F90` (34), `flow_discharges.F90` (35), `flow_groundwater.F90` (36). |
| 38–44 | physics의 sedtrans(38)는 수송 본체·파형·평형농도 파일(38–40), bedupdate(42)는 지형 갱신·Beachwizard 파일(42–43)을 묶는다. 41·44행은 빈 셀 행이다. 원문: `sedtrans	sedtrans.F90` (38), `sedtrans_waveform.F90` (39), `sedtrans_eqconc.F90` (40), `bedupdate	bedupdate.F90` (42), `bedupdate_beachwizard.F90` (43). |
| 45–49 | technical(45). mpi는 MPI 확장 파일(45), c는 introspection과 mnemonic 파일(47–48)에 대응한다. 46·49행은 빈 셀 행이다. 원문: `technical	mpi	mpi_extensions.F90` (45), `c	c_introspection.F90` (47), `c_mnemonic.F90` (48). |
| 50–54 | utilities / utils(50). 수학·mnemonic·공간 매개변수·상수 유틸리티 파일(50–53)을 묶는다. 54행은 빈 셀 행이다. 원문: `utilities	utils	utils_math.F90` (50), `utils_mnemonic.F90` (51), `utils_spaceparams.F90` (52), `utils_constants.F90` (53). |
| 55–60 | types / type(55). params·spaceparams·waveparams·timeparams 형식 파일(55–58)을 묶는다. Sheet2·Sheet3 변환 헤더는 각각 0행×0열로 표시된다(59–60). 원문: `types	type	type_params.F90` (55), `type_spaceparams.F90` (56), `type_waveparams.F90` (57), `type_timeparams.F90` (58), `### sheet Sheet2 (0x0)` (59), `### sheet Sheet3 (0x0)` (60). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 2: `category`, `namespaces`, `source files` 뒤에 빈 표제 셀과 `43.0`·`47.0`이 있으며 두 숫자의 의미는 이 파일 안에 설명되어 있지 않다.
- 59–60: `Sheet2 (0x0)`·`Sheet3 (0x0)` 헤더만 있고 해당 시트의 데이터 행은 없다.
