---
title: "SWASH 부유체·강체 6DOF — floating object / moving rigid body 운동·유체력·KBC"
model: SWASH
component: src (floating rigid body)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashRigBoddata.ftn90(모듈 변수·ribdat type), SwashMotionRigidBod.ftn90(generalized-alpha 적분), SwashForcesRigidBod.ftn90(mooring·fender·복원력·rotatep), SwashHydroLoads.ftn90(Froude-Krylov 압력적분), SwashFloatObjects.ftn90(draft·label·면적/부피/관성모멘트·pretension), SwashUpdKBCrigb.ftn90(운동학 BC), SwashFlobjOutp.ftn90(출력)을 각 file:line 인용; 2026-10-15 SWASH recovery 대조 보고서 반영"
last_source_check: "2026-10-15 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/SWASH/source-analysis/swash-architecture-source-map.md
  - models/SWASH/README.md
---

# SWASH 부유체·강체 6DOF — floating object / moving rigid body

> SWASH의 부유체 기능은 두 모드로 나뉜다: `ifloat==1`(고정체, 압력장만 부과·하중은 출력용) vs `ifloat==2`(운동하는 강체). 강체 운동은 generalized-alpha 시간적분으로 풀고, 유체력은 선체 wet surface 위 전압력(정수압+비정수압) 적분(Froude-Krylov)으로 얻으며, 계류삭(mooring)·fender·부력복원력이 추가된다. (경로: raw/source_code/swash/src/) [10-15 대조 정정]

## 1. 두 가지 부유체 모드 (`ifloat`)

| 값 | 의미 | 근거 |
|---|---|---|
| `ifloat == 1` | 고정 부유체(fixed body). 압력장만 부과, 하중은 출력 목적으로만 계산 | `SwashFloatObjects.ftn90:314-317` (`lfbs = 1` "superfluous, but used to compute hydrodynamic loads as output"), `SwashFlobjOutp.ftn90:103-114` |
| `ifloat == 2` | 운동하는 강체(moving rigid body). 2D 평면 격자의 강체는 여섯 자유도를 선택할 수 있다. | `SwashFloatObjects.ftn90:318-322`, `SwashMotionRigidBod.ftn90:84` (`if ( ifloat /= 2 ) return`); `src/SwashReadInput.ftn90:1071–1088`의 여섯 자유도 선택; inputs-setup:SI1-563. [10-15 대조 정정] [10-15 전수 검증 보완] |

1D에서는 SWAY·ROLL·YAW를 비활성화한다. SURGE·HEAVE·PITCH의 입력 선택은 유지한다 (`src/SwashCheckPrep.ftn90:1872–1874,1900–1906`; inputs-setup:SI1-563). [10-15 대조 정정] [10-15 전수 검증 정정]

운동 루틴들(`SwashMotionRigidBod`, `SwashForcesRigidBod`, `SwashUpdKBCrigb`)은 모두 `ifloat /= 2`일 때 즉시 return — `SwashMotionRigidBod.ftn90:84`, `SwashForcesRigidBod.ftn90:93`, `SwashUpdKBCrigb.ftn90:88`.

## 2. 데이터 구조 (`SwashRigBoddata`)

모듈 목적(verbatim): `SwashRigBoddata.ftn90:40` "Module containing data for rigid bodies computation".

### 2.1 6 자유도(DOF) 인덱싱
`bdof(:,:,:)` logical 배열이 각 DOF 활성 여부를 나타낸다 (`SwashRigBoddata.ftn90:128-135`, verbatim):
- `bdof(:,1,1)`: surge, `bdof(:,2,1)`: sway, `bdof(:,3,1)`: heave (병진, 2번째 인덱스 = ndim 방향, 3번째 인덱스 1 = translation)
- `bdof(:,1,2)`: roll, `bdof(:,2,2)`: pitch, `bdof(:,3,2)`: yaw (회전, 3번째 인덱스 2 = rotation)

`ndim = 3` (`SwashRigBoddata.ftn90:54` "number of dimensions related to body motions").

### 2.2 상태 변수 (previous=0 / current=1 시간레벨)
강체별·DOF별로 운동학 상태를 보관 (`SwashRigBoddata.ftn90:105-126`):

| 변수 | 의미 |
|---|---|
| `afot0/1`, `afor0/1` | 선형/각 가속도 (translation/rotation) |
| `vfot0/1`, `vfor0/1` | 선형/각 속도 |
| `xfot0/1`, `xfor0/1` | 선형/각 변위 |
| `xfoti`, `xfori` | FSI 반복과정 중간 변위 (`:123,:126` "intermediate ... in iterative process of fluid-structure interaction") |
| `fhyd0/1`, `thyd0/1` | 유체동역학 힘/토크 |
| `fbod0/1`, `tbod0/1` | 스프링-댐핑(계류·fender·복원) 힘/토크 |

### 2.3 물성·부력 관련
- `bmass` 질량, `bmoi(:,:)` 회전축별 관성모멘트, `bcog(:,:)` 무게중심 좌표 (`SwashRigBoddata.ftn90:83,97,77`)
- `barea` 수선면적(water plane area), `bvol` 잠긴 부피, `bcob` 부심(center of buoyancy), `bmoax/bmoay` x/y축 단면 2차모멘트 (`:75,98,76,95-96`)

### 2.4 계류삭·fender 파라미터
- `bmli(:,:,1:10)`: 계류삭. 1=스프링계수, 2=댐핑계수, 3-5=해저 부착점(COG 상대), 6-8=선체 부착점(COG 상대), 9=평형길이, 10=프리텐션계수 (`SwashRigBoddata.ftn90:84-94`, verbatim)
- `bfen(:,:,1:4)`: fender. 1=스프링계수, 2-4=선체 부착점 (`:78-82`)
- `cpto` 프리텐션 포함 여부, `ptop` PTO(power take-off) 출력 (`:136,103`)

### 2.5 시간적분 스킴 선택 (`mfoti`)
`SwashRigBoddata.ftn90:59-63` (verbatim): 1=Newmark, 2=Chung-Hulbert, 3=Hilber-Hughes-Taylor, 4=Wood-Bossak-Zienkiewicz. `alfaf`(힘 implicitness), `alfam`(관성 implicitness)는 generalized-alpha 스킴이 내부 결정 (`:67-70`).

또한 linked-list용 derived type `ribdat`(label, nfen, nmli, parm(7), dof(6), fen/mli pointer, nextrib pointer)와 target `frigbod`이 정의됨 (`SwashRigBoddata.ftn90:138-149`).

## 3. 운동방정식 적분 — generalized-alpha (`SwashMotionRigidBod`)

목적/방법(verbatim): `SwashMotionRigidBod.ftn90:40` "Solves the equations of motion for floating rigid bodies", `:44-50` — 선형·각운동량 보존에서 유도된 force/torque balance를 generalized-alpha (Chung & Hulbert 1993)로 풀며, 특수 케이스로 Newmark(1959, 비소산)와 Chung-Hulbert(2차 소산, SWASH 기본)가 있음.

### 3.1 파라미터
`SwashMotionRigidBod.ftn90:86-88`: `alfa = pship(10)` (under-relaxation factor), `beta = pship(3)`, `gamma = pship(4)` (generalized-alpha implicitness factors). `alfam`, `alfaf`는 모듈 변수로부터.

FLOAT의 ALPHA 판독은 `call INREAL ( 'ALPHA', pship(1), 'STA', 0. )`이다 (`src/SwashReadInput.ftn90:1226`; inputs-setup:SI1-569 수정안; guide-syntax-build:SG1-612). [10-15 대조 정정]
가속도 완화의 RELAX 판독은 `call INREAL('RELAX'  , pship(10), 'STA', 0.3)`이다 (`src/SwashReadInput.ftn90:1021`; inputs-setup:SI1-569 수정안). [10-15 대조 정정]
NEWMARK의 BETA 판독은 `call INREAL ('BETA' , pship(3), 'STA', 0.25)`이다 (`src/SwashReadInput.ftn90:1003`; inputs-setup:SI1-569 수정안). [10-15 대조 정정]
범위 밖 BETA는 경고 후 0.25로 바꾼다 (`src/SwashCheckPrep.ftn90:1379–1381`; inputs-setup:SI1-569 수정안). [10-15 대조 정정]
NEWMARK의 GAMMA 판독은 `call INREAL ('GAMMA', pship(4), 'STA', 0.50)`이다 (`src/SwashReadInput.ftn90:1004`; inputs-setup:SI1-569 수정안). [10-15 대조 정정]
범위 밖 GAMMA는 경고 후 0.5로 바꾼다 (`src/SwashCheckPrep.ftn90:1383–1385`; inputs-setup:SI1-569 수정안). [10-15 대조 정정]
CH·HHT·WBZ의 읽기 기본은 모두 1이다 (`src/SwashReadInput.ftn90:1007,1010,1014` `call INREAL ('RHO', pship(5), 'STA', 1.0)`; inputs-setup:SI1-569 수정안). [10-15 대조 정정] [10-15 전수 검증 보완]
범위 밖 값은 실제 계수 계산에 사용하는 rhoinf를 1로 고친다 (`src/SwashCheckPrep.ftn90:1388–1391`; inputs-setup:SI1-569 수정안). [10-15 대조 정정]
CH·HHT·WBZ가 각각 alfam·alfaf를 계산한다 (`src/SwashCheckPrep.ftn90:1406–1421`; inputs-setup:SI1-566). [10-15 대조 정정]
이어서 beta·gamma를 rho에서 다시 정한다 (`src/SwashCheckPrep.ftn90:1427–1429`; inputs-setup:SI1-566). [10-15 대조 정정]

### 3.2 병진 운동 (translation, `:92-123`)
각 body `m`, 방향 `n`에 대해 `bdof(m,n,1)`가 true일 때만 (`:96`):

단위질량당 총 힘 (`:100-101`):
$$f_0 = \frac{f_{hyd,0}+f_{bod,0}}{m_{body}}, \quad f_1 = \frac{f_{hyd,1}+f_{bod,1}}{m_{body}}$$

가속도 갱신 (generalized-alpha, `:109`):
$$a_1 = \frac{-\alpha_m\, a_0 + \alpha_f\, f_0 + (1-\alpha_f)\, f_1}{1-\alpha_m}$$

under-relaxation (`:105,113`): `accu`에 이전 반복값 저장 후 $a_1 \leftarrow \alpha\, a_1 + (1-\alpha)\,a_{prev}$ — FSI 반복 안정화용.

속도·변위 (Newmark 형, `:117,119`):
$$v_1 = v_0 + \Delta t\,[\gamma\, a_1 + (1-\gamma)\, a_0]$$
$$x_1 = x_0 + \Delta t\,\{v_0 + \Delta t\,[\beta\, a_1 + (0.5-\beta)\, a_0]\}$$

### 3.3 회전 운동 (rotation, `:127-158`)
구조 동일하나 `bdof(m,n,2)` 검사(`:131`), 단위 각질량당 토크 $f_0=(t_{hyd,0}+t_{bod,0})/I$ where $I=$`bmoi(m,n)` (`:135-136`), 그리고 `afor/vfor/xfor` 사용. ⚠ 회전은 축별 관성모멘트로 분리 적분 — 완전한 6DOF 자이로스코픽 결합항(coupled rigid-body Euler 방정식)은 보이지 않음(축별 독립 ODE).

## 4. 유체동역학 하중 — Froude-Krylov (`SwashHydroLoads`)

목적/방법(verbatim): `SwashHydroLoads.ftn90:41` "Calculates hydrodynamic loads acting on floating body", `:44-56` — wet surface 위 전압력 적분으로 Froude-Krylov 힘을, 무게중심 둘레 모멘트를 동일하게 적분. 비정수압은 각 연직층에서 **선형분포 가정**, 적분 기여는 직사각형(작용점 1/2 높이)+삼각형(작용점 2/3 높이) 두 부분으로 분해.

호출: `SwashForcesRigidBod.ftn90:97`에서 `call SwashHydroLoads ( mbod, fhyd1(1,1)..thyd1(1,3) )`로 current 시간레벨 힘/토크를 산출.

### 4.1 압력 성분
- 정수압: $\text{frc1} = \rho_w g (s_1 + \text{flos})\,dx$ (연직), 측면은 $\tfrac12 \rho_w g\,dz^2$ (`SwashHydroLoads.ftn90:170,204`)
- 비정수압($q$): `ihydro /= 0`일 때만 (`:181,215`). 연직은 셀중심 $q(nm,1)$ (`:184`), 측면은 층계면 정의된 $q$의 직사각형+삼각형 (`:242-243`):
  $$\text{frc1}=\rho_w\, q_d\, dz, \quad \text{frc2}=\rho_w\,\tfrac12(q_d+q_k)\,dz$$
- 선체에서의 비정수압 보간(부분 잠긴 층, `:258`): `qh = q(nm,k) - (qd-q(nm,k))*(zloc+flos)/(sloc-zloc)` — 층 내 선형보간으로 hull 위치 압력.

### 4.2 작용점·모멘트 팔
moment arm은 무게중심 기준 (`:174,208`): `rx = 0.5*(xcgrid+xcgrid_md) - bcog(l,1)`, `rz2 = s1 - 2/3*dz - bcog(l,3)` (삼각형), `rz1 = ... - 1/2*dz - ...` (직사각형). 모멘트 = 힘 × arm (예 `momy(l) = momy(l) - rx*frc1`, `:177`).

### 4.3 1D vs 2D 분기
- 1D: `oned`일 때 u-point 루프 (`:145-497`), 연직력+y축모멘트(pitch), x방향 수평력(port/starboard side) 처리.
- 2D: `:498-1464`, 추가로 sway(y방향 힘)·roll(x축모멘트)·yaw(z축모멘트). 좌표회전 적용:
  - `ifloat==1`(고정·출력용)일 때 `alpobj` 각으로 격자를 회전 (`:502-515`), `beta = ±(π-alpobj)` (`:506-510`).
  - `ifloat==2`(운동체)일 때 **회전 안함** — `calpo=1, salpo=0, cbeta=-1, sbeta=0` (`:517-525`, verbatim "in case of moving bodies, do not rotate!").
  - 힘 회전: `frc_rx = frc*cbeta`, `frc_ry = frc*sbeta` 등 (`:610-611`).

### 4.4 선체 형상 케이스
세 가지 기하 상황을 각 방향별로 처리: (a) 선체 바로 아래(`presp(nm)==1`, 연직력) `:163,560`; (b) 선체 옆 압력화↔자유표면 전이(port/starboard side) `:195,279,598,715`; (c) 선체 밑면 단차(`flos(nm)<flos(neighbor)`, "underneath floating object") `:363,832,1263`. `presp`(pressurized point flag)와 `lfbs`(label of floating body, `:165`) 로 셀 판별.

### 4.5 병렬 reduce
서브도메인 합산: `SWREDUCE(forx/forz/momy,...,SWSUM)` (1D/2D 공통, `:1468-1470`), 2D 추가로 `fory/momx/momz` (`:1472-1477`). 서브도메인 경계 끝점은 이웃이 소유하므로 제외 (`mend=ml-1` 등, `:149-150,530-534`).

## 5. 외력: 계류·fender·복원력·중력·PTO (`SwashForcesRigidBod`)

목적/방법(verbatim): `SwashForcesRigidBod.ftn90:40` "Computes forces and torques on moving rigid bodies", `:44-51` — (1) 유체 압력에 의한 Froude-Krylov 힘, (2) 계류삭·fender 힘, (3) 부력 복원력. 복원력은 body 운동이 전산 schematization에 포함되지 않으므로 **명시적으로(explicitly) 추가**해야 함.

### 5.1 계류삭 (mooring line, linear spring-mass-damper, `:101-155`)
선체 부착점(`bmli(m,l,6:8)`)을 각변위로 회전(`rotatep`, `:115`) 후 선형변위 추가(`:123-125`), 해저 부착점(`bmli(m,l,3:5)`) 기준 위치 계산(`:129-131`):
- 길이 `lml = sqrt(vec·vec)` (`:135`), 연신 `extml1 = lml - bmli(m,l,9)`(평형길이) (`:139`), 연신율 `demldt = (extml1-extml0)/dt` (`:143`).
- 힘 (`:147`): $f_{ml} = \text{pretension} + k\cdot\text{ext} + c\cdot\dot{\text{ext}}$ (`bmli(m,l,10) + bmli(m,l,1)*extml1 + bmli(m,l,2)*demldt`).
- 방향각 `angml(l,1:3) = atan2(...)` 각 성분 (`:151-153`).

### 5.2 Fender (linear spring-mass, `:159-208`)
부착점을 **역**각변위로 회전(`:169` `-xfor1`) 후 역병진(`:173-175`). 회전된 fender 위치가 hull 안쪽이면(`vecr(2) > vec(2)` 아님, `:184`) 힘 계산:
- 스프링 `fspr = bfen(m,l,1)*(vec(2)-vecr(2))` (`:186`), 댐핑 `fdmp = 1.e6 * vfot1(m,1)` (`:187`, ⚠ 하드코딩 계수 1.e6), 합력 `ffe = sqrt(fspr²+fdmp²)` (`:191`).
- 주석(verbatim, `:182`): "estimated as original position of fender and only considering the y-coordinate, which should be okay if motions are small compared to body size" — 소변위 근사.

### 5.3 스프링-댐핑 힘·토크 합산 (`:212-256`)
병진력 `fbod1(m,n) = -Σ f_ml·sin(angml) - Σ ffe·sin(angfe)` (`:217,220`). 토크는 축별로 cross-product 형태로 (`:230,239,248` 등), 변위벡터 `disml/disfe`와 각 성분의 sin 곱. `bdof` 비활성 DOF는 건너뜀(`:215,228,237,246`).

### 5.4 부력 복원력 (`:258-269`)
heave·roll·pitch에만 존재 (verbatim `:259`). 
- heave: `fbod1(m,3) -= rhow*grav*barea(m)*xfot1(m,3)` (`:263`) — 수선면적 × 침하 변위.
- roll: `tbod1(m,1) -= (rhow*grav*(bmoax + bvol*bcob) - grav*bmass*bcog(:,3))*xfor1(m,1)` (`:265`) — metacentric 복원토크 형태(단면2차모멘트+부심-무게중심 항).
- pitch: `bmoay`로 동일 (`:267`).

### 5.5 중력·PTO
중력은 heave에 `fbod1(m,3) -= bmass(m)*grav` (`:275`). PTO 출력 `ptop(m) = Σ bmli(m,l,2)*demldt²` — 댐핑계수×연신율² (`:284-290`, verbatim "based on damping coefficient of the PTO unit").

### 5.6 회전행렬 (`rotatep`, contained, `:296-348`)
오른손 법칙 회전행렬 $R_x,R_y,R_z$ 정의 후 (`:312-340`), 적용 순서 (verbatim `:342-344`): "rv = rz * ry * rx * v" — `rv = matmul(matmul(matmul(rz,ry),rx), v)` (`:346`). roll→pitch→yaw 순(오른쪽부터 적용).

## 6. 운동학 경계조건 갱신 (`SwashUpdKBCrigb`)

목적(verbatim): `SwashUpdKBCrigb.ftn90:40` "Updates kinematic boundary conditions at rigid body surface". 강체 운동으로 인한 선체 표면 법선속도를 `skc(nm)`에 누적 — 비정수압 압력 결합(Neumann형 BC)에 쓰임.

### 6.1 implicit 가중
`theta = pship(11)` (`:90`), body 속도 `vrb = theta*v1 + (1-theta)*v0` (예 surge `:116`) — 시간 implicitness.

### 6.2 DOF별 기여 (`skc` 누적)
각 DOF가 선체 아래(underneath, `presp(nm)==1`) 및 선체 옆 전이(port/starboard side) 셀에서 hull slope와 곱해져 누적:
- **surge** (`:107-165`, 2D `:285-349`): `skc += vrb*dsdx`, side는 `skc -= vrb*dsdx` where `dsdx = (flou(nm)-flou(nmd))/dx` (hull slope, flou는 아래쪽 양). 
- **sway** (2D만, `:351-415`): `flov` slope, dsdy.
- **heave** (`:167-180,417-430`): `skc += vrb` (slope 무관, 순수 연직).
- **roll** (2D, `:432-510`): `skc -= vrb*rz*dsdy + vrb*ry` (`:456`) — 위치벡터 ry/rz와 결합.
- **pitch** (`:182-254,512-590`): `skc += vrb*rz*dsdx - vrb*rx` (`:204`).
- **yaw** (2D, `:592-725`): `skc += -vrb*ry*dsdx + vrb*rx*dsdy` (`:619`).

위치벡터는 모두 무게중심 상대 (`rx = ... - bcog(l,1)` 등, `:196`), `rz`는 hull 위치(`-0.5*(flou+flou_d)-bcog(l,3)` 등 `:198`). `skc=0.`로 초기화 (`:92`).

## 7. 부유체 파라미터 계산 (`SwashFloatObjects`)

목적/방법(verbatim): `SwashFloatObjects.ftn90:41` "Determines some parameters for floating objects", `:45-50` — (1) 수위/속도점 draft, (2) 운동 강체 label, (3) 면적·부피·단면2차모멘트·부심, (4) 계류삭 프리텐션.

### 7.1 Draft 계산 (`dpsopt` 방식)
수위점 draft `flos`를 사용자 입력 `flobjf`로부터 4가지 방식 (`:122-130` 1D, `:166-174` 2D): 1=min, 2=평균, 3=max, 4=직접. 속도점 draft는 "tiled approach"로 `flou=max(flos,flos_nmu)`, `flov=max(flos,flos_num)` (`:240,265,284`). 음의 수심 체크(`:310`).

### 7.2 Label 부여
`ifloat==1`이면 `lfbs=1`(출력용 superfluous, `:316`), `ifloat==2`이면 `lfbs = int(lbodf)` 사용자 정의 라벨 (`:320`).

### 7.3 body 물성 적분 (`ifloat==2`만, `:335-451`)
셀별로 면적 `area`, 부피 `vol=flos*area`, 단면2차모멘트 `bmoax/bmoay += r²*area`, 부심 `bcob -= 0.5*flos*vol` 누적 (`:361-374` 1D, `:415-430` 2D). 서브도메인 reduce 후 `bcob = bcob/bvol`로 정규화 (`:441-449`).

### 7.4 계류삭 프리텐션 (`:455-491`)
`cpto(m)` true면, 수직성분이 부력을 상쇄하도록 초기 경사 계산: `fac = (rhow*bvol - bmass)*grav / nmlb` (`:466`), 경사 `gamma = atan2(수직차, 수평거리)` (`:470`), `bmli(m,n,10) = fac/sin(gamma)` (`:473`). 수평선이면 프리텐션 0 (`:475-476`). `cpto` false면 0 (`:483`).

## 8. 출력 (`SwashFlobjOutp`)

목적(verbatim): `SwashFlobjOutp.ftn90:40` "Requests hydrodynamic loads and/or body motions for the purpose of output". 출력량 인덱스(`oqproc`/`voqr`):

| idx | 양 | 단위변환 | line |
|---|---|---|---|
| 101-103 | surge/sway/heave 힘 | /1000 (kN) | `:140-148` |
| 104-106 | roll/pitch/yaw 모멘트 | /1000 | `:152-160` |
| 107-109 | x/y/z 병진 변위 | `xfot1` | `:172-180` |
| 110-112 | roll/pitch/yaw 회전 | `xfor1*180/pi` (deg) | `:184-192` |
| 113 | PTO power | /1000 (kW) | `:196` |

`ifloat==1`은 출력 직전 `bdof`를 `oqproc(100+l)`로 세팅 후 `SwashHydroLoads` 직접 호출(`:107-114`), `ifloat==2`는 이미 계산된 `fhyd1/thyd1`을 그대로 복사(`:120-126`). 변위·회전·PTO 출력은 `ifloat==2`에서만(`:166-200`).

출력 단위: [outputs §2.4 출력 변수 이름·단위·정의](../../../_staging/recovery/compare/swash-outputs-vs-code.md#24-p109118-출력-변수-이름단위정의) (outputs:SO1-305 수정안).

## 9. 전체 흐름 (요약)

1. 초기화: `SwashFloatObjects` — draft·label·body 물성·프리텐션 (`SwashFloatObjects.ftn90:107~`).
2. 매 time step(`ifloat==2`): `SwashForcesRigidBod` → 내부에서 `SwashHydroLoads`(유체력) + 계류/fender/복원/중력/PTO (`SwashForcesRigidBod.ftn90:97~292`).
3. `SwashMotionRigidBod` — generalized-alpha로 가속도·속도·변위 갱신, under-relaxation(FSI) (`SwashMotionRigidBod.ftn90:92~158`).
4. `SwashUpdKBCrigb` — 갱신된 body 속도로 hull 표면 KBC(`skc`) 재계산 → 압력 결합 (`SwashUpdKBCrigb.ftn90:92~`).
5. 출력 요청 시 `SwashFlobjOutp`.

FSI 반복 조건은 `if ( ( resm(1) > epslin(1) .or. resm(2) > epslin(2) ) .and. j < maxit ) then`이다 (`src/SwashComputStruc.ftn90:107`; inputs-setup:SI1-569 수정안). [10-15 대조 정정]
병진·회전 변위의 반복 간 최대 차이를 비교한다 (`src/SwashComputStruc.ftn90:153,160`; inputs-setup:SI1-569 수정안). [10-15 대조 정정]
이전 시간 병진·회전 변위가 기준을 확대할 수 있다 (`src/SwashComputStruc.ftn90:92–96`; inputs-setup:SI1-567). [10-15 대조 정정]
실제 기준은 각각 `max(tol,tol×max(abs(이전 변위)))`이다 (`src/SwashComputStruc.ftn90:92–96`; inputs-setup:SI1-567). [10-15 대조 정정] [10-15 전수 검증 정정]
회전은 라디안 기준이다 (`src/SwashComputStruc.ftn90:160,175–177`; inputs-setup:SI1-567). [10-15 대조 정정] [10-15 전수 검증 보완]
이동 강체에서 relax 밖값을 0.3으로 고친다 (`src/SwashCheckPrep.ftn90:1436–1438`; inputs-setup:SI1-568). [10-15 대조 정정]
이동 강체가 아니면 `tol=0`·`maxiter=1`로 바꾼다 (`src/SwashCheckPrep.ftn90:1440–1443`; inputs-setup:SI1-568). [10-15 대조 정정]


## 문서와 코드 차이 (10-15 대조)

출처: [inputs-setup](../../../_staging/recovery/compare/swash-inputs-setup-vs-code.md), [outputs](../../../_staging/recovery/compare/swash-outputs-vs-code.md), [guide-syntax-build](../../../_staging/recovery/compare/swash-guide-syntax-build-vs-code.md)의 최종 결론과 원문 인용.

문서 판: SWASH 12.01 매뉴얼 swashuse·swashtech, 공개 저장소 `7949227 2026-05-06 "release v12.01"`에서 마지막 변경; 코드 판: `VERNUM 12.01`, 공개 저장소 main `a486d5f 2026-05-26`, 12.01 뒤 `608ffd7`·`9554c98` 포함.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| guide-syntax-build:SG1-612 | swashuse PDF p.157 (edt 106–106): FLOAT [alpha] [theta] | swashuse PDF p.157 (edt 106–106): `FLOAT [alpha] [theta]` | `src/SwashReadInput.ftn90:981–983`의 FLOAT 공통 진입부가 `call INKEYW ('REQ',' ')`를 먼저 호출한다. `src/ocpcre.ftn:342–348`은 INT·REAL에서 `CALL MSGERR (2, 'Data field skipped:'//ELTEXT)` 후 `GOTO 510`으로 다음 필드를 읽는다. `src/SwashReadInput.ftn90:1226–1227` `call INREAL ( 'ALPHA', pship(1), 'STA', 0. )` / `call INREAL ( 'THETA', pship(2), 'STA', 1. )`. 이름 입력은 `src/ocpcre.ftn:606–609`의 KEY·NAAM 비교 경로를 탄다. `switch.pl:57–66`의 비활성 접두어 규칙은 이 일반 소스 행들을 주석으로 만들지 않는다. | E 코드 결함 후보 · 강함 | FLOAT의 위치 수치 입력은 선행 INKEYW(REQ)에서 건너뛴다. 예를 들어 `FLOAT 0.2 0.7`은 수치마다 수준 2 오류를 기록하며 ALPHA·THETA의 STA 판독에는 기본값 0·1이 남는다. ALPHA와 THETA에 이름을 붙인 입력은 별도 경로로 읽는다. 결함 도입은 재등록 blame인 f7ebbca가 아니라 5d279d7(2022-12-27 v9.01)이다. 12.01 문서와 소스의 PFLOW 수치 구문이 함께 남아 있고 후속 608ffd7·9554c98도 이 경로를 바꾸지 않았다. 같은 판의 입력 구문 모순이므로 A가 아닌 E 강함이다. 준비 단계의 범위 보정은 버린 수치를 복구하지 않는다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| guide-syntax-build:SG1-892 | 부체 theta·시간적분 조건 | swashuse PDF p.69–70·100은 부체의 가압 흐름과 IMPLICIT 요구를 설명한다. `THETA=0.5`의 0.51 보정과 움직이는 부체의 ALPHA 강제 대입은 명시하지 않는다. | `src/SwashCheckPrep.ftn90:1115–1143` `horwinc = .false.` / `!` / `if ( mtimei /= 2 ) call msgerr (3, 'semi-implicit time integration is required in case of floating object or pressurized flow')` / `!` / `if ( pship(1) < 0. .or. pship(1) > 1. ) then` / `call msgerr (1, 'incorrect compressibility factor for flow beneath fixed floating object')` / `pship(1) = 0.` / `endif` / `!` / `if ( pship(2) < 0.5 .or. pship(2) > 1. ) then` / `call msgerr (1, 'incorrect theta value for time integration beneath floating object')` / `pship(2) = 1.` / `endif` / `!` / `if ( .not. pship(2) /= 0.5 ) pship(2) = 0.51` / `!` / `! check motion rigid bodies` / `!` / `if ( ifloat /= 2 .and. mbod > 1 ) then` / `call msgerr (3, 'specification of labels for rigid bodies as input grid is required')` / `else if ( mbod == 1 ) then` / `ifloat = 2` / `else if ( mbod == 0 ) then` / `ifloat = min( 1, ifloat )` / `endif` / `!` / `! in case of moving object, set compressibility factor to zero` / `!` / `if ( ifldyn(18) /= 0 .or. ifloat == 2 ) pship(1) = 0.` | C 문서 누락 | 부체 분기는 IMPL을 요구하고 ALPHA의 [0,1]·THETA의 [0.5,1] 범위를 검사한다. 정확히 0.5인 THETA는 0.51로 바꾼다. `if ( ifldyn(18) /= 0 .or. ifloat == 2 ) pship(1) = 0.`이다. C는 문서에 있는 IMPL 요구를 제외한 보정·강제 대입 조건에 한정한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| guide-syntax-build:SG1-897 | 부체 적분 계수·coupling 보정 | swashuse PDF p.71–72는 CH·HHT·WBZ 선택과 rho 범위를 설명한다. 범위 밖 값의 대체와 고정 부체의 coupling 보정은 명시하지 않는다. | `src/SwashCheckPrep.ftn90:1378–1392` `if ( mfoti == 1 ) then` / `if ( pship(3) < 0. .or. pship(3) > 0.5 ) then` / `call msgerr (1, 'incorrect beta for the Newmark scheme')` / `pship(3) = 0.25` / `endif` / `if ( pship(4) < 0. .or. pship(4) > 1. ) then` / `call msgerr (1, 'incorrect gamma for the Newmark scheme')` / `pship(4) = 0.5` / `endif` / `else if ( mfoti > 1 ) then` / `rhoinf = pship(5)` / `if ( rhoinf < 0. .or. rhoinf > 1. ) then` / `call msgerr (1, 'incorrect spectral radius for the generalized-alpha method')` / `rhoinf = 1.` / `endif`; `src/SwashCheckPrep.ftn90:1406–1429` `alfam = (2.*rhoinf-1.) / (1.+rhoinf)` / `alfaf = rhoinf / (1.+rhoinf)` / `!` / `else if ( mfoti == 3 ) then` / `!` / `! Hilber-Hughes-Taylor scheme` / `!` / `alfam = 0.` / `alfaf = (1.-rhoinf) / (1.+rhoinf)` / `!` / `else if ( mfoti == 4 ) then` / `!` / `! Wood-Bossak-Zienkiewicz scheme` / `!` / `alfam = (rhoinf-1.) / (1.+rhoinf)` / `alfaf = 0.` / `!` / `endif` / `!` / `if ( mfoti > 1 ) then` / `!` / `fac      = 1. - alfam + alfaf` / `pship(3) = 0.25 * fac * fac` / `pship(4) = fac - 0.5`; `src/SwashCheckPrep.ftn90:1435–1451` `if ( ifloat == 2 ) then` / `if ( pship(10) < 0. .or. pship(10) > 1. ) then` / `call msgerr (1, 'incorrect under-relaxation value for FSI coupling')` / `pship(10) = 0.3` / `endif` / `else` / `! no iteration process required!` / `pship(8) = 0.` / `pship(9) = 1.` / `endif` / `!` / `! check implicitness factor for kinematic boundary conditions` / `!` / `if ( ifloat == 2 ) then` / `if ( pship(11) < 0. .or. pship(11) > 1. ) then` / `call msgerr (1, 'incorrect theta value for update kinematic boundary conditions')` / `pship(11) = 0.5` | C 문서 누락 | rho는 [0,1]에서 검사한다. CH·HHT·WBZ의 alfam·alfaf와 beta·gamma 대입은 해당 적분법의 내부 표현이다. C는 수학적 변환 자체가 아니라 범위 밖 입력의 대체 및 `ifloat == 2`가 아닌 분기에서 `pship(8) = 0.`과 `pship(9) = 1.`로 coupling을 보정하는 처리에 한정한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| inputs-setup:SI1-361 | FLOAT `theta=0.5`·Crank–Nicolson | swashuse PDF p.69 “[theta] = 0.5 corresponds to the Crank−Nicolson scheme” | `src/SwashCheckPrep.ftn90:1129` `if ( .not. pship(2) /= 0.5 ) pship(2) = 0.51` | C | 코드는 정확히 0.5인 값을 조용히 0.51로 바꾼다. 사용자 입력 0.5가 실제 계산에서도 유지된다고 쓰면 안 된다. 의도적인 보정 줄이 있으므로 결함 후보 대신 문서 누락으로 판정한다. |
| inputs-setup:SI1-532 | 수위·흘수·LABEL의 공간 바깥 값 | swashuse PDF p.22의 외부장 목록은 DRAFT·LABEL의 규칙을 적지 않는다. | `src/SwashCheckPrep.ftn90:2480` `draft = SVALQI (xp, yp, 18, flobj, NEAREST)`; `src/SwashCheckPrep.ftn90:2492` `labl = SVALQI (xp, yp, 19, lbod, 0.)`; `src/SwashFloatObjects.ftn90:320` `lfbs = int(lbodf)` | C | DRAFT는 최근접 값을 쓴다. LABEL은 격자 밖 0을 쓴다. LABEL을 공간 보간한 실수에서 int로 절단해 강체 번호로 만든다. 반올림과 다르다. |
| inputs-setup:SI1-561 | FLOAT·BODY 별칭·DOF ALL | swashuse PDF p.69–72 문법에 없다. | `src/SwashReadInput.ftn90:981` `if ( KEYWIS ('SHIP') .or. KEYWIS ('VESS') .or. KEYWIS ('WEC') .or. KEYWIS ('FLOAT') .or. KEYWIS ('BODY') .or. KEYWIS ('PONT') .or. KEYWIS ('PFLOW') ) then`; `src/SwashReadInput.ftn90:984` `if ( KEYWIS('METH') .or. KEYWIS('SOLV') ) then`; `src/SwashReadInput.ftn90:1088` `if ( KEYWIS ('ALL') ) bodtmp%dof(1:6) = .true.` | C | 동일 부유체 명령 분기로 일곱 이름을 받는다. METH도 SOLVER를 선택한다. DOF ALL은 여섯 자유도를 모두 켠다. |
| inputs-setup:SI1-562 | 부유체 반음해·움직이는 흘수·보간 방식 | swashuse PDF p.69–70은 입력 파일 필요 조건을 적는다. | `src/SwashCheckPrep.ftn90:1117` `if ( mtimei /= 2 ) call msgerr (3, 'semi-implicit time integration is required in case of floating object or pressurized flow')`; `src/SwashCheckPrep.ftn90:1143` `if ( ifldyn(18) /= 0 .or. ifloat == 2 ) pship(1) = 0.`; `src/SwashCheckPrep.ftn90:1147` `if ( ifloat /= 0 ) dpsopt = 4`<br>swashuse PDF p.100은 부유체의 가압 흐름에 반음해 적분이 필요하다고 명시한다. | C | 부유체·가압 흐름의 반음해 적분 조건은 swashuse PDF p.100에 있다. C는 동적 DRAFT·이동 강체에서 alpha를 0으로 바꾸는 조건과 부유체의 수심 보간을 `dpsopt=4`로 바꾸는 세부 처리에 한정한다. [10-15 결론 검증 정정] [10-15 전수 검증 정정] |
| inputs-setup:SI1-563 | 강체 수·단일 LABEL 생략·1D 자유도 | swashuse PDF p.70은 LABEL의 다중 강체 조건을 적는다. 1D 자유도 보정을 적지 않는다. | `src/SwashCheckPrep.ftn90:1135–1138` `else if ( mbod == 1 ) then`<br>`ifloat = 2`<br>`else if ( mbod == 0 ) then`<br>`ifloat = min( 1, ifloat )`; `src/SwashCheckPrep.ftn90:1904–1906` `bdof(:,2,1) = .false.`<br>`bdof(:,1,2) = .false.`<br>`bdof(:,3,2) = .false.` | C | 강체 자료가 없으면 이동 모드를 고정 모드 이하로 낮춘다. 1D에서는 SWAY·ROLL·YAW를 끈다. SURGE·HEAVE·PITCH만 남는다. |
| inputs-setup:SI1-564 | BODY 번호·질량·관성모멘트 유효성의 입력 검사 부재 | swashuse PDF p.70은 LABEL 정합성을 요구한다. 양수 검사와 자동 번호 재배열을 설명하지 않는다. | `src/SwashReadInput.ftn90:1054–1056` `call ININTG ('L'   , labl, 'REQ', 0 )`<br>`call INREAL ('MASS', mass, 'REQ', 0.)`<br>`call INREAL ('IX'  , moix, 'REQ', 0.)`; `src/SwashCheckPrep.ftn90:1867–1871` `m = currib%label`<br>`bmass(m) = currib%parm(1)`<br>`do j = 1, ndim`<br>`bmoi(m,j) = currib%parm(j+1)`<br>`bcog(m,j) = currib%parm(j+4)`; `src/SwashMotionRigidBod.ftn90:135` `f0 = ( thyd0(m,n) + tbod0(m,n) ) / bmoi(m,n)` | C | l을 배열 첨자로 직접 쓴다. DIMENSION은 입력값을 읽지만 1..mbod 검사·중복 번호 검사·질량과 관성모멘트 양수 검사를 하지 않는다. 사용자가 번호·질량·활성 회전 관성을 유효하게 준비해야 한다. |
| inputs-setup:SI1-565 | MLINE·FENDER 계수 읽기와 PRET의 수평 예외 | swashuse PDF p.70–71은 계수 단위·PRET 여부만 적는다. | `src/SwashReadInput.ftn90:1106–1108` `112         call INREAL ('K', bk, 'REP', -1.)`<br>`if ( bk /= -1. ) then`<br>`call INREAL ('B'   , bb, 'REQ', 0.)`; `src/SwashFloatObjects.ftn90:472–476` `if ( gamma /= 0. ) then`<br>`bmli(m,n,10) = fac / sin(gamma)`<br>`else`<br>`! horizintal line? no pretension`<br>`bmli(m,n,10) = 0.` | C | `K=−1`은 반복 종료 sentinel이다. 수치 읽기 자체는 그 밖의 음수 K·B를 양수로 고치지 않는다. 수평 계류선은 PRET가 있어도 예장력을 0으로 둔다. |
| inputs-setup:SI1-566 | generalized-alpha 계수 대입 | swashuse PDF p.71–72은 방법 이름·rho 범위·성질을 적는다. 계수식을 인쇄하지 않는다. | `src/SwashCheckPrep.ftn90:1406–1407` `alfam = (2.*rhoinf-1.) / (1.+rhoinf)`<br>`alfaf = rhoinf / (1.+rhoinf)`; `src/SwashCheckPrep.ftn90:1413–1414` `alfam = 0.`<br>`alfaf = (1.-rhoinf) / (1.+rhoinf)`; `src/SwashCheckPrep.ftn90:1420–1421` `alfam = (rhoinf-1.) / (1.+rhoinf)`<br>`alfaf = 0.`; `src/SwashCheckPrep.ftn90:1427–1429` `fac      = 1. - alfam + alfaf`<br>`pship(3) = 0.25 * fac * fac`<br>`pship(4) = fac - 0.5` | C | CH·HHT·WBZ가 각각 alfam·alfaf를 계산한다. 이어서 beta·gamma를 rho에서 다시 정한다. NEWMARK 사용자값 유지와 구분한다. 이 C 판정은 설명서의 계수식 누락과 코드의 대입식을 구분한 것이다. [10-15 결론 검증 정정] |
| inputs-setup:SI1-569 | 가속도 완화·Newmark 갱신 | swashuse PDF p.72는 under-relaxation만 적는다. 갱신식을 인쇄하지 않는다. | `src/SwashMotionRigidBod.ftn90:109` `afot1(m,n) = ( -alfam * afot0(m,n) + alfaf * f0 + (1.-alfaf) * f1 ) / (1.-alfam)`; `src/SwashMotionRigidBod.ftn90:113` `afot1(m,n) = alfa * afot1(m,n) + (1.-alfa) * accu`; `src/SwashMotionRigidBod.ftn90:117` `vfot1(m,n) = vfot0(m,n) + dt * ( gamma * afot1(m,n) + (1.-gamma) * afot0(m,n) )`; `src/SwashMotionRigidBod.ftn90:119` `xfot1(m,n) = xfot0(m,n) + dt * ( vfot0(m,n) + dt * ( beta * afot1(m,n) + (0.5-beta) * afot0(m,n) ) )` | C | 각 자유도의 가속도를 완화한다. 완화한 가속도로 속도·변위를 갱신한다. 회전도 같은 형식으로 토크/관성모멘트에서 갱신한다. |
| inputs-setup:SI1-570 | KBC 기본값·범위 보정의 문서 범위 경계 | swashuse PDF p.71 문법에는 KBC가 있다. 상세 설명은 swashuse PDF p.73으로 이어진다. | `src/SwashInit.ftn90:355` `pship(11) = 0.5`; `src/SwashCheckPrep.ftn90:1449–1451` `if ( pship(11) < 0. .or. pship(11) > 1. ) then`<br>`call msgerr (1, 'incorrect theta value for update kinematic boundary conditions')`<br>`pship(11) = 0.5`; `src/SwashUpdKBCrigb.ftn90:116` `vrb = theta * vfot1(l,1) + (1.-theta) * vfot0(l,1)`<br>swashuse PDF p.73은 KBC theta의 `0 ≤ [theta] ≤ 1`과 기본값 0.5 및 이전·현재 속도의 가중 의미를 설명한다. | C | KBC의 기본값·범위·가중 의미는 swashuse PDF p.73과 코드가 일치한다. C는 이동 강체에서 범위 밖 theta를 경고 후 0.5로 되돌리는 처리에 한정한다. [10-15 결론 검증 정정] [10-15 전수 검증 정정] |
| outputs:SO1-287 | 여러 부유체의 열 수 | swashuse PDF p.117–118의 부유체 출력 변수 정의는 부유체별 열 수를 적지 않는다. | `src/SwashDecOutQ.ftn90:205–206` `nvoqp = nvoqp + mbod` / `ovsvty(ivtype) = ovsvty(ivtype) + mbod`; `src/SwashFlobjOutp.ftn90:88` `nflob = mbod` | C 문서 누락 | 이동 부유체가 여러 개이면 하중·변위·PTO를 부유체 수만큼의 열로 쓴다. [10-15 전수 검증 정정] |
