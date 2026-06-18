---
title: "LISFLOOD-FP 하도·구조 — SGC sub-grid channel·1D channel·porosity·weir/bridge"
model: LISFLOOD-FP
component: channel-sgc-structures
canonical_source: self
citation_status: verified
verification_method: "sgc.cpp:1-1768 / ch_flow.cpp:1-1166 / por_flow.cpp:1-418 / weir_flow.cpp:1-339 직접 Read; enum·구조체는 lisflood.h:194-195,478 grep 확인"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "[[lisflood-fp-architecture-source-map]]"
---

# LISFLOOD-FP 하도·구조 처리

LISFLOOD-FP의 하도(channel) 표현은 두 계열이 공존한다.

| 계열 | 파일 | 차원 | 격자 결합 | 비고 |
|---|---|---|---|---|
| **SGC** (Sub-Grid Channel, Neal) | `sgc.cpp`, `weir_flow.cpp`(bridge) | 격자 내부 sub-grid 단면 | 같은 2D 셀에 하도+범람원 공존 | 현행 주력 |
| **1D classic channel** (Bates/Trigg) | `ch_flow.cpp` | 별도 1D 세그먼트 벡터 | `ChanMask`로 2D에서 격리 | kinematic / diffusive 두 solver |
| **porosity** | `por_flow.cpp` | 2D 셀 스케일링 | sub-grid 구조물·지형복잡도 | 별도 옵션 (SGC와 무관) |

핵심 차이: SGC는 셀 **하나** 안에 하도 단면이 함께 존재(같은 `H[p0]`, 같은 `SGCVol`)하며 셀보다 작은(sub-grid) 하도를 폭-깊이 함수로 표현 (`sgc.cpp:6-7` 헤더 주석). classic 1D는 별도 `ChannelSegment*` 벡터에 노드 단위로 저장된다.

---

## 1. SGC sub-grid channel (`sgc.cpp`)

### 1.1 채널 단면형(chantype)과 면적/체적/수리반경

`SGCchantype[gr]` 그룹별 단면형. 면적·수리반경·체적이 각각 별도 switch로 분기.

| ct | 단면형 | A (면적) `CalcSGC_A` | R (수리반경) `CalcSGC_R` | V (체적) `CalcSGC_UpV` |
|---|---|---|---|---|
| 1 | 직사각형(default) | `we*hflow` (`:134`) | `A/(w+2R)`, R=min(h,hbf) (`:240-241`) | `h*c` (`:200`) |
| 2 | 멱함수 $h=x^{sl}$ | within-bank `A=h·we·(1-1/(sl+1))` (`:142`) | β-다항 wetted-perimeter (`:244-262`) | `c·h^(1/sl+1)` (`:204`) |
| 3 | linear slope | `A=we·h·0.5` (`:151`) | `A/(h+√(h²+w²))` (`:265`) | `h*c` (`:208`) |
| 4 | 삼각형 | `A=we·h·0.5` (`:160`) | `A/(2√(h²+w²))`, w=w/2 (`:270-271`) | `h*c` (`:212`) |
| 5 | 포물선형 | `A=h·we·2/3` (`:169`) | 해석적 포물선 wetted perimeter (`:278-281`) | `c·h^(3/2)` (`:216`) |
| 6 | 직사각형(no banks) | `we*hflow` (`:175`) | `A/w` (둘레=폭만) (`:285`) | `h*c` (`:220`) |
| 7 | 사다리꼴 | `(we+sl·h)·h` (`:180`) | `A/(w+2h√(1+sl²))` (`:290`) | (case 7 미구현 — 주석만 `:302-307`) |

out-of-bank(h≥bf) 시 면적은 bankfull 면적 + 직사각형 추가항(`(*we)*(hflow-bf)`)으로 더한다 (예: `:144`). out-of-bank 수리반경은 wetted perimeter가 bankfull에 고정된다 ("wetted perimeter is actually constant" `:266,272,291`).

### 1.2 멱함수 채널(ct=2)의 β wetted-perimeter 근사

ct=2의 수리반경은 둘레를 직접 적분하지 않고 폐형(β) 다항식으로 근사한다. `SGC_wp_prams` (`:18-121`)가 32개 γ 상수(`SGCgamma[0..31]`, `:32-92`)로부터 그룹별 β1~β4를 만든다. 형태 (s = `SGCs[gr]`):

$$\beta_k = \gamma_{k,0} + \gamma_{k,1}\tfrac1s + \gamma_{k,2}\tfrac1{s^2} + \gamma_{k,3}\tfrac1{s^3} + \gamma_{k,4}s + \gamma_{k,5}s^2 + \gamma_{k,6}s^3 + \gamma_{k,7}\sqrt{s}$$

(`sgc.cpp:114-117`). 무차원 깊이 `hp = 2h/wbf` (반폭 기준, `:246`)에 대해 임계 `SGCbetahmin`(=0.05, lisflood.h:478) 아래는 β1·β2, 위는 β3·β4를 쓰고 `SGCbeta5`(임계점 wetted-perimeter 분율 `:119`)로 이어붙인다 (`:248-260`).

### 1.3 채널 bed/체적 전처리 — `CalcSGCz` (`:312-559`)

도메인 전 셀 루프. 셀에 SGC가 있으려면 `SGCwidth>0` 이고 `DEM!=DEM_NO_DATA` (`:424`).

- **하도 길이** `SGCc[p0]`: 4-이웃에 trib(=폭>0)이 있거나 도메인 가장자리이면 반-셀폭씩 누적 → 최소 min(dx,dy) 보장 후 meander 계수 m 적용 (`:430-435`). `w0·SGCc > dA` 면 셀 체적 초과 방지로 `SGCc = dA/w0` (`:439-440`).
- **bed 고도** `SGCz`: 우선순위 (`:442-446`)
  1. bedfile 지정 시 그 값 (단 DEM-0.01 상한)
  2. `SGCbfh_mode` ON → `z0 - p` (p를 깊이로 해석)
  3. `SGCA_mode` ON → `z0 - p/w0` (p를 면적으로 해석)
  4. 집수면적 a>0 → `z0 - r·a^p` (수리지형식)
  5. else → `z0 - r·w0^p` (폭 기반 수리지형식)
- **bankfull 깊이/체적**: `SGCbfH = DEM - SGCz` (`:449`), 레벼 있으면 가산 (`:450`). `SGCbfV`는 단면형별 (예: ct1 `SGCc·SGCbfH` `:457`, ct2 `:462-463`).
- meander 계수 m은 시간스텝 영향 때문에 1로 상한 (`:390`), 그룹 최소값을 `Parptr->SGC_m`에 추적 (`:409`).
- 망닝 n은 전처리에서 `n²`으로 미리 제곱 저장 (`:388`) — 이후 flow 식에서 그대로 사용.
- `ChanMask`(supergrid) 읽힌 경우 마스크 셀의 DEM을 NoData로 만들어 2D 계산 제외, 단 SGC가 있으면 채널 유지 (`:529-557`).

### 1.4 SGC 흐름 — 하도·범람원 결합 (`CalcFPQxSGC` `:798-911`, y `:914-1027`)

한 셀 인터페이스에서 **하도 흐름 Qc**와 **범람원 흐름 Q**를 따로 계산해 합산한다 (`Q = Qc + Q` `:896,1012`). RESULT_CHECK 블록 내(`#ifdef RESULT_CHECK :726`, 닫힘 `:1768`) — CPU 검증용 경로.

**하도 흐름 (양 셀 모두 w>0일 때만, `:820`):**
관성파(inertial/local-inertial) 식. hflow는 두 셀 수면의 max에서 bed의 max를 뺀 값 (`:823`). 마찰경사 `Sf = -dh/(dx·m)` (meander 보정, `:834`). 양 셀 면적을 구해 **작은 면적**의 단면(보수적)을 선택 (`:839-854`):

$$Q^{n+1}_c = \frac{q_c - g\,A\,\Delta t\,S_f}{1 + \Delta t\,g\,c_n\,|q_c|/(R^{4/3}A)}$$

(`sgc.cpp:844`). 여기서 `cn`은 SGC 망닝 n² (분포형 `SGCManningsn` 있으면 셀평균 제곱, 아니면 그룹 `SGCn[gr0]` — 이미 제곱됨 `:829-830`). **Qc는 m³/s 단위** (FP의 m²/s와 다름, `:843` 주석).

**범람원 흐름 (effective width we < 셀폭일 때만, `:862`):**
하도 폭 we가 셀폭 이상이면 FP 흐름 생략. h를 bankfull만큼 차감(`h0 = max(h0-bf0,0)` `:865`)해 over-bank 깊이만 사용. 표준 FP 관성식:

$$Q^{n+1}_{fp} = \frac{q_0 - g\,\Delta t\,h_{flow}\,S_f}{1 + g\,\Delta t\,f_n^2|q_0|/h_{flow}^{7/3}}$$

(`sgc.cpp:880`), 이후 `(dx - we)`를 곱해 m³/s로 환산 (`:882`). routing scheme ON이면 가파른 수면경사(`|Sf|≥RouteSfThresh`)에서 FP flux 0 (`:878,884-885`).

### 1.5 SGC 셀 깊이 갱신 — `SGC_UpdateH` (`:1031-1206`)

체적 기반 갱신. 셀 dV = Tstep·(들어온 Qx,Qy 차) + `SGCdVol`(점원/강우/증발/routing 누적) (`:1092-1093`). `SGCVol += dV` 후 음수면 0 (mass balance error 유발, `:1098`). H 환원 분기 (`:1107-1112`):

| 조건 | H 계산 |
|---|---|
| SGCwidth=0 (하도 없음) | `H = SGCVol/dA` (표준) |
| SGCVol≥SGCbfV 이고 폭<평균셀폭 (over-bank) | `H = SGCbfH + (SGCVol-SGCbfV)/dA` |
| else (within-bank) | `H = CalcSGC_UpH(...)` 단면형 역산 (`:1659-1695`) |

`CalcSGC_UpH`: ct1 `V/c`, ct2 `(V/c)^(sl/(sl+1))`, ct5 `(V/c)^(2/3)` 등 V→h 역함수 (`:1666-1693`). 점원(point source) QFIX/QVAR/FREE는 update 전(`:1044-1079`), HFIX/HVAR는 update 후(`:1129-1178`)에 처리 — 수면고도 오류 방지 위해 분리 (`:1042-1043` 주석).

### 1.6 SGC 경계조건·점원 자유유출 — `SGC_BCs` (`:1211-1431`), `CalcSGC_pointFREE` (`:1740-1766`)

`SGC_BCs`는 N/E/S/W 4변을 인덱싱(`:1231-1286`)해 FREE/HFIX/HVAR/QFIX/QVAR 처리. FREE·HFIX·HVAR 모두 하도가 있으면 §1.4와 같은 관성식으로 `qSGold` 갱신 후 over-bank 분만 FP로 (`:1364-1406`). lat-long 그리드에서 Q 단위 보정: 정규격자면 `Q_multiplier=dx`, lat-long이면 1 (`:1220`). `CalcSGC_pointFREE`(`:1740`)는 자유유출 식 `qSG = sign·(|qSG|+|g·dt·A·Sf|)/(1+...)` (`:1750`) — fabs+sign으로 유출방향만 허용.

### 1.7 SGC hotstart·증발·강우·routing

- **hotstart** `SGC_hotstart` (`:563-724`): 수면으로부터 초기 Q를 정상류 망닝식 `q = h^(5/3)·Sf/fn·min(w0,w1)` 로 추정 (SGC `:601`, FP `:629`). Sf는 `√(dh/dx)` (kinematic 형태).
- **증발** `SGC_Evaporation` (`:1436-1521`): 하도 within-bank·bank-transition·표준 3경우로 체적손실 분리. within-bank는 `CalcSGC_UpV` 차분으로 손실체적 계산 (`:1485-1488`), bank transition은 FP+하도 혼합 (`:1492-1505`).
- **강우** `SGC_Rainfall` (`:1525-1552`): routing OFF일 때만 사용 — `SGCdVol += rain·dt·dA` (`:1544`).
- **routing scheme** `SGC_Routing` (`:1556-1654`): 가파른 도메인 안정화용. 비-하도 셀에서 `Sf≥RouteSfThresh`면 최저 이웃(`FlowDir`)으로 `Tstep/RouteInt` 분율만큼 체적을 강제 routing (`:1620-1647`). routing ON이면 강우도 여기서 추가.

---

## 2. Classic 1D channel (`ch_flow.cpp`)

별도 `ChannelSegmentType` 벡터. 다중 하천(`RiversIndexVec`) 루프로 OpenMP 병렬화(`ch_flow.cpp:343,594`). 헤더(`:6`): "1D kinematic wave approximation, Newton-Raphson".

### 2.1 kinematic solver `ChannelQ` (`:321-485`)

명시적(explicit) 비선형. 망닝식 상수부 `alpha = S^(1/2)/(n·w^(2/3))` (`:379,406`). 각 노드에서:

$$C = \alpha_0 A_i^{5/3} + \phi\,\tfrac{dx}{dt}A_{i+1} - \text{BankQ} + \text{inflows}$$

(`:412,422,426-428`), `Newton_Raphson`(`:488-501`)로 `NewA[i+1]` 해를 구함. φ는 over-bank 시 셀폭/하도폭 비 `dx/w` 보정 (`:392-399`). bank flow `BankQ`(`:505-525`)는 4-이웃 Qx,Qy 합으로 범람원 교환을 잡는다. 흐름·면적 변환은 `CalcQ`(`:529-534`) `Q=|s|·(wh)^(5/3)/(n·w^(2/3))`, `CalcA`(`:537-544`) 역산.

### 2.2 diffusive solver `ChannelQ_Diff` (`:566-776`)

암시적(implicit). 노드당 (A,Q) 2변수 → `2·nodes` 연립. de St. Venant diffusive 형태를 Newton-Raphson으로 풀되 banded Jacobian을 LU(Crout)로 — `bandec`/`banbks`는 Numerical Recipes C §2.4 이식(`:1014-1018,1022-1082,1095-1126`). 함수벡터 `calcF`(`:780-919`): 연속식(홀수행 `:807-809`)·운동량식(짝수행 `:836-847`), 시간가중 `th=1`(완전 암시적, `:787`). Jacobian `calcJ`(`:921-1004`)는 5-대각 compact 저장. 최대 200 반복(`:586,725-726`). 종료기준 `exitcrit` 4종(norm/max × solution/residual, `:707-723`). FREE BC는 마지막 단면에 망닝식을 대입해 재계산 (`:855-896` calcF, `:962-998` calcJ).

### 2.3 하도 BC 식별자

`Q_Ident`: FREE1·HFIX2·HVAR3·QFIX4·QVAR5·TRIB7·RATE8 (예: `:179-200` start-from-Q 분기). 지류(trib)는 dummy junction node로 main 채널에 `Next_Segment`/`Next_Segment_Loc`로 연결 (`:126,460,743`). `ChannelVol`(`:548-562`)은 `ChanMask!=-1` 셀의 `H·dA` 합.

---

## 3. Porosity (`por_flow.cpp`)

SGC와 독립된 옵션. 헤더(`:5-9`): "floodplain structures and topographic complexity" 스케일링. `CalcFPQxPor`/`CalcFPQyPor`(`:21,201`)는 표준 storage-cell(비관성, 적응 timestep) FP 흐름에 porosity 계수를 곱한다:

$$Q = \frac{h_{flow}^{5/3}\,S_f\,dy}{f_n}\cdot por$$

(`por_flow.cpp:65`). `Por_Ident` 4종 (`:60-95`):

| Por_Ident | 의미 | 배열 |
|---|---|---|
| 1 | 셀별 aerial(면적) porosity | `paerial[p0]` (`:62-64`) |
| 2 | 깊이층(zlev)별 aerial | `paerial[...+pH*xsz*ysz]` (`:69-74`) |
| 3 | 방향별 boundary(둘레) porosity | `pbound[...]` 방향 인덱스 (`:80-81`) |
| 4 | 깊이층별 boundary | `pbound[...+pH...]` (`:91-92`) |

두 이웃 중 작은 porosity 채택 `por=min(por0,por1)` (`:64`). `MaskTest`로 채널셀 제외(`:52`). 적응 timestep `0.25·dy²/alpha` (`:99`), 비적응 시 flow limiter `dA·|dh|/(8·dt)` (`:106-113`). `PorArea`(`:384-417`)는 저장면적 자체를 `dA·por`로 축소 (Por_Ident 1·3 셀별, 2·4 깊이층별 `:401-413`).

---

## 4. Weir / Bridge (`weir_flow.cpp`)

헤더(`:5-9`): weir(Dawson), 단방향 culvert(Wilson), SGC flow(Neal), bridge orifice(Neal/Trigg). `CalcWeirQx`(`:21`)/`CalcWeirQy`(`:181`). `Weir_Typ`: `EWeir_Weir=0` / `EWeir_Bridge=1` (lisflood.h:194-195). SGC ON이면 DEM 대신 하도 bed `SGCz`로 z 재설정 (`:63-67,222-226`).

### 4.1 Weir 식 (`:75-108`)

자유류/잠수류 전이. 상류수두 `hu = h+z - Weir_hc` (`:83`):

- 자유류 (`hd/hu < Weir_m`): $Q = C_d\,w\,h_u^{1.5}$ (`:86`)
- 잠수류: $Q = C_d\,w\,h_u\sqrt{h_u-h_d}/\sqrt{Weir\_m}$ (`:88`)

`Weir_Fixdir`로 단방향(culvert) 제어 (방향코드 0=양방향, x: 2/4, y: 1/3 `:81,97,237,253`).

### 4.2 Bridge orifice 식 (`:109-172`)

SGC 전용. 3-체제 (`:153-170`):

1. **수면이 soffit 아래** (`hu,hd<Soffit`): SGC open-channel flow `Qoc` (관성식, `:136`).
2. **압력류** (`Zratio>Tz`): orifice `Qp = Cd·Area·√(2g(hu-hd+heg))` (`:143`), `heg`는 상류 속도수두 `usVel²/2g` (`:141-142`).
3. **전이** (`1≤Zratio≤Tz`): Qoc·Qp 선형보간 (`:160`).

`Z = min(Soffit-z0,Soffit-z1)`(최소 개구 `:121`), `Area=Width·Z`, `Tz`=전이대(`Weir_m` 재활용 `:115`), `Soffit`=`Weir_hc`. `Zratio`=깊이/개구 (`:140,146`). y방향 bridge는 SGC ON일 때만 동작 (`:267`). Toby Dunne가 y에서 `QxSGold` 오리셋 버그 수정한 주석 (`:334`).

---

## 5. 자료구조 요약 (verified)

| 배열/필드 | 의미 | 출처 |
|---|---|---|
| `SGCwidth[p0]` | 셀 하도 폭 (0=하도없음) | `:395,424` |
| `SGCz[p0]` | 하도 bed 고도 | `:446,515` |
| `SGCbfH[p0]` | bankfull 깊이 = DEM-SGCz | `:449` |
| `SGCbfV[p0]` | bankfull 체적 | `:457` |
| `SGCc[p0]` | 단면형 상수(하도길이·폭 결합) | `:435,456` |
| `SGCVol[p0]` | 셀 총 체적 | `:1097` |
| `SGCdVol[p0]` | 누적 체적변화(점원·강우·증발·routing) | `:1072,1093` |
| `QxSGold/QySGold` | SGC 하도 flux(m³/s) | `:844,961` |
| `SGCgroup[p0]` | 셀 채널 그룹번호 | `:402,827` |
| `SGCchantype[gr]` | 그룹 단면형 1~7 | `:131,329` |
| `SGCn[gr]` | 그룹 망닝 n² (전처리 제곱) | `:388,830` |
| `SGCm[gr]` | meander 계수 | `:409,828` |
| `SGCbeta1..5` | ct2 wetted-perimeter β | `:104-119` |
| `ChannelSegmentType` (classic) | 1D 노드 벡터 | `ch_flow.cpp:45` |

> classic 1D vs SGC, 전역 솔버 호출 순서, time-step 제어 등 모델 전체 골격은 [[lisflood-fp-architecture-source-map]] 참조.
