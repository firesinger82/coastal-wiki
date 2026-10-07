---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Utilities/mod_convertwgs84.f90
lines: 149
sha256: 981f05a2e0ba0030adf7bb17179a0d454d89de734137eed9911041f3573671b0
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_convertwgs84.f90 — 판독 구간 기록

구간은 1행부터 149행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | EFDC+·GPLv2 머리말(1–8). CONVERTWGS84는 지리 좌표와 UTM(Universal Transverse Mercator)을 변환한다는 주석이다(9–13). GLOBAL의 RKD·PI·HEMI·UTMZ 사용(15), implicit none(17). 주석 범위는 HEMI=1 북반구·2 남반구, UTMZ=1:60이다(19–20). 좌표계 기본값은 `character(20):: GEOSYS = '1.WGS84/NAD83'` (24). 장·단반경, 중앙자오선 축척(scale), x/y 오프셋(offset), 중앙자오선·편평률(flattening)·이심률(eccentricity) 관련 변수 선언과 contains·빈 줄(25–34). |
| 35–64 | UTMPARS 입구(35–36). `if( HEMI==1 )then` (38)은 `FN = 0` (39), `elseif(HEMI==2 )then` (40)은 `FN = 1.D7` (41). 조건 밖에서 `FE = 500000._RKD` (44), `SCLF = 0.9996_RKD` (45). `if( GEOSYS(1:1)=='1' )then` (47)은 `R_MJR = 6378137._RKD` (48), `FLA  = 1._RKD/298.257223563_RKD` (49). `elseif(GEOSYS(1:1)=='2' )then` (50)은 `R_MJR = 6378137._RKD` (51), `FLA  = 1._RKD/298.257222101_RKD` (52). `elseif(GEOSYS(1:1)=='3' )then` (53)은 `R_MJR = 6378135._RKD` (54), `FLA  = 1._RKD/298.26_RKD` (55). 조건 밖에서 `E2 = 2*FLA-FLA**2` (58), `EP2 = E2/(1-E2)` (59), `R_MNR = R_MJR*SQRT(1-E2)` (60), `LAM0 = 6*(UTMZ-30)-3    !CENTRAL MERIDIAN IN DEGREE` (61). 루틴 종료·빈 줄(63–64). |
| 65–86 | UTM_WGS84 입구·입출력 단위 주석(65–72). LON/LAT 배열은 십진 도(decimal degree), XUTM/YUTM 배열은 m이다. 인수와 SIZE(LON) 작업 배열 선언(74–77). 원문은 `L0  = PI*LAM0/180` (79), `LAM = PI*LON/180` (80), `PHI = PI*LAT/180` (81), `DLAM= LAM-L0` (82), `RN = R_MJR/SQRT(1-E2*SIN(PHI)**2)` (84), `F2 = (R_MJR-R_MNR)/(R_MJR+R_MNR)` (85). |
| 87–106 | 시작 시 65행 UTM_WGS84 루틴 안. 계수 원문은 `AP = R_MJR*(1-F2+(5._RKD/4)*(F2**2-F2**3)+(81._RKD/64)*(F2**4-F2**5))` (87), `BP = (3._RKD/2)*R_MJR*F2*(1-F2+(7._RKD/8)*(F2**2-F2**3)+(55._RKD/64)*(F2**4-F2**5))` (88), `CP = (15._RKD/16)*R_MJR*F2**2*(1-F2+(3._RKD/4)*(F2**2-F2**3))` (89), `DP = (35._RKD/48)*R_MJR*F2**3*(1-F2+(11._RKD/16)*(F2**2-F2**3))` (90), `EP = (315._RKD/51)*(R_MJR*F2**4)*(1-F2)` (91). 이어 `LEN1 = AP*PHI-BP*SIN(2*PHI)+CP*SIN(4*PHI)-DP*SIN(6*PHI)+EP*SIN(8*PHI)` (92), `ETA2 = EP2*COS(PHI)**2` (93), `TAPH = TAN(PHI)**2` (94), `A2 = RN/2*SIN(PHI)*COS(PHI)` (95), `A4 = RN/24*SIN(PHI)*COS(PHI)**3*(5-TAPH+9*ETA2+4*ETA2**2)` (96), `A6 = RN/720*SIN(PHI)*COS(PHI)**5*(61-58*TAPH+TAPH**2+270*ETA2-330*ETA2*TAPH)` (97), `B1 = RN*COS(PHI)` (98), `B3 = RN/6*COS(PHI)**3*(1-TAPH+ETA2)` (99), `B5 = RN/120*COS(PHI)**5*(5-18*TAPH+TAPH**2+14*ETA2-58*ETA2*TAPH+13*ETA2**2-64*ETA2**2*TAPH)` (100). 출력식은 `YUTM = SCLF*(LEN1+A2*DLAM**2+A4*DLAM**4+A6*DLAM**6)+FN` (102), `XUTM = SCLF*(B1*DLAM+B3*DLAM**3+B5*DLAM**5)+FE` (103). 루틴 종료·빈 줄(105–106). |
| 107–133 | UTMR_WGS84는 m 단위 XUTM/YUTM을 십진 도 LON/LAT로 역변환한다(107–113). 인수·SIZE(XUTM) 작업 배열 선언(115–118). `L0  = PI*LAM0/180` (120), `RM  = YUTM/SCLF` (121), `MU = RM/(R_MJR*(1-E2/4-3*E2**2/64 - 5*E2**3/256))` (122), `E1 = (1-SQRT(1-E2))/(1+SQRT(1-E2))` (124), `J1 = 3*E1/2 - 27*E1**3/32` (125), `J2 = 21*E1**2/16 - 55*E1**4/32` (126), `J3 = 151*E1**3/96` (127), `J4 = 1097*E1**4/512` (128), `BX = MU+J1*SIN(2*MU)+J2*SIN(4*MU)+J3*SIN(6*MU)+J4*SIN(8*MU)` (129), `ETAX2 = EP2*COS(BX)**2` (130), `VX2 = 1+ETAX2` (131), `NX  = R_MJR/SQRT(1-E2*SIN(BX)**2)` (132), `TX  = TAN(BX)` (133). |
| 134–149 | 시작 시 107행 UTMR_WGS84 루틴 안. `A2  = -VX2*TX/(2*NX**2)` (134), `A4  = -A2/(12*NX**2)*(5+3*TX**2+ETAX2-9*ETAX2*TX**2-4*ETAX2**2)` (135), `A6  = -A2/(360*NX**4)*(61-90*TX**2+45*TX**4-46*ETAX2)` (136), `B1 = 1/(NX*COS(BX))` (138), `B3  = -B1/(6*NX**2)*(1+2*TX**2+ETAX2)` (139), `B5  = -B1/(120*NX**4)*(5+28*TX**2+24*TX**4+6*ETAX2+8*ETAX2*TX**2)` (140), `Y   = (XUTM-FE)/SCLF` (141), `LAT = BX+A2*Y**2+A4*Y**4+A6*Y**6` (142), `LON = B1*Y+B3*Y**3+B5*Y**5 +L0` (143), `LAT = LAT*180/PI ! TO DEGREE` (144), `LON = LON*180/PI ! TO DEGREE` (145). 루틴·모듈 종료·빈 줄(146–149). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 38–42·47–56: HEMI 조건과 GEOSYS 조건에는 최종 else가 없다. FN·R_MJR·FLA의 모듈 선언에는 초기값이 없다(25·29·31).
- 35–63·65–147: 두 변환 루틴은 UTMPARS에서 설정하는 모듈 변수를 사용한다. 두 변환 루틴 내부에는 UTMPARS 호출이 없다.
- 91: 정변환의 EP 계수에는 315._RKD/51이 적혀 있다.
- 41·102·121·141: 정변환은 YUTM에 FN을 더한다. 역변환의 RM은 YUTM/SCLF이며 FN을 빼는 항이 없다. 역변환의 x 오프셋 식에는 XUTM-FE가 있다.
