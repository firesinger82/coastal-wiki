---
title: "SWAN spectral file format (swanuse Appendix D) — BOUNDSPEC/SPECOUT/NESTOUT 파일구조: SWAN version·TIME·LOCATIONS/LONLAT·RFREQ/AFREQ·CDIR/NDIR·QUANT·FACTOR/ZERO/NODATA + 1D 3-quantity/2D 1-quantity verbatim"
topic: swan
canonical_source: external
external_source: "swanuse (User Manual, SWAN Cycle III version 41.51) Appendix D 'Spectrum files, input and output' (node50.md). spectral input(BOUNDSPEC) + output(SPECOUT/NESTOUT) 파일 표준 포맷 version 1. 1D nonstat spherical + 2D stat Cartesian 예제 + formal description."
citation_status: verified
verification_method: "models/SWAN/raw/manuals/website_markdown/online_doc/swanuse/node50.md 직접 read. 파일 키워드(SWAN/TIME/LOCATIONS/LONLAT/RFREQ/AFREQ/CDIR/NDIR/QUANT/FACTOR/ZERO/NODATA/LOCATION) 구조 + 1D 3-quantity/2D 1-quantity 규칙 + exception value + FACTOR scaling verbatim. source-analysis output-formats(dispatch)와 cross-check."
note_author: "Claude Opus 4.8 (1M context) raw markdown direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — 파일 포맷 키워드·구조 verbatim, BOUNDSPEC/SPECOUT/NESTOUT·nesting 정합"
verification_date: 2026-06-03
related:
  - models/SWAN/source-analysis/swan-output-formats.md
  - models/SWAN/manual-notes/swan-command-numerics-output-reference.md
  - models/SWAN/source-analysis/swan-nesting-io-implementation.md
  - models/SWAN/manual-notes/swan-output-variable-definitions.md
---

# SWAN spectral file format (swanuse Appendix D) — verified

> swanuse Appendix D (User Manual 41.51 / node50) 직접 read. SWAN **spectral 파일의 표준 포맷**(version 1) — `BOUNDSPEC`(입력) + `SPECOUT`/`NESTOUT`(출력) + nesting 이 공유. 본 노트 = **파일 구조/키워드**(format spec), [[swan-output-formats]] = output **dispatch 메커닉**(source-code), [[swan-output-variable-definitions]] = quantity **의미**. **first line 의 `SWAN`+version 으로 인식**.

## 1. 파일 식별 + 포함 정보

- **첫 줄 = 키워드 `SWAN` + version number**(현행 1) → SWAN/외부 프로그램이 인식.
- 포함: locations 좌표 / frequencies / directions(2D) / time(time-dependent) / spectral energy·variance density (+ 1D 는 average direction·directional spreading).

## 2. Free format 규약 ★

- **free format**(FORTRAN convention), 단 **모든 키워드·quantity 이름은 line 1번째 위치에서 시작**(Appendix B syntax).
- line 의 필수 입력 **이후 정보는 무시** → 사용자 주석으로 활용 가능(예: location 좌표 뒤 location 이름 — SWAN read 시 무시).
- `$` = comment line (예: `$ Data produced by SWAN version 41.51`).
- **source term 파일도 동일 포맷**(quantity 만 다름).

## 3. 파일 구조 (formal description verbatim 순서)

| 순서 | 내용 |
|---|---|
| 1 | `SWAN` + version number |
| 2 | **nonstat 만**: 키워드 `TIME` |
| 3 | **nonstat 만**: time coding option (ISO `=1` 권장). stationary 면 2-3 부재 |
| 4 | locations: `LOCATIONS`(Cartesian, x-y m problem coord) 또는 `LONLAT`(spherical, lon-lat) + 개수 + 각 location 좌표 |
| 5 | frequency (1D·2D 공통): `AFREQ`(절대) 또는 `RFREQ`(상대) + 개수 + Hz column(줄당 1개) |
| 6 | direction (**2D 만**): `NDIR`(nautical) 또는 `CDIR`(Cartesian) + 개수 + degree column |
| 7 | `QUANT` + quantity 개수 + 각 quantity {name / unit / **exception value**(undefined 시 기록값)} |
| 8 (VVV) | data table: {date-time(nonstat 만)} + location별 spectrum. nonstat 은 VVV 부터 반복 |

## 4. 1D vs 2D quantity 규칙 ★★

### 1D spectrum — 항상 **3 quantity**
순서: ① energy/variance density ② average direction(`CDIR` Cartesian / `NDIR` nautical) ③ directional spreading.
- spreading 키워드: SWAN **write** = `DSPRDEGR`(degrees); SWAN **read** = `DSPRD`/`DEGR`(option DEGREES) 또는 `DSPRP`/`POWER`(option POWER, BOUND SHAPE).
- 각 location: `LOCATION` + index(같은 줄). spectrum undefined(land 등) 시 `NODATA`(이후 숫자 없음).
- table = frequency 당 3열(density / CDIR·NDIR / DSPR).

### 2D spectrum — 항상 **1 quantity**
energy 또는 variance density. 이름: **`EnDens`**(true energy density) / **`VaDens`**(variance density).
- 각 location: 키워드 **`FACTOR`** + 곱할 factor + scaled density table.
  - **true density = table 값 × FACTOR** (예: factor `0.675611E-06`).
  - SWAN 은 compact 위해 **정수로 truncate** 기록(read 시 real 로 수용; 후처리 프로그램도 real 수용 권장).
  - `FACTOR` → spectrum 이 **identical 0** 이면 `ZERO`(숫자 없음), **undefined**(land 등 미계산) 이면 `NODATA`(숫자 없음)로 대체.

## 5. Exception value 예 (예제 verbatim)

| quantity | unit | exception |
|---|---|---|
| VaDens (1D) | m²/Hz | `-0.9900E+02` (-99) |
| VaDens (2D) | m²/Hz/degr | `-0.9900E+02` |
| CDIR | degr | `-0.9990E+03` (-999) |
| DSPRDEGR | degr | `-0.9000E+01` (-9) |

→ 1D 예제: 25 frequency(0.0418-1.0 Hz), 2 location(LONLAT), VaDens+CDIR+DSPRDEGR. 2D 예제: 25 freq × 12 dir(30-360°), VaDens m²/Hz/degr + FACTOR.

## 6. 연결

- [[swan-output-formats]] — SPEC1D/SPEC2D dispatch + 파일 naming·unit (source-code; 본 노트는 그 파일의 내부 포맷)
- [[swan-command-numerics-output-reference]] — `SPECOUT`/`NESTOUT` command 구문 + `BOUNDSPEC`(setup-grid ref)
- [[swan-nesting-io-implementation]] — NESTOUT→BOUNDNEST nesting 이 이 spectral 파일로 parent→child 전달
- [[swan-output-variable-definitions]] — EnDens/VaDens/CDIR·NDIR/DSPR quantity 의 적분 정의 (Appendix A)
- [[swan-documentation-stack]] §7 한계의 swanuse Appendix 잔여(D) 충족
