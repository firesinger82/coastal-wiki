---
file: models/ADCIRC/raw/source_code/adcirc/util/inflate.F
lines: 221
sha256: 9d4786f14be60d49c8975254179c13439c0d98b6d27cb0c35271fc2bee2ee8a9
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# inflate.F — 판독 구간 기록

구간은 1행부터 221행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | ADCIRC 명칭·저작권·LGPL 3 이상·무보증 머리말과 구분 주석이다. |
| 20–44 | inflate 프로그램 시작(20). FEMA/LACPR의 특수 63/64/73/74 희소 형식(sparse format)을 전체 노드(node) 형식으로 복원하며 입력·출력 이름과 선택 인수를 받는다는 주석(22–27). implicit none과 길이 80 입력 줄, 길이 256 파일명·출력 버퍼·chunkify 인수, 길이 8 분할 파일명, 분할 카운터, 노드·자료 수, real*8 값 및 allocatable u/v를 선언한다(29–43). 빈 줄(44). |
| 45–81 | 시작 시 20행 inflate 프로그램 안. chunksOut=false 초기화(45). `if(COMMAND_ARGUMENT_COUNT().lt.2) then` (47)이면 사용법·STDIN/STDOUT·chunkify 설명 후 stop이다. GET_COMMAND_ARGUMENT로 입력·출력 이름을 받는다(57–58). `if ( COMMAND_ARGUMENT_COUNT().eq.3 ) call GET_COMMAND_ARGUMENT(3,chunkify)` (59). `if (chunkify.eq."chunkify") chunksOut = .true.` (61). `if(filefrom.eq."STDIN") then` (63)은 in=5이고 `else` (65)는 in=1로 입력 파일을 연다. `if(fileto.eq."STDOUT") then` (70)은 out=6이고 `else` (72)는 out=2이다. 그 안의 `if (chunksOut) then` (74)은 `chunkNum = 10` (75), `chunkFileName = "chunk.10"` (76)으로 첫 파일을 연다. `else` (78)는 fileto를 연다. |
| 82–107 | 시작 시 20행 inflate 프로그램 안. 제목 한 줄을 읽어 출력하고 nsnaps·nodes·dtdp·nspoolge·k를 읽는다(83–85). 자료 수가 hotstart 뒤 실제 개수와 다를 수 있다는 주석(87–88). countsnaps(nsnaps,in)을 호출한다(89). `if (chunksOut) then` (92) 안에서 `numSnapsPerChunk = nsnaps / 10;` (93)으로 정수 분할 크기를 구한다. 출력에 전체 nsnaps와 기존 헤더 값을 쓴다(97). u/v(nodes)를 할당한다(99–100). 자료 수를 믿지 않고 무한 루프로 읽는다는 주석(102–105). i=0·snapNum=1 초기화(106–107). |
| 108–134 | 시작 시 20행 inflate 프로그램 안. `if(k.eq.1) then` (108)의 `do` (109)에서 time·iter·np·default를 읽고 EOF이면 라벨 95로 이동한다(110). `if (chunksOut) then` (111), `if (snapNum.gt.numSnapsPerChunk) then` (112)이면 현재 출력을 닫고 chunkNum 증가·이름 끝 두 자리 쓰기·새 파일 열기·snapNum=1을 실행한다(113–117). time/iter를 출력한다(120). `do j=1,nodes` (121)은 u를 default로 채운다. `do j=1,np` (124)은 희소 노드 번호 nnum과 x를 읽어 u(nnum)에 복사한다. `do j=1,nodes` (128)은 전체 노드 번호와 u를 출력한다. i와 snapNum을 각각 1 증가시킨다(132–133). 무한 루프 종료(134). |
| 135–163 | 시작 시 20행 inflate 프로그램·108행 k 조건의 분기 경계. `else` (135)의 `do` (136)에서 time·iter·np·default를 읽는다. `if (chunksOut) then` (138), `if (snapNum.gt.numSnapsPerChunk) then` (139)은 출력 닫기·chunkNum 증가·새 파일 열기·snapNum=1을 실행한다(140–144). time/iter를 출력한다(147). `do j=1,nodes` (148)은 u/v 모두 default로 채운다. `do j=1,np` (152)은 nnum·x·y를 읽어 u/v(nnum)에 복사한다. `do j=1,nodes` (157)은 전체 노드 번호와 u/v를 출력한다. i만 증가시킨다(161). 루프·k 조건 종료(162–163). |
| 164–183 | 시작 시 20행 inflate 프로그램 안. 라벨 95와 처리 자료 수 출력(165–166). u/v 해제와 장치 1·2 닫기(167–170). 파일 번호 형식은 i2(172), 제목은 a80(173), 헤더는 정수 개수·E15.7 시간 간격 등(174), 자료 시각은 E20.10(175), 스칼라 값은 e15.8(176), 벡터 두 값은 e13.6(177)이다. 프로그램 종료·구분 주석·빈 줄(178–183). |
| 184–221 | countsnaps의 실제 자료 수 집계 목적·hotstart 뒤 헤더 개수 및 SMS 관련 주석(184–192). 루틴 입구와 nsnaps intent(out), in intent(in), 건너뛸 헤더·시각·노드 수·default·카운터 선언(193–202). nsnaps=0(204). `do` (205)에서 자료 헤더를 읽고 EOF이면 라벨 195로 이동한다(206). `do j=1,np` (207)에서 노드 줄을 건너뛴다. nsnaps를 증가시킨다(210). 집계 출력(213–214). rewind(in) 뒤 처음 두 줄을 다시 읽어 건너뛴다(215–217). return·루틴 종료·구분 주석(218–221). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32·59–61: chunkify 선언에는 초기값이 없다. 명령행 인수가 정확히 3개일 때만 chunkify를 읽는다. 문자열 비교는 그 조건 밖에 있다.
- 70–81·111–117·138–144: STDOUT 분기는 out=6만 설정한다. 분할 출력의 chunkNum·chunkFileName 초기화는 fileto가 STDOUT이 아닌 분기 안에 있다. 자료 루프의 분할 조건에는 STDOUT 제외 조건이 없다.
- 92–97: 분할 크기는 정수 nsnaps/10이다. 첫 출력 파일 헤더의 자료 수는 분할 크기가 아니라 전체 nsnaps이다.
- 83–97·113–117·140–144: 제목·파일 헤더 출력은 첫 파일을 연 뒤에 있다. 새 분할 파일을 여는 두 블록에는 제목·파일 헤더 출력문이 없다.
- 107·133·135–162: snapNum은 1로 시작한다. k=1 루프에는 snapNum 증가문이 있다. 벡터 루프에는 snapNum 증가문이 없다.
- 63–68·89·215–217: 입력이 STDIN이면 장치 5를 countsnaps에 전달한다. countsnaps는 전달받은 장치에 rewind를 실행한다.
- 124–126·152–155: 희소 입력의 nnum을 u/v 배열 인덱스로 직접 사용한다. 해당 블록에는 nnum의 1..nodes 범위 검사문이 없다.
- 75–76·115·142·172: 분할 파일 번호는 10에서 시작한다. 파일명의 7:8 위치를 i2 형식으로 갱신한다. 번호 자릿수를 늘리는 분기는 없다.
