# CADMAS-SURF code-23 전수 대조

기록 경로 기준: `_staging/recovery/read/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/`.
원문은 각 기록 frontmatter의 `file:`이다.
각 구간을 `nl -ba <원문> | sed -n 'A,Bp'`로 열어 의미와 인용을 대조했다.
원문 행 수는 공백·주석을 포함한다.
정정·보완 수는 종류별 변경 위치 수이다.
같은 위치의 같은 종류 수정은 한 건으로 센다.
이상 없음 수는 정정·보완이 없는 구간 표 행 수이다.
후속 사실의 변경은 별도 위치로 센다.

| 기록 | 대조 구간 행 수 | 대조 원문 행 수 | 상태 |
|---|---:|---:|---|
| Count_data/Ct_TSTEP.f.md | 2 | 21 | 완료 |
| Count_data/endt.f.md | 1 | 14 | 완료 |
| Count_data/tb_end.f.md | 1 | 19 | 완료 |
| Read_data/Rd_BCTSET.f.md | 2 | 30 | 완료 |
| Read_data/Rd_BSURFS.f.md | 2 | 34 | 완료 |
| Read_data/Rd_CONTACT.f.md | 1 | 11 | 완료 |
| Read_data/Rd_CORD2C.f.md | 1 | 14 | 완료 |
| Read_data/Rd_CORD2R.f.md | 1 | 14 | 완료 |
| Read_data/Rd_FORCE.f.md | 1 | 19 | 완료 |
| Read_data/Rd_FRIC.f.md | 1 | 23 | 완료 |
| Read_data/Rd_GRAV.f.md | 1 | 11 | 완료 |
| Read_data/Rd_GRID.f.md | 1 | 19 | 완료 |
| Read_data/Rd_LOAD.f.md | 2 | 38 | 완료 |
| Read_data/Rd_MAT1.f.md | 2 | 49 | 완료 |
| Read_data/Rd_MAT9.f.md | 2 | 35 | 완료 |
| Read_data/Rd_MATS1.f.md | 2 | 29 | 완료 |
| Read_data/Rd_MATT1.f.md | 1 | 15 | 완료 |
| Read_data/Rd_MPC.f.md | 2 | 43 | 완료 |
| Read_data/Rd_NLPARM.f.md | 2 | 37 | 완료 |
| Read_data/Rd_PARAM.f.md | 1 | 31 | 완료 |
| Read_data/Rd_PBAR.f.md | 1 | 26 | 완료 |
| Read_data/Rd_PBARL.f.md | 1 | 27 | 완료 |
| Read_data/Rd_PLOAD.f.md | 1 | 13 | 완료 |
| Read_data/Rd_PLOAD1.f.md | 1 | 25 | 완료 |
| Read_data/Rd_PLOAD2.f.md | 1 | 27 | 완료 |
| Read_data/Rd_PLOAD4.f.md | 2 | 38 | 완료 |
| Read_data/Rd_REST.f.md | 1 | 16 | 완료 |
| Read_data/Rd_RFORCE.f.md | 1 | 11 | 완료 |
| Read_data/Rd_RLOAD1.f.md | 2 | 30 | 완료 |
| Read_data/Rd_SHELL.f.md | 1 | 13 | 완료 |
| Read_data/Rd_SOLID.f.md | 2 | 26 | 완료 |
| Read_data/Rd_SPC.f.md | 1 | 20 | 완료 |
| Read_data/Rd_SPC1.f.md | 2 | 62 | 완료 |
| Read_data/Rd_SPCADD.f.md | 2 | 34 | 완료 |
| Read_data/Rd_SUBCASE.f.md | 2 | 58 | 완료 |
| Read_data/Rd_TABLEM1.f.md | 1 | 22 | 완료 |
| Read_data/Rd_TEMP.f.md | 1 | 17 | 완료 |
| Read_data/Rd_TEMPD.f.md | 1 | 16 | 완료 |
| Read_data/Rd_TEMPP1.f.md | 3 | 73 | 완료 |
| Read_data/Rd_TLOAD1.f.md | 1 | 29 | 완료 |
| Read_data/Rd_TSTEP.f.md | 2 | 30 | 완료 |
| Read_data/Rd_TSTEPNL.f.md | 1 | 30 | 완료 |
| Read_data/Read_data.f.md | 23 | 858 | 완료 |
| Read_data/get_comm.f.md | 2 | 26 | 완료 |
| Read_data/inqtxt.f.md | 1 | 15 | 완료 |
| Read_data/resfr.f.md | 1 | 13 | 완료 |
| Read_data/thru.f.md | 1 | 14 | 완료 |
| Set_table/Set_table.f.md | 16 | 373 | 완료 |
| Set_table/St_BCTPARA.f.md | 1 | 22 | 완료 |
| Set_table/St_BCTSET.f.md | 2 | 30 | 완료 |

완료 기록 50개에서 구간 표 107행과 원문 2500행을 대조했다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| Read_data/Rd_BSURFS.f.md:1–13 (정정) | IE·IG를 요소·격자점 번호로 단정 | 해당 구간에서 확인되는 변수명으로 기술 | 7 |
| Read_data/Rd_BSURFS.f.md:14–34 (정정) | IE·IG의 물리적 의미 단정 | 조건과 저장 대상의 변수명을 명시 | 20–25 |
| Read_data/Rd_CORD2C.f.md:1–14 (정정) | ICRD·CORD 의미를 사실로 단정; CORD를 좌표로 단정 | 좌표계 의미를 해석으로 구분; 실제 입력 배열 범위로 기술 | 5–10; 9–10 |
| Read_data/Rd_CORD2R.f.md:1–14 (정정) | ICRD·CORD 의미를 사실로 단정; CORD를 좌표로 단정 | 좌표계 의미를 해석으로 구분; 실제 입력 배열 범위로 기술 | 5–10; 9–10 |
| Read_data/Rd_FORCE.f.md:1–19 (정정) | F·RN을 크기·방향으로 단정 | 입력 변수명으로 기술 | 7–11 |
| Read_data/Rd_FORCE.f.md:1–19 (보완) | ELSE 부재 설명 누락 | 두 조건이 모두 거짓일 때 R_FRC 미대입을 명시 | 13–17 |
| Read_data/Rd_FRIC.f.md:1–23 (보완) | ELSE 부재 설명 누락 | 모든 조건이 거짓이면 읽기 없음 | 7–21 |
| Read_data/Rd_LOAD.f.md:1–17 (정정) | 입력값을 전체 배율·하중 번호로 단정 | 실제 입력 변수와 쌍의 수를 기술 | 8–9 |
| Read_data/Rd_MAT1.f.md:1–17 (정정) | POR·AMAT(3)·상수의 물리적 의미 단정 | 변수명과 식의 상수로 기술 | 8–16 |
| Read_data/Rd_MAT1.f.md:18–49 (정정) | 혼합 밀도로 단정 | AMAT(3) 재계산으로 기술 | 37 |
| Read_data/Rd_MPC.f.md:1–20 (정정) | IG·IC·A 의미 단정 | 실제 입력 변수명으로 기술 | 8–9 |
| Read_data/Rd_LOAD.f.md:후속 사실 12·25 (정정) | 하중 번호로 단정 | L(I) 조건으로 기술 | 12·25 |
| Read_data/Rd_MAT1.f.md:후속 사실 16·34–37 (정정) | 혼합 밀도·환산으로 단정 | 대입 대상과 연산으로 기술 | 16·34–37 |
| Read_data/Rd_PARAM.f.md:1–31 (보완) | ELSE 부재 본문 누락 | 외부·내부 사슬의 ELSE 부재와 미대입 반환 명시 | 8–28 |
| Read_data/Rd_PBARL.f.md:1–27 (보완) | ELSE 부재 누락 및 형상으로 표현 | 문자열 검색과 불일치 시 다음 반복 명시 | 9–20 |
| Read_data/Rd_PLOAD.f.md:1–13 (정정) | P·IG의 물리적 의미 단정 | 실제 입력 변수로 기술 | 7 |
| Read_data/Rd_PLOAD1.f.md:1–25 (정정) | 하중·방향으로 의미 단정 | 입력 변수와 검색 문자열로 기술 | 7–18 |
| Read_data/Rd_PLOAD1.f.md:1–25 (보완) | ELSE 부재 설명 누락 | 불일치 시 다음 반복 명시 | 10–20 |
| Read_data/Rd_PLOAD2.f.md:1–27 (정정) | 압력·요소 범위로 의미 단정 | 조건과 실제 입력·저장 변수로 기술 | 8–23 |
| Read_data/Rd_PLOAD4.f.md:1–17 (정정) | 요소 범위로 의미 단정 | 입력 변수와 IDE2 대입으로 기술 | 9–15 |
| Read_data/Rd_PLOAD4.f.md:18–38 (정정) | 좌표계·방향·요소 범위로 단정 | 입력·저장 변수로 기술 | 21–33 |
| Read_data/Rd_REST.f.md:1–16 (보완) | ELSE 부재 누락 | 불일치 시 IP·RTIM 미변경 명시 | 7–14 |
| Read_data/Rd_RLOAD1.f.md:1–23 (보완) | ELSE 부재 본문 누락 | 불일치 시 기본값 유지 명시 | 9–21 |
| Read_data/Rd_PLOAD4.f.md:후속 사실 10·14·20–36 (정정) | 압력·방향으로 단정 및 RN 기본값 설명 누락 | 실제 입력 변수와 기본값 분기 명시 | 10·14·20–36 |
| Read_data/Rd_BSURFS.f.md:후속 사실 21 (정정) | 요소 번호로 의미 단정 | IE(I) 조건으로 기술 | 21·27–29 |
| Read_data/Rd_SPC.f.md:1–20 (정정) | 물리적 의미 및 RESFR 내부 동작 무근거 단정 | 실제 입력·저장 변수와 호출 인수로 기술 | 8–17 |
| Read_data/Rd_SPC1.f.md:1–35 (정정) | 격자점·성분·범위 의미 단정 | 실제 변수와 저장 위치로 기술 | 9–31 |
| Read_data/Rd_SPC1.f.md:36–62 (정정) | 격자점으로 의미 단정 | 입력 배열 범위로 기술 | 40–42 |
| Read_data/Rd_SPCADD.f.md:1–14 (정정) | 집합·하위 번호로 의미 단정 | 실제 입력 변수로 기술 | 7 |
| Read_data/Rd_SUBCASE.f.md:1–18 (정정) | GET_COMM 내부 의미를 외부 근거 없이 기술 | 호출 이후 실제 IP 조건으로 기술 | 15–17 |
| Read_data/Rd_SUBCASE.f.md:19–58 (보완) | 바깥 DO 원문·닫힘 및 ELSE 부재 설명 누락 | 바깥 DO와 닫힘 행 및 미인식 처리 명시 | 6·19–56 |
| Read_data/Rd_TABLEM1.f.md:1–22 (정정) | 두 좌표로 의미 단정 및 인덱스 요약 | 복사 대상 인덱스와 변수 명시 | 14–16 |
| Read_data/Rd_TEMP.f.md:1–17 (정정) | 집합·격자점·온도로 의미 단정 | 입력·저장 변수명으로 기술 | 7–14 |
| Read_data/Rd_TEMPD.f.md:1–16 (정정) | 집합·기본 온도로 의미 단정 | 입력 변수로 기술 | 7 |
| Read_data/Rd_SPC1.f.md:후속 사실 19·26·36–38 (정정) | 0 격자점으로 의미 단정 | IG(I) 조건으로 기술 | 19·26·36–38 |
| Read_data/Rd_SPC1.f.md:후속 사실 45·55 (정정) | 0 격자점으로 의미 단정 | IG(I) 조건으로 기술 | 45·55 |
| Read_data/Rd_TEMPP1.f.md:1–22 (정정) | 온도 입력으로 단정; 요소의 시작·끝 번호로 단정 | T1·T2 입력 위치로 기술; 실제 대입 대상과 값 명시 | 12–17; 20–21 |
| Read_data/Rd_TEMPP1.f.md:23–56 (정정) | 요소 범위로 단정 | 실제 읽기·저장 배열과 인덱스로 기술 | 29–52 |
| Read_data/Rd_TEMPP1.f.md:57–73 (보완) | 바깥 블록 조건식·닫힘 행 누락 | DO·IF 원문과 닫힘 위치 명시 | 23·27·55·69·71 |
| Read_data/Rd_TLOAD1.f.md:1–29 (보완) | ELSE 부재 본문 누락 | 불일치 시 기본값 유지 명시 | 9–21 |
| Read_data/Rd_TSTEP.f.md:1–12 (정정) | 입력값을 단계·시간·출력 간격으로 단정 | 입력 변수와 기본값 대상 명시 | 9–11 |
| Read_data/Rd_TSTEP.f.md:13–30 (정정) | 입력값 의미 단정 | 입력 변수와 기본값 대상 명시 | 19–21 |
| Read_data/Rd_TEMPP1.f.md:후속 사실 50·57–67 (정정) | 요소 번호·온도값으로 단정 | 실제 조건·변수·대입 범위 명시 | 50·57–67 |
| Read_data/Read_data.f.md:11–72 (보완) | 내부 분기 사슬 ELSE 부재 누락 | 실행·주석 사슬의 ELSE 부재 명시 | 35–47·60–67 |
| Read_data/Read_data.f.md:73–99 (정정) | 좌표계 개수·역참조표 용도 단정 | 대입·할당 변수로 기술 | 86–98 |
| Read_data/Read_data.f.md:100–148 (정정) | 배열의 요소 종류 단정 | 구간 내 배열 할당으로 기술 | 119–145 |
| Read_data/Read_data.f.md:149–200 (정정) | 스프링 용도로 단정 | 실제 배열 할당으로 기술 | 149–154 |
| Read_data/Read_data.f.md:454–514 (정정) | 두 기록 위치도 할당한다고 기술 | 배열 할당과 스칼라 초기화를 구분 | 504–513 |
| Read_data/Read_data.f.md:515–556 (정정) | NNSTP를 연속 항목 수로 제한 | 실제 대입값과 저장 위치로 기술 | 530–534 |
| Read_data/Read_data.f.md:629–668 (보완) | 바깥 블록을 이름만 표기 | DO·IF 원문과 닫힘 행을 명시 | 596·600·854·856 |
| Read_data/Read_data.f.md:669–701 (보완) | 바깥 블록을 이름만 표기 | DO·IF 원문과 닫힘 행을 명시 | 596·600·854·856 |
| Read_data/Read_data.f.md:702–724 (보완) | 바깥 블록을 이름만 표기 | DO·IF 원문과 닫힘 행을 명시 | 596·600·854·856 |
| Read_data/Read_data.f.md:725–760 (보완) | 바깥 블록을 이름만 표기; 다른 루틴의 증분 동작에 근거 위치 없음 | DO·IF 원문과 닫힘 행 명시; 이미 대조한 RD_PLOAD2의 증분 행 인용 | 596·600·854·856; 743; Rd_PLOAD2.f:10·19 |
| Read_data/Read_data.f.md:761–797 (보완) | 바깥 블록을 이름만 표기 | DO·IF 원문과 닫힘 행 명시 | 596·600·854·856 |
| Read_data/Read_data.f.md:798–832 (보완) | 바깥 블록을 이름만 표기 | DO·IF 원문과 닫힘 행 명시 | 596·600·854·856 |
| Read_data/Read_data.f.md:833–858 (보완) | 바깥 블록을 이름만 표기 | DO·IF 원문과 닫힘 행 명시 | 596·600·854·856 |
| Read_data/Read_data.f.md:833–858 (정정) | J_BCTP·R_BCTP 읽기 수량 불명확 | 정수 한 성분과 실수 두 성분 구분 | 582–583·841–843 |
| Set_table/Set_table.f.md:1–13 (정정) | KK(8)·ICRDR 용도를 구간 내 근거 없이 단정 | 루프 범위와 실제 첨자 대입 명시 | 10–11 |
| Set_table/Set_table.f.md:14–38 (정정) | 요소 종류·속성 의미 단정 | 원문 대입 변수 대응 명시 | 16–24 |
| Set_table/Set_table.f.md:39–64 (정정) | 인수 용도를 구간 내 근거 없이 단정 | 실제 호출 인수와 순서로 기술 | 57–63 |
| Set_table/Set_table.f.md:98–119 (정정) | 다른 루틴의 집합 수 계산을 근거 없이 단정; ST_SID에도 INDGR를 전달하는 것으로 읽히는 요약 | 호출 인수와 대입으로 기술; INDGR는 ST_SPC에만 전달함을 명시 | 100–101; 113–115 |
| Set_table/Set_table.f.md:120–141 (정정) | SID_COUNT 내부 동작 단정; ST_SID에도 ICRDR·INDGR 전달로 잘못 기술 | 호출 인수로 기술; 두 호출의 인수 구분 | 122–123; 135–137 |
| Set_table/Set_table.f.md:142–171 (정정) | 다른 루틴의 집합 수·항목 수 계산 단정 | 실제 호출 인수와 후속 저장 명시 | 152–156 |
| Set_table/Set_table.f.md:172–197 (정정) | SID_COUNT 내부 동작 단정; ST_SID에도 IELR 전달로 잘못 기술 | 호출 인수와 대입으로 기술; IELR는 ST_PLOAD1에만 전달함을 명시 | 174–175; 187–189 |
| Set_table/Set_table.f.md:198–216 (정정) | 온도 입력으로 의미 단정 | 실제 호출 인수로 기술 | 209–210 |
| Set_table/Set_table.f.md:217–235 (정정) | SID_COUNT 내부 집합 수 계산 단정 | 호출 인수와 후속 저장으로 기술 | 219–221 |
| Set_table/Set_table.f.md:236–275 (정정) | SID_COUNT·TB_COUNT 내부 계산 단정 | 호출 인수와 후속 저장으로 기술 | 238–242 |
| Set_table/Set_table.f.md:276–302 (정정) | SID_COUNT 내부 집합 수 계산 단정 | 호출 인수와 대입으로 기술 | 278–280 |
| Set_table/Set_table.f.md:303–333 (정정) | 내부 표 번호 및 SID_COUNT 내부 계산 단정; ST_SID에도 IELR·INDGR 전달로 잘못 기술 | 첨자 계산·호출 인수로 기술; 두 호출의 인수를 구분 | 305–315; 328–332 |
| Set_table/Set_table.f.md:334–362 (정정) | 접촉 쌍 및 SID_COUNT 내부 동작 단정 | 호출 인수와 대입으로 기술 | 336–337 |
| Set_table/Set_table.f.md:후속 사실 305–310·363–371 (정정) | 동적 하중의 표 번호로 의미 단정 | 대입 대상 명시 및 역참조표 주석 근거 명시 | 305–310·363–371 |
| Set_table/St_BCTPARA.f.md:1–22 (정정) | 접촉 쌍으로 의미 단정 | 실제 루프 인덱스 범위로 기술 | 7 |
| Set_table/St_BCTSET.f.md:1–25 (정정) | 두 표면 번호로 의미 단정 | 실제 복사 대상과 인덱스로 기술 | 15–16 |
| Set_table/St_BCTSET.f.md:26–30 (정정) | 표면·내부 번호로 의미 단정 | 실제 첨자 계산과 대입으로 기술 | 27 |

대상 기록 50개가 모두 완료되었다.
수정한 기록은 30개이다.
위 기록별 표에서 대조한 구간 표 행 수의 합은 107이다.
위 기록별 표에서 대조한 원문 행 수의 합은 2500이다.
원문 50개의 SHA-256은 각 기록 frontmatter와 일치했다.
원문의 빈 행과 내용 없는 `C` 주석을 제외한 모든 행은 해당 구간의 백틱 인용에 포함되어 있다.
행 번호가 붙은 원문 인용은 해당 원문 행과 일치했다.
작업 시작 시점과 비교한 frontmatter 및 구간 경계는 동일하다.
실제 수정 표식 집계는 아래 최종 집계와 일치했다.
모델은 실행하지 않았다.

정정 56, 보완 18, 이상 없음 44
