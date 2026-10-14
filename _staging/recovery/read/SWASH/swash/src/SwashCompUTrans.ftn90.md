---
file: models/SWASH/raw/source_code/swash/src/SwashCompUTrans.ftn90
lines: 86
sha256: c160735898c1730cd4204ecfdecde6243c300c093cf1ea1d44477e9be87de10f
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashCompUTrans.ftn90 — 판독 구간 기록

구간은 1행부터 86행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | `SwashCompUTrans` 입구(1). 기관·저작권 2010–2026·GPL 3 이상·무보증 주석(3–27), 작성자·2023년 신설(30–36). 삼각 격자(triangular mesh)에서 수송방정식(transport equations)을 풀어 성분(constituents)을 계산한다는 목적 주석(38–40). |
| 42–65 | 시작 시 1행 루틴 안. ocpcomm4·SwashCommdata3·outp_data의 ltraoutp·SwashFlowdata 사용(44–47). `integer, save :: ient = 0 ! number of entries in this subroutine` (53), 중단 함수 STPNOW 선언(54). 구조·소스·성분 계산 구분 주석(56–65). `if (ltrace) call strace (ient,'SwashCompUTrans')` (62). |
| 66–81 | 시작 시 1행 루틴 안. `if ( kmax == 1 ) then` (66)은 수심평균(depth-averaged) 경로로 `call SwashExpDepUtrans ( rp(1,1,1), rpo(1,1), rp1(1,1), rp0(1,1), rpi(1,1,0), u1(1,1), qn(1,1), fluxt(1,1) )` (70), `if (STPNOW()) return` (71). `else` (73)는 고정 층수의 층평균(layer-averaged) 경로로 `call SwashExpLayUtrans` (77), `if (STPNOW()) return` (78). 층수 분기 종료(80). |
| 82–86 | 시작 시 1행 루틴 안. 출력용 평균 농도 갱신 주석(82–83). `if ( ltraoutp ) call SwashAverOutp ( 2 )` (84). 루틴 종료(86). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
