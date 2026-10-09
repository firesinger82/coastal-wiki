---
file: models/ADCIRC/raw/source_code/adcirc/docs/user_guide/tips_and_tricks/grid_dev_edit.rst
lines: 88
sha256: bd74b23b1eade9bcba9dc95ce5d5e3fc23bd3aaf9ac12a2e007e0cc7a5c733a1
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# grid_dev_edit.rst — 판독 구간 기록

구간은 1행부터 88행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | Grid Development and Editing — 메타 지시문과 참조 라벨을 포함한다(1–8). ADCIRC 실행에는 fort.14 형태의 격자(mesh)가 필요하다고 적는다(10–11). 격자·데이터 표시는 visualization 문서를 참조한다(12–13). 격자 작성의 복잡성을 고려하여 기존 격자 사용, 기존 격자 수정, 새 격자 작성의 장단점을 신중하게 비교해야 한다고 적는다(14–16). 원문: `` A mesh in the form of a :ref:`fort.14 file <fort14>` is required to run `` (10); ` ADCIRC. This page presents basic info on options available to mesh construction ` (11); ` end editing. For information on viewing meshes or other ADCIRC data, see ` (12); `` :doc:`visualization`. In many cases, a mesh may already exist to `` (13). |
| 18–32 | Tools for ADCIRC Meshing / SMS — SMS는 ADCIRC를 포함한 모델의 생성, 편집, 보기, 실행을 지원하는 상용 Windows 그래픽 프로그램이라고 설명한다(26–27). ADCIRC 파일 형식 지원을 언급하고 Aquaveo와 XMS Wiki 링크를 제시한다(28–31). |
| 33–53 | OceanMesh2D — GNU GPLv3.0으로 공개된 MATLAB 기반 자동 삼각형 격자 생성 소프트웨어라고 설명한다(36–38). ADCIRC 전처리기(pre-processor)로 격자 생성, Courant 제약 검사·편집, fort.13 속성 생성, fort.15와 조석 퍼텐셜(tidal potential)·조석 수위 경계 조건(tidal elevation boundary conditions)의 자동 생성, fort.24 등 다른 입력 생성, msh 클래스(class) 저장, plot 명령으로 표시, ASCII fort.xx 쓰기를 나열한다(40–52). 클래스·명령·파일 형식을 원문대로 옮긴다. 원문: ` -  Generating the mesh. ` (42); ` -  Checking for and editing the mesh to satisfy Courant constraints. ` (43); `` -  Generating :ref:`fort.13 file <fort13>` attributes. `` (44); `` -  Generating :ref:`fort.15 file <fort15>`, including automatic generation of `` (45); `    tidal potential information and tidal elevation boundary conditions. ` (46); `` -  Generating other input files such as :ref:`fort.24 file <fort24>`. `` (47); ``` -  Storing the mesh and its attributes into a ``msh`` class container that can ``` (48); `    be saved as an efficient .mat binary. ` (49); ``` -  Plotting the mesh and its attributes using the generalized ``plot`` command. ``` (50); ``` -  Writing the from the ``msh`` class container into the ASCII fort.xx input ``` (51); `    files. ` (52). |
| 54–77 | References — HTML 원문 지시문(raw directive)과 `<references />`를 포함한다(57–59). 세 각주는 OceanMesh2D V3.0.0 배포, OceanMesh2D 1.0 논문, 2018년 사용자 가이드와 각각의 DOI를 제시한다(61–74). 뒤의 빈 줄도 포함한다(75–77). |
| 78–88 | HTML 스타일 지시문 — wrap-table의 제목 셀과 본문 셀에 공백 처리, 단어 줄바꿈, 최대 폭, 넘침 줄바꿈, 자동 하이픈을 설정하는 CSS를 포함한다(78–88). 이 값은 모델 매개변수가 아니라 문서 표시 설정이다. 원문: ` .. raw:: html ` (78); `    <style> ` (80); `    .wrap-table th, .wrap-table td { ` (81); `      white-space: normal !important; ` (82); `      word-wrap: break-word !important; ` (83); `      max-width: 100% !important; ` (84); `      overflow-wrap: break-word !important; ` (85); `      hyphens: auto !important; ` (86); `    } ` (87); `    </style> ` (88). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
