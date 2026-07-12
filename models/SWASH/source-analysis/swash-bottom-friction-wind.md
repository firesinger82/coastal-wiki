---
title: "SWASH 바닥마찰 + 바람응력 — SwashBotFrict/SwashWindStress (구조격자) & SwashUBotFrict/SwashUWindStress (비구조 mesh)"
model: SWASH
component: src (외력항: 바닥마찰·바람응력)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashBotFrict.ftn90(:39-52 헤더, :100-927 6 roughness 옵션 식), SwashWindStress.ftn90(:38-58 Charnock 헤더, :380-520 4 drag 옵션 식, :960-993 stress 적용), SwashUBotFrict.ftn90(:38-380 flexible mesh), SwashUWindStress.ftn90(:38-466 mesh wind) 를 file:line 인용"
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

**입력 카드·기본값(2026-07-12 직독)**: `FRICtion` 카드가 `irough` 를 설정 — 키워드 생략 시 **MANNing 이 기본**(`irough=3`, cf=0.019). `CONstant`→1(cf=0.002), `CHEZy`→2(C=65), `MANNing`→3(n=0.019), `LOGlaw [SMOOTH|ROUGH [h]]`→4(기본 SMOOTH, pbot(2)=0), `COLEbrook [h]`→5, `LINear [k]`→11 (`SwashReadInput.ftn90:777-806`). 카드 자체를 생략하면 바닥마찰 off(`irough` 초기 0 유지).

산출 `cfricu`/`cfricv`는 무차원 마찰계수 $c_f$(헤더 "constant"는 dimensionless라고 명시, `SwashBotFrict.ftn90:47`). 단, 옵션 1·11(linear)은 m/s 차원 (`SwashBotFrict.ftn90:104` 주석 "dimension is m/s").

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

⚠ 미확인: SwashUBotFrict는 `periodic` 동기화 호출이 없음 (`SwashUBotFrict.ftn90` 전체에 periodic 부재) — mesh판은 반복격자 미지원으로 보임.

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
`pwnd(2)`=Charnock 분모 계수(풍속 정규화), `pwnd(3)`=Charnock 계수 b. 미수렴(`maxnit=100`, `:73`) 시 경고 + `s=22.4` 복귀 (`SwashWindStress.ftn90:439-442`).

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

### 3.7 Flexible mesh판 (SwashUWindStress)

동일 4 drag 방법·동일 상수(`pp/qq/rr=0.55/2.97/-1.49`, `uref=31.5`, `SwashUWindStress.ftn90:78-81`)·동일 Charnock 반복식 (`SwashUWindStress.ftn90:312` = `SwashWindStress.ftn90:437`). 차이점:
- face 법선/접선으로 분해: `windu(iface)=nx*ux+ny*uy`(법선풍), `wndimp(iface)`에 접선풍 임시저장 (`SwashUWindStress.ftn90:160-164`).
- `call perot ( u0, 1, 1 )`로 cell 속도벡터 복원 후 상대풍 계산 (`SwashUWindStress.ftn90:217,244`).
- 내부 wet face만 처리: `face(iface)%atti(FMARKER)==0 .and. wetu(iface)==1` (`SwashUWindStress.ftn90:230` 등).
- 응력항: `windu(iface) = alpha * cwndu(iface) * windu(iface)` (`SwashUWindStress.ftn90:435`). relwav crest 한정도 face별 (`SwashUWindStress.ftn90:441-464`).

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
| `pwnd(2),(3)` | Charnock 분모계수·계수 b | `SwashWindStress.ftn90:437` |
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
- 구조격자판과 mesh판의 **반복식·상수가 완전 동일**함을 확인 (Nikuradse `SwashBotFrict.ftn90:298`=`SwashUBotFrict.ftn90:254`; Charnock `SwashWindStress.ftn90:437`=`SwashUWindStress.ftn90:312`). 모순 없음.
- Manning 식의 $h^{1/3}$ 지수, Colebrook의 `18*log10` 계수와 `cfix=1.0129` 하한, Nikuradse `erough=33`/`esmoot=9`/`ev=11.6` 상수 모두 소스에서 직접 확인.
- ~~⚠ 미확인: `pbot`/`pwnd`/`fricf` 배열 매핑 read 루틴 — 입력 키워드명은 source-needed.~~ **부분 해소(2026-07-12)**: `FRICtion` 카드→`irough`+`pbot(1)`/`pbot(2)` 매핑·키워드·기본값을 §2 서두에 직독 반영(`SwashReadInput.ftn90:777-806`). `pwnd`(바람)·`fricf`(공간변동 마찰 read) 매핑은 여전히 미정독.
- ⚠ 미확인: SwashUBotFrict는 옵션 1/11 분기에서 linear(11)와 constant(1)를 동일 처리(`SwashUBotFrict.ftn90:109-135`); 구조격자판도 동일(`SwashBotFrict.ftn90:102-134`). linear bottom friction의 별도 물리식은 두 파일 모두 cfricu에 그대로 대입할 뿐 별도 분기 없음 — "linear"는 단지 cfricu가 m/s 차원으로 해석됨을 의미(주석 `:104`).
