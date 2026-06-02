# INDEX

위키 전체 항목의 living map. 새 항목 추가 시 여기에도 등록.

## concepts/ (도메인 개념)

| 토픽 | 상태 | 비고 |
|---|---|---|
| [tides](concepts/tides/) | **DRAFT** (01-05 verified, 06 source-needed) | 조석 — 5/6 verified. 06은 `models/<model>/` 작성 후 verified 가능 |
| [waves](concepts/waves/) | **STABLE** (01-06 verified + 04 §3.4 WW3 SMC boundary issue verified) | 파랑 — 6/6 verified. Holthuijsen 2007 + KHOA 284 용어 + SWAN library + MPT 74정점 + **04 §3.4 WW3 SMC nested grid boundary mismatch spurious energy bug (Issue #1600 OPEN, UK Met Office, 2026-05-28 GitHub API verbatim)** |
| [sediment-transport](concepts/sediment-transport/) | **STABLE** (01-04·06 verified, 05 source-needed) | 표사이동 — 5/6 verified. Soulsby 1997 + KHOA 113 용어 + EFDC SED (Original/SEDZLJ) + Delft3D/XBeach/ROMS source-analysis 통합 |
| [currents](concepts/currents/) | **DRAFT** (01-05 verified, 06 source-needed) | 조류 — 5/6 verified (UTide 2D + 수치조류도 + KHOA 60+ 용어). 동해 수치조류도 미커버 명시 |
| [sst](concepts/sst/) | **STABLE** (01·02·03·04·05 verified, 06 source-needed) | 해수면 수온 — 5/6 verified. 01 정의, 02 heat budget, 03 회귀·MHW, 04 5 데이터셋 운영, 05 MHW 식별 실행 (13정점 ~180 events). experience/ 4건 연결 |
| [littoral-drift](concepts/littoral-drift/) | **DRAFT** (01·02 verified) | 연안표사 — 2/6 verified. 01 정의·CERC·Komar-Inman, 02 Holthuijsen §7.4.2-3 radiation stress + Bowen 1969 / Battjes 1974 longshore current 유도 |
| [storm-surge](concepts/storm-surge/) | **DRAFT** (01·02·03·04·07 verified, 05 partial-verified Hinnamnor+Bolaven, Maemi source-needed, 06 미생성) | 폭풍해일 — 5/7 verified + 1/7 partial. 01 정의, 02 Pugh §6-7 + ADCIRC GWCE + **§3.4 hurricane PBL Sathia & Giometto 2026 (arxiv:2605.03933) verified — 두 scaling 식 u_*/β·u_*/√(βN) + 2.5% 오차 abstract 직접 fetch + §3.4.4~3.4.8 PDF 34p full read 보강 (2026-05-28): derivation Pollard 1973 응용, LES 216 sims 256×256×512 격자 + Bou-Zeid Smagorinsky, parity R²=0.99 RMSE 23.5m / neutral C_R=0.58 RMSE 6.92m, characteristic heights v_max 65-85%·inflow 6-20% of h, R-scaling h~R^((1-n)/2)·K_m~R^(-2n), 결합식 B1 p=4**, 03 separation·MK trend·return period (Pugh §6:1 §7:8 §8:3:2-3), 04 NWS modes·KHOA + **archive ~1년 verified**, **05 §2 Hinnamnor 2022 verified — 포항 137 cm 9월 누년대비 +36 cm spike + 울산 124 cm + 마산/통영 음의 편차 (영향 없음) + 생일도 부이 H_s=5.81 m + 9월 풍속 18.6 m/s, KHOA Annual Report 2022 §3 표 3-5/3-258/3-253/3-223/3-213 직접 인용 ([[khoa-annual-2022-hinnamnor-surge]] 분리, 2026-05-28)** + Bolaven 2012 군산외해 ADCP 잔차 verified ([[khoa-annual-2012-bolaven-surge]]) + Maemi 2003 source-needed (KHOA Annual 2012부터 변환, 2003 부재), **07 ML emulators — PACT (Liu et al. 2026 arxiv:2605.09036, PDF 41p full read 2026-05-28: 5 CMIP6 모델 + 4-station Battery/Boston/Lewes/CBBT + Table 2 RMSE 0.027-0.034m / 5% peak ~50% baseline 대비 / inference 3.4s vs ADCIRC 4.5-7h / Table 7-8 reanalysis-GCM gap NCEP→GCM 0.15m vs GCM↔GCM 0.05m / Peak-Aware loss eq 35) + StormNet (Nader·Dawson et al. 2026 arxiv:2604.20688 GNN-LSTM bias correction, US Gulf Coast 학습 / Idalia 2023, RMSE 48h>70% 72h>50%) verified entries**. ADCIRC source-analysis/storm-surge/ 7개 promote 완료 |

## models/ (모델별 객관 자료)

| 모델 | 상태 | 비고 |
|---|---|---|
| [EFDC](models/EFDC/) | **WIP** (source-analysis 20 + manual-notes 5 verified) | 사용자 주력 — SedTran-Original/SEDZLJ + hydro core + boundary + wetdry. manual-notes: overview + user r850 + theory v12 (TOC) + sediment 2003 + **theory v12 Ch 2 hydrodynamics deep (식 2.1-2.150 + Mellor-Yamada 4 옵션 + 5 wind drag + SIG/SGZ)** + **`source-analysis/efdc_dispersion.md` verified (2026-05-28) — calhdmf.f90/calhdmf3.f90/calhdmf.for/caldiff.for direct read: Smagorinsky $A_H = AHOXY + AHDXY \cdot \Delta x \Delta y \sqrt{D}$ + 2TL DSQR `0.5*SXY²` (Craig 2011 fix) vs 3TL/GVC 1/16 corner avg + ISHDMF 0/1/2 옵션 + AHMAP.INP spatially variable (input.f90:3722-3795) + Card C12 default `AHD=0.025`** + **`source-analysis/sediment/efdc_sedzlj.md` verified (2026-05-28) — SedTran-SEDZLJ/ 5 sub-routine direct read (s_main 359 + s_sedzlj 917 + s_shear 340 + s_slope 110 + s_bedload 293 = 2019 lines): Christoffersen-Jonsson 1985 wave-current shear (Eq 3.8/3.10/4.11/4.12/4.23/4.25) + Gessler 1965 / Krone deposition probability + Sedflume ERATEND vs power-law A·τ^N erosion + active-layer TACT = TACTM·D50·τ/τcrit·ρb + Van Rijn 1981 Eq 20a/20b/21 bedload + Lick 2009 Eq 3.36 SH_SCALE slope correction + Card C36 NSEDFLUME=0/98/99 dispatch** |
| [SWAN](models/SWAN/) | **STABLE+** (source-analysis 29 + manual-notes 9 + web-refs 1 verified = 39, 2026-06-02 +3 swantech Ch2: dissipation·nonlinear·obstacles) | 천해 풍파 spectral · Holthuijsen 공동개발 · 모든 source-term · scheme · 추가 promote 다수 + **swantech.pdf (v41.51) Ch 2 deep-verify 완료 (6 notes, §2.1-2.6 전구간 + §2.3.5-8)**: `swan-tech-ch2-governing-equations` (§2.1-2.2 Eq 2.16 action balance) + `swan-tech-ch2-sources-sinks` (§2.3.1-2 general+wind Eq 2.27-2.37) + **`swan-tech-ch2-dissipation-detailed` verified (2026-06-02) — §2.3.3 Eq 2.43-2.74: whitecapping Komen/saturation-Yan/opposing-current/ST6 + bottom friction JONSWAP/Collins/Madsen + depth-breaking BJ/Thornton-Guza, 계수값 verbatim (C_ds·δ·γ=0.73 등)** + **`swan-tech-ch2-nonlinear-detailed` verified (2026-06-02) — §2.3.4 Eq 2.75-2.108: quadruplets DIA(Hasselmann 1985)/WRT-XNL(Van Vledder) + triads FTIM(2.100)·SPB(2.101)·LTA(2.102)·ext-LTA(2.103)·biphase(2.104-5)·4 interaction-coeff(Freilich-Guza/Madsen-Sørensen/Bredmose/QuadWave-Akrish2024)·DCTA(2.106-8 Booij/Zijlema2022/Benit-Reniers noncollinear), 41.51 신설 체계** + **`swan-tech-ch2-obstacles-diffraction-setup` verified (2026-06-02) — §2.5-2.6 Eq 2.131-2.147: Goda(2.131)/d'Angremond(2.132-5) transmission + freeboard R/T tanh(2.136-7) + Holthuijsen2003 phase-decoupled diffraction(2.138-44) + Dingemans1987 set-up(2.145-7)** + `swan-tech-ch2-vegetation-ice-bragg-gen12` (§2.3.5-8) ※ **PDF↔online HTML 식번호 offset 발견·정리** (HTML이 중간식 추가번호; dissipation +1 → triads +15; 본 위키는 PDF 번호 채택) + **`manual-notes/swan-booij-1999-jgr-foundational.md` verified (2026-06-01) — Part 1 doi:10.1029/98JC02622 JGR 104 pp.7649-7666 + Part 2 doi:10.1029/1998JC900123 pp.7667-7681 bibliographic + abstract verbatim** + **`manual-notes/swan-documentation-stack.md` verified (2026-06-01) — 4 PDF docs (swanuse 154p + swantech 176p + swanimp 35p + swanpgr 51p) TOC verbatim + Ch 1 정확 인용: Cycle III 41.51 / SWAN cycle 1·2·3 historical (30.62/30.75/40.01/32.10) / WAM-WAVEWATCH-TOMAWAC 비교 / GitLab hosting since 41.41 / 57 User commands list / 8 Tech chapters + 본 위키 20 노트 매핑 표** + **`source-analysis/swan-source-coverage-audit.md` verified (2026-06-01) — 58 source files inventory (Swan*.ftn90 47 + legacy .ftn 11) + 12 신규 발견 (SwanIEM 41.85 surfbeat / SwanBraggScat 41.80 / SwanGSECorr 41.00 GSE / SwanQCM 41.90 quasi-coherent / mod_xnl4v5 8989라인 Van Vledder XNL4 / SwanCompUnstruc 41.20 Casey Dietrich ADCIRC contributor / SwanReadADC·Easymesh·Triangle multi-format grid readers / SwanVTKWrite 3 files) — 8 신설 후보 식별** |
| [ADCIRC](models/ADCIRC/) | **WIP** (source-analysis 42 + local-workflow 11 + manual-notes 21 verified + web-refs 1 + swan-coupling §SWAN Temporal Controls verified + DG #502 verified) | NWS modes + GAHM/AHM + tide + storm-surge. manual-notes 21 verified (M-B audit), local-workflow 11 → source-analysis/local-workflow/ 이관 (2026-05-24) + **`adcirc-swan-coupling.md §SWAN Temporal Controls` verified (2026-05-28) — PR #498 (OPEN, phase 1 of 2) GitHub API + diff 직접 fetch: SWANTimeControl namelist + RunStartDateTime + fort.26 COMPUTE 카드 + couple2swan.F SwanTimeStep [1,SWAN_MTC] gate + sentinel fallback. Storm landfall 시간 only SWAN compute → ADCIRC+SWAN coupled wall-clock 절감** + **`adcirc-dg-continuity-solver.md` verified (2026-06-01) — PR #502 (OPEN WIP, author namo626, 2026-04-29) GitHub API fetch: 25 files / +10,358 -67 lines / 5 신규 .F90 (dg 5733 + dg_integration 1324 + messenger_elem 1189 + slopelimiter 206 + precipitation 159) + modified decomp 1303 라인 element-based partition. DG modal `ZE(i,j,k)` + TVD-RK + Barth-Jespersen slope limiter (slopeflag=6) + face-based MPI MESSENGER_ELEM. dofh=1 P1 only 현재. WIP — checklist/test/publication 모두 unchecked** |
| [XBeach](models/XBeach/) | **WIP** (source-analysis 16 + manual-notes 3 verified + web-refs 1) | morphology · avalanching · bed_friction · wave_boundary. manual-notes 3 verified 2026-05-24 (xbeach.readthedocs.io examples audit) |
| [Delft3D](models/Delft3D/) | **WIP** (source-analysis 15 + manual-notes 2 + web-refs 1 + §8 verified + dflowfm_mdu_input verified) | sediment·dredge·flow-wave·turbulence + M-D 1차 (engines·flow2d3d_dispatcher) + **M-D 2차 (dflowfm·dimr coupling BMI)** + M-C 2차 (manuals·FLOW v4.07.01) + **web-refs §8 verified — DIMRset_2026.02 (1067 commits / 300 files: UNST-9480/8857/9617 + circumcenter OBSOLETE + WAQ DELWAQ-1232 + PETSc 3.24 + C++20) + PR #900 UNST-9952 mdu time read fix OPEN (W22 promote, GitHub API 직접 fetch 2026-05-26)** + **`source-analysis/delft3d_dflowfm_mdu_input.md` verified (2026-05-28) — PR #900 diff 직접 fetch: readMDUFile `[Time]` block 18 파라미터 verbatim + UNST-9952 fix (line 1045↔1768 reorder) + m_flowtimes defaults lifecycle 도해** |
| [ROMS](models/ROMS/) | **WIP** (source-analysis 14 + manual-notes 3 + web-refs 1 + §8 verified + roms_4dvar §I+§J verified) | 4dvar·advection·baroclinic + M-D 1차 (driver·nonlinear) + **M-D 2차 (bulk_flux COARE)** + M-C 2차 (wiki-overview·getting-started·**cppdefs-options 32 cat**) + **web-refs §8 verified — PR #75 MULTI_SCALE_B 4D-Var OPEN feature/multiscale (62k+ adds / 93 files: 7개 multiscale_* core + convolution mono/multi split + get_state refactor 16h files), Weaver 2013 qj.1955 / 2016 qj.2664 / 2018 qj.3302 인용 정확화 (GitHub API 직접 fetch 2026-05-26)** + **`source-analysis/roms_4dvar.md §I` verified (2026-05-28) — multi_scale_B_v1.pdf full read: Matérn eq(1) + weighted sum eq(2) + implicit diffusion (1-∇κ∇)^M eq(4) + 7 multiscale_* algorithm flow + s4dvar.in 11 신규 파라미터 + CG+CI 솔버 + WC13 Fig 11 cost-J 비교 + Gregori 2008 negative-lobe 조건** + **`roms_4dvar.md §J` verified (2026-06-01) — PR #75 후속 5 commit (2026-05-27~31): J.1 4D-Var algorithms update (I4DVAR/R4DVAR/RBL4DVAR 동시 + NetCDF def_*.F 11 files +12 라인 균일) / J.2 B-correlation CDL template 신규 / J.3 tracer_metadata.F 신규 / **J.4 Dirac parameters 11 키워드 + Mlap 20→10 / NiterCG 50→20 default 절반 감소 (s4dvar.in verbatim diff)** / J.5 parallel bug fix** |

## textbook/ (교과서 통합)

| 노트 | source_id | 상태 |
|---|---|---|
| [tides-lubbad2009-overview.md](textbook/notes/tides-lubbad2009-overview.md) | lubbad2009-tides-slides | draft-unsourced |

원본 PDF 매니페스트: [textbook/sources.yml](textbook/sources.yml).
토픽별 분류: [textbook/INDEX.md](textbook/INDEX.md).

## examples/ (통합 실습)

| 예제 | 다루는 개념 | 사용 모델 | 상태 |
|---|---|---|---|
| (없음) | | | |

## experience/ (검증 통과 경험)

| 항목 | 통과 기준 | 상태 |
|---|---|---|
| [KHOA 15정점 1년 조위 UTide 검증](experience/khoa-multi-station-tide-validation-2026.md) | 3조건 통과 (15정점 독립 / KHOA 공식값 ±0.1% / fetch+analyze 스크립트 재현 가능) | **verified** |
| [KHOA 14년 기후 추세 — 한국 연안 SLR 2007-2025](experience/khoa-annual-climate-trend.md) | 3조건 통과 (13정점 19년 / KHOA Annual Report 직접 데이터 / 선형회귀 재현 가능) | **verified** |
| [KHOA 9년 SST 가온 추세 — 한국 연안 2017-2025](experience/khoa-sst-warming-trend.md) | 3조건 통과 (13정점 9년 / KHOA Annual Report 직접 데이터 / 회귀+SLR 정합성 cross-check) | **verified** (단기 caveat 명시) |
| [KHOA SST 5-source global cross-check](experience/khoa-sst-global-crosscheck.md) | 3조건 통과 (OISST v2.1 + HadISST + COBE-SST2 + NIFS KODC vs KHOA 5-way / 2017-2025 ~1.25 °C/dec 일치 + 1968-2022 0.27/0.19 + 1850-2025 0.064) | **verified** |
| [NIFS 다층 수온 trend 1968-2025](experience/nifs-vertical-sst-trends.md) | 3조건 통과 (NIFS 다층 surface +0.30 / 100m +0.13 / 200m -0.59 °C/dec + 동해 100m cooling + thermosteric ~10% SLR) | **verified** |
| [한국 연안 2024 광역 MHW — daily Hobday 13정점](experience/khoa-2024-mhw-extreme.md) | 3조건 통과 (13정점 daily OISST / 63 events 객관 집계 / KHOA 2024 §3.1 cross-check) | **verified** |
| [KHOA 49정점 16년 UTide 분석 (2010-2025) — 천해분조·nodal·폭풍해일·SLR·10태풍](experience/khoa-49-station-16yr-utide-2026.md) | 3조건 통과 (49정점 × 평균 14년 ZIP / KHOA 공시 HC + 45정점 nodal 9.7% + MSL 16yr +5.0 mm/yr & KHOA Annual Report 11yr ±0.1-1 mm/yr 정합 + 강화대교 SLR 가속 +7 mm/yr & 장항 감속 −3.7 발견 + 10 태풍 surge + 8 분조 cross-ref / utide_validation/*.py 재현) | **verified** |

## research/ (Hermes coastal-research 워크벤치)

| 영역 | 역할 | 상태 |
|---|---|---|
| [research/README.md](research/README.md) | inbox 정책, promote 규칙, frontmatter 표준 | active |
| [research/manifest.md](research/manifest.md) | Hermes 프로필 운영 기록, 수집 방법, 쿼리 세트, 한계 | active |
| [research/inbox/](research/inbox/) | X·arXiv·블로그·툴 신규 후보 | empty |
| [research/digests/](research/digests/) | 주간·월간 Hermes 요약 | empty |
| [research/watchlist/](research/watchlist/) | 모니터링 대상 계정·저자·기관·repo·키워드 | empty |

## 상태 표기

- `TBD` — 디렉토리만 존재, 내용 없음
- `WIP` — 작성 중 (citation_status가 draft-unsourced/source-needed 혼재 또는 일부 파일만 작성)
- `DRAFT` — 초안 완료, 사용자 verify 대기
- `STABLE` — 모든 frontmatter `citation_status: verified`
- `DEPRECATED` — 보존하되 새 작업 금지

상세 인용 상태는 각 파일 frontmatter의 `citation_status` 참조 ([CONVENTIONS.md §2](CONVENTIONS.md)).
