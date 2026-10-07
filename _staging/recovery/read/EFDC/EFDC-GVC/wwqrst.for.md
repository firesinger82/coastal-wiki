---
file: models/EFDC/raw/source_code/EFDC-GVC/wwqrst.for
lines: 94
sha256: 0742598a9589151246ba548e1d634923ad63f987dba99221d20f6480cc7c48d5
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# wwqrst.for — 판독 구간 기록

구간은 1행부터 94행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | `WWQRST` 시작(6). 수정 날짜·버전·변경 기록 틀을 적는다(10–24). 종료 시 공간 분포(spatial distribution)를 IWQORST 장치에 쓴다는 주석(26). `EFDC.PAR`·`EFDC.CMN`을 포함한다(30–31). XTEM·FEXIST 선언은 주석이다(32–33). |
| 35–49 | 시작 시 6행 WWQRST 루틴 안. 문자 형식 재시작(ASCII restart) 파일 WQWCRST.OUT을 장치 1에서 열고 삭제한 뒤 다시 연다(35–39). ISDYNSTP=0은 DT·N·TBEGIN으로 시각을 계산하고 TCON으로 나누며 ELSE는 TIMESEC/TCON을 쓴다(41–46). N·TIME 헤더와 변수 제목을 쓴다(47–48). 원문 조건·계산식·반복·호출: `IF(ISDYNSTP.EQ.0)THEN` (41), `TIME=DT*FLOAT(N)+TCON*TBEGIN` (42), `TIME=TIME/TCON    ` (43), `ELSE` (44), `TIME=TIMESEC/TCON` (45). |
| 50–60 | 시작 시 6행 WWQRST 루틴 안. 기본 출력 상태 수 NWQV0에 NWQV를 복사한다(51). IDNOTRVA>0이면 NWQV0를 1 증가시킨다(52). 셀 L=2..LA·층 K=1..KC에서 L/K와 WQV의 연속 상태 인덱스 1..NWQV0를 출력한다(53–57). 파일을 닫는다(59). 원문 조건·계산식·반복·호출: `NWQV0=NWQV` (51), `IF(IDNOTRVA.GT.0) NWQV0=NWQV0+1` (52), `DO L=2,LA` (53), `DO K=1,KC` (54). |
| 61–83 | 시작 시 6행 WWQRST 루틴 안. 이진 재시작(binary restart) 안내와 WQWCRST.BIN 존재 검사·삭제·비형식 파일 열기·N/TIME·상태 수 조절·셀/층/상태별 WRITE·닫기 전체가 주석이다(61–82). 실행되는 이진 출력 블록은 없다. |
| 84–94 | 시작 시 6행 WWQRST 루틴 안. 자료 FORMAT은 2I5/1P/22E12.4, 시각 헤더는 I10/F12.5이다(84–85). 고정 변수 헤더의 22개 상태명에는 PTO4·AMN·NIT·DO·MALG라는 표기가 있다(86–91). 빈 주석·RETURN·END를 포함한다(92–94). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26·37–39·47–59: 주석은 장치 IWQORST를 적지만 실행 OPEN·WRITE·CLOSE는 장치 1을 사용한다.
- 51–55: IDNOTRVA>0일 때 출력 상한을 NWQV+1로 증가시킨다. 출력 목록은 1..NWQV0이고 IDNOTRVA 인덱스를 별도 항목으로 지정하지 않는다.
- 55·84·86–91: 자료 출력 개수는 NWQV0로 결정하지만 FORMAT은 고정 22E12.4이며 변수 헤더의 상태명도 22개로 고정되어 있다.
- 61–82: 이진 재시작 안내가 있으나 해당 파일 처리·WRITE 문장은 모두 주석이다.
