---
title: "처오름 정량화 — R2% 분해와 매개변수화 3종(Stockdon·Larson·Ghonim) 실식 + 모델의 두 경로(파라미터화 vs shoreline 해상)"
topic: swash-zone
canonical_source: self
citation_status: verified
verification_method: "[[02-theory]] §3.4 가 '계수는 본 노트에서 단언하지 않음 — 필요 시 원논문 full-read 후 별도 verified 승격' 으로 남긴 공백을 채운다. **원논문이 아니라 모델 구현을 출처로 삼는다** — ShorelineS Technical Manual v1.0 식 (73)(74)(75)(p.49)와 구현 `functions/dune_erosion.m:82-93` 을 **양쪽 다 읽어 일치를 확인**했다(snapshot f3ec863). 모델별 경로 구분은 각 모델 verified source-analysis 노트로 소급한다. 원논문(Stockdon et al. 2006 등)은 미판독이므로 §2 의 서술은 '이 형태로 구현돼 있다' 이지 '원논문이 이렇다' 가 아니다."
note_author: "Claude Opus 5"
note_date: 2026-09-22
related:
  - concepts/swash-zone/02-theory.md
  - concepts/swash-zone/04-code-and-tools.md
  - models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md
  - models/SWASH/source-analysis/swash-wetting-drying-runup.md
---

# 처오름 정량화

> [[02-theory]] §3.4 는 Hunt(1959)·Stockdon(2006)을 **문헌 인용만** 남기고 계수를 단언하지 않았다
> ("교과서 본문 미보유 — 원논문 full-read 후 별도 verified 승격"). 본 노트가 그 공백을 채우되,
> **출처가 원논문이 아니라 모델 구현**이라는 점을 먼저 밝힌다.

## 1. $R_{2\%}$ 는 무엇을 재는가

처오름 높이는 단일 값이 아니라 분포다. 설계·경보에 쓰는 것은 **초과확률 2% 값** $R_{2\%}$ 다
([[02-theory]] §3.1).

분해는 둘로 한다.

$$R_{2\%} = \underbrace{\bar{\eta}}_{\text{setup}} + \underbrace{S/2}_{\text{swash}}, \qquad
S^2 = S_{inc}^2 + S_{IG}^2$$

- **setup** $\bar{\eta}$ — 쇄파로 해안에 물이 쌓여 생기는 평균수위 상승. 정상 성분
- **swash** $S$ — 그 위를 오르내리는 변동. **입사파대역**($S_{inc}$)과 **저주파(IG)**($S_{IG}$)의 제곱합

완경사·소산성 해빈일수록 $S_{IG}$ 가 지배한다 — [[02-theory]] §2.2 의 reflective/dissipative 구분과 같은 축이다.

## 2. 매개변수화 3종 — ShorelineS 구현 기준

아래 식은 **ShorelineS Technical Manual v1.0 (p.49, 식 73–75)** 과 구현
`functions/dune_erosion.m:82-93` 이 **일치함을 양쪽 읽어 확인한 것**이다.
원논문은 판독하지 않았으므로 "이 모델이 이 형태로 구현했다" 까지만 말한다.

공통 인자: $\sqrt{H_0 L_0}$ (심해 파고·파장), `slope` = 해빈경사.

| 형태 | 식 | 경사 의존 | 매뉴얼 설명 |
|---|---|---|---|
| **Stockdon (2006)** | $R = 1.1\sqrt{H_0L_0}\left(0.35\,\beta + \frac{\sqrt{0.563\beta^2 + 0.004}}{2}\right)$ | **있음** | 기본 선택 |
| **Larson et al. (2016)** | $R = 0.158\sqrt{H_0L_0}$ | **없음** | 경사 무관 → 완경사+해일에서 **과대** 위험. 급경사·협소 해빈용 |
| **Ghonim (2019)** | $R = \beta\sqrt{H_0L_0}$ | 있음 | Larson 형에 경사를 넣은 것. 넓은 해빈에서 Stockdon 과 비슷한 값 |

Stockdon 형은 괄호 안에서 **setup 항**($0.35\beta$)과 **swash 항**($\sqrt{0.563\beta^2+0.004}/2$)이
그대로 §1 의 분해에 대응한다. $\beta \to 0$ 에서 swash 항이 $\sqrt{0.004}/2$ 로 남는 것이
소산성 해빈의 IG 지배를 표현한다.

**경사 자체도 모델이 만든다.** ShorelineS 는 사구 발끝고/berm 폭에서
$\beta = \mathrm{clamp}(D_f/(W_{berm}-W_{berm,min}),\ 0.001,\ 0.5)$ 로 산출한다(`dune_erosion.m:81`).
즉 같은 "Stockdon 식" 이라도 $\beta$ 정의가 모델마다 다르면 값이 달라진다.

### ★ 인식하지 못한 이름은 조용히 Larson 이 된다

`dune_erosion.m:82-93` 의 분기는 `'sto'` → Stockdon, `'gho'` → Ghonim, **그 외 전부** → Larson 이다.
`runupform` 기본값은 `'Stockdon'` 이지만(Appendix B), **오타를 내면 오류가 아니라 Larson 이 적용된다.**
Larson 은 경사 무관이라 완경사 해빈에서 과대 처오름을 주므로 조용한 오적용의 대가가 크다.

대비되는 설계가 있다 — ADCIRC 의 얼음 항력법은 인식하지 못한 이름에
`terminate(ADCIRC_EXIT_FAILURE)` 를 낸다([[../../models/ADCIRC/manual-notes/19-ice-coverage]] §4-②).
**같은 "문자열로 공식 선택" 패턴인데 실패 처리가 정반대다.**

## 3. 모델이 처오름을 얻는 두 경로

| 경로 | 방식 | 대표 | 한계 |
|---|---|---|---|
| **A. 매개변수화** | $H_0$·$L_0$·$\beta$ 로 $R$ 을 계산해 사구 침식·월류 판정에 넣는다 | ShorelineS(`dune_erosion.m`) | 식이 교정된 조건 밖에서 외삽. 경사 정의에 민감 |
| **B. shoreline 해상** | 침수-건조 마스크로 물가선을 직접 추적해 처오름을 **결과로** 얻는다 | SWASH([[../../models/SWASH/source-analysis/swash-wetting-drying-runup]]), XBeach-NH, FUNWAVE, Celeris | 격자·시간 해상도 비용. 쇄파·마찰 설정에 민감 |

[[04-code-and-tools]] 의 모델 계열 비교가 B 경로 모델들을 다룬다 — 본 노트는 **A와 B의 성격 차이**만 세운다.

핵심은 **A는 $R_{2\%}$ 를 입력으로 받고 B는 출력으로 낸다**는 것이다. A 계열 모델에서 처오름은
가정이며, 그 가정이 틀리면 하류의 사구 침식·월류가 통째로 틀린다.

## 4. 남은 것

- **원논문 미판독**: Stockdon et al. (2006)·Larson et al. (2016)·Ghonim (2019) 원문을 읽지 않았다.
  계수의 적용범위(교정 해빈·파랑조건)는 본 노트가 말할 수 없다. 읽으면 §2 를 원문 기준으로 승격한다.
- **$S_{inc}$·$S_{IG}$ 분리 계측**: 관측·모델 시계열에서 스펙트럼으로 가르는 방법은 미작성
  (README 가 예정한 `scalogram`·shoreline tracking).
- **모델 간 $\beta$ 정의 차이**: ShorelineS 만 확인했다. 다른 모델이 어떤 경사를 쓰는지는 미조사.
