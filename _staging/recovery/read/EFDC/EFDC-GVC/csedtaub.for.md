---
file: models/EFDC/raw/source_code/EFDC-GVC/csedtaub.for
lines: 55
sha256: 11abc48c4d9a3c65d2b3b1ed8322ba6fbec2ae9e63cf949eb95959398561a04e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# csedtaub.for — 판독 구간 기록

구간은 1행부터 55행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | 구분 주석과 `REAL FUNCTION CSEDTAUB(DENBULK,TDUM,V1,V2,V3,IOPT)` (6) 선언. EFDC-FULL 1.0a·2001-11-01 수정 표기, 빈 변경 이력 양식(8–17), EFDC.PAR 포함(19). 바닥 체적 밀도(bed bulk density)에 따른 응집성 퇴적물(cohesive sediment)의 전체·질량 침식(bulk or mass erosion) 임계응력(critical stress) 계산 주석(21–22). 옵션 1과 2 모두 Hwang·Mehta 1989 문헌을 표기한다(24–34). |
| 36–44 | 시작 시 6행 CSEDTAUB 함수 안. `IF(IOPT.EQ.1)THEN` (36)에서 `DENBULK=0.001*DENBULK` (37), 내부 `IF(DENBULK.LE.1.013)THEN` (38)이면 `CSEDTAUB=0.0` (39). ELSE(40)는 `CSEDTAUB=0.001*(9.808*DENBULK-9.934)` (41). 두 ENDIF와 구분 주석(42–44). 변환된 DENBULK=1.013까지 반환값은 0이다. |
| 45–55 | 시작 시 6행 CSEDTAUB 함수 안. `IF(IOPT.EQ.2)THEN` (45)에서 `DENBULK=0.001*DENBULK` (46), 내부 `IF(DENBULK.LE.1.013)THEN` (47)이면 `CSEDTAUB=0.0` (48). ELSE(49)는 `CSEDTAUB=0.001*(9.808*DENBULK-9.934)` (50). 두 ENDIF·주석·RETURN·END(51–55). 호출문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 36–52: IOPT=1과 IOPT=2의 밀도 변환·임계값·반환식은 같다.
- 6·36–52: TDUM/V1/V2/V3는 인수 목록에만 등장한다. 두 옵션은 입력 인수 DENBULK 자체에 0.001*DENBULK를 대입한다.
- 36–54: 반환값 대입 경로는 IOPT=1 또는 IOPT=2이다. 다른 IOPT의 기본 반환값 대입은 없다.

