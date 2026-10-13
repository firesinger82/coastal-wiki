---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/nf_fwrite2d_bry.F
lines: 397
sha256: 25cba5f528cfa6bc61e00ad284c60d90067bd841c0790ab3aeb9c117860c801f
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# nf_fwrite2d_bry.F — 판독 구간 기록

구간은 1행부터 397행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–63 | `#include "cppdefs.h"` (1)로 `cppdefs.h`를 포함하고 모듈을 연다(2). `#ifdef ADJUST_BOUNDARY` (4)로 경계 조정(boundary adjustment) 구현 전체를 감싼다. 저작권·라이선스·NetCDF/PIO 2차원 경계장(boundary field) 쓰기 설명·인수·주석과 빈 줄(5–63). PIO 설명은 `# if defined PIO_LIB && defined DISTRIBUTE` (23)·`# endif` (27), `# if defined PIO_LIB && defined DISTRIBUTE` (30)·`# endif` (35) 안이다. ExtractField는 0=추출 없음·1=보간(interpolation)·1보다 큼=간격 추출(decimation)이다(43–46). `# ifdef POSITIVE_ZERO` (54)·`# endif` (61) 안의 주석은 직렬/병렬 비교를 위해 양의 0(positive zero)을 강제한다고 설명한다(55–59). |
| 64–84 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4) 안. 공통 모듈 사용(64–67). `# ifdef DISTRIBUTE` (69) 안에서 mp_bcasti·mp_collect 사용(70), `# endif` (71)로 닫는다. pack_boundary2d 사용·implicit none(72·74). 인터페이스에 nf90_fwrite2d_bry 등록(76–77), `# if defined PIO_LIB && defined DISTRIBUTE` (78) 안에 pio_fwrite2d_bry 등록(79), `# endif` (80)로 닫는다. 인터페이스 종료·CONTAINS·주석(81–84). |
| 85–126 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4) 안. nf90_fwrite2d_bry 함수 시작(86–92), mod_netcdf 사용(95), 정수·실수·문자·선택적 추출 인수 선언(99–107). `# ifdef ASSUMED_SHAPE` (109)이면 Abry(LBij:,:,:) 선언(110), `# else` (111)이면 Abry(LBij:UBij,4,Nrec) 선언(112), `# endif` (113)로 닫는다. MinValue·MaxValue는 각각 선택적 출력이다(114–115). 카운터·추출 플래그(flag)·상태·start/total(4)·크기 `(UBij-LBij+1)*4*Nrec`인 Awrk 선언(119–125). |
| 127–160 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4)·86행 NetCDF 루틴 안. status=nf90_noerr(131). `#  ifdef DISTRIBUTE` (135)이면 tile=MyRank(136), `#  else` (137)이면 `tile=-1` (138), `#  endif` (139)로 닫는다. IorJ를 IOBOUNDS에서 복사(144), `Npts=IorJ*4*Nrec` (145)로 점 수를 계산한다. `IF (PRESENT(ExtractField)) THEN` (150)이면 Extract_Flag 입력 복사(151), `ELSE` (152)이면 기본 `Extract_Flag=0` (153)이다. Awrk=0 초기화(159). 주석·빈 줄을 포함한다. |
| 161–188 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4)·86행 NetCDF 루틴 안. pack_boundary2d에 격자·변수명·시간·추출 플래그·경계·Nrec·스케일·Abry를 전달하고 start·total·Npts·Awrk를 받는다(165–170). `IF (PRESENT(MinValue)) THEN` (176)의 `IF (OutThread) THEN` (177)에서 MinValue=spval·MaxValue=-spval 초기화(178–179). i=1..Npts 루프(180)의 `IF (ABS(Awrk(i)).lt.spval) THEN` (181)에서 `MinValue=MIN(MinValue,Awrk(i))` (182); `MaxValue=MAX(MaxValue,Awrk(i))` (183)으로 최소·최대를 계산한다. 조건·루프 종료·주석(184–188). |
| 189–209 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4)·86행 NetCDF 루틴 안. status=nf90_noerr 초기화(193). `IF (OutThread) THEN` (194)이면 nf90_put_var 호출(195). `# ifdef DISTRIBUTE` (198) 안에서 mp_bcasti로 status를 전송하고(204) `# endif` (205)로 닫는다. RETURN·함수 종료·빈 줄(207–209). |
| 210–263 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4) 안. `# if defined PIO_LIB && defined DISTRIBUTE` (210)로 PIO 구현을 연다. pio_fwrite2d_bry 함수 시작(213–219), mod_pio_netcdf 사용(222), 입력 인수 선언(226–234). `#  ifdef ASSUMED_SHAPE` (236)이면 assumed-shape Abry(237), `#  else` (238)이면 명시적 4방향·Nrec Abry(239), `#  endif` (240)로 닫는다. 선택적 최소/최대, 파일·변수 기술자(descriptor), 경계 소속·카운터·격자·정밀도·경계·start/total(4)·상태 선언(241–258). 초기값 상수는 `real(r8), parameter :: Aspv = 0.0_r8` (260)이다. Awrk 크기는 `(UBij-LBij+1)*4*Nrec`(262). |
| 264–306 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4)·210행 `# if defined PIO_LIB && defined DISTRIBUTE` (210)·213행 PIO 루틴 안. status=PIO_noerr(268), tile=MyRank, dkind·gtype을 pioVar에서 복사(272–274). `SELECT CASE (gtype)` (276)의 `CASE (p2dvar, p3dvar)` (277)은 Istr/Iend·Jstr/Jend(278–281), `CASE (r2dvar, r3dvar)` (282)은 IstrR/IendR·JstrR/JendR(283–286), `CASE (u2dvar, u3dvar)` (287)은 Istr/IendR·JstrR/JendR(288–291), `CASE (v2dvar, v3dvar)` (292)은 IstrR/IendR·Jstr/JendR(293–296)를 고른다. `CASE DEFAULT` (297) 기본값은 rho 경계(298–301). IorJ 복사(304), `Npts=IorJ*4*Nrec` (305)로 점 수를 계산한다. |
| 307–335 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4)·210행 `# if defined PIO_LIB && defined DISTRIBUTE` (210)·213행 PIO 루틴 안. 타일(tile) Istr/Iend/Jstr/Jend를 복사한다(309–312). 서·동·남·북 경계 소속을 DOMAIN에서 얻는다(316–319). start=[1,1,1,tindex], total=[IorJ,4,Nrec,1]로 설정한다(323–330). 압축(pack)·스케일 구분 주석·빈 줄(332–335). |
| 336–367 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4)·210행 `# if defined PIO_LIB && defined DISTRIBUTE` (210)·213행 PIO 루틴 안. Awrk=Aspv 초기화(336). ir=1..Nrec(338)에서 `rc=(ir-1)*IorJ*4` (339)로 레코드 오프셋(offset)을 계산한다. ib=1..4(340)의 `IF (bounded(ib)) THEN` (341)에서 `bc=(ib-1)*IorJ+rc` (342)로 방향 오프셋을 계산한다. `IF ((ib.eq.iwest).or.(ib.eq.ieast)) THEN` (343)의 j 루프(344)는 `ic=1+(j-LBij)+bc` (345); `Awrk(ic)=Abry(j,ib,ir)*Ascl` (346)으로 인덱스·스케일을 계산한다. `#  ifdef POSITIVE_ZERO` (347)의 `IF (ABS(Awrk(ic)).eq.0.0_r8) THEN` (348)는 양의 0 대입(349), `#  endif` (351)로 닫는다. `ELSE IF ((ib.eq.isouth).or.(ib.eq.inorth)) THEN` (353)의 i 루프(354)는 `ic=1+(i-LBij)+bc` (355); `Awrk(ic)=Abry(i,ib,ir)*Ascl` (356) 계산이다. `#  ifdef POSITIVE_ZERO` (357)의 `IF (ABS(Awrk(ic)).eq.0.0_r8) THEN` (358)는 양의 0 대입(359), `#  endif` (361)로 닫는다. 조건·루프 종료(362–366), 주석(367). |
| 368–397 | 시작 시 4행 `#ifdef ADJUST_BOUNDARY` (4)·210행 `# if defined PIO_LIB && defined DISTRIBUTE` (210)·213행 PIO 루틴 안. mp_collect(ng,model,Npts,Aspv,Awrk) 호출(370). `IF (PRESENT(MinValue)) THEN` (376)에서 MinValue=spval·MaxValue=-spval 초기화(377–378), i=1..Npts 루프(379)의 `IF (ABS(Awrk(i)).lt.spval) THEN` (380)에서 `MinValue=MIN(MinValue,Awrk(i))` (381); `MaxValue=MAX(MaxValue,Awrk(i))` (382)로 최소·최대를 계산한다. PIO_put_var로 버퍼를 쓴다(391). RETURN·함수 종료(393–394), `# endif` (395)로 PIO 조건, `#endif` (396)으로 ADJUST_BOUNDARY 조건을 닫고 모듈 종료(397). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 114–115·176–187 및 241–242·376–385: MinValue·MaxValue는 각각 선택적 출력이다. 두 구현은 PRESENT(MinValue)만 검사하고 MaxValue에도 대입한다.
- 229·264–394: PIO 구현은 선택적 ExtractField를 선언한다. 이후 이 인수를 검사하거나 참조하는 실행문은 없다. NetCDF 구현은 추출 플래그를 pack_boundary2d에 전달한다(150–154·165–170).
- 273·309–312: PIO 구현은 dkind·Istr·Iend·Jstr·Jend를 대입한다. 이후 이 지역 변수들을 참조하는 실행문은 없다.
- 260·336–370·379–384: PIO 버퍼 전체 초기값은 0이다. 타일이 소유한 경계 범위만 값을 채우고 mp_collect를 호출한다. 최소/최대 루프는 ABS(Awrk(i))<spval 조건을 사용하며 0을 제외하는 조건은 없다.
