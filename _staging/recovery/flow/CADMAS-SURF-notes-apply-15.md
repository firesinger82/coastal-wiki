---
title: "CADMAS-SURF 노트 반영 — 배정 15"
canonical_source: self
citation_status: verified
note_author: "Codex"
note_date: 2026-11-04
last_source_check: "2026-11-04 (recovery 대조 반영)"
verification_method: "2026-11-04 CADMAS-SURF recovery 대조 보고서 반영. 배정표 행 ID·분류·파일별 행 수와 최종 근거를 대조."
---

# CADMAS-SURF 노트 반영 — 배정 15

배정표는 [CADMAS-SURF-note-job-15.tsv](../assign/CADMAS-SURF-note-job-15.tsv)이다.
표의 결론은 각 conclusion-verify 파일의 같은 행 ID를 따른다.
노트 경로의 기준은 models/CADMAS-SURF/이다.

### manual-notes/cadmas-agent-manual.md

- 추가·수정: models/CADMAS-SURF/manual-notes/cadmas-agent-manual.md:2–69 (frontmatter·본문).
- 표 추가: models/CADMAS-SURF/manual-notes/cadmas-agent-manual.md:71–119.
- 표 반영: 41행 / 배정표 41행.
- 수정안 반영: agent:KA1-502·503·504(유지)·505·506·507·508(최종 F 적용)·509·510·511·512·513·514·515·516.
- 넣지 않은 배정 행: 없음.

### source-analysis/cadmas-2f-twophase-compressible-gas.md

- 추가·수정: models/CADMAS-SURF/source-analysis/cadmas-2f-twophase-compressible-gas.md:6–93 (frontmatter·본문·매개변수 표).
- 표 추가: models/CADMAS-SURF/source-analysis/cadmas-2f-twophase-compressible-gas.md:95–138.
- 표 반영: 36행 / 배정표 36행.
- 수정안 반영: 2f-theory의 반영 전 노트 22·30·39·43·45·58–64·68·74행 수정안(KF1-012·018·111·201·202·203·204·207·219); 2f-input:KF3-196; 2f-program:KF2-002·003·007(순서 유지)·027·328·342·360; tutorials-build:KU1-222·800·801·802·807·808·810·811; 3d2f-vs-3d:KD1-893·894·895·896·897·898.
- 넣지 않은 배정 행: 없음.

### source-analysis/cadmas-2f-structure-coupling-cutcell.md

- 추가·수정: models/CADMAS-SURF/source-analysis/cadmas-2f-structure-coupling-cutcell.md:6–69 (frontmatter·본문).
- 표 추가: models/CADMAS-SURF/source-analysis/cadmas-2f-structure-coupling-cutcell.md:71–113.
- 표 반영: 35행 / 배정표 35행.
- 수정안 반영: 2f-program:KF2-351·358(기존 구조 설명 유지·자료 구조 누락 보충); callflow:RF-010·011; str-theory:KT1-856·857·858; 3d2f-vs-3d:KD1-900·901·902·903.
- 넣지 않은 배정 행: 없음.

### source-analysis/cadmas-surf3d-timestep-nesting-stoc-coupling.md

- 추가·수정: models/CADMAS-SURF/source-analysis/cadmas-surf3d-timestep-nesting-stoc-coupling.md:6–74 (frontmatter·CFL·환경 파일·STOC).
- 표 추가: models/CADMAS-SURF/source-analysis/cadmas-surf3d-timestep-nesting-stoc-coupling.md:76–109.
- 표 반영: 26행 / 배정표 26행.
- 수정안 반영: 3d-theory:KS1-720; 3d-input:KS3-406; 2f-program:KF2-020·022·023·349·357; callflow:RF-009·020(수신 뒤 경계 재적용 문장은 유지); tutorials-build:KU1-063·069·075·076·814; 3d2f-vs-3d:KD1-908(3D 설명 유지·3D2F 설명 보충).
- callflow의 Claude 렌더 확인 (11-04)은 그림 정정이 없다고 기록한다.
- 넣지 않은 배정 행: 없음.

### manual-notes/cadmas-2f-manual-compressibility.md

- 기존 정정 대조: models/CADMAS-SURF/manual-notes/cadmas-2f-manual-compressibility.md:2–73의 frontmatter·본문 정정은 작업 시작 때 이미 반영되어 있었다.
- 표 추가: models/CADMAS-SURF/manual-notes/cadmas-2f-manual-compressibility.md:81–109.
- 표 반영: 21행 / 배정표 21행.
- 수정안 반영: 2f-theory의 반영 전 노트 18·26·28·30·31·32·33·40·41·44·48·52행 수정안; 2f-program:KF2-002·003·005·007·097·114·343·359·360; 2f-input:KF3-190; tutorials-build:KU1-951; 3d2f-vs-3d:KD1-910·911.
- 넣지 않은 배정 행: 없음.

## 최종 대조

배정표의 159행을 지정 노트에 반영했다.
파일별 행 수는 배정표의 41·36·35·26·21행과 같다.
표에 배정 외 행과 중복 행이 없다.
상대 링크·금지 경로 문자열·표의 여섯 칸·frontmatter를 점검했다.
Markdown 렌더러는 다섯 대조 표를 각각 41·36·35·26·21행으로 처리했다.
각 표 행은 여섯 칸으로 렌더됐다.
git diff --check가 통과했다.
