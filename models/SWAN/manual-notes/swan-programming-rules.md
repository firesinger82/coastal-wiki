---
title: "SWAN Programming Rules (swanpgr v1.3) — ANSI F90 standards + control/module/layout rules + 13-section subroutine template + naming(sw/swmod) + STRACE/IENT verbatim"
topic: swan
canonical_source: external
external_source: "swanpgr (SWAN Programming Rules, Version 1.3, SWAN team, 2006-03-22). Chapters 1 Introduction / 2 FORTRAN 90 standards / 3 Control statements / 4 Use of modules / 5 Program layout / 6 Input-output / 7 Error messages / 8 Pseudo code / 9 Performance / 10 Machine dependency / 11 Exceptions / 12 Names / 13 Examples(templates) / Bibliography / Log sheet."
citation_status: verified
verification_method: "models/SWAN/raw/manuals/website_markdown/online_doc/swanpgr/ node1-18.md 전 노드 직접 read. F90 규칙·control 구문·module 규약·13-section layout·subroutine/module template·naming 규약 verbatim. source-analysis 의 실제 SWAN 서브루틴 주석블록 구조와 cross-check."
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
- **`IMPLICIT NONE`** + 모든 변수 명시 선언 + `INTENT`. 단 implicit 관례 유지: `i`-`n` = integer, `c`/`z` = complex, 나머지 = real.
- 변수 1개당 선언문 1개. 선언에 **항상 `::`**. **알파벳 순**. 첫 몇 글자로 구별 가능. 의미있는(영어) 이름.
- `INTEGER IARRAY(100)` (type 선언) > `DIMENSION IARRAY(100)`. array dimension 에 real 식 금지. **mixed-mode(single/double) 식 금지**.
- pointer 는 항상 `NULLIFY` 초기화. **allocatable array 우선**(heap; automatic array=stack overflow 위험). 미사용 allocatable 은 서브루틴 끝에서 deallocate. validity check 는 `STAT=`. 길이 미지/대형 데이터·linked list 는 `POINTER`+`TARGET`.
- **`END DO`**(`CONTINUE` 금지), nested 는 각자 `END DO`. do loop 구조 label 로 가독성.
- 소문자 권장. space·comment block·줄간격 충분히. multi-dim array 는 논리구조 일치 시.
- 다음 call 까지 값 유지 = **`SAVE` attribute**(statement 아님).
- constant 는 `parameter` statement(unit number·array dim·물리/수치 상수 한 곳 정의). 예 `PI = 4.*ATAN(1.)`.
- statement label: **FORMAT 전용** + 오름차순.
- character: argument 전달은 `CHARACTER(LEN=*)`, 길이는 `LEN` intrinsic(전달 금지). relational(`.LT.` 등) 대신 `LGE/LGT/LLE/LLT`. ASCII/EBCDIC 비의존 위해 `ICHAR/CHAR` 대신 **`IACHAR/ACHAR`**.
- **obsolete F77 금지**: statement function, assigned goto, named/blank common, arithmetic if, `EQUIVALENCE`, `ENTRY`, `ERR=`/`END=`(→`IOSTAT`), `PAUSE`, multiple entry/return, IF block 외부서 ENDIF jump, non-integer do index, H edit descriptor.
- intrinsic 은 **generic name**(`ABS`, not `CABS`/`DABS`). 신규는 `>`,`>=`,`<`,`=<`,`==`,`/=`(기존은 `.GT.` 등 허용).
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

> source-analysis 의 모든 SWAN 서브루틴이 따르는 **표준 layout**. nesting indent **3 칸**, **tab 절대 금지**(이식성).

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

- top-level 서브루틴은 임의 이름(mnemonic). 하위 서브루틴은 name conflict 방지 위해 **`sw` 로 시작** 권장. module 은 **`swmod` + 3-digit**(예 `swmod1`/`swmod2` — [[swan-implementation-manual]] §2 의 general modules 와 일치).
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

→ **`SAVE IENT`/`DATA IENT/0/` + `IF(LTRACE) CALL STRACE(IENT,'name')`** 패턴 = 모든 SWAN 서브루틴 진입부 trace. source-analysis 노트에서 반복 관찰되는 구조의 공식 근거.

## 14. 메타 (node17-18)

- Bibliography: [1] Chapman S.J.(1998) *Fortran 90/95 for scientists and engineers*, WCB McGraw-Hill / [2] Morgan J.S. & Schonfelder J.L.(1993) *Programming in Fortran 90*, Alfred Waller.
- Log sheet: v1.0(2005-04-28 initial) → v1.1(2005-05-19 RWS-RIKZ 코멘트) → **v1.2(2006-01-10 영어 번역)** → **v1.3(2006-03-22 minor + 확장)**. → swanpgr 는 **2006년 이후 본문 미갱신**(swanimp/swanuse/swantech 가 41.51 인 것과 대조).

## 15. 연결

- [[swan-documentation-stack]] — 4 docs (본 노트가 swanpgr deep 화)
- [[swan-implementation-manual]] — swanimp (ANSI F90 한계·switch·`swmod` module 명명 cross-ref)
- [[swan-source-coverage-audit]] / [[swan-foundation]] — §5 13-section layout + §13 STRACE/IENT 가 실제 소스에서 관찰되는 곳
- 공식: http://www.swan.tudelft.nl
