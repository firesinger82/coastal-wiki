---
file: models/EFDC/raw/source_code/EFDC-GVC/rwqrst.for
lines: 93
sha256: 2b8e224fdd40789989ef0ee0dfa42bf6a5bb37d12718e6d40e354b62a4abca0b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# rwqrst.for — 판독 구간 기록

구간은 1행부터 93행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | 머리말·수정 이력(1–24). `SUBROUTINE RWQRST` (6)은 재시작(restart) 파일에서 초기조건(initial conditions)을 읽는다는 주석(26). `INCLUDE 'EFDC.PAR'` (30), `INCLUDE 'EFDC.CMN'` (31), FEXIST 논리형·NN 정수·XTIME 실수 선언(32–34). 바이너리(binary) 재시작 파일을 먼저 확인하고 없으면 ASCII 파일을 사용한다는 주석(36–37). 포함 파일 내부는 판독 대상에 포함하지 않았다. |
| 39–54 | 시작 시 6행 RWQRST 루틴 안. `LK=(LA-1)*KC` (39). WQWCRST.BIN 존재 여부 INQUIRE(41). `IF(.NOT. FEXIST)THEN` (42)이면 단위 1 WQWCRST.INP 열기·헤더 2줄 건너뛰기(43–45). NWQV0=NWQV(47), `IF(IDNOTRVA.GT.0) NWQV0=NWQV0+1` (48). `DO M=1,LK` (49)에서 L/K와 WQV(L,K,1..NWQV0)를 목록 지시 형식(list-directed format)으로 읽는다(51). 디버그 출력은 주석(50), 루프 종료·파일 닫기(52–54). |
| 55–74 | 시작 시 6행 RWQRST 루틴·42행 파일 존재 분기 안에서 else(55)로 시작한다. WQWCRST.BIN을 FORM='UNFORMATTED'로 열고(57–58), NN/XTIME를 읽기(59), `XTIME=XTIME` (60) 자기 대입, 단위 0에 재시작 시간 출력·FORMAT 911(61–63). ACCESS='TRANSPARENT' OPEN은 주석(56). NWQV0=NWQV(64), `IF(IDNOTRVA.GT.0) NWQV0=NWQV0+1` (65). `DO M=1,LK` (66)에서 L/K 레코드 읽기(67), NW=1..NWQV0에서 WQV 스칼라를 각 레코드로 읽기(68–70). 루프 종료·닫기·파일 존재 분기 종료(71–74). |
| 75–93 | 시작 시 6행 RWQRST 루틴 안. 대형조류(macroalgae) 생물량(biomass)은 바닥층에만 남긴다는 주석(75). `IF(IDNOTRVA.GT.0)THEN` (76), `IF(KC.GT.1)THEN` (80) 안 K=2..KC·L=2..LA에서 `WQV(L,K,22)=0.` (83). 바닥층 SMAC 적용 루프는 주석(77–79). 루프·조건 종료(84–87). FORMAT 90/999(89–90), 주석·RETURN·END(91–93). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41–58: 재시작 파일명은 WQWCRST.BIN·WQWCRST.INP로 고정한다. 이 파일에는 ICIFN을 참조하는 문장이 없다.
- 48·65·76–83: 대형조류 입력 시 NWQV0는 NWQV+1이다. 상층 생물량 초기화는 IDNOTRVA 대신 상태변수 인덱스 22를 사용한다.
- 51·67–69: 재시작 입력 L/K는 배열 인덱스로 직접 사용한다. 이 파일에는 L/K 범위·중복·IOSTAT 검사가 없다.
- 59–63·89: XTIME=XTIME 자기 대입이 있다. FORMAT 90은 실행 READ에서 사용하지 않는다.
- 51·69·75–87: 이 파일은 WQV를 읽고 대형조류 상층 WQV를 0으로 설정한다. WQVO·엽록소·흡착 관련 보조 농도 대입은 없다.

