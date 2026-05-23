# Local JMA-MSM GUI Contract

Date: 2026-04-13

Purpose:
- record what the running `JMA_MSM_Converter.exe` GUI explicitly tells us
- stabilize the raw-input contract for the local `JMA-MSM -> NWS=13` branch

## Window Evidence

Observed window title:
- `JMA MSM 다운로드 & fort.22.nc 변환기`

Observed tabs:
- `1. 다운로드`
- `2. 변환`
- `한번에 실행`

Interpretation:
- this tool combines acquisition and conversion in one interface
- the local workflow is not only "take existing raw files and convert them"

## Download Contract

Observed fields on the download tab:
- start date
- end date
- save folder

Interpretation:
- the user specifies a date range directly
- the raw download directory is chosen at runtime
- the local raw-input location is not necessarily fixed in the repository tree

Observed fields on the conversion tab:
- input NC file selector
- simulation start time
- output file path

Observed fields on the integrated run tab:
- `전체 실행 (다운로드 -> 변환)`
- quick start and end date fields

Interpretation:
- the GUI supports both staged and one-shot workflows
- the conversion step explicitly depends on an NC input file and a simulation start time

## Upstream Source Evidence

Observed displayed source:
- `RISH Kyoto University`
- `http://database.rish.kyoto-u.ac.jp/arch/jmadata/data/gpv/netcdf/MSM-S/`

Interpretation:
- the converter is wired to the MSM-S NetCDF archive at RISH Kyoto
- the upstream source itself is now known and no longer a gap

## Variable And Resolution Evidence

Observed displayed variables:
- `u`
- `v`
- `psea`
- `temp`
- `rh`

Observed displayed temporal resolution:
- `1시간`

Interpretation:
- the downloader works with hourly MSM-S NetCDF products
- the converter likely has access to more variables than the minimum ADCIRC forcing set
- only a subset is later promoted into `NWS=13`, based on the notebook evidence:
  - `psea -> PSFC`
  - `u -> U10`
  - `v -> V10`

## What This Closes

This note closes these uncertainties:
- the upstream archive location
- the fact that raw download is part of the GUI workflow
- the fact that start and end dates are primary user inputs
- the fact that the source products are hourly NetCDF files

## Executed Run Evidence

Observed run result from `2026-04-13`:
- save folder used: `E:\AI_ENV`
- created raw directory: `E:\AI_ENV\2003`
- created raw files:
  - `E:\AI_ENV\2003\0901.nc`
  - `E:\AI_ENV\2003\0902.nc`
  - `E:\AI_ENV\2003\0903.nc`
- created converted file:
  - `E:\AI_ENV\fort.22.nc`

Interpretation:
- the downloader creates a year directory under the chosen save folder
- the observed raw filenames use an `MMDD.nc` convention
- the converter can write `fort.22.nc` directly into the chosen working directory

## What Still Remains Open

- whether the observed `MMDD.nc` naming rule is universal across years and longer runs
- whether the save folder receives raw files, merged files, and `fort.22.nc` together or in separate stages for all modes
- whether the `2. 변환 한번에 실행` tab uses the same folder layout as the notebook workflow
