---
file: models/EFDC/raw/source_code/EFDC-GVC/rwqben.for
lines: 87
sha256: 74b7b6203c1e890b08503e7ba1eee4b17b02d2fe65ef71d445465117857aed93
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# rwqben.for — 판독 구간 기록

구간은 1행부터 87행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | 머리말과 `SUBROUTINE RWQBEN(IWQTBEN)` (6). 수정일·버전·변경 이력 주석(10–21). 목적 주석은 공간·시간별 저질 플럭스(benthic flux)의 PO4D·NH4·NO3·SAD·COD·O2·TAM 매개변수를 INWQBEN에서 읽는다고 적는다(26–27). EFDC.PAR·EFDC.CMN 포함(31–32). NSMZM 크기의 XBFPO4D·XBFNH4·XBFNO3·XBFCOD·XBFO2·XBFSAD와 79자 TITLE(3)·3자 BENCONT 선언(34–36). 포함 파일 내부는 판독하지 않았다. |
| 38–52 | 시작 시 6행 RWQBEN 안. SUNFN을 단위 1·STATUS='UNKNOWN'으로 열고 WQ3D.OUT을 단위 2·append로 연다(38–39). `IF(IWQTBEN.EQ.0)THEN` (41)이면 TITLE 3행을 읽어 로그에 쓴다(42–44). IWQTBEN 날짜 메시지 출력(46–47). 한 레코드를 건너뛰고 TITLE(1)을 읽어 로그에 쓴다(49–51). 분기 종료·주석 포함. |
| 53–59 | 시작 시 6행 RWQBEN 안. I=1..IWQZ에서 MM과 XBFPO4D(I)·XBFNH4(I)·XBFNO3(I)·XBFSAD(I)·XBFCOD(I)·XBFO2(I)를 FORMAT 51로 읽고 같은 형식으로 로그에 쓴다(53–58). 주석(59). 값의 계산·단위 환산·범위 제한은 이 블록에 없다. |
| 60–69 | 시작 시 6행 RWQBEN 안. L=2..LA에서 IWQ=IWQZMAP(L,1)(60–61). 각 구역(zone) 임시 배열의 IWQ 값을 WQBFPO4D·WQBFNH4·WQBFNO3·WQBFSAD·WQBFCOD·WQBFO2의 L 위치에 복사한다(62–67). 루프 종료·주석(68–69). |
| 70–79 | 시작 시 6행 RWQBEN 안이며 L 루프 밖. 다음 IWQTBEN·BENCONT를 읽고 로그에 쓴다(70–71). `IF(BENCONT.EQ.'END')THEN` (73)이면 입력 단위 1 CLOSE·IWQBEN=0(74–75). 분기 밖에서 로그 단위 2 CLOSE(78). 분기 종료·주석 포함. |
| 80–87 | 시작 시 6행 RWQBEN 안. FORMAT 999=1X, 50=A79, 51=I8·10F8.3, 52=I7·1X·A3, 60=날짜 메시지(80–84). 주석·RETURN·END(85–87). 이 파일에는 서브루틴 CALL이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26–27·34–35·54–57·62–67: 목적 주석은 TAM을 포함한다. 활성 입력·저장·출력 목록은 PO4D·NH4·NO3·SAD·COD·O2의 6개이다.
- 53–58: 입력 MM은 로그에 쓰인다. 저장 배열 인덱스는 루프 I이며 이 파일에는 MM과 I의 일치 검사가 없다.
- 34–35·53·60–67: 임시 배열 크기는 NSMZM, 입력 루프 상한은 IWQZ이다. 셀의 구역 인덱스는 IWQZMAP(L,1)이며 이 파일에는 상한·구역 인덱스 범위 검사가 없다.
- 38·70–78: 입력 파일 OPEN은 매 호출 실행문이다. 끝의 READ는 인수 IWQTBEN을 다음 입력값으로 덮어쓴다. 입력 파일 CLOSE는 BENCONT='END' 조건에만 있고 로그 파일 CLOSE는 분기 밖에 있다.
