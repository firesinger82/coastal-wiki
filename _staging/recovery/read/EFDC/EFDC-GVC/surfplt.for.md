---
file: models/EFDC/raw/source_code/EFDC-GVC/surfplt.for
lines: 73
sha256: 52ffd880cf18d0e8050284003f4ddff6a1e1b868364cd0b3a1df9a979ead916e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# surfplt.for — 판독 구간 기록

구간은 1행부터 73행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | SURFPLT 입구(1), 자유 수면 고도(free surface elevation) 등고선 파일 작성 주석(3–5). `INCLUDE 'EFDC.PAR'` (7)·`INCLUDE 'EFDC.CMN'` (8). 길이 80 TITLE·INTEGER*4 VER 선언 및 EE 구분 주석(10–17). 포함 파일 내부는 이 판독 범위에 없다. |
| 18–32 | 시작 시 1행 SURFPLT 루틴 안. `IF(IPPHXY.LE.2)THEN` (18), `IF(JSPPH.NE.1) GOTO 300` (19). JSPPH=1일 때 장치 10의 SURFCON.OUT을 열고 삭제한 뒤 다시 연다(20–22). 제목 설정(23), `LINES=LA-1` (24), `LEVELS=1` (25), `DBS=0.` (26). 제목·행/층 수·DBS를 출력하고 닫은 뒤 JSPPH=0(27–31), 300 CONTINUE(32). |
| 33–47 | 시작 시 1행 루틴·18행 IPPHXY 분기 안. `IF(ISDYNSTP.EQ.0)THEN` (33)이면 `TIME=DT*FLOAT(N)+TCON*TBEGIN` (34), `TIME=TIME/TCON` (35). `ELSE` (36)는 `TIME=TIMESEC/TCON` (37). 조건 종료(38) 뒤 SURFCON.OUT을 APPEND로 열고 N·TIME 출력(39–40). `IF(IPPHXY.EQ.0)THEN` (41)·`DO L=2,LA` (42)에서 `SURFEL=BELV(L)+HP(L)` (43). SURFEL·BELV·HP·HBED(L,KBT(L))·HBEDA를 FORMAT 201로 출력(44–45), 루프·조건 종료(46–47). |
| 48–73 | 시작 시 1행 루틴·18행 IPPHXY 분기 안. `IF(IPPHXY.EQ.1)THEN` (48)·`DO L=2,LA` (49)에서 `SURFEL=BELV(L)+HP(L)` (50). IL·JL·SURFEL·BELV·HP·HBED·HBEDA를 FORMAT 200으로 출력(51–52). 별도 `IF(IPPHXY.EQ.2)THEN` (55)·`DO L=2,LA` (56)에서 `SURFEL=BELV(L)+HP(L)` (57). 같은 출력에 DLON·DLAT를 추가(58–59). 두 루프·조건 종료(53–54·60–61), 파일 close·바깥 조건 종료(62–63). FORMAT은 제목 A80, 시각 I10/F12.4, 행/층 수 2I10, 공간 정보 2I5/9E14.5 또는 9E14.5, DBS 12E12.4(65–70). RETURN·END·끝 빈 줄(71–73). 외부 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14: VER는 선언 이후 이 파일에서 사용하지 않는다.
- 18·41·48·55: 바깥 조건은 IPPHXY<=2이다. 셀 자료 출력 분기는 IPPHXY=0·1·2만 있다.
- 19–31: 파일 삭제와 머리말 작성은 JSPPH=1일 때만 실행한다. 이 분기 종료 시 JSPPH를 0으로 대입한다.
