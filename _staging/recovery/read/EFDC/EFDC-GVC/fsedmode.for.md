---
file: models/EFDC/raw/source_code/EFDC-GVC/fsedmode.for
lines: 99
sha256: 5b82350fa1238681beb4c51265cbae726a270d7659d93f260e1147d016c38cd4
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# fsedmode.for — 판독 구간 기록

구간은 1행부터 99행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | 구분 주석과 `FUNCTION FSEDMODE(WS,USTOT,USGRN,RSNDM,ISNDM1,ISNDM2,IMODE)` 선언(1–6). 소류사(bedload)는 IMODE=1, 부유사(suspended load)는 IMODE=2라는 수송 비율 목적(8–9). `EFDC.PAR` 포함(11). 총 전단응력(total stress) 또는 입자 전단응력(grain stress)의 마찰속도(shear velocity) 선택 주석(13–14). `IF(WS.EQ.0)THEN  ! DSI` (16)이면 `FSEDMODE=1.0` (17), RETURN(18). 별도 `IF(ISNDM2.EQ.0)THEN` (20)은 USTOT를 US에 복사(21), `ELSE` (22)는 USGRN을 복사(23). 속도비 `USDWS=US/WS` (26), 옵션 선택 주석(28–29). |
| 30–49 | 시작 시 6행 FSEDMODE 함수 안. 옵션 0은 두 수송 비율을 독립적으로 최대화한다는 주석(30–32). 조건과 기본값 `IF(ISNDM1.EQ.0) FSEDMODE=1.0` (34). 옵션 1의 이진 관계(binary relationship) 설명(36–39). `IF(ISNDM1.EQ.1)THEN` (41) 안에서 `FSEDMODE=0.` (42). 내부 `IF(IMODE.EQ.1)THEN` (43)은 `FSEDMODE=1.0` (44), `ELSE` (45)는 `IF(USDWS.GE.RSNDM)FSEDMODE=1.` (46). 조건 종료(47–48). |
| 50–65 | 시작 시 6행 FSEDMODE 함수 안. 옵션 2는 소류사 비율 1·부유사 선형 관계(linear relationship)라는 주석(50–53). `IF(ISNDM1.EQ.2)THEN` (55), 내부 `IF(IMODE.EQ.1)THEN` (56)은 `FSEDMODE=1.0` (57). `ELSE` (58) 안에서 `TMPVAL=((USDWS)-0.4)/9.6` (59), `TMPVAL=MIN(TMPVAL,1.0)` (60), `TMPVAL=MAX(TMPVAL,0.0)` (61), 반환값 TMPVAL 복사(62). 선형 값을 0..1로 제한한다. 조건 종료(63–64). |
| 66–81 | 시작 시 6행 FSEDMODE 함수 안. 옵션 3은 두 수송을 이진 관계로 나누고 동시 수송을 하지 않는다는 주석(66–71). `IF(ISNDM1.EQ.3)THEN` (73) 안에서 `FSEDMODE=0.` (74). 내부 `IF(IMODE.EQ.1)THEN` (75)의 식 `IF(USDWS.LT.RSNDM)FSEDMODE=1.` (76). `ELSE` (77)의 식 `IF(USDWS.GE.RSNDM)FSEDMODE=1.` (78). 조건 종료(79–80). |
| 82–99 | 시작 시 6행 FSEDMODE 함수 안. 옵션 4는 선형 부유사 비율로 전체 수송을 나누어 두 비율 합을 1로 만든다는 주석(82–85). `IF(ISNDM1.EQ.4)THEN` (87) 안에서 `TMPVAL=((USDWS)-0.4)/9.6` (88), `TMPVAL=MIN(TMPVAL,1.0)` (89), `TMPVAL=MAX(TMPVAL,0.0)` (90). 내부 `IF(IMODE.EQ.1)THEN` (91)은 `FSEDMODE=1.-TMPVAL` (92), `ELSE` (93)는 TMPVAL 복사(94). 조건 종료·RETURN·END(95–99). 외부 루틴 CALL 문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–18: WS=0이면 ISNDM1·ISNDM2·IMODE 검사 전에 반환값을 1로 설정한다.
- 34–96: WS가 0이 아닌 경로의 반환값 대입은 ISNDM1=0..4 조건 안에만 있다. 이 범위 밖 옵션의 기본 반환값 대입은 없다.
- 43–47·56–63·75–79·91–95: IMODE=1만 별도로 검사한다. ELSE는 IMODE=2 여부를 추가로 검사하지 않는다.
- 59–61·88–90: 두 선형 옵션은 0.4와 9.6을 고정 계수로 쓴다. 두 선형 블록에는 RSNDM 참조가 없다.
