---
title: "adcirc tide harmonic prep"
topic: tides
canonical_source: self
reference_contract_date: 2026-09-16
reference_contract_evidence_by: "Claude Opus (claude-opus-5) — 선정 원문·코드 사실 추출"
reference_contract_by: "Codex — 근거 판정·회귀/해석해 구분·문서 보강"
reference_contract_human_approval: not-issued
reference_contract_scope: "quarter-annular 입력·출력 비교 계약과 해석해 적용 경계의 한정 대조. 실제 모델 실행·수치/물리 검증·기존 전체 노트 재검증 아님."
external_evidence_date: 2026-09-14
external_evidence_review: "Claude Fable 5.1 — 외부 제품·변환 확인 방법·독립 관측/지표 원문 대조; 과학적 사람 승인 아님"
external_evidence_human_approval: not-issued
external_evidence_scope: "외부 조석 제품 정의·변환 확인 방법·관측 독립성·지표 근거와 관련 무근거 권고 정정. 실제 자료/실행/수치/물리 검증 아님."
citation_status: verified
has_source_needed: true
evidence_extension_date: 2026-09-14
evidence_extension_by: "Codex — 입력 품질·검증 확인 방법 보강"
evidence_extension_scope: "새 확인 방법 절과 NTIP/NTIF·AMIG 상세 정의 대조. 기존 다른 절 재검증 아님; 실제 자료/실행/수치/물리 검증 미수행."
evidence_extension_review: "Claude Fable 5.1 — 새 확인 방법 원문 대조; 공식 예제의 추가 구분은 Codex 최종 검토 대상"
evidence_extension_human_approval: not-issued
source_correction_date: 2026-09-14
source_correction_by: "Codex — scoped source cross-reference"
source_correction_human_approval: not-issued
source_correction_review: "Claude Fable 5.1 — NBFR/첨자/노드/위상/시간/ETRF 변경 원문 대조; 과학적 사람 승인 아님"
source_correction_scope: "NBFR 입력 레코드/첨자와 경계 노드 순서·위상/시간 기준, 전통 분조 경로 ETRF 항. 전체 노트 재검증·실제 실행·수치/물리 검증 아님."
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-tide-harmonic-prep.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시. 2026-09-14: NBFR 입력·노드/분조 순서·위상/시간·ETRF 항의 한정 대조, 본문 한정 대조 범위 참조. 실제 실행·수치/물리 검증 미수행."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---


## 2026-09-14 한정 대조 범위

이 보강의 코드 판본은 ADCIRC `6037225ce4573efd3c1f8877a5dc908d01c199a8`이다. 아래 `src/` 인용의 루트는 `models/ADCIRC/raw/source_code/adcirc/`다. **문서 지원·코드 구현** 중 NBFR 입력, 경계 노드 전달, 위상/시간 기준, 전통 분조 경로의 ETRF 항을 대조했다. **실행 확인·수치 검증·물리 검증·개별 입력자료 품질 확인은 수행하지 않았다.** 이 코드 대조는 다른 절과 외부 DB 규약을 포함하지 않는다. 외부 자료에 대한 별도 보강 범위는 harmonic-prep의 「외부 조석 자료」 절을 따른다. 과거 검증 이력과 이번 정정을 구분하며 이번 정정에 대한 사람 승인은 발급하지 않았다.

<a id="input-quality-and-validation"></a>

## 입력 품질·실행·검증 확인 방법 (2026-09-14 보강)

이 절은 **확인할 증거와 수행 순서**를 정한다. 실제 사용할 조석 DB·지형·관측자료와 허용오차는 아직 선정하지 않았으므로 **입력 품질·실행 확인·수치 검증·물리 검증은 미완**이다. 외부 DB 정의와 관측·오차 지표의 원문 대조는 아래 별도 절에 정리했다. 확인되지 않은 변환 세부·정량 권고는 `source-needed`로 남긴다.

### 문서와 코드가 다를 때의 입력 기준

[공식 조석 개요](https://adcirc.github.io/adcirc/user_guide/model_configuration/tides/index.html)의 두 설명은 [상세 파라미터 정의](https://adcirc.github.io/adcirc/technical_reference/parameter_definitions/index.html) 및 이 노트의 S 판본 코드와 구별해야 한다(S는 위 한정 대조 범위의 전체 SHA).

- 개요의 분조 수 설명은 `NTIP`에 붙어 있지만, 상세 정의에서 **NTIP는 퍼텐셜/SAL 사용 방식**, **NTIF는 퍼텐셜 분조 수**다. 코드도 `NTIP`를 0–2로 검사하고 `NTIF`로 분조 입력을 반복한다. `docs/user_guide/model_configuration/tides/index.rst:15–19`; `docs/technical_reference/parameter_definitions/index.rst:452–459,758–759`; `src/read_input.F:1717–1745,3335–3349`.
- 개요의 `AMIG` 설명에는 amplitude가 나오지만, 상세 정의와 코드에서 **AMIG는 주파수**, 경계 진폭은 **EMO**다. `PER=2π/AMIG`와 시간 인수에 곱하는 위치를 함께 확인한다. `docs/user_guide/model_configuration/tides/index.rst:29–32`; `docs/technical_reference/parameter_definitions/index.rst:789–801`; `src/read_input.F:3445–3455`; `src/gwce.F:1638–1649`.

위 `docs/`·`src/`의 루트는 `models/ADCIRC/raw/source_code/adcirc/`다. 2026-09-14 웹 조회에서도 개요의 같은 표현을 확인했다. 이 두 불일치의 대조를 문서 사이트 전체의 정확성 판정으로 확대하지 않는다.

### 입력 품질 확인표

다음은 [위키의 입력 품질 기준](../../../../BUILD-PLAN.md)에 따른 확인 계획이다. 실제 자료값을 채우는 공간은 coastal-runs이며, 이 노트는 일반 절차와 출처를 제공한다.

| 확인 대상 | 설정 전에 확보·대조할 증거 | 현재 확인 수준/미확정 |
|---|---|---|
| 조석 DB·분조 정의 | 제품명·판본·문서 절·분조 목록·각주파수·해수면 조석/하중 조석의 변수 의미·단위 | [제품별 정의](#external-data-conventions)에 확인 범위 명시. TPXO 개별 파일 형식과 실제 자료는 미확인 |
| 지형·좌표·기준면 | 지형과 조석·관측 자료의 좌표/기준면·수심 부호·변환 이력; fort.14 노드와 원자료 대응 | [fort.14 구조](https://adcirc.github.io/adcirc/technical_reference/input_files/fort14.html) 및 [수심 노트](../adcirc-bathymetry-input-foundation.md)로 진입. 개별 데이터 미확인 |
| 공간·시간 범위와 해상도 | 경계 노드가 제품 유효 영역에 포함되는지, 연안 mask/격자 해상도, 제품의 대표 기간·허용 예측 시각과 실행/관측 기간 | 사용할 자료가 미선정. 범위 밖·외삽·대표성 불확실성을 기록해야 함 |
| 결측·품질·오차 | 품질 플래그·결측값·제공기관의 오차/불확실성 정의; 제외·대체·보간 정책과 근거 | FES mask/결측 정의와 NAO scale/결측 처리, UHSLC QC 원문 확보. 실제 사용할 자료의 품질 판정은 미수행 |
| 분조·노드 순서 | NBFR 헤더와 각 분조 블록, 분조당 NETA개 행을 fort.14의 경계 구간/구간 내 순서와 대조 | 아래 §A 및 `src/mesh.F:1822–1834`, `src/read_input.F:3445–3470,3485–3497`. 실제 입력 대조 미수행 |
| 위상·시각·노달보정 | 위상 부호/기준 경도·시간대·epoch, STATIM/REFTIM과 FF/FACE 기준; 제공 제품이 이미 포함한 보정과 별도 보정의 중복 여부 | ADCIRC §D/F, FES/NAO 부호·예측 정의는 [외부 자료 절](#external-data-conventions). TPXO 규약과 실제 FF/FACE 변환은 미확인 |
| 변환·보간의 독립 확인 | 원 격자점과 변환 결과를 대조하고, 별도 계산 또는 제공기관 예측과 몇 위치·시각의 재합성을 비교. 해안 mask·위상 주기 경계 처리의 방법/오차를 기록 | 확인 방법은 계획. 특정 보간법·도구의 적합성/성능은 아직 확정하지 않음 |
| 퍼텐셜·SAL·초기 강제 | 경계 수위와 퍼텐셜/SAL을 구분한 선택 이유, NTIP/NTIF·분조·입력파일·ramp·초기시각의 정합 | §A/F와 [퍼텐셜의 한정 대조](adcirc-tide-forcing-implementation.md). SAL/full-formula 전체 재검증은 미수행 |

### 실행 확인에서 확보할 것

1. 실행파일의 코드 판본·빌드 옵션, 입력파일 버전, 실행 명령과 종료 상태를 고정한다. 입력 검사와 계산 경로 확인을 분리한다([BUILD-PLAN §4–6](../../../../BUILD-PLAN.md)).
2. `fort.16`의 NTIP 선택 및 NBFR 분조·노드·진폭·위상 echo를 입력과 대조한다. `src/read_input.F:1731–1745,3431–3435,3485–3497`은 로그 생성 위치다. echo만으로 내부 계산 경로의 실행이나 물리 적합성을 확정하지 않는다.
3. 순수 주기 수위 경계 예제에서는 선택한 경계점·시각의 출력과 §A/D/F 합성을 대조한다. ramp와 함께 작동하는 다른 경계 항이 있으면 그 항까지 확인해야 한다. 합성 코드의 위치는 `src/gwce.F:1638–1649`이며 **이번에 이 대조 실행은 하지 않았다**.
4. 출력의 정점·변수·시간 범위와 간격을 확인한다. 조화분해는 강제 입력의 NBFR와 별도로 NFREQ·NAMEFR·HAFREQ/HAFF/HAFACE, THAS/THAF·NHAINC 및 출력 위치 선택을 확인한다. `fort.51`은 지정 수위 정점의 진폭/위상 출력이다. 근거: `docs/technical_reference/parameter_definitions/index.rst:1140–1177,1191–1213`; `docs/technical_reference/output_files/fort51.rst:1–23`. 여기서는 세부 출력 형식 코드의 전체 유효값을 확정하지 않는다.

### 수치 검증과 물리 검증의 분리

- **회귀 예제**: 공식 testsuite의 `adcirc_quarterannular-2d-netcdf`에 대해 [입력·control·자동 비교 계약](#quarterannular-reference-contract)을 한정 대조했다. 비선형 입력과 선형 해석해의 조건을 구분하며 실제 회귀 실행·해석해 검증은 미수행이다.
- **수치 검증**: 사용할 해석해/기준해의 식·조건·출처, 물수지/보존 진단, 격자·시간간격 민감도와 오차 기준을 결과 전에 정한다. 회귀검사의 기본 tolerance를 해역의 물리 오차 기준으로 사용하지 않는다. 현재 기준해 대조와 허용오차 선정은 미수행이다([BUILD-PLAN §4–6](../../../../BUILD-PLAN.md)).
- **물리 검증**: 경계·보정에 사용한 자료와 독립적인 관측/실험을 구분하고, 정점/기간·기준면·시간대·결측·관측오차를 확인한다. 비교할 진폭·주기적인 위상 차이·시계열 오차의 정의와 허용 범위, 분조 분리와 분석창의 근거를 먼저 확보한다. 일반 조화분해 이론은 [조석 분석 방법](../../../../concepts/tides/03-analysis-methods.md), ADCIRC 관측검증 권고는 `docs/user_guide/model_configuration/tides/index.rst:57–65`다. [독립 관측·오차 지표](#independent-observation-and-errors)의 원문·정의는 확보했다. **선정 정점/기간·실제 분석·목적별 허용오차는 미확정**이며 관측 대조를 수행했다고 쓰지 않는다.

외부 자료의 일반 규약과 관측·지표 근거는 아래에 정리했다. 다음 실제 입력 단계에는 atlas 판본·경계 노드·시각과 관측 정점/기간을 지정하고 변환 결과를 대조해야 한다. 기준해·보존/민감도와 목적별 허용치도 별도로 필요하다. 개인 실행 결과는 [coastal-runs 채널](../../../../RUNS-CHANNEL.md)에 둔다.

<a id="quarterannular-reference-contract"></a>

## 공개 quarter-annular 예제의 기준과 비교 계약 (2026-09-16)

이 절은 **공식 예제 설명·입력·비교 코드의 한정 대조**다. ADCIRC를 실행하거나 해석해 오차·수렴률·관측 적합성을 측정한 결과가 아니다. S는 위 ADCIRC 판본, T는 `models/ADCIRC/raw/source_code/adcirc-testsuite/`의 `72bb573073ea89e538890f9352dd8e92bae562f5`다. 아래 Q는 T의 `adcirc/adcirc_quarterannular-2d-netcdf/`를 뜻한다.

### 기준해와 저장된 control 출력의 역할

[공식 quarter-annular 설명][quarterannular-official]은 방사 대칭의 수심 변화 영역에서 **선형 2DDI·3D 문제의 해석해**가 가능하다고 설명한다. 같은 페이지의 실행 예제는 유한 진폭·이류·이차 저면마찰을 포함한다고 명시한다. Q의 `fort.15:8–12,28–30`도 해당 비선형 항을 켜고 회전 계수를 0으로 지정한다. 따라서 선형 해석해가 존재한다는 사실을 이 비선형 입력의 정확한 기준해가 확보됐다는 뜻으로 쓰지 않는다. 해석해와 계산을 비교하려면 지배식·마찰·강제·초기/경계 조건을 먼저 맞춰야 한다(앞 두 근거에서 도출한 적용 조건).

T는 릴리스 사이의 계산 일관성을 확인하는 testsuite다(`README.md:1–4`). 이 케이스의 자동 비교 기준은 Q의 `control/`에 저장된 출력이며, 비교기는 해석해를 계산하지 않는다(`test_runner/adcirc_test/adcirctest.py:429–445`). 저장된 control을 독립 관측이나 해석해로 표시하지 않는다. 해석해의 원문·조건은 다음 절에 연결했으며, **그 조건을 맞춘 ADCIRC 실행과 수치 검증은 미완(`source-needed`)**이다.

### 선형 조석해: 원문 조건과 이차 수심의 특수형

[Lynch & Gray (1978)][lynch1978-polar]의 선정 판독 범위는 인쇄면 1410–1412, 1414–1415(PDF 3–5, 7–8쪽)다. 식 (1)–(2)는 이류를 제외하고 미소 수위 진동·상수 선형 마찰률 $\tau$를 사용하는 수심평균 선형 방정식이다. 판독한 운동량식에는 Coriolis 항이 없다. 극좌표 조석 문제는 바람 없는 성분을 따로 풀며, $h=H_0r^n$, 안쪽 $r_1$과 측면 $\theta=0,\phi$에서 무유량, 바깥 $r_2$에서 $\Re\{\zeta_0(\theta)e^{i\omega t}\}$를 준다(식 (6)–(9)). 이 해는 주기 조석 응답이며 cold-start와 ramp를 포함한 전 시간 이력의 해가 아니다.

원문의 식 (20)–(25)를 **$n=2$, 각도에 무관한 한 분조 경계($j=0$)**로 제한하면 다음과 같이 무차원 반경으로 정리할 수 있다. 이는 원문 멱함수 해와 두 반경 경계조건에서 도출한 표기이며 새로운 실측 결과가 아니다. $A$는 바깥 경계의 복소 진폭, $H_0=h_1/r_1^2$, $\omega>0$이며 $x=r/r_1$, $x_2=r_2/r_1$로 둔다.

$$
\beta^2=\frac{\omega^2-i\omega\tau}{gH_0},\qquad
m_\pm=-1\pm\sqrt{1-\beta^2},\qquad
B(x)=m_-x^{m_+}-m_+x^{m_-}.
$$

$$
Z(r)=A\frac{B(r/r_1)}{B(x_2)},\qquad
\eta(r,t)=\Re\{Z(r)e^{i\omega t}\},\qquad
U_r(r)=-\frac{g}{\tau+i\omega}\frac{dZ}{dr}.
$$

$U_r$는 방사 방향 수심평균 속도의 복소 진폭이며 $u_r=\Re\{U_re^{i\omega t}\}$, 각도 방향 속도는 0이다. 속도식은 원문의 운동량식 (2)에서 도출했다. 이 표기는 $m_+\ne m_-$, $B(x_2)\ne0$인 경우에 한정한다. 중근에는 별도의 극한형이 필요하고, 감쇠 없는 공진에서 분모가 0인 경우 유한한 주기 정상해로 사용하지 않는다. $B'(1)=0$, $Z(r_2)=A$가 두 반경 경계조건을 만족하며, $Z$는 $r^2Z''+3rZ'+\beta^2Z=0$을 따른다(식 (20a), (23), (25d–e)에서 도출).

Q와 공유하는 **기하·주파수**는 $r_1=60960$ m, $r_2=152400$ m, $h_1=3.048$ m, $\phi=\pi/2$, $\omega=0.0001405257$ rad/s이며, 경계 진폭을 $A=0.3048$ m로 둘 수 있다. 그러나 원문의 $\tau$는 일정한 선형 마찰률이고 Q의 `FFACTOR=0.0025`는 이차 마찰계수다. **0.0025를 위 식의 $\tau$에 그대로 대입하지 않는다.** 또한 `NOLIFA/NOLICA/NOLICAT=1`인 Q를 그대로 이 선형 방정식의 입력으로 간주하지 않는다. 해석해 대조용 입력에서는 선택한 선형 항·마찰·회전·정상주기 비교창을 별도로 고정해야 한다(원문 식 (1)–(2), Q `fort.15:9–12,28–30`; S `docs/technical_reference/parameter_definitions/index.rst:383–428`).

### 선택한 입력과 확인할 출력

| 항목 | T 판본의 실제 입력 | 근거 |
|---|---|---|
| 격자·경계 | 96요소·63노드. x축의 안쪽/바깥쪽 반경은 60,960/152,400 m, 수심은 3.048/19.05 m. 수위 경계는 1구간 9노드로 `7,14,21,28,35,42,49,56,63` 순서 | Q `fort.14:1–9,162–173` |
| 해법·강제 선택 | `IHOT=0`, `ICS=1`, `IM=0`; `NOLIBF=NOLIFA=NOLICA=NOLICAT=1`, `CORI=0`; `NTIP=NTIF=NWS=0`, `NBFR=1` | Q `fort.15:6–16,28–34` |
| 경계 M2 | 각주파수 `0.0001405257 rad/s`, `FF=1`, `FACE=0°`; 9개 경계점 모두 `EMO=0.3048 m`, `EFA=0°`. 입력의 분조 수위와 조석 퍼텐셜 사용 여부는 별개 | Q `fort.15:31–44`; S `src/gwce.F:1638–1649` |
| 시간·ramp | `DTDP=174.656 s`, `STATIM=REFTIM=0 day`, `RNDAY=5 day`, `NRAMP=1`, `DRAMP=2 day` | Q `fort.15:17–24` |
| 시계열 출력 | 수위·속도 정점 각 3곳과 전체 노드 출력을 0–5 day, 3 time step 간격으로 요청. 코드/출력 시간축의 실제 시각은 별도 확인 대상 | Q `fort.15:46–57` |
| 조화분해·재시작 | M2 한 분조, `THAS=4`, `THAF=5 day`, `NHAINC=1`, `NHASE=NHASV=NHAGE=NHAGV=1`; `NHSTAR=5`, `NHSINC=1236` | Q `fort.15:58–64` |

`DRAMP=2 day`를 2일 뒤 강제가 정확히 1이 되는 선형 ramp로 읽지 않는다. S는 이 설정에서 `DRampElev=DRAMP`, `RampElev=tanh(2 TimeLoc/(86400 DRampElev))`를 사용한다. 경계 합성에는 이 계수가 곱해지고, `TimeH=IT*DTDP+(STATIM−REFTIM)*86400`이다(S `src/read_input.F:2908–2916`; `src/timestep.F:257–258,301–308`; `src/gwce.F:1638–1651`). 선형 주기해와 비교할 때에는 ramp와 초기 과도응답의 영향을 별도로 확인한다.

Q의 출력 선택값 `NOUTE/NOUTV/NOUTGE/NOUTGV=5`, `NHSTAR=5`는 S의 입력 코드에서 NetCDF4(HDF5) 출력 선택으로 처리된다. 문서의 일부 값 열거만 보고 미지원이라고 판단하지 않는다. 여기서 확인한 것은 입력 분기이며 실제 출력 라이브러리 실행이 아니다(S `src/read_input.F:3642–3646,3757–3761,4143–4148,4217–4222,4534–4537`).

공식 웹 설명의 hotstart 주기는 512 step이지만 선택한 T 입력은 **1236 step**이다. 웹 예제 설명을 다른 testsuite 판본의 입력값으로 그대로 복사하지 않는다([공식 설명][quarterannular-official]; Q `fort.15:63`). `fort.15:2`의 `ADCIRC V45.07`은 실행 식별 문자열이다. 아래 여섯 NetCDF control 파일의 global attribute `version`은 모두 `v56.0.1-21-gbcb79a8`, `source`는 `CircleCI`다. 이 파일 내 판본 표기는 현재 S의 코드 SHA와 구분하며, 정확한 컴파일러·빌드 옵션까지 입증하지는 않는다(근거: Q `control/{fort.61.nc,fort.62.nc,fort.63.nc,fort.64.nc,maxele.63.nc,maxvel.63.nc}`의 해당 속성).

### 자동 회귀 비교가 확인하는 범위

`test_list.yaml:423–434`에 등록된 출력은 `fort.61.nc`, `fort.62.nc`, `fort.63.nc`, `fort.64.nc`, `maxele.63.nc`, `maxvel.63.nc` **여섯 개**다. `fort.51`–`fort.54` 조화출력은 입력에서 요청하더라도 이 목록의 자동 비교 대상은 아니다. 필요한 분조 진폭·위상 검증은 별도로 설계해야 한다(Q `fort.15:58–62`; 위 YAML).

비교기는 각 등록 파일이 control과 계산 위치에 모두 존재하는지 확인하고 NetCDF를 읽어 수치 배열을 비교한다. 기준 쪽 변수 목록을 순회하므로 기준에 없는 추가 변수의 존재를 검사하는 구조는 아니다. 수치 dtype인 `f`·`i`만 비교하고 이름에 `time_of`가 들어간 변수는 건너뛴다. `numpy.testing.assert_allclose(control[var], test[var], atol=tolerance, equal_nan=True)` 호출에서 **`rtol`은 명시하지 않는다**. 따라서 CLI의 `--tolerance`를 모든 출력의 순수 절대오차나 해역의 물리 허용오차로 해석하지 않는다. 런타임 NumPy의 상대오차 기본값과 변수 단위·제외 항목을 함께 고정해야 한다. 근거: T `test_runner/adcirc_test/adcirctest.py:429–445,491–505,527–545`; `README.md:29–35`. 읽을 때 제외하는 경계 관련 변수는 `neta, nvel, nvdll, max_nvdll, ibtype, nbdv, nvell, nbvv, ibtypee, max_nvell`이며, global attribute의 동일성을 검사하는 루프는 아니다(동 코드 `19–30,491–500,527–545`).

### 실제 검증으로 이어가기 위한 조건

1. **회귀 재현**: 선택한 S/T 판본, 실행파일·빌드, Python 의존성, 입력 SHA와 control SHA를 고정하고 별도 실행 공간에서 해당 한 케이스를 실행한다. 여섯 파일의 비교 결과와 종료 상태를 보존한다. 위 README의 단일 테스트 실행 인터페이스를 사용하며 vendor 원본 디렉터리를 실행 결과로 덮어쓰지 않는다.
2. **출력/강제 확인**: 경계 노드 순서와 시각·ramp를 맞춰 M2 합성과 경계 수위 출력을 비교한다. 조화분해 진폭·위상은 요청한 분석창·분조·단위·위상 규약을 대조하고 자동 회귀 비교와 별도 결과로 기록한다. 근거: Q 입력의 위 항목들과 S `src/gwce.F:1638–1649`.
3. **해석해 검증**: 위 원문 식·조건과 동일한 선형/마찰/강제 조건을 갖춘 입력을 별도로 고정하고 주기 응답과 대조한다. 격자·시간간격 변화에 따른 오차·보존량과 판정 기준은 실행 전에 정한다. 이는 [BUILD-PLAN §4–6](../../../../BUILD-PLAN.md)에 따른 다음 검증 조건이며 수행 기록이 아니다.

현재 확보한 것은 선택한 회귀 입력과 출력 비교 계약, control 파일에 기록된 판본 표기, 선형 해석해의 원문 조건과 위 특수형이다. control의 정확한 빌드 환경, 선형 해석해와 동일 조건인 ADCIRC 입력·계산, 보존/민감도 결과, 실제 해역 관측 검증은 아직 확보하지 않았다. 이 미확인 사항을 회귀 PASS나 문서 보강 완료로 대체하지 않는다.

[quarterannular-official]: https://adcirc.org/home/documentation/example-problems/quarter-annular-harbor-with-tidal-forcing-example/
[lynch1978-polar]: https://ccht.ccee.ncsu.edu/wp-content/uploads/sites/10/2019/05/Lynch-1978-JHY.pdf

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

FES handbook p. 6의 loading atlas는 **radial component**이고, [PyFES 설정][pyfes-guide]도 `tide`와 `radial`을 분리한다. ADCIRC `fort.24`는 self-attraction/earth-load 강제 항이며 `SALTAMP/SALTPHA`를 `TIP2`에 합성한다(`docs/technical_reference/input_files/fort24.rst:1–8`; `src/timestep.F:1547–1559`). **radial 변위 파일을 단위만 바꿔 fort.24로 쓰는 변환은 이 근거로 성립하지 않는다.** 두 변수의 물리량·퍼텐셜 환산·부호·분조를 잇는 정의가 추가로 필요하다(`source-needed`). 경계 수위 EMO/EFA 준비와 별도로 다룬다.

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


## Scope

Exactly what ADCIRC's reader expects in the fort.15 NBFR boundary harmonic block (`AMIG/FF/FACE` + per-node `EMO/EFA`), how `fort.24`/`fort.24.nc` self-attraction-and-loading (SAL) is read (only when `NTIP=2`), how constituent name matching works (strict, case-sensitive trim), the units/sign/phase conventions ADCIRC applies, and what `REFTIM` does to the harmonic time base. Use this when converting external databases (NAO99jb, FES2022b, TPXO) to ADCIRC inputs, or debugging tide phase/amplitude validation errors.

**Key fact**: ADCIRC has **no built-in parser** for FES/NAO/TPXO databases. It only consumes preprocessed `fort.15` harmonic block and optional `fort.24` SAL.

## Source basis

- `read_input.F:1719-1745, 3344-3497, 6282-6463` — `NTIP`, NBFR boundary block, SAL reader.
- `gwce.F:1638-1650` — boundary elevation synthesis.
- `timestep.F:251-258, 1517-1562` — `TimeH` and tidal-potential application.
- `hstart.F:1530-1537` — SAL into TIP2.

## A. fort.15 NBFR boundary harmonic block

```
NBFR
do j = 1, NBFR
   BOUNTAG(j)                      ! constituent tag string
   AMIG(j)  FF(j)  FACE(j)         ! frequency, nodal factor, equilibrium argument (deg)
end do
do j = 1, NBFR
   ELEVALPHA(j)                    ! constituent tag (printed only, no validation)
   do i = 1, NETA
      EMO(j,i)  EFA(j,i)           ! constituent j, boundary node i; amplitude (m), phase lag (deg)
   end do
end do
```

References (`read_input.F`):
- `NBFR` read + arrays allocated: `read_input.F:3438-3446`.
- Per-constituent header `BOUNTAG, AMIG, FF, FACE`: `:3445-3450`.
- `FACE` deg → rad after read: `:3450`.
- Per-constituent boundary block `ELEVALPHA + EMO/EFA`: `:3464-3469`.
- `EFA` deg → rad after logging: `read_input.F:3521-3525`.

Important: `ELEVALPHA` is **only printed** as "verification"; **no match/validation against `BOUNTAG`** (`:3499-3504`). You must keep the per-constituent ordering consistent yourself.

경계 노드 순서는 전체 격자 번호의 정렬 순서가 아니다. `src/mesh.F:1822–1834`는 `K=1..NOPE`, 각 구간의 `I=1..NVDLL(K)` 순서로 `NBDV(K,I)`를 `NBD`에 이어 붙인다. 분조별 `EMO/EFA` 행은 이 순서에 맞아야 하며 `src/read_input.F:3507–3510`의 노드·진폭·위상 출력과 대조할 수 있다. 공식 [fort.15 구조](https://adcirc.github.io/adcirc/technical_reference/input_files/fort15.html)도 분조를 첫 첨자로 표기한다. 이 절의 도식은 전체 입력 파일 예제가 아니다.

## B. fort.24 SAL reader

Called from main startup (`adcirc.F:292-293`); reader at `read_input.F:6320-6501`.

**Active only for `NTIP=2`**:
- `NTIP < 2`: SAL arrays zeroed (`:6498-6500`).
- `NTIP=0`: tidal potential entirely off.
- `NTIP=1`: tidal potential active, no SAL.
- `NTIP=2`: tidal potential + SAL.

NetCDF preferred if `fort.24.nc` exists (`:6368-6382`).

### NetCDF format

Required dims/vars (`:6391-6403`):
- Dimensions: `node`, `num_constituents`, `char_len`.
- Variables: `constituents`, `frequency`, `sal_amplitude`, `sal_phase`.

Constituent count must equal `NTIF` (`:6405-6409`).

### ASCII format (`fort.24`)

Per-constituent block (`:6467-6493`):
```
<dummy_char>  <dummy_char>          ! 2 dummy chars
<dummy_real>                        ! ignored
<dummy_int>                         ! ignored
<const_name>                        ! e.g. "M2"
do i = 1, num_nodes
   JJ  SALTAMP(JJ)  SALTPHA(JJ)
end do
```

`SALTPHA` deg → rad after read.

## C. Constituent matching

`fort.15` tidal-potential tags are **`TIPOTAG`** (different from `BOUNTAG`!) (`:3361-3363`).

- NetCDF SAL: `TRIM(TIPOTAG(I)) == TRIM(const_name)` (`:6416-6423`).
- ASCII SAL: each SAL `const_name` matched to some `TIPOTAG(J)` (`:6474-6481`).

**Strict, case-sensitive**, no aliasing.

## D. Phase / sign / units

| Quantity | Input units | Internal (post-read) | Sign |
|---|---|---|---|
| `FACE`, `FACET` (eq. arg.) | degrees | radians | added to argument |
| `EFA` (boundary phase lag) | degrees | radians | **subtracted** in `cos(arg − EFA)` |
| `SALTPHA` (SAL phase) | degrees | radians | **subtracted** in `cos(arg − SALTPHA)` |
| `EMO`, `SALTAMP` | meters | (no conversion) | direct multiplier |

Boundary synthesis (`gwce.F:1644-1649`):
```
Eta2(NBDI) += EMO * FF * RampElev * cos(AMIG*timeh + FACE − EFA)
```

SAL synthesis into `TIP2` (`timestep.F:1551-1552`, `hstart.F:1530-1537`):
```
TIP2 += SALTMUL * SALTAMP * cos(ARGT − SALTPHA)
```

ADCIRC uses **lag-subtracted** phase (`cos(arg − phase)`; `src/gwce.F:1642–1649`). FES/PyFES와 이번 NAO 패키지에서 확인한 lag 합성은 [제품별 근거](#external-data-conventions)에 정리했다. 부호가 같아도 epoch·단위·천문식·노달보정까지 같다는 뜻은 아니다. TPXO의 특정 배포 형식은 아직 대조하지 않았다.

## E. FF and FACE meaning

- `FF` (boundary): nodal factor (multiplies amplitude at runtime).
- `FFT` (tidal potential): same role for potential and SAL.
- `FACE` (boundary): equilibrium argument `(V₀ + u)` (added to argument).
- `FACET` (tidal potential): same role for potential.

FES의 천문 인수·노달보정 의미는 [PyFES nodal 식][pyfes-nodal]을 참조한다. 실제 FF/FACE 생성에서는 제품과 예측기의 판본·분조·epoch·보정 포함 여부를 맞춘다. T_TIDE/UTIDE/pyTMD의 출력을 동일한 ADCIRC 입력으로 사용할 수 있다는 일괄 호환 주장은 여기서 확정하지 않는다.

## F. REFTIM and TimeH

`REFTIM` is the harmonic reference time in **days** (`:2541`).

```
TimeH = IT * DTDP + (StaTim − RefTim) * 86400
```
(`timestep.F:251-258`).

`STATIM`과 `REFTIM`은 일(day) 단위로 읽히며(`src/read_input.F:2548–2557`), 내부 `TimeH`는 초다(`src/timestep.F:257–258`). 합성은 `AMIG(J)*(TimeH−NCYC*PER(J))+FACE(J)−EFA(J,I)`이며 `EFA`는 입력의 도(degree)에서 radian으로 변환한다(`src/read_input.F:3450-3450,3493–3496`; `src/gwce.F:1642–1649`). 실제 입력을 준비할 때 원자료의 기준시각·위상 규약·단위와 이 정의를 대조해야 한다. 이 코드 확인은 외부 DB의 규약이나 실제 변환 자료의 품질을 검증한 것이 아니다.

Harmonic synthesis uses `timeh`, **not** raw model time (`gwce.F:1642-1644`, `timestep.F:1536-1539`).

`STATIM/REFTIM`은 이 코드에서 수치적인 일(day) 값이다. 시각대/달력 epoch를 자동으로 부여한다고 가정하지 않는다. 외부에서 구한 FACE/FACET의 기준시각과 같은 실제 시각을 나타내도록 연결한다(`src/timestep.F:257–258`; `src/gwce.F:1642–1649`).

## G. 외부 atlas에서 fort.15로

1. [제품별 정의와 변환 대조](#external-data-conventions)를 따라 ocean/geocentric/radial 성분, 판본, 분조, 단위, 유효 영역을 고정한다.
2. 실제 시작시각과 STATIM/REFTIM을 대응시키고 분조별 AMIG(rad/s), FF, FACE(deg)의 epoch·천문/노달보정을 기록한다. 전체 공급기관 예측과 NBFR 일부 분조의 비교는 성분부터 맞춘다.
3. 경계 노드마다 동일 자료에서 추출한 진폭·lag를 EMO(m), EFA(deg)로 변환한다. 결측/외삽·보간 처리와 원자료 대응을 보존한다.
4. §A의 NBFR 레코드와 분조/노드 순서대로 작성하고 fort.16 echo 및 같은 성분의 재합성에 대조한다(`src/read_input.F:3445–3470,3485–3497`; `src/gwce.F:1638–1649`).

이 절차의 실제 변환 실행은 미수행이다. SAL은 위 [loading tide 구분](#external-data-conventions)의 별도 물리량 정의를 확보한 뒤 준비한다.

## H. Validation pitfalls

- **Epoch·시각대**: FACE/FACET의 기준과 TimeH의 기준을 대조한다. 오차를 임의의 90°/180° 증상으로 단정하지 않는다(§D/F 합성식).
- **Lead/lag**: 부호를 뒤집은 오차는 원래 위상에 의존한다. 순환 위상 차이와 복소 오차를 함께 본다([지표 정의](#independent-observation-and-errors)).
- **단위·결측**: cm 값을 m로 쓰면 진폭이 100배가 된다. 결측 sentinel에 단위 변환/보간을 적용하기 전에 제외한다([제품별 정의](#external-data-conventions)).
- **분조/노드 순서**: NBFR의 ELEVALPHA는 echo되지만 BOUNTAG와 대조되지 않는다. SAL의 TIPOTAG 매칭과 혼동하지 않는다(§A/C; `src/read_input.F:3499–3511`).
- **노달보정**: 이 NBFR 경로는 입력 FF/FACE를 합성에 사용한다. 시간에 따라 변하는 공급기관 예측과의 차이를 대상 기간에서 평가한다. 고정 1개월/분기별 갱신을 공통 정확도 기준으로 사용하지 않는다(`src/gwce.F:1642–1649`; [PyFES nodal 정의][pyfes-nodal]).
- **관측/atlas 혼동**: 원 DB와의 재합성 일치, 동화/보정에 사용한 관측 일치, 독립 관측 검증을 구분한다([독립성 기준](#independent-observation-and-errors)).

## Decision Guide

| Need | Setup |
|---|---|
| 주기 수위 경계 | NBFR와 EMO/EFA를 준비한다. NTIP/NTIF 퍼텐셜 선택은 별도다. 위 회귀 예제는 NTIP=0, NTIF=0, NBFR=1이다. |
| 퍼텐셜/SAL도 포함 | NTIP의 0/1/2 정의와 §A/F·forcing 노트를 대조한다. SAL 사용에는 성분·물리량·분조·파일의 추가 근거가 필요하며, 모든 해역에 일괄 권고하지 않는다. |
| FES2022b / NAO99Jb / TPXO | [제품별 정의](#external-data-conventions)에 따라 변환한다. 제품명·격자 간격·포함 분조 수만으로 특정 해역의 정확도 순위를 정하지 않는다. |
| 관측과 비교 | [독립성·분석창·지표](#independent-observation-and-errors)를 고정한다. 해역·목적별 허용치는 미선정이다. |
| 긴 실행 기간 | 고정 FF/FACE 합성과 선택한 공급기관 예측의 기간 내 차이를 확인한다. 보정 변경/재시작 방법과 허용오차는 별도 검증 대상이다. |
| Disable tidal potential and periodic elevation forcing | `NTIP=0`; keep the required `NBFR=0` line. Any non-periodic elevation boundary data are a separate input (`src/read_input.F:1719–1745,3410–3444`; [official NBFR definition](https://adcirc.github.io/adcirc/technical_reference/parameter_definitions/index.html)). |

## Working Rules

- Always write `STATIM`, `REFTIM`, and the FF/FACE epoch in the run README. These three must align.
- Use 8-character constituent names ("M2      ", "S2      ", etc.) padded; ADCIRC trims, but consistent is safer.
- Output `fort.51` harmonic analysis at validation stations to compute model-side amplitude/phase, then compare against gauge harmonic constants — this is far more diagnostic than time-series RMSE.
- 지역별 DB 선택은 해당 정점/기간의 독립 관측 대조로 판단한다. NAO99Jb도 N2/K2/P1을 포함하므로 이 분조들의 존재만으로 FES의 추가 정확도를 주장하지 않는다([NAO README §2][nao-readme]).
- 기존 SAL의 일괄 5–10% 진폭 감소 권고는 `source-needed`다. 해당 조건·정량 근거를 확인하기 전 특정 과대예측의 원인 판정에 사용하지 않는다.

## Common Pitfalls

(See "H. Validation pitfalls" above — most issues come from epoch and phase convention.)

Additional:
- ▢ Hot-start across `NTIP` change — harmonic accumulators / SAL arrays inconsistent.
- ▢ Modifying NBFR block but not regenerating SAL constituent set — names mismatch silently.
- ▢ Nesting (boundary forcing from coarse-grid output) — coarse `EMO/EFA` may not be exact at fine boundary nodes; interpolate carefully.

## Next expansion

- 판본·천문/노달보정이 명시된 FF/FACE 생성 및 공급기관 예측과의 대조.
- FES2022b → fort.15 conversion script.
- SAL 입력과 외부 제품의 물리량/퍼텐셜 정의 연결. FES radial loading의 직접 이전은 미입증.
- Validation harmonic analysis (`fort.51`) post-processing.

## References

- Westerink et al. 1992 (ADCIRC tide formulation).
- Hendershott 1972 (SAL theory).
- T_TIDE: Pawlowicz et al. 2002.
- UTIDE: Codiga 2011.
- FES2022b: [CNES dataset DOI](https://doi.org/10.24400/527896/A01-2024.004), [handbook Issue 2.0][fes-hdbk]. 이 handbook p. 1의 FES2022 논문은 in preparation으로 기재돼 있어, 기존의 불명확한 “Lyard et al. 2024” 출판 인용을 대체한다.
- 외부 자료·검증 지표 출처는 해당 절의 제품 문서, NAO 입력/합성 코드, UHSLC와 Wang et al. (2022)에 명시했다.
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/adcirc/source_code/adcirc/src`. Auto-draft = false; review_required = true.
