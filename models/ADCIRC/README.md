---
last_source_check: 2026-10-11 (recovery 재판독 대조)
---

# models/ADCIRC

> **Canonical source**: 이 디렉토리(`models/ADCIRC/`)가 ADCIRC 모델의 구현·메커닉에 대한 진실의 원천.

## 기능과 근거에서 찾기

[ADCIRC 기능 지도·근거 상태](source-analysis/adcirc-topic-map.md)에서 기능별 문서·식·코드 노트와 미확인 범위를 찾는다. 지도는 `source-needed`이며, [조석 입력 확인 방법](source-analysis/tide/adcirc-tide-harmonic-prep.md#input-quality-and-validation)은 입력 품질부터 실행·수치·물리 검증에 필요한 증거를 안내한다. 실제 자료 검사·모델 실행·물리 검증을 완료했다는 의미는 아니다.

## 정체 카드

- **이름**: ADCIRC (ADvanced CIRCulation Model)
- **저자/관리주체**: R. Luettich (UNC), J. Westerink (Notre Dame) 외. 1990년대 ~ 현재
- **라이선스**: 학술/연구 무료 사용, 상업 라이선스 별도 (adcirc.org/license)
- **공식 사이트**: [https://adcirc.org/](https://adcirc.org/) (raw/manuals/website 에 1086 HTML mirror)
- **GitHub**: [adcirc/adcirc](https://github.com/adcirc/adcirc), [adcirc/adcircpy](https://github.com/adcirc/adcircpy), [adcirc/adcirc-testsuite](https://github.com/adcirc/adcirc-testsuite)
- **소스 위치 (본 위키)**: `raw/source_code/adcirc/` (Fortran core) + `adcirc-testsuite` + `adcircpy` (Python) + `gahm` (vortex parametrization) + `asgs` (forecast system) + `StormEvents` + `FigureGen`
- **공식 메뉴얼**: `raw/manuals/pdfs/` 98 PDFs (workshops, papers, theory) + Luettich & Westerink (2004) "Formulation and Numerical Implementation of the 2D/3D ADCIRC" + 공식 wiki mirror
- **공식 문서사이트 미러**: https://adcirc.github.io/adcirc/ (Sphinx) → md 150편 + SITE-INDEX 색인 (2026-07-14 취득, rst→gfm 무손실 변환; 위키 밖 로컬 아카이브 — [manifest.md](manifest.md) docs-site 절 참조)
- **공식 교과서**: Pugh "Tides, Surges and Mean Sea-Level" (`source_id: sea-level`, [`textbook/md/sea-level.md`](../../textbook/md/sea-level.md)) — storm surge 이론 기반
- **사용 도메인**: 2D/3D barotropic ocean circulation — 조석·폭풍해일·연안 흐름
- **격자**: unstructured triangular finite element mesh (`fort.14`)
- **수치 기법**: Generalized Wave Continuity Equation (GWCE) — semi-implicit 3-time-level(A00/B00/C00 가중, consistent JCG / lumped 옵션) + 3D internal mode θ³-가중(Alp1/2/3) 복소 tridiagonal([[adcirc-3d-vssol-vertical-scheme]]), parallel (MPI)

GWCE의 A00·B00·C00 가중과 consistent JCG·lumped 선택은 v56.2.1 코드와 대응한다. (`[file=src/gwce.F line=516]` ` GA00DPAvgOAreaIE4 = ALPHAL(IE)*A00*G*DPAvg*Cfac/AreaIE4 `; `[file=src/gwce.F line=2000]` ` IF (ILump.eq.0) THEN ! default, fully consistent LHS `; `[file=src/gwce.F line=2003]` ` CALL JCG(NP,MNP,MNEI,NEITAB,COEF,GWCE_LV,ETAS, `; `[file=src/gwce.F line=2014]` ` RDIAG = 1.0d0 / COEFDTemp(I)   ! COEFD --> COEFDTemp  08-11-2022 SB `)

## 하위 디렉토리 현황

노트 수는 2026-09-14 집계다. 아래 종결·audit done과 raw 규모는 이전 기록이며, 현재 기능별 실행·수치/물리 검증 상태는 위 기능 지도의 범위 구분을 따른다.

| 경로 | 노트 수 | 상태 | 비고 |
|---|---:|---|---|
| `source-analysis/` | 38편: 37 verified + 기능 지도 1 source-needed (2026-09-14; 하위 디렉터리 포함) | **종결 2026-07-11** (AUDIT-LEDGER §5) | NWS modes·GAHM·mesh tools·source-code 분석. **VSSOL 연직스킴(adcirc-3d-vssol-vertical-scheme, 2026-07-11) 으로 마지막 코어 갭 해소**. (2026-06-18 정화: 개인 local-workflow/ 23 + forcing-input + storm-surge JMA-MSM/NWS13 운영 플레이북 3 제거; 로컬 provenance 중립화) |
| `manual-notes/` | **22** verified (이전 집계) | **M-B audit done 2026-05-24** (이전 기록) | 19-ice-coverage는 v49.64+ PDF와 v56.2.1 코드의 차이를 기록한다. (adcirc_modifications_for_ice.pdf, PDF 3쪽 / 인쇄 3쪽.) 현재 NCICE 허용값은 0·10·12·14·17이다. (`[file=src/read_input.F line=2316]` ` IF (NCICE.NE.0.AND.NCICE.NE.10.and.NCICE.NE.12.AND.NCICE.ne.14.AND.NCICE.ne.17) THEN `; `[file=src/read_input.F line=2317]` ` CALL terminate(exit_code=ADCIRC_EXIT_FAILURE, `) 현재 기본 얼음 항력은 Lupkes 분기를 사용한다. (`[file=src/wind.F line=132]` ` CHARACTER(len=10) :: DragLawString = 'default' ! controls wind drag formulation `; `[file=src/wind.F line=139]` ` CHARACTER(len=10) :: DragLawString = 'Powell' `; `[file=src/wind.F line=767]` ` CASE("Lupkes","default","Powell") `) IceCube 실행 식의 0% 값은 0.00075이다. (`[file=src/wind.F line=761]` ` pic = PercentIce*0.01d0 `; `[file=src/wind.F line=762]` ` IceDrag = (0.075d0 + 0.75d0*pic - 0.9d0*pic*pic `; `[file=src/wind.F line=763]` ` &              + 0.2d0*pic*pic*pic)*0.01d0 `) 해석: PDF의 0.000075는 자릿수 오류일 가능성이 있다. (adcirc_modifications_for_ice.pdf, PDF 3쪽 / 인쇄 3쪽: `When pic = 0 the drag coefficient is equal to the minimum value for Garratt (.000075)`; `[file=src/wind.F line=762]` ` IceDrag = (0.075d0 + 0.75d0*pic - 0.9d0*pic*pic `; `[file=src/wind.F line=763]` ` &              + 0.2d0*pic*pic*pic)*0.01d0 `) 노트 수와 과거 verified 집계는 이번 대조에서 확인하지 않음. |

| 항목 | 문서·코드 대조 | 출처와 원문 |
|---|---|---|
| ICE-10 기본 얼음 drag 공식 | 문서는 미지정 또는 default에서 IceCube를 사용한다고 적는다. 코드는 default에서 Lupkes 분기를 사용한다. 코드의 옛 주석 124–127은 실제 CASE와 다르다. | `[file=docs/technical_reference/input_files/fort25.rst line=7]` ` When using ice fields, the wind drag coefficient is first computed by the usual Garratt formula based on wind speed, then a wind drag coefficient is computed by a new function called IceCube that is based solely on the percent of ice coverage, then the maximum of the Garratt and IceCube drag coefficients is taken but must still be less than or equal to the drag cap in ADCIRC. If there is no ice in a particular area, then the drag coefficient is the same as Garratt. `<br>`[file=docs/technical_reference/input_files/fort25.rst line=43]` ` The IceCube formulation is used if the DragLawString is not specified in the fort.15, or is specified as “IceCube” or “default”. IceCube is a cubic function that represents a smoother transition between Garratt and the RaysIce formulation for low ice cover percentages and low wind speeds. This function is as follows:” `<br>`[file=docs/technical_reference/input_files/fort25.rst line=47]` ` \mathrm{CDF} = [0.075 + 0.75 \mathrm{IC} – 0.9 \mathrm{IC}^2 + 0.2 \mathrm{IC}^3 ] 10^{-2} \text{ (IceCube formulation, this is the default)} `<br>`[file=src/wind.F line=132]` ` CHARACTER(len=10) :: DragLawString = 'default' ! controls wind drag formulation `<br>`[file=src/wind.F line=736]` ` SELECT CASE(TRIM(DragLawString)) `<br>`[file=src/wind.F line=767]` ` CASE("Lupkes","default","Powell") `<br>`[file=src/wind.F line=776]` ` pic = min(PercentIce*0.01d0,1d0) `<br>`[file=src/wind.F line=777]` ` Cform = Cform_max*(1d0-pic)**beta `<br>`[file=src/wind.F line=778]` ` WindIceDrag = WindDrag*(1d0 - pic) + (Cskin + Cform)*pic ` |
| ICE-11 IceCube의 IC=0 수치·IC 정의 | 문서의 IC=0 수치는 .000075이다. 실제 식의 상수항은 0.075×0.01=.00075이다. 문서는 IC 범위를 0–1로 정의하고 다음 문장에서는 IC=50·100을 사용한다. 해석: 마지막 문장의 50·100은 percent에 해당한다. | `[file=docs/technical_reference/input_files/fort25.rst line=39]` ` in which IC is the ice concentration varying from 0.0 to 1.0 for open water and complete ice cover conditions, respectively. To specify this quadratic formulation for the wind drag, set the DragLawString parameter in the fort.15 file to “RaysIce”. `<br>`[file=docs/technical_reference/input_files/fort25.rst line=47]` ` \mathrm{CDF} = [0.075 + 0.75 \mathrm{IC} – 0.9 \mathrm{IC}^2 + 0.2 \mathrm{IC}^3 ] 10^{-2} \text{ (IceCube formulation, this is the default)} `<br>`[file=docs/technical_reference/input_files/fort25.rst line=49]` ` When IC = 0 the drag coefficient is equal to the minimum value for Garratt (.000075), when IC = 50 it has a value of 0.0025 and a zero gradient, and when IC = 100 it has a value of 0.00125. `<br>`[file=src/wind.F line=761]` ` pic = PercentIce*0.01d0 `<br>`[file=src/wind.F line=762]` ` IceDrag = (0.075d0 + 0.75d0*pic - 0.9d0*pic*pic `<br>`[file=src/wind.F line=763]` ` &              + 0.2d0*pic*pic*pic)*0.01d0 ` |

OWI ASCII는 percent를 입력한다. (`[file=docs/technical_reference/input_files/fort25.rst line=21]` ` If numIceFields in the fort.25 file is set to 1, only the fort.225 file will be read; if numIceFields in the fort.25 file is set to 2 then both the fort.225 and fort.227 files will be read. The fort.225 (the basin scale, i.e., large scale coarse grid) and optional fort.227 (the region scale, i.e., smaller scale finer grid) files contain the actual ice percentage values (0.0 to 100.0%) and a value of -1.0 which means land or no data available. A value of -1.0% is treated as 0.0% ice in ADCIRC. `) IceCube 식은 PercentIce를 0–1 비율로 바꾼다. (`[file=src/wind.F line=761]` ` pic = PercentIce*0.01d0 `) GRIB2의 면적 비율은 caller가 100배로 바꾼다. (`[file=src/wind.F line=1395]` ` IF (NCICE.eq.14) then `; `[file=src/wind.F line=1396]` ` Cicenow = 100d0*(CICE1(I) + `; `[file=src/wind.F line=1397]` ` &                          CTRATIO*(CICE2(I)-CICE1(I))) `) NCICE=17의 netCDF 면적 비율도 caller가 100배로 바꾼다. (`[file=src/wind.F line=1727]` ` Cicenow = 100d0*(CICE1(I) + CTRATIO*(CICE2(I)-CICE1(I)))   ! GML added 20210727 `)

| `web-refs/` | 2 verified | **신설 2026-05-24** | adcirc-official-resources.md + adcirc-foundational-papers.md — 공식 자원·기초 문헌 색인; 공식 사이트·GitHub repos (adcirc/adcirc·adcircpy·gahm·asgs·OceanMesh2D)·핵심 논문 (Luettich 1991-92·Westerink 1992·Dietrich 2010-11·Holland 1980) |
| `raw/` | 1090 .md + 98 pdf + 140 fortran (16.9 GB) | archive | source_code + manuals + website mirror |

## 본 위키에서의 핵심 활용

- [`concepts/storm-surge/02-theory.md`](../../concepts/storm-surge/02-theory.md) — Pugh §6-7 + ADCIRC GWCE 정형
- [`concepts/storm-surge/04-code-and-tools.md`](../../concepts/storm-surge/04-code-and-tools.md) — NWS modes (0/6/12/13/14/19/20/29/30) 운영 워크플로
- [`concepts/storm-surge/03-analysis-methods.md`](../../concepts/storm-surge/03-analysis-methods.md) — surge separation·return period (Pugh §6:1·§7:8·§8:3:2-3)
- [`concepts/tides/06-model-application.md`](../../concepts/tides/06-model-application.md) — 조석 forcing
- [[khoa-tide-surge-coupling]] (예정) — KHOA 실측 tide-surge separation 검증

## 작성 우선순위 (남은 작업)

1. ✅ **M-B**: `manual-notes/` audit 완료 2026-05-24 — 21 verified (external URL catalog)
2. ✅ **M-E**: `web-refs/` 신설 2026-05-24 — adcirc-official-resources.md
3. ✅ **정화 2026-06-18**: 개인 ADCIRC 운영자료(local-workflow/ 23 + forcing-input-foundation) canonical 제거. preprocessing/bathymetry/topic-map 는 공식문서 코어로 in-place 정화. 개인 사례(wide6 mesh evidence 등)는 바이블 검증 통과 시 experience/ 로.
4. Hinnamnor 2022 / Maemi 2003 case 추가 (storm-surge/05 + KHOA cross-ref)
