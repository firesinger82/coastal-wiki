---
title: "FUNWAVE-TVD User's Manual (v3.0, 2016) 발췌"
model: FUNWAVE
citation_status: verified
verification_method: "doc/funwave_tvd_3.0.pdf → raw/manuals/funwave_tvd_3.0.md (opendataloader-pdf 변환) 직접 인용. 2026-06-13."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-13
---

# FUNWAVE-TVD User's Manual (v3.0) 발췌

> 출처: `doc/funwave_tvd_3.0.pdf` (Release Dec 2016) → `raw/manuals/funwave_tvd_3.0.md`(변환본, gitignore). 원 개발 Kirby et al. 1998.

## 1. Abstract (verbatim 요지)

완전비선형 Boussinesq(FUNWAVE, Kirby 1998 시초)의 신버전. 개선점:
1. **더 완전한 fully nonlinear Boussinesq 방정식 set**
2. **MUSCL-TVD solver + adaptive Runge-Kutta** time stepping
3. **viscosity 쇄파 + shock-capturing 쇄파** 둘 다
4. **wetting-drying** moving boundary (HLL 결합)
5. **parallel** computation 옵션

도출: conservation form 이론식 + 압력경사항 재배열(numerically **well-balanced**) + 수치scheme + 예제. 참조: Shi et al. 2012a(Cartesian) / Kirby et al. 2012(spherical).

## 2. 매뉴얼 구성 (TOC)

- §2 이론: 2.3 Cartesian conservative fully nonlinear Boussinesq / 2.4 spherical weakly nonlinear
- §3 수치: 3.6.1 Sponge layer / 3.7 Wavemaker(3.7.1 internal wavemaker theory)
- 예제 + benchmark

## 3. 버전 이력 (1.0→3.0)

- 1.0→1.1: grid nesting, wind effect, spherical 조파, 시간평균 properties
- 1.1→2.0: spherical 더 완전한 Boussinesq(Kirby 2012, weakly nonlinear, zα 기준). **`-DZALPHA`** 옵션(nesting scheme 개선: PHI_COLL·CAL_DISPERSION·GET_Eta_U_V tridiagonal BC)
- 2.0→2.1: **공간변화 friction**(friction matrix·Manning), 출력 효율
- 2.1→2.2: **sponge layer 개선** — LD-type가 TVD와 결합 시 2dx sawtooth noise 장기누적 → **friction-type·viscous-type sponge 추가**

## 4. 본 위키 연결

- 소스 구조: [`../source-analysis/funwave-source-map.md`](../source-analysis/funwave-source-map.md)
- 빌드(`-DZALPHA` 등 FLAG): [`../source-analysis/funwave-build-and-blackwell-port.md`](../source-analysis/funwave-build-and-blackwell-port.md)
- 입력(격자·수심·wavemaker): §3.7 wavemaker theory ↔ WK_IRR/WK_DATA2D ([`source-map`](../source-analysis/funwave-source-map.md) §3)
