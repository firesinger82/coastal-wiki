---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Out/FormatOutputMPI.f90
lines: 36
sha256: fb653deb87a91c38a612bbee7b04393afb5ce7bf7fd6c0c9414731ee9526a1c3
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# FormatOutputMPI.f90 — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | EFDC+ 웹사이트·저장소 출처, 2021–2024 저작권과 GPLv2 머리말(1–8). 빈 줄(9). |
| 10–23 | `WriteBreak(unit_num)` 시작(10). implicit none과 integer intent(in) 출력 장치 번호(unit number) 선언(12–15). 지정 장치에 공백 한 줄, 양 끝이 세로 막대인 하이픈 구분선, 공백 한 줄을 `(a)` 형식으로 쓴다(17–19). 루틴 종료·빈 줄(21–23). 조건·계산식·외부 호출은 없다. |
| 24–36 | `WriteInteger(int_to_write_out, unit_num,variable_desc)` 시작(24). implicit none(26). 출력 정수·장치 번호의 integer intent(in) 인수와 Character(20) intent(in) 설명문 선언(29–31). `(A20,I5)` 형식으로 설명문과 정수를 지정 장치에 출력한다(34). 루틴 종료·빈 줄(35–36). 조건·계산식·외부 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 31·34: variable_desc의 선언 길이는 20이다. 출력 형식은 설명문 A20과 정수 I5의 고정 폭을 사용한다.
