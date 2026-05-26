# INDEX

위키 전체 항목의 living map. 새 항목 추가 시 여기에도 등록.

## concepts/ (도메인 개념)

| 토픽 | 상태 | 비고 |
|---|---|---|
| [tides](concepts/tides/) | **DRAFT** (01-05 verified, 06 source-needed) | 조석 — 5/6 verified. 06은 `models/<model>/` 작성 후 verified 가능 |
| [waves](concepts/waves/) | **STABLE** (01-06 verified) | 파랑 — 6/6 verified. Holthuijsen 2007 + KHOA 284 용어 + SWAN library + MPT 74정점 |
| [sediment-transport](concepts/sediment-transport/) | **STABLE** (01-04·06 verified, 05 source-needed) | 표사이동 — 5/6 verified. Soulsby 1997 + KHOA 113 용어 + EFDC SED (Original/SEDZLJ) + Delft3D/XBeach/ROMS source-analysis 통합 |
| [currents](concepts/currents/) | **DRAFT** (01-05 verified, 06 source-needed) | 조류 — 5/6 verified (UTide 2D + 수치조류도 + KHOA 60+ 용어). 동해 수치조류도 미커버 명시 |
| [sst](concepts/sst/) | **STABLE** (01·02·03·04·05 verified, 06 source-needed) | 해수면 수온 — 5/6 verified. 01 정의, 02 heat budget, 03 회귀·MHW, 04 5 데이터셋 운영, 05 MHW 식별 실행 (13정점 ~180 events). experience/ 4건 연결 |
| [littoral-drift](concepts/littoral-drift/) | **DRAFT** (01·02 verified) | 연안표사 — 2/6 verified. 01 정의·CERC·Komar-Inman, 02 Holthuijsen §7.4.2-3 radiation stress + Bowen 1969 / Battjes 1974 longshore current 유도 |
| [storm-surge](concepts/storm-surge/) | **DRAFT** (01·02·03·04·07 verified, 05 partial Bolaven 2012, 06 미생성) | 폭풍해일 — 5/7 verified + 1/7 partial. 01 정의, 02 Pugh §6-7 + ADCIRC GWCE + **§3.4 hurricane PBL Sathia & Giometto 2026 (arxiv:2605.03933) verified — 두 scaling 식 u_*/β·u_*/√(βN) + 2.5% 오차 abstract 직접 fetch**, 03 separation·MK trend·return period (Pugh §6:1 §7:8 §8:3:2-3), 04 NWS modes·KHOA + **archive ~1년 verified**, 05 Maemi/Hinnamnor cross-ref + **Bolaven 2012 군산외해 ADCP 잔차 verified** ([[khoa-annual-2012-bolaven-surge]]), **07 ML emulators — PACT (Liu et al. 2026 arxiv:2605.09036) verified entry, abstract 직접 fetch**. ADCIRC source-analysis/storm-surge/ 7개 promote 완료 |

## models/ (모델별 객관 자료)

| 모델 | 상태 | 비고 |
|---|---|---|
| [EFDC](models/EFDC/) | **WIP** (source-analysis 18 + manual-notes 5 verified) | 사용자 주력 — SedTran-Original/SEDZLJ + hydro core + boundary + wetdry. manual-notes: overview + user r850 + theory v12 (TOC) + sediment 2003 + **theory v12 Ch 2 hydrodynamics deep (식 2.1-2.150 + Mellor-Yamada 4 옵션 + 5 wind drag + SIG/SGZ)** |
| [SWAN](models/SWAN/) | **STABLE** (README + action-balance + wink-pattern + source-analysis 21 노트 verified) | 천해 풍파 spectral · Holthuijsen 공동개발 · 모든 source-term · scheme · 추가 promote 다수 |
| [ADCIRC](models/ADCIRC/) | **WIP** (source-analysis 41 + local-workflow 11 + manual-notes 21 verified + web-refs 1) | NWS modes + GAHM/AHM + tide + storm-surge. manual-notes 21 verified (M-B audit), local-workflow 11 → source-analysis/local-workflow/ 이관 (2026-05-24) |
| [XBeach](models/XBeach/) | **WIP** (source-analysis 16 + manual-notes 3 verified + web-refs 1) | morphology · avalanching · bed_friction · wave_boundary. manual-notes 3 verified 2026-05-24 (xbeach.readthedocs.io examples audit) |
| [Delft3D](models/Delft3D/) | **WIP** (source-analysis 14 + manual-notes 2 + web-refs 1 + §8 verified) | sediment·dredge·flow-wave·turbulence + M-D 1차 (engines·flow2d3d_dispatcher) + **M-D 2차 (dflowfm·dimr coupling BMI)** + M-C 2차 (manuals·FLOW v4.07.01) + **web-refs §8 verified — DIMRset_2026.02 (1067 commits / 300 files: UNST-9480/8857/9617 + circumcenter OBSOLETE + WAQ DELWAQ-1232 + PETSc 3.24 + C++20) + PR #900 UNST-9952 mdu time read fix OPEN (W22 promote, GitHub API 직접 fetch 2026-05-26)** |
| [ROMS](models/ROMS/) | **WIP** (source-analysis 14 + manual-notes 3 + web-refs 1 + W22 §8 source-needed) | 4dvar·advection·baroclinic + M-D 1차 (driver·nonlinear) + **M-D 2차 (bulk_flux COARE)** + M-C 2차 (wiki-overview·getting-started·**cppdefs-options 32 cat**) + **web-refs §8 Recent updates — PR #75 MULTI_SCALE_B 4D-Var source-needed (W22 promote, Weaver 2013/2016/2018)** |

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
