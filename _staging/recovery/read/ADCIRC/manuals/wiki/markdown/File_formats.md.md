---
file: models/ADCIRC/raw/manuals/wiki/markdown/File_formats.md
lines: 32
sha256: bdfc0b07bc74df613c5232d33c13869f0e691d9609c495e0863e925eb4c9d8e6
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# File_formats.md — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | 제목·판본 표기·빈 줄과 ADCIRC File Formats 절 제목을 포함한다(1–6). |
| 7–14 | Input Files Contributor needed / 필수 입력 — 모든 실행에 필요한 두 파일을 제시한다(9). `fort.14`는 삼각형 유한요소(triangular finite element) 격자, `fort.15`는 실행 매개변수·주파수 의존 경계 강제(forcing)·출력 옵션을 설정한다(11–13). 원문: `Required: Every ADCIRC run requires the following two input files:` (9); `- [fort.14 file](/Fort.14_file) - Grid file: Defines the ADCIRC triangular finite element grid` (11); `- [fort.15 file](/Fort.15_file) - Parameter file: Sets runtime parameters, frequency-dependent boundary forcing, and output options` (13). |
| 15–20 | Input Files / 자주 사용하는 선택 입력 — 구성에 따라 `fort.13` 절점 속성(nodal attribute)과 `fort.22` 바람 강제 파일을 사용한다(15–19). 바람 파일 형식은 바람 입력 형식과 `NWS`에 의존한다고 설명한다(19). 원문: `Optional, frequently used, depending on simulation configuration:` (15); `- [fort.13 file](/Fort.13_file) - Nodal Attribute file: Defines parameters (e.g., Mannings N, canopy cover) that can be set at specific nodes.` (17); `- [fort.22 file](/Fort.22_file) - Wind forcing file. The specific format of this file depends on the wind input format. See the NWS parameter in the fort.15 file description.` (19). |
| 21–31 | Input Files / 강제 구성별 선택 입력 — 결합 SWAN 실행의 `fort.26`과 `swaninit`, 기상 입력의 Oceanweather 형식과 `NWS12`·`NWS13` 링크를 제공한다(21–30). `fort.26`에는 결합 코드의 비정형 격자(unstructured grid) 명령이 필요하다고 적는다(24). 원문: `Optional, depending on simulation forcing configuration:` (21); `- For coupled SWAN runs:` (23); `[fort.26 file](/Fort.26_file) - SWAN parameter file. Same format as a traditional SWAN input file, but with "SWAN unstructured grid" commands specific to the coupled ADCIRC+SWAN code.` (24); `- [swaninit file](/index.php?title=Swaninit_file&action=edit&redlink=1) - SWAN init file. This is the same as in a traditional SWAN run.` (26); `Meteorological Inputs (NWS#):` (28); `- Oceanweather (OWI) Formats [NWS12](/NWS12) and [NWS13](/NWS13)` (30). |
| 32–32 | Output Files Contributor needed — 절 제목만 있고 출력 파일 목록은 없다(32). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 26: `Swaninit_file` 링크에는 `action=edit&redlink=1`이 붙어 있다.
- 32: 출력 파일 절에는 `Contributor needed` 표기가 있고 본문이 없다.
