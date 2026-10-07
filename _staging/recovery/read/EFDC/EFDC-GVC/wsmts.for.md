---
file: models/EFDC/raw/source_code/EFDC-GVC/wsmts.for
lines: 69
sha256: 2bc5d0ebc587380d99310dc4ea938415f611d2c26a3308064ee207379282c4d1
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# wsmts.for — 판독 구간 기록

구간은 1행부터 69행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | 인수 TINDAY가 있는 루틴 선언은 주석이고 실행 선언은 인수 없는 `WSMTS`이다(6–7). 수정 날짜·버전·변경 기록 틀과 시계열(time-series) 출력 목적을 적는다(11–29). `EFDC.PAR`·`EFDC.CMN`을 포함한다(31–32). TINDAY를 자기 자신에 대입한다(33). 원문 조건·계산식·반복·호출: `TINDAY=TINDAY` (33). |
| 35–44 | 시작 시 7행 WSMTS 루틴 안. WQSDTS1.OUT·WQSDTS2.OUT을 장치 1·2에서 추가 모드로 연다(35–36). ISDYNSTP=0은 DT·N·TBEGIN으로 시각을 계산하여 TCTMSR로 나누고 ELSE는 TIMESEC/TCTMSR을 쓴다(38–43). 원문 조건·계산식·반복·호출: `IF(ISDYNSTP.EQ.0)THEN` (38), `TIMTMP=DT*FLOAT(N)+TCON*TBEGIN` (39), `TIMTMP=TIMTMP/TCTMSR  ` (40), `ELSE` (41), `TIMTMP=TIMESEC/TCTMSR  ` (42). |
| 45–61 | 시작 시 7행 WSMTS 루틴 안. 출력 지점 M=1..ISMTS에서 LL=LSMTS(M)을 가져온다(45–46). SMPON·SMPOP·SMPOC의 인덱스 1·2·3을 각각 합한다(47–49). 첫 파일에는 I/J·시각·퇴적물 농도(sediment concentration)·수질 플럭스(flux)·SMT·SMBST·세 유기물 합을 출력한다(50–54). 둘째 파일에는 I/J·시각·SMCSOD/SMNSOD 등 반응 항과 SMDFN·SMDFP·SMDFC의 1..3 값을 출력한다(55–59). 각 WRITE에서 시각 뒤 실수 항목은 21개이다(50–54·55–59). 지점 루프를 닫는다(60). 원문 조건·계산식·반복·호출: `DO M=1,ISMTS` (45), `LL=LSMTS(M)` (46), `TSMPON = SMPON(LL,1)+SMPON(LL,2)+SMPON(LL,3)` (47), `TSMPOP = SMPOP(LL,1)+SMPOP(LL,2)+SMPOP(LL,3)` (48), `TSMPOC = SMPOC(LL,1)+SMPOC(LL,2)+SMPOC(LL,3)` (49). |
| 62–69 | 시작 시 7행 WSMTS 루틴 안. 대체 FORMAT은 주석이다(62). 실행 FORMAT은 2I5/F11.5/1P/23E11.3이다(63). 두 파일을 닫고 RETURN·END로 끝낸다(65–69). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–7·33: TINDAY 인수형 선언은 주석이고 실행 선언에는 인수가 없다. 실행문의 TINDAY=TINDAY는 자기 대입이다.
- 47–49: 유기물 세 배열의 합산 인덱스는 각각 고정 1·2·3이다.
- 50–59·63: 두 WRITE의 시각 뒤 자료 개수는 각각 21개이며 FORMAT의 지수형 반복 수는 23이다.
