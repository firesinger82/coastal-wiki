---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fortrotm.rst
lines: 55
sha256: 46853cd0c0baaa04a78d662155bca3e06d8d2ec1ffbb6d17c372ad8d525cac03
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fortrotm.rst — 판독 구간 기록

구간은 1행부터 55행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | Fort.rotm: Rotation of the geographical coordinates — meta 지시문과 참조 표지를 포함한다(1–5). 구면 지구(Spherical Earth)의 지리 좌표(geographical coordinates)를 회전하는 파일이다(10–12). 북극을 바다에서 육지로 옮기고 남극도 육지에 두어 구면 좌표 지배방정식의 특이점(singularity)을 제거하려는 목적을 설명한다(13–16). 원문: `The fort.rotm file is used to rotate the geographical` (10); ``coordinates on the Spherical Earth (see :ref:`ICS <ics_parameter>` for details on how to`` (11); `specify that rotation is desired). Rotation is typically desired in order to` (12); `move the North Pole from the ocean onto land (and keep the South Pole on land)` (13); `so that the singularity in the Spherical coordinate form of the governing` (14); `equations is removed (see the File Format Examples section below for examples of` (15); `valid rotations that achieve this goal).` (16). |
| 18–38 | File Format — 첫 줄은 형식 종류를 나타내는 문자열이고 다음 줄들은 값이다(21–22). 새 북극 위치, 내재적 회전(intrinsic rotation)의 세 각, 회전 행렬(rotation matrix)의 세 행이라는 세 형식을 제시한다(24–37). 원문: `File format is short but there are three variants. General format is: first line` (21); `is a string indicating format type, following lines are the values.` (22); `#. znorth_in_spherical_coors` (24); `   lon0 lat0 ! Comment: lon0 lat0 is the center of the new north pole` (26); `#. z-x-z` (28); `   alpha beta gamma ! Comment: intrinsic rotation of alpha, beta, gamma` (30); `#. rotation_matrix` (32); `   rot11 rot12 rot13` (34); `   rot21 rot22 rot23` (35); `   rot31 rot32 rot33` (36); `   ! Comment: a rotation matrix R: x-> x' is given` (37). |
| 39–55 | File Format Examples — 두 극을 육지로 옮기는 세 예제를 제시한다(42–55). 어느 선택에서도 결과가 사실상 같아야 한다고 적는다(42–43). 원문: `The following examples ensure that both poles are rotated onto land. The results` (42); `should stay effectively the same no matter the choice.` (43); `-  znorth_in_spherical_coors` (45); `   -42.8906 72.3200 ! Greenland-Antarctica` (47); `-  znorth_in_spherical_coors` (49); `   112.8516 40.3289 ! China-Argentina` (51); `-  znorth_in_spherical_coors` (53); `   114.16991 0.77432 ! Borneo-Brazil` (55). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 26·30행: `lon0`, `lat0`, `alpha`, `beta`, `gamma`의 단위를 이 파일에서 명시하지 않는다.
