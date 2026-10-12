# SWAN code-7 전수 대조 기록

2026-10-13에 지정된 10개 기록을 각 frontmatter의 `file:` 원문과 대조했다.
구간 표의 내용 행 102개를 대조했다.
하단 코드 사실 행 53개를 대조했다.
원문 대조 범위는 아래 표의 3,646행이다.
각 구간의 원문은 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
한 번에 연 원문은 200행 이하이다.

다음 표의 대조 행 수는 구간 행 수와 코드 사실 행 수의 합이다.
정정 수와 보완 수는 각 표식이 붙은 기록 행 수이다.
두 표식이 함께 붙은 3행은 정정과 보완에 각각 집계했다.
이상 없음은 두 표식이 모두 없는 대조 행 수이다.

| 기록 | 구간 행 | 코드 사실 행 | 대조 행 합계 | 원문 범위 | 정정 | 보완 | 두 표식 | 이상 없음 |
|---|---:|---:|---:|---|---:|---:|---:|---:|
| [SwanReadTriangleGrid.ftn90.md](../swan/src/SwanReadTriangleGrid.ftn90.md) | 6 | 6 | 12 | 1–178 | 0 | 3 | 0 | 9 |
| [SwanSpectPart.ftn.md](../swan/src/SwanSpectPart.ftn.md) | 29 | 11 | 40 | 1–1477 | 3 | 22 | 1 | 16 |
| [SwanSweepSel.ftn90.md](../swan/src/SwanSweepSel.ftn90.md) | 9 | 6 | 15 | 1–375 | 0 | 8 | 0 | 7 |
| [SwanTranspAc.ftn90.md](../swan/src/SwanTranspAc.ftn90.md) | 7 | 2 | 9 | 1–178 | 0 | 5 | 0 | 4 |
| [SwanTranspX.ftn90.md](../swan/src/SwanTranspX.ftn90.md) | 6 | 3 | 9 | 1–161 | 0 | 4 | 0 | 5 |
| [SwanVTKPDataSets.ftn90.md](../swan/src/SwanVTKPDataSets.ftn90.md) | 9 | 7 | 16 | 1–308 | 0 | 7 | 0 | 9 |
| [SwanVTKWriteData.ftn90.md](../swan/src/SwanVTKWriteData.ftn90.md) | 9 | 4 | 13 | 1–207 | 1 | 3 | 1 | 10 |
| [SwanVTKWriteHeader.ftn90.md](../swan/src/SwanVTKWriteHeader.ftn90.md) | 10 | 4 | 14 | 1–292 | 0 | 5 | 0 | 9 |
| [SwanVertlist.ftn90.md](../swan/src/SwanVertlist.ftn90.md) | 12 | 7 | 19 | 1–418 | 2 | 4 | 0 | 13 |
| [m_constants.ftn90.md](../swan/src/m_constants.ftn90.md) | 5 | 3 | 8 | 1–52 | 1 | 1 | 1 | 7 |
| 합계 | 102 | 53 | 155 | 3,646행 | 7 | 62 | 3 | 89 |

조건과 대입식의 백틱 인용을 원문과 대조했다.
주석 속 수식도 대조했다.
분기 의미와 블록 종료 행을 대조했다.
오류 메시지 뒤의 이동 또는 반환을 대조했다.
대상 원문의 행 첫머리 전처리 표식은 `!TIMG`, `!GRAPH`, `!FXFRO`였다.
`swan/switch.pl` 82–105행의 표식 제거 규칙을 확인했다.
`swan/switch.pl` 22·24행의 `-timg`와 `-fixfront` 옵션 대응도 확인했다.
대상 기록의 전처리 스위치 설명은 원문 규칙과 일치했다.

원문 해시는 대조 시작 상태와 같다.
기록의 frontmatter는 대조 시작 상태와 같다.
기록의 구간 경계는 대조 시작 상태와 같다.
모델은 실행하지 않았다.

다음 목록의 원문 행은 해당 기록의 `file:`에 지정된 파일을 기준으로 한다.
새 요지의 괄호는 해당 행에 붙인 표식 종류이다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [SwanReadTriangleGrid.ftn90.md:83–115](../swan/src/SwanReadTriangleGrid.ftn90.md) | 할당 실패 처리를 포괄적으로 적고 입력 오류 이동을 생략했다. | (보완) 할당 실패의 goto 900과 read의 end=950·err=910을 적었다. | 95–107 |
| [SwanReadTriangleGrid.ftn90.md:116–133](../swan/src/SwanReadTriangleGrid.ftn90.md) | 정점 입력의 오류 이동을 생략했다. | (보완) 두 입력문의 파일 끝·판독 오류 이동 위치를 적었다. | 120·125 |
| [SwanReadTriangleGrid.ftn90.md:134–168](../swan/src/SwanReadTriangleGrid.ftn90.md) | kvertc 할당 실패 처리를 포괄적으로 적고 입력 오류 이동을 생략했다. | (보완) 할당 실패의 goto 900과 세 read의 end=950·err=910을 적었다. | 144–160 |
| [SwanSpectPart.ftn.md:64–123](../swan/src/SwanSpectPart.ftn.md) | OUTPUT 명령으로 현재 값을 설정할 수 있다는 뜻으로 옮겼다. | (정정) 주석의 can be made를 사용자 설정 가능하게 바꿀 수 있다는 뜻으로 옮겼다. | 94–97 |
| [SwanSpectPart.ftn.md:225–351](../swan/src/SwanSpectPart.ftn.md) | NP=-1·0의 뜻을 풀어 적지 않았고 풍향 좌표 관례를 생략했다. | (보완) NP 두 값의 주석 의미와 UDIR의 Cartesian 관례를 적었다. | 292·297–303 |
| [SwanSpectPart.ftn.md:352–400](../swan/src/SwanSpectPart.ftn.md) | IENT·NP·XP 초기값을 백틱으로 인용하지 않았다. | (보완) SAVE·DATA와 NP·XP 초기화 원문을 인용했다. | 356–361 |
| [SwanSpectPart.ftn.md:401–420](../swan/src/SwanSpectPart.ftn.md) | 초기값·선택 인덱스·선택 비율 대입을 요약만 했다. | (보완) 복사·초기화·선택 인덱스·비율 -1 대입을 인용했다. | 408–418 |
| [SwanSpectPart.ftn.md:421–449](../swan/src/SwanSpectPart.ftn.md) | 결합 번호·재정렬 초기값·선택 결과의 대입과 ELSE 부재를 생략했다. | (보완) PMAP·INDEX 대응식과 재정렬 대입을 인용하고 ELSE 부재를 적었다. | 423–449 |
| [SwanSpectPart.ftn.md:450–479](../swan/src/SwanSpectPart.ftn.md) | 복사·초기화·선택 파고 대입과 주석 속 IF 원문을 생략했다. | (보완) 해당 대입과 주석 처리된 해제 조건을 인용했다. | 455–470 |
| [SwanSpectPart.ftn.md:583–616](../swan/src/SwanSpectPart.ftn.md) | 초기값과 점별 순서·정렬 인덱스 대입을 요약만 했다. | (보완) 초기값과 인덱스 대응 대입을 원문으로 인용했다. | 583·591·600–610 |
| [SwanSpectPart.ftn.md:617–736](../swan/src/SwanSpectPart.ftn.md) | MK>0 조건과 뒤의 할당 범위를 구분하지 않았고 초기 대입 인용을 생략했다. | (정정·보완) 해제에만 MK>0이 적용됨을 적고 저장 크기·초기값을 인용했다. | 718·723–733 |
| [SwanSpectPart.ftn.md:737–783](../swan/src/SwanSpectPart.ftn.md) | 이웃 수 초기값을 백틱으로 인용하지 않았다. | (보완) K=0 원문을 인용했다. | 741 |
| [SwanSpectPart.ftn.md:826–848](../swan/src/SwanSpectPart.ftn.md) | 이웃 수 저장 대입을 요약만 했다. | (보완) NEIGH의 9번째 행에 저장하는 대입을 인용했다. | 841 |
| [SwanSpectPart.ftn.md:849–978](../swan/src/SwanSpectPart.ftn.md) | 라벨·거리·큐·탐색·추적 초기값을 요약만 했다. | (보완) 초기값 대입과 DATA를 원문으로 인용했다. | 956·961–977 |
| [SwanSpectPart.ftn.md:979–1013](../swan/src/SwanSpectPart.ftn.md) | 탐색 상태·거리 대입과 바깥 IH 루프의 종료 행을 생략했다. | (보완) 대입 원문과 IH 루프의 1113행 종료를 적었다. | 979–998·1113 |
| [SwanSpectPart.ftn.md:1014–1068](../swan/src/SwanSpectPart.ftn.md) | 거리·라벨 대입과 세 IF 사슬의 ELSE 부재를 생략했다. | (보완) 대입 원문과 ELSE 부재를 적고 EXIT의 대상 루프를 밝혔다. | 1014–1067·1113 |
| [SwanSpectPart.ftn.md:1069–1114](../swan/src/SwanSpectPart.ftn.md) | 탐색 복원·거리 초기값·라벨 저장 대입을 요약만 했다. | (보완) 누락된 대입 원문을 인용했다. | 1071–1097 |
| [SwanSpectPart.ftn.md:1115–1143](../swan/src/SwanSpectPart.ftn.md) | 초기값·선택 갱신·반환 대입과 동률 처리 의미를 생략했다. | (보완) 대입 원문과 같음 조건에 따른 뒤 이웃 선택을 적었다. | 1121–1140 |
| [SwanSpectPart.ftn.md:1144–1159](../swan/src/SwanSpectPart.ftn.md) | 큐 저장 대입을 요약만 했다. | (보완) 큐 저장 대입 원문을 인용했다. | 1152 |
| [SwanSpectPart.ftn.md:1160–1174](../swan/src/SwanSpectPart.ftn.md) | 빈 큐 판별값을 백틱으로 인용하지 않았다. | (보완) 두 분기의 IEMPTY 대입을 인용했다. | 1166–1170 |
| [SwanSpectPart.ftn.md:1175–1191](../swan/src/SwanSpectPart.ftn.md) | 큐 앞 값 대입을 백틱으로 인용하지 않았다. | (보완) 큐 앞 값 대입 원문을 인용했다. | 1181 |
| [SwanSpectPart.ftn.md:1316–1363](../swan/src/SwanSpectPart.ftn.md) | 초기값·IS=0 원문과 경계 보간의 바깥 ELSE 범위를 생략했다. | (보완) 초기값을 인용하고 IF·방향 루프의 종료를 밝혔다. | 1317–1341·1351–1362 |
| [SwanSpectPart.ftn.md:1364–1390](../swan/src/SwanSpectPart.ftn.md) | 분할 번호 대입과 주석 속 고주파 꼬리 식을 인용하지 않았다. | (보완) 분할 번호 대입과 비활성 꼬리 식을 인용했다. | 1372·1389 |
| [SwanSpectPart.ftn.md:1391–1418](../swan/src/SwanSpectPart.ftn.md) | 주석 처리된 네 적분식과 피크 갱신 대입을 생략했다. | (보완) 비활성 적분식과 피크 갱신 대입을 원문으로 인용했다. | 1394–1397·1409–1411 |
| [SwanSpectPart.ftn.md:1419–1457](../swan/src/SwanSpectPart.ftn.md) | NPO 초기값·파고 대입·주석 파장식·ELSE 기본값의 인용이 빠졌다. | (보완) 해당 대입과 비활성 파장식을 인용했다. | 1419·1439–1454 |
| [SwanSpectPart.ftn.md:1458–1477](../swan/src/SwanSpectPart.ftn.md) | 오류 출력의 NPO+1 계산을 요약만 했다. | (보완) WRITE의 NPO+1 계산을 인용했다. | 1464·1469–1470 |
| [SwanSpectPart.ftn.md:코드 사실 90–97](../swan/src/SwanSpectPart.ftn.md) | OUTPUT 명령으로 현재 사용자 설정이 가능하다고 적었다. | (정정) 사용자 설정 가능하게 바꿀 수 있다는 주석의 의미로 고쳤다. | 94–97 |
| [SwanSweepSel.ftn90.md:75–128](../swan/src/SwanSweepSel.ftn90.md) | ient 초기값을 백틱으로 인용하지 않았다. 기저 성분의 주석 식을 생략했다. | (보완) ient 선언 초기값을 인용했다. rdx·rdy 성분의 주석 식을 인용했다. | 112·99–100 |
| [SwanSweepSel.ftn90.md:129–149](../swan/src/SwanSweepSel.ftn90.md) | 범위·개수·배열 초기값을 요약만 했다. | (보완) 모든 초기 대입을 인용했다. | 133–146 |
| [SwanSweepSel.ftn90.md:150–193](../swan/src/SwanSweepSel.ftn90.md) | 개수 초기값·활성 표식·첫 주파수 복사 대입을 인용하지 않았다. | (보완) 대입 원문과 IF·바깥 주파수 루프의 종료 행을 적었다. | 150–190·262 |
| [SwanSweepSel.ftn90.md:194–238](../swan/src/SwanSweepSel.ftn90.md) | 경계 인덱스·논리 표식 초기값과 비주기 경계 표식 대입을 요약만 했다. | (보완) 누락된 대입을 인용했다. | 194–223 |
| [SwanSweepSel.ftn90.md:239–263](../swan/src/SwanSweepSel.ftn90.md) | 기본·빈 방향 범위 대입과 ELSE 부재를 생략했다. | (보완) 대입 원문과 전체 활성일 때 기본 범위 유지 경로를 적었다. | 241–255 |
| [SwanSweepSel.ftn90.md:264–300](../swan/src/SwanSweepSel.ftn90.md) | 방향 수 기본값·범위 제한 대입과 오류 메시지의 뜻을 생략했다. | (보완) 대입 원문과 최소·최대 방향 빈 누락 메시지를 적었다. | 266–299 |
| [SwanSweepSel.ftn90.md:301–336](../swan/src/SwanSweepSel.ftn90.md) | 주석 속 IF와 기본값 대입의 인용 및 오류 메시지 뜻을 생략했다. | (보완) 비활성 IF·기본값과 최소·최대 주파수 빈 누락 메시지를 적었다. | 303–335 |
| [SwanSweepSel.ftn90.md:337–375](../swan/src/SwanSweepSel.ftn90.md) | 활성 주파수 탐색·출력의 대입과 오류 메시지 뜻을 생략했다. | (보완) 표식·인덱스 대입과 주파수 인덱스 오류 메시지를 적었다. | 342–369 |
| [SwanTranspAc.ftn90.md:50–79](../swan/src/SwanTranspAc.ftn90.md) | 주파수·방향 인접 계수의 감소·증가 순서를 생략했다. | (보완) 행렬의 다섯 위치를 원문 인덱스로 대응시켰다. | 75–79 |
| [SwanTranspAc.ftn90.md:80–112](../swan/src/SwanTranspAc.ftn90.md) | 방향 단위·기저 성분 식·ient 초기값 인용을 생략했다. | (보완) 라디안 단위와 기저 성분 식 및 선언 초기값을 적었다. | 87–90·105 |
| [SwanTranspAc.ftn90.md:113–137](../swan/src/SwanTranspAc.ftn90.md) | 다섯 배열의 초기값을 백틱으로 인용하지 않았다. | (보완) 각 배열 초기화 원문을 인용했다. | 117–124 |
| [SwanTranspAc.ftn90.md:138–150](../swan/src/SwanTranspAc.ftn90.md) | STRSD 인수에서 주파수별 방향 범위를 생략했다. | (보완) idcmin·idcmax 전달을 적었다. | 143–146 |
| [SwanTranspAc.ftn90.md:165–178](../swan/src/SwanTranspAc.ftn90.md) | 구간 설명에 방식 선택 사슬의 ELSE 부재를 적지 않았다. | (보완) int(PNUMS(8))=1·2 외의 ELSE가 없음을 적었다. | 156–175 |
| [SwanTranspX.ftn90.md:45–80](../swan/src/SwanTranspX.ftn90.md) | 행렬 인접점의 부호·순서와 기저 성분 식을 생략했다. | (보완) 다섯 계수의 위치 및 기저 성분 식을 적었다. | 67–76 |
| [SwanTranspX.ftn90.md:81–108](../swan/src/SwanTranspX.ftn90.md) | 선언 초기값과 스텐실 인덱스 대입을 요약만 했다. | (보완) ient 초기값과 세 인덱스 대입을 인용했다. | 85·105–107 |
| [SwanTranspX.ftn90.md:109–120](../swan/src/SwanTranspX.ftn90.md) | 평면 좌표 계수 기본값을 백틱으로 인용하지 않았다. | (보완) fac1·fac2 기본값 대입을 인용했다. | 111–112 |
| [SwanTranspX.ftn90.md:141–161](../swan/src/SwanTranspX.ftn90.md) | acold 분기별 대입을 요약만 했다. | (보완) 두 분기의 배열·인덱스를 원문으로 인용했다. | 143–147 |
| [SwanVTKPDataSets.ftn90.md:46–100](../swan/src/SwanVTKPDataSets.ftn90.md) | ient 초기값을 백틱으로 인용하지 않았다. | (보완) 선언 초기값 원문을 인용했다. | 74 |
| [SwanVTKPDataSets.ftn90.md:101–134](../swan/src/SwanVTKPDataSets.ftn90.md) | 격자 종류 선택 사슬의 ELSE 부재를 구간 행에 적지 않았다. | (보완) ELSE 부재와 그 밖의 pstype 경로를 적었다. | 111–133 |
| [SwanVTKPDataSets.ftn90.md:135–184](../swan/src/SwanVTKPDataSets.ftn90.md) | 변수 종류·이름 대입을 요약만 했다. | (보완) 대응 배열 인덱스와 대입 원문을 인용했다. | 144·148·155 |
| [SwanVTKPDataSets.ftn90.md:185–210](../swan/src/SwanVTKPDataSets.ftn90.md) | 대소문자 초기값·파일명 복사와 오류 메시지의 부분영역 번호 대응을 생략했다. | (보완) 대입 원문 및 메시지의 iproc·iproc+1과 배열의 iproc-1·iproc 대응을 적었다. | 185–205·231·298 |
| [SwanVTKPDataSets.ftn90.md:211–232](../swan/src/SwanVTKPDataSets.ftn90.md) | 두 번째 분할 검사 메시지의 내용·번호 대응을 생략했다. | (보완) 부분영역 번호 불일치와 격자 이름 보고를 적었다. | 216–229 |
| [SwanVTKPDataSets.ftn90.md:254–273](../swan/src/SwanVTKPDataSets.ftn90.md) | 프로세서 번호의 부분 문자열 인덱스와 접두사 기본값을 요약만 했다. | (보완) 번호 덮어쓰기와 p/P/점 접두사 생성 원문을 인용했다. | 254–264 |
| [SwanVTKPDataSets.ftn90.md:274–308](../swan/src/SwanVTKPDataSets.ftn90.md) | 비구조 경로의 파일명 번호 인덱스와 접두사 기본값을 요약만 했다. | (보완) 번호 덮어쓰기와 접두사 생성 원문을 인용했다. | 278–288 |
| [SwanVTKWriteData.ftn90.md:83–119](../swan/src/SwanVTKWriteData.ftn90.md) | ient·ios 초기값과 프로세서 번호 대입을 요약만 했다. | (보완) 초기값·포인터 연결·프로세서 번호 대입을 인용했다. | 86·112–116 |
| [SwanVTKWriteData.ftn90.md:120–135](../swan/src/SwanVTKWriteData.ftn90.md) | 변수 종류의 배열 인덱스 대입을 요약만 했다. | (보완) ivtyp(jvar) 대입 원문을 인용했다. | 122 |
| [SwanVTKWriteData.ftn90.md:코드 사실 126–146·155–162](../swan/src/SwanVTKWriteData.ftn90.md) | 실제 출력 개수가 프로세서 소속 조건만으로 결정된다고 적었다. | (정정·보완) ios=0과 소속 조건이 모두 필요함을 적고 조건식을 인용했다. | 116·132·144·160 |
| [SwanVTKWriteHeader.ftn90.md:46–102](../swan/src/SwanVTKWriteHeader.ftn90.md) | ient 초기값을 백틱으로 인용하지 않았다. | (보완) 선언 초기값 원문을 인용했다. | 79 |
| [SwanVTKWriteHeader.ftn90.md:103–114](../swan/src/SwanVTKWriteHeader.ftn90.md) | 출력 상태 초기값을 백틱으로 인용하지 않았다. | (보완) ios 초기화 대입을 인용했다. | 105 |
| [SwanVTKWriteHeader.ftn90.md:137–164](../swan/src/SwanVTKWriteHeader.ftn90.md) | ioff 초기값·원점 의미와 종류 선택 사슬의 ELSE 부재를 생략했다. | (보완) ioff 원문·밑줄 다음 원점과 IF 종료 이후 범위를 적었다. | 115–163 |
| [SwanVTKWriteHeader.ftn90.md:165–198](../swan/src/SwanVTKWriteHeader.ftn90.md) | 변수 종류·이름의 배열 인덱스 대입을 요약만 했다. | (보완) 변수 종류·이름 대입 원문을 인용했다. | 169·173·185 |
| [SwanVTKWriteHeader.ftn90.md:199–223](../swan/src/SwanVTKWriteHeader.ftn90.md) | 좌표의 세 번째 성분에 관한 주석을 생략했다. | (보완) z=0의 주석 내용을 적었다. | 208 |
| [SwanVertlist.ftn90.md:59–123](../swan/src/SwanVertlist.ftn90.md) | 공통 추적 변수 초기값을 백틱으로 인용하지 않았다. | (보완) ient 선언 초기값을 인용했다. | 84 |
| [SwanVertlist.ftn90.md:124–150](../swan/src/SwanVertlist.ftn90.md) | 할당 상태 초기값과 포인터 연결 원문 및 오류 메시지 내용을 생략했다. | (보완) 초기값·포인터 연결을 인용하고 vlist 할당 문제 보고를 적었다. | 135–144 |
| [SwanVertlist.ftn90.md:151–179](../swan/src/SwanVertlist.ftn90.md) | 평균 계산 초기값·풍속 배열 인덱스·기본 방향 대입과 IF 종료 행을 생략했다. | (보완) 대입 원문과 175·176행 종료를 적었다. | 151–178 |
| [SwanVertlist.ftn90.md:180–218](../swan/src/SwanVertlist.ftn90.md) | 초기 정점 순서와 선택 정렬의 교환 대입을 요약만 했다. | (보완) 초기 순서와 거리·정점 번호의 교환 대입을 인용했다. | 194–211 |
| [SwanVertlist.ftn90.md:219–246](../swan/src/SwanVertlist.ftn90.md) | pos 채우기와 level 초기화를 모두 235행 j 루프 안의 작업처럼 적었다. | (정정) j 루프의 241행 종료와 그 밖의 246행 level 초기화를 구분했다. | 229–246·313 |
| [SwanVertlist.ftn90.md:380–408](../swan/src/SwanVertlist.ftn90.md) | nvf를 각 전면의 실제 정점 수로 적고 전면 수 계산을 포괄적으로 설명했다. | (정정) 전면 수의 하한·상한 순서와 nvf의 분할 폭 역할 및 끝 인덱스 제한을 구분했다. | 387–406 |
| [m_constants.ftn90.md:16–27](../swan/src/m_constants.ftn90.md) | exp 함수의 하한·상한이라고 적고 주석의 방지 목적과 근삿값을 생략했다. | (정정·보완) 함수 인수의 하한·상한으로 고치고 언더플로·오버플로 및 약 1.41을 적었다. | 18–23 |

정정 7, 보완 62, 이상 없음 89
