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
- **v2.4.0 Galibier 릴리스 검토 (2026-06-27)**: 공식 v2.4.0 "Galibier"(2026.01, 2026-06-15) — **바이너리(exe)+매뉴얼108p+testbed report 360p(Docker CPU/Windows 2판)만, 소스 미동봉**. 소스는 GitHub 태그 `v2.4.0_Galibier_release`(GPL-3.0). Docker `deltares/sfincs-cpu:sfincs-v2.4.0-Galibier-Release`. 산출: manual-notes v2.4.0-galibier-validation-testbed(77 케이스)·changelog-known-issues.
- **★ provenance 확정 (2026-06-27)**: `git clone --branch v2.4.0_Galibier_release` → **정확 sha `1f1d8286520a8709b2e513854dff18a3616583db`**(2026-06-15, "2026.01 galibier release #341"). 위키 감사 raw clone(`raw/source_code/sfincs/source/src/`)과 **`diff -rq` = 0 차이** → **위키 SFINCS 소스 감사 = v2.4.0 Galibier 소스로 확정**(SnapWave submodule main 2026-06-10 포함).
- **Windows 빌드 검증 (2026-06-27, 위키 외부)**: v2.4.0 소스를 VS2022 Professional + Intel oneAPI 2024.2(ifort)로 빌드 성공 → `sfincs.exe` v2.4.0 Galibier, OpenMP(libiomp5md) 런타임 정상. 빌드 노하우는 Claude 메모리(reference-sfincs-windows-build) 참조 — 위키 canonical 아님.

## 라이선스

- 소스: GNU GPL-3.0 (`source_code/sfincs/LICENSE`)
- 실행파일: Deltares Freeware (download.deltares.nl/sfincs)
