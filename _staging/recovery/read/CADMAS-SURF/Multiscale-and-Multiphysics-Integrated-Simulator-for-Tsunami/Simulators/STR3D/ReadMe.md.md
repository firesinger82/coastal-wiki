---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/ReadMe.md
lines: 24
sha256: eb748ce05f5332c6a51ac26b77691650451dfd19380f5b85b83cd3ca367df6ed
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ReadMe.md — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | 기능 개요. 초기 정적 해석을 포함한 직접 과도응답해석(direct transient response analysis), Total Lagrange 기하 비선형, 탄소성 재료 비선형, 정·동 마찰 접촉을 적는다. 사면체·오면체·육면체의 1·2차 요소와 직사각형 단면 보 요소를 나열한다. Biot 식 기반 지반과 석조 재료, 병렬 계산 가능한 multifrontal 및 영역 분할 CG 해법을 적는다. 원문: `# STR-3D` (1); `**Outline of Functions**` (2); `1. Analysis type: Direct transient response analysis (static analysis is used initially)` (3); `2. Nonlinear analysis function: Geometric nonlinear (Total Lagrange method) Material nonlinear (elastoplastic) contact (static friction, dynamic friction)` (4); `3. Element library: Tetrahedron, pentahedron, hexahedron, each first-order and second-order element, beam element (rectangular cross section)` (5); `4. Special materials: Ground (based on Biot's formula), masonry materials` (6); `5. Matrix solver: Multifrontal method, domain-divided CG method (both can be calculated in parallel)` (7). |
| 8–13 | 다운로드·결합·전후처리 안내. Code의 Download ZIP을 안내한다. CADMAS-SURF/3D2F 결합 지원과 매뉴얼 참조를 적는다. Femap을 권장한다. 원문: `# How to download and compile STR3D` (8); `STR3D source code is stored in the in the Sourse code folder. You can download all the files by clicking on "Code" (green button on the top-right corner) and then select "Download ZIP".` (9); `# Coupled analysis with CADMAS-SURF/3D2F` (10); `Supports coupling with [CADMAS-SURF/3D2F](https://github.com/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/tree/main/Simulators/CADMAS-2F). You can find more details in the manual.` (11); `# Recommended pre and post-processors` (12); `+ Femap` (13). |
| 14–18 | 빌드 필수 라이브러리 목록. MUMPS·METIS·scalapack·BLAS의 원문 표기를 보존한다. 원문: `# Libraries required to build STR` (14); `+ MUMPS` (15); `+ METIS` (16); `+ scalapack` (17); `+ BLAS` (18). |
| 19–24 | 인용·주요 기능·연락처·문헌·Home 링크. 링크 대상 내용은 이 기록에서 판독하지 않았다. 원문: `# Important information about STR3D` (19); `+ [How to cite](https://github.com/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/wiki/How-to-cite)` (20); `+ [Main Features](https://github.com/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/wiki/Main-features(CADMAS%E2%80%90STR))` (21); `+ [Get in touch](https://github.com/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/wiki/Get-in-touch)` (22); `+ [Documentation](https://github.com/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/wiki/Papers-related-to-CADMAS%E2%80%90STR)` (23); `# If you want to know more about STR3D, go back to [Home](https://github.com/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/wiki)` (24). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11: 링크 표시는 CADMAS-SURF/3D2F이지만 URL 경로의 마지막 디렉터리는 CADMAS-2F이다.
