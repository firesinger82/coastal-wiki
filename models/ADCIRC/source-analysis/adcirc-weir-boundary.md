---
title: "ADCIRC weir/levee 경계(weir_boundary.F90) — internal/external barrier 월류(overtopping) free/submerged flow + time-varying weir(TVW) + IBTYPE 4/24 levee·64 vertical element wall. BARMIN 임계"
topic: adcirc
canonical_source: self
citation_status: verified
last_source_check: 2026-10-11 (recovery 재판독 대조)
verification_method: "models/ADCIRC/raw/source_code/adcirc/src/weir_boundary.F90 (2715, module WEIR) 직접 read — BARINHT/BARLANHT(internal/external barrier 고도 47-50), BARMIN 0.04m 임계(51), vertical element wall BARMIN64=1.2·H0(259), TVW(time-varying weir) namelist file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-04
verification_by: "Claude Opus 4.8 (1M context) — weir 월류·TVW verbatim"
verification_date: 2026-06-04
related:
  - models/ADCIRC/source-analysis/adcirc-boundary-conditions.md
  - models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md
  - models/ADCIRC/source-analysis/adcirc-momentum-implementation.md
---

# ADCIRC weir/levee 경계 (weir_boundary.F90)

> `weir_boundary.F90`(2715, module `WEIR`) 직접 read. [[adcirc-boundary-conditions]] 의 **internal barrier(IBTYPE 4/24 levee·5/25 +pipes·64 vertical element wall)** 월류(overtopping) 계산의 실제 구현. paired weir node 양쪽 수위차로 둑 위 월류 유량 산출. 제방·방조제·도로 둑의 범람(overtopping flooding) 핵심 — 한국 연안 방조제·storm surge 침수.

## 1. Barrier 고도 (module WEIR, :47-55)

| 변수 | 의미 |
|---|---|
| `BARINHT1/2` | **internal** barrier(levee, 양면 wet) 고도 — 이전/현 step |
| `BARLANHT1/2` | **external** barrier(land, 한면 wet) 고도 |
| `BARMIN` | `BARMIN=0.04d0`는 weir 식에서 비교하는 값이다 (`src/weir_boundary.F90:50` `real(8), parameter :: BARMIN = 0.04d0 !...Minimum water depth above weir to appply weir formula`). |
| `BARMIN64*` | vertical element wall(IBTYPE 64) 의 submerged 판정 임계(`1.2·H0`, wetdry HOFF 등가) |

## 2. Weir 월류 (overtopping)

paired node(둑 양쪽, [[adcirc-boundary-conditions]] §2 weir/weird dual)의 수위 `ζ1/ζ2` 와 둑 고도 `BARHT` 로:
- 외부 weir는 `RBARWL = 2.d0*(ETA2(NNBB) - BARLANHT2(BARRIER_INDEX))/3.d0`으로 계산한다 (`src/weir_boundary.F90:1750` `RBARWL = 2.d0*(ETA2(NNBB) - &`; `src/weir_boundary.F90:1751` `BARLANHT2(BARRIER_INDEX))/3.d0`). 외부 weir는 `if (RBARWL > BARMIN) then`에서 월류한다 (`src/weir_boundary.F90:1752` `if (RBARWL > BARMIN) then`). 해석: 외부 실제 수두는 0.06 m보다 커야 한다 (`src/weir_boundary.F90:50` `real(8), parameter :: BARMIN = 0.04d0 !...Minimum water depth above weir to appply weir formula`; `src/weir_boundary.F90:1750` `RBARWL = 2.d0*(ETA2(NNBB) - &`; `src/weir_boundary.F90:1751` `BARLANHT2(BARRIER_INDEX))/3.d0`; `src/weir_boundary.F90:1752` `if (RBARWL > BARMIN) then`). 내부 weir의 해당 월류 분기는 상류 실제 수두가 0.04 m보다 커야 한다 (`src/weir_boundary.F90:50` `real(8), parameter :: BARMIN = 0.04d0 !...Minimum water depth above weir to appply weir formula`; `src/weir_boundary.F90:1876` `elseif ((RBARWL1 > RBARWL2) .and. (RBARWL1 > BARMIN)) then`). 내부 weir는 수위차·dry source·wet edge 조건도 적용한다 (`src/weir_boundary.F90:1872` `elseif (abs(RBARWL1 - RBARWL2) < 0.01d0) then`; `src/weir_boundary.F90:1889` `if (NODECODE(NNBB1) == 0 .or. NNBB1WN == 0) then`; `src/weir_boundary.F90:1876` `elseif ((RBARWL1 > RBARWL2) .and. (RBARWL1 > BARMIN)) then`).
- 하류 둑 위 수두가 상류 수두의 2/3보다 크면 subcritical 식을 쓴다 (`src/weir_boundary.F90:1865` `RBARWL1F = 2.d0*RBARWL1/3.d0`; `src/weir_boundary.F90:1887` `if (RBARWL2 > RBARWL1F) then`; `src/weir_boundary.F90:1892` `FLUX = -RampIntFlux*RBARWL2*BARINCFSB(I)* &`; `src/weir_boundary.F90:1893` `(2.d0*G*(RBARWL1 - RBARWL2))**0.5d0`).
- 그 외 월류 가능한 경우는 supercritical 식을 쓴다 (`src/weir_boundary.F90:1887` `if (RBARWL2 > RBARWL1F) then`; `src/weir_boundary.F90:1900` `FLUX = -RampIntFlux*BARINCFSP(I)*RBARWL1F* &`; `src/weir_boundary.F90:1901` `(RBARWL1F*G)**0.5d0`). 해석: 양쪽 수위가 모두 둑 위여도 supercritical일 수 있다 (`src/weir_boundary.F90:1887` `if (RBARWL2 > RBARWL1F) then`).
- supercritical/subcritical 전환은 하류/상류 수심비로 판정. → 월류 유량 `Q` 가 [[adcirc-momentum-implementation]] 의 normal flux 로 양 node 에 부호 반대 적용(질량 보존).

## 3. Vertical element wall — IBTYPE 64 (:259)

- `BARMIN64`와 두 상태별 기본 수두 문턱은 `1.2d0*H0`다 (`src/weir_boundary.F90:258` `BARMIN64 = 1.2d0*H0 ! This is equivalent to HOFF in wetdry.F`; `src/weir_boundary.F90:259` `BARMIN64_NOSUBM = 1.2d0*H0`; `src/weir_boundary.F90:260` `BARMIN64_SUBM = 1.2d0*H0`). submerged 전환은 이전 상태별 수두 문턱과 `ETASLP <= BARSLIM64_ELEM`을 함께 검사한다 (`src/weir_boundary.F90:2104` `if (((ISSUBMP == 0 .and. RBARWLL >= BARMIN64_NOSUBM) .or. &`; `src/weir_boundary.F90:2105` `(ISSUBMP == 1 .and. RBARWLL >= BARMIN64_SUBM)) .and. &`; `src/weir_boundary.F90:2106` `(ETASLP <= BARSLIM64_ELEM)) then`). 이후 기울기 조건과 edge 조건을 별도로 검사해 submerged 상태를 해제한다 (`src/weir_boundary.F90:2116` `if (ISSUBMERGED64(I) /= 0 .and. &`; `src/weir_boundary.F90:2117` `NODECODE(NNBB1) /= 0 .and. &`; `src/weir_boundary.F90:2118` `HTOT < 4.d0*H0) then`; `src/weir_boundary.F90:2130` `if (SLP > BARSLIM64_EDGE) then`; `src/weir_boundary.F90:2141` `if (SLP > BARSLIM64_EDGE) then`; `src/weir_boundary.F90:2157` `if (UNSUBMERGE) then`; `src/weir_boundary.F90:2158` `ISSUBMERGED64(I) = 0`).

## 4. Time-Varying Weir (TVW)

- TVW는 둑 고도를 시간에 따라 바꾼다 (`src/weir_boundary.F90:1743` `call COMPUTE_BARRIER_HEIGHT(BARRIER_INDEX, &`; `src/weir_boundary.F90:1835` `call COMPUTE_BARRIER_HEIGHT(I, TIMELOC, BARINHT1(I) &`). `VARYTYPE=1`의 필수 시작 시각 검사는 day·hour·sec를 쓴다 (`src/weir_boundary.F90:1133` `if (ISNULL(TimeStartday) .and. &`; `src/weir_boundary.F90:1134` `ISNULL(TimeStartHour) .and. &`; `src/weir_boundary.F90:1135` `ISNULL(TimeStartSec)) then`). 필수 끝 시각 검사도 day·hour·sec를 쓴다 (`src/weir_boundary.F90:1140` `if (ISNULL(TimeEndday) .and. &`; `src/weir_boundary.F90:1141` `ISNULL(TimeEndHour) .and. &`; `src/weir_boundary.F90:1142` `ISNULL(TimeEndSec)) then`). minute만 지정하면 이 검사는 종료 경로로 들어간다 (`src/weir_boundary.F90:1136` `call terminate(exit_code=ADCIRC_EXIT_FAILURE, &`; `src/weir_boundary.F90:1143` `call terminate(exit_code=ADCIRC_EXIT_FAILURE, &`).

- 기본 입력 파일명은 `fort.tvw`다 (`src/global.F:324` `CHARACTER(80)                :: TVW_FILE = 'fort.tvw' !..From namelist, file for time varying weirs`). `TVW_FILE`로 입력 파일명을 바꿀 수 있다 (`src/weir_boundary.F90:997` `call openFileForRead(99, trim(INPUTDIR)//'/'// &`; `src/weir_boundary.F90:998` `trim(tvw_file), IOS, required=.false.)`). 현행 rst의 제목은 `Fort.142`다 (`docs/technical_reference/input_files/time_varying_weirs.rst:3` `Fort.142: Time Varying Weirs Input File`).
- `VARYTYPE=3`의 시간 offset은 `TimeStartDay·TimeStartHour·TimeStartMin·TimeStartSec`를 초로 합한다 (`src/weir_boundary.F90:1095` `OFFSET = TimeStartDay*86400d0 + &`; `src/weir_boundary.F90:1096` `TimeStartHour*3600d0 + &`; `src/weir_boundary.F90:1097` `TimeStartMin*60d0 + &`; `src/weir_boundary.F90:1098` `TimeStartSec`). `HOT` 생략 또는 0은 cold start 기준이다 (`src/weir_boundary.F90:1106` `if (ISNULL(I=HOT) .or. (HOT == 0)) then`; `src/weir_boundary.F90:1107` `HOTADD = 0d0`). `HOT=1`일 때만 핫스타트 시간을 offset에 더한다 (`src/weir_boundary.F90:1108` `elseif (HOT == 1) then`; `src/weir_boundary.F90:1109` `HOTADD = DTDP*dble(ITHS)`; `src/weir_boundary.F90:1110` `OFFSET = OFFSET + HOTADD`).
- schedule의 시작 시간 식은 `BAR_DEG_START = TimeStartDay*86400d0 + TimeStartHour*3600d0 + TimeStartMin*60d0 + TimeStartSec + HOTSEC`다 (`src/weir_boundary.F90:1377` `BAR_DEG_START = TimeStartDay*86400d0 + &`; `src/weir_boundary.F90:1378` `TimeStartHour*3600d0 + &`; `src/weir_boundary.F90:1379` `TimeStartMin*60d0 + &`; `src/weir_boundary.F90:1380` `TimeStartSec + &`; `src/weir_boundary.F90:1381` `HOTSEC`). 현재 끝 시간 식은 `BAR_DEG_END = TimeEndDay*86400d0 + TimeEndHour*3600d0 + TimeEndMin*60d0 + TimeStartSec + HOTSEC`다 (`src/weir_boundary.F90:1382` `BAR_DEG_END = TimeEndDay*86400d0 + &`; `src/weir_boundary.F90:1383` `TimeEndHour*3600d0 + &`; `src/weir_boundary.F90:1384` `TimeEndMin*60d0 + &`; `src/weir_boundary.F90:1385` `TimeStartSec + &`; `src/weir_boundary.F90:1386` `HOTSEC`).
- v53 schedule 문서는 끝의 초를 `TimeEndSec`로 지정한다 (`models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/schedule-file/index.md:418` `**TimeEndSec** – number of seconds since the beginning of the schedule when the change in weir height is complete`). v56.2.1 코드는 그 자리에 `TimeStartSec`를 더한다 (`src/weir_boundary.F90:1385` `TimeStartSec + &`).
- `ScheduleFile` 경로는 `GLOBALDIR`다 (`src/weir_boundary.F90:1335` `inquire (FILE=trim(GLOBALDIR)//"/"//trim(MYFILE), &`).
- 내부 경계 높이 하한은 두 노드 지반 높이의 최댓값이다 (`src/weir_boundary.F90:641` `DEPTH = max(-DP(NBV(MYIDX)), -DP(IBCONN(MYIDX)))`; `src/weir_boundary.F90:642` `if (BAR_HEIGHT < DEPTH) then`; `src/weir_boundary.F90:645` `BAR_HEIGHT = DEPTH`).
- 장벽 높이 계산은 GWCE 전에 호출한다 (`src/timestep.F:966` `CALL COMPUTE_EXTERNAL_BOUNDARY_FLUX(I,TIMELOC,QN2(I))`; `src/weir_boundary.F90:1743` `call COMPUTE_BARRIER_HEIGHT(BARRIER_INDEX, &`; `src/timestep.F:1030` `CALL COMPUTE_INTERNAL_BOUNDARY_FLUX(I,J,K,`; `src/weir_boundary.F90:1835` `call COMPUTE_BARRIER_HEIGHT(I, TIMELOC, BARINHT1(I) &`; `src/timestep.F:1073` `call solveGWCE(it, ITIME_BGN, timeloc, timeh)`). 단계 끝은 핫스타트 쓰기 뒤에 현재 높이를 이전 높이로 복사한다 (`src/timestep.F:1215` `CALL writeHotstart(TimeLoc, IT)`; `src/timestep.F:1227` `IF(NFLUXIB.EQ.1)THEN`; `src/timestep.F:1228` `BARINHT1(:)=BARINHT2(:)`; `src/timestep.F:1230` `IF(NFLUXB.EQ.1)THEN`; `src/timestep.F:1231` `BARLANHT1(:)=BARLANHT2(:)`).

## 5. 위치

- [[adcirc-boundary-conditions]] 가 IBTYPE 카탈로그(둑 종류)를, 본 노트가 **월류 유량 계산 메커니즘**을 담당. wetting-drying([[adcirc-wetting-drying-implementation]])과 연계(둑 위 wet/dry).
- 응용: 방조제 월파 침수, 제방 붕괴 범람, hurricane levee overtopping(New Orleans 등).

## 6. 연결

- [[adcirc-boundary-conditions]] — IBTYPE 4/5/24/25/64 weir 카탈로그(본 노트가 그 월류 구현)
- [[adcirc-momentum-implementation]] — 월류 Q → normal flux
- [[adcirc-wetting-drying-implementation]] — 둑 위 wet/dry(BARMIN·H0)
