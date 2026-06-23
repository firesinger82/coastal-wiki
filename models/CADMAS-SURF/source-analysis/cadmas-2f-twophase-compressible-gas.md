---
title: "CADMAS-2F 기액 2상 — 압축성 기상 EOS·변밀도 one-fluid VOF·준압축성 압력-Poisson (vf_a1main·v1eos·user_eos·vpdrdt·cset2f)"
model: CADMAS-SURF
component: src (CADMAS-SURF/3D2F two-phase gas-liquid)
canonical_source: self
verification_method: "CADMAS-SURF/3D2F 소스 직접 read (raw/.../CADMAS-SURF-3D2F/Source code/). 메인헤더 '기액2상' vf_a1main.f:1-9 + 신규배열 RHOG/DRHODP/DRHODT/RHOGO(:69-76·364-367) + Picard 밀도-압력 루프(:1347-1388) + EOS user_eos.f:23-34(등온이상기체 ρ=(p+P0)/RT)·vf_v1eos.f:7·63-78·170-172 + 변밀도 1/ρ=1/(F·RHO0(1)+(1-F)·RHOG) vf_vpcoef.f:169-171·vf_vgene.f:101-103·vf_vmodif.f:106-108 + 준압축성 vf_vpdrdt.f:78-156(div v=-(1-F)Dρ/Dt/ρ) + 경계정합 vf_cset2f.f:5 + 제어 VF_ACOMPI.h:33-40·vf_iiopt.f:81-101. file:line 직접 인용. 단상 SURF/3D 대비 신규분만."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-23
related:
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-smac-velocity-pressure-solver.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-vof-free-surface.md
  - models/CADMAS-SURF/source-analysis/cadmas-2f-structure-coupling-cutcell.md
  - models/CADMAS-SURF/README.md
---

# CADMAS-2F 기액 2상 (압축성 기상)

> `CADMAS-SURF/3D2F`(=CADMAS-2F)는 단상 [SURF/3D](cadmas-surf3d-architecture-source-map.md)의 `vf_*` 인프라(SMAC·donor-acceptor VOF·k-ε 공유)에 **압축성 기상(gas phase)**을 추가한 버전. 본 노트는 **단상 대비 신규분만** 기록. 경로 루트: `raw/.../Simulators/CADMAS-SURF-3D2F/Source code/`.
>
> ⚠️ **명칭 주의**: "2F"=기액 2-Fluid(2상). `sf_*` 패밀리는 2상이 아니라 **유체-구조 결합**(cut-cell 공극) → [cadmas-2f-structure-coupling-cutcell](cadmas-2f-structure-coupling-cutcell.md). 표면장력·상변화(질량이동)·PLIC **없음** — 두 상은 공유 압력 + VOF 혼합 변밀도로만 상호작용.

## 1. 메인 정체 (vf_a1main.f:1-9)

```
CDT   VF_A1MAIN:CADMAS-SURF/3D-2Fのメインルーチン
CD      (1)解析対象:自由表面を含む気液2相3次元非圧縮性流体
```
해석대상 = **자유표면 포함 기액 2상 3D 비압축성 유체**, 방법 SMAC+VOF 동일. 신규 배열(`vf_a1main.f:69-76`, 할당 :364-367): `RHOG`(기상밀도)·`DRHODP`((dρ/dp)/ρ [1/Pa])·`DRHODT`((dρ/dt)/ρ [1/s])·`RHOGO`(전시각 기상밀도).

## 2. 기상 상태방정식 EOS (신규)

`USER_EOS`(`user_eos.f:23-34`) — **등온 이상기체**:
```
RHOG   = (PP + P0)/(RCONS·TCONS)      ρ = (p+P0)/(R·T)
DRHODP = 1.0/(PP + P0)                (dρ/dp)/ρ
```
드라이버 `VF_V1EOS`(헤더 `状態方程式 rho=rho(p)` `vf_v1eos.f:7`) — `NF>0` 셀에 대류 물질도함수 `(1-F)(Dρ/Dt)/ρ` 채움(`:170-172`). `ISTATE=0`이면 비압축 기상(`RHOG=RHO0(2)`, `:63-67`).

## 3. 변밀도 one-fluid VOF (단일 운동량장)

별도 기상 운동량식 **없음** — 액상 상수밀도 `RHO0(1)`·기상 가변밀도 `RHOG`를 VOF F-가중 혼합한 **단일 운동량장**(변밀도). 단상 코드 옆에 주석으로 남아 diff 가시(`vf_vpcoef.f:168-171`):
```
!!  RI=1/(FX·RHO0(1)+(1-FX)·RHO0(2))           ← 단상(상수 기상)
    RHO02 = ...RHOG(I)+...RHOG(IM)... (면보간)
    RI=1/(FX·RHO0(1)+(1-FX)·RHO02)              ← 2상(가변 RHOG)
```
동일 패턴 `vf_vgene.f:100-103`·`vf_vmodif.f:105-108`. 역밀도 `RI=1/(F·ρ_liq+(1-F)·ρ_gas_face)`가 압력구배항을 곱함(예측자·보정자). 재료헤더 `RHO0(1)`=액상·`RHO0(2)`=기상·`ANU0(1/2)` 액/기 점성(`VF_APHYSR.h:26-27`, 파싱 `vf_iimate.f:38-58`).

## 4. 준압축성 압력-Poisson (핵심 신규)

기상 압축성을 **별도 압축성 solver 가 아니라 SMAC 압력-Poisson 변형**으로 처리(단일 압력장 유지). `VF_VPDRDT`(헤더 `…密度変化による項` `vf_vpdrdt.f:8`). 변형 연속식(in-code 유도 `:78-88`):
```
div v + (1-F)·(Dρ/Dt)/ρ = 0   ← (1-F)(Dρ/Dt)/ρ 를 Poisson에 가산
ρ^new = ρ^old + (dρ/dp)^old·Δp
```
Poisson 대각·RHS 증강(`vf_vpdrdt.f:110-156`):
```
AD += AVLT·DRHODP/DTNOW
AD -= AVLT·DRHODP·DRHODT
BB += AVL·DRHODT
```
→ 발산구속이 `∇·v = -(1-F)(Dρ/Dt)/ρ`로 대체, `∂ρ/∂p` Jacobian 을 행렬에 implicit 반영 = **low-Mach/준압축성** 기상. `ISTATE=0`이면 표준 비압축 Poisson 으로 환원(`:77`).

## 5. EOS↔압력 Picard 결합 루프 (신규)

ρ↔p 상호의존 → 메인 속도/압력 서브루프 안에 **내부 밀도수렴 반복** `DO LL=1,MAXITR`(`vf_a1main.f:1347-1388`): `VF_V1EOS`로 ρ 재계산 → under-relaxation `RHOG=SRELAX·RHOG+(1-SRELAX)·WK01` + `NF==8`(기체)셀 상대오차 `SERR` → `VF_V1CAL(...RHOG,RHOGO...)` → `IF(SERR≤SERROR) EXIT`. 단상에 없는 Picard 밀도-압력 결합.

## 6. 제어 파라미터 (신규 입력)

| 파라미터 | 의미 | 인용 |
|---|---|---|
| `ISTATE` | 기상압축 0=무시·1=등온 | `VF_ACOMPI.h:33-39`, 파싱 `vf_iiopt.f:81-87` |
| `MAXITR` | 밀도수렴 최대반복 | `VF_ACOMPI.h:40` |
| `SPARAM(1-3)` | p0·R·T | `VF_ACOMPR.h:39-47` |
| `SERROR`·`SRELAX` | 수렴오차·완화계수 | `VF_ACOMPR.h:39-47`, `vf_iiopt.f:81-101` |

## 7. 기액 경계정합 + 음향 CFL 무시

- `VF_CSET2F`(헤더 `気相と液相の境界条件の整合性を調整` `vf_cset2f.f:5`) — 기상↔액상 경계조건 정합.
- **음향 CFL 미추가**: `VF_CDTCAL`이 `RHOG`를 받지만 압축밀도 timestep 줄은 주석처리(`vf_cdtcal.f:81-82` `RHO2=F·RHO0(1)+(1-F)·RHO0(2)` 유지, `!! RHOG` 비활성) → Δt는 여전히 비압축 이류/확산 CFL, 압축성은 압력 solve 에 implicit.

> disclosed: 표면장력·상변화(증발/응축 질량이동) 모델 **부재**. 두 상은 공유 압력 + VOF 혼합 변밀도로만 결합. 슬래밍 충격압의 공기쿠션(압축 기포) 효과가 주 목적.
