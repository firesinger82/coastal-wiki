---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/fennel_wrt.h
lines: 206
sha256: c437b5c6838206818456f975cedd7219ad38946c7095241f43e9ff333f439dc8
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# fennel_wrt.h — 판독 구간 기록

구간은 1행부터 206행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 저작권·MIT/X 라이선스와 Fennel 생태계(ecosystem) 입력 매개변수를 출력 NetCDF에 쓰는다는 주석(1–13). 주석은 wrt_info.F에서 이 파일을 포함한다고 적음(9–10). 빈 줄·Fortran 도입 주석(14–17). 이 파일 안에는 루틴·루프·전처리 조건의 시작이 없다. 이후 코드는 매개변수 값을 변환하지 않고 해당 격자의 값을 출력 루틴에 전달한다. |
| 18–57 | 정수 BioIter는 `CALL netcdf_put_ivar (ng, model, ncname, 'BioIter',               &` (18); `&                      BioIter(ng), (/0/), (/0/),                  &` (19); `&                      ncid = ncid)` (20)로 씀. 실수 netcdf_put_fvar 호출은 AttSW(23–25), AttChl(28–30), PARfrac(33–35), Vp0(38–40), I_thNH4(43–45), D_p5NH4(48–50), NitriR(53–55)를 같은 이름의 NetCDF 변수에 씀. 모든 호출은 배열 원소 (ng), 위치/개수 인수 (/0/), (/0/), ncid=ncid를 전달함. 각 오류 조건 원문은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (21·26·31·36·41·46·51·56). 빈 줄을 포함함. |
| 58–97 | netcdf_put_fvar는 K_NO3(58–60), K_NH4(63–65), K_PO4(68–70), K_Phy(73–75), Chl2C_m(78–80), ChlMin(83–85), PhyCN(88–90), R_P2N(93–95)를 출력함. 변수 이름 문자열과 원소 이름은 각 호출에서 동일함. 각 호출은 (ng) 원소·(/0/), (/0/)·ncid=ncid를 전달함. 오류 조건 원문은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (61·66·71·76·81·86·91·96). 빈 줄을 포함함. |
| 98–137 | netcdf_put_fvar는 PhyIP(98–100), PhyIS(103–105), PhyMin(108–110), PhyMR(113–115), ZooAE_N(118–120), ZooBM(123–125), ZooCN(128–130), ZooER(133–135)를 출력함. 각 호출은 같은 이름의 (ng) 원소·(/0/), (/0/)·ncid=ncid를 전달함. 오류 조건 원문은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (101·106·111·116·121·126·131·136). 빈 줄을 포함함. |
| 138–182 | netcdf_put_fvar는 ZooGR(138–140), ZooMin(143–145), ZooMR(148–150), LDeRRN(153–155), LDeRRC(158–160), CoagR(163–165), SDeRRN(168–170), SDeRRC(173–175), RDeRRN(178–180)를 출력함. 각 호출은 같은 이름의 (ng) 원소·(/0/), (/0/)·ncid=ncid를 전달함. 오류 조건 원문은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (141·146·151·156·161·166·171·176·181). 빈 줄을 포함함. |
| 183–206 | netcdf_put_fvar는 RDeRRC(183–185), wPhy(188–190), wLDet(193–195), wSDet(198–200), pCO2air(203–205)를 출력함. 각 호출은 같은 이름의 (ng) 원소·(/0/), (/0/)·ncid=ncid를 전달함. 오류 조건 원문은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (186·191·196·201·206). 빈 줄을 포함하며 마지막 행은 pCO2air 오류 검사다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 68–71·93–96·158–161·173–186·203–206: 인산염·탄소·하천 재광물화·대기 CO2 매개변수 쓰기 호출을 감싸는 전처리 조건은 이 파일에 없다.
