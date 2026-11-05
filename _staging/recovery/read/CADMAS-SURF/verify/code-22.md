# CADMAS-SURF code-22 전수 대조

검증일: 2026-11-04.
상태: 지정된 기록 50개를 모두 대조했다.
대조 범위는 각 기록의 frontmatter `file:`이 지정한 원문이다.
각 구간을 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
각 출력 구간은 200행 이하이다.
원문의 빈 행과 주석 행도 대조 행 수에 포함했다.
구간 경계와 frontmatter는 유지했다.
원문과 노트와 git은 수정하지 않았다.
모델은 실행하지 않았다.

아래 기록 경로의 기준은 `_staging/recovery/read/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/`이다.
변경 목록의 원문 행은 해당 기록의 `file:` 경로에 속한다.

기록별 대조 결과:

| 기록 | 대조한 구간 행 수 | 대조한 원문 행 수 | 원문 범위 | 정정 | 보완 | 이상 없는 구간 행 수 | 상태 |
|---|---:|---:|---|---:|---:|---:|---|
| glb_comm/ens_geom0.f.md | 2 | 19 | 1–19 | 0 | 0 | 2 | 완료·이상 없음 |
| glb_comm/femap_out0.f.md | 2 | 26 | 1–26 | 0 | 0 | 2 | 완료·이상 없음 |
| glb_comm/fmp_bar0.f.md | 3 | 52 | 1–52 | 0 | 0 | 3 | 완료·이상 없음 |
| glb_comm/fmp_nodal0.f.md | 5 | 184 | 1–184 | 0 | 0 | 5 | 완료·이상 없음 |
| glb_comm/fmp_ous0.f.md | 2 | 24 | 1–24 | 1 | 0 | 2 | 완료 |
| glb_comm/fmp_rod0.f.md | 3 | 52 | 1–52 | 0 | 0 | 3 | 완료·이상 없음 |
| glb_comm/fmp_soil0.f.md | 2 | 43 | 1–43 | 0 | 0 | 2 | 완료·이상 없음 |
| glb_comm/fmp_sol0.f.md | 3 | 67 | 1–67 | 0 | 0 | 3 | 완료·이상 없음 |
| glb_comm/fric_updt.f.md | 3 | 44 | 1–44 | 0 | 0 | 3 | 완료·이상 없음 |
| glb_comm/fricchk0.f.md | 3 | 66 | 1–66 | 1 | 1 | 1 | 완료 |
| glb_comm/gather_nodal_d.f.md | 2 | 24 | 1–24 | 0 | 0 | 2 | 완료·이상 없음 |
| glb_comm/gather_nodal_i.f.md | 2 | 24 | 1–24 | 0 | 0 | 2 | 완료·이상 없음 |
| glb_comm/gather_surface.f.md | 2 | 24 | 1–24 | 0 | 0 | 2 | 완료·이상 없음 |
| glb_comm/glb_comm.f.md | 4 | 68 | 1–68 | 0 | 2 | 2 | 완료 |
| glb_comm/islv_updt.f.md | 4 | 102 | 1–102 | 2 | 0 | 2 | 완료 |
| glb_comm/istchk0.f.md | 5 | 124 | 1–124 | 1 | 1 | 3 | 완료 |
| glb_comm/mdpress0.f.md | 4 | 105 | 1–105 | 1 | 0 | 3 | 완료 |
| glb_comm/npflow0.f.md | 2 | 20 | 1–20 | 0 | 0 | 2 | 완료·이상 없음 |
| glb_comm/outnod0.f.md | 5 | 116 | 1–116 | 0 | 0 | 5 | 완료·이상 없음 |
| glb_comm/output0.f.md | 5 | 98 | 1–98 | 0 | 0 | 5 | 완료·이상 없음 |
| glb_comm/outsoil0.f.md | 2 | 18 | 1–18 | 1 | 0 | 1 | 완료 |
| glb_comm/outsol0.f.md | 3 | 33 | 1–33 | 2 | 0 | 1 | 완료 |
| glb_comm/rd_restart0.f.md | 2 | 29 | 1–29 | 0 | 0 | 2 | 완료·이상 없음 |
| glb_comm/rdpress0.f.md | 7 | 211 | 1–211 | 0 | 1 | 6 | 완료 |
| glb_comm/recv_pres0.f.md | 3 | 44 | 1–44 | 1 | 0 | 2 | 완료 |
| glb_comm/recv_rst0.f.md | 1 | 11 | 1–11 | 1 | 0 | 0 | 완료 |
| glb_comm/recv_surf0.f.md | 5 | 142 | 1–142 | 1 | 1 | 3 | 완료 |
| glb_comm/remesh0.f.md | 3 | 53 | 1–53 | 2 | 0 | 1 | 완료 |
| glb_comm/resfrc0.f.md | 3 | 51 | 1–51 | 0 | 0 | 3 | 완료·이상 없음 |
| glb_comm/rmsh_init0.f.md | 5 | 115 | 1–115 | 0 | 1 | 4 | 완료 |
| glb_comm/scatter_nodal_d.f.md | 2 | 24 | 1–24 | 0 | 0 | 2 | 완료·이상 없음 |
| glb_comm/scatter_nodal_i.f.md | 2 | 24 | 1–24 | 0 | 0 | 2 | 완료·이상 없음 |
| glb_comm/scatter_surface.f.md | 2 | 24 | 1–24 | 0 | 0 | 2 | 완료·이상 없음 |
| glb_comm/send_cont0.f.md | 2 | 34 | 1–34 | 0 | 0 | 2 | 완료·이상 없음 |
| glb_comm/send_pos0.f.md | 2 | 20 | 1–20 | 0 | 0 | 2 | 완료·이상 없음 |
| glb_comm/stickchk0.f.md | 5 | 103 | 1–103 | 1 | 3 | 2 | 완료 |
| glb_comm/wt_restart0.f.md | 3 | 62 | 1–62 | 1 | 0 | 2 | 완료 |
| input/Count_data/Count_data.f.md | 7 | 226 | 1–226 | 0 | 5 | 2 | 완료 |
| input/Count_data/Ct_BCTSET.f.md | 2 | 21 | 1–21 | 1 | 0 | 2 | 완료 |
| input/Count_data/Ct_BSURFS.f.md | 2 | 26 | 1–26 | 0 | 0 | 2 | 완료·이상 없음 |
| input/Count_data/Ct_LOAD.f.md | 2 | 31 | 1–31 | 1 | 0 | 1 | 완료 |
| input/Count_data/Ct_MPC.f.md | 2 | 26 | 1–26 | 1 | 0 | 1 | 완료 |
| input/Count_data/Ct_PLOAD2.f.md | 1 | 17 | 1–17 | 0 | 0 | 1 | 완료·이상 없음 |
| input/Count_data/Ct_SPC.f.md | 1 | 14 | 1–14 | 0 | 0 | 1 | 완료·이상 없음 |
| input/Count_data/Ct_SPC1.f.md | 2 | 36 | 1–36 | 1 | 0 | 1 | 완료 |
| input/Count_data/Ct_SPCADD.f.md | 2 | 31 | 1–31 | 1 | 0 | 1 | 완료 |
| input/Count_data/Ct_TABLEM1.f.md | 1 | 12 | 1–12 | 0 | 0 | 1 | 완료·이상 없음 |
| input/Count_data/Ct_TEMP.f.md | 1 | 13 | 1–13 | 1 | 0 | 0 | 완료 |
| input/Count_data/Ct_TEMPD.f.md | 1 | 13 | 1–13 | 1 | 0 | 0 | 완료 |
| input/Count_data/Ct_TEMPP1.f.md | 3 | 36 | 1–36 | 1 | 1 | 1 | 완료 |

정정·보완 목록:

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| glb_comm/fmp_ous0.f.md:코드 사실 6–10 | 수신 프로세스 번호 1 | 수신 호출의 송신원 프로세스 번호 1 [11-04 전수 검증 정정] | 6–10 |
| glb_comm/fricchk0.f.md:13–43 | 0인 상태의 대상이 불명확하고 ELSE 부재 미표시 | IFRIC(1,I)의 0 검사와 GOTO 대상 및 ELSE 부재 명시 [11-04 전수 검증 정정] | 21–43,63 |
| glb_comm/fricchk0.f.md:44–66 | 바깥 루프 이름만 기재 | 바깥 DO 범위와 닫힘 및 ELSE 부재 명시 [11-04 전수 검증 보완] | 13,20,45–49,63–64 |
| glb_comm/glb_comm.f.md:34–57 | 바깥 DO·SELECT 이름만 기재 | SELECT의 선택식과 두 블록의 닫힘 명시 [11-04 전수 검증 보완] | 11,15,64,66 |
| glb_comm/glb_comm.f.md:58–68 | 바깥 DO·SELECT 이름만 기재 | SELECT의 선택식과 두 블록의 닫힘 명시 [11-04 전수 검증 보완] | 11,15,64,66 |
| glb_comm/islv_updt.f.md:44–74 | 소유 프로세스·전역 번호를 근거 없이 단정 | 대입 사실과 번호 의미의 해석을 구분하고 CASE 한정 [11-04 전수 검증 정정] | 50–71 |
| glb_comm/islv_updt.f.md:75–102 | 번호 변환 의미 단정 | 대입 사실과 번호 변환 해석을 구분 [11-04 전수 검증 정정] | 82–96 |
| glb_comm/istchk0.f.md:83–103 | 바깥 I 루프 이름만 기재 | DO 범위와 닫힘 명시 [11-04 전수 검증 보완] | 55,122 |
| glb_comm/istchk0.f.md:104–124 | NNOD 이하를 모두 INDG로 변환 | 양수 조건 복원 및 ELSE 부재·루프 닫힘 명시 [11-04 전수 검증 정정] | 55,106–117,122 |
| glb_comm/mdpress0.f.md:64–89 | PFD·PFND를 압력으로 단정 | 배열 대입 사실과 압력 해석을 구분하고 ELSE 부재 명시 [11-04 전수 검증 정정] | 76–85 |
| glb_comm/outsoil0.f.md:11–18 | 파트 범위를 세 항의 합으로 축약하고 물리량 단정 | IPS의 +1과 IPE의 +NP_ENS(6)을 구분하고 물리량을 해석으로 표시 [11-04 전수 검증 정정] | 11–14 |
| glb_comm/outsol0.f.md:1–16 | 변수의 물리적 의미 단정 | 선언 사실과 물리적 의미 해석 구분 [11-04 전수 검증 정정] | 3–15 |
| glb_comm/outsol0.f.md:17–28 | 응력·변형률·주응력 데이터를 전달한다고 단정 | 실제 인수 배열의 동일성 기술 [11-04 전수 검증 정정] | 22,27 |
| glb_comm/rdpress0.f.md:160–185 | 바깥 IP 루프 이름만 기재 | DO 범위와 닫힘 명시 [11-04 전수 검증 보완] | 141,184 |
| glb_comm/recv_pres0.f.md:31–44 | TNEXT를 다음 시각으로 단정 | 수신·분기 사실과 시각 해석 구분 [11-04 전수 검증 정정] | 36–39 |
| glb_comm/recv_rst0.f.md:1–11 | 재시작 유형으로 단정 | 수신 사실과 값의 용도 해석 구분 [11-04 전수 검증 정정] | 5–6 |
| glb_comm/recv_surf0.f.md:1–36 | 수위로 단정하고 KK(81) 저장을 방송보다 먼저 서술 | 수신·대입·방송 순서 복원 및 물리적 의미 해석 구분 [11-04 전수 검증 정정] | 17–27 |
| glb_comm/recv_surf0.f.md:90–115 | 바깥 IP 루프 이름만 기재 | DO 범위와 닫힘 명시 [11-04 전수 검증 보완] | 71,114 |
| glb_comm/remesh0.f.md:1–26 | DELZ·IFIX 의미 단정 | 수신 사실과 물리적 의미 해석 구분 [11-04 전수 검증 정정] | 21–25 |
| glb_comm/remesh0.f.md:27–40 | IFIX1W를 추가 고정 표시로 단정 | 수신값의 인덱스별 가산 사실 기술 [11-04 전수 검증 정정] | 31–35 |
| glb_comm/rmsh_init0.f.md:82–103 | 바깥 IP 루프 이름만 기재 | DO 범위와 닫힘 명시 [11-04 전수 검증 보완] | 61,102 |
| glb_comm/stickchk0.f.md:48–76 | 바깥 SELECT의 선택식·닫힘 및 GOTO 목표 불명확 | IDYN 선택식·CASE 경계·SELECT 닫힘과 GOTO 목표 명시 [11-04 전수 검증 보완] | 24–25,52–70,87,101 |
| glb_comm/stickchk0.f.md:77–86 | 바깥 SELECT의 선택식·닫힘 및 GOTO 목표 불명확 | IDYN 선택식·CASE 경계·SELECT 닫힘과 GOTO 목표 명시 [11-04 전수 검증 보완] | 24–25,87,101 |
| glb_comm/stickchk0.f.md:87–103 | 바깥 SELECT 이름만 기재 | 선택식과 닫힘 명시 [11-04 전수 검증 보완] | 24,101 |
| glb_comm/stickchk0.f.md:코드 사실 80·96 | IDYN의 동적·정적 의미 단정 | CASE별 조건 사실과 의미 해석 구분 [11-04 전수 검증 정정] | 24–25,80,87,96 |
| glb_comm/wt_restart0.f.md:1–29 | N 양수일 때만 N도 방송한다고 요약 | N의 무조건 방송과 NNOW(N)의 양수 조건을 구분 [11-04 전수 검증 정정] | 16–24 |
| input/Count_data/Count_data.f.md:95–120 | 바깥 DO·IF 사슬 이름만 기재 | IF 시작 조건과 DO·IF 닫힘 및 ELSE 부재 명시 [11-04 전수 검증 보완] | 72,76,222,224 |
| input/Count_data/Count_data.f.md:121–144 | 바깥 DO·IF 사슬 이름만 기재 | IF 시작 조건과 DO·IF 닫힘 및 ELSE 부재 명시 [11-04 전수 검증 보완] | 72,76,222,224 |
| input/Count_data/Count_data.f.md:145–172 | 바깥 DO·IF 사슬 이름만 기재 | IF 시작 조건과 DO·IF 닫힘 및 ELSE 부재 명시 [11-04 전수 검증 보완] | 72,76,222,224 |
| input/Count_data/Count_data.f.md:173–202 | 바깥 DO·IF 사슬 이름만 기재 | IF 시작 조건과 DO·IF 닫힘 및 ELSE 부재 명시 [11-04 전수 검증 보완] | 72,76,222,224 |
| input/Count_data/Count_data.f.md:203–226 | 바깥 DO·IF 사슬 이름만 기재 | IF 시작 조건과 DO·IF 닫힘 및 ELSE 부재 명시 [11-04 전수 검증 보완] | 72,76,222,224 |
| input/Count_data/Ct_BCTSET.f.md:코드 사실 8–19 | 선두 공백으로 축약 | 첫 8열 전체 공백과 첫 글자 + 조건 구분 [11-04 전수 검증 정정] | 4,12 |
| input/Count_data/Ct_LOAD.f.md:14–31 | 선두 공백으로 축약 | 8열 전체 공백과 첫 글자 + 조건 구분 [11-04 전수 검증 정정] | 4,18–23 |
| input/Count_data/Ct_MPC.f.md:9–26 | 선두 공백으로 축약 | 8열 전체 공백과 첫 글자 + 조건 구분 [11-04 전수 검증 정정] | 4,13–18 |
| input/Count_data/Ct_SPC1.f.md:19–36 | 선두 공백으로 축약 | 8열 전체 공백과 첫 글자 + 조건 구분 [11-04 전수 검증 정정] | 5,23–28 |
| input/Count_data/Ct_SPCADD.f.md:14–31 | 선두 공백으로 축약 | 8열 전체 공백과 첫 글자 + 조건 구분 [11-04 전수 검증 정정] | 4,18–23 |
| input/Count_data/Ct_TEMP.f.md:1–13 | IG를 온도 지정 절점 번호로 단정 | 정수 입력 사실과 용도 해석 구분 [11-04 전수 검증 정정] | 4,6 |
| input/Count_data/Ct_TEMPD.f.md:1–13 | ID를 기본 온도 집합 번호로 단정 | 정수 입력 사실과 용도 해석 구분 [11-04 전수 검증 정정] | 4,6 |
| input/Count_data/Ct_TEMPP1.f.md:10–26 | 선두 공백으로 축약 | 8열 전체 공백과 첫 글자 + 조건 구분 [11-04 전수 검증 정정] | 5,14 |
| input/Count_data/Ct_TEMPP1.f.md:27–36 | 바깥 DO·IF 이름만 기재 | IF 조건식과 두 블록의 닫힘 명시 [11-04 전수 검증 보완] | 10,14,27,32,34 |

집계의 기준은 위 표의 기록 50개이다.
대조한 구간 행은 142개이다.
대조한 원문 행은 2,782개이다.
정정 24건은 구간 행 21개와 코드 사실 문단의 행 3개를 센 값이다.
보완 16건은 보완한 구간 행 16개를 센 값이다.
이상 없음 105건은 정정·보완이 필요하지 않았던 구간 행 105개를 센 값이다.
수정이 필요하지 않았던 기록은 기록별 표에서 25개이다.
구간별 인용과 원문의 행 번호를 기계적으로 재확인했다.
원문의 비어 있지 않은 코드 행과 내용 있는 주석 행은 모두 해당 구간에 백틱으로 인용되어 있다.
단일 행 번호가 붙은 원문 인용에서 내용·행 번호 불일치는 없었다.
원문 50개의 SHA-256은 각 frontmatter 값과 일치했다.

정정 24, 보완 16, 이상 없음 105
