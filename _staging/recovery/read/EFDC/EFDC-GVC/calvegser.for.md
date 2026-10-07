---
file: models/EFDC/raw/source_code/EFDC-GVC/calvegser.for
lines: 92
sha256: 4dfebc44a839f9d7c8ed04b3f76bef37e16ce36cfa506ddf93c0f7421c1b52b7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calvegser.for — 판독 구간 기록

구간은 1행부터 92행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–42 | 구분 주석과 CALVEGSER(ISTL) 선언을 포함한다(1–6). 머리말은 EFDC-FULL 1.0a와 2001-11-01 수정일을 적는다(8–10). 주석은 식생(vegetation) 시계열(time series)의 수·종별 시계열 번호·보간 위치·시간 환산계수와 RDLPSQ·BPVEG·HPVEG 배열을 설명한다(19–29). 시간에 따라 변하는 식생 저항 매개변수(resistance parameters)를 갱신한다는 주석이 있다(33–34). EFDC.PAR와 EFDC.CMN을 포함한다(38–39). |
| 43–61 | 시작 시 6행 CALVEGSER 루틴 안. NVEGSER>0 분기와 NS=1..NVEGSER 루프를 연다(43–45). ISDYNSTP=0이면 DT·N·TBEGIN·TCON으로 시계열 시간을 구한다(47–48). ELSE는 TIMESEC를 사용한다(49–51). M1을 이전 보간 위치에서 시작한다(52). 100번 표지에서 M2=M1+1을 구한다(53–54). TIME이 TVEGSER(M2,NS)보다 크면 M1=M2로 바꾸고 GOTO 100으로 반복한다(55–57). ELSE는 MVEGTLAST를 저장한다(58–60). 원문 실행문: `IF(NVEGSER.GT.0)THEN` (43); `DO NS=1,NVEGSER` (45); `IF(ISDYNSTP.EQ.0)THEN` (47); `TIME=DT*FLOAT(N)/TCVEGSER(NS)+TBEGIN*(TCON/TCVEGSER(NS))` (48); `ELSE` (49); `TIME=TIMESEC/TCVEGSER(NS)` (50); `M1=MVEGTLAST(NS)` (52); `M2=M1+1` (54); `IF(TIME.GT.TVEGSER(M2,NS))THEN` (55); `M1=M2` (56); `ELSE` (58); `MVEGTLAST(NS)=M1` (59). |
| 62–70 | 시작 시 6행 CALVEGSER 루틴·43행 NVEGSER>0 분기·45행 NS 루프 안. 두 시각의 차이 TDIFF와 가중치(weight) WTM1·WTM2를 구한다(62–64). RDLPSQ·BPVEG·HPVEG의 현재 시계열 값은 각각 두 표 값의 선형 보간(linear interpolation)으로 계산한다(65–67). NS 루프를 닫는다(69). 원문 실행문: `TDIFF=TVEGSER(M2,NS)-TVEGSER(M1,NS)` (62); `WTM1=(TVEGSER(M2,NS)-TIME)/TDIFF` (63); `WTM2=(TIME-TVEGSER(M1,NS))/TDIFF` (64); `VEGSERRT(NS)=WTM1*VEGSERR(M1,NS)+WTM2*VEGSERR(M2,NS)` (65); `VEGSERBT(NS)=WTM1*VEGSERB(M1,NS)+WTM2*VEGSERB(M2,NS)` (66); `VEGSERHT(NS)=WTM1*VEGSERH(M1,NS)+WTM2*VEGSERH(M2,NS)` (67). |
| 71–86 | 시작 시 6행 CALVEGSER 루틴·43행 NVEGSER>0 분기 안. M=1..MVEGTYP 루프에서 종의 시계열 번호 NSTMP를 가져온다(71–72). NSTMP>0이면 보간한 RDLPSQ·BPVEG·HPVEG를 복사한다(73–76). BDLTMP와 PVEGX·PVEGY·PVEGZ 및 BDLPSQ를 갱신한다(77–81). 조건과 루프 및 NVEGSER 분기를 닫는다(82–85). 원문 실행문: `DO M=1,MVEGTYP` (71); `NSTMP=NVEGSERV(M)` (72); `IF(NSTMP.GT.0)THEN` (73); `RDLPSQ(M)=VEGSERRT(NSTMP)` (74); `BPVEG(M)=VEGSERBT(NSTMP)` (75); `HPVEG(M)=VEGSERHT(NSTMP)` (76); `BDLTMP=BPVEG(M)*BPVEG(M)*RDLPSQ(M)` (77); `PVEGX(M)=1.-BETVEG(M)*BDLTMP` (78); `PVEGY(M)=1.-BETVEG(M)*BDLTMP` (79); `PVEGZ(M)=1.-ALPVEG(M)*BDLTMP` (80); `BDLPSQ(M)=BPVEG(M)*RDLPSQ(M)` (81). |
| 87–92 | 시작 시 6행 CALVEGSER 루틴 안. 6000 FORMAT은 주석 처리되어 있다(87). 구분 주석과 RETURN·END를 포함한다(88–92). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·43–85: 인수 ISTL은 루틴 선언에 있으나 이 파일의 실행문에서 참조하지 않는다.
- 52–60: 보간 위치는 MVEGTLAST에서 시작해 M1을 증가시키는 방향으로만 탐색한다. 이 탐색 블록에는 M2의 상한 검사와 시간 역행 처리가 없다.
- 62–67: 두 시각의 차이 TDIFF를 가중치의 분모에 사용한다. 이 블록에는 TDIFF=0 검사 또는 가중치를 0..1로 제한하는 문장이 없다.
- 77–81: PVEGX·PVEGY·PVEGZ는 1에서 계산된 항을 빼는 식으로 대입한다. 이 블록에는 계산 후 값의 하한·상한을 제한하는 문장이 없다.
