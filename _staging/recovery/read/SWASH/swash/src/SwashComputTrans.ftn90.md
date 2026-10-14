---
file: models/SWASH/raw/source_code/swash/src/SwashComputTrans.ftn90
lines: 113
sha256: 22745607a05ee98f93c78a184e7bf20eb1ba083b501e6c2ea9cfe89525c56f12
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashComputTrans.ftn90 — 판독 구간 기록

구간은 1행부터 113행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | `SwashComputTrans` 입구(1). 기관·저작권 2010–2026·GPL 3 이상·무보증 주석(3–27), 작성자·2013년 신설(30–36). 수송방정식(transport equations)으로 성분(constituents)을 계산한다는 목적 주석(38–40). |
| 42–66 | 시작 시 1행 루틴 안. ocpcomm4·SwashCommdata3·m_genarr·outp_data의 ltraoutp·SwashFlowdata 사용(44–48). `integer, save :: ient = 0 ! number of entries in this subroutine` (54), STPNOW 선언(55), 구조·소스 구분 주석(57–62). `if (ltrace) call strace (ient,'SwashComputTrans')` (63). 성분 계산 주석(65–66). |
| 67–86 | 시작 시 1행 루틴 안. `if ( oned ) then` (67)은 1차원 경로. `if ( kmax == 1 ) then` (71)은 수심평균(depth-averaged) 수송으로 `call SwashExpDep1DHtrans ( rp(1,1,1), rpo(1,1), u1(1,1), qx(1,1), flux(1,1,1), ibl(1), ibr(1), kgrpnt(1,1) )` (75), `if (STPNOW()) return` (76). `else` (78)는 고정 층수의 층평균(layer-averaged) 수송으로 `call SwashExpLay1DHtrans ( ibl(1), ibr(1), kgrpnt(1,1) )` (82), `if (STPNOW()) return` (83). 층수 분기 종료(85). |
| 87–108 | 시작 시 1행 루틴·67행 `if ( oned ) then` 안에서 `else` (87)로 2차원 경로. `if ( kmax == 1 ) then` (91)은 `call SwashExpDep2DHtrans ( rp(1,1,1), rpo(1,1), u1(1,1), qx(1,1), v1(1,1), qy(1,1), flux(1,1,1) )` (95), `if (STPNOW()) return` (96). `else` (98)는 `call SwashExpLay2DHtrans` (102), `if (STPNOW()) return` (103). 층수·차원 분기 종료(105·107). [10-15 전수 검증 보완] |
| 109–113 | 시작 시 1행 루틴 안. 출력용 평균 농도 갱신 주석(109–110). `if ( ltraoutp ) call SwashAverOutp ( 2 )` (111). 루틴 종료(113). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
