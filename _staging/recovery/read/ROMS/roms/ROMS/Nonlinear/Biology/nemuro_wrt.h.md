---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/nemuro_wrt.h
lines: 431
sha256: 40515af195aad4338ab15b33c63e464830a1354a9898f7c68fda5d37f6d74aee
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# nemuro_wrt.h — 판독 구간 기록

구간은 1행부터 431행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 저작권·MIT/X 사용허가·License_ROMS.md 안내(1–7). NEMURO 생태계(ecosystem) 입력 매개변수를 NetCDF 출력 파일에 쓰며 `wrt_info.F`에 삽입된다는 주석(9–10). C 주석 종료·빈 줄·Fortran 작업 설명 주석(13–17). 이 파일 자체에는 루틴 선언이 없다. |
| 18–72 | `netcdf_put_ivar`로 BioIter(ng)를 BioIter에 기록(18–20). `netcdf_put_fvar`로 AttSW·AttPS·AttPL·PARfrac·AlphaPS·AlphaPL·BetaPS·BetaPL·VmaxS·VmaxL의 ng 원소를 동명 변수에 기록(23–25·28–30·33–35·38–40·43–45·48–50·53–55·58–60·63–65·68–70). 모든 호출은 시작·개수 `(/0/)`와 `ncid = ncid`를 전달한다. 각 호출 다음 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (21·26·31·36·41·46·51·56·61·66·71)이다. 오류를 발견하면 포함한 루틴에서 반환한다. |
| 73–137 | `netcdf_put_fvar`로 KNO3S/KNO3L/KNH4S/KNH4L/KSiL을 출력 이름 K_NO3S/K_NO3L/K_NH4S/K_NH4L/K_SiL에 기록(73–95). 이어 PusaiS·PusaiL·KGppS·KGppL·ResPS0·ResPL0·KResPS·KResPL의 ng 원소를 동명 변수에 기록(98–135). 매 호출의 시작·개수는 `(/0/)`이고 ncid를 지정한다. 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (76·81·86·91·96·101·106·111·116·121·126·131·136)이다. 마지막 빈 줄도 포함(137). |
| 138–202 | `netcdf_put_fvar`로 GammaS·GammaL·MorPS0·MorPL0·KMorPS·KMorPL·GRmaxSps·GRmaxLps·GRmaxLpl·GRmaxLzs·GRmaxPpl·GRmaxPzs·GRmaxPzl의 ng 원소를 동명 변수에 기록(138–200). 시작·개수 `(/0/)`와 ncid를 전달한다. 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (141·146·151·156·161·166·171·176·181·186·191·196·201)이다. |
| 203–232 | `netcdf_put_fvar`로 KGraS·KGraL·KGraP·LamS·LamL·LamP의 ng 원소를 동명 변수에 기록(203–230). 시작·개수 `(/0/)`와 ncid를 전달한다. 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (206·211·216·221·226·231)이다. |
| 233–268 | `#ifdef HOLLING_GRAZING` (233)으로 Holling 섭식(grazing) 분기를 연다. `netcdf_put_fvar`로 KPS2ZS·KPS2ZL·KPL2ZL·KZS2ZL·KPL2ZP·KZS2ZP·KZL2ZP의 ng 원소를 출력 이름 K_PS2ZS·K_PS2ZL·K_PL2ZL·K_ZS2ZL·K_PL2ZP·K_ZS2ZP·K_ZL2ZP에 기록(234–266). 시작·개수 `(/0/)`와 ncid를 전달한다. 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (237·242·247·252·257·262·267)이다. |
| 269–306 | 시작 시 233행 `#ifdef HOLLING_GRAZING` 안. `#else` (269)는 HOLLING_GRAZING 미정의 분기이다. `netcdf_put_fvar`로 PS2ZSstar·PS2ZLstar·PL2ZLstar·PL2ZLstar·PL2ZPstar·ZS2ZPstar·ZL2ZPstar를 이 순서로 동명 변수에 기록(271–303). PL2ZLstar 호출은 281–283행과 286–288행에 반복된다. 시작·개수 `(/0/)`와 ncid를 전달한다. 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (274·279·284·289·294·299·304)이다. `#endif` (305)로 전처리 분기를 닫고 빈 줄을 포함한다(306). |
| 307–361 | 전처리 분기 밖에서 `netcdf_put_fvar`로 PusaiPL·PusaiZS·MorZS0·MorZL0·MorZP0·AlphaZS·AlphaZL·AlphaZP·BetaZS·BetaZL·BetaZP의 ng 원소를 동명 변수에 기록(307–359). 시작·개수 `(/0/)`와 ncid를 전달한다. 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (310·315·320·325·330·335·340·345·350·355·360)이다. |
| 362–396 | `netcdf_put_fvar`로 Nit0·VP2N0·VP2D0·VD2N0·VO2S0·KNit·KNit의 ng 원소를 이 순서로 동명 변수에 기록(362–394). KNit 호출은 387–389행과 392–394행에 반복된다. 시작·개수 `(/0/)`와 ncid를 전달한다. 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (365·370·375·380·385·390·395)이다. |
| 397–431 | `netcdf_put_fvar`로 KP2D·KP2N·KD2N·KO2S·RSiN·setVPON·setVOpal의 ng 원소를 동명 변수에 기록(397–429). 시작·개수 `(/0/)`와 ncid를 전달한다. 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (400·405·410·415·420·425·430)이다. 마지막 빈 줄을 포함한다(431). 이 파일은 출력만 수행하며 매개변수 기본값이나 물리식 계산을 설정하지 않는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 281–289: HOLLING_GRAZING 미정의 분기에서 PL2ZLstar(ng)를 'PL2ZLstar'에 쓰는 동일한 호출이 연속 두 번 있다.
- 387–395: KNit(ng)를 'KNit'에 쓰는 동일한 호출이 연속 두 번 있다.
