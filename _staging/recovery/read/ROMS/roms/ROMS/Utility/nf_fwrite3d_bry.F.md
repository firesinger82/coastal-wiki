---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/nf_fwrite3d_bry.F
lines: 413
sha256: ad1b7688f5470b1481f57213246dfa8188aac0ceb9c482d1fb6010a6ede2aeaa
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# nf_fwrite3d_bry.F — 판독 구간 기록

구간은 1행부터 413행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–65 | `#include "cppdefs.h"` (1)로 `cppdefs.h`를 포함하고 모듈을 연다(2). `#ifdef ADJUST_BOUNDARY` (4)로 경계 조정(boundary adjustment) 구현을 감싼다. 저작권·라이선스·NetCDF/PIO 3차원 경계장(boundary field) 쓰기·인수·주석과 빈 줄(5–65). PIO 설명은 `# if defined PIO_LIB && defined DISTRIBUTE` (24)·`# endif` (28), `# if defined PIO_LIB && defined DISTRIBUTE` (30)·`# endif` (35) 안이다. ExtractField는 0=추출 없음·1=보간(interpolation)·1보다 큼=간격 추출(decimation)이다(45–48). `# ifdef POSITIVE_ZERO` (56)·`# endif` (63) 안의 주석은 직렬/병렬 출력 비교를 위한 양의 0(positive zero)을 설명한다(57–61). |
| 66–86 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4) 안. 공통 모듈 4개 사용(66–69). `# ifdef DISTRIBUTE` (71)에서 mp_bcasti·mp_collect 사용(72), `#  endif` (73)로 닫는다. pack_boundary3d 사용·implicit none(74·76). 인터페이스에 nf90_fwrite3d_bry 등록(78–79), `# if defined PIO_LIB && defined DISTRIBUTE` (80)에서 pio_fwrite3d_bry 등록(81), `# endif` (82)로 닫는다. 인터페이스 종료·CONTAINS·주석(83–86). |
| 87–130 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4) 안. nf90_fwrite3d_bry 함수 시작(88–94), mod_netcdf 사용(97). 입력 정수·선택적 추출·실수·문자 선언(101–109). `# ifdef ASSUMED_SHAPE` (111)이면 Abry(LBij:,LBk:,:,:) 선언(112), `# else` (113)이면 Abry(LBij:UBij,LBk:UBk,4,Nrec) 선언(114), `# endif` (115)로 닫는다. MinValue·MaxValue는 각각 선택적 출력(optional output)이다(116–117). 길이·점 수·tile·추출 플래그(flag)·상태·start/total(5) 선언(121–125). 상수는 `real(r8), parameter :: Aspv = 0.0_r8` (127)이다. Awrk 크기는 `(UBij-LBij+1)*(UBk-LBk+1)*4*Nrec`(129). |
| 131–166 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4)·88행 NetCDF 루틴 안. status=nf90_noerr(135). `#  ifdef DISTRIBUTE` (139)이면 tile=MyRank(140), `#  else` (141)이면 `tile=-1` (142), `#  endif` (143)로 닫는다. IorJ는 IOBOUNDS에서 복사(148). `Klen=UBk-LBk+1` (149); `IJKlen=IorJ*Klen` (150); `Npts=IJKlen*4*Nrec` (151)로 수직 길이·경계 길이·점 수를 계산한다. `IF (PRESENT(ExtractField)) THEN` (156)이면 Extract_Flag 입력 복사(157), `ELSE` (158)이면 기본 `Extract_Flag=0` (159)이다. Awrk=0 초기화(165). 초기화 설명·주석·빈 줄을 포함한다. |
| 167–194 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4)·88행 NetCDF 루틴 안. 주석은 2D 경계 압축이라고 적는다(168). pack_boundary3d에 격자·변수명·시간·추출 플래그·수평/수직 경계·Nrec·스케일·Abry를 전달하고 start·total·Npts·Awrk를 받는다(171–176). `IF (PRESENT(MinValue)) THEN` (182)의 `IF (OutThread) THEN` (183)에서 MinValue=spval·MaxValue=-spval 초기화(184–185). i=1..Npts 루프(186)의 `IF (ABS(Awrk(i)).lt.spval) THEN` (187)에서 `MinValue=MIN(MinValue,Awrk(i))` (188); `MaxValue=MAX(MaxValue,Awrk(i))` (189)로 최소·최대를 계산한다. 조건·루프 종료(190–193), 주석(194). |
| 195–215 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4)·88행 NetCDF 루틴 안. status=nf90_noerr 초기화(199). `IF (OutThread) THEN` (200)이면 nf90_put_var 호출(201). `# ifdef DISTRIBUTE` (204) 안에서 mp_bcasti로 상태를 전송하고(210) `# endif` (211)로 닫는다. RETURN·함수 종료·빈 줄(213–215). |
| 216–269 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4) 안. `# if defined PIO_LIB && defined DISTRIBUTE` (216)로 PIO 구현을 연다. pio_fwrite3d_bry 함수 시작(219–225), mod_pio_netcdf 사용(228), 입력·선택적 추출·실수·문자 선언(232–240). `#  ifdef ASSUMED_SHAPE` (242)이면 assumed-shape Abry(243), `#  else` (244)이면 명시적 Abry(245), `#  endif` (246)로 닫는다. 최소/최대·파일/변수 기술자(descriptor)·경계 소속·카운터·격자·정밀도·길이·start/total(5)·상태 선언(247–264). 초기값 상수는 `real(r8), parameter :: Aspv = 0.0_r8` (266)이다. Awrk 크기는 `(UBij-LBij+1)*(UBk-LBk+1)*4*Nrec`(268). |
| 270–314 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4)·216행 `# if defined PIO_LIB && defined DISTRIBUTE` (216)·219행 PIO 루틴 안. status=PIO_noerr(274), tile=MyRank, dkind·gtype 복사(278–280). `SELECT CASE (gtype)` (282)의 `CASE (p2dvar, p3dvar)` (283)은 Istr/Iend·Jstr/Jend(284–287), `CASE (r2dvar, r3dvar)` (288)은 IstrR/IendR·JstrR/JendR(289–292), `CASE (u2dvar, u3dvar)` (293)은 Istr/IendR·JstrR/JendR(294–297), `CASE (v2dvar, v3dvar)` (298)은 IstrR/IendR·Jstr/JendR(299–302)를 선택한다. `CASE DEFAULT` (303) 기본값은 rho 경계(304–307). IorJ 복사(310), `Klen=UBk-LBk+1` (311); `IJKlen=IorJ*Klen` (312); `Npts=IJKlen*4*Nrec` (313)으로 수직 길이·경계 길이·점 수를 계산한다. |
| 315–345 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4)·216행 `# if defined PIO_LIB && defined DISTRIBUTE` (216)·219행 PIO 루틴 안. 타일(tile) Istr/Iend/Jstr/Jend 복사(317–320), 서·동·남·북 경계 소속 복사(324–327). start=[1,1,1,1,tindex], total=[IorJ,Klen,4,Nrec,1]로 설정한다(331–340). 압축(pack)·스케일 구분 주석·빈 줄(342–345). |
| 346–383 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4)·216행 `# if defined PIO_LIB && defined DISTRIBUTE` (216)·219행 PIO 루틴 안. Awrk=Aspv 초기화(346). ir=1..Nrec(348)에서 `rc=(ir-1)*IJKlen*4` (349)로 레코드 오프셋(offset)을 계산한다. ib=1..4(350)의 `IF (bounded(ib)) THEN` (351)에서 `bc=(ib-1)*IJKlen+rc` (352)로 방향 오프셋을 계산한다. `IF ((ib.eq.iwest).or.(ib.eq.ieast)) THEN` (353)의 k·j 루프(354·356)는 `kc=(k-LBk)*IorJ+bc` (355)·`ic=1+(j-LBij)+kc` (357); `Awrk(ic)=Abry(j,k,ib,ir)*Ascl` (358)로 인덱스·스케일을 계산한다. `#  ifdef POSITIVE_ZERO` (359)의 `IF (ABS(Awrk(ic)).eq.0.0_r8) THEN` (360)는 양의 0 대입(361), `#  endif` (363)로 닫는다. `ELSE IF ((ib.eq.isouth).or.(ib.eq.inorth)) THEN` (366)의 k·i 루프(367·369)는 `kc=(k-LBk)*IorJ+bc` (368)·`ic=1+(i-LBij)+kc` (370); `Awrk(ic)=Abry(i,k,ib,ir)*Ascl` (371) 계산이다. `#  ifdef POSITIVE_ZERO` (372)의 `IF (ABS(Awrk(ic)).eq.0.0_r8) THEN` (373)는 양의 0 대입(374), `#  endif` (376)로 닫는다. 조건·루프 종료(377–382), 주석(383). |
| 384–413 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4)·216행 `# if defined PIO_LIB && defined DISTRIBUTE` (216)·219행 PIO 루틴 안. mp_collect(ng,model,Npts,Aspv,Awrk) 호출(386). `IF (PRESENT(MinValue)) THEN` (392)에서 MinValue=spval·MaxValue=-spval 초기화(393–394), i=1..Npts 루프(395)의 `IF (ABS(Awrk(i)).lt.spval) THEN` (396)에서 `MinValue=MIN(MinValue,Awrk(i))` (397); `MaxValue=MAX(MaxValue,Awrk(i))` (398)로 최소·최대를 계산한다. 조건·루프 종료(399–401). PIO_put_var로 버퍼를 쓴다(407). RETURN·함수 종료(409–410), `# endif` (411)로 PIO 조건, `#endif` (412)로 ADJUST_BOUNDARY 조건을 닫고 모듈 종료(413). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 168·171–176: NetCDF 압축 구분 주석은 2D boundary라고 적는다. 실제 호출은 수직 경계 LBk·UBk를 전달하는 pack_boundary3d이다.
- 116–117·182–193 및 247–248·392–401: MinValue·MaxValue는 각각 선택적 출력이다. 두 구현은 PRESENT(MinValue)만 검사하고 MaxValue에도 대입한다.
- 235·270–410: PIO 구현은 선택적 ExtractField를 선언한다. 이후 이 인수를 검사하거나 참조하는 실행문은 없다. NetCDF 구현은 추출 플래그를 pack_boundary3d에 전달한다(156–160·171–176).
- 127·165 및 279·317–320: NetCDF 루틴의 Aspv 상수는 선언 뒤 사용되지 않는다. PIO 루틴의 dkind·Istr·Iend·Jstr·Jend는 대입 뒤 참조되지 않는다.
- 266·346–386·395–400: PIO 버퍼 초기값은 0이다. 타일 소유 경계 범위만 채운 뒤 mp_collect를 호출한다. 최소/최대 루프는 ABS(Awrk(i))<spval을 사용하며 0을 제외하는 조건은 없다.
