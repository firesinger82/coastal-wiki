---
file: models/EFDC/raw/source_code/EFDC-GVC/showval1.for
lines: 263
sha256: 48c06111e543c861126777991f83ea9f4c865d62a95652eba8d5f5219da2548a
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# showval1.for — 판독 구간 기록

구간은 1행부터 263행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | 머리말·SHOWVAL1 선언·버전·수정 이력·주석(1–21). EFDC.PAR·EFDC.CMN을 포함한다(22–23). BLANK·ASTER·32문자 CSURF·20문자 CSALS·CSALB 배열 선언(25), 공백·별표 DATA 초기화(27–28), 구분 주석을 포함한다(29–31). |
| 32–50 | 시작 시 6행 SHOWVAL1 루틴 안. `      IF(NSHOWC.EQ.NSHOWR)THEN` (32)이면 SHOW.INP를 열고 6줄을 읽어 넘긴다(33–36). NSHTYPE·NSHOWR·관측 I·J·ISHPRT와 수면고(surface elevation) 범위·염분(salinity) 최댓값을 읽고 닫는다(37–39). `        IF(NSHTYPE.EQ.1)THEN` (40)이면 `          IZSMIN=NINT(ZSSMIN)` (41); `          IZSMAX=NINT(ZSSMAX)` (42); `          ISALMAX=NINT(SSALMAX)` (43)으로 표시 범위를 정수화한다. NSHOWC=0 후 문자 그래프 제목·범위를 장치 6에 출력한다(44–49). `         ELSE` (50)는 다음 구간의 다른 출력 유형으로 이어진다. |
| 51–94 | 시작 시 6행 SHOWVAL1 루틴·32행 재입력 참 분기·40행 조건의 50행 ELSE 안. 원문 조건·분기는 `          IF(NSHTYPE.EQ.2)THEN` (51); `           ELSE` (60); `            IF(NSHTYPE.EQ.3)THEN` (61); `            IF(NSHTYPE.GE.5)THEN` (71); `            IF(NSHTYPE.EQ.4)THEN` (81). 유형 2는 시간 단계(step)·염분, 유형 3은 일(day)·염분, 유형 5 이상은 퇴적물(sediment), 유형 4는 수온(temperature) 제목을 출력한다(52–89). 각 해당 블록은 NSHOWC를 0으로 둔다. 내부 분기와 두 바깥 분기를 닫고 주석을 포함한다(91–94). |
| 95–100 | 시작 시 6행 SHOWVAL1 루틴 안이며 재입력 분기 밖. `      IMODTMP=MOD(N,ISHPRT)` (95)로 출력 주기 나머지를 구한다. `      IF(IMODTMP.NE.0)THEN` (96)이면 `        NSHOWC=NSHOWC+1` (97) 후 즉시 RETURN이다(98). 조건 종료·주석을 포함한다(99–100). |
| 101–131 | 시작 시 6행 SHOWVAL1 루틴 안. `      IF(NSHTYPE.EQ.1)THEN` (101)이면 `        NSHOWC=NSHOWC+1` (102) 후 CSURF·CSALS·CSALB를 공백으로 채운다(103–109). L=LIJ(ICSHOW,JCSHOW), KBP=KGVCP(L)을 사용한다(110–111). 수면고·위치 계산은 `        ZSURF=(HP(L)+BELV(L))*100.` (112); `        IF(IS1DCHAN.GT.0) ZSURF=HP(L)*100.` (113); `        ZSTMP=(31.*(ZSURF-ZSSMIN)/(ZSSMAX-ZSSMIN))+1.` (114); `        IZSTMP=NINT(ZSTMP)` (115). 범위 조건은 `        IF(IZSTMP.GT.32)IZSTMP=32` (116); `        IF(IZSTMP.LT.1)IZSTMP=1` (117)이며 별표를 넣는다(118). 표층·바닥층 염분 위치는 `        SSTMP=(19.*SAL(L,KC)/SSALMAX)+1.` (119); `        SBTMP=(19.*SAL(L,KBP)/SSALMAX)+1.` (120); `        ISSTMP=NINT(SSTMP)` (121); `        ISBTMP=NINT(SBTMP)` (122). 범위 조건은 `        IF(ISSTMP.GT.20)ISSTMP=20` (123); `        IF(ISSTMP.LT.1)ISSTMP=1` (124); `        IF(ISBTMP.GT.20)ISBTMP=20` (125); `        IF(ISBTMP.LT.1)ISBTMP=1` (126)이며 두 염분 배열에 별표를 넣는다(127–128). N·I·J와 32·20·20개의 문자를 출력한다(129–130). `       ELSE` (131)는 숫자 표시 분기로 이어진다. |
| 132–158 | 시작 시 6행 SHOWVAL1 루틴·101행 조건의 131행 ELSE 안. `        NSHOWC=NSHOWC+1` (132)로 호출 수를 늘린다. `        IF(ISDYNSTP.EQ.0)THEN` (133)이면 `          TIME=(DT*FLOAT(N)+TCON*TBEGIN)/86400.` (134), `        ELSE` (135)이면 `          TIME=TIMESEC/86400.` (136)으로 시간을 일 단위로 환산한다. 시간 표시 보정 조건·식은 `	  IF(TIME.GE.9999.5) TIME=TIME-10000.0` (138); `	  IF(TIME.LT.0.0) TIME=ABS(TIME)` (139). L·KBP·LN을 가져온다(140–142). 수면고 계산·1차원 수로(channel) 조건은 `        ZSURF=(HP(L)+BELV(L))*100.` (143); `        IF(IS1DCHAN.GT.0) ZSURF=HP(L)*100.` (144). 표층 셀 중심 속도와 동·북 성분 회전은 `        UTMP=0.5*STCUV(L)*(U(L+1,KC)+U(L,KC))*100.` (145); `        VTMP=0.5*STCUV(L)*(V(LN,KC)+V(L,KC))*100.` (146); `        VELEKC=CUE(L)*UTMP+CVE(L)*VTMP` (147); `        VELNKC=CUN(L)*UTMP+CVN(L)*VTMP` (148). KBP 바닥층의 같은 식은 `        UTMP=0.5*STCUV(L)*(U(L+1,KBP)+U(L,KBP))*100.` (149); `        VTMP=0.5*STCUV(L)*(V(LN,KBP)+V(L,KBP))*100.` (150); `        VELEKB=CUE(L)*UTMP+CVE(L)*VTMP` (151); `        VELNKB=CUN(L)*UTMP+CVN(L)*VTMP` (152). 점성·확산 관련 AV·AB 표시값은 `        AVKS=AV(L,KS)*10000.*HP(L)` (153); `        AVKB=AV(L,KBP)*10000.*HP(L)` (154); `        ABKS=AB(L,KS)*10000.*HP(L)` (155); `        ABKB=AB(L,KBP)*10000.*HP(L)` (156). 표층·바닥층 SAL을 복사한다(157–158). |
| 159–186 | 시작 시 6행 SHOWVAL1 루틴·101행 조건의 131행 ELSE 안. `        IF(NSHTYPE.EQ.6)THEN` (159)이면 `          SEDKC=SEDT(L,KC)/1000.` (160); `          SEDKB=SEDT(L,KBP)/1000.` (161); `          SNDKC=SNDT(L,KC)/1000.` (162); `          SNDKB=SNDT(L,KBP)/1000.` (163)으로 SEDT·SNDT를 1000으로 나눈다. `         ELSE` (164)에서는 원값을 복사한다(165–168). 분기 종료(169) 뒤 수면고·속도·염분·퇴적물·수온·AV·AB의 정수화 식은 `        IZSURF=NINT(ZSURF)` (170); `        IVELEKC=NINT(VELEKC)` (171); `        IVELNKC=NINT(VELNKC)` (172); `        ISALKC=NINT(SALKC)` (173); `        ISEDKC=NINT(SEDKC)` (174); `        ISNDKC=NINT(SNDKC)` (175); `        ITEMKC=NINT(TEM(L,KC))` (176); `        IAVKS=NINT(AVKS)` (177); `        IABKS=NINT(ABKS)` (178); `        IVELEKB=NINT(VELEKB)` (179); `        IVELNKB=NINT(VELNKB)` (180); `        ISALKB=NINT(SALKB)` (181); `        ISEDKB=NINT(SEDKB)` (182); `        ISNDKB=NINT(SNDKB)` (183); `        ITEMKB=NINT(TEM(L,KBP))` (184); `        IAVKB=NINT(AVKB)` (185); `        IABKB=NINT(ABKB)` (186). |
| 187–216 | 시작 시 6행 SHOWVAL1 루틴·101행 조건의 131행 ELSE 안. 원문 조건·분기는 `        IF(NSHTYPE.EQ.2)THEN` (187); `         ELSE` (191); `          IF(NSHTYPE.EQ.3)THEN` (192); `          IF(NSHTYPE.GE.5)THEN` (197); `          IF(NSHTYPE.EQ.4)THEN` (209). 유형 2는 N과 표층·바닥층 정수 값을 형식 7로 출력한다(188–190). `         ELSE` (191) 안에서 유형 3은 TIME과 염분을 형식 77로 출력한다(193–195). 유형 5 이상은 점착성 퇴적물(cohesive sediment) 값을 형식 77로 쓰고, 비점착성 퇴적물(noncohesive sediment) 값은 추가 형식 79로 쓴다(204–207). 대체 WRITE 두 묶음은 주석이다(198–203). 유형 4는 수온을 출력한다(210–212). 내부 분기·101행 분기·주석을 포함한다(214–216). |
| 217–244 | 시작 시 6행 SHOWVAL1 루틴 안. 구분 주석(217–218), 입력 건너뛰기 형식 1, 구분선 2, 염분·퇴적물·수온 제목 3·33·34, 표층·바닥층 구분 4·5, cm·cm/s·PSU·cm²/s 단위 표기 6을 정의한다(219–233). 정수 출력 형식 7(234–236), 수면고·염분 문자 그래프 제목·범위 형식 8·9·10, 32A1·20A1·20A1 출력 형식 11을 정의한다(237–244). |
| 245–263 | 시작 시 6행 SHOWVAL1 루틴 안. 표층·바닥층 제목 44, 일·염분 단위 66, 퇴적물 MG/L 단위 67, 수온 D:C 단위 68을 정의한다(245–252). 시간 F6.1과 나머지 정수 필드의 형식 77(253–255), 추가 비점착성 퇴적물 두 필드의 형식 79(256–258), 주석·RETURN·END를 포함한다(259–263). 다른 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 37·95: ISHPRT를 입력으로 읽은 뒤 MOD(N,ISHPRT)에 사용한다. 이 파일에는 ISHPRT=0 검사가 없다.
- 114·119–120: 문자 그래프는 ZSSMAX-ZSSMIN 및 SSALMAX로 나눈다. 표시 인덱스는 뒤에서 제한하지만 이 분모들을 검사하는 문장은 없다.
- 138–139: 시간 보정은 TIME>=9999.5일 때 10000.0을 한 번 뺀다. 이어 음수이면 ABS를 적용한다.
- 111·120·141·149–156: 바닥 표시층은 KGVCP(L)이다. 표층 AV·AB는 KS, 표층 속도·염분은 KC를 사용한다.
- 71·159–168·197–207: 퇴적물 출력 조건은 NSHTYPE>=5다. SEDT·SNDT를 1000으로 나누는 조건은 NSHTYPE=6이다.
