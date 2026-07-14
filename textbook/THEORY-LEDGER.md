# THEORY-LEDGER — 교재 이론 이식 원장 (4-레이어 ①, T 트랙)

> **목적**: 교재 프로젝트 `textbook-ai-data-full`(작성자 로컬 repo — 16챕터, 인용 없는 AI 합성 MDX; 위치는 [plan.md](../plan.md) 4-레이어 섹션 참조)를 `textbook/notes/theory-ch<NN>-<slug>.md` 로 **인용보강 이식**하는 진척·지표 추적. 정책: [plan.md "4-레이어 지식 아키텍처 v2"](../plan.md) · [CONVENTIONS §8.1](../CONVENTIONS.md). 패턴: [models/AUDIT-LEDGER.md](../models/AUDIT-LEDGER.md).
>
> **챕터당 절차(인용접지 파이프라인)**: MDX 이식(컴포넌트 제거) → 원자 단언 분해 → `textbook/md/` FTS5·페이지 대조 → `(source_id, p.N)` 부착 → **미매칭 단언 = 삭제 또는 source-needed 콜아웃** → validator(3종+layer lint) → 지표 기록. 부분 부착 ≠ 파일 verified. frontmatter: `layer: 1` + AI 합성 provenance.
>
> **완주 분모 = 15챕터**(00.5~15 전부, ch00 Intro 만 제외) — **F-4 사용자 확정 (a) 전부 이식**(2026-07-12; 리뷰어 양측의 (b) 도메인 축소 권고 기각). 챕터 간 유도 의존은 `depends_on` 으로 명시 가능(①→① 허용·순환 금지, CONVENTIONS §8.1).
>
> **stop/go 게이트**: T1 파일럿 지표로 장별 scope·페이스 재산정(고정 "세션당 N챕터" 없음). Codex 게이트 ⓐ(T1 후)·ⓒ(~4챕터 배치마다).
>
> **지표 정의(게이트 ⓐ 확장)**: 단언 수 / 매칭률(부착÷전체) / **anchor 정밀도**(표본 재검증에서 직접 지지 판정 비율 — 광범위 인용·적용문맥 인용은 부적정) / **수식 대조**(전사 오류 0 여부; OCR 소실 페이지는 disclosed) / **residue**(무출처 잔존 단언 수 — verified 는 0 필수) / 소요. 단언별 원장(audit table)은 후속 개선 항목.

## 진척 대시보드

| 챕터 | 주제 | 노트 | 주 출처 후보 | 상태 | 단언 수 | 매칭률 | 소요 |
|---|---|---|---|:--:|--:|--:|--:|
| 00 | Intro (학습 안내) | — | — | **이식 제외** (사이트 안내문, 이론 아님) | - | - | - |
| 00.5 | 수학 도구 (벡터·텐서·RTT) | [theory-ch00_5-math-tools](notes/theory-ch00_5-math-tools.md) | ★**hudspeth2005-wave-forces**(§2·§3, 주출처 정정)·stewart-physical-ocean | ✅ **T7 완료**(2026-07-14, Codex 파일럿 게이트 반영) | 31 | 77% (24 부착·7 삭제/미이식) · ★**주 출처 정정**: hydraulics-and-hydrology=벡터/텐서/RTT/발산정리 전무(스캔 0건)→Hudspeth §2 수학예비+§3 유체기초로 확정 · 핵심 부착: Levi-Civita p.29·gradient p.31·Laplacian p.32·D/Dt=∂t+q·∇ p.32-33·Gauss div p.69·Green p.70·RTT p.78·속도구배 분해 p.80-83·Einstein합 p.666 · ★게이트 정정: 마커 실측 정정 9곳·pathline 복원(stewart p.199-201, 삭제 오판)·rank/공변반변 삭제 · 삭제: 순수 수학사·streakline·Stokes 정리·워크예제 · 미표기 residue 0 · ★기초 파일럿(depends_on:[]) | ~1.4h |
| 01 | 보존법칙 (검사체적·RTT) | — | hydraulics-and-hydrology | ⬜ | | | |
| 02 | 연속방정식 | — | hydraulics-and-hydrology | ⬜ | | | |
| 03 | Euler·Bernoulli | — | hydraulics-and-hydrology | ⬜ | | | |
| 04 | Navier-Stokes | — | hydraulics-and-hydrology | ⬜ | | | |
| 05 | RANS·난류 | — | hydraulics-and-hydrology | ⬜ | | | |
| 06 | 경계층 | — | hydraulics-and-hydrology | ⬜ | | | |
| 07 | 와도 동역학 | — | hydraulics-and-hydrology | ⬜ | | | |
| **08** | **선형 파동·분산관계** | [theory-ch08-linear-waves](notes/theory-ch08-linear-waves.md) | water-wave-mechanics(주)·holthuijsen2007 | ✅ **T1 완료**(2026-07-12, 게이트 ⓐ MODIFY 반영 재검증) | 26 | 92% (24 부착·2 삭제) · 게이트 후 anchor 정밀화 6곳·residue 2건 해소(쓰나미 p.22-23·Phillips p.173/Hasselmann p.163) → residue 0 | ~0.7h |
| 09 | 비선형 파동·스펙트럼 | [theory-ch09-nonlinear-spectra](notes/theory-ch09-nonlinear-spectra.md) | holthuijsen2007(주)·water-wave-mechanics | ✅ **T3 완료**(2026-07-12, 게이트 ⓒ MODIFY 반영) | 30 | 87% (26 부착·4 삭제) · ★연도 오기 1건 정정(Hasselmann 1957→1962 p.203) · ⓒ④ Stokes 2차 anchor p.302→p.318-319(Eq.11.29·11.32·11.33)+α 계수 정의 · Beaufort 표·SMB 시대오류·Jeffreys·Draupner 수치 삭제 · residue 0 | ~0.5h |
| 10 | 해안 변형 (shoaling·refraction) | [theory-ch10-coastal-transformation](notes/theory-ch10-coastal-transformation.md) | water-wave-mechanics(주)·holthuijsen2007·mechanics-of-sediment-transport | ✅ **T4 완료**(2026-07-12, 게이트 ⓒ MODIFY 반영) | 26 | 88% (23 부착·2 삭제·1 보류) · ⓒ⑤ ★Sommerfeld 1896 해+Fresnel 적분 p.134 실존 — 초판 '대체' 오판 번복, Penney-Price p.133 과 병기 복원 · ⓒ⑧ rip 정의 MST p.766 부착 · ⓒ⑦ depends_on ch09→탐색 강등 · ⚠️**5π/16 = MST p.765 Eq.16.30 OCR 훼손 — 원 PDF 확인 대기(보류·삭제 미확정)** · 0.15Hb·rip 80% 삭제 · 미표기 residue 0 · source-needed 1(5π/16, has_source_needed) | ~0.5h |
| 11 | SWAN 모델 | — | ★claim-level 분해 — 일반 이론만 ①, 모델 구현은 models/SWAN 탐색 링크(복제 금지) | ⬜ | | | |
| **12** | **조석** | [theory-ch12-tides](notes/theory-ch12-tides.md) | sea-level(Pugh, 주)·stewart-physical-ocean | ✅ **T2 완료**(2026-07-12, 게이트 ⓒ MODIFY 반영) | 28 | 86% (24 부착·4 삭제) · ★원문 오류 정정 3건: 예측기 1862→**1873**(p.155) · Doodson 1924→**1921/1922 출처 간 불일치 명기**(ⓒ① stewart p.318-319 본문 vs sea-level p.74 서지) · ⓒ③ 조석가속도 1.1e-6 g→**11.2×10⁻⁸ g 정정 복원**(p.78-79, 삭제 번복) · ⓒ② 장파 판정 p.156 직접 보강 · residue 0 · **첫 ①→① 의존**(ch08 얕은물 한계) | ~0.6h |
| 13 | 퇴적물 이송 (Shields·Rouse) | [theory-ch13-sediment-transport](notes/theory-ch13-sediment-transport.md) | marine-sands-manual(주)·mechanics-of-sediment-transport·efdc-sed-trans-2003 | ✅ **T5 완료**(2026-07-13, 게이트 ⓒ 2차 반영 07-14) | 35 | 91% (32 부착·3 삭제) · ★연도 미지지 2건 미이식(Krone '1962'·Partheniades '1965' — 실측 Ariathurai & Krone 1976 p.66) · ★CERC 공식 = marine-sands p.198-199 실측 부착 · ⓒ2차: z_a=2d50 삭제 오판 복원(p.149 Zyserman-Fredsøe)·VanRijn 0.053/2.1 = efdc p.58 판독 정정·Rouse profile 식 문자소실→전사 제거 · Rouse 모드표·boulder표·fluid mud 삭제 · **★van-rijn-1993 미러 = OCR 껍데기 판정** · 미표기 residue 0 | ~0.8h |
| 14 | 해안 형태동역학 (Dean·CERC·Bruun) | [theory-ch14-coastal-morphodynamics](notes/theory-ch14-coastal-morphodynamics.md) | coastal-processes-with-eng-apps·coastal-structures-design·coastal-eng-guidelines·MST·marine-sands | ✅ **T6 완료**(2026-07-14, 게이트 ⓒ 2차+확인 반영) | 41 | 80% (33 부착·8 삭제/미이식) · ★Hallermeier '10.9'→**68.5 정정 복원**(CSD p.127 Eq.3 실존 — ⓒ2차가 '공식 미전사' 오판 적발) · ⓒ2차 복원: salient 분기 조건(CP p.30 Fig3.17c)·GENESIS/SBEACH 제한 활용(CSD p.149) · CERC 중복 단언 제거+depends_on ch13 탐색 강등 · Dean x^{2/3}·A표·K값·Kamphuis식·Bruun 정량식·one-line 유도 미전사(계보·정성은 부착) · ★CP 미러=35p 부분본 판정 · 미표기 residue 0 | ~1.1h |
| 15 | EFDC 운용 | — | ★claim-level 분해 — 일반 이론만 ①, 모델 구현은 models/EFDC 탐색 링크(복제 금지) | ⬜ | | | |

- 매칭률 = (source_id, page) 부착 단언 / 전체 원자 단언. 미매칭 처리(삭제/source-needed) 건수는 노트 frontmatter·본문 콜아웃에.
- 상태: ⬜ 미착수 / 🔄 진행 / ✅ verified / 🟡 source-needed 잔존.

## 게이트 기록

| 게이트 | 일자 | 판정 | 요지 |
|---|---|---|---|
| (설계) Codex 2회차 | 2026-07-12 | MODIFY→반영 | 4-레이어 v2 — plan.md 검증 이력 참조 |
| **ⓒ T2~T4 배치** (Codex 6회차) | 2026-07-12 | **MODIFY — 8건 반영 완료(2026-07-12 후속 세션). ①~⑤·⑦·⑧ 노트 반영, ⑥ 5π/16 = source-needed 보류(원 PDF p.765 사용자 확인 대기 — T5 선행조건 아님)** |
| **ⓒ 확인 라운드** (Codex 7회차, 019f5661 resume) | 2026-07-12 | **MODIFY→반영: ②③④⑦⑧ APPROVE / 잔여 4건 정정 — ①Stewart 'Doodson (1922)' 페이지 p.319→p.318·'명명 체계'→'Doodson 번호 식별' 축소 ⑤Fresnel 적분 상·하한 OCR 미검증→기호 전사 제거 ⑥G9 형식화: in-text source-needed 토큰+frontmatter has_source_needed ⑥' 원장 'residue 0(disclosed)'→'미표기 residue 0·source-needed 1' 정정. T5 진행 승인(원 PDF 확인은 선행조건 아님)** | 8건: ①T2 Doodson p.74=서지목록일 뿐 — stewart p.318-319 로 분리+연도 1921/1922 불일치 명기 ②T2 조석 장파 판정 sea-level p.156 보강 ③★조석가속도 = 삭제 아닌 **11.2×10⁻⁸ g 정정 복원**(sea-level p.78-79 직접 제시) ④T3 Stokes 2차식 anchor p.302(속도·수송)→**p.319 Eq.11.33** 교체+α 계수 정의 ⑤★★T4 Sommerfeld 1896 해+Fresnel 적분이 **p.134 에 실존** — '미확인' 오판, "Sommerfeld 해 p.134 + Penney-Price 정리 p.133" 복원 ⑥5π/16 = mechanics-of-sediment-transport **p.765 Eq.16.30** OCR 훼손 후보 — 원 PDF 확인 전 삭제 확정 불가 ⑦T4 depends_on ch09 REJECT→탐색 강등 ⑧T4 rip 문장 무인용 — 출처 부착 또는 순수 탐색 전환. 적정 확인: 1873 정정·분조 주기·Hm0·Iribarren·Hasselmann 1962·Sxx·T2/T4→ch08 의존 |
| **T7 기초 파일럿 (ch00.5)** (Codex 10회차, resume) | 2026-07-14 | **MODIFY→반영: 주 출처 교체(hydraulics→Hudspeth) APPROVE·스코프(ch01-04 유도 기반) APPROVE / 정정 — 페이지 마커 9곳 실측 정정(Levi-Civita p.29·gradient p.31·Laplacian p.32·Leibnitz p.34·Taylor p.36-38·속도구배 p.80-83·Green Eq.2.123c·∂D 통일)·Einstein합 p.666 부착·rank일반/공변반변 삭제(직접출처 없음)·★pathline 복원(stewart p.199-201 실존, 삭제 오판·streakline만 미이식). '자기완결적'→'briefly outlined' 완화. residue 0 재확보. ★교훈 재확인: grep 근사 페이지 금지, ---PAGE-N--- 마커 실측 필수** |
| **ⓒ 2차 배치 (T5·T6)** (Codex 8회차, 019f5661 resume) | 2026-07-14 | **MODIFY→당일 반영: 핵심 앵커(Soulsby θcr·Eq96·MPM·Exner·CERC 계보·계절단면·DOC·Bruun 서지) 적정 확인 / 정정 9건 — ★T6 Hallermeier 68.5 식 = CSD p.127 실존('미전사' 오판, 정정 복원) ★T5 z_a=2d50 = MS p.149 실존(삭제 오판 복원) ★VanRijn 0.053·2.1 = efdc p.58 판독('검증 불가' 과장 정정) ★GENESIS = CSD p.149 실존('0건' 철회) ★salient 정성 조건 = CP p.11·30 복원 / Rouse profile 식 문자소실→전사 제거 / Dean number 앵커 p.26/27 분리 / T6 depends_on ch13 = CERC 복제라 부적정→중복 제거+탐색 강등 / 지표 재집계(T5 91%·T6 80%). 반복 교훈: 미매칭 삭제 전 인접 페이지·타 소스 재검색 — 2회 연속 위반** |
| **ⓒ 2차 확인 라운드** (Codex 9회차, resume) | 2026-07-14 | **MODIFY→반영: 9건 중 ①②④⑤⑥⑧ APPROVE / 잔여 3건 정정 — ③T5 Rouse 수 정확식 $b=w_s/(\kappa u_*)$ 도 미러 소실(Eq.105 분수 문자)→정성+변수 나열로 완화 / ⑦T6 salient 분기 조건(CP p.30 Fig3.17c '너무 먼 이안지형→salient') 본문 실제 복원(선언만→단언 추가, +1 부착) / T5 §7 fluid mud 표기 정정(WWM p.289 용어 실존·claim-level 미지지). T5 91%(32/35)·T6 80%(33/41) 확정, residue 0 승인. T트랙 7/15 종결** |
| **ⓐ T1 파일럿** (Codex 3회차, lint ⓑ 겸) | 2026-07-12 | **MODIFY→필수 6건 반영, T2 진행 가능** | 인용검증: §3 진행파 p.72-77→**p.78 §3.4.4 Eq3.40-42 정정**·선형화 페이지 분리(DFSBC p.73/KFSBC p.74)·바닥 p.63 Eq3.9 / residue 2건(쓰나미 파장·Phillips/Hasselmann) 앵커 확보 / 수식 전사 오류 0(p.78 OCR 소실은 disclosed) / lint: 전용 경로 layer·depends_on **강제**+대상 실존성+`..` 금지+scope guard **HEAD 기준** 전환+escape 감사출력. 후속 개선(비차단): 단언별 audit table·회귀테스트·동일 layer 순환 정책 |
