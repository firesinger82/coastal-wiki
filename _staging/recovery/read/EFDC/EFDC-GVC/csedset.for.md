---
file: models/EFDC/raw/source_code/EFDC-GVC/csedset.for
lines: 142
sha256: df79379c6f6527b9dbeeb0c83a95d0ab39502f2de25f7da1a6d54e6d9c9ef928
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# csedset.for — 판독 구간 기록

구간은 1행부터 142행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | 구분 주석과 `REAL FUNCTION CSEDSET(LINDEX,SED_LCL,SHEAR,IOPT)` (6) 선언. EFDC-FULL 1.0a·2001-11-01 수정 표기와 빈 변경 이력 양식(8–17). EFDC.PAR·EFDC.CMN 포함(19–20). 응집성 퇴적물(cohesive sediment)의 농도 의존 침강 속도(settling velocity) 계산 주석(22–23). IOPT=1 근거로 Hwang·Mehta 1989 문헌을 적는다(25–29). |
| 31–55 | 시작 시 6행 CSEDSET 함수 안. `IF(IOPT.EQ.1)THEN` (31)에서 `TMP=SED_LCL/2000.` (32); `TMP=LOG10(TMP)` (33); `TMP=-16.*TMP*TMP/9.` (34); `TMP=10.**TMP` (35); `CSEDSET=8.E-4*TMP` (36). 농도/2000의 상용로그를 제곱하고 −16/9 계수·10의 거듭제곱·8.E-4 계수를 적용한다. IOPT=2는 Shresta·Orlob 1996 문헌 주석(39–43). 농도 mg/L에서 g/L, 전단(shear) 1/s, 속도 m/hour에서 m/s 변환 주석(45–47). `IF(IOPT.EQ.2)THEN` (49)에서 `SED_LCL=1.E-3*SED_LCL` (50); `RNG=0.11075+0.0386*SHEAR` (51); `BG=EXP(-4.20706+0.1465*SHEAR)` (52); `WTMP=BG*( SED_LCL**RNG )` (53); `CSEDSET=WTMP/3600.` (54). 두 분기 종료·주석(37–38·55). |
| 56–79 | 시작 시 6행 CSEDSET 함수 안. IOPT=3의 Ziegler·Nesbit 1995 문헌 표기(57–61). 농도 mg/L를 g/cm³로 1.E-6 배, 운동학적 전단응력(kinematic shear stress)을 dy/cm²로 1.E4 배, cm/s를 m/s로 0.01 배라는 주석(63–67). `IF(IOPT.EQ.3)THEN` (69)에서 `SED_LCL=1.E-6*SED_LCL` (70); `GG=1.E4*SHEAR` (71); `CG=GG*SED_LCL` (72); `CG=MAX(CG,7.51E-6)` (73); `BD2=-0.4-0.25*LOG10(CG-7.5E-6)` (74); `CON=9.6E-4*( (1.E-8)**BD2 )` (75); `VAL=CG**(-0.85-BD2)` (76); `CSEDSET=0.01*CON*VAL` (77). CG를 7.51E-6 이상으로 제한하고 LOG10(CG−7.5E-6)을 사용한다. ENDIF·주석(78–79). |
| 80–101 | 시작 시 6행 CSEDSET 함수 안. IOPT=4 표제 뒤 `IF(IOPT.EQ.4)THEN` (82)에서 `GG=1.E4*SHEAR` (83); `TMP=GG*SED_LCL` (84); `CSEDSET=8.E-5` (85), `IF(TMP.LT.40.0) CSEDSET=1.51E-5*(TMP**0.45)` (86), `IF(TMP.GT.400.0) CSEDSET=0.893E-6*(TMP**0.75)` (87). TMP=40..400에서는 앞서 지정한 8.E-5가 남는다. IOPT=5 표제(90–91), `IF(IOPT.EQ.5)THEN` (92), 내부 `IF(SED_LCL.LE.SED_CRIT) THEN` (93)이면 `CSEDSET = CONSTWS1/86400.` (94), ELSE(95)는 `CSEDSET = ((SED_CRIT*CONSTWS1) +` (96); `+           (CONSTWS2*(SED_LCL-SED_CRIT)))/SED_LCL` (97); `CSEDSET = CSEDSET/86400.` (98). 후자 식은 SED_CRIT 경계의 CONSTWS1 부분과 초과 농도의 CONSTWS2 부분을 농도로 나눈다. 두 옵션의 분기 종료·주석(88–89·99–101). |
| 102–117 | 시작 시 6행 CSEDSET 함수 안. IOPT=6 표제·`IF(IOPT.EQ.6)THEN` (104)에서 `GG=1.E4*SHEAR` (105); `TMP=GG*SED_LCL` (106); `IF(TMP.LT.100.0) CSEDSET=2.*1.16E-5*(TMP**0.5)` (107); `IF(TMP.GE.100.0) CSEDSET=2.*1.84E-5*(TMP**0.4)` (108). TMP=100에서 두 번째 식을 적용한다. IOPT=7 표제·`IF(IOPT.EQ.7)THEN` (113)에서 `TMP=SHEAR*SED_LCL` (114); `CSEDSET=0.0052*(TMP**0.470138)` (115). 분기 종료·주석(109–112·116–117). |
| 118–142 | 시작 시 6행 CSEDSET 함수 안. IOPT=8을 이전 IOPT=5의 변형이라고 적는 주석(118). 원래 옵션 5 식은 `cjhorig      IF(IOPT.EQ.5)THEN` (120); `cjhorig        GG=1.E4*SHEAR` (121); `cjhorig        TMP=GG*SED` (122); `cjhorig        CSEDSET=3.82E-5*(TMP**0.12)` (123)로 주석 처리되었다. 주석은 수정 옵션 5의 m/day를 m/s로 86400으로 나누며 두 함수의 교점을 3.8로 적는다(126–129). 실행 조건은 `IF(IOPT.EQ.8)THEN` (130)이며 `GG=1.E4*SHEAR` (131); `TMP=GG*SED_LCL             ! TMP=C*tau` (132). 내부 `IF(TMP .LT. 3.8 ) THEN` (133)이면 `CSEDSET = (1.270*(TMP**0.79))/86400. ! 12/31/03 new WP regr` (134), ELSE(135)는 `CSEDSET = (3.024*(TMP**0.14))/86400. ! 12/31/03 Burban&Lick` (136). 각 ENDIF(137–138), 주석·빈 줄·RETURN·END(139–142). 호출문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·31–138: LINDEX는 함수 인수 목록에만 등장한다. 본문의 실행식은 LINDEX를 참조하지 않는다.
- 49–50·69–70: IOPT=2와 IOPT=3은 입력 인수 SED_LCL 자체를 각각 1.E-3배와 1.E-6배로 다시 대입한다.
- 31–33: IOPT=1은 SED_LCL/2000.을 LOG10에 전달한다. 이 분기에는 해당 값이 양수인지 검사하는 조건이 없다.
- 31–138: 반환값 대입 경로는 IOPT=1..8이다. 그 밖의 IOPT에 대한 기본 반환값 대입은 없다.
- 126–130: 수정식 바로 앞 주석은 IOPT=5라고 적는다. 그 수정식의 실행 조건은 IOPT=8이다.

