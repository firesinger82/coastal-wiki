---
file: models/SWASH/raw/source_code/swash/src/SwashPrintGridInfo.ftn90
lines: 176
sha256: fb5cd6ccedd9361915d44fb90b41772cef72b469112e26856793c46e9f3b256f
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashPrintGridInfo.ftn90 — 판독 구간 기록

구간은 1행부터 176행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–51 | `SwashPrintGridInfo` 시작(1). 기관·SWASH 비정수압(non-hydrostatic) 파랑·흐름 모델·2010–2026 저작권·GPL 3 이상·무보증 주석(3–27). 저자·2023년 신설 이력(30–36), 격자(mesh) 관련 정보 출력 목적(38–40). ocpcomm4·SwanGriddata·SwanGridobjects 사용(44–46), implicit none·지역변수 절 머리말(48–51). |
| 52–79 | 시작 시 1행 SwashPrintGridInfo 루틴 안. `ient = 0` (52)·면 반복 인덱스 iface·내부 셀/면 개수 ncellsi/nfacesi 선언(52–55). 평균/현재 격자 간격 avegsiz/gridsize·평균용 개수 npav·인접 외심(circumcenter) 거리 역수 rdx 선언(57–60). 길이 80 문자열 두 개 helptxt·셀/면 객체 포인터 cell/face 선언(62–65). 구조·의사코드·Source text 주석(67–72). `if (ltrace) call strace (ient,'SwashPrintGridInfo')` (73). `cell => gridobject%cell_grid` (77). `face => gridobject%face_grid` (78), 구분 주석(79). [10-15 전수 검증 보완] |
| 80–107 | 시작 시 1행 루틴 안. `if ( grid_generator == meth_adcirc ) then` (80)은 삼각형 전용·SMS/ADCIRC 문자열(84–85), `elseif ( grid_generator == meth_triangle ) then` (87)은 삼각형 전용·Triangle(91–92), `elseif ( grid_generator == meth_easy ) then` (94)은 삼각형 전용·Easymesh(98–99) 문자열을 쓴다. `else` (101)는 삼각형 또는 혼합 셀(hybrid cell)·unknown 문자열을 쓴다(103–104). 조건 종료·주석(106–107). |
| 108–124 | 시작 시 1행 루틴 안. 내부 면·셀 개수는 `nfacesi = nfaces - nfacesb` (110), `ncellsi = ncells - ncellsb` (111). 격자 종류·생성기를 PRINTF에 출력한다(115). 정점은 전체 개수 `nverts`를 출력한다(115). 셀은 `ncells`, `ncellsi`, `ncellsb`를 출력한다(115–116). 면은 `nfaces`, `nfacesi`, `nfacesb`를 출력한다(116). 최소·최대·평균 격자 간격 계산 머리말(118–119). 초기값은 `mingsiz = 1.0e10` (120), `maxgsiz = 0.0` (121), `avegsiz = 0.` (122), `npav    = 0.` (123), 구분 주석(124). [10-15 전수 검증 정정] |
| 125–155 | 시작 시 1행 루틴 안. `do iface = 1, nfaces` (125)·`if ( face(iface)%atti(FMARKER) == 0 ) then   ! internal face` (127)은 내부 면만 처리한다. `rdx = face(iface)%attr(FACEDISTG)` (131). 129행 주석은 인접 도심(centroid) 거리 역수라고 적는다. `if ( rdx /= 0. ) then` (133)이면 `gridsize = 1./rdx` (137). `if ( gridsize < mingsiz ) then` (141)은 `mingsiz = gridsize` (142)로 최소값을 바꾸고, `elseif ( gridsize > maxgsiz ) then` (143)은 `maxgsiz = gridsize` (144)로 최대값을 바꾼다. 이 IF/ELSEIF 사슬에는 ELSE가 없다(141–145). 조건 종료(145) 후 `avegsiz = avegsiz + gridsize` (147), `npav    = npav    + 1.` (148). rdx 조건은 150행에서 닫힌다. 내부 면 조건은 152행에서 닫힌다. iface 루프는 154행에서 닫힌다. 구분 주석(151·153·155). [10-15 전수 검증 보완] |
| 156–176 | 시작 시 1행 루틴 안이며 iface 루프 밖. `avegsiz = avegsiz / npav` (156). 최소·최대·평균 격자 간격 출력(158–160). format 100은 비구조 격자(unstructured grid)의 종류·생성기·정점/셀/면 개수와 내부/경계 개수 형식이고, 200/300/400은 각 격자 간격을 f12.5로 출력한다(162–174). 주석·루틴 종료(175–176). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 64·77: cell은 포인터 선언과 gridobject%cell_grid 연결 이후 이 루틴에서 참조되지 않는다.
- 60·129–131: rdx 선언 주석은 외심 사이 거리 역수라고 쓰고, 실행부 주석은 도심 사이 거리 역수라고 쓴다. 두 설명 모두 FACEDISTG 값을 가리킨다.
- 120–145: 최소값 갱신과 최대값 갱신은 if/elseif이다. 최소값이 갱신되는 반복에서는 최대값 조건을 평가하지 않는다.
- 123·125–156: npav는 내부 면이면서 rdx/=0인 경우에만 증가한다. 루프 뒤 avegsiz/npav 앞에는 npav=0을 검사하는 조건이 없다.
