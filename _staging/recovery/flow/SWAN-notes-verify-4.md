# SWAN 노트 추가·수정 줄 전수 대조

- 작업일: 2026-10-13.
- 대상 줄은 작업 시작 시 각 대상 노트의 `git diff -U0 HEAD -- <노트>`에서 얻은 모든 `+` 줄이다.
- 줄 수에는 frontmatter, 빈 줄, 표 구분선, 코드 울타리를 포함한다.
- 정정 수와 보완 수는 해당 태그를 붙인 노트의 줄 수로 센다.
- 원문 범위는 현재 SWAN 코드, 인용된 과거 커밋, 로컬 웹 문서, 로컬 PDF, 지정된 최종 결론 보고서와 반영 기록이다.
- 노트 위치는 정정 후 줄 번호로 기록한다.

| 노트 | 상태 | 대조한 + 줄 수 | 정정 수 | 보완 수 |
|---|---|---:|---:|---:|
| `models/SWAN/manual-notes/swan-implementation-manual.md` | 완료 | 143 | 4 | 1 |
| `models/SWAN/manual-notes/swan-tech-ch2-vegetation-ice-bragg-gen12.md` | 완료 | 76 | 6 | 2 |
| `models/SWAN/source-analysis/swan-st6-babanin-implementation.md` | 완료 | 35 | 1 | 2 |
| `models/SWAN/manual-notes/swan-tech-ch8-unstructured-ops.md` | 완료 | 46 | 6 | 1 |
| `models/SWAN/manual-notes/swan-action-balance.md` | 완료 | 23 | 1 | 4 |
| 합계 | 완료 | 323 | 18 | 10 |

완료한 노트의 대조 근거와 정정 목록을 아래에 순서대로 기록한다.

## 1. swan-implementation-manual.md

작업 시작 diff의 `+` 줄 143개를 모두 대조했다.
이 수에는 frontmatter 2줄과 결론표 72행을 포함한다.
결론표 72행의 분류와 결론은 R7 §5의 최종 10-13 판정과 일치한다.
A 행의 HASH와 날짜는 `SWAN-git-verify-A.md`의 I-030·I-033·I-057·N-001·N-002·N-012·N-014 판정과 일치한다.
과거 코드 인용은 해당 `HASH:path`의 원문과 대조했다.
기존 노트 인용은 읽기 전용 `git diff -U100000 HEAD`의 삭제 줄과 문맥에서 복원한 HEAD 원문과 대조했다.

원문 대조 범위는 다음과 같다.

- `swanimp.pdf` PDF 8–11·15–22·24–29·31–35쪽의 배포 목록, 설치 조건, 전처리, CMake, 초기화, 실행 및 시험 안내.
- `swanpgr.pdf` PDF 51쪽의 문서 판 이력.
- `website/online_doc/swanimp/node1·5·10·11·13·19·20·21.html`의 인용 문장과 문맥.
- `website/online_doc/swanuse/node47·49.html`의 편집용 구문표 설명.
- `website/problems_and_fixes/patches/41.51.A:123,366–368,390–391`.
- SWAN 저장소의 `README.md`, `CMakeLists.txt`, `src/CMakeLists.txt`, `Makefile`, `switch.pl`, `bin/swanrun`, `bin/swanrun.bat`의 인용과 조건 분기.
- `src/ocpids.ftn:193,494–546`, `src/swanmain.ftn:965–968`, `src/swanser.ftn:5852,7397–7398`, `src/swanpre1.ftn:637–642`, `src/swanparll.ftn:2263–2294`, `src/SwanParallel.ftn90:481–483`, `src/SwanCompUnstruc.ftn90:823–849`, `src/srclist.cmake:1–17`, `misc/swan.edt`, `misc/machinefile`.
- R7 §4·§5, `SWAN-git-verify-A.md`, `SWAN-git-verify-D.md:65,68`, `SWAN-notes-apply-7.md`의 해당 노트 반영 기록.

상대 링크 17개는 모두 실제 파일을 가리킨다.
이 수는 노트 전체의 Markdown 파일 링크를 센 값이다.
대상 줄에 mermaid 상자는 없다.
대상 줄에 개인 절대경로, 이중 대괄호 링크, 한계 문장은 없다.
정정 후 읽기 전용 `git diff --check HEAD -- <노트>`를 통과했다.

### 정정·보완 목록

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `swan-implementation-manual.md:112` | 정정 | `first 3 or 4 columns`의 PDF 19쪽 / 인쇄 13쪽 → PDF 18쪽 / 인쇄 12쪽 | `swanimp.pdf` PDF 18쪽의 `an indentifiable prefix in the first 3 or 4 columns`. HTML은 `swanimp/node10.html:49–50`. |
| `swan-implementation-manual.md:188` | 정정 | `src/CMakeLists.txt:71`의 조건문 인용 → `src/CMakeLists.txt:72` | 71행은 주석이다. 72행은 `if( OPENMP AND MPI )`이다. |
| `swan-implementation-manual.md:209` | 정정 | 형식 3의 `05/30/87` 및 형식 5의 `87/05/30` → 두 예시에 `15:30:00` 복원 | `swanimp/node19.html:119,123`은 각각 `05/30/87  15:30:00`, `87/05/30  15:30:00`이다. `src/ocpids.ftn:520–521,533`도 시·분·초를 읽는다. |
| `swan-implementation-manual.md:247` | 보완 | 기존 노트 줄 번호의 기준 미표시 → 반영 전 HEAD 기준 명시 | 읽기 전용 diff에서 복원한 HEAD의 76·83·141·145·148행 등이 표의 기존 노트 인용과 일치한다. |
| `swan-implementation-manual.md:307` | 정정 | N-007의 PDF 19쪽 / 인쇄 13쪽 → PDF 18쪽 / 인쇄 12쪽 | `swanimp.pdf` PDF 18쪽의 `first 3 or 4 columns`. R7의 분류 F와 결론은 유지한다. |

### 기계 확인 후보 판정

- `README.md:35` 후보: 오판이다. SWAN 저장소 README 35행에 `The SWAN software can be used freely under the terms of the [GNU General Public License]`가 있다.
- `README.md:245` 첫 후보: 오판이다. README 245행은 `1. **serial**: for computers using one processor (recommended for small tests)`이다. 노트 I-045의 인용을 유지했다.
- `README.md:134` 후보: 오판이다. README 134행에 관리자 권한 없이 설치할 수 있다는 괄호 문장과 뒤의 사용자 지정 디렉터리 문장이 있다.
- `README.md:63` 후보: 오판이다. README 63행에 `Due to the use of ANSI standard Fortran90`으로 시작하는 인용 문장 전체가 있다.
- `README.md:266` 후보: 오판이다. README 266행은 `mpirun -np <n> swan.exe`이다.
- `swan-implementation-manual.md:76` 후보: 오판이다. 반영 전 HEAD 76행은 `make config        # macros.inc 생성 (1회, 필수 선행)`이다. 표는 기존 노트 문구를 인용한다.
- `swan-implementation-manual.md:83` 후보: 오판이다. 반영 전 HEAD 83행에 Windows Nmake·Intel Fortran·Intel MPI 문구가 있다. 현재 본문은 classic 설치 안내로 범위를 구분한다.
- `swan-implementation-manual.md:141` 후보: 오판이다. 반영 전 HEAD 141행에 `CMake 3.12+`와 Ninja 권장 문구가 있다. 현재 본문은 CMake 3.20을 적는다.
- `swan-implementation-manual.md:145` 후보: 오판이다. 반영 전 HEAD 145행에 `mkdir build && cd build`와 `src 비오염` 주석이 있다. 표는 이 기존 오기를 인용한다.
- `swan-implementation-manual.md:148` 후보: 오판이다. 반영 전 HEAD 148행에 `/usr/local/swan`과 `C:\PROGRAM FILES\swan`이 있다. 현재 본문은 사용자 폴더 기본값을 적는다.
- `README.md:245` 재등장 후보: 오판이다. N-021도 같은 README 245행을 인용한다. 해당 원문과 일치하므로 유지했다.

이 노트의 미해결 항목은 없다.

## 2. swan-tech-ch2-vegetation-ice-bragg-gen12.md

작업 시작 diff의 `+` 줄 76개를 모두 대조했다.
이 수에는 frontmatter 2줄과 결론표 20행을 포함한다.
결론표 20행의 분류는 R2 §5의 최종 판정과 일치한다.
결론 문장은 보고서의 의미와 일치한다.
SS-129에는 코드와 사용자 매뉴얼이 명시한 기본 설정 조건을 보탰다.
이 노트의 결론표에는 A 행과 과거 커밋 인용이 없다.

원문 대조 범위는 다음과 같다.

- `swantech.pdf` PDF 52–60쪽 / 인쇄 44–52쪽의 (2.108)–(2.130), 식생 그림 2.3, 무번호 해빙식과 Jacobsen 식.
- `swantech.pdf` PDF 30쪽의 (2.46)·(2.47).
- `swanuse.pdf` PDF 65–66·77·79쪽의 GEN1·GEN2·GEN3·식생·BRAGG 명령과 기본 계수.
- `src/swancom1.ftn:5877–5881,6022–6024,7365–7368`의 평균 주파수·파수와 SVEG 전달.
- `src/swancom2.ftn:762–763,851–921,945–993,1542–1557`의 식생 분모·누적 층 높이·부분층·깊은 물 조건·Simpson 구간 수·해빙 주파수 단위.
- `src/swancom3.ftn:369–513`의 포화 스펙트럼, 무차원 수심·에너지 제한, 성장·완화 분기, 해빙 배율.
- `src/swancom4.ftn:4747–4800`, `src/swanmain.ftn:965,1459–1468`, `src/swanpre1.ftn:2639–2658,2817–2822,2843–2858`.
- `src/SwanBraggScat.ftn90:38`, `src/SwanIEM.ftn90:38`, `src/SwanQCM.ftn90:38`, `src/SwanVTKWriteHeader.ftn90:36`의 내부 변경 번호와 날짜.
- R2 §4·§5의 해당 행과 `SWAN-notes-apply-2.md`의 담당 노트 기록.
- 기존 노트 인용은 읽기 전용 diff에서 복원한 HEAD 64·72·74·217·255·262행.

상대 파일 링크 16개는 모두 실제 파일을 가리킨다.
이 수는 노트 전체에서 수식의 대괄호·소괄호를 링크 후보에서 제외한 값이다.
대상 줄에 mermaid 상자는 없다.
대상 줄에 개인 절대경로, 이중 대괄호 링크, 한계 문장은 없다.
정정 후 읽기 전용 `git diff --check HEAD -- <노트>`를 통과했다.

### 정정·보완 목록

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `swan-tech-ch2-vegetation-ice-bragg-gen12.md:7` | 정정 | 식 (2.108)–(2.130) 모두 `LaTeX verbatim` → 인쇄식·동치 전사·구현 차이를 구분한 대조 | PDF 58쪽의 (2.119)는 `β1/(2π) × π/g²`이다. 노트 233행은 동치식 `β1/(2g²)`이다. R2:SS-725도 이 동치식을 지시한다. |
| `swan-tech-ch2-vegetation-ice-bragg-gen12.md:294` | 정정 | 항상 `[10^-25,.0036]`으로 제한한다는 서술 → GEN2의 기본 설정에서 적용하는 범위 | `swancom3.ftn:396–397`의 상한은 `PWIND(10)`이다. `swanmain.ftn:1467`의 기본값은 `.0036`이다. `swanpre1.ftn:2857`은 사용자 `EDMLPM`을 읽는다. |
| `swan-tech-ch2-vegetation-ice-bragg-gen12.md:323` | 보완 | Bragg 내부 변경 번호·날짜의 직접 인용 없음 → 소스 주석 추가 | `SwanBraggScat.ftn90:38`: `!   41.80, September 2021: New module`. |
| `swan-tech-ch2-vegetation-ice-bragg-gen12.md:324` | 정정 | IEM `41.85`의 번호 성격 미표시 → 내부 변경 번호 명시 | `SwanIEM.ftn90:38`: `!   41.85, January 2019: New module`. 배포판 선언은 `swanmain.ftn:965`의 `VERNUM = 41.51`이다. |
| `swan-tech-ch2-vegetation-ice-bragg-gen12.md:325` | 정정 | QCM `41.90`의 번호 성격 미표시 → 내부 변경 번호 명시 | `SwanQCM.ftn90:38`: `!   41.90, June 2021: New module`. |
| `swan-tech-ch2-vegetation-ice-bragg-gen12.md:327` | 정정 | VTK `41.95`의 번호 성격 미표시 → 내부 변경 번호 명시 | `SwanVTKWriteHeader.ftn90:36`: `!   41.95, July 2022: New subroutine`. |
| `swan-tech-ch2-vegetation-ice-bragg-gen12.md:398` | 보완 | 결론의 AI 해석 및 기존 노트 줄 번호 기준 미표시 → R2의 AI 해석과 반영 전 HEAD 기준 명시 | R2 §5는 각 결론을 `해석:`으로 표시한다. HEAD의 해당 기존 노트 줄은 표의 인용과 일치한다. |
| `swan-tech-ch2-vegetation-ice-bragg-gen12.md:415` | 정정 | SS-129의 범위 문장에 기본 설정 조건 없음 → GEN2의 기본 설정 명시 | `swancom3.ftn:396–397`, `swanmain.ftn:1467`, `swanpre1.ftn:2857`, `swanuse.pdf` PDF 65–66쪽. 분류 C는 유지한다. |

사용자가 지정한 기계 확인 후보는 이 노트에 없다.
링크 검사에서 생긴 `(2/\pi)` 후보는 수식 (2.126)의 일부이므로 링크가 아니다.
이 노트의 미해결 항목은 없다.

## 3. swan-st6-babanin-implementation.md

작업 시작 diff의 `+` 줄 35개를 모두 대조했다.
이 수에는 frontmatter 2줄과 결론표 13행을 포함한다.
결론표의 분류와 결론은 R2·R5 최종 판정과 일치한다.
이 노트의 결론표에는 A 행과 과거 SWAN 커밋 인용이 없다.

원문 대조 범위는 다음과 같다.

- `swantech.pdf` PDF 33쪽 / 인쇄 25쪽의 ST6 설명.
- `swanuse.pdf` PDF 67–71쪽 / 인쇄 59–63쪽의 ST6 설정·계수·SSWELL·NEGATINP와 PDF 138쪽 / 인쇄 130쪽의 부록 구문.
- `website/online_doc/swanuse/node28.html:736–748`.
- `src/SdsBabanin.ftn90:168–259,543–660,686–727,924–1001,1098–1162,1324–1361,1500–1529,1850–1892,2019–2039,2150–2212`의 조건·수식·단위·주석 표지.
- `src/swanmain.ftn:1376–1390`, `src/swanpre1.ftn:2983–3024,3115–3142`, `src/swancom1.ftn:6823–6875,7416–7436,7480–7540`, `src/swancom2.ftn:2829–2859`.
- `SWAN-external-sources.md` §3과 그 저장 원문 `ext/ww3man.pdf` PDF 62–63쪽 / 인쇄 54–55쪽, `ext/swld.F90:379–415`.
- R2 §5의 SS-529–537·SS-733–735와 R5 §5의 PN-185.
- 기존 노트 인용은 읽기 전용 diff에서 복원한 ST6 HEAD 67·68·117·120·124행과 whitecapping HEAD 128행.

WW3 식 (2.143)·(2.144), 표 2.8의 기본값, W3SWL6의 ANAR·BN·DDIS 인용은 저장된 외부 원문과 일치한다.
음의 입력과 감소 인자의 적용 순서는 `SdsBabanin.ftn90:702,724`와 일치한다.
`!NRL` 주석 종료와 `ISOL==0` 내부의 활성 NaN 종료는 서로 다른 경로이다.
상대 파일 링크 5개는 모두 실제 파일을 가리킨다.
대상 줄에 mermaid 상자는 없다.
대상 줄에 개인 절대경로, 이중 대괄호 링크, 검증 한계 문장은 없다.
정정 후 읽기 전용 `git diff --check HEAD -- <노트>`를 통과했다.

### 정정·보완 목록

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `swan-st6-babanin-implementation.md:6` | 정정 | 검증 방법 필드의 과거 마이그레이션 경로·커밋 설명 → 이번 SWAN·PDF·R2·R5·WW3 원문 대조 범위 | 이 절에 열거한 원문을 실제 대조했다. 검증 방법과 과거 문서 작성 이력을 분리했다. |
| `swan-st6-babanin-implementation.md:117` | 보완 | 계수 생략 가능 주장에 초기값 대입만 인용 → `UNC` 입력 처리도 인용 | `swanpre1.ftn:2992–2993`은 A1SDS·A2SDS에 `CALL INREAL (..., 'UNC', 0.)`를 사용한다. 초기값은 `swanmain.ftn:1376–1377`이다. |
| `swan-st6-babanin-implementation.md:149` | 보완 | 결론의 AI 해석 및 기존 노트 줄 번호 기준 미표시 → R2·R5의 AI 해석과 반영 전 HEAD 기준 명시 | R2 §5의 결론 문장은 `해석:`을 붙인다. 기존 노트 인용은 HEAD의 해당 줄과 일치한다. |

### 기계 확인 후보 판정

- `swancom1.ftn:6875`의 `SOURCE` 후보: 오판이다. 6875행은 `USE SdsBabanin`이다. 이 행은 6823행에서 시작하는 `SUBROUTINE SOURCE` 안에 있다. 노트는 6875행을 SOURCE 선언으로 인용하지 않고 SOURCE 내부의 모듈 사용문으로 설명한다.

이 노트의 미해결 항목은 없다.

## 4. swan-tech-ch8-unstructured-ops.md

작업 시작 diff의 `+` 줄 46개를 모두 대조했다.
이 수에는 frontmatter 2줄과 결론표 9행을 포함한다.
결론표 9행의 분류와 결론은 R1 §5의 최종 판정과 일치한다.
이 노트의 결론표에는 A 행과 과거 커밋 인용이 없다.

원문 대조 범위는 다음과 같다.

- `swantech.pdf` PDF 148–155쪽 / 인쇄 140–147쪽의 역기저, 보간, 힘, 확산항, 작용 보존식.
- `swantech.pdf` PDF 64–65·81–83·116쪽의 회절 식 번호, GSE 확산항과 안정성 식, radiation stress 식.
- `website/online_doc/swantech/node93–96.html`의 장별 식 번호와 `node95.html:74,76,79–91`의 교차 참조·셀 중심 설명.
- `website/online_doc/swantech/node29.html:126–133,151–164`와 `node38.html:467–478`의 식과 번호.
- `src/SwanGridCell.ftn90:143–180`, `src/SwanTranspX.ftn90:103–138`, `src/SwanGSECorr.ftn90:125–274`, `src/SwanInterpolatePoint.ftn90:123–246`.
- `src/SwanComputeForce.ftn90:153–165,203–230,278–288`, `src/SwanDiffPar.ftn90:250–259,317–320`, `src/swancom5.ftn:2916–2935,3000–3017`.
- R1 §4·§5와 `SWAN-notes-apply-2.md:24`, `SWAN-notes-apply-3.md:49`의 반영 기록.

식 (8.29)의 행렬과 노트의 전사는 일치한다.
수정된 법선 관계와 중복 면적 인자 설명은 역기저 정의와 일치한다.
제8장 식 (8.17)–(8.45)의 PDF·HTML 번호는 일치한다.
다른 장을 가리키는 교차 참조의 PDF·HTML 번호는 별도로 정정했다.
상대 파일 링크 12개는 모두 실제 파일을 가리킨다.
대상 줄에 mermaid 상자는 없다.
대상 줄에 개인 절대경로, 이중 대괄호 링크, 한계 문장은 없다.
정정 후 읽기 전용 `git diff --check HEAD -- <노트>`를 통과했다.

### 정정·보완 목록

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `swan-tech-ch8-unstructured-ops.md:82` | 정정 | GSE 확산항을 PDF 식 (3.13)으로 지칭 → PDF의 무번호 확산항과 HTML 식 (3.13) 구분 | `swantech.pdf` PDF 82쪽의 확산항은 무번호이다. PDF 83쪽의 (3.13)은 안정성 지표 Q의 식이다. `node38.html:467–478`은 확산항을 (3.13)으로 표시한다. |
| `swan-tech-ch8-unstructured-ops.md:83` | 정정 | 회절 매개변수 PDF 식 (2.141) → PDF 식 (2.138), HTML 식 (2.180) | `swantech.pdf` PDF 64쪽의 회절 매개변수 식과 `node29.html:126–133`. PDF 65쪽의 (2.141)은 평활식이다. |
| `swan-tech-ch8-unstructured-ops.md:117` | 정정 | HTML 표시 2.181을 PDF 식 (2.141)에 대응 → 링크 표시와 실제 대상 구분 | `node95.html:76`의 표시 문자열은 2.181이다. 링크의 `eq3-44` 대상은 `node29.html:129–133`의 (2.180)이다. 그 식은 PDF 64쪽의 (2.138)이다. |
| `swan-tech-ch8-unstructured-ops.md:124` | 정정 | 관련 노트의 GSE 참조를 Eq 3.13으로만 표시 → PDF 무번호·HTML (3.13) 구분 | `swantech.pdf` PDF 82쪽 / 인쇄 74쪽과 `node38.html:467–478`. |
| `swan-tech-ch8-unstructured-ops.md:125` | 정정 | 관련 노트의 회절 참조 Eq 2.141 → PDF 식 (2.138) | `swantech.pdf` PDF 64쪽 / 인쇄 56쪽. |
| `swan-tech-ch8-unstructured-ops.md:132` | 보완 | 결론의 AI 해석 표시 없음 → R1의 AI 해석 명시 | R1 §5의 결론과 원문 인용을 구분한다. |
| `swan-tech-ch8-unstructured-ops.md:140` | 정정 | 코드에 없는 `1/(2*area)`를 직접 인용 → 실제 `asum`·`amat`·`rhs` 식 인용 | `SwanTranspX.ftn90:128,135–136`. R1:TN-223은 해당 구간에 면적 인자를 다시 곱하는 계산이 없다고 적는다. 분류 B와 결론은 유지한다. |

### 기계 확인 후보 판정

- `src/SwanTranspX.ftn90:128`의 `1/(2*area)` 후보: 실제 오류이다. 128–136행에 이 문자열은 없다. R1의 부재 설명을 존재하는 코드 인용으로 바꿔 옮긴 오류이다. 노트 140행을 실제 원문으로 정정했다.

이 노트의 미해결 항목은 없다.

## 5. swan-action-balance.md

작업 시작 diff의 `+` 줄 23개를 모두 대조했다.
이 수에는 frontmatter 2줄과 결론표 3행을 포함한다.
결론표 3행의 분류와 결론은 R2 §5의 SS-741–743 최종 판정과 일치한다.
이 노트의 결론표에는 A 행과 과거 커밋 인용이 없다.

원문 대조 범위는 다음과 같다.

- `swantech.pdf` PDF 25쪽 / 인쇄 17쪽의 식 (2.31)과 `Dtot < 0` 정의.
- `swantech.pdf` PDF 59–60쪽 / 인쇄 51–52쪽의 GEN1·GEN2 포화 스펙트럼과 완화식.
- `swanuse.pdf` PDF 65–66·69·74쪽의 GEN1·GEN2·GEN3, WESTH 기본 선택, JONSWAP 기본 계수와 단위.
- `src/swanpre1.ftn:2544–2559,2904–2907`, `src/swanmain.ftn:1396`, `src/swancom3.ftn:452–501`, `src/swancom2.ftn:2092–2125,2177–2193`.
- R2 §4·§5의 SS-741–743과 `SWAN-notes-apply-2.md:16`의 반영 기록.
- 기존 노트 인용은 읽기 전용 diff에서 복원한 HEAD 61·63·112·121·131행.

WESTH 기본 선택과 JONSWAP 계수 `.038 m²s⁻³`는 원문과 일치한다.
입력 예의 `.067`은 사용자 계수 입력 경로로 전달된다.
쇄파 식에서 앞의 음수를 제거한 전사는 매뉴얼의 음수 `Dtot` 정의와 일치한다.
상대 파일 링크 3개는 모두 실제 파일을 가리킨다.
대상 줄에 mermaid 상자는 없다.
대상 줄에 개인 절대경로, 이중 대괄호 링크, 한계 문장은 없다.
정정 후 읽기 전용 `git diff --check HEAD -- <노트>`를 통과했다.

### 정정·보완 목록

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `swan-action-balance.md:10` | 정정 | 공동 개발자의 저서라는 이유로 현행 알고리즘의 기준 문헌이라고 단정 → 이번 추가·수정 줄의 실제 원문 대조 방법 | R2:SS-741·742는 기존 노트의 모형 분류와 기본값을 현행 매뉴얼·코드에 맞춰 고친다. 저자 관계를 현행 구현 일치의 근거로 사용하지 않는다. |
| `swan-action-balance.md:63` | 보완 | GEN1·GEN2 설명에 사용자 매뉴얼만 인용 → 기술 매뉴얼의 포화 스펙트럼·완화식 추가 | `swantech.pdf` PDF 59쪽의 (2.124)–(2.127)과 PDF 60쪽의 (2.128)–(2.130). |
| `swan-action-balance.md:125` | 보완 | `.067` 입력 예에 기본값 대입만 인용 → 실제 사용자 계수 입력 처리도 인용 | `swanpre1.ftn:2556–2558`의 `CALL IGNORE ('CON')`과 `CALL INREAL('CFJON',PBOT(3),'UNC',0.)`. |
| `swan-action-balance.md:135` | 보완 | 양의 소산 크기 정의에 R2만 인용 → 원래 부호 정의가 있는 PDF 식 (2.31) 추가 | `swantech.pdf` PDF 25쪽 / 인쇄 17쪽의 `Dtot < 0`과 `Sds,br = Dtot / Etot × E`. |
| `swan-action-balance.md:243` | 보완 | 결론의 AI 해석 및 기존 노트 줄 번호 기준 미표시 → R2의 AI 해석과 반영 전 HEAD 기준 명시 | R2 §5와 읽기 전용 diff에서 복원한 HEAD의 기존 노트 문구. |

사용자가 지정한 기계 확인 후보는 이 노트에 없다.
이 노트의 미해결 항목은 없다.

## 6. 최종 확인

대조한 줄은 작업 시작 diff의 합계 323줄이다.
정정 태그를 붙인 줄은 18줄이다.
보완 태그를 붙인 줄은 10줄이다.
이 수는 위 노트별 정정·보완 목록과 대응한다.
수정 후에도 각 노트의 diff `+` 줄 수는 처음과 같다.
이번 정정·보완은 모두 처음의 대상 줄 안에 있다.
대상 줄의 누락은 없다.

결론표 117행의 분류를 보고서 최종본과 대조했다.
SS-129에는 원문에 있는 GEN2 기본 설정 조건을 명시했다.
SS-530·531·537의 경로·쪽 표기·조사 차이는 결론의 의미를 바꾸지 않는다.
자동 추출한 코드 인용 289건의 문자열 대조에서 불일치는 없다.
노트 전체의 상대 파일 링크 53개가 모두 존재한다.
대상 줄에 mermaid 상자는 없다.
frontmatter 5개는 YAML 구문 검사를 통과했다.
결론표 117행은 모두 여섯 열이다.
대상 노트의 읽기 전용 `git diff --check HEAD`는 통과했다.

사용자가 제시한 기계 후보 13건을 각각 판정했다.
실제 오류는 `SwanTranspX.ftn90:128`의 가짜 인용 1건이다.
나머지 12건은 원문 또는 반영 전 노트와 일치한다.
추가 문자열 검사에서 잡힌 ST6의 `실행하지 않는다`는 주석 처리된 코드의 동작 설명이다.
이 문장은 검증 작업의 한계 문장이 아니다.
대상 줄에 검증 한계 문장과 미해결 항목은 없다.


### 대조한 대상 줄

줄 번호는 작업 시작 시의 노트 기준이다.
이번 정정·보완에서 줄 수를 바꾸지 않았으므로 현재 줄 번호도 같다.
빈 줄과 표 구분선도 이 범위에 포함한다.

| 노트 | 대조한 `+` 줄 번호 |
|---|---|
| `swan-implementation-manual.md` | 7–8, 23–25, 31, 35, 48, 51, 61–64, 68–70, 75–76, 86–87, 96–98, 103, 112, 116–119, 134, 142–144, 158–160, 164, 167, 172–175, 179, 183, 188–189, 209–214, 218, 224–225, 231–233, 237–240, 242–322 |
| `swan-tech-ch2-vegetation-ice-bragg-gen12.md` | 7, 12, 31–32, 67–68, 71–73, 80–81, 84–86, 126–127, 164–165, 225, 233, 238, 271–272, 278–279, 282, 286–287, 294–295, 323–325, 327–329, 336, 339, 377–378, 386–421 |
| `swan-st6-babanin-implementation.md` | 6, 11, 62, 73–74, 84, 109, 111, 115, 117–118, 122, 143–165 |
| `swan-tech-ch8-unstructured-ops.md` | 7–8, 22, 53–55, 59, 82–85, 87, 91–93, 99–103, 116–118, 122–144 |
| `swan-action-balance.md` | 10–11, 62–63, 112, 121, 125, 131, 134–135, 237–249 |
