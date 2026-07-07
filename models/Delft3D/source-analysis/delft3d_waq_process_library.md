---
title: "Delft3D WAQ 프로세스 라이브러리 — 수질 반응식 (산소·영양염·BOD·질화/탈질·1차생산)"
model: Delft3D
component: waq/waq_process
canonical_source: self
citation_status: verified
verification_method: "Delft3D 소스 직접 read (src/engines_gpl/waq/waq_process/). 재포기 rear.f90(Schmidt/Wanninkhof 식·flux), 질화 nitrif.f90(Michaelis-Menten·O2함수·3버전), 탈질 denwat.f90(O2억제함수), BOD산화 decbod.f90(ultimate BOD 변환·Monod), 산소포화 satoxy.f90(Weiss), 영양염제한 nlalg.f90(MONOD min), detritus 무기화 decdet.f90(전자수용체·영양비 보정), 최소산소 oxymin.f90, 일조함수 dlalg.f90 — 각 file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/README.md
---

# Delft3D WAQ 프로세스 라이브러리 — 수질 반응식

> 경로: `src/engines_gpl/waq/waq_process/` — D-Water Quality(DELWAQ)의 과학식 본체. 각 프로세스가 독립 Fortran 모듈로, 셀(segment) 루프를 돌며 상태변수 농도로부터 반응 flux(`FL`)·출력량을 계산한다. 커널·자료구조·전치(transport)는 [[delft3d_delwaq]] 참조 — 여기는 **수질 반응 formulation(생지화학)** 에 집중.

## 0. 공통 프로세스 루틴 호출 규약

모든 프로세스 루틴은 동일 시그니처를 따른다 (예: `rear.f90:30-32`, `nitrif.f90:31-33`):

```fortran
subroutine <proc>(process_space_real, fl, ipoint, increm, num_cells, &
                  noflux, iexpnt, iknmrk, num_exchanges_u_dir, ...)
```

- `process_space_real(*)` — 입출력 양(I/O) 평탄화 배열. `ipoint(k)`가 k번째 양의 시작 오프셋, `increm(k)`가 셀당 stride (`rear.f90:78-105`, `nitrif.f90:134-152`).
- `fl(*)` — 반환 flux 배열. 셀마다 `iflux = iflux + noflux` 로 진행 (`nitrif.f90:282`).
- 셀 루프 `do iseg = 1, num_cells`, 활성 셀만 처리 — `BTEST(IKNMRK(ISEG),0)` (활성 비트) 또는 `extract_waq_attribute`로 `ikmrk1==1`(물 셀) 판정 (`nitrif.f90:157`, `rear.f90:110-111`).
- `rear`는 추가로 수직층 속성 `ikmrk2`(표층/바닥 구분)를 검사해 표층에서만 재포기 적용 (`rear.f90:120-121`).

라이선스 헤더(GPL v3, Stichting Deltares)는 모든 파일 1-22행 동일.

---

## 1. 용존산소 (Dissolved Oxygen)

### 1.1 산소 포화농도 `satoxy.f90`

헤더 verbatim: `>       Saturation concentration of oxygen` (`satoxy.f90:39`), `COMPUTATION OF OXYGEN SATURATION CONCENTRATION` (`satoxy.f90:45`). 입력 = 수온 `temp`, 염분 `sal`, 방식 switch (`satoxy.f90:95-97`).

**옵션 1 — Weiss (van Gils 표현)** (`satoxy.f90:99-108`): 염분→염소도 변환 `chlorinity_from_sal` 후

$$O_{sat} = \big(14.652 - 0.41022\,T + (0.089392\,T)^2 - (0.042685\,T)^3\big)\,(1 - Cl/10^5)$$

(주의: 소스는 `(0.089392*temp)**2`처럼 계수 포함 항 전체를 거듭제곱 — `satoxy.f90:106-107`.)

**옵션 2 — Weiss (Monteiro/cisr)** (`satoxy.f90:110-118`): $\theta=(T+273)/100$ 의 로그·다항으로

$$O_{sat} = \exp\!\Big(a_1 + a_2/\theta + a_3\ln\theta + a_4\theta + S(b_1 + b_2\theta + b_3\theta^2)\Big)\times 1.428571$$

계수 `a1=-173.4292, a2=249.6339, a3=143.3483, a4=-21.8492, b1=-0.033096, b2=0.014259, b3=-0.0017` (`satoxy.f90:78-84`). 인자 1.428571 = 32·1000/22400 (mL/L → g/m³ 환산, 주석 `satoxy.f90:112`).

### 1.2 재포기 `rear.f90`

헤더 verbatim: `>       Reaeration of carbon dioxide and oxygen` (`rear.f90:38`). 포화백분율 출력 `satperc = o2/oxsat*100` (`rear.f90:117`). `ifrear`(정수 옵션, `rear.f90:127`)로 전달계수 `rearrc`[m/day] 선택 — 14가지(case 0~13):

| ifrear | 공식 | 식 (file:line) |
|---|---|---|
| 0 | 사용자 1/day | `rearrc = rearkl*totdep` (`162`) |
| 2 | Churchill 1962 | `5.026·v^0.969 / H^0.673` (`176`) |
| 3 | O'Connor–Dobbins 1958 | `3.863·v^0.5 / H^0.5` (`184`) |
| 5 | Owens–Edwards–Gibb 1964 | `5.322·v^0.67 / H^0.85` (`200`) |
| 6 | Langbien–Durum 1967 | `11.23·v / H^0.333` (`208`) |
| 7 | Van Pagee/Delvigne | `rearkl·0.065·v_wind² + 3.86·√(v/H)` (`215-216`) |
| 10 | Wanninkhof O₂ | Schmidt수 4차다항·`0.31·v_wind²·(Sc/Sc20)^-0.5·24/100` (`242-249`) |
| 11 | Wanninkhof CO₂ | enhancement `b_enha` 추가 (`262-263`) |
| 13 | Guerin(담수) | `(a·exp(b1·v_wind^b2)+c1·rain^c2)·(Sc/Sc20)^-0.67` (`293`) |

Wanninkhof Schmidt수: 염분>5(해수)일 때 하드코딩 계수 사용 (`a_o=1920.4, b_o=-135.6, …` `rear.f90:67-76`; 적용 `rear.f90:242-247`).

**flux**: Wanninkhof 계열은 온도보정 없이 결손 곱 (`rear.f90:312-313`)

$$F = rearrc\,(O_{sat}-O_2)/H$$

그 외는 온도계수 `reartc^{T-20}` 적용 + 표면피복 보정 `(1-fcover)` + 시간스텝 한계 (`rear.f90:315-320`):

$$F = \min\!\Big(\tfrac{1}{\Delta t},\; \tfrac{rearrc\,(1-fcover)}{H}\Big)\,(O_{sat}-O_2)$$

음의 flux는 현존 산소량으로 제한: `fl1 = max(-o2/delt, fl1)` (`rear.f90:325`).

### 1.3 일 최소 산소 `oxymin.f90`

헤더: `>       Potential daily mimimum dissolved oxygen concentration` (`oxymin.f90:35`). 녹조·규조의 총생산·호흡으로 주야 변동을 추정 (`oxymin.f90:104-117`):

$$PROD = (P_g+R_g)\cdot Green + (P_d+R_d)\cdot Diat,\quad RESP = R_g\,Green + R_d\,Diat$$
$$C_{min} = \min\big(O_2 - 0.5\cdot2.67\,RESP\,(1-DL),\; O_2 - 0.5\cdot2.67\,PROD\,(1-DL)\big)$$

2.67 = O₂:C 화학량비, `DL`=일조비율. 보상(재포기) 발생/미발생 두 추정의 최소값 (주석 `oxymin.f90:99-100`).

---

## 2. 질소 순환 — 질화·탈질

### 2.1 질화 `nitrif.f90`

헤더 verbatim: `>       Nitrification of ammonium + decay of CBOD` (`nitrif.f90:37`), `NITRIFICATION FORMULA COMPOSED OF A ZERO-ORDER TERM, AND MICHAELIS-MENTEN TERMS FOR AMMONIUM AND OXYGEN` (`nitrif.f90:43-44`). `IVERSN`(`nitrif.f90:159`)으로 3버전 분기.

**신버전(IVERSN=1)** (`nitrif.f90:163-210`): 임계온도 `CRTEMP`·임계산소 `CROXY` 미만이면 MM율 0 (`nitrif.f90:181`), 그 외 zero차+MM:

$$AMFUNC = \frac{NH_4}{K_{SAM}\cdot poros + NH_4},\quad OXFUNC = \frac{O_2}{K_{SOX}\cdot poros + O_2}$$
$$F_{nit} = K0NIT + KNIT\cdot TC^{T-20}\cdot AMFUNC\cdot OXFUNC$$

(`nitrif.f90:197-199`). 산소·암모늄 가용성 한계(안전계수 0.5/0.9, 질화 화학량비 `NOX_RATIO=4.57` gO₂/gN) (`nitrif.f90:203-205`):

$$F_{nit} \le \min(0.5\,O_2/4.57/\Delta t,\; 0.9\,NH_4/\Delta t)$$

**TEWOR 버전(IVERSN=2)** (`nitrif.f90:215-226`): 단순 1차 `RC·NH4·OXFUNC`.

**구버전(IVERSN=0)** (`nitrif.f90:234-276`): 산소함수 `O2FUNC`를 임계 `OOX`/`COX` 사이에서 보간하되 skewness 거듭제곱 적용 (`nitrif.f90:258-261`), 온도≤임계면 zero차만 (`nitrif.f90:266-271`).

### 2.2 탈질(수주) `denwat.f90`

헤더 verbatim: `>       Denitrification in water column` (`denwat.f90:38`). 산소 **억제**가 핵심.

**신버전(IVERSN=1)** (`denwat.f90:211-255`): 온도≥임계 또는 산소≥임계면 MM율 0 (`denwat.f90:228`):

$$NIFUNC = \frac{NO_3}{K_{SNI}\cdot poros + NO_3},\quad OXFUNC = 1 - \frac{O_2}{K_{SOX}\cdot poros + O_2}$$
$$F_{den} = K0DEN + KDEN\cdot TC^{T-20}\cdot NIFUNC\cdot OXFUNC$$

(`denwat.f90:247-251`). 산소 음수면 `OXFUNC=1` (`denwat.f90:249`).

**구버전(IVERSN=0)**: 산소억제함수를 임계 `OOXDEN`(상한 1)·`COXDEN`(하한 0) 사이 곡률 `CURVAQ = -log(1)+exp(CURVA)`로 비선형 보간 (`denwat.f90:182-191`, 동일식 `286-294`):

$$O2FUNC = \frac{COXDEN\cdot poros - O_2}{(COXDEN-OOXDEN)poros + CURVAQ\,(O_2 - OOXDEN\cdot poros)}$$
$$F_{den} = DENR + DENRC\cdot TC^{T-20}\cdot NO_3\cdot O2FUNC$$

(`denwat.f90:310`). 온도계수·산소항이 공간균일하면 루프 밖 1회 계산(최적화) (`denwat.f90:146-200`).

---

## 3. BOD 산화 `decbod.f90`

헤더 verbatim: `>       Oxydation of BOD-fractions with Monod kinetics for the TEWOR models` (`decbod.f90:37`), `Oxydation of three fractions of BOD (background, sewage overflow slow and fast settling) via MONOD-kinetics` (`decbod.f90:43-44`). 3 BOD pool.

**BOD₅ → ultimate BOD 변환** (`decbod.f90:161-163`):

$$BODU_i = \frac{BOD5_i}{1 - e^{-5\,RCBOD_i}}$$

(5일 누적분으로부터 1차반응 가정 ultimate 환산.)

**산소제한(Monod)** (`decbod.f90:167`): $OXFUNC = O_2/(KMOX+O_2)$.

**flux**(`decbod.f90:171-177`): 각 pool `dBOD5_i = RCBOD_i·OXFUNC·BOD5_i`, 산소소비 `OXYDEM = Σ RCBOD_i·OXFUNC·BODU_i`. 출력으로 총 BOD5/BODU 합산 (`decbod.f90:191-195`). RCBOD<1e-10이면 정지(0 방지) (`decbod.f90:140-157`).

관련: 별도 질화에 의한 산소소비(CBOD decay)는 `nitrif.f90` 헤더에 명시되나 본체는 질화 flux 중심.

---

## 4. 영양염 제한·1차생산 (DYNAMO 계열)

### 4.1 영양염 제한함수 `nlalg.f90`

헤더 verbatim: `>       Nutrient limiation function for DYNAMO algae` (`nlalg.f90:37`). MONOD 제한 후 **최소값 법칙(Liebig)**:

$$DIN = NO_3/AMOPRF + NH_4 \quad(\text{NH}_4\text{ 우선이용 }AMOPRF\text{ 보정})$$

(`nlalg.f90:101`). 음수 농도면 0 처리 (`nlalg.f90:102, 107, 115`).

$$FN = \frac{DIN}{DIN+K_{MDIN}},\; FP = \frac{PO_4}{PO_4+K_{MP}},\; FS = \frac{Si}{Si+K_{MSi}}$$
$$F_{nut} = \min(FN, FP, FS)$$

(`nlalg.f90:105-121`). 규소 `KMSI==-1`이면 비규조로 보고 `FS=1` (`nlalg.f90:113-114`).

### 4.2 일조함수 `dlalg.f90`

헤더 verbatim: `>       Daylength function for algae DYNAMO` (`dlalg.f90:37`). 성장포화 일조 대비 정규화 (`dlalg.f90:77`): $f_{DL} = \min(DL, KMDL)/KMDL$.

(온도함수 `tfalg.f90` = `>       Temperature functions for algae growth and mortality`, `tfalg.f90:35` — ⚠ 본문 식 미인용, source-needed.)

---

## 5. 유기물 무기화 (detritus mineralisation) `decdet.f90`

헤더 verbatim: `>       Mineralisation & conversion of detritus POC1,POC2,POC3,POC4,DOC` (`decdet.f90:43`). 입자성 유기 C/N/P/Si의 분해·전환(DOC화) flux.

**화학량비 의존 분해율** (`decdet.f90:323-356`): POC 대비 N·P 비율이 상·하한 사이면 상하한 율을 선형보간 (`decdet.f90:348-354`):

$$FNUT = \min\!\Big(\tfrac{(PON/POC)-ALN}{AUN-ALN}, \tfrac{(POP/POC)-ALP}{AUP-ALP}\Big),\quad RC20 = RC20_{LO} + FNUT(RC20_{UP}-RC20_{LO})$$

**보정계수** (`decdet.f90:363-390`): 온도 `TEMPC = TC^{T-20}` (`363`); 전자수용체 `ELFACT` = 1(호기, O₂>0.1) / `B_NO3`(탈질, NO₃>0.1) / `B_SULF`(황산염환원) (`367-373`); 영양 stripping `N_FACT/P_FACT/S_FACT`를 [0.5,5] clamp (`378-386`).

**flux** (`decdet.f90:395-409`): 무기화 `DECOC = RC20C·TEMPC·ELFACT·POC`, DOC/POC 전환 분배 `CNVPC = B_DTP·DECOC`, `CNVDC = B_DTD·DECOC`. N/P/S는 `N_FACT` 등으로 추가 보정 (`decdet.f90:399-409`), 출력 flux 배열에 적재 (`decdet.f90:423-428`).

---

## 6. 본 노트가 다루지 않는 인접 영역

- 커널·통합·전치 스킴, 프로세스 등록 메커니즘 → [[delft3d_delwaq]]
- 동적 식물플랑크톤 종조성 모델(BLOOM): `waq_process/bloom/`, protist: `waq_process/protist/` — ⚠ 본 노트 미분석, source-needed
- ✅ 퇴적물 산소요구·매몰(SOD, sediment flux): `sedox.f90`(SODCH4 sech 반복해법+메탄)/`botmin.f90`(S1/S2 무기화)/`sedsod.f90` — [[delft3d_waq_sediment_oxygen_demand]] 로 해소(2026-07-07, verified)
- CO₂/CH₄ 포화: `satco2.f90`/`satch4.f90` — 파일 존재만 확인, source-needed

> 전체 프로세스 파일 184개(`waq_process/` 최상위 ls 기준). 본 노트는 산소·N순환·BOD·1차생산제한·무기화의 **대표 루틴**만 식 단위로 인용했다.
