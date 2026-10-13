---
title: "swan nesting io implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "2026-10-13 recovery 반영분을 검증했다. 작업 시작 시 git diff -U0 HEAD의 추가·수정 24줄을 현재 코드, 과거 커밋 원문, PDF 및 대조 보고서 최종 판정과 대조했다." # [10-13 전수 검증 정정]
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
last_source_check: "2026-10-13 (recovery 대조 반영)"
---

# SWAN nesting I/O — NESTOUT writer, BOUND NEST reader, format checks

## Scope note

How a coarse SWAN run writes a nest file (`NESTOUT`) and how the receiving fine-grid run reads it back (`BOUND NEST` → `BCFILE` → runtime `RBFILE`). Includes spectrum format remapping (`CHGBAS`), error/warning emission paths for malformed or short files.

Companion to `swan-boundary-implementation.md` (covers `SWBOUN` body in general; this note focuses on the NEST-specific path end-to-end).

## Source basis

Codex deep scan 2026-05-06 of `swanpre2.ftn` (NESTOUT parser, NGRID setup, BCFILE), `swanout1.ftn`/`swanout2.ftn` (writer side), `swanmain.ftn` (runtime read + injection), `swanser.ftn` (`WRSPEC` ASCII writer).

## A. NESTOUT command parsing

In the output-request parser:
- `[file=src/swanpre2.ftn line=1984]` — `IF (KEYWIS('NEST'))` enters the `NESTout 'sname' 'fname'` block
- `[file=src/swanpre2.ftn line=2002]` — `SWNMPS` resolves `'SNAME'` to a defined point set; checks type `N` (nest) at `[file=src/swanpre2.ftn line=2004]`
- `[file=src/swanpre2.ftn line=2017]` — filename via `INCSTR('FNAME', FILENM, 'REQ', ' ')`
- `[file=src/swanpre2.ftn line=2026, 2028]` — output-request bookkeeping: `OQI(1) = NREF` (unit placeholder), `OUTP_FILES(NREOQ) = FILENM`

FOR의 UF는 UNKNOWN 상태와 FORMATTED 형식이다. (`src/ocpmix.ftn:1799` `IS  = INDEX('ONSU',S)`; `src/ocpmix.ftn:1800` `IFO = INDEX('FU',F)`; `src/ocpmix.ftn:1778–1779`.)

같은 실행에서 이미 연 파일은 기존 unit을 재사용한다. `src/ocpmix.ftn:1842–1847`의 `IF (OPENED) THEN` 분기는 `IUNIT = IUTTM` 뒤에 반환한다. 기존 디스크 파일에 무조건 append한다고 보장하는 규약은 아니다. `src/ocpmix.ftn:1869–1873`의 OPEN은 `STATUS=FISTAT(IS),ACCESS='SEQUENTIAL',FORM=FORM(IFO)`를 지정한다. [10-13 전수 검증 보완]

## B. NESTOUT runtime writer

- `[file=src/swanout1.ftn line=477]` — `RTYPE='SPRC'` dispatches to `CALL SWSPEC(...)` (NESTOUT's writer)
- `[file=src/swanout2.ftn line=1895]` to `[file=src/swanout2.ftn line=2001]` — on first call (`NREF == 0`), `SWSPEC` writes the **header**: TIME, LOCATIONS, FREQ grid, DIR grid, QUANT (quantity metadata)
- `[file=src/swanout2.ftn line=2005]` — each subsequent write emits the current time block (`CHTIME`) for nonstat runs
- `[file=src/swanout2.ftn line=2024]` to `[file=src/swanout2.ftn line=2075]` — per-time-step loop over locations writes spectra:
  - 2D spectrum → `WRSPEC` (full directional×frequency)
  - 1D spectrum → `LOCATION` line + per-frequency entries
- FOR의 UF는 UNKNOWN 상태와 FORMATTED 형식이다. (`src/ocpmix.ftn:1778–1779`; `src/ocpmix.ftn:1799` `IS  = INDEX('ONSU',S)`; `src/ocpmix.ftn:1800` `IFO = INDEX('FU',F)`.) [10-13 전수 검증 보완]
- WRSPEC이 쓰는 ASCII 밀도 표는 NINT로 반올림한다. (`src/swanser.ftn:5575` `WRITE (NREF, FIX_SPEC) (NINT(ACLOC(ID,IS)/EFAC), ID=1,MDC)`.) [10-13 전수 검증 정정]

## C. NGRID command setup (output grid)

- `[file=src/swanpre2.ftn line=794, 803]` — `NGRID 'SNAME'` parsing
- Structured nest case: rectangle parameters + 4-side discretization at `[file=src/swanpre2.ftn line=901-958]` produces boundary points
- Unstructured case: extracts boundary vertices from mesh markers (`VM /= 0`) at `[file=src/swanpre2.ftn line=963-973]`
- Runtime validation: `SPRCON` validates N-grid points against computational grid via `SINUPT` at `[file=src/swanmain.ftn line=4609-4637]`

## D. BOUND NEST reader on fine grid

- `BOUNDNEST` (`NE`) command path calls `BCFILE(FILENM, 'NEST', ...)` at `[file=src/swanpre2.ftn line=2943, 2988]`
- `BCFILE` reads header/type/locations/freq/dir at `[file=src/swanpre2.ftn line=4078-4352]`; metadata stored in `BFILED` + spectral axis arrays
- Runtime read each step via `RBFILE` at `[file=src/swanmain.ftn line=6916, 7469]`
- `TIMCO` matching: explicit at `[file=src/swanmain.ftn line=7724, 7781, 8034]` — reader advances until `TIMCO <= TIMF2`, then linearly interpolates between `TIMF1` and `TIMF2`

## E. Spectrum format identity check (does fine grid require exact match?)

**No exact match required** — SWAN remaps via `CHGBAS`:
- Direction grid: `CHGBAS(BSPDIR → SPCDIR)` at `[file=src/swanmain.ftn line=8451]`
- Frequency grid: `CHGBAS(BSPFRQ → SPCSIG)` at `[file=src/swanmain.ftn line=8482]`

SET FREQ·SET DIR·SET TIMEFORMAT은 지원하는 명령문이 아니다. 주파수와 방향의 스펙트럼 격자는 CGRID에서 지정한다. (`src/swanpre1.ftn:1730` `CALL ININTG('MDC',MDC,'RQI',0)`; `src/swanpre1.ftn:1739` `CALL INREAL('FLOW',FRLOW,'STA',-999.)`; `src/swanpre1.ftn:1740` `CALL INREAL('FHIGH',FRHIG,'STA',-999.)`; `2980d1a:src/swanpre1.ftn:2123–2166`; 현재 SET 분기 `src/swanpre1.ftn:2169–2213`.) [R4:T1-300](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론). [10-13 전수 검증 보완]

### Above-highest-frequency tail

When the boundary file's highest frequency is below the fine grid's, SWAN extrapolates with the diagnostic high-frequency tail (`PWTAIL`):
- Tail extrapolation at `[file=src/swanmain.ftn line=8458]` to `[file=src/swanmain.ftn line=8496]`
- Truncation detection at `[file=src/swanmain.ftn line=8458-8464]`
- Tail fill at `[file=src/swanmain.ftn line=8494-8496]`

**No hard error** when fine grid extends above coarse grid's frequency range. The user sees this only if they analyze the high-frequency tail of the fine result.

## F. Pitfalls visible in the code

| Symptom | Code path | Behavior |
|---------|-----------|----------|
| Nest freq range narrower than fine grid | `[file=src/swanmain.ftn line=8458-8464]` truncation detect; `[file=src/swanmain.ftn line=8494-8496]` power-law tail fill | **No hard error** — silently extrapolates with `PWTAIL` |
| Nest TIME range too short for full fine-grid run | `[file=src/swanmain.ftn line=8019]` "data on boundary file exhausted" warning; `[file=src/swanmain.ftn line=8022]` marks `BFILED(1) = -1`; subsequent calls skip updates `[file=src/swanmain.ftn line=7695]` | Continues with last known spectrum; **no fail** |
| Malformed file / short read | `[file=src/swanmain.ftn line=8508]` 'read error', `[file=src/swanmain.ftn line=8514]` 'insufficient data' | Error message but run continues with partial data |
| Not a true nesting file / no boundary points | Header parse errors at `[file=src/swanpre2.ftn line=4168, 4177, 4199]` | Runtime error; user sees in PRINTF |

So **time-range exhaustion silently propagates the last spectrum** — the receiving run does NOT fail. Watch for "exhausted" warnings in the log output.

## Decision Guide

| Concern | Action |
|---------|--------|
| 주파수와 방향의 스펙트럼 격자 | CGRID에서 지정한다. (`src/swanpre1.ftn:1730` `CALL ININTG('MDC',MDC,'RQI',0)`; `src/swanpre1.ftn:1739` `CALL INREAL('FLOW',FRLOW,'STA',-999.)`; `src/swanpre1.ftn:1740` `CALL INREAL('FHIGH',FRHIG,'STA',-999.)`; `src/swanpre1.ftn:1741` `CALL ININTG('MSC',MSS,'STA',-999)`.) [10-13 전수 검증 보완] |
| Worried about high-frequency cutoff in fine | extend coarse run's frequency range OR accept tail extrapolation |
| Coarse run shorter than fine simulation | run coarse for at least `[fine_start, fine_end]` |
| Multiple fine grids inside one coarse | one `NESTOUT` per fine grid (define separate `NGRID` per fine) |

## Working Rules

1. FOR의 UF는 UNKNOWN 상태와 FORMATTED 형식이다. (`src/ocpmix.ftn:1778–1779`; `src/ocpmix.ftn:1799` `IS  = INDEX('ONSU',S)`; `src/ocpmix.ftn:1800` `IFO = INDEX('FU',F)`.) [10-13 전수 검증 보완]
2. **`CHGBAS` remap is automatic** — no warning if grids differ. Inspect `BSPFRQ` and `SPCSIG` headers for any quality concerns.
3. **TIMCO matching is anchored at run start** — if you change `COMPUTE NONSTAT` start time between coarse and fine, the reader still advances until `TIMCO ≤ TIMF2`. Mismatch silently uses earliest available time.
4. **Time exhaustion = silent failure mode** — set up monitoring on the log file for "data on boundary file exhausted" messages.
5. NGRID must be defined **before** referencing it in `NESTOUT`.

## Common Pitfalls

- **Time exhaustion** — coarse run ends earlier than fine-grid simulation: the fine run continues with the last spectrum (no error). Always log-check.
- **Spectral grid mismatch silent quality loss** — re-running coarse with fine's spectral grid is cheap insurance for validation work.
- FOR의 UF는 UNKNOWN 상태와 FORMATTED 형식이다. (`src/ocpmix.ftn:1778–1779`; `src/ocpmix.ftn:1799` `IS  = INDEX('ONSU',S)`; `src/ocpmix.ftn:1800` `IFO = INDEX('FU',F)`.) [10-13 전수 검증 보완]
- **NGRID after NESTOUT** in command file — parser fails, but error is unspecific.
- 같은 실행에서 이미 연 파일은 기존 unit을 재사용한다. 기존 디스크 파일에 무조건 append한다고 보장하는 규약은 아니다. (`src/ocpmix.ftn:1842–1847`의 `IF (OPENED) THEN` 및 `IUNIT = IUTTM`; `src/ocpmix.ftn:1869–1873`의 OPEN 지정자.) [10-13 전수 검증 보완]

## References

- `src/swanpre2.ftn` — `NESTOUT` parser, `NGRID` setup, `BCFILE` (NEST reader header).
- `src/swanout1.ftn` — `SWORDC` dispatch to `SWSPEC`.
- `src/swanout2.ftn` — `SWSPEC` writer body, time block writes.
- `src/swanmain.ftn` — `RBFILE` runtime read, `CHGBAS` remap, exhaustion handling.
- `src/swanser.ftn` — `WRSPEC` ASCII writer.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex scan | 30+ file:line citations |
| Coverage | NESTOUT writer (header + per-time block), BOUND NEST reader, NGRID setup, CHGBAS remapping, exhaustion/error paths |
| Review status | `review_required: true` |

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD `43e9bbb` (2026-07-13 patch B). (`src/swanmain.ftn:965` `VERNUM = 41.51`.)

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R6:O-010 | NGRID 원점·각도 설명 | swanuse PDF 101쪽 / 인쇄 93쪽: `[xpn] geographic location of the origin of the computational grid of this coarse-grid run`. `[alpn]`에도 `of this coarse-grid run`이라고 쓴다. | `src/swanpre2.ftn:929` `XF=XPCN`. `src/swanpre2.ftn:930` `YF=YPCN`. `src/swanpre2.ftn:936` `ANGLE=ANG+PI2*(90.*REAL(I-1))/360.`. `src/swanpre2.ftn:947` `OPSTMP%XP(MIP)=XI+REAL(KK)*(XF-XI)/REAL(INTE)`. | B 문서 오기 | NGRID의 XPN·YPN·ALPN은 생성할 중첩 경계의 원점과 방향을 지정한다. |
| R6:O-011 | NGRID UNSTRUCTURED 파일 | swanuse PDF 102쪽 / 인쇄 94쪽: `The .node and .ele files are required.` Easymesh에는 `The .n and .e files are required.` | `src/swanpre2.ftn:815` `FILENM = TRIM(BASENM)//'.n'`. `src/swanpre2.ftn:851` `FILENM = TRIM(BASENM)//'.node'`. `src/swanpre2.ftn:963` `MIP = COUNT(MASK=VM/=0)`. | B 문서 오기 | NGRID UNSTRUCTURED는 Triangle의 .node 또는 Easymesh의 .n에서 경계 정점을 읽는다. 요소 파일은 이 명령이 읽지 않는다. |
| R6:O-012 | NGRID EASYMESH 정점 읽기 | swanuse PDF 102쪽 / 인쇄 94쪽: EASYMESH: `the necessary grid information is read from two files as produced by Easymesh.`. | `src/swanpre2.ftn:838` `DO KK = 1, NVTX`. `src/swanpre2.ftn:839` `READ(NDS, 100, END=950, ERR=910) XG(I),YG(I),VM(I)`. `src/swanpre2.ftn:1008` `100  FORMAT((6X,2E22.15,I3))`. 884행의 Triangle 경로는 `READ(NDS, *, END=950, ERR=910) I,XG(I),YG(I),VM(I)`이다. git 원문: `b2ae30e:src/swanpre2.ftn:839`에 같은 READ가 있다. `7ee8981`과 `43e9bbb`에도 유지된다. `src/swanpre2.ftn:794–811`의 NGRID·UNSTRUCTURED·EASYMESH 입력으로 도달하며 전처리 표식이 없다. [SWAN-git-verify-E](../../../_staging/recovery/compare/SWAN-git-verify-E.md)의 확정 판정은 E 유지(강함)이다. | E 코드 결함 후보 (강함) | NGRID EASYMESH는 KK를 증가시키면서 XG(I), YG(I), VM(I)에 저장한다. `100  FORMAT((6X,2E22.15,I3))`은 정점 번호 칸을 건너뛰므로 I에 번호를 대입하지 않는다. Triangle 경로는 같은 READ에서 I를 먼저 읽는다. 정점 배열 인덱스의 강한 정적 결함 후보이다. [10-13 결론 검증 보완] [10-13 git 이력 판정] |
| R6:O-028 | NESTOUT의 밀도 명칭 | swanuse PDF 96쪽 / 인쇄 88쪽: `two-dimensional action density spectra (relative frequency)`. swanuse PDF 118쪽 / 인쇄 110쪽은 Appendix D 형식을 지정한다. | `src/swanpre2.ftn:2015` `RTYPE  = 'SPRC'`. `src/swanout2.ftn:1965`의 SWSPEC 원문은 `WRITE (NREF, 102) 'EnDens',`이다. `src/swanout2.ftn:1971`의 SWSPEC 원문은 `WRITE (NREF, 102) 'VaDens',`이다. SWCMSP는 `src/swanout2.ftn:2277`의 `ECLL = OFAC * ACLL * SPCSIG(ISIGM)`으로 밀도값을 계산한다. 단위 변환은 [R6:O-100](../../../_staging/recovery/compare/swan-outputs-vs-code.md#25-appendix-d와-스펙트럼-읽기쓰기)에 있다. | B 문서 오기 | NESTOUT은 상대 주파수의 2D 분산 밀도 또는 에너지 밀도를 기록한다. 내부 파작용 밀도를 그대로 기록하지 않는다. [10-13 전수 검증 정정] |
| R6:N-009 | FOR의 UF와 파일 재사용 | 수정 전 노트의 33행(이번 git diff의 삭제 줄): `'UF' = "unformatted"`. 수정 전 노트의 110행: `Multiple NESTOUT to same file — appends not overwrites`. | `src/ocpmix.ftn:1799` `IS  = INDEX('ONSU',S)`. `src/ocpmix.ftn:1800` `IFO = INDEX('FU',F)`. 1778행은 상태 UNKNOWN을 등록한다. 1779행은 FORMATTED를 등록한다. `src/ocpmix.ftn:1842–1847`의 `IF (OPENED) THEN` 분기는 `IUNIT = IUTTM` 뒤에 반환한다. `src/ocpmix.ftn:1869–1873`은 OPEN 지정자를 제시한다. | B 문서 오기 | FOR의 UF는 UNKNOWN 상태와 FORMATTED 형식이다. 같은 실행에서 이미 연 파일은 기존 unit을 재사용한다. 기존 디스크 파일에 무조건 append한다고 보장하는 규약은 아니다. [10-13 전수 검증 정정] |
