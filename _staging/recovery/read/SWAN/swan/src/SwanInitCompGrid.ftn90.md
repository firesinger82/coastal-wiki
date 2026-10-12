---
file: models/SWAN/raw/source_code/swan/src/SwanInitCompGrid.ftn90
lines: 103
sha256: 580e5c74d6863e56c73a69d88fcd7cc95c186bec51ec9cb0217f5eff23f69c67
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanInitCompGrid.ftn90 — 판독 구간 기록

구간은 1행부터 103행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–52 | `SwanInitCompGrid` 입구(1). 기관·GPL 3 이상·무보증·작성자·갱신 이력(3–36). 비정형 계산 격자(computational grid) 기술 배열을 초기화한다는 목적(38–41). 통신·공통 데이터·일반 배열·병렬·격자 데이터 모듈과 `implicit none`(45–51). |
| 53–67 | 시작 시 1행 루틴 안. 입력 명령 상태 `logcom(7)`는 `intent(inout)`이다(55). 저장 추적 계수의 초기값 선언은 `integer, save :: ient = 0 ! number of entries in this subroutine`(59)이다. 할당 상태 `istat`를 선언한다(60). 구조·소스 안내 주석(62–67). [10-13 전수 검증 보완] |
| 68–88 | 시작 시 1행 루틴 안. 추적 조건은 `if (ltrace) call strace (ient,'SwanInitCompGrid')` (68)이다. `SwanCheckGrid` 호출(72). `istat = 0`(74)으로 할당 상태를 초기화하고 작용밀도 할당 조건 `if(.not.allocated(ac2)) allocate(ac2(MDC,MSC,nverts), stat = istat)` (75)를 실행한다. 실패 조건은 `if ( istat /= 0 ) then` (76)이며 `call msgerr ( 4, 'Allocation problem in SwanInitCompGrid: array ac2 ' )`(77)를 호출한다. 이어 `return`(78)한다. 실패 조건은 79행에서 끝난다. 작용밀도 전체 대입은 `ac2 = 0.`(80)이다. 입력 명령 상태 대입은 `logcom(6) = .true.`(81)이다. 직렬 실행(serial run) 관련 조건은 `if ( .not.logcom(7) ) then` (85)이다. 참 분기의 복사식은 `nvertsg = nverts`(86)와 `ncellsg = ncells`(87)이다. 직렬 실행 관련 조건은 ELSE 없이 88행에서 끝난다. [10-13 전수 검증 보완] |
| 89–103 | 시작 시 1행 루틴 안. 구조 격자(structured grid) 배열을 빈 배열로 할당한다는 주석(90–91). 할당 조건·크기는 `if ( .not.allocated(KGRPNT) ) allocate(KGRPNT(0,0))` (93); `if ( .not.allocated(KGRBND) ) allocate(KGRBND(0)  )` (94)이다. 대입식은 `MCGRD   = nverts`(98), `MCGRDGL = nvertsg`(99), `MXCGL   = nvertsg`(100)이다. 주석은 `MCGRD` 설정을 `AC1`과 `COMPDA` 할당에 연결한다(96). 전역 y 방향 크기 기본값은 `MYCGL   = 1` (101)이다. 주석·루틴 종료(102–103). [10-13 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 75–80: `ac2`가 이미 할당되어 있으면 재할당하지 않는다. 그 뒤 기존 배열을 포함해 `ac2` 전체를 0으로 설정한다.
- 93–94: 구조 격자 배열이 이미 할당되어 있으면 빈 크기로 다시 할당하지 않는다. 이 루틴에는 기존 배열 크기 검사가 없다.
