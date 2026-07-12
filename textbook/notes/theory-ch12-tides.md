---
title: "이론 ch12 — 조석: 평형 이론 · Laplace 동역학 · 조화 분석 · 해일 기초"
topic: tides
layer: 1
depends_on:
  - textbook/notes/theory-ch08-linear-waves.md
canonical_source: self
citation_status: verified
provenance: "교재 프로젝트 textbook-ai-data-full ch12(AI 합성 MDX, 무인용) 이식분 — 2026-07-12 원자 단언 분해 후 textbook/md 대조 (source_id, page) 부착. ★원문 오류 정정 3건: 예측기 1862→1873 · Doodson 1924→1921/1922(출처 간 표기 불일치 명기, stewart p.318-319 본문 vs sea-level p.74 서지) · 조석가속도 1.1e-6 g→11.2×10⁻⁸ g 정정 복원(sea-level p.78-79; 게이트 ⓒ ③으로 초판 '삭제'를 번복). 미매칭 삭제 4건(역기압 1cm/hPa 수치·대조/소조 조차 수치·전지구 조석모델 상품명·해일 사례 목록). 장파 판정은 sea-level p.156 직접 보강(게이트 ⓒ ②). 한국 연안 특성·도구·모델 목록은 이론 아님 — concepts 탐색 위임. T2([THEORY-LEDGER](../THEORY-LEDGER.md)), 게이트 ⓒ MODIFY 반영 완료."
verification_method: "sea-level(Pugh) p.16-18·69-79·98·109·112-113·124·155-156·166-167·179·197-198 + stewart-physical-ocean p.117·133·318-319·321·324 — textbook/md 미러 페이지 직접 대조 (2026-07-12, 게이트 ⓒ 재검증 포함)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-12
related:
  - concepts/tides/01-concept.md
  - textbook/notes/tides-stewart-ch17.md
  - textbook/notes/theory-ch08-linear-waves.md
---

# 조석 — 평형 이론 · 동역학 · 조화 분석

> 4-레이어 **① 이론** 노트. 조석 = 천체 인력 기원의 장주기 수면 변동 — 해수 운동은 연속·운동량 방정식을 따르므로 **장파로 전파**해야 함이 출처에 직접 명시 (sea-level, p.156, §5:1) → [[theory-ch08-linear-waves]] §4 의 **얕은물 한계**가 적용되는 장파(근거 의존 ①→①).
> 탐색 링크(근거 의존 아님): 도메인 요약·한국 연안 특성 `concepts/tides/`(01·02) · 조화분석 도구(UTide 등) `concepts/tides/04` · 해일 상세 `concepts/storm-surge/` · Stewart ch.17 발췌 [[tides-stewart-ch17]].

## 1. 기원 — 천체 인력과 평형 조석

- 정량 이론의 출발은 **Newton(1642-1727)의 만유인력** 적용 (sea-level, p.18). 대조(spring)가 삭·망 부근에 온다는 관찰 기록은 그 이전부터 존재 (sea-level, p.16).
- **조석력 유도** (sea-level, p.77, Eq. 3:2-3:3): 달을 향한 지점 P₁ 에는 달 쪽으로의 순힘 $2Gm_m a/R^3$, 반대쪽 P₂ 에는 달 반대쪽으로의 순힘(인력이 필요 가속보다 약함), 측면 P₃ 는 지구 중심 방향 — 결과는 **달-지구 축 방향으로 길쭉해진 평형 형상**, 즉 양쪽 부풀음(자전에 따라 반일주 성분).
- **조석 가속도 크기**: 달 기조력 가속도 ≈ **11.2×10⁻⁸ g** (Eq. 3:5 에 천문 상수 대입; "100 kg 인 사람이 P₁·P₂ 통과 시 11.2 mg 가벼워짐"), 태양 ≈ 5.2×10⁻⁸ g (sea-level, p.78-79). ★원문 교재의 "1.1×10⁻⁶ g" 는 자릿수 오류 — 출처 기준 **11.2×10⁻⁸ g 로 정정 복원**(게이트 ⓒ; 초판 이식의 '삭제' 처리를 번복).
- **태양 조석력 = 달의 0.46배** — 큰 질량이 거리 세제곱으로 상쇄 (sea-level, p.79). 대조·소조는 달·태양 강제의 합성/직교 배치에서 발생(삭망/현, p.16·79). ※원문 교재의 대조 5-10 m·소조 2-5 m 같은 조차 수치는 지역 의존 값이라 미이식.

## 2. 동역학 조석 — Laplace 조석방정식과 회전 효과

- 평형 이론은 해양의 즉시 응답을 가정 — 실제는 해분의 동역학 응답. **Laplace(1775)** 가 가속도·정수압을 결합한 동역학 정식화를 도입 (sea-level, p.109). 형태는 수심 평균 **얕은물 방정식 + Coriolis + 조석 강제** — 조석이 장파로 전파함은 출처 직접 명시 (sea-level, p.156), kh≪1 한계식은 [[theory-ch08-linear-waves]] §4.
- **Coriolis 매개변수** $f = 2\Omega\sin\phi$ — 회전 좌표계 운동량 방정식의 표준 항 (stewart-physical-ocean, p.133).
- **Amphidromic system**: 회전 해분의 조석 응답은 무조점(amphidrome) 중심의 회전 패턴 — cotidal line 이 무조점에서 방사, 최대 조차는 연안을 따라 분포 (stewart-physical-ocean, p.324; sea-level, p.166-167).
- **Kelvin wave**: 해안에 갇힌 장파 — **한 방향으로만 해안을 따라 전파**(남반구는 왼쪽 해안) (sea-level, p.166). **Poincaré wave**: 회전 지구에서 자유 전파하는 또 다른 장파 부류 (sea-level, p.179).
- 심해 조석은 위성 고도계로 관측되어 예측에 결합 (stewart-physical-ocean, p.321). ※원문 교재의 특정 전지구 모델 상품명 나열(TPXO/FES/OTPS)은 코퍼스 미확인 — 미이식.

## 3. 조화 분석

- 조위 시계열을 조화 성분 합으로 전개: $\eta(t) = Z_0 + \sum_i H_i\cos(\omega_i t - g_i)$ — **평형 조석의 조화 전개**가 §4:2 의 출발 (sea-level, p.98; nodal 보정 §4:2:2). 성분 결정은 **최소제곱 fitting** (sea-level, p.112-113).
- **주요 성분 주기** (stewart-physical-ocean, p.319 표): M₂ 12.4206 h · S₂ 12.0000 h · N₂ 12.6584 h (+K₁·O₁ 일주 성분 동일 표). 정밀 전개는 **Cartwright & Tayler(1971)** 계열 (sea-level, p.113).
- **Doodson 조화 전개·성분 명명 체계**: 조석 포텐셜을 6개 기본 천문 주파수의 Fourier 급수로 전개, 각 성분에 **Doodson number** $f=n_1f_1+\cdots+n_6f_6$ 부여 — 예: M₂ = 255.555 (stewart-physical-ocean, p.318-319, Eq. 17.17·Table 17.1). ※연도 표기는 출처 간 불일치 — Stewart 는 "Doodson (1922)"(p.319), Pugh 는 서지 목록에서 "Doodson (1921)"(sea-level, p.74; 본문 아닌 참고문헌 나열). ★원문 교재의 "1924" 는 어느 출처로도 미지지 — 오기.
- **얕은물 비선형 배음**: 천해에서 비선형성이 M₄·S₄ 등 4분일주(fourth-diurnal) 성분을 생성 — nodal 인자는 모성분의 곱을 따름, 예: $f(M_4)=f(M_2)\times f(M_2)$ (sea-level, p.124).
- 예측: 추출 성분으로 임의 미래 시점 합성 — 기계식 **조석 예측기는 Lord Kelvin & Edward Roberts, 1873** (sea-level, p.155 — ★원문 교재의 "1862" 는 오기, 출처 기준 정정).

## 4. 기상 기원 수위 변동(해일) 기초

- 해일 = 기상 강제(바람 응력·기압)가 조석 위에 더하는 수위 — 강제 목록에서 **inverted barometer 효과**(저기압→수위 상승)와 바람 응력이 주요 항 (stewart-physical-ocean, p.117). ※"1 hPa ≈ 1 cm" 정량 관계는 코퍼스에서 페이지 미확인 — 미이식(개념만).
- **바람 응력 법칙과 wind set-up**: 응력 법칙(stress laws) §6:4:1 과 바람 set-up §6:4:2 (sea-level, p.197-198) — 폐쇄/천해역에서 해안 방향 바람이 수면 경사를 세움.
- 상세(태풍 해일 역학·사례·수치모델)는 이론 범위 밖 — `concepts/storm-surge/`(탐색 링크)가 canonical.

## 5. 역사 연표 (코퍼스 실측분)

Newton 만유인력 기반 평형 조석(p.18) → **Laplace 1775** 동역학 정식화(p.109) → **Kelvin & Roberts 1873** 기계식 조석 예측기(p.155) → **Doodson 1921/1922** 성분 전개·명명(연도 표기 출처 간 불일치 — stewart-physical-ocean p.318-319 "1922" · sea-level p.74 서지 "1921") → **Cartwright & Tayler 1971** 현대적 재전개(p.113) → 위성 고도계 시대의 심해 조석 관측(stewart-physical-ocean, p.321). (모두 sea-level 페이지, 별도 표기 외.)

## 6. 연결

- [[theory-ch08-linear-waves]] — 얕은물 한계·장파 (근거 의존)
- [[tides-stewart-ch17]] — Stewart ch.17 기존 발췌 (탐색)
- `concepts/tides/` 01-04 — 도메인 요약·한국 연안·분석 도구 (탐색; 상세 이론 canonical 은 본 노트)
- 다음: ch09 비선형·스펙트럼 / ch13 표사 (T 트랙)
