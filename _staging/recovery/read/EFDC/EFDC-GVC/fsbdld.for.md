---
file: models/EFDC/raw/source_code/EFDC-GVC/fsbdld.for
lines: 65
sha256: 1d8377751e2323e55149af96f72cb8b287d980d25e275089de73f036f2ca9d1b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# fsbdld.for — 판독 구간 기록

구간은 1행부터 65행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | 구분 주석과 REAL 함수 FSBDLD의 DIASED·GPDIASED·D50·DEP·PEXP·PHID·CSHIELDS·SBDLDP·ISOPT 인수 선언(1–7). EFDC-FULL 1.0a·수정자·날짜, 대체 소류사(bed load) 계수식 추가 이력(9–20). `EFDC.PAR` 포함(22). 무차원 소류사 수송계수 목적(24), DIASED=입경(grain diameter)·GPDIASED=비중(specific gravity)·CSHIELDS=침강속도(settling velocity)라는 원문 주석(26–28). 상수 선택 조건 `IF(ISOPT.EQ.0) FSBDLD=SBDLDP` (32). |
| 34–45 | 시작 시 6행 FSBDLD 함수 안. Van Rijn 1984의 소류사 논문 서지 주석(34–37). `IF(ISOPT.EQ.1)THEN` (39) 안에서 `RD=DIASED*SQRT(GPDIASED)*1.E6` (40), `RD=(1./RD)**0.2` (41), `TMP=CSHIELDS**2.1` (42), `FSBDLD=0.053*RD/TMP` (43). 조건 종료·빈 주석(44–45). |
| 46–54 | 시작 시 6행 FSBDLD 함수 안. 수정 Enguland-Hansen 식이라는 원문 주석과 참고문헌 추가 예정 주석(46–47). `IF(ISOPT.EQ.2)THEN` (49) 안에서 `TMP1=(DEP/D50)**0.33333` (50), `TMP2=(PEXP/PHID)**1.125` (51), `FSBDLD=2.0367*TMP1*TMP2` (52). 조건 종료·빈 주석(53–54). |
| 55–65 | 시작 시 6행 FSBDLD 함수 안. Wu·Wang·Jia의 J. Hydr. Res. V38, 3000이라는 원문 서지 주석(55). `IF(ISOPT.EQ.3)THEN` (57) 안에서 `TMP1=0.03*((PHID/PEXP)**0.6)` (58), `TMP2=TMP1**2.2` (59), `FSBDLD=0.0053/TMP2` (60). 조건 종료·주석·빈 줄·RETURN·END(61–65). 외부 루틴 CALL 문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32·39–61: 반환값 대입은 ISOPT=0·1·2·3 조건 안에만 있다. 그 밖의 ISOPT를 위한 기본 반환값 대입은 이 파일에 없다.
- 46–47: ISOPT=2 설명 주석은 참고문헌을 추가해야 한다고 적는다. 해당 분기의 서지 정보는 이 파일에 없다.
