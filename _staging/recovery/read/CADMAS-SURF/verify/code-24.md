# CADMAS-SURF code-24 전수 검증

대상은 사용자 지정 기록 50개다.
기록 경로의 공통 접두사는 `_staging/recovery/read/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/`다.
원문은 각 기록 frontmatter의 `file:`이다.
대상 기록 50개의 구간 행 97개를 모두 대조했다.
대조한 원문은 빈 행과 주석을 포함하여 4,213행이다.
원문 구간은 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
각 출력 구간은 200행 이하다.
추가 기계 확인에서 원문 SHA-256과 기록의 해시가 모두 일치했다.
내용이 있는 원문 행의 인용 누락과 인용문·행 번호 불일치는 없었다.
정정·보완 수는 각 표지가 붙은 고유 구간 행 수다.
같은 구간에 두 표지가 있으면 각 항목에 한 번씩 센다.
이상 없음 수는 대조를 마쳤고 두 표지가 모두 없는 구간 행 수다.
모델은 실행하지 않았다.

## 기록별 완료 목록

| 기록 | 대조한 구간 행 수 | 대조한 원문 행 수 | 상태 |
|---|---:|---:|---|
| input/Set_table/St_BSURFS.f.md | 2 | 36 | 완료 |
| input/Set_table/St_ELEM.f.md | 5 | 265 | 완료 |
| input/Set_table/St_FORCE.f.md | 1 | 27 | 완료 |
| input/Set_table/St_MATS1.f.md | 1 | 18 | 완료 |
| input/Set_table/St_MATT1.f.md | 1 | 17 | 완료 |
| input/Set_table/St_MPC.f.md | 1 | 31 | 완료 |
| input/Set_table/St_PLOAD.f.md | 7 | 303 | 완료 |
| input/Set_table/St_PLOAD1.f.md | 1 | 32 | 완료 |
| input/Set_table/St_PLOAD4.f.md | 1 | 46 | 완료 |
| input/Set_table/St_SID.f.md | 1 | 18 | 완료 |
| input/Set_table/St_SPC.f.md | 1 | 30 | 완료 |
| input/Set_table/St_SPC1.f.md | 1 | 35 | 완료 |
| input/Set_table/St_TEMP.f.md | 1 | 33 | 완료 |
| input/Set_table/St_TEMPP1.f.md | 1 | 33 | 완료 |
| input/Set_table/nm_count.f.md | 1 | 26 | 완료 |
| input/Set_table/sid_count.f.md | 1 | 17 | 완료 |
| input/Set_table/sid_count2.f.md | 1 | 21 | 완료 |
| input/Set_table/tb_count.f.md | 1 | 13 | 완료 |
| input/input.f.md | 1 | 16 | 완료 |
| input/data_check.f.md | 6 | 401 | 완료 |
| main/alloc.f.md | 2 | 110 | 완료 |
| main/astea_mechanical.f.md | 3 | 139 | 완료 |
| main/bar_geom.f.md | 1 | 65 | 완료 |
| main/contact_geom.f.md | 1 | 65 | 완료 |
| main/dirinit.f.md | 1 | 15 | 완료 |
| main/elem_init.f.md | 2 | 79 | 완료 |
| main/ens_case.f.md | 2 | 96 | 완료 |
| main/ens_case_t.f.md | 2 | 92 | 완료 |
| main/ens_geom.f.md | 3 | 165 | 완료 |
| main/flnset1.f.md | 1 | 19 | 완료 |
| main/getprm.f.md | 1 | 35 | 완료 |
| main/main.f.md | 2 | 106 | 완료 |
| main/mk_dir.c.md | 1 | 22 | 완료 |
| main/mumps_para.f.md | 1 | 24 | 완료 |
| main/ncgset.f.md | 2 | 81 | 완료 |
| main/part_renum.f.md | 1 | 72 | 완료 |
| main/part_surf.f.md | 1 | 16 | 완료 |
| main/rdpress.f.md | 3 | 139 | 완료 |
| main/rmsh_init.f.md | 3 | 136 | 완료 |
| main/rmsh_initp.f.md | 3 | 152 | 완료 |
| main/rod_geom.f.md | 1 | 65 | 완료 |
| main/rst_cntl.f.md | 3 | 109 | 완료 |
| main/shell_geom.f.md | 2 | 98 | 완료 |
| main/solid_geom.f.md | 2 | 114 | 완료 |
| main/surf_geom.f.md | 2 | 95 | 완료 |
| main/tstepset.f.md | 1 | 41 | 완료 |
| module/dmumps_root.h.md | 2 | 75 | 완료 |
| module/dmumps_struc.h.md | 5 | 265 | 완료 |
| module/input_work.f90.md | 6 | 297 | 완료 |
| module/m_mumps.f90.md | 1 | 8 | 완료 |

## 정정·보완 목록

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| input/Set_table/St_BSURFS.f.md:1–24 | 접촉 영역별 면 목록으로 단정 | 정정: 식별자 비교와 배열 복사로 서술 | 9–24 |
| input/Set_table/St_ELEM.f.md:1–52 | IG=0 종료 범위 모호, 오류 출력 요약 누락 | 정정: 절점 루프 EXIT와 WRITE·ERRSTP 순서 명시 | 33–50 |
| input/Set_table/St_ELEM.f.md:163–217 | 모든 유형의 재료·좌표계 변환 및 꼭짓점·변 중앙으로 단정 | 정정: 변환 조건을 구별하고 가중치 인덱스 조건 명시 | 171–212 |
| input/Set_table/St_FORCE.f.md:1–27 | 힘 6성분·절점·좌표계의 물리적 의미 단정 | 정정: 배열 성분 복사 및 변환 조건으로 서술 | 10–25 |
| input/Set_table/St_MPC.f.md:1–31 | 다점 구속·방정식·절점 의미 단정 | 정정: 용도 해석 구분과 배열 변환 명시 | 1–29 |
| input/Set_table/St_PLOAD.f.md:1–77 | 압력 하중 의미 단정과 전 요소 검색 표현 | 정정: 용도 해석 구별, 첫 일치에서 검색 탈출 및 오류 출력 명시 | 20–72 |
| input/Set_table/St_PLOAD.f.md:1–77 | ELSE 없는 분기 사슬 설명 누락 | 보완: 조건 불일치 시 해당 분기에 실행문 없음 명시 | 25–45,54–58 |
| input/Set_table/St_PLOAD.f.md:151–187 | 반환이 I=2에만 종속되는 표현 | 정정: 부호 반전 조건과 일치 시 반환 구별 | 176–181 |
| input/Set_table/St_PLOAD1.f.md:1–32 | 선 하중 용도 단정 | 정정: 해석으로 구분 | 1–30 |
| input/Set_table/St_PLOAD4.f.md:1–46 | 압력·면 절점·좌표계 의미 단정 | 정정: 용도 해석 구분과 변환 대상 성분 명시 | 1–44 |
| input/Set_table/St_SPC.f.md:1–30 | 단점 구속·절점 의미 단정 | 정정: 용도 해석 구분과 변환 대상 성분 명시 | 1–28 |
| input/Set_table/St_TEMP.f.md:1–33 | 온도 용도 단정 | 정정: 용도 해석 구분 | 1–31 |
| input/Set_table/sid_count2.f.md:1–21 | 온도 세트 의미 단정 | 정정: 검색 배열과 범위로 서술 | 5–19 |
| input/data_check.f.md:1–77 | 파일명과 랭크 대응 생략 | 보완: 랭크 0과 ELSE의 파일명 구별 | 10–15 |
| main/alloc.f.md:1–56 | 접촉 추가 절점·적분점 의미 단정 | 정정: KK 복사 대상과 NGP 값으로 서술 | 8–41 |
| main/alloc.f.md:57–110 | 할당 배열의 물리적 용도 단정 | 정정: 해당 구간에서 확인되는 배열 할당으로 서술 | 57–93 |
| main/astea_mechanical.f.md:63–108 | 접촉 활성로만 조건 요약 | 정정: I_BCT 및 MYRANK의 실제 조건 명시 | 94–108 |
| main/astea_mechanical.f.md:63–108 | 랭크 0·1 외의 동작 설명 누락 | 보완: 랭크 사슬에 마지막 ELSE 없음 명시 | 85–92 |
| main/astea_mechanical.f.md:109–139 | 마지막 랭크 분기의 ELSE 부재 미표시 | 보완: 랭크 0·1 외에는 해당 MPI 호출 없음 명시 | 133–137 |
| main/bar_geom.f.md:1–65 | 좌표와 외부 절점 번호 출력 순서 뒤바뀜 | 정정: 절점 번호 이후 좌표 출력 순서 명시 | 30–48 |
| main/dirinit.f.md:1–15 | 호출 내부 계산과 두 끝 단면 의미 단정 | 정정: 호출·배열 복사는 사실로, 용도는 해석으로 구분 | 6–12 |
| main/elem_init.f.md:1–48 | 비영 랭크 전체가 SEND_KK를 호출하는 요약 | 정정: ALLREDUCE는 MYRANK>0, SEND_KK는 MYRANK==1로 구분하고 D 의미는 해석으로 표시 | 12–46 |
| main/elem_init.f.md:49–79 | SIGY(2,I)를 두 번째 적분점으로 단정 | 정정: 실제 배열 성분으로 서술 | 59–60 |
| main/ens_case.f.md:1–53 | pore_water_flux를 유량으로 단정 | 정정: 출력 변수명과 vector per node 선언에 맞춤 | 50–52 |
| main/ens_case.f.md:54–96 | 초기 0의 무조건 출력 설명 누락 | 보완: 초기 출력과 조건부 단계 출력 구분 | 87–92 |
| main/ens_case_t.f.md:1–55 | pore_water_flux를 유량으로 단정 | 정정: 출력 변수명과 vector per node 선언에 맞춤 | 52–54 |
| main/ens_geom.f.md:132–165 | GSURF 내부 동작을 사실로 단정 | 정정: 호출 인수와 용도 해석 구분 | 144–146 |
| main/main.f.md:56–106 | 바깥 분기 원문 미인용과 ELSE를 나머지 해법으로 한정 | 정정: 바깥 IF 인용과 NPROCS 조건까지 포함한 ELSE 의미 보존 | 29,73,77–97 |
| main/part_renum.f.md:1–72 | 분류에서 열거되지 않은 유형 처리 설명 누락 | 보완: 두 SELECT CASE의 CASE DEFAULT 부재 명시 | 22–29,57–64 |
| main/part_surf.f.md:1–16 | IPFC의 압력 면 용도 단정 | 정정: 복사 사실과 용도 해석 구분 | 3–12 |
| main/rdpress.f.md:1–69 | WLEVEL·ALEVEL 모두 수위로 단정 및 종료 범위 모호 | 정정: 입력 변수 그대로 기술하고 END=10 대상과 이후 대입 명시 | 21–68 |
| main/rdpress.f.md:70–99 | 바깥 IF 인용과 닫힘 위치 누락 | 보완: MYRANK 조건·ELSE·ENDIF 위치 명시 | 11,100,137 |
| main/rdpress.f.md:100–139 | 방송 수신을 랭크 1에 한정하는 요약과 바깥 조건 생략 | 정정: 명령 전송만 랭크 1이며 방송과 반환은 ELSE 전체에 적용 | 11,100–108,137 |
| main/rmsh_init.f.md:1–52 | 면적좌표·허용값 용도 단정 및 분기 순서 압축 | 정정: 함수 인수와 IF/ELSEIF 조건·K 루프 EXIT로 서술 | 34–51 |
| main/rmsh_init.f.md:53–92 | 바깥 블록 조건·닫힘·GOTO 대상 및 오류 출력 요약 미비 | 보완: 바깥 구문과 종료 행, 레이블 10, WRITE·ERRSTP, ELSE/DEFAULT 부재 보완 | 19–91 |
| main/rmsh_init.f.md:93–136 | RZ 수직 의미 단정 및 L을 마지막 면에서 얻었다고 단정 | 정정: RZ 식과 L의 조건부 대입 구별 | 109–134 |
| main/rmsh_init.f.md:93–136 | CASE DEFAULT 부재 누락 | 보완: Z 계산이 N=3·4에만 존재함 명시 | 109–119 |
| main/rmsh_initp.f.md:1–62 | 허용값 의미 단정과 갱신 조건 압축 | 정정: AREAIN 인수·분기 순서·엄격한 크기 비교·EXIT 범위 명시 | 44–61 |
| main/rmsh_initp.f.md:63–102 | 바깥 블록 조건·닫힘·GOTO 대상 및 오류 출력 요약 미비 | 보완: 바깥 구문과 종료 행, 레이블 10, WRITE·ERRSTP, ELSE/DEFAULT 부재 보완 | 30–101 |
| main/rmsh_initp.f.md:103–152 | Z를 높이로 단정 및 L의 조건부 갱신 누락 | 정정: 변수 계산과 마지막 반복값 및 L의 별도 조건 구별 | 118–138 |
| main/rmsh_initp.f.md:103–152 | CASE DEFAULT 부재 누락 | 보완: Z 계산이 N=3·4에만 존재함 명시 | 118–128 |
| main/rst_cntl.f.md:41–79 | 종료 범위가 루틴인지 불명확 | 정정: 무한 DO만 빠져나온 뒤 표시 개수 집계 수행 명시 | 53–78 |
| main/rst_cntl.f.md:80–109 | ELSEIF 구간을 RTIM(2)>0 분기 내부로 표시 | 정정: 선행 조건 거짓·NRST>0 및 마지막 ELSE 부재와 ENDIF 명시 | 45,80–105 |
| main/solid_geom.f.md:58–114 | 절점 교환 분기의 마지막 ELSE 부재 누락 | 보완: ND=15·20 외에는 교환 없이 출력함 명시 | 98–108 |
| main/surf_geom.f.md:1–47 | 이 구간에서 IPFC를 압력 면으로 단정 | 정정: 실제 선택 대상 배열과 조건으로 서술 | 14–35 |
| module/dmumps_root.h.md:48–75 | 성분 이름만으로 크기·역표 의미 단정 | 정정: 선언 사실과 이름을 통한 해석 구분 | 50–60 |
| module/input_work.f90.md:1–64 | 선언만으로 M_* 최대 식별자·역표 의미 단정 | 정정: 선언 사실과 변수 역할 해석 구분 | 5–63 |
| module/input_work.f90.md:65–126 | M_TBM1을 최대 식별자로 단정 | 정정: 선언된 변수명으로 서술 | 112–118 |
| module/input_work.f90.md:228–269 | M_TBD1·ITBD1R 역할 단정 | 정정: 해당 구간의 형식 선언으로 서술 | 249–255 |
| module/input_work.f90.md:270–297 | M_BSRF·ICRGR의 최대 식별자·접촉 역표 의미 단정 | 정정: 정수 및 포인터 선언으로 서술 | 288–297 |
| input/Set_table/St_PLOAD.f.md:188–227 | 반환을 I>=7에 종속시키는 표현 | 정정: 부호 반전 조건과 일치 시 반환을 구분 | 214–221 |
| input/Set_table/St_PLOAD.f.md:78–111 | 요소 형상 또는 P의 물리적 의미 단정 | 정정: 형상별 용도는 해석으로 구분하고 부호 반전 변수는 P로 명시 | 78–110 |
| input/Set_table/St_PLOAD.f.md:112–150 | 요소 형상 또는 P의 물리적 의미 단정 | 정정: 형상별 용도는 해석으로 구분하고 부호 반전 변수는 P로 명시 | 112–149 |
| input/Set_table/St_PLOAD.f.md:151–187 | 요소 형상 또는 P의 물리적 의미 단정 | 정정: 형상별 용도는 해석으로 구분하고 부호 반전 변수는 P로 명시 | 151–186 |
| input/Set_table/St_PLOAD.f.md:188–227 | 요소 형상 또는 P의 물리적 의미 단정 | 정정: 형상별 용도는 해석으로 구분하고 부호 반전 변수는 P로 명시 | 188–226 |
| input/Set_table/St_PLOAD.f.md:228–264 | 요소 형상 또는 P의 물리적 의미 단정 | 정정: 형상별 용도는 해석으로 구분하고 부호 반전 변수는 P로 명시 | 228–263 |
| input/Set_table/St_PLOAD.f.md:265–303 | 요소 형상 또는 P의 물리적 의미 단정 | 정정: 형상별 용도는 해석으로 구분하고 부호 반전 변수는 P로 명시 | 265–303 |

정정 43, 보완 12, 이상 없음 46
