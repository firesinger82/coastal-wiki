---
title: "SWAN swanuse §1-3 General description — limitations + internal scenarios/limiters/bugs + units/conventions + generation modes + time-date verbatim"
topic: swan
canonical_source: external
external_source: "swanuse.pdf (User Manual, SWAN Cycle III version 41.51) §1 About + §2 General description and instructions for use (Introduction/Limitations/Internal scenarios/Relation to WAM/Units/Grids/Physics activation/Time-date) + §3 Input-output files (p.1-22) + node1-18.md."
citation_status: verified
verification_method: "swanuse website_markdown node4(Limitations)/node5(Internal scenarios·limiters·bugs)/node7(Units·conventions)/node13(Physics activation·Table 2.1 generation modes)/node14(Time-date)/node3·6·15-18 직접 read. 정책·convention·default verbatim."
note_author: "Claude Opus 4.8 (1M context) raw markdown direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — limitations·conventions·generation mode verbatim"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/manual-notes/swan-command-setup-grid-reference.md
  - models/SWAN/manual-notes/swan-tech-ch3-refraction-limiter.md
---

# SWAN swanuse §1-3 General description — verified

> swanuse.pdf (User Manual v41.51) §1-3 직접 read. SWAN **사용 정책·한계·convention·generation mode** — command(§4, [[swan-command-setup-grid-reference]] 외 2노트) 의 배경. swantech(이론) ↔ swanuse(사용) 의 "instructions for use".

## 1. §2.2 Limitations (실무 한계)

- **DIA quadruplet**: directional 분포 폭·frequency resolution 의존. **long-crested(narrow dir) 부정확** + freq ratio 10% 크게 벗어나면 부정확 (WAM·WW3 공통 fundamental). [[swan-command-physics-reference]] QUADRUPL
- **LTA triad**: narrow flume(long-crested) 관측 tuning → 일반 case 주의. [[swan-command-physics-reference]] TRIAD
- **wave-induced set-up**: 1D=exact, **2D=근사 (open coast 만; closed basin/lake 금지)**. [[swan-tech-ch4-5-bc-2d-setup]] §5
- **wave-induced current 미계산** — 필요시 circulation model(SWAN↔모델 iteration)로 입력
- **diffraction**: phase-decoupled (qualitative redistribution) → **harbour·reflecting obstacle 앞 부적합**. [[swan-tech-ch2-obstacles-diffraction-setup]] §4
- **scale**: any scale 가능하나 **coastal 전용 설계**; oceanic scale 은 WW3·WAM 보다 비효율 (flexibility 는 lab~shelf + WAM/WW3 nesting spherical 용)

## 2. §2.3 Internal scenarios, limiters, shortcomings, coding bugs ★

> 입력이 불량(bathymetry/wave field 미해상)이면 비현실적 결과 가능. **입력격자→계산격자 보간**이 예상외 패턴 유발 가능. SWAN 은 종료 대신 **internal scenario·limiter** 발동 (robust + local 문제 + 전체계산 후 진단 가능 정책).

예시:
- **refraction limiter**: 1 spatial step refraction 제한 (NUMERIC CTHETA). 수심 급변(ocean edge·island, 1-2 step에 oceanic→shallow) 시 부정확하나 국소면 수용 — 단 부정확 효과가 멀리 radiate 가능. ([[swan-tech-ch3-refraction-limiter]] §3.8 Eq 3.41)
- **super-critical current**: SWAN 처리 불가 → 국소 **sub-critical 로 감소** (froudmax=0.8 SET)
- **depth limit**: 수심 < 사용자 한계 시 한계값 (default **0.05 m**, SET depmin)
- **boundary 미재현**: imposed 경계파를 계산영역 밖으로 나가는 computed 파로 **대체** → 경계 imposed Hs 미보존 (hsrerr 경고)
- **수렴 문제**: **3 iteration process** — ① 공간 전파(stationary 여러 iteration / nonstat time step당 1, 4-sweep quadrant가 spectral dir와 일치 시 curvilinear 국소 비수렴) ② current 시 spectral 전파(refraction+freq shift) ③ set-up SOR. PRINT 파일에 수렴정보.
- **fundamental shortcoming + coding bug**: 결과가 현실적으로 보여도 국소 부정확 가능. 발견된 bug·fix 는 SWAN web + 신 release 에 공개.

## 3. §2.5 Units and coordinate systems

- **SI units** (m, kg, s, N, W): wave height·depth m, period s
- **방향 convention** (wind/wave 입출력):
  - **Cartesian**: 벡터가 **향하는** 방향, x축 기준 반시계
  - **Nautical**: wind/wave 가 **오는** 방향, 북 기준 시계 (SET NAUTICAL)
  - **기타 방향(grid orientation 등)은 항상 Cartesian!**
- **좌표계**: Cartesian(flat, origin (0,0) 임의 — 단 너무 큰 수 금지, offset 권장) / spherical(longitude·latitude). = problem coordinate system

## 4. §2.7 Activation of physical processes + generation modes

물리 process: wind input·whitecapping·bottom friction·depth breaking·vegetation·mud·sea ice·turbulence·obstacle·quadruplet·triad·set-up + **Bragg scattering (since 41.41)**.

**Generation mode** (Holthuijsen-De Boer 1988): **1st-gen** = Phillips 상수 0.0081 / **2nd-gen** = variable Phillips / **3rd-gen** = full source terms. **Table 2.1**:

| process | 1st/2nd | 3rd |
|---|---|---|
| linear wind growth | Cavaleri-Malanotte-Rizzoli (mod) | Cavaleri-MR |
| exp wind growth | Snyder 1981 (mod) | Snyder / **Janssen 1989·91** / **Yan 1987** |
| whitecapping | Holthuijsen-De Boer 1988 | Komen 1984 / Janssen 1991 / **Alves-Banner 2003** |
| quadruplet | — | Hasselmann 1985 (DIA) |
| triad | Eldeberky 1996 / Booij 2009 | (1·2·3 공통) |
| breaking | Battjes-Janssen 1978 | (공통) |
| bottom friction | JONSWAP / Collins | (공통) |
> [[swan-tech-ch2-sources-sinks]] / [[swan-tech-ch2-dissipation-detailed]]. GEN1/GEN2/GEN3 command.

## 5. §2.8 Time and date notation

- **ISO notation** (권장): 연도 **0-9999**
- 2-digit 연도 (format 2-6): **1931-2030**
- ⚠ **WAM nesting 시 주의** (WAM 은 ISO 미사용)

## 6. §3 Input and output files (요약)

- **General**: command file (표준입력) + 입력 데이터 파일(grid 별) + 출력 파일
- **I/O facilities**: ASCII / binary(Matlab·netCDF), free/fixed format, header
- **Print file**: `*.prt` (echo·warning·error·**수렴 정보**) + error message (maxerr level)
- **§1 About**: 4 docs (User/Tech/Impl/Programming, [[swan-documentation-stack]]), Cycle III 41.51

## 7. Appendix (요약, swanuse Appendix A-D)

- **A Definitions of variables** (p.115): Hs=4√m_0, Tm01/Tm02/Tmm10, Dir, Dspr, 모든 출력변수 정확 정의 ([[swan-command-numerics-output-reference]] §2.2 변수 목록)
- **B Command syntax** (p.121): keyword(대문자 필수부 + 소문자 optional)·required/optional·spelling·repetition·continuation(`&`)
- **C swan.edt** (p.127): 전체 command template 파일
- **D Spectrum files** (p.137): 1D/2D spectrum 입출력 format (SWAN standard)

## 8. 연결

- [[swan-documentation-stack]] — 4 docs 구조 + Ch 1 historical(cycle 1·2·3)
- [[swan-command-setup-grid-reference]] / [[swan-command-physics-reference]] / [[swan-command-numerics-output-reference]] — §4 command (본 노트 = §1-3 배경)
- [[swan-tech-ch3-refraction-limiter]] — internal scenario refraction limiter 이론
- [[swan-tech-ch4-5-bc-2d-setup]] — set-up 2D open-coast 한계 이론
