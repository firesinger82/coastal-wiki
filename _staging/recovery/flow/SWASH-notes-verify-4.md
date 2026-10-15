# SWASH 노트 추가·수정 줄 전수 대조 4

검증일: 2026-10-15.

대상은 사용자 지정 노트 3개이다.
기존 노트는 작업 시작 시 `git diff -U0 HEAD -- <노트>`의 추가 줄을 대조한다.
새 파일 `swash-build-run-differences.md`는 전체 줄을 대조한다.
삭제 줄은 최종 보고서의 수정 근거와 대조한다.
빈 줄과 frontmatter도 줄 수에 포함한다.
정정 수와 보완 수는 각각 수정한 원래 줄의 수로 센다.
한 줄에서 사실·링크·인용을 함께 고치면 정정으로 센다.
노트별 완료 기록은 아래에 덧붙인다.

현재 상태: 대상 줄 전수 대조 완료.

## 1. swash-tech-ch2-ch5-mimetic-conservation.md — 완료

노트: `models/SWASH/manual-notes/swash-tech-ch2-ch5-mimetic-conservation.md`.
대조 133줄, 정정 5줄, 보완 2줄이다.
삭제 25줄도 최종 보고서의 수정안과 대조했다.
이 절의 줄 번호는 정정 후 노트의 줄 번호다.
이번 정정으로 줄 수는 바뀌지 않았다.

대상 줄은 6–7, 16–23, 25, 27–34, 36, 38–40, 42, 44–56, 58, 60, 63–79, 85, 89–164다.
빈 줄·제목·표 머리글을 포함하여 이 범위 전체를 확인했다.
차이 표 57행은 배정표 `SWASH-note-job-6.tsv`와 대조했다.
각 행의 분류와 결론은 theory-framework·theory-unstructured 보고서 §5 및 마지막 전수 검증 기록과 대조했다.
표의 코드 인용은 현재 원문과 대조했다.
ST1-245의 과거 코드 인용은 `8756667`의 `SwashCheckPrep.ftn90:1244–1248` 및 `SwashUpdateDepths.ftn90:175–192`와 대조했다.
식·숫자·보존 조건은 swashtech의 해당 PDF 쪽 이미지 및 쪽별 판독 기록과 대조했다.
frontmatter의 문서 버전·작성일·쪽수는 PDF 메타데이터와 대조했다.
상대 링크는 노트 위치에서 실제 파일로 연결된다.
금지된 절대 경로와 이중 대괄호는 없다.
mermaid 블록은 없다.
해결된 판독 작업을 미완으로 남기는 문장은 없다.
매뉴얼 자체의 빈 장·준비 중 문장은 원문 상태를 설명하는 사실이다.

### 정정·보완 목록

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| swash-tech-ch2-ch5-mimetic-conservation.md:40 | 보완 | Arakawa C-grid 및 primal/dual staggering 근거 `PDF p.17` → `PDF p.17,53–54` | swashtech p.17의 Arakawa–Lamb 설명, p.53의 staggering 유도, p.54 Figure 2.8의 primal outer·dual inner 배치. |
| swash-tech-ch2-ch5-mimetic-conservation.md:42 | 정정 | §2.6.2 `PDF p.53–61, 인쇄 45–53` → `PDF p.54–61, 인쇄 46–53` | swashtech p.53은 §2.6.1이다. §2.6.2는 p.54에서 시작한다. |
| swash-tech-ch2-ch5-mimetic-conservation.md:44 | 정정 | Eq. 2.22의 `\varphi` → `\phi` | swashtech p.55 식 (2.22), theory-framework ST1-220. |
| swash-tech-ch2-ch5-mimetic-conservation.md:69 | 정정 | `전역 보존은 균일 수심(∇d=0)에서만` → `평탄한 바닥(∇d=0)과 외력 부재`를 증명의 전제로 명시하고 경계 운동량 플럭스 수지를 명시 | swashtech p.86의 uniform bed 및 경계 적분식, theory-unstructured ST2-081·084. `d`는 바닥 수심이고 총수심 `h`와 다르다. |
| swash-tech-ch2-ch5-mimetic-conservation.md:92 | 정정 | 제4장의 상태만 기재 → 제1장 §1.1·제9·12장의 준비 중 상태와 제8장의 빈 장 상태도 복원 | swashtech p.9,65,109,111,117. ST1-318·ST2-141 수정안에는 이 사실 목록을 삭제할 근거가 없다. |
| swash-tech-ch2-ch5-mimetic-conservation.md:96 | 정정 | `경계조건 이론은 문서 밖` → 제2장이 설명을 제10장으로 미룬 사실과 제10장의 준비 중 문장을 각각 기재 | swashtech p.19의 Chapter 10 안내, p.113의 준비 중 문장. |
| swash-tech-ch2-ch5-mimetic-conservation.md:160 | 보완 | `아래 행렬식 검산` → theory-unstructured §2.8의 실제 검산 문단 링크 | `swash-theory-unstructured-vs-code.md` §2.8, ST2-169–173 뒤 검산 문단. swashtech p.102의 인쇄 행렬과도 대조했다. |

### 삭제 줄 판정

삭제 줄 번호는 HEAD의 번호다.
6행의 페이지 규약 변경은 ST1-311의 PDF 쪽수 지시와 일치한다.
15행의 완전 보존 표현 변경은 ST1-312·ST2-099의 조건 명시 지시와 일치한다.
17,19–23,25,27–29,31,33–36,38,40,43–45행은 ST1-311–317·ST2-048·099·103·105의 페이지·가중치·경계·보존 조건 수정 근거와 대조했다.
51행의 후속 대상 문장은 이번 제6·7장 판독과 ST2-141의 반영으로 대체되었다.
55행의 완결 표현은 ST1-318에 따라 제거되었다.
55행에 함께 있던 실제 빈 장 목록에는 삭제 근거가 없어서 현재 92행에 복원했다.
56행의 제10장 공백 사실은 유지했다.
56행에서 유래한 문서 전체에 대한 단정은 현재 96행에서 원문 범위로 정정했다.

### 기계 확인 후보 판정

- `src/SwashCheckPrep.ftn90:1244` 뒤 `과 `: 오탐이다. 현재 139행의 과거 커밋 인용이다. `8756667`의 1244–1248행에 조건과 분기가 있다. 인접 한국어를 코드 인용으로 읽은 결과다.
- `src/SwashUpdateDepths.ftn90:187` 뒤 `에도 이 선택과 산술평균이 있다. 문서 문장은 `: 오탐이다. 현재 139행의 과거 커밋 인용이다. `8756667`의 187행에 `hum(nm) = 0.5 * ( hs(nm) + hs(nmu) )`가 있다.
- `manual-notes/swash-tech-ch2-ch5-mimetic-conservation.md:6`의 페이지 규약 인용: 오탐이다. 현재 140행의 ST1-311이 인용한 수정 전 HEAD 6행과 일치한다.
- 같은 노트 `:15`의 설계 원리 인용: 오탐이다. 현재 141행의 ST1-312가 인용한 수정 전 HEAD 15행과 일치한다.
- 같은 노트 `:22`의 `div = -gradᵀ` 인용: 오탐이다. 현재 142행의 ST1-313이 인용한 수정 전 HEAD 22행과 일치한다.
- 같은 노트 `:36`의 에너지 보존 3조건 인용: 오탐이다. 현재 143행의 ST1-315가 인용한 수정 전 HEAD 36행과 일치한다.
- 같은 노트 `:55`의 완결 인용: 오탐이다. 현재 144행의 ST1-318이 인용한 수정 전 HEAD 55행과 일치한다.

누계: 대조 133, 정정 5, 보완 2.

## 2. swash-build-run-differences.md — 완료

노트: `models/SWASH/manual-notes/swash-build-run-differences.md`.
새 파일의 1–53행 전체를 대조했다.
대조 53줄, 정정 0줄, 보완 0줄이다.
삭제 줄은 없다.

frontmatter 1–18행의 파일 정보와 관련 경로를 확인했다.
19–32행의 제목·출처·쪽 규약·판 정보·표 머리글을 확인했다.
판 정보는 git AD 보고서 §1의 문서 기준과 코드 기준에 일치한다.
33–53행의 차이 표 21행은 배정표 `SWASH-note-job-6.tsv:58–78` 및 guide-syntax-build·theory-unstructured의 §5와 대조했다.
분류와 결론 문장은 최종 전수 검증 기록이 반영된 보고서와 일치한다.
SG1-795의 E 중간과 SG1-796의 E 강함은 git E2 보고서의 조건·반대 경로와 일치한다.
현재 코드 근거는 원자료 README·CMakeLists·src/CMakeLists·Makefile·switch.pl·clobber.cmake·Unix/Windows 실행 스크립트·machinefile·swanparll·ocpmix·SwashModule1의 해당 줄과 대조했다.
FindMPI의 인용은 로컬 `/usr/share/cmake-3.28/Modules/FindMPI.cmake:44–61,104–108`과 대조했다.
과거 코드 근거는 `8756667`, `25c79e7`, `7949227`, `7a02da1`, `ba5b15d`, `a486d5f`의 인용 파일과 대조했다.
매뉴얼 제12장의 상태는 swashtech PDF p.117 판독 기록의 원문과 일치한다.
기계 후보를 포함하여 원문과 다른 인용은 없다.
상대 링크 9개는 실제 파일로 연결된다.
금지된 절대 경로와 이중 대괄호는 없다.
mermaid 블록과 미완 작업 문장은 없다.
정정·보완 목록은 해당 없음이다.

### 기계 확인 후보 판정

- `README.md:55`의 Perl 문장: 오탐이다. 노트 33행의 인용은 원자료 `raw/source_code/swash/README.md:55`의 전체 문장과 일치한다.
- `README.md:66`의 ANSI Fortran90 문장: 오탐이다. 노트 34행의 인용은 원자료 README 66행과 일치한다. 컴파일러 목록도 67–73행과 일치한다.
- `src/CMakeLists.txt:15` 뒤 `의 switch.pl 호출과 `: 오탐이다. 노트 35행은 `8756667`의 15행을 인용한다. 해당 과거 원문에 switch.pl 호출이 있다. 현재 호출 위치는 19행이다.
- 첫 번째 `README.md:177`의 `cmake .. -GNinja -DMPI=ON`: 오탐이다. 노트 37행의 인용은 원자료 README 177행과 일치한다.
- 두 번째 `README.md:177`의 같은 명령: 오탐이다. 노트 38행의 인용도 원자료 README 177행과 일치한다.
- `README.md:203`의 `cmake -P clobber.cmake`: 오탐이다. 노트 38행의 인용은 원자료 README 203행과 일치한다.
- `README.md:88`의 `mkdir build && cd build`: 오탐이다. 노트 39행의 인용은 원자료 README 88행과 일치한다.

누계: 대조 186, 정정 5, 보완 2.

## 3. swash-nonhydrostatic-pressure-solver.md — 완료

노트: `models/SWASH/source-analysis/swash-nonhydrostatic-pressure-solver.md`.
대조 36줄, 정정 5줄, 보완 0줄이다.
삭제 10줄도 보고서의 수정안과 대조했다.
이 절의 줄 번호는 정정 후 노트의 줄 번호다.
이번 정정으로 줄 수는 바뀌지 않았다.

대상 줄은 6–7, 52–53, 59, 75–81, 86, 89, 91–112다.
빈 줄·제목·표 머리글을 포함하여 이 범위 전체를 확인했다.
frontmatter 6행의 파일 길이 4284·5705와 Method·압력 조립·솔버·전처리 인용 위치를 실제 원문과 대조했다.
본문 52–53행의 비압축 조건은 swashtech PDF p.64 및 ST1-326과 일치한다.
59,75–81행의 구조·비구조 솔버 구분은 실제 호출과 ST1-327·ST2-225 수정안에 일치한다.
swashuse PDF p.92,99–101의 이미지에서 압력 BiCGSTAB와 수위 PCG·Newton의 설명을 확인했다.
93–97행의 theta 처리와 시간 방법 선택은 입력·준비·호출·소비 코드 및 SI2-181·SG1-101과 일치한다.
108–112행의 차이 표 5행은 배정표 `SWASH-note-job-7.tsv:80–84` 및 최종 보고서 §5와 일치한다.
SI2-181의 E 강함은 git E2 판정과 일치한다.
젖은 셀·명시적 1DH·BOX 조건에서 theta=0이 분모에 들어가는 경로를 확인했다.
ST1-182·183의 Laplacian 합성식과 격자 조건은 swashtech PDF p.46 이미지 및 계수 조립 원문과 일치한다.
과거 커밋의 검사식과 tridiag 호출도 직접 열어 대조했다.
대상 줄의 상대 링크는 실제 파일로 연결된다.
금지된 절대 경로와 이중 대괄호는 없다.
mermaid 블록과 미완 작업 문장은 없다.

### 정정 목록

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| swash-nonhydrostatic-pressure-solver.md:77 | 정정 | 삭제된 층 수·분산 설명 없음 → 매뉴얼이 수직층 수를 늘려 주파수 분산을 개선한다고 설명하는 사실 복원 | swashuse PDF p.16의 `SWASH improves its frequency dispersion by increasing this number of layers`. ST1-327의 솔버 구분 수정안은 이 별도 사실을 부정하지 않는다. |
| swash-nonhydrostatic-pressure-solver.md:86 | 정정 | `Delft3D difu·SWAN·XBeach 모두 SIP 사용` 및 XBeach `α=0.94` 단정 → SWAN의 스펙트럼 5대각 SWSIP, XBeach solver_sip, SWASH의 Stone 인용을 각각 명시 | Delft3D 연결 노트 §4는 difu를 수송 해법으로 설명한다. `models/Delft3D/raw/source_code/Delft3D/src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src/compute/difu.f90:48–71,812–818`은 방향별 이산화와 연직 소거를 보여 준다. SIP 공유 계보의 근거가 아니다. `models/SWAN/raw/source_code/swan/src/swancom1.ftn:8388–8389`는 스펙트럼 5대각 SIP를 명시한다. `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/solver.F90:309–322,385–391`은 Stone SIP를 명시한다. XBeach의 40행 초기 alpha는 110행에서 입력 매개변수로 덮인다. SWASH `src/SwashSolvers.ftn90:1854–1858`은 Stone(1968)을 인용한다. |
| swash-nonhydrostatic-pressure-solver.md:91 | 정정 | `알고리즘 line-by-line`, `5705줄 전수` → 연결 노트에 솔버·전처리 개요가 정리된 사실과 원본의 루틴 목록 위치 | `swash-linear-solvers.md` §1–7은 루틴별 개요와 선택한 코드 인용을 제시한다. 이 노트의 verification_by는 특정 구간의 직접 검증으로 적혀 있다. `src/SwashSolvers.ftn90:4–23`은 루틴 목록이다. 파일의 전체 길이만으로 모든 줄의 검증을 주장하지 않는다. |
| swash-nonhydrostatic-pressure-solver.md:92 | 정정 | `Keller-box 연직 이산화(tridiag 적용부)` → avm의 연직 밴드 결합과 tridiag의 수평 격자점 순회를 구분 | `src/SwashSolvers.ftn90:121–137`은 avm의 연직 결합 합산이다. `:4353–4368`은 수평 격자 배열과 x 방향 지표를 정의한다. `:4395–4422,4466–4479`는 수평 지표 m의 소거·대입이다. `src/SwashExpDep1DHflow.ftn90:1265` 및 ST1-327은 수심 평균 1DH 압력의 tridiag 호출을 확인한다. |
| swash-nonhydrostatic-pressure-solver.md:111 | 정정 | `속도장.` 뒤의 잘못 분리된 백틱과 `<br>` → 원문 인용을 닫은 뒤 정상 `<br>swashtech PDF` | theory-framework §5 ST1-326(752행)의 원문 인용과 줄바꿈을 복원했다. 결론 분류와 결론 문장은 유지했다. |

### 삭제 줄 판정

삭제 줄 번호는 HEAD의 번호다.
6행은 기존 검증 방법을 보존하면서 recovery 반영 기록을 추가했다.
51행의 divergence-free 요약은 ST1-326의 국소 비압축 조건 설명으로 대체되었다.
57행의 `depth-averaged 기본`은 ST1-327에 따라 구조 2D로 한정되었다.
73행의 Dep/Lay 일괄 구분은 ST1-327·ST2-225의 격자별 호출 구분으로 대체되었다.
73행의 층 수·분산 설명에는 삭제 근거가 없어서 현재 77행에 매뉴얼의 설명으로 복원했다.
78행의 이중 대괄호는 상대 Markdown 링크로 바뀌었다.
78행에서 유래한 SIP 공유 계보의 근거 오류는 현재 86행에서 정정했다.
81행의 TODO 제목은 완료된 근거 절의 제목으로 바뀌었다.
83–84행은 기존 링크를 상대 Markdown 링크로 바꾼 줄이다.
83–84행에서 유래한 검증 범위 과장과 연직 tridiag 표현은 현재 91–92행에서 정정했다.
85행 전체는 inputs-physics-numerics §4 SI2-181이 제시한 네 문장으로 대체되었다.
85행의 `[0.5,1] 강제` 삭제는 theta=0 통과 조건과 나눗셈 원문에 근거한다.
86행의 후속 시간적분 항목은 apply-7 기록대로 SG1-101의 방법 선택 사실로 대체되었다.

### 기계 확인 후보 판정

- `src/SwashCheckPrep.ftn90:1145` 뒤 `부터 같다. `: 오탐이다. 현재 108행은 `8756667:src/SwashCheckPrep.ftn90:1145–1157`을 인용한다. 과거 원문의 검사식·음수 보정 분기는 현재 1273–1285행과 일치한다.
- `source-analysis/swash-nonhydrostatic-pressure-solver.md:51`의 divergence-free 문장: 인용 내용의 오탐이다. 현재 111행은 수정 전 HEAD 51행을 인용하며 내용이 일치한다. 같은 셀의 별도 줄바꿈 서식 오류는 위 정정 목록대로 고쳤다.
- 같은 노트 `:73`의 Dep=SIP 요약: 오탐이다. 현재 112행의 ST1-327은 수정 전 HEAD 73행을 인용하며 내용이 일치한다.
- `src/SwashExpDep1DHflow.ftn90:933` 뒤 `에도 같은 `: 오탐이다. 현재 112행은 `8756667`의 933행을 인용한다. 해당 과거 원문에 `call tridiag ( a, b, c, d, dq, kgrpnt )`가 있다.

누계: 대조 222, 정정 10, 보완 2.

## 최종 집계

| 노트 | 대상 줄 대조 | 삭제 줄 별도 대조 | 정정 | 보완 |
|---|---:|---:|---:|---:|
| swash-tech-ch2-ch5-mimetic-conservation.md | 133 | 25 | 5 | 2 |
| swash-build-run-differences.md | 53 | 0 | 0 | 0 |
| swash-nonhydrostatic-pressure-solver.md | 36 | 10 | 5 | 0 |
| 합계 | 222 | 35 | 10 | 2 |

대상 줄 수는 작업 시작 시 기존 노트의 추가 줄 169개와 새 파일 전체 53개의 합이다.
마지막 읽기 전용 diff에서도 기존 노트의 추가·삭제 줄 수는 각각 133·25 및 36·10이다.
새 파일은 git diff 출력과 별개로 전체 53줄을 대조했다.
수정한 노트 줄 12개는 모두 최초 대상 줄에 속한다.
각 정정·보완 줄에는 지정된 전수 검증 태그가 있다.
차이 표 83행의 분류와 결론을 대조했다.
이 표들에 A 행은 없다.
E 행 3개의 강도는 최종 보고서와 같다.
기계 확인 후보 18건은 각각 원문 위치를 열어 판정했다.
18건 모두 인용 문자열 불일치의 오탐이다.
그중 ST1-326 셀의 별도 서식 오류는 정정에 포함했다.
최종 파일의 상대 링크 대상과 금지 문자열을 다시 확인했다.
대상 줄에 미완 작업 문장과 빌드·실행 검증 할 일은 없다.
대상 범위의 미해결 항목은 없다.

대조 222, 정정 10, 보완 2
