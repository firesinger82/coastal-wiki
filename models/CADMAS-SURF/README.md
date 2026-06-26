# models/CADMAS-SURF

> **Canonical source**: 이 디렉토리(`models/CADMAS-SURF/`)가 CADMAS-SURF 계열의 구현·메커닉에 대한 진실의 원천. `concepts/<topic>/06-model-application.md` 등은 여기로의 링크만 가짐.
>
> 🆕 **현재 상태(2026-06-23 신설+전수검수)**: CDIT/PARI 공식 GitHub org [`CADMAS-SURF`](https://github.com/CADMAS-SURF) 의 [`Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami`](https://github.com/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami) repo clone(`raw/source_code/`, git HEAD `da7668f` 2024-08-30, **~1255 Fortran 파일** + **영·일 매뉴얼 PDF 19** + 튜토리얼). **4개 시뮬레이터 전부 C티어 검수 완료 — source-analysis 12 + manual-notes 1**: SURF/3D(단상, 6노트)·CADMAS-2F(2상+FSI, 2)·STR3D(FEM 구조·지반, 3)·AGENT(피난, 1, 전수). 전부 file:line/page 인용, 영문 매뉴얼 지배방정식 ↔ 소스 cross-confirm. VOF 기반 위상해상 RANS 수치파동수조 — SWASH·FUNWAVE(위상해상)보다 한 단계 위인 **자유수면 추적 Navier-Stokes(VOF)** class. **100% 전수 검수 완료 — 코드(SA 16) + 매뉴얼(26 PDF, manual-notes 5)**. Okada 단층 쓰나미소스·HiDEM(DEM) 결합·STR3D geo/ 병렬쌍둥이 적발 + 영문 기술매뉴얼 4종 소스 cross-confirm(MUMPS 플래그 stale·Tobler 식 소스전용 등 적발). 잔여(후속, 케이스/번역 필요): 바이너리 3툴 내부·일문 상세·튜토리얼 절차(전부 source-needed/how-to).

## 정체 카드

- **이름**: **CADMAS-SURF** — VOF 기반 수치파동수조(numerical wave flume/channel). 정전 참조: **CDIT (2001) "수치파동수조의 연구·개발"(Research and development of numerical wave channel), CDIT Library** (영문 매뉴얼 참고문헌 ①, [`CADMAS-SURF3D_Manural_English.pdf`](raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Manual/CADMAS-SURF3D_Manural_English.pdf) 인용)
  - ⚠️ 약어 전개("Computer Aided Design of MAritime Structure" / "Super Roller Flume …")는 2차 웹 출처(scientific.net AMR.588-589.1376, ICCE proceedings) 기반 — 본 repo 매뉴얼 1차 확인 전이므로 `source-needed`.
- **정의**: 자유수면을 **VOF(Volume of Fluid)법**으로 추적하는 **비압축 단상(single-phase) Navier-Stokes 솔버** — 파·해양구조물 상호작용(波力·월파·쇄파). repo README 직접 인용: *"the single-phase Navier-Stokes equation (CADMAS-SURF/3D), which calculates the sea surface using the VOF method"* ([README.md](raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/README.md) L3)
- **저자/관리주체**: **CDIT**(Coastal Development Institute of Technology, 沿岸技術研究センター) + **PARI**(Port and Airport Research Institute, 港湾空港技術研究所). 공식 org [github.com/CADMAS-SURF](https://github.com/CADMAS-SURF) (연락 `cadmas.surf3d@gmail.com`). 결합 하이드로 모델 STOC-ML/STOC-IC 는 **PARI 개발·배포** (README L10-12 인용).
- **라이선스**: ⚠️ **repo에 LICENSE/COPYING 파일 부재**(clone HEAD `da7668f` 확인). README는 *"How to Cite"* 만 명시(인용 의무, [wiki/How-to-cite](https://github.com/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/wiki/How-to-cite)). → 재배포·수정 권리 명시 없음, **`source-needed`**(원저작권 CDIT/PARI).
- **공식 사이트**: CDIT [www.cdit.or.jp](https://www.cdit.or.jp/english/about/index4.html) · PARI [www.pari.go.jp/en](https://www.pari.go.jp/en/) · STOC 배포 [pari.go.jp/unit/tsunamitakashio/open-software/t-stoc](https://www.pari.go.jp/unit/tsunamitakashio/open-software/t-stoc/download/index.html)
- **소스 위치 (본 위키)**: ✅ `raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/` (gitignore 로컬, GitHub clone — Fortran 96.7%·C 1.8%·Makefile 1.5%)
- **사용 도메인**: 연안구조물 **내파(耐波) 설계** — 방파제·호안 작용 파력, 월파량, 쇄파 변형, 처오름. tsunami source→propagation→runup→구조물 변형 전단계 통합(멀티스케일·멀티피직스).
- **격자·수치**: 직교 staggered 격자 + **VOF 자유수면** + porous body(투과 소파구조) + **k-ε 난류** + 조파 source·무반사 경계. 3D판 = **CADMAS-SURF/3D-MG**: Fortran 90(동적배열·6자 초과 명칭) 위에 **MPI SPMD 영역분할 병렬**(영문 매뉴얼 Ch1 Overview 인용). 단일프로세서 시 standalone 거동.

## 모델 분류 — 위상해상 VOF RANS (수치파동수조)

- 본 위키 위상해상 모델군 **SWASH(비정수압 천수)·FUNWAVE/Celeris(Boussinesq)** 보다 한 단계 위 충실도 — **자유수면을 VOF로 직접 추적하는 RANS**. 분산·천수뿐 아니라 **쇄파 비선형·구조물 충격압·기액 2상**까지 해상. 대가는 비용(3D RANS).
- **단상↔2상 계층**: `CADMAS-SURF/3D`(단상) → `CADMAS-2F`(=`CADMAS-SURF/3D2F`, 기액 2상 VOF, 기상 효과 고려). 슬래밍/충격파압·공기연행에 2상 필요.
- **멀티스케일 결합**(repo의 본질): `STOC-ML/IC`(정수압/비정수압 광역 tsunami 전파, PARI) → `CADMAS-SURF/3D`(국소 자유수면) → `CADMAS-2F`(2상) → `STR3D`(FEM 구조·지반) → `AGENT`(피난). 광역→국소→구조→피난 일관 사슬.

## 구성요소 (repo Simulators/)

| 컴포넌트 | 역할 | 위치 |
|---|---|---|
| **CADMAS-SURF/3D** | 3D 비압축 단상 VOF NS | `Simulators/CADMAS-SURF-3D/` (240 Fortran) — ✅ C티어 검수 (SA 6) |
| **CADMAS-SURF/3D2F** (CADMAS-2F) | 3D 기액 2상 VOF + FSI | `Simulators/CADMAS-SURF-3D2F/` (388) — ✅ C티어 검수 (SA 2: 압축성 2상·구조결합) |
| **STR3D** | FEM 구조·지반 계산 | `Simulators/STR3D/` (587) — ✅ C티어 검수 (SA 3: FEM·solver·접촉/결합) |
| **AGENT** | 피난 시뮬레이터 | `Simulators/AGENT/` (40) — ✅ 전수 검수 (SA 1) |
| **STOC-ML / STOC-IC** | 정수압/비정수압 광역 tsunami (PARI 별도 배포) | (외부, pari.go.jp) |
| Pre/Post | CADMAS-MESH(-MULTI)·CADMAS-VR·ViewKai | `Pre and post-processors/` |

## 하위 디렉토리 현황

| 경로 | 상태 | 비고 |
|---|---|---|
| `source-analysis/` | ✅ 16 verified (코드 100% 포섭) | **SURF/3D(6)**: [architecture-source-map](source-analysis/cadmas-surf3d-architecture-source-map.md)(SMAC+VOF 루프·명명·데이터모델) · [smac-velocity-pressure-solver](source-analysis/cadmas-surf3d-smac-velocity-pressure-solver.md)(예측자·Poisson·MILU-BiCGSTAB) · [vof-free-surface](source-analysis/cadmas-surf3d-vof-free-surface.md)(donor-acceptor·NF 머신) · [turbulence-and-porous-resistance](source-analysis/cadmas-surf3d-turbulence-and-porous-resistance.md)(k-ε·Morison drag·파력) · [wave-generation-and-boundaries](source-analysis/cadmas-surf3d-wave-generation-and-boundaries.md)(조파·Sommerfeld·대수칙) · [timestep-nesting-stoc-coupling](source-analysis/cadmas-surf3d-timestep-nesting-stoc-coupling.md)(CFL·親子 nesting·STOC). **2F(2)**: [cadmas-2f-twophase-compressible-gas](source-analysis/cadmas-2f-twophase-compressible-gas.md)(압축성 기상 EOS·변밀도·준압축성 Poisson) · [cadmas-2f-structure-coupling-cutcell](source-analysis/cadmas-2f-structure-coupling-cutcell.md)(sf_* FSI cut-cell 공극). **STR3D(3)**: [str3d-fem-core-newmark-elasto-plastic](source-analysis/str3d-fem-core-newmark-elasto-plastic.md)(Newmark-β·요소·탄소성+균열·Biot) · [str3d-linear-solvers](source-analysis/str3d-linear-solvers.md)(ICCG/BiCGStab·PARDISO/MUMPS) · [str3d-contact-and-fluid-coupling](source-analysis/str3d-contact-and-fluid-coupling.md)(MPC 접촉·Coulomb·MPMD 결합). **AGENT(1)**: [cadmas-agent-evacuation-simulator](source-analysis/cadmas-agent-evacuation-simulator.md)(potential-field 피난·Tobler·익사판정). **S티어/커버리지(4)**: [cadmas-surf3d-stier-and-auxiliary-physics](source-analysis/cadmas-surf3d-stier-and-auxiliary-physics.md)(입출력·MPI·BC + ★Okada 단층소스·스칼라/온도수송·파이론 구현) · [str3d-stier-parallel-mesh-io](source-analysis/str3d-stier-parallel-mesh-io.md)(MPI·METIS·FEMAP + geo/ FEM 병렬쌍둥이) · [cadmas-2f-stier-and-hidem-dem-coupling](source-analysis/cadmas-2f-stier-and-hidem-dem-coupling.md)(sf_* 지원 + ★HiDEM DEM 결합) · [cadmas-pre-post-processors](source-analysis/cadmas-pre-post-processors.md)(ViewKai 소스 + MESH/VR 바이너리) |
| `manual-notes/` | ✅ 5 verified (26 PDF 전수) | [surf3d-governing-equations](manual-notes/cadmas-surf3d-english-manual-governing-equations.md)(Table 0-1-1+§2 지배식) · [2f-compressibility](manual-notes/cadmas-2f-manual-compressibility.md)(기상 압축성, EOS/Poisson cross-confirm) · [str-fem-theory-input](manual-notes/cadmas-str-manual-fem-theory-input.md)(Biot·Newmark·von Mises/DP·MPC·NASTRAN, MUMPS 플래그 stale 적발) · [agent-manual](manual-notes/cadmas-agent-manual.md)(피난, Tobler 식 소스전용 적발) · [manuals-catalogue](manual-notes/cadmas-manuals-catalogue.md)(튜토리얼·일문중복·STOC-CADMAS·Pre/post) |
| `web-refs/` | (미생성) | CDIT/PARI 공식 + 응용논문(tsunami 방파제·월파·detached breakwater) |
| `raw/source_code/...` | ✅ clone (gitignore) | git HEAD `da7668f` 2024-08-30, 1263 Fortran |

## 다음 후보 (잔여)

- **S티어**: SURF/3D IO·parser(`vf_o*`·`vf_i*`)·MPI 래퍼(`vf_zxmp*`) / STR3D 병렬통신(mpi_comm·glb_comm·util) / 2F·STR3D MPI 디테일
- **manual-notes 18종**: 일문 SURF/3D·STOC-CADMAS·CADMAS-2F·STR3D(CADMAS-STR)·AGENT 매뉴얼 + 영문 튜토리얼
- **Pre/post 4툴**: CADMAS-MESH(-MULTI)·CADMAS-VR·ViewKai
- 약어 전개·라이선스 1차 확인(매뉴얼 표지·CDIT Library 서지)
- `concepts/` cross-link: wave-force·overtopping·breaking·tsunami 토픽에서 위상해상 VOF 옵션으로 링크
