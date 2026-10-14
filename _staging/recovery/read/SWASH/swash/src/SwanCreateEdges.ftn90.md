---
file: models/SWASH/raw/source_code/swash/src/SwanCreateEdges.ftn90
lines: 194
sha256: 75f3fc8b50a74da2f25ac035be2b786dab69c4827bc4e73633de7576ba1db543
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwanCreateEdges.ftn90 — 판독 구간 기록

구간은 1행부터 194행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–50 | SwanCreateEdges 루틴 입구(1), 기관·작성자·GPL 3 이상·무보증 머리말(2–29), 작성자·2007년 신설 이력(30–36). 변(edge) 기반 자료구조(data structure)를 생성한다는 목적(38–40). 삼각형 요소(element)로부터 면(face)을 계산해 저장한다는 방법(42–44). ocpcomm4·SwanGriddata 사용(48–49). |
| 51–80 | 시작 시 1행 SwanCreateEdges 루틴 안. implicit none(51), `ient = 0` (55)과 면·꼭짓점(vertex)·반복 인덱스·최대 면 수(55–65), 2×3 vf(66)를 선언한다. cntv1·cntv2는 각 끝점별 면 수, iflist1·iflist2는 끝점별 면 번호 목록인 할당 가능 배열(68–71). facefound 논리값(73), 구조·실행부 표제 주석(75–80). [10-15 전수 검증 보완] |
| 81–106 | 시작 시 1행 SwanCreateEdges 루틴 안. `if (ltrace) call strace (ient,'SwanCreateEdges')` (81). `maxnf = 3*ncells   ! maximum number of faces` (85), `istat = 0` (87), `if(.not.allocated(kvertf)) allocate (kvertf(2,maxnf), stat = istat)` (88). `if ( istat /= 0 ) then` (89)이면 `call msgerr ( 4, 'Allocation problem in SwanCreateEdges: array kvertf ' )` (90)을 호출한다. 이어 `return` (91)한다. `kvertf = 0` (93), cntv1·cntv2(nverts), iflist1·iflist2(nverts,10) 할당(95–98). 초기화 대입문은 `cntv1   =  0` (100), `cntv2   =  0` (101), `iflist1 = -1` (102), `iflist2 = -2` (103), `nfaces = 0` (105)이다. [10-15 전수 검증 보완] |
| 107–143 | 시작 시 1행 SwanCreateEdges 루틴 안. `do j = 1, ncells` (107)에서 `v1 = kvertc(1,j)` (109), `v2 = kvertc(2,j)` (110), `v3 = kvertc(3,j)` (111)로 세 꼭짓점을 얻는다. 면별 끝점 대입문은 `vf(1,1) = v2` (113), `vf(2,1) = v3` (114), `vf(1,2) = v3` (115), `vf(2,2) = v1` (116), `vf(1,3) = v1` (117), `vf(2,3) = v2` (118)이다. `kloop: do k = 1, 3` (120)에서 `v1 = vf(1,k)` (124)와 `v2 = vf(2,k)` (125)로 두 끝점을 가져온다. `facefound = .false.` (129)로 탐색 표시를 초기화한다. `mloop: do m = 1, 10` (131) 안에서 `iface = iflist1(v1,m)` (133)로 면 번호를 얻는다. `do n = 1, 10` (135)에서 `if ( iflist2(v2,n) == iface ) then` (136)이면 `facefound = .true.` (137)로 기존 면을 찾았다고 표시한다. 이어 `exit mloop` (138)로 반복을 벗어난다. 내부 루프 종료(139–142). [10-15 전수 검증 보완] |
| 144–162 | 시작 시 `do j = 1, ncells` (107)와 `kloop: do k = 1, 3` (120) 안이다. kloop는 `enddo kloop` (188)로 닫힌다. j 반복은 `enddo` (190)로 닫힌다. `if ( .not.facefound ) then` (144)은 역방향 끝점 순서로 탐색한다. `nloop: do n = 1, 10` (146), `iface = iflist2(v1,n)` (148), `do m = 1, 10` (150)의 `if ( iflist1(v2,m) == iface ) then` (151)이면 `facefound = .true.` (152)로 탐색 표시를 설정한다. 이어 `exit nloop` (153)로 반복을 벗어난다. 루프·조건 종료(154–159) 뒤 `if ( facefound ) cycle kloop` (161)로 중복 면을 건너뛴다. [10-15 전수 검증 보완] |
| 163–194 | 163–188행은 `do j = 1, ncells` (107) 안의 `kloop: do k = 1, 3` (120)에 속한다. kloop는 `enddo kloop` (188)로 닫힌다. j 반복은 `enddo` (190)로 닫힌다. 192행 배열 해제는 두 반복 밖에 있다. nfaces를 증가시키고 `if ( nfaces > maxnf ) then` (164)이면 `call msgerr ( 4, 'inconsistency found in SwanCreateEdges: more than maximum allowable faces found ' )` (165)을 호출한다. 이어 `return` (166)한다. `m = cntv1(v1) +1` (169), `if ( m > 10 ) then` (170)이면 `call msgerr ( 4, 'SwanCreateEdges: more than 10 faces around vertex ' )` (171)을 호출한다. 이어 `return` (172)한다. `cntv1  (v1  ) = m` (174)과 `iflist1(v1,m) = nfaces` (175)로 첫 끝점의 목록을 갱신한다. `m = cntv2(v2) +1` (177), `if ( m > 10 ) then` (178)도 `call msgerr ( 4, 'SwanCreateEdges: more than 10 faces around vertex ' )` (179)을 호출한다. 이어 `return` (180)한다. `cntv2  (v2  ) = m` (182)과 `iflist2(v2,m) = nfaces` (183)로 두 번째 끝점의 목록을 갱신한다. `kvertf(1,nfaces) = v1` (185)과 `kvertf(2,nfaces) = v2` (186)로 면의 두 끝점을 저장한다. kloop·j 루프 종료(188–190), 작업 배열 네 개 해제(192), 루틴 종료(194). 인덱스·카운터 계산 원문: `nfaces = nfaces + 1` (163). [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 97–98·131–157·169–181: 끝점별 탐색 목록 길이와 탐색 상한은 10으로 고정한다. 두 끝점 위치의 카운터를 각각 검사한다.
- 88–93: kvertf가 이미 할당되어 있으면 재할당하지 않고 전체를 0으로 설정한다. 기존 배열의 크기를 검사하는 문장은 없다.
- 95–98: 작업 배열 네 개의 allocate에는 stat 인수가 없다. kvertf 할당에는 stat 검사가 있다(88–92).
