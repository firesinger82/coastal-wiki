---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/csedvis.f90
lines: 36
sha256: 2b7f23f6a3505464346aded690c23c8790dcea8c8b4468191bfd5507a02d8a76
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# csedvis.f90 — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | EFDC+ 저작권·GPLv2·주소와 CSEDVIS(SED) 함수 입구(1–9). 주석은 고농도 점착성 퇴적물(cohesive sediment)·물 혼합물의 동점성계수(kinematic viscosity)를 계산한다고 적는다(14–15). 근거 문헌은 Mehta와 Jiang의 1990년 파랑에 의한 바닥 진흙 운동 관측이다(17–19). implicit none과 기본 REAL의 반환값·입력·보간 변수 선언을 포함한다(21–22). |
| 24–32 | 시작 시 9행 `FUNCTION CSEDVIS(SED)` 루틴 안. SED≤25667은 0.116883D−3×SED, SED≥36667은 1.52646D−6×SED+3.125로 VISR을 계산한다(24–25). 25667<SED<36667이면 폭 11000의 WTL/WTH 가중치를 만들고 양 끝 식의 VISL/VISH를 선형 보간(linear interpolation)한다(26–31). 세 조건은 독립 IF이며 중간 구간 조건을 32행에서 닫는다. 원문(조건·반복·대입·호출, 등장 순서): `if( SED <= 25667.) VISR = 0.116883D-3*SED` (24); `if( SED >= 36667.) VISR = 1.52646D-6*SED+3.125` (25); `if( SED > 25667.0 .and. SED < 36667.0 )then` (26); `WTL = (36667.-SED)/11000.` (27); `WTH = (SED-25667.)/11000.` (28); `VISL = 0.116883D-3*25667` (29); `VISH = 1.52646D-6*36667.+3.125` (30); `VISR = WTL*VISL+WTH*VISH` (31). |
| 33–36 | 시작 시 9행 `FUNCTION CSEDVIS(SED)` 루틴 안. 반환값은 1.D−6×10**VISR이다(33). 추가 루틴 호출은 없다. 빈 줄·END FUNCTION·마지막 빈 줄로 끝난다(34–36). 원문(조건·반복·대입·호출, 등장 순서): `CSEDVIS = 1.D-6*(10.**VISR)` (33). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22·24–33: 변수와 반환값은 KIND가 없는 REAL이다. 일부 계수는 D 지수 리터럴을 사용하고 가중치·10.**VISR의 밑은 기본 실수 리터럴을 사용한다.
- 24–33: SED의 하한을 별도로 검사하거나 값을 제한하는 문장은 없다. SED<=25667 조건은 음수 SED도 포함한다. VISR과 반환값에도 상한·하한 제한문은 없다.
