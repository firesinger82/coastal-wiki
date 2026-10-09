---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort47.rst
lines: 17
sha256: d3d844498cec296a52f0823e162bec4c1845d85e1b2eab0ee4abcabc571e2cc6
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort47.rst — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Fort.47: Temperature Values at the Surface Layer — 대기 모델 출력 또는 표면 수온 경계값 파일(Surface Temperature Boundary Values File)로 주어진 상부 수온 경계조건(top temperature boundary condition)을 기록한다(6). 표면층(surface layer) 수온만 기록하며 fort.63과 같은 형식을 따른다(6). fort.15의 IDEN이 3 또는 4일 때만 제공한다(6). 원문: ``The fort.47 file records the top temperature boundary condition that is either provided via output from an atmospheric model or as an input variable into the code via a Surface Temperature Boundary Values File. This output file follows the same format as the :doc:`Water Surface Elevation <fort63>` file, as it only records the temperature values for the surface layer. The output file is only provided if the :ref:`IDEN <IDEN>` value in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>` is given as a 3 or 4, as ADCIRC evaluates the temperature changes for these two :ref:`IDEN <IDEN>` values.`` (6). |
| 8–17 | Notes — fort.63의 형식을 따르고 표면층 수온만 기록한다(11–12). 생성 조건과 경계값의 두 출처를 반복한다(13–16). 출력 시기는 fort.63의 NSPOOLGE 매개변수와 일치한다고 적는다(17). 원문: `* Output format follows fort.63 conventions` (11); `* Only records temperature values at the surface layer` (12); `* Generated only when IDEN = 3 or 4` (13); `* Temperature boundary conditions can come from` (14); `    * Atmospheric model output` (15); `    * Surface Temperature Boundary Values File` (16); `* Output timing matches fort.63 parameters (NSPOOLGE) ` (17). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
