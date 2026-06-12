---
title: "KHOA 장기관측 100년 폭풍해일고 EVA — 해수부(2022) 설계값 감사·정의·기후증폭 (1956-2025)"
topic: storm-surge
canonical_source: self
citation_status: verified
verification_method: "AI programmatic pipeline: (1) KHOA distribution.do ZIP 과거자료 확장 다운로드 1956-2025 (49정점, 신규 832 연도, fetch_history.py — 무자료=HTTP500+html 즉시마킹, setsid 백그라운드) (2) 정점·연도별 utide(OLS, nodal) 잔차=폭풍해일 → 연최대치·POT 디클러스터 캐시 (3) 극치분석 4법: Gumbel/GEV(L-moment Hosking) 연최대 + POT/GPD(genpareto) + 지역빈도 RFA(지수홍수) + 부트스트랩 CI (4) 해수부 2022 보고서 100년 설계 폭풍해일고 21항만 대조 (5) 정의확인: 서승원·이화영 2012(목포 pADCIRC+unSWAN 100년 가상태풍) + Pugh 교과서(concepts/storm-surge) (6) MSL 추세 vs KHOA 보도자료 2025-12-28 동일기간 1989-2024 (7) datum 동질화 Pettitt 변화점 (8) joint tide-surge probability 총수위 분해 MC. 실행 py=coastal-wiki/.venv(utide 0.3.1·scipy 1.17.1). 도구·산출: /home/firesinger/khoa_tide/utide_validation/{analyze_surge_return_level,analyze_regional_eva,build_eva_cache,analyze_utilization,build_msl_cache,analyze_twl_trend,homogenize_datum,analyze_joint_probability}.py + extensions/6_*~16_*. [2026-06-12 Fable 5 재검토 후 정정: §2 표를 최종 10_design_audit.csv 단일 run 기준으로 재생성(이전 6_surge_return_level.csv 구버전 혼입 제거, 보령 Gumbel>GEV 역전 반영)·§3 CI 분모규칙(22→장항제외 21)·동해항 CI과대 추가·CI기준 vs RFA기준 플래그 분리 명시·해수부2022 서지 보강·reproducible 로컬한정 명시.]"
note_author: "Claude Opus 4.8 (1M context) + 사용자 합의"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — 다중 cross-ref (독립 ADCIRC+SWAN 모델값 + KHOA 공식 SLR 발표 + Pugh 교과서 + 자기일관성)"
verification_date: 2026-06-03
experience_evidence:
  repeated_observation: true   # 21항만 독립 + 4방법 수렴 + 목포 3중 일치(관측RFA·독립모델·검증)
  objective_data: true         # 해수부2022 설계값 + 서승원2012 ADCIRC모델 + KHOA보도자료 SLR + Pugh교과서
  reproducible: true           # utide_validation/*.py + ZIP 1956-2025 — 단 도구·원자료는 로컬 ~/khoa_tide/ 한정(위키 repo 외부); 재현엔 해당 환경 필요
---

# KHOA 장기관측 100년 폭풍해일고 EVA — 해수부(2022) 설계값 감사·정의·기후증폭

> **3조건 통과** ([BOUNDARY.md](../BOUNDARY.md)): (1) 반복관찰 — 21항만 독립 + 극치 4방법 수렴 + 목포 3중 일치 (2) 객관데이터 — 해수부 2022 설계보고서 + 서승원·이화영 2012 ADCIRC+SWAN 모델값 + KHOA 보도자료 2025-12 SLR + Pugh 교과서 (3) 재현 — `utide_validation/*.py` + ZIP.
>
> **전신**: [[khoa-49-station-16yr-utide-2026]] (49정점 16년 utide, 폭풍해일 residual). 본 노트는 **시간확장(16년→최대 70년, 1956-2025) + 분석확장(residual → 100년 극치 EVA + 설계값 감사 + 기후증폭)**. 방법론 출처는 [`concepts/storm-surge/03-analysis-methods.md`](../concepts/storm-surge/03-analysis-methods.md)(Pugh tide-surge separation·return period·POT).

## 1. 데이터 확장

전신 노트의 2010-2025를 KHOA `distributionSearchZipFile.do`로 **1956-2025 확장**(`fetch_history.py`, 신규 832 연도). 정점 보유: 부산·목포 1956~(54-70y), 울산1962·제주1963·여수/묵호1965~, 통영1976·군산1980·보령1985~. 무자료=HTTP500+html(302 아님). 광양·태안 등 신설정점은 2010~만.

## 2. 핵심: 극치분석 방법 선택이 결론을 좌우

폭풍해일 잔차(=관측−utide예측) → 100년 재현값. **방법 의존성이 결정적** (값 = 최종 감사 산출 `extensions/10_design_audit.csv` 단일 기준, n = 정점별 보유연수):

| 방법 | 여수 | 군산 | 보령 | 특성 |
|---|--:|--:|--:|---|
| Gumbel-연최대(AM) | 148 | 127 | 149 | 가벼운꼬리; **단기록일수록 과소** (보령 n=41은 GEV 상회) |
| GEV-AM (L-moment) | 184 | 191 | 143 | shape 허용 (음수 shape → 유계) |
| POT/GPD (태풍피크) | 244 | 189 | 155 | 혼합모집단 제거 |
| RFA (지역빈도) | 157 | 177 | 181 | 가장 안정 |
| **해수부 2022** | **230** | **228** | **224** | 가상태풍 |

→ 방법 범위 ~100cm 폭 (Gumbel 127–149 vs POT 155–244). **단일 방법(특히 Gumbel-AM 단독)으로 결론내면 오인** — 단 "Gumbel이 항상 최저"는 거짓(보령 Gumbel 149 > GEV 143; Gumbel 과소는 **단기록 정점에서** 체계적). 보고서와의 화해는 **해역별로 다름**: 남해 여수는 POT 244가 보고서 230 상회(보고서 지지)하나, **서해 군산·보령은 POT/RFA 전부가 보고서보다 낮음**(→ §3·§4 서해 체계적 보수성). 단일검조소 POT는 CI 매우 넓음(여수 [151~420]) → RFA가 실용 기준. (부트스트랩 B=10⁴)

## 3. 전국 설계 감사 (21항만)

보고서값 보유 **22 정점** 중 장항(스파이크 자료오류, 아래) 제외 **21정점** 기준. POT-GPD 95% CI가 보고서값 포함 = **17/21 → 보고서 대체로 관측지지**.

**CI 벗어난 4정점** (CI 기준):
- **과대방향**(보고서 > CI상한): 보령(224 vs CI고 215.5)·**동해항(59 vs 47.9)**
- **과소방향**(보고서 < CI하한): 목포(142 vs CI저 178.4)·속초(48 vs 50.1)

**설계판정 플래그** (RFA 기준 — CI와 별개 잣대):
- **과대의심**: 광양(249 vs RFA 140)·보령(224 vs RFA 181)
- **과소의심**: 목포(142 vs RFA 191·POT 216)·속초(48 vs RFA 67·POT 74)
- 주의: 광양은 n=16로 CI 광역[111~746]→**CI상 통과**하나 RFA로는 최강 과대의심(§아래); 동해항은 CI상 과대이나 동해·소규모(보고서 59cm)로 설계영향 작음 → 설계플래그엔 미포함.
- **자료오류**: 장항(연최대 398.8cm 스파이크, 분모 제외)

**관측 기반 보령·광양 진단** (`analyze_gwangyang_check.py`, 17_18_*): 공개 100년 독립모델값은 보령·광양 모두 미발견(연구가 남해·남동 태풍대 집중; 광양은 Jin 2024 매미강화 시나리오 광양만 5.01m뿐=100년 아님) → 관측감사가 유일 독립검증. "검조소가 정온한 만안쪽이라 과소"는 데이터로 기각: 광양 검조소 해일=인근 동급(7개 태풍 광양/여수=0.93~1.14, 광양 최대 95cm 힌남노 ≪ 보고서249), **증폭점 아님** → 보고서 249는 검조소밖 만최심부 모델증폭 의존 or 과대(**최강 과대의심**). 보령(72.9)=인근 군산71·안흥75 균일 → 서해 **전체 체계적 보수성**(개별이상 아님, 보고서 군산228≈보령224).

## 4. 보고서 '폭풍해일고' 정의 + 목포 3중검증

한국 설계기준: **설계조위 = 약최고고조위(천문조+연주조) + 폭풍해일 편차**. 보고서값=편차(총수위 아님) → 우리 잔차와 같은 범주. 단 설계 편차는 **wave setup(+0.2~1m, Pugh)·비대칭 최악경로 가상태풍·노출 설계지점**을 포함, 정온 검조소 잔차는 과소포착.

**목포 3중 일치** (결정적 검증): 독립 설계모델 [서승원·이화영 2012, pADCIRC+unSWAN, 100년 가상태풍 비대칭 최악트랙] **목포 100년 해일고=191cm** = 우리 **RFA 191**(정확일치)·POT 216. 해수부 2022 목포항=141.7(둘다보다 낮음). → 우리 관측법이 공개 설계모델과 cm일치(방법검증), 보고서 목포는 과소.

## 5. 기후: MSL 추세 + 빈도증폭 (KHOA 공식 일치)

- 원자료 연평균 MSL 추세, 해양수산부 보도자료(국립해양조사원, 2025-12-28, 1989-2024 36년)와 **동일기간 대조 → 전국 우리 3.25 vs KHOA 3.2 mm/yr (36년 11.7 vs 11.5cm)**. 해역평균 서해3.0·남해3.0·동해3.5 정합, 남해완만·동해광범위 패턴 재현.
- **추세 분해**: 연최대 총수위 ≈ MSL + 해일, **MSL 지배**(해일 극치추세 미약: 목포·군산만 유의·감소).
- **빈도증폭**: 관측 MSL 2100 선형투영(해일분포 불변) → 현재 100년 침수가 **제주 3년·인천 4년·부산 10년·여수 17년 빈도**로. 폭풍 불변에도 MSL만으로 설계빈도 수십배 잠식.

## 6. datum 동질화 + 실제신호 분리

오염은 **~1985 이전 집중**: 손상연도(목포 1970=67/1979=0cm, Pettitt+인접중앙값±25cm로 제거) + 기준면 계단(부산 1956-58 −45cm). 1989+는 깨끗. **중요: 목포 高상승률(5.1mm/yr)은 datum오류 아닌 영산강하구언/간척 지반침하 실제신호** — KHOA "범위"는 해역요약치지 개별정점 상하한 아님(전국·해역 평균 일치가 올바른 검증). 강제하향=오보정.

## 7. joint tide-surge probability — 침수 척도 분해

설계=약최고고조위+최악해일 합. 실제 극한해일은 만조와 비동시(독립)+천해 interaction(Pugh §7:8). 총수위 척도:

| 정점 | 약최고고조위 | 관측 100년 총수위 | 설계 총수위 | 차이 |
|---|--:|--:|--:|--:|
| 목포(검증) | 494 | 641 | 636 | **−5** ✓ |
| 보령 | 780 | 873 | 1004 | +131 |
| 광양 | 410 | 475 | 659 | +184 |

→ **목포 설계 총수위 ≈ 관측 100년 침수위(오차 5cm)로 프레임워크 검증**(낮은 해일이 조위·interaction으로 보정; 목포 만조시 해일억제 σ24.7→18.5). 보령+131/광양+184는 침수척도에서도 큰 설계여유 = 높은 설계해일 + 최악조위·최악해일 비동시조합 보수성 + SLR여유고(적정). 보고서가 낮은 목포는 총수위로 보면 실제와 정합(과소 재해석).

## 8. 종합 결론

1. **모델 vs 관측 = 승패 아닌 상호보완**. 관측(RFA/POT)은 설계값 감사 도구. 보고서 17/21 통과.
2. **목포가 3중(관측RFA 191 = 독립모델 191 = 검증) 검증** → 우리 파이프라인 신뢰 확립.
3. **MSL는 KHOA 공식과 cm 일치** → 빈도증폭·감사 결과에 동일 신뢰 이전.
4. **설계 보수성은 명명·정량 가능**: wave setup + 비동시조합 + SLR여유고. 보령·광양은 적정 여유 초과분 검토 가치.
5. **데이터 한계도 분리**: datum오염(목포 구자료)은 보정, 실제신호(목포 침하)는 보존.

## 9. 미해결 / 다음

- 보령·광양 공개 설계모델값 탐색 완료 → **미발견**(관측감사가 유일 독립검증). 단서: 연안빅데이터플랫폼 bigdata-coast.kr "빈도별 해일고 데이터셋"(1km격자, 동해안 공개; 서남해판 있으면 좌표값 추출 가능). wave setup 기여 SWAN 정량.
- 빈도증폭에 IPCC 가속(SSP) 반영(선형투영은 보수적 과소). VLM(목포 침하) GNSS/위성고도계 분리.
- joint tide-surge probability를 Pugh §8:3:3 convolution(정식)으로 격상.
- 장항 스파이크 완전제외 후 감사 갱신.

## 10. 연결

- 전신: [[khoa-49-station-16yr-utide-2026]] · 방법: [`concepts/storm-surge/03-analysis-methods.md`](../concepts/storm-surge/03-analysis-methods.md), [`01-concept.md`](../concepts/storm-surge/01-concept.md)(η 분해·wave setup)
- 설계모델: [`models/ADCIRC/`](../models/ADCIRC/), [`models/SWAN/source-analysis/swan-adcirc-coupling.md`](../models/SWAN/source-analysis/swan-adcirc-coupling.md)
- 기후: [[khoa-annual-climate-trend]] (SLR)
- 외부 출처:
  - **해양수산부 「연안(해안)침수예상도」** (본 노트 약칭 '해수부 2022' = 사용 자료 vintage) — 저기압·강풍 이상고조 기반 **가상태풍 시나리오 + ADCIRC 수치모의**로 50~200년(주로 100년) 빈도 폭풍해일고·침수범위 산정, **서·남해안** 대상, 연안포털 <https://coast.mof.go.kr> 게시(연안빅데이터맵 <https://bigdata-coast.kr> KOOS 태풍해일 자료 포함). 본 노트 **감사 대상**. 인용 설계 폭풍해일고: 광양 249·보령 224·군산 228.4·여수 230.4·목포 141.7 cm 등 ([`extensions/10_design_audit.csv`] 보고서 열). (항만별 설계고는 연안포털·빅데이터맵 데이터셋 기준 — 단일 PDF 보고서 문서번호는 미특정; 프로그램 산출 데이터.)
  - 서승원·이화영(2012) 한국해안·해양공학회논문집 24(4) 235-246 (목포 pADCIRC+unSWAN 100년 가상태풍 비대칭 최악트랙)
  - **Jin, H., Hwang, T., Kim, H.-J., Min, B.-I., Lee, W.-D. (2024)** "Storm surge simulations using hypothetical scenarios based on historical typhoons impacting the Korean Peninsula: analysis of storm surge and overtopping volumes" *한국수자원학회논문집(J. Korea Water Resour. Assoc.)* 57(12):1037-1051, doi:10.3741/JKWRA.2024.57.12.1037 — 매미강화 시나리오(Maemi-S2/S3) 광양만(지점 25) **5.01m = 기준대비 3.32배** (100년 빈도 아닌 시나리오 최악치)
  - 해양수산부 보도자료 2025-12-28 (국립해양조사원 관측, 해수면 36년 11.5cm)
