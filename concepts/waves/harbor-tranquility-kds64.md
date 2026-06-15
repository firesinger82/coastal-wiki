---
title: "항만 정온도(harbor tranquility) 설계 표준 — KDS 64 + SWAN 실무"
topic: waves
canonical_source: self
citation_status: verified
source: "KDS 64 원문 직접 확인 (opendataloader-pdf 변환본 [[standards/kds-64/]], 2026-06-13): 반사율=KDS 64 10 10 참고표 4.3-4(Seelig·Ahrens 1981); 정온 기준파고=KDS 64 40 10 해설표 4.3-1(어선박지 사용가능 최대파고). [2026-06-15 §4.2/4.3 정량값 추가: 하역한계파고 해설표 4.2-4(日本港灣協會 1989, 소형 0.3/중대형 0.5/초대형 0.7~1.5m)·하역vs계류 개념 해설표 4.2-3·선체동요 권고기준 참고표 4.2-1(PIANC 2023, Surge/Sway/Heave/Yaw/Pitch/Roll) — kds-64-40-10-수역시설.md:477-544 직접 추출.] SWAN 정온도 표준 실무=한국 항만설계 관행. ※율포항 항-특정 내용 제거(2026-06-13). ※초판의 '기준파고 미존재' 정정은 오류였음(pdftotext 표 누락) — opendataloader-pdf로 표 확인."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-12
---

# 항만 정온도 설계 표준 — KDS 64 + SWAN 실무

> 한국 항만·어항 **정온도(harbor tranquility/agitation) 설계실무**의 객관 표준. 모델 선택 trade-off는 [`06-model-application.md §1.1`](06-model-application.md); 이 노트는 **국가 설계기준(KDS 64) 정량값 + 표준 SWAN 워크플로**.

## 1. 표준 모델 = SWAN (위상평균)

한국 정온도 실무는 **SWAN Model**을 표준으로 사용 (설계파산정 + 항내정온도 모두). SWAN이 고려하는 전파과정: 굴절·천수·**회절(diffraction)**·쇄파·blocking/reflection. 정온도는 SWAN의 **회절 옵션 + 구조물 반사율**로 처리.

- ⚠️ SWAN 회절은 **위상평균 근사**(phase-decoupled, Holthuijsen 2003 — [[swan-tech-ch2-obstacles-diffraction-setup]]). 항만 **공진·다중반사·장주기**엔 정확도 한계 → 정밀 검증은 위상해상 Boussinesq([`../../models/FUNWAVE/`](../../models/FUNWAVE/)·[`../../models/Celeris/`](../../models/Celeris/), §7).
- 표준 SWAN 설정(실무 예): STATIONARY, GEN3 KOMEN, BREAKING α=1.0 γ=0.73, FRICTION JON 0.038, 약최고고조위 수위.

## 2. nesting 격자 (SWAN 표준)

정온도는 외해→항내 scale가 커서 **광역→중간역→상세역 nesting**으로 구성. 광역에서 외해 설계파를 받아 단계적으로 상세역(항 입구·항내)까지 전달, 상세역(통상 Δ~10m)에서 항내 파고 평가.

| 영역(역할) | 격자간격(통상) |
|---|---|
| 광역 (외해 변형) | ~100 m |
| 중간역 (연안 천수) | ~50 m |
| **상세역 (항내 평가)** | **~10 m** |

## 3. 구조물 반사율 (KDS 64 10 10 참고표 4.3-4, Seelig·Ahrens 1981)

| 구조형식 | 반사율 | 구조형식 | 반사율 |
|---|--:|---|--:|
| 직립벽 (마루 정수면 위) | 0.7~1.0 | 이형소파 블록사면 | 0.3~0.5 |
| 직립벽 (마루 정수면 아래) | 0.5~0.7 | 직립소파 구조물 | 0.3~0.6 |
| 사석사면 (1:2~3) | 0.3~0.6 | 자연해빈 | 0.05~0.2 |

## 4. 항내정온 기준파고 (KDS 64 40 10)

정온도 판정의 **기준파고**는 용도에 따라 셋: (4.1) 어선 박지 사용가능 최대파고, (4.2) 계류시설 하역/계류 한계파고, (4.3) 선체동요 권고기준(파고 대신 동요량). 원문: [`../../standards/kds-64/kds-64-40-10-수역시설.md`](../../standards/kds-64/kds-64-40-10-수역시설.md).

### 4.1 어선용 박지 — 사용가능 최대파고 (해설표 4.3-1)

(대상어선 선종·선형·이용실태로 조정)

| 구분 | 수심 3.0m 미만 | 3.0m 이상 |
|---|--:|--:|
| 항내 묘박·정박 가능 최대 | 0.60 m | 0.70 m |
| 항로 항행 가능 최대 | 0.90 m | 1.20 m |
| 양육·준비 가능 | 0.30 m | 0.40 m |
| 휴식 가능 최대 | 0.40 m | 0.50 m |

### 4.2 계류시설 — 하역/계류 한계파고

**개념 구별** (해설표 4.2-3): **하역한계파고**=평상파, 하역작업 가능 판단(중대형 항만 위주) / **계류한계파고**=이상파, 태풍 등 이상파랑 시 계류가능 여부(어항은 하역한계와 동일 개념으로 간주하기도 함).

**하역한계파고 값** (해설표 4.2-4, 日本港灣協會 1989):

| 선형 | 하역한계파고 |
|---|--:|
| 소형선 (≈500 G/T 미만) | 0.3 m |
| 중·대형선 | 0.5 m |
| 초대형선 (≈50,000 G/T 이상, 돌핀·시버스) | 0.7~1.5 m |

계류한계파고는 항내파랑·선박동요·계류방식에 좌우돼 특정값 제시가 어려움 → 필요시 **계류안정성 실험** 별도 검토(원문 (4)).

### 4.3 선체동요 권고기준 (참고표 4.2-1, PIANC 2023)

파고가 아니라 **허용 선체동요량**으로 안전 하역을 판정. 값은 Peak-to-peak(단 Sway는 0-to-peak); 수치·실측·인터뷰·전문가 합의 종합값:

| 선종 (세부) | Surge | Sway | Heave | Yaw | Pitch | Roll |
|---|--:|--:|--:|--:|--:|--:|
| 액체벌크 | ±1.0 | ±1.0 | ±1.0 | — | — | — |
| 드라이벌크 (Crane/Grab) | ±1.0 | ±1.0 | ±0.5 | — | — | ±3.0° |
| 일반화물선 | ±1.0 | ±0.75 | ±0.5 | — | — | ±2.5° |
| 컨테이너선 (95% 효율) | 0.2~0.4 | ±0.4 | +0.3 | ±1.0° | ±0.3° | ±0.3° |
| 로로/페리 (차량, 운영) | ±0.3 | +0.6 | ±0.6 | — | — | 2° |
| 크루즈 (PBB, typical) | ±0.3 | −0.6~0.3 | ±0.3 | — | — | 2° |

(단위 m / 각도 °. 전체 선종·extreme 값은 원문 참고표 4.2-1.) 장주기·부진동 민감 → §6 위상해상 티어 검토 대상.

### 4.4 어항·계류시설 고유 조항 (64 65 00 · 64 55)

기준파고(§4.1-4.3) 외에, 시설 유형별 정온 설계 조항:

- **어항 — 소파블록식 방파제** (64 65 00): 진입파·반사파 영향으로 직립제로 정온 확보가 어려운 경우 적합하나, **부진동 등 주기가 긴 수면변동엔 효과가 적다**([`../../standards/kds-64/kds-64-65-00-어항.md`](../../standards/kds-64/kds-64-65-00-어항.md):788). 어항 설계조건은 파고·주기·정온도를 함께 설정(:2588).
- **어항 — 대피용 소형선 부두** (64 65 00:479): 기상악화 시 종렬계류, 양육/휴식 기능구분 불필요. **항내정온이 불완전한 어항**은 어선 상호 충돌·파손 방지 위해 충분한 여유 확보.
- **계류시설 일반** (64 55 10:541): 시버스·폐쇄성 항만 등 특수 경우 **장주기 파랑·항내 부진동** 발생 시 계류선박 선체동요로 안벽 충돌 가능 → 동요 검토로 안벽 상부 돌출길이 결정.
- **부유식 계류시설(폰툰)** (64 55 30:439): **장주기 파랑 내습 지역의 폰툰은 동요 시뮬레이션 기법으로 동요해석 권장**. 파랑 우려 시 파력 고려(KDS 64 10 10 §4.3.9.6 부체 동요).

→ 공통 함의: **부진동·장주기**는 SWAN 위상평균으로 약함 → §6 위상해상 티어(공진·부진동 직접 해상)로 검증.

## 5. 표준 워크플로

```
심해설계파(빈도별·파향별, 예 50년) ─SWAN nesting(광역→중간→상세)─▶ 항내 파고분포
   → 실험안별(현상태/비교안/채택안) × 주영향 파향 × 반사율(KDS64 10 10)
   → 항내 파고 vs 기준파고(KDS64 40 10) 대조 → 정온확보 구역 판정
```
- 출력: 파향-파고 벡터도 + 파고분포도(정온확보 구역 음영).
- 평면배치 대안을 비교해 **정온확보 가능한 채택안** 도출이 목적.

## 6. SWAN 표준 vs FUNWAVE/Celeris 정밀 티어

| | SWAN (표준·인허가) | FUNWAVE / Celeris (정밀 검증) |
|---|---|---|
| 회절 | 위상평균 근사 (phase-decoupled, Holthuijsen 2003) | **위상해상**(파위상 직접 해상) |
| 공진·다중반사·**부진동(장주기)** | 약함 | 강함 (§4.4 어항/계류 부진동 민감 케이스) |
| 방정식 | 작용평형(spectral) | 완전비선형 확장 Boussinesq (FUNWAVE = Celeris COULWAVE 모드 동급) |
| 위치 | KDS 64 표준, routine 설계 | 공진 민감·SWAN 의심 케이스 검증 |
| 비용 | 빠름 | 느림 → **GPU로 상쇄** (Celeris solver+render 동거 실시간) |

- **왜 위상해상이 부진동에 강한가**: SWAN 회절은 위상평균 근사라 항만 공진·다중반사·장주기 부진동 정확도 한계([[swan-tech-ch2-obstacles-diffraction-setup]]). FUNWAVE/Celeris는 파위상을 직접 해상해 공진·부진동을 잡음. 두 모델은 **같은 완전비선형 Boussinesq 클래스**([`../../models/Celeris/web-refs/celeris-coulwave-theory.md`](../../models/Celeris/web-refs/celeris-coulwave-theory.md) §2 — Celeris COULWAVE 모드 = FUNWAVE 방정식족).
- **Celeris의 정온도 강점**: solver+rendering GPU 동거 실시간이라 항 평면배치 대안을 **돌리며 스크리닝**([`../../models/Celeris/source-analysis/celeris-render.md`](../../models/Celeris/source-analysis/celeris-render.md)) → 유망안만 정밀 케이스. FUNWAVE는 배치 HPC로 채택안 정밀 재현([`../../models/FUNWAVE/source-analysis/funwave-dispersion-solver.md`](../../models/FUNWAVE/source-analysis/funwave-dispersion-solver.md)).

→ 권장: **SWAN으로 표준 정온도(인허가) + 부진동·공진 민감 시 FUNWAVE/Celeris 동일 케이스 정밀 재현·교차검증**.

## 7. 연결

- [`06-model-application.md §1.1`](06-model-application.md) — 정온도 모델 선택 trade-off
- [[swan-tech-ch2-obstacles-diffraction-setup]] — SWAN 회절 근사(Holthuijsen 2003)
- [`../../models/Celeris/web-refs/celeris-coulwave-theory.md`](../../models/Celeris/web-refs/celeris-coulwave-theory.md) — Celeris COULWAVE = 완전비선형 Boussinesq(FUNWAVE 동급), 위상해상 근거
- [`../../models/FUNWAVE/`](../../models/FUNWAVE/) · [`../../models/Celeris/`](../../models/Celeris/) — 정밀 티어 (배치 HPC vs 실시간 GPU)
- 외부: KDS 64 10 10(구조물 반사율)·KDS 64 40 10(정온 기준파고·하역한계·선체동요), 2024 해양수산부
