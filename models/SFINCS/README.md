# SFINCS — Super-Fast INundation of CoastS

> Deltares 의 **오픈소스 reduced-complexity 복합침수(compound flooding) 모델**. 연안(조석·해일·파)·강우(pluvial)·하천(fluvial) 침수를 **고속·동적**으로 모의 — early warning·대규모 risk·ensemble 용. full-physics(ADCIRC/Delft3D) 대비 계산비용 대폭 절감하며 reasonable 정확도.

## 정체

- **개발**: Deltares (네덜란드). reduced-complexity engine (Leijnse et al. 2021 *Coastal Engineering*).
- **목적**: compound flooding(연안+강우+하천 동시) 고속 모의. 단순화 SWE(국소관성 LIE 류) + subgrid + quadtree 적응격자로 가속.
- **라이선스**: 소스 = **GNU GPL-3.0** (`raw/source_code/sfincs/LICENSE`). Windows/Docker 사전컴파일 실행파일 = Deltares Freeware (비상업 무료, 재배포·수정 불가).
- **공식**:
  - 사이트: <https://www.deltares.nl/en/software/sfincs/>
  - 문서: <https://sfincs.readthedocs.io/en/latest/> (user manual)
  - 소스: <https://github.com/Deltares/SFINCS> (GPL-3.0)
  - 실행파일: <https://download.deltares.nl/sfincs> · Docker `deltares/sfincs-cpu`
  - Python 빌더: HydroMT-SFINCS (<https://github.com/Deltares/hydromt_sfincs>)

## 현재 상태 (2026-06-18 신규 생성 → 소스 전수 검수)

- ✅ 공식 GitHub clone (`raw/source_code/sfincs/`, depth-1, 182 f90, GPL-3.0)
- ✅ **source-analysis 8** (전 코어 모듈, file:line + 적대 검증): architecture-source-map + **flow_solver**(reduced SWE momentum/continuity, Bates friction·CFL) + **subgrid_quadtree**(고속화) + **nonhydrostatic_wavemaker** + **boundaries_forcing**(spiderweb 태풍) + **snapwave**(연안 파·IG·Baldock) + **structures_physics** + **io_data**(BMI)
- ✅ **manual-notes 5** (readthedocs RST + **v2.4.0 Galibier 릴리스**): [numerical-implementation](manual-notes/sfincs-numerical-implementation.md)(overview·LIE/SSWE·Bates2010·subgrid·stability) + [parameters-io-reference](manual-notes/sfincs-parameters-io-reference.md)(sfincs.inp·입력·forcing·구조물·output) + [model-building-running](manual-notes/sfincs-model-building-running.md)(HydroMT v2 component API·DDB·실행파일·Docker/Singularity 실행) + **[v2.4.0-galibier-validation-testbed](manual-notes/sfincs-v2.4.0-galibier-validation-testbed.md)**(77 케이스 검증 카탈로그·regression/skillbed) + **[v2.4.0-galibier-changelog-known-issues](manual-notes/sfincs-v2.4.0-galibier-changelog-known-issues.md)**(릴리스 델타·버전 provenance)
  - ℹ️ readthedocs `docs/*.rst` 중 **사용자 대상 실질 내용 RST 전부 커버** — 미추출은 `singularity.rst`(Deltares 사내 빌드 문서)·`numerical_implementation.rst`·`validation.rst`(heading-only WIP skeleton)뿐
  - ⚠️ v2.4.0 Galibier(2026.01) 릴리스 = **바이너리(exe)+PDF만, 소스 미동봉** — 소스는 GitHub 태그 `v2.4.0_Galibier_release`(GPL-3.0). 위키 raw clone = main HEAD 2026-06-18(태그 미기록)
- ✅ **web-refs 1** ([official-resources](web-refs/sfincs-official-resources.md))

## 소스 구조 (`raw/source_code/sfincs/source/`)

| 경로 | 내용 |
|---|---|
| `src/*.f90` | **코어 36 모듈** (C-tier) — main·momentum·continuity·subgrid·quadtree·boundaries·meteo·snapwave 등 |
| `src/snapwave/` | **SnapWave** 파솔버(연안 wave, infragravity) 9 모듈 |
| `third_party_open/netcdf` | netCDF-fortran (⬛ T-tier 외부) |
| `sfincs_lib`/`sfincs_dll`/`sfincs` | 빌드 타깃(lib·DLL·exe), BMI 인터페이스 |
| `docs/` | readthedocs 소스 |

## 본 위키 연계

- 개념(도메인 집): **[`concepts/compound-flooding`](../../concepts/compound-flooding/)** — SFINCS 가 정의적으로 속하는 복합침수 토픽([06-model-application](../../concepts/compound-flooding/06-model-application.md) 모델 스펙트럼 hub). + [`concepts/storm-surge`](../../concepts/storm-surge/)(해일)·[`concepts/waves`](../../concepts/waves/)(SnapWave)
- 모델 비교: full-physics [`ADCIRC`](../ADCIRC/)·[`Delft3D`](../Delft3D/) 대비 reduced-complexity 고속 대안. ML emulator([`concepts/storm-surge/07-ml-emulators`](../../concepts/storm-surge/07-ml-emulators.md))와 함께 "고속 침수" 계열.
- 자매 모델: [`LISFLOOD-FP`](../LISFLOOD-FP/)(Bristol/Sheffield reduced-complexity flood) — 동류 reduced-complexity inundation.
