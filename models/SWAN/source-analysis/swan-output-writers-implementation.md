---
title: "swan output writers implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "2026-10-13 HEAD 대비 추가·수정 41줄을 R6·R8 최종 보고서, git 판정 D·E, 현재·과거 코드, 웹 HTML, swanuse PDF 98·109·114–117쪽에 대조했다." # [10-13 전수 검증 정정]
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
last_source_check: "2026-10-13 (recovery 대조 반영)"
---

# SWAN output writers — SWBLOK, SWTABP, SWSPEC internals

## Scope note

Code-level walk-through of how SWAN writes block (BLOCK), table (TABLE), and spectral (SPECout, NESTout) outputs. Includes integer-encoded factor format, format-flag dispatch, derived-quantity computation from `AC2`, and file pointer management.

Companion to `swan-command-file-reference.md` (covers output command syntax) and `swan-nesting-io-implementation.md` (covers NESTout specifically).

## Source basis

Codex deep scan 2026-05-06 of `models/swan/source_code/swan/src/swanout1.ftn`, `swanout2.ftn`, `swanser.ftn`.

## A. SWORDC + SWOUTP dispatcher

- `SWORDC` at `[file=src/swanout1.ftn line=527]` decodes request metadata (`NVOQP`, `VOQR`, `OQPROC`, time gating via `OUTR(1:2)`) but does NOT call writer backends itself.
- `SWOUTP` at `[file=src/swanout1.ftn line=435-509]` is the runtime dispatcher.

### Routing by RTYPE

`[file=src/swanout1.ftn line=436-447]`: `RTYPE(1:3) == 'BLK'` → `SWBLOK / SWBLKP / SWBLKV`
일반 TABLE은 SWTABP를 쓴다. -netcdf 빌드의 병렬 TABC는 SWBLKP에 중간 출력을 맡긴다. (`src/swanout1.ftn:454` `IF (RTYPE(1:3) .EQ. 'TAB') THEN`; `src/swanout1.ftn:455` `!NCF          IF (PARLL.AND.(RTYPE.EQ.'TABC')) THEN`; `src/swanout1.ftn:457` `!NCF             CALL SWBLKP ( CORQ%OQI, CORQ%IVTYP, MIP, 1, VOQR,`.)
`[file=src/swanout1.ftn line=469-503]`: `RTYPE(1:2) == 'SP'` → `SWSPEC`

### Spectral subtype routing

일반 ABS 2D 요청은 SPEC이다. 일반 REL 2D 요청은 SPRC이다. 마지막 C는 이 구현에서 2D 분기를 선택한다. Cartesian 방향 규약을 뜻하지 않는다. (`src/swanpre2.ftn:1890` `RTYPE  = 'SPEC'`; `src/swanpre2.ftn:1894` `RTYPE(3:3)  = 'R'`; `src/swanout2.ftn:1944` `IF (RTYPE(4:4).EQ.'C') THEN`.)

ASCII ABS L은 SPBC 또는 SPB1로 저장된다. 머리말은 AFREQ이지만 값 계산에는 상대 주파수용 양의 OTYPE을 넘긴다. (`src/swanpre2.ftn:1904` `RTYPE(3:3) = 'B'`; `src/swanout2.ftn:2011` `IF (RTYPE.EQ.'SPEC') THEN`; `src/swanout2.ftn:2014` `OTYPE = 2`.)

NetCDF REL L은 세 번째 문자가 L이므로 relative를 참으로 설정하지 못한다. 기본 relative=false가 유지되어 절대 주파수용 음의 OTYPE을 선택한다. (`src/swanpre2.ftn:1902` `RTYPE(3:3) = 'L'`; `src/swn_outnc.ftn90:608` `if (RTYPE(3:3) .eq. 'R') lspcaux%relative = .true.`; `src/swn_outnc.ftn90:680` `otype = -2`.)

Character-test routing (instead of full string switch) is used throughout.

## B. SWBLOK (BLOCK output)

- Subroutine: `[file=src/swanout2.ftn line=18]`
- Output mode by `RTYPE`: `'BLKP'/'BLKD'/else` → `IPD = 1/2/3` at `[file=src/swanout2.ftn line=163-172]`

### 실수 형식과 자동 배율

일반 BLOCK는 SBLKPT의 실수 형식으로 기록한다. HEADER는 기본 F6.4를 사용한다. NOHEADER는 기본 6E12.4를 사용한다. HEADER의 자동 배율은 보통 OVHEXP에서 정한다. (`src/swanout2.ftn:483` `CHARACTER (LEN=21) :: WFORM2 = '(1X,I4,1X, 151(F6.0))'`; `src/swanout2.ftn:535` `WRITE (WFORM2(17:17), '(I1)') DEC_BLOCK`; `src/swanout2.ftn:254` `IFAC = INT (10.+LOG10(OVHEXP(IVTYPE))) - 13`.) 기본 형식의 초기값은 `src/swmod2.ftn:212`의 `FLT_BLOCK = '(6E12.4)'`와 `src/swmod2.ftn:220`의 `DEC_BLOCK = 4`이다. [10-13 전수 검증 보완]

FACTOR와 정수 밀도 표는 2D 스펙트럼 형식으로 분리해 설명한다. (`src/swanser.ftn:5575` `WRITE (NREF, FIX_SPEC) (NINT(ACLOC(ID,IS)/EFAC), ID=1,MDC)`.)

### Per-quantity write loop

`[file=src/swanout2.ftn line=246-349]`:
- `DO JVAR = 1, NVAR`
- Scalar vs vector branch at `[file=src/swanout2.ftn line=285]`, `[file=src/swanout2.ftn line=307]`
- Each field written via `SBLKPT` at `[file=src/swanout2.ftn line=304-305]`, `[file=src/swanout2.ftn line=340-345]`

### SBLKPT의 머리말

BLOCK HEADER의 첫 x 묶음 앞에는 9행이 있다. 기본 자료 형식은 F6.4이다. 자동 배율은 통상 실제 최댓값 대신 OVHEXP를 사용한다. (`src/swanout2.ftn:514–544`의 데이터 전 WRITE; `src/swanout2.ftn:253` `IF (OVHEXP(IVTYPE) .LT. 0.5E10) THEN`; `src/swanout2.ftn:254` `IFAC = INT (10.+LOG10(OVHEXP(IVTYPE))) - 13`; swanuse PDF 109쪽 / 인쇄 101쪽, PDF 114쪽 / 인쇄 106쪽.)

비정상 HEADER BLOCK의 시각은 물리량 또는 벡터 성분의 블록마다 기록한다. 출력 점마다 기록하는 구조가 아니다. (`src/swanout2.ftn:246` `DO JVAR = 1, NVAR`; `src/swanout2.ftn:304` `CALL SBLKPT(IPD, NREF, DFAC, PSNAME, OVUNIT(IVTYPE),`.)

## C. SWTABP (TABLE output)

- Subroutine: `[file=src/swanout2.ftn line=1172]`

### Format branches

| `RTYPE` | Format | file:line |
|---------|--------|-----------|
| `TABD` | NOHEADER | `[file=src/swanout2.ftn line=1405]` |
| `TABP` | HEADER (legacy print) | `[file=src/swanout2.ftn line=1410]` |
| `TABI` | HEADER + indexed first column | `[file=src/swanout2.ftn line=1410]` + `[file=src/swanout2.ftn line=1419-1425]`, `[file=src/swanout2.ftn line=1564-1569]` |
| `TABT` | SWAN standard | `[file=src/swanout2.ftn line=1480]` |
| `TABS` | SWAN standard with site metadata | same; quantity-definitions at `[file=src/swanout2.ftn line=1481-1533]` |

### Per-point loop

`[file=src/swanout2.ftn line=1560-1604]`:
- `DO IP = 1, MIP`
- Each quantity formatted and appended per row
- Special time-quantity handling when `IVTYPE == 40` at `[file=src/swanout2.ftn line=1572-1577]`

So `TABLE 'STATIONS' SWAN 'fname' HSIGN PER` goes through the `TABT/TABS` branch with quantity-definitions header.

## D. SWSPEC (SPECout writer)

- Subroutine: `[file=src/swanout2.ftn line=1719]`
- 2D vs 1D split on `RTYPE(4:4) == 'C'`:
  - 2D header: `[file=src/swanout2.ftn line=1944-1976]`
  - 1D header: `[file=src/swanout2.ftn line=1976-2000]`
  - 2D write: `WRSPEC` at `[file=src/swanout2.ftn line=2057-2059]`
  - 1D write: triplets at `[file=src/swanout2.ftn line=2060-2071]`

### `WRSPEC` (the actual integer-encoded spectrum writer)

- Subroutine: `[file=src/swanser.ftn line=5448]`
- Computes max amplitude `[file=src/swanser.ftn line=5553-5563]`
- If tiny: emit `'ZERO'` at `[file=src/swanser.ftn line=5564-5566]`
- Else: emit `'FACTOR'` with scaled physical factor at `[file=src/swanser.ftn line=5568-5572]`
- Integerize bins via `NINT(ACLOC(ID,IS) / EFAC)` at `[file=src/swanser.ftn line=5575]`

### `FACTOR` normalization

`[file=src/swanser.ftn line=5568]`:
```
EFAC = 1.01 * max * 10**(-DEC_SPEC)
```
Then written as `EFAC * 2 * PI**2 / 180` at `[file=src/swanser.ftn line=5571]` to convert radian-based density to Hz/degree convention for the file.

노트의 요약에도 전체 배율 EFAC×2π²/180을 적어 단위 변환을 명확히 한다. (`src/swanser.ftn:5571` `WRITE (NREF, 95) EFAC * 2. * PI**2 / 180.`.)

## E. Quantity computation from `AC2`

- Derived wave quantities computed in `SWOEXA` at `[file=src/swanout1.ftn line=3194]`
- Local spectrum `ACLOC` interpolated from `AC2` at `[file=src/swanout1.ftn line=3438-3460]`

### HSIGN

- `IVTYPE = 10` (HSIGN)
- Computation: integrate spectral energy density, then `Hs = 4 * sqrt(ETOT)` at `[file=src/swanout1.ftn line=3482-3512]`
- Exact assignment line: `[file=src/swanout1.ftn line=3511]`

### Peak period (RTPEAK)

- Simple peak: `IVTYPE = 12` at `[file=src/swanout1.ftn line=3752-3768]`
- Parabolic-fit peak: `IVTYPE = 53` at `[file=src/swanout1.ftn line=3775-3818]`
- Both use `2π / σ_peak`

So `HSIGN`, `RTPEAK`, `PER` (mean period), `DIR` (mean direction), etc., are all derived from `AC2` per output point inside `SWOEXA`. The user's command file lists these by name (`HSIGN PER DIR`); SWAN looks up `IVTYPE` and dispatches to the appropriate computation.

## F. Time-stamped output and file pointer management

### When `CHTIME` is written

- BLOCK: each `SBLKPT` call writes the time at `[file=src/swanout2.ftn line=521-524]`
- TABLE TABS: time written once before point loop at `[file=src/swanout2.ftn line=1557-1559]`
- SPEC: time written once per call at `[file=src/swanout2.ftn line=2005-2007]`

비정상 HEADER BLOCK의 시각은 물리량 또는 벡터 성분의 블록마다 기록한다. 스펙트럼 파일의 비정상 시각은 각 출력 호출의 지점별 스펙트럼 자료 앞에 한 번 기록한다. (`src/swanout2.ftn:246` `DO JVAR = 1, NVAR`; `src/swanout2.ftn:2005–2007`의 시각 WRITE.)

### File open / append behavior

"Open once when `NREF == 0`, then reuse unit in `OQI(1)`":
- BLOCK: `[file=src/swanout2.ftn line=183-189]`
- TABLE: `[file=src/swanout2.ftn line=1384-1396]`
- SPEC: `[file=src/swanout2.ftn line=1895-1902]`

같은 실행에서 이미 연 파일은 기존 unit을 재사용한다. 기존 디스크 파일에 무조건 append한다고 보장하는 규약은 아니다. (`src/ocpmix.ftn:1799` `IS  = INDEX('ONSU',S)`; `src/ocpmix.ftn:1800` `IFO = INDEX('FU',F)`.) unit 재사용은 `src/ocpmix.ftn:1842–1847`의 `IF (OPENED) THEN` 분기에서 `IUNIT = IUTTM`으로 처리한다. `src/ocpmix.ftn:1869–1873`의 OPEN에는 append 위치 지정이 없다. [10-13 전수 검증 보완]

### Explicit rewrite (only special paths)

MATLAB block output reopens with `STATUS='REPLACE'` at `[file=src/swanout2.ftn line=191-193]`. Normal text outputs are not reopened each timestep.

## Decision Guide

| Need | Use |
|------|-----|
| ASCII 격자 출력 | `BLOCK`의 실수 형식. HEADER는 기본 F6.4이다. NOHEADER는 기본 6E12.4이다. |
| Time series at fixed stations | `TABLE` (one row per time per point) |
| Frequency × direction spectrum at points | `SPECOUT SPEC2D` |
| 1D frequency-only spectrum | `SPECOUT SPEC1D` |
| Boundary file for fine-grid nest | `NESTOUT` (covered separately) |

## Working Rules

1. 2D 스펙트럼의 축척 밀도는 NINT로 반올림한다. (`src/swanser.ftn:5575` `WRITE (NREF, FIX_SPEC) (NINT(ACLOC(ID,IS)/EFAC), ID=1,MDC)`.)
2. **`HEADER` vs `NOHEADER`** affects file size, not content. Use `NOHEADER` for downstream scripts that consume only data rows.
3. **Spectrum file `FACTOR` includes `2π²/180` conversion** — to extract m²/(Hz·deg), multiply integer by `FACTOR`.
4. 같은 실행에서 이미 연 파일은 기존 unit을 재사용한다. 기존 디스크 파일에 무조건 append한다고 보장하는 규약은 아니다. (`src/ocpmix.ftn:1799–1800` `IS  = INDEX('ONSU',S)`, `IFO = INDEX('FU',F)`.) unit 재사용 근거는 `src/ocpmix.ftn:1842–1847`의 `IUNIT = IUTTM`이다. `src/ocpmix.ftn:1869–1873`의 OPEN에는 append 위치 지정이 없다. [10-13 전수 검증 보완]
5. **`HSIGN = 4*sqrt(ETOT)`** is the canonical formula; ensure your downstream comparison computes Hs the same way.

## Common Pitfalls

- Forgetting to apply `FACTOR` when reading SWAN output — values look 1000× off.
- **`TABLE TABD` (no header)** consumed by a script expecting headers — silent column shift.
- **`SPECOUT SPEC1D` written with `RTYPE='SPRE'`** vs `'SPRC'` (2D) — different column layout.
- 스펙트럼 파일의 비정상 시각은 각 출력 호출의 지점별 스펙트럼 자료 앞에 한 번 기록한다. (`src/swanout2.ftn:2005–2007`의 시각 WRITE.)

## References

- `src/swanout1.ftn` — `SWOUTP` dispatcher, `SWORDC`, `SWOEXA` quantity computation.
- `src/swanout2.ftn` — `SWBLOK`, `SBLKPT`, `SWTABP`, `SWSPEC`.
- `src/swanser.ftn:5448` — `WRSPEC`.
- `src/swanser.ftn` — `WRSPEC` actual integerized spectrum writer.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex scan | 30+ file:line citations |
| Coverage | dispatcher, BLOCK, TABLE, SPEC writers, HSIGN/RTPEAK computation, file pointer policy |
| Review status | `review_required: true` |

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD `43e9bbb` (2026-07-13 patch B). (`src/swanmain.ftn:965` `VERNUM = 41.51`.)

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R6:O-020 | BLOCK HEADER 행 수·정밀도·자동 배율 | swanuse PDF 109쪽 / 인쇄 101쪽: `The number of header lines is 8.` swanuse PDF 114쪽 / 인쇄 106쪽: `value is written as a 5 position integer.` `the largest number occurring in the block`. | `src/swanout2.ftn:253–254` `IF (OVHEXP(IVTYPE) .LT. 0.5E10) THEN`, `IFAC = INT (10.+LOG10(OVHEXP(IVTYPE))) - 13`. `src/swanout2.ftn:483` `CHARACTER (LEN=21) :: WFORM2 = '(1X,I4,1X, 151(F6.0))'`. `src/swanout2.ftn:535` `WRITE (WFORM2(17:17), '(I1)') DEC_BLOCK`. 514–544행은 시각 분기의 WRITE 중 하나를 선택하여 첫 x 묶음의 자료 앞에 9행을 기록한다. | B 문서 오기 | BLOCK HEADER의 첫 x 묶음 앞에는 9행이 있다. 기본 자료 형식은 F6.4이다. 자동 배율은 통상 실제 최댓값 대신 OVHEXP를 사용한다. [10-13 전수 검증 정정] |
| R6:O-024 | TABLE 머리말·파일명 | swanuse PDF 115쪽 / 인쇄 107쪽: `Number of header lines is 4.` `In case of NOHEADER the filename is required.` | `src/swanout2.ftn:1411–1417`에 WRITE 4번이 있다. 1445행과 1478행은 물리량 이름·단위를 쓴다. `src/swanout2.ftn:1479` `WRITE (NREF, 20) OUT_COMMENT`. `src/swanpre2.ftn:1606` `CALL INCSTR ('FNAME', FILENM, 'STA', ' ')`. `src/swanpre2.ftn:1621` `NREF = PRINTF`. | B 문서 오기 | TABLE HEADER는 이름·단위·빈 행을 포함해 7행을 쓴다. NOHEADER에서도 파일명을 생략하면 PRINT를 사용한다. |
| R6:O-025 | INDEXED 마지막 END | swanuse PDF 115쪽 / 인쇄 107쪽: `is the sequence number of the output point.`. `The last line of each file is the word END.` | `src/swanout2.ftn:1566` `WRITE (OUTLIN(1:8), '(I8)') IP`. `src/swanout2.ftn:1602` `WRITE (NREF, '(A)') OUTLIN(1:LINKAR-1)`. `src/swanout2.ftn:1606` `RETURN`. git 원문: `2980d1a:src/swanout2.ftn:1561,1597,1601`은 점 번호·자료 출력 뒤 RETURN이다. `2980d1a..43e9bbb`에서 END 문자열 추가·TABI 변경을 찾는 git 검색은 0커밋이다. 병렬 수집은 `src/swanparll.ftn:4561,4567–4610`에도 END 기록이 없다. [SWAN-git-verify-D](../../../_staging/recovery/compare/SWAN-git-verify-D.md)의 확정 판정은 D이다. | D 문서에만 있음 | INDEXED는 첫 열에 출력점 번호를 기록한다. 조사한 41.45 공개 커밋 `2980d1a`부터 `43e9bbb`까지 구현은 파일 끝에 END 행을 기록하지 않는다. [10-13 결론 검증 보완] [10-13 git 이력 판정] |
| R6:O-034 | 출력 위치 보간 | swanuse PDF 98쪽 / 인쇄 90쪽: `The values of the output quantities along the curve are interpolated from the computational grid.` | `src/swanout1.ftn:3439` `CALL SWOINA (XC(IP), YC(IP), AC2, ACLOC, KGRPNT, DEPXY,`. `src/swanout1.ftn:3459` `ACLOC(:,:) = AC2(:,:,IP)`. `src/SwanInterpolateAc.ftn90:275` `ww(k) = 0.`. `src/SwanInterpolateAc.ftn90:289` `if (obstcell) ww(k) = ww(k) / sumww`. `src/SwanInterpolateAc.ftn90:290` `acintp(:,:) = acintp(:,:) + ww(k) * ac2(:,:,v(k))`. `src/SwanInterpolateOutput.ftn90:308` `foutp(ip) = sum (ww(:) * finp(v(:)))`. swanuse §2.6.4의 [node12.html](../raw/manuals/website/online_doc/swanuse/node12.html):49–59는 출력 격자 보간과 바닥·흐름의 두 단계 보간을 설명한다. [modifications.htm](../raw/manuals/website/modifications/modifications.htm):573–575,1302–1306은 장애물을 가로지르는 보간 방지를 명시한다. | C 문서 누락 | Hs 등은 작용밀도를 보간한 뒤 적분한다. 저장된 수심·소산 등은 스칼라를 보간한다. 비구조 격자의 COMPGRID 요청은 정점값을 직접 쓴다. 출력 보간 자체와 장애물 횡단 방지는 문서에 있다. C는 swanuse 출력 절에 없는 적분·보간 순서, 삼각형 가중치의 0 처리와 재정규화 식에 한정한다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R6:O-110 | ABS L의 축과 값 | swanuse PDF 117쪽 / 인쇄 109쪽의 ABS/REL 선택과 L 선택. ABS는 `absolute frequency spectrum`이다. | `src/swanpre2.ftn:1904` `RTYPE(3:3) = 'B'`. `src/swanout2.ftn:1934` `IF (RTYPE(3:3).EQ.'R' .OR. RTYPE(3:3).EQ.'L') THEN`. 1937행은 AFREQ를 쓴다. `src/swanout2.ftn:2011` `IF (RTYPE.EQ.'SPEC') THEN`. `src/swanout2.ftn:2014` `OTYPE = 2`. 2017–2020행은 1D에도 같은 비교를 적용한다. `src/swanout1.ftn:470–479`에서 LSRFB가 거짓이면 L 요청도 AC2를 SWSPEC에 넘긴다. `src/swanout2.ftn:2279–2280`은 `IF (ICUR.EQ.0 .OR. OTYPE.GT.0`과 `&                                    ) THEN`으로 상대 주파수 경로를 고른다. git 원문 `b2ae30e:src/swanout2.ftn:2003`의 SPEC 전체 문자열 비교는 `7ee8981:src/swanout2.ftn:2007`과 `43e9bbb:src/swanout2.ftn:2011`에도 유지된다. [SWAN-git-verify-E](../../../_staging/recovery/compare/SWAN-git-verify-E.md)의 확정 판정은 E 유지(강함)이다. | E 코드 결함 후보 (강함) | ASCII ABS L은 SPBC 또는 SPB1로 저장된다. 머리말은 AFREQ이지만 값 계산에는 상대 주파수용 양의 OTYPE을 넘긴다. LSRFB가 거짓인 일반 스펙트럼 경로에서도 이 요청에 도달한다. 흐름이 있으면 축의 의미와 값 계산이 달라지는 강한 정적 결함 후보이다. 무흐름에서는 두 주파수가 같아 이 차이가 드러나지 않는다. NetCDF 출력은 별도 분기로 빠진다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] [10-13 git 이력 판정] |
| R6:O-112 | NetCDF REL L | swanuse PDF 116–117쪽 / 인쇄 108–109쪽는 REL과 L을 조합할 수 있게 제시한다. `.nc`는 NetCDF 출력이다. | `src/swanpre2.ftn:1902` `RTYPE(3:3) = 'L'`. `src/swn_outnc.ftn90:89` `logical                                  :: is2d = .false., relative = .false.`. `src/swn_outnc.ftn90:608` `if (RTYPE(3:3) .eq. 'R') lspcaux%relative = .true.`. `src/swn_outnc.ftn90:680` `otype = -2`. `src/swn_outnc.ftn90:687` `otype = -1`. `src/swanout2.ftn:1877–1885`는 `!NCF`가 활성화된 빌드에서 .nc/.NC 파일을 swn_outnc_spec으로 보낸다. `src/swanout1.ftn:470–479`은 LSRFB가 거짓인 L 요청도 이 writer에 연결한다. git 원문 `b2ae30e:src/swn_outnc.ftn90:614`의 R 전용 판별은 `7ee8981:src/swn_outnc.ftn90:608`과 `43e9bbb:src/swn_outnc.ftn90:608`에도 유지된다. [SWAN-git-verify-E](../../../_staging/recovery/compare/SWAN-git-verify-E.md)의 확정 판정은 E 유지(강함)이다. | E 코드 결함 후보 (강함) | NetCDF REL L은 세 번째 문자가 L이므로 relative를 참으로 설정하지 못한다. 기본 relative=false가 유지되어 절대 주파수용 음의 OTYPE을 선택한다. 일반 REL의 R 판별은 이 누락을 보정하지 않는다. -netcdf 빌드의 .nc 스펙트럼 요청에 적용하는 강한 정적 결함 후보이다. LSRFB가 거짓인 일반 경로에서도 도달한다. 흐름이 없으면 절대·상대 주파수의 수치 차이는 없다. [10-13 결론 검증 보완] [10-13 git 이력 판정] |
| R6:N-004 | 스펙트럼 내부 코드 | `models/SWAN/source-analysis/swan-output-writers-implementation.md:38`: `'SPRC' = "Spectrum Relative Cartesian (2D)", 'SPAC' = absolute 2D` | `src/swanpre2.ftn:1890` `RTYPE  = 'SPEC'`. `src/swanpre2.ftn:1894` `RTYPE(3:3)  = 'R'`. `src/swanout2.ftn:1944` `IF (RTYPE(4:4).EQ.'C') THEN`. | B 문서 오기 | 일반 ABS 2D 요청은 SPEC이다. 일반 REL 2D 요청은 SPRC이다. 마지막 C는 이 구현에서 2D 분기를 선택한다. Cartesian 방향 규약을 뜻하지 않는다. L의 SPBC·SPLC는 O-110·O-112의 예외를 함께 기록한다. |
| R6:N-005 | BLOCK와 스펙트럼 FACTOR 혼동 | `models/SWAN/source-analysis/swan-output-writers-implementation.md:56`: `So output value = (file integer) × DFAC.` 74행: `[QUANT]   [unit]   FACTOR=Xe-NN`. 76행: `(matrix of integers row by row)`.<br>swanuse PDF 109쪽 / 인쇄 101쪽: `The number of header lines is 8.` swanuse PDF 114쪽 / 인쇄 106쪽: `value is written as a 5 position integer.` `the largest number occurring in the block`. | O-020·O-021. `src/swanout2.ftn:483` `CHARACTER (LEN=21) :: WFORM2 = '(1X,I4,1X, 151(F6.0))'`. `src/swanout2.ftn:535` `WRITE (WFORM2(17:17), '(I1)') DEC_BLOCK`. | B 문서 오기 | 일반 BLOCK는 SBLKPT의 실수 형식으로 기록한다. HEADER는 기본 F6.4를 사용한다. NOHEADER는 기본 6E12.4를 사용한다. HEADER의 자동 배율은 보통 OVHEXP에서 정한다. FACTOR와 정수 밀도 표는 2D 스펙트럼 형식으로 분리해 설명한다. |
| R6:N-007 | 밀도 단위 변환 | `models/SWAN/source-analysis/swan-output-writers-implementation.md:127`: `there's a 2π² conversion baked into FACTOR.` | O-100. `src/swanser.ftn:5571` `WRITE (NREF, 95) EFAC * 2. * PI**2 / 180.`. 같은 노트 125행은 `EFAC * 2 * PI**2 / 180`을 정확히 적고 Hz/degree 변환이라고 설명한다. | F 표기 차이 | 노트 125행의 전체 배율은 writer와 일치한다. 127행의 2π²는 /180을 생략한 요약 표현이다. 이를 별개의 잘못된 구현식으로 읽은 B를 F로 고친다. 노트의 요약에도 전체 배율 EFAC×2π²/180을 적어 단위 변환을 명확히 한다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R6:N-008 | BLOCK 시각의 반복 단위 | `models/SWAN/source-analysis/swan-output-writers-implementation.md:156`: `one per file write per call vs one per point`. | `src/swanout2.ftn:246` `DO JVAR = 1, NVAR`. `src/swanout2.ftn:304` `CALL SBLKPT(IPD, NREF, DFAC, PSNAME, OVUNIT(IVTYPE),`. `src/swanout2.ftn:2004–2007`의 시각 WRITE는 2024행의 점 순회 앞에 있다. | B 문서 오기 | 비정상 HEADER BLOCK의 시각은 물리량 또는 벡터 성분의 블록마다 기록한다. 출력 점마다 기록하는 구조가 아니다. 스펙트럼 파일의 비정상 시각은 각 출력 호출의 지점별 스펙트럼 자료 앞에 한 번 기록한다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] [10-13 전수 검증 정정] |
| R8:N1-012 | TABLE의 병렬 netCDF 경로 | `source-analysis/swan-output-writers-implementation.md:33`은 `RTYPE(1:3) == 'TAB'`의 피호출을 SWTABP로만 적는다 | `src/swanout1.ftn:454` `IF (RTYPE(1:3) .EQ. 'TAB') THEN` 안의 `src/swanout1.ftn:455`은 `!NCF          IF (PARLL.AND.(RTYPE.EQ.'TABC')) THEN`이다. `src/swanout1.ftn:457–458`은 `!NCF             CALL SWBLKP ( CORQ%OQI, CORQ%IVTYP, MIP, 1, VOQR,`와 `!NCF     &                     VOQ(1), IONOD )`이다. `src/swanout1.ftn:460–462`은 그 밖의 SWTABP 호출이다. `switch.pl:102–103`은 -netcdf 선택에 따라 !NCF 또는 !NNCF를 활성화한다. | C 문서 누락 | 일반 TABLE은 SWTABP를 쓴다. -netcdf 빌드의 병렬 TABC는 SWBLKP에 중간 출력을 맡긴다. 코드 `src/swanout1.ftn:456`의 주석은 이 경로를 코어 사이 자료 전달용 중간 BLOCK 파일로 설명한다. C는 기존 노트의 분기표 누락에 한정한다. [10-13 결론 검증 보완] |
