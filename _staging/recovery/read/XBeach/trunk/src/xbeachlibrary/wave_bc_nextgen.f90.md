---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_bc_nextgen.f90
lines: 201
sha256: 0fc44ed733e47d942b9a2e8f47de8043e9e1880984544a200eaae0777301ad66
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# wave_bc_nextgen.f90 — 판독 구간 기록

구간은 1행부터 201행까지 빈틈없이 이어진다. 16–198행의 루틴 초안은 모두 주석이다. 아래 주석 내 조건·식은 실행 코드와 구분하여 기록하며, 주석 접두어 뒤의 코드 표기를 옮긴다.

| 구간 | 내용 |
|---|---|
| 1–15 | `wave_bc_nextgen` 모듈, XBeach 경계조건을 Delft3D/FlowFM으로 이식하려는 설명(2–5), `use paramsconst`(6), implicit none·save·private(7–9). public 선언은 주석(10). 실제 변수 `initialized = .false.`(12), contains(14). |
| 16–53 | 주석으로 된 `wave_bc_generate` 인수 목록(16–18), 시각별 경계점 에너지/flux 생성·필요시 초기화 및 시계열 생성 설명(19–23). t·wbctype·기준점 xref/yref 설명(28–33), 입력 및 출력 형·크기: seed(40), eebc(nbc,ntheta), uibc/vibc/zsbc(nbc), isBoundary·isRecomputed 논리형(41–51). |
| 54–70 | 실행 블록이 아닌 주석 초안의 `if (isBoundary .eqv. false) then`(55)은 eebc·uibc·vibc·zsbc를 0.d0, isRecomputed를 .false.로 설정(57–61); 주석 else(62)는 비어 있으며 endif(64). 남은 행은 주석·빈 줄. |
| 71–109 | 주석 설계 설명: surfbeat spectral 경계, 독립 프로세스 실행, 공통 기준점·평균수심·방향격자·random seed와 지역 경계점/거리/수심(71–89). 초안 startbcf=.false.(92); 주석 `if(.not. bccreated ) then`(94)이면 bccreated/startbcf=.true.(95–96), `bcendtime=huge(0.0d0)`(97), newstatbc=1(98). 그 주석 조건 안 `if ((instat==INSTAT_JONS.or.instat==INSTAT_JONS_TABLE & & .or. instat==INSTAT_SWAN.or.instat==INSTAT_VARDENS).and.xmaster) then`(101–102)은 `spectral_wave_bc(sg,par,curline)`(103); 병렬 `elseif (instat==INSTAT_REUSE.and.xmaster) then`(104)은 curline=1(105). 106·108에서 주석 조건 종료. |
| 110–140 | 주석 `if (t .ge. bcendtime) then`(110)에서 unit 71·72 close(111–112), 내부 `if ((instat==INSTAT_JONS.or.instat==INSTAT_JONS_TABLE & & .or. instat==INSTAT_SWAN.or.instat==INSTAT_VARDENS).and.xmaster) then`(113–114)은 `spectral_wave_bc`(115); `elseif (instat==INSTAT_REUSE.and.xmaster) then`(116)은 startbcf=.true., `curline = curline + 1`(118). 120에서 바깥 주석 조건 종료. 별도 주석 `if (  (instat==INSTAT_JONS).or. & (instat==INSTAT_JONS_TABLE).or. & (instat==INSTAT_SWAN) .or. & (instat==INSTAT_VARDENS) .or. & (instat==INSTAT_REUSE) ) then`(123–127) 안 `if (startbcf) then`(129)에서 wbcseries(curline)의 bcendtime·rt·dtbcfile·Trep·theta0·ebcfname·qbcfname 복사(131–137). 주석 startbcf 조건은 140에서 종료. |
| 141–167 | 실행 블록은 없음. 주석상 123–127행 instat 조건 내부이며 129행 startbcf 조건은 종료되어 있다. 초안 방향 루프 `sigt(:,:,itheta) = 2*par%px/par%Trep`(144), `sigm = sum(sigt,3)/ntheta`(146), `dispersion(par,s)`(147). wordsize 조회(151), `reclen=wordsize*(sg%ny+1)*(sg%ntheta)`(152)로 에너지 파일 unit 71 열기(153), `reclen=wordsize*((sg%ny+1)*4)`(154)로 flux 파일 unit 72 열기(155). 주석 `if (.not. allocated(q1) ) then`(156)은 q1/q2/q(ny+1,4)와 ee1/ee2(ny+1,ntheta) 할당(157–158). 이 조건 밖 두 시점 ee1/ee2·q1/q2 direct read(160–163). `old=floor((par%t/dtbcfile)+1)`(164), recpos=1(165); 주석 end if(166). |
| 168–188 | 주석 초안 `new=floor((par%t/dtbcfile)+1)`(168). `if (new/=old) then`(171)에서 `recpos=recpos+(new-old)`(172); 내부 `if (new-old>1) then`(174)은 recpos+1과 recpos 두 record를 모두 읽음(175–178), else(179)는 ee2/q2를 ee1/q1로 옮긴 뒤 다음 record만 읽음(180–183). 내부 endif(184) 뒤 old=new(185), end if(186), 추가 endif(187). |
| 189–201 | 주석 식 `tnew = dble(new)*dtbcfile`(189), `facinterp=(tnew-par%t)/dtbcfile`(190), `eebc = (1.d0-facinterp)*ee2 + facinterp*ee1`(191), `qbc  = (1.d0-facinterp)*q2  + facinterp*q1`(192), `uibc = qbc/hbc*min(par%t/par%taper,1.0d0)`(193), `vibc = qbc/hbc*min(par%t/par%taper,1.0d0)`(194), `eebc = eebc*min(par%t/par%taper,1.0d0)`(195). 주석 루틴 종료(198), 실제 모듈 종료(200), 빈 줄(201). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10·16–198: public 선언과 경계조건 생성 루틴 전체가 주석이다. 실제 모듈에는 실행 루틴이 없다.
- 12: initialized는 .false. 선언 뒤 이 파일의 실행 코드에서 읽거나 갱신하지 않는다.
- 55: 주석 조건의 논리 상수 표기는 `.false.`가 아니라 `false`이다.
- 129–140·151–166·187: 초안의 startbcf 조건은 140행에서 닫히고, 파일 open/read는 그 뒤에 적혀 있다. 166행과 187행에도 종료문이 있어 주석 초안의 블록 종료 배치는 후속 검토 대상이다.
- 193–194: 주석의 uibc와 vibc 계산식은 동일한 qbc/hbc를 사용한다.
