---
file: models/EFDC/raw/source_code/EFDC-GVC/rwqcsr.for
lines: 223
sha256: b0fd7dbe40933d843ebfbfb65c29de1016a31395fa2fc50410c4905aae8a1b8d
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# rwqcsr.for — 판독 구간 기록

구간은 1행부터 223행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | 머리말·수정 이력(1–24)·루틴 `SUBROUTINE RWQCSR` (6)과 물기둥(water column) 수질(water quality) 시계열(time series) 판독·갱신 목적 주석(26). `INCLUDE 'EFDC.PAR'` (30), `INCLUDE 'EFDC.CMN'` (31), `CHARACTER*11 FNWQSR(21)` (33) 선언·구분 주석(32–36). 포함 파일 내부는 판독 대상에 포함하지 않았다. |
| 37–80 | 시작 시 6행 RWQCSR 루틴 안. `IF(ITNWQ.GT.0) GOTO 1000` (37)은 초기 파일 판독을 건너뛴다. FNWQSR(1..21)에 CWQSR01.INP..CWQSR21.INP 파일명을 설정(41–61). 개방 경계(open boundary)·체적 유입원(volumetric source) 농도 시계열이라는 주석(65–66). `DO NW=1,NWQV` (70), `IF(NWQCSR(NW).GE.1)THEN` (72)에서 파일을 단위 1로 열고(73), `DO IS=1,15` (77)로 제목·헤더 15줄을 FORMAT 1로 건너뛴다(78–79). |
| 81–112 | 시작 시 6행 RWQCSR 루틴·70행 NW 루프·72행 NWQCSR(NW).GE.1 참 분기 안. `DO NS=1,NWQCSR(NW)` (81)에서 MWQCTLT=1(82), ISTYP·자료 수 MWQCSR·시간 환산 TCWQCSR·시간 이동 TAWQCSR·RMULADJ/ADDADJ를 IOSTAT=ISO로 읽는다(83–84). `IF(ISO.GT.0) GOTO 900` (85). `IF(ISTYP.EQ.1)THEN` (86)이면 수직 가중치 WKQ(1..KC) 읽기(87), `IF(ISO.GT.0) GOTO 900` (88), `DO M=1,MWQCSR(NS,NW)` (89)에서 시간·단일 농도 CSERTMP 읽기(90), `IF(ISO.GT.0) GOTO 900` (91), `TWQCSER(M,NS,NW)=TWQCSER(M,NS,NW)+TAWQCSR(NS,NW)` (92), K 루프에서 `WQCSER(M,K,NS,NW)=(RMULADJ*(CSERTMP+ADDADJ))*WKQ(K)` (94). else(97)는 시간과 KC개 농도 입력(98–100), `IF(ISO.GT.0) GOTO 900` (101), `TWQCSER(M,NS,NW)=TWQCSER(M,NS,NW)+TAWQCSR(NS,NW)` (102), K 루프의 `WQCSER(M,K,NS,NW)=RMULADJ*(WQCSER(M,K,NS,NW)+ADDADJ)` (104). 두 입력 경로·NS 루프·파일·NW 루프 종료(107–112). |
| 113–144 | 시작 시 6행 RWQCSR 루틴 안. 정상 입력은 `GOTO 901` (115). 900 라벨에서 NW/NS/M 오류 출력과 STOP(117–119). 정상 라벨과 FORMAT 1/601/602(121–125). 1000 라벨(129)은 37행 분기 진입점. NW=1..NWQV·K=1..KC에서 기본값 `CSERTWQ(K,0,NW)=0.` (137)을 설정(135–139). 농도 시계열 보간(interpolation) 제목·구분 주석(140–144). |
| 145–176 | 시작 시 6행 RWQCSR 루틴 안. `DO NW=1,NWQV` (145), `DO NS=1,NWQCSR(NW)` (147). `IF(ISDYNSTP.EQ.0)THEN` (148)이면 `TIME=DT*FLOAT(N)+TCON*TBEGIN` (149), `TIME=TIME/TCWQCSR(NS,NW)` (150); else는 `TIME=TIMESEC/TCWQCSR(NS,NW)` (152). 이전 MWQCTLT를 M1에 복사(155), 라벨 100에서 `M2=M1+1` (157). `IF(TIME.GT.TWQCSER(M2,NS,NW))THEN` (158)이면 M1=M2와 `GOTO 100` (159–160), else는 MWQCTLT=M1(161–162). `TDIFF=TWQCSER(M2,NS,NW)-TWQCSER(M1,NS,NW)` (165), `WTM1=(TWQCSER(M2,NS,NW)-TIME)/TDIFF` (166), `WTM2=(TIME-TWQCSER(M1,NS,NW))/TDIFF` (167). K=1..KC에서 `CSERTWQ(K,NS,NW)=WTM1*WQCSER(M1,K,NS,NW)` (169), 연속행 `&                   +WTM2*WQCSER(M2,K,NS,NW)` (170). K/NS/NW 루프 종료와 주석(171–176). |
| 177–200 | 시작 시 6행 RWQCSR 루틴 안. 첫 호출 유출 농도(outflow concentration) 초기화 주석(179). `IF(ITNWQ.EQ.0)THEN` (183), `DO NW=1,NWQV` (185), `DO K=1,KC` (186) 안 남쪽 `DO LL=1,NWQOBS` (187)에서 NSID와 L=LIJ 복사(188–189), `CWQLOS(LL,K,NW)=WTCI(K,1)*WQOBCS(LL,1,NW)` (190), 연속행 `&    +WTCI(K,2)*WQOBCS(LL,2,NW)+CSERTWQ(K,NSID,NW)` (191), NWQLOS=0(192). 서쪽 `DO LL=1,NWQOBW` (194)에서 NSID와 L 복사(195–196), `CWQLOW(LL,K,NW)=WTCI(K,1)*WQOBCW(LL,1,NW)` (197), 연속행 `&    +WTCI(K,2)*WQOBCW(LL,2,NW)+CSERTWQ(K,NSID,NW)` (198), NWQLOW=0(199). 서쪽 루프 종료(200). |
| 201–223 | 시작 시 6행 RWQCSR 루틴·183행 ITNWQ.EQ.0 참 분기·185행 NW 루프·186행 K 루프 안. 동쪽 `DO LL=1,NWQOBE` (201)에서 NSID와 L=LIJ 복사(202–203), `CWQLOE(LL,K,NW)=WTCI(K,1)*WQOBCE(LL,1,NW)` (204), 연속행 `&    +WTCI(K,2)*WQOBCE(LL,2,NW)+CSERTWQ(K,NSID,NW)` (205), NWQLOE=0(206). 북쪽 `DO LL=1,NWQOBN` (208)에서 NSID와 L 복사(209–210), `CWQLON(LL,K,NW)=WTCI(K,1)*WQOBCN(LL,1,NW)` (211), 연속행 `&    +WTCI(K,2)*WQOBCN(LL,2,NW)+CSERTWQ(K,NSID,NW)` (212), NWQLON=0(213). LL/K/NW 루프·조건 종료(214–218), 구분 주석·RETURN·END(219–223). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 33·41–61·70–73: 파일명 배열은 21개로 고정한다. 판독 루프는 NWQV까지 돌며 이 블록에는 NWQV<=21 검사가 없다.
- 83–105: IOSTAT 오류 분기는 ISO>0만 검사한다. 이 READ들에는 ISO<0 또는 END 처리문이 없다.
- 155–167: M2를 증가시키는 탐색에는 MWQCSR 상한 검사가 없다. 보간 분모 TDIFF가 0인지 검사하는 조건도 없다.
- 188–212: 네 방향 유출 초기화에서 L=LIJ를 계산한다. 각 농도식과 초기화 대입은 LL을 사용하며 이 블록에서 L을 참조하지 않는다.

