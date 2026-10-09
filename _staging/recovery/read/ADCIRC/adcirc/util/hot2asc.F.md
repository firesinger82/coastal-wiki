---
file: models/ADCIRC/raw/source_code/adcirc/util/hot2asc.F
lines: 379
sha256: 84455a76e402362a2b2bf06add46b94158c822b370e7aba7ce4e936b909ba193
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# hot2asc.F — 판독 구간 기록

구간은 1행부터 379행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | ADCIRC 명칭, 1994–2025 저작권, LGPL 3 이상 재배포·수정 조건과 무보증 설명 및 구분 주석이다. |
| 20–66 | hot2asc 프로그램과 implicit none(20–21). 전역·지역 노드(node)·요소(element) 수, hotstart 모델·시각·버전, 조화 분석(harmonic analysis) 성분·관측점 수·출력 플래그를 선언한다(22–35). `integer,parameter :: IN = 10, OUT=11, NVARS=18, NHSVARS=12` (37). 입력 이름 binfname는 길이 7, 출력 이름 ascfname는 길이 11이다(40–41). get3D·getHarmonic·getReSynth와 real(8) 시각·작업값을 선언한다(43–50). vars는 출력 단계·누적 수 변수 이름 18개이고 hsvars는 NZ·NF·MM·NP·NSTAE·NSTAV·NHASE·NHASV·NHAGE·NHAGV·ICALL·NFREQ의 이름 12개이다(52–65). 빈 줄(66). |
| 67–104 | 시작 시 20행 hot2asc 프로그램 안. v48.xx 안내와 i=1 초기화(67–69). `if (COMMAND_ARGUMENT_COUNT() < i) then` (70)은 사용법 출력 후 stop이고 `else` (73)는 GET_COMMAND_ARGUMENT로 파일명을 받는다(74). binfname에 이름을 복사하고 ascfname에 '.asc'를 붙인다(77–78). inquire 뒤 `if (.not.fileFound) then` (84)은 오류 출력 후 stop이고 `else` (88)는 파일 발견 안내이다. 입력은 ACCESS='DIRECT'·RECL=8(92), 출력은 FORM='FORMATTED'·ACCESS='SEQUENTIAL'(98–99)로 연다. 각각 `if ( errorIO.gt.0) then` (93·100) 안에서 오류와 'Stopping.'을 출력한다. |
| 105–150 | 시작 시 20행 hot2asc 프로그램 안. hotstart 파일이 자기 기술형(self describing)이 아니므로 사용자가 추가 데이터 존재 여부를 지정한다는 주석(105–107). get3D/getHarmonic/getReSynth를 false로 초기화한다(108–110). i를 증가시키고 `do j = i, COMMAND_ARGUMENT_COUNT()` (113)에서 인수를 읽는다. `select case (arg)` (115)의 `case("harmonic","Harmonic","HARMONIC")` (116)은 getHarmonic=true, `case("resynth","ReSynth","RESYNTH")` (120)는 getReSynth=true, `case default` (124)는 미인식 안내이다. irec=1로 시작하여 fileVersion과 imhs를 읽는다(130–136). 버전 출력의 계산 원문은 `$  ishft(fileVersion,-20), iand(1023,ishft(fileVersion,-10)),` (133), `$  iand(1023,fileVersion)` (134)이다. `select case (imhs)` (139)의 `case(1,2,11,21,31)` (140)은 get3D=true와 3차원 미지원 안내이다. 그 안의 `if (getHarmonic) then` (143)은 getHarmonic=false로 바꾼다. `case default` (148)는 3차원 데이터가 없다는 안내이다. |
| 151–189 | 시작 시 20행 hot2asc 프로그램 안. time·iths·np_g·ne_g·np_a·ne_a를 순서대로 읽고 출력하며 레코드(record) 번호를 증가시킨다(152–168). np=np_g·ne=ne_g(170–171). dsply로 ETA1·ETA2·EtaDisc·UU2·VV2의 np개 값을 출력한다(173–177). `if (imhs ==  10) call dsply(in,out,irec,"CH1",np)` (179)은 농도 배열 추가 출력이다. idsply로 NODECODE(np)·NOFF(ne)를 출력한다(181–182). `do i = 1, NVARS` (184)에서 정수 kk를 읽고 vars(i) 이름과 함께 출력한다(185–187). 루프 종료와 빈 줄(188–189). |
| 190–238 | 시작 시 20행 hot2asc 프로그램 안. `if (getHarmonic) then` (191)이면 rec=irec+1에서 icha를 읽고 irec를 증가시킨다(192–193). `do i = 1, NHSVARS` (194)에서 rec=irec+i의 정수를 출력한다. `select case(hsvars(i))` (198)의 `case("NF")` (199), `case("NFREQ")` (200), `case("MM")` (201), `case("NSTAE")` (202), `case("NSTAV")` (203), `case("NP")` (204), `case("NHAGE")` (205), `case("NHAGV")` (206), `case("NHASE")` (207), `case("NHASV")` (208)은 후속 판독용 변수에 kk를 복사한다. `case default` (209)는 작업이 없다. `irec = irec + NHSVARS` (213). `do i=1,nfreq+nf` (214)에서 길이 8 이름 두 개와 hafreq·haff·haface 값을 읽고 출력한다(215–226). timeud와 itud를 읽고 출력한다(229–232). itud가 4바이트라는 레코드 설명 주석(233–237) 뒤 `irec = irec + 3` (238)을 실행한다. |
| 239–273 | 시작 시 20행 hot2asc 프로그램·191행 getHarmonic 참 분기 안. `do i=1,mm` (240), `do j=1,mm` (241)에서 ha 행렬을 읽고 출력한다(242–244). `if ( nhase.eq.1 ) then` (248)의 `do n=1,nstae` (249), `do i=1,mm` (250)은 수위 관측점 staelv를 출력한다. `if ( nhasv.eq.1) then` (259)의 `do n=1,nstav` (260), `do i=1,mm` (261)은 속도 관측점 staulv/stavlv를 출력한다. 각 read 뒤 irec를 증가시킨다. 루프·관측점 분기 종료와 빈 줄(270–273). |
| 274–301 | 시작 시 20행 hot2asc 프로그램·191행 getHarmonic 참 분기 안. `if ( nhage.eq.1 ) then` (274)의 `do n=1,npha` (275), `do i=1,mm` (276)에서 전역 수위 gloelv를 출력한다. `if ( nhagv.eq.1) then` (285)의 `do n=1,npha` (286), `do i=1,mm` (287)에서 전역 속도 gloulv/glovlv를 출력한다. 각 read 뒤 irec를 증가시킨다. 루프·전역 분기와 getHarmonic 분기 종료(296–300), 빈 줄(301). |
| 302–339 | 시작 시 20행 hot2asc 프로그램 안. `if (getReSynth) then` (302)이면 정수 kk를 읽어 "NE_A =" 이름으로 출력한다(303–304). `if (nhage.eq.1) then` (305)의 `do i = 1, npha` (306)은 ELAV/ELVA를 읽고 출력한다. `if ( nhagv.eq.1 ) then` (315)의 `do i = 1, np` (316)은 XVELAV·YVELAV·XVELVA·YVELVA를 읽고 출력한다. 레코드 번호를 읽을 때마다 증가시킨다. 분기 종료(330–331). 최종 irec 안내, 입력·출력 close, stop, 프로그램 종료와 빈 줄(333–339). |
| 340–360 | dsply(in,out,irec,varname,size) 입구와 integer 인수·real(8) 작업값 x·문자열 선언(340–345). 변수 머리말 출력(347). `do i = 1, size` (349)에서 real(8) 값을 읽고 irec를 증가시키며 변수명·인덱스·값을 출력한다(351–352). 350행의 선행 증가는 주석이다. return, 머리말 형식과 a10·i8·1pe20.10 값 형식, 루틴 종료·빈 줄(355–360). |
| 361–379 | idsply 입구·integer 작업값 x 및 인수 선언(361–365). 변수 머리말 출력(367). `do i = 1, size` (369)에서 정수를 읽고 irec를 증가시키며 변수명·인덱스·값을 출력한다(371–372). 370행의 선행 증가는 주석이다. return, 머리말 형식과 a10·i8·I10 값 형식, 루틴 종료·공백 줄(375–379). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 40–41·74–78: 명령행 파일명은 길이 80의 arg로 받는다. 실제 입력 이름 변수 binfname의 길이는 7이다. 긴 이름을 위한 별도 길이 검사문은 없다.
- 92–103: 두 open의 errorIO>0 분기는 'Stopping.'을 출력한다. 해당 분기 안에는 stop이나 return이 없다.
- 139–150·173–191·302: 3차원 분기는 get3D=true를 설정하고 getHarmonic을 false로 바꾼다. 기본 배열 출력이나 getReSynth 판독을 중단하는 문장은 해당 분기에 없다.
- 31–35·191–208·302–316: npha·nhage·nhagv의 값 대입은 getHarmonic 분기 안에 있다. getReSynth 분기는 독립적이고 이 변수를 참조한다. 선언에는 초기값이 없다.
- 192·213·215–238: 조화 분석의 첫 정수는 rec=irec+1에서 읽는다. timeud/itud 이후에는 irec를 3만큼 증가시킨다. 입력 open의 RECL은 8로 고정되어 있다.
- 164–171: np_a/ne_a를 읽고 출력한다. 이후 기본 배열 판독 크기는 np_g/ne_g를 복사한 np/ne이다.
- 28·192: icha는 조화 분석 분기에서 읽는다. 이후 icha 값에 따른 조건 분기는 없다.
- 22·39·42: iargc·title·output3D는 이 파일에서 선언 이후 사용되지 않는다.
