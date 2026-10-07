---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-Original/csedset.f90
lines: 133
sha256: 33b59e3d33b691249d5eeffb68aae13f1ffed2db4b43d9f5e4c5c71f02a34726
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# csedset.f90 — 판독 구간 기록

구간은 1행부터 133행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | EFDC+·저작권·GPLv2 머리말(1–8). CSEDSET(SED,SHEAR,IOPT) 입구(9). 점착성 퇴적물(cohesive sediment)의 농도 의존 침강속도(settling velocity)를 m/s로 계산한다는 주석(11–12). 2015년 Shrestha–Orlob 식 갱신 이력을 적는다(14–19). SED·SHEAR·IOPT는 intent(IN)이다(23–24). SED<=0.0001이면 CSEDSET=0과 return으로 종료한다(27–30). 조건·계산·호출 원문: `if( SED <= 0.0001 )then` (27). |
| 32–44 | 시작 시 9행 CSEDSET 안. Hwang–Mehta 1989를 출처로 적는 IOPT=1 분기이다(32–37). SED/2000., LOG10, -16/9 계수, 10의 거듭제곱, 8.E-4 계수를 순서대로 사용한다(38–42). 분기 종료와 빈 줄을 포함한다(43–44). 조건·계산·호출 원문: `if( IOPT == 1 )then` (37); `TMPSED = SED/2000.` (38); `TMP = LOG10(TMPSED)` (39); `TMP = -16.*TMP*TMP/9.` (40); `TMP = 10.**TMP` (41); `CSEDSET = 8.E-4*TMP` (42). |
| 45–64 | 시작 시 9행 CSEDSET 안. Shrestha–Orlob 1996을 출처로 적는 IOPT=2 분기이다(45–50). 2015년 폐기된 식은 주석 처리되어 있다(51–55). 수정된 Mehta 식은 농도에 1.E-3을 곱하고, SHEAR 선형식으로 RNG·BG를 구한 뒤 WTMP/3600.을 반환한다(57–63). 조건·계산·호출 원문: `if( IOPT == 2 )then` (50); `!SED = (SED/2.65E-6)**(1/3)` (52); `!BG = 0.03*SHEAR**(-0.5)` (53); `!WTMP = SED*BG` (54); `!CSEDSET = WTMP/3600.` (55); `TMPSED  = 1.E-3*SED` (58); `RNG     = 1.11075 + 0.0386*SHEAR` (59); `BG      = EXP( -4.20706 + 0.1465*SHEAR )` (60); `WTMP    = BG*TMPSED**RNG` (61); `CSEDSET = WTMP/3600.` (62). |
| 65–80 | 시작 시 9행 CSEDSET 안. Ziegler–Nesbit 1995를 출처로 적는 IOPT=3 분기이다(65–70). 주석은 SED의 g/m³를 g/cm³로, SHEAR의 m²/s²를 cm²/s²로 바꾼다고 적는다(71–73). CG는 7.51E-6 이상으로 제한한다(74). LOG10(CG-7.5E-6), 1.E-8의 BD2승, CG의 거듭제곱으로 m/s 값을 구한다(75–78). 조건·계산·호출 원문: `if( IOPT == 3 )then` (70); `TMPSED  = 1.E-6*SED        ! *** CONVERT G/M^3 TO G/CM^3` (71); `GG      = 1.E4*SHEAR       ! *** CONVERT FROM M^2/S^2 TO CM^2/S^2` (72); `CG      = GG*TMPSED        ! *** G/CM/S^2 = G/CM^3 * CM^2/S^2` (73); `CG      = max(CG,7.51E-6)` (74); `BD2     = -0.4 - 0.25*LOG10(CG - 7.5E-6)` (75); `CON     = 9.6E-4*(1.E-8)**BD2` (76); `VAL     = CG**(-0.85-BD2)` (77); `CSEDSET = 0.01*CON*VAL` (78). |
| 81–102 | 시작 시 9행 CSEDSET 안. IOPT=4는 GG*SED를 TMPSED로 계산하고 기본 침강속도 8.E-5를 설정한다(82–85). TMPSED<40 또는 >400일 때 각각 별도 거듭제곱 식으로 덮어쓴다(86–87). IOPT=5는 Housatonic River 주석과 하루에서 초로 바꾸는 /86400.을 사용한다(90–101). TMPSED<3.8이면 0.79승, else이면 0.14승을 사용한다(96–100). 두 옵션은 서로 독립된 if 블록이다. 조건·계산·호출 원문: `if( IOPT == 4 )then` (82); `GG      = 1.E4*SHEAR       ! *** CONVERT FROM M^2/S^2 TO CM^2/S^2` (83); `TMPSED  = GG*SED` (84); `CSEDSET = 8.E-5` (85); `if( TMPSED < 40.0  ) CSEDSET = 1.510E-5*(TMPSED**0.45)` (86); `if( TMPSED > 400.0 ) CSEDSET = 0.893E-6*(TMPSED**0.75)` (87); `if( IOPT == 5 )then` (93); `GG      = 1.E4*SHEAR       ! *** CONVERT FROM M^2/S^2 TO CM^2/S^2` (94); `TMPSED  = GG*SED` (95); `if( TMPSED < 3.8 )then` (96); `CSEDSET = (1.270*(TMPSED**0.79))/86400. ! 12/31/03 new WP regr` (97); `else` (98); `CSEDSET = (3.024*(TMPSED**0.14))/86400. ! 12/31/03 Burban&Lick` (99). |
| 103–119 | 시작 시 9행 CSEDSET 안. IOPT=6은 GG*SED를 TMPSED로 계산한다(104–106). TMPSED<100이면 2.*1.16E-5와 0.5승, else이면 2.*1.84E-5와 0.4승을 사용한다(107–112). IOPT=7은 SHEAR*SED에 0.0052와 0.470138승을 사용한다(115–118). 두 옵션은 독립된 if 블록이다. 조건·계산·호출 원문: `if( IOPT == 6 )then` (104); `GG      = 1.E4*SHEAR       ! *** CONVERT FROM M^2/S^2 TO CM^2/S^2` (105); `TMPSED  = GG*SED` (106); `if( TMPSED <  100.0 )then` (107); `CSEDSET = 2.*1.16E-5*(TMPSED**0.5)` (108); `else` (109); `CSEDSET = 2.*1.84E-5*(TMPSED**0.4)` (110); `if( IOPT == 7 )then` (115); `TMPSED  = SHEAR*SED` (116); `CSEDSET = 0.0052*(TMPSED**0.470138)` (117). |
| 120–133 | 시작 시 9행 CSEDSET 안. Christopher Hall의 2015년 수정 Shrestha 주석(120). IOPT=8은 SED에 1.E-3을 곱해 g/L로 바꾼다(121–122). SHEAR>0.1이면 BG=0.06/SQRT(SHEAR), else이면 BG=0.1이다(123–127). TMPSED/2650의 1./3.승으로 침강속도를 계산한다(128). 분기 종료·return·END·마지막 빈 줄을 포함한다(129–133). 조건·계산·호출 원문: `if( IOPT == 8 )then` (121); `TMPSED = 1.E-3*SED        ! *** CONVERT G/M^3 TO G/L` (122); `if( SHEAR > 0.1 )then` (123); `BG = 0.06/SQRT(SHEAR)` (124); `else` (125); `BG = 0.1` (126); `CSEDSET = BG*(TMPSED/2650)**(1./3.)` (128). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–30·37–129: SED<=0.0001은 항상 0을 반환한다. 이 조건을 통과한 IOPT 중 1..8 밖의 값을 처리하는 기본값 대입은 없다.
- 74–75: CG의 하한은 7.51E-6이다. 바로 다음 LOG10 식은 CG에서 7.5E-6을 뺀다.
- 85–87: 옵션 4의 기본값 8.E-5는 TMPSED=40과 TMPSED=400에서도 유지된다. 두 덮어쓰기 조건은 엄격한 <와 >이다.
- 83–117: 옵션 4..7에는 SHEAR 또는 TMPSED의 비음수 제한 조건이 없다. 옵션 4..7의 실행식에는 TMPSED의 비정수 거듭제곱이 있다.

