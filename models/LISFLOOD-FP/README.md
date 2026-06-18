# LISFLOOD-FP — 2D 수리 침수 모델 (v8.2)

> 복잡 지형 위 **범람(floodplain inundation)을 계산효율적으로** 모의하는 2D 수리(hydrodynamic) 모델. 원개발 University of Bristol(Bates 그룹), v8.x 는 **SEAMLESS-WAVE 프로젝트**(Georges Kesserwani, University of Sheffield) 주도. **다중 솔버**(reduced-physics ACC ~ 완전 2D shallow-water FV1/DG2) + **GPU 가속** + **동적 해상도 적응(multiwavelet)**.

> ⚠ **이름 주의**: 본 모델은 **LISFLOOD-FP**(Bristol/Sheffield, hydraulic flood inundation). EC-JRC 의 **LISFLOOD**(distributed hydrological rainfall-runoff)와 **별개 모델**.

## 정체

- **개발**: University of Bristol 원조(Bates et al.) → v8.0+ SEAMLESS-WAVE(Kesserwani, U. Sheffield).
- **목적**: DEM 위 2D 범람 — 연안·하천·강우 침수. reduced-physics(고속) ↔ 완전 SWE(고정확) 솔버 선택.
- **버전**: **v8.2** (2024-07-29). **8.x 특징 = GPU multiwavelet DG2 + dynamic resolution adaptivity**(비균일격자 acc_nugrid).
- **라이선스**: **GNU GPL-2.0** (Zenodo 메타데이터; repo LICENSE 파일 본문 부재).
- **언어**: C++ + CUDA. CMake ≥3.13 빌드 (Windows MSVC/Intel · Linux). netCDF·libnuma 의존.
- **canonical 정본 소스**: **Zenodo doi:10.5281/zenodo.13121102** (v8.2 아카이브). 공식 GitHub 단일 repo 미확인 → Zenodo 정본.

## 현재 상태 (2026-06-18 신규 생성)

- ✅ Zenodo v8.2 아카이브 다운로드·압축해제 (`raw/source_code/LISFLOOD-FP/`, raw gitignored)
- ✅ **source-analysis 7** (전 솔버군, file:line + 적대 검증): architecture-source-map + **classic-acc-flow**(ACC local-inertia Bates2010·diffusive·Trent) + **channel-sgc**(sub-grid channel·관성식·weir/bridge orifice) + **swe-fv1-dg2**(FV1 Godunov·DG2 multiwavelet·HLL Riemann·SSP-RK2) + **cuda-gpu**(FlowVector·ghostraster) + **io-boundary** + **lisflood2-driver**(sgm_fast 관성파·CFL)
- ✅ **web-refs 1** ([official-resources](web-refs/lisflood-fp-official-resources.md))
- ⬜ manual-notes (Bristol/SEAMLESS-WAVE docs·INSTALL.md — 후속)

## 소스 구조 (`raw/source_code/LISFLOOD-FP/`)

| 경로 | 내용 |
|---|---|
| `*.cpp` (root) | **classic FP 솔버**: lisflood.cpp(main)·fp_acc(ACC local-inertia)·fp_flow(diffusive)·fp_trent·sgc(sub-grid channel)·por_flow(porosity)·weir/ch_flow·boundary·input·output |
| `swe/` | **신규 SWE 솔버**: fv1(FV1 Godunov 1차)·dg2/dg2new(**DG2 multiwavelet** 2차)·hll(HLL Riemann flux)·flux·fields·boundary·input/output |
| `cuda/` | **GPU(CUDA)** 버전: acc·fv1·dg2·acc_nugrid(동적 해상도) |
| `lisflood2/` | 신규 driver 계층 | 
| `rain`·`preprocess`·`postprocess` | 강우·전후처리 |
| `test`·`testing` | 검증 케이스(대용량) |

## 본 위키 연계

- 자매 모델: [`SFINCS`](../SFINCS/)(Deltares reduced-complexity compound flooding) — 동류 고속 침수. LISFLOOD-FP 는 솔버 스펙트럼(ACC reduced ~ DG2 full SWE)이 더 넓음.
- 개념: [`concepts/storm-surge`](../../concepts/storm-surge/)(연안 침수)·향후 compound-flooding/inundation 토픽.
- full-physics [`ADCIRC`](../ADCIRC/)·[`Delft3D`](../Delft3D/) 대비 raster 기반 고속 범람. ACC(local inertia)=SFINCS reduced SWE 와 유사 계열.
