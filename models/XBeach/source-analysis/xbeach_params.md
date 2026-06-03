---
title: "XBeach 파라미터 입력 시스템(params.F90) — all_input: params.txt readkey + setallowednames(enum) + default/range 검증 + backward compatibility(instat→wavemodel)"
topic: xbeach
canonical_source: self
citation_status: verified
verification_method: "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90 (2712) 직접 read — all_input(25) readkey_int/dbl/name, setallowednames(front/tide enum 507-562), check_file_exist('params.txt')(54), check_instat_backward_compatibility(63), wavemodel isSetParameter(71) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — 파라미터 입력 시스템 verbatim"
verification_date: 2026-06-03
related:
  - models/XBeach/source-analysis/xbeach-parameter-glossary-v1.md
  - models/XBeach/source-analysis/xbeach_initialize.md
  - models/XBeach/source-analysis/xbeach_mode_dispatch.md
---

# XBeach 파라미터 입력 시스템 (params.F90)

> `params.F90`(2712) 직접 read. `params.txt`(XBeach 의 단일 입력파일) 를 읽어 `parameters` derived type(`par%*`) 채우는 시스템(module `params`). 모든 par 의 default·범위·enum·backward compat 을 한 곳에서 정의. 파라미터 **목록**(의미)은 [[xbeach-parameter-glossary-v1]], 본 노트는 **읽기·검증 메커니즘**.

## 1. all_input (params.F90:25) — 마스터 읽기

```fortran
call check_file_exist('params.txt')                          ! 입력파일 필수
par%X = readkey_int/dbl/name('params.txt','X', default, min, max, ...)   ! 키별 읽기+검증
```
- `readkey_*`(readkey_module): int/dbl/name/dblvec — 키워드별 값 읽기 + **default + [min,max] 범위 검증**(범위 밖이면 경고/clamp). 미지정 키는 default.
- `readkey_inio = toall`: 읽은 모든 키를 PRINT/log 에 echo(입력 검증 추적).

## 2. enum 파라미터 — setallowednames (params.F90:507-562)

문자열 옵션을 정수 상수로 매핑:
```fortran
call setallowednames('abs_1d',FRONT_ABS_1D, 'abs_2d',FRONT_ABS_2D, 'wall',FRONT_WALL, ...)  ! front
call setallowednames('instant',TIDETYPE_INSTANT, 'velocity',..., 'hybrid',...)              ! tide
```
- front/back/lateral BC·tidetype·break·scheme·wavemodel·solver 등 enum 을 허용이름→상수로. 잘못된 이름 시 에러([[xbeach_flow_boundary_conditions]]·[[xbeach_wave_breaking]] 의 상수원).

## 3. Backward compatibility

- `check_instat_backward_compatibility`(:63): 구 `instat`(파 입력 type) → 신 `wavemodel`(stationary/surfbeat/nonh) 매핑([[xbeach_mode_dispatch]]). 구 입력파일 호환.
- `wavemodel` isSetParameter(:71) 우선, 없으면 instat 로 추론.
- `useXBeachGSettings`: 사전 정의 설정 collection(default set).

## 4. 검증·의존

- 파라미터 간 의존 검증(예: nonh 면 front=nonh_1d 강제, params.F90:1718-1732). file length 검증(`checkbcfilelength` 등). MPI broadcast(`parmapply`).

## 5. 연결

- [[xbeach-parameter-glossary-v1]] — par 목록·의미(본 노트는 읽기 메커니즘)
- [[xbeach_initialize]] — all_input 후 초기화
- [[xbeach_mode_dispatch]] — wavemodel/instat 매핑
- [[xbeach_flow_boundary_conditions]] / [[xbeach_wave_breaking]] — enum 상수(front/break) 정의원
