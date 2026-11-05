---
title: "CADMAS 튜토리얼·빌드 문서와 코드 차이"
model: CADMAS-SURF
component: manual-notes
canonical_source: self
citation_status: verified
has_source_needed: false
last_source_check: "2026-11-04 (recovery 대조 반영)"
verification_method: "2026-11-04 CADMAS-SURF recovery 대조 보고서 반영"
verification_by: "Codex — 최종 결론 근거 행과 보고서 원문 이식"
verification_date: 2026-11-04
note_author: "Codex"
note_date: 2026-11-04
layer: 2
depends_on: []
related:
  - models/CADMAS-SURF/manual-notes/cadmas-manuals-catalogue.md
---

# CADMAS 튜토리얼·빌드 문서와 코드 차이

매뉴얼 목록은 [CADMAS 매뉴얼 카탈로그](cadmas-manuals-catalogue.md)에 있다.

## 문서와 코드 차이 (11-04 대조)

비교한 판: 코드는 github.com/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami `da7668f`(2024-08-30, 커밋 1개)의 Simulators/이며, 문서는 CADMAS-AGENT_Tutorial_English, CADMAS-SURF3D_Tutorial_English, CADMAS-2F_Tutorial_English 및 각 시뮬레이터 ReadMe·Makefile이다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| agent:KA1-304 | `AGENT tutorial p.1·4`; `AGENT manual p.9`; `AGENT/m_potential.f90:68–69`<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KA1.md) · [보고서](../../../_staging/recovery/compare/cadmas-agent-docs-vs-code.md) | `0: non-accessible cell`<br>`-1: accessible cell` | `AGENT/m_potential.f90:68–69` `!  move_boundary=0        : 道` / `!  move_boundary=-1       : 道ではない(進入不可)` | B 문서 오기 | 진입 가능 값은 0이다. 진입 불가 값은 -1이다. |
| agent:KA1-309 | `AGENT tutorial p.3·6`; `AGENT manual p.8`; `AGENT/read_agent.f90:35·58–60`<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KA1.md) · [보고서](../../../_staging/recovery/compare/cadmas-agent-docs-vs-code.md) | `Agent.inp`<br>`W_mod` | `AGENT/read_agent.f90:35` `open(12,file='agent.inp',status='old',form='formatted',err=99)`; 58–60행의 10열 읽기는 KA1-051에 전문 인용했다. | B 문서 오기 | 입력 파일명은 소문자 agent.inp이다. p.6 화면의 W_mod 헤더에 해당하는 입력은 weight_mob(n)이다. |
| agent:KA1-318 | `AGENT tutorial p.7·11·15·18`; `AGENT/read_condition.f90:30`; `AGENT/read_cadmas.f90:102`<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KA1.md) · [보고서](../../../_staging/recovery/compare/cadmas-agent-docs-vs-code.md) | `nregion=1`<br>`file="./tutorial.ma"`<br>`file="../test.ma"`<br>`ma file directory` | `AGENT/read_condition.f90:30` `namelist /offline/ nregion,file`; 59행 `read(11,offline)`; `AGENT/read_cadmas.f90:102` `open(300+m,file=trim(cadfile(m)),status='old',form='unformatted',err=99)` | B 문서 오기 | offline의 file은 .ma 파일의 경로이다. |
| agent:KA1-320 | `AGENT tutorial p.8`; `AGENT/main.f90:13`; `AGENT/Makefile:4–9`<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KA1.md) · [보고서](../../../_staging/recovery/compare/cadmas-agent-docs-vs-code.md) | `agent_ver3.3/ma.out`<br>`intra-node parallelism is possible with ver3.5_omp` | `AGENT/main.f90:13` `write(*,*)"agent_ver3.5 start"`; `AGENT/Makefile:8` `COPT    = -O2 -fallow-argument-mismatch` | A 판 차이 | `AGENT tutorial p.8`은 agent_ver3.3 실행 경로와 별도 ver3.5_omp 판을 명시한다. 공개 코드는 `AGENT/main.f90:13`의 agent_ver3.5 표지와 OpenMP 옵션 없는 Makefile을 사용한다. |
| agent:KA1-321 | `AGENT tutorial p.8`; `AGENT/main.f90:17`; `AGENT/mod_comm.f90:98`<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KA1.md) · [보고서](../../../_staging/recovery/compare/cadmas-agent-docs-vs-code.md) | `[executable file path] -np 1` | `AGENT/main.f90:17` `call init_mpmd`; `AGENT/mod_comm.f90:98` `call mpi_init(ierr)` | B 문서 오기 | `AGENT tutorial p.8`의 비스케줄러 예시는 MPI 런처를 생략했다. 같은 쪽 위 예시처럼 런처 뒤에 -np 1과 실행 파일 경로를 둔다. |
| agent:KA1-322 | `AGENT tutorial p.10–11`; `AGENT/read_condition.f90:28·53·61–64`<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KA1.md) · [보고서](../../../_staging/recovery/compare/cadmas-agent-docs-vs-code.md) | `danger.inp`<br>`.ma file (STOC output data)`<br>`modify OnOff flag` | `AGENT/make_n_potential.f90:97` `open(60,file=filename,status='old')`; `AGENT/read_condition.f90:61–64` `if(flag_danger==1)then` / `rewind(11)` / `read(11,danger)` / `endif` | B 문서 오기 | 회피 플래그는 .ma가 아니라 namelist.inp에서 수정한다. |
| agent:KA1-327 | `AGENT tutorial p.7·15`; `AGENT/make_potential_shelter.f90:59–62`<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KA1.md) · [보고서](../../../_staging/recovery/compare/cadmas-agent-docs-vs-code.md) | `flag_danger: flag of writing shelter potential →1(On)`<br>`flag_WP=1` | `AGENT/make_potential_shelter.f90:59–62` `if(flag_WP==1) then` / `open(32,file=filename)` / `do j=jpmax,1,-1` / `write(32,'(1000F10.2)')(m_pot_shelter(n,i,j),i=1,ipmax)` | B 문서 오기 | 피난소별 비용 쓰기는 `flag_WP=1`이다. |
| agent:KA1-328 | `AGENT tutorial p.5·17`; `AGENT/make_potential_shelter.f90:29·32·41·58`<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KA1.md) · [보고서](../../../_staging/recovery/compare/cadmas-agent-docs-vs-code.md) | `shelter potential files(000.txt, 001.txt)`<br>`output file by case WP` | `AGENT/make_potential_shelter.f90:41` `do n=1,n_shelter`; 58행 `write(filename,'(i3.3,".txt")')n`; 29행 `do m=1,n_shelter`; 32행 `write(filename,'(i3.3,".txt")')m` | B 문서 오기 | 두 피난소의 비용 파일명은 001.txt와 002.txt이다. |
| agent:KA1-329 | `AGENT tutorial p.17–18`; `AGENT/read_condition.f90:41·53`<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KA1.md) · [보고서](../../../_staging/recovery/compare/cadmas-agent-docs-vs-code.md) | `.ma file (STOC output data)`<br>`modify OnOff flag` | `AGENT/read_condition.f90:53` `read(11,flag)` | B 문서 오기 | RP 플래그는 namelist.inp에서 수정한다. |
| agent:KA1-331 | `AGENT tutorial p.6·18`; `AGENT manual p.8`; `AGENT/read_condition.f90:26`; `AGENT/read_agent.f90:58–60`<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KA1.md) · [보고서](../../../_staging/recovery/compare/cadmas-agent-docs-vs-code.md) | `agent_start = 0` | `AGENT/read_condition.f90:26` `namelist /agent/ n_rw,rw_dt,n_slope`; `AGENT/read_agent.f90:60` `& ,weight_shelter(n),weight_mob(n),agent_start(n)` | B 문서 오기 | agent_start는 &agent 키워드가 아니다. 사람별 agent.inp 열이다. |
| tutorials-build:KU1-110 | 3D·2F·AG ReadMe.md:4; STR ReadMe.md:9; 각 Source code/Makefile 또는 makefile<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KU1.md) · [보고서](../../../_staging/recovery/compare/cadmas-tutorials-build-vs-code.md) | `source code ... Sourse code folder`<br>`Code`<br>`Download ZIP` | 실제 폴더명 `Source code`; 각 Makefile의 소스 목록은 2.5절에 전량 대조한다. | B 문서 오기 | 소스 폴더 이름을 `Source code`로 정정한다. |
| tutorials-build:KU1-121 | STR ReadMe.md:10–11; `STR3D/main/astea_mechanical.f:40–43`; `3D2F/Makefile:5`<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KU1.md) · [보고서](../../../_staging/recovery/compare/cadmas-tutorials-build-vs-code.md) | `Supports coupling with CADMAS-SURF/3D2F`<br>`Simulators/CADMAS-2F` | `STR3D/main/astea_mechanical.f:40–43` `IF( ICPL == 2 ) THEN`<br>`CALL RECV_RST(KK)`<br>`ELSE`<br>`CALL RST_CNTL(KK)`; 실제 폴더 `S/CADMAS-SURF-3D2F`와 `3D2F/Makefile:5` `LOAD    = a.3d2f-opt`. | B 문서 오기 | STR3D의 연성 링크를 `Simulators/CADMAS-SURF-3D2F`로 정정한다. |
| tutorials-build:KU1-817 | `3D2F/Makefile:12–114`; `3D2F/dummy.f90:1,8`; 2F 파일 목록<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KU1.md) · [보고서](../../../_staging/recovery/compare/cadmas-tutorials-build-vs-code.md) | (문서에 해당 문장 없음) | `3D2F/dummy.f90:1` `integer(4) function getcwd(dirname)`; `3D2F/dummy.f90:8` `integer(4) function chdir(dirname)` | C 문서 누락 | 3D2F의 실제 Fortran 388개 중 기본 빌드 목록은 387개다. |
| tutorials-build:KU1-902 | `3D/Makefile:41,84,94–96`; `3D/vf_im2inp.f:1`<br>[근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KU1.md) · [보고서](../../../_staging/recovery/compare/cadmas-tutorials-build-vs-code.md) | `vf_iitime.f vf_im1inp.f vf_im2inp.o vf_ip1inp.f vf_ir1inp.f \` | `3D/vf_im2inp.f:1` `SUBROUTINE VF_IM2INP(DMTBTT,DMTBZZ,DMTBHH,DMTBUN,DMTBUT)`; `3D/Makefile:84` `OBJS   = $(SRCS:.f=.o) $(DUMMY)` | F 표기 차이 | SRCS의 vf_im2inp.o는 치환 뒤에도 같은 객체를 뜻한다. |
