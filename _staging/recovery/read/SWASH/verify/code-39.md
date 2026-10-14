# SWASH 판독 기록 전수 대조 — code-39

검증일은 2026-10-15다.
각 기록 frontmatter의 `file:`을 원문으로 사용했다.
각 구간을 `nl -ba <원문> | sed -n 'A,Bp'`로 열어 대조했다.
한 번에 연 원문 구간은 최대 104행이다.
구간 행 95개와 후속 사실 행 25개를 대조했다.
구간별 원문 행 수의 합은 3,579행이다.

다음 집계에서 정정과 보완은 표식 종류별 판독 행 수다.
두 표식이 있는 5행은 정정과 보완에 각각 포함했다.
이상 없음은 수정하지 않은 판독 행 수다.
`SwashLayUIntfaces`의 후속 사실란에 있는 `없음` 표시는 집계에서 제외했다.

| 기록 | 대조 원문 행 | 구간 행 수 | 후속 사실 행 수 | 정정 | 보완 | 두 표식 모두 | 이상 없음 |
|---|---:|---:|---:|---:|---:|---:|---:|
| [SwashInputField.ftn90.md](../swash/src/SwashInputField.ftn90.md) | 1–446 (446행) | 10 | 4 | 2 | 9 | 2 | 5 |
| [SwashInputGrid.ftn90.md](../swash/src/SwashInputGrid.ftn90.md) | 1–415 (415행) | 11 | 4 | 0 | 9 | 0 | 6 |
| [SwashIntWavgen.ftn90.md](../swash/src/SwashIntWavgen.ftn90.md) | 1–272 (272행) | 7 | 6 | 2 | 6 | 1 | 6 |
| [SwashKepsMod1DH.ftn90.md](../swash/src/SwashKepsMod1DH.ftn90.md) | 1–920 (920행) | 25 | 5 | 1 | 18 | 1 | 12 |
| [SwashKepsMod2DH.ftn90.md](../swash/src/SwashKepsMod2DH.ftn90.md) | 1–1212 (1212행) | 30 | 5 | 2 | 21 | 1 | 13 |
| [SwashLayUIntfaces.ftn90.md](../swash/src/SwashLayUIntfaces.ftn90.md) | 1–120 (120행) | 5 | 0 | 0 | 1 | 0 | 4 |
| [SwashLayerIntfaces.ftn90.md](../swash/src/SwashLayerIntfaces.ftn90.md) | 1–194 (194행) | 7 | 1 | 1 | 1 | 0 | 6 |
| 합계 | 3579행 | 95 | 25 | 8 | 65 | 5 | 52 |

각 기록의 frontmatter와 구간 경계는 변경하지 않았다.
원문 SHA-256은 7개 모두 기록의 값과 일치했다.
백틱 인용문에 표시된 단일 행 번호는 해당 원문 행과 일치했다.
조건문·반복문·대입문의 인용 누락 검사를 추가로 수행했다.
원문과 노트와 git은 변경하지 않았다.
모델은 실행하지 않았다.

`swash/switch.pl` 57–66행은 대응 스위치 변수가 `/TRUE/`에 일치하면 행 첫머리 표시를 제거한다.
대상 원문 7개에는 `!TIMG`, `!MPI`, `!F95`, `!DOS`, `!UNIX`, `!/Cray`, `!/SGI`, `!/impi`, `!CVIS`, `!MatL4` 표시 행이 없다.

`SwashKepsMod1DH`는 738행 자유수면 주석과 784행 바닥 주석 뒤에서 각각 접면 0과 kmax를 사용한다.
`SwashKepsMod2DH`는 1003행 자유수면 주석과 1053행 바닥 주석 뒤에서 각각 접면 0과 kmax를 사용한다.
`SwashLayUIntfaces` 44–46행과 `SwashLayerIntfaces` 46–48행은 k가 수면에서 아래로 증가한다고 설명한다.
두 접면 파일의 층 두께 식에서 1번 층은 접면 0과 1 사이에 있다.
`SwashInputField`, `SwashInputGrid`, `SwashIntWavgen`에는 층 인덱스의 상하 방향을 설명하는 주석이 없다.

아래 목록은 수정한 판독 행을 기록별로 나열한다.
후속 사실 행은 구간 앞에 `후속 사실`로 표시했다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [SwashInputField.ftn90.md:95–150](../swash/src/SwashInputField.ftn90.md) | 입력 종류별 번호와 상태를 요약으로만 기재했다. | **보완**. 초기값과 각 분기의 번호·상태 대입문을 인용했다. | 112–150 |
| [SwashInputField.ftn90.md:151–185](../swash/src/SwashInputField.ftn90.md) | 바깥 입력 종류 분기의 조건식이 없다. 번호와 상태 대입은 요약뿐이다. | **보완**. 바깥 조건식과 종료 행을 명시했다. 각 분기의 번호·상태 대입문을 인용했다. | 113, 152–184 |
| [SwashInputField.ftn90.md:186–232](../swash/src/SwashInputField.ftn90.md) | 벡터 상태·성분 매개변수 복사·ADCIRC 상태 대입을 요약했다. | **보완**. 해당 대입문을 원문대로 인용했다. | 195–198, 212–218, 228–229 |
| [SwashInputField.ftn90.md:233–280](../swash/src/SwashInputField.ftn90.md) | 끝 인덱스 좌표 복사를 오른쪽·위쪽 가상 좌표로 단정했다. 작업 배열 초기식은 요약뿐이다. | **정정·보완**. 복사할 인덱스를 명시했다. 층·좌표 반복 범위와 초기식을 인용했다. | 233–237, 273–279, 425 |
| [SwashInputField.ftn90.md:281–320](../swash/src/SwashInputField.ftn90.md) | 바깥 층 반복문과 저장 분기를 이름으로만 기재했다. | **보완**. 바깥 반복문·조건식과 종료 행을 명시했다. | 233, 246–346, 425 |
| [SwashInputField.ftn90.md:321–349](../swash/src/SwashInputField.ftn90.md) | 바깥 층 반복문과 저장 분기를 이름으로만 기재했다. | **보완**. 바깥 반복문·조건식과 종료 행을 명시했다. 최종 else가 없음을 적었다. | 233, 246–346, 425 |
| [SwashInputField.ftn90.md:350–393](../swash/src/SwashInputField.ftn90.md) | 끝 인덱스 복사를 가상 경계라고 단정했다. 바깥 반복문과 초기식이 인용되지 않았다. | **정정·보완**. 복사 인덱스를 명시했다. 반복문과 초기식을 인용했다. 최종 else 부재를 적었다. | 233, 353–354, 363–388, 425 |
| [SwashInputField.ftn90.md:394–425](../swash/src/SwashInputField.ftn90.md) | 바깥 반복문과 I/O 상태 초기식을 요약했다. 여러 블록의 종료를 묶어 적었다. | **보완**. 반복문·초기식을 인용했다. 각 조건의 종료 행을 구분했다. | 233, 394–425 |
| [SwashInputField.ftn90.md:426–446](../swash/src/SwashInputField.ftn90.md) | 시각·입력 상태·오류 경로 파일명 대입을 요약했다. | **보완**. 각 대입문을 원문대로 인용했다. | 431, 435, 442 |
| [SwashInputGrid.ftn90.md:149–182](../swash/src/SwashInputGrid.ftn90.md) | 곡선 격자 종류와 엇갈림 상태 대입을 요약했다. | **보완**. 격자 종류·엇갈림 상태 대입문을 인용했다. | 167, 171 |
| [SwashInputGrid.ftn90.md:183–209](../swash/src/SwashInputGrid.ftn90.md) | 바깥 격자 종류 분기의 조건식이 없다. 비정형 격자의 종류·크기 대입은 요약뿐이다. | **보완**. 바깥 조건식과 종료 행을 명시했다. 종류·크기 대입문을 인용했다. | 150, 200–207, 251 |
| [SwashInputGrid.ftn90.md:210–252](../swash/src/SwashInputGrid.ftn90.md) | 바깥 격자 종류 분기의 조건식이 없다. 1차원 격자 수 복구 대입은 요약뿐이다. | **보완**. 분기 사슬의 조건식·else·종료 행을 명시했다. 복구 대입문을 인용했다. | 150, 210, 240, 251 |
| [SwashInputGrid.ftn90.md:253–292](../swash/src/SwashInputGrid.ftn90.md) | 입력 상태·동적 상태·시각 복사를 요약했다. | **보완**. 해당 대입문을 원문대로 인용했다. | 260, 266, 277–284 |
| [SwashInputGrid.ftn90.md:293–316](../swash/src/SwashInputGrid.ftn90.md) | 잘못된 층 수를 1 또는 kmax로 바꾸는 식이 요약뿐이다. | **보완**. 두 복구 대입문을 인용했다. | 303, 307 |
| [SwashInputGrid.ftn90.md:317–355](../swash/src/SwashInputGrid.ftn90.md) | 출력 점 집합의 유형·길이 복사·초기값·점 수 대입은 요약뿐이다. | **보완**. 해당 대입문을 원문대로 인용했다. | 320–352 |
| [SwashInputGrid.ftn90.md:356–375](../swash/src/SwashInputGrid.ftn90.md) | 목록 연결과 상태 변경을 요약했다. | **보완**. 대입문과 포인터 연결문을 인용했다. | 368–373 |
| [SwashInputGrid.ftn90.md:376–393](../swash/src/SwashInputGrid.ftn90.md) | 계산 격자 종류가 다를 때 플래그 대입을 요약했다. | **보완**. 거짓 플래그 대입문을 인용했다. | 382 |
| [SwashInputGrid.ftn90.md:394–415](../swash/src/SwashInputGrid.ftn90.md) | 두 번째 성분의 좌표·격자 매개변수 복사를 요약했다. | **보완**. 복사 대입문을 인용했다. | 395–405 |
| [SwashIntWavgen.ftn90.md:97–116](../swash/src/SwashIntWavgen.ftn90.md) | 정수면 수심·배열 초기값·소멸 모드 수 초기값은 요약뿐이다. | **보완**. 해당 대입문을 원문대로 인용했다. | 101, 111–115 |
| [SwashIntWavgen.ftn90.md:117–157](../swash/src/SwashIntWavgen.ftn90.md) | 주석의 kd > 1 조건과 성분 복사·0 대입·파수 저장 인용이 빠졌다. | **보완**. 주석의 수량 조건과 각 대입문을 보완했다. 반복문·조건의 종료를 명시했다. | 117–156, 243 |
| [SwashIntWavgen.ftn90.md:158–183](../swash/src/SwashIntWavgen.ftn90.md) | 파수 자체를 보정한다고 서술했다. 바깥 반복문과 최종 else 부재가 빠졌다. | **정정·보완**. 보정 대상을 파향 theta로 바로잡았다. 반복문과 최종 else 부재를 명시했다. | 117, 158–182, 243 |
| [SwashIntWavgen.ftn90.md:184–216](../swash/src/SwashIntWavgen.ftn90.md) | 바깥 주파수 반복문을 이름으로만 적었다. | **보완**. 반복문 원문과 종료 행을 명시했다. | 117, 243 |
| [SwashIntWavgen.ftn90.md:217–244](../swash/src/SwashIntWavgen.ftn90.md) | 바깥 반복문과 저장 대입식이 인용되지 않았다. 소스 조건의 최종 else 부재는 구간 행에 없다. | **보완**. 반복문·저장 대입문을 인용했다. 조건 종료와 최종 else 부재를 명시했다. | 117, 219–243 |
| [SwashIntWavgen.ftn90.md:245–272](../swash/src/SwashIntWavgen.ftn90.md) | 경고 억제 플래그 대입과 차단 주파수의 Hz 환산식을 요약했다. | **보완**. 플래그 대입문과 omegcf/pi2를 포함하는 메시지 작성문을 인용했다. | 253, 264, 268 |
| [SwashIntWavgen.ftn90.md:후속 사실 128–144·186–241](../swash/src/SwashIntWavgen.ftn90.md) | 차단 주파수 초과만으로 진폭을 0으로 설정한다고 서술했다. | **정정**. numdisp 조건 안에서만 차단을 수행한다고 바로잡았다. | 126–134 |
| [SwashKepsMod1DH.ftn90.md:1–64](../swash/src/SwashKepsMod1DH.ftn90.md) | 주석의 시간 분할 차수·생성항 양적 처리·단계별 분리 방향을 빠뜨렸다. | **보완**. 각 수치 처리와 방향을 주석대로 보완했다. | 47–60 |
| [SwashKepsMod1DH.ftn90.md:288–326](../swash/src/SwashKepsMod1DH.ftn90.md) | 바깥 l 반복문을 이름으로만 적었다. | **보완**. 반복문 원문과 종료 행을 명시했다. | 255, 377 |
| [SwashKepsMod1DH.ftn90.md:327–358](../swash/src/SwashKepsMod1DH.ftn90.md) | 바깥 반복 조건을 참 분기로만 적었다. 두 반복문 원문과 종료 행이 없다. | **보완**. 바깥 조건식과 반복문 및 각각의 종료 행을 명시했다. | 255, 288, 296, 357–377 |
| [SwashKepsMod1DH.ftn90.md:359–378](../swash/src/SwashKepsMod1DH.ftn90.md) | 바깥 반복 조건식과 종료 행이 없다. 로그의 위치 인덱스 계산을 생략했다. | **보완**. 바깥 블록의 조건식·종료를 명시했다. minf+MXF-2를 포함하는 출력문을 인용했다. | 255, 288, 364–377 |
| [SwashKepsMod1DH.ftn90.md:401–444](../swash/src/SwashKepsMod1DH.ftn90.md) | 구간 시작의 바깥 반복문·수심 조건을 이름으로만 적었다. | **보완**. 바깥 반복문·조건식과 각각의 종료 행을 명시했다. | 386–405 |
| [SwashKepsMod1DH.ftn90.md:445–484](../swash/src/SwashKepsMod1DH.ftn90.md) | 바깥 l 반복문을 이름으로만 적었다. 층 방향의 주석 근거가 없다. | **보완**. 반복문 원문과 종료 행을 명시했다. 자유수면·바닥 주석으로 접면 방향을 확인했다. | 407, 738–804, 912 |
| [SwashKepsMod1DH.ftn90.md:485–511](../swash/src/SwashKepsMod1DH.ftn90.md) | 바깥 l 반복문을 이름으로만 적었다. | **보완**. 반복문 원문과 종료 행을 명시했다. | 407, 912 |
| [SwashKepsMod1DH.ftn90.md:512–545](../swash/src/SwashKepsMod1DH.ftn90.md) | 바깥 l 반복문과 l=1 분기를 이름으로만 적었다. | **보완**. 반복문·조건식·다음 분기와 종료 행을 명시했다. | 407, 487, 613, 736, 912 |
| [SwashKepsMod1DH.ftn90.md:546–575](../swash/src/SwashKepsMod1DH.ftn90.md) | 바깥 l 반복문과 l=1 분기를 이름으로만 적었다. | **보완**. 반복문·조건식·다음 분기와 종료 행을 명시했다. | 407, 487, 613, 736, 912 |
| [SwashKepsMod1DH.ftn90.md:576–612](../swash/src/SwashKepsMod1DH.ftn90.md) | 바깥 l 반복문과 l=1 분기를 이름으로만 적었다. | **보완**. 반복문·조건식·다음 분기와 종료 행을 명시했다. | 407, 487, 613, 736, 912 |
| [SwashKepsMod1DH.ftn90.md:613–639](../swash/src/SwashKepsMod1DH.ftn90.md) | 바깥 반복문과 l 분기 연결을 이름으로만 적었다. | **보완**. 바깥 반복문·시작 조건식·후속 조건식과 종료 행을 명시했다. | 407, 487, 613, 736, 912 |
| [SwashKepsMod1DH.ftn90.md:640–667](../swash/src/SwashKepsMod1DH.ftn90.md) | 바깥 반복문과 l=2 분기를 이름으로만 적었다. | **보완**. 바깥 반복문·분기 조건식과 종료 행을 명시했다. | 407, 487, 613, 736, 912 |
| [SwashKepsMod1DH.ftn90.md:668–697](../swash/src/SwashKepsMod1DH.ftn90.md) | 바깥 반복문과 l=2 분기를 이름으로만 적었다. | **보완**. 바깥 반복문·분기 조건식과 종료 행을 명시했다. | 407, 487, 613, 736, 912 |
| [SwashKepsMod1DH.ftn90.md:698–737](../swash/src/SwashKepsMod1DH.ftn90.md) | alpha·fac를 공극률 조건 안에서 계산한다고 서술했다. 바깥 블록과 최종 else 부재가 빠졌다. | **정정·보완**. alpha·fac는 반복문 앞의 계산으로 바로잡았다. 바깥 블록과 최종 else 부재를 명시했다. | 407, 487, 613, 698–736, 912 |
| [SwashKepsMod1DH.ftn90.md:738–782](../swash/src/SwashKepsMod1DH.ftn90.md) | 자유수면 계수 설명에서 하부 계수를 누락했다. 바깥 반복문과 최종 else 부재가 빠졌다. | **보완**. 상부 0·하부 -2를 구분했다. 바깥 반복문과 else의 소속을 명시했다. | 407, 738–782, 912 |
| [SwashKepsMod1DH.ftn90.md:783–850](../swash/src/SwashKepsMod1DH.ftn90.md) | 바깥 반복문 원문과 바닥 l 분기의 최종 else 부재가 빠졌다. | **보완**. 바깥 반복문·종료와 최종 else 부재를 명시했다. | 407, 786–849, 912 |
| [SwashKepsMod1DH.ftn90.md:851–878](../swash/src/SwashKepsMod1DH.ftn90.md) | 바깥 l 반복문을 이름으로만 적었다. | **보완**. 반복문 원문과 종료 행을 명시했다. | 407, 912 |
| [SwashKepsMod1DH.ftn90.md:879–912](../swash/src/SwashKepsMod1DH.ftn90.md) | 바깥 반복문 원문과 진단 위치 인덱스 계산이 빠졌다. | **보완**. 반복문·종료 행과 m+MXF-2를 포함하는 출력문을 인용했다. | 407, 900, 912 |
| [SwashKepsMod2DH.ftn90.md:1–65](../swash/src/SwashKepsMod2DH.ftn90.md) | 주석의 생성항 양적 처리와 단계별 분리 방향을 생략했다. | **보완**. 소멸항·생성항 처리와 수직 이류 차분·분리 방향을 보완했다. | 52–61 |
| [SwashKepsMod2DH.ftn90.md:325–361](../swash/src/SwashKepsMod2DH.ftn90.md) | rturmx를 난류량 최대값이라고만 설명했다. | **정정**. maxval(abs(...))의 절댓값 연산을 명시했다. | 355–356 |
| [SwashKepsMod2DH.ftn90.md:362–400](../swash/src/SwashKepsMod2DH.ftn90.md) | j = j + 1을 반복 횟수 초기화로 설명했다. 바깥 l 반복문을 이름으로만 적었다. | **정정·보완**. 반복 횟수 증가와 잔차·위치 초기화를 구분했다. 반복문 원문과 종료 행을 명시했다. | 364–369; 327, 571 |
| [SwashKepsMod2DH.ftn90.md:401–413](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 여섯 블록을 이름으로만 적었다. | **보완**. 각 반복문·조건식과 종료 행을 명시했다. | 327, 362–395, 409–412, 547–571 |
| [SwashKepsMod2DH.ftn90.md:414–456](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 l·k 반복문과 반복 조건을 이름으로만 적었다. | **보완**. 각 반복문·조건식과 종료 행을 명시했다. | 327, 362, 371, 547–571 |
| [SwashKepsMod2DH.ftn90.md:457–499](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 l·k 반복문과 반복 조건을 이름으로만 적었다. | **보완**. 각 반복문·조건식과 종료 행을 명시했다. | 327, 362, 371, 547–571 |
| [SwashKepsMod2DH.ftn90.md:500–548](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 l·k 반복문과 반복 조건을 이름으로만 적었다. | **보완**. 각 반복문·조건식과 종료 행을 명시했다. | 327, 362, 371, 547–571 |
| [SwashKepsMod2DH.ftn90.md:549–572](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 반복문·조건식과 진단 위치 인덱스 계산이 빠졌다. | **보완**. 바깥 블록·종료와 minf+MXF-2 및 ninf+MYF-2를 포함하는 출력문을 인용했다. | 327, 362, 554–571 |
| [SwashKepsMod2DH.ftn90.md:652–693](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 l 반복문을 이름으로만 적었다. 층 방향의 주석 근거가 없다. | **보완**. 반복문·종료 행을 명시했다. 자유수면·바닥 주석으로 접면 방향을 확인했다. | 612, 1003–1082, 1199 |
| [SwashKepsMod2DH.ftn90.md:694–722](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 l 반복문을 이름으로만 적었다. | **보완**. 반복문·종료 행을 명시했다. | 612, 1199 |
| [SwashKepsMod2DH.ftn90.md:723–758](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 반복문과 l=1 분기를 이름으로만 적었다. | **보완**. 반복문·조건식·다음 분기와 종료 행을 명시했다. | 612, 696, 850, 1001, 1199 |
| [SwashKepsMod2DH.ftn90.md:759–800](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 반복문과 l=1 분기를 이름으로만 적었다. | **보완**. 반복문·조건식·다음 분기와 종료 행을 명시했다. | 612, 696, 850, 1001, 1199 |
| [SwashKepsMod2DH.ftn90.md:801–849](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 반복문과 l=1·식생 조건을 이름으로만 적었다. | **보완**. 반복문·조건식·종료를 명시했다. 식생 조건과 다공성 조건을 구분했다. | 612, 696, 759–803, 850, 1001, 1199 |
| [SwashKepsMod2DH.ftn90.md:850–878](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 반복문과 l 분기 연결을 이름으로만 적었다. | **보완**. 반복문·시작 조건식·후속 조건식과 종료 행을 명시했다. | 612, 696, 850, 1001, 1199 |
| [SwashKepsMod2DH.ftn90.md:879–908](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 반복문과 l=2 분기를 이름으로만 적었다. | **보완**. 반복문·조건식과 종료 행을 명시했다. | 612, 696, 850, 1001, 1199 |
| [SwashKepsMod2DH.ftn90.md:909–952](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 반복문과 l=2 분기를 이름으로만 적었다. | **보완**. 반복문·조건식과 종료 행을 명시했다. | 612, 696, 850, 1001, 1199 |
| [SwashKepsMod2DH.ftn90.md:953–1002](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 반복문과 l=2 분기를 이름으로만 적었다. 최종 else 부재가 빠졌다. | **보완**. 반복문·조건식과 종료 행을 명시했다. 최종 else 부재를 적었다. | 612, 696, 850, 1001, 1199 |
| [SwashKepsMod2DH.ftn90.md:1003–1052](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 반복문 원문과 자유수면 l 분기의 최종 else 부재가 빠졌다. | **보완**. 바깥 반복문·종료와 else의 소속을 명시했다. | 612, 1005–1051, 1199 |
| [SwashKepsMod2DH.ftn90.md:1053–1106](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 l 반복문을 이름으로만 적었다. | **보완**. 반복문 원문과 종료 행을 명시했다. | 612, 1199 |
| [SwashKepsMod2DH.ftn90.md:1107–1131](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 반복문·경계 조건식과 최종 else 부재가 빠졌다. | **보완**. 반복문·경계 조건식·종료와 else의 소속을 명시했다. | 612, 1055–1130, 1199 |
| [SwashKepsMod2DH.ftn90.md:1132–1161](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 l 반복문을 이름으로만 적었다. | **보완**. 반복문 원문과 종료 행을 명시했다. | 612, 1199 |
| [SwashKepsMod2DH.ftn90.md:1162–1200](../swash/src/SwashKepsMod2DH.ftn90.md) | 바깥 반복문 원문과 진단 위치 인덱스 계산이 빠졌다. | **보완**. 반복문·종료 행과 m+MXF-2 및 n+MYF-2를 포함하는 출력문을 인용했다. | 612, 1186, 1199 |
| [SwashLayUIntfaces.ftn90.md:1–49](../swash/src/SwashLayUIntfaces.ftn90.md) | 아래로 증가하는 k 인덱스만 적었다. | **보완**. 접면 인덱스와 층 두께 인덱스를 구분했다. 1번 층이 최상층임을 명시했다. | 44–46, 72–82 |
| [SwashLayerIntfaces.ftn90.md:1–51](../swash/src/SwashLayerIntfaces.ftn90.md) | 아래로 증가하는 k 인덱스만 적었다. | **보완**. 접면 인덱스와 층 두께 인덱스를 구분했다. 1번 층이 최상층임을 명시했다. | 46–48, 76–86 |
| [SwashLayerIntfaces.ftn90.md:105–123](../swash/src/SwashLayerIntfaces.ftn90.md) | hku·hkum을 현재·이전 시간의 값으로 단정했다. | **정정**. 파일에 명시된 hu·hum과 접면 차의 대응으로 바로잡았다. | 105–120 |

정정 8, 보완 65, 이상 없음 52
