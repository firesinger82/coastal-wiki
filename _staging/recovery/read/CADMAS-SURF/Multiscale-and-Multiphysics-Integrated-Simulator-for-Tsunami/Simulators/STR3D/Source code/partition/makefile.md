---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/partition/makefile
lines: 20
sha256: bf8929ce2b397e3d8663cf9149a63b59ba2c9e8f2987ce0840e14d2b638ed217
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# makefile — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | 모듈·Fortran·C 옵션. MODDIR=../module, FFLAGS=-c $(FOPT) -I $(MODDIR), CFLAGS=-c이다. 빈 줄을 포함한다. 원문: `MODDIR = ../module ` (1); `FFLAGS = -c $(FOPT) -I $(MODDIR) ` (3); `CFLAGS = -c ` (4). |
| 6–11 | 분할(partition) 객체 목록. bcast_tbl.o부터 part*·송수신 객체와 metis_partition.o까지 원문 파일명을 나열한다. 원문: `OBJS = bcast_tbl.o       cont_tbl_g.o      dealloc.o         ens_geom_p.o      \` (6); `       ex_add.o          ex_pload4.o       ex_spc.o          ex_spc1.o         \` (7); `       part.o            partition.o       part_c.o          part_geom.o       \` (8); `       part_send_tblx.o  part_send_tblx1.o part_send_tblx2.o recv_tbl.o        \` (9); `       recv_tblx.o       send_tbl.o        metis_partition.o` (10). |
| 12–20 | all은 OBJS에 의존한다. .SUFFIXES는 .f·.c·.o이다. .f.o는 FCOMP·FFLAGS, .c.o는 CCOMP·CFLAGS로 선행 파일을 컴파일한다. 명령은 판독만 했다. 원문: `all : $(OBJS) ` (12); `.SUFFIXES: .f .c .o ` (14); `.f.o : ` (16); `	$(FCOMP) $(FFLAGS) $< ` (17); `.c.o : ` (19); `	$(CCOMP) $(CFLAGS) $< ` (20). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 3–4·17·20: Fortran은 FOPT를 FFLAGS로 전달하지만 CFLAGS는 -c만이며 C 명령은 COPT를 참조하지 않는다.
