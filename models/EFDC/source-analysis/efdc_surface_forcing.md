---
title: "EFDC+ 수면 풍응력 + 대기강제 source-analysis — caltsxy.f90 (WINDSTRESS 4 drag law·WSER/ASER·강수-증발)"
topic: efdc-surface-forcing
canonical_source: self
citation_status: verified
verification_method: "EFDC+ Stable(12.4, sha 3ed76b6) raw source 직접 read: caltsxy.f90(865) — IWDRAG 4 drag law(:774-802)·풍응력 TSX=1.225E-3·CD10·U10·rel(:807-815) file:line 직접 검증. 소비처 calpuv2c/calexp/calqvs. 소스주석 primary Hersbach 2011 ECMWF(:785)·COARE3.6 Edson2013(:788). ice 분기(:612-753)는 [[efdc_ice]] 소관 제외."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
verification_by: "Claude Opus 4.8 (1M context) — caltsxy.f90:772-817 직접 read 검증"
verification_date: 2026-07-04
related:
  - models/EFDC/source-analysis/efdc_heat_temperature.md
  - models/EFDC/source-analysis/efdc_cyclone_wind.md
  - models/EFDC/source-analysis/efdc_bottom_friction.md
  - models/EFDC/source-analysis/efdc_ice.md
---

# EFDC+ 수면 풍응력 + 대기강제 — `caltsxy.f90`

> 소스: [`caltsxy.f90`](../raw/source_code/EFDCPlus_Stable/EFDC/caltsxy.f90) (865). EFDC+ Stable = 12.4, sha `3ed76b6`.
> **정체**: 시변 **수면 풍응력(TSX/TSY) + 대기강제(기압·기온·강수·증발)** 드라이버 — 저면마찰([[efdc_bottom_friction]])·열([[efdc_heat_temperature]])의 momentum-forcing 형제. 기존엔 ice 분기(:612-753 → [[efdc_ice]])만 커버, **풍드래그 법칙·WSER/ASER 시계열·공간 station 가중·강수/증발 volume 결합은 미문서**.

## 0. 구조

| 서브루틴 | 라인 | 역할 |
|---|---|---|
| `CALTSXY(INITFLAG)` | 9-753 | WSER(풍)/ASER(대기)/ISER(빙) 시계열→현재시각 보간 + 공간 station 가중 + cyclone overlay + per-cell `WINDSTRESS` dispatch + ice 서브모델(:612-753, [[efdc_ice]]) |
| `WINDSTRESS(L)` | 755-864 | per-cell 풍응력 법칙: sheltering + IWDRAG 4택1 drag → TSX/TSY(m²/s²) + 2m 풍속 WINDST(heat용) |

## 1. 풍 시계열 → 벡터 (:228-258)
```fortran
! WSER 시간보간 — M2 를 NREC 로 clamp, ★"THIS ALLOWS USING EXTRAPOLATION"(:234) 무음 외삽
DEG = 90 - dir                                       ! :244 기상학 관례→E/N 분해
CONVRT2 = LOG(2.0/0.003)/LOG(WINDH(NW)/0.003)         ! :255-258 풍속계고→2m 로그법칙(★z0=0.003 하드코딩=open grassland)
```
시변 wind-map window(`IWMP` TWNDMAPBEG/END) + **다중 station 공간가중 `WNDWHT`**(:265-298), 2m→10m `CONVRT2=LOG(10/0.003)/LOG(2/0.003)`(:278).

## 2. WINDSTRESS — 4 drag law (IWDRAG, :774-802)
```fortran
IWDRAG<2 : ORIGINAL EFDC piecewise polynomial (U10<5 / 5-7 / >7 구간)   ! :776-782
IWDRAG==2: HERSBACH 2011 ECMWF  CD10=(0.00103+0.00004·U10^1.48)/U10^0.21 ! :786
IWDRAG==3: COARE 3.6 (Edson 2013) neutral 간소화 (U10>20 선형 / else quartic)  ! :790-792
IWDRAG==4: USER 선형(WDRAG1/2·CDRAG1/2 보간)                             ! :796-801
```

## 3. 풍응력식 (:807-820)
```fortran
! IWDRAG>0: 물 상대 풍속 (current-relative)
TSEAST = WINDSXX*WNDVELE + WINDSXY*WNDVELN - U(L,KC)   ! :807 ★-U(L,KC) 상대풍
TSX(L) = 1.225E-3*CD10*U10*TSEAST                      ! :810 (★1.225E-3=ρa/ρw 하드코딩)
if( IWDRAG==3 .and. ISTOPT(2)==2 ) TSX = 1.225E-3*CDCOARE(L)*U10*TSEAST   ! :812-815 heat COARE 시 momentum drag 교체
! IWDRAG==0: 절대풍(상대 아님) :816-820
```
2m 풍속(heat용) `WINDST(L)=U10/CONVRT2`(:862). 방향 sheltering/채널용 legacy Wu형 `C2=1.2E-6*(0.8+0.065*U10)`(:833,846,857).

## 4. 대기강제 (ASER, :332-470)
- 기압·건구·습구·강수·증발·solar·cloud 시계열 보간. 포화증기압 `SVPAT=10.**((0.7859+0.03477*TATM)/(1.+0.00412*TATM))`(:360).
- **기압→수두**(barometric IATMP): `ATMP(L)=PATMT(L)*0.0101974*G`(:439,470, m²/s²).
- 증발/전도 wind function: `CLEVAP=1.E-3*(0.8+0.065*WINDST)`(:509-529), `CCNHTT`(:532-551).

## 5. 강수/증발 → 연속식 (calqvs, ★여기서 준비, 저기서 적용)
`QSUM(L,KC) += DXYP(L)*(RAINT - EVAPT)` (calqvs.f90:1618,1631, top-layer 체적소스). 증발률 `EVAPT=CLEVAP*0.7464E-3*WINDST*(SVPW1-VPAT)/PATMT`(calpuv9c.f90:1332). → forcing 은 caltsxy 에서 **준비**, transport/continuity 스텝에서 **적용**.

## 6. Momentum handoff (소비처)
- 외부모드: `calpuv2c.f90:224,226` `+DXYU*(TSX-RITB1*TBX)` (수면전단→수심적분 momentum, [[efdc_bottom_friction]] TBX 와 나란히).
- 내부모드: `calexp.f90:1383-1384` `DU -= CDZUU*TSX`.
- **cyclone overlay**: `call CycloneFields(TIMEDAY)`(:487) → per-cell WINDSTRESS 재계산([[efdc_cyclone_wind]]).

## 7. 주요 findings
- **z0=0.003 하드코딩** — 전 풍속계고·2m↔10m 변환이 지형/수면 무관 고정(open grassland, :255-278).
- **ρa/ρw=1.225E-3 하드코딩** — 온도/염분 밀도의존 없음(:810).
- **무음 시간외삽** — WSER/ASER 종료 후 마지막 구간 기울기 외삽(:234, 매뉴얼은 hold-last 암시).
- **IWDRAG==3 & ISTOPT(2)==2 결합**(:812-815) — heat COARE 옵션이 momentum drag(CDCOARE)를 조용히 교체.
- **current-relative 는 IWDRAG>0 게이트**(:807 -U(L,KC)) — IWDRAG==0 은 절대풍(:816).
- **방향투영 폐기**(:842→844): `WINDXX=WINDSXX·..+WINDSXY·..` 계산 후 즉시 `WINDXX=WNDFAC*WNDVELE` 덮어씀(X-채널 sheltering).
- **dead var** WINDS1/WINDS2 동일식·미사용(:246-247 copy-paste).

## 8. 관련
- [[efdc_heat_temperature]] — 수면 heat(TATMT/SVPAT/CLEVAP 공유, COARE ISTOPT(2)==2)
- [[efdc_cyclone_wind]] — mod_cyclone(CycloneFields overlay, TSX 재계산)
- [[efdc_bottom_friction]] — TBX 저면전단(momentum 조립부 TSX 와 나란히)
- [[efdc_ice]] — ice 분기(:612-753, TAUICE 풍응력 overwrite)
- **Primary**: Hersbach 2011 ECMWF · COARE 3.6 Edson2013(coare36.f90) · Wu 1980/Garratt 1977(uncited) · Ryan-Harleman 1974(CE-QUAL-W2) · theory [[efdc-theory-v12-ch2-hydrodynamics]] §wind drag.
