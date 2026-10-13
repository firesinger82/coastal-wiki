# SWAN 노트 추가 줄 전수 검증 3

검증일: 2026-10-13.

대상은 사용자가 지정한 노트 5개의 `git diff -U0 HEAD -- <노트>`에 표시되는 추가 줄이다.
추가 줄에는 frontmatter와 빈 줄을 포함한다.
각 노트의 검증 시작 시점 추가 줄 수를 기록한다.
정정 수와 보완 수는 이 작업에서 수정한 기존 줄 수로 센다.
원문은 로컬 SWAN 소스·과거 커밋·HTML·PDF이다.
결론 분류는 지정된 보고서의 최종 `[10-13 ...]` 기록과 대조한다.
완료한 노트는 아래에 원문 대조 범위와 수정 내역을 기록한다.

## 진행 기록

시작 시점의 다섯 노트 추가 줄은 총 267줄이다.
각 노트의 추가 줄 수는 아래 완료 기록에서 합산한다.

## 1. swan-output-variable-definitions.md — 완료

대상: [출력 변수 정의 노트](../../../models/SWAN/manual-notes/swan-output-variable-definitions.md).
대조한 추가 줄은 148줄이다.
이 수에는 빈 줄 14줄과 frontmatter 2줄이 포함된다.
정정은 0줄이다.
보완은 0줄이다.
정정 목록은 없다.

본문·표·링크·frontmatter를 모두 대조했다.
R5·R6의 차이 표 65행은 각 보고서 제5절의 최종 분류·결론과 일치했다.
E 행은 [git 판정 표](../compare/SWAN-git-verify-E.md)의 PN-127·PN-128·O-052·O-063·O-077·O-099·O-138·O-139와 일치했다.
[반영 기록 6](SWAN-notes-apply-6.md)의 추가 날짜와 검증 방법 기록을 확인했다.

원문 대조 범위는 swanuse PDF 36·103–105·110–114·123–128·142쪽과 swantech PDF 18·36·116쪽이다.
swanuse PDF 128쪽 이미지는 TMBOT 식의 제곱근 범위를 확인하는 데 사용했다.
웹 원문은 `online_doc/swanuse/node12.html:63–68`과 `node32.html:273–333,417–420,1244–1338`을 대조했다.
코드 원문은 인용된 swanmain·swanout1·swanout2·swancom1·swancom3·swancom5·swanpre1·swanpre2·swanser·swmod1·ocpmix·SwanSpectPart·SwanIntgratSpc·SwanComputeForce·misc/swan.edt의 해당 줄과 분기 문맥을 대조했다.
QUANTITY 기본값 표의 물리량 이름 86개는 swanmain의 LEXP·HEXP·EXCV 등록값과 모두 일치했다.
Table A.1의 MS·DSPR 23쌍은 인용된 감마함수 식의 소수 첫째 자리 계산값과 모두 일치했다.
과거 원문은 `b2ae30e`·`7ee8981`·`43e9bbb`의 해당 파일을 `git show`로 열어 대조했다.
상대 링크의 대상 파일은 모두 존재했다.
추가 줄에 개인 절대 경로·위키링크·금지된 한계 문장은 없었다.
이 노트의 추가 줄에는 mermaid 상자가 없다.
미해결 항목은 0개이다.

### 기계 확인 후보 판정

| 후보 | 판정과 근거 |
|---|---|
| 노트 181행, `src/swanout1.ftn:4159` 뒤 `의 CEX/DDIR은` | 오판이다. 실제 인용은 `b2ae30e:src/swanout1.ftn:4159`이다. 해당 줄은 `CEX = CEX/DDIR`이다. 한국어 연결 문장은 코드 인용이 아니다. 노트를 유지했다. |
| 노트 181행, `src/swanout1.ftn:4247` 뒤 `과` | 오판이다. `7ee8981`과 `43e9bbb`의 4247행은 모두 `CEX = CEX/DDIR`이다. 노트를 유지했다. |
| 노트 187행, `src/swancom5.ftn:5112` 뒤 `의 ABS는` | 오판이다. 세 커밋의 5112행은 모두 `ARADSTR    = ABS(ARADSTR)`이다. 노트를 유지했다. |
| 노트 193행, `src/SwanSpectPart.ftn:1447` 뒤 `의 방향식은` | 오판이다. 세 커밋의 1447행은 모두 `XP(4,NPO) = MOD( 630.-ATAN2(SUMEY(IP),SUMEX(IP))/DEGRAD , 360. )`이다. 노트를 유지했다. |
| 노트 205행, `src/swanout1.ftn:1981` 뒤 `의 JDSXI 분기는` | 오판이다. `b2ae30e`의 1981–2000행은 JDSXI 보간 분기이다. 뒤의 두 커밋에서는 1987–2006행에 같은 분기가 있다. 세 분기 모두 RHO·GRAV 변환을 포함하지 않는다. 노트를 유지했다. |
| 노트 206행, `src/swanmain.ftn:3625` 뒤 `의 IUNT는` | 오판이다. `b2ae30e`의 3625–3626행은 인용한 IUNT 목록이다. 목록은 73을 포함하며 76·79·80을 포함하지 않는다. 노트를 유지했다. |
| 노트 206행, `src/swanmain.ftn:3690` 뒤 `과` | 오판이다. `7ee8981`의 3690–3691행과 `43e9bbb`의 3691–3692행은 앞의 IUNT 목록과 같다. 노트를 유지했다. |

## 2. swan-parallel-implementation.md — 완료

대상: [병렬 구현 노트](../../../models/SWAN/source-analysis/swan-parallel-implementation.md).
대조한 추가 줄은 41줄이다.
이 수에는 빈 줄 6줄과 frontmatter 2줄이 포함된다.
정정은 0줄이다.
보완은 0줄이다.
정정 목록은 없다.

R1·R4·R7의 차이 표 17행은 각 보고서 제5절의 최종 분류·결론과 일치했다.
본문의 OpenMP 배열 설명은 [R8 N1-004](SWAN-callflow.md#8-차이-결론)와 일치했다.
추가 줄 범위와 날짜는 [반영 기록 4](SWAN-notes-apply-4.md)의 이 노트 기록과 일치했다.
기존 작성·마이그레이션 경위는 HEAD 대비 변경 전 frontmatter와 같은 내용이다.

원문 대조 범위는 swantech PDF 137–141쪽, swanimp PDF 19–20·22·25·27·32–33쪽, swanuse PDF 21–22·37–38·46쪽이다.
웹 원문은 `swanimp/node13.html:48–53`, `node17.html:79–81`, `node19.html:58–63`, `node20.html:163–184`를 대조했다.
공개 patch `41.51.A:366–368,390–391`에는 심볼릭 링크 생성·정리 문맥이 있었다.
코드 원문은 루트·src의 CMakeLists.txt, swmod2·swanparll·SwanParallel·SwanCompUnstruc·swancom1·swanpre1·ocpids·switch.pl·bin/swanrun·bin/swanrun.bat의 인용 줄과 조건문을 대조했다.
IHALOX·IHALOY 대입 검색은 swmod2의 JAC=1·WFR=3 두 선언만 반환했다.
MPI·METIS·OpenMP 표지는 인용 원문과 일치했다.
상대 링크의 대상 파일은 모두 존재했다.
추가 줄에 개인 절대 경로·위키링크·금지된 한계 문장은 없었다.
이 노트의 추가 줄에는 mermaid 상자가 없다.
사용자가 제시한 기계 확인 후보는 이 노트에 없다.
미해결 항목은 0개이다.

## 3. swan-spectral-file-format.md — 완료

대상: [스펙트럼 파일 형식 노트](../../../models/SWAN/manual-notes/swan-spectral-file-format.md).
대조한 추가 줄은 36줄이다.
이 수에는 빈 줄 3줄과 frontmatter 2줄이 포함된다.
정정은 1줄이다.
보완은 5줄이다.
수정 후 추가 줄 수도 36줄이다.

R6의 차이 표 12행은 보고서 제5절의 최종 분류·결론과 일치했다.
O-140은 [git 판정 표](../compare/SWAN-git-verify-E.md)의 강한 E 판정과 일치했다.
추가된 날짜·검증 방법은 [반영 기록 6](SWAN-notes-apply-6.md)과 일치했다.
원문 대조 범위는 swanuse PDF 119–120·145–151쪽과 swanpre2·swanmain·swanser·swanout2·swancom1·swancom2의 인용 줄이다.
TEST의 머리말 수와 실제 원천항 목록을 함께 대조했다.
1D 밀도 예외 처리의 IQCM 조건과 PI2 변환 순서를 확인했다.
추가 줄의 외부 모델 입력 문장은 연결된 노트가 가리키는 XBeach·EFDC 원문의 해당 읽기 부분만 열어 판정했다.
상대 링크의 대상 파일은 모두 존재했다.
추가 줄에 개인 절대 경로·위키링크·금지된 한계 문장은 없었다.
이 노트의 추가 줄에는 mermaid 상자가 없다.
수정한 여섯 줄의 원문·링크·정정 표지를 다시 확인했다.
미해결 항목은 0개이다.

### 정정·보완 목록

| 노트:줄 | 종류 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| swan-spectral-file-format.md:22 | 보완 | writer는 SWAN 1을 쓴다는 문장에 reader 인용만 있음 → writer의 버전 상수·WRITE 인용 추가 | `src/swanout2.ftn:1866`의 `INTEGER, SAVE :: IVERF = 1`과 1907행의 `WRITE (NREF, 101) IVERF`이다. 1908행 FORMAT은 SWAN 표식을 기록한다. |
| swan-spectral-file-format.md:26 | 보완 | SWAN 1 기록에 reader·PDF 예제 인용 → 같은 writer 상수·WRITE 인용 추가 | `src/swanout2.ftn:1866,1907–1908`이다. |
| swan-spectral-file-format.md:65 | 보완 | 건조점·보간 실패 설명에 수심 조건만 인용 → IERR 오류의 NODATA 분기 인용 추가 | `src/swanout2.ftn:2054–2055`의 `IF (IERR.GT.0) THEN`과 `WRITE (NREF, 220) 'NODATA'`이다. 보간의 EXCPT는 2266행에서 2412행의 `IERR = 1`로 연결된다. |
| swan-spectral-file-format.md:85 | 정정 | XBeach와 EFDC를 이 스펙트럼의 소비자로 함께 서술하고 one-way nesting으로 일반화 → XBeach의 2D 스펙트럼 입력과 EFDC GETSWAN_GRP의 TABLE 입력을 각각 명시 | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/waveparamsnew.F90:418,936,1048–1094`는 `read_swan_file`과 VaDens·EnDens·FACTOR·2D 배열 읽기이다. `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Waves/mod_getswan.f90:32–37`은 `GETSWAN_GRP`와 `TABLE 'GRP1' HEADer 'EXAMPLE.grp' HS PDIR RTP WLEN DEPTH DISSIP`를 명시한다. 96–101행은 물리량별 열을 찾는다. R6에는 EFDC가 이 스펙트럼을 읽는다는 근거가 없다. |
| swan-spectral-file-format.md:97 | 보완 | O-106의 보간 실패 설명에 수심 조건만 인용 → IERR 오류의 NODATA 분기 인용 추가 | `src/swanout2.ftn:2054–2055`이다. 결론 분류와 결론 문장은 유지했다. |
| swan-spectral-file-format.md:103 | 보완 | N-019의 SWAN 1 기록에 reader 인용만 있음 → writer의 버전 상수·WRITE 인용 추가 | `src/swanout2.ftn:1866,1907–1908`이다. 결론 분류와 결론 문장은 유지했다. |

### 기계 확인 후보 판정

| 후보 | 판정과 근거 |
|---|---|
| 노트 101행, `src/swancom2.ftn:3643` 뒤 `의 10회 반복은` | 오판이다. 실제 인용은 `b2ae30e:src/swancom2.ftn:3643`이다. 해당 줄은 `DO LOOP = 1, 10`이다. 한국어 연결 문장은 코드 인용이 아니다. 노트를 유지했다. |
| 노트 101행, `src/swancom2.ftn:3733` 뒤 `과` | 오판이다. `7ee8981:src/swancom2.ftn:3733`은 `DO LOOP = 1, 10`이다. 노트를 유지했다. |
| 노트 101행, `src/swancom2.ftn:3733` 뒤 `에도 유지된다`와 git 판정 링크 | 오판이다. `43e9bbb:src/swancom2.ftn:3733`도 같은 10회 반복이다. 3734행은 NODATA를 기록한다. git 판정 링크의 대상 파일도 존재한다. 노트를 유지했다. |

## 4. swan-data-structures-implementation.md — 완료

대상: [자료구조 구현 노트](../../../models/SWAN/source-analysis/swan-data-structures-implementation.md).
대조한 추가 줄은 23줄이다.
이 수에는 빈 줄 3줄과 frontmatter 2줄이 포함된다.
정정은 0줄이다.
보완은 0줄이다.
정정 목록은 없다.

R1·R8의 차이 표 6행은 각 보고서 최종 분류·결론과 일치했다.
본문의 AC1·JCOMPDA·기억 배열·OpenMP·해법별 초기화 설명은 해당 R8 결론과 일치했다.
추가 줄 범위와 날짜는 [반영 기록 4](SWAN-notes-apply-4.md)의 이 노트 기록과 일치했다.
기존 작성·마이그레이션 경위는 HEAD 대비 변경 전 frontmatter와 같은 내용이다.
차이 표가 인용한 수정 전 노트 문장은 git diff의 삭제 줄과 일치했다.

원문은 `swanmain.ftn:296,497–519,6892–6904`의 AC1 선언·할당·복사를 대조했다.
할당부 주석에는 MXITNS 조건이 없었다.
실행문에는 MXITNS 조건이 있었다.
`swancom1.ftn:1487,1541–1549,1581–1590,1698–1699`는 활성 기억 배열의 초기화와 sweep 반복 순서를 뒷받침했다.
`swanout1.ftn:1987–2006`은 JCOMPDA 열 선택과 보간을 뒷받침했다.
`swancom1.ftn:1170–1175,3644–3653`은 SWMATR의 PRIVATE 선언과 절편 전달을 뒷받침했다.
`swancom1.ftn:3656–3729,7291–7294,8931–8938,9441–9446`과 `SwanTranspAc.ftn90:117–118`은 해법별 초기화 구분과 일치했다.
`swanpre1.ftn:4705–4724`는 방향 격자 구성 뒤의 조건부 양의 2.E-6 rad 이동과 일치했다.
상대 링크의 대상 파일은 모두 존재했다.
추가 줄에 개인 절대 경로·위키링크·금지된 한계 문장은 없었다.
이 노트의 추가 줄에는 mermaid 상자가 없다.
사용자가 제시한 기계 확인 후보는 이 노트에 없다.
미해결 항목은 0개이다.

## 5. swan-surfbeat-iem.md — 완료

대상: [SURFBEAT 구현 노트](../../../models/SWAN/source-analysis/swan-surfbeat-iem.md).
대조한 추가 줄은 19줄이다.
이 수에는 빈 줄 4줄과 frontmatter 2줄이 포함된다.
정정은 1줄이다.
보완은 0줄이다.
수정 후 추가 줄 수도 19줄이다.

R5:PN-072의 C 분류와 결론 문장은 보고서 제5절의 최종본과 일치했다.
입력 조건·기본값 설명은 R5의 PN-071·PN-073 및 수정안과 일치했다.
추가 줄 범위와 frontmatter 갱신은 [반영 기록 3](SWAN-notes-apply-3.md)과 일치했다.
SwanIEM.ftn90의 실제 줄 수는 1230줄이다.
subroutine 선언은 78·324·488·679행의 네 개이다.
frontmatter와 관련 링크의 `p.80`은 swanuse의 인쇄 80쪽에 해당했다.
해당 PDF 쪽 번호는 88쪽이다.

원문은 swanuse PDF 88–90쪽과 swantech PDF 66–68쪽을 대조했다.
`swanpre1.ftn:2132–2150`과 `swanmain.ftn:4104–4189`은 정상성·차원·격자·방향·서쪽 경계·두 COMPUTE 조건을 뒷받침했다.
`swanmain.ftn:1214`와 `SwanIEM.ftn90:172–187`은 기본 균등 주파수 분포와 Hz의 각주파수 변환에 해당했다.
`SwanIEM.ftn90:550,613–652`은 0.01 증가분·성분 선택·증가·종료·오류 검사 순서와 일치했다.
QCM 관련 링크의 설명은 R3:QC-002 최종 결론과 통계적 교차상관의 원문 정의를 기준으로 정정했다.
`SwanQCM.ftn90:1593,2568–2572`의 W 변환·상관함수 계산도 해당 판정을 뒷받침했다.
소스 내부 변경 번호 41.90·41.85는 각 모듈 38행과 일치했다.
상대 링크의 대상 파일은 모두 존재했다.
추가 줄에 개인 절대 경로·위키링크·금지된 한계 문장은 없었다.
이 노트의 추가 줄에는 mermaid 상자가 없다.
사용자가 제시한 기계 확인 후보는 이 노트에 없다.
미해결 항목은 0개이다.

### 정정 목록

| 노트:줄 | 종류 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| swan-surfbeat-iem.md:123 | 정정 | QCM을 다른 phase-resolving 시도로 표현 → Wigner 분포로 파랑 성분 간 교차상관을 다루는 QC 설명으로 변경 | swantech PDF 67–68쪽 / 인쇄 59–60쪽은 교차상관을 포함한 Wigner 분포와 2차 파랑 통계를 정의한다. R3:QC-002 최종 결론은 QC가 개별 파면을 합성하지 않는다고 명시한다. 41.90·41.85는 `src/SwanQCM.ftn90:38`과 `src/SwanIEM.ftn90:38`의 내부 변경 표기로 명시했다. |

## 최종 집계

| 노트 | 대조한 추가 줄 | 정정 | 보완 | 미해결 |
|---|---:|---:|---:|---:|
| swan-output-variable-definitions.md | 148 | 0 | 0 | 0 |
| swan-parallel-implementation.md | 41 | 0 | 0 | 0 |
| swan-spectral-file-format.md | 36 | 1 | 5 | 0 |
| swan-data-structures-implementation.md | 23 | 0 | 0 | 0 |
| swan-surfbeat-iem.md | 19 | 1 | 0 | 0 |
| 합계 | 267 | 2 | 5 | 0 |

추가 줄 수는 수정 전후의 `git diff -U0 HEAD -- <노트>`에서 파일 머리말을 제외한 `+` 줄을 센 값이다.
수정 전후의 추가 줄 번호 집합은 같다.
총 267줄에는 frontmatter 10줄과 빈 줄 30줄이 포함된다.
차이 표의 행 ID는 노트별 행을 합쳐 101행이다.
이 대상에 A 분류 행은 없다.
과거 코드 인용의 b2ae30e·7ee8981·43e9bbb는 각각 2022-08-10·2024-09-02·2026-07-13의 커밋이다.
사용자가 제시한 기계 확인 후보 10건의 개별 판정은 제1절과 제3절에 모두 기록했다.
추가 줄의 상대 링크 69개는 모두 실제 파일을 가리킨다.
이 수는 중복 링크를 포함한다.
정정·보완한 7줄에는 지정된 표지가 있다.
대상 노트의 `git diff --check HEAD -- <노트 5개>`는 오류 없이 종료했다.
이 작업의 노트 수정은 위 정정·보완 목록의 7줄이다.
미해결 항목은 0개이다.
