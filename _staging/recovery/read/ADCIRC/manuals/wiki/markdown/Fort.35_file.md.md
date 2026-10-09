---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.35_file.md
lines: 9
sha256: c67cdce0eec8799876422bdcf6f2c97e510d77374f736e76f79bfb871cebaca3
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.35_file.md — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Fort.35 file / 역할·적용 조건 — 제목·판본·빈 줄을 포함한다(1–4). 무운동층(level of no motion) 경계조건 입력 파일이며 3D 경압(baroclinic) 실행에서 지정 경계 플래그(boundary condition flag)가 1일 때 읽는다고 명시한다(5). 원문: `The fort.35 is the Level of No Motion Boundary Condition Input File.  It is read in for 3D baroclinic simulations when the [BCFLAG_LNM](/index.php?title=BCFLAG_LNM&action=edit&redlink=1) (boundary condition flag for the level of no motion) is set to 1 in the [fort.15 file](/Fort.15_file).` (5). |
| 7–9 | File Format — 별도 `fort.35 file format` 문서로 연결한다(7–9). 이 구간은 입력행을 제시하지 않는다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5: `BCFLAG_LNM` 참조 URL에 `action=edit&redlink=1`이 들어 있다.
