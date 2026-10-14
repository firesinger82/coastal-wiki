---
file: models/SWASH/raw/source_code/swash/src/SwanPointinMesh.ftn90
lines: 127
sha256: 86eb928432fe0a98569bc5b32fb936ee4c677f0653d55c0cddbb78143b0684e7
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwanPointinMesh.ftn90 — 판독 구간 기록

구간은 1행부터 127행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–60 | `logical function SwanPointinMesh ( x, y )` (1), 기관·작성자·GPL 3 이상·무보증 머리말(2–29), 2007년 신설 이력(30–36). 점에서 수직선을 그어 경계 면(face) 교차 수가 홀수이면 격자 내부라는 목적·방법(38–45). ocpcomm4·SwanGriddata·SwanGridobjects·SwanCompdata 사용(49–52), implicit none(54), 입력 좌표 x·y(58–59). |
| 61–93 | 시작 시 1행 SwanPointinMesh 함수 안. `ient = 0` (63)과 면·경계 반복 인덱스·교차 수·끝점 번호(64–68), 좌표·교차 y좌표(70–74), face 포인터(pointer)(76), 구조·실행부 표제(78–83). `if (ltrace) call strace (ient,'SwanPointinMesh')` (84), face 연결(88), `numcrs = 0` (90), 경계 면 루프 주석(92–93). [10-15 전수 검증 보완] |
| 94–117 | 시작 시 1행 SwanPointinMesh 함수 안. `do jb = 1, nfacesb` (94)에서 `iface = jbface(jb)` (96)로 경계 면을 얻는다. `v1 = face(iface)%atti(FACEV1)` (98)과 `v2 = face(iface)%atti(FACEV2)` (99)로 끝점을 얻는다. 좌표 대입문은 `x1 = xcugrd(v1)` (101), `y1 = ycugrd(v1)` (102), `x2 = xcugrd(v2)` (103), `y2 = ycugrd(v2)` (104)이다. `if ( ( (x1 > x) .and. (x2 <= x) ) .or. ( (x2 > x) .and. (x1 <= x) ) ) then` (106)의 `if ( y1 > y .or. y2 > y ) then` (108)은 `yc = y1 + (x-x1) * (y2-y1) / (x2-x1)` (110), `if ( yc > y ) numcrs = numcrs + 1` (111)이다. 두 분기·경계 루프 종료(113–117). [10-15 전수 검증 보완] |
| 118–127 | 시작 시 1행 SwanPointinMesh 함수 안. 홀수 교차 수 설명(119–120). `if ( mod(numcrs,2) == 1 ) then` (121)은 `SwanPointinMesh = .true.` (122)를 대입한다. `else` (123)는 `SwanPointinMesh = .false.` (124)를 대입한다. 조건·함수 종료(125–127). [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
