---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Out/Mod_Map_Write_NetCDF.f90
lines: 496
sha256: 4491b9f7f2860ba8e5da48a47e843bdaf039e4069acc54c64b0980a1566b806f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Mod_Map_Write_NetCDF.f90 — 판독 구간 기록

구간은 1행부터 496행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | EFDC+ 표제·저작권 안내·GPLv2 주석(1–8). NetCDF 출력용 매핑(mapping) 모듈 설명과 저자(10–14). 모듈 시작(15). GLOBAL·MPI 변수·출력 배열·Map/Gather/Sort 및 배열 연결 모듈을 사용한다(17–24). DRIFTER에서는 Gather_Drifter_Arrays만 가져온다(22). implicit none·contains·루틴 머리말·빈 줄(26–34). |
| 35–95 | Map_Write_NetCDF 입구(35). 지역 정수·배열 등록 수·target allocatable 임시 배열을 선언한다(40–58). LEC/LNC는 LCM 크기로 할당한다(60–61). 정수 ActLay와 real(rkd) TSED/BULKDENS/PERSED 임시 배열은 지역(local) LCM과 전역(global) LCM_Global, KB, NSCM 크기를 사용한다(64–72). 파고·주기·방향·소산(dissipation) 임시 배열은 LCM 크기이다(73–76). 모든 임시 배열을 0으로 초기화한다(78–92). j=0(94). |
| 96–142 | 시작 시 35행 Map_Write_NetCDF 안. Assign_Loc_Glob_For_Write에 CUE·CUN·CVN·CVE·DZC·BELV·HP·U·V·W의 크기·지역·전역 배열을 전달한다(97–125). 각 등록 전 `j = j + 1` (96)와 같은 증분을 사용한다(99·102·105·108·111·114·118·121·124). 1..LA 루프에서 `LEC_temp_gl(m) = Map2Global(LEC(m)).LG` (130), `LNC_temp_gl(m) = Map2Global(LNC(m)).LG` (138)로 LEC/LNC 인덱스를 전역 번호로 옮긴다(129–139). 두 임시 배열을 전역 배열에 등록한다(133·141). 등록 전 증분은 `j = j + 1` (127), `j = j + 1` (135)이다. |
| 143–184 | 시작 시 35행 Map_Write_NetCDF 안. 전단응력(shear stress) 출력은 `if( IS_NC_OUT(2) == 1 )then` (145) 안에서 `if( ISTRAN(6) > 0 .or. ISTRAN(7) > 0 )then` (147)로 퇴적물 경로를 선택한다. 그 안 `if( LSEDZLJ )then` (148)이면 TAU 등록(150–151), `elseif( ISBEDSTR >= 1 )then` (153)이면 TAUBSED 등록(155–156), 추가 `if( ISBEDSTR == 1 )then` (158)이면 TAUBSND 등록(159–160). 내부 else(162)는 TAUB 등록(163–164). 퇴적물 조건의 else(166)는 QQ 등록(167–168). 풍속·기압 출력은 `if( NCDFOUT > 0 .or. HFREOUT > 0 .or. IS_NC_OUT(4) == 1 )then` (174)이면 WNDVELE·WNDVELN·PATMT 등록(175–182). 각 증분은 `j = j + 1` (150)와 같은 식이다(155·159·163·167·175·178·181). |
| 185–232 | 시작 시 35행 Map_Write_NetCDF 안. `if( IS_NC_OUT(3) == 1 )then` (187) 안 `if( ISWAVE >= 3 )then` (188)이면 1..LA 루프에서 WV의 HEIGHT/PERIOD/DIR을 임시 배열로 복사하고 등록한다(189–206). 같은 출력 조건 안 `if( ISWAVE == 4 )then` (210)이면 WV(l).DISSIPA(KC)를 복사해 등록하고 WVHUU·WVHVV·WVHUV를 등록한다(211–228). 증분은 `j = j + 1` (189)와 같은 식이다(196·202·211·218·222·226). 두 파랑 조건과 출력 조건 종료·빈 줄(230–232). |
| 233–290 | 시작 시 35행 Map_Write_NetCDF 안. 각각 `if( IS_NC_OUT(16) == 1 )then` (235), `if( IS_NC_OUT(13) == 1 )then` (243), `if( IS_NC_OUT(14) == 1 )then` (249), `if( IS_NC_OUT(17) == 1 )then` (256), `if( IS_NC_OUT(49) == 1 )then` (264), `if( IS_NC_OUT(24) == 1 )then` (271), `if( IS_NC_OUT(18) == 1 )then` (278), `if( IS_NC_OUT(19) == 1 )then` (285)이면 SAL·TEM·TEMB·DYE·SFL·TOX·SED·SND를 해당 전역 배열에 등록한다(237–288). 증분은 `j = j + 1` (236)와 같은 식이다(244·250·257·265·272·279·286). NC_WRITE_CONS/CONM 이름·출력 번호는 주석에 있다(234·242·255·263·270·277·284). |
| 291–313 | 시작 시 35행 Map_Write_NetCDF 안. wq=0 초기화(292). 26..46 루프(293)에서 `if(IS_NC_OUT(m) > 0) wq = 1` (294)를 실행한다. `if( wq == 1 )then` (296)이면 `j = j + 1` (297) 뒤 WQV 전체 3차원을 등록한다(298–299). `if( IS_NC_OUT(12) == 1 )then` (303)이면 Gather_Drifter_Arrays를 호출한다(309). 기름 유출(oil spill) 관련 todo와 조건부 NC_WRITE_FIELD 호출은 주석이다(305–306). 퇴적층 출력 주석(313). |
| 314–365 | 시작 시 35행 Map_Write_NetCDF 안. `if( LSEDZLJ )then` (314) 안에서 2..LA·1..KB 루프로 `Reverse_Temp_2D_ActLay(L,K) = LAYERACTIVE(K,L)` (319)를 실행하고 ActLay 임시 배열을 등록한다(317–325). TAU도 등록한다(327–328). 다음 같은 범위 루프에서 `Reverse_Temp_2D_TSED(L,K) = TSED(K,L)` (334), `Reverse_Temp_2D_BULKDENS(L,K) = BULKDENS(K,L)` (346)로 TSED/BULKDENS 축 순서를 바꾸고 등록한다(330–352). 2..LA·1..KB·1..NSCM 루프에서 `Reverse_Temp_3D(L,K,nn) = PERSED(nn,K,L)` (358)로 PERSED를 옮겨 등록한다(355–365). 증분은 `j = j + 1` (323)와 같은 식이다(327·330·338·350·363). 330행과 338행 사이에는 배열 등록 호출이 없다. |
| 366–409 | 시작 시 35행 Map_Write_NetCDF·314행 LSEDZLJ 참 분기 안. D50AVG·ERO_SED_FLX·DEP_SED_FLX 등록(367–376). `if( ICALC_BL > 0 )then` (378)이면 CBL·QSBDLDX·QSBDLDY 등록(380–388). `if( IS_NC_OUT(25) == 1 .and. ISTRAN(5) > 0 )then        ! *** Bed Toxics` (391)이면 KBT·HBED·TOXB 등록(393–401), 그 안 `if( ICALC_BL > 0 )then` (403)이면 CBLTOX 등록(404–406). 증분은 `j = j + 1` (367)와 같은 식이다(370·374·380·383·386·393·396·399·404). |
| 410–451 | 시작 시 35행 Map_Write_NetCDF·314행 if 블록 안에서 병렬 elseif로 전환한다. `elseif( ISBEXP >= 1 .and. KB > 1 .and. ( ISTRAN(6) >= 1 .or. ISTRAN(7) >= 1 ) )then` (410)이면 KBT·HBED·BDENBED·PORBED 등록(412–425). 그 안 `if( ISTRAN(6) >= 1 .or. ISTRAN(7) >= 1 )then` (427)이면 SEDB·SNDB를 모두 등록한다(429–435). `if( IS_NC_OUT(25) == 1 .and. ISTRAN(5) >= 1 )then       ! *** Bed Toxics` (439)이면 TOXB 등록(440–442). 증분은 `j = j + 1` (412)와 같은 식이다(415·419·423·429·433·440). 바깥 if 종료(444). j를 등록 수로 정하고 Handle_Calls_MapGatherSort 호출(447·450). |
| 452–483 | 시작 시 35행 Map_Write_NetCDF 안. `if( LSEDZLJ )then` (453)이면 2..LA_Global·1..KB 루프에서 `LAYERACTIVE_Global(K,LG) = Gl_Reverse_Temp_2D_ActLay(LG,K)` (457), `TSED_Global(K,LG) = Gl_Reverse_Temp_2D_TSED(LG,K)` (464), `BULKDENS_Global(K,LG) = Gl_Reverse_Temp_2D_BULKDENS(LG,K)` (471)로 LAYERACTIVE/TSED/BULKDENS의 전역 축 순서를 되돌린다(455–473). 2..LA_Global·1..NSCM·1..KB 루프에서 `PERSED_Global(nn,k,LG) = Gl_Reverse_Temp_3D(LG,K,nn)` (479)로 PERSED를 되돌린다(476–482). 조건 종료(483). |
| 484–496 | 시작 시 35행 Map_Write_NetCDF 안. 지역·전역 축 교환 임시 배열 8개를 명시적으로 해제한다(485–492). 루틴 종료·빈 줄·모듈 종료(494–496). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 40–41: 루틴 안 num_arrays_to_write_out은 지역 변수이다. 이 파일의 모듈은 Mod_Map_Write_EE_Binary를 use한다(23). 이 판독은 이름 접근 규칙이나 컴파일 결과를 판단하지 않는다.
- 160: TAUBSND_Global 등록 호출의 전역 크기 인수도 size(TAUBSND,1)이다. 같은 호출의 지역 크기 인수와 같다.
- 305–306: “Oil spill not functional with MPI” todo가 있다. 바로 아래 기름 유출 조건부 출력 호출은 주석 처리되어 있다.
- 327–340: TAU 등록 후 j가 330행과 338행에서 각각 1 증가한다. 두 증분 사이 실행문은 TSED 임시 배열 복사 루프이며 Assign_Loc_Glob_For_Write 호출은 없다.
- 410·427–435: 410행 분기는 ISTRAN(6) 또는 ISTRAN(7)이 1 이상인 조건을 포함한다. 그 안 427행은 같은 or 조건을 다시 검사하고 SEDB·SNDB를 모두 등록한다.
- 60–76·485–492: 임시 배열 14개를 할당한다. 명시적 deallocate는 축 교환 배열 8개에만 있다. LEC/LNC 및 파랑 임시 배열 4개는 이 목록에 없다. 자동 해제 여부는 판단하지 않는다.
- 391·439: LSEDZLJ 분기의 퇴적층 독성물질(bed toxics) 조건은 ISTRAN(5)>0이다. 병렬 분기의 조건은 ISTRAN(5)>=1이다.
