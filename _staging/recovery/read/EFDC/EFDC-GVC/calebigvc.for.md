---
file: models/EFDC/raw/source_code/EFDC-GVC/calebigvc.for
lines: 91
sha256: 4cb5ae20fa5cc105f6f8f0d340058425471df2158b019ab8aaaff92df19a9453
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calebigvc.for — 판독 구간 기록

구간은 1행부터 91행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | 구분·빈 주석과 `SUBROUTINE CALEBIGVC` 선언(6). EFDC-FULL 1.0a·최종 수정·빈 변경 기록(8–17). 목적 주석은 CALEBI의 외부 부력 적분(external buoyancy integral) 계산이라고 적는다(19). `EFDC.PAR`·`EFDC.CMN`을 포함한다(23–24). CH(LCM,KCM) 지역 DIMENSION 문은 주석이다(25). 구분·빈 주석을 포함한다. |
| 29–53 | 시작 시 6행 CALEBIGVC 루틴 안. 이전 BI1/BI2/BE 계산 전체는 주석이다. L=2..LA의 BI1/BI2 초기화(29–31)와 최상층 주석 식 `C      CH(L,KC)=DZC(KC)*B(L,KC)` (32); `C      BE(L)=GP*DZC(KC)*B(L,KC)` (33). K=KS..1·L=2..LA의 주석 조건·누적식은 `C	 IF(K.GE.KGVCP(L))THEN` (38); `C        CH(L,K)=CH(L,K+1)+DZC(K)*B(L,K)` (39); `C        BE(L)=BE(L)+GP*DZC(K)*B(L,K)` (40). K=1..KC·L=2..LA의 주석 조건·적분식은 `C	 IF(K.GE.KGVCP(L))THEN` (47); `C        BI1(L)=BI1(L)+GP*DZC(K)*(CH(L,K)-0.5*DZC(K)*B(L,K))` (48); `C        BI2(L)=BI2(L)+GP*DZC(K)*(CH(L,K)+Z(K-1)*B(L,K))` (49). 해당 루프·조건 종료도 주석이며 실행되지 않는다(34·36–37·41–46·50–52). 빈 주석(35·44·53). |
| 54–66 | 시작 시 6행 CALEBIGVC 루틴 안. K=1..KC·L=2..LA의 BI1GVC/BI2GVC/BEGVC를 0으로 초기화한다(54–60). L=2..LA의 최상층 값은 `CH(L,KC)=DZC(KC)*B(L,KC)` (63); `BEGVC(L,KC)=GP*DZC(KC)*B(L,KC)` (64). 두 식은 KGVCP 조건 밖에서 실행된다. L 루프 종료(65)와 빈 주석(61·66). |
| 67–75 | 시작 시 6행 CALEBIGVC 루틴 안. `DO K=KS,1,-1` (67)·L=2..LA(68)에서 `IF(K.GE.KGVCP(L))THEN` (69)인 층만 누적한다. 원문은 `CH(L,K)=CH(L,K+1)+DZC(K)*B(L,K)` (70); `BEGVC(L,K)=BEGVC(L,K+1)+GP*DZC(K)*B(L,K)` (71). CH는 K+1층의 CH에 DZC*B를 더한다. BEGVC는 K+1층의 BEGVC에 GP*DZC*B를 더한다. 조건·두 루프 종료(72–74), 주석(75). |
| 76–91 | 시작 시 6행 CALEBIGVC 루틴 안. KBOT=1..KC(76)마다 K=KBOT..KC(77)·L=2..LA(78)를 반복한다. `IF(K.GE.KGVCP(L))THEN` (79)이면 해당 KBOT의 부력 적분을 누적한다. 원문은 `BI1GVC(L,KBOT)=BI1GVC(L,KBOT)` (80); `&        +GP*DZC(K)*(CH(L,K)-0.5*DZC(K)*B(L,K))` (81); `BI2GVC(L,KBOT)=BI2GVC(L,KBOT)+GP*DZC(K)*(CH(L,K)+Z(K-1)*B(L,K))` (82). 조건·L/K/KBOT 루프 종료(83–86). 구분·빈 주석(87–89), RETURN(90)·END(91). 이 파일에는 다른 루틴 CALL 문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·19: 실행 루틴 선언은 CALEBIGVC이다(6). 목적 주석의 루틴 이름은 CALEBI이다(19).
- 54–71: BI1GVC·BI2GVC·BEGVC는 K=1..KC에서 모두 0으로 초기화한다(54–60). CH는 최상층을 대입하고(63), 나머지 층은 K>=KGVCP(L) 조건에서만 대입한다(69–70). 이 루틴에는 CH 전체를 0으로 초기화하는 실행문이 없다.
- 76–83: KBOT 루프의 범위는 1..KC이다(76). 적분항 적용 조건은 K>=KGVCP(L)이다(79). 이 블록에는 KBOT>=KGVCP(L) 검사문이 없다.
