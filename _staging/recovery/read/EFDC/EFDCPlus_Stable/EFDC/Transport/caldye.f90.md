---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Transport/caldye.f90
lines: 148
sha256: 48df6a60d5945a60aa4e8bd200f83a040c4d08d01f3632482a784dd29ad5d801
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# caldye.f90 — 판독 구간 기록

구간은 1행부터 148행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | CALDYE의 GPLv2 머리말·GLOBAL·Allocate_Initialize 사용을 포함한다(1–14). SAVE 할당 배열 DYEF·TTHICK, 지역 인덱스·계수, SAVE DYESTEP 및 외부 CALVOLTERM을 선언한다(16–22). DYEF가 미할당이면 AllocateDSI를 LCM,-KCM,0.0 인수로 두 배열에 호출하고 DYESTEP=0으로 초기화한다(24–28). 매 호출 DYESTEP에 DELT를 더한다(30). 원문: `if( .not. allocated(DYEF) )then` (24); `DYESTEP = 0.0` (27); `DYESTEP = DYESTEP + DELT` (30). |
| 32–51 | 시작 시 9행 CALDYE 루틴 안이다. IFIRST=1로 두고 MD=1..NDYE를 순회한다(32–33). 염료(dye) ITYPE=0은 보존성(conservative) 분기이며 CYCLE한다(35–37). ELSEIF ITYPE=1은 비보존성(nonconservative) 분기다(39–40). SETTLE/=0이고 KC>1이면 침강(settling)·상승(rising)을 계산한다(43). IFIRST=1일 때 K·LP 루프에서 TTHICK=DELT*HPKI를 계산하고 IFIRST=0으로 만든다(44–50). 원문: `IFIRST = 1` (32); `do MD = 1,NDYE` (33); `if( DYES(MD).ITYPE == 0  )then` (35); `elseif( DYES(MD).ITYPE == 1 )then` (39); `if( DYES(MD).SETTLE /= 0 .and. KC > 1 )then` (43); `if( IFIRST == 1 )then` (44); `do K = 1,KC` (45); `do LP = 1,LLWET(K+1,ND)` (46); `TTHICK(L,K) = DELT*HPKI(L,K)` (47); `IFIRST = 0` (50). |
| 52–71 | 시작 시 9행 CALDYE 루틴, 33행 DO 루프, 39행 ELSEIF 분기(35행 IF 선택문), 43행 IF 참 분기 안이다. 표층 KC의 젖은 셀 목록을 순회하여 CLEFT, 0 이상 농도 CRIGHT, 갱신 농도와 하부면 DYEF를 계산한다(53–59). K=KS..1 역순으로 아래 층을 처리한다(61–63). CLEFT는 1+SETTLE*TTHICK이며 CRIGHT에서 상부 DYEF*TTHICK를 빼고 농도를 나눈다(64–66). 하부면 DYEF=-SETTLE*DYE를 저장하고 침강 조건을 닫는다(67–70). 원문: `do LP = 1,LLWET(KC,ND)` (53); `L = LKWET(LP,KC,ND)` (54); `CLEFT = 1.0 + DYES(MD).SETTLE*TTHICK(L,K)` (55); `CRIGHT = max(DYE(L,KC,MD),0.0)` (56); `DYE(L,KC,MD) = CRIGHT/CLEFT` (57); `DYEF(L,KC-1) = -DYES(MD).SETTLE*DYE(L,KC,MD)` (58); `do K = KS,1,-1` (61); `do LP = 1,LLWET(K-1,ND)` (62); `L = LKWET(LP,K-1,ND)` (63); `CLEFT = 1.0 + DYES(MD).SETTLE*TTHICK(L,K)` (64); `CRIGHT = max(DYE(L,K,MD),0.0) - DYEF(L,K)*TTHICK(L,K)` (65); `DYE(L,K,MD) = CRIGHT/CLEFT` (66); `DYEF(L,K-1) = -DYES(MD).SETTLE*DYE(L,K,MD)` (67). |
| 72–106 | 시작 시 9행 CALDYE 루틴, 33행 DO 루프, 39행 ELSEIF 분기(35행 IF 선택문) 안이다. DYESTEP>=DYESTEPW이면 동역학(kinetics) 처리를 수행한다(73). TREF>0, 온도 수송 활성, KRATE0>0 조건은 DAGE=DYESTEP/86400으로 일(day) 단위를 만든다(76–78). 층·젖은 셀 루프는 KRATE0·KRATE1의 온도차 거듭제곱을 사용하여 DYE를 줄인다(79–82). ELSEIF KRATE1/=0은 온도 독립 변화다(86). KRATE1<0이면 EXP(-KRATE1*DYESTEP), else는 1/(1+DYESTEP*KRATE1)을 계수로 쓴다(88–92). 병렬 ND·K·젖은 셀 루프에서 계수를 농도에 곱한다(94–103). 원문: `if( DYESTEP >= DYESTEPW )then` (73); `if( DYES(MD).TREF > 0. .and. ISTRAN(2) > 0 .and. DYES(MD).KRATE0 > 0.0 )then` (76); `DAGE = DYESTEP/86400.` (78); `do K = 1,KC` (79); `do LP = 1,LLWET(K,ND)` (80); `L = LKWET(LP,K,ND)` (81); `DYE(L,K,MD) = DYE(L,K,MD) - ( DYES(MD).KRATE0**(TEM(L,K)-DYES(MD).TREF) + DYE(L,K,MD)*DYES(MD).KRATE1**(TEM(L,K)-DYES(MD).TREF) )*DAGE` (82); `elseif( DYES(MD).KRATE1 /= 0.0 )then` (86); `if( DYES(MD).KRATE1 < 0.0 )then` (88); `CDYETMP = EXP(-DYES(MD).KRATE1*DYESTEP)     ! *** Exponential decay` (89); `CDYETMP = 1./(1.+DYESTEP*DYES(MD).KRATE1)   ! *** Growth rate` (91); `do ND = 1,NDM` (95); `do K = 1,KC` (96); `do LP = 1,LLWET(K,ND)` (97); `L = LKWET(LP,K,ND)` (98); `DYE(L,K,MD) = CDYETMP*DYE(L,K,MD)` (99). |
| 107–129 | 시작 시 9행 CALDYE 루틴, 33행 DO 루프, 39행 ELSEIF 분기(35행 IF 선택문), 73행 IF 참 분기 안이다. 휘발(volatilization) KL_OPT>0이며 온도 수송 또는 IVOLTEMP가 활성일 때 분자량(molecular weight)의 역거듭제곱 DYEMW를 계산한다(108–109). 병렬 ND·표층 젖은 셀 루프는 CALVOLTERM에 수심·역층두께·유속·수온·염분·대기·풍속·휘발 옵션과 표층 농도를 전달한다(112–118). VOLTERM*DYESTEP을 표층 농도에서 빼고 0 이상으로 제한한다(120–121). 휘발 분기 뒤 DYESTEP=0으로 초기화하고 동역학 조건을 닫는다(125–128). 원문: `if( DYES(MD).VOL.KL_OPT > 0 .and. ( ISTRAN(2) > 0 .or. IVOLTEMP > 0 ) )then` (108); `DYEMW = 1./DYES(MD).VOL.MW**0.66667` (109); `do ND = 1,NDM` (112); `do LP = 1,LLWET(KC,ND)` (113); `L = LKWET(LP,KC,ND)` (114); `VOLTERM = CALVOLTERM(HP(L), HPKI(L,KC), STCUV(L), UHE(L), VHE(L), HU(L), HV(L), TEM(L,KC), SAL(L,KC), &` (116); `TATMT(L), PATMT(L), WINDST(L), VOL_VEL_MAX, VOL_DEP_MIN, DYEMW, DYES(MD).VOL.HE,                &` (117); `DYES(MD).VOL.AIRCON, DYES(MD).VOL.TCOEFF, DYES(MD).VOL.MULT, DYE(L,KC,MD), DYES(MD).VOL.KL_OPT, 0.0)` (118); `DYE(L,KC,MD) = DYE(L,KC,MD) - VOLTERM*DYESTEP` (120); `DYE(L,KC,MD) = max(DYE(L,KC,MD), 0.0)` (121); `DYESTEP = 0.0` (127). |
| 130–148 | 시작 시 9행 CALDYE 루틴, 33행 DO 루프, 130행 ELSEIF 분기(35행 IF 선택문) 안이다. 130행 ELSEIF는 같은 선택 분기군의 ITYPE=2 경로를 연다. 물의 나이(age of water)라는 주석의 0차 증가(zeroth-order growth)를 처리한다(131). DAGE=DELT/86400을 계산한다(132). 병렬 ND·K·젖은 셀 루프는 농도 변수 DYE에 일 단위 DAGE를 더한다(134–143). ITYPE 선택·MD 루프·루틴 종료와 반환을 포함한다(144–148). 원문: `elseif( DYES(MD).ITYPE == 2 )then` (130); `DAGE = DELT/86400.` (132); `do ND = 1,NDM` (135); `do K = 1,KC` (136); `do LP = 1,LLWET(K,ND)` (137); `L = LKWET(LP,K,ND)` (138); `DYE(L,K,MD) = DYE(L,K,MD) + DAGE` (139). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19·45–47·53·62·80: ND는 지역 정수다. 침강·온도 의존 처리의 LLWET 및 LKWET 참조 구간에는 ND 초기 대입이나 ND 루프가 없다. ND 루프는 95행, 112행, 135행에 있다.
- 45–47·54: TTHICK 계산 루프는 LP를 돌지만 LKWET에서 L을 얻는 대입이 없다. 해당 루프의 TTHICK·HPKI 인덱스는 L이다. 이 파일에서 첫 명시적 L 대입은 54행이다.
- 45–49·53–58: 표층 농도 갱신은 DYE(L,KC,MD)를 사용한다. 그 CLEFT 식의 두께 인덱스는 KC 대신 K이다. 해당 블록 앞의 K 루프는 1..KC이다.
- 88–91: KRATE1<0 분기의 식은 EXP(-KRATE1*DYESTEP)이며 주석은 Exponential decay이다. 반대 분기의 식은 1/(1+DYESTEP*KRATE1)이며 주석은 Growth rate이다.
- 33·73·127–128: DYESTEP은 모든 MD가 공유하는 SAVE 변수다. 동역학 처리를 수행한 ITYPE=1 입도의 분기 안에서 DYESTEP=0으로 재설정한다.
- 82·99·120–121: 온도 의존 및 독립 변화 뒤에는 농도 하한을 적용하는 대입이 없다. 휘발 처리 뒤에는 max(DYE,0.0) 대입이 있다.

