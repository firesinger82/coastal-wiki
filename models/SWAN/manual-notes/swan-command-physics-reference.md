---
title: "SWAN swanuse §4.5.4 Physics commands reference — GEN/WCAPPING/QUADRUPL/BREAKING/FRICTION/TRIAD/VEGETATION 구문·default verbatim"
topic: swan
canonical_source: external
external_source: "swanuse.pdf (User Manual, SWAN Cycle III version 41.51) §4.5.4 Physics (p.57-83) + node28.md. 각 command 구문·파라미터·default·키워드. swantech 물리(이론)의 user-command 대응."
citation_status: verified
verification_method: "swanuse website_markdown node28.md (Physics, 1577줄) 직접 read: GEN1/2/3(ST6 RBW12 calibration lines)·SSWELL·NEGATINP·WCAPPING·QUADRUPL·BREAKING·FRICTION·TRIAD·VEGETATION 구문+default verbatim. swanuse.pdf §4.5.4 TOC 대조. 나머지(MUD/SICE/TURBULENCE/BRAGG/LIMITER/OBSTACLE/SETUP/DIFFRACTION/SURFBEAT/SCAT/OFF)는 요약. **2026-09-28 SCOPED EDIT**: §11 ASTD 미사용 — swanpre1.ftn:1388-1391·:2780, swanmain.ftn:4972-4974, swanout1.ftn:2714, swancom1-5·SdsBabanin ASTD grep 0건. 2026-10-13 recovery 대조 보고서 R1–R8 반영."
last_source_check: 2026-10-13 (recovery 대조 반영)
note_author: "Claude Opus 4.8 (1M context) raw markdown direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — command 구문·default 값 verbatim"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/manual-notes/swan-tech-ch2-dissipation-detailed.md
  - models/SWAN/manual-notes/swan-tech-ch2-nonlinear-detailed.md
  - models/SWAN/manual-notes/swan-tech-ch2-sources-sinks.md
---

# SWAN swanuse §4.5.4 Physics commands reference — verified

> swanuse.pdf (User Manual v41.51) §4.5.4 Physics 직접 read. **이론(swantech) ↔ user command(swanuse)** 대응 — 각 물리 command 의 정확 **구문·파라미터·default**. [swan-documentation-stack](swan-documentation-stack.md) 가 forward-link 한 command reference (physics 부분). 이론 detail 은 각 `swan-tech-ch2-*` 참조.

## 1. GEN3 — wind input + quadruplet + whitecapping 3rd-gen ★

```
GEN3 < KOMen [cds2] [stpm] | -> WESTHuysen | ST6 [a1sds] [a2sds] [p1sds] [p2sds] ... > (AGROW [a])
```
- **3rd-gen mode** (wind input + quadruplet + whitecapping 동시). 삼파 상호작용과 바닥 마찰은 명령을 생략하면 꺼진다. 수심 쇄파는 명령을 생략해도 켜진다. GEN3는 수심 쇄파를 새로 활성화하지 않는다. `src/swanmain.ftn:1113` `ISURF  = 1`.
- **WESTH = default** (saturation-based whitecapping + Yan 1987 wind, [swan-tech-ch2-dissipation-detailed](swan-tech-ch2-dissipation-detailed.md) §2)
- **KOMEN**: WAM Cycle 3 (Komen 1984 exp growth). `cds2=2.36e-5`, `stpm=3.02e-3`
- **JANSSEN**: WAM Cycle 4. `cds1=4.5`, `delta=0.5`
- **ST6** (Rogers 2012 RBW12, [swan-tech-ch2-dissipation-detailed](swan-tech-ch2-dissipation-detailed.md) §4): `a1sds`(local diss T1) `a2sds`(cumulative T2) `p1sds=p2sds=4`. 키워드: `UP`(default, E_T norm)/DOWN, wind drag `HWANG`(default)/FAN/ECMWF, `VECTAU`(default)/SCATAU, `U10PROXY [windscaling]`(default, U10=windscaling×U_*, **windscaling 32** — RBW12 28에서 변경)/TRUE10, `DEBIAS [cdfac]`(DEBIAS를 적으면 CDFAC는 필수)

ST6의 두 소산 계수는 생략할 수 있다. 초기값은 각각 2.8E-6과 3.5E-5다. `src/swanmain.ftn:1376` `A1SDS       = 2.8E-6`; `src/swanmain.ftn:1377` `A2SDS       = 3.5E-5`. DEBIAS를 적으면 CDFAC는 필수다. `src/swanpre1.ftn:3028` `CALL INREAL ( 'CDFAC', CDFAC, 'REQ', 1. )`.
- **AGROW**: linear growth(Cavaleri-Malanotte-Rizzoli 1981) 활성, `a=0.0015`. 미사용 시 nonstationary INIT ZERO 에선 경계/AGROW 없으면 에너지 0 유지

**ST6 권장 calibration lines** (RBW12, [windscaling]별 a1sds/a2sds 상이):
```
GEN3 ST6 4.7E-7 6.6E-6 U10P 28. AGROW      ! windscaling 28
GEN3 ST6 2.8E-6 3.5E-5 U10P 32. AGROW      ! windscaling 32 (mean square slope 개선)
GEN3 ST6 6.5E-6 8.5E-5 ... U10PROXY 35.0 AGROW
```
> 문서는 SSWELL을 명시하라고 안내한다. 코드 초기값은 ARDHUIN 너울 소산을 선택한다. swanuse PDF 70쪽 / 인쇄 62쪽: “this SSWELL command should be provided”. `src/swanmain.ftn:1390` `ARDHUIN     = .TRUE.`.

## 2. SSWELL — swell dissipation (ST6 짝)

```
SSWELL < -> ARDhuin [cdsv] | ZIEger [b1] >
```
- **ARDHUIN** (Ardhuin 2010, WW3/ST4 non-breaking) `cdsv=1.2` 예
- **ZIEGER**: ZIEGER B1을 생략하면 0.00025를 쓴다. `src/swanpre1.ftn:3128` `CALL INREAL ('B1', B1Z, 'STA', 0.00025)`. NEGATINP를 적으면 RDCOEF는 필수다. 명령 전체를 생략한 초기값은 0이다. `src/swanpre1.ftn:3141` `CALL INREAL('RDCOEF',RDCOEF,'REQ',0.)`; `src/swanmain.ftn:1383` `RDCOEF      = 0.`.
> [swan-tech-ch2-dissipation-detailed](swan-tech-ch2-dissipation-detailed.md) §4 SSWELL ZIEGER/ARDHUIN.

## 3. WCAPPING — whitecapping (GEN3 와 별도 조정)

```
WCAP < KOMEN [cds2] [stpm] [powst] [delta] [powk] | -> AB [cds2] [br] CURrent [cds3] >
```
- **AB = default** (Alves-Banner 2003 / Van der Westhuysen 2007): `cds2=5.0e-5`, `br=1.75e-3`(threshold saturation). `CURRENT` (Van der Westhuysen 2012 enhanced current diss) `cds3=0.8`
- **KOMEN**: `cds2=2.36e-5`, `stpm=3.02e-3`, `powst=2`, **`delta=1`** (40.91A부터 변경, 저주파/mean period 개선; 원래 0=WAM Cycle 3), `powk=1`
> [swan-tech-ch2-dissipation-detailed](swan-tech-ch2-dissipation-detailed.md) §1-3 (Eq 2.43-2.58). `OFF WCAP` 비활성.

## 4. QUADRUPL — quadruplet nonlinear

```
QUADrupl [iquad] [lambda] [Cnl4] [Csh1] [Csh2] [Csh3]
```
- **`iquad` = 2 default**: 1=semi-impl DIA/sweep, **2=explicit DIA/sweep**, 3=explicit DIA/iteration (**current 시 권장** — sweep간 freq overlap 비보존 방지), 8=fast(piecewise const interp), 4=Multiple DIA, **51=XNL deep / 52=XNL+WAM depth scaling / 53=XNL finite depth** ([swan-tech-ch2-nonlinear-detailed](swan-tech-ch2-nonlinear-detailed.md) §A.2)
- `lambda=0.25`, `Cnl4=3e7`, `Csh1=5.5`, `Csh2=0.833333`, `Csh3=-1.25` (DIA, [swan-tech-ch2-nonlinear-detailed](swan-tech-ch2-nonlinear-detailed.md) §A.1 Eq 2.75-2.79)
> DIA 는 long-crested·freq resolution 10%+ 편차 시 부정확. `OFF QUAD` 비활성.

## 5. BREAKING — depth-induced breaking

```
BREaking < -> CONstant [alpha] [gamma] | BKD [alpha] [gamma0] [a1] [a2] [a3] >
```
- **CONSTANT = default**: `alpha=1.0`, **`gamma=0.73`** (breaker index H_max/d, Battjes-Stive 1985)
- **BKD** (γ scales with bottom slope β + dimensionless depth kd): `alpha=1.0`, `gamma0=0.54`, `a1=7.59`, `a2=-8.06`, `a3=8.09`
> [swan-tech-ch2-dissipation-detailed](swan-tech-ch2-dissipation-detailed.md) §6 (Eq 2.64-2.68). command 미사용해도 **default breaking 적용** (끄려면 `OFF BREAKING`).

## 6. FRICTION — bottom friction

```
FRICtion < -> JONswap CONstant [cfjon] | COLLins [cfw] | MADsen [kn] | RIPples [S] [D] >
```
- **JONSWAP = default** (Hasselmann 1973): **`cfjon=0.038`** m²s⁻³ (sandy 권장, wind-sea+swell 공통; **0.067 권장 안 함**, smoother Gulf of Mexico 0.019)
- **COLLINS** (1972): `cfw=0.015`
- **MADSEN** (1988): `kn=0.05` m (roughness length)
- **RIPPLES** (Smith 2011, ripple+sediment 의존): `S=2.65`(specific gravity), `D=0.0001` m(sediment diameter)
> [swan-tech-ch2-dissipation-detailed](swan-tech-ch2-dissipation-detailed.md) §5 (Eq 2.59-2.63). cfw/kn 은 INPGRID FRICTION 으로 spatial 가능. **command 미사용 시 friction 무시** (default off).

## 7. TRIAD — triad nonlinear (shallow)

```
TRIad < -> DCTA [trfac] [p] COLL|NONC | LTA [trfac] | FTIM [trfac] | SPB [trfac] [a] > BIPHASE ... TRANSFER ...
```
- **DCTA = default** (Booij 2009): `trfac=4.4`, `p=4/3`(high-freq tail), **`COLL` default**(collinear)/NONC(noncollinear) ([swan-tech-ch2-nonlinear-detailed](swan-tech-ch2-nonlinear-detailed.md) §B.7)
- **LTA** (extended): `trfac=1.0` (§B.4) / **FTIM** (§B.2): `trfac=1.0` / **SPB** (Becq-Girard 1999, §B.3): `trfac=0.9`, `a=0.95`(K=a·k_loc)
- **BIPHASE**: `ELDEBERKY`(default, Ursell `urcrit=0.63` — Eldeberky 0.2/Doering-Bowen 0.63) / `DEWIT`(2022, bed slope+peak period, `lpar=0` no averaging) (§B.5)

비구조 격자는 DEWIT LPAR≠0을 거부한다. `src/swanpre1.ftn:3449` `IF ( OPTG.EQ.5 .AND. PTRIAD(9).NE.0. ) THEN`; `src/swanpre1.ftn:3452` `PTRIAD(9) = 0.`.
- **TRANSFER** (DCTA 제외): FG(Freilich-Guza1984)/MS(Madsen-Sørensen1993)/BREDMOSE(2005)/**QUADWAVE=default**(Akrish 2024) (§B.6)
> command 미사용 시 **triad 무시**.

## 8. VEGETATION — wave damping (vegetation)

```
VEGEtation [iveg] < [height] [diamtr] [nstems] [drag] >
```
- **`iveg`=1 default** (Suzuki 2011, Dalrymple 1984 cylinder, freq-uniform) / 2 (Jacobsen 2019 freq-dependent canopy, **수직 layering 미지원**)
- 수직 segment 별 `height`/`diamtr`/`nstems`/`drag`를 반복한다. NSTEMS는 양의 정수 필수 입력이다. 생략 시 정상 기본값 처리 대신 입력 오류가 발생한다. `src/swanpre1.ftn:2692` `CALL ININTG ('NSTEMS',NN,'REQ', 1 )`; `src/swanpre1.ftn:2693` `IF ( NN.LE.0 ) THEN`.
> [swan-tech-ch2-vegetation-ice-bragg-gen12](swan-tech-ch2-vegetation-ice-bragg-gen12.md) §2.3.5.

## 9. 기타 physics command (요약, default off 또는 별도)

| command | 기능 | 본 위키 |
|---|---|---|
| `NEGATINP [rdcoef]` | negative wind input (swell, ZIEGER 짝) | dissipation §4 |
| `MUD [layer] [rhom] [viscm]` | fluid mud 감쇠 | (없음) |
| `SICE` (R19/D15/M18/R21B) | AICE는 SICE의 위치 인수가 아니다. 균일 해빙 농도와 두께는 ICE에서 읽는다. `src/swanpre1.ftn:2625` `CALL INREAL('AICE',PICE(1),'REQ',0.)`; `src/swanpre1.ftn:2626` `CALL INREAL('HICE',PICE(2),'REQ',0.)`. | veg-ice-bragg §2.3.6 |
| `TURBULENCE` | 난류 점성 입력장 읽기만으로 ITURBV가 켜지지 않는다. TURB CURRENT는 점성 파일 없이 수심·유속으로 값을 만든다. `src/swanpre1.ftn:4355` `VARTUR = .TRUE.`; `src/swanpre1.ftn:2741` `ITURBV = 1`; `src/swanpre1.ftn:2744` `IF (KEYWIS('CUR')) THEN`. | (없음) |
| `BRAGG` (FT/FILE) | BRAGG의 바닥 스펙트럼 선택은 FT 또는 FILE이다. `src/swanpre1.ftn:3495` `CALL INKEYW ('STA', 'FT')`. | veg-ice-bragg §2.3.7 |
| `LIMITER [ursell] [qb]` | Ursell·Qb limiter | (없음) |
| `OBSTACLE` (TRANS/REFL/FREEBOARD) | sub-grid obstacle | [swan-tech-ch2-obstacles-diffraction-setup](swan-tech-ch2-obstacles-diffraction-setup.md) §1-3 |
| `SETUP [supcor]` | wave-induced set-up (open coast) | obstacles-diffraction-setup §5 / [swan-tech-ch4-5-bc-2d-setup](swan-tech-ch4-5-bc-2d-setup.md) |
| `DIFFRACtion [idiffr] [smpar] [smnum] [cgmod]` | 생략값은 각각 1, 0, 0, 1이다. `CGMOD=0`은 지리 전파속도의 회절 배율 적용을 끈다. swanuse PDF 87–88쪽 / 인쇄 79–80쪽. `src/swanpre1.ftn:2115` `CALL ININTG ('IDIFFR', IDIFFR, 'STA', 1)`; `src/swanpre1.ftn:2118` `CALL INREAL ('CGMOD', PDIFFR(3), 'STA', 1.)`. | obstacles-diffraction-setup §4 |
| `SURFBEAT` | Reniers와 Zijlema의 IEM을 활성화한다. 1D 모드·곡선 격자·비구조 격자에서는 사용할 수 없다. swanuse PDF 88쪽 / 인쇄 80쪽: `CANNOT BE USED IN CASE OF CURVILINEAR or UNSTRUCTURED GRIDS AND NOT IN 1D-MODE.` | [swan-surfbeat-iem](../source-analysis/swan-surfbeat-iem.md) | [10-13 전수 검증 정정]
| `SCAT` | quasi-coherent scattering (Smit-Janssen 2013) | [swan-quasi-coherent](../source-analysis/swan-quasi-coherent.md) / [swan-tech-ch2-7-qcm-theory](swan-tech-ch2-7-qcm-theory.md) |
| `OFF <BREAKING\|WCAP\|QUAD\|...>` | 특정 process 비활성 | — |

## 10. 핵심 default 요약표 (실무 tuning)

| command | default | 주요 default 값 |
|---|---|---|
| GEN3 | WESTH | windscaling 32(ST6), AGROW a=0.0015 |
| WCAP | AB | cds2=5e-5, br=1.75e-3 / KOMEN cds2=2.36e-5, **delta=1** |
| QUADRUPL | iquad=2 | lambda=0.25, Cnl4=3e7 |
| BREAKING | CONSTANT | **alpha=1, gamma=0.73** |
| FRICTION | (off; JONSWAP cfjon=0.038 권장) | Collins 0.015 / Madsen kn=0.05 |
| TRIAD | (off; DCTA trfac=4.4 p=4/3) | SPB a=0.95, BIPHASE urcrit=0.63 |

> KOMEN의 기본 `cds2=2.36e-5`는 swantech PDF 30쪽 / 인쇄 22쪽의 WAM Cycle 3 계수 `Cds = 2.36 × 10⁻⁵`와 같다. 기본 쇄파 계수 `gamma=0.73`은 swantech PDF 36쪽 / 인쇄 28쪽의 Battjes와 Stive 자료 평균값이다. 식 (2.68)은 PDF 35쪽 / 인쇄 27쪽의 쇄파 소산식이다. [swan-tech-ch2-dissipation-detailed](swan-tech-ch2-dissipation-detailed.md). [10-13 전수 검증 정정]

## 11. 한계

- ★ **대기 안정도 보정 없음 (소스 직독 2026-09-28).** 기온-수온차 `ASTD` 는 `INPGRID ASTD`(`swanpre1.ftn:1388-1391`)·`WIND ... ASTD`(`:2780`, `CASTD`) 로 읽혀 보간·저장·출력(`swanmain.ftn:4972-4974`, `swanout1.ftn:2714`)만 되고, `swancom1-5.ftn`·`SdsBabanin.ftn90` 에 `ASTD` 참조 0건, `CASTD` 는 초기화·읽기·0 대입 외 사용 없음 → GEN3 풍입력 어디에도 안정도 보정이 들어가지 않는다. swanuse 매뉴얼도 `ASTD` 를 기술하지 않는다. `SET [level]` 은 수위 증분이지 안정도 설정이 아니다([swan-command-setup-grid-reference](swan-command-setup-grid-reference.md)). 발견 경위: `concepts/sst/06 §8` 오기 정정.

- MUD·TURBULENCE·LIMITER·OBSTACLE·SETUP·DIFFRACTION·SURFBEAT·SCAT의 파라미터와 기본값은 아래 문서와 코드 차이 표에 기록한다.
- swanuse §4.4 Start-up(PROJECT/SET/MODE/COORDINATES) + §4.5.1-3 grid/input/BC + §4.5.5 NUMERIC + §4.6 output command 미커버 (별도 노트).
- ST6 [a1sds]/[a2sds] 의 windscaling별 calibration 상호의존 — RBW12 원논문([swan-foundational-papers](../web-refs/swan-foundational-papers.md)) 참조.

## 12. 연결

- [swan-documentation-stack](swan-documentation-stack.md) — 4 docs + 57 command 목록 (본 노트가 physics 부분 deep)
- [swan-tech-ch2-dissipation-detailed](swan-tech-ch2-dissipation-detailed.md) — WCAPPING/BREAKING/FRICTION/ST6 이론
- [swan-tech-ch2-nonlinear-detailed](swan-tech-ch2-nonlinear-detailed.md) — QUADRUPL/TRIAD 이론
- [swan-tech-ch2-sources-sinks](swan-tech-ch2-sources-sinks.md) — GEN wind input 이론
- [swan-foundational-papers](../web-refs/swan-foundational-papers.md) — Rogers2012(ST6)·Becq-Girard1999(SPB)·Akrish2024(QuadWave) 원논문

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

빈 인용 칸은 `—`로 표시한다. 표의 절 번호는 각 행이 링크한 대조 보고서의 절 번호다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R3:NT-047 | 회절 명령의 CGMOD 누락 | `manual-notes/swan-command-physics-reference.md:122` `DIFFRACtion [idiffr] [smpar] [smnum]`. swanuse PDF 87–88·DIFFRACTION 절(node28:3035,3155–3164)은 CGMOD를 포함한 구문과 기본값을 이미 적는다. | `src/swanpre1.ftn:2115` `CALL ININTG ('IDIFFR', IDIFFR, 'STA', 1)`; `src/swanpre1.ftn:2116` `CALL INREAL ('SMPAR', PDIFFR(1), 'STA', 0.0)`; `src/swanpre1.ftn:2117` `CALL INREAL ('SMNUM', PDIFFR(2), 'STA', 0.)`; `src/swanpre1.ftn:2118` `CALL INREAL ('CGMOD', PDIFFR(3), 'STA', 1.)` | C 문서 누락 | 명령 형식을 `DIFFRACtion [idiffr] [smpar] [smnum] [cgmod]`로 보충한다. 생략값은 각각 1, 0, 0, 1이다. `CGMOD=0`은 지리 전파속도의 회절 배율 적용을 끈다. [R3](../../../_staging/recovery/compare/swan-theory-obstacles-setup-qc-bc-vs-code.md#5-차이-결론) |
| R5:PN-003 | GEN1/2 CDRAG | GEN1/2 CDRAG. swanuse PDF 65쪽 / 인쇄 57쪽: `[cdrag] drag coefficient. Default: [cdrag] = 0.0012`. | `src/swanpre1.ftn:2822` `CALL INREAL ('CDRAG',  PWIND(11), 'UNC', 0.)`; `src/swanmain.ftn:1468` `PWIND(11) = 0.00123`; `src/swancom3.ftn:457` `FACTA = PWIND(1) * PI * PWIND(9)**2 * PWIND(11)**2 / GRAV**2` | B 문서 오기 | CDRAG의 실행 기본값은 0.00123이다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-008 | ST6 A1SDS/A2SDS 기본값 | GEN3 ST6 A1SDS/A2SDS. swanuse PDF 69쪽 / 인쇄 61쪽: `[a1sds] coefficient related to local dissipation term T1.`, `[a2sds] coefficient related to cumulative dissipation term T2.` 기본값 문장은 없다. | `src/swanpre1.ftn:2992` `CALL INREAL ('A1SDS', A1SDS, 'UNC', 0.)`; `src/swanpre1.ftn:2993` `CALL INREAL ('A2SDS', A2SDS, 'UNC', 0.)`; `src/swanmain.ftn:1376` `A1SDS       = 2.8E-6`; `src/swanmain.ftn:1377` `A2SDS       = 3.5E-5`; `src/SdsBabanin.ftn90:225` `T1(IS)=A1SDS*F(IS)*ANAR(IS)*NDEDENS(IS)**P1SDS` | C 문서 누락 | ST6의 두 소산 계수는 생략할 수 있다. 초기값은 각각 2.8E-6과 3.5E-5다. swanuse PDF 68쪽 / 인쇄 60쪽의 `GEN3 ST6 2.8E-6 3.5E-5 U10P 32. AGROW`에도 값은 나오지만 생략 시 기본값이라는 설명은 없다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-011 | WINDSCALING | GEN3 ST6 TRUE10/U10PROXY. swanuse PDF 67쪽 / 인쇄 59쪽: `Default is U10PROXY with [windscaling] = 32`. swanuse PDF 69쪽 / 인쇄 61쪽: `U10 = [windscaling] × U∗`, `Default: [windscaling] = 28.` | `src/swanpre1.ftn:3017` `CALL INKEYW ('STA', 'U10P')`; `src/swanpre1.ftn:3019` `TRUE_U10 = .TRUE.`; `src/swanpre1.ftn:3024` `CALL INREAL ( 'WINDSCALING', WNDSCL, 'UNC', 0. )`; `src/swanmain.ftn:1384` `WNDSCL      = 32.     ! see notes in SdsBabanin.f90`; `src/SdsBabanin.ftn90:599` `TEMP2 = WIND10  !  "TEMP2=WIND10" is basically saying "use DBYB as is"`; `src/SdsBabanin.ftn90:601` `TEMP2 = WNDSCL * UFRIC`; `src/swanmain.ftn:1384` `WNDSCL      = 32.` | B 문서 오기 | WINDSCALING의 실행 기본값은 32다. 매뉴얼 계수표의 28은 본문 및 코드와 다르다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-012 | DEBIAS의 CDFAC | GEN3 ST6 DEBIAS CDFAC. swanuse PDF 67쪽 / 인쇄 59쪽: `This option is effective only if HWANG is also used.` swanuse PDF 69쪽 / 인쇄 61쪽: `Default: [cdfac] = 1.` | `src/swanpre1.ftn:3028` `CALL INREAL ( 'CDFAC', CDFAC, 'REQ', 1. )`; `src/swanmain.ftn:1385` `CDFAC       = 1.      ! factor on Cdrag to counter bias in winds`; `src/swancom3.ftn:1059` `ELSE IF (IDRAG.EQ.4) THEN`; `src/swancom3.ftn:1074` `UFRIC = MIN(USCAP,UFRIC) * SQRT(CDFAC)` | B 문서 오기 | DEBIAS를 적으면 CDFAC는 필수다. 값을 생략하면 입력 오류가 발생한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-014 | SSWELL 생략 | SSWELL ARDHUIN CDSV. swanuse PDF 70쪽 / 인쇄 62쪽: `SSWELL`의 기본 선택 `ARDhuin [cdsv]`. `Default: [cdsv] = 1.2`. `if GEN3 ST6... command is used, this SSWELL command should be provided.` | `src/swanpre1.ftn:3118` `CALL INKEYW ('STA', 'ARD')`; `src/swanpre1.ftn:3124` `ARDHUIN = .TRUE.`; `src/swanpre1.ftn:3125` `CALL INREAL ('CDSV', CDSV, 'STA', 1.2)`; `src/swanmain.ftn:1382` `CDSV        = 1.2`; `src/swancom1.ftn:7519` `IF (IWCAP.EQ.8) THEN`; `src/swancom1.ftn:7529` `ELSE IF (ARDHUIN) THEN`; `src/SdsBabanin.ftn90:2046` `SWDIS(ID,IS) = RHOAW * CDSV * 2.0 * KWAVE(IS,1)  &`; `src/swanmain.ftn:1390` `ARDHUIN     = .TRUE.` | C 문서 누락 | 문서는 SSWELL을 명시하라고 안내한다. 코드 초기값은 ARDHUIN 너울 소산을 선택한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-015 | ZIEGER B1 | SSWELL ZIEGER B1. swanuse PDF 70쪽 / 인쇄 62쪽: `[b1] non-dimensional proportionality coefficient.` 기본값 문장은 없다. | `src/swanpre1.ftn:3127` `ZIEGER = .TRUE.`; `src/swanpre1.ftn:3128` `CALL INREAL ('B1', B1Z, 'STA', 0.00025)`; `src/swanmain.ftn:1386` `B1Z         = 0.00025`; `src/SdsBabanin.ftn90:2200` `SWDIS(IS) = 2.0*B1Z*SPCSIG(IS)*SQRTBN(IS)/3.0` | C 문서 누락 | ZIEGER B1을 생략하면 0.00025를 쓴다. swanuse PDF 70쪽 / 인쇄 62쪽의 예제 `SSWELL ZIEGER 0.00025`에도 같은 값이 있으므로 누락은 생략 시 기본값 설명에 한정한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-016 | NEGATINP의 RDCOEF | NEGATINP RDCOEF. swanuse PDF 70–71쪽 / 인쇄 62–63쪽: `NEGatinp [rdcoef]`, `fraction between 0 and 1`, `Default [rdcoef]=0.0`. | `src/swanpre1.ftn:3141` `CALL INREAL('RDCOEF',RDCOEF,'REQ',0.)`; `src/swanmain.ftn:1383` `RDCOEF      = 0.`; `src/swanmain.ftn:3801` `IF ( RDCOEF.LT.0. .OR. RDCOEF.GT.1. ) THEN` | B 문서 오기 | NEGATINP를 적으면 RDCOEF는 필수다. 명령 전체를 생략한 초기값은 0이다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-018 | ST6 보정·권고 | swanuse PDF 67–68쪽 / 인쇄 59–60쪽의 ST6 보정 예, UP·VECTAU 권고, `a Hs decrease from 2.48 to 2.28 m`, swanuse PDF 71쪽 / 인쇄 63쪽의 `0.04 is recommended`. | — | H 코드 대조 대상 아님 | 보정 예와 RDCOEF 값은 문서의 적용 권고다. 입력 계수의 구현과 성능 근거를 구분한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-025 | IQUAD 3/8의 첫 반복 | QUADRUPL 3/8의 갱신 주기. swanuse PDF 72쪽 / 인쇄 64쪽: `fully explicit computation` … `per iteration`. | `src/swancom1.ftn:7637` `IF ( ITER .EQ. 1 ) THEN`; `src/swancom1.ftn:7643` `CALL SWSNL3 (                  WWINT   ,WWAWG   ,`; `src/swancom1.ftn:7703` `IF ( ITER .EQ. 1 ) THEN`; `src/swancom1.ftn:7709` `CALL SWSNL8 (WWINT   ,UE      ,SA1     ,SA2     ,SPCSIG  ,` | C 문서 누락 | 구조 격자에서 IQUAD 3/8은 첫 반복에 매 sweep마다 계산한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-032 | DIA·마찰 권고 | swanuse PDF 72쪽 / 인쇄 64쪽의 DIA 방향·주파수 해상도 한계와 IQUAD=3/8 권고. swanuse PDF 74쪽 / 인쇄 66쪽의 모래 바닥 `0.038` 및 매끄러운 해저 `0.019` 권고. | `src/swanmain.ftn:6662` `IF (ABS(GAMMA-1.1).GT.0.055) THEN` | H 코드 대조 대상 아님 | 마찰 권고값과 DIA 정확도 설명을 모든 격자의 검증 결과로 쓰지 않는다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-038 | DEWIT LPAR | TRIAD BIPHASE DEWIT LPAR. swanuse PDF 76쪽 / 인쇄 68쪽: `[lpar] = 0 means no averaging. Default: [lpar] = 0.` | `src/swanpre1.ftn:3446` `ELSEIF (KEYWIS('WIT') .OR. KEYWIS('DEWIT')) THEN`; `src/swanpre1.ftn:3448` `CALL INREAL ('LPAR', PTRIAD(9), 'STA', 0.)`; `src/swanpre1.ftn:3449` `IF ( OPTG.EQ.5 .AND. PTRIAD(9).NE.0. ) THEN`; `src/swanpre1.ftn:3452` `PTRIAD(9) = 0.`; `src/swancom4.ftn:5772` `LPAR = PTRIAD(9)`; `src/swancom4.ftn:5777` `IF (LPAR.NE.0.) THEN` | C 문서 누락 | 비구조 격자에서는 DEWIT의 LPAR≠0을 허용하지 않는다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-041 | NSTEMS | VEGETATION NSTEMS. swanuse PDF 77쪽 / 인쇄 69쪽: `number of plant stands per square meter for each layer.`, `Default: [nstems] = 1.`, `will be multiplied by this horizontally varying plant density.` | `src/swanpre1.ftn:2692` `CALL ININTG ('NSTEMS',NN,'REQ', 1 )`; `src/swanpre1.ftn:2693` `IF ( NN.LE.0 ) THEN`; `src/swanpre1.ftn:2695` `NN = 1`; `src/swancom2.ftn:861` `IF ( VARNPL ) SVEG1 = SVEG1 * NPLA2(KCGRD(1))` | B 문서 오기 | NSTEMS는 양의 정수 필수 입력이다. 생략 시 정상 기본값 처리 대신 입력 오류가 발생한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-042 | MUD LAYER | MUD LAYER/RHOM/VISCM. swanuse PDF 77쪽 / 인쇄 69쪽: `MUD [layer] [rhom] [viscm]`, 두 활성 경로 `this command or the commands INPGRID MUDLAY and READINP MUDLAY`, `[layer]` … `(in m)`, `[rhom]` … `(in kg/m3). Default` … `1300.`, `[viscm]` … `(in m2/s). Default` … `0.0076.` | `src/swanpre1.ftn:2587` `IMUD = 1`; `src/swanpre1.ftn:2589` `CALL INREAL('RHOM' ,PMUD(2),'UNC',0.)`; `src/swanpre1.ftn:2590` `CALL INREAL('VISCM',PMUD(3),'UNC',0.)`; `src/swanpre1.ftn:4366` `IMUD   = 1`; `src/swanmain.ftn:1405` `PMUD(1)   = 0.`; `src/swanmain.ftn:1406` `PMUD(2)   = 1300.`; `src/swanmain.ftn:1407` `PMUD(3)   = 0.0076`; `src/swancom1.ftn:7353` `CALL SMUD ( DEP2   ,IMATDA  ,` | C 문서 누락 | 균일 MUD LAYER를 생략하면 초기 두께는 0 m다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-045 | SICE의 AICE 설명 | SICE AICE. swanuse PDF 78–79쪽 / 인쇄 70–71쪽: `[aice] ice concentration as a fraction from 0 to 1.`, `The value of [aice] in this command is then not required`. | `src/swanpre1.ftn:2625` `CALL INREAL('AICE',PICE(1),'REQ',0.)`; `src/swancom1.ftn:7315` `IF ( VARAICE ) THEN`; `src/swancom1.ftn:7316` `AICELOC = AICE2(KCGRD(1))`; `src/swancom1.ftn:7318` `AICELOC = PICE(1)` | B 문서 오기 | AICE는 SICE의 위치 인수가 아니다. 균일 농도는 ICE 명령에서 읽는다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-046 | IC4M2 | IC4M2. 현재 swanuse PDF 78쪽 / 인쇄 70쪽의 물리 명령명은 `SICE`다. IC4M2는 사용자 요청에 따라 별도 대조한다. | `src/swanpre1.ftn:2603` `! Note that IC4M2 is deprecated in manual but left intact`; `src/swanpre1.ftn:2605` `IF (KEYWIS ('IC4M2')) THEN`; `src/swanpre1.ftn:2606` `IICE = 3` | C 문서 누락 | IC4M2의 옛 필수 인수 문법은 코드에 남아 있다. swantech PDF 55쪽과 웹 `swantech/node21.html:97`의 IC4M2는 WW3 방법 설명이다. SWAN 입력 명령의 호환 문법과 필수 인수 설명은 별도로 보충한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-048 | TURB 입력·활성화 | TURBULENCE의 읽기 명령과 자동 활성화. swanuse PDF 79쪽 / 인쇄 71쪽: `This physical effect is also activated by reading values of the turbulent viscosity using the READGRID TURB command`, `The command READGRID TURB is necessary if this command TURB is used`. | `src/swanpre1.ftn:1453` `IF (KEYWIS ('READ')) THEN`; `src/swanpre1.ftn:4355` `VARTUR = .TRUE.`; `src/swanmain.ftn:1119` `ITURBV = 0`; `src/swanpre1.ftn:2741` `ITURBV = 1`; `src/swanpre1.ftn:2750` `VARTUR = .TRUE.`; `src/swancom1.ftn:7373` `IF ( ITURBV.GE.1 ) THEN` | B 문서 오기 | 값 읽기는 READINP TURB다. 난류 소산 활성화에는 TURB 명령이 필요하다. CURRENT 경로에서는 점성 파일을 요구하지 않는다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-052 | LIMITER의 영구·경계값 표현 | LIMITER URSELL/QB. swanuse PDF 81쪽 / 인쇄 73쪽: `de-activate permanently the quadruplets when the actual Ursell number exceeds [ursell]`, `as soon as` … `exceeds [qb] then the action limiter will not be used in case of decreasing action density`. 기본값은 `10.0`, `1.0`이다. | `src/swanpre1.ftn:1902` `CALL INREAL('URSELL',PTRIAD(3),'UNC',0.)`; `src/swanpre1.ftn:1903` `CALL INREAL('QB'    ,PNUMS(28),'UNC',0.)`; `src/swanmain.ftn:1438` `PTRIAD(3)  = 10.`; `src/swanmain.ftn:1280` `PNUMS(28) = 1.`; `src/swancom1.ftn:7592` `IF (URSELL(KCGRD(1)).LT.PTRIAD(3)) THEN`; `src/swancom1.ftn:7988` `IF (QB_LOC.LT.PNUMS(28)) THEN` | B 문서 오기 | URSELL·QB 조건은 현재 격자점에서 다시 검사한다. 문턱과 같은 경우에도 해당 계산·감소 제한을 건너뛴다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-053 | TRANSM TRCOEF | OBSTACLE TRANSM TRCOEF. swanuse PDF 83쪽 / 인쇄 75쪽: `Default: [trcoef]=0.0 (no transmission = complete blockage).`, 계수는 유의파고 비다. | `src/swanpre1.ftn:1084` `CALL INREAL ('TRCOEF', TRCF, 'REQ', 0.)`; `src/swanpre1.ftn:1085` `IF ((TRCF.LT.0.) .OR. (TRCF.GT.1.)) THEN`; `src/swanpre1.ftn:1113` `TRCF  = 0.`; `src/swanser.ftn:3114` `TRCF(1,1) = OBHKT * OBHKT` | B 문서 오기 | TRANSM을 적으면 TRCOEF를 명시해야 한다. TRANSM 전체 생략의 투과계수는 0이다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-058 | RDIFF POWN | OBSTACLE RDIFF POWN. swanuse PDF 84쪽 / 인쇄 76쪽: `cos[pown](θ − θrefl)`, `Default: [pown] = 1.` | `src/swanpre1.ftn:1163` `CALL INREAL ('POWN', POWN, 'REQ', 1.)`; `src/swanpre1.ftn:1164` `DUM = MOD(POWN,1.)`; `src/swanpre1.ftn:1165` `IF (POWN.LT.0.) THEN`; `src/swanpre1.ftn:1168` `IF (DUM.NE.0.) THEN`; `src/swanser.ftn:3320` `POWN     = COBST%RFCOEF(2)` | B 문서 오기 | RDIFF의 POWN은 필수다. 코드는 0 이상의 정수 값을 요구한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-059 | 투과·반사 합 검사 | OBSTACLE 에너지 보존 검사. swanuse PDF 84쪽 / 인쇄 76쪽: `the program checks if the criterion [reflc]2+[trcoef]2 ≤ 1 is fulfilled.` | `src/swanpre1.ftn:1246` `IF (LFREE.EQ.0 .AND. ITRAS.EQ.0 .AND. LREF.EQ.1) THEN`; `src/swanpre1.ftn:1247` `DUM = TRCF*TRCF + REF0*REF0`; `src/swanpre1.ftn:1248` `IF (DUM.GT.1.) CALL MSGERR(3,'Kt^2 + Kr^2 > 1 ')` | C 문서 누락 | 입력 단계의 에너지 합 검사는 FREEBOARD 없는 상수 투과·반사 조합에 한정한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-060 | FREEBOARD와 DAM | OBSTACLE FREEBOARD HGT/GAMMAT/GAMMAR와 DAM 결합. swanuse PDF 84–85쪽 / 인쇄 76–77쪽: HGT는 필수다. 두 gamma의 기본값은 1이다. `freeboard dependency has no effect on the transmission coefficient as computed using the DAM option.` | `src/swanpre1.ftn:1214` `CALL INREAL ('HGT'   , HGT , 'REQ', 0.)`; `src/swanpre1.ftn:1215` `CALL INREAL ('GAMMAT', GAMT, 'STA', 1.)`; `src/swanpre1.ftn:1216` `CALL INREAL ('GAMMAR', GAMR, 'STA', 1.)`; `src/swanmain.ftn:3917` `IF ( IFREE.EQ.1 .AND. (ITRAS.NE.0 .OR. IRFRD.EQ.1) ) THEN`; `src/swanmain.ftn:3921` `IFREE = 0` | C 문서 누락 | DAM 또는 주파수 의존 반사와 결합하면 FREEBOARD 전체를 끈다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-061 | FREEBOARD GAMT=GAMR=0 | OBSTACLE FREEBOARD 두 gamma의 허용값. swanuse PDF 84–85쪽 / 인쇄 76–77쪽: 두 계수 모두 `This parameter should be higher than zero.` | `src/swanpre1.ftn:1217` `IF ( GAMT.LT.0. .OR. GAMR.LT.0. ) THEN`; `src/swanpre1.ftn:1220` `ELSEIF ( GAMT.LT.0.1 ) THEN`; `src/swanpre1.ftn:1222` `GAMT = 0.1`; `src/swanpre1.ftn:1223` `ELSEIF ( GAMR.LT.0.1 ) THEN`; `src/swanpre1.ftn:1225` `GAMR = 0.1`; `src/swanser.ftn:3089` `FBR = 0.5 * ( 1. + TANH(2.*FVH/GAMR) )` | E 코드 결함 후보·강함 | GAMT=GAMR=0인 FREEBOARD 입력은 GAMT만 0.1로 보정한다. GAMR는 저장·재읽기 뒤 `IF ( LFREE.EQ.1 ) THEN`에서 반사식의 분모로 사용된다. 선택 전처리로 꺼지는 행이 아니다. 최초 반입 `b2ae30e`(2022-08-10), 41.51의 `7ee8981`, 현재 `43e9bbb`에서 같은 분기다. CP-004와 같은 강한 결함 후보이다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-064 | 장애물 자동 이동 | 장애물 자동 이동. swanuse PDF 83쪽 / 인쇄 75쪽: `SWAN will move the obstacle` … `(1% of the mesh size)`, `not` … `in case of unstructured grids.` | `src/swanmain.ftn:3873` `CALL SWOBST (XGRDGL, YGRDGL, KGRPGL, CROSSGL)`; `src/swanser.ftn:2497` `X3 = COBST%XCRP(1)`; `src/swanser.ftn:2501` `X4 = COBST%XCRP(JP)` | B 문서 오기 | 2023-10-16에 자동 이동 루틴이 삭제되었다. 41.51 문서의 1% 이동 설명을 현재 동작으로 쓰지 않는다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-065 | 장애물·Bragg 적용 권고 | swanuse PDF 82–86쪽 / 인쇄 74–78쪽의 장애물 배치·반사 정확도 권고. `Avoid sharp angles`, `wet points on both sides`, `reflected spectrum is not taken into account`는 계산 영역 경계 조건이다. swanuse PDF 80쪽 / 인쇄 72쪽의 Bragg 시간간격·완화 권고도 포함한다. | `src/swanser.ftn:2533` `CROSS(ILINK,ICC) = JJ` | H 코드 대조 대상 아님 | 배치·반복 완화·시간 간격의 권고는 실제 격자에서 검증해야 하는 적용 지침이다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-066 | QUAY의 투과 1 | QUAY의 단위 투과 주장 보충. swanuse PDF 85쪽 / 인쇄 77쪽: `the reflection coefficient is set to 0 and the transmission coefficient to 1.` | `src/swanser.ftn:3097` `FBT = 99999.`; `src/swanser.ftn:3098` `FBR = 0.`; `src/swanser.ftn:3113` `OBHKT = MIN(1.,FBT * COBST%TRCOEF(1))` | B 문서 오기 | QUAY는 원래 투과계수가 0인 경우 투과를 1로 만들지 않는다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-068 | SETUP 병렬 제한 | SETUP 격자·병렬 제약. swanuse PDF 86쪽 / 인쇄 78쪽: `CANNOT BE USED IN CASE OF UNSTRUCTURED GRIDS.` swanuse PDF 87쪽 / 인쇄 79쪽: `not computed correctly with spherical coordinates`, `not supported` … `either MPI or OpenMP`. | `src/swanpre1.ftn:2083` `IF (KSPHER.NE.0) CALL MSGERR (2,`; `src/swanpre1.ftn:2085` `IF (PARLL .AND. .NOT.ONED) THEN`; `src/swanpre1.ftn:2086` `CALL MSGERR(4,'setup is not supported in parallel run')`; `src/swanpre1.ftn:2089` `IF (OPTG.EQ.5) THEN`; `src/swanpre1.ftn:2091` `LSETUP = 0`; `src/swanparll.ftn:188` `IF ( NPROC.GT.1 ) THEN`; `src/swanparll.ftn:189` `PARLL = .TRUE.` | C 문서 누락 | 코드의 거부 조건은 PARLL이며 비1D인 경우다. 문서의 미지원 안내와 입력기의 검사 조건을 구분한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-070 | 회절 평활화 부호 | DIFFRACTION 평활화 식. swanuse PDF 87쪽 / 인쇄 79쪽의 쪽 이미지를 직접 확인했다. 원문은 `Eⁿᵢ,ⱼ = Eⁿ⁻¹ᵢ,ⱼ − a [Eᵢ₋₁,ⱼ + Eᵢ,ⱼ₋₁ − 4Eᵢ,ⱼ + Eᵢ₊₁,ⱼ + Eᵢ,ⱼ₊₁]ⁿ⁻¹`이다. | `src/swancom5.ftn:5722–5723` `EN(IND) = ENTMP(IX,IY) -`; `src/swancom5.ftn:5737` `EN(IND) = EN(IND) - TMP*(ENTMP(IX,IY)-ENTMP(IX+1,IY))` | B 문서 오기 | 유효한 내부점의 코드 식은 Enew=Eold+a(이웃 합−4Eold)다. 문서의 라플라시안 부호가 반대다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-074 | SCAT의 다른 물리 선택 변경 | SCAT IQCM. swanuse PDF 90–91쪽 / 인쇄 82–83쪽: `=0 no scattering`, `=1` … `non-uniform bathymetry and currents`, `=2` … `slowly varying bathymetry`, `[iqcm] = 1.` | `src/swanpre1.ftn:3590` `CALL ININTG ('IQCM', IQCM, 'STA', 1 )`; `src/swanmain.ftn:3825` `IF (IQCM.EQ.1) IREFR = 0`; `src/swanmain.ftn:6451` `IQCM = 1`; `src/swanmain.ftn:6454` `IF ( IQCM.NE.0 .AND. IDIFFR.GT.0 ) THEN`; `src/swanmain.ftn:6457` `IDIFFR = 0`; `src/swanmain.ftn:6475` `IF ( IQCM.NE.0 ) THEN`; `src/swanmain.ftn:6480` `PNUMS(8) = 0.`; `src/swanmain.ftn:6481` `ITFRE = 0`; `src/swanmain.ftn:6448` `IF ( ICUR.EQ.0 .AND. IQCM.GT.1 ) THEN` | C 문서 누락 | 흐름이 없으면 IQCM>1은 1로 바뀐다. 굴절은 `IF (IQCM.EQ.1) IREFR = 0` 및 `swanmain.ftn:6461–6464`의 조건부 검사로 끈다. QC 활성 시 주파수 이동을 끄고, `IF ( IQCM.NE.0 .AND. IDIFFR.GT.0 ) THEN`이면 회절을 끈다. 모든 QC 선택에 굴절 비활성화를 일반화하지 않는다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-075 | RFAC | SCAT GRID RFAC. swanuse PDF 90쪽 / 인쇄 82쪽: 해상도 `Δk/rf`, 상관 길이 `2π rf/Δk`. swanuse PDF 91쪽 / 인쇄 83쪽: `factor through which the incident spectral width is multiplied`, `larger or equal 1`, `[rfac] = 1.` | `src/swanpre1.ftn:3603` `CALL INREAL ('RFAC', PSCAT(7), 'STA', 1.)`; `src/swanpre1.ftn:3604` `IF ( PSCAT(7).LT.1. )`; `src/SwanQCM.ftn90:521` `dkx  = sdev / rfac`; `src/SwanQCM.ftn90:522` `dky  = sdev / rfac` | B 문서 오기 | 파수 격자 간격은 스펙트럼 폭을 RFAC로 나눈 값이다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-078 | SETUP·회절·QC 적용 지침 | swanuse PDF 87쪽 / 인쇄 79쪽의 SETUP 개방 해안 적용, 회절 항만·반사물 앞 한계, 공간 해상도 `1/5 to 1/10`, 완화 `0.01`, 필터 폭 `εx = ½√(3n)Δx`. swanuse PDF 90쪽 / 인쇄 82쪽의 QC에서 쇄파·삼파항을 쓰지 말라는 지시. | — | H 코드 대조 대상 아님 | 물리 적용 지침을 입력기에서 모두 금지하는 조건으로 옮기지 않는다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-192 | NEGATINP의 정확한 4% 주장 | NEGATINP의 반대 방향 비교. swanuse PDF 71쪽 / 인쇄 63쪽: `its magnitude is 4% of the corresponding value of the spectral bin that is in the opposite direction (i.e. in the wind direction).` | `src/SdsBabanin.ftn90:621` `TEMP4=( UOVERC * COSDIF - 1.0 )`; `src/SdsBabanin.ftn90:622` `TEMP4=MAX(0.0,TEMP4)`; `src/SdsBabanin.ftn90:623` `WPSI=TEMP4**2`; `src/SdsBabanin.ftn90:694` `TEMP4 = ( UoverC * COSDIF - 1.0 )`; `src/SdsBabanin.ftn90:695` `TEMP4 = MIN(0.0,TEMP4)`; `src/SdsBabanin.ftn90:696` `WPSI = TEMP4**2` | B 문서 오기 | RDCOEF=0.04는 음의 분기 기여에 곱하는 계수다. 반대 방향의 양의 풍입력에 대한 정확한 비율을 보장하지 않는다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-147 | GROWTH/PARW | — | `src/swanpre1.ftn:3218` `IF (KEYWIS('GROWTH') .OR. KEYWIS ('PARW')) THEN`; `src/swanpre1.ftn:3220` `CALL INKEYW ('STA', 'G3')`; `src/swanpre1.ftn:3221` `IF (KEYWIS('G1') .OR. KEYWIS ('SNY1')) THEN`; `src/swanmain.ftn:1465` `PWIND(7)  = 0.`; `src/swanmain.ftn:1466` `PWIND(8)  = -0.56` | C 문서 누락 | 옛 풍입력 문법이 코드에 남아 있다. GEN1/2 본문에 없는 추가 계수도 읽는다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-148 | BREAKING ASYM | — | `src/swanpre1.ftn:2413` `ELSE IF (KEYWIS('ASYM')) THEN`; `src/swanpre1.ftn:2414` `ISURF = 7`; `src/swanpre1.ftn:2415` `CALL INREAL ('ALPHA' , PSURF(1) ,'STA', 1.0)`; `src/swanpre1.ftn:2416` `CALL INREAL ('GAMMA0', PSURF(4) ,'STA', 0.6)`; `src/swanpre1.ftn:2417` `CALL INREAL ('A'     , PSURF(5) ,'STA', 0.8)`; `src/swancom2.ftn:3249` `!        calculate breaker index based on Saprykina et al. (2017)` | C 문서 누락 | ASYM의 기본 ALPHA·GAMMA0·A는 1.0·0.6·0.8이다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-149 | BIPHASE SAPR | — | `src/swanpre1.ftn:3441` `IF (KEYWIS('SAPR')) THEN`; `src/swanpre1.ftn:3442` `IBIPH = 2`; `src/swanpre1.ftn:3443` `CALL INREAL ('A', PTRIAD(9), 'STA', 1.0)`; `src/swanpre1.ftn:3444` `IF (.NOT.PTRIAD(9).NE.0.)`; `src/swancom1.ftn:5922` `BIPHAS(KCGRD(1)) = 0.5*PI * (MIN(1.,DELL/PTRIAD(9)) - 1.)` | C 문서 누락 | SAPR 쌍위상 선택이 존재한다. A는 기본 1이며 0은 허용하지 않는다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-150 | OFF RESCALE/SOURCES | — | `src/swanpre1.ftn:3663` `ELSE IF (KEYWIS ('RESCALE')) THEN`; `src/swanpre1.ftn:3665` `BRESCL = .FALSE.`; `src/swanpre1.ftn:3666` `ELSE IF (KEYWIS ('SOURCES')) THEN`; `src/swanpre1.ftn:3667` `OFFSRC = .TRUE.`; `src/swancom1.ftn:3754` `IF (BRESCL) CALL RESCALE(AC2, ISSTOP, IDCMIN, IDCMAX, NRSCAL)`; `src/SwanCompUnstruc.ftn90:1090` `if ( .not.OFFSRC ) then` | C 문서 누락 | 문서의 OFF 목록 외에 RESCALE과 SOURCES가 있다. SOURCES의 전체 원천항 우회는 비구조 경로에서 확인된다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-153 | 반사 RFD | — | `src/swanpre1.ftn:1181` `IF (KEYWIS('RFD')) THEN`; `src/swanpre1.ftn:1183` `CALL INREAL ('FD1', FD1, 'REQ', 0.565)`; `src/swanpre1.ftn:1184` `CALL INREAL ('FD2', FD2, 'REQ', 0.75)`; `src/swanpre1.ftn:1185` `CALL INREAL ('FD3', FD3, 'REQ', -21.)`; `src/swanpre1.ftn:1186` `CALL INREAL ('FD4', FD4, 'REQ', 0.066)`; `src/swanpre1.ftn:1187` `IF (FD3.GE.0.) THEN`; `src/swanser.ftn:3714–3715` `REF0 = FD1 +` | C 문서 누락 | RFD는 각주파수 의존 반사를 지정한다. FD1–FD4는 필수이며 FD3는 음수여야 한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-159 | RIPPLES의 DRAG 변경 | — | `src/swanmain.ftn:3785` `IF (IWIND.EQ.8) THEN`; `src/swanmain.ftn:3787` `IF (IDRAG.LT.4) IDRAG = 4`; `src/swanmain.ftn:3792` `IF (IBOT.EQ.5) IDRAG = 1` | C 문서 누락 | RIPPLES는 ST6 드래그 검사 뒤에도 IDRAG를 WU로 바꾼다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-160 | YAN·WESTH 계수·DRAG SWELL | swanuse PDF 137쪽 / 인쇄 129쪽 `YAN`, `WESTH [cds2] [br]`, `SWELL` | `src/swanpre1.ftn:2933` `LWINDM = 5`; `src/swanpre1.ftn:3054` `IDRAG = 3` | C 문서 누락 | Appendix C의 YAN·WESTH·DRAG SWELL 문법은 코드에 남아 있다. YAN은 백파 선택을 바꾸지 않는다. swanuse PDF 71쪽 / 인쇄 63쪽의 WCAP AB에는 같은 CDS2·BR 기본값이 있다. C는 GEN3 WESTH의 인수 연결과 DRAG SWELL의 본문 설명에 한정한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-161 | GEN3 BABANIN | swanuse PDF 137쪽 / 인쇄 129쪽 `BABANIN` | `src/swanpre1.ftn:2944` `!         "BABanin"=legacy mode of input ; "ST6"=new mode of input`; `src/swanpre1.ftn:2950` `IDRAG = 4`; `src/swanpre1.ftn:2955` `IWCAP = 8`; `src/swanpre1.ftn:2965` `CALL INKEYW ('REQ', ' ')`; `src/swanpre1.ftn:2977` `VECTOR_TAU = .FALSE.`; `src/swanpre1.ftn:2956` `CALL INREAL ('A1SDS', A1SDS, 'REQ', 0.)` | C 문서 누락 | 옛 BABANIN 입력은 여섯 계수와 UP/DOWN을 명시해야 한다. VECTAU 생략 시 스칼라 응력 적분을 쓴다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-162 | SSWELL ROGERS | swanuse PDF 138쪽 / 인쇄 130쪽 `ROGers [cdsv] [feswell]` | `src/swanpre1.ftn:3120` `ROGERS = .TRUE.`; `src/swanpre1.ftn:3121` `CALL INREAL ('CDSV'   , CDSV   , 'STA', 1.2)`; `src/swanpre1.ftn:3122` `CALL INREAL ('FESWELL', FESWELL, 'REQ', 0. )`; `src/swancom1.ftn:7519` `IF (IWCAP.EQ.8) THEN`; `src/swancom1.ftn:7524` `ELSE IF (ROGERS) THEN`; `src/swancom1.ftn:7525` `CALL SSWELL_ROGERS (SPCSIG, KWAVE, IDCMIN, IDCMAX` | C 문서 누락 | ROGERS의 CDSV 기본값은 1.2다. FESWELL은 필수다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-163 | 추가 WCAPPING 선택 | swanuse PDF 138쪽 / 인쇄 130쪽 `LHIG`, `BJ`, `KBJ` | `src/swanpre1.ftn:2489` `CALL INREAL ('PWTAIL', PWTAIL(1), 'STA', 5.)`; `src/swanpre1.ftn:2490` `IF (PWTAIL(1).LE.1.) CALL MSGERR (3, 'Incorrect PWTAIL')`; `src/swanmain.ftn:1355` `PWCAP(5) = 1.`; `src/swanmain.ftn:1359` `PWCAP(6) = 0.88`; `src/swanmain.ftn:1360` `PWCAP(7) = 1.`; `src/swanmain.ftn:1361` `PWCAP(8) = 0.75`; `src/swancom2.ftn:2531` `C_LH(IS) = PWCAP(5) * EXP(A) * SQRT(ETOT2) * SPCSIG(IS)**2 /`; `src/swancom2.ftn:2502` `IF (IWCAP.EQ.5) HM = PWCAP(6) / KM01 ! (PWCAP(8) * KM_WAM)` | C 문서 누락 | 추가 백파 선택은 Appendix C에 남아 있다. KBJ의 KCONV는 읽지만 현 HM 계산에는 쓰이지 않는다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-164 | MDIA 계수 목록 | swanuse PDF 138쪽 / 인쇄 130쪽 `CNL4_12` | `src/swanpre1.ftn:3162` `CALL INREAL('LAMBDA',RLAMBDA(ILAMBDA+1),'STA',-1.)`; `src/swanpre1.ftn:3163` `IF (RLAMBDA(ILAMBDA+1).LT.0.) THEN`; `src/swanpre1.ftn:3169` `MDIA = ILAMBDA`; `src/swanpre1.ftn:3187` `CNL4_2 = CNL4_1`; `src/swanpre1.ftn:3191` `CNL4_1 = CNL4_1 * ((2.*PI)**9)` | C 문서 누락 | MDIA는 설정별 계수 목록을 읽고 각주파수 단위로 바꾼다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-165 | 추가 BREAKING 선택 | swanuse PDF 138쪽 / 인쇄 130쪽 `VAR`, `RUE`, `TG` | `src/swanpre1.ftn:2388` `CALL INREAL ('COEFF1', PSURF(7), 'STA', 0.88)`; `src/swancom2.ftn:3168` `BRCOEF = PSURF(4) + PSURF(7) * EXP ( -PSURF(8) / DDDS )`; `src/swancom2.ftn:3125` `BRCOEF = PSURF(4)` | C 문서 누락 | VAR·RUE·TG의 실제 기본값은 §3.3의 읽기 값이다. VAR의 GAMMAX는 현 양의 경사 식에 사용되지 않는다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-166 | BKD·방향·주파수 보정 | swanuse PDF 138–139쪽 / 인쇄 130–131쪽 `[npnts]`, `DIRectionality`, `FREQDep` | `src/swanpre1.ftn:2408` `CALL INREAL ('NPNTS' , PNUMS(37),'STA', 95. )`; `src/swanpre1.ftn:2424` `IF (KEYWIS ('DIR').OR.ISURF.EQ.6) THEN`; `src/swanpre1.ftn:2426` `CALL INREAL ('SPREAD', PSURF(15), 'STA', 12.5)`; `src/swancom1.ftn:2347` `IF (MODGAM .AND. ACCUR.GE.PNUMS(37)) MODGAM = .FALSE.`; `src/swancom2.ftn:3326` `KTETA = MAX(1.,DSPR/((PSURF(15)/180.)*PI))`; `src/swancom2.ftn:2163` `FMIN  = PI2*PSURF(17)`; `src/swancom2.ftn:2164` `FMAX  = PI2*PSURF(18)` | C 문서 누락 | BKD는 DIR 생략 시에도 방향 퍼짐 보정을 켠다. NPNTS·SPREAD·FREQDEP 값과 단위는 §3.3을 따른다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-167 | JONSWAP VAR·COLLINS CFC | swanuse PDF 139쪽 / 인쇄 131쪽 `[cfj1] [cfj2] [dsp1] [dsp2]`, `[cfc]` | `src/swanpre1.ftn:2563` `CALL INREAL('CFC',PBOT(1),'UNC',0.)`; `src/swanmain.ftn:1394` `PBOT(1)   = 0.0`; `src/swancom2.ftn:404` `DSP  = SQRT(2.*XDUM) *180./PI`; `src/swancom2.ftn:413–414` `CFBOT(IS) = PBOT(6) + (PBOT(7)-PBOT(6))*(DSP-PBOT(8))/`; `src/swancom2.ftn:526` `IF (IBOT.EQ.2 .AND. ICUR.EQ.1 .AND. PBOT(1).GT.0.) THEN` | C 문서 누락 | JONSWAP VAR은 방향 퍼짐별 계수다. COLLINS CFC>0과 흐름이 함께 있으면 추가 항을 계산한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-168 | MUD RHOW/VISCW | swanuse PDF 140쪽 / 인쇄 132쪽 `[rhow] [viscw]` | `src/swanpre1.ftn:2591` `CALL INREAL('RHOW' ,PMUD(4),'UNC',0.)`; `src/swanpre1.ftn:2592` `CALL INREAL('VISCW',PMUD(5),'UNC',0.)`; `src/swanmain.ftn:1408` `PMUD(4)   = RHO`; `src/swanmain.ftn:1409` `PMUD(5)   = 1.3E-6`; `src/swanser.ftn:861` `RHOW    = PMUD(4)`; `src/swanser.ftn:862` `KINVISW = PMUD(5)`; `src/swanser.ftn:864` `ZETA  = SQRT(KINVISM/KINVISW)`; `src/swanser.ftn:865` `GAMMA = RHOW/RHOM` | C 문서 누락 | MUD는 물의 밀도와 운동점성계수도 읽는다. 초기값은 RHO와 1.3E-6 m²/s다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-169 | TRIAD CUTFR/B/DINT | swanuse PDF 139쪽 / 인쇄 131쪽 `[cutfr] [dint]`, `[b]` | `src/swanpre1.ftn:3351` `CALL INREAL ('CUTFR', PTRIAD(2), 'STA', -1.)`; `src/swanpre1.ftn:3352` `CALL INREAL ('DINT' , PTRIAD(8), 'STA',60.0)`; `src/swanpre1.ftn:3377` `CALL INREAL ('B'    , PTRIAD(7), 'STA', 0.0 )`; `src/swanpre1.ftn:3378` `CALL INREAL ('DINT' , PTRIAD(8), 'STA',-1.  )`; `src/swanpre1.ftn:3390` `CALL INREAL ('DINT' , PTRIAD(8), 'STA',-1.)`; `src/swancom4.ftn:3968` `IF ( PTRIAD(8).NE.-1. ) THEN`; `src/swancom4.ftn:3969` `PWDTH = PTRIAD(8) * PI/180.`; `src/swanmain.ftn:4243` `IF ( .NOT.FULCIR ) MTH = MDC - 1` | C 문서 누락 | LTA의 DINT 기본값은 60°다. SPB·FTIM의 DINT 기본값 -1은 고정 폭을 쓰지 않는 표지다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-170 | 숫자 TRIAD 선택 | swanuse PDF 139쪽 / 인쇄 131쪽 `[itriad]` | `src/swanpre1.ftn:3400` `CALL ININTG ('ITRIAD', ITRIAD, 'STA', 5)`; `src/swanpre1.ftn:3417` `!            original LTA (before version 41.01)`; `src/swanpre1.ftn:3418` `CALL INREAL ('TRFAC', PTRIAD(1), 'STA', 0.05)`; `src/swanpre1.ftn:3419` `CALL INREAL ('CUTFR', PTRIAD(2), 'STA', 2.5)`; `src/swanpre1.ftn:3420` `PTRIAD(8) = 0.` | C 문서 누락 | 숫자 TRIAD 선택의 후속 인수는 방법별로 다르다. 11은 옛 LTA다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-171 | SCAT GRID KXY | swanuse PDF 140쪽 / 인쇄 132쪽 `Kxy [kxlow] [kylow] [kxlen] [kylen] [mkxc] [mkyc]` | `src/swanpre1.ftn:3599` `CALL ININTG ('MKXC' , mkxc    , 'STA', -1)`; `src/swanpre1.ftn:3600` `CALL ININTG ('MKYC' , mkyc    , 'STA', -1)`; `src/SwanQCM.ftn90:354` `kxmin = pscat(3)`; `src/SwanQCM.ftn90:355` `kymin = pscat(4)`; `src/SwanQCM.ftn90:356` `kxlen = pscat(5)`; `src/SwanQCM.ftn90:357` `kylen = pscat(6)` | C 문서 누락 | KXY는 파수 영역을 직접 지정한다. 격자 개수의 -1은 자동 설정 표지다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-172 | FIG MINFR/SHAPE | swanuse PDF 140쪽 / 인쇄 132쪽 `[minfr] [shape]` | `src/swanpre1.ftn:1133` `CALL INREAL ('MINFR' , MFR , 'STA', 0.015)`; `src/swanpre1.ftn:1134` `CALL INREAL ('SHAPE' , SHP , 'STA', 1.5)`; `src/swanmain.ftn:3960` `FIGF = MIN( 1., 2.*PI * MFR / SPCSIG(JJ) )**SHP` | C 문서 누락 | FIG의 스펙트럼 모양은 기본 MINFR=0.015 Hz와 SHAPE=1.5로 정한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-175 | KN=0의 대체 | — | `src/swancom2.ftn:355` `IF (.NOT. AKN.NE.0.) AKN = 0.001` | C 문서 누락 | 입력 거칠기 0은 0.001 m로 바뀐다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-189 | 사파 OFF와 LIMITER | — | `src/swanmain.ftn:6652` `IF (IQUAD.EQ.0 .AND. PNUMS(20).LT.100.) THEN`; `src/swanmain.ftn:6655` `PNUMS(20) = 1.E+20` | C 문서 누락 | 사파를 끄면 조건에 따라 작용 밀도 제한 계수를 1E20으로 바꾼다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-190 | Bragg 입력 수심 격자 | — | `src/swanmain.ftn:6638` `IF ( IBRAG.NE.0 ) THEN`; `src/swanmain.ftn:6639` `IF ( IGTYPE(1).NE.1 ) THEN`; `src/swanmain.ftn:6640` `CALL MSGERR (2,'A regular bottom grid is required')`; `src/swanmain.ftn:6643` `IF (PBRAG(1).GT.0.5*MAX(MXG(1),MYG(1))) THEN` | C 문서 누락 | Bragg는 정규 입력 수심 격자와 영역 크기 검사를 수행한다. FILE 선택도 이 검사에 들어간다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-191 | 풍입력·백파 조합 검사 | — | `src/swanmain.ftn:6426` `IF  ( IWCAP.EQ.7 .AND. IWIND.NE.5 ) THEN`; `src/swanmain.ftn:6427` `CALL MSGERR(1,'Activate wind option Yan (1987) in case of')`; `src/swanmain.ftn:6431` `IF  ( IWCAP.EQ.8 .AND. IWIND.NE.8 ) THEN`; `src/swanmain.ftn:6435` `IF  ( IWIND.EQ.8 .AND. IWCAP.NE.8 ) THEN`; `src/swanmain.ftn:6442` `IF  ( IWIND .EQ. 4 .AND. IWCAP .NE. 2) THEN`; `src/swanmain.ftn:6432` `CALL MSGERR(1,'Babanin dissipation with non-Babanin input')` | C 문서 누락 | 조합 검사는 수준 1 경고다. 해당 검사 자체가 두 선택을 자동으로 맞추지는 않는다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-177 | 기본 수심 쇄파 | `manual-notes/swan-command-physics-reference.md:28` `breaking 은 **별도 활성**` | `src/swanmain.ftn:1113` `ISURF  = 1` | B 문서 오기 | 수심 쇄파는 기본 활성이다. 삼파·바닥 마찰의 기본 비활성과 구분한다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R5:PN-178 | BRAGG CON | `manual-notes/swan-command-physics-reference.md:118` `` `BRAGG` (CON/FILE) `` | `src/swanpre1.ftn:3495` `CALL INKEYW ('STA', 'FT')` | B 문서 오기 | BRAGG의 선택 이름을 FT/FILE로 고친다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
