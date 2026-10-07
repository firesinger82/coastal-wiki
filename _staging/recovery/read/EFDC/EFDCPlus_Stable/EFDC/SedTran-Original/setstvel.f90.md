---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-Original/setstvel.f90
lines: 41
sha256: 674211839621e55d04d7378e5e654f350386c37ee99c8df0d3a1bdfad9e048fc
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# setstvel.f90 — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | EFDC+·저작권·GPLv2 머리말(1–8). SETSTVEL(D,SSG) 입구(9). 비점착성 퇴적물(noncohesive sediment)의 침강(settling)·Shields 기준(Shields criteria)에 van Rijn 식을 사용한다는 주석(11–12). 변경 이력·implicit none·반환값·입경·비중(specific gravity)·작업변수 선언을 포함한다(14–18). |
| 20–27 | 시작 시 9행 SETSTVEL 안. 동점성계수(kinematic viscosity) VISC=1.D-6을 고정한다(20). SSG와 9.82로 GP를 구하고 입경 D를 곱한 GPD·SQRT(GPD)·RD를 계산한다(21–24). 침강속도(settling velocity) 계산 주석과 빈 줄을 포함한다(26–27). 조건·계산·호출 원문: `VISC = 1.D-6` (20); `GP = (SSG-1.)*9.82` (21); `GPD = GP*D` (22); `SQGPD = SQRT(GPD)` (23); `RD = SQGPD*D/VISC` (24). |
| 28–41 | 시작 시 9행 SETSTVEL 안. 독립된 if 세 개로 입경 범위를 나눈다(28·31·35). D<1.0E-4는 SQGPD*RD/18., 1.0E-4<=D<1.E-3은 제곱근 TMP를 포함한 전이식, D>=1.E-3은 1.1*SQGPD를 사용한다(29·32–33·36). WSET를 반환값에 복사하고 함수와 마지막 빈 줄을 끝낸다(38–41). 조건·계산·호출 원문: `if( D < 1.0E-4 )then` (28); `WSET = SQGPD*RD/18.` (29); `if( D >= 1.0E-4 .and. D < 1.E-3 )then` (31); `TMP = SQRT(1.+0.01*RD*RD)-1.` (32); `WSET = 10.0*SQGPD*TMP/RD` (33); `if( D >= 1.E-3 )then` (35); `WSET = 1.1*SQGPD` (36). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20–24: 동점성계수는 1.D-6, 중력 관련 계수는 9.82로 고정되어 있다.
- 21–24·28–37: SQRT(GPD)는 입경 분기 전에 실행된다. 이 함수에는 D·SSG의 입력 범위 검사나 GPD의 비음수 제한이 없다.

