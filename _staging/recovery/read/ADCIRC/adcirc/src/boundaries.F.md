---
file: models/ADCIRC/raw/source_code/adcirc/src/boundaries.F
lines: 675
sha256: ed67cb7f38c0f3cfae615da42f8e43b765233adaa7db5db4770b10fb7245a47e
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# boundaries.F — 판독 구간 기록

구간은 1행부터 675행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | ADCIRC 저작권 1994–2025, LGPL 3 이상, 무보증·라이선스 안내(1–19). 경계 정의 자료와 루틴을 모듈화하고 NetCDF·XDMF 입출력을 위한 자료 구조를 도입했다는 주석(20–32). global 모듈 등에서 옮긴 코드라는 설명은 원문 주석이다(29–31). |
| 33–98 | `module boundaries`·implicit none(33–35). 경계 길이, 법선(normal) 방향의 코사인·사인과 이전 값, 축약 절점의 법선, 절점·경계 유형·장벽(barrier)·관로(pipe)·수직 벽 경계의 잠김 상태·경계 변·전달 작업 배열을 allocatable로 선언(36–65·89–91). 경계 개수와 작업 인덱스, 유량(flux) 경계 개수 및 ibtype=64 플래그를 선언(67–86). 하천 경계 배열·절점 수·구간 수를 선언(68–72). 기본값 원문은 `LOGICAL :: BndBCRiver     = .FALSE.` (73), `LOGICAL :: NPEBC          = .FALSE. !WJP 03.272018 Non-periodic elevation boundary condition flag` (74). 과거 변수 설명 주석과 빈 줄을 포함한다(88·92–98). |
| 99–134 | `simpleBoundary_t`는 원래 파일 내 순서, XDMF ID, 절점 번호, 0 기준 절점 번호, 시각화 좌표를 가진다(99–108). 수위(elevation) 경계와 단순 유량 경계 배열·카운터를 선언(109–116). `externalFluxBoundary_t`는 외부 장벽의 절점·높이·계수·시각화 좌표를 추가한다(118–130). 기본값은 `integer :: numAttributes = 2` (123), 속성 ID 배열 크기도 2(124). 외부 경계 배열·개수·카운터 및 빈 주석을 포함한다(131–134). |
| 135–180 | `internalFluxBoundary_t`는 ibtype=4·24·64 내부 장벽의 연결 절점, 높이·두 유량 계수, 양쪽 0 기준 절점 번호, 시각화용 유형 속성을 가진다(135–151). `integer :: numAttributes = 4` (140), 속성 ID 크기 4(141). 관로가 있는 ibtype=5·25 형식은 관로 높이·계수·직경을 추가한다(156–174). `integer :: numAttributes = 7` (161), 속성 ID 크기 7(162). 각 형식의 배열·개수·카운터를 선언(152–154·175–177). 지정 유량 유형의 상수 원문은 `integer, parameter :: specifiedFluxBoundaryTypes(5) = (/ 2, 12, 22, 32, 52 /)` (179). 빈 줄·주석 포함(155·178·180). |
| 181–204 | `xdmfMetaData_t`는 ID 생성 여부, 길이 80의 변수명·긴 이름·표준 이름·좌표·단위·양의 방향 문자열과 각 ID, 자료 집합 개수를 보유한다(181–197). 필드 선언에 기본값 대입은 없다. contains와 구분 주석·빈 줄을 포함한다(198–204). |
| 205–224 | `allocateElevationBoundaryLengths()`는 sizes의 mnope를 사용한다(205–214). nvdll과 ibtypee를 mnope 크기로 할당한다(215–216). 문제를 찾기 쉬운 값으로 초기화한다는 주석 아래 두 배열을 -99999로 초기화한다(218–220). 루틴 종료·구분 주석·빈 줄 포함(221–224). |
| 225–248 | `allocateFluxBoundaryLengths()`는 sizes의 mnbou를 사용한다(225–235). nvell·ibtype_orig·ibtype을 mnbou 크기로 할당하고 모두 -99999로 초기화한다(236–243). 주석은 쌍을 이루는 장벽 경계에서 주 절점(primary node)의 수를 저장한다고 설명한다(229–231). 루틴 종료·구분 주석·빈 줄 포함(244–248). |
| 249–268 | `allocateAdcircElevationBoundaryArrays()`는 mnope·mneta를 사용한다(249–257). nbdv(mnope,mneta)와 nbd(mneta)를 할당하고 모두 -99999로 초기화한다(258–263). 루틴 종료와 주석·빈 줄 포함(264–268). |
| 269–323 | `allocateAdcircFluxBoundaryArrays()`는 mnbou·mnvel을 사용한다(269–278). me2gw, 현재·이전 법선, 경계 유형, 외부·내부 장벽 및 관로 속성, 연결 절점, 잠김 상태, 길이·변의 제3 절점·요소(element), 전달 작업 배열과 ZNG 배열을 mnvel 크기로 할당한다(279–296). nbvv의 범위는 `(mnbou,0:mnvel)` (287), 하천 bcrnbvv도 `(mnbou,0:mnvel)`이며 bcrnvell은 mnbou 크기다(299–300). nbv·lbcodei·장벽·관로·ibconn·nbvv·bndlen2o3·bndedge3rd·bndedgeelem·하천 배열을 -99999 또는 실수형 대응 값으로 초기화한다(302–319). 이 블록의 나머지 할당 배열에는 값 대입이 없다. 루틴 종료·주석·빈 줄 포함(320–323). |
| 324–356 | `allocateBoundaryArrays()`의 머리말과 sizes·로그·종료 모듈 사용, i·scratchMessage 선언(324–336). elevationBoundaries(mnope)를 할당하고 `do i=1,nope` (339)에서 각 nodes·xdmf_nodes를 nvdll(i) 크기로 할당한다(338–342). 네 유량 경계 형식 배열을 유형별 개수로 할당하고 네 카운터를 1로 초기화한다(343–350). `do i=1,nbou` (351) 안 `select case(ibtype_orig(i))` (352), `case(0,1,2,10,11,12,20,21,22,30,32,52,94,122)` (353)에서 단순 경계의 nodes·xdmf_nodes를 nvell(i) 크기로 할당한다(354–355). 카운터 식은 `sfCount = sfCount + 1` (356). |
| 357–390 | 시작 시 330행 allocateBoundaryArrays 루틴·351행 i 루프·352행 select 안. 병렬 `case(3,13,23)` (357)는 외부 장벽의 nodes·barlanht·barlancfsp·xdmf_nodes를 할당하고 `efCount = efCount + 1` (362). `case(4,24,64)` (363)는 내부 장벽의 nodes·ibconn·barinht·barincfsb·barincfsp·xdmf_nodes·xdmf_ibconn을 할당하고 `ifCount = ifCount + 1` (371). `case(5,25)` (372)는 관로 형식의 같은 장벽 속성과 pipeht·pipecoef·pipediam 및 XDMF 절점 배열을 할당하고 `ifwpCount = ifwpCount + 1` (384). 각 절점 배열 크기는 nvell(i)이다(358–383). `case default` (385)는 유형 번호를 담은 오류 메시지를 만들고 `terminate(exit_code=ADCIRC_EXIT_FAILURE, message=scratchMessage)`를 호출한다(386–388). select·루프 종료(389–390). |
| 391–432 | 시작 시 330행 allocateBoundaryArrays 루틴 안이며 351행 루프 밖. 수위 경계는 i=1..nope, 각 유량 형식은 i=1..해당 형식 개수의 루프에서 할당된 nodes·xdmf_nodes·장벽·관로 속성·연결 절점 배열을 -99999 또는 -99999.d0으로 초기화한다(391–426). internalFluxBoundary_t의 ibTypeAttribute·leveeGeom과 각 형식의 bGeom·leveeGeom은 이 초기화 블록에서 할당하지 않는다. 루틴 종료와 구분 주석·빈 줄 포함(427–432). |
| 433–448 | `allocateElevationBoundaryArrays()`는 mneta·mnope를 사용한다(433–441). nbdv(mnope,mneta), nvdll(mnope), nbd(mneta), ibtypee(mnope)를 할당한다(442–443). 이 루틴에는 값 초기화나 allocated 검사가 없다. 루틴 종료·주석·빈 줄 포함(444–448). |
| 449–483 | `allocateFluxBoundaryArrays()`는 mnvel·mnbou를 사용한다(449–457). 경계 절점·유형·길이·매핑·현재 법선, 장벽·관로·잠김 상태, nbvv(mnbou,0:mnvel), 경계별 nvell·ibtype·ibtype_orig, 전달·ZNG·하천 배열을 할당한다(458–478). 이 루틴에는 값 초기화나 allocated 검사가 없다. 루틴 종료·주석·빈 줄 포함(479–483). |
| 484–536 | `getBoundarySizesForPrep`는 adcprep에 nbou·nvel·neta·nope를 복사한다(484–504). exist_flux=0으로 시작하여 `do k=1,nbou` (510), `select case(ibtype(k))` (511), `case(2,12,22,32,52)` (512)에서 `exist_flux = exist_flux + size(simpleFluxBoundaries(k)%nodes)` (513). `case default` (514)는 추가 동작이 없다(515). j와 nweir를 0으로 초기화하고 두 번째 k 루프(519–521), `select case(ibtype(k))` (522), `case(4,24,64)` (523)에서 `nweir = nweir + nvell(k)` (524). `case(5,25)` (525)는 미지원 메시지로 terminate를 호출한다(526). `case default` (527)는 추가 동작이 없다(528). select·루프·루틴 종료 및 주석·빈 줄 포함(529–536). |
| 537–570 | `getBoundariesForPrep` 머리말은 XDMF 격자(mesh)에서 읽은 자료를 adcprep의 중복된 변수 구조로 전달하기 위한 루틴이라고 설명한다(537–546). 입구의 인수는 경계 길이·유형·절점·연결 절점, 장벽 계수, 월류보(weir) 절점 쌍, iden·nfover·exist_flux·flux14_ary다(548–550). terminate를 가져온다(551). 경계 배열은 intent(out), flux14_ary는 allocatable intent(out), iden·nfover는 intent(in), exist_flux는 intent(inout)이다(553–568). 지역 i·j·k·nweir 선언·빈 줄 포함(569–570). |
| 571–605 | 시작 시 548행 getBoundariesForPrep 루틴 안. `if (nope.ne.0) then` (571)은 nvdll·nbdv를 출력 배열로 복사한다(572–573). 별도 `if (nbou.ne.0) then` (575)은 nvell·nbvv를 복사한다(576–577). 두 조건 밖에서 ibtypee·ibtype·ibconnr·lbcodei를 복사하고 flux14_ary(exist_flux)를 할당한다(579–583). j·nweir·exist_flux를 0으로 초기화한다(584–586). `do k = 1,nbou` (587), `select case(ibtype(k))` (588), `case(0,10,20,30,40,1,11,21,41)` (589)는 i=1..nvell(k)에서 p_ibconnr(k,i)=0으로 설정한다(590–592). `case(2,12,22,32,52)` (593)는 같은 i 범위에서 모듈 ibconnr(k,i)=0, flux14_ary(exist_flux)=nbvv(k,i) 복사 뒤 `exist_flux = exist_flux + 1` (597), 루프 종료 후 bndbcriver=.false.(599). `case(3,13,23)` (600)는 barlanhtr·barlancfspr를 bar1·bar2로 복사하고 p_ibconnr(k,:) 전체를 0으로 설정한다(601–605). |
| 606–628 | 시작 시 548행 getBoundariesForPrep 루틴·587행 k 루프·588행 select 안. `case(4,24,64)` (606)는 i=1..nvell(k)에서 내부 장벽의 세 속성을 bar1·bar2·bar3에 복사한다(607–610). `nweir = nweir + 1` (612) 뒤 weir(nweir)에 nbvv, weird(nweir)에 ibconnr를 복사한다(613–614). `case(5,25)` (616)는 미지원 메시지로 terminate를 호출한다(617). `case default` (618)는 유닛 6에 미지원 유형 오류를 쓰며 이 분기에는 terminate 호출이 없다(619–620). select·루프·루틴 종료·주석·빈 줄 포함(621–628). |
| 629–651 | `allocateFluxBoundaryArrayTemporaries()`의 머리말은 초기화 뒤 불필요해지는 경계 속성을 임시 보유한다고 설명한다(629–636). sizes의 mnvel·mnbou 사용과 implicit none(637–639). 외부·내부 장벽 속성, 관로 속성, 연결 절점의 R 접미사 배열을 모두 (mnbou,mnvel)로 할당한다(640–645). 값 초기화는 없다. 루틴 종료·주석·빈 줄 포함(646–651). |
| 652–675 | `freeFluxBoundaryArrayTemporaries()`는 임시 외부·내부 장벽 속성, 관로 속성, ibconnr 배열을 deallocate한다(652–668). allocated 검사나 조건 분기는 없다. 루틴 종료·주석·빈 줄과 boundaries 모듈 종료를 포함한다(669–675). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 100·113·179·353: 단순 경계 유형 설명 주석의 목록은 서로 다르다. 실제 할당 case는 32·94·122를 포함한다. 지정 유량 상수 목록은 2·12·22·32·52이다.
- 183–197: xdmfMetaData_t의 createdIDs와 ndset을 포함한 필드 선언에는 기본값 대입이 없다.
- 279–319: allocateAdcircFluxBoundaryArrays는 csii·siii·이전 법선·me2gw·issubmerged64·전달·ZNG 배열을 할당한다. 해당 루틴의 초기화 대입 목록에는 이 배열들이 없다.
- 215–216·236–238·258–259·442–443·458–478: 같은 모듈 배열을 할당하는 여러 루틴이 있다. 이 루틴들은 allocated 검사 없이 allocate한다. 외부 호출 순서는 이 파일에서 확인하지 않았다.
- 338–425: 구조체의 nodes와 경계 속성 배열을 할당·초기화한다. 선언된 bGeom·leveeGeom·ibTypeAttribute의 할당문은 이 파일에 없다.
- 343·351–356·510–513: simpleFluxBoundaries는 numSimpleFluxBoundaries 크기로 할당하고 sfCount로 접근한다. getBoundarySizesForPrep는 전체 경계 순서 k로 simpleFluxBoundaries(k)에 접근한다.
- 583–597: flux14_ary는 명시적 하한 없이 할당한다. exist_flux를 0으로 재설정한 뒤 첫 유량 절점을 flux14_ary(exist_flux)에 대입하고 나서 exist_flux를 증가시킨다.
- 581·589–599: p_ibconnr에는 먼저 모듈 ibconnr 전체를 복사한다. 비유량 경계 분기는 p_ibconnr를 0으로 바꾸지만 지정 유량 분기는 모듈 ibconnr를 0으로 바꾼다.
- 519·566–569·584: getBoundarySizesForPrep의 j는 0 대입 뒤 사용되지 않는다. getBoundariesForPrep의 j도 0 대입 뒤 사용되지 않는다. iden·nfover는 선언된 입력 인수이며 본문에서 참조하지 않는다.
- 571–582: nvdll·nbdv와 nvell·nbvv 복사는 경계 개수 조건 안에 있다. ibtypee·ibtype·ibconnr·lbcodei 복사는 그 조건 밖에 있다.
