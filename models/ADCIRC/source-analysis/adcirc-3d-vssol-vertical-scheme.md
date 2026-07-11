---
title: "ADCIRC 3D internal mode — VSSOL 연직 시간적분 스킴 (vsmy.F: θ³-가중 복소 tridiagonal + w adjoint)"
topic: general
canonical_source: self
citation_status: verified
has_source_needed: false
verification_method: "vsmy.F(5281줄) VSSOL(:142-1703)·TRIDIAG(:2097-2130)·InmINT(:2299-2319)·EDDYVIS(:1785-2062) + read_input.F 3D 블록(:5073,5102,5127-5137) + global_3dvs.F(:98,193-195) + timestep.F(:1121-1125) + docs parameter_definitions/index.rst:1309-1316(ALP1/2/3)·fort15.rst:129 직접 read (2026-07-10~11). 모든 식·계수 verbatim 인용."
note_author: "Claude Fable 5 (source-code direct read)"
note_date: 2026-07-11
related:
  - models/ADCIRC/source-analysis/adcirc-3d-mode.md
  - models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md
  - models/ADCIRC/source-analysis/adcirc-transport-solver.md
  - concepts/currents/time-integration-cross-model.md
---

# ADCIRC VSSOL — 3D internal mode 연직 시간적분

> [[adcirc-3d-mode]] 가 3D dispatch·IDEN·EOS·난류 옵션을 커버하고, [[time-integration-cross-model]] §5 가 "VSSOL 연직 시간적분 미커버"로 지적한 갭의 해소 노트. 3D 스칼라(S/T) transport 는 별도 스킴([[adcirc-transport-solver]] Alp4).

## 1. 정체 — 무엇을 언제 푸는가

- `VSSOL(IT,TimeLoc)` = 3D internal mode **수평속도의 연직구조** 솔버 (vsmy.F:142-1703). `C3DVS` 시 매 timestep 호출 (timestep.F:1121-1123; 직전에 barotropic 압력 `MOM_LV_X`→`BTP` 를 **time level s·s+1 평균**으로 적재, timestep.F 주석 "averaged between time levels s and s+1").
- **복소 속도 정식화**: `q = u + i·v` (`COMPLEX(8)`, 헤더 :124 "3D Complex Velocity field (GAMMA)") — Coriolis 가 복소 회전(스칼라 곱)이 되어 2×2 행렬 불필요.
- 시간간격: `DelT => DTDP` (read_input.F:5073, POINTER alias — global_3dvs.F:98) — **2D 와 동일 dt, 별도 subcycling 없음**. 2-time-level(s → s+1) 스킴.
- 좌표: 무차원 sigma `[b,a] = [-1,+1]` 고정 (global_3dvs.F:193-195, `AMB=A-B=2`).

## 2. θ³-가중 시간적분 — 항별 3개의 독립 implicitness

fort.15 3D 블록에서 `READ(15,*) Alp1,Alp2,Alp3` (read_input.F:5127), 계수 조립 :5132-5137:

```fortran
IDTAlp1   = iy*DelT*Alp1      ! Coriolis LHS      (iy = 복소 i)
IDT1MAlp1 = iy*DelT*(1.-Alp1) ! Coriolis RHS
DTAlp3    = DelT*Alp3         ! 연직확산 LHS
DT1MAlp3  = DelT*(1-Alp3)     ! 연직확산 RHS
DTAlp2    = DelT*Alp2         ! 저면응력 LHS
DT1MAlp2  = DelT*(1.-Alp2)    ! 저면응력 RHS
```

공식 의미 (docs `parameter_definitions/index.rst:1309-1316` verbatim): "Time weighting coefficients for the 3D velocity solution. 0.= fully explicit, 0.5=time centered, 1.= fully implicit". (fort15.rst:129 에 입력 라인.)

| 항 | θ knob | LHS 반영 (vsmy.F) |
|---|---|---|
| **Coriolis** | `Alp1` | `CCL = 1 + Corif·IDTAlp1` (:993) — 복소 대각 회전 |
| **저면응력(slip)** | `Alp2` | `Mk(1) += DTAlp2·TK(NH)/Hsp1OAMB` (:1015) |
| **연직확산** | `Alp3` | `RCL = DTAlp3/Hsp1Hsp1OAMBAMB` (:995) — sigma 사상에서 온 `1/(H/(a−b))²` 배율 |

**explicit(RHS 전용) 항**: 수평이류 `LAdvec`(:870, `sponge·IFNLCT` 게이트)·수평응력 `LStress = 3·EVM·(...)`(:871)·biharmonic(:923)·**연직이류 `VAdvec`**·경압 `BPG`·순압 `BTPG`(s+1/2 평균) — 전부 Fr 벡터로만 (:1019-1026).

## 3. 연직 이산화 — linear FE Galerkin (consistent mass)

- **질량행렬 `Inm`** (InmINT, vsmy.F:2299-2319): 선형 요소 `∫ψₙψₘ dσ` — `Inm(k,3)=(σ(k+1)−σ(k))/6`, `Inm(k,2)=2(Inm(k,1)+Inm(k,3))` 의 고전 1D FE 3-band. **lumped 아님** — RHS 에서 이웃층 값이 `Inm(k,1)/(k,3)` 로 가중됨 (:1020-1025).
- **확산행렬 `KVnm`** (:589-598): `KVnm(k,3) = −½(EVTot(k+1)+EVTot(k))/(σ(k+1)−σ(k))`, `KVnm(k,2) = −(KVnm(k,1)+KVnm(k,3))` — 요소 평균 eddy viscosity 의 flux 형, 행합 0(보존형). `EVTot` 은 매 node·step `EDDYVIS` 호출로 갱신 (:584; IEVC 프로파일 카탈로그·MY2.5 `IEVC=50/51 → CALL TURB` :2038 은 [[adcirc-3d-mode]] §F).
- 조립: `Mkm1/Mk/Mkp1(k) = CCL·Inm(k,·) + RCL·KVnm(k,·)` (:1027-1029) — 복소 3-band compact storage.

## 4. 해법 — 복소 Thomas (TRIDIAG)

- `CALL TRIDIAG(Mkm1,Mk,Mkp1,Fr,Gamma,NFEN)` (:1125) → `qkp1(NH,k)=Gamma(k)` (:1133). node 별 독립 — 수평 결합은 explicit 항에만 있으므로 **NFEN 크기 복소 tridiagonal 을 NP 번** 푸는 구조.
- TRIDIAG(:2097-2130): 위→아래 소거(`DO J=nfen-1,1,-1`) + 대각 0 검사 시 즉시 terminate ("Diagonal term in the VS matrix is zero").
- 시간레벨 shift: `q(NH,k)=qkp1(NH,k)` (:1678) — `qkp1` 을 별도 보존하는 이유는 transport 계산 공급 (:1127-1130 주석).

## 5. 경계조건

- **바닥**: `ISlip=0` no-slip → Dirichlet 행 `Fr(1)=0, Mk(1)=(1,−1)` (:997-1001; 주석 "-I*IV=V") / `ISlip≥1` slip → 저면응력을 `TK(NH)` 로 LHS(Alp2)·RHS(1−Alp2) 분배 (:1010,:1015). `ISlip=1` 선형 slip 계수, `=2` 최소 2차, `=3` 2차 (헤더 :946-948; `READ(15,*) ISlip,KP` read_input.F:5102). ※2016 개정으로 `KSlip` 대신 2D 마찰 `TK` 재사용 (":1009-1010 주석 arash May 31 2016 based on Rosemary's work" — 구식 KSlip 코드 주석잔존).
- **표면**: 바람응력을 natural BC 로 `Fr(NFEN)` 에 — `+ ΔT·½·(WS^{s+1}/H^{s+1} + WS^s/H^s)` (:1043-1046) = **고정 trapezoidal(½·½)**, Alp 가중과 무관. `NWS≠0` 게이트 (:1042, Casey 220120).
- **측면 flux 경계**: 법선/접선 회전 후 행 수정 — `LBcodeI 0~9` essential normal flux + free tangential slip, `10~19` zero tangential slip, `20~29` natural (:1053-1090).

## 6. 연직속도 w — 연속식 적분 + ★adjoint 보정

1. 바닥 kinematic BC: `WZkp1(NH,1) = −u·∂h/∂x − v·∂h/∂y` (:1377).
2. 아래→위 연속식 marching (:1379-1388): 층별 수평발산(`DUDX+DVDY`, 요소 FE 기울기 :1347-1357) + sigma 사상 보정항.
3. **adjoint 보정** (:1390-1404): 표면 kinematic BC `WZSurfBC = ∂η/∂t + u·∂η/∂x + v·∂η/∂y` (:1396; `DEtaDT=(Eta2−Eta1)/DelT` :603) 와 적분값의 불일치를 `WZCorrection = (WZSurfBC−WZSurf)·(Wf/H² + (σ−b)/(a−b))/(2Wf/H²+1)` 로 전 층에 분배 (:1401-1403).
   - ★`Wf=0.d0` **하드코딩** (:1392, 주석 "This value should match surface B.C. exactly") → 보정이 σ-선형, 표면에서 정확 일치·바닥 kinematic BC 보존.
4. dry 노드(활성 요소 0)는 w=0 (:1408-).

## 7. ★Findings / 함정

- **θ 가 하나가 아니라 셋** — Coriolis·저면응력·연직확산이 독립 `Alp1/Alp2/Alp3`. 문서 기본값 권고는 없음(0/0.5/1 의미만) — 값 선택은 사용자 몫.
- **이류는 전부 explicit** — 수평(LAdvec)·연직(VAdvec) 이류 모두 RHS. implicit 은 연직확산·Coriolis·저면응력뿐 → 3D 층내 강한 연직이류·수평이류는 여전히 dt 제약 요인. ROMS 의 implicit 연직이류 옵션(OMEGA_IMPLICIT)과 대비 ([[time-integration-cross-model]] §4).
- **consistent mass** — 연직 FE 가 lumped 아님: RHS 에 이웃층 기여(Inm off-diagonal). 층별 후처리 시 `q` 를 point value 로 취급해도 되지만 모멘텀 수지 분석은 Inm 가중 고려.
- **바람응력 시간가중은 Alp 와 무관한 고정 ½** (:1043-1046) — Alp3=1(완전 implicit) 로 놓아도 표면 강제는 centered.
- **복소 정식화 함정**: `u=REAL(q)`, `v=AIMAG(q)` — 디버깅·후처리에서 실수부/허수부 혼동 주의. Coriolis 부호는 `CCL=1+i·f·ΔT·Alp1` 회전에 내장.
- **2016 슬립계수 이관**: 저면 slip 이 자체 `KSlip=KP·|q(1)|` 계산(주석처리 :985-988, :1009, :1014)에서 2D 마찰계수 `TK(NH)` 재사용으로 변경 — fort.15 `KP` 는 `ISlip` 분기 선택에만 잔존 의미. 구문서와 코드가 다를 수 있는 지점.
- **w 는 사후진단적** — qkp1 확정 후 연속식으로 유도(모멘텀에 재결합 없음), 보정은 표면 BC 정확 일치 지향(`Wf=0`).

## 연결

- [[adcirc-3d-mode]] — IDEN dispatch·EOS·IEVC 난류 카탈로그(§F)·MY2.5
- [[adcirc-transport-solver]] — 3D S/T transport 의 별도 semi-implicit(Alp4)·ADC_TRIDAG2
- [[adcirc-timestep-orchestration]] — per-step 순서(VSSOL 은 GWCE·momentum 후)
- [[time-integration-cross-model]] §4 — 12모델 연직 implicit 대조
