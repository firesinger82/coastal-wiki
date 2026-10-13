---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/extract_slice.F
lines: 172
sha256: 94292b3e8a9339e0e2dc908d242602dbe4647076a8e4687073216153f670be5e
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# extract_slice.F — 판독 구간 기록

구간은 1행부터 172행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | cppdefs.h를 끼워 넣고 extract_slice_mod를 시작하며 SOLVE3D를 연다(1–3). 저작권·라이선스와 수직 선형 보간(vertical linear interpolation)으로 z=-100m 같은 일정 깊이 3D 슬라이스(slice)를 출력한다는 주석이다(5–14). 격자·모델·타일(tile)·배열 경계·Adata·음의 지형 추종 깊이(terrain-following depth) Adepth·육해 마스크(mask)·음의 z_slice와 Aslice 출력을 설명한다(18–34). 원문 조건·루프·대입·전처리: `#include "cppdefs.h"` (1)；`#ifdef SOLVE3D` (3). |
| 38–48 | 시작 시 3행 `#ifdef SOLVE3D` 안. mod_param·mod_scalars를 사용하고 implicit none을 선언한다(38–41). extract_slice만 PUBLIC으로 지정하고 기본 PRIVATE·CONTAINS·구분 주석을 둔다(43–48). |
| 49–79 | 시작 시 3행 `#ifdef SOLVE3D` 안. `extract_slice` 시작과 MASKING에서 Amask 인수 추가이다(49–56). 정수 입력과 z_slice(:)를 선언한다(60–62). ASSUMED_SHAPE에서 Adata/Adepth/Aslice의 하한만 명시하며 Aslice 세 번째 하한도 LBk이다(64–70). ELSE에서는 Adata/Adepth의 세 경계와 Aslice의 수평 경계만 명시한다(71–78). 각 경로의 Amask는 MASKING에서만 선언한다. 원문 조건·루프·대입·전처리: `# ifdef MASKING` (52)；`# endif` (54)；`# ifdef ASSUMED_SHAPE` (64)；`#  ifdef MASKING` (67)；`#  endif` (69)；`# else` (71)；`#  ifdef MASKING` (74)；`#  endif` (76)；`# endif` (78). |
| 80–123 | 시작 시 3행 `#ifdef SOLVE3D`·49행 `SUBROUTINE extract_slice (ng, model, tile, gtype,                 &` 안. 지역 i/iz/j/k/k1/k2·수평 범위·mslice와 마스크·깊이·가중치를 선언한다(82–87). gtype 선택에서 PSI는 Istr/Iend·Jstr/Jend, RHO/W는 R 경계, U는 Istr부터 IendR와 JstrR부터 JendR, V는 IstrR부터 IendR와 Jstr부터 JendR를 사용한다(95–116). mslice=SIZE(z_slice)로 요청 깊이 수를 정한다(120). 원문 조건·루프·대입·전처리: `SELECT CASE (gtype)` (95)；`CASE (p3dvar)` (96)；`Imin=BOUNDS(ng)%Istr (tile)` (97)；`Imax=BOUNDS(ng)%Iend (tile)` (98)；`Jmin=BOUNDS(ng)%Jstr (tile)` (99)；`Jmax=BOUNDS(ng)%Jend (tile)` (100)；`CASE (r3dvar, w3dvar)` (101)；`Imin=BOUNDS(ng)%IstrR(tile)` (102)；`Imax=BOUNDS(ng)%IendR(tile)` (103)；`Jmin=BOUNDS(ng)%JstrR(tile)` (104)；`Jmax=BOUNDS(ng)%JendR(tile)` (105)；`CASE (u3dvar)` (106)；`Imin=BOUNDS(ng)%Istr (tile)` (107)；`Imax=BOUNDS(ng)%IendR(tile)` (108)；`Jmin=BOUNDS(ng)%JstrR(tile)` (109)；`Jmax=BOUNDS(ng)%JendR(tile)` (110)；`CASE (v3dvar)` (111)；`Imin=BOUNDS(ng)%IstrR(tile)` (112)；`Imax=BOUNDS(ng)%IendR(tile)` (113)；`Jmin=BOUNDS(ng)%Jstr (tile)` (114)；`Jmax=BOUNDS(ng)%JendR(tile)` (115)；`mslice = SIZE(z_slice)` (120). |
| 124–143 | 시작 시 3행 `#ifdef SOLVE3D`·49행 `SUBROUTINE extract_slice (ng, model, tile, gtype,                 &` 안. j·i 처리 범위를 순회한다(124–125). MASKING이면 my_mask=Amask(i,j), ELSE이면 1.0_r8이다(126–130). iz=1..mslice에서 my_mask>0.5일 때 상·하 깊이를 읽는다(131–134). z_slice>=Ztop이면 k1/k2=UBk·r1=1·r2=0, Zbot>=z_slice이면 r1/r2=0이다(135–142). 그 밖의 깊이는 ELSE를 연다(143). 원문 조건·루프·대입·전처리: `DO j=Jmin,Jmax` (124)；`DO i=Imin,Imax` (125)；`# ifdef MASKING` (126)；`my_mask=Amask(i,j)` (127)；`# else` (128)；`my_mask=1.0_r8` (129)；`# endif` (130)；`DO iz=1,mslice` (131)；`IF (my_mask.gt.0.5_r8) THEN` (132)；`Ztop=Adepth(i,j,UBK)` (133)；`Zbot=Adepth(i,j,LBK)` (134)；`IF (z_slice(iz).ge.Ztop) THEN    ! shallower than top grid` (135)；`k1=UBk                         ! cell. The slice is in` (136)；`k2=UBK                         ! the upper cell half` (137)；`r1=1.0_r8                      ! shallower than top grid` (138)；`r2=0.0_r8                      ! above its middle depth` (139)；`ELSE IF (Zbot.ge.z_slice(iz)) THEN` (140)；`r1=0.0_r8                      ! If deeper, ignore` (141)；`r2=0.0_r8` (142)；`ELSE` (143). |
| 144–155 | 시작 시 3행 `#ifdef SOLVE3D`·49행 `SUBROUTINE extract_slice (ng, model, tile, gtype,                 &`·124행 `DO j=Jmin,Jmax`·125행 `DO i=Imin,Imax`·131행 `DO iz=1,mslice`·132행 `IF (my_mask.gt.0.5_r8) THEN`·135행 `IF (z_slice(iz).ge.Ztop) THEN    ! shallower than top grid`의 143행 `ELSE` 분기 안. k=UBk..LBk+1 역순으로 각 깊이 구간을 검사한다(144–147). Ztop>z_slice이며 z_slice>=Zbot이면 k1=k-1·k2=k를 저장한다(148–150). 순회 후 dz·r2·r1를 계산하고 수심 분기를 닫는다(151–155). 원문 조건·루프·대입·전처리: `DO k=UBk,LBk+1,-1              ! Otherwise, interpolate` (144)；`Ztop=Adepth(i,j,k  )         ! field at slice depth` (145)；`Zbot=Adepth(i,j,k-1)` (146)；`IF ((Ztop.gt.z_slice(iz)).and.(z_slice(iz).ge.Zbot)) THEN` (147)；`k1=k-1` (148)；`k2=k` (149)；`dz=Adepth(i,j,k2)-Adepth(i,j,k1)` (152)；`r2=(z_slice(iz)-Adepth(i,j,k1))/dz` (153)；`r1=1.0_r8-r2` (154). |
| 156–172 | 시작 시 3행 `#ifdef SOLVE3D`·49행 `SUBROUTINE extract_slice (ng, model, tile, gtype,                 &`·124행 `DO j=Jmin,Jmax`·125행 `DO i=Imin,Imax`·131행 `DO iz=1,mslice`·132행 `IF (my_mask.gt.0.5_r8) THEN` 안. r1+r2>0이면 Aslice는 r1*Adata(i,j,k1)+r2*Adata(i,j,k2)이다(156–157). ELSE이면 spval을 넣는다(158–160). my_mask>0.5의 ELSE는 육지값 0.0_r8이다(161–163). 모든 루프·루틴·SOLVE3D·모듈을 끝내고 마지막 빈 줄까지 포함한다(164–172). 원문 조건·루프·대입·전처리: `IF ((r1+r2).gt.0.0_r8) THEN` (156)；`Aslice(i,j,iz)=r1*Adata(i,j,k1) + r2*Adata(i,j,k2)` (157)；`ELSE` (158)；`Aslice(i,j,iz)=spval           ! unbounded slice depth` (159)；`ELSE` (161)；`Aslice(i,j,iz)=0.0_r8            ! land masked value` (162)；`#endif` (170). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 70·77·131·157–162: ASSUMED_SHAPE의 Aslice는 세 번째 차원 하한을 LBk로 선언한다. ELSE의 Aslice는 세 번째 차원을 콜론으로 선언한다. 실행부의 슬라이스 인덱스 iz는 두 경로 모두 1..mslice이다.
- 95–116: gtype 선택은 p3dvar·r3dvar/w3dvar·u3dvar·v3dvar case만 있다. CASE DEFAULT와 선택 전에 수평 범위를 초기화하는 문장은 없다.
- 135–142·156–162: 최상층 깊이와 같거나 더 얕으면 최상층 값에 가중치 1을 준다. 최하층 깊이와 같거나 더 깊으면 가중치를 모두 0으로 만들어 spval을 출력한다. 마스크가 0.5 이하이면 출력값은 spval이 아니라 0.0_r8이다.
- 144–154: 깊이 구간 검색 루프는 일치한 뒤에도 EXIT 없이 계속 돈다. k1/k2는 일치 조건 안에서 설정하며 검색 성공 플래그는 없다. 이후 r2 계산은 dz로 나누고 이 블록에 dz=0 검사는 없다.
