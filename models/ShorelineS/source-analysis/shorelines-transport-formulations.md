---
title: "ShorelineS transport.m — 실제 7분기 공식(CERC1/2/3·KAMP·MILH·VR14·RAY·TIDEPROF)·회절 2차항·고각도 처리"
model: ShorelineS
component: functions/transport.m, get_Sphimax.m, get_timestep.m
canonical_source: self
citation_status: verified
verification_method: "sha 7bf4481ab — transport.m 237줄 전문·get_Sphimax.m 162줄·get_timestep.m 80줄 직접 read, 계수·식 verbatim 전사. 문서화(주석 :10 'CERC KAMP MILH CERC3 VR14')와 실분기(:140-220) 대조."
note_author: "Claude Fable 5"
note_date: 2026-07-17
related:
  - models/ShorelineS/source-analysis/shorelines-architecture-map.md
  - models/ShorelineS/source-analysis/shorelines-coastline-change.md
  - models/ShorelineS/manual-notes/shorelines-roelvink2020-frontiers.md
---

# transport.m — 연안표사 공식의 실체

> `transport.m`(237줄): QS [m³/yr, 공극 포함] 을 파랑조건(nw)×해안점(nq) 행렬로 계산. **문서화된 선택지(주석 :10)는 5종이지만 실분기는 7종**(+RAY·TIDEPROF).

## 1. 공식 분기 전수 (`transport.m:140-223`)

| trform | 라인 | 입력 H·각 | 식 (verbatim 요지) | 비고 |
|---|---|---|---|---|
| `CERC`/`CERC1` | :140-144 | **외해** HStdp·dPHItdp | `QS = qscal·b·H^2.5·(sin2φ − (2/tanbetasetup)cosφ·dHS)` | k=0.2 하드코딩(:141 — 주석: "SPM 값 0.39 는 typically quite high"). 계수 b 는 사용자 입력 |
| `CERC2` | :147-153 | 외해(공식 내 암묵 굴절) | `QS = qscal·365·24·3600·b2·H^{12/5}·Tp^{1/5}·(cos^{6/5}φ·sinφ − …dHS)` — b1 = k·ρw·g^0.5/(16√γ·(ρs−ρw)(1−p)) SPM 이론계수, b2 = b1·((γg)^0.5/2π)^0.2 (:149-150) | k=0.39(SPM) |
| `CERC3` | :156-162 | **쇄파점** HSbr·dPHIbr | `QS = qscal·365·24·3600·b3·g^0.5·γ^{-0.52}·HSbr^2.5·(sin2φbr − …dHS)` — b3 = k·ρw/(16(ρs−ρw)(1−p)) ≈0.023 (:158 주석) | k=0.35, Vitousek-Barnard 2015 계보(:155 주석) |
| `KAMP` | :165-171 | 쇄파 HSbr | 질량식 `2.33·ρs/(ρs−ρw)·Tp^1.5·tanβ^0.75·d50^{-0.25}·HSbr²·(|sin2φbr|^0.6·sign(φbr) − …dHS)` → 체적 `/(ρs(1−p))·yr` (:169-170) | Kamphuis. ★주석 이력: 구버전은 HStdp² — 현행 HSbr² (:167-169 3단 진화 주석) |
| `MILH` | :174-179 | 쇄파 HSbr | `0.15·ρs/(ρs−ρw)·Tp^0.89·tanβ^0.86·d50^{-0.69}·HSbr^2.75·|sin2φbr|^0.5·sign` (:177) | Mil-Homens 2013 재보정 Kamphuis |
| `VR14` | :182-192 | 쇄파 HSbr | `0.0006·kswell·ρs·tanβ^0.4·d50^{-0.6}·HSbr^2.6·v` , v=vwave=`0.3·(g·HSbr)^0.5·(sin2φbr − …dHS)`(:187), kswell=`0.015·pswell+(1−0.01·pswell)`(:184) | Van Rijn 2014. vtide=0 하드(:183 — 조석류 유속 미가산) |
| `RAY` | :194-197 | — | s-φ 곡선: `QS = −c1·φ·exp(−(c2·φ)²)+QSoffset` + 해석적 dQS/dφ(:197) | 외부 ray 결과 이식용 |
| `TIDEPROF` | :199-220 | 조석+파랑 | `transport_tidewave` 단면적분(정점별 루프) — Baldock 소산 α=1.0·γ=0.78 기본(:200-201), submerged groyne 시 `transport_groynesubmerged` 로 단면 재분배(:213-219) | 유일하게 단면(cross-shore) 해상 |

- 공통: `QS(|φ|>90°)=0`(전 분기)·`qscal` 전역 보정계수·출력 m³/yr 공극 포함(질량식은 `/(1−porosity)` 환산).
- 무효 trform → 경고만 출력(:222) — QS=0 유지(fail-soft).

## 2. 회절 2차항 dHS (`transport.m:102-122`)

회절 ON + QS 모드일 때 파고 연안경사 `dHS=(HS(i+1)−HS(i−1))/dist`(:117)를 **모든 공식의 각도항에 `−(2/tanbetasetup)·cosφ·dHS` 로 가산** — 구조물 배후 파고경사가 유발하는 순환류 수송(구버전 계수 `−2cosφ` 에서 setup 경사 반영형으로 개정된 이력이 주석 대비로 남음, 예 :142-143). CERC1/2·KAMP·MILH 는 HStdp 기반, 나머지는 HSbr 기반 dHS(:106-108).

## 3. 고각도 불안정 처리 (`transport.m:124-137` + `get_Sphimax.m`)

- `suppresshighangle==1`: `dPHItdp>dPHIcrit` 인 점의 각도를 임계각으로 클램프(:134-135)·dHS 무효화(:128)·|φ|>90° 파고 0(:132) — Ashton 계열 upwind 처리의 각도판.
- **임계각·QSmax 산출**(`get_Sphimax.m:86-150`): φ=35°/45° 두 계산 + 반복 **포물선(2차) 피팅 최대화**(3점 quadratic fit `A\B`, 꼭짓점 `−a2/(2a1)`, ≤10회) — 셀별 수송 최대 각도(공식별로 다름)를 수치적으로 탐색. QSmax 는 적응 dt 에도 사용.

## 4. 적응 시간간격 (`get_timestep.m:51-77`)

- `adt = dsmin²·h0min/(4·max|QSmax|)`(:61) — one-line **확산 안정성 기준**(확산계수 ∝ QSmax/h0). 파랑조건 다중이면 확률가중 합(:58-59).
- 안전장치: 하한 1분(:66)·초기 스텝 상한 1일(:75)·직전 스텝 대비 ×100/÷1000 클램프(:72-73)·다중 섹션 최솟값(:68). `tc<0` 이면 고정 dt(:52).
