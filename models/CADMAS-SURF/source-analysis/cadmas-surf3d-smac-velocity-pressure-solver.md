---
title: "CADMAS-SURF/3D SMAC 流速-압력 결합 — 예측자·압력 Poisson·보정 + 포러스 운동량 (vf_v1cal·veuler·vpcoef·vpsol·m1bcgs·vmodif)"
model: CADMAS-SURF
component: src (SMAC flow solver + linear solver)
canonical_source: self
verification_method: "CADMAS-SURF/3D-MG 소스 직접 read (raw/.../CADMAS-SURF-3D/Source code/). vf_v1cal.f(드라이버) 호출순서 :155-289 + vf_veuler.f Euler 예측자 :122-125 + vf_vflxd[uvw].f DONOR 스킴 헤더·플럭스 :67-99 + vf_vpcoef.f Poisson 7대각 계수·발산RHS :152-348 + vf_vpsol.f solve 호출 :65-76 + vf_m1bcgs.f (M)ILU-BiCGSTAB 헤더 :9-10·반복 :178-227·수렴판정 :144·219 + vf_vmodif.f 속도·압력 보정 :72-206. 포러스 GLV/GGV 가중 운동량 결합 file:line 직접 인용."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-23
related:
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-turbulence-and-porous-resistance.md
---

# CADMAS-SURF/3D SMAC 流速-압력 결합

> CADMAS 의 압력-속도 결합 = **SMAC法**(Simplified Marker And Cell). 압력 자체가 아니라 **속도보정 포텐셜 함수 `PT`** 를 Poisson 방정식으로 풀고, 그 구배로 속도를 projection(보정)한 뒤 압력을 갱신. 드라이버 `VF_V1CAL`(메인루프 `vf_a1main.f:1058` 에서 `LOOPS`회 호출). 경로 루트 → [architecture-source-map](cadmas-surf3d-architecture-source-map.md).

## 1. SMAC 시퀀스 (vf_v1cal.f 드라이버)

헤더 `VF_V1CAL:流速・圧力を計算する`(`vf_v1cal.f:13`). 1스텝 순서:

| 단계 | 서브루틴 | 호출 위치 | 역할 |
|---|---|---|---|
| ① 운동량 플럭스(이류+점성) | `VF_VFLXDU/V/W` | `vf_v1cal.f:155·169·183` | x/y/z 운동량 대류·점성항 (DONOR 스킴) |
| ② 소스·소멸(drag 등) | `VF_VGENE` | `vf_v1cal.f:199-208` | 압력구배·포러스 drag → QU/QV/QW |
| ③ **예측자(가속도→仮流速)** | `VF_VEULER` | `vf_v1cal.f:218-228` | 명시적 Euler 잠정속도 |
| ④ **압력 Poisson 계수조립** | `VF_VPCOEF` | `vf_v1cal.f:261-269` | 7대각 행렬 + 발산 RHS |
| ⑤ **선형 solve** | `VF_VPSOL`→`VF_M1BCGS` | `vf_v1cal.f:278-281` | 포텐셜 `PT` (BiCGSTAB) |
| ⑥ **속도·압력 보정(projection)** | `VF_VMODIF` | `vf_v1cal.f:287-289` | `∇PT` 로 속도 보정, PP 갱신 |

## 2. 예측자 — 명시적 Euler 잠정속도 (vf_veuler.f)

헤더 `VF_VEULER:仮流速をEuler法で計算する`(`vf_veuler.f:9`). 갱신형:
```
vf_veuler.f:125 :  U = (GV*U_old + DTNOW*DU) / GV0
```
(v: `:179-182`, w: `:236-239`). `DU` = 운동량 플럭스 + 소스(QU)의 합. `GV`/`GV0` = 면중심 관성공극 `GLV`/`GLV0`(시간의존 공극) — **포러스 body 의 관성이 시간미분항에 가상질량으로 들어감**(`vf_veuler.f:120-125`).

## 3. 운동량 이류 스킴 — DONOR(1차 풍상) blended (vf_vflxd[uvw].f)

세 파일 모두 헤더에 `(DONORスキーム)` 명시 (`vf_vflxdu.f:8`·`vf_vflxdv.f:8`·`vf_vflxdw.f:8`). `VF_V1CAL` 은 DONOR 외 옵션을 에러 처리 — `'DONOR ONLY.'`(`vf_v1cal.f:160·174·188`). 즉 본 빌드의 운동량 이류는 **사실상 1차 풍상**.

blend 파라미터 `SCMVP`: 풍상가중 `SU=SCMVP`, 중심가중 `SC=1-SCMVP` (`vf_vflxdu.f:67-68`). 풍상 플럭스는 부호 셀렉터 `MAX(WIN,0)·U(I) - MAX(-WIN,0)·U(I+1)` (`vf_vflxdu.f:80-82`), 중심 플럭스 `FG=WIN*(U(I)+U(I+1))*0.5` (`vf_vflxdu.f:79`). `SCMVP=1` → 순수 donor-cell.

> 면속도 `WIN` 은 관성공극 가중: `WIN=(GLX(I)*U+GLX(I+1)*U)*0.5` (`vf_vflxdu.f:77-78`), 점성항은 면적투과율 가중 `(GGX(I)+GGX(I+1))*ANU` (`vf_vflxdu.f:85-86`).

## 4. 압력 Poisson — 포텐셜 함수 PT (vf_vpcoef.f)

헤더 `VF_VPCOEF:ポテンシャル関数の連立1次方程式を作成する` + `対角項を正にするため係数に-1.0を乗じる`(`vf_vpcoef.f:8-9`). **7대각** 행렬(AD 대각 + ALI/ALJ/ALK/AUI/AUJ/AUK 인접 6면):
- off-대각 계수 = 면적투과율 × 공극/관성: x면 `GV=...GGV(I)/GLV(I)+GGV(IM)/GLV(IM)...`, `AIM=AYZ*XX(5,I)*GGX(I,J,K)*GV` (`vf_vpcoef.f:152-155`; y `:226-228`; z `:301-303`)
- 대각 `AD=AKM+AJM+AIM+AIP+AJP+AKP` (`vf_vpcoef.f:342`)
- **발산 RHS** = 면적투과율 가중 속도발산: `VD=AYZ*(GGX(IP)*U(IP)-GGX(I)*U(I)) + AXZ*(GGY...) + AXY*(GGZ...)` (`vf_vpcoef.f:345-347`), 공극시간변화 소스 `VQ=-(GGV-GGV0)*DTI*AVL` (`vf_vpcoef.f:348`)

## 5. 선형 solver — (M)ILU-BiCGSTAB (vf_vpsol.f → vf_m1bcgs.f)

헤더 `VF_M1BCGS:(M)ILU-BiCGSTAB法により非対称連立1次方程式を解く / A*x=bを解く`(`vf_m1bcgs.f:9-10`).
- **Bi-CGSTAB 반복**: ALPHA(`:178`)·OMEGA(`:203`)·BETA(`:227`), 해갱신 `XW+ALPHA*PP+OMEGA*RR`(`:210`)
- **전처리**: ILU/MILU — 분해 `VF_MZDCMP`(`:101`), 적용 `VF_MZMINV`(`:111·136·173·197`). `ICGTYP=0`→ILU, `≠0`→MILU(`:56-58`), MILU 파라미터 `CGPARA`(`:43`). **좌전처리**(잔차norm은 `MINV*BB` 기준 `:114-115`)
- **수렴판정**: `XNORM ≤ BNORM*EPSR2 + EPSA2`(`:144·219`), 발산 `XNORM>DIV2`(`:220`). 임계값 `CGEPSA`(절대)·`CGEPSR`(상대)·`CGDIV`(발산)
- **caller 체크**(`vf_vpsol.f:71-76`): `ICGITR>ICGMAX`→NOT CONVERGED, `-2`→INSTABILITY, `-1`→CAN NOT DECOMPOSITION

## 6. 속도·압력 보정 = projection (vf_vmodif.f)

헤더 `VF_VMODIF:流速・圧力を補正する`(`vf_vmodif.f:7`).
- 속도 projection(공극/관성 가중 구배): `GV=...GGV(I)/GLV(I)+GGV(I-1)/GLV(I-1)...`, `U=U+XX(5,I)*GV*(PT(I)-PT(I-1))` (`vf_vmodif.f:72-74`; v `:125-127`; w `:178-180`)
- **압력 갱신**(SMAC): `PP = PP - (RHO0/DTNOW)*PT` (`vf_vmodif.f:201·206`) — 푼 미지수는 속도보정 포텐셜 `PT`, 압력은 여기서만 갱신

## 7. 포러스 body 가 운동량에 들어가는 방식 (요약)

`GGV`=공극률, `GGX/Y/Z`=면적투과율, `GLV=GGV+(1-GGV)*CM`=관성(가상질량) 공극. ① 이류 면속도(GLX/Y/Z)·점성(GGX/Y/Z) 가중 ②예측자 시간미분항 `/GLV` ③Poisson off-대각 `GGx·GGV/GLV` ④발산 RHS 면적투과율 ⑤보정 구배 `GGV/GLV`. **저항(drag) 力 자체**(½C_D(1-γ)u|u|)는 `vf_vgene.f` 에서 소스로 → [turbulence-and-porous-resistance §B](cadmas-surf3d-turbulence-and-porous-resistance.md).
