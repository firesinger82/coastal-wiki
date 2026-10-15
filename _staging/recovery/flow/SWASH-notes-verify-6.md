# SWASH 노트 변경 줄 전수 대조 6

대조일은 2026-10-15이다.
대상은 `swash-output.md`, `swash-implicit-depthavg-flow.md`, `swash-explicit-layered-flow.md`, `swash-unstructured-solvers.md`이다.
기존 노트의 최초 대상 줄은 작업 시작 시 `git diff -U0 HEAD -- <노트>`의 모든 추가 줄이다.
새 노트의 대상 줄은 전체 줄이다.
삭제 줄은 최종 보고서의 수정 근거와 별도로 대조한다.
최종 대조 수는 정정 후 같은 diff의 + 줄 수이다. frontmatter와 빈 줄을 포함한다.
시작 시 대상 수와 잔존 문장 정리로 늘어난 수는 마지막 집계에서 구별한다.
정정 수와 보완 수는 이 작업에서 수정한 대상 노트의 줄 수이다.
완료한 노트의 기록은 아래에 순서대로 덧붙인다.

## 1. swash-output.md — 완료

작업 시작 시 추가·수정 111줄을 대조했다.
대상 범위는 `7–8, 63–65, 141–142, 147–155, 183–185, 252–343`이다.
삭제 6줄은 이전 `7, 137–138, 143, 171, 238`행이다.
삭제 근거는 반영 기록 3의 frontmatter 갱신과 outputs §4의 SO1-289–293이다.
사용자 지시 6에 따라 기존 233행의 미확인 문장도 사실 문장으로 고쳤다.
이 잔존 문장 점검은 시작 시 대상 111줄과 별도로 기록한다.
정정은 2줄이다.
보완은 2줄이다.

차이 표 74행의 분류와 결론을 각 보고서 최종 §5 및 callflow §8과 대조했다.
E 후보의 강도는 최종 보고서와 같다.
SO1-293의 커밋과 날짜는 AD 판정과 같다.
개별 `ovkeyw(ivtype)` 대입은 `5d279d7`에서 94개이다.
같은 대입은 `9b8a012`과 현재 파일에서 각각 96개이다.
초기 채움 `XXXX`는 이 수에 포함하지 않았다.
HSIG의 제곱합·분모·최종화 조건은 `SwashAverOutp.ftn90:89–121`과 일치한다.
현재 코드와 과거 커밋의 인용 범위를 열어 대조했다.
swashuse PDF p.20·101–109·113–122·145–146·162–163의 관련 정의를 대조했다.
숫자·단위·식은 p.109·114–119·121·145의 쪽 이미지에서 확인했다.
frontmatter의 소스 범위와 날짜는 반영 기록 및 해당 원문과 대응한다.
상대 링크의 대상 파일은 모두 존재한다.
절대 경로와 이중 대괄호는 없다.
Mermaid 블록은 없다.

| 위치 | 종류 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| `models/SWASH/source-analysis/swash-output.md:233` | 정정 | 모든 allocatable 배열의 해제 여부는 확인되지 않았다. | 열거된 배열의 조건부 해제와 연결 목록의 delete 호출을 서술했다. | `src/SwashCleanMem.ftn90:62–128,540–561`; 해당 파일 판독 기록; callflow의 SwashCleanMem 직접 호출 표 |
| `models/SWASH/source-analysis/swash-output.md:274` | 보완 | 현재 출력 조건만 인용했다. | 최초 공개판의 같은 조건과 최종 보고서의 이력 결론을 보탰다. | `8756667:src/SwashDecOutQ.ftn90:129`; inputs-setup §5 SI1-054; AD SI1-054 |
| `models/SWASH/source-analysis/swash-output.md:283` | 보완 | 과거 WATL 564행 뒤에 VKSI를 줄 번호 없이 이어 적었다. | VKSI에 `8756667:src/SwashInit.ftn90:612`를 보탰다. | `8756667:src/SwashInit.ftn90:564,612`; outputs §5 SO1-061 |
| `models/SWASH/source-analysis/swash-output.md:342` | 정정 | 대조 전 노트의 미배정·범위 밖 문장을 그대로 재인용했다. | 당시 분류를 과거 사실로 서술했다. 본문 §6의 직접 매핑 인용을 명시했다. | outputs §4 SO1-292; `src/SwashInit.ftn90:809–812` |

기계 확인 후보 판정은 다음과 같다.

| 후보 | 판정 |
|---|---|
| `8756667:src/SwashInit.ftn90:1629` `outpar(1) = 0.` | 오탐이다. 지정 커밋 1629행과 일치한다. |
| `8756667:src/SwashInit.ftn90:564` `ovkeyw(ivtype) = 'WATL'` | 후보 자체는 오탐이다. 지정 커밋 564행과 일치한다. 같은 행의 별도 VKSI 인용에는 612행을 보탰다. |
| `8756667:src/SwashReadInput.ftn90:319` `call ININTG ('NDEC', dec_block, 'STA', 6)` | 오탐이다. 지정 커밋 319행과 일치한다. |
| `8756667:src/SwashReadInput.ftn90:321` `call ININTG ('LEN', nlen, 'STA', 200)` | 오탐이다. 지정 커밋 321행과 일치한다. |
| `8756667:src/SwashInit.ftn90:639` `ovunit(ivtype) = uf` | 오탐이다. 지정 커밋 639행과 일치한다. |
| `8756667:src/SwashInit.ftn90:1315` `ovunit(ivtype) = uf` | 오탐이다. 지정 커밋 1315행과 일치한다. |
| `8756667:src/SwashAverOutp.ftn90:94` `etavar = etavar + s1*s1` | 오탐이다. 지정 커밋 94행과 일치한다. |
| `8756667:src/SwashAverOutp.ftn90:98` `nwavoutp > 1.` | 오탐이다. 지정 커밋 98행의 전체 if 조건에 있는 부분 문자열이다. |
| `5d279d7:src/SwashInit.ftn90:1468` `ovkeyw(ivtype) = 'MSEDK'` | 오탐이다. 지정 커밋 1468행과 일치한다. |
| `5d279d7:src/SwashInit.ftn90:1481` `ivtype = 101` | 오탐이다. 지정 커밋 1481행과 일치한다. |
| `9b8a012:src/SwashInit.ftn90:1481` `ivtype = 95` | 오탐이다. 지정 커밋 1481행과 일치한다. |
| `9b8a012:src/SwashInit.ftn90:1482` `ovkeyw(ivtype) = 'DIVU'` | 오탐이다. 지정 커밋 1482행과 일치한다. |
| `9b8a012:src/SwashInit.ftn90:1493` `ivtype = 96` | 오탐이다. 지정 커밋 1493행과 일치한다. |
| `9b8a012:src/SwashInit.ftn90:1494` `ovkeyw(ivtype) = 'DIVQ'` | 오탐이다. 지정 커밋 1494행과 일치한다. |

이 노트의 미해결 항목은 없다.

## 2. swash-implicit-depthavg-flow.md — 완료

대조 대상은 시작 시점의 + 줄 57개이다. 삭제 줄 7개도 대조했다. 정정은 5줄이다. 보완은 2줄이다. 사용자 지시 6에 따라 기존 256·258행의 미완 설명도 점검했다. 이 두 행의 수정은 정정 수에 포함했다.

- 대상 범위: `7–8,29,141–144,146–148,155–158,166–170,211,222–224,254,257,259–290`.
- frontmatter의 파일·헤더·theta·행렬 조립·solver 호출 인용을 현재 소스와 대조했다.
- 차이 표 21행의 분류와 결론을 theory-framework·theory-unstructured 보고서의 §5와 마지막 전수 검증 기록에 대조했다. ST1-333은 E 중간이다. ST2-365는 E 강함이다. A 행은 없다.
- swashtech PDF p.21·24–25·45·56–57·59·94·98의 식과 조건은 쪽 이미지로 대조했다. p.97·111은 쪽별 판독 기록으로 대조했다. swashuse PDF p.99–100은 쪽 이미지로 대조했다. p.140의 모든 유속이 유출 방향인 조건은 판독 기록으로 대조했다.
- ST1-333의 초기판·11.01·문서 시점 진단식은 E2의 ST1-310 판정과 대조했다. ST2-365의 `835452f` 도입 대입은 과거 소스와 대조했다. 두 항목의 호출 조건과 현재 대입도 열어 확인했다.
- 삭제 구7행은 검증 날짜를 덧붙인 교체이다. 구28행의 보존 범위 변경은 ST1-323에 근거한다. 구140·142행의 부호만으로 내린 결론 제거는 ST1-322에 근거한다. 구196행의 “bottom friction만” 제거는 `wndimp(iface)`를 포함하는 현재 1041행에 근거한다. 구236행의 미확인 제목 제거는 사용자 지시 6에 따른다. 구239행의 다층 후속 요구를 남기라는 보고서 근거는 없다. 해당 미완 항목 제거는 사용자 지시 6에 부합한다. 다층 소스 헤더 `src/SwashImpLayUflow.ftn90:50–51`도 이류의 Euler explicit 처리를 명시한다.
- 상대 링크 5개가 실제 파일을 가리킨다. 절대 경로와 이중 대괄호는 없다. Mermaid 블록은 없다.

### 정정·보완 목록

행 번호는 수정 후 노트 기준이다.

| 노트:줄 | 종류 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `swash-implicit-depthavg-flow.md:141` | 정정 | 축약한 contrib 식을 490–493행으로 인용 → 완전한 식과 482–484행으로 교체. | `src/SwashImpDepM1DHflow.ftn90:482–484`는 이류·점성을 제외한다는 주석과 `contrib = zgrad + pgrad(nm) + qgrad(nm) - windu(nm)/max(1.e-3,hum(nm))`이다. |
| `swash-implicit-depthavg-flow.md:142` | 정정 | 균일 1D 조건만 제시 → 양의 수심을 가진 젖은 내부 면 조건을 명시. | 같은 소스 456행 `if ( humn(nm) > 0. ) then`, 468행 `if ( wetu(nm) == 1 ) then`, 458–459·490–492행. ST1-056·322. |
| `swash-implicit-depthavg-flow.md:155` | 보완 | 명시적 경로의 체적 진단만 인용 → 해당 M1DH 경로의 자유수면 점 진단 인용 추가. | `src/SwashImpDepM1DHflow.ftn90:1261` `if ( presp(nm) == 0 ) vol = vol + s1(nm)`. |
| `swash-implicit-depthavg-flow.md:168` | 보완 | 외력을 끈 부분계 → 식 (2.23)의 외력·점성·마찰 제외 조건과 원문 인용 명시. | swashtech PDF p.57 식 (2.23). `src/SwashImpDepM1DHflow.ftn90:476–486,508`. ST1-229·323. |
| `swash-implicit-depthavg-flow.md:211` | 정정 | 배열 인덱스를 생략한 분모와 중복 설명 → 실제 분모 식과 이류·점성의 이전 시각 계산 근거. | `src/SwashImpDepUflow.ftn90:306` `call perot ( u0, 1, 1 )`; 474–490·760–768·1039–1045행. |
| `swash-implicit-depthavg-flow.md:256` | 정정 | 별도 solver 노트 후보·호출부만 인용 → 이미 있는 구조·비구조 solver 노트와 구현 위치. | `src/SwashSolvers.ftn90:1811,4297,5283,5491`; `src/SwashUServ.ftn90:299,1211,2324`. |
| `swash-implicit-depthavg-flow.md:258` | 정정 | cross-advection 검증을 미완으로 남긴 설명 → 두 실제 계수와 부호만으로 전체 반대칭을 뜻하지 않는다는 설명. | `src/SwashImpDepM2DHflow.ftn90:607–608,657–658`; ST1-322. |

### 기계 확인 후보 판정

| 후보 | 판정 |
|---|---|
| `source-analysis/swash-implicit-depthavg-flow.md:140` `의 반대부호 = skew-symmetric 이산 연산자 구현.` | 오탐이다. ST1-322가 인용한 수정 전 노트 구140행이다. 시작 diff의 삭제 줄과 일치한다. 현재 본문은 가중 관계와 적용 조건으로 고쳤다. |
| `source-analysis/swash-implicit-depthavg-flow.md:142` `양쪽 부호 동일` | 오탐이다. ST1-322가 인용한 수정 전 노트 구142행이다. 시작 diff의 삭제 줄과 일치한다. 현재 146–148행은 점성의 가중 자기수반 관계를 설명한다. |
| `source-analysis/swash-implicit-depthavg-flow.md:154` `헤더 Method는 M-1DH와 동일(strictly conservative, CN, skew-symmetric central, theta=0.` | 오탐이다. ST1-323의 과거 노트 인용이다. 해당 문장은 현재 164행에 있다. 두 M 경로의 헤더 42–68행과 시간 분할의 제한을 대조했다. |
| `source-analysis/swash-implicit-depthavg-flow.md:147` `mass flux/에너지 진단` | 오탐이다. ST1-333의 과거 노트 인용이다. 해당 문장은 현재 153행에 있다. `src/SwashImpDepM1DHflow.ftn90:1194–1268`의 플럭스·진단과 대조했다. 체적 진단의 한정은 현재 155–157행에 있다. |

이 노트의 미해결 항목은 없다.

## 3. swash-explicit-layered-flow.md — 완료

대조 대상은 시작 시점의 + 줄 44개이다. 삭제 줄 5개도 대조했다. 정정은 7줄이다. 보완은 3줄이다. 사용자 지시 6에 따라 기존 132·198·199·203행의 미완 설명도 점검했다. 이 네 행의 수정은 정정 수에 포함했다.

- 대상 범위: `7–8,98–100,135–137,163–164,200–202,204–234`.
- frontmatter의 세 유동 파일과 모듈 정의를 열어 인용 범위를 대조했다. 본문의 압력 경계·축소 압력계·상대 연직속도·연직 압력경사 설명을 현재 소스와 대조했다.
- 차이 표 21행의 분류와 결론은 네 근거 보고서의 최종본과 일치한다. A·E 행은 없다. ST1-334·ST2-428·ST2-429의 B 판정은 AD §3 및 `8756667` 소스의 동일 식으로 확인했다.
- 표의 문서 원문 칸에서 보고서에도 있던 문서명 오기 2건을 고쳤다. ST2-385의 바닥 마찰 설명은 swashuse PDF p.76–78이다. ST2-387의 연직 음해 적분 설명은 swashuse PDF p.100–101이다. swashtech의 같은 쪽은 각각 보간·이류·벡터 재구성과 분산 관계·푸리에 해석을 다룬다. 이 정정은 두 행의 C 분류와 결론을 바꾸지 않는다.
- swashuse PDF p.40·90·93·101·136–137과 swashtech PDF p.63–64의 층 방향·정의·식·숫자는 쪽 이미지로 대조했다. 그 밖의 해당 명령과 빈 장 설명은 쪽별 판독 기록으로 대조했다. swashuse PDF p.116의 출력 정의는 출력 노트에서 확인한 이미지와도 대조했다.
- 삭제 구7행은 검증 날짜를 덧붙인 교체이다. 구97행의 bottom-face 제거 설명은 ST1-334에 따라 고쳤다. 구132행의 위층 축소 설명은 ST2-429에 따라 고쳤다. 구158행의 표면→바닥 복원 설명은 ST2-428에 따라 고쳤다. 구194행의 gmatw 미전사 설명은 ST2-392의 실제 조립식으로 대체했다.
- 상대 링크 9개가 실제 파일을 가리킨다. 절대 경로와 이중 대괄호는 없다. Mermaid 블록은 없다.

### 정정·보완 목록

행 번호는 수정 후 노트 기준이다.

| 노트:줄 | 종류 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `swash-explicit-layered-flow.md:98` | 정정 | 좌우 경계 계수를 합친 뒤 제거 → 남길 계수에서 제거할 계수를 뺀 뒤 제거. | `src/SwashExpLay1DHflow.ftn90:552–555,561–564`는 각각 계수 차와 영 대입이다. |
| `swash-explicit-layered-flow.md:132` | 정정 | solver 상세 source-needed → 실제 BiCGSTAB·전처리 선택 조건과 선형 솔버 노트 링크. | `src/SwashExpLay1DHflow.ftn90:2409–2447`의 `qmax == 1` 분기, `lprecon` 검사, 세 전처리 호출. |
| `swash-explicit-layered-flow.md:198` | 정정 | 미확인 / source-needed 제목 → 관련 구현 제목. | 사용자 지시 6. 아래 항목의 소스와 기존 선형 솔버 노트가 모두 있다. |
| `swash-explicit-layered-flow.md:199` | 정정 | solver 내부는 별도 노트 참조 필요 → 다섯 구현의 정의 위치와 실제 노트 링크. | `src/SwashSolvers.ftn90:3312,4297,3050,2694,2258`. |
| `swash-explicit-layered-flow.md:203` | 정정 | P2DH는 동일 메커닉으로 간주·미전사 → 2DH subgrid 목적과 u/v 압력경사 배열. | `src/SwashExpLayP2DHflow.ftn90:56–57,92–95,928,944–947,3488–3491`. 해당 파일의 이번 판독 기록도 존재한다. |
| `swash-explicit-layered-flow.md:222` | 정정 | ST2-385 문서명 swashtech p.76–78 → swashuse p.76–78. | swashuse 판독 기록 p.76의 FRICTION 시작, p.77의 LOGLAW, p.78의 FRICTION 끝. swashtech p.76–78은 이류·보간·재구성이다. |
| `swash-explicit-layered-flow.md:223` | 정정 | ST2-387 문서명 swashtech p.100–101 → swashuse p.100–101. | swashuse p.100의 연직 이류·점성 theta 적분과 p.101의 VERTICAL 정의. swashtech p.100–101은 분산 관계와 푸리에 해석이다. |
| `swash-explicit-layered-flow.md:226` | 보완 | ST2-390의 Keller-box 계면 배치에 p.90만 인용 → 기법 설명 p.90과 배치 설명 p.136–137을 구별. | swashuse p.136 §5.4.3 및 p.137 Figure 5.2(b). |
| `swash-explicit-layered-flow.md:227` | 보완 | ST2-391의 STANDARD 셀 중심 배치에 p.90만 인용 → 중앙차분 설명 p.90과 배치 설명 p.136–137을 구별. | swashuse p.136 §5.4.3 및 p.137 Figure 5.2(a). |
| `swash-explicit-layered-flow.md:228` | 보완 | ST2-392의 두 압력 배치에 p.90만 인용 → 압력경사 이산화 p.90과 압력 배치 p.136–137을 구별. | swashuse p.90의 두 방법과 p.136–137의 배치 정의·그림. |

### 기계 확인 후보 판정

| 후보 | 판정 |
|---|---|
| `SwashExpLayP1DHflow.ftn90:88` `ihydro==3` | 오탐이다. 노트 33행의 88–91행 인용은 subgrid 방법의 영문 설명이다. `ihydro==3`은 다음 35행의 별도 문장이다. 실제 조건문은 해당 소스 611행에 있다. |
| `source-analysis/swash-explicit-layered-flow.md:97` `표층` | 오탐이다. ST1-334가 인용한 수정 전 노트 구97행이다. 시작 diff의 삭제 줄과 일치한다. 현재 99–100행은 위쪽 계면의 계수 1·3을 제거하는 정확한 방향이다. |

이 노트의 미해결 항목은 없다.

## 4. swash-unstructured-solvers.md — 완료

대조 대상은 시작 시점의 + 줄 29개이다. 삭제 줄 13개도 대조했다. 정정은 1줄이다. 보완은 3줄이다. 사용자 지시 6에 따라 기존 90행의 uncited-attributable 표기도 문헌 근거로 바꿨다. 이 행의 수정은 보완 수에 포함했다.

- 대상 범위: `6–7,21,37,45–48,75,81–82,87–89,91–105`.
- frontmatter의 SwashUServ.ftn90 길이는 2823줄로 확인했다. Perot 재구성식과 네 문헌의 주석 인용을 해당 소스에서 확인했다.
- 차이 표 4행의 분류와 결론은 theory-unstructured 최종본과 일치한다. A·E 행은 없다. ST2-399는 AD의 후속 변경 무관 목록과 일치한다.
- swashtech PDF p.79의 식 (5.24)·(5.25)를 이미지로 대조했다. 면 방향 부호를 위치 벡터에 곱한 식이 두 표현을 연결한다. p.124 참고문헌 [72]의 저자·제목·권·쪽·연도를 이미지로 대조했다. p.111·115–116의 해당 내용은 판독 기록으로 대조했다.
- swashuse PDF p.91–93·99–101의 해법·옵션·기본값은 앞 노트에서 읽은 기록과 이미지로 대조했다. 내부 PCG의 별도 카드 근거를 표에 보탰다.
- `src/`의 파일 내용에서 식별자 경계가 있는 `uvc`를 검색하면 16개 파일이다. 선언·할당·사용을 포함한 수이다. 대상 파일은 SwashCheckPrep, SwashCleanMem, SwashCompUFlow, SwashElemOutp, SwashExpDepUflow, SwashExpLayUflow, SwashFlowdata, SwashImpDepUflow, SwashImpLayUflow, SwashQuanOutp, SwashUBotFrict, SwashUHorzVisc, SwashUKepsMod, SwashULogLaw, SwashUServ, SwashUWindStress의 각 .ftn90 파일이다. `SwashU*.ftn90`는 21개이다.
- 삭제 구6·20·36·80·81행의 미검수·미커버 설명 제거는 사용자 지시 6과 반영 기록 2의 현재 범위 서술에 부합한다. 구43–46행의 축약 수식은 ST2-052 수정안에 따라 148·149·157행의 실제 대입문으로 바뀌었다. 구74·86–88행은 이중 대괄호 링크를 실제 상대 링크로 교체한 것이다. 구74행에서 이어진 과도한 폐합 동일시도 이번 75행 정정으로 제거했다.
- 상대 링크 8개가 실제 파일을 가리킨다. 절대 경로와 이중 대괄호는 없다. Mermaid 블록은 없다.

### 정정·보완 목록

행 번호는 수정 후 노트 기준이다.

| 노트:줄 | 종류 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `swash-unstructured-solvers.md:75` | 정정 | 두 인용을 동일 wet/dry·porosity 폐합으로 묶음 → 각 구현이 인용하는 두 문헌을 별도로 명시. | `src/SwashSolvers.ftn90:5322–5334,5530–5542`는 max/min 및 nested Newton이다. `src/SwashUServ.ftn90:2363–2381`는 Heaviside 기반 Newton이다. 두 서지는 각각의 헤더에 있다. |
| `swash-unstructured-solvers.md:82` | 보완 | Perot 2000을 uncited-attributable로 표시 → 기술매뉴얼의 실제 서지와 재구성식 인용 추가. | `src/SwashUServ.ftn90:56,148–157`; swashtech PDF p.124 참고문헌 [72]. 16개 파일 수는 위의 소스 검색과 일치한다. |
| `swash-unstructured-solvers.md:90` | 보완 | Perot 2000을 uncited-attributable로 반복 → 소스 주석 네 문헌의 위치와 기술매뉴얼 서지 위치 명시. | `src/SwashUServ.ftn90:1260–1262,364–366,1143,2379–2381`; swashtech PDF p.124 [72]. |
| `swash-unstructured-solvers.md:105` | 보완 | Newton 카드만 직접 인용 → 내부 PCG의 `pnums(21)`·`pnums(24)` 인용 추가. | `src/SwashUServ.ftn90:762–763` `reps  = dble(pnums(21))`, `maxit = nint(pnums(24))`. 압력 BiCGSTAB는 1321–1323행에서 22·23·25 카드를 읽는다. |

### 기계 확인 후보 판정

이 노트에 배정된 기계 확인 후보는 없다.

이 노트의 미해결 항목은 없다.

## 최종 집계

| 노트 | 시작 + 줄 | 최종 + 줄 | 시작 삭제 줄 | 최종 삭제 줄 | 정정 | 보완 |
|---|---:|---:|---:|---:|---:|---:|
| swash-output.md | 111 | 112 | 6 | 7 | 2 | 2 |
| swash-implicit-depthavg-flow.md | 57 | 60 | 7 | 10 | 5 | 2 |
| swash-explicit-layered-flow.md | 44 | 48 | 5 | 9 | 7 | 3 |
| swash-unstructured-solvers.md | 29 | 30 | 13 | 14 | 1 | 3 |
| 합계 | 241 | 250 | 31 | 40 | 15 | 10 |

시작 대상 241줄은 모두 대조했다. 사용자 지시 6으로 정리한 기존 문장은 8줄이다. 이 8줄의 전후와 근거는 각 노트의 목록에 있다. 수심평균 노트의 255행 빈 줄도 최종 diff의 + 줄로 새로 포함되었다. 이 빈 줄은 본문 교체 전후에 내용이 같다. 최종 + 줄 250개가 모두 대조 범위에 들어간다.

최초 삭제 31줄의 근거는 각 노트 절에 기록했다. 최종 삭제 수가 늘어난 9줄은 위의 기존 문장 8줄과 빈 줄 1개이다. 이들 삭제에도 각 정정·보완의 동일한 원문 근거를 적용했다.

정정·보완 표의 25개 위치는 실제 수정한 25줄과 일치한다. 모두 지정된 전수 검증 표시가 있다. 표 행의 표시는 결론 문장 칸 끝에 있다. 시작 대상 외에 추가로 고친 문장도 이 수에 포함했다.

차이 표는 출력 74행, 반암시 수심평균 21행, 명시적 다층 21행, 비구조 솔버 4행으로 총 120행이다. 기계 확인 후보 20건은 각각 판정했다. 후보의 지정 인용 자체는 모두 오탐이다. WATL 후보와 같은 행의 별도 VKSI 인용에는 정확한 과거 줄 번호를 보탰다.

상대 링크 37개는 모두 실제 파일을 가리킨다. 절대 경로와 이중 대괄호는 없다. 네 노트에는 Mermaid 블록이 없다. 미완 작업 문장과 빌드·실행 할 일은 남아 있지 않다. 매뉴얼의 빈 장·준비 중인 장을 설명하는 인용은 해당 원문의 사실이다.

최종 `git diff --check`는 오류를 출력하지 않았다. 이 작업의 쓰기는 대상 노트 네 개와 이 기록에 한정했다. 미해결 항목은 없다.

대조 250, 정정 15, 보완 10
