# SWAN code-4 전수 검증

검증일은 2026-10-13이다.
각 기록의 frontmatter `file:`에 적힌 원문을 대조했다.
기록의 구간마다 `nl -ba <원문> | sed -n 'A,Bp'`로 원문을 열었다.
각 원문 출력은 200행 이하였다.
구간에 포함된 주석과 빈 행도 확인했다.

`swan/switch.pl` 82–105행의 전처리 규칙을 확인했다.
규칙에서 `!JAC`는 `jac=TRUE`일 때 제거된다.
`!WFR`는 그 ELSE 경로에서 제거된다.
`!MPI`는 `mpi=TRUE`일 때 제거된다.
`!NCF`는 `ncf=TRUE`일 때 제거된다.
대상 원문 8개에는 행 첫머리 전처리 표지가 없다.

아래 원문 행 수는 각 원문의 1행부터 마지막 행까지 센 값이다.
대조 구간 행 수는 각 기록의 구간 표에서 셌다.
코드 사실 항목 수는 각 기록 끝의 목록에서 셌다.
정정·보완·이상 없음의 집계 단위는 구간 행 또는 코드 사실 항목 하나이다.
정정과 보완을 함께 한 7건은 두 열에 모두 포함했다.
대조한 기록 항목은 총 104건이다.
내용을 수정한 기록 항목은 총 59건이다.

| 기록 | 원문 행 수 | 대조 구간 행 수 | 대조 코드 사실 항목 수 | 정정 | 보완 | 정정·보완 중복 | 이상 없음 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [SwanGriddata.ftn90.md](../swan/src/SwanGriddata.ftn90.md) | 89 | 3 | 0 | 1 | 0 | 0 | 2 |
| [SwanGridobjects.ftn90.md](../swan/src/SwanGridobjects.ftn90.md) | 194 | 6 | 2 | 0 | 5 | 0 | 3 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md) | 1,230 | 31 | 12 | 3 | 27 | 3 | 16 |
| [SwanInitCompGrid.ftn90.md](../swan/src/SwanInitCompGrid.ftn90.md) | 103 | 4 | 2 | 0 | 3 | 0 | 3 |
| [SwanInterpolateAc.ftn90.md](../swan/src/SwanInterpolateAc.ftn90.md) | 296 | 7 | 4 | 0 | 6 | 0 | 5 |
| [SwanInterpolateOutput.ftn90.md](../swan/src/SwanInterpolateOutput.ftn90.md) | 317 | 7 | 4 | 0 | 6 | 0 | 5 |
| [SwanInterpolatePoint.ftn90.md](../swan/src/SwanInterpolatePoint.ftn90.md) | 248 | 6 | 3 | 0 | 4 | 0 | 5 |
| [SwanIntgratSpc.ftn90.md](../swan/src/SwanIntgratSpc.ftn90.md) | 348 | 8 | 5 | 5 | 6 | 4 | 6 |
| 합계 | 2,825 | 72 | 32 | 9 | 57 | 7 | 45 |

수정 목록의 원문 행은 해당 기록의 frontmatter `file:`을 기준으로 한다.
`코드 사실` 표시는 구간 표 아래의 기존 목록 항목을 뜻한다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [SwanGriddata.ftn90.md](../swan/src/SwanGriddata.ftn90.md):52–76 | kvertc,kvertf를 셀 및 면 꼭짓점 번호 배열로 단정했다. | [정정] 원문에서 확인되는 저장·할당 가능 2차원 정수 배열 선언만 기록했다. | 68–69 |
| [SwanGridobjects.ftn90.md](../swan/src/SwanGridobjects.ftn90.md):57–79 | 경계 및 경계조건 표지를 0/1로 정의한다고만 적었다. | [보완] 각 표지의 0과 1에 대응하는 상태를 명시했다. | 66–70 |
| [SwanGridobjects.ftn90.md](../swan/src/SwanGridobjects.ftn90.md):80–106 | 셀 경계 표지를 0/1 설명으로 줄였다. | [보완] 경계 셀은 1이고 내부 셀은 0임을 명시했다. | 91–92 |
| [SwanGridobjects.ftn90.md](../swan/src/SwanGridobjects.ftn90.md):107–145 | 경계 표지와 좌우 셀 대응을 구체적으로 적지 않았다. | [보완] 표지의 0/1 의미와 끝점 방향벡터에 대한 첫 번째·두 번째 셀의 위치를 명시했다. | 113–123 |
| [SwanGridobjects.ftn90.md](../swan/src/SwanGridobjects.ftn90.md):146–175 | 반변 기저 성분과 면 방향을 포괄적으로 적었다. | [보완] 주석의 기저 성분 식과 현재 꼭짓점으로 향하는 면 방향을 명시했다. | 156–158 |
| [SwanGridobjects.ftn90.md](../swan/src/SwanGridobjects.ftn90.md):176–194 | fullupdated를 완전 갱신 상태라고만 적었다. | [보완] 지리 공간과 스펙트럼 공간 모두에서 갱신된 상태라는 주석을 보완했다. | 180 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):1–77 | nmax가 최대 개수라는 한정과 E0의 단위·분포 설명이 빠졌다. | [보완] nmax의 최대 개수와 E0의 J/m2 단위·균등 주파수 분포를 명시했다. | 54–70 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):141–173 | ient 초기값이 백틱 원문으로 인용되지 않았다. | [보완] ient 초기값 선언을 원문 그대로 인용했다. | 144 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):174–206 | 주파수 개수·첫 주파수 대입의 원문 인용과 분기 종료 위치가 빠졌다. | [보완] MSC와 SPCSIG(1) 대입을 인용했다. 주파수 분포 조건의 ELSE와 ENDIF 위치를 명시했다. | 174–207·267 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):207–240 | 최저·최고 주파수와 첫 주파수의 대입식을 생략했다. | [보완] slow·shig·SPCSIG(1)·freqs(1)의 대입식을 인용했다. | 209–210·224·236 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):241–267 | 보간 결과의 대입식을 생략했다. | [보완] AC2 대입식을 인용했다. | 258 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):268–289 | 장애물 경계조건용 배열을 SWTRCF로 설명했다. 첫 주파수 거듭제곱 대입 인용이 빠졌다. | [정정·보완] 해당 배열은 Ebig이고 참조 루틴은 SWTRCF임을 구분했다. SIGPOW 첫 열의 대입식을 인용했다. | 276·283–284 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):290–323 | 경계 개수·경계 주소·작용밀도 초기화의 대입식을 생략했다. | [보완] 서쪽·남쪽·북쪽 경계의 주소와 영 대입식을 인용했다. | 293–318 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):381–409 | ient 초기값의 원문 인용과 E의 주석 단위가 빠졌다. | [보완] ient 초기값 선언과 E의 분산 밀도 단위를 인용했다. | 384·396 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):410–447 | E를 에너지 밀도로 설명했다. 영 파고 대입과 ELSE 없는 경계 조건 설명이 빠졌다. | [정정·보완] E를 분산 밀도로 고쳤다. 밀도·격자 주소·영 파고 대입과 조건 종료를 보완했다. | 396·412–446 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):448–487 | 첫 주파수·보간 입출력의 대입식을 생략했다. | [보완] freq(1)·spec1·E0의 대입식을 인용했다. | 457·471·477 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):488–551 | 방법 주석의 nic 증가 설명과 반복 조건을 생략했다. | [보완] 주석의 설명을 기록했다. 실제 증가 대상 e_trs와 구분했다. | 534–535·616·645 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):552–606 | ient와 임시 배열의 초기값 대입을 요약했다. | [보완] 초기값 선언과 배열별 영·거짓 대입을 인용했다. | 555·592–605 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):607–648 | 선택된 주파수·방향 번호 대입과 쌍 수 초기값 인용이 빠졌다. | [보완] iwtt·ittt·nic의 대입식을 인용했다. | 620·625–626·636 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):649–678 | 두 오류 호출의 내용·등급과 선택 번호·개수 저장식을 생략했다. | [보완] 실제 msgerr 호출을 인용했다. 선택 번호와 주파수별 성분 수의 대입식을 인용했다. | 649–672 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):738–800 | ient 초기값 인용과 방향 표의 열별 의미·단위가 빠졌다. | [보완] 초기값 선언과 방향 표의 여섯 열을 보완했다. Ev의 주석 단위를 기록했다. | 745–750·758·789 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):855–898 | 건조점 고정값·Ebig 초기값·물리 계수의 대입식을 생략했다. | [보완] 각 고정값과 초기값·계수 대입을 인용했다. | 875–886 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):899–934 | 수심과 건조점 군속도의 대입식을 생략했다. | [보완] deploc와 cg(ind)의 대입식을 인용했다. | 901·929 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):935–969 | 두 성분의 인덱스·방향 사인·각주파수 대입을 생략했다. | [보완] 모든 성분 추출 대입을 인용했다. 부정이 들어간 차주파수 상한 조건의 뜻을 명시했다. | 941–966 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):970–1000 | 격자 주소·수심·외해 위상속도 대입과 내부 IF의 종료를 생략했다. | [보완] 해당 대입식을 인용했다. 990행 IF가 995행에서 닫힘을 명시했다. | 973–995 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):1035–1070 | 건조점 고정값의 원문 인용과 바깥 조건·루프의 개별 종료 위치가 빠졌다. | [보완] 고정값 대입식을 인용했다. IF와 두 공간 루프의 종료 행을 대응시켰다. | 1057–1069 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):1071–1094 | 외해 주소·수심과 경계 위상 초기값의 인용이 빠졌다. | [보완] 각 대입식을 원문 그대로 인용했다. | 1076·1080·1089–1091 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):1095–1129 | 현재 주소·수심 대입과 주석 식을 제외한 이유가 빠졌다. | [보완] 두 대입식을 인용했다. 주석이 밝힌 제외 이유를 보완했다. | 1097·1099·1112 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):1130–1158 | T5 기본값의 원문 인용과 내부 조건 종료가 빠졌다. | [보완] T5 영 대입과 ENDIF 행을 보완했다. | 1147–1149 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):1159–1174 | 건조점 속도 인용이 원문과 달랐다. 바깥 블록의 종료 위치를 묶어서 적었다. | [보완] Ut 영 대입을 원문으로 인용했다. 조건·공간 루프의 종료와 후속 주파수 계산 위치를 명시했다. | 1161–1173 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):1175–1207 | jdl < 1을 음수 방향 번호 보정이라고 설명했다. 격자 주소·수심 대입을 생략했다. | [정정·보완] 0을 포함하는 1 미만 조건으로 고쳤다. 주소·수심 대입을 인용했다. | 1178·1184–1192 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):1208–1230 | 차주파수 조건과 두 성분 루프의 종료를 묶어서 적었다. | [보완] ELSE가 없는 차주파수 조건과 이름 있는 두 루프의 종료를 각각 대응시켰다. | 959·1208–1211 |
| [SwanIEM.ftn90.md](../swan/src/SwanIEM.ftn90.md):코드 사실 801·1033·1073–1082 | 각 y 행 서쪽 점에서 kbly 값을 설정한다고만 적었다. | [보완] kbly 대입이 유효 젖은 점 조건과 서쪽 점 조건을 모두 통과해야 함을 명시했다. | 970–1033·1073–1082 |
| [SwanInitCompGrid.ftn90.md](../swan/src/SwanInitCompGrid.ftn90.md):53–67 | ient 초기값이 원문 그대로 인용되지 않았다. | [보완] 초기값 선언 전체를 인용했다. | 59 |
| [SwanInitCompGrid.ftn90.md](../swan/src/SwanInitCompGrid.ftn90.md):68–88 | 초기값·전역 크기 대입과 할당 오류 메시지를 축약했다. | [보완] 각 대입과 실제 오류 호출·RETURN을 인용했다. 두 조건의 종료 위치를 명시했다. | 74–88 |
| [SwanInitCompGrid.ftn90.md](../swan/src/SwanInitCompGrid.ftn90.md):89–103 | 격자 크기 대입의 인용이 원문과 달랐다. MCGRD의 주석 용도가 빠졌다. | [보완] 각 대입을 원문 그대로 인용했다. 주석의 AC1·COMPDA 할당 목적을 명시했다. | 96–100 |
| [SwanInterpolateAc.ftn90.md](../swan/src/SwanInterpolateAc.ftn90.md):62–119 | ient 초기값 인용이 빠졌다. | [보완] 초기값 선언을 인용했다. | 73 |
| [SwanInterpolateAc.ftn90.md](../swan/src/SwanInterpolateAc.ftn90.md):120–159 | 포인터 연결·결과 초기값·일치 분기 대입·셀 발견 초기값을 축약했다. | [보완] 포인터 연결과 모든 초기값·복사식을 인용했다. 일치 조건의 RETURN·ENDIF를 명시했다. | 124–156 |
| [SwanInterpolateAc.ftn90.md](../swan/src/SwanInterpolateAc.ftn90.md):160–200 | 셀·꼭짓점·면 방향 대입과 여유각·발견 플래그 기본값이 빠졌다. | [보완] 각 대입을 인용했다. 두 EXIT의 대상과 셀 루프의 종료를 명시했다. | 164–200 |
| [SwanInterpolateAc.ftn90.md](../swan/src/SwanInterpolateAc.ftn90.md):201–230 | 미발견 메시지의 좌표 오프셋과 각 초기화 대입을 생략했다. | [보완] WRITE·msgerr·RETURN의 순서를 인용했다. 좌표·예외·교차 플래그 대입을 보완했다. | 205–219 |
| [SwanInterpolateAc.ftn90.md](../swan/src/SwanInterpolateAc.ftn90.md):231–269 | 장애물 수·좌표·포인터 갱신과 조건 종료를 축약했다. | [보완] 모서리 수와 선분 끝점·시작점 대입을 인용했다. 연결 순서와 조건 종료를 명시했다. | 235–268 |
| [SwanInterpolateAc.ftn90.md](../swan/src/SwanInterpolateAc.ftn90.md):270–296 | ivc(1) 대입과 장애물 플래그·영 가중치의 인용이 빠졌다. | [보완] ivc(1)=k와 플래그·가중치 대입을 원문으로 보완했다. | 272–280 |
| [SwanInterpolateOutput.ftn90.md](../swan/src/SwanInterpolateOutput.ftn90.md):65–126 | ient 초기값 인용이 빠졌다. | [보완] 초기값 선언을 인용했다. | 79 |
| [SwanInterpolateOutput.ftn90.md](../swan/src/SwanInterpolateOutput.ftn90.md):127–174 | 직접 복사·예외값·꼭짓점 번호·셀 발견 플래그의 대입식을 축약했다. | [보완] 포인터 연결과 각 대입을 인용했다. RETURN과 CYCLE의 실행 순서를 명시했다. | 130–173 |
| [SwanInterpolateOutput.ftn90.md](../swan/src/SwanInterpolateOutput.ftn90.md):175–225 | 셀·면 방향·초기값·경고 메시지 작성식을 축약했다. | [보완] 해당 대입과 좌표 오프셋을 포함한 WRITE를 인용했다. EXIT와 CYCLE의 대상을 명시했다. | 181–225 |
| [SwanInterpolateOutput.ftn90.md](../swan/src/SwanInterpolateOutput.ftn90.md):226–249 | 꼭짓점 좌표와 교차 플래그 대입을 생략했다. | [보완] 세 대입식을 인용했다. | 234–236 |
| [SwanInterpolateOutput.ftn90.md](../swan/src/SwanInterpolateOutput.ftn90.md):250–286 | 장애물 수·좌표·포인터 갱신과 조건 종료를 축약했다. | [보완] 각 대입과 연결을 인용했다. 장애물 조건이 285행에서 닫힘을 명시했다. | 252–285 |
| [SwanInterpolateOutput.ftn90.md](../swan/src/SwanInterpolateOutput.ftn90.md):287–317 | ivc(1)·플래그·영 가중치 인용과 바깥 활성 조건 종료가 빠졌다. | [보완] 누락 대입을 인용했다. 활성 조건에 ELSE가 없음을 명시했다. 조건과 점 루프의 종료를 대응시켰다. | 289–312 |
| [SwanInterpolatePoint.ftn90.md](../swan/src/SwanInterpolatePoint.ftn90.md):56–106 | ient 초기값 인용이 빠졌다. | [보완] 초기값 선언을 인용했다. | 67 |
| [SwanInterpolatePoint.ftn90.md](../swan/src/SwanInterpolatePoint.ftn90.md):107–151 | 초기값·일치 분기 대입과 미발견 메시지를 축약했다. | [보완] 포인터 연결과 대입식을 인용했다. 실제 WRITE·msgerr·RETURN 순서를 명시했다. | 111–148 |
| [SwanInterpolatePoint.ftn90.md](../swan/src/SwanInterpolatePoint.ftn90.md):152–200 | 셀·꼭짓점·방향·기본값 대입과 미발견 오류 처리를 축약했다. | [보완] 각 대입을 인용했다. 메시지 작성·msgerr·RETURN의 순서를 명시했다. | 156–200 |
| [SwanInterpolatePoint.ftn90.md](../swan/src/SwanInterpolatePoint.ftn90.md):201–233 | 꼭짓점 스칼라·무게중심·면적 대입을 생략했다. | [보완] 각 대입식을 원문으로 인용했다. | 204–216 |
| [SwanIntgratSpc.ftn90.md](../swan/src/SwanIntgratSpc.ftn90.md):55–101 | ient 초기값의 인용과 wpar의 구체적 의미가 빠졌다. | [보완] 초기값 선언을 인용했다. wpar의 파수·군속도 의미를 명시했다. | 73·78 |
| [SwanIntgratSpc.ftn90.md](../swan/src/SwanIntgratSpc.ftn90.md):102–148 | 상·하한 초과 검사를 경계 교차라고 설명했다. 초기 모멘트·영 계수의 인용이 빠졌다. | [정정·보완] 실제로 검사하는 현재 주파수의 초과 조건과 분기 순서를 명시했다. pmom·cia·cib의 영 대입을 인용했다. | 106·119–134 |
| [SwanIntgratSpc.ftn90.md](../swan/src/SwanIntgratSpc.ftn90.md):149–183 | fmax > 100을 상한을 무한대로 취급한다고 단정했다. 오류 메시지와 반환값 인용이 빠졌다. | [정정·보완] 확인 가능한 ctail=0 대입으로 고쳤다. msgerr·오류 반환값·RETURN을 인용했다. 바깥 조건 종료를 대응시켰다. | 155–182 |
| [SwanIntgratSpc.ftn90.md](../swan/src/SwanIntgratSpc.ftn90.md):184–231 | 상·하한 초과 검사를 경계 교차라고 설명했다. 영 계수 인용이 빠졌다. | [정정·보완] 현재 주파수의 초과 조건과 분기 순서를 명시했다. cia·cib의 영 대입을 인용했다. | 202–219 |
| [SwanIntgratSpc.ftn90.md](../swan/src/SwanIntgratSpc.ftn90.md):264–306 | 상·하한 초과 검사를 경계 교차라고 설명했다. 영 계수 인용이 빠졌다. | [정정·보완] 현재 주파수의 초과 조건과 분기 순서를 명시했다. cia·cib의 영 대입을 인용했다. | 275–292 |
| [SwanIntgratSpc.ftn90.md](../swan/src/SwanIntgratSpc.ftn90.md):307–348 | 두 IF·ELSEIF 사슬의 ELSE 부재와 조건별 종료 위치를 생략했다. 반환 대입식 인용이 빠졌다. | [보완] 두 사슬 모두 ELSE가 없음을 명시했다. 각 ENDIF를 시작 조건과 대응시켰다. 반환값 대입을 인용했다. | 321–348 |
| [SwanIntgratSpc.ftn90.md](../swan/src/SwanIntgratSpc.ftn90.md):코드 사실 114–129·197–214·270–287 | 상·하한 초과 조건을 경계 교차 조건이라고 설명했다. | [정정] 실제 검사인 현재 주파수 초과와 ELSEIF 순서를 명시했다. 왼쪽 끝에 대한 상한 검사가 없음을 구분했다. | 114–129·197–214·270–287 |

수정된 기록의 frontmatter는 작업 전 값과 같다.
각 기록의 구간 경계는 작업 전 값과 같다.
원문 8개의 SHA-256은 작업 전 값과 같다.
조건·대입식의 백틱 인용을 해당 구간 원문과 대조했다.
단일 행 번호가 붙은 실행문·초기값 인용을 해당 원문 행과 대조했다.
수정 표지의 항목 수는 위 수정 목록과 일치한다.
모델을 실행하지 않았다.
git을 조작하지 않았다.

정정 9, 보완 57, 이상 없음 45
