---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.35_file_format.md
lines: 13
sha256: 2fd8bc1d1dbaa6802942ec2cf91f0321a9f6a6a93db24d04f3cc662af3527f9f
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.35_file_format.md — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | Fort.35 file format — 문서 제목(1)과 판본 표기 `_revid=462_` (3)를 포함한다. 빈 줄(2·4)을 포함한다. |
| 5–6 | 무운동면(level of no motion) 경계조건 입력 — fort.35는 3차원 경압(baroclinic) 모의에서 fort.15의 BCFLAG_LNM을 1로 설정할 때 읽는다(5). 이 값은 적용 조건으로 제시된다. 원문: `The ADCIRC Level of No Motion Boundary Condition Input File (fort.35) is read in for 3D baroclinic simulations when the [BCFLAG_LNM](/index.php?title=BCFLAG_LNM&action=edit&redlink=1) (boundary condition flag for the level of no motion) is set to 1 in the [fort.15 file](/Fort.15_file). Its format is as follows:` (5). |
| 7–13 | 파일 형식 — 자료 묶음(data set) 반복 안에 날짜 주석 줄과 해양 경계 절점(ocean boundary node) 반복을 둔다(7–13). 절점별 줄은 k와 elevation_change를 나열한다(11). 빈 줄(8)을 포함한다. 원문: `for i=1 to numberOfDataSets` (7); `comment line (date)` (9); `for k=1 to number_of_ocean_boundary_nodes` (10); `k, elevation_change` (11); `end k loop` (12); `end i loop` (13). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5: `BCFLAG_LNM` 링크 주소에 `action=edit&redlink=1`이 들어 있다.
- 7·10–11: `numberOfDataSets`, `number_of_ocean_boundary_nodes`, `elevation_change`의 정의는 이 파일에 없다. `elevation_change`의 단위도 이 파일에 없다.
