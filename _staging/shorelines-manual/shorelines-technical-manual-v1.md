---
title: "ShorelineS Technical Manual v1.0 발췌 — 수송 7공식·회절 2종·투과 3식·사구/월류·파라미터 기본값"
model: ShorelineS
component: manual-notes
canonical_source: self
citation_status: verified
verification_method: "repo `doc/ShorelineS_manual_v1.0.pdf` 66쪽 전수 — 표지·목차·본문 p1-16 렌더 직독 + p17-66 pdftotext -layout 추출 직독. 식·기본값·키워드 verbatim 전사, 쪽번호는 PDF 내부 표기('N of 66')를 따른다. 기존 source-analysis 5노트의 코드 실측과 대조해 §9에 확인·확장·불일치를 분리 기록. §9.3 의 매뉴얼 내부 불일치 3건은 snapshot f3ec863 의 소스를 직접 읽어 판정했다 — initialize_defaultvalues.m:158,193 / wave_diffraction.m:106-118,373-374 / transport.m:10,140,194 / prepare_structures.m:114 / prepare_dunes.m:96. ※파일 인코딩 ISO-8859+CRLF(grep -a 필요)."
note_author: "Claude Opus 5"
note_date: 2026-09-22
related:
  - models/ShorelineS/README.md
  - models/ShorelineS/manual-notes/shorelines-faq-operational.md
  - models/ShorelineS/manual-notes/shorelines-roelvink2020-frontiers.md
  - models/ShorelineS/source-analysis/shorelines-transport-formulations.md
  - models/ShorelineS/source-analysis/shorelines-diffraction-mud-topology.md
  - models/ShorelineS/source-analysis/shorelines-coastline-change.md
---

# ShorelineS Technical Manual v1.0 — 발췌

> 출처: repo `doc/ShorelineS_manual_v1.0.pdf`, 66쪽. 저자 Bas Huisman·Dano Roelvink·Anouk de Bakker·Anne de Beer·Vassia Dagalaki, 검토 Johan Reyns (p2). 발행 **2024-10-15**, Deltares·IHE Delft·UNESCO 로고 (p1).

## 0. 판본과 범위 — 스냅샷보다 앞선 문서다

- **적용 대상**: "This manual applies to ShorelineS version 1.0 also known as the 'TKI' release" (p5 §1.3).
- **성격**: "technical reference guide" — 입력 명세 + 기능 배후 물리 + 수치 구현 (p5 §1.1). 튜토리얼이 아니다.
- ⚠**시점 어긋남**: 매뉴얼은 2024-10-15 자인데 본 위키의 소스 스냅샷은 `f3ec863`(2026-08-13, 코드는 `7bf4481ab` 2025-10-07 과 동일)이다. 즉 **매뉴얼이 코드보다 약 1년 앞선다.** 매뉴얼과 코드가 어긋나는 지점은 매뉴얼이 낡았을 가능성을 먼저 본다(§9).

## 1. 모델 정체와 타 모델 대비 위치

"open-source numerical model for coastal planform evolution, based on one-dimensional equations for alongshore sediment transport and mass conservation, on a free-form grid" (p6 §2.1). 해안선 구간은 자유 변형·합병·분리하며 undulation·섬·스핏·salient·tombolo 를 형성한다.

매뉴얼이 직접 제시한 3자 비교 (p8 Table 1 — 발췌):

| | Coastline models (e.g. Unibest) | **ShorelineS** | Field models (e.g. XBeach, Delft3D) |
|---|---|---|---|
| 사구 침식/월류 | no | **equilibrium**(*1 파라미터화된 bypass) | not or detailed(*2) |
| 사구 성장 | no | **yes** | experimental(*3 Delft3D FM-Aeolis) |
| 스핏·고각도 파랑 | no | **yes** | yes, takes long |
| 하구/조석 수송 | no | **inlet only**(*5 조석 inlet 유지용 river function) | yes |
| 퇴적물 | sand | **sand & partially mud**(*8 mud 는 연안수송 + mud flat 체적요소 보존) | sand & mud |
| 이안제 | difficult(*6) | **yes**(*9 회절·투과 모두 고려) | yes(*7) |
| 적용 난이도 / 셋업 기간 | difficult / weeks | **easy / ~week** | moderate–hard / >month |
| 결과 상세도 | low | **moderate / high** | high |

각주 번호는 원문 표기(*1…*9)를 그대로 옮겼다 (p8).

## 2. 지배식과 수치 (p11-12 §3.1.2-3.1.3)

질량보존 (식 1):

$$\frac{\partial n}{\partial t} = -\frac{1}{D_c}\frac{\partial Q_s}{\partial s} - \frac{RSLR}{\tan\beta} + \frac{1}{D_c}\sum q_i$$

`n` 횡단거리, `s` 연안거리, `Dc` 활성 단면고(m), `Qs` 연안표사(m³/yr), `tanβ` 사구/배리어 마루~폐쇄수심 평균경사, `RSLR` 상대해면상승(m/yr), `qi` 횡단수송·월류·양빈·채사·하천/조석 inlet 교환 source/sink (m³/m/yr).

시간적분은 **staggered forward time–central space explicit** (식 2, p11):
$\Delta n_i^j = -\frac{1}{D_c}\frac{2(Q_{s,i}^j - Q_{s,i-1}^j)}{L_i}\Delta t$, $L_i=\sqrt{(x_{i+1}-x_{i-1})^2+(y_{i+1}-y_{i-1})^2}$. 좌표 갱신은 식 3이며 "The scheme can be shown to be conserving the land area (Roelvink et al., 2020)" (p12).

**활성 단면고 `Dc`**: 내측 폐쇄수심(Hallermeier 1981)~사구 발끝이 전형. 세립·수십년 규모에서는 외측 폐쇄수심(Hallermeier 1983) 또는 이동성 기반 폐쇄수심(Hallermeier 1978)이 낫다. 키워드 `d`, 공간변화형은 `d=[x1,y1,hactive1; x2,y2,hactive2; ...]` (p12 §3.1.3). **"there is a linear relationship between the active height and the response of the coast to gradients in alongshore sediment transport"** — 캘리브레이션 1순위 노브라는 뜻이다.

## 3. 격자와 시간증분 (p12-15)

- **격자 `ds0`**: 전형 50-100 m. "grid resolutions of <=O(10) meter pose some difficulties for a stable model run" (p12 §3.1.4). 격자는 매 timestep 자동 재생성되며 **70%~140%** 범위를 벗어나면 점 삽입/삭제. `griddingmethod=2`(기본, 전면 재보간) / `=1`(해당 셀만 분할·병합, **덜 확산적**).
- **공간변화 격자**: `griddingmethod=1` + `ds0=[x1,y1,ds1; ...]` (p13 §3.1.5).
- **격자 평활** (식 4, p13): 3점 `s_{i,smooth}=f·s_{i-1}+(1-2f)·s_i+f·s_{i+1}`. **기본 f=0** — "to avoid artificial diffusion in the numerical scheme". 과평활은 planform 면적 손실을 부른다.
- **전빈 방위 `phif`** (p13-14 §3.1.7): 폐쇄수심 바깥의 준정적 전빈. 미지정이 기본(초기 해안선을 심해 전빈으로 간주, 기간 내 불변) / 고정값(`phif=270`) / 공간변화 / `phif={'gaussian',7}`(7셀 평활).
- **적응 시간증분** (식 5-7, p14 §3.2.2, Vitousek & Barnard 2015): $\Delta t < D_c\Delta s^2/(4Q_{max})$, $\varepsilon_{max}=2Q_{max}/D_c$. `tc` 로 이 자동증분의 비율 지정(`tc=0.9`=90%). **자동증분과 입력 파랑자료 시간간격의 최솟값**을 쓰므로 파랑조건을 건너뛰지 않는다.
- **고정 시간증분** (p15 §3.2.3): `tc=0`+`dt`(년 단위, `dt=1/365`=1일). 전형 3시간~1일. 고정증분에서는 구간 내 파랑조건을 **'에너지 벡터' 평균**으로 집약한다(3시간 자료·1일 증분이면 8개를 벡터합→평균→가중평균 조건으로 환산).
- **사구 부증분 `dtdune`** (p15 §3.2.4): 연 단위 분수. 해안선 증분보다 클 수 없다.

## 4. 파랑·조석·수위·바람 (p16-24)

**파랑 입력 3형식** (p16 §4.1.1): ① 정적(`Hso`·`phiw0`·`tper`·`spread`, 매 스텝 섹터 내 균등분포 무작위 추출) ② 시계열 `.wvt`(`yyyymmddHHMM`, Hs, Tp, Dir) ③ 파랑 기후 `.wvc`(Hs, Tp, Dir, 확률). `randomseed` 로 재현 가능(기본 꺼짐).
> ⚠**"a wave climate should not be combined with a variable timestep"** — 가변증분이 저에너지 조건을 과대평가하므로 `tc=0`+`dt` 를 쓰라 (p16).

**공간변화 조건** (p17 §4.1.2): `WVCfile` 셀배열 / 참조파일 / **NetCDF**(`station_x`,`station_y`,`time`,`point_hm0`,`point_tp`,`point_wavdir`). 보간은 `interpolationmethod` = `alongshoremapping`(정확·느림) 또는 `weighteddistance`(부정확·빠름). 조건 선택은 전 지점 **동기화**되므로 파랑기후는 한 기준지점 분류에 근거해야 한다.

**2단 굴절** (p18 식 8-11, Figure 4-1): 심해(`o`, 수심 `ddeep`) → 폐쇄수심 근방(`tdp`, 수심 `dnearshore`)은 **전빈 방위 기준** Snell; `tdp` → 쇄파점(`br`)은 **해안선 법선 기준**. 심해→전빈 굴절은 등수심선 평행 가정. 2D 파랑모형 결과를 폐쇄수심에서 직접 넣으면 1단계를 건너뛴다.

**profile mode 파랑** (p19-20 §4.1.4, `trform=TIDEPROF`): 1D 파랑에너지 수지(식 12)를 Baldock et al.(1998) 소산(식 13-14)으로 풀되 **implicit 1차 스킴 + 예측자/수정자**(식 15-19). 파랑구동류는 Feddersen et al.(1998) 저면전단응력을 연안압력force 와 등치해 $v_w$ 에 대한 2차방정식으로 해석적으로 푼다(식 20-21).

**조석** (p20-22 §4.2): `tidefile` 에 M2·M4 성분을 수심 약 5 m 의 대표 연안지점들에서 준다 — 11열(`x_stat`,`y_stat`,`eta`×2,`detads`×2,`phi`×2,`k`×2,`surfslope`). 연안 운동량 수지를 선형화(식 22-23)하고 주기해(식 24-26)를 쓰며, 마찰 파라미터 λ 는 $\lambda=3/8\cdot\pi\cdot C_d\cdot\hat v$ 의 2차방정식으로 푼다(식 27). **"only depends on the water depth"** 인 해석해라 M4 등 고차성분은 선형 중첩으로 더한다. 횡단유속은 연속식에서 복원(식 28-29). 합성유속은 단순합 $v=v_{tide}+v_w$ (식 30).

**수위·바람·기후변화** (p23-24): `WATfile`(.WAT)/`WL0` — **사구 모듈에 필수**. `WNDfile`(.WND, 풍속·풍향)+`uz`·`phiwind0`·`z`·`Cd`. `ccSLR`(상수 또는 [Nx2] 표)·`tanbeta`(Bruun 후퇴)·`ccHS`(예 0.001=연 +0.1%)·`ccDIR`(예 0.05 °/yr).

## 5. 수송공식 (p25-28 §5.1)

매뉴얼이 문서화한 공식은 **7종**이다. 최대 수송은 어느 공식이든 해안법선 기준 **외해 입사각 40°~45°** 에서 발생하며, `qscal`(기본 1)로 전 공식을 일괄 보정한다 (p25).

| 키워드 | 파랑 위치 | 식 | 계수·근거 |
|---|---|---|---|
| `CERC1` | 외해 | (34) $Q_s=b\,q_{scal}H_{s,off}^{5/2}\sin2\phi_{off}$ | `b` **기본 1e6** — "this value has to be set by the user for every case". 원리 설명용 |
| `CERC2` | 외해(굴절·천수 내포) | (35) $K_1q_{scal}t_{sc}H^{2.4}T_p^{0.2}\cos^{1.2}\phi\sin\phi$ | **K0=0.39** m^0.5/s. Ashton & Murray(2006) CEM 과 직접 비교용 |
| `CERC3` | 쇄파점 | (36) $K_2q_{scal}t_{sc}H_{s,br}^{5/2}\sin2\phi_{br}$ | **K0=0.35**(SPM, USACE 1984). GENESIS 등에서 널리 쓰는 판 |
| `KAMP` | 쇄파점 | (37) $2.33q_{scal}t_{sc}K_3H^2T_p^{1.5}\tan^{0.75}\beta\,D_{50}^{-0.25}\sin^{0.6}2\phi_{br}$ | Kamphuis(1991) |
| `MILH` | 쇄파점 | (38) $0.15q_{scal}t_{sc}K_3H^{2.75}T_p^{0.89}\tan^{0.86}\beta\,D_{50}^{-0.69}\sin^{0.5}2\phi_{br}$ | Mil-Homens(2013) 재보정 |
| `VR14` | 쇄파점 | (39) $0.0006q_{scal}t_{sc}K_4K_{swell}\rho_s\tan^{0.4}\beta D_{50}^{-0.6}H^{2.6}v_{total}$ | Van Rijn(2015) = TRANSPOR2004 파라미터화. $K_{swell}=0.015P_{swell}(1-0.01P_{swell})$ |
| `TIDEPROF` | 단면 전체 | (40-47) Soulsby–van Rijn(1997) bed+suspended | `Acal` 기본 **0.2**, `Cf`·`hmin`·`hclosure`·`profile`·`dx` 필요 |

> ★**VR14 의 조석류는 미구현이다.** $v_{total}=v_{wave}+v_{curr}$ 로 적혀 있으나 매뉴얼이 명시한다 — "also the tide-driven flow velocity can be specified (vcurr), **which is a capability that will be added in the future**" (p27). 코드 실측(`transport.m:183` vtide=0 하드코딩)과 일치한다.

**회절 ON 시 추가항**: "an additional term for the gradient in wave energy is resolved in the 'transport computation' which resembles the effect of residual water-level setup driven circulation" (p25).

## 6. 경계조건·고각도·차폐 (p28-30)

**측방 경계** `boundaryconditionstart`/`end` (p28 §5.2) — 순환형은 모델이 자동 감지:
`closed`(또는 `{'closed',25000}` 로 25,000 m³/yr 강제) · `fixed`/`Neumann`(수송경사 0) · `angleconstant`(초기 방위 또는 `{'angleconstant',310}`) · `periodic`(양단 수송률 평균). 경계 격자는 **초기 방위의 법선으로만** 이동한다.

**고각도 불안정** (p29-30 §5.3, Ashton et al. 2001): ~40° 이상 사입사에서 교란이 성장한다 — "not just a numerical feature of models, but also a physical phenomenon". 임계각 초과 지점에서 **downdrift 수송을 최대수송으로 고정(국소 upwind)** 해 스핏 성장은 허용하되 안정성은 유지한다. CEM 의 거동을 대부분 물려받되 **격자 기반이 아닌 벡터 기반**이라 넓은 영역에서 효율적이다. `twopoints=1` 권장(둘째 downdrift 셀까지 분산), `maxangle` **기본 60°**, `plotUPW=1` 로 적용지점 가시화.

**차폐** (p30 §5.4): 해안 요소·섬·구조물이 만드는 그림자를 매 timestep 재평가하고, 해당 지점 수송을 0으로 둔다 — **단, 회절 영향을 받는 지점은 예외**.

## 7. 구조물·양빈 (p31-47)

**구조물 판정은 해안선 교차 횟수로 한다** (p31-33): 이안제 = 교차 없음(해안선에 대체로 등거리, 서로 그늘 금지) / 그로인·항만제 = **두 번 교차**(시계방향 정의, L·T형 가능). "If it crosses the coastline twice then the model will assume it is a groyne instead" (p31). 스위치 `struct`·`revet`·`sedlim`, 좌표 `xhard`/`yhard`·`LDBstructures`·`xrevet`/`yrevet`·`LDBrevetments`·`LDBsedlim`(x,y,임계폭). **구조물은 전 기간 상시 존재하며, 시간에 따른 건설·철거는 재시작(restart)으로만 구현한다** (p33 §6.1.1).

**회절 2종** (p33-36 §6.1.2, `diffraction=1`): $H_d=k_d H_i$, $\varphi_d=\varphi_i+\omega_r$ (식 48-49). `kdform`·`wdform` 로 각각 파고·파향 처리를 고른다.
- **Kamphuis(2000)/Dabees & Kamphuis(1998)** (식 50-51): $k_d$ 를 $\omega_r$ 구간별 3분할($0.69+0.008\omega_r$ / $0.71+0.37\sin\omega_r$ / $0.83+0.17\sin\omega_r$), $\omega_r=\omega$. 장파봉 실험 기반, **공간경사가 상대적으로 매끄럽다**.
- **Roelvink** (식 52-53): $k_d=1-\exp(-(0.5/\omega_*)^4)$, $\omega_*=(\omega_r+90)/180$; 회전은 임계각 초과분만 $\omega_{r,corr}=rotfac(\omega_r-\omega_t)$. **XBeach 비정수압 시뮬레이션 결과에 피팅**(Figure 6-8). `rotfac` 기본 **0.8**, $\omega_t$ 기본 **-20°**(방향분산 12° 이하 장파봉), 분산 32° 이상이면 자동으로 **-35°** 까지 확대. **국소 공간경사가 Kamphuis 보다 뚜렷하다**.

양측 회절 합성은 **에너지 벡터합**(식 54-55). 영향권 판정은 $\omega_{eps}$(기본 90°) 기준이며, 두 구조물 영향이 겹치면 각도는 같은 방식, 파고는 **두 kd 의 곱**. 겹치는 복잡 배치는 권장하지 않으며, 겹칠 때는 **회전이 가장 큰 구조물을 지배 구조물로** 삼는다 (p36).

**투과 3식** (p37-41 §6.1.3, `transmission`, **그로인은 불가**): `transmform='angr'` d'Angremond et al.(1996) **기본** (식 56) / `'gent'` Van Gent et al.(2023) (식 57, 투과계수 상한이 0.8 이 아니라 1까지, 계수 c1..c5 = 0.43·3.1·0.75·-0.25·0.5) / `'seabrhall'` Seabrook & Hall(1998) (식 58, D50 포함, 적용범위 식 59-60 밖에서는 발산). 구조물 제원 `transmbwdepth`·`transmcrestheight`(MSL 기준 양수 상방)·`transmslope`·`transmcrestwidth`·`transmd50`. `transmdir=1`(기본)이면 투과파 파향을 구조물 법선 쪽으로 **투과율에 선형 비례해** 돌린다. 투과가 커질수록 회절 성분은 비례해 줄어 100% 투과에서 0이 된다.
> ⚠매뉴얼 자체의 경고: Ranasinghe & Turner(2006)의 **잠제 주변 수평순환은 이 식들에 포함돼 있지 않다** — 짧은 잠제가 해안 가까이, 거의 직각 입사일 때 특히 문제 (p41).

**그로인 bypass** (p41-42 §6.1.4): $Q_{bypass}=(F_c-D_s/D_{LT})Q_{updrift}$ (식 61, $D_s\le D_{LT}$ 일 때만). 구조물 선단수심 $D_s=A_p y_{str}^{2/3}$(Dean 평형단면, $A_p=(1.04+0.086\log D_{50})^2$, 식 62), 활성 수송수심 $D_{LT}=(A_w/\gamma)(H_{1/3})_b$ (Hanson 1989, 식 63) — `Aw` 기본 **1.27**이나 **연평균 파랑조건으로 돌릴 때는 5 정도로 올리라**. `bypassfactor`(Fc) 전형 1~1.4, updrift 수송에만·downdrift 해안선이 더 육측일 때만 적용. 분배는 기본 균등, `bypassdistrpwr`>1 이면 구조물 가까이 집중(식 64).

**호안 bypass** (p42-43 §6.1.5): 시간적분 flux 를 updrift 공급량+국소 퇴적량으로 제한 — $Q_s\le Q_{s,updrift}+\Delta s\Delta n_{rev}D_c/(2\Delta t)$ (식 65). `iterrev` 회 sweep.

**양빈 2종** (p44-47 §6.2): 정선 양빈(`nourish`, `.nor` 7열: x1,y1,x2,y2,시작,종료,체적)은 총체적÷기간÷연장÷`Dc` 로 정선 전진율로 환산되며 **하천 공급·sink·bar-welding 표현에도 쓴다**. 전빈 양빈(`fnourish`, `.fnor`)은 확산계수 $K_{SFN}$ 로 서서히 공급 — Hallin et al.(2019) 지수감쇠(식 67-68), $\lambda_0=0.56\times10^{-6}$·$m_b=-0.5$. 미지정 시 $K_{SFN}=\max(-4.86\times10^{-5}V_0+0.035,\ 0.001)$ (식 66).
> ⚠**네덜란드 19개 전빈양빈 자료 회귀식이다** — "for cases outside the Netherlands it is advised to use a user-defined diffusion coefficient" (p46-47).

## 8. 횡단 상호작용·구간 상호작용·출력 (p48-57)

**월류** (p48 §7.1, Ashton & Murray 2006): `spitwidth` 기본 **50 m**. 매 스텝 **입사파 방향으로** 배리어 폭을 재고 임계폭 미만이면 육측점을 차이만큼 이동시키되 **스텝당 국소 격자간격의 일정 비율(예 10%)을 넘지 못하게** 해 이산화 인공물을 막는다. 사입사에서는 스핏을 가로지르는 거리가 길어 월류가 덜 일어난다. 해측/육측 활성고를 달리 둘 수 있어(`Bheight`+`Dsf`/`Dbb`) 해측 침식폭보다 육측 퇴적폭이 커질 수 있다. 속도는 `OWtimescale`(년)로 평형폭에 지수적으로 접근.

**사구** (p48-52 §7.2, `dune=1`, Larson et al. 2016): 풍성수송은 Lettau & Lettau(1978) 잠재수송률(식 70-71)에 fetch 지수포화 $q_{wind}=q_{WE}(1-\exp(-\delta_{wind}F_L))$ (식 72, $\delta_{wind}=0.1$). 침식은 **총수위(조석+폭풍해일+런업)가 사구 발끝에 닿을 때만** 발생하며 $q_{wave}=4C_s(R'+SWL-D_F)^2/T_H$ (식 76). 런업 `runupform` 3종 — `Stockdon`(기본, 식 73) / `Larson`(경사 무관, 급경사·협소 해빈용, 완경사에서 과대, 식 74) / `Ghonim`(2019, 경사 포함, Stockdon 과 유사, 식 75). 결합은 식 77-78. 입력은 `LDBdune` [Nx5] (x, y, berm 폭, 사구 발끝고, 사구 마루고). **경사가 1/15 보다 급하면 사구 발끝을 낮춰** 총수위 도달 빈도를 늘린다. 사구를 켜면 "in many cases the **'active height' of the coastline should be reduced**" (p50).

**점착성/till 사구** (p53 §7.3): `xtill`(전면 모래층 두께, **설정해야 활성화**)·`Cstill`(기본 5e-6, 일반 `Cs`=5e-4 보다 느림)·`perctill`(기본 80% 가 세립). 모래층을 먼저 `Cs` 로 깎고 그 다음 till 을 `Cstill` 로 깎으며, 침식물 중 모래분만 해안 성장에 기여한다. 풍성수송은 전면 모래층에 더해져 층이 다시 자랄 수 있다.

**합병·분리** (p54 §8.1): 스핏 해측이 월류 허용치보다 크게 침식되거나 월류가 꺼져 있을 때 분리가 일어나고, 스핏이 본토로 접근·연장되면 합병한다.

**수로 유지** (p55 §8.2): `LDBchannel`(또는 `xrmc`/`yrmc`)로 **석호/하천 내부 → 입구 바깥** 경로를 주면 임계폭 미만일 때 토사를 해측으로 밀어낸다. `channelwidth`, `channelfac` 기본 **0.08**.

**출력** (p56 §9.1): `output.mat`(`outputdir`, `storageinterval` 일 단위)에 **O 구조체**(원시, 격자 크기가 시간에 따라 변함, **순간값**)와 **P 구조체**(격자 재보간)를 함께 저장. O 구조체가 순간값이므로 **누적 수송은 출력 간격이 충분히 촘촘할 때만 계산 가능하다**.

## 9. 코드 실측과의 대조 — 확인 / 확장 / 불일치

기존 `source-analysis/` 5노트는 이 매뉴얼이 나오기 전(2026-07)에 코드를 직접 읽어 작성했다. 대조 결과를 셋으로 나눈다.

### 9.1 매뉴얼이 확인해 준 것

| 코드 실측(기존 노트) | 매뉴얼 근거 |
|---|---|
| `transport.m:183` VR14 **vtide=0 하드코딩** | p27 — vcurr 는 "will be added in the future" |
| `rotfac=0.8`, 주석 "0.8 according to comparison with wave-resolving XBeach" | p35 — Roelvink 파라미터화는 **XBeach 비정수압 결과 피팅**, 기본 0.8 |
| `omegat` −20°(장파봉)~−35°(단파봉) | p35 — 기본 −20°, 분산 32° 이상에서 −35° |
| 회절 Kd = Roelvink 지수형 / Kamphuis 구간식 | p34-35 식 50·52 |
| `maxangle` 60°, `twopoints` 권장 | p30 |
| CERC3 계수 **k=0.35** / CERC2 **0.39** | p26 — CERC3 = SPM 0.35, CERC2 = 0.39 |
| 고정증분에서 파랑조건 **에너지벡터 집약** | p15 §3.2.3 |
| 월류 = Ashton–Murray 벡터판 | p48 §7.1 |

### 9.2 매뉴얼이 새로 준 것

- 투과 3식(d'Angremond/van Gent 2023/Seabrook-Hall)과 `transmdir` 의 선형 스케일링 — 기존 노트에 없던 축.
- 전빈 양빈 $K_{SFN}$ 회귀식과 **네덜란드 19개 사례 한정**이라는 적용범위 경고.
- `Aw` 를 연평균 파랑 구동 시 1.27→5 로 올리라는 운용 지침(p41).
- `runupform='Ghonim'` 3번째 선택지.
- 구조물 판정이 **해안선 교차 횟수**라는 규칙과, 시간에 따른 구조물 변경은 **restart 로만** 가능하다는 제약.
- `interpolationmethod` 2종의 정확도/속도 트레이드오프.

### 9.3 불일치 — 코드로 판정한 3건

매뉴얼 본문과 Appendix B 기본값 표가 어긋나는 지점이 셋 있다. **전부 코드를 직접 읽어 판정했다.**

**① `rotfac` — 본문 0.8 vs 표 1.5. 판정: 본문이 맞고, ★표의 값은 애초에 쓰이지 않는다.**

`initialize_defaultvalues.m:158` 은 확실히 `S.rotfac=1.5` 로 두고 `prepare_structures.m:114` 가 이를 `STRUC.rotfac` 으로 넘긴다. 그런데 회절 루틴은 그 값을 **읽지 않는다** — `wave_diffraction.m:106-114` 가 지역변수로 다시 계산한다.

```matlab
alfa=min(max(WAVE.dirspr-12,0),32)/20;
rotfac_longcrested  = 0.8;   % at dirspr = 12 (default)
omegat_longcrested  = -20;
rotfac_shortcrested = 0.8;   % at dirspr = 32
omegat_shortcrested = -35;
rotfac = (1-alfa)*rotfac_longcrested + alfa*rotfac_shortcrested;
omegat = (1-alfa)*omegat_longcrested + alfa*omegat_shortcrested;
```

이후 `:373-374`·`:544-545` 가 쓰는 것은 이 지역 `rotfac` 이다. 따라서:

- **`rotfac` 입력 키워드는 Roelvink 회절 경로에서 효과가 없다.** 사용자가 값을 줘도 `:113` 이 덮어쓴다. Appendix B 의 1.5 는 **사문(死文) 기본값**이다.
- 두 앵커가 **둘 다 0.8** 이라 블렌딩은 rotfac 에 대해서는 항등이다 — 방향분산에 따라 실제로 변하는 것은 `omegat`(−20°→−35°)뿐이다. 매뉴얼 p35 의 "The degree of rotation also depends on a spreading factor of the waves (rotfac)" 는 이 점에서 부정확하다.
- `wdform` 이 dabees/hurst/kamphuis 계열이면 `:118` 이 `rotfac=1`·`omegat=0` 으로 고정한다 — 회전 보정은 **Roelvink 방향모드 전용**이다.

**② `trform='CERC'` vs 본문 `CERC1`. 판정: 모순이 아니라 별칭이다.**
`transport.m:140` 이 `strcmpi(...,'CERC') || strcmpi(...,'CERC1')` 로 **둘 다 받는다.** Appendix B 의 기본 `'CERC'` = 본문의 CERC1.

**③ `Kw` — 본문 식 설명 1.2 vs 파라미터 목록·표 4.2. 판정: 4.2 가 맞고 본문 식 설명이 틀렸다.**
`initialize_defaultvalues.m:193` 이 `S.kw=4.2` 이고 `prepare_dunes.m:96` 이 이를 받는다. p49 의 "Kw is an empirical coefficient of 1.2 [-] based on Sherman et al. 2013" 은 **stale 서술**이다 — 같은 문서의 p50 목록과 p63 표는 4.2 로 일치한다.

### 9.4 매뉴얼이 다루지 않은 코드 분기 — `RAY`

`transport.m:194` 에 `elseif ~isempty(findstr(lower(TRANSP.trform),'ray'))` 분기가 실재한다(s-φ 곡선 + 해석적 `dQS/dφ`, 외부 ray 계산 결과 이식용). 매뉴얼 §5.1 은 이를 **다루지 않는다.** 코드 주석(`transport.m:10`)의 문서화 목록도 `'CERC','KAMP','MILH','CERC3','VR14'` 5종뿐이라 RAY·TIDEPROF 가 빠져 있었는데, **매뉴얼 v1.0 이 TIDEPROF 를 문서화하면서 격차는 `RAY` 하나로 줄었다.**

## 10. 주요 입력 파라미터 기본값 (Appendix B, p61-63 발췌)

| 그룹 | 키워드 = 기본값 |
|---|---|
| 파랑 | `hso`=1 · `tper`=6 · `phiw0`=330 · `spread`=90 · `dirspr`=12 · `ddeep`=25 · `dnearshore`=8 · `randomseed`=-1 · `interpolationmethod`='weighted_distance' |
| 해안선 | `ds0`=100 · `griddingmethod`=2 · `d`=10 · `phif`=[] · `maxangle`=60 · `gisconvention`=0 · `preserveorientation`=0 |
| 수송 | `trform`='CERC' · `b`=1e6 · `qscal`=1 · `d50`=2e-4 · `d90`=3e-4 · `porosity`=0.4 · `tanbeta`=0.03 · `rhos`=2650 · `rhow`=1025 · `alpha`=1.8 · `gamma`=0.72 · `pswell`=20 · `ks`=0.05 · `hclosure`=8 |
| 회절 | `diffraction`=0 · `wdform`='Roelvink' · `kdform`='Kamphuis' · `rotfac`=1.5(⚠**무시됨 → 실효 0.8**, §9.3 ①) · `diffdist`=[] |
| 호안·투과 | `revet`=1 · `iterrev`=5 · `critwidth`=5 · `transmd50`=1 · `perm`=0 |
| 양빈 | `nourish`=0 · `growth`=1 · `nourrate`=100 · `fnourish`=0 · `mb`=-0.5 · `labda0`=5.6e-7 |
| 사구 | `dune`=0 · `kf`=0.02 · `cs`=5e-4 · `cstill`=5e-6 · `perctill`=80 · `d50r`=2.5e-4 · `rhoa`=1.225 · `duneaw`=0.1 · `kw`=4.2 · `k`=0.41 · `segmaw`=0.1 · `aoverwash`=3 · `wberm`=50 · `dfelev`=3 · `dcelev`=8 |
| 바람·수위 | `Cd`=0.002 · `z`=10 · `phiwnd0`=330 · `runupform`='Stockdon' · `runupfactor`=1 · `swl0`=0 |

> ⚠ 표의 `rotfac`=1.5 는 회절 루틴이 덮어쓰므로 **실효값이 아니다**(§9.3 ①). `kw` 는 4.2 가 맞다(§9.3 ③).
