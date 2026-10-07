---
file: models/SFINCS/raw/source_code/sfincs/source/src/sfincs_error.f90
lines: 52
sha256: 5c146930f461166c3e8b484663f23eac404ed902877f6b5fba34b795ae26a4dd
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# sfincs_error.f90 — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | `sfincs_error` 모듈 시작(1), sfincs_log 사용(3), contains(5). 사이의 주석 줄도 포함한다. |
| 7–19 | `stop_sfincs(message, error_code)`의 implicit none 및 intent(in) 정수·가변 길이 문자열 선언(7–12). 오류 접두어와 message를 logstr에 쓰고(14), `call write_log(logstr, 1)` (15), `stop error_code` (16)로 종료한다. 루틴 종료·주석(18–19). |
| 20–52 | `check_file_exists(file_name, file_type, stop_on_error) result(exists)`는 파일 존재 여부를 반환한다는 주석(20–24). sfincs_data 사용·implicit none(25–27). 입력 문자열은 가변 길이이고 message는 256자다(29–33). exists=true로 초기화한다(35). `inquire( file=trim(file_name), exist=exists)` (37)로 실제 존재 여부를 얻는다. `if (.not. exists) then` (39) 안의 `if (stop_on_error) then` (41)이면 파일 유형·이름과 파일 없음 메시지를 작성한다(43). `call stop_sfincs(trim(message), 2)` (44)로 종료 루틴을 호출한다. stop_on_error가 false이면 이 호출 없이 exists를 반환한다. 조건·함수·모듈 종료와 주석(46–52). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16·44: stop_sfincs는 전달받은 error_code를 STOP에 사용한다. check_file_exists의 파일 없음 종료 호출은 error_code를 2로 고정한다.
- 29–31·43: file_name과 file_type의 선언 길이는 가변이다. 오류 메시지 버퍼는 256자다. 이 함수에는 메시지 작성 전 입력 문자열 길이를 검사하는 조건문이 없다.
