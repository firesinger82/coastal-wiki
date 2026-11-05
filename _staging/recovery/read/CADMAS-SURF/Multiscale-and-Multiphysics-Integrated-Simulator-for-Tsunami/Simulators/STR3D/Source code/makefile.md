---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/makefile
lines: 98
sha256: 8871b3a013988bdec6366937040e7b40a2aa2f34a44bebb6fcac9d3dbae08041
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# makefile — 판독 구간 기록

구간은 1행부터 98행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | 컴파일러(compiler)·옵션·명명·아카이버(archiver)를 export한다. FCOMP=mpiifort, FOPT=-no-heap-arrays, CCOMP=mpicc, COPT는 빈 값, FNAME=LOWER_CASE_, ARC=ar r이다. 빈 줄을 포함한다. 원문: `export FCOMP=mpiifort` (1); `export FOPT=-no-heap-arrays` (2); `export CCOMP=mpicc` (3); `export COPT=` (4); `export FNAME=LOWER_CASE_` (5); `export ARC=ar r` (6). |
| 8–26 | 외부 라이브러리 경로와 링크 옵션. METIS는 ../lib, BLAS는 ../BLAS-3.7.0, ScaLAPACK은 ../scalapack-2.0.2, MUMPS는 ../MUMPS_4.10.0이다. 각각 -lmetis·-lblas·-lscalapack·-ldmumps -lmumps_common -lpord를 지정한다. ALL_L은 BLAS·SCALAPACK·MUMPS 대상이고 LIBS는 MUMPS·SCALAPACK·BLAS·METIS 순이다. 버전 문자열과 명령 옵션을 보존한다. 원문: `METIS_DIR=../lib` (8); `BLAS_DIR=../BLAS-3.7.0` (9); `SCALAPACK_DIR=../scalapack-2.0.2` (10); `MUMPS_DIR=../MUMPS_4.10.0` (11); `LIBMETIS=-L$(METIS_DIR) -lmetis` (13); `BLAS=blas_l` (15); `LIBBLAS=-L$(BLAS_DIR) -lblas` (16); `SCALAPACK=scalapack_l` (18); `LIBSCALAPACK=-L$(SCALAPACK_DIR) -lscalapack` (19); `MUMPS=mumps_l` (21); `LIBMUMPS=-L$(MUMPS_DIR)/lib  -ldmumps -lmumps_common -lpord` (22); `ALL_L=$(BLAS) $(SCALAPACK) $(MUMPS)` (24); `LIBS=$(LIBMUMPS) $(LIBSCALAPACK) $(LIBBLAS) $(LIBMETIS)` (25). |
| 27–40 | all의 라이브러리·디렉터리 대상 목록과 str.exe 링크. 객체는 각 디렉터리 와일드카드와 input/*/*.o에서 모으며 LIBS를 뒤에 붙인다. blas_l은 make double, scalapack_l은 make lib, mumps_l은 make d를 각 경로에서 호출한다. 명령은 판독만 했다. 원문: `all : $(ALL_L) module_o contact_o femap_o geo_o glb_comm_o input_o input_Count_data_o input_Read_data_o \` (27); `      input_Set_table_o main_o mpi_comm_o partition_o seq_o src_o util_o` (28); `	$(FCOMP) -o str.exe module/*.o contact/*.o femap/*.o geo/*.o glb_comm/*.o input/*.o input/*/*.o \` (29); `                 main/*.o mpi_comm/*.o partition/*.o seq/*.o src/*.o util/*.o $(LIBS)` (30); `blas_l :` (32); `	cd $(BLAS_DIR) ; make double` (33); `scalapack_l :` (35); `	cd $(SCALAPACK_DIR) ; make lib` (36); `mumps_l :` (38); `	cd $(MUMPS_DIR) ; make d` (39). |
| 41–67 | module_o부터 input_Set_table_o까지 하위 빌드 대상. 각 디렉터리로 cd한 뒤 make all을 실행하도록 적는다. module·contact·femap·geo·glb_comm·input·input/Count_data·input/Read_data·input/Set_table의 명령 줄을 그대로 보존한다. 원문: `module_o :` (41); `	cd module ; make all` (42); `contact_o :` (44); `	cd contact ; make all` (45); `femap_o :` (47); `	cd femap ; make all` (48); `geo_o :` (50); `	cd geo ; make all` (51); `glb_comm_o :` (53); `	cd glb_comm ; make all` (54); `input_o :` (56); `	cd input ; make all` (57); `input_Count_data_o :` (59); `	cd input/Count_data ; make all` (60); `input_Read_data_o :` (62); `	cd input/Read_data ; make all` (63); `input_Set_table_o :` (65); `	cd input/Set_table ; make all` (66). |
| 68–85 | main_o·mpi_comm_o·partition_o·seq_o·src_o·util_o 하위 빌드 대상. 각 디렉터리의 make all 명령과 공백 줄을 보존한다. 이 기록에서 명령을 실행하지 않았다. 원문: `main_o :` (68); `	cd main ; make all` (69); `mpi_comm_o :` (71); `	cd mpi_comm ; make all` (72); `partition_o :` (74); `	cd partition ; make all` (75); `seq_o :` (77); `	cd seq ; make all` (78); `src_o :` (80); `	cd src ; make all` (81); `util_o :` (83); `	cd util ; make all` (84). |
| 86–98 | 정리 대상. clean은 clean_blas·clean_scalapack·clean_mumps·clean_str에 의존한다. 외부 라이브러리는 각 디렉터리에서 make clean을 호출한다. clean_str은 두 깊이의 객체·module/*.mod·*.exe를 제거하는 명령이다. 삭제 명령은 판독만 했다. 원문: `clean : clean_blas clean_scalapack clean_mumps clean_str` (86); `clean_blas :` (88); `	cd $(BLAS_DIR) ; make clean` (89); `clean_scalapack :` (91); `	cd $(SCALAPACK_DIR) ; make clean` (92); `clean_mumps :` (94); `	cd $(MUMPS_DIR) ; make clean` (95); `clean_str :` (97); `	rm -f */*.o */*/*.o module/*.mod *.exe` (98). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24·27·32–39: ALL_L에는 BLAS·SCALAPACK·MUMPS 빌드 대상이 있고 METIS 빌드 대상은 없다. 25행 LIBS에는 LIBMETIS가 포함된다.
- 27–28·41–84: all은 module_o와 다른 디렉터리 대상을 같은 선행 목록에 나열한다. 이 파일에는 다른 *_o 대상이 module_o에 의존한다는 별도 규칙이 없다.
- 29–30: 링크 명령은 FCOMP와 LIBS를 사용하며 FOPT를 직접 포함하지 않는다.
