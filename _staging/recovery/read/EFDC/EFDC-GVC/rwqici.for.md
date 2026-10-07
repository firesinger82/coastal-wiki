---
file: models/EFDC/raw/source_code/EFDC-GVC/rwqici.for
lines: 100
sha256: 5c8d9e7e550352a2493ecc7f05f07a8997e73b328d82efc90eb2df15e6dd357c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# rwqici.for — 판독 구간 기록

구간은 1행부터 100행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | 머리말·수정 이력(1–22). `SUBROUTINE RWQICI(IWQTICI)` (4)은 공간·시간 변동 초기조건(initial conditions) 판독이라는 주석(24). `INCLUDE 'EFDC.PAR'` (28), `INCLUDE 'EFDC.CMN'` (29), XWQV(NWQVM)와 TITLE(3)·ICICONT 선언(31–32). 포함 파일 내부는 판독 대상에 포함하지 않았다. |
| 34–60 | 시작 시 4행 RWQICI 루틴 안. 단위 1 ICIFN, 단위 2 WQ3D.OUT append로 연다(34–35). `IF(IWQTICI.EQ.0)THEN` (37)이면 제목 3줄을 읽고 출력(38–41). 초기조건 적용 일자 로그(43–44). 빈 줄과 제목 1줄 판독·출력(46–48), `DO M=2,LA` (49)에서 I/J/K 및 XWQV(1..NWQV)를 읽는다(50). `IF(IJCT(I,J).LT.1 .OR. IJCT(I,J).GT.8)THEN` (51)이면 I/J/K/M-1 출력과 STOP(52–54). L=LIJ(I,J), NW=1..NWQV에서 WQV(L,K,NW)=XWQV(NW) 복사·출력(55–59), M 루프 종료(60). |
| 61–82 | 시작 시 4행 RWQICI 루틴 안. 엽록소(chlorophyll) 비의 역수 주석(62). L=2..LA·K=1..KC 루프(64–65)에서 `WQCHL(L,K) = WQV(L,K,1)*WQCHLC + WQV(L,K,2)*WQCHLD` (66), 연속행 `*      + WQV(L,K,3)*WQCHLG` (67). `IF(IWQSRP.EQ.1)THEN` (68)이면 총 활성 금속(total active metal, TAM)을 사용하여 `O2WQ = MAX(WQV(L,K,19), 0.0)` (69), `WQTAMD = MIN( WQTAMDMX*EXP(-WQKDOTAM*O2WQ), WQV(L,K,20) )` (70), `WQTAMP(L,K) = WQV(L,K,20) - WQTAMD` (71), `WQPO4D(L,K) = WQV(L,K,10) / (1.0 + WQKPO4P*WQTAMP(L,K))` (72), `WQSAD(L,K)  = WQV(L,K,17) / (1.0 + WQKSAP*WQTAMP(L,K))` (73). `ELSE IF(IWQSRP.EQ.2)THEN` (74)이면 총 부유물질(total suspended solids) SEDT를 사용하여 `WQPO4D(L,K) = WQV(L,K,10) / (1.0 + WQKPO4P*SEDT(L,K))` (75), `WQSAD(L,K)  = WQV(L,K,17) / (1.0 + WQKSAP*SEDT(L,K))` (76). else는 총 농도를 용존 인산염(phosphate)·규소(silica) 농도에 복사(77–79). 조건·루프 종료(80–82). |
| 83–100 | 시작 시 4행 RWQICI 루틴 안. 다음 적용일 IWQTICI와 연속 입력 제어 ICICONT 판독·출력(84–85). `IF(ICICONT.EQ.'END')THEN` (86)이면 단위 1 닫기, `IWQICI = 0` (88)으로 입력 사용 종료(87–89). 단위 2 닫기(91). FORMAT 999/50/52/60/84(93–97), 84 형식은 3I5·21E12.4이다(97). 주석·RETURN·END(98–100). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 34·37–41·86–89: 매 호출 ICIFN을 OPEN한다. 첫 제목 판독은 IWQTICI=0일 때만 실행하고 단위 1 CLOSE는 ICICONT='END'일 때만 실행한다.
- 49–60·64–82: 입력 루프는 LA-1개 좌표·층 레코드를 읽는다. 이후 보조 농도 계산은 전체 KC개 층을 순회한다. 이 파일에는 입력 K 범위·중복 좌표·전체 셀/층 충족 여부 검사가 없다.
- 31–32: ICICONT는 길이 3으로 선언하며 END 문자열과 비교한다. 입력 FORMAT 84는 농도 21개로 고정한다(97).
- 56–58·68–80: 이 파일의 입력 대입은 WQV에만 한다. WQVO 대입은 없다. WQTAMP 대입은 IWQSRP=1 분기에만 있다.

