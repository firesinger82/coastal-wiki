---
file: models/EFDC/raw/source_code/EFDC-GVC/calebi.for
lines: 55
sha256: 5aa158b328f5f0591594bfd2c74001d51634d9bf3ab0bf8697d4be9440514da0
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calebi.for — 판독 구간 기록

구간은 1행부터 55행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | 구분·빈 주석과 `SUBROUTINE CALEBI` 선언(6). EFDC-FULL 1.0a·최종 수정·빈 변경 기록(8–17). 목적 주석은 외부 부력 적분(external buoyancy integral) 계산을 적는다(19). `EFDC.PAR`·`EFDC.CMN`을 포함한다(23–24). CH(LCM,KCM) 지역 DIMENSION 문은 주석이다(25). 구분·빈 주석을 포함한다. |
| 29–44 | 시작 시 6행 CALEBI 루틴 안. L=2..LA의 BI1/BI2를 0으로 초기화한다(29–31). 최상층 누적값과 외부 부력값은 `CH(L,KC)=DZC(KC)*B(L,KC)` (32); `BE(L)=GP*DZC(KC)*B(L,KC)` (33). `IF(KC.GT.1)THEN` (36)이면 `DO K=KS,1,-1` (37)·L=2..LA(38)에서 `CH(L,K)=CH(L,K+1)+DZC(K)*B(L,K)` (39); `BE(L)=BE(L)+GP*DZC(K)*B(L,K)` (40)으로 위층 값을 누적한다. 두 루프와 KC 조건 종료(41–43), 주석(44). |
| 45–51 | 시작 시 6행 CALEBI 루틴 안. K=1..KC·L=2..LA(45–46)의 두 부력 적분을 누적한다. 원문은 `BI1(L)=BI1(L)+GP*DZC(K)*(CH(L,K)-0.5*DZC(K)*B(L,K))` (47); `BI2(L)=BI2(L)+GP*DZC(K)*(CH(L,K)+Z(K-1)*B(L,K))` (48). BI1은 층 내 0.5*DZC*B 항을 빼고 BI2는 Z(K−1)*B 항을 더한다. 두 루프 종료(49–50)와 주석(51). |
| 52–55 | 시작 시 6행 CALEBI 루틴 안. 구분·빈 주석(52–53), RETURN(54), END(55). 이 파일에는 다른 루틴 CALL 문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
