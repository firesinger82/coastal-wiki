# ROMS — 원자료 판독 사실표 (2026-10-02)

원자료: `models/ROMS/raw/` 파일 11,681개. 판독 기록: `_staging/total-read/records/`·`model-audit/`(07-19~09). 파일별 목록: [ROMS-files.tsv](ROMS-files.tsv).

"노트언급" = `models/ROMS/` 노트(raw 제외)에 그 파일명이 나옴(이름 일치일 뿐 분석 증거는 아님, 같은 이름 파일은 함께 셈). "LLM판독" = Claude·Codex·grok 이 내용을 읽고 남긴 파일별 기록(질 미검증). "결함감사만" = 파일별 판독 기록은 없고 Codex 결함 감사(`codex-defect-reports/`, 08-29)에서 코어 파일로 다뤄짐. "실패" = 기계 sweep 이 못 읽음(대부분 바이너리). 파서 구조 추출(07-24 적발분)은 판독으로 세지 않음.


## 파일 종류별

| 종류 | 파일 | LLM판독 | 부분판독 | 결함감사만 | 실패 | 기록없음 | 노트언급 |
|---|--:|--:|--:|--:|--:|--:|--:|
| 코드 | 6,583 | 0 | 0 | 41 | 10 | 6,532 | 618 |
| 문서 | 1,307 | 1,221 | 0 | 0 | 10 | 76 | 104 |
| 웹문서 | 1,162 | 1,162 | 0 | 0 | 0 | 0 | 0 |
| 기타(설정·입력·빌드) | 2,382 | 0 | 0 | 0 | 22 | 2,360 | 64 |
| 바이너리 | 247 | 0 | 0 | 0 | 33 | 214 | 2 |

## 폴더별 (모델 자체 / 외부 라이브러리 / 테스트·예제 구분은 사용자 확정 대상)

| 폴더 | 파일 | LLM판독 | 부분판독 | 결함감사만 | 실패 | 기록없음 | 노트언급 |
|---|--:|--:|--:|--:|--:|--:|--:|
| `source_code/WRF/var` | 2,209 | 0 | 0 | 0 | 3 | 2,206 | 0 |
| `source_code/roms/ROMS` | 1,040 | 1 | 0 | 41 | 0 | 998 | 427 |
| `source_code/WRF/chem` | 1,029 | 0 | 0 | 0 | 0 | 1,029 | 0 |
| `manuals/wiki` | 964 | 642 | 0 | 0 | 0 | 322 | 34 |
| `manuals/website` | 856 | 838 | 0 | 0 | 0 | 18 | 0 |
| `manuals/website_markdown` | 838 | 838 | 0 | 0 | 0 | 0 | 11 |
| `source_code/roms_libs/ARPACK` | 674 | 1 | 0 | 0 | 6 | 667 | 1 |
| `source_code/WRF/external` | 545 | 1 | 0 | 0 | 2 | 542 | 0 |
| `source_code/roms_test/WC13` | 311 | 18 | 0 | 0 | 11 | 282 | 71 |
| `source_code/WRF/phys` | 231 | 0 | 0 | 0 | 0 | 231 | 0 |
| `source_code/roms-jedi/test` | 221 | 1 | 0 | 0 | 0 | 220 | 3 |
| `source_code/roms_matlab/seagrid` | 202 | 0 | 0 | 0 | 6 | 196 | 0 |
| `source_code/roms_test/IRENE` | 170 | 7 | 0 | 0 | 0 | 163 | 5 |
| `source_code/roms_matlab/colormaps` | 158 | 0 | 0 | 0 | 0 | 158 | 0 |
| `source_code/roms-jedi/src` | 137 | 0 | 0 | 0 | 0 | 137 | 24 |
| `source_code/WRF/hydro` | 132 | 3 | 0 | 0 | 0 | 129 | 0 |
| `source_code/WRF/test` | 103 | 0 | 0 | 0 | 6 | 97 | 0 |
| `source_code/roms_matlab/m_map` | 97 | 2 | 0 | 0 | 11 | 84 | 0 |
| `source_code/roms/User` | 85 | 0 | 0 | 0 | 0 | 85 | 46 |
| `source_code/WRF/tools` | 82 | 0 | 0 | 0 | 4 | 78 | 0 |
| `source_code/WRF/run` | 81 | 0 | 0 | 0 | 18 | 63 | 0 |
| `source_code/WRF/frame` | 72 | 0 | 0 | 0 | 0 | 72 | 0 |
| `source_code/roms_matlab/utility` | 70 | 0 | 0 | 0 | 0 | 70 | 0 |
| `source_code/WRF/wrftladj` | 64 | 0 | 0 | 0 | 0 | 64 | 0 |
| `source_code/WRF/share` | 61 | 0 | 0 | 0 | 0 | 61 | 0 |
| `source_code/roms_test/USEC` | 52 | 1 | 0 | 0 | 0 | 51 | 2 |
| `source_code/roms_test/double_gyre` | 51 | 0 | 0 | 0 | 0 | 51 | 12 |
| `source_code/roms_test/lake_jersey` | 49 | 0 | 0 | 0 | 0 | 49 | 12 |
| `source_code/roms_matlab/4dvar` | 45 | 0 | 0 | 0 | 0 | 45 | 0 |
| `source_code/roms/Compilers` | 44 | 0 | 0 | 0 | 0 | 44 | 0 |
| `source_code/roms_test/lake_decimate` | 42 | 2 | 0 | 0 | 0 | 40 | 24 |
| `source_code/WRF/dyn_em` | 40 | 0 | 0 | 0 | 0 | 40 | 0 |
| `source_code/roms_matlab/grid` | 40 | 0 | 0 | 0 | 0 | 40 | 0 |
| `source_code/roms_matlab/seawater` | 40 | 0 | 0 | 0 | 0 | 40 | 0 |
| `source_code/WRF/Registry` | 39 | 0 | 0 | 0 | 0 | 39 | 0 |
| `source_code/roms_eccofs/Data` | 39 | 0 | 0 | 0 | 0 | 39 | 1 |
| `source_code/roms_test/LAKE_ERIE` | 34 | 0 | 0 | 0 | 0 | 34 | 8 |
| `source_code/roms_test/dogbone` | 31 | 0 | 0 | 0 | 0 | 31 | 8 |
| `source_code/roms/Master` | 30 | 0 | 0 | 0 | 0 | 30 | 12 |
| `source_code/roms_matlab/netcdf` | 29 | 0 | 0 | 0 | 0 | 29 | 0 |
| `source_code/roms/ESM` | 27 | 1 | 0 | 0 | 0 | 26 | 0 |
| `source_code/roms_test/DAMEE_4` | 27 | 0 | 0 | 0 | 0 | 27 | 2 |
| `source_code/roms/Data` | 24 | 1 | 0 | 0 | 0 | 23 | 3 |
| `source_code/roms_test/bio_toy` | 24 | 0 | 0 | 0 | 0 | 24 | 1 |
| `source_code/roms_test/upwelling` | 23 | 0 | 0 | 0 | 0 | 23 | 8 |
| `source_code/roms_test/lake_ice` | 21 | 1 | 0 | 0 | 0 | 20 | 9 |
| `source_code/roms-jedi/tools` | 20 | 2 | 0 | 0 | 0 | 18 | 0 |
| `source_code/roms_matlab/landmask` | 20 | 0 | 0 | 0 | 0 | 20 | 0 |
| `source_code/WRF/doc` | 19 | 1 | 0 | 0 | 0 | 18 | 0 |
| `source_code/roms_matlab/mex` | 19 | 0 | 0 | 0 | 1 | 18 | 0 |
| `source_code/roms_matlab/t_tide` | 18 | 0 | 0 | 0 | 5 | 13 | 0 |
| `source_code/roms_test/channel` | 18 | 0 | 0 | 0 | 1 | 17 | 2 |
| `source_code/roms_test/soliton` | 17 | 0 | 0 | 0 | 0 | 17 | 5 |
| `source_code/roms_matlab/initial` | 15 | 0 | 0 | 0 | 0 | 15 | 0 |
| `source_code/roms_test/test_head` | 15 | 0 | 0 | 0 | 0 | 15 | 3 |
| `source_code/WRF/arch` | 14 | 0 | 0 | 0 | 0 | 14 | 0 |
| `source_code/roms_test/DuckNC` | 14 | 1 | 0 | 0 | 0 | 13 | 3 |
| `source_code/roms_test/marsh_test` | 14 | 1 | 0 | 0 | 0 | 13 | 4 |
| `source_code/roms_test/riverplume` | 14 | 0 | 0 | 0 | 0 | 14 | 1 |
| `source_code/WRF/main` | 13 | 0 | 0 | 0 | 0 | 13 | 0 |
| `source_code/roms_test/inlet_test` | 12 | 0 | 0 | 0 | 0 | 12 | 1 |
| `source_code/roms_test/vegetation_test` | 12 | 1 | 0 | 0 | 0 | 11 | 2 |
| `source_code/roms_test/shoreface` | 11 | 1 | 0 | 0 | 0 | 10 | 2 |
| `source_code/roms_eccofs/RBL4DVAR_mixres` | 10 | 1 | 0 | 0 | 0 | 9 | 2 |
| `source_code/roms_test/flt_test` | 10 | 0 | 0 | 0 | 0 | 10 | 1 |
| `source_code/WRF` | 9 | 1 | 0 | 0 | 0 | 8 | 1 |
| `source_code/WRF/inc` | 9 | 0 | 0 | 0 | 0 | 9 | 0 |
| `source_code/roms_matlab/boundary` | 9 | 0 | 0 | 0 | 0 | 9 | 0 |
| `source_code/roms_matlab/tidal_ellipse` | 8 | 0 | 0 | 0 | 1 | 7 | 7 |
| `source_code/roms_test/benchmark` | 8 | 0 | 0 | 0 | 0 | 8 | 1 |
| `source_code/roms-jedi/cmake` | 7 | 0 | 0 | 0 | 0 | 7 | 0 |
| `source_code/roms_matlab/bathymetry` | 7 | 0 | 0 | 0 | 0 | 7 | 0 |
| `source_code/roms_matlab/coastlines` | 7 | 0 | 0 | 0 | 0 | 7 | 0 |
| `source_code/roms_matlab/forcing` | 7 | 0 | 0 | 0 | 0 | 7 | 0 |
| `source_code/roms_test/bl_test` | 7 | 0 | 0 | 0 | 0 | 7 | 1 |
| `source_code/roms_test/canyon` | 7 | 0 | 0 | 0 | 0 | 7 | 1 |
| `source_code/roms_test/estuary_test` | 7 | 0 | 0 | 0 | 0 | 7 | 1 |
| `source_code/roms_test/lmd_test` | 7 | 0 | 0 | 0 | 0 | 7 | 1 |
| `source_code/roms_test/sed_test` | 7 | 0 | 0 | 0 | 0 | 7 | 1 |
| `source_code/roms_test/test_chan` | 7 | 0 | 0 | 0 | 0 | 7 | 2 |
| `source_code/roms_eccofs/Forward` | 6 | 1 | 0 | 0 | 0 | 5 | 1 |
| `source_code/roms_matlab/ioda` | 6 | 0 | 0 | 0 | 0 | 6 | 0 |
| `source_code/roms_test/basin` | 6 | 0 | 0 | 0 | 0 | 6 | 1 |
| `source_code/roms_test/grav_adj` | 6 | 0 | 0 | 0 | 0 | 6 | 1 |
| `source_code/roms_test/kelvin` | 6 | 0 | 0 | 0 | 0 | 6 | 1 |
| `source_code/roms_test/lab_canyon` | 6 | 0 | 0 | 0 | 0 | 6 | 1 |
| `source_code/roms_test/seamount` | 6 | 0 | 0 | 0 | 0 | 6 | 1 |
| `source_code/roms_test/weddell` | 6 | 0 | 0 | 0 | 0 | 6 | 1 |
| `source_code/roms_test/windbasin` | 6 | 0 | 0 | 0 | 0 | 6 | 2 |
| `source_code/roms_matlab/coupling` | 5 | 0 | 0 | 0 | 0 | 5 | 0 |
| `source_code/roms-jedi` | 4 | 0 | 0 | 0 | 0 | 4 | 1 |
| `source_code/roms` | 4 | 1 | 0 | 0 | 0 | 3 | 2 |
| `source_code/WRF/.github` | 3 | 1 | 0 | 0 | 0 | 2 | 0 |
| `source_code/roms-jedi/.github` | 3 | 0 | 0 | 0 | 0 | 3 | 0 |
| `source_code/roms-jedi/docs` | 3 | 3 | 0 | 0 | 0 | 0 | 1 |
| `source_code/roms/docs` | 3 | 3 | 0 | 0 | 0 | 0 | 1 |
| `source_code/roms_eccofs/docs` | 3 | 3 | 0 | 0 | 0 | 0 | 1 |
| `source_code/roms_matlab` | 3 | 1 | 0 | 0 | 0 | 2 | 1 |
| `source_code/roms-jedi/bundle` | 2 | 0 | 0 | 0 | 0 | 2 | 1 |
| `source_code/roms/.git_filters` | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| `source_code/roms_matlab/bin` | 2 | 0 | 0 | 0 | 0 | 2 | 1 |
| `source_code/roms_test/External` | 2 | 0 | 0 | 0 | 0 | 2 | 1 |
| `source_code/roms_test/bin` | 2 | 0 | 0 | 0 | 0 | 2 | 1 |
| `manuals/refs` | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| `source_code/roms_eccofs` | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| `source_code/roms_libs` | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| `source_code/roms_test` | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| `source_code/roms_test/docs` | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
