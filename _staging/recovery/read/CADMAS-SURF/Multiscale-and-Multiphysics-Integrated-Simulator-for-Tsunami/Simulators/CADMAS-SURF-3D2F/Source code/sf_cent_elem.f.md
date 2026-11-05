---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_cent_elem.f
lines: 17
sha256: aae6e1db88401ce598d9d0aeafe43b4c9e9226f5d2a15459c63cdf6316f65684
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_cent_elem.f — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 암시적 배정밀도(double precision)와 GELM(3,NELM)·IELM(24,NELM)·POS(3,*)를 선언한다. GELM 전체를 0으로 초기화한다. 원문: `      SUBROUTINE SF_CENT_ELEM(GELM,NELM,IELM,POS)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION GELM(3,NELM),IELM(24,NELM),POS(3,*)` (5); `      GELM(:,:) = 0.` (7) |
| 9–17 | 시작 시 1행 SF_CENT_ELEM 루틴 안이다. I=1..NELM마다 `N = IELM(4,I)` (10)을 설정한다. J=1..N 루프로 POS의 `IELM(4+J,I)` 열을 더한다. 누적값을 `DBLE(N)` (14)으로 나눈다. POS가 구조물 위치 좌표라는 근거는 같은 디렉터리의 `sf_array.f90:65`이다. 이 루틴이 사용하는 절점 수·번호의 첨자는 `sf_array.f90:11–12`의 주석 표기 (3,I)·(4:23,I)와 다르다. 원문: `      DO I = 1, NELM` (9); `        N = IELM(4,I)` (10); `        DO J = 1, N` (11); `          GELM(:,I) = GELM(:,I) + POS(:,IELM(4+J,I))` (12); `        ENDDO` (13); `        GELM(:,I) = GELM(:,I) / DBLE(N)` (14); `      ENDDO` (15); `      END` (17) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10–14: 구성 절점 수 N으로 나누기 전에 N>0을 확인하는 조건문은 없다.
