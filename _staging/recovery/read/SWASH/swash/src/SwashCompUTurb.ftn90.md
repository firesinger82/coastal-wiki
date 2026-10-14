---
file: models/SWASH/raw/source_code/swash/src/SwashCompUTurb.ftn90
lines: 88
sha256: bf5edcd82513d146ffe53491517b9ff80034c7df11243f0318ba23a8c56f792c
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashCompUTurb.ftn90 — 판독 구간 기록

구간은 1행부터 88행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–51 | `SwashCompUTurb` 입구(1). 기관·저작권 2010–2026·GPL 3 이상·무보증 주석(3–27), 작성자·2023년 신설(30–36). 삼각 격자(triangular mesh)의 3차원 난류모형(turbulence model)으로 난류량을 계산한다는 목적(38–40). 표준 k-ε 난류 폐쇄(standard k-epsilon closure), 수직 혼합(vertical mixing), 수직 유속경사와 바닥마찰에 관한 방법 주석(42–47). Launder와 Spalding의 1974년 논문을 주석에 적는다(49–50). 45–46행 주석은 3차원 난류가 주로 수직 유속경사와 바닥마찰로 생성된다고 설명한다. 46–47행 주석은 그 길이 규모가 일반적으로 수심보다 작다고 설명한다. [10-15 전수 검증 보완] |
| 52–74 | 시작 시 1행 루틴 안. ocpcomm4·SwashCommdata3·outp_data의 lturoutp 사용(54–56). `integer, save :: ient = 0 ! number of entries in this subroutine` (62), STPNOW 선언(63). 구조·소스 구분 주석(65–70), `if (ltrace) call strace (ient,'SwashCompUTurb')` (71), 난류량 계산 주석(73–74). |
| 75–88 | 시작 시 1행 루틴 안. `if ( iturb == 1 ) then` (75)은 표준 k-ε 주석(77) 뒤 `call SwashUKepsMod` (79), `if (STPNOW()) return` (80). 분기 종료(82). 출력용 평균 난류량 갱신 주석(84–85). `if ( lturoutp ) call SwashAverOutp ( 3 )` (86). 루틴 종료(88). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 75–86: 난류모형 호출은 iturb=1에만 있다. 출력 평균 호출은 iturb 분기 밖에서 lturoutp만 검사한다.
