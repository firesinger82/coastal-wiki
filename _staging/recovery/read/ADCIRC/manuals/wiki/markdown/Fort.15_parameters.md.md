---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.15_parameters.md
lines: 135
sha256: bbd5dce81f6d1b89d60847695830457ff7cf3ab090d713f992ebc7635b156ec5
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.15_parameters.md — 판독 구간 기록

구간은 1행부터 135행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | Fort.15 parameters / 제목·목차 — 제목·판본·목차·빈 줄을 포함한다(1–30). 주요 제어·3D·NetCDF·namelist 절을 나열한다(7–29). |
| 31–44 | Main Controls / Metadata and Logging / 표 머리 — 매개변수·자료형·필수 여부·설명·값이라는 다섯 열 제목을 개별 행으로 적는다(35–43). 원문: `Parameter` (35); `Type` (37); `Required?` (39); `Description` (41); `Values` (43). |
| 45–62 | Metadata and Logging / RUNDES — 실행 설명 문자열의 이름, 길이 상한, 항상 필요하다는 조건과 영숫자 허용을 제시한다(45–61). 부등호의 HTML 문자 참조와 LaTeX 표기를 모두 그대로 옮긴다(50·53). 원문: `` `RUNDES` `` (45); `        &#x2264;` (50); `    {\displaystyle \leq }` (53); `32 character string` (55); `Always` (57); `Run description` (59); `Any alpha-numeric` (61). |
| 63–80 | Metadata and Logging / RUNID — 실행 식별 문자열의 이름, 길이 상한, 항상 필요하다는 조건과 영숫자 허용을 제시한다(63–79). 부등호의 HTML 문자 참조와 LaTeX 표기를 모두 그대로 옮긴다(68·71). 원문: `` `RUNID` `` (63); `        &#x2264;` (68); `    {\displaystyle \leq }` (71); `24 character string` (73); `Always` (75); `Run identification` (77); `Any alpha-numeric` (79). |
| 81–90 | Metadata and Logging / NFOVER — 정수(integer) 형식이며 항상 필요한 비치명적 오류 무시 제어의 이름과 허용값을 제시한다(81–89). 기본값은 이 구간에 없다. 원문: `` `[NFOVER](/index.php?title=NFOVER&action=edit&redlink=1)` `` (81); `integer` (83); `Always` (85); `Non-fatal error override option` (87); `0 or 1` (89). |
| 91–100 | Metadata and Logging / NABOUT — 정수 형식이며 항상 필요한 로깅 수준(logging level)의 이름과 허용값을 제시한다(91–99). 기본값은 이 구간에 없다. 원문: `` `[NABOUT](/index.php?title=NABOUT&action=edit&redlink=1)` `` (91); `integer` (93); `Always` (95); `Logging level` (97); `-1, 0, 1, 2, or 3` (99). |
| 101–110 | Metadata and Logging / NSCREEN — 정수 형식이며 항상 필요한 로그 출력 위치의 이름과 허용값을 제시한다(101–109). 기본값은 이 구간에 없다. 원문: `` `[NSCREEN](/index.php?title=NSCREEN&action=edit&redlink=1)` `` (101); `integer` (103); `Always` (105); `Logging output destination` (107); `-1, 0, or 1` (109). |
| 111–126 | Numerics & Physics부터 Hotstart Output and Numeric Controls까지 — 여섯 절·소절 제목과 빈 줄이 이어진다(111–124). NetCDF를 사용하지 않는 2DDI 파일 종료 위치와 NetCDF 사용 시 끝에 추가해야 하는 메타데이터의 처음·마지막 항목을 적는다(125). 원문: ``For a 2DDI ADCIRC run that does not use netCDF, the file ends here. For any ADCIRC run that uses netCDF, the lines `NCPROJ` through `NCDATE` (described in the [NetCDF Control](#NetCDF_Control) section below) are required metadata and must be added at the end of the fort.15 file.`` (125). |
| 127–132 | 3D Model Run / NetCDF Control — 3D 절 제목만 있고 입력 목록은 없다(127–128). NetCDF 출력 또는 재시작 형식 선택 시에만 후속 행을 읽는다고 적는다(129–131). 원문: `The following lines will be read in only if the NetCDF output or hotstart format is chosen` (131). |
| 133–135 | Namelists — Fortran namelist 행은 선택 사항이지만 사용할 경우 파일 맨 끝에 있어야 한다고 명시한다(135). namelist 예시는 이 파일에 없다. 원문: `The following Fortran namelist lines are optional, but if they appear, they must appear at the very end of the fort.15 file.` (135). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 50·53·68·71: 문자열 길이 상한의 부등호가 HTML 문자 참조 `&#x2264;`와 LaTeX `{\displaystyle \leq }`로 각각 나타난다.
- 81·91·101: 세 변수 참조 URL에 `action=edit&redlink=1`이 들어 있다.
- 111–124·127–128·133–135: 여러 절·소절은 제목만 있거나 안내 문장만 있고 매개변수 목록·형식 예시가 없다.
- 125·129–132: 125행은 `NCPROJ`부터 `NCDATE`까지의 항목을 아래 NetCDF Control 절에서 설명한다고 적는다. 해당 절에는 조건 문장만 있고 그 항목 목록이나 정의가 없다.
