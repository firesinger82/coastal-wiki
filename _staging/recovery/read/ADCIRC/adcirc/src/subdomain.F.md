---
file: models/ADCIRC/raw/source_code/adcirc/src/subdomain.F
lines: 853
sha256: 7eea4dea6f36ec14163db542f46dd2d677e742dc9250a35a77cd30c5c43661c9
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# subdomain.F — 판독 구간 기록

구간은 1행부터 853행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | 저작권·LGPL v3 이상·무보증 머리말(1–19). 부분 영역 모델링(subdomain modeling)이 원래 격자에서 작은 격자를 추출해 일련의 폭풍해일(storm surge) 실행 시간을 줄이는 접근이라는 주석과 작성자·2013년 표기를 포함한다(20–34). 빈 줄·logging_macros.h 전처리 포함문·빈 줄(35–37). |
| 38–62 | subdomain 모듈 시작(38). globaldir와 로깅 이름을 가져온다(39–42). 활성 여부·출력 형식/주기·경계 강제(boundary enforcing) 플래그, 기록할 전역/지역 경계 절점, 두 시간 수준의 수위·유속·젖음/마름(wet/dry) 상태 및 강제값 배열을 선언한다(44–58). nlines/bchange, contains와 빈 줄을 포함한다(59–62). 이 선언 블록에는 기본값 대입이 없다. |
| 63–116 | readFort015 입구·매개변수 설명 주석(63–86). 주석은 NOUTGS=0/1/2를 full/old/new run으로 적고 enforceBN=0/1/2를 forcing 없음/old/new로 적는다(68–77). 모듈·인수 없는 루틴의 지역 선언과 추적 로그(89–101). fort.015 존재를 확인하고 없으면 terminate를 호출한다(103–110). 루트만 활성 로그를 출력하고 globaldir의 fort.015를 열어 NOUTGS/NSPOOLGS/enforceBN을 읽는다(112–116). 원문: `#ifdef CMPI` (91); `if (fileFound.eqv..false.) then` (105); `if (myproc.eq.0) print *, "Subdomain Active"` (112). |
| 117–143 | 시작 시 63행 readFort015 안. NOUTGS select의 case 0은 판독문 없는 주석이다(117–119). case 1은 ncbnr와 cbnr 목록을 읽고 할당한다(120–126). case 2는 nobnr/obnr 및 nibnr/ibnr를 각각 읽고 할당한다(127–139). case default는 잘못된 NOUTGS 메시지로 terminate를 호출한다(140–142). select 종료까지 포함한다(143). 원문: `select case(noutgs)` (117); `case(0)` (118); `case(1)` (120); `case(2)` (127); `case default` (140). |
| 144–204 | 시작 시 63행 readFort015 안. CMPI에서 기록 절점 목록을 지역화(localization)한다(144–146). case 0은 주석만 있다(147–148). case 1은 np 루프에서 any(cbnr==nodes_lg(i))를 두 번 검사해 지역 개수를 센 뒤 지역 인덱스 배열을 채운다(149–164). case 2는 obnr/ibnr 각각에 같은 두 단계 처리를 한다(165–195). case default는 terminate다(196–198). select·전처리·루틴 종료와 빈 줄을 포함한다(199–204). 원문: `#ifdef CMPI` (144); `select case(noutgs)` (146); `case(0)` (147); `case(1)` (149); `if(any(cbnr.eq.nodes_lg(i))) then` (153); `localncbnr = localncbnr+1` (154); `if(any(cbnr.eq.nodes_lg(i))) then` (160); `case(2)` (165); `if(any(obnr.eq.nodes_lg(i))) then` (169); `localnobnr = localnobnr+1` (170); `if(any(obnr.eq.nodes_lg(i))) then` (176); `if(any(ibnr.eq.nodes_lg(i))) then` (184); `localnibnr = localnibnr+1` (185); `if(any(ibnr.eq.nodes_lg(i))) then` (191); `case default` (196). 인덱스 증가 원문: `j=j+1` (162); `j=j+1` (178); `j=j+1` (193). |
| 205–270 | writeFort065는 개방 해양 경계(open ocean boundary) 절점의 ETA2·u/v·NODECODE를 기록한다는 주석을 가진다(205–209). it=1이면 CMPI는 PE와 MYPROC의 I4.4 문자열 디렉터리, 비-CMPI는 현재 경로의 fort.065를 REPLACE로 연다(223–235). 헤더의 스텝 수는 rnday를 초로 바꿔 dt×nspoolgs로 나눈 정수값이다(228·233). mod(it,NSPOOLGS)=0이면 APPEND로 열어 스텝 번호와 절점당 두 레코드를 쓴다(239–260). CMPI는 전역 절점 번호 gn, 비-CMPI는 cbnr의 n을 쓴다(245–258). close·루틴 종료와 빈 줄까지 포함한다(261–270). 원문: `if (it.eq.1) then` (223); `write(1065,*) nspoolgs,localncbnr,int(rnday*86400/(dt*nspoolgs)),` (228); `write(1065,*) nspoolgs,ncbnr,int(rnday*86400/(dt*nspoolgs)),` (233); `if(mod(it,NSPOOLGS).eq.0) then` (239). |
| 271–336 | writeFort066는 외측 경계(outer boundary)의 ETAS·u/v·NODECODE를 쓴다(271–278). it=1의 CMPI/비-CMPI 분기는 각각 PE####/fort.066과 현재 경로 fort.066을 REPLACE로 열고 헤더를 쓴다(289–301). 스텝 수 식은 아래 원문과 같다(294·299). mod(it,NSPOOLGS)=0일 때 APPEND하며 지역 인덱스를 전역 번호로 바꾸거나 obnr의 n을 사용해 두 레코드를 쓴다(305–326). close·종료·빈 줄을 포함한다(327–336). 원문: `if (it.eq.1) then` (289); `write(1066,*) nspoolgs,localnobnr,int(rnday*86400/(dt*nspoolgs)),` (294); `write(1066,*) nspoolgs, nobnr,int(rnday*86400/(dt*nspoolgs)),` (299); `if(mod(it,NSPOOLGS).eq.0) then` (305). |
| 337–397 | writeFort067는 내측 경계(inner boundary)의 ETAS를 기록한다(337–344). it=1이면 CMPI의 PE#### 경로 또는 현재 경로 fort.067을 REPLACE로 열고 헤더를 쓴다(355–367). 스텝 수 계산식은 아래 원문과 같다(360·365). mod(it,NSPOOLGS)=0이면 APPEND로 스텝 번호와 절점별 ETAS 한 레코드를 쓴다(371–390). CMPI는 nodes_lg로 전역 번호를 구한다(377–380). close·종료·빈 줄을 포함한다(391–397). 원문: `if (it.eq.1) then` (355); `write(1067,*) nspoolgs,localnibnr,int(rnday*86400/(dt*nspoolgs)),` (360); `write(1067,*) nspoolgs, nibnr, int(rnday*86400/(dt*nspoolgs)),` (365); `if(mod(it,NSPOOLGS).eq.0) then` (371). |
| 398–455 | openFort019H(TimeLoc)는 핫스타트(hotstart)용 경계조건 파일의 위치를 찾는다는 주석을 가진다(398–400). myproc/iths/neta·종료 루틴과 CMPI messenger를 사용하고 TimeLoc를 입력으로 선언한다(402–413). CMPI는 PE####/fort.019, 비-CMPI는 globaldir/fort.019를 연다(414–419). 헤더·sbtiminc/ncbn·cbn을 읽으며 abs(ncbn-neta)>1이면 terminate한다(420–432). 두 수준의 수위·u/v·젖음/마름·강제값 배열을 할당하고 첫 수준을 0으로 설정한다(433–442). 첫 경계 레코드를 두 번째 수준에 읽고 첫 젖음/마름 상태에 복사한다(443–449). 루틴 종료·빈 줄까지 포함한다(451–455). 원문: `if (abs(ncbn-neta).gt.1) then` (426). |
| 456–512 | openFort019C는 콜드스타트(coldstart) 경계 입력을 연다(456–475). CMPI/비-CMPI 경로 구분과 헤더·sbtiminc/ncbn·cbn 판독은 앞 루틴과 같은 구조다(470–481). abs(ncbn-neta)>1이면 terminate한다(482–488). 두 수준·강제값 배열 할당, 첫 수위·속도·젖음/마름 0 초기화, 첫 레코드 판독 뒤 젖음/마름 복사를 수행한다(489–506). 종료·빈 줄까지 포함한다(508–512). 원문: `if (abs(ncbn-neta).gt.1) then` (482). |
| 513–559 | readFort019는 ETA2·u/v·젖음/마름 경계 입력이라는 주석과 it 입력을 가진다(513–526). it=1이고 ihot=0이면 openFort019C를 호출한다(528–530). mod(it,sbtiminc)=0이면 첫 수준으로 이전 값을 복사하고 새 두 번째 수준을 읽는다(532–543). rateTS는 스텝 나머지/실수 sbtiminc다(546). 수위·u/v는 두 수준 사이 선형 보간(linear interpolation), 젖음/마름 강제값은 첫 수준을 그대로 사용한다(547–552). 종료와 빈 줄까지 포함한다(554–559). 원문: `if (it.eq.1.and.ihot.eq.0) then  ! coldstart` (528); `if (mod(it,sbtiminc).eq.0) then` (532); `rateTS = mod(it,sbtiminc)/dble(sbtiminc)` (546); `setEcb(i) = ecbn1(i) + (ecbn2(i)-ecbn1(i))*ratets` (548); `setUcb(i) = ucbn1(i) + (ucbn2(i)-ucbn1(i))*ratets` (549); `setVcb(i) = vcbn1(i) + (vcbn2(i)-vcbn1(i))*ratets` (550). |
| 560–611 | readFort020 입구·외측 경계 ETAS·u/v·젖음/마름 입력 주석·선언(560–573). it=1이면 CMPI의 PE#### 또는 globaldir에서 fort.020을 열어 헤더·sbtiminc/nobn·obn 목록을 읽고 배열을 할당한다(575–592). 판독 주기 if는 주석이며 이후 read는 호출마다 실행된다(594–605). 이전 wdobn2를 wdobn1에 복사하고 새 레코드를 읽어 setE/U/V/WDob에 그대로 복사한다(595–604). 루틴 종료·빈 줄을 포함한다(607–611). 원문: `if (it.eq.1) then` (575); `!if (mod(it,sbtiminc).eq.0) then` (594). |
| 612–655 | readFort021 입구·내측 경계 ETAS 입력 주석·선언(612–625). it=1이면 CMPI의 PE#### 또는 globaldir에서 fort.021을 열어 헤더·sbtiminc/nibn·ibn과 수위/강제값 배열을 준비한다(627–641). 판독 주기 if는 주석이다(643). 호출마다 레코드를 읽어 eibn2와 setEib에 복사한다(644–650). 종료·빈 줄까지 포함한다(652–655). 원문: `if (it.eq.1) then` (627); `!         if (mod(it,sbtiminc).eq.0) then` (643). |
| 656–674 | enforceEcb는 cbn 목록의 n=cbn(i)를 구해 ETA2(n)에 setEcb(i)를 복사한다(656–668). 주석은 timestep.F에서 호출한다고 적혀 있다(658–659). 선언·루프 종료·루틴 종료·빈 줄을 포함한다(661–674). 원문: `ETA2(n) = setEcb(i)` (667). |
| 675–693 | enforceEob는 obn 목록의 절점 ETAS를 setEob로 설정한다(675–687). 외측 경계 강제 주석·모듈·지역변수 선언·종료·빈 줄을 포함한다(677–693). 원문: `ETAS(n) = setEob(i)` (686). |
| 694–713 | enforceUVcb는 cbn 절점의 UU2/VV2를 setUcb/setVcb에서 복사한다(694–707). 개방 해양 경계 속도 강제 주석과 선언·종료·빈 줄을 포함한다(696–713). 원문: `UU2(n) = setUcb(i)` (705); `VV2(n) = setVcb(i)` (706). |
| 714–732 | enforceUVob는 obn 절점의 UU2/VV2를 setUob/setVob에서 복사한다(714–727). 외측 경계 속도 강제 주석·선언·종료·빈 줄을 포함한다(716–732). 원문: `UU2(n) = setUob(i)` (725); `VV2(n) = setVob(i)` (726). |
| 733–752 | enforceWDcb는 cbn 절점의 NNODECODE를 setWDcb에서 복사한다(733–745). 주석은 outer boundary라고 적혀 있다(735–736). 모듈·변수 선언·종료·빈 줄을 포함한다(738–752). 원문: `NNODECODE(n) = setWDcb(i)` (744). |
| 753–773 | enforceWDob는 obn 절점의 NNODECODE를 setWDob에서 복사한다(753–765). 외측 경계 젖음/마름 강제 주석·선언·종료·빈 줄을 포함한다(755–773). 원문: `NNODECODE(n) = setWDob(i)` (764). |
| 774–792 | enforceEib는 ibn 절점의 ETAS를 setEib에서 복사한다(774–786). 내측 경계 강제 주석·모듈·지역변수 선언·종료·빈 줄을 포함한다(776–792). 원문: `ETAS(n) = setEib(i)` (785). |
| 793–823 | enforceGWCELVob는 일반화 파동 연속방정식(generalized wave continuity equation, GWCE)의 벡터를 바꿔 jcg 해법이 외측 경계 수위를 따르도록 한다는 주석을 가진다(793–798). COEF/ETAS/GWCE_LV와 이웃 표 NEITAB를 가져온다(800–805). 각 obn 절점에서 newGWCElv=0으로 시작한다(807–809). j=1..mnei의 neighbor가 0이 아닐 때 COEF×ETAS를 누적한 뒤 GWCE_LV(n)에 대입한다(810–817). 종료·빈 줄을 포함한다(819–823). 원문: `if (neighbor.ne.0) then` (812); `newGWCElv = newGWCElv + COEF(n,j)*ETAS(neighbor)` (813). |
| 824–853 | checkChange는 외측 경계 젖음/마름 변화와 다음 스텝 재계산 플래그에 관한 주석을 가진다(824–828). ilump와 CMPI messenger를 사용한다(830–834). bchange=1이면 ncchange=1로 두고 bchange=0으로 되돌린다(836–839). 이전/새 상태가 다르면 bchange=1로 설정한다(840–844). CMPI에서 ILump=0이면 WetDrySum(NCCHANGE)을 호출한다(845–849). 루틴·모듈 종료와 빈 줄을 포함한다(851–853). 원문: `if (bchange.eq.1) then` (836); `if (wdobn2(i).ne.wdobn1(i)) then` (841); `IF ( ILump.eq.0 ) THEN` (846). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 69–71·118–120·147–150: 머리말의 NOUTGS=0 설명은 full run이다. 두 select의 case 0 주석은 subdomain run (no b.c. recording)이다. case 1은 cbnr 목록을 판독·지역화한다.
- 90–96: CMPI 전처리를 켠 readFort015에는 mod_terminate의 같은 only 목록 use가 두 번 적혀 있다.
- 103–116·202: readFort015는 단위 1015를 연다. 이 파일에는 단위 1015를 닫는 close가 없다.
- 44·50–51·59: subdomainOn, eobn1/uobn1/vobn1/eibn1, nlines는 이 파일의 실행문에서 사용하지 않는다. bchange 선언에는 초기값 대입이 없다.
- 228·233·239·294·299·305·360·365·371·532·546: NSPOOLGS와 sbtiminc는 나눗셈 또는 mod의 인수다. 이 파일에는 두 값의 양수 여부 검사 조건이 없다.
- 398–449: openFort019H의 TimeLoc 입력과 iths, 지역 j/it/itread는 본문에서 사용하지 않는다. 본문은 첫 경계 레코드를 읽는다. 주석의 적절한 파일 위치 찾기와 연결되는 탐색 루프는 이 루틴에 없다.
- 426·482: ncbn과 neta 비교는 abs(ncbn-neta)>1이다. 차이가 1인 경우에는 이 조건의 terminate를 호출하지 않는다.
- 546–551: readFort019는 수위·u/v만 보간한다. setWDcb는 첫 시간 수준 wdcbn1을 사용한다.
- 594–605·643–650: readFort020/readFort021의 mod(it,sbtiminc) 판독 조건은 주석이다. 두 루틴은 호출마다 새 레코드를 읽는다.
- 588–589·597–599: wdobn2는 할당 뒤 별도 초기화 없이 첫 호출에서 wdobn1에 복사된다. 새 wdobn2 판독은 이 복사문 뒤에 있다.
- 421·477·583·635: fort.019/020/021의 헤더 판독은 동일한 모듈 변수 sbtiminc에 대입한다. 파일별로 별도 주기를 저장하는 변수가 없다.
- 444–447·501–504·533–541·595–599·644–647: 레코드 스텝 번호와 절점 번호를 n에 읽는다. 이 판독 블록에는 파일 번호와 cbn/obn/ibn 목록을 비교하는 조건이 없다.
- 38–59·824–849: 모듈과 checkChange에는 implicit none이 없다. checkChange의 GLOBAL only 목록은 ilump다. 비-CMPI 코드에는 NCCHANGE를 가져오는 use나 명시 선언이 없다. CMPI의 MESSENGER 내부는 판독하지 않았다.
