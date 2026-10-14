# ROMS 노트 반영 기록 — 작업 5 (2026-10-14)

배정표는 [note-job-5.tsv](../assign/note-job-5.tsv)이다.
보고서 끝의 `전수 검증 기록 (10-14)`을 최종 결론으로 적용한다.
쓰기 대상은 지정된 노트 세 파일과 이 기록 파일이다.

## 파일별 반영 결과

### cppdefs 차이 노트

- 파일: [roms-wiki-cppdefs-options-differences-1.md](../../../models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-1.md:1).
- 추가 범위: `models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-1.md:1–225`.
- 배정표에서 이 파일에 배정한 199행을 넣었다.
- 결론별 수량은 배정표와 추가 표에서 각각 A 152행, B 39행, C 4행, D 1행, F 3행이다.
- 표 행 ID는 배정표와 같다.
- A 행의 결론 문장에 git 판정 커밋 HASH와 날짜를 적었다.
- RB-016의 커밋 날짜는 [A6 판정](../compare/ROMS-git-verify-A6.md)의 `a4d1e9de` (2020-09-28)를 반영했다.
- 이 파일에는 기존 노트 수정안의 별도 반영 대상이 없다.
- 넣지 않은 배정 행은 없다.

### Representer 노트

- 파일: [roms_representer_model.md](../../../models/ROMS/source-analysis/roms_representer_model.md:7).
- 수정 범위: `models/ROMS/source-analysis/roms_representer_model.md:7–8`, `:22`, `:72–76`, `:113–116`, `:148–166`, `:199`, `:209–211`, `:217–233`.
- 차이 절 추가 범위: `models/ROMS/source-analysis/roms_representer_model.md:235–246`.
- 배정표에서 이 파일에 배정한 C 4행을 넣었다.
- 추가 행 ID는 `da-representer:RT2-366`, `da-representer:RT2-390`, `da-representer:RT2-391`, `theory-numerics:RTN-388`이다.
- 수정안 반영 ID는 `theory-numerics:RTN-384`, `theory-numerics:RTN-388`, `da-representer:RT2-390`, `da-representer:RT2-391`, `callflow-da:RF2-032`이다.
- `da-4dvar:DA1-813`의 전체장 방정식과 Picard 설명을 유지했다.
- `inputs:RI1-1060`의 초기시각 설명을 유지했다.
- callflow-da §6.3의 RPM impulse 행은 R4 분석 RPM 범위라는 조건을 반영했다.
- RPM 변수 설명에 `da-representer:RT2-366`의 전체장 결론을 반영했다.
- 최소화기 호출과 `zgrad0`·`cg_beta`·`px`의 생산·소비 위치를 연결했다.
- 넣지 않은 배정 행과 수정안 행은 없다.

### NetCDF 노트

- 파일: [roms_io_netcdf.md](../../../models/ROMS/source-analysis/roms_io_netcdf.md:7).
- 수정 범위: `models/ROMS/source-analysis/roms_io_netcdf.md:7–8`, `:21–25`, `:37–49`, `:80–83`, `:105–110`, `:153`, `:163–185`, `:205–207`, `:212–215`, `:225–230`, `:236–253`.
- 차이 절 추가 범위: `models/ROMS/source-analysis/roms_io_netcdf.md:254–257`.
- 이 파일에 직접 넣는 배정 표 행은 0개다.
- 사용자 지시에 따라 [차이 파일](../../../models/ROMS/source-analysis/roms_io_netcdf-differences.md) 링크를 넣었다.
- 전체 `ROMS-assign-*.tsv`의 3열이 `source-analysis/roms_io_netcdf.md`인 237행을 집계했다.
- 집계 결과는 A 37행, B 85행, C 67행, D 27행, E 5행, F 16행이다.
- 수정안 반영 ID는 `coupling-nesting-parallel:RCN-1959`, `coupling-nesting-parallel:RCN-1984`, `inputs:RI1-1042`, `inputs:RI1-1043`, `inputs:RI1-1044`, `build-options-history:RBH-3504`, `build-options-history:RBH-3505`이다.
- outputs-metadata 수정안 반영 ID는 `OMD-N016`, `OMD-N017`, `OMD-N018`, `OMD-N021`, `OMD-N022`, `OMD-N023`이다.
- `outputs-metadata:OMD-N019`와 `outputs-metadata:OMD-N020`의 절 제목을 유지했다.
- `da-4dvar:DA1-817`과 `callflow-da:RF2-025`의 DAI 수정을 반영했다.
- `da-4dvar:DA1-818`의 상세 구조 `source-needed` 표기를 유지했다.
- 같은 수정안에 따라 정규화 파일의 생성·조회 조건과 LCZ의 추가 마지막 레코드를 연결했다.
- `sediment-ice-vegetation:RN1-044`, `biology:NT-023`, `inputs:RI1-1045`, `tools-guides:RTG-1981`의 텍스트 입력 역할 설명을 유지했다.
- 넣지 않은 수정안 행은 없다.

## 완료 확인

- `note-job-5.tsv`의 203행을 지정 파일의 표에 모두 넣었다.
- 새 cppdefs 차이 노트의 199행과 Representer 노트의 4행을 합산한 값이다.
- 행 ID와 배정 파일의 대조에서 누락·추가·중복은 없다.
- 표의 결론 문장 203개를 보고서의 최종 결론 문장과 대조했다.
- A 152행의 결론 문장에는 커밋 HASH와 날짜가 모두 있다.
- 두 노트의 수정안 반영 행과 유지 행을 파일별 기록에 적었다.
- NetCDF의 결론별 개수는 전체 배정표에서 센 237행과 같다.
- 노트 세 파일의 frontmatter와 배정 표의 6열 형식을 검사했다.
- 노트 세 파일의 상대 링크 68개가 연결된다.
- 노트와 이 기록에는 사용자 홈 절대 경로와 위키 링크 구문 문자열이 없다.
- 변경한 기존 노트 두 파일은 `git diff --check`를 통과했다.
- 넣지 않은 배정 행과 수정안 행은 없다.
