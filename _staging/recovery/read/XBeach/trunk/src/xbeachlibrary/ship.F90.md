---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/ship.F90
lines: 459
sha256: 3de3ac9f8f31964fb511e526cb401a0531fb0d523906f0623d0c2481014f25aa
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# ship.F90 — 판독 구간 기록

구간은 1행부터 459행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 저작권·LGPL 2.1 머리말. |
| 27–74 | `ship_module`·파생형 ship 선언(27–71): 이름·격자 간격/개수·force/motion/flying/heading 옵션, 형상·중심 좌표, depth/zhull/zs/ph, 이동 시계열, 질량/관성, 매핑 작업 배열. contains(73). |
| 75–113 | `ship_init` 인수·모듈·지역 변수(75–90), `logical                                     :: toall = .true.` (91). `if(par%ships==1) then` (95)이면 `par%nship = count_lines(par%shipfile)` (98), ship 배열 할당(100). 그 안의 `if (xmaster) then` (101)에서 `create_new_fid`·파일 열기·선박 이름 읽기·닫기(102–107). master 블록 밖·ships 활성 안의 `USEMPI`는 이름별 `xmpi_bcast(sh(i)%name,toall)` (111). |
| 114–129 | 95의 활성 분기 안에서 선박별 루프 시작(114). `sh(i)%dx  = readkey_dbl(sh(i)%name,'dx',  5.d0,   0.d0,      100.d0)` (116), `sh(i)%dy  = readkey_dbl(sh(i)%name,'dy',  5.d0,   0.d0,      100.d0)` (117); `sh(i)%nx  = readkey_int(sh(i)%name,'nx',  20,        1,      1000  )` (118), `sh(i)%ny  = readkey_int(sh(i)%name,'ny',  20,        1,      1000  )` (119). `sh(i)%shipgeom = readkey_name(sh(i)%name,'shipgeom',required=.true.)` (120). `sh(i)%xCG  = readkey_dbl(sh(i)%name,'xCG',  0.d0,   -1000.d0,      1000.d0)` (121), `sh(i)%yCG  = readkey_dbl(sh(i)%name,'yCG',  0.d0,   -1000.d0,      1000.d0)` (122), `sh(i)%zCG  = readkey_dbl(sh(i)%name,'zCG',  0.d0,   -1000.d0,      1000.d0)` (123). `sh(i)%shiptrack = readkey_name(sh(i)%name,'shiptrack',required=.true.)` (124). `sh(i)%compute_force  = readkey_int(sh(i)%name,'compute_force' ,  0,  0, 1)` (125), `sh(i)%compute_motion = readkey_int(sh(i)%name,'compute_motion',  0,  0, 1)` (126), `sh(i)%flying         = readkey_int(sh(i)%name,'flying',  0,  0, 1)` (127), `sh(i)%read_heading   = readkey_int(sh(i)%name,'read_heading',  0,  0, 1)` (128): 기본값·하한·상한을 호출 인수 그대로 전달. |
| 130–164 | 95 활성·114 선박 루프 안. 선박 격자 배열 할당(130–135), `n2=(sh(i)%nx+1)*(sh(i)%ny+1)` (136), n2/4×n2 매핑 배열 할당(137–145), ph/zs 0(146–147). `create_new_fid` (149), `if(xmaster)` (151,156)일 때 형상 파일 열기/닫기; 행별 `read_v` (154). 별도 `if (sh(i)%compute_motion==0) then` (158)이면 `sh(i)%zhull=-sh(i)%depth` (159); 그 조건 종료 후 독립 `if (sh(i)%compute_force==0) then` (161)이면 ph=depth(162). |
| 165–191 | 95 활성·114 선박 루프 안. `sh(i)%track_nt=count_lines(sh(i)%shiptrack)` (167), `create_new_fid` (169) 및 `if(xmaster)` 파일 열기(170), 5개 이동 배열 할당(172–176). `if (sh(i)%flying==0) then` (178) 안의 `if (sh(i)%read_heading==0) then` (179)이면 t,x,y를 `read_v` (181); else t,x,y,dir를 `read_v` (186), `sh(i)%track_dir(it)=par%px/180d0*(270d0-sh(i)%track_dir(it))` (188). heading 분기 밖·flying==0 안에서 track_z=0(191). |
| 192–219 | 95의 ships 활성 분기·114 선박 루프·178 flying 조건의 else(192) 안에서 시작. 그 안 `if (sh(i)%read_heading==0) then` (193)이면 t,x,y,z를 `read_v` (195), else t,x,y,dir,z를 `read_v` (200), `sh(i)%track_dir(it)=par%px/180d0*(270d0-sh(i)%track_dir(it))` (202). flying 조건 밖 `if(xmaster) close(fid)` (206). 이어 별도 `if (sh(i)%read_heading==0) then` (210): `sh(i)%track_dir(1)=atan2(sh(i)%track_y(2)-sh(i)%track_y(1),sh(i)%track_x(2)-sh(i)%track_x(1))` (211), 내부 시점 `sh(i)%track_dir(it)=atan2(sh(i)%track_y(it+1)-sh(i)%track_y(it-1),sh(i)%track_x(it+1)-sh(i)%track_x(it-1))` (213), 마지막 시점 `sh(i)%track_dir(it)=atan2(sh(i)%track_y(it)-sh(i)%track_y(it-1),sh(i)%track_x(it)-sh(i)%track_x(it-1))` (216). 선박 루프 끝(218). |
| 220–241 | 시작은 95의 활성 분기 안·선박 루프 밖. `if (xmaster) then` (221)에서 전역 중심/힘/모멘트/회전각 12개 배열을 nship 크기로 할당(223–234), 중심·힘 6개만 0 초기화(235–240). |
| 242–262 | 95의 ships 조건의 else(242)에서 시작. 그 안 `if (xmaster) then` (243)에서 동일 12개 배열을 par%nship 크기로 할당(246–257), 조건·루틴 종료(258–261). |
| 263–290 | `shipwave` 선언·매핑/보간 의존성(263–277). `logical, save                               :: firstship=.true.` (278), iprint=0 및 `real                                        :: xymiss=-999` (280–281), 지역 allocatable zsvirt(283). `if (.not. allocated(zsvirt)) allocate(zsvirt(s%nx+1,s%ny+1))` (287), `zsvirt=s%zs+s%ph` (288); s%ph는 0으로 되돌림(289). |
| 291–320 | 선박 루프 시작(291), 이전 x/y 저장(295–296), `linear_interp`로 t에서 x/y(297–298). `if (sh(i)%flying==1) then` (299)이면 z 보간(300), else z=0(302). 조건 밖 dir 보간(304), `radius=max(sh(i)%nx*sh(i)%dx,sh(i)%ny*sh(i)%dy)/2` (305), `cosdir=cos(dirship)` (306), `sindir=sin(dirship)` (307). 격자 루프의 `sh(i)%x(ix,iy)=s%shipxCG(i)+(ix-sh(i)%nx/2-1)*sh(i)%dx*cosdir - (iy-sh(i)%ny/2-1)*sh(i)%dy*sindir` (314), `sh(i)%y(ix,iy)=s%shipyCG(i)+(ix-sh(i)%nx/2-1)*sh(i)%dx*sindir + (iy-sh(i)%ny/2-1)*sh(i)%dy*cosdir` (315). `n1=(s%nx+1)*(s%ny+1)` (319), `n2=(sh(i)%nx+1)*(sh(i)%ny+1)` (320). |
| 321–353 | 291 선박 루프 안. MKMAP 1회 수행 제안 주석(321–322), 실제로 `MKMAP` (323–326)·`GRMAP` (327–328)은 조건 없이 호출. `if (sh(i)%compute_force==1) then` (330)에서 `sh(i)%ph = sh(i)%zs-sh(i)%zhull` (333), `ship_force` (337). 그 안 `if (sh(i)%compute_motion==1) then` (339): 움직임 갱신 TBD 주석(342), 격자 루프의 `sh(i)%zhull(ix,iy)=s%shipzCG(i)-sh(i)%zCG-sh(i)%depth(ix,iy) &` / `& -(sh(i)%x(ix,iy)-sh(i)%xCG)*sin(s%shipchi(i))  &` / `& +(sh(i)%y(ix,iy)-sh(i)%yCG)*sin(s%shipphi(i))` (348–350). 353에서 motion 조건 종료. |
| 354–369 | 291 루프·330 force then 안에서 시작, motion 조건은 닫힘. 제안식은 주석(357). `sh(i)%ph = -sh(i)%zhull` (358), `sh(i)%ph = max(sh(i)%ph,0.d0)` (359); 격자별 `if (sh(i)%depth(ix,iy)==0) sh(i)%ph(ix,iy)=0.d0` (362). 330의 else(365)에서는 `sh(i)%ph = -sh(i)%zhull-s%shipzCG(i)` (366), `sh(i)%ph = max(sh(i)%ph,0.d0)` (367). 368에서 force 조건 끝. |
| 370–398 | 291 선박 루프 안·force 조건 밖에서 `grmap2` 호출(372–373)에 XBeach 압력·면적과 선박 압력·셀 면적 `sh(i)%dx*sh(i)%dy` (372), 매핑 가중치 및 4개 참조점(373)을 전달. 374–397은 전부 비활성 주석: 역회전 좌표·격자 번호·쌍선형 보간 대체 코드. 398에서 선박 루프 종료. |
| 399–413 | 선박 루프 밖. `if (firstship) then` (403)이면 초기조건 `s%zs=s%zs-s%ph` (407). 이 조건 밖에서 firstship=false(410), shipwave 끝(412). |
| 414–433 | `ship_force` 선언·인수·지역 변수(414–421), 힘/모멘트 6개를 0으로 설정(426–431). `hdx=.5d0*sh%dx` (432), `hdy=.5d0*sh%dy` (433). |
| 434–448 | iy=1:ny, ix=1:nx 셀 루프(434–435). `dFx=.5*(sh%ph(ix,iy)+sh%ph(ix+1,iy))*(sh%depth(ix+1,iy)-sh%depth(ix,iy))*sh%dy` (436), `dFy=.5*(sh%ph(ix,iy)+sh%ph(ix,iy+1))*(sh%depth(ix,iy+1)-sh%depth(ix,iy))*sh%dx` (437), `dFz=sh%ph(ix,iy)*sh%dx*sh%dy` (438). 누적 `s%shipFx(i)=s%shipFx(i)+dFx` (439), `s%shipFy(i)=s%shipFy(i)+dFy` (440), `s%shipFz(i)=s%shipFz(i)+dFz` (441). `s%shipMx(i)=s%shipMx(i)+((sh%y(ix,iy)+hdy)-sh%yCG)*dFz-(.5d0*(sh%zhull(ix,iy)+sh%zhull(ix,iy+1))-sh%zCG)*dFy` (442), `s%shipMy(i)=s%shipMy(i)-((sh%x(ix,iy)+hdx)-sh%xCG)*dFz+(.5d0*(sh%zhull(ix,iy)+sh%zhull(ix+1,iy))-sh%zCG)*dFx` (443). 444은 비활성 대체식. `s%shipMz(i)=s%shipMz(i)-(.5*(((iy-sh%ny/2-1)*sh%dy-sh%yCG)+((iy+1-sh%ny/2-1)*sh%dy-sh%yCG)))*dFx &` / `& +(.5*(((ix-sh%nx/2-1)*sh%dx-sh%xCG)+((ix+1-sh%nx/2-1)*sh%dx-sh%xCG)))*dFy` (445–446). |
| 449–459 | 셀 루프 밖 단위 계수 곱셈 `s%shipFx(i)=s%shipFx(i)      *par%rho*par%g` (449), `s%shipFy(i)=s%shipFy(i)      *par%rho*par%g` (450), `s%shipFz(i)=s%shipFz(i)      *par%rho*par%g` (451), `s%shipMx(i)=s%shipMx(i)      *par%rho*par%g` (452), `s%shipMy(i)=s%shipMy(i)      *par%rho*par%g` (453), `s%shipMz(i)=s%shipMz(i)      *par%rho*par%g` (454). 빈 줄·루틴·모듈 종료. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 158–160·333·337–350: 초기화 루틴(`ship_init`) 안에서 zhull은 compute_motion==0 분기(158–160)에서만 대입된다(그 밖에는 `shipwave`의 motion 분기 348–350에서도 대입). [10-02 검증 정정: 범위 명확화] shipwave의 force 분기는 먼저 zhull로 압력과 힘을 계산하고, 그 뒤 motion 분기에서 zhull을 갱신한다.
- 232–240·348–350: 회전각 배열은 할당되지만 초기화 루틴에서 값을 설정하지 않는다. motion 분기의 zhull 식은 shipchi/shipphi를 참조하며 움직임 갱신은 TBD 주석(342)이다.
- 167·210–216: 이동 자료 길이를 세고 첫 방향 산출에서 두 번째 점을 참조하지만, track_nt>=2 검사는 이 파일에 없다.
- 295–296·305·321–326: shipx_old·shipy_old·radius는 대입 뒤 사용되지 않는다. 정지 선박에 MKMAP을 한 번만 적용한다는 주석과 달리 호출을 거르는 조건은 없다.
- 362·365–368: depth==0인 셀의 압력 0 처리는 compute_force==1 분기에서만 실행한다.
- 278·403–410: firstship은 저장 변수이고 첫 호출 뒤 false가 된다. ship_init에서 이 값을 다시 true로 설정하는 코드는 없다.
- 314–315·445–446: 중심 기준 인덱스에서 정수 nx/2·ny/2를 사용한다. ship 형의 mass·Jx·Jy·Jz(58–61)는 이 파일의 루틴들에서 읽거나 계산하지 않는다.
