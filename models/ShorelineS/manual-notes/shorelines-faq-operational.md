---
title: "ShorelineS FAQ 발췌 — 운영 파라미터·안정성 지침 (repo doc/ 동봉 FAQ PDF)"
model: ShorelineS
component: manual-notes
canonical_source: self
citation_status: verified
verification_method: "repo doc/'ShorelineS - frequently asked questions.pdf' pdftotext 추출·직접 read. 쪽번호 부재(FAQ 형식) — 질문 제목 단위로 인용. 수치·키워드 verbatim."
note_author: "Claude Fable 5"
note_date: 2026-07-18
related:
  - models/ShorelineS/README.md
  - models/ShorelineS/manual-notes/shorelines-roelvink2020-frontiers.md
  - models/ShorelineS/source-analysis/shorelines-transport-formulations.md
---

# FAQ 발췌 — 운영 지침 (사실상 사용자 매뉴얼)

> repo `doc/ShorelineS - frequently asked questions.pdf`. 인용 단위 = 질문 제목(쪽번호 없는 문서).

## 1. 격자 (Q "How to define the model grid?")

- **전형 `S.ds0` = 50–100 m**. "grid resolutions of ~10 meter pose some difficulties for a stable model run" — 10 m 급은 안정성 곤란 명시.
- regrid 방법 2종: 기본 `S.griddingmethod=2`(전체 재보간) / `=1`(초과 셀만 분할·병합 — 국소 세분 가능, `S.ds0=[x,y,ds;…]` 공간가변) — 코드 [make_sgrid_mc](../source-analysis/shorelines-diffraction-mud-topology.md) §3 METHOD 1/2 와 일치.
- `S.smoothfac`(griddingmethod 2 전용) 0–0.1, 기본 0 권장.

## 2. 시간 (Q "How to define begin and end time?")

- 기본 = 가변 timestep: `S.tc` 는 자동 dt 의 사용 비율(예 0.9). **입력 파랑조건 DT 와의 최솟값** 채택 — 파랑조건을 건너뛰지 않게 보장.
- 고정 dt: `S.tc=0` + `S.dt`[yr]. **전형 dt = 3시간~1일**. 고정 dt 사용 시 dt 내 파랑조건들을 **'에너지 벡터' 합산 평균**으로 집약.

## 3. 능동높이 (Q "What is the relevance of active height?")

- `S.d` = 내측 폐합수심~사구 기저(침식해안은 사구 포함) 수직거리 — m³/yr→m/yr 환산 분모(코드 h0). 공간가변 `[x,y,h;…]` 지원. "active profile height and the transport rate (scaling) are co-varying" — 캘리브 시 동시조정 경고.

## 4. 개방해안 경계 (Q "Which boundary conditions...")

`S.boundary_condition_start/end` = **closed**(또는 {closed, 25000 m³/yr} 고정수송) / **fixed**(=Neumann, 위치고정) / **angleconstant**(방위고정, 예 {angleconstant,310}) / **Periodic**(시-종점 수송 평균). 경계 셀 변화는 초기 해안방위에 수직 강제.

## 5. 고각도 불안정 (Q "Why do I get high-angle instabilities...")

- 물리 현상(≳40° 사각 입사 시 섭동 성장 — 스핏·undulation), 모델은 저→고각 전이점 인식 후 **직하류 점에 최대수송 적용**으로 캡(Sand Motor·나미비아 flying spit 재현 근거).
- 권장 `S.twopoints=1`(전이점 하류 2셀 분배로 매끄럽게), **`S.maxangle` 기본 60°**(셀 간 각도변화 상한).

## 6. 소격자 안정화 (Q "What options are there to make the model stable...")

- **`S.relaxationdistance`**[m]: 흐름 관성 — 강제력 급감 시 수송 즉시 정지 않고 감속거리 부여(<50 m 격자·고각도 상황 권장).
- **`S.smoothrefrac`**(0–1): TDP→쇄파점 파랑변환에 쓰는 해안방위의 이웃 평균화(소격자에서 국소 방위 요동→파랑 피드백 차단, 예 0.5).

## 7. 구조물·개입 (해당 Q 들 — 요지)

- groyne: 우회(bypass)+회절, 이안제: 회절+투과(수중 시), revetment: 별도 처리 Q 존재. 양빈=정례(rate)·shoreface(수중 berm, 확산계수는 네덜란드 해안 유도 [get_fnourishment_diffusion](../source-analysis/shorelines-diffraction-mud-topology.md) §4).
- 참고문헌 절에 Kamphuis 1992(ICCE) 등 — transport 공식 계보 문헌 리스트 존재.
