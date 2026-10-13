---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/ecosim_wrt.h
lines: 469
sha256: b041fa5aae8460a6159b67f64b1f7e24da8ac549fa73abe1c1288ccec66a6a2b
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ecosim_wrt.h — 판독 구간 기록

구간은 1행부터 469행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–50 | 파일 내부에서 열린 바깥 블록·전처리 조건 없음. 저작권·MIT/X·EcoSim 생물광학(bio-optical) 입력 매개변수(parameter)를 NetCDF에 쓰고 wrt_info.F에 포함된다는 C 주석(1–13), 빈 줄·Fortran 주석(14–17). netcdf_put_ivar로 BioIter(ng)를 쓰고 netcdf_put_lvar로 RtUVR_flag·NFIX_flag·Regen_flag(ng)를 쓴다(18–20·23–25·28–30·33–35). 스칼라(scalar) 시작·개수 인수는 (/0/)·(/0/)이며 모든 호출에 ng·model·ncname·ncid=ncid를 전달한다. 각 호출 뒤 오류 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (21·26·31·36). `IF (ncid.ne.DIA(ng)%ncid) THEN` (38)이면 netcdf_put_fvar로 light에 ec_wave_ab를 시작 (/1/)·개수 (/NBands/)로 쓴다(39–41). `#ifdef DIAGNOSTICS_BIO` (42) 안 `ELSE` (43)이면 dia_light를 시작 (/1/)·개수 (/NDbands/)로 쓴다(44–46). `#endif` (47)·IF 종료(48) 뒤 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (49). 빈 줄(50). |
| 51–95 | 파일 내부에서 열린 바깥 블록·전처리 조건 없음. netcdf_put_fvar는 HsNO3·HsNH4·HsSiO·HsPO4·HsFe·GtALG_max·PhyTbase·PhyTfac·BET_를 같은 NetCDF 변수 이름으로 쓴다(51–53·56–58·61–63·66–68·71–73·76–78·81–83·86–88·91–93). 각 인수는 해당 배열의 (:,ng), 시작 (/1/)·개수 (/Nphy/), ncid=ncid이다. 각 호출 뒤 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (54·59·64·69·74·79·84·89·94)이면 RETURN한다. 빈 줄도 포함한다. |
| 96–155 | 파일 내부에서 열린 바깥 블록·전처리 조건 없음. netcdf_put_fvar로 maxC2nALG·minC2nALG·C2nALGminABS·maxC2SiALG·minC2SiALG·C2SiALGminABS·maxC2pALG·minC2pALG·C2pALGminABS·maxC2FeALG·minC2FeALG·C2FeALGminABS를 쓴다(96–153의 각 3행 호출). 각 값은 (:,ng), 시작 (/1/)·개수 (/Nphy/), ncid=ncid이다. 호출 뒤 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (99·104·109·114·119·124·129·134·139·144·149·154)이면 RETURN한다. 마지막 빈 줄(155). |
| 156–200 | 파일 내부에서 열린 바깥 블록·전처리 조건 없음. netcdf_put_fvar로 qu_yld·E0_comp·E0_inhib·inhib_fac·C2CHL_max·mxC2Cl·b_C2Cl·mxC2Cn·b_C2Cn을 쓴다(156–158·161–163·166–168·171–173·176–178·181–183·186–188·191–193·196–198). 각 값은 (:,ng), 시작 (/1/)·개수 (/Nphy/), ncid=ncid이다. 호출 뒤 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (159·164·169·174·179·184·189·194·199)이면 RETURN한다. 마지막 빈 줄(200). |
| 201–240 | 파일 내부에서 열린 바깥 블록·전처리 조건 없음. netcdf_put_fvar로 mxPacEff·b_PacEff·mxChlB·b_ChlB·mxChlC·b_ChlC·mxPSC·b_PSC를 쓴다(201–203·206–208·211–213·216–218·221–223·226–228·231–233·236–238). 각 값은 (:,ng), 시작 (/1/)·개수 (/Nphy/), ncid=ncid이다. 호출 뒤 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (204·209·214·219·224·229·234·239)이면 RETURN한다. 마지막 빈 줄(240). |
| 241–270 | 파일 내부에서 열린 바깥 블록·전처리 조건 없음. netcdf_put_fvar로 mxPPC·b_PPC·mxLPUb·b_LPUb·mxHPUb·b_HPUb를 쓴다(241–243·246–248·251–253·256–258·261–263·266–268). 각 값은 (:,ng), 시작 (/1/)·개수 (/Nphy/), ncid=ncid이다. 호출 뒤 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (244·249·254·259·264·269)이면 RETURN한다. 마지막 빈 줄(270). |
| 271–300 | 파일 내부에서 열린 바깥 블록·전처리 조건 없음. netcdf_put_fvar로 FecDOC·FecPEL·FecCYC·ExALG·WS·HsGRZ를 쓴다(271–273·276–278·281–283·286–288·291–293·296–298). FecPEL의 인수는 FecPEL(:,:,ng), 시작 (/1,1/)·개수 (/Nphy,Nfec/)이며 나머지는 (:,ng), 시작 (/1/)·개수 (/Nphy/)이다. 모두 ncid=ncid를 전달한다. 호출 뒤 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (274·279·284·289·294·299)이면 RETURN한다. 마지막 빈 줄(300). |
| 301–340 | 파일 내부에서 열린 바깥 블록·전처리 조건 없음. netcdf_put_fvar로 MinRefuge·RefugeDep·Norm_Vol·Norm_Surf·HsDOP·C2pALKPHOS·HsDON·C2nNupDON을 쓴다(301–303·306–308·311–313·316–318·321–323·326–328·331–333·336–338). 각 값은 (:,ng), 시작 (/1/)·개수 (/Nphy/), ncid=ncid이다. 호출 뒤 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (304·309·314·319·324·329·334·339)이면 RETURN한다. 마지막 빈 줄(340). |
| 341–360 | 파일 내부에서 열린 바깥 블록·전처리 조건 없음. netcdf_put_fvar로 HsDOC_ba·GtBAC_max·BacTbase·BacTfac를 쓴다(341–343·346–348·351–353·356–358). 각 값은 (:,ng), 시작 (/1/)·개수 (/Nbac/), ncid=ncid이다. 호출 뒤 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (344·349·354·359)이면 RETURN한다. 마지막 빈 줄(360). |
| 361–400 | 파일 내부에서 열린 바깥 블록·전처리 조건 없음. netcdf_put_fvar로 C2nBAC·C2pBAC·C2FeBAC·BacDOC·BacPEL·BacCYC·ExBAC_c·ExBacC2N의 격자별 스칼라 (ng)를 쓴다(361–363·366–368·371–373·376–378·381–383·386–388·391–393·396–398). 시작·개수는 (/0/)·(/0/), ncid=ncid이다. 호출 뒤 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (364·369·374·379·384·389·394·399)이면 RETURN한다. 마지막 빈 줄(400). |
| 401–430 | 파일 내부에서 열린 바깥 블록·전처리 조건 없음. netcdf_put_fvar로 Bac_Ceff·RtNIT·HsNIT의 (ng) 값을 시작 (/0/)·개수 (/0/)로 쓴다(401–403·406–408·411–413). cDOCfrac_c(:,ng)는 시작 (/1/)·개수 (/Ndom/)로 쓴다(416–418). RtUVR_DIC(ng)는 이름 RtUVR_DIC로 쓴다(421–423). 이름 RtUVR_DOC에 전달하는 값도 RtUVR_DIC(ng)이며 해당 호출 원문은 `CALL netcdf_put_fvar (ng, model, ncname, 'RtUVR_DOC',             &` (426); `&                      RtUVR_DIC(ng), (/0/), (/0/),                &` (427); `&                      ncid = ncid)` (428)이다. 각 호출은 ncid=ncid를 전달한다. 호출 뒤 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (404·409·414·419·424·429)이면 RETURN한다. 마지막 빈 줄(430). |
| 431–469 | 파일 내부에서 열린 바깥 블록·전처리 조건 없음. netcdf_put_fvar로 WF·RegTbase·RegTfac·RegCR·RegNR·RegSR·RegPR·RegFR를 같은 변수 이름으로 쓴다(431–433·436–438·441–443·446–448·451–453·456–458·461–463·466–468). 각 값은 (:,ng), 시작 (/1/)·개수 (/Nfec/), ncid=ncid이다. 각 호출 뒤 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (434·439·444·449·454·459·464·469)이면 RETURN한다. 이 파일은 마지막 오류 조건에서 끝나며 외부 루틴 종료문은 포함하지 않는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 421–428: NetCDF 이름 RtUVR_DIC와 RtUVR_DOC에 두 호출 모두 RtUVR_DIC(ng)를 전달한다. RtUVR_DOC(ng)를 전달하는 호출은 이 파일에 없다.
- 38–49: ncid가 DIA(ng)%ncid와 같은 경우 light를 쓰는 ELSE 블록은 DIAGNOSTICS_BIO 안에만 있다. 이 전처리 조건이 제외되면 해당 ncid에서 light를 쓰는 호출이 이 블록에 남지 않는다.
