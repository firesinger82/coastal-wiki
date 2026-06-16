---
title: "SWASH 경계조건 + 파 생성 forcing — BounCond dispatch · bound/Stokes/short wave · 스펙트럼 · internal wavegen · sponge"
model: SWASH
component: src (boundary / wave forcing)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashBounCond.ftn90 의 btype 매핑·blayk·istok/ibound·키워드 dispatch(:876-1004), SwashBCboundwave.ftn90 전문(Hasselmann 1962 상호작용 계수), SwashBCStokeswave.ftn90 전문(1~4 layer 1·2차 Stokes), SwashBCshortwave.ftn90 전문(evanescent 필터·Ursell·주기성 보정), SwashBCspectrum.ftn90 전문(JONSWAP·single-summation·Miles 1989), SwashIntWavgen.ftn90 전문(source function·shape factor), SwashReadBndval.ftn90 전문(시계열 파일 시간보간), SwashSpongeLayer.ftn90/SwashUSpongLayer.ftn90 전문(Mayer 1998 Eqs 43-44). BC 물리 루틴 호출부는 SwashUpdateUData.ftn90:497-509·:785-829·:1177 인용. piwg 정의는 SwashModule1.ftn90:305·526 인용."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/SWASH/source-analysis/swash-architecture-source-map.md
  - models/SWASH/README.md
---

# SWASH 경계조건 + 파 생성 forcing

> 개방경계 타입 dispatch + 입사파 합성(short/Stokes/bound long wave) + 파라메트릭 스펙트럼 + 내부 wavemaker + sponge 흡수경계. (경로: raw/source_code/swash/src/)

배정 9개 파일은 두 단계로 나뉜다. **(A) 설정·합성 단계** — `SwashBounCond`가 경계 키워드를 파싱해 타입(`btype`)·수직분포(`blayk`)·차수(`istok`)를 결정하고, 입사 Fourier 성분을 만든 뒤 `SwashBCspectrum`/`SwashBCStokeswave`/`SwashBCshortwave`/`SwashBCboundwave`/`SwashIntWavgen`가 성분별 진폭·위상·파수를 산출. **(B) 적용 단계** — 시간루프에서 `SwashUpdateUData`/`SwashUpdateData`가 합성 성분을 실제 속도/수위 경계값으로 부과(Riemann·weakly-reflective 포함). sponge 두 루틴은 흡수경계 감쇠계수를 사전계산.

## 1. SwashBounCond — 경계 타입/조건 dispatch

`SwashBounCond ( xcgrid, ycgrid, kgrpnt )` (`SwashBounCond.ftn90:1`). Purpose: *"Specifies boundary locations and conditions"* (`:40`). 1985줄 거대 루틴 — 좌표/측면 선택, 키워드 파싱, Fourier 성분 생성을 담당.

### 1.1 경계 타입 코드(btype)

명령 구문은 헤더 주석에 verbatim (`:328`):
```
BTYPe WLEV|VEL|VX|VY|DISCH|RIEMann|LRIEman|WEAKrefl|SOMMerfeld|OUTFlow
```
키워드 → `btype` 매핑 (`:876-904`):

| 키워드 | btype | 의미 (선언부 주석 `:82-91`) |
|---|---|---|
| `WLEV` | 2 | water level opening |
| `VEL`/`VX`/`VY` | 3 | velocity opening |
| `DISCH` | 5 | discharge opening |
| `RIEM` | 6 | Riemann invariant opening |
| `LRIE` | 6 + `lriem=.true.` | 선형화 Riemann (`:890-892`) |
| `WEAK` | 7 | weakly reflective opening |
| `SOMM`/`RADI` | 8 | Sommerfeld radiation |
| `OUTF` | 10 | outflow condition |

키워드 미지정 시 기본 `btype=3` (velocity) (`:902-904`). 2D에서 파(regular/bichromatic/spectrum)를 부과할 때는 법선+접선 성분 모두 기술하기 위해 `btype = -btype`으로 부호 반전 (예 `:1103`, `:1164`, `:1237`). `btype<0` 의미는 선언부 주석 *"< 0; =-btype, where both normal and tangential components are described"* (`:91`).

### 1.2 수직분포(blayk)

`LAY n` / `HYP` / `LOG` 파싱 (`:908-930`). 코드 의미(`:75-79`):
- `blayk = -2`: 연직 로그분포 (`LOG`, `:926`; depth-averaged kmax=1에서는 금지 `:922-924`)
- `blayk = -1`: hyperbolic cosine / Stokes 분포 (`HYP`, `:920`)
- `blayk = 0`: 연직 균일 (`:929`)
- `blayk > 0`: 적용 layer 번호

타입-분포 조합 제약은 `msgerr(3,...)`로 강제 (`:932-934`): 예) hyperbolic cosine는 `btype` 3 또는 7만 허용.

### 1.3 차수(istok)와 bound wave 옵션(ibound)

`ADDBound`/`ADDIG` 키워드 (`:955-965`):

| 키워드 | istok | ibound | 의미 |
|---|---|---|---|
| `ADDB` | 2 | 0 | 2차 bound (super-harmonic) 추가 |
| `ADDIG` | 1 | 1 | bound infragravity(long) wave 추가 |
| (없음) | 1 | 0 | 1차 free wave만 |

`blayk == -1`(hyperbolic cosine)이면 `istok = 0`으로 강제(Airy hyperbolic cosine 분포 사용, `:966`). `istok` 의미는 선언부 주석 (`:100-104`): 0=Airy hyperbolic cosine, 1=1차 Stokes(Airy), 2=2차 Stokes, 3=2차 sub/super-harmonic 전달함수. 다중 주파수 스펙트럼에서는 `istok==2 → 3`으로 승격 (`:1035`, `:1171`, `:1244`).

bound wave는 `btype` 3/7, `blayk` -1/0 조합에서만 허용 — 그 외엔 경고 후 `istok=1, ibound=0`으로 복귀 (`:968-979`).

### 1.4 wavemaker 종류(bcimp)

선언부 주석(`:67-74`): `bcimp` = 1 Fourier / 2 regular / 3 bichromatic / 4 parametric spectrum / 5 time series / 6 spectrum from file / 7 SWAN file. `UNIForm`/`VARiable` 하위에서 `FOUR`/`REGU`/`BICH`/`SPECT`/`SPECF`/`SPECS` 키워드로 분기 (구문 `:336-349`, dispatch `:991`, `:1161`, `:1234`, `:1347`, `:1422-1437`).

### 1.5 layer 인코딩(bgp(8))

istok를 blayk에 합성 인코딩: `blayk == -1`일 때 istok 0/1/2/3 → blayk `-1/-11/-21/-31`로 변환해 `bgptmp%bgp(8)`에 저장 (`:1390-1401`). 적용 단계에서 이 인코딩을 역으로 디코드해 사용.

## 2. SwashBCshortwave — 1차 free short wave 합성

`SwashBCshortwave ( bcfour, nfreq, xp, yp, ibgrpt, swd, wdir, rsgn, vdir, shape )` (`SwashBCshortwave.ftn90:1`). Purpose: *"Computes first order free short wave components for synthesizing time series along open boundaries"* (`:40`).

주파수 루프(`:128-224`)당 처리:

1. **방향 부호 s** — 입사방향과 정렬해 경계 대칭 유지. `vdir`(u/v) 와 `sin/cos(wdir-alpc)` 부호로 결정 (`:111-123`).
2. **evanescent mode 필터** — `numdisp`(수치 분산관계 사용) 시 cut-off 주파수 $\omega_{cf} = 0.9 \cdot 2\,k_{max}\sqrt{g/d}$ 초과 성분의 진폭을 0으로 (`:106`, `:138-146`).
3. **파수** — `disprel(swd,omega,kwav,...)`로 분산관계 해 (`:150`); `kwave(ibgrpt,j)`에 저장.
4. **TMA 보정** — `shape==3`(TMA)이면 천수 진폭 보정 $a \leftarrow a\,\omega^2/(g k\sqrt{2n})$ (`:156`).
5. **Ursell 수** — Beji(1995) 변형 $Ur = a\,k/\tanh^3(kd)$ (`:165`); 최대값 추적해 >0.2면 경고(선형이론·2차 bound wave 무효, `:228-236`).
6. **주기성 보정** — `bcperx`/`bcpery`일 때 파수가 $2\pi/L$의 정수배가 되도록 방향 보정 (`:172-196`).
7. **입사각 제약** — 경계 법선 기준 ±80° 밖이면 `cycle`로 건너뜀 (`cos/sin(theta) < 0.174`, `:198-213`).
8. **위상 시프트 + 성분 저장** — $\phi \mathrel{+}= k(\cos(\theta+\alpha_c)x_p + \sin(\theta+\alpha_c)y_p)$ (`:217`), 직교 성분 `comp1 = a\cos\phi`, `comp2 = a\sin\phi` 저장 (`:221-222`).

필터된 evanescent 비율 ≥10%면 cut-off Hz와 함께 경고 (`:240-251`).

## 3. SwashBCStokeswave — 1·2차 Stokes 성분 (연직 layer별)

`SwashBCStokeswave ( bcfour, nfreq, ibgrpt, swd, istok )` (`SwashBCStokeswave.ftn90:1`). Purpose: *"Computes first and second order Stokes wave components for synthesizing time series along open boundaries"* (`:40`). 저자 Panagiotis Vasarmidis, 2023 추가 (`:32-36`).

핵심: `kmax`(연직 layer 수)별로 다른 다항식 계수를 사용해 비정수압 다층 모델에 맞는 표면·속도 1·2차 성분을 산출. `kmax == 1,2,3,4` 분기 (`:101`, `:166`, `:245`, `:334`). spectrum 판정: `istok==3 .and. nfreq>2`이면 spectrum=true → 2차 성분에서 $2\omega > \omega_{nfreq}$ 시 중단 (`:93-97`, `:138`).

각 분기 구조(예 kmax=1, `:101-164`):
- 위상 cosine/sine을 `comp1/comp2`(short wave 단계에서 저장)에서 추출: `cph = comp1/ampl`, `sph = comp2/ampl` (`:112-113`).
- **1차 표면**: `stkz1c = a·cph`, `stkz1s = a·sph` (`:117-118`).
- **1차 속도**: $fac = 2 a g / \sqrt{(4+k^2d^2)\,g\,d}$ (`:122`), `stku1c/s` 저장.
- **2차**(`istok>1`): `c2ph=2cph²-1`, `s2ph=2·sph·cph` (`:145-146`); 표면 `stkz2c/s` (`:150-153`), 속도 `stku2c/s` (`:157-160`).

kmax=2/3/4는 동일 패턴이나 비정수압 layer 수에 맞춘 고차 유리식 계수(`dn` 분모, 다항식 분자). kmax=3·4의 2차 속도 계수는 $10^{14}\sim10^{20}$ 규모 정수 계수의 14~24차 $kd$ 다항식 (`:306-328`, `:400-427`) — 연직 모드별 분산관계 정합 계수로 추정. ⚠ 미확인: 이 다항식 계수의 출처 문헌은 헤더에 명시 없음(source-needed).

## 4. SwashBCboundwave — 2차 bound long wave (Hasselmann 1962)

`SwashBCboundwave ( bcfour, nfreq, xp, yp, ibgrpt, swd, wdir, rsgn, vdir, shape )` (`SwashBCboundwave.ftn90:1`). Purpose: *"Computes second order bound long wave to be added to Fourier series along open boundaries"* (`:40`). Method: Hasselmann (1962) J. Fluid Mech. 12, 481-500의 상호작용 계수 (`:44-48`). 저자 Dirk Rijnsdorp.

이중 주파수 루프(`floop` j, `sloop` k=j+1..nfreq, `:148-359`)로 차주파수 $f_3 = f_2 - f_1$ 성분을 합성:

- 1차 성분 파수 `disprel` (`:164`), TMA 보정 (`:168`).
- 유효 깊이 범위 `khmin=0.4 < kd < khmax=10` + 진폭≠0 게이트 (`:83-84`, `:215`, `:284`).
- bound wave 방향 `theta3 = alpc + atan(...)` (`:292`), 파수 $k_3 = \sqrt{k_1^2+k_2^2+2k_1k_2\cos\Delta\theta}$ (`:300`), 군속도 $c_{g3} = 2\pi f_3/k_3$ (`:304`).
- 위상 $\phi_3 = \phi_1-\phi_2+\pi + k_3(\cos\theta_3 x_p + \sin\theta_3 y_p)$ (`:308-312`).
- **상호작용 계수** $D_p$ — Hasselmann Eq.(4.3) (`:320`); $T_1$ — 2차 potential 시간미분, Eq.(4.7)+(1.26) (`:325`); $T_2$ — Eq.(4.4) (`:330`); $D_z = T_1+T_2$ — Eq.(4.2) (`:334`).
- 진폭 $a_3 = |D_z|\,a_1 a_2$ (`:338`), 주파수 bin `l = nint(f3/df)` (`:340`).
- **저장**: 표면 `zetab(ibgrpt,l) += a3·exp(iφ3)`, 질량flux `fluxbu/fluxbv` (1D/optg=5는 fluxbu만, 2D는 cosθ3/sinθ3 분해) (`:344-351`).

## 5. SwashBCspectrum — 파라메트릭 스펙트럼 → Fourier 성분

`SwashBCspectrum ( bcfour, spparm )` (`SwashBCspectrum.ftn90:1`). Purpose: *"Computes Fourier components based on energy density spectrum..."* (`:40`). Method: 다방향장은 성분별 단일 방향 가정, Miles(1989) single-summation으로 방향분포 cdf에서 무작위 추출 (`:44-50`).

흐름:

1. **shape/period** — `spshape(2)` 부호로 shape(1=PM,2=JONSWAP,3=TMA)·peak/mean 판정 (`:132-138`). Hs: `spshape(1)`로 rms($\sqrt2\,\cdot$)/significant 구분 (`:144-148`).
2. **주파수 격자** — cyclic 주기 `tcycl`(미지정 시 `tfinc-tinic+dt`)에서 `df=1/tcycl` (`:152-160`); Nyquist `fnyq=0.5/dt`; 범위 `fmin=(nfp/2)df`, `fmax=min(fnyq,3fp)` (`:162-179`).
3. **에너지 스펙트럼** — `call jonswap(spec,fmin,df,nfreq,fp,gamma)` (`:184`). m0 계산 (`:192`).
4. **mean period 반복** — peak 미지정 시 m1로 평균주기 산출, 수렴(eps=0.01)까지 최대 10회 반복으로 tp 보정 (`:196-222`).
5. **정규화** — `fac = Hs²/16/m0`로 스펙트럼 스케일 (`:232-233`).
6. **Fourier 성분** — `ampl = sqrt(2·df·spec(j))`, `omega = 2πf`, 위상은 MASTER 노드 난수(seedf) 후 `SWBROADC`로 전 노드 배포 (`:243-272`). 초기 theta=0.
7. **방향분포** — `spparm(4)≠0`이면 cos-power 모델: 방향폭→ms 변환(`:286-298`), spreading에 따라 sector 결정(`:302-310`), 51개 방향의 cdf 구성 후 난수(seedt)로 각 주파수에 보간 방향 할당 (`:314-353`).

## 6. SwashIntWavgen — 내부 wavemaker (source function)

`SwashIntWavgen ( igser, nfreq, wdir, shape )` (`SwashIntWavgen.ftn90:1`). Purpose: *"Computes the source function amplitude and shape factor of source area"* (`:40`). 저자 Vasarmidis, 2019 (`:32-36`).

내부 파 생성은 도메인 내부 source line/area에 source 항을 더해 양방향 전파파를 생성하는 방식. 파라미터는 `piwg` 배열(`SwashModule1.ftn90:305 miwg=10`, `:526`).

주파수 루프(`:117-243`):
- swd = `piwg(3)` (`:101`); evanescent cut-off·필터 동일(`:106`, `:126-134`).
- 파수 `disprel`, `kwave(j,1)` 저장 (`:138-140`); TMA 보정·Ursell(`:144-156`); 주기성 보정(`:160-182`).
- **shape factor β** — $\beta = 80 / (piwg(4))^2 / (2\pi/k)^2$ (source area 폭 piwg(4) 기반, `:186`).
- **energy velocity cen** — `kpmax`(=비정수압 layer 차수)별 다항식 (`:193-215`): kpmax=1 $c_{en}=8\sqrt{gd}/(4+k^2d^2)^{1.5}$; kpmax 2/3는 고차 유리식; 그 외 분기는 $(0.5 + kd/\sinh 2kd)(\omega/k)$ (연속 분산관계 군속도).
- **shape factor I** — optg≠5(structured)에서 source 라인 방향(`lsrcfx`/`lsrcfy`)별 가우시안 (`:219-235`); optg=5(unstructured)는 단순 가우시안 (`:233`).
- **source amplitude** — `igser%sfamp(j) = 2·ampl·cen/ishap` (`:241`), β·theta 저장 (`:239-240`).

호출은 `SwashUpdateUData.ftn90:1177` (`tsmo=piwg(5)`, `:1162`).

## 7. SwashReadBndval — 시계열 경계값 파일 읽기 + 시간보간

`SwashReadBndval ( bfiled, bctime, bcloc, bndval )` (`SwashReadBndval.ftn90:1`). Purpose: *"Reads boundary values from boundary file(s) and store them"* (`:40`).

- `binfo` = 0 시계열 / 1 1D 스펙트럼 / 2 2D 스펙트럼 (`:61-64`). 구현된 읽기는 `binfo==0` 시계열만 (`:146-165`).
- 메인 루프 `bcloop` (`:102`): `timco > timf2`(현재시각이 마지막 읽은 값 초과)이면 새 값 read. 직전 값을 time level 1로 이동 후(`:108-115`) 헤딩라인·각 경계점 데이터 읽기.
- 시간코딩 `iiopt==0`은 `read(timf2,bval)`, 그 외엔 `DTRETI`로 날짜 디코드 (`:148-159`).
- 파일 소진 시 다음 파일(filename list) open 또는 종료 — `bfiled(1)=-1` 설정, `timf2=999999999` (`:177-216`).
- **시간보간**: `wf1 = (timf2-timco)/(timf2-timf1)`, `wf2=1-wf1`; **보간값은 반드시 `bndval(:,1)`에 저장** (`:222-237`, 주석 `:233`).

## 8. SwashSpongeLayer — sponge 흡수경계 감쇠계수 (structured)

`SwashSpongeLayer ( sponxl, sponxr, sponyb, sponyt )` (`SwashSpongeLayer.ftn90:1`). Purpose: *"Determines damping function for flow variables due to sponge layers"* (`:40`). Method: Mayer, Garapon & Sorensen (1998) IJNMF 28, 293-315의 Eqs (43)-(44) (`:44-48`).

핵심 감쇠식 (성장률 `grt=0.5`, `:68`):
$$\gamma(\xi) = grt\cdot\xi^3 + (1-grt)\cdot\xi^6$$
여기서 $\xi$는 정규화 거리(경계에서 1, 안쪽으로 0). 4면(좌/우/하/상) 폭 `spwidl/spwidr/spwidb/spwidt`별로 별도 처리.

- **1D 좌측** (`:96-129`): 시작점 `isl = 1 + nint(spwidl/dx)`, u-point 루프, `xl = dist/spwidl` (경계로 갈수록 1), `sponxl(indx) = grt·xl³ + (1-grt)·xl⁶`. 우측 대칭(`:131-162`).
- **2D**: u-point 루프에서 누적 거리 `dist`로 `xl = 1 - dist/spwidl` 계산(`:180`), 동일 다항식. 구면좌표(`kspher>0`)는 위도 cosine·`lendeg`로 거리 보정 (`:194-206`).
- **상하 sponge** (`spwidb/spwidt`)는 v-point 루프로 동일 (`:260-352`).

## 9. SwashUSpongLayer — sponge (unstructured mesh)

`SwashUSpongLayer` (`SwashUSpongLayer.ftn90:1`). Purpose: 동일하되 *"...on unstructured mesh"* (`:40`). 동일 Mayer(1998) Eqs 43-44 (`:44-48`), 동일 `grt=0.5` (`:64`).

- sponge layer `i=1..nspl` 별 boundary marker `vm`·폭 `width` (`:106-109`).
- **face 루프**: 각 face 중심에서 같은 marker의 경계 face까지 최단거리 `dmin` 탐색 (`:111-143`), `dnb = 1 - dmin/width`, `sponu(iface,i)%gamma = grt·dnb³ + (1-grt)·dnb⁶`, 가장 가까운 boundary face 저장 (`:145-161`).
- **cell 루프**: cell 중심 기준 동일 처리 — boundary cell 두 경계 정점 marker 확인 후 `spons(icell,i)%gamma` 저장 (`:165-228`).

## 10. 적용 단계 — 합성 성분이 경계값으로 부과되는 곳

(이 절은 배정외 파일 `SwashUpdateUData.ftn90` 인용; 합성→적용 연결 맥락)

시간루프에서 `rsgn = sign(1.,-fac)` (좌/하 경계 inflow +1, 우/상 outflow -1, `SwashUpdateUData.ftn90:331`). `it==0`(첫 진입)에서 성분 합성 루틴 호출 (`:497-509`): BCshortwave → BCboundwave(ibnd==1) → BCStokeswave(istok≠0) → BCtransferfnc(istok==3).

**Riemann 부과** (`btype==6`, `:785-799`):
- 선형화(`lriem`): $u_1 = bval - rsgn\sqrt{g/d}\,\zeta_0$ (`:793`)
- 완전: $u_1 = bval - 2\,rsgn\sqrt{g\,h_u}$ (`:797`)

**Weakly reflective** (`btype==7`, `:801-829`): 연직분포(klay=-2 로그 / -1 hyperbolic cosine)별로 입사+반사 분리해 명시적 부과. 로그분포는 $z_0$ 거칠기 길이 기반 적분(`:809-822`).

## 11. 파일 간 정합·요약

| 파일 | 역할 | 핵심 출력 | 출처식 |
|---|---|---|---|
| SwashBounCond | 키워드 dispatch·btype/blayk/istok 결정·Fourier 성분 생성 | bgp(), curbfs | (자체) |
| SwashBCshortwave | 1차 free wave | comp1/comp2, kwave | Beji 1995(Ursell) |
| SwashBCStokeswave | 1·2차 Stokes (layer별) | stkz/stku 1·2 c/s | ⚠ 계수 출처 미명시 |
| SwashBCboundwave | 2차 bound long wave | zetab, fluxbu/v | Hasselmann 1962 |
| SwashBCspectrum | 파라메트릭 스펙트럼 합성 | bcfour ampl/omega/phase/theta | JONSWAP, Miles 1989 |
| SwashIntWavgen | 내부 wavemaker source | sfamp, bshap | (자체, kpmax별) |
| SwashReadBndval | 시계열 파일 읽기·시간보간 | bndval(:,1) | (자체) |
| SwashSpongeLayer | sponge (structured) | sponxl/r/b/t | Mayer 1998 (43,44) |
| SwashUSpongLayer | sponge (unstructured) | sponu/spons %gamma | Mayer 1998 (43,44) |

**공통 패턴 확인됨**: (1) evanescent cut-off $\omega_{cf}=0.9\cdot2k_{max}\sqrt{g/d}$ — BCshortwave(`:106`)·IntWavgen(`:106`) 동일. (2) Ursell >0.2 경고 — 둘 다 동일(`BCshortwave:228`, `IntWavgen:247`). (3) 주기성 방향보정 로직 — BCboundwave/BCshortwave/IntWavgen 동일 구조. (4) sponge 다항식 $grt\,\xi^3+(1-grt)\xi^6$ — 두 sponge 루틴 동일.

**미확인(source-needed)**: BCStokeswave의 kmax=2,3,4 고차 다항식 계수 출처 문헌(헤더 미명시); SwashReadBndval의 1D/2D 스펙트럼(`binfo`=1/2) 읽기는 이 루틴에 미구현(다른 경로 추정).
