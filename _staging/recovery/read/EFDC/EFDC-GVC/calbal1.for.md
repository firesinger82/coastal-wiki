---
file: models/EFDC/raw/source_code/EFDC-GVC/calbal1.for
lines: 92
sha256: 3e8686930e706262534999bdae0e18d41de6c2242d83a59f713716a67f3a15a4
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calbal1.for — 판독 구간 기록

구간은 1행부터 92행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | 구분 주석과 `SUBROUTINE CALBAL1` (6) 입구. 버전·수정일·변경 이력 머리말이다(8–17). 체적(volume)·질량(mass)·운동량(momentum)·에너지(energy) 수지를 계산한다는 주석이다(19–20). `INCLUDE 'EFDC.PAR'` (24); `INCLUDE 'EFDC.CMN'` (25)로 공통 선언을 포함한다. |
| 29–57 | 시작 시 6행 CALBAL1 루틴 안. `IF(NBAL.GT.1) RETURN` (29)이면 초기화 전에 반환한다. 33–34행은 초기 체적·염 질량(salt mass)·염료 질량(dye mass)·운동량·운동에너지(kinetic energy)·위치에너지(potential energy)와 관련 유량(flux) 초기화 주석이다. VOLBEG·SALBEG·DYEBEG·UMOBEG·VMOBEG·UUEBEG·VVEBEG·PPEBEG·BBEBEG를 0으로 초기화한다(38–46). VOLOUT·SALOUT·DYEOUT·UMOOUT·VMOOUT·UUEOUT·VVEOUT·PPEOUT·BBEOUT를 0으로 초기화한다(48–56). |
| 58–70 | 시작 시 6행 CALBAL1 루틴 안. L=2..LA 루프(58)에서 LN=LNC(L)로 북쪽 이웃을 얻는다(59). 체적 합산은 `VOLBEG=VOLBEG+SPB(L)*DXYP(L)*HP(L)` (60). 수평 운동량 합산은 `UMOBEG=UMOBEG+SPB(L)*0.5*DXYP(L)*HP(L)*(DYIU(L)*HUI(L)*UHDYE(L)` (61); `&                                 +DYIU(L+1)*HUI(L+1)*UHDYE(L+1))` (62); `VMOBEG=VMOBEG+SPB(L)*0.5*DXYP(L)*HP(L)*(DXIV(L)*HVI(L)*VHDXE(L)` (63); `&                                 +DXIV(LN)*HVI(LN)*VHDXE(LN))` (64). PPEBEG 위치에너지는 `PPEBEG=PPEBEG+SPB(L)*0.5*DXYP(L)` (65); `&             *(GI*P(L)*P(L)-G*BELV(L)*BELV(L))` (66). 루프 종료 뒤 합 운동량 크기는 `AMOBEG=SQRT(UMOBEG*UMOBEG+VMOBEG*VMOBEG)` (69). |
| 71–92 | 시작 시 6행 CALBAL1 루틴 안. K=1..KC·L=2..LA(71–72), LN=LNC(L)(73)로 북쪽 이웃을 얻는다. SALBEG·DYEBEG 합산은 `SALBEG=SALBEG+SCB(L)*DXYP(L)*HP(L)*SAL(L,K)*DZC(K)` (74); `DYEBEG=DYEBEG+SCB(L)*DXYP(L)*HP(L)*DYE(L,K)*DZC(K)` (75). 76–79행의 면별 운동에너지 대체식은 주석이다. 실행 수평 운동에너지·밀도 관련 위치에너지 합산은 `UUEBEG=UUEBEG+SPB(L)*0.125*DXYP(L)*HP(L)*DZC(K)` (80); `&      *( (U(L,K)+U(L+1,K))*(U(L,K)+U(L+1,K)) )` (81); `VVEBEG=VVEBEG+SPB(L)*0.125*DXYP(L)*HP(L)*DZC(K)` (82); `&      *( (V(L,K)+V(LN,K))*(V(L,K)+V(LN,K)) )` (83); `BBEBEG=BBEBEG+SPB(L)*GP*DXYP(L)*HP(L)*DZC(K)*( BELV(L)` (84); `&      +0.5*HP(L)*(Z(K)+Z(K-1)) )*B(L,K)` (85). 두 루프를 닫고 RETURN·END로 종료한다(86–92). 실행 CALL 문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 29·38–56: NBAL>1이면 누적량·초기량을 0으로 설정하는 구간 전에 반환한다.
- 60–66·74–85: 체적·운동량·에너지 합산에는 SPB를 곱한다. SALBEG·DYEBEG 합산에는 SCB를 곱한다.
- 76–83: 면별 속도 제곱을 따로 합하는 0.25 식은 주석이다. 실행 운동에너지 식은 두 면 속도의 합을 제곱하여 0.125를 곱한다.
