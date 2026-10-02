---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_boundary_datastore.f90
lines: 78
sha256: 189a137244043330e3b3a33bd8ea3d0b8d015e5c0e863c7f93492fafab5c77a2
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# wave_boundary_datastore.f90 — 판독 구간 기록

구간은 1행부터 78행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `wave_boundary_datastore` 모듈(1), 경계조건 정보를 네 종류의 파생형에 저장하고 main/init/update에서 접근한다는 주석(2–10). implicit none·save(11–12), 형 정의 머리말과 빈 줄. |
| 16–32 | `waveBoundaryParametersType`: masterFileName(1024), np·ntheta, x0·y0·hboundary, nonhspectrum, sprdthr·trepfac, Tm01switch, allocatable xb·yb·theta, 정수 scalar randomseed·nspr, rho·nmax·fcutoff(17–29). 이 형에는 기본값·범위 검사·계산식이 없다. |
| 33–41 | spectral 파일 정보 `filenames` 형(35): fname(1024), FILELIST 위치 listline, `logical                                :: repeat = .false.`(38). 반복은 rtbc cycle 기준이라는 주석. |
| 42–49 | `waveBoundaryAdministrationType`(43): `logical                                 :: initialized = .false.`(44); 새 시계열 계산 시작 시각 startComputeNewSeries와 현재 시계열 시작 시각 startCurrentSeries, 단위 s(45–46). 시각의 초기값은 선언에 없다. |
| 50–62 | `waveSpectrumAdministrationType`(51): nspectra, allocatable bcfiles, repeatwbc, bccount, spectrumendtime, allocatable lastwaveelevation(:,:)·xspec(:)·yspec(:), 대표 Hbc·Tbc·Dbc(52–59). nspectra와 bccount는 init spectrum에서 설정한다는 주석. 이 형 선언에는 기본값이 없다. |
| 63–71 | `waveBoundaryTimeSeriesType`(64): allocatable eebct(:,:,:), qxbct/qybct(:,:), zsbct/ubct/vbct/wbct(:,:), tbc(:)(65–68). 선언만 있고 할당·계산·호출은 없다. |
| 72–78 | 위 네 파생형의 모듈 변수 waveBoundaryParameters·waveBoundaryAdministration·waveBoundaryTimeSeries·waveSpectrumAdministration 선언(73–76), 모듈 종료(78). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
