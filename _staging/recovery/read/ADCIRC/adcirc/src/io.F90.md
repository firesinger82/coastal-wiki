---
file: models/ADCIRC/raw/source_code/adcirc/src/io.F90
lines: 121
sha256: 06a1f2938502f57ac99c44e20d42e42921e60cb0dd548b6110ea98ad805eeecf
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# io.F90 — 판독 구간 기록

구간은 1행부터 121행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | ADCIRC 명칭·1994–2025 저작권·LGPL 3 이상·무보증 머리말(1–19). IO 모듈 구분 주석과 입출력(I/O) 유틸리티의 목적 문서(20–29). 주석은 파일 열기 오류 검사·존재 확인·표준 오류 처리를 제공한다고 적는다(24–28). 빈 줄·logging_macros.h 포함·빈 줄(30–32). |
| 33–55 | mod_io 모듈 입구·implicit none·기본 private·openFileForRead 공개·contains(33–40). 루틴 문서는 기존 입력 파일의 존재를 먼저 확인한 뒤 열며, required의 기본값은 필수 파일이라고 설명한다(43–48). 선택 파일(optional file)의 실패는 errorIO를 0이 아닌 값으로 반환한다는 설명과 로깅 설명(48–49). lun·filename·errorIO·선택 인수 required의 입출력 문서와 구분 주석(51–55). |
| 56–77 | 시작 시 33행 mod_io 모듈 안. openFileForRead 입구(56). terminate·ADCIRC_EXIT_FAILURE 및 로깅 루틴/상수/형식을 사용한다(57–58). 입력 논리 장치 번호(logical unit number) lun·임의 길이 전체 경로(full pathname) filename·출력 정수 errorIO·선택 논리 인수 required·지역 fileFound/fileRequired·길이 256 메시지 버퍼(buffer) scratchMessage 선언(59–65). 추적 로그 범위 매크로(67). `if (present(required)) then` (70)이면 fileRequired=required(71); else(72)의 기본값은 `fileRequired = .true. ! default: file is required` (73). errorIO=0 초기화·빈 줄(76–77). |
| 78–98 | 시작 시 33행 mod_io 모듈·56행 openFileForRead 루틴 안. 단위 번호 검색 메시지를 내부 WRITE·FORMAT 21로 만들고 logMessage(INFO) 호출(79–81). INQUIRE(file=trim(filename),exist=fileFound)(82). `if (fileFound .eqv. .false.) then` (83)이면 파일 없음 메시지와 allMessage(INFO)(84–86), `errorIO = 1` (87). `if (fileRequired) then` (88)이면 terminate(exit_code=ADCIRC_EXIT_FAILURE,message='Required file not found: '//trim(filename)) 호출(89–90). 선택 파일도 이 바깥 분기에서는 RETURN한다(92). else(93)는 파일 발견 메시지와 logMessage(INFO)(94–96). 조건 종료·빈 줄(97–98). |
| 99–121 | 시작 시 33행 mod_io 모듈·56행 openFileForRead 루틴 안이며 83행 존재 조건문 밖. `open (lun, file=trim(filename), status='OLD', &` (100); `action='READ', iostat=errorIO)` (101)로 기존 파일을 읽기 전용으로 열고 IOSTAT을 errorIO로 받는다. `if (errorIO /= 0) then` (102)이면 열기 실패 메시지와 allMessage(ERROR)(103–105). `if (fileRequired) then` (106)이면 terminate(exit_code=ADCIRC_EXIT_FAILURE,message='Could not open required file: '//trim(filename)) 호출(107–108). 선택 파일도 이 실패 분기에서는 RETURN한다(110). else(111)는 성공 메시지와 logMessage(INFO)(112–114). 조건·openFileForRead·mod_io 종료 및 구분 주석·빈 줄(115–121). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 60·65·84–85·94–95·103–104·112–113: filename은 임의 길이 character(*) 입력이다. scratchMessage는 길이 256으로 고정되어 있다. 파일명을 포함하는 로그는 이 버퍼에 내부 WRITE로 작성하며 이 루틴에는 파일명 길이 검사나 잘라내기 문장이 없다.
