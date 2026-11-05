---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/fmp_ous0.f
lines: 24
sha256: 3f23b2562ce142bd656c1350d02b57d4b5bebdd095635f8bb4eb9eff7ffd6358
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fmp_ous0.f — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | 암시적 배정밀도와 쉼표 문자를 선언한다(3–4). 프로세스 1에서 IOUT·ISTEP·TIME을 순서대로 수신한다(6–10). 원문: `      SUBROUTINE FMP_OUS0(IOUT,IFL)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      CHARACTER*1 C /','/` (4); `      CALL M_MPI_RECV_I(IOUT,1,1)` (6); `      CALL M_MPI_RECV_I(ISTEP,1,1)` (8); `      CALL M_MPI_RECV_D(TIME,1,1)` (10). |
| 11–24 | 시작 시 1행 fmp_ous0 루틴 안. IOUT과 단계·시간을 쓴다(12–14). 고정 레코드 0,23, 및 시간·1,·<NULL>을 출력하고 종료한다(16–24). 원문: `      WRITE(IFL,'(I0,A)') IOUT,C` (12); `      WRITE(IFL,'(A,I0,A,1PE10.4)') 'Step ',ISTEP,'  Time ',TIME` (14); `      WRITE(IFL,'(A)') '0,23,'` (16); `      WRITE(IFL,'(1PE10.4,A)') TIME,C` (18); `      WRITE(IFL,'(A)') '1,'` (20); `      WRITE(IFL,'(A)') '<NULL>'` (22); `      END` (24). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–10: 출력 집합 번호·단계·시간의 송신원 프로세스 번호는 모두 1로 고정되어 있다. [11-04 전수 검증 정정]
