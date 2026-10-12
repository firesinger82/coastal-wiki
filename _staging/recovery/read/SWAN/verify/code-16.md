# SWAN 판독 기록 전수 검증 — code-16

대조일은 2026-10-13이다.
대조 원문은 각 대상 기록의 frontmatter `file:`에 적힌 파일이다.
원문의 각 구간을 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
한 번에 연 대상 원문 구간은 최대 115행이다.

| 기록 | 구간 표 대조 행 | 후속 사실 대조 행 | 대조 대상 행 합계 | 대조한 원문 범위 | 원문 행 수 | 정정 | 보완 | 이상 없음 |
|---|---:|---:|---:|---|---:|---:|---:|---:|
| [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md) | 63 | 27 | 90 | 1–2658 | 2,658 | 11 | 39 | 43 |
| [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md) | 21 | 12 | 33 | 1–871 | 871 | 7 | 16 | 13 |
| 합계 | 84 | 39 | 123 | 두 원문 전체 | 3,529 | 18 | 55 | 56 |

행 수는 두 기록의 구간 표 본문과 후속 사실 항목에서 셌다.
원문 행 수는 실제 파일에서 셌다.
정정과 보완은 각 유형의 표시를 붙인 대상 행 수다.
두 표시를 모두 붙인 6행은 두 유형에 각각 포함했다.
이상 없음은 수정하지 않은 대상 행 수다.

구간 경계와 frontmatter는 보존했다.
두 원문의 SHA-256은 frontmatter에 기재된 값과 일치했다.
조건 인용과 바로 붙은 행 번호를 원문에 대조했다.
`!/Cray`·`!/SGI`·`!CVIS` 행의 활성 스위치는 각각 `-cray`·`-sgi`·`-cvis`로 확인했다.
스위치 판정 근거는 `models/SWAN/raw/source_code/swan/switch.pl` 29–32행과 93–96행이다.
`!$`·`!$OMP`·`!/A`·`!/Z`·`!!real`은 같은 파일 82–105행의 표시 제거 대상이 아니다.
모델은 실행하지 않았다.

| 구분 | 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|---|
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1–82 | 윤년 방법을 일반적으로만 요약. | 4의 배수·세기 해 제외와 연도 0·1000·2000 예외를 원문 주석의 주장으로 구분. | 79–81 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):133–160 | 초기값과 기준일 설정 대입을 인용하지 않음. 월 검사 사슬의 ELSE 부재를 명시하지 않음. | IYEAR·IDNOW·REFDAY·LOGREF·DTTIME 대입을 원문으로 인용. 월 검사에 ELSE가 없고 145행에서 닫힘을 명시. | 133·137–145·150–153 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):161–249 | 윤년 방법을 일반적으로만 요약. | 4의 배수·세기 해 제외와 연도 0·1000·2000 예외를 원문 주석의 주장으로 구분. | 217–219 |
| 정정 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):250–291 | 지역 변수 주석을 4세기 묶음으로 요약. | IMIL 주석의 천년 표현과 실제 IDYMIL의 4세기 정의를 구분. | 241·248·252–259 |
| 정정 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):292–329 | 328행을 세기·4세기 경계 보정으로 요약. | 100의 배수가 아니거나 400의 배수인 해의 일수 보정으로 명시. | 328 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):292–329 | ICNT와 IYR의 0 대입을 인용하지 않음. | ICNT 초기값과 ELSE의 IYR 대입을 원문으로 인용. | 302·322–324 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):607–672 | 인수의 의미와 선언만 포괄적으로 언급. IOSTAT 메시지 수준을 생략. | 입출력 인수와 파일·시간·성분별 헤더 수를 명시. IOSTAT 0/-1/-2와 오류 출력값의 의미를 명시. | 615–626·643–646 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):673–700 | BNEW와 NDSD의 설정을 인용하지 않음. | BNEW 참·거짓과 NDSD 초기값 및 파일명 저장 대입을 원문으로 인용. | 690–691·696–698 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):744–769 | 두 파일 열기 분기의 IOSTAT 초기값을 인용하지 않음. | 각 분기의 IOSTAT = 0을 해당 행 번호로 인용. | 748·760 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):851–915 | 인수와 작업 변수의 선언만 요약. | 배치·격자 점 수·파일 단위·헤더 수·곱셈 계수의 의미를 추가. 주석의 IDLAM/NHEDL 및 ARR input 표기를 구분. IOERR 메시지 수준을 추가. | 861–890 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):916–955 | IENT 초기값을 DATA 0으로만 요약. | DATA IENT /0/을 원문으로 인용. | 917 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):956–986 | IDLA의 CASE 1~6만 나열. | CASE DEFAULT가 없음을 해당 구간에 명시. | 961–986 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):987–1014 | IDLA의 CASE 1~6만 나열. | CASE DEFAULT가 없음을 해당 구간에 명시. | 989–1014 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1015–1044 | IDLA의 CASE 1~6만 나열. | CASE DEFAULT가 없음을 해당 구간에 명시. | 1017–1042 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1045–1084 | IOERR 초기값을 인용하지 않음. | 서식·비서식 파일 열기 분기의 IOERR 초기값을 각각 인용. | 1056·1060 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1085–1113 | 오류 경로의 파일명 기본값을 인용하지 않음. | 911번과 920번의 UNKNOWN_FILE 대입을 각각 원문으로 인용. | 1090·1106 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1114–1137 | 930번의 파일명 초기화 값이 빠짐. | 930번의 UNKNOWN_FILE 대입을 원문으로 인용. | 1132 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1138–1229 | 호출·초기화·ITRACE 조건과 횟수를 포괄적으로만 요약. | 주석의 첫 호출문·초기값·ITRACE=0 및 ITRACE>0 조건을 인용. | 1196–1200 |
| 정정 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1248–1314 | MSGERR가 LEVERR를 높인다고 조건 없이 요약. | 필요할 때 LEVERR를 높인다는 원문의 한정을 복원. | 1309–1311 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1358–1395 | 오류 접두어 대입과 노드 접미사 위치·형식을 요약만 함. | 각 ERRM 대입과 ERRFNM 부분 문자열 범위 및 FORMAT을 원문으로 인용. | 1360·1362·1364·1366·1368·1380–1382 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1478–1491 | IENT 초기값을 DATA 0으로만 요약. | DATA  IENT /0/을 원문으로 인용. | 1479 |
| 정정 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1578–1588 | A16과 A4를 모두 프로젝트 폭으로 묶음. | PROJID의 A16과 실행 식별자 PROJNR의 A4를 구분. | 1548·1580–1586 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1589–1679 | SF 코드를 문자 목록으로만 제시. IUNIT 출력과 DDNAME의 조건부 주석을 생략. | SF의 상태·서식 의미와 IUNIT 출력 및 IUNIT>0일 때의 DDNAME 주석을 추가. | 1665–1671 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1680–1747 | 오류 코드 주석을 포괄적으로만 요약. | 코드별 의미와 IUNIT 조건을 명시. 주석의 IENSIO가 선언 목록에 없음을 구분. | 1684–1700 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1748–1789 | 구조 주석의 파일명·열림 상태 분기를 묶어서 요약. | 주석의 IUNIT·DDNAME·파일 열림·파일명 일치 조건과 분기별 동작을 복원. | 1751–1770 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1790–1819 | 오류 코드 대입과 SF 부분 문자열 복사를 인용하지 않음. | 각 오류 코드 대입과 SF(1:1)/SF(2:2)를 원문으로 인용. | 1793·1797–1798·1803·1809 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1820–1848 | 오류 상태와 기존 단위 대입을 인용하지 않음. | IENODD·IOSTTM·IEEXST·IEOPEN 및 IUNIT 대입을 각 오류 분기에 인용. | 1823·1832·1839·1845–1847 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1849–1873 | IFUN 초기 단위와 단위·오류 코드 대입을 인용하지 않음. | FUNLO에서 시작하는 대입과 IUNIT·IENUNF 대입을 원문으로 인용. | 1852·1863·1866 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1874–1907 | 오류 코드 대입을 인용하지 않음. 다시 여는 OPEN의 ERR=999를 생략. | IOSTAT 대입을 인용. 다시 여는 OPEN의 999번 오류 이동을 명시. | 1880·1894·1897–1901·1905 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1908–1938 | 두 OPEN의 오류 이동과 IUNIT=-1 대입을 인용하지 않음. | 각 OPEN의 ERR=999와 IOSTAT 지정 및 HIOPEN·오류 반환 대입을 인용. | 1909·1915·1922·1934–1936 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):1939–2004 | 방법 주석의 비교식과 EPS 식을 개괄적으로만 요약. | 주석의 TINY 비교와 EPS 수식을 인용. EPS 비교가 이하임을 명시. | 2002–2003 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):2049–2063 | IENT 초기값과 EQREAL 참 대입을 인용하지 않음. | IENT 초기값과 ELSE의 EQREAL 대입을 원문으로 인용. | 2050·2059 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):2141–2149 | IENT 초기값을 DATA 0으로만 요약. | DATA IENT/0/을 원문으로 인용. | 2142 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):2263–2279 | DATITM 공백 초기화를 요약만 함. | DATITM(IITM) = '    '을 원문으로 인용. | 2271–2273 |
| 정정 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):2280–2308 | 항목 수 초과 오류 출력과 DATITM 공백 대입을 한 조건의 동작처럼 연결. | 2303행에서 항목 수 검사가 닫힘을 명시. 2304행은 RITM=0 분기에서 검사 결과와 무관하게 실행함을 구분. | 2297–2304 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):2280–2308 | IITM·LCHSTR·RITM과 DATITM의 상수 대입을 인용하지 않음. | 초기값·따옴표 종료 상태·빈 항목 및 쉼표 처리 상태 대입을 인용. | 2280·2287–2288·2304·2307 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):2309–2334 | 공백·따옴표·일반 문자 처리의 상태 대입을 인용하지 않음. | RITM·LCHSTR·ICR1 대입을 원문으로 인용. | 2316·2327·2329–2330 |
| 정정 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):2439–2527 | OPMLFC를 문자 코드 상한으로만 요약. | OPMLFC는 허용 문자 코드 최대값에 1을 더한 값임을 명시. | 2521–2526 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):2439–2527 | 복사 방향을 양방향이라는 목적 설명으로만 요약. | 주석의 MOVE=TO_와 MOVE=FROM_ 조건 및 복사 방향을 명시. | 2514–2515 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):2586–2608 | NSL·MCHAR·CC·IERR의 상수 대입과 주석 처리된 시험 출력 조건을 인용하지 않음. | 각 상수 대입과 비활성 ITEST.GE.250 조건을 원문으로 인용. | 2587·2589·2595·2599·2605 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):2609–2619 | 오류 코드 801의 대입을 인용하지 않음. | IERR = 801을 원문으로 인용. | 2612 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):2620–2644 | STRING·NSL 초기값과 오류 코드 802 대입을 인용하지 않음. | 각 초기값과 IERR = 802를 원문으로 인용. | 2625–2626·2641 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):2645–2658 | 비활성 시험 출력 조건을 주석이라고만 요약. | ITEST.GE.250 조건과 출력 항목을 주석으로 인용. | 2646 |
| 정정 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):후속 사실 6 (953·1118) | 진입한 모든 배열을 나누고 끝에서 다시 곱한다고 요약. | 나눗셈 구간에 도달한 경우와 900번 재곱셈 경로를 구분. | 920·951–955·1116–1120·1132–1135 |
| 정정 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):후속 사실 8 (924·1051–1053) | NUMFIL을 진입 시 무조건 초기화한다고 요약. | NDSD<0 반환을 통과한 뒤 초기화함을 명시. | 920·924·1049–1054 |
| 정정 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):후속 사실 9 (1050·1090–1098) | EOF 경로를 닫기 뒤 911번 조회로 일괄 서술. | 911번에 도달하는 NUMFIL>=2 또는 NDSL<=0 조건을 명시. | 1049–1054·1083–1098 |
| 정정 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):후속 사실 11 (1199–1200·1230–1239) | 반환 조건을 IENT>ITRACE만으로 서술. 동등하면 항상 출력한다고 서술. | ITRACE=0 반환을 분리. 동등 시 출력 설명을 ITRACE>0에 한정. | 1199–1200·1230–1243 |
| 정정 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):후속 사실 13 (1451–1452·1482–1488) | LEVERR>=4를 실제 종료 조건으로 서술. MAXERR=-1 검사의 효과를 생략. | 반환값의 참 설정과 MAXERR·OpenMP에 의한 거짓 덮어쓰기를 구분. | 1482–1488 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):후속 사실 15 (1851–1869) | 저장 IFUN을 증가시키는 경로만 설명. | IFUN=0이면 FUNLO를 대입하는 첫 선택 경로를 추가. | 1851–1855 |
| 보완 | [ocpmix.ftn.md](../swan/src/ocpmix.ftn.md):후속 사실 17 (2002–2003·2054–2059) | EPS를 EPSILON과 차이의 곱으로만 설명. | EPS가 0일 때 TINY(REAL1)로 바꾸는 보정을 추가. | 2054–2057 |
| 보완 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):17–43 | p1/p2 초기값·이전 값 이동과 대칭 가중치 대입을 요약만 함. | 초기값·p3/p2 갱신 순서·z1 저장 및 w(n+1-i) 대입을 인용. | 23–27·31·38 |
| 보완 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):44–102 | 입력·출력 단위와 이력 주석의 조건·결과값 인용을 생략. | 원문 단위 표기와 이력의 음수 조건 및 cg=-10을 인용. | 78–79·93–96 |
| 보완 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):118–213 | 오류 번호만 나열. 영역 밖 예시의 수치를 생략. | 오류 코드별 원문 의미를 추가. 20의 x1 표기를 보존. 상수 입력·출력 예시를 인용. | 187–196·200–211 |
| 보완 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):214–251 | 정상·오류 상태와 단일 입력점의 출력 대입을 인용하지 않음. | ierr 0/2/3과 y2 = y1(1)을 원문으로 인용. | 226·231·243·248 |
| 보완 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):252–288 | 단조성 위반 오류 코드 1/2의 대입을 인용하지 않음. | 증가·감소 검사 분기의 오류 코드 대입을 원문으로 인용. | 257·274 |
| 보완 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):289–324 | 검색 초기값과 복사 대입을 요약만 함. 특수점·끝점 주석의 식을 생략. | 검색 상태 대입과 닫힘 행을 추가. 304·314행 주석의 조건·인덱스 표현을 원문대로 인용. | 293–307·312·314–316 |
| 보완 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):390–432 | 퇴화 다각형과 누적값의 초기화를 인용하지 않음. 꼭짓점 인덱스를 묶어서 요약. | 각 0 대입과 조건 닫힘 행을 추가. ipol/ipol1 좌표 대입과 무게중심 주석을 명시. | 390–396·410·413–415·420–423 |
| 보완 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):433–480 | 이력 주석의 nx>0 조건을 인용하지 않음. | 원문의 nx > 0을 백틱으로 인용. | 467 |
| 보완 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):481–501 | dx 초기값을 인용하지 않음. 내부 루프 종료 행을 생략. | dx = 0을 인용. 내부 루프는 489행에서 닫힘을 명시. | 485·489 |
| 정정 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):502–616 | 578–579행을 양 끝 함수 부호 가정으로 설명. | 영점의 양쪽에 있는 x1/x2 좌표 가정으로 정정. | 578–579 |
| 보완 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):502–616 | xacc 주석의 부등식과 오류 1의 단정 및 IPRINT별 출력 조건을 생략. | 정확도 부등식과 오류 주석을 인용. IPRINT=0/>0 및 연결 파일 부재 조건을 추가. | 561·572·581–584 |
| 정정 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):617–646 | unused를 미사용 표지라고 해석. | 원문의 set start value와 일치하는 시작 기본값으로 명시. | 618 |
| 보완 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):617–646 | ierr·luprint 초기값과 주석 처리된 출력 조건 및 경계 주석 조건을 인용하지 않음. | 초기값과 633행 경계 조건 및 644–645행 비활성 출력을 인용. | 617·628·633·644–645 |
| 보완 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):647–669 | 경계·시작값 대입과 비활성 시험 출력 조건을 요약만 함. | 경계 및 시작값 대입과 주석 처리된 luprint 조건을 인용. 수렴 검사 닫힘 행을 추가. | 648–650·659–665·667 |
| 보완 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):670–695 | 부호별 경계 갱신에서 원본 값을 생략. 오류 코드 대입을 인용하지 않음. | 각 분기의 xl/fl/xh/fh 대입과 ierr 1/2를 원문으로 인용. | 672–681·683·693 |
| 보완 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):696–716 | 끝점 근·오류 코드·반환값 대입을 인용하지 않음. 이전 반복 종료 행을 생략. | 각 대입과 이전 iter 루프의 692행 종료를 명시. | 692·697·699·701·708 |
| 보완 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):786–853 | 검사 이력의 조건 인용과 입력 단위를 생략. | 음수·y>15 조건과 w/d/grav의 원문 단위 표기를 추가. | 821–822·836–838 |
| 정정 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):854–871 | 분모에 y의 식을 포함하는 파데 근사식을 다항식이라고 서술. | 파데 근사식으로 정정. | 862–863 |
| 보완 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):854–871 | y>15 분기의 x=y 대입을 인용하지 않음. | x = y를 원문으로 인용. | 859–860 |
| 정정 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):후속 사실 3 (187–196·254–284) | 오류 설정 직후 이동한다고 서술. | 오류 설정과 이동 사이의 좌표 출력을 복원. | 257–259·265–267·274–276·282–284 |
| 정정 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):후속 사실 4 (254–287·296–316) | 검색 조건이 s1<=s2 하나라고 서술. | i1<n1까지 포함한 DO WHILE 조건을 인용. | 298 |
| 정정 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):후속 사실 5 (166–167·203–205·309–316) | 마지막 점보다 앞선 출력점은 모두 보간식을 적용한다고 서술. | 끝값 보정 조건을 그대로 제시. 앞선 점에는 복사 분기와 보간 분기가 모두 있음을 구분. | 306–316 |
| 정정 | [serv_xnl4v5.ftn90.md](../swan/src/serv_xnl4v5.ftn90.md):후속 사실 10 (662–668) | 차이가 xacc 이하라고 서술. | 차이의 절댓값과 xacc를 비교한다고 정정. | 662–667 |

정정 18, 보완 55, 이상 없음 56
