---
file: models/SWASH/raw/source_code/swash/src/m_parall.ftn
lines: 199
sha256: 6dad9e280699b075418020be654205a56ba0db341834037c8d33ed568679ff26
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# m_parall.ftn — 판독 구간 기록

구간은 1행부터 199행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–53 | `MODULE M_PARALL` 시작(1). 소속·작성자 머리말(4–11), 비정수압 파랑·흐름 모델(non-hydrostatic wave-flow model)이라는 설명과 2010–2026 저작권(14–15), GPL 3 이상·무보증 안내(17–28)를 포함한다. 작성자·2003년과 2004년 변경 이력(31–39)을 적는다. 목적 주석은 메시지 전달 인터페이스(Message Passing Interface, MPI)를 이용하는 분산 메모리(distributed memory) 병렬 처리 데이터라고 설명한다(41–44). 방법·사용 모듈 항목은 `---`이다(46–52). |
| 54–90 | 시작 시 1행 M_PARALL 모듈 안. `IMPLICIT NONE`(54), 인수 없음이라는 주석(56–58), 주 프로세스 순위(rank)와 겹침 영역(halo area) 폭을 선언한다(60–67). 고정 매개변수 원문은 `PARAMETER (MASTER = 1,` (68), `     &           IHALOX = 3, IHALOY = 3)` (69)이다. MASTER는 1이고 x·y 방향 겹침 폭은 각각 3이다. INODE·NPROC, 문자·정수·실수·배정밀도 MPI 자료형 SWCHAR/SWINT/SWREAL/SWDBLE, 집합 연산(collective operation) SWMAX/SWMIN/SWSUM, 병렬 실행 표시 PARLL을 주석으로 설명하고 선언한다(71–89). 주석의 PARLL 의미는 참이면 병렬 실행이고 거짓이면 병렬 실행이 아니다(77). 이 구간에는 해당 변수의 초기값 대입이 없다. |
| 91–125 | 시작 시 1행 M_PARALL 모듈 안. 전역 영역(global domain)과 부분 영역(subdomain)의 데이터 설명 주석이다. DWRKEX는 인접 영역 송수신 배정밀도 작업 배열이다(93). IBLKAD의 1번 위치는 이웃 수 m이고, `3*i-1`·`3*i`·`3*i+1` 위치는 이웃 번호·방향·뒤쪽 배열 포인터이다(94–102). `3*m+2`는 겹치는 미지수 수이며 `3*m+3 ... 3*m+2+n`과 `3*m+3+n ... 3*m+2*n+2`는 송신·수신 미지수 위치라는 주석이다(103–108). IMRGE의 0은 파일 병합 안 함이고 1은 병합 후 개별 파일 삭제이다(109–112). INCORN·IWEIG·IWRKEX·KGRPGL의 의미를 설명한다(113–119). KGRPGL은 1이면 비활성 격자점이고 1보다 크면 활성 격자점이다(117–119). KPART 주석은 −1일 때 `!               =-1; automatically setting based on computation mode` (121)에 따라 계산 모드를 기준으로 자동 선택한다. 나머지 KPART 값은 1 띠 분할(stripwise partitioning), 2 직교 재귀 이분할(orthogonal recursive bisection, ORB), 3 x축 띠 분할, 4 y축 띠 분할이라고 적는다(120–125). 이 값들은 설명 주석이며 기본값을 대입하는 실행문이 아니다. [10-15 전수 검증 보완] |
| 126–171 | 시작 시 1행 M_PARALL 모듈 안. LMXF/LMXL/LMYF/LMYL은 부분 영역 첫·끝 인덱스가 전역 영역 첫·끝 인덱스와 같은지 표시한다는 주석이다(126–133). LORB는 참이면 ORB이고 거짓이면 띠 분할이라는 주석이다(134–136). 전역 젖은 격자점 수 MCGRDGL, 전역 x·y 격자점 수 MXCGL/MYCGL, 전역 기준 부분 영역 인덱스 MXF/MXL/MYF/MYL, 경계점 수 NBGGL, 송수신 WRKEXG, 부분 영역 좌표 극값, 전역 좌표 XGRDGL/YGRDGL을 설명한다(137–153). 스칼라 정수·실수·논리 변수를 선언한다(155–162). SAVE·ALLOCATABLE 배열 IBLKAD/IWEIG/IWRKEX/KGRPGL, XGRDGL/YGRDGL, WRKEXG, REAL*8 DWRKEX, 논리 INCORN을 선언한다(164–171). 이 구간에는 배열 할당이나 값 대입이 없다. |
| 172–195 | 시작 시 1행 M_PARALL 모듈 안. 사용·호출 루틴, 오류 메시지, 비고, 구조 항목은 모두 `---` 주석이다(173–191). 원문 소스 항목 주석(193–194) 뒤 `END MODULE M_PARALL`(195)로 모듈을 닫는다. 이 모듈에는 CONTAINS나 루틴 호출 실행문이 없다. |
| 196–199 | 바깥 모듈이 닫힌 뒤의 스위치 표시 줄이다. 원문은 `!MPI!/impi` (196), `!MPI!/impi      MODULE MPI` (197), `!MPI!/impi      INCLUDE 'mpif.h'` (198), `!MPI!/impi      END MODULE MPI` (199)이다. switch.pl 58·64행은 줄 첫머리의 `!MPI`와 `!/impi`를 해당 스위치에서 순서대로 제거한다. 따라서 이 줄들은 `-mpi`와 `-impi`를 함께 적용할 때 MPI 모듈 선언·mpif.h 포함·모듈 종료 코드가 된다. 둘 중 하나만 적용하면 남은 표시가 주석을 유지한다. mpif.h 내용은 이 파일 판독 범위에 포함하지 않았다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 68–69: 주 프로세스 순위 MASTER는 1로 고정한다. x·y 방향 겹침 영역 폭 IHALOX/IHALOY는 각각 3으로 고정한다.
- 86–89·155–171: PARLL과 병렬 처리·영역 정보 스칼라 선언에는 초기값이 없다. 이 파일에는 해당 값을 초기화하는 실행문이나 ALLOCATABLE 배열을 할당하는 실행문이 없다. 다른 파일의 초기화는 확인하지 않았다.
