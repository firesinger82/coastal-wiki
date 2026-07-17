---
title: "ShorelineS 소스 아키텍처 맵 — 5-phase 메인 루프·transport 공식 선택·136 함수 분모"
model: ShorelineS
component: functions (top-level)
canonical_source: self
citation_status: verified
verification_method: "sha 7bf4481ab clone(raw/source_code/shorelines/) 직접 read — ShorelineS.m(293줄) 초기화 체인·PHASE 주석·호출 라인 verbatim, prepare_transport.m trform 주석, functions/ 파일명 전수 목록(ls 136 실측). 각 모듈 내부 로직은 미검수(후속 deep SA 대상 — 본 노트는 골격·분모 확정용)."
note_author: "Claude Fable 5"
note_date: 2026-07-17
related:
  - models/ShorelineS/README.md
  - models/ShorelineS/web-refs/shorelines-official-resources.md
  - models/AUDIT-LEDGER.md
---

# ShorelineS 소스 아키텍처 맵

> `functions/` 136 .m 의 골격. 경로: `models/ShorelineS/raw/source_code/shorelines/functions/`. 진입점 = `ShorelineS.m`(293줄) — `[S,O]=ShorelineS(S0)` 단일 호출, 입력 = 케이스 구조체 S(스크립트가 채움), 출력 = 결과 구조체 O.

## 1. 초기화 체인 (`ShorelineS.m:56-76`)

```
initialize_defaultvalues → initialize_randomgenerator → initialize_time
→ prepare_coastline → prepare_dunes → prepare_climatechange
→ prepare_waveconditions → prepare_runupconditions → prepare_windconditions → prepare_tide
→ prepare_structures → prepare_nourishment → prepare_fnourishment
→ prepare_transport → prepare_mudcoast → prepare_spit → prepare_channel → prepare_delta
→ initialize_bathyupdate → initialize_plot → initialize_output
```

각 prepare_* 가 대문자 상태 구조체(COAST·DUNE·CC·WAVE·RUNUP·WIND·TIDE·STRUC·NOUR·FNOUR·TRANSP·MUD·SPIT·CHANNEL·DELTA·BATHY)를 생성 — 이후 메인 루프가 이 구조체들을 갱신.

## 2. 메인 시간 루프 — 5 phase (`ShorelineS.m:81-293`)

`while TIME.tnow<TIME.tend`(:81) 안에서:

| Phase | 주석 라인 | 내용 (호출 실측) |
|---|---|---|
| **0 GRID** | :92 | `prepare_grid_groyne`(:94) — groyne 로 분할된 해안선 grid 재구성 |
| **1 TRANSPORT** | :97 | 섹션 루프 `for i_mc=1:COAST.n_mc`(:101): `make_sgrid_mc`(regrid, :104) → `interpolate_props`(:107) → `introduce_climatechange`(:110) → (파랑·transport 계산) → 적응 timestep `get_timestep`(:188)·`get_coastlineupdate_timestep`(:200) |
| **2 COASTLINE CHANGE** | :209 | `coastline_change`(:226 — COAST·WAVE·TRANSP·DUNE·MUD·STRUC·GROYNE·NOUR·FNOUR·CC 전부 입력) — 표사수지 경사 → 해안선 이동 |
| **3 OTHER PROCESSES** | :234 | 스핏·월류·수로·삼각주·병합/분리 등 |
| **4 PLOT/STORE** | :263 | `update_shoreline`(:276)·출력 저장 |

- 시간 전진: `get_nexttimestep`(:282). 적응 dt 기록 `TIME.adt_record`(:197).
- **다중 해안선(멀티폴리곤)**: `_mc` 접미사 함수군(`make_sgrid_mc`·`merge_coastlines_mc`·`find_shadows_mc`·`find_overwash_mc`) — 섬·석호 등 n_mc 개 섹션을 병렬 처리, 병합/분리 허용.

## 3. Transport 축 (C티어 — deep SA 1순위)

- **공식 선택**: `S.trform` = `'CERC' | 'KAMP' | 'MILH' | 'VR14'` (`prepare_transport.m:9,104`). CERC 계수 `S.b`(:105), VR14 swell 백분율 `S.pswell`(:120).
- 전용 파일 9: `transport.m`(본체)·`transport_boundary_condition`·`transport_bypass`(groyne 우회)·`transport_groynesubmerged`·`transport_revetment`·`transport_shadow_treat`(차폐)·`transport_soulsbyvanrijn`·`transport_mud`(점착성 해안)·`transport_tidewave`.
- 상한 각도/최대 transport 각: `get_Sphimax.m`.

## 4. 파랑 축 (C티어)

`wave_angles`·`wave_breakingheight`·`wave_cur_1D`·`wave_diffraction`+`wave_diffraction_coeff`(구조물 배후 회절)·`wave_refraction`·`wave_shoalref`(천수+굴절)·`wave_transmission`(투과성 구조물) + 외부 파랑장 보간 `get_interpolated_wavefield_*` 3종.

## 5. 프로세스 모듈 축 (C티어)

| 모듈 | 파일 |
|---|---|
| 사구 | `dune_erosion`·`dune_flux`·`dune_growth`·`extract_berm` |
| 스핏/월류 | `prepare_spit`·`find_overwash_mc` |
| 양빈 | `get_nourishments`·shoreface 양빈 `get_fnourishment{,_diffusion,_fraction,_rate}` |
| 조석 | `tide_1d_ana_anycomp`·`interpolate_tide`·`make_tide/` |
| 하천·수로·삼각주 | `get_riverdischarges`·`move_channel`·`prepare_channel`·`prepare_delta` |
| 기후변화(SLR) | `introduce_climatechange`·`prepare_climatechange` |
| 해안선 위상 | `merge_coastlines{,_mc}`·`insert_section`·`select_multi_polygon`·`snap_coastline_to_data`·`cleanup_nans` |

## 6. S티어 (지원 — 검수 권장)

- 입출력·유틸: `readkeys`·`get_inputfiledata`·`collect_variables`·`struct2log`·`save_shorelines{,_netcdf}`·`nc_readfromgroup`·보간/기하 `get_*` 다수(`get_disper` 분산관계 포함)·`interpNANs{,DIR}`.
- 시각화: `plot_*` 7종·`make_video`. Octave 호환: `isoctave`.
- 진입 래퍼: `runShorelineS.m`.

## 7. 분모·티어 판정 (AUDIT-LEDGER §14 근거)

- **functions/ .m = 136**(ls 실측). T티어(vendored 외부 라이브러리) = **0** — 전부 자체 MATLAB 구현(파일명 전수 검토, 외부 패키지 디렉토리 부재).
- C티어(물리·수치 코어) 후보 ≈ transport 9 + wave 9+3 + coastline/update 3 + phase 모듈군(§5) ≈ **40±** / 나머지 S티어.
- 후속 deep SA 우선순위: ①`transport.m`+공식 4종 계수 실측(케이스1 CERC 이론과 대조 — [theory-ch14](../../../textbook/notes/theory-ch14-coastal-morphodynamics.md)) ②`coastline_change.m`(one-line 이산화·안정성) ③`wave_diffraction`(Roelvink 2020 §회절과 대조) ④스핏/월류 메커닉 ⑤적응 timestep 규칙(`get_timestep`).
