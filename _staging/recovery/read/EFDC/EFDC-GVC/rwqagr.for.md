---
file: models/EFDC/raw/source_code/EFDC-GVC/rwqagr.for
lines: 84
sha256: cdddc5a65d44cd7f8d11063099971303a7cd248a55581c8067cec81d6e3e1008
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# rwqagr.for — 판독 구간 기록

구간은 1행부터 84행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | 머리말과 `SUBROUTINE RWQAGR(IWQTAGR)` (6). 수정일·버전·변경 이력 주석(10–21). 목적 주석은 조류 성장(algal growth)·호흡(respiration)·포식(predation) 속도와 기본 광 소광계수(light extinction coefficient)의 공간·시간별 입력을 INWQAGR에서 읽는다고 적는다(26–28). EFDC.PAR·EFDC.CMN 포함(32–33), 79자 TITLE(3)·3자 AGRCONT 선언(35). 구분 주석 포함. 포함 파일 내부는 판독하지 않았다. |
| 37–51 | 시작 시 6행 RWQAGR 안. AGRFN을 단위 1·STATUS='UNKNOWN'으로 열고 WQ3D.OUT을 단위 2·append로 연다(37–38). `IF(IWQTAGR.EQ.0)THEN` (40)이면 제목 3행을 읽어 로그에 쓴다(41–43). 현재 IWQTAGR 날짜 메시지 출력(46–47). 한 레코드를 넘기고 TITLE(1)을 읽어 로그에 쓴다(49–51). 분기 종료·주석 포함. |
| 52–66 | 시작 시 6행 RWQAGR 안. I=1..IWQZ 루프(52). 예전 고정 형식 READ·WRITE와 WQSDCOEF 항목은 주석이다(53–58). 실제 입력은 자유 형식(list-directed)으로 MM, WQPMC·WQPMD·WQPMG·WQPMM, WQBMRC·WQBMRD·WQBMRG·WQBMRM, WQPRRC·WQPRRD·WQPRRG·WQPRRM, WQKEB를 각 배열의 I 인덱스에 읽는다(59–61). 같은 MM·13개 값을 FORMAT 51로 로그에 쓴다(62–64). 루프 종료·주석(65–66). 값의 계산·범위 제한·기본값 대입은 이 입력 블록에 없다. |
| 67–76 | 시작 시 6행 RWQAGR 안이며 I 루프 밖. 다음 IWQTAGR·AGRCONT를 읽고 로그에 쓴다(67–68). `IF(AGRCONT.EQ.'END')THEN` (70)이면 단위 1 CLOSE·IWQAGR=0(71–72). 분기 밖에서 단위 2를 닫는다(75). 분기 종료·주석 포함. |
| 77–84 | 시작 시 6행 RWQAGR 안. FORMAT 999=1X, 50=A79, 51=I8·14F8.3, 52=I7·1X·A3, 60=날짜 메시지(77–81). 주석·RETURN·END(82–84). 이 파일에는 서브루틴 CALL이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 52·59–64: 입력 MM은 로그에 쓰인다. 저장 배열 인덱스는 MM이 아니라 루프 I이며 이 파일에는 MM과 I의 일치 검사가 없다.
- 53–64: 주석 처리한 이전 READ·WRITE에는 WQSDCOEF가 있다. 활성 READ·WRITE에는 WQPMM·WQBMRM·WQPRRM이 있고 WQSDCOEF가 없다.
- 37·67–75: 입력 파일 OPEN은 매 호출 실행문이다. 끝의 READ는 인수 IWQTAGR를 다음 입력값으로 덮어쓴다. 입력 파일 CLOSE는 AGRCONT='END' 조건에만 있고 로그 파일 CLOSE는 분기 밖에 있다.
- 62–64·79: 활성 로그는 MM 뒤에 실수 값 13개를 넘긴다. FORMAT 51은 실수 서식 14개를 선언한다.
