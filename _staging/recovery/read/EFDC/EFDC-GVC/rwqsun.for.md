---
file: models/EFDC/raw/source_code/EFDC-GVC/rwqsun.for
lines: 173
sha256: 850469d110abe4cb7f3f04fb351a978d636798dab7ea55b541b3023de2e8caa7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# rwqsun.for — 판독 구간 기록

구간은 1행부터 173행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 구 RWQSUN과 일평균 일사(solar radiation)·일장 비율(fractional daylength) 입력 목적 주석(1–14). `CTT   SUBROUTINE RWQSUN` (6), INCLUDE·TITLE/SUNCONT 선언(15–18), SUNFN·WQ3D.OUT OPEN(20–21)은 모두 CTT 주석이며 실행되지 않는다. |
| 23–59 | 주석 처리된 구 루틴 블록이며 실행 조건·루프 안은 아니다. 주석 조건 `CTT      IF(IWQTSUN.EQ.0)THEN` (23)은 제목 3줄 판독·출력(24–27). 시각·제목·WQI0/WQFD 읽기·출력은 주석(29–36). 주석 조건 `CTT      IF(IWQTSUN.EQ.0)THEN` (38)이면 WQI1/WQI2=WQI0 복사(39–41). 다음 적용일·SUNCONT 판독·출력(43–44), 주석 조건 `CTT      IF(SUNCONT.EQ.'END')THEN` (45), CLOSE와 `CTT        IWQSUN = 0` (47), 종료·FORMAT·RETURN·END(46–59). 모두 실행되지 않는다. |
| 60–94 | 구분 주석과 실제 `SUBROUTINE RWQSUN` (63), 새 버전·수정 이력(67–83). 일평균 일사와 일장 비율 판독·보간(interpolation) 목적(85–86). `INCLUDE 'EFDC.PAR'` (90), `INCLUDE 'EFDC.CMN'` (91), 구분 주석(92–94). 포함 파일 내부는 판독 대상에 포함하지 않았다. |
| 95–136 | 시작 시 63행 RWQSUN 루틴 안. `IF(ITNWQ.GT.0) GOTO 1000` (95). 고정 파일 SUNDAY.INP를 열기(103), IS=1..7로 제목·헤더 7줄 건너뛰기(107–109). M=0, `ISPAR=1` (112), ISPAR를 MCSUNDAY 대용으로 쓴다는 주석(113). NSUNDAY·TCSUNDAY·TASUNDAY·RMULADJ·ADDADJ를 읽기(114–115), `IF(ISO.GT.0) GOTO 900` (116). `DO M=1,NSUNDAY` (117)에서 TSSRD/SOLSRD/SOLFRD 읽기(118), `IF(ISO.GT.0) GOTO 900` (119). `TSSRD(M)=TCSUNDAY*( TSSRD(M)+TASUNDAY )` (120), `SOLSRD(M)=RMULADJ*(SOLSRD(M)+ADDADJ) * PARADJ` (121). 루프 종료·닫기(122–124), 정상 `GOTO 901` (126). 라벨 900에서 오류 출력·STOP(128–130), 정상 라벨·FORMAT 1/601(132–135), 주석(136). |
| 137–173 | 시작 시 63행 RWQSUN 루틴 안. 라벨 1000과 일평균 일사 보간 제목(139–144). `IF(ISDYNSTP.EQ.0)THEN` (145)이면 `TIME=(DT*FLOAT(N)+TCON*TBEGIN)/86400.` (146); else는 `TIME=TIMESEC/86400.` (148). M1=ISPAR(151), MCSUNDAY 대용 주석(152). 라벨 100에서 `M2=M1+1` (155), `IF(TIME.GT.TSSRD(M2))THEN` (156)이면 M1=M2·`GOTO 100` (157–158); else는 ISPAR=M1(159–160). `TDIFF=TSSRD(M2)-TSSRD(M1)` (164), `WTM1=(TSSRD(M2)-TIME)/TDIFF` (165), `WTM2=(TIME-TSSRD(M1))/TDIFF` (166), `SOLSRDT=WTM1*SOLSRD(M1)+WTM2*SOLSRD(M2)` (167), `SOLFRDT=WTM1*SOLFRD(M1)+WTM2*SOLFRD(M2)` (168). 구분 주석·RETURN·END(169–173). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–59·63: 구 RWQSUN은 CTT 주석 처리되었다. 실제 루틴은 SUNFN 대신 고정 파일 SUNDAY.INP를 사용한다(103).
- 111–113·151–162: 보간 인덱스는 ISPAR에 저장한다. 주석은 MCSUNDAY의 대용이라고 적는다.
- 114–121: SOLSRD는 RMULADJ/ADDADJ/PARADJ로 보정한다. SOLFRD는 입력값을 그대로 저장하며 이 블록에는 0..1 범위 검사가 없다.
- 116·119: IOSTAT 오류 분기는 ISO>0만 검사한다. 입력 READ에는 ISO<0 또는 END 처리문이 없다.
- 128–135: WRITE(6,601)은 M을 전달한다. FORMAT 601에는 정수 출력 지정자가 없다.
- 151–168: 시간 탐색에는 NSUNDAY 자료 수 상한 검사가 없다. TDIFF=0 검사도 없다.

