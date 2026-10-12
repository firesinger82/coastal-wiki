---
file: models/ShorelineS/raw/source_code/shorelines/functions/update_bathy.m
lines: 108
sha256: fbe8bf797b98d97d991741d7d79942cb976cbd5d86b163c708c6c74a0b9c6ba5
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# update_bathy.m — 판독 구간 기록

구간은 1행부터 108행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | 함수 시그니처(1), 1차원·2차원 결합 모델(coupled model)의 수심 지형(bathymetry) 갱신 목적(4), 저작권·LGPL·무보증 주석과 빈 줄(6–33). 입력 S·BATHY·TIME·COAST의 기본값 설정문은 없다. 원문: `function [S,BATHY]=update_bathy(S,BATHY,TIME,COAST)` (1). |
| 34–66 | 시작 시 1행 함수 안. bathyupdate가 비어 있지 않고 dt가 갱신 시간 차이/365와 같을 때 처리한다(34). TIME.it로 S.bathyname을 만들고 wlgrid·wldep를 호출하여 격자와 부호를 바꾼 바닥고를 읽고 마지막 행·열을 제외한다(37–47). Dean 단면 계수 A=0.1과 폐쇄수심(depth of closure) Dc=S.d를 정한다(48–49). 그림과 이전 거리 계산 루프는 주석이며 격자 좌표·기존 바닥고를 복사하고 zgu를 0으로 초기화한다(50–66). 원문: `if ~isempty(S.bathyupdate)&& S.dt==(BATHY.tupdate-tnow)/365` (34), `S.bathyname=strcat('modified_it',num2str(TIME.it),'.dep');` (37), `grid=wlgrid('read',S.gridfile);` (38), `x=grid.X;` (39), `y=grid.Y;` (40), `S.xg=x;` (41), `S.yg=y;` (42), `nx=size(x,1)-1;` (43), `ny=size(x,2)-1;` (44), `zb=-wldep('read',S.depfile,grid);` (45), `zb=zb(1:end-1,1:end-1);` (46), `S.zg=zb;` (47), `A=0.1;  %Dean profile factor` (48), `Dc=S.d; %closure depth` (49), `xg=S.xg;` (58), `yg=S.yg;` (59), `zg0=zb;` (60), `zgu=zeros(size(xg));` (66). |
| 67–95 | 시작 시 1행 함수·34행 지형 갱신 참 분기 안. 두 격자 루프에서 마지막 인수로 100000을 넘겨 get_disttopolyline을 호출하고 −A·dist^(2/3)를 계산한다(67–70). surfwidth 이내에서는 zgu, else에서는 min(Dc,zg0)를 쓴다(71–75). inpolygon 내부는 양의 Dean 식과 landmax로 제한한다(78–84). NaN을 999로 바꾸고 깊이 부호를 뒤집어 마지막 행·열을 복제한 뒤 wldep write를 호출한다(85–89). S.depfile과 S.zg를 갱신한다(90·94). 원문: `for i=1:size(xg,2);` (67), `for j=1:size(xg,1);` (68), `[dist(j,i),ip]=get_disttopolyline(COAST.x_mc,COAST.y_mc,xg(j,i),yg(j,i),100000);` (69), `zgu(j,i)=-A*(dist(j,i)).^(2/3);` (70), `if dist(j,i) <= S.surfwidth` (71), `zg(j,i)=zgu(j,i);` (72), `else` (73), `zg(j,i)=min(Dc,zg0(j,i));` (74), `IN=inpolygon(xg,yg,COAST.x_mc,COAST.y_mc);` (78), `zg(IN)=min(A*(dist(IN)).^(2/3),S.landmax);` (83), `zgu(IN)=min(A*(dist(IN)).^(2/3),S.landmax);` (84), `zg(isnan(zg))=999;` (85), `dps=-zg;` (86), `dps=[dps dps(:,end);dps(end,:) dps(end,end)];` (88), `wldep('write',S.bathyname,'',dps)` (89), `S.depfile=S.bathyname;` (90), `S.zg=zg;` (94). [10-12 전수 검증 정정] |
| 96–108 | 시작 시 1행 함수·34행 지형 갱신 참 분기 안. TIME.it로 S.wavefile을 만들고 waverefrac_implicit을 호출한 뒤 그림 1·2를 닫는다(97–100). BATHY.tbu를 증가시키고 다음 update_time을 선택한다(103–104). 조건·함수 끝과 빈 줄(106–108). 원문: `S.wavefile=strcat('Wave_table',num2str(TIME.it));` (97), `[S]=waverefrac_implicit(S);` (98), `close(figure(1));` (99), `close(figure(2));` (100), `BATHY.tbu=BATHY.tbu+1;` (103), `BATHY.tupdate=BATHY.update_time(BATHY.tbu);` (104). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 34: tnow는 조건에서 참조되지만 함수 인수나 이 파일의 지역 대입으로 정의되지 않는다.
- 43–44: nx·ny는 계산 이후 이 파일에서 참조되지 않는다.
- 34·103–104: 갱신 여부는 시간 차이의 정확한 등식으로 검사한다. tbu 증가 뒤 update_time 배열 끝을 검사하는 조건은 이 파일에 없다.
- 48·69·85: Dean 계수 0.1, get_disttopolyline의 마지막 인수 100000, NaN 바닥고 대체값 999는 하드코딩되어 있다. [10-12 전수 검증 정정]
