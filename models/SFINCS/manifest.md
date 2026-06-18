# SFINCS Acquisition Manifest

**Acquired**: 2026-06-18

## source_code/

| Repo | Source | Clone | Size |
|------|--------|-------|------|
| sfincs | <https://github.com/Deltares/SFINCS> (Deltares, GPL-3.0) | `git clone --depth 1` (main HEAD, 2026-06-18) | ~105M (raw, gitignored) |

- 182 Fortran (.f90/.F90); 코어 36 = `source/src/*.f90` + `source/src/snapwave/` 9.
- `source/third_party_open/netcdf` = netCDF-fortran 4.6.1 (vendored, ⬛ T-tier).
- **재현**: `git clone --depth 1 https://github.com/Deltares/SFINCS.git` → `models/SFINCS/raw/source_code/sfincs/`. depth-1 이라 exact commit sha 미기록(main HEAD 2026-06-18). 정확 버전 필요 시 full clone 후 `git log -1`.
- raw/ 는 `.gitignore` 제외(vendor source tree).

## docs/

- readthedocs: <https://sfincs.readthedocs.io/en/latest/> (manual-notes 후속 추출 대상)
- 소스 내 `docs/` (readthedocs RST 소스) 동봉.

## 라이선스

- 소스: GNU GPL-3.0 (`source_code/sfincs/LICENSE`)
- 실행파일: Deltares Freeware (download.deltares.nl/sfincs)
