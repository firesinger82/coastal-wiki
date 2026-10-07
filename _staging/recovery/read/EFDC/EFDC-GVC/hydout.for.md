---
file: models/EFDC/raw/source_code/EFDC-GVC/hydout.for
lines: 108
sha256: 5f80778a4fbdb75feab9f158be075f2ab495e855cf95151f75f407cd423326a1
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# hydout.for — 판독 구간 기록

구간은 1행부터 108행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | 구분 주석과 `SUBROUTINE HYDOUT` 입구(6). 머리말은 작성자·버전·수정 이력을 적는다(8–19). 목적 주석은 퇴적물 바닥 모델(sediment bed model)에 입력할 전 영역 바닥 유속(bottom velocity) 시계열 출력을 설명한다(23–24). `EFDC.PAR`·`EFDC.CMN` 포함(28–29). 제목 네 개는 CHARACTER*80, 시간 단위 문자열 TUNITS는 CHARACTER*14로 선언한다(34–35). |
| 39–62 | 시작 시 6행 `SUBROUTINE HYDOUT` 루틴 안. JSHYDOUT!=1이면 300 레이블로 이동하여 제목 작성을 건너뛴다(39). 제목은 바닥 유속 파일·위도/경도·UVEL/VVEL/SPD/DIR·CM/S/DEG 단위 문자열이다(45–48). SEDBED.HYD를 장치 11에서 열어 삭제하고 다시 연다(50–52). 제목과 FORMAT을 출력한 후 닫고 JSHYDOUT=0을 설정한다(53–60). 300 레이블과 빈 줄 포함(61–62). 원문(조건·루프·계산·호출·파일 처리, 실행 순서): `IF(JSHYDOUT.NE.1) GOTO 300` (39); `TITLE1='BOTTOM VELOCITY OUTPUT FOR SEDIMENT BED MODEL'` (45); `TITLE2='   DLAT          DLONG'` (46); `TITLE3='        UVEL     VVEL     SPD     DIR '` (47); `TITLE4='       (CM/S)   (CM/S)   (CM/S)  (DEG)'` (48); `OPEN(11,FILE='SEDBED.HYD',STATUS='UNKNOWN')` (50); `CLOSE(11,STATUS='DELETE')` (51); `OPEN(11,FILE='SEDBED.HYD',STATUS='UNKNOWN')` (52); `CLOSE(11)` (59); `JSHYDOUT=0` (60); `300 CONTINUE` (62). |
| 63–82 | 시작 시 6행 `SUBROUTINE HYDOUT` 루틴 안. ISDYNSTP=0이면 DT·N·TBEGIN으로 TIME을 계산하고 TCTMSR로 나눈다(66–67). else는 TIMESEC/TCTMSR이다(68–70). TCTMSR를 1.0·60.·3600.·86400.과 순서대로 동등 비교하여 SECONDS/MINUTES/HOURS/DAYS를 설정한다(71–78). 어느 값도 맞지 않으면 UNKNOWN UNITS이다(79–81). 원문(조건·루프·계산·호출·파일 처리, 실행 순서): `IF(ISDYNSTP.EQ.0)THEN` (66); `TIME=(DT*FLOAT(N)+TCON*TBEGIN)/TCTMSR` (67); `ELSE` (68); `TIME=TIMESEC/TCTMSR` (69); `ENDIF` (70); `IF(TCTMSR.EQ.1.0)THEN` (71); `TUNITS=' SECONDS'` (72); `ELSE IF(TCTMSR.EQ.60.)THEN` (73); `TUNITS=' MINUTES'` (74); `ELSE IF(TCTMSR.EQ.3600.)THEN` (75); `TUNITS=' HOURS'` (76); `ELSE IF(TCTMSR.EQ.86400.)THEN` (77); `TUNITS=' DAYS'` (78); `ELSE` (79); `TUNITS=' UNKNOWN UNITS'` (80); `ENDIF` (81). |
| 83–94 | 시작 시 6행 `SUBROUTINE HYDOUT` 루틴 안. SEDBED.HYD를 APPEND·UNKNOWN으로 열고 시간과 단위를 기록한다(83–85). L=2..LC-1에서 LN=LNC(L)을 얻는다(86–87). 속도 배율 RUVTMP 기본값은 50.이며 SPB(L)=0이면 100.이다(88–89). U/V의 첫 층에서 동쪽·북쪽 면과 현재 면 값을 합하여 UTMP1/VTMP1을 계산한다(90–91). CUE/CVE·CUN/CVN으로 UTMP/VTMP를 변환하고 속력(speed)을 제곱합의 제곱근으로 계산한다(92–94). 원문(조건·루프·계산·호출·파일 처리, 실행 순서): `OPEN(11, FILE='SEDBED.HYD',POSITION='APPEND',STATUS='UNKNOWN')` (83); `DO L=2,LC-1` (86); `LN=LNC(L)` (87); `RUVTMP=50.` (88); `IF(SPB(L).EQ.0) RUVTMP=100.` (89); `UTMP1=RUVTMP*(U(L+1,1)+U(L,1))` (90); `VTMP1=RUVTMP*(V(LN,1)+V(L,1))` (91); `UTMP=CUE(L)*UTMP1+CVE(L)*VTMP1` (92); `VTMP=CUN(L)*UTMP1+CVN(L)*VTMP1` (93); `SPD=SQRT(UTMP**2+VTMP**2)` (94). |
| 95–104 | 시작 시 6행 `SUBROUTINE HYDOUT` 루틴·86행 `DO L=2,LC-1` 루프 안. UTMP와 VTMP가 모두 0이면 DIR=0으로 설정하고 210 레이블로 이동한다(95–98). 그 밖의 경우 ATAN2(UTMP,VTMP)를 계산하여 57.2958을 곱한다(99–100). DIR<0이면 360.을 더한다(101). 210에서 위도·경도·두 속도 성분·속력·방향(direction)을 출력한다(102). L 루프를 종료하고 파일을 닫는다(103–104). 원문(조건·루프·계산·호출·파일 처리, 실행 순서): `IF(UTMP.EQ.0.0.AND.VTMP.EQ.0.0)THEN` (95); `DIR=0` (96); `GOTO 210` (97); `ENDIF` (98); `DIR=ATAN2(UTMP,VTMP)` (99); `DIR=57.2958*DIR` (100); `IF(DIR.LT.0.)DIR=DIR+360.` (101); `ENDDO` (103); `CLOSE(11)` (104). |
| 105–108 | 시작 시 6행 `SUBROUTINE HYDOUT` 루틴 안. 위도·경도 E12.7 두 개, 속도·속력 F6.1 세 개, 방향 F4.0의 출력 FORMAT을 선언한다(105). 빈 줄과 RETURN·END로 루틴을 끝낸다(106–108). 원문(조건·루프·계산·호출·파일 처리, 실행 순서): `RETURN` (107). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 39·50–60: 제목 초기화 분기는 JSHYDOUT=1일 때만 통과한다. 그 분기는 기존 SEDBED.HYD를 STATUS='DELETE'로 지우고 제목을 다시 기록한 뒤 JSHYDOUT=0으로 설정한다.
- 86–91: 출력 셀 범위는 2..LC-1이다. U/V의 수직 인덱스는 모두 1로 고정되어 있다. 이 파일에는 KGVCU/KGVCV를 사용하는 속도 접근이 없다.
- 88–89: RUVTMP의 기본값 50.과 SPB(L)=0 분기의 값 100.은 코드에 직접 적혀 있다.
- 66–81: TIME 계산은 TCTMSR로 나눈 뒤 시간 단위를 판별한다. 단위 분기는 TCTMSR의 네 값과 동등 비교하며 그 밖의 값도 계산된 TIME과 UNKNOWN UNITS로 출력한다. 이 블록에는 TCTMSR=0 검사가 없다.
- 99–101: 방향 식은 ATAN2(UTMP,VTMP) 순서를 사용한다. 라디안(radian)을 도(degree)로 바꾸는 계수는 57.2958로 직접 적혀 있다. 음수 방향에는 360.을 한 번 더한다.
