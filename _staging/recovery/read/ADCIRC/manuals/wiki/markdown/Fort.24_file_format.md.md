---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.24_file_format.md
lines: 22
sha256: 4c1d537b64a303d401d1b6e771dc0809d2c85c4df717346c56b8bbc2e494f9bf
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.24_file_format.md — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Fort.24 file format / 머리말 — 제목·판본·빈 줄과 입력 자료 행·반복문·가독성 설명을 포함한다(1–5). 원문: `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. Loops indicate multiple lines of input. ` (5). |
| 7–17 | 조화 성분(harmonic constituent)별 입력 — 성분 반복문 안에 네 머리행을 두고 전체 절점에 대해 절점 번호·SAL 진폭(amplitude)·위상(phase)을 입력하는 중첩 반복문(nested loop)을 제시한다(7–16). 원문: `for k=1,[NTIF](/NTIF)` (7); `Alpha line` (9); `Constituent frequency` (10); `1` (11); `Constituent name (e.g., M2)` (12); `for j=1,[NP](/index.php?title=NP&action=edit&redlink=1)` (13); `[JN](/index.php?title=JN&action=edit&redlink=1), [SALTAMP(k,JN)](/index.php?title=SALTAMP(k,JN)&action=edit&redlink=1), [SALTPHA(k,JN)](/index.php?title=SALTPHA(k,JN)&action=edit&redlink=1)` (14); `end j loop` (15); `end k loop` (16). |
| 18–22 | Note — 성분별 첫 네 행은 파일에 반드시 있어야 하지만 읽을 때 건너뛴다고 명시한다(20). 속도 정보가 없는 tea 조화 형식이며 성분 순서가 fort.15의 조석 퍼텐셜(tidal potential) 항목 순서와 같아야 한다고 적는다(22). 위상·진폭의 단위 및 교점 계수(nodal factor)·평형 위상(equilibrium argument)에 의한 값의 수정을 설명한다(22). 원문: `The first four lines (Alpha line, Constituent frequency, 1, Constituent name) for each constituent must be present in the file but they are skipped over during the ADCIRC read.` (20); `The format of this file is identical to the “tea” harmonic format with no velocity information included. Entries are grouped by constituents and must be in the same order as the tidal potential terms listed in the [fort.15](/Fort.15). Phases must be in degrees. Amplitudes must be in units compatible with the units of gravity. These values are modified by the nodal factor and equilibrium argument provided for the tidal potential terms.` (22). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 13–14: 절점 수·번호·SAL 진폭·위상 참조 URL에 `action=edit&redlink=1`이 들어 있다.
