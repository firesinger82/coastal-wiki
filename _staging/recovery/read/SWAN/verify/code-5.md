# SWAN 판독 기록 전수 대조 — code-5

검증일은 2026-10-13이다.
각 기록의 구간 표 행을 frontmatter의 `file:` 원문과 의미까지 대조했다.
원문은 구간별로 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
한 번에 연 원문 구간의 최대 길이는 구간 경계에서 계산한 135행이다.
정정·보완·이상 없음의 집계 단위는 구간 표 한 행이다.

| 기록 | 대조한 구간 표 행 수 | 대조한 원문 행 수 | 정정 | 보완 | 이상 없음 |
|---|---:|---:|---:|---:|---:|
| [SwanParallel.ftn90.md](../swan/src/SwanParallel.ftn90.md) | 32 | 1746 | 0 | 12 | 20 |
| [SwanPointinMesh.ftn90.md](../swan/src/SwanPointinMesh.ftn90.md) | 4 | 127 | 0 | 0 | 4 |
| [SwanPrepComp.ftn90.md](../swan/src/SwanPrepComp.ftn90.md) | 3 | 94 | 1 | 0 | 2 |
| [SwanPrintGridInfo.ftn90.md](../swan/src/SwanPrintGridInfo.ftn90.md) | 5 | 177 | 2 | 1 | 2 |
| [SwanPropvelS.ftn90.md](../swan/src/SwanPropvelS.ftn90.md) | 8 | 335 | 4 | 2 | 2 |
| [SwanPropvelX.ftn90.md](../swan/src/SwanPropvelX.ftn90.md) | 4 | 116 | 0 | 0 | 4 |
| 합계 | 56 | 2595 | 7 | 15 | 34 |

원문 행은 해당 기록의 frontmatter `file:`를 기준으로 한다.
전처리 표시는 [switch.pl 82–105행](../../../../../models/SWAN/raw/source_code/swan/switch.pl#L82)으로 판정했다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| SwanParallel.ftn90.md:323–380 | 할당 실패 시 msgerr 수준 4 호출과 반환만 서술했다. | [보완] 오류 설명과 istat를 msgstr에 쓰는 문장을 추가했다. write와 return을 원문으로 인용했다. | 375–378 |
| SwanParallel.ftn90.md:381–424 | 고립 정점 오류 메시지와 반환을 요약했다. | [보완] msgstr에 정점 번호를 쓰는 write를 추가했다. 415행 ELSE가 402행 IF에 대응함을 명시했다. return을 인용했다. | 402–419 |
| SwanParallel.ftn90.md:425–483 | 역방향 항목 탐색과 최종 수준 4 오류만 요약했다. | [보완] 항목 발견 시 k 루프의 exit를 추가했다. 비대칭 정점 쌍 메시지 작성과 수준 1 보고 후 계속 검사함을 추가했다. | 433–449 |
| SwanParallel.ftn90.md:484–527 | Metis 함수 호출과 오류별 msgerr·반환만 설명했다. | [보완] 주석의 기본 옵션인 edge-cut 최소화와 C식 번호를 추가했다. 분기별 오류 설명을 msgstr에 쓰는 단계를 추가했다. 알 수 없는 오류에는 ierr가 포함됨을 명시했다. | 485–518 |
| SwanParallel.ftn90.md:682–746 | 보조 배열의 할당 실패 검사와 msgerr 인용만 있었다. | [보완] 오류 설명과 istat를 msgstr에 쓰는 단계와 반환을 추가했다. | 688–692 |
| SwanParallel.ftn90.md:932–977 | 연결 표 검색 불일치를 msgerr 수준 4와 반환으로 요약했다. | [보완] 지역·전체 정점 목록 손상 메시지를 msgstr에 쓰는 문장과 return을 추가했다. | 948–954 |
| SwanParallel.ftn90.md:978–1008 | 통신량과 소유 정점 수의 백분율을 요약했으나 계산식을 인용하지 않았다. | [보완] 수신 정점 수 합을 소유 정점 수로 나눈 뒤 100을 곱하는 출력문을 인용했다. | 989–1000 |
| SwanParallel.ftn90.md:1462–1517 | 전체 임시 배열의 할당 실패 검사만 요약했다. 1470행 반환이 빠졌다. | [보완] 할당 실패 메시지 전달과 루틴 반환을 명시했다. return을 인용했다. | 1468–1471 |
| SwanParallel.ftn90.md:1559–1602 | 각도·거리·순서 작업 배열의 할당 실패 검사만 적었다. | [보완] 할당 실패 시 msgerr 수준 4 호출 뒤 반환함을 명시했다. return을 인용했다. | 1585–1588 |
| SwanParallel.ftn90.md:1603–1656 | 시작 시 다각형 j 루프 안이라고 했으나 루프 종료 행이 빠졌다. | [보완] 1559행 j 루프는 1651행 enddo에서 닫힘을 추가했다. 전체 임시 배열 해제는 루프 밖임을 명시했다. | 1559·1649–1655 |
| SwanParallel.ftn90.md:1657–1708 | 주석의 복잡도 O(N log2 N)를 일반 텍스트로만 적었다. | [보완] 주석의 복잡도 식을 백틱으로 인용했다. 원문 행 1684를 붙였다. | 1684 |
| SwanParallel.ftn90.md:1709–1746 | 힙 구성과 반복 이동을 요약했으나 ip==1일 때 반환하는 동작이 빠졌다. | [보완] ip==1일 때 ia(1)을 채운 뒤 반환함을 추가했다. return과 두 go to를 원문으로 인용했다. | 1721–1724·1739–1742 |
| SwanPrepComp.ftn90.md:1–50 | 사용 모듈을 원문에 없는 통신 용도로 분류했다. | [정정] 원문에 있는 모듈명으로 고쳤다. m_obsta의 ONLY 대상이 OBSTDONE임을 명시했다. | 44–48 |
| SwanPrintGridInfo.ftn90.md:1–48 | ocpcomm4를 원문에 없는 통신 용도로 설명했다. | [정정] 사용 모듈을 ocpcomm4·SwanGriddata·SwanGridobjects로 명시했다. | 44–48 |
| SwanPrintGridInfo.ftn90.md:83–128 | 생성기별 설명 설정만 요약했다. 삼각형만 사용한다는 수량 제한과 ELSE의 기본 문자열이 빠졌다. | [보완] 각 분기의 helptxt 출력문을 인용했다. SMS/ADCIRC·Triangle·Easymesh에는 solely triangles를 설정함을 명시했다. ELSE에는 triangles or hybrid cells와 unknown을 설정함을 명시했다. | 83–109 |
| SwanPrintGridInfo.ftn90.md:129–163 | 격자 크기 계산을 세 높이의 역제곱 평균으로 요약했다. IF·ELSEIF의 배타성과 ELSE 부재를 명시하지 않았다. | [정정] 역제곱 평균의 제곱근에 대한 역수로 고쳤다. 최소 갱신 조건이 거짓일 때만 최대 갱신 조건을 검사함을 명시했다. ELSE가 없음을 명시했다. | 138–157 |
| SwanPropvelS.ftn90.md:1–77 | 수송 속도 제한 이력을 방향 속도 제한으로만 요약했다. 파수 공간 미분을 사용하는 대체 식의 추가 이력이 빠졌다. | [보완] 2009년 파수 공간 미분 기반 방향 수송 속도 대체 식의 추가 이력을 명시했다. 2012년 csigma와 ctheta 제한 옵션 추가 이력을 명시했다. | 53–57 |
| SwanPropvelS.ftn90.md:78–139 | cad·cas 출력과 삼각함수를 묶어 설명했다. 삼각함수 작업 배열의 제곱·곱 의미가 빠졌다. | [보완] cad가 theta 방향임을 명시했다. cas가 sigma 방향임을 명시했다. coscos·sincos·sinsin의 주석을 인용하여 제곱과 곱을 구별했다. | 83–84·88·102–103 |
| SwanPropvelS.ftn90.md:140–174 | cad·cas와 계수를 모두 초기화한 뒤 주파수 이동·굴절의 비활성 여부로 반환하는 순서로 설명했다. | [정정] cad·cas 초기화 뒤 154행 반환 조건을 검사하는 순서로 고쳤다. 계수 cd·cs는 반환하지 않았을 때 초기화함을 명시했다. ITFRE가 0이 아니어도 가능한 반환 조건을 명시했다. | 149–159 |
| SwanPropvelS.ftn90.md:215–239 | 방향 속도 성분과 기저 벡터의 절댓값 합이라고 설명했다. cas의 부호를 항상 유지한다고 단정했다. | [정정] 기저 벡터 성분 합과 공간 수송 속도의 곱에 절댓값을 적용함을 명시했다. 조건이 참일 때 cas*fac/abs(cas)로 대체하는 원문 연산으로 고쳤다. | 223–230 |
| SwanPropvelS.ftn90.md:240–276 | ELSE의 군속도/파수 계수에서 음의 부호를 빠뜨렸다. 회절 인자까지 더하는 항으로 요약했다. | [정정] ELSE 계수는 -cgo/kwave임을 명시했다. 회절 인자를 cad에 곱한 뒤 회절 경사 항을 반영하는 연산으로 고쳤다. 흐름 보정이 그 뒤임을 명시했다. | 248–275 |
| SwanPropvelS.ftn90.md:310–335 | 공간 속도와 기저 벡터의 절댓값 합이라고 설명했다. cad의 부호를 항상 유지한다고 단정했다. | [정정] 각 기저 벡터의 성분 합과 공간 속도를 곱한 후 절댓값을 적용하는 순서를 명시했다. cad*fac/abs(cad)로 대체하는 연산으로 고쳤다. 제한 분기와 굴절 분기의 종료 행을 구별했다. | 312–333 |

모든 대상 구간의 조건식과 계산식 인용을 원문 행 번호와 대조했다.
구간 경계는 변경하지 않았다.
frontmatter는 변경하지 않았다.
원문 여섯 파일의 SHA-256은 작업 시작 시 값과 일치한다.
SwanParallel 원문에서 센 `!MPI` 83행은 모두 기록에 `mpi=TRUE` 활성 조건이 적혀 있다.
다른 다섯 원문에는 해당 전처리 표시 행이 없다.
모델은 실행하지 않았다.

정정 7, 보완 15, 이상 없음 34
