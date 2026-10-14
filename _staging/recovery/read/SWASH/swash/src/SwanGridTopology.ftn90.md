---
file: models/SWASH/raw/source_code/swash/src/SwanGridTopology.ftn90
lines: 98
sha256: fb9cbaa0fe0ae401dee46507bed43ebfe19f76d62f7bfeaffd403924ead0495f
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwanGridTopology.ftn90 — 판독 구간 기록

구간은 1행부터 98행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–65 | SwanGridTopology 입구(1), 기관·작성자·GPL 3 이상·무보증 머리말(2–29), 2007년 신설 이력(30–36). SWAN 격자 위상(topology)을 설정한다는 목적 주석(38–40). 격자와 영역 위상을 프로그램의 다른 부분에 유용한 구조로 반환한다는 방법(42–45). ocpcomm4·SwanGriddata·SwanGridobjects 사용(49–51), implicit none(53). `ient = 0` (57)과 할당 상태 istat(57–58), 구조·실행부 표제(60–65). [10-15 전수 검증 보완] |
| 66–77 | 시작 시 1행 SwanGridTopology 루틴 안. `if (ltrace) call strace (ient,'SwanGridTopology')` (66). `allocate(gridobject%vert_grid(nverts), stat = istat)` (70)로 꼭짓점 배열을 할당한다. `if ( istat == 0 ) allocate(gridobject%cell_grid(ncells), stat = istat)` (71), `if ( istat == 0 ) allocate(gridobject%face_grid(nfaces), stat = istat)` (72). `if ( istat /= 0 ) then` (73)이면 `call msgerr ( 4, 'Allocation problem in SwanGridTopology: array vert, cell or face' )` (74)을 호출한다. 이어 `return` (75)한다. 73행 조건은 `endif` (76)으로 닫힌다. [10-15 전수 검증 보완] |
| 78–98 | 시작 시 1행 SwanGridTopology 루틴 안. 꼭짓점(vertex) 구성 `call SwanGridVert ( nverts, xcugrd, ycugrd, vmark )` (80), 셀(cell) 구성 `call SwanGridCell ( ncells, nverts, xcugrd, ycugrd, kvertc )` (84), 면(face) 구성 `call SwanGridFace ( nfaces, ncells, nverts, xcugrd, ycugrd, kvertf )` (88) 순서다. `call SwashBndTopology` (92), `call SwashPrintGridInfo` (96)로 경계 위상 구성과 격자 정보 출력을 수행한다. 각 호출 설명 주석과 루틴 종료(78–98). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 70–76: 객체 배열 할당 앞에 associated 또는 기존 할당 여부를 검사하는 조건은 없다. 할당 실패 분기는 앞서 할당한 배열을 해제하지 않고 return한다.
- 80–96: 구성 루틴 호출 사이에 성공 여부를 검사하는 조건은 없다.
