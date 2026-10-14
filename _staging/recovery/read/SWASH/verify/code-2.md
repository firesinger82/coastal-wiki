SWASH 판독 기록 전수 대조 결과. 대조일은 2026-10-15이다.

아래 집계표의 12개 기록을 대조했다.
대조한 구간표 행은 91행이다.
대조한 원문은 3,367행이다.
행 수는 각 기록의 구간표와 frontmatter의 `file:`이 가리키는 원문에서 셌다.
각 구간의 원문은 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
원문을 여는 각 명령의 구간은 200행 이하로 제한했다.

집계 단위는 구간표 한 행이다.
정정과 보완이 함께 있는 행은 정정에만 집계했다.

| 기록 | 대조한 구간표 행 수 | 대조한 원문 행 수 | 정정 | 보완 | 이상 없음 |
|---|---:|---:|---:|---:|---:|
| [SwanReadADCGrid.ftn90.md](../swash/src/SwanReadADCGrid.ftn90.md) | 7 | 187 | 1 | 4 | 2 |
| [SwanReadEasymeshGrid.ftn90.md](../swash/src/SwanReadEasymeshGrid.ftn90.md) | 5 | 155 | 0 | 3 | 2 |
| [SwanReadGrid.ftn90.md](../swash/src/SwanReadGrid.ftn90.md) | 3 | 95 | 0 | 1 | 2 |
| [SwanReadTriangleGrid.ftn90.md](../swash/src/SwanReadTriangleGrid.ftn90.md) | 6 | 178 | 0 | 3 | 3 |
| [Swash.ftn90.md](../swash/src/Swash.ftn90.md) | 3 | 71 | 0 | 0 | 3 |
| [SwashAmbCurrent.ftn90.md](../swash/src/SwashAmbCurrent.ftn90.md) | 15 | 668 | 0 | 14 | 1 |
| [SwashAntiCreep1DH.ftn90.md](../swash/src/SwashAntiCreep1DH.ftn90.md) | 9 | 303 | 0 | 9 | 0 |
| [SwashAntiCreep2DH.ftn90.md](../swash/src/SwashAntiCreep2DH.ftn90.md) | 11 | 466 | 0 | 10 | 1 |
| [SwashAverOutp.ftn90.md](../swash/src/SwashAverOutp.ftn90.md) | 6 | 195 | 0 | 2 | 4 |
| [SwashBCStokeswave.ftn90.md](../swash/src/SwashBCStokeswave.ftn90.md) | 11 | 435 | 2 | 7 | 2 |
| [SwashBCboundwave.ftn90.md](../swash/src/SwashBCboundwave.ftn90.md) | 8 | 361 | 1 | 5 | 2 |
| [SwashBCshortwave.ftn90.md](../swash/src/SwashBCshortwave.ftn90.md) | 7 | 253 | 0 | 4 | 3 |
| 합계 | 91 | 3,367 | 4 | 62 | 25 |

전처리 규칙은 `models/SWASH/raw/source_code/swash/switch.pl`의 57–66행과 대조했다.
이 규칙은 해당 스위치 변수가 `TRUE`에 일치할 때 행 첫머리의 표시를 제거한다.
대상 원문 12개에는 이 규칙이 처리하는 표시 행이 없었다.

층 인덱스 설명은 각 대상 파일의 원문 주석과 대조했다.
`SwashAntiCreep1DH` 83–84행과 `SwashAntiCreep2DH` 79–80행은 kd와 ku를 각각 k-1과 k+1로 정의한다.
해당 주석은 위층·아래층 방향을 명시하지 않는다.
기록은 이 인덱스 표기를 유지했다.

원문 12개의 SHA-256은 작업 시작 시 값과 같았다.
기록 12개의 frontmatter와 구간 경계는 바뀌지 않았다.
수정본의 조건식·대입식 인용 점검에서는 추가 누락이 없었다.
모델은 실행하지 않았다.
원문·노트·git은 변경하지 않았다.

아래 목록은 구간별 정정·보완 내용이다.
원문 행은 해당 기록의 `file:`이 가리키는 파일의 행 번호이다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [SwanReadADCGrid.ftn90.md](../swash/src/SwanReadADCGrid.ftn90.md):60–86 | ient 초기값을 평문으로만 표기했다. | 보완. ient의 선언·초기값을 원문 그대로 인용했다. | 63 |
| [SwanReadADCGrid.ftn90.md](../swash/src/SwanReadADCGrid.ftn90.md):87–115 | 파일 열기·할당 초기값을 평문으로만 표기했다. | 보완. ndsd·iostat·grdfil·istat 초기값을 인용했다. 독립적인 할당 조건의 닫힘 행을 명시했다. | 91–115 |
| [SwanReadADCGrid.ftn90.md](../swash/src/SwanReadADCGrid.ftn90.md):116–142 | vmark 초기값을 평문으로만 표기했다. | 보완. vmark 초기값을 원문 그대로 인용했다. | 142 |
| [SwanReadADCGrid.ftn90.md](../swash/src/SwanReadADCGrid.ftn90.md):143–155 | idum을 총점 수로 단정했다. 경계 마커 대입식을 평문으로만 표기했다. | 정정·보완. 원문에서 뜻을 설명하지 않은 idum의 용도 단정을 삭제했다. vm·vmark 대입식을 인용했다. | 146–155 |
| [SwanReadADCGrid.ftn90.md](../swash/src/SwanReadADCGrid.ftn90.md):156–175 | 경계 마커 저장을 말로만 요약했다. | 보완. 한 꼭짓점 분기와 두 꼭짓점 분기의 마커 대입식을 인용했다. | 162–174 |
| [SwanReadEasymeshGrid.ftn90.md](../swash/src/SwanReadEasymeshGrid.ftn90.md):59–85 | ient·ndsd·iostat 초기값을 평문으로만 표기했다. | 보완. 선언과 초기값 대입식을 원문 그대로 인용했다. | 62·81–82 |
| [SwanReadEasymeshGrid.ftn90.md](../swash/src/SwanReadEasymeshGrid.ftn90.md):86–111 | istat 초기값을 평문으로만 표기했다. | 보완. istat 초기값 대입식을 원문 그대로 인용했다. | 89 |
| [SwanReadEasymeshGrid.ftn90.md](../swash/src/SwanReadEasymeshGrid.ftn90.md):112–138 | ndsd·iostat 초기값을 평문으로만 표기했다. | 보완. 파일 열기 전 초기값 대입식을 원문 그대로 인용했다. | 115–116 |
| [SwanReadGrid.ftn90.md](../swash/src/SwanReadGrid.ftn90.md):58–69 | ient 선언 초기값을 평문으로만 표기했다. | 보완. ient 선언 초기값을 원문 그대로 인용했다. | 60 |
| [SwanReadTriangleGrid.ftn90.md](../swash/src/SwanReadTriangleGrid.ftn90.md):59–92 | ient·ndsd·iostat 초기값을 평문으로만 표기했다. | 보완. 선언과 초기값 대입식을 원문 그대로 인용했다. | 62·88–89 |
| [SwanReadTriangleGrid.ftn90.md](../swash/src/SwanReadTriangleGrid.ftn90.md):93–115 | istat 초기값을 평문으로만 표기했다. | 보완. istat 초기값 대입식을 원문 그대로 인용했다. | 96 |
| [SwanReadTriangleGrid.ftn90.md](../swash/src/SwanReadTriangleGrid.ftn90.md):134–150 | ndsd·iostat 초기값을 평문으로만 표기했다. | 보완. 파일 열기 전 초기값 대입식을 원문 그대로 인용했다. | 137–138 |
| [SwashAmbCurrent.ftn90.md](../swash/src/SwashAmbCurrent.ftn90.md):51–78 | ient 초기값을 평문으로만 표기했다. | 보완. ient 선언 초기값을 원문 그대로 인용했다. | 54 |
| [SwashAmbCurrent.ftn90.md](../swash/src/SwashAmbCurrent.ftn90.md):79–122 | 격자 주소·경계 복사·상수 배경류 대입식을 요약했다. | 보완. 주소와 값의 대입식을 모두 인용했다. varva 조건의 닫힘 행을 명시했다. | 89–116 |
| [SwashAmbCurrent.ftn90.md](../swash/src/SwashAmbCurrent.ftn90.md):123–175 | 바깥 조건을 이름으로만 표시했다. 주소·경계 복사식을 요약했다. | 보완. 바깥 조건식과 닫힘 행을 명시했다. 주소·경계 복사식을 인용했다. | 81·85·123–175·512·666 |
| [SwashAmbCurrent.ftn90.md](../swash/src/SwashAmbCurrent.ftn90.md):176–244 | 바깥 조건을 이름으로만 표시했다. 주소·경계 복사식을 요약했다. | 보완. 바깥 조건식과 닫힘 행을 명시했다. 주소·경계 복사식을 인용했다. | 81·85·123·127·176–244·309·512·666 |
| [SwashAmbCurrent.ftn90.md](../swash/src/SwashAmbCurrent.ftn90.md):245–310 | 바깥 조건을 이름으로만 표시했다. 주소·경계 복사식을 요약했다. | 보완. 바깥 조건식과 닫힘 행을 명시했다. 주소·경계 복사식을 인용했다. | 81·85·123·127·245–310·512·666 |
| [SwashAmbCurrent.ftn90.md](../swash/src/SwashAmbCurrent.ftn90.md):311–361 | 바깥 조건을 이름으로만 표시했다. 주소·경계 복사식을 요약했다. | 보완. 바깥 조건식과 닫힘 행을 명시했다. 주소·경계 복사식을 인용했다. | 81·85·123·311–361·512·666 |
| [SwashAmbCurrent.ftn90.md](../swash/src/SwashAmbCurrent.ftn90.md):362–400 | 바깥 조건을 이름으로만 표시했다. 주소식을 요약했다. | 보완. 바깥 조건식과 닫힘 행을 명시했다. 주소식을 인용했다. | 81·85·123·313·362–409·493·512·666 |
| [SwashAmbCurrent.ftn90.md](../swash/src/SwashAmbCurrent.ftn90.md):401–428 | 바깥 조건·루프를 이름으로만 표시했다. 주소·경계 복사식을 요약했다. | 보완. 바깥 조건식·루프와 닫힘 행을 명시했다. 주소·경계 복사식을 인용했다. | 81·85·123·313·362·382·401–428·493·512·666 |
| [SwashAmbCurrent.ftn90.md](../swash/src/SwashAmbCurrent.ftn90.md):429–494 | 바깥 조건을 이름으로만 표시했다. 주소·경계 복사식을 요약했다. | 보완. 바깥 조건식과 닫힘 행을 명시했다. 주소·경계 복사식을 인용했다. | 81·85·123·313·429–494·512·666 |
| [SwashAmbCurrent.ftn90.md](../swash/src/SwashAmbCurrent.ftn90.md):495–513 | 바깥 조건과 영구 건조점의 0 대입식을 요약했다. | 보완. 바깥 조건식과 닫힘 행을 명시했다. 영구 건조점의 대입식을 인용했다. | 81·85·123·497–512·666 |
| [SwashAmbCurrent.ftn90.md](../swash/src/SwashAmbCurrent.ftn90.md):514–542 | 바깥 조건과 주소·복사·상수 대입식을 요약했다. | 보완. 바깥 조건식과 대입식을 인용했다. 마지막 else가 없는 조건 사슬과 닫힘 행을 명시했다. | 81·514–542·666 |
| [SwashAmbCurrent.ftn90.md](../swash/src/SwashAmbCurrent.ftn90.md):543–595 | 바깥 조건과 주소·속도 복사식을 요약했다. | 보완. 바깥 조건식과 닫힘 행을 명시했다. 주소·속도 복사식을 인용했다. | 81·514·518·543–595·664·666 |
| [SwashAmbCurrent.ftn90.md](../swash/src/SwashAmbCurrent.ftn90.md):596–645 | 바깥 조건과 주소·속도 복사식을 요약했다. | 보완. 바깥 조건식과 닫힘 행을 명시했다. 주소·속도 복사식을 인용했다. | 81·514·518·543·596–645·664·666 |
| [SwashAmbCurrent.ftn90.md](../swash/src/SwashAmbCurrent.ftn90.md):646–668 | 바깥 조건과 영구 건조점 대입식을 요약했다. | 보완. 바깥 조건식과 대입식을 인용했다. 조건 사슬의 마지막 else 부재와 닫힘 행을 명시했다. | 81·514·518·543·649–668 |
| [SwashAntiCreep1DH.ftn90.md](../swash/src/SwashAntiCreep1DH.ftn90.md):1–78 | 변환으로 곡률 항이 생긴다는 설명만 기록했다. | 보완. 곡률 항 생략 시 인공 수직 혼합이 생길 수 있다는 조건과 가능성을 보완했다. | 44–47 |
| [SwashAntiCreep1DH.ftn90.md](../swash/src/SwashAntiCreep1DH.ftn90.md):79–123 | ient 초기값·경계 주소·경계 플럭스 초기화를 요약했다. | 보완. 초기값·주소·플럭스 대입식을 원문 그대로 인용했다. | 81·114–122 |
| [SwashAntiCreep1DH.ftn90.md](../swash/src/SwashAntiCreep1DH.ftn90.md):124–164 | 주석의 미분식을 생략했다. 일부 기본값과 주소식을 요약했다. | 보완. 식 4.83의 주석 수식과 msta·dif2d·주소 대입식을 인용했다. | 124–155 |
| [SwashAntiCreep1DH.ftn90.md](../swash/src/SwashAntiCreep1DH.ftn90.md):165–187 | 바깥 루프와 주석의 층별 미분식을 축약했다. | 보완. 바깥 루프문과 층 인덱스를 포함한 주석 수식을 인용했다. | 134·165–186 |
| [SwashAntiCreep1DH.ftn90.md](../swash/src/SwashAntiCreep1DH.ftn90.md):188–213 | 끝점 소유권 주석과 주소 대입식을 생략했다. | 보완. ml 제외 이유를 주석에 한정해 보완했다. 주소 대입식을 인용했다. | 190·201–202 |
| [SwashAntiCreep1DH.ftn90.md](../swash/src/SwashAntiCreep1DH.ftn90.md):214–229 | 주소 복사를 요약했다. | 보완. 주소 대입식을 원문 그대로 인용했다. | 219 |
| [SwashAntiCreep1DH.ftn90.md](../swash/src/SwashAntiCreep1DH.ftn90.md):230–262 | 주소·상수 확산계수 대입식을 요약했다. | 보완. 주소·상수 확산계수 대입식을 원문 그대로 인용했다. | 235–253 |
| [SwashAntiCreep1DH.ftn90.md](../swash/src/SwashAntiCreep1DH.ftn90.md):263–282 | 바깥 루프와 주석의 미분식을 요약했다. | 보완. 바깥 루프문·닫힘 행·주석 수식을 인용했다. | 230·263–281·299–301 |
| [SwashAntiCreep1DH.ftn90.md](../swash/src/SwashAntiCreep1DH.ftn90.md):283–303 | 바깥 루프를 이름으로만 표시했다. 닫힘을 묶어서 기록했다. | 보완. 바깥 루프문과 각 블록의 닫힘 행을 명시했다. | 230·263·283–303 |
| [SwashAntiCreep2DH.ftn90.md](../swash/src/SwashAntiCreep2DH.ftn90.md):1–56 | 성층의 강도와 곡률 항 생략 시의 영향·근거 쪽수를 생략했다. | 보완. 강한 성층 조건과 인공 수직 혼합 가능성을 보완했다. 보고서 번호·쪽수를 명시했다. | 44–55 |
| [SwashAntiCreep2DH.ftn90.md](../swash/src/SwashAntiCreep2DH.ftn90.md):125–186 | 주석의 미분식과 일부 기본값·인덱스·주소·경계 초기화식을 요약했다. | 보완. 식 4.83과 모든 누락된 대입식을 원문 그대로 인용했다. | 127–181 |
| [SwashAntiCreep2DH.ftn90.md](../swash/src/SwashAntiCreep2DH.ftn90.md):187–218 | 바깥 루프와 주석의 미분식을 요약했다. | 보완. 바깥 루프문·닫힘 행·주석 수식을 인용했다. periodic 호출의 블록 위치를 명시했다. | 141·149·187–218 |
| [SwashAntiCreep2DH.ftn90.md](../swash/src/SwashAntiCreep2DH.ftn90.md):219–275 | 일부 기본값·인덱스·주소·경계 초기화식을 요약했다. | 보완. nsta·nend·dif2d·격자 간격·인덱스·주소·경계 초기화 대입식을 인용했다. | 222–270 |
| [SwashAntiCreep2DH.ftn90.md](../swash/src/SwashAntiCreep2DH.ftn90.md):276–304 | 바깥 루프와 주석의 미분식을 요약했다. | 보완. 바깥 루프문·닫힘 행·주석 수식을 인용했다. periodic 호출의 블록 위치를 명시했다. | 230·238·276–304 |
| [SwashAntiCreep2DH.ftn90.md](../swash/src/SwashAntiCreep2DH.ftn90.md):305–342 | 이웃 인덱스·주소식을 요약했다. | 보완. 이웃 인덱스·주소 대입식을 원문 그대로 인용했다. | 320–325 |
| [SwashAntiCreep2DH.ftn90.md](../swash/src/SwashAntiCreep2DH.ftn90.md):343–357 | 주소 대입식을 생략했다. | 보완. 주소 대입식을 원문 그대로 인용했다. | 349 |
| [SwashAntiCreep2DH.ftn90.md](../swash/src/SwashAntiCreep2DH.ftn90.md):358–400 | 이웃 인덱스·주소와 상수 확산계수 대입식을 요약했다. | 보완. 이웃 인덱스·주소·dif2d 대입식을 원문 그대로 인용했다. | 364–398 |
| [SwashAntiCreep2DH.ftn90.md](../swash/src/SwashAntiCreep2DH.ftn90.md):401–433 | 바깥 조건·루프와 주석의 미분식을 요약했다. | 보완. 바깥 조건식·루프문·닫힘 행과 주석 수식을 인용했다. 402행 이후의 블록 범위를 명시했다. | 361–362·386·390·401–433·461–464 |
| [SwashAntiCreep2DH.ftn90.md](../swash/src/SwashAntiCreep2DH.ftn90.md):434–466 | 바깥 루프와 닫힘 행을 묶어서 기록했다. | 보완. 바깥 루프문과 각 블록의 닫힘 행을 명시했다. | 361–362·413·445–466 |
| [SwashAverOutp.ftn90.md](../swash/src/SwashAverOutp.ftn90.md):81–116 | 비양수 수심 분기의 누적량 초기화를 요약했다. | 보완. 각 격자 분기의 setup·etavar 초기화식을 인용했다. | 98–110 |
| [SwashAverOutp.ftn90.md](../swash/src/SwashAverOutp.ftn90.md):117–148 | 바깥 파랑 출력 조건을 이름으로만 표시했다. | 보완. 바깥 조건식을 인용했다. 중첩 조건의 닫힘 행을 각각 명시했다. | 85·117–125 |
| [SwashBCStokeswave.ftn90.md](../swash/src/SwashBCStokeswave.ftn90.md):42–88 | istok=0의 유속 분포 설명에서 에어리파 이론이라는 주석을 생략했다. | 보완. istok=0에도 에어리파 이론이 명시됨을 보완했다. | 54–55 |
| [SwashBCStokeswave.ftn90.md](../swash/src/SwashBCStokeswave.ftn90.md):129–165 | 바깥 층 수 조건을 이름으로만 표시했다. | 보완. 바깥 조건식과 닫힘 행을 명시했다. 층 수 조건 사슬의 마지막 else 부재를 기록했다. | 101·129–164·433 |
| [SwashBCStokeswave.ftn90.md](../swash/src/SwashBCStokeswave.ftn90.md):166–200 | 바깥 층 수 조건을 이름으로만 표시했다. | 보완. 바깥 조건식과 닫힘 행을 명시했다. 마지막 else 부재를 기록했다. | 101·166–199·433 |
| [SwashBCStokeswave.ftn90.md](../swash/src/SwashBCStokeswave.ftn90.md):201–244 | 바깥 층 수 조건을 이름으로만 표시했다. | 보완. 바깥 조건식과 닫힘 행을 명시했다. 마지막 else 부재를 기록했다. | 101·166·201–243·433 |
| [SwashBCStokeswave.ftn90.md](../swash/src/SwashBCStokeswave.ftn90.md):245–284 | 바깥 층 수 조건을 이름으로만 표시했다. | 보완. 바깥 조건식과 닫힘 행을 명시했다. 마지막 else 부재를 기록했다. | 101·245–283·433 |
| [SwashBCStokeswave.ftn90.md](../swash/src/SwashBCStokeswave.ftn90.md):285–333 | 유속 계수를 kd의 18제곱까지로 설명했다. 바깥 조건을 이름으로만 표시했다. | 정정·보완. 18제곱은 괄호 안 다항식의 차수임을 명시했다. 바깥 kd 인자를 구분했다. 조건식과 닫힘 행을 보완했다. | 101·245·285–333·433 |
| [SwashBCStokeswave.ftn90.md](../swash/src/SwashBCStokeswave.ftn90.md):334–378 | 바깥 층 수 조건을 이름으로만 표시했다. | 보완. 바깥 조건식과 닫힘 행을 명시했다. 마지막 else 부재를 기록했다. | 101·334–377·433 |
| [SwashBCStokeswave.ftn90.md](../swash/src/SwashBCStokeswave.ftn90.md):379–400 | 바깥 층 수 조건을 이름으로만 표시했다. | 보완. 바깥 조건식과 닫힘 행을 명시했다. 마지막 else 부재를 기록했다. | 101·334·379–400·429–433 |
| [SwashBCStokeswave.ftn90.md](../swash/src/SwashBCStokeswave.ftn90.md):401–435 | 유속 계수를 kd의 24제곱까지로 설명했다. 바깥 조건·루프를 이름으로만 표시했다. | 정정·보완. 24제곱은 긴 괄호 안 다항식의 차수임을 명시했다. 바깥 인자를 구분했다. 조건식·루프문·닫힘 행을 보완했다. | 101·334·379·381·401–435 |
| [SwashBCboundwave.ftn90.md](../swash/src/SwashBCboundwave.ftn90.md):50–126 | 방향 변수의 좌표계와 vdir 값별 유속 성분을 생략했다. | 보완. wdir·theta1·theta2·theta3의 기준 좌표계와 vdir의 참·거짓 대응을 보완했다. | 70–79·117–119 |
| [SwashBCboundwave.ftn90.md](../swash/src/SwashBCboundwave.ftn90.md):170–214 | 파수 간격을 주기 길이의 2pi 배수로 설명했다. cycle의 반복 범위와 바깥 루프를 축약했다. | 정정·보완. 간격을 pi2/xclen 또는 pi2/yclen으로 바로잡았다. cycle이 현재 반복만 건너뜀을 명시했다. 바깥 루프문·닫힘 행·마지막 else 부재를 보완했다. | 148·170–214·359 |
| [SwashBCboundwave.ftn90.md](../swash/src/SwashBCboundwave.ftn90.md):215–269 | 바깥 루프를 이름으로만 표시했다. 주기 경계 조건 사슬의 마지막 else 부재를 생략했다. | 보완. 바깥 루프문·닫힘 행을 명시했다. bcperx 우선순위와 마지막 else 부재를 보완했다. | 148·215–269·359 |
| [SwashBCboundwave.ftn90.md](../swash/src/SwashBCboundwave.ftn90.md):270–313 | 바깥 조건·루프와 cycle의 반복 범위를 축약했다. | 보완. 바깥 조건식·루프문·닫힘 행을 명시했다. cycle이 현재 반복만 건너뜀을 명시했다. | 148·215·217·270–313·353–359 |
| [SwashBCboundwave.ftn90.md](../swash/src/SwashBCboundwave.ftn90.md):314–341 | 바깥 조건·루프를 이름으로만 표시했다. T1·T2의 변환 근거 일부를 생략했다. | 보완. 바깥 조건식·루프문·닫힘 행을 명시했다. 주석의 식 4.7 및 485쪽 변환 관계를 보완했다. | 148·215·217·284·314–341·353–359 |
| [SwashBCboundwave.ftn90.md](../swash/src/SwashBCboundwave.ftn90.md):342–361 | 바깥 조건·루프와 닫힘 행을 묶어서 기록했다. | 보완. 바깥 조건식·루프문과 각 블록의 닫힘 행을 명시했다. | 148·215·217·284·342–361 |
| [SwashBCshortwave.ftn90.md](../swash/src/SwashBCshortwave.ftn90.md):42–100 | 방향 변수의 좌표계와 vdir 값별 유속 성분을 생략했다. | 보완. wdir·theta의 기준 좌표계와 vdir의 참·거짓 대응을 보완했다. | 62–69·87 |
| [SwashBCshortwave.ftn90.md](../swash/src/SwashBCshortwave.ftn90.md):128–169 | 주석의 고전 어셀 수 식과 변형식의 적용 설명을 생략했다. | 보완. 주석 속 식을 원문 그대로 인용했다. kd > 1 또는 중간 수심이라는 설명을 보완했다. | 162–165 |
| [SwashBCshortwave.ftn90.md](../swash/src/SwashBCshortwave.ftn90.md):170–214 | 주기 방향 보정의 간격과 바깥 루프를 축약했다. 마지막 else 부재를 생략했다. | 보완. 파수 성분의 반올림 간격을 명시했다. 바깥 루프문·닫힘 행·마지막 else 부재를 보완했다. | 128·170–214·224 |
| [SwashBCshortwave.ftn90.md](../swash/src/SwashBCshortwave.ftn90.md):215–237 | 바깥 루프를 이름으로만 표시했다. 경고문에서 유효하지 않다는 부정을 생략했다. | 보완. 바깥 루프문과 경고 분기의 범위를 명시했다. PRINTF 출력문과 경고의 부정 의미를 보완했다. | 128·215–237 |

아래 구간은 대조 후 수정할 사항이 없었다.

| 기록 | 이상 없는 구간 |
|---|---|
| [SwanReadADCGrid.ftn90.md](../swash/src/SwanReadADCGrid.ftn90.md) | 1–59, 176–187 |
| [SwanReadEasymeshGrid.ftn90.md](../swash/src/SwanReadEasymeshGrid.ftn90.md) | 1–58, 139–155 |
| [SwanReadGrid.ftn90.md](../swash/src/SwanReadGrid.ftn90.md) | 1–57, 70–95 |
| [SwanReadTriangleGrid.ftn90.md](../swash/src/SwanReadTriangleGrid.ftn90.md) | 1–58, 116–133, 151–178 |
| [Swash.ftn90.md](../swash/src/Swash.ftn90.md) | 1–41, 42–53, 54–71 |
| [SwashAmbCurrent.ftn90.md](../swash/src/SwashAmbCurrent.ftn90.md) | 1–50 |
| [SwashAntiCreep2DH.ftn90.md](../swash/src/SwashAntiCreep2DH.ftn90.md) | 57–124 |
| [SwashAverOutp.ftn90.md](../swash/src/SwashAverOutp.ftn90.md) | 1–47, 48–80, 149–172, 173–195 |
| [SwashBCStokeswave.ftn90.md](../swash/src/SwashBCStokeswave.ftn90.md) | 1–41, 89–128 |
| [SwashBCboundwave.ftn90.md](../swash/src/SwashBCboundwave.ftn90.md) | 1–49, 127–169 |
| [SwashBCshortwave.ftn90.md](../swash/src/SwashBCshortwave.ftn90.md) | 1–41, 101–127, 238–253 |

정정 4, 보완 62, 이상 없음 25
