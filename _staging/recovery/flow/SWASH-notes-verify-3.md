# SWASH 노트 전수 대조 3 (2026-10-15)

대상은 사용자 지정 노트 네 개다. 기존 노트의 대상 줄은 작업 시작 시 `git diff -U0 HEAD -- <노트>`의 모든 추가 줄이다. 새 파일의 대상 줄은 전체 줄이다. 삭제 줄은 최종 보고서의 삭제 근거와 대조한다. 빈 줄과 frontmatter도 집계한다.

현재 코드, 지정한 공개 저장소 사본의 과거 코드, 쪽별 판독 기록, PDF 쪽 이미지, 최종 대조 보고서를 근거로 사용한다. 수정은 대상 노트와 이 기록에만 적용한다. 정정 수와 보완 수는 수정한 노트 줄 수로 집계한다. 같은 줄의 복수 정정은 한 줄로 센다. 내용 정정과 인용 보완이 함께 있는 줄은 정정으로 센다.

## 진행 기록

### 1. swash-input-parsing-check.md — 완료

대조한 추가 줄은 136줄이다. 삭제 줄은 11줄이다. 정정은 5줄이다. 보완은 1줄이다. 추가 줄의 시작 시점 범위는 7–8, 60–63, 73–76, 124, 144–145, 201–203, 235–245, 280, 306–307, 310–415다. 마지막 범위에는 차이 표 96행이 포함된다. 빈 줄·표 머리·frontmatter도 대조했다. 아래 노트 줄 번호는 이 검증의 수정 후 번호다.

현재 코드 인용과 공개 저장소 사본의 과거 코드 인용을 열었다. 최종 보고서의 수정안·결론·전수 검증 기록과 대조했다. 매뉴얼 판독 기록과 추출 텍스트를 대조했다. 숫자·기호·표가 있는 문장은 쪽 이미지도 대조했다. swashuse PDF p.108의 FRAME·Nautical 설명도 쪽 이미지에서 확인했다. A 판정으로 바뀐 행은 없다. FLOAT와 TEST의 E 판정은 E1 보고서의 강한 근거와 같다. 모든 상대 링크가 실제 파일을 가리킨다. 절대 경로와 이중 대괄호 링크는 없다. 새 미완 항목은 없다.

삭제 줄의 근거: frontmatter는 판독 방법을 보존하고 recovery 반영을 추가했다. KEYWIS·UNC 설명은 SI1-705·SG1-920 수정안에 따른다. 두 source-needed 문장은 SG1-925의 직접 파싱 근거로 대체했다. 삼각형 조건은 SI1-707에 따라 90도 이상으로 고쳤다. 같은 삭제 줄에 있던 전체 예각 안내는 삭제 근거가 없어 복원했다. 오류 수준 네 줄과 종료 요약은 SG1-922·SI1-706에 따른다. CFL 행은 SG1-923·SI2-292에 따른다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| swash-input-parsing-check.md:76 | 보완 | UNC 설명의 보고서 링크만 있음 → 네 입력 루틴의 직접 코드 인용 추가 | `src/ocpcre.ftn:474–480,656–661,818–823,999–1004`. INREAL은 INDBLE을 호출한다. 나머지 UNC 분기는 미입력 값을 보존한다. |
| swash-input-parsing-check.md:204 | 정정 | 전체 예각 안내 삭제 → 전체 예각일 때 수준 0 안내를 호출한다는 사실 복원 | `src/SwashCheckGrid.ftn90:168,195`의 `acute = .true.`와 `if (acute) call msgerr (0, 'The grid contains solely acute triangles ')`. SI1-707은 각도 경계 정정만 요구한다. |
| swash-input-parsing-check.md:245 | 정정 | level 4 이상이면 true → `LEVERR >= 4`이면 반환값을 우선 true로 설정 | `src/ocpmix.ftn:1494–1500`. 뒤에서 MAXERR 예외와 OpenMP 병렬 구역 예외가 반환값을 덮어쓴다. |
| swash-input-parsing-check.md:326 | 정정 | 근사 분산 안내 조건이 ITEST·numdisp뿐임 → 외부 조건 `.not.momskip` 추가 | `src/SwashPrintSettings.ftn90:75,100–102`와 `src/SwashMain.ftn90:183`. SG1-033 최종본에 생략된 외부 조건을 원문에 맞췄다. C 분류는 유지했다. |
| swash-input-parsing-check.md:348 | 정정 | REPEATING의 1D·비구조 제한은 swashuse PDF p.37 → p.38 | swashuse PDF p.38 쪽 이미지의 `NOT FOR 1D-MODE AND UNSTRUCTURED GRIDS.`. SG1-875 최종본의 쪽 인용 오류도 노트에서 바로잡았다. |
| swash-input-parsing-check.md:397 | 정정 | STPNOW는 level 4 이상에서 true → level 4 이상에서 반환값을 우선 true로 설정 | `src/ocpmix.ftn:1494–1500`. 본문과 SI1-706 결론의 대입 순서를 일치시켰다. B 분류는 유지했다. |

기계 확인 후보 판정은 다음과 같다. 후보 12건은 모두 오판이다.

| 후보 | 판정과 원문 |
|---|---|
| 노트:224의 `- level **2**: 심각 경고` | 수정 전 노트의 인용이다. 시작 시점 git diff의 삭제 줄 및 SG1-922 원문과 같다. 현재 노트의 수준 정의를 인용한 것이 아니다. 현재 표 위치는 361줄이다. |
| `src/ocpmix.ftn:1386` 뒤의 “부터 수준 2 Error…” | 앞의 `8756667 2022-09-03`이 적용되는 과거 인용이다. 해당 커밋 1386–1389줄의 수준 2·3 분기와 같다. 현재 표 위치는 361줄이다. |
| `src/ocpmix.ftn:1375` 뒤의 “에도 같다…” | `a486d5f` 과거 인용 뒤의 설명이다. 해당 커밋 1375–1378줄의 수준 2·3 분기와 같다. 현재 표 위치는 361줄이다. |
| `src/SwashCheckPrep.ftn90:1117` 뒤의 “부터 같은 범위…” | `8756667` 과거 인용이다. 해당 커밋 1117–1128줄의 열린 범위 검사와 high<low 보정이 설명과 같다. 현재 표 위치는 362줄이다. |
| `src/SwashCheckPrep.ftn90:1245` 뒤의 “에도 같다…” | `a486d5f` 과거 인용이다. 해당 커밋 1245–1256줄의 CFL 조건과 같다. 현재 표 위치는 362줄이다. |
| `src/SwashCheckPrep.ftn90:262` 뒤의 “에도 같은 활성화…” | `8756667` 과거 인용이다. 해당 커밋 262–265줄의 바람 입력장 활성화와 같다. 현재 표 위치는 363줄이다. |
| `8756667:src/SwashReadInput.ftn90:281`의 NAME 호출 | 해당 커밋 281줄에 `call INCSTR ('NAME'  , PROJID, 'UNC', BLANK)`가 있다. 현재 표 위치는 378줄이다. |
| `8756667:src/SwashReadInput.ftn90:1756`의 EXCVAL 호출 | 해당 커밋 1756줄에 `call INREAL ('EXCVAL', excfld(9), 'STA', excfld(8))`가 있다. 현재 표 위치는 381줄이다. |
| `5d279d7:src/SwashReadInput.ftn90:930`의 INKEYW 호출 | 해당 커밋 930줄에 `call INKEYW ('REQ',' ')`가 있다. 현재 표 위치는 383줄이다. |
| `8756667:src/ocpmix.ftn:1386`의 LEV 분기 | 해당 커밋 1386줄에 `ELSE IF (LEV.EQ.2) THEN`이 있다. 현재 표 위치는 397줄이다. |
| `src/SwashReadInput.ftn90:2220` 뒤의 “도” | `8756667` 과거 인용이다. 해당 커밋 2220줄의 TEST 분기 수준은 30이다. 현재 표 위치는 399줄이다. |
| `src/SwashReadTestpnts.ftn90:216` 뒤의 “도 FILE 키워드 없이…” | `8756667` 과거 인용이다. 해당 커밋 216줄은 FNAME을 직접 읽는다. `misc/swash.edt:334` 및 swashuse PDF p.163 쪽 이미지도 같은 문법이다. 현재 표 위치는 400줄이다. |

### 2. swash-architecture-source-map.md — 완료

대조한 추가 줄은 51줄이다. 삭제 줄은 14줄이다. 정정은 6줄이다. 보완은 1줄이다. 추가 줄의 시작 시점 범위는 7–8, 19–23, 37–43, 51, 54–59, 66, 94, 100–114, 116–128이다. 차이 표 11행을 포함한다. 아래 노트 줄 번호는 수정 후 번호다.

현재 원문 목록과 srclist의 대응을 대조했다. `.f90`와 `${EXTF}`를 각각 `.ftn90`와 `.ftn` 원본에 대응시키면 160개가 중복 없이 일치한다. 현재 원본은 `.ftn90` 152개와 `.ftn` 8개다. `a486d5f`의 srclist도 현재 목록과 같다. `Swash.ftn90`는 71줄이다. frontmatter의 판독 방법과 날짜는 반영 기록과 일치한다.

계산 드라이버·INITIAL·mimetic·비정수압 선택·MPI 초기화와 종료·층별 교환의 인용 구간을 열었다. MPI 라이브러리 내부는 이 노트의 판정 대상이 아니다. `7949227`·`9554c98`·`a486d5f`의 CheckPrep 5974·5979줄을 각각 열었다. STEADY 호출 위치는 같고 압력 격자 초기화 조건만 바뀐다. 커밋 날짜와 변경 내용은 AD 판정 및 RF-011 최종본과 일치한다. swashuse PDF p.55·99·143–144와 swashtech PDF p.117을 판독 기록·추출 텍스트와 대조했다. A·E 행은 없다. mermaid 블록은 없다. 상대 링크는 모두 존재한다. 절대 경로·이중 대괄호 링크·미완 작업 목록은 없다.

삭제 줄의 근거: 소스 수는 RF-009·SG1-931에 따른다. 호출 단계는 RF-008·RF-011에 따른다. 이 과정에서 삭제 근거 없이 사라진 SwashInit·SwashReadInput 호출은 복원했다. Exp/Imp·M·U 설명과 예시 행은 RF-006·RF-007·ST1-341·ST1-342에 따른다. SWAN 링크는 기존 대상의 실제 Markdown 경로로 바뀌었다. 미보강 제목과 다섯 TODO는 사용자의 미완 항목 제거 지시에 따라 관련 노트 링크로 대체한 것이다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| swash-architecture-source-map.md:37 | 정정 | 초기화 호출 설명 삭제 → SwashMain의 SwashInit 호출 복원 | `src/SwashMain.ftn90:126`의 `call SwashInit ( inerr )`. callflow §1 및 RF-008 수정안은 중간 단계를 추가하라고 한다. 초기화 삭제 근거는 없다. |
| swash-architecture-source-map.md:38 | 정정 | 명령 읽기 호출 설명 삭제 → SwashMain의 SwashReadInput 호출 복원 | `src/SwashMain.ftn90:135–140`의 반복문과 `call SwashReadInput ( comput )`. callflow §1의 명령 읽기 순서와 같다. |
| swash-architecture-source-map.md:40 | 정정 | SwashComputStruc가 유동을 호출함 → `.not.momskip` 조건을 원문대로 명시 | `src/SwashComputStruc.ftn90:125`의 `if ( .not.momskip ) call SwashComputFlow`. |
| swash-architecture-source-map.md:43 | 정정 | INITIAL이 입력 중 해 배열을 설정함 → 입력 중 SwashInitCond에서 처리함 | `src/SwashReadInput.ftn90:2825–2826`. `src/SwashInitCond.ftn90:141–146`의 STEADY는 표지만 설정한다. 배열 설정으로 일반화하지 않는다. |
| swash-architecture-source-map.md:60 | 보완 | M과 일반 경로 구별에 보고서 링크만 있음 → 두 경로 헤더의 직접 인용 추가 | `src/SwashImpDep1DHflow.ftn90:54–57`과 `src/SwashImpDepM1DHflow.ftn90:42–44`. 일반 경로도 운동량 보존 이류를 기술한다. |
| swash-architecture-source-map.md:61 | 정정 | 시간 에너지 보존 한계만 있음 → M1DH 헤더의 이산 질량·운동량 보존과 공간 에너지 보존도 명시 | `src/SwashImpDepM1DHflow.ftn90:42–47`. ST1-341 수정안이 요구한 공간 보존과 시간 보존의 구별을 반영했다. |
| swash-architecture-source-map.md:129 | 정정 | 치명 오류/정상 종료라는 요약 → MPI 초기화 상태와 `LEVERR.GE.4` 조건 명시 | `src/swanparll.ftn:307–326`. ELSE는 수준 4 미만을 포함한다. ST2-420의 C 분류는 유지했다. |

기계 확인 후보 판정은 다음과 같다. 후보 6건은 모두 오판이다.

| 후보 | 판정과 원문 |
|---|---|
| `source-analysis/swash-architecture-source-map.md:44`의 `U(연직 단면)` — RF-006 | 수정 전 노트의 인용이다. 시작 시점 diff의 삭제 줄 및 RF-006 원문과 같다. 현재 정의는 `src/SwashCompUFlow.ftn90:40`의 삼각 격자로 정정되어 있다. 현재 표 위치는 120줄이다. |
| 같은 노트 `:40`의 `시간적분 (비정수압 압력)` | 수정 전 노트의 인용이다. 시작 시점 diff 및 RF-007 원문과 같다. 실제 대응은 `src/SwashComputFlow.ftn90:44–47` 및 `src/SwashReadInput.ftn90:1499–1513,1864–1865`와 같다. 현재 표 위치는 121줄이다. |
| `src/SwashCheckPrep.ftn90:5979` 뒤의 “를” | `9554c98`의 과거 코드 변경을 설명하는 연결어다. 해당 커밋 원문은 `if ( lsubg .and. ihydro /= 3 ) then`이다. `7949227` 원문은 `if ( lsubg ) then`이다. 현재 표 위치는 124줄이다. |
| `src/srclist.cmake:2` 뒤의 “은 현재 목록과 같다…” | `a486d5f:src/srclist.cmake:2–161`이라는 범위 인용 뒤의 설명이다. 과거 파일과 현재 파일이 같다. 전처리 확장자에 대응시킨 목록은 현재 원본 160개와 같다. 현재 표 위치는 125줄이다. |
| 같은 노트 `:43`의 `운동량보존(momentum-conservative) 변형` | 수정 전 노트의 인용이다. 시작 시점 diff 및 ST1-341 원문과 같다. 실제 선택자는 `src/SwashComputFlow.ftn90:93–96`의 mimetic이다. 현재 표 위치는 126줄이다. |
| 같은 노트 `:44`의 `U(연직 단면)` — ST1-342 | RF-006과 같은 수정 전 문장을 별도 보고서 행이 인용한다. `src/SwashExpDepUflow.ftn90:44`는 삼각 격자를 명시한다. 현재 표 위치는 127줄이다. |

### 3. swash-grid-oceanpack-infra.md — 완료

대조한 추가 줄은 33줄이다. 삭제 줄은 2줄이다. 정정은 3줄이다. 보완은 6줄이다. 추가 줄의 시작 시점 범위는 7–8, 64–68, 113–115, 124–146이다. 차이 표 12행을 포함한다. 사용자 확인 항목 6에 따라 추가 줄 밖의 기존 27줄도 대조하고 정정했다. 이 기존 한 줄은 추가 줄 수 33에 합산하지 않았다. 아래 노트 줄 번호는 수정 후에도 같다.

frontmatter는 기존 직접 판독 방법을 보존하고 이번 대조 날짜를 추가했다. 외심·무게중심·면 거리의 현재 코드를 열었다. swashtech PDF p.43·44·52·53의 식·그림·조건을 쪽 이미지 및 판독 기록과 대조했다. p.52의 정삼각형 좌표를 코드의 외심식에 대입하면 중심은 `(0, 1/2)`이다. 쌍대 변 하나의 길이 0과 양쪽 중심 거리 합의 0을 구분했다.

날짜·파일 이름·파일 단위 번호·SET·ADC·ITRACE의 인용 구간과 과거 원문을 열었다. swashuse PDF p.25·27·32·45–46·122·155의 숫자·따옴표·명령 도식을 쪽 이미지로 대조했다. 부록 B의 문자·반복·연속 행 설명도 대조했다. ITRACE의 E 강함은 E1 최종 판정과 같다. A 행은 없다. 상대 링크는 모두 존재한다. mermaid·절대 경로·이중 대괄호 링크·미완 항목은 없다.

삭제 줄의 근거: frontmatter는 판독 내용을 보존했다. SwanGridCell 요약의 변경은 ST2-005·ST1-307의 외심 보정 설명에 따른다. 삭제된 ncc 증가 사실은 삭제 근거가 없어 실제 대체 분기의 설명에 복원했다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| swash-grid-oceanpack-infra.md:27 | 정정 | fullupdated는 거의 미사용이며 추가 검증 필요 → 선언 이외의 이름 참조가 없음 | 현재 `src/` 전체의 대소문자 무시 검색 결과는 `src/SwanGridobjects.ftn90:181`의 선언 한 곳이다. 해당 판독 기록도 같은 선언을 기록한다. 좌표 오프셋 설명은 `src/SwanInterpolatePoint.ftn90:124–127`의 경고 메시지로 한정했다. |
| swash-grid-oceanpack-infra.md:66 | 정정 | 외심이 외부이면 무조건 대체 → ccn이 참인 검사에서 외부로 판정할 때 대체 | `src/SwanGridCell.ftn90:246,263–291`. 같은 대체 분기의 `ncc = ncc + 1`도 복원했다. SET CC 경로는 `numcrs = 1`로 외심을 유지한다. |
| swash-grid-oceanpack-infra.md:68 | 정정 | SET CC 다음의 모호한 “이 동작” → 매뉴얼에 설명된 대상은 외심의 무게중심 대체라고 명시 | swashtech PDF p.44·52 쪽 이미지. ST2-005는 기하학적 대체 설명을 일치로 판정한다. ST1-307은 선택 명령의 설명 누락을 별도로 C로 판정한다. |
| swash-grid-oceanpack-infra.md:135 | 보완 | fort.14를 언급한 쪽만 인용 → READgrid UNSTRUC 도식의 쪽도 추가 | swashuse PDF p.39·156 및 `misc/swash.edt:42–43`은 TRIAngle·EASYmesh를 열거한다. `src/SwashReadInput.ftn90:2489–2497`에는 ADC 경로가 있다. SG1-867의 C 범위를 직접 뒷받침한다. |
| swash-grid-oceanpack-infra.md:136 | 보완 | SI1-077의 현재 코드 결론만 있음 → 최종본의 과거 커밋 근거 추가 | `8756667:src/ocpids.ftn:500,512–516`. 현재 `src/ocpids.ftn:504,517–557`과 연도 절단점이 같다. AD의 SI1-077 및 H9 판정과 같다. |
| swash-grid-oceanpack-infra.md:137 | 보완 | SI1-081의 현재 길이 결론만 있음 → 최종본의 과거 커밋 근거 추가 | `8756667:src/ocpmod.ftn:227`의 LENFNM=140. 현재 `src/ocpmod.ftn:224–227`은 경로를 포함한 길이를 명시한다. SERIES 첫 이름의 별도 제한은 `src/ocpmix.ftn:690`이다. |
| swash-grid-oceanpack-infra.md:138 | 보완 | SI1-102의 현재 한도 결론만 있음 → 과거 커밋·SGI 한도·설정 읽기 인용 추가 | `8756667:src/ocpids.ftn:192`의 99999. 현재 `src/ocpids.ftn:135,195–196,253,275–277`은 읽기·쓰기·기본 한도·SGI 분기를 구분한다. AD 최종 판정과 같다. |
| swash-grid-oceanpack-infra.md:139 | 보완 | SI1-210의 현재 형식 결론만 있음 → 최종본의 과거 커밋 근거 추가 | `8756667:src/ocpids.ftn:539`의 여섯 정수 읽기. swashuse PDF p.45·46의 형식 5는 닫는 따옴표만 있다. H9는 이 형식을 바꾸지 않는다. |
| swash-grid-oceanpack-infra.md:142 | 보완 | 일반 STRACE 구간만 인용 → ITRACE 활성화·OpenMP·과거 인용 추가 | `src/SwashReadInput.ftn90:2788–2792`, `src/ocpmix.ftn:1242–1252`, `8756667:src/ocpmix.ftn:1254,1262–1263`. E1 SO1-205의 E 강함을 유지했다. |

이 노트에 사용자가 지정한 기계 확인 후보는 없다.

### 4. swash-vegetation-porosity.md — 완료

대조한 추가 줄은 24줄이다. 삭제 줄은 3줄이다. 정정은 7줄이다. 보완은 4줄이다. 추가 줄의 시작 시점 범위는 7–8, 112–114, 238–256이다. 차이 표 6행을 포함한다. 사용자 확인 항목 6에 따라 추가 줄 밖의 기존 131줄도 대조하고 정정했다. 이 기존 한 줄은 추가 줄 수 24에 합산하지 않았다. 아래 노트 줄 번호는 수정 후 번호다.

frontmatter에 적힌 식의 줄 번호와 배열 이름도 현재 원문으로 대조했다. 식생·다공성 입력, 준비 단계의 검사와 계수 설정, 유속 갱신을 연결해 확인했다. 구조물 높이·대표 파주기·공극률의 단위·기본값·범위는 swashuse PDF p.42–43·48·81–82 쪽 이미지와 판독 기록을 대조했다. 수동 추적자의 질량교환 설명은 p.86–87과 대조했다. swashtech PDF p.63 식 (3.2)에는 표에서 지적한 다공성·식생 계수가 없다. C 분류의 범위를 이 식으로 한정한 최종 보고서 결론과 같다.

선언·단위 미완 항목은 SwashModule1 판독 기록과 현재 선언부·대입식으로 해결했다. kinvis의 단위는 dynvis/rhow의 차원으로 확인했다. cvm의 무차원 성질은 체적비와 유속 갱신식으로 확인했다. iporos·ihydro는 물리 단위가 없는 정수 선택자다. 층별 식의 k−1 경계는 위쪽이다. k=1이 맨 위층이라는 SWASH 규약과 충돌하는 대상 줄은 없다. A·E 행은 없다. 상대 링크는 모두 존재한다. mermaid·절대 경로·이중 대괄호 링크·미완 항목은 없다.

삭제 줄의 근거: frontmatter는 판독 내용을 보존했다. ppor(2)의 사용처 추정 문장은 SI2-087·SI2-106 수정안의 선언부·입력부 근거로 바뀌었다. 기존 경고 문장의 나머지 네 변수도 이번 판독과 원문 대조로 해결했다. 선언·단위 확인을 다음 작업으로 남기지 않았다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| swash-vegetation-porosity.md:7 | 정정 | 식생 보정식 684 및 u점 계수 338–340 → 보정식 694–695 및 s점·u점 식 구별 | `src/SwashVeget.ftn90:684`는 분기문이다. 보정식은 645–646·694–695줄이다. `src/SwashPorousStruc.ftn90:338–340`은 apors/bpors/cpors이다. 354–356줄은 aporu/bporu/cporu이다. |
| swash-vegetation-porosity.md:113 | 보완 | HEIGHT 기본값 99999만 표기 → m 단위와 매뉴얼 인용 추가 | swashuse PDF p.81은 바닥 기준 높이의 단위 m와 기본값 99999를 함께 명시한다. `src/SwashReadInput.ftn90:968`과 같다. |
| swash-vegetation-porosity.md:114 | 보완 | 파주기 사용처만 인용 → 대표 파주기의 선언과 s 단위 근거 추가 | `src/SwashModule1.ftn90:538`, `src/SwashPorFricDep.ftn90:80`, `src/SwashPorFricLay.ftn90:83`, swashuse PDF p.81. |
| swash-vegetation-porosity.md:131 | 정정 | kinvis 정의가 다른 모듈에 있다는 경고 → 선언 위치를 명시한 사실 문장 | `src/SwashModule1.ftn90:250,421`. 식의 Van Gent 출처는 `src/SwashPorousStruc.ftn90:44–55`에 명시되어 있다. |
| swash-vegetation-porosity.md:238 | 보완 | 높이 정의·기본값의 보고서 링크만 있음 → 선언부·입력부 직접 인용 추가 | `src/SwashModule1.ftn90:533–535`, `src/SwashReadInput.ftn90:968`. |
| swash-vegetation-porosity.md:240 | 정정 | kinvis 선언·단위 source-needed → real 동점성 변수·dynvis/rhow·m²/s | `src/SwashModule1.ftn90:250,421`, `src/SwashCheckPrep.ftn90:918`. swashuse PDF p.34의 kg/(m·s)를 kg/m³로 나누면 m²/s이다. |
| swash-vegetation-porosity.md:241 | 정정 | cvm 선언·단위 source-needed → real 식생 부가질량 계수·무차원 | `src/SwashModule1.ftn90:593`, `src/SwashVeget.ftn90:185–188`, `src/SwashExpDep1DHflow.ftn90:721`. swashuse PDF p.82는 added mass coefficient를 명시한다. |
| swash-vegetation-porosity.md:242 | 정정 | iporos 선언·단위 source-needed → 단위 없는 integer 선택자 0/1 | `src/SwashModule1.ftn90:476–478`. 0은 비활성이다. 1은 활성이다. |
| swash-vegetation-porosity.md:243 | 정정 | ihydro 선언·단위 source-needed → 단위 없는 integer 선택자 0–3 | `src/SwashModule1.ftn90:614–618`. 정수압·box·표준 수직 이산화·압력층 box의 순서이다. |
| swash-vegetation-porosity.md:255 | 정정 | switch.pl 뒤에 !VEGE만 인용하고 cvm 외부 조건 생략 → 접두어 제거 규칙의 부재와 식생 활성 조건 명시 | `switch.pl:1–24,57–67`에는 VEGE 선택·제거 규칙이 없다. `src/SwashReadInput.ftn90:1305,1347–1352`는 활성 코드다. `src/SwashCheckPrep.ftn90:771`이 cvm 보정의 외부 조건이다. 침전물 인용도 해당 `.not.lmixt` 분기인 803·812–819줄로 맞췄다. SG1-886의 C 분류는 유지했다. |
| swash-vegetation-porosity.md:258 | 보완 | SI1-222의 현재 동작 결론만 있음 → 최종본의 과거 커밋 근거 추가 | `8756667:src/SwashCheckPrep.ftn90:1877`의 `nporf(indx) = max( n, 0.1 )`. 현재 2351줄과 같다. AD 최종 판정은 문서 오기 B이다. |

기계 확인 후보 판정: `switch.pl:57–66` 뒤의 `!VEGE`는 실제 인용 오류다. 지정한 원문에는 이 토큰을 제거하는 규칙이 없다. 최종 보고서 SG1-886은 제거 규칙의 부재를 설명한다. 노트에서 빠진 부정 설명을 255줄에 복원했다.

## 최종 집계

| 노트 | 시작 시점 추가 줄 | 삭제 근거를 대조한 줄 | 추가 줄 밖에서 해결한 기존 미완 줄 | 정정 줄 | 보완 줄 |
|---|---:|---:|---:|---:|---:|
| swash-input-parsing-check.md | 136 | 11 | 0 | 5 | 1 |
| swash-architecture-source-map.md | 51 | 14 | 0 | 6 | 1 |
| swash-grid-oceanpack-infra.md | 33 | 2 | 1 | 3 | 6 |
| swash-vegetation-porosity.md | 24 | 3 | 1 | 7 | 4 |
| 합계 | 244 | 30 | 2 | 21 | 12 |

마지막 줄의 대조 수는 시작 시점 git diff의 추가 줄 합계이다. 삭제 30줄과 기존 미완 2줄은 별도 열로 집계했다. 정정·보완 수는 이번 검증 태그가 붙은 수정 후 노트 줄 수이다. 미완 변수 한 줄을 네 사실 줄로 바꾼 경우 정정 4줄로 센다. 정정과 보완을 중복 집계한 줄은 없다.

차이 표 125행의 분류는 최종 보고서와 모두 같다. E 행 세 개의 강함 판정은 E1 보고서와 같다. 결론 문장의 실질 변경은 SG1-033의 momskip 조건, SI1-706의 STPNOW 대입 순서, ST2-420의 MPI 초기화·오류 조건, SG1-886의 식생 활성 조건이다. 네 변경의 원문 근거는 위 정정 목록에 적었다. 나머지 결론 문장은 서식·경로 전개·검증 태그를 제외하면 최종 보고서와 같다. SG1-875의 문서 쪽 번호 오류도 쪽 이미지로 바로잡았다.

기계 확인 후보는 19건이다. 과거 커밋·수정 전 노트·범위 인용에 따른 오판은 18건이다. 부정 설명이 빠진 !VEGE 인용 정정은 1건이다. 각 후보의 판정은 노트별 기록에 한 줄씩 적었다.

네 노트의 frontmatter는 YAML 파싱을 통과했다. 상대 링크의 대상 파일은 모두 존재한다. 네 노트에는 mermaid 블록이 없다. 절대 홈 경로와 이중 대괄호 링크가 없다. 미완 항목과 빌드·실행 검증 할 일은 없다. `git diff --check`는 통과했다. 미해결 항목은 없다.

대조 244, 정정 21, 보완 12
