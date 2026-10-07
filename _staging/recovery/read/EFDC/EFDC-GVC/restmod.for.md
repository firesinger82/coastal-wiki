---
file: models/EFDC/raw/source_code/EFDC-GVC/restmod.for
lines: 149
sha256: 732bb3e532708ac3a6f6083583335e55b200a9d291340ab255452dcdb506cba7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# restmod.for — 판독 구간 기록

구간은 1행부터 149행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | 구분 주석·RESTMOD 선언·EFDC-FULL 1.0a·수정일·변경 기록 머리말(1–17). 19행 설명은 RESTOUT이 재시작 파일(restart file)을 쓴다고 적는다. EFDC.PAR·EFDC.CMN을 포함하고 LIJMOD의 크기를 100으로 선언한다(23–25). |
| 29–51 | 시작 시 6행 RESTMOD 루틴 안. RESTART.OUT을 삭제 후 생성한다(29–31). 고정 시간 간격이면 DT·N·TBEGIN으로, 동적 시간 간격이면 TIMESEC으로 TIME을 계산하여 N과 함께 쓴다(35–42). RESTMOD.INP에서 NIJMOD와 좌표 ITMP·JTMP를 읽고 LIJ로 찾은 셀 번호를 LIJMOD에 저장한다(44–50). 원문: `IF(ISDYNSTP.EQ.0)THEN` (35) / `TIME=DT*FLOAT(N)+TCON*TBEGIN` (36) / `TIME=TIME/TCON` (37) / `ELSE` (38) / `TIME=TIMESEC/TCON` (39) / `DO NNIJ=1,NIJMOD` (46) / `LIJMOD(NNIJ)=LIJ(ITMP,JTMP)` (48). |
| 52–69 | 시작 시 6행 RESTMOD 루틴 안. L=2..LA에서 LSMOD를 1로 시작한다(52–53). LIJMOD와 같은 셀은 LSMOD를 0으로 바꾼다(54–56). LSMOD=1인 셀만 수심 4개·BELV, 수심 적분(depth integrated) 유량 4개, U·U1·V·V1의 1..KC 층, QQ·QQ1·QQL·QQL1·DML의 0..KC 층을 출력한다(57–69). 원문: `DO L=2,LA` (52) / `LSMOD=1` (53) / `DO NNIJ=1,NIJMOD` (54) / `IF(L.EQ.LIJMOD(NNIJ)) LSMOD=0` (55) / `IF(LSMOD.EQ.1)THEN` (57). |
| 70–92 | 시작 시 6행 RESTMOD 루틴 안. 시작 시 52행 L 루프·57행 LSMOD=1 참 분기 안. ISCO(1..5)=1의 개별 조건으로 염분(salinity), 수온(temperature), 염료(dye), 첫 퇴적물(sediment) 성분의 바닥·수체 현재 및 이전 값, SFL·SFL2를 출력한다(70–89). 셀 선택 조건과 L 루프를 닫는다(90–91). 원문: `IF(ISCO(1).EQ.1)THEN` (70) / `IF(ISCO(2).EQ.1)THEN` (74) / `IF(ISCO(3).EQ.1)THEN` (78) / `IF(ISCO(4).EQ.1)THEN` (82) / `IF(ISCO(5).EQ.1)THEN` (86). |
| 93–130 | 시작 시 6행 RESTMOD 루틴 안. M=1..5에서 ISCO(M)=1인 성분의 네 방향 경계 이력을 출력한다(93–129). 각 경계의 K=1..KC에서 NLOS·NLOW·NLOE·NLON 자체에 N을 빼서 저장한 뒤 정수 FORMAT으로 출력한다(96–126). CLOS·CLOW·CLOE·CLON은 실수 FORMAT으로 출력한다(101·109·117·125). 원문: `DO M=1,5` (93) / `IF(ISCO(M).EQ.1)THEN` (94) / `DO LL=1,NCBS` (96) / `DO K=1,KC` (97) / `NLOS(LL,K,M)=NLOS(LL,K,M)-N` (98) / `DO LL=1,NCBW` (104) / `DO K=1,KC` (105) / `NLOW(LL,K,M)=NLOW(LL,K,M)-N` (106) / `DO LL=1,NCBE` (112) / `DO K=1,KC` (113) / `NLOE(LL,K,M)=NLOE(LL,K,M)-N` (114) / `DO LL=1,NCBN` (120) / `DO K=1,KC` (121) / `NLON(LL,K,M)=NLON(LL,K,M)-N` (122). |
| 131–149 | 시작 시 6행 RESTMOD 루틴 안. RESTART.OUT을 닫는다(133). ISRESTO=-2의 OUT3D 호출은 주석이다(135). 906·907 FORMAT은 5E17.8·13E17.8이고 CMRM 대체 형식은 주석이다(139–142). 경계 정수는 12I10, 시각 머리말은 I20·4X·F12.4이다(143–144). 구분 주석·RETURN·END를 포함한다(145–149). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 25·45–49: LIJMOD 배열 크기는 100이다. NIJMOD개의 좌표를 읽어 LIJMOD에 저장하는 루프 앞에는 NIJMOD≤100 검사가 없다.
- 52–91: RESTMOD.INP에 나열된 셀은 LSMOD=0으로 설정한다. 셀별 출력은 LSMOD=1에서만 실행된다. 나열된 셀을 위한 대체 값 또는 자리 레코드를 쓰는 ELSE는 이 블록에 없다.
- 98·106·114·122·133–149: 경계 시간 인덱스 배열 NLOS·NLOW·NLOE·NLON에서 N을 직접 뺀다. 출력 뒤 이 배열들에 N을 되더하는 문장은 이 파일에 없다.
