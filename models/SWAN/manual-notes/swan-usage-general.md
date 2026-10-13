---
title: "SWAN swanuse §1-3 General description — limitations + internal scenarios/limiters/bugs + units/conventions + generation modes + time-date verbatim"
topic: swan
canonical_source: external
external_source: "swanuse.pdf (User Manual, SWAN Cycle III version 41.51) §1 About + §2 General description and instructions for use (Introduction/Limitations/Internal scenarios/Relation to WAM/Units/Grids/Physics activation/Time-date) + §3 Input-output files (p.1-22) + node1-18.md."
citation_status: verified
verification_method: "swanuse website_markdown node4(Limitations)/node5(Internal scenarios·limiters·bugs)/node7(Units·conventions)/node13(Physics activation·Table 2.1 generation modes)/node14(Time-date)/node3·6·15-18 직접 read. 정책·convention·default verbatim. 2026-10-13 recovery 대조 보고서 R1–R8 반영."
last_source_check: 2026-10-13 (recovery 대조 반영)
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

> swanuse.pdf (User Manual v41.51) §1-3 직접 read. SWAN **사용 정책·한계·convention·generation mode** — command(§4, [swan-command-setup-grid-reference](swan-command-setup-grid-reference.md) 외 2노트) 의 배경. swantech(이론) ↔ swanuse(사용) 의 "instructions for use".

## 1. §2.2 Limitations (실무 한계)

- **DIA quadruplet**: directional 분포 폭·frequency resolution 의존. **long-crested(narrow dir) 부정확** + freq ratio 10% 크게 벗어나면 부정확 (WAM·WW3 공통 fundamental). [swan-command-physics-reference](swan-command-physics-reference.md) QUADRUPL
- **LTA triad**: narrow flume(long-crested) 관측 tuning → 일반 case 주의. [swan-command-physics-reference](swan-command-physics-reference.md) TRIAD
- **wave-induced set-up**: 1D의 정확성은 채택한 물리 평형식에 관한 설명으로 한정한다. 수치해의 오차가 0이라는 뜻으로 쓰지 않는다. [R3:NT-049](../../../_staging/recovery/compare/swan-theory-obstacles-setup-qc-bc-vs-code.md#5-차이-결론). [swan-tech-ch4-5-bc-2d-setup](swan-tech-ch4-5-bc-2d-setup.md) §5.
- **wave-induced current 미계산** — 필요시 circulation model(SWAN↔모델 iteration)로 입력
- **diffraction**: 시야 차폐, 수 파장 미만의 거리, 결맞는 반사, 유의한 반사계수의 동시 조건은 적용 권고다. swantech PDF 65쪽 / 인쇄 57쪽: “Diffraction in SWAN should not be used if,”; “and”. [swan-tech-ch2-obstacles-diffraction-setup](swan-tech-ch2-obstacles-diffraction-setup.md) §4.
- **scale**: any scale 가능하나 **coastal 전용 설계**; oceanic scale 은 WW3·WAM 보다 비효율 (flexibility 는 lab~shelf + WAM/WW3 nesting spherical 용)

## 2. §2.3 Internal scenarios, limiters, shortcomings, coding bugs ★

> 입력이 불량(bathymetry/wave field 미해상)이면 비현실적 결과 가능. **입력격자→계산격자 보간**이 예상외 패턴 유발 가능. SWAN 은 종료 대신 **internal scenario·limiter** 발동 (robust + local 문제 + 전체계산 후 진단 가능 정책).

예시:
- **refraction limiter**: 1 spatial step refraction 제한 (NUMERIC CTHETA). 수심 급변(ocean edge·island, 1-2 step에 oceanic→shallow) 시 부정확하나 국소면 수용 — 단 부정확 효과가 멀리 radiate 가능. ([swan-tech-ch3-refraction-limiter](swan-tech-ch3-refraction-limiter.md) §3.8 Eq 3.41)
- **super-critical current**: SWAN 처리 불가 → 국소 **sub-critical 로 감소** (froudmax=0.8 SET)
- **depth limit**: DEPMIN의 초기값은 0.05 m이다. 임계값 이하의 활성점에서는 파 작용밀도를 0으로 만든다. `src/swanmain.ftn:1139` `DEPMIN = 0.05`; `src/swancom1.ftn:3292` `AC2(ID,IS,KCGRD(1)) = 0.`.
- **boundary 미재현**: 입사 성분은 부과값을 사용한다. 출사 성분은 계산값을 사용한다. swanuse PDF 20쪽 / 인쇄 12쪽: “accepts only … incoming … replaces … outgoing … with computed outgoing components”. `src/swancom1.ftn:3663` `DO IDDUM = IDCMIN(IS), IDCMAX(IS)`; `src/swancom1.ftn:3671` `AC2(ID,IS,KCGRD(1)) = SWMATR(ID,IS,JMATR) / TEMP`.
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

표 2.1을 전체 지원 물리 목록으로 사용하지 않는다. ST6 설명은 GEN3 본문에 있으므로 C 판정은 이 요약표에 한정한다. swanuse PDF 28쪽 / 인쇄 20쪽의 표 2.1; PDF 67쪽 / 인쇄 59쪽의 GEN3 본문. `src/swanpre1.ftn:2983` `ELSE IF (KEYWIS('ST6')) THEN`.

| process | 1st/2nd | 3rd |
|---|---|---|
| linear wind growth | Cavaleri-Malanotte-Rizzoli (mod) | Cavaleri-MR |
| exp wind growth | Snyder 1981 (mod) | Snyder / **Janssen 1989·91** / **Yan 1987** |
| whitecapping | Holthuijsen-De Boer 1988 | Komen 1984 / Janssen 1991 / **Alves-Banner 2003** |
| quadruplet | — | Hasselmann 1985 (DIA) |
| triad | Eldeberky 1996 / Booij 2009 | (1·2·3 공통) |
| breaking | Battjes-Janssen 1978 | (공통) |
| bottom friction | JONSWAP / Collins | (공통) |
> [swan-tech-ch2-sources-sinks](swan-tech-ch2-sources-sinks.md) / [swan-tech-ch2-dissipation-detailed](swan-tech-ch2-dissipation-detailed.md). GEN1/GEN2/GEN3 command.

## 5. §2.8 Time and date notation

- **ISO notation** (권장): 연도 **0-9999**
- 두 자리 연도를 포함하는 형식 2·3·5·6은 1930–2029로 읽는다. 형식 4는 시각만 읽는다. `src/ocpids.ftn:494` `INTEGER :: JUMPYEAR = 30`; `src/ocpids.ftn:506` `IF (DTTIME(1).LT.JUMPYEAR) THEN`.
- ⚠ **WAM nesting 시 주의** (WAM 은 ISO 미사용)

## 6. §3 Input and output files (요약)

- **General**: 기본 명령 입력은 INPUT 파일이다. `src/ocpids.ftn:182` `INPFIL = 'INPUT'`. 계산 결과 출력은 요청 자료구조를 따른다.
- **I/O facilities**: ASCII / binary(Matlab·netCDF), free/fixed format, header
- **Print file**: `*.prt` (echo·warning·error·**수렴 정보**) + error message (maxerr level)
- **§1 About**: SWAN 문서는 User·Tech·Impl·Programming의 네 종류이다. User·Tech·Impl의 문서 판은 Cycle III 41.51이다. Programming의 문서 판은 1.3이다. (swanuse PDF 9쪽 / 인쇄 1쪽; 각 매뉴얼 PDF 1쪽의 표지; [swan-documentation-stack](swan-documentation-stack.md).) [10-13 전수 검증 정정]

## 7. Appendix (요약, swanuse Appendix A-D)

- **A Definitions of variables** (p.115): Hs=4√m_0, Tm01/Tm02/Tmm10, Dir, Dspr, 모든 출력변수 정확 정의 ([swan-command-numerics-output-reference](swan-command-numerics-output-reference.md) §2.2 변수 목록)
- **B Command syntax** (p.121): keyword(대문자 필수부 + 소문자 optional)·required/optional·spelling·repetition·continuation(`&`)
- **C swan.edt** (p.127): 전체 command template 파일
- **D Spectrum files** (p.137): 1D/2D spectrum 입출력 format (SWAN standard)

## 8. 연결

- [swan-documentation-stack](swan-documentation-stack.md) — 4 docs 구조 + Ch 1 historical(cycle 1·2·3)
- [swan-command-setup-grid-reference](swan-command-setup-grid-reference.md) / [swan-command-physics-reference](swan-command-physics-reference.md) / [swan-command-numerics-output-reference](swan-command-numerics-output-reference.md) — §4 command (본 노트 = §1-3 배경)
- [swan-tech-ch3-refraction-limiter](swan-tech-ch3-refraction-limiter.md) — internal scenario refraction limiter 이론
- [swan-tech-ch4-5-bc-2d-setup](swan-tech-ch4-5-bc-2d-setup.md) — set-up 2D open-coast 한계 이론

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

빈 인용 칸은 `—`로 표시한다. 표의 절 번호는 각 행이 링크한 대조 보고서의 절 번호다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R3:NT-049 | 1D 정확성과 회절 적용 권고 | `manual-notes/swan-usage-general.md:26` `1D=exact`; 28 `harbour·reflecting obstacle 앞 부적합`. SU-004와 OQ-027은 적용 가정·권고다. | — | H 코드 대조 대상 아님 | 1D의 정확성은 채택한 물리 평형식에 관한 설명으로 한정한다. 수치해의 오차가 0이라는 뜻으로 쓰지 않는다. 회절의 네 가지 동시 금지 조건은 PDF 65, 인쇄 57의 원문 연결 관계를 유지한다. [R3](../../../_staging/recovery/compare/swan-theory-obstacles-setup-qc-bc-vs-code.md#5-차이-결론) |
| R4:T1-003 | 입사·출사 오기 | swanuse PDF 14쪽 / 인쇄 6쪽: “replaces … waves … that propagate into … with … waves that move out”. swanuse PDF 20쪽 / 인쇄 12쪽: “accepts only … incoming … replaces … outgoing … with computed outgoing components”. | `src/swanmain.ftn:6945` `CALL SINTRP (W1, W2, BSPECS(1,1,K1,1), BSPECS(1,1,K2,1),`; `src/swanmain.ftn:6946` `&                    AC2(1,1,INDXGR), SPCDIR, SPCSIG)`; `src/swancom1.ftn:3299` `IF (KCGRD(2) .LE. 1) RETURN`; `src/swancom1.ftn:3300` `IF (.NOT.ONED .AND. (KCGRD(3).LE.1)) RETURN`; `src/swancom1.ftn:3369` `CALL SWPSEL (SWPDIR                            ,IDCMIN        ,`; `src/swancom1.ftn:3663` `DO IDDUM = IDCMIN(IS), IDCMAX(IS)`; `src/swancom1.ftn:3671` `AC2(ID,IS,KCGRD(1)) = SWMATR(ID,IS,JMATR) / TEMP`; `src/swanmain.ftn:6916` `CALL RBFILE ( SPCSIG, SPCDIR,` | B 문서 오기 | 부과한 입사 성분은 사용한다. 출사 성분은 계산값으로 바꾼다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-004 | 얕은 수심 설명 | swanuse PDF 14쪽 / 인쇄 6쪽: “current is locally reduced to sub-critical flow”; “depth is set at that limit”. | `src/swanmain.ftn:4919` `CGFACT = CGMAX / VTOT`; `src/swancom1.ftn:3292` `AC2(ID,IS,KCGRD(1)) = 0.` | B 문서 오기 | DEPMIN 이하에서는 파 작용밀도를 0으로 만든다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-005 | 근사·수렴·물리 한계 | swanuse PDF 12–15쪽 / 인쇄 4–7쪽: DIA “poor approximation for long-crested waves”; LTA “observations in a narrow wave flume”; set-up “approximate equations”; diffraction “does not properly handle … harbours”; “There are three iteration processes”. | — | H 코드 대조 대상 아님 | 유효성·수렴 가능성에 관한 설명을 입력값 검사로 해석하지 않는다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-006 | 해상도·경계·시간창 권고 | swanuse PDF 18–24쪽 / 인쇄 10–16쪽: “make an input grid so large that it completely covers”; “start at a time that is early enough”; “30° to 45°”; “50–1000 m”; “0.04 ≤ f ≤ 1.00 Hz”. | — | H 코드 대조 대상 아님 | 권고값과 파서가 강제하는 허용값을 구분한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-007 | 효율·academic 용도 | swanuse PDF 12쪽 / 인쇄 4쪽: “probably one order of magnitude more efficient”; swanuse PDF 38쪽 / 인쇄 30쪽: REPEATING “only for academic cases”. | `src/swanpre1.ftn:855` `KREPTX = 1` | H 코드 대조 대상 아님 | 성능 배수는 문서의 추정이다. academic 용도는 사용 권고이다. 두 문장은 입력 명령의 구현 판정과 구분한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-009 | 타 모델과의 관계 | swanuse PDF 15쪽 / 인쇄 7쪽: “basic scientific philosophy … identical”; “resolutions should not differ more than a factor two or three”. | — | H 코드 대조 대상 아님 | 타 모델과의 과학적 비교와 중첩 권고는 명령 지원 판정과 구분한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-012 | 보간 설명의 생략 | swanuse PDF 18쪽 / 인쇄 10쪽: “tri-linear interpolation”; “bi-linear interpolation in space”. 기술 매뉴얼 swantech PDF 151–152 / 인쇄 143–144의 §8.4 및 웹 `swantech/node93.html`은 삼각형 내부 선형 보간을 설명한다. | `src/swanmain.ftn:5592` `SVALQI = ( WF1*ARRINP(II)   + WF2*ARRINP(II+MXG(IGRID))`; `src/swanmain.ftn:5593` `&               + WF3*ARRINP(II+1) + WF4*ARRINP(II+1+MXG(IGRID)) )`; `src/swanmain.ftn:5594` `&               / SUMWREG`; `src/swanmain.ftn:5616` `CALL SwanInterpolatePoint(SVALQI, XP, YP, ARRINP, EXCFLD(IGRID))`; `src/swanmain.ftn:8847` `SIZE2 = W1*SIZE1 + W3*SIZE3`; `src/swanmain.ftn:8849` `COMPDA(INDX,JX2) = SIZE2*UU/VTOT`; `src/swanout1.ftn:1676` `CALL SwanInterpolateOutput ( VOQ(1,VOQR(4)), VOQ(1,1),` | C 문서 누락 | 사용자 매뉴얼 §2.6의 기본 선형 보간 설명에는 예외값 재정규화·벡터 크기 보정·삼각형 보간의 구분이 빠졌다. 삼각형 보간 자체는 swantech §8.4에 있으므로 네 매뉴얼 전체의 누락으로 판정하지 않는다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-018 | 물리 요약표의 빠진 선택 | swanuse PDF 28쪽 / 인쇄 20쪽: 표 제목 “Overview of physical processes and generation mode”; 풍파 성장에 Snyder·Janssen·Yan을 열거한다. swanuse PDF 67쪽 / 인쇄 59쪽의 GEN3 설명에는 ST6가 있다. | `src/swanpre1.ftn:2983` `ELSE IF (KEYWIS('ST6')) THEN`; `src/swanpre1.ftn:2987` `LWINDM = 8`; `src/swanpre1.ftn:2991` `IWCAP = 8` | C 문서 누락 | 표 2.1을 전체 지원 물리 목록으로 사용하지 않는다. ST6 설명은 GEN3 본문에 있으므로 C 판정은 이 요약표에 한정한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-020 | 두 자리 연도 범위 | swanuse PDF 27쪽 / 인쇄 19쪽: “between the years 1931 and 2030”; “formats 2-6”. | `src/ocpids.ftn:494` `INTEGER :: JUMPYEAR = 30`; `src/ocpids.ftn:507` `DTTIME(1) = 2000 + DTTIME(1)`; `src/ocpids.ftn:509` `DTTIME(1) = 1900 + DTTIME(1)`; `src/ocpids.ftn:528` `READ (TIMSTR, '(I2,2(1X,I2))', ERR=98) (DTTIME(II), II=4,6)`; `src/ocpids.ftn:506` `IF (DTTIME(1).LT.JUMPYEAR) THEN` | B 문서 오기 | 형식 2·3·5·6은 1930–2029를 표현한다. 형식 4는 시각만 읽는다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R7:I-043 | 두 자리 연도 유효 범위 | swanimp PDF 28쪽, 인쇄 22쪽: `January 1, 1911 and December 31, 2010 (both inclusive)` | `src/ocpids.ftn:494` `INTEGER :: JUMPYEAR = 30     ! Used in interpretation of 2-digit year code`; `src/ocpids.ftn:506` `IF (DTTIME(1).LT.JUMPYEAR) THEN`; `src/ocpids.ftn:507` `DTTIME(1) = 2000 + DTTIME(1)`; `7ee8981:src/ocpids.ftn:494` `INTEGER :: JUMPYEAR = 30     ! Used in interpretation of 2-digit year code` | B 문서 오기 | 41.51 공개 코드도 두 자리 연도의 분기값으로 30을 사용한다. 형식 2·3·5·6의 연도 범위는 1930–2029이다. 1911–2010이라는 문서 범위는 같은 판의 코드와 다르다. swanimp PDF 28쪽 이미지의 1911–2010 표기를 확인했다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:F-010 | 실험실부터 전 지구 규모 | `website/features/features.htm:48–50` `<li>Propagation from` | — | H 코드 대조 대상 아님 | 적용 규모 주장이다. [10-13 결론 검증 보완] [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:S-001 | 설정의 적용 범위 | `website/settings/settings.htm:30–33` `There is no such thing as one single list of parameter settings that can be used for various applications (e.g., hindcasts, forecasts, regional` | — | H 코드 대조 대상 아님 | 환경·목적별 권고이다. 하나의 설정으로 모든 적용을 대표할 수 없다는 조건을 유지한다. [10-13 결론 검증 보완] [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:S-006 | 지역 규모 시험·개방 연안 | `website/settings/settings.htm:52` `Below an overview of the various tested source term parametrizations available for open water systems at the coastal and regional scale O(10-100 km).<br>` | — | H 코드 대조 대상 아님 | O(10-100 km)에서 시험된 적합성 주장이다. 코드의 공간 크기 상한으로 바꾸지 않는다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:S-016 | 복잡한 현장 정확성 | `website/settings/settings.htm:162–163` `SWAN to make accurate wave predictions over complex field sites.<br><br></td>` | — | H 코드 대조 대상 아님 | 정확한 예측이 가능하다는 적용 성능 주장이다. [10-13 결론 검증 보완] [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:S-018 | 파일 주석의 출처·용도·도입판 | `website/settings/basin.swn:1` `$ settings suitable for estuaries, tidal inlets and lakes`; `website/settings/booij99.swn:1`, `website/settings/tud.swn:1`, `website/settings/tud2.swn:1`은 출처·도입판을 적는다. `website/settings/fort.26.v41.10:1`, `website/settings/fort.26.v41.31:1`은 SWAN+ADCIRC 결합 설정의 도입판을 적는다. | — | H 코드 대조 대상 아님 | 여섯 파일의 1행은 시험·적용 용도 또는 출처의 설명이다. [10-13 결론 검증 보완] [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:S-019 | 수렴 설정 권고 | `website/settings/tud2.swn:8–9` `$ to terminate the SWAN computation properly, using the numerical settings below is recommended` | `src/swanpre1.ftn:1952` `CALL ININTG ('MXITST' , MXITST   , 'STA', 50)                 40.41` | H 코드 대조 대상 아님 | 권장 수렴 설정이다. MXITST=50은 반복 상한이며 수렴 성공을 보장하는 값이 아니다. [10-13 결론 검증 보완] [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
