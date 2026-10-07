---
file: models/EFDC/raw/source_code/EFDC-GVC/funden.for
lines: 58
sha256: 36dec1a06faed3089ab1000f154e7494f441daf14fcba0588faea8fafaed59c1
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# funden.for — 판독 구간 기록

구간은 1행부터 58행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | 구분 주석과 `FUNCTION FUNDEN(SAL,SED,TEM)` 선언(1–6). 염분(salinity)·온도(temperature)·퇴적물(sediment)의 함수로 밀도(density)를 계산한다는 목적(10). EFDC-FULL 1.0a·수정자·날짜·변경 이력 틀(12–23). IMPLICIT REAL*8은 주석 처리(25), `EFDC.PAR` 포함(27). 고정 계수 `SSG=2.5` (29), `SDEN=1./2500000.` (31). |
| 33–44 | 시작 시 6행 FUNDEN 함수 안. 염분·온도 밀도 주석(33–34). SSTMP=SAL·TTMP=TEM 복사(35–36). 온도 다항식 `RHTMP=999.842594+6.793952E-2*TTMP-9.095290E-3*TTMP*TTMP` (37); `&    +1.001685E-4*TTMP*TTMP*TTMP-1.120083E-6*TTMP*TTMP*TTMP*TTMP` (38); `&    +6.536332E-9*TTMP*TTMP*TTMP*TTMP*TTMP` (39). 염분 보정식 `RHO=RHTMP+SSTMP*(0.824493-4.0899E-3*TTMP+7.6438E-5*TTMP*TTMP` (40); `&   -8.2467E-7*TTMP*TTMP*TTMP+5.3875E-9*TTMP*TTMP*TTMP*TTMP)` (41); `&   +SQRT(SSTMP)*SSTMP*(-5.72466E-3+1.0227E-4*TTMP` (42); `&   -1.6546E-6*TTMP*TTMP)+4.8314E-4*SSTMP*SSTMP` (43). |
| 45–58 | 시작 시 6행 FUNDEN 함수 안. 2007-06-18 퇴적물 보정 변경 주석(45–46). 이전 `(SSG-1.)` 보정식은 주석 처리(48). 실행식 `RHO=RHO*( (1.-SDEN*SED)+SSG*SDEN*SED )` (49). FUNDEN=RHO 반환값 복사(53), 구분 주석·RETURN·END(54–58). 조건 분기와 외부 루틴 CALL 문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 29·31·49: 퇴적물 보정 계수 SSG=2.5와 SDEN=1./2500000.을 함수 안에서 고정한다. 두 계수를 인수로 받는 선언은 없다.
- 35·42: SAL을 SSTMP에 복사한 뒤 SQRT(SSTMP)를 계산한다. 이 함수에는 염분 범위를 검사하는 실행 조건이 없다.
