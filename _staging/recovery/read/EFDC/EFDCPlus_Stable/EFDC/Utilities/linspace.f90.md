---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Utilities/linspace.f90
lines: 52
sha256: da9c36aacfe2a7c30cf912933fc3b9af4b8b241739fe1685454525c726b16ff4
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# linspace.f90 — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | EFDC+·GPLv2 머리말(1–8), lower부터 upper까지 양 끝을 포함하는 등간격 수열이라는 설명과 인수 주석(9–16). `subroutine linspace(arr_size, lower, upper, evenly_space)` (17), GLOBAL의 RKD 사용과 implicit none(19–21). 입력은 정수 arr_size·RKD lower/upper이며 출력 배열 크기는 arr_size이다(24–27). 지역 range·i 선언과 빈 줄(29–32). |
| 33–44 | 시작 시 17행 linspace 루틴 안. 원문은 `range = upper - lower` (33). `if( arr_size == 0 )then` (36)이면 즉시 return한다(37). 독립 조건 `if( arr_size == 1 )then` (40)이면 첫 원소에 lower를 복사한 뒤 return한다(41–42). 두 조건 종료와 빈 줄을 포함한다(38–44). |
| 45–52 | 시작 시 17행 linspace 루틴 안이며 두 크기 조건 밖. `do i = 1, arr_size` (46)에서 `evenly_space(i) = lower + range * (i - 1) / (arr_size - 1)` (47). 루프 종료·return·빈 줄·루틴 종료(48–52). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 36–47: 크기 특례는 arr_size==0 및 arr_size==1이다. arr_size<0을 별도로 처리하는 조건은 이 루틴에 없다.
