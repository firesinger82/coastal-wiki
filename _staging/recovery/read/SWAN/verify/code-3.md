# SWAN code-3 전수 대조 기록

검증일은 2026-10-13이다.
검증 범위는 사용자가 지정한 판독 기록 16개이다.
원문은 각 기록의 frontmatter `file:` 경로를 사용했다.
각 구간의 원문을 `nl -ba <원문> | sed -n 'A,Bp'`로 열어 의미와 인용을 대조했다.
한 번에 연 원문 구간은 모두 200행 이하였다.
오류와 누락은 해당 구간을 대조한 뒤 작은 `apply_patch`로 반영했다.

기록별 구간 표에서 94행을 대조했다.
원문에서 빈 행과 주석을 포함한 3,944행을 대조했다.
기록 하단의 코드 사실 46행도 해당 원문과 대조했다.
아래 행 수는 대상 기록의 구간 표와 코드 사실 목록에서 집계했다.

| 기록 | 대조한 구간 행 수 | 대조한 코드 사실 행 수 | 대조한 원문 행 수 | 원문 범위 | 변경 없는 구간 |
|---|---:|---:|---:|---|---|
| [SwanComputeForce.ftn90.md](../swan/src/SwanComputeForce.ftn90.md) | 8 | 3 | 317 | 1–317 | 1–59, 310–317 |
| [SwanConvAccur.ftn90.md](../swan/src/SwanConvAccur.ftn90.md) | 6 | 3 | 241 | 1–241 | 1–54 |
| [SwanConvStopc.ftn90.md](../swan/src/SwanConvStopc.ftn90.md) | 7 | 3 | 272 | 1–272 | 없음 |
| [SwanCreateEdges.ftn90.md](../swan/src/SwanCreateEdges.ftn90.md) | 5 | 3 | 194 | 1–194 | 1–52 |
| [SwanCrossObstacle.ftn90.md](../swan/src/SwanCrossObstacle.ftn90.md) | 3 | 2 | 113 | 1–113 | 1–51 |
| [SwanDiffPar.ftn90.md](../swan/src/SwanDiffPar.ftn90.md) | 9 | 4 | 460 | 1–460 | 없음 |
| [SwanDispParm.ftn90.md](../swan/src/SwanDispParm.ftn90.md) | 3 | 2 | 111 | 1–111 | 1–54 |
| [SwanFindObstacles.ftn90.md](../swan/src/SwanFindObstacles.ftn90.md) | 4 | 2 | 143 | 1–143 | 1–55 |
| [SwanFindPoint.ftn90.md](../swan/src/SwanFindPoint.ftn90.md) | 5 | 3 | 173 | 1–173 | 1–50 |
| [SwanGSECorr.ftn90.md](../swan/src/SwanGSECorr.ftn90.md) | 6 | 3 | 280 | 1–280 | 1–53 |
| [SwanGradDepthorK.ftn90.md](../swan/src/SwanGradDepthorK.ftn90.md) | 8 | 4 | 390 | 1–390 | 1–58 |
| [SwanGradVel.ftn90.md](../swan/src/SwanGradVel.ftn90.md) | 5 | 3 | 251 | 1–251 | 1–58 |
| [SwanGridCell.ftn90.md](../swan/src/SwanGridCell.ftn90.md) | 8 | 3 | 356 | 1–356 | 1–55 |
| [SwanGridFace.ftn90.md](../swan/src/SwanGridFace.ftn90.md) | 11 | 4 | 441 | 1–441 | 1–52 |
| [SwanGridTopology.ftn90.md](../swan/src/SwanGridTopology.ftn90.md) | 3 | 2 | 94 | 1–94 | 1–54, 77–94 |
| [SwanGridVert.ftn90.md](../swan/src/SwanGridVert.ftn90.md) | 3 | 2 | 108 | 1–108 | 1–52 |
| 합계 | 94 | 46 | 3944 | 각 원문 전체 | 16개 구간 |

조건과 계산식의 부정, 분기, 계수, 기본값, 단위, 실행 순서를 대조했다.
주석 속 식은 실행문과 구분했다.
구간 시작점의 바깥 블록과 `endif`·`enddo` 위치를 대조했다.
표본 오류 유형인 인덱스 계산, 주석 수식, 닫힌 바깥 조건, `else` 부재, 오류 처리 생략도 전체에서 확인했다.
전처리 표시의 기준은 `models/SWAN/raw/source_code/swan/switch.pl:82–105`이다.
대상 원문 16개에는 이 규칙에 해당하는 행 첫머리 전처리 표시가 없었다.

수정 후 구간 표의 실행 조건과 값 대입식에 대한 원문 인용 누락 검사는 0건이었다.
숫자 행 번호가 바로 붙은 코드 인용의 원문 대조에서 불일치는 0건이었다.
이 검사는 구간별 의미 대조를 보조했다.
원문의 SHA-256은 16개 모두 기존 frontmatter 값과 일치했다.
구간 경계와 frontmatter는 변경하지 않았다.
모델은 실행하지 않았다.
원문·노트·git은 수정하지 않았다.

아래 표의 원문 행은 해당 기록의 `file:`이 가리키는 원문 행이다.
`후속 사실`은 구간 표 아래 코드 사실 목록의 행을 가리킨다.
새 요지의 표식은 해당 기록 행에 붙인 정정·보완 표식에 대응한다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [SwanComputeForce.ftn90.md](../swan/src/SwanComputeForce.ftn90.md):60–132 | area를 면적으로 설명. ient 초기값의 원문 인용 누락. | [정정·보완] area는 쌍대영역 면적의 두 배. `ient = 0` 인용. | 80,88 |
| [SwanComputeForce.ftn90.md](../swan/src/SwanComputeForce.ftn90.md):133–151 | 응력 배열의 0 초기화를 요약만 함. | [보완] sxx·sxy·syy 초기화 대입식 인용. | 146–148 |
| [SwanComputeForce.ftn90.md](../swan/src/SwanComputeForce.ftn90.md):152–200 | 수심 대입과 누적 초기값 원문 인용 누락. 내부 루프 닫힘 행 누락. | [보완] 수심 대입과 여섯 누적 초기값 인용. 내부 루프 종료 행 명시. | 154,158–173,183,191 |
| [SwanComputeForce.ftn90.md](../swan/src/SwanComputeForce.ftn90.md):201–241 | area를 면적으로 요약. 초기값·셀/꼭짓점 번호·좌표 대입 인용 누락. | [정정·보완] area의 배수 설명 정정. 초기값과 번호·좌표 대입 및 루프 종료 보완. | 203–235,276,309 |
| [SwanComputeForce.ftn90.md](../swan/src/SwanComputeForce.ftn90.md):242–276 | area 누적을 면적 누적으로 설명. 다음 셀·좌표 대입 인용 누락. | [정정·보완] 면적의 두 배 누적으로 정정. 다음 셀·좌표 대입과 바깥 루프 종료 보완. | 88,245–264,309 |
| [SwanComputeForce.ftn90.md](../swan/src/SwanComputeForce.ftn90.md):277–309 | 면적 배수 누락. 오류 문자열 쓰기 및 분기 닫힘 행 누락. | [정정·보완] 면적의 두 배로 나눔을 명시. 오류 문자열·호출·cycle 및 ENDIF 행 보완. | 88,280–302 |
| [SwanConvAccur.ftn90.md](../swan/src/SwanConvAccur.ftn90.md):55–104 | ient 초기값 원문 인용 및 accur 백분율 단위 누락. | [보완] `ient = 0`과 accur의 백분율 단위 보완. | 59,70 |
| [SwanConvAccur.ftn90.md](../swan/src/SwanConvAccur.ftn90.md):105–148 | 카운터·평균·차이·헤더 초기값을 요약만 함. | [보완] 모든 초기값과 반복 초기화 원문 인용. 블록 종료 행 보완. | 111–138 |
| [SwanConvAccur.ftn90.md](../swan/src/SwanConvAccur.ftn90.md):149–194 | 시험점 플래그·모멘트 초기값 원문 인용 누락. | [보완] 플래그와 모멘트 초기값 및 내부·바깥 블록 종료 행 보완. | 151–193,226–228 |
| [SwanConvAccur.ftn90.md](../swan/src/SwanConvAccur.ftn90.md):195–228 | 출력 배열 대입과 시험점 상대차 식·헤더 플래그 대입 인용 누락. | [보완] 배열 대입·상대차 네 식·헤더 플래그 및 출력 분기 종료 인용. | 200–201,217–219 |
| [SwanConvAccur.ftn90.md](../swan/src/SwanConvAccur.ftn90.md):229–241 | accur를 활성 꼭짓점 비율이라고만 설명. | [정정] 활성 꼭짓점 중 요구 정확도 달성 꼭짓점의 백분율로 정정. | 234–236 |
| [SwanConvStopc.ftn90.md](../swan/src/SwanConvStopc.ftn90.md):1–64 | 파고 급변만 요약하여 곡률 기준의 위험이라는 원문 판단 누락. | [보완] 주석에 명시된 곡률 기준 위험과 그 이유 보완. | 50–52 |
| [SwanConvStopc.ftn90.md](../swan/src/SwanConvStopc.ftn90.md):65–122 | 초기값 인용·accur 단위·차이 배열의 두 반복 위치 누락. | [보완] ient 원문 인용. 백분율 단위와 현재·전전 반복을 명시. | 69,74,77,84 |
| [SwanConvStopc.ftn90.md](../swan/src/SwanConvStopc.ftn90.md):123–163 | 카운터·차이 배열·헤더·시험점 초기화 인용 누락. | [보완] 초기화 대입과 시험점 블록 종료 행 보완. | 129–151 |
| [SwanConvStopc.ftn90.md](../swan/src/SwanConvStopc.ftn90.md):164–199 | elseif를 병렬 분기로 표현. 초기 모멘트·차이 대입 인용 누락. | [정정·보완] elseif의 순차 조건 관계 정정. 초기값·차이 대입·블록 종료 보완. | 166–198 |
| [SwanConvStopc.ftn90.md](../swan/src/SwanConvStopc.ftn90.md):200–239 | 이전 차이 보관식 원문 인용과 개별 블록 종료 행 누락. | [보완] 두 보관식 인용. 내부·바깥 조건과 반복 종료 행 구별. | 202,208,235–258 |
| [SwanConvStopc.ftn90.md](../swan/src/SwanConvStopc.ftn90.md):240–258 | 시험점 출력식을 요약만 함. 헤더 플래그 대입 인용 누락. | [보완] 출력 식 전체와 헤더 플래그 대입 및 출력 분기 종료 보완. | 247–249 |
| [SwanConvStopc.ftn90.md](../swan/src/SwanConvStopc.ftn90.md):259–272 | accur의 백분율 단위를 마지막 계산에서 생략. | [보완] 계산 대상과 백분율 단위 명시. | 265–267 |
| [SwanCreateEdges.ftn90.md](../swan/src/SwanCreateEdges.ftn90.md):53–80 | ient 초기값을 요약만 함. | [보완] 초기값 원문 인용. | 55 |
| [SwanCreateEdges.ftn90.md](../swan/src/SwanCreateEdges.ftn90.md):81–106 | istat 초기값 누락. 배열·면 수 초기값 및 할당 오류 메시지 인용 누락. | [보완] 초기값 전체와 할당 오류 메시지·return·ENDIF 보완. | 87–105 |
| [SwanCreateEdges.ftn90.md](../swan/src/SwanCreateEdges.ftn90.md):107–160 | 끝점·면 번호·플래그 대입을 요약만 함. 내부 종료 행 구분 누락. | [보완] 모든 끝점·면 번호·플래그 대입 인용. 검색 블록 종료 행 명시. | 109–159 |
| [SwanCreateEdges.ftn90.md](../swan/src/SwanCreateEdges.ftn90.md):161–194 | 초과 오류 메시지 및 목록·끝점 저장식 인용 누락. | [보완] 세 오류 분기의 메시지·return·ENDIF와 목록·끝점 대입 보완. | 164–186 |
| [SwanCrossObstacle.ftn90.md](../swan/src/SwanCrossObstacle.ftn90.md):52–80 | ient 초기값 원문 인용 누락. | [보완] 초기값 인용. | 61 |
| [SwanCrossObstacle.ftn90.md](../swan/src/SwanCrossObstacle.ftn90.md):81–113 | 교차 반환값의 초기 대입과 else 대입 인용 누락. | [보완] 두 논리 대입식 인용. | 85,109 |
| [SwanDiffPar.ftn90.md](../swan/src/SwanDiffPar.ftn90.md):1–85 | 두 원래 아이코날 식의 인용과 Berkhoff에서 D의 의미 누락. | [보완] 두 주석 분수식·delta 식·연산자 구분·K/k 정의 보완. | 44–72 |
| [SwanDiffPar.ftn90.md](../swan/src/SwanDiffPar.ftn90.md):86–156 | 초기값 인용과 셀 면적/쌍대영역 면적의 두 배 구분 누락. | [보완] ient 초기값 인용. area0·area1·carea 구분. | 95,105–107 |
| [SwanDiffPar.ftn90.md](../swan/src/SwanDiffPar.ftn90.md):157–213 | 파고·군속도·방향 계수 초기값 및 수심 대입 인용 누락. | [보완] 네 대입식과 에너지 조건 종료 행 보완. | 170–178,190,208 |
| [SwanDiffPar.ftn90.md](../swan/src/SwanDiffPar.ftn90.md):214–278 | carea를 면적으로 설명. 초기값·셀 정보 대입 인용 누락. | [정정·보완] 면적의 두 배로 정정. 초기값·번호·좌표·면적 대입 및 구면 조건 종료 보완. | 107,226–248,272 |
| [SwanDiffPar.ftn90.md](../swan/src/SwanDiffPar.ftn90.md):279–334 | carea 누적을 면적으로 설명. 다음 셀 정보 대입 인용 누락. | [정정·보완] 면적의 두 배로 정정. 셀 정보 대입·구면 조건·바깥 루프 종료 보완. | 107,281–291,315,324,362 |
| [SwanDiffPar.ftn90.md](../swan/src/SwanDiffPar.ftn90.md):335–369 | 정규화 분모의 배수와 내부·바깥 종료 및 else 부재를 구분하지 않음. | [보완] carea 정의와 세 IF·루프의 종료 행 명시. | 107,338–362 |
| [SwanDiffPar.ftn90.md](../swan/src/SwanDiffPar.ftn90.md):370–407 | carea를 면적으로 설명. 회절 미분·누적 초기값과 셀 대입 인용 누락. | [정정·보완] 면적의 두 배로 정정. 초기값·셀·좌표 대입 인용. | 107,372–402 |
| [SwanDiffPar.ftn90.md](../swan/src/SwanDiffPar.ftn90.md):408–437 | carea 누적을 면적으로 설명. 다음 셀 대입 인용 누락. | [정정·보완] 면적의 두 배로 정정. 셀·좌표 대입과 바깥 루프 종료 보완. | 107,410–427,458 |
| [SwanDiffPar.ftn90.md](../swan/src/SwanDiffPar.ftn90.md):438–460 | 최종 미분 대입 인용과 정규화 배수 및 개별 블록 종료 누락. | [보완] 두 출력 대입·carea 정의·블록 종료·else 부재 보완. | 107,439–458 |
| [SwanDispParm.ftn90.md](../swan/src/SwanDispParm.ftn90.md):55–81 | ient 초기값 인용 누락. | [보완] 초기값 인용. | 67 |
| [SwanDispParm.ftn90.md](../swan/src/SwanDispParm.ftn90.md):82–111 | 스텐실·수심·진흙 두께 대입과 얕은 수심 기본값 인용 누락. | [보완] 모든 대입식·기본값 및 내부 블록 종료 행 보완. | 86–108 |
| [SwanFindObstacles.ftn90.md](../swan/src/SwanFindObstacles.ftn90.md):56–87 | ient 초기값 인용 누락. | [보완] 초기값 인용. | 63 |
| [SwanFindObstacles.ftn90.md](../swan/src/SwanFindObstacles.ftn90.md):88–112 | 교차 배열 초기값 및 장애물 선분 좌표 대입 인용 누락. | [보완] 초기값과 좌표 대입 네 식 인용. | 97,105–111 |
| [SwanFindObstacles.ftn90.md](../swan/src/SwanFindObstacles.ftn90.md):113–143 | 면 번호·좌표·선분 갱신 대입 및 개별 루프 종료 행 누락. | [보완] 끝점·좌표·선분 갱신 대입과 세 루프 종료 행 보완. | 119–141 |
| [SwanFindPoint.ftn90.md](../swan/src/SwanFindPoint.ftn90.md):51–88 | ient 초기값 인용 누락. | [보완] 초기값 인용. | 60 |
| [SwanFindPoint.ftn90.md](../swan/src/SwanFindPoint.ftn90.md):89–122 | 좌표·최소거리 갱신 대입 인용 누락. 미발견 대입·return 위치를 묶음 표시. | [보완] 좌표·번호·거리 대입 인용. 미발견 대입·return·ENDIF 분리. | 99–119 |
| [SwanFindPoint.ftn90.md](../swan/src/SwanFindPoint.ftn90.md):123–145 | 면 번호·좌표 대입과 바깥 블록 종료 행 누락. | [보완] 대입 여섯 식과 경계 조건·면 루프·바깥 조건 종료 보완. | 133–139,167–171 |
| [SwanFindPoint.ftn90.md](../swan/src/SwanFindPoint.ftn90.md):146–173 | 끝점 대입을 반환으로 요약. 대입식과 각 종료 위치 누락. | [정정·보완] 끝점 저장과 exit 실행 위치 구분. 모든 미발견·끝점 대입과 종료 행 보완. | 150–171 |
| [SwanFindPoint.ftn90.md](../swan/src/SwanFindPoint.ftn90.md):후속 사실 53–54·97–171 | kvert는 내부 꼭짓점 루프와 경계 면 분기에서만 대입된다고 단정. | [정정] 경계 상자 밖 분기의 99행 대입을 포함하도록 정정. | 97–100,117,151–164 |
| [SwanGSECorr.ftn90.md](../swan/src/SwanGSECorr.ftn90.md):54–117 | carea를 쌍대영역 면적으로 설명. ient 인용 누락. | [정정·보완] 면적의 두 배로 정정. 초기값 인용. | 78,88 |
| [SwanGSECorr.ftn90.md](../swan/src/SwanGSECorr.ftn90.md):118–160 | carea를 면적으로 요약. 꼭짓점 대입과 누적 초기값 인용 누락. | [정정·보완] 면적 배수 정정. 꼭짓점·초기값·주파수 분기 종료 보완. | 88,125,141,157–159 |
| [SwanGSECorr.ftn90.md](../swan/src/SwanGSECorr.ftn90.md):161–202 | 현재 셀 정보 대입과 블록 종료 행 누락. | [보완] 셀·꼭짓점·좌표·면적 대입 및 내부·바깥 종료 행 보완. | 167–177,196,253–278 |
| [SwanGSECorr.ftn90.md](../swan/src/SwanGSECorr.ftn90.md):203–253 | carea를 면적으로 설명. 다음 셀 대입과 내부·바깥 종료 행 누락. | [정정·보완] 면적의 두 배로 정정. 다음 셀 대입과 종료 행 보완. | 88,205–243,276–278 |
| [SwanGSECorr.ftn90.md](../swan/src/SwanGSECorr.ftn90.md):254–280 | 정규화 배수와 개별 종료 행 및 else 부재 누락. | [보완] 분모 정의와 조건·루프 종료를 구분. | 88,257–278 |
| [SwanGSECorr.ftn90.md](../swan/src/SwanGSECorr.ftn90.md):후속 사실 181–187·219–225·257 | carea를 쌍대영역 면적으로 설명. | [정정] 쌍대영역 면적의 두 배로 정정. | 88,257 |
| [SwanGradDepthorK.ftn90.md](../swan/src/SwanGradDepthorK.ftn90.md):59–110 | area를 면적으로 설명. ient 초기값 인용 누락. | [정정·보완] 면적의 두 배로 정정. 초기값 인용. | 74,80 |
| [SwanGradDepthorK.ftn90.md](../swan/src/SwanGradDepthorK.ftn90.md):111–159 | 면적 배수 누락. 미분·면적 초기값과 셀·수심 대입 인용 누락. | [정정·보완] 면적의 두 배로 정정. 초기값과 셀·수심 대입 인용. | 80,113–150 |
| [SwanGradDepthorK.ftn90.md](../swan/src/SwanGradDepthorK.ftn90.md):160–204 | area 누적을 면적으로 설명. 셀·수심·좌표 대입 인용 누락. | [정정·보완] 면적의 두 배로 정정. 모든 셀·수심·좌표 대입 인용. | 80,162–194 |
| [SwanGradDepthorK.ftn90.md](../swan/src/SwanGradDepthorK.ftn90.md):205–237 | 오류 문자열 쓰기·표지의 초기화 식·면적 배수·종료 행 누락. | [보완] 오류 문자열·msgerr·return과 10번 표지 대입 및 종료 행 보완. | 80,212–236 |
| [SwanGradDepthorK.ftn90.md](../swan/src/SwanGradDepthorK.ftn90.md):238–300 | 면적 배수 누락. 면적 초기값·셀 정보·진흙 두께 대입 인용 누락. | [정정·보완] 면적의 두 배로 정정. 초기값과 모든 셀·진흙 대입 및 종료 행 보완. | 80,240–295 |
| [SwanGradDepthorK.ftn90.md](../swan/src/SwanGradDepthorK.ftn90.md):301–356 | 면적 누적 배수 누락. 다음 셀·진흙 대입 인용과 종료 행 누락. | [정정·보완] 면적의 두 배로 정정. 셀·수심·좌표·진흙 대입과 블록 종료 보완. | 80,303–346,388 |
| [SwanGradDepthorK.ftn90.md](../swan/src/SwanGradDepthorK.ftn90.md):357–390 | 오류 문자열·30번 표지 초기화 식·정규화 배수·종료 행 누락. | [보완] write·msgerr·return·표지 대입과 면적 배수 및 종료 행 보완. | 80,364–388 |
| [SwanGradVel.ftn90.md](../swan/src/SwanGradVel.ftn90.md):59–108 | area를 면적으로 설명. ient 초기값 인용 누락. | [정정·보완] 쌍대영역 면적의 두 배로 정정. 초기값 인용. | 74,80 |
| [SwanGradVel.ftn90.md](../swan/src/SwanGradVel.ftn90.md):109–158 | 면적 배수 누락. 미분·면적 초기값과 셀·수심 대입 인용 및 주석 조건 누락. | [정정·보완] 면적의 두 배로 정정. 초기값·셀 정보·수심 대입과 120행 주석 뜻 보완. | 80,111–149 |
| [SwanGradVel.ftn90.md](../swan/src/SwanGradVel.ftn90.md):159–213 | area 누적 배수 누락. 셀·좌표·수심 대입 인용 누락. | [정정·보완] 면적의 두 배로 정정. 셀·좌표·수심 대입 인용. | 80,161–201 |
| [SwanGradVel.ftn90.md](../swan/src/SwanGradVel.ftn90.md):214–251 | 오류 문자열 쓰기·표지 초기값·면적 배수·구면 조건 종료 누락. | [보완] 오류 write·msgerr·return과 표지 대입 및 정규화 정의 보완. | 80,221–249 |
| [SwanGridCell.ftn90.md](../swan/src/SwanGridCell.ftn90.md):56–116 | ient 초기값 인용 누락. | [보완] 초기값 인용. | 70 |
| [SwanGridCell.ftn90.md](../swan/src/SwanGridCell.ftn90.md):117–162 | 셀 크기·식별자·기본 표지·활성·꼭짓점·면적 대입 인용 누락. | [보완] 셀 속성 대입식 전체 인용. | 130–158 |
| [SwanGridCell.ftn90.md](../swan/src/SwanGridCell.ftn90.md):163–200 | 공변 성분·방향 저장식 인용과 갱신 순서 설명 누락. | [보완] 저장식 인용. 순차 대입 의존 관계와 내부·바깥 루프 종료 명시. | 173–198,251 |
| [SwanGridCell.ftn90.md](../swan/src/SwanGridCell.ftn90.md):201–251 | 좌표 초기값·입력 좌표·무게중심/외심·면 저장식 및 개별 종료 행 누락. | [보완] 누락 대입식 전체와 조건·루프 종료 행 보완. | 207–249 |
| [SwanGridCell.ftn90.md](../swan/src/SwanGridCell.ftn90.md):252–291 | 식별자 대응·초기값·조회·인접 셀 저장식 인용과 루프 종료 구분 누락. | [보완] 대응 배열과 인접 셀 대입식 및 세 루프 종료 명시. | 261–288 |
| [SwanGridCell.ftn90.md](../swan/src/SwanGridCell.ftn90.md):292–316 | 인접 셀 수·셀·꼭짓점 대입 인용과 블록 종료 행 누락. | [보완] 조회 대입식과 내부·바깥 종료 행 보완. | 294–315,352–354 |
| [SwanGridCell.ftn90.md](../swan/src/SwanGridCell.ftn90.md):317–356 | 발견 플래그·후보 셀·꼭짓점·연결 저장식과 개별 종료 행 누락. | [보완] 모든 누락 대입식과 중첩 조건·루프 종료 보완. | 319–354 |
| [SwanGridFace.ftn90.md](../swan/src/SwanGridFace.ftn90.md):53–121 | ient 인용과 입력 면 끝점 배열을 채울 주체의 요구 누락. | [보완] 초기값 인용. 격자 생성기 입력 의무 주석 보완. | 59–60,73 |
| [SwanGridFace.ftn90.md](../swan/src/SwanGridFace.ftn90.md):122–170 | 면 번호·끝점·길이 저장과 여섯 기본값 인용 누락. | [보완] 면 속성 대입과 기본값 모두 인용. | 136–167 |
| [SwanGridFace.ftn90.md](../swan/src/SwanGridFace.ftn90.md):171–203 | 초기값·끝점·목록 저장식·초과 오류 메시지 인용 누락. | [보완] 초기값·대입·메시지·return·ENDIF 보완. | 176–200 |
| [SwanGridFace.ftn90.md](../swan/src/SwanGridFace.ftn90.md):204–257 | 국소 끝점·검색 번호·플래그·ID 저장식과 오류 메시지 및 내부 종료 누락. | [보완] 조회·저장식·오류 처리·중첩 블록 종료 모두 보완. | 214–256 |
| [SwanGridFace.ftn90.md](../swan/src/SwanGridFace.ftn90.md):258–284 | 전역 끝점·인접 셀 저장식 인용 및 구체적 오류 메시지·종료 위치 누락. | [보완] 조회·저장식·반시계 순서 오류 메시지·return·종료 행 보완. | 258–281 |
| [SwanGridFace.ftn90.md](../swan/src/SwanGridFace.ftn90.md):285–320 | 법선 방향을 좌측 셀 밖에서 시작한다고 표현. 조회·좌우 선택·저장식 누락. | [정정·보완] 좌측 셀에서 나오는 방향으로 정정. 모든 조회·선택·저장식과 종료 행 보완. | 293–317 |
| [SwanGridFace.ftn90.md](../swan/src/SwanGridFace.ftn90.md):321–360 | 보간·거리 기본값과 끝점·셀·좌표 대입 및 종료 행 누락. | [보완] 모든 대입식과 내부·바깥 조건·면 루프 종료 보완. | 323–359,416–418 |
| [SwanGridFace.ftn90.md](../swan/src/SwanGridFace.ftn90.md):361–400 | 좌우 셀·외심·중점·무게중심 대입 및 기본값 전체 식 누락. | [보완] 조회 대입식·기본값·내부와 바깥 종료 행 보완. | 363–399,416–418 |
| [SwanGridFace.ftn90.md](../swan/src/SwanGridFace.ftn90.md):401–418 | 우측 무게중심 대입과 역거리 기본값 전체 식 누락. | [보완] 좌표·기본값 대입 인용. 비영 거리 조건 종료 명시. | 403–414 |
| [SwanGridFace.ftn90.md](../swan/src/SwanGridFace.ftn90.md):419–441 | 셀 표지 초기화·설정·면 번호 조회 대입 인용 누락. | [보완] 세 대입식과 exit 및 조건 종료 보완. | 424–435 |
| [SwanGridTopology.ftn90.md](../swan/src/SwanGridTopology.ftn90.md):55–76 | 할당 오류 메시지 생략. 초기값 인용에서 공백 생략. | [보완] 원문 초기값 인용과 오류 메시지·return·ENDIF 명시. | 57,73–76 |
| [SwanGridVert.ftn90.md](../swan/src/SwanGridVert.ftn90.md):53–74 | 초기값 인용을 원문과 다르게 `ient=0`으로 표기. | [정정] 원문 그대로 `ient = 0`으로 인용. | 64 |
| [SwanGridVert.ftn90.md](../swan/src/SwanGridVert.ftn90.md):75–108 | ID·경계조건·활성·좌표 대입식 원문 인용 누락. | [보완] 꼭짓점 속성 대입식 전체 인용. | 87–104 |

마지막 집계의 단위는 기록의 구간 행과 코드 사실 행이다.
정정과 보완은 각각 해당 표식이 붙은 행 수이다.
같은 행에 두 표식이 있으면 양쪽에 각각 집계했다.
이상 없음은 대조 후 수정하지 않은 행 수이다.
변경한 행은 80개이다.
두 표식이 함께 붙은 행은 22개이다.
변경 없는 행은 구간 표 16행과 코드 사실 44행이다.

정정 26, 보완 76, 이상 없음 60
