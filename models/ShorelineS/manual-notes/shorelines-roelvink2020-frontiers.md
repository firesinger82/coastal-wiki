---
title: "Roelvink et al. 2020 (Frontiers Mar. Sci. 7:535) — ShorelineS 정식화 발췌·코드 대조"
model: ShorelineS
component: manual-notes
canonical_source: self
citation_status: verified
verification_method: "repo 동봉 doc/FMarS2020_Roelvink_etal.pdf 를 pdftotext 로 추출·직접 read. 페이지 번호는 논문 내 쪽번호(1-19, Frontiers Vol.7 Art.535). 식·용어 verbatim 전사, 코드 라인과 대조."
note_author: "Claude Fable 5"
note_date: 2026-07-17
related:
  - models/ShorelineS/README.md
  - models/ShorelineS/source-analysis/shorelines-coastline-change.md
  - models/ShorelineS/source-analysis/shorelines-transport-formulations.md
---

# Roelvink et al. (2020) — 모델 기술 논문 발췌

> Roelvink, Huisman, Elghandour, Ghonim, Reyns (2020) "Efficient Modeling of Complex Sandy Coastal Evolution at Monthly to Century Time Scales", *Front. Mar. Sci.* 7:535, doi:10.3389/fmars.2020.00535. ShorelineS 의 사실상 이론 매뉴얼.

## 1. 지배방정식 (p.4 "Basic Equation")

$$\frac{\partial n}{\partial t} = -\frac{1}{D_c}\frac{\partial Q_s}{\partial s} - \frac{RSLR}{\tan\beta} + \frac{1}{D_c}\sum q_i \quad (\text{Eq.1})$$

- n=횡단(cross-shore) 좌표·s=연안 좌표·Dc=능동 단면고·Qs=연안수송[m³/yr]·tanβ=평균 단면경사·RSLR=상대해수면상승·qi=소스항(양빈 등). **코드**: `coastline_change.m:317`(−dSds/h0)·`:365`(−SLRo/tanbeta·양빈 가산).
- 계보(p.2): Pelnard-Considère one-line → 고각도 불안정(HAWI, Ashton et al. 2001; Falqués LAWI) → 격자기반 CEM 대비 **벡터 기반 free-form** 이 신규성(p.5).

## 2. 수치 스킴 (p.5 "Coastline Evolution")

$$\Delta n_i^j = -\frac{1}{D_c}\frac{2(Q_{s,i}^j - Q_{s,i-1}^j)}{L_i}\Delta t \quad (\text{Eq.5})$$

- **staggered forward-time central-space explicit**, Li=√((x_{i+1}−x_{i−1})²+(y_{i+1}−y_{i−1})²) — 코드 `:314-316` 동형(ds=Li/2 표기 차이뿐).
- 국소 해안방위는 인접 2점으로 정의, 각 세그먼트에서 수송 계산(p.5).

## 3. 고각도 불안정 (p.5 "High-Angle Instability")

- 국소각이 임계각 초과 + updrift 측은 미만이면 **downdrift 점 수송을 최대수송(또는 임계각)으로 고정** — 중심차분만으론 불안정, 국소 upwind 처리로 스핏이 매끄럽게 발달(Figure 3 대비). "physics ... same as in Ashton et al. (2001, 2016), Ashton and Murray (2006)" — CEM 거동 계승을 명시. **코드**: `transport.m:125-137`(임계각 클램프)+`get_Sphimax.m`(임계각·QSmax 포물선 반복 탐색).
- 차폐(shadowing): 타 해안·구조물에 의한 파랑 차단, 구조물 스케일≫파장 가정 — 아니면 회절 활성(Elghandour 2018) (p.5).

## 4. 배리어/스핏 월류 (p.5 "Barrier or Spit Overwash")

- Ashton-Murray(2006)의 **최소 배리어폭** 개념: 임계폭 미만 구간은 해측 침식분을 육측에 퇴적해 폭 유지(Leatherman 1979 인용). **코드**: `find_overwash_mc.m`(파향 transect 교차·spitwidth·거리가중 배분).

## 5. 기타 (개관)

- 능동 단면고 = "beach berm height plus ..." 폐합수심 결합(p.13 부근), 검증 케이스: 10년 서향 직선해안 안정성 시험(p.9)·Sand Motor 등.
- 한계·전망(p.17-18): 회절·굴절 근사 향상, cross-shore 과정(Vitousek 2017·Robinet 2018·Antolínez 2019·Palalane-Larson 2020 등) 통합 검토(p.3).
- 수송공식 목록은 Table 1(p.5) — 코드 실분기 7종과의 대조는 [shorelines-transport-formulations](../source-analysis/shorelines-transport-formulations.md) §1.
