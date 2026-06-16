---
title: "SWASH 스펙트럼 경계 + 2차 transfer function — SwashBCspecfile / SwashBCtransferfnc"
model: SWASH
component: src (boundary / spectral synthesis)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashBCspecfile.ftn90 전문(1-932) read — SPEC1D/SWAN 파일 파서, 방향분포 합성, Fourier 성분 저장, nesting 좌표 매칭. SwashBCtransferfnc.ftn90 핵심부(1-668) + 40개 contained function 구조(grep) read — 2차 sub/super-harmonic transfer function 합성 메인 루프 + 대표 함수(etasub1·velsb11) 식 인용. 호출처 SwashUpdateUData/Data·SwashBounCond grep 확인."
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
- 선분 방향 투영비 `fac = rx*(xp-x1)+ry*(yp-y1)`, `[−0.001,1.001]` 범위면 채택(`:838-841`)
- 경계점 데이터 `bgptmp%bgp(1..9)` 저장: 격자주소, btype, `nint(1000*fac)`/`nint(1000*(1-fac))` 두 인접 위치 가중치, nbv2/nbv1 두 variance set index, smoothing `nint(100000*tsmo)`, blayk, ibound (`:848-861`)

→ 한 계산 경계점이 인접한 두 SWAN 스펙트럼 위치를 선형보간하도록 설정.

---

## 3. SwashBCtransferfnc — 2차 결합파 transfer function

Authors: Panagiotis Vasarmidis (`SwashBCtransferfnc.ftn90:32-33`). Method 인용: "Details on the computation of interaction coefficients of two primary wave components can be found in P. Vasarmidis et al, *A study of the non-linear properties and wave generation of the multi-layer non-hydrostatic wave model SWASH*, Ocean Engineering, 2024" (`:47-51`).

진입점 인자(`:1,63-82`): `bcfour`(1차 Fourier 성분 리스트), `nfreq`, `(xp,yp)`(격자점 좌표), `ibgrpt`(경계점 인덱스), `swd`(still water depth), `wdir`(입사/peak 방향), `rsgn`(±1: 좌하 inflow / 우상 outflow), `vdir`(u/v 속도 방향 플래그), `shape`(스펙트럼 형상 1=PM/2=Jonswap/3=TMA).

호출 조건: 호출처에서 `istok == 3 .and. it == 0` (2차 Stokes/bound-wave 모드, 초기 셋업 시점) — `SwashUpdateUData.ftn90:509`.

### 3.1 메인 이중 루프 — 성분쌍 상호작용

`floop`(j=1..nfreq, `:151`) × `sloop`(k=j+1..nfreq, `:218`): **서로 다른 두 1차 성분 (ampl1,omega1,theta1)·(ampl2,omega2,theta2)의 모든 쌍**에 대해 결합파 계산.

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

전체 40개 contained function: `eta{sub,sup}{1-4}` 8개 + `vel{sb,sp}{layer-pair}{kmax}` 32개 (`:429-4707` grep 확인). `velsbIJ`의 두 번째 자리(J=kmax)·세번째(I=레이어) 인덱싱으로 kmax 레이어 시스템의 각 레이어 속도 transfer를 표현.

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

## 5. 미확인 / source-needed

- `subzc/subuc/supzc` 등 누적 배열의 **선언 모듈과 차원** — grep으로 `SwashCommdata3`/`m_bndspec`에서 직접 확인 못함(검색 무결과). 사용 패턴상 `(nbgrpt, nfreq?, kmax)` 추정이나 ⚠ 미확인 (source-needed).
- `etaXXX`/`velXXX` 대수식의 물리적 유도 — 코드는 닫힌 형식만 제공, 유도는 Vasarmidis et al. (2024) 논문 참조(`:47-51`). 식 자체는 etasub1/velsb11만 본문 인용, 나머지 38개는 동형 구조로 미전사(분량 비례 생략).
- `CHGBAS`·`disprel`·`GAMMAF`·`REFIXY` 구현 본체는 별도 파일 — 본 노트 범위 외(호출 인터페이스만 인용).
- `seedf`/`seedt` 정의 위치 — `SwashCommdata3`/`SwashCommdata4` 추정이나 직접 미확인 (source-needed).
