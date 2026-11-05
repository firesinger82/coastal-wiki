# CADMAS-SURF 판독 기록 sonnet 표본 (11-04)

## 요약

- 표본은 28행이다. 코드 행 20개([1]–[20])와 PDF 쪽 행 8개([21]–[28])를 대조했다.
- 맞음 27행, 부분 1행, 틀림 0행이다.
- 코드 행 20개의 백틱 인용 전체를 스크립트로 원문 줄과 비교했다. 글자 불일치는 0건이다. 인용 뒤 행 번호 불일치도 0건이다.
- 인용되지 않은 비공백 원문 줄은 주석 `c`/`C` 한 글자 줄과 [18]의 786–787·795–796 연속행뿐이다. [18]은 이 연속행을 "하나의 고정형식 연속문"으로 묶어 인용했으므로 누락이 아니다.
- 부분 1행은 [6]이다. 조건 `MYRANK == 1`이 빠졌다.
- 쪽 밖 문맥 표기 3건([22], [24], [27])은 판정을 낮추지 않았다. 해당 쪽 이미지에는 제목 `SF_ELEM_RANGE`, `5.4. Time series file`, `１．［２］（２）`가 보이지 않는다. 앞 쪽 문맥으로 보이며, 확인하지 못했다.
- 확인하지 않은 것: 기록에 쓰인 일본어 주석 번역 중 구간 밖 용어(예: [12]의 TR·PPS 의미)는 대조하지 않았다.

## 행별 판정

| 번호 | 기록:줄 | 원문 구간 또는 쪽 | 판정 | 근거(원문 인용) |
|---|---|---|---|---|
| 1 | vf_vpsol.f.md:16 (3D2F) | 52–90 | 맞음 | 인용 34개가 원문과 일치한다. `IF (ISW.EQ.0) THEN` 55–63의 PT 초기화, `CALL VF_M1BCGS(DBUF,` 70–75, ICGITR 세 조건 76–81이 모두 있다. `ICGITR.GT.ICGMAX`는 "NOT CONVERGED.", `-2`는 "INSTABILITY.", `-1`은 "CAN NOT DECOMPOSITION."이며 기록의 한국어 요약과 같다. |
| 2 | Makefile.md:20 (3D) | 141–169 | 맞음 | 인용 29개가 일치한다. 141–169의 `vf_cforce.o` … `vf_cwmtb22.o` 목록이 빠짐없이 있고, 이어짐 `\` 줄(150–151, 160–161, 164–165)도 따로 인용했다. |
| 3 | cont_tbl.f.md:17 (STR3D) | 113–144 | 맞음 | 인용 26개가 일치한다. `IF( IBEL(I) == 0 ) CYCLE`(115), `CASE( 4 )`의 `IBTE(:,IP) = NP(1:4)`, `CASE( 6 )`의 `DO M = 3, 5`(3개)와 `MKTEPN`, `CASE( 8 )`의 `DO M = 1, 6`(6개)와 `MKTEHX`, `KK(94) = NIGSF`가 기록과 같다. 루틴 이름 CONT_TBL은 1행 `SUBROUTINE CONT_TBL(KK,ITO)`와 같다. |
| 4 | VF_AFILEI.h.md:18 (3D2F) | 119–158 | 맞음 | 인용 40개가 일치한다. ITRPRM (1,*) 코드 0–5·11, (2,*) 코드 <0·0–8·11–19, (3,*) 코드 -1~-4가 모두 있다. 한국어 번역(예: `=-1:x座標最小位置の造波境界の解` = x 최소 좌표 위치 조파 경계의 해)이 맞다. 실행 분기 없음 서술도 맞다. |
| 5 | etamtx.f.md:16 (STR3D) | 29–42 | 맞음 | 인용 12개가 일치한다. `CALL MATML(FTF(1,I,J),1,F(1,1,I),3,F(1,1,J),2,N3,N3,3)`와 `E(:,4) = FTF(:,1,2) + FTF(:,2,1)` 등 여섯 열이 기록과 같다. |
| 6 | recv_surf.f.md:15 (STR3D) | 1–28 | 부분 | 인용 20개는 일치한다. 서술 "비영 랭크는 명령 11 전송"이 틀렸다. 원문은 `IF( MYRANK == 1 ) CALL M_MPI_SEND_I(11,1,0)  ! SEND IOP=11 TO GLB_COMM`(18)이며, 전송은 랭크 1만 한다. 랭크 2 이상은 보내지 않고 19–21의 BCAST·RECV만 한다. "랭크 0의 NPFC 수신"은 `CALL M_MPI_RECV_I(NPFC,1,0)`(21)이며, 뜻은 랭크 0에서 받는다는 것이다. 문장이 모호하다. |
| 7 | vf_iiequa.f.md:15 (3D) | 1–28 | 맞음 | 인용 19개가 일치한다. 구간 안 분기는 27행 `IF (NWD.LT.2) CALL VF_A2ERR('VF_IIEQUA','SYNTAX ERROR.')` 하나이며 기록과 같다. 29행 이후는 구간 밖이다. |
| 8 | sf_bc_reset.f.md:18 (3D2F) | 96–110 | 맞음 | 인용 11개가 일치한다. 바깥 블록 표기가 맞다: 48–51 `DO ID`/`DO K`/`DO J`/`DO I` 네 루프, 67행 `IF( NB0 > 0 ) THEN`의 `ELSE`(96). NF>=0이면 `1 + 2*(ID-1)`, 아니면 `2 + 2*(ID-1)`(100–104)이 맞다. 65행 `IF( NB <= 0 ) CYCLE`은 바깥 조건으로 표기되지 않았으나 구간 밖 설명이다. |
| 9 | sf_gpres.f.md:15 (3D2F) | 1–30 | 맞음 | 인용 17개가 일치한다. `DATA G0 / 9.8D3 /`(14), `IF( IJK <= 0 ) CYCLE`(24)은 "IPGRID 첫 지표가 양수인 절점만"과 일치한다. "셀 중심 높이"는 `Z0 = ZZ(1,K) + .5D0 * ZZ(2,K)`에 대한 해석이며 ZZ(2,K)가 셀 폭이라는 근거는 이 구간에 없다. 확인하지 못했다. |
| 10 | sf_str0.f.md:15 (3D2F) | 1–9 | 맞음 | 인용 5개가 일치한다. 10행 이후(`IF(ICPL.EQ.2) CALL SF_SEND_RST()` 등)는 구간 밖이다. |
| 11 | vf_wsfmb2.f.md:27 (3D2F) | 575–627 | 맞음 | 인용 47개가 일치한다. 미인용 줄은 빈 주석 `c` 6줄뿐이다. `fac=0.5`(i가 1 또는 imax1) 조건과 `do 22 k=1,nn1` 안의 `ekl`·`ek`·`se1` 누적식이 기록과 같다. 바깥 표기(514행 `subroutine vf_dife`, 552행 `do 100 i=1,imax1`)가 맞다. |
| 12 | vf_vpcoef.f.md:24 (3D2F) | 435–512 | 맞음 | 인용 72개가 일치한다. 436–511이 모두 `C2F` 주석 처리된 코드라는 서술이 맞다. 바깥 표기가 맞다: 124–126 `DO 120 K`/`DO 110 J`/`DO 100 I`, 142행 `ELSEIF (N.GT.-1) THEN`(141행 `C2F ELSEIF (N.EQ.0)`은 주석). 512행 이후 `ELSE`(514)·`P.G ERROR.`는 구간 밖이다. |
| 13 | vf_fconvs.f.md:18 (3D2F) | 130–174 | 맞음 | 인용 43개가 일치한다. 바깥 표기가 맞다: 84 `DO 220 K`, 85 `DO 210 J`, 86 `DO 200 I`, 90 `IF (NF0.GT.0 .AND. FF0.GE.FLOWER .AND. FF0.LE.FUPPER) THEN`. `IF (DM+DP.LE.ZERO)`이면 `S1=0.0D0`, 아니면 `S1=(FM-FP)/(DM+DP)`(169–173)가 맞다. I+1 측 NFL 네 분기(≤-1, 8, 0, 그 외)는 모두 인용으로 담겼다. |
| 14 | vf_a1main.f.md:40 (3D) | 1148–1177 | 맞음 | 인용 29개가 일치한다. 1145행 `GOTO 500`·1146행 ` 1000 CONTINUE` 뒤이므로 "500 반복을 벗어남"이 맞다. `IE.EQ.1.AND.ETIME.LT.1.0D30`이면 `IEE=1`, `IRSTRN(1)=NNOW`·`(2)=NNOW`·`(3)=1`, `.ars` 파일의 `-999,TNOW` 쓰기와 `stop_ars` 열기(IE.EQ.1), ELSE의 `NNOW,TNOW`가 기록과 같다. IE는 1005행 `IE = IEND(1)`이며 종료 조건 판정 결과이다. |
| 15 | vf_pmgp2c.f.md:22 (3D) | 306–346 | 맞음 | 인용 41개가 일치한다. 286행 `IF (MGPRNK.GE.0) THEN` 안이며 "부모 존재 분기" 표기가 맞다. 330–334 `CALL VF_PMGP2C_CF(... IS,JJ,KK,-1,MGNV)`의 방향 -1, 342행 `NN = NN + MGNV`가 맞다. 310–329의 `C` 주석은 종전 직접 대입 코드이고 336–340의 `c` 줄은 디버그 코드이다. |
| 16 | Ct_SPC1.f.md:16 (STR3D) | 19–36 | 맞음 | 인용 14개가 일치한다. `IF( CHAR(1:8) == BLK .OR. CHAR(1:1) == '+' )`(23)에서 "선두 공백"은 첫 8자 공백을 뜻한다(5행 `CHARACTER*8 BLK`). `IF( IG(I) == 0 ) RETURN`(26)과 `BACKSPACE(ITI)`(30)가 맞다. |
| 17 | cont_tbl_g.f.md:21 (STR3D) | 301–338 | 맞음 | 인용 22개가 일치한다. `CASE( 3 )`은 `IP = IP + 1`, `CASE( 4 )`는 `EDGQUAD`·`IEDQW(KP:KP+3) = JP`·`IP = IP + 4`·`JP = JP + 1`·`KP = KP + 4`이며 기록과 같다. |
| 18 | Read_data.f.md:35 (STR3D) | 761–797 | 맞음 | 인용 23개가 일치하고 786–787, 795–796은 연속문으로 묶어 인용했다. 바깥 표기가 맞다: 596 `DO`, 600 `IF( CHAR(1:8) == 'ENDDATA ' ) THEN`부터 `ELSEIF` 체인. `MPCADD`가 `RD_SPCADD( IMPA(1,I_MPCAD), NMPA, ...)`를 호출한다는 서술이 맞다. EIGRL·FREQ1이 `READ(CHAR,...)`로 직접 읽는다는 서술이 맞다. |
| 19 | vf_bwuwn.f.md:21 (3D) | 296–332 | 맞음 | 인용 40개가 일치한다. 바깥 표기가 맞다: 1 `SUBROUTINE VF_BWUWN`, 257 `DO 500 JD=1,4`, 260 `IF (IBCTYP(1,JD).EQ.1) THEN`. `IF (N.EQ.-3 .AND. MTBTYP .EQ.3) THEN`의 빈 분기를 "속도 재설정 건너뜀"이라 서술한 것이 맞다. 근거는 VF_AFILEI.h 189–192의 `=3:水位指定`이다. SA에 180/90/270도를 더한 뒤 `SA*PI/180.0D0`로 라디안 변환하는 식이 모두 있다. |
| 20 | vf_seuler.f.md:15 (3D2F) | 1–42 | 맞음 | 인용 34개가 일치한다. 일본어 주석 번역이 맞다: `スカラ量の時間積分を計算(Euler法)` = 스칼라량의 시간 적분 계산(오일러법), `空隙率` = 공극률, `生成消滅` = 생성·소멸. 43행 이후 적분식은 구간 밖이다. |
| 21 | CADMAS-AGENT_Manual_English.pdf p019-030.md:15 | p.21 (인쇄 20) | 맞음 | 쪽 이미지(cad-agent-manual-021)와 대조했다. `6.1.3 Module variables about potential（m_potential）`, `Table 6-4`의 24개 변수 행 전부(xpin … pot_mob_revise)의 type·dimension·description이 일치한다. `m_pot_shlter` 철자와 `i_signpost`의 `Location of shelters`, 단위 `[m]` 5건이 맞다. 기본값·허용범위가 없다는 서술이 맞다. |
| 22 | CADMAS-STR_Program Instructions(CADMAS)_English.pdf p001-023.md:30 | p.16 | 맞음 | 이미지(cad-str-instr-cadmas-016)와 대조했다. 표 4행 `EPS R8 I Tolerance for range setting`, `N I4 I`, `NP(N) I4 I`, `GRID(3,*) R8 I`이 일치하고 표 아래는 여백이다. 표 제목 `SF_ELEM_RANGE`와 `3. Subroutine Description`은 이 쪽에 보이지 않는다. 앞 쪽 문맥으로 보이며 확인하지 못했다. |
| 23 | CADMAS-STR_Program Instructions_English.pdf p001-018.md:21 | p.7 (인쇄 4) | 맞음 | 이미지(cad-str-instr-007)와 대조했다. `S=S_1+S_2`, `S_1: Type 1 boundary (on S_1 δu=0)`, `S_2: Type 2 boundary (on S_2 σ^T·n=t)`, 세 단계 변형식, 벡터 표기식 ③, `ε_v=ε_x+ε_y+ε_z`, 6성분 `ε̂`·`σ̂'`, `[3] Spatial discretization`의 Yagawa–Yoshimura 1995 Chapter 5와 MacNeal 1976 RHM-43 인용, `p=[N]{P}`가 모두 일치한다. |
| 24 | CADMAS-STR_Manual_English.pdf p001-018.md:17 | p.5 | 맞음 | 이미지(cad-str-manual-005)와 대조했다. `Only elastic-plastic (bilinear) is selectable`, `塑性係数, H` 2.E+9, `初期降伏応力` 3.E+7, `0. Von Mises or 3. Drucker-Prager`, `0.等方硬化`, `Friction Angle` 고정 `0.07`, 보 요소는 `0. Von Mises`만, ⑤의 `tensile strength cannot be specified for subgrade materials`가 일치한다. 위 화면에 회색으로 표시된 `摩擦角(A) 0.07`·아래 화면의 `圧縮`·`せん断` 입력란은 서술되지 않았으나 쪽의 문단·표가 아닌 화면 내용이다. `１．［２］（２）` 표기는 이 쪽에 보이지 않는다. |
| 25 | CADMAS-2F_Manural_English.pdf p127-144.md:25 | p.137 (인쇄 599) | 맞음 | 이미지(cad-2f-manual-137)와 대조했다. 구문 5줄(`[KC]` 오기 포함), ISTR~KC2 변수표의 단위·형·기본값·제한(`TSTEP>0. 0`, `1=<IC1=<IC2<NI-1` 등)이 일치한다. Note 5줄(`not output by default`, `at least 2 × 2 cells`, `[* c1 = <0]`→`[* c1 = 1]`, `[* c2 <= 0]`→`[* c2 = N-1]`, 와도 `[+1]`~`[+3]`)이 맞다. 쪽 맨 아래 `■Detailed file output control data`는 기록의 "제목"과 같다. |
| 26 | CADMAS-AGENT_Manual_English.pdf p001-018.md:20 | p.6 (인쇄 5) | 맞음 | 이미지(cad-agent-manual-006)와 대조했다. Table 3-1의 입력 5행(`agent.inp` 설명 `Agete data`, `move_boundary.inp`의 `JInput` 오기 포함)과 단위 번호 11/12/22/21/20, 파일명 없는 3행(`required when flag_WP=0`, `flag_danger=1`, `whenflag_prob=1`), `data.ma` 13, 출력 4행(14/15/16/100)이 모두 일치한다. 세 행의 Unit number가 빈칸이라는 서술이 맞다. |
| 27 | CADMAS-2F_Manural_English.pdf p145-160.md:22 | p.152 (인쇄 614) | 맞음 | 이미지(cad-2f-manual-152)와 대조했다. 데이터 행 `4.01016249E+01 -9.65151936E-02 -1.60249489E-01 -1.45746660E-01`, `～～ Omitted ～`, 빈 오른쪽 칸, 나머지 공백이 일치한다. 제목 `5.4. Time series file`은 이 쪽에 보이지 않는다. 앞 쪽 문맥으로 보이며 확인하지 못했다. |
| 28 | AGENT_Tutorial_English.pdf p001-021.md:18 | p.6 | 맞음 | 이미지(cad-agent-tutorial-006)와 대조했다. 제목 `Agent.inp（evacuee data）`, 열 10개와 단위(`[m]`, `[m/s]`, `[deg]`, `[s]`), `0.0～1.0`·`0.0以上` 범위, `First line has to start from “#”`, 헤더 줄 `# N, X0, Y0, V, deadline, rw_sigma, W_signpost, W_shelter, W_mod, starttime`, 9행의 좌표(1: 0.5,1.5 … 9: 9.5,5.5)와 공통값(1.00, 0.3, 0.00, 1.00, 1.00, 0.00, 0.0), 노란 별 2개, 하단 문장 `...there is a program for creating`이 일치한다. 격자 그림의 회색 칸(장애물로 보임)은 서술되지 않았다. |
