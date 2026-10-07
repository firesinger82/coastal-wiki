---
file: models/EFDC/raw/source_code/EFDC-GVC/csndeqc.for
lines: 156
sha256: daa64ee06f1e08ebced2c97cc6d49a9e295d654b0bf59298db72d2a199c2e541
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# csndeqc.for — 판독 구간 기록

구간은 1행부터 156행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | 구분 주석과 `REAL FUNCTION CSNDEQC(SNDDIA,SSG,WS,TAUR,TAUB,D50,SIGPHI,` (6); `&                SNDDMX,VDR,IOPT,ISNDAL)` (7) 선언. EFDC-FULL 1.0a·2001-11-01 수정 표기, 빈 변경 이력 양식(9–18), EFDC.PAR 포함(20). 비응집성 퇴적물(noncohesive sediment)의 바닥 부근 기준 농도(near-bed reference concentration) 계산 목적(22–23). SNDDIA=모래 입경, SSG=비중(specific gravity), WS=침강 속도(settling velocity), TAUR=물 밀도로 정규화한 임계 Shields 응력(critical Shields stress), TAUB=정규화한 바닥 응력(bed stress), SIGPHI=phi 크기 표준편차(standard deviation), SNDDMX=D90 또는 최대 입경의 주석(25–32). 옵션 1의 Garcia·Parker 1991 문헌(34–37). |
| 39–61 | 시작 시 6–7행 CSNDEQC 함수 안. `IF(IOPT.EQ.1)THEN` (39)에서 `IF(WS.EQ.0)THEN  ! DSI` (40)이면 반환값 0과 즉시 RETURN(41–43). 그 밖에 `REY=1.E6*SNDDIA*SQRT( 9.8*(SSG-1.)*SNDDIA )   !EQ 42` (44); `REY=REY**0.6                                  !SEE EQ 43` (45); `DFAC=1.` (46); `IF(ISNDAL.GE.1) DFAC=(SNDDIA/D50)**0.2        !SEE EQ 43` (47); `RLAM=1.-0.29*SIGPHI                           !EQ 51` (48); `USTAR=SQRT(TAUB)` (49); `VAL=DFAC*RLAM*REY*USTAR/WS                    !Z IN EQ 43` (50); `VAL=1.3E-7*(VAL**5)                           !TOP OF EQ 45` (51); `TMP=VAL/(1+3.33*VAL)                          !EQ 45` (52); `CSNDEQC=1.E6*SSG*TMP                          !CONVERT TO MASS CONC` (53). DFAC 기본값은 1이며 ISNDAL>=1에서 입경비를 적용한다. 질량 농도(mass concentration) 변환 주석은 반환식에 붙어 있다(53). USTAR<WS일 때 기준 농도 0, 소류사(bed load)는 SSEDTOX에서 처리한다는 주석(54–56). 실제 조건 `IF(USTAR.LT.WS) CSNDEQC=0.` (57). 진단 WRITE는 주석(58–59), ENDIF·구분 주석(60–61). |
| 62–80 | 시작 시 6–7행 CSNDEQC 함수 안. 옵션 2의 Smith·McLean 1977 문헌(62–65). `IF(IOPT.EQ.2)THEN` (67)에서 `VAL=2.4E-3*( (TAUB/TAUR)-1. )` (68); `VAL=MAX(VAL,0.)` (69); `TMP=0.65*VAL/(1.+VAL)` (70); `CSNDEQC=1.E6*SSG*TMP` (71). 응력 초과비에 2.4E-3을 곱한 VAL을 0 이상으로 제한한다. 소류사 관련 주석(72–74), `USTAR=SQRT(TAUB)` (75); `IF(USTAR.LT.WS) CSNDEQC=0.` (76). 진단 WRITE 주석·ENDIF·구분 주석(77–80). |
| 81–106 | 시작 시 6–7행 CSNDEQC 함수 안. 옵션 3의 Van Rijn 1984 문헌(81–84). `IF(IOPT.EQ.3)THEN` (86)에서 `REY=1.E4*SNDDIA*( (9.8*(SSG-1.))**0.333 )` (87); `IF(REY.LE.10.) TAURS=(4.*WS/REY)**2` (88); `IF(REY.GT.10.) TAURS=0.016*WS*WS` (89); `REY3=REY**0.3` (90); `VAL=(TAUB/TAURS)-1.` (91). 입력 TAUR를 사용하는 VAL 대체식은 주석 `C        VAL=(TAUB/TAUR)-1.` (92). 이어 `VAL=MAX(VAL,0.)` (93); `VAL=VAL**1.5` (94); `RATIO=SNDDIA/(3.*SNDDMX)` (95); `TMP=0.015*RATIO*VAL/REY3` (96); `CSNDEQC=1.E6*SSG*TMP` (97). 소류사 관련 주석(98–100), `USTAR=SQRT(TAUB)` (101); `IF(USTAR.LT.WS) CSNDEQC=0.` (102). 진단 WRITE 주석·ENDIF·구분 주석(103–106). |
| 107–129 | 시작 시 6–7행 CSNDEQC 함수 안. 옵션 4는 임계응력 없는 SEDFLUME 자료의 Hamrick 매개변수화라는 주석(107–109). `IF(IOPT.EQ.4)THEN` (111) 안 `IF(WS.EQ.0)THEN  ! DSI` (112)이면 반환값 0과 즉시 RETURN(113–115). 그 밖에 `REY=1.E4*SNDDIA*( (9.8*(SSG-1.))**0.333 )` (116); `TMPVAL=SQRT(TAUB)/WS` (117); `REY3=REY**1.333` (118); `TMPVAL=REY3*TMPVAL` (119); `VAL=(TMPVAL-1.0)**5.` (120); `VAL=4.E-9*VAL` (121); `CSNDEQC=1.E6*SSG*VAL/(1.+VDR)` (122). TMPVAL−1의 다섯 제곱과 4.E-9 계수·1.+VDR 분모를 사용한다. 소류사 관련 주석(123–125), `USTAR=SQRT(TAUB)` (126); `IF(USTAR.LT.WS) CSNDEQC=0.` (127). ENDIF·주석(128–129). |
| 130–156 | 시작 시 6–7행 CSNDEQC 함수 안. 옵션 5는 임계응력 포함 SEDFLUME 자료의 Hamrick 매개변수화라는 주석(130–132). `IF(IOPT.EQ.5)THEN` (134) 안 `IF(WS.EQ.0)THEN  ! DSI` (135)이면 반환값 0과 즉시 RETURN(136–138). 그 밖에 `REY=1.E4*SNDDIA*( (9.8*(SSG-1.))**0.333 )` (139); `TMPVAL=SQRT(TAUB)/WS` (140); `REY3=REY**1.333` (141); `TMPVAL=REY3*TMPVAL` (142); `VAL=0.0` (143); `IF(TMPVAL.GT.1.0) VAL=(TMPVAL-1.0)**5.` (144); `VAL=4.E-9*VAL` (145); `CSNDEQC=1.E6*SSG*VAL/(1.+VDR)` (146). VAL 기본값 0에서 TMPVAL>1.0일 때만 다섯 제곱을 대입한다. 소류사 관련 주석(147–149), `USTAR=SQRT(TAUB)` (150); `IF(USTAR.LT.WS) CSNDEQC=0.` (151). ENDIF·빈 줄, 미호출 FORMAT 600, RETURN·END(152–156). 외부 루틴 호출문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 39–155: 반환값 대입 경로는 IOPT=1..5이다. 그 밖의 옵션에 대한 기본 반환값 대입은 없다.
- 40–43·67–79·86–105·112–115·135–138: WS=0의 즉시 반환 검사는 옵션 1·4·5에 있다. 옵션 3은 WS를 사용하여 TAURS를 계산한 뒤 TAUB/TAURS를 계산하며 WS=0 검사는 없다. 옵션 2의 TAUB/TAUR 분모에도 별도 0 검사는 없다.
- 116–122·139–146: 옵션 4는 TMPVAL 값의 조건 없이 (TMPVAL-1.0)**5.를 계산한다. 옵션 5는 VAL=0.0으로 초기화하고 TMPVAL>1.0일 때만 해당 거듭제곱을 대입한다.
- 48–53: 옵션 1의 RLAM은 1.-0.29*SIGPHI이다. 이 파일에는 RLAM 또는 SIGPHI의 범위를 제한하는 조건문이 없다.
- 44·87·116·139: 입경 기반 계산은 중력가속도 계수 9.8을 실행식에 직접 사용한다.

