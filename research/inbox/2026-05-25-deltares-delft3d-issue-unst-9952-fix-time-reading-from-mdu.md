---
title: "Deltares/Delft3D issue: UNST-9952 fix time reading from mdu"
origin: hermes-coastal-research
discovered_date: 2026-05-25
source_url: "https://github.com/Deltares/Delft3D/pull/900"
source_type: github
query: "GitHub API Deltares/Delft3D issues since 2026-05-18; ADCIRC/Delft3D/EFDC/ROMS/SWAN/XBeach"
citation_status: draft-unsourced
promote_candidate: models
---

## 한 줄 요약

GitHub issue/PR updated 2026-05-22: # What was done 

Moved the [time] read block in readMDU up in the routine, behind the geometry block. Some output fields use tstart_user and tstop_user, which was modified by the [time] read after fields  were already set based on the m_flowtimes defaults.
 

# Evidence of the work done 

-

## 왜 coastal-wiki에 유용할 수 있는지

최근 이슈/PR은 모델 사용상 주의점, 빌드/입출력 변경, 버그 가능성을 추적하는 데 유용할 수 있다.

## 관련 모델/개념 키워드

Delft3D, hydrodynamic, morphodynamic model

## 원문 링크

- https://github.com/Deltares/Delft3D/pull/900

## 검색어

`GitHub API Deltares/Delft3D issues since 2026-05-18; ADCIRC/Delft3D/EFDC/ROMS/SWAN/XBeach`

## 주의

아직 검증되지 않은 `draft-unsourced` 자료이다. 검색 노출 기반 후보, 정량 랭킹 아님. 본문 promote 전 원문과 추가 출처를 재확인해야 한다.
