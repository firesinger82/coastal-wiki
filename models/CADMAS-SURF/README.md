# models/CADMAS-SURF

> **Canonical source**: 이 디렉토리(`models/CADMAS-SURF/`)가 CADMAS-SURF 계열의 구현·메커닉에 대한 진실의 원천. `concepts/<topic>/06-model-application.md` 등은 여기로의 링크만 가짐.
>
> 🆕 **현재 상태(2026-06-23 신설+코어검수)**: CDIT/PARI 공식 GitHub org [`CADMAS-SURF`](https://github.com/CADMAS-SURF) 의 [`Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami`](https://github.com/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami) repo clone(`raw/source_code/`, git HEAD `da7668f` 2024-08-30, **1263 Fortran 파일** + **영·일 매뉴얼 PDF 19** + 튜토리얼). **CADMAS-SURF/3D 코어 검수 완료 — source-analysis 5 + manual-notes 1**(전부 file:line/page 인용, 영문 매뉴얼 지배방정식 ↔ 소스 cross-confirm). VOF 기반 위상해상 RANS 수치파동수조 — SWASH·FUNWAVE(위상해상)보다 한 단계 위인 **자유수면 추적 Navier-Stokes(VOF)** class.

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
| **CADMAS-SURF/3D** | 3D 비압축 단상 VOF NS | `Simulators/CADMAS-SURF-3D/` (Source code 240 Fortran) |
| **CADMAS-SURF/3D2F** (CADMAS-2F) | 3D 기액 2상 VOF | `Simulators/CADMAS-SURF-3D2F/` |
| **STR3D** | FEM 구조·지반 계산 | `Simulators/STR3D/` |
| **AGENT** | 피난 시뮬레이터 | `Simulators/AGENT/` |
| **STOC-ML / STOC-IC** | 정수압/비정수압 광역 tsunami (PARI 별도 배포) | (외부, pari.go.jp) |
| Pre/Post | CADMAS-MESH(-MULTI)·CADMAS-VR·ViewKai | `Pre and post-processors/` |

## 하위 디렉토리 현황

| 경로 | 상태 | 비고 |
|---|---|---|
| `source-analysis/` | ✅ 5 verified | [architecture-source-map](source-analysis/cadmas-surf3d-architecture-source-map.md)(SMAC+VOF 루프·명명·데이터모델) · [smac-velocity-pressure-solver](source-analysis/cadmas-surf3d-smac-velocity-pressure-solver.md)(예측자·Poisson·MILU-BiCGSTAB) · [vof-free-surface](source-analysis/cadmas-surf3d-vof-free-surface.md)(donor-acceptor·NF 머신) · [turbulence-and-porous-resistance](source-analysis/cadmas-surf3d-turbulence-and-porous-resistance.md)(k-ε·Morison drag·파력) · [wave-generation-and-boundaries](source-analysis/cadmas-surf3d-wave-generation-and-boundaries.md)(조파·Sommerfeld·대수칙) |
| `manual-notes/` | ✅ 1 verified | [english-manual-governing-equations](manual-notes/cadmas-surf3d-english-manual-governing-equations.md)(Table 0-1-1 + §2 지배방정식, 소스 cross-confirm). 잔여: 일문·CADMAS-2F·STR3D·AGENT 매뉴얼 |
| `web-refs/` | (미생성) | CDIT/PARI 공식 + 응용논문(tsunami 방파제·월파·detached breakwater) |
| `raw/source_code/...` | ✅ clone (gitignore) | git HEAD `da7668f` 2024-08-30, 1263 Fortran |

## 다음 후보

- **source-analysis 착수**: `CADMAS-SURF-3D/Source code/vf_a1main.f`(main driver) → VOF 이류(`vf_*` advection)·k-ε·포러스 body·조파 source/무반사 경계 서브루틴별 file:line
- **manual-notes**: 영문 매뉴얼 `CADMAS-SURF3D_Manural_English.pdf` Ch1 Overview·지배방정식·경계조건 page 인용 발췌
- **AUDIT-LEDGER 등록**: 신규 모델로 C/S/T 티어 인벤토리 추가
- 약어 전개·라이선스 1차 확인(매뉴얼 표지·CDIT Library 서지)
- `concepts/` cross-link: wave-force·overtopping·breaking·tsunami 토픽에서 위상해상 VOF 옵션으로 링크
