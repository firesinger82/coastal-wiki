---
title: "조류 — 01 개념"
topic: currents
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "AI cross-reference against khoa-portcals-glossary (KHOA·PORTCALS 용어집) + textbook/md/stewart_textbook.md (§17.4 p.313) + textbook/md/134340780-Tides-and-Currents.md (Lubbad p.50). 15개 KHOA glossary term needle lookup PASS. §7 천해 비선형 효과 출처 보강(2026-06-21, L4 자가 감사 적발): M4/MS4/M6 overtide 생성 = Pugh sea-level L4461-4471(2차→4th-diurnal, 3차→6th-diurnal), 분조 목록 = tides/03-analysis-methods + tides-foreman1977-appendix note, 서해 우세 = tides-khoa-nonharmonic-research note."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 조류 — 01 개념

## 1. 정의

> **조류 (潮流, *tidal current* / *tidal stream*)**: 조석에 의한 해수면 높이 변화로 바닷물이 주기적으로 이동하는 **수평운동(흐름)**. 조류는 주기적으로 흐름 방향이 바뀌며, 일정한 방향으로 계속 흐르는 **해류(ocean current)와는 구별된다**. ([KHOA] 조류)

[PORTCALS] (추가): 조류는 해류와 달리 유향·유속이 시간에 따라 변하고 일정한 시간이 지나면 원래 상태가 됨. **연안에서는 보통 조류가 해류보다 더 강함**.

영문 일반 표기: *tidal current* (미국·국제). *tidal stream* (영국).

### 1.1 강도 (Stewart §17.4 p.313)

> "Tides produce strong currents in many parts of the ocean. **Tidal currents can have speeds of up to 5 m/s in coastal waters**, impeding navigation and mixing coastal waters." (`stewart-physical-ocean`, p.313)

조류의 해양적 역할 (Stewart §17.4 p.313-314):
1. 강한 흐름 (외해 0.1 m/s, 연안 1-2 m/s, 극단 5 m/s)
2. 해산·대륙사면·중앙해령 위에서 **내부파 생성** → 해양 혼합 주요 동력
3. 심해 저서 퇴적물 부유 가능
4. 조석 혼합이 심층 순환 영향

## 2. 조류 분류

### 2.1 시간적 분류 — 창조·낙조·정조·게류

| 한국어 | 한자 | 영문 | 정의 |
|---|---|---|---|
| 창조류 | 漲潮流 | flood current | 저조에서 고조로 해수면이 높아질 때 흐르는 조류. **해안에서는 바다→육지**, 수로에서는 상류 방향. ([KHOA] 창조류) |
| 낙조류 | 落潮流 | ebb current | 고조에서 저조로 해수면이 낮아질 때 흐르는 조류. **해안에서는 육지→바다**. ([KHOA] 낙조류) |
| 정조 | 停潮 | slack tide / stand of tide | 고조 또는 저조 전후, 해면 승강이 매우 느려 거의 정지 상태. 조차 작을 때가 길게 나타남. ([KHOA] 정조, [PORTCALS] 정조) |
| 게류 | 憩流 | slack water | 창조류·낙조류 흐름 방향이 바뀔 때 조류 흐름이 약하거나 거의 없는 상태. 전류시(轉流時)라고도 함. **하루에 4회 발생** (장소에 따라 2회). ([KHOA] 게류) |
| 최강창조류 | 最强漲潮流 | maximum flood current | 창조류 중 가장 빠른 유속 |
| 최강낙조류 | 最强落潮流 | maximum ebb current | 낙조류 중 가장 빠른 유속. 연안·만에서는 보통 고조→저조 중간에서 발생 ([KHOA] 최강낙조류) |

**중요 구분 — 정조 vs 게류** ([KHOA] 게류):
- **정조**: 조위(수직)의 변화가 없는 상태
- **게류**: 조류(수평)의 흐름이 멈춘 상태
- 이론상 정조 때 조류 유속이 최소가 되지만, **해저지형 등의 영향으로 게류는 조석의 정조 시간과 일치하지 않고 늦게 나타남**.

게류 전후 약 1시간 정도가 유속이 약함.

### 2.2 공간 패턴 — 왕복성·회전성

| 분류 | 영문 | 정의 |
|---|---|---|
| **왕복성조류** | reversing tidal current | 연안해역·좁은 수로에서 약 6시간 간격으로 창조류·낙조류가 **거의 일직선상에서 반대 방향**으로 흐름. 방향 전환 시 게류 (전류시) 발생. ([KHOA] 왕복성조류) |
| **회전성조류** | rotary tidal current | 외해·넓은 해역에서 시간에 따라 방향이 연속적으로 **회전**하며 흐름. 한국 동해 외해에서 관찰. (별도 보강) |

→ 조류타원 (current ellipse) 표현이 회전성 패턴의 자연 표현. `02-theory.md` §3 참조.

## 3. 조류 vs 해류 비교

| 항목 | 조류 (tidal current) | 해류 (ocean current) |
|---|---|---|
| 기원 | 조석 (천체 인력) | 바람·밀도 차·열염 | 
| 주기성 | 강함 (12.4 h, 24 h 등) | 약함 (계절·년 변동) |
| 방향 | 주기적으로 변함 | 비교적 일정 |
| 강도 | 연안에서 강함 (1-5 m/s) | 외해에서도 비교적 약함 (0.1-2 m/s) |
| 예측 | 분조 분해로 정확 예측 | 모델·관측 합성 |
| 출처 ([KHOA] 조류) | "연안에서는 보통 조류가 해류보다 더 강함" | |

한국 주요 해류 (별도 보강): 쿠로시오 해류 분지 → 동한해류·황해난류·동해 외해.

## 4. 조류 관측 (KHOA 표준)

> **조류관측 (tidal current observation)**: 조석에 의한 해수의 주기적 수평흐름인 조류의 유향·유속을 연속하여 관측. 파랑 등의 영향을 없애기 위해 **수심 3~10 m 층**에서 관측. 필요에 따라 층별 관측도. ([KHOA] 조류관측)

### 4.1 관측 기간 (KHOA 표준)

| 기간 | 용도 |
|---|---|
| **1주야 (25시간)** | 최소 — M₂·창낙조류 1주기 |
| **15주야** | 반월 (대조·소조 포함) |
| **30주야** | 1개월 (분조 좀 더 분리) |
| **6개월** | 다수 분조 분해 |

### 4.2 관측 장비

- 초기: 프로펠러식 기계식 유속계
- 현재: **ADCP (Acoustic Doppler Current Profiler)** — 음파 기반 층별 유속 관측
- KHOA 사용 기종: RCM-9, RDCP-600 등

→ 분석 방법 상세는 `03-analysis-methods.md`.

## 5. 조류 산출물 (KHOA 정의)

| 산출물 | 영문 | 정의 |
|---|---|---|
| **조류곡선** | tidal current variation curve | 조류의 시간적 변화 곡선 ([PORTCALS] 조류곡선) |
| **조류타원** | tidal current ellipse | 조석 주기(12시간 25분) 동안 조류 유향·유속을 벡터로 나타내고 끝을 연결한 타원. **반장축·반단축 크기, 장축 기울기, 회전 방향, 위상**으로 표현. 이를 통해 최강 창조류·낙조류의 크기·방향·시각 정보 산출. ([KHOA] 조류타원) |
| **조류도** | tidal current chart | 어느 지점에서 최강 창조류·낙조류 유향·유속과 시간별 유향·유속을 표시. 조류관측 자료를 분석한 **수치모델 결과** 토대. 국립해양조사원 주요 해역별 간행 ([KHOA]·[PORTCALS] 조류도) |
| **조류표** | Tidal Current Table | 주요 해역 매일 전류시간·최강 창조류·낙조류 시간·유속·유향 예측 정보. **국립해양조사원 매년 간행** ([KHOA] 조류표) |
| **조류예보** | tidal current prediction | 매일의 전류시각, 최강 창조류·낙조류 시각·유향·유속, 시간별 유향·유속 예측. 관측 기반·수치모델 기반 두 방법 ([KHOA] 조류예보) |
| **등조류선** | co-current line | 조류 유속·유향을 동시 측정한 동서·남북 성분의 시간 변화 곡선에서 한 점의 각 시각 속도 벡터의 정점을 연결한 선 ([KHOA] 등조류선) |

## 6. 도서 vs 좁은 수로 — 특성 차이 (Lubbad 2009 p.50)

조류 패턴은 지형에 따라 다름 ([`textbook/notes/tides-lubbad2009-overview.md`](../../textbook/notes/tides-lubbad2009-overview.md) §7):

- **큰 만 + 큰 입구**: 조류 약함 (단면 큼 → 가속 적음)
- **좁고 긴 만 또는 좁은 inlet**: 조류 **강함** (단면 수축 → 가속)

베르누이·연속방정식에 의한 유속 증폭 — 한국 서해 수많은 만·수로에서 강한 조류 발생 (예: 명량해협, 진도해협).

## 7. 천해 비선형 효과

천해에서는 조위뿐 아니라 조류도 비선형이며, 그 핵심은 **천해 비선형 분조(overtide)**다. 분조 이론·식·검출은 조석 토픽이 canonical 홈이므로(CONVENTIONS §6) 여기서는 요약·연결만 한다.

- **M₄·MS₄·M₆** 등 천해 분조는 M₂·S₂의 비선형 상호작용으로 생성된다 — 2차(진폭 제곱) 상호작용이 4th-diurnal의 M₄·S₄·MS₄를, 3차 상호작용이 6th-diurnal의 M₆(3×M₂ speed)를 만든다(Pugh, *Sea Level*, 천해조석 비선형 상호작용 절: `textbook/md/sea-level.md` L4461–4471). 분조 목록·분석은 [[../tides/03-analysis-methods]](Foreman 1977 appendix: M3·M4·MS4·M6 등 비선형 분조) 및 [`textbook/notes/tides-foreman1977-appendix.md`](../../textbook/notes/tides-foreman1977-appendix.md) 참조.
- 이 천해 분조가 조류 곡선을 비대칭화한다 → **창·낙조류 비대칭**(창조류 우세 또는 낙조류 우세, 지형 의존). 한국 서해의 천해 분조 우세(M₄·MS₄ 강함)는 KHOA 조화상수로 관측된다([`textbook/notes/tides-khoa-nonharmonic-research.md`](../../textbook/notes/tides-khoa-nonharmonic-research.md) §천해 분조 비율, [`concepts/tides/04-code-and-tools.md`](../tides/04-code-and-tools.md) L343).
- 창·낙조류 비대칭은 표사 이동 순(net)방향 결정의 주요 인자다(← `concepts/sediment-transport/` 작성 시 cross-link).

## 8. 보강·미해결

- **한국 해역별 조류 패턴 typical 값** (서해 강함, 동해 약함 등 정량)
- 한국 주요 해류 (쿠로시오 가지·동한해류·황해난류) 인용
- 회전성 조류의 Coriolis 의존성 정밀 — Stewart §10-11 또는 별도 source
- Lagrangian vs Eulerian 측정 ([KHOA] 라그랑주식해류측정·오일러식해류측정 등 별도 노트화)

## 9. 연결

- `02-theory.md` — 분조 분해·조류타원·dynamic 흐름
- `03-analysis-methods.md` — UTide 2D·ADCP·KHOA 관측 protocol
- `04-code-and-tools.md` — UTide 2D 출력·수치조류도 격자
- `05-examples.md` — 광역 수치조류도 데이터 활용
- `concepts/tides/` — 동일 분조 set, 위상 기준 G/g/κ
- 소스:
  - [`textbook/notes/tides-khoa-cross-verification.md`](../../textbook/notes/tides-khoa-cross-verification.md) §5 — 수치조류도 단위 (cm/s) 검증
  - [`textbook/notes/tides-lubbad2009-overview.md`](../../textbook/notes/tides-lubbad2009-overview.md) §7 — 조류 in inlets
  - KHOA glossary — 60+ 조류 용어
