---
title: "Delft3D dflowfm MDU 입력 — readMDUFile 함수 + [Time] block + PR #900 fix"
topic: delft3d-dflowfm-mdu-input
canonical_source: self
verification_method: "GitHub PR #900 (Deltares/Delft3D) diff 직접 fetch 2026-05-28 (`gh pr diff 900 -R Deltares/Delft3D`) — `src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/dflowfm_data/unstruc_model.f90` +113 -112 hunk verbatim 인용. PR body verbatim 인용 (UNST-9952). [Time] block 파라미터 18개 모두 diff 의 prop_get 호출 그대로 인용. Bug mechanism 은 PR description (Moore field setup + m_flowtimes defaults) 명시 그대로."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-28
citation_status: verified
verification_by: "Claude Opus 4.7 (1M context) — PR #900 diff + body GitHub API 직접 fetch + Fortran source verbatim"
verification_date: 2026-05-28
related:
  - models/Delft3D/source-analysis/delft3d_dflowfm_overview.md
  - models/Delft3D/web-refs/delft3d-official-resources.md
---

# Delft3D dflowfm — MDU input 파싱 (`readMDUFile`) + UNST-9952 fix

> 출처: PR [#900](https://github.com/Deltares/Delft3D/pull/900) diff 직접 fetch (`gh pr diff 900 -R Deltares/Delft3D`). 대상 파일 `src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/dflowfm_data/unstruc_model.f90` (+113 -112 hunk verbatim).

## 1. `readMDUFile` 함수 개요

`subroutine readMDUFile(filename, istat)` 가 dflowfm 의 입력 파일 **MDU** (Model Definition Unstructured) 를 파싱. INI-style block 구조이며 각 block 은 `prop_get(md_ptr, '<section>', '<key>', <var>)` 호출로 읽힌다.

주요 block (verified 가능한 항목만):

| Block | 역할 |
|---|---|
| `[geometry]` | mesh / structure / bathymetry 설정 (line ~1045 부근 ChangeStructureDimensions 까지) |
| `[Time]` | reference date, time step, simulation window — **PR #900 의 핵심** (아래 §2-3) |
| `[hydrology]` | InterceptionModel 등 |
| 그 외 다수 | (본 노트 scope 외) |

## 2. `[Time]` block 파라미터 (PR #900 diff +block verbatim)

PR #900 의 fix 가 `[Time]` block 을 옮긴 위치에서 read 되는 파라미터들. 모든 호출은 `prop_get(md_ptr, 'Time', '<key>', <var>[, success])` 형식:

| MDU 키 | Fortran 변수 | 단위·default·제약 |
|---|---|---|
| `refDate` | `refdat` → `irefdate` → `refdate_mjd` | YYYYMMDD → Modified Julian Date 변환 (`ymd2modified_jul`). 실패 시 LEVEL_ERROR |
| `tZone` | `Tzone` | (시간 offset) |
| `tUnit` | `md_tunit` | `'D'`→86400 / `'H'`→3600 / `'M'`→60 / default 1 (sec) → `tfac` |
| `tStart` | `tstart_user` | `× tfac` 적용 후 sec |
| `tStop` | `tstop_user` | `× tfac` 적용 후 sec |
| `dtUser` | `dt_user` | 미지정 (`≤0`) 시 default 300.0 sec + `dt_max`=60 + `autotimestep`=`AUTO_TIMESTEP_2D_OUT` |
| `dtNodal` | `dt_nodal` | nodal correction 적용 주기 |
| `dtMax` | `dt_max` | `> dt_user` 시 dt_user 로 clamp + msgbuf 경고 |
| `autoTimeStep` | `autotimestep` | optional, success flag |
| `autoTimeStepDiff` | `jadum` | ≠0 시 LEVEL_ERROR ("not supported") |
| `autoTimeStepVisc` | `ja_timestep_auto_visc` | `1234` 면 hidden feature 활성 (1로 set), 그 외 ≠0 은 LEVEL_ERROR |
| `autoTimeStepNoStruct` | `ja_timestep_nostruct` | optional |
| `autoTimeStepNoQout` | `ja_timestep_noqout` | optional |
| `dtFacMax` | `dt_fac_max` | time step 변화 ratio cap |
| `dtInit` | `dt_init` | 초기 time step |
| `timeStepAnalysis` | `ja_time_step_analysis` | (분석 모드) |
| `startDateTime` | `start_date_time` | string `YYYYMMDDHHMMSS` 류 — `datetimestring_to_seconds(start_date_time, refdat, tim)` 후 `Tstart_user = tim` overwrite (`tStart` 보다 우선) |
| `tStartTlfsmo` | `tstart_tlfsmo_user` | 미지정 시 `tstart_user` 로 fallback. 지정 시 `× tfac` |
| `startDateTimeTlfsmo` | `start_date_time_tlfsmo` | string → `tstart_tlfsmo_user` overwrite. 검증: `tstart_tlfsmo_user ≤ tstart_user` 필수 (위반 시 reset + LEVEL_WARN) |
| `stopDateTime` | `stop_date_time` | string → `Tstop_user` overwrite |
| `updateRoughnessInterval` | `dt_update_roughness` | `< dt_user` 시 LEVEL_ERROR (대원칙: ≥ `dt_max` 이지만 `dt_user` 로 강제) |

→ 18개 파라미터 read 후 `m_flowtimes` 모듈 변수 (`tstart_user`, `tstop_user`, `dt_user`, `dt_max`, ...) 가 user 값으로 갱신됨.

## 3. UNST-9952 bug + PR #900 fix

### 3.1 Bug mechanism (PR description verbatim)

> "Moved the [time] read block in readMDU up in the routine, behind the geometry block. Some output fields use tstart_user and tstop_user, which was modified by the [time] read after fields were already set based on the m_flowtimes defaults."

→ 이전 (PR 전) read 순서:

```
1. [geometry] read (line ~1045 까지)
2. ... (다른 섹션들 — output fields 가 m_flowtimes defaults 의 tstart_user/tstop_user 로 setup) ...
3. [hydrology] InterceptionModel read (line ~1768)
4. [Time] read (line 1768~1884) ← 이때 tstart_user/tstop_user overwrite
5. (나머지 routine)
```

문제: 2번 단계에서 output field 가 **stale m_flowtimes defaults** 의 `tstart_user`/`tstop_user` 로 setup → 4번에서 user 값으로 overwrite 되지만 이미 output field 는 stale 값에 묶여 있어 **output time inconsistency**.

### 3.2 Fix (PR #900)

`[Time]` block read 위치를 `[geometry]` 의 `ChangeStructureDimensions` (line 1045) 직후로 이동. 새 순서:

```
1. [geometry] read (~ line 1045)
2. [Time] read (line 1046~1163, 119 줄) ← user 값으로 tstart_user/tstop_user/... 갱신
3. ... (output field setup — 이제 최신 user 값 사용) ...
4. [hydrology] InterceptionModel read
5. (나머지 routine)
```

diff hunks (verbatim):

- `+@@ -1045,6 +1045,119 @@` — line 1045 이후에 119 줄 (Time block) 추가
- `-@@ -1768,118 +1881,6 @@` — line 1768 이후의 116 줄 (옛 Time block) 제거

순 효과: **content 자체는 그대로** (Time block parameter 호출은 동일), 단지 **read 시점만 앞당겨짐**.

### 3.3 m_flowtimes defaults lifecycle (도해)

```
[unstruc_model.f90 readMDUFile 진입]
    │
    ▼
[m_flowtimes 모듈 default 적재 — tstart_user, tstop_user 등 default 값]
    │
    ▼
[geometry] read ────► mesh / structure 설정
    │
    │  ◄ PR #900: 여기에 [Time] read 삽입
    ▼
[Time] read ─────► m_flowtimes 모듈 변수 user 값으로 overwrite
    │              (tstart_user, tstop_user, dt_user, dt_max, dt_nodal, ...)
    ▼
... (output field setup 단계 — m_flowtimes 의 최신 user 값 read) ...
    │
    ▼
[hydrology] read
    │
    ▼
[기타 section read]
    │
    ▼
[routine 종료]
```

옛 흐름은 `[Time] read` 가 "output field setup" 보다 **뒤에** 있어서 setup 시점에 stale defaults 가 사용됐다.

## 4. 변경 영향 범위

### 4.1 변경된 파일 (PR #900 — 4 total, additions 185 / deletions 120)

| 파일 | 변경 | 비고 |
|---|---|---|
| `engines_gpl/dflowfm/packages/dflowfm_kernel/src/dflowfm_data/unstruc_model.f90` | +113 -112 | **핵심 — readMDU reorder** |
| `engines_gpl/dflowfm/packages/dflowfm_kernel/src/dflowfm_io/sedtrails_netcdf.f90` | (sedtrails_write_stats 일부) | output time consistency 관련 보조 |
| `tests/e02_f042_c01` | (테스트) | 신규 검증 케이스 |
| `tests/e02_f042_c02` | (테스트) | 신규 검증 케이스 |

### 4.2 사용자 영향

- **기존 MDU 파일은 그대로 유효** — 입력 schema 변화 없음
- **수정 효과**: output NetCDF 의 time axis 가 `tStart` / `startDateTime` / `tStop` / `stopDateTime` 와 정합. 이전에는 시뮬레이션 자체는 정상이지만 output time 이 stale defaults 기준으로 기록될 수 있었음
- 영향 정점: 정확한 정성·정량적 영향 범위는 PR body 가 명시하지 않음 ("Clear from the issue description" 으로 UNST-9952 issue 참조)

### 4.3 검증 한계

- UNST-9952 issue tracker 본문은 GitHub repo Issue 가 아닌 Deltares 내부 Jira → 외부 직접 접근 불가
- output time inconsistency 의 정량 magnitude (몇 초·몇 dt_user 단위) 는 PR 어디에도 명시되지 않음 — empirical run 으로 확인 필요
- PR OPEN 상태 — merge 시점·release 포함 여부는 별도 추적 (`web-refs/delft3d-official-resources.md §8.2`)

## 5. References

- PR #900: <https://github.com/Deltares/Delft3D/pull/900> (OPEN, branch `fm/bugfix/UNST-9952_fix_time_reading_from_mdu`)
- 본 fix 가 다루는 파일: [`unstruc_model.f90`](https://github.com/Deltares/Delft3D/blob/fm/bugfix/UNST-9952_fix_time_reading_from_mdu/src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/dflowfm_data/unstruc_model.f90)
- web-refs cross-ref: [`web-refs/delft3d-official-resources.md §8.2`](../web-refs/delft3d-official-resources.md)
- 관련 노트: [[delft3d_dflowfm_overview]] (FM 엔진 개관)

## 6. 후속 작성 후보

- MDU 의 `[geometry]` block parameter set (mesh / structure / bathymetry) — 본 노트와 동일 patterns 으로
- `[hydrology]` block (InterceptionModel + 후속)
- MDU file family 와 D3D-4 MDF file 의 1:1 매핑표 (legacy migration 시 유용)
