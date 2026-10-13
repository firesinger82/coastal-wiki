# SWAN 노트 추가 줄 전수 검증 12

검증일: 2026-10-13.
대상은 사용자 지정 노트 6개의 `git diff -U0 HEAD -- <노트>` 추가 줄이다.
작업 시작 시 추가 줄은 총 325줄이다. 이 수는 frontmatter와 빈 줄을 포함한 diff의 `+` 줄 집계이다.
원문은 사용자가 지정한 로컬 코드, 과거 커밋, 웹 HTML, PDF이다.
결론 분류와 결론 문장은 대조 보고서의 최종 `[10-13 ...]` 판정과 대조한다.
정정 수와 보완 수는 이 작업에서 바꾼 대상 줄 수로 센다.
노트별 줄 번호는 해당 노트의 검증 완료 시점을 기준으로 적는다.

| 대상 노트 | 시작 시 추가 줄 수 | 상태 | 정정 수 | 보완 수 |
|---|---:|---|---:|---:|
| `models/SWAN/manual-notes/swan-command-setup-grid-reference.md` | 97 | 완료 | 0 | 0 |
| `models/SWAN/manual-notes/swan-tech-ch3-qc-curvilinear.md` | 77 | 완료 | 7 | 0 |
| `models/SWAN/manual-notes/swan-tech-ch8-unstructured-grid-scheme.md` | 45 | 완료 | 1 | 1 |
| `models/SWAN/source-analysis/swan-source-coverage-audit.md` | 59 | 완료 | 25 | 0 |
| `models/SWAN/manual-notes/swan-tech-ch7-parallel.md` | 27 | 완료 | 1 | 0 |
| `models/SWAN/source-analysis/swan-stationary-vs-nonstationary.md` | 20 | 완료 | 0 | 0 |

## 노트별 검증 결과

### swan-command-setup-grid-reference.md — 완료

- 대조한 추가 줄은 97줄이다. frontmatter 7–8줄과 빈 줄도 포함했다. 정정은 0줄이다. 보완은 0줄이다.
- 대조 범위는 7–8, 22, 28–31, 33–35, 39, 45–47, 50–51, 55–56, 80–84, 89, 91–93, 99, 105, 114, 120, 122–124, 144, 150, 152–154, 158–215줄이다.
- 코드 인용 205건을 지정된 원문 줄과 대조했다. PROJECT·SET·CGRID·READGRID·INPGRID·READINP·INITIAL의 조건과 수식을 주변 코드에서도 대조했다. MAXMES와 CASTD의 사용처는 소스 검색으로 대조했다.
- PDF 근거는 swanuse 18–19, 35–43, 48–55, 64, 132–133, 135쪽과 swantech 144쪽이다. 웹 근거는 node23, node25, node26, node49와 수정 이력이다.
- 차이 표 44행의 분류와 결론을 R4·R5·R7 최종본과 대조했다. R4의 T1-062·T1-147·T1-310·T1-311은 뒤쪽 변경 요약과 본문 최종 결론을 함께 대조했다. A 분류 행은 없다.
- frontmatter의 반영 기록은 SWAN-notes-apply-5.md의 해당 노트 기록과 일치한다. 상대 링크는 모두 존재한다. 추가 줄에 절대 경로, 위키 링크, 지정된 한계 문장은 없다. Mermaid 상자는 없다.
- 정정 목록: 없음.
- 기계 확인 후보 판정: 노트 215줄의 `website/modifications/modifications.htm:291`은 오탐이다. 원문 291–304줄을 이어 읽으면 `The lowest and the highest frequencies can be specified. The number of frequencies will be computed by SWAN such that the ratio of frequency resolution is 10%. This is required by the DIA method.`와 일치한다. 인용 시작 줄 291도 맞다. 노트를 유지했다.

### swan-tech-ch3-qc-curvilinear.md — 완료

- 대조한 추가 줄은 77줄이다. frontmatter 7–8줄과 빈 줄도 포함했다. 정정은 7줄이다. 보완은 0줄이다.
- 대조 범위는 7–8, 22, 28, 32, 34–36, 43–44, 46–48, 50, 53, 63–65, 70–72, 81–83, 92, 97–98, 100–103, 111, 117–119, 123–164줄이다.
- swantech PDF 68, 110–116, 153쪽과 swanuse PDF 90–91, 128, 139–140쪽을 대조했다. swantech 113·115·116쪽 이미지를 열어 수식의 괄호·부호·첨자를 대조했다. 웹 node34·node55–57·swanuse/node28도 대조했다.
- 현재 코드의 자동 파수 격자, FFT 점 수, QC 쇄파, 기울기 분기, Tukey 창, 곡선 격자 변환, 힘 계산을 대조했다. `7ee8981:src/SwanQCM.ftn90:1363`과 `b2ae30e:src/SwanQCM.ftn90:1358,2362`에서 QC 쇄파 호출·정의를 대조했다.
- 차이 표 30행의 분류와 결론은 R1·R3 최종본과 일치한다. 정정 후 단일 위치 코드 인용 74건은 모두 원문과 일치한다. 여러 위치를 묶은 인용도 지정 구간을 열어 대조했다.
- 상대 링크는 모두 존재한다. 추가 줄에 절대 경로, 위키 링크, 지정된 한계 문장은 없다. Mermaid 상자는 없다.
- 정정 목록:
  - `swan-tech-ch3-qc-curvilinear.md:8`: `online HTML +43 offset`과 `[D] 보조식은 PDF 무번호`를 고쳤다. PDF (3.44)–(3.45)는 HTML (3.86)–(3.87)에 대응한다. PDF (3.46)–(3.69)는 HTML (3.89)–(3.112)에 대응한다. `[D]`는 PDF (3.54)이다. 근거는 swantech PDF 111–116과 웹 node55:92,426,508·node56:63,238·node57:301이다.
  - `swan-tech-ch3-qc-curvilinear.md:28`: PDF (2.146)–(2.155)와 HTML (2.225)–(2.230)을 함께 적은 범위 표기를 고쳤다. §3.9 서두의 PDF 참조는 (2.154)–(2.155)이다. 웹 참조는 (2.225)–(2.230)이다. 근거는 swantech PDF 110–111과 웹 node55:48–50이다.
  - `swan-tech-ch3-qc-curvilinear.md:34`: `작아 수용`을 `수용할 만큼 작을 것으로 기대한다고 적는다`로 고쳤다. 근거는 swantech PDF 111의 `we expect that such aliasing errors would prove to be small enough to be accepted`와 R3:QC-074이다.
  - `swan-tech-ch3-qc-curvilinear.md:43`: `dkx = sdev / rfac`를 `dkx  = sdev / rfac`로 고쳤다. 근거는 `src/SwanQCM.ftn90:521`의 등호 앞 두 칸이다.
  - `swan-tech-ch3-qc-curvilinear.md:149`: `dkx = sdev / rfac`를 `dkx  = sdev / rfac`로 고쳤다. 근거는 `src/SwanQCM.ftn90:521`이다.
  - `swan-tech-ch3-qc-curvilinear.md:156`: `at least second order accurate`를 `at least second order accuracy`로 고쳤다. 근거는 swantech PDF 112 / 인쇄 104쪽이다.
  - `swan-tech-ch3-qc-curvilinear.md:157`: `dkx = sdev / rfac`를 `dkx  = sdev / rfac`로 고쳤다. 근거는 `src/SwanQCM.ftn90:521`이다.
- 사용자 지정 기계 확인 후보: 없음.

### swan-tech-ch8-unstructured-grid-scheme.md — 완료

- 대조한 추가 줄은 45줄이다. frontmatter 7–8줄과 빈 줄도 포함했다. 정정은 1줄이다. 보완은 1줄이다.
- 대조 범위는 7–8, 22, 51, 98–100, 104–106, 112, 114, 118–120, 124–153줄이다.
- swantech PDF 96, 144–151쪽과 swanuse PDF 24, 135쪽을 대조했다. 웹 node84–92의 식 번호와 swanuse node11·node25·node49 및 수정 이력을 대조했다.
- 현재 코드의 격자 검사, sweep 수 선택, GRAPH·FXFRO 전환, 정점 목록, 최소 bin 확장과 수송 행렬 조립을 대조했다. 인용된 `7ee8981`, `122b595`, `43e9bbb`의 해당 파일·줄도 대조했다.
- 차이 표 16행의 분류와 결론은 R1·R7·R8 최종본과 일치한다. R8:T1-014에 덧붙인 날짜 2026-07-13은 git A 판정과 `git show`의 0dabfa4 날짜에 일치한다. 0dabfa4의 변경문에서 GRAPH·FXFRO 분기 추가를 확인했다. R7:H-1346의 `R7:` 접두어는 보고서 식별자를 명시한 차이이다.
- 정정·보완 후 단일 위치 코드 인용 25건은 원문과 일치한다. 스위치 표지와 줄 끝 판 번호도 원문과 일치한다. 상대 링크는 모두 존재한다. 지정된 금지 경로·위키 링크·한계 문장은 없다. Mermaid 상자는 없다.
- 정정 목록: `swan-tech-ch8-unstructured-grid-scheme.md:22`의 `BSBT(=N-scheme)`를 `BSBT`로 고쳤다. N-scheme과의 일치가 특성선 방향으로 사각형을 삼각분할한 정규 격자에 한정됨을 덧붙였다. 근거는 swantech PDF 149 / 인쇄 141쪽의 `but they are not identical in general`과 R1:TN-201이다.
- 보완 목록: `swan-tech-ch8-unstructured-grid-scheme.md:141`의 `call msgerr (1, ... )`를 원문의 완전한 호출로 보완했다. 셀 수 검사와 각도 검사에도 각각 위치를 붙였다. 근거는 `src/SwanCheckGrid.ftn90:106,111,118,151`이다.
- 사용자 지정 기계 확인 후보: 없음.

### swan-source-coverage-audit.md — 완료

- 대조한 추가 줄은 59줄이다. frontmatter 6–7줄과 빈 줄도 포함했다. 정정은 25줄이다. 보완은 0줄이다.
- 대조 범위는 6–7, 27, 38–41, 107–124, 144, 157, 170, 184, 200, 206, 210, 229, 240, 243, 251–258, 276–277, 279, 283–284, 286, 289–298줄이다.
- 소스 파일 수, 표의 파일 줄 수, §2의 링크 대상 수, swancom1의 선언 수를 다시 셌다. 연결 노트의 실제 소스 근거와 원문 루틴 선언을 대조했다. §3의 헤더 발췌가 모두 1–60줄의 직인용이라는 frontmatter 주장은 수정했다.
- swanimp PDF 8–10·21쪽과 swanuse PDF 72·79·88·89쪽 및 swantech PDF 57·81–83·100·154쪽을 대조했다. 기존 노트의 부정확한 미커버 분류를 현재 연결 내용에 맞췄다.
- 차이 표 3행의 최종 분류와 결론은 R7과 일치한다. I-057·N-002의 추가 날짜는 git A 판정과 일치한다. `7ee8981:src/SwanThreadBounds.ftn90:1`과 `git show 0dabfa4 -- src/SwanThreadBounds.ftn90`의 `deleted file mode 100644`를 대조했다. 0dabfa4의 날짜는 2026-07-13이다.
- 상대 링크는 모두 존재한다. 추가 줄에 절대 경로, 위키 링크, 지정된 한계 문장은 없다. Mermaid 상자는 없다.
- 정정 목록:
  - `swan-source-coverage-audit.md:6`: 전: 모든 author/version/purpose comment block verbatim 인용 (line 1-60)·기존 20개. 후: 헤더 발췌의 요약을 구분했다. 목적 주석 68줄을 명시했다. 고유 링크 수 19개를 기록했다. 근거: `src 파일 확장자 집계; §2 상대 링크 20건·고유 대상19개; src/SwanCompUnstruc.ftn90:68; src/mod_xnl4v5.ftn90:28`.
  - `swan-source-coverage-audit.md:27`: 전: 기존 20개 노트·12개 신규 발견 verified. 후: 소스 57+18개와 고유 연결 19개로 구분했다. 근거: `현행 src 집계; §2 링크 대상 집계`.
  - `swan-source-coverage-audit.md:108`: 전: swancom1-5 (legacy compute). 후: swancom1 + swancom5 + swanpre1 (ACTION·전파법·PROP 파서). 근거: `swan-schemes-implementation.md:22`.
  - `swan-source-coverage-audit.md:109`: 전: SwanPropvelS / SwanPropvelX / SwanTranspAc / SwanTranspX. 후: swancom1 + swancom5 + swanmain (전파 조립·호출). 근거: `swan-propagation-implementation.md:24`.
  - `swan-source-coverage-audit.md:110`: 전: swancom1 + SwanPrepComp. 후: swanmain + swanpre1 + swancom5 + SwanTranspX + swanout1. 근거: `swan-time-stepping-implementation.md:25–28,66`.
  - `swan-source-coverage-audit.md:111`: 전: swancom4-5 (source terms) + SdsBabanin. 후: swancom1 (SOURCE 조립) + swancom2–5 + SdsBabanin. 근거: `src/swancom1.ftn:6823; wave/swan-source-terms-implementation.md:42`.
  - `swan-source-coverage-audit.md:112`: 전: swancom4 (Sin). 후: swancom3 (WNDPAR·SWIND0/3/4/5) + swanpre1. 근거: `src/swancom3.ftn:1526,1842,2094,2668; swan-wind-formulations-implementation.md:24`.
  - `swan-source-coverage-audit.md:113`: 전: swancom4 (Sds). 후: swancom2 (SWCAP·SWCAP8) + swancom1 (호출·조립). 근거: `src/swancom2.ftn:2213,2693; src/swancom1.ftn:7505–7515`.
  - `swan-source-coverage-audit.md:115`: 전: SwanBndStruc + swanpre2. 후: swanpre1 + swanpre2 + swanmain + swmod2. 근거: `swan-boundary-implementation.md:25–28`.
  - `swan-source-coverage-audit.md:116`: 전: SwanInterpolate* + swanpre2. 후: swanpre2 + swanout1/2 + swanmain + swanser. 근거: `swan-nesting-io-implementation.md:24`.
  - `swan-source-coverage-audit.md:117`: 전: **SwanDiffPar** + SwanFindObstacles + SwanCrossObstacle. 후: SwanDiffPar + SwanFindObstacles + swancom5 + swanpre1. 근거: `swan-diffraction-obstacles.md의 원문 파일 인용`.
  - `swan-source-coverage-audit.md:120`: 전: SwanGriddata + SwanGridobjects + swmod1/2. 후: SwanGriddata + swmod1/2 + swanmain. 근거: `swan-data-structures-implementation.md의 원문 파일 인용`.
  - `swan-source-coverage-audit.md:121`: 전: swanout1/2 + nctablemd + swn_outnc + SwanVTKWrite*. 후: swanout1/2 + swanpre2 + swanser + swn_outnc. 근거: `swan-output-formats.md:20–24; swan-output-writers-implementation.md:24`.
  - `swan-source-coverage-audit.md:122`: 전: agioncmd + swan.edt (User App C). 후: swanpre1/2 + ocpcre + misc/swan.edt (입력 명령). 근거: `src/agioncmd.ftn90:13–18; swan-command-file-reference.md:28–31`.
  - `swan-source-coverage-audit.md:124`: 전: swancom4-5 (deep). 후: swancom1 (SOURCE 조립) + swancom2–5 + SdsBabanin. 근거: `src/swancom1.ftn:6823; wave/swan-source-terms-implementation.md:42`.
  - `swan-source-coverage-audit.md:144`: 전: 본 위키 미커버·신설 후보. 후: 기존 swan-surfbeat-iem 연결과 SURFBEAT의 PDF 88 / 인쇄 80쪽. 근거: `src/SwanIEM.ftn90:1,42; swanuse PDF88; swan-surfbeat-iem.md`.
  - `swan-source-coverage-audit.md:157`: 전: 미커버·Tech p.48. 후: 기존 Bragg 노트 연결과 본문 PDF 57 / 인쇄 49쪽. 근거: `src/SwanBraggScat.ftn90:1,42; swantech PDF57; swanuse PDF79`.
  - `swan-source-coverage-audit.md:170`: 전: SWAN refraction의 artifact·미커버. 후: 공간 전파 GSE의 확산 보정과 기존 GSE 노트 연결. 근거: `src/SwanGSECorr.ftn90:40; swantech PDF81–83,154`.
  - `swan-source-coverage-audit.md:184`: 전: 본 위키 미커버·신설 후보. 후: 기존 QC 노트 연결과 SCAT의 PDF 89 / 인쇄 81쪽. 근거: `src/SwanQCM.ftn90:42; swanuse PDF89; swan-quasi-coherent.md`.
  - `swan-source-coverage-audit.md:200`: 전: DIA 대비 high-precision·신설 후보. 후: 문서의 XNL 선택값 51·52·53과 기존 XNL 노트 연결. 근거: `src/mod_xnl4v5.ftn90:4–5; swanuse PDF72; 연결 노트`.
  - `swan-source-coverage-audit.md:210`: 전: 본 위키 미언급·.e 확장자. 후: 리더의 .n·.e 파일과 기존 격자 리더 노트 연결. 근거: `src/SwanReadEasymeshGrid.ftn90:40`.
  - `swan-source-coverage-audit.md:253`: 전: §3.8 / §8.6. 후: §3.2.1–3.2.2 / §8.6. 근거: `swantech PDF81–83,100,154`.
  - `swan-source-coverage-audit.md:256`: 전: 1684. 후: 1678줄; 현재 파일 집계. 근거: `src/SwanCompUnstruc.ftn90 현재 splitlines/wc -l 집계`.
  - `swan-source-coverage-audit.md:277`: 전: 원논문 fetch 후 노트 신설 가치. 후: 기존 XNL4 노트와 모듈 저자·목적 연결. 근거: `src/mod_xnl4v5.ftn90:2–5; swan-xnl4-exact-quadruplet.md`.
  - `swan-source-coverage-audit.md:279`: 전: 19개 서브루틴·13개 기존 커버. 후: 20개 선언·14개 기존 노트 연결·4개 유틸리티·2개 setup 루틴. 근거: `src/swancom1.ftn SUBROUTINE 선언20개; swan-setup-solver-swancom1-crosswalk.md:42–63`.
- 기계 확인 후보 판정: `src/SwanCompUnstruc.ftn90:848`의 `의 원문은` 후보는 오탐이다. 이 구절은 노트 41줄의 한국어 설명이다. 인용 본문 `!GRAPH                ivert = flist(kvert,swpdir)`는 현재 코드와 `43e9bbb:src/SwanCompUnstruc.ftn90:848`에 그대로 있다. 노트를 유지했다.
- 기계 확인 후보 판정: `src/SwanCompUnstruc.ftn90:849`의 `의 원문은` 후보는 오탐이다. 이 구절은 노트 41줄의 한국어 설명이다. 인용 본문 `!FXFRO                ivert = vlist(kvert,swpdir)`는 현재 코드와 `43e9bbb:src/SwanCompUnstruc.ftn90:849`에 그대로 있다. 노트를 유지했다.

### swan-tech-ch7-parallel.md — 완료

- 대조한 추가 줄은 27줄이다. frontmatter 7–8줄과 빈 줄도 포함했다. 정정은 1줄이다. 보완은 0줄이다.
- 대조 범위는 7–8, 21, 28, 46–48, 80–81, 93–110줄이다.
- swantech PDF 137–141쪽, swanuse PDF 21–22·46쪽, swanimp PDF 19·22·25쪽을 대조했다. 웹 swanimp node13:48–53·node17:79–81과 수정 이력 139·949–951줄도 대조했다.
- halo 상수의 선언과 사용, 활성점 계수·IWEIG 배분, METIS의 tpwgts, MPI 통신 호출과 ACUPDA·PARLL 조건을 원문과 대조했다. `!JAC`, `!WFR`, `!MPI`, `!METIS` 표지는 원문과 일치한다.
- 차이 표 6행의 분류와 결론은 R1·R7 최종본과 일치한다. H-139의 추가 커밋과 날짜는 git A 판정의 `24a7d67`(2023-10-16)과 일치한다. 해당 커밋의 `src/SwanParallel.ftn90:504`에서도 METIS 호출을 확인했다.
- 상대 링크는 모두 존재한다. 추가 줄에 절대 경로, 위키 링크, 지정된 한계 문장은 없다. Mermaid 상자는 없다.
- 정정 목록: `swan-tech-ch7-parallel.md:7`의 `알고리즘·라이브러리·버전 history verbatim 정리`를 원문 인용과 AI 한국어 요약을 함께 포함한다는 설명으로 고쳤다. 실제 대조한 27줄과 원자료 종류를 명시했다. 근거는 swantech PDF 137–141쪽과 본문의 한국어 해석 문장이다.
- 기계 확인 후보 판정: 노트 110줄의 `website/modifications/modifications.htm:949`은 오탐이다. 원문 949–951줄에 인용한 세 문장이 연속으로 있다. HTML 링크를 문장으로 읽으면 인용과 일치한다. 시작 줄 949도 맞다. 노트를 유지했다.

### swan-stationary-vs-nonstationary.md — 완료

- 대조한 추가 줄은 20줄이다. frontmatter 6–7줄과 빈 줄도 포함했다. 정정은 0줄이다. 보완은 0줄이다.
- 대조 범위는 6–7, 66, 147, 149, 171, 182, 184, 214–225줄이다.
- TMREL의 분모, SACC2의 모멘트 정의, IQCM 분기, DTABS 생략값, AC1 전체·0 크기 할당과 시간 복사 조건, 기본 전파법, 회절 덮어쓰기, COMPUTE·NUMERIC 파서를 현재 코드와 대조했다. 조건문의 변수명·괄호·논리 연산자는 원문과 일치한다.
- `b2ae30e:src/swancom1.ftn:9606`의 TMREL 식과 커밋 날짜 2022-08-10을 대조했다. R5:PN-085와 git E 판정의 강한 결함 후보 결론도 일치한다. 비정렬의 `src/SwanConvStopc.ftn90:187,219,225`는 주기 정규화 비교 근거와 일치한다.
- 차이 표 4행의 분류와 결론을 R4·R5 최종본과 대조했다. AC1 설명은 R8:N1-001과 일치한다. swanuse PDF 94 / 인쇄 86쪽의 MXITNS 기본값 인용도 일치한다.
- frontmatter의 이전 마이그레이션 기록과 214줄의 생성 기록은 `_staging/swan-prescan/wiki-candidate/models/SWAN/source-analysis/swan-stationary-vs-nonstationary.md:6,219`에 같은 내용으로 남아 있다. recovery 반영 기록은 SWAN-notes-apply-4.md:31과 일치한다.
- 상대 링크는 모두 존재한다. 추가 줄에 절대 경로, 위키 링크, 지정된 한계 문장은 없다. Mermaid 상자는 없다.
- 정정 목록: 없음.
- 사용자 지정 기계 확인 후보: 없음.

## 최종 집계와 확인

- 대조한 추가 줄은 총 325줄이다. 근거는 위 표의 97 + 77 + 45 + 59 + 27 + 20줄이다.
- 정정한 줄은 총 34줄이다. 근거는 위 표의 0 + 7 + 1 + 25 + 1 + 0줄이다.
- 인용을 보완한 줄은 1줄이다. 해당 줄은 `swan-tech-ch8-unstructured-grid-scheme.md:141`이다.
- 시작 시 추가 줄과 최종 추가 줄의 줄 번호 집합은 일치한다. 변경된 35줄은 정정·보완 기록의 전후 문자열과 모두 일치한다.
- 변경된 줄의 끝에는 지정된 정정 또는 보완 태그가 있다. 대상 노트 6개의 YAML frontmatter는 정상적으로 해석된다. 변경한 표의 열 수는 각 표의 머리글과 일치한다.
- 대상 추가 줄의 상대 링크는 모두 실제 파일을 가리킨다. 대상 추가 줄에는 지정된 절대 경로·위키 링크·한계 문장이 없다. 대상 추가 줄에는 Mermaid 호출 상자가 없다.
- 사용자 지정 기계 확인 후보 4건은 원문 대조 결과 모두 오탐이다. 각 판정은 해당 노트의 결과에 기록했다.
- 읽기 전용 `git diff --check`에서 공백 오류는 나오지 않았다. 미해결 항목은 0건이다.
