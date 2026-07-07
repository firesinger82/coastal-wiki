---
title: "CADMAS-SURF/3D 갇힌 공기압(entrapped air) source-analysis — vf_fpvcip/vf_fpvcpp (VOF 기포 라벨링 + 폴리트로픽 가스법칙)"
topic: cadmas-surf3d-entrapped-air-pressure
canonical_source: self
citation_status: verified
verification_method: "CADMAS-SURF/3D raw source 직접 read: Source code/vf_fpvcip.f(266)+vf_fpvcpp.f(217) — 폴리트로픽 가스법칙(vf_fpvcpp.f:191) file:line 직접 검증. 소스 OPTION PV=CONST(vf_iiopt.f:80-85). [[cadmas-surf3d-stier-and-auxiliary-physics]] §B-3 은 2절(헤더 라인만)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-07
verification_by: "Claude Opus 4.8 (1M context) — vf_fpvcpp.f:188-193 직접 read 검증"
verification_date: 2026-07-07
related:
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-stier-and-auxiliary-physics.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-vof-free-surface.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-smac-velocity-pressure-solver.md
---

# CADMAS-SURF/3D 갇힌 공기압 — `vf_fpvcip.f` + `vf_fpvcpp.f`

> 소스: `.../CADMAS-SURF-3D/Source code/vf_fpvcip.f`(266, 기포 라벨링) + `vf_fpvcpp.f`(217, pocket 압력). (raw 경로 `models/CADMAS-SURF/raw/source_code/.../Simulators/CADMAS-SURF-3D/Source code/`.)
> **정체**: VOF 자유수면 위 **폐쇄 공기영역(air pocket)의 압력** — 케이슨·파라펫 **충격파압의 "에어쿠션"** 물리. `OPTION PV=CONST`. [[cadmas-surf3d-stier-and-auxiliary-physics]] §B-3 이 헤더 2절만 → 가스법칙·flood-fill·venting 미커버.

## 0. 구조 (2 서브루틴)
| 서브루틴 | 라인 | 역할 |
|---|---|---|
| `VF_FPVCIP` | vf_fpvcip.f 전체 | 이산 air-pocket 라벨 `IPVC` 구성(connected-component) |
| `VF_FPVCPP` | vf_fpvcpp.f 전체 | pocket 당 압력 1개(가스법칙) |

상수 `PVCP0`(대기압)·`PVCGM`(γ) — `VF_APHYSR.h`, 기본 0/0(`vf_a2dflt.f:207-208`). `MAXPVC=500`(`VF_A0PRM.h:19`).

## 1. VF_FPVCIP — 기포 라벨링 (connected-component)
```fortran
IF( NF(I,J,K) > 0 ) IPVC=-1                    ! :42 gas/surface 셀 후보 seed
! 반복 DFS flood-fill(6-이웃, stack NLIM) → pocket id NPVCB   :62-103
! MAXPVC=500 overflow guard   :134
! MPI: rank별 global label offset(VF_P1SUMI)   :111-133
! cross-rank union-find min-label 병합(VF_P3SRI2 halo·VF_P1MINI)+compaction   :143-253 (ISWAP=0 까지)
```

## 2. VF_FPVCPP — pocket 압력 (폴리트로픽 가스법칙)
```fortran
! vent 판정: pocket 이 개방경계면(INDB(3,M)∈{4,5,7}) 접촉 → IPVCBC(L)=1   :74-103
! 체적발산 PVCDIV(L)=ΣDV/ΣV(gas cell)   :121-147
! 체적가중 현재압력 PAV=PVCPFS(L)/PVCVFS(L)   :189
! ★폴리트로픽 가스법칙(backward-Euler):
PVCPES(L) = (PAV+PVCP0)/(1.0D0 + PVCGM*DTNOW*PVCDIV(L)) - PVCP0     ! :191
!   = dP/dt = -γ(P+P0)·div 의 음해 → (P+P0)V^γ = const
! vent pocket → gauge 0   :183-184
! NF=8(full-gas) 셀에 write-back PP   :201-202
```
입력 `OPTION PV=CONST <P0> <γ>`, γ≥1 검사(`vf_iiopt.f:80-85`).

## 3. 주요 findings (code≠manual)
- **★키워드 misnomer**: 옵션명은 `PV=CONST`(Boyle 등온 `PV=const` 암시)이나 실제는 **폴리트로픽 `P·V^γ=const`**(사용자 지정 γ=`PVCGM`, γ≥1 강제 :85). "PV=const" 를 무비판 반복 금지.
- **★기본 OFF**: `PVCP0=0`·`PVCGM=0` 기본(`vf_a2dflt.f:207-208`), gate `IF(PVCP0≥ZERO=1e-20)`(`vf_f1cal.f:223`) — **기본 run 에서 에어쿠션 압력완화 비활성**. CADMAS 충격압 결과 인용 시 `PV=CONST` 활성 여부 확인 필요(중대 caveat).
- **완전폐쇄 pocket 만 압축성**: 조파/방사/자유경계 접촉 pocket 은 대기압으로 vent(:183-184).
- **평균 체적 = NF=8(gas-only) 셀 기준**(:128,147) — surface 셀 `(1-F)` 부분체적은 누적 후 폐기(:148). 매뉴얼의 제어체적 정의와 대조 확인.

## 4. Primary sources
- **CADMAS-SURF/3D 매뉴얼**(repo 내 `Manual/CADMAS-SURF3D_Manual_Japanese.pdf`·English) — "空気圧 / PV=CONST"(entrapped air) 절.
- **CDIT** *Research and Development of Numerical Wave Flume (CADMAS-SURF)*, 2001 — CADMAS 정본.
- ⚠ Sakakiyama-Kajima 1992(porous)는 **무관**(다공질 drag 노트 소관, 오인용 금지).

## 5. 관련
- [[cadmas-surf3d-stier-and-auxiliary-physics]] — §B-3(본 노트가 심화, 2절→cross-link 축약 권장)
- [[cadmas-surf3d-vof-free-surface]] — VOF NF flag(gas pocket 식별 기반)
- [[cadmas-surf3d-smac-velocity-pressure-solver]] — 압력-속도 결합(pocket PP write-back 소비)
