---
file: models/SWAN/raw/source_code/swan/src/SwanCompdata.ftn90
lines: 83
sha256: 3dcbfa472c9406f18478b1c6404e331710267ab7af385bbd692297ae5cf07567
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanCompdata.ftn90 — 판독 구간 기록

구간은 1행부터 83행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–50 | `module SwanCompdata` 시작(1). 기관·작성자·GPL 3 이상·무보증 머리말(3–27). 버전과 갱신 이력(30–41). 비정형 격자(unstructured grid)의 계산 데이터를 저장한다는 목적·방법 주석(43–49). 전처리 이력 주석은 `!GRAPH!   43.05, January 2023: wavefront scheduling based on graph levels` (40), `!FXFRO!   43.05, January 2023: wavefront scheduling` (41)이다. `!GRAPH`는 `-fixfront`를 쓰지 않을 때 표시가 제거된다. `!FXFRO`는 `-fixfront`에서 표시가 제거된다. 두 행은 표시 제거 후에도 주석이다. 스위치 이름의 근거는 `models/SWAN/raw/source_code/swan/switch.pl:24`이며 표시 제거의 근거는 같은 파일의 87–88행이다. |
| 51–69 | 시작 시 1행 모듈 안. `use swcomm3`와 `implicit none`(53–55). 경계 다각형(boundary polygon) 수 `nbpol`, 다각형별 경계 꼭짓점 수 `nbpt(10000)` 선언(62–63). `-fixfront`에서 활성화되는 선언은 `!FXFRO    integer                                    :: nfront ! number of wavefronts` (64)이다. 계산 스텐실(computational stencil) `vs(MICMAX)` 선언(66–68). OpenMP의 `!$omp threadprivate(vs)` 지시문(69). |
| 70–83 | 시작 시 1행 모듈 안. 경계 꼭짓점 목록 `blist`, 경계 표지(boundary marker) `bmark`, 자기 부분영역(subdomain)의 경계 꼭짓점 전역 번호 `bvertg`를 저장·할당 가능 2차원 배열로 선언(71–73). `-fixfront` 미사용 시 활성 선언은 `!GRAPH    integer, dimension(:,:), save, allocatable :: flist  ! wavefront list` (74); `!GRAPH    integer, dimension(:,:), save, allocatable :: fptr   ! pointers per wavefront` (75), `!GRAPH    integer, dimension(:)  , save, allocatable :: nfront ! number of wavefronts` (78)이다. `-fixfront` 사용 시 활성 선언은 `!FXFRO    integer, dimension(:)  , save, allocatable :: fronts ! start vertex index of wavefronts` (76); `!FXFRO    integer, dimension(:)  , save, allocatable :: fronte ! end vertex index of wavefronts` (77)이다. 이들은 파면(wavefront) 목록·포인터·시작 및 끝 번호·파면 수를 보유한다. 꼭짓점 목록 `vlist` 선언(79). 소스 본문 주석과 모듈 종료(80–83). [10-13 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 63: `nbpt`의 선언 크기는 10000으로 고정되어 있다.
- 64·74–78: `nfront`는 `-fixfront`에서 스칼라 정수로 선언된다. `-fixfront` 미사용 시 `nfront`는 할당 가능 1차원 정수 배열로 선언된다.
