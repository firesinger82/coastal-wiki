---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_interpolated_wavefield_Hs_dir_Tp.m
lines: 107
sha256: ce00eda92477d507e6d2bd70e9439a44c03537fdb8ac0efd7fba1a7c5f667422
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_interpolated_wavefield_Hs_dir_Tp.m — 판독 구간 기록

구간은 1행부터 107행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | 함수 시그니처는 `function [ Hg,phiwg,iwtw,phiwg_wr,Hg_wr ] = get_interpolated_wavefield_Hs_dir_Tp( xg,yg,Hg_all,phiwg_all,Hso,phiw0,Tp0,Hstab,dirtab,Tptab )` (1). 파고(wave height)·파향(wave direction) 변환장의 보간(interpolation) 목적을 설명한다(2–6). 조건 수에 관한 주석은 `nHs times nphiw conditions`이다(7). 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(9–36). [10-12 전수 검증 정정] |
| 37–60 | 시작 시 1행 get_interpolated_wavefield_Hs_dir_Tp 함수 안. iwtw=0으로 시작한다(37). 방향 표를 펼치는 반복은 `for i=2:length(dirtab)` (38). `if dirtab(i)<dirtab(i-1)` (39)이면 `dirtab(i)=dirtab(i)+360;` (40). `if phiw0<dirtab(1)` (43)이면 `phiw0=phiw0+360;` (44). 그 안에서 `if phiw0>dirtab(end)` (45)이면 경고를 출력하고 phiw0=0·Hso=0·iwtw=1로 설정한다(46–49). 별도 `if phiw0>dirtab(end)` (52)이면 `phiw0=phiw0-360;` (53). 그 안에서 `if phiw0<dirtab(1)` (54)이면 같은 경고와 세 값을 설정한다(55–58). 두 방향 범위 분기는 51·60행에서 닫힌다. |
| 61–80 | 시작 시 1행 get_interpolated_wavefield_Hs_dir_Tp 함수 안. 세 입력값을 표의 양 끝으로 제한하는 식은 `Hso=max(min(Hso,Hstab(end)),Hstab(1));` (61), `phiw0=max(min(phiw0,dirtab(end)),dirtab(1));` (62), `Tp0=max(min(Tp0,Tptab(end)),Tptab(1));` (63). 표 크기와 번호 배열은 `nHs=length(Hstab);` (64); `ndir=length(dirtab);` (65); `nTp=length(Tptab);` (66); `numHs=[1:nHs];` (67); `numdir=[1:ndir];` (68); `numTp=[1:nTp];` (69). interp1 호출은 `indHs=interp1(Hstab,numHs,Hso);` (70); `inddir=interp1(dirtab,numdir,phiw0);` (71); `indTp=interp1(Tptab,numTp,Tp0);` (72). 하위 인덱스(index)와 상위 인덱스는 `ind(1,1)=min(floor(indHs),nHs-1);` (73); `ind(1,2)=min(floor(inddir),ndir-1);` (74); `ind(1,3)=min(floor(indTp),nTp-1);` (75); `ind(2,:)=ind(1,:)+1;` (76). 보간 가중치(weight)는 `w(1,1)=ind(2,1)-indHs;` (77); `w(1,2)=ind(2,2)-inddir;` (78); `w(1,3)=ind(2,3)-indTp;` (79); `w(2,:)=1-w(1,:);` (80). |
| 81–102 | 시작 시 1행 get_interpolated_wavefield_Hs_dir_Tp 함수 안. 빈 줄 뒤 Hg·cosphiwg·sinphiwg를 xg와 같은 크기의 0 배열로 초기화한다(81–85). 삼중 반복은 `for k=1:2` (86), `for j=1:2` (87), `for i=1:2` (88). i1·j2·k3는 ind의 해당 성분을 복사한다(89–91). 파고 누적식은 `Hg=Hg+squeeze(Hg_all(:,:,  i1,    j2,    k3)) ...` (92); `*w(i,1)*w(j,2)*w(k,3);` (93). 파고를 곱한 방향 코사인(cosine) 누적식은 `cosphiwg=cosphiwg+squeeze(cosd(phiwg_all(:,:,  i1,    j2,    k3))  ...` (94); `.*Hg_all(:,:,  i1,    j2,    k3)) ...` (95); `*w(i,1)*w(j,2)*w(k,3);` (96). 방향 사인(sine) 누적식은 `sinphiwg=sinphiwg+squeeze(sind(phiwg_all(:,:,  i1,    j2,    k3))  ...` (97); `.*Hg_all(:,:,  i1,    j2,    k3)) ...` (98); `*w(i,1)*w(j,2)*w(k,3);` (99). 세 반복을 닫는다(100–102). |
| 103–107 | 시작 시 1행 get_interpolated_wavefield_Hs_dir_Tp 함수 안. 빈 줄 뒤 방향을 복원하는 식은 `phiwg=mod(atan2d(sinphiwg,cosphiwg),360);` (104). phiwg_wr·Hg_wr는 빈 배열로 반환한다(105–106). 함수가 끝난다(107). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·82–84: 입력 yg는 함수 본문에서 참조하지 않는다. xg는 0 배열의 크기를 정하는 데 사용한다.
- 47–49·56–58·61–63: 방향 범위 경고 분기는 Hso=0을 설정한다. 후속 식은 Hso를 Hstab(1)과 Hstab(end) 사이로 다시 제한한다.
- 64–75·89–99: 이 파일에는 각 표의 길이가 2 이상인지 검사하는 조건이 없다. 하위 인덱스 식은 표 길이에서 1을 뺀 값과 비교한다.
