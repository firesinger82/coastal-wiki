---
file: models/SWASH/raw/source_code/swash/src/SwanCompdata.ftn90
lines: 66
sha256: 296c7dbe47f9422daab5642d4f290c7d871e21a48abf87dfb58197af67a950b8
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwanCompdata.ftn90 — 판독 구간 기록

구간은 1행부터 66행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | `module SwanCompdata` (1), 기관·작성자·GPL 3 이상·무보증 머리말(2–29). 작성자와 2007년 신설·2008년 경계 다각형(boundary polygon) 변경 이력(30–38). 비구조 격자(unstructured grid) 계산용 데이터를 보유한다는 목적·방법 주석(40–46), 모듈 사용 표제와 빈 주석(48–49). |
| 50–66 | 시작 시 1행 SwanCompdata 모듈 안. `implicit none` (50), 매개변수·변수 표제 주석(51–56). nbpol은 경계 다각형 수(57), `integer, dimension(10000)                  :: nbpt   ! number of boundary vertices for each boundary polygon` (58)은 다각형별 경계 꼭짓점(vertex) 수를 저장한다. save allocatable blist는 다각형별 정렬 꼭짓점 목록(60), jbcell·jbface는 경계 셀(cell)·면(face) 인덱스 배열(61–62)이다. 실행부 표제 주석과 모듈 종료(63–66). 실행 루틴과 조건문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 57–62: nbpt의 길이는 10000으로 고정한다. nbpol·nbpt 선언에는 초기값 대입이 없다.
