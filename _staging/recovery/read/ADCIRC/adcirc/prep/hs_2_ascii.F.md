---
file: models/ADCIRC/raw/source_code/adcirc/prep/hs_2_ascii.F
lines: 147
sha256: 764fa0b7e76422d1e20303095518772684f652aa4cf43c17182a717d5d0fea2b
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# hs_2_ascii.F — 판독 구간 기록

구간은 1행부터 147행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | ADCIRC 저작권·LGPL 3 이상·무보증 머리말(1–19). 이진 재시작(hotstart) 파일을 유사한 ASCII 파일로 변환한다는 목적 및 2001·2005년 이력 주석(20–25), 빈 줄(26–27). |
| 28–40 | `PROGRAM hs_2_ascii`와 IMPLICIT NONE(28–30). 노드·요소 수, 레코드 위치, 재시작 모델·시각·단계 및 출력 관련 계수 선언(32–39). 파일명은 CHARACTER*60이다(36). NODECODE와 NOFF는 정수 할당 배열, ETA1/ETA2/UU2/VV2/CH1은 REAL(8) 할당 배열이다(37–38). |
| 41–58 | 시작 시 28행 프로그램 안. 사용자에게 이진 파일명을 읽고 `OPEN (99,FILE=FNAME,ACCESS='DIRECT',RECL=8)` (45)로 연다. 사용자에게 MNP와 MNE를 별도로 읽는다(49–52). 수위·속도·농도·노드 코드 배열은 MNP, NOFF는 MNE 크기로 할당한다(56–57). |
| 59–84 | 시작 시 28행 프로그램 안. 레코드 1·2·3에서 IMHSF·TIMEHSF·ITHSF를 읽는다(59–64). I=1..MNP 루프(66)에서 ETA1·ETA2·UU2·VV2를 읽고 `IHOTSTP=IHOTSTP+4` (71)이다. CH1 판독과 IM 조건은 주석 처리되어 있다(72–75). NODECODE를 읽고 `IHOTSTP=IHOTSTP+1` (77)이다. I=1..MNE 루프(79)는 NOFF를 읽고 `IHOTSTP=IHOTSTP+1` (81)로 이동한다. 빈 줄도 포함한다(83–84). |
| 85–106 | 시작 시 28행 프로그램 안. 현재 IHOTSTP 뒤의 연속 18개 레코드에서 IESTP/NSCOUE, IVSTP/NSCOUV, ICSTP/NSCOUC, IPSTP, IWSTP/NSCOUM, IGEP/NSCOUGE, IGVP/NSCOUGV, IGCP/NSCOUGC, IGPP, IGWP/NSCOUGW를 읽는다(87–104). 장치 99를 닫는다(105). |
| 107–121 | 시작 시 28행 프로그램 안. 출력 이름을 `OPEN(99,FILE='hs_2_ascii.out')` (109)로 고정한다. IMHSF·TIMEHSF·ITHSF를 순서대로 쓴다(113–115). 노드 루프(116)는 번호 I 및 ETA1·ETA2·UU2·VV2·NODECODE를 한 행에 쓴다(117). 요소 루프(119)는 NOFF만 쓴다(120). |
| 122–147 | 시작 시 28행 프로그램 안. 앞서 읽은 공통 정수 정보 18개를 같은 순서로 각각 출력한다(122–139). 출력 장치를 닫고 프로그램을 끝낸다(141–143). 마지막 빈 줄도 포함한다(144–147). 실행 조건 분기나 외부 루틴 호출은 이 프로그램에 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 45: 직접 접근 입력의 레코드 길이는 8로 고정되어 있다. 이 OPEN 문장에는 FORM 지정이 없다.
- 49–57: MNP·MNE는 사용자 입력으로 배열 크기를 정한다. 해당 입력 뒤에 양수 조건 검사나 파일 내용과 비교하는 조건은 없다.
- 38·56–57·72–75·117: CH1은 선언·할당되지만 판독문은 주석 처리되어 있다. ASCII 노드 출력 목록에도 CH1이 없다.
- 32–143: 정수 J는 선언되어 있지만 실행문에서 사용되지 않는다.
