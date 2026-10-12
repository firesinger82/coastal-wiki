---
file: models/SWAN/raw/source_code/swan/src/SwanGridTopology.ftn90
lines: 94
sha256: a8fd7e4d6e9004fcdeac91ff0239b94550ba2324b29663f42c7fbcadd3f8818c
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanGridTopology.ftn90 — 판독 구간 기록

구간은 1행부터 94행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–54 | `SwanGridTopology` 입구(1). 기관·GPL 3 이상·무보증·작성자·갱신 이력(3–36). 격자 위상(grid topology)을 설정하고 프로그램에서 쓸 격자·지역 연결 정보를 구조에 담는 목적·방법(38–45). 통신·격자 데이터·격자 객체 모듈과 `implicit none`(49–53). |
| 55–76 | 시작 시 1행 루틴 안. 저장 추적 계수 `ient = 0`, 할당 상태 `istat` 선언(57–58). 구조·소스 안내 주석(60–65). 추적 조건·호출은 `if (ltrace) call strace (ient,'SwanGridTopology')` (66)이다. 꼭짓점 객체 배열을 `nverts`로 할당한다(70). 앞 할당 성공 조건은 `if ( istat == 0 ) allocate(gridobject%cell_grid(ncells), stat = istat)` (71); `if ( istat == 0 ) allocate(gridobject%face_grid(nfaces), stat = istat)` (72)이며 순서대로 셀 `ncells`와 면 `nfaces` 배열을 할당한다. 실패 조건은 `if ( istat /= 0 ) then` (73)이며 `call msgerr ( 4, 'Allocation problem in SwanGridTopology: array vert, cell or face' )`(74)를 호출한다. 이 분기는 `return`(75)으로 반환한다. 실패 조건은 76행에서 닫힌다. [10-13 전수 검증 보완] |
| 77–94 | 시작 시 1행 루틴 안. 꼭짓점 설정 `SwanGridVert(nverts,xcugrd,ycugrd,vmark)` 호출(80). 셀 설정 `SwanGridCell(ncells,nverts,xcugrd,ycugrd,kvertc)` 호출(84). 면 설정 `SwanGridFace(nfaces,ncells,nverts,xcugrd,ycugrd,kvertf)` 호출(88). 정보 출력 `SwanPrintGridInfo` 호출(92). 각 호출 안내 주석과 루틴 종료(77–94). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 70–76: 세 객체 배열은 순서대로 할당된다. 후속 할당 실패 시 앞에서 성공한 배열을 해제하는 문장은 이 오류 분기에 없다.
- 80–92: 세 격자 설정 루틴과 정보 출력 루틴을 연속으로 호출한다. 각 호출 사이에 반환 상태를 검사하는 문장은 이 파일에 없다.
