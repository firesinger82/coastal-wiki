<a id="external-data-conventions"></a>

## 외부 조석 자료: 판본·변수·변환 근거

아래는 **공급기관 원문을 대조한 AI 요약**이다. 개별 atlas 파일의 값·경계 보간·ADCIRC 실행을 확인한 결과가 아니다. 웹 문서는 2026-09-14 조회판이며, 같은 제품명이라도 배포판과 예측 소프트웨어 설정을 함께 기록한다.

| 자료와 대조 판본 | 확인한 정의 | ADCIRC 입력 준비에서의 의미 |
|---|---|---|
| FES2022b, [handbook][fes-hdbk] Issue 2.0, 2026-02-03, 인쇄 pp. 1, 6–7, 15, 17, 24–25 | Cartesian 배포는 1/30°·34분조. `amplitude`는 cm, `phase`는 지각(deg). 해수면 조석과 radial loading을 구분. mask 0=원 해양값, 1=외삽, 2=육지, 3=호수. Appendix A의 예시 결측값은 `1.844674e+19` | 결측을 먼저 제외하고 cm→m. 실제 파일의 좌표·변수·속성을 읽는다. 유한요소 원격자와 Cartesian 형식은 구분하며, mask=1의 유한값을 연안 정확도 보증으로 사용하지 않는다. |
| NAO99Jb, [공식 README][nao-readme] 2000-09-09, §2/4/5/7 | 일본 주변 110–165°E, 20–65°N, 5분 격자·16단주기 분조. `_gc`는 지심 조석, 일반 제품은 해저에 대한 ocean tide; radial loading은 전지구 0.5° 제품만 있고 지역 모델은 없다. 예측 시각은 UTC, 출력은 cm. §7은 `nao2xyap.f`로 Greenwich phase 형식 변환을 안내 | [공식 패키지][nao-code]의 `nao2xyap.f:90–93,116–122,167`은 헤더의 진폭/위상 scale과 결측을 해석한다. 출력 진폭은 cm, 위상은 deg. 정수 격자를 그대로 EMO로 쓰지 않는다. 단주기 합성의 lag 부호는 `naotidej.f:1112–1117,757–771,807–817`에서 확인했다. |
| TPXO10-atlas-v2, [OSU 제품 페이지][tpxo-atlas]에 명시된 2024-08-14 배포판 | MSL에 대한 해수면 조화상수, 1/30° atlas. 기본 전지구 해와 지역 patch를 결합. OSU binary/NetCDF와 TMD3 통합 NetCDF는 다른 형식 | [OTPS/OTPSnc][otps]는 상수 추출·예측 도구다. 이번에는 특정 배포 파일의 변수·단위·복소 부호·결측을 대조하지 않았다(`source-needed`). FES/NAO의 scale·위상 변환식을 그대로 적용하지 않는다. |

NAO 코드 인용은 위 `naotidej000909.tar.gz` 안의 `naotidej/` 기준이다(패키지 SHA-256 `f61c3e473c5c40812b76e27063016cec0602c756c86607aee3c8b2108c862328`). 이는 입력 변환·합성 인터페이스의 한정 판독이며 예측 패키지 전체 검증이 아니다.

### FES loading tide와 fort.24의 구분

FES handbook p. 6의 loading atlas는 **radial component**이고, [PyFES 설정][pyfes-guide]도 `tide`와 `radial`을 분리한다. ADCIRC `fort.24`는 self-attraction/earth-load 강제 항이며 `SALTAMP/SALTPHA`를 `TIP2`에 합성한다(`docs/technical_reference/input_files/fort24.rst:1–8`; `src/timestep.F:1543–1555`). **radial 변위 파일을 단위만 바꿔 fort.24로 쓰는 변환은 이 근거로 성립하지 않는다.** 두 변수의 물리량·퍼텐셜 환산·부호·분조를 잇는 정의가 추가로 필요하다(`source-needed`). 경계 수위 EMO/EFA 준비와 별도로 다룬다.

### 변환 결과를 무엇과 대조할 것인가

1. **성분과 단위를 먼저 맞춘다.** FES는 위 handbook의 ocean tide 파일, NAO는 README의 ocean/geocentric/radial 선택을 명시한다. 진폭과 위상은 동일 제품·판본·격자점/보간에서 한 쌍으로 추출한다. NAO의 전체 예측에는 16단주기 외에 추론 분조와 장주기가 포함되므로, NBFR 일부 분조 합성과 전체 예측값을 곧바로 같다고 판정하지 않는다([NAO README §4][nao-readme]).
2. **공급기관 예측기와 설정을 고정한다.** FES handbook p. 20은 PyFES ≥2025.2.0을 지정한다. 같은 페이지의 Schureman order 3 기본값 설명과 [PyFES 2026.5.3 안내][pyfes-guide]의 `FESSettings` order 1 기본값 설명은 다르므로, 버전·천문식·minor inference·장주기 포함 여부를 명시하고 실제 설정을 확인한다. 공급기관의 특정 판본 설명을 다른 판본의 기본값으로 전파하지 않는다.
3. **위상은 원형량으로 처리한다.** [PyFES 조화상수 표현][pyfes-analysis]과 NAO `naotidej.f:1112–1117`은 진폭/위상을 cos·sin 성분으로 표현한다. 이 식에서 도출하면 $z=Ae^{ig}$를 보간한 후 $A=\lvert z\rvert,\;g=\operatorname{atan2}(\Im z,\Re z)$로 복원할 수 있다. $g$는 계산 시 radian이다. 359°와 1°를 직접 산술평균하지 않는다. 이 표현 선택만으로 해안 mask·육지를 가로지르는 보간·외삽의 적합성이 보장되지는 않는다.
4. **같은 위치·실제 UTC 시각에서 같은 분조를 합성한다.** FES의 lag와 Greenwich 천문 인수·노달보정 정의는 [PyFES nodal 식][pyfes-nodal], NAO의 시각·성분은 README §4에 근거한다. ADCIRC 쪽은 아래 §D/F의 `AMIG*TimeH+FACE−EFA`에 맞춰 epoch와 보정의 포함 여부를 대조한다. 단위·시각·분조·보정을 맞춘 뒤 원 격자점/내삽점/연안점 및 시작·중간·끝 시각의 차이를 기록한다. 이는 **변환 확인 계획**이며 실제 비교는 미수행이다.
5. **품질 표시를 보존한다.** FES 제품 mask와 PyFES 반환 `flags`는 다른 정보다. 후자는 양수=사용한 내삽점 수, 음수=외삽, 0=정의되지 않음이다([PyFES Prediction Functions][pyfes-guide]). 미리 외삽된 atlas를 내삽하면 반환 flag만으로 원 atlas의 외삽 여부를 알 수 없으므로 제품 mask도 함께 확인한다(두 정의에서 도출한 확인 방법).

<a id="independent-observation-and-errors"></a>

## 독립 관측과 오차 기준

**관측 후보**로 [UHSLC Research Quality Data][uhslc-data]의 hourly 자료를 사용할 수 있다. RQD와 기본 QC만 거친 Fast Delivery를 구분하고 정점 metadata·품질 평가·시각 오류 기록을 확인한다. 정점의 zero는 임의의 station datum일 수 있고, 같은 장소의 A/B 시계열은 기준면이 다를 수 있다. 수위의 평균을 맞춘 경우 제거한 평균과 기간을 별도로 남긴다. RQD라는 명칭이 해당 모델에 대한 검증 독립성을 보장하지 않는다.

**독립성**은 관측 정점 ID·별칭·좌표·사용 기간을 경계 DB의 동화 자료와 ADCIRC 보정/경계 구축에 사용한 자료에 각각 대조해 판정한다([BUILD-PLAN §4–6](../../../../BUILD-PLAN.md)). FES handbook p. 6과 Appendix B는 동화 정점 목록을, [TPXO10-atlas 페이지][tpxo-atlas]는 연안 관측 동화와 비동화 자료 검증의 구분을 제공한다. FES는 모든 동화 위치에서 모든 분조를 사용한 것도 아니다. 따라서 이름이 목록에 없거나 검증 기간만 다르다는 이유로 독립성을 확정하지 않고, 정점·분조·기간별 이력이 불명확하면 **독립성 미확정**으로 남긴다. 원래 DB와의 일치는 변환 확인이고, 관측에 대한 물리 검증은 별도다.

**지표 정의**: 동일한 단위·분조·위상/노달보정 규약으로 환산한 진폭 $A$, lag $g$에서 다음을 구분한다. $m,o$는 모델/관측, $i$는 정점, $k$는 분조다. 아래 복소 오차식은 [Wang et al. (2022) §3.1 식(3)][wang2022]의 한 주기 평균식에서 전개한 것이며, 이번 ADCIRC의 검증 결과가 아니다.

| 지표 | 정의와 해석 |
|---|---|
| 진폭 차이 | $\Delta A=A_m-A_o$. 진폭이 작은 분조의 상대오차는 분모와 관측 불확실성을 함께 표시한다. |
| 순환 위상 차이 | $\Delta g=\operatorname{atan2}[\sin(g_m-g_o),\cos(g_m-g_o)]$. 삼각함수 입력은 radian, 보고 시 degree로 바꾼다. $A=0$이면 위상은 정의되지 않으므로 위상 지표에서 제외하고 진폭/복소 지표에는 남긴다(조화표현에서 도출). |
| 정점·분조 복소 거리 | $E_{ik}=\lvert A_{m,ik}e^{ig_{m,ik}}-A_{o,ik}e^{ig_{o,ik}}\rvert$. 위상 래핑에 연속적이며 진폭과 위상 차이를 함께 반영한다. |
| 한 분조의 정점군 RMS | $D_k=\sqrt{\frac{1}{2N}\sum_{i=1}^{N}E_{ik}^{2}}$. 동일 가중치 N개 정점에 대해 **한 주기를 평균한 RMS**다. 복소 거리의 RMS보다 $1/\sqrt{2}$ 작다. 가중치/정점군을 바꾸면 정의도 명시한다. |
| 분조군 RSS | $\mathrm{RSS}=\sqrt{\sum_{k\in K}D_k^2}$. 사용 분조 집합 K와 정점군을 표시한다. 유한·불규칙 관측창의 전체 시계열 RMSE와 자동으로 같지 않다. |
| 시계열 bias·RMSE | 공통 유효 시각의 $e_j=\eta_{m,j}-\eta_{o,j}$에 대해 $b=M^{-1}\sum_j e_j$, $\mathrm{RMSE}=\sqrt{M^{-1}\sum_j e_j^2}$. 이는 실제 표본에 적용하는 정의이며, 위 한 주기/분조군 평균과 구별한다. 평균 제거·필터·ramp 제외를 했다면 처리와 표본 수를 함께 보고한다. |

관측에서 조석 성분을 추정할 때는 분석창과 분조 분리도 먼저 확인한다. [PyFES 조화분해의 Rayleigh 조건][pyfes-analysis]은 주파수 $\nu$를 cycles/time으로 두면 $T>C_R/\lvert\nu_1-\nu_2\rvert$이며 $C_R\ge1$이다. 충족 여부만으로 결측·잡음·행렬 조건까지 검증되지는 않는다. 모델과 관측에 공통 분석창·분조·노달보정·시간/기준면을 적용하고, 미분리 분조와 추론 성분은 따로 표시한다. 조석만 계산한 출력과 관측 총수위 사이에는 기상 등 잔차가 포함될 수 있다([PyFES Observation Equation][pyfes-analysis]); 이를 모두 조석 경계 오차로 해석하지 않는다.

**허용치 선정은 미완**이다. 정점·기간·목적·관측 불확실성이 정해져야 물리적 합격 기준을 정할 수 있다([BUILD-PLAN §4–6](../../../../BUILD-PLAN.md)). 문헌의 RMS/RSS 수치는 그 자료·해역의 결과이며 ADCIRC 공통 tolerance가 아니다. 현재 확보한 것은 제품 정의·변환 확인 방법·관측 후보·지표 식이다. 실제 atlas/관측 파일의 품질·변환 결과·기준해/관측 대조 및 목적별 허용치는 아직 확인하지 않았다.

[fes-hdbk]: https://www.aviso.altimetry.fr/fileadmin/documents/data/tools/hdbk_FES2022.pdf
[nao-readme]: https://www.miz.nao.ac.jp/rise/s/nao99/README_NAOTIDE_En.html
[nao-code]: https://www.miz.nao.ac.jp/rise/s/nao99/data/naotidej000909.tar.gz
[tpxo-atlas]: https://www.tpxo.net/global/tpxo10-atlas
[otps]: https://www.tpxo.net/otps
[pyfes-guide]: https://cnes.github.io/aviso-fes/user_guide.html
[pyfes-analysis]: https://cnes.github.io/aviso-fes/theory/harmonic_analysis.html
[pyfes-nodal]: https://cnes.github.io/aviso-fes/theory/nodal_corrections.html
[uhslc-data]: https://uhslc.soest.hawaii.edu/datainfo/
[wang2022]: https://doi.org/10.5194/os-18-881-2022
