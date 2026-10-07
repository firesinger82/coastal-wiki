---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-Original/setshld.f90
lines: 52
sha256: 3dfd60ac081bf1bfd051023edc181dab76370baaeeb8e372e36cfab9d5b2e719
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# setshld.f90 — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | EFDC+·저작권·GPLv2 머리말(1–8). SETSHLD(TSC,THETA,D,SSG,DSR,USC) 입구(9). 비점착성 퇴적물(noncohesive sediment)의 침강(settling)·Shields 기준(Shields criteria)에 van Rijn 식을 사용한다는 주석(13–14). implicit none과 실수 인수·작업변수를 선언한다(16–18). D<=1E-8이면 TSC=0.0000055·USC=0.0023을 설정하고 조기 반환한다(20–24). 조건·계산·호출 원문: `if( D <= 1E-8 )then` (20); `TSC = 0.0000055` (21); `USC = 0.0023` (22). |
| 26–31 | 시작 시 9행 SETSHLD 안. 동점성계수(kinematic viscosity) VISC=1.D-6을 고정한다(26). 비중(specific gravity) SSG와 9.82로 GP를 계산한다(27). GP/VISC²와 입경의 곱으로 무차원 입경(dimensionless grain diameter) DSR을 구하고 GPD=GP*D를 계산한다(28–30). 조건·계산·호출 원문: `VISC = 1.D-6` (26); `GP = (SSG-1.)*9.82` (27); `TMP = GP/(VISC*VISC)` (28); `DSR = D*(TMP**0.333333)` (29); `GPD = GP*D` (30). |
| 32–52 | 시작 시 9행 SETSHLD 안. Shields 매개변수(Shields parameter) THETA를 DSR 구간에 따라 계산한다(32–47). 독립된 if의 범위는 DSR<=4, 4<DSR<=10, 10<DSR<=20, 20<DSR<=150, DSR>150이다(33·36·39·42·45). 마지막 범위의 THETA는 0.055이다(46). TSC=GPD*THETA, USC=SQRT(TSC)를 계산하고 루틴·마지막 빈 줄을 끝낸다(48–52). 조건·계산·호출 원문: `if(DSR <= 4.0 )then` (33); `THETA = 0.24/DSR` (34); `if(DSR > 4.0 .and. DSR <= 10.0 )then` (36); `THETA = 0.14/(DSR**0.64)` (37); `if(DSR > 10.0 .and. DSR <= 20.0 )then` (39); `THETA = 0.04/(DSR**0.1)` (40); `if(DSR > 20.0 .and. DSR <= 150.0 )then` (42); `THETA = 0.013*(DSR**0.29)` (43); `if(DSR > 150.0 )then` (45); `THETA = 0.055` (46); `TSC = GPD*THETA` (48); `USC = SQRT(TSC)` (49). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20–24: 작은 입경 조기 반환 경로는 TSC·USC만 대입한다. 이 경로에는 THETA·DSR 대입이 없다.
- 26–29: 동점성계수는 1.D-6, 중력 관련 계수는 9.82로 고정되어 있다. DSR 식은 0.333333 지수를 사용한다.

