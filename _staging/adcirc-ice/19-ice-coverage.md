---
title: "ADCIRC ICE 커버리지 — 풍응력 항력 수정 전용(Garratt/IceCube/RaysIce/Lüpkes)·NWS 1000+·CICE_TIMINC"
model: ADCIRC
component: manual-notes
canonical_source: self
citation_status: verified
verification_method: "공식 자료 `raw/manuals/pdfs/adcirc_modifications_for_ice.pdf`(10쪽, Chris Massey·Ray Chapman, ERDC-CHL, 'Modifications to ADCIRC v49.64+ for ICE Coverage') pdftotext -layout 전수 추출 후 직접 read. 모든 단언을 snapshot `e8b62a70` 소스와 대조 — wind.F:120-139(항력 상한·DragLawString 기본값)·:507(Garratt 식)·:728-792(WindIceDrag 4분기)·:984 외(호출부), couple2swan.F:966,1033,1055,1185(SWAN 전달), global.F:673(CICE_TIMINC). 자료는 v49.64+ 기준이라 현 스냅샷과 어긋나는 지점을 §4에 분리 기록."
note_author: "Claude Opus 5"
note_date: 2026-09-22
related:
  - models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md
  - models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md
  - models/ADCIRC/source-analysis/adcirc-swan-coupling.md
---

# ADCIRC ICE 커버리지

> 출처: `raw/manuals/pdfs/adcirc_modifications_for_ice.pdf` — "Modifications to ADCIRC v49.64+ for ICE Coverage",
> Chris Massey·Ray Chapman (ERDC-CHL), 10쪽 발표자료. **버전 기준이 v49.64+ 로 현 스냅샷(`e8b62a70`)보다 앞선다.**

## 1. 적용 범위 — 오직 풍응력 항력

> "Ice coverage in ADCIRC was added as a way to **modify the wind drag values**.
> In no other way is ice coverage considered during ADCIRC's computational process." (p.2)

코드에서 확인된다 — 얼음 농도 `ciceout`은 `WindIceDrag()` 하나로만 흘러가고(`wind.F:984`·`:1026`·`:1072`·`:1122`·`:1189`),
운동량·연속식·저면마찰 어디에도 들어가지 않는다. **열역학·표류·유빙 응력은 없다.**

⚠ **단, ADCIRC+SWAN 결합에서는 예외다** (§4-③).

## 2. 활성화 — fort.15 변경 두 곳뿐

> "These are the only changes required in the fort.15 file in order to use ice coverage." (p.6)

| 항목 | 값 |
|---|---|
| `NWS` | **1000 + 평소 바람 옵션**. OWI 형식 ice 는 **12000** — 예시의 `NWS=12012` 는 OWI ice(12000) + OWI wind(12) |
| `WTIMINC` 줄 | `3600.0 86400.0  ! WTIMINC, CICE_TIMINC` — 바람 증분 뒤에 **얼음 증분**을 잇는다. 둘 다 초 단위 |

코드 대조: `NWS` 에서 1000 자리를 떼어 `NCICE` 로 쓰는 처리가 실재하고
([adcirc-met-forcing-implementation](../source-analysis/adcirc-met-forcing-implementation.md) §실측),
`CICE_TIMINC`·`CICE_TIME1`·`CICE_TIME2` 는 `global.F:673` 에 선언돼 있다.

## 3. 항력 공식

### 3.1 기저 — Garratt (1977)

ADCIRC 기본 풍응력 항력은 Garratt 형이며 상한 **0.0035** 를 건다 (p.2).

$$C_D = \frac{0.75 + 0.067\,|\vec{w}|}{1000}$$

코드: `wind.F:507`(식), `wind.F:122` `WindDragLimit = 0.0035d0`.
**따라서 Garratt 최솟값(무풍)은 $0.75\times10^{-3} = 0.00075$ 다.** 이 값이 §4-① 의 쟁점이다.

### 3.2 ICE CUBE — 얼음 비율의 3차 다항식

자료가 문서화한 유일한 얼음 항력식이다. `pic` = 얼음 피복률(0–1).

$$C_{D,\text{ice}} = \left(0.075 + 0.75\,p_{ic} - 0.9\,p_{ic}^2 + 0.2\,p_{ic}^3\right)\times 10^{-2}$$

`wind.F:749-765` verbatim 일치. 설계 조건 세 가지를 실제로 만족한다:

| 조건 | 계산 | 결과 |
|---|---|---|
| `pic`=0 → Garratt 최솟값 | $0.075\times10^{-2}$ | **0.00075** ✓ |
| `pic`=0.5 → 0.0025, 기울기 0 | $(0.075+0.375-0.225+0.025)\times10^{-2}$ ; $\frac{d}{dp}=0.75-1.8p+0.6p^2 \to 0$ | **0.0025**, 기울기 **0** ✓ |
| `pic`=1 → 0.00125 | $(0.075+0.75-0.9+0.2)\times10^{-2}$ | **0.00125** ✓ |

**적용 규칙**: Garratt(풍속 기반)와 ICE CUBE(얼음 기반) 중 **큰 값**을 쓴다 (p.3).
코드 `wind.F:764` `WindIceDrag = max(IceDrag,WindDrag)`.

## 4. 자료와 현 스냅샷의 차이

### ① ★"0.000075" 은 오기다 — 실제 0.00075

자료 p.3 과 **소스 주석**(`wind.F:751-752`)이 똑같이 "the minimum value for Garratt (.000075)" 라 적는다.
그러나 같은 파일의 Garratt 식(`wind.F:507`)은 $ (0.75+0.067|w|)/1000 $ 이므로 무풍 최솟값은 **0.00075** 이고,
ICE CUBE 식에 `pic`=0 을 넣어도 $0.075\times10^{-2} = 0.00075$ 다. **10배 차이의 자릿수 오기**이며
식 자체는 옳다. 자료와 소스 주석이 같은 오기를 공유한다 — 주석에서 자료로, 또는 그 반대로 옮겨진 것으로 보인다.

### ② 현 스냅샷의 얼음 항력은 4종이다 — 자료는 1종만 다룬다

`wind.F:736-787` 의 `SELECT CASE(TRIM(DragLawString))`:

| `DragLawString` | 식 | 근거 |
|---|---|---|
| `RaysIce` | $(0.125 + 0.5\,p_{ic}(1-p_{ic}))\times10^{-2}$, `pic<1%` 면 항력 그대로 | `wind.F:738-747` |
| `IceCube` | §3.2 | `wind.F:749-765` |
| `Lupkes` / `default` / `Powell` | $C_D(1-p_{ic}) + (C_{skin}+C_{form})p_{ic}$, $C_{form}=C_{form,max}(1-p_{ic})^\beta$ | `wind.F:767-779`. Lüpkes et al. (2012) doi:10.1029/2012JD017630 · Joyce et al. (2019) doi:10.1016/j.ocemod.2019.101421 |
| 그 외 | `terminate(ADCIRC_EXIT_FAILURE)` — 조용히 넘어가지 않는다 | `wind.F:781-786` |

**기본값 주의**: `DragLawString` 기본은 `wind.F:132` 에서 `'default'`, `:139` 에서 `'Powell'` 로 두 곳에 나타나며
둘 다 `Lupkes` 분기로 간다. 즉 **아무것도 지정하지 않으면 ICE CUBE 가 아니라 Lüpkes 형이 쓰인다.**
자료만 읽고 ICE CUBE 를 기대하면 어긋난다. `fort.15` 의 `metControl` 네임리스트에서 지정한다(`read_input.F:242`).

### ③ ★SWAN 결합에서는 "항력 전용" 이 아니다

자료의 "In no other way is ice coverage considered" 는 **ADCIRC 단독** 기준이다.
`couple2swan.F` 는 `NCICE≠0` 일 때 얼음장을 SWAN 으로 넘긴다:

- `SWAN_IICE => IICE` 로 SWAN 쪽 플래그를 받고(`:966`), `SWAN_IICE` 값에 따라 분기(`:1033`·`:1055`)
- `ICETIMEFRAC = ((STATIM*86400+ITIME*DT)-CICE_TIME1)/CICE_TIMINC` 로 시간 보간(`:1185`·`:1213`)

따라서 ADCIRC+SWAN 구성에서 얼음은 **SWAN 의 파랑 감쇠 물리로도 들어간다.**
상세는 [adcirc-swan-coupling](../source-analysis/adcirc-swan-coupling.md).

## 5. 정리

| 축 | 내용 |
|---|---|
| 물리 범위 | 풍응력 항력만(단독 실행 기준). 열역학·표류 없음 |
| 입력 | `NWS += 1000`(OWI ice 12000), `CICE_TIMINC` |
| 항력 선택 | `DragLawString` — 기본은 **Lüpkes**, 자료가 설명하는 ICE CUBE 는 명시 지정 필요 |
| 결합 | SWAN 으로 얼음장 전달(단독 실행과 다름) |
| 주의 | 자료·소스 주석의 "0.000075" 는 **0.00075** 의 오기 |
