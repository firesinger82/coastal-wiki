---
title: "XBeach Beach Wizard(beachwizard.F90) — 관측 파 celerity/wavenumber(Argus 영상·radar) 동화로 bathymetry 갱신(depth inversion + Kalman-류 보정)"
topic: xbeach
canonical_source: self
citation_status: verified
verification_method: "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/beachwizard.F90 (806) 직접 read — cobs(관측 celerity)/ccom(계산 celerity)/ccmco(차이)/sigC(불확실성)/tradar(radar 주기)/bwinit(80) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — celerity 동화 bathymetry 갱신 구조 verbatim"
verification_date: 2026-06-03
related:
  - models/XBeach/source-analysis/xbeach_morphology.md
  - models/XBeach/source-analysis/xbeach-bathymetry-input-foundation.md
---

# XBeach Beach Wizard (beachwizard.F90)

> `beachwizard.F90`(806) 직접 read. **관측 파 celerity 동화(data assimilation)로 bathymetry 추정·갱신** 모듈. Argus 비디오/radar 로 측정한 파 전파속도(celerity)·wavenumber 를 분산관계로 역산 → 수심 보정. 직접 측량 어려운 surfzone bathymetry 를 원격관측으로 update.

## 1. 원리 — celerity → depth inversion

선형 분산관계 `c² = (g/k)·tanh(kh)` 에서 **관측 celerity c_obs 로 수심 h 역산**:
- `cobs`(관측 celerity, 영상/radar), `ccom`(모델 계산 celerity, 현 bathymetry), `ccmco = ccom − cobs`(차이).
- 차이를 줄이는 방향으로 bathymetry 보정(얕으면 c 작음 → c 차이로 깊이 조정).

## 2. 불확실성 가중 (Kalman-류)

- `sigC`(celerity 관측 표준편차)·`sigCdef`(기본 불확실성) — 관측 신뢰도 가중 보정(불확실한 관측은 약하게 반영). prior(현 bathymetry) + observation 의 가중 결합(Kalman update 형식).
- `tradar` = wavenumber/celerity 파일의 대표 주기.

## 3. 용도·위치

- **surfzone bathymetry 모니터링**: 측량선 접근 불가 쇄파역을 Argus 영상으로 시간연속 추정. morphology([[xbeach_morphology]])와 독립적(관측 동화 도구).
- niche(연구·관측소 운영). bwinit(:80) 초기화 후 관측 시계열 동화.

## 4. 연결

- [[xbeach_morphology]] — bathymetry 갱신(이쪽은 관측 동화, morphology 는 sediment 역학)
- [[xbeach-morphology-foundation]] — bathymetry 입력
- Aarninkhof / Holman (Argus video) / van Dongeren et al.(Beach Wizard) 계열
