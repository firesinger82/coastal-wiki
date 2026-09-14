---
title: "adcirc tide harmonic prep"
topic: tides
canonical_source: self
citation_status: verified
has_source_needed: true
evidence_extension_date: 2026-09-14
evidence_extension_by: "Codex — 입력 품질·검증 확인 방법 보강"
evidence_extension_scope: "새 확인 방법 절과 NTIP/NTIF·AMIG 상세 정의 대조. 기존 다른 절 재검증 아님; 실제 자료/실행/수치/물리 검증 미수행."
evidence_extension_review: "Claude Fable 5.1 — 새 확인 방법 원문 대조; 공식 예제의 추가 구분은 Codex 최종 검토 대상"
evidence_extension_human_approval: not-issued
source_correction_date: 2026-09-14
source_correction_by: "Codex — scoped source cross-reference"
source_correction_human_approval: not-issued
source_correction_review: "Claude Fable 5.1 — NBFR/첨자/노드/위상/시간/ETRF 변경 원문 대조; 과학적 사람 승인 아님"
source_correction_scope: "NBFR 입력 레코드/첨자와 경계 노드 순서·위상/시간 기준, 전통 분조 경로 ETRF 항. 전체 노트 재검증·실제 실행·수치/물리 검증 아님."
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-tide-harmonic-prep.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시. 2026-09-14: NBFR 입력·노드/분조 순서·위상/시간·ETRF 항의 한정 대조, 본문 한정 대조 범위 참조. 실제 실행·수치/물리 검증 미수행."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---


## 2026-09-14 한정 대조 범위

이 보강의 코드 판본은 ADCIRC `6037225ce4573efd3c1f8877a5dc908d01c199a8`이다. 아래 `src/` 인용의 루트는 `models/ADCIRC/raw/source_code/adcirc/`다. **문서 지원·코드 구현** 중 NBFR 입력, 경계 노드 전달, 위상/시간 기준, 전통 분조 경로의 ETRF 항을 대조했다. **실행 확인·수치 검증·물리 검증·개별 입력자료 품질 확인은 수행하지 않았다.** 다른 절과 외부 DB 규약은 이번 검증 범위에 포함하지 않는다. 과거 검증 이력과 이번 정정을 구분하며 이번 정정에 대한 사람 승인은 발급하지 않았다.

<a id="input-quality-and-validation"></a>

## 입력 품질·실행·검증 확인 방법 (2026-09-14 보강)

이 절은 **확인할 증거와 수행 순서**를 정한다. 실제 사용할 조석 DB·지형·관측자료와 허용오차는 아직 선정하지 않았으므로 **입력 품질·실행 확인·수치 검증·물리 검증은 미완**이다. 아래 G/H·Decision Guide의 외부 DB 호환성·지역 성능·권고 기간은 이 보강에서 재검증하지 않았다. 그 설명을 검증된 변환 규약으로 재사용하지 않는다. 필요한 원문이 없는 부분은 `source-needed`로 남긴다.

### 문서와 코드가 다를 때의 입력 기준

[공식 조석 개요](https://adcirc.github.io/adcirc/user_guide/model_configuration/tides/index.html)의 두 설명은 [상세 파라미터 정의](https://adcirc.github.io/adcirc/technical_reference/parameter_definitions/index.html) 및 이 노트의 S 판본 코드와 구별해야 한다(S는 위 한정 대조 범위의 전체 SHA).

- 개요의 분조 수 설명은 `NTIP`에 붙어 있지만, 상세 정의에서 **NTIP는 퍼텐셜/SAL 사용 방식**, **NTIF는 퍼텐셜 분조 수**다. 코드도 `NTIP`를 0–2로 검사하고 `NTIF`로 분조 입력을 반복한다. `docs/user_guide/model_configuration/tides/index.rst:15–19`; `docs/technical_reference/parameter_definitions/index.rst:452–459,758–759`; `src/read_input.F:1703–1731,3335–3349`.
- 개요의 `AMIG` 설명에는 amplitude가 나오지만, 상세 정의와 코드에서 **AMIG는 주파수**, 경계 진폭은 **EMO**다. `PER=2π/AMIG`와 시간 인수에 곱하는 위치를 함께 확인한다. `docs/user_guide/model_configuration/tides/index.rst:29–32`; `docs/technical_reference/parameter_definitions/index.rst:789–801`; `src/read_input.F:3431–3441`; `src/gwce.F:1638–1649`.

위 `docs/`·`src/`의 루트는 `models/ADCIRC/raw/source_code/adcirc/`다. 2026-09-14 웹 조회에서도 개요의 같은 표현을 확인했다. 이 두 불일치의 대조를 문서 사이트 전체의 정확성 판정으로 확대하지 않는다.

### 입력 품질 확인표

다음은 [위키의 입력 품질 기준](../../../../BUILD-PLAN.md)에 따른 확인 계획이다. 실제 자료값을 채우는 공간은 coastal-runs이며, 이 노트는 일반 절차와 출처를 제공한다.

| 확인 대상 | 설정 전에 확보·대조할 증거 | 현재 확인 수준/미확정 |
|---|---|---|
| 조석 DB·분조 정의 | 제품명·판본·문서 절·분조 목록·각주파수·해수면 조석/하중 조석의 변수 의미·단위 | ADCIRC 소비 형식만 확인. FES/NAO/TPXO의 판본별 정의는 `source-needed` |
| 지형·좌표·기준면 | 지형과 조석·관측 자료의 좌표/기준면·수심 부호·변환 이력; fort.14 노드와 원자료 대응 | [fort.14 구조](https://adcirc.github.io/adcirc/technical_reference/input_files/fort14.html) 및 [수심 노트](../adcirc-bathymetry-input-foundation.md)로 진입. 개별 데이터 미확인 |
| 공간·시간 범위와 해상도 | 경계 노드가 제품 유효 영역에 포함되는지, 연안 mask/격자 해상도, 제품의 대표 기간·허용 예측 시각과 실행/관측 기간 | 사용할 자료가 미선정. 범위 밖·외삽·대표성 불확실성을 기록해야 함 |
| 결측·품질·오차 | 품질 플래그·결측값·제공기관의 오차/불확실성 정의; 제외·대체·보간 정책과 근거 | 형식이 유효해도 품질 통과로 취급하지 않음; 제품별 원문 `source-needed` |
| 분조·노드 순서 | NBFR 헤더와 각 분조 블록, 분조당 NETA개 행을 fort.14의 경계 구간/구간 내 순서와 대조 | 아래 §A 및 `src/mesh.F:1822–1834`, `src/read_input.F:3431–3456,3485–3497`. 실제 입력 대조 미수행 |
| 위상·시각·노달보정 | 위상 부호/기준 경도·시간대·epoch, STATIM/REFTIM과 FF/FACE 기준; 제공 제품이 이미 포함한 보정과 별도 보정의 중복 여부 | ADCIRC 시간/부호는 §D/F에서 한정 대조. 외부 규약은 `source-needed` |
| 변환·보간의 독립 확인 | 원 격자점과 변환 결과를 대조하고, 별도 계산 또는 제공기관 예측과 몇 위치·시각의 재합성을 비교. 해안 mask·위상 주기 경계 처리의 방법/오차를 기록 | 확인 방법은 계획. 특정 보간법·도구의 적합성/성능은 아직 확정하지 않음 |
| 퍼텐셜·SAL·초기 강제 | 경계 수위와 퍼텐셜/SAL을 구분한 선택 이유, NTIP/NTIF·분조·입력파일·ramp·초기시각의 정합 | §A/F와 [퍼텐셜의 한정 대조](adcirc-tide-forcing-implementation.md). SAL/full-formula 전체 재검증은 미수행 |

### 실행 확인에서 확보할 것

1. 실행파일의 코드 판본·빌드 옵션, 입력파일 버전, 실행 명령과 종료 상태를 고정한다. 입력 검사와 계산 경로 확인을 분리한다([BUILD-PLAN §4–6](../../../../BUILD-PLAN.md)).
2. `fort.16`의 NTIP 선택 및 NBFR 분조·노드·진폭·위상 echo를 입력과 대조한다. `src/read_input.F:1717–1731,3431–3435,3485–3497`은 로그 생성 위치다. echo만으로 내부 계산 경로의 실행이나 물리 적합성을 확정하지 않는다.
3. 순수 주기 수위 경계 예제에서는 선택한 경계점·시각의 출력과 §A/D/F 합성을 대조한다. ramp와 함께 작동하는 다른 경계 항이 있으면 그 항까지 확인해야 한다. 합성 코드의 위치는 `src/gwce.F:1638–1649`이며 **이번에 이 대조 실행은 하지 않았다**.
4. 출력의 정점·변수·시간 범위와 간격을 확인한다. 조화분해는 강제 입력의 NBFR와 별도로 NFREQ·NAMEFR·HAFREQ/HAFF/HAFACE, THAS/THAF·NHAINC 및 출력 위치 선택을 확인한다. `fort.51`은 지정 수위 정점의 진폭/위상 출력이다. 근거: `docs/technical_reference/parameter_definitions/index.rst:1140–1177,1191–1213`; `docs/technical_reference/output_files/fort51.rst:1–23`. 여기서는 세부 출력 형식 코드의 전체 유효값을 확정하지 않는다.

### 수치 검증과 물리 검증의 분리

- **회귀 예제**: 공식 testsuite의 `adcirc_quarterannular-2d-netcdf`는 `test_list.yaml:423–434`에 정의돼 있다. `test_runner/adcirc_test/adcirctest.py:429–445`는 지정된 `control/` 파일과 계산 출력을 비교한다. testsuite 판본은 `72bb573073ea89e538890f9352dd8e92bae562f5`, 루트는 `models/ADCIRC/raw/source_code/adcirc-testsuite/`다. 이 케이스의 `adcirc/adcirc_quarterannular-2d-netcdf/fort.15:15,31–44`는 **NTIP=0, NTIF=0, NBFR=1(M2)**로 경계 조석을 지정한다. 즉 이 입력 예제에서 경계 조석과 퍼텐셜은 별도 선택이다. 기준 출력과 일치했다는 주장에는 실제 실행 결과가 필요하다.
- **수치 검증**: 사용할 해석해/기준해의 식·조건·출처, 물수지/보존 진단, 격자·시간간격 민감도와 오차 기준을 결과 전에 정한다. 회귀검사의 기본 tolerance를 해역의 물리 오차 기준으로 사용하지 않는다. 현재 기준해 대조와 허용오차 선정은 미수행이다([BUILD-PLAN §4–6](../../../../BUILD-PLAN.md)).
- **물리 검증**: 경계·보정에 사용한 자료와 독립적인 관측/실험을 구분하고, 정점/기간·기준면·시간대·결측·관측오차를 확인한다. 비교할 진폭·주기적인 위상 차이·시계열 오차의 정의와 허용 범위, 분조 분리와 분석창의 근거를 먼저 확보한다. 일반 조화분해 이론은 [조석 분석 방법](../../../../concepts/tides/03-analysis-methods.md), ADCIRC 관측검증 권고는 `docs/user_guide/model_configuration/tides/index.rst:57–65`다. **관측자료·분석 세부 절차·목적별 허용오차는 `source-needed`**이며 관측 대조를 수행했다고 쓰지 않는다.

이 묶음의 다음 완료 조건은 외부 자료 규약·변환/보간 확인 방법과 사용할 기준해/관측·오차 기준의 출처를 확보하는 것이다. 실제 실행·검증 완료 판정에는 별도의 재현 가능한 결과가 필요하며, 개인 결과는 [coastal-runs 채널](../../../../RUNS-CHANNEL.md)에 둔다.

## Scope

Exactly what ADCIRC's reader expects in the fort.15 NBFR boundary harmonic block (`AMIG/FF/FACE` + per-node `EMO/EFA`), how `fort.24`/`fort.24.nc` self-attraction-and-loading (SAL) is read (only when `NTIP=2`), how constituent name matching works (strict, case-sensitive trim), the units/sign/phase conventions ADCIRC applies, and what `REFTIM` does to the harmonic time base. Use this when converting external databases (NAO99jb, FES2022b, TPXO) to ADCIRC inputs, or debugging tide phase/amplitude validation errors.

**Key fact**: ADCIRC has **no built-in parser** for FES/NAO/TPXO databases. It only consumes preprocessed `fort.15` harmonic block and optional `fort.24` SAL.

## Source basis

- `read_input.F:1705-1731, 3344-3497, 6282-6463` — `NTIP`, NBFR boundary block, SAL reader.
- `gwce.F:1638-1650` — boundary elevation synthesis.
- `timestep.F:251-258, 1517-1562` — `TimeH` and tidal-potential application.
- `hstart.F:1525-1532` — SAL into TIP2.

## A. fort.15 NBFR boundary harmonic block

```
NBFR
do j = 1, NBFR
   BOUNTAG(j)                      ! constituent tag string
   AMIG(j)  FF(j)  FACE(j)         ! frequency, nodal factor, equilibrium argument (deg)
end do
do j = 1, NBFR
   ELEVALPHA(j)                    ! constituent tag (printed only, no validation)
   do i = 1, NETA
      EMO(j,i)  EFA(j,i)           ! constituent j, boundary node i; amplitude (m), phase lag (deg)
   end do
end do
```

References (`read_input.F`):
- `NBFR` read + arrays allocated: `:3410-3418`.
- Per-constituent header `BOUNTAG, AMIG, FF, FACE`: `:3431-3436`.
- `FACE` deg → rad after read: `:3436`.
- Per-constituent boundary block `ELEVALPHA + EMO/EFA`: `:3450-3455`.
- `EFA` deg → rad after logging: `:3493-3497`.

Important: `ELEVALPHA` is **only printed** as "verification"; **no match/validation against `BOUNTAG`** (`:3485-3490`). You must keep the per-constituent ordering consistent yourself.

경계 노드 순서는 전체 격자 번호의 정렬 순서가 아니다. `src/mesh.F:1822–1834`는 `K=1..NOPE`, 각 구간의 `I=1..NVDLL(K)` 순서로 `NBDV(K,I)`를 `NBD`에 이어 붙인다. 분조별 `EMO/EFA` 행은 이 순서에 맞아야 하며 `src/read_input.F:3493–3496`의 노드·진폭·위상 출력과 대조할 수 있다. 공식 [fort.15 구조](https://adcirc.github.io/adcirc/technical_reference/input_files/fort15.html)도 분조를 첫 첨자로 표기한다. 이 절의 도식은 전체 입력 파일 예제가 아니다.

## B. fort.24 SAL reader

Called from main startup (`adcirc.F:292-293`); reader at `read_input.F:6282-6463`.

**Active only for `NTIP=2`**:
- `NTIP < 2`: SAL arrays zeroed (`:6460-6462`).
- `NTIP=0`: tidal potential entirely off.
- `NTIP=1`: tidal potential active, no SAL.
- `NTIP=2`: tidal potential + SAL.

NetCDF preferred if `fort.24.nc` exists (`:6330-6344`).

### NetCDF format

Required dims/vars (`:6353-6365`):
- Dimensions: `node`, `num_constituents`, `char_len`.
- Variables: `constituents`, `frequency`, `sal_amplitude`, `sal_phase`.

Constituent count must equal `NTIF` (`:6367-6371`).

### ASCII format (`fort.24`)

Per-constituent block (`:6429-6455`):
```
<dummy_char>  <dummy_char>          ! 2 dummy chars
<dummy_real>                        ! ignored
<dummy_int>                         ! ignored
<const_name>                        ! e.g. "M2"
do i = 1, num_nodes
   JJ  SALTAMP(JJ)  SALTPHA(JJ)
end do
```

`SALTPHA` deg → rad after read.

## C. Constituent matching

`fort.15` tidal-potential tags are **`TIPOTAG`** (different from `BOUNTAG`!) (`:3347-3349`).

- NetCDF SAL: `TRIM(TIPOTAG(I)) == TRIM(const_name)` (`:6378-6385`).
- ASCII SAL: each SAL `const_name` matched to some `TIPOTAG(J)` (`:6436-6443`).

**Strict, case-sensitive**, no aliasing.

## D. Phase / sign / units

| Quantity | Input units | Internal (post-read) | Sign |
|---|---|---|---|
| `FACE`, `FACET` (eq. arg.) | degrees | radians | added to argument |
| `EFA` (boundary phase lag) | degrees | radians | **subtracted** in `cos(arg − EFA)` |
| `SALTPHA` (SAL phase) | degrees | radians | **subtracted** in `cos(arg − SALTPHA)` |
| `EMO`, `SALTAMP` | meters | (no conversion) | direct multiplier |

Boundary synthesis (`gwce.F:1644-1649`):
```
Eta2(NBDI) += EMO * FF * RampElev * cos(AMIG*timeh + FACE − EFA)
```

SAL synthesis into `TIP2` (`timestep.F:1547-1548`, `hstart.F:1525-1532`):
```
TIP2 += SALTMUL * SALTAMP * cos(ARGT − SALTPHA)
```

ADCIRC uses **lag-subtracted** phase (`cos(arg − phase)`). FES2022b convention is the same; NAO99jb and TPXO also use lag convention. ⚠ source-needed(외부 DB 위상규약 서술 — FES2022b·NAO99jb·TPXO 공식문서 미인용). **Confirm** before using a database.

## E. FF and FACE meaning

- `FF` (boundary): nodal factor (multiplies amplitude at runtime).
- `FFT` (tidal potential): same role for potential and SAL.
- `FACE` (boundary): equilibrium argument `(V₀ + u)` (added to argument).
- `FACET` (tidal potential): same role for potential.

These come from astronomical theory; standard tools (T_TIDE, UTIDE, pyTMD) compute them per epoch.

## F. REFTIM and TimeH

`REFTIM` is the harmonic reference time in **days** (`:2541`).

```
TimeH = IT * DTDP + (StaTim − RefTim) * 86400
```
(`timestep.F:251-258`).

`STATIM`과 `REFTIM`은 일(day) 단위로 읽히며(`src/read_input.F:2534–2543`), 내부 `TimeH`는 초다(`src/timestep.F:257–258`). 합성은 `AMIG(J)*(TimeH−NCYC*PER(J))+FACE(J)−EFA(J,I)`이며 `EFA`는 입력의 도(degree)에서 radian으로 변환한다(`src/read_input.F:3436,3493–3496`; `src/gwce.F:1642–1649`). 실제 입력을 준비할 때 원자료의 기준시각·위상 규약·단위와 이 정의를 대조해야 한다. 이 코드 확인은 외부 DB의 규약이나 실제 변환 자료의 품질을 검증한 것이 아니다.

Harmonic synthesis uses `timeh`, **not** raw model time (`gwce.F:1642-1644`, `timestep.F:1532-1535`).

**This is the most common source of phase errors**: `FACE`/`FACET` from your database are computed for some epoch (often midnight UTC of a specific day). `REFTIM` must match that epoch, expressed in your run's time-axis convention.

## G. NAO99jb / FES2022b workflow

ADCIRC has **no native NAO/FES parser**. You preprocess externally:

1. Pick run start `STATIM` and epoch `REFTIM`.
2. For each constituent (M2, S2, K1, O1, etc.), get astronomical `f` (nodal factor), `(V₀+u)` (eq. arg) for `REFTIM` from T_TIDE / UTIDE / pyTMD.
3. From FES/NAO database, extract per-boundary-node amplitude and Greenwich phase lag at the configured constituent set.
4. Write `fort.15` NBFR block:
   - Header line `NBFR`.
   - Per constituent: `BOUNTAG`, then `AMIG, FF, FACE` (FF and FACE both for `REFTIM` epoch, FACE in degrees).
   - Per constituent: `ELEVALPHA`, then per-node `EMO  EFA` (EFA in degrees, **lag** convention).

For SAL, similar process; write to `fort.24` ASCII or `fort.24.nc` NetCDF.

## H. Validation pitfalls

- ▢ **Wrong epoch** for `REFTIM` vs `FACE/FACET` — phase off by a constant. Symptom: high phase RMSE but reasonable amplitude.
- ▢ **Lead vs lag** phase convention — sign flip. Symptom: phase off by ~180° on some constituents. Confirm `cos(arg − phase)` form.
- ▢ **Greenwich vs local** zone phase — many databases give Greenwich (UTC); ADCIRC's `STATIM/REFTIM` defines its own zone (usually UTC by convention).
- ▢ **Amplitude in cm not m** — silent factor of 100.
- ▢ **Constituent name mismatch** — strict trim; "M2" != "m2" (case sensitive in some compilers).
- ▢ **Order mismatch** between `BOUNTAG` and `ELEVALPHA` blocks — `ELEVALPHA` is only printed; you must keep order consistent manually.
- ▢ **Forgetting nodal correction** — if you use astronomical reference `(V₀+u)` for *one* date but run for years, `f` and `(V₀+u)` change. ADCIRC applies them as constants — for runs > 1 month, recompute or accept reduced accuracy.
- ▢ **NTIP=2 without `fort.24`** — SAL arrays stay zero; the model runs but you lose SAL physics. Check log for "fort.24 not found."

## Decision Guide

| Need | Setup |
|---|---|
| Tide-only run | `NTIP=1`, fort.15 NBFR block; **no fort.24** |
| Tide + SAL (recommended) | `NTIP=2`, fort.15 NBFR + fort.24 |
| FES2022b global | T_TIDE/pyTMD for FF/FACE; FES interpolation for amplitudes/phases at boundary nodes |
| NAO99jb regional (Asia/Pacific) | Same workflow; NAO99jb covers M2/S2/K1/O1 well |
| Combined FES + tide gauge | Boundary from FES; verify against gauges in interior |
| TPXO global | Similar; conventions match |
| Long run (>1 yr) | Document FF/FACE epoch; consider re-running with new astronomical reference quarterly |
| Disable tidal potential and periodic elevation forcing | `NTIP=0`; keep the required `NBFR=0` line. Any non-periodic elevation boundary data are a separate input (`src/read_input.F:1705–1731,3410–3444`; [official NBFR definition](https://adcirc.github.io/adcirc/technical_reference/parameter_definitions/index.html)). |

## Working Rules

- Always write `STATIM`, `REFTIM`, and the FF/FACE epoch in the run README. These three must align.
- Use 8-character constituent names ("M2      ", "S2      ", etc.) padded; ADCIRC trims, but consistent is safer.
- Output `fort.51` harmonic analysis at validation stations to compute model-side amplitude/phase, then compare against gauge harmonic constants — this is far more diagnostic than time-series RMSE.
- For Korean coast, NAO99jb gives good M2/S2/K1/O1 starting point; FES2022b adds N2, K2, P1 if you need finer accuracy. ⚠ source-needed(지역 정확도 서술 출처 미인용).
- SAL from fort.24 typically reduces M2 amplitude by ~5-10% in shelf seas — if your run shows persistent +10% M2 overprediction, missing SAL is a likely cause. ⚠ source-needed(~5-10% 정량값 출처 미인용).

## Common Pitfalls

(See "H. Validation pitfalls" above — most issues come from epoch and phase convention.)

Additional:
- ▢ Hot-start across `NTIP` change — harmonic accumulators / SAL arrays inconsistent.
- ▢ Modifying NBFR block but not regenerating SAL constituent set — names mismatch silently.
- ▢ Nesting (boundary forcing from coarse-grid output) — coarse `EMO/EFA` may not be exact at fine boundary nodes; interpolate carefully.

## Next expansion

- T_TIDE / pyTMD recipe for FF/FACE generation.
- FES2022b → fort.15 conversion script.
- SAL preparation from FES2022b loading-tide grids.
- Validation harmonic analysis (`fort.51`) post-processing.

## References

- Westerink et al. 1992 (ADCIRC tide formulation).
- Hendershott 1972 (SAL theory).
- T_TIDE: Pawlowicz et al. 2002.
- UTIDE: Codiga 2011.
- FES2022b: Lyard et al. 2024.
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/adcirc/source_code/adcirc/src`. Auto-draft = false; review_required = true.
