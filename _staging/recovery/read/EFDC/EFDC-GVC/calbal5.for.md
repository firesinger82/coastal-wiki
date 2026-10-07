---
file: models/EFDC/raw/source_code/EFDC-GVC/calbal5.for
lines: 255
sha256: 320305357f463ca1f000a9bbc096c8c60bd61a469b5742ad8c54e98cc190098c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calbal5.for — 판독 구간 기록

구간은 1행부터 255행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | 구분 주석과 `SUBROUTINE CALBAL5` (6) 입구. 버전·수정일·변경 이력 머리말과 체적(volume)·질량(mass)·운동량(momentum)·에너지(energy) 수지 목적 주석이다(8–20). `INCLUDE 'EFDC.PAR'` (24); `INCLUDE 'EFDC.CMN'` (25)로 공통 선언을 포함한다. 수지 기간 종료 검사 주석이다(29). |
| 31–51 | 시작 시 6행 CALBAL5 루틴 안. `IF(NBAL.EQ.NTSMMT)THEN` (31)일 때 종료량 계산·출력·기간 초기화를 실행한다. 32–33행 진단 출력은 주석이다. 37–38행은 최종 체적·염 질량(salt mass)·염료 질량(dye mass)·운동량·운동에너지(kinetic energy)·위치에너지(potential energy) 및 관련 유량(flux) 주석이다. VOLEND·SALEND·DYEEND·UMOEND·VMOEND·UUEEND·VVEEND·PPEEND·BBEEND를 0으로 초기화한다(42–50). |
| 52–64 | 시작 시 6행 루틴·31행 NBAL 분기 안. L=2..LA(52)에서 LN=LNC(L)로 북쪽 이웃을 얻는다(53). 체적·수평 운동량·PPE 위치에너지 합산은 `VOLEND=VOLEND+SPB(L)*DXYP(L)*HP(L)` (54); `UMOEND=UMOEND+SPB(L)*0.5*DXYP(L)*HP(L)*(DYIU(L)*HUI(L)*UHDYE(L)` (55); `&                                 +DYIU(L+1)*HUI(L+1)*UHDYE(L+1))` (56); `VMOEND=VMOEND+SPB(L)*0.5*DXYP(L)*HP(L)*(DXIV(L)*HVI(L)*VHDXE(L)` (57); `&                                 +DXIV(LN)*HVI(LN)*VHDXE(LN))` (58); `PPEEND=PPEEND+SPB(L)*0.5*DXYP(L)` (59); `&             *(GI*P(L)*P(L)-G*BELV(L)*BELV(L))` (60). 루프를 닫은 뒤 합 운동량 크기는 `AMOEND=SQRT(UMOEND*UMOEND+VMOEND*VMOEND)` (63). |
| 65–82 | 시작 시 6행 루틴·31행 NBAL 분기 안. K=1..KC·L=2..LA(65–66), LN=LNC(L)(67)로 북쪽 이웃을 얻는다. 염·염료 합산은 `SALEND=SALEND+SCB(L)*DXYP(L)*HP(L)*SAL(L,K)*DZC(K)` (68); `DYEEND=DYEEND+SCB(L)*DXYP(L)*HP(L)*DYE(L,K)*DZC(K)` (69). 70–73행 면별 0.25 운동에너지 대체식은 주석이다. 실행 운동에너지·밀도 관련 위치에너지 합산은 `UUEEND=UUEEND+SPB(L)*0.125*DXYP(L)*HP(L)*DZC(K)` (74); `&      *( (U(L,K)+U(L+1,K))*(U(L,K)+U(L+1,K)) )` (75); `VVEEND=VVEEND+SPB(L)*0.125*DXYP(L)*HP(L)*DZC(K)` (76); `&      *( (V(L,K)+V(LN,K))*(V(L,K)+V(LN,K)) )` (77); `BBEEND=BBEEND+SPB(L)*GP*DXYP(L)*HP(L)*DZC(K)*( BELV(L)` (78); `&      +0.5*HP(L)*(Z(K)+Z(K-1)) )*B(L,K)` (79). 두 루프를 닫는다(80–81). |
| 83–110 | 시작 시 6행 루틴·31행 NBAL 분기 안. 누적 유출량에 시간 간격 DT를 곱하는 식은 `UUEOUT=DT*UUEOUT` (83); `VVEOUT=DT*VVEOUT` (84); `PPEOUT=DT*PPEOUT` (85); `BBEOUT=DT*BBEOUT` (86); `VOLOUT=DT*VOLOUT` (87); `SALOUT=DT*SALOUT` (88); `DYEOUT=DT*DYEOUT` (89); `UMOOUT=DT*UMOOUT` (90); `VMOOUT=DT*VMOOUT` (91). 총에너지 합은 `ENEBEG=UUEBEG+VVEBEG+PPEBEG+BBEBEG` (93); `ENEEND=UUEEND+VVEEND+PPEEND+BBEEND` (94); `ENEOUT=UUEOUT+VVEOUT+PPEOUT+BBEOUT` (95). 초기량에서 유출량을 빼는 수지 기준량은 `VOLBMO=VOLBEG-VOLOUT` (97); `SALBMO=SALBEG-SALOUT` (98); `DYEBMO=DYEBEG-DYEOUT` (99); `UMOBMO=UMOBEG-DYEOUT` (100); `VMOBMO=VMOBEG-DYEOUT` (101); `ENEBMO=ENEBEG-ENEOUT` (102). 최종량과 기준량의 오차는 `VOLERR=VOLEND-VOLBMO` (104); `SALERR=SALEND-SALBMO` (105); `DYEERR=DYEEND-DYEBMO` (106); `UMOERR=UMOEND-UMOBMO` (107); `VMOERR=VMOEND-VMOBMO` (108); `ENEERR=ENEEND-ENEBMO` (109). |
| 111–138 | 시작 시 6행 루틴·31행 NBAL 분기 안. 상대오차(relative error)의 초기 대입은 `RVERDE=-9999.` (111); `RSERDE=-9999.` (112); `RDERDE=-9999.` (113); `RUERDE=-9999.` (114); `RVERDE=-9999.` (115); `REERDE=-9999.` (116); `RVERDO=-9999.` (118); `RSERDO=-9999.` (119); `RDERDO=-9999.` (120); `RUERDO=-9999.` (121); `RVERDO=-9999.` (122); `REERDO=-9999.` (123). 최종량이 0이 아닐 때의 조건·비율은 `IF(VOLEND.NE.0.) RVERDE=VOLERR/VOLEND` (125); `IF(SALEND.NE.0.) RSERDE=SALERR/SALEND` (126); `IF(DYEEND.NE.0.) RDERDE=DYEERR/DYEEND` (127); `IF(UMOEND.NE.0.) RUMERDE=UMOERR/UMOEND` (128); `IF(VMOEND.NE.0.) RVMERDE=VMOERR/VMOEND` (129); `IF(ENEEND.NE.0.) REERDE=ENEERR/ENEEND` (130). 유출량이 0이 아닐 때의 조건·비율은 `IF(VOLOUT.NE.0.) RVERDO=VOLERR/VOLOUT` (132); `IF(SALOUT.NE.0.) RSERDO=SALERR/SALOUT` (133); `IF(DYEOUT.NE.0.) RDERDO=DYEERR/DYEOUT` (134); `IF(UMOOUT.NE.0.) RUMERDO=UMOERR/UMOOUT` (135); `IF(VMOOUT.NE.0.) RVMERDO=VMOERR/VMOOUT` (136); `IF(ENEOUT.NE.0.) REERDO=ENEERR/ENEOUT` (137). 각 한 줄 IF는 자기 대입문만 제어한다. |
| 139–175 | 시작 시 6행 루틴·31행 NBAL 분기 안. BAL.OUT 출력 주석이다(141). `IF(JSBAL.EQ.1)THEN` (145)이면 `OPEN(89,FILE='BAL.OUT',STATUS='UNKNOWN')` (146); `CLOSE(89,STATUS='DELETE')` (147); `OPEN(89,FILE='BAL.OUT',STATUS='UNKNOWN')` (148)로 기존 파일을 삭제하고 다시 연다. JSBAL=0을 설정한다(149). `ELSE` (150)이면 `OPEN(89,FILE='BAL.OUT',POSITION='APPEND',STATUS='UNKNOWN')` (151)로 추가 기록한다. 154–175행 WRITE는 기간 길이 NTSMMT·종료 시점 N, 초기량·유출량·초기량에서 유출량을 뺀 값·최종량·오차·최종량 기준 상대오차·유출량 기준 상대오차를 단위 89에 출력한다. |
| 176–203 | 시작 시 6행 루틴·31행 NBAL 분기 안. 에너지 성분별 기준량 계산은 `UUEBMO=UUEBEG-UUEOUT` (176); `VVEBMO=VVEBEG-VVEOUT` (177); `PPEBMO=PPEBEG-PPEOUT` (178); `BBEBMO=BBEBEG-BBEOUT` (179). UUE·VVE·PPE·BBE 각 성분의 초기량·유출량·기준량·최종량을 차례로 출력한다(180–200). CLOSE(89)로 파일을 닫는다(202). |
| 204–241 | 시작 시 6행 루틴·31행 NBAL 분기 안. 890 형식은 수지 기간과 종료 시점을 적는다(204–205). 891·893–898 형식은 각 표의 열 제목이다(206–208·210–222). `892 FORMAT (1X,7(E14.6,2X))` (209)는 7개 E14.6 값 형식이다. 899·900은 빈 줄 형식이다(223–224). 901–916은 각 에너지 성분의 초기·유출·기준·최종 값에 붙일 문자열과 E14.6 형식이다(225–240). |
| 242–255 | 시작 시 6행 루틴·31행 NBAL 분기 안. 구분·카운터(counter) 초기화 주석 뒤 NBAL=0을 대입한다(246). 31행 조건을 닫는다(248). 조건 밖에서 `NBAL=NBAL+1` (250)으로 NBAL을 증가시킨다. RETURN·END로 종료한다(254–255). 실행 CALL 문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 100–101: UMOBMO와 VMOBMO는 각각 UMOBEG·VMOBEG에서 DYEOUT를 뺀다. 같은 파일은 UMOOUT·VMOOUT를 DT로 곱하고 출력한다(90–91·159).
- 114·121·128–129·135–136·171·174: 초기값 대입 이름은 RUERDE·RUERDO이다. 운동량 상대오차 계산·출력 이름은 RUMERDE·RVMERDE·RUMERDO·RVMERDO이다. 이 파일에는 이 네 계산·출력 이름의 -9999 초기 대입이 없다.
- 111·115·118·122: RVERDE=-9999.와 RVERDO=-9999.는 각 초기화 목록에서 두 번씩 나온다.
- 31·83–91·246–250: 유출량에 DT를 곱하는 대입은 NBAL=NTSMMT일 때 실행한다. 그 분기 끝에서 NBAL=0을 대입하고 조건 밖에서 NBAL을 1 증가시킨다.
- 145–151: JSBAL=1 경로는 단위 89 파일을 STATUS=DELETE로 닫고 다시 연다. 다른 경로는 POSITION=APPEND로 연다.
