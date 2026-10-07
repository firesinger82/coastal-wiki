---
file: models/EFDC/raw/source_code/EFDC-GVC/wqzero.for
lines: 86
sha256: 171d026558e73e5b81689fa3c1c11bd1149a3730c0b311ebff067f378f361101
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# wqzero.for — 판독 구간 기록

구간은 1행부터 86행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | `WQZERO` 시작(6). 수질 평균용 누적 배열(water quality averaging summation arrays)을 초기화한다는 목적과 작성·수정 날짜, EFDC-FULL 버전, 변경 기록 틀을 적는다(10–27). `EFDC.PAR`·`EFDC.CMN`을 포함한다(29–30). |
| 32–51 | 시작 시 6행 WQZERO 루틴 안. 출력 지점 M 루프와 LWQTS 참조는 주석이다(32·35). 실행 루프는 셀 LL=2..LA·층 K=1..KC·상태 NW=1..NWQV이다(33–36). WQVSUM·WQVMAX는 0, WQVMIN은 9.99E+21로 초기화한다(37–40). TOCWQSUM·PO4DWQSUM·SADWQSUM·TPWQSUM·TNWQSUM·TSIWQSUM·BOD5SUM·CHLMSUM·POCSUM·POPSUM·PONSUM을 0으로 둔다(41–51). 원문 조건·계산식·반복·호출: `DO LL=2,LA` (33), `DO K=1,KC` (34), `DO NW=1,NWQV` (36), `WQVSUM(LL,K,NW) = 0.0` (37), `WQVMIN(LL,K,NW) = 9.99E+21` (38), `WQVMAX(LL,K,NW) = 0.0` (39), `TOCWQSUM(LL,K) = 0.0` (41), `PO4DWQSUM(LL,K) = 0.0` (42), `SADWQSUM(LL,K) = 0.0` (43), `TPWQSUM(LL,K) = 0.0` (44), `TNWQSUM(LL,K) = 0.0` (45), `TSIWQSUM(LL,K) = 0.0` (46), `BOD5SUM(LL,K) = 0.0` (47), `CHLMSUM(LL,K) = 0.0` (48), `POCSUM(LL,K) = 0.0` (49), `POPSUM(LL,K) = 0.0` (50), `PONSUM(LL,K) = 0.0` (51). |
| 52–81 | 시작 시 6행 WQZERO 루틴·33행 LL 루프·34행 K 루프 안. TOCWQ·TNWQ·TPWQ·SADWQ·POC·POP·PON·CHLM의 최소/최대 배열을 각각 9.99E+21/0으로 둔다(52–67). 염분(salinity)·수온(water temperature)·TSS·광 소멸(light extinction) 계열의 합은 0, 최소는 9.99E+21, 최대는 0으로 둔다(68–79). 셀·층 루프를 닫는다(80–81). TSS와 그 밖의 배열 약어는 원문 이름이다. 원문 조건·계산식·반복·호출: `TOCWQMIN(LL,K) = 9.99E+21` (52), `TOCWQMAX(LL,K) = 0.0` (53), `TNWQMIN(LL,K) = 9.99E+21` (54), `TNWQMAX(LL,K) = 0.0` (55), `TPWQMIN(LL,K) = 9.99E+21` (56), `TPWQMAX(LL,K) = 0.0` (57), `SADWQMIN(LL,K) = 9.99E+21` (58), `SADWQMAX(LL,K) = 0.0` (59), `POCMIN(LL,K) = 9.99E+21` (60), `POCMAX(LL,K) = 0.0` (61), `POPMIN(LL,K) = 9.99E+21` (62), `POPMAX(LL,K) = 0.0` (63), `PONMIN(LL,K) = 9.99E+21` (64), `PONMAX(LL,K) = 0.0` (65), `CHLMMIN(LL,K) = 9.99E+21` (66), `CHLMMAX(LL,K) = 0.0` (67), `SALSUM(LL,K) = 0.0` (68), `SALMN(LL,K) = 9.99E+21` (69), `SALMX(LL,K) = 0.0` (70), `WQTEMSUM(LL,K) = 0.0` (71), `WQTEMMIN(LL,K) = 9.99E+21` (72), `WQTEMMAX(LL,K) = 0.0` (73), `TSSSUM(LL,K) = 0.0` (74), `TSSMN(LL,K) = 9.99E+21` (75), `TSSMX(LL,K) = 0.0` (76), `WQKETSUM(LL,K) = 0.0` (77), `WQKETMN(LL,K) = 9.99E+21` (78), `WQKETMX(LL,K) = 0.0` (79). |
| 82–86 | 시작 시 6행 WQZERO 루틴 안. TIMESUM=0·NWQCNT=0으로 시간 합과 누적 횟수를 초기화한다(82–83). 빈 주석·RETURN·END를 포함한다(84–86). 원문 조건·계산식·반복·호출: `TIMESUM = 0.0` (82), `NWQCNT = 0` (83). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 33–35: 출력 지점 수 IWQTS·LWQTS를 쓰는 루프는 주석이며, 실행 초기화는 전체 셀 2..LA에 적용된다.
- 38–39·52–79: 최소 배열의 초기값은 고정 9.99E+21이고, 최대 배열의 초기값은 모두 0이다. 수온 WQTEMMAX도 0으로 초기화한다(73).
