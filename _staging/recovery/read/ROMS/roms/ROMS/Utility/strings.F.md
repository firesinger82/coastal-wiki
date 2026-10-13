---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/strings.F
lines: 632
sha256: 18a28383d60b90475cb632008a29eef575c5015033ca7c0dd4fc60acbeac44c7
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# strings.F — 판독 구간 기록

구간은 1행부터 632행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–50 | `#include "cppdefs.h"` (1)로 cppdefs.h를 포함한다. strings_mod 모듈·저작권과 오류 확인·표준 이름·문자열 할당·검색·결합·대소문자 변환 절차 목록(2–33). find_string·lowercase·uppercase 사용 예는 주석이다(25–31). implicit none·PRIVATE·9개 공개 절차·CONTAINS 및 빈 주석(35–50). |
| 51–102 | FoundError 시작·flag와 NoErr 비교 설명(51–70). stdout·Master 사용, 정수 flag·NoErr·line과 routine 문자열 및 logical 결과 선언(72–83). foundit 거짓(89). `IF (flag.ne.NoErr) THEN` (90)이면 foundit 참(91), `IF (Master) THEN` (92)에서 오류 값·호출 행·루틴 출력(93–95). 출력 조건 밖에서 FLUSH(stdout)(97). 조건·함수 종료·빈 주석(98–102). |
| 103–155 | GlobalError 시작(103–104). 분리 통신자(communicator)에서 모든 프로세스가 호출한다는 설명(108–130). mod_parallel·stdout 사용(134–135). `#if defined DISTRIBUTE && defined DISJOINTED` (137)에서 mp_barrier·mp_bcasti를 가져오며 `#endif` (139). flag는 intent(inout), ng·model·NoErr·line과 routine은 입력(143–146). 결과·MasterProcess 선언(150–151), `#ifdef DISTRIBUTE` (152)에서 MyCOMM 선언, `#endif` (154). |
| 156–197 | 시작 시 103행 GlobalError 안. `#ifdef DISTRIBUTE` (158)·`#endif` (161)은 설명 주석을 감싼다. `#ifdef DISTRIBUTE` (164), `# ifdef DISJOINTED` (165)는 MyCOMM=FULL_COMM_WORLD(166), `MasterProcess=FullRank.eq.0` (167). `# else` (168)는 MyCOMM=OCN_COMM_WORLD(169), `MasterProcess=MyRank.eq.0` (170). `# endif` (171), `#else` (172)는 MasterProcess=Master(173), `#endif` (174). `#if defined DISTRIBUTE && defined DISJOINTED` (175)에서 mp_bcasti(ng,model,flag,MyCOMM)(177), `#endif` (178). foundit 거짓(184), `IF (flag.ne.NoErr) THEN` (185)이면 참(186), `IF (MasterProcess) THEN` (187)에서 로그(188–190), 그 조건 밖에서 FLUSH(stdout)(192). RETURN·함수 종료·빈 주석(195–197). |
| 198–250 | TaskError 시작(198–199). 작업 통신자에서 모든 프로세스가 호출한다는 설명(201–227). mod_parallel·stdout 사용(229–230), `#if defined DISTRIBUTE && defined DISJOINTED` (232)에서 mp_barrier·mp_bcasti 가져옴(233), `#endif` (234). flag intent(inout), ng·model·NoErr·line·routine 입력(238–241). 결과·MasterProcess와 `#ifdef DISTRIBUTE` (247) 안의 MyCOMM 선언(248), `#endif` (249). |
| 251–297 | 시작 시 198행 TaskError 안. `#ifdef DISTRIBUTE` (253)·`#endif` (256)은 설명 주석. `#ifdef DISTRIBUTE` (259), `# ifdef DISJOINTED` (260), `#  ifdef CONCURRENT_KERNEL` (261)은 MyCOMM=TASK_COMM_WORLD(262), `MasterProcess=TaskRank.eq.0` (263). `#  else` (264)는 MyCOMM=FULL_COMM_WORLD(265), `MasterProcess=FullRank.eq.0` (266). `#  endif` (267), `# else` (268)는 MyCOMM=OCN_COMM_WORLD(269), `MasterProcess=MyRank.eq.0` (270). `# endif` (271), `#else` (272)는 MasterProcess=Master(273), `#endif` (274). `#if defined DISTRIBUTE && defined DISJOINTED` (275)은 mp_bcasti(ng,model,flag,MyCOMM)(277), `#endif` (278). foundit 거짓(284), `IF (flag.ne.NoErr) THEN` (285)에서 참(286), `IF (MasterProcess) THEN` (287)에서 로그(288–290). 그 조건 밖에서 FLUSH(stdout)(292). RETURN·함수 종료·빈 주석(295–297). |
| 298–366 | StandardName 시작·standard_name 결합 설명·variable·선택 prefix/suffix·출력 Sname·지역 정수 선언(298–327). i=1:LEN(Sname) 루프에서 CHAR(32)로 공백을 채운다(333–335). `Lstr=LEN_TRIM(variable)` (339), `Icomma=INDEX(variable,CHAR(44),BACK=.FALSE.)` (340). `IF (Icomma.gt.0) THEN                               ! remove comma` (341)일 때 `Sname=variable(1:Icomma-1) // variable(Icomma+1:Lstr)` (342), `Lstr=LEN_TRIM(Sname)` (343). `ELSE` (344)는 variable 부분 복사(345). i=1:Lstr 루프(348)에서 `IF (Sname(i:i).eq.CHAR(32)) THEN` (349)이면 `Sname(i:i)=CHAR(95)` (350). `IF (PRESENT(prefix)) THEN` (356)은 `Sname=TRIM(ADJUSTL(prefix)) // TRIM(ADJUSTL(Sname))` (357). `IF (PRESENT(suffix)) THEN` (360)은 `Sname=TRIM(ADJUSTL(Sname)) // TRIM(ADJUSTL(suffix))` (361). RETURN·루틴 종료·빈 주석(364–366). |
| 367–400 | assign_string 시작·할당 가능한 문자열 재할당 설명(367–383). A는 길이 지연(deferred length) allocatable intent(inout), string은 입력(387–388). lstr·ErrFlag 정수 선언·할당 주석(392–398). `ErrFlag=-1` (399)로 시작한다. |
| 401–415 | 시작 시 367행 assign_string 안. `lstr=LEN_TRIM(string)` (401). `IF (.not.allocated(A)) THEN` (402)은 길이 lstr의 A를 STAT=ErrFlag로 할당(403). `ELSE` (404)는 A 해제 후 같은 길이로 재할당(405–406). 조건 종료(407) 뒤 A에 원래 string을 대입한다(411). RETURN·함수 종료·빈 주석(413–415). |
| 416–468 | find_string 시작·문자열 배열 검색 설명·입출력 선언(416–444). A 크기는 Asize이며 Aindex는 출력이다. logical 결과와 i 선언(448–450). foundit 거짓·Aindex=0 초기화(456–457). i=1:Asize(458)에서 `IF (TRIM(A(i)).eq.TRIM(string)) THEN` (459)이면 foundit 참·Aindex=i·EXIT(460–462). RETURN·함수 종료·빈 주석(466–468). |
| 469–529 | join_string 시작·쉼표 결합 설명·A(Asize) 입력과 string·Lstring 출력 및 지역 정수 선언(469–499). `lstr=LEN(string)` (507), i=1:lstr에서 문자열을 공백으로 초기화(508–510). `is=1` (514), i=1:Asize(515)에서 `lstr=LEN_TRIM(A(i))` (516). `IF (lstr.gt.0) THEN` (517)일 때 `ie=is+lstr-1` (518), `string(is:ie)=TRIM(A(i))` (519), `is=ie+1` (520), `string(is:is)=','` (521), `is=is+2` (522). 루프 종료 뒤 `Lstring=LEN_TRIM(string)-1` (525). RETURN·루틴 종료·빈 주석(527–529). |
| 530–580 | lowercase 시작·소문자 변환 설명과 주석 참고문헌 Cooper Redwine 1995(530–550). Sinp 입력·동일 길이 Sout·정수 선언(554–560). `character (26), parameter :: Lcase = 'abcdefghijklmnopqrstuvwxyz'` (562), `character (26), parameter :: Ucase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'` (563). `lstr=LEN(Sinp)` (569), Sout 복사(570), i=1:lstr(571)에서 `j=INDEX(Ucase, Sout(i:i))` (572). `IF (j.ne.0) THEN` (573)이면 `Sout(i:i)=Lcase(j:j)` (574). RETURN·함수 종료·빈 주석(578–580). |
| 581–632 | uppercase 시작·대문자 변환 설명·같은 주석 참고문헌(581–601). Sinp 입력·동일 길이 Sout·정수 선언(605–611). `character (26), parameter :: Lcase = 'abcdefghijklmnopqrstuvwxyz'` (613), `character (26), parameter :: Ucase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'` (614). `lstr=LEN(Sinp)` (620), Sout 복사(621), i=1:lstr(622)에서 `j=INDEX(Lcase, Sout(i:i))` (623). `IF (j.ne.0) THEN` (624)이면 `Sout(i:i)=Ucase(j:j)` (625). RETURN·함수·모듈 종료(629–632). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 138·177·233·277: GlobalError·TaskError는 mp_barrier를 가져오지만 호출하지 않는다. mp_bcasti 호출은 DISTRIBUTE와 DISJOINTED가 모두 정의된 경우에만 포함된다.
- 302–304·339–361: 설명은 prefix의 공백을 밑줄로 바꾼다고 적는다. 실제 공백 치환 루프는 variable을 복사한 Sname에 적용한다. prefix·suffix는 그 루프 뒤에 연결한다. 쉼표 제거는 INDEX로 찾은 첫 쉼표에만 적용한다.
- 399–411: assign_string은 할당의 STAT를 ErrFlag에 받는다. A=string 앞에는 ErrFlag 조건 검사가 없다. 할당 길이는 LEN_TRIM(string)이며 대입 값은 원래 string이다.
- 514–525: join_string의 부분 문자열 쓰기 앞에는 출력 문자열 길이와 ie·is를 비교하는 조건이 없다. 각 비어 있지 않은 요소 뒤에 쉼표를 기록한다. 마지막 쉼표를 제거하는 대입 없이 Lstring만 LEN_TRIM(string)-1로 계산한다. 모든 요소가 비어 있으면 이 식은 -1을 반환한다.
