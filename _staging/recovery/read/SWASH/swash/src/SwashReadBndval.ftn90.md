---
file: models/SWASH/raw/source_code/swash/src/SwashReadBndval.ftn90
lines: 264
sha256: bf4634ffb8c6cebba5a4ed1b17172e05a4c1ab1b7633d993dfddcbb8369105c7
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashReadBndval.ftn90 — 판독 구간 기록

구간은 1행부터 264행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | `SwashReadBndval ( bfiled, bctime, bcloc, bndval )` 입구(1). 소속·작성자·SWASH 설명·2010–2026 저작권·GPL 3 이상·무보증 머리말(2–29). Marcel Zijlema와 2010년 2월 신규 루틴 이력(30–36). 목적 주석은 경계 파일의 경계값(boundary value)을 읽어 저장한다고 적는다(38–40). `ocpcomm2`, `ocpcomm4`, `SwashCommdata3`, `SwashTimecomm`을 사용하고 `implicit none`을 선언한다(42–49). 전처리는 `models/SWASH/raw/source_code/swash/switch.pl` 57–66행의 표시 제거 규칙을 따른다. `!TIMG`·`!MPI`·`!F95`·`!DOS`·`!UNIX`·`!/Cray`·`!/SGI`·`!/impi`·`!CVIS`·`!MatL4`는 해당 스위치가 켜질 때만 제거되어 코드가 된다. `!DIFF`·`!MUD`·`!TEST`·`!VEGE`는 그 규칙에 없으므로 주석으로 남는다. 이 대상 파일에는 위 표시 행이 없다. |
| 50–88 | 시작 시 1행 SwashReadBndval 안. 인수는 정수 `bfiled(20)` 파일 정보, 정수 `bcloc(nbval)` 저장 위치, 배정밀도 `bctime(2)` 시간, 실수 `bndval(nbval,2)` 두 시간 수준 값이다(53–57). 지역 `binfo` 주석은 0=시계열(time series), 1=1차원 스펙트럼(spectrum), 2=2차원 스펙트럼을 적는다(61–64). 정수 루프·파일 단위·시간 코드 변수, `ient = 0` 저장 변수, 실수 경계값·배정밀도 시간·시간 보간(interpolation) 가중치, 문자 버퍼를 선언한다(65–81). 구조·의사코드·실행부 구분 주석까지 포함한다(82–88). |
| 89–119 | 시작 시 1행 SwashReadBndval 안. 추적 조건은 `if (ltrace) call strace (ient,'SwashReadBndval')` (89). 파일 소진 조건은 `if ( bfiled(1) == -1 ) return` (93). `bctime`에서 이전·현재 판독 시간을, `bfiled(6:7)`에서 시간 코드·정보 형식을 복사한다(95–98). 진단 조건은 `if ( ITEST >= 120 ) write (PRINTF, 201) bfiled(1), binfo, timf1, timf2, timco` (100). `bcloop: do` (102) 안에서 `if ( timco > timf2 ) then` (106)이면 현재 경계값을 이전 시간 열로 옮긴다. `do i = 1, bfiled(8)` (112)에서 `bcloc(i)` 위치의 2열을 1열로 복사한다(113–115). 파일명 목록·데이터 파일 단위를 `bfiled(4:5)`에서 받는다(117–118). 이전 판독 시간도 `timf1 = timf2` (110)로 갱신한다. 106행 `if ( timco > timf2 ) then`은 243행 `endif`에서 닫힌다. 102행 `bcloop: do`는 245행 `enddo bcloop`에서 닫힌다. [10-15 전수 검증 보완] |
| 120–145 | 시작 시 1행 SwashReadBndval·102행 `bcloop: do`(245행 종료)·106행 `if ( timco > timf2 ) then`의 참 분기(243행 종료) 안. 표지 100의 조건은 `if ( .not. bfiled(1) > 0 ) timf2 = 0.` (120). `do i = 1, bfiled(15)` (124)에서 시간 단계별 머리말을 읽으며 EOF는 110, 오류는 910으로 이동한다(125). 로그 조건은 `if ( ITEST >= 90 ) write (PRINTF, 202) hedlin` (126), `if ( ITEST >= 60 ) write (PRINTF, 203) timf1, timf2, timco, bfiled(8), bfiled(15)` (129). `do i = 1, bfiled(8)` (133)에서 저장 위치를 복사하고 `do j = 1, bfiled(16)` (139)으로 각 경계값의 머리말을 읽는다(140). 로그 조건은 `if ( ITEST >= 100 ) write (PRINTF, 202) hedlin` (141). 주석·빈 구분 행까지 포함한다. 140행도 `read (ndsd, '(a)', end=110, err=910) hedlin`이므로 EOF는 110으로 이동한다. 140행의 판독 오류는 910으로 이동한다. 133행 `do i = 1, bfiled(8)`은 167행 `enddo`에서 닫힌다. [10-15 전수 검증 보완] |
| 146–174 | 시작 시 1행 SwashReadBndval·102행 `bcloop: do`(245행 종료)·106행 `if ( timco > timf2 ) then`의 참 분기(243행 종료)·133행 `do i = 1, bfiled(8)`(167행 종료) 안. `if ( binfo == 0 ) then` (146)에서만 경계값을 읽는다. `if ( iiopt == 0 ) then` (148)은 자유 형식으로 `timf2, bval`을 읽는다(150). `else` (152)는 문자열 머리말 판독, `LSPLIT (hedlin, datitm, 2)`, `DTRETI (datitm(1), iiopt, timf2)`, `datitm(2)`의 `(g20.0)` 판독을 수행한다(154–157). 로그 조건은 `if ( ITEST >= 60 ) write (PRTEST, *) ' boundary value ', timf2, bval` (161). `bctime(2)`와 해당 위치 2열에 판독 결과를 저장한다(162–163). 분기·i 루프 종료 뒤 `if ( ITEST >= 60 ) write (PRINTF, 204) binfo, timf2` (169), `cycle bcloop` (173)로 다시 시간 조건을 검사한다. 150행과 154행의 외부 파일 판독은 `end=110`을 지정한다. 두 판독문과 157행의 내부 판독문에는 `err=` 지정이 없다. 146행 조건은 165행 `endif`에서 닫힌다. 이 조건에는 `else`가 없다. [10-15 전수 검증 보완] |
| 175–217 | 시작 시 1행 SwashReadBndval·102행 `bcloop: do`(245행 종료)·106행 `if ( timco > timf2 ) then`의 참 분기(243행 종료) 안. EOF 표지 110에서 데이터 파일을 닫는다(177). `if ( ndsl > 0 ) then` (181)이면 목록에서 `FILENM`을 읽고 FORMATTED/OLD로 다음 파일을 연다(183–184). 목록 EOF는 120, 목록 판독·파일 열기 오류는 920이다. `do i = 1, bfiled(14)` (186)의 파일 머리말 판독은 EOF=930·오류=910이며(188), `if ( ITEST >= 80 ) write (PRINTF, 202) hedlin` (189)로 출력한다. 이후 `goto 100` (194). `else` (196)는 단일 파일 경로이며 `goto 130` (199). 표지 120에서 목록을 닫고 `bfiled(5) = 0`으로 설정한다(205–207). 표지 130에서 `msgerr (1, 'data on boundary file exhausted')` 호출(211), `bfiled(4) = 0`, `bfiled(1) = -1`, `timf2     = 999999999.` (213–215), `cycle bcloop` (216). 181행 조건은 201행 `endif`에서 닫힌다. [10-15 전수 검증 보완] |
| 218–245 | 시작 시 1행 SwashReadBndval·102행 `bcloop: do`(245행 종료) 안이며 106행 `if ( timco > timf2 ) then`의 `else` (218, 243행 종료). 시간 보간 조건은 `if ( timf1 /= timf2 ) then` (222). 참이면 `wf1 = ( timf2 - timco ) / ( timf2 - timf1 )` (223), `else` (224)는 `wf1 = 0.` (225). 그 조건 밖에서 `wf2 = 1. - wf1` (227). `do i = 1, bfiled(8)` (229)에서 위치를 받으며 로그 조건은 `if ( i == 1 .and. ITEST >= 80 ) write (PRTEST, 205) timco, wf1, timf1, timf2, ibloc` (231). 보간식은 `bndval(ibloc,1) = wf1 * bndval(ibloc,1) + wf2 * bndval(ibloc,2)` (235). 주석은 보간값을 반드시 1열에 저장하라고 적는다(233). 루프 종료 뒤 `bctime(1)=timco`, `bctime(2)=timf2` 저장(238–239), `exit bcloop` (241), 시간 분기·bcloop 종료(243–245). [10-15 전수 검증 보완] |
| 246–264 | 시작 시 1행 SwashReadBndval 안. 정상 `return` (247). 진단용 format 201–205는 파일·형식·시간·머리말·보간 가중치 출력을 정의한다(249–253). 오류 표지 910은 `inquire`로 데이터 파일명을 얻고 `msgerr` 심각도 4로 판독 오류를 보고한 뒤 반환한다(255–257). 표지 920은 파일 열기 오류를 같은 심각도로 보고하고 반환한다(258–259). 표지 930은 파일명을 조회하고 예상하지 못한 EOF를 같은 심각도로 보고한 뒤 반환한다(260–262). 구분 주석·루틴 종료(263–264). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 61–64·146–165: `binfo` 선언 주석은 0·1·2를 정의한다. 경계값 판독 실행 분기는 `binfo == 0`만 있다. 1·2에 대한 별도 판독 분기는 이 파일에 없다.
- 120·215–216·106: 파일 소진 시 `timf2`를 `999999999.`로 설정하고 bcloop를 반복한다. 다음 반복의 시간 조건은 `timco > timf2`이며, 이 루프 안에는 93행의 `bfiled(1) == -1` 조기 반환을 반복하는 문장이 없다.
- 183–207·196–199·213–214: 파일명 목록 EOF 경로는 `bfiled(5)`를 0으로 설정한다. 단일 파일 EOF 경로는 표지 130으로 바로 이동하므로 그 대입을 통과하지 않는다. 두 경로는 `bfiled(4)=0`, `bfiled(1)=-1`을 함께 수행한다.
- 125·140·150·154–157: 머리말 판독에는 `err=910`이 있다. 시간·값 판독문과 문자열의 내부 판독문에는 `err=` 지정이 없다.
- 235·238: 보간식은 `bndval(ibloc,1)`을 입력으로 사용하면서 같은 열을 덮어쓴다. 이후 `bctime(1)`에는 현재 시간 `timco`를 저장한다.
