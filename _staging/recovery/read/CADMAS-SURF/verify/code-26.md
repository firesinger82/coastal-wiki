# CADMAS-SURF code-26 전수 검증

검증일: 2026-11-04.
각 기록의 frontmatter `file:` 원문을 구간별로 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
한 번의 원문 출력은 200행 이하로 제한했다.
조건·대입식·연속문·선언·호출 인수·주석·블록 경계와 한국어 요약의 의미를 대조했다.
원문은 변경하지 않았다.
모델은 실행하지 않았다.
git은 조작하지 않았다.
원문의 SHA-256은 각 기록의 frontmatter 값과 일치했다.
수정한 기록의 frontmatter와 구간 경계는 수정 전과 일치했다.
빈 행과 구분용 C 주석을 제외한 모든 원문 행은 해당 구간의 백틱 인용에 포함되어 있다.

기록 경로의 기준은 `../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/`이다.
대조 원문 행 수에는 빈 행과 주석 행을 포함한다.
정정·보완·이상 없음의 집계 단위는 기록 표의 구간 행이다.
같은 구간에 여러 수정이 있으면 목록은 항목별로 적고, 집계는 정정을 우선하여 한 번만 센다.
후속 사실 항목의 수정은 해당 원문을 포함하는 구간 행에 합산했다.

| 기록 | 대조 구간 행 수 | 대조 원문 행 수 | 상태 |
|---|---:|---:|---|
| partition/ex_add.f.md | 2 | 21 | 완료 |
| partition/ex_pload4.f.md | 2 | 36 | 완료 |
| partition/ex_spc.f.md | 2 | 33 | 완료 |
| partition/ex_spc1.f.md | 2 | 30 | 완료 |
| partition/metis_partition.c.md | 2 | 34 | 완료 |
| partition/part.f.md | 7 | 267 | 완료 |
| partition/part_c.f.md | 11 | 547 | 완료 |
| partition/part_geom.f.md | 3 | 109 | 완료 |
| partition/part_send_tblx.f.md | 2 | 31 | 완료 |
| partition/part_send_tblx1.f.md | 16 | 723 | 완료 |
| partition/part_send_tblx2.f.md | 6 | 187 | 완료 |
| partition/partition.f.md | 2 | 33 | 완료 |
| partition/recv_tbl.f.md | 8 | 302 | 완료 |
| partition/recv_tblx.f.md | 9 | 369 | 완료 |
| partition/send_tbl.f.md | 13 | 492 | 완료 |
| seq/cgadmg_s.f.md | 2 | 50 | 완료 |
| seq/cgindx2_s.f.md | 3 | 68 | 완료 |
| seq/clsindex_s.f.md | 2 | 71 | 완료 |
| seq/geomtx_s.f.md | 2 | 26 | 완료 |
| seq/glbstfg_s.f.md | 2 | 42 | 완료 |
| seq/gmtxhx2_s.f.md | 2 | 47 | 완료 |
| seq/gmtxpn2_s.f.md | 2 | 59 | 완료 |
| seq/gmtxte1_s.f.md | 1 | 16 | 완료 |
| seq/gmtxte2_s.f.md | 2 | 35 | 완료 |
| seq/gnpflw_s.f.md | 3 | 74 | 완료 |
| seq/mkindex_s.f.md | 8 | 324 | 완료 |
| seq/nl_static_s.f.md | 8 | 261 | 완료 |
| seq/nl_transient_s.f.md | 10 | 341 | 완료 |
| seq/npflow_s.f.md | 3 | 79 | 완료 |
| seq/npforce_s.f.md | 3 | 79 | 완료 |
| seq/spcdrhvg_s.f.md | 1 | 23 | 완료 |
| src/bcgstb.f.md | 3 | 73 | 완료 |
| src/bdfbm.f.md | 1 | 23 | 완료 |
| src/bdfhx2.f.md | 2 | 51 | 완료 |
| src/bdfpn2.f.md | 2 | 38 | 완료 |
| src/bdfte1.f.md | 1 | 23 | 완료 |
| src/bdftrs.f.md | 1 | 23 | 완료 |
| src/bdyfc.f.md | 3 | 66 | 완료 |
| src/beam0.f.md | 2 | 23 | 완료 |
| src/beam2.f.md | 2 | 23 | 완료 |
| src/blmbm.f.md | 2 | 32 | 완료 |

완료 기록 41개에서 구간 160행과 원문 5184행을 대조했다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| partition/ex_add.f.md:7–21 (보완) | ELSE 유무 미표기 | IF/ELSEIF 사슬에 ELSE 없음 명시 | 13–17 |
| partition/part_c.f.md:326–398 (정정) | 구간 근거 없이 접촉 항목으로 단정 | IELCP 조건과 IELC 배열로 서술 | 342–344 |
| partition/part_c.f.md:399–462 (정정) | 모든 추가 절점에 가산하는 요약 | IP > 0인 경우로 한정 | 458–461 |
| partition/part_geom.f.md:73–109 (보완) | ELSE 유무 미표기 | ELSE 없음 명시 | 93–101 |
| partition/part_send_tblx1.f.md:1–46 (정정) | 접촉 의미를 근거 없이 단정 | INDC0 항목 번호로 서술 | 39–45 |
| partition/part_send_tblx1.f.md:47–84 (정정) | 소유하지 않은 접촉 절점으로 단정 | IBN 조건과 INDC0 배열로 서술 | 63–69 |
| partition/part_send_tblx1.f.md:85–119 (보완) | 바깥 루프 이름만 기재 | 루프 범위와 닫힘 행 명시 | 63·71·75·133·141·143 |
| partition/part_send_tblx1.f.md:120–160 (정정) | 바깥 루프 범위 누락과 종료·접촉 의미 단정 | 루프 범위·닫힘·GOTO 대상·EXIT 범위 명시 | 63–143 |
| partition/part_send_tblx1.f.md:85–119 (정정) | 모서리·면·사각형 의미를 단정 | 상태별 배열 참조와 네 항목 대입으로 서술 | 85–118 |
| partition/part_send_tblx1.f.md:239–291 (정정) | 배열의 물리적 의미를 근거 없이 단정 | 배열 이름과 할당·복사·해제 대상으로 서술 | 240–288 |
| partition/part_send_tblx1.f.md:292–344 (정정) | 면·모서리·접촉 자료로 단정 | 참조·할당 배열로 서술 | 319–338 |
| partition/part_send_tblx1.f.md:345–400 (정정) | 접촉·마스터·사각형 의미를 단정 | 조건과 참조 배열로 서술 | 345–400 |
| partition/part_send_tblx1.f.md:401–441 (정정) | 바깥 블록 범위 누락과 면·사각형 단정 | 블록 조건·닫힘과 배열 대입 명시 | 345–440 |
| partition/part_send_tblx1.f.md:442–493 (정정) | 접촉 항목으로 단정 | NODX·INDC0 대응으로 서술 | 444–460 |
| partition/part_send_tblx1.f.md:494–542 (정정) | 송신 요약에 NEX·NINCX 조건 누락과 접촉 의미 단정 | 개수와 자료의 송신 조건 구분 | 496–539 |
| partition/part_send_tblx1.f.md:543–582 (정정) | 면·모서리·사각형 의미 단정 | 참조 배열로 서술 | 547–575 |
| partition/part_send_tblx1.f.md:583–640 (정정) | 기하 의미 단정과 송신 조건 요약 누락 | 배열 대응과 각각의 송신 조건 명시 | 584–635 |
| partition/part_send_tblx1.f.md:641–699 (정정) | 접촉·마찰·변위·마스터 의미 단정 | 크기 식과 배열 참조로 서술 | 643–690 |
| partition/part_send_tblx1.f.md:700–723 (정정) | 접촉 항목 수로 단정 | 검사 변수로 서술 | 700–707 |
| partition/recv_tbl.f.md:1–29 (정정) | 수신 변수의 물리적 의미와 전체 범위를 단정 | 수신 순서와 KK 대응을 명시 | 12–22 |
| partition/recv_tbl.f.md:199–240 (정정) | 접촉 그룹 수로 단정 | 배열 크기와 대입식으로 서술 | 201–230 |
| partition/recv_tbl.f.md:241–283 (정정) | 모서리 수로 단정 | 수신 변수로 서술 | 243–248 |
| partition/recv_tbl.f.md:284–302 (정정) | 면·모서리 의미 단정 | 각각의 수신 조건 변수로 서술 | 286–294 |
| partition/recv_tblx.f.md:39–92 (보완) | 바깥 IP 루프 범위·닫힘 누락 | DO 범위·종료 323행과 적용 분기 명시 | 37·49·123·125·323 |
| partition/recv_tblx.f.md:93–126 (보완) | 바깥 IP 루프 범위·닫힘 누락 | DO 범위·종료 323행과 적용 분기 명시 | 37·49·123·125·323 |
| partition/recv_tblx.f.md:127–172 (보완) | 바깥 IP 루프 범위·닫힘 누락 | DO 범위·종료 323행과 적용 분기 명시 | 37·49·123·125·323 |
| partition/recv_tblx.f.md:173–217 (보완) | 바깥 IP 루프 범위·닫힘 누락 | DO 범위·종료 323행과 적용 분기 명시 | 37·49·123·125·323 |
| partition/recv_tblx.f.md:218–259 (보완) | 바깥 IP 루프 범위·닫힘 누락 | DO 범위·종료 323행과 적용 분기 명시 | 37·49·123·125·323 |
| partition/recv_tblx.f.md:260–295 (보완) | 바깥 IP 루프 범위·닫힘 누락 | DO 범위·종료 323행과 적용 분기 명시 | 37·49·123·125·323 |
| partition/recv_tblx.f.md:296–324 (보완) | 바깥 IP 루프 범위·닫힘 누락 | DO 범위·종료 323행과 적용 분기 명시 | 37·49·123·125·323 |
| partition/recv_tblx.f.md:39–92 (정정) | 접촉 요소로 단정 | INDCEA·INDCE 구간으로 서술 | 71–80 |
| partition/recv_tblx.f.md:173–217 (정정) | 접촉 의미 단정 | NINDCX 조건과 INDC 항목으로 서술 | 206–216 |
| partition/recv_tblx.f.md:296–324 (정정) | 접촉·마찰·변위 의미 단정 | 재할당 배열과 수신 배열 구분 | 298–321 |
| partition/send_tbl.f.md:1–61 (정정) | 접촉 의미를 단정 | 조건별 참조 배열로 서술 | 26–48 |
| partition/send_tbl.f.md:97–127 (정정) | 접촉 요소와 속성 의미 단정 | IELM 행 범위와 참조 배열로 서술 | 109–120 |
| partition/send_tbl.f.md:287–333 (정정) | 접촉 의미 단정 | 참조 배열과 EX_ADD 경계 대응으로 서술 | 291–329 |
| partition/send_tbl.f.md:334–369 (정정) | 접촉 의미 단정 | INDA0·INC 경계와 INDCW 변환·송신 조건으로 서술 | 350–365 |
| partition/send_tbl.f.md:287–333 (보완) | GOTO 경로를 행 번호로만 지시 | 조건식과 대상 레이블 행 명시 | 285·489 |
| partition/send_tbl.f.md:334–369 (보완) | GOTO 경로를 행 번호로만 지시 | 조건식과 대상 레이블 행 명시 | 285·489 |
| partition/send_tbl.f.md:370–400 (보완) | GOTO 경로를 행 번호로만 지시 | 조건식과 대상 레이블 행 명시 | 285·489 |
| partition/send_tbl.f.md:401–442 (보완) | GOTO 경로를 행 번호로만 지시 | 조건식과 대상 레이블 행 명시 | 285·489 |
| partition/send_tbl.f.md:443–486 (보완) | GOTO 경로를 행 번호로만 지시 | 조건식과 대상 레이블 행 명시 | 285·489 |
| partition/send_tbl.f.md:370–400 (정정) | 면·모서리·속성 의미 단정 | 행별 변환과 송신 조건 명시 | 390–399 |
| partition/send_tbl.f.md:443–486 (정정) | 사각형 의미 단정 | IELQ 변환과 송신 조건 명시 | 449–454 |
| seq/cgadmg_s.f.md:32–50 (보완) | 바깥 블록 이름만 기재 | 조건·루프 범위·닫힘 행 명시 | 7–43 |
| seq/cgadmg_s.f.md:32–50 (정정) | 오류 메시지를 호출한다고 서술 | GOTO·WRITE·CALL 순서 구분 | 38·47–48 |
| seq/cgindx2_s.f.md:22–56 (정정) | 접촉 추가 요소로 단정 | 실제 반복 범위와 건너뛰는 첨자 구간 명시 | 22–24 |
| seq/cgindx2_s.f.md:22–56 (정정) | 침투 경로로 단정 | ISEEP·ITYP 조건으로 서술 | 29–55 |
| seq/cgindx2_s.f.md:57–68 (보완) | 바깥 루프 이름만 기재 | 반복 범위와 닫힘 행 명시 | 22·60 |
| seq/geomtx_s.f.md:1–11 (정정) | POR를 공극률로 근거 없이 단정 | AMAT와 POR의 대입 관계로 서술 | 8–10 |
| seq/glbstfg_s.f.md:1–16 (정정) | 시간 단위와 강성 행렬 의미 단정 | 산술평균과 초기화 범위로 서술 | 13–15 |
| seq/glbstfg_s.f.md:17–42 (정정) | 저장·확산 의미 단정과 ELSE 유무 미표기 | 실제 식과 ELSE 없음 명시 | 30–34 |
| seq/gmtxhx2_s.f.md:23–47 (정정) | 호출 인수의 수학적 의미를 단정 | 호출·누적 사실과 형상 함수 해석 구분 | 33–41 |
| seq/gmtxpn2_s.f.md:1–36 (정정) | NI·NJ의 기하 의미 단정 | ID 조건과 적분 점 해석 구분 | 8–9·28–32 |
| seq/gmtxpn2_s.f.md:37–59 (정정) | RN·DNDX·DET 의미 단정 | 호출·누적 사실과 수학적 해석 구분 | 46–54 |
| seq/gmtxte1_s.f.md:1–16 (정정) | 형상 함수·도함수 의미 단정 | 배열과 호출 사실 및 해석 구분 | 4–14 |
| seq/gmtxte2_s.f.md:21–35 (정정) | 형상 함수·도함수 의미 단정 | 호출·누적 사실과 해석 구분 | 23–31 |
| seq/gnpflw_s.f.md:1–16 (정정) | POR 공극률 의미 단정 | AMAT 첨자와 대입 관계 명시 | 10–13 |
| seq/gnpflw_s.f.md:17–46 (정정) | 변위·압력·시간 의미 단정 | 배열 연산 사실과 물리적 해석 구분 | 17–31 |
| seq/gnpflw_s.f.md:47–74 (정정) | 호출 인수의 적분 수 의미 단정 | ND별 실제 인수와 해석 구분 | 54–65 |
| seq/mkindex_s.f.md:49–81 (보완) | 바깥 SELECT 조건과 닫힘 누락 | ISEEP·CASE 경계·종료 행 명시 | 25·26·82·127 |
| seq/mkindex_s.f.md:49–81 (정정) | 접촉 추가 구간으로 첨자를 뭉뚱그림 | 정확한 제외 범위와 ELSE 없음 명시 | 55–78 |
| seq/mkindex_s.f.md:82–128 (정정) | CASE 진입 위치와 접촉 의미 단정 | SELECT 조건·종료와 실제 변수 명시 | 25·82–90·127 |
| seq/mkindex_s.f.md:82–128 (보완) | ELSE 유무 미표기 | ELSE 없음 명시 | 104–122 |
| seq/mkindex_s.f.md:129–170 (보완) | 메모리 오류 요약에 출력 순서 누락 | WRITE·FORMAT·CALL 순서 명시 | 139–144 |
| seq/mkindex_s.f.md:192–222 (보완) | 바깥 SELECT 닫힘 누락 | 조건과 CASE 경계·종료 행 명시 | 171·192·223·322 |
| seq/mkindex_s.f.md:223–262 (보완) | 바깥 SELECT 닫힘 누락 | 조건과 CASE 경계·종료 행 명시 | 171·223·263·322 |
| seq/mkindex_s.f.md:263–324 (보완) | 바깥 SELECT 닫힘 누락 | 조건과 종료 행 명시 | 171·263·322 |
| seq/nl_static_s.f.md:1–45 (정정) | 조건을 침투로 뭉뚱그림과 접촉력 단정 | 배열별 초기화와 정확한 조건 명시 | 26–38 |
| seq/nl_static_s.f.md:1–45 (보완) | ELSE 유무 미표기 | ELSE 없음 명시 | 40–44 |
| seq/nl_static_s.f.md:84–104 (정정) | 순위별 호출을 뭉뚱그림 | KK(25)와 MYRANK별 호출 구분 | 84–92 |
| seq/nl_static_s.f.md:151–176 (보완) | 바깥 루프 범위·닫힘 누락 | 두 DO 범위와 종료 행 명시 | 105·117·204·238 |
| seq/nl_static_s.f.md:177–205 (보완) | 바깥 루프 범위·닫힘 누락 | 두 DO 범위와 종료 행 명시 | 105·117·204·238 |
| seq/nl_static_s.f.md:206–239 (보완) | 바깥 루프 범위·닫힘 누락 | DO 범위와 종료 행 명시 | 105·238 |
| seq/nl_static_s.f.md:151–176 (보완) | 오류 처리 요약에 메시지 출력 누락 | 조건과 WRITE·CALL 순서 및 ELSE 없음 명시 | 155–160 |
| seq/nl_static_s.f.md:240–261 (보완) | 출력 경로와 ELSE 유무 미표기 | 랭크별 처리 뒤 모든 랭크의 OUTPUT 호출 명시 | 244–255 |
| seq/nl_transient_s.f.md:57–89 (정정) | 재시작·결합·순위별 조건을 뭉뚱그림 | KK(84)·ICPL·MYRANK별 호출 명시 | 57–72 |
| seq/nl_transient_s.f.md:57–89 (보완) | REMESH를 조건부로만 서술 | 세 조건과 ELSE 없음 명시 | 80–88 |
| seq/nl_transient_s.f.md:90–122 (정정) | 순위별 호출을 뭉뚱그림 | KK(25)와 MYRANK별 호출 구분 | 90–98 |
| seq/nl_transient_s.f.md:90–122 (보완) | 바깥 루프 이름만 기재 | DO 범위와 닫힘 행 명시 | 74·111·123·215·250·339 |
| seq/nl_transient_s.f.md:123–165 (보완) | 바깥 루프 이름만 기재 | DO 범위와 닫힘 행 명시 | 74·111·123·215·250·339 |
| seq/nl_transient_s.f.md:166–187 (보완) | 바깥 루프 이름만 기재 | DO 범위와 닫힘 행 명시 | 74·111·123·215·250·339 |
| seq/nl_transient_s.f.md:188–216 (보완) | 바깥 루프 이름만 기재 | DO 범위와 닫힘 행 명시 | 74·111·123·215·250·339 |
| seq/nl_transient_s.f.md:217–255 (보완) | 바깥 루프 이름만 기재 | DO 범위와 닫힘 행 명시 | 74·111·123·215·250·339 |
| seq/nl_transient_s.f.md:256–293 (보완) | 바깥 루프 이름만 기재 | DO 범위와 닫힘 행 명시 | 74·111·123·215·250·339 |
| seq/nl_transient_s.f.md:294–315 (보완) | 바깥 루프 이름만 기재 | DO 범위와 닫힘 행 명시 | 74·111·123·215·250·339 |
| seq/nl_transient_s.f.md:316–341 (보완) | 바깥 루프 이름만 기재 | DO 범위와 닫힘 행 명시 | 74·111·123·215·250·339 |
| seq/nl_transient_s.f.md:166–187 (보완) | 비수렴 조건과 오류 메시지 출력 누락 | 분기 우선순위·WRITE·CALL·ELSE 없음 명시 | 166–171 |
| seq/nl_transient_s.f.md:217–255 (정정) | 순위별 호출을 뭉뚱그림 | I_BCT와 MYRANK 조건 명시 | 217–244 |
| seq/nl_transient_s.f.md:294–315 (보완) | 명령 전송과 OUTPUT의 전체 조건 누락 | 중첩 조건·ELSE 없음·OUTPUT 도달 조건 명시 | 294–310 |
| seq/nl_transient_s.f.md:316–341 (보완) | 순위별 호출을 뭉뚱그림 | MYRANK별 호출과 루프 종료 명시 | 333–339 |
| seq/npflow_s.f.md:33–58 (보완) | ELSE 유무 미표기 | ELSE 없음 명시 | 47–56 |
| seq/npforce_s.f.md:1–27 (정정) | BETA·W4를 재료 가중으로 단정 | RR 첨자와 DT12 계산 관계 명시 | 12–19 |
| seq/npforce_s.f.md:28–62 (정정) | 접촉 추가 구간으로 첨자를 뭉뚱그림 | 반복 범위와 제외 범위 명시 | 28–30 |
| seq/npforce_s.f.md:63–79 (정정) | 항의 물리적 의미 단정 | 실제 배열 연산과 해석 구분 | 65–72 |
| seq/npforce_s.f.md:63–79 (보완) | ELSE 유무 미표기 | ELSE 없음 명시 | 65–75 |
| seq/spcdrhvg_s.f.md:1–23 (정정) | 지정 압력 의미 단정 | INDOP의 정확한 첨자와 조건 명시 | 6–11 |
| src/bcgstb.f.md:1–31 (정정) | X 전체 초기화로 서술 | NEQEXT 선언과 NEQ 호출 범위 구분 | 8·19–23 |
| src/bcgstb.f.md:62–73 (보완) | 비수렴 메시지 출력 누락 | 정상 점프 경로와 WRITE·CALL 순서 구분 | 54–55·61–66 |
| src/bdfhx2.f.md:20–51 (정정) | P·DET·H 의미를 단정 | 호출 사실과 수학적 해석 구분 | 29–32 |
| src/bdyfc.f.md:19–51 (보완) | 바깥·안쪽 분기 사슬의 ELSE 구분 누락 | ITYP에는 없고 ND에는 있음 명시 | 34–50 |
| src/bdyfc.f.md:52–66 (보완) | 바깥 루프 범위·닫힘 누락 | DO 범위와 CONTINUE 레이블 행 명시 | 19·64 |
| src/beam0.f.md:1–14 (정정) | 응력·구성행렬 의미 단정 | 선언된 배열 이름·크기로 서술 | 3–4 |
| src/beam0.f.md:15–23 (정정) | SY 절댓값으로 잘못 서술 | SY에 S(1)의 절댓값 대입 명시 | 17–18 |
| src/beam2.f.md:1–14 (정정) | 응력·구성행렬 의미 단정 | 선언된 배열 이름·크기로 서술 | 3–4 |
| src/beam2.f.md:15–23 (정정) | 응력 의미 단정 | 정확한 대입 대상으로 서술 | 19 |
| src/blmbm.f.md:1–15 (정정) | 변형률 행렬 의미 단정 | 실제 선언 배열로 서술 | 3–5 |
| src/blmbm.f.md:16–32 (보완) | RETURN 경로를 행 번호로만 지시 | 실제 조건식과 도달 조건 명시 | 14–16 |
| partition/part_send_tblx1.f.md:401–441 (정정) | NODGX와 IEQX 모두에 절점 번호를 넣는 요약 | KG와 IVRQ(KG)의 저장 대상 구분 | 417–427 |
| partition/part_send_tblx1.f.md:345–400 (보완) | 구간 끝의 바깥 블록을 이름만 기재 | 범위·조건과 닫힘 행 명시 | 345·353·357·367·397·411·430·438·440 |
| partition/part_send_tblx1.f.md:543–582 (정정) | 모서리 의미 단정 | 실제 루프 범위로 서술 | 560–562 |
| partition/metis_partition.c.md:1–21 (정정) | 외부 함수·인수 의미를 근거 없이 단정 | 실제 변수 초기화와 함수명 해석 구분 | 7–11·19–20 |
| seq/mkindex_s.f.md:263–324 (정정) | 외부 라이브러리 설정 의미를 단정 | 실제 필드와 값으로 서술 | 265–273 |
| seq/mkindex_s.f.md:263–324 (정정) | JOB·INFOG 의미를 단정 | 호출·대입 사실과 해석 구분 | 297–320 |
| seq/gnpflw_s.f.md:17–46 및 후속 사실 (정정) | 후속 사실에서 변위·시간 의미를 단정 | UG 배열의 차분 연산으로 서술 | 21–25 |
| seq/mkindex_s.f.md:82–128 및 후속 사실 (정정) | 후속 사실에서 침투 경로로 단정 | 실제 CASE 조건으로 서술 | 25·82·97 |
| seq/npflow_s.f.md:1–32 및 후속 사실 (정정) | 후속 사실에서 수직 방향을 단정 | 세 번째 배열 성분과 설명 부재로 서술 | 10 |
| seq/npforce_s.f.md:63–79 및 후속 사실 (정정) | 후속 사실에서 압력력 의미를 단정 | 실제 차감 배열과 행으로 서술 | 65–77 |
| src/beam2.f.md:15–23 및 후속 사실 (정정) | 후속 사실에서 응력 의미를 단정 | 정확한 대입 대상으로 서술 | 15–20 |

정정 63, 보완 26, 이상 없음 71
