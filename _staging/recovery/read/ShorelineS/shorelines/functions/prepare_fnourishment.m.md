---
file: models/ShorelineS/raw/source_code/shorelines/functions/prepare_fnourishment.m
lines: 132
sha256: ee0d2030f872e0ce2d4a7d9a9fa108b0ac85c47dd75368784cb044035db1c80e
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# prepare_fnourishment.m — 판독 구간 기록

구간은 1행부터 132행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–62 | 함수 시그니처는 `function [FNOUR] = prepare_fnourishment(S);` (1). 주석은 전빈 양빈(shoreface nourishment) 공급원항(source term), S.fnourish·mb·labda0·rhos·sal·temp·fnorfile 입력과 좌표·길이·수심·입경·시행 시각·체적·확산 계수(diffusion coefficient)·침강 속도(fall velocity) 출력을 설명한다(2–34). 이 파일에는 S 필드 기본값 대입이 없다. 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(35–62). |
| 63–85 | 준비 로그 뒤 FNOUR를 만든다(63–66). x·y·L·d·d50·tstart·V·n·K·V_t를 빈 배열로 초기화한다(67–76). fnourish·mb·labda0·rhos·sal·temp를 같은 이름의 S 필드에서 복사한다(77–84). 주석과 빈 줄을 포함한다. |
| 86–100 | `if ~isempty(FNOUR.fnourish) && FNOUR.fnourish ~= 0` (86) 안에서 `if ~isempty(findstr(lower(S.fnorfile),'.fnor'))` (88)이면 load(91)를 호출한다. `FNOUR.x         = [fnor(:,1) fnor(:,2)];` (92), `FNOUR.y         = [fnor(:,3) fnor(:,4)];` (93)로 시작·끝 좌표를 구성한다. 5·6·7열은 L·d·d50에 복사한다(94–96). `FNOUR.tstart    = datenum(num2str(fnor(:,8)),'yyyymmdd');` (97)로 날짜를 변환하고 9열은 V에 복사한다(98). `FNOUR.n         = size(fnor,1);` (99)로 양빈 개수를 계산한다. |
| 101–120 | 시작 시 86행 활성화 분기·88행 .fnor 분기 안. `for i = 1:FNOUR.n` (101)에서 `if isempty(S.k)` (104)이면 `FNOUR.K(i) = get_fnourishment_diffusion( FNOUR.V(i) / FNOUR.L(i) );` (105)를 호출한다. `else` (106)는 S.k(i)를 복사한다(107). `FNOUR.w(i) = get_fallvelocity(FNOUR.d50(i), FNOUR.rhos, FNOUR.sal, FNOUR.temp);` (111)로 각 양빈의 침강 속도를 얻는다. 루프 종료(112) 뒤 `else` (114)는 88행 조건 불성립 시 파일 정보 부재를 출력한다(115). struct2log 호출은 주석이다(118). 두 분기를 닫는다(116·120). |
| 121–132 | 공백만 있는 줄과 빈 줄이다. 추가 실행문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–14·104–107: 입력 설명에는 S.k가 없다. 실행 코드는 S.k를 검사하고 양빈별 K 입력으로 사용한다.
- 67–76·111: 초기 빈 배열 목록에는 w가 없다. w는 활성화·.fnor 분기와 양빈 루프 안에서 생성한다.
- 1·120–132: 파일은 마지막 분기 end 뒤 빈 줄로 끝난다. 함수 자체를 닫는 별도 end는 없다.
- 92–93: 양빈 좌표 구성식에는 xyoffset을 적용하는 식이 없다.
