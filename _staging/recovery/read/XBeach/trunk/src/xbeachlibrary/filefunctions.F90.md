---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/filefunctions.F90
lines: 363
sha256: d5e4c239d7ecec15ef329769fb187aecaf61bf701d6955850a11dcae52e1fe00
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# filefunctions.F90 — 판독 구간 기록

구간은 1행부터 363행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `filefunctions` 모듈. `slen`·`xmaster`·`paramsconst` 사용(2–4), 기본 private·save, 공개 함수와 검사 루틴 지정(6–8). `check_file_length`는 1D·2D·3D 절차의 generic interface(9–13). |
| 16–30 | `create_new_fid`: `fileunit=-1` 후 `create_new_fid_generic()` 호출(22–23). 반환값 -1이면 `writelog`로 unit 부족을 기록하고 `halt_program` 호출(24–27), 그 외 unit 반환(28). |
| 31–69 | `check_file_exist`: 선택 인자 `forceclose`가 없으면 종료 여부 `endsim=.true.`(43–47). `error=0` 후 master만 generic 존재 검사(49–50). `error==1 .and. endsim`이면 로그·종료(52–57); 선택 출력 `exist`는 error가 1이면 false, 나머지는 true(59–65). |
| 70–96 | 1D 길이 검사: master에서 `dat(d1)` 할당·새 unit·파일 open 후 실수 d1개 list-directed 읽기(81–85). `iostat/=0`이면 짧거나 잘못된 값이라는 로그·종료(86–90); 정상 경로는 close·deallocate(91–92). 추가 데이터나 정확한 총행수는 검사하지 않는다. |
| 97–123 | 2D 길이 검사: master에서 `dat(d1,d2)`를 할당해 i 안쪽·j 바깥 implied-do로 읽음(109–113). 읽기 상태가 0이 아니면 로그·종료(114–118), close·해제(119–120). |
| 124–150 | 3D 길이 검사: master에서 `dat(d1,d2,d3)` 할당, i→j→k 순 implied-do 읽기(136–140). 오류 시 `writelog('esl',...)`·`halt_program`(141–145), close·해제(146–147). |
| 151–196 | `checkbcfilelength` 선언: 파일명·행수의 `fileinfo` 형(156–159), 종료시간·파랑 경계유형·파일유형·선택 nonh 인자(161–170). nonh 미지정 시 false(172–176). master가 `(a)` 형식으로 성공한 레코드를 세고 rewind(178–188), 첫 문자열 읽기 오류는 `report_file_read_error`(191–194). 보조 unit `fid2`도 발급(195–196). |
| 197–223 | 첫 문자열이 `LOCLIST`이면 `nlocs=nlines-1`, 각 행에서 좌표 d1·d2와 파일명 읽기(197–204), `check_file_exist` 후 각 파일 레코드 수를 `(a)`로 계산(205–214). 그 외 단일 파일명·행수를 등록(216–221); 목록 파일 close(222). |
| 224–245 | 위치별 파일을 열고 파랑 유형으로 filetype 결정. PARAMETRIC·SWAN·VARDENS는 첫 문자열이 `FILELIST`이면 1 및 행수−1, 아니면 0(227–237); JONS_TABLE은 2, REUSE는 3(238–242). 각 파일에서 `total=0.d0`, `i=0`(244–245). |
| 246–267 | 시간 검사 case 0은 `total=2.d0*tstop`(247–248). case 1은 `t,dt,dummy`를 읽어 `total=total+t`, 파일 존재 확인(249–258). case 2는 `d1..d5,t,dt`를 읽어 t 누적(259–267). 반복 조건은 `total<tstop .and. i<nlines`; 읽기 오류는 `report_file_read_error` 호출(252–254·262–264). |
| 268–294 | REUSE case 3: nonh이면 `d1,total,d2,d3,dummy`, 아니면 `total,d2..d6,dummy` 읽기(270–274), total은 누적하지 않고 입력값으로 교체; 참조 파일 존재 검사(278). `end select`(281) 이후 모든 filetype에 공통으로 `close(fid)`(282) 뒤 `if (total<tstop) then`(283)이면 총시간·요구시간 로그와 `call halt_program`(284–289). [10-02 검증 정정: REUSE 전용이 아니라 select 밖 공통 검사] 위치 루프·master 분기·루틴 끝(290–293). |
| 295–326 | `get_file_length`: n·io를 0으로(304–305), 공백 파일명 또는 존재하지 않는 파일이면 0(307–313). 존재하면 고정 unit 11로 실수 하나씩 list-directed 읽으며 n 증가, 첫 비정상 상태까지 반복한 뒤 n−1(315–321). 문자 레코드 자체가 아니라 실수 읽기 성공 횟수를 센다. |
| 327–344 | `check_file_exist_generic`: `inquire(file=filename,exist=file_exists)`(334), 기본 error=0, 존재하지 않으면 1(336–340). |
| 345–363 | `create_new_fid_generic`: 선언 시 `tryunit=9999`(346), 열려 있는 unit이면 감소(350–354); `tryunit<=10`이면 −1로 반환하도록 루프 종료(355–358). 비어 있는 unit을 반환(360), 함수·모듈 끝(361–363). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 49–65: 파일 존재 검사는 master만 실행하며, 이 루틴 안에는 error 전달 호출이 없다. 비master는 초기 error=0을 사용해 선택 출력 exist를 true로 설정한다.
- 142: 3D 오류 로그의 인자 형태는 `writelog('esl','Error processing file ...',...)`이며, 1D·2D의 `'sle','',...`(87·115)과 다르다.
- 227–242: 열거된 wbctype 외에는 filetype에 새 값을 대입하는 분기가 없고, 246행에서 해당 인자를 select case에 사용한다.
- 315–321: `get_file_length`는 고정 unit 11을 사용하고, 첫 실수 읽기 오류에서 계수를 끝낸다.
- 346·353–360: `tryunit`은 선언 초기값 9999를 갖고 호출 간 저장되는 변수이며, 감소 후 다음 호출에서 9999로 재설정하는 문장은 없다.
