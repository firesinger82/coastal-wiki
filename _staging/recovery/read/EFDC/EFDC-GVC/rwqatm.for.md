---
file: models/EFDC/raw/source_code/EFDC-GVC/rwqatm.for
lines: 76
sha256: 6e744f4e568cce1d937a4dfc0cbf9143d84cc2fb4a8d41d8b0a30a8b04c55dd5
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# rwqatm.for — 판독 구간 기록

구간은 1행부터 76행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | 머리말과 `SUBROUTINE RWQATM` (6). 추가일·수정일·버전·변경 이력 주석(10–23). 목적 주석은 21개 상태변수(state variable)의 일정 농도와 각 격자셀의 강우 유입량을 곱해 대기 습식 침적(wet atmospheric deposition) 부하(load)를 g/day로 계산한다고 적는다(27–29). EFDC.PAR·EFDC.CMN 포함(32–33). 구분 주석 포함. 포함 파일 내부는 판독하지 않았다. |
| 35–47 | 시작 시 6행 RWQATM 안. 단위 주석은 WQATM=mg/L, RAINT=m/sec, DXYP=m², WQATML=g/day이다(36–40). `CV2=86400.0` (41). NW=1..NWQV·L=2..LA에서 `WQATML(L,KC,NW)=WQATM(NW)*RAINT(L)*DXYP(L)*CV2` (44)로 KC층 부하를 대입한다. 두 루프 종료·주석(45–47). 이 계산은 뒤의 진단 파일 조건 밖에 있다. |
| 48–68 | 시작 시 6행 RWQATM 안. `IF(ITNWQ.EQ.0)THEN` (48)이면 WQATM.DIA를 단위 1에서 열고 삭제 후 재개방한다(50–52). 이 안의 `IF(ISDYNSTP.EQ.0)THEN` (54)은 `TIME=(DT*FLOAT(N)+TCON*TBEGIN)/86400.` (55). `ELSE` (56)는 `TIME=TIMESEC/86400.` (57). N·TIME 기록(59). L=2..LA에서 IL·JL·WQATML(L,KC,1..NWQV)를 기록한다(61–63). 파일 CLOSE·ITNWQ 분기 종료·주석(65–68). |
| 69–76 | 시작 시 6행 RWQATM 안이며 진단 분기 밖. FORMAT 110은 2I4와 7E11.3을 세 행에 배치한다(69). FORMAT 112는 진단 제목·N·TIME의 I10·F12.5이다(70–71). 구분 주석·RETURN·END(72–76). 이 파일에는 서브루틴 CALL이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–29·42·62·69: 주석의 상태변수 수는 21이다. 실제 계산·출력 개수는 NWQV이며 FORMAT 110은 7개씩 세 행의 실수 서식을 둔다.
- 41·44·55·57: 하루 환산 계수는 86400.0으로 고정되어 있다. 진단 시간은 TCON이 아니라 86400으로 나눈다.
- 42–46: 이 루틴의 WQATML 대입은 KC층에만 있다. 그 밖의 층을 초기화하거나 대입하는 문장은 이 파일에 없다.
