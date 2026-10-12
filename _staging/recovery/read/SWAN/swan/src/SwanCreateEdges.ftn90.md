---
file: models/SWAN/raw/source_code/swan/src/SwanCreateEdges.ftn90
lines: 194
sha256: 80779b165ef57b1d3375ccc49829a1e8a8786b3770dedfa31a4d2341c38c18e3
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanCreateEdges.ftn90 — 판독 구간 기록

구간은 1행부터 194행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–52 | `SwanCreateEdges` 입구(1). 기관·GPL 3 이상·무보증·작성자·새 루틴 이력(3–36). 삼각형(triangle) 요소에서 면(face)을 구해 변(edge) 기반 자료구조를 생성한다는 목적·방법(38–44). 통신·격자 데이터 모듈과 `implicit none`(48–51). 빈 주석(52). |
| 53–80 | 시작 시 1행 루틴 안. 면 번호, 할당 상태, 순회·계수 변수, 최대 면 수, 세 꼭짓점과 면별 꼭짓점 쌍 `vf(2,3)` 선언(55–66). 꼭짓점별 계수 `cntv1/cntv2`, 면 번호 목록 `iflist1/iflist2`를 할당 가능 배열로 선언한다(68–71). 면 발견 플래그 선언(73). `ient = 0` 초기값(55). 구조·소스 안내 주석(75–80). [10-13 전수 검증 보완] |
| 81–106 | 시작 시 1행 루틴 안. 추적 조건·호출은 `if (ltrace) call strace (ient,'SwanCreateEdges')` (81)이다. 최대 면 수 식은 `maxnf = 3*ncells   ! maximum number of faces` (85)이다. 할당 조건은 `if(.not.allocated(kvertf)) allocate (kvertf(2,maxnf), stat = istat)` (88)이다. 실패 조건은 `if ( istat /= 0 ) then` (89)이며 `call msgerr ( 4, 'Allocation problem in SwanCreateEdges: array kvertf ' )`(90)를 호출한다. 이 분기는 `return`(91)으로 반환한다. 조건은 92행에서 닫힌다. `kvertf = 0`(93)으로 초기화한다. 계수 배열은 `nverts`, 면 목록 배열은 `(nverts,10)`으로 할당한다(95–98). 계수 초기값은 `cntv1   =  0`(100), `cntv2   =  0`(101)이다. 목록 초기값은 `iflist1 = -1`(102), `iflist2 = -2`(103)이다. 면 수 초기값은 `nfaces = 0`(105)이다. 할당 상태 초기값은 `istat = 0`(87)이다. [10-13 전수 검증 보완] |
| 107–160 | 시작 시 1행 루틴 안. `do j = 1, ncells`(107)에서 세 꼭짓점을 읽고 마주 보는 세 면의 끝점 쌍을 `(v2,v3)`, `(v3,v1)`, `(v1,v2)`로 저장한다(109–118). `kloop: do k = 1, 3`(120)에서 면 발견 플래그를 거짓으로 두고 `mloop: do m = 1, 10` 및 `do n = 1, 10`(131·135)으로 목록을 검색한다. 일치 조건은 `if ( iflist2(v2,n) == iface ) then` (136)이다. 일치 시 `mloop`를 종료한다(137–139). 반대 순서 검색 조건은 `if ( .not.facefound ) then` (144)이다. 그 안의 `nloop: do n = 1, 10` 및 `do m = 1, 10`(146·150)의 일치 조건은 `if ( iflist1(v2,m) == iface ) then` (151)이다. 일치 시 `nloop`를 종료한다(152–154). 검색 조건 종료·주석(157–160). 셀 꼭짓점 대입은 `v1 = kvertc(1,j)`(109), `v2 = kvertc(2,j)`(110), `v3 = kvertc(3,j)`(111)이다. 면 끝점 대입은 `vf(1,1) = v2`(113), `vf(2,1) = v3`(114), `vf(1,2) = v3`(115), `vf(2,2) = v1`(116), `vf(1,3) = v1`(117), `vf(2,3) = v2`(118)이다. 검색 끝점은 `v1 = vf(1,k)`(124), `v2 = vf(2,k)`(125)이다. 검색 초기값은 `facefound = .false.`(129)이다. 첫 검색은 `iface = iflist1(v1,m)`(133)를 읽는다. 일치 시 `facefound = .true.`(137)를 설정한다. 반대 검색은 `iface = iflist2(v1,n)`(148)를 읽는다. 일치 시 `facefound = .true.`(152)를 설정한다. 첫 일치 조건은 139행에서 닫힌다. 첫 내부 루프와 `mloop`는 각각 140행과 142행에서 닫힌다. 두 번째 일치 조건은 154행에서 닫힌다. 두 번째 내부 루프와 `nloop`는 각각 155행과 157행에서 닫힌다. 반대 검색 조건은 159행에서 닫힌다. [10-13 전수 검증 보완] |
| 161–194 | 시작 시 1행 루틴·107행 셀 루프·120행 면 루프 안. 발견된 면 건너뛰기는 `if ( facefound ) cycle kloop` (161)이다. 면 수 증가식은 `nfaces = nfaces + 1` (163)이다. 최대 면 수 검사 `if ( nfaces > maxnf ) then` (164)의 참 분기는 `call msgerr ( 4, 'inconsistency found in SwanCreateEdges: more than maximum allowable faces found ' )`(165)를 호출한다. 이 분기는 `return`(166)으로 반환한다. 조건은 167행에서 닫힌다. 첫 끝점 목록 위치식은 `m = cntv1(v1) +1` (169)이며 검사 조건은 `if ( m > 10 ) then` (170)이다. 실패하면 오류 후 반환하고, 성공하면 계수와 목록을 저장한다(171–175). 두 번째 끝점 목록 위치식은 `m = cntv2(v2) +1` (177), 검사 조건은 `if ( m > 10 ) then` (178)이다. 같은 오류 처리를 거쳐 두 번째 목록을 저장한다(179–183). 면 끝점 번호 저장(185–186). 면·셀 루프 종료(188–190). 네 작업 배열 해제·루틴 종료(192–194). 첫 끝점 초과 분기는 `call msgerr ( 4, 'SwanCreateEdges: more than 10 faces around vertex ' )`(171)를 호출한다. 이 분기는 `return`(172)으로 반환한다. 조건은 173행에서 닫힌다. 첫 목록 저장식은 `cntv1  (v1  ) = m`(174), `iflist1(v1,m) = nfaces`(175)이다. 두 번째 초과 분기는 같은 메시지의 `call msgerr ( 4, 'SwanCreateEdges: more than 10 faces around vertex ' )`(179)를 호출한다. 이 분기는 `return`(180)으로 반환한다. 조건은 181행에서 닫힌다. 두 번째 목록 저장식은 `cntv2  (v2  ) = m`(182), `iflist2(v2,m) = nfaces`(183)이다. 면 끝점 저장식은 `kvertf(1,nfaces) = v1`(185), `kvertf(2,nfaces) = v2`(186)이다. [10-13 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 97–98·131–157·170–180: 면 목록의 두 번째 차원과 검색 범위는 10으로 고정되어 있다. 새 면의 끝점별 계수가 10을 넘으면 오류를 보고하고 반환한다.
- 95–98·164–180·192: 작업 배열을 할당한 뒤 발생하는 세 초과 검사 분기는 192행의 명시적 `deallocate`에 도달하기 전에 반환한다.
- 88·93: `kvertf`가 이미 할당되어 있으면 재할당하지 않는다. 그 뒤에는 배열 전체를 0으로 설정한다. 기존 배열의 크기를 검사하는 문장은 이 블록에 없다.
