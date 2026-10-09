---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.rotm.md
lines: 25
sha256: 5a3abcce75e085b35df908556deaf344fce00e9171c5d083202cd1d0f0a5bc52
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.rotm.md — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Fort.rotm — 제목과 판본 표기 `_revid=528_`(1–3)을 포함한다. 구면 지구(spherical Earth)의 지리 좌표(geographical coordinates)를 회전하는 파일이라고 설명한다(5). 회전 지정 방법은 `ICS` 참조로 안내한다(5). 지배방정식(governing equations)의 구면 좌표 특이점(singularity)을 없애기 위해 북극을 바다에서 육지로 옮기고 남극을 육지에 유지하는 회전을 보통 원한다고 설명한다(5). 원문: `The fort.rotm file is used to rotate the geographical coordinates on the Spherical Earth (see [ICS](/ICS) for details on how to specify that rotation is desired). Rotation is typically desired in order to move the North Pole from the ocean onto land (and keep the South Pole on land) so that the singularity in the Spherical coordinate form of the governing equations is removed (see the File Format Examples section below for examples of valid rotations that achieve this goal). ` (5). |
| 7–16 | File Format — 첫 행은 형식 종류 문자열이고 뒤 행들은 값이라고 설명한다(9). 새 북극 중심의 경도·위도, 내재 회전(intrinsic rotation)의 세 각도, 회전 행렬(rotation matrix)의 세 형식을 제시한다(11–15). 연결되어 보이는 형식 문자열을 수정하지 않고 옮긴다. 입력 파일 형식 원문: `File format is short but there are three variants. General format is: first line is a string indicating format type, following lines are the values. ` (9); `- znorth_in_spherical_coorslon0 lat0&#160;! Comment: lon0 lat0 is the center of the new north pole` (11); `- z-x-zalpha beta gamma&#160;! Comment: intrinsic rotation of alpha, beta, gamma` (13); `- rotation_matrixrot11 rot12 rot13rot21 rot22 rot23rot31 rot32 rot33! Comment: a rotation matrix R: x-> x' is given` (15). |
| 17–25 | File Format Examples — 세 예제가 두 극을 육지로 회전시킨다고 설명한다(19). 선택과 무관하게 결과는 실질적으로 같아야 한다고 적는다(19). Greenland–Antarctica, China–Argentina, Borneo–Brazil 예제의 좌표를 제시한다(21–25). 조건과 예제 원문: `The following examples ensure that both poles are rotated onto land. The results should stay effectively the same no matter the choice.` (19); `- znorth_in_spherical_coors-42.8906 72.3200 &#160;! Greenland-Antarctica` (21); `- znorth_in_spherical_coors112.8516 40.3289 &#160;! China-Argentina` (23); `- znorth_in_spherical_coors114.16991 0.77432 &#160;! Borneo-Brazil` (25). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 9·11–15·21–25행: 9행은 형식 문자열과 값을 서로 다른 행으로 설명한다. 형식 목록과 예제는 `znorth_in_spherical_coorslon0`, `z-x-zalpha`, `rotation_matrixrot11`, `znorth_in_spherical_coors-42.8906`처럼 문자열과 값 또는 변수 이름을 붙여 표시한다.
- 11–15행: 경도·위도 및 회전 각도의 단위를 이 파일에 명시하지 않는다.
