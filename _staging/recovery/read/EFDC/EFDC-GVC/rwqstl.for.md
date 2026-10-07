---
file: models/EFDC/raw/source_code/EFDC-GVC/rwqstl.for
lines: 74
sha256: f4c1d1a2a8b94300bb8c50746108cfd649ae6ae712cebc3264ea71e96d30b334
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# rwqstl.for — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | 머리말·수정 이력(1–24). `SUBROUTINE RWQSTL(IWQTSTL)` (6), 조류(algae)·난분해성/분해성 입자 유기물(refractory/labile particulate organic matter)·입자 금속(particulate metal)의 침강속도(settling velocity)와 재포기(reaeration) 조정계수를 읽는다는 주석(26–28). `INCLUDE 'EFDC.PAR'` (32), `INCLUDE 'EFDC.CMN'` (33), TITLE(3)·STLCONT 선언(35)과 주석(34·36). 포함 파일 내부는 판독 대상에 포함하지 않았다. |
| 37–56 | 시작 시 6행 RWQSTL 루틴 안. STLFN을 단위 1, WQ3D.OUT append를 단위 2로 열기(37–38). `IF(IWQTSTL.EQ.0)THEN` (40)이면 제목 3줄 판독·출력(41–44). 적용일 출력(45–46), 빈 줄·제목 1줄 판독·출력(48–50). `DO I=1,IWQZ` (51)에서 MM·영역 I의 WQWSC/D/G·WQWSRP/LP/S·스칼라 WQWSM을 읽고 출력(52–55). 영역 루프 종료(56). 이 블록에는 속도 계산식이 없다. |
| 57–74 | 시작 시 6행 RWQSTL 루틴 안. 다음 적용일 IWQTSTL과 STLCONT를 읽고 출력(58–59). `IF(STLCONT.EQ.'END')THEN` (60)이면 단위 1 닫기(61), `IWQSTL = 0` (62), 조건 종료(63). 단위 2 닫기(65). FORMAT 999/50/51/52/60(67–71), 주석·RETURN·END(72–74). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26–28·52–55: 머리말은 재포기 조정계수 입력을 설명한다. 실행 READ에는 침강속도 7개만 있으며 REAC 대입은 없다.
- 51–55: MM을 읽고 로그에 출력한다. 배열은 MM 대신 루프 인덱스 I에 대입한다. WQWSM은 영역 루프에서 같은 스칼라에 반복 입력한다.
- 37–44·60–63: 매 호출 STLFN을 OPEN한다. 제목 3줄은 IWQTSTL=0일 때만 읽는다. 단위 1 CLOSE는 STLCONT='END'일 때만 실행한다.

