---
file: models/EFDC/raw/source_code/EFDC-GVC/calbuoy.for
lines: 221
sha256: 10e7cb837873150511e2c624af14b0dbeb1e20dd94b1035a13c08eb05f23cc7d
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calbuoy.for — 판독 구간 기록

구간은 1행부터 221행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | 구분 주석과 `SUBROUTINE CALBUOY` 입구(1–6). EFDC-FULL 1.0a, John Hamrick의 2001-11-01 수정, 변경 기록 틀(8–17). 부력(buoyancy)은 UNESCO 상태방정식(equation of state)의 Mellor 근사를 쓴다는 주석과 논문 정보 J. Atmos. Oceanic Technol. 8, p.609(19–21). `INCLUDE 'EFDC.PAR'` (25), `INCLUDE 'EFDC.CMN'` (26), 구분 주석(27–29). 포함 파일 내부는 이 판독 대상이 아니다. |
| 30–41 | 시작 시 6행 CALBUOY 안. `IF(IBSC.EQ.1) GOTO 1000` (30)은 염분(salinity)만 사용하는 선형 진단 경로로 이동. 이동하지 않으면 `ISPCOR=0` (32). 기준 밀도(reference density)는 압력 P=0·염분 S=0·수온 T=TEMO라는 주석(34). 식은 `RHOO=999.842594+6.793952E-2*TEMO-9.095290E-3*TEMO*TEMO` (36), 연속행 `&    +1.001685E-4*TEMO*TEMO*TEMO-1.120083E-6*TEMO*TEMO*TEMO*TEMO` (37), `&    +6.536332E-9*TEMO*TEMO*TEMO*TEMO*TEMO` (38). B를 P=0에서의 밀도로 계산한다는 주석(40). |
| 42–51 | 시작 시 6행 CALBUOY 안. `IF(ISTRAN(1).EQ.0.AND.ISTRAN(2).EQ.0)THEN` (42)에서는 K=1..KC·L=2..LA 순회(44–45). 모든 B(L,K)에 RHOO를 복사(46), 루프·조건 종료(47–50), 주석(51). |
| 52–67 | 시작 시 6행 CALBUOY 안. `IF(ISTRAN(1).GE.1.AND.ISTRAN(2).EQ.0)THEN` (52)은 염분만 수송하는 경로. K=1..KC·L=2..LA(54–55)에서 `SAL(L,K)=MAX(SAL(L,K),0.)` (56)으로 염분 하한을 0으로 설정. SSTMP=SAL·TTMP=TEMO 복사(57–58). `B(L,K)=RHOO+SSTMP*(0.824493-4.0899E-3*TTMP+7.6438E-5*TTMP*TTMP` (59), `&   -8.2467E-7*TTMP*TTMP*TTMP+5.3875E-9*TTMP*TTMP*TTMP*TTMP)` (60), `&   +SQRT(SSTMP)*SSTMP*(-5.72466E-3+1.0227E-4*TTMP` (61), `&   -1.6546E-6*TTMP*TTMP)+4.8314E-4*SSTMP*SSTMP` (62)로 밀도 계산. 루프·조건 종료(63–66). |
| 68–80 | 시작 시 6행 CALBUOY 안. `IF(ISTRAN(1).EQ.0.AND.ISTRAN(2).GE.1)THEN` (68)은 수온만 수송하는 경로. K=1..KC·L=2..LA(70–71)에서 TTMP=TEM 복사(72). `B(L,K)=999.842594+6.793952E-2*TTMP-9.095290E-3*TTMP*TTMP` (73), `&    +1.001685E-4*TTMP*TTMP*TTMP-1.120083E-6*TTMP*TTMP*TTMP*TTMP` (74), `&    +6.536332E-9*TTMP*TTMP*TTMP*TTMP*TTMP` (75). 루프·조건 종료(76–79), 주석(80). |
| 81–99 | 시작 시 6행 CALBUOY 안. `IF(ISTRAN(1).GE.1.AND.ISTRAN(2).GE.1)THEN` (81)은 염분·수온 수송 경로. K=1..KC·L=2..LA(83–84)에서 `SAL(L,K)=MAX(SAL(L,K),0.)` (85), SSTMP=SAL·TTMP=TEM 복사(86–87). 담수 밀도(freshwater density)는 `RHTMP=999.842594+6.793952E-2*TTMP-9.095290E-3*TTMP*TTMP` (88), `&    +1.001685E-4*TTMP*TTMP*TTMP-1.120083E-6*TTMP*TTMP*TTMP*TTMP` (89), `&    +6.536332E-9*TTMP*TTMP*TTMP*TTMP*TTMP` (90). 염분 보정은 `B(L,K)=RHTMP+SSTMP*(0.824493-4.0899E-3*TTMP+7.6438E-5*TTMP*TTMP` (91), `&   -8.2467E-7*TTMP*TTMP*TTMP+5.3875E-9*TTMP*TTMP*TTMP*TTMP)` (92), `&   +SQRT(SSTMP)*SSTMP*(-5.72466E-3+1.0227E-4*TTMP` (93), `&   -1.6546E-6*TTMP*TTMP)+4.8314E-4*SSTMP*SSTMP` (94). 루프·조건 종료(95–98). |
| 100–115 | 시작 시 6행 CALBUOY 안. Mellor 압력 보정(pressure correction) 주석(100). `IF(ISPCOR.EQ.1)THEN` (102)의 K=1..KC·L=2..LA(104–105)에서 `PRES=RHOO*G*HP(L)*(1.-ZZ(K))*1.E-6` (106), `CCON=1449.2+1.34*(SAL(L,K)-35.)+4.55*TEM(L,K)` (107)와 `&    -0.045*TEM(L,K)*TEM(L,K)+0.00821*PRES+15.E-9*PRES*PRES` (108), `TMP=PRES/(CCON*CCON)` (109), `B(L,K)=B(L,K)+1.E+4*TMP*(1.-0.2*TMP)` (110). 루프·조건 종료(111–114). |
| 116–136 | 시작 시 6행 CALBUOY 안. 밀도를 부력으로 바꾼다는 주석(116). K=1..KC·L=2..LA에서 `B(L,K)=(B(L,K)/RHOO)-1.` (120), 루프 종료(121–122). 낮은 퇴적물 농도(sediment concentration) 보정 주석(124). `IF(ISTRAN(6).GE.1.OR.ISTRAN(7).GE.1)THEN` (126)은 K=1..KC·L=2..LA의 TVAR1S·TVAR1W를 0으로 초기화(128–133), 조건 종료(135). |
| 137–162 | 시작 시 6행 CALBUOY 안. `IF(ISTRAN(6).GE.1)THEN` (137)의 NS=1..NSED·K=1..KC·L=2..LA 루프(139–141)에서 `TVAR1S(L,K)=TVAR1S(L,K)+SDEN(NS)*SED(L,K,NS)` (142), `TVAR1W(L,K)=TVAR1W(L,K)+(SSG(NS)-1.)*SDEN(NS)*SED(L,K,NS)` (143). 루프·조건 종료(144–148). 150–161행은 실행되지 않는 이전 보정 블록이다. 그 주석 식은 `C        B(L,K)=B(L,K)*(1.-SDEN(NS)*SED(L,K,NS))` (155)와 `C     &        +(SSG(NS)-1.)*SDEN(NS)*SED(L,K,NS)` (156). 주석 원문(실행하지 않음): `C      IF(ISTRAN(6).GE.1)THEN` (150). |
| 163–190 | 시작 시 6행 CALBUOY 안. `IF(ISTRAN(7).GE.1)THEN` (163)의 NN=1..NSND에서 `NS=NN+NSED` (166), K=1..KC·L=2..LA 순회(167–168). `TVAR1S(L,K)=TVAR1S(L,K)+SDEN(NS)*SND(L,K,NN)` (169), `TVAR1W(L,K)=TVAR1W(L,K)+(SSG(NS)-1.)*SDEN(NS)*SND(L,K,NN)` (170). 루프·조건 종료(171–175). 177–189행은 실행되지 않는 이전 보정 블록이다. 주석 식은 `C        B(L,K)=B(L,K)*(1.-SDEN(NS)*SND(L,K,NN))` (183)와 `C     &        +(SSG(NS)-1.)*SDEN(NS)*SND(L,K,NN)` (184). 주석 원문(실행하지 않음): `C      IF(ISTRAN(7).GE.1)THEN` (177), `C      NS=NN+NSED` (180). |
| 191–207 | 시작 시 6행 CALBUOY 안. `IF(ISTRAN(6).GE.1.OR.ISTRAN(7).GE.1)THEN` (191)의 K=1..KC·L=2..LA에서 `B(L,K)=B(L,K)*(1.-TVAR1S(L,K))+TVAR1W(L,K)` (195). 루프·조건 종료(196–199). `GOTO 2000` (201)으로 정상 경로가 진단 경로를 건너뛴다. 구분 주석 뒤에는 염분만의 선형 함수이며 진단 전용이라는 주석(205–206). |
| 208–221 | 시작 시 6행 CALBUOY 안. 1000 CONTINUE(208)는 30행 IBSC=1 이동 목적지이다. K=1..KC·L=2..LA에서 `B(L,K)=0.00075*SAL(L,K)` (212). 루프 종료(213–214), 주석(215–217). 2000 CONTINUE(218)는 정상·진단 경로 공통 반환 지점이다. RETURN·END(220–221). 이 파일에는 CALL 문장이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32·102–114: 정상 경로는 매 호출 ISPCOR=0으로 설정한다. 이후 압력 보정 조건은 ISPCOR=1이다. 두 위치 사이에 ISPCOR를 바꾸는 실행문은 이 파일에 없다.
- 56·85: 염분을 사용하는 두 정상 밀도 분기는 SAL 배열 자체를 MAX(SAL,0)으로 갱신한다. 진단 분기에는 같은 하한 설정이 없다(208–214).
- 30·126–199·208–214: IBSC=1 이동은 정상 밀도 계산과 퇴적물 부력 보정을 모두 건너뛴다. 진단 경로의 식은 계수 0.00075를 고정하여 SAL에 곱한다.
- 36–38·59–62·73–75·88–94: 수온에 관한 다항식 계수는 원문에 상수로 적혀 있다. 해당 계산 블록에는 TEMO·TEM의 상한·하한을 검사하거나 제한하는 문장이 없다.
- 130–143·169–170·195: 두 퇴적물 종류의 보정량을 TVAR1S·TVAR1W에 먼저 합산하고 B*(1−TVAR1S)+TVAR1W를 한 번 적용한다. 종류별로 B를 연속 보정하던 두 블록은 주석이다(150–161·177–189).
