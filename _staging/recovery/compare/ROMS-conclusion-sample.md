# ROMS 결론 표본 검증 (sonnet, 10-14) — 30행: OK 23, 부분 4, 틀림 3

표본: 결론 절 9,248행에서 무작위 30행(H 아닌 행 24, H 6행). seed `roms-conc-10-14`. 검증자 sonnet 3명이 원문 줄·git 이력을 직접 열어 판정했다.

| 보고서 | 행 ID | 원 결론 | 판정 | 근거 | 고칠 내용 |
|---|---|---|---|---|---|
| build-options-history | RBH-0821 | D | 틀림 | 현재 코드에 ESMF_COUPLING 0건. `git log -S ESMF_COUPLING`이 4b22f48b(2017-07-31, ticket:738)를 찾는다. ROMS-git-verify-D1 확정 결론은 A다. | A로 바꾸고 git 판정 문장을 반영한다. |
| coupling-nesting-parallel | RCN-050 | C | 부분 | mct_roms_wrf.h:443 `scale=-1.0_r8/(rho0*Cp)`, coupling_mct.dat:99–100 오프셋 0.0·배율 1.0. coupling.in:102는 변수 목록뿐이다. 같은 배율이 .h 490·507행에도 있다. | dat 배율과 수신 코드 배율이 다르다는 사실을 적고, dat 배율이 쓰이는지 코드로 확인해 결론을 정한다. |
| build-options-history | RBH-1535 | C | 틀림(결론 문장) | TKE_DIF4·tkenu4는 checkdefs.F:2373, wrt_info.F:490–492, def_info.F, read_phypar.F, inp_par.F:652, mod_scalars.F에만 있다. Nonlinear 혼합 계산에서 확산 연산자를 적용하는 줄이 없다. TKE_DIF2도 같다. | 결론 문장을 "입력·점검 출력·기록은 있으나 확산 연산자 적용 줄은 없다"로 바꾸고 E 검토 대상으로 판정한다. |
| inputs | RI1-1003 | C | OK | inp_par.F:710–726, Variables.wiki:2686–2689 | — |
| tools-guides | RTG-098 | C | OK | FAQ.wiki:120·124, diag.F:243–249 | SOLVE3D 조건 명시 권장 |
| build-options-history | RBH-1701 | A | OK | e8719fb7(2011-09-23, ticket:519) | — |
| build-options-history | RBH-1156 | A | OK | roms-3.5 u2dbc_im.F:640, e8719fb7 | — |
| outputs-metadata | OMD-K022 | C | OK | memory.F:363·396·473–479 | — |
| coupling-nesting-parallel | RCN-1553 | H | OK | Model_Coupling_SANDY.wiki:11 | — |
| testcases | RT1-1236 | H | OK | INLET_TEST_CASE.wiki:89 그림 캡션 | — |
| testcases | RT1-1388 | C | OK | ana_smflux.h:153–160, bl_test.h:51–62, set_data.F:569–570 | 노트 문장을 "ANA_SMFLUX를 정의하지 않는다(bl_test.h:51,60–62)"로 |
| build-options-history | RBH-1181 | A | OK | e8719fb7 | — |
| biology | PW-041 | B | OK | npzd_Powell_inp.h:275·303 | — |
| mixing-bc-forcing | RMF1-246 | F | OK | lmd_skpp.F:869–897 전개가 위키 a2·a3와 같다. | — |
| testcases | RT1-1439 | C | OK | ana_tair.h:86–89, benchmark.h:43 | — |
| testcases | RT1-748 | A | OK | ee8968bb(2018-06-21) | — |
| build-options-history | RBH-3077 | C | OK | ice_evp.F:278–280, checkdefs.F:1437, cppdefs.h:666 | 근거에 cppdefs.h:666 추가 |
| outputs-metadata | OMD-D066 | B | OK | step2d_LF_AM3.h:662–669·807·815·817 | — |
| tools-guides | RTG-1116 | H | 부분 | nc_slice는 저장소 roms_matlab/netcdf/nc_slice.m에 있고 7번째 인자 method가 있다. | roms_matlab은 판독 대상 밖이다. H를 유지하되 이유를 "판독 대상 밖 Matlab 도구(roms_matlab)"로 바꾼다. |
| outputs-metadata | OMD-SO072 | H | 부분 | 인용 read_phypar.F:8194는 blk_ZQ와 무관하다. 실제는 5527–5528 `WRITE (out,200)`과 8204 형식 `(1p,e11.4,2x,a,t32,a)`이다. | 근거를 5527·8204로 바꾸고 출력 형식 일치로 판정한다. 예제 값을 기본값으로 해석하지 않는다는 문장은 유지한다. |
| testcases | RT1-1107 | F | OK | ana_grid.h:380–381·516·1055, ana_initial.h:425 | — |
| build-options-history | RBH-3100 | C | OK | vegetation_var.h:45·52, mod_ncparam.F:2636 | 노트 문장에 VEGETATION·MARSH_DYNAMICS 선행 조건 추가 |
| sediment-ice-vegetation | RSM1-030 | B | 부분 | B는 맞다. 직접 근거는 Equations_of_Motion.wiki:136–137과 pre_step3d.F:1037 `FC(i,0)=dt*bustr`이다. | 근거 추가, 문장을 "K_M/Hz ∂u/∂s 형태"로 |
| build-options-history | RBH-1588 | A | 틀림 | ROMS-git-verify 확정 결론 B. Options.wiki 제목은 "OBSOLETE as of revision 701". 충돌 목록과 맞는 판이 없다(roms-3.6 riverplume1.h:17–18). | B로 바꾼다. |
| testcases | RT1-1298 | C | OK | riverplume2.h:16–48 | 노트 문장에서 "undef" 삭제 |
| build-options-history | RBH-0805 | A | OK | e8719fb7, roms-3.5 obc_volcons.F:143 | — |
| inputs | RI1-0964 | C | OK | read_stapar.F:155·228–230 | — |
| outputs-metadata | OMD-SN419 | A | OK | a4a82c5f(2023-07-01, trac:942) | 근거의 git log 목록을 a4a82c5f 한 줄로 |
| testcases | RT1-077 | H | OK | Amarel.wiki:74 | — |
| coupling-nesting-parallel | RCN-1162 | H | OK | Lake_Jersey ABDC.wiki:29 | — |

결정: 표본 오류(부분 4, 틀림 3)를 보고 결론 절 전 행을 `gpt-6-astra`로 전수 검증한다. 틀림 2건(RBH-0821, RBH-1588)은 git 이력 판정을 보고서에 아직 반영하지 않아 생긴 것이다.
