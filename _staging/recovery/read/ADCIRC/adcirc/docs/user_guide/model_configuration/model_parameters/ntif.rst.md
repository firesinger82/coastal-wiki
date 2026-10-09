---
file: models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/model_parameters/ntif.rst
lines: 19
sha256: aaa66c980c5dc30fb08c18a85c950ce76c8587a7428c3b3a347c03b142da4422
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# ntif.rst — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | NTIF — 메타데이터·앵커·제목을 포함한다(1–8). 천문 강제력(astronomical forcing)을 구성하는 분조(tidal constituent)의 개수라고 정의한다(10–12). 평형 조석 퍼텐셜(equilibrium tidal potential)과 사용 시 자기 인력·하중 조석(self-attraction and loading tide)을 포함하는 원문 조건을 옮긴다. 원문: `` **NTIF** is an input in the :ref:`fort.15 file <fort15>` that indicates `` (10); ` the number of tidal constituents that make up the astronomical forcing (the ` (11); ` equilibrium tidal potential and, if used, the self-attraction and loading tide). ` (12). |
| 14–19 | Usage Notes — 다른 fort.15 매개변수 NTIP를 1 또는 2로 설정해야 한다는 문장과 마지막 빈 줄을 포함한다(17–19). 원문: `` The other :ref:`fort.15 file <fort15>` parameter, :ref:`NTIP <ntip_parameter>`, must `` (17); ` be set to 1 or 2. ` (18). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
