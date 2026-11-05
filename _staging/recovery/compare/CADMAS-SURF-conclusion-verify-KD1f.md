# CADMAS-SURF 차이 결론 재대조 — KD1-766–913

## 1 요약

대상은 보고서 §5의 KD1-766–913 148행이다. H 행과 강도를 적은 E 행을 모두 포함한다.

최종 결론은 A 12행, B 9행, C 100행, D 0행, E 7행, F 10행, H 6행, 일치 4행이다. E의 강도는 강함 6행과 중간 1행이다. 약함은 0행이다.

보고서 결론에서 바뀐 행은 63행이다. 유지한 행은 85행이다. 분류 자체가 바뀐 행은 39행이다. 인용 위치·조건·식·수량·부정을 고치거나 보완한 행은 25행이다. 집계 근거는 아래 표의 행 ID·최종 결론·바뀜 칸이다.

인용 정정 행은 KD1-767, 769, 778, 779, 780, 782, 785, 819, 822, 823, 830, 831, 832, 837, 840, 844, 852, 871, 874, 879, 885, 888, 902, 903, 910이다.

코드 경로의 `3D`와 `3D2F`는 `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/` 아래 각 `CADMAS-SURF-3D/Source code/`와 `CADMAS-SURF-3D2F/Source code/`를 뜻한다.

`바뀜`은 분류·강도·결론의 의미 또는 원문 인용이 달라졌는지를 뜻한다. 원문 조건·식·수량·인용 위치의 정정은 이유 칸에 적는다. 판 근거의 추가와 문체 정리는 변경에 포함하지 않는다.

쪽 이미지 경로는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/`이다. `cad-2f-manual PDF p.N`은 `cad-2f-manual-NNN.png`이다. `cad-str-instr-cadmas PDF p.N`은 `cad-str-instr-cadmas-NNN.png`이다. PDF 쪽과 인쇄 쪽이 다르면 인쇄 쪽을 별도로 적었다.

판 판정 결론 칸의 E 강도는 E3의 확정 결론이다. A·B 판정은 AD5의 확정 결론이다. 해당 행의 판 판정이 없으면 `-`로 적었다. 외부 출처 기록의 X 8행은 이 KD1 범위에 해당하지 않는다.

## 2 행별 최종 결론 표

### KD1-766–795

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| KD1-766 | C | - | C | 아니오 | 3D2F sf_pos_init.f:1–85; cad-str-instr-cadmas PDF pp.6,8 | 문서는 초기 교환 흐름을 적는다. 조건부 DVEL 분배와 초기 표면 전달 순서는 코드의 추가 구현이다. | 초기 절점 압력·표면 상태를 구조 모델에 보낸다. 구조물 위치 좌표와 조건부 지반 다르시 유속을 받아 분배한다. |
| KD1-767 | C | - | C | 예 | 3D2F sf_pos_update1.f:1–36 | 지형변위와 체적 검사는 ISTM 조건 안에 있다. 보고서에서 빠진 조건을 보완한다. | `TNEXT = TNOW + DT`이다. `IF( TNEXT > TSTR2 ) THEN`에서 절점 압력을 준비한다. 그 안의 `IF( ISTM == 1 ) THEN`에서 지형변위와 체적 검사 자료를 준비한다. |
| KD1-768 | C | - | C | 아니오 | 3D2F sf_pos_update2.f:1–100; cad-str-instr-cadmas PDF pp.4,8 | 문서는 두 구조 시각 사이 보간을 적는다. IGEO 조건에 따른 DVEL 교환·분배를 함께 기술하는 구현 설명은 빠져 있다. | 구조물 위치 좌표와 조건부 지반 다르시 유속을 교환한다. 유체 다음시각에 맞춰 두 구조 시각 사이를 보간한다. |
| KD1-769 | C | - | C | 예 | 3D2F sf_pos_updt.f:1–82 | 허용량은 요소 크기뿐 아니라 전역 최소 유체격자 크기도 사용한다. 보고서의 비교 대상 설명을 고친다. | 절점 이동량 `DP`와 허용량 `TOL`을 비교한다. `IGFC(I) == 1`이면 `TOL = D_MIN * 1.D-3`을 쓴다. `IRND(I) == 1`이면 `TOL = GRDL(I) * 1.D-2`를 쓴다. 나머지 절점은 `TOL = GRDL(I) * 1.D-1`을 쓴다. `IF( DP < TOL ) THEN`에서 절점을 고정한다. 요소의 절점 고정 여부로 `SPC(I)%IFIX`를 갱신한다. |
| KD1-770 | C | - | C | 아니오 | 3D2F sf_prsini.f:1–40; cad-str-instr-cadmas PDF pp.1 | 문서는 data.prs 출력 제어를 적는다. 이 행의 파일 헤더 구성 항목은 생략한다. | data.prs에 수면·최상부 높이·구조 표면·압력 작용 절점 표지를 쓴다. |
| KD1-771 | C | - | C | 아니오 | 3D2F sf_prstrn.f:1–24; cad-str-instr-cadmas PDF pp.1,23 | 문서는 압력 계산과 파일 출력 제어를 적는다. 시각별 표면압력 레코드 구성은 생략한다. | 구조 절점의 유체 압력을 구하고 시각별로 표면압력 파일에 쓴다. |
| KD1-772 | C | - | C | 아니오 | 3D2F sf_rd_obst.f:1–215; cad-str-instr-cadmas PDF pp.11 | 문서는 data.bdf의 절점·요소·공극률 입력을 적는다. 요소 최소크기 산정은 생략한다. | data.bdf의 절점·요소·재료·공극률을 읽고 요소 최소크기를 계산한다. |
| KD1-773 | C | - | C | 아니오 | 3D2F sf_rd_restart.f:1–121 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | 유체와 구조 연성의 재시작 상태를 읽는다. 구조물 위치 좌표와 지반 다르시 유속을 분배한다. |
| KD1-774 | C | - | C | 아니오 | 3D2F sf_realloc.f:1–42; cad-str-instr-cadmas PDF pp.20–21 | 문서는 이동 자료 갱신을 적는다. 갱신 개수에 따른 개별 배열 재할당은 생략한다. | 갱신한 구조 요소·절점·표면 개수에 맞춰 연성 배열을 재할당한다. |
| KD1-775 | C | - | C | 아니오 | 3D2F sf_recv_cont.f:1–116; cad-str-instr-cadmas PDF pp.12 | 문서는 접촉 그룹·연결표를 적는다. 코드의 삼각형 대표크기 계산은 생략한다. | 구조 접촉 그룹·표면·연결표를 받고 접촉 삼각형과 대표크기를 구성한다. |
| KD1-776 | C | - | C | 아니오 | 3D2F sf_reduce_d.f:1–50 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | 인덱스 대응표를 이용해 분할 실수 자료를 전체 번호 배열에 합산한다. |
| KD1-777 | C | - | C | 아니오 | 3D2F sf_reduce_i.f:1–49 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | 인덱스 대응표를 이용해 분할 정수 자료를 전체 번호 배열에 합산한다. |
| KD1-778 | C | - | C | 예 | 3D2F sf_remv.f:1–28 | 이 루틴은 물 체적 자체를 보정하지 않는다. GGV·GGF·GGW 갱신으로 설명을 한정한다. | 지형 제거 두께에서 셀·면 공극률과 `GGW`를 갱신한다. 제거 두께는 `RZ = DMIN1(DZ,H)`이다. 남은 두께는 `H = H - RZ`이다. |
| KD1-779 | C | - | C | 예 | 3D2F sf_reset_ff.f:1–72 | 0 대입은 새 고체에 한정되지 않는다. 주변 값이 없는 경우의 1 대입을 보완한다. | `IF( NF(I,J,K) < 0 ) THEN`에서 스칼라 값을 0으로 만든다. `ELSEIF( NFP(I,J,K) < 0 .AND. NF(I,J,K) == 0 ) THEN`에서 주변 유효셀 값으로 복원한다. 유효 이웃을 찾지 못하면 `IF( IDR == 4 ) FF(I,J,K) = 1.D0`을 적용한다. |
| KD1-780 | C | - | C | 예 | 3D2F sf_reset_uu.f:1–72 | 보고서는 도달 불가 평균 코드를 현재 동작에 포함했다. 실제 실행문은 0 대입 뒤 CYCLE이다. | `IF( INDX(I,J,K) == -1 ) THEN`에서 면 유속을 0으로 만든다. `ELSEIF( INDXP(I,J,K) /= 0 .AND. INDX(I,J,K) == 0 ) THEN`에서도 유속을 0으로 만든다. 이 분기의 `CYCLE` 때문에 뒤의 주변 속도 평균 코드는 실행되지 않는다. |
| KD1-781 | C | - | C | 아니오 | 3D2F sf_rface0.f:1–62 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | 법선 경사로 지반·돌 표면 유형과 지형 연동 절점을 구분한다. |
| KD1-782 | C | - | C | 예 | 3D2F sf_rface2.f:1–74 | 수평 셀 탐색은 모든 절점이 아니라 양의 지형 연동 표지를 가진 절점에만 적용한다. | 지형 연동 절점 표지를 분배한다. `IF( IRGRID(IG) <= 0 ) CYCLE`을 통과한 절점의 수평 유체셀 번호를 찾는다. 담당 영역 밖 절점은 `IRGRID(IG) = 0`으로 둔다. |
| KD1-783 | C | - | C | 아니오 | 3D2F sf_rint.f:1–11 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | 두 점 사이에서 한 좌표를 기준으로 다른 좌표를 선형 보간한다. |
| KD1-784 | C | - | C | 아니오 | 3D2F sf_s34.f:1–21 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | 삼각형·사각형의 부호 있는 2차원 면적을 계산한다. |
| KD1-785 | C | - | C | 예 | 3D2F sf_send_rst.f:1–16 | STM에는 출력 제어 IRSTYP을 보내지 않는다. 수신 대상별 제어값을 구분한다. | `IF( MYRANK == 0 ) THEN`에서 구조 대표 랭크에 `IRSTYP`과 `IRETYP`을 보낸다. `IF( ISTM == 1 )`이면 STM 대표 랭크에는 `IRETYP`을 보낸다. |
| KD1-786 | C | - | C | 아니오 | 3D2F sf_send_surf.f:1–42; cad-str-instr-cadmas PDF pp.6 | 문서는 초기 표면 전달 흐름을 적는다. 압력 면적률과 절점 표지의 전송 묶음은 생략한다. | 수면·최상부 높이·구조 표면·압력 면적률·절점 표지를 구조 모델에 보낸다. |
| KD1-787 | C | - | C | 아니오 | 3D2F sf_stm0.f:1–18 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | STM 연성 초기 공극률·면 상태를 구성하고 연성 이전 상태를 보존한다. |
| KD1-788 | C | - | C | 아니오 | 3D2F sf_stm1.f:1–18 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | STM의 초기 지형·수심을 교환하고 필요한 연성 재시작을 읽는다. |
| KD1-789 | C | - | C | 아니오 | 3D2F sf_stm2.f:1–27 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | STM의 지형변화를 반영하고 경계·면 상태·유체장을 재구성한다. |
| KD1-790 | C | - | C | 아니오 | 3D2F sf_stm3.f:1–14 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | 설정에 따른 EnSight와 STM 연성 재시작 출력을 수행한다. |
| KD1-791 | C | - | C | 아니오 | 3D2F sf_stm_c_mpi_comm_rank.f:1–9 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | COMM_2FC_STM에서 자기 랭크 조회를 수행한다. |
| KD1-792 | C | - | C | 아니오 | 3D2F sf_stm_c_mpi_comm_size.f:1–9 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | COMM_2FC_STM에서 통신 집합 크기 조회를 수행한다. |
| KD1-793 | C | - | C | 아니오 | 3D2F sf_stm_c_mpi_recv_d.f:1–21 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | COMM_2FC_STM에서 배정밀도 자료 수신을 수행한다. |
| KD1-794 | C | - | C | 아니오 | 3D2F sf_stm_c_mpi_recv_i.f:1–21 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | COMM_2FC_STM에서 정수 자료 수신을 수행한다. |
| KD1-795 | C | - | C | 아니오 | 3D2F sf_stm_c_mpi_send_d.f:1–21 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | COMM_2FC_STM에서 배정밀도 자료 송신을 수행한다. |

### KD1-796–825

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| KD1-796 | C | - | C | 아니오 | 3D2F sf_stm_c_mpi_send_i.f:1–21 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | COMM_2FC_STM에서 정수 자료 송신을 수행한다. |
| KD1-797 | C | - | C | 아니오 | 3D2F sf_stm_comm_init.f:1–69 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | STM과 통신 집합·대표 랭크를 정하고 연성 표지를 배포한다. |
| KD1-798 | C | - | C | 아니오 | 3D2F sf_stm_finalize.f:1–18 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | STM의 마지막 지형 응답을 받은 뒤 종료 표지 1을 보낸다. |
| KD1-799 | C | - | C | 아니오 | 3D2F sf_stm_gather_d.f:1–76 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | 분할 실수 수평 격자를 전역 수평 격자에 모은다. 끝 면 포함은 ID와 분할 표지로 정한다. |
| KD1-800 | C | - | C | 아니오 | 3D2F sf_stm_gather_i.f:1–76 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | 분할 정수 수평 격자를 전역 수평 격자에 모은다. 끝 면 포함은 ID와 분할 표지로 정한다. |
| KD1-801 | C | - | C | 아니오 | 3D2F sf_stm_obst.f:1–53 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | STM 지형으로 공극률·면 상태·관성 공극률을 재구성한다. |
| KD1-802 | C | - | C | 아니오 | 3D2F sf_stm_scatter_d.f:1–53 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | 전역 수평 실수 격자를 각 PE 담당 영역에 분배한다. |
| KD1-803 | C | - | C | 아니오 | 3D2F sf_str0.f:1–35; cad-str-instr-cadmas PDF pp.5 | 문서는 SF_STR0의 핵심 흐름을 적는다. 현재 코드의 조건별 STM·구조 처리 분기는 추가 구현이다. | 구조물 입력·외표면·분할·공극률·경계조건의 초기 전처리를 순서대로 호출한다. |
| KD1-804 | C | - | C | 아니오 | 3D2F sf_str1.f:1–51; cad-str-instr-cadmas PDF pp.6 | 문서의 SF_STR1 흐름도는 분리된 POS_INIT_S/R을 쓴다. 현재 통합 초기화와 재시작 처리를 설명하지 않는다. | 구조 연성 초기 압력 출력·초기 위치 교환 또는 재시작과 유체장 재설정을 수행한다. |
| KD1-805 | C | - | 일치 | 예 | 3D2F sf_str2.f:1–45; cad-str-instr-cadmas PDF p.7 | 구조 연성 매뉴얼의 처리 흐름에 이미 적힌 동작이다. 전용 파일이라는 이유만으로 문서 누락으로 분류할 수 없다. | 구조물 위치를 갱신하고 표면·공극률·경계조건·유체장을 재구성한다. |
| KD1-806 | C | - | C | 아니오 | 3D2F sf_str3.f:1–19 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | 조건에 따라 구조물 압력·EnSight를 출력하고 연성 재시작을 처리한다. |
| KD1-807 | C | - | 일치 | 예 | 3D2F sf_str_obst.f:1–77 ; cad-str-instr-cadmas PDF pp.13–14 | 구조 연성 매뉴얼의 처리 흐름에 이미 적힌 동작이다. 전용 파일이라는 이유만으로 문서 누락으로 분류할 수 없다. | 이전 형상을 보존하고 구조물 교차체적에서 공극률·셀·면 상태·관성 공극률을 재구성한다. |
| KD1-808 | C | - | C | 아니오 | 3D2F sf_stria.f:1–16 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | 2차원 또는 3차원 삼각형 면적을 계산한다. |
| KD1-809 | C | - | C | 아니오 | 3D2F sf_tetdiv.f:1–45; cad-str-instr-cadmas PDF pp.17 | 문서는 사면체 분할 입출력을 적는다. 지원하는 여섯 절점 수의 분기 목록은 생략한다. | 4·6·8·10·15·20절점 요소를 사면체 집합으로 분해한다. |
| KD1-810 | C | - | C | 아니오 | 3D2F sf_tetvol.f:1–25 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | 사면체 네 꼭짓점의 부호 있는 체적을 계산한다. |
| KD1-811 | C | - | C | 아니오 | 3D2F sf_trm1.f:1–26 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | 3차원 삼각형의 로컬 직교기저·변환행렬·원점을 구성한다. |
| KD1-812 | C | - | C | 아니오 | 3D2F sf_trm2.f:1–35 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | 2차원 삼각형 좌표변환 행렬과 기준 삼각형을 구성한다. |
| KD1-813 | C | - | C | 아니오 | 3D2F sf_trns1.f:1–20 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | 3차원 삼각형 좌표를 로컬 좌표로 변환하고 변환 후 법선 성분을 계산한다. |
| KD1-814 | C | - | C | 아니오 | 3D2F sf_trns2.f:1–13 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | 2차원 삼각형 좌표에서 원점을 뺀 뒤 변환행렬을 곱한다. |
| KD1-815 | C | - | C | 아니오 | 3D2F sf_type.f90:1–10 | 본문의 루틴 인용과 실행문이 일치한다. 문서에 없는 연성·수치·입출력 구현이므로 C이다. | 절단 형상을 보존하는 SPACE 파생형의 고정표지·개수·인덱스·좌표 배열을 정의한다. |
| KD1-816 | C | - | 일치 | 예 | 3D2F sf_updt_obst.f:1–480; cad-str-instr-cadmas PDF pp.20–21 | 매뉴얼에 프로세스별 절점·요소·표면 자료의 교환·갱신이 이미 적혀 있다. | 이웃 PE와 구조 요소·절점·표면 자료를 교환해 이동 구조물의 로컬 목록을 갱신한다. |
| KD1-817 | C | - | C | 아니오 | 3D2F sf_vecml.f:1–24 | 본문 인용과 코드의 입력·분기·출력 동작이 일치한다. 이 행의 구현 세부는 문서의 설명에 빠져 있다. | N성분 벡터의 내적을 계산한다. |
| KD1-818 | C | - | C | 아니오 | 3D2F sf_volchk.f:1–60 | 본문 인용과 코드의 입력·분기·출력 동작이 일치한다. 이 행의 구현 세부는 문서의 설명에 빠져 있다. | 이동 요소의 사면체 체적을 검사하고 고정 절점 표지를 대표 PE에 모은다. |
| KD1-819 | C | - | C | 예 | 3D2F sf_wt_restart.f:1–120 | 보고서의 출력시각 목록은 파일 쓰기가 아니라 구조 모델로의 통신이다. | 유체·구조·STM의 재시작 상태를 조건별로 파일에 쓴다. `IF( ICPL == 2 .AND. TNOW + DT > TSTR2 ) THEN`에서 대표 PE가 구조 모델에 재시작 횟수를 보낸다. `IF( NR > 0 ) THEN`이면 스텝 번호와 시각 목록도 보낸다. |
| KD1-820 | C | - | 일치 | 예 | 3D2F user_eos.f:13–38; cad-2f-manual PDF pp.3,142(인쇄 465,604) | 매뉴얼은 등온 사용자 상태방정식과 압력 미분 및 ISTATE=1의 매개변수를 적는다. 코드도 같은 선택과 식을 구현한다. | ISTATE=1의 등온 이상기체 밀도와 정규화 압력 미분을 계산한다. |
| KD1-821 | C | - | C | 아니오 | 3D2F vf_a2array.f90:1–97 | 본문 인용과 코드의 입력·분기·출력 동작이 일치한다. 이 행의 구현 세부는 문서의 설명에 빠져 있다. | 3D 메인의 지역 배열을 모듈 배열로 옮기고 2상·압축성·연성 배열을 추가한다. |
| KD1-822 | C | - | C | 예 | 3D2F vf_bwuwg.f:1–294 | 보고서의 상대속도 설정·복원이라는 표현은 IFLG별 대입을 정확히 나타내지 않는다. | `NUMB0+1`부터 `NUMB`까지의 이동 장애물 경계를 처리한다. `IFLG=0`은 상별 벽조건과 혼합 경계값을 설정한다. `IFLG=1`은 경계 유속을 장애물 속도로 설정한다. `IFLG=2`는 법선 경계 유속을 0으로 만든다. |
| KD1-823 | C | - | C | 예 | 3D2F vf_cfxyz.f:1–248 | 인수와 계산식에 BCF 경계값은 없다. 보고서의 경계값 표현을 셀 상태로 고친다. | 셀 VOF와 셀 상태·공극률에서 x·y·z 엇갈림 셀의 VOF를 구성한다. |
| KD1-824 | C | - | C | 아니오 | 3D2F vf_cgcpr1.f:1–34 | 본문 인용과 코드의 입력·분기·출력 동작이 일치한다. 이 행의 구현 세부는 문서의 설명에 빠져 있다. | 이동 경계 재할당 때 기존 NUMB0개의 1열 실수 경계값을 복사한다. |
| KD1-825 | C | - | C | 아니오 | 3D2F vf_cgcpr2.f:1–36 | 본문 인용과 코드의 입력·분기·출력 동작이 일치한다. 이 행의 구현 세부는 문서의 설명에 빠져 있다. | 이동 경계 재할당 때 기존 NUMB0개 경계의 3열 실수 값을 복사한다. |

### KD1-826–855

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| KD1-826 | C | - | C | 아니오 | 3D2F vf_cggvh.f:1–126 | 본문 인용과 코드의 입력·분기·출력 동작이 일치한다. 이 행의 구현 세부는 문서의 설명에 빠져 있다. | HIDEM의 공극률·이동속도를 유체 시각과 서브루프 가중치에 맞춰 갱신한다. |
| KD1-827 | C | - | C | 아니오 | 3D2F vf_cgind0.f:1–59 | 본문 인용과 코드의 입력·분기·출력 동작이 일치한다. 이 행의 구현 세부는 문서의 설명에 빠져 있다. | 이동 장애물이 없는 면·경계 인덱스를 보존한다. |
| KD1-828 | C | - | C | 아니오 | 3D2F vf_cgindb.f:1–183 | 본문 인용과 코드의 입력·분기·출력 동작이 일치한다. 이 행의 구현 세부는 문서의 설명에 빠져 있다. | 현재 면 상태와 보존 경계에서 이동 장애물 INDB를 구성한다. |
| KD1-829 | C | - | C | 아니오 | 3D2F vf_cgindx.f:1–378 | 본문 인용과 코드의 입력·분기·출력 동작이 일치한다. 이 행의 구현 세부는 문서의 설명에 빠져 있다. | 공극률·기포영역·주변 상태에서 이동 장애물 셀과 새 경계면 번호를 구성한다. |
| KD1-830 | C | - | C | 예 | 3D2F vf_cgswp.f:1–86 | 보존 대상은 이동 장애물 경계가 아니라 기존 NUMB0개 경계이다. | 이동 장애물 경계를 재구성할 때 기존 `NUMB0`개 경계의 유속·압력·VOF·조도 값을 저장하거나 복원한다. |
| KD1-831 | C | - | C | 예 | 3D2F vf_cset2f.f:1–81 | 액상의 값을 그대로 복사하지 않는 IBVF=5 예외를 보완한다. | `IF (IBVG.EQ.0) THEN`에서 미지정 기상 경계조건을 보완한다. 그 안의 `IF (IBVF.NE.5) THEN`에서는 액상 경계종류·값을 복사한다. ELSE에서는 기상 종류를 1로 두고 유속·압력 경계값을 0으로 둔다. |
| KD1-832 | C | - | C | 예 | 3D2F vf_debug.f:1–61 | TNOW를 출력하며 지정 시각 선택 기능은 없다. 화면 표시 전용이 아닌 파일 입출력이므로 C이다. | 현재 시각·표지와 셀 상태·VOF·공극률의 진단 목록을 파일에 쓴다. |
| KD1-833 | C | - | C | 아니오 | 3D2F vf_fnfbub.f:1–75,271–291, vf_f1cal.f:202 | 본문 인용과 코드의 입력·분기·출력 동작이 일치한다. 이 행의 구현 세부는 문서의 설명에 빠져 있다. | 고립 기체·액체 상태 보정 코드를 담는다. 36행 RETURN 때문에 현재 호출은 아무 처리 없이 반환한다. |
| KD1-834 | C | - | C | 아니오 | 3D2F vf_iihidm.f:1–50 | 본문 인용과 코드의 입력·분기·출력 동작이 일치한다. 이 행의 구현 세부는 문서의 설명에 빠져 있다. | HIDEM YES·NO를 읽어 IHIDEM을 1·0으로 설정한다. |
| KD1-835 | C | - | C | 아니오 | 3D2F vf_jpcoef.f:1–207 | 본문 인용과 코드의 입력·분기·출력 동작이 일치한다. 이 행의 구현 세부는 문서의 설명에 빠져 있다. | HIDEM 압력 전달용 보조 포텐셜 방정식의 행렬·초기값을 만든다. |
| KD1-836 | C | - | C | 아니오 | 3D2F vf_jphdm1.f:1–239 | 본문 인용과 코드의 입력·분기·출력 동작이 일치한다. 이 행의 구현 세부는 문서의 설명에 빠져 있다. | HIDEM과 유체의 랭크·격자 범위·분할 대응을 교환한다. |
| KD1-837 | C | - | C | 예 | 3D2F vf_jphdm2.f:1–339 | ISW=0의 분기 밖에 압력 송신이 있다. 압력 계산 생략의 대상을 보조 풀이로 한정한다. | 유체 압력과 HIDEM 공극률·구조 속도를 교환한다. `ISW=0`은 보조 압력 방정식 풀이를 생략한다. 이 경우에도 압력 송신은 수행한다. |
| KD1-838 | A | A | C | 예 | 3D vf_p0barr.f:16–24, vf_zxmg_barri.f:22; 3D2F vf_p1barr.f:16–24, vf_zxmp_barri.f:23; 두 사본 diff -u | 배리어의 집합은 comm_model에서 MGCOMM으로 바뀐다. 그 변경을 2상류 물리 기능 때문이라고 판정할 근거는 없으므로 AD5의 A를 C로 고친다. | 유체 통신 집합의 동기화와 통신시간 계측을 수행한다. |
| KD1-839 | A | A | F | 예 | 3D2F vf_p1end.f:1–24; 3D vf_p0end.f; 두 사본 diff -u | 3D의 P0/ZXMG 대응 루틴과 diff -u에서 이름만 다르다. 실행문 의미가 같으므로 AD5의 A를 F로 고친다. | 유체 병렬 환경을 정상 종료한다. |
| KD1-840 | A | A | F | 예 | 3D2F vf_p1enda.f:1–27; 3D vf_p0enda.f; 두 사본 diff -u | 3D의 P0/ZXMG 대응 루틴과 diff -u에서 이름만 다르다. 실행문 의미가 같으므로 AD5의 A를 F로 고친다. | `MPI_COMM_WORLD`의 `MPI_ABORT` 호출 뒤에 종료 함수 호출문이 이어진다. |
| KD1-841 | A | A | C | 예 | 3D2F vf_p1init.f:1–34, vf_a1main.f:279–282; 3D2F 전체 rg CALL VF_P[01]INIT | 빈 실행 경로와 미호출 상태를 기록하는 행이다. 2상류 때문에 달라진 초기화라는 근거가 없으므로 AD5의 A를 C로 고친다. | 초기화라는 개요와 모듈 선언만 남긴 빈 루틴이다. 현재 실행문은 GOTO·RETURN이다. 메인은 이 루틴 대신 VF_P0INIT를 호출한다. |
| KD1-842 | A | A | F | 예 | 3D2F vf_p1time.f:1–25; 3D vf_p0time.f; 두 사본 diff -u | 3D의 P0/ZXMG 대응 루틴과 diff -u에서 이름만 다르다. 실행문 의미가 같으므로 AD5의 A를 F로 고친다. | VF_ZXMP_WTIME을 이용해 경과시간을 얻는다. |
| KD1-843 | C | - | C | 아니오 | 3D2F vf_v1eos.f:63–81,168–173; cad-2f-manual PDF pp.24,61(인쇄 486,523) | 문서는 기상 밀도와 물질미분을 정의한다. 코드 배열의 RHOG 정규화와 ISTATE=0 초기 반환을 함께 설명하지 않는다. | 기상 밀도·정규화 압력 미분·기상 밀도 물질변화율을 갱신한다. |
| KD1-844 | C | - | C | 예 | 3D2F vf_vpdrdt.f:1–166 | ALI·AUI·ALJ·AUJ·ALK·AUK도 갱신한다. 보고서에서 빠진 비대각 항을 추가한다. | 기상 밀도변화에 따른 압력 방정식의 대각·비대각·우변 항을 추가한다. |
| KD1-845 | A | A | F | 예 | 3D2F vf_zxmp_abort.f:1–31; 3D vf_zxmg_abort.f; 두 사본 diff -u | 3D의 P0/ZXMG 대응 루틴과 diff -u에서 이름만 다르다. 실행문 의미가 같으므로 AD5의 A를 F로 고친다. | MPI_COMM_WORLD를 고정 오류코드 77로 중단한다. |
| KD1-846 | A | A | F | 예 | 3D2F vf_zxmp_final.f:1–30; 3D vf_zxmg_final.f; 두 사본 diff -u | 3D의 P0/ZXMG 대응 루틴과 diff -u에서 이름만 다르다. 실행문 의미가 같으므로 AD5의 A를 F로 고친다. | MPI_FINALIZE를 호출한다. |
| KD1-847 | A | A | F | 예 | 3D2F vf_zxmp_init.f:1–30; 3D vf_zxmg_init.f; 두 사본 diff -u | 3D의 P0/ZXMG 대응 루틴과 diff -u에서 이름만 다르다. 실행문 의미가 같으므로 AD5의 A를 F로 고친다. | MPI 초기화 래퍼를 제공한다. MPI_INIT 호출은 CCC 주석이므로 현재는 초기화하지 않는다. |
| KD1-848 | A | A | F | 예 | 3D2F vf_zxmp_wtime.f:1–30; 3D vf_zxmg_wtime.f; 두 사본 diff -u | 3D의 P0/ZXMG 대응 루틴과 diff -u에서 이름만 다르다. 실행문 의미가 같으므로 AD5의 A를 F로 고친다. | MPI_WTIME 값을 반환한다. |
| KD1-849 | H | - | H | 아니오 | 3D Source code의 rg --files --hidden 결과: .DS_Store | 파일은 모델 소스가 아닌 디렉터리 메타데이터이다. | macOS 디렉터리 메타데이터이다. 모델 코드 대조 대상이 아니다. |
| KD1-850 | A | A | C | 예 | 3D VF_A0PRM_mpversion.h:2–17,53 | MAXLIN과 입력·병렬 상수를 가진 별도 헤더이다. 2상류 때문에 바뀐 코드라는 근거가 없어 AD5의 A를 C로 고친다. | 묶음 입력·병렬 입력 방식의 별도 상수 헤더 사본이다. |
| KD1-851 | A | A | C | 예 | 3D db_ini.f:43–144, vf_a1main.f:859 | 모델의 격자·공극률 파일 출력이다. 화면 표시 전용은 아니다. 호출은 CAKIY 주석이다. 2상류 변경 근거가 없어 AD5의 A를 C로 고친다. | 별도 그래픽 파일의 격자 초기정보를 쓴다. 메인의 DB_INI 호출은 비활성 주석이었다. |
| KD1-852 | A | A | C | 예 | 3D db_trn.f:62–130, vf_og1trn.f:101 | 비활성 호출은 메인이 아니라 VF_OG1TRN에 있다. 모델 결과 파일 출력이다. 2상류 변경 근거가 없어 AD5의 A를 C로 고친다. | 별도 그래픽 파일에 시각별 결과를 쓴다. `vf_og1trn.f:101`의 `CAKIY CALL DB_TRN`은 비활성 주석이다. |
| KD1-853 | A | A | C | 예 | 3D mod_apara.f:1–85,202–206,1074–1094; 3D/3D2F vf_pmgc2p.f diff @@ -11,7 +11,6 @@ | MOD_APARA는 부모 영역도 분할하는 네스팅 구현이다. 모듈 제거를 2상류 물리 변경으로 설명하는 근거가 없으므로 AD5의 A를 C로 고친다. | 영역분할 부모의 공극률·경계 버퍼 집산·분배 목록을 구성한다. 3D2F의 대응 PMGC2P 코드에는 MOD_APARA 사용문과 이 부모 분할 경로가 없다. |
| KD1-854 | A | A | C | 예 | 3D vf_cwmsrc.f:45–145; 3D/3D2F vf_a1main.f diff의 VF_CWMSRC 삭제 구간 | 조파 소스의 호출 제거는 확인된다. 삭제 자체를 2상류 기능으로 볼 근거는 없으므로 AD5의 A를 C로 고친다. | 내부 조파 소스 유속을 만든다. 3D2F는 이 기능 경로를 제거한다. |
| KD1-855 | A | A | C | 예 | 3D vf_cwmtb12.f:27–70; 3D/3D2F vf_a1main.f·vf_cwmak0.f diff의 MTBTYP2·IWVTYP=-4 삭제 구간 | 두 번째 조파행렬의 제거는 기능 지원 범위의 설명 누락이다. 2상류 때문에 바뀐 식이라는 근거가 없어 AD5의 A를 C로 고친다. | 두 번째 조파행렬 수위를 보간한다. 3D2F는 행렬2를 제거한다. |

### KD1-856–885

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| KD1-856 | A | A | C | 예 | 3D vf_cwmtb22.f:31–65; 3D/3D2F vf_bwffsf.f·vf_bwuwn.f diff의 행렬2 삭제 구간 | 두 번째 조파행렬의 제거는 기능 지원 범위의 설명 누락이다. 2상류 때문에 바뀐 식이라는 근거가 없어 AD5의 A를 C로 고친다. | 두 번째 조파행렬 유속을 보간한다. 3D2F는 행렬2를 제거한다. |
| KD1-857 | A | A | C | 예 | 3D vf_fgene.f:32–70, vf_f1cal.f:155; 3D2F vf_f1cal.f:143,207; 두 vf_f1cal.f diff -u | CAKIY 표지와 호출 비활성화는 확인된다. 면 VOF 추가는 별도 변경이다. 조파 생성항 제거가 2상류 기능 때문이라는 근거로 결합하지 않는다. 지원 범위 설명 누락 C로 판정하여 AD5의 A를 고친다. | 내부 조파 소스의 VOF 생성항을 만든다. 3D2F의 `vf_f1cal.f:143`에는 `CAKIY CALL FGENE(XX,ZZ,FF,WVU,QF,NF)`가 비활성 주석으로 남아 있다. |
| KD1-858 | A | A | A | 아니오 | 3D vf_fpvcpp.f:182–204; 3D/3D2F vf_f1cal.f·vf_iiopt.f diff; 3D2F vf_a1main.f:1347–1386 | 기포별 압력에서 2상 기상 밀도장 계산으로 바뀐 경로가 직접 대조된다. AD5의 A를 유지한다. | 3D는 영역별 기포 압력을 계산한다. 3D2F는 기상 상태방정식과 밀도·압력 반복을 쓴다. 판 근거는 `vf_f1cal.f`의 `VF_FPVCPP` 삭제와 `vf_iiopt.f`의 `PV=CONST`에서 `STATE`로 바뀐 diff이다. |
| KD1-859 | A | A | C | 예 | 3D vf_im2inp.f:1–5,46–64,179–180; 3D/3D2F vf_a1main.f diff의 VF_IM2INP 삭제 구간 | 입력 경로 제거는 확인된다. 2상류 계산 때문에 제거했다는 근거가 없어 AD5의 A를 C로 고친다. | 두 번째 조파행렬 파일을 읽는다. 3D2F는 해당 입력을 제거한다. |
| KD1-860 | A | A | C | 예 | 3D vf_p0barr.f:16–24, vf_zxmg_barri.f:22; 3D2F vf_p1barr.f:16–24, vf_zxmp_barri.f:23 | comm_model과 MGCOMM은 구분되는 통신 집합이다. 실행 범위 설명은 필요하지만 2상류 물리 변경의 근거가 없으므로 AD5의 A를 C로 고친다. | MG 통신 집합 배리어이다. 3D2F의 유체 배리어 역할은 VF_P1BARR가 맡는다. |
| KD1-861 | A | A | F | 예 | 3D vf_p0end.f:15–16; 3D2F vf_p1end.f:15–16; P0END/P1END 및 ZXMG_FINAL/ZXMP_FINAL diff -u | 대응 종료 함수의 이름만 바뀌고 MPI_FINALIZE 동작은 같다. AD5의 A를 F로 고친다. | 병렬 정상종료이다. 3D2F 메인은 VF_P1END를 호출한다. |
| KD1-862 | A | A | C | 예 | 3D vf_pcdc2p.f:1–6,45–92,196–212; 3D2F vf_pmgc2p.f:1–5 | 전용 파일의 부재만으로 판 차이가 되지는 않는다. 부모·자식 전송 방식의 설명 누락으로 판정하여 AD5의 A를 C로 고친다. | 자식 유체영역 정보를 부모로 보내는 별도 사본이다. 3D2F에는 PMGC2P 계열만 남는다. |
| KD1-863 | A | A | C | 예 | 3D vf_pcdp2c.f:1–6,45–76,144–162; 3D2F vf_pmgp2c.f:1–5 | 전용 파일의 부재만으로 판 차이가 되지는 않는다. 부모·자식 전송 방식의 설명 누락으로 판정하여 AD5의 A를 C로 고친다. | 부모 유체영역 정보를 자식으로 보내는 별도 사본이다. 3D2F에는 PMGP2C 계열만 남는다. |
| KD1-864 | A | A | H | 예 | 3D vf_pmgc2p._org:1–14,824–872; 3D2F vf_pmgc2p.f_org:1–14; 두 파일 diff -u | 이 행의 결론은 백업 파일의 이름과 존재에 관한 항목이다. 모델 동작의 판 차이가 아니므로 AD5의 A를 H로 고친다. | 3D의 `vf_pmgc2p._org`는 PMGC2P 백업 파일이다. `.f_org`와 파일명이 다르다. 파일명 차이는 모델 동작의 대조 대상이 아니다. |
| KD1-865 | A | A | A | 아니오 | 3D vf_stoc_1d.f:1–215; 3D2F vf_stoc_init.f:39–42; 두 vf_stoc_init.f 및 vf_a1main.f diff -u | 2FC 모델을 검사하는 명시적 분기에서 직접 STOC 접속을 끈다. 해당 3D 전용 통신 경로와 결합하여 AD5의 A를 유지한다. | STOC 접속부 접선속도 한 층을 교환한다. 3D2F는 직접 STOC 접속을 사용하지 않는다. 판 근거는 `vf_stoc_init.f:39–42`의 `if( my_model.eq.l_cadmas_2fc ) then` 안의 `NB_SC=0`과 `return` 추가 diff이다. |
| KD1-866 | A | A | A | 아니오 | 3D vf_stoc_area.f:1–237; 3D2F vf_stoc_init.f:39–42; 두 vf_stoc_init.f 및 vf_a1main.f diff -u | 2FC 모델을 검사하는 명시적 분기에서 직접 STOC 접속을 끈다. 해당 3D 전용 통신 경로와 결합하여 AD5의 A를 유지한다. | STOC와 유체 전체격자 좌표·접속영역을 교환한다. 3D2F는 직접 STOC 접속을 사용하지 않는다. 판 근거는 `vf_stoc_init.f:39–42`의 `if( my_model.eq.l_cadmas_2fc ) then` 안의 `NB_SC=0`과 `return` 추가 diff이다. |
| KD1-867 | A | A | A | 아니오 | 3D vf_stoc_fconv.f:1–91; 3D2F vf_stoc_init.f:39–42; 두 vf_stoc_init.f 및 vf_a1main.f diff -u | 2FC 모델을 검사하는 명시적 분기에서 직접 STOC 접속을 끈다. 해당 3D 전용 통신 경로와 결합하여 AD5의 A를 유지한다. | STOC 경계의 VOF 이류 플럭스를 조정한다. 3D2F는 직접 STOC 접속을 사용하지 않는다. 판 근거는 `vf_stoc_init.f:39–42`의 `if( my_model.eq.l_cadmas_2fc ) then` 안의 `NB_SC=0`과 `return` 추가 diff이다. |
| KD1-868 | A | A | A | 아니오 | 3D vf_stoc_obst.f:1–226; 3D2F vf_stoc_init.f:39–42; 두 vf_stoc_init.f 및 vf_a1main.f diff -u | 2FC 모델을 검사하는 명시적 분기에서 직접 STOC 접속을 끈다. 해당 3D 전용 통신 경로와 결합하여 AD5의 A를 유지한다. | STOC에서 장애물 지형을 받는다. 3D2F는 직접 STOC 접속을 사용하지 않는다. 판 근거는 `vf_stoc_init.f:39–42`의 `if( my_model.eq.l_cadmas_2fc ) then` 안의 `NB_SC=0`과 `return` 추가 diff이다. |
| KD1-869 | A | A | A | 아니오 | 3D vf_stoc_pors.f:1–259; 3D2F vf_stoc_init.f:39–42; 두 vf_stoc_init.f 및 vf_a1main.f diff -u | 2FC 모델을 검사하는 명시적 분기에서 직접 STOC 접속을 끈다. 해당 3D 전용 통신 경로와 결합하여 AD5의 A를 유지한다. | STOC에서 셀·면 공극률을 받는다. 3D2F는 직접 STOC 접속을 사용하지 않는다. 판 근거는 `vf_stoc_init.f:39–42`의 `if( my_model.eq.l_cadmas_2fc ) then` 안의 `NB_SC=0`과 `return` 추가 diff이다. |
| KD1-870 | A | A | A | 아니오 | 3D vf_stoc_recv.f:1–153; 3D2F vf_stoc_init.f:39–42; 두 vf_stoc_init.f 및 vf_a1main.f diff -u | 2FC 모델을 검사하는 명시적 분기에서 직접 STOC 접속을 끈다. 해당 3D 전용 통신 경로와 결합하여 AD5의 A를 유지한다. | STOC에서 경계값을 받는다. 3D2F는 직접 STOC 접속을 사용하지 않는다. 판 근거는 `vf_stoc_init.f:39–42`의 `if( my_model.eq.l_cadmas_2fc ) then` 안의 `NB_SC=0`과 `return` 추가 diff이다. |
| KD1-871 | A | A | A | 예 | 3D vf_stoc_send.f:1–462; 3D2F vf_stoc_init.f:39–42; 두 vf_stoc_init.f 및 vf_a1main.f diff -u | 2FC 모델을 검사하는 명시적 분기에서 직접 STOC 접속을 끈다. 해당 3D 전용 통신 경로와 결합하여 AD5의 A를 유지한다. 송신량 H/S는 총유량이 아니라 면적으로 나눈 플럭스이므로 표현을 고친다. | STOC에 면적·VOF 가중 유속·단위면적당 유량·수위를 보낸다. 3D2F는 직접 STOC 접속을 사용하지 않는다. 판 근거는 `vf_stoc_init.f:39–42`의 `if( my_model.eq.l_cadmas_2fc ) then` 안의 `NB_SC=0`과 `return` 추가 diff이다. |
| KD1-872 | A | A | F | 예 | 3D vf_zgetim.f:1–87; 3D2F vf_zgetln.f:1–87; 두 파일 diff -u; vf_im1inp.f diff -u | 차이는 루틴명·개요·오류 메시지의 루틴명뿐이다. 입력 동작이 같으므로 AD5의 A를 F로 고친다. | 행렬파일을 한 줄씩 읽고 단어로 나눈다. 3D2F는 VF_ZGETLN으로 합친다. |
| KD1-873 | A | A | C | 예 | 3D vf_zgetln_mpversion.f:33–42,52–89 | MAXLIN행을 묶어 읽고 분배하는 입력 구현이다. 2상류 물리 변경 근거가 없어 AD5의 A를 C로 고친다. | 묶음 줄 입력 VF_ZGETLN의 별도 병렬 사본이다. |
| KD1-874 | A | A | F | 예 | 3D vf_zgetln_mpversion.f.orig:1–87; 3D2F vf_zgetln.f:1–87; diff -u 결과 0행 | 원본 백업은 묶음 입력이 아니라 한 줄 입력이다. 3D2F VF_ZGETLN과 바이트가 같다. AD5의 A를 F로 고친다. | 3D의 `vf_zgetln_mpversion.f.orig`는 한 줄씩 읽어 단어를 분리하는 백업이다. 3D2F의 `vf_zgetln.f`와 내용이 같다. |
| KD1-875 | A | A | C | 예 | 3D vf_zxmp_gatheri.f:22–31 | MGCOMM의 0번 PE에 대한 모델 자료 집산·분배를 정하는 래퍼이다. MPI 라이브러리 내부가 아니다. 2상류 기능 변경 근거가 없어 AD5의 A를 C로 고친다. | 정수 고정길이 자료를 대표 PE에 모으는 래퍼이다. |
| KD1-876 | A | A | C | 예 | 3D vf_zxmp_gathervd.f:23–35 | MGCOMM의 0번 PE에 대한 모델 자료 집산·분배를 정하는 래퍼이다. MPI 라이브러리 내부가 아니다. 2상류 기능 변경 근거가 없어 AD5의 A를 C로 고친다. | 배정밀도 가변길이 자료를 대표 PE에 모으는 래퍼이다. |
| KD1-877 | A | A | C | 예 | 3D vf_zxmp_gathervi.f:23–35 | MGCOMM의 0번 PE에 대한 모델 자료 집산·분배를 정하는 래퍼이다. MPI 라이브러리 내부가 아니다. 2상류 기능 변경 근거가 없어 AD5의 A를 C로 고친다. | 정수 가변길이 자료를 대표 PE에 모으는 래퍼이다. |
| KD1-878 | A | A | C | 예 | 3D vf_zxmp_scattervd.f:23–35 | MGCOMM의 0번 PE에 대한 모델 자료 집산·분배를 정하는 래퍼이다. MPI 라이브러리 내부가 아니다. 2상류 기능 변경 근거가 없어 AD5의 A를 C로 고친다. | 대표 PE의 가변길이 실수 자료를 각 PE에 분배하는 래퍼이다. |
| KD1-879 | E | E 유지(강함) | E · 강함 | 예 | 3D2F vf_bwuwt.f:31–41,60–75,136–182; vf_iiboun.f:153–156,196–222; 3D vf_bwuwt.f:151–163; 3D2F BCVI 대입 rg | 경계면별 배열 설명과 3D 대응 호출이 상 첨자 사용에 모두 모순된다. 입력·재배열 경로도 경계면 번호를 보존한다. E3의 강함을 유지한다. | BCVI의 첨자는 경계면 번호 L이다. LGF는 2 또는 3인 상 구분이다. 3D2F는 `CALL VF_CLOGKS(DL,VA,BCVI(LGF),ANU1,VT)`를 호출한다. 자기 배열 설명과 3D의 `BCVI(L)` 호출에 모순되는 코드 결함 후보이다. 파서의 `IF (LGF.EQ.2) BCVI(L)=BT`도 경계면 첨자를 사용한다. 상별 조도 재배열은 없다. `IB.EQ.8`이고 `VA.LT.ZERO .OR. AN.LT.ZERO`가 거짓인 경로에서 잘못된 경계면 조도를 읽을 수 있다. 근거 강도는 강함이다. |
| KD1-880 | E | E 유지(강함) | E · 강함 | 아니오 | 3D2F vf_a1main.f:860,895–903,1244–1252; Simulators 전체 rg -n -i '\bLBQC\b': vf_a1main.f:900 한 줄 | LEQC를 검사하는 현재 분기와 LEQC를 사용하는 후속 재할당에 모두 모순된다. 전체 검색에서 LBQC 초기화나 공유 선언이 없다. E3의 강함을 유지한다. | 초기 이동 경계 재할당의 `IF (NUMB.GT.NUMB0) THEN` 안에서 `IF (2*LEQC.GT.3) THEN`이면 `ALLOCATE(WKBC(2*NUMB*LBQC),STAT=IERR)`를 실행한다. LBQC는 초기화되지 않은 암시적 정수이다. 후속 재할당은 `LEQC`를 사용한다. Simulators 전체의 `rg -n -i '\bLBQC\b'` 결과는 `vf_a1main.f:900` 한 줄이다. LBQC를 설정하거나 별도로 선언하는 반대 경로는 없다. 코드 결함 후보의 근거 강도는 강함이다. |
| KD1-881 | E | E 유지(강함) | E · 강함 | 아니오 | 3D2F vf_f1cal.f:1–10,109–111,157–162; vf_a1main.f:1433–1438; 3D vf_f1cal.f:1–13, vf_a1main.f:1104–1115; 두 vf_f1cal.f diff -u | 날짜 표지는 존재하지만 현재 호출·선언 및 루틴 내부 배열 사용이 서로 맞지 않는다. 3D의 정상 구분·전달은 불일치를 의도한 설계로 설명하지 못한다. E3의 강함을 유지한다. | 3D2F의 7행 NWK1 뒤에는 쉼표가 없다. 고정형식에서 다음 연속행 DELH와 이어 읽으면 이름은 NWK1DELH가 된다. NWK1과 DELH가 두 인수로 분리되지 않는다. 메인의 호출은 NWK1에서 끝나며 DELH·DELH_IN을 넘기지 않는다. 반대 근거로 2016.09 날짜 표지와 3D의 2012.03 선언을 확인했다. 3D는 앞 인수 뒤에 쉼표가 있고 DELH·DELH_IN을 넘긴다. 3D2F 본문은 ISEABT!=0일 때 두 배열을 VF_FSEABT로 넘긴다. 날짜 표지는 불완전한 이식의 위치를 설명하지만 호출·선언 불일치를 해소하지 않는다. 근거 강도 강함. |
| KD1-882 | E | E 유지(강함) | E · 강함 | 아니오 | 3D2F vf_sdiff.f:1–2,41–49,74–84; vf_s1cal.f:95–97; vf_k1cal.f:129–130,142–143; vf_a1main.f:1413–1418; vf_iiequa.f:52–56; cad-2f-manual PDF p.121 | 새 선언과 정상 난류 호출이 각각 농도 호출의 FF 누락을 드러낸다. 정의·ENTRY·INTERFACE 검색에 대체 인터페이스가 없다. 문서와 파서는 농도 계산을 허용한다. E3의 강함을 유지한다. | 새 VF_SDIFF는 ZZ 다음에 FF·CC를 받는다. 농도 드라이버는 FF 없이 CC부터 넘긴다. 전체 인수 수가 하나 적고 뒤 인수가 한 칸씩 밀린다. 반대 근거로 같은 판 난류 드라이버를 확인했다. 난류 호출은 FF를 넘긴다. 온도·농도 드라이버에서 별도 오버로드나 인수 보정 경로는 없다. 적용 조건은 LEQC>0이다. 근거 강도 강함. |
| KD1-883 | E | E 유지(강함) | E · 강함 | 아니오 | 3D2F vf_sdiff.f:1–2,41–49,60–62; vf_t1cal.f:90–91; vf_k1cal.f:129–130; vf_a1main.f:1404–1409; vf_iiequa.f:41–49; cad-2f-manual PDF pp.2,121 | 새 선언과 정상 난류 호출에 모두 모순된다. 기본 방정식에 에너지를 포함하지 않는다는 설명과 별개로 TEMPERATURE CALC 입력·실행 경로가 있다. 다른 인터페이스는 없다. E3의 강함을 유지한다. | 온도 드라이버는 새 VF_SDIFF에 FF를 넘기지 않는다. 실제 인수는 17개이고 새 선언은 18개이다. TT부터 순서가 밀려 기존 NF가 새 FLCW 자리에 들어간다. 마지막 INDC 인수도 없다. 반대 근거로 같은 판의 난류 호출을 확인했다. 난류 호출은 새 인수 순서를 따른다. 적용 조건은 LEQT!=0이다. 근거 강도 강함. |
| KD1-884 | E | E 유지(중간) | E · 중간 | 아니오 | 3D2F vf_a1main.f:568–577,860–903,1140–1153,1197–1242; vf_cgindx.f:232–237; vf_bwke.f:34–48; sf_alloc1.f:44–75; sf_str2.f:32; sf_stm2.f:14 | 현재 NUMB 갱신과 난류 경계 참조가 맞지 않는다. 구조·STM의 정상 재할당도 반대되는 독립 근거이다. 파일 기반 비연성 경로에는 그 호출이 없다. 조합 의존성을 반영하여 E3의 중간을 유지한다. | 파일 기반 이동 장애물은 NUMB를 바꾸지만 INDBK·INDBE·INDBT·INDBC의 확대·재구성을 주석으로 남긴다. 실제 난류 경계 루프는 1~NUMB의 INDBK·INDBE를 읽는다. 반대 근거로 SF_ALLOC1을 확인했다. 구조·STM 드라이버의 SF_ALLOC1은 해당 배열을 재할당한다. 파일 기반 이동 장애물의 이 메인 분기는 그 보정 경로를 호출하지 않는다. 적용 조건은 이동으로 새 경계가 생기고 난류·온도·농도 중 해당 방정식을 켠 경우이다. 근거 강도 중간. |
| KD1-885 | E | E 유지(강함) | E · 강함 | 예 | 3D2F vf_vpdrdt.f:34,77–118,130–156; vf_v1eos.f:83–105,126–137; user_eos.f:23–34; vf_v1cal.f:357–372; cad-2f-manual PDF pp.3,61 | 자기 주석과 y·z 계수 경로가 I+1을 지지한다. 표면셀 복사는 전체 기상셀의 좌우 미분을 같게 만들지 않는다. 후속 풀이 전에 상쇄 보정도 없다. E3와 같은 강함이다. 보고서의 WUC<=0 영향 조건은 WUC<0으로 고친다. | `IF(WUC.GT.0.0D0) THEN`의 ELSE에서 `IF(NF(I+1,J,K).GT.0) THEN`이면 `AUI(I,J,K) = AUI(I,J,K) + DCOEF*DRHODP(I-1,J,K)`를 실행한다. 주석은 I+1의 밀도 차분을 적는다. y·z의 같은 분기는 J+1·K+1의 압력 미분을 읽는다. 이 불일치는 코드 결함 후보이다. 제공 상태방정식에서는 ISTATE=1일 때 해당 계산을 수행한다. 실제 계수 차이는 현재 셀과 I+1의 NF가 양수이고 WUC<0이며 AVL이 0이 아니고 양쪽 DRHODP가 다를 때 생긴다. WUC=0이면 DCOEF도 0이다. 의도된 반대 첨자나 후속 상쇄 보정은 없다. 근거 강도는 강함이다. |

### KD1-886–913

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| KD1-886 | B | B | B | 아니오 | models/CADMAS-SURF/source-analysis/cadmas-2f-stier-and-hidem-dem-coupling.md:21–26; 두 Source code의 rg --files --hidden, diff -qr, 공통 변경 파일 diff -u 120개 | 같은 노트가 변밀도 추가를 적으면서 공유 이름만으로 재분석 불요라고 쓴다. 동일 115개와 변경 120개가 실제 파일 비교로 구분된다. 672는 변경 파일의 diff -u 구간을 합산한 값이다. AD5의 B를 유지한다. | 같은 vf 이름의 변경을 생략하면 안 된다. 바이트 동일 파일 115개만 3D 판독으로 대신한다. 나머지 공통 파일 120개는 차이 구간 672개를 대조한다. |
| KD1-887 | C | - | C | 아니오 | models/CADMAS-SURF/source-analysis/cadmas-2f-stier-and-hidem-dem-coupling.md:24; 3D2F vf_veuler.f:138–152, vf_cfxyz.f:1–13, vf_bwuwg.f:60–96; vf_a1main.f·vf_sdiff.f·vf_og1trn.f의 사본 diff | 변밀도항 이외에도 이전 유속·면 VOF·이동벽·수송 인터페이스가 변경된다. 기존 노트가 생략한 동작을 보완하는 C이다. | 3D2F는 변밀도 외에도 면 VOF, 기상·이동벽 경계, 이전 유속, 공극률 변화, 계산상태, 수송 인수, 출력 형식을 바꾼다. |
| KD1-888 | C | - | C | 예 | models/CADMAS-SURF/source-analysis/cadmas-2f-stier-and-hidem-dem-coupling.md:26; 3D2F vf_bwke.f:115–117, vf_cfxyz.f:1–13, vf_iimate.f:35–60, vf_sdiff.f:74–84 | 보고서의 vf_bwke.f:118은 빈 줄이다. 혼합 난류량의 실제 대입은 116–117행이다. 해당 처리가 EOS 목록 밖에 있으므로 C를 유지한다. | 기상 EOS 집합 외에도 면 VOF·상별 벽조건·혼합 난류량·상별 초기값·수송 계산영역이 달라진다. |
| KD1-889 | A | A | A | 아니오 | models/CADMAS-SURF/source-analysis/cadmas-2f-stier-and-hidem-dem-coupling.md:30–36; 3D2F mod_comm.f90:41,55–58; vf_stoc_init.f:39–42; vf_jphdm1.f:1–17; 두 mod_comm.f90·vf_stoc_init.f diff | 2FC의 자기 모델 표지와 직접 STOC 연결을 제외하는 분기가 함께 있다. AD5의 A를 유지한다. | HIDEM은 2FC와 별도 MPMD 통신 집합을 쓴다. 이 2FC 사본은 직접 STOC 접속을 사용하지 않는다. 판 근거는 `vf_stoc_init.f:39–42`의 `if( my_model.eq.l_cadmas_2fc ) then` 안에 추가된 `NB_SC=0`과 `return`의 사본 diff이다. STM은 별도 연성 모델이다. |
| KD1-890 | B | B | B | 아니오 | models/CADMAS-SURF/source-analysis/cadmas-2f-stier-and-hidem-dem-coupling.md:40; 3D2F sf_c_mpi_comm_rank.f:1–9; cad-str-instr-cadmas PDF p.23 | 문서는 SF_C_MPI를 CADMAS와 STR의 통신으로 설명한다. 코드도 Fortran MPI 호출이다. C 언어 바인딩으로 쓴 노트의 오기이므로 AD5의 B를 유지한다. | sf_c_mpi_*는 COMM_2FC_STR를 사용하는 Fortran 통신 래퍼이다. C 언어 바인딩이라는 뜻으로 쓰지 않는다. |
| KD1-891 | B | B | B | 아니오 | models/CADMAS-SURF/source-analysis/cadmas-2f-stier-and-hidem-dem-coupling.md:41; 3D2F mod_comm.f90:26,35,58, sf_stm_c_mpi_comm_rank.f:3–7, sf_stm_comm_init.f:1–69 | STM과 STOC는 모델 번호·이름·통신 집합이 다르다. 같은 코드의 명칭을 혼동한 노트의 오기이므로 AD5의 B를 유지한다. | sf_stm_*는 STM 연성의 통신·수평 격자 집산·분배이다. STOC 직접 접속용 vf_stoc_*와 구분한다. |
| KD1-892 | C | - | H | 예 | models/CADMAS-SURF/source-analysis/cadmas-2f-stier-and-hidem-dem-coupling.md:46; 3D2F Source code의 rg --files --hidden 목록 | 행의 최종 문장은 파일 포섭 개수와 검수 상태를 다룬다. 모델 동작의 문서 누락이 아니므로 H로 고친다. | 3D2F Source code의 일반 파일은 411개이다. 그중 `.f`·`.f90` 파일은 388개이다. 파일 포섭 개수는 검수 범위에 관한 기록이다. |
| KD1-893 | C | - | C | 아니오 | models/CADMAS-SURF/source-analysis/cadmas-2f-twophase-compressible-gas.md:20; 3D/3D2F vf_iimdl.f·vf_iiopt.f·vf_ii1inp.f·vf_stoc_init.f·vf_a1main.f diff | 공통 기반에 기능을 추가했다는 요약에는 삭제된 입력·실행 경로가 빠져 있다. 물리·실행 범위를 보완하는 C이다. | 3D2F는 2상·기상 압축성·구조·STM·HIDEM을 추가한다. 내부 조파 소스·행렬2·자동 재시작·STOC 직접 경로 일부는 3D 사본에만 있다. |
| KD1-894 | C | - | C | 아니오 | models/CADMAS-SURF/source-analysis/cadmas-2f-twophase-compressible-gas.md:26–39; 3D2F vf_a1main.f:1–9, vf_v1eos.f:63–74, user_eos.f:23–38, vf_vpdrdt.f:77–88; cad-2f-manual PDF pp.2–3,142 | 비압축성이라는 메인 주석을 적용 범위 전체로 확대할 수 없다. 매뉴얼과 코드에 있는 ISTATE별 선택 조건이 노트의 해석대상 문장에 빠져 있다. | 메인 주석은 기액 2상 비압축성 유체라고 적는다. ISTATE=0은 상수 기상 밀도를 쓴다. ISTATE=1은 등온 기상 EOS와 밀도변화 압력항을 쓴다. |
| KD1-895 | B | B | B | 아니오 | models/CADMAS-SURF/source-analysis/cadmas-2f-twophase-compressible-gas.md:39,53–62; 3D2F vf_v1eos.f:168–172, vf_vpdrdt.f:95–96,154–156; cad-2f-manual PDF pp.24,61 | 같은 노트의 Poisson 적용 설명과 실제 계산식은 (1-F)를 압력항에서 곱한다. VF_V1EOS의 168행 주석에는 (1-F)가 있지만 실행 식에는 없다. AD5의 B를 유지한다. | DRHODT는 코드의 GGV 가중 시간항과 기상 밀도 이류항을 RHOG로 나눈 값이다. 이 배열에 (1-F)를 미리 곱한다고 쓰지 않는다. 압력항은 AVL=(1-FF)*셀체적을 따로 곱한다. |
| KD1-896 | B | B | B | 아니오 | models/CADMAS-SURF/source-analysis/cadmas-2f-twophase-compressible-gas.md:43–49; 3D vf_vgene.f:80; 3D2F vf_vgene.f:100–103, vf_iimate.f:35–46; 두 vf_vgene.f diff | 같은 노트는 RHO0(2)를 기상으로 정의한다. 따라서 그 기상을 포함하는 혼합식을 단상이라고 부른 설명은 내부 모순이다. AD5의 B를 유지한다. | RHO0(2)를 쓰는 !! 대안도 상수 밀도 기상을 갖는 2상식이다. 3D 사본의 역밀도는 스칼라 RHO0의 역수이다. |
| KD1-897 | C | - | C | 아니오 | models/CADMAS-SURF/source-analysis/cadmas-2f-twophase-compressible-gas.md:68; 3D2F vf_a1main.f:1347–1386, vf_a2dflt.f:47–48; cad-2f-manual PDF p.142 | 오차 계산과 완화의 순서를 원문대로 구분한다. 기본 반복 횟수와 NF=8 오차 범위를 보완하는 C이다. | 기체셀 오차를 완화 이전 밀도로 계산한다. 내부 셀 밀도에 완화를 적용한다. VF_V1CAL을 호출한 뒤 오차가 SERROR 이하면 반복을 끝낸다. MAXITR 기본값은 1이다. |
| KD1-898 | C | - | C | 아니오 | models/CADMAS-SURF/source-analysis/cadmas-2f-twophase-compressible-gas.md:82; 3D2F vf_cdtcal.f:75–89,115–145; 두 vf_cdtcal.f diff | RHO0 혼합은 LEQT 분기의 열확산 제한이다. C2F 주석은 기상 경계 유량을 제외하던 옛 조건을 보존한다. 노트의 계산 범위 설명을 보완하는 C이다. | 시간간격 루틴은 실제 RHOG 대신 상수 RHO0(1/2)의 FF 혼합밀도를 열확산 제한에 쓴다. 기상 경계 유량도 이류 제한에 포함한다. 음향 파속 제한식은 이 diff에 추가하지 않는다. |
| KD1-899 | H | - | H | 예 | models/CADMAS-SURF/source-analysis/cadmas-2f-twophase-compressible-gas.md:84; cad-2f-manual PDF p.2(인쇄 464) | 적용 목적은 코드 수식과 직접 대조하는 대상이 아니다. 영어판 개요는 충격파압이 작용하는 케이슨에 대한 기상 압축 효과 도입을 설명한다. | 영어판 개요는 충격파압이 작용하는 케이슨에 대한 기상 압축 효과를 개발 배경으로 설명한다. 이 적용 목적은 코드 대조 대상이 아니다. |
| KD1-900 | C | - | C | 아니오 | models/CADMAS-SURF/source-analysis/cadmas-2f-structure-coupling-cutcell.md:19; 3D2F Source code의 sf_*.f·sf_*.f90 목록; sf_str_obst.f:63–74, sf_str2.f:22–43, sf_bc_reset.f:67–75, sf_cinit.f:40–54; cad-str-instr-cadmas PDF pp.7,13–14 | 교차체적 산출만으로 연성 갱신이 끝나지 않는다. 노트가 생략한 셀·면 상태와 경계·유체장 재구성을 보완한다. | sf_* .f·.f90 파일은 144개이다. 구조물 교차체적은 셀·면 공극률을 바꾼다. 그 뒤 셀·면 상태와 경계조건·유체장을 재구성한다. |
| KD1-901 | C | - | C | 아니오 | models/CADMAS-SURF/source-analysis/cadmas-2f-structure-coupling-cutcell.md:47–48; 3D2F mod_comm.f90:26,35,58, sf_stm1.f:14, sf_stm2.f:8–14, sf_stm_comm_init.f:1–69 | 소스는 STM이라는 모델명과 수심·지형 교환 동작을 정의한다. 영문 확장형 대신 확인되는 모델명과 연성 동작으로 기술한다. | 이 보고서에서는 원문 모델명 STM을 유지한다. STM 수심·지형 연성과 STOC 직접 접속을 구분한다. 원문에 없는 영문 약어 확장형을 단정하지 않는다. |
| KD1-902 | B | B | B | 예 | models/CADMAS-SURF/source-analysis/cadmas-2f-structure-coupling-cutcell.md:52; 3D2F sf_pos_update2.f:28–49, sf_array.f90:65–75; cad-str-instr-cadmas PDF pp.4,8 | 좌표와 다르시 유속을 변위와 구조 속도로 쓴 것은 변수 정의의 오기이다. AD5의 B를 유지한다. 수신 조건과 실제 인용 줄을 보완한다. | `TNEXT = TNOW + DT`이다. `IF( TNEXT > TSTR2 ) THEN` 안의 `IF( MYRANK == 0 ) THEN`에서 POS20을 받는다. POS20은 구조물 절점 위치 좌표이다. `IF( IGEO == 1 ) CALL SF_C_MPI_RECV_D(DVEL20,NELM0*3,IROOTS)`는 요소별 지반 다르시 유속을 받는다. 두 수신은 `sf_pos_update2.f:39–40`에 있다. |
| KD1-903 | B | B | B | 예 | models/CADMAS-SURF/source-analysis/cadmas-2f-structure-coupling-cutcell.md:56; 3D2F sf_rface0.f:13–30 | 법선 z성분이 -sin85°보다 작으면 거의 아래를 향한다. 연직면이라는 해석은 삼각함수 조건과 모순된다. AD5의 B를 유지한다. 분류 대상 요소 조건을 보완한다. | `IF( IELM(3,IE) == 2 ) THEN`인 요소 표면을 분류한다. `CR1 = -DSIN( 85.D0 / 180.D0 * PI )`이다. `CR2 =  DSIN( 15.D0 / 180.D0 * PI )`이다. `IF( E(3) < CR1 ) THEN`이면 IRFACE를 1로 둔다. `ELSEIF( E(3) > CR2 ) THEN`이면 IRFACE를 2로 둔다. 첫 조건은 거의 아래를 향하는 법선이다. |
| KD1-904 | A | A | A | 아니오 | models/CADMAS-SURF/source-analysis/cadmas-surf3d-smac-velocity-pressure-solver.md:68; 3D vf_vmodif.f:201–206; 3D2F vf_vmodif.f:100–111,318–328; 두 vf_vmodif.f diff | 2상 혼합 역밀도를 유속 보정에 넣는 동시에 포텐셜의 압력 환산을 바꾼다. C2F로 남은 옛 식도 판 근거이다. AD5의 A를 유지한다. | 3D의 `RT=RHO0/DTNOW` 압력 환산은 3D 사본에 한정한다. 3D2F는 `PP(I,J,K)=PP(I,J,K)-PT(I,J,K)/DTNOW`를 쓴다. 유속 보정에는 면 혼합 역밀도 RI를 곱한다. 판 근거는 `vf_vmodif.f:319`의 `C2F   RT=RHO0/DTNOW`와 3D/3D2F의 압력·유속 보정 diff이다. |
| KD1-905 | A | A | C | 예 | models/CADMAS-SURF/source-analysis/cadmas-surf3d-vof-free-surface.md:29; 3D vf_f1cal.f:155; 3D2F vf_f1cal.f:143,207; 두 vf_f1cal.f diff | CAKIY 표지와 호출 비활성화는 확인된다. 면 VOF 추가는 별도 변경이다. 조파 생성항 제거가 2상류 기능 때문이라는 근거로 결합하지 않는다. 지원 범위 설명 누락 C로 판정하여 AD5의 A를 고친다. | VF_FGENE 호출은 3D 사본의 순서이다. 3D2F는 내부 조파 생성항을 제거하고 갱신 뒤 면 VOF를 구성한다. |
| KD1-906 | A | A | C | 예 | models/CADMAS-SURF/source-analysis/cadmas-surf3d-wave-generation-and-boundaries.md:42; 3D/3D2F vf_cwmak0.f diff @@ -55,8 +55,6 @@; vf_iimdl.f diff @@ -64,9 +64,6 @@; vf_a1main.f의 행렬2 삭제 diff; 3D vf_cwmtb12.f:65–70, vf_cwmtb22.f:56–65 | 행렬2 입력·호출 삭제는 확인된다. 2상류 물리 때문에 바뀐 처리라는 근거는 없다. 지원 범위를 설명하지 않은 C로 판정하여 AD5의 A를 고친다. | IWVTYP=-4와 VF_CWMTB12/22는 3D 사본에 한정한다. 3D2F는 두 번째 조파행렬 입력·배열·호출을 제거한다. |
| KD1-907 | A | A | C | 예 | models/CADMAS-SURF/source-analysis/cadmas-surf3d-turbulence-and-porous-resistance.md:72; 3D vf_vgene.f:99–126; 3D2F vf_vgene.f:119–127; 두 vf_iiopt.f·vf_vgene.f diff | DRAG-DF 선택 제거와 기본 이차항력 유지는 확인된다. 제거 자체가 2상류 기능 때문이라는 근거는 없으므로 지원 범위 설명 누락 C로 판정한다. AD5의 A와 다르다. | DRAG-DF와 입경 계수표 대안은 3D 사본에 한정한다. 3D2F는 해당 입력과 운동량 생성항 분기를 제거한다. 기본 이차항력은 남긴다. |
| KD1-908 | A | A | A | 아니오 | models/CADMAS-SURF/source-analysis/cadmas-surf3d-timestep-nesting-stoc-coupling.md:57; 두 mod_comm.f90 diff @@ -32,13 +32,13 @@; 3D2F mod_comm.f90:41,58,213–221; vf_stoc_init.f:39–42 | 2FC의 자기 모델 선택과 통신 집합 구성이 MG 사본과 다르다. 명시적인 2FC 선택 표지가 있으므로 AD5의 A를 유지한다. | 3D의 자기 모델은 l_cadmas_mg이다. 3D2F는 l_cadmas_2fc이다. 판 근거는 `mod_comm.f90:41`의 자기 모델 대입 변경 diff이다. 3D2F는 STM 집합을 구성한다. `vf_stoc_init.f:39–42`는 2FC의 직접 STOC 접속을 조기 반환한다. |
| KD1-909 | A | A | A | 아니오 | models/CADMAS-SURF/source-analysis/cadmas-surf3d-entrapped-air-pressure.md:51; 3D vf_iiopt.f:79–86, vf_fpvcpp.f:182–202; 3D2F vf_iiopt.f:80–101, vf_a1main.f:1347–1386; 두 vf_iiopt.f·vf_f1cal.f diff | 기포별 압력식에서 압축성 기상 밀도장과 압력 반복으로 바뀐 판 차이이다. AD5의 A를 유지한다. | PV=CONST와 PVCGM의 기포별 폴리트로픽 경로는 3D 사본에 한정한다. 3D2F는 STATE와 기상 밀도·압력 반복을 쓴다. 판 근거는 `vf_iiopt.f`의 `PV=CONST` 삭제와 `STATE` 추가 diff 및 `vf_f1cal.f`의 `VF_FPVCPP` 호출 삭제이다. |
| KD1-910 | B | B | B | 예 | models/CADMAS-SURF/manual-notes/cadmas-2f-manual-compressibility.md:33; 3D2F vf_a2dflt.f:47–48, vf_iiopt.f:81–87, user_eos.f:23–34; cad-2f-manual PDF p.142(인쇄 604) | 매뉴얼의 ISTATE 기본값 표와 코드가 모두 0이다. 동작 확인용 등온 사용자 함수를 기본 선택으로 혼동한 노트의 오기이다. AD5의 B를 유지한다. 노트의 인쇄 603쪽은 604쪽으로 고친다. | 코드 기본값은 ISTATE=0이다. OPTION STATE 1을 입력해야 등온 이상기체 분기를 선택한다. 영어판의 해당 입력 표는 PDF 142쪽의 인쇄 604쪽이다. |
| KD1-911 | B | B | B | 아니오 | models/CADMAS-SURF/manual-notes/cadmas-2f-manual-compressibility.md:52; 3D2F vf_iiopt.f:89–101, A11111.in:705–712; cad-2f-manual PDF p.142(인쇄 604) | 영어판도 DENS_ERROR라고 인쇄했다. 코드 입력명과 구두점 한 글자가 다르므로 철자 오기로 판정한다. 문서 문자열이므로 F로 처리하면 실제 입력에서 실패한다. AD5의 B를 유지한다. | 코드 입력 키워드는 DENS-ERROR이다. 밑줄 표기 DENS_ERROR를 코드 키워드로 쓰지 않는다. |
| KD1-912 | C | - | H | 예 | models/CADMAS-SURF/README.md:30; 두 Source code의 rg --files --hidden 및 diff -qr | Fortran 파일 수와 검수 범위의 기록이다. 모델 동작의 문서 누락이 아니므로 H로 고친다. | 3D2F는 Fortran .f·.f90 388개와 일반 파일 전체 411개를 구분한다. 같은 이름의 바이트 차이 120개와 3D2F 전용 176개를 이 보고서에 연결한다. |
| KD1-913 | H | - | H | 예 | models/CADMAS-SURF/README.md:5; cadmas-3d2f-vs-3d.md §4 KD1-913 | 전수 검수 완료는 작업 상태 문구이다. 물리식·수치 구현·입출력 동작과 대조할 명제가 아니므로 H를 유지한다. | 전수 검수 완료는 파일·문서 검수 범위에 관한 작업 상태 문구이다. 모델 동작의 코드 대조 대상이 아니다. |

대상 148행: 유지 85, 변경 63
