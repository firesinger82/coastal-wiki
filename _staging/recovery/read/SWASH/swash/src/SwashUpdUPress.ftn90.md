---
file: models/SWASH/raw/source_code/swash/src/SwashUpdUPress.ftn90
lines: 116
sha256: d69976b150756147edc6ef91839f542ff233fd09b6430cec6a3a9e3a88e1d042
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashUpdUPress.ftn90 — 판독 구간 기록

구간은 1행부터 116행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–73 | `SwashUpdUPress` 시작(1), 기관·저작권·GPL 3 이상·무보증 머리말(2–29). 작성자·2023년 신규 작성 이력(30–36). 삼각 격자(triangular mesh) 대기압(atmospheric pressure)을 공간 입력장으로 초기화·갱신한다는 목적(38–40). 필요할 때 개방 경계(open boundary) 수위를 보정한다는 주석(41). ocpcomm4·SwashCommdata2/3·m_genarr·SwashFlowdata·SwanGriddata·SwanGridobjects·SwanCompdata 사용(45–52). 경계 유형·셀/면 인덱스·경계 면 루프·셀 정점 3개·cell/face 포인터 선언(58–66). `integer, save         :: ient = 0` (60)으로 초기화한다. 구조·소스 시작 주석도 포함한다(68–73). [10-15 전수 검증 정정] [10-15 전수 검증 보완] |
| 74–98 | 시작 시 1행 루틴 안. `if (ltrace) call strace (ient,'SwashUpdUPress')` (74). `cell => gridobject%cell_grid` (78), `face => gridobject%face_grid` (79)로 연결한다. `if ( ifldyn(13) == 1 ) then` (81) 안에서 `do icell = 1, ncells` (85), `v(1) = cell(icell)%atti(CELLV1)` (89), `v(2) = cell(icell)%atti(CELLV2)` (90), `v(3) = cell(icell)%atti(CELLV3)` (91), `patm(icell) = ( presf(v(1),2) + presf(v(2),2) + presf(v(3),2) )/ 3.` (93)로 셀 대기압을 평균한다. 루프·입력장 조건 종료(95–97). [10-15 전수 검증 보완] |
| 99–116 | 시작 시 1행 루틴 안이며 97행에서 닫힌 81행 `if ( ifldyn(13) == 1 ) then` 블록 밖. `if ( prmean > 0. ) then` (101) 안에서 `do jf = 1, nfacesb` (103). `iface = jbface(jf)` (105), `icell = face(iface)%atti(FACEC1)` (106), `btype = face(iface)%atti(FBTYPE)` (108)를 대입한다. `if ( btype == 2 ) bcs(iface) = bcs(iface) + ( prmean - patm(icell) ) / (rhow*grav)` (110)로 해당 경계 수위를 보정한다. 루프·prmean 조건·루틴 종료(112–116). 이 파일에는 switch.pl 대상 표지나 !DIFF·!MUD·!TEST·!VEGE 표지 행이 없다. [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
