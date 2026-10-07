---
file: models/EFDC/raw/source_code/EFDC-GVC/acon.for
lines: 120
sha256: 12bc4851f235a20631ce3d8d4db4c384bc57e01a8b8f1433e193a8e0994e4688
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# acon.for — 판독 구간 기록

구간은 1행부터 120행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–45 | 구분 주석·빈 줄(1–5·7–22), `SUBROUTINE ACON(ITVAL)` 입구(6). 주석은 EFDC-FULL VERSION 1.0a와 2001년 11월 1일 수정자를 적는다(10·12). `INCLUDE 'EFDC.PAR'` (23), `INCLUDE 'EFDC.CMN'` (24)로 외부 선언을 포함한다. `PARAMETER (NJELM=2,NATDM=1)` (26)은 상수를 정한다. ZAD·유속·염분·온도·염료·SFL·독성물질·퇴적물 배열의 DIMENSION 및 COMMON 선언은 주석 처리되어 있다(30–42). 포함 파일 내부는 이 판독 범위에 없다. |
| 46–67 | 시작 시 6행 ACON 루틴 안. `IF(ZVAL.LT.ZAD(1,ITVAL))THEN` (46)이면 첫 수직 자료점의 UAGD·VAGD·WAGD·SALAD·TEMAD·DYEAD·SFLAD를 결과에 복사한다(47–55). 기존 `DYEA=SALAD(1,ITVAL)`은 제거 주석이며 실행문은 `DYEA=DYEAD(1,ITVAL)`이다(52–54). `DO NT=1,NTOX` (56), `DO NS=1,NSED` (59), `DO NX=1,NSND` (62)에서 각 독성물질(toxicant)·퇴적물(sediment)·모래(sand)의 첫 자료점도 복사한다(57·60·63). 참 분기는 `RETURN` (65)으로 끝난다. 조건 종료·주석(66–67). |
| 68–87 | 시작 시 6행 ACON 루틴 안. `IF(ZVAL.GE.ZAD(NAZD,ITVAL))THEN` (68)이면 마지막 수직 자료점 NAZD의 유속·염분(salinity)·온도(temperature)·염료(dye)·SFL을 복사한다(69–75). `DO NT=1,NTOX` (76), `DO NS=1,NSED` (79), `DO NX=1,NSND` (82)에서 해당 마지막 자료점의 농도도 복사한다(77·80·83). 참 분기는 `RETURN` (85)으로 끝난다. 조건 종료·주석(86–87). |
| 88–101 | 시작 시 6행 ACON 루틴 안. NZ=1 초기화(88), 표지 1000(89), `NZP=NZ+1` (90)로 인접 자료점 번호를 정한다. `IF(ZVAL.GE.ZAD(NZ,ITVAL).AND.ZVAL.LT.ZAD(NZP,ITVAL))THEN` (91)이면 선형 보간(linear interpolation)을 수행한다. 역간격은 `DZI=1./(ZAD(NZP,ITVAL)-ZAD(NZ,ITVAL))` (92)이다. 가중치는 `WTNZ=DZI*(ZAD(NZP,ITVAL)-ZVAL)` (93), `WTNZP=DZI*(ZVAL-ZAD(NZ,ITVAL))` (94)이다. 결과식은 `UAG=WTNZ*UAGD(NZ,ITVAL)+WTNZP*UAGD(NZP,ITVAL)` (95), `VAG=WTNZ*VAGD(NZ,ITVAL)+WTNZP*VAGD(NZP,ITVAL)` (96), `WAG=WTNZ*WAGD(NZ,ITVAL)+WTNZP*WAGD(NZP,ITVAL)` (97), `SALA=WTNZ*SALAD(NZ,ITVAL)+WTNZP*SALAD(NZP,ITVAL)` (98), `TEMA=WTNZ*TEMAD(NZ,ITVAL)+WTNZP*TEMAD(NZP,ITVAL)` (99), `DYEA=WTNZ*DYEAD(NZ,ITVAL)+WTNZP*DYEAD(NZP,ITVAL)` (100), `SFLA=WTNZ*SFLAD(NZ,ITVAL)+WTNZP*SFLAD(NZP,ITVAL)` (101)이다. |
| 102–120 | 시작 시 6행 ACON 루틴·91행 보간 조건의 참 분기 안. `DO NT=1,NTOX` (102)에서 `TOXA(NT)=WTNZ*TOXAD(NZ,NT,ITVAL)+WTNZP*TOXAD(NZP,NT,ITVAL)` (103)을 계산한다. `DO NS=1,NSED` (105)에서 `SEDA(NS)=WTNZ*SEDAD(NZ,NS,ITVAL)+WTNZP*SEDAD(NZP,NS,ITVAL)` (106)을 계산한다. `DO NX=1,NSND` (108)에서 `SNDA(NX)=WTNZ*SNDAD(NZ,NX,ITVAL)+WTNZP*SNDAD(NZP,NX,ITVAL)` (109)을 계산한다. 참 분기는 `RETURN` (111)으로 끝난다. `ELSE` (112)는 `NZ=NZ+1` (113), `GOTO 1000` (114)으로 다음 인접 자료점을 검사한다. 조건 종료·구분 주석(115–118), 마지막 RETURN·END(119–120). 다른 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26·30–42: NJELM은 선언 이후 이 파일에 나타나지 않는다. NATDM의 후속 등장은 주석 처리된 배열 선언에만 있다.
- 88–115: 표지 1000으로 돌아가는 자료점 검색에는 NZ 상한 검사나 검색 실패 종료문이 없다.
- 91–94: 보간 가중치는 인접 ZAD 값의 차이로 나눈다. 이 블록에는 차이가 0인지 검사하는 조건이 없다. ZAD 입력의 검증은 이 파일 판독으로 확인하지 않았다.
