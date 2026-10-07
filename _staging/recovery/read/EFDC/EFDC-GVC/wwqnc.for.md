---
file: models/EFDC/raw/source_code/EFDC-GVC/wwqnc.for
lines: 60
sha256: dc25b2f0afd51deddd30e9c6a54ce8d9c7831475e59f036f1aa6910017e1f471
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# wwqnc.for — 판독 구간 기록

구간은 1행부터 60행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | `WWQNC` 시작(6). 수정 날짜·버전·변경 기록 틀을 적는다(10–24). 음수 수질 상태 변수(negative water quality state variable) 정보를 IWQONC 장치에 쓴다는 주석(26). `EFDC.PAR`·`EFDC.CMN`을 포함한다(30–31). NWQVM 크기의 CHARACTER*5 WQVN을 선언한다(33). |
| 35–43 | 시작 시 6행 WWQNC 루틴 안. IWQNC=1에서만 NCOFN 파일을 장치 1의 추가 모드로 연다(35–37). DATA 목록은 BC·BD·BG·RPOC·LPOC·DOC·RPOP·LPOP·DOP·PO4T·RPON·LPON·DON·NH4·NO3·SU·SA·COD·O2·TAM·FCB·MALG의 22개 상태명을 고정 문자열로 정의한다(39–42). DATA는 초기 데이터 정의문이다. 원문 조건·계산식·반복·호출: `IF(IWQNC.EQ.1)THEN` (35), `DATA WQVN/` (39), `* 'BC   ','BD   ','BG   ','RPOC ','LPOC ','DOC  ','RPOP ','LPOP ',` (40), `* 'DOP  ','PO4T ','RPON ','LPON ','DON  ','NH4  ','NO3  ','SU   ',` (41), `* 'SA   ','COD  ','O2   ','TAM  ','FCB  ','MALG '/` (42). |
| 44–55 | 시작 시 6행 WWQNC 루틴·35행 IF 참 분기 안. 셀 L=2..LA·층 K=1..KC·상태 NW=1..NWQV 루프를 순회한다(44–46). WQV(L,K,NW)<0일 때만 WQVN·ITNWQ·L·I·J·K·값을 출력한다(47–48). 세 루프·파일·IWQNC 조건을 닫는다(49–55). 상태 값을 수정하는 대입은 이 출력 루프에 없다. 원문 조건·계산식·반복·호출: `DO L=2,LA` (44), `DO K=1,KC` (45), `DO NW=1,NWQV` (46), `IF(WQV(L,K,NW).LT.0.0) WRITE(1,90) WQVN(NW),` (47), `*        ITNWQ,L,IL(L),JL(L),K,WQV(L,K,NW)` (48). |
| 56–60 | 시작 시 6행 WWQNC 루틴 안. 음수 상태 출력 FORMAT은 A5/I8/4I5/E11.3이다(57). 빈 주석·RETURN·END를 포함한다(56–60). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26·37·47·53: 주석은 장치 IWQONC를 적지만 실행 OPEN·WRITE·CLOSE는 장치 1을 사용한다.
- 33·39–42·46–47: WQVN 배열 크기는 NWQVM이며 DATA의 상태명은 고정 22개이다. 실행 출력 루프의 범위는 NWQV이고 이 블록에는 상태명 개수와의 일치 검사가 없다.
