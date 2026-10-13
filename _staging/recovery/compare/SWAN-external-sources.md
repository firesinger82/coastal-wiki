# SWAN 외부 원문 필요 3행 — 외부 원문 대조 결과

작성일 2026-10-13. 저장소 파일은 수정하지 않았다. 내려받은 원문 사본은 scratchpad/ext/ 아래에 있다.

## 1. TN-089 (swantech 각주: SWAN의 유효 γ는 WAM보다 2π 크다)

### 찾은 원문
- 확인한 사실: Hersbach and Janssen (1999) 본문은 읽지 못했다.
- 시도한 경로: AMS 논문 페이지(HTTP 403·CAPTCHA), data-ww3.ifremer.fr/BIB/Hersbach_Janssen_JTECH1999.pdf(HTTP 403), r.jina.ai 우회(403), web.archive.org(스냅샷 없음), scholar.archive.org(세션 검증 차단).
- 따라서 논문의 식 (7), (8), (11) 원문은 확보하지 못했다. 아래 식은 동등한 권위 출처에서 읽었다.
- 출처 A (WW3 코드 주석, https://raw.githubusercontent.com/NOAA-EMC/WW3/develop/model/src/w3srcemd.F90 줄 84–110): `dN(k)max = Xp alpha pi^-1 (2pi)**4 / g**2 * 1/(k**3 sigma) = FACP/(k**3 sigma)  (1)`; 같은 파일의 알고리즘은 `FACP = XP / PI * 0.62E-3 * TPI**4 / GRAV**2` (w3gridmd.F90 줄 3138), `XP = 0.15` (줄 2766). 주석은 alpha=0.62e-4라고 쓰고 코드는 0.62E-3을 쓴다. 이 둘이 서로 다르다.
- 출처 B (ECWAM 코드, https://raw.githubusercontent.com/ecmwf-ifs/ecwam/develop/src/ecwam/implsch.F90 줄 349–356, yowfred.F90 줄 56): `DELFL(M) = COFRM4(M)*DELT`, `USFM = UFRIC*MAX(FMEANWS,FMEAN)`, `COEF4 = 5.0E-07`, `COFRM4 = COEF4*G*FR(M)**(-4.)`. 주석: “INCREASE OF SPECTRUM IN A TIME STEP IS LIMITED TO A FINITE FRACTION OF A TYPICAL F**(-4) EQUILIBRIUM SPECTRUM.”
- 출처 C (ECMWF IFS Cy48r1 Part VII, https://www.ecmwf.int/sites/default/files/elibrary/2023/81373-ifs-documentation-cy48r1-part-vii-ecmwf-wave-model.pdf, 5.2절 식 5.17, 3.2.7절 식 3.37–3.38): `|ΔF|max = 5×10^-7 g u* f^-4 <f>windsea Δt` (Hersbach and Janssen (1999) 제한기의 변형이라고 밝힌다); `Fmax(f) = αmax g² (2π)^-4 f^-5` (1차원), `Fmax(f,θ) = (αmax/π) g² (2π)^-4 f^-5` (2차원).
- 출처 D (SWAN 코드 주석 swancom1.ftn 줄 8062): HJLIM이 쓰는 Hersbach–Janssen 식을 `|D E(f,t)| = 3.0 * 1.0E-7 * g * u* * f_c * dt/ (f^4)`로 적는다. 검색 결과 요약도 같은 3×10^-7 계수를 보고했다.

### 코드 대조
- 확인한 사실: swancom1.ftn:7978–7979는 `DAC2MX = |PNUMS(20)*0.0081 / (2 σ k³ cg)|`이다. 이는 swantech 식 (3.42) `ΔN = γ α_PM/(2σk³cg)`와 같다. γ = PNUMS(20), 기본값 0.1 (swanmain.ftn:1276).
- 확인한 사실: 같은 식을 주석 줄 7920–7941이 `|D E(s)| = factor α_PM g²/s^5` (Ris, 1997)에서 유도한다.
- 직접 계산한 사실: 심해에서 σ²=gk, cg=σ/(2k)를 쓰면 SWAN 제한 폭은 F(σ,θ)=σ·ΔN = γ α_PM g²/σ^5이다. 주파수 f 기준으로 바꾸면 ΔF(f,θ) = γ α_PM g² (2π)^-4 f^-5이다.
- 확인한 사실: 이 값은 한 방향 구간(rad당)에 무방향 1차원 Phillips 준위(출처 C 식 3.37의 형태)를 그대로 적용한 것이다. 출처 C 식 3.38의 2차원 준위에는 1/π이 붙어 있다.
- 확인한 사실: HJLIM(swancom1.ftn:8004–8143)은 `C_HJ = (2π)²·3.0e-7·DT·σ_c`, `DAC2MX = C_HJ·u*/(σ³k)` (줄 8115, 8120)이다. 직접 계산한 사실: 출처 D의 식을 σ 기준 작용밀도로 바꾸면 `3e-7 (2π)² σ_c Δt g u* σ^-5`가 되고, σ²=gk를 쓰면 `C_HJ u*/(σ³k)`와 일치한다. 따라서 HJLIM은 출처 D의 식과 일치한다.
- 확인하지 않은 것: Hersbach and Janssen (1999)의 식 (7), (8), (11)의 인쇄 형태. 이 논문의 기존 WAM 제한기 계수(식 (7))를 읽지 못했으므로 “2π”의 정확한 비율을 논문 식으로 계산하지 못했다.
- 해석: WW3 코드의 FACP에는 α/π 형태가 있다(출처 A). 같은 α와 같은 분율을 쓰면 SWAN 제한 폭과 WAM 제한 폭의 비는 방향 정규화 때문에 π 또는 2π 정도의 계수가 된다. 어느 쪽인지는 WAM의 방향 정규화 가정(반평면 π 또는 전방향 2π)에 달려 있다. 각주의 “2π”는 이 계수와 같은 차수이므로 모순되지 않는다. 그러나 이 해석은 식 (7)을 읽지 않은 추정이다.

### 최종 결론
- 분류: **H (코드 대조 대상 아님)**. SWAN 코드 줄 7978–7979는 문서 식 (3.42)와 일치한다. “2π” 주장은 WAM 쪽 정규화에 대한 설명이며 SWAN 코드 어느 줄에도 2π 계수가 없다. 코드 결함 후보 없음. 보조: 문서 쪽 각주 내용은 외부 논문 식 (7)을 읽지 못해 “미검증, 모순 증거 없음”으로 둔다.

### 노트에 쓸 결론 문장
- “swancom1.ftn:7978–7979의 제한 폭은 swantech 식 (3.42) `γ α_PM/(2σk³cg)`와 일치한다(γ = PNUMS(20), α_PM = 0.0081).”
- “이 식은 한 방향 구간에 무방향 Phillips 준위를 적용하므로, WAM의 2차원 준위(IFS 식 3.38의 α/π)와 방향 정규화가 다르다.”
- “각주의 2π 비율은 WAM 쪽 정규화에 관한 문서 설명이며 SWAN 코드 줄이 검증 대상이 아니다. Hersbach and Janssen (1999) 식 (7)의 인쇄 본문은 접근 불가(AMS·ifremer HTTP 403)로 읽지 못했다.”
- “HJLIM(swancom1.ftn:8115–8121)은 `3.0×10^-7 g u* f_c Δt f^-4` 형태의 Hersbach–Janssen 제한기를 σ 기준 작용밀도로 옮긴 식이며, 주석 식과 산술적으로 일치한다.”

## 2. QC-020 (swantech 각주 6: 작용 변수 ψ, Akrish et al. (2020) 식 (2.2))

### 찾은 원문
- 출처: TU Delft 기관 저장소의 CC BY 최종본, https://pure.tudelft.nl/ws/portalfiles/portal/71750151/modelling_statistical_wave_interferences_over_shear_currents.pdf (DOI 10.1017/jfm.2020.143), 쪽 A2-4–A2-6, 2.1–2.2절.
- 식 (2.1) 원문: `ω = U · k + σ.`
- 식 (2.2) 원문: `ψ = (1/√(2g)) [ g a^-1 η + i a φ ],` 여기서 `a(x, −i∇x)`는 기호 `a(x,k) = √σ(x,k)`에 대응하는 유사미분 연산자다(부록 A).
- 식 (2.3) 원문: `ρ⟨|ψ|²⟩ = m0/σ + O(ε)`. 식 (2.4): `ρ⟨|aψ|²⟩ = m0 + O(ε)`.
- 식 (2.7) 원문: `Γ(x, x', t) = ⟨ψ(x + x'/2, t) ψ*(x − x'/2, t)⟩`. 식 (2.9): `W(x, k, t) = ∫ Γ(x, x', t) exp(−ik·x') dx'`. 원문 문장: “the zero-order moment of W equals the variance of ψ, and therefore following (2.3) gives a leading-order evaluation of the mean action density.”
- 식 (2.10) 원문: `Hs = 4 √m00, m00 = m0/(ρg)`. 식 (2.11): `m0 = ρ ∫ σ(x,k) N(x,k,t) dk`. 원문 문장: 종래의 작용밀도 스펙트럼 N을 W가 일반화한다.

### 코드 대조
- 확인한 사실: SwanQCM.ftn90:1593 `W(iky,ikx,ic) = ctb * cg / k`. ctb는 (σ,θ) 격자의 AC2를 쌍선형 보간한 값이다(줄 1588). k는 파수 격자의 |k|, cg는 줄 1541–1543에서 구한 유한 수심 군속도다.
- 확인한 사실: SwanQCM.ftn90:2360 `memqcm(id,is,KCGRD(1)) = ctb * kwave(is,1) / cgo(is,1)`. 줄 2358 주석은 “multiply with the inverse of Jacobian”이다.
- 직접 계산한 사실: AC2(σ,θ) dσ dθ = W k dk dθ 이고 dσ = cg dk 이므로 W = AC2·cg/k 이다. 줄 1593과 줄 2360은 서로 역변환이다.
- 확인한 사실: 논문 식 (2.9)·(2.11)의 N(x,k)는 파수 공간 작용밀도이므로 위 야코비안이 논문의 N ↔ (σ,θ) 변환과 같은 종류이다.
- 직접 계산한 사실: 식 (2.3)과 (2.10)에서 ⟨|ψ|²⟩ = m0/(ρσ) = g·m00/σ 이다. SWAN의 AC2는 분산밀도/σ (m00/σ 꼴)이므로 논문의 ψ-분산은 코드의 W보다 상수 g배 크다. 코드에는 g 인자와 ρ가 없다.
- 확인하지 않은 것: SwanQCM.ftn90 안에서 W가 σ 가중과 함께 파고로 되돌아가는 모든 경로. 줄 1593·2360이 서로 역변환이므로 순환(왕복)에서는 상수 g가 소거된다. 그러나 W를 직접 파고에 쓰는 줄이 있다면 g 인자를 확인해야 한다. 이 파일에서 `hs`를 직접 계산하는 줄은 grep으로 찾지 못했다.
- 해석: 코드는 ψ 자체가 아니라 분산 정규화된 작용밀도(g, ρ 상수 제외)의 Wigner 분포를 파수 공간에서 쓴다. 이 정규화 선택은 상수 배율이므로 선형 연산과 왕복 변환의 결과를 바꾸지 않는다.

### 최종 결론
- 분류: **F (표기·정규화 차이)**. 야코비안 cg/k는 식 (2.3), (2.9), (2.11)과 일치한다. 상수 g와 ρ는 코드가 생략하며, 왕복에서 소거된다. 코드 결함 후보 아님.

### 노트에 쓸 결론 문장
- “SwanQCM.ftn90:1593은 AC2(σ,θ)를 파수 공간 밀도로 바꾸는 야코비안 W = AC2·cg/k이고, 줄 2360은 그 역(AC2 = W·k/cg)이다. 이는 Akrish 외 (2020) 식 (2.9)의 Wigner 분포 W와 식 (2.11)의 파수 공간 작용밀도 N의 관계와 같은 종류이다.”
- “Akrish 외 (2020) 식 (2.2)–(2.3)에서 ρ⟨|ψ|²⟩ = m0/σ, m0 = ρ g m00 이므로 ⟨|ψ|²⟩ = g m00/σ 이다. SWAN 코드는 분산 기준 작용밀도 m00/σ를 쓰며 상수 g를 두지 않는다. 이 차이는 표기 선택이며 왕복 변환에서 소거된다.”

## 3. SS-537 (Zieger 너울 소산, SdsBabanin.ftn90:2196–2200, B1Z = 0.00025)

### 찾은 원문
- 확인한 사실: Zieger 외 (2015) 본문(Elsevier)은 직접 읽지 못했다. ScienceDirect는 초록 페이지만 열린다. 아래 식은 이 논문의 구현을 그대로 옮긴 두 출처에서 읽었다.
- 출처 A (WAVEWATCH III 매뉴얼 v5.16, https://polar.ncep.noaa.gov/waves/wavewatch/manual.v5.16.pdf, 2.3.11절 “Sin + Sds : Zieger et al. 2015”, 쪽 54–55): 식 (2.143) 원문 `Sswl(k,θ) = −(2/3) b1 σ √Bn N(k,θ).` 식 (2.144) 원문 `b1 = B1 2 √E kp.` 문장: “B1 is a scaling coefficient, E is the total sea surface variance Eq. (2.23) and kp is the peak wavenumber. Eq. (2.144) can be flagged through the SWL6 namelist parameter CSTB1.” 표 2.8: `b1 is constant CSTB1 SWL6 n/a(v4.18) F(v5.16)`; `b1, B1 SWLB1 SWL6 0.25E-3(v4.18) 0.0032(v5.16)`.
- 출처 B (WW3 코드 w3swldmd.F90 W3SWL6, https://raw.githubusercontent.com/NOAA-EMC/WW3/develop/model/src/w3swldmd.F90): `ANAR = 1.0/(SUM(K,1)*DTH)`, `BN = ANAR*(ABAND*SIG*DTH)*WN**3`, `B1 = SWL6B1*(2.*SQRT(SUM(ABAND*DDEN/CG))*WN(IK))` (CSTB1가 거짓일 때만), `DDIS(IK) = -(2./3.)*B1*SIG(IK)*SQRT(BN(IK))`.
- 출처 C (Aijaz, Rogers, Babanin 2016, Ocean Modelling 103, 98–117, https://www7320.nrlssc.navy.mil/pubs/2016/rogers2-2016.pdf, 2.3절): 식 (10) 원문 `Snb(σ,θ) = −2/3 b1 σ √Bn · E(σ,θ)`; 식 (11) 원문 `b1 = B1 2ε kp` (ε²은 전체 해면 분산, kp는 피크 파수). 문장: Young 외 (2013)는 b1의 범위를 0.0002–0.0014로 추정했고, Zieger 외 (2015)는 b1을 파형경사로 스케일하면 고도계 대비 파고 정확도가 좋아졌다고 보고했다.
- 확인한 사실: 위 세 출처가 모두 같은 구조를 준다. 한 식(상수 b1)과 다른 식(b1 = B1·2√E·kp, 파형경사 의존)이 구분된다. Zieger 외 (2015)의 식 번호 (23)과 (28)은 SdsBabanin.ftn90 줄 2196–2198의 주석이 붙인 번호이며, 논문 본문에서 직접 확인하지 못했다. 상수형이 (23), 경사 의존형이 (28)이라는 대응은 출처 A·C의 구조와 모순되지 않는다.

### 코드 대조
- 확인한 사실: SdsBabanin.ftn90:2189–2191 `BN = ANAR(IS)*SIGDENS(IS)*(KWAVE(IS,1)**3)*CG(IS,1)`, `SQRTBN = SQRT(BN)`. 줄 2153 `SIGDENS = Σ SPCSIG·AC2·DDIR`은 방향 적분한 에너지밀도 E(σ)이다. 줄 2189 `ANAR = 1/AINV`, AINV = Σ KTHETA·DDIR (줄 2183).
- 직접 계산한 사실: W3SWL6의 `ABAND·SIG·DTH`는 방향 적분한 E(k) = E(σ)·cg 와 같다. 따라서 WW3의 BN = ANAR·E(σ)·cg·k³ 이고 SWAN의 BN과 같은 식이다. ANAR는 두 코드가 모두 1/(Σ K ΔΘ) (K는 최대값으로 정규화된 방향 분포)이다.
- 확인한 사실: 줄 2200 `SWDIS(IS) = 2.0*B1Z*SPCSIG(IS)*SQRTBN(IS)/3.0`은 `(2/3)·b1·σ·√Bn`이다. 이것은 식 (2.143)·W3SWL6의 DDIS = −(2/3)·B1·σ·√BN과 계수 2/3까지 같다. 부호는 줄 2210에서 IMATDA에 +SWDIS로 더해지는 암시항과 줄 2212 `PLSWEL = −SWDIS`에서 소산으로 처리된다.
- 확인한 사실: swanmain.ftn:1386 `B1Z = 0.00025`와 swanpre1.ftn:3128 `INREAL('B1', B1Z, 'STA', 0.00025)`가 기본값 0.00025를 준다. 이 값은 WW3 v4.18의 SWLB1 기본값 0.25E-3과 같다. WW3 v5.16의 기본값 0.0032는 steepness-scaled b1(CSTB1=F)용 B1 계수다.
- 확인한 사실: SWAN 코드에는 b1 = B1·2√E·kp 분기가 없다. 줄 2197–2198 주석이 “does *not* include the steepness-dependent B1”이라고 밝힌다. 따라서 SWAN의 B1Z는 논문 용어로는 상수형 b1이며, 이름만 B1이다. 줄 2200은 식 (23) 형태에만 해당한다.
- 해석: 변수 이름 B1Z와 사용자 명령 `B1`이 상수형 b1을 뜻하는데 논문에서 B1은 경사 의존형의 비례 계수다. 이름이 겹치지만 값(0.00025)은 WW3 v4 기본값과 같으므로 동작은 일치한다. 확인하지 않은 것: Young 외 (2013)의 0.0014 근거와 Zieger 외 (2015) 본문에서 0.25E-3이 식 (23)의 b1로 쓰였는지.

### 최종 결론
- 분류: **F (표기 차이)**. 계수 2/3, √Bn 정규화(ANAR·E(σ)·cg·k³), 기본값 0.00025는 WW3 식 (2.143)·코드와 일치한다. 이름 B1Z는 논문의 b1(상수형)에 해당하므로 표기가 다르다. 경사 의존 B1(식 (28))은 구현되지 않았음을 코드 주석이 밝힌다. 코드 결함 후보 아님.
- 보조: 원 노트의 “코드에만” 표시는 “일치(식 (23)형)”로 바꿀 수 있다. 식 번호 (23), (28)은 논문 본문 미확인이라고 병기한다.

### 노트에 쓸 결론 문장
- “SdsBabanin.ftn90:2200의 `2·B1Z·σ·√Bn/3`은 WAVEWATCH III 매뉴얼 v5.16 식 (2.143) `Sswl = −(2/3) b1 σ √Bn N`의 상수 b1형과 계수까지 같다.”
- “Bn은 SWAN(SdsBabanin.ftn90:2189–2191)과 WW3(w3swldmd.F90 W3SWL6)에서 모두 ANAR·E(σ)·cg·k³ 형태이다.”
- “B1Z = 0.00025(swanmain.ftn:1386)는 WW3 v4.18의 SWLB1 기본값 0.25E-3과 같다. 경사 의존형 b1 = B1·2√E·kp(WW3 식 (2.144), Aijaz 외 2016 식 (11))는 SWAN에 구현되어 있지 않다.”
- “Zieger 외 (2015) 본문의 식 (23)·(28) 번호는 코드 주석에서 가져왔으며 논문 본문은 직접 읽지 못했다.”
