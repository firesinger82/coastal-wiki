---
title: "CADMAS-SURF/3D 난류·포러스 저항·파력 — k-ε(Launder-Spalding)·Morison drag/관성·파력적분 (vf_k1cal·cnut0·vgene·cglv·cforce)"
model: CADMAS-SURF
component: src (k-ε turbulence + porous resistance + wave force)
canonical_source: self
verification_method: "CADMAS-SURF/3D-MG 소스 직접 read (raw/.../CADMAS-SURF-3D/Source code/). k-ε: vf_k1cal.f 드라이버(:8·85-170) + vf_kgene.f 생성식(:160-181) + vf_cnut0.f νt=Cμk²/ε(:47) + 상수 vf_a2dflt.f:169-177(Cμ=0.09·σk=1.0·σε=1.3·C1=1.44·C2=1.92·κ=0.4·A=5.5) / 선언 VF_APHYSR.h:31-39. 포러스 drag: vf_vgene.f Morison ½CD(1-γ)u|u| (x:110·y:186·z:262) + Dupuit-Forchheimer 분기(:111-) + 관성 GLV=γ+(1-γ)CM vf_cglv.f:34·vf_cglxyz.f:67. 파력: vf_cforce.f -P·dS 면적분(:6·75-77·278). file:line 직접 인용."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-23
related:
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-smac-velocity-pressure-solver.md
---

# CADMAS-SURF/3D 난류·포러스 저항·파력

> 세 서브시스템: **(A) k-ε 2방정식 난류**(표준 Launder-Spalding), **(B) 포러스 body 저항**(Morison 2차 drag + 가상질량 관성 — 소파블록/투과방파제), **(C) 파력 적분**(구조물 표면압 -P·dS). 경로 루트 → [architecture-source-map](cadmas-surf3d-architecture-source-map.md).

## A. k-ε 2방정식 난류 모델

드라이버 `VF_K1CAL`(헤더 `k-ε2方程式モデルの計算` `vf_k1cal.f:8`, 메인루프 `vf_a1main.f:1095`):

| 단계 | 위치 |
|---|---|
| 이류 플럭스(k·ε, DONOR) | `vf_k1cal.f:102-110` (`VF_SCONVD`, DONOR 외 에러 :109) |
| k 확산 `ν₀+νt/σk` | `vf_k1cal.f:113-122` (`W=1/AKSGK` :113) |
| ε 확산 `ν₀+νt/σε` | `vf_k1cal.f:123-132` (`W=1/AKSGE` :123) |
| 생성·소산 소스 | `vf_k1cal.f:134-136` (`VF_KGENE`) |
| 시간적분(Euler) | `vf_k1cal.f:138-145` (`VF_SEULER`) |
| 대수칙 벽셀 | `vf_k1cal.f:147-149` (`VF_BWKELG`) |
| 클램프 `AK←AKMINK·AE←AKMINE` | `vf_k1cal.f:156-160` |

**생성항** `VF_KGENE`(헤더 `乱流量の生成消滅項` `vf_kgene.f:6`):
- 전단생성 `GS=νt·(2(∂u/∂x)²+2(∂v/∂y)²+2(∂w/∂z)²+(∂u/∂y+∂v/∂x)²+(∂v/∂z+∂w/∂y)²+(∂w/∂x+∂u/∂z)²)` (`vf_kgene.f:160-165`)
- 부력항 `GT=0`(본 빌드 비활성, `vf_kgene.f:168`)
- k 소스 `QK += Gv·(GST-ε)` (생성-소산, `vf_kgene.f:179`)
- ε 소스 `QE += Gv·(C1·(ε/k)·GST·(1+C3·RF) - C2·(ε/k)·ε)` (`vf_kgene.f:180-181`)

**渦점성** `VF_CNUT0`(헤더 `渦動粘性係数…(k-ε2方程式モデル)` `vf_cnut0.f:5`): 정확한 식
```
vf_cnut0.f:47 :  ANUT = AKCMU * AK*AK / W      (W=MAX(AE,AKMINE))
```
= **νt = Cμ·k²/ε** (블록주석 `νt=Cμ・k2/ε` `vf_cnut0.f:41`). 분자+渦점성 합 `ANU=ANU0+ANUT`(`vf_cnu00.f:57`). 난류열확산은 Pr_t(`vf_clm00.f:58`), 물질확산은 Sc_t(`vf_cdd00.f:61`).

**모델 상수** (디폴트 `vf_a2dflt.f:169-177`, 선언/문서 `VF_APHYSR.h:31-39`, 입력 override `vf_iimdl.f:274-295`):

| 상수 | 변수 | 디폴트 | 인용 |
|---|---|---|---|
| Cμ | `AKCMU` | **0.09** | `vf_a2dflt.f:169` |
| σk | `AKSGK` | **1.0** | `vf_a2dflt.f:170` |
| σε | `AKSGE` | **1.3** | `vf_a2dflt.f:171` |
| C₁ε | `AKC1` | **1.44** | `vf_a2dflt.f:172` |
| C₂ε | `AKC2` | **1.92** | `vf_a2dflt.f:173` |
| C₃ε | `AKC3` | 0.0 | `vf_a2dflt.f:174` |
| κ(대수칙) | `AKK0` | 0.4 | `vf_a2dflt.f:175` |
| A(대수칙) | `AKA0` | 5.5 | `vf_a2dflt.f:176` |
| Pr_t | `AKPR` | 1.0 | `vf_a2dflt.f:177` |

→ **표준 Launder-Spalding k-ε** (Cμ=0.09·C₁ε=1.44·C₂ε=1.92·σk=1.0·σε=1.3), 사용자 override 가능.

## B. 포러스 body 저항 (소파블록·투과방파제)

CADMAS 의 투과성 소파구조 모델링 핵심. 두 부분으로 분리:

**(B-1) 2차 drag 力 (Morison형)** — `VF_VGENE`(헤더 `流速に関する生成消滅項` `vf_vgene.f:7`, [SMAC 단계②](cadmas-surf3d-smac-velocity-pressure-solver.md#1-smac-시퀀스-vf_v1calf-드라이버)). x운동량:
```
vf_vgene.f:108 :  UVW = SQRT(U*U+V*V+W*W)
vf_vgene.f:110 :  QU = QU - 0.5*CD*XX(5,I)*(1-GGX(I,J,K))*U*UVW
```
= **−½·C_D·(1−γ_x)·u·|u|** (y `:186`, z `:262`). `(1-GGX/Y/Z)`=면의 고체(비투과) 면적률 → drag 는 막힌 면적에 비례. drag계수 `CD` 는 셀중심 `CD0`(입력 `VF_IIPORO`, `vf_iiporo.f:239`)를 면보간(`:92·168·244`).
- **대안 Dupuit-Forchheimer 저항법칙**(`IDRGN>0` 분기, `vf_vgene.f:111-`): α=`DRGAP`·β=`DRGBT`·돌직경 `DRGDR`(`VF_APHYSR.h:107-110`), 돌크기 테이블 룩업(`:122-124`). → CADMAS 는 2가지 포러스 저항 closure 제공(기본 2차 C_D / Dupuit-Forchheimer α·β).

**(B-2) 가상질량 관성(CM)** — 명시적 力이 아니라 **운동량 시간미분항을 곱하는 유효 공극** `GLV` 로 folding:
```
vf_cglv.f:34    :  GLV = GGV + (1-GGV)*CM0           (셀중심)
vf_cglxyz.f:67  :  GLX = GGX + (1-GGX)*CM0           (면중심, GLY/GLZ 동형)
```
= Sakakiyama-Kajima형 가상질량(고체가 많은 셀일수록 유체가 큰 겉보기 관성). 매스텝 1회 산출(`vf_a1main.f:723-724`)→`VF_V1CAL` 전달(`:1058-1060`). [예측자 `/GLV`·Poisson `GGV/GLV` 결합](cadmas-surf3d-smac-velocity-pressure-solver.md#7-포러스-body-가-운동량에-들어가는-방식-요약).

> 입력계수: `CM0`(관성)·`CD0`(저항)는 3D 배열(`vf_a1main.f:65-66·234`), `VF_IIPORO`(`vf_iiporo.f:211·239`)가 입력파일 키워드 `'CM0'`/`'CD0'`(`vf_iifile.f:101-103`)로 설정.

## C. 파력 적분 (구조물 작용 波力)

`VF_CFORCE`(헤더 `指定範囲内の流体と構造物間の波力を計算する` `vf_cforce.f:6`) — **drag 루틴이 아니라** 구조물 표면 압력적분 후처리. 6 방향력 `ISW=1..6`(`vf_cforce.f:25-31`)에 대해 유체/장애물(`NF=-1`) 계면면의 `−P·dS` 합산(`vf_cforce.f:75-77·101-103`), VOF 부분셀 `FF` 가중(`:78-97`), MPI reduce(`VF_P1SUMD` `:278`). **CM·CD·u|u| drag 항 없음** — 내파설계의 작용파력(방파제 케이슨 활동·전도 검토용) 산출이 목적.

## 물리상수 헤더

`VF_APHYSR.h`(`/VF_APHYSR/` COMMON): `RHO0`밀도(:23)·`ANU0`분자동점성(:24)·`GRZ0`중력z성분(음수, :25)·k-ε상수(:31-40)·Dupuit-Forchheimer(:107-110)·속도리미터 `VVMAX`(:111). `VF_A0PRM.h`: `ZERO=1.0D-20`·`ZEROG=1.0D-6`(:22).

> ⚠️ provenance 주의(서브에이전트 전제 교정): `vf_cforce.f`=파력 적분(drag 아님), 포러스 drag 는 `vf_vgene.f`. `VF_APARAR.h`=병렬분할 격자경계(물리상수 아님). 부력생성 `C₃ε` 항은 `GT=0` 으로 비활성.
