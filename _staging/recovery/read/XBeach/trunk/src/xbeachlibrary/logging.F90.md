---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/logging.F90
lines: 389
sha256: bce674aa627966352d8e32b68e4503cd85fc0aa701ad40dc76f4aa8055974271
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# logging.F90 — 판독 구간 기록

구간은 1행부터 389행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–52 | `logging_module`: 파일 unit 세 개는 save 선언(11–13). C logger와 distributelog 추상 인터페이스(16–33), 두 procedure 포인터의 초기값 null(36–37). 로그 수준 ALL=0, DEBUG=1, INFO=2, WARN=3, ERROR=4, FATAL=5, OFF=6(41–47). `writeloginterface.inc` 포함(50). 원문 조건·식(행 순서): `integer, parameter, public :: LEVEL_ALL = 0` (41); `integer, parameter, public :: LEVEL_DEBUG = 1` (42); `integer, parameter, public :: LEVEL_INFO  = 2` (43); `integer, parameter, public :: LEVEL_WARN  = 3` (44); `integer, parameter, public :: LEVEL_ERROR = 4` (45); `integer, parameter, public :: LEVEL_FATAL = 5` (46); `integer, parameter, public :: LEVEL_OFF = 6` (47). |
| 53–75 | `set_logger`: C 함수 포인터를 `c_f_procpointer`로 logging_callback에 연결(60). `logmsg`는 callback이 associated일 때만 `string_to_char_array(msg)` (71)와 callback(level,c_string)(72)을 실행. 원문 조건·식(행 순서): `if (associated(logging_callback)) then` (70); `c_string = string_to_char_array(msg)` (71); `end if` (73). |
| 76–103 | `start_logfiles`: 바깥 xmaster 안에서 generate_logfileid 세 번 호출(84·87·90), 각 open도 xmaster 조건(85·88·91); XBlog.txt·XBerror.txt·XBwarning.txt를 replace로 연다. 같은 바깥 블록에서 음수 unit이면 error=1(93). xmaster 블록 밖에서 error==1일 때 화면 출력 후 stop(97–100). 원문 조건·식(행 순서): `if (xmaster) then` (82); `logfileid       = generate_logfileid()` (84); `if (xmaster)    open(logfileid,     file='XBlog.txt',       status='replace')` (85); `errorfileid     = generate_logfileid()` (87); `if (xmaster)    open(errorfileid,   file='XBerror.txt',     status='replace')` (88); `warningfileid   = generate_logfileid()` (90); `if (xmaster)    open(warningfileid, file='XBwarning.txt',   status='replace')` (91); `if (logfileid < 0 .or. errorfileid < 0 .or. warningfileid < 0) error = 1` (93); `endif ! xmaster` (95); `if (error==1) then` (97); `endif` (100). |
| 104–125 | `close_logfiles`: xmaster일 때만 세 unit 종료; error 파일만 `STATUS='DELETE'` (108). `get_logfileid`는 조건 없이 세 저장 unit을 출력 인수로 복사(120–122). 원문 조건·식(행 순서): `if (xmaster) then` (106); `endif` (110); `lid = logfileid` (120); `eid = errorfileid` (121); `wid = warningfileid` (122). |
| 126–150 | `generate_logfileid`: tryunit=98, fileopen=true, error=0(133–135). fileopen 동안 inquire(138); 열려 있을 때만 `tryunit=tryunit-1` (140). 그 조건 밖이지만 while 안에서 tryunit<=10이면 -1·false 설정 후 return(142–145). 원문 조건·식(행 순서): `tryunit  = 98` (133); `fileopen = .true.` (134); `error    = 0` (135); `do while (fileopen)` (137); `if (fileopen) then` (139); `tryunit=tryunit-1` (140); `endif` (141); `if (tryunit<=10) then` (142); `tryunit     = -1` (143); `fileopen    = .false.` (144); `endif` (146). |
| 151–186 | `progress_indicator`: initialize이면 lastper=0, system_clock 호출, lastt 설정(166–169). else에서는 system_clock·tnow 계산(171–172); 진행률 간격 또는 시간 간격 조건(173)을 만족할 때 writelog(174). 그 안에서 진행률 간격을 넘겼을 때 lastper를 mod로 맞추고, 아니면 curper로 설정(175–179). 같은 출력 조건 안이지만 안쪽 if 밖에서 lastt=tnow(180). 원문 조건·식(행 순서): `if (initialize) then` (166); `lastper = 0.d0` (167); `lastt = dble(count)/count_rate` (169); `else` (170); `tnow = dble(count)/count_rate` (172); `if (curper>=lastper+dper .or. tnow>=lastt+dt) then` (173); `if (curper>=lastper+dper) then` (175); `lastper = curper-mod(curper,dper)` (176); `else` (177); `lastper = curper` (178); `endif` (179); `lastt = tnow` (180); `endif` (181); `endif` (182). |
| 187–199 | `report_file_read_error`: 파일명과 숫자 형식·줄바꿈·탭 확인 안내를 writelog로 출력(194–196)한 뒤 `halt_program` (197). |
| 200–247 | `writelog_startup`: version.def/dat 포함(211·220); HAVE_CONFIG_H에서 config.h·cwd 선언·getcwd(214–218). date_and_time은 xmaster 조건 밖(222). xmaster 안에서 버전 1.24., revision·빌드 일시·URL·시작 날짜/시각·zone 출력(224–243); cwd와 MPI 프로세스 수 출력은 추가 전처리 조건(236–242). 원문 조건·식(행 순서): `if (xmaster) then` (224); `endif` (243). |
| 248–287 | USEMPI에서만 `writelog_mpi`. 바깥 xmaster 안의 error 분기: 1=분할 방식, 2=도메인 수 불일치, 3/4=M/N nx/4·ny/4 제한으로 로그 후 `halt_program` (258–273); 5/6=M/N nx/8·ny/8 효율 경고만(274–279); else는 processor grid 로그(280–281). 원문 조건·식(행 순서): `if (xmaster) then` (257); `if (error==1) then` (258); `elseif (error==2) then` (261); `elseif (error==3) then` (264); `elseif (error==4) then` (269); `elseif (error==5) then` (274); `elseif (error==6) then` (277); `else` (280); `endif` (282); `endif` (283). |
| 288–331 | `writelog_finalize`: xmaster 안에서 cpu_time(tend) 호출(304), duration·dt·셀/단계당 performance 계산(306–308) 및 출력. USEMPI이면서 optional t0와 t01이 모두 present일 때, 이 xmaster 안에서 MPI_Wtime 및 total/loop 시간 로그(316–321). xmaster 끝(325) 밖에서 `close_logfiles` (327), logging_callback null(329). 원문 조건·식(행 순서): `if (xmaster) then` (302); `duration    = tend-tbegin` (306); `dt          = t/n` (307); `performance = duration/(nx+1)/(ny+1)/n` (308); `if (present(t0) .and. present(t01)) then` (316); `t1 = MPI_Wtime()` (317); `endif` (321); `endif` (325). |
| 332–374 | `writelog_distribute`: has_logger 판정은 xmaster 밖(342). xmaster 안에서 level=0 뒤 destination의 s/l/w/e를 순차 독립 검사(346·349·357·362), 수준 1/2/3/4로 갱신. l일 때 callback이 없을 때만 unit 6 출력(351–354), 그 안쪽 if 밖에서 logfile 출력(355). w/e는 각각 unit 0와 경고/오류 파일 출력. xmaster 안이지만 모든 destination if 밖에서 `logmsg(level, trim(display))` (367). `writelog.inc` 포함(372). 원문 조건·식(행 순서): `has_logger = associated(logging_callback)` (342); `if (xmaster) then` (344); `level = 0` (345); `if (scan(destination,'s')>0) then` (346); `level = 1` (347); `end if` (348); `if (scan(destination,'l')>0) then` (349); `level = 2` (350); `if (.not. has_logger) then` (351); `end if` (354); `end if` (356); `if (scan(destination,'w')>0) then` (357); `level = 3` (358); `end if` (361); `if (scan(destination,'e')>0) then` (362); `level = 4` (363); `end if` (366); `endif` (368). |
| 375–389 | `assignlogdelegate_internal`: distributelog를 먼저 null로 되돌림(381); C 포인터가 associated일 때만 `c_f_procpointer`로 연결(382–384). 사용되지 않는 지역 i 선언(379). 모듈 끝·마지막 빈 행 포함. 원문 조건·식(행 순서): `if (c_associated(fPtr)) then` (382); `endif` (384). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 85·88·91·93: 로그 파일 open은 unit 음수 검사보다 앞에 있고 IOSTAT 지정은 없다.
- 108: close_logfiles는 XBerror 파일을 DELETE 상태로 닫는다.
- 130·135: generate_logfileid의 지역 error는 0으로 설정되지만 이후 참조하지 않는다.
- 228: 시작 로그의 버전 접두사는 `version 1.24.`로 고정되어 있다.
- 277–279: error==6은 N 방향 ny/8 경고 다음에 M 방향 도메인을 줄이라는 문구를 출력한다.
- 307–308: n으로 나누는 식 앞에 n==0 검사는 이 루틴에 없다.
- 346–367: destination에 s만 있으면 level=1을 설정하지만 그 분기에는 직접 화면 write가 없고 뒤에서 logmsg를 호출한다.
- 379: assignlogdelegate_internal의 지역 i는 선언 뒤 사용하지 않는다.
