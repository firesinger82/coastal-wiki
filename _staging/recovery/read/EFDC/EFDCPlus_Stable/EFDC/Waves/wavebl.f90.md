---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Waves/wavebl.f90
lines: 235
sha256: ad8d8db5232e81c4efc9160d1c0946462c9533bf10f804770ddf99e4639065d0
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# wavebl.f90 — 판독 구간 기록

구간은 1행부터 235행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–43 | EFDC+·GPLv2 머리말(1–8). WAVEBL은 파랑 경계층(wave boundary layer) 정보만 지정한다는 주석이다(9–10). 주석 옵션은 NTSWV 파랑 힘 도입 시간 스텝 수, WVLCAL=1 파장 계산·0 입력 파장, ISDZBR 진단 출력, IFWAVE=0 wave.inp·1 SWAN, SWANGRP=1 전체 격자·0 위치 파일이다(11–16). 변경 기록·빈 줄(17–26), GLOBAL·GETSWANMOD·WAVELENGTH·MPI 변수 사용과 선언(27–41), 빈 줄(42–43). 외부 CSEDVIS를 선언한다(41). |
| 44–77 | 시작 시 9행 WAVEBL 안. `if( JSWAVE == 0 )then` (44)은 최초 초기화 경로이다. L=1:LC에서 HMPW/HMUW/HMVW·WVKHC/HU/HV·WVTMP1–4·WVENEP·UWVSQ를 0으로 초기화한다(46–58). 원문 기본값은 `QQWC(L) = 1.E-12` (59), `QQWCR(L) = 1.E-12` (60), `QQWV1(L) = 1.E-12` (61; 경계층 응력 주석), `QQWV2(L) = 1.E-12` (62; 수주 응력 주석), `QQWV3(L) = 1.E-12` (63). K=1:KC·L=1:LC에서 WVHUU/HVV/HUV·WVPP/PU/PV·FXWAVE/FYWAVE를 0으로 초기화한다(65–76). |
| 78–97 | 시작 시 9행 WAVEBL·44행 JSWAVE==0 조건 안. `if( ISSTEAD == 0 )then` (78)은 `if( process_id == master_id ) write(*,'(A)')'WAVE: READING WAVETIME.INP'` (80), `call GETWAVEDAY` (81). `if( WAVEDAY(1) > TIMEDAY .or. WAVEDAY(NWVTIM) < TIMEDAY) STOP 'TIMEDAY IS OUT OF THE WAVE-TIME RANGE!'` (82). NW=1:NWVTIM-1 루프의 `if( WAVEDAY(NW+1) > TIMEDAY .and. WAVEDAY(NW) <= TIMEDAY )then` (84)은 IWVCOUNT=NW 후 EXIT(85–86). `else` (89)는 `IWVCOUNT = 1` (91), `NWVTIM   = 1` (92), WAVEDAY(2) 할당(93), 두 원소에 TIMEDAY 복사(94). 조건 종료·입력 준비 주석·빈 줄(95–97). |
| 98–114 | 시작 시 9행 WAVEBL·44행 JSWAVE==0 조건 안. `if( IFWAVE == 0 )then` (98) 안의 `if( process_id == master_id )then` (99)은 입력 시간 로그를 쓴다(100–101). master 조건 밖에서 `call GETWAVEINP` (103). `elseif( IFWAVE == 1 )then` (105)은 `if( process_id == master_id ) write(*,'(A38,F12.4)')'WAVE: READING SWAN OUPUT AT WAVE-TIME:',REAL(WAVEDAY(IWVCOUNT))` (106). 내부 `if( SWANGRP == 1 )then` (107)은 GETSWAN_GRP 호출(108), `else` (109)는 GETSWAN_LOC 호출(110). 내부·입력 조건 종료(111–112), `JSWAVE = 1` (113). |
| 115–131 | 시작 시 9행 WAVEBL 안이며 44행 if의 갱신 분기에서 시작한다. `elseif( JSWAVE == 1 .and. IWVCOUNT < NWVTIM .and. TIMEDAY >= WAVEDAY(IWVCOUNT+1) )then` (115)은 `IWVCOUNT = IWVCOUNT + 1` (117). 내부 `if( IFWAVE == 0 )then` (118)은 `if( process_id == master_id ) write(*,'(A36,F12.4)')'WAVE: READING WAVE.INP AT WAVE-TIME:',REAL(WAVEDAY(IWVCOUNT))` (119), GETWAVEINP 호출(120). `elseif( IFWAVE == 1 )then` (122)은 `if( process_id == master_id ) write(*,'(A38,F12.4)')'WAVE: READING SWAN OUPUT AT WAVE-TIME:',REAL(WAVEDAY(IWVCOUNT))` (123). `if( SWANGRP == 1 )then` (124)은 GETSWAN_GRP(125), `else` (126)는 GETSWAN_LOC(127). 조건 종료·빈 줄(128–131). |
| 132–160 | 시작 시 9행 WAVEBL 안이며 JSWAVE 조건 밖. 준비 주석·OpenMP(Open Multi-Processing) parallel/do 지시문(132–136). ND=1:NDM에서 `LF = 2+(ND-1)*LDM` (138), `LL = min(LF+LDM-1,LA)` (139). L 루프에서 `WV(L).HEIGHT = min(0.75*HP(L),WV(L).HEISIG)` (142). `if( WV(L).HEIGHT >= WHMI .and. HP(L) > HDRYWAV )then` (143)은 WDEP1에 HP 복사(144), `WPRD  = 2.*PI/WV(L).FREQ` (145). 내부 `if( WVLCAL == 1 )then` (146)은 `call BISEC(DISRELATION,WLMIN,WLMAX,EPS,WPRD,WDEP1,0._8,0._8,RRLS)` (147), LENGTH에 RRLS 복사(148). 내부 조건 밖에서 `WV(L).K   = max( 2.*PI/WV(L).LENGTH, 0.01 )` (150), `WV(L).KHP = min(WV(L).K*HP(L),SHLIM)` (151). 조건·루프·OMP DO 종료·설명 주석·빈 줄(152–160). |
| 161–184 | 시작 시 9행 WAVEBL·135행 OpenMP parallel 영역 안. `if( process_id == master_id )then` (161) 안 OMP SINGLE(163)의 `if( ISDZBR > 0 )then` (164)은 WAVEBL_DIA.OUT을 열고 삭제 close 후 다시 연다(165–167). 조건·SINGLE 종료(168–170). 다음 OMP DO(172)·ND 루프(173)는 `LF = 2+(ND-1)*LDM` (174), `LL = min(LF+LDM-1,LA)` (175). L 루프(176)의 `if( ISTRAN(7) > 0 )then` (178)은 `ZBRE(L) = max(SEDDIA50(L,KBT(L)),1E-6)*2.5` (180). `else` (181)는 KSW를 ZBRE에 복사(182; Z0=KSW/30 주석). 조건 종료·빈 줄(183–184). |
| 185–215 | 시작 시 9행 WAVEBL·135행 OpenMP parallel·173행 ND·176행 L 루프 안. `if( WV(L).HEIGHT >= WHMI .and. HP(L) > HDRYWAV )then` (185)은 `AEXTMP   = 0.5*WV(L).HEIGHT/SINH(WV(L).KHP)` (186), `UWORBIT  = AEXTMP*WV(L).FREQ` (187), `UWVSQ(L) = UWORBIT*UWORBIT` (188). `if( UWORBIT < 1.E-6 )then` (189)은 UWVSQ·QQWV1=0 후 CYCLE(190–192). 조건 밖에서 `VISMUDD = 1.36E-6` (194), `if( ISMUD >= 1 ) VISMUDD = CSEDVIS(SED(L,KSZ(L),1))` (195), `REYWAVE = UWORBIT*AEXTMP/VISMUDD` (196), `RA= AEXTMP/ZBRE(L)` (197). `if( REYWAVE <= 5D5 )then` (200)은 `FCW  = 2*REYWAVE**(-0.5)` (202). `elseif( REYWAVE>5D5 .and. RA>1.57 )then` (204)은 `FCW = 0.09*REYWAVE**(-0.2)` (206). `elseif( REYWAVE>5D5 .and. RA <= 1.57 )then` (208)은 `FCW = EXP(5.2*RA**(-0.19)-6)` (210), `FCW = min(FCW,0.3)` (211). 분기 주석은 층류(laminar)·매끈한 난류(turbulent smooth)·거친 난류(turbulent rough)이다. 분기 밖에서 `CDTMP = 0.5*FCW` (213), `QQWV1(L) = min(CDTMP*UWORBIT*UWORBIT,QQMAX)` (214). |
| 216–235 | 시작 시 9행 WAVEBL·135행 OpenMP parallel·173행 ND·176행 L 루프 안이며 185행 if의 불성립 분기에서 시작한다. `else` (216)는 QQWV1·UWVSQ를 0으로 설정한다(217–218). 조건·루프·OMP DO·parallel 종료(219–223). `if( process_id == master_id )then` (225) 안의 `if( ISDZBR > 0 )then` (226)은 진단 머리말을 쓴다(227). L=2:LA에서 L/IL/JL·HEIGHT/FREQ/LENGTH/K/UWVSQ/QQWV1/ZBRE를 출력하고 UNIT 1을 닫는다(228–231). 조건·루틴 종료·빈 줄(232–235). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 82–88: 입력 범위 검사에서는 TIMEDAY==WAVEDAY(NWVTIM)을 허용한다. 구간 선택은 WAVEDAY(NW+1)>TIMEDAY를 사용하고 루프 상한은 NWVTIM-1이다.
- 115–130: 파랑 시간 갱신 경로는 한 호출에서 IWVCOUNT를 한 번 증가시킨다. 여러 시간 구간을 따라잡는 반복문은 이 경로에 없다.
- 142–152: K·KHP 갱신은 높이·수심 조건 안에 있고, 조건 불성립 시 K·KHP를 다시 설정하는 else는 없다.
- 227–229: 진단 머리말은 네 번째 파랑 열을 WVKHP(L)로 적는다. 대응 출력값은 WV(L).K이다.
- 11·33–40: NTSWV는 설명 주석에만 나온다. 지역 NWV/IWV/JWV/IOS·WWVH/WANGLE/WWPRDP/WVLEN/DISPTMP는 선언 이후 사용되지 않는다.
