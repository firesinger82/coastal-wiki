# Celeris 외부 원문 판정 (11-04)

이 문서는 `celeris-lynett2026-vs-code.md`의 X 2행(CP3-013, CP3-017)을 외부 문헌으로 판정한다.
두 원문(Kim 2009, Kennedy 2000)의 출판사 본문은 열지 못했다. 출판사 페이지(ScienceDirect, ResearchGate, ASCE)가 403·404를 돌려주었다.
그래서 각 행에서 원문을 인용한 2차 문헌을 쓰고, 어느 문장이 2차 문헌인지 표시한다.
2차 문헌 가운데 FUNWAVE-TVD 3.0 문서는 위키 안의 사본이고, Fotia 학위논문과 Kim·Lynett ICCE 초록은 웹에서 받아 `pdftotext`로 읽었다.

## CP3-013 완전비선형 세부식·평가높이

### 서지
- Lynett et al. 2026, p.3 “Kim et al. (2009) provided the detailed form of these equations”; “particular elevation, zα”.
- Kim, D.H., Lynett, P.J., Socolofsky, S.A. (2009), *Ocean Modelling* 27(3–4):198–214, DOI 10.1016/j.ocemod.2009.01.005.

### 찾은 원문
- Kim 2009 본문은 열지 못했다. 식 번호와 쪽은 확인하지 못했다.
- Kim·Lynett ICCE 초록(https://icce-ojs-tamu.tdl.org/icce/article/download/1290/pdf_343/8685)은 Kim 2009를 인용한다. 이 초록은 평균 속도를 “arbitrary water depth zα”에서 정의하고 zα의 숫자값은 적지 않는다.
- 위키의 FUNWAVE-TVD 3.0 문서 `models/FUNWAVE/raw/manuals/funwave_tvd_3.0.md:323`은 Nwogu(1993)의 zα 선택을 설명한다.
- Fotia 학위논문(https://udspace.udel.edu/bitstreams/41acc7ea-81ba-41da-a813-ca330ae8e78b/download, Delaware, 2차 문헌) 1208–1210행(pdftotext 줄)은 Wei 등의 식을 설명한다.
- 같은 학위논문 1345–1346행 식 (2.11)은 Kennedy 2001의 이동 기준면을 적는다.

### 원문 인용(2차 문헌)
- FUNWAVE-TVD 3.0 문서, `funwave_tvd_3.0.md:323`: “Following Nwogu (1993), zα is usually chosen in order to optimize the apparent dispersion relation of the linearized model relative to the full linear dispersion in some sense. In particular, the choice α = (zα/h)2/2 + zα/h = −2/5 recovers a Pad´e approximant form of the dispersion relation, while the choice α = −0.39, corresponding to the choice zα = −0.53h, minimizes the maximum error in wave phase speed occurring over the range 0 ≤ kh ≤ π.”
- Fotia 학위논문: “reference velocity uα = (uα , vα ) at a reference elevation zα = −0.531h … Nwogu (1993) found that the error is minimized for zα = −0.531h, when 0 < kh < π.”
- Fotia 학위논문 식 (2.11), Kennedy 2001: “zα = ζh + βη = −0.5528h + 0.4472η”.
- Kim·Lynett ICCE 초록: “U i is the horizontal velocity at an arbitrary water depth z α”.
- ERDC/CHL CHETN-I-106 (2025) Table 1 “Main Reference” 행: Coulwave의 주 문헌은 Kim et al. (2009)이다.

### 코드 인용
- `models/Celeris/raw/source_code/Celeris-WebGPU/js/constants_load_calc.js:38`: `Bous_alpha: -0.531,  // extended Boussinesq (Nwogu) parameter,`
- `shaders/Pass3A_COULWAVE.wgsl:44`: `let za_here = -d_here + ( 1.0 + globals.Bous_alpha ) * H_here;`
- 같은 파일 45행의 주석 처리된 대안: `//let za_here = d_here * globals.Bous_alpha;`
- `shaders/Pass3_COULWAVE.wgsl:344–345`: `temp7C= -vort_here * ( (za_here - 0.5 * (eta_here - d_here)) * dTdy` / `+ (0.5 * za_here * za_here - 1.0 / 6.0 * (eta_here * eta_here  - eta_here * d_here + d_here * d_here)) * dSdy );`

### 판정과 이유
판정은 H(원문 이론 정의)이고, 일부는 확인하지 못한 채 남는다.
- 확인한 것: −0.531은 Nwogu(1993)가 위상속도 오차를 최소화하는 zα=−0.531h의 계수이다. FUNWAVE 3.0 문서의 Beta_ref=−0.531도 같은 값이다(`funwave_tvd_3.0.md:1602`). 코드의 Bous_alpha는 이 계수이다.
- 확인한 것: H_here=η+d이므로 코드의 za = −d + (1+α)H = −0.531d + 0.469η이다(대입은 이 판정에서 직접 계산). 이 식은 고정 높이 zα=−0.531h가 아니고, 순간 수면과 함께 움직이는 기준면이다. Kennedy 2001 식 (2.11)과 같은 형태이고, 계수만 −0.5528·0.4472 대신 −0.531·0.469이다.
- 확인한 것: 코드의 vort 항 `za − 0.5(η−d)`와 `0.5 za² − (1/6)(η²−ηd+d²)`는 Fotia 학위논문 식 (2.13)–(2.14)의 V3와 같은 구조이다(`(zα − ½(η−h))`, `½zα² − (1/6)(η²−ηh+h²)`). 변수명이 달라 d는 정지 수심 h에 해당한다.
- 확인하지 못한 것: Kim 2009가 쓰는 zα의 숫자값. Kim 2009 식의 E/F/G 항별 동일성. 와도 제외 항의 범위.
- 이유: 이 세 가지는 Kim 2009 본문이 필요하다. 2차 문헌 가운데 Kim 2009의 zα 값을 적은 것을 찾지 못했다.

### 노트에 쓸 결론 문장
“Celeris COULWAVE 경로의 Bous_alpha=−0.531은 Nwogu(1993)의 기준높이 계수이고 FUNWAVE 3.0의 Beta_ref와 같은 값이다. 코드는 za=−d+(1+α)H로 기준면을 순간 수면에 연동한다. Lynett 2026 p.3은 이 값과 식을 인쇄하지 않는다. Kim 2009 식과의 항별 일치는 원문 본문을 열지 못해 확인하지 않았다.”

## CP3-017 Kennedy 매개변수 동일성

### 서지
- Lynett et al. 2026, p.3 “breaking parameters as given in Kennedy et al. (2000) are used here”.
- Kennedy, A.B., Chen, Q., Kirby, J.T., Dalrymple, R.A. (2000), *J. Waterway, Port, Coastal, Ocean Eng.* 126(1):39–47, DOI 10.1061/(ASCE)0733-950X(2000)126:1(39).

### 찾은 원문
- Kennedy 2000 본문은 열지 못했다. 식 번호와 쪽은 확인하지 못했다.
- 위키 안: `models/FUNWAVE/raw/manuals/funwave_tvd_3.0.md:1099–1111`(식 82·83).
- 위키 안: `models/FUNWAVE/raw/manuals/funwave_tvd_3.0.md:1628`(Cbrk1·Cbrk2는 “parameter C1 in Kennedy et al. (2000)”).
- 웹: Fotia 학위논문 식 (2.26)–(2.28)과 그 아래 문단(Kennedy 2000 모형을 서술, 학위논문 쪽 29–30, 2차 문헌).
- 웹: Kazolea·Ricchiuto 계열 arXiv 1912.01905(2차 문헌)는 T* = 5√(h/g)를 Kennedy 2000에 돌리고 δ를 [0.9, 1.5] 범위로 적는다.

### 원문 인용(2차 문헌)
- FUNWAVE-TVD 3.0 문서 `:1103`: “ν = Bδb2(h + η)ηt (82) where δb = 1.2.”
- 같은 문서 `:1111`: “The default values of ηt(I) and ηt(F) are 0.65 × 2√gh and 0.15√gh as in the previous FUNWAVE version (i.e., Cbrk1 = 0.65 and Cbrk2=0.15 …)”. 이 문장은 Kennedy 2000이 아니고 FUNWAVE 이전 판의 기본값을 말한다. 2배 표기는 기존 노트가 소스(1배)와 다름을 이미 기록했다(`concepts/waves/wave-breaking-cross-model.md:64`).
- Fotia 학위논문 식 (2.26): “ν = BK δb2 Hη,t … δb = 1.2.” 식 (2.27): BK = 1 (η,t ≥ 2η,t*), η,t/η,t* − 1 (η,t* < η,t ≤ 2η,t*), 0 (η,t ≤ η,t*).
- Fotia 학위논문 식 (2.28) 아래: “The default values of η,t(I) and η,t(F) are 0.65√gh and 0.15√gh, respectively. The default transition time used here is T* = 5√(h/g).”
- arXiv 1912.01905: “Kennedy et al. (2000) proposed using Ni = γi√gh, Nt = γt√gh and a transition time T* = 5√(h/g).”; “δ is typically chosen in the interval [0.9, 1.5]”.

### 코드 인용
- `js/constants_load_calc.js:57–60`: `delta_breaking: 2.0,  // eddy viscosity coefficient` / `T_star_coef: 5.0,  // defines length of time until breaking becomes fully developed` / `dzdt_I_coef: 0.50,  // start breaking parameter` / `dzdt_F_coef: 0.15,  // end breaking parameter`
- `shaders/Pass_Breaking.wgsl:93–94`: `let h_here = eta_here - B_here;` / `let c_here = sqrt(globals.g * h_here);`
- `shaders/Pass_Breaking.wgsl:100–102`: `let T_star=globals.T_star_coef*sqrt(h_here/globals.g);` / `let dzdt_I=globals.dzdt_I_coef*c_here;` / `let dzdt_F=globals.dzdt_F_coef*c_here;`
- `shaders/Pass_Breaking.wgsl:125`: `let nu_breaking = min(1.0 * globals.dx * globals.dy / globals.dt, B_Breaking * globals.delta_breaking * h_here * detadt);`

### 판정과 이유
판정은 B(논문은 Kennedy 값과 같다고 썼으나 코드의 두 값이 다름)이다. 근거는 2차 문헌이다.

| 매개변수 | Kennedy 2000(2차 문헌 인용) | 코드 | 비교 |
|---|---|---|---|
| T* | 5√(h/g) | `T_star_coef` 5.0 × √(h_here/g) | 같다 |
| η_t(F) | 0.15√(gh) | `dzdt_F_coef` 0.15 × c_here | 같다 |
| η_t(I) | 0.65√(gh) | `dzdt_I_coef` 0.50 × c_here | 다르다(0.50 대 0.65) |
| 점성 계수 | ν = Bδ_b²(h+η)η_t, δ_b = 1.2, δ_b² = 1.44 | ν = B·delta_breaking·h_here·detadt, delta_breaking = 2.0 | 다르다 |

- 점성 계수 비교: 코드는 delta_breaking을 δ_b²에 해당하는 곱셈 계수로 쓴다(h_here가 총수심 η+d이므로 (h+η)에 해당). 이 대응에서 코드값 2.0은 Kennedy의 δ_b²=1.44와 다르다. delta_breaking을 δ_b 자체로 읽어도 1.2와 다르다. 어느 읽기에서도 2.0은 1.2·1.44와 같지 않다.
- 임계값 비교: c_here는 순간 총수심 기준 √(g h_here)이다. Kennedy와 FUNWAVE의 √(gh)는 정지 수심 h 기준으로 쓰인다는 점이 다르다. 이 차이는 수심 대 총수심의 문제이고, 0.50 대 0.65의 차이와 별개이다. 후자는 계수 자체의 차이이다.
- 위키 내부 일관성: `concepts/waves/wave-breaking-cross-model.md:48`이 이미 dzdt_I 0.50·dzdt_F 0.15·T_star 5.0·δ_b 2.0을 적는다. 같은 문서 `:47`은 FUNWAVE의 Cbrk1을 0.65로 적는다. 두 모델의 η_t(I) 계수가 다름을 이 문서가 이미 보인다.
- 확인하지 않은 것: Kennedy 2000 본문에서 같은 값(0.65, 0.15, 1.2, 5)이 인쇄되었는지의 직접 대조. 2차 문헌 네 곳(FUNWAVE 3.0 문서, Fotia 학위논문, arXiv 1912.01905, 위키 `FUNWAVE` 노트)이 같은 값을 Kennedy 2000에 돌린다.
- 한계: Lynett 2026이 “as given in Kennedy”라고 쓴 문장은 모든 값이 같다는 주장이 아니고 모형 구조를 따른다는 뜻으로 읽을 수도 있다. 이 읽기에서도 코드의 두 값(0.50, 2.0)이 Kennedy 값과 다르다는 사실은 바뀌지 않는다.

### 노트에 쓸 결론 문장
“Celeris의 T_star_coef 5.0과 dzdt_F_coef 0.15는 Kennedy 2000의 T*=5√(h/g), η_t(F)=0.15√(gh)와 같다. dzdt_I_coef 0.50은 Kennedy의 η_t(I)=0.65√(gh)와 다르다. delta_breaking 2.0은 Kennedy의 δ_b=1.2(δ_b²=1.44)와 어느 읽기에서도 다르다. 따라서 Lynett 2026 p.3의 ‘Kennedy 매개변수와 같다’는 문장은 코드 기본값에 대해 두 값에서 성립하지 않는다. Kennedy 2000 본문은 열지 못했고, 위 값은 FUNWAVE 3.0 문서와 Fotia 학위논문이 Kennedy 2000에 돌린 값이다.”

## 최종

| 행 ID | 최종 결론 | 근거 |
|---|---|---|
| CP3-013 | H 및 부분 미확인. 코드의 −0.531은 Nwogu(1993)의 zα=−0.531h 계수이고 FUNWAVE 3.0의 Beta_ref와 같다. 코드는 za=−d+(1+α)H로 기준면을 순간 수면에 연동한다. Kim 2009 식의 zα 숫자값과 E/F/G 항별 일치는 원문 본문을 열지 못해 확인하지 않았다. | `funwave_tvd_3.0.md:323`, `:1602`; Fotia 학위논문 1208–1210행·식 (2.11), (2.13)–(2.14); `constants_load_calc.js:38`; `Pass3A_COULWAVE.wgsl:44`; `Pass3_COULWAVE.wgsl:344–345` |
| CP3-017 | B. T_star_coef 5.0과 dzdt_F_coef 0.15는 Kennedy 값과 같다. dzdt_I_coef 0.50은 0.65와 다르고, delta_breaking 2.0은 δ_b=1.2(δ_b²=1.44)와 다르다. 근거는 2차 문헌이고 Kennedy 2000 본문은 열지 못했다. | `funwave_tvd_3.0.md:1103,1111`; Fotia 학위논문 식 (2.26)–(2.28) 및 아래 문단; arXiv 1912.01905; `constants_load_calc.js:57–60`; `Pass_Breaking.wgsl:100–102,125` |
