---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/get_env.F
lines: 167
sha256: 4882b23437e0916962e50af0949a38574be9f11e0cb148030673572f1b41fb49
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# get_env.F — 판독 구간 기록

구간은 1행부터 167행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | get_env_mod 시작(1), 저작권·MIT/X 라이선스 주석(3–8). Fortran 2003 내장 루틴(intrinsic routine) GET_ENVIRONMENT_VARIABLE로 환경 변수(environment variable)를 읽고 해석한다는 설명(10–11). Master/stdout 사용(15–16), implicit none(18), get_env 인터페이스는 정수 get_env_i·논리 get_env_l·문자열 get_env_s를 등록한다(22–26). CONTAINS·빈 주석(28–29). 이 파일에는 C 전처리기 지시행이 없다. |
| 30–53 | 시작 시 1행 모듈 안이며 열린 전처리 조건 없음. `get_env_i(name,value) RESULT(status)` 시작(30), 정수 해석 목적 주석(32–36). 출력 정수 value·입력 name(40–41), 지역 Lstr/status·길이 40 string·길이 512 msg 선언(45–47). 찾지 못하면 value=-1을 반환한다는 주석(49–52), 빈 주석 포함. |
| 54–78 | 시작 시 30행 get_env_i 안이며 열린 전처리 조건 없음. `GET_ENVIRONMENT_VARIABLE(name,string,Lstr,status)` 호출(54). `IF ((Lstr.gt.0).and.(status.eq.0)) THEN` (58) 안 `READ (string, *, IOSTAT=status, IOMSG=msg) value` (59)로 정수를 해석한다. `IF (Master.and.(status.ne.0)) THEN` (60)은 변환 오류 로그(61). 바깥 ELSE(63)는 `status=1` (64), `value=-1` (65), `IF (Master) THEN` (66)에서 미발견 로그(67). 조건 종료(69), 변환·미발견 FORMAT(71–74), 반환·함수 종료·빈 주석(75–78). |
| 79–105 | 시작 시 1행 모듈 안이며 열린 전처리 조건 없음. `get_env_l` 시작(79), 논리값 해석 설명(81–85). 출력 logical value·입력 name, 지역 Lstr/status 및 길이 40 string 선언(89–95). 미발견 시 .FALSE. 반환 주석(97–100), `GET_ENVIRONMENT_VARIABLE` 호출(102), 변환 머리말·빈 주석(104–105). |
| 106–120 | 시작 시 79행 get_env_l 안이며 열린 전처리 조건 없음. 기본값 `value=.FALSE.` (106). `IF ((Lstr.gt.0).and.(status.eq.0)) THEN` (108) 안 `IF ((string(1:1).eq.'0') .or.                                   &` (109), `     &      (string(1:1).eq.'F') .or.                                   &` (110), `     &      (string(1:1).eq.'f')) THEN` (111)이면 value=.FALSE.(112), ELSE(113)는 value=.TRUE.(114). 조건 종료·반환·함수 종료·빈 주석(115–120). 첫 글자만 판정하며 내장 호출의 status를 함수 결과로 반환한다. |
| 121–148 | 시작 시 1행 모듈 안이며 열린 전처리 조건 없음. `get_env_s` 시작(121), 문자열 환경 변수 설명(123–127). 입력 name·출력 value, 지역 Lstr1/Lstr2/status와 길이 1024 string 선언(131–137). 미발견 시 value=CHAR(32)를 반환한다는 주석(139–142). `GET_ENVIRONMENT_VARIABLE` 호출(144), `Lstr2=LEN(value)` (148)로 출력 문자열 길이를 구한다. 빈 주석 포함. |
| 149–167 | 시작 시 121행 get_env_s 안이며 열린 전처리 조건 없음. `IF (Lstr1.gt.Lstr2) THEN` (150)이면 `value=string(1:Lstr2)` (151)로 출력 길이에 맞춰 자르고, `IF (Master) THEN` (152)에서 name/string 및 요구·출력 길이를 로그한다(153). ELSE(155)는 `value=string(1:Lstr1)` (156). 조건 종료(157), 출력 길이 부족 FORMAT(159–162), 반환·함수 및 모듈 종료·빈 주석(163–167). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 58–69: get_env_i는 정수 READ의 status가 0이 아니면 Master에서 오류를 출력한다. READ 실패 분기에 value=-1을 설정하는 대입은 없다. value=-1은 환경 변수 판독 조건의 ELSE에서만 대입한다.
- 106–116: get_env_l은 문자열 첫 글자의 '0'·'F'·'f'만 .FALSE.로 판정한다. 나머지 비어 있지 않은 성공 판독 문자열은 .TRUE.로 설정한다. Fortran 논리값 READ는 사용하지 않는다.
- 136–156: get_env_s의 내부 문자열 길이는 1024로 고정되어 있다. 부분 문자열 범위는 Lstr1과 출력 value 길이 Lstr2의 비교로 결정한다. 이 블록에는 내부 string 길이 1024와 Lstr1을 비교하는 조건이 없다.
- 140–157: get_env_s의 주석은 미발견 시 value=CHAR(32)를 반환한다고 적는다. 실행 블록에는 status 조건 검사 또는 명시적인 CHAR(32) 대입이 없으며 내장 호출 뒤 길이에 따른 부분 문자열 대입만 있다.
