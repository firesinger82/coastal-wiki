---
title: "EFDC 파라메트릭 태풍 바람장(mod_cyclone.f90) — Holland/Hubbert/McConochie/Willoughby 4 모델 + track 보간(Pc/Rmw/Vmax/B) + 이동속도 비대칭. storm-surge TC wind"
topic: efdc
canonical_source: self
citation_status: verified
verification_method: "models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mod_cyclone.f90 (658) 직접 read — ICYCLONE 1 Holland/2 Hubbert/3 McConochie/4 Willoughby(61), CycloneTrackPoint(Pc/Rmw/Vmax/B=2.5 Holland shape/Vfx·Vfy/delP/fcor 17-57), track interp(166), 이동속도 Vfm(206) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-04
verification_by: "Claude Opus 4.8 (1M context) — parametric cyclone 4 모델 verbatim"
verification_date: 2026-06-04
related:
  - models/EFDC/source-analysis/efdc_hydro_core.md
  - models/EFDC/manual-notes/efdc-theory-v12-ch2-hydrodynamics.md
  - concepts/storm-surge/
---

# EFDC 파라메트릭 태풍 바람장 (mod_cyclone.f90)

> `mod_cyclone.f90`(658, module `cyclone`) 직접 read. EFDC 의 **태풍(cyclone) 파라메트릭 바람·기압장** 생성 — best-track(중심위치·중심기압·최대풍반경)으로부터 wind/pressure 격자장 합성. storm-surge 모의의 외력(EFDC 가 surge 모델로 쓰일 때). 한국 연안 태풍 해일(Maemi/Hinnamnor 등) 직결.

## 1. 4 parametric 모델 (ICYCLONE, :61)

```fortran
ICYCLONE = 0 none / 1 Holland / 2 Hubbert / 3 McConochie / 4 Willoughby
```
- **Holland (1980)**: 표준 gradient wind profile. `B`(Holland shape parameter, default 2.5) 로 풍속 분포 sharpness 조절. central pressure deficit `delP = Pn − Pc`(외곽-중심 기압차)로 풍속 진폭.
- **Hubbert / McConochie / Willoughby (2006)**: 비대칭·이중 eyewall 등 개선 profile(Willoughby = dual-exponential 관측 fit).

## 2. Track point 자료 (CycloneTrackPoint, :17-28)

| 변수 | 의미 |
|---|---|
| `Pc` | 중심기압(hPa), default 1010 |
| `Rmw` | 최대풍반경(km) |
| `Vmax` | 최대풍속(m/s) |
| `B` | Holland shape(2.5) |
| `Vfx`/`Vfy` | 태풍 이동속도 x/y(m/s) |
| `delP`/`fcor` | 중심기압편차 / Coriolis |

- best-track(JSON `fson`)으로 시계열 입력. track 간 **선형 보간**(`factor`, :166)으로 매 step 현재 위치·강도.

## 3. 바람장 합성

- 거리 r(격자점↔태풍중심)로 gradient wind `V(r)` 산출(Holland: `V = √(B·delP/ρ·(Rmw/r)^B·exp(−(Rmw/r)^B) + (r·f/2)²) − r·f/2`).
- **이동 비대칭**: 태풍 이동속도 `Vfm = √(Vfx²+Vfy²)`(:206)를 더해 우측(북반구) 강풍 비대칭. inflow angle 회전.
- 기압장 `P(r) = Pc + delP·exp(−(Rmw/r)^B)` → 역기압(inverse barometer) 해일.
- → wind stress(C_D, [[efdc-theory-v12-ch2-hydrodynamics]] §wind drag)·기압 forcing 으로 [[efdc_hydro_core]] 운동량에 입력.

## 4. 위치

- EFDC 가 태풍 해일 모델일 때 외력 공급(관측 best-track → 격자 wind/pressure). 외부 wind 파일(OWI 등) 대안.
- [[concepts/storm-surge/01-concept]] 의 ADCIRC GAHM/AHM(parametric TC wind)과 같은 계열 — EFDC 측 구현.

## 5. 연결

- [[efdc_hydro_core]] — wind stress·기압 forcing → 운동량
- [[efdc-theory-v12-ch2-hydrodynamics]] — wind drag C_D
- [[concepts/storm-surge/01-concept]] — 태풍 해일(ADCIRC parametric wind 대응)
- Holland 1980 / Willoughby et al. 2006 / Hubbert et al. 1991
