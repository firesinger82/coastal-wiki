# LISFLOOD-FP Acquisition Manifest

**Acquired**: 2026-06-18

## source_code/

| Source | Version | Format | Size |
|--------|---------|--------|------|
| Zenodo **doi:10.5281/zenodo.13121102** | **v8.2** (2024-07-29) | LISFLOOD-FP-v8.2.zip (348 MB, 3170 files) | ~810M (raw extracted, gitignored) |

- 다운로드: `curl -L https://zenodo.org/api/records/13121102/files/LISFLOOD-FP-v8.2.zip/content` (resume `-C -` 필요 — 1차 162MB 절단 후 이어받음).
- 압축해제: `python3 -m zipfile -e` (unzip 미설치). 추출 후 nested `.git` 제거.
- C++/CUDA. 코어: root `*.cpp`(classic FP: acc/flow/trent/sgc) + `swe/`(FV1/DG2/HLL) + `cuda/`(GPU).
- raw/ 는 `.gitignore` 제외(vendor source tree).
- 공식 GitHub 단일 repo 미확인 → **Zenodo 가 v8.2 정본**. Bristol(원조)·SEAMLESS-WAVE/U.Sheffield(v8.x).

## 라이선스

- GNU GPL-2.0 (Zenodo 메타데이터; repo LICENSE 파일 본문 부재).
