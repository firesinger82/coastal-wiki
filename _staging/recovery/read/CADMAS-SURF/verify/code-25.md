# CADMAS-SURF code-25 전수 검증 (11-04)

기록 경로 기준: `_staging/recovery/read/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/`.
원문 경로 기준: `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/`.

구간 행 수는 각 기록의 구간 표에서 센 값이다. 원문 행 수는 해당 구간의 끝 행에서 시작 행을 빼고 1을 더한 값의 합이다.
정정·보완은 아래 변경 목록의 항목 수이다. 이상 없음은 변경하지 않은 완료 구간 행 수이다.
원문은 각 구간마다 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다. 한 번에 200행을 넘기지 않았다.
모델은 실행하지 않았다. 원문·노트·git은 수정하지 않았다.

집계: 대상 기록 50개, 구간 행 109개, 원문 3,219행을 대조했다. 구간 표 아래 코드 사실 59개도 대조했다.
백틱 원문 인용 2,391개의 문구와 행 번호는 원문과 일치했다. 의미가 있는 비공백 원문 행의 인용 누락은 없었다. 빈 줄과 구분용 주석 행도 구간 대조에 포함했다.
frontmatter와 구간 경계는 최초 기록과 같았다. 각 원문의 SHA-256은 frontmatter 값과 일치했다.

상태: 전체 완료.

| 기록 | 대조한 구간 행 수 | 대조한 원문 행 수 | 상태 |
|---|---:|---:|---|
| module/m_part.f90.md | 3 | 75 | 완료 |
| module/m_val.f90.md | 6 | 300 | 완료 |
| module/mavbl.f90.md | 1 | 9 | 완료 |
| module/mod_comm.f90.md | 8 | 342 | 완료 |
| module/mpc_work.f90.md | 1 | 35 | 완료 |
| module/mpi_param.f90.md | 1 | 10 | 완료 |
| module/mused.f90.md | 6 | 262 | 완료 |
| mpi_comm/c_mpi_allreduce_i.f.md | 1 | 12 | 완료 |
| mpi_comm/c_mpi_barrier.f.md | 1 | 9 | 완료 |
| mpi_comm/c_mpi_init.f.md | 3 | 87 | 완료 |
| mpi_comm/c_mpi_recv_d.f.md | 1 | 14 | 완료 |
| mpi_comm/c_mpi_recv_i.f.md | 1 | 11 | 완료 |
| mpi_comm/c_mpi_send_d.f.md | 1 | 13 | 완료 |
| mpi_comm/c_mpi_send_i.f.md | 1 | 11 | 완료 |
| mpi_comm/c_mpi_waitall.f.md | 1 | 9 | 완료 |
| mpi_comm/cg_mpi_allreduce_d.f.md | 1 | 23 | 완료 |
| mpi_comm/cg_mpi_allreduce_i.f.md | 1 | 22 | 완료 |
| mpi_comm/cg_mpi_irecv_d.f.md | 1 | 14 | 완료 |
| mpi_comm/cg_mpi_irecv_i.f.md | 1 | 14 | 완료 |
| mpi_comm/cg_mpi_isend_d.f.md | 1 | 14 | 완료 |
| mpi_comm/cg_mpi_isend_i.f.md | 1 | 14 | 완료 |
| mpi_comm/comm_cg.f.md | 2 | 58 | 완료 |
| mpi_comm/comm_cg2.f.md | 3 | 71 | 완료 |
| mpi_comm/comm_cg2x.f.md | 3 | 71 | 완료 |
| mpi_comm/comm_cgx.f.md | 2 | 58 | 완료 |
| mpi_comm/comm_dbl.f.md | 2 | 44 | 완료 |
| mpi_comm/comm_dblx.f.md | 2 | 44 | 완료 |
| mpi_comm/comm_intx.f.md | 2 | 44 | 완료 |
| mpi_comm/comm_tblx.f.md | 7 | 345 | 완료 |
| mpi_comm/m_mpi_bcast_d.f.md | 1 | 13 | 완료 |
| mpi_comm/m_mpi_bcast_i.f.md | 1 | 11 | 완료 |
| mpi_comm/m_mpi_recv_d.f.md | 1 | 14 | 완료 |
| mpi_comm/m_mpi_recv_i.f.md | 1 | 11 | 완료 |
| mpi_comm/m_mpi_reduce_d.f.md | 1 | 23 | 완료 |
| mpi_comm/m_mpi_send_d.f.md | 1 | 13 | 완료 |
| mpi_comm/m_mpi_send_i.f.md | 1 | 11 | 완료 |
| mpi_comm/recv_kk.f.md | 1 | 9 | 완료 |
| mpi_comm/recv_pres.f.md | 2 | 45 | 완료 |
| mpi_comm/recv_rr.f.md | 1 | 10 | 완료 |
| mpi_comm/recv_rst.f.md | 1 | 19 | 완료 |
| mpi_comm/recv_surf.f.md | 2 | 60 | 완료 |
| mpi_comm/remesh.f.md | 4 | 99 | 완료 |
| mpi_comm/send_cont.f.md | 2 | 40 | 완료 |
| mpi_comm/send_kk.f.md | 1 | 9 | 완료 |
| mpi_comm/send_pos.f.md | 2 | 47 | 완료 |
| mpi_comm/send_rr.f.md | 1 | 10 | 완료 |
| partition/bcast_tbl.f.md | 4 | 140 | 완료 |
| partition/cont_tbl_g.f.md | 11 | 448 | 완료 |
| partition/dealloc.f.md | 3 | 105 | 완료 |
| partition/ens_geom_p.f.md | 2 | 47 | 완료 |

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| module/m_part.f90.md:1–30 | 배열의 분할·절점·통신 용도 단정 | [정정] 선언만으로 입증되지 않은 용도를 해석으로 구분 | 5–30 |
| module/m_part.f90.md:31–58 | NG 등의 개수·연결표 용도 단정 | [정정] 용도 설명을 해석으로 구분 | 32–57 |
| module/m_part.f90.md:59–75 | 확장 절점·프로세스 용도 단정 | [정정] 용도 설명을 해석으로 구분 | 59–75 |
| module/m_val.f90.md:1–63 | 선언만 있는 배열에 좌표·재료·하중 등의 용도 부여 | [정정] 용도 설명을 해석으로 구분 | 5–63 |
| module/m_val.f90.md:64–123 | 주파수·동하중·시간 단계 용도 단정 | [정정] 용도 설명을 해석으로 구분 | 65–122 |
| module/m_val.f90.md:183–231 | 기하·슬레이브·마찰 용도 단정 | [정정] 주석으로 확인되는 CONTACT와 개별 배열 용도 해석을 구분 | 183–230 |
| module/m_val.f90.md:232–264 | CADMAS 연결·자유도·MPC 인덱스 용도 단정 | [정정] 선언 및 주석을 넘어서는 용도를 해석으로 구분; DARCY FLUX는 단위를 추가하지 않고 플럭스로 표기 | 232–263 |
| module/m_val.f90.md:265–300 | N_PART를 분할 개수로 단정 | [정정] 정수 선언과 분할 개수 해석을 구분 | 282–300 |
| module/mavbl.f90.md:1–9 | INTEGER(8)을 8바이트로 단정 | [정정] 소스에 명시된 kind=8로 기술 | 1·5 |
| module/mod_comm.f90.md:127–171 | ELSE 없는 imodel 분기의 미해당 동작 생략 | [보완] ELSE 부재와 my_model 유지 명시 | 128–144 |
| module/mod_comm.f90.md:222–260 | 디렉터리 분기 사슬의 ELSE 부재 생략 | [보완] ELSE 부재 명시 | 250–254 |
| module/mpc_work.f90.md:1–35 | 종속·행열 인덱스·작업 용도를 단정 | [정정] 용도 설명을 해석으로 구분 | 3–33 |
| module/mpi_param.f90.md:1–10 | CPLWORLD·MYWORLD의 용도 단정 | [정정] 용도 설명을 해석으로 구분 | 5–8 |
| module/mused.f90.md:1–56 | 8바이트 단정과 배열 형의 외부 근거 미표기 | [정정] kind=8로 정정하고 형 선언 출처 명시 | 1·9·13–56; module/m_val.f90:7–67 |
| module/mused.f90.md:57–93 | 데이터 테이블·형 분류의 출처 생략 | [보완] M_VAL 주석·형 선언 출처 명시 | 57–93; module/m_val.f90:5·69–122 |
| module/mused.f90.md:94–134 | 출력 용도 단정과 형·분류 출처 생략 | [정정] 선언부 주석 분류로 한정하고 출처 명시; FLUX 주석 번역을 플럭스로 통일 | 95–134; module/m_val.f90:124–181 |
| module/mused.f90.md:135–180 | 접촉 분류·형 선언 출처 생략 | [보완] M_VAL 출처 명시 | 135–180; module/m_val.f90:183–230 |
| module/mused.f90.md:181–222 | 자유도 용도 단정과 분류 출처 생략 | [정정] INDEX 주석으로 한정하고 출처 명시 | 181–221; module/m_val.f90:232–298 |
| module/mused.f90.md:223–262 | 배열 용도 단정과 소속 근거 생략 | [정정] 선언 모듈 기준으로 기술하고 출처 명시 | 223–258; module/mpc_work.f90:7–32; module/m_part.f90:11–73 |
| mpi_comm/c_mpi_init.f.md:28–60 | IROOTC를 모든 랭크로 송신 | [정정] 송신 루프 대상은 1부터 NPROCS0-1 | 53–55 |
| mpi_comm/c_mpi_init.f.md:61–87 | 바깥 조건 인용과 브로드캐스트의 무조건 실행 여부 미명시 | [보완] 바깥 IF 및 닫힘 행과 무조건 BCAST를 명시 | 29·81·83–85; mpi_comm/m_mpi_bcast_i.f:9 |
| mpi_comm/c_mpi_init.f.md:코드 사실 45–59 | IRANK를 다른 값으로 바꾸는 문장이 없음 | [정정] 수신 호출이 IRANK를 갱신하고 수신값을 누적 | 45–51 |
| mpi_comm/comm_cg.f.md:1–25 | 절점·자유도 용도 단정 | [정정] 인덱스 계산 사실과 용도 해석을 구분 | 17–25 |
| mpi_comm/comm_cg2.f.md:1–30 | NODEXP 계열을 절점으로 단정 | [정정] 실제 인덱스 계산과 절점 해석 구분 | 19–30 |
| mpi_comm/comm_cg2.f.md:53–71 | 수신 절점 용도 단정 | [정정] 인덱스 계산과 절점 해석 구분 | 54–61 |
| mpi_comm/comm_cg2x.f.md:1–30 | NODEXP 계열을 절점으로 단정 | [정정] 실제 인덱스 계산과 절점 해석 구분 | 19–30 |
| mpi_comm/comm_cg2x.f.md:53–71 | 수신 절점 용도 단정 | [정정] 인덱스 계산과 절점 해석 구분 | 54–61 |
| mpi_comm/comm_cgx.f.md:1–25 | 절점·자유도 용도 단정 | [정정] 인덱스 계산 사실과 용도 해석을 구분 | 17–25 |
| mpi_comm/comm_tblx.f.md:1–35 | KK의 개수·물리 용도 단정 | [정정] 대입 사실과 개수·경계 해석 구분 | 12–34 |
| mpi_comm/comm_tblx.f.md:36–88 | 2차원 배열의 열 수를 자료 개수로 표현하고 확장 IELQ로 요약 | [정정] 원소 수와 열 수 구분 및 GSURFX 인덱스·인수 명시 | 38–87 |
| mpi_comm/comm_tblx.f.md:89–145 | FTID 보존량을 N1개로 표현 | [정정] FTID 보존량은 6행의 앞 N1개 열 | 137–141 |
| mpi_comm/comm_tblx.f.md:204–264 | FCP 보존량을 N0개로 표현 | [정정] 첫 층의 3행·N0열 보존으로 명시 | 206–210 |
| mpi_comm/comm_tblx.f.md:265–308 | 조기 반환 조건 생략 | [보완] RETURN의 원문 조건과 이 구간 도달 조건 명시 | 263 |
| mpi_comm/comm_tblx.f.md:309–345 | 조기 반환 조건 생략 | [보완] RETURN의 원문 조건과 이 구간 도달 조건 명시 | 263 |
| mpi_comm/recv_kk.f.md:1–9 | 송신 랭크와 실행 랭크의 구별 및 래퍼 근거 생략 | [보완] 랭크 1로부터 수신하며 실행 랭크 조건은 없음을 명시 | 5–7; mpi_comm/m_mpi_recv_i.f:1–9 |
| mpi_comm/recv_pres.f.md:29–45 | ELSE 없는 송신 분기의 미해당 동작 생략 | [보완] 0·1 이외 랭크에서는 송신하지 않음 명시 | 39–43 |
| mpi_comm/recv_rr.f.md:1–10 | 송신 랭크와 실행 랭크의 구별 및 래퍼 근거 생략 | [보완] 랭크 1로부터 수신하며 실행 랭크 조건은 없음을 명시 | 6–8; mpi_comm/m_mpi_recv_i.f:1–9; mpi_comm/m_mpi_recv_d.f:1–12 |
| mpi_comm/recv_rst.f.md:코드 사실 16–17 | 재시작 용도 단정 | [정정] 저장 위치와 용도 해석 구분 | 16–17 |
| mpi_comm/recv_surf.f.md:1–28 | 모든 비영 랭크가 명령 11을 전송 | [정정] 명령 11은 MYRANK==1만 송신하며 비영 랭크는 0으로부터 수신 | 17–22 |
| mpi_comm/recv_surf.f.md:코드 사실 29·34·38 | 면당 정수 개수로 단정 | [정정] 차원·전송 개수와 면 해석 구분 | 29·34·38 |
| mpi_comm/remesh.f.md:1–32 | 절점 용도 단정과 랭크 조건의 범위 불명확 | [정정] 인덱스 대입·절점 해석 구분 및 랭크 0 범위 명시 | 16–31 |
| mpi_comm/remesh.f.md:33–56 | 절점 용도 단정 및 바깥 조건의 원문 인용 누락 | [정정] 인덱스 대입·절점 해석 구분 및 바깥 IF와 닫힘 명시 | 16·33–55 |
| mpi_comm/remesh.f.md:57–91 | 절점·연결점 용도 단정 | [정정] 배열 인덱스 사실과 연결점 해석 구분 | 57–89 |
| mpi_comm/remesh.f.md:92–99 | 수직 이동·좌표·요소 용도 단정과 GSURF 두 번째 POS 생략 | [정정] 실제 인수 순서 및 성분 대입과 물리적 해석 구분 | 93–97 |
| mpi_comm/send_cont.f.md:32–40 | 바깥 IF 조건 및 ELSE 부재 생략 | [보완] 바깥 조건·닫힘·미해당 랭크 동작 명시 | 11·32–38 |
| mpi_comm/send_cont.f.md:코드 사실 18·20·26 | 면당 정수 개수로 단정 | [정정] 열당 개수와 면 해석 구분 | 18·20·26 |
| mpi_comm/send_pos.f.md:1–24 | 내부 절점 용도 단정 | [정정] 전송 원소 수와 내부 절점 해석 구분 | 16–23 |
| mpi_comm/send_pos.f.md:25–47 | 명령 14 송신의 랭크 1 조건과 IGEO 조건을 요약에서 생략 | [정정] 랭크 0·1·그 밖의 랭크 및 IGEO 조건을 구분 | 25–39 |
| partition/bcast_tbl.f.md:14–63 | 동하중 용도 단정 | [정정] 해당 조건에서 할당하는 배열 이름 명시 | 42–47 |
| partition/bcast_tbl.f.md:64–111 | 자료 개수가 모두 곱이라고 요약 | [정정] RTIM은 2+KK(83)이며 나머지는 개별 인수 식을 따름 | 64–108 |
| partition/bcast_tbl.f.md:112–140 | 조기 반환 조건 생략 | [보완] RETURN의 원문 조건과 도달 조건 명시 | 110 |
| partition/cont_tbl_g.f.md:1–60 | NOD와 ICSF·IELQ의 기하학적 의미 단정 | [정정] 실제 DATA·조건·슬라이스와 삼각형·면 해석 구분 | 7–10·29–60 |
| partition/cont_tbl_g.f.md:61–111 | 접촉 면·요소·절점 의미 단정 | [정정] 실제 인덱스 대입과 기하학적 해석 구분 | 64–107 |
| partition/cont_tbl_g.f.md:112–152 | 요소·절점 번호 의미 단정 | [정정] 기하학적 용도를 해석으로 구분 | 121–145 |
| partition/cont_tbl_g.f.md:153–213 | 접촉 영역·삼각형·사각형·중앙 절점 의미 단정 | [정정] 조건·이중 인덱스·대입식과 기하학적 해석 구분 | 179–210 |
| partition/cont_tbl_g.f.md:214–257 | 접촉 면·절점·영역 의미 단정 | [정정] 배열 인덱스 사실과 해석 구분 및 영역 간 중복 제외 명시 | 216–256 |
| partition/cont_tbl_g.f.md:258–300 | 삼각형·시작 절점·요소·로컬 변 의미 단정 | [정정] 기하학적 용도를 해석으로 구분 | 264–292 |
| partition/cont_tbl_g.f.md:301–338 | 영역·면·변 의미 단정 | [정정] 실제 조건과 인덱스 증가 및 기하학적 해석 구분 | 310–337 |
| partition/cont_tbl_g.f.md:339–381 | 바깥 루프 범위 미인용과 기하학적 의미 단정 | [정정] 바깥 DO와 닫힘 명시 및 기하학적 해석 구분 | 310·339–381 |
| partition/cont_tbl_g.f.md:401–432 | 접촉 면·원 요소·삼각형 의미 단정 | [정정] 원 인덱스와 분기별 계산을 명시하고 기하학적 해석 구분 | 408–431 |
| partition/cont_tbl_g.f.md:433–448 | 영역 쌍·초기 슬레이브 용도 단정 | [정정] 용도 설명을 해석으로 구분 | 435–446 |
| partition/cont_tbl_g.f.md:코드 사실 128–145 | 새 표면 절점과 IBTE 생성 개수 단정 | [정정] 직접 확인되는 대입·IP 증가와 생성 용도 해석 구분 | 128–145 |
| partition/dealloc.f.md:1–35 | 지정 변위·하중 용도 단정 | [정정] 해제 배열 이름과 용도 해석 구분 | 23–35 |
| partition/dealloc.f.md:36–81 | 동하중·시계열·단계·작업 통신 용도 단정 | [정정] 해제 배열 이름·소속 근거와 용도 해석 구분 | 37–80; module/m_part.f90:16–22 |
| partition/dealloc.f.md:코드 사실 14–103 | 후반부 해제 배열의 접촉 용도 단정 | [정정] 조기 반환 사실과 접촉 해석 구분 | 82–103 |
| partition/ens_geom_p.f.md:29–47 | IEP를 분할표로 단정 | [정정] 실제 인수와 분할 용도 해석 구분 | 35–38 |
| module/m_val.f90.md:124–182 | FLUX를 유량으로 한정해 번역 | [정정] 단위·정의가 없는 FLUX는 플럭스로 표기 | 149–157 |
| module/mod_comm.f90.md:80–126 | 주석의 분할 순서를 병렬 관계로 번역 | [정정] 원문의 world, group, model 순서 보존 | 118 |

정정 56, 보완 12, 이상 없음 47
