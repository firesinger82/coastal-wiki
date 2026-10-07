---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/Input_Files/Run_Control_Files.md
lines: 26
sha256: 5cd5dd9474e4c0ccb757eef444c6906fb496ebfa6b6feea72445d116c566ec2f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Run_Control_Files.md — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 머리말 — 페이지 제목은 Run Control Files이다(3). 페이지 ID, space, URL, 버전, 갱신 시각과 문서 경로를 기록한다(2–8). |
| 10–16 | Run Control Files / 실행 제어(run control) 파일 — 주 입력 파일(master input file), 수질(water quality), 퇴적물 속성작용(sediment diagenesis), RPEM 설정 파일을 나열한다(12–15). 파일 이름과 설명을 그대로 옮긴다. 마지막 빈 줄을 포함한다(16). 원문: `\| efdc.inp \| master input file \|` (12); `\| wq3dwc.inp \| water quality input \|` (13); `\| wq3dsd.inp \| sediment diagenesis \|` (14); `\| wqrpem.inp \| RPEM settings \|` (15). |
| 17–26 | Restart Related Files — 유체역학 재시작(hydrodynamic restart), 젖음·마름(wetting & drying), 하상 온도(bed temperature), 수질, 퇴적물 속성작용, 뿌리 식물·부착생물(rooted plant & epiphyte)의 재시작 관련 파일을 나열한다(21–26). 파일 이름과 설명을 그대로 옮긴다. 원문: `\| restart.inp \| hydrodynamic restart \|` (21); `\| rstwd.inp \| wetting  & drying \|` (22); `\| temp.rst \| bed temperature restart \|` (23); `\| wqwcrst.inp \| water quality restart \|` (24); `\| wqsdrst.inp \| sediment diagenesis restart file \|` (25); `\| wqrpemrst.inp \| rooted plant & epiphyte \|` (26). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 15행: `RPEM settings`라고 적지만 RPEM 약어의 풀이는 이 파일에 없다.

