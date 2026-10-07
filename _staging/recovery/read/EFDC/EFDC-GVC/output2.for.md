---
file: models/EFDC/raw/source_code/EFDC-GVC/output2.for
lines: 174
sha256: 5f2332718d633fef6d6277c795e806e5fd2007b4c8663ab05c015ef32f02ccc0
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# output2.for — 판독 구간 기록

구간은 1행부터 174행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | 구분 주석과 `SUBROUTINE OUTPUT2` 입구(1–6). EFDC-FULL 1.0a·수정일·변경 이력 주석(8–17). `INCLUDE 'EFDC.PAR'`·`INCLUDE 'EFDC.CMN'` (21–22). 구분 주석도 포함한다(23–25). 포함 파일 내부는 판독하지 않았다. |
| 26–57 | 시작 시 6행 OUTPUT2 안. 완화 해법(relaxation solution) 결과 머리말(26). 단위 7에 RP·GLOBAL SQUARED ERROR 제목·ERRMAX/ERRMIN을 쓴다(28–35). N=1..NTS를 10 간격으로 순회하여 ERR 배열을 쓰는 루프는 주석이다(37–39). 다시 RP·ITERATIONS TO CONVERGENCE 제목·ITRMAX/ITRMIN을 쓴다(42–47). ITR 배열 출력 루프도 주석이다(49–51). FORMAT 20/21/30 및 구분 주석을 포함한다(40·52–57). |
| 58–72 | 시작 시 6행 OUTPUT2 안. 조화 분석(harmonic analysis) 머리말(58–61). L=2..LA 루프(62)에서 `PAM(L)=(AMCP(L)*AMCP(L)+AMSP(L)*AMSP(L))**.5` (63)로 진폭(amplitude)을 계산한다. `IF(AMSP(L).EQ.0.0.AND.AMCP(L).EQ.0.0)THEN` (64)이면 `PPH(L)=999999.` (65). `ELSE` (66)는 `PPH(L)=ATAN2(AMSP(L),AMCP(L))` (67)로 위상(phase)을 계산한다. 조건·루프를 닫고 구분 주석으로 끝난다(68–72). |
| 73–92 | 시작 시 6행 OUTPUT2 안. L 루프의 `PAM(L)=PAM(L)*GI` (74)로 진폭 출력값을 바꾼다. 제목 뒤 `CALL PPLOT (1)` (77)을 실행하며 FORMAT은 조석 수면 변위(tidal surface displacement) 진폭의 단위를 METERS로 적는다(79). 별도 L 루프의 위상 출력 식은 `PAM(L)=0.5*TIDALP*PPH(L)/PI` (84). 제목 뒤 `CALL PPLOT (1)` (87)을 실행하며 위상 FORMAT의 단위는 SEC이다(89). 구분 주석을 포함한다(90–92). |
| 93–123 | 시작 시 6행 OUTPUT2 안. X·Y 조석 속도(tidal velocity) 진폭의 층 루프·PAM 식·제목·PPLOT(2)·FORMAT은 모두 주석이다(93–120). 주석 식은 `C     PAM(L)=SQRT(AMCU(L,KK)*AMCU(L,KK)` (96), `C    &               +AMSU(L,KK)*AMSU(L,KK))` (97), `C     PAM(L)=SQRT(AMCV(L,KK)*AMCV(L,KK)` (112), `C    &               +AMSV(L,KK)*AMSV(L,KK))` (113). Y 블록은 LN=LNC(L) 주석 대입도 포함한다(111). 구분 주석으로 끝난다(121–123). |
| 124–141 | 시작 시 6행 OUTPUT2 안. P/U/V 진폭 출력 머리말과 단위 7의 표 제목·L 루프·PAM/PPH/U/V 기록은 주석이다(124–131). FORMAT 72는 실행 가능한 형식 선언으로 남아 있다(132). 벡터 퍼텐셜(vector potential) 수송 속도 머리말(136) 뒤 조건 `C     IF(ISVPTHA.NE.1) GOTO 100` (138)은 주석이다. 구분 주석도 포함한다(133–141). |
| 142–155 | 시작 시 6행 OUTPUT2 안. X 벡터 퍼텐셜 속도의 KK/L 루프와 PPLOT(2) 호출은 주석이다(142–150). 주석 식은 `C     PAM(L)=0.5*(UVPT(L,KK)+UVPT(L+1,KK))/HMU(L)` (145). FORMAT 1458은 X 방향·M/S·층 제목으로 남아 있다(152). 구분 주석을 포함한다(153–155). |
| 156–174 | 시작 시 6행 OUTPUT2 안. Y 벡터 퍼텐셜 속도의 KK/L 루프·LN 대입·PPLOT(2)는 주석이다(156–165). 주석 식은 `C     PAM(L)=0.5*(VVPT(L,KK)+VVPT(LN,KK))/HMV(L)` (160). FORMAT 1459는 Y 방향·M/S·층 제목으로 남아 있다(167). 구분 주석·100 CONTINUE·RETURN·END로 끝난다(168–174). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 64–67·83–87: 두 조화 계수가 0인 셀의 PPH는 999999.이다. 위상 출력 루프는 이 값을 별도 조건 없이 TIDALP/(2·PI)로 변환한다.
- 28·42: 같은 호출 안에서 RP를 FORMAT 40으로 두 번 출력한다.
- 40·52·54·132·152·167: FORMAT 20/21/30/72/1458/1459는 선언되어 있다. 이 파일의 실행 가능한 READ/WRITE 문장은 이 형식들을 참조하지 않는다.
