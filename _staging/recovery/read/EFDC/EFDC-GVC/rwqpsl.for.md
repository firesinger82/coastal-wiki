---
file: models/EFDC/raw/source_code/EFDC-GVC/rwqpsl.for
lines: 361
sha256: af79358df1923bfce34d905876287f8557c67386c76501e33ee35618d1679138
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# rwqpsl.for — 판독 구간 기록

구간은 1행부터 361행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | 구 RWQPSL과 단위·환산 설명 주석(1–24). `CTT      OLD SUBROUTINE RWQPSL` (6)은 주석이며 실행 루틴 선언이 아니다. kg/day, 유량 m³/s, 산소 g/m³, TAM kmol/day, FCB MPN/100mL의 구 입력 단위 주석(10–21). INCLUDE·`CTT      PARAMETER (CONV1=1.0E3,CONV2=8.64E4)` (28)·문자 선언·PSLFN/WQ3D.OUT OPEN까지 CTT 주석 처리(25–32). |
| 34–65 | 시작 시 6행에서 소개한 구 루틴의 주석 블록 안이며 실행 조건·루프 안은 아니다. 주석 조건 `CTT      IF(IWQTPSL.EQ.0)THEN` (34)은 제목·IWQPS 판독(35–42). 시각·제목 로그와 주석 `CTT      DO M=1,IWQPS` (49)에서 좌표·유량·부하 읽기(43–51). 주석 조건 `CTT        IF(IJCT(I,J).LT.1 .OR. IJCT(I,J).GT.8)THEN` (52), 좌표 오류 STOP(53–55), L/IWQPSC 설정(56–57). 주석 식 `CTT          WQWPSL(M,NW) = WQWPSL(M,NW) * CONV1` (59), `CTT        WQTT = WQPSQ(M)*CONV2` (61), `CTT        WQWPSL(M,19) = WQWPSL(M,19) * WQTT` (62), `CTT        WQWPSL(M,20) = WQWPSL(M,20) * CONV1` (63), `CTT        WQWPSL(M,NWQV) = WQWPSL(M,NWQV) * WQTT` (64), 주석 루프 종료(65). 모두 실행되지 않는다. |
| 66–125 | 구 루틴의 주석 후반(66–84). 다음 시각·PSLCONT 읽기·출력(67–68), 주석 조건 `CTT      IF(PSLCONT.EQ.'END')THEN` (69), 파일 닫기·`CTT        IWQPSL = 0` (71), 주석 FORMAT·RETURN·END(74–84). 구분 주석(85–90). 실제 `SUBROUTINE RWQPSL` (91), 새 버전·수정 이력(95–110), 모든 부하는 kg/day이며 대장균(coliform)은 MPN/day, 첫 20 상태변수는 g/day로 내부 환산한다는 주석(113–115). `INCLUDE 'EFDC.PAR'` (119), `INCLUDE 'EFDC.CMN'` (120), `DIMENSION RLDTMP(21)` (122)·구분 주석(124–125). 포함 파일 내부는 판독 대상에 포함하지 않았다. |
| 126–180 | 시작 시 91행 RWQPSL 루틴 안. `IF(ITNWQ.GT.0) GOTO 1000` (126). `IF( NPSTMSR.GE.1)THEN` (134)이면고정 파일 WQPSL.INP 열기(135), IS=1..13 제목·헤더 건너뛰기(139–141). `DO NS=1,NPSTMSR` (143)에서 MWQPTLT=1(144), 자료 수·시간 환산·시간 이동·RMULADJ/ADDADJ를 읽기(145–146), `IF(ISO.GT.0) GOTO 900` (147). `RMULADJ=1000.*RMULADJ` (148), `ADDADJ=ADDADJ` (149). `DO M=1,MWQPSR(NS)` (150)에서 시간과 부하 1..7/8..14/15..21 읽기(151·153·155), `IF(ISO.GT.0) GOTO 900` (152·154·156). `TWQPSER(M,NS)=TWQPSER(M,NS)+TAWQPSR(NS)` (157), `WQPSSER(M,21,NS)=RMULADJ*RLDTMP(21)` (159), NW=1..20에서 `WQPSSER(M,NW,NS)=RMULADJ*RLDTMP(NW)` (161), NW=1..21에서 `WQPSSER(M,NW,NS)=MAX(WQPSSER(M,NW,NS),0.0)` (164)로 음수 제한. 루프·파일·조건 종료(166–170). 정상 `GOTO 901` (174), 라벨 900 오류 출력·STOP(176–178), 정상 라벨 901(180). |
| 181–229 | 시작 시 91행 RWQPSL 루틴 안. FORMAT 1/601/602(182–184), 라벨 1000(188). NW=1..NWQV에서 기본값 `WQPSSRT(NW,0)=0.` (195). 부하 시계열 보간(interpolation) 제목(200). `DO NS=1,NPSTMSR` (202), `IF(ISDYNSTP.EQ.0)THEN` (203)이면 `TIME=DT*FLOAT(N)+TCON*TBEGIN` (204), `TIME=TIME/TCWQPSR(NS)` (205); else는 `TIME=TIMESEC/TCWQPSR(NS)` (207). M1=MWQPTLT(NS)(210), 라벨 100에서 `M2=M1+1` (212). `IF(TIME.GT.TWQPSER(M2,NS))THEN` (213)이면 M1=M2·`GOTO 100` (214–215), else는 MWQPTLT=M1(216–217). `TDIFF=TWQPSER(M2,NS)-TWQPSER(M1,NS)` (220), `WTM1=(TWQPSER(M2,NS)-TIME)/TDIFF` (221), `WTM2=(TIME-TWQPSER(M1,NS))/TDIFF` (222), NW 루프에서 `WQPSSRT(NW,NS)=WTM1*WQPSSER(M1,NW,NS)` (224), 연속행 `&                   +WTM2*WQPSSER(M2,NW,NS)` (225). 루프 종료·주석(226–229). |
| 230–272 | 시작 시 91행 RWQPSL 루틴 안. `IF(ITNWQ.EQ.0)THEN` (232)이면 WQPSLT.DIA를 열기·삭제·재열기(234–236), N/TIME 출력(238), NS=1..NPSTMSR에서 변수별 보간 부하 출력·닫기(240–244), 조건 종료(246). 상수·변동 점오염원(point source) 부하 결합 제목과 여러 점오염원을 셀·층별로 합치도록 3차원 배열로 바꾸었다는 주석(250–254). 구 결합 루프와 식은 CMRM 주석 처리(255–262). NW=1..NWQV·K=1..KC·L=2..LA에서 `WQWPSL(L,K,NW) = 0.0` (269)으로 매 호출 결합 부하 초기화(266–272). |
| 273–298 | 시작 시 91행 RWQPSL 루틴 안. 상수·변동 부하를 셀에 더한다는 주석(274). `IF(ITNWQ.EQ.0)THEN` (276)이면 WQPSL.DIA 열기·삭제·재열기·N/TIME 출력(278–281), 조건 종료(283). `DO NS=1,IWQPS` (285)에서 L=LIJ(ICPSL,JCPSL), K=KCPSL, ITMP=MVPSL 복사(286–288). `IF(ITNWQ.EQ.0) WRITE(1,121)NS,L,ICPSL(NS),JCPSL(NS),K,ITMP` (289). `IF(K.GE.1)THEN` (290)이면 NW=1..NWQV에서 `WQWPSL(L,K,NW) = WQWPSL(L,K,NW)` (292), 연속행 `+         + WQWPSLC(NS,NW) + WQPSSRT(NW,ITMP)` (293)로 해당 층에 누적. else(295) 뒤 sigma 층·일반 수직좌표(generalized vertical coordinates, GVC)의 균등 부하 분포 변경 주석(297–298). |
| 299–322 | 시작 시 91행 RWQPSL 루틴·285행 NS 루프·295행 else(K.GE.1 불성립) 안. `if (IGRIDV .eq. 0) then` (299)이면 `TMPVAL=1./FLOAT(KC)` (300), KK=1..KC·NW=1..NWQV(301–302)에서 `WQWPSL(L,KK,NW) = WQWPSL(L,KK,NW)` (303), 연속행 `+         + TMPVAL*( WQWPSLC(NS,NW) + WQPSSRT(NW,ITMP) )` (304). else(308)는 `TMPVAL=1.0/ (FLOAT(KC)/GVCSCLP(L))` (309), 이어서 `TMPVAL=1./ (GVCSCLPI(L)*FLOAT(KC))` (310), `DO KK=KC,KC-int(GVCSCLPI(L)*KC)+1,-1` (311), NW 루프(312)에서 `WQWPSL(L,KK,NW) = WQWPSL(L,KK,NW)` (313), 연속행 `+         + TMPVAL*( WQWPSLC(NS,NW) + WQPSSRT(NW,ITMP) )` (314). 두 루프·IGRIDV 분기·K 분기·NS 루프 종료와 빈 줄·주석(315–322). |
| 323–361 | 시작 시 91행 RWQPSL 루틴 안. `IF(ITNWQ.EQ.0)THEN` (323)이면 별도 OPEN/헤더는 주석(325–329), L=2..LA에서 ITMP=IWQPSC(L,1)(331–332). `IF(ITMP.GT.0)THEN` (333)이면 K=1..KC에서 결합 부하를 WQPSL.DIA에 출력(334–336). 루프·조건 종료(337–338). 구 출력 루프는 주석이며 주석 조건 `C         IF(ITMP.GT.0)THEN` (343)도 실행되지 않는다(340–347). CLOSE(1)·첫 호출 조건 종료(349–351), FORMAT 110/111/112/121(353–356), 구분 주석·RETURN·END(357–361). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–84·91: 구 RWQPSL의 선언·입력·환산·종료는 CTT 주석이다. 실제 루틴 선언은 91행에 있다.
- 145–161: ADDADJ를 입력하고 ADDADJ=ADDADJ 자기 대입을 한다. 실행 부하 계산에는 ADDADJ를 사용하지 않는다.
- 113–115·148–164: 주석은 대장균 입력 MPN/day와 첫 20변수 환산을 설명한다. 실제 식은 RMULADJ에 1000을 곱하고 21번째 변수에도 같은 RMULADJ를 적용한다.
- 210–225: 보간 탐색에는 MWQPSR 자료 수 상한 검사가 없다. TDIFF=0 검사도 없다.
- 202–208·238·281: 이 파일의 TIME 계산은 NPSTMSR 시계열 루프 안에 있다. 첫 호출의 진단 출력은 NPSTMSR과 별개로 TIME을 참조한다.
- 290–311: K>=1 분기에는 K<=KC 검사가 없다. 그 밖의 모든 K값은 균등 분포 else로 들어간다.
- 309–314: TMPVAL을 두 번 연속 계산한다. 누적식은 두 번째 값을 사용한다. 층 수는 int(GVCSCLPI(L)*KC)로 정하고 가중치는 GVCSCLPI(L)*FLOAT(KC)의 역수로 정한다.

