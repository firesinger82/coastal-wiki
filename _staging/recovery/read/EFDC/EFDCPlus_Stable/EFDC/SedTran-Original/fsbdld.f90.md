---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-Original/fsbdld.f90
lines: 54
sha256: e526b2b000682f7486061109139cd1cbe671b07509694378dbebb2cab5018e44
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# fsbdld.f90 — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | EFDC+·저작권·GPLv2 머리말(1–8). FSBDLD 함수 입구(9). 무차원 소류사(bedload) 수송계수 PHI를 계산한다는 주석(11–16). ISOPT=0은 상수, 1은 van Rijn 1984, 2는 수정 Engelund–Hansen, 3은 Wu 등으로 설명한다(12–15). implicit none·intent(IN) 인수·반환값·작업 실수를 선언한다(18–23). |
| 25–38 | 시작 시 9행 FSBDLD 안. ISOPT=0이면 사용자 SBDLDP를 반환한다(25–27). 병렬 elseif의 ISOPT=1은 van Rijn 1984 Part I를 출처로 적는다(29–33). DIASED·GPDIASED로 RD를 구하고 역수의 0.2승, CSHIELDS의 2.1승, 0.053 계수로 반환값을 계산한다(34–37). 조건·계산·호출 원문: `if( ISOPT == 0 )then` (25); `elseif( ISOPT == 1 )then` (29); `RD  = DIASED*SQRT(GPDIASED)*1.E6` (34); `RD  = (1./RD)**0.2` (35); `TMP = CSHIELDS**2.1` (36); `FSBDLD = 0.053*RD/TMP` (37). |
| 39–45 | 시작 시 9행 FSBDLD·25행 옵션 선택 블록 안. ISOPT=2는 수정 Engelund–Hansen 식이다(39–40). 주석은 참고문헌을 추가해야 한다고 적는다(41). DEP/D50의 0.33333승, 노출(exposure)/은폐(hiding) PEXP/PHID의 1.125승에 2.0367을 곱한다(42–44). 조건·계산·호출 원문: `elseif( ISOPT == 2 )then` (39); `TMP1   = (DEP/D50)**0.33333` (42); `TMP2   = (PEXP/PHID)**1.125` (43); `FSBDLD = 2.0367*TMP1*TMP2` (44). |
| 46–54 | 시작 시 9행 FSBDLD·25행 옵션 선택 블록 안. ISOPT=3은 Wu·Wang·Jia의 2000년 J. Hydr. Res. 문헌을 적는다(46–47). PHID/PEXP의 0.6승에 0.03을 곱하고 다시 2.2승으로 올린 뒤 0.0053을 나눈다(48–50). 선택 블록·함수 종료·마지막 빈 줄을 포함한다(51–54). 조건·계산·호출 원문: `elseif( ISOPT == 3 )then` (46); `TMP1   = 0.03*((PHID/PEXP)**0.6)` (48); `TMP2   = TMP1**2.2` (49); `FSBDLD = 0.0053/TMP2` (50). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 25–51: ISOPT=0..3 밖의 값을 처리하는 else나 반환값 기본 대입은 없다.
- 39–41: 옵션 2의 출처 주석은 REFERENCE TO BE ADDED 상태이다.
- 34–50: RD·CSHIELDS 기반 TMP·D50·PHID·PEXP·TMP2를 분모로 사용한다. 이 함수에는 해당 분모의 0 검사나 SQRT·거듭제곱 입력 범위 검사가 없다.

