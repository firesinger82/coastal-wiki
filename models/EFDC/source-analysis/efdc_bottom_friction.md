---
title: "EFDC+ 저면마찰 source-analysis — caltbxy.f90 (STBX/STBY drag law + wave-current BBL + vegetation + channel friction)"
topic: efdc-bottom-friction
canonical_source: self
citation_status: verified
verification_method: "EFDC+ Stable(12.4, sha 3ed76b6) raw source 직접 read: EFDC/caltbxy.f90(879줄) — DSI drag(:542)·legacy(:598)·GOTM(:517-519)·ripple(:328-329) file:line 직접 검증. 소비처 calpuv9c.f90/hdmt.f90 cross-ref. primary source 소스주석 Nezu-Nakagawa 1993(:541)·Hamrick 2001/2002(:25,:27)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
verification_by: "Claude Opus 4.8 (1M context) — caltbxy.f90:325-330·511-548·595-607 직접 read 검증"
verification_date: 2026-07-04
related:
  - models/EFDC/source-analysis/efdc_hydro_core.md
  - models/EFDC/source-analysis/efdc_external_mode_solver.md
  - models/EFDC/source-analysis/efdc_turbulence.md
  - models/EFDC/source-analysis/sediment/efdc_sedzlj.md
---

# EFDC+ 저면마찰 source-analysis — `caltbxy.f90`

> 소스: [`EFDC/caltbxy.f90`](../raw/source_code/EFDCPlus_Stable/EFDC/caltbxy.f90) (879줄, 단일 `SUBROUTINE CALTBXY` :30-878). EFDC+ Stable = 12.4, sha `3ed76b6`.
> **핵심**: 저면조도 `ZBR` → 2차 drag law 계수 `STBX/STBY` 산출. ZBR = EFDC 수력 최다 calibration knob 이나 기존 노트 미커버(hydro_core 는 하류 implicit `RCX/RCY`만 언급). 호출: `hdmt.f90:253`(init)·`:1148`(step).

## 0. CALTBXY 의 정체 — "drag 계수, stress 아님"

⚠ CALTBXY 는 **drag 계수 STBX/STBY** (무차원)만 산출. 실제 저면응력 `TBX/TBY` 와 저면 turbulent intensity `QQ(L,0)` 은 **하류 HDMT 에서 조립**(`hdmt.f90:266-267`) — "bottom stress" 추적 시 흔한 혼동점. 계수는 momentum solver 의 implicit drag `RCX/RCY`(`calpuv9c.f90:269-270`)로 소비.

블록 구조 (단일 subroutine 내):

| 라인 | 블록 |
|---|---|
| :69-80 | DELT 선택 (3TL DT2 / 2TL DT·DTDYN) |
| :83-217 | first-call init: 면조도 ZBRATU/V·implicit/explicit split(ISITB)·vegetation flags |
| :276-498 | **wave-current BBL** (ZBRE·ripple·analytic BBL 적분 → STBX/Y) |
| :500-634 | **non-wave 저면응력** (GOTM/DSI-default/legacy 3분기) ← 최다 경로 |
| :637-816 | internal-mode vegetation drag FXVEG/FYVEG |
| :819-873 | sub-grid channel friction CHANFRIC |

## 1. 면 조도 (:99-100)

셀중심 `ZBR` → 면(face) 가중평균:
```fortran
ZBRATU(L) = 0.5*(DXP(LW)*ZBR(LW)+DXP(L)*ZBR(L))*DXIU(L)   ! :99  U-면
```
파랑용 Nikuradse 조도 `ZBRE = KSW/30` (:132).

## 2. Non-wave 저면 drag (:500-634) — 3 분기

`ISGOTM/IFRICTION`·`ICALTB` dispatch:

### 2.1 GOTM 반복 log-law (:511-522)
```fortran
do itr = 1, itz0b(=10)                             ! :516 10회 반복
  z0b_gotm = 0.1*AVO/max(AVO,GTAUB) + 0.03*ZBR(L)  ! :517 점성+조도 조합 z0
  rr       = VKC/log((z0b_gotm+ztemp)/z0b_gotm)     ! :518 log-law
  GTAUB    = rr*sqrt(UCTR²+VCTR²)                    ! :519 u* 갱신
enddo
STBX = STBY = rr                                     ! :521-522
```

### 2.2 DSI-default 2차 drag (`ICALTB==0`, :524-546) — **표준 경로**
```fortran
HUDZBR = HU(L)/ZBRATU(L)
HUDZBR = max(HUDZBR, 7.5)                    ! :538 하한(LOG→0 방지)
! *** NEZU & NAKAGAWA (1993), wake parameter 0.2, -0.8 = wake-1  (:541 주석)
STBX(L) = (VKC/(LOG(HUDZBR) - 0.8))**2       ! :542
STBX(L) = min(CDMAXU, STBX(L))               ! :545 안정 상한
```
- `CDMAXU = CDLIMIT*HU/(DELT*UMAGTMP)` (:532) — 시간스텝 안정 상한.

### 2.3 Legacy log-law (:595-606)
```fortran
STBX(L) = STBXO(L)*0.16/((LOG(HUDZBR) - 1.)**2)              ! :598  (0.16=VKC²=0.4²)
! SGZ 층두께 변형:
DZHUDZBR = 1. + SGZUU(L,KSZU(L))*HURTMP/ZBRATU(L)            ! :601
STBX(L) = STBXO(L)*0.16/((LOG(DZHUDZBR))**2)                 ! :605
```

> ⚠ **calibration gotcha (분기간 상수차)**: DSI-default 는 `(VKC/(LOG(H/ZBR)-0.8))²` (-0.8 Nezu-Nakagawa wake), legacy 는 `0.16/(LOG(H/ZBR)-1.)²` (-1.0). **동일 ZBR 이라도 `ICALTB` 분기 전환 시 유효 drag 이 바뀜** — 매뉴얼이 얼버무리는 실무 함정. `7.5` 하한(:538,:595,:839,:862)은 shallow·고조도 셀 drag 을 비물리적으로 clamp.

## 3. Wave-current BBL (:276-498)

파랑 존재 시 저면경계층. apparent roughness 증대 + ripple + analytic BBL 적분:
```fortran
ZBRE = ZBRE*(1 + 0.19*ustar_wc/ustar_c)     ! :305 Grant-Madsen형 apparent roughness
RIPAMP = 0.22/TAUE**0.16                      ! :328 ripple 진폭 (excess shear)
RIPSTP = 0.16/TAUE**0.04                      ! :329 ripple 경사
```
`:455-475` = in-BBL / above-BBL 대수 profile 혼합 analytic 적분(`CDTMPU`·`(1+ZDHZR)LOG(1+HZRDZ)`). 계보 = Christoffersen-Jonsson/Grant-Madsen (소스주석 미인용, attributable). SEDZLJ·`QQWV2≤1e-12` 셀은 BBL bypass (→ [[efdc_sedzlj]]).

## 4. Vegetation drag (:637-816)

internal-mode 식생저항:
```fortran
FXVEG = 0.25*CPVEGU*(DXP*(BDLPSQ*HVGT/PVEGZ)+...)*DXIU   ! :799  (0.25=0.5 drag×0.5 면평균)
```
`BDLPSQ` = stem density × diameter × Cd. macrophyte + rigid vegetation 분기.

## 5. Sub-grid channel friction (:819-873)
```fortran
STBXCH = 0.16/(LOG(HUDZBR)-1.)**2       ! :840  채널 부분 drag
CHANFRIC = ... (STBXCH + vegetation 결합, :847)   ! Hamrick 2002 (0-나눗셈 fix :27)
```

## 6. 하류 결합 (소비처, 재문서화 아님)

| 산출 | 소비처 | 형태 |
|---|---|---|
| STBX/STBY | `calpuv9c.f90:269-270` | implicit drag `RCX = 1/(1 + RITB*DELT*HUI*STBX*|u| + DELT*FXVEGE)` |
| STBX/STBY | `hdmt.f90:266-267,1170` | 저면응력 `TBX = STBX*√(VU²+u²)*u` (2차 stress) |
| TBX/TBY | sediment([[efdc_sedzlj]])·turbulence([[efdc_turbulence]] QQ(L,0)) | Shields 임계·bed TKE |

- **implicit/explicit 분배** `RITB/RITB1`(:111-122, first-call `ISITB`): `ISITB==2` 완전 implicit `CDLIMIT=100` vs `==0` 완전 explicit `CDLIMIT=0.5` — **한 플래그로 안정상한 200× 변동**.

## 7. 관련
- [[efdc_hydro_core]] — CALEXP/CALPUV/CALUVW momentum (STBX→RCX 소비), 본 노트가 상류 drag 공급
- [[efdc_external_mode_solver]] — 외부모드 수위 CG solve (RCX 반영)
- [[efdc_turbulence]] — MY2.5 (bed TBX→QQ(L,0) turbulent intensity)
- [[efdc_sedzlj]] — 저면응력 TBX 소비(Shields), wave BBL bypass
- **Primary**: Nezu-Nakagawa 1993 (wake param 0.2, :541) · Hamrick 1992/2001/2002 (:25,:27) · Grant-Madsen/Christoffersen-Jonsson (wave BBL, uncited-attributable).
