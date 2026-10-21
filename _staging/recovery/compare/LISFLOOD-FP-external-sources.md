# LISFLOOD-FP 외부 원문 대조: LI2-203 (홍수 위험도 등급), LB1-235 (시간간격 조건)

작성일은 2026-10-21이다.
이 문서는 비교표 두 행에 대한 외부 1차 자료 조사 결과이다.
이 조사에서 모델을 실행하지 않았다.
원문 PDF는 작업 임시 폴더에 내려받아 `pdftotext -layout`으로 글자를 뽑아 확인했다.
쪽 번호는 "인쇄 쪽"(쪽 아래의 번호)과 "PDF 쪽"(파일 안 순서)을 구분해 적었다.

---

## 1. LI2-203: 홍수 위험도 등급 `Haz = H * (Vc + C(1.5))`

### 1.1 확인한 코드·매뉴얼 값 (질문에서 받은 값, 이 조사에서 다시 열지 않았다)

- 코드 `util.cpp:218`은 `Haz = Arrptr->H[p0] * (Vc + C(1.5)); // Changed to equation from DEFRA 2006 (ALD)`이다.
- 2013 사용자 매뉴얼 PDF p.38은 위험도가 `based on DEFRA 2003`이라고 쓰고, p.43이 `DEFRA. 2003. Flood Risks to People Phase 1, R&D Technical Report FD2317`을 인용한다.
- 코드 줄에는 잔해 계수(DF) 항이 없다.

### 1.2 출처 (모두 직접 열어 확인함)

| 약칭 | 서지 | URL |
|---|---|---|
| FD2317 | Ramsbottom, D., Floyd, P., Penning-Rowsell, E. (2003, July). *Flood Risks to People, Phase 1, R&D Technical Report FD2317*. Defra / Environment Agency Flood and Coastal Defence R&D Programme. ISBN 1844321355. | https://assets.publishing.service.gov.uk/media/602a8e2ae90e07055b9d3240/Flood_Risks_to_People_Phase_1_technical_report.pdf |
| FD2321/TR1 | HR Wallingford, Flood Hazard Research Centre (Middlesex Univ.), Risk & Policy Analysts (2006, March). *Flood Risks to People, Phase 2, FD2321/TR1, The Flood Risks to People Methodology*. | https://assets.publishing.service.gov.uk/media/602bbc768fa8f50383c41f80/Flood_risks_to_people_-_Phase_2_The_flood_risks_to_people_methodology_technical_report.pdf |
| FD2321/TR2 | 같은 저자 (2006, March). *Flood Risks to People, Phase 2, FD2321/TR2, Guidance Document*. | https://assets.publishing.service.gov.uk/media/602bbc3de90e07055f646148/Flood_risks_to_people_-_Phase_2_Guidance_Document_Technical_report.pdf |
| FD2321/PR | 같은 저자 (2006, March). *Flood Risks to People, Phase 2, Project Record, FD2321/PR*. | https://assets.publishing.service.gov.uk/media/602bbb768fa8f50386a7f8aa/Flood_risks_to_people_-_Phase_2_Project_Record.pdf |
| 보충 노트 | Surendran, S., Gibbs, G. (Environment Agency), Wade, S., Udale-Clarke, H. (HR Wallingford) (2008, May). *Supplementary note on flood hazard ratings and thresholds for development planning and control purpose*. | https://assets.publishing.service.gov.uk/media/602d04a98fa8f5037d371a08/FLOOD_HAZARD_RATINGS_AND_THRESHOLDS_explanatory_note.pdf |

### 1.3 원문 인용

**FD2317 (2003, Phase 1).** 식은 5.5.2절(인쇄 p.31, PDF p.39)에 있다. 식 번호는 없다. 표 5.2에 같은 식이 쓰인다.

> Based on the work considered in Section 4, it is clear that the degree of hazard is a function of both velocity (v) and depth (d). However, it should be noted that whilst a flood with depth but no velocity is hazardous, a flood with (virtually) no depth is not. For the purposes of this analysis, the degree of hazard will be associated with the function (v + 1.5) x d. A further factor for debris is added to reflect the degree of increased hazard. This expression is based on experience of flood hazard estimation. It is recognised that the expression appears rather arbitrary and refinement of this relationship is proposed in Phase 2, based on a more detailed assessment of previous work together with possible new research.

- 표 5.2(인쇄 p.31)의 열 머리는 `Hazard rating = d(v+1.5) + DF`이다. DF 열의 값은 `2 - likely`, `1 - possible`, `0 - unlikely`이다.
- 사례 계산(인쇄 p.35, PDF p.43, Gowdall 마을)은 `{1 x (0.5 + 1.5)} + 0 = 2`이다.

LaTeX로 옮기면 다음과 같다.

$$HR = d \,(v + 1.5) + DF,\qquad DF \in \{0,1,2\}$$

**FD2321/PR (2006, 프로젝트 기록).** PDF p.49에 Phase 1의 식을 다시 설명하는 글이 있다.

> In Phase 1 the following formula was used to combine velocity and depth: (v + 1.5) x d. There is a risk when the velocity is zero and the depth is large, hence the addition of 1.5 to the velocity term.

- 같은 보고서 5.2절(PDF p.32)은 `Hazard rating = d(v+1.5)+DF`와 `DF 0-2 score described the likelihood of debris`를 적는다.

**FD2321/TR1 (2006, Phase 2).**

- 3.2절 "The Phase 1 flood hazard formula"(인쇄 p.6, PDF p.16)는 Phase 1 식을 다음처럼 되풀이한다.

> HR = d x (v + 1.5) + DF ... DF = debris factor (= 0, 1, 2 depending on probability that debris will lead to a significantly greater hazard)

- 3.4절(인쇄 p.10, PDF p.20)은 DF를 바꾼 이유를 적는다.

> In the original Phase 1 methodology, a debris factor (DF) was added to the depth/velocity function. The value of DF was taken to be 0, 1, 2 depending on the probability that debris would lead to a significantly greater hazard. ... the values will need to be reduced (and values of 0, 0.5, 1 are suggested) to reflect the change in the depth/velocity function.

- 표 3.1(인쇄 p.10)은 DF 값을 깊이·토지이용별로 준다. 0~0.25 m는 모두 0이다. 0.25~0.75 m는 목초·경작지 0, 삼림 0.5, 도시 1이다. d>0.75 m 또는 v>2는 목초·경작지 0.5, 삼림 1, 도시 1이다.
- 3.5절 "Final flood risks to people method: Hazard rating formula"(인쇄 p.10, PDF p.20)가 최종식이다. 식 번호는 없다.

> The revised 'hazard rating' expression ... is: HR = d x (v + 0.5) + DF ... DF = debris factor (= 0, 0.5, 1 depending on probability that debris will lead to a significantly greater hazard)

$$HR = d \,(v + 0.5) + DF,\qquad DF \in \{0,\,0.5,\,1\}$$

- 부록 1의 표 3.1 "Equivalent Hazard Depths (m) for Different Hazard Rating Equations"(인쇄 p.60, PDF p.70)는 `HR = d(v+0.5)`와 `HR = d(v+1.5)`를 나란히 비교한다. 보고서는 이 두 식을 "the following statements ..."로 견주고 0.5 쪽을 최종식으로 채택한다.
- 표 3.2(인쇄 p.7~8, PDF p.18)의 등급 문턱은 `<0.75` Low, `0.75-1.25` Moderate, `1.25-2.5` Significant, `>2.5` Extreme이다.

**FD2321/TR2 (2006, 안내서).** "Flood Hazard" 항(인쇄 p.24, PDF p.32)이 같은 최종식을 쓴다.

> HR = d x (v + 0.5) + DF ... DF = debris factor calculated using Table 3.1

- 이 표 3.1은 TR1 표 3.1과 같은 값이다(출처 표기 `Ref: FD2321/TR1 Table 3.1`).

**보충 노트 (2008, FD2320 정정).**

- 보충 노트는 `H = d x (v + 0.5) + DF`를 표 2의 머리에 쓰고, 최종식이 FD2321/TR1 `page 10 (section 3.5)`에 있으며 FD2320과 FD2321 두 보고서에서 같다고 적는다.
- 이 노트는 FD2320/TR2 표 13.1의 문턱(`1.25 - 2.0` Significant, `>2.0` Extreme)이 FD2321과 다르다는 점을 정리한다. 속도 상수는 두 보고서 모두 0.5이다.
- 이 노트와 FD2320/TR2 원문에서 1.5를 쓰는 식은 찾지 못했다. FD2320/TR2 원문 자체는 열지 않았다.

### 1.4 비교

- 코드 상수 1.5는 FD2317(2003)의 `d(v+1.5)+DF`의 상수 1.5와 같다.
- 코드 상수 1.5는 FD2321/TR1·TR2(2006)의 `d(v+0.5)+DF`의 상수 0.5와 다르다.
- 코드 주석 `DEFRA 2006`은 상수 1.5와 맞지 않는다. 2006년판 식의 속도 상수는 0.5이다.
- 매뉴얼의 `DEFRA 2003`·FD2317 인용은 상수 1.5와 맞는다.
- 1.5가 0.5에 DF를 합쳐 넣은 값이라는 근거는 어느 출처에서도 찾지 못했다. FD2317은 1.5를 "속도가 0이고 깊이가 큰 경우의 위험을 위한 덧셈 항"이라고 설명하고, DF는 따로 0, 1, 2로 둔다.
- 코드 줄 `H*(Vc+1.5)`에는 DF 항이 없다. 이것은 DF=0인 경우(잔해 가능성이 없는 경우)의 식과 같다. DF 생략에 대한 문서 설명은 이 조사에서 찾지 못했다.
- 확인하지 않은 것은 두 가지이다. 하나는 코드 변수 `Vc`가 속도인지(단위가 m/s인지)이다. 다른 하나는 코드 주석 작성자(ALD)가 2006년판을 의도하고 상수를 잘못 남겼는지이다. 이 두 가지는 이 조사 범위 밖이다.

### 1.5 제안 결론

- 제안 분류는 **B (문서 오기: 코드 주석 `DEFRA 2006`이 실제 상수와 어긋남)** 이다. 매뉴얼의 `DEFRA 2003` 서술은 상수 1.5와 맞는다.
- 보조 분류로 **C (DF 항 생략을 설명하지 않은 누락)** 를 붙일 수 있다.
- 2006년판 식(0.5)을 의도했다면 코드 결함 후보가 된다. 이 판단은 코드 작성자 의도를 알아야 하므로 이 조사에서 확정하지 않았다.
- 노트에 넣을 한 문장: "`util.cpp:218`의 상수 1.5는 FD2317(2003, 인쇄 p.31)의 $HR=d(v+1.5)+DF$와 같고, 2006년 FD2321의 $HR=d(v+0.5)+DF$(TR1 3.5절 인쇄 p.10)와 다르며, 코드 주석의 `DEFRA 2006`은 이 상수와 맞지 않고 DF 항은 코드에 없다."

---

## 2. LB1-235: 시간간격 조건 (`factor of 2`)

### 2.1 출처

| 약칭 | 서지 | URL | 열람 상태 |
|---|---|---|---|
| 매뉴얼 2.6.2 | Bates, P., Horritt, M., Wilson, M., Hunter, N. (2005, 22 June). *LISFLOOD-FP User manual and technical note, Code release 2.6.2*. Univ. of Bristol. | https://www.bristol.ac.uk/media-library/sites/geography/migrated/documents/lisflood-manual-v2.6.2.pdf | 열어서 글자 확인함 |
| Hunter 2005 | Hunter, N.M., Horritt, M.S., Bates, P.D., Wilson, M.D., Werner, M.G.F. (2005). An adaptive time step solution for raster-based storage cell modelling of floodplain inundation. *Advances in Water Resources* 28(9), 975-991. doi:10.1016/j.advwatres.2005.03.007 | https://www.sciencedirect.com/science/article/abs/pii/S0309170805000850 | 열지 못함 (403, 유료). Semantic Scholar는 공개 PDF 없음(`CLOSED`)으로 표시한다. ResearchGate는 접속 차단 페이지를 돌려준다. |
| Werner & Lambert 2007 | Werner, M.G.F., Lambert, M.F. (2007). Comparison of modelling approaches used in practical flood extent modelling. *Journal of Hydraulic Research* 45(2), 202-215. doi:10.1080/00221686.2007.10525036 | https://www.tandfonline.com/doi/abs/10.1080/00221686.2007.10525036 | 열지 못함 (403). Semantic Scholar는 공개 PDF 없음(`CLOSED`)으로 표시한다. |
| Hunter 박사논문 | Hunter, N.M. (2005). *Development and assessment of dynamic storage cell codes for flood inundation modelling*. PhD thesis, Univ. of Bristol. | https://research-information.bris.ac.uk/files/34500523/424007.pdf | 공개 파일 주소는 확인했으나 내려받기가 차단되었다(Cloudflare 확인 화면, WebFetch 403). 열지 못함. |
| 매뉴얼 5.9.6 | LISFLOOD-FP User manual, Code release 5.9.6 (Univ. of Bristol). | https://www.bristol.ac.uk/media-library/sites/geography/migrated/documents/lisflood-manual-v5.9.6.pdf | 열어서 확인함. 적응 시간간격 식은 싣지 않고 서술만 한다. |
| Neal 외 | Neal, J. 외, LISFLOOD-FP 세 모델 비교 논문(White Rose 승인 원고). | http://eprints.whiterose.ac.uk/79279/1/Neal_revised.pdf | 열어서 확인함. 시간간격 식은 그림이라 글자로 뽑히지 않았다. |

### 2.2 확인한 원문 (매뉴얼 2.6.2, 인쇄 p.38)

이 매뉴얼은 2008년 bridge판 매뉴얼의 해당 대목과 같은 글이다. 이 매뉴얼의 서지는 Hunter 외 논문을 `(in press) ... An unconditionally stable explicit solution for raster-based storage cell modelling of floodplain inundation. Advances in Water Resources`로 적는다. 출판 제목은 Hunter 2005의 `An adaptive time step solution ...`로 바뀌어 있다.

식 [11]~[14]는 다음과 같다(글자로 뽑은 그대로의 의미를 LaTeX로 옮김).

- 식 [11]: 확산 방정식

$$\frac{\partial h}{\partial t} - \alpha\left(\frac{\partial^2 h}{\partial x^2}+\frac{\partial^2 h}{\partial y^2}\right)=0$$

- 식 [12]: 정사각 격자의 양해법

$$\frac{h^{t+1}_{i,j}-h^{t}_{i,j}}{\Delta t}-\frac{\alpha}{\Delta x^2}\left(h^{t}_{i+1,j}+h^{t}_{i-1,j}+h^{t}_{i,j+1}+h^{t}_{i,j-1}-4h^{t}_{i,j}\right)=0$$

- 식 [13]: 폰 노이만 안정성 조건 (원문 `von Neumann stability analysis produces the following time step condition`)

$$\Delta t \le \frac{\Delta x^2}{4\alpha}$$

- 식 [14]: 수력 모델의 최적 시간간격 (원문 `an optimal time step for the hydraulic model at a specific location is given by`)

$$\Delta t=\frac{\Delta x^{2}}{4}\min\left(\frac{2\,n}{h_{flow}^{5/3}}\left|\frac{\partial h}{\partial x}\right|^{1/2},\ \frac{2\,n}{h_{flow}^{5/3}}\left|\frac{\partial h}{\partial y}\right|^{1/2}\right)$$

- 글자 추출에서 `5/3` 지수와 `1/2` 지수는 확인했다. 분자의 `2 n`은 추출문에서 `2 n ∂h 1/2`로 나온다. 앞에 붙는 계수는 $\Delta x^2/4$이다.
- 식 [14] 뒤의 문장은 다음과 같다.

> We thus arrive at an expression for the time step similar in form to that used by Werner & Lambert (in press) but larger by a factor of 2. In Werner & Lambert (in press) the time step was set to allow small chequerboard oscillations to decay down to a flat free surface, whereas in this analysis we counter the build up of these oscillations directly, and hence can use a larger time step.

- 매뉴얼 2.6.2의 서지 항목은 `Werner, M.G.F. & Lambert, M.F. in press. Evaluation of modelling approaches for river reach scale inundation modelling, Journal of Hydraulic Research.`이다. 이 항목은 bridge판의 서지와 같다.
- bridge판 매뉴얼에서 같은 식은 [13]~[16] 번호로 붙고, `factor of 2` 문장은 p.50에 있다. 번호는 bridge판이 2 더 크다. 이 번호 차이는 bridge판 안 앞쪽 식 두 개가 추가된 결과로 보이며, 이 조사에서는 추가된 식이 무엇인지 확인하지 않았다.

### 2.3 비교

- 매뉴얼 2.6.2의 식 [14]와 bridge판 식 [16]은 계수가 모두 $\Delta x^2/4$이다. 두 판 사이에 계수 차이는 없다.
- 식 [14]의 $\Delta x^2/4$는 확산 방정식의 폰 노이만 조건 $\Delta t \le \Delta x^2/(4\alpha)$(식 [13])에서 직접 나온다. 이 도출은 매뉴얼 안에서 확인했다.
- Werner & Lambert 논문의 시간간격 식은 열지 못했다. 따라서 그 논문의 계수는 직접 확인하지 못했다.
- 매뉴얼 글만으로 추정하면, Werner & Lambert의 계수는 $\Delta x^2/4$의 절반인 $\Delta x^2/8$ 꼴이다. 이것은 "similar in form ... but larger by a factor of 2"라는 서술에서 나온 추정이며 원문 확인이 아니다.
- 매뉴얼은 인용 논문을 `in press`로만 쓴다. 출판 논문(2007, JHR 45(2), 202-215)의 제목은 "Comparison of modelling approaches used in practical flood extent modelling"이다. 매뉴얼에 적힌 제목 "Evaluation of modelling approaches for river reach scale inundation modelling"과 다르다. 제목 변경은 사실이다. 같은 논문이라는 판단은 저자·학술지가 같다는 사실에 근거한 추정이다.
- Hunter 2005 논문 본문의 식은 열지 못했다. 매뉴얼 2.6.2의 식 [11]~[14]가 이 논문의 내용을 옮긴 것이라는 점은 매뉴얼 서지와 Neal 외 논문의 서술(`The optimum time step ... analogy to a diffusion system`)과 맞다. 그러나 이는 2차 근거이다.
- 매뉴얼 5.9.6은 적응 해법의 시간간격이 $(1/\Delta x)^2$에 비례한다고만 서술하고 식은 싣지 않는다. 이 서술은 $\Delta t \propto \Delta x^2$과 맞는다.
- 코드 `fp_flow.cpp:155,160`의 계수는 LB1-234와 같다고 기존 비교표에 적혀 있다. 이 조사에서 코드는 다시 열지 않았다.

### 2.4 제안 결론

- 제안 분류는 **A (판 차이: 문서에만 있는 서술)** 가 아니라 **H (비교 불가: 외부 원문 식을 확인하지 못함)** 이다.
- 단, 계수 $\Delta x^2/4$ 자체는 같은 저자 그룹의 2005년 매뉴얼 식 [14]와 같고 폰 노이만 조건에서 도출되므로, bridge 매뉴얼 [16]의 계수에 오류가 있다는 증거는 없다.
- `factor of 2`는 계수 비교의 대상이 Werner & Lambert 논문이다. 이 논문 원문을 확보하면 H를 해소할 수 있다. 확보하면 그 논문의 식 번호와 계수가 $\Delta x^2/8$ 꼴인지 확인하면 된다. 이때 같은 쪽의 `chequerboard` 서술도 함께 확인해야 한다.
- 노트에 넣을 한 문장: "bridge 매뉴얼 p.50의 식 [16] $\Delta t=\frac{\Delta x^2}{4}\min(\cdots)$는 2005년 매뉴얼 2.6.2 식 [14](인쇄 p.38)와 같은 계수이며 폰 노이만 조건 $\Delta t\le\Delta x^2/(4\alpha)$(식 [13])에서 나오고, 'factor of 2' 비교 대상인 Werner & Lambert(2007, JHR 45(2), 202-215)의 식은 원문을 열지 못해 확인하지 않았다."

---

## 3. 열지 못한 자료 (정리)

- Hunter 외 2005 (Adv. Water Resour. 28, 975-991) 본문: 유료·차단으로 열지 못했다.
- Werner & Lambert 2007 (JHR 45(2), 202-215) 본문: 유료·차단으로 열지 못했다.
- Hunter 박사논문(Bristol, 2005): 공개 주소를 찾았으나 내려받기가 차단되었다.
- FD2320/TR2 원문: 열지 않았다. 보충 노트의 서술로만 확인했다.
- 위 항목은 사용자가 PDF를 직접 받아 주면 같은 방식으로 식 번호와 계수를 확인할 수 있다.

## Claude 확인과 최종 결론 (10-21)

이 절이 최종이다.

### LI2-203 최종 결론: B 문서 오기(코드 주석의 출처 연도)

- `util.cpp:218` `Haz = Arrptr->H[p0] * (Vc + C(1.5)); // Changed to equation from DEFRA 2006 (ALD)`의 계산식은 FD2317(2003) 식 `Hazard rating = d(v+1.5)+DF`에서 DF를 뺀 것과 같다.
- FD2321/TR1(2006) §3.5의 최종식은 `HR = d x (v + 0.5) + DF`이다. 코드의 상수 1.5는 이 식과 다르다.
- 매뉴얼(PDF p.38)의 `based on DEFRA 2003`은 코드 계산식과 맞는다.
- 따라서 틀린 것은 코드 주석의 "DEFRA 2006"이다. 매뉴얼과 코드 계산식은 같은 2003 식을 따른다.
- 코드는 DF 항을 더하지 않는다. 이것은 DF = 0인 경우와 같다.
- 코드 작성자가 2006 식을 쓰려고 했는지는 원문으로 가를 수 없다. 그래서 E로 두지 않는다. 계산식이 자기 주석 하나와만 어긋나고, 같은 판 매뉴얼과는 맞기 때문이다.
- 노트에 쓸 결론 문장: "위험도 식 `H*(Vc+1.5)`는 DEFRA FD2317(2003) 식 d(v+1.5)+DF에서 DF를 뺀 것과 같다. 코드 주석의 'DEFRA 2006'은 FD2321(2006) 최종식 d(v+0.5)+DF와 다르다(외부 원문: FD2317 p.31, FD2321/TR1 p.10)."

### LB1-235 최종 결론: H 코드 대조 대상 아님(외부 문헌 사이의 비교 주장)

- bridge p.50 식 [16]의 계수 $\Delta x^2/4$는 코드 `fp_flow.cpp:160` `*TSptr=getmin(*TSptr,(C(0.25)*Parptr->dy*Parptr->dy/alpha));`와 같다. 이 대응은 LB1-234에서 판정했다.
- 2005 매뉴얼 2.6.2 p.38도 같은 계수와 같은 "factor of 2" 문장을 적는다(위 sonnet 판독).
- 남은 주장은 "Werner & Lambert의 식보다 2배 크다"는 외부 논문 사이의 비교다. 이것은 코드 동작에 대한 주장이 아니다.
- Werner & Lambert(2007, J. Hydraulic Research 45(2), 202–215, doi:10.1080/00221686.2007.10525036)와 Hunter et al.(2005, Advances in Water Resources 28, 975–991, doi:10.1016/j.advwatres.2005.03.007)는 Unpaywall과 Semantic Scholar에서 공개 사본이 없다(10-21 조회, `is_oa` False, `openAccessPdf` CLOSED). Semantic Scholar 인용 문맥 200건에도 이 계수를 옮긴 문장이 없었다.
- 노트에 쓸 결론 문장: "bridge판 [16]의 $\Delta x^2/4$는 코드 `fp_flow.cpp:160`의 `C(0.25)`와 같다. Werner & Lambert 식보다 2배 크다는 문장은 외부 문헌 사이의 비교이며 코드 대조 대상이 아니다."

분류별 개수 변화: X 2 → 0. LI2-203은 B, LB1-235는 H.
