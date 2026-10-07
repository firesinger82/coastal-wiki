---
file: models/SFINCS/raw/source_code/sfincs/source/src/sfincs_openacc.f90
lines: 81
sha256: cd698c083d87843d18533761f90a3805b7f3371df8d6685e5631ec39ecc31d20
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# sfincs_openacc.f90 — 판독 구간 기록

구간은 1행부터 81행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | sfincs_openacc 모듈은 sfincs_data를 사용하고 implicit none을 선언한다(1–5). contains와 `initialize_openacc()` 입구를 포함한다(7–9). `!call acc_init( acc_device_nvidia )` (11)는 주석 처리된 호출이다. GPU 메모리로 배열을 복사한다는 주석과 빈 주석을 포함한다(13–14). |
| 15–46 | 시작 시 9행 initialize_openacc 루틴 안. 하나의 OpenACC enter data copyin 지시문이 연속 행으로 이어진다(15–43). 수위·유량·속도·바닥고·최대값·체적(15), 격자 플래그·경계·평균속도(16–17), subgrid 속도점·수위점 표(18–20), 이웃 인덱스(21–23), 유량원·배수(24), 조파기 인덱스·방향·보간·파랑 forcing(25–29), 구조물(30), 파랑·풍응력·바람·기압·강수·외부 유량(31–35), 격자 간격·역수·면적과 마찰·Coriolis·저류·점성(36–37), cuv 대응·x73·gnapp2(38–40), 시간간격 분석 배열(41), SCS·강수·침투 상태(42), Green-Ampt·Horton 계수와 상태(43)를 지정한다. 이 루틴에는 if 조건이나 값을 계산하는 대입식이 없다. 루틴 종료와 주석을 포함한다(44–46). |
| 47–81 | `finalize_openacc()` 시작(47). 하나의 OpenACC exit data delete 지시문이 49–77행으로 이어진다. 수위·유량·속도·바닥고·진단값(49), 격자·경계·subgrid·이웃 배열(50–57), 유량원·배수·조파기·구조물(58–64), 파랑·기상·강수·외부 유량(65–69), 격자 간격·면적·물리 계수(70–71), cuv 대응·x73·gnapp2(72–74), 시간간격 분석(75), SCS·강수·침투 및 Green-Ampt·Horton 배열(76–77)을 삭제 대상으로 지정한다. 이 루틴에도 조건·값 계산식은 없다. 루틴·모듈 종료와 주석을 포함한다(78–81). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11: acc_init 호출은 주석 처리되어 있다. 이 파일의 실행문에는 별도 acc_init 호출이 없다.
- 35·69: prcp는 copyin 목록의 같은 행에 두 번 등장한다. delete 목록의 같은 행에도 두 번 등장한다.
- 36·70: copyin 목록에는 dyrinvc가 있다. delete 목록에는 dxrinvc 뒤에 dxm이 이어지며 dyrinvc가 없다.
