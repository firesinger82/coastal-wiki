---
file: models/EFDC/raw/source_code/EFDC-GVC/rsmrst.for
lines: 76
sha256: eb1d35b195f2cadb4301b66b5de076b840835e4616780afc1ce3846d3309a725
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# rsmrst.for — 판독 구간 기록

구간은 1행부터 76행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | 머리말과 `SUBROUTINE RSMRST` (6). 버전·수정일·변경 이력 주석(10–21). 주석은 재시작 파일(restart file)의 초기조건을 INSMRST에서 읽는다고 적는다(26). EFDC.PAR·EFDC.CMN 포함(30–31), FEXIST 논리형·NN 정수·XTIME 실수 선언(32–34). 이진 파일(binary file)이 없으면 ASCII 파일을 사용한다는 주석(36–37). 포함 파일 내부는 판독하지 않았다. |
| 39–52 | 시작 시 6행 RSMRST 안. INQUIRE로 WQSDRST.BIN 존재 여부를 FEXIST에 받는다(39). `IF(.NOT. FEXIST)THEN` (40)이면 WQSDRST.INP를 단위 1·STATUS='UNKNOWN'으로 연다(41). 두 레코드를 건너뛴다(42–43). M=2..LA에서 파일의 L, NSMG개의 SMPON·SMPOP·SMPOC와 SM1NH4·SM2NH4·SM2NO3·SM2PO4·SM2H2S·SMPSI·SM2SI·SMBST·SMT를 자유 형식(list-directed)으로 직접 읽는다(45–50). 단위 1 CLOSE(52). |
| 53–70 | 시작 시 6행 RSMRST·40행 IF 블록 안. `ELSE` (53)는 이진 파일 존재 경로이다. WQSDRST.BIN을 단위 1·FORM='UNFORMATTED'·STATUS='UNKNOWN'으로 연다(55–56). ACCESS='TRANSPARENT' 대안은 주석(54). NN·XTIME을 읽고 XTIME=XTIME 자기 대입 후 단위 0에 로그를 쓴다(57–61). M=2..LA에서 먼저 L 레코드를 읽고 다음 레코드에서 ASCII 경로와 같은 배열·9개 SM 값을 읽는다(62–68). 단위 1 CLOSE·IF 종료(69–70). 값의 추가 계산은 없다. |
| 71–76 | 시작 시 6행 RSMRST 안이며 파일 선택 분기 밖. 주석과 `90 FORMAT(I5, 18E12.4)` (72), `999 FORMAT(1X)` (73). RETURN·END(75–76). 이 파일에는 서브루틴 CALL이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 39–56: 파일 선택은 WQSDRST.BIN 존재 여부만 검사한다. ASCII 파일을 별도로 INQUIRE하는 문장은 없고 두 OPEN 모두 STATUS='UNKNOWN'을 사용한다.
- 45–49·62–67: M은 판독 횟수를 제어한다. 배열 인덱스 L은 파일에서 읽으며 이 파일에는 L의 범위 검사나 M과 L의 일치 검사가 없다.
- 57–59: XTIME 판독 직후 실행문은 XTIME=XTIME 자기 대입이다. 이후 XTIME 사용은 로그 출력이다.
- 72: FORMAT 90이 선언되어 있다. 실제 ASCII READ는 자유 형식이며 이 파일에는 FORMAT 90을 사용하는 입출력문이 없다.
