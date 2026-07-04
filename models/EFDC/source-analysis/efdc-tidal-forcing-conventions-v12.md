---
title: "EFDC+ v12.4 조석·바람 강제력 규약 — C17 PFAM/PFPH 절대시간 합성, nodal 보정 부재, wser ISWDINT"
topic: tides
canonical_source: self
citation_status: verified
verification_method: "EFDC+ v12.4 소스 직접 read — input.f90(C17 read/변환·wser read)·setopenbc.f90(런타임 합성)·hdmt.f90(TIMESEC 초기화)·cellmask.f90·caltsxy.f90 file:line 전부 2026-07-04 재확인. nodal 부재는 전 .f90 'nodal' grep 0건 + PFAM 소비처 전수 grep으로 확인. 위상 페어링·fallback 정확도는 efdc_settings_gui 2026-07 감사에서 utide 대조 실증(적대 교차리뷰 통과)."
note_author: "Claude Fable 5 (2026-07 efdc_settings_gui 감사 결과 정리)"
note_date: 2026-07-04
verification_by: "Claude Fable 5 — v12.4 소스 file:line 직접 확인 + utide 교차검증 (2026-07 감사)"
verification_date: 2026-07-04
related:
  - models/EFDC/source-analysis/efdc_boundary_conditions.md
  - models/EFDC/source-analysis/efdc-boundary-condition-foundation.md
  - models/EFDC/source-analysis/efdc_cyclone_wind.md
  - models/EFDC/manual-notes/efdc-implementation-guide.md
  - models/EFDC/manual-notes/efdc-user-manual-r850.md
---

# EFDC+ v12.4 조석·바람 강제력 규약

> **Canonical source: self.** C17 조화 조석 경계(`PFAM`/`PFPH`)와 `wser.inp` 바람 입력을 v12.4가 **실제로 어떻게 소비하는지**를 소스 file:line 으로 고정한 규약 노트. R8.5.0 매뉴얼(2020-21) 서술과의 드리프트 주석은 [[efdc-implementation-guide]]·[[efdc-user-manual-r850]]의 ⚠️ 블록 참조. PSER/SETBCS/SETOPENBC 전체 경계조건 파이프라인은 [[efdc_boundary_conditions]]가 canonical.

## 1. C17 PFAM/PFPH 소비 체인 (절대 TIMESEC 합성)

읽기 → 변환 → 런타임 합성:

1. **읽기**: `SEEK('C17')` 후 성분(MTIDE)×경계(NPFOR)별 `PFAM(NP,M), PFPH(NP,M)` (`input.f90:903` 부근, NPFORT 분기별).
2. **cos/sin 변환**: `RAD = 2π·PFPH/TCP(M)` → `CPFAM0 = PFAM·cos(RAD)`, `SPFAM0 = PFAM·sin(RAD)` (`input.f90:913-915`, NPFORT≥1 분기; NPFORT=0은 S/W/E/N 경계 카드 처리에서 동일 변환 후 ×G로 `PCB*/PSB*` 생성, `input.f90:980-1005` 등 — [[efdc_boundary_conditions]] §G).
3. **런타임 합성**: `hdmt.f90:89` `TIMESEC = DBLE(TCON)·DBLE(TBEGIN)`(런 시작 시 **절대 시간**으로 초기화) → `setopenbc.f90:232` `TN = TIMESEC`, `:234-237` `CCCOS/SSSIN = cos/sin(2π·mod(TN,TCP)/TCP)` → `:255-260`(남측; 서/동/북 동형) `FP += PCB·cos + PSB·sin`.

cos·cos + sin·sin 합성 항등식으로 정리하면:

```
η_tide(t) = Σ_M  PFAM(M) · cos( 2π·(TIMESEC − PFPH(M)) / TCP(M) )
```

**핵심 규약 2가지**:

- `PFPH`는 도(°)가 아니라 **TCP와 같은 시간 단위(초)의 위상 lag**다 (`RAD = 2π·PFPH/TCP`가 성립하려면 PFPH∈[0,TCP)).
- 합성 시각은 run 상대시간이 아니라 **절대 `TIMESEC`(= TCON·TBEGIN 부터 진행)**. 따라서 레거시 매뉴얼의 "phase relative to time origin of TBEGIN" 서술을 "run 시작 = 위상 0"으로 읽으면 안 되고, `TBEGIN`을 바꾸면 `PFPH`를 재계산해야 한다:

```
PFPH = [ TCON·TBEGIN + TCP·(G − (V0+u)) / 360 ]  mod TCP     (G, V0+u 는 도 단위)
```

## 2. v12.4에는 내부 nodal 보정이 없다

- v12.4 전 `.f90`에서 `nodal` 문자열 grep **0건** (2026-07-04). `PFAM/CPFAM/SPFAM` 소비처는 `input.f90`(read/변환)과 선언(`mod_var_global.f90`·`varalloc.f90`)뿐이고, `TCP` 합성은 `input.f90`+`setopenbc.f90`뿐 — 즉 조화 합성 경로 어디에도 nodal factor f, 천문인수 V0+u 계산이 없다.
- EPA 레거시 EFDC 매뉴얼에도 'nodal' 언급 0건 (2026-07 감사 web/문서 조사).
- **따라서 사용자가 직접**: 진폭에 nodal factor를 곱해 `PFAM = f·H`로 넣고, 위상에는 §1 공식대로 **V0+u를 fold**해서 `PFPH`로 넣어야 한다. 장기(수개월~수년) 런에서 f·u가 유의하게 변하면 구간 분할 재계산 또는 시계열(PSER) 강제로 전환.

## 3. 위상 페어링 규칙 (G vs g — 한국에서 +9h 함정)

조화상수 위상과 천문인수는 **같은 시간 기준**끼리 짝지어야 한다:

| 위상 종류 | 짝지을 천문인수 |
|---|---|
| Greenwich 위상 **G** (UTC 기준) | **진 UTC** epoch에서 계산한 V0+u |
| Zone 위상 **g** (예: KHOA 고시 135°E 기준) | **지방시** 인수 (local-time 기준 V0+u 상당) |

이를 섞으면 — 예: KHOA g(135°E)를 UTC V0+u와 결합 — 한국에서 성분당 **+9h 상당의 위상 오류**가 발생한다 (2026-07 감사에서 utide 합성 대조로 실증). 변환식: `G = g + ω·(zone lag)` (ω=성분 각속도 °/h, 동경 135°E는 lag=−9h 관계) — 어느 쪽 기준이든 **일관되게** §1 공식에 투입하면 동일한 PFPH가 나온다.

## 4. Nodal factor 1차 근사 (Schureman) — fallback 정확도

utide 등 정밀 FUV 계산이 불가할 때 쓰는 Schureman 1차 근사 (N = 달 승교점 경도):

| 성분 | f (1차 근사) |
|---|---|
| M2 | 1.000 − 0.037·cos N |
| K1 | 1.006 + 0.115·cos N |
| O1 | 1.009 + 0.187·cos N |
| K2 | 1.024 + 0.286·cos N |
| S2, P1 | ≈ 1.0 |

2026-07 감사에서 utide FUV 정밀값 대비 **±2% 이내** 확인 (테스트 회귀로 고정, §6). 태양 성분(S2·P1)은 nodal 변조가 무시 가능.

## 5. wser 바람 규약 (ISWDINT)

`wser.inp` 헤더의 `ISWDINT` (`input.f90:6903` read):

| ISWDINT | 문서상 의미 | v12.4 실제 동작 |
|---|---|---|
| 0 | 풍속+풍향(불어**가는** 방향) | read: 1열에 `WINDSCT` 배율 (`input.f90:6918-6922`). 런타임 그대로 소비 |
| 1 | 풍속+풍향(불어**오는** 방향) | read 시 2열 180° 반전 (`input.f90:6923-6933`) → 이후 0과 동일 |
| 2 | 동/북 **속도 성분** (DSI 블로그·wser 헤더 서술) | read는 두 열에 배율만 곱함 (`input.f90:6934-6939`) — **성분→풍속/풍향 변환 없음** |

런타임 유일 소비처 `caltsxy.f90:244-251`(TSWND 사용처는 `caltsxy.f90` 외에 read/선언뿐)은 **무조건** 1열=풍속, 2열=풍향으로 해석한다: `DEGM = 90 − VAL(:,2)`(나침반 방위→수학각), `WINDE = 풍속·cos(DEGM)`, `WINDN = 풍속·sin(DEGM)`. 따라서:

- **`ISWDINT=2`로 성분(E/N)을 넣으면 v12.4는 조용히 오독한다** — E성분을 풍속으로, N성분을 방위각으로 읽음. 사용 금지.
- 실재 옵션은 0(toward)/1(from)뿐. 내부 표준은 "불어가는 방향" 나침반 방위 + 풍속.
- 참고: 풍속은 이후 `WINDH` 측정고도에서 2 m 로그 변환(`caltsxy.f90:253-255` 부근, z0=0.003 open grassland).

## 6. 참조 구현 (레퍼런스)

EFDC_DSI 저장소 `Programs/efdc_settings_gui`:

- `core/tidal/unified_tidal_extractor.py` — `constituent_to_pfam_pfph()` (§1·§3·§4 규약 구현; utide FUV 우선, Schureman 1차 fallback)
- `tests/test_tidal_efdc_synthesis.py` — v12.4 `setopenbc` 합성식을 그대로 재현해 PFAM/PFPH 변환을 검증하는 회귀 테스트 (위상 페어링·fallback ±2% 포함)

## 관련 노트

- [[efdc_boundary_conditions]] — PSER+조화 경계 전체 파이프라인 (canonical)
- [[efdc-boundary-condition-foundation]] — 경계조건 기초
- [[efdc_cyclone_wind]] — 사이클론 바람장 (wser과 별개 경로)
- [[efdc-implementation-guide]] / [[efdc-user-manual-r850]] — R8.5.0 매뉴얼 노트 + v12.4 드리프트 ⚠️ 주석
- `concepts/tides/` — 조화분해·nodal 이론 일반
