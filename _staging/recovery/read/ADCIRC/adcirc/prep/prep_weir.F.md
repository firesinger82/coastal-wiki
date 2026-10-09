---
file: models/ADCIRC/raw/source_code/adcirc/prep/prep_weir.F
lines: 188
sha256: 49215267e0dff2d53ccc6629e303adcb1297ae8445a3decdeb9da1d73f7119fb
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# prep_weir.F — 판독 구간 기록

구간은 1행부터 188행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | ADCIRC 명칭·1994–2025 저작권·LGPL 3 이상·무보증 머리말(1–19). 모듈 설명 주석은 작성자 Zachary Cobell과 날짜 2012/03/12를 적는다(20–23). 주석은 시간가변 보(time varying weir)와 육지 경계조건(land boundary condition)의 지정 루틴이며 유형 3,13,23,4,24,5,25의 값을 설정한다고 적는다(24–26). 구분 주석과 빈 주석도 포함한다(27–30). |
| 31–74 | `MODULE PREP_WEIR` 시작(31). PRE_GLOBAL의 경계·좌표·프로세스·노드 변수, KDTREE2_MODULE, mod_logging의 SCREENUNIT을 가져온다(32–35). implicit none과 할당 가능 배열 BAR_LOCATIONS·LNBV·LIBCONN·LBCODEI·NODES_TVW·NWEIRBNDRY, 정수 NTIMEVARYINGWEIR, 두 탐색 트리 포인터, 길이 400의 TIMEVARYINGWEIRMSSG를 선언한다(37–48). contains 뒤 `ALLOCATE_WEIRBOUNDARY()`가 시작하며 지역 정수와 XY 배열을 선언한다(50–61). XY는 `(1:2,1:NNODG)`, NWEIRBNDRY는 NPROC 크기로 할당하고 NWEIRBNDRY 전체를 0으로 초기화한다(63–65). XY의 첫째·둘째 행에 X·Y 전체를 복사한다(67–68). 최근접 탐색 트리(k-d tree) 생성 호출은 `GLOBAL_SEARCHTREE => KDTREE2_CREATE(XY,REARRANGE=.TRUE.,` (70), `&               SORT=.TRUE.)` (71)이다. 루틴 종료와 빈 줄을 포함한다(73–74). |
| 75–105 | 시작 시 31행 PREP_WEIR 모듈 안. `FIND_BOUNDARY_NODES(LAT,LON,IDX)`는 실수 입력 LAT·LON과 정수 출력 IDX를 받는다(75–81). `INTEGER,PARAMETER    :: SEARCHDEPTH = 1` (82)과 그 크기의 KDRESULTS를 선언한다(83). 허용 비교값은 `EPS = EPSILON(1.0D0)` (85)이다. 지역 X=LAT·Y=LON을 복사한 뒤 `CALL KDTREE2_N_NEAREST(TP=GLOBAL_SEARCHTREE,` (90), `&                 QV=(/X,Y/),NN=SEARCHDEPTH,RESULTS=KDRESULTS)` (91)로 한 결과를 찾는다. 조건은 `IF(KDRESULTS(1)%DIS.GT.EPS)THEN` (93)이다. 참이면 좌표를 담은 오류 메시지를 출력하고 `CALL EXIT(1)` (97)을 호출한다(94–98). 조건 밖에서 첫 결과의 IDX를 출력 인수에 복사하고 return한다(100–102). 루틴 종료와 빈 줄을 포함한다(104–105). |
| 106–142 | 시작 시 31행 PREP_WEIR 모듈 안. `PARSE_TIME_VARYING_WEIR_INFO()`는 GLOBAL의 USE_TVW·TVW_FILE을 가져온다(106–108). 길이 2000의 InputString·modifiedString, 길이 200의 ScheduleFile, 좌표·수위·시작/종료 시간·ZF·VARYTYPE·상태 변수를 선언한다(109–120). 이름목록(namelist) `/TimeVaryingWeir/`는 X1,Y1,X2,Y2,VaryType,ZF,ETA_MAX와 시작·종료의 일·시·초를 포함한다(122–126). `CALL ALLOCATE_WEIRBOUNDARY()` (128) 뒤 TVW_FILE의 존재 여부를 확인한다(130). `IF(.NOT.exists)THEN` (131)이면 안내 출력, USE_TVW=false, `TVW_FILE= 'none'` (135) 설정 후 return한다(132–137). 조건 밖에서 TVW_FILE을 읽기 전용 UNIT=98로 열고 NTIMEVARYINGWEIR을 읽는다(138–139). 같은 크기의 메시지·노드 배열을 할당하며 `NODES_TVW(:) = -1` (142)로 초기화한다(140–142). |
| 143–155 | 시작 시 31행 PREP_WEIR 모듈·106행 PARSE_TIME_VARYING_WEIR_INFO 루틴 안. UNIT=99의 `namelist.scratch`를 쓰기 모드로 연다(143–144). `DO I = 1,NTIMEVARYINGWEIR` (145)에서 UNIT=98의 한 줄을 InputString에 읽고, ADJUSTL 결과를 TIMEVARYINGWEIRMSSG(I)에 저장한다(146–147). 이름목록 문자열 생성문은 `WRITE(modifiedString,'(A)') "&TimeVaryingWeir "//` (148), `&                  TRIM(ADJUSTL(InputString))//" /"` (149)이다. 이 문자열을 UNIT=99에 쓰고 루프 종료 뒤 닫는다(150–152). 같은 파일을 읽기 모드로 다시 여는 문장은 `OPEN(UNIT=99,FILE="namelist.scratch",ACTION="READ",` (154), `&               IOSTAT=IOS,ERR=200)` (155)이다. |
| 156–171 | 시작 시 31행 PREP_WEIR 모듈·106행 PARSE_TIME_VARYING_WEIR_INFO 루틴 안. `DO I = 1,NTIMEVARYINGWEIR` (156)에서 매번 `X1 = -99999D0` (157), `Y1 = -99999D0` (158)을 설정한다. `READ(99,NML=TimeVaryingWeir,IOSTAT=IOS)` (159) 뒤 `CALL FIND_BOUNDARY_NODES(X1,Y1,IDX)` (160)을 호출하고 IDX를 NODES_TVW(I)에 복사한다(161). 루프 종료 뒤 `CLOSE(99,STATUS="DELETE")` (163)로 임시 파일을 삭제하고 return한다(162–164). 레이블 200은 SCREENUNIT에 오류를 출력하고 `CALL EXIT(1)` (167)을 호출한다(165–167). 빈 줄·루틴 종료·빈 줄을 포함한다(168–171). |
| 172–188 | 시작 시 31행 PREP_WEIR 모듈 안. 논리 함수 `ISNULL(CHECKNUMBER)`는 REAL(8) 입력을 받는다(172–175). `EPS = EPSILON(1.0D0)` (176)이며 반환값을 false로 초기화한다(177). 조건 `IF(ABS(CHECKNUMBER+99999D0).LE.EPS)THEN` (178)이면 true로 설정한다(179–180). 함수 종료·빈 줄·모듈 종료와 마지막 공백 행들을 포함한다(181–188). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32–48·56–61·109–119: PRE_GLOBAL에서 가져온 NVELL·IBCONNR·LBCODE·NBOU·MNVEL·NBVV·NVEL은 이 파일의 실행문에 등장하지 않는다. BAR_LOCATIONS·LNBV·LIBCONN·LBCODEI·BARRIER_SEARCHTREE는 선언 뒤 사용되지 않는다. ALLOCATE_WEIRBOUNDARY의 지역 정수 I·JG·K·NWEIR·IDX·IDX2·IDX3과 PARSE_TIME_VARYING_WEIR_INFO의 ScheduleFile은 선언 뒤 사용되지 않는다.
- 63–71·128–137: 배열 할당과 GLOBAL_SEARCHTREE 생성은 TVW_FILE 존재 검사보다 먼저 실행된다. 파일이 없는 분기는 이 할당을 해제하는 문장 없이 return한다. 이 파일에는 탐색 트리 파괴 호출이 없다.
- 77–91: FIND_BOUNDARY_NODES는 인수 LAT를 지역 X에, LON을 지역 Y에 그대로 복사한다. 이 루틴에는 좌표 변환식이 없다.
- 82–98: 최근접 결과 수는 1로 고정한다. `%DIS`와 비교하는 값은 `EPSILON(1.0D0)`이며 별도의 거리 허용값을 읽는 문장은 없다. `%DIS`의 정의는 이 파일에 없다.
- 48·109·146–147: 메시지 배열 요소의 문자 길이는 400이다. InputString의 문자 길이는 2000이다. 저장문은 `TIMEVARYINGWEIRMSSG(I) = ADJUSTL(InputString)`이다.
- 122–126·156–159: 이름목록은 좌표·형태·수위·시간 변수를 포함한다. 이름목록 판독 루프에서 판독 전에 기본값을 대입하는 변수는 X1과 Y1뿐이다. 두 기본값은 -99999D0이다.
- 139·146·154–167: UNIT=98의 수·문자열 판독에는 IOSTAT가 없다. UNIT=99의 이름목록 판독은 IOS를 받지만 판독 뒤 IOS 조건 검사가 없다. 오류 레이블 200은 UNIT=99의 OPEN 문에 있는 ERR=200으로 연결된다.
- 138–163: 입력 파일의 장치 번호는 98이며 임시 파일의 장치 번호는 99이다. 임시 파일명은 `namelist.scratch`로 고정한다. UNIT=99는 삭제하며 닫지만 이 루틴에는 UNIT=98을 닫는 문장이 없다.
- 172–181: ISNULL은 -99999D0과의 차이를 기계 엡실론(machine epsilon)으로 검사한다. 이 파일에는 ISNULL 호출이 없다.
