---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.24_file.md
lines: 17
sha256: aa2400ad1c64f2ccecd26095bc7fc192f162175dba72d2e7d320a0a234b965a5
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.24_file.md — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Fort.24 file / 역할·적용 조건 — 제목·판본·빈 줄을 포함한다(1–4). 해양 자체 인력·하중(ocean self-attraction and loading, SAL) 조석을 담으며 조석 강제력 옵션의 지정값에서 ADCIRC에 사용한다고 적는다(5). 원문: `The fort.24 file contains ocean self-attraction and loading (SAL) tides[&#91;1&#93;](#cite_note-Ray-1) that are used to force ADCIRC when [NTIP](/NTIP)=2 in the [fort.15 file](/Fort.15_file).` (5). |
| 7–10 | Specification — 자료 동화된 조석 해(data-assimilated tidal solutions)로 이 파일을 생성할 수 있는 OceanMesh2D 함수 이름을 제시한다(9). 원문: `The [OceanMesh2D](/Grid_Development_and_Editing#OceanMesh2d) function "Make_f24" can be used to generate the fort.24 file from data-assimilated tidal solutions.` (9). |
| 11–14 | File Format — 별도 `fort.24 file format` 문서로 연결한다(11–13). 마지막 빈 줄을 포함한다(14). |
| 15–17 | References — Ray의 1998년 해양 자체 인력·하중 논문에 대해 제목·학술지·권·쪽·DOI를 적는다(17). 이 구간은 논문 본문을 제공하지 않는다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5·17: 인용 링크는 `#cite_note-Ray-1`을 가리키고 참고문헌의 역참조는 `#cite_ref-Ray_1-0`을 가리킨다. 이 Markdown 파일에는 두 이름을 가진 명시적 앵커가 없다. 5행에는 HTML 문자 참조 `&#91;1&#93;`도 남아 있다.
