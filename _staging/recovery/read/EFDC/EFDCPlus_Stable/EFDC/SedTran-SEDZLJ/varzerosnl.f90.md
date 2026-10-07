---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/varzerosnl.f90
lines: 33
sha256: 8f0e5343b663665160adb5b00e80d288b030a193c763d11f3c7c92c258bea39a
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# varzerosnl.f90 — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | VARZEROSNL의 GPLv2 머리말·루틴 선언을 포함한다(1–9). 주석은 할당 뒤 여러 배열을 0으로 만드는 루틴이라고 적는다(11). 변경 기록은 2015-06 SIGMA-Z 도입을 적는다(14–17). GLOBAL 사용과 implicit none 및 빈 줄을 포함한다(19–22). |
| 23–33 | 시작 시 9행 VARZEROSNL 루틴 안이다. NCORENO 배열 전체를 0으로 초기화한다(23–24). 스칼라 기본값은 전단응력(shear stress) 계산 최소 수심 HPMIN=0.25, 바닥 수층 질량의 최대 퇴적(deposition) 비율 MAXDEPLIMIT=0, 물 밀도 RHO=1000 kg/m³, 활성층(active layer) 배수 TACTM=0, WATERDENS=1 g/cm³이다(26–31). 루틴 종료를 포함한다(33). 원문: `NCORENO = 0` (24); `HPMIN = 0.25      ! *** Minimum depth to compute shears` (27); `MAXDEPLIMIT = 0.0 ! *** The maximum fraction of mass from bottom water column layer that can be deposited on active bed layer.` (28); `RHO = 1000.0      ! *** Density of water in kg/m^3.` (29); `TACTM = 0.0       ! *** Active layer multiplier` (30); `WATERDENS = 1.0   ! *** Density of water in g/cm^3` (31). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28·30: MAXDEPLIMIT와 TACTM의 초기값은 각각 0.0이다. 이 루틴에는 해당 값의 범위 검사 또는 입력 판독이 없다.

