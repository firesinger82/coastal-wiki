---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/ecb_wrt_pio.h
lines: 253
sha256: 95a20471df627305263fa4ac61f94f7c9316f9a54a8ddf39159f4e8c92decd04
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ecb_wrt_pio.h — 판독 구간 기록

구간은 1행부터 253행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | 저작권·MIT/X 사용권·License_ROMS.md 안내(1–14), 빈 줄·설정 출력 주석(15–19). 하구 탄소 생지화학(Estuarine Carbon Biogeochemistry) 모델의 매개변수를 병렬 입출력(Parallel I/O, PIO) 라이브러리로 NetCDF 파일에 기록하며 wrt_info.F에 포함된다는 머리말(9–11). 이 파일에는 루틴 선언과 전처리 지시문이 없다. |
| 20–78 | 전처리 조건과 파일 내부의 바깥 조건·루프 없음. `pio_netcdf_put_ivar`가 BioIter(ng)를 'BioIter'로 기록(20–22). `pio_netcdf_put_fvar`가 AttSW·AttChl·PARfrac·Vp0·I_thNH4·D_p5NH4·NitriR·K_NO3·K_NH4·K_PO4·K_Phy의 (ng) 값을 같은 이름으로 기록(25–77). 모든 호출의 시작·개수 인수는 `(/0/), (/0/)`이고 pioFile을 지정한다. 각 호출 직후 원문 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (23·28·33·38·43·48·53·58·63·68·73·78)이며 오류이면 즉시 반환한다. |
| 79–153 | 전처리 조건과 파일 내부의 바깥 조건·루프 없음. 빈 줄을 포함하여 Chl2C_m·ChlMin·PhyCN·R_P2N·PhyIP·PhyIS·PhyMin·PhyMR·ZooAE_N·ZooBM·ZooCN·ZooER·ZooGR·ZooMin·ZooMR의 (ng) 값을 `pio_netcdf_put_fvar`로 같은 이름에 기록(80–152). 시작·개수 인수는 `(/0/), (/0/)`이고 pioFile을 지정한다. 원문 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (83·88·93·98·103·108·113·118·123·128·133·138·143·148·153). |
| 154–218 | 전처리 조건과 파일 내부의 바깥 조건·루프 없음. LDeRRN·LDeRRC·CoagR·SDeRRN·SDeRRC·RDeRRN·RDeRRC·wPhy·wLDet·wSDet·rkd1·rkdTSS1·rkdS1의 (ng) 값을 `pio_netcdf_put_fvar`로 같은 이름에 기록(155–217). 시작·개수 인수는 `(/0/), (/0/)`이고 pioFile을 지정한다. 원문 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (158·163·168·173·178·183·188·193·198·203·208·213·218). |
| 219–253 | 전처리 조건과 파일 내부의 바깥 조건·루프 없음. 빈 줄을 포함하여 ElDON·EsDON·deltN·deltC·gammaC·slCexc·pCO2air의 (ng) 값을 `pio_netcdf_put_fvar`로 같은 이름에 기록(220–252). 시작·개수 인수는 `(/0/), (/0/)`이고 pioFile을 지정한다. 원문 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (223·228·233·238·243·248·253)。이 구간에는 매개변수 계산이나 기본값 설정이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
