---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/makefile
lines: 38
sha256: 0fce220fc2921947a9038256b6e2cd1b85f8e1a183df46797712790f3fd92ba8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# makefile — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | 모듈 검색 경로와 컴파일 옵션. MODDIR은 ../module이다. FFLAGS는 객체 생성 -c, 외부 FOPT, 모듈 검색 -I $(MODDIR)를 결합한다. 2·4행 공백 줄을 포함한다. 원문: `MODDIR = ../module ` (1); `FFLAGS = -c $(FOPT) -I $(MODDIR) ` (3). |
| 5–31 | 접촉(contact) 관련 객체 목록. areacd.o부터 vrtxstk.o·wrksize.o까지의 각 파일명을 보존한다. 원문: `OBJS = areacd.o      areain.o      bctset.o      circhk.o      \` (5); `       cntrfc.o      contact.o     contactp.o    cont_init.o   \` (6); `       cont_init_p.o cont_tbl.o    cont_tbl_p.o  corredge.o    \` (7); `       corrface1.o   corrface2.o   corrface3.o   crh2edge.o    \` (8); `       crh2face.o    crh2set.o     crh2stke.o    crh2stkf.o    \` (9); `       crh2vrtx.o    csfhx.o       csfpn.o       csfte.o       \` (10); `       edgechk.o     edgedl.o      edgeout.o     edgeslip.o    \` (11); `       edgestk.o     edgquad.o     elcquad.o     enpfrcd.o     \` (12); `       estfedge.o    estfface.o    facechk.o     faceon.o      \` (13); `       faceout.o     facerl.o      facesepa.o    facestk.o     \` (14); `       fricchk.o     fricedge.o    fricface.o    fricint.o     \` (15); `       fricset.o     fricstf.o     grazeel.o     gsfhx.o       \` (16); `       gsfpn.o       gsurf.o       gsurfq.o      gsurfx.o      \` (17); `       initidx.o     istchk.o      lencd.o       lhsidx.o      \` (18); `       mktehx.o      mktepn.o      mpccorr.o     mpccorr11.o   \` (19); `       mpccorr12.o   mpccorr13.o   mpccorr2.o    mpccorr3.o    \` (20); `       mpcedge.o     mpcface.o     mpcpreb.o     mpcrank.o     \` (21); `       mpcset.o      mpcset2.o     mpcsize.o     mpcslv.o      \` (22); `       mpcstke.o     mpcstkf.o     mpcvrtx.o     mstnod.o      \` (23); `       npfedge.o     npfface.o     npforced.o    npfric.o      \` (24); `       npfricd.o     nrmvec.o      penchk.o      penst.o       \` (25); `       resfric.o     rfcedge.o     rfcface.o     rhsidxb.o     \` (26); `       rhsidxf.o     rhsidxr.o     rlcorr.o      rmpccal.o     \` (27); `       slvnrm.o      spcdedge.o    spcdface1.o   spcdface2.o   \` (28); `       spcdface3.o   stickchk.o    tredge.o      trface.o      \` (29); `       volcd.o       volin.o       volin3.o      vrtxchk.o     \` (30); `       vrtxsepa.o    vrtxslip.o    vrtxstk.o     wrksize.o    ` (31). |
| 32–38 | all 대상은 OBJS에 의존한다. .SUFFIXES는 .f와 .o를 등록한다. .f.o 접미사 규칙(suffix rule)은 $(FCOMP) $(FFLAGS) $<로 선행 Fortran 파일을 컴파일한다. 빈 줄도 구간에 포함한다. 이 파일에는 FCOMP·FOPT의 자체 정의가 없다. 명령은 실행하지 않았다. 원문: `all : $(OBJS) ` (33); `.SUFFIXES: .f .o ` (35); `.f.o : ` (37); `	$(FCOMP) $(FFLAGS) $< ` (38). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
