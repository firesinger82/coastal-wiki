---
file: models/SWASH/raw/source_code/swash/src/SwanGridobjects.ftn90
lines: 195
sha256: 4fbcec8a3f31f4e513aac5248aae8722451c92d28e3ab9c7133d139178d18cd7
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwanGridobjects.ftn90 — 판독 구간 기록

구간은 1행부터 195행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–56 | SwanGridobjects 모듈 입구(1), 기관·작성자·GPL 3 이상·무보증 머리말(2–29). 2007년 신설·2008년 꼭짓점 속성 BPOL 추가 이력(30–38). 비구조 격자(unstructured grid)의 꼭짓점(vertex)·셀(cell)·면(face) 파생형(derived type)을 보유하는 목적·방법(40–46). 사용 모듈 없음(48–50), implicit none(52), 매개변수 표제(54–56). |
| 57–80 | 시작 시 1행 SwanGridobjects 모듈 안. 꼭짓점 주변 셀 수 상수 `integer, parameter :: MINVERTCELL = 4   ! mininum number of cells around a vertex` (59), `integer, parameter :: MAXVERTCELL = 10  ! maximum number of cells around a vertex` (60). 정수 속성 수 `integer, parameter :: MAXVERTATTI = 7   ! maximum number of attributes of type integer` (62). 정수 슬롯 상수는 `VERTID  = 1` (64), `VMARKER = 2` (65), `VBC     = 3` (68), `VERTF1  = 4` (71), `VERTF2  = 5` (72), `BINDX   = 6` (73), `BPOL    = 7` (74)이다. VMARKER 1/0은 경계/내부, VBC 1/0은 경계조건 있음/없음 주석(66–70). 실수 속성 수 `integer, parameter :: MAXVERTATTR = 2   ! maximum number of attributes of type real` (76), 실수 슬롯 상수는 `VERTX = 1` (78)과 `VERTY = 2` (79)이다. [10-15 전수 검증 보완] |
| 81–107 | 시작 시 1행 SwanGridobjects 모듈 안. `integer, parameter :: MINCELLVERT = 3   ! mininum number of vertices in a cell` (83), `integer, parameter :: MAXCELLVERT = 5   ! maximum number of vertices in a cell` (84), `integer, parameter :: MINCELLFACE = 3   ! mininum number of faces in a cell` (85), `integer, parameter :: MAXCELLFACE = 5   ! maximum number of faces in a cell` (86). 정수 속성 수 `integer, parameter :: MAXCELLATTI = 7   ! maximum number of attributes of type integer` (88). 정수 슬롯 상수는 `CELLID   = 1` (90), `CMARKER  = 2` (91), `NEXTCELL = 3` (94), `CELLRECT = 4` (95), `CELLV1   = 5` (96), `CELLV2   = 6` (97), `CELLV3   = 7` (98)이다. CMARKER 1/0은 경계/내부, NEXTCELL은 반시계 방향 다음 셀, CELLRECT는 비영이면 직사각형이라는 주석(92–95). 실수 속성 수 `integer, parameter :: MAXCELLATTR = 5   ! maximum number of attributes of type real` (100). 실수 슬롯 상수는 `CELLAREA = 1` (102), `CELLCX   = 2` (103), `CELLCY   = 3` (104), `CELLCCX  = 4` (105), `CELLCCY  = 5` (106)이다. 이 상수들은 각각 면적과 도심·외심의 두 좌표 슬롯을 가리킨다(102–106). [10-15 전수 검증 정정] [10-15 전수 검증 보완] |
| 108–146 | 시작 시 1행 SwanGridobjects 모듈 안. 정수 속성 수 `integer, parameter :: MAXFACEATTI = 9   ! maximum number of attributes of type integer` (110). 정수 슬롯 상수는 `FACEID  = 1` (112), `FMARKER = 2` (113), `FACEV1  = 3` (116), `FACEV2  = 4` (117), `FACEC1  = 5` (118), `FACEC2  = 6` (119)이다. 주석의 `face(j)%atti(FMARKER) = 1`은 경계 면을 뜻한다(114). `face(j)%atti(FMARKER) = 0`은 내부 면을 뜻한다(115). 주석은 `face(j)%atti(FACEC1) < face(j)%atti(FACEC2)`를 항상 요구한다(121). 이동 벡터의 정의는 `(second vertex - first vertex)`이다(123). 주석은 첫 셀이 그 벡터의 왼쪽에 있다고 적는다(122). 주석은 두 번째 셀이 그 벡터의 오른쪽에 있다고 적는다(123–124). `FACECL  = 7` (125)과 `FACECR  = 8` (126)은 법선 기준 좌우 셀 슬롯이다. 주석은 법선이 왼쪽에서 오른쪽으로 향한다고 적는다(127–128). `FBTYPE  = 9` (129)는 경계 유형 슬롯이다. 실수 속성 수 `integer, parameter :: MAXFACEATTR = 8   ! maximum number of attributes of type real` (131). 실수 슬롯 상수는 `FACELEN   = 1` (133), `FACENORMX = 2` (134), `FACENORMY = 3` (135), `FACEMX    = 4` (136), `FACEMY    = 5` (137), `FACEDISTC = 6` (138), `FACEDISTG = 7` (140), `FACELINPF = 8` (142)이다. 주석은 이 슬롯들을 길이·법선·중점·외심 사이 거리·도심 사이 거리·보간 계수로 설명한다(133–145). 보간(interpolation) 설명식은 주석 `! q_face = q_r + face(j)%attr(FACELINPF) (q_l - q_r),` (144)에 있다. 보간식의 인덱스 정의는 `l = face(j)%atti(FACECL)`과 `r = face(j)%atti(FACECR)`이다(145). [10-15 전수 검증 보완] |
| 147–165 | 시작 시 1행 SwanGridobjects 모듈 안. 변수·실행부 표제(147–152). geomtype은 행렬식·공변(covariant) 및 반변(contravariant) 기저 성분·면 방향각을 보유한다(153–160). facetype은 atti(MAXFACEATTI), attr(MAXFACEATTR)를 보유한다(162–165). 주석은 `dx1 , dx2`를 `a_(1)`의 두 성분으로 설명한다(155). 주석은 `dy1 , dy2`를 `a_(2)`의 두 성분으로 설명한다(156). 반변 성분의 주석 수식은 `rdx(b) = a^(b)_1` (157)과 `rdy(b) = a^(b)_2` (158)이다. th1·th2는 현재 꼭짓점을 향하는 면의 방향각이다(159). [10-15 전수 검증 보완] |
| 166–186 | 시작 시 1행 SwanGridobjects 모듈 안. celltype은 nov·nof·active, geom(MAXCELLVERT), face(MAXCELLFACE), 정수·실수 속성, updated(MAXCELLVERT)를 보유한다(167–176). verttype은 noc·active·fullupdated, cell(MAXVERTCELL), 정수·실수 속성, updated(MAXVERTCELL)를 보유한다(178–186). fullupdated 주석은 지리·스펙트럼 공간(spectral space) 모두 갱신되었는지를 뜻한다(181). |
| 187–195 | 시작 시 1행 SwanGridobjects 모듈 안. gridtype은 vert_grid·cell_grid·face_grid의 1차원 포인터(pointer) 배열을 보유한다(188–192). target인 gridobject를 선언한다(193). 빈 줄과 모듈 종료(194–195). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 153–186: 파생형 필드 선언에는 기본값 대입이 없다.
- 188–193: gridtype 포인터 선언에는 null() 초기화가 없다.
- 138–145: FACEDISTC·FACEDISTG 주석은 거리를 설명한다. FACELINPF 주석의 식에는 곱셈 기호 없이 괄호가 이어진다. 이 식은 실행문이 아니다.
