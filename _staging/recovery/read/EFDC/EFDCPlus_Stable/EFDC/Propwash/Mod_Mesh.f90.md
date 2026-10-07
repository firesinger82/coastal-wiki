---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Propwash/Mod_Mesh.f90
lines: 34
sha256: 95e1de465c8fd70fd31d678128d7c6b48b4721d42155d68bc2663bba548d11c9
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Mod_Mesh.f90 — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | EFDC+·GPLv2·저작권 및 DSI 머리말(1–11). Propwash 파일을 읽는 루틴을 포함한다는 목적 주석(12–14). mod_mesh 시작(15), GLOBAL의 RKD·RK4와 mod_position 사용(17–18), implicit none(20). 기본 private와 mesh 공개(22–24), 빈 줄 포함. |
| 26–34 | 시작 시 15행 mod_mesh 안. mesh는 position을 확장(26). 면적(area)·반경 방향 폭(radial width)·축 방향 길이(axial length) 기본값은 0.0, 현재 L 인덱스 cell 기본값은 0(27–30). 원문은 area·width·length의 단위를 모두 [m]로 적는다. 형식 종료·빈 줄·모듈 종료(31–34). 조건·실행 루틴·호출은 없다. 원문: `real(kind = rkd) :: area = 0.0    !< area of the cell in [m]` (27); `real(kind = rkd) :: width = 0.0   !< width (radial direction) of the cell of the cell in [m]` (28); `real(kind = rkd) :: length = 0.0  !< length (axial direction) of the cell of the cell in [m]` (29); `integer          :: cell = 0      !< L index of the current position` (30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27: area는 면적이라는 주석을 갖고 있으나 같은 선언의 단위 주석은 [m]이다.
