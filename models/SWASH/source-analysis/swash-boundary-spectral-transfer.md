---
title: "SWASH 스펙트럼 경계 + 2차 transfer function — SwashBCspecfile / SwashBCtransferfnc"
model: SWASH
component: src (boundary / spectral synthesis)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashBCspecfile.ftn90 전문(1-932) read — SPEC1D/SWAN 파일 파서, 방향분포 합성, Fourier 성분 저장, nesting 좌표 매칭. SwashBCtransferfnc.ftn90 핵심부(1-668) + 28개 contained function 구조(grep) read — 2차 sub/super-harmonic transfer function 합성 메인 루프 + 대표 함수(etasub1·velsb11) 식 인용. 호출처 SwashUpdateUData/Data·SwashBounCond grep 확인. 2026-10-15 SWASH recovery 대조 보고서 반영" # [10-15 전수 검증 정정]
last_source_check: "2026-10-15 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/SWASH/source-analysis/swash-architecture-source-map.md
  - models/SWASH/README.md
---

# SWASH 스펙트럼 경계 + 2차 transfer function

> 스펙트럼 경계파일(SPEC1D / SWAN 연계)을 읽어 random-phase Fourier 성분으로 합성하고(`SwashBCspecfile`), 1차 파성분 쌍의 2차 sub-/super-harmonic 결합파(bound wave)를 transfer function으로 합성한다(`SwashBCtransferfnc`). 경로: raw/source_code/swash/src/

---

## 1. 두 파일의 역할 분담

| 파일 | 라인수 | Purpose (verbatim) | 호출처 |
|---|---|---|---|
| `SwashBCspecfile.ftn90` | 932 | "Reads 1D or 2D spectrum from file, and makes it appropriate for synthesizing time series along open boundaries" (`SwashBCspecfile.ftn90:40`) | `SwashBounCond.ftn90:1368,1833,1957` |
| `SwashBCtransferfnc.ftn90` | 4709 | "Computes second order sub- and super-harmonic transfer functions of surface elevation and horizontal layer-averaged velocities" (`SwashBCtransferfnc.ftn90:42-43`) | `SwashUpdate{U}Data.ftn90:509/870/754/1546` |

`SwashBCspecfile`은 **1차 파성분(amplitude·omega·phase·theta) 생성** 단계, `SwashBCtransferfnc`는 그 1차 성분으로부터 **2차 bound-wave 보정** 단계로, 시간적으로 분리된 두 워크플로다.

---

## 2. SwashBCspecfile — 스펙트럼 파일 파싱

진입점 `SwashBCspecfile.ftn90:1` 인자: `filenm`(파일명), `nbps`(경계점 수), `bpix/bpiy`(경계점 인덱스), `tcycl`(cyclic period), `lnest`(SWAN nesting 여부), `btype`(경계 유형), `blayk`(레이어 지정 방식), `tsmo`(cold-start smoothing 기간) — `SwashBCspecfile.ftn90:56-74`.

파일은 `FOR`로 열고(`:184`), 첫 헤더 라인으로 두 포맷을 분기한다(`:189-190`):

- `EQCSTR(hedlin,'SPEC1D')` → 2-컬럼(주파수, variance density) 단순 1D 파일 (`:190-280`)
- `EQCSTR(hedlin,'SWAN')` → SWAN 스펙트럼 파일 (`:281-911`)
- 그 외 → `msgerr(3,'unsupported boundary data file')` (`:910`)

### 2.1 SPEC1D 경로 (`:190-280`)

각 (`f`, `spec`) 줄을 읽어 음수 밀도면 에러(`:204-207`), Fourier 성분 linked list에 누적: 진폭 `tmpf%ampl = sqrt(2.*spec)`, 각주파수 `tmpf%omega = 2.*pi*f` (`:211-212`). 주파수 간격 `df`는 첫 두 줄에서 추출(`:208`).

**cyclic period override**: 사용자가 `tcycl`을 줬어도 1D 파일에서는 `1/df`로 강제하고 경고(`:222-225`). nesting(`SPECSWAN`)에서는 SPEC1D 부적합 에러(`:194`).

Fourier 성분 최종 저장(`:236-269`): 진폭에 `sqrt(df)` 곱해 스펙트럼 밀도→진폭 변환(`bfstmp%ampl(j) = currf%ampl * sqrt(df)`, `:260`), 위상은 random(`bfstmp%phase(j) = 2.*pi*tarr(j)`, `:262`), `theta(j)=0`(방향확산 없음, `:263`). `azero=-1.e10`, 입사각 `spparm(3)=-999.`("indicent angle is assumed to be normal on the boundary", `:233-234`).

### 2.2 SWAN 스펙트럼 파일 경로 (`:281-911`)

SWAN ASCII 스펙트럼 포맷을 단계별로 파싱:

| 블록 | 라인 | 동작 |
|---|---|---|
| `TIME` 헤더 | `:289-297` | nonstationary 스펙트럼 금지 에러 (`:290`) |
| `LOC`/`LONLAT` | `:302-335` | 경계 위치 좌표 read(`REFIXY`, `:318`); Cartesian/spherical 불일치 검사(`:303-305`) |
| `FREQ` | `:341-356` | Hz→rad/s 변환 `bspfrq(j)=2.*pi*f` (`:347`); `msc<3`이면 에러(`:355`) |
| `DIR` | `:358-399` | degree→rad(`:365`); Nautical일 때 `180+dnorth-dir`(`:364`); 방향 오름/내림차순 자동 감지(`dorder`, `:367-386`) |
| `QUANT` | `:403-462` | 양 종류 식별: ENDENS/VADENS(`switch(1)`), NDIR/CDIR(`switch(2)`), DSPR/POWER(`switch(3)`) |

**density 정규화 factor `bfac`** (`:493-500`):
- Jacobian `1/(2pi)`: $E(f)\,[\text{Hz}] \to E(\omega)\,[\text{rad/s}]$ (`:493-494`)
- 2D면 `* 180/pi` (radian 방향 보정, `:497`)
- ENDENS(에너지밀도)면 `/(rhow*grav)` (`:500`)

**균일 주파수 격자 재구성** (`:465-484`): `df = 2*pi/tcycl`(tcycl 지정 시) 또는 파일의 `bspfrq(2)-bspfrq(1)`(`:467-471`); `[fmin,fmax]`에 `nfreq = nint((fmax-fmin)/df)+1`개 균일 분포(`:475-484`).

#### 1D SWAN 입력의 방향분포 합성 (`:538-643`)

파일이 방향성 없는 1D면(`mdc==0`), peak 주파수의 방향/스프레드에서 cos-power 분포를 인공 생성:

- 방향 스프레드(degr)→cos power: $m_s = \max(\text{fac}\cdot\text{dwidth}^{-2}-2,\,1)$, fac는 dd>23/17 구간별 1.2/1.096/1.01 (`:578-591`)
- $m_s$ 크기로 방향 sector 결정: $m_s\le6\Rightarrow\pi$, $\le30\Rightarrow0.5\pi$, $\le100\Rightarrow0.25\pi$, else $0.125\pi$ (`:600-608`)
- 정규화계수 cnorm: $m_s>10$이면 $\sqrt{m_s/2\pi}(1+0.25/m_s)$, 아니면 감마함수 비 $\Gamma(0.5m_s+1)/(\sqrt{\pi}\,\Gamma(0.5m_s+0.5))$ (`:620-624`)
- 2D 밀도: `bspden(i,j) = edir * spec1(j)`, `edir = cnorm * max(cos^ms, 1e-10)` (`:629-639`)

#### 2D SWAN 입력 (`:645-677`)

`bspden`을 방향순서(`dorder`)에 맞춰 직접 read(`:649-653`), exception value는 0 처리(`:664-668`). peak 방향 검색 후 방향축을 peak 기준 상대화: `bspdir = bspdir - thp` (`:671-675`).

#### 변수밀도 → Fourier 성분 (random direction sampling) (`:679-790`)

핵심 합성 알고리즘:

1. **균일 주파수 격자로 보간** (에너지 보존): `CHGBAS(bspfrq, freq, ..., spec1, spec2, msc, nfreq, ...)` → `varden(i,j)` (`:681-695`)
2. **유의파고**: `hs = 4.*sqrt(sum(varden)*df*ddir)` (`:699`)
3. **방향 CDF 구성**: `ddstr = sum(varden,dim=2)`; `cdf(i)=sum(ddstr(1:i))` 정규화(`:705-709`)
4. **random phase**: seed `seedf`, `phase(j)=2.*pi*tarr(j)` (`:735-747`)
5. **random direction**: 별도 seed `seedt`로 CDF에서 random 추첨 → 각 주파수에 방향 보간 할당, 해당 variance density로 진폭 `ampl = sqrt(2.*rval2*df*ddir)` (`:753-783`)
6. **진폭 스펙트럼 wave-height 보정**: `bfstmp%ampl = hs * bfstmp%ampl / (4.*sqrt(m0))` — m0는 합성된 $\sum 0.5a^2$ (`:782-786`)

각 주파수가 **단일 random 방향**을 갖는 것이 특징(directional spread를 ensemble of single-direction component로 표현). MPI에서는 MASTER가 random 생성 후 `SWBROADC`로 전파(`:735-742,753-760`).

### 2.3 nesting 시 경계점 좌표 매칭 (`:804-887`)

`lnest`(SPECSWAN)일 때, 연속한 두 SWAN 위치 (x1,y1)→(x2,y2) 선분 위에 놓인 계산격자 경계점을 찾아 보간 가중치를 부여:

- 선분에 대한 상대 수직거리 `rdist = abs(rx*(yp-y1) - ry*(xp-x1))`, `rdist<0.1`이면 선분 위로 간주(`:833-836`)
- 선분 방향 투영비는 `fac = rx*(xp-x1)+ry*(yp-y1)`이다. (`src/SwashBCspecfile.ftn90:838-841`). [10-15 대조 정정]
  fac는 −0.001 초과·1.001 미만이어야 한다. (`src/SwashBCspecfile.ftn90:841` `if ( fac > -0.001 .and. fac < 1.001 ) then`). [10-15 대조 정정]
  `fac<0.01`이면 0으로 만든다. (`src/SwashBCspecfile.ftn90:845` `if ( fac < 0.01 ) fac = 0.`). [10-15 대조 정정]
  `fac>0.99`이면 1로 만든다. (`src/SwashBCspecfile.ftn90:846` `if ( fac > 0.99 ) fac = 1.`). [10-15 대조 정정]
- 경계점 데이터 `bgptmp%bgp(1..9)` 저장: 격자주소, btype, `nint(1000*fac)`/`nint(1000*(1-fac))` 두 인접 위치 가중치, nbv2/nbv1 두 variance set index, smoothing `nint(100000*tsmo)`, blayk, ibound (`:848-861`)

→ 한 계산 경계점이 인접한 두 SWAN 스펙트럼 위치를 선형보간하도록 설정.

---

## 3. SwashBCtransferfnc — 2차 결합파 transfer function

Authors: Panagiotis Vasarmidis (`SwashBCtransferfnc.ftn90:32-33`). Method 인용: "Details on the computation of interaction coefficients of two primary wave components can be found in P. Vasarmidis et al, *A study of the non-linear properties and wave generation of the multi-layer non-hydrostatic wave model SWASH*, Ocean Engineering, 2024" (`:47-51`).

진입점 인자(`:1,63-82`): `bcfour`(1차 Fourier 성분 리스트), `nfreq`, `(xp,yp)`(격자점 좌표), `ibgrpt`(경계점 인덱스), `swd`(still water depth), `wdir`(입사/peak 방향), `rsgn`(±1: 좌하 inflow / 우상 outflow), `vdir`(u/v 속도 방향 플래그), `shape`(스펙트럼 형상 1=PM/2=Jonswap/3=TMA).

호출 조건: 호출처에서 `istok == 3 .and. it == 0` (2차 Stokes/bound-wave 모드, 초기 셋업 시점) — `SwashUpdateUData.ftn90:509`.

### 3.1 메인 이중 루프 — 성분쌍 상호작용

`floop`(j=1..nfreq, `:151`) × `sloop`(k=j+1..nfreq, `:218`): **방향·상대수심 범위·비영 진폭 조건을 통과한 서로 다른 두 1차 성분 (ampl1,omega1,theta1)·(ampl2,omega2,theta2)의 쌍**에 대해 결합파 계산(`SwashBCtransferfnc.ftn90:204-218,271-283`).

각 성분의 파수는 `disprel(swd, omega, kwav, rval, n)` 분산관계로 산출(`:163,230`). `n`은 group/phase 속도비. `kd = kwav*swd`(무차원 수심, `:165,232`).

**필터링**:
- 방향은 입사방향과 정합되게 부호 `s` 부여(symmetry 보존, `:130-145`)
- 무차원 수심 게이트 `kd1>khmin(0.2) .and. kd1<khmax(5.)` (`:86-87,216,283`) — 매우 얕거나 깊은 성분 제외
- 경계 법선 대비 ±80° 이내만 채택 (`cos/sin(theta) ` 임계 0.174, `:199-214,266-281`)

**주기경계 보정**(`bcperx`/`bcpery`): 파수의 경계방향 성분이 `2pi/length`의 정수배가 되도록 방향 양자화(`:173-197,240-264`).

### 3.2 sub-harmonic (차주파수) 결합파 (`:285-350`)

```
omega3 = omega2 - omega1                                   (:287)
```
조건: `nfreq==2 .or. .not. omega3 < odmin(0.02)` — 너무 작은 차주파수 제외(10.05 버그픽스, `:38,289`). 주파수 index `l = nint(omega3/dw)` (`:293`).

결합파 파수(코사인 법칙):
$$k_3 = \sqrt{k_1^2 + k_2^2 - 2k_1 k_2 \cos(\theta_1-\theta_2)}$$
(`:297`, double precision로 계산). 방향 `theta3 = alpc + atan(...)` (`:301`), 위상 `phase3 = phase2 - phase1 + k_3(\cos\theta_3 x_p + \sin\theta_3 y_p)` (`:305-309`).

### 3.3 super-harmonic (합주파수) 결합파 (`:352-417`)

```
omega3 = omega1 + omega2                                   (:354)
```
조건 `.not. omega3 > wn`(최고 주파수 초과 제외, `:356`). index `l = nint((omega3-2.*w0)/dw)` (`:360`). 파수는 `+` 부호 코사인 법칙(`:364`), 위상 `phase3 = phase1 + phase2 + ...` (`:372-376`).

### 3.4 레이어 수별 transfer function 디스패치 (`:313-331,380-398`)

`kmax`(연직 레이어 수, 1~4)에 따라 contained function 선택:

| kmax | eta(표면) | vel(레이어별) |
|---|---|---|
| 1 | etasub1/etasup1 | velsb11/velsp11 |
| 2 | etasub2/etasup2 | velsb12,velsb22 / velsp12,velsp22 |
| 3 | etasub3/etasup3 | velsb13,velsb23,velsb33 / velsp.. |
| 4 | etasub4/etasup4 | velsb14..velsb44 (4개) / velsp.. |

내부 함수는 총 28개다 (`src/SwashBCtransferfnc.ftn90:429–4707`의 `real function` 선언). 수면 전달함수 `eta{sub,sup}{1-4}`는 8개다. 속도 전달함수 `vel{sb,sp}{I}{J}`는 20개다. `I`는 층 번호다. `J`는 전체 층 수 `kmax`다 (`src/SwashBCtransferfnc.ftn90:313–330,380–397`의 호출 대입). 층 번호 1은 맨 위층이다 (`src/SwashExpLayUflow.ftn90:1060–1068`). [10-15 전수 검증 정정]

각 함수는 `kd1,kd2,omega1,omega2,swd,grav`만으로 구성된 **순수 대수식**(분산관계 기반 닫힌 형식). 대표 예 etasub1 (`:499-504`):
$$\eta_{\text{sub}}^{(1)} = \frac{(kd_1-kd_2)^2\big[4g\,kd_1kd_2 + (\ldots)h\big]}{2\,kd_1kd_2\,h\big[-4g(kd_1-kd_2)^2 + (4+(kd_1-kd_2)^2)(\omega_1-\omega_2)^2 h\big]}$$
(분자 중간항 verbatim `:500-502`, $h$=swd). velsb11 동일 구조의 속도 transfer (`:657-663`). 모든 함수의 Note: "transfer function needs to be multiplied with a1 * a2" (`:483,562,641`).

### 3.5 결합파 누적 저장 (`:333-348,400-415`)

가중치 `rval = ampl1 * ampl2` (`:335,402`)를 곱해 전역 코사인/사인 성분 배열에 **누적**:

- 표면: `subzc(ibgrpt,l) += eta*rval*cos(phase3)`, `subzs += eta*rval*sin(phase3)` (`:337-338`); super는 `supzc/supzs` (`:404-405`)
- 속도: 1D 또는 `optg==5`(unstructured)면 `subuc(ibgrpt,l,:) += vel(:)*rval*cos(phase3)` (방향 분해 없음, `:340-342`); 2D 구조격자면 `cos/sin(theta3)`로 u/v 분해해 `subuc/subus/subvc/subvs`에 저장(`:343-348`).

`(ibgrpt, l, layer)` 인덱싱 — 경계점·결합파 주파수index·연직레이어별. 여러 성분쌍이 같은 `l`로 매핑되면 합산되어 결합파 스펙트럼을 누적 구성.

---

## 4. 데이터 흐름 종합

```
[스펙트럼 파일]                          [2차 보정]
SwashBCspecfile                          SwashBCtransferfnc
  파싱 → 균일 격자 보간(CHGBAS)            성분쌍 (j,k) 루프
  random phase + random direction         disprel → kwav,kd
  진폭 = sqrt(2·varden·df·ddir)           kd 게이트 + 방향 ±80° 필터
  Hs 보정                                  sub: ω2-ω1 / super: ω1+ω2
  → bfsdat(ampl,omega,phase,theta)        etaXXX/velXXX (kmax별 대수식)
        │                                  × ampl1·ampl2
        └──────── bcfour ────────────────► sub/sup{z,u,v}{c,s}(ibgrpt,l,:) 누적
```

`SwashBCspecfile`이 만든 1차 `bfsdat` 리스트가 `SwashBCtransferfnc`의 `bcfour` 입력으로 흘러, 1차 random-phase 성분 위에 2차 bound-wave가 얹힌다.

---

## 5. 배열 선언과 원문 연결 [10-15 전수 검증 정정]

- `subuc`·`supuc`는 경계점×주파수×층 배열이다. (`src/SwashModule2.ftn90:384–385`; `src/SwashCheckPrep.ftn90:1689–1690` `if ( .not.allocated(subuc) ) allocate(subuc(nbgrpt,nfreq,kmax))`·`if ( .not.allocated(supuc) ) allocate(supuc(nbgrpt,nfreq,kmax))`). [10-15 대조 정정]
- `subzc`·`supzc`는 경계점×주파수 배열이다. (`src/SwashModule2.ftn90:392–393`; `src/SwashCheckPrep.ftn90:1699–1700` `if ( .not.allocated(subzc) ) allocate(subzc(nbgrpt,nfreq))`·`if ( .not.allocated(supzc) ) allocate(supzc(nbgrpt,nfreq))`). [10-15 대조 정정]
- 이 배열의 선언 모듈은 `SwashModule2.ftn90`의 `m_bndspec`이다. ([inputs-setup:SI1-713](../../../_staging/recovery/compare/swash-inputs-setup-vs-code.md#4-노트-대조와-수정안)). [10-15 대조 정정]
- 상호작용 계수의 계산 방법은 코드의 Method 주석이 Vasarmidis et al. (2024) 논문으로 안내한다 (`src/SwashBCtransferfnc.ftn90:47–51`). 이 노트의 대표 식은 `etasub1`과 `velsb11`이다 (`src/SwashBCtransferfnc.ftn90:499–504,657–663`). [10-15 전수 검증 정정]
- `CHGBAS`는 `src/swanser.ftn:3331`에 정의되어 있다. `disprel`은 `src/SwashServices.ftn90:13`에 정의되어 있다. `GAMMAF`는 `src/swanser.ftn:3892`에 정의되어 있다. `REFIXY`는 `src/swanser.ftn:174`에 정의되어 있다. [10-15 전수 검증 정정]
- `seedf`·`seedt`는 `SwashModule2.ftn90`의 `m_bndspec` 모듈에 선언한다. (`src/SwashModule2.ftn90:368–369`). [10-15 대조 정정]
- `seedf`는 위상 난수용이다. (`src/SwashModule2.ftn90:368` `integer   , dimension(:)    , save, allocatable :: seedf  ! seed used to generate pseudorandom phases`). [10-15 대조 정정]
- `seedt`는 파향 난수용이다. (`src/SwashModule2.ftn90:369` `integer   , dimension(:)    , save, allocatable :: seedt  ! seed used to generate pseudorandom spectral directions`). [10-15 대조 정정]

## 문서와 코드 차이 (10-15 대조)

결론과 원문 인용은 [inputs-setup](../../../_staging/recovery/compare/swash-inputs-setup-vs-code.md#5-차이-결론)의 최종본에서 옮겼다.
swashuse의 인쇄 쪽은 PDF 쪽에서 8을 뺀 값이다.

문서 판: SWASH 12.01 매뉴얼 swashuse·swashtech(공개 저장소 `7949227`, 2026-05-06, "release v12.01"에서 마지막 변경). 코드 판: VERNUM 12.01(공개 저장소 main `a486d5f`, 2026-05-26, 12.01 뒤 `608ffd7`·`9554c98` 포함).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| inputs-setup:SI1-319 | SPECFILE cycle의 SPEC1D 예외 | `swashuse PDF p.63` “[cycle] the cyclic period ...”; `swashuse PDF p.57`의 `SPECFile ’fname’ [cycle]` | `src/SwashBCspecfile.ftn90:222–224` `if ( tcycl < 9.e9 ) then`<br>`write (msgstr,'(a,f9.2,a)') 'user-defined cyclic period is ignored. Instead, a cyclic period of ',1./df,' sec will be used.'`<br>`call msgerr (1, trim(msgstr) )` | C 문서 누락 | SPEC1D에서는 사용자가 준 cycle을 무시한다. 실제 주기는 `1/df`이다. SWAN 파일의 cycle 처리와 구분해야 한다. [10-15 전수 검증 보완] |
| inputs-setup:SI1-324 | SPECSWAN 1D-MODE 금지 | `swashuse PDF p.64` “CANNOT BE USED IN 1D-MODE.” | `src/SwashBCspecfile.ftn90:398` `if ( oned .and. mdc /= 0 ) call msgerr (3, 'directional wave spectrum not allowed in 1D mode')`; `src/SwashBCspecfile.ftn90:719–722` `if ( .not.oned ) then`<br>`bfstmp%spparm(3) = thp`<br>`else`<br>`bfstmp%spparm(3) = -999.` | B 문서 오기 | 코드의 1D 거부 조건은 방향 스펙트럼 `mdc≠0`이다. 비방향 SWAN 스펙트럼의 1D 처리 경로가 있다. SPECSWAN·lnest 전체를 1D에서 차단하는 검사는 없다. git 이력: `8756667:src/SwashBCspecfile.ftn90:381` `if ( oned .and. mdc /= 0 ) call msgerr (3, 'directional wave spectrum not allowed in 1D mode')`. 최초 공개판도 1D의 방향 스펙트럼만 거부한다. 비방향 스펙트럼의 1D 경로가 뒤에 새로 추가된 이력은 없다. SPECSWAN의 1D 거부 조건은 방향 성분 mdc가 0이 아닌 경우다. ([AD 판정표](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)) [10-15 결론 검증 정정] [10-15 git 이력 판정] |
| inputs-setup:SI1-507 | 난수 seedf·seedt의 일회 초기화 | `swashuse PDF p.34` seed는 공통 정수값만 적는다. | `src/SwashBounCond.ftn90:235` `if ( lseed ) then`; `src/SwashBounCond.ftn90:236` `if ( myseed < 1000 ) myseed = 1000*myseed`; `src/SwashBounCond.ftn90:241–244` `seedf(i) = abs(myseed) +    i - 1`<br>`seedt(i) = abs(myseed) + 2*(i - 1)`<br>`enddo`<br>`lseed = .false.`; `src/SwashReadInput.ftn90:2625–2634`는 SOURCE 입력에서도 같은 초기화 조건·정수열·표지 해제를 사용한다. | C 문서 누락 | 처음 경계·소스가 seed를 초기화한다. 위상 난수와 파향 난수에 다른 정수열을 넣는다. 그 뒤 SET SEED를 바꾸는 것만으로 이미 만든 seedf·seedt를 다시 만들지 않는다. git 이력: `7949227:src/SwashBounCond.ftn90:237` `if ( lseed ) then`. H1·H2·H6·H7은 시드 초기화 표지를 공용 모듈로 옮긴다. H8은 SOURCE가 먼저 나오는 경우도 초기화한다. 문서는 초기화 순서를 설명하지 않는다. 이전 동작을 적은 문장과의 충돌이 아니므로 C를 유지한다. HEAD는 BOUND 또는 SOURCE 중 먼저 읽은 경로에서 시드 배열을 한 번 초기화한다. 문서는 이 호출 순서와 두 정수열을 설명하지 않는다. ([AD 판정표](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)) [10-15 결론 검증 보완] [10-15 git 이력 판정] [10-15 전수 검증 보완] |
| inputs-setup:SI1-547 | SPEC1D Δf·음수 밀도·random phase | `swashuse PDF p.62–63`은 두 열과 예제만 적는다. | `src/SwashBCspecfile.ftn90:204–208` `if ( spec < 0. ) then`<br>`call msgerr (3, 'error in reading 1D spectrum file: density is negative')`<br>`exit`<br>`endif`<br>`if ( nfreq < 2 ) df = f - df`; `src/SwashBCspecfile.ftn90:262–263` `bfstmp%phase(j) = 2.*pi*tarr(j)`<br>`bfstmp%theta(j) = 0.            ! no directional spreading` | C 문서 누락 | Δf는 처음 두 주파수의 차이이다. 모든 후속 간격의 균일성을 검사하지 않는다. 음수 밀도는 오류이다. 위상은 난수이고 방향 분산은 0이다. |
| inputs-setup:SI1-548 | nesting 허용 거리·투영·가중치 반올림 | `swashuse PDF p.63`은 좌표 보간을 설명한다. 임계값을 적지 않는다. | `src/SwashBCspecfile.ftn90:833` `rdist = abs( rx*(yp-y1) - ry*(xp-x1) )`; `src/SwashBCspecfile.ftn90:836` `if ( rdist < 0.1 ) then`; `src/SwashBCspecfile.ftn90:841` `if ( fac > -0.001 .and. fac < 1.001 ) then`; `src/SwashBCspecfile.ftn90:845–846` `if ( fac < 0.01 ) fac = 0.`<br>`if ( fac > 0.99 ) fac = 1.`; `src/SwashBCspecfile.ftn90:855` `bgptmp%bgp(3) = nint(1000.*fac)` | C 문서 누락 | 위치 선분 길이 대비 거리 10% 미만을 허용한다. 투영 길이는 −0.001 초과·1.001 미만이다. 양 끝 1% 구간은 끝점으로 붙인다. 나머지 가중치는 0.001 단위이다. SEGMENT XY의 1% 검색과 다르다. |
| inputs-setup:SI1-714 | nesting 투영 끝점 | `models/SWASH/source-analysis/swash-boundary-spectral-transfer.md:100` “`[−0.001,1.001]` 범위면 채택” | `8756667:src/SwashBCspecfile.ftn90:792` `if ( fac > -0.001 .and. fac < 1.001 ) then` | B 문서 오기 | fac는 −0.001 초과·1.001 미만이어야 한다. `fac<0.01`이면 0으로 만든다. `fac>0.99`이면 1로 만든다. `rdist<0.1`의 10% 거리 조건을 유지한다. git 이력: `8756667:src/SwashBCspecfile.ftn90:792` `if ( fac > -0.001 .and. fac < 1.001 ) then`. fac의 열린 부등식은 최초 공개판부터 같다. 양 끝점을 포함한 이전 판은 없다. fac는 −0.001 초과·1.001 미만이어야 한다. `fac<0.01`이면 0으로 만든다. `fac>0.99`이면 1로 만든다. `rdist<0.1`의 10% 거리 조건을 유지한다. ([AD 판정표](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)) [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| inputs-setup:SI1-712 | 난수 seed 선언 확인 | `models/SWASH/source-analysis/swash-boundary-spectral-transfer.md:197` “SwashCommdata3/SwashCommdata4 추정이나 직접 미확인” | 코드에만(C). `src/SwashModule2.ftn90:368` `integer   , dimension(:)    , save, allocatable :: seedf  ! seed used to generate pseudorandom phases`; `src/SwashModule2.ftn90:369` `integer   , dimension(:)    , save, allocatable :: seedt  ! seed used to generate pseudorandom spectral directions`. | C 문서 누락 | seedf·seedt는 SwashModule2.ftn90의 m_bndspec 모듈에 선언한다. 두 배열은 위상·파향 난수용이다. git 이력: `7949227:src/SwashModule2.ftn90:366` `integer   , dimension(:)    , save, allocatable :: seedf  ! seed used to generate pseudorandom phases`. 두 배열 선언은 H7의 문맥 행이다. 이번 커밋은 배열의 선언 모듈을 바꾸지 않았다. seedf와 seedt는 7949227과 HEAD 모두 m_bndspec에 선언되어 있다. ([AD 판정표](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)) [10-15 결론 검증 보완] [10-15 git 이력 판정] [10-15 전수 검증 정정] |
| inputs-setup:SI1-713 | 전달함수 배열 차원 확인 | `models/SWASH/source-analysis/swash-boundary-spectral-transfer.md:194` “선언 모듈과 차원”의 “미확인 (source-needed)” | 코드에만(C). `src/SwashCheckPrep.ftn90:1689` `if ( .not.allocated(subuc) ) allocate(subuc(nbgrpt,nfreq,kmax))`; `src/SwashCheckPrep.ftn90:1699` `if ( .not.allocated(subzc) ) allocate(subzc(nbgrpt,nfreq))`.<br>`src/SwashModule2.ftn90:384–385`는 subuc·supuc를 dimension(:,:,:)로 선언한다. `src/SwashModule2.ftn90:392–393`은 subzc·supzc를 dimension(:,:)로 선언한다. `src/SwashCheckPrep.ftn90:1690` `if ( .not.allocated(supuc) ) allocate(supuc(nbgrpt,nfreq,kmax))`; `src/SwashCheckPrep.ftn90:1700` `if ( .not.allocated(supzc) ) allocate(supzc(nbgrpt,nfreq))`. | C 문서 누락 | subuc·supuc는 경계점×주파수×층 배열이다. subzc·supzc는 경계점×주파수 배열이다. Module2의 m_bndspec 선언과 준비 단계의 allocate에서 배열 차원이 일치한다. [10-15 결론 검증 보완] [10-15 전수 검증 정정] |
