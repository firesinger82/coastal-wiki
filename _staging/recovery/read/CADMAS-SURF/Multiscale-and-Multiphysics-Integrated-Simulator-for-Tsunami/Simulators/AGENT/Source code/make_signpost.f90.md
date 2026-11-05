---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Source code/make_signpost.f90
lines: 72
sha256: fc55c71e333e95f76364b062ad54b9a8322b30228d7dfd187542d7fdcd3ed3a4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# make_signpost.f90 — 판독 구간 기록

구간은 1행부터 72행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 이정표 설정 주석(3). 모듈·`implicit none`(9)·인수와 지역 변수를 선언한다. 원문: `subroutine make_signpost(ierr)` (1); `!----------------------------------------` (2); `! 道標の設定` (3); `!----------------------------------------` (4); `  use m_potential,only: ipmax,jpmax,dxy,n_signpost &` (5); `                     & ,i_signpost,j_signpost      &` (6); `                     & ,r_signpost,narea_signpost` (7); `  use m_agent,only: n_agent,weight_signpost,iflag_signpost` (8); `  implicit none` (9); `!` (10); `![arguments]` (11); `  integer,intent(out):: ierr` (12); `!` (13); `![local variables]` (14); `  integer:: n,m,i,j,is,js,ie,je,irsign` (15); `  real(8):: rand` (16); `  integer:: ierror` (17); `  character(32):: rout='make_signpost'` (18); `!` (19); `  ierr=0` (20); `!` (21); `!` (22) |
| 23–43 | 시작 시 1행 루틴 안. 각 에이전트가 각 표지에 따르는지 설정한다는 주석(23). iflag_signpost의 첫 차원은 0:n_signpost, 둘째는 n_agent로 할당한다. 난수가 weight_signpost 이하이면 이정표를 따른다는 주석(35)의 값 1, 아니면 이정표 무시라는 주석(37)의 값 0이다. 이정표 범위 밖이면 당연히 무시한다는 주석(40)의 인덱스 0도 0으로 설정한다. 원문: `!各エージェントが各標識に従うかどうかを設定` (23); `  allocate(iflag_signpost(0:n_signpost,n_agent),stat=ierror)` (24); `  if(ierror/=0) then` (25); `     ierr=-10` (26); `     call errmsg(rout,ierr)` (27); `     write(*,*) 'cannot allocate iflag_signpost arrays'` (28); `  endif` (29); `!` (30); `  do n=1,n_agent` (31); `    do m=1,n_signpost` (32); `      call random_number(rand)` (33); `      if(rand<=weight_signpost(n))then` (34); `        iflag_signpost(m,n)=1    !道標に従う` (35); `      else` (36); `        iflag_signpost(m,n)=0    !道標を無視` (37); `      endif` (38); `    enddo` (39); `        iflag_signpost(0,n)=0    !道標範囲外なら当然無視` (40); `  enddo` (41); `!` (42); `!` (43) |
| 44–72 | 시작 시 1행 루틴 안. 영역 안 각 이정표 유효 영역 설정 주석(44). r_signpost/dxy의 정수 반경을 쓰고 영역 밖 범위를 제한한다. 원 내부 셀에 이정표 번호를 넣는다. 표지 유효 범위를 map_signpost.csv에 디버그 출력한다는 주석(64)대로 j 역순으로 쓴다. 원문: `!領域内での各道標の有効域を設定` (44); `  narea_signpost(:,:)=0` (45); `  do n=1,n_signpost` (46); `    irsign =int(r_signpost(n)/dxy)` (47); `    is=i_signpost(n)-irsign` (48); `      if(is<1) is=1` (49); `    ie=i_signpost(n)+irsign` (50); `      if(ie>ipmax) ie=ipmax` (51); `    js=j_signpost(n)-irsign` (52); `      if(js<1) js=1` (53); `    je=j_signpost(n)+irsign` (54); `      if(je>jpmax) je=jpmax` (55); `    do j=js,je` (56); `    do i=is,ie` (57); `      if((i_signpost(n)-i)**2+(j_signpost(n)-j)**2<=irsign**2) &` (58); `       & narea_signpost(i,j)=n` (59); `    enddo` (60); `    enddo` (61); `  enddo` (62); `!` (63); `![DebugWrite]標識の有効範囲をmap_signpost.csvに出力` (64); `  open(99,file='map_signpost.csv')` (65); `  do j=jpmax,1,-1` (66); `     write(99,'(10000(i5,'',''))') (narea_signpost(i,j),i=1,ipmax)` (67); `  enddo` (68); `  close(99)` (69); `!` (70); `  return` (71); `end subroutine make_signpost` (72) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 46–62: 이정표 유효 영역이 겹치면 뒤에서 순회한 번호가 같은 셀의 narea_signpost를 덮어쓴다.
