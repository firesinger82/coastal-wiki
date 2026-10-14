# SWASH 판독 기록 전수 검증 — code-23

검증일은 2026-10-15이다.
대상 기록 9개의 구간 표 104행을 각 frontmatter의 `file:` 원문과 대조했다.
대조한 원문은 총 3,693행이다.
원문 행 수에는 주석과 빈 행을 포함했다.
구간 표 아래의 코드 사실 목록도 해당 원문 구간과 대조했다.

집계 단위는 구간 표의 데이터 행이다.
정정과 보완이 함께 있는 구간은 정정으로 집계했다.
보완은 정정 없이 누락만 채운 구간이다.
이상 없음은 수정하지 않은 구간이다.

| 기록 | 대조한 기록 행 | 대조한 원문 행 | 정정 | 보완 | 이상 없음 |
|---|---:|---:|---:|---:|---:|
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md) | 28 | 1138 | 0 | 26 | 2 |
| [SwashFloatObjects.ftn90.md](../swash/src/SwashFloatObjects.ftn90.md) | 13 | 493 | 0 | 11 | 2 |
| [SwashFlobjOutp.ftn90.md](../swash/src/SwashFlobjOutp.ftn90.md) | 7 | 204 | 0 | 2 | 5 |
| [SwashFlowDP.ftn90.md](../swash/src/SwashFlowDP.ftn90.md) | 9 | 308 | 0 | 6 | 3 |
| [SwashFlowUDP.ftn90.md](../swash/src/SwashFlowUDP.ftn90.md) | 6 | 172 | 0 | 3 | 3 |
| [SwashFlowdata.ftn90.md](../swash/src/SwashFlowdata.ftn90.md) | 12 | 386 | 3 | 6 | 3 |
| [SwashForcesRigidBod.ftn90.md](../swash/src/SwashForcesRigidBod.ftn90.md) | 10 | 350 | 0 | 7 | 3 |
| [SwashGeometrics.ftn90.md](../swash/src/SwashGeometrics.ftn90.md) | 11 | 334 | 0 | 8 | 3 |
| [SwashHDiffZplane1DH.ftn90.md](../swash/src/SwashHDiffZplane1DH.ftn90.md) | 8 | 308 | 0 | 6 | 2 |
| 합계 | 104 | 3693 | 3 | 75 | 26 |

각 구간은 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
한 번에 연 원문 구간은 모두 200행 이하이다.
구간 경계와 frontmatter는 최초 기록과 일치한다.
원문 9개의 SHA-256은 각 기록의 기존 `sha256:` 값과 일치한다.
단일 행 번호가 붙은 백틱 인용은 공백을 포함하여 해당 원문 행과 대조했다.
모델은 실행하지 않았다.

전처리 표시의 판정 기준은 `models/SWASH/raw/source_code/swash/switch.pl` 57–66행이다.
이 규칙은 해당 스위치 변수가 `TRUE`에 일치할 때 행 첫머리의 표시를 제거한다.
대상 원문 9개에는 이 규칙의 `!TIMG`, `!MPI`, `!F95`, `!DOS`, `!UNIX`, `!/Cray`, `!/SGI`, `!/impi`, `!CVIS`, `!MatL4`로 시작하는 행이 없다.

`SwashExpLayUtrans.ftn90` 754–757행은 바닥 난류운동에너지 주석과 `rtur(icell,kmax,1)`을 연결한다.
`SwashHDiffZplane1DH.ftn90` 105–108행은 보간점 위치를 z좌표로 정의한다.
같은 파일의 239–240행은 오른쪽 점의 높이가 더 크면 왼쪽 보간에 `k1 = k2 - 1`을 선택한다.
같은 파일의 258–259행은 왼쪽 점의 높이가 더 크면 오른쪽 보간에 `k1 = k2 - 1`을 선택한다.
대상 기록에서 층 방향을 거꾸로 설명한 문장은 발견하지 않았다.
층 번호의 방향을 직접 명시하지 않은 선언에는 방향 설명을 추정하여 추가하지 않았다.

아래 원문 행 번호는 각 기록의 `file:` 원문을 기준으로 한다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):1–79 | 이류 기법 선택과 r-ratio 정점 설명 누락 | [보완] 1차 풍상 또는 고차 기법과 가장 상류 정점 사용 주석 추가 | 53–54 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):158–191 | mlev 초기값을 말로만 기재 | [보완] 초기값과 면 길이 대입 및 루프 범위와 조건 종료 인용 | 168–190 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):192–246 | 초기값과 부호 대입식 인용 및 ELSE 부재 누락 | [보완] CFL 초기값과 유량 합 초기값 및 방향 부호를 인용하고 ELSE 부재 명시 | 192–245 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):247–297 | mtmax 기본값과 제한 대입식 및 메시지 내용 누락 | [보완] 초기화와 제한식 및 두 메시지 수준과 내용 인용; ELSE 부재 명시 | 249–296 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):298–330 | 건조점 행렬 초기값과 icistb 원문 인용 누락 | [보완] 행렬과 우변 초기화 및 성분 분기의 ELSE 부재 명시 | 300–329; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):331–366 | 외부 성분 루프와 부호 대입 및 ELSE 부재 인용 누락 | [보완] 성분 루프 범위와 부호 원문 및 ELSE 부재 추가 | 300; 333–365; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):367–400 | 바깥 조건식과 복귀 시간 초기화 원문 누락 | [보완] 활성 블록 조건과 종료 행 및 경계 농도 대입식 추가 | 300; 333–411; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):401–424 | 닫힌 경계 초기화와 외부 조건식 누락 | [보완] 닫힌 경계 대입식과 정확한 활성 블록 종료 행 추가 | 300; 333–417; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):425–460 | nc 초기값과 농도 복사 및 바깥 루프 범위 누락 | [보완] 초기식과 인덱스 저장 및 루프 종료 행 추가 | 300; 425–457; 1060; 1082; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):461–500 | 바깥 루프 범위와 수평 유량 계수 대입 인용 누락 | [보완] 루프 범위와 보간인자 및 거리 역수와 면적 대입식 추가 | 300; 425–497; 655; 1060; 1082; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):501–559 | 외부 내부면 조건과 평균 초기값 원문 누락 | [보완] 활성 조건식과 종료 행 및 정점 탐색과 평균 초기식 추가 | 300; 425–558; 609–655; 1060; 1082; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):560–610 | propsc와 유량 방향의 바깥 조건식 및 평균 초기값 누락. 바깥 유량 분기의 조건식과 범위 누락 | [보완] 두 바깥 조건식과 종료 행 및 평균 초기식 추가. 구간 첫 행이 유량 조건의 ELSE임을 명시 | 300; 425–655; 1060; 1082; 1131; 515; 560; 605 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):611–656 | 확산계수 대입식과 바깥 조건 및 최종 ELSE 부재 누락 | [보완] 확산계수 원문과 활성 블록 종료 및 ELSE 부재 추가 | 300; 425–655; 1060; 1082; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):657–685 | 바깥 루프와 대상 셀 루프 범위 원문 누락 | [보완] 활성 루프 종료 행과 대상 셀 인덱스 원문 추가 | 300; 425; 453; 659–682; 1060; 1082; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):686–736 | 기여 초기값과 방향 부호 및 ELSE 부재 누락 | [보완] 초기값과 부호 대입식 및 활성 루프 범위 추가 | 300; 425; 453; 686–735; 1060; 1082; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):737–772 | 바깥 루프 범위와 바닥층 주석 근거 누락 | [보완] 활성 루프 종료 행과 kmax 바닥층의 파일 내 근거 추가 | 300; 425; 453; 746–769; 1060; 1082; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):773–800 | 퇴적물 바깥 조건을 이름으로만 기재 | [보완] 퇴적물 조건식과 활성 루프 종료 행 추가 | 300; 425; 453; 739–804; 1060; 1082; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):801–833 | 퇴적물과 진흙 바깥 조건 및 kwu 초기값 원문 누락 | [보완] 활성 조건식과 종료 행 및 수직속도와 kwu 대입식 추가 | 300; 425; 453; 739–830; 1060; 1082; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):834–861 | 젖은 셀 바깥 조건식과 영 계수 원문 누락 | [보완] 활성 조건식과 종료 행 및 영 계수 대입식 인용 | 300; 425; 453; 813–860; 921–925; 1060; 1082; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):862–902 | 중앙차분 바깥 조건식과 w 분기의 ELSE 부재 누락. 바깥 중앙차분 분기의 조건식과 범위 누락 | [보완] 중앙차분 조건과 종료 행 및 w=0 보정 미실행 명시. 구간 첫 행이 중앙차분 조건의 ELSE임을 명시 | 300; 425; 453; 813–925; 1060; 1082; 1131; 834; 862; 901 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):903–928 | 젖은 셀 바깥 조건을 이름으로만 기재 | [보완] 활성 조건식과 모든 바깥 루프 종료 행 추가 | 300; 425; 453; 813; 819; 821; 921–925; 1060; 1082; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):929–983 | 바깥 루프 종료 행과 수직속도 및 영 계수 원문 누락 | [보완] 활성 루프 범위와 대입식 추가 | 300; 425; 453; 929–982; 1060; 1082; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):984–1028 | 양해 조건식과 개별 닫힘 및 대각 대입식 누락 | [보완] 블록별 종료 행과 양해 분기 밖의 풀이 범위 및 대입식 추가 | 300; 425; 453; 929–1027; 1060; 1082; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):1029–1061 | 중간해 인덱스 대입과 바깥 루프 범위 원문 누락 | [보완] n*maxsb 인덱스와 활성 루프 종료 행 추가 | 300; 425; 453; 1031–1060; 1082; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):1062–1110 | mass 초기값과 최종 농도 대입 인용 누락 | [보완] 초기식과 최종 저장식 및 질량 진단의 외부 블록 범위 추가 | 300; 425; 1064–1108; 1131 |
| [SwashExpLayUtrans.ftn90.md](../swash/src/SwashExpLayUtrans.ftn90.md):1111–1138 | 오류 메시지 원문과 바깥 루프 범위 누락 | [보완] 두 오류 메시지와 return 의미 및 성분 루프 종료 행 인용 | 300; 1124–1131 |
| [SwashFloatObjects.ftn90.md](../swash/src/SwashFloatObjects.ftn90.md):107–143 | 흘수 직접 복사식과 ELSE 부재 누락 | [보완] 복사식과 루프 범위 및 차원 조건 종료 행 추가 | 111–142; 216 |
| [SwashFloatObjects.ftn90.md](../swash/src/SwashFloatObjects.ftn90.md):144–193 | 바깥 oned 조건식과 직접 복사 및 ELSE 부재 누락 | [보완] 차원 조건의 원문과 종료 행 및 복사식 추가 | 111; 144–192; 216 |
| [SwashFloatObjects.ftn90.md](../swash/src/SwashFloatObjects.ftn90.md):194–228 | 바깥 차원 조건식과 가상점 복사식 누락 | [보완] oned 조건과 종료 행 및 경계값 복사식 추가 | 111; 144; 194–216 |
| [SwashFloatObjects.ftn90.md](../swash/src/SwashFloatObjects.ftn90.md):229–248 | u점 루프 범위와 차원 분기 종료 원문 누락 | [보완] 루프 원문과 차원 조건 종료 행 추가 | 229–247; 306 |
| [SwashFloatObjects.ftn90.md](../swash/src/SwashFloatObjects.ftn90.md):249–307 | 바깥 oned 조건과 루프 범위 원문 누락 | [보완] 차원 조건식과 종료 행 및 u점과 v점 루프 인용 | 229; 249–306 |
| [SwashFloatObjects.ftn90.md](../swash/src/SwashFloatObjects.ftn90.md):308–334 | 표지 초기값 원문과 ELSE 부재 누락 | [보완] lfbs 초기식과 ELSE 부재 추가 | 314–322 |
| [SwashFloatObjects.ftn90.md](../swash/src/SwashFloatObjects.ftn90.md):335–379 | 물성 초기값과 면적 대입식 원문 누락 | [보완] 다섯 초기식과 area 대입 및 조건 종료 행 추가 | 335–378; 437; 451 |
| [SwashFloatObjects.ftn90.md](../swash/src/SwashFloatObjects.ftn90.md):380–400 | 외부 이동 강체 조건과 차원 조건 원문 누락 | [보완] ifloat와 oned 조건 및 종료 행 추가 | 335; 343; 380–400; 437; 451 |
| [SwashFloatObjects.ftn90.md](../swash/src/SwashFloatObjects.ftn90.md):401–438 | 외부 조건식을 이름으로만 기재 | [보완] 이동 강체와 차원 조건 및 각 루프의 종료 행 추가 | 335; 343; 380; 392–393; 434–451 |
| [SwashFloatObjects.ftn90.md](../swash/src/SwashFloatObjects.ftn90.md):439–454 | 외부 이동 강체 조건식 누락 | [보완] ifloat 조건식과 종료 행 추가 | 335; 451 |
| [SwashFloatObjects.ftn90.md](../swash/src/SwashFloatObjects.ftn90.md):455–493 | 장력 영 초기값을 말로만 기재 | [보완] 분기별 영 초기식과 조건별 종료 행 추가 | 455–491 |
| [SwashFlobjOutp.ftn90.md](../swash/src/SwashFlobjOutp.ftn90.md):81–100 | 물체 수 대입과 ELSE 부재 누락 | [보완] nflob 분기별 대입식 인용 및 ELSE 부재 명시 | 85–89 |
| [SwashFlobjOutp.ftn90.md](../swash/src/SwashFlobjOutp.ftn90.md):101–129 | 출력 요청과 하중 복사식 및 ELSE 부재 누락 | [보완] 성분별 대입식 인용과 ELSE 부재 명시 | 103–128 |
| [SwashFlowDP.ftn90.md](../swash/src/SwashFlowDP.ftn90.md):87–128 | 이웃 인덱스와 직접 복사식 및 ELSE 부재 누락 | [보완] 계산식과 경계 복사식 및 차원 분기 범위 추가 | 87–127; 214 |
| [SwashFlowDP.ftn90.md](../swash/src/SwashFlowDP.ftn90.md):129–167 | 바깥 차원 조건과 이웃 인덱스 및 ELSE 부재 누락 | [보완] 조건식과 종료 행 및 직접 복사와 인덱스 계산식 추가 | 87; 129–167; 214 |
| [SwashFlowDP.ftn90.md](../swash/src/SwashFlowDP.ftn90.md):168–214 | 바깥 조건과 가상점 복사 및 건조점 영 초기식 누락 | [보완] 외부 블록 범위와 모든 경계 복사식 및 영 초기식 추가 | 87; 129; 133; 168–214 |
| [SwashFlowDP.ftn90.md](../swash/src/SwashFlowDP.ftn90.md):229–248 | 이웃 인덱스 계산식 인용 누락 | [보완] mu 계산식과 차원 조건 종료 행 추가 | 229–247; 306 |
| [SwashFlowDP.ftn90.md](../swash/src/SwashFlowDP.ftn90.md):249–269 | 바깥 차원 조건과 이웃 인덱스 원문 누락 | [보완] oned 조건과 종료 행 및 mu 계산식 추가 | 229; 249–268; 306 |
| [SwashFlowDP.ftn90.md](../swash/src/SwashFlowDP.ftn90.md):270–308 | 바깥 조건과 이웃 인덱스 및 영 초기값 원문 누락 | [보완] oned 조건과 nu 계산식 및 건조점 영 초기식 추가 | 229; 249; 270–306 |
| [SwashFlowUDP.ftn90.md](../swash/src/SwashFlowUDP.ftn90.md):96–123 | 외부 dpsopt 조건식과 직접 대입 인용 누락 | [보완] 조건식과 분기 종료 행 및 dps 대입식 추가 | 81; 114; 124; 170 |
| [SwashFlowUDP.ftn90.md](../swash/src/SwashFlowUDP.ftn90.md):124–146 | 바깥 dpsopt 조건식 누락 | [보완] 분기 사슬의 시작 조건과 종료 행 인용 | 81; 124; 170 |
| [SwashFlowUDP.ftn90.md](../swash/src/SwashFlowUDP.ftn90.md):147–172 | 바깥 분기의 조건식과 경계면 직접 복사식 누락 | [보완] dpsopt 분기의 범위와 복사식 추가 | 81; 124; 160–170 |
| [SwashFlowdata.ftn90.md](../swash/src/SwashFlowdata.ftn90.md):58–78 | 인덱스 주석의 +1 관계와 경계값 원문 인용 누락 | [보완] 선언 주석의 인덱스 관계와 값 인용 | 58–77 |
| [SwashFlowdata.ftn90.md](../swash/src/SwashFlowdata.ftn90.md):79–129 | ibb 아래쪽 경계와 음수 부호 대응 및 유효 3D점 설명 누락 | [보완] 경계 위치와 -ibb 주석 및 uwetp와 vwetp의 유효점 의미 추가 | 82; 92; 111–116 |
| [SwashFlowdata.ftn90.md](../swash/src/SwashFlowdata.ftn90.md):130–164 | 인접점 위치와 수직항 삼중대각 및 Poisson 의미 생략 | [보완] 계수별 정확한 위치와 행렬의 방정식 역할 추가 | 131; 135; 137; 139–140; 154–163 |
| [SwashFlowdata.ftn90.md](../swash/src/SwashFlowdata.ftn90.md):201–225 | flux를 구조 격자용으로 단정. 압력 보정 배열의 차원과 격자 구분 생략 | [정정·보완] 원문에 있는 셀 면 총유량으로 한정. 각 보정 배열의 1DH와 2DH 및 세밀 격자와 층평균 역할 추가 | 214–215; 202–206 |
| [SwashFlowdata.ftn90.md](../swash/src/SwashFlowdata.ftn90.md):226–257 | hks와 hs 주석에 없는 현재 시간 수준을 단정 | [정정] 시간 수준이 없는 선언과 새 시간 및 옛 시간 선언을 구분 | 226–229; 243–244 |
| [SwashFlowdata.ftn90.md](../swash/src/SwashFlowdata.ftn90.md):258–291 | pfac 값 원문과 qbot 및 qv의 비정수압 한정 생략 | [보완] 거리 계수 주석 인용과 압력 유형 및 qm의 1DH 범위 추가 | 269–279 |
| [SwashFlowdata.ftn90.md](../swash/src/SwashFlowdata.ftn90.md):292–322 | 레이놀즈 응력 주석식을 음의 곱으로만 요약 | [보완] 아홉 성분 식의 부호와 변수 순서 인용 및 시간 수준 구분 추가 | 293–305; 319–322 |
| [SwashFlowdata.ftn90.md](../swash/src/SwashFlowdata.ftn90.md):323–344 | vnu2d 위치별 계산 차원 대응 생략 | [보완] 2DH 수심점과 1DH 수위점 및 비구조 셀 면 대응 추가 | 343 |
| [SwashFlowdata.ftn90.md](../swash/src/SwashFlowdata.ftn90.md):345–370 | zks 주석에 없는 현재 시간 수준을 단정 | [정정] 시간 수준이 없는 zks와 새 및 옛 시간 배열을 구분 | 360–362 |
| [SwashForcesRigidBod.ftn90.md](../swash/src/SwashForcesRigidBod.ftn90.md):101–156 | 초기 부착점과 회전점 복사식 원문 누락 | [보완] 벡터 초기화와 저장식 및 물체 루프 종료 행 추가 | 101–119; 256 |
| [SwashForcesRigidBod.ftn90.md](../swash/src/SwashForcesRigidBod.ftn90.md):157–209 | 방충재 영 초기식과 바깥 루프 및 소운동 근사의 한정 누락 | [보완] 대입식과 루프 종료 행 및 주석의 불확실성 보존 | 101; 163–208; 256 |
| [SwashForcesRigidBod.ftn90.md](../swash/src/SwashForcesRigidBod.ftn90.md):210–224 | 힘 영 초기식과 외부 루프 범위 원문 누락 | [보완] 초기식 인용 및 물체 루프 종료 행 추가 | 101; 214; 256 |
| [SwashForcesRigidBod.ftn90.md](../swash/src/SwashForcesRigidBod.ftn90.md):225–256 | 세 토크 영 초기값과 루프 범위 원문 누락 | [보완] 초기식과 합산 루프 및 외부 루프 종료 행 인용 | 101; 227–256 |
| [SwashForcesRigidBod.ftn90.md](../swash/src/SwashForcesRigidBod.ftn90.md):278–295 | PTO 동력 초기값을 말로만 기재 | [보완] ptop 영 초기식 원문 인용 | 284 |
| [SwashForcesRigidBod.ftn90.md](../swash/src/SwashForcesRigidBod.ftn90.md):296–321 | x회전행렬 상수 성분과 각도 대응 원문 누락 | [보완] 모든 0과 1 대입식 및 각도와 방향 주석 추가 | 300–320 |
| [SwashForcesRigidBod.ftn90.md](../swash/src/SwashForcesRigidBod.ftn90.md):322–350 | y와 z 회전행렬의 상수 성분을 말로만 기재 | [보완] 모든 0과 1 대입식 원문 인용 | 322–340 |
| [SwashGeometrics.ftn90.md](../swash/src/SwashGeometrics.ftn90.md):93–132 | 바깥 optg 조건식과 coslat 기본값 및 경계 복사식 누락. myc-1 경계 내부점 인덱스를 말로만 기재 | [보완] 조건식과 종료 행 및 계수와 경계 대입식 인용. 포인터 대입식 원문 추가 | 76; 93–132; 170; 314; 127 |
| [SwashGeometrics.ftn90.md](../swash/src/SwashGeometrics.ftn90.md):133–169 | 바깥 optg 조건식과 coslat 기본값 및 경계 복사식 누락. mxc-1 경계 내부점 인덱스를 말로만 기재 | [보완] 조건식과 종료 행 및 기본값과 경계 대입식 인용. 포인터 대입식 원문 추가 | 76; 133–169; 314; 164 |
| [SwashGeometrics.ftn90.md](../swash/src/SwashGeometrics.ftn90.md):170–199 | 바깥 optg 조건을 이름으로만 기재 | [보완] 조건식과 종료 행 및 iy 루프 종료 행 추가 | 76; 174; 199; 227; 314 |
| [SwashGeometrics.ftn90.md](../swash/src/SwashGeometrics.ftn90.md):200–242 | 바깥 optg 조건과 경계 복사식 누락. myc-1 경계 내부점 인덱스를 말로만 기재 | [보완] 활성 블록 조건과 종료 행 및 복사 대입식 추가. 포인터 대입식 원문 추가 | 76; 170; 174; 227–241; 314; 237 |
| [SwashGeometrics.ftn90.md](../swash/src/SwashGeometrics.ftn90.md):243–270 | 바깥 optg 조건식 누락 | [보완] 조건식과 종료 행 및 ix 루프 종료 행 추가 | 76; 170; 245; 298; 314 |
| [SwashGeometrics.ftn90.md](../swash/src/SwashGeometrics.ftn90.md):271–299 | 바깥 optg 조건식과 ix 루프 범위 인용 누락 | [보완] 활성 조건과 루프 원문 및 종료 행 추가 | 76; 170; 245; 298; 314 |
| [SwashGeometrics.ftn90.md](../swash/src/SwashGeometrics.ftn90.md):300–315 | 바깥 optg 조건식과 경계 복사식 누락. mxc-1 경계 내부점 인덱스를 말로만 기재 | [보완] 조건식과 종료 행 및 복사식 원문 추가. 포인터 대입식 원문 추가 | 76; 170; 300–314; 308 |
| [SwashGeometrics.ftn90.md](../swash/src/SwashGeometrics.ftn90.md):316–334 | 하측과 좌측 포인터의 인덱스식을 말로만 기재 | [보완] iy-1과 ix-1 포인터 대입식 원문 추가 | 321–322 |
| [SwashHDiffZplane1DH.ftn90.md](../swash/src/SwashHDiffZplane1DH.ftn90.md):114–164 | 확산계수 초기식과 제한식 및 이웃 인덱스 인용 누락 | [보완] 계수 대입식과 icistb 증가식 및 루프 종료 행 추가 | 131–163; 306 |
| [SwashHDiffZplane1DH.ftn90.md](../swash/src/SwashHDiffZplane1DH.ftn90.md):165–197 | 층 병합 인덱스 초기화와 증가식 및 높이 저장식 누락 | [보완] 분기별 인덱스 계산과 저장식 및 goto 도착점 인용 | 131; 165–196; 304–306 |
| [SwashHDiffZplane1DH.ftn90.md](../swash/src/SwashHDiffZplane1DH.ftn90.md):198–226 | 바깥 수심 조건과 층 검색 초기값 및 인덱스 저장식 누락 | [보완] 조건과 종료 행 및 검색 인덱스 대입식 추가 | 131; 165; 206–225; 304–306 |
| [SwashHDiffZplane1DH.ftn90.md](../swash/src/SwashHDiffZplane1DH.ftn90.md):227–254 | 바깥 수심 조건과 보간층 인덱스 및 경계 복사식 누락 | [보완] 조건과 종료 행 및 k2±1 계산식과 경계 복사식 추가 | 131; 165; 229–253; 300–306 |
| [SwashHDiffZplane1DH.ftn90.md](../swash/src/SwashHDiffZplane1DH.ftn90.md):255–273 | 바깥 수심 및 유효 층 조건식과 보간 인덱스 원문 누락 | [보완] 활성 조건과 종료 행 및 k2±1과 경계 복사식 추가 | 131; 165; 229; 234; 257–272; 300–306 |
| [SwashHDiffZplane1DH.ftn90.md](../swash/src/SwashHDiffZplane1DH.ftn90.md):274–308 | 바깥 수심 및 유효 층 조건식과 grad 초기식 누락 | [보완] 조건식과 개별 종료 행 및 grad 영 초기값 인용 | 131; 165; 229; 234; 280; 300–306 |

정정 3, 보완 75, 이상 없음 26
