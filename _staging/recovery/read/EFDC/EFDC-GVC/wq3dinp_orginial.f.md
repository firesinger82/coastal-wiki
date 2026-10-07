---
file: models/EFDC/raw/source_code/EFDC-GVC/wq3dinp_orginial.f
lines: 258
sha256: ff229270b59e8c49fbac726fb5e76d6d588dd1fe07fa91480d7fd51ee4e7ce33
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# wq3dinp_orginial.f — 판독 구간 기록

구간은 1행부터 258행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | 머리말·구분 주석(1–5), `SUBROUTINE WQ3DINP` 입구(6). 수질 하위 모델(water quality submodel) 입력 파일을 읽는다는 주석과 작성자·수정일·EFDC-FULL 1.0a 표기(7–30). `INCLUDE 'EFDC.PAR'` (31), `INCLUDE 'EFDC.CMN'` (32). 헤더 배열 `CHARACTER*3 CWQHDR(NWQVM)` (34)과 시간 문자열 `CHARACTER*11  HHMMSS` (36) 선언, 빈 주석(37). 포함 파일 내부는 이 파일의 판독 대상이 아니다. |
| 38–62 | 시작 시 6행 WQ3DINP 루틴 안. 기본값 원문은 `DATA IWQTICI,IWQTAGR,IWQTSTL,IWQTSUN,IWQTBEN,IWQTPSL,IWQTNPL/7*0/` (38), `DATA ISMTICI/0/` (39). 같은 변수들을 자신에게 대입한다(40–47). WQWCTS.OUT 삭제 문장은 주석 처리되어 있다(49–50). WQ3D.OUT은 STATUS='UNKNOWN'으로 열고 STATUS='DELETE'로 닫는다(52–53). 속도 계수 지도(rate coefficient map) 우회라는 주석(55), ISWQCMAP·ISWQSMAP의 0 대입은 주석이다(57–58). `NWQKCNT=0` (60), `NWQKDPT=1` (61). |
| 63–80 | 시작 시 6행 WQ3DINP 루틴 안. UHEQ의 1·LC 인덱스를 0으로 초기화한다(63–64). `DO ND=1,NDMWQ` (65)에서 `LF=2+(ND-1)*LDMWQ` (66), `LL=LF+LDM-1` (67)을 계산한다. `DO L=LF,LL` (68)에서 UHEQ(L)=1.0으로 설정한다(69). 루프 종료(70–71). TINDAY=0.0·ITNWQ=0 초기화와 TINDAY 자기 대입(73–75). 수직층 역수는 `RKCWQ = 1.0/REAL(KC)` (77). `DO K=1,KC` (78)에서 `WQHT(K)=REAL(KC-K)*RKCWQ` (79), 루프 종료(80). |
| 81–135 | 시작 시 6행 WQ3DINP 루틴 안. 파일 단위 번호 대입은 CXH 주석이다(82–91). 이전 수질 변수 이름 21개는 주석 처리되어 있다(93–113). 실행되는 WQTSNAME(1:21) 문자열 대입은 순서대로 CHC·CHG·CHD·ROC·LOC·DOC·P4D·ROP·LOP·DOP·RON·LON·DON·NHX·NOX·SUU·SAA·COD·DOX·TAM·FCB이다(115–135). |
| 136–171 | 시작 시 6행 WQ3DINP 루틴 안. `DO M=0,NWQPS` (137), 그 안 `DO J=1,NWQV` (140)에서 WQPSQ·WQPSQC·WQWPSLC를 0으로 초기화한다(138–143). `DO K=1,KC` (145)에서 IWQPSC·WQDSQ의 1·LC 경계 인덱스를 0으로 초기화한다(146–150). `DO ND=1,NDMWQ` (152)에서 `LF=2+(ND-1)*LDMWQ` (153), `LL=LF+LDM-1` (154). 그 안 `DO K=1,KC` (155), `DO L=LF,LL` (156)에서 IWQPSC·IWQPSV·WQDSQ를 0으로 초기화한다(157–162). `DO J=1,NWQV` (164), `DO K=1,KC` (165), `DO L=1,LC` (166)에서 분포 부하(distributed load) WQWDSL·점 부하(point source load) WQWPSL을 0으로 초기화한다(167–171). |
| 172–205 | 시작 시 6행 WQ3DINP 루틴 안. `CALL RWQC1(IWQDT)` (173). RWQC2·RWQMAP 호출은 주석이다(174–175). WQWCTS.OUT을 열어 삭제하고 다시 연다(178–180). NWQVOUT=0으로 시작한다(182). `DO NW=1,NWQV` (183)에서 `IF(ISTRWQ(NW).EQ.1)THEN` (184)이면 `NWQVOUT=NWQVOUT+1` (185), 해당 WQTSNAME을 CWQHDR에 복사한다(186). 조건·루프 종료(187–188). 선택된 헤더를 1969 형식으로 출력한다(190). 실행 형식은 I·J·K·TIME 다음에 A3 필드 21개를 배치한다(192–195). 이전 고정 헤더 형식은 주석이다(197–202). 파일을 닫는다(204), 빈 주석(205). |
| 206–218 | 시작 시 6행 WQ3DINP 루틴 안. 일주기 용존산소(diurnal dissolved oxygen) 분석 초기화 주석(206–207). `IF(NDDOAVG.GE.1)THEN` (208)이면 DIURNDO.OUT을 열어 삭제한다(209–210). 그 안 `DO K=1,KC` (211), `DO L=2,LA` (212)에서 `DDOMAX(L,K)=-1.E6` (213), `DDOMIN(L,K)=1.E6` (214)로 극값 초기치를 설정한다. 루프·조건 종료 및 빈 주석(215–218). |
| 219–232 | 시작 시 6행 WQ3DINP 루틴 안. 광 감쇠(light extinction) 분석 초기화 주석(219–220). `IF(NDLTAVG.GE.1)THEN` (221)이면 LIGHT.OUT을 열어 삭제한다(222–223), NDLTCNT=0 초기화(224). 그 안 `DO K=1,KC` (225), `DO L=2,LA` (226)에서 RLIGHTT·RLIGHTC를 0으로 초기화한다(227–228). 루프·조건 종료 및 빈 주석(229–232). |
| 233–245 | 시작 시 6행 WQ3DINP 루틴 안. 수질 평균 합산 배열 초기화 주석(233–234)과 `CALL WQZERO` (235). `IF(IWQICI.EQ.2) CALL RWQRST` (237)는 재시작 입력(restart input) 호출이다. 별도 `IF(IWQBEN.EQ.1)THEN` (239)에서 `CALL SMINIT` (240), `CALL SMRIN1(IWQDT)` (241). SMRIN2·RSMMAP 호출은 주석이다(242–243). 같은 분기 안에서 `IF(ISMICI.EQ.2) CALL RSMRST` (244), 바깥 조건 종료(245). |
| 246–258 | 시작 시 6행 WQ3DINP 루틴 안. TFILE 열기·시간 취득·출력·삭제는 모두 주석 처리되어 있다(247–252). 실행 가능한 형식 문장 `100 FORMAT('  TIME = ',A11,' HH.MM.SS.HH')` (254)이 남아 있다. 다른 시간 형식은 주석이다(255). 빈 주석(246·253·256), RETURN·END로 루틴을 끝낸다(257–258). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 38–47·73–74: DATA로 초기화한 여덟 변수에는 자기 대입이 있다. TINDAY에도 0 대입 직후 자기 대입이 있다.
- 55–61: 속도 계수 지도 우회라는 주석 아래 ISWQCMAP=0·ISWQSMAP=0은 주석 처리되어 있다. 실행문은 NWQKCNT=0·NWQKDPT=1이다.
- 36·247–255: HHMMSS는 선언되어 있다. HHMMSS를 취득하거나 출력하는 문장은 모두 주석 처리되어 있다. 100 FORMAT 문장은 주석 밖에 남아 있다.
