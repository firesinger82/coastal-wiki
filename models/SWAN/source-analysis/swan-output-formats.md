---
title: "swan output formats"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-output-formats.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시. 2026-10-13 recovery 대조 보고서 R1–R8 반영"
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
last_source_check: "2026-10-13 (recovery 대조 반영)"
---

## Scope

SWAN's output dispatch system: `BLOCK` gridded output (`BLKP/BLKD/BLKV`), `TABLE` point output (`TABD/TABI/TABS/TABT/TABP`), 1D vs 2D spectral output (`SPEC1D`/`SPEC2D`), `NESTOUT` for parent-child nesting (writes spectral file consumed by `BOUND NEST`), NetCDF activation via build option (no `NCNAME` keyword), file naming/unit assignment, MPI per-rank file naming (`-NNN`), and the `OUTPUT tbeg deltt` time-frequency control. Use this when wiring outputs for a SWAN run, debugging spectrum file structure, or interpreting BLOCK vs TABLE files.

## Source basis

- `swanpre2.ftn:1160-1226, 1243, 1482-2467` — output parsers, frequency control.
- `swanout1.ftn:435, 681-706` — `SWOUTP` dispatch, `SWORDC` enable.
- `swanout2.ftn:178-2154` — writers, NetCDF routing, spectrum format.
- `swn_outnc.ftn90:1003-1641` — NetCDF variable definitions.
- `swanmain.ftn:1760-2277` — output variable types.
- `swanpre2.ftn:2649-4144` — `BOUND NEST`, `BCFILE`, `SwBOUN`.
- `ocpmix.ftn:1665-1849`, `swmod1.ftn:460` — file unit assignment.
- `src/CMakeLists.txt:31,104,108`, `switch.pl:102` — NetCDF build.

## A. BLOCK output (gridded)

Parsed as `BLOCK 'sname' HEADER/NOHEADER 'fname' ... <DSPR/HSIGN/DIR/.../TPS/...>` with optional `OUTPUT tbeg deltt` (`swanpre2.ftn:1160`).

Request types (`:1194`):

| Type | Meaning |
|---|---|
| `BLKP` | Paper / header text format |
| `BLKD` | Datafile / no-header format |
| `BLKV` | VTK filenames |

Variables resolved through `OVKEYW`. Examples:
- `HS`/`HSIGN` → ivtype 10 (`swanmain.ftn:1760`).
- `DIR` → 13 (`:1795`).
- `TPS` → 53 (`:2277`).

`SVARTP` matches against `OVKEYW` and aliases (`swanpre2.ftn:2452`).

Writer dispatch: `SWOUTP` → `SWBLOK / SWBLKP / SWBLKV` (`swanout1.ftn:435`).

Format: datafile writes each scalar/vector component as gridded block via `FLT_BLOCK`; `IDLA` controls ordering (`swanout2.ftn:560`). Header/paper writes frame/title/unit/time + x/y grid labels (`:510`).

## B. TABLE output (point)

Parsed as `TABLE 'sname' HEADER/NOHEADER/INDEXED 'fname' <...>` + optional `OUTPUT tbeg deltt` (`swanpre2.ftn:1565`).

Request types (`:1588`):

| Type | Meaning |
|---|---|
| `TABD` | NOHEADER의 실수 텍스트 |
| `TABI` | Indexed |
| `TABS` | TABLE SWAN. 위치 목록을 포함한다. 비정상 계산은 TIME도 포함한다. |
| `TABT` | TABLE STAB. 위치 목록 대신 TABLE 표식을 쓴다. |
| `TABP` | Paper / formatted |

`SWTABP` writes one row per output point; continues if many quantities requested (`swanout2.ftn:1257`).

Headers (`:1410-1480`):
- `TABP/TABI`: run/table/version + quantity short names + units.
- TABLE SWAN은 TABS이며 위치 목록을 포함한다. TABS의 비정상 계산은 TIME도 포함한다. (`src/swanpre2.ftn:1594` `RTYPE = 'TABS'`; `src/swanout2.ftn:1493` `WRITE (NREF, 102) 'TIME', 'time-dependent data'`.)
- TABLE STAB은 TABT이며 TABLE 표식을 쓴다. 두 형식의 차이를 시간 유무로 설명하지 않는다. (`src/swanout2.ftn:1489` `IF (RTYPE.EQ.'TABT') THEN`; `src/swanout2.ftn:1490` `WRITE (NREF,102) 'TABLE'`.)

Rows fixed-field text:
- Time: `A18`.
- `TABD`: uses `FLT_TABLE`.
- Other: `F13.X`.
- Vector quantities: two columns.

## C. SPEC1D / SPEC2D

문법은 `SPECOUT 'sname' SPEC1D/SPEC2D ABS/REL S/L 'fname' ... OUTPUT ...`이다. 일반 ABS 2D 요청은 SPEC이다. 일반 REL 2D 요청은 SPRC이다. 마지막 C는 이 구현에서 2D 분기를 선택한다. Cartesian 방향 규약을 뜻하지 않는다. (`src/swanpre2.ftn:1890` `RTYPE  = 'SPEC'`; `src/swanpre2.ftn:1894` `RTYPE(3:3)  = 'R'`; `src/swanout2.ftn:1944` `IF (RTYPE(4:4).EQ.'C') THEN`.)

`SWSPEC` documents (`swanout2.ftn:1823`):
- `SPEC` = 2D spectral output.
- `SPE1` = 1D frequency spectrum.

File header: SWAN-standard spectral file, then optional `TIME, LOCATIONS/LONLAT, RFREQ` or `AFREQ`, frequency list. For 2D: `NDIR/CDIR` direction list (`:1907`).

Quantity:
- 2D: one `VaDens`/`EnDens` quantity, units `m²/Hz/degr` or `J/m²/Hz/degr` (`:1944`).
- 1D: three quantities — density, mean direction, directional spread (`:1977`).

Computation: `SWCMSP` (`:2154`):
- `|OTYPE|=2` for 2D.
- `|OTYPE|=1` for 1D (integrates over θ).

2D calls `WRSPEC`; 1D writes `LOCATION` and one line per frequency with density, direction, spread (`:2057`).

## D. NESTOUT (parent dump)

Parsed as `NESTOUT 'sname' 'fname' (OUTPUT tbeg deltnst ...)`; output point set must be type `N` (`swanpre2.ftn:1978`).

Internally creates output request `RTYPE='SPRC'` (`:2015`).

That means **spectral, relative-frequency, complete 2D directional output**, written through same `SWSPEC` machinery.

Resulting parent file is SWAN-standard spectral file with locations, `RFREQ`, directions, 2D density blocks — suitable as child boundary file (`swanout2.ftn:1934`).

## E. BOUND NEST (child consumption)

`SWBOUN` reads `BOUNDARY`. Structure explicitly documents `NEST: Read filename; Call BCFILE` (`swanpre2.ftn:2649`).

For file/spec boundary input, `SWBOUN` reads `FILE/SPEC`, increments boundary-file count, calls `BCFILE` (`:3666`).

`BCFILE` opens parent spectral file, reads `SWAN, TIME, LOCATIONS/LONLAT`, frequencies, directions, stores file characteristics. Spectral densities are read later by `RESPEC` during computation (`:4015`).

For `BCTYPE='NEST'`, file locations interpolate to child boundary grid points via `SWBCPT` (`:4144`).

So **NESTOUT writes; BOUND NEST reads** — same spectral file format.

## F. NetCDF (build option, no `NCNAME` keyword)

There is **no literal `NCNAME` symbol** in this source tree.

NetCDF activated by build option `NETCDF`:
- 현재 src/CMakeLists.txt에서 -netcdf를 추가하는 줄은 31행이다. (`src/CMakeLists.txt:31` `list( APPEND SWITCHES -netcdf )`.)
- !NCF를 제거하는 줄은 switch.pl 102행이다. (`switch.pl:102` `if ($ncf=~/TRUE/) {$newline=~s/^!NCF//;}`.)
- srclistnc 선택과 Fortran 링크는 src/CMakeLists.txt 104·108행이다. (`src/CMakeLists.txt:104` `include( ${SRC}/srclistnc.cmake )`; `src/CMakeLists.txt:108` `target_link_libraries( swan${VERSION} PUBLIC NetCDF::NetCDF_Fortran )`.)

Runtime routing by `.nc/.NC` filename checks in `!NCF` paths for block/table/spec output (`swanout2.ftn:178, 1876`).

NetCDF variables defined via `STNAMES` (`swn_outnc.ftn90:1641`):
- `depth, xcur/ycur, hs, tm01, tp, theta0, spread, xwnd/ywnd, tps`.
- Partition variables.

`create_variables` defines map or point variables (`:1604`).

Spectral NetCDF also writes auxiliary `depth, currents, hs, wind` unless `NOAUX` (`:1003`).

## G. Units / file naming

Output requests store (`swanpre2.ftn:1243`):
- `OQI(1)=NREF`.
- `OQI(2)=request index`.
- `OQI(3)=number of variables`.
- `OUTP_FILES(NREOQ)=FILENM`.

If filename blank → output to `PRINTF`; otherwise `NREF=0` and writer opens later (`:1222`).

In MPI/parallel mode SWAN appends `-NNN` node numbers to many output filenames (`:1226, 1915`).

`FOR` assigns free unit numbers when `IUNIT=0`; qualifiers `O/N/S/U` and `F/U`; opens sequential formatted/unformatted (`ocpmix.ftn:1665`). Free unit search starts at `FUNLO`, skips reserved 411-417 (`:1849`).

Standard units: `INPUTF=3, PRINTF=4, SCREEN=6` (`swmod1.ftn:460`).

## H. Output frequency

`OUTPUT` parsed as pseudo-variable `IVTYPE=98` (`swanpre2.ftn:2467`).

For BLOCK/TABLE/SPEC/NESTOUT, `OUTPUT` reads:
- `tbeg` → `OQR(1)`.
- `delt` → `OQR(2)`.

Using `INCTIM/INITVD` (`swanpre2.ftn:1482, 1957, 2038`).

Runtime: `SWORDC` enables output (`swanout1.ftn:681`):
- If final time reached with negative interval.
- 정기 출력은 요청 시각 이상인 첫 계산 시각에서 수행한다. (`src/swanout1.ftn:698` `ELSE IF (OUTR(2).GT.0. .AND. TIMCO.GE.TNEXT) THEN`.)
- Then advances next output time by `OUTR(2)`.

**Stationary mode always outputs** (`:706`) — once per stationary computation.

## Decision Guide

| Need | Output |
|---|---|
| Hsig map for plotting | `BLOCK 'COMPGRID' HEADER 'hs.dat' HSIGN OUTPUT t0 1 hr` |
| Hsig time series at gauge | `TABLE 'pts' HEADER 'hs_pts.dat' TIME XP YP HSIGN TPS DIR OUTPUT t0 30 min` |
| 1D frequency spectrum at point | `SPECOUT 'pts' SPEC1D ABS 'spec.dat'` |
| 2D directional spectrum | `SPECOUT 'pts' SPEC2D ABS 'spec2d.dat'` |
| Parent → child nesting | `NESTOUT 'nest_pts' 'nest.spec' OUTPUT t0 1 hr` |
| 받는 실행 | `BOUNDNEST1 NEST 'nest.spec' OPEN`. fname 하나를 읽는다. (`src/swanpre2.ftn:2971` `CALL INCSTR ('FNAME',FILENM,'REQ', ' ')`.) |
| NetCDF map output | Build with `NETCDF` flag; use `.nc` extension in filename |
| MPI parallel runs | Output filenames auto-append `-NNN` per rank |

## Working Rules

- MAT는 NOHEADER가 필요하다. (`src/swanpre2.ftn:1212` `CALL MSGERR(4,'No header allowed for Matlab files')`; swanuse PDF 109쪽 / 인쇄 101쪽.)
- For SPEC2D files, ensure `RFREQ`/`AFREQ` (relative vs absolute frequency) matches downstream tool expectations.
- For nesting: parent and child must use **compatible** frequencies and directions (typically same, or child wider range).
- Output frequency: BLOCK every 1 hour, TABLE every 15-30 min, SPEC at peak storm time only (very large files).
- NetCDF output requires SWAN built with `-DNETCDF` flag — verify with linker output.
- For parallel SWAN: `-NNN` files need post-processing to merge — use SWAN's `SWAN-merge` tool or manual concatenation.
- `BLKV` (VTK) useful for ParaView visualization.

## Common Pitfalls

- ▢ Looking for `NCNAME` keyword — doesn't exist; NetCDF activated by build flag + `.nc` filename.
- ▢ Setting `OUTPUT t0 1` thinking units are seconds — depends on `INCTIM` mode; check `MODE` settings.
- ▢ Stationary run outputting once per `MXITST` iteration — actually outputs once per stationary computation.
- ▢ SPEC2D file size — very large; restrict to a few stations and few output times.
- ▢ Output filename collision in MPI (without `-NNN` suffix support) — check that suffix is appended.
- ▢ Parent nest `NESTOUT` with too-coarse output frequency — child boundary stale between updates.
- ▢ `BOUND NEST` reading file with mismatched frequency bins — interpolation may produce zeros at child range edges.
- ▢ Forgetting `OUTPUT tbeg deltt` — output uses default (often once at end).

## Next expansion

- BLOCK variable list (full ivtype table).
- SPEC2D file format example.
- NetCDF SWAN viewer tool reference.
- SWAN-merge for MPI output post-processing.

## References

- SWAN User Manual (Output and Output options).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/swan/source_code/swan/src`. Auto-draft = false; review_required = true.

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD `43e9bbb` (2026-07-13 patch B). (`src/swanmain.ftn:965` `VERNUM = 41.51`.)

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R4:T1-014 | 출력 시간 반올림 | swanuse PDF 18쪽 / 인쇄 10쪽: “nearest” | `src/swanout1.ftn:698` `ELSE IF (OUTR(2).GT.0. .AND. TIMCO.GE.TNEXT) THEN`. | B 문서 오기 | 정기 출력은 요청 시각 이상인 첫 계산 시각에서 수행한다. |
| R6:O-022 | MAT·NetCDF·VTK 선택 | swanuse PDF 109–110쪽 / 인쇄 101–102쪽: `.mat`은 binary MATLAB이다. `.nc`는 NetCDF이다. `.vtk` 요청은 격자에 따라 `.vts` 또는 `.vtu`를 생성한다. | `src/swanpre2.ftn:1212` `CALL MSGERR(4,'No header allowed for Matlab files')`. `src/swanpre2.ftn:1216` `VTK = INDEX( FILENM, '.VT' ).NE.0 .OR.`. `src/swanpre2.ftn:1220` `RTYPE = 'BLKV'`. `src/swanout2.ftn:294` `CALL SWRMAT( MYK, MXK, NAMVAR,`. `src/swanout2.ftn:299` `!NCF                CALL swn_outnc_appendblock(MYK, MXK, IVTYPE, OQI(1),`. | C 문서 누락 | NetCDF는 `-netcdf` 빌드에서 활성화한다. MAT는 NOHEADER가 필요하다. 확장자 검사는 문자열 포함 검사이다. 문서는 MAT의 HEADER 금지를 적지 않는다. |
| R6:O-091 | PARTIT | swanuse PDF 114쪽 / 인쇄 106쪽: `raw spectral partition file meant for wave system tracking post-processing.` `PARTIT cannot be used as an output parameter in TABLE.` | `src/swanout2.ftn:1131` `&                 CHTIME(1:8),CHTIME(10:16),YP,XP,'''grid_point''',`. `src/swanout2.ftn:1153` `WRITE(NREF,'(I3,F8.2,F8.2,F8.2,F9.2,F9.2,F7.2)')`. `src/swanout2.ftn:1154` `&                 0, HS, TP, WL, DIR, DSPR, 999.99`. 1158–1159행은 분할 번호·Hs·Tp·WL·DIR·DSPR·WF를 쓴다. | C 문서 누락 | 머리말 좌표 순서는 YP, XP이다. 전체 파랑 행의 wind fraction 자리에는 999.99를 쓴다. 각 분할은 일곱 열이다. PTSTEEP은 이 파일에 쓰지 않는다. 매뉴얼은 형식의 상세를 외부 문서로 넘긴다. 여기서는 SWAN이 실제 쓰는 필드만 확정한다. |
| R6:O-113 | MONth·ESCAle·COMPress | swanuse PDF 142쪽 / 인쇄 134쪽: `MONth ESCAle COMPress`. 4장에는 의미 설명이 없다. | `src/swanpre2.ftn:1931` `!NCF           ORQTMP%OQI(4) = ORQTMP%OQI(4) + 1`. 1935행은 +2이다. 1939행은 +4이다. `src/swn_outnc.ftn90:1337` `if ( mod(iocode,2) == 1 .and. NSTATM == 1) monthly = .true.`. `src/swn_outnc.ftn90:1327` `! the energy itself is then stored as int16 instead of float`. | C 문서 누락 | MONTH는 비정상 시간축의 기준을 월초로 둔다. ESCALE은 시각·위치별 배율과 int16 밀도를 쓴다. COMPRESS는 전체 구조 격자의 건조점을 point list에서 뺀다. 세 키워드는 Appendix C에 있으므로 “어떤 문서에도 없는 명령”으로 세지 않는다. |
| R6:O-114 | NetCDF 물리량 지원 집합 | swanuse PDF 109쪽 / 인쇄 101쪽은 BLOCK의 `.nc` 출력을 설명한다. PDF 115쪽 / 인쇄 107쪽의 TABLE 설명은 출력 물리량을 BLOCK과 공유한다고 적는다. 이 쪽에는 `.nc` 설명이 없다. 두 쪽에는 NetCDF 지원 물리량 목록이 없다. | `src/swanpre2.ftn:1267` `!NCF                   IF ( STNAMES(IVTYPE,1).EQ. ' ' ) CALL MSGERR (2,`. `src/swn_outnc.ftn90:1616` `stname = STNAMES(ivtyp(i),1)`. 1635행은 미지원 물리량 경고이다. [공식 변경 이력](../raw/manuals/website/modifications/modifications.htm) 1206–1211행은 미지원 NetCDF 출력 물리량 경고를 설명한다. | C 문서 누락 | 지원 물리량의 제한 자체는 공식 변경 이력에 명시되어 있다. C는 swanuse PDF 109쪽·115에 지원 목록이 빠진 점에 한정한다. STNAMES(1642–1691행)에 등록된 일반 물리량은 DEPTH, VEL, UBOT, HSIGN, TM01, RTP, DIR, PDIR, DSPR, WLEN, WIND, RTM01, DHSIGN, DRTM01, TM02, URMS, UFRIC, CDRAG, HSWELL, TMM10, RTMM10, WATLEV, BOTLEV, TPS이다. PTHSIGN·PTRTP·PTDIR·PTDSPR는 각 6개 열만 등록된다. TRANSP·FORCE·QP·BFI는 이 목록에 없다. [10-13 결론 검증 보완] [10-13 전수 검증 정정] |
| R6:O-131 | TABLE SWAN·STAB | 명령 설명 없음. Appendix D는 스펙트럼 형식만 명세한다. | `src/swanpre2.ftn:1593` `ELSE IF (KEYWIS ('SWAN')) THEN`. `src/swanpre2.ftn:1594` `RTYPE = 'TABS'`. `src/swanpre2.ftn:1595` `ELSE IF (KEYWIS ('STAB')) THEN`. `src/swanpre2.ftn:1596` `RTYPE = 'TABT'`. `src/swanout2.ftn:1490` `WRITE (NREF,102) 'TABLE'`. `src/swanout2.ftn:1522` `WRITE (NREF, 104) OVEXCV(IVTYPE), 'exception value'`. | C 문서 누락 | 두 형식은 SWAN 1 머리말과 QUANT 메타데이터를 쓴다. TABS는 위치 목록과 비정상 TIME을 쓴다. TABT는 위치 목록 대신 TABLE을 쓴다. 두 형식을 “시간 유무”만으로 나누면 틀린다. 벡터 메타데이터는 X-와 Y-로 분리한다. |
| R6:O-133 | MDGRID·NOAUX·NESTOUT NetCDF 기본값 | 두 키워드는 네 매뉴얼과 웹 원문에서 검색 0건. | `src/swanpre2.ftn:1942` `!NCF        IF (KEYWIS('MDGRID')) THEN`. `src/swanpre2.ftn:1946` `!NCF        IF (KEYWIS('NOAUX')) THEN`. `src/swanpre2.ftn:2034` `!NCF     &       ORQTMP%OQI(4) = 18`. `src/swn_outnc.ftn90:1315` `spc_as_map = .true.`. `src/swn_outnc.ftn90:1305` `noaux  = .true.`. | C 문서 누락 | MDGRID는 COMPGRID 전체 점 수 조건을 통과하면 건조점까지 포함한 격자 배열을 쓴다. NOAUX는 보조 물리량을 생략한다. NESTOUT .nc의 18은 ESCALE=2와 NOAUX=16을 합한 값이다. 모두 -netcdf 빌드 조건이다. |
| R6:O-134 | NetCDF의 밀도·시간 기록 | `.nc` 출력은 문서에 있으나 이 차이는 명세하지 않는다. | `src/swn_outnc.ftn90:740` `SPCDIR(1,2), SPCDIR(1,3), 1., KGRPNT,  &`. `src/swn_outnc.ftn90:1352` `if ( ivtype == 40 ) return`. `src/swn_outnc.ftn90:1358` `xpctime = seconds_since_epoch(xpctmp(1), xpctmp(2))`. `src/swn_outnc.ftn90:1364` `call MSGERR(3, 'The projnr number may not be zero')`. | C 문서 누락 | 스펙트럼 계산에 OFAC=1을 전달하므로 NetCDF는 분산 밀도를 기록한다. ASCII의 INRHOG에 따른 EnDens 전환과 다르다. TIME 물리량 열은 만들지 않고 시간축을 쓴다. 정상 BLOCK의 정수 PROJNR=0은 오류이다. 비정수 PROJNR에는 기록 번호 1을 쓴다. 기록자에 주파수는 Hz로 넘긴다. 방향은 radian으로 넘긴다. 근거는 같은 파일 649행의 `lspcaux%f     = SPCSIG/PI2`와 654행의 `lspcaux%theta = SPCDIR(:,1)`이다. |
| R6:O-136 | BLOCK UNIT의 적용 형식 | swanuse PDF 114쪽 / 인쇄 106쪽: `The program divides computed values by [unit] before writing to file`. | `src/swanout2.ftn:294` `CALL SWRMAT( MYK, MXK, NAMVAR,`. `src/swanout2.ftn:295` `&                    VOQ(1,VOQR(IVTYPE)), NREF, IREC(IRQ),`. `src/swanout2.ftn:300` `!NCF     &                                     IRQ, VOQ(1,VOQR(IVTYPE)),`. `src/swanout1.ftn:438` `CALL SWBLKV ( CORQ%OQI, CORQ%OQR, CORQ%IVTYP,`. | C 문서 누락 | MAT·NetCDF에는 원래 VOQ를 넘긴다. VTK 호출에는 FAC 배열을 넘기지 않는다. 이 세 형식에는 텍스트 SBLKPT의 UNIT 나눗셈을 적용하지 않는다. 문서에는 형식별 예외가 빠져 있다. |
| R6:N-006 | TABS·TABT | 이 노트의 수정 전 판(`a0298b83`) 62행은 TABT를 `SWAN-standard with time`으로 적었다. 같은 판 69행은 TABS/TABT 모두에 `TIME, LOCATIONS`를 배정했다. 두 줄은 이번 대조에서 고쳤다. [10-13 표본 정정] | O-131. `src/swanout2.ftn:1489` `IF (RTYPE.EQ.'TABT') THEN`. `src/swanout2.ftn:1490` `WRITE (NREF,102) 'TABLE'`. `src/swanout2.ftn:1493` `WRITE (NREF, 102) 'TIME', 'time-dependent data'`. | B 문서 오기 | TABLE SWAN은 TABS이며 위치 목록을 포함한다. TABS의 비정상 계산은 TIME도 포함한다. TABLE STAB은 TABT이며 TABLE 표식을 쓴다. 두 형식의 차이를 시간 유무로 설명하지 않는다. |
| R7:N-031 | netCDF 참조 줄 | `models/SWAN/source-analysis/swan-output-formats.md:126` ``- Appends `-netcdf` to `switch.pl` (`CMakeLists.txt:26`).`` | `src/CMakeLists.txt:30–32` `list( APPEND SWITCHES -netcdf )`; `src/CMakeLists.txt:104` `include( ${SRC}/srclistnc.cmake )`; `src/CMakeLists.txt:108` `target_link_libraries( swan${VERSION} PUBLIC NetCDF::NetCDF_Fortran )`; `switch.pl:102` `if ($ncf=~/TRUE/) {$newline=~s/^!NCF//;}`. | B 문서 오기 | 현재 src/CMakeLists.txt에서 -netcdf를 추가하는 줄은 31행이다. !NCF를 제거하는 줄은 switch.pl 102행이다. srclistnc 선택과 Fortran 링크는 src/CMakeLists.txt 104·108행이다. [10-13 결론 검증 보완] |
