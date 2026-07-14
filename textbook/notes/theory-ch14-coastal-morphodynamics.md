---
title: "이론 ch14 — 해안 형태동역학: 균형 단면 · 계절 단면·Dean number · 연안 표사 · closure · 표사 수지 · Bruun · 구조물 · 양빈"
topic: coast
layer: 1
depends_on: []
canonical_source: self
citation_status: verified
provenance: "교재 프로젝트 textbook-ai-data-full ch14(AI 합성 MDX, 무인용) 이식분 — 2026-07-14 원자 단언 분해·(source_id, page) 부착 + 같은 날 게이트 ⓒ 2차(Codex 8회차) MODIFY 반영. ★원문 오기 1건 정정 복원: Hallermeier closure 2차항 '10.9'→**68.5**(coastal-structures-design p.127 Eq.3 실존 — 초판 '공식 미전사'는 인접 페이지 재검색 누락 오판). 게이트 ⓒ 2차 복원 3건: Hallermeier 식·salient/tombolo 정성 조건(CP p.11·30)·GENESIS/SBEACH 제한적 활용(CSD p.149; '코퍼스 0건' 철회). CERC 상세는 ch13 §8 과의 복제 제거 — depends_on ch13 탐색 강등. 미매칭 삭제/미이식: one-line 확산방정식 유도(Pelnard-Considère)·Dean h=Ax^{2/3} 명시식·A(d) 수치표·CERC K 계수값·Kamphuis 명시식·Dean number 임계표·Bruun 정량식·양빈 손실률 5-10%/년·salient 정량 임계비. 원문 연도 '(Bruun) 1954'·'Dean 1973/1977' 미지지, 'Komar 1998'=서지 실존(CSD p.157)·claim-level 미지지. 워크 계산·한국 사례·수치모델 비교표는 이론 아님 — concepts/models 탐색 위임. T6([THEORY-LEDGER](../THEORY-LEDGER.md))."
verification_method: "coastal-processes-with-eng-apps(Dean & Dalrymple) p.11-12·26-27·30(영문 생존 구간; ※미러=35p 부분본 판정) + mechanics-of-sediment-transport p.797-799(§16.5.2-16.5.3) + coastal-structures-design p.124-127·130-133·145·149·157·159 + coastal-eng-guidelines p.27·50-51·93·97-98 + marine-sands-manual p.198-199 — textbook/md 미러 페이지 직접 대조 (2026-07-14, 게이트 ⓒ 2차 재검증 포함)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-14
related:
  - textbook/notes/theory-ch13-sediment-transport.md
  - textbook/notes/theory-ch10-coastal-transformation.md
  - concepts/littoral-drift/01-concept.md
  - concepts/sediment-transport/01-concept.md
---

# 해안 형태동역학 — 균형 단면·계절 변화·연안 표사·해수면 응답·구조물·양빈

> 4-레이어 **① 이론** 노트. 입자 스케일 이송([[theory-ch13-sediment-transport]])이 단면·해안선 스케일 진화로 연결되는 층.
> 탐색 링크(근거 의존 아님): 이송 공식 canonical [[theory-ch13-sediment-transport]] §8 · 연안류 [[theory-ch10-coastal-transformation]] · 도메인 `concepts/littoral-drift/`·`concepts/sediment-transport/` · 형태 수치모델 구현 `models/`(XBeach·Delft3D 등). (게이트 ⓒ 2차: 본 장 단언은 전부 1차 출처 직접 앵커 — ch13 근거 의존 아님.)

## 1. 균형 단면 (equilibrium beach profile)

- **정의**: 주어진 입경·파랑·조석 조건에는 고유한 균형 단면이 존재 — 모래 알갱이에 작용하는 **건설력(constructive)과 파괴력(destructive)의 균형** 상태. 조건(수위·파고·주기)이 바뀌면 이전 단면은 **새 균형을 향해 진화** (coastal-processes-with-eng-apps, p.26, §3.3).
- 무파 조건이면 단면은 안식각(약 32°) 사면 — 실제 해빈은 파 작용 때문에 그보다 훨씬 완만한 **위로 오목한** 형태 (coastal-processes-with-eng-apps, p.26).
- **동역학 그림(neutral line → 동적 균형)**: 중립선 안쪽 입자는 육지 쪽, 바깥 입자는 외해 쪽으로 이동하다가 사면 각 점에서 파 항력과 입자 무게의 사면 성분이 평형이 되면 **동적 균형 단면** 도달 — 해안 가까울수록 파력이 커서 **경사가 가파르고 입자가 조립** (mechanics-of-sediment-transport, p.797-798, §16.5.2-16.5.3).
- **경험 관계 4종** (coastal-processes-with-eng-apps, p.26-27): ①조립 입경 ↔ 가파른 경사(Beach Erosion Board 1933 뉴저지·**Bascom 1951** 캘리포니아 정상관) ②파고 증가 → 완만화(파괴력 증가+쇄파대 확폭) ③주기 증가 → 육지향 이송·전진·가파른 경사 ④**수위 상승 → 외해 이송 + 단면이 연직 상승·육지 쪽 이동 = 해안선 후퇴**.
- 균형 단면 이론의 현대 계보는 **Dean(1991) "Equilibrium beach profiles: characteristics and applications"** 리뷰 — 양빈 설계에서 "투입 모래가 평형 경사로 재배치된다" 는 전제의 근거 문헌 (coastal-structures-design, p.125 본문 인용·p.157 서지). ※원문 교재의 명시식 $h=Ax^{2/3}$·유도(균일 에너지 소산)·$A(d)$ 수치표·"Dean 1977" 연도는 코퍼스 미확인 — 미전사.

## 2. 계절 단면 변화와 Dean number

- **겨울(폭풍) 단면**: 강한 폭풍이 물가(foreshore)를 침식 → 외해 퇴적, **쇄파대에 bar 형성**. **여름 단면**: 약한 파 조건에서 입자가 육지향 이동, foreshore 퇴적·bar 소멸 (mechanics-of-sediment-transport, p.798-799, Fig. 16.45 "Typical beach profiles").
- 이 **beach cycle** 개념 계보는 Scripps 해양연구소의 캘리포니아 연안 onshore/offshore 이송 연구 — 계절적이지만 실제로는 **폭풍 통과가 지배**해 주~월 시간 스케일로 작동; 폭풍 후 swash 대 완경사+dry beach 의 연직 escarpment, 정온기 후 넓은 dry beach 가 특징 (coastal-structures-design, p.133). 시간 스케일 관점: 지형 분류는 십년 스케일, 폭풍 수위·파랑이 단기 해안선 위치를 통제 (p.133).
- **Dean number** $D \equiv \dfrac{H_b}{wT}$ — 쇄파고·침강속도·주기의 무차원 조합으로 단면 응답을 기술 (coastal-processes-with-eng-apps, p.26, Eq. 3.1); 명명 유래는 Suh & Dalrymple(1987) (p.27 각주). 병용 무차원수: **surf similarity parameter**(Battjes 1974) $\zeta=\tan\beta/\sqrt{H_0/L_0}$, Froude 형 $F=w/\sqrt{gH_b}$ (p.26-27, Eq. 3.2-3.3).
- ※원문 교재의 임계값 표($\Omega<1$ reflective / $1{-}6$ 천이 / $>6$ dissipative)는 코퍼스 미확인 — 미이식.

## 3. 연안 표사 (longshore transport)

- 이송 공식의 canonical 은 [[theory-ch13-sediment-transport]] §8 — CERC 공식(기원·최단순형·적용 한계)과 보정 계보(Kamphuis 1991 등)는 그쪽에서 인용·서술하며 **본 장은 재서술하지 않음**(claim 복제 금지; 게이트 ⓒ 2차로 중복 단언 제거·탐색 링크 전환).
- 구동 물리(radiation stress → 연안류)는 [[theory-ch10-coastal-transformation]] §5-6 (탐색). ※원문 교재의 CERC $K$ 계수값(0.39-0.77)·Kamphuis 명시식·정확한 $H_b^{5/2}\sin(2\alpha_b)$ 전사는 미러 문자 대조 불가 — 미전사(ch13 §8 의 출처 기술 참조).

## 4. 표사 활동 한계 수심 (depth of closure)

- 해빈·근해의 **활성 폭·활성 수심** 산정이 양빈·단면 분석의 선행 절차 — 산정 기법의 표준 참조가 **Hallermeier(1981)** (coastal-eng-guidelines, p.98).
- **실측 정의**: 반복 측량 단면들의 고도 표준편차 $\sigma_i$ 가 외해로 가며 0 에 접근·유지되는 수심 = **DOC(depth of closure)** — 그 너머는 단면 변화가 유의하지 않음 (coastal-structures-design, p.125-126, Fig. 2). 양빈 단위부피 산정도 DOC 까지의 연직 기둥으로 정의 (p.145, Fig. 12).
- **Hallermeier 경험식**: $d_{n1} = 2.28\,H_e - 68.5\,\dfrac{H_e^2}{g\,T_e^2}$ — $H_e$ = 연중 12시간만 초과되는 근해 폭풍파고("12-hour" wave), $T_e$ = 그 동반 주기 (coastal-structures-design, p.127, Eq. 3). ★원문 교재의 2차항 계수 "10.9" 는 오기 — 출처 기준 **68.5 로 정정 복원**(게이트 ⓒ 2차; 초판 '공식 전체 미전사'는 인접 페이지 재검색 누락 오판). ※전형값 4-8 m 는 코퍼스 미확인 — 미이식.

## 5. 표사 수지(sediment budget)와 셀

- 양빈·침식 평가의 중심은 **littoral system 의 경계 식별과 sediment budget**: 공급원(하천·근해 퇴적체) 유무, pocket beach 인지 광역 littoral system 의 일부인지, 시스템 경계가 어디인지가 선행 질문 (coastal-eng-guidelines, p.97-98, "Morphology"·"Sediment budget" 절).
- **형태 지표로 경계·방향 읽기**: sand spit·cuspate foreland·**제티의 fillet**·섬 배후 **tombolo** 가 표사 이동의 형태학적 지표 — 국지 침식 문제는 흔히 인근 inlet·외해 사주 이동·인공 변경의 반영 (coastal-structures-design, p.132). 지형학적 개념 모델이 양빈 설계의 필수 틀 (p.132-133).
- ※원문 교재의 수지표(항목별 규모)는 코퍼스 미확인 — 미이식. "Komar 1998" 은 *Beach Processes and Sedimentation* 2판 서지가 실존하나(coastal-structures-design, p.157) 수지·셀 단언을 직접 귀속할 본문은 없음 — claim-level 미지지로 귀속 미이식(게이트 ⓒ 2차 표현 정정).

## 6. 해수면 상승 응답 — Bruun 계보

- **정성 메커니즘은 코퍼스 직접 지지**: 수위(조위) 상승 → 새 균형 단면 필요 → **단면이 연직으로 들려 육지 쪽으로 이동 = 해안선 후퇴 + 외해 방향 이송** (coastal-processes-with-eng-apps, p.27).
- 이 응답의 정량화 계보가 **Bruun(1962) "Sea-level rise as a cause of shore erosion"** (J. Waterways and Harbors Div., ASCE 88(WW1), 117-132) (coastal-structures-design, p.159, 서지). ※원문 교재의 정량식 $R = S\,L_*/(h_*+B)$·유도·"1954 분류 체계" 연혁은 코퍼스 미확인 — 미전사(한계 논의 포함 order-of-magnitude 용법은 위 정성 근거 수준으로만 이식).

## 7. 해안 구조물 영향

- **연안 이송 차단 구조물(groyne·항 입구·도류제)**: **updrift 퇴적 + downdrift 침식** (marine-sands-manual, p.198). 미국 사례에서 groin 은 강한 연안 이송 구역에서 가장 잘 기능 — 두 groin 으로 침식 해안 안정화 사례 (coastal-processes-with-eng-apps, p.12, 영문 예제 본문).
- **TOMBOLO** = 섬을 본토(또는 다른 섬)에 잇는 bar/spit (coastal-eng-guidelines, p.93 용어집). **형성 기구**: 섬(이안 구조물)의 파 차폐로 파봉이 차폐역 쪽으로 만곡 → 배후에 퇴적체가 성장해 섬-해안을 잇는 지상 연결 형성 — 해안→섬 또는 섬→해안 양방향 성장 가능 (coastal-processes-with-eng-apps, p.30, §Tombolos). 제티 fillet·tombolo 는 이송 방향 지표로도 사용 (coastal-structures-design, p.132).
- **이안 방파제 응답의 지배 변수**: 구조물과 자연계의 상호작용은 **마루고·연안 방향 길이·이안 거리**에 좌우 (coastal-processes-with-eng-apps, p.11) — ★초판 이식의 "salient 조건 코퍼스 미확인" 은 오판, 정성 조건 복원(게이트 ⓒ 2차). ※정량 임계비(길이/이안거리)는 코퍼스 미확인 — 미이식(설계 상세는 `concepts/waves/06`·KDS 축 탐색).
- 침식률이 **~5 m/yr 를 넘으면** 주기적 양빈만으로는 손실을 따라가기 어려움 — 구조물 병행 대안 검토 (coastal-structures-design, p.124).

## 8. 해빈 양빈 (beach nourishment/replenishment)

- 양빈은 seawall·revetment·groyne·이안제 등과 병렬되는 연안 공법 옵션 — 타 공법과의 조합 빈번 (coastal-eng-guidelines, p.27).
- **설계 전제 = 프로세스 이해**: 대상 해빈의 형태·공급원·경계·단면 이력·입도 분석이 적합성 평가·설계·비용산정의 중심 (coastal-eng-guidelines, p.97-98). 원빈(native) 표사 특성은 복합 채취·체분석($\phi_{84},\phi_{16},\phi_{50}$)·침강속도 실측으로 정량화 (p.98).
- **투입 후 거동**: dry beach 외측에 놓인 모래는 **균형 경사·surf-zone 형태로 신속 재배치**(cross-shore 평형화; Dean 1991 계보 인용) (coastal-structures-design, p.125). 설계는 해안선 단위길이당 부피(**fill density**)로 정량화 (p.130).
- **재보충(renourishment)**: 폭풍 후 반복 보충이 event-driven 유지관리 항목으로 표준화 (coastal-eng-guidelines, p.51). 계약기간 중에도 연안 프로세스가 투입 모래를 제거할 수 있음 (p.48).
- **입경 원칙**: 요구보다 **굵은 입경 선정**이 위험 저감 수단으로 명시 (coastal-eng-guidelines, p.50). ※원문 교재의 손실률 "5-10%/년" 수치는 코퍼스 미확인 — 미이식.
- **수치모델의 위상**: 해안선 진화의 복잡성 때문에 수치모델은 양빈 **예비설계 단계에는 통상 부적합** — 기본 형성안 완료 후 **최종설계 보조**로 유효. 실무에서 USACE 승인 모델 **GENESIS**(해안선)·**SBEACH**(단면)로 fill 의 확산(diffusion/dispersion)·구간별 성능을 시험한 사례 (coastal-structures-design, p.149; GENESIS 서지 p.159). ★초판 이식의 "one-line 계열 코퍼스 0건" 판정은 오판 — GENESIS 실존, 철회(게이트 ⓒ 2차). ※원문 교재의 one-line **확산방정식 유도**(Pelnard-Considère 계보·연안 확산계수 D)는 여전히 코퍼스 미확인 — 미이식. 모델별 비교(XBeach·Delft3D 등)는 모델 축 — `models/` 탐색 위임.

## 9. 역사 연표 (코퍼스 실측분)

Bascom 1951 입경-경사 정상관 (coastal-processes-with-eng-apps, p.26) → Scripps 그룹 summer/winter beach 개념 (coastal-structures-design, p.133) → **Bruun 1962** 해수면 상승-침식 (p.159 서지) → **Battjes 1974** surf similarity (coastal-processes-with-eng-apps, p.27) → **Hallermeier 1981** 활성 한계 수심 (coastal-eng-guidelines, p.98; 경험식 coastal-structures-design, p.127) → **SPM/CERC 1984** 표준화 (marine-sands-manual, p.198) → **Suh & Dalrymple 1987** Dean number 명명 (coastal-processes-with-eng-apps, p.27 각주) → **Dean 1991** 균형 단면 리뷰 (coastal-structures-design, p.157) → **Kamphuis 1991** 보정 공식 (marine-sands-manual, p.199). ※원문 교재의 "Bruun 1954"·"Dean 1973/1977"·"Komar 1998"·"Roelvink 2009(XBeach)" 는 코퍼스 미지지 또는 모델 축 — 미이식.

## 10. 연결

- [[theory-ch13-sediment-transport]] — 이송 공식·CERC canonical (탐색 — 게이트 ⓒ 2차로 근거 의존에서 강등)
- [[theory-ch10-coastal-transformation]] — radiation stress·연안류 (탐색)
- `concepts/littoral-drift/`·`concepts/sediment-transport/`·`concepts/waves/06` — 도메인·설계·한국 사례 (탐색)
- 다음: 기초 챕터(00.5-07) 또는 ch11/15 claim-level 분해 (T 트랙).
