---
file: models/SWAN/raw/source_code/swan/src/SwanVTKWriteData.ftn90
lines: 207
sha256: 6b0bc2d3a22b9c2592137776646bd1f1b2fef802fc03d425c759b2ae268ee7e0
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanVTKWriteData.ftn90 — 판독 구간 기록

구간은 1행부터 207행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–45 | SwanVTKWriteData 시작(1). 기관·GPL 3 이상·무보증 머리말(3–27), 저자·2022년 이력(30–36). VTK 파일에 후첨 데이터(appended data)를 쓰는 목적(38–40). VTK 형식 문서 URL은 원문의 방법 주석이다(44). |
| 46–82 | 시작 시 1행 SwanVTKWriteData 루틴 안. ocpcomm4·swcomm1·m_parall·outp_data·SwanGriddata·SwanGridobjects 사용(48–53), implicit none(55). 입력 길이 lenp·격자 크기 mxk/myk·변수 수 nvar·장치번호 uvtk, ivtyp·변수 위치 voqr·부분영역 번호 ionod, real*4 data(mxk*myk,*)·pstype 선언(59–72). 원문 고정값은 `integer     , parameter :: datasize = 4             ! number of bytes of integers and reals` (76); `integer     , parameter :: ndim = 3                 ! space dimension` (77); `! (set to 3 as required by Paraview)` (78); `integer     , parameter :: nov = 3                  ! number of vertices in cell (triangles only)` (79); `integer*1   , parameter :: ptype = 5                ! polygon type (5 = triangle)` (80); `character(1), parameter :: lf = char(10)            ! line feed character` (81). 수치 자료 크기=4바이트, 공간 차원=3, 삼각형(triangle) 정점 수=3, 셀 타입=5(integer*1), 줄바꿈=char(10)이다. |
| 83–119 | 시작 시 1행 루틴 안. 인덱스·`integer, save           :: ient = 0                 ! number of entries in this subroutine` (86)·I/O 상태 ios·변수 종류·integer*4 nbytes·정점 번호 v1/v2/v3·msgstr(80)·celltype 포인터 선언(85–100). 구조·소스 주석(102–107), `if (ltrace) call strace (ient,'SwanVTKWriteData')` (108). `cell => gridobject%cell_grid` (112)로 셀 포인터를 연결한다. `ios = 0` (114)으로 출력 상태를 초기화한다. `iproc = INODE` (116)로 현재 프로세서 번호를 얻는다. [10-13 전수 검증 보완] |
| 120–135 | 시작 시 1행 루틴 안. jvar=1..nvar 루프(120), `ivtype = ivtyp(jvar)` (122)로 변수 종류 복사. `if ( ovsvty(ivtype) < 3 ) then        ! scalars` (124)이면 스칼라(scalar) 데이터 길이 `nbytes = lenp * datasize` (126), `if ( ios == 0 ) write(uvtk,iostat=ios) nbytes` (128)로 길이 출력. j=1..myk·i=1..mxk 루프(129·131), `ip = (j-1)*mxk` (130)로 선형 인덱스 계산, `if ( ios == 0 .and. ionod(ip+i) == iproc ) write(uvtk,iostat=ios) data(ip+i,voqr(ivtype))` (132)로 현재 프로세서 소속 데이터만 출력. [10-13 전수 검증 보완] |
| 136–151 | 시작 시 1행 루틴·120행 jvar 루프 안이며 124행의 병렬 `else                                  ! vectors (three components per node!)` (136). 벡터(vector) 길이는 `nbytes = ndim * lenp * datasize` (138), `if ( ios == 0 ) write(uvtk,iostat=ios) nbytes` (140)로 길이 출력. j·i 루프(141·143), `ip = (j-1)*mxk` (142). `if ( ios == 0 .and. ionod(ip+i) == iproc ) write(uvtk,iostat=ios) data(ip+i,voqr(ivtype)), data(ip+i,voqr(ivtype)+1), 0.` (144)로 voqr(ivtype), voqr(ivtype)+1의 두 성분과 세 번째 성분 0을 출력. 분기·변수 루프 종료(148·150). |
| 152–163 | 시작 시 1행 루틴 안이며 변수 루프 밖. 좌표는 세 성분이며 z=0이라는 주석(152–153). `nbytes = ndim * lenp * datasize` (155), `if ( ios == 0 ) write(uvtk,iostat=ios) nbytes` (156)로 길이 출력. j·i 루프(157·159), `ip = (j-1)*mxk` (158), `if ( ios == 0 .and. ionod(ip+i) == iproc ) write(uvtk,iostat=ios) data(ip+i,voqr(1)), data(ip+i,voqr(2)), 0.` (160)로 현재 프로세서의 voqr(1)·voqr(2)·0 좌표 출력. |
| 164–177 | 시작 시 1행 루틴 안. `if ( pstype == 'U' ) then` (164)일 때 비구조 격자(unstructured grid) 연결 목록(connectivity) 출력. `nbytes = nov * ncells * datasize` (169), `if ( ios == 0 ) write(uvtk,iostat=ios) nbytes` (170)로 길이 출력. j=1..ncells 루프(171), `v1 = cell(j)%face(1)%atti(FACEV1) -1` (172); `v2 = cell(j)%face(2)%atti(FACEV1) -1` (173); `v3 = cell(j)%face(3)%atti(FACEV1) -1` (174)로 FACEV1 정점 번호를 0 시작 인덱스로 변환, `if ( ios == 0 ) write(uvtk,iostat=ios) v1, v2, v3` (175)로 세 정점 출력. |
| 178–191 | 시작 시 1행 루틴·164행 U 분기 안. 연결 배열에서 각 셀 끝 위치(offset)의 길이는 `nbytes = ncells * datasize` (180), `if ( ios == 0 ) write(uvtk,iostat=ios) nbytes` (181)로 길이 출력·`if ( ios == 0 ) write(uvtk,iostat=ios) (j, j=nov, nov*ncells, nov)` (182)로 3·6·…·3×ncells 출력. 셀 타입 길이는 `nbytes = ncells * datasize` (186), `if ( ios == 0 ) write(uvtk,iostat=ios) nbytes` (187)로 길이 출력·`if ( ios == 0 ) write(uvtk,iostat=ios) (ptype, j=1, ncells)` (188)로 ptype을 ncells번 출력. U 조건 종료(190). |
| 192–207 | 시작 시 1행 루틴 안. 줄바꿈을 포함한 AppendedData 종료 문자열(192), `if ( ios == 0 ) write(uvtk,iostat=ios) trim(vtkline)` (193)로 출력. VTKFile 종료 문자열(197), `if ( ios == 0 ) write(uvtk,iostat=ios) trim(vtkline)` (198)로 출력. `if ( ios /= 0 ) then` (202)이면 iostat 값을 메시지로 만들고 msgerr(2) 호출(203–204). 루틴 종료(207). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 76·80·186–188: ptype은 integer*1이며 값은 5이다. 셀 타입 블록 길이 nbytes는 ncells*datasize로 계산하며 datasize는 4이다. 실제 셀 타입 출력 목록은 ptype을 ncells번 반복한다.
- 77–80·144·160·169–182: 공간 차원과 셀 정점 수는 3으로 고정되어 있다. 벡터와 좌표의 세 번째 성분은 0으로 출력한다. 연결 목록은 삼각형만 처리한다.
- 126–146·155–162: 데이터 블록 길이는 lenp를 사용한다. 실제 출력문은 `ios == 0 .and. ionod(ip+i) == iproc` 조건을 모두 만족할 때만 실행한다(132·144·160). iproc는 INODE에서 복사한다(116). 이 루틴에는 두 개수의 일치 여부를 검사하는 실행문이 없다. [10-13 전수 검증 정정] [10-13 전수 검증 보완]
- 112·164–190: cell 포인터 연결은 pstype 분기 전에 수행한다. 셀 속성을 참조하는 실행문은 pstype=U 분기에만 있다.
