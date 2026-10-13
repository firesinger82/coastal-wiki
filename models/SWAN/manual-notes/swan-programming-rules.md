---
title: "SWAN Programming Rules (swanpgr v1.3) — ANSI F90 standards + control/module/layout rules + 13-section subroutine template + naming(sw/swmod) + STRACE/IENT verbatim"
topic: swan
canonical_source: external
external_source: "swanpgr (SWAN Programming Rules, Version 1.3, SWAN team, 2006-03-22). Chapters 1 Introduction / 2 FORTRAN 90 standards / 3 Control statements / 4 Use of modules / 5 Program layout / 6 Input-output / 7 Error messages / 8 Pseudo code / 9 Performance / 10 Machine dependency / 11 Exceptions / 12 Names / 13 Examples(templates) / Bibliography / Log sheet."
citation_status: verified
verification_method: "models/SWAN/raw/manuals/website_markdown/online_doc/swanpgr/ node1-18.md 전 노드 직접 read. F90 규칙·control 구문·module 규약·13-section layout·subroutine/module template·naming 규약 verbatim. source-analysis 의 실제 SWAN 서브루틴 주석블록 구조와 cross-check. 2026-10-13 recovery 대조 보고서 R1–R8 반영"
last_source_check: "2026-10-13 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context) raw markdown direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — 코딩 규약 verbatim, 13-section template ↔ source-analysis 주석블록 정합"
verification_date: 2026-06-03
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/manual-notes/swan-implementation-manual.md
  - models/SWAN/source-analysis/swan-foundation.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
---

# SWAN Programming Rules (swanpgr v1.3) — verified

> swanpgr (Programming Rules v1.3, 2006-03-22) node1-18 직접 read. SWAN **개발자용 코딩 규약**의 객관 레이어. source-analysis 의 모든 노트가 인용하는 서브루틴 **13-section 주석블록 구조**·`STRACE/IENT` trace·naming 규약(`sw`/`swmod`)의 1차 출처. "no final status" — 경험·통찰에 따라 갱신되는 문서(node1).

## 1. 정체 (node1)

shallow water wave model SWAN 개발 규칙. 목적: reliable·stable·readable·structured 코드 + maintenance/error tracking 단순화. plain text vs FORTRAN text(sanserif typewriter font) 구분. **인접 프로그램도 준수 권장**.

## 2. FORTRAN 90 standards (node2) ★

핵심 규칙 verbatim 요약:

- **ANSI FORTRAN 90** 준수. 텍스트: Chapman(1998), Morgan & Schonfelder(1993).
- **modular programming** 강력 권장. 한 줄에 **한 statement**.
- program unit 첫 줄 = `PROGRAM`/`SUBROUTINE`/`FUNCTION`/`MODULE`.
- 신규 unit = **free format + `.f90`**, 기존 = `.f`(Linux)/`.for`(Windows). free format include 는 fixed form 서브루틴에 포함 불가.
- label 컬럼 1-5, statement 7-72(cf. F77). line **최대 80자**, follow-on mark `&`.
- parameter 전달은 **argument list 우선**, 아니면 module. **common block 금지**.
- **`IMPLICIT NONE`** + 변수 명시 선언 + `INTENT` 규칙(원문은 pointers 예외 명시, `raw/manuals/website_markdown/online_doc/swanpgr/node2.md:44-48`). 단 implicit 관례 유지: `i`-`n` = integer, `c`/`z` = complex, 나머지 = real.
- 변수 1개당 선언문 1개. 선언에 **항상 `::`**. **알파벳 순**. 첫 몇 글자로 구별 가능. 의미있는(영어) 이름.
- `INTEGER IARRAY(100)` (type 선언) > `DIMENSION IARRAY(100)`. array dimension 에 real 식 금지. **mixed-mode(single/double) 식 금지**.
- pointer 는 항상 `NULLIFY` 초기화. **allocatable array 우선**(heap; automatic array=stack overflow 위험). 미사용 allocatable 은 서브루틴 끝에서 deallocate. validity check 는 `STAT=`. 길이 미지/대형 데이터·linked list 는 `POINTER`+`TARGET`.
- **`END DO`**(`CONTINUE` 금지), nested 는 각자 `END DO`. do loop 구조 label 로 가독성.
- 소문자 권장. space·comment block·줄간격 충분히. multi-dim array 는 논리구조 일치 시.
- 원문은 SAVE 속성을 요구하면서 fixed form 예제에는 SAVE IENT 문을 쓴다. B는 문서 내부의 규칙·예제 불일치이다. (swanpgr PDF 11쪽 / 인쇄 5쪽: `Use the SAVE attribute (not the SAVE statement!)`; swanpgr PDF 41쪽 / 인쇄 35쪽: `SAVE IENT`; `src/SdsBabanin.ftn90:1454` `SAVE IENT`; R7:N-024.)
- constant 는 `parameter` statement(unit number·array dim·물리/수치 상수 한 곳 정의). 예 `PI = 4.*ATAN(1.)`.
- statement label: **FORMAT 전용** + 오름차순.
- character: argument 전달은 `CHARACTER(LEN=*)`, 길이는 `LEN` intrinsic(전달 금지). relational(`.LT.` 등) 대신 `LGE/LGT/LLE/LLT`. ASCII/EBCDIC 비의존 위해 `ICHAR/CHAR` 대신 **`IACHAR/ACHAR`**.
- **obsolete F77 금지**: statement function, assigned goto, named/blank common, arithmetic if, `EQUIVALENCE`, `ENTRY`, `ERR=`/`END=`(→`IOSTAT`), `PAUSE`, multiple entry/return, IF block 외부서 ENDIF jump, non-integer do index, H edit descriptor.
- intrinsic 은 **generic name**(`ABS`, not `CABS`/`DABS`). 신규는 `>`,`>=`,`<`,`=<`,`==`,`/=`(기존은 `.GT.` 등 허용). 원문의 `=<`는 오기이다. 코드가 사용하는 Fortran 연산자는 `<=`이다. (swanpgr PDF 12쪽 / 인쇄 6쪽: `>, >=, <, =<, == and /=`; `src/SwanConvAccur.ftn90:213` `if ( hsabs <= max(hsrel,hsoval) .and. tmabs <= max(tmrel,tmoval) ) npacc = npacc + 1.`; R7:N-022.)
- **`STOP` 금지** — 단 (a) fatal error 출력 후 error 서브루틴 (b) explicit lockup routine 만.
- 2개 초과 배타 선택 = **`SELECT CASE`**. `WHERE` 금지(성능 저하). **BLAS 금지**. **`GOTO` 금지** — error handling(label `9999` `CONTINUE` jump)만.
- clean do loop, `IF THEN ELSE` 는 가능하면 loop 밖. 중간결과 I/O 회피(array 저장/재계산 우선). nested 다차원 array 는 **inner loop = first index**(cache/vector 효율).

## 3. Control statements (node3)

3 구조만: sequence / selection / iteration.
- **selection**: `IF-THEN-ELSE` 또는 `SELECT CASE`(+`CASE default`). `IF-THEN-ELSEIF-ELSE` 는 대안이나 모든 분기 평가 단점.
- **iteration**: `DO-ENDDO`(`CYCLE`/`EXIT`), `DO WHILE`, `REPEAT UNTIL`. **DO WHILE 은 `DO`+`IF(.NOT.cond)EXIT` 로 시뮬레이션 권장**. REPEAT UNTIL = `DO … IF(cond)EXIT ; ENDDO`.

## 4. Use of modules (node4)

idea = **data hiding + locality**. 관련 서브루틴·데이터를 한 module 에. **common block 금지**(module 으로 대체). explicit interface(`USE`) — (a) module 에 서브루틴 전체 배치(작은 변경도 cascade 재컴파일) 또는 (b) interface 만(중복) — 둘 다 허용. 모든 entity **default `PRIVATE`**, 외부 필요분만 `PUBLIC`. module 은 서로 다른 서브루틴이 공유하는 데이터 보유 금지(private data 는 가능).

## 5. Program layout — 13-section 주석블록 (node5) ★★

> 매뉴얼이 SWAN 프로그램·서브루틴에 요구하는 **표준 layout**이다. nesting indent **3 칸**, **tab 절대 금지**(이식성).

patch B의 SwanThreadBounds 삭제로 활성 STRACE 파일과 호출행이 각각 하나 줄었다. 현재 집계는 75파일 중 62파일과 호출행 292개이다. STRACE 호출은 표준 주석 layout 전체의 준수율이 아니다. (R7:N-023의 직속 `.ftn`·`.ftn90` 파일과 기본 `-unix` 치환 집계; `0dabfa4` 2026-07-13의 삭제 원문 `deleted file mode 100644`; `43e9bbb:src/SdsBabanin.ftn90:1456` `      IF (LTRACE) CALL STRACE (IENT,'SWIND0_NRL')`.)

표준 순서:
1. program unit statement
2. **comment block**: programmer 이름 / version + date + machine / 수정 version+date+이유 / copyright(GNU GPL 권장) / 기능 설명. version 은 `1.0` 시작 — major = 정수부 +1·소수 0, minor = 소수 +1. machine accuracy 민감 routine 은 경고 주석.
3. input/output 변수 선언 + `i`(input)/`o`(output) 표시 주석 (lexicographic + `INTENT`)
4. local 변수: 선언 / `SAVE`·parameter·data / lexicographic 설명 주석
5. comment block: I/O(unit·file) / 사용 서브루틴 / 이 서브루틴을 부르는 서브루틴 / error message / **pseudo code(Ch 8)**
6. program text (FORMAT 문은 unit 끝)

→ **Ch 13 template 외 다른 layout 사용 금지** (node5 verbatim). 실제 번호 매김(`0. Authors` `1. Updates` `2. Purpose` `3. Method` `4. Argument variables` `5. Parameter variables` `6. Local variables` `8. Subroutines used` `9. Subroutines calling` `10. Error messages` `11. Remarks` `12. Structure` `13. Source text`)은 §10 template 참조.

## 6. Input/output (node6)

- **`PRINT` 금지** — `READ`/`WRITE` 만. file unit number 는 generic 함수/서브루틴 제공, 변수로 사용, **11 미만 금지**. **`IOSTAT=`**(not `ERR=`/`END=`). carriage control 은 blank 만. error message 에 module 이름 포함. 미사용 file close. `OPEN` 은 machine-dependent(Ch 10). 입력은 대소문자 무구분 + numerical 은 **free format**.

## 7. Error messages (node7)

기본 = **hard(imperative)** option — 에러 시 메시지 + 필요 시 중단. soft(non-imperative) 는 수치법 에러(비수렴)만 — error number 를 parameter list 에 추가하고 계속(parameter 로 명시 선택). error vs warning 구분. **에러 10개 등 과다 시 STOP, warning 최대 10개 출력**. STOP 은 fatal error 후 호출 서브루틴에 내장. 입력 에러는 모두 출력할 때까지 계속.

## 8. Pseudo code (node8-11)

- 알고리즘 수학 기술은 논문처럼 정확히(super/subscript). 미가용 기호는 `sqrt`/`sum` 번역. 구조도 유사(indent, JSP 는 가독성 약간 낮음). 3 제어구조: `if/then/else`, `select/case`, `for i=i1(i2)i3` / `while` / `repeat until`.
- I/O 는 descriptive text + source file/machine. `STDIN`/`STDOUT` 사용. 그 외 file 은 OPEN/close.
- pseudo code 는 integer/real 무구분(real, infinite accuracy). 필요 시 PASCAL `DIV`/`MOD`. **목적 = 알고리즘 명확 기술**(각 statement 기술 아님), 임의 프로그래머가 즉시 코딩 가능해야. 너무 복잡하면 문서 참조.

## 9. 성능 (node9 / node2 후미)

clean loop(IF/GOTO/CALL 없이). 예: `DO i; IF(var>0) a(i)=0. ELSE a(i)=b(i); ENDDO` → `IF(var>0) a(:)=0. ELSE a(:)=b(:)`. inner loop 를 가장 길게 + first index. indirect addressing·do loop 내 division·(외견상)recursion 회피.

## 10. Machine dependency (node13)

- precision: CRAY 등 64-bit. double→single 변환 위해 `DOUBLE PRECISION`/`COMPLEX*16` 명시 + `REAL`/`COMPLEX` 중복선언 줄 컬럼 1-2 에 `ce` 표시. generic intrinsic name.
- `OPEN` 은 machine-dependent(filename; IBM mainframe 거부) → OPEN 을 한 서브루틴에 집중.
- machine 상수(accuracy·largest real) 는 generic 서브루틴 초기화 + module 포함.
- plot 은 machine/device/package-dependent → real plot call 회피, machine-dependent call 분리 또는 neutral file.

## 11. Exceptions (node14)

FORTRAN 표준 이탈 허용 사례: **array 전달 = start address 전달** 특성 이용(dummy argument 의 dimension number/size 가 actual 과 달라도 됨). 이유: (a) linear solver 등 구조상 array-as-array (b) top-level parameter 수 감소 → error 회피. **risk 있어 user 가 다루는 top layer 서브루틴만 허용**, 하위는 모두 정연하게. 사용 시 array bound 수동 확인(checker/debugger 무력).

## 12. Names for SWAN program units (node12, node15) ★

- 최상위 서브루틴은 기억하기 쉬운 이름을 자유롭게 정할 수 있다. 하위 서브루틴에는 이름 충돌을 피하기 위해 `sw` 접두어를 권장한다. 문서는 모듈 이름의 예로 `swmod` 뒤에 세 자리 기호를 붙이는 방식을 든다. 실제 일반 모듈 이름은 `swmod1`과 `swmod2`이다. (swanpgr PDF 37쪽 / 인쇄 31쪽: `could for example be followed by a 3-digit symbol`; swanimp PDF 21쪽 / 인쇄 15쪽: `swmod1.f, swmod2.f`; [swan-implementation-manual](swan-implementation-manual.md) §2.) [10-13 전수 검증 정정]
- 적용된 서브루틴/module 이름 + 기능 설명의 **ASCII file 최신 유지** 필수.

## 13. Subroutine/module template (node16) ★★

> source-analysis 가 인용하는 실제 SWAN 주석블록. fixed-form subroutine 골격(verbatim):
```fortran
!****************************************************************
      SUBROUTINE SWBODY ()
      USE OCPCOMM4
      IMPLICIT NONE
!     | Delft University of Technology … Programmers: The SWAN team |
!     SWAN … Copyright (C) 2002  Delft University of Technology
!     … GNU General Public License version 2 …
!  0. Authors          40.23: Marcel Zijlema
!  1. Updates          40.23, Aug. 02: New subroutine
!  2. Purpose          … 3. Method …
!  4. Argument variables
      INTEGER, INTENT(IN) :: VARIABLE
!  5. Parameter variables   ---
!  6. Local variables       INTEGER :: I, J
!  8. Subroutines used      ---
!  9. Subroutines calling   ---
! 10. Error messages        ---
! 11. Remarks               ---
! 12. Structure   (pseudo code)
! 13. Source text
      SAVE IENT
      DATA IENT/0/
      IF (LTRACE) CALL STRACE (IENT,'SWBODY')
      ...
      RETURN
      END
```
free-form 은 `subroutine SwanRoutineBody()` + `use ocpcomm4` + `integer, save :: ient = 0` + `if (ltrace) call strace (ient,'SwanRoutineBody')`. module 골격: `MODULE MODBODY`(fixed) / `module SwanModuleBody`(free) 동일 13-section.

`SAVE IENT`/`DATA IENT/0/`와 `IF(LTRACE) CALL STRACE(IENT,'name')`는 서브루틴 진입부 trace의 표준 템플릿이다. (swanpgr PDF 41쪽 / 인쇄 35쪽.) 현재 집계는 75파일 중 62파일과 호출행 292개이다. STRACE 호출은 표준 주석 layout 전체의 준수율이 아니다. (R7:N-023의 기본 `-unix` 치환 집계; `0dabfa4` 2026-07-13.)

## 14. 메타 (node17-18)

- Bibliography: [1] Chapman S.J.(1998) *Fortran 90/95 for scientists and engineers*, WCB McGraw-Hill / [2] Morgan J.S. & Schonfelder J.L.(1993) *Programming in Fortran 90*, Alfred Waller.
- Log sheet: v1.0(2005-04-28 initial) → v1.1(2005-05-19 RWS-RIKZ 코멘트) → **v1.2(2006-01-10 영어 번역)** → **v1.3(2006-03-22 minor + 확장)**. → swanpgr 는 **2006년 이후 본문 미갱신**(swanimp/swanuse/swantech 가 41.51 인 것과 대조).

## 15. 연결

- [swan-documentation-stack](swan-documentation-stack.md) — 4 docs (본 노트가 swanpgr deep 화)
- [swan-implementation-manual](swan-implementation-manual.md) — swanimp (ANSI F90 한계·switch·`swmod` module 명명 cross-ref)
- [swan-source-coverage-audit](../source-analysis/swan-source-coverage-audit.md) / [swan-foundation](../source-analysis/swan-foundation.md) — §5 13-section layout + §13 STRACE/IENT 가 실제 소스에서 관찰되는 곳
- 공식: http://www.swan.tudelft.nl

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치 (swanpgr v1.3, 2006-03-22). 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb (2026-07-13 patch B).

표의 원문 인용과 AI 결론은 [R7 §5](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론)에서 옮겼다. N-022·N-023·N-024의 노트 인용과 줄 번호는 보고서에 보존된 반영 전 노트를 가리킨다. [10-13 전수 검증 보완]

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R7:P-001 | 문서 판·ANSI F90 | swanpgr PDF 9쪽, 인쇄 3쪽: `ANSI FORTRAN 90 standards`; PDF 51쪽, 인쇄 45쪽: `1.3` `March 22, 2006`; swanimp PDF 15쪽과 `../raw/manuals/website/online_doc/swanimp/node5.html:49–53`은 두 예외를 명시한다. | `src/swanout2.ftn:969` `!     note: stream access is a Fortran 2003 standard`; `src/swanser.ftn:7397` `CALL EXECUTE_COMMAND_LINE('mkdir '//TRIM(PATH), EXITSTAT=ESTAT,`; 이력: `7ee8981:src/swanout2.ftn:969` `!     note: stream access is a Fortran 2003 standard`; `7ee8981:src/swanser.ftn:7397` `CALL EXECUTE_COMMAND_LINE('mkdir '//TRIM(PATH), EXITSTAT=ESTAT,` | C 문서 누락 | 41.51 공개 코드도 Fortran 2003 stream과 Fortran 2008 EXECUTE_COMMAND_LINE을 사용한다. ANSI Fortran 90만을 사용한다는 설명에는 기존 구현 예외를 보충한다. C는 swanpgr에 한정한다. swanimp와 수정 이력 939행은 두 예외를 명시한다. |
| R7:P-002 | 모듈화 권고·500문장 한도 | swanpgr PDF 9쪽, 인쇄 3쪽: `Modular programming is strongly recommended`; `maximum of 500 source statements` | `src/swanpre1.ftn:19` `SUBROUTINE SWREAD`; 이력: `7ee8981:src/swanpre1.ftn:19` `SUBROUTINE SWREAD (COMPUT)                                          40.31 30.90`; `7ee8981:src/swanpre1.ftn:3254` `CALL INREAL ('EDMLPM', PWIND(10), 'UNC', 0.)`; `7ee8981`·`43e9bbb`의 `src/swanpre1.ftn:19–3696`에서 `^ {6,}CALL\b`에 맞는 활성 CALL은 각각 591문장이다. | C 문서 누락 | 41.51 공개 코드와 현재 SWREAD에는 행 시작의 활성 CALL만 각각 591문장이다. 이는 swanpgr PDF 9쪽의 500 source statements보다 많다. C는 swanpgr의 기존 구현 예외 누락이다. 이 작성 규칙을 현재 구현의 문장 수 상한으로 쓰지 않는다. |
| R7:P-003 | 한 줄 한 문장 | swanpgr PDF 9쪽, 인쇄 3쪽: `Only one statement per line is allowed.` | `src/mod_xnl4v5.ftn90:1289` `if (allocated (q_xk)) deallocate (q_xk)  ; allocate(q_xk(0:nkq))`; 이력: `7ee8981:src/mod_xnl4v5.ftn90:1289` `if (allocated (q_xk)) deallocate (q_xk)  ; allocate(q_xk(0:nkq))` | C 문서 누락 | 한 줄에서 DEALLOCATE와 ALLOCATE를 함께 실행하는 구문은 41.51 공개 코드에 이미 있다. 한 줄 한 문장 규칙에는 이 기존 예외를 구분한다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-006 | 주석 1열·권장 열 위치 | swanpgr PDF 9쪽, 인쇄 3쪽: `An exclamation mark (!) is used in the 1st column`; `preferably ... columns 7 to 72` | `src/SdsBabanin.ftn90:126` `    ! Local variables:`; 이력: `7ee8981:src/SdsBabanin.ftn90:126` `! Local variables:` | C 문서 누락 | 들여쓴 free form 주석은 41.51 공개 코드에 이미 있다. 모든 주석이 첫 열에서 시작한다는 구현 설명을 쓰지 않는다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-007 | 80자·연속행 열 | swanpgr PDF 10쪽, 인쇄 4쪽: `maximum of 80 characters`; `73rd column`; `6th column` | `src/swancom1.ftn:2971` `REAL  :: KWAVE(MSC,MICMAX), DMW(MSC,MICMAX)    ,`; 2972행 `&         UE(MSC4MI:MSC4MA , MDC4MI:MDC4MA )    ,`; 이력: `7ee8981:src/swancom1.ftn:2971` `REAL  :: KWAVE(MSC,MICMAX), DMW(MSC,MICMAX)    ,                    40.59 40.17 40.22` | C 문서 누락 | 41.51 공개 코드의 KWAVE 선언행도 우측 변경 표지를 포함해 80자를 넘는다. 고정 형식의 변경 표지와 컴파일 대상 문장 영역을 구분한다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-008 | 19개 연속행 | swanpgr PDF 9쪽, 인쇄 3쪽: `ANSI FORTRAN 90 standards`; swanimp PDF 21쪽, 인쇄 15쪽: `limit of 19 continuation lines is violated`; swanimp PDF 21쪽, 인쇄 15쪽: `the limit of 19 continuation lines is violated` | `src/swancom1.ftn:2971` `REAL  :: KWAVE(MSC,MICMAX), DMW(MSC,MICMAX)    ,`; 이력: `7ee8981:src/swancom1.ftn:2971` `REAL  :: KWAVE(MSC,MICMAX), DMW(MSC,MICMAX)    ,                    40.59 40.17 40.22`; `7ee8981:src/swancom1.ftn:2995` `&         REFLSO(MDC,MSC)                                            40.41` | C 문서 누락 | 41.51 공개 코드와 현재 코드의 `swancom1.ftn:2971–2995` 선언에는 연결행 24개가 있다. swanimp PDF 21쪽이 19행 제한의 예외를 이미 설명한다. C는 swanpgr의 ANSI Fortran 90 규칙에 한정하며 문서 전체의 누락으로 쓰지 않는다. |
| R7:P-009 | 인자·모듈 전달·COMMON 금지 | swanpgr PDF 10·19쪽, 인쇄 4·13쪽: `Common blocks are not acceptable.`; `common blocks are prohibited` | `src/SwanConvAccur.ftn90:97` `common/convaccur/npacc,nwetp,hsmean,tmmean`; `src/SwanConvStopc.ftn90:115` `common/convstopc/npacc,nwetp`; 이력: `7ee8981:src/SwanConvAccur.ftn90:103` `common/convaccur/npacc,nwetp,hsmean,tmmean`; `7ee8981:src/SwanConvStopc.ftn90:119` `common/convstopc/npacc,nwetp` | C 문서 누락 | 41.51 공개 코드도 수렴 환산값을 COMMON으로 공유한다. COMMON 금지 규칙에는 이 기존 구현 예외를 구분한다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-010 | IMPLICIT NONE·명시 선언·INTENT | swanpgr PDF 10쪽, 인쇄 4쪽: `mandatory statement IMPLICIT NONE`; `with the exception of pointers` | `src/SdsBabanin.ftn90:113` `LOGICAL          , INTENT(IN)  ::  TESTFL`; `src/SwanBraggScat.ftn90:525` `integer n, ierr`; 이력: `7ee8981:src/SdsBabanin.ftn90:113` `LOGICAL          , INTENT(IN)  ::  TESTFL`; `7ee8981:src/SwanBraggScat.ftn90:525` `integer n, ierr`; `7ee8981:src/SwanBraggScat.ftn90:522` `contains`; `7ee8981:src/SwanBraggScat.ftn90:524` `subroutine fit2(x,y,z,n,a,b,c,ierr)`; `7ee8981:src/SwanBraggScat.ftn90:526` `real*8 a,b,c,x(n),y(n),z(n)`; `7ee8981:src/SwanBraggScat.ftn90:118` `implicit none`; `src/SwanBraggScat.ftn90:118` `implicit none`; 522행 `contains`; 524행 `subroutine fit2(x,y,z,n,a,b,c,ierr)` | B 문서·노트 오기 | fit2는 IMPLICIT NONE이 있는 SWBRBOT의 내부 서브루틴이다. 단위마다 IMPLICIT NONE이 없다는 집계는 그 자체로 규칙 위반을 입증하지 않는다. 인자 INTENT의 누락도 41.51 공개 코드에 이미 있다. B는 이 차이를 판 변경으로 해석한 보고서의 오기이다. swanpgr PDF 22쪽은 입력·출력 인자와 지역변수 선언을 구분하므로 지역변수의 INTENT 부재도 위반으로 세지 않는다. [10-13 전수 검증 정정] |
| R7:P-011 | 변수명 자료형 관례·의미·구별 가능성 | swanpgr PDF 10쪽, 인쇄 4쪽: `integer names start with i up to and including n`; `complex variables with c or z`; `preferably in English` | `src/SdsBabanin.ftn90:123` `REAL             , INTENT(IN)  ::  CG(:,:)`; 121행 `INTEGER          , INTENT(IN)  ::  NFREQ`; 이력: `7ee8981:src/SdsBabanin.ftn90:123` `REAL             , INTENT(IN)  ::  CG(:,:)    ! CG(MSC,MICMAX)`; `7ee8981:src/swancom1.ftn:2971` `REAL  :: KWAVE(MSC,MICMAX), DMW(MSC,MICMAX)    ,                    40.59 40.17 40.22` | C 문서 누락 | 41.51 공개 코드도 K로 시작하는 KWAVE를 REAL로 선언한다. 자료형별 첫 글자 규칙에는 이 기존 예외를 구분한다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-012 | 변수당 선언·항상 ::·알파벳순 | swanpgr PDF 10쪽, 인쇄 4쪽: `Each variable must be declared in a separate statement`; `Always use the sign ::`; `alphabetical order` | `src/SdsBabanin.ftn90:143` `INTEGER           :: II,IS ! counters`; 145행 `REAL              :: ST1_INT,ST2_INT,SDS_INT`; 이력: `7ee8981:src/SdsBabanin.ftn90:143` `INTEGER           :: II,IS ! counters` | C 문서 누락 | 41.51 공개 코드도 한 선언문에 여러 변수를 쓴다. 변수당 한 선언 규칙에는 이 기존 예외를 구분한다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-013 | DIMENSION 문 금지·실수 차원 금지·assumed-size 최소화 | swanpgr PDF 10쪽, 인쇄 4쪽: `instead of DIMENSION`; `Never use real expressions in array dimensions`; `Use the * option as little as possible` | `src/swancom1.ftn:2992` `&         QTL1(MSC4D,*) ,QTL2(MSC4D,*)          ,` | H 코드 대조 대상 아님 | 문서는 assumed-size를 가능한 한 줄이라고 권고한다. 인용한 QTL1·QTL2 선언은 `*`를 사용한다. 이 사례만으로 최소화 권고의 충족 여부나 모든 차원식의 자료형을 판정하지 않는다. |
| R7:P-014 | 혼합 정밀도 표현 | swanpgr PDF 10쪽, 인쇄 4쪽: `Mixed-mode expressions (single-precision/double-precision) are not used.` | `src/ocpmix.ftn:293` `10  TT   = TIMESC - DBLE(NDAY)*24.*3600.`; 271행 `REAL*8  TT`; 이력: `7ee8981:src/ocpmix.ftn:293` `10  TT   = TIMESC - DBLE(NDAY)*24.*3600.` | C 문서 누락 | DBLE(NDAY)와 단정밀 리터럴을 함께 쓰는 식은 41.51 공개 코드와 현재 코드에서 같다. 혼합 정밀도 금지 규칙에는 이 식을 예외로 적는다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-015 | POINTER·NULLIFY·TARGET | swanpgr PDF 10–11쪽, 인쇄 4–5쪽: `Always initialize pointers with the NULLIFY instruction`; `Use POINTER and TARGET` | `src/SwanConvAccur.ftn90:109` `vert => gridobject%vert_grid`; 이력: `7ee8981:src/SwanConvAccur.ftn90:115` `vert => gridobject%vert_grid` | C 문서 누락 | 41.51 공개 코드도 vert를 NULLIFY 없이 gridobject%vert_grid에 직접 연결한다. NULLIFY만을 초기화 방법으로 설명하지 않는다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-016 | allocatable 우선·종료 해제·STAT | swanpgr PDF 10–11쪽, 인쇄 4–5쪽: `as many allocatable arrays as possible`; `always be deallocated`; `preference is given to the STAT= attribute` | `src/SdsBabanin.ftn90:127` `REAL             , ALLOCATABLE ::  SDS(:)`; 155행 `ALLOCATE(SDS(NFREQ))`; 297행 `DEALLOCATE(SDS)` | H 코드 대조 대상 아님 | 문서는 allocatable 사용을 우선하고 사용이 끝난 배열을 해제하라고 요구한다. STAT=는 선호 사항이다. CALC_SDS는 SDS를 ALLOCATE한 뒤 297행에서 DEALLOCATE한다. 이 구체 경로와 모델 전체의 배열 수명 보장은 구분한다. |
| R7:P-017 | END DO·중첩 종료·루프 이름 | swanpgr PDF 11쪽, 인쇄 5쪽: `Always end a do loop with END DO instead of CONTINUE`; `Use labels to identify the structure` | `src/ocpids.ftn:512` `DO 20 IMM = 1, 12`; 517행 `20    CONTINUE`; 이력: `7ee8981:src/ocpids.ftn:512` `DO 20 IMM = 1, 12                                                  !!`; `7ee8981:src/ocpids.ftn:517` `20    CONTINUE                                                           !!` | C 문서 누락 | 번호가 있는 DO와 CONTINUE의 조합은 41.51 공개 코드에 이미 있다. END DO 작성 규칙에는 이 기존 제어문을 구분한다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-018 | 소문자·공백·배열 구조·보조변수 | swanpgr PDF 11쪽, 인쇄 5쪽: `small letters are recommended`; `Make ample use of spaces`; `where they match the logical structure`; `Do not use special auxiliary variables` | `src/SdsBabanin.ftn90:138` `REAL             , ALLOCATABLE ::  XFF(:),ADF(:) ! temporary arrays` | H 코드 대조 대상 아님 | 소문자·공백·배열 구조·보조변수 설명은 가독성과 구조 적합성에 관한 권고이다. 인용한 XFF·ADF의 temporary arrays 주석만으로 불필요한 보조변수라고 판정하지 않는다. |
| R7:P-019 | SAVE 속성·SAVE 문 금지 | swanpgr PDF 11쪽, 인쇄 5쪽: `Use the SAVE attribute (not the SAVE statement!)`; swanpgr PDF 41쪽, 인쇄 35쪽: `INTEGER :: I, J`; `SAVE IENT`; `RETURN` | `src/SdsBabanin.ftn90:1454` `SAVE IENT`; `src/SwanBndStruc.ftn90:74` `integer, save                        :: ient = 0 ! number of entries in this subroutine` | B 문서·노트 오기 | swanpgr PDF 11쪽은 SAVE 속성을 쓰고 SAVE 문을 쓰지 말라고 한다. 같은 문서 PDF 41쪽의 fixed form 예제는 `SAVE IENT`를 쓴다. 실제 코드에도 SAVE 문과 SAVE 속성 선언이 모두 있다. B는 문서의 규칙과 예제 사이의 불일치이다. [10-13 전수 검증 정정] |
| R7:P-021 | FORMAT 전용 label·오름차순 | swanpgr PDF 11쪽, 인쇄 5쪽: `used exclusively for FORMAT statements`; `ascending order`; 같은 매뉴얼 PDF 13쪽은 오류 처리의 숫자 label 예외를 허용한다. | `src/ocpids.ftn:517` `20    CONTINUE`; 이력: `7ee8981:src/ocpids.ftn:517` `20    CONTINUE                                                           !!` `src/ocpids.ftn:512–517`의 `DO 20 IMM = 1, 12`와 `GOTO 20`은 월 문자열 검색 반복이다. | C 문서 누락 | 41.51 공개 코드도 월 문자열을 찾는 DO 반복에서 `20 CONTINUE`를 쓴다. swanpgr PDF 13쪽의 오류 처리 예외와 이 반복 제어는 다르다. C는 swanpgr의 FORMAT 전용 label 규칙이 이 반복 제어를 설명하지 않는 부분에 한정한다. |
| R7:P-023 | 문자열 비교 | swanpgr PDF 11쪽, 인쇄 5쪽: `Use FORTRAN functions LGE, LGT, LLE, LLT instead.` | `src/ocpids.ftn:514` `IF (MONCI.NE.MONC(IMM)) GOTO 20`; 이력: `7ee8981:src/ocpids.ftn:514` `IF (MONCI.NE.MONC(IMM)) GOTO 20` | C 문서 누락 | MONCI와 MONC의 관계 연산자 비교는 41.51 공개 코드에 이미 있다. LGE·LGT·LLE·LLT만 사용한다는 구현 설명을 쓰지 않는다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-024 | ASCII 변환 함수 | swanpgr PDF 12쪽, 인쇄 6쪽: `Use the IACHAR and ACHAR statements` | `src/ocpids.ftn:193` `TABC = CHAR(9)`; `src/swanser.ftn:6490` `!UNIX      ITABVL = ICHAR('	')`; 이력: `7ee8981:src/ocpids.ftn:193` `TABC = CHAR(9)                                                    40.69`; `7ee8981:src/swanser.ftn:6490` `!UNIX      ITABVL = ICHAR('	')` | C 문서 누락 | 41.51 공개 코드도 CHAR와 ICHAR를 사용한다. IACHAR·ACHAR 작성 규칙과 기존 TAB 처리 구현을 구분한다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-025 | free output 금지·FORMAT·inline 형식 | swanpgr PDF 12쪽, 인쇄 6쪽: `Do not use free format output`; `always use FORMAT statements`; `WRITE statement itself is not recommended` | `src/SdsBabanin.ftn90:1368` `WRITE(*,*)'UFRIC = ',UFRIC`; 이력: `7ee8981:src/SdsBabanin.ftn90:1368` `WRITE(*,*)'UFRIC = ',UFRIC` | C 문서 누락 | 41.51 공개 코드도 ST6 진단에서 WRITE(*,*)를 사용한다. 자유 형식 출력 금지 규칙에는 이 기존 예외를 구분한다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-026 | 배열 전체 표현·데이터 의존성·초기화 | swanpgr PDF 12쪽, 인쇄 6쪽: `Use arrays as units in expressions`; `Avoid data-dependency`; `Initialize every variable` | `src/swanmain.ftn:464` `COMPDA = 0.`; `src/SwanCompUnstruc.ftn90:423` `hsprev = 99999.` | H 코드 대조 대상 아님 | 문서는 배열 전체 표현·데이터 의존성 회피·변수 초기화의 작성 규칙을 제시한다. 코드는 COMPDA를 할당한 분기에서 `COMPDA = 0.`을 실행한다. SwanCompUnstruc은 `hsprev = 99999.`로 초기화한다. 이 사례를 모든 변수·모든 경로의 초기화 보장으로 확대하지 않는다. |
| R7:P-027 | COMMON·EQUIVALENCE·ENTRY·PAUSE·assigned GOTO·alternate RETURN | swanpgr PDF 12쪽, 인쇄 6쪽: `Do not use ... obsolete ... statements` | `src/SwanConvStopc.ftn90:115` `common/convstopc/npacc,nwetp`; 이력: `7ee8981:src/SwanConvStopc.ftn90:119` `common/convstopc/npacc,nwetp` | C 문서 누락 | COMMON 문은 41.51 공개 코드에도 있다. 금지 구문의 제거를 41.51 이후의 변경으로 설명하지 않는다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-028 | 산술 IF·비정수 DO·H descriptor | swanpgr PDF 12쪽, 인쇄 6쪽: `Arithmetic if`; `Non-integer index in a do loop`; `The H edit descriptor` | `src/fftpack51.ftn90:4817` `if (n-2) 300,102,103`; 이력: `7ee8981:src/fftpack51.ftn90:4817` `if (n-2) 300,102,103` | C 문서 누락 | 동봉 FFT 소스의 산술 IF는 41.51 공개 코드에도 있다. 산술 IF 금지 규칙을 동봉 소스 전체의 준수 보증으로 쓰지 않는다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-029 | ERR·END 대신 IOSTAT | swanpgr PDF 12·23쪽, 인쇄 6·17쪽: `use IOSTAT specifier instead` | `src/ocpids.ftn:122` `READ (11, *, ERR=930, END=930) INIVEF`; 이력: `7ee8981:src/ocpids.ftn:122` `READ (11, *, ERR=930, END=930) INIVEF                             10.16` | C 문서 누락 | 41.51 공개 코드도 READ의 ERR·END 지정자를 사용한다. IOSTAT만 사용한다는 구현 설명을 쓰지 않는다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-030 | generic intrinsic | swanpgr PDF 12쪽, 인쇄 6쪽: `ABS instead of CABS or DABS` | `src/SwanBraggScat.ftn90:261` `else if ( ixf >= float(mxg(1)-1) ) then`; 이력: `7ee8981:src/SwanBraggScat.ftn90:261` `else if ( ixf >= float(mxg(1)-1) ) then` | C 문서 누락 | 41.51 공개 코드도 FLOAT를 호출한다. generic intrinsic만 사용한다는 구현 설명을 쓰지 않는다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-031 | 새 비교 연산자 =< | swanpgr PDF 12쪽, 인쇄 6쪽: `>, >=, <, =<, == and /=`; [원본 PDF](../../../models/SWAN/raw/manuals/pdfs/swanpgr.pdf), PDF 12쪽 이미지 `swanpgr-12.png`; `../raw/manuals/website/online_doc/swanpgr/node2.html:260` `=&lt;` | `src/SwanConvAccur.ftn90:213` `if ( hsabs <= max(hsrel,hsoval) .and. tmabs <= max(tmrel,tmoval) ) npacc = npacc + 1.` | B 문서·노트 오기 | PDF 원본의 12쪽과 `swanpgr-12.png`에는 `=<`가 인쇄되어 있다. 웹 node2.html:260에도 `=&lt;`가 있다. 인용한 활성 코드는 `<=`를 사용한다. 문서의 `=<`를 `<=`로 고치는 B 판정을 유지한다. [10-13 전수 검증 정정] |
| R7:P-033 | STOP 예외·오류 처리 | swanpgr PDF 12–13쪽, 인쇄 6–7쪽: `an error subroutine after printing of a fatal error`; `explicit lockup routine` | `src/SdsBabanin.ftn90:1369` `WRITE(*,*)'stopping ; tau_total = ',TAU_TOTAL`; 1370행 `STOP`; 이력: `7ee8981:src/SdsBabanin.ftn90:1369` `WRITE(*,*)'stopping ; tau_total = ',TAU_TOTAL`; `7ee8981:src/SdsBabanin.ftn90:1367` `IF(IS_THIS_A_NAN)THEN`; `7ee8981:src/SdsBabanin.ftn90:1370` `STOP` | C 문서 누락 | ST6 계산 루틴의 NaN 진단과 직접 STOP은 41.51 공개 코드에도 있다. 모든 종료가 공통 오류 루틴을 거친다는 설명을 쓰지 않는다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-034 | 두 선택 초과 SELECT·WHERE·BLAS | swanpgr PDF 13쪽, 인쇄 7쪽: `SELECT CASE`; `Do not use WHERE statements`; `Do not use BLAS routines` | `src/agioncmd.ftn90:1165` `where (abs(values - dummyvalue) < epsilon(1.)) values = fill_value`; 이력: `7ee8981:src/agioncmd.ftn90:1165` `where (abs(values - dummyvalue) < epsilon(1.)) values = fill_value` | C 문서 누락 | netCDF 코드의 WHERE 문은 41.51 공개 코드에도 있다. WHERE 금지 규칙에는 이 기존 예외를 구분한다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-035 | GOTO는 오류 처리만 | swanpgr PDF 13쪽, 인쇄 7쪽: `Do not use a GOTO statement except for error handling` | `src/swanser.ftn:6501` `GOTO 100`; 이력: `7ee8981:src/swanser.ftn:6494` `100 IF (IF .LE. LENTXT .AND. .NOT. FOUND) THEN`; `7ee8981:src/swanser.ftn:6495` `IF (.NOT. (TEXT(IF:IF) .EQ. ' ' .OR.`; `7ee8981:src/swanser.ftn:6496` `&              ICHAR(TEXT(IF:IF)) .EQ. ITABVL)) THEN`; `7ee8981:src/swanser.ftn:6499` `IF = IF + 1`; `7ee8981:src/swanser.ftn:6501` `GOTO 100` | C 문서 누락 | TXPBLA의 GOTO 100은 공백 탐색 반복에 쓰인다. 이 제어문은 41.51 공개 코드에도 있다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-036 | clean loop·분기 이동·가장 긴 내부 루프·첫 인덱스 | swanpgr PDF 13·31쪽, 인쇄 7·25쪽: `if appropriate`; `inner loop is the longest`; `provided the inner loop is long enough` | `src/SwanBraggScat.ftn90:539` `do i=1,n`; 540행 `sx=sx+x(i)` | H 코드 대조 대상 아님 | 문서는 `if appropriate`와 `provided the inner loop is long enough`라는 조건을 둔 성능 권고이다. fit2의 `do i=1,n`은 입력 n에 따라 반복한다. IF·CALL의 존재나 정적 들여쓰기만으로 성능 규칙 위반을 판정하지 않는다. |
| R7:P-037 | 중간 I/O·간접주소·나눗셈·재귀 회피 | swanpgr PDF 13·31쪽, 인쇄 7·25쪽: `unless there is a very good reason`; `Avoid indirect addressing, if possible`; `Avoid division in a do loop`; `Avoid (seemingly) recursions` | `src/SdsBabanin.ftn90:186` `EDENST(IS)=CTMP1/(CG(IS,1)*KWAVE(IS,1)**3)` | H 코드 대조 대상 아님 | 중간 I/O는 충분한 이유가 있을 때 허용하고 간접주소는 가능하면 피하라고 권고한다. CALC_SDS의 인용한 루프는 `EDENST(IS)=CTMP1/(CG(IS,1)*KWAVE(IS,1)**3)`을 계산한다. 나눗셈의 존재를 계산 오류나 정량적 성능 저하로 판정하지 않는다. |
| R7:P-039 | END로만 서브루틴 종료 | swanpgr PDF 15쪽, 인쇄 9쪽: `Exit a subroutine only via END.`; swanpgr PDF 41쪽, 인쇄 35쪽: `INTEGER :: I, J`; `SAVE IENT`; `RETURN` | `src/ocpmix.ftn:1392` `RETURN`; 1394행 `END SUBROUTINE MSGERR` | B 문서·노트 오기 | swanpgr PDF 15쪽은 `Exit a subroutine only via END.`라고 적는다. 같은 문서 PDF 41쪽의 예제는 `RETURN` 다음 `END`를 쓴다. MSGERR도 RETURN 다음 END SUBROUTINE을 둔다. B는 문서 규칙과 문서 예제의 불일치이다. [10-13 전수 검증 정정] |
| R7:P-040 | 모듈 명시 interface·PRIVATE·공유 데이터 | swanpgr PDF 19쪽, 인쇄 13쪽: `Explicit interfaces should be use`; `private by default`; `Modules may not contain data that is shared by different subroutines` | `src/nctablemd.ftn90:27` `private`; `src/SwanCompdata.ftn90:62` `integer                                    :: nbpol  ! total number of boundary polygons`; 이력: `7ee8981:src/nctablemd.ftn90:27` `private`; `7ee8981:src/SwanCompdata.ftn90:59` `integer                                    :: nbpol  ! total number of boundary polygons` | C 문서 누락 | 41.51 공개 코드의 SwanCompdata도 경계 다각형 수를 모듈 데이터로 보유한다. 모듈 공유 데이터 금지를 현재 데이터 구조의 설명으로 쓰지 않는다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-041 | 3칸 들여쓰기·단위 분리 주석·공백·TAB | swanpgr PDF 21쪽, 인쇄 15쪽: `indent by three positions`; `Never use tabs` | `src/swanser.ftn:6489` `!DOS      ITABVL = ICHAR('	')`; 6490행 `!UNIX      ITABVL = ICHAR('	')`; 이력: `7ee8981:src/swanser.ftn:6489` `!DOS      ITABVL = ICHAR('	')` | B 문서·노트 오기 | TAB 문자 리터럴은 41.51 공개 코드에도 있다. 문자열 내용과 코드 들여쓰기를 구분한다. 들여쓰기 폭의 배수 집계를 규칙 위반 수로 쓰지 않는다. [10-13 전수 검증 정정] |
| R7:P-042 | 저자·판·날짜·기계·변경 이유·라이선스·기능·정밀도 경고 | swanpgr PDF 21쪽, 인쇄 15쪽: `Programmer's name`; `Version number followed by the date and machine`; `contain a warning` | `src/swanmain.ftn:231` `!     34.01, Feb. 99: Changed STOP statement in a jump to end of subroutine` | H 코드 대조 대상 아님 | 저자·변경 이유·기계 정보·정밀도 경고는 주석의 내용에 관한 작성 요구이다. 인용한 Updates 주석은 STOP 변경을 설명한다. 표제 문자열의 존재를 모든 설명이 충실하다는 근거로 쓰지 않는다. |
| R7:P-043 | 버전 1.0·major/minor | swanpgr PDF 21쪽, 인쇄 15쪽: `has a start value of 1.0`; `Major modifications ... 1`; swanpgr PDF 40쪽, 인쇄 34쪽: `40.23, Aug. 02: New subroutine` | `src/swanmain.ftn:231` `!     34.01, Feb. 99: Changed STOP statement in a jump to end of subroutine` | B 문서·노트 오기 | swanpgr PDF 21쪽은 루틴 판 번호의 시작값을 1.0으로 정한다. 같은 문서 PDF 40쪽은 `40.23, Aug. 02: New subroutine`을 예시한다. B는 개별 루틴 번호 규칙과 모델 판 번호를 사용한 문서 예제의 불일치이다. [10-13 전수 검증 정정] |
| R7:P-044 | 인자·지역 변수·호출·I/O·오류·의사 코드·FORMAT 위치 | swanpgr PDF 22쪽, 인쇄 16쪽: `Argument variables`; `Local variables`; `Error messages`; `pseudo code`; `Format statements ... at the end` | `src/ocpmix.ftn:1370` `WRITE (PRINTF,12) ERRM, STRING`; 1371행 `12  FORMAT (' ** ', A, ': ',A)`; 이력: `7ee8981:src/ocpmix.ftn:1370` `WRITE (PRINTF,12) ERRM, STRING`; `7ee8981:src/ocpmix.ftn:1371` `12  FORMAT (' ** ', A, ': ',A)`; `7ee8981:src/ocpmix.ftn:1372` `IF (LEV.GT.MAXERR) THEN` | C 문서 누락 | MSGERR의 FORMAT 문은 41.51 공개 코드에서도 실행문 사이에 있다. 모든 FORMAT이 절차 끝에 있다는 구현 설명을 쓰지 않는다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-045 | PRINT 금지·별표 장치·11 미만 장치·장치 변수·일반 할당 | swanpgr PDF 23쪽, 인쇄 17쪽: `Do not use the PRINT statement`; `Never use * as a device number`; `smaller than 11 are prohibited`; swanimp PDF 28쪽, 인쇄 22쪽 및 `../raw/manuals/website/online_doc/swanimp/node19.html:92–97`은 입력·출력 장치 번호 3·4·6을 명시한다. | `src/nctablemd.ftn90:332` `print "(A)", "Could not find ", trim(varname), " in record table"`; `src/ocpids.ftn:181` `INPUTF = 3`; 이력: `7ee8981:src/nctablemd.ftn90:332` `print "(A)", "Could not find ", trim(varname), " in record table"`; `7ee8981:src/ocpids.ftn:181` `INPUTF = 3` | C 문서 누락 | 41.51 공개 코드도 PRINT와 초기 장치 번호 3을 사용한다. I/O 작성 규칙에는 이 기존 예외를 구분한다. 장치 번호는 swanimp에 이미 설명되어 있다. C는 swanpgr 작성 규칙의 기존 예외 누락에 한정한다. |
| R7:P-046 | carriage control·명확한 오류·CLOSE·숫자 FREE·입력 대소문자 | swanpgr PDF 23쪽, 인쇄 17쪽: `Only use a blank for carriage control`; `Close files`; `should not differentiate`; `numerical data should always be free format` | `src/ocpids.ftn:176` `150    CLOSE (11)`; 513행 `CALL UPCASE (MONCI)`; 502행 `READ (TIMSTR, '(I4,I2,I2,1X,3I2)', ERR=98) (DTTIME(II), II=1,6)`; 이력: `7ee8981:src/ocpids.ftn:176` `150    CLOSE (11)`; `7ee8981:src/ocpids.ftn:502` `READ (TIMSTR, '(I4,I2,I2,1X,3I2)', ERR=98) (DTTIME(II), II=1,6)` | C 문서 누락 | 41.51 공개 코드도 날짜 숫자를 명시한 FORMAT으로 읽는다. 모든 숫자 입력이 자유 형식이라는 구현 설명을 쓰지 않는다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-047 | hard·soft 오류·10개 경고·fatal STOP | swanpgr PDF 25쪽, 인쇄 19쪽: `print a maximum of 10 warnings`; `A STOP needs to be built into the calling subroutine after fatal errors`; swanpgr PDF 25쪽은 오류 수에 `for example 10`을 붙인다. swanuse PDF 36쪽과 `../raw/manuals/website/online_doc/swanuse/node23.html:221–234`는 MAXMES의 계산 중 오류 메시지 한도와 기본값 200을 설명한다. | `src/ocpmix.ftn:1358` `IF (LEV.GT.LEVERR) LEVERR=LEV`; 1482행 `IF (LEVERR .GE. 4) THEN`; `src/swanmain.ftn:1625` `MAXMES = 200`; 이력: `7ee8981:src/ocpmix.ftn:1358` `IF (LEV.GT.LEVERR) LEVERR=LEV`; `7ee8981:src/swanmain.ftn:1624` `MAXMES = 200`; `7ee8981:src/ocpmix.ftn:1482` `IF (LEVERR .GE. 4) THEN` `src/ocpmix.ftn:1358–1370`의 MSGERR는 `LEV.EQ.1`이면 Warning을 선택하고 호출마다 PRINTF로 출력한다. 1487–1488행은 `IF (MAXERR.EQ.-1) STPNOW = .FALSE.`와 OpenMP 활성문의 `!$    IF (OMP_IN_PARALLEL()) STPNOW = .FALSE.`이다. | C 문서 누락 | swanpgr의 오류 10회는 예시이고 경고 출력 최대 10회는 규칙이다. MSGERR의 인용한 출력 경로에는 경고 횟수 상한이 없다. STPNOW는 `IF (LEVERR .GE. 4) THEN`에서 참이 되지만 MAXERR=-1 또는 OpenMP 병렬 구간이면 거짓으로 바꾼다. swanuse의 MAXMES=200은 계산 중 오류 메시지 한도이다. C는 swanpgr의 경고·종료 규칙과 이 기존 처리의 차이에 한정한다. |
| R7:P-048 | 의사 코드 수식·제어·I/O 파일·:=·DIV/MOD·외부 상세 참조 | swanpgr PDF 27–29쪽, 인쇄 21–23쪽: `Use superscripts and subscripts`; `STDIN and STDOUT`; `:= is preferred`; `sufficient to refer to a document` | `src/SwanConvAccur.ftn90:101` `!   Description of the pseudo code` | H 코드 대조 대상 아님 | 의사 코드의 수식·파일명·연산자 표기는 설명의 작성 규칙이다. SwanConvAccur:101은 `Description of the pseudo code`라는 자리표시 주석이다. 이 표제만으로 임의 프로그래머가 구현할 수 있는 설명이라고 판단하지 않는다. |
| R7:P-049 | 기계 종속 정밀도·ce 전환 | swanpgr PDF 33쪽, 인쇄 27쪽: `DOUBLE PRECISION or COMPLEX * 16`; `letter combination ce` | `src/SwanBraggScat.ftn90:526` `real*8 a,b,c,x(n),y(n),z(n)`; 이력: `7ee8981:src/SwanBraggScat.ftn90:526` `real*8 a,b,c,x(n),y(n),z(n)` | C 문서 누락 | 41.51 공개 코드도 fit2에서 REAL*8을 직접 선언한다. 이 선언을 41.51 이후의 정밀도 정책 변경으로 설명하지 않는다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-050 | OPEN 집중·기계 상수·plot 호출 분리 | swanpgr PDF 33–34쪽, 인쇄 27–28쪽: `as many open statements as possible in one machine-dependent subroutine`; `recommended`; `plot routine` | `src/ocpmix.ftn:1386` `OPEN (UNIT=IERRF, FILE=ERRFNM, FORM='FORMATTED')`; `src/swanout2.ftn:970` `OPEN(UNIT=UVTK, FILE=VTKFIL, FORM='UNFORMATTED',` | H 코드 대조 대상 아님 | 문서는 가능한 한 OPEN을 한 루틴에 모으고 기계 상수 초기화를 모듈로 공유하라고 권고한다. MSGERR의 오류 파일 OPEN과 swanout2의 VTK OPEN은 다른 루틴에 있다. 분산된 OPEN의 존재만으로 이 조건부 권고의 위반이나 실행 결함을 판정하지 않는다. |
| R7:P-051 | 배열 rank·시작주소 예외·최상위만 허용 | swanpgr PDF 35쪽, 인쇄 29쪽: `arrays are transferred by using the start address`; `except in the top layer of subroutines the user needs to handle` | `src/SwanCompUnstruc.ftn90:867` `call SwanGradDepthorK ( compda(1,JDP2), compda(1,JMUDL2), spcsig, dhdx, dhdy, dkdx, dkdy, ivert )`; 이력: `7ee8981:src/SwanCompUnstruc.ftn90:870` `call SwanGradDepthorK ( compda(1,JDP2), compda(1,JMUDL2), spcsig, dhdx, dhdy, dkdx, dkdy, ivert )` | C 문서 누락 | 내부 계산 루틴이 COMPDA 원소를 배열 시작주소로 전달하는 호출은 41.51 공개 코드에도 있다. 이 호출을 41.51 이후 추가된 예외로 설명하지 않는다. C는 swanpgr 작성 규칙에 기존 구현 예외가 표시되지 않은 부분에 한정한다. |
| R7:P-052 | sw·swmod 이름 권고 | swanpgr PDF 37쪽, 인쇄 31쪽: `suggestion is to start all SWAN routines with ... sw`; `swmod ... 3-digit symbol` | `src/SdsBabanin.ftn90:7` `SUBROUTINE CALC_SDS(NFREQ,EDENS,F,KDS,ANAR_IN,TESTFL,KWAVE,CG)` | H 코드 대조 대상 아님 | 문서는 최상위 루틴 이름을 자유롭게 정할 수 있다고 한다. 하위 루틴의 sw 접두어와 모듈의 swmod 접두어는 제안이다. CALC_SDS의 이름이 sw로 시작하지 않는다는 사실을 강제 규칙 위반으로 판정하지 않는다. |
| R7:P-053 | ASCII 이름·기능 목록 유지 | swanpgr PDF 37쪽, 인쇄 31쪽: `an ASCII file with applied subroutine names and modules is kept up-to-date` | `src/srclist.cmake:1` `set( swan_src`; `src/swancom4.ftn:49` `!     SWFTIM  (triad-wave interactions calculated using the full integration`; `2980d1a:src/srclist.cmake:1` `set( swan_src`; 41.45부터 `43e9bbb`까지 조사한 Git 이력에서 별도 목록 경로 `*subrout*`, `*routinelist*`, `*routine-list*`는 0커밋이다. [확정 검색 근거](../../../_staging/recovery/compare/SWAN-git-verify-D.md). | D 현재 해당 구현 없음 | 문서가 말한 이름·모듈·기능의 별도 ASCII 통합목록은 조사한 Git 배포에 없다. srclist.cmake는 빌드 파일 목록이다. 소스 파일별 루틴 설명은 별도로 존재한다. [10-13 전수 검증 정정] |
| R7:P-054 | fixed·free 서브루틴·모듈 예제 | swanpgr PDF 39–48쪽, 인쇄 33–42쪽: `SWBODY`; `SwanRoutineBody`; `MODBODY`; `SwanModuleBody`; swanpgr PDF 41쪽, 인쇄 35쪽: `INTEGER :: I, J`; `SAVE IENT`; `RETURN` | `src/SdsBabanin.ftn90:1456` `IF (LTRACE) CALL STRACE (IENT,'SWIND0_NRL')` | B 문서·노트 오기 | swanpgr PDF 39–48쪽은 fixed form·free form 예제를 제공한다. PDF 41쪽의 `INTEGER :: I, J`, `SAVE IENT`, `RETURN`은 같은 문서의 변수당 선언·SAVE 속성·END 종료 규칙과 다르다. B는 예제가 규칙을 준수한다는 문서 내부 설명의 불일치이다. [10-13 전수 검증 정정] |
| R7:P-055 | 서지·수정 이력·서문 | swanpgr PDF 7·49·51쪽, 인쇄 1·43·45쪽: `no final status`; `Initial document`; `Translation into English` | `README.md:30` `This Readme provides a brief overview of software installation and configuration instructions for users and developers.` | H 코드 대조 대상 아님 | Chapman 1998과 Morgan·Schonfelder 1993은 참고 서지이다. 2005–2006년 문서 변경 표는 소스 변경 내역이 아니다. 표지·저작권·목차·빈 쪽에도 실행 코드 명제가 없다. |
| R7:N-022 | 비교 연산자 오기 | `swan-programming-rules.md:48` ``- intrinsic 은 **generic name**(`ABS`, not `CABS`/`DABS`). 신규는 `>`,`>=`,`<`,`=<`,`==`,`/=`(기존은 `.GT.` 등 허용).``; swanpgr PDF 12쪽(인쇄 6쪽), 쪽 이미지 `swanpgr-12.png`, `../raw/manuals/website/online_doc/swanpgr/node2.html:260`에도 `=<`가 있다. | `src/SwanConvAccur.ftn90:213` `if ( hsabs <= max(hsrel,hsoval) .and. tmabs <= max(tmrel,tmoval) ) npacc = npacc + 1.` | B 문서 오기 | 쪽 이미지에서도 원문의 =< 인쇄를 확인했다. 노트는 이를 그대로 옮겼다. 원문을 인용할 때 =<를 보존하고 오기임을 표시한다. 코드가 사용하는 Fortran 연산자는 <=이다. |
| R7:N-023 | trace 파일 수와 준수 의미 | `swan-programming-rules.md:65` ``> 매뉴얼이 SWAN 프로그램·서브루틴에 요구하는 **표준 layout**이다. nesting indent **3 칸**, **tab 절대 금지**(이식성). 실제 준수는 `src/` 소스 **75개 중 63개**가 `CALL STRACE` 진입부 패턴을 포함하는 수준이다.`` | `src/SdsBabanin.ftn90:1456` `IF (LTRACE) CALL STRACE (IENT,'SWIND0_NRL')`; 이력 대조: `7ee8981 2024-09-02 initial release (v 41.51)`; `7ee8981:src/SwanThreadBounds.ftn90:85` `    if (ltrace) call strace (ient,'SwanThreadBounds')`; `git show 7ee8981:src`의 직속 .ftn·.ftn90 파일은 76개이다. 기본 -unix 치환 후 활성 CALL STRACE가 있는 파일은 63개이다. 활성 호출행은 293개이다.; `0dabfa4 2026-07-13 updated src (patch B)`; `git show 0dabfa4 -- src/SwanThreadBounds.ftn90` 원문 `deleted file mode 100644`; `43e9bbb:src/SdsBabanin.ftn90:1456` `      IF (LTRACE) CALL STRACE (IENT,'SWIND0_NRL')`; 같은 집계에서 현재 파일은 75개이다. 활성 호출 파일은 62개이다. 활성 호출행은 292개이다. | A 확정 (0dabfa4 2026-07-13) | patch B의 SwanThreadBounds 삭제로 활성 STRACE 파일과 호출행이 각각 하나 줄었다. 현재 집계는 75파일 중 62파일과 호출행 292개이다. 노트의 총 75파일은 문서 시점의 총 76파일과 다르다. 노트의 STRACE 63파일은 현재 62파일과 다르다. STRACE 호출은 표준 주석 layout 전체의 준수율이 아니다. git 판정 근거는 `0dabfa4`(2026-07-13)이다. [10-13 전수 검증 정정] |
| R7:N-024 | SAVE 규칙과 예제 충돌 | `swan-programming-rules.md:43` ``- 다음 call 까지 값 유지 = **`SAVE` attribute**(statement 아님).``; 같은 노트 135행은 `SAVE IENT`이다. swanpgr PDF 11쪽(인쇄 5쪽)의 규칙과 PDF 41쪽(인쇄 35쪽)의 fixed form 예제가 서로 다르다. `../raw/manuals/website/online_doc/swanpgr/node2.html:172–173`, `../raw/manuals/website/online_doc/swanpgr/node16.html:154,236`. | `src/SdsBabanin.ftn90:1454` `SAVE IENT`. | B 문서 오기 | 원문은 SAVE 속성을 요구하면서 fixed form 예제에는 SAVE IENT 문을 쓴다. B는 문서 내부의 규칙·예제 불일치이다. 노트가 규칙을 잘못 옮긴 것은 아니다. 실제 코드의 SAVE 문을 함께 적는다. |
