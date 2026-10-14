# SWASH 판독 기록 전수 검증 — code-1

검증일은 2026-10-15이다.
대상은 사용자 지정 기록 22개이다.
대조 원문은 각 기록 frontmatter의 `file:`이다.
각 구간을 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
한 번에 연 원문 구간은 200행 이하이다.
구간 표의 162행이 가리키는 원문 3,962행을 모두 대조했다.
구간 밖의 기록 내 코드 사실도 해당 원문과 대조했다.

정정·보완은 유형별로 변경한 구간 표 행 수이다.
같은 구간에 정정과 보완이 있으면 두 유형에서 각각 센다.
중복 집계한 구간은 `src/SwanGridobjects.ftn90.md:81–107`과 `src/SwanInterpolatePoint.ftn90.md:64–106`이다.
이상 없음은 정정·보완이 모두 필요하지 않았던 구간 표 행 수이다.
아래 숫자는 대상 기록의 구간 표와 이 보고서의 변경 목록에서 집계했다.

| 기록 | 대조한 구간 표 행 수 | 대조한 원문 행 수 | 원문 범위 | 정정 | 보완 | 이상 없음 |
|---|---:|---:|---|---:|---:|---:|
| [CMakeLists.txt.md](../swash/CMakeLists.txt.md) | 7 | 63 | 1–63 | 0 | 0 | 7 |
| [Makefile.md](../swash/Makefile.md) | 5 | 41 | 1–41 | 1 | 0 | 4 |
| [README.md.md](../swash/README.md.md) | 12 | 264 | 1–264 | 1 | 1 | 10 |
| [bin/swashrun.bat.md](../swash/bin/swashrun.bat.md) | 7 | 86 | 1–86 | 0 | 0 | 7 |
| [bin/swashrun.md](../swash/bin/swashrun.md) | 7 | 137 | 1–137 | 0 | 6 | 1 |
| [clobber.cmake.md](../swash/clobber.cmake.md) | 3 | 18 | 1–18 | 0 | 0 | 3 |
| [misc/machinefile.md](../swash/misc/machinefile.md) | 2 | 8 | 1–8 | 0 | 0 | 2 |
| [misc/swash.edt.md](../swash/misc/swash.edt.md) | 29 | 343 | 1–343 | 0 | 1 | 28 |
| [src/CMakeLists.txt.md](../swash/src/CMakeLists.txt.md) | 6 | 88 | 1–88 | 0 | 3 | 3 |
| [src/SwanBpntlist.ftn90.md](../swash/src/SwanBpntlist.ftn90.md) | 14 | 509 | 1–509 | 0 | 13 | 1 |
| [src/SwanCompdata.ftn90.md](../swash/src/SwanCompdata.ftn90.md) | 2 | 66 | 1–66 | 0 | 0 | 2 |
| [src/SwanCreateEdges.ftn90.md](../swash/src/SwanCreateEdges.ftn90.md) | 6 | 194 | 1–194 | 0 | 5 | 1 |
| [src/SwanFindPoint.ftn90.md](../swash/src/SwanFindPoint.ftn90.md) | 4 | 173 | 1–173 | 0 | 3 | 1 |
| [src/SwanGridCell.ftn90.md](../swash/src/SwanGridCell.ftn90.md) | 13 | 418 | 1–418 | 0 | 12 | 1 |
| [src/SwanGridFace.ftn90.md](../swash/src/SwanGridFace.ftn90.md) | 11 | 441 | 1–441 | 0 | 10 | 1 |
| [src/SwanGridTopology.ftn90.md](../swash/src/SwanGridTopology.ftn90.md) | 3 | 98 | 1–98 | 0 | 2 | 1 |
| [src/SwanGridVert.ftn90.md](../swash/src/SwanGridVert.ftn90.md) | 3 | 108 | 1–108 | 0 | 2 | 1 |
| [src/SwanGriddata.ftn90.md](../swash/src/SwanGriddata.ftn90.md) | 3 | 86 | 1–86 | 0 | 0 | 3 |
| [src/SwanGridobjects.ftn90.md](../swash/src/SwanGridobjects.ftn90.md) | 7 | 195 | 1–195 | 1 | 4 | 3 |
| [src/SwanInterpolateOutput.ftn90.md](../swash/src/SwanInterpolateOutput.ftn90.md) | 8 | 251 | 1–251 | 0 | 7 | 1 |
| [src/SwanInterpolatePoint.ftn90.md](../swash/src/SwanInterpolatePoint.ftn90.md) | 6 | 248 | 1–248 | 1 | 5 | 1 |
| [src/SwanPointinMesh.ftn90.md](../swash/src/SwanPointinMesh.ftn90.md) | 4 | 127 | 1–127 | 0 | 3 | 1 |
| 합계 | 162 | 3962 | 각 기록의 전체 구간 | 4 | 77 | 83 |

조건식·계산식·상수·초기값의 인용을 대조했다.
분기의 부정·수량·순서와 블록 종료 행을 대조했다.
셸·배치·빌드·설정 파일의 명령·기본값·버전 표기를 대조했다.
`swash/switch.pl` 57–66행의 전처리 규칙을 확인했다.
대상 원문에는 그 규칙으로 활성화되는 행 첫머리 표시가 없었다.
`SwanBpntlist.ftn90` 439·477행의 `!TEST`는 그 규칙에 없었다.
기존 기록은 두 `!TEST` 행이 주석으로 남는다는 사실을 올바르게 적었다.
대상 원문에는 수직 층의 `k-1`을 위층·아래층으로 해석할 계산 블록이 없었다.
`SwanGridFace.ftn90` 350행의 `lower/south boundary`는 경계 위치 주석이다.
`SwanGridobjects.ftn90` 157–158행의 주석 수식은 해당 기록에 보완했다.

아래 기록 경로는 `_staging/recovery/read/SWASH/swash/` 기준이다.
원문 행은 각 기록의 `file:`이 가리키는 원문 기준이다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [Makefile.md](../swash/Makefile.md):27–35 (정정) | $(CURDIR)를 저장소 최상위 경로로 단정했다. | $(CURDIR)를 make의 현재 작업 디렉터리로 고쳤다. | 35 |
| [README.md.md](../swash/README.md.md):41–74 (정정) | oneAPI HPC Toolkit과 OpenMP를 컴파일러 예시로 함께 나열했다. | 컴파일러는 gfortran과 Intel Fortran Compiler Classic으로 한정했다. oneAPI HPC Toolkit의 포함 관계와 두 컴파일러의 OpenMP 지원을 명시했다. | 60–64 |
| [README.md.md](../swash/README.md.md):122–156 (보완) | 설치를 생략할 수 있다는 설명에서 비권고 조건을 누락했다. | 설치 생략을 권고하지 않는다는 원문의 단서를 추가했다. | 155 |
| [bin/swashrun.md](../swash/bin/swashrun.md):1–15 (보완) | input·npmpi·npomp의 초기값을 설명만 했다. | 초기화 대입문 세 개를 원문으로 인용했다. | 7–9 |
| [bin/swashrun.md](../swash/bin/swashrun.md):29–60 (보완) | 오류 출력 명령과 mpi 초기화를 요약만 했다. | 오류 메시지·사용법 출력 명령과 mpi=1을 인용했다. 각 분기와 반복의 닫힘 행을 명시했다. | 34–60 |
| [bin/swashrun.md](../swash/bin/swashrun.md):61–80 (보완) | machinefile 생성 표시 hfc=1을 코드로 인용하지 않았다. | hfc=1을 원문 코드로 인용했다. | 69 |
| [bin/swashrun.md](../swash/bin/swashrun.md):81–99 (보완) | orig의 초기값과 변경값을 코드로 인용하지 않았다. | orig=n·orig=y를 인용했다. 실행 모드 분기의 닫힘 행을 명시했다. | 82·90–99 |
| [bin/swashrun.md](../swash/bin/swashrun.md):100–119 (보완) | 바깥 입력 분기를 이름만 적었다. inode 초기화를 코드로 인용하지 않았다. | 바깥 조건식과 fi 위치를 추가했다. inode=0과 출력 분기의 fi 위치를 추가했다. | 81·100–119·133–136 |
| [bin/swashrun.md](../swash/bin/swashrun.md):120–137 (보완) | 바깥 입력 분기를 이름만 적었다. | 바깥 조건식을 인용했다. 참 분기가 끝나는 행과 else·fi 위치를 명시했다. | 81·120–136 |
| [misc/swash.edt.md](../swash/misc/swash.edt.md):270–281 (보완) | SOLVer 항목을 추가 해법이라고만 적었다. | SOLVer가 IMPL에 이어지는 문법임을 명시했다. | 275–277 |
| [src/CMakeLists.txt.md](../swash/src/CMakeLists.txt.md):1–16 (보완) | WIN32·UNIX 분기에서 ELSE 유무와 닫힘 위치를 적지 않았다. | ELSE가 없음을 명시했다. 플랫폼·컴파일러·MPI 조건의 닫힘 행을 추가했다. | 2–15 |
| [src/CMakeLists.txt.md](../swash/src/CMakeLists.txt.md):34–53 (보완) | 바깥 컴파일러 분기를 이름만 적었다. Intel 플랫폼 분기의 ELSE 유무를 적지 않았다. | 바깥 IF 원문과 ENDIF 위치를 추가했다. Intel 플랫폼 분기에 ELSE가 없음을 명시했다. | 25·34–52 |
| [src/CMakeLists.txt.md](../swash/src/CMakeLists.txt.md):71–88 (보완) | 실행 파일 생성 조건과 설치 명령의 경계를 적지 않았다. 설치 플랫폼 분기의 ELSE 유무를 적지 않았다. | 생성 조건의 ENDIF가 설치 명령 앞에 있음을 명시했다. 설치 플랫폼 분기에 ELSE가 없음을 명시했다. | 72–88 |
| [src/SwanBpntlist.ftn90.md](../swash/src/SwanBpntlist.ftn90.md):59–128 (보완) | idebug와 ient 초기화를 설명만 했다. | idebug=0과 ient = 0을 원문으로 인용했다. | 72–75 |
| [src/SwanBpntlist.ftn90.md](../swash/src/SwanBpntlist.ftn90.md):129–178 (보완) | BINDX·BPOL·nbpt·blistot 초기화와 vc 선택 대입문을 생략했다. | 초기화 대입문과 각 후보를 vc에 넣는 원문을 추가했다. | 147–178 |
| [src/SwanBpntlist.ftn90.md](../swash/src/SwanBpntlist.ftn90.md):179–195 (보완) | 첫 꼭짓점과 탐색 변수의 초기화를 요약만 했다. | 첫 꼭짓점 저장식과 다각형·카운터·면 번호 초기화를 인용했다. | 182–194 |
| [src/SwanBpntlist.ftn90.md](../swash/src/SwanBpntlist.ftn90.md):196–246 (보완) | 현재 셀·면 매핑과 vn·firstvert 초기화를 요약만 했다. | 셀·꼭짓점·면 매핑 대입문과 vn·firstvert 설정을 인용했다. | 202–244 |
| [src/SwanBpntlist.ftn90.md](../swash/src/SwanBpntlist.ftn90.md):247–276 (보완) | 바깥 경계 면 조건을 이름만 적었다. 꼭짓점 저장식과 카운터 초기화를 요약했다. | 바깥 조건식·블록 종료 행을 추가했다. v1·v2 및 목록 저장식과 icntfc 초기화를 인용했다. | 196·198·250–275·324·328·354 |
| [src/SwanBpntlist.ftn90.md](../swash/src/SwanBpntlist.ftn90.md):277–324 (보완) | 바깥 분기식을 생략했다. ELSE가 없는 분기 사슬과 저장·초기화 대입문을 생략했다. | 바깥 조건·닫힘 행·ELSE 부재를 명시했다. 다각형 저장·초기화 대입문을 추가했다. | 196·198·253·277–328·354 |
| [src/SwanBpntlist.ftn90.md](../swash/src/SwanBpntlist.ftn90.md):325–354 (보완) | 바깥 경계 면 조건을 이름만 적었다. 탐색 실패 메시지의 내용을 생략했다. | 바깥 조건식을 추가했다. 328행 뒤는 경계 면 조건 밖임을 명시했다. msgerr 호출 원문을 추가했다. | 196·198·325–354 |
| [src/SwanBpntlist.ftn90.md](../swash/src/SwanBpntlist.ftn90.md):355–370 (보완) | 잘못된 경계 꼭짓점의 메시지 생성을 요약만 했다. | 목록 인덱스 대입과 메시지 작성·msgerr 호출 원문을 추가했다. | 364–367 |
| [src/SwanBpntlist.ftn90.md](../swash/src/SwanBpntlist.ftn90.md):371–400 (보완) | 할당 상태·배열·카운터 초기화와 목록 인덱스 저장을 요약했다. | 초기화·목록 저장 대입문과 할당 실패 메시지를 인용했다. | 376–393 |
| [src/SwanBpntlist.ftn90.md](../swash/src/SwanBpntlist.ftn90.md):401–429 (보완) | 출력 곡선의 형식·점 수·좌표 저장·LOPS 값을 요약했다. | 출력 곡선의 설정식과 좌표 인덱스 대입문을 인용했다. | 406–424 |
| [src/SwanBpntlist.ftn90.md](../swash/src/SwanBpntlist.ftn90.md):430–464 (보완) | VMMAX·MIP·JJ 초기값과 목록 인덱스 저장식 및 ELSE 부재를 생략했다. | 초기화·목록 인덱스 대입문을 인용했다. JJ 분기 사슬에 ELSE가 없음을 명시했다. | 432–463 |
| [src/SwanBpntlist.ftn90.md](../swash/src/SwanBpntlist.ftn90.md):465–478 (보완) | 바깥 VM 반복을 이름만 적었다. 배열 복사식과 ISH 초기값을 생략했다. | 바깥 DO와 블록 종료 행을 명시했다. 배열 복사식과 ISH = 0을 인용했다. | 442·465–476·505–506 |
| [src/SwanBpntlist.ftn90.md](../swash/src/SwanBpntlist.ftn90.md):479–509 (보완) | 바깥 MIP 조건을 이름만 적었다. 출력 곡선과 좌표 인덱스 대입문을 생략했다. | 바깥 DO·IF와 닫힘 위치를 추가했다. 곡선 설정 및 IARR2·blist·좌표 저장식을 인용했다. | 442·465·479–506 |
| [src/SwanCreateEdges.ftn90.md](../swash/src/SwanCreateEdges.ftn90.md):51–80 (보완) | ient 초기값을 코드로 인용하지 않았다. | ient = 0을 인용했다. | 55 |
| [src/SwanCreateEdges.ftn90.md](../swash/src/SwanCreateEdges.ftn90.md):81–106 (보완) | 할당 상태·배열·카운터 초기값을 설명만 했다. | 초기화 대입문과 할당 실패 메시지를 인용했다. | 87–105 |
| [src/SwanCreateEdges.ftn90.md](../swash/src/SwanCreateEdges.ftn90.md):107–143 (보완) | 꼭짓점·면 인덱스 매핑과 facefound 설정을 요약했다. | kvertc·vf·iflist1 매핑 대입문과 facefound 설정을 인용했다. | 109–137 |
| [src/SwanCreateEdges.ftn90.md](../swash/src/SwanCreateEdges.ftn90.md):144–162 (보완) | 바깥 반복을 이름만 적었다. 역방향 목록 대입문과 탐색 표시를 요약했다. | 바깥 DO와 종료 행을 추가했다. iface·facefound 대입문을 인용했다. | 107·120·148–159·188–190 |
| [src/SwanCreateEdges.ftn90.md](../swash/src/SwanCreateEdges.ftn90.md):163–194 (보완) | 바깥 반복을 이름만 적었다. 오류 메시지와 끝점별 저장식을 요약했다. | 바깥 DO와 종료 행을 명시했다. 서로 다른 오류 메시지와 끝점별 인덱스 저장식을 인용했다. | 107·120·163–190 |
| [src/SwanFindPoint.ftn90.md](../swash/src/SwanFindPoint.ftn90.md):59–96 (보완) | ient 초기값을 코드로 인용하지 않았다. | ient = 0을 인용했다. | 61 |
| [src/SwanFindPoint.ftn90.md](../swash/src/SwanFindPoint.ftn90.md):97–124 (보완) | 미발견 값·좌표 매핑·최소 거리 갱신 대입문을 요약했다. | kvert·xc·yc·dismin 대입문을 인용했다. | 101–120 |
| [src/SwanFindPoint.ftn90.md](../swash/src/SwanFindPoint.ftn90.md):125–173 (보완) | 바깥 SwanPointinMesh 조건을 이름만 적었다. 좌표 매핑과 끝점 선택 대입문을 요약했다. | 바깥 조건식과 종료 행을 명시했다. 면·꼭짓점·좌표 매핑 및 kvert 대입문을 인용했다. | 106·125–171 |
| [src/SwanGridCell.ftn90.md](../swash/src/SwanGridCell.ftn90.md):66–120 (보완) | ient 초기값을 코드로 인용하지 않았다. | ient = 0을 인용했다. | 69 |
| [src/SwanGridCell.ftn90.md](../swash/src/SwanGridCell.ftn90.md):121–156 (보완) | 카운터·셀 속성·꼭짓점 초기화를 요약했다. | 초기화와 셀·꼭짓점 인덱스 대입문을 인용했다. | 128–155 |
| [src/SwanGridCell.ftn90.md](../swash/src/SwanGridCell.ftn90.md):157–173 (보완) | 바깥 반복을 이름만 적었다. 면적 저장식을 요약했다. | DO와 종료 행을 추가했다. CELLAREA 저장식을 인용했다. | 132·164·302 |
| [src/SwanGridCell.ftn90.md](../swash/src/SwanGridCell.ftn90.md):174–206 (보완) | 바깥 반복을 이름만 적었다. 공변 성분과 각도 저장식을 요약했다. | DO와 종료 행을 추가했다. 기저·각도 저장식과 내부 무한 반복의 종료 행을 추가했다. | 132·179–182·196–199·302 |
| [src/SwanGridCell.ftn90.md](../swash/src/SwanGridCell.ftn90.md):207–233 (보완) | 바깥 반복을 이름만 적었다. CVLEFT와 도심 초기값·저장식을 요약했다. | DO와 종료 행을 추가했다. 방향 표시와 도심 초기화·저장식을 인용했다. | 132·213–232·302 |
| [src/SwanGridCell.ftn90.md](../swash/src/SwanGridCell.ftn90.md):234–280 (보완) | 바깥 반복을 이름만 적었다. 교차 수 초기화와 끝점 매핑을 요약했다. | DO와 종료 행을 추가했다. 좌표 매핑과 numcrs 초기값 및 ccn 닫힘 행을 추가했다. | 132·236–280·302 |
| [src/SwanGridCell.ftn90.md](../swash/src/SwanGridCell.ftn90.md):281–302 (보완) | 바깥 반복을 이름만 적었다. 외심·도심·면 끝점 저장식을 요약했다. | DO와 종료 행을 추가했다. 외심·도심 선택과 면 끝점 인덱스 대입문을 인용했다. | 132·284–302 |
| [src/SwanGridCell.ftn90.md](../swash/src/SwanGridCell.ftn90.md):303–330 (보완) | 꼭짓점 ID 매핑과 주변 셀 수 초기화를 요약했다. | vc·ivlist·noc 대입문과 반복 종료 행을 추가했다. | 323–330 |
| [src/SwanGridCell.ftn90.md](../swash/src/SwanGridCell.ftn90.md):331–352 (보완) | 셀 꼭짓점·ivlist·주변 셀 저장을 요약했다. | 꼭짓점 매핑과 주변 셀 번호 저장식을 인용했다. | 334–346 |
| [src/SwanGridCell.ftn90.md](../swash/src/SwanGridCell.ftn90.md):353–380 (보완) | 주변 셀 수와 셀·꼭짓점 매핑을 요약했다. | 주변 셀 수 및 셀·꼭짓점 대입문을 인용했다. | 356–368 |
| [src/SwanGridCell.ftn90.md](../swash/src/SwanGridCell.ftn90.md):381–400 (보완) | 바깥 반복을 이름만 적었다. nxtcell 초기화와 후보 셀 매핑을 요약했다. | 바깥 DO와 종료 행을 추가했다. nxtcell·jcell·꼭짓점 대입문을 인용했다. | 354·360·381–416 |
| [src/SwanGridCell.ftn90.md](../swash/src/SwanGridCell.ftn90.md):401–418 (보완) | 바깥 반복을 이름만 적었다. nxtcell과 NEXTCELL 저장을 요약했다. | 중첩 DO의 닫힘 위치를 명시했다. nxtcell 및 NEXTCELL 대입문을 인용했다. | 354·360·383·401–416 |
| [src/SwanGridFace.ftn90.md](../swash/src/SwanGridFace.ftn90.md):65–121 (보완) | ient 초기값을 코드로 인용하지 않았다. | ient = 0을 인용했다. | 73 |
| [src/SwanGridFace.ftn90.md](../swash/src/SwanGridFace.ftn90.md):122–170 (보완) | 면 번호·끝점 저장과 면 속성 초기화를 요약했다. | 면 번호·끝점·길이 저장식과 0 초기화 대입문을 인용했다. | 136–166 |
| [src/SwanGridFace.ftn90.md](../swash/src/SwanGridFace.ftn90.md):171–203 (보완) | 카운터·목록 초기화와 끝점별 면 저장을 요약했다. | 초기값·인덱스 저장식·상한 초과 메시지 원문을 인용했다. | 176–200 |
| [src/SwanGridFace.ftn90.md](../swash/src/SwanGridFace.ftn90.md):204–257 (보완) | 탐색의 면 인덱스·발견 표시·실패 메시지를 요약했다. | 양방향 탐색의 면 인덱스와 논리값 설정 및 실패 메시지를 인용했다. | 214–256 |
| [src/SwanGridFace.ftn90.md](../swash/src/SwanGridFace.ftn90.md):258–284 (보완) | 바깥 반복·인접 셀 저장·방향 오류 처리를 요약했다. | 바깥 DO와 닫힘 행을 명시했다. 끝점·인접 셀 대입문과 오류 메시지를 인용했다. | 206·210·258–283 |
| [src/SwanGridFace.ftn90.md](../swash/src/SwanGridFace.ftn90.md):285–318 (보완) | 좌우 셀의 선택·저장과 법선 복사를 요약했다. | 좌우 셀 매핑과 법선 저장 대입문을 인용했다. 법선 방향 주석을 추가했다. | 294–317 |
| [src/SwanGridFace.ftn90.md](../swash/src/SwanGridFace.ftn90.md):319–360 (보완) | 바깥 반복을 이름만 적었다. 보간 계수·거리 예외값과 도심 매핑을 요약했다. | DO와 IF의 닫힘 행을 추가했다. 계수·거리의 0 대입문과 경계 좌표 매핑을 인용했다. | 287·321–359·416–418 |
| [src/SwanGridFace.ftn90.md](../swash/src/SwanGridFace.ftn90.md):361–400 (보완) | 바깥 분기를 이름만 적었다. 내부 면의 좌표 매핑과 거리 예외값을 요약했다. | 바깥 IF의 ELSE와 닫힘 행을 명시했다. 외심·중점·도심 매핑 및 거리 0 대입문을 인용했다. | 287·321·361–399·416–418 |
| [src/SwanGridFace.ftn90.md](../swash/src/SwanGridFace.ftn90.md):401–419 (보완) | 바깥 조건을 이름만 적었다. 오른쪽 도심과 거리 예외값을 요약했다. | 바깥 IF의 ELSE 범위를 명시했다. 도심 좌표와 거리 0 대입문을 인용했다. | 287·321·361·403–418 |
| [src/SwanGridFace.ftn90.md](../swash/src/SwanGridFace.ftn90.md):420–441 (보완) | 경계 셀 표시 초기화·설정과 면 인덱스 복사를 요약했다. | CMARKER 초기화·설정 및 iface 대입문을 인용했다. | 424–434 |
| [src/SwanGridTopology.ftn90.md](../swash/src/SwanGridTopology.ftn90.md):1–65 (보완) | ient 초기값을 코드로 인용하지 않았다. | ient = 0을 인용했다. | 57 |
| [src/SwanGridTopology.ftn90.md](../swash/src/SwanGridTopology.ftn90.md):66–77 (보완) | 첫 배열 할당과 할당 실패 메시지를 요약했다. | 첫 allocate 명령과 오류 메시지 및 분기 닫힘 행을 추가했다. | 70–76 |
| [src/SwanGridVert.ftn90.md](../swash/src/SwanGridVert.ftn90.md):62–80 (보완) | ient 초기값을 코드로 인용하지 않았다. | ient = 0을 인용했다. | 64 |
| [src/SwanGridVert.ftn90.md](../swash/src/SwanGridVert.ftn90.md):81–108 (보완) | 꼭짓점 번호·경계 표시·활성 표시와 좌표 저장식을 요약했다. | VERTID·VBC·active 초기값과 좌표 저장식을 인용했다. | 87–104 |
| [src/SwanGridobjects.ftn90.md](../swash/src/SwanGridobjects.ftn90.md):57–80 (보완) | 꼭짓점 속성 상수를 원문 대입식 없이 나열했다. | 정수·실수 속성의 상수 대입식을 인용했다. | 64–79 |
| [src/SwanGridobjects.ftn90.md](../swash/src/SwanGridobjects.ftn90.md):81–107 (정정) | CELLRECT의 rectangle을 사각형으로 넓혀 적었다. | 원문 rectangle을 직사각형으로 고쳤다. | 95 |
| [src/SwanGridobjects.ftn90.md](../swash/src/SwanGridobjects.ftn90.md):81–107 (보완) | 셀 속성 상수를 원문 대입식 없이 나열했다. | 정수·실수 속성의 상수 대입식을 인용했다. | 90–106 |
| [src/SwanGridobjects.ftn90.md](../swash/src/SwanGridobjects.ftn90.md):108–146 (보완) | 면 속성 상수와 보간식의 좌우 인덱스 정의를 생략했다. 꼭짓점 이동 벡터 방향을 적지 않았다. | 속성 상수를 인용했다. FMARKER 값과 두 번째 꼭짓점에서 첫 번째 꼭짓점을 빼는 벡터 정의 및 보간식의 l·r 정의를 추가했다. | 112–145 |
| [src/SwanGridobjects.ftn90.md](../swash/src/SwanGridobjects.ftn90.md):147–165 (보완) | 기저 성분을 요약하면서 주석의 반변 성분 수식을 생략했다. | 공변 성분의 대응과 주석 수식 rdx(b) = a^(b)_1·rdy(b) = a^(b)_2를 추가했다. | 155–159 |
| [src/SwanInterpolateOutput.ftn90.md](../swash/src/SwanInterpolateOutput.ftn90.md):74–113 (보완) | ient 초기값을 코드로 인용하지 않았다. | ient = 0을 인용했다. | 77 |
| [src/SwanInterpolateOutput.ftn90.md](../swash/src/SwanInterpolateOutput.ftn90.md):114–131 (보완) | 전체 복사와 출력 예외값 초기화를 요약했다. | foutp 대입문과 조기 반환 조건의 종료 행을 추가했다. | 117–128 |
| [src/SwanInterpolateOutput.ftn90.md](../swash/src/SwanInterpolateOutput.ftn90.md):132–163 (보완) | 꼭짓점 매핑·일치점 출력·발견 표시 초기화를 요약했다. | ivert·foutp·cellfound 대입문과 cycle 명령을 인용했다. | 136·154–160 |
| [src/SwanInterpolateOutput.ftn90.md](../swash/src/SwanInterpolateOutput.ftn90.md):164–204 (보완) | 바깥 반복을 이름만 적었다. 셀·꼭짓점·각도 매핑과 eps·cellfound 값을 요약했다. | 바깥 DO와 종료 행을 추가했다. 매핑 대입문과 eps = 0. 및 cellfound 설정을 인용했다. | 132·168–204·249 |
| [src/SwanInterpolateOutput.ftn90.md](../swash/src/SwanInterpolateOutput.ftn90.md):205–223 (보완) | 바깥 반복을 이름만 적었다. 경고의 좌표식과 꼭짓점 좌표 저장식을 요약했다. | 바깥 DO와 종료 행을 추가했다. 좌표식이 포함된 경고 작성문과 좌표 저장 대입문을 인용했다. | 132·209–223·249 |
| [src/SwanInterpolateOutput.ftn90.md](../swash/src/SwanInterpolateOutput.ftn90.md):224–242 (보완) | 바깥 활성 조건을 이름만 적었다. ivc(1) 설정을 코드로 인용하지 않았다. | 바깥 DO·IF와 닫힘 행을 추가했다. ivc(1) = k를 인용했다. | 132·216·237·247–249 |
| [src/SwanInterpolateOutput.ftn90.md](../swash/src/SwanInterpolateOutput.ftn90.md):243–251 (보완) | 바깥 활성 조건을 이름만 적었다. | 바깥 DO·IF와 닫힘 행을 명시했다. | 132·216·247–249 |
| [src/SwanInterpolatePoint.ftn90.md](../swash/src/SwanInterpolatePoint.ftn90.md):64–106 (정정) | 지역 변수 eps를 예외값으로 설명했다. | eps를 원문 주석에 따라 작은 수로 고쳤다. | 76 |
| [src/SwanInterpolatePoint.ftn90.md](../swash/src/SwanInterpolatePoint.ftn90.md):64–106 (보완) | ient 초기값을 코드로 인용하지 않았다. | ient = 0을 인용했다. | 67 |
| [src/SwanInterpolatePoint.ftn90.md](../swash/src/SwanInterpolatePoint.ftn90.md):107–149 (보완) | 출력 예외값·일치점 출력·셀 발견 표시와 경고 좌표식을 요약했다. | foutp·cellfound 설정과 오프셋 좌표가 포함된 경고 원문을 인용했다. | 116–148 |
| [src/SwanInterpolatePoint.ftn90.md](../swash/src/SwanInterpolatePoint.ftn90.md):150–192 (보완) | 셀·꼭짓점·각도 매핑과 eps·cellfound 설정을 요약했다. | 매핑 대입문과 eps·cellfound 설정을 인용했다. 반복의 종료 위치를 추가했다. | 156–192 |
| [src/SwanInterpolatePoint.ftn90.md](../swash/src/SwanInterpolatePoint.ftn90.md):193–220 (보완) | 미발견 경고의 좌표식과 스칼라·도심·면적 저장식을 요약했다. | 경고 작성문 및 phi1·phi2·phi3·도심·면적 대입문을 인용했다. | 197–216 |
| [src/SwanInterpolatePoint.ftn90.md](../swash/src/SwanInterpolatePoint.ftn90.md):221–248 (보완) | 바깥 세 스칼라 조건을 이름만 적었다. 일정 기울기를 쓴다는 주석을 생략했다. | 바깥 조건식과 ENDIF 위치를 명시했다. 일정 기울기를 사용하는 보간 주석을 추가했다. | 210·221–246 |
| [src/SwanPointinMesh.ftn90.md](../swash/src/SwanPointinMesh.ftn90.md):61–93 (보완) | ient와 numcrs 초기값을 코드로 인용하지 않았다. | 두 초기화 대입문을 인용했다. | 63·90 |
| [src/SwanPointinMesh.ftn90.md](../swash/src/SwanPointinMesh.ftn90.md):94–117 (보완) | 경계 면·꼭짓점·좌표 인덱스 매핑을 요약했다. | iface·v1·v2 및 좌표 매핑 대입문을 인용했다. | 96–104 |
| [src/SwanPointinMesh.ftn90.md](../swash/src/SwanPointinMesh.ftn90.md):118–127 (보완) | 함수 반환 논리값을 설명만 했다. | 참·거짓 반환 대입문을 인용했다. | 122–124 |

대상 기록의 frontmatter를 유지했다.
대상 기록의 구간 경계를 유지했다.
원문 22개의 SHA-256은 각 기록의 frontmatter와 일치했다.
지정 기록과 이 보고서만 수정했다.
원문·노트·git은 수정하지 않았다.
모델은 실행하지 않았다.
실행 결과와 수치·물리적 타당성은 검증하지 않았다.

정정 4, 보완 77, 이상 없음 83
