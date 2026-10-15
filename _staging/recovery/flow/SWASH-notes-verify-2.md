# SWASH 노트 추가·수정 줄 원문 대조 (2026-10-15)

대상은 지정된 노트 3개이다.
기존 노트는 시작 시점의 `git diff -U0 HEAD -- <노트>` 추가 줄을 대상으로 한다.
새 노트는 전체 줄을 대상으로 한다.
삭제 줄은 최종 보고서의 수정 근거와 대조한다.
줄 수에는 frontmatter, 빈 줄, 표 구분 줄을 포함한다.
대조 수는 지정된 추가 줄 수이다.
삭제 근거를 확인한 줄 수는 별도로 집계한다.
정정 수와 보완 수는 변경한 노트 줄의 수이다.
기록의 줄 번호는 정정 전을 기준으로 한다.
정정 후 줄 번호가 달라지면 함께 적는다.

## 수행 기록

노트 단위로 대조 결과를 덧붙인다.

## swash-user-manual.md — 완료

대상은 `models/SWASH/manual-notes/swash-user-manual.md`이다.
추가 165줄을 대조했다.
삭제 49줄의 근거를 확인했다.
정정은 6줄이다.
보완은 3줄이다.
수정 전후 줄 번호는 같다.

추가 줄 범위: 7–8, 17, 22–23, 46, 49, 63–67, 77, 81, 84, 92–99, 101, 104, 110, 115, 121, 126–127, 132, 139, 143, 152, 156–158, 171, 175, 181, 185, 188, 191, 196, 198–199, 202, 206–207, 209–210, 212–214, 216–217, 220, 222, 226, 228, 230–232, 238, 248–249, 263–264, 267–363.

frontmatter의 v12.01·167쪽은 원문 표지와 PDF에 일치한다.
`pdftotext -layout`의 현재 출력은 LF 6842개이다.
본문의 문법·기본값·단위·부호·조건·식은 쪽별 판독 기록, 추출 텍스트, 해당 쪽 이미지, 현재 코드와 대조했다.
층 번호는 최상층 k=1을 기준으로 대조했다.
차이 표 82행은 각 보고서 §4·§5와 마지막 전수 검증 기록을 대조했다.
A 분류 행은 없다.
E 강도는 SI1-155 중간, SI1-571 강함, SI2-111 강함, SI2-194 중간으로 최종 git 판정에 일치한다.
상대 링크 38개는 실제 파일을 가리킨다.
Mermaid 블록은 없다.
`/home/firesinger/`와 이중 대괄호 링크는 없다.

### 정정·보완 목록

아래 원문 코드 경로는 `models/SWASH/raw/source_code/swash/` 기준이다.

| 구분 | 노트:줄 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| 정정 | models/SWASH/manual-notes/swash-user-manual.md:96 | “기본 수온·염분의” 실제 밀도 → SET의 수온·염분 값으로 계산하는 실제 밀도 | `src/SwashReadInput.ftn90:535–536`은 TEMP·SALINITY를 읽는다. `src/SwashCheckPrep.ftn90:894–905`는 tempw·salw를 사용한다. theory-framework 최종 ST1-292·ST1-343도 지정값과 초기화 조건을 구별한다. |
| 정정 | models/SWASH/manual-notes/swash-user-manual.md:98 | “명령 미지정 시 일반 조건은 0” → BACKVISC 미지정 시 일반 조건의 배경 점성은 0 m²/s | `src/SwashCheckPrep.ftn90:909–913`의 대상은 bvisc이다. swashuse PDF p.34는 단위를 m²/s로 적는다. inputs-setup 최종 SI1-129에 일치한다. |
| 정정 | models/SWASH/manual-notes/swash-user-manual.md:101 | “STA·DYN 별칭 및 SKIPMOM·LIN은 코드의 추가 선택” → STA는 정상 모드이다. DYN은 NONST와 같은 비정상 모드이다. DYNAMIC·SKIPMOM·LINEAR는 부록 C에도 있다. | `src/SwashReadInput.ftn90:397–432`; swashuse PDF p.35·155; inputs-setup 최종 SI1-083·SI1-501. |
| 정정 | models/SWASH/manual-notes/swash-user-manual.md:139 | 선행 설명 없는 “이 문제” → 기본 PEAK 상태에서 모양 키워드를 생략한 MEAN 반복과 MEAN 뒤 PEAK의 부호 상태를 명시 | swashuse PDF p.56; `src/SwashBounCond.ftn90:272–296`; `src/SwashBCspectrum.ftn90:132–137`; E1 최종 SI1-571. E 강함은 유지했다. |
| 정정 | models/SWASH/manual-notes/swash-user-manual.md:231 | 일반적인 “PCG solver” → Newton을 끈 구조 격자 2DH는 PCG이다. Newton을 끈 1DH는 tridiag이다. | `src/SwashImpDep2DHflow.ftn90:2555,2742`; `src/SwashImpDep1DHflow.ftn90:851,954`; inputs-physics-numerics 최종 SI2-279. |
| 정정 | models/SWASH/manual-notes/swash-user-manual.md:248 | “새 경계 입력을 준비하는 절차를 따로 적는다” → 계산 뒤 fbfs 삭제, cubfs nullify, lbfs=false의 사실 문장 | `src/SwashMain.ftn90:135–140,333–339`; inputs-setup §4 SI1-098. 미완 작업 문장을 제거했다. |
| 보완 | models/SWASH/manual-notes/swash-user-manual.md:46 | evanescent 필터 설명의 직접 코드 인용 없음 → 해당 코드 인용 추가 | `src/SwashBCshortwave.ftn90:136–146`의 numdisp·omega 조건과 진폭 0 대입. |
| 보완 | models/SWASH/manual-notes/swash-user-manual.md:127 | 종료 생략·1%/99% 조건의 직접 코드 인용 없음 → 해당 코드 인용 추가 | `src/SwashInputGrid.ftn90:274–289`의 TENDINP 기본값 1.d20과 나머지 검사. |
| 보완 | models/SWASH/manual-notes/swash-user-manual.md:346 | 출처가 생략된 “§5” → inputs-setup §5.1 상대 링크 | `swash-inputs-setup-vs-code.md:712`의 “5.1 D의 전체 원문 검색”. maxmes 검색 결과와 D 결론은 유지했다. |

### 삭제 줄 근거

줄 번호는 HEAD의 삭제 전 번호이다.

| 삭제 줄 | 근거와 확인 결과 |
|---|---|
| 7, 16, 22, 63, 188, 244–247 | 검증 방법의 갱신, 상대 링크 전환, 표 행 이동, 후속 절의 구체화이다. apply-2와 guide-syntax-build §4 SG1-919에 대응한다. 사용자 지시대로 해결된 후속 항목을 사실·참조 문장으로 바꿨다. 문서의 정체와 연결 대상은 유지했다. |
| 21, 45, 48, 62, 73, 77, 80, 89, 92, 102, 108, 113 | inputs-setup §4의 SI1-700·042·047·701·116·120·702·135·140·703·173·715와 최종 §5에 대응한다. GFDL 쪽, 필터의 목적, 1% 경계, OUTPUT 분류, maxmes 효과, 실제·기준 밀도, 점성 종류, 선택 키워드, 투영 효과, 각도 열린 구간, 비정형 고정층, DAY를 원문대로 반영했다. |
| 127, 136, 178, 180, 190, 193–194, 199, 201, 207, 209–210, 240–241 | guide-syntax-build §4의 SG1-905·906·908–914·916·917·935와 최종 §5에 대응한다. inputs-physics-numerics의 SI2-289·291도 함께 대조했다. 파라미터 이름, 경계 입력 종류, BREAK 조건, theta 범위, solver 분기, 기본값, CFL, 등분포와 분산식을 원문대로 반영했다. |
| 140–141, 157, 163, 167, 170, 173, 183, 187, 191, 196, 205 | inputs-physics-numerics §4·최종 §5의 WIND, VISCOSITY, POROSITY, VEGETATION, CORIOLIS, TRANSPORT, AMBIENT, NONHYDROSTATIC, BOTCEL 대조에 대응한다. 설명서 사양과 코드의 생략값·예외를 구별한다. |
| 216, 226 | outputs §4 SO1-294·298과 최종 §5에 대응한다. 출력량 정의와 부록의 쪽을 구별했다. STOP의 COMPUTE 유무 분기를 반영했다. |

삭제 49줄은 모두 위 목록에 포함된다.
미완 작업 문장인 248줄은 이번 검증에서 실제 처리 설명으로 정정했다.
빌드·실행 검증을 요청하는 할 일 항목은 없다.

### 기계 확인 후보 판정 — 26건

각 행은 사용자가 제시한 순서의 후보 한 건이다.
과거 노트 줄은 읽기 전용 diff의 삭제 내용과 역대응으로 확인했다.
과거 코드 줄은 공개 저장소 사본의 `git show HASH:경로`로 확인했다.

| 번호 | 후보 | 판정 |
|---|---|---|
| M01 | `swash-user-manual.md:207`의 TIME INTEGRATION 제목 | 정상 과거 노트 인용이다. HEAD 207줄과 일치한다. 현재 제목은 228줄에서 PDF p.98–101과 인쇄 p.90–93을 구별한다. |
| M02 | `src/SwashBounCond.ftn90:369` 뒤 “(2022-09-03)부터 READXY 인수는 XP·YP” | 정상이다. 288줄의 HASH는 8756667이다. 해당 과거 369줄은 `call READXY ('XP','YP',...)`이다. 뒤 문장은 코드 인용이 아닌 이력 설명이다. |
| M03 | `swash-user-manual.md:136`의 Fourier(REGULAR)·time series(SPECTRUM) | 정상 과거 노트 인용이다. HEAD 136줄과 일치한다. 현재 본문 152줄은 네 입력 종류를 구별한다. |
| M04 | `src/SwashCheckPrep.ftn90:956` 뒤 “0.15·0.3 분기가 공존” | 정상이다. 290줄이 인용한 8756667의 해당 분기에 두 값이 공존한다. |
| M05 | `src/SwashCheckPrep.ftn90:1076` 뒤 “에도 같다” | 정상이다. 290줄은 a486d5f의 BETA 조건을 가리킨다. 현재 같은 경로의 1076줄에도 분기가 있다. |
| M06 | `src/SwashInit.ftn90:417` 뒤 “(2022-09-03)의 500” | 정상이다. 291줄은 8756667을 가리킨다. 해당 줄은 `pnums(25) = 500.`이다. |
| M07 | `src/SwashReadInput.ftn90:1194` 뒤 “100부터 두 값이 같은 판에 공존” | 정상이다. 291줄은 8756667을 가리킨다. 해당 줄의 MAXITER 생략값은 100이다. |
| M08 | `src/SwashInit.ftn90:377` 뒤 “CORRDEP는 MUSCL” | 정상이다. 293줄은 8756667의 CORRDEP 초기값을 가리킨다. pnums(11)=6은 MUSCL이다. |
| M09 | `swash-user-manual.md:241`의 분산식 | 정상 과거 노트 인용이다. HEAD 241줄과 일치한다. 현재 264줄의 식은 swashuse PDF p.128 이미지와 대조했다. |
| M10 | `src/SwashCheckPrep.ftn90:1145` 뒤 “같은 조건” | 정상이다. 297줄이 인용한 8756667의 theta 하한·상한 검사와 일치한다. |
| M11 | `src/SwashCheckPrep.ftn90:1273` 뒤 “에도 같다” | 정상이다. 297줄의 a486d5f에서도 theta 검사식이 같다. 현재 코드 인용과 과거 코드 인용을 혼동한 후보이다. |
| M12 | `src/SwashReadInput.ftn90:778` 뒤 “A2 입력과 같은 판” | 정상이다. 299줄의 8756667에서 A2를 읽는다. 같은 판의 WindStress는 수면 경사 항에 사용한다. |
| M13 | `src/SwashCheckPrep.ftn90:379` 뒤 “에도 있으며” | 정상이다. 314줄의 7949227에 위도 0을 포함한 Coriolis 해제 조건이 있다. E2의 E 강함과 일치한다. |
| M14 | `src/SwashInit.ftn90:417` 뒤 “500과” | 정상이다. 328줄의 8756667에는 500이 있다. 같은 판 ReadInput 1194줄에는 100이 있다. E2의 E 중간과 일치한다. |
| M15 | `manual-notes/swash-user-manual.md:140`의 WIND 제목 | 정상 과거 노트 인용이다. HEAD 140줄과 일치한다. 현재 156줄은 PDF p.73–76과 인쇄 p.65–68을 구별한다. |
| M16 | `8756667:src/SwashInit.ftn90:433`의 `maxmes = 200` | 정상이다. 과거 원문의 해당 줄과 일치한다. 현재 Init 474줄과도 값이 같다. |
| M17 | `8756667:src/SwashInit.ftn90:130`의 `grav   = 9.813` | 정상이다. 과거 원문의 해당 줄과 일치한다. |
| M18 | `8756667:src/SwashReadInput.ftn90:341`의 `call INKEYW ('STA',' ')` | 정상이다. 과거 원문의 해당 줄과 일치한다. |
| M19 | `8756667:src/SwashReadInput.ftn90:541`의 `mproj = 0` | 정상이다. 과거 원문의 해당 줄과 일치한다. |
| M20 | `8756667:src/SwashReadInput.ftn90:1724`의 REP/PER 조건 | 정상이다. 과거 원문의 해당 줄은 `if ( KEYWIS ('REP') .or. KEYWIS('PER') ) then`이다. |
| M21 | `8756667:src/SwashLayUIntfaces.ftn90:91`의 sigmacoor 호출 | 정상이다. 과거 원문의 해당 줄은 `call sigmacoor( zku , hu , nfaces )`이다. |
| M22 | `8756667:src/SwashBounCond.ftn90:274`의 부호 반전 | 정상이다. 과거 원문의 해당 줄은 `spshape(2) = -spshape(2)`이다. |
| M23 | `8756667:src/SwashBounCond.ftn90:943`의 FOUR 조건 — 코드 칸 | 정상이다. 노트 360줄의 코드 칸을 확인했다. 과거 원문은 `if ( KEYWIS('FOUR') ) then`이다. |
| M24 | `8756667:src/SwashBounCond.ftn90:943`의 FOUR 조건 — 결론 칸 | 정상이다. 노트 360줄의 결론 칸에서 같은 과거 원문을 다시 인용한다. M23과 별개 후보로 대조했다. |
| M25 | `manual-notes/swash-user-manual.md:76`의 `9.81` | 정상 과거 노트 인용이다. diff에서 역대응한 HEAD 76줄의 값은 9.81이다. 현재 표의 위치는 80줄이다. |
| M26 | `manual-notes/swash-user-manual.md:77`의 `1000.` | 정상 과거 노트 인용이다. HEAD 77줄의 값은 1000.이다. 현재 81줄은 설명서의 참조 밀도임을 적는다. |

## swash-linear-solvers.md — 완료

대상은 `models/SWASH/source-analysis/swash-linear-solvers.md`이다.
추가 48줄을 대조했다.
삭제 9줄의 근거를 확인했다.
정정은 0줄이다.
보완은 0줄이다.

추가 줄 범위: 6–7, 21, 26, 30–35, 75–76, 84–87, 115–117, 121–123, 125–150.

frontmatter의 소스 5705줄은 현재 파일과 일치한다.
Keller-box band와 인용 논문 정보는 `src/SwashSolvers.ftn90:133–137,237–239,1856–1862,3369–3371,4784–4786,5328–5334`와 대조했다.
격자별 호출은 각 flow 파일의 표에 적힌 호출 줄과 대조했다.
PCG의 초기 기준은 `src/SwashSolvers.ftn90:1207,1213`의 전처리 잔차 내적이다.
반복 상한의 입력·소비는 Init 458줄, ReadInput 1540–1546줄, Solvers 1938줄·3451줄, UServ 1323줄·1846줄에 일치한다.
차이 표 15행의 분류와 결론은 guide-syntax-build, inputs-physics-numerics, theory-unstructured의 최종 §5에 일치한다.
theory-unstructured의 두 전수 검증 기록에 나뉜 ST2-219–228과 ST2-403–430을 모두 대조했다.
A 분류 행은 없다.
ST2-403의 E 중간은 E2 SI2-194와 일치한다.
SI2-190은 두 허용오차의 합을 반영한 최종 F 판정이다.
ST2-430은 PCG와 BiCGSTAB 카드 혼동을 고친 최종 B 판정이다.
swashtech PDF p.115–116 이미지의 `M=LU=A+K`와 식 (11.3)의 양의 K 부호에 일치한다.
swashtech PDF p.119–128의 참고문헌에는 Stone·Ferziger의 서지 항목이 없다.
상대 링크 13개는 실제 파일을 가리킨다.
Mermaid 블록은 없다.
절대 홈 경로, 이중 대괄호 링크, 미완 작업 항목은 없다.

삭제 6·20·25·29–30줄은 검증 설명과 격자별 solver 구분의 수정이다.
근거는 theory-unstructured §4 ST2-225와 inputs-physics-numerics 최종 SI2-189·279이다.
삭제 104줄은 PCG와 BiCGSTAB의 카드 혼동이다.
근거는 theory-unstructured §4·최종 §5 ST2-430과 실제 카드 대입이다.
삭제 108–110줄은 동일 파일을 가리키는 상대 Markdown 링크로 바뀌었다.
이 삭제·치환은 apply-4의 선형 솔버 반영 기록과 일치한다.

### 기계 확인 후보 판정 — 4건

| 번호 | 후보 | 판정 |
|---|---|---|
| S01 | `src/SwashInit.ftn90:417` 뒤 “500을” | 정상이다. 노트 147줄은 8756667의 `pnums(25) = 500.`을 가리킨다. 현재 파일의 417줄을 인용한 것이 아니다. |
| S02 | `src/SwashReadInput.ftn90:1194` 뒤 “100을 사용” | 정상이다. 노트 147줄은 8756667을 가리킨다. 해당 과거 줄은 MAXITER 생략값 100을 읽는다. |
| S03 | `src/SwashReadInput.ftn90:1543` 뒤 “에도 100” | 정상이다. 노트 147줄은 7949227을 가리킨다. 해당 과거 줄과 현재 줄의 생략값은 모두 100이다. |
| S04 | `src/SwashSolvers.ftn90:3449` 뒤 “부터 BiCGSTAB는” | 정상이다. 노트 150줄의 범위는 8756667의 3449–3451줄이다. reps(1)·reps(2)·maxit에 pnums(22)·pnums(23)·pnums(25)를 대입한다. |

## swash-official-resources.md — 완료

대상은 `models/SWASH/web-refs/swash-official-resources.md`이다.
추가 27줄을 대조했다.
삭제 6줄의 근거를 확인했다.
정정은 0줄이다.
보완은 0줄이다.

추가 줄 범위: 7–8, 24–26, 33–48, 53, 68–71, 76.

frontmatter와 URL 표의 주소·버전·DOI는 원자료 `README.md:3–8,30–38`과 일치한다.
GPL v3 표기는 원자료 `LICENSE:1–2`와 일치한다.
논문 서지 유지의 근거는 guide-syntax-build 최종 SG1-934이다.
2011 논문의 저자·제목·권·쪽은 swashtech PDF p.128의 참고문헌 [118]에도 있다.
2003 논문의 서지는 swashtech PDF p.125의 참고문헌 [87]에도 있다.

공개 사본에서 `git show -s --date=short --format`으로 744735e, 8756667, 5d279d7, 9b8a012, 9d03fff, e7a8009, 25c79e7, 7949227, 608ffd7, 9554c98, a486d5f의 날짜·제목을 대조했다.
노트 34–42줄의 HASH·날짜·제목은 모두 일치한다.
`git show -s --format=%H %P`로 a486d5f의 부모를 따라 집계한 고유 커밋 수는 91개이다.
이 수는 AD §1과 E1 §1에 일치한다.
원자료의 `.git/refs/heads/main`과 `.git/shallow`는 모두 a486d5f를 가리킨다.
원자료의 src 파일 162개를 공개 사본의 `git show a486d5f:src/파일`과 바이트 단위로 대조했다.
파일 이름과 내용은 모두 일치한다.
웹 패치 게시 중단과 GitLab 수정 반영은 저장된 `problems_and_fixes.htm:27–29`와 일치한다.
웹 사본과 원자료의 swashuse·swashtech PDF에서 각각 `pdftotext -layout`으로 얻은 텍스트가 일치한다.

비구조 MPI 제한은 원자료 `README.md:245`와 `src/SwashReadInput.ftn90:2481–2484`에 일치한다.
최종 theory-unstructured ST2-421도 같은 판정이다.
nesting 조건은 swashuse PDF p.25·63과 inputs-setup §4 SI1-001 수정안에 일치한다.
`src/SwashBounCond.ftn90:1957`은 nesting 표지를 true로 전달한다.
`src/SwashBCspecfile.ftn90:289–313`은 비정상 스펙트럼, 좌표계 불일치, 단일 위치를 거부한다.
FUNWAVE·Celeris 연결의 Boussinesq 분류는 연결된 각 README의 정체 카드에 일치한다.
상대 링크 18개는 실제 파일을 가리킨다.
차이 표와 Mermaid 블록은 없다.
절대 홈 경로, 이중 대괄호 링크, 미완 작업 항목은 없다.

삭제 7줄은 검증 방법에 대조 기록을 덧붙인 치환이다.
삭제 23–25·36줄은 같은 URL·DOI를 링크 없는 주소로 바꾼 치환이다.
삭제 55줄은 FUNWAVE·Celeris의 같은 파일을 가리키는 상대 Markdown 링크 치환이다.
이 삭제·치환은 apply-3의 공식 자료 노트 반영 기록과 일치한다.
이 노트에 배정된 기계 확인 후보는 없다.

## 최종 집계

| 노트 | 대상 추가 줄 | 삭제 근거 확인 줄 | 정정 줄 | 보완 줄 |
|---|---:|---:|---:|---:|
| swash-user-manual.md | 165 | 49 | 6 | 3 |
| swash-linear-solvers.md | 48 | 9 | 0 | 0 |
| swash-official-resources.md | 27 | 6 | 0 | 0 |
| 합계 | 240 | 64 | 6 | 3 |

추가·삭제 줄 수는 지정한 읽기 전용 `git diff -U0 HEAD -- <노트>`에서 집계했다.
정정·보완 수는 이번 검증 표지가 붙은 고유 노트 줄에서 집계했다.
이번에 바꾼 노트 9줄은 모두 시작 시점의 추가 줄 범위 안에 있다.
모든 표지는 지정한 줄 끝에 있다.
표 행의 표지는 결론 문장 칸 끝에 있다.
기계 확인 후보 30건의 판정을 모두 기록했다.
상대 링크 69개의 대상 파일이 존재한다.
대상 추가 줄의 미대조 항목은 없다.
삭제 근거의 미확인 항목은 없다.
미해결 항목은 없다.

대조 240, 정정 6, 보완 3
