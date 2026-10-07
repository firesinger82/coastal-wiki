---
file: models/EFDC/raw/source_code/EFDC-GVC/wsmrst.for
lines: 88
sha256: d15421b7fc1a3ff92fde411940fed5b0efaf4d7b8265ae6d3fb8d8bf0bea952f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# wsmrst.for — 판독 구간 기록

구간은 1행부터 88행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | `WSMRST` 시작(6). 수정 날짜·버전·변경 기록 틀을 적는다(10–24). 종료 시 공간 분포(spatial distribution)를 ISMORST 장치에 쓴다는 주석(26). `EFDC.PAR`·`EFDC.CMN`을 포함한다(30–31). FEXIST 선언은 주석이다(32). |
| 34–48 | 시작 시 6행 WSMRST 루틴 안. 문자 형식 재시작(ASCII restart) 파일 WQSDRST.OUT을 장치 1에서 열고 삭제한 뒤 다시 연다(34–38). ISDYNSTP=0은 DT·N·TBEGIN으로 시각을 계산하여 TCON으로 나누고 ELSE는 TIMESEC/TCON을 쓴다(40–45). N·TIME 헤더와 변수 제목을 쓴다(46–47). 원문 조건·계산식·반복·호출: `IF(ISDYNSTP.EQ.0)THEN` (40), `TIME=DT*FLOAT(N)+TCON*TBEGIN` (41), `TIME=TIME/TCON    ` (42), `ELSE` (43), `TIME=TIMESEC/TCON` (44). |
| 49–57 | 시작 시 6행 WSMRST 루틴 안. L=2..LA에서 셀 번호, SMPON·SMPOP·SMPOC의 NW=1..NSMG 값과 SM1NH4·SM2NH4·SM2NO3·SM2PO4·SM2H2S·SMPSI·SM2SI·SMBST·SMT를 쓴다(49–54). WQSDRST.OUT을 닫는다(56). 원문 조건·계산식·반복·호출: `DO L=2,LA` (49). |
| 58–77 | 시작 시 6행 WSMRST 루틴 안. 이진 재시작(binary restart) 설명과 WQSDRST.BIN 존재 검사·삭제·비형식 파일 열기·헤더·셀별 자료 WRITE·닫기 전체가 주석이다(58–76). 실행되는 이진 출력 블록은 없다. |
| 78–88 | 시작 시 6행 WSMRST 루틴 안. 자료 FORMAT은 I5/1P/18E12.4, 시각 헤더는 I10/F13.5이다(79–80). 변수 헤더는 GPON·GPOP·GPOC를 각각 1..3과 G1NH4·G2NH4·G2NO3·G2PO4·G2H2S·GPSI·G2SI·GBST·GT로 고정한다(81–85). 대체 FORMAT 주석·RETURN·END를 포함한다(78·86–88). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26·36–38·46–56: 목적 주석은 장치 ISMORST를 적지만 실행 OPEN·WRITE·CLOSE는 장치 1을 사용한다.
- 50–53·79·81–85: 세 유기물 배열 출력 개수는 NSMG로 결정한다. 자료 FORMAT은 고정 18E12.4이고 변수 헤더의 군 번호는 각각 1..3이다.
- 58–76: 이진 재시작 파일 출력 안내가 있지만 해당 파일 처리·WRITE 문장은 모두 주석이다.
