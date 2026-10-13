# SWAN 노트 추가·수정 줄 전수 대조

대상 노트는 `models/SWAN/manual-notes/swan-documentation-stack.md`이다.
작업 시작 시 `git diff -U0 HEAD -- models/SWAN/manual-notes/swan-documentation-stack.md`의 추가 줄은 230줄이다.
이 수에는 frontmatter 3줄과 빈 줄 12줄을 포함한다.
아래 줄 번호는 별도 표기가 없으면 작업 시작 시 노트의 줄 번호이다.
대조 기준은 저장된 코드·HTML·PDF와 사용자가 지정한 보고서의 최종 결론이다.

## 진행 기록

- 2026-10-13: 대상 줄 목록을 확정했다.
- 2026-10-13: 노트의 추가 줄 230줄 대조를 완료했다. 정정 7줄과 보완 2줄을 반영했다.
- 2026-10-13: 최종 diff의 추가 줄 목록이 작업 시작 목록과 같음을 확인했다. 대상 노트의 `git diff --check`가 통과했다.

## 노트별 결과

| 노트 | 상태 | 대조한 추가 줄 | 정정 | 보완 |
|---|---|---:|---:|---:|
| [swan-documentation-stack.md](../../../models/SWAN/manual-notes/swan-documentation-stack.md) | 완료 | 230 | 7 | 2 |

대조 줄 수는 작업 시작 시 지정된 `git diff -U0 HEAD`의 추가 줄을 센 값이다.
정정 수와 보완 수는 이번에 붙인 `[10-13 전수 검증 정정]`과 `[10-13 전수 검증 보완]`의 노트 줄 수이다.
수정 전후 노트의 줄 수는 모두 434줄이다.
수정한 9줄은 모두 작업 시작 시 추가 줄 목록에 속한다.
미해결 항목은 없다.

### 전체 추가 줄의 대조 범위

| 작업 시작 시 노트 줄 | 추가 줄 수 | 대조 근거와 결과 |
|---|---:|---|
| 5, 7–8, 85, 107 | 5 | PDF 표지·저작권·쪽 수·목차·swantech §1.4를 대조했다. frontmatter의 이메일 출처를 정정했다. 명령 57개의 집계 기준을 보완했다. |
| 135, 157, 161, 164, 168, 183–185, 197–199 | 11 | swantech 목차와 R1·R3의 해당 결론을 대조했다. swanimp의 빌드·전처리·초기화 설명을 대조했다. swanpgr의 규칙·예제·문서 이력을 대조했다. `switch.pl:21–37`과 `src/SwanConvAccur.ftn90:97`을 대조했다. 옵션 목록의 PDF 범위를 정정했다. |
| 201, 207–230, 238, 240, 242–246, 250–253 | 36 | 연결된 노트의 주제와 매뉴얼 장·절을 대조했다. R1·R2·R3·R6의 연결 절을 확인했다. 경계조건의 장 매핑과 출력 변수의 포괄적 정합 표현을 정정했다. Appendix C의 가치 평가를 원문 설명으로 바꾸었다. ADCIRC 연결을 보완했다. |
| 257–267 | 11 | 제목·표 머리글·빈 줄을 확인했다. 문서 판과 코드 판을 확인했다. `43e9bbb`의 날짜는 2026-07-13이다. 현재 `src/swanmain.ftn:965,967–968`에는 41.51과 patch A·B가 있다. |
| 268–286 | 19 | 문서 구성·배포 표의 12개 행을 R7 최종 결론과 대조했다. 다운로드·설정 HTML, 현재 코드, 인용 커밋을 대조했다. N-025·N-026의 수정 전 노트 인용을 매뉴얼 원문으로 교체했다. |
| 287–330 | 44 | 패치·수정 이력의 44개 행을 R7 및 Git 판정 보고서와 대조했다. HTML의 연속 문장과 태그를 확인했다. 모든 코드 인용과 과거 커밋 인용을 대조했다. DIA·triad·굴절 식의 조건을 확인했다. |
| 331–388 | 58 | 수정 이력의 58개 행을 R7 및 Git 판정 보고서와 대조했다. 호환성의 예외, 기본값 변경, 제거 이력, 빌드 조건을 확인했다. COMMON·STOP·배열 할당·CDLIM·IQUAD 인용을 확인했다. |
| 389–434 | 46 | 수정 이력의 46개 행을 R7 및 Git 판정 보고서와 대조했다. netCDF 속성의 정상·비정상 조건을 확인했다. INIT PAR와 자동 초기화의 조건을 확인했다. MPI 자료형·기준점·HPGL 제거 인용을 확인했다. |
| 합계 | 230 | 빈 줄 12줄을 포함한다. |

### 결론과 인용의 교차 확인

표의 행은 160개이다.
분류별 행 수는 A 16개, B 1개, C 10개, D 23개, F 1개, H 109개이다.
이 수는 노트의 `R7:` 표 행을 센 값이다.
160개 행의 분류와 결론은 [R7 최종 결론](../compare/swan-implementation-history-vs-code.md#5-차이-결론)과 일치한다.
A 행에 덧붙인 커밋·날짜 문장은 [Git A 판정](../compare/SWAN-git-verify-A.md)과 일치한다.
보고서의 실행 한계 문장을 생략한 D-005·D-011·H-1121은 결론의 분류와 내용이 유지되어 있다.

| A 행의 커밋 | 날짜 | 해당 행 |
|---|---|---|
| `7ee8981` | 2024-09-02 | S-002, H-529, H-531, H-1149의 후속 변경, H-1180, H-1205 |
| `0dabfa4` | 2026-07-13 | Q-018 |
| `24a7d67` | 2023-10-16 | H-139, H-961, H-1123 |
| `122b595` | 2023-02-28 | H-472, H-566, H-755, H-1228의 41.45 비교 기준 |
| `2980d1a` | 2023-02-27 | H-538, H-1149의 첫 변경, H-1170 |

인용한 과거 파일은 `git show HASH:path`로 열었다.
변경을 주장한 행은 해당 커밋 전후의 읽기 전용 `git diff`로도 확인했다.
`2980d1a`의 IDRAG·ITRIAD·TRFAC 변경을 확인했다.
`24a7d67`의 PWCAP 대입 삭제와 SwanParallel 추가를 확인했다.
`7ee8981`의 TRFAC 변경과 SWSPB·SWFTIM 호출 교체를 확인했다.
`0dabfa4`의 patch B 활성화를 확인했다.
H-131의 SwanPunCollect 삭제는 `24a7d67` 전후에서 확인했다.
H-1371의 Makefile 추가는 `acb58b3` 전후에서 확인했다.

`122b595`와 `43e9bbb`의 `src/`를 각각 검색했다.
두 판에서 `FD.?RIAM`, `Cumulative Steepness` 또는 단어 `CSM`, `MPI_REAL4`, `starplot`은 각각 0행이다.
두 판의 `HPGL` 일치는 각각 7행이다.
이 7행은 모두 제거 이력 주석이다.
HottifySWAN의 전체 이력 검색 판정은 [Git D 판정](../compare/SWAN-git-verify-D.md)과 대조했다.

HTML 인용은 태그와 줄바꿈을 구분하여 읽었다.
`modifications.htm:566`은 `<li>`로 시작한다.
H-566의 인용 문장은 그 항목의 567행에 이어지므로 시작 줄 인용을 유지했다.
`!MPI` 등 전처리 표지와 코드 줄 끝의 판 번호는 원문과 대조하여 유지했다.

### 최종 형식 확인

상대 링크 65개가 실제 파일을 가리킨다.
절 앵커를 포함한 상대 링크는 모두 해당 절이 있다.
frontmatter는 YAML로 해석된다.
수정한 표 행은 기존 열 수를 유지한다.
대상 노트의 Mermaid 블록 수는 0개이다.
대상 노트에 절대 사용자 경로와 이중 대괄호 위키 링크가 없다.
대상 노트에 사용자가 지정한 실행·확인 한계 문장이 없다.

## 정정·보완 목록

아래 `N`은 [대상 노트](../../../models/SWAN/manual-notes/swan-documentation-stack.md)이다.
`S`는 `models/SWAN/raw/source_code/swan/`이다.
`W`는 `models/SWAN/raw/manuals/website/`이다.
PDF는 `models/SWAN/raw/manuals/pdfs/`의 원본이다.

| 종류 | 노트:줄 | 수정 전 | 수정 후 | 근거 원문 |
|---|---|---|---|---|
| 정정 | N:7 | User Manual front matter에 `e-mail m.zijlema@tudelft.nl`이 있다고 적었다. | 이메일을 삭제했다. 표지·저작권 쪽을 명시했다. 이번 대조 범위를 기록했다. | swanuse PDF 1쪽은 `SWAN Cycle III version 41.51`이다. PDF 3쪽은 저자·우편 주소·홈페이지·저작권·GNU FDL 1.2를 적는다. 이메일 주소는 없다. 전체 swanuse PDF 텍스트에서도 해당 이메일의 일치는 0건이다. |
| 보완 | N:85 | `57 commands`의 집계 기준이 없었다. | swanuse PDF 5–7쪽의 명령 이름을 중복 없이 세는 기준을 명시했다. | 목차의 PROJECT부터 STOP까지 명령 항목은 59개이다. READGRID와 OBSTACLE은 각각 두 항목이다. 첫 명령어의 고유값은 57개이다. |
| 정정 | N:185 | `swanimp PDF 19–20쪽 / 인쇄 13–14쪽` | `swanimp PDF 18–20쪽 / 인쇄 12–14쪽`으로 바꾸었다. 현재 옵션 판독의 `switch.pl:21–37`도 명시했다. | PDF 18쪽의 `perl switch.pl [-dos] [-unix] ... [-netcdf] *.ftn`이 14개 옵션의 전체 목록이다. PDF 19–20쪽은 그 설명의 이어지는 부분이다. S/switch.pl:21–37의 판독 분기는 17개이다. |
| 정정 | N:216 | 경계조건 노트를 `§2.5 + Ch 4`에 대응시켰다. | Ch 4와 PDF·인쇄 쪽 번호로 바꾸었다. | swantech PDF 5쪽 목차의 §2.5는 `Modelling of obstacles`이다. PDF 125–126쪽의 Ch 4는 `Wave boundary and initial conditions`이다. 연결 노트의 범위도 SWBOUN·경계 파일·경계값 적용이다. |
| 보완 | N:220 | `(외부, swan-coupling 별도)` | 실제 파일인 `swan-adcirc-coupling-implementation.md`의 상대 링크를 추가했다. | [ADCIRC 결합 구현 노트](../../../models/SWAN/source-analysis/swan-adcirc-coupling-implementation.md)의 제목은 `swan adcirc coupling implementation`이다. 파일이 존재한다. |
| 정정 | N:244 | 출력 변수 전체를 `적분식 verbatim`과 `이론 Eq ... output quantity 정합`으로 묶었다. | 문서 정의의 위치와 파고·주기·방사응력 식의 대상을 구분했다. 변수별 판정은 R6 최종 결론으로 연결했다. | swanuse PDF 123–128쪽은 변수 정의이다. swantech PDF 18쪽의 (2.11)–(2.12)는 파고·주기이다. PDF 116쪽의 (3.59)–(3.61)는 방사응력이다. [R6:O-051](../compare/swan-outputs-vs-code.md#5-차이-결론)은 QP 문서식을 B로 판정한다. 모든 출력 변수의 정합으로 묶을 수 없다. |
| 정정 | N:246 | `cross-walk 가치 ... 대부분 커버됨, 잔여 가치 낮음` | Appendix C가 명령 구문을 제시한다는 설명으로 바꾸었다. PDF·인쇄 쪽을 명시했다. | swanuse PDF 135쪽: `Below the file swan.edt is presented in which all the commands that can be used with SWAN are specified.` 원문은 잔여 가치를 평가하지 않는다. |
| 정정 | N:278 | `swan-documentation-stack.md:182`와 수정 전 `14 옵션` 문장을 원문으로 인용했다. | swanimp PDF 18쪽과 W/online_doc/swanimp/node10.html:54–55의 실제 명령 목록을 인용했다. | 기존 182행은 빈 줄이다. HTML 54–55행의 목록에는 `-dos`, `-unix`부터 `-adcirc`, `-netcdf`까지 14개 옵션이 있다. R7:N-025의 C 분류와 결론은 유지했다. |
| 정정 | N:279 | `swan-documentation-stack.md:194`와 수정 전 `v1.3 ... 이후 미갱신` 문장을 원문으로 인용했다. | swanpgr PDF 1쪽의 판과 PDF 51쪽의 마지막 문서 이력을 인용했다. | 기존 194행은 목차 표의 `Performance / Machine dependency / Exceptions / Names` 행이다. PDF 1쪽은 `Version 1.3`이다. PDF 51쪽 마지막 이력은 `1.3`, `March 22, 2006`이다. R7:N-026의 H 분류와 결론은 유지했다. |

## 기계 확인 후보 판정

아래 10개 후보는 각각 원문을 열어 판정했다.
10개 모두 노트 인용이 맞으므로 해당 인용을 유지했다.

| 후보 | 노트 줄 | 판정 | 확인한 원문 |
|---|---:|---|---|
| problems_and_fixes.htm:48의 Windows 7 문장 | 287 | 오탐. 수정 없음. | W/problems_and_fixes/problems_and_fixes.htm:48의 `patch`에 `<tt>` 태그가 있다. 태그를 제외한 문장은 `However, Windows 7 (or higher) demands that patch must be run with administrative privileges.`이다. |
| README.md:285의 bug reports 문장 | 287 | 오탐. 수정 없음. | S/README.md:285의 `For bug reports please send to the [SourceForge mailing list](http://sourceforge.net/mail/?group_id=384349).`와 그대로 일치한다. 저장소 루트의 README가 아니다. |
| README.md:31의 Implementation Manual 문장 | 288 | 오탐. 수정 없음. | S/README.md:31의 `Please see the [Implementation Manual](https://swanmodel.sourceforge.io/online_doc/swanimp/swanimp.html) for additional documentation.`와 그대로 일치한다. |
| modifications.htm:47의 LTA 문장 | 292 | 오탐. 수정 없음. | W/modifications/modifications.htm:47–48의 문장이다. 48행의 링크 표시문 `Section 2.3.4`를 포함하면 노트 인용과 같다. |
| modifications.htm:112의 SPB 문장 | 293 | 오탐. 수정 없음. | W/modifications/modifications.htm:112–114의 연속 문장이다. 114행의 `Becq-Girard et al. (1999)`는 링크 표시문이다. |
| modifications.htm:131의 HottifySWAN 문장 | 294 | 오탐. 수정 없음. | W/modifications/modifications.htm:131–132의 연속 문장이다. 132행의 `this page`는 링크 표시문이다. |
| modifications.htm:133의 winddrag 문장 | 295 | 오탐. 수정 없음. | W/modifications/modifications.htm:133–135의 연속 문장이다. `will gives`도 원문 그대로이다. |
| modifications.htm:170의 Alves·Banner 문장 | 297 | 오탐. 수정 없음. | W/modifications/modifications.htm:170–185의 연속 문단이다. 주파수 국소량·Komen 비교·Yan 결합·GEN3 WESTH 조건이 인용과 같다. |
| modifications.htm:195의 문서 분리 문장 | 298 | 오탐. 수정 없음. | W/modifications/modifications.htm:195–200의 연속 문장이다. `Morever`와 `LaTeX for dummies`도 원문 그대로이다. |
| modifications.htm:202의 온라인 문서 문장 | 299 | 오탐. 수정 없음. | W/modifications/modifications.htm:202–204의 연속 문장이다. `<font>`와 링크 태그를 제외한 내용이 인용과 같다. |

추가 자동 대조에서 결론 셀의 반복 인용을 직전 코드 인용과 잘못 연결한 후보도 원문으로 판정했다.
H-219의 첫 반복 조건은 S/src/swancom1.ftn:7703에 있다.
H-695의 선택 조건은 S/src/swancom5.ftn:1710에 있다.
H-778의 선택 조건은 S/src/swancom5.ftn:1667에 있다.
H-1227의 입력 조건은 S/src/swanpre1.ftn:1990에 있다.
H-1268의 조건은 S/src/swn_outnc.ftn90:1241에 있다.
H-894의 중복 판 번호는 W/modifications/modifications.htm:894–901에 있다.
H-538의 이전 IDRAG 값과 H-1123의 삭제 대입은 해당 커밋의 diff에 있다.
검색식·검색 결과를 코드 원문으로 잘못 묶은 후보는 Git 판정 기록과 두 비교 판의 검색으로 구분했다.
