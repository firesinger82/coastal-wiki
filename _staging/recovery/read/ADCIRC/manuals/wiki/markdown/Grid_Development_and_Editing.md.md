---
file: models/ADCIRC/raw/manuals/wiki/markdown/Grid_Development_and_Editing.md
lines: 58
sha256: 7a934623a8bf1d2ae054ed529b07691d7c62b89cd1a25a929bde366dcef22707
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Grid_Development_and_Editing.md — 판독 구간 기록

구간은 1행부터 58행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | Grid Development and Editing — 제목, 판본 표기, 빈 줄과 목차를 포함한다(1–18). ADCIRC 실행에 격자(mesh)의 fort.14 파일이 필요하다(5). 원문은 기존 격자의 사용·수정·신규 구축을 신중히 비교하라고 한다(5). 원문: `A mesh in the form of a [fort.14 file](/Fort.14_file) is required to run ADCIRC. This page presents basic info on options available to mesh construction end editing. For information on viewing meshes or other ADCIRC data, see [visualization](/Visualization). In many cases, a mesh may already exist to suite one's needs. Given the complexities and challenges associated with mesh construction, users should carefully weigh the merits of using an existing mesh, revising an existing mesh, or building a new one. ` (5). |
| 19–24 | Tools for ADCIRC Meshing / SMS — SMS는 Windows에서 ADCIRC 등의 모델 격자를 만들고 편집하고 보고 실행하는 상용 그래픽 프로그램이다(19–23). Aquaveo와 SMS 위키 안내 링크가 있다(23). |
| 25–49 | OceanMesh2D — GNU GPLv3.0의 MATLAB 기반 삼각 격자 자동 생성 도구를 소개한다(25–30). 격자 생성과 Courant 제약에 맞춘 검사·편집을 지원한다고 적는다(32–36). fort.13 속성, 조석 포텐셜(tidal potential)과 조석 수위 경계조건을 포함한 fort.15, fort.24 등의 입력 파일 생성을 열거한다(38–42). `msh` 컨테이너 저장, `plot` 시각화, ASCII fort.xx 내보내기를 열거한다(44–48). |
| 50–58 | Blue Kenue Contributor needed / References — 기여자를 구하는 Blue Kenue 절 제목 다음에 참고문헌 절이 나온다(50–52). OceanMesh2D 버전 자료, 격자 생성 논문, 사용자 안내서의 서지와 DOI를 적는다(54–58). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 50–52행: `Blue Kenue  Contributor needed` 절에는 설명 본문이 없다.
