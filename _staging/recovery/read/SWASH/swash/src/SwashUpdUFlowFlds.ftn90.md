---
file: models/SWASH/raw/source_code/swash/src/SwashUpdUFlowFlds.ftn90
lines: 125
sha256: fc9cae0428b96613dea95dbc0e2479f93e5527b18b96321d3489e499f4a14471
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashUpdUFlowFlds.ftn90 — 판독 구간 기록

구간은 1행부터 125행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–73 | `SwashUpdUFlowFlds` 시작(1), 기관·저작권·GPL 3 이상·무보증 머리말(2–29). 작성자·2020년 신규 작성 이력(30–36). 삼각 격자(triangular mesh) 유동 변수를 공간 입력장으로 초기화·갱신한다는 목적(38–40). ocpcomm4·SwashCommdata2·m_genarr·SwashFlowdata·SwanGriddata·SwanGridobjects 사용(44–49), implicit none(51). 셀·면 인덱스와 3개 정점, 면 법선(normal)·면 중앙 속도 성분, cell/face 구조체 포인터 선언(55–66). `integer, save         :: ient = 0` (56)으로 초기화한다. 구조·소스 시작 주석(68–73). [10-15 전수 검증 보완] |
| 74–100 | 시작 시 1행 루틴 안. `if (ltrace) call strace (ient,'SwashUpdUFlowFlds')` (74). `cell => gridobject%cell_grid` (78), `face => gridobject%face_grid` (79)로 연결한다. `if ( initsf .or. ifldyn(7) == 1 ) then` (81)에서 `do icell = 1, ncells` (85), `v(1) = cell(icell)%atti(CELLV1)` (89), `v(2) = cell(icell)%atti(CELLV2)` (90), `v(3) = cell(icell)%atti(CELLV3)` (91), `s1(icell) = ( wlevf(v(1),2) + wlevf(v(2),2) + wlevf(v(3),2) )/ 3.` (93)로 셀 수위를 계산한다. 95행 `enddo` 뒤 `initsf = .false.` (97)로 바꾼다. 조건 종료(99). [10-15 전수 검증 보완] |
| 101–125 | 시작 시 1행 루틴 안이며 99행에서 닫힌 81행 `if ( initsf .or. ifldyn(7) == 1 ) then` 블록 밖. `if ( inituf .or. ifldyn(2) == 1 ) then` (101)에서 `do iface = 1, nfaces` (105), `v(1) = face(iface)%atti(FACEV1)` (107), `v(2) = face(iface)%atti(FACEV2)` (108), `nx = face(iface)%attr(FACENORMX)` (110), `ny = face(iface)%attr(FACENORMY)` (111). `ux = 0.5 * ( uxf(v(1),2) + uxf(v(2),2) )` (113), `uy = 0.5 * ( uyf(v(1),2) + uyf(v(2),2) )` (114), `u1(iface,1) = nx * ux + ny * uy` (116)로 면 법선 속도를 계산한다. 118행 `enddo` 뒤 `inituf = .false.` (120), `initvf = .false.` (121)를 대입한다, 조건·루틴 종료(123–125). 이 파일에는 switch.pl 대상 표지나 !DIFF·!MUD·!TEST·!VEGE 표지 행이 없다. [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 101·120–121: 유속 갱신 조건은 inituf 또는 ifldyn(2)==1만 검사한다. 해당 갱신 뒤에는 inituf와 initvf를 모두 .false.로 바꾼다.
- 116: u1 갱신 대상의 두 번째 인덱스는 1로 고정된다. 이 파일에는 다른 두 번째 인덱스의 u1 대입이 없다.
