---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_wq_vars.f90
lines: 1121
sha256: 73124452069610344389ce9772c8f76c272ad449fb9f840d87169f5fbfe30ed1
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_wq_vars.f90 — 판독 구간 기록

구간은 1행부터 1121행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | EFDC+ 안내·저작권·GPLv2 머리말(1–8). `Module Variables_WQ`는 GLOBAL을 사용하고 implicit none을 지정한다(9–11). 수질 성분명 WQCONSTIT(50)·동물플랑크톤명 ZOONAME(20)을 선언한다(13–14). 상수 원문은 `integer, parameter :: MAXWQ = 50 !< Maximum number of WQ components` (17), `integer, parameter :: NTSWQVM = 50    !< Maximum number of WQ time series` (18). 조류(algae)·동물플랑크톤(zooplankton) 그룹 수, 이동성·침강 플래그와 수질 성분 인덱스를 선언한다(19–30). 빈 줄과 수층 부영양화(water column eutrophication) 주석까지 포함한다(31–32). |
| 33–110 | 시작 시 9행 Variables_WQ 모듈 선언부 안. 수질 변수 수·입출력 플래그·구역 수·온도 조회표(lookup table) 크기를 선언한다(35–83). 기본값 원문은 `integer :: IWQZONES = 0    !< Flag to activact the use of WQ zones` (37), `integer :: IWQBEN = 0      !< Sediment diagensis flux option` (38). IWQICI 주석은 초기조건 0=상수·1=공간별 수심 평균·2=수평·수직 변화를 적는다(44). IDOSFRM 주석은 용존산소(dissolved oxygen) 포화식 0/1/2, IDOSELE 주석은 고도 보정 0/1/2를 적는다(81–82). ISKINETICS·ISTRWQ는 MAXWQ 크기이다(84–85). 점원(point source)·네 방향 개방경계(open boundary)·구역 대응의 정수 allocatable 배열, NWQCSR(NTSWQVM)을 선언한다(87–109). |
| 111–190 | 시작 시 9행 모듈 선언부 안. 시간 간격과 실수 수질 계수를 선언한다(112–153). DOELEV·WQAOCR부터 WQKTCOD까지 표시된 초기화는 0이다(117·119–153). 광합성 유효복사(photosynthetically active radiation) 비율의 원문은 `real :: PARADJ    = 0.43   ! Photosynthetically active solar radiation fraction` (118). 수심·역수심·염분·수온·역층체적·조류 인/탄소비, 습성 침적(wet deposition), 퇴적물 플럭스(sediment flux), 엽록소(chlorophyll), 유기물 침적 플럭스, 배경 소광계수(extinction coefficient), 경계농도·인/규소 가용상 비율·온도표·점원 질량부하 배열을 선언한다(155–188). 퇴적물 플럭스 배열은 target 속성을 갖는다(165–170). 빈 줄(154·158·189–190)도 포함한다. |
| 191–252 | 시작 시 9행 모듈 선언부 안. `type ALGAECLASS`를 시작한다(192). 이름·그룹 ID·염분 독성·겨울 증식·규소 활성·유속 제한·이동성 필드가 있다(193–199). IDN 주석은 1=남세균(cyanobacteria)·2=규조류(diatoms)·3=녹조류(green algae)·4=대형조류(macroalgae)를 적는다(194). 최대 생물량(biomass), 성장·포식 최적 온도와 온도 계수, 질소·인·CO2 반포화상수(half-saturation constant), 탄소/엽록소비, 포식·기초대사(basal metabolism) 산물의 탄소·인·질소 분배율을 선언한다(201–243). 규소 산물 분배율·규소/탄소비·규소 반포화상수를 선언한다(245–251). 이 구간 필드에는 선언 시 기본값이 없다. |
| 253–321 | 시작 시 9행 모듈·192행 ALGAECLASS 형식 안. 탄소/건중량비·대형수생식물(macrophyte) 소광계수·남세균 염분 독성·산소 화학량론(stoichiometry)·식물 높이 환산·성장 시작 수심·최대 길이를 선언한다(253–266). 유체역학 되먹임(hydrodynamic feedback)의 ISDRAG·ISMACL 주석은 0/1 옵션이며 항력(drag)·직경·줄기 높이·밀도·차단계수를 선언한다(268–275). ISVARSETTLE 주석은 0=지정 침강/부상속도·1=일중 변화·2=일중 및 빛 의존·3=Visser 등의 동적 속도를 적는다(278–282). 밀도·광량·위상·세포 항력과 구역별 성장·대사·유속 제한·침강·최소 생물량 배열이 있다(283–316). WQKMVA부터 WQKMVE까지의 주석 식은 `Vel_limit = D + (A - D) / (1 + (Vel/C)**B)**E` (310–314)이며 실행 대입식은 아니다. 층별 SETTLING 배열 선언 뒤 형식을 끝낸다(318–321). |
| 322–377 | 시작 시 9행 모듈 선언부 안이며 ALGAECLASS 형식 밖. 기본값 원문은 `integer :: MACDRAG = 0` (322). ALGAES와 현재/광조건 세포밀도 3차원 배열을 선언한다(323–325). 유기탄소·인·질소 가수분해(hydrolysis), 질산화(nitrification), 탈질(denitrification), 규소 분배, 산소 호흡, 일사, 총활성금속(TAM)의 용해도, 분변성 대장균군(fecal coliform bacteria) 감쇠, 퇴적물 산소요구량(sediment oxygen demand) 온도 계수와 출력 시각을 선언한다(327–376). WQKFCB 주석 단위는 1/day이고 WQNITM 주석 단위는 /day이다(370·354). 이 구간에는 실행식·호출이 없다. |
| 378–424 | 시작 시 9행 모듈 선언부 안. 수질 구역·부하·온도표 인덱스용 정수 배열을 선언한다(379–387). 성장·대사·포식률, 3차원 조류 수직 이동률, 온도 의존표, 층 상단 수심비, 일중 산소·광 소광 분석과 재폭기(reaeration)·COD 계수 배열을 선언한다(390–424). WQKRO 주석은 OConnor-Dobbins 3.933·Owen-Gibbs 5.32를 적는다(410). WQWSLP와 WQWSRP 주석은 모두 refractory POM 침강속도(m/day)라고 적는다(422–423). 계수 값 대입은 이 선언 구간에 없다. |
| 425–480 | 시작 시 9행 모듈 선언부 안. 대기부하·일사·점원 시계열·층 높이 역수·유기물 가수분해·DOC 호흡·탈질·암모늄 선호도·산소포화·동역학(kinetics) 행렬·생성/소멸 누적·입자 침강·현재층 영양염 배열을 선언한다(425–469). SMAC 주석은 고정 생물군을 1.0/0.0으로 켜고 끄는 플래그이다(470). 용존 이산화탄소(dissolved carbon dioxide)용 CO2WQ·CDOSATIDX·WQCDOS·WQITOP·WQKRCDOS·WQP22를 선언한다(472–479). 빈 줄(471·480)까지 포함한다. |
| 481–552 | 시작 시 9행 모듈 선언부 안. 대형수생식물/부착생물(periphyton) 존재 셀, 최하·최상층, 높이·직경·층 점유율·차단비·단위체적 식물 투영면적 배열을 선언한다(482–491). 퇴적물 속성변화(sediment diagenesis) 플래그·구역 수·반응 그룹 수를 선언한다(493–507). NSMG 주석은 G1/G2/G3의 3개로 고정한다고 적지만 선언에는 대입이 없다(504). 온도 확산·고체농도·입자 혼합·저산소 이력(hysteresis)·질산화·인/규소 흡착·황화수소 산화·용존/입자상 분율·온도표 범위 계수를 선언한다(509–551). 이 구간에는 실행식이 없다. |
| 553–610 | 시작 시 9행 모듈 선언부 안. 퇴적물 온도표 인덱스·구역 대응과 수층/퇴적물 연결 배열을 선언한다(554–558). 공극수(pore water) 확산·입자 혼합·조류 유래 탄소/질소/인의 반응 그룹별 분율·층간 혼합·탈질/질산화 반응속도·온도 의존 계수·매몰속도(burial rate)·산소요구량 배율을 선언한다(559–609). SMW2 주석 단위는 cm/year이고 SMDD·SMDP 주석 단위는 m2/day이다(601·561·566). 이 구간 배열은 모두 allocatable 선언이며 실제 할당은 뒤의 SD_Allocate에 있다. |
| 611–642 | 시작 시 9행 모듈 선언부 안. 퇴적물 입자상 탄소·인·질소·규소 배열을 선언한다(611–614). SM1/SM2 황화수소·암모늄·질산염·인산염·규소, 스트레스·산소요구량·플럭스 배열은 target 속성을 갖고 SMHYST는 논리 배열이다(616–633). 동물플랑크톤 그룹 인덱스·온도표 인덱스·온도표 하한/상한/간격을 선언한다(635–641). 이 구간 선언에는 초기값이 없다. |
| 643–707 | 시작 시 9행 모듈 선언부 안. `type ZOOPLGROUP`는 이름·ID·피식/포식 플래그를 가진다(643–647). 섭식(grazing) 탄소 임계값·원소/탄소비·먹이 반포화상수·유기탄소 이용률·온도 계수·임계 산소·사망률을 선언한다(649–667). 사망·포식·대사 산물의 탄소·질소·인·규소 분배율을 선언한다(668–697). 최대 섭식량·기준온도 대사/포식률·조류 이용률과 셀별 성장/대사/포식/사망률 배열을 선언하고 형식을 끝낸다(699–707). 필드 기본값 대입은 없다. |
| 708–750 | 시작 시 9행 모듈 선언부 안이며 ZOOPLGROUP 형식 밖. ZOOPL·가용 먹이·가용 조류/유기탄소·온도 의존표·동역학 행렬·점원 부하·분율·조류 영향·탄소/질소/인/규소/산소 영향 배열을 선언한다(709–741). `Contains` (743) 뒤 WQ_Allocate의 배열 할당·초기화 안내 주석이 있다(744–750). 실행 루틴은 다음 구간에서 시작한다. |
| 751–808 | `Subroutine WQ_Allocate`는 Allocate_Initialize를 사용하고 NAL을 선언한다(751–753). `AllocateDSI`로 네 방향 경계 셀 인덱스·농도 시계열 인덱스·수질 구역 대응·점원 인덱스를 정수 0 인수로 할당한다(756–776). 경계 시계열 크기는 각 NBB*M과 NWQVM이고 셀별 대응은 LCM·KCM이다(760–766). NWQCSR 할당 호출은 주석 처리되며 SCANWQ가 먼저 사용한다는 주석이 있다(778). TWQ·SWQ·VOLWQ·WQAPC·대기부하·퇴적물 플럭스·엽록소·침적·경계농도·인/규소 비율·점원 부하·XSMO20에 대해 실수 0.0 인수로 AllocateDSI를 호출한다(781–808). 개방경계 농도 배열 두 번째 크기는 2이다(801–804). |
| 809–842 | 시작 시 751행 WQ_Allocate 안. ALGAES(NALGAEM)를 할당하고 `Do NAL = 1, NALGAEM` (813)에서 IDN=NAL과 구역별 생리계수·유속 제한계수 배열의 AllocateDSI를 호출한다(814–831). SETTLING 호출 원문은 `call AllocateDSI(ALGAES(NAL).SETTLING, LCM, -KCM, 0.0)` (833)이다. 루프 종료 뒤 LAYERBOT은 1, LAYERTOP은 KC를 초기화 인수로 넘긴다(836–837). 높이 배열 호출 원문은 `call AllocateDSI(HEIGHT_MAC,     LCM,     -NALGAEM,  0.)` (838)이다. 직경·층 점유율·차단비·투영면적도 AllocateDSI로 0. 인수를 넘긴다(839–842). 음수 크기 인수의 내부 해석은 이 파일에 없다. |
| 843–888 | 시작 시 751행 WQ_Allocate 안. 수질 구역·퇴적물 대응·점원 시계열 인덱스 배열에 정수 0을 넘긴다(844–851). 셀별 조류 성장/대사/포식, 온도표, 일중 산소·광 분석, 재폭기·가수분해·COD·규소·침강·대기부하 배열에 실수 0.0을 넘겨 AllocateDSI를 호출한다(853–888). WQBSETL의 중간 크기는 4이다(856). IBENMAP의 두 번째 크기는 2이다(845). 온도표는 NWQTDM, 구역 계수는 NWQZM, 공간 분석은 LCM·KCM을 사용한다. |
| 889–932 | 시작 시 751행 WQ_Allocate 안. 퇴적물 특성·일사 시계열·점원 부하 시간/값·역층높이·가수분해/호흡/탈질·질산화·산소·영양염·침강·생성/소멸 작업 배열에 실수 0.0을 넘겨 AllocateDSI를 호출한다(889–931). 시계열 일사 배열의 크기는 NDASER이다(890–892). V_MLSER의 크기 인수는 NDWQPSR·NWQVM·NWQPSRM이다(895). WQRPSET·WQLPSET·WQWSSET의 두 번째 크기는 2이다(919–921). 고정 생물군 플래그 호출 원문은 `call AllocateDSI(SMAC,     LCM,   1.0)        !< Fixed biota flag set to "on"` (932)이다. |
| 933–965 | 시작 시 751행 WQ_Allocate 안. ICWQTS·WQV·WQVO·WQWPSLC·WQPSSRT를 직접 allocate하며 각각 0:NWQVM, 0:KCM, 0:NWQPSM, 0:NWQPSRM의 명시적 하한을 사용한다(935–939). 해당 배열을 0/0.0으로 초기화한다(940–944). `deallocate(WQKEB)` (946) 후 AllocateDSI로 NWQZM 크기를 다시 할당한다(947). 이산화탄소 작업 배열을 0.0 인수로 할당한다(950–955). `do NAL = 1, NALGAE` (957) 안의 조건 원문은 `if( IVARSETL == 3 )then` (958)이다. 참이면 CELLDENS·CELLDENSLIGHT를 LCM·KCM·NALGAE 크기, 0.0 인수로 할당하고 `EXIT` (961)한다. 조건·루프·루틴을 끝낸다(962–965). |
| 966–1006 | SD_Allocate 설명 주석·빈 줄 뒤 `Subroutine SD_Allocate`가 Allocate_Initialize를 사용한다(967–976). 퇴적물 온도 인덱스·구역 대응을 정수 0 인수로 할당한다(979–980). 수층/퇴적물 연결·확산·입자 혼합·유기물 반응 그룹 분배·퇴적물 두께/시간·플럭스 배열을 실수 0.0 인수로 AllocateDSI에 넘긴다(983–1006). SMFCBA·SMFNBA·SMFPBA는 NALGAEM·NSMGM 크기이고 SMFCR·SMFNR·SMFPR는 NSMZM·NSMGM 크기이다(995–1000). |
| 1007–1058 | 시작 시 975행 SD_Allocate 안. 반응속도·층간 혼합·온도표·매몰·산소요구량·퇴적물 농도·플럭스·온도 배열을 실수 0.0 인수로 AllocateDSI에 넘긴다(1007–1052). 온도표 배열은 NWQTDM, 구역 계수는 NSMZM, 유기물 농도/플럭스는 LCM·NSMGM 크기를 사용한다. 논리 배열은 `allocate(SMHYST(LCM))` (1055)로 직접 할당한다. 이 호출 다음에는 값 대입 없이 SD_Allocate가 끝난다(1057). 빈 줄(1053·1056·1058)도 포함한다. |
| 1059–1086 | 머리말 주석은 Subroutine WQ3DINP와 SD 배열 할당을 적는다(1062·1064). 실제 루틴은 `Subroutine Zoo_Allocate` (1067)이며 Allocate_Initialize를 사용하고 지역 NZO를 선언한다(1068–1069). IWQZT를 LCM 크기, 정수 0 인수로 할당한다(1072). ZOOPL(NZOOPL)를 직접 할당하고 `Do NZO = 1, NZOOPL` (1077)에서 그룹별 RMAXZ·BMRZ·PRRZ를 NWQZM, UBZ를 NALGAEM, WQGZ·WQBZ·WQPZ·WQDZ를 LCM 크기, 실수 0.0 인수로 AllocateDSI에 넘긴다(1078–1085). 그룹 루프가 끝난다(1086). |
| 1087–1121 | 시작 시 1067행 Zoo_Allocate 안이며 1077행 그룹 루프 밖. 가용 먹이·유기탄소·온도표·동역학 작업 배열·점원 부하·분율·조류 및 원소 영향 배열에 대해 AllocateDSI를 호출하며 실수 초기화 인수는 모두 0.0이다(1088–1116). BAZ는 LCM·NZOOPL·NALGAEM, WQWPSZ는 LCM·KCM·NZOOPL, SBZPAL은 LCM·KCM·NALGAEM이다(1089·1098·1102). 영향 배열 SLPOCZ부터 SDOZ까지는 LCM·KCM이다(1103–1116). Zoo_Allocate 종료·빈 줄·Variables_WQ 모듈 종료까지 포함한다(1118–1121). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 192–321·811–834: ALGAECLASS의 일반 필드에는 선언 시 초기값이 없다. WQ_Allocate의 그룹 루프는 IDN과 allocatable 필드만 설정한다. 나머지 일반 필드의 값 대입은 이 루틴에 없다.
- 422–423: WQWSLP와 WQWSRP의 설명 주석은 모두 refractory POM 침강속도라고 적는다.
- 643–707·1075–1086: ZOOPLGROUP의 일반 필드에는 선언 시 초기값이 없다. Zoo_Allocate의 그룹 루프는 allocatable 필드만 할당한다.
- 652: ASCZ 주석은 Phosphorus-to-Carbon이라고 적지만 단위는 gSi/gC로 적는다.
- 946–947: WQKEB를 해제한 뒤 다시 할당한다. 해제 앞에 allocated 조건 검사는 이 루틴에 없다.
- 957–963: CELLDENS·CELLDENSLIGHT 할당 조건은 그룹 번호 NAL을 참조하지 않는 스칼라 IVARSETL==3이다. 할당 뒤 EXIT로 그룹 루프를 끝낸다.
- 1055–1057: SD_Allocate는 SMHYST를 직접 할당한다. 이 루틴에는 SMHYST 값 초기화가 없다.
- 1062–1067: Zoo_Allocate 앞 주석의 루틴 이름은 WQ3DINP이고 설명 대상은 SD 배열이다. 실제 선언 이름은 Zoo_Allocate이다.
