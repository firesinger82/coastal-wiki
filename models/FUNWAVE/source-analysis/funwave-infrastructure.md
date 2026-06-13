---
title: "FUNWAVE-TVD 전수분석 — 인프라(경계·초기화·MPI·IO·전역변수)"
model: FUNWAVE
citation_status: verified
verification_method: "src/bc.F·init.F·parallel.F·io.F·samples.F·statistics.F·nesting.F·misc.F·mod_global.F·mod_param.F·mod_input.F 전수 read (서브에이전트, 2026-06-13). file:line src 기준."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-13
---

# FUNWAVE-TVD 인프라

> 경계조건·초기화·MPI 도메인분해·입출력·초기파형·전역상태. 코어 흐름은 [`funwave-source-map.md`](funwave-source-map.md).

## 1. 경계조건 bc.F
- `BOUNDARY_CONDITION`(:53): 4방향 개방경계 P·Q=0, Fx=0.5g(ξ²Γ3+2ξ·Deps); MASK<1 셀 flux 처리. ABS/LEFT_BC_IRR는 서경계 skip
- `EXCHANGE`(:426): 매 step 주변수(Eta·U·V·HU·HV·MASK·AGE·nu_break) ghost 교환 + 교환후 MASK 곱(land 0) + FILTERING 시 SHAPIRO_3
- `PHI_COLL`(:631): VTYPE별 ghost(1 η대칭/2 u반대칭/3 v반대칭/4 교차0/5 전대칭/6 전반대칭)+PERIODIC+`phi_exch`. (분산은 [`funwave-dispersion-solver.md`](funwave-dispersion-solver.md))
- `PHI_COLL_VARIABLE_LENGTH`(:539): P·Q 등 비표준크기 mirror

## 2. 초기화 init.F
- `ALLOCATE_VARIABLES`(:54): 전 2D 배열 ALLOCATE(좌표·MUSCL L/R·미분·flux·통계·쇄파·sponge·분산 U4/V4/U1p)
- `INITIALIZATION`(:280): 구면격자(Lat_theta·Dx·Dy·Coriolis)·MUSCL kappa(SEC→−1/else→1/3)·수심(DAT파일/FLA상수/SLO경사)·PHI_COLL ghost·BATHY CORRECTION·WaterLevel·DepthX/Y·Cd(In_Cd)·초기파형(INITIAL_*)·WAVEMAKER_INITIALIZATION·CALCULATE_SPONGE·MASK/MASK9·COUPLING_INITIAL·EtaBlowVal
- `INITIAL_UVZ`(:1283): 초기 Eta/U/V/MASK 파일읽기

## 3. MPI parallel.F
- `phi_exch`(:55): 2D real ghost 비동기교환(MPI_IRECV/ISEND/WAITALL, E-W len=Nloc·Nghost, N-S len=Mloc·Nghost)
- `phi_exch_variable_length`(:184)/`phi_int_exch`(:314, MASK용 INTEGER)
- `DISTRIBUTE_VarGlob`(:446): rank0 전역배열→ghost확장 PHIGLOB→각 rank 로컬블록 MPI_ISEND 분배

## 4. 입출력 io.F (13 subr)
- `OUTPUT`(:52): dispatcher(SCREEN_INTV→STATISTICS, PLOT_INTV→PREVIEW, station, VESSEL/SEDIMENT/FOAM 카운터)
- `READ_INPUT`(:149, 5065줄 최장): input.txt 전체 파싱(READ_STRING/FLOAT/INTEGER/LOGICAL) — 격자·수심·시간·WaveMaker·DISPERSION·Gamma·breaking·sponge·friction·OUT_* 플래그. RESULT_FOLDER 생성
- `PREVIEW`(:4304): 필드출력(eta_00001 5자리, OUT_ETA/U/V/MASK/Hmax... → PutFile). `PREVIEW_MEAN`(:4630): 시간평균(Hsig·Sxx)
- `STATIONS`(:3786 Cart/:4132 Sph): station 시계열(time,eta,u,v) 버퍼→ASCII. `GetFile`(:4751, PARALLEL 분배)·`PutFile`(:4863/:4894, ASCII/binary)

## 5. 초기파형 samples.F (11 subr)
- `SOLITARY_WAVE_LEFT_BOUNDARY`(:56): 서경계 고독파 `a/cosh²(...)`
- `INITIAL_GAUSIAN`(:258, INI_GAU) `AMP·exp(−r²/WID²)` / `INITIAL_RECTANGULAR`(:173, INI_REC) / `INITIAL_DIPOLE`(:347, INI_DIP) / `INITIAL_N_WAVE`(:439, Tadepalli-Synolakis) / `INITIAL_SOLITARY_WAVE`(:511, INI_SOL Nwogu)+`SUB_SLTRY`(:582 Newton 계수)

## 6. statistics.F·nesting.F·misc.F
- `STATISTICS`(statistics.F:52): MassVolume·Energy(0.5gH²+0.5u²H)·MaxEta·Froude 출력+`CHECK_STATISTICS`(:192 NaN→MPI_ABORT)
- `COUPLING_INITIAL`(nesting.F:53)/`OneWayCoupling`(:357): parent grid 경계 시계열 선형보간→ghost (one-way nesting)
- `INDEX`(misc.F:54): MPI_CART_CREATE(PX×PY)·n_west/east/suth/nrth·iista/iiend·Mloc=(iiend−iista+1)+2Nghost
- `ESTIMATE_DT`(misc.F:216): CFL `DT=CFL·min(DX/|U+c|,DY/|V+c|)`+MPI_ALLREDUCE(MIN)
- `MAX_MIN_PROPERTY`(:307)·`CHECK_BLOWUP`(:394 |Eta|>EtaBlowVal→중단)·`SHAPIRO_3`(:479 a1=44/64 저역필터)

## 7. 전역상태 mod_global·param·input
- **GLOBAL**(mod_global.F:52): 주변수 U·V·HU·HV·Eta·Eta0·Ubar·Vbar / 수심 Depth·H·Depthx·Depthy / flux Fx·Fy·Gx·Gy·P·Q / MUSCL UxL·UxR·EtaRxL... / 분산미분 Uxx·Uxy·Vyy·DUxx... / 시간미분 Ut·Vt·Utxx... / 분산중간 U4·V4·U1p·V1p·U2·U3 / MASK·MASK9 / 쇄파 AGE_BREAKING·nu_break·ROLLER_FLUX / SPONGE / 통계 Umean·ETAmean·UUsum·SigWaveHeight / MPI myid·n_west·ProcessorID·iista. 분산제어 gamma1/2/3(g3=0 선형SWE)·Beta_ref=−0.531·Nghost=3
- **PARAM**(mod_param.F:53): SP precision(DOUBLE→8 / else SELECTED_REAL_KIND(6,30)), grav=9.81·pi·R_earth=6371000·RHO_WATER=1000·RHO_AIR=1.15·SMALL=1e-6, 공유 I/J/K/tmp1~5
- **INPUT_READ**(mod_input.F:53): READ_INTEGER/FLOAT/LOGICAL/STRING(KEY=VALUE 파싱, `CHECK_CONSISTENCY_TYPE` 타입판별)

## 8. 전체 호출 흐름
```
main → READ_INPUT(io) ← INPUT_READ
     → INDEX(misc, MPI_CART) → ALLOCATE_VARIABLES(init) → INITIALIZATION(init: PHI_COLL→phi_exch, GetFile→DISTRIBUTE_VarGlob, COUPLING_INITIAL)
     → [시간루프] ESTIMATE_DT → BOUNDARY_CONDITION → EXCHANGE/EXCHANGE_DISPERSION → OneWayCoupling → MAX_MIN_PROPERTY → CHECK_BLOWUP
                → OUTPUT(STATISTICS / STATIONS / PREVIEW→PutFile)
```

## 9. 연결
- [`funwave-code-graph.md`](funwave-code-graph.md) · [`funwave-source-map.md`](funwave-source-map.md) · [`funwave-dispersion-solver.md`](funwave-dispersion-solver.md) · [`funwave-flux-tvd.md`](funwave-flux-tvd.md) · [`funwave-physics-sources.md`](funwave-physics-sources.md) · [`funwave-feature-modules.md`](funwave-feature-modules.md)
