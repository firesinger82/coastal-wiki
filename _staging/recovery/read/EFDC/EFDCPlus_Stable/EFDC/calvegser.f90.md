---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calvegser.f90
lines: 69
sha256: ae3609e224063a3bcb2b73fe96fca42a0d4893d351248ea5bc4f963669d13414
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calvegser.f90 — 판독 구간 기록

구간은 1행부터 69행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | EFDC+ 저작권·GPLv2·참조 URL 머리말(1–8). CALVEGSER 시작(9). 주석은 시간 가변 식생 저항(vegetation resistance)의 계열 수·식생 분류별 계열 ID·보간 위치·시간 변환 계수와 RDLPSQ/BPVEG/HPVEG 값을 설명한다(11–24). GLOBAL 사용, implicit none 및 지역 정수·실수 선언을 포함한다(28–33). |
| 35–54 | 시작 시 9행 `SUBROUTINE CALVEGSER()` 루틴 안. NVEGSER>0에서 각 계열 NS를 순회한다(35–36). TIMESEC을 TCVEGSER로 나눈다(37). MVEGTLAST에서 시작해 TIME이 다음 TVEGSER보다 크면 M1을 한 칸 올리고 라벨 100으로 되돌아간다(39–44). ELSE에서 현재 보간 위치를 저장한다(45–47). 두 시각의 차와 선형 보간(linear interpolation) 가중치 WTM1/WTM2를 계산한다(48–50). 같은 가중치로 현재 RDLPSQ/BPVEG/HPVEG 계열 값을 만든다(51–53). 원문(조건·반복·대입·호출, 등장 순서): `if( NVEGSER > 0 )then` (35); `do NS = 1,NVEGSER` (36); `TIME = TIMESEC/TCVEGSER(NS)` (37); `M1 = MVEGTLAST(NS)` (39); `M2 = M1+1` (41); `if( TIME > TVEGSER(M2,NS) )then` (42); `M1 = M2` (43); `else` (45); `MVEGTLAST(NS) = M1` (46); `TDIFF = TVEGSER(M2,NS)-TVEGSER(M1,NS)` (48); `WTM1 = (TVEGSER(M2,NS)-TIME)/TDIFF` (49); `WTM2 = (TIME-TVEGSER(M1,NS))/TDIFF` (50); `VEGSERRT(NS) = WTM1*VEGSERR(M1,NS)+WTM2*VEGSERR(M2,NS)` (51); `VEGSERBT(NS) = WTM1*VEGSERB(M1,NS)+WTM2*VEGSERB(M2,NS)` (52); `VEGSERHT(NS) = WTM1*VEGSERH(M1,NS)+WTM2*VEGSERH(M2,NS)` (53). |
| 55–69 | 시작 시 9행 `SUBROUTINE CALVEGSER()` 루틴·35행 `if( NVEGSER > 0 )then` 분기 안. 식생 분류 M=1..MVEGTYP에서 NVEGSERV(M)>0인 분류만 갱신한다(55–57). 보간한 RDLPSQ/BPVEG/HPVEG를 복사한다(58–60). BPVEG²×RDLPSQ를 BDLTMP로 계산하며 주석 단위는 무차원 개체 밀도(population density)다(61). PVEGZ=1−ALPVEG×BDLTMP와 BDLPSQ=BPVEG×RDLPSQ를 계산한다(62–63). 분류 루프·NVEGSER 분기·RETURN·END 및 마지막 빈 줄을 포함한다(64–69). 원문(조건·반복·대입·호출, 등장 순서): `do M = 1,MVEGTYP` (55); `NSTMP = NVEGSERV(M)` (56); `if( NSTMP > 0 )then` (57); `RDLPSQ(M) = VEGSERRT(NSTMP)` (58); `BPVEG(M) = VEGSERBT(NSTMP)` (59); `HPVEG(M) = VEGSERHT(NSTMP)` (60); `BDLTMP = BPVEG(M)*BPVEG(M)*RDLPSQ(M)    ! *** Population density (dimensionless)` (61); `PVEGZ(M) = 1.-ALPVEG(M)*BDLTMP` (62); `BDLPSQ(M) = BPVEG(M)*RDLPSQ(M)` (63). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 37·48–50: TIME 계산은 TCVEGSER(NS)로 나눈다. 보간 가중치는 TDIFF로 나눈다. 이 파일에는 두 분모가 0인지 검사하는 조건이 없다.
- 39–47: TIME이 다음 표 시각보다 크면 M1/M2를 계속 늘린다. 이 루프에는 계열의 마지막 인덱스 검사 문장이 없다.
- 49–50·62: WTM1/WTM2와 PVEGZ 계산 뒤 이 파일에는 값의 상한·하한을 제한하는 문장이 없다.
