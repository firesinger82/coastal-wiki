---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Mapping/Calculate_Local_Shear.f90
lines: 86
sha256: 5f14c8a6a963ba2a662bb05458ac314041f9b911820bbf79c119d7e586b0a26d
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Calculate_Local_Shear.f90 — 판독 구간 기록

구간은 1행부터 86행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | EFDC+·저작권·GPLv2 머리말과 EE 출력에 필요한 지역 전단(shear) 선계산 목적·작성자·날짜 주석(1–16). `Calculate_Local_Shear`를 시작한다(18). GLOBAL·MPI·Variables_MPI·Variables_MPI_Mapping·Variables_MPI_Write_Out를 사용하고 implicit none·정수 L을 선언한다(20–29). 빈 줄을 포함한다. |
| 31–43 | 시작 시 18행 Calculate_Local_Shear 안. `if( ISTRAN(6) > 0 .or. ISTRAN(7) > 0 )then` (31)의 퇴적물 경로에서 `if( LSEDZLJ )then` (33). 주석은 TAU를 dynes/cm², WATERDENS를 gm/cm³로 적고 SHEAR를 물 밀도로 정규화한 m²/s²로 설명한다(34–35). L=2..LA에서 `if( LBED(L) )then` (37)은 `SHEAR_Local(L) = QQ(L,0)/CTURB2` (38). else(39)는 `SHEAR_Local(L) = TAU(L) * 0.1 / (WATERDENS*1000.)` (40). 셀 조건·루프 종료와 빈 줄(41–43). |
| 44–61 | 시작 시 18행 Calculate_Local_Shear·31행 퇴적물 참 분기·33행 방식 분기 안. `elseif( ISBEDSTR >= 1 )then` (44)은 L=2..LA에서 `if( LBED(L) )then` (46)일 때 `SHEAR_Local(L) = QQ(L,0)/CTURB2` (47), else에서는 TAUBSED(L)를 복사한다(48–49). 이 루프 뒤 `if( ISBEDSTR == 1 )then` (53)은 L=2..LA에서 `if( LBED(L) )then` (55)일 때 `SHEAR_Local2(L) = QQ(L,0)/CTURB2` (56), else에서 TAUBSND(L)를 복사한다(57–58). 내부 조건·루프 종료(59–61). |
| 62–72 | 시작 시 18행 Calculate_Local_Shear·31행 퇴적물 참 분기·33행 방식 분기 안. `else` (62)는 LSEDZLJ 불성립이고 ISBEDSTR>=1도 불성립한 경로이다. L=2..LA에서 `if( LBED(L) .OR. TIMEDAY < SEDSTART )then` (65)이면 `SHEAR_Local(L) = QQ(L,0)/CTURB2` (66), else에서는 TAUB(L)를 복사한다(67–68). 셀 조건·루프·방식 분기 종료와 빈 줄(69–72). |
| 73–86 | 시작 시 18행 Calculate_Local_Shear·31행 퇴적물 여부 분기 안. `else` (73)는 퇴적물 수송 조건 불성립 경로이다. `if( ISGOTM > 0 )then` (75)은 L=2..LA에서 `SHEAR_Local(L) = max(QQ(L,KSZ(L)-1),QQMIN)/CTURB2` (77). else(79)는 같은 범위에서 `SHEAR_Local(L) = max(QQ(L,0),QQMIN)/CTURB2` (81). 두 루프·조건 종료·빈 줄·루틴 종료(78–86). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 31–84: 이 루틴에는 SHEAR_Local·SHEAR_Local2 전체 초기화 문장이 없다. 모든 셀 대입의 루프 범위는 2..LA이다.
- 44–61: SHEAR_Local2의 대입은 퇴적물 경로에서 LSEDZLJ가 불성립하고 ISBEDSTR==1인 조건 안에만 있다.
- 38·47·56·66·77·81: 퇴적물 경로의 QQ/CTURB2 식에는 QQMIN 제한이 없다. 퇴적물 조건의 else 경로는 max(QQ,QQMIN)을 사용한다.
