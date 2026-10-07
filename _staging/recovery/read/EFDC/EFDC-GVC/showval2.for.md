---
file: models/EFDC/raw/source_code/EFDC-GVC/showval2.for
lines: 292
sha256: 429a6d719b54a207126f0082ec2c68f4d523529a12939502734dc461c0cd0f96
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# showval2.for — 판독 구간 기록

구간은 1행부터 292행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 머리말·SHOWVAL2 선언·Mike Morton 수정일 주석(1–12). EFDC.PAR·EFDC.CMN 포함(13–14), BLANK·ASTER·CSURF(32)·CSALS(20)·CSALB(20) 문자 선언(16), 공백·별표 DATA 초기화(18–19), 구분 주석을 포함한다(20–22). |
| 23–41 | 시작 시 6행 SHOWVAL2 루틴 안. `      IF(NSHOWC.EQ.NSHOWR)THEN` (23)이면 SHOW.INP를 열고 6줄을 읽어 넘긴다(24–27). 출력 유형·재입력 주기·표시 I·J·ISHPRT와 수면고(surface elevation) 범위·염분(salinity) 최댓값을 읽는다(28–29). `        IF(NSHTYPE.EQ.1)THEN` (31)이면 `          IZSMIN=NINT(ZSSMIN)` (32); `          IZSMAX=NINT(ZSSMAX)` (33); `          ISALMAX=NINT(SSALMAX)` (34)로 문자 그래프 범위를 정수화한다. NSHOWC를 0으로 두고 제목·범위를 장치 6에 출력한다(35–40). `         ELSE` (41)는 다음 유형 분기로 이어진다. |
| 42–86 | 시작 시 6행 SHOWVAL2 루틴·23행 재입력 참 분기·31행 조건의 41행 ELSE 안. 원문 조건·분기는 `          IF(NSHTYPE.EQ.2)THEN` (42); `           ELSE` (51); `            IF(NSHTYPE.EQ.3)THEN` (52); `            IF(NSHTYPE.EQ.4)THEN` (63); `            IF(NSHTYPE.EQ.5)THEN` (73). 유형 2는 N·염분, 유형 3은 TIME·염분, 유형 4는 퇴적물(sediment), 유형 5는 수온(temperature)의 제목을 출력한다(43–81). 각 블록에서 NSHOWC를 0으로 둔다. 빈 제목 출력 일부는 주석이다(47·49·55·58·60·68·70·78·80). 내부·바깥 분기를 닫고 주석을 포함한다(83–86). |
| 87–115 | 시작 시 6행 SHOWVAL2 루틴 안. `      IF(NSHTYPE.EQ.1)THEN` (87)이면 `        NSHOWC=NSHOWC+1` (88) 후 문자 배열을 공백으로 채운다(89–95). L을 LIJ로 구하고(96), `        ZSURF=(HP(L)+BELV(L))*100.` (97); `        ZSTMP=(31.*(ZSURF-ZSSMIN)/(ZSSMAX-ZSSMIN))+1.` (98); `        IZSTMP=NINT(ZSTMP)` (99)로 수면고 위치를 계산한다. 범위 조건은 `        IF(IZSTMP.GT.32)IZSTMP=32` (100); `        IF(IZSTMP.LT.1)IZSTMP=1` (101). 표층 KC·바닥층 1의 염분 위치 식은 `        SSTMP=(19.*SAL(L,KC)/SSALMAX)+1.` (103); `        SBTMP=(19.*SAL(L,1)/SSALMAX)+1.` (104); `        ISSTMP=NINT(SSTMP)` (105); `        ISBTMP=NINT(SBTMP)` (106). 염분 인덱스 조건은 `        IF(ISSTMP.GT.20)ISSTMP=20` (107); `        IF(ISSTMP.LT.1)ISSTMP=1` (108); `        IF(ISBTMP.GT.20)ISBTMP=20` (109); `        IF(ISBTMP.LT.1)ISBTMP=1` (110). 별표를 넣고 32·20·20문자를 출력한다(102·111–114). `      ELSE` (115)는 숫자 표시 분기로 이어진다. |
| 116–149 | 시작 시 6행 SHOWVAL2 루틴·87행 조건의 115행 ELSE 안. `       IF(MOD(N,ISHPRT) .EQ. 0)THEN` (116)이면 `        NSHOWC=NSHOWC+1` (117)로 표시 횟수를 늘린다. `        IF(ISDYNSTP.EQ.0)THEN` (118)이면 `          TIME=(DT*FLOAT(N)+TCON*TBEGIN)/86400.` (119), `        ELSE` (120)이면 `          TIME=TIMESEC/86400.` (121)로 시간을 일(day) 단위로 계산한다. L·LN을 지정한다(123–124). 수면고는 `        ZSURF=(HP(L)+BELV(L))*100.` (125). 표층 속도 평균·동북 성분 회전은 `        UTMP=0.5*STCUV(L)*(U(L+1,KC)+U(L,KC))*100.` (126); `        VTMP=0.5*STCUV(L)*(V(LN,KC)+V(L,KC))*100.` (127); `        VELEKC=CUE(L)*UTMP+CVE(L)*VTMP` (128); `        VELNKC=CUN(L)*UTMP+CVN(L)*VTMP` (129). 바닥층 1의 같은 식은 `        UTMP=0.5*STCUV(L)*(U(L+1,1)+U(L,1))*100.` (130); `        VTMP=0.5*STCUV(L)*(V(LN,1)+V(L,1))*100.` (131); `        VELEKB=CUE(L)*UTMP+CVE(L)*VTMP` (132); `        VELNKB=CUN(L)*UTMP+CVN(L)*VTMP` (133). AV·AB 표시 환산은 `        AVKS=AV(L,KS)*10000.*HP(L)` (134); `        AVKB=AV(L,1)*10000.*HP(L)` (135); `        ABKS=AB(L,KS)*10000.*HP(L)` (136); `        ABKB=AB(L,1)*10000.*HP(L)` (137). 염분 복사(138–139), 비활성 퇴적물 환산식 `C       SEDKC=SEDT(L,KC)/1000.` (140); `C       SEDKB=SEDT(L,1)/1000.` (141); `C       SNDKC=SNDT(L,KC)/1000.` (142); `C       SNDKB=SNDT(L,1)/1000.` (143), 실행 SEDT·SNDT·TEM의 표층·바닥층 복사(144–149)를 포함한다. |
| 150–166 | 시작 시 6행 SHOWVAL2 루틴·87행 조건의 115행 ELSE·116행 출력 주기 참 분기 안. 비활성 정수화 대입식은 `C        IZSURF=NINT(ZSURF)` (150); `C        IVELEKC=NINT(VELEKC)` (151); `C        IVELNKC=NINT(VELNKC)` (152); `C        ISALKC=NINT(SALKC)` (153); `C        ISEDKC=NINT(SEDKC)` (154); `C        ISNDKC=NINT(SNDKC)` (155); `C        ITEMKC=NINT(TEM(L,KC))` (156); `C        IAVKS=NINT(AVKS)` (157); `C        IABKS=NINT(ABKS)` (158); `C        IVELEKB=NINT(VELEKB)` (159); `C        IVELNKB=NINT(VELNKB)` (160); `C        ISALKB=NINT(SALKB)` (161); `C        ISEDKB=NINT(SEDKB)` (162); `C        ISNDKB=NINT(SNDKB)` (163); `C        ITEMKB=NINT(TEM(L,1))` (164); `C        IAVKB=NINT(AVKB)` (165); `C        IABKB=NINT(ABKB)` (166). 수면고·속도·염분·퇴적물·수온·AV·AB의 이 정수 변환들은 모두 주석이다. |
| 167–209 | 시작 시 6행 SHOWVAL2 루틴·87행 조건의 115행 ELSE·116행 출력 주기 참 분기 안. 원문 조건·분기는 `        IF(NSHTYPE.EQ.2)THEN` (167); `         ELSE` (175); `          IF(NSHTYPE.EQ.3)THEN` (176); `          IF(NSHTYPE.EQ.4)THEN` (184); `          IF(NSHTYPE.EQ.5)THEN` (198). 유형 2는 N·I·J·실수 수면고와 표층·바닥층 속도·염분·AV·AB를 형식 7로 출력한다(172–174). `         ELSE` (175) 안에서 유형 3은 TIME·N·I·J·수면고·속도·염분을 형식 77로 출력한다(180–182). 유형 4는 같은 형식으로 SEDT와 SNDT를 각각 한 줄씩 출력한다(191–196). 유형 5는 TEM을 출력한다(202–204). 이전 정수 WRITE들은 주석이다(168–170·177–179·185–190·199–201). 세 바깥 분기 종료·주석을 포함한다(206–209). |
| 210–249 | 시작 시 6행 SHOWVAL2 루틴 안. 구분 주석·입력 건너뛰기 형식 1·PC 화면 형식 변경 주석(210–213). 실행 구분선·제목·단위·실수 출력 형식 2..7을 정의한다(214–225). cm·cm/s·PPT·CMSQS 단위를 적는다(221–222). 문자 그래프 형식 8..11(227–234), 염분·수온·표층/바닥층 제목 33·34·44(235–240), DAYS·CM·CM/S·PPT·MG/L·DEGC 단위 66..68(241–246), F9.5 시간·정수 N/I/J·실수 변수 형식 77(247–248), 빈 줄을 포함한다(226·249). |
| 250–292 | 시작 시 6행 SHOWVAL2 루틴 안. John Hamrick의 원래 형식이라는 주석(250–251) 뒤 이전 FORMAT 2·3·33·34·4..11·44·66..68·77 전체가 주석이다(252–287). 끝 구분 주석·RETURN·END를 포함한다(288–292). 다른 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 87–117: 문자 그래프 유형 1에는 출력 주기 MOD 검사가 없다. 숫자 표시 ELSE에만 MOD(N,ISHPRT)=0 검사가 있다.
- 104·130–149: 바닥 표시값은 수직 인덱스 1을 사용한다. 이 파일에는 KGVCP를 읽는 문장이 없다.
- 28·98·103–104·116: ISHPRT, ZSSMAX-ZSSMIN, SSALMAX는 각각 MOD 인수 또는 분모다. 이 값들이 0인지 검사하는 문장은 없다.
- 88·116–117·207–208: NSHOWC는 문자 그래프 실행 또는 숫자 출력 주기의 참 분기에서만 증가한다. 숫자 출력 주기 조건이 거짓인 호출에는 증가 문장이 없다.
