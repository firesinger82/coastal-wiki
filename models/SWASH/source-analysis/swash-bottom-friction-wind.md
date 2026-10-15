---
title: "SWASH 바닥마찰 + 바람응력 — SwashBotFrict/SwashWindStress (구조격자) & SwashUBotFrict/SwashUWindStress (비구조 mesh)"
model: SWASH
component: src (외력항: 바닥마찰·바람응력)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashBotFrict.ftn90(:39-52 헤더, :100-927 6 roughness 옵션 식), SwashWindStress.ftn90(:38-58 Charnock 헤더, :380-520 4 drag 옵션 식, :960-993 stress 적용), SwashUBotFrict.ftn90(:38-380 flexible mesh), SwashUWindStress.ftn90(:38-466 mesh wind) 를 file:line 인용. 2026-10-15 SWASH recovery 대조 보고서 반영"
last_source_check: "2026-10-15 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/SWASH/source-analysis/swash-architecture-source-map.md
  - models/SWASH/README.md
---

# SWASH 바닥마찰 + 바람응력

> 바닥마찰계수(6 방법)와 바람응력 drag(4 방법)의 SWASH 구현. 구조격자판(SwashBotFrict/SwashWindStress)과 flexible mesh판(SwashUBotFrict/SwashUWindStress) 2세트. (경로: raw/source_code/swash/src/)

## 1. 파일 구성과 역할

| 파일 | 격자 | 산출 변수 | 신설 |
|---|---|---|---|
| `SwashBotFrict.ftn90` | 구조격자 (oned + 2D) | `cfricu`, `cfricv` | 2010-01 (`SwashBotFrict.ftn90:36`) |
| `SwashUBotFrict.ftn90` | 비구조 삼각 mesh | `cfricu`(cell) | 2020-02 (`SwashUBotFrict.ftn90:36`) |
| `SwashWindStress.ftn90` | 구조격자 (oned + 2D) | `cwndu`/`cwndv` → `windu`/`windv` | 2010-03 (`SwashWindStress.ftn90:36`) |
| `SwashUWindStress.ftn90` | 비구조 삼각 mesh | `cwndu`(face) → `windu` | 2023-03 (`SwashUWindStress.ftn90:36`) |

네 파일 모두 저자 Marcel Zijlema (`SwashBotFrict.ftn90:32`, `SwashUBotFrict.ftn90:32`, `SwashWindStress.ftn90:32`, `SwashUWindStress.ftn90:32`).

`SwashBotFrict`는 깊이평균 속도 `u,v`를 인자로 받음 (`SwashBotFrict.ftn90:66-67`). `SwashUBotFrict`는 face 깊이평균 속도 `u`만 받음 (`SwashUBotFrict.ftn90:67`).

---

## 2. 바닥마찰 — 6 roughness 방법

Purpose/Method 헤더 verbatim (`SwashBotFrict.ftn90:39-52`):

```
!   Purpose
!   Calculates bottom friction coefficient
!   Method
!   Based on 6 roughness methods:
!   1) a dimensionless constant,
!   2) Chezy formulation,
!   3) Manning formulation,
!   4) Colebrook-White formulation,
!   5) Nikuradse roughness height (logarithmic velocity profile assumed), or
!   6) linear bottom friction
```

선택자는 `irough`. 마찰계수는 `varfr`(공간변동 마찰)이면 `fricf(nm,2)` 배열에서, 아니면 상수 `pbot(1)`(Nikuradse는 `pbot(2)`)에서 읽음 (예: `SwashBotFrict.ftn90:106,128`). 모든 식은 적셔진 셀(`wetu(nm)==1`)에만 적용 (`SwashBotFrict.ftn90:112`).

**입력 카드·기본값(2026-07-12 직독)**: `FRICtion` 카드가 `irough` 를 설정 — 키워드 생략 시 **MANNing 이 기본**(`irough=3`, cf=0.019). `CONstant`→1(cf=0.002), `CHEZy`→2(C=65), `MANNing`→3(n=0.019), `LOGlaw [SMOOTH|ROUGH [h] ]`→4(기본 SMOOTH, pbot(2)=0), `COLEbrook [h]`→5, `LINear [k]`→11 (`SwashReadInput.ftn90:777-806`). 카드 자체를 생략하면 바닥마찰 off(`irough` 초기 0 유지). [10-15 대조 정정]

옵션 1의 이차 마찰 계수는 무차원이다 (`src/SwashBotFrict.ftn90:47`; swashuse PDF p.76). [10-15 대조 정정]
옵션 11의 선형 마찰 계수는 m/s이다 (`src/SwashBotFrict.ftn90:104`; `src/SwashExpDep2DHflow.ftn90:869,905`). [10-15 대조 정정]

### 2.1 옵션별 식 (구조격자, file:line)

| `irough` | 방법 | 식 (constant 분기) | file:line |
|---|---|---|---|
| 1 또는 11 | 무차원 상수 / linear | $c_f = \text{pbot(1)}$ | `:128`, `:418` |
| 2 | Chezy | $c_f = g / C^2$ | `:162`, `:492` |
| 3 | Manning | $c_f = g\,n^2 / h^{1/3}$ | `:196`, `:566` |
| 4 | Nikuradse (조도지정) | $c_f = \big(\kappa / \ln(33\,h/(e\,k_s))\big)^2$ | `:275`, `:728` |
| 5 | Colebrook-White | $C = 18\log_{10}(\max(12h/k_s,\,1.0129))$, $c_f=g/C^2$ | `:351-352`, `:888-889` |

- **Chezy** (옵션 2): `cfricu(nm) = grav / ( pbot(1) * pbot(1) )` (`SwashBotFrict.ftn90:162`). pbot(1)=Chezy 계수 $C$.
- **Manning** (옵션 3): `cfricu(nm) = grav * pbot(1) * pbot(1) / hum(nm)**(1./3.)` (`SwashBotFrict.ftn90:196`). pbot(1)=Manning $n$, `hum`=u-point 수심. $h^{1/3}$ 지수가 1/3임에 주의 — Chezy $C = h^{1/6}/n$ 의 $c_f=g/C^2$ 변환과 일치.
- **Colebrook-White** (옵션 5): `cz = 18. * log10 ( max(12.*hum(nm) / pbot(1), cfix) )` then `cfricu(nm) = grav / cz**2` (`SwashBotFrict.ftn90:351-352`). pbot(1)=조도높이 $k_s$. `cfix=1.0129`(`:73`)는 log10 인자 하한 → $C\ge0.1$ 정도로 음수 Chezy 방지.

### 2.2 Nikuradse (옵션 4) — 로그 wall-law + Newton-Raphson

조도높이 $k_s$(`pbot(2)`)가 지정되면 닫힌식:
```
cfricu(nm) = ( vonkar / log( erough*hum(nm)/(exp(1.)*pbot(2)) ) )**2.
```
(`SwashBotFrict.ftn90:275`) — $c_f = (\kappa/\ln(33 h/(e\,k_s)))^2$. `erough=33.0`(`:75`, rough bed 경험상수), `vonkar`=폰카르만 상수.

$k_s=0$(매끈 바닥)이면 Reynolds수 기반 반복 (`SwashBotFrict.ftn90:279-314`):
```
r = abs(u(nm))*hum(nm)/(exp(1.)*kinvis)          ! Reynolds 수  (:279)
... if ( r > ev**2 ) then  ! ev=11.6 viscous sublayer edge (:77)
   Newton-Raphson:
   s = sold*(1.+log(esmoot*r/sold))/(1.+vonkar*sold)   ! esmoot=9.0 smooth 상수 (:298)
... cfricu(nm) = 1./(s*s)                          ! s = u/u*  (:314)
```
수렴 기준 `eps=0.01`(`:74`), 최대 `maxnit=100`(`:71`). 미수렴 시 `msgerr(1,...)` 경고 후 `s=sqrt(r)` (`SwashBotFrict.ftn90:300-303`).

### 2.3 1D vs 2D / u-v 분기

`oned`이면 u-point 1-루프만 (`SwashBotFrict.ftn90:100-365`). 2D는 u-point 루프(`nfu..nl × mf..ml`, `cfricu`) + v-point 루프(`mfu..ml × nf..nl`, `cfricv`)로 동일 식 반복 (예 Chezy: `:451-479` u, `:467-479` v). 2D 끝에서 반복격자 동기화:
```
call periodic ( cfricu, kgrpnt, 1, 1 )
call periodic ( cfricv, kgrpnt, 1, 1 )
```
(`SwashBotFrict.ftn90:924-925`).

미지원 `irough`은 `msgerr(4,'unknown roughness method...')` 후 return (`SwashBotFrict.ftn90:362`, `:917`).

### 2.4 Flexible mesh판 (SwashUBotFrict)

동일 6 방법(`SwashUBotFrict.ftn90:44-51`), 단 셀 중심에서 계산. `varfr`이면 3 꼭짓점 마찰의 산술평균:
```
cf = ( fricf(v(1),2) + fricf(v(2),2) + fricf(v(3),2) )/ 3.
```
(`SwashUBotFrict.ftn90:121` 등). 수심은 셀 수심 `hs(icell)` 사용 (Manning `:201`, Colebrook `:366`). Nikuradse는 먼저 `call perot ( u, 1, 1 )`로 cell-vector 복원 후 `utot = sqrt(uvc(icell,1,1)**2 + uvc(icell,1,2)**2)`로 속도 크기 (`SwashUBotFrict.ftn90:213,225,282`). 반복식·상수는 구조격자판과 동일 (`SwashUBotFrict.ftn90:254` vs `SwashBotFrict.ftn90:298`).

swashuse PDF p.38은 비구조 REPEATING을 금지한다 (`src/SwashCheckPrep.ftn90:206,210`; theory-unstructured:ST2-406). [10-15 대조 정정]

---

## 3. 바람응력 — 4 drag 방법 + Charnock

Method 헤더 verbatim (`SwashWindStress.ftn90:42-58`):

```
!   The so-called Charnock drag coefficient formulation is proposed by Charnock (1955).
!   He assumed a logarithmic wind velocity profile in the turbulent layer above the free surface:
!     w10(z)     1        z
!     ------ = ----- ln (---)
!       u*     kappa      z0
!   where u* is the friction velocity, kappa is the Von Karman constant, z is the vertical height
!   above the free surface and z0 is the roughness height:
!     z0 = b * u*^2/g
!   with b the dimensionless Charnock coefficient and g the gravity acceleration.
!   Since, Cd = u*^2/w10^2 we have an implicit relation between drag coefficient Cd and wind speed w10.
```

선택자는 `iwind`. drag는 무조건 상한 `cdcap`로 clip: `cd = min( cdcap, cd )` (예 `SwashWindStress.ftn90:385`).

### 3.1 공통 전처리

```
alpha  = pwnd(4)     ! 10m → 표면 보정계수  (:130)
wcrstp = pwnd(10)    ! crest 적용 비율      (:131)
wfac = rhoa / ( rhow * alpha * alpha )    ! 응력 배율  (:135)
wxc = u10 * cos(wdic) ;  wyc = u10 * sin(wdic)   ! 일정 바람 성분  (:139-140)
```
(`SwashWindStress.ftn90:130-140`). `rhoa`=공기밀도, `rhow`=물밀도.

`varwi`(공간변동 바람)이면 격자상 바람을 `wxf/wyf`에서 covariant 보간 (`SwashWindStress.ftn90:218`, 2D), 아니면 상수 `wxc/wyc` (`:236`). `lstag(5/6)`이면 staggered 입력 직접 사용 (`SwashWindStress.ftn90:193-205,247-259`).

### 3.2 drag 옵션별 식 (file:line)

| `iwind` | 방법 | 식 | file:line |
|---|---|---|---|
| 1 | 상수 drag | $C_d = \text{pwnd(1)}$ | `:384`, `:528` |
| 2 | Charnock | Newton-Raphson, $C_d=1/s^2$ | `:437`, `:657` |
| 3 | 풍속 선형 | $C_d=10^{-3}(\text{pwnd5}+\text{pwnd6}\,|\nabla\zeta|+\text{pwnd7}\,W)$ | `:478`, `:788` |
| 4 | 2차 다항 fit | $C_d=10^{-3}(p+q\,u_{tl}+r\,u_{tl}^2)$ | `:508`, `:887` |

- **옵션 3 선형** (`SwashWindStress.ftn90:478`):
  ```
  cd = 0.001*( pwnd(5) + pwnd(6)*abs(dsdx) + pwnd(7)*wspeed )
  ```
  `wspeed = max(pwnd(8), min(w10,pwnd(9)))` 로 [pwnd8,pwnd9] clamp (`:476`). 1D는 수면경사 `dsdx`, 2D는 경사 크기 `slope=sqrt(dsdx^2+dsdy^2)` 사용 (`SwashWindStress.ftn90:785,788`).
- **옵션 4 다항** (`SwashWindStress.ftn90:508`):
  ```
  utl = w10/uref                                  ! uref=31.5 (:79,506)
  cd = 0.001*( pp + qq*utl + rr*utl*utl )         ! pp=0.55 qq=2.97 rr=-1.49 (:76-78)
  ```

### 3.3 Charnock (옵션 2) — Newton-Raphson

암시적 Charnock 관계를 반복으로 푼다 (`SwashWindStress.ftn90:423-447`):
```
s    = 22.4 ; sold = 0.                          ! 초기값  (:427-428)
do
   if ( abs(sold-s) < (eps*s) ) exit             ! eps=0.01 (:75)
   sold = s
   s = sold*(log(pwnd(3)*grav*sold*sold / (max(0.001,pwnd(2)*w10*w10)))-2.) / (vonkar*sold-2.)   ! (:437)
enddo
cd = 1./(s*s)                                    ! s=w10/u* → Cd=u*^2/w10^2  (:447)
```
`pwnd(2)`는 무차원 Charnock beta이다 (`src/SwashReadInput.ftn90:840`). [10-15 대조 정정]
`pwnd(3)`는 풍속 측정 높이이다 (`src/SwashReadInput.ftn90:841`). [10-15 대조 정정]
미수렴 시 `s = 22.4`로 복귀한다 (`src/SwashWindStress.ftn90:439–442`). [10-15 대조 정정]

### 3.4 상대풍 (relwnd) — 흐름에 대한 상대 풍속

`relwnd`이면 풍속에서 표류 흐름을 빼서 상대풍 사용:
```
w10 = abs(alpha*windu(nm) - u0(nm,1))            ! 1D  (:393)
```
(`SwashWindStress.ftn90:393`). 2D는 성분별: `rwx = alpha*windu(nm) - u0(nm,1)`, `rwy = 0.25*alpha*(windv 4점) - 0.25*(v0 4점)` 후 `w10 = sqrt(rwx**2+rwy**2)` (`SwashWindStress.ftn90:551-561`). `relwnd`이 아니면 그냥 `abs(windu(nm))` (`:397`).

### 3.5 응력 적용

drag·풍속으로 stress coefficient 계산:
```
cwndu(nm) = wfac * cd * w10                       ! (:401 등)
```
이후 실제 stress 항으로 변환 (`SwashWindStress.ftn90:960-972`):
```
do i = 1, mcgrd
   windu(i) = alpha*cwndu(i)*windu(i)             ! (:962)
windv도 동일 (:970, 2D만)
```
영구 dry점은 `cwndu(1)=0.` (`SwashWindStress.ftn90:955-956`). 2D 끝 반복격자 동기화 `periodic(cwndu/cwndv,...)` (`SwashWindStress.ftn90:948-949`).

### 3.6 파봉 한정 적용 (relwav)

`relwav`이면 (1) 파봉 추종으로 wind을 wave celerity만큼 보정 (`SwashWindStress.ftn90:166-187,301-367`), (2) 파봉 근처에만 응력 적용 (`SwashWindStress.ftn90:978-993`):
```
if ( s0(i) > smax(i) ) smax(i) = s0(i)
if ( s0(i) < (1.-wcrstp) * smax(i) ) then
   windu(i) = 0. ;  windv(i) = 0. (2D)
```
즉 수면이 국지 최대(`smax`)의 `(1-wcrstp)` 미만으로 떨어진 곳(파곡)은 응력 0. wave celerity 보정은 `wcel = min( abs(dsdt)/fac, sqrt(grav*hum) )`로 천수 속도 상한 (`SwashWindStress.ftn90:180,326`).

swashuse PDF p.75는 crest배를 임계값으로 설명한다 (inputs-physics-numerics:SI2-030). [10-15 대조 정정]
구조격자와 비구조격자 코드는 1−crest배를 사용한다 (`src/SwashWindStress.ftn90:984`; `src/SwashUWindStress.ftn90:458`). [10-15 대조 정정]
이 차이는 E 중간의 코드 결함 후보이다 (inputs-physics-numerics:SI2-030; theory-framework:ST1-294; theory-unstructured:ST2-371). [10-15 대조 정정]
`smax`는 매 파의 높이가 아니라 0에서 시작한 누적 최대 수위이다 (`src/SwashCheckPrep.ftn90:3110`; `src/SwashWindStress.ftn90:982`). [10-15 대조 정정]
해석: `relwnd`가 참인 1DH의 연속시간 형태는 `\tau/\rho_w=(\rho_a/\rho_w)C_d\alpha^{-2}\vert \alpha U-u\vert (\alpha U-u)`이다 (`src/SwashWindStress.ftn90:135,391–401,962`; inputs-physics-numerics:SI2-038). [10-15 대조 정정] [10-15 전수 검증 정정]
코드는 유속 부분을 시간 적분의 분모로 옮긴다 (`src/SwashExpDep1DHflow.ftn90:465–473,721`; inputs-physics-numerics:SI2-038). [10-15 대조 정정] [10-15 전수 검증 보완]

### 3.7 Flexible mesh판 (SwashUWindStress)

동일 4 drag 방법·동일 상수(`pp/qq/rr=0.55/2.97/-1.49`, `uref=31.5`, `SwashUWindStress.ftn90:78-81`)·동일 Charnock 반복식 (`SwashUWindStress.ftn90:312` = `SwashWindStress.ftn90:437`). 차이점:
- face 법선/접선으로 분해: `windu(iface)=nx*ux+ny*uy`(법선풍), `wndimp(iface)`에 접선풍 임시저장 (`SwashUWindStress.ftn90:160-164`).
- `call perot ( u0, 1, 1 )`로 cell 속도벡터 복원 후 상대풍 계산 (`SwashUWindStress.ftn90:217,244`).
- 내부 wet face만 처리: `face(iface)%atti(FMARKER)==0 .and. wetu(iface)==1` (`SwashUWindStress.ftn90:230` 등).
- 응력항: `windu(iface) = alpha * cwndu(iface) * windu(iface)` (`SwashUWindStress.ftn90:435`). relwav crest 한정도 face별 (`SwashUWindStress.ftn90:441-464`).

`src/SwashExpDepUflow.ftn90:667–673`은 `relwnd`에서 `wndimp`를 `cwndu`를 `hum`으로 나눈 값으로 바꾼다 (theory-unstructured:ST2-370). [10-15 대조 정정]
`src/SwashExpDepUflow.ftn90:1040`은 이 값을 분모에 사용한다 (theory-unstructured:ST2-370). [10-15 대조 정정]
다층 대입은 `src/SwashExpLayUflow.ftn90:1084`의 최상층이다 (theory-unstructured:ST2-370). [10-15 대조 정정]

---

## 4. 파라미터 매핑 요약

| 변수 | 의미 | 출처 |
|---|---|---|
| `irough` | 바닥 roughness 방법 선택 (1,2,3,4,5,11) | `SwashBotFrict.ftn90:102` 등 |
| `pbot(1)` | 마찰계수 상수 ($C$/$n$/$k_s$/linear) | `SwashBotFrict.ftn90:128,162,196,351` |
| `pbot(2)` | Nikuradse 조도높이 $k_s$ | `SwashBotFrict.ftn90:273,726` |
| `fricf(nm,2)` | 공간변동(varfr) 마찰계수 | `SwashBotFrict.ftn90:114` |
| `iwind` | wind drag 방법 선택 (1,2,3,4) | `SwashWindStress.ftn90:380` |
| `pwnd(1)` | 상수 drag $C_d$ | `SwashWindStress.ftn90:384` |
| `pwnd(2),(3)` | `pwnd(2)`는 무차원 Charnock beta이다. `pwnd(3)`는 풍속 측정 높이이다. | `src/SwashReadInput.ftn90:840–841` [10-15 대조 정정] |
| `pwnd(4)` (alpha) | 10m→표면 보정 | `SwashWindStress.ftn90:130` |
| `pwnd(5),(6),(7)` | 선형 drag 절편·경사·풍속 계수 | `SwashWindStress.ftn90:478` |
| `pwnd(8),(9)` | 선형 drag 풍속 clamp [min,max] | `SwashWindStress.ftn90:476` |
| `pwnd(10)` (wcrstp) | crest 적용 비율 | `SwashWindStress.ftn90:131,984` |
| `cdcap` | drag 상한 | `SwashWindStress.ftn90:385` |
| `relwnd` | 흐름 상대 풍속 사용 | `SwashWindStress.ftn90:391` |
| `relwav` | 파봉추종 + crest 한정 적용 | `SwashWindStress.ftn90:166,978` |

---

## 5. 검수 메모

- 4 파일 모두 헤더 Purpose/Method를 verbatim 인용했고, 모든 마찰계수식·drag식·Charnock/Nikuradse 반복식을 file:line으로 직접 인용 — citation_status: verified 정당.
- 구조격자판과 mesh판의 반복식·상수는 같다 (Nikuradse `src/SwashBotFrict.ftn90:298`·`src/SwashUBotFrict.ftn90:254`; Charnock `src/SwashWindStress.ftn90:437`·`src/SwashUWindStress.ftn90:312`). [10-15 대조 정정]
- Manning 식의 $h^{1/3}$ 지수, Colebrook의 `18*log10` 계수와 `cfix=1.0129` 하한, Nikuradse `erough=33`/`esmoot=9`/`ev=11.6` 상수 모두 소스에서 직접 확인.
- `FRICtion` 카드의 방법·계수 매핑은 `src/SwashReadInput.ftn90:777–806`에 있다 (theory-framework:ST1-291·338·339). [10-15 대조 정정]
- Charnock의 BETA·HEIGHT 대응은 `src/SwashReadInput.ftn90:840–841`에 있다 (inputs-physics-numerics:SI2-287). [10-15 대조 정정]
- 비구조 공간 마찰 입력은 `fricf`의 세 꼭짓점 값을 산술평균한다 (`src/SwashUBotFrict.ftn90:121`; theory-unstructured:ST2-359). [10-15 대조 정정]
- 계수 생성은 `irough=1`과 `irough=11`에서 같은 대입을 사용한다 (`src/SwashUBotFrict.ftn90:109–131`; theory-unstructured:ST2-359). [10-15 대조 정정]
- `src/SwashReadInput.ftn90:801–803`은 LINEAR를 `irough=11`로 읽는다 (theory-unstructured:ST2-359). [10-15 대조 정정]
- `src/SwashExpDepUflow.ftn90:687–758`의 소비자는 `irough=11`에서 속력 인자를 생략한다 (theory-unstructured:ST2-359). [10-15 대조 정정]
- 이 분기가 선형 마찰을 구현한다 (`src/SwashExpDepUflow.ftn90:687–702`; `misc/swash.edt:148`; theory-unstructured:ST2-359). [10-15 대조 정정] [10-15 전수 검증 정정]

## 문서와 코드 차이 (10-15 대조)

문서 판: SWASH 12.01 매뉴얼 swashuse·swashtech(공개 저장소 `7949227`, 2026-05-06, "release v12.01"에서 마지막 변경); 코드 판: `VERNUM 12.01`, 공개 저장소 main `a486d5f`(2026-05-26, 12.01 뒤 `608ffd7`·`9554c98` 포함).

문서 인용의 인쇄 쪽은 PDF 쪽에서 8을 뺀 값이다.

근거 보고서: [inputs-physics-numerics](../../../_staging/recovery/compare/swash-inputs-physics-numerics-vs-code.md#5-차이-결론), [theory-framework](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md#5-차이-결론), [theory-unstructured](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#5-차이-결론).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| inputs-physics-numerics:SI2-009 | FIT 최대 풍속 문장 | swashuse PDF p.74: “Uref = 31.5 m/s is the speed at which the drag attains its maximum value in this expression.” | `src/SwashWindStress.ftn90:76–79`의 계수는 `0.55`, `2.97`, `-1.49`, `31.5`이다. | B | 해석: 인쇄된 FIT 계수의 최대점은 31.3942953 m/s이다. 31.5 m/s는 정규화 기준 풍속이다. 최대점 설명에는 반올림의 구분이 필요하다. `8756667:src/SwashWindStress.ftn90:76–79`부터 FIT 계수와 기준 풍속은 같다. 인쇄 계수의 극댓값 위치와 정규화 기준 풍속을 동일시한 문장에 한해 B를 유지한다. |
| inputs-physics-numerics:SI2-010 | 흐름과 바람 반대 방향 설명 | swashuse PDF p.74: “it will decrease when the water flow and wind are in opposite directions.” | `src/SwashWindStress.ftn90:393`: `w10 = abs(alpha*windu(nm) - u0(nm,1))`; `src/SwashExpDep1DHflow.ftn90:465`: `if ( relwnd ) then`; `src/SwashExpDep1DHflow.ftn90:473`: `wndimp(nm) = cwndu(nm) / max(1.e-3,hum(nm))` | B | 해석: 바람과 흐름의 방향이 반대이면 상대풍속 크기는 증가한다. 문서의 decrease 문장을 응력 감소의 일반 조건으로 쓰지 않는다. 상대풍속 식은 `8756667:src/SwashWindStress.ftn90:393`부터 같다. 반대 방향에서 상대풍속이 감소하던 이전 구현의 변경이 아니므로 B를 유지한다. |
| inputs-physics-numerics:SI2-030 | crest 필터의 임계값 | swashuse PDF p.75: “surface elevation is larger than the given fraction [crest] of the maximum elevation with respect to the datum level.” | `src/SwashModule1.ftn90:589`: `! =10; ratio of forced crest height to maximum surface elevation`; `src/SwashWindStress.ftn90:982`: `if ( s0(i) > smax(i) ) smax(i) = s0(i)`; `src/SwashWindStress.ftn90:984–987`: `if ( s0(i) < (1.-wcrstp) * smax(i) ) then` / `!` / `windu(i) = 0.` / `if ( .not.oned ) windv(i) = 0.`; `src/SwashUWindStress.ftn90:458`: `if ( wlvl < (1.-wcrstp) * smax(iface) ) windu(iface) = 0.`; `src/SwashReadInput.ftn90:892–894`는 RELWAVE를 켠다. `src/SwashUpdateData.ftn90:2541`과 `src/SwashUpdateUData.ftn90:1348`은 `relwav`가 참인 풍응력 경로를 호출한다. 필터는 각각 978행의 `if ( relwav ) then`과 441행의 같은 조건 안에 있다. | E 중간 | 해석: 문서는 crest배의 수위 임계값을 설명한다. 두 코드 경로는 1−crest배를 사용한다. 이 차이는 E 중간의 코드 결함 후보이다. 구조 격자 식은 `8756667:src/SwashWindStress.ftn90:984`부터, 비구조 식은 `9b8a012:src/SwashUWindStress.ftn90:458`부터 존재한다. `7949227` 및 두 후속 커밋 이후에도 보수 임계값은 같다. 상부 강제 구간 비율이라는 코드 주석은 반대 근거이므로 E 중간을 유지한다. |
| inputs-physics-numerics:SI2-036 | 선형 항력의 범위 밖 풍속 | swashuse PDF p.75: “wind speed in between [wlow] and [whigh].” | `src/SwashWindStress.ftn90:476`: `wspeed = max(pwnd(8), min(w10,pwnd(9)))` | C | 코드가 풍속을 경계값으로 잘라 항력계수를 계산한다. 응력에 곱하는 `w10` 자체는 자르지 않는다. |
| inputs-physics-numerics:SI2-037 | Charnock 반복 안전장치 | swashuse PDF p.73–76에는 반복 종료 조건과 복구값이 없다. | `src/SwashWindStress.ftn90:73`: `integer, parameter :: maxnit = 100  ! maximum number of iterations`; `src/SwashWindStress.ftn90:75`: `real   , parameter :: eps  =  0.01  ! convergence criterion`; `src/SwashWindStress.ftn90:433`: `if ( abs(sold-s) < (eps*s) ) exit`; `src/SwashWindStress.ftn90:439–442`: `if ( .not. nit < maxnit ) then` / `call msgerr (1, 'no convergence in Charnock drag computation')` / `s = 22.4` / `exit` | C | 상대 변화 기준은 0.01이다. 반복 상한은 100이다. 미수렴 때 `s=22.4`를 사용한다. |
| inputs-physics-numerics:SI2-038 | alpha 응력 정규화 | swashuse PDF p.74에는 `U_s=\alpha U_{10}`만 있다. | `src/SwashWindStress.ftn90:135`: `wfac = rhoa / ( rhow * alpha * alpha )`; `src/SwashWindStress.ftn90:401`: `cwndu(nm) = wfac * cd * w10`; `src/SwashWindStress.ftn90:962`: `windu(i) = alpha*cwndu(i)*windu(i)`; `src/SwashWindStress.ftn90:391–393`의 `if ( relwnd ) then`에서 상대풍속을 계산한다. `src/SwashExpDep1DHflow.ftn90:465–473`의 같은 조건에서 `wndimp`를 계산한다. `src/SwashExpDep1DHflow.ftn90:721`: `denom = 1. + cvegu(nm,1,2) + cpomu(nm,1) + dt * ( cbot(nm) + cporfr + cveg + wndimp(nm) )` | C | 해석: `relwnd`가 참인 1DH의 연속시간 형태는 `\tau/\rho_w=(\rho_a/\rho_w)C_d\alpha^{-2}\vert \alpha U-u\vert (\alpha U-u)`이다. 코드가 유속 부분을 시간 적분의 분모로 옮긴다. 문서는 alpha의 제곱으로 나누는 정규화를 적지 않는다. [10-15 전수 검증 정정] |
| inputs-physics-numerics:SI2-039 | RELWAVE 파속 산정·이력 최대값 | swashuse PDF p.74–75에는 파속 근사식과 최대값 갱신 절차가 없다. | `src/SwashWindStress.ftn90:175–180`: `dsdx = ( s0(nmu) - s0(nm) ) / dx` / `fac  = max( abs(dsdx), 1.e-6 )` / `!` / `dsdt = 0.5 * ( s1(nmu) + s1(nm) - so(nmu) - so(nm) ) / dt` / `!` / `wcel = min( abs(dsdt) / fac, sqrt( grav * hum(nm) ) )`; `src/SwashWindStress.ftn90:982`: `if ( s0(i) > smax(i) ) smax(i) = s0(i)`; `src/SwashCheckPrep.ftn90:3110`: `if ( relwav ) smax = 0.` | C | 파속은 수위 변화율과 경사로 계산한다. 코드가 파속 크기에 천수파속 상한을 둔다. 최대 수위는 0에서 시작한 누적 최대값이다. |
| inputs-physics-numerics:SI2-040 | RELATIVE가 항력식의 입력도 변경 | swashuse PDF p.75: “the wind stress depends on the wind velocity relative to the water.” | `src/SwashWindStress.ftn90:498`: `w10 = abs(alpha*windu(nm) - u0(nm,1))`; `src/SwashWindStress.ftn90:506`: `utl = w10/uref`; `src/SwashWindStress.ftn90:508`: `cd = 0.001*( pp + qq*utl + rr*utl*utl )` | C | 코드가 상대풍속을 응력의 속도 인자뿐 아니라 항력계수의 풍속 인자에도 사용한다. Charnock·LINEAR·FIT 분기가 이 동작을 공유한다. |
| inputs-physics-numerics:SI2-287 | Charnock 변수 의미 | `source-analysis/swash-bottom-friction-wind.md:175`: “`pwnd(2)`=Charnock 분모 계수(풍속 정규화), `pwnd(3)`=Charnock 계수 b.”; 229: “Charnock 분모계수·계수 b” | `src/SwashReadInput.ftn90:840–841`: `call INREAL('BETA'  ,pwnd(2),'STA',0.032)` / `call INREAL('HEIGHT',pwnd(3),'STA',10.)` | B | pwnd(2)는 무차원 Charnock beta이다. pwnd(3)는 풍속 측정 높이이다. 최초 공개 소스 8756667의 `src/SwashReadInput.ftn90:773–774`부터 BETA→pwnd(2), HEIGHT→pwnd(3) 대응은 같다. 두 원소의 의미를 교환한 판은 없다. B는 소스 분석 노트의 변수 설명 오기이다. |
| theory-framework:ST1-262 | 식 (3.2) 바닥 마찰 | swashtech PDF p.63: `-c_f\lVert\mathbf u\rVert\mathbf u`; `c_f` `dimensionless bottom friction coefficient`. | `src/SwashExpDep2DHflow.ftn90:903` `utot = sqrt( u0(nm)*u0(nm) + v*v )`; `src/SwashExpDep2DHflow.ftn90:905` `cbot(nm) = cfricu(nm) * utot / hum(nm)`; `src/SwashExpDep2DHflow.ftn90:1356` `denom = 1. + cvegu(nm,1,2) + cpomu(nm,1) + dt * ( cbot(nm) + cporfr + cveg + wndimp(nm) )` | F 표기 차이 | 유속식에서는 `c_f\lVert\mathbf u\rVert/h`이다. Euler 암시적 분모가 유속과 반대 방향의 마찰을 적용한다. `irough == 11`의 선형 마찰은 문서 식에 없는 별도 처리이다. 해석: `u^{n+1}=[u^n-\Delta t\,R]/[1+\Delta t\,c_f\lVert u^n\rVert/h]`는 마찰 유속만 암시적으로 둔 식이다. |
| theory-framework:ST1-263 | 식 (3.2) 바람 항 | swashtech PDF p.63: `+\boldsymbol\tau_w` | `src/SwashExpDep2DHflow.ftn90:1354` `contrib = advecx(nm) + advecy(nm) + zgrad + pgrad(nm) + qgrad(nm) - windu(nm)/max(1.e-3,hum(nm)) - visc(nm) + corf(nm)`; `src/SwashExpDep2DHflow.ftn90:1360`은 `-dt*contrib`로 유속을 갱신한다. | F 표기 차이 | 유속식은 바람 응력을 수심으로 나눈다. 구동력의 음의 바람 부호와 최종 `-dt*contrib`를 결합하면 양의 바람 가속도가 된다. `1.e-3` 수심 하한은 아래 ST1-295와 같다. 해석: `-\Delta t[-\tau_w/h]=+\Delta t\,\tau_w/h`이다. [10-15 전수 검증 정정] |
| theory-framework:ST1-291 | 선형 마찰과 마찰 비활성 | swashtech PDF p.63 식 (3.2)는 이차 마찰을 적는다. 선형 선택·기본값 없음. swashuse PDF p.76은 FRICTION 명령을 사용하지 않으면 바닥 마찰을 계산하지 않는다고 명시한다. | `src/SwashExpDep2DHflow.ftn90:858` `if ( irough == 11 ) then`; `src/SwashExpDep2DHflow.ftn90:869` `cbot(nm) = cfricu(nm) / hum(nm)`; `src/SwashExpDep2DHflow.ftn90:914` `cbot = 0.`; `src/SwashInit.ftn90:313` `irough = 0`; `src/SwashReadInput.ftn90:777` `if ( KEYWIS ('FRIC') ) then`; `src/SwashReadInput.ftn90:801–803` `else if ( KEYWIS('LIN') ) then`<br>`irough = 11`<br>`call INREAL('K',pbot(1),'UNC', 0.)`. | C 문서 누락 | C는 swashtech PDF p.63의 선형 마찰 선택 설명에 한정한다. FRICTION LIN이 `irough = 11`을 선택하며 유속 크기를 계수에 곱하지 않는다. 기본 비활성은 사용자 설명서 p.76과 일치한다. 선형 계수의 단위는 ST1-339에서 구별한다. |
| theory-framework:ST1-293 | 상대 풍속과 암시적 바람 항 | swashtech PDF p.64 식 (3.3)는 절대 10 m 풍속식이다. 상대 풍속 분기 없음. swashuse PDF p.74–75는 유속에 대한 상대 풍속과 `RELATIVE [alpha]`를 설명한다. | `src/SwashInit.ftn90:294–297` `pwnd(4) = 1.`<br>`pwnd(10)= 0.4`<br>`relwnd  = .false.`<br>`relwav  = .false.`; `src/SwashWindStress.ftn90:549–552` `if ( relwnd ) then`<br>`!`<br>`rwx = alpha*windu(nm) - u0(nm,1)`<br>`rwy = 0.25*alpha*( windv(nm) + windv(ndm) + windv(nmu) + windv(ndmu) ) - 0.25*( v0(nm,1) + v0(ndm,1) + v0(nmu,1) + v0(ndmu,1) )`; `src/SwashExpDep2DHflow.ftn90:843` `wndimp(nm) = cwndu(nm) / max(1.e-3,hum(nm))`; `src/SwashReadInput.ftn90:895–897`의 `REL`은 `relwnd = .true.`를 대입한다. `src/SwashUpdateData.ftn90:2541`의 호출 조건은 `if ( iwind /= 0 .and. (it == 0 .or. ifldyn(5) == 1 .or. relwnd .or. relwav) ) call SwashWindStress`이다. `src/SwashExpDep2DHflow.ftn90:834` `if ( relwnd ) then`. | C 문서 누락 | C는 기술문서 p.64의 상대 풍속 및 암시적 분모 설명에 한정한다. 상대 풍속 기능은 사용자 설명서에 있다. REL 선택 경로는 수심 평균 모드의 유속 또는 다층 모드의 최상층 유속을 뺀다. 상대 풍속 계수의 유속 항은 암시적 분모에 넣는다. |
| theory-framework:ST1-294 | 파속 보정과 파봉 한정 바람 | swashtech PDF p.1–66에는 이 절차가 없다. swashuse PDF p.74–76은 RELWAVE를 설명한다. p.75는 응력이 작용하는 수위가 `larger than the given fraction [crest] of the maximum elevation with respect to the datum level`이라고 적는다. p.76의 기본값은 `[crest] = 0.4`이다. | `src/SwashWindStress.ftn90:166` `if ( relwav ) then`; `src/SwashWindStress.ftn90:175–183` `dsdx = ( s0(nmu) - s0(nm) ) / dx`<br>`fac  = max( abs(dsdx), 1.e-6 )`<br>`!`<br>`dsdt = 0.5 * ( s1(nmu) + s1(nm) - so(nmu) - so(nm) ) / dt`<br>`!`<br>`wcel = min( abs(dsdt) / fac, sqrt( grav * hum(nm) ) )`<br>`if ( dsdx < 0. ) wcel = -wcel`<br>`!`<br>`windu(nm) = windu(nm) - wcel`; `src/SwashWindStress.ftn90:984–989` `if ( s0(i) < (1.-wcrstp) * smax(i) ) then`<br>`!`<br>`windu(i) = 0.`<br>`if ( .not.oned ) windv(i) = 0.`<br>`!`<br>`endif`; `src/SwashReadInput.ftn90:892–894`의 `RELW`는 `relwav = .true.`와 `call INREAL('CREST',pwnd(10),'STA',0.4)`를 실행한다. `src/SwashWindStress.ftn90:131` `wcrstp = pwnd(10)`; `src/SwashWindStress.ftn90:978` `if ( relwav ) then`. 호출 조건은 ST1-293이다. | E 코드 결함 후보(근거 중간) | 근거 강도: 중간. 파속 보정과 파봉 한정 기능 자체는 사용자 설명서에 있다. 차이는 파봉 임계값이다. 문서는 최대 수위의 crest배를 쓰지만 코드는 1−crest배 미만의 응력을 0으로 만든다. 기본 `crest=0.4`이면 코드의 경계는 최대 수위의 0.6배이다. `src/SwashWindStress.ftn90:116`의 강제 구간 높이 비율이라는 주석은 의도된 상단 구간 해석의 반대 근거이다. 입력과 준비 검사 `src/SwashCheckPrep.ftn90:1046–1048`에는 보수 변환이 없다. 인용 실행문에는 비활성 전처리 접두어가 없다. `8756667:src/SwashWindStress.ftn90:984`와 `7949227:src/SwashWindStress.ftn90:984`가 같으며 최초 문서 `8756667:doc/swashuse PDF p.65`도 crest배를 적는다. 같은 근거를 다룬 [git 판정 E2의 SI2-030](../../../_staging/recovery/compare/SWASH-git-verify-E2.md)과 맞춰 E로 정정한다. |
| theory-framework:ST1-295 | 바람 활성·항력 계수 상한·수심 하한 | swashtech PDF p.64는 `c_d`의 의미만 적는다. 활성 기본값과 두 하한·상한 없음. swashuse PDF p.73은 WIND 명령에 의한 활성화를 설명한다. p.34는 `[cdcap] = 99999`와 항력 계수를 자르지 않는다는 뜻을 적는다. | `src/SwashInit.ftn90:286` `u10  = 0.`; `src/SwashInit.ftn90:291` `iwind   = 0`; `src/SwashInit.ftn90:298` `cdcap   = 99999.`; `src/SwashWindStress.ftn90:524–529` `if ( iwind == 1 ) then`<br>`!`<br>`! constant drag coefficient`<br>`!`<br>`cd = pwnd(1)`<br>`cd = min( cdcap, cd )`; `src/SwashExpDep2DHflow.ftn90:1354` `contrib = advecx(nm) + advecy(nm) + zgrad + pgrad(nm) + qgrad(nm) - windu(nm)/max(1.e-3,hum(nm)) - visc(nm) + corf(nm)`; `src/SwashReadInput.ftn90:830–837`의 `WIND`·`CON`은 `iwind = 1`을 선택한다. `src/SwashReadInput.ftn90:540`은 `CDCAP`을 읽는다. `src/SwashCheckPrep.ftn90:288–291`은 읽은 바람 입력장이 있으면 `iwind`를 켠다. 실제 호출은 ST1-293에 인용했다. | C 문서 누락 | C는 swashtech PDF p.64에 없는 활성 선택과 수심 하한의 구현 설명이다. WIND 선택과 CDCAP은 사용자 설명서에 있다. 초기값 0만으로 전체 계산의 바람 비활성을 판정하지 않는다. 상수 항력도 `min( cdcap, cd )`를 거치며 가속도 분모는 `max(1.e-3,hum(nm))`이다. |
| theory-framework:ST1-339 | 상수·선형 마찰의 단위 | `source-analysis/swash-bottom-friction-wind.md:55` `단, 옵션 1·11(linear)은 m/s 차원` swashuse PDF p.76은 CONSTANT의 계수를 `dimensionless coefficient`로 명시한다. | `src/SwashBotFrict.ftn90:47` `!   1) a dimensionless constant,`; `src/SwashBotFrict.ftn90:104` `! dimensionless constant or linear bottom friction (dimension is m/s)`; `src/SwashExpDep2DHflow.ftn90:869` `cbot(nm) = cfricu(nm) / hum(nm)`; `src/SwashExpDep2DHflow.ftn90:905` `cbot(nm) = cfricu(nm) * utot / hum(nm)`; `src/SwashReadInput.ftn90:780–782`의 `CON`은 `irough = 1`을, `src/SwashReadInput.ftn90:801–803`의 `LIN`은 `irough = 11`을 선택한다. | B 문서 오기 (현재 노트) | 옵션 1의 이차 마찰 계수는 무차원이다. 옵션 11의 선형 마찰 계수는 m/s이다. 주석의 괄호는 바로 앞 선형 마찰의 단위이다. 두 `cbot` 식의 단위는 모두 `\mathrm s^{-1}`이다. 입력 선택과 실제 마찰 분기는 ST1-291과 같다. [10-15 전수 검증 정정] |
| theory-unstructured:ST2-124 | 바닥 마찰의 면 속도식 — 번호 없음 | swashtech PDF p.94: `\int_{\tilde e}c_f\lVert\mathbf u\rVert\mathbf u\cdot\mathbf t_{\tilde e}\,dl\approx(\Delta s_{fl}c_{f,l}\lVert\mathbf u_l\rVert+\Delta s_{fr}c_{f,r}\lVert\mathbf u_r\rVert)u_f` | `src/SwashExpDepUflow.ftn90:756` `utot = sqrt( uvc(icell,1)*uvc(icell,1) + uvc(icell,2)*uvc(icell,2) )`; `src/SwashExpDepUflow.ftn90:758` `cbot(iface) = cbot(iface) + faca * cfricu(icell) * utot / hum(iface)`; `src/SwashExpDepUflow.ftn90:1040` `denom = 1. + dt * ( cbot(iface) + wndimp(iface) )` | F 표기 차이 | 해석: 전체 길이·가중 수심으로 나누면 `cbot` 계수다. 코드는 마찰을 음해 분모로 처리한다. [theory-unstructured 보고서](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#5-차이-결론)의 ST2-365는 마른 면의 배열 초기화를 E 강함으로 판정한다. [10-15 전수 검증 정정] |
| theory-unstructured:ST2-126 | 바람 응력의 면 중점법 — 번호 없음 | swashtech PDF p.94: `\int_{\tilde e}\boldsymbol\tau_w\cdot\mathbf t_{\tilde e}\,dl\approx\Delta s_f\boldsymbol\tau_{w,f}\cdot\mathbf n_f`; `the wind speed u10 is evaluated directly at the cell face.` | `src/SwashUWindStress.ftn90:157–160` `ux = 0.5 * ( wxf(vf1,2) + wxf(vf2,2) )`, `uy = 0.5 * ( wyf(vf1,2) + wyf(vf2,2) )`, `!`, `windu(iface) = nx * ux + ny * uy`; `src/SwashUWindStress.ftn90:258` `cwndu(iface) = wfac * cd * w10`; `src/SwashUWindStress.ftn90:435` `windu(iface) = alpha * cwndu(iface) * windu(iface)` | F 표기 차이 | 해석: 입력 꼭짓점 바람을 면 중점으로 보간한 뒤 법선으로 투영한다. 전체 쌍대 길이로 나눈 면 응력이 `windu`다. |
| theory-unstructured:ST2-359 | 상수 마찰·선형 마찰·공간 입력 | swashtech PDF p.94는 이차 마찰을 설명한다. swashuse PDF p.76–77은 CONSTANT와 공간 마찰 입력을 설명한다. misc/swash.edt:148의 FRICTION 구문에는 LINEAR도 있다. | `src/SwashUBotFrict.ftn90:109` `if ( irough == 1 .or. irough == 11 ) then`; `src/SwashUBotFrict.ftn90:111` `! dimensionless constant or linear bottom friction (dimension is m/s)`; `src/SwashUBotFrict.ftn90:121` `cf = ( fricf(v(1),2) + fricf(v(2),2) + fricf(v(3),2) )/ 3.`; `src/SwashUBotFrict.ftn90:123` `cfricu(icell) = cf`; `src/SwashUBotFrict.ftn90:131` `cfricu(icell) = pbot(1)`; `src/SwashExpDepUflow.ftn90:702` `cbot(iface) = ( finp * cfricu(icelll) + (1.-finp) * cfricu(icellr) ) / hum(iface)`; `src/SwashReadInput.ftn90:777–803`의 CONSTANT·LINEAR는 각각 `irough=1`·11을 설정한다. `src/SwashExpDepUflow.ftn90:687`의 `if ( irough == 11 ) then`은 선형 마찰 분기다. :758은 이차 마찰에서 utot를 곱한다. | C 문서 누락 | 두 선택은 같은 계수 대입을 사용한다. 소비자는 `irough=11`에서 속력 인자를 곱하지 않는다. 따라서 두 선택의 힘은 같지 않다. C는 선형·이차 마찰 소비자의 차이와 비구조 꼭짓점 입력의 셀 평균에 한정한다. |
| theory-unstructured:ST2-360 | Chézy 계수 | swashuse PDF p.76–77은 CHEZY 선택과 입력 단위를 설명한다. swashtech PDF p.94는 일반 마찰계수를 쓴다. 아래 무차원 계수 변환식과 0 입력 분기는 적지 않는다. | `src/SwashUBotFrict.ftn90:137` `else if ( irough == 2 ) then`; `src/SwashUBotFrict.ftn90:151–153` `if ( cf /= 0. ) then`, `!`, `cfricu(icell) = grav / ( cf * cf )`; `src/SwashUBotFrict.ftn90:163–165` `if ( pbot(1) /= 0. ) then`, `!`, `cfricu(icell) = grav / ( pbot(1) * pbot(1) )` | C 문서 누락 | 공간 입력과 상수 입력 모두 중력을 Chézy 계수 제곱으로 나눈다. 계수가 0이면 이 블록은 대입하지 않는다. |
| theory-unstructured:ST2-361 | Manning 계수 | swashuse PDF p.76–77은 MANNING 선택과 입력 단위를 설명한다. 아래 수심 의존 변환식과 양의 수심 조건은 swashtech PDF p.94 및 사용설명서의 해당 설명에 없다. | `src/SwashUBotFrict.ftn90:173` `else if ( irough == 3 ) then`; `src/SwashUBotFrict.ftn90:187–189` `if ( hs(icell) > 0. ) then`, `!`, `cfricu(icell) = grav * cf * cf / hs(icell)**(1./3.)`; `src/SwashUBotFrict.ftn90:201` `cfricu(icell) = grav * pbot(1) * pbot(1) / hs(icell)**(1./3.)` | C 문서 누락 | 코드는 양의 셀 수심에서만 Manning 계수를 무차원 마찰계수로 바꾼다. |
| theory-unstructured:ST2-362 | Nikuradse 거친 바닥 | swashuse PDF p.76–78은 LOGLAW·ROUGHNESS 선택을 설명한다. swashtech PDF p.94에는 아래 수심 평균 로그 변환식이 없다. | `src/SwashUBotFrict.ftn90:209` `else if ( irough == 4 ) then`; `src/SwashUBotFrict.ftn90:231` `cfricu(icell) = ( vonkar / log( erough*hs(icell)/(exp(1.)*cf) ) )**2.`; `src/SwashUBotFrict.ftn90:288` `cfricu(icell) = ( vonkar / log( erough*hs(icell)/(exp(1.)*pbot(2)) ) )**2.`; `src/SwashUBotFrict.ftn90:75` `real   , parameter :: erough = 33.0   ! empirical constant for logarithmic log-law in case of rough beds`; `src/SwashCheckPrep.ftn90:5955–5959`는 `if ( irough /= 0 .and. ( irough /= 4 .or. kmax == 1 ) ) then` 안에서 비구조 SwashUBotFrict를 호출한다. | C 문서 누락 | 공간 입력은 `cf`를 사용한다. 상수 입력은 `pbot(2)`를 사용한다. 두 경로 모두 양의 수심과 0이 아닌 거칠기 조건에서 로그식을 계산한다. 이 식은 수심 평균 LOGLAW 계수다. 다층의 `irough=4`는 `src/SwashUpdateUData.ftn90:1337–1338`에서 SwashULogLaw를 호출한다. C는 수심 평균 로그식의 수치 계수와 분기 조건에 한정한다. |
| theory-unstructured:ST2-363 | 매끈한 바닥의 반복·실패 복귀 | swashuse PDF p.77은 LOGLAW SMOOTH 선택을 설명한다. swashtech PDF p.94 및 그 사용설명서 설명에는 아래 반복 문턱·상한·복귀값이 없다. | `src/SwashUBotFrict.ftn90:71–77` `integer, parameter :: maxnit = 100    ! maximum number of iterations`, `!`, `real   , parameter :: cfix   = 1.0129 ! minimum value for argument of log10 function in Colebrook-White`, `real   , parameter :: eps    = 0.01   ! convergence criterion`, `real   , parameter :: erough = 33.0   ! empirical constant for logarithmic log-law in case of rough beds`, `real   , parameter :: esmoot = 9.0    ! empirical constant for logarithmic log-law in case of smooth beds`, `real   , parameter :: ev     = 11.6   ! edge of viscous sublayer`; `src/SwashUBotFrict.ftn90:235–236` `r = utot*hs(icell)/(exp(1.)*kinvis)`, `if ( r < 0.001 ) r = 0.001`; `src/SwashUBotFrict.ftn90:250` `if ( abs(sold-s) < (eps*s) ) exit`; `src/SwashUBotFrict.ftn90:254` `s    = sold*(1.+log(esmoot*r/sold))/(1.+vonkar*sold)`; `src/SwashUBotFrict.ftn90:256–259` `if ( .not. nit < maxnit ) then`, `call msgerr (1, 'no convergence in bottom friction computation')`, `s = sqrt(r)`, `exit`; `src/SwashUBotFrict.ftn90:270` `cfricu(icell) = 1./(s*s)` | C 문서 누락 | 거칠기가 0이면 Reynolds 수에 비례하는 반복 변수 r를 0.001 이상으로 제한한다. 원문의 r는 `utot*hs(icell)/(exp(1.)*kinvis)`이므로 Reynolds 수 자체와 구별한다. `r > ev**2`에서 반복한다. 실패하면 `s = sqrt(r)`로 복귀한다. 상수 입력도 :292–327에서 같은 절차를 쓴다. C는 반복 알고리즘에 한정한다. |
| theory-unstructured:ST2-364 | Colebrook–White 계수·미지원 마찰 | swashuse PDF p.76–77은 COLEBROOK 선택을 설명한다. swashtech PDF p.94 및 사용설명서의 해당 설명에는 아래 로그식·인자 하한·오류 분기가 없다. | `src/SwashUBotFrict.ftn90:337` `else if ( irough == 5 ) then`; `src/SwashUBotFrict.ftn90:351–354` `if ( hs(icell) > 0. .and. cf /= 0. ) then`, `!`, `cz = 18. * log10 ( max(12.*hs(icell) / cf, cfix) )`, `cfricu(icell) = grav / cz**2`; `src/SwashUBotFrict.ftn90:366–367` `cz = 18. * log10 ( max(12.*hs(icell) / pbot(1), cfix) )`, `cfricu(icell) = grav / cz**2`; `src/SwashUBotFrict.ftn90:377` `call msgerr ( 4, 'unknown roughness method for bottom friction' )` | C 문서 누락 | 로그 인자의 하한은 1.0129다. 비구조 마찰 루틴은 나열한 선택 이외의 번호를 거부한다. |
| theory-unstructured:ST2-366 | 바람 배율·상수 항력·상한 | swashuse PDF p.34는 CDCAP을 설명한다. p.74–75는 바람 배율·상수 항력과 기본값을 설명한다. swashtech PDF p.64·94는 밀도비와 면 응력을 설명한다. | `src/SwashInit.ftn90:293–298` `pwnd(1) = 0.002`, `pwnd(4) = 1.`, `pwnd(10)= 0.4`, `relwnd  = .false.`, `relwav  = .false.`, `cdcap   = 99999.`; `src/SwashUWindStress.ftn90:138` `wfac = rhoa / ( rhow * alpha * alpha )`; `src/SwashUWindStress.ftn90:225–226` `cd = pwnd(1)`, `cd = min( cdcap, cd )`; `src/SwashUWindStress.ftn90:258` `cwndu(iface) = wfac * cd * w10`; `src/SwashUWindStress.ftn90:435` `windu(iface) = alpha * cwndu(iface) * windu(iface)` | C 문서 누락 | 코드는 공기·물 밀도비와 바람 보정 배율을 적용한다. 모든 항력 선택은 `cdcap`으로 항력계수를 제한한다. C는 alpha를 응력 계수에 분배하는 내부 환산식에 한정한다. |
| theory-unstructured:ST2-367 | Charnock 항력의 반복 | swashuse PDF p.73·75는 CHARNOCK 선택과 입력값을 설명한다. swashtech PDF p.94 및 사용설명서의 해당 설명에는 아래 반복 정지·실패 복귀 절차가 없다. | `src/SwashUWindStress.ftn90:264` `else if ( iwind == 2 ) then`; `src/SwashUWindStress.ftn90:75–77` `integer, parameter :: maxnit = 100  ! maximum number of iterations`, `!`, `real   , parameter :: eps  =  0.01  ! convergence criterion`; `src/SwashUWindStress.ftn90:302` `s    = 22.4`; `src/SwashUWindStress.ftn90:308` `if ( abs(sold-s) < (eps*s) ) exit`; `src/SwashUWindStress.ftn90:312` `s    = sold*(log(pwnd(3)*grav*sold*sold / (max(0.001,pwnd(2)*w10*w10)))-2.) / (vonkar*sold-2.)`; `src/SwashUWindStress.ftn90:314–317` `if ( .not. nit < maxnit ) then`, `call msgerr (1, 'no convergence in Charnock drag computation')`, `s = 22.4`, `exit`; `src/SwashUWindStress.ftn90:322–325` `cd = 1./(s*s)`, `cd = min( cdcap, cd )`, `!`, `cwndu(iface) = wfac * cd * w10` | C 문서 누락 | 코드는 상대 변화 0.01을 정지 문턱으로 사용한다. 반복 실패 시 초기값 22.4를 다시 사용한다. |
| theory-unstructured:ST2-368 | 수면 경사·풍속에 따른 선형 항력 | swashuse PDF p.75: `[a2] not used.`. 같은 쪽의 LINEAR 인쇄식에도 a2와 경사 항이 없다. | `src/SwashUWindStress.ftn90:331` `else if ( iwind == 3 ) then`; `src/SwashUWindStress.ftn90:367–371` `slope = rdx * ( s0(icellr) - s0(icelll) )`, `wspeed = max(pwnd(8), min(w10,pwnd(9)))`, `!`, `cd = 0.001*( pwnd(5) + pwnd(6)*abs(slope) + pwnd(7)*wspeed )`, `cd = min( cdcap, cd )`; `src/SwashReadInput.ftn90:842–845`의 LINEAR 분기는 `iwind = 3`과 `call INREAL('A2'   ,pwnd(6),'UNC',0.)`로 계수를 읽는다. | B 문서 오기 | LINEAR 항력계수에는 a2와 수면 경사 크기의 곱이 들어간다. a2는 활성 계수다. 문서의 미사용 설명은 B다. wlow·whigh는 항력식의 wspeed를 제한하며 응력 속력 인자 w10 자체를 바꾸지는 않는다. [SWASH-git-verify-AD.md §3 SI2-022·SI2-024](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)와 같은 사실이다. `8756667 2022-09-03 initial release`의 `src/SwashReadInput.ftn90:778`과 `src/SwashWindStress.ftn90:478`에 입력·소비가 있다. 비구조 식은 `9b8a012 2023-10-11 initial release (v 10.01)`의 `src/SwashUWindStress.ftn90:370`에 있다. 12.01 뒤 두 커밋은 이 식을 바꾸지 않았다. |
| theory-unstructured:ST2-370 | 상대 바람과 음해 속도 항 | swashuse PDF p.74–75는 RELATIVE의 유속 차감을 설명한다. swashtech PDF p.94 및 사용설명서의 해당 설명에는 비구조 접선 보간과 음해 분모의 식이 없다. | `src/SwashUWindStress.ftn90:244–247` `vt = nx * ( finp * uvc(icelll,1,2) + (1.-finp) * uvc(icellr,1,2) ) - ny * ( finp * uvc(icelll,1,1) + (1.-finp) * uvc(icellr,1,1) )`, `!`, `rwx = alpha*windu (iface) - u0(iface,1)`, `rwy = alpha*wndimp(iface) - vt`; `src/SwashExpDepUflow.ftn90:667` `if ( relwnd ) then`; `src/SwashExpDepUflow.ftn90:673` `wndimp(iface) = cwndu(iface) / hum(iface)`; `src/SwashExpDepUflow.ftn90:1040` `denom = 1. + dt * ( cbot(iface) + wndimp(iface) )`; `src/SwashReadInput.ftn90:895–896`의 RELATIVE 선택은 relwnd를 켠다. `src/SwashUWindStress.ftn90:164`는 wndimp에 접선 바람을 임시 저장한다. | C 문서 누락 | 상대 풍속의 법선 성분은 면 속도를 뺀다. 접선 성분은 양쪽 셀 재구성 속도의 가중값을 뺀다. 코드는 속도 의존 항을 운동량 분모에 넣는다. C는 접선 속도 보간과 wndimp를 분모 계수로 바꾸는 절차에 한정한다. |
| theory-unstructured:ST2-371 | 파속을 뺀 바람·파봉 한정 응력 | swashuse PDF p.74–75는 RELWAVE와 파봉 제한을 설명한다. p.75의 `fraction [crest] of the maximum elevation with respect to the datum level.`은 기준면에서 crest배인 임계 수위다. | `src/SwashUWindStress.ftn90:184` `if ( relwav ) then`; `src/SwashUWindStress.ftn90:199–207` `slope = rdx * ( s0(icellr) - s0(icelll) )`, `fac   = max( abs(slope), 1.e-6 )`, `!`, `dsdt = ( finp * s1(icelll) + (1.-finp) * s1(icellr) - finp * so(icelll) - (1.-finp) * so(icellr) ) / dt`, `!`, `wcel = min( abs(dsdt) / fac, sqrt( grav * hum(iface) ) )`, `if ( slope < 0. ) wcel = -wcel`, `!`, `windu(iface) = windu(iface) - wcel`; `src/SwashUWindStress.ftn90:458` `if ( wlvl < (1.-wcrstp) * smax(iface) ) windu(iface) = 0.`; `src/SwashReadInput.ftn90:892–894`는 RELWAVE에서 relwav를 켜고 CREST를 pwnd(10)에 읽는다. `src/SwashCheckPrep.ftn90:1046–1048`은 범위 밖 값만 복구한다. `src/SwashUpdateUData.ftn90:1348`은 iwind가 0이 아니고 relwav가 참이면 SwashUWindStress를 호출한다. `src/SwashUWindStress.ftn90:134`는 `wcrstp = pwnd(10)`이다. :441–458은 젖은 내부면의 수위를 smax와 비교한다. 조건문에는 비활성 전처리 접두어가 없다. | E 코드 결함 후보(중간) | RELWAVE 문서는 crest배의 최대 수위를 응력 적용 임계값으로 설명한다. 코드는 `(1.-wcrstp) * smax(iface)`를 사용한다. `crest=0.5`에서는 두 임계값이 같지만 다른 값에서는 달라질 수 있다. 두 격자에서 같은 식이 반복된다는 반대 근거가 있으므로 E 중간으로 판정한다. 파속 추정·차감의 존재 자체는 문서와 일치한다. [SWASH-git-verify-E2.md §2 SI2-030](../../../_staging/recovery/compare/SWASH-git-verify-E2.md)과 같은 임계값이다. 비구조 식은 `9b8a012 2023-10-11 initial release (v 10.01)`의 `src/SwashUWindStress.ftn90:458`부터 있다. `7949227 2026-05-06 release v12.01`에도 같다. `608ffd7`·`9554c98`은 이 식을 수정하지 않았다. |
| theory-unstructured:ST2-386 | 다층 이차 마찰의 속력 환산 | swashuse PDF p.76은 수심 평균 마찰계수와 다층 난류 처리를 구별한다. swashtech PDF p.94·109 및 사용설명서의 해당 설명에는 아래 속력 환산식이 없다. | `src/SwashExpLayUflow.ftn90:290–295` `if ( irough /= 0 .and. irough /= 4 .and. irough /= 11 ) then`, `call perot ( udep, 1, 1 )`, `work(:,1) = uvc(:,1,1)`, `work(:,2) = uvc(:,1,2)`, `endif`, `call perot ( u0, 1, kmax )`; `src/SwashExpLayUflow.ftn90:1244–1250` `utot = sqrt( uvc(icell,kmax,1)*uvc(icell,kmax,1) + uvc(icell,kmax,2)*uvc(icell,kmax,2) )`, `!`, `if ( utot > 1.e-8 ) then`, `!`, `fac = work(icell,1)*work(icell,1) + work(icell,2)*work(icell,2)`, `!`, `amatu(iface,kmax,1) = amatu(iface,kmax,1) + faca * cfricu(icell) * fac / ( utot * hkum(iface,kmax) )` | C 문서 누락 | 코드는 수심 평균 속력의 제곱을 최하층 속력으로 나눈다. 최하층 속력이 `10^{-8}` 이하이면 이 항을 추가하지 않는다. 단순히 최하층 속력에 `c_f`를 곱한 계수와 다르다. |
