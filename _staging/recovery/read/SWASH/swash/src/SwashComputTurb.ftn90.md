---
file: models/SWASH/raw/source_code/swash/src/SwashComputTurb.ftn90
lines: 108
sha256: cd10f5fc9fe5fda77f460b78ba250bc28e73d64c6987c0e0492d34037e7e3a92
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashComputTurb.ftn90 — 판독 구간 기록

구간은 1행부터 108행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–51 | `SwashComputTurb` 입구(1). 기관·저작권 2010–2026·GPL 3 이상·무보증 주석(3–27), 작성자·2011년 신설(30–36). 3차원 난류모형(turbulence model)으로 난류량을 계산한다는 목적(38–40). 표준 k-ε 난류 폐쇄(standard k-epsilon closure), 수직 혼합(vertical mixing), 수직 유속경사와 바닥마찰에 관한 방법 주석(42–47). 주석은 3차원 난류가 주로 수직 유속경사와 바닥마찰로 생성된다고 설명한다(45–46). 주석은 그 길이 규모가 보통 수심보다 작다고 설명한다(46–47). Launder와 Spalding의 1974년 논문을 주석에 적는다(49–50). [10-15 전수 검증 보완] |
| 52–75 | 시작 시 1행 루틴 안. ocpcomm4·SwashCommdata3·m_genarr·outp_data의 lturoutp 사용(54–57). `integer, save :: ient = 0 ! number of entries in this subroutine` (63), STPNOW 선언(64), 구조·소스 구분 주석(66–71). `if (ltrace) call strace (ient,'SwashComputTurb')` (72). 난류량 계산 주석(74–75). |
| 76–88 | 시작 시 1행 루틴 안. `if ( oned ) then` (76)으로 1차원 경로. `if ( iturb /= 0 ) then` (80)은 표준 k-ε 주석(82) 뒤 `call SwashKepsMod1DH ( kgrpnt(1,1) )` (84), `if (STPNOW()) return` (85). 난류 사용 조건 종료(87). |
| 89–103 | 시작 시 1행 루틴·76행 `if ( oned ) then` 안에서 `else` (89)로 2차원 경로. `if ( iturb /= 0 ) then` (93)은 표준 k-ε 주석(95) 뒤 `call SwashKepsMod2DH` (97), `if (STPNOW()) return` (98). 난류 사용 조건·차원 분기 종료(100·102). [10-15 전수 검증 보완] |
| 104–108 | 시작 시 1행 루틴 안. 출력용 평균 난류량 갱신 주석(104–105). `if ( lturoutp ) call SwashAverOutp ( 3 )` (106). 루틴 종료(108). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 76–106: `if ( oned ) then` (76)의 참 분기는 `if ( iturb /= 0 ) then` (80)에서 `call SwashKepsMod1DH ( kgrpnt(1,1) )` (84)를 실행한다. 89행 `else` 분기는 `if ( iturb /= 0 ) then` (93)에서 `call SwashKepsMod2DH` (97)를 실행한다. 두 루틴 호출의 주석은 모두 표준 k-ε 모형이다(82·95). `if ( lturoutp ) call SwashAverOutp ( 3 )` (106)은 난류 사용 조건과 차원 분기 밖에 있다. [10-15 전수 검증 정정]
