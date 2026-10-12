---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_interpolated_wavefield_dir_Tp.m
lines: 115
sha256: 028fd41f4c9db8a21b37290296eee88a908ed9d411cbee6164dea9deb1d7954f
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_interpolated_wavefield_dir_Tp.m — 판독 구간 기록

구간은 1행부터 115행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | 함수 시그니처는 `function [ Hg,phiwg,iwtw,phiwg_wr,Hg_wr ] = get_interpolated_wavefield_dir_Tp( xg,yg,Hg_all,phiwg_all,Hso,phiw0,Tp0,dirtab,Tptab )` (1). 파고(wave height)·파향(wave direction) 변환장의 보간(interpolation) 목적과 표 조건에 관한 주석을 포함한다(2–8). 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(9–36). |
| 37–60 | 시작 시 1행 get_interpolated_wavefield_dir_Tp 함수 안. iwtw=0으로 시작한다(37). 방향 표의 반복은 `for i=2:length(dirtab)` (38). `if dirtab(i)<dirtab(i-1)` (39)이면 `dirtab(i)=dirtab(i)+360;` (40). `if phiw0<dirtab(1)` (43)이면 `phiw0=phiw0+360;` (44). 그 안에서 `if phiw0>dirtab(end)` (45)이면 경고를 출력하고 phiw0=0·Hso=0·iwtw=1로 설정한다(46–49). 별도 `if phiw0>dirtab(end)` (52)이면 `phiw0=phiw0-360;` (53). 그 안에서 `if phiw0<dirtab(1)` (54)이면 같은 경고와 세 값을 설정한다(55–58). 두 방향 범위 분기를 닫는다(51·60). |
| 61–87 | 시작 시 1행 get_interpolated_wavefield_dir_Tp 함수 안. 방향 제한식은 `phiw0=max(min(phiw0,dirtab(end)),dirtab(1));` (61). 표 크기와 번호 배열은 `nTp=length(Tptab);` (62); `ndir=length(dirtab);` (63); `numTp=[1:nTp];` (64); `numdir=[1:ndir];` (65). 외삽(extrapolation)을 넣은 interp1 두 문장은 주석이다(66–67). 실제 보간 호출은 `indTp=interp1(Tptab,numTp,Tp0);` (68); `inddir=interp1(dirtab,numdir,phiw0);` (69). `if any(isnan(indTp))\|\|any(isnan(inddir))` (71)이면 error로 요청 주기 또는 방향의 표 범위 이탈을 알린다(72). 주기 인덱스(index)·가중치(weight)는 `iT1=min(floor(indTp),nTp-1);` (75); `iT2=iT1+1;` (76); `wT1=iT2-indTp;` (77); `wT2=1-wT1;` (78). 방향 인덱스·가중치는 `id1=min(floor(inddir),ndir-1);` (79); `id2=id1+1;` (80); `wd1=id2-inddir;` (81); `wd2=1-wd1;` (82). 네 결합 가중치는 `w1=wT1*wd1;` (84); `w2=wT2*wd1;` (85); `w3=wT1*wd2;` (86); `w4=wT2*wd2;` (87). |
| 88–104 | 시작 시 1행 get_interpolated_wavefield_dir_Tp 함수 안. 파고 보간식은 `Hg=squeeze(Hg_all(:,:,id1,iT1)*w1+Hg_all(:,:,id1,iT2)*w2 ...` (89); `+Hg_all(:,:,id2,iT1)*w3+Hg_all(:,:,id2,iT2)*w4);` (90). 각도를 직접 더하는 두 줄은 주석이다(91–92). 파고를 곱한 방향 코사인(cosine) 보간식은 `cosphiwg=squeeze(cosd(phiwg_all(:,:,id1,iT1)).*Hg_all(:,:,id1,iT1)*w1 ...` (93); `+cosd(phiwg_all(:,:,id1,iT2)).*Hg_all(:,:,id1,iT2)*w2 ...` (94); `+cosd(phiwg_all(:,:,id2,iT1)).*Hg_all(:,:,id2,iT1)*w3 ...` (95); `+cosd(phiwg_all(:,:,id2,iT2)).*Hg_all(:,:,id2,iT2)*w4);` (96). 방향 사인(sine) 보간식은 `sinphiwg=squeeze(sind(phiwg_all(:,:,id1,iT1)).*Hg_all(:,:,id1,iT1)*w1 ...` (97); `+sind(phiwg_all(:,:,id1,iT2)).*Hg_all(:,:,id1,iT2)*w2 ...` (98); `+sind(phiwg_all(:,:,id2,iT1)).*Hg_all(:,:,id2,iT1)*w3 ...` (99); `+sind(phiwg_all(:,:,id2,iT2)).*Hg_all(:,:,id2,iT2)*w4);` (100). 방향 복원식은 `phiwg=atan2d(sinphiwg,cosphiwg);` (101). 파고의 외해 파고 스케일링(scaling) 식은 `Hg=Hg*max(Hso);` (104). 빈 줄과 스케일링 주석을 포함한다(88·102–103). |
| 105–115 | 시작 시 1행 get_interpolated_wavefield_dir_Tp 함수 안. 고정 추출 위치의 행·열 배열은 `row=[22,22,24,30,38];` (106), `col=[40,46,52,60,63];` (107). 추출 반복은 `for iwr=1:5` (109). phiwg_wr·Hg_wr에 해당 행·열 값을 복사한다(110–111). 좌표 plot 문장은 주석이다(112). 반복·함수 종료와 빈 줄을 포함한다(113–115). [10-12 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·112: 입력 xg·yg는 실행문에서 참조하지 않는다. 두 입력이 나타나는 plot 문장은 주석이다.
- 61·68–73: phiw0에는 표 범위 제한식이 있다. Tp0에는 범위 제한식이 없으며 interp1 결과가 NaN이면 error를 호출한다.
- 106–111: 추출 위치는 행 [22,22,24,30,38]·열 [40,46,52,60,63]으로 고정되어 있다. 이 파일에는 해당 행·열과 파랑장 크기를 비교하는 검사문이 없다. [10-12 전수 검증 정정]
