# 전수 판독 코퍼스 provenance (2026-07-21)

기계 산출은 [`PROVENANCE.json`](PROVENANCE.json) — 모델별 파일수·Merkle 루트(전 파일 `경로:sha256` 연쇄 해시)·git repo 메타·최신 mtime. 코퍼스가 바뀌면 Merkle 루트가 바뀌므로 "이 판독이 어느 스냅샷 기준인가"를 이 값으로 특정한다.

## 취득 방식

**git clone (10 모델)** — 모델별로 **여러 저장소**가 `raw/source_code/` 아래 병렬 배치. 전부 커밋 고정.

| 모델 | repo 수 | 구성 |
|---|---:|---|
| ADCIRC | 7 | `adcirc`(본체 1,313) · `asgs`(운영 4,580) · `adcirc-testsuite`(837) · `gahm`(292) · `StormEvents`(186) · `adcircpy`(154) · `FigureGen`(39) |
| ROMS | 7 | `roms`(본체 1,224) · **`WRF`(4,744 — 별개 대기모델)** · `roms_test`(1,051) · `roms_matlab`(801) · `roms_libs`(675) · `roms-jedi`(397) · `roms_eccofs`(57) |
| Delft3D | 3 | `Delft3D`(본체 30,755) · `hydromt_delft3dfm`(200) · `Delft-FIAT`(163) |
| EFDC | 2 | `EFDCPlus_Stable`(381) · `EFDC-GVC`(313, legacy) |
| FUNWAVE | 2 | ⚠ `dirty:5` — GPU(Blackwell cuSPARSE v2) 포팅 로컬 수정 잔존 |
| CADMAS-SURF·Celeris·SWAN·SWASH·ShorelineS | 각 1 | — |

**스냅샷 (3 모델)** — git 부재는 결함이 아니라 **배포 방식 자체가 git이 아니기 때문**:

| 모델 | 버전 | 근거 | 배포 |
|---|---|---|---|
| **LISFLOOD-FP** | **v8.2** (2024-07-29) | 위키 README + Zenodo 메타(GPL-2.0·348 MB) | Zenodo `doi:10.5281/zenodo.13121102` — 공식 GitHub 단일 repo 미확인 |
| **SFINCS** | **v2.4.0 Galibier** (2026.01 release) | `docs/developments.rst:32,35` | Deltares 릴리스 |
| **XBeach** | SVN **r5583** (`trunk`) | `configure.ac:3` `$Revision: 5583 $` | Deltares **SVN** (git 아님) |

## ★ 판독 중 발견: 소스 내 버전 선언이 stale

**LISFLOOD-FP `VersionHistory.h:16-19` 는 `8.1.0` 을 선언하지만 실제 코퍼스는 v8.2.**
- 그 파일의 이력이 **2020-07 `8.0.1` 에서 끊김**
- 반면 8.x 핵심 기능은 전부 실재: `cuda/`(GPU) · `swe/`(FV1·DG2 완전 2D shallow-water) · `lisflood2/` · `cuda/acc_nugrid`(multiwavelet 동적 해상도 적응)
- 원인 추정: Bristol(Bates) SVN 시절 관행이 Sheffield(Kesserwani) 주도 8.x 로 넘어오며 미갱신
- **함의: 소스 내 버전 문자열을 신뢰하면 오판한다.** 실제로 본 판독 중 1차로 8.1.0 으로 잘못 읽었고, 사용자 지적으로 정정.

## 미확정 사항 (disclosed)

- 로컬 코퍼스가 **upstream 전량인지는 미검증**. 본 매니페스트는 "로컬에 있는 것"을 고정할 뿐, "받을 때 빠진 것"은 다루지 못한다. → upstream 대조는 판독 완료 후 별도 단계(공식 배포본 재취득 후 파일목록·해시 비교).
- ROMS 클론 내 **WRF 4,744 파일**은 별개 대기모델이나 분모에 포함(전수 원칙).
- Delft3D 31,087 중 third-party·빌드 산출물 비중 미분류 — 전수 원칙에 따라 전부 판독 대상.
