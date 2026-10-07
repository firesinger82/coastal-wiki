---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-Original/csndeqc.f90
lines: 133
sha256: 712b26eaa922591d1f32191fef2dd0f5d5dac9153ceef8f317e0713926fc4660
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# csndeqc.f90 — 판독 구간 기록

구간은 1행부터 133행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | EFDC+·저작권·GPLv2 머리말(1–8). CSNDEQC 함수 입구(9). 비점착성 퇴적물(noncohesive sediment)의 바닥 부근 참조농도(reference concentration)를 계산한다는 주석(11). 2011년 WS<=0 처리와 USTAR<WS일 때 0 설정 이력을 적는다(16–19). 입경·비중(specific gravity)·침강속도(settling velocity)·밀도 정규화 전단응력·phi 표준편차(standard deviation)·SNDDMX의 설명을 포함한다(21–28). 인수와 지역변수 선언 후 USTAR=SQRT(TAUB)를 계산한다(31–36). 조건·계산·호출 원문: `USTAR = SQRT(TAUB)` (36). |
| 38–60 | 시작 시 9행 CSNDEQC 안. USTAR<WS이면 반환농도는 0이다(38–39). 그 조건 불성립 시 IOPT=1의 병렬 elseif는 Garcia–Parker 1991을 적는다(41–45). WS>0이면 입자 Reynolds 수(Reynolds number)를 0.6승으로 바꾸고 DFAC=1을 설정한다(47–50). ISNDAL>=1이면 입경/D50의 0.2승으로 DFAC를 덮어쓴다(51). SIGPHI 기반 RLAM, USTAR/WS, 5승, 포화식(saturation expression), 1.E6*SSG 질량농도 변환을 계산한다(52–56). WS 분기의 else는 0을 반환한다(57–59). 조건·계산·호출 원문: `if( USTAR < WS )then` (38); `elseif( IOPT == 1 )then` (41); `if( WS > 0. )then` (47); `REY = 1.E6*SNDDIA*SQRT( 9.8*(SSG-1.)*SNDDIA )   !EQ 42` (48); `REY = REY**0.6                                  !SEE EQ 43` (49); `DFAC = 1.` (50); `if( ISNDAL >= 1) DFAC = (SNDDIA/D50)**0.2       !SEE EQ 43` (51); `RLAM = 1.-0.29*SIGPHI                           !EQ 51` (52); `VAL = DFAC*RLAM*REY*USTAR/WS                    !Z IN EQ 43` (53); `VAL = 1.3E-7*(VAL**5)                           !TOP OF EQ 45` (54); `TMP = VAL/(1+3.33*VAL)                          !EQ 45` (55); `CSNDEQC = 1.E6*SSG*TMP                          !CONVERT TO MASS CONC` (56); `else` (57). |
| 61–92 | 시작 시 9행 CSNDEQC·38행 조건 선택 블록 안. IOPT=2는 Smith–McLean 1977을 적고 TAUB/TAUR 기반 초과응력을 비음수로 제한해 농도를 계산한다(61–70). IOPT=3은 van Rijn 1984를 적는다(72–76). WS>0인 경우 REY<=10 또는 >10에 따라 TAURS를 구한다(78–81). 81행 주석은 2021년 계수를 0.016에서 0.16으로 수정했다고 적는다. 초과응력을 비음수 제한·1.5승으로 바꾼 뒤 SNDDIA/(3.*SNDDMX)와 REY3으로 농도를 계산한다(82–88). WS 분기의 else는 0을 반환한다(89–91). 조건·계산·호출 원문: `elseif( IOPT == 2 )then` (61); `VAL = 2.4E-3*( (TAUB/TAUR)-1. )` (67); `VAL = max(VAL,0.)` (68); `TMP = 0.65*VAL/(1.+VAL)` (69); `CSNDEQC = 1.E6*SSG*TMP` (70); `elseif( IOPT == 3 )then` (72); `if( WS > 0. )then` (78); `REY = 1.E4*SNDDIA*( (9.8*(SSG-1.))**0.333 )` (79); `if( REY <= 10. ) TAURS = (4.*WS/REY)**2` (80); `if( REY  > 10. ) TAURS = 0.16*WS*WS                      ! *** Corrected 2021-06 from 0.016.  0.16 = 0.4^2 from VanRijn 1984` (81); `REY3 = REY**0.3` (82); `VAL = (TAUB/TAURS)-1.` (83); `VAL = max(VAL,0.)` (84); `VAL = VAL**1.5` (85); `RATIO = SNDDIA/(3.*SNDDMX)` (86); `TMP = 0.015*RATIO*VAL/REY3` (87); `CSNDEQC = 1.E6*SSG*TMP` (88); `else` (89). |
| 93–109 | 시작 시 9행 CSNDEQC·38행 조건 선택 블록 안. IOPT=4는 임계응력(critical stress)이 없는 Hamrick SEDFLUME 매개변수화(parameterization)라는 주석(93–97). WS>0이면 REY·SQRT(TAUB)/WS·REY의 1.333승을 사용한다(98–102). TMPVAL-1.0의 5승에 4.E-9를 곱하고 공극비(void ratio) 1.+VDR로 나누어 농도를 계산한다(103–105). WS 분기의 else는 0을 반환한다(106–108). 조건·계산·호출 원문: `elseif( IOPT == 4 )then` (93); `if( WS > 0. )then` (98); `REY = 1.E4*SNDDIA*( (9.8*(SSG-1.))**0.333 )` (99); `TMPVAL = SQRT(TAUB)/WS` (100); `REY3 = REY**1.333` (101); `TMPVAL = REY3*TMPVAL` (102); `VAL = (TMPVAL-1.0)**5.` (103); `VAL = 4.E-9*VAL` (104); `CSNDEQC = 1.E6*SSG*VAL/(1.+VDR)` (105); `else` (106). |
| 110–133 | 시작 시 9행 CSNDEQC·38행 조건 선택 블록 안. IOPT=5는 임계응력을 사용하는 Hamrick SEDFLUME 옵션이다(110–113). WS>0이면 옵션 4와 같은 REY·TMPVAL을 계산하되 VAL=0으로 초기화하고 TMPVAL>1.0인 경우만 5승을 적용한다(114–122). WS 분기의 else는 0을 반환한다(123–125). 바깥 else는 잘못된 옵션으로 STOPP를 호출한다(126–129). return·END·마지막 빈 줄을 포함한다(131–133). 조건·계산·호출 원문: `elseif( IOPT == 5 )then` (110); `if( WS > 0. )then` (114); `REY = 1.E4*SNDDIA*( (9.8*(SSG-1.))**0.333 )` (115); `TMPVAL = SQRT(TAUB)/WS` (116); `REY3 = REY**1.333` (117); `TMPVAL = REY3*TMPVAL` (118); `if( TMPVAL > 1.0 ) VAL = (TMPVAL-1.0)**5.` (120); `VAL = 4.E-9*VAL` (121); `CSNDEQC = 1.E6*SSG*VAL/(1.+VDR)` (122); `else` (123); `else` (126); `call STOPP('BAD CSNDEQC OPTION')` (128). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 36–38: USTAR=SQRT(TAUB)는 옵션과 WS 검사를 하기 전에 실행된다. 이 함수에는 음수 TAUB를 제한하는 조건이 없다.
- 41–59: 옵션 1의 RLAM=1.-0.29*SIGPHI에는 비음수 제한이 없다. 이 값은 VAL의 5승을 계산하는 식에 사용된다.
- 67·80–87: 옵션 2는 TAUR로 나눈다. 옵션 3은 REY·TAURS·SNDDMX·REY3로 나눈다. 이 분모가 0인지 확인하는 조건은 해당 분기들에 없다.
- 103–105·119–122: 옵션 4는 (TMPVAL-1.0)**5.를 조건 없이 계산한다. 옵션 5는 VAL=0.0으로 시작하고 TMPVAL>1.0일 때만 같은 거듭제곱을 계산한다.

