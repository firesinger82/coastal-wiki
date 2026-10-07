---
file: models/EFDC/raw/source_code/EFDC-GVC/welcome.for
lines: 109
sha256: b9b242fee742051ae0664ca4ca1bbe9b48631e571afdc52d94c2b841aad788fd
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# welcome.for — 판독 구간 기록

구간은 1행부터 109행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 주석·구분선(1–5), `SUBROUTINE WELCOME` (6). EFDC-FULL 1.0a와 2001년 11월 1일 마지막 수정이라는 머리말 주석(7–10). 변경 기록 빈 양식·구분 주석(11–20). |
| 21–50 | 시작 시 6행 WELCOME 루틴 안. 장치 6에 FORMAT 번호 100부터 128까지 순서대로 WRITE한다(21–49). 마지막 주석(50). 이 구간에는 조건 분기나 다른 루틴 호출이 없다. |
| 51–77 | 시작 시 6행 WELCOME 루틴 안. FORMAT 100의 빈 줄(51), FORMAT 101의 별표 테두리(52–53), FORMAT 102–103의 공백 내부(54–57). FORMAT 104–110은 EFDC 글자를 문자 그림으로 출력한다(58–71). FORMAT 111–113은 공백 내부를 출력한다(72–77). 테두리 및 본문 행의 들여쓰기는 5X이다. |
| 78–93 | 시작 시 6행 WELCOME 루틴 안. FORMAT 114–121은 TETRA TECH 문자 그림과 안내 문구를 출력한다(78–93). 안내 문구는 프로그램 이름(78–79), 개발자 JOHN M. HAMRICK(82–83), 유지·지원 주체 TETRA TECH,INC.(86–87), RELEASE DATE: 14 JUNE 2007(90–91)이다. 이 문구는 FORMAT의 고정 문자열이다. |
| 94–106 | 시작 시 6행 WELCOME 루틴 안. FORMAT 122–123은 공백 내부(94–97). FORMAT 124–125는 EFDC와 프로그램 이름이 JOHN M. HAMRICK의 상표라는 고정 안내 문구이다(98–101). FORMAT 126은 공백 내부(102–103), FORMAT 127은 아래 테두리(104–105), FORMAT 128은 두 줄 구분(106). |
| 107–109 | 시작 시 6행 WELCOME 루틴 안. 주석(107), RETURN(108), END(109). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10·90–91: 머리말의 마지막 수정 날짜는 2001년 11월 1일이다. 배너의 고정 RELEASE DATE 문자열은 2007년 6월 14일이다.
