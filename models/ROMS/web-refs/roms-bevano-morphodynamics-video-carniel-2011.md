---
title: "ROMS 결합 표사모델 × ARGUS 비디오 검증 — Bevano 하구 (Carniel et al. 2011)"
topic: roms-web-refs
canonical_source: self
citation_status: verified
has_source_needed: false
verification_method: "Carniel S., Sclavo M., Archetti R. (2011) 'Towards validating a last generation, integrated wave-current-sediment numerical model in coastal regions using video measurements', Oceanological and Hydrobiological Studies 40(4):11-20, doi:10.2478/s13545-011-0036-1 — **출판본 PDF 전문 직접 read (2026-07-19, pdftotext -layout)**. 대상해역 p.12-13·격자/설정 p.14-16·결과 p.16-18·검증 p.18-19 페이지 단위 인용. ★저자 자신이 검증 수준을 'qualitative/semi-quantitative'로 한정 — 본 노트도 동일 강도로만 서술."
note_author: "Claude Fable 5"
note_date: 2026-07-19
verification_by: "Claude Fable 5 — 출판본 PDF 직독"
verification_date: 2026-07-19
related:
  - models/ROMS/web-refs/roms-coawst-adriatic-applications.md
  - models/ROMS/source-analysis/roms_wec.md
  - concepts/sediment-transport/06-model-application.md
  - concepts/littoral-drift/06-model-application.md
---

# ROMS 결합 표사모델 × ARGUS 비디오 검증 — Bevano 하구

> [`roms-coawst-adriatic-applications.md`](roms-coawst-adriatic-applications.md) §3.5 Bevano 사례의 **모델측 원전**. 표사 메커닉은 [`concepts/sediment-transport/`](../../../concepts/sediment-transport/) 가 canonical, 본 노트는 적용·검증 맥락.

## 1. 출처

| 항목 | 값 |
|---|---|
| 제목 | "Towards validating a last generation, integrated wave-current-sediment numerical model in coastal regions using video measurements" |
| 저자 | S. Carniel, M. Sclavo (ISMAR-CNR) · R. Archetti (Univ. Bologna DICAM) |
| 게재 | *Oceanological and Hydrobiological Studies* **40**(4), 11–20 (2011) |
| DOI | `10.2478/s13545-011-0036-1` |

★**제목의 "Towards"가 정확한 표현** — 저자 스스로 이 작업을 **정성적·준정량적(semi-quantitative) 첫걸음**으로 규정(초록·결론 p.19). 운영 단계 진입에는 추가 튜닝 필요를 명시.

## 2. 대상 해역 (p.12-13)

NW Adriatic, Ravenna 남쪽 약 5 km **Bevano 하구**(Emilia-Romagna 연안). 지배 파랑 = **Bora(NE)·Sirocco(SE)** — 전자는 최강풍으로 **Hs 3 m 초과** 가능, 후자는 저에너지지만 **긴 fetch**. 양자 모두 침식·범람 유발.

**하구 인공개조 이력**: ~2005 년까지 자연 상태로 **북향 점진 이동**. **2006 년 초** 기존 북측 하구 폐쇄 + 남쪽 **500~600 m** 지점에 신규 하구 준설, 하천은 floodway 로 외해 직결. 신규 하구는 **목재 구조물**로 보호(SE 파랑·대조에 의한 북향 이동 억제 목적). 이후 모니터링: 신 하구 남측 가장자리가 **NE 부에서 점진 침식**, 최북단은 하상을 잠식해 대유량 시 흐름 지연.

## 3. 수치 설정 (p.14-16)

| 항목 | 값 |
|---|---|
| 모델 | ROMS 3D 자유수면 σ-좌표, **SWAN two-way 결합 + 전용 표사 모듈**(Warner et al. 2008) |
| 격자 | **160 × 115 점, 연직 12 σ-level**, 곡선격자(X축 CCW 약 8° 회전) |
| 해상도 | ★**X축 8~23 m · Y축 7~55 m** — 하구 규모 초고해상 |
| 수심 | 최근 5년 고해상 실측. ★도메인 외 하천 표면적을 반영하는 **reservoir 를 서측에 추가**(하천 유황·유속 재현 목적) |
| 표사 | **4 입도군 동시 모사** — **0.05 · 0.125 · 0.300 · 0.5 mm**, 각각 침강속도·침식/퇴적 임계전단 부여. 공간분포는 Gardelli et al. (2007) 실측, 격자점마다 4분율 합=1 |
| 연직혼합 | **k-ε (GLS)** 2방정식 2차모멘트 closure (Carniel et al. 2009) |
| 침수 | wetting/drying 활성 — 수위 상승 시 격자 순차 침수. 쇄파류는 radiation stress 로(Warner et al. 2008) |
| 경계 | 조위 = Punta Corsini(Ravenna) 조위계 실측, 바람 = 지역 기상모델(Signell et al. 2005), 파랑 = Cesenatico 파고부이(하구 외해 약 10 km, 수심 10 m) |
| 초기 | 정지 해면 + 안정 밀도장(단기 폭풍 사례이므로) |

**대상 사례**: **2010-03-09~10 Bora 폭풍** — 약 24시간 동안 **Hs 약 3.5 m·주기 9 s·입사 65°**(Cesenatico 부이 실측).

## 4. 모델 결과 (p.16-18)

- **유속**: Bora 가 북→남 정상류 생성. 최대치는 **汀線에서 다소 떨어진 사주(bar) 외측**. 표층 **0.85~0.9 m/s**, 저층 **약 0.5 m/s**. 수심적분 최대 약 0.75 m/s.
- **저면응력**: 폭풍 피크 시 기존 **사주 근방·하구 전면**에 집중 — 이것이 연안류를 셋업.
- **파랑장**: 규칙적 등수심선을 따라 굴절·쇄파로 파고 점감·파향 회전, 하구 내부로 침투하나 급격히 감쇠.
- **지형변화**(2일 적분, 무차원=최대침식으로 정규화): 汀線 인근 거의 전역 침식, **최대 피해는 현 하구 남측**. 하구 전면은 **퇴적 경향**(조류 약화 + 파랑작용 복합으로 추정).
- ★**핵심 결과 — 사주의 외해 이동 약 40 m**. 폭풍 시 전형적 seaward bar migration.

## 5. ★ARGUS 비디오 검증 (p.13, p.18-19)

- 관측계: 연구지 북 약 2 km **Lido di Dante** 의 **ARGUS 비디오 스테이션**(Holman & Stanley 2007, 2003 설치). 4 카메라 영상 병합·정사보정 → 항공사진처럼 실거리 측정 가능. **timex 영상** = 1 Hz 로 10분간 600 장 시간평균. 백색 띠 = 쇄파 → 汀線·사주 위치 지시.
- 검증 방식: 폭풍 전(**2010-03-03**) vs 후(**2010-04-01**) timex 영상의 **횡단면 픽셀 강도 패턴**(강도 0-256) 비교(Holland et al. 1997), Bevano 하구 북 약 500 m 측선.
- ★**결과 일치**: 영상이 지시한 사주 이동거리 **약 40 m**, 모델 산출 **약 40 m** — **동일 자릿수(same order of magnitude)로 독립 일치**.

⚠ **검증 강도의 한계(저자 명시, p.19)**: 이는 **"good qualitative conformity"** 이며 준정량 수준. RMSE·skill score 같은 통계량은 산출되지 않았다. 저자가 꼽은 미비점 — 입도별 임계전단유속 산정, 표사 동태 매핑용 현장자료 확충, 연안류 정밀 결정, **비극한 조건에서의 검증**.

## 6. 본 위키 접점

| 본 위키 자료 | 접점 |
|---|---|
| [`roms-coawst-adriatic-applications.md`](roms-coawst-adriatic-applications.md) | 리뷰 §3.5 Bevano 의 모델측 근거 |
| [`source-analysis/roms_wec.md`](../source-analysis/roms_wec.md) | radiation stress 쇄파류·파-류 결합 |
| [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) | 다입도군(4-class) 표사 모사 구성 사례 |
| [`concepts/littoral-drift/06-model-application.md`](../../../concepts/littoral-drift/06-model-application.md) | 연안방향 이송 지배 + 사주 외해 이동 |

→ **한국 적용 함의**: ① **하구 규모(10 m 급) 해상도에서 ROMS 결합계가 작동**한다는 구성 선례 — 격자 8~55 m·연직 12층·4 입도군. ② **비디오 관측이 저비용 형태변화 검증수단**이 될 수 있다는 실증(사주 이동 40 m 독립 일치). 단 **정량 skill 검증은 아니며**, 국내 적용 시 동일 수준의 일치를 기대할 근거는 본 논문에 없음(미실증).
