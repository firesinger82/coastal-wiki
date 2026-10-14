---
file: models/SWASH/raw/source_code/swash/src/Swash.ftn90
lines: 71
sha256: 7c3b16e651ecfe49bbaadb071cea134aa7d90d5340de9495d5dff746a56fc645
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# Swash.ftn90 — 판독 구간 기록

구간은 1행부터 71행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | `program Swash` (1), 기관·SWASH 팀·GPL 3 이상·무보증 머리말(2–29). Marcel Zijlema와 2009년 신설 이력(30–36). 연안의 파 운동(wave motion)과 천수 흐름(shallow water flow)을 모의한다는 목적(38–40). |
| 42–53 | 시작 시 1행 Swash 프로그램 안. implicit none(42), 정지 여부를 반환하는 STPNOW 논리 함수 선언(46), 지역변수·구조·실행부 표제 주석(44–53). |
| 54–71 | 시작 시 1행 Swash 프로그램 안. MPI(Message Passing Interface) 환경 초기화 `call SWINITMPI` (56). `if (STPNOW()) goto 999` (57)이면 주 실행을 건너뛴다. `call SwashMain` (61) 뒤 999 continue(63), `call SWEXITMPI` (67)로 MPI를 종료한다. 설명 주석과 end program(54–71). 이 파일에는 !MPI 표시 행이 없으며 두 MPI 래퍼(wrapper) 호출은 원문 실행문이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
