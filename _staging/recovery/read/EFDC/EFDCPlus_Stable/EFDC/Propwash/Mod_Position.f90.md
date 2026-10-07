---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Propwash/Mod_Position.f90
lines: 74
sha256: 0da21d20dc61bf2a1127dd5a84c8e5e53a63211d02091dce41f1301c18cb9567
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Mod_Position.f90 — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | EFDC+·GPLv2·저작권 머리말(1–8), Mod_Position 시작(9). GLOBAL의 RKD·RK4와 Mod_MPI_Helper_Functions 사용(11–12), implicit none·기본 private·position 공개(14–17). position 형식의 time·x_pos/y_pos/z_pos·var(3) 기본값은 0.0(19–24). ero(:)는 종별 침식률(erosion rate)의 allocatable 배열(25). 형식 결합 절차(type bound procedure) write_out·interp_pos, 형식 종료·모듈 contains와 빈 줄(26–35). 원문: `real (kind = RKD)   :: time   = 0.0       !< Current time we are at` (20); `real (kind = RKD)   :: x_pos  = 0.0       !< x position [meters]` (21); `real (kind = RKD)   :: y_pos  = 0.0       !< y position [meters]` (22); `real (kind = RKD)   :: z_pos  = 0.0       !< z position [meters]` (23); `real (kind = RKD)   :: var(3) = 0.0       !< Spatially dependent variable` (24); `real (kind = RKD), allocatable :: ero(:)  !< Spatially dependent erosion rate by sediment class` (25). |
| 36–48 | 시작 시 9행 Mod_Position 안. 두 좌표 사이 보간(interpolation)이라는 주석(36–39), interp_pos 시작(40), implicit none·inout self 선언(42–44). 지역변수 주석 뒤 실행문 없이 종료(45–47). |
| 49–74 | 시작 시 9행 Mod_Position 안. 좌표·종속 변수 출력 주석(49–54), write_out(self,unit_num,cell,counter) 시작(55). 입력 self·unit_num, 선택 인수(optional argument) cell·counter와 지역 L 선언(59–62). present(cell)이면 L=cell, else는 L=-1(64–68). unit_num에 문자열, x/y/z·var(1)·L을 (a,4f15.5,I8)로 출력(70). 루틴·모듈 종료·빈 줄(72–74). 외부 계산 루틴 호출은 없다. 원문: `if(present(cell) )then` (64); `L = cell` (65); `L = -1` (67). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 40–47: interp_pos는 self 인수를 선언한 뒤 종료한다. 좌표를 보간하거나 self에 대입하는 실행문이 없다.
- 55·61·64–70: counter는 optional 인수로 선언한다. 출력 루틴은 counter를 검사하거나 출력하지 않는다.
