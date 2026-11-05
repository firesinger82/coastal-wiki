---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/shift0.f
lines: 21
sha256: 865157ca12977d9e8eff1db67e119947fb245e610e83f6e754e221c94eb89dfe
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# shift0.f — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | SHIFT0는 정수 배열(integer array)의 복사 IA=IB와 입력·출력·개수 N을 주석으로 설명한다(2–8). IA(N)·IB(N)을 선언한다(11). 구분·복사 시작 주석을 포함한다. 원문: `      SUBROUTINE  SHIFT0( IA,IB,N )` (2); `C  IA = IB  ---  DATA SHIFT` (4); `C  IA      = SHIFT AREA                                    --- ( O )` (6); `C  IB      = SHIFT DATA                                    --- ( I )` (7); `C  N       = NUMBER OF SHIFT DATA                          --- ( I )` (8); `      DIMENSION  IA(N),IB(N)` (11); `C--- SHIFT ---` (14). |
| 15–21 | 시작 시 2행 SHIFT0 루틴 안. I=1..N에서 IB(I)를 IA(I)에 복사한다(15–17). 빈 주석·RETURN·END를 포함한다. 원문: `      DO 1000 I=1,N` (15); `         IA(I) = IB(I)` (16); ` 1000 CONTINUE` (17); `      RETURN` (20); `      END` (21). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
