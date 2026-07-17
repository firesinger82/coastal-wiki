---
title: "이론 ch11 — 스펙트럼 파랑모델링: wave action 보존 · 5D action balance · 3세대 소스항 (SWAN claim-level 분해)"
topic: waves
layer: 1
depends_on:
  - textbook/notes/theory-ch08-linear-waves.md
  - textbook/notes/theory-ch09-nonlinear-spectra.md
canonical_source: self
citation_status: verified
provenance: "교재 프로젝트 textbook-ai-data-full ch11(AI 합성 MDX, 무인용) 이식분 — 2026-07-17 claim-level 분해(THEORY-LEDGER 방침: 일반 이론만 ①, SWAN 구현·운용 서술은 models/SWAN 링크·복제 금지) + 같은 날 Codex 게이트(18회차) MODIFY 반영. 주 출처 = **holthuijsen2007**(§7.3.5 해류-파 상호작용·§8.4 천해 에너지/action balance·§6.4.7 모델 세대 구분·§9 SWAN·부록 D). ★원문 오류 정정 1건: 'Komen et al. (1984) = 1세대 모델' → Komen 1984 는 WAM Cycle III(3세대) 바람입력·whitecapping 폐합 계수의 출처(p.308-309·312, 게이트 APPROVE). ★게이트 정정: **Thornton & Guza 1983 = p.92-93 실존**(가중 Rayleigh 쇄파 파고 분포 Eq.4.2.30-31, '문헌리스트뿐' 오판 철회·복원 — 단 'SWAN 옵션' 단언 자체는 여전히 미지지)·S_bfr Eq.9.3.29 = 미러 OCR 훼손으로 전사 보류했다가 **원 PDF 인쇄 p.295 직접 실측으로 해소(2026-07-17)** — $S_{bfr}=-(C_{bfr}/g)[\\sigma/\\sinh(kd)]^2 E u_{rms,bottom}$, 게이트 제안식과 일치·Doppler Eq.D.4 p.355→**p.356**·cσ 식 U∂d/∂s 표기 정정·Cycle IV β = Komen et al. 1994 귀속(γ·τwave 만 Janssen 1991a)·Eq.9.3.4 '무해류' 조건 보강·'3세대 지배방정식'→phase-averaged 수송방정식으로 완화·§6 경계 축소(스펙트럼 이산화 상세·SWAN 능력 서술 → models 축, swan-action-balance.md 우선링크 제외). 미이식(모델 축 소유) 6: Yan 1987 'SWAN 옵션'(본문 무단언 — 문헌 p.201 뿐; 공식 SWAN 문서는 models 축에 존재)·주파수 25-40 bin·방향 36 bin 운용 설정·SWAN 1.0 1993/40.x 연표·INPUT 파일·실행 워크플로(11.6)·EFDC 결합 상세·축산항(11.8)·워크예제(11.9). 삭제 4: 'WAM=NOAA WaveWatch 전신'(WAVEWATCH=Tolman 1991 별도 모델, p.305 fn1)·MIKE 21 SW(textbook/md 코퍼스 0건)·'정상상태=입력=소산' 일반화(미확인)·MDX c_θ 식(코퍼스 Eq.7.3.33 과 불일치 — 전사 제거, 코퍼스 형으로 대체). 43 단언 중 33 부착(77%)·10 삭제/미이식·source-needed 0."
verification_method: "holthuijsen2007 p.92-93(§4.2.2 Thornton-Guza 1983 가중 Rayleigh)·p.212-214(§6.4.7 1·2·3세대)·p.238-239(§7.3.5 cσ Eq.7.3.32·cθ Eq.7.3.33·action A=E/σ Bretherton & Garrett 1969)·p.276-278(§8.4 θ-공간 전파항·Eq.8.4.3·5D fn7)·p.302(Fig.8.19 천해 에너지 흐름)·p.304-317(§9 SWAN: key concepts·Eq.9.3.1-4 action balance·소스항 정식·수치 근거)·p.353-356(부록 D: cg+U 벡터합 p.353·Doppler Eq.D.4 p.356) — textbook/md 미러 ---PAGE-N--- 마커 실측 대조 (2026-07-17, Codex 게이트 18회차 재검증 포함)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-17
related:
  - textbook/notes/theory-ch08-linear-waves.md
  - textbook/notes/theory-ch09-nonlinear-spectra.md
  - textbook/notes/theory-ch10-coastal-transformation.md
  - textbook/notes/theory-ch01-conservation.md
---

# 스펙트럼 파랑모델링 — wave action 보존 · action balance · 3세대 소스항

> 4-레이어 **① 이론** 노트 — **claim-level 분해**: ch11 원문(SWAN 챕터)에서 **일반 스펙트럼 파랑모델링 이론**만 이식. SWAN 고유의 수치기법·명령·운용은 `models/SWAN/`(manual-notes·source-analysis)이 canonical — 여기서는 탐색 링크만.
> 근거 의존(①→①): 스펙트럼·quadruplet [[theory-ch09-nonlinear-spectra]] · 군속도·분산·파 에너지 [[theory-ch08-linear-waves]].
> 탐색 링크(근거 의존 아님): 굴절·천수 [[theory-ch10-coastal-transformation]] · 마스터 보존법칙 형식 [[theory-ch01-conservation]] · `models/SWAN/`.

## 1. 왜 energy 가 아닌 action 인가

- **해류가 있으면 파 에너지는 보존되지 않는다**: 해류가 radiation stress 에 대해 일을 하며 파와 에너지를 교환 (holthuijsen2007, p.239, §7.3.5; Longuet-Higgins & Stewart 1960-1964 계보). 대신 **wave action $A=E/\sigma$** (에너지 ÷ 상대 각주파수)가 보존됨 (holthuijsen2007, p.239; Bretherton & Garrett 1969·Mei et al. 2006 귀속).
- 따라서 **파-해류 상호작용을 다루는 파랑모델은 에너지 balance 가 아닌 action balance 방정식 기반** (holthuijsen2007, p.239).
- 상대 주파수 $\sigma$ 는 해류와 함께 움직이는 좌표계의 주파수 — 분산관계 $\sigma^2=gk\tanh(kd)$ 가 그대로 성립하고(근거 [[theory-ch08-linear-waves]] §1), 고정 좌표계의 절대 주파수와는 **Doppler 이동** $\omega=\sigma+\mathbf{k}\cdot\mathbf{U}$ 로 연결 (holthuijsen2007, 부록 D, Eq. D.3 p.355·Eq. D.4 p.356).

## 2. 스펙트럼 balance 방정식 — 4D 에서 5D 로

- **연안 에너지 balance (4D)**: 심해 balance 에 **방향 공간($\theta$) 전파항**을 추가 — 굴절·회절로 파향이 돌아가는 것을 방향 bin 간 에너지 수송으로 표현: $\dfrac{\partial E}{\partial t}+\dfrac{\partial c_{g,x}E}{\partial x}+\dfrac{\partial c_{g,y}E}{\partial y}+\dfrac{\partial c_\theta E}{\partial\theta}=S$ (holthuijsen2007, p.276-278, §8.4.1, Eq. 8.4.3; 유도 = 방향 bin 순 유입 Eq. 8.4.1). 연안에선 $c_g$ 가 수평 변하므로 미분 밖으로 못 꺼냄 (p.278).
- **해류·시변 수심 → 5D**: 개별 성분의 주파수도 변하므로 **$\sigma$-공간 전파항**을 추가해 $t,x,y,\sigma,\theta$ 5차원에서 정식화 — 해류 존재 시 절대 주파수 $f$ 대신 상대 주파수 $\sigma$ 사용 (holthuijsen2007, p.276, §8.4.1 각주 7).
- **스펙트럼 action balance 방정식** (파-해류 상호작용을 다루는 phase-averaged 스펙트럼 파랑모델의 수송 방정식; action 밀도 $N(\sigma,\theta)=E(\sigma,\theta)/\sigma$): $$\frac{\partial N}{\partial t}+\frac{\partial c_{g,x}N}{\partial x}+\frac{\partial c_{g,y}N}{\partial y}+\frac{\partial c_\sigma N}{\partial\sigma}+\frac{\partial c_\theta N}{\partial\theta}=\frac{S(\sigma,\theta)}{\sigma}$$ — 1항 국소 시간변화, 2·3항 지리 공간 전파(군속도, 천수 포함), 4항 수심·해류에 의한 상대주파수 이동, 5항 수심·해류 유발 굴절(회절은 근사 옵션), 우변 = 에너지 밀도 소스항을 $\sigma$ 로 나눈 action 소스항 (holthuijsen2007, p.306-307, §9.3.1, Eq. 9.3.1; 구면좌표 대규모형 Eq. 9.3.3).
- **무해류 극한에서 에너지 balance 로 환원**: 주파수 이동이 없어져 Eq. 9.3.1 이 에너지 balance(Eq. 9.3.2)로 축소 (holthuijsen2007, p.306). **정상·1D·무해류 상황은 1차원 정상 에너지 balance** $\partial(c_{g,x}E)/\partial x+\partial(c_\theta E)/\partial\theta=S$ 로 대폭 축소 — 계산량 절감 (p.307, Eq. 9.3.4, "stationary, one-dimensional, no currents").
- 형식은 임의 보존량의 마스터 balance([[theory-ch01-conservation]] §6, holthuijsen 부록 E)의 스펙트럼 위상공간 버전 (탐색).

## 3. 해류가 파 전파에 미치는 효과 — 전파 속도들

- **에너지 수송 방향 = $\mathbf{c}_g+\mathbf{U}$ 벡터합**: 해류가 있으면 에너지는 파향(orthogonal, 마루 법선)과 다른 방향(wave ray)으로 수송 — 일부 에너지가 마루를 따라 흐름 (holthuijsen2007, p.353, 부록 D §2; 그림 p.238 Fig. 7.15).
- **주파수 이동 $c_\sigma$**: 시변 수심·해류 위를 이동하는 파의 상대주파수 변화율 $c_\sigma=\dfrac{\partial\sigma}{\partial d}\left(\dfrac{\partial d}{\partial t}+U\dfrac{\partial d}{\partial s}\right)-c_g k\dfrac{\partial U_n}{\partial n}$ ($U$ = 유선방향 해류 속력, $s$ = 유선 좌표) (holthuijsen2007, p.238, §7.3.5, Eq. 7.3.32; 유도 부록 D §3).
- **방향 전환율 $c_\theta$ (수심+해류 굴절)**: $c_{\theta}=-\dfrac{c_g}{c}\dfrac{\partial c}{\partial m}-\dfrac{\partial U_n}{\partial m}$ — 1항 수심 유발, 2항 해류 유발 굴절(마루 방향 $m$ 을 따른 파향 법선 해류 $U_n$ 의 변화) (holthuijsen2007, p.239, §7.3.5, Eq. 7.3.33; 유도 p.353-355 부록 D Eq. D.1-D.2). ※원 교재의 $c_\theta$ 식은 코퍼스와 불일치 — 전사 제거, 코퍼스 형으로 대체. 순수 수심 굴절은 [[theory-ch10-coastal-transformation]](탐색).

## 4. 3세대 소스항 물리 — $S=S_{in}+S_{nl4}+S_{nl3}+S_{wc}+S_{bfr}+S_{surf}$

3세대 연안 모델의 소스항 = 바람 생성 + 비선형 상호작용(quadruplet·triad) + 소산 3종(whitecapping·바닥마찰·수심 유발 쇄파) (holthuijsen2007, p.304, §9.1; 소산 3분류 p.312, §9.3.4). 천해 스펙트럼 에너지 흐름 전체상: 바람 → triad·quadruplet 재분배 → 저주파(피크 이동·infra-gravity)·고주파(2차 피크 가능) + 전 주파수 쇄파 소산·저중주파 바닥마찰 (holthuijsen2007, p.302, Fig. 8.19).

- **$S_{in}$ 바람 입력**: Miles 공명 피드백 + 초기 성장의 합 $S_{in}=\alpha+\beta E(\sigma,\theta)$ — 초기 성장 $\alpha$ 는 Cavaleri & Malanotte-Rizzoli (1981) 경험식 (holthuijsen2007, p.308, Eq. 9.3.7-9.3.9). 구동 입력은 10 m 풍속 $U_{10}$, 내부적으로 마찰속도 $u_*^2=C_D U_{10}^2$ 로 변환 (p.307-308, Eq. 9.3.5; $C_D$ = Wu 1982, Eq. 9.3.6). 지수 성장 계수 $\beta$: **WAM Cycle III 계열 = Snyder et al. (1981)·Komen et al. (1984)**, **Cycle IV 계열 = Komen et al. (1994) 의 $\beta$ 정식** — 성장률 $\gamma$·유효 표면조도·파 유발 응력 $\tau_{wave}$ 피드백은 Janssen (1991a) (p.308-309, Eq. 9.3.10-9.3.16). ★원 교재의 "Komen et al. (1984) = 1세대 모델" 은 오류 — Komen 1984 는 3세대 WAM Cycle III 의 바람입력·whitecapping 폐합 계수 출처 (p.308-309·312).
- **$S_{nl4}$ quadruplet 4파 상호작용**: 공명 4파 간 에너지 재분배 — 정식화는 Hasselmann (1962) Boltzmann 적분(근거 [[theory-ch09-nonlinear-spectra]] §5). 운용 계산은 **DIA (discrete-interaction approximation, Hasselmann et al. 1985a)** — 2개 quadruplet 배치($\lambda=0.25$, $\theta=\mp11.5°/\pm33.6°$)로 근사 (holthuijsen2007, p.310, §9.3.3, Eq. 9.3.17-9.3.20). 유한수심은 심해 값에 스케일 인자 $R(k_{peak}d)$ 곱 (p.311, Eq. 9.3.21-22; Hasselmann & Hasselmann 1981). DIA 는 근사 — near-exact Xnl(WRT, van Vledder 2006)은 연구용(운용엔 과대 계산) (p.310, 각주 4).
- **$S_{nl3}$ triad 3파 상호작용 (천해)**: 얕은 물에서 3파 공명이 고조파 생성 — 운용 계산은 **LTA (lumped-triad approximation, Eldeberky 1996)**, Ursell 수 $>0.1$ 일 때만 적용, 상호작용 계수는 Madsen & Sørensen (1993) (holthuijsen2007, p.310-311, Eq. 9.3.23-9.3.24).
- **$S_{wc}$ whitecapping (심해 쇄파)**: 파가 가팔라져 마루가 부서지는 소산 — pulse 기반 모델 (Hasselmann 1974; WAMDI 1988 채택) $S_{wc}=-\mu k E(\sigma,\theta)$, 계수 $\mu$ 는 전체 파형경사 $\tilde s=\tilde k\sqrt{m_0}$ 에 의존 (holthuijsen2007, p.312, Eq. 9.3.25-9.3.26). 계수는 이상화된 심해 성장의 에너지 balance 폐합으로 튜닝(Komen et al. 1984)되어 **고주파 cut-off 처리에 민감** — 모델 간 성장률 차이의 원인 (p.312-313).
- **$S_{bfr}$ 바닥 마찰**: 대륙붕 모래 바닥의 지배적 바닥 소산 $S_{bfr}(\sigma,\theta)=-\dfrac{C_{bfr}}{g}\left[\dfrac{\sigma}{\sinh(kd)}\right]^2 E(\sigma,\theta)\,u_{rms,bottom}$ (holthuijsen2007, p.313, Eq. 9.3.29 — **원 PDF 인쇄 p.295 직접 실측 2026-07-17**, 미러 OCR 훼손분 해소). 계수 모델 3종: **경험적 JONSWAP** (Hasselmann et al. 1973; $C_{bfr}=0.038/u_{rms,bottom}$ swell · $0.067/u_{rms,bottom}$ wind-sea, Bouws & Komen 1983), **drag-law Collins (1972)** ($C_{bfr}=0.015$), **eddy-viscosity Madsen et al. (1988)** ($C_{bfr}=f_w/\sqrt2$, Eq. 9.3.30) — 현장 데이터로는 우열 판정 불가 (p.313). ※원 교재는 JONSWAP·Madsen 2종만 언급 — 코퍼스 기준 3종으로 보강.
- **$S_{surf}$ 수심 유발 쇄파**: 천해 불규칙 파랑의 총 소산을 **bore 소산 모델** (Battjes & Janssen 1978)로 기술 — 국소 최대 파고 $H_{max}=\gamma D$($D$ = set-up 포함 총수심, breaker 계수 $\gamma$ 기본 0.73) (holthuijsen2007, p.314, §9.3.4). 쇄파 한계·유형은 [[theory-ch09-nonlinear-spectra]] §2(근거). **쇄파 파고의 통계 기술 = Thornton & Guza (1983) 가중 Rayleigh**: Rayleigh 분포에 가중함수 $W(H)$ 를 곱해 쇄파만의 밀도함수 $p^*_{Hbr}(H)$ 를 적합($\gamma\approx0.42$·$n=4$ 제안) — surf zone 소산 추정(§8.4.5 문맥)에 사용 (holthuijsen2007, p.92-93, §4.2.2, Eq. 4.2.30-4.2.31). ※'SWAN $S_{surf}$ 옵션 = Thornton-Guza' 라는 원 교재 단언 자체는 코퍼스 미지지 — 모델별 옵션 목록은 `models/SWAN/` 축.

## 5. 파랑모델 세대 구분 (1·2·3세대)

- **1세대**: quadruplet·whitecapping 을 명시 계산하지 않고 — 바람입력 계수를 증폭($B\approx5\beta$)해 관측 성장을 재현하고, 스펙트럼 상한 $E_{lim}$(JONSWAP/PM $f^{-5}$ tail)을 강제해 whitecapping 을 모사 (holthuijsen2007, p.213, §6.4.7, Eq. 6.4.23-24). overshoot 현상 재현 불가·tail 형상 강제가 한계 (p.213).
- **2세대**: quadruplet 을 사전계산 근사(JONSWAP 스펙트럼용)로 대체하거나, wind-sea 를 JONSWAP 매개변수 진화식 + swell 전파로 나누는 hybrid — tail 은 여전히 $f^{-5}$·$f^{-4}$ 강제 (holthuijsen2007, p.213-214).
- **3세대**: quadruplet 을 **DIA 로 명시 계산**하고 스펙트럼 형상을 **a priori 강제 없이 자유 발달**시킴 — prototype 은 **WAM** (WAMDI group 1988; Komen et al. 1994) (holthuijsen2007, p.214, §6.4.7).
- **SWAN 은 3세대 연안 모델** (Booij et al. 1999; 자유 이용 오픈소스): 심해 물리(바람·quadruplet·whitecapping·바닥마찰) 정식은 **WAM 과 동일**하고, 천해 과정(수심 유발 쇄파·triad)을 보강 (holthuijsen2007, p.304 §9.1-9.2·p.306 §9.2). 대양용 3세대 모델로는 WAM·WAVEWATCH(Tolman 1991)가 있고 연안 고해상도(≲1 km)에는 explicit 전파의 Courant 제약 때문에 비경제 (p.305, §9.2 + 각주 1).

## 6. 모델 구현·수치·운용 = `models/SWAN/` (claim-level 분해 경계)

- **연안에서 implicit 기법을 쓰는 이유**(일반 원리만): explicit 전파 기법은 Courant 조건에 묶여 연안 고해상도에서 비경제 — implicit up-wind 는 무조건 안정이라 큰 time step 허용 (holthuijsen2007, p.305, Eq. 9.2.1·p.317, §9.5.2). 이산화·sweep·수렴 등 수치 상세는 모델 축.
- **수치 상세·명령·운용은 모델 축이 canonical(복제 금지)**: 지배방정식 구현 `models/SWAN/manual-notes/swan-tech-ch2-governing-equations.md` · 소스항 구현 `swan-tech-ch2-sources-sinks.md`·`swan-tech-ch2-dissipation-detailed.md`·`swan-tech-ch2-nonlinear-detailed.md` · 이산화·sweep `swan-tech-ch3-discretization.md`·반복해법 `swan-tech-ch3-solution-iteration-limiter.md` · 격자·명령 `swan-command-setup-grid-reference.md` · 창립 논문 `swan-booij-1999-jgr-foundational.md`·`web-refs/swan-foundational-papers.md` (탐색). (※`swan-action-balance.md` 는 본 노트와 범위 중복 + 서지 연도·계수 이견이 있어 우선 링크에서 제외 — 게이트 18회차 지적, 후속 대조 대상.)
- **유체모델 결합의 이론적 접점**: radiation stress 구배(파 유발 force)를 별도 유체역학 모델에 전달해 해류·수위를 풀고, 그 결과를 파 계산에 되먹임(정상 케이스 반복·비정상 케이스 주기 교환)하는 구조 (holthuijsen2007, p.314-315, §9.4). radiation stress 이론은 [[theory-ch10-coastal-transformation]] §4(탐색) · 모델별 지원 범위(회절 근사 여부·파 유발 해류 미계산 등)와 EFDC 측 구현은 `models/SWAN/`·`models/EFDC/` 축(탐색).

## 7. 연결

- [[theory-ch08-linear-waves]] — 분산관계·군속도·파 에너지 (근거 의존)
- [[theory-ch09-nonlinear-spectra]] — 스펙트럼 기술·quadruplet Hasselmann 1962·쇄파 한계 (근거 의존)
- [[theory-ch10-coastal-transformation]] — 천수·굴절·radiation stress (탐색)
- [[theory-ch01-conservation]] — 마스터 보존법칙 형식 (탐색)
- `models/SWAN/` — 구현·수치·명령·운용 canonical (탐색) · `models/EFDC/` — 파-흐름 결합 수리동역학 측 (탐색)
- 다음: ch15 EFDC 운용 claim-level 분해 — T트랙 마지막.
