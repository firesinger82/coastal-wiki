# SWASH 노트 추가·수정 줄 전수 대조 (10-15, 작업 8)

대상은 `models/SWASH/README.md`, `swash-boundary-wave-forcing.md`, `swash-scalar-transport.md`, `swash-implicit-layered-flow.md`이다.
기존 노트의 대상은 작업 시작 시 `git diff -U0 HEAD -- <노트>`의 모든 추가 줄이다.
새 파일의 대상은 전체 줄이다.
삭제 줄은 최종 보고서의 수정 근거를 확인한다.
대조 줄 수는 frontmatter·빈 줄·표 구분자·코드 블록 경계를 포함한다.
정정 수와 보완 수는 수정한 노트 줄 수로 센다.
각 노트의 완료 기록에 대조 범위, 근거, 수정 전후, 기계 확인 후보 판정을 남긴다.

## 진행

네 노트의 작업 시작 추가 줄 241개와 삭제 줄 24개의 대조를 완료했다. 사용자 지시 6에 따른 기존 줄 정리 9개도 원문과 대조했다.

## 1. models/SWASH/README.md — 완료

- 대조한 추가 줄은 88개다. 작업 시작 줄 범위는 1–5, 10–14, 27, 36, 49–50, 53–56, 61, 64–132다.
- 삭제 줄 7개를 모두 확인했다. SI1-710, SO1-297, ST1-330–332, ST2-427과 SG1-931–933이 집계·현황 수정의 근거다. 과거 검수 기록은 과거 기록으로 보존되어 있다.
- 정정은 9줄이다. 보완은 1줄이다. 사용자 지시 6에 따라 기존 후속 항목도 함께 정리했다.
- frontmatter 1–4행은 보고서 반영 작업의 날짜와 방법을 적는다. 반영 기록 SWASH-notes-apply-8.md와 일치한다.
- 차이 표 6행의 분류와 결론은 최종 보고서 §5와 일치한다. 보고서 당시 파일 집계와 현재 목록을 구분했다.
- E 표 41행의 문장과 강도는 여섯 비교 보고서 §5 및 SWASH-callflow.md §8과 일치한다. 표에 적힌 현재 소스의 인용 위치를 모두 직접 열었다.
- E 표 강도는 강함 30행, 중간 10행, 약함 1행이다. SI1-229의 약함을 포함하여 최종 전수 검증 기록과 일치한다.
- swashuse PDF p.75·115·116 이미지는 crest 조건, 압력·침전물 출력 단위 및 인쇄 쪽 번호를 뒷받침한다.
- 공개 사본의 git show로 7949227·a486d5f·608ffd7·9554c98의 날짜와 제목을 확인했다. AD §1의 문서·코드 기준과 일치한다.
- 상대 링크는 실제 파일로 연결된다. 절대 로컬 경로와 이중 대괄호는 없다. 대상 추가 줄에 mermaid 블록은 없다.

### 정정·보완 목록

줄 번호는 이번 정정 후의 노트 번호다. 이 노트는 줄 수를 유지했다.

| 위치 | 종류 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| models/SWASH/README.md:49 | 정정 | 보고서 목록 집계만 제시 → 보고서 당시 21·3·1과 현재 21·4·1을 구분 | 각 디렉터리의 직접 *.md 목록; 새 swash-build-run-differences.md:1–21; SI1-710·ST1-332 |
| models/SWASH/README.md:54 | 정정 | 매뉴얼 3개 링크 → 현재 4개 링크 | models/SWASH/manual-notes/*.md 직접 목록 |
| models/SWASH/README.md:58 | 정정 | 다음 후보 → 관련 판독 자료 | 사용자 지시 6; 아래 세 원문의 판독 기록 |
| models/SWASH/README.md:60 | 정정 | 유동·솔버·조파 심화 예정 → 각 원문의 기능 사실 | src/SwashImpDep2DHflow.ftn90:40–61; src/SwashSolvers.ftn90:3312,4297; src/SwashBCtransferfnc.ftn90:40–51 |
| models/SWASH/README.md:62 | 정정 | gfortran/MPI 빌드 검증 할 일 → 기존 빌드·실행 파일 대조 노트 링크 | 사용자 지시 6; manual-notes/swash-build-run-differences.md:21; SG1-933 |
| models/SWASH/README.md:63 | 정정 | 처오름대 교차 링크 갱신 예정 → §3의 기존 연결 사실 | concepts/swash-zone/04-code-and-tools.md:39–42 |
| models/SWASH/README.md:69 | 보완 | 쪽 번호 관계만 설명 → 대조 전 README 인용과 보고서 당시 집계임을 명시 | 시작 diff의 삭제 줄; 최종 보고서 SI1-710·ST1-330–332·ST2-427; PDF 이미지 |
| models/SWASH/README.md:76 | 정정 | 사용자 설명서 제목 인용 :213 → :235 | manual-notes/swash-user-manual.md:235 |
| models/SWASH/README.md:78 | 정정 | 보존식 노트 제목 인용 :13 → :14 | manual-notes/swash-tech-ch2-ch5-mimetic-conservation.md:14 |
| models/SWASH/README.md:88 | 정정 | 실행 확인의 부정 문장 → 정적 대조에서 분류한 E 후보라는 사실 | 각 비교 보고서 §5; SWASH-callflow.md §8 |

### 기계 확인 후보 판정

- README.md:18의 `src/`: 오탐이다. 대조 전 위키 README의 삭제 줄에 있다. vendor README를 가리키지 않는다. 69행에 인용 시점을 보완했다.
- README.md:44의 `v12.01, src 152 Fortran`: 오탐이다. 시작 diff의 삭제 줄과 일치한다. 현재 원문은 .ftn90 152개와 .ftn 8개이다.
- README.md:42의 `(미생성)`: 오탐이다. 시작 diff의 삭제 줄과 일치한다. 현재 매뉴얼 직접 목록은 네 파일이다.
- README.md:5의 `**source-analysis 19 + manual-notes 2(swashtech·swashuse) + web-refs 1**`: 오탐이다. 대조 전 위키 README의 삭제 줄에 있다.
- src/SwashInputField.ftn90:188 뒤의 `src/ocpmix.ftn:963–965`: 오탐이다. 두 번째 파일의 독립 인용이다. 188행의 FAC 판독과 ocpmix 965행의 VFAC 나눗셈을 각각 확인했다.
- src/SwashCheckPrep.ftn90:591 뒤의 `src/SwashBCStokeswave.ftn90:101,166,245,334`: 오탐이다. 압력층 조건과 속도층별 구현을 가리키는 별도 인용이다. kpmax 검사와 kmax=1·2·3·4 분기를 각각 확인했다.
- src/SwashInit.ftn90:485 뒤의 `src/SwashCheckPrep.ftn90:5773–5774,5807`: 오탐이다. 초기 표본 카운터와 COMPUTE 준비의 평균 배열 초기화를 가리키는 별도 인용이다. 두 파일의 실제 대입을 확인했다.

## 2. models/SWASH/source-analysis/swash-boundary-wave-forcing.md — 완료

- 대조한 추가 줄은 86개다. 작업 시작 줄 범위는 7–8, 95–96, 149–152, 195–198, 221–294다.
- 삭제 줄 3개를 모두 확인했다. verification_method는 기존 기록에 보고서 반영을 덧붙였다. 폭과 delta를 혼동한 삭제 문장은 SI1-711이 정정한다. 스펙트럼 읽기 경로의 추정 삭제는 SI1-319와 SwashBCspecfile.ftn90:190–226이 뒷받침한다.
- 정정은 10줄이다. 보완은 1줄이다. 기존 110행의 미확인 문장도 사용자 지시 6에 따라 정리했다.
- 차이 표 62행의 분류와 결론을 최종 §5 및 전수 검증 기록과 대조했다. A 행은 없다. E 행 5개는 SI1-534·535·549·560 및 ST2-416이다. 다섯 행은 모두 강함이다.
- 각 표 행의 현재 소스와 과거 커밋 인용을 열었다. 겹치는 현재 소스 인용은 108개 구간으로 합쳐 대조했다. 과거 커밋은 17개 인용 구간을 열었다.
- 보고서 수정안 SI1-711, ST2-416, SG1-927–929를 본문과 대조했다. SG1-929 수정안의 nowarn1 표기는 실행문의 nowarn으로 판정했다.
- swashuse p.56–69의 판독 기록과 해당 원문을 대조했다. 숫자·식·단위는 p.36·37·59·64·65·67–69·128·132–134·157 이미지로 확인했다. swashtech p.19·63·83·84·113 원문과 p.63·83·84 이미지를 확인했다. p.145·147·156의 참조 위치와 부록 구문도 확인했다.
- 수식의 부호와 층수 조건을 유지했다. 표의 SG1-084·087 항목 칸에 잘린 문구만 짧은 제목으로 고쳤다. 결론 분류는 유지했다.
- 상대 링크는 실제 파일로 연결된다. 절대 로컬 경로와 이중 대괄호는 없다. 대상 추가 줄에 mermaid 블록은 없다.

### 정정·보완 목록

줄 번호는 정정 후의 노트 번호다. 이 노트는 줄 수를 유지했다.

| 위치 | 종류 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| swash-boundary-wave-forcing.md:7 | 정정 | 약반사 BC 호출 :785–829 → :858–870 | src/SwashUpdateUData.ftn90:858–870. :785–829는 Riemann·로그 분포 처리다. YAML 주석으로 정정 태그를 붙였다. |
| swash-boundary-wave-forcing.md:96 | 정정 | 경고 처리 뒤 nowarn 저장 → 외부 조건을 만족하면 10% 미만에도 저장 | src/SwashBCshortwave.ftn90:240–251; SG1-929 |
| swash-boundary-wave-forcing.md:110 | 정정 | 다항식의 차수·계수 규모와 출처 추정 → 분기별 분자·분모 및 설명서가 제시한 문헌 | src/SwashBCStokeswave.ftn90:229–231,313–315,407–409; swashuse PDF p.65·134 |
| swash-boundary-wave-forcing.md:221 | 정정 | 고차 계수 출처 문헌 미확인 → 설명서의 Keller-box 유도 설명과 Vasarmidis et al. (2024) 인용 | swashuse PDF p.134; p.65 |
| swash-boundary-wave-forcing.md:236 | 정정 | 항목 칸의 10 m 행이 0에서 잘림 → Table 5.3의 이론 차단 주파수 | swashuse PDF p.133 이미지의 10 m·K=3 값은 0.95다. 문서 원문 칸의 전체 표는 이미 정확하다. |
| swash-boundary-wave-forcing.md:238 | 정정 | 144 evanescent에서 잘린 항목 칸 → 에바네슨트 성분 제거 예제 | swashuse PDF p.134; SG1-087 |
| swash-boundary-wave-forcing.md:261 | 보완 | 파고·주기·CYCLE의 양수 조건에 직접 인용 없음 → 검사 줄을 추가 | src/SwashBounCond.ftn90:1246–1249,1266–1267; SI1-541 |
| swash-boundary-wave-forcing.md:263 | 정정 | 원 논문 검증의 부정 문장 → 설명서에 없는 코드 계수의 기록이라는 사실 | SI1-543; src/SwashServices.ftn90:278–297 |
| swash-boundary-wave-forcing.md:276 | 정정 | Mayer 논문 대조의 부정 지시 → 코드의 스펀지 함수 기록이라는 사실 | SI1-558; src/SwashSpongeLayer.ftn90:68,117; src/SwashUSpongLayer.ftn90:129–151,194–216 |
| swash-boundary-wave-forcing.md:277 | 정정 | 정형 영역 일반화·반복 방향 일괄 해제 → optg==1 및 x 조건 뒤 else if y 조건 | src/SwashCheckPrep.ftn90:660–701; 같은 최종 보고서 SG1-884의 정확한 조건 |
| swash-boundary-wave-forcing.md:278 | 정정 | 반대 검사도 찾지 못했다 → 준비 검사에는 구면 1D 금지 조건이 없다 | src/SwashCheckPrep.ftn90:658–702; SI1-560·E1 |

### 기계 확인 후보 판정

- 8756667:src/SwashBounCond.ftn90:564의 `if ( optg == 3 ) then`: 오탐이다. 해당 과거 커밋 564행과 일치한다.
- 8756667:src/SwashBounCond.ftn90:474의 방향 주석: 오탐이다. 해당 커밋은 counterclockwise와 clockwise를 모두 적는다. 후보 표시의 문구 절단은 노트 오류가 아니다.
- a79b2c6:src/SwashBounCond.ftn90:1158의 DIR1 판독: 오탐이다. 해당 커밋은 STA·−999를 사용한다.
- 8756667:src/SwashUpdateData.ftn90:934의 유량/수심 대입: 오탐이다. 해당 커밋 원문과 일치한다.
- 8756667:src/SwashBounCond.ftn90:873의 `else`: 오탐이다. 다음 줄은 `btype = 3`이다.
- a79b2c6:src/SwashCheckPrep.ftn90:545의 조건문, 노트 251행: 오탐이다. kpmax<5·qlay==0·ihydro==3 조건이 해당 커밋과 일치한다.
- 7949227:src/SwashBounCond.ftn90:194의 lriem 선언: 오탐이다. 해당 커밋 194행과 일치한다. 현재 파일에서는 193행이다.
- 8756667:src/SwashBounCond.ftn90:174의 lriem 선언: 오탐이다. 해당 커밋 174행과 일치한다.
- 8756667:src/SwashBounCond.ftn90:392의 vert(ix2) 조건: 오탐이다. 해당 커밋 392행과 일치한다.
- a79b2c6:src/SwashCheckPrep.ftn90:545의 조건문, 노트 267행: 오탐이다. 앞 후보와 별개인 두 번째 인용 위치도 같은 원문과 일치한다.
- 8756667:src/SwashReadInput.ftn90:2096의 WIDTH 판독: 오탐이다. 해당 커밋의 WIDTH는 piwg(2), DELTA는 2098행의 piwg(4)다.

## 3. models/SWASH/source-analysis/swash-scalar-transport.md — 완료

- 대조한 추가 줄은 37개다. 작업 시작 줄 범위는 7–8, 57, 178–180, 184, 187–188, 225, 227, 229–254다.
- 삭제 줄 10개를 모두 확인했다. SI2-141·146–148·151·283–284와 SWASH-notes-apply-2.md가 단위·매개변수·anti-creep 설명 교체의 근거다. 기존 수심평균 부유사 psm=1.0의 삭제는 다층 경로를 근거로 한 과도한 교체였으므로 57행에 복원했다.
- 삭제된 두 다층 수송 파일의 판독 유보는 이번 판독 기록으로 해소된다. SwashExpLay2DHtrans.ftn90.md는 1–1256행을 기록한다. SwashExpLayUtrans.ftn90.md는 1–1138행을 기록한다.
- 정정은 3줄이다. 보완은 1줄이다.
- frontmatter의 dispatch·Purpose·Method·fluxlim 위치를 현재 원문과 대조했다. 전체 파일 범위의 끝은 535에서 534로 고쳤다. last_source_check는 SWASH-notes-apply-2.md의 반영 날짜와 일치한다.
- 차이 표 12행의 분류와 결론은 최종 보고서 §5와 일치한다. SI2-150의 PDF 표기와 SI2-243의 백틱 차이는 의미 차이가 아니다. A 행은 없다. SI2-141은 git-verify-E2.md와 같은 E 강함이다.
- 표와 본문의 현재 소스 인용 구간을 모두 직접 열었다. 침식의 > 조건, 퇴적의 < 조건, psed의 단위, k−1 위층·kmax 최하층, 두 확산 보간 식을 확인했다.
- swashuse PDF p.23·83–87·159를 대조했다. p.85·86·87·159 이미지는 침식·퇴적 부호와 조건, 단위, 5.5d50, 부록 매개변수 이름 및 인쇄 쪽 번호를 뒷받침한다.
- 공개 사본의 8756667·9b8a012 원문은 침식식의 과거 인용과 일치한다. 9554c98의 SwashCheckPrep 변경은 수송 초기화 호출 위치를 옮긴다. 해당 변경에는 psed(12)의 밀도 환산이 없다.
- 상대 링크는 실제 파일로 연결된다. 절대 로컬 경로와 이중 대괄호는 없다. mermaid 블록과 남은 미완 문장은 없다.

### 정정·보완 목록

- 정정 — models/SWASH/source-analysis/swash-scalar-transport.md:7. 전: SwashExpDep1DHtrans 전문(:1-535). 후: 전문(:1-534). 근거: src/SwashExpDep1DHtrans.ftn90:534가 마지막 end subroutine이다.
- 정정 — models/SWASH/source-analysis/swash-scalar-transport.md:57. 전: 수심평균 1DH 절에서 부유사는 snum을 사용한다고 설명했다. 후: 수심평균 부유사는 psm=1.0이다. 다층 부유사는 psed(3)=snum이다. 근거: src/SwashExpDep1DHtrans.ftn90:157–161,303–305; src/SwashExpLay1DHtrans.ftn90:159–162,362–364; src/SwashReadInput.ftn90:1442. SI2-148의 다층 근거를 수심평균 경로 전체에 적용하지 않도록 고쳤다.
- 보완 — models/SWASH/source-analysis/swash-scalar-transport.md:230. 전: psed 단위와 ALFA·AK 이름에 모듈 정의만 연결했다. 후: swashuse PDF p.87과 src/SwashReadInput.ftn90:1444,1458을 추가했다. 근거: p.87의 N/m²·kg/m²/s와 AK→psed(13)·ALFA→psed(4) 입력문이다.
- 정정 — models/SWASH/source-analysis/swash-scalar-transport.md:245. 전: 문서 원문 칸이 “swashuse PDF p.159 및”에서 끊겼다. 후: p.83–87 본문의 설명 누락과 p.159 부록의 네 이름을 각각 적었다. 근거: SI2-146 최종 본문·결론과 해당 매뉴얼 쪽이다.

### 기계 확인 후보 판정

- src/SwashExpLay1DHtrans.ftn90:472 뒤의 “부터, 비구조 식은”: 오탐이다. 실제 인용은 8756667의 과거 472행이다. 해당 git show의 침식식이 노트와 일치한다. 한국어 연결 문장은 코드 인용이 아니다.
- src/SwashExpLayUtrans.ftn90:662 뒤의 “부터 같다.”: 오탐이다. 실제 인용은 9b8a012의 과거 662행이다. 해당 git show의 침식식이 노트와 일치한다. 현재 파일의 대응 침식식은 792행이다.

## 4. models/SWASH/source-analysis/swash-implicit-layered-flow.md — 완료

- 대조한 추가 줄은 30개다. 작업 시작 줄 범위는 7–8, 121–125, 158–161, 185–189, 213–226이다.
- 삭제 줄 4개를 모두 확인했다. ST1-335는 최하층과 최상층 조건의 정정 근거다. ST1-336은 시간 근사 보존 문구의 복원 근거다. ST2-431은 비구조 수위 행렬의 비대칭 단정 삭제 근거다. frontmatter의 보고서 반영 문구는 SWASH-notes-apply-6.md와 일치한다.
- 정정은 7줄이다. 보완은 1줄이다. 사용자 지시 6에 따라 기존 미완 절의 제목과 세 항목을 현재 원문의 사실 문장으로 바꿨다.
- frontmatter에 적힌 각 파일의 모든 인용 구간을 직접 열었다. qmax는 기본값이 아니라 kpmax−qlay 계산값이므로 용어를 고쳤다.
- 차이 표 3행의 분류와 결론은 최종 보고서와 일치한다. ST1-335는 B, ST1-336은 C, ST2-431은 B다. 보고서의 기존 검증 태그 생략과 상대 경로 확장에는 의미 차이가 없다. A·E 행은 없다.
- 2588–2592행의 fac1은 k−1 경계면에 연결된다. fac2는 k 경계면에 연결된다. 최하층 kmax와 최상층 1의 조건은 8756667의 2507–2511행에도 같다.
- M1D의 42–47행은 공간 에너지 보존과 시간 근사 보존을 구분한다. 시간 분할 이유와 theta=0.5 조건을 직접 확인했다.
- swashuse PDF p.99 이미지의 인쇄 쪽은 91이다. 같은 쪽은 반음해 수위 선형계를 대칭 양의 정부호라고 설명한다. pcgu·newtonU·bicgstab3 호출 위치를 원문과 대조했다.
- 상대 링크는 실제 파일로 연결된다. 절대 로컬 경로와 이중 대괄호는 없다. mermaid 블록과 남은 미완 문장은 없다.

### 정정·보완 목록

- 정정 — models/SWASH/source-analysis/swash-implicit-layered-flow.md:7. 전: iproj/qmax 기본값. 후: iproj 기본값·qmax 계산. 근거: src/SwashCheckPrep.ftn90:585의 qmax = kpmax - qlay와 630–636행의 iproj 기본값 분기다.
- 정정 — models/SWASH/source-analysis/swash-implicit-layered-flow.md:121. 전: face 두께·Δσ로 발산 연산자를 구성한다고 설명했다. 후: 실제 식의 hku·hks·zku·rdx와 여섯 성분을 적었다. 근거: src/SwashImpLay1DHflow.ftn90:2588–2599; src/SwashLayerIntfaces.ftn90:84,109–119. 인용 구간은 Δσ를 직접 사용하는 식이 아니다.
- 정정 — models/SWASH/source-analysis/swash-implicit-layered-flow.md:189. 전: sum(rhs)>0 사전 검사와 주석 1759행을 인용했다. 후: Newton 경로의 실제 조건 if ( .not. sum(rhsn) > 0d0 ) then과 오류 출력을 적었다. 근거: src/SwashImpLayUflow.ftn90:1761–1764.
- 정정 — models/SWASH/source-analysis/swash-implicit-layered-flow.md:208. 전: 미확인 / source-needed. 후: 보조 루틴과 행렬 연결. 근거: 아래 세 항목의 현재 원문 대조와 사용자 지시 6이다.
- 정정 — models/SWASH/source-analysis/swash-implicit-layered-flow.md:210. 전: 보조 루틴 내부는 별도 모듈이므로 source-needed라고 적었다. 후: 정형 풀이·전처리·Newton의 SwashSolvers 정의 위치, 비구조 풀이·Perot의 SwashUServ 정의 위치, sigmacoor의 SwashServices 정의 위치를 적었다. 근거: src/SwashSolvers.ftn90:2258,2694,3050,3312,4297,5283; src/SwashUServ.ftn90:17,299,1707,2324; src/SwashServices.ftn90:454. 이번 판독 기록은 세 파일의 해당 구현을 포함한다.
- 정정 — models/SWASH/source-analysis/swash-implicit-layered-flow.md:211. 전: gmatu·gmatw·dmat의 기하학적 의미는 추가 정독이 필요하다고 적었다. 후: gmatu·dmat 성분 1–6의 피연산 위치, gmatw의 제한된 연직 위치, ishif 설정 위치를 적었다. 근거: src/SwashImpLay1DHflow.ftn90:2691–2694,2853–2866,2884–2892; src/SwashCheckPrep.ftn90:5462–5482.
- 정정 — models/SWASH/source-analysis/swash-implicit-layered-flow.md:212. 전: 2D v 방향 설명은 1D 대칭 추론에 의존한다고 적었다. 후: v 운동량 조립 시작, 연직 삼중대각 풀이, vwetp 조건의 압력 보정 위치를 적었다. 근거: src/SwashImpLay2DHflow.ftn90:2170,3673–3698,6074–6077. 이번 판독 기록도 해당 구간을 포함한다.
- 보완 — models/SWASH/source-analysis/swash-implicit-layered-flow.md:216. 전: 표의 노트 인용이 변경 전 위치라는 설명이 없었다. 후: 두 보고서의 120·153·177행 인용은 수정 전 노트의 근거라고 명시했다. 근거: 작업 시작 git diff의 삭제 줄 번호와 ST1-335·336·ST2-431의 원문 칸이다.

### 기계 확인 후보 판정

- source-analysis/swash-implicit-layered-flow.md:120의 “표면(k==kmax)·표면압력층(presp==1)에서 경계조정”: 오탐이다. 표는 수정 전 노트 120행을 오류 사례로 인용한다. 현재 본문의 kmax 최하층·k=1 최상층 설명은 원문과 일치한다. 과거 인용임을 216행에 보완했다.
- src/SwashImpLay1DHflow.ftn90:2507 뒤의 “의”: 오탐이다. 실제 인용은 8756667의 2507–2511행이다. fac1·fac2와 두 조건문이 해당 git show 원문과 일치한다. 한국어 조사 “의”는 코드 인용이 아니다.
- source-analysis/swash-implicit-layered-flow.md:153의 “strictly energy conservative in discrete space ... The discrete advective operator…”: 오탐이다. 표는 수정 전 노트의 생략 인용을 재현한다. 원문의 nearly energy conservative for discrete time은 현재 본문 158–160행에 복원되어 있다.

## 최종 집계

| 노트 | 작업 시작 추가 줄 | 작업 시작 삭제 줄 | 정정 | 보완 |
|---|---:|---:|---:|---:|
| models/SWASH/README.md | 88 | 7 | 9 | 1 |
| models/SWASH/source-analysis/swash-boundary-wave-forcing.md | 86 | 3 | 10 | 1 |
| models/SWASH/source-analysis/swash-scalar-transport.md | 37 | 10 | 3 | 1 |
| models/SWASH/source-analysis/swash-implicit-layered-flow.md | 30 | 4 | 7 | 1 |
| 합계 | 241 | 24 | 29 | 4 |

- 대조 수는 작업 시작 diff의 추가 줄 수다. 삭제 줄의 근거 확인 수는 별도 열에 적었다.
- 정정 수에는 사용자 지시 6에 따른 기존 줄 정리 9개가 포함된다. README 58·60·62·63행, 경계 노트 110행, 암시적 다층 노트 208·210·211·212행이다.
- 최종 git diff의 추가 줄은 README 92개, 경계 노트 87개, 스칼라 노트 37개, 암시적 다층 노트 34개다. 합계 250개가 모두 검증 범위에 포함된다. diff 재배치로 추가 줄로 잡힌 README 57·59행은 빈 줄이다.
- 기계 확인 후보 23개는 각각 원문을 열어 판정했다. 모두 과거 위치·별도 인용·연결 문장을 잘못 묶은 오탐이다.
- 최종 파일의 상대 링크는 모두 존재한다. 새 정정·보완 표식 33개는 줄 끝에 있다. 표 행의 표식은 결론 문장 칸 끝에 있다.
- 네 노트에는 절대 로컬 경로와 이중 대괄호가 없다. 남은 미완 항목은 없다.
- 쓰기는 대상 노트 네 파일과 이 기록에 한정했다.

대조 241, 정정 29, 보완 4
